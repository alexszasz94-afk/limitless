# Video 1 - prompts

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_1.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

**THEXMASGLOW - CHRISTMAS PROJECTOR**
Working title: Christmas Projector

## Hook

she walks a Christmas-dressed big-box aisle and finds a pallet of TheXmasGlow — then the box opens at home and the whole house disappears under falling snow and fir trees.

## Planned cut

```
C01 → C02 → C03 → C04 → C05 → C06 → C07
C01 and C05 each cut two frames inside one clip
```

---

## C01 - Store aisle walk → the pallet

*Section:* Hook - store → shelf  
*Status:* IN THE CUT  
*Clip in the cut:* `v1_c01_g3.mp4`  
*What it is:* One clip, two frames: she pushes the cart down the aisle, then finds the pallet of TheXmasGlow cartons

- frames: `v1_c01_g1.png`, `v1_c01_r1.png`
- clips: `v1_c01_g1.mp4`, `v1_c01_g2.mp4`, `v1_c01_g3.mp4`

### FRAME 1 — STORE AISLE WALK

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `ref01.png` | framing + camera position + cart + pose |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
Copy the attached reference photo EXACTLY: same camera position, same height, same lens, same distance, same vertical 9:16 framing, same supermarket aisle receding into depth, same shelving on both sides, same floor, same ceiling lights, same shopping cart in the same spot and same angle, same body pose and same head turn. Change only two things. FIRST: the woman is now about 35 years old, natural everyday face, no makeup look, casual winter outfit, hair down, pushing the same cart in the same pose. SECOND: the store is now decorated for Christmas — garlands of green fir and red ribbon wrapped along the shelf edges, small warm white fairy lights strung across the aisle, a few red and gold baubles hanging from the ceiling, festive red and green product displays on the shelves. Everything else in the frame stays identical to the reference. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, natural realistic lighting, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
```

> **What we read off it:** Framing, cart and head-turn held. Store dressed with trees, garland and hanging baubles; aisle depth matches the source.

### FRAME 2 — PALLET OF OUR BOXES

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `ref02.png` | pallet framing + store context |
| @Image 2 | `box_festive_green_g2.png` | our carton — artwork, colour, proportions |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
Copy the FIRST attached reference photo's framing EXACTLY: same camera position, same height, same distance, same angle onto the retail shelf/pallet stacked full of identical product cartons, same vertical 9:16 crop, same surrounding store aisle and shelving visible at the edges, same lighting. Replace every carton on that shelf with OUR product box, shown in the SECOND attached reference: a tall upright rectangular tuck-top carton with a square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector standing on a separate white four-legged splayed stand base, a slim red remote printed beside it, a gold village skyline along the bottom. No transparent window anywhere on the carton. The boxes are stacked neatly, rows deep, all facing the camera, identical to each other. Same supermarket as the aisle reference, decorated for Christmas with fir garland and warm fairy lights along the shelf edge. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, natural realistic lighting, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
```

> **What we read off it:** Carton artwork is consistent across the whole stack and the wordmark reads. The printed projector render is simplified vs the packshot — fine at this distance, but do not treat this frame as the product reference.

### CLIP — SEEDANCE 2.5 · v1_c01_g3.mp4 · SUBMITTED 18:49

**Attached to this job**

| slot | file | why |
|---|---|---|
| start_image | `v1_c01_g1.png` | frame 0.0 s |
| image ref | `v1_c01_r1.png` | product / second reference |
| video ref | `scene_no_audio-1.mp4` | 3.93 s · silenced |

**Clip prompt — the one in the cut** - `seedance_2_5 · 720p · 4 s · 9:16 · audio on`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room plus the spoken line. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

TASK: image-to-video. The start image is frame 0.0s. Hold its wardrobe, store, lighting and lens exactly.

[1] SUMMARY
A woman in a supermarket Christmas aisle stops her trolley, reacts in shock and points off-camera; the camera whip-pans right onto a pallet of dark-green product boxes. Handheld vertical UGC. 4 seconds, one continuous take with one whip pan.

[2] GLOBAL STYLE
Real handheld phone footage filmed by a friend walking behind her. Natural retail lighting warmed by the red and gold decorations. Extremely sharp, clean, well exposed. Subtle handheld breathing throughout. The ONLY blur in the clip is the deliberate horizontal motion blur inside the whip pan. No cinematic grade, no film grain, no vignette, no slow motion.

[3] ASSET ROLES
The start image controls the woman's identity, her cream knit sweater and dark jeans, the aisle, the shelving and the lighting. @Image 1 controls ONLY the look of the product pallet the pan lands on: a tall stack of DARK-GREEN cartons with a red banner and a white projector illustration, with red poinsettia and garland on top. Do not copy camera angle or lighting from @Image 1. @Video 1 controls ONLY the camera path and the rhythm of the performance: walk, stop, hand to mouth, point, whip pan right, settle on the product stack. Do not copy the woman, her clothes, the trolley colour, the store or the boxes from @Video 1. @Video 1 is silent - there is no audio, no music and no soundtrack in it to copy.

[4] CHARACTERS
THE WOMAN - long light-brown hair, cream oatmeal knit sweater, dark jeans, seen from behind and slightly to her left. COUNT LOCK: exactly one person on screen for all 4 seconds. No other shoppers, no staff, no children.

[5] LOCATION - every one of these exists in the start image and must survive to the last frame before the pan: a wide polished pale-floor supermarket aisle; decorated Christmas trees with red and gold ornaments standing on top of the left-hand shelves; red baubles hanging from the ceiling; red-accented shelving on the right. THE TROLLEY - the dark grey shopping trolley she is pushing.

[6] FIRST FRAME - exactly the start image: THE WOMAN from behind and slightly left, both hands on THE TROLLEY handle, mid-aisle, walking away from camera.

[7] TIMELINE
0.0-1.0s - camera handheld, follows THE WOMAN from behind at walking pace; THE WOMAN pushes THE TROLLEY forward two steps.
1.0-2.0s - THE WOMAN releases the handle and takes one step forward ahead of THE TROLLEY. THE TROLLEY keeps rolling forward on its own down the aisle, unpushed. Her right hand flies up and covers her mouth; her head turns to her right; her shoulders lift. Camera holds.
2.0-3.0s - THE WOMAN drops the hand from her mouth and throws her right arm straight out, index finger pointing forward and to the right, off the right edge of frame. THE WOMAN speaks. Camera holds.
3.0-4.0s - as her arm reaches full extension the camera WHIP PANS hard to the right with heavy horizontal motion blur; THE WOMAN leaves frame to the left; the pan decelerates and settles on the tall pallet of DARK-GREEN product cartons from @Image 1 standing in the aisle with red poinsettia and garland on top. Tiny push-in and hold.

[8] DIALOGUE
English dialogue. THE WOMAN: "There is no way!" Spoken 2.1-2.9s. Delivery: loud, delighted, genuinely stunned, American accent. This spoken line is the ONLY voice in the clip. No subtitles, no on-screen text.

[9] CAMERA AND OPTICS - single continuous handheld take, vertical 9:16, normal wide-angle phone lens, chest height, about two metres behind THE WOMAN, her body in the centre-left third. One camera movement only: the whip pan right at 3.0s. Do not cut. Do not zoom. Do not orbit. No fisheye, no barrel distortion, no warped shelving or curved floor lines.

[10] LIGHTING - flat overhead retail lighting with warm pools under the decorations, clean white balance, no colour cast change across the clip.

[11] PHYSICS - THE TROLLEY rolls straight and slows gradually under its own momentum after she lets go; it never turns, never tips, never leaves the floor, never stops dead. Her sweater and hair move naturally with her turn.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: low supermarket room ambience, the rattle of trolley wheels on the hard floor, and her single spoken line. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - exactly one person. THE TROLLEY continues forward alone after 1.0s. The aisle, the decorated trees on the shelf tops and the hanging red baubles are present in every frame before the pan. The pan lands on cartons that are DARK GREEN with a red banner.
BANNED: any music, any song, any score, any soundtrack, any instrument, any singing; a second shopper, the trolley stopping dead or vanishing, THE WOMAN turning to face the camera, any cut, blue or white or brown or kraft boxes, a shelf of unrelated products, subtitles, on-screen text, slow motion, any blur outside the pan.
```

**Other takes**

Takes not used (2)v1_c01_g1.mp4 · 17:29 — First pass — hold the start frame · scene-1.mp4Promptjob b655c5a6CopyTASK: image-to-video. The start image is frame 0.0s. Hold its wardrobe, store, lighting and lens exactly.

[1] SUMMARY
A woman in a supermarket Christmas aisle stops her trolley, reacts in shock and points off-camera; the camera whip-pans right onto a pallet of dark-green product boxes. Handheld vertical UGC. 4 seconds, one continuous take with one whip pan.

[2] GLOBAL STYLE
Real handheld phone footage filmed by a friend walking behind her. Natural retail lighting warmed by the red and gold decorations. Extremely sharp, clean, well exposed. Subtle handheld breathing throughout. The ONLY blur in the clip is the deliberate horizontal motion blur inside the whip pan. No cinematic grade, no film grain, no vignette, no slow motion.

[3] ASSET ROLES
The start image controls the woman's identity, her cream knit sweater and dark jeans, the aisle, the shelving and the lighting. @Image 1 controls ONLY the look of the product pallet the pan lands on: a tall stack of DARK-GREEN cartons with a red banner and a white projector illustration, with red poinsettia and garland on top. Do not copy camera angle or lighting from @Image 1. @Video 1 controls ONLY the camera path and the rhythm of the performance: walk, stop, hand to mouth, point, whip pan right, settle on the product stack. Do not copy the woman, her clothes, the trolley colour, the store or the boxes from @Video 1.

[4] CHARACTERS
THE WOMAN - long light-brown hair, cream oatmeal knit sweater, dark jeans, seen from behind and slightly to her left. COUNT LOCK: exactly one person on screen for all 4 seconds. No other shoppers, no staff, no children.

[5] LOCATION - every one of these exists in the start image and must survive to the last frame before the pan: a wide polished pale-floor supermarket aisle; decorated Christmas trees with red and gold ornaments standing on top of the left-hand shelves; red baubles hanging from the ceiling; red-accented shelving on the right. THE TROLLEY - the dark grey shopping trolley she is pushing.

[6] FIRST FRAME - exactly the start image: THE WOMAN from behind and slightly left, both hands on THE TROLLEY handle, mid-aisle, walking away from camera.

[7] TIMELINE
0.0-1.0s - camera handheld, follows THE WOMAN from behind at walking pace; THE WOMAN pushes THE TROLLEY forward two steps.
1.0-2.0s - THE WOMAN releases the handle and takes one step forward ahead of THE TROLLEY. THE TROLLEY keeps rolling forward on its own down the aisle, unpushed. Her right hand flies up and covers her mouth; her head turns to her right; her shoulders lift. Camera holds.
2.0-3.0s - THE WOMAN drops the hand from her mouth and throws her right arm straight out, index finger pointing forward and to the right, off the right edge of frame. THE WOMAN speaks. Camera holds.
3.0-4.0s - as her arm reaches full extension the camera WHIP PANS hard to the right with heavy horizontal motion blur; THE WOMAN leaves frame to the left; the pan decelerates and settles on the tall pallet of DARK-GREEN product cartons from @Image 1 standing in the aisle with red poinsettia and garland on top. Tiny push-in and hold.

[8] DIALOGUE
English dialogue. THE WOMAN: "There is no way!" Spoken 2.1-2.9s. Delivery: loud, delighted, genuinely stunned, American accent. No subtitles, no on-screen text.

[9] CAMERA AND OPTICS - single continuous handheld take, vertical 9:16, normal wide-angle phone lens, chest height, about two metres behind THE WOMAN, her body in the centre-left third. One camera movement only: the whip pan right at 3.0s. Do not cut. Do not zoom. Do not orbit. No fisheye, no barrel distortion, no warped shelving or curved floor lines.

[10] LIGHTING - flat overhead retail lighting with warm pools under the decorations, clean white balance, no colour cast change across the clip.

[11] PHYSICS - THE TROLLEY rolls straight and slows gradually under its own momentum after she lets go; it never turns, never tips, never leaves the floor, never stops dead. Her sweater and hair move naturally with her turn.

[12] AUDIO - natural room sound only: supermarket ambience, trolley wheels on hard floor, her voice. No music, no score, no background song.

[13] POSITIVE LOCKS - exactly one person. THE TROLLEY continues forward alone after 1.0s. The aisle, the decorated trees on the shelf tops and the hanging red baubles are present in every frame before the pan. The pan lands on cartons that are DARK GREEN with a red banner.
BANNED: a second shopper, the trolley stopping dead or vanishing, THE WOMAN turning to face the camera, any cut, blue or white or brown or kraft boxes, a shelf of unrelated products, subtitles, on-screen text, music, slow motion, any blur outside the pan.v1_c01_g2.mp4 · 17:55 — Audio rule + motion fix · scene-1.mp4Promptjob 377edec4CopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room plus the spoken line. If any music appears anywhere in the 4 seconds the clip is wrong.

TASK: image-to-video. The start image is frame 0.0s. Hold its wardrobe, store, lighting and lens exactly.

[1] SUMMARY
A woman in a supermarket Christmas aisle stops her trolley, reacts in shock and points off-camera; the camera whip-pans right onto a pallet of dark-green product boxes. Handheld vertical UGC. 4 seconds, one continuous take with one whip pan.

[2] GLOBAL STYLE
Real handheld phone footage filmed by a friend walking behind her. Natural retail lighting warmed by the red and gold decorations. Extremely sharp, clean, well exposed. Subtle handheld breathing throughout. The ONLY blur in the clip is the deliberate horizontal motion blur inside the whip pan. No cinematic grade, no film grain, no vignette, no slow motion.

[3] ASSET ROLES
The start image controls the woman's identity, her cream knit sweater and dark jeans, the aisle, the shelving and the lighting. @Image 1 controls ONLY the look of the product pallet the pan lands on: a tall stack of DARK-GREEN cartons with a red banner and a white projector illustration, with red poinsettia and garland on top. Do not copy camera angle or lighting from @Image 1. @Video 1 controls ONLY the camera path and the rhythm of the performance: walk, stop, hand to mouth, point, whip pan right, settle on the product stack. Do not copy the woman, her clothes, the trolley colour, the store or the boxes from @Video 1. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] CHARACTERS
THE WOMAN - long light-brown hair, cream oatmeal knit sweater, dark jeans, seen from behind and slightly to her left. COUNT LOCK: exactly one person on screen for all 4 seconds. No other shoppers, no staff, no children.

[5] LOCATION - every one of these exists in the start image and must survive to the last frame before the pan: a wide polished pale-floor supermarket aisle; decorated Christmas trees with red and gold ornaments standing on top of the left-hand shelves; red baubles hanging from the ceiling; red-accented shelving on the right. THE TROLLEY - the dark grey shopping trolley she is pushing.

[6] FIRST FRAME - exactly the start image: THE WOMAN from behind and slightly left, both hands on THE TROLLEY handle, mid-aisle, walking away from camera.

[7] TIMELINE
0.0-1.0s - camera handheld, follows THE WOMAN from behind at walking pace; THE WOMAN pushes THE TROLLEY forward two steps.
1.0-2.0s - THE WOMAN releases the handle and takes one step forward ahead of THE TROLLEY. THE TROLLEY keeps rolling forward on its own down the aisle, unpushed. Her right hand flies up and covers her mouth; her head turns to her right; her shoulders lift. Camera holds.
2.0-3.0s - THE WOMAN drops the hand from her mouth and throws her right arm straight out, index finger pointing forward and to the right, off the right edge of frame. THE WOMAN speaks. Camera holds.
3.0-4.0s - as her arm reaches full extension the camera WHIP PANS hard to the right with heavy horizontal motion blur; THE WOMAN leaves frame to the left; the pan decelerates and settles on the tall pallet of DARK-GREEN product cartons from @Image 1 standing in the aisle with red poinsettia and garland on top. Tiny push-in and hold.

[8] DIALOGUE
English dialogue. THE WOMAN: "There is no way!" Spoken 2.1-2.9s. Delivery: loud, delighted, genuinely stunned, American accent. This spoken line is the ONLY voice in the clip. No subtitles, no on-screen text.

[9] CAMERA AND OPTICS - single continuous handheld take, vertical 9:16, normal wide-angle phone lens, chest height, about two metres behind THE WOMAN, her body in the centre-left third. One camera movement only: the whip pan right at 3.0s. Do not cut. Do not zoom. Do not orbit. No fisheye, no barrel distortion, no warped shelving or curved floor lines.

[10] LIGHTING - flat overhead retail lighting with warm pools under the decorations, clean white balance, no colour cast change across the clip.

[11] PHYSICS - THE TROLLEY rolls straight and slows gradually under its own momentum after she lets go; it never turns, never tips, never leaves the floor, never stops dead. Her sweater and hair move naturally with her turn.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: low supermarket room ambience, the rattle of trolley wheels on the hard floor, and her single spoken line. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - exactly one person. THE TROLLEY continues forward alone after 1.0s. The aisle, the decorated trees on the shelf tops and the hanging red baubles are present in every frame before the pan. The pan lands on cartons that are DARK GREEN with a red banner.
BANNED: any music, any song, any score, any soundtrack, any instrument, any singing; a second shopper, the trolley stopping dead or vanishing, THE WOMAN turning to face the camera, any cut, blue or white or brown or kraft boxes, a shelf of unrelated products, subtitles, on-screen text, slow motion, any blur outside the pan.

**Prompt** - `job b655c5a6`

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its wardrobe, store, lighting and lens exactly.

[1] SUMMARY
A woman in a supermarket Christmas aisle stops her trolley, reacts in shock and points off-camera; the camera whip-pans right onto a pallet of dark-green product boxes. Handheld vertical UGC. 4 seconds, one continuous take with one whip pan.

[2] GLOBAL STYLE
Real handheld phone footage filmed by a friend walking behind her. Natural retail lighting warmed by the red and gold decorations. Extremely sharp, clean, well exposed. Subtle handheld breathing throughout. The ONLY blur in the clip is the deliberate horizontal motion blur inside the whip pan. No cinematic grade, no film grain, no vignette, no slow motion.

[3] ASSET ROLES
The start image controls the woman's identity, her cream knit sweater and dark jeans, the aisle, the shelving and the lighting. @Image 1 controls ONLY the look of the product pallet the pan lands on: a tall stack of DARK-GREEN cartons with a red banner and a white projector illustration, with red poinsettia and garland on top. Do not copy camera angle or lighting from @Image 1. @Video 1 controls ONLY the camera path and the rhythm of the performance: walk, stop, hand to mouth, point, whip pan right, settle on the product stack. Do not copy the woman, her clothes, the trolley colour, the store or the boxes from @Video 1.

[4] CHARACTERS
THE WOMAN - long light-brown hair, cream oatmeal knit sweater, dark jeans, seen from behind and slightly to her left. COUNT LOCK: exactly one person on screen for all 4 seconds. No other shoppers, no staff, no children.

[5] LOCATION - every one of these exists in the start image and must survive to the last frame before the pan: a wide polished pale-floor supermarket aisle; decorated Christmas trees with red and gold ornaments standing on top of the left-hand shelves; red baubles hanging from the ceiling; red-accented shelving on the right. THE TROLLEY - the dark grey shopping trolley she is pushing.

[6] FIRST FRAME - exactly the start image: THE WOMAN from behind and slightly left, both hands on THE TROLLEY handle, mid-aisle, walking away from camera.

[7] TIMELINE
0.0-1.0s - camera handheld, follows THE WOMAN from behind at walking pace; THE WOMAN pushes THE TROLLEY forward two steps.
1.0-2.0s - THE WOMAN releases the handle and takes one step forward ahead of THE TROLLEY. THE TROLLEY keeps rolling forward on its own down the aisle, unpushed. Her right hand flies up and covers her mouth; her head turns to her right; her shoulders lift. Camera holds.
2.0-3.0s - THE WOMAN drops the hand from her mouth and throws her right arm straight out, index finger pointing forward and to the right, off the right edge of frame. THE WOMAN speaks. Camera holds.
3.0-4.0s - as her arm reaches full extension the camera WHIP PANS hard to the right with heavy horizontal motion blur; THE WOMAN leaves frame to the left; the pan decelerates and settles on the tall pallet of DARK-GREEN product cartons from @Image 1 standing in the aisle with red poinsettia and garland on top. Tiny push-in and hold.

[8] DIALOGUE
English dialogue. THE WOMAN: "There is no way!" Spoken 2.1-2.9s. Delivery: loud, delighted, genuinely stunned, American accent. No subtitles, no on-screen text.

[9] CAMERA AND OPTICS - single continuous handheld take, vertical 9:16, normal wide-angle phone lens, chest height, about two metres behind THE WOMAN, her body in the centre-left third. One camera movement only: the whip pan right at 3.0s. Do not cut. Do not zoom. Do not orbit. No fisheye, no barrel distortion, no warped shelving or curved floor lines.

[10] LIGHTING - flat overhead retail lighting with warm pools under the decorations, clean white balance, no colour cast change across the clip.

[11] PHYSICS - THE TROLLEY rolls straight and slows gradually under its own momentum after she lets go; it never turns, never tips, never leaves the floor, never stops dead. Her sweater and hair move naturally with her turn.

[12] AUDIO - natural room sound only: supermarket ambience, trolley wheels on hard floor, her voice. No music, no score, no background song.

[13] POSITIVE LOCKS - exactly one person. THE TROLLEY continues forward alone after 1.0s. The aisle, the decorated trees on the shelf tops and the hanging red baubles are present in every frame before the pan. The pan lands on cartons that are DARK GREEN with a red banner.
BANNED: a second shopper, the trolley stopping dead or vanishing, THE WOMAN turning to face the camera, any cut, blue or white or brown or kraft boxes, a shelf of unrelated products, subtitles, on-screen text, music, slow motion, any blur outside the pan.
```

**Prompt** - `job 377edec4`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room plus the spoken line. If any music appears anywhere in the 4 seconds the clip is wrong.

TASK: image-to-video. The start image is frame 0.0s. Hold its wardrobe, store, lighting and lens exactly.

[1] SUMMARY
A woman in a supermarket Christmas aisle stops her trolley, reacts in shock and points off-camera; the camera whip-pans right onto a pallet of dark-green product boxes. Handheld vertical UGC. 4 seconds, one continuous take with one whip pan.

[2] GLOBAL STYLE
Real handheld phone footage filmed by a friend walking behind her. Natural retail lighting warmed by the red and gold decorations. Extremely sharp, clean, well exposed. Subtle handheld breathing throughout. The ONLY blur in the clip is the deliberate horizontal motion blur inside the whip pan. No cinematic grade, no film grain, no vignette, no slow motion.

[3] ASSET ROLES
The start image controls the woman's identity, her cream knit sweater and dark jeans, the aisle, the shelving and the lighting. @Image 1 controls ONLY the look of the product pallet the pan lands on: a tall stack of DARK-GREEN cartons with a red banner and a white projector illustration, with red poinsettia and garland on top. Do not copy camera angle or lighting from @Image 1. @Video 1 controls ONLY the camera path and the rhythm of the performance: walk, stop, hand to mouth, point, whip pan right, settle on the product stack. Do not copy the woman, her clothes, the trolley colour, the store or the boxes from @Video 1. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] CHARACTERS
THE WOMAN - long light-brown hair, cream oatmeal knit sweater, dark jeans, seen from behind and slightly to her left. COUNT LOCK: exactly one person on screen for all 4 seconds. No other shoppers, no staff, no children.

[5] LOCATION - every one of these exists in the start image and must survive to the last frame before the pan: a wide polished pale-floor supermarket aisle; decorated Christmas trees with red and gold ornaments standing on top of the left-hand shelves; red baubles hanging from the ceiling; red-accented shelving on the right. THE TROLLEY - the dark grey shopping trolley she is pushing.

[6] FIRST FRAME - exactly the start image: THE WOMAN from behind and slightly left, both hands on THE TROLLEY handle, mid-aisle, walking away from camera.

[7] TIMELINE
0.0-1.0s - camera handheld, follows THE WOMAN from behind at walking pace; THE WOMAN pushes THE TROLLEY forward two steps.
1.0-2.0s - THE WOMAN releases the handle and takes one step forward ahead of THE TROLLEY. THE TROLLEY keeps rolling forward on its own down the aisle, unpushed. Her right hand flies up and covers her mouth; her head turns to her right; her shoulders lift. Camera holds.
2.0-3.0s - THE WOMAN drops the hand from her mouth and throws her right arm straight out, index finger pointing forward and to the right, off the right edge of frame. THE WOMAN speaks. Camera holds.
3.0-4.0s - as her arm reaches full extension the camera WHIP PANS hard to the right with heavy horizontal motion blur; THE WOMAN leaves frame to the left; the pan decelerates and settles on the tall pallet of DARK-GREEN product cartons from @Image 1 standing in the aisle with red poinsettia and garland on top. Tiny push-in and hold.

[8] DIALOGUE
English dialogue. THE WOMAN: "There is no way!" Spoken 2.1-2.9s. Delivery: loud, delighted, genuinely stunned, American accent. This spoken line is the ONLY voice in the clip. No subtitles, no on-screen text.

[9] CAMERA AND OPTICS - single continuous handheld take, vertical 9:16, normal wide-angle phone lens, chest height, about two metres behind THE WOMAN, her body in the centre-left third. One camera movement only: the whip pan right at 3.0s. Do not cut. Do not zoom. Do not orbit. No fisheye, no barrel distortion, no warped shelving or curved floor lines.

[10] LIGHTING - flat overhead retail lighting with warm pools under the decorations, clean white balance, no colour cast change across the clip.

[11] PHYSICS - THE TROLLEY rolls straight and slows gradually under its own momentum after she lets go; it never turns, never tips, never leaves the floor, never stops dead. Her sweater and hair move naturally with her turn.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: low supermarket room ambience, the rattle of trolley wheels on the hard floor, and her single spoken line. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - exactly one person. THE TROLLEY continues forward alone after 1.0s. The aisle, the decorated trees on the shelf tops and the hanging red baubles are present in every frame before the pan. The pan lands on cartons that are DARK GREEN with a red banner.
BANNED: any music, any song, any score, any soundtrack, any instrument, any singing; a second shopper, the trolley stopping dead or vanishing, THE WOMAN turning to face the camera, any cut, blue or white or brown or kraft boxes, a shelf of unrelated products, subtitles, on-screen text, slow motion, any blur outside the pan.
```

---

## C02 - Box on the table

*Section:* B-roll 1 - the product  
*Status:* IN THE CUT  
*Clip in the cut:* `v1_c02_g3.mp4`  
*What it is:* Two hands on the carton, festive wooden table

- frames: `v1_c02_g1.png`
- clips: `v1_c02_g1.mp4`, `v1_c02_g2.mp4`, `v1_c02_g3.mp4`

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `ref03.png` | hands, grip, table, camera angle |
| @Image 2 | `box_festive_green_g2.png` | our carton — artwork, colour, proportions |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same wooden table surface, same two hands resting on the box in the same position and same grip, same arms entering frame the same way, same background depth. Replace the box with OUR product box from the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle the original box occupied. Dress the wooden table more festively: a sprig of fir and a few red berries, two or three small gold and red baubles, a short cream candle, a soft warm string light trailing across the wood, all at the edges of frame so the box stays the clear subject. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, natural realistic lighting, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
```

> **What we read off it:** Best packaging read of the set — headline, wordmark and the 16 Patterns / Remote Control / Timer strip all legible. Table dressing sits at the edges so the carton stays the subject.

### CLIP — SEEDANCE 2.5 · v1_c02_g3.mp4 · SUBMITTED 18:44

**Attached to this job**

| slot | file | why |
|---|---|---|
| start_image | `v1_c02_g1.png` | frame 0.0 s |
| video ref | `scene_no_audio-2.mp4` | 2.13 s · silenced |

**Clip prompt — the one in the cut** - `seedance_2_5 · 720p · 4 s · 9:16 · audio on`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

EXIT RULE - SECOND MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - THIRD MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a wooden table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, gold THEXMASGLOW banner, the words CHRISTMAS LIGHT PROJECTOR, a white projector on a red circle. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray, no window.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a cream knit sleeve on the left wrist, a thin gold bracelet on the right wrist.

[5] LOCATION - a dark round wooden table fills the frame. A lit cream pillar candle sits at the top left, holly sprigs with red berries beside it, warm fairy lights out of focus behind. The candle, the holly and the fairy lights must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the wooden table, lid flaps folded back, with the candle, the holly and the fairy lights still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle or the holly disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
```

**Other takes**

Takes not used (2)v1_c02_g1.mp4 · 17:29 — First pass — hold the start frame · scene-2.mp4Promptjob 28aba27cCopyTASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a wooden table and lift the white projector straight up out of it. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics and rhythm of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, gold THEXMASGLOW banner, the words CHRISTMAS LIGHT PROJECTOR, a white projector on a red circle. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray, no window.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a cream knit sleeve on the left wrist, a thin gold bracelet on the right wrist.

[5] LOCATION - a dark round wooden table fills the frame. A lit cream pillar candle sits at the top left, holly sprigs with red berries beside it, warm fairy lights out of focus behind. The candle, the holly and the fairy lights must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE
0.0-1.0s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it; the tuck tongue releases out of the front panel.
1.0-2.0s - the lid flaps fold upward and backward away from camera on the rear fold, staying attached to THE BOX, opening the top; the dark interior comes into view.
2.0-3.0s - both HANDS reach down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is now clearly visible.
3.0-4.0s - THE HANDS lift THE PROJECTOR straight up and out of THE BOX in one smooth vertical move until it clears the rim and is held above the open carton, white dome and BLACK top face facing camera.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift.

[12] AUDIO - natural room sound only: cardboard flaps, fingers on the carton. No music, no speech, no score.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands. The top face of THE PROJECTOR is BLACK.
BANNED: an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle or the holly disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text, music.v1_c02_g2.mp4 · 17:55 — Audio rule + motion fix · scene-2.mp4Promptjob 6614d81eCopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

SPEED RULE - SECOND MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift of the product out of the box is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a wooden table and lift the white projector briskly straight up out of it. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, gold THEXMASGLOW banner, the words CHRISTMAS LIGHT PROJECTOR, a white projector on a red circle. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray, no window.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a cream knit sleeve on the left wrist, a thin gold bracelet on the right wrist.

[5] LOCATION - a dark round wooden table fills the frame. A lit cream pillar candle sits at the top left, holly sprigs with red berries beside it, warm fairy lights out of focus behind. The candle, the holly and the fairy lights must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.1s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second.
3.1-4.0s - THE PROJECTOR is held steady above the open carton, white dome and BLACK top face square to camera, with a small natural settle of the hands.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast.
BANNED: any music, any song, any score, any soundtrack; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle or the holly disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.

**Prompt** - `job 28aba27c`

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a wooden table and lift the white projector straight up out of it. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics and rhythm of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, gold THEXMASGLOW banner, the words CHRISTMAS LIGHT PROJECTOR, a white projector on a red circle. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray, no window.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a cream knit sleeve on the left wrist, a thin gold bracelet on the right wrist.

[5] LOCATION - a dark round wooden table fills the frame. A lit cream pillar candle sits at the top left, holly sprigs with red berries beside it, warm fairy lights out of focus behind. The candle, the holly and the fairy lights must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE
0.0-1.0s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it; the tuck tongue releases out of the front panel.
1.0-2.0s - the lid flaps fold upward and backward away from camera on the rear fold, staying attached to THE BOX, opening the top; the dark interior comes into view.
2.0-3.0s - both HANDS reach down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is now clearly visible.
3.0-4.0s - THE HANDS lift THE PROJECTOR straight up and out of THE BOX in one smooth vertical move until it clears the rim and is held above the open carton, white dome and BLACK top face facing camera.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift.

[12] AUDIO - natural room sound only: cardboard flaps, fingers on the carton. No music, no speech, no score.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands. The top face of THE PROJECTOR is BLACK.
BANNED: an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle or the holly disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text, music.
```

**Prompt** - `job 6614d81e`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

SPEED RULE - SECOND MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift of the product out of the box is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a wooden table and lift the white projector briskly straight up out of it. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, gold THEXMASGLOW banner, the words CHRISTMAS LIGHT PROJECTOR, a white projector on a red circle. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray, no window.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a cream knit sleeve on the left wrist, a thin gold bracelet on the right wrist.

[5] LOCATION - a dark round wooden table fills the frame. A lit cream pillar candle sits at the top left, holly sprigs with red berries beside it, warm fairy lights out of focus behind. The candle, the holly and the fairy lights must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.1s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second.
3.1-4.0s - THE PROJECTOR is held steady above the open carton, white dome and BLACK top face square to camera, with a small natural settle of the hands.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast.
BANNED: any music, any song, any score, any soundtrack; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle or the holly disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
```

---

## C03 - Product in hand — kitchen

*Section:* B-roll 1 - the product  
*Status:* IN THE CUT  
*Clip in the cut:* `v1_c03_g2.mp4`  
*What it is:* Held in the air over the marble island, black mesh lens up

- frames: `v1_c03_g1.png`
- clips: `v1_c03_g1.mp4`, `v1_c03_g2.mp4`

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `ref04.png` | the whole shot — camera, hands, product, and the countertop in the lower right |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
COPY @Image 1 EXACTLY. The ONLY thing that changes is the kitchen behind her. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, the jewellery, the sleeve, and the white marble countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the bright white marble countertop occupies the LOWER RIGHT of the frame as a clean pale wedge running diagonally, passing behind and below her right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE — her two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but her fingers, with a visible gap of air between the base of the stand and the marble below. Left forearm enters from the lower left in a cream ribbed knit sleeve pushed back; right forearm enters from the right with a thin gold bangle at the wrist and two slim gold rings on the fingers. Fair skin, neat natural nails.

SCALE AND PLACEMENT — the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT — a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER — honed white marble with soft cool-grey veining and a squared edge, matte sheen.

THE KITCHEN — this is the only change. A warm modern kitchen, softly defocused: pale greige flat-front shaker cabinets with slim brushed-brass bar pulls, a stainless steel wall oven built into the tall cabinet run on the left, a white marble slab backsplash, a warm white LED strip glowing under the upper cabinets, and a pine garland with small warm fairy lights running high along the top of the cabinetry. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfectly exposed, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

> **What we read off it:** g3 — my prompt was the bug, not the model. g2 described the background as “a warm modern kitchen, softly out of focus” and never once mentioned the countertop, so the model dropped it and filled the bottom half with floor. It rendered exactly what was asked. g3 names the counter as a thing that must be in frame, says where it sits, and bans the failure outright — “DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.” The counter block and the kitchen block are now word for word identical in C03 and C04 so both shots read as the same island.

### CLIP — SEEDANCE 2.5 · v1_c03_g2.mp4 · SUBMITTED 17:55

**Attached to this job**

| slot | file | why |
|---|---|---|
| start_image | `v1_c03_g1.png` | frame 0.0 s |

**Clip prompt — the one in the cut** - `seedance_2_5 · 720p · 4 s · 9:16 · audio on`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the marble the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a marble kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the marble counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the marble until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the marble. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the marble in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the marble; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm under-cabinet light plus soft daylight, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The marble is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the marble, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
```

**Other takes**

Takes not used (1)v1_c03_g1.mp4 · 17:29 — First pass — hold the start framePromptjob cccb6cf2CopyTASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two hands raise the white projector high above a marble kitchen counter, then lower it slowly and set it down. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands holding THE PROJECTOR, entering from the bottom of frame.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the marble counter.

[7] TIMELINE
0.0-1.0s - camera locked. THE HANDS raise THE PROJECTOR straight upward, away from the marble, until the bottom of the stand is roughly 35 cm above the counter. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the marble. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
1.0-3.0s - THE HANDS lower THE PROJECTOR in one long, slow, continuous straight vertical descent toward the marble. The travel is deliberate and unbroken. No hesitation, no wobble, no sideways drift, no rotation.
3.0-3.5s - the four feet of the stand touch the marble and settle. Tiny compression, no bounce, no slide.
3.5-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm under-cabinet light plus soft daylight, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with weight; it stays perfectly upright and level through the whole descent. The marble is hard: contact is a small firm settle.

[12] AUDIO - natural room sound only: a soft contact tap when the stand meets the marble. No music, no speech, no score.

[13] POSITIVE LOCKS - the countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent is long and slow, not a short drop.
BANNED: the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping or rotating, the camera moving, a cut, subtitles, on-screen text, music.

**Prompt** - `job cccb6cf2`

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two hands raise the white projector high above a marble kitchen counter, then lower it slowly and set it down. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands holding THE PROJECTOR, entering from the bottom of frame.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the marble counter.

[7] TIMELINE
0.0-1.0s - camera locked. THE HANDS raise THE PROJECTOR straight upward, away from the marble, until the bottom of the stand is roughly 35 cm above the counter. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the marble. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
1.0-3.0s - THE HANDS lower THE PROJECTOR in one long, slow, continuous straight vertical descent toward the marble. The travel is deliberate and unbroken. No hesitation, no wobble, no sideways drift, no rotation.
3.0-3.5s - the four feet of the stand touch the marble and settle. Tiny compression, no bounce, no slide.
3.5-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm under-cabinet light plus soft daylight, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with weight; it stays perfectly upright and level through the whole descent. The marble is hard: contact is a small firm settle.

[12] AUDIO - natural room sound only: a soft contact tap when the stand meets the marble. No music, no speech, no score.

[13] POSITIVE LOCKS - the countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent is long and slow, not a short drop.
BANNED: the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping or rotating, the camera moving, a cut, subtitles, on-screen text, music.
```

---

## C04 - Same kitchen — plugging in

*Section:* B-roll 1 - the product  
*Status:* IN THE CUT  
*Clip in the cut:* `v1_c04_g1.mp4`  
*What it is:* Close over the marble, cable about to go into the port at the base

- frames: `v1_c04_g1.png`
- clips: `v1_c04_g1.mp4`, `v1_c04_g2.mp4`

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `ref05.png` | the whole shot — camera distance and tilt, both hands, the cable, product scale |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
COPY @Image 1 EXACTLY. The ONLY thing that changes is the kitchen behind her. Everything else is a literal copy.

CAMERA — this is the part that went wrong last time, so follow it precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently — a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The marble surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT — standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS — exactly as in @Image 1. Her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; on that wrist a stack of thin gold bangles, beige ribbed knit sleeve pushed back. Her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. Two slim gold rings on that hand. The white cable trails away to the right across the marble and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER — honed white marble with soft cool-grey veining and a squared edge, matte sheen.

THE KITCHEN — this is the only change. A warm modern kitchen, softly defocused across the top third of the frame: pale greige flat-front shaker cabinets with slim brushed-brass bar pulls, a stainless steel wall oven built into the tall cabinet run on the right, a white marble slab backsplash, a warm white LED strip glowing under the upper cabinets, and a pine garland with small warm fairy lights running high along the top of the cabinetry. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfectly exposed, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

> **What we read off it:** g3 — I mis-read the reference, then wrote the mistake into the prompt. ref05 is a close, shallow downward angle with the product large in frame. I described it as “a HIGH DOWNWARD ANGLE… tilted down roughly 45 degrees… small in frame with a lot of counter around it” — and the model delivered that faithfully. The lesson is to describe the reference from the reference, not from memory of it. g3 leads with the camera, says the angle is shallow and the product large, and bans the four ways it went wrong by name. Two jobs wasted on a reference that was open in front of me the whole time.

### CLIP — SEEDANCE 2.5 · v1_c04_g1.mp4 · SUBMITTED 17:29

**Attached to this job**

| slot | file | why |
|---|---|---|
| start_image | `v1_c04_g1.png` | frame 0.0 s |

**Clip prompt — the one in the cut** - `seedance_2_5 · 720p · 4 s · 9:16 · audio on`

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a hand wearing a stack of gold bangles, resting on the left side of the dome. It does not move.
THE RIGHT HAND - a hand wearing gold rings, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the white marble around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the marble. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the marble immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
```

**Other takes**

Takes not used (1)v1_c04_g2.mp4 · 17:55 — Audio rule + motion fixPromptjob eaf23f27CopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a hand wearing a stack of gold bangles, resting on the left side of the dome. It does not move.
THE RIGHT HAND - a hand wearing gold rings, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the white marble around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the marble. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the marble immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a small plastic click as the connector seats, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: any music, any song, any score, any soundtrack; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text.

**Prompt** - `job eaf23f27`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a hand wearing a stack of gold bangles, resting on the left side of the dome. It does not move.
THE RIGHT HAND - a hand wearing gold rings, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the white marble around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the marble. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the marble immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a small plastic click as the connector seats, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: any music, any song, any score, any soundtrack; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text.
```

---

## C05 - Hand on the door → the reveal

*Section:* B-roll 2 - the payoff  
*Status:* IN THE CUT  
*Clip in the cut:* `v1_c05_g5.mp4`  
*What it is:* One clip, two frames: the door is shut tight on the far side, then it opens on the room under full projection

- frames: `v1_c05_g1.png`, `v1_c05_r2.png`
- clips: `v1_c05_g1.mp4`, `v1_c05_g2.mp4`, `v1_c05_g3.mp4`, `v1_c05_g4.mp4`, `v1_c05_g5.mp4`, `v1_c05_g6.mp4`, `v1_c05_g7.mp4`

### FRAME 1 — HAND ON THE DOOR

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `v1_c05_g1.png` | our own g1 — door, wreath, knob, hallway, hand and camera all held; only the light leak changes |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
Recreate @Image 1 with ONE change.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same white panelled door, the same antique brass round doorknob, the same small pine wreath with the red velvet bow on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position, the same warm low-key evening light.

THE CHANGE: the door is now FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out — no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
```

> **What we read off it:** g2 — fixed. g1 ran a full-height rainbow strip down the door edge, which gives the reveal away before the cut. Door is now flush and the seam is a plain shadow line. Feeding our own g1 back as the reference held the wreath, knob and hand exactly — far tighter than re-describing the hallway from scratch.

### FRAME 2 — THE REVEAL

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `v1_c05_r2.png` | our own g1 — room, projection, tree, sofa and camera all held; the projector unit and the boy change |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same tall living room, the same Christmas light projection covering every wall and the ceiling — glowing Christmas trees, snowflakes, stars, baubles and candy canes in gold, green, red and blue — the same decorated tree, the same stockings on the mantel, the same white shelving, the same cream sofa with red tartan cushions, the same wrapped gifts, the same tall window on the left, the same camera position and height, the same magical low-key evening light.

CHANGE 1 — the projector unit must NOT be visible. Remove the small white glowing device and its little side table from the lower left completely. Replace that corner with plain floor and the edge of the rug. No projector anywhere in frame.

CHANGE 2 — the boy now stands TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder. The girl beside him stays exactly as she is, seen from behind, still looking up at the projected wall.

Both children are fully dressed in warm red-and-white knitted Christmas jumpers and matching knitted lounge trousers with thick socks. Wholesome family Christmas scene.

Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
```

> **What we read off it:** g2 — fixed. Projector and its side table are gone from the lower left, and the boy has turned front-on so there is a face in the reveal. Girl left from behind on purpose — one turned, one not, reads as caught rather than posed. Wardrobe wording kept as “knitted jumper + lounge trousers” to stay clear of the NSFW filter; it still reads as pyjamas.

### CLIP — SEEDANCE 2.5 · v1_c05_g5.mp4 · SUBMITTED 19:21

**Attached to this job**

| slot | file | why |
|---|---|---|
| start_image | `v1_c05_g1.png` | frame 0.0 s |
| image ref | `v1_c05_r2.png` | product / second reference |
| video ref | `scene_no_audio-5.mp4` | silenced, padded to 4.5 s @ 1080×1920 |

**Clip prompt — the one in the cut** - `seedance_2_5 · 720p · 4 s · 9:16 · audio on`

```text
RULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on the walls and on the ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the way the whole field of glowing shapes slides and swarms across the plaster without ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

WHAT THE LIGHT DOES, described so it cannot be mistaken for a texture:
- The whole field of glowing shapes SLIDES BODILY across the wall and across the ceiling, the way light from a spinning projector head sweeps a room. It never locks onto the plaster.
- On top of that sliding, individual shapes POUR DOWNWARD like heavy snowfall filmed through a window at night, and each one spins slowly as it goes and drags a faint soft trail.
- SPEED: a single shape crosses the full height of the wall in ABOUT ONE SECOND. That is fast. A viewer must see it moving within the first quarter second of the clip.
- THE TEST: take any two frames a third of a second apart and lay them on top of each other. NOT ONE glowing shape is in the same place. Not one. If any shape has stayed put, the clip is wrong.
- The moving light also pours down over the tree, the sofa, the floor and across both children's faces and pyjamas as it passes over them, so the brightness on everything in the room is changing continuously.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, doors, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

IMAGE QUALITY RULE - SECOND MOST IMPORTANT. The finished clip must look at least as sharp and as clean as the start image. Do not soften it, do not smear it, do not repaint it, do not re-imagine it. Hold the exact sharpness, exposure, contrast and fine detail of the start image: the wood grain of the floor, the panel edges and painted sheen of the white door, the brass of the round knob, the skin texture and fine hairs of the bare forearm, the individual leaves of the green wreath and its red bow. Crisp modern phone footage, in focus from the first frame to the last. BANNED: blur, soft focus, haze, motion smear on objects that are not moving, mushy low-detail surfaces, plastic or waxy skin, a repainted or re-imagined door or hallway, colour shift, washed-out or muddy exposure, upscaling artefacts, a dreamy or filtered look.

AUDIO RULE - THIRD MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

CHILDREN MOTION RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light is sweeping and pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the moving projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children and their red-and-white Fair Isle pyjamas, and the COLOUR and STYLE of the Christmas shapes.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.
Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: tall decorated Christmas tree centre, cream sofa with a knit throw right, tall windows left, patterned rug, presents under the tree. Sweeping, pouring light covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured light appears along the opening edge. Through that slice, glowing shapes are clearly seen racing downward and sideways past the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light is sweeping across the far wall and the tree and raining down over the floor ahead and over the camera's own path.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the field of light keeps sliding and pouring down every wall and across both children, shapes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The light is sweeping and pouring across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the moving projection as the only bright light source. Because the shapes are sweeping and pouring, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Pyjamas and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
```

**Other takes**

Takes not used (6)v1_c05_g1.mp4 · 17:29 — First pass — hold the start frame · scene-5.mp4Promptjob 185cbfbcCopyTASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two laughing children inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. @Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children, their red-and-white Fair Isle pyjamas, and the style and colour of the projected Christmas patterns. Do not copy @Image 1's camera angle or framing. @Video 1 controls ONLY the camera path and the rhythm: hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway into the room, then tilts up. Do NOT copy the room, the furniture, the children, the blue colour, or anything projected from @Video 1.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing centre of the room facing camera, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Projected Christmas shapes - snowflakes, stars, small fir trees and candy canes in gold, green, red and blue - cover the walls AND the ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured moving light appears along the opening edge.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; coloured projected shapes sweep across the floor ahead.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY stands centre facing camera, mouth wide open laughing, arms out, bouncing on his toes. THE GIRL is behind him to the left, turning and laughing. Snowflakes, stars, small fir trees and candy canes drift and rotate continuously across the walls.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same Christmas shapes drift and swirl across the ceiling too. THE BOY jumps once with both arms straight up.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the projection as the only bright moving light source. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The children's pyjamas and hair move naturally with their motion.

[12] AUDIO - natural room sound only: the door handle, the door swinging, children laughing and squealing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across walls and ceiling. Exactly two children. The reveal shows CHRISTMAS imagery only.
BANNED: jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; a frozen still pattern; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text; music.v1_c05_g2.mp4 · 17:55 — Audio rule + motion fix · scene-5.mp4Promptjob af3cd11dCopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. They are never standing still, never posed, never frozen, never waiting. They are running, spinning, jumping and laughing continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Their faces are fully alive: eyes wide, mouths open laughing and shouting. This must look like real children filmed on a phone, not like a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two children running and laughing inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. Documentary realism, extremely natural. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. @Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children, their red-and-white Fair Isle pyjamas, and the style and colour of the projected Christmas patterns. Do not copy @Image 1's camera angle or framing, and do not copy its stillness - @Image 1 is a photograph, this clip must move. @Video 1 controls ONLY the camera path and the rhythm: hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway into the room, then tilts up. Do NOT copy the room, the furniture, the children, the blue colour, or anything projected from @Video 1. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, in the centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Moving projected Christmas shapes - snowflakes, stars, small fir trees and candy canes in gold, green, red and blue - cover the walls AND the whole ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured MOVING light appears along the opening edge, shapes visibly sliding through that slice.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; coloured projected shapes sweep across the floor ahead and travel over the camera's own path.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps up onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Snowflakes, stars, fir trees and candy canes drift, rotate and sweep continuously across every wall.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same Christmas shapes drift and swirl across the entire ceiling, corner to corner, still moving. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the moving projection as the only bright light source, so the light on the walls, the furniture and the children is constantly shifting and sliding. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The sofa cushion compresses when THE BOY lands. The children's pyjamas and hair swing and lift with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the walls and the ceiling. Both children are in full motion from the moment they appear. The reveal shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; children standing still, posed or frozen; jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.v1_c05_g3.mp4 · 18:14 — Audio rule + motion fix · scene-5.mp4Promptjob cdc7911bCopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the wall and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the main wall:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - the stars, the candy canes, the small fir trees, the baubles - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the furniture, the tree and the children's faces and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. They are never standing still, never posed, never frozen, never waiting. They are running, spinning, jumping and laughing continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Their faces are fully alive: eyes wide, mouths open laughing and shouting. This must look like real children filmed on a phone, not like a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two children running and laughing inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. Documentary realism, extremely natural. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. It is a photograph, so it shows the projection frozen - do NOT copy that stillness, the projection in this clip must travel.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children and their red-and-white Fair Isle pyjamas, and the COLOUR and STYLE of the Christmas shapes. It is also a photograph - copy its look, never its stillness.
@Video 1 IS THE MOTION AUTHORITY. Copy from it exactly two things: first, the camera path and rhythm - hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway, then tilts up; and second, and most important, HOW THE PROJECTED LIGHT TRAVELS - the speed at which the projected shapes slide across the walls and ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the floor, the furniture and the people. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes, small fir trees and baubles in gold, green, red and blue. Do NOT copy its room, its furniture, its people, its flat blue colour, its captions or its audio.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, in the centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Travelling projected Christmas shapes cover the walls AND the whole ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured light appears along the opening edge, with shapes visibly sliding downward through that slice.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; projected shapes sweep across the floor ahead and travel over the camera's own path.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps up onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. The whole projected field keeps sliding down and to the right across every wall and across both children.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same shapes slide across the entire ceiling in the same direction at the same speed. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the travelling projection as the only bright light source. Because the field is sliding, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The sofa cushion compresses when THE BOY lands. The children's pyjamas and hair swing and lift with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - every projected shape changes position on the surface in every single frame. Both children are in full motion from the moment they appear. The reveal shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; children standing still, posed or frozen; jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.v1_c05_g4.mp4 · 18:44 — Audio rule + motion fixPromptjob d447d883CopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
The walls and the entire ceiling of this room are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes, tiny fir trees and baubles in gold, green, red and blue - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the tree, the sofa, the floor and across the children's faces and pyjamas as it passes over them, so the light on everything in the room is constantly shifting.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light-snow is pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the falling projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children and their red-and-white Fair Isle pyjamas, and the COLOUR and STYLE of the Christmas shapes. Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: tall decorated Christmas tree centre, cream sofa with a knit throw right, tall windows left, patterned rug, presents under the tree. Falling light-snow covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured light appears along the opening edge. Through that slice, glowing shapes are clearly seen POURING DOWNWARD past the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light-snow is raining down across the far wall and the tree, and falls over the floor ahead and over the camera's own path.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the light-snow keeps pouring steadily down every wall and across both children, flakes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The snow is falling across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the falling projection as the only bright light source. Because the shapes are pouring down, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Pyjamas and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the walls and on the ceiling; a viewer can follow individual flakes travelling downward. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; snow that falls for a moment then stops; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.v1_c05_g6.mp4 · 19:36 — Rule 1 — the light on the walls movesPromptjob 20993c33CopyRULE 1 - THE LIGHT ON THE WALLS AND CEILING MOVES. THIS IS THE WHOLE POINT OF THE CLIP.
Light this room the way a SPINNING MIRROR BALL lights a room. The projector head is TURNING - one slow revolution every three seconds - so every glowing Christmas shape it throws SWEEPS BODILY across the walls and across the ceiling, travelling sideways, bending over corners and running up onto the ceiling. Nothing is painted on. Nothing holds still.
On top of that sweep, the shapes also DRIFT DOWNWARD like heavy snow past a window at night, each one slowly turning as it goes.
SPEED: one shape crosses the whole wall in ONE SECOND. Movement is obvious within the first quarter-second of the clip.
THE TEST: two frames a third of a second apart share NO shape in the same place. Not one.
The start image is a single PAUSED frame of this moving light. At 0.0s it un-pauses and the light never stops again.
"Match the start image" means the room, the door, the people and the colours - NOT where the light sits. The light must leave its starting position instantly.
The moving light also washes across the tree, the sofa, the floor and both children's faces and pyjamas, so the brightness on everything keeps changing.

RULE 2 - SHARPNESS. The clip must be at least as sharp and clean as the start image: the wood grain of the floor, the panel edges of the white door, the brass knob, the skin and fine hairs of the bare forearm, the leaves of the green wreath. Crisp phone footage, in focus throughout. No blur, no haze, no soft focus, no waxy skin, no repainted door, no colour shift, no washed-out exposure.

RULE 3 - NO MUSIC OF ANY KIND. No song, score, soundtrack, melody, instruments, singing or festive music bed. Only real room sound: the door handle and door swinging, children laughing and squealing, quiet room tone.

TASK: image-to-video, 4 seconds, one continuous handheld phone POV take, vertical 9:16, normal wide-angle lens at eye height. The start image is frame 0.0s.

THE SHOT: first-person POV. A bare right forearm turns the brass knob and pushes the white panelled door open; the camera walks through into a warm double-height Christmas living room and tilts up to the ceiling.

WHAT IS IN THE ROOM (from @Image 1): tall decorated Christmas tree centre, cream sofa with a knit throw on the right, tall windows left, patterned rug, presents. Exactly TWO children - THE BOY and THE GIRL, both in matching red-and-white Fair Isle pyjamas. No adults, no third child, no pets.

TIMELINE - the light is sweeping and pouring in every beat:
0.0-1.0s the hand turns the knob and pushes; the door cracks open and a vertical slice of coloured light appears at the edge. Through the gap, glowing shapes are clearly seen racing sideways and downward.
1.0-2.0s the door swings wide, the camera steps forward through the doorway. Light sweeps across the far wall and the tree and rakes over the floor ahead.
2.0-3.0s the camera is inside. THE BOY is already running, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying. The field of light keeps sliding across every wall and over both of them.
3.0-4.0s the camera keeps walking forward and TILTS UP; the ceiling fills the top of frame with the same light sweeping across it. THE BOY jumps again, arms straight up; THE GIRL is still turning below.

The children are in full motion from the first frame they appear - never posed, never frozen, a different whole-body pose every half second.

BANNED: a projected pattern that stays in place; a static or frozen pattern; shapes that only twinkle, pulse, brighten or fade without travelling; light that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves briefly then stops; any music; blur or soft focus; children standing still; jellyfish, fish, coral, bubbles or underwater imagery; a room lit flat blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.v1_c05_g7.mp4 · 19:55 — Guide architecture — SUMMARY + timed beatsPromptjob 68b514e3CopySUMMARY: a first-person hand pushes a white door open and walks into a Christmas living room where a projected snowflake field shimmers over every wall and the whole ceiling. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the door, the hand, the hallway and the colour. @Image 2 controls only the layout of the room behind the door. Both images show ONE room. The video contains only one room and only one Christmas tree.

SUBJECTS:
THE HAND - a bare right forearm entering from the lower right, palm on a round brass knob.
THE FIELD - the projected light: hundreds of small glowing snowflakes and dots in red, green, blue, gold and white, thrown by a single projector standing in the room, covering the walls and the whole ceiling as ONE continuous field.
THE CHILDREN - exactly two, in matching red-and-white Fair Isle pyjamas, standing on the rug in front of the tree.

HOW THE FIELD BEHAVES - this is the point of the clip:
The field as a whole is ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is.
The motion lives INSIDE it. Every single snowflake is alive for all four seconds:
- each flake DRIFTS slowly downward and slightly sideways, about one flake-width every half second, the way real snow falls past a window at night;
- a flake that reaches the bottom of a wall fades out there, and a new flake fades in high near the ceiling, so the overall density never alters;
- each flake turns slowly on its own centre as it drifts;
- each flake breathes, brightening and dimming on its own timing, never all together;
- each flake's colour cycles slowly through red, green, blue and gold.
The wall and the ceiling are lit by the SAME projector, so they are one field and behave identically at the same moment. If the flakes on the wall are drifting, the flakes on the ceiling are drifting exactly as much. The ceiling is never a still pattern above a moving wall.
Nothing is painted, printed or stencilled on the plaster. The start image is one paused frame of this; at 0.0s it un-pauses. Matching the start image applies to the door, the hallway, the room and the colours, not to where any individual flake sits.

TIMELINE:
0.0-1.0s THE HAND pushes the door open and it swings away from camera; the gap widens and the lit room appears through it. The camera holds still.
1.0-3.0s the camera pushes forward through the doorway into the room in one smooth walking move, and the room fills the frame. THE CHILDREN stand on the rug facing camera, one waving, both shifting their weight, the smaller one bouncing on her toes. The snowflakes drift down the walls and across the ceiling the whole time.
3.0-4.0s the camera tilts up from the top of the tree to the ceiling until the ceiling fills the upper half of the frame, the same drifting field covering it.

THE DOOR: the door is plain painted white panelled wood and its edge stays plain painted white wood. There is no glowing strip, no rainbow fringe, no coloured sparkle bar and no light-up trim on the door edge, on the door frame, or in the gap between them. The only thing seen through the gap is the room beyond. Light spilling out lands as a soft warm wash on the hallway floor.

AUDIO: room tone, a handle click, the door sweeping over the floor, two children laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion throughout, no slow motion, no speed ramp. Exactly two children, no third child, no adult, no pet. One tree. One continuous take. The field's outer boundary holds still while every flake inside it drifts, turns, breathes and shifts colour. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; the whole pattern rotating, spinning or sliding as one sheet; flakes that only twinkle in place without travelling; a still ceiling above a moving wall; a rainbow or glowing strip on the door edge or door frame; any music; blur; the projector unit in shot; jellyfish, fish, coral or bubbles; a cut; on-screen text.

**Prompt** - `job 185cbfbc`

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two laughing children inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. @Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children, their red-and-white Fair Isle pyjamas, and the style and colour of the projected Christmas patterns. Do not copy @Image 1's camera angle or framing. @Video 1 controls ONLY the camera path and the rhythm: hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway into the room, then tilts up. Do NOT copy the room, the furniture, the children, the blue colour, or anything projected from @Video 1.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing centre of the room facing camera, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Projected Christmas shapes - snowflakes, stars, small fir trees and candy canes in gold, green, red and blue - cover the walls AND the ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured moving light appears along the opening edge.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; coloured projected shapes sweep across the floor ahead.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY stands centre facing camera, mouth wide open laughing, arms out, bouncing on his toes. THE GIRL is behind him to the left, turning and laughing. Snowflakes, stars, small fir trees and candy canes drift and rotate continuously across the walls.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same Christmas shapes drift and swirl across the ceiling too. THE BOY jumps once with both arms straight up.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the projection as the only bright moving light source. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The children's pyjamas and hair move naturally with their motion.

[12] AUDIO - natural room sound only: the door handle, the door swinging, children laughing and squealing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across walls and ceiling. Exactly two children. The reveal shows CHRISTMAS imagery only.
BANNED: jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; a frozen still pattern; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text; music.
```

**Prompt** - `job af3cd11d`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. They are never standing still, never posed, never frozen, never waiting. They are running, spinning, jumping and laughing continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Their faces are fully alive: eyes wide, mouths open laughing and shouting. This must look like real children filmed on a phone, not like a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two children running and laughing inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. Documentary realism, extremely natural. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. @Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children, their red-and-white Fair Isle pyjamas, and the style and colour of the projected Christmas patterns. Do not copy @Image 1's camera angle or framing, and do not copy its stillness - @Image 1 is a photograph, this clip must move. @Video 1 controls ONLY the camera path and the rhythm: hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway into the room, then tilts up. Do NOT copy the room, the furniture, the children, the blue colour, or anything projected from @Video 1. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, in the centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Moving projected Christmas shapes - snowflakes, stars, small fir trees and candy canes in gold, green, red and blue - cover the walls AND the whole ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured MOVING light appears along the opening edge, shapes visibly sliding through that slice.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; coloured projected shapes sweep across the floor ahead and travel over the camera's own path.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps up onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Snowflakes, stars, fir trees and candy canes drift, rotate and sweep continuously across every wall.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same Christmas shapes drift and swirl across the entire ceiling, corner to corner, still moving. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the moving projection as the only bright light source, so the light on the walls, the furniture and the children is constantly shifting and sliding. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The sofa cushion compresses when THE BOY lands. The children's pyjamas and hair swing and lift with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the walls and the ceiling. Both children are in full motion from the moment they appear. The reveal shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; children standing still, posed or frozen; jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
```

**Prompt** - `job cdc7911b`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the wall and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the main wall:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - the stars, the candy canes, the small fir trees, the baubles - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the furniture, the tree and the children's faces and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. They are never standing still, never posed, never frozen, never waiting. They are running, spinning, jumping and laughing continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Their faces are fully alive: eyes wide, mouths open laughing and shouting. This must look like real children filmed on a phone, not like a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two children running and laughing inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. Documentary realism, extremely natural. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. It is a photograph, so it shows the projection frozen - do NOT copy that stillness, the projection in this clip must travel.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children and their red-and-white Fair Isle pyjamas, and the COLOUR and STYLE of the Christmas shapes. It is also a photograph - copy its look, never its stillness.
@Video 1 IS THE MOTION AUTHORITY. Copy from it exactly two things: first, the camera path and rhythm - hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway, then tilts up; and second, and most important, HOW THE PROJECTED LIGHT TRAVELS - the speed at which the projected shapes slide across the walls and ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the floor, the furniture and the people. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes, small fir trees and baubles in gold, green, red and blue. Do NOT copy its room, its furniture, its people, its flat blue colour, its captions or its audio.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, in the centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Travelling projected Christmas shapes cover the walls AND the whole ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured light appears along the opening edge, with shapes visibly sliding downward through that slice.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; projected shapes sweep across the floor ahead and travel over the camera's own path.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps up onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. The whole projected field keeps sliding down and to the right across every wall and across both children.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same shapes slide across the entire ceiling in the same direction at the same speed. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the travelling projection as the only bright light source. Because the field is sliding, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The sofa cushion compresses when THE BOY lands. The children's pyjamas and hair swing and lift with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - every projected shape changes position on the surface in every single frame. Both children are in full motion from the moment they appear. The reveal shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; children standing still, posed or frozen; jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
```

**Prompt** - `job d447d883`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
The walls and the entire ceiling of this room are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes, tiny fir trees and baubles in gold, green, red and blue - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the tree, the sofa, the floor and across the children's faces and pyjamas as it passes over them, so the light on everything in the room is constantly shifting.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light-snow is pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the falling projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children and their red-and-white Fair Isle pyjamas, and the COLOUR and STYLE of the Christmas shapes. Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: tall decorated Christmas tree centre, cream sofa with a knit throw right, tall windows left, patterned rug, presents under the tree. Falling light-snow covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured light appears along the opening edge. Through that slice, glowing shapes are clearly seen POURING DOWNWARD past the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light-snow is raining down across the far wall and the tree, and falls over the floor ahead and over the camera's own path.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the light-snow keeps pouring steadily down every wall and across both children, flakes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The snow is falling across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the falling projection as the only bright light source. Because the shapes are pouring down, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Pyjamas and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the walls and on the ceiling; a viewer can follow individual flakes travelling downward. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; snow that falls for a moment then stops; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
```

**Prompt** - `job 20993c33`

```text
RULE 1 - THE LIGHT ON THE WALLS AND CEILING MOVES. THIS IS THE WHOLE POINT OF THE CLIP.
Light this room the way a SPINNING MIRROR BALL lights a room. The projector head is TURNING - one slow revolution every three seconds - so every glowing Christmas shape it throws SWEEPS BODILY across the walls and across the ceiling, travelling sideways, bending over corners and running up onto the ceiling. Nothing is painted on. Nothing holds still.
On top of that sweep, the shapes also DRIFT DOWNWARD like heavy snow past a window at night, each one slowly turning as it goes.
SPEED: one shape crosses the whole wall in ONE SECOND. Movement is obvious within the first quarter-second of the clip.
THE TEST: two frames a third of a second apart share NO shape in the same place. Not one.
The start image is a single PAUSED frame of this moving light. At 0.0s it un-pauses and the light never stops again.
"Match the start image" means the room, the door, the people and the colours - NOT where the light sits. The light must leave its starting position instantly.
The moving light also washes across the tree, the sofa, the floor and both children's faces and pyjamas, so the brightness on everything keeps changing.

RULE 2 - SHARPNESS. The clip must be at least as sharp and clean as the start image: the wood grain of the floor, the panel edges of the white door, the brass knob, the skin and fine hairs of the bare forearm, the leaves of the green wreath. Crisp phone footage, in focus throughout. No blur, no haze, no soft focus, no waxy skin, no repainted door, no colour shift, no washed-out exposure.

RULE 3 - NO MUSIC OF ANY KIND. No song, score, soundtrack, melody, instruments, singing or festive music bed. Only real room sound: the door handle and door swinging, children laughing and squealing, quiet room tone.

TASK: image-to-video, 4 seconds, one continuous handheld phone POV take, vertical 9:16, normal wide-angle lens at eye height. The start image is frame 0.0s.

THE SHOT: first-person POV. A bare right forearm turns the brass knob and pushes the white panelled door open; the camera walks through into a warm double-height Christmas living room and tilts up to the ceiling.

WHAT IS IN THE ROOM (from @Image 1): tall decorated Christmas tree centre, cream sofa with a knit throw on the right, tall windows left, patterned rug, presents. Exactly TWO children - THE BOY and THE GIRL, both in matching red-and-white Fair Isle pyjamas. No adults, no third child, no pets.

TIMELINE - the light is sweeping and pouring in every beat:
0.0-1.0s the hand turns the knob and pushes; the door cracks open and a vertical slice of coloured light appears at the edge. Through the gap, glowing shapes are clearly seen racing sideways and downward.
1.0-2.0s the door swings wide, the camera steps forward through the doorway. Light sweeps across the far wall and the tree and rakes over the floor ahead.
2.0-3.0s the camera is inside. THE BOY is already running, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying. The field of light keeps sliding across every wall and over both of them.
3.0-4.0s the camera keeps walking forward and TILTS UP; the ceiling fills the top of frame with the same light sweeping across it. THE BOY jumps again, arms straight up; THE GIRL is still turning below.

The children are in full motion from the first frame they appear - never posed, never frozen, a different whole-body pose every half second.

BANNED: a projected pattern that stays in place; a static or frozen pattern; shapes that only twinkle, pulse, brighten or fade without travelling; light that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves briefly then stops; any music; blur or soft focus; children standing still; jellyfish, fish, coral, bubbles or underwater imagery; a room lit flat blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
```

**Prompt** - `job 68b514e3`

```text
SUMMARY: a first-person hand pushes a white door open and walks into a Christmas living room where a projected snowflake field shimmers over every wall and the whole ceiling. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the door, the hand, the hallway and the colour. @Image 2 controls only the layout of the room behind the door. Both images show ONE room. The video contains only one room and only one Christmas tree.

SUBJECTS:
THE HAND - a bare right forearm entering from the lower right, palm on a round brass knob.
THE FIELD - the projected light: hundreds of small glowing snowflakes and dots in red, green, blue, gold and white, thrown by a single projector standing in the room, covering the walls and the whole ceiling as ONE continuous field.
THE CHILDREN - exactly two, in matching red-and-white Fair Isle pyjamas, standing on the rug in front of the tree.

HOW THE FIELD BEHAVES - this is the point of the clip:
The field as a whole is ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is.
The motion lives INSIDE it. Every single snowflake is alive for all four seconds:
- each flake DRIFTS slowly downward and slightly sideways, about one flake-width every half second, the way real snow falls past a window at night;
- a flake that reaches the bottom of a wall fades out there, and a new flake fades in high near the ceiling, so the overall density never alters;
- each flake turns slowly on its own centre as it drifts;
- each flake breathes, brightening and dimming on its own timing, never all together;
- each flake's colour cycles slowly through red, green, blue and gold.
The wall and the ceiling are lit by the SAME projector, so they are one field and behave identically at the same moment. If the flakes on the wall are drifting, the flakes on the ceiling are drifting exactly as much. The ceiling is never a still pattern above a moving wall.
Nothing is painted, printed or stencilled on the plaster. The start image is one paused frame of this; at 0.0s it un-pauses. Matching the start image applies to the door, the hallway, the room and the colours, not to where any individual flake sits.

TIMELINE:
0.0-1.0s THE HAND pushes the door open and it swings away from camera; the gap widens and the lit room appears through it. The camera holds still.
1.0-3.0s the camera pushes forward through the doorway into the room in one smooth walking move, and the room fills the frame. THE CHILDREN stand on the rug facing camera, one waving, both shifting their weight, the smaller one bouncing on her toes. The snowflakes drift down the walls and across the ceiling the whole time.
3.0-4.0s the camera tilts up from the top of the tree to the ceiling until the ceiling fills the upper half of the frame, the same drifting field covering it.

THE DOOR: the door is plain painted white panelled wood and its edge stays plain painted white wood. There is no glowing strip, no rainbow fringe, no coloured sparkle bar and no light-up trim on the door edge, on the door frame, or in the gap between them. The only thing seen through the gap is the room beyond. Light spilling out lands as a soft warm wash on the hallway floor.

AUDIO: room tone, a handle click, the door sweeping over the floor, two children laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion throughout, no slow motion, no speed ramp. Exactly two children, no third child, no adult, no pet. One tree. One continuous take. The field's outer boundary holds still while every flake inside it drifts, turns, breathes and shifts colour. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; the whole pattern rotating, spinning or sliding as one sheet; flakes that only twinkle in place without travelling; a still ceiling above a moving wall; a rainbow or glowing strip on the door edge or door frame; any music; blur; the projector unit in shot; jellyfish, fish, coral or bubbles; a cut; on-screen text.
```

---

## C06 - Kid on the bed

*Section:* B-roll 2 - the payoff  
*Status:* IN THE CUT  
*Clip in the cut:* `v1_c06_g8.mp4`  
*What it is:* Boy standing on the mattress mid-bounce, ceiling under full projection

- frames: `v1_c06_g1.png`
- clips: `v1_c06_g1.mp4`, `v1_c06_g10.mp4`, `v1_c06_g2.mp4`, `v1_c06_g3.mp4`, `v1_c06_g4.mp4`, `v1_c06_g5.mp4`, `v1_c06_g6.mp4`, `v1_c06_g7.mp4`, `v1_c06_g8.mp4`, `v1_c06_g9.mp4`

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `v1_c06_g1.png` | our own g1 — bedroom, projection, bed dressing and camera all held; the projector and the boy change |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same cosy bedroom, the same Christmas light projection covering the walls and ceiling — glowing Christmas trees, snowflakes, stars, red baubles and candy canes — the same wooden bed with the dark green duvet, the cream knitted throw, the plaid pillows, the small lit Christmas tree beside the bed, the same stocking on the wall, the same camera position and height, the same magical low-key evening light.

CHANGE 1 — the projector unit must NOT be visible. Remove the small white glowing device and the little stool it sits on from the lower left completely. Replace that corner with plain wall and floor. No projector anywhere in frame.

CHANGE 2 — the boy is now standing UP ON THE BED, barefoot on the mattress in the middle of the duvet, knees bent and arms raised out to his sides, caught mid-bounce with the duvet dimpling under his feet, head tipped back looking up at the projected ceiling, laughing. He is clearly on top of the bed, not sitting on its edge.

The boy is fully dressed in a warm red-and-white knitted Christmas jumper and matching knitted lounge trousers. Wholesome family Christmas scene.

Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
```

> **What we read off it:** g2 — fixed. Projector and stool removed; the boy is up on the mattress mid-bounce with the duvet dimpling under his feet, which is the pose the clip needs to animate into a jump. Sitting on the bed edge (g1) had nowhere to go.

### CLIP — SEEDANCE 2.5 · v1_c06_g8.mp4 · SUBMITTED 22:26

**Attached to this job**

| slot | file | why |
|---|---|---|
| start_image | `v1_c06_g1.png` | frame 0.0 s |

**Clip prompt — the one in the cut** - `seedance_2_5 · 720p · 4 s · 9:16 · audio on`

```text
SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while an animated snowfall plays across the wall behind him and the whole ceiling, thrown there by a projector standing on the floor. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, THE BOY and the colour.

SUBJECTS:
THE BOY - exactly one child in red-and-white Fair Isle pyjamas, standing on the bed.
THE PROJECTOR - a small Christmas projector switched on and running on the bedroom floor, out of shot. Its lens throws one wide cone of coloured light across the room. Everything glowing on the plaster is that cone landing.
THE SCREEN - the wall behind the bed and the whole ceiling together, catching that cone as one continuous surface. The light lands directly on bare plaster and wraps around the corner where wall meets ceiling. No rectangle, no visible screen edge, no television.

WHAT IS PLAYING ON THE SCREEN - this is the point of the clip:
A looping snowfall animation is PLAYING on THE SCREEN for all four seconds, exactly the way a film plays on a cinema screen: the screen itself is fixed to the plaster and holds perfectly still, while the picture playing on it is in constant motion. The animation is a night snowfall - hundreds of small glowing six-point snowflakes and round dots in red, green, blue, gold and white, all falling.
Track these three so the fall is unmistakable:
FLAKE A - a large white six-point flake that begins just above the headboard on the left of the wall. It falls steadily and drifts slightly right, passing the middle of the wall at 2.0s, and fades out low near the skirting board at 4.0s.
FLAKE B - a red flake on the ceiling directly above the headboard. It travels across the ceiling toward the far corner, ending about a third of the way across at 4.0s.
FLAKE C - a small gold dot on the right of the wall. It falls the full height of the wall in the first two seconds, fades out at the bottom, and a fresh gold dot fades in high near the ceiling and falls the same path again.
Every other flake behaves like these three: roughly a quarter of the wall's height every second, downward with a slight sideways drift, each one turning slowly on its own centre and breathing brighter and dimmer on its own timing, each cycling slowly through red, green, blue and gold. Density stays even because a flake fading out at the bottom is matched by one fading in at the top.
Because the wall and the ceiling are one screen fed by one projector lens, the snowfall on the ceiling plays at the same moment and at the same speed as the snowfall on the wall.
The start image is one paused frame of this animation. At 0.0s the projector un-pauses and the snowfall plays. Matching the start image applies to the bedroom, the bed, THE BOY and the colours, not to where any individual flake sits.

TIMELINE:
0.0-1.5s THE BOY bends his knees and pushes off the mattress; both feet leave the duvet, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
1.5-2.5s He lands on both feet and drives straight into a second, higher jump, knees tucking.
2.5-4.0s The camera tilts up in one slow smooth move until the ceiling fills the upper half of the frame. THE BOY stays low in frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take. The camera makes one move only, a tilt up. THE SCREEN stays bolted to the plaster while the snowfall plays across it. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; a frozen pattern; the whole pattern turning or sliding as one sheet; any music; the projector unit in shot; a second child; a cut; on-screen text.
```

**Other takes**

Takes not used (9)v1_c06_g1.mp4 · 17:29 — First pass — hold the start framePromptjob bbd46a17CopyTASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and projected pattern exactly.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes move across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the projected Christmas shapes and the lighting. It is the only authority on the scene.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Projected snowflakes, stars, candy canes, baubles and green fir trees cover the wall behind the bed and continue onto the ceiling.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The ceiling is covered in the same drifting Christmas projection. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the projection is the only bright moving light source, unchanged in character across the clip.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - natural room sound only: mattress springs, a child laughing and squealing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across wall and ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, a frozen still pattern, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text, music.v1_c06_g2.mp4 · 17:55 — Audio rule + motion fixPromptjob 314d7700CopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and projected pattern exactly.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes sweep across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the look of the projected Christmas shapes and the lighting. It is the only authority on the scene. It is a photograph - do not copy its stillness, this clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Moving projected snowflakes, stars, candy canes, baubles and green fir trees cover the wall behind the bed and continue across the whole ceiling.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off. Behind him the projected shapes visibly slide and rotate across the wall.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second, face fully redrawing between beats.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The ceiling is fully covered in the same drifting, swirling Christmas projection, corner to corner, still visibly moving. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the bed and the boy is constantly shifting and sliding across them.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the wall and the ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.v1_c06_g3.mp4 · 18:21 — Audio rule + motion fix · scene-6.mp4Promptjob cb2a248dCopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the wall and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the wall behind the bed:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - every snowflake, star, candy cane, bauble and fir tree, on the wall and on the ceiling alike - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the bed, the duvet and the boy's face and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

@Video 1 IS THE MOTION AUTHORITY FOR THE PROJECTED LIGHT AND FOR NOTHING ELSE. It was filmed in a real bedroom with a real rotating projector running. Copy from it exactly: the speed at which the projected shapes slide across the wall and the ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the bed and over the child. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes, baubles and fir trees, in the exact colours and styles shown in the start image. Do NOT copy its room, its bed, its person, its flat blue colour, its captions or its audio.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and the LOOK of the projected shapes exactly - but not their stillness.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes sweep across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the projected Christmas shapes and the lighting. @Video 1 controls only HOW THAT LIGHT MOVES. The start image is a photograph - do not copy its stillness, this clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Moving projected snowflakes, stars, candy canes, baubles and green fir trees sweep across the wall behind the bed and across the ceiling. The coverage is dense but uneven and constantly changing, because the field is sliding - that is correct and expected.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off. Behind him the projected field is already sliding down and to the right.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second, face fully redrawing between beats.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The same sliding Christmas projection is travelling across the ceiling at the same speed and in the same direction as on the wall. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the bed and the boy is constantly shifting and sliding across them.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected field slides continuously and visibly in every single frame, on the wall and on the ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.v1_c06_g4.mp4 · 18:50 — Audio rule + motion fixPromptjob c9657884CopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
The wall behind the bed and the entire ceiling are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes, baubles and small green fir trees - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the bed, the duvet and across the boy's face and pyjamas as it passes over them, so the light on him is constantly shifting.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and the LOOK of the Christmas shapes exactly - but not their stillness.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while light-snow pours down the wall behind him and across the ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit only by the falling projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness. This clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Falling light-snow covers the wall behind the bed AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses at the push-off. Behind him the light-snow is already pouring straight down the wall, flakes clearly travelling from the top of the wall towards the bed.
1.0-2.0s - THE BOY lands, the mattress compresses, and he immediately pushes off into a second higher jump, arms swinging above his head, hair lifting. A clearly different whole-body pose every half second. The snow keeps raining down behind him and washes down over his back and shoulders as it falls.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top. Light-snow is pouring across the entire ceiling as well, streaming away towards the far wall at the same speed. THE BOY keeps bouncing throughout, still laughing, still changing pose every half second.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[9] LIGHTING - warm dim bedroom, the falling projection is the only bright light source, so the light on the wall, the bed and the boy is constantly pouring and shifting across them.

[10] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the wall and on the ceiling; a viewer can follow individual flakes travelling downward. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; snow that falls for a moment then stops; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.v1_c06_g5.mp4 · 19:21 — Rule Zero — motion is the only pass condition · scene_no_audio-6.mp4Promptjob 7242157bCopyRULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on the wall behind the bed and on the entire ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running in this exact kind of bedroom. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the way the whole field of glowing shapes slides and swarms across the plaster without ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

WHAT THE LIGHT DOES, described so it cannot be mistaken for a texture:
- The whole field of glowing shapes SLIDES BODILY across the wall and across the ceiling, the way light from a spinning projector head sweeps a room. It never locks onto the plaster.
- On top of that sliding, individual shapes POUR DOWNWARD like heavy snowfall filmed through a window at night, and each one spins slowly as it goes and drags a faint soft trail.
- SPEED: a single shape crosses the full height of the wall in ABOUT ONE SECOND. That is fast. A viewer must see it moving within the first quarter second of the clip.
- THE TEST: take any two frames a third of a second apart and lay them on top of each other. NOT ONE glowing shape is in the same place. Not one. If any shape has stayed put, the clip is wrong.
- The moving light also pours down over the bed, the duvet, the small tree and across the boy's face and pyjamas as it passes over him, so the brightness on everything in the room is changing continuously.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, bed, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

AUDIO RULE - SECOND MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

IMAGE QUALITY RULE: the finished clip must look at least as sharp and as clean as the start image. Hold its exact sharpness, exposure, contrast and fine detail - the knit of the cream throw, the pile of the dark green velvet duvet, the grain of the wooden headboard, the boy's skin and hair. Crisp modern phone footage, in focus throughout. BANNED: blur, soft focus, haze, mushy low-detail surfaces, plastic or waxy skin, colour shift, washed-out exposure, a dreamy or filtered look.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
A boy in Christmas pyjamas jumps on his bed while light sweeps and pours down the wall behind him and across the whole ceiling; the camera eases back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit only by the moving projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, jumping on the bed, knees bending and springing, arms up, mouth wide open laughing and shouting, a clearly different whole-body pose every half second. Never standing still, never posed, never frozen.
COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw across the foot of the bed, pillows at the head, a wooden headboard on the right, a small lit Christmas tree on the right. Sweeping, pouring light covers the wall behind the bed AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - THE BOY is already mid-bounce, knees bending, arms coming up, mouth open laughing. The duvet rucks and lifts under his feet. Behind him the field of glowing shapes is already sliding across the wall and raining downward; shapes visibly travel from the top of the wall to the bottom within this beat.
1.0-2.0s - he pushes off harder and jumps higher, both feet leaving the mattress, arms straight up over his head, head tipping back. The light keeps sweeping and pouring down the wall and over him, so the bright patches crossing his pyjamas and face are constantly moving.
2.0-4.0s - one single continuous camera move: the camera eases BACKWARD in a slow zoom-out while TILTING UPWARD, until the CEILING fills the upper half of frame. The light is sweeping and pouring across the entire ceiling too, streaming away towards the far side of the room at the same speed. THE BOY stays in the lower part of frame and keeps bouncing and laughing the whole time.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. One combined movement only: the slow zoom-out plus upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[9] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the ceiling, the bed and the boy is constantly pouring and shifting across them. Do not flood the room with one flat colour.

[10] PHYSICS - the mattress compresses and springs back under each landing; the duvet and the knit throw ruck, lift and fall with every bounce. Pyjamas and hair lift on each jump.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: a child laughing and squealing, the mattress and bedding compressing and creaking, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light is visibly sweeping and pouring in every single frame, on the wall and on the ceiling; a viewer can follow individual shapes travelling across and down. Exactly one child, visibly excited and moving in every frame. The projection shows CHRISTMAS imagery only. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; the boy standing still, posed or frozen; a second child; an adult; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a cut; subtitles; on-screen text.v1_c06_g6.mp4 · 19:36 — Rule 1 — the light on the walls movesPromptjob fab60aa7CopyRULE 1 - THE LIGHT ON THE WALL AND CEILING MOVES. THIS IS THE WHOLE POINT OF THE CLIP.
Light this bedroom the way a SPINNING MIRROR BALL lights a room. The projector head is TURNING - one slow revolution every three seconds - so every glowing Christmas shape it throws SWEEPS BODILY across the wall behind the bed and across the whole ceiling, travelling sideways, bending over the corner and running up onto the ceiling. Nothing is painted on. Nothing holds still.
On top of that sweep, the shapes also DRIFT DOWNWARD like heavy snow past a window at night, each one slowly turning as it goes.
SPEED: one shape crosses the whole wall in ONE SECOND. Movement is obvious within the first quarter-second of the clip.
THE TEST: two frames a third of a second apart share NO shape in the same place. Not one.
The start image is a single PAUSED frame of this moving light. At 0.0s it un-pauses and the light never stops again.
"Match the start image" means the room, the bed, the boy and the colours - NOT where the light sits. The light must leave its starting position instantly.
The moving light also washes over the duvet, the small tree and the boy's face and pyjamas, so bright patches keep travelling across him.

RULE 2 - NO MUSIC OF ANY KIND. No song, score, soundtrack, melody, instruments, singing or festive music bed. Only real room sound: a child laughing and squealing, the mattress and bedding compressing, quiet room tone.

RULE 3 - SHARPNESS. At least as sharp and clean as the start image: the knit of the cream throw, the pile of the dark green velvet duvet, the grain of the wooden headboard, the boy's skin and hair. Crisp phone footage, in focus throughout. No blur, no haze, no soft focus, no waxy skin, no colour shift, no washed-out exposure.

TASK: image-to-video, 4 seconds, one continuous handheld phone take, vertical 9:16, normal wide-angle lens at chest height. The start image is frame 0.0s.

THE SHOT: a boy jumps on his bed while light sweeps down the wall behind him and across the ceiling; the camera eases back and tilts up.

WHAT IS IN THE ROOM - all of this exists in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw across the foot, pillows at the head, a wooden headboard on the right, a small lit Christmas tree on the right. Exactly ONE child - THE BOY, in red-and-white Fair Isle pyjamas. No second child, no adults, no pets.

TIMELINE - the light is sweeping and pouring in every beat:
0.0-1.0s THE BOY is already mid-bounce, knees bending, arms coming up, mouth open laughing; the duvet rucks and lifts under his feet. Behind him the field of shapes is already sliding across the wall and raining downward.
1.0-2.0s he pushes off harder and jumps higher, both feet leaving the mattress, arms straight up, head tipping back. The light keeps sweeping over the wall and over him.
2.0-4.0s one single continuous camera move: the camera eases BACKWARD in a slow zoom-out while TILTING UP, until the ceiling fills the upper half of frame with the same light sweeping across it. THE BOY stays low in frame, still bouncing and laughing.

He is in full motion in every frame - never posed, never frozen, a different whole-body pose every half second. The mattress compresses and springs back on every landing; the duvet and throw ruck and fall; pyjamas and hair lift on each jump.

BANNED: a projected pattern that stays in place; a static or frozen pattern; shapes that only twinkle, pulse, brighten or fade without travelling; light that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves briefly then stops; any music; blur or soft focus; the boy standing still; a second child; an adult; jellyfish, fish, coral, bubbles or underwater imagery; a room lit flat blue; the projector unit visible; a cut; subtitles; on-screen text.v1_c06_g7.mp4 · 19:55 — Guide architecture — SUMMARY + timed beatsPromptjob 2a6e0f3fCopySUMMARY: a boy bounces on his bed in a Christmas bedroom while a projected snowflake field shimmers over the wall behind him and the whole ceiling. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, the boy and the colour.

SUBJECTS:
THE BOY - exactly one child, in red-and-white Fair Isle pyjamas, standing on the bed. No second child, no adult, no pet.
THE FIELD - the projected light: hundreds of small glowing snowflakes and dots in red, green, blue, gold and white, thrown by a single projector standing in the bedroom, covering the wall behind the bed and the whole ceiling as ONE continuous field.
THE BED - dark green velvet duvet, cream knit throw across the foot, pillows against the headboard.

HOW THE FIELD BEHAVES - this is the point of the clip:
The field as a whole is ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is, and no shape travels a long distance across the wall.
The motion lives INSIDE it. Every single snowflake is alive for all four seconds:
- each flake DRIFTS slowly downward and slightly sideways, about one flake-width every half second, the way real snow falls past a window at night;
- a flake that reaches the bottom of the wall fades out there, and a new flake fades in high near the ceiling, so the overall density never alters;
- each flake turns slowly on its own centre as it drifts;
- each flake breathes, brightening and dimming on its own timing, never all together;
- each flake's colour cycles slowly through red, green, blue and gold.
The wall and the ceiling are lit by the SAME projector, so they are one field and behave identically at the same moment. Whatever the flakes on the wall are doing, the flakes on the ceiling are doing at the same instant, at the same speed. The ceiling is never a still pattern above a moving wall, and the wall is never a still pattern below a moving ceiling.
Nothing is painted, printed or stencilled on the plaster. The start image is one paused frame of this; at 0.0s it un-pauses. Matching the start image applies to the bedroom, the bed, THE BOY and the colours, not to where any individual flake sits.

TIMELINE:
0.0-1.5s THE BOY bends his knees, then pushes off the mattress hard; both feet leave the duvet and his arms swing straight up over his head. The mattress compresses under him and springs back. He is laughing with his mouth open. The snowflakes drift down the wall and across the ceiling.
1.5-2.5s THE BOY lands on both feet, the duvet dents and recovers, and he immediately drives into a second jump, higher than the first, knees tucking up.
2.5-4.0s the camera tilts up in one slow smooth move until the ceiling fills the upper half of the frame, the same drifting field covering it. THE BOY stays low in the frame and keeps bouncing.

AUDIO: room tone, the mattress and springs compressing on each landing, bedding rustling, a boy laughing and squealing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - a real boy jumping at real speed, landing with real weight. No slow motion, no slow-motion feel, no floating, no speed ramp, no dreamy drift. Exactly one child. One continuous take. The camera makes one move only, a tilt up - it does not zoom, push in or pull out. The field's outer boundary holds still while every flake inside it drifts, turns, breathes and shifts colour. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; a floating or weightless jump; the whole pattern rotating, spinning, swinging or sliding as one sheet; a frozen or still pattern; flakes that only twinkle in place without travelling; a still ceiling above a moving wall; any music; blur; the projector unit in shot; jellyfish, fish, coral or bubbles; a second child; an adult; a cut; on-screen text.v1_c06_g9.mp4 · 22:33 — Guide architecture — fast, busy light showPromptjob a3247d8eCopySUMMARY: a projector plays a fast, busy Christmas light show across a bedroom wall and the whole ceiling while a boy bounces on his bed. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, THE BOY and the colour.

SUBJECTS:
THE PROJECTOR - a Christmas projector switched on and running on the bedroom floor, out of shot. Its lens throws one wide cone of coloured light across the room. Everything glowing on the plaster is that cone landing.
THE SCREEN - the wall behind the bed and the whole ceiling together, catching that cone as one continuous surface. The light lands directly on bare plaster and wraps around the corner where wall meets ceiling. No rectangle, no visible screen edge, no television.
THE LIGHT SHOW - the animation playing on THE SCREEN: glowing six-point snowflakes, round dots and stars in red, green, blue, gold and white.
THE BOY - exactly one child in red-and-white Fair Isle pyjamas, bouncing on the bed.

THE LIGHT SHOW IS THE POINT OF THIS CLIP:
THE SCREEN itself is fixed to the plaster and never moves. Everything playing on it is RACING. This is not a shimmer and it is not a twinkle in place - every element travels a long, obvious distance across the plaster within four seconds, far enough that you can follow it with your eye.
- The snowflakes POUR downward fast, each one falling the full height of the wall in about one and a half seconds, fading out at the skirting board while fresh ones pour in along the ceiling line, so the fall never stops.
- Every flake spins as it falls and swings from side to side across its own path.
- Every flake flicks to a different colour about twice a second - red, green, blue, gold, white - so the whole wall keeps shifting colour.
- The round dots blink on and off rapidly like fast fairy lights, hundreds of them out of step with one another.
Because one lens feeds both surfaces, every event below plays on the wall and on the ceiling at the same instant and at the same speed.

TIMELINE:
0.0-1.0s SCREEN: a bright gold shooting star streaks diagonally from the top left of the wall down to the bottom right, leaving a short trail behind it, while the snow pours down the whole wall. BOY: bends his knees and pushes off the mattress, both feet leaving the duvet, arms swinging up over his head, mouth open laughing. CAMERA: holds.
1.0-2.0s SCREEN: a second shooting star crosses the ceiling from one corner to the other; the larger flakes swell bigger and shrink back down as they fall. BOY: lands on both feet and drives straight into a second, higher jump.
2.0-3.0s SCREEN: a wave of green sweeps across the wall and over the ceiling, every element flushing green as the wave passes, then the colours scatter apart again. CAMERA: tilts up in one slow smooth move until the ceiling fills the upper half of the frame.
3.0-4.0s SCREEN: a third shooting star crosses the ceiling, the dots burst outward in rings, and the snow keeps pouring at full speed. BOY: stays low in the frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take. The camera makes one move only, a tilt up. THE SCREEN stays bolted to the plaster while everything playing on it races across it. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; a frozen or still pattern; elements that stay in one place; the whole pattern turning or sliding as one sheet; any music; the projector unit in shot; a second child; a cut; on-screen text.v1_c06_g10.mp4 · 22:46 — Guide architecture — every stillness word stripped outPromptjob 634f95a6CopySUMMARY: a Christmas projector fills a bedroom wall and ceiling with falling snowflakes, stars and little Christmas trees of light while a boy bounces on his bed. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, THE BOY and the colour.

SUBJECTS:
THE PROJECTOR - a Christmas projector switched on and running on the bedroom floor, out of shot, throwing one wide cone of coloured light. Every glowing shape in the room is that cone landing.
THE SHAPES - glowing six-point snowflakes, small stars, little Christmas trees and round dots in red, green, blue, gold and white, scattered across the wall behind the bed, the ceiling, the bed and THE BOY himself.
THE BOY - exactly one child in red-and-white Fair Isle pyjamas, bouncing on the bed.

HOW THE SHAPES TRAVEL - this is the point of the clip:
Every shape is falling. Each one starts high, up along the line where the wall meets the ceiling, and travels downward for the whole four seconds, fast enough to cross the wall from the ceiling to the skirting board in about a second and a half. Follow any single one and you watch it pass landmark after landmark:
- a big white snowflake starts above the headboard, passes the top of the headboard at 0.5s, slides down over the pillows at 1.2s, crosses THE BOY's chest and sleeve at 2.0s, carries on down over the green duvet, and reaches the skirting board at 3.5s where it fades out;
- a gold star starts at the far corner of the ceiling and travels the length of the ceiling toward the camera, arrives at the line where ceiling meets wall at 2.5s, and keeps going down the wall from there;
- a red Christmas tree shape falls beside the headboard on the right, spinning as it drops, and arrives on the duvet at 3.0s.
Every other shape is doing the same thing at the same moment from a different starting height, so the wall and the ceiling are one continuous downpour of light for all four seconds. As each shape leaves the bottom, a fresh one appears up along the ceiling line and falls the same way, so the room never empties.
As they fall the shapes also spin on their own centres, swing sideways across their own paths, and flick to a new colour about twice a second.
One lens lights the wall and the ceiling together, so the downpour on the ceiling runs at the same instant and at the same speed as the downpour on the wall.
The start image catches this downpour at one instant only. From 0.0s every shape carries on falling from wherever it happens to be.

TIMELINE:
0.0-1.5s THE BOY bends his knees and pushes off the mattress, both feet leaving the duvet, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back. CAMERA holds.
1.5-2.5s THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking up.
2.5-4.0s CAMERA tilts up in one smooth move until the ceiling fills the upper half of the frame. THE BOY stays low in the frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take. The camera makes one move only, a tilt up. Every glowing shape is travelling downward across the plaster for the whole four seconds, covering real distance. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; any music; the projector unit in shot; a second child; a cut; on-screen text.

**Prompt** - `job bbd46a17`

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and projected pattern exactly.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes move across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the projected Christmas shapes and the lighting. It is the only authority on the scene.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Projected snowflakes, stars, candy canes, baubles and green fir trees cover the wall behind the bed and continue onto the ceiling.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The ceiling is covered in the same drifting Christmas projection. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the projection is the only bright moving light source, unchanged in character across the clip.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - natural room sound only: mattress springs, a child laughing and squealing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across wall and ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, a frozen still pattern, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text, music.
```

**Prompt** - `job 314d7700`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and projected pattern exactly.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes sweep across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the look of the projected Christmas shapes and the lighting. It is the only authority on the scene. It is a photograph - do not copy its stillness, this clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Moving projected snowflakes, stars, candy canes, baubles and green fir trees cover the wall behind the bed and continue across the whole ceiling.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off. Behind him the projected shapes visibly slide and rotate across the wall.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second, face fully redrawing between beats.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The ceiling is fully covered in the same drifting, swirling Christmas projection, corner to corner, still visibly moving. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the bed and the boy is constantly shifting and sliding across them.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the wall and the ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
```

**Prompt** - `job cb2a248d`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the wall and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the wall behind the bed:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - every snowflake, star, candy cane, bauble and fir tree, on the wall and on the ceiling alike - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the bed, the duvet and the boy's face and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

@Video 1 IS THE MOTION AUTHORITY FOR THE PROJECTED LIGHT AND FOR NOTHING ELSE. It was filmed in a real bedroom with a real rotating projector running. Copy from it exactly: the speed at which the projected shapes slide across the wall and the ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the bed and over the child. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes, baubles and fir trees, in the exact colours and styles shown in the start image. Do NOT copy its room, its bed, its person, its flat blue colour, its captions or its audio.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and the LOOK of the projected shapes exactly - but not their stillness.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes sweep across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the projected Christmas shapes and the lighting. @Video 1 controls only HOW THAT LIGHT MOVES. The start image is a photograph - do not copy its stillness, this clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Moving projected snowflakes, stars, candy canes, baubles and green fir trees sweep across the wall behind the bed and across the ceiling. The coverage is dense but uneven and constantly changing, because the field is sliding - that is correct and expected.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off. Behind him the projected field is already sliding down and to the right.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second, face fully redrawing between beats.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The same sliding Christmas projection is travelling across the ceiling at the same speed and in the same direction as on the wall. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the bed and the boy is constantly shifting and sliding across them.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected field slides continuously and visibly in every single frame, on the wall and on the ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
```

**Prompt** - `job c9657884`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
The wall behind the bed and the entire ceiling are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes, baubles and small green fir trees - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the bed, the duvet and across the boy's face and pyjamas as it passes over them, so the light on him is constantly shifting.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and the LOOK of the Christmas shapes exactly - but not their stillness.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while light-snow pours down the wall behind him and across the ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit only by the falling projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness. This clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Falling light-snow covers the wall behind the bed AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses at the push-off. Behind him the light-snow is already pouring straight down the wall, flakes clearly travelling from the top of the wall towards the bed.
1.0-2.0s - THE BOY lands, the mattress compresses, and he immediately pushes off into a second higher jump, arms swinging above his head, hair lifting. A clearly different whole-body pose every half second. The snow keeps raining down behind him and washes down over his back and shoulders as it falls.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top. Light-snow is pouring across the entire ceiling as well, streaming away towards the far wall at the same speed. THE BOY keeps bouncing throughout, still laughing, still changing pose every half second.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[9] LIGHTING - warm dim bedroom, the falling projection is the only bright light source, so the light on the wall, the bed and the boy is constantly pouring and shifting across them.

[10] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the wall and on the ceiling; a viewer can follow individual flakes travelling downward. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; snow that falls for a moment then stops; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
```

**Prompt** - `job 7242157b`

```text
RULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on the wall behind the bed and on the entire ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running in this exact kind of bedroom. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the way the whole field of glowing shapes slides and swarms across the plaster without ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

WHAT THE LIGHT DOES, described so it cannot be mistaken for a texture:
- The whole field of glowing shapes SLIDES BODILY across the wall and across the ceiling, the way light from a spinning projector head sweeps a room. It never locks onto the plaster.
- On top of that sliding, individual shapes POUR DOWNWARD like heavy snowfall filmed through a window at night, and each one spins slowly as it goes and drags a faint soft trail.
- SPEED: a single shape crosses the full height of the wall in ABOUT ONE SECOND. That is fast. A viewer must see it moving within the first quarter second of the clip.
- THE TEST: take any two frames a third of a second apart and lay them on top of each other. NOT ONE glowing shape is in the same place. Not one. If any shape has stayed put, the clip is wrong.
- The moving light also pours down over the bed, the duvet, the small tree and across the boy's face and pyjamas as it passes over him, so the brightness on everything in the room is changing continuously.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, bed, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

AUDIO RULE - SECOND MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

IMAGE QUALITY RULE: the finished clip must look at least as sharp and as clean as the start image. Hold its exact sharpness, exposure, contrast and fine detail - the knit of the cream throw, the pile of the dark green velvet duvet, the grain of the wooden headboard, the boy's skin and hair. Crisp modern phone footage, in focus throughout. BANNED: blur, soft focus, haze, mushy low-detail surfaces, plastic or waxy skin, colour shift, washed-out exposure, a dreamy or filtered look.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
A boy in Christmas pyjamas jumps on his bed while light sweeps and pours down the wall behind him and across the whole ceiling; the camera eases back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit only by the moving projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, jumping on the bed, knees bending and springing, arms up, mouth wide open laughing and shouting, a clearly different whole-body pose every half second. Never standing still, never posed, never frozen.
COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw across the foot of the bed, pillows at the head, a wooden headboard on the right, a small lit Christmas tree on the right. Sweeping, pouring light covers the wall behind the bed AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - THE BOY is already mid-bounce, knees bending, arms coming up, mouth open laughing. The duvet rucks and lifts under his feet. Behind him the field of glowing shapes is already sliding across the wall and raining downward; shapes visibly travel from the top of the wall to the bottom within this beat.
1.0-2.0s - he pushes off harder and jumps higher, both feet leaving the mattress, arms straight up over his head, head tipping back. The light keeps sweeping and pouring down the wall and over him, so the bright patches crossing his pyjamas and face are constantly moving.
2.0-4.0s - one single continuous camera move: the camera eases BACKWARD in a slow zoom-out while TILTING UPWARD, until the CEILING fills the upper half of frame. The light is sweeping and pouring across the entire ceiling too, streaming away towards the far side of the room at the same speed. THE BOY stays in the lower part of frame and keeps bouncing and laughing the whole time.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. One combined movement only: the slow zoom-out plus upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[9] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the ceiling, the bed and the boy is constantly pouring and shifting across them. Do not flood the room with one flat colour.

[10] PHYSICS - the mattress compresses and springs back under each landing; the duvet and the knit throw ruck, lift and fall with every bounce. Pyjamas and hair lift on each jump.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: a child laughing and squealing, the mattress and bedding compressing and creaking, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light is visibly sweeping and pouring in every single frame, on the wall and on the ceiling; a viewer can follow individual shapes travelling across and down. Exactly one child, visibly excited and moving in every frame. The projection shows CHRISTMAS imagery only. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; the boy standing still, posed or frozen; a second child; an adult; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a cut; subtitles; on-screen text.
```

**Prompt** - `job fab60aa7`

```text
RULE 1 - THE LIGHT ON THE WALL AND CEILING MOVES. THIS IS THE WHOLE POINT OF THE CLIP.
Light this bedroom the way a SPINNING MIRROR BALL lights a room. The projector head is TURNING - one slow revolution every three seconds - so every glowing Christmas shape it throws SWEEPS BODILY across the wall behind the bed and across the whole ceiling, travelling sideways, bending over the corner and running up onto the ceiling. Nothing is painted on. Nothing holds still.
On top of that sweep, the shapes also DRIFT DOWNWARD like heavy snow past a window at night, each one slowly turning as it goes.
SPEED: one shape crosses the whole wall in ONE SECOND. Movement is obvious within the first quarter-second of the clip.
THE TEST: two frames a third of a second apart share NO shape in the same place. Not one.
The start image is a single PAUSED frame of this moving light. At 0.0s it un-pauses and the light never stops again.
"Match the start image" means the room, the bed, the boy and the colours - NOT where the light sits. The light must leave its starting position instantly.
The moving light also washes over the duvet, the small tree and the boy's face and pyjamas, so bright patches keep travelling across him.

RULE 2 - NO MUSIC OF ANY KIND. No song, score, soundtrack, melody, instruments, singing or festive music bed. Only real room sound: a child laughing and squealing, the mattress and bedding compressing, quiet room tone.

RULE 3 - SHARPNESS. At least as sharp and clean as the start image: the knit of the cream throw, the pile of the dark green velvet duvet, the grain of the wooden headboard, the boy's skin and hair. Crisp phone footage, in focus throughout. No blur, no haze, no soft focus, no waxy skin, no colour shift, no washed-out exposure.

TASK: image-to-video, 4 seconds, one continuous handheld phone take, vertical 9:16, normal wide-angle lens at chest height. The start image is frame 0.0s.

THE SHOT: a boy jumps on his bed while light sweeps down the wall behind him and across the ceiling; the camera eases back and tilts up.

WHAT IS IN THE ROOM - all of this exists in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw across the foot, pillows at the head, a wooden headboard on the right, a small lit Christmas tree on the right. Exactly ONE child - THE BOY, in red-and-white Fair Isle pyjamas. No second child, no adults, no pets.

TIMELINE - the light is sweeping and pouring in every beat:
0.0-1.0s THE BOY is already mid-bounce, knees bending, arms coming up, mouth open laughing; the duvet rucks and lifts under his feet. Behind him the field of shapes is already sliding across the wall and raining downward.
1.0-2.0s he pushes off harder and jumps higher, both feet leaving the mattress, arms straight up, head tipping back. The light keeps sweeping over the wall and over him.
2.0-4.0s one single continuous camera move: the camera eases BACKWARD in a slow zoom-out while TILTING UP, until the ceiling fills the upper half of frame with the same light sweeping across it. THE BOY stays low in frame, still bouncing and laughing.

He is in full motion in every frame - never posed, never frozen, a different whole-body pose every half second. The mattress compresses and springs back on every landing; the duvet and throw ruck and fall; pyjamas and hair lift on each jump.

BANNED: a projected pattern that stays in place; a static or frozen pattern; shapes that only twinkle, pulse, brighten or fade without travelling; light that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves briefly then stops; any music; blur or soft focus; the boy standing still; a second child; an adult; jellyfish, fish, coral, bubbles or underwater imagery; a room lit flat blue; the projector unit visible; a cut; subtitles; on-screen text.
```

**Prompt** - `job 2a6e0f3f`

```text
SUMMARY: a boy bounces on his bed in a Christmas bedroom while a projected snowflake field shimmers over the wall behind him and the whole ceiling. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, the boy and the colour.

SUBJECTS:
THE BOY - exactly one child, in red-and-white Fair Isle pyjamas, standing on the bed. No second child, no adult, no pet.
THE FIELD - the projected light: hundreds of small glowing snowflakes and dots in red, green, blue, gold and white, thrown by a single projector standing in the bedroom, covering the wall behind the bed and the whole ceiling as ONE continuous field.
THE BED - dark green velvet duvet, cream knit throw across the foot, pillows against the headboard.

HOW THE FIELD BEHAVES - this is the point of the clip:
The field as a whole is ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is, and no shape travels a long distance across the wall.
The motion lives INSIDE it. Every single snowflake is alive for all four seconds:
- each flake DRIFTS slowly downward and slightly sideways, about one flake-width every half second, the way real snow falls past a window at night;
- a flake that reaches the bottom of the wall fades out there, and a new flake fades in high near the ceiling, so the overall density never alters;
- each flake turns slowly on its own centre as it drifts;
- each flake breathes, brightening and dimming on its own timing, never all together;
- each flake's colour cycles slowly through red, green, blue and gold.
The wall and the ceiling are lit by the SAME projector, so they are one field and behave identically at the same moment. Whatever the flakes on the wall are doing, the flakes on the ceiling are doing at the same instant, at the same speed. The ceiling is never a still pattern above a moving wall, and the wall is never a still pattern below a moving ceiling.
Nothing is painted, printed or stencilled on the plaster. The start image is one paused frame of this; at 0.0s it un-pauses. Matching the start image applies to the bedroom, the bed, THE BOY and the colours, not to where any individual flake sits.

TIMELINE:
0.0-1.5s THE BOY bends his knees, then pushes off the mattress hard; both feet leave the duvet and his arms swing straight up over his head. The mattress compresses under him and springs back. He is laughing with his mouth open. The snowflakes drift down the wall and across the ceiling.
1.5-2.5s THE BOY lands on both feet, the duvet dents and recovers, and he immediately drives into a second jump, higher than the first, knees tucking up.
2.5-4.0s the camera tilts up in one slow smooth move until the ceiling fills the upper half of the frame, the same drifting field covering it. THE BOY stays low in the frame and keeps bouncing.

AUDIO: room tone, the mattress and springs compressing on each landing, bedding rustling, a boy laughing and squealing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - a real boy jumping at real speed, landing with real weight. No slow motion, no slow-motion feel, no floating, no speed ramp, no dreamy drift. Exactly one child. One continuous take. The camera makes one move only, a tilt up - it does not zoom, push in or pull out. The field's outer boundary holds still while every flake inside it drifts, turns, breathes and shifts colour. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; a floating or weightless jump; the whole pattern rotating, spinning, swinging or sliding as one sheet; a frozen or still pattern; flakes that only twinkle in place without travelling; a still ceiling above a moving wall; any music; blur; the projector unit in shot; jellyfish, fish, coral or bubbles; a second child; an adult; a cut; on-screen text.
```

**Prompt** - `job a3247d8e`

```text
SUMMARY: a projector plays a fast, busy Christmas light show across a bedroom wall and the whole ceiling while a boy bounces on his bed. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, THE BOY and the colour.

SUBJECTS:
THE PROJECTOR - a Christmas projector switched on and running on the bedroom floor, out of shot. Its lens throws one wide cone of coloured light across the room. Everything glowing on the plaster is that cone landing.
THE SCREEN - the wall behind the bed and the whole ceiling together, catching that cone as one continuous surface. The light lands directly on bare plaster and wraps around the corner where wall meets ceiling. No rectangle, no visible screen edge, no television.
THE LIGHT SHOW - the animation playing on THE SCREEN: glowing six-point snowflakes, round dots and stars in red, green, blue, gold and white.
THE BOY - exactly one child in red-and-white Fair Isle pyjamas, bouncing on the bed.

THE LIGHT SHOW IS THE POINT OF THIS CLIP:
THE SCREEN itself is fixed to the plaster and never moves. Everything playing on it is RACING. This is not a shimmer and it is not a twinkle in place - every element travels a long, obvious distance across the plaster within four seconds, far enough that you can follow it with your eye.
- The snowflakes POUR downward fast, each one falling the full height of the wall in about one and a half seconds, fading out at the skirting board while fresh ones pour in along the ceiling line, so the fall never stops.
- Every flake spins as it falls and swings from side to side across its own path.
- Every flake flicks to a different colour about twice a second - red, green, blue, gold, white - so the whole wall keeps shifting colour.
- The round dots blink on and off rapidly like fast fairy lights, hundreds of them out of step with one another.
Because one lens feeds both surfaces, every event below plays on the wall and on the ceiling at the same instant and at the same speed.

TIMELINE:
0.0-1.0s SCREEN: a bright gold shooting star streaks diagonally from the top left of the wall down to the bottom right, leaving a short trail behind it, while the snow pours down the whole wall. BOY: bends his knees and pushes off the mattress, both feet leaving the duvet, arms swinging up over his head, mouth open laughing. CAMERA: holds.
1.0-2.0s SCREEN: a second shooting star crosses the ceiling from one corner to the other; the larger flakes swell bigger and shrink back down as they fall. BOY: lands on both feet and drives straight into a second, higher jump.
2.0-3.0s SCREEN: a wave of green sweeps across the wall and over the ceiling, every element flushing green as the wave passes, then the colours scatter apart again. CAMERA: tilts up in one slow smooth move until the ceiling fills the upper half of the frame.
3.0-4.0s SCREEN: a third shooting star crosses the ceiling, the dots burst outward in rings, and the snow keeps pouring at full speed. BOY: stays low in the frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take. The camera makes one move only, a tilt up. THE SCREEN stays bolted to the plaster while everything playing on it races across it. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; a frozen or still pattern; elements that stay in one place; the whole pattern turning or sliding as one sheet; any music; the projector unit in shot; a second child; a cut; on-screen text.
```

**Prompt** - `job 634f95a6`

```text
SUMMARY: a Christmas projector fills a bedroom wall and ceiling with falling snowflakes, stars and little Christmas trees of light while a boy bounces on his bed. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, THE BOY and the colour.

SUBJECTS:
THE PROJECTOR - a Christmas projector switched on and running on the bedroom floor, out of shot, throwing one wide cone of coloured light. Every glowing shape in the room is that cone landing.
THE SHAPES - glowing six-point snowflakes, small stars, little Christmas trees and round dots in red, green, blue, gold and white, scattered across the wall behind the bed, the ceiling, the bed and THE BOY himself.
THE BOY - exactly one child in red-and-white Fair Isle pyjamas, bouncing on the bed.

HOW THE SHAPES TRAVEL - this is the point of the clip:
Every shape is falling. Each one starts high, up along the line where the wall meets the ceiling, and travels downward for the whole four seconds, fast enough to cross the wall from the ceiling to the skirting board in about a second and a half. Follow any single one and you watch it pass landmark after landmark:
- a big white snowflake starts above the headboard, passes the top of the headboard at 0.5s, slides down over the pillows at 1.2s, crosses THE BOY's chest and sleeve at 2.0s, carries on down over the green duvet, and reaches the skirting board at 3.5s where it fades out;
- a gold star starts at the far corner of the ceiling and travels the length of the ceiling toward the camera, arrives at the line where ceiling meets wall at 2.5s, and keeps going down the wall from there;
- a red Christmas tree shape falls beside the headboard on the right, spinning as it drops, and arrives on the duvet at 3.0s.
Every other shape is doing the same thing at the same moment from a different starting height, so the wall and the ceiling are one continuous downpour of light for all four seconds. As each shape leaves the bottom, a fresh one appears up along the ceiling line and falls the same way, so the room never empties.
As they fall the shapes also spin on their own centres, swing sideways across their own paths, and flick to a new colour about twice a second.
One lens lights the wall and the ceiling together, so the downpour on the ceiling runs at the same instant and at the same speed as the downpour on the wall.
The start image catches this downpour at one instant only. From 0.0s every shape carries on falling from wherever it happens to be.

TIMELINE:
0.0-1.5s THE BOY bends his knees and pushes off the mattress, both feet leaving the duvet, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back. CAMERA holds.
1.5-2.5s THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking up.
2.5-4.0s CAMERA tilts up in one smooth move until the ceiling fills the upper half of the frame. THE BOY stays low in the frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take. The camera makes one move only, a tilt up. Every glowing shape is travelling downward across the plaster for the whole four seconds, covering real distance. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; any music; the projector unit in shot; a second child; a cut; on-screen text.
```

---

## C07 - Double-height living room

*Section:* B-roll 2 - the payoff  
*Status:* IN THE CUT  
*Clip in the cut:* `v1_c07_g6.mp4`  
*What it is:* The wide payoff — two kids, the girl caught mid-jump on the sofa

- frames: `v1_c07_g1.png`
- clips: `v1_c07_g1.mp4`, `v1_c07_g2.mp4`, `v1_c07_g3.mp4`, `v1_c07_g4.mp4`, `v1_c07_g5.mp4`, `v1_c07_g6.mp4`

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `v1_c07_g1.png` | our own g1 — the double-height room, projection, windows, tree and staircase all held; the projector goes, two kids arrive |

**Prompt** - `gpt_image_2 · 9:16 · 2k · medium`

```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same enormous double-height living room, the same Christmas light projection blanketing the whole ceiling and every wall — glowing Christmas trees, snowflakes, stars and baubles in blue, gold, green and red — the same tall black-framed windows on the left, the same big decorated Christmas tree, the same staircase with lit garland on the right, the same long cream sectional sofa and ottoman, the same camera position and height, the same magical low-key evening light.

CHANGE 1 — the projector unit must NOT be visible. Remove the small white glowing device and the round side table from the lower left completely. Replace that corner with plain rug and floor. No projector anywhere in frame.

CHANGE 2 — add TWO children to the room: a boy and a girl. The girl is JUMPING ON THE SOFA — caught mid-air above the cream sectional cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off. The boy stands on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room.

Both children are fully dressed in warm red-and-white knitted Christmas jumpers and matching knitted lounge trousers with thick socks. Wholesome family Christmas scene.

Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
```

> **What we read off it:** g2 — fixed. Projector and side table gone, two kids added at the right scale for the room, girl caught mid-air over the sofa cushions. Keeping them small preserves the “look how big this is” read — the room is still the subject, the kids are the human scale.

### CLIP — SEEDANCE 2.5 · v1_c07_g6.mp4 · SUBMITTED 19:55

**Attached to this job**

| slot | file | why |
|---|---|---|
| start_image | `v1_c07_g1.png` | frame 0.0 s |

**Clip prompt — the one in the cut** - `seedance_2_5 · 720p · 4 s · 9:16 · audio on`

```text
SUMMARY: two children play in a double-height Christmas living room while a projected snowflake field shimmers over every wall and the whole ceiling. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the room, the furniture, the children and the colour.

SUBJECTS:
THE GIRL - on the rug on the left, back to camera, spinning with her arms out.
THE BOY - on the right, jumping on the cream sectional sofa.
Exactly two children. No third child, no adult, no pet.
THE FIELD - the projected light: hundreds of small glowing snowflakes and dots in red, green, blue, gold and white, thrown by a single projector standing in the room, covering every wall and the whole ceiling as ONE continuous field.
THE ROOM - a tall lit Christmas tree centre, tall black-framed windows left, a staircase right, a cream sectional sofa right, an ottoman front centre, a rug on the floor. All of it survives to the last frame.

HOW THE FIELD BEHAVES - this is the point of the clip:
The field as a whole is ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is.
The motion lives INSIDE it. Every single snowflake is alive for all four seconds:
- each flake DRIFTS slowly downward and slightly sideways, about one flake-width every half second, the way real snow falls past a window at night;
- a flake that reaches the floor line fades out there, and a new flake fades in high near the ceiling, so the overall density never alters;
- each flake turns slowly on its own centre as it drifts;
- each flake breathes, brightening and dimming on its own timing, never all together;
- each flake's colour cycles slowly through red, green, blue and gold.
Every wall and the ceiling are lit by the SAME projector, so they are one field and behave identically at the same moment. Whatever the flakes on the walls are doing, the flakes on the ceiling are doing at the same instant, at the same speed.
Nothing is painted, printed or stencilled on the plaster. The start image is one paused frame of this; at 0.0s it un-pauses. Matching the start image applies to the room, the furniture, the children and the colours, not to where any individual flake sits.

FRAMING FIX: the start image has a dark unlit angular wedge of ceiling and a hard diagonal seam in the TOP RIGHT. It is gone by 1.0s, pushed out of frame by the camera step described below, and from 1.0s on the top right is ordinary lit ceiling carrying the same drifting field. There is no dark triangle and no hard diagonal cut-off anywhere after 1.0s.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles, and the dark wedge and the diagonal seam slide out of the top right. THE BOY bounces on the sofa cushion with his arms over his head, laughing. THE GIRL spins on the rug with her face turned up.
1.0-2.0s the camera holds in the closer position. THE BOY pushes off harder and both feet leave the cushion, which compresses and springs back. THE GIRL keeps turning and tips her head back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the ceiling fills the upper half of the frame, the same drifting field covering it. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, a sofa cushion compressing on each landing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. No slow motion, no floating, no speed ramp. Exactly two children. One continuous take. The field's outer boundary holds still while every flake inside it drifts, turns, breathes and shifts colour. Walls and ceiling always move together. THE BOY stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; the whole pattern rotating, spinning or sliding as one sheet; a frozen or still pattern; flakes that only twinkle in place without travelling; a still ceiling above moving walls; any music; blur; a dark unlit wedge or hard diagonal line in the top right after 1.0s; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; a cut; on-screen text.
```

**Other takes**

Takes not used (5)v1_c07_g1.mp4 · 17:29 — First pass — hold the start framePromptjob b2f0f418CopyTASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and projected pattern exactly.

[1] SUMMARY
Two excited children play in a Christmas living room covered in moving projected light, one jumping on the sofa; the camera tilts up to reveal the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the projected Christmas shapes and the lighting. It is the only authority on the scene.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out.
THE BOY - on the right, mid-jump on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Projected snowflakes, stars and candy canes in blue, gold and red cover the walls and continue onto the ceiling.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - camera locked wide. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward.
1.0-2.0s - THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up at the ceiling.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame, revealing the same Christmas shapes drifting and swirling across the ceiling. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. One camera movement: the upward tilt from 2.0s. No cut, no zoom, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the projection is the only bright moving light source, unchanged in character across the clip.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - natural room sound only: children laughing and squealing, cushions compressing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across walls and ceiling. Exactly two children. Both children are visibly excited and moving in every frame.
BANNED: a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, a frozen still pattern, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text, music.v1_c07_g2.mp4 · 17:55 — Audio rule + motion fixPromptjob a3be98ccCopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the ceiling looks half covered and the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely, and what replaces the top right is more of the same fully projected ceiling. From 1.0s onward the CEILING IS COMPLETELY AND EVENLY COVERED with moving projected Christmas shapes across its whole width, corner to corner, edge to edge, with NO dark patch, NO unlit triangle, NO bare plane, NO hard diagonal cut-off line anywhere. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and projected pattern exactly, apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room covered in moving projected light, one jumping on the sofa; the camera steps forward and tilts up to reveal a fully covered ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the look of the projected Christmas shapes and the lighting. It is a photograph - do not copy its stillness or its top-right framing problem, this clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Moving projected snowflakes, stars and candy canes in blue, gold and red cover the walls and the entire ceiling.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more fully projected ceiling. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward.
1.0-2.0s - the camera is now settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Projected shapes sweep visibly across the walls, the tree and the children.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame, revealing Christmas shapes drifting and swirling across the WHOLE ceiling, evenly covered corner to corner with no dark gap. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly shifting and sliding across them.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: children laughing and squealing, and cushions compressing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the walls and the ceiling. The ceiling is fully and evenly covered from 1.0s onward. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a half-covered ceiling; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.v1_c07_g3.mp4 · 18:21 — Audio rule + motion fix · scene-7.mp4Promptjob aa28629cCopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the walls and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the ceiling:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - every snowflake, star, candy cane and bauble, on the walls and on the ceiling alike - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the tree, the sofa and the children's faces and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

@Video 1 IS THE MOTION AUTHORITY FOR THE PROJECTED LIGHT AND FOR NOTHING ELSE. It was filmed in a real living room with a real rotating projector running. Copy from it exactly: the speed at which the projected shapes slide across the walls and the ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the furniture and over the people. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes and baubles in blue, gold and red, in the exact colours and styles shown in the start image. Do NOT copy its room, its furniture, its people, its flat blue colour, its captions or its audio.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely, and what replaces the top right is more of the same lit, moving ceiling. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and the LOOK of the projected shapes exactly - but not their stillness, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room washed in sliding projected light, one jumping on the sofa; the camera steps forward and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the projected Christmas shapes and the lighting. @Video 1 controls only HOW THAT LIGHT MOVES. The start image is a photograph - do not copy its stillness or its top-right framing problem, this clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Projected snowflakes, stars and candy canes in blue, gold and red sweep across the walls and the ceiling. The coverage is dense but uneven and constantly changing, because the field is sliding - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit, moving ceiling. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The projected field is already sliding down and to the right.
1.0-2.0s - the camera is now settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Projected shapes sweep visibly across the walls, the tree and the children.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. The same sliding Christmas projection is travelling across the ceiling at the same speed and in the same direction as on the walls, shapes entering at the upper left and leaving at the lower right. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly shifting and sliding across them.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: children laughing and squealing, and cushions compressing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected field slides continuously and visibly in every single frame, on the walls and on the ceiling. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall or ceiling; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.v1_c07_g4.mp4 · 18:44 — Audio rule + motion fixPromptjob 18ef173cCopyAUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
Every wall and the entire ceiling of this room are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes and baubles in blue, gold and red - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the tree, the sofa, the staircase and across the children's faces and pyjamas as it passes over them, so the light on everything is constantly shifting.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely and are replaced by more of the same lit ceiling with snow pouring across it. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and the LOOK of the Christmas shapes exactly - but not their stillness, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room where light-snow pours down every wall and the ceiling, one jumping on the sofa; the camera steps forward and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit only by the falling projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness or its top-right framing problem. This clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Falling light-snow covers the walls and the ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit ceiling with snow pouring across it. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The light-snow is already raining steadily down every wall.
1.0-2.0s - the camera is settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Glowing shapes pour visibly downward across the walls, down over the tree and down over both children, flakes clearly travelling from the top of frame towards the floor.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. Light-snow is pouring across the entire ceiling too, streaming away towards the far end of the room at the same speed. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[9] LIGHTING - warm dim room, the falling projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly pouring and shifting across them.

[10] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: children laughing and squealing, and cushions compressing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the walls and on the ceiling; a viewer can follow individual flakes travelling downward. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; snow that falls for a moment then stops; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.v1_c07_g5.mp4 · 19:21 — Rule Zero — motion is the only pass condition · scene_no_audio-7.mp4Promptjob d6a1e2c1CopyRULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on every wall and on the entire ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running in this exact kind of double-height living room. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the way the whole field of glowing shapes slides and swarms across the plaster without ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

WHAT THE LIGHT DOES, described so it cannot be mistaken for a texture:
- The whole field of glowing shapes SLIDES BODILY across the walls and across the ceiling, the way light from a spinning projector head sweeps a room. It never locks onto the plaster.
- On top of that sliding, individual shapes POUR DOWNWARD like heavy snowfall filmed through a window at night, and each one spins slowly as it goes and drags a faint soft trail.
- SPEED: a single shape crosses the full height of the wall in ABOUT ONE SECOND. That is fast. A viewer must see it moving within the first quarter second of the clip.
- THE TEST: take any two frames a third of a second apart and lay them on top of each other. NOT ONE glowing shape is in the same place. Not one. If any shape has stayed put, the clip is wrong.
- The moving light also pours down over the tree, the sofa, the staircase and across both children's faces and pyjamas as it passes over them, so the brightness on everything in the room is changing continuously.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

AUDIO RULE - SECOND MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FRAMING FIX RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely and are replaced by more of the same lit ceiling with light sweeping across it. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

IMAGE QUALITY RULE: the finished clip must look at least as sharp and as clean as the start image. Hold its exact sharpness, exposure, contrast and fine detail. Crisp modern phone footage, in focus throughout. BANNED: blur, soft focus, haze, mushy low-detail surfaces, plastic or waxy skin, colour shift, washed-out exposure, a dreamy or filtered look.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas, geometry and materials exactly - but NOT its stillness, NOT the position of its light pattern, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room while light sweeps and pours down every wall and the ceiling, one jumping on the sofa; the camera steps forward and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit only by the moving projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness or its top-right framing problem.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Sweeping, pouring light covers the walls and the ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit ceiling with light sweeping across it. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The field of light is already sliding and raining steadily down every wall.
1.0-2.0s - the camera is settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Glowing shapes sweep sideways and pour visibly downward across the walls, down over the tree and down over both children, clearly travelling from the top of frame towards the floor.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. The light is sweeping and pouring across the entire ceiling too, streaming away towards the far end of the room at the same speed. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[9] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly pouring and shifting across them. Do not flood the room with one flat colour.

[10] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: children laughing and squealing, and cushions compressing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child; an adult; the children standing still; jellyfish, fish, coral, bubbles or any underwater imagery; the projector unit visible anywhere in frame; a cut; subtitles; on-screen text.

**Prompt** - `job b2f0f418`

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and projected pattern exactly.

[1] SUMMARY
Two excited children play in a Christmas living room covered in moving projected light, one jumping on the sofa; the camera tilts up to reveal the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the projected Christmas shapes and the lighting. It is the only authority on the scene.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out.
THE BOY - on the right, mid-jump on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Projected snowflakes, stars and candy canes in blue, gold and red cover the walls and continue onto the ceiling.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - camera locked wide. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward.
1.0-2.0s - THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up at the ceiling.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame, revealing the same Christmas shapes drifting and swirling across the ceiling. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. One camera movement: the upward tilt from 2.0s. No cut, no zoom, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the projection is the only bright moving light source, unchanged in character across the clip.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - natural room sound only: children laughing and squealing, cushions compressing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across walls and ceiling. Exactly two children. Both children are visibly excited and moving in every frame.
BANNED: a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, a frozen still pattern, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text, music.
```

**Prompt** - `job a3be98cc`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the ceiling looks half covered and the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely, and what replaces the top right is more of the same fully projected ceiling. From 1.0s onward the CEILING IS COMPLETELY AND EVENLY COVERED with moving projected Christmas shapes across its whole width, corner to corner, edge to edge, with NO dark patch, NO unlit triangle, NO bare plane, NO hard diagonal cut-off line anywhere. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and projected pattern exactly, apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room covered in moving projected light, one jumping on the sofa; the camera steps forward and tilts up to reveal a fully covered ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the look of the projected Christmas shapes and the lighting. It is a photograph - do not copy its stillness or its top-right framing problem, this clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Moving projected snowflakes, stars and candy canes in blue, gold and red cover the walls and the entire ceiling.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more fully projected ceiling. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward.
1.0-2.0s - the camera is now settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Projected shapes sweep visibly across the walls, the tree and the children.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame, revealing Christmas shapes drifting and swirling across the WHOLE ceiling, evenly covered corner to corner with no dark gap. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly shifting and sliding across them.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: children laughing and squealing, and cushions compressing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the walls and the ceiling. The ceiling is fully and evenly covered from 1.0s onward. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a half-covered ceiling; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
```

**Prompt** - `job aa28629c`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the walls and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the ceiling:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - every snowflake, star, candy cane and bauble, on the walls and on the ceiling alike - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the tree, the sofa and the children's faces and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

@Video 1 IS THE MOTION AUTHORITY FOR THE PROJECTED LIGHT AND FOR NOTHING ELSE. It was filmed in a real living room with a real rotating projector running. Copy from it exactly: the speed at which the projected shapes slide across the walls and the ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the furniture and over the people. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes and baubles in blue, gold and red, in the exact colours and styles shown in the start image. Do NOT copy its room, its furniture, its people, its flat blue colour, its captions or its audio.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely, and what replaces the top right is more of the same lit, moving ceiling. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and the LOOK of the projected shapes exactly - but not their stillness, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room washed in sliding projected light, one jumping on the sofa; the camera steps forward and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the projected Christmas shapes and the lighting. @Video 1 controls only HOW THAT LIGHT MOVES. The start image is a photograph - do not copy its stillness or its top-right framing problem, this clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Projected snowflakes, stars and candy canes in blue, gold and red sweep across the walls and the ceiling. The coverage is dense but uneven and constantly changing, because the field is sliding - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit, moving ceiling. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The projected field is already sliding down and to the right.
1.0-2.0s - the camera is now settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Projected shapes sweep visibly across the walls, the tree and the children.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. The same sliding Christmas projection is travelling across the ceiling at the same speed and in the same direction as on the walls, shapes entering at the upper left and leaving at the lower right. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly shifting and sliding across them.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: children laughing and squealing, and cushions compressing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected field slides continuously and visibly in every single frame, on the walls and on the ceiling. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall or ceiling; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
```

**Prompt** - `job 18ef173c`

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
Every wall and the entire ceiling of this room are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes and baubles in blue, gold and red - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the tree, the sofa, the staircase and across the children's faces and pyjamas as it passes over them, so the light on everything is constantly shifting.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely and are replaced by more of the same lit ceiling with snow pouring across it. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and the LOOK of the Christmas shapes exactly - but not their stillness, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room where light-snow pours down every wall and the ceiling, one jumping on the sofa; the camera steps forward and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit only by the falling projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness or its top-right framing problem. This clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Falling light-snow covers the walls and the ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit ceiling with snow pouring across it. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The light-snow is already raining steadily down every wall.
1.0-2.0s - the camera is settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Glowing shapes pour visibly downward across the walls, down over the tree and down over both children, flakes clearly travelling from the top of frame towards the floor.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. Light-snow is pouring across the entire ceiling too, streaming away towards the far end of the room at the same speed. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[9] LIGHTING - warm dim room, the falling projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly pouring and shifting across them.

[10] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: children laughing and squealing, and cushions compressing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the walls and on the ceiling; a viewer can follow individual flakes travelling downward. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; snow that falls for a moment then stops; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
```

**Prompt** - `job d6a1e2c1`

```text
RULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on every wall and on the entire ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running in this exact kind of double-height living room. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the way the whole field of glowing shapes slides and swarms across the plaster without ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

WHAT THE LIGHT DOES, described so it cannot be mistaken for a texture:
- The whole field of glowing shapes SLIDES BODILY across the walls and across the ceiling, the way light from a spinning projector head sweeps a room. It never locks onto the plaster.
- On top of that sliding, individual shapes POUR DOWNWARD like heavy snowfall filmed through a window at night, and each one spins slowly as it goes and drags a faint soft trail.
- SPEED: a single shape crosses the full height of the wall in ABOUT ONE SECOND. That is fast. A viewer must see it moving within the first quarter second of the clip.
- THE TEST: take any two frames a third of a second apart and lay them on top of each other. NOT ONE glowing shape is in the same place. Not one. If any shape has stayed put, the clip is wrong.
- The moving light also pours down over the tree, the sofa, the staircase and across both children's faces and pyjamas as it passes over them, so the brightness on everything in the room is changing continuously.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

AUDIO RULE - SECOND MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FRAMING FIX RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely and are replaced by more of the same lit ceiling with light sweeping across it. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

IMAGE QUALITY RULE: the finished clip must look at least as sharp and as clean as the start image. Hold its exact sharpness, exposure, contrast and fine detail. Crisp modern phone footage, in focus throughout. BANNED: blur, soft focus, haze, mushy low-detail surfaces, plastic or waxy skin, colour shift, washed-out exposure, a dreamy or filtered look.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas, geometry and materials exactly - but NOT its stillness, NOT the position of its light pattern, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room while light sweeps and pours down every wall and the ceiling, one jumping on the sofa; the camera steps forward and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit only by the moving projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness or its top-right framing problem.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Sweeping, pouring light covers the walls and the ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit ceiling with light sweeping across it. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The field of light is already sliding and raining steadily down every wall.
1.0-2.0s - the camera is settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Glowing shapes sweep sideways and pour visibly downward across the walls, down over the tree and down over both children, clearly travelling from the top of frame towards the floor.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. The light is sweeping and pouring across the entire ceiling too, streaming away towards the far end of the room at the same speed. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[9] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly pouring and shifting across them. Do not flood the room with one flat colour.

[10] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: children laughing and squealing, and cushions compressing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child; an adult; the children standing still; jellyfish, fish, coral, bubbles or any underwater imagery; the projector unit visible anywhere in frame; a cut; subtitles; on-screen text.
```

---

---

## Board metadata (archived from board.meta.json, 2026-09-18)

**Final cut order** - the order the shots appear in the edit,
which is not always the order the cards sit in on the board.

```
C01 → C02 → C03 → C04 → C05 → C06 → C07 C01 and C05 each cut two frames inside one clip
```

**Stats trimmed off the lane panel**

| field | value |
|---|---|
| Stage | Final cut |
| Frames | gpt_image_2 |
| Clips | seedance_2_5 · 720p → 2K |
| Source reel | AquaWish |

**Shot notes**

- `c01` - Framing, cart and head-turn held. Store dressed with trees, garland and hanging baubles; aisle depth matches the source.
- `c02` - Best packaging read of the set — headline, wordmark and the 16 Patterns / Remote Control / Timer strip all legible. Table dressing sits at the edges so the carton stays the subject.
- `c03` - g3 — my prompt was the bug, not the model. g2 described the background as “a warm modern kitchen, softly out of focus” and never once mentioned the countertop, so the model dropped it and filled the bottom half with floor. It rendered exactly what was asked. g3 names the counter as a thing that must be in frame, says where it sits, and bans the failure outright — “DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.” The counter block and the kitchen block are now word for word identical in C03 and C04 so both shots read as the same island.
- `c04` - g3 — I mis-read the reference, then wrote the mistake into the prompt. ref05 is a close, shallow downward angle with the product large in frame. I described it as “a HIGH DOWNWARD ANGLE… tilted down roughly 45 degrees… small in frame with a lot of counter around it” — and the model delivered that faithfully. The lesson is to describe the reference from the reference, not from memory of it. g3 leads with the camera, says the angle is shallow and the product large, and bans the four ways it went wrong by name. Two jobs wasted on a reference that was open in front of me the whole time.
- `c05` - g2 — fixed. g1 ran a full-height rainbow strip down the door edge, which gives the reveal away before the cut. Door is now flush and the seam is a plain shadow line. Feeding our own g1 back as the reference held the wreath, knob and hand exactly — far tighter than re-describing the hallway from scratch.
- `c06` - g2 — fixed. Projector and stool removed; the boy is up on the mattress mid-bounce with the duvet dimpling under his feet, which is the pose the clip needs to animate into a jump. Sitting on the bed edge (g1) had nowhere to go.
- `c07` - g2 — fixed. Projector and side table gone, two kids added at the right scale for the room, girl caught mid-air over the sofa cushions. Keeping them small preserves the “look how big this is” read — the room is still the subject, the kids are the human scale.


## File traceability — verified 2026-09-21

This inventory accounts for local media. It does **not** certify that every historical take has a full prompt. Recovered records below supplement the original shot sections; they do not change the selected take. Image and clip take numbers are independent. A matching stem is not evidence that a clip used that image.

| Local file (relative to this archive) | Evidence / status |
|---|---|
| `clips/upscaled/v1_c01_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v1_c02_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v1_c03_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v1_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v1_c05_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v1_c06_g8.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v1_c07_g6.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c01_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c01_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c02_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c02_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c03_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c04_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c05_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c05_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c05_g4.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c05_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c05_g6.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c05_g7.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g10.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g4.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g6.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g7.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g8.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c06_g9.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c07_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c07_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c07_g4.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c07_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v1_c07_g6.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v1_c01_r1.png` | Embedded PNG `hf-job-id`: `f856f2d8-3780-4d1a-a59a-1761fa8d19a2`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v1_c05_r1.png` | Embedded PNG `hf-job-id`: `9a799ad8-0d8c-49de-9f8b-82b9d920dc38`. Exact service prompt and returned parameters recovered below. |
| `references/v1_c05_r2.png` | Embedded PNG `hf-job-id`: `602a896a-3f45-4638-8604-0569f9547aa7`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c01_g1.png` | Embedded PNG `hf-job-id`: `f6401335-a937-4621-8c87-b1885795abd0`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c02_g1.png` | Embedded PNG `hf-job-id`: `069cf5d0-38f6-4faa-b102-42bb2887c30f`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c03_g1.png` | Embedded PNG `hf-job-id`: `2603e3e9-bc93-4c54-b884-78a45cd30f7b`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c03_g2.png` | Embedded PNG `hf-job-id`: `c299703a-9594-42a8-bea7-74fd78ea5544`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c03_g3.png` | Embedded PNG `hf-job-id`: `fb902941-abc4-441f-97aa-509a143e3983`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v1_c04_g1.png` | Embedded PNG `hf-job-id`: `da3b103f-361c-415c-8ca0-a19a5403d0d7`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c04_g2.png` | Embedded PNG `hf-job-id`: `85380c7a-5da3-47c9-b62f-e500c5c3ccd0`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c04_g3.png` | Embedded PNG `hf-job-id`: `54c37f6c-0e31-44bb-9cf0-4c18e7a69f83`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v1_c05_g1.png` | Embedded PNG `hf-job-id`: `7a255476-516b-4c2d-b3e3-e98e05a8096c`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c05_g2.png` | Embedded PNG `hf-job-id`: `c0e36341-9fe3-45e9-a792-2131ba5b073f`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c06_g1.png` | Embedded PNG `hf-job-id`: `54aa9693-6cf0-46ae-bb75-3daef60aef45`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c06_g2.png` | Embedded PNG `hf-job-id`: `7bf26c13-2c47-41e8-bd9a-8c09b7cb46ad`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c07_g1.png` | Embedded PNG `hf-job-id`: `3a88d6da-3303-4655-8601-58d8c276034e`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v1_c07_g2.png` | Embedded PNG `hf-job-id`: `7a5cb60b-0a26-4555-921b-a51c18f7ba42`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |

### Recovered take — `references/v1_c05_r1.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `9a799ad8-0d8c-49de-9f8b-82b9d920dc38`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
Copy the attached reference photo's FRAMING exactly: same camera position, same height, same distance, same vertical 9:16 composition, two young siblings placed in exactly the same spots and same seated poses as the two figures in the reference, facing the same direction, seen mostly from behind. Everything else changes. This is a DIFFERENT living room from the reference — a cosy, heavily Christmas-decorated family living room with a decorated fir tree, stockings on the mantel, a sofa with knitted throws, wrapped gifts on the floor. The two siblings are different children, around five and seven years old, both fully dressed in warm red-and-white knitted Christmas jumpers and matching lounge trousers, thick socks. A smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base sits low in the room, throwing light UP from the top of its dome. An animated Christmas light projection covers every surface — walls, ceiling, furniture: dense falling snowflakes, glowing green fir trees, golden stars, red and gold baubles, candy canes, in a warm gold and cool blue palette. The projection behaves like real projected light — flat, slightly translucent, wrapping and distorting as it crosses furniture and corners, brightest on flat walls, fading in shadowed recesses. No decals, no printed wallpaper, no stickers. The room is otherwise dark so the projection reads bright. Wholesome family Christmas scene. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, clean low-light exposure with no grain or smear, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "f3042793-315d-4b74-9ec5-988d9973ce92",
        "type": "media_input",
        "url": "https://d2ol7oe51mr4n9.cloudfront.net/user_REMOVED/f3042793-315d-4b74-9ec5-988d9973ce92.png"
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


### Recovered take — `starting_frames/v1_c03_g3.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `fb902941-abc4-441f-97aa-509a143e3983`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
COPY @Image 1 EXACTLY. The ONLY thing that changes is the kitchen behind her. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, the jewellery, the sleeve, and the white marble countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the bright white marble countertop occupies the LOWER RIGHT of the frame as a clean pale wedge running diagonally, passing behind and below her right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE — her two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but her fingers, with a visible gap of air between the base of the stand and the marble below. Left forearm enters from the lower left in a cream ribbed knit sleeve pushed back; right forearm enters from the right with a thin gold bangle at the wrist and two slim gold rings on the fingers. Fair skin, neat natural nails.

SCALE AND PLACEMENT — the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT — a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER — honed white marble with soft cool-grey veining and a squared edge, matte sheen.

THE KITCHEN — this is the only change. A warm modern kitchen, softly defocused: pale greige flat-front shaker cabinets with slim brushed-brass bar pulls, a stainless steel wall oven built into the tall cabinet run on the left, a white marble slab backsplash, a warm white LED strip glowing under the upper cabinets, and a pine garland with small warm fairy lights running high along the top of the cabinetry. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfectly exposed, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "77045fb2-b216-459e-8d4c-fd77c9e05d9a",
        "type": "media_input",
        "url": "https://d2ol7oe51mr4n9.cloudfront.net/user_REMOVED/77045fb2-b216-459e-8d4c-fd77c9e05d9a.png"
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


### Recovered take — `starting_frames/v1_c04_g3.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `54c37f6c-0e31-44bb-9cf0-4c18e7a69f83`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
COPY @Image 1 EXACTLY. The ONLY thing that changes is the kitchen behind her. Everything else is a literal copy.

CAMERA — this is the part that went wrong last time, so follow it precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently — a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The marble surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT — standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS — exactly as in @Image 1. Her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; on that wrist a stack of thin gold bangles, beige ribbed knit sleeve pushed back. Her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. Two slim gold rings on that hand. The white cable trails away to the right across the marble and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER — honed white marble with soft cool-grey veining and a squared edge, matte sheen.

THE KITCHEN — this is the only change. A warm modern kitchen, softly defocused across the top third of the frame: pale greige flat-front shaker cabinets with slim brushed-brass bar pulls, a stainless steel wall oven built into the tall cabinet run on the right, a white marble slab backsplash, a warm white LED strip glowing under the upper cabinets, and a pine garland with small warm fairy lights running high along the top of the cabinetry. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfectly exposed, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "64b95049-8d7f-4357-9871-3bac534a4929",
        "type": "media_input",
        "url": "https://d2ol7oe51mr4n9.cloudfront.net/user_REMOVED/64b95049-8d7f-4357-9871-3bac534a4929.png"
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

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C01: the board did not show the exact image prompt of `v1_c01_g1.png`; it now does.
- C01: the board did not show the exact image prompt of `v1_c01_r1.png`; it now does.
- C02: the board did not show the exact image prompt of `v1_c02_g1.png`; it now does.
- C03: the board did not show the exact image prompt of `v1_c03_g3.png`; it now does.
- C03: the board showed `v1_c03_g1.png` as the start frame, but the clip in the cut was animated from `v1_c03_g3.png` (Higgsfield start image, pixel-matched). Board corrected.
- C04: the board did not show the exact image prompt of `v1_c04_g3.png`; it now does.
- C04: the board showed `v1_c04_g1.png` as the start frame, but the clip in the cut was animated from `v1_c04_g3.png` (Higgsfield start image, pixel-matched). Board corrected.
- C05: the board did not show the exact image prompt of `v1_c05_g2.png`; it now does.
- C05: the board did not show the exact image prompt of `v1_c05_r2.png`; it now does.
- C05: the board showed `v1_c05_g1.png` as the start frame, but the clip in the cut was animated from `v1_c05_g2.png` (Higgsfield start image, pixel-matched). Board corrected.
- C06: the board did not show the exact image prompt of `v1_c06_g2.png`; it now does.
- C06: the board showed `v1_c06_g1.png` as the start frame, but the clip in the cut was animated from `v1_c06_g2.png` (Higgsfield start image, pixel-matched). Board corrected.
- C07: the board did not show the exact image prompt of `v1_c07_g2.png`; it now does.
- C07: the board showed `v1_c07_g1.png` as the start frame, but the clip in the cut was animated from `v1_c07_g2.png` (Higgsfield start image, pixel-matched). Board corrected.

### C01 — Store aisle walk → the pallet

**In the cut:** `starting_frames/v1_c01_g1.png`, `references/v1_c01_r1.png` → `clips/v1_c01_g3.mp4`

#### Image prompt — `starting_frames/v1_c01_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `f6401335-a937-4621-8c87-b1885795abd0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142340_f6401335-a937-4621-8c87-b1885795abd0.png
**References, in submission order**
- @Image 1: `references/ref01.png` · Higgsfield media `95c37a95-4490-4b56-af4a-fdf3e4991fbd`

````text
Copy the attached reference photo EXACTLY: same camera position, same height, same lens, same distance, same vertical 9:16 framing, same supermarket aisle receding into depth, same shelving on both sides, same floor, same ceiling lights, same shopping cart in the same spot and same angle, same body pose and same head turn. Change only two things. FIRST: the woman is now about 35 years old, natural everyday face, no makeup look, casual winter outfit, hair down, pushing the same cart in the same pose. SECOND: the store is now decorated for Christmas — garlands of green fir and red ribbon wrapped along the shelf edges, small warm white fairy lights strung across the aisle, a few red and gold baubles hanging from the ceiling, festive red and green product displays on the shelves. Everything else in the frame stays identical to the reference. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, natural realistic store lighting, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Image prompt — `references/v1_c01_r1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `f856f2d8-3780-4d1a-a59a-1761fa8d19a2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142341_f856f2d8-3780-4d1a-a59a-1761fa8d19a2.png
**References, in submission order**
- @Image 1: `references/ref02.png` · Higgsfield media `73541734-3ba4-4b16-922f-4a1e1aee4d04`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `e836baed-2bc4-410b-adcb-b17b23f228b8`

````text
Copy the FIRST attached reference photo's framing EXACTLY: same camera position, same height, same distance, same angle onto the retail shelf/pallet stacked full of identical product cartons, same vertical 9:16 crop, same surrounding store aisle and shelving visible at the edges, same lighting. Replace every carton on that shelf with OUR product box, shown in the SECOND attached reference: a tall upright rectangular tuck-top carton with a square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector standing on a separate white four-legged splayed stand base, a slim red remote printed beside it, a gold village skyline along the bottom. No transparent window anywhere on the carton. The boxes are stacked neatly, rows deep, all facing the camera, identical to each other. Same supermarket as the aisle reference, decorated for Christmas with fir garland and warm fairy lights along the shelf edge. Shot on iPhone, photorealistic, tack-sharp focus, crisp readable packaging detail, natural realistic store lighting, no motion blur, no extra text beyond the packaging copy, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Video prompt — `clips/v1_c01_g3.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `73c4db86-5a0f-4ec9-a6a1-dc237587e7af`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_184937_73c4db86-5a0f-4ec9-a6a1-dc237587e7af.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v1_c01_g3.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c01_g1.png` · Higgsfield media `c940eb75-8e49-4556-8957-1d2d44922c62`
- image ref 1: `content/video_1_assets/references/v1_c01_r1.png` · Higgsfield media `1ef91ac0-83b4-4680-a5bb-f14d08731e7b`
- video ref 1: `references/scene_no_audio-1.mp4` — silenced upload · 3.93 s · Higgsfield media `d036fd39-f69d-4d62-9d76-c4f136c562f0`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room plus the spoken line. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

TASK: image-to-video. The start image is frame 0.0s. Hold its wardrobe, store, lighting and lens exactly.

[1] SUMMARY
A woman in a supermarket Christmas aisle stops her trolley, reacts in shock and points off-camera; the camera whip-pans right onto a pallet of dark-green product boxes. Handheld vertical UGC. 4 seconds, one continuous take with one whip pan.

[2] GLOBAL STYLE
Real handheld phone footage filmed by a friend walking behind her. Natural retail lighting warmed by the red and gold decorations. Extremely sharp, clean, well exposed. Subtle handheld breathing throughout. The ONLY blur in the clip is the deliberate horizontal motion blur inside the whip pan. No cinematic grade, no film grain, no vignette, no slow motion.

[3] ASSET ROLES
The start image controls the woman's identity, her cream knit sweater and dark jeans, the aisle, the shelving and the lighting. @Image 1 controls ONLY the look of the product pallet the pan lands on: a tall stack of DARK-GREEN cartons with a red banner and a white projector illustration, with red poinsettia and garland on top. Do not copy camera angle or lighting from @Image 1. @Video 1 controls ONLY the camera path and the rhythm of the performance: walk, stop, hand to mouth, point, whip pan right, settle on the product stack. Do not copy the woman, her clothes, the trolley colour, the store or the boxes from @Video 1. @Video 1 is silent - there is no audio, no music and no soundtrack in it to copy.

[4] CHARACTERS
THE WOMAN - long light-brown hair, cream oatmeal knit sweater, dark jeans, seen from behind and slightly to her left. COUNT LOCK: exactly one person on screen for all 4 seconds. No other shoppers, no staff, no children.

[5] LOCATION - every one of these exists in the start image and must survive to the last frame before the pan: a wide polished pale-floor supermarket aisle; decorated Christmas trees with red and gold ornaments standing on top of the left-hand shelves; red baubles hanging from the ceiling; red-accented shelving on the right. THE TROLLEY - the dark grey shopping trolley she is pushing.

[6] FIRST FRAME - exactly the start image: THE WOMAN from behind and slightly left, both hands on THE TROLLEY handle, mid-aisle, walking away from camera.

[7] TIMELINE
0.0-1.0s - camera handheld, follows THE WOMAN from behind at walking pace; THE WOMAN pushes THE TROLLEY forward two steps.
1.0-2.0s - THE WOMAN releases the handle and takes one step forward ahead of THE TROLLEY. THE TROLLEY keeps rolling forward on its own down the aisle, unpushed. Her right hand flies up and covers her mouth; her head turns to her right; her shoulders lift. Camera holds.
2.0-3.0s - THE WOMAN drops the hand from her mouth and throws her right arm straight out, index finger pointing forward and to the right, off the right edge of frame. THE WOMAN speaks. Camera holds.
3.0-4.0s - as her arm reaches full extension the camera WHIP PANS hard to the right with heavy horizontal motion blur; THE WOMAN leaves frame to the left; the pan decelerates and settles on the tall pallet of DARK-GREEN product cartons from @Image 1 standing in the aisle with red poinsettia and garland on top. Tiny push-in and hold.

[8] DIALOGUE
English dialogue. THE WOMAN: "There is no way!" Spoken 2.1-2.9s. Delivery: loud, delighted, genuinely stunned, American accent. This spoken line is the ONLY voice in the clip. No subtitles, no on-screen text.

[9] CAMERA AND OPTICS - single continuous handheld take, vertical 9:16, normal wide-angle phone lens, chest height, about two metres behind THE WOMAN, her body in the centre-left third. One camera movement only: the whip pan right at 3.0s. Do not cut. Do not zoom. Do not orbit. No fisheye, no barrel distortion, no warped shelving or curved floor lines.

[10] LIGHTING - flat overhead retail lighting with warm pools under the decorations, clean white balance, no colour cast change across the clip.

[11] PHYSICS - THE TROLLEY rolls straight and slows gradually under its own momentum after she lets go; it never turns, never tips, never leaves the floor, never stops dead. Her sweater and hair move naturally with her turn.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: low supermarket room ambience, the rattle of trolley wheels on the hard floor, and her single spoken line. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - exactly one person. THE TROLLEY continues forward alone after 1.0s. The aisle, the decorated trees on the shelf tops and the hanging red baubles are present in every frame before the pan. The pan lands on cartons that are DARK GREEN with a red banner.
BANNED: any music, any song, any score, any soundtrack, any instrument, any singing; a second shopper, the trolley stopping dead or vanishing, THE WOMAN turning to face the camera, any cut, blue or white or brown or kraft boxes, a shelf of unrelated products, subtitles, on-screen text, slow motion, any blur outside the pan.
````

**Other takes of C01 on disk (2)**

#### Video prompt — `clips/v1_c01_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `b655c5a6-5988-40dc-a35f-6b9315920ce4`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_172938_b655c5a6-5988-40dc-a35f-6b9315920ce4.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c01_g1.png` · Higgsfield media `c940eb75-8e49-4556-8957-1d2d44922c62`
- image ref 1: `content/video_1_assets/references/v1_c01_r1.png` · Higgsfield media `1ef91ac0-83b4-4680-a5bb-f14d08731e7b`
- video ref 1: uploaded image, not on the drive · Higgsfield media `4916f99a-a552-436e-9abb-b4d70c3d3055`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its wardrobe, store, lighting and lens exactly.

[1] SUMMARY
A woman in a supermarket Christmas aisle stops her trolley, reacts in shock and points off-camera; the camera whip-pans right onto a pallet of dark-green product boxes. Handheld vertical UGC. 4 seconds, one continuous take with one whip pan.

[2] GLOBAL STYLE
Real handheld phone footage filmed by a friend walking behind her. Natural retail lighting warmed by the red and gold decorations. Extremely sharp, clean, well exposed. Subtle handheld breathing throughout. The ONLY blur in the clip is the deliberate horizontal motion blur inside the whip pan. No cinematic grade, no film grain, no vignette, no slow motion.

[3] ASSET ROLES
The start image controls the woman's identity, her cream knit sweater and dark jeans, the aisle, the shelving and the lighting. @Image 1 controls ONLY the look of the product pallet the pan lands on: a tall stack of DARK-GREEN cartons with a red banner and a white projector illustration, with red poinsettia and garland on top. Do not copy camera angle or lighting from @Image 1. @Video 1 controls ONLY the camera path and the rhythm of the performance: walk, stop, hand to mouth, point, whip pan right, settle on the product stack. Do not copy the woman, her clothes, the trolley colour, the store or the boxes from @Video 1.

[4] CHARACTERS
THE WOMAN - long light-brown hair, cream oatmeal knit sweater, dark jeans, seen from behind and slightly to her left. COUNT LOCK: exactly one person on screen for all 4 seconds. No other shoppers, no staff, no children.

[5] LOCATION - every one of these exists in the start image and must survive to the last frame before the pan: a wide polished pale-floor supermarket aisle; decorated Christmas trees with red and gold ornaments standing on top of the left-hand shelves; red baubles hanging from the ceiling; red-accented shelving on the right. THE TROLLEY - the dark grey shopping trolley she is pushing.

[6] FIRST FRAME - exactly the start image: THE WOMAN from behind and slightly left, both hands on THE TROLLEY handle, mid-aisle, walking away from camera.

[7] TIMELINE
0.0-1.0s - camera handheld, follows THE WOMAN from behind at walking pace; THE WOMAN pushes THE TROLLEY forward two steps.
1.0-2.0s - THE WOMAN releases the handle and takes one step forward ahead of THE TROLLEY. THE TROLLEY keeps rolling forward on its own down the aisle, unpushed. Her right hand flies up and covers her mouth; her head turns to her right; her shoulders lift. Camera holds.
2.0-3.0s - THE WOMAN drops the hand from her mouth and throws her right arm straight out, index finger pointing forward and to the right, off the right edge of frame. THE WOMAN speaks. Camera holds.
3.0-4.0s - as her arm reaches full extension the camera WHIP PANS hard to the right with heavy horizontal motion blur; THE WOMAN leaves frame to the left; the pan decelerates and settles on the tall pallet of DARK-GREEN product cartons from @Image 1 standing in the aisle with red poinsettia and garland on top. Tiny push-in and hold.

[8] DIALOGUE
English dialogue. THE WOMAN: "There is no way!" Spoken 2.1-2.9s. Delivery: loud, delighted, genuinely stunned, American accent. No subtitles, no on-screen text.

[9] CAMERA AND OPTICS - single continuous handheld take, vertical 9:16, normal wide-angle phone lens, chest height, about two metres behind THE WOMAN, her body in the centre-left third. One camera movement only: the whip pan right at 3.0s. Do not cut. Do not zoom. Do not orbit. No fisheye, no barrel distortion, no warped shelving or curved floor lines.

[10] LIGHTING - flat overhead retail lighting with warm pools under the decorations, clean white balance, no colour cast change across the clip.

[11] PHYSICS - THE TROLLEY rolls straight and slows gradually under its own momentum after she lets go; it never turns, never tips, never leaves the floor, never stops dead. Her sweater and hair move naturally with her turn.

[12] AUDIO - natural room sound only: supermarket ambience, trolley wheels on hard floor, her voice. No music, no score, no background song.

[13] POSITIVE LOCKS - exactly one person. THE TROLLEY continues forward alone after 1.0s. The aisle, the decorated trees on the shelf tops and the hanging red baubles are present in every frame before the pan. The pan lands on cartons that are DARK GREEN with a red banner.
BANNED: a second shopper, the trolley stopping dead or vanishing, THE WOMAN turning to face the camera, any cut, blue or white or brown or kraft boxes, a shelf of unrelated products, subtitles, on-screen text, music, slow motion, any blur outside the pan.
````

#### Video prompt — `clips/v1_c01_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `377edec4-d967-4eb4-bdd8-9ca4f6bd5383`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175511_377edec4-d967-4eb4-bdd8-9ca4f6bd5383.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c01_g1.png` · Higgsfield media `c940eb75-8e49-4556-8957-1d2d44922c62`
- image ref 1: `content/video_1_assets/references/v1_c01_r1.png` · Higgsfield media `1ef91ac0-83b4-4680-a5bb-f14d08731e7b`
- video ref 1: uploaded image, not on the drive · Higgsfield media `4916f99a-a552-436e-9abb-b4d70c3d3055`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room plus the spoken line. If any music appears anywhere in the 4 seconds the clip is wrong.

TASK: image-to-video. The start image is frame 0.0s. Hold its wardrobe, store, lighting and lens exactly.

[1] SUMMARY
A woman in a supermarket Christmas aisle stops her trolley, reacts in shock and points off-camera; the camera whip-pans right onto a pallet of dark-green product boxes. Handheld vertical UGC. 4 seconds, one continuous take with one whip pan.

[2] GLOBAL STYLE
Real handheld phone footage filmed by a friend walking behind her. Natural retail lighting warmed by the red and gold decorations. Extremely sharp, clean, well exposed. Subtle handheld breathing throughout. The ONLY blur in the clip is the deliberate horizontal motion blur inside the whip pan. No cinematic grade, no film grain, no vignette, no slow motion.

[3] ASSET ROLES
The start image controls the woman's identity, her cream knit sweater and dark jeans, the aisle, the shelving and the lighting. @Image 1 controls ONLY the look of the product pallet the pan lands on: a tall stack of DARK-GREEN cartons with a red banner and a white projector illustration, with red poinsettia and garland on top. Do not copy camera angle or lighting from @Image 1. @Video 1 controls ONLY the camera path and the rhythm of the performance: walk, stop, hand to mouth, point, whip pan right, settle on the product stack. Do not copy the woman, her clothes, the trolley colour, the store or the boxes from @Video 1. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] CHARACTERS
THE WOMAN - long light-brown hair, cream oatmeal knit sweater, dark jeans, seen from behind and slightly to her left. COUNT LOCK: exactly one person on screen for all 4 seconds. No other shoppers, no staff, no children.

[5] LOCATION - every one of these exists in the start image and must survive to the last frame before the pan: a wide polished pale-floor supermarket aisle; decorated Christmas trees with red and gold ornaments standing on top of the left-hand shelves; red baubles hanging from the ceiling; red-accented shelving on the right. THE TROLLEY - the dark grey shopping trolley she is pushing.

[6] FIRST FRAME - exactly the start image: THE WOMAN from behind and slightly left, both hands on THE TROLLEY handle, mid-aisle, walking away from camera.

[7] TIMELINE
0.0-1.0s - camera handheld, follows THE WOMAN from behind at walking pace; THE WOMAN pushes THE TROLLEY forward two steps.
1.0-2.0s - THE WOMAN releases the handle and takes one step forward ahead of THE TROLLEY. THE TROLLEY keeps rolling forward on its own down the aisle, unpushed. Her right hand flies up and covers her mouth; her head turns to her right; her shoulders lift. Camera holds.
2.0-3.0s - THE WOMAN drops the hand from her mouth and throws her right arm straight out, index finger pointing forward and to the right, off the right edge of frame. THE WOMAN speaks. Camera holds.
3.0-4.0s - as her arm reaches full extension the camera WHIP PANS hard to the right with heavy horizontal motion blur; THE WOMAN leaves frame to the left; the pan decelerates and settles on the tall pallet of DARK-GREEN product cartons from @Image 1 standing in the aisle with red poinsettia and garland on top. Tiny push-in and hold.

[8] DIALOGUE
English dialogue. THE WOMAN: "There is no way!" Spoken 2.1-2.9s. Delivery: loud, delighted, genuinely stunned, American accent. This spoken line is the ONLY voice in the clip. No subtitles, no on-screen text.

[9] CAMERA AND OPTICS - single continuous handheld take, vertical 9:16, normal wide-angle phone lens, chest height, about two metres behind THE WOMAN, her body in the centre-left third. One camera movement only: the whip pan right at 3.0s. Do not cut. Do not zoom. Do not orbit. No fisheye, no barrel distortion, no warped shelving or curved floor lines.

[10] LIGHTING - flat overhead retail lighting with warm pools under the decorations, clean white balance, no colour cast change across the clip.

[11] PHYSICS - THE TROLLEY rolls straight and slows gradually under its own momentum after she lets go; it never turns, never tips, never leaves the floor, never stops dead. Her sweater and hair move naturally with her turn.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: low supermarket room ambience, the rattle of trolley wheels on the hard floor, and her single spoken line. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - exactly one person. THE TROLLEY continues forward alone after 1.0s. The aisle, the decorated trees on the shelf tops and the hanging red baubles are present in every frame before the pan. The pan lands on cartons that are DARK GREEN with a red banner.
BANNED: any music, any song, any score, any soundtrack, any instrument, any singing; a second shopper, the trolley stopping dead or vanishing, THE WOMAN turning to face the camera, any cut, blue or white or brown or kraft boxes, a shelf of unrelated products, subtitles, on-screen text, slow motion, any blur outside the pan.
````

### C02 — Hands on the box

**In the cut:** `starting_frames/v1_c02_g1.png` → `clips/v1_c02_g3.mp4`

#### Image prompt — `starting_frames/v1_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `069cf5d0-38f6-4faa-b102-42bb2887c30f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142340_069cf5d0-38f6-4faa-b102-42bb2887c30f.png
**References, in submission order**
- @Image 1: `references/ref03.png` · Higgsfield media `cc58af5b-3d75-4e53-99b5-57e43c0703fa`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `e836baed-2bc4-410b-adcb-b17b23f228b8`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same wooden table surface, same two hands resting on the box in the same position and same grip, same arms entering frame the same way, same background depth. Replace the box with OUR product box from the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle the original box occupied. Dress the wooden table more festively: a sprig of fir and a few red berries, two or three small gold and red baubles, a short cream candle, a soft warm string light trailing across the wood, all at the edges of frame so the box stays the clear subject. Shot on iPhone, photorealistic, tack-sharp focus, crisp readable packaging detail, warm natural window light, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Video prompt — `clips/v1_c02_g3.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `81f1a189-c494-4408-ae60-618e137dabf4`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_184455_81f1a189-c494-4408-ae60-618e137dabf4.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v1_c02_g3.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c02_g1.png` · Higgsfield media `55e74114-74c8-446a-9885-25f174c60dec`
- video ref 1: `references/scene_no_audio-2.mp4` — silenced upload · 2.13 s · Higgsfield media `14a9bd36-39da-4d5f-bed0-026f90c39c25`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

EXIT RULE - SECOND MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - THIRD MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a wooden table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, gold THEXMASGLOW banner, the words CHRISTMAS LIGHT PROJECTOR, a white projector on a red circle. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray, no window.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a cream knit sleeve on the left wrist, a thin gold bracelet on the right wrist.

[5] LOCATION - a dark round wooden table fills the frame. A lit cream pillar candle sits at the top left, holly sprigs with red berries beside it, warm fairy lights out of focus behind. The candle, the holly and the fairy lights must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the wooden table, lid flaps folded back, with the candle, the holly and the fairy lights still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle or the holly disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
````

**Other takes of C02 on disk (2)**

#### Video prompt — `clips/v1_c02_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `28aba27c-20f4-40d2-b4e4-9b800bbead5c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_172938_28aba27c-20f4-40d2-b4e4-9b800bbead5c.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c02_g1.png` · Higgsfield media `55e74114-74c8-446a-9885-25f174c60dec`
- video ref 1: uploaded image, not on the drive · Higgsfield media `0ba4e716-6200-4b81-8bff-0d939adb776e`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a wooden table and lift the white projector straight up out of it. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics and rhythm of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, gold THEXMASGLOW banner, the words CHRISTMAS LIGHT PROJECTOR, a white projector on a red circle. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray, no window.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a cream knit sleeve on the left wrist, a thin gold bracelet on the right wrist.

[5] LOCATION - a dark round wooden table fills the frame. A lit cream pillar candle sits at the top left, holly sprigs with red berries beside it, warm fairy lights out of focus behind. The candle, the holly and the fairy lights must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE
0.0-1.0s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it; the tuck tongue releases out of the front panel.
1.0-2.0s - the lid flaps fold upward and backward away from camera on the rear fold, staying attached to THE BOX, opening the top; the dark interior comes into view.
2.0-3.0s - both HANDS reach down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is now clearly visible.
3.0-4.0s - THE HANDS lift THE PROJECTOR straight up and out of THE BOX in one smooth vertical move until it clears the rim and is held above the open carton, white dome and BLACK top face facing camera.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift.

[12] AUDIO - natural room sound only: cardboard flaps, fingers on the carton. No music, no speech, no score.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands. The top face of THE PROJECTOR is BLACK.
BANNED: an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle or the holly disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text, music.
````

#### Video prompt — `clips/v1_c02_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `6614d81e-03b1-4044-b575-dfc192345e05`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175510_6614d81e-03b1-4044-b575-dfc192345e05.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c02_g1.png` · Higgsfield media `55e74114-74c8-446a-9885-25f174c60dec`
- video ref 1: uploaded image, not on the drive · Higgsfield media `0ba4e716-6200-4b81-8bff-0d939adb776e`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

SPEED RULE - SECOND MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift of the product out of the box is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a wooden table and lift the white projector briskly straight up out of it. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, gold THEXMASGLOW banner, the words CHRISTMAS LIGHT PROJECTOR, a white projector on a red circle. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray, no window.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a cream knit sleeve on the left wrist, a thin gold bracelet on the right wrist.

[5] LOCATION - a dark round wooden table fills the frame. A lit cream pillar candle sits at the top left, holly sprigs with red berries beside it, warm fairy lights out of focus behind. The candle, the holly and the fairy lights must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.1s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second.
3.1-4.0s - THE PROJECTOR is held steady above the open carton, white dome and BLACK top face square to camera, with a small natural settle of the hands.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast.
BANNED: any music, any song, any score, any soundtrack; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle or the holly disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
````

### C03 — The projector lifted

**In the cut:** `starting_frames/v1_c03_g3.png` → `clips/v1_c03_g2.mp4`

#### Image prompt — `starting_frames/v1_c03_g3.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `fb902941-abc4-441f-97aa-509a143e3983`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_164418_fb902941-abc4-441f-97aa-509a143e3983.png
**References, in submission order**
- @Image 1: `references/ref04.png` · Higgsfield media `77045fb2-b216-459e-8d4c-fd77c9e05d9a`

````text
COPY @Image 1 EXACTLY. The ONLY thing that changes is the kitchen behind her. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, the jewellery, the sleeve, and the white marble countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the bright white marble countertop occupies the LOWER RIGHT of the frame as a clean pale wedge running diagonally, passing behind and below her right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE — her two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but her fingers, with a visible gap of air between the base of the stand and the marble below. Left forearm enters from the lower left in a cream ribbed knit sleeve pushed back; right forearm enters from the right with a thin gold bangle at the wrist and two slim gold rings on the fingers. Fair skin, neat natural nails.

SCALE AND PLACEMENT — the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT — a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER — honed white marble with soft cool-grey veining and a squared edge, matte sheen.

THE KITCHEN — this is the only change. A warm modern kitchen, softly defocused: pale greige flat-front shaker cabinets with slim brushed-brass bar pulls, a stainless steel wall oven built into the tall cabinet run on the left, a white marble slab backsplash, a warm white LED strip glowing under the upper cabinets, and a pine garland with small warm fairy lights running high along the top of the cabinetry. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfectly exposed, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v1_c03_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `eb75d3ea-443e-44b5-9d25-24d50d10490a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175510_eb75d3ea-443e-44b5-9d25-24d50d10490a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v1_c03_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `156bd1b1-2bea-4381-9d8a-0f3ca01389cf`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the marble the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a marble kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the marble counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the marble until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the marble. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the marble in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the marble; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm under-cabinet light plus soft daylight, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The marble is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the marble, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
````

**Other takes of C03 on disk (3)**

#### Image prompt — `starting_frames/v1_c03_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `2603e3e9-bc93-4c54-b884-78a45cd30f7b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142342_2603e3e9-bc93-4c54-b884-78a45cd30f7b.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `93ffe771-244c-4b26-9081-85ce98447314`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `e836baed-2bc4-410b-adcb-b17b23f228b8`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same height, same distance, same vertical 9:16 framing, same kitchen counter in the foreground, same kitchen background and its depth, same two hands holding the product up at the same height and same angle, same arms entering frame the same way. Replace the product in the hands with OUR projector: a smooth matte white dome-topped cylindrical body standing on a SEPARATE white four-legged splayed stand base, the light exits the TOP of the dome, it is NOT a camera — no front lens, no swivel head, no tripod. Its design matches the product printed on the carton in the SECOND attached reference. The hands hold it the same way the original product was held, same scale in frame. Change the background only a little: make the kitchen more Christmassy — a short fir garland with warm white fairy lights along the upper cabinets, two or three red and gold baubles, a small red-and-cream dish towel, everything soft and out of focus behind the product. Shot on iPhone, photorealistic, tack-sharp focus on the product, crisp detail, warm natural kitchen light, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Image prompt — `starting_frames/v1_c03_g2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `c299703a-9594-42a8-bea7-74fd78ea5544`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_150852_c299703a-9594-42a8-bea7-74fd78ea5544.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `778fddd9-64c5-4a9e-8d7c-a8da676b0e00`

````text
Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.

FRAMING - copy @Image 1 exactly: a woman's two hands hold a small Christmas star projector UP IN THE AIR, lifted clear off the countertop, held at chest height in front of her. There is visible empty space underneath the product - it is NOT resting on any surface, nothing touches it but her fingers. Same camera height, same hand positions, same distance from lens as @Image 1.

THE PRODUCT - a compact matte-white rounded dome-shaped projector body sitting on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel. This black disc on top is essential and must be clearly visible, exactly like the unit in @Image 1. Do not render an all-white top.

HER HANDS - fair skin, neat natural nails, two slim gold rings, a thin gold bangle on one wrist, cream ribbed knit sleeve pushed back.

BACKGROUND - a warm modern kitchen, softly out of focus: pale greige shaker cabinets, a stainless wall oven, white quartz counters, a pine garland with red berries and warm fairy lights along the upper cabinetry. Evening interior light, warm white, clean and even, shallow depth of field.
````

#### Video prompt — `clips/v1_c03_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `cccb6cf2-82cb-44af-9089-c292a87844e1`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_172938_cccb6cf2-82cb-44af-9089-c292a87844e1.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `156bd1b1-2bea-4381-9d8a-0f3ca01389cf`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two hands raise the white projector high above a marble kitchen counter, then lower it slowly and set it down. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands holding THE PROJECTOR, entering from the bottom of frame.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the marble counter.

[7] TIMELINE
0.0-1.0s - camera locked. THE HANDS raise THE PROJECTOR straight upward, away from the marble, until the bottom of the stand is roughly 35 cm above the counter. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the marble. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
1.0-3.0s - THE HANDS lower THE PROJECTOR in one long, slow, continuous straight vertical descent toward the marble. The travel is deliberate and unbroken. No hesitation, no wobble, no sideways drift, no rotation.
3.0-3.5s - the four feet of the stand touch the marble and settle. Tiny compression, no bounce, no slide.
3.5-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm under-cabinet light plus soft daylight, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with weight; it stays perfectly upright and level through the whole descent. The marble is hard: contact is a small firm settle.

[12] AUDIO - natural room sound only: a soft contact tap when the stand meets the marble. No music, no speech, no score.

[13] POSITIVE LOCKS - the countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent is long and slow, not a short drop.
BANNED: the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping or rotating, the camera moving, a cut, subtitles, on-screen text, music.
````

### C04 — The cable going in

**In the cut:** `starting_frames/v1_c04_g3.png` → `clips/v1_c04_g1.mp4`

#### Image prompt — `starting_frames/v1_c04_g3.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `54c37f6c-0e31-44bb-9cf0-4c18e7a69f83`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_164418_54c37f6c-0e31-44bb-9cf0-4c18e7a69f83.png
**References, in submission order**
- @Image 1: `references/ref05.png` · Higgsfield media `64b95049-8d7f-4357-9871-3bac534a4929`

````text
COPY @Image 1 EXACTLY. The ONLY thing that changes is the kitchen behind her. Everything else is a literal copy.

CAMERA — this is the part that went wrong last time, so follow it precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently — a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The marble surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT — standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS — exactly as in @Image 1. Her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; on that wrist a stack of thin gold bangles, beige ribbed knit sleeve pushed back. Her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. Two slim gold rings on that hand. The white cable trails away to the right across the marble and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER — honed white marble with soft cool-grey veining and a squared edge, matte sheen.

THE KITCHEN — this is the only change. A warm modern kitchen, softly defocused across the top third of the frame: pale greige flat-front shaker cabinets with slim brushed-brass bar pulls, a stainless steel wall oven built into the tall cabinet run on the right, a white marble slab backsplash, a warm white LED strip glowing under the upper cabinets, and a pine garland with small warm fairy lights running high along the top of the cabinetry. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfectly exposed, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v1_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `5cd2cf13-d782-4089-9a3f-3c778b57486e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_172938_5cd2cf13-d782-4089-9a3f-3c778b57486e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v1_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `f5a6b062-7558-4477-b080-aee224cf0663`

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
THE LEFT HAND - a hand wearing a stack of gold bangles, resting on the left side of the dome. It does not move.
THE RIGHT HAND - a hand wearing gold rings, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the white marble around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the marble. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the marble immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
````

**Other takes of C04 on disk (3)**

#### Image prompt — `starting_frames/v1_c04_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `da3b103f-361c-415c-8ca0-a19a5403d0d7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142458_da3b103f-361c-415c-8ca0-a19a5403d0d7.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `2603e3e9-bc93-4c54-b884-78a45cd30f7b`
- @Image 2: uploaded image, not on the drive · Higgsfield media `e9b7679d-5c0a-42b9-9166-e9c3c08de12f`

````text
The FIRST attached image is the scene. The SECOND attached image gives the camera framing. Re-shoot the EXACT SAME kitchen from the first image — identical counter, identical cabinets, identical Christmas decoration, identical fir garland and warm fairy lights, identical baubles, identical wall colour, identical time of day and identical warm window light — but from the camera position of the second reference: the opposite side of the counter, looking back across it, same camera height, same distance, same vertical 9:16 framing and same composition as the second reference. The same projector from the first image is present, held in the same two hands: a smooth matte white dome-topped cylindrical body standing on a SEPARATE white four-legged splayed stand base, light exits the TOP of the dome, it is NOT a camera — no front lens, no swivel head, no tripod. It must be the identical projector, same size, same proportions, same finish as in the first image. The room, the props and the lighting must read as the same continuous scene, just seen from the other side. Shot on iPhone, photorealistic, tack-sharp focus on the product, crisp detail, warm natural kitchen light, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Image prompt — `starting_frames/v1_c04_g2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `85380c7a-5da3-47c9-b62f-e500c5c3ccd0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_150852_85380c7a-5da3-47c9-b62f-e500c5c3ccd0.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `14889836-9934-409f-b183-673412b8370b`
- @Image 2: uploaded image, not on the drive · Higgsfield media `778fddd9-64c5-4a9e-8d7c-a8da676b0e00`

````text
Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.

CAMERA GEOMETRY - this is the critical instruction. Copy the camera of @Image 1 exactly: a HIGH DOWNWARD ANGLE, the phone held at standing chest height and tilted down roughly 45 degrees over a white marble kitchen island. The pale marble countertop sweeps across and fills the lower two thirds of the frame and recedes into depth. The projector stands ON the countertop in the middle of the frame, seen from above and slightly in front, small in frame with a lot of counter around it. The woman is on the near side of the island, so only her forearms and hands enter frame from the right and lower right. DO NOT use a straight-on eye-level angle. DO NOT frame the product large and centred at lens height.

THE PRODUCT - a compact matte-white rounded dome-shaped projector on a small white four-legged splayed stand, standing upright on the counter. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this high angle, exactly like the unit in @Image 2. Do not render an all-white top.

THE CABLE - in her right hand she pinches the connector end of a slim white USB-C power cable between thumb and forefinger, held a few centimetres from the small port on the back of the projector's base, tip aimed squarely at that port, arm mid-reach as if about to plug it in. The rest of the white cable trails loosely across the marble behind her hand. The cable and the port must both be clearly visible and unobstructed. Her other hand rests lightly on the counter beside the projector steadying it.

HER HANDS - fair skin, neat natural nails, two slim gold rings, a thin gold bangle, cream ribbed knit sleeve.

BACKGROUND - beyond the island, a warm modern kitchen softly out of focus with a pine garland and warm fairy lights. Evening interior light, warm white, clean and even, shallow depth of field.
````

#### Video prompt — `clips/v1_c04_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `eaf23f27-c6c1-4b9c-93fc-bfd3635cbf25`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175510_eaf23f27-c6c1-4b9c-93fc-bfd3635cbf25.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `f5a6b062-7558-4477-b080-aee224cf0663`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a hand wearing a stack of gold bangles, resting on the left side of the dome. It does not move.
THE RIGHT HAND - a hand wearing gold rings, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a white marble countertop with grey veining fills the lower half of frame and stays there for the whole clip; behind it a warm modern kitchen with tall matte beige-taupe cabinets, a stainless wall oven set into the cabinet run on the left, warm under-cabinet light, and a green garland with small warm fairy lights along the top of the cabinets. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the white marble around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the marble. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the marble immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a small plastic click as the connector seats, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: any music, any song, any score, any soundtrack; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text.
````

### C05 — The door opens on the room

**In the cut:** `starting_frames/v1_c05_g2.png`, `references/v1_c05_r2.png` → `clips/v1_c05_g5.mp4`

#### Image prompt — `starting_frames/v1_c05_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `c0e36341-9fe3-45e9-a792-2131ba5b073f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_150851_c0e36341-9fe3-45e9-a792-2131ba5b073f.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c05_g1.png` · Higgsfield media `bd0c928c-db3f-42e0-8bf5-19e5961d43bc`

````text
Recreate @Image 1 with ONE change.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same white panelled door, the same antique brass round doorknob, the same small pine wreath with the red velvet bow on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position, the same warm low-key evening light.

THE CHANGE: the door is now FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
````

#### Image prompt — `references/v1_c05_r2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `602a896a-3f45-4638-8604-0569f9547aa7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_150851_602a896a-3f45-4638-8604-0569f9547aa7.png
**References, in submission order**
- @Image 1: `content/video_1_assets/references/v1_c05_r1.png` · Higgsfield media `ff693c44-6d58-4832-93ed-40e3c3c5978c`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same tall living room, the same Christmas light projection covering every wall and the ceiling - glowing Christmas trees, snowflakes, stars, baubles and candy canes in gold, green, red and blue - the same decorated tree, the same stockings on the mantel, the same white shelving, the same cream sofa with red tartan cushions, the same wrapped gifts, the same tall window on the left, the same camera position and height, the same magical low-key evening light.

CHANGE 1 - the projector unit must NOT be visible. Remove the small white glowing device and its little side table from the lower left completely. Replace that corner with plain floor and the edge of the rug. No projector anywhere in frame.

CHANGE 2 - the boy now stands TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder. The girl beside him stays exactly as she is, seen from behind, still looking up at the projected wall.

Both children are fully dressed in warm red-and-white knitted Christmas jumpers and matching knitted lounge trousers with thick socks. Wholesome family Christmas scene.

Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
````

#### Video prompt — `clips/v1_c05_g5.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `3f2e9f9d-9c5d-4fd3-9166-585477e50ac5`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_192147_3f2e9f9d-9c5d-4fd3-9166-585477e50ac5.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v1_c05_g5.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `5bec6a19-f599-41d8-aea3-86f851b70785`
- image ref 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `b4a0acbd-adc9-4274-b56c-cbb15c1b1eed`
- video ref 1: `references/scene_no_audio-5.mp4` — silenced upload padded to 4.50 s · Higgsfield media `5a88bec0-4962-479c-b159-287e3bd5e502`

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
- The moving light also pours down over the tree, the sofa, the floor and across both children's faces and pyjamas as it passes over them, so the brightness on everything in the room is changing continuously.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, doors, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

IMAGE QUALITY RULE - SECOND MOST IMPORTANT. The finished clip must look at least as sharp and as clean as the start image. Do not soften it, do not smear it, do not repaint it, do not re-imagine it. Hold the exact sharpness, exposure, contrast and fine detail of the start image: the wood grain of the floor, the panel edges and painted sheen of the white door, the brass of the round knob, the skin texture and fine hairs of the bare forearm, the individual leaves of the green wreath and its red bow. Crisp modern phone footage, in focus from the first frame to the last. BANNED: blur, soft focus, haze, motion smear on objects that are not moving, mushy low-detail surfaces, plastic or waxy skin, a repainted or re-imagined door or hallway, colour shift, washed-out or muddy exposure, upscaling artefacts, a dreamy or filtered look.

AUDIO RULE - THIRD MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

CHILDREN MOTION RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light is sweeping and pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the moving projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children and their red-and-white Fair Isle pyjamas, and the COLOUR and STYLE of the Christmas shapes.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.
Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: tall decorated Christmas tree centre, cream sofa with a knit throw right, tall windows left, patterned rug, presents under the tree. Sweeping, pouring light covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured light appears along the opening edge. Through that slice, glowing shapes are clearly seen racing downward and sideways past the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light is sweeping across the far wall and the tree and raining down over the floor ahead and over the camera's own path.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the field of light keeps sliding and pouring down every wall and across both children, shapes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The light is sweeping and pouring across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the moving projection as the only bright light source. Because the shapes are sweeping and pouring, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Pyjamas and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
````

**Other takes of C05 on disk (8)**

#### Image prompt — `starting_frames/v1_c05_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `7a255476-516b-4c2d-b3e3-e98e05a8096c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142340_7a255476-516b-4c2d-b3e3-e98e05a8096c.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `fafedddf-1b02-4f7a-a5ff-b49fb63399d5`

````text
Copy the attached reference photo EXACTLY: same camera position, same height, same distance, same vertical 9:16 framing, same closed interior door filling the frame the same way, same hand reaching in from the same side at the same height and same grip on the handle, same hallway lighting and same wall visible at the edges. Change only the door itself a little: it is now a warm white panelled interior door with a brushed brass lever handle, a small fir wreath with a red ribbon hung low on it, and a thin line of colourful light glowing out from the gap underneath and around the edges, hinting at something happening in the room behind. Same hand, same pose, same composition otherwise. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, natural realistic hallway lighting, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Image prompt — `references/v1_c05_r1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `9a799ad8-0d8c-49de-9f8b-82b9d920dc38`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142458_9a799ad8-0d8c-49de-9f8b-82b9d920dc38.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `f3042793-315d-4b74-9ec5-988d9973ce92`

````text
Copy the attached reference photo's FRAMING exactly: same camera position, same height, same distance, same vertical 9:16 composition, two young siblings placed in exactly the same spots and same seated poses as the two figures in the reference, facing the same direction, seen mostly from behind. Everything else changes. This is a DIFFERENT living room from the reference — a cosy, heavily Christmas-decorated family living room with a decorated fir tree, stockings on the mantel, a sofa with knitted throws, wrapped gifts on the floor. The two siblings are different children, around five and seven years old, both fully dressed in warm red-and-white knitted Christmas jumpers and matching lounge trousers, thick socks. A smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base sits low in the room, throwing light UP from the top of its dome. An animated Christmas light projection covers every surface — walls, ceiling, furniture: dense falling snowflakes, glowing green fir trees, golden stars, red and gold baubles, candy canes, in a warm gold and cool blue palette. The projection behaves like real projected light — flat, slightly translucent, wrapping and distorting as it crosses furniture and corners, brightest on flat walls, fading in shadowed recesses. No decals, no printed wallpaper, no stickers. The room is otherwise dark so the projection reads bright. Wholesome family Christmas scene. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, clean low-light exposure with no grain or smear, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Video prompt — `clips/v1_c05_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `185cbfbc-9af2-4d26-90ae-ab5d84382b45`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_172939_185cbfbc-9af2-4d26-90ae-ab5d84382b45.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `5bec6a19-f599-41d8-aea3-86f851b70785`
- image ref 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `b4a0acbd-adc9-4274-b56c-cbb15c1b1eed`
- video ref 1: uploaded image, not on the drive · Higgsfield media `e1efda68-06ef-4d1e-8d92-458f57abc6ef`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two laughing children inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. @Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children, their red-and-white Fair Isle pyjamas, and the style and colour of the projected Christmas patterns. Do not copy @Image 1's camera angle or framing. @Video 1 controls ONLY the camera path and the rhythm: hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway into the room, then tilts up. Do NOT copy the room, the furniture, the children, the blue colour, or anything projected from @Video 1.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing centre of the room facing camera, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Projected Christmas shapes - snowflakes, stars, small fir trees and candy canes in gold, green, red and blue - cover the walls AND the ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured moving light appears along the opening edge.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; coloured projected shapes sweep across the floor ahead.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY stands centre facing camera, mouth wide open laughing, arms out, bouncing on his toes. THE GIRL is behind him to the left, turning and laughing. Snowflakes, stars, small fir trees and candy canes drift and rotate continuously across the walls.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same Christmas shapes drift and swirl across the ceiling too. THE BOY jumps once with both arms straight up.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the projection as the only bright moving light source. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The children's pyjamas and hair move naturally with their motion.

[12] AUDIO - natural room sound only: the door handle, the door swinging, children laughing and squealing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across walls and ceiling. Exactly two children. The reveal shows CHRISTMAS imagery only.
BANNED: jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; a frozen still pattern; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text; music.
````

#### Video prompt — `clips/v1_c05_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `af3cd11d-b2a0-4034-9940-2613c3f33c01`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175511_af3cd11d-b2a0-4034-9940-2613c3f33c01.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `5bec6a19-f599-41d8-aea3-86f851b70785`
- image ref 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `b4a0acbd-adc9-4274-b56c-cbb15c1b1eed`
- video ref 1: uploaded image, not on the drive · Higgsfield media `e1efda68-06ef-4d1e-8d92-458f57abc6ef`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. They are never standing still, never posed, never frozen, never waiting. They are running, spinning, jumping and laughing continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Their faces are fully alive: eyes wide, mouths open laughing and shouting. This must look like real children filmed on a phone, not like a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two children running and laughing inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. Documentary realism, extremely natural. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. @Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children, their red-and-white Fair Isle pyjamas, and the style and colour of the projected Christmas patterns. Do not copy @Image 1's camera angle or framing, and do not copy its stillness - @Image 1 is a photograph, this clip must move. @Video 1 controls ONLY the camera path and the rhythm: hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway into the room, then tilts up. Do NOT copy the room, the furniture, the children, the blue colour, or anything projected from @Video 1. Do NOT copy any audio, music or soundtrack from @Video 1.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, in the centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Moving projected Christmas shapes - snowflakes, stars, small fir trees and candy canes in gold, green, red and blue - cover the walls AND the whole ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured MOVING light appears along the opening edge, shapes visibly sliding through that slice.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; coloured projected shapes sweep across the floor ahead and travel over the camera's own path.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps up onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Snowflakes, stars, fir trees and candy canes drift, rotate and sweep continuously across every wall.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same Christmas shapes drift and swirl across the entire ceiling, corner to corner, still moving. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the moving projection as the only bright light source, so the light on the walls, the furniture and the children is constantly shifting and sliding. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The sofa cushion compresses when THE BOY lands. The children's pyjamas and hair swing and lift with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the walls and the ceiling. Both children are in full motion from the moment they appear. The reveal shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; children standing still, posed or frozen; jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
````

#### Video prompt — `clips/v1_c05_g3.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `cdc7911b-2186-47a1-b867-3eed56b5e637`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_181407_cdc7911b-2186-47a1-b867-3eed56b5e637.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `5bec6a19-f599-41d8-aea3-86f851b70785`
- image ref 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `b4a0acbd-adc9-4274-b56c-cbb15c1b1eed`
- video ref 1: uploaded image, not on the drive · Higgsfield media `e1efda68-06ef-4d1e-8d92-458f57abc6ef`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the wall and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the main wall:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - the stars, the candy canes, the small fir trees, the baubles - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the furniture, the tree and the children's faces and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. They are never standing still, never posed, never frozen, never waiting. They are running, spinning, jumping and laughing continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Their faces are fully alive: eyes wide, mouths open laughing and shouting. This must look like real children filmed on a phone, not like a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room filled with moving projected light, two children running and laughing inside; the camera pushes in and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a warm room lit by moving coloured projection. Sharp, clean, correctly exposed. Natural handheld bounce as the camera walks. Documentary realism, extremely natural. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall. It is a photograph, so it shows the projection frozen - do NOT copy that stillness, the projection in this clip must travel.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children and their red-and-white Fair Isle pyjamas, and the COLOUR and STYLE of the Christmas shapes. It is also a photograph - copy its look, never its stillness.
@Video 1 IS THE MOTION AUTHORITY. Copy from it exactly two things: first, the camera path and rhythm - hand turns the handle, a slice of light appears at the door edge, the door swings wide, the camera walks forward through the doorway, then tilts up; and second, and most important, HOW THE PROJECTED LIGHT TRAVELS - the speed at which the projected shapes slide across the walls and ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the floor, the furniture and the people. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes, small fir trees and baubles in gold, green, red and blue. Do NOT copy its room, its furniture, its people, its flat blue colour, its captions or its audio.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, in the centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind THE BOY and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: a tall decorated Christmas tree centre, a cream sofa with a knit throw on the right, tall windows on the left, a patterned rug, presents under the tree. Travelling projected Christmas shapes cover the walls AND the whole ceiling.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured light appears along the opening edge, with shapes visibly sliding downward through that slice.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway; projected shapes sweep across the floor ahead and travel over the camera's own path.
2.0-3.0s - the camera is fully inside the room: the tall decorated tree centre, cream sofa right, tall windows left. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps up onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. The whole projected field keeps sliding down and to the right across every wall and across both children.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame - the same shapes slide across the entire ceiling in the same direction at the same speed. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[9] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: forward walk from 1.0s, and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[10] LIGHTING - the hallway is warm and dim; the room is warm and dim with the travelling projection as the only bright light source. Because the field is sliding, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with a single flat blue colour.

[11] PHYSICS - the door swings on its hinges, it is never lifted off or removed. The sofa cushion compresses when THE BOY lands. The children's pyjamas and hair swing and lift with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - every projected shape changes position on the surface in every single frame. Both children are in full motion from the moment they appear. The reveal shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; children standing still, posed or frozen; jellyfish, fish, octopus, coral, whales, bubbles or any underwater or aquarium imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
````

#### Video prompt — `clips/v1_c05_g4.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `d447d883-3461-4388-8fbc-9d99ee3cb608`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_184455_d447d883-3461-4388-8fbc-9d99ee3cb608.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `5bec6a19-f599-41d8-aea3-86f851b70785`
- image ref 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `b4a0acbd-adc9-4274-b56c-cbb15c1b1eed`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
The walls and the entire ceiling of this room are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes, tiny fir trees and baubles in gold, green, red and blue - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the tree, the sofa, the floor and across the children's faces and pyjamas as it passes over them, so the light on everything in the room is constantly shifting.

CHILDREN MOTION RULE - THE THIRD MOST IMPORTANT RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm and lighting exactly.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light-snow is pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the falling projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed white panelled door, the brass round knob, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow on the right-hand wall.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree, the cream sofa, the tall windows, the two children and their red-and-white Fair Isle pyjamas, and the COLOUR and STYLE of the Christmas shapes. Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching red-and-white Fair Isle pyjamas, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a warm double-height living room: tall decorated Christmas tree centre, cream sofa with a knit throw right, tall windows left, patterned rug, presents under the tree. Falling light-snow covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, no light at its edge, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door cracks open and a narrow vertical slice of coloured light appears along the opening edge. Through that slice, glowing shapes are clearly seen POURING DOWNWARD past the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light-snow is raining down across the far wall and the tree, and falls over the floor ahead and over the camera's own path.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the light-snow keeps pouring steadily down every wall and across both children, flakes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The snow is falling across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the falling projection as the only bright light source. Because the shapes are pouring down, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Pyjamas and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the walls and on the ceiling; a viewer can follow individual flakes travelling downward. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; snow that falls for a moment then stops; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
````

#### Video prompt — `clips/v1_c05_g6.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `20993c33-f801-4a31-9160-fdafc2a1a3ea`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_193629_20993c33-f801-4a31-9160-fdafc2a1a3ea.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `5bec6a19-f599-41d8-aea3-86f851b70785`
- image ref 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `b4a0acbd-adc9-4274-b56c-cbb15c1b1eed`

````text
RULE 1 - THE LIGHT ON THE WALLS AND CEILING MOVES. THIS IS THE WHOLE POINT OF THE CLIP.
Light this room the way a SPINNING MIRROR BALL lights a room. The projector head is TURNING - one slow revolution every three seconds - so every glowing Christmas shape it throws SWEEPS BODILY across the walls and across the ceiling, travelling sideways, bending over corners and running up onto the ceiling. Nothing is painted on. Nothing holds still.
On top of that sweep, the shapes also DRIFT DOWNWARD like heavy snow past a window at night, each one slowly turning as it goes.
SPEED: one shape crosses the whole wall in ONE SECOND. Movement is obvious within the first quarter-second of the clip.
THE TEST: two frames a third of a second apart share NO shape in the same place. Not one.
The start image is a single PAUSED frame of this moving light. At 0.0s it un-pauses and the light never stops again.
"Match the start image" means the room, the door, the people and the colours - NOT where the light sits. The light must leave its starting position instantly.
The moving light also washes across the tree, the sofa, the floor and both children's faces and pyjamas, so the brightness on everything keeps changing.

RULE 2 - SHARPNESS. The clip must be at least as sharp and clean as the start image: the wood grain of the floor, the panel edges of the white door, the brass knob, the skin and fine hairs of the bare forearm, the leaves of the green wreath. Crisp phone footage, in focus throughout. No blur, no haze, no soft focus, no waxy skin, no repainted door, no colour shift, no washed-out exposure.

RULE 3 - NO MUSIC OF ANY KIND. No song, score, soundtrack, melody, instruments, singing or festive music bed. Only real room sound: the door handle and door swinging, children laughing and squealing, quiet room tone.

TASK: image-to-video, 4 seconds, one continuous handheld phone POV take, vertical 9:16, normal wide-angle lens at eye height. The start image is frame 0.0s.

THE SHOT: first-person POV. A bare right forearm turns the brass knob and pushes the white panelled door open; the camera walks through into a warm double-height Christmas living room and tilts up to the ceiling.

WHAT IS IN THE ROOM (from @Image 1): tall decorated Christmas tree centre, cream sofa with a knit throw on the right, tall windows left, patterned rug, presents. Exactly TWO children - THE BOY and THE GIRL, both in matching red-and-white Fair Isle pyjamas. No adults, no third child, no pets.

TIMELINE - the light is sweeping and pouring in every beat:
0.0-1.0s the hand turns the knob and pushes; the door cracks open and a vertical slice of coloured light appears at the edge. Through the gap, glowing shapes are clearly seen racing sideways and downward.
1.0-2.0s the door swings wide, the camera steps forward through the doorway. Light sweeps across the far wall and the tree and rakes over the floor ahead.
2.0-3.0s the camera is inside. THE BOY is already running, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying. The field of light keeps sliding across every wall and over both of them.
3.0-4.0s the camera keeps walking forward and TILTS UP; the ceiling fills the top of frame with the same light sweeping across it. THE BOY jumps again, arms straight up; THE GIRL is still turning below.

The children are in full motion from the first frame they appear - never posed, never frozen, a different whole-body pose every half second.

BANNED: a projected pattern that stays in place; a static or frozen pattern; shapes that only twinkle, pulse, brighten or fade without travelling; light that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves briefly then stops; any music; blur or soft focus; children standing still; jellyfish, fish, coral, bubbles or underwater imagery; a room lit flat blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
````

#### Video prompt — `clips/v1_c05_g7.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `68b514e3-819e-4d21-95c1-d64bc900f165`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_195537_68b514e3-819e-4d21-95c1-d64bc900f165.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `5bec6a19-f599-41d8-aea3-86f851b70785`
- image ref 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `b4a0acbd-adc9-4274-b56c-cbb15c1b1eed`

````text
SUMMARY: a first-person hand pushes a white door open and walks into a Christmas living room where a projected snowflake field shimmers over every wall and the whole ceiling. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the door, the hand, the hallway and the colour. @Image 2 controls only the layout of the room behind the door. Both images show ONE room. The video contains only one room and only one Christmas tree.

SUBJECTS:
THE HAND - a bare right forearm entering from the lower right, palm on a round brass knob.
THE FIELD - the projected light: hundreds of small glowing snowflakes and dots in red, green, blue, gold and white, thrown by a single projector standing in the room, covering the walls and the whole ceiling as ONE continuous field.
THE CHILDREN - exactly two, in matching red-and-white Fair Isle pyjamas, standing on the rug in front of the tree.

HOW THE FIELD BEHAVES - this is the point of the clip:
The field as a whole is ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is.
The motion lives INSIDE it. Every single snowflake is alive for all four seconds:
- each flake DRIFTS slowly downward and slightly sideways, about one flake-width every half second, the way real snow falls past a window at night;
- a flake that reaches the bottom of a wall fades out there, and a new flake fades in high near the ceiling, so the overall density never alters;
- each flake turns slowly on its own centre as it drifts;
- each flake breathes, brightening and dimming on its own timing, never all together;
- each flake's colour cycles slowly through red, green, blue and gold.
The wall and the ceiling are lit by the SAME projector, so they are one field and behave identically at the same moment. If the flakes on the wall are drifting, the flakes on the ceiling are drifting exactly as much. The ceiling is never a still pattern above a moving wall.
Nothing is painted, printed or stencilled on the plaster. The start image is one paused frame of this; at 0.0s it un-pauses. Matching the start image applies to the door, the hallway, the room and the colours, not to where any individual flake sits.

TIMELINE:
0.0-1.0s THE HAND pushes the door open and it swings away from camera; the gap widens and the lit room appears through it. The camera holds still.
1.0-3.0s the camera pushes forward through the doorway into the room in one smooth walking move, and the room fills the frame. THE CHILDREN stand on the rug facing camera, one waving, both shifting their weight, the smaller one bouncing on her toes. The snowflakes drift down the walls and across the ceiling the whole time.
3.0-4.0s the camera tilts up from the top of the tree to the ceiling until the ceiling fills the upper half of the frame, the same drifting field covering it.

THE DOOR: the door is plain painted white panelled wood and its edge stays plain painted white wood. There is no glowing strip, no rainbow fringe, no coloured sparkle bar and no light-up trim on the door edge, on the door frame, or in the gap between them. The only thing seen through the gap is the room beyond. Light spilling out lands as a soft warm wash on the hallway floor.

AUDIO: room tone, a handle click, the door sweeping over the floor, two children laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion throughout, no slow motion, no speed ramp. Exactly two children, no third child, no adult, no pet. One tree. One continuous take. The field's outer boundary holds still while every flake inside it drifts, turns, breathes and shifts colour. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; the whole pattern rotating, spinning or sliding as one sheet; flakes that only twinkle in place without travelling; a still ceiling above a moving wall; a rainbow or glowing strip on the door edge or door frame; any music; blur; the projector unit in shot; jellyfish, fish, coral or bubbles; a cut; on-screen text.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v1_c06_g2.png` → `clips/v1_c06_g8.mp4`

#### Image prompt — `starting_frames/v1_c06_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `7bf26c13-2c47-41e8-bd9a-8c09b7cb46ad`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_150852_7bf26c13-2c47-41e8-bd9a-8c09b7cb46ad.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c06_g1.png` · Higgsfield media `3eecb330-db4d-41ce-8bbe-92f79021ee6a`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same cosy bedroom, the same Christmas light projection covering the walls and ceiling - glowing Christmas trees, snowflakes, stars, red baubles and candy canes - the same wooden bed with the dark green duvet, the cream knitted throw, the plaid pillows, the small lit Christmas tree beside the bed, the same stocking on the wall, the same camera position and height, the same magical low-key evening light.

CHANGE 1 - the projector unit must NOT be visible. Remove the small white glowing device and the little stool it sits on from the lower left completely. Replace that corner with plain wall and floor. No projector anywhere in frame.

CHANGE 2 - the boy is now standing UP ON THE BED, barefoot on the mattress in the middle of the duvet, knees bent and arms raised out to his sides, caught mid-bounce with the duvet dimpling under his feet, head tipped back looking up at the projected ceiling, laughing. He is clearly on top of the bed, not sitting on its edge.

The boy is fully dressed in a warm red-and-white knitted Christmas jumper and matching knitted lounge trousers. Wholesome family Christmas scene.

Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
````

#### Video prompt — `clips/v1_c06_g8.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `e6445200-298a-4220-8455-3a0dd864175d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_222626_e6445200-298a-4220-8455-3a0dd864175d.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v1_c06_g8.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`

````text
SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while an animated snowfall plays across the wall behind him and the whole ceiling, thrown there by a projector standing on the floor. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, THE BOY and the colour.

SUBJECTS:
THE BOY - exactly one child in red-and-white Fair Isle pyjamas, standing on the bed.
THE PROJECTOR - a small Christmas projector switched on and running on the bedroom floor, out of shot. Its lens throws one wide cone of coloured light across the room. Everything glowing on the plaster is that cone landing.
THE SCREEN - the wall behind the bed and the whole ceiling together, catching that cone as one continuous surface. The light lands directly on bare plaster and wraps around the corner where wall meets ceiling. No rectangle, no visible screen edge, no television.

WHAT IS PLAYING ON THE SCREEN - this is the point of the clip:
A looping snowfall animation is PLAYING on THE SCREEN for all four seconds, exactly the way a film plays on a cinema screen: the screen itself is fixed to the plaster and holds perfectly still, while the picture playing on it is in constant motion. The animation is a night snowfall - hundreds of small glowing six-point snowflakes and round dots in red, green, blue, gold and white, all falling.
Track these three so the fall is unmistakable:
FLAKE A - a large white six-point flake that begins just above the headboard on the left of the wall. It falls steadily and drifts slightly right, passing the middle of the wall at 2.0s, and fades out low near the skirting board at 4.0s.
FLAKE B - a red flake on the ceiling directly above the headboard. It travels across the ceiling toward the far corner, ending about a third of the way across at 4.0s.
FLAKE C - a small gold dot on the right of the wall. It falls the full height of the wall in the first two seconds, fades out at the bottom, and a fresh gold dot fades in high near the ceiling and falls the same path again.
Every other flake behaves like these three: roughly a quarter of the wall's height every second, downward with a slight sideways drift, each one turning slowly on its own centre and breathing brighter and dimmer on its own timing, each cycling slowly through red, green, blue and gold. Density stays even because a flake fading out at the bottom is matched by one fading in at the top.
Because the wall and the ceiling are one screen fed by one projector lens, the snowfall on the ceiling plays at the same moment and at the same speed as the snowfall on the wall.
The start image is one paused frame of this animation. At 0.0s the projector un-pauses and the snowfall plays. Matching the start image applies to the bedroom, the bed, THE BOY and the colours, not to where any individual flake sits.

TIMELINE:
0.0-1.5s THE BOY bends his knees and pushes off the mattress; both feet leave the duvet, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
1.5-2.5s He lands on both feet and drives straight into a second, higher jump, knees tucking.
2.5-4.0s The camera tilts up in one slow smooth move until the ceiling fills the upper half of the frame. THE BOY stays low in frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take. The camera makes one move only, a tilt up. THE SCREEN stays bolted to the plaster while the snowfall plays across it. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; a frozen pattern; the whole pattern turning or sliding as one sheet; any music; the projector unit in shot; a second child; a cut; on-screen text.
````

**Other takes of C06 on disk (10)**

#### Image prompt — `starting_frames/v1_c06_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `54aa9693-6cf0-46ae-bb75-3daef60aef45`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142458_54aa9693-6cf0-46ae-bb75-3daef60aef45.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `1b02a435-1854-4f65-8530-61e1c647cef0`

````text
Copy the attached reference photo's FRAMING exactly: same camera position, same height, same distance, same vertical 9:16 composition, one young child placed in exactly the same spot and same seated pose as the figure in the reference, facing the same direction. Everything else changes. This is a DIFFERENT child — around six years old, fully dressed in a warm red-and-white knitted Christmas jumper and matching lounge trousers — sitting up on a made bed in a DIFFERENT room, cosy and Christmas-decorated with a small fir tree in the corner, a knitted blanket folded on the bed, a stocking on the wall. A smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base sits low in the room, throwing light UP from the top of its dome. An animated Christmas light projection covers every surface — walls, ceiling, bedding: dense falling snowflakes, glowing green fir trees, golden stars, red and gold baubles, candy canes, in a warm gold and cool blue palette. The projection behaves like real projected light — flat, slightly translucent, wrapping and distorting as it crosses the bedding and corners, brightest on flat walls, fading in shadowed recesses. No decals, no printed wallpaper, no stickers. The room is otherwise dark so the projection reads bright. Wholesome family Christmas scene. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, clean low-light exposure with no grain or smear, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Video prompt — `clips/v1_c06_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `bbd46a17-3faf-4297-b5c5-753f519eae9a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_172938_bbd46a17-3faf-4297-b5c5-753f519eae9a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and projected pattern exactly.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes move across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the projected Christmas shapes and the lighting. It is the only authority on the scene.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Projected snowflakes, stars, candy canes, baubles and green fir trees cover the wall behind the bed and continue onto the ceiling.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The ceiling is covered in the same drifting Christmas projection. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the projection is the only bright moving light source, unchanged in character across the clip.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - natural room sound only: mattress springs, a child laughing and squealing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across wall and ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, a frozen still pattern, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text, music.
````

#### Video prompt — `clips/v1_c06_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `314d7700-8fd5-4b92-b024-9e16c3fc9604`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175511_314d7700-8fd5-4b92-b024-9e16c3fc9604.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and projected pattern exactly.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes sweep across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the look of the projected Christmas shapes and the lighting. It is the only authority on the scene. It is a photograph - do not copy its stillness, this clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Moving projected snowflakes, stars, candy canes, baubles and green fir trees cover the wall behind the bed and continue across the whole ceiling.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off. Behind him the projected shapes visibly slide and rotate across the wall.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second, face fully redrawing between beats.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The ceiling is fully covered in the same drifting, swirling Christmas projection, corner to corner, still visibly moving. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the bed and the boy is constantly shifting and sliding across them.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the wall and the ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
````

#### Video prompt — `clips/v1_c06_g3.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `cb2a248d-fd0e-4067-932f-b96f6ba92683`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_182144_cb2a248d-fd0e-4067-932f-b96f6ba92683.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`
- video ref 1: uploaded image, not on the drive · Higgsfield media `183e956d-e23f-4690-a3f6-c6f1c7ecb447`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the wall and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the wall behind the bed:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - every snowflake, star, candy cane, bauble and fir tree, on the wall and on the ceiling alike - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the bed, the duvet and the boy's face and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

@Video 1 IS THE MOTION AUTHORITY FOR THE PROJECTED LIGHT AND FOR NOTHING ELSE. It was filmed in a real bedroom with a real rotating projector running. Copy from it exactly: the speed at which the projected shapes slide across the wall and the ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the bed and over the child. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes, baubles and fir trees, in the exact colours and styles shown in the start image. Do NOT copy its room, its bed, its person, its flat blue colour, its captions or its audio.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and the LOOK of the projected shapes exactly - but not their stillness.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while projected Christmas shapes sweep across the wall and ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the projected Christmas shapes and the lighting. @Video 1 controls only HOW THAT LIGHT MOVES. The start image is a photograph - do not copy its stillness, this clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Moving projected snowflakes, stars, candy canes, baubles and green fir trees sweep across the wall behind the bed and across the ceiling. The coverage is dense but uneven and constantly changing, because the field is sliding - that is correct and expected.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses under him at the push-off. Behind him the projected field is already sliding down and to the right.
1.0-2.0s - THE BOY lands on the mattress, it compresses, and he immediately pushes off into a second higher jump, arms swinging up above his head. His hair lifts on each jump. A clearly different whole-body pose every half second, face fully redrawing between beats.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top of frame. The same sliding Christmas projection is travelling across the ceiling at the same speed and in the same direction as on the wall. THE BOY keeps bouncing throughout this move, still laughing, still changing pose every half second.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[10] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the bed and the boy is constantly shifting and sliding across them.

[11] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected field slides continuously and visibly in every single frame, on the wall and on the ceiling. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
````

#### Video prompt — `clips/v1_c06_g4.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `c9657884-bf5e-42cc-bdc2-835b9df64f63`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_185051_c9657884-bf5e-42cc-bdc2-835b9df64f63.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
The wall behind the bed and the entire ceiling are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes, baubles and small green fir trees - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the bed, the duvet and across the boy's face and pyjamas as it passes over them, so the light on him is constantly shifting.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas and the LOOK of the Christmas shapes exactly - but not their stillness.

[1] SUMMARY
A boy in Christmas pyjamas jumps and laughs on his bed while light-snow pours down the wall behind him and across the ceiling; the camera pulls back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit only by the falling projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness. This clip must move.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, standing on the bed, arms raised. COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw at the foot, pillows, a wooden headboard on the right, and a small lit Christmas tree on the right. Falling light-snow covers the wall behind the bed AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image: THE BOY standing on the bed, arms raised, reaching up and to his left.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - camera locked wide from the foot of the bed. THE BOY bends his knees and pushes off the mattress into a jump, both feet leaving the duvet, arms up, mouth open laughing. The duvet compresses at the push-off. Behind him the light-snow is already pouring straight down the wall, flakes clearly travelling from the top of the wall towards the bed.
1.0-2.0s - THE BOY lands, the mattress compresses, and he immediately pushes off into a second higher jump, arms swinging above his head, hair lifting. A clearly different whole-body pose every half second. The snow keeps raining down behind him and washes down over his back and shoulders as it falls.
2.0-4.0s - one single continuous camera move: the camera zooms out slowly and tilts upward at the same time, so more of the bedroom enters the bottom of frame and the CEILING enters the top. Light-snow is pouring across the entire ceiling as well, streaming away towards the far wall at the same speed. THE BOY keeps bouncing throughout, still laughing, still changing pose every half second.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height from the foot of the bed. One camera movement: the combined slow zoom-out and upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[9] LIGHTING - warm dim bedroom, the falling projection is the only bright light source, so the light on the wall, the bed and the boy is constantly pouring and shifting across them.

[10] PHYSICS - the mattress compresses and springs back under each landing; the duvet creases where his feet land. THE BOY stays on the bed the whole time.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: mattress springs and duvet rustle, and a child laughing and squealing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the wall and on the ceiling; a viewer can follow individual flakes travelling downward. Exactly one child. THE BOY is jumping, not standing still.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; snow that falls for a moment then stops; a second child, an adult, THE BOY standing still, THE BOY stepping off the bed or walking, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
````

#### Video prompt — `clips/v1_c06_g5.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `7242157b-6c75-4ed2-ba80-a1880def70a8`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_192147_7242157b-6c75-4ed2-ba80-a1880def70a8.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`
- video ref 1: uploaded image, not on the drive · Higgsfield media `43ac59bf-6871-418d-a34a-1bb14aac8554`

````text
RULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on the wall behind the bed and on the entire ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running in this exact kind of bedroom. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the way the whole field of glowing shapes slides and swarms across the plaster without ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

WHAT THE LIGHT DOES, described so it cannot be mistaken for a texture:
- The whole field of glowing shapes SLIDES BODILY across the wall and across the ceiling, the way light from a spinning projector head sweeps a room. It never locks onto the plaster.
- On top of that sliding, individual shapes POUR DOWNWARD like heavy snowfall filmed through a window at night, and each one spins slowly as it goes and drags a faint soft trail.
- SPEED: a single shape crosses the full height of the wall in ABOUT ONE SECOND. That is fast. A viewer must see it moving within the first quarter second of the clip.
- THE TEST: take any two frames a third of a second apart and lay them on top of each other. NOT ONE glowing shape is in the same place. Not one. If any shape has stayed put, the clip is wrong.
- The moving light also pours down over the bed, the duvet, the small tree and across the boy's face and pyjamas as it passes over him, so the brightness on everything in the room is changing continuously.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, bed, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

AUDIO RULE - SECOND MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

IMAGE QUALITY RULE: the finished clip must look at least as sharp and as clean as the start image. Hold its exact sharpness, exposure, contrast and fine detail - the knit of the cream throw, the pile of the dark green velvet duvet, the grain of the wooden headboard, the boy's skin and hair. Crisp modern phone footage, in focus throughout. BANNED: blur, soft focus, haze, mushy low-detail surfaces, plastic or waxy skin, colour shift, washed-out exposure, a dreamy or filtered look.

TASK: image-to-video. The start image is frame 0.0s. Hold its bedroom, bed, boy, pyjamas, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
A boy in Christmas pyjamas jumps on his bed while light sweeps and pours down the wall behind him and across the whole ceiling; the camera eases back and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim bedroom lit only by the moving projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the bedroom, the bed, the boy, his pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.

[4] CHARACTERS
THE BOY - red-and-white Fair Isle pyjamas, jumping on the bed, knees bending and springing, arms up, mouth wide open laughing and shouting, a clearly different whole-body pose every half second. Never standing still, never posed, never frozen.
COUNT LOCK: exactly one child. No second child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw across the foot of the bed, pillows at the head, a wooden headboard on the right, a small lit Christmas tree on the right. Sweeping, pouring light covers the wall behind the bed AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - THE BOY is already mid-bounce, knees bending, arms coming up, mouth open laughing. The duvet rucks and lifts under his feet. Behind him the field of glowing shapes is already sliding across the wall and raining downward; shapes visibly travel from the top of the wall to the bottom within this beat.
1.0-2.0s - he pushes off harder and jumps higher, both feet leaving the mattress, arms straight up over his head, head tipping back. The light keeps sweeping and pouring down the wall and over him, so the bright patches crossing his pyjamas and face are constantly moving.
2.0-4.0s - one single continuous camera move: the camera eases BACKWARD in a slow zoom-out while TILTING UPWARD, until the CEILING fills the upper half of frame. The light is sweeping and pouring across the entire ceiling too, streaming away towards the far side of the room at the same speed. THE BOY stays in the lower part of frame and keeps bouncing and laughing the whole time.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. One combined movement only: the slow zoom-out plus upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls.

[9] LIGHTING - warm dim bedroom, the moving projection is the only bright light source, so the light on the wall, the ceiling, the bed and the boy is constantly pouring and shifting across them. Do not flood the room with one flat colour.

[10] PHYSICS - the mattress compresses and springs back under each landing; the duvet and the knit throw ruck, lift and fall with every bounce. Pyjamas and hair lift on each jump.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: a child laughing and squealing, the mattress and bedding compressing and creaking, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light is visibly sweeping and pouring in every single frame, on the wall and on the ceiling; a viewer can follow individual shapes travelling across and down. Exactly one child, visibly excited and moving in every frame. The projection shows CHRISTMAS imagery only. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; the boy standing still, posed or frozen; a second child; an adult; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a cut; subtitles; on-screen text.
````

#### Video prompt — `clips/v1_c06_g6.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `fab60aa7-bbc9-47c2-93a7-a4121213ddcd`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_193629_fab60aa7-bbc9-47c2-93a7-a4121213ddcd.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`

````text
RULE 1 - THE LIGHT ON THE WALL AND CEILING MOVES. THIS IS THE WHOLE POINT OF THE CLIP.
Light this bedroom the way a SPINNING MIRROR BALL lights a room. The projector head is TURNING - one slow revolution every three seconds - so every glowing Christmas shape it throws SWEEPS BODILY across the wall behind the bed and across the whole ceiling, travelling sideways, bending over the corner and running up onto the ceiling. Nothing is painted on. Nothing holds still.
On top of that sweep, the shapes also DRIFT DOWNWARD like heavy snow past a window at night, each one slowly turning as it goes.
SPEED: one shape crosses the whole wall in ONE SECOND. Movement is obvious within the first quarter-second of the clip.
THE TEST: two frames a third of a second apart share NO shape in the same place. Not one.
The start image is a single PAUSED frame of this moving light. At 0.0s it un-pauses and the light never stops again.
"Match the start image" means the room, the bed, the boy and the colours - NOT where the light sits. The light must leave its starting position instantly.
The moving light also washes over the duvet, the small tree and the boy's face and pyjamas, so bright patches keep travelling across him.

RULE 2 - NO MUSIC OF ANY KIND. No song, score, soundtrack, melody, instruments, singing or festive music bed. Only real room sound: a child laughing and squealing, the mattress and bedding compressing, quiet room tone.

RULE 3 - SHARPNESS. At least as sharp and clean as the start image: the knit of the cream throw, the pile of the dark green velvet duvet, the grain of the wooden headboard, the boy's skin and hair. Crisp phone footage, in focus throughout. No blur, no haze, no soft focus, no waxy skin, no colour shift, no washed-out exposure.

TASK: image-to-video, 4 seconds, one continuous handheld phone take, vertical 9:16, normal wide-angle lens at chest height. The start image is frame 0.0s.

THE SHOT: a boy jumps on his bed while light sweeps down the wall behind him and across the ceiling; the camera eases back and tilts up.

WHAT IS IN THE ROOM - all of this exists in the start image and must survive to the last frame: a bed with a dark green velvet duvet, a cream knit throw across the foot, pillows at the head, a wooden headboard on the right, a small lit Christmas tree on the right. Exactly ONE child - THE BOY, in red-and-white Fair Isle pyjamas. No second child, no adults, no pets.

TIMELINE - the light is sweeping and pouring in every beat:
0.0-1.0s THE BOY is already mid-bounce, knees bending, arms coming up, mouth open laughing; the duvet rucks and lifts under his feet. Behind him the field of shapes is already sliding across the wall and raining downward.
1.0-2.0s he pushes off harder and jumps higher, both feet leaving the mattress, arms straight up, head tipping back. The light keeps sweeping over the wall and over him.
2.0-4.0s one single continuous camera move: the camera eases BACKWARD in a slow zoom-out while TILTING UP, until the ceiling fills the upper half of frame with the same light sweeping across it. THE BOY stays low in frame, still bouncing and laughing.

He is in full motion in every frame - never posed, never frozen, a different whole-body pose every half second. The mattress compresses and springs back on every landing; the duvet and throw ruck and fall; pyjamas and hair lift on each jump.

BANNED: a projected pattern that stays in place; a static or frozen pattern; shapes that only twinkle, pulse, brighten or fade without travelling; light that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves briefly then stops; any music; blur or soft focus; the boy standing still; a second child; an adult; jellyfish, fish, coral, bubbles or underwater imagery; a room lit flat blue; the projector unit visible; a cut; subtitles; on-screen text.
````

#### Video prompt — `clips/v1_c06_g7.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `2a6e0f3f-1c4a-4ec2-abf5-113c5e8065a8`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_195536_2a6e0f3f-1c4a-4ec2-abf5-113c5e8065a8.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`

````text
SUMMARY: a boy bounces on his bed in a Christmas bedroom while a projected snowflake field shimmers over the wall behind him and the whole ceiling. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, the boy and the colour.

SUBJECTS:
THE BOY - exactly one child, in red-and-white Fair Isle pyjamas, standing on the bed. No second child, no adult, no pet.
THE FIELD - the projected light: hundreds of small glowing snowflakes and dots in red, green, blue, gold and white, thrown by a single projector standing in the bedroom, covering the wall behind the bed and the whole ceiling as ONE continuous field.
THE BED - dark green velvet duvet, cream knit throw across the foot, pillows against the headboard.

HOW THE FIELD BEHAVES - this is the point of the clip:
The field as a whole is ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is, and no shape travels a long distance across the wall.
The motion lives INSIDE it. Every single snowflake is alive for all four seconds:
- each flake DRIFTS slowly downward and slightly sideways, about one flake-width every half second, the way real snow falls past a window at night;
- a flake that reaches the bottom of the wall fades out there, and a new flake fades in high near the ceiling, so the overall density never alters;
- each flake turns slowly on its own centre as it drifts;
- each flake breathes, brightening and dimming on its own timing, never all together;
- each flake's colour cycles slowly through red, green, blue and gold.
The wall and the ceiling are lit by the SAME projector, so they are one field and behave identically at the same moment. Whatever the flakes on the wall are doing, the flakes on the ceiling are doing at the same instant, at the same speed. The ceiling is never a still pattern above a moving wall, and the wall is never a still pattern below a moving ceiling.
Nothing is painted, printed or stencilled on the plaster. The start image is one paused frame of this; at 0.0s it un-pauses. Matching the start image applies to the bedroom, the bed, THE BOY and the colours, not to where any individual flake sits.

TIMELINE:
0.0-1.5s THE BOY bends his knees, then pushes off the mattress hard; both feet leave the duvet and his arms swing straight up over his head. The mattress compresses under him and springs back. He is laughing with his mouth open. The snowflakes drift down the wall and across the ceiling.
1.5-2.5s THE BOY lands on both feet, the duvet dents and recovers, and he immediately drives into a second jump, higher than the first, knees tucking up.
2.5-4.0s the camera tilts up in one slow smooth move until the ceiling fills the upper half of the frame, the same drifting field covering it. THE BOY stays low in the frame and keeps bouncing.

AUDIO: room tone, the mattress and springs compressing on each landing, bedding rustling, a boy laughing and squealing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - a real boy jumping at real speed, landing with real weight. No slow motion, no slow-motion feel, no floating, no speed ramp, no dreamy drift. Exactly one child. One continuous take. The camera makes one move only, a tilt up - it does not zoom, push in or pull out. The field's outer boundary holds still while every flake inside it drifts, turns, breathes and shifts colour. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; a floating or weightless jump; the whole pattern rotating, spinning, swinging or sliding as one sheet; a frozen or still pattern; flakes that only twinkle in place without travelling; a still ceiling above a moving wall; any music; blur; the projector unit in shot; jellyfish, fish, coral or bubbles; a second child; an adult; a cut; on-screen text.
````

#### Video prompt — `clips/v1_c06_g9.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `a3247d8e-6c7c-44b2-99af-902bb15a5ecf`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_223335_a3247d8e-6c7c-44b2-99af-902bb15a5ecf.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`

````text
SUMMARY: a projector plays a fast, busy Christmas light show across a bedroom wall and the whole ceiling while a boy bounces on his bed. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, THE BOY and the colour.

SUBJECTS:
THE PROJECTOR - a Christmas projector switched on and running on the bedroom floor, out of shot. Its lens throws one wide cone of coloured light across the room. Everything glowing on the plaster is that cone landing.
THE SCREEN - the wall behind the bed and the whole ceiling together, catching that cone as one continuous surface. The light lands directly on bare plaster and wraps around the corner where wall meets ceiling. No rectangle, no visible screen edge, no television.
THE LIGHT SHOW - the animation playing on THE SCREEN: glowing six-point snowflakes, round dots and stars in red, green, blue, gold and white.
THE BOY - exactly one child in red-and-white Fair Isle pyjamas, bouncing on the bed.

THE LIGHT SHOW IS THE POINT OF THIS CLIP:
THE SCREEN itself is fixed to the plaster and never moves. Everything playing on it is RACING. This is not a shimmer and it is not a twinkle in place - every element travels a long, obvious distance across the plaster within four seconds, far enough that you can follow it with your eye.
- The snowflakes POUR downward fast, each one falling the full height of the wall in about one and a half seconds, fading out at the skirting board while fresh ones pour in along the ceiling line, so the fall never stops.
- Every flake spins as it falls and swings from side to side across its own path.
- Every flake flicks to a different colour about twice a second - red, green, blue, gold, white - so the whole wall keeps shifting colour.
- The round dots blink on and off rapidly like fast fairy lights, hundreds of them out of step with one another.
Because one lens feeds both surfaces, every event below plays on the wall and on the ceiling at the same instant and at the same speed.

TIMELINE:
0.0-1.0s SCREEN: a bright gold shooting star streaks diagonally from the top left of the wall down to the bottom right, leaving a short trail behind it, while the snow pours down the whole wall. BOY: bends his knees and pushes off the mattress, both feet leaving the duvet, arms swinging up over his head, mouth open laughing. CAMERA: holds.
1.0-2.0s SCREEN: a second shooting star crosses the ceiling from one corner to the other; the larger flakes swell bigger and shrink back down as they fall. BOY: lands on both feet and drives straight into a second, higher jump.
2.0-3.0s SCREEN: a wave of green sweeps across the wall and over the ceiling, every element flushing green as the wave passes, then the colours scatter apart again. CAMERA: tilts up in one slow smooth move until the ceiling fills the upper half of the frame.
3.0-4.0s SCREEN: a third shooting star crosses the ceiling, the dots burst outward in rings, and the snow keeps pouring at full speed. BOY: stays low in the frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take. The camera makes one move only, a tilt up. THE SCREEN stays bolted to the plaster while everything playing on it races across it. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; a frozen or still pattern; elements that stay in one place; the whole pattern turning or sliding as one sheet; any music; the projector unit in shot; a second child; a cut; on-screen text.
````

#### Video prompt — `clips/v1_c06_g10.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `634f95a6-ad17-40d7-af69-11ec84133bc9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_224609_634f95a6-ad17-40d7-af69-11ec84133bc9.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c06_g2.png` · Higgsfield media `08badfd0-da8f-4796-853a-423bf096bd43`

````text
SUMMARY: a Christmas projector fills a bedroom wall and ceiling with falling snowflakes, stars and little Christmas trees of light while a boy bounces on his bed. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the bed, THE BOY and the colour.

SUBJECTS:
THE PROJECTOR - a Christmas projector switched on and running on the bedroom floor, out of shot, throwing one wide cone of coloured light. Every glowing shape in the room is that cone landing.
THE SHAPES - glowing six-point snowflakes, small stars, little Christmas trees and round dots in red, green, blue, gold and white, scattered across the wall behind the bed, the ceiling, the bed and THE BOY himself.
THE BOY - exactly one child in red-and-white Fair Isle pyjamas, bouncing on the bed.

HOW THE SHAPES TRAVEL - this is the point of the clip:
Every shape is falling. Each one starts high, up along the line where the wall meets the ceiling, and travels downward for the whole four seconds, fast enough to cross the wall from the ceiling to the skirting board in about a second and a half. Follow any single one and you watch it pass landmark after landmark:
- a big white snowflake starts above the headboard, passes the top of the headboard at 0.5s, slides down over the pillows at 1.2s, crosses THE BOY's chest and sleeve at 2.0s, carries on down over the green duvet, and reaches the skirting board at 3.5s where it fades out;
- a gold star starts at the far corner of the ceiling and travels the length of the ceiling toward the camera, arrives at the line where ceiling meets wall at 2.5s, and keeps going down the wall from there;
- a red Christmas tree shape falls beside the headboard on the right, spinning as it drops, and arrives on the duvet at 3.0s.
Every other shape is doing the same thing at the same moment from a different starting height, so the wall and the ceiling are one continuous downpour of light for all four seconds. As each shape leaves the bottom, a fresh one appears up along the ceiling line and falls the same way, so the room never empties.
As they fall the shapes also spin on their own centres, swing sideways across their own paths, and flick to a new colour about twice a second.
One lens lights the wall and the ceiling together, so the downpour on the ceiling runs at the same instant and at the same speed as the downpour on the wall.
The start image catches this downpour at one instant only. From 0.0s every shape carries on falling from wherever it happens to be.

TIMELINE:
0.0-1.5s THE BOY bends his knees and pushes off the mattress, both feet leaving the duvet, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back. CAMERA holds.
1.5-2.5s THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking up.
2.5-4.0s CAMERA tilts up in one smooth move until the ceiling fills the upper half of the frame. THE BOY stays low in the frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take. The camera makes one move only, a tilt up. Every glowing shape is travelling downward across the plaster for the whole four seconds, covering real distance. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; any music; the projector unit in shot; a second child; a cut; on-screen text.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v1_c07_g2.png` → `clips/v1_c07_g6.mp4`

#### Image prompt — `starting_frames/v1_c07_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `7a5cb60b-0a26-4555-921b-a51c18f7ba42`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_150852_7a5cb60b-0a26-4555-921b-a51c18f7ba42.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c07_g1.png` · Higgsfield media `cb37f87c-c8ee-4de4-838a-1731eddad191`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same enormous double-height living room, the same Christmas light projection blanketing the whole ceiling and every wall - glowing Christmas trees, snowflakes, stars and baubles in blue, gold, green and red - the same tall black-framed windows on the left, the same big decorated Christmas tree, the same staircase with lit garland on the right, the same long cream sectional sofa and ottoman, the same camera position and height, the same magical low-key evening light.

CHANGE 1 - the projector unit must NOT be visible. Remove the small white glowing device and the round side table from the lower left completely. Replace that corner with plain rug and floor. No projector anywhere in frame.

CHANGE 2 - add TWO children to the room: a boy and a girl. The girl is JUMPING ON THE SOFA - caught mid-air above the cream sectional cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off. The boy stands on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room.

Both children are fully dressed in warm red-and-white knitted Christmas jumpers and matching knitted lounge trousers with thick socks. Wholesome family Christmas scene.

Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
````

#### Video prompt — `clips/v1_c07_g6.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `152bf982-99ed-4a4c-a783-9fb3935f53eb`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_195536_152bf982-99ed-4a4c-a783-9fb3935f53eb.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v1_c07_g6.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `88a5ad92-3965-4b0e-8d9a-9d983c5e0a5a`

````text
SUMMARY: two children play in a double-height Christmas living room while a projected snowflake field shimmers over every wall and the whole ceiling. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the room, the furniture, the children and the colour.

SUBJECTS:
THE GIRL - on the rug on the left, back to camera, spinning with her arms out.
THE BOY - on the right, jumping on the cream sectional sofa.
Exactly two children. No third child, no adult, no pet.
THE FIELD - the projected light: hundreds of small glowing snowflakes and dots in red, green, blue, gold and white, thrown by a single projector standing in the room, covering every wall and the whole ceiling as ONE continuous field.
THE ROOM - a tall lit Christmas tree centre, tall black-framed windows left, a staircase right, a cream sectional sofa right, an ottoman front centre, a rug on the floor. All of it survives to the last frame.

HOW THE FIELD BEHAVES - this is the point of the clip:
The field as a whole is ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is.
The motion lives INSIDE it. Every single snowflake is alive for all four seconds:
- each flake DRIFTS slowly downward and slightly sideways, about one flake-width every half second, the way real snow falls past a window at night;
- a flake that reaches the floor line fades out there, and a new flake fades in high near the ceiling, so the overall density never alters;
- each flake turns slowly on its own centre as it drifts;
- each flake breathes, brightening and dimming on its own timing, never all together;
- each flake's colour cycles slowly through red, green, blue and gold.
Every wall and the ceiling are lit by the SAME projector, so they are one field and behave identically at the same moment. Whatever the flakes on the walls are doing, the flakes on the ceiling are doing at the same instant, at the same speed.
Nothing is painted, printed or stencilled on the plaster. The start image is one paused frame of this; at 0.0s it un-pauses. Matching the start image applies to the room, the furniture, the children and the colours, not to where any individual flake sits.

FRAMING FIX: the start image has a dark unlit angular wedge of ceiling and a hard diagonal seam in the TOP RIGHT. It is gone by 1.0s, pushed out of frame by the camera step described below, and from 1.0s on the top right is ordinary lit ceiling carrying the same drifting field. There is no dark triangle and no hard diagonal cut-off anywhere after 1.0s.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles, and the dark wedge and the diagonal seam slide out of the top right. THE BOY bounces on the sofa cushion with his arms over his head, laughing. THE GIRL spins on the rug with her face turned up.
1.0-2.0s the camera holds in the closer position. THE BOY pushes off harder and both feet leave the cushion, which compresses and springs back. THE GIRL keeps turning and tips her head back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the ceiling fills the upper half of the frame, the same drifting field covering it. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, a sofa cushion compressing on each landing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. No slow motion, no floating, no speed ramp. Exactly two children. One continuous take. The field's outer boundary holds still while every flake inside it drifts, turns, breathes and shifts colour. Walls and ceiling always move together. THE BOY stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: slow motion; the whole pattern rotating, spinning or sliding as one sheet; a frozen or still pattern; flakes that only twinkle in place without travelling; a still ceiling above moving walls; any music; blur; a dark unlit wedge or hard diagonal line in the top right after 1.0s; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; a cut; on-screen text.
````

**Other takes of C07 on disk (6)**

#### Image prompt — `starting_frames/v1_c07_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `3a88d6da-3303-4655-8601-58d8c276034e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_142340_3a88d6da-3303-4655-8601-58d8c276034e.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `bf0de75e-9468-459f-959f-aa46f70616c4`

````text
Copy the attached reference photo's FRAMING exactly: same camera position, same low-to-mid height looking up into a tall double-height living room, same distance, same vertical 9:16 composition, same amount of wall and ceiling in frame. Everything else changes. This is a DIFFERENT, more heavily Christmas-decorated double-height living room — a tall decorated fir tree, garland wound up a staircase bannister, stockings, wrapped gifts, a large sofa. No people in frame. A smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base sits low in the room, throwing light UP from the top of its dome. An animated Christmas light projection covers every surface — the tall walls, the high ceiling, the staircase, the furniture: dense falling snowflakes, glowing green fir trees, golden stars, red and gold baubles, candy canes, in a warm gold and cool blue palette. The projection behaves like real projected light — flat, slightly translucent, wrapping and distorting as it crosses furniture, corners and the stair rail, brightest on the big flat walls, fading in shadowed recesses and stretching as it climbs toward the ceiling. No decals, no printed wallpaper, no stickers. The room is otherwise dark so the projection reads bright. Shot on iPhone, photorealistic, tack-sharp focus, crisp detail, clean low-light exposure with no grain or smear, no motion blur, no text overlay, no captions, no watermark. Normal wide-angle lens, straight vertical lines, no fisheye distortion.
````

#### Video prompt — `clips/v1_c07_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `b2f0f418-d8fe-4d68-b566-27a5dd312a4e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_172938_b2f0f418-d8fe-4d68-b566-27a5dd312a4e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `88a5ad92-3965-4b0e-8d9a-9d983c5e0a5a`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and projected pattern exactly.

[1] SUMMARY
Two excited children play in a Christmas living room covered in moving projected light, one jumping on the sofa; the camera tilts up to reveal the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the projected Christmas shapes and the lighting. It is the only authority on the scene.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out.
THE BOY - on the right, mid-jump on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Projected snowflakes, stars and candy canes in blue, gold and red cover the walls and continue onto the ceiling.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - camera locked wide. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward.
1.0-2.0s - THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up at the ceiling.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame, revealing the same Christmas shapes drifting and swirling across the ceiling. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. One camera movement: the upward tilt from 2.0s. No cut, no zoom, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the projection is the only bright moving light source, unchanged in character across the clip.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - natural room sound only: children laughing and squealing, cushions compressing. No music, no score, no background song.

[13] POSITIVE LOCKS - the projected animation is NEVER static: every shape is in continuous motion in every frame, drifting, rotating and swirling across walls and ceiling. Exactly two children. Both children are visibly excited and moving in every frame.
BANNED: a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, a frozen still pattern, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text, music.
````

#### Video prompt — `clips/v1_c07_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `a3be98cc-8d55-4931-b12b-d4d3971d585d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175511_a3be98cc-8d55-4931-b12b-d4d3971d585d.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `88a5ad92-3965-4b0e-8d9a-9d983c5e0a5a`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTION MOTION RULE - THE SECOND MOST IMPORTANT RULE IN THIS CLIP: the projected Christmas shapes are a MOVING ANIMATION, never a printed pattern and never a still slide. Every single shape is travelling in every single frame, from frame one. Snowflakes drift steadily downward across the surfaces and rotate as they fall. Stars sweep sideways and twinkle on and off. Candy canes and small fir trees slide across the surface and turn slowly. Any given shape crosses a visible distance of at least a third of the wall during the 4 seconds. New shapes enter from one edge continuously while others leave the opposite edge. The whole field also swirls slowly as a single mass. If you compared any two frames half a second apart, every shape would be in a clearly different place. The pattern NEVER holds still, never locks to the wall, never behaves like wallpaper, never freezes for even a single frame.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the ceiling looks half covered and the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely, and what replaces the top right is more of the same fully projected ceiling. From 1.0s onward the CEILING IS COMPLETELY AND EVENLY COVERED with moving projected Christmas shapes across its whole width, corner to corner, edge to edge, with NO dark patch, NO unlit triangle, NO bare plane, NO hard diagonal cut-off line anywhere. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and projected pattern exactly, apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room covered in moving projected light, one jumping on the sofa; the camera steps forward and tilts up to reveal a fully covered ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the look of the projected Christmas shapes and the lighting. It is a photograph - do not copy its stillness or its top-right framing problem, this clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Moving projected snowflakes, stars and candy canes in blue, gold and red cover the walls and the entire ceiling.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more fully projected ceiling. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward.
1.0-2.0s - the camera is now settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Projected shapes sweep visibly across the walls, the tree and the children.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame, revealing Christmas shapes drifting and swirling across the WHOLE ceiling, evenly covered corner to corner with no dark gap. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly shifting and sliding across them.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: children laughing and squealing, and cushions compressing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected animation is in continuous visible motion in every frame on both the walls and the ceiling. The ceiling is fully and evenly covered from 1.0s onward. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a static or frozen projected pattern; a pattern that looks printed, painted or like wallpaper; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a half-covered ceiling; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
````

#### Video prompt — `clips/v1_c07_g3.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `aa28629c-385e-4644-8db1-268c6b15c35f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_182144_aa28629c-385e-4644-8db1-268c6b15c35f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `88a5ad92-3965-4b0e-8d9a-9d983c5e0a5a`
- video ref 1: uploaded image, not on the drive · Higgsfield media `45adf644-96a2-43df-be2d-3b0fce38e061`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

PROJECTED LIGHT MOTION - THE SECOND MOST IMPORTANT RULE. READ IT AS A TIMELINE, NOT AS A DESCRIPTION.
The projector is a ROTATING projector head. Its whole field of light turns continuously, so every projected shape SLIDES ACROSS the walls and the ceiling the way clouds cross a sky. These shapes are light travelling over the plaster. They are NOT a pattern printed on the plaster and they do NOT belong to the surface.
Direction and speed are fixed for the entire clip: the whole field drifts steadily DOWNWARD AND TO THE RIGHT at a constant rate of about one shape-width every half second. Nothing accelerates, nothing pauses, nothing reverses.
TRACK ONE SHAPE TO CHECK YOURSELF - THE BIG BLUE SNOWFLAKE on the ceiling:
0.0s - it sits in the UPPER LEFT of the lit surface.
1.0s - it has travelled a quarter of the way down and to the right, and rotated about 45 degrees.
2.0s - it is at the CENTRE of the surface, rotated about 90 degrees.
3.0s - it is three quarters of the way across, in the LOWER RIGHT area.
4.0s - it has slid off the lower right edge and left the surface completely.
Every other shape - every snowflake, star, candy cane and bauble, on the walls and on the ceiling alike - travels the same path at the same speed, so the whole field moves as one mass. As shapes leave at the lower right, new ones enter continuously at the upper left. The coloured light also slides across the tree, the sofa and the children's faces and pyjamas as it passes over them.
If you froze two frames half a second apart and laid one on the other, NO shape would be in the same place.

@Video 1 IS THE MOTION AUTHORITY FOR THE PROJECTED LIGHT AND FOR NOTHING ELSE. It was filmed in a real living room with a real rotating projector running. Copy from it exactly: the speed at which the projected shapes slide across the walls and the ceiling, the fact that they never stop moving for a single frame, and the way the coloured light slides over the furniture and over the people. Copy that movement exactly.
Do NOT copy anything else from @Video 1. Its imagery is an underwater aquarium scene - this clip projects CHRISTMAS shapes only: snowflakes, stars, candy canes and baubles in blue, gold and red, in the exact colours and styles shown in the start image. Do NOT copy its room, its furniture, its people, its flat blue colour, its captions or its audio.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely, and what replaces the top right is more of the same lit, moving ceiling. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and the LOOK of the projected shapes exactly - but not their stillness, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room washed in sliding projected light, one jumping on the sofa; the camera steps forward and tilts up to the ceiling. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit by moving coloured projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the projected Christmas shapes and the lighting. @Video 1 controls only HOW THAT LIGHT MOVES. The start image is a photograph - do not copy its stillness or its top-right framing problem, this clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Projected snowflakes, stars and candy canes in blue, gold and red sweep across the walls and the ceiling. The coverage is dense but uneven and constantly changing, because the field is sliding - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit, moving ceiling. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The projected field is already sliding down and to the right.
1.0-2.0s - the camera is now settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Projected shapes sweep visibly across the walls, the tree and the children.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. The same sliding Christmas projection is travelling across the ceiling at the same speed and in the same direction as on the walls, shapes entering at the upper left and leaving at the lower right. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[9] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[10] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly shifting and sliding across them.

[11] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: children laughing and squealing, and cushions compressing. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[13] POSITIVE LOCKS - the projected field slides continuously and visibly in every single frame, on the walls and on the ceiling. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place on the wall or ceiling; shapes that only brighten and fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
````

#### Video prompt — `clips/v1_c07_g4.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `18ef173c-d94e-4d5d-bb45-9ad5b3da1ea0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_184454_18ef173c-d94e-4d5d-bb45-9ad5b3da1ea0.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `88a5ad92-3965-4b0e-8d9a-9d983c5e0a5a`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FALLING SNOW OF LIGHT - THE SECOND MOST IMPORTANT RULE. THIS IS THE WHOLE POINT OF THE CLIP.
Every wall and the entire ceiling of this room are covered in SNOW MADE OF LIGHT, and that snow is FALLING. Film it exactly the way you would film heavy snowfall through a window at night. Hundreds of glowing Christmas shapes - snowflakes, stars, candy canes and baubles in blue, gold and red - POUR CONTINUOUSLY DOWNWARD across every lit surface, top to bottom, without stopping for a single frame.
SPEED: a single flake crosses the full height of the wall in about TWO SECONDS. That is fast, obvious, unmistakable motion - a viewer must see it moving instantly.
BEHAVIOUR: each flake spins slowly as it falls and drags a faint soft trail behind it. They do not fall as one rigid sheet - they drift and swirl sideways at slightly different speeds, so the whole field churns and shimmers. New shapes pour in continuously at the top of every surface and fall away off the bottom.
THE START IMAGE IS A PAUSED FRAME OF THIS SNOWFALL. At 0.0s the video RESUMES and the snow immediately starts falling again and never stops.
The falling coloured light also pours down over the tree, the sofa, the staircase and across the children's faces and pyjamas as it passes over them, so the light on everything is constantly shifting.

FRAMING FIX RULE - THE THIRD MOST IMPORTANT RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely and are replaced by more of the same lit ceiling with snow pouring across it. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas and the LOOK of the Christmas shapes exactly - but not their stillness, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room where light-snow pours down every wall and the ceiling, one jumping on the sofa; the camera steps forward and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit only by the falling projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness or its top-right framing problem. This clip must move and must reframe.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Falling light-snow covers the walls and the ceiling. Its coverage is dense but uneven and constantly changing, because it is falling - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the snow is falling in every single beat
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit ceiling with snow pouring across it. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The light-snow is already raining steadily down every wall.
1.0-2.0s - the camera is settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Glowing shapes pour visibly downward across the walls, down over the tree and down over both children, flakes clearly travelling from the top of frame towards the floor.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. Light-snow is pouring across the entire ceiling too, streaming away towards the far end of the room at the same speed. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[9] LIGHTING - warm dim room, the falling projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly pouring and shifting across them.

[10] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: children laughing and squealing, and cushions compressing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light-snow is visibly falling in every single frame, on the walls and on the ceiling; a viewer can follow individual flakes travelling downward. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room.
BANNED: any music, any song, any score, any soundtrack; a projected pattern that stays in the same place; shapes that only brighten, twinkle or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; a static or frozen projected pattern; snow that falls for a moment then stops; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child, an adult, the children standing still, jellyfish or fish or any underwater imagery, the projector unit visible anywhere in frame, a cut, subtitles, on-screen text.
````

#### Video prompt — `clips/v1_c07_g5.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `d6a1e2c1-dcb6-449a-a837-da36f77322d6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_192147_d6a1e2c1-dcb6-449a-a837-da36f77322d6.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `88a5ad92-3965-4b0e-8d9a-9d983c5e0a5a`
- video ref 1: uploaded image, not on the drive · Higgsfield media `0950f1d2-62b5-42fa-8d5d-5f23b658af53`

````text
RULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on every wall and on the entire ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running in this exact kind of double-height living room. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the way the whole field of glowing shapes slides and swarms across the plaster without ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

WHAT THE LIGHT DOES, described so it cannot be mistaken for a texture:
- The whole field of glowing shapes SLIDES BODILY across the walls and across the ceiling, the way light from a spinning projector head sweeps a room. It never locks onto the plaster.
- On top of that sliding, individual shapes POUR DOWNWARD like heavy snowfall filmed through a window at night, and each one spins slowly as it goes and drags a faint soft trail.
- SPEED: a single shape crosses the full height of the wall in ABOUT ONE SECOND. That is fast. A viewer must see it moving within the first quarter second of the clip.
- THE TEST: take any two frames a third of a second apart and lay them on top of each other. NOT ONE glowing shape is in the same place. Not one. If any shape has stayed put, the clip is wrong.
- The moving light also pours down over the tree, the sofa, the staircase and across both children's faces and pyjamas as it passes over them, so the brightness on everything in the room is changing continuously.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

AUDIO RULE - SECOND MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

FRAMING FIX RULE: the start image has a problem in the TOP RIGHT of frame - a dark angular unlit wedge of ceiling and a hard diagonal seam line where the projection stops, so the room reads as a strange broken shape. THIS MUST BE GONE BY 1.0s. The person filming takes ONE clear step forward into the room at the start of the clip, which reframes the shot: the dark wedge and the diagonal seam leave the frame entirely and are replaced by more of the same lit ceiling with light sweeping across it. From 1.0s onward there is NO dark unlit triangle and NO hard diagonal cut-off line anywhere in frame. The living room must read as a normal, well-proportioned, comprehensible room.

IMAGE QUALITY RULE: the finished clip must look at least as sharp and as clean as the start image. Hold its exact sharpness, exposure, contrast and fine detail. Crisp modern phone footage, in focus throughout. BANNED: blur, soft focus, haze, mushy low-detail surfaces, plastic or waxy skin, colour shift, washed-out exposure, a dreamy or filtered look.

TASK: image-to-video. The start image is frame 0.0s. Hold its living room, tree, children, pyjamas, geometry and materials exactly - but NOT its stillness, NOT the position of its light pattern, and apart from the framing fix above.

[1] SUMMARY
Two excited children play in a Christmas living room while light sweeps and pours down every wall and the ceiling, one jumping on the sofa; the camera steps forward and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone footage, warm dim double-height living room lit only by the moving projection, sharp and clean, correctly exposed, slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the room, the tree, both children, their pyjamas, the LOOK and COLOUR of the Christmas shapes and the lighting. It is a photograph - copy its look, NEVER its stillness or its top-right framing problem.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.

[4] CHARACTERS
THE GIRL - on the rug on the left, back to camera, arms out, spinning.
THE BOY - on the right, jumping on the cream sectional sofa, arms up.
COUNT LOCK: exactly two children. No third child, no adults, no pets.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a tall lit Christmas tree centre, tall black-framed windows on the left, a staircase on the right, a cream sectional sofa on the right, an ottoman front centre, a rug on the floor. Sweeping, pouring light covers the walls and the ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the person filming takes ONE clear step forward into the room. The frame moves in and settles; the dark angular wedge and the diagonal seam in the top right slide out of frame and are replaced by more lit ceiling with light sweeping across it. THE BOY bounces on the sofa cushion, knees bending, arms up over his head, mouth open laughing. THE GIRL spins on the rug with both arms out, laughing, face turned upward. The field of light is already sliding and raining steadily down every wall.
1.0-2.0s - the camera is settled in its new closer position. THE BOY pushes off harder and jumps higher off the cushion, both feet leaving it, arms straight up. THE GIRL keeps turning and tips her head back to look up. Glowing shapes sweep sideways and pour visibly downward across the walls, down over the tree and down over both children, clearly travelling from the top of frame towards the floor.
2.0-4.0s - one single continuous camera move: the camera TILTS UPWARD past the top of the tree until the CEILING fills the upper half of frame. The light is sweeping and pouring across the entire ceiling too, streaming away towards the far end of the room at the same speed. Both children stay in the lower part of frame and keep moving - THE BOY still bouncing, THE GIRL still turning.

[8] CAMERA AND OPTICS - vertical 9:16, normal wide-angle phone lens, chest height. Two movements only: the single step forward from 0.0-1.0s, and the upward tilt from 2.0s. No cut, no orbit, no whip pan. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls or leaning windows.

[9] LIGHTING - warm dim room, the moving projection is the only bright light source, so the light on the walls, the ceiling, the tree and the children is constantly pouring and shifting across them. Do not flood the room with one flat colour.

[10] PHYSICS - the sofa cushion compresses and springs back under each landing. THE BOY stays on the sofa. Pyjamas and hair move naturally with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly two things and nothing else: children laughing and squealing, and cushions compressing. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Exactly two children, both visibly excited and moving in every frame. The room reads as a normal living room. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; a dark unlit wedge or triangle in the top right; a hard diagonal line where the projection stops; a strange or broken-looking room shape; a third child; an adult; the children standing still; jellyfish, fish, coral, bubbles or any underwater imagery; the projector unit visible anywhere in frame; a cut; subtitles; on-screen text.
````

### Board text retired on 2026-09-23

These prompt texts were on the board but match no Higgsfield job and no text elsewhere in this file. Kept here verbatim so nothing is lost; do not reuse them — use the verified prompts above.

#### C03 — board label "Prompt"

````text
COPY @Image 1 EXACTLY. The ONLY thing that changes is the kitchen behind her. Everything else is a literal copy.KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, the jewellery, the sleeve, and the white marble countertop.THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the bright white marble countertop occupies the LOWER RIGHT of the frame as a clean pale wedge running diagonally, passing behind and below her right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.THE POSE — her two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but her fingers, with a visible gap of air between the base of the stand and the marble below. Left forearm enters from the lower left in a cream ribbed knit sleeve pushed back; right forearm enters from the right with a thin gold bangle at the wrist and two slim gold rings on the fingers. Fair skin, neat natural nails.SCALE AND PLACEMENT — the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.THE PRODUCT — a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.THE COUNTER — honed white marble with soft cool-grey veining and a squared edge, matte sheen.THE KITCHEN — this is the only change. A warm modern kitchen, softly defocused: pale greige flat-front shaker cabinets with slim brushed-brass bar pulls, a stainless steel wall oven built into the tall cabinet run on the left, a white marble slab backsplash, a warm white LED strip glowing under the upper cabinets, and a pine garland with small warm fairy lights running high along the top of the cabinetry. Evening interior light, warm white, clean and even.Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfectly exposed, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### C04 — board label "Prompt"

````text
COPY @Image 1 EXACTLY. The ONLY thing that changes is the kitchen behind her. Everything else is a literal copy.CAMERA — this is the part that went wrong last time, so follow it precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently — a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The marble surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.THE PRODUCT — standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.THE HANDS — exactly as in @Image 1. Her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; on that wrist a stack of thin gold bangles, beige ribbed knit sleeve pushed back. Her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. Two slim gold rings on that hand. The white cable trails away to the right across the marble and off the frame. Both the connector and the port must be unobstructed and clearly readable.THE COUNTER — honed white marble with soft cool-grey veining and a squared edge, matte sheen.THE KITCHEN — this is the only change. A warm modern kitchen, softly defocused across the top third of the frame: pale greige flat-front shaker cabinets with slim brushed-brass bar pulls, a stainless steel wall oven built into the tall cabinet run on the right, a white marble slab backsplash, a warm white LED strip glowing under the upper cabinets, and a pine garland with small warm fairy lights running high along the top of the cabinetry. Evening interior light, warm white, clean and even.Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfectly exposed, zero motion blur, nothing blurry or soft, no CGI look.No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### C05 — board label "Prompt"

````text
Recreate @Image 1 with ONE change.KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same white panelled door, the same antique brass round doorknob, the same small pine wreath with the red velvet bow on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position, the same warm low-key evening light.THE CHANGE: the door is now FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out — no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
````

#### C05 — board label "Prompt"

````text
Recreate @Image 1 with two changes.KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same tall living room, the same Christmas light projection covering every wall and the ceiling — glowing Christmas trees, snowflakes, stars, baubles and candy canes in gold, green, red and blue — the same decorated tree, the same stockings on the mantel, the same white shelving, the same cream sofa with red tartan cushions, the same wrapped gifts, the same tall window on the left, the same camera position and height, the same magical low-key evening light.CHANGE 1 — the projector unit must NOT be visible. Remove the small white glowing device and its little side table from the lower left completely. Replace that corner with plain floor and the edge of the rug. No projector anywhere in frame.CHANGE 2 — the boy now stands TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder. The girl beside him stays exactly as she is, seen from behind, still looking up at the projected wall.Both children are fully dressed in warm red-and-white knitted Christmas jumpers and matching knitted lounge trousers with thick socks. Wholesome family Christmas scene.Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
````

#### C06 — board label "Prompt"

````text
Recreate @Image 1 with two changes.KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same cosy bedroom, the same Christmas light projection covering the walls and ceiling — glowing Christmas trees, snowflakes, stars, red baubles and candy canes — the same wooden bed with the dark green duvet, the cream knitted throw, the plaid pillows, the small lit Christmas tree beside the bed, the same stocking on the wall, the same camera position and height, the same magical low-key evening light.CHANGE 1 — the projector unit must NOT be visible. Remove the small white glowing device and the little stool it sits on from the lower left completely. Replace that corner with plain wall and floor. No projector anywhere in frame.CHANGE 2 — the boy is now standing UP ON THE BED, barefoot on the mattress in the middle of the duvet, knees bent and arms raised out to his sides, caught mid-bounce with the duvet dimpling under his feet, head tipped back looking up at the projected ceiling, laughing. He is clearly on top of the bed, not sitting on its edge.The boy is fully dressed in a warm red-and-white knitted Christmas jumper and matching knitted lounge trousers. Wholesome family Christmas scene.Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
````

#### C07 — board label "Prompt"

````text
Recreate @Image 1 with two changes.KEEP IDENTICAL: the same vertical 9:16 iPhone photo of the same enormous double-height living room, the same Christmas light projection blanketing the whole ceiling and every wall — glowing Christmas trees, snowflakes, stars and baubles in blue, gold, green and red — the same tall black-framed windows on the left, the same big decorated Christmas tree, the same staircase with lit garland on the right, the same long cream sectional sofa and ottoman, the same camera position and height, the same magical low-key evening light.CHANGE 1 — the projector unit must NOT be visible. Remove the small white glowing device and the round side table from the lower left completely. Replace that corner with plain rug and floor. No projector anywhere in frame.CHANGE 2 — add TWO children to the room: a boy and a girl. The girl is JUMPING ON THE SOFA — caught mid-air above the cream sectional cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off. The boy stands on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room.Both children are fully dressed in warm red-and-white knitted Christmas jumpers and matching knitted lounge trousers with thick socks. Wholesome family Christmas scene.Natural handheld UGC look, tack sharp, perfectly exposed, zero motion blur, no CGI look.
````
