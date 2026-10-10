# Video 12 - B-roll image archive

**C01 hook status (2026-09-21):** image and clips/v12_c01_g1.mp4 approved by Daniel.

**Current status (2026-09-21):** 6/6 requested B-roll clips saved and added to board for review. One generation per C02-C07 shot, Seedance 2.5 at 720p. Requested durations 4/4/4/5/5/4 seconds. C05 has no end frame and uses this video's C07 moving room reference. C01 is separate work.
**Latest correction status (2026-09-22):** C06 take 5 completed and on the board for review. Earlier outputs and failed-job records preserved.
**Review corrections:** C06 take 2, C07 take 2 saved and on the board for review. Previous takes remain available with the user-reported rejection reasons.

**Settings:** Higgsfield `gpt_image_2_5`; variant `sunburst`; resolution `2k`; quality `medium`; aspect_ratio `9:16`; count `1`. Reference role `image` is mapped by the backend to `image_references`.

## Reusable blocks
Camera, product geometry, hand positions and projection-quality wording reopened from video 11's exact archive. Full submitted text is recorded below. Named materials, people, rooms, Christmas content and surface-specific light mapping are the changes. No motion prompts were requested or submitted.

## C02 - starting frame

**Frame:** `starting_frames/v12_c02_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** 48f89cec-1b88-4bf9-bf8a-78bd0711a977
**Status:** Completed and saved locally; awaiting Daniel's review.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c02_g1.png` - bbfc652c-e9eb-4430-9b53-610b56917312 - role image (backend image_references)
2. `../../product_images/box_festive_green_g2.png` - 2597b25d-60d1-4060-9602-32b0ee26c2f7 - role image (backend image_references)

Reused from v11 C02 take 1 - changed: Hands/skin and sleeve: about 29, with fair freckled skin and slender fingers, cranberry-red ribbed wool. Table and background: a dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge; a warmly lit Georgian Christmas dining room with powder-blue walls, white panel mouldings, a carved white fireplace with cranberry stockings, a dark mahogany sideboard, and a decorated fir tree with red tartan ribbons and warm gold lights. All camera, grip, scale, product and sharpness wording retained.

### Image prompt
```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 29, with fair freckled skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a cranberry-red ribbed wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a warmly lit Georgian Christmas dining room with powder-blue walls, white panel mouldings, a carved white fireplace with cranberry stockings, a dark mahogany sideboard, and a decorated fir tree with red tartan ribbons and warm gold lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The later animation request and exact submitted take are archived below.

### Take history
Take 1 only. Awaiting Daniel's review. No prior generation overwritten. No reroll.


### Video prompt - take 1

**Clip:** clips/v12_c02_g1.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 4, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "48f89cec-1b88-4bf9-bf8a-78bd0711a977"}, {"role": "image", "value": "48f89cec-1b88-4bf9-bf8a-78bd0711a977"}]}
**Job ID:** 89534e88-5a63-46cd-bdbc-2abf89bffd40
**Status:** Completed, saved locally and added to the board; awaiting Daniel's review. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested 4s; audio stream present; 1876173 bytes.
**Sampled visual review:** Sampled frames preserve the supplied opening composition and printed THEXMASGLOW box artwork. The right hand lifts the projector out of frame while the left hand remains on the lower carton. One generation; awaiting Daniel's review.
**References, in order:**
- {"role": "start_image", "value": "48f89cec-1b88-4bf9-bf8a-78bd0711a977", "path": "starting_frames/v12_c02_g1.png"}
- {"role": "image", "value": "48f89cec-1b88-4bf9-bf8a-78bd0711a977", "path": "starting_frames/v12_c02_g1.png"}
**Backend adjustments:** {"medias[1].role": {"requested": "image", "used": "image_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v11 C02 video take 1 - scene nouns changed to the existing video 12 images. All unchanged source motion/camera/timing text preserved verbatim. C02 contains the requested new one-handed lift, carton-hand and original-artwork corrections; its video reference was removed. C05 uses the approved g4 camera continuity and this video own C07 moving room reference. Full exact changes follow.

```text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a cranberry-red ribbed wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a warmly lit Georgian Christmas dining room with powder-blue walls, white panel mouldings, a carved white fireplace with cranberry stockings, a dark mahogany sideboard, and a decorated fir tree with red tartan ribbons and warm gold lights. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
```

#### Exact source edits - in application order

1. Physical scene nouns adapted to the existing starting frame.

Before:
```text
ivory cable-knit wool
```

After / added:
```text
cranberry-red ribbed wool
```

2. Physical scene nouns adapted to the existing starting frame.

Before:
```text
[5] LOCATION - a honey-toned elm table fills the frame: broad flowing timber grain, a matte finish and a substantial straight edge. A lit cream pillar candle sits at the left, fir sprigs with white berries and small antique gold and pearl-white baubles beside it, and behind it, sharply in focus, muted forest-green walls with cream picture rails, a cream limestone fireplace with brass candleholders and red knitted stockings, a Christmas tree with red glass baubles and gold ribbon to the left, and a built-in dark walnut bookcase to the right. The candle, the fir, the berries, the baubles, the fireplace and the tree must still be in the final frame.
```

After / added:
```text
[5] LOCATION - a dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a warmly lit Georgian Christmas dining room with powder-blue walls, white panel mouldings, a carved white fireplace with cranberry stockings, a dark mahogany sideboard, and a decorated fir tree with red tartan ribbons and warm gold lights. The same table, carton, decorations and background remain visible through the final frame.
```

3. Physical scene nouns adapted to the existing starting frame.

Before:
```text
honey-toned elm table
```

After / added:
```text
dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge
```

4. Physical scene nouns adapted to the existing starting frame.

Before:
```text
The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. 
```

After / added:
```text
No video reference is attached. 
```

5. Daniel requested a one-handed lift with the other hand remaining on the box.

Before:
```text
BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.
```

After / added:
```text
HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.
```

6. Update exit to preserve carton hand.

Before:
```text
EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.
```

After / added:
```text
EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.
```

7. Remove conflicting unboxing video reference; reinforce exact frame and artwork.

Before:
```text
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.
```

After / added:
```text
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.
```

8. One opening hand; second hand anchors carton.

Before:
```text
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
```

After / added:
```text
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
```

9. One-handed product grip.

Before:
```text
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
```

After / added:
```text
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
```

10. Correct hand roles during lift.

Before:
```text
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
```

After / added:
```text
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
```

11. Correct hand roles during exit.

Before:
```text
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
```

After / added:
```text
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
```

12. Keep stabilizing hand visible to end.

Before:
```text
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge, lid flaps folded back, with the candle, the fir, the berries, the fireplace and the tree still in shot. Nothing else moves.
```

After / added:
```text
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.
```

13. Physical scene nouns adapted to the existing starting frame.

Before:
```text
and settles once the hands have gone
```

After / added:
```text
and settles against the left hand, which remains on the carton
```

14. Physical scene nouns adapted to the existing starting frame.

Before:
```text
Exactly two hands, and both of them are on the product for the whole lift and the whole exit.
```

After / added:
```text
Exactly two hands: the right lifts the product; the left remains on the box throughout.
```

15. Physical scene nouns adapted to the existing starting frame.

Before:
```text
the last frame shows only the open box on the table.
```

After / added:
```text
the last frame shows the open printed box on the table with the left hand still bracing it.
```

16. Remove obsolete two-handed bans and lock visible printed box.

Before:
```text
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
```

After / added:
```text
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
```

17. Daniel requested the actual starting frame and visible original carton design.

After / added:
```text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.
```

18. Match the actual supplied starting hand positions.

Before:
```text
[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.
```

After / added:
```text
[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.
```

#### Animation take history
Take 1 completed, saved and added to board for review. No reroll. C01 is separate work and unchanged by this B-roll round.

## C03 - starting frame

**Frame:** `starting_frames/v12_c03_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** 0ee1c12a-5989-4980-b36a-a7efd0ddefe1
**Status:** Completed and saved locally; awaiting Daniel's review.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c03_g1.png` - 4b0ce2fa-f22e-4fdc-a781-0a2f43789130 - role image (backend image_references)
2. `../video_10_assets/starting_frames/v10_c03_g1.png` - 89ed549a-35bb-4e66-8865-c5a112bc239a - role image (backend image_references)

Reused from v11 C03 take 1 - changed: Hands/skin and sleeve: about 29, with fair freckled skin and slender fingers, cranberry-red ribbed wool. Counter and kitchen: a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge; powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range. All camera, grip, scale, product and sharpness wording retained.

### Image prompt
```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 29, with fair freckled skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a cranberry-red ribbed wool sweater sleeve pushed back; right forearm enters from the right in the same cranberry-red ribbed wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The later animation request and exact submitted take are archived below.

### Take history
Take 1 only. Awaiting Daniel's review. No prior generation overwritten. No reroll.


### Video prompt - take 1

**Clip:** clips/v12_c03_g1.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 4, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "0ee1c12a-5989-4980-b36a-a7efd0ddefe1"}]}
**Job ID:** fb519a5f-f70d-40f1-bb13-356c7e92bb7d
**Status:** Completed, saved locally and added to the board; awaiting Daniel's review. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested 4s; audio stream present; 1485928 bytes.
**Sampled visual review:** Sampled frames show a two-handed lift, lowering onto the counter and release, with the original kitchen and counter retained. One generation; awaiting review.
**References, in order:**
- {"role": "start_image", "value": "0ee1c12a-5989-4980-b36a-a7efd0ddefe1", "path": "starting_frames/v12_c03_g1.png"}
**Backend adjustments:** {}

Reused from v11 C03 video take 1 - scene nouns changed to the existing video 12 images. All unchanged source motion/camera/timing text preserved verbatim. C02 contains the requested new one-handed lift, carton-hand and original-artwork corrections; its video reference was removed. C05 uses the approved g4 camera continuity and this video own C07 moving room reference. Full exact changes follow.

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in cranberry-red ribbed wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge; behind it powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
```

#### Exact source edits - in application order

1. Physical scene nouns adapted to the existing starting frame.

Before:
```text
ivory cable-knit wool
```

After / added:
```text
cranberry-red ribbed wool
```

2. Physical scene nouns adapted to the existing starting frame.

Before:
```text
[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a pale ivory honed travertine countertop - small natural pores and delicate beige mineral veins, matte stone and a straight square edge - fills the lower half of frame and stays there for the whole clip; behind it a warm Christmas kitchen with deep sage-green inset cabinets with aged brass cup pulls, a brushed brass range built into the tall cabinet run on the left, a warm ivory square ceramic tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays crisp and in focus, matching the start image. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.
```

After / added:
```text
[5] LOCATION - hold every detail visible in the start image: a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge; behind it powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.
```

3. Physical scene nouns adapted to the existing starting frame.

Before:
```text
pale ivory honed travertine kitchen counter
```

After / added:
```text
white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge
```

4. Physical scene nouns adapted to the existing starting frame.

Before:
```text
travertine counter
```

After / added:
```text
white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge
```

5. Physical scene nouns adapted to the existing starting frame.

Before:
```text
The travertine is hard
```

After / added:
```text
The counter is hard
```

#### Animation take history
Take 1 completed, saved and added to board for review. No reroll. C01 is separate work and unchanged by this B-roll round.

## C04 - starting frame

**Frame:** `starting_frames/v12_c04_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** 36021679-fd7f-46b5-bb2c-70929fdee825
**Status:** Completed and saved locally; awaiting Daniel's review.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c04_g1.png` - e243effc-2c21-4bed-9551-e592483315ca - role image (backend image_references)
2. `../video_10_assets/starting_frames/v10_c04_g1.png` - 1d69a04c-84ad-4a97-8d55-d5ce334848c1 - role image (backend image_references)

Reused from v11 C04 take 1 - changed: Hands/skin and sleeve: about 29, with fair freckled skin and slender fingers, cranberry-red ribbed wool. Counter and kitchen: a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge; powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range. All camera, grip, scale, product and sharpness wording retained.

### Image prompt
```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 29, with fair freckled skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a cranberry-red ribbed wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The later animation request and exact submitted take are archived below.

### Take history
Take 1 only. Awaiting Daniel's review. No prior generation overwritten. No reroll.


### Video prompt - take 1

**Clip:** clips/v12_c04_g1.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 4, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "36021679-fd7f-46b5-bb2c-70929fdee825"}]}
**Job ID:** 3eab3881-bde4-4e25-8123-1edb15476884
**Status:** Completed, saved locally and added to the board; awaiting Daniel's review. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested 4s; audio stream present; 1008437 bytes.
**Sampled visual review:** Sampled frames show the cable seating in the lower dome-body socket, followed by red illumination, and the plug remaining connected. One generation; awaiting review.
**References, in order:**
- {"role": "start_image", "value": "36021679-fd7f-46b5-bb2c-70929fdee825", "path": "starting_frames/v12_c04_g1.png"}
**Backend adjustments:** {}

Reused from v11 C04 video take 1 - scene nouns changed to the existing video 12 images. All unchanged source motion/camera/timing text preserved verbatim. C02 contains the requested new one-handed lift, carton-hand and original-artwork corrections; its video reference was removed. C05 uses the approved g4 camera continuity and this video own C07 moving room reference. Full exact changes follow.

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand PLUGS a white USB-C connector INTO the small dark socket in the bottom rim of the projector's white dome, and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a cranberry-red ribbed wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same cranberry-red ribbed wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge; behind it powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the stone and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the stone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
```

#### Exact source edits - in application order

1. Physical scene nouns adapted to the existing starting frame.

Before:
```text
ivory cable-knit wool
```

After / added:
```text
cranberry-red ribbed wool
```

2. Physical scene nouns adapted to the existing starting frame.

Before:
```text
ivory cable-knit
```

After / added:
```text
cranberry-red ribbed wool
```

3. Physical scene nouns adapted to the existing starting frame.

Before:
```text
[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a pale ivory honed travertine countertop - small natural pores and delicate beige mineral veins, matte stone and a straight square edge - fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with deep sage-green inset cabinets with aged brass cup pulls, a brushed brass range built into the tall cabinet run on the right, a warm ivory square ceramic tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays crisp and in focus, matching the start image. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.
```

After / added:
```text
[5] LOCATION - hold every detail visible in the start image: a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge; behind it powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.
```

#### Animation take history
Take 1 completed, saved and added to board for review. No reroll. C01 is separate work and unchanged by this B-roll round.

## C05 - starting frame

**Frame:** `starting_frames/v12_c05_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** eb4c35e2-309e-446d-aff5-9ffd9d6c4ed6
**Status:** Completed and saved locally; awaiting Daniel's review.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c05_g1.png` - 6a0df249-6245-439e-a380-e9bbdf6dc580 - role image (backend image_references)
2. `../video_10_assets/starting_frames/v10_c05_g1.png` - c301edff-f38f-42fc-bdde-d914d68ab37d - role image (backend image_references)

Reused from v11 C05 take 1 - changed: Hands/skin and sleeve: about 29, with fair freckled skin and slender fingers, cranberry-red ribbed wool. Door: a midnight-navy painted two-panel door, one large recessed rectangular upper panel and one smaller lower panel, satin finish and delicate brush texture. All camera, grip, scale, product and sharpness wording retained.

### Image prompt
```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the cranberry-red ribbed wool sleeve and no jewellery, with fair freckled skin, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a midnight-navy painted two-panel door, one large recessed rectangular upper panel and one smaller lower panel, satin finish and delicate brush texture, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the midnight-navy paint reads clearly as deep blue rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The later animation request and exact submitted take are archived below.

### Take history
Take 1 only. Awaiting Daniel's review. No prior generation overwritten. No reroll.


### Video prompt - take 1

**Clip:** clips/v12_c05_g1.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "eb4c35e2-309e-446d-aff5-9ffd9d6c4ed6"}, {"role": "video", "value": "28e20c13-6f51-4af8-bfb9-fbeed0a92ecf"}]}
**Job ID:** 232c05ca-ad58-48be-86ea-c2521722f045
**Status:** Completed, saved locally and added to the board; awaiting Daniel's review. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; requested 5s; audio stream present; 4461001 bytes.
**Sampled visual review:** Five-second generation with the supplied closed-door start and moving C07 room reference, with no end frame. Sampled frames show children moving through the revealed room without a visible reference-pose hold. The camera advances and gradually raises its view toward the ceiling; please review the final framing. One take retained.
**References, in order:**
- {"role": "start_image", "value": "eb4c35e2-309e-446d-aff5-9ffd9d6c4ed6", "path": "starting_frames/v12_c05_g1.png"}
- {"role": "video", "value": "28e20c13-6f51-4af8-bfb9-fbeed0a92ecf", "video": 12, "path": "clips/v12_c07_g1.mp4", "original_name": "v12_c07_g1.mp4", "sha256": "13f3e46598b73ab0cceae28c5b93a87578d0333fae5e826dedaccba6bb4e6088", "duration": 4.05, "audio": true}
**Backend adjustments:** {"medias[1].role": {"requested": "video", "used": "video_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v11 C05 video take 4 - scene nouns changed to the existing video 12 images. All unchanged source motion/camera/timing text preserved verbatim. C02 contains the requested new one-handed lift, carton-hand and original-artwork corrections; its video reference was removed. C05 uses the approved g4 camera continuity and this video own C07 moving room reference. Full exact changes follow.

```text
CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.

CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the cathedral ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the gift wagon travels and the villagers work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a midnight-navy painted two-panel door, one large recessed rectangular upper panel and one smaller lower panel, satin finish and delicate brush texture fully closed with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, cathedral ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Inside the flat projected North Pole village picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny village children keep carrying and passing wrapped gifts beside the village, shooting stars streak and fade, the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit village windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the actual room surfaces. The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole cathedral ceiling and over every ceiling seam, right into all four corners. No bare un-animated patch of plaster and no bare ceiling detail anywhere in the closing framing.

BEATS
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera advances slowly through the doorway while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the gift wagon and the villagers keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl with warm tan skin and straight dark-brown hair in two loose braids runs a broad curving path across the rug and alongside the sofa; the boy with light skin, freckles and tousled auburn hair follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole cathedral ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, chimney surface and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and ceiling details. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.

ROOM AND IDENTITY - a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved cathedral ceiling and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. The children are a boy of about five with light skin, freckles and tousled auburn hair and a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Preserve these identities and this architecture from @Video 1.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.
```

#### Exact source edits - in application order

1. Physical scene nouns adapted to the existing starting frame.

Before:
```text
a closed three-panel forest-green door
```

After / added:
```text
a midnight-navy painted two-panel door, one large recessed rectangular upper panel and one smaller lower panel, satin finish and delicate brush texture fully closed
```

2. Physical scene nouns adapted to the existing starting frame.

Before:
```text
panel edges of the forest-green door
```

After / added:
```text
panel edges of the door
```

3. Physical scene nouns adapted to the existing starting frame.

Before:
```text
the bare forearm and its ivory sleeve
```

After / added:
```text
the forearm and sleeve exactly as shown in the starting image
```

4. Physical scene nouns adapted to the existing starting frame.

Before:
```text
copper-braided girl
```

After / added:
```text
girl with warm tan skin and straight dark-brown hair in two loose braids
```

5. Physical scene nouns adapted to the existing starting frame.

Before:
```text
dark-curled boy
```

After / added:
```text
boy with light skin, freckles and tousled auburn hair
```

6. Room/identity nouns adapted to new video.

After / added:
```text
ROOM AND IDENTITY - a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved barrel vault and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. The children are a boy of about five with light skin, freckles and tousled auburn hair and a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Preserve these identities and this architecture from @Video 1.
```

7. Physical scene nouns adapted to the existing starting frame.

Before:
```text
curved barrel-vault ceiling
```

After / added:
```text
cathedral ceiling
```

8. Physical scene nouns adapted to the existing starting frame.

Before:
```text
barrel-vault ceiling
```

After / added:
```text
cathedral ceiling
```

9. Physical scene nouns adapted to the existing starting frame.

Before:
```text
barrel vault
```

After / added:
```text
cathedral ceiling
```

10. Physical scene nouns adapted to the existing starting frame.

Before:
```text
shallow arch rib
```

After / added:
```text
ceiling seam
```

11. Physical scene nouns adapted to the existing starting frame.

Before:
```text
arch ribs
```

After / added:
```text
ceiling details
```

12. Physical scene nouns adapted to the existing starting frame.

Before:
```text
arch rib
```

After / added:
```text
ceiling detail
```

13. Physical scene nouns adapted to the existing starting frame.

Before:
```text
limestone chimney
```

After / added:
```text
warm-grey fieldstone chimney
```

14. Physical scene nouns adapted to the existing starting frame.

Before:
```text
limestone
```

After / added:
```text
chimney surface
```

15. Physical scene nouns adapted to the existing starting frame.

Before:
```text
ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the cathedral ceiling, steps over each ceiling seam and breaks at both projecting corners of the warm-grey fieldstone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.
```

After / added:
```text
ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the actual room surfaces. The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.
```

16. Replace workshop-specific set with current scene elements.

After / added:
```text
PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.
```

17. Animate corresponding objects already present in this video's Christmas artwork.

Before:
```text
THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
```

After / added:
```text
THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
```

18. Physical scene nouns adapted to the existing starting frame.

Before:
```text
toy train
```

After / added:
```text
gift wagon
```

19. Physical scene nouns adapted to the existing starting frame.

Before:
```text
the train advances
```

After / added:
```text
the gift wagon advances
```

20. Physical scene nouns adapted to the existing starting frame.

Before:
```text
tiny elves
```

After / added:
```text
tiny village children
```

21. Physical scene nouns adapted to the existing starting frame.

Before:
```text
elves
```

After / added:
```text
villagers
```

22. Physical scene nouns adapted to the existing starting frame.

Before:
```text
workshop
```

After / added:
```text
village
```

#### Animation take history
Take 1 completed, saved and added to board for review. No reroll. C01 is separate work and unchanged by this B-roll round.

## C05 F2 - room reference

**Reference:** `references/v12_c05_r1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** 16ec0091-87a5-4b00-9673-799570413b29
**Status:** Completed and saved locally; awaiting Daniel's review.
**References, in attached order:**
1. `../video_11_assets/references/v11_c05_r1.png` - dda4701e-8d9d-4351-99f8-60bb9093cf68 - role image (backend image_references)
2. `../video_9_assets/references/v9_c05_r4.png` - 1c500339-2855-45b6-bd9b-4c3633b5a272 - role image (backend image_references)

Reused from v11 C05 F2 take 1 - changed: New children and clothing: a boy of about five with light skin, freckles and tousled auburn hair; a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids; warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Room: a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved barrel vault and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Projection story: Snowy Christmas village. Architecture-specific mapping rewritten for those surfaces. Camera/pose, density, contrast, single-origin light and sharpness wording retained. C05/C07 share the new house and children.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about five with light skin, freckles and tousled auburn hair; the girl is of about eight with warm tan skin and straight dark-brown hair in two loose braids. Both children are fully dressed for winter in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved barrel vault and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Seen from the doorway; the new a midnight-navy painted two-panel door, one large recessed rectangular upper panel and one smaller lower panel, satin finish and delicate brush texture is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the muted cranberry wool rug, the cream boucle sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the surface texture of the fieldstone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
Not requested; no video generation performed.

### Take history
Take 1 only. Awaiting Daniel's review. No prior generation overwritten. No reroll.

## C06 - starting frame

**Frame:** `starting_frames/v12_c06_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** ad7bddc8-13d6-46cb-9af2-439134e2db10
**Status:** Completed and saved locally; awaiting Daniel's review.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c06_g1.png` - a11380c1-3dd8-4a0a-accc-481aec5fa3bf - role image (backend image_references)
2. `../video_9_assets/starting_frames/v9_c06_g4.png` - 480dee42-d78d-4dd4-b3b0-cca1aed16477 - role image (backend image_references)

Reused from v11 C06 take 1 - changed: New children and clothing: a boy of about five with light skin, freckles and tousled auburn hair; a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids; warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Room: a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Projection story: Snowy Christmas village. Architecture-specific mapping rewritten for those surfaces. Camera/pose, density, contrast, single-origin light and sharpness wording retained. C05/C07 share the new house and children.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about five with light skin, freckles and tousled auburn hair, fully dressed for winter in a warm forest-green and cream knitted Christmas jumper with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed has a cream wool duvet with red tartan throw, pillows and a knitted stocking. A small real Christmas tree with gold lights and red ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The later animation request and exact submitted take are archived below.

### Take history
Take 1 only. Awaiting Daniel's review. No prior generation overwritten. No reroll.


### Video prompt - take 1

**Clip:** clips/v12_c06_g1.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}]}
**Job ID:** 548bef39-7dd5-43d5-993e-f95cda060c4b
**Status:** Completed, saved locally and added to the board; awaiting Daniel's review. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; requested 5s; audio stream present; 5367789 bytes.
**Sampled visual review:** Review flag: the wall projection is present, but the ceiling starts mostly bare and fills during roughly the first 1.5 seconds despite the prompt requiring full projection from the start. The child keeps jumping. Single take retained; no reroll.
**References, in order:**
- {"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png"}
**Backend adjustments:** {}

Reused from v11 C06 video take 1 - scene nouns changed to the existing video 12 images. All unchanged source motion/camera/timing text preserved verbatim. C02 contains the requested new one-handed lift, carton-hand and original-artwork corrections; its video reference was removed. C05 uses the approved g4 camera continuity and this video own C07 moving room reference. Full exact changes follow.

```text
Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the cream plaster wall and the asymmetric attic ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the asymmetric attic ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

#### Exact source edits - in application order

1. Physical scene nouns adapted to the existing starting frame.

Before:
```text
ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the hipped ceiling with its small flat central panel, four broad sloping plaster planes and four straight hip seams, the cream plaster walls, the bed with its cream duvet and red tartan throw, the scalloped walnut headboard, the upholstered bench at the foot, the small lit Christmas tree, the wool rug, the right-hand recessed bay window with burgundy curtains, the stocking, THE BOY and the colour.
```

After / added:
```text
ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.
```

2. Physical scene nouns adapted to the existing starting frame.

Before:
```text
THE BOY - exactly one child, about six years old with warm brown skin and close-cropped dark curls, in cosy red-and-cream knitted Christmas jumper with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
```

After / added:
```text
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
```

3. Physical scene nouns adapted to the existing starting frame.

Before:
```text
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.
```

After / added:
```text
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.
```

4. Physical scene nouns adapted to the existing starting frame.

Before:
```text
The start image is one paused frame of that film; at 0.0s it un-pauses.
```

After / added:
```text
The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance.
```

5. Physical scene nouns adapted to the existing starting frame.

Before:
```text
SURFACE MAPPING - the moving picture bends at every real hip seam between the four sloping ceiling planes and the central flat panel, foreshortens on each plane and changes angle again onto the vertical walls and window recess. The planes and seams themselves never move.
```

After / added:
```text
SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

6. Physical scene nouns adapted to the existing starting frame.

Before:
```text
hipped plaster ceiling
```

After / added:
```text
asymmetric attic ceiling
```

7. Physical scene nouns adapted to the existing starting frame.

Before:
```text
hipped ceiling
```

After / added:
```text
asymmetric attic ceiling
```

8. Physical scene nouns adapted to the existing starting frame.

Before:
```text
hip seams of the ceiling
```

After / added:
```text
seams of the ceiling
```

9. Physical scene nouns adapted to the existing starting frame.

Before:
```text
North Pole Christmas workshop
```

After / added:
```text
Christmas village
```

10. Animate corresponding objects already present in this video's Christmas artwork.

Before:
```text
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
```

After / added:
```text
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
```

11. Physical scene nouns adapted to the existing starting frame.

Before:
```text
toy train
```

After / added:
```text
gift wagon
```

12. Physical scene nouns adapted to the existing starting frame.

Before:
```text
the train advances
```

After / added:
```text
the gift wagon advances
```

13. Physical scene nouns adapted to the existing starting frame.

Before:
```text
tiny elves
```

After / added:
```text
tiny village children
```

14. Physical scene nouns adapted to the existing starting frame.

Before:
```text
elves
```

After / added:
```text
villagers
```

15. Physical scene nouns adapted to the existing starting frame.

Before:
```text
workshop
```

After / added:
```text
village
```

#### Animation take history
Take 1 completed, saved and added to board for review. No reroll. C01 is separate work and unchanged by this B-roll round.


### Video prompt - take 2 (user-requested correction)

**Clip:** clips/v12_c06_g2.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}, {"role": "image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}]}
**Job ID:** 594b672b-c09a-4cd0-b706-1773cbeec10f
**Status:** Completed and added to board for review. One replacement generation; no automatic reroll.
**Output verification:** {"width": 720, "height": 1280, "duration": 5.05, "frames": "121", "fps": "24/1", "audio": true, "bytes": 6085217, "review_sheet": "C:\\Users\\<user>\\AppData\\Local\\Temp\\v12_c06_g2_review.jpg"}
**Sampled visual review:** Take 2 sampled review: projection is already visible on the wall and sloping ceiling at the opening, but a large bare upper ceiling panel remains in the framing. This does not fully satisfy the requested complete ceiling coverage. The child and projected elements move. One replacement only; flagged for Daniel's review.
**References, in order:**
- {"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png"}
- {"role": "image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png", "purpose": "Same approved frame locks the already-projected look."}
**Backend adjustments:** {"medias[1].role": {"requested": "image", "used": "image_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v12 C06 video take 1 - only the requested motion correction and explicitly recorded supporting changes below. Same starting frame, model, resolution, duration and camera choreography.
**User review of take 1:** Rejected - Projection appeared during the opening instead of already covering the walls and ceiling.

```text
OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the cream plaster wall and the asymmetric attic ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the asymmetric attic ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

**Exact changes and reasons:**
```json
[
  {
    "from": "",
    "to": "OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.",
    "reason": "Preserve complete projection from frame zero."
  },
  {
    "from": "DO NOT INCLUDE: a camera",
    "to": "DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera",
    "reason": "Exclude rejected opening transition."
  }
]
```


### Video prompt - take 3 (user-requested correction)

**Clip:** clips/v12_c06_g3.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}, {"role": "image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}]}
**Job ID:** b264b66d-ba1a-460a-8d11-e6742eb73b13
**Status:** Completed, saved and added to the board for review; one replacement generation.
**Output verification:** {"width": 720, "height": 1280, "duration": 5.05, "frames": "121", "fps": "24/1", "audio": true, "bytes": 4344272, "review_sheet": "C:\\Users\\<user>\\AppData\\Local\\Temp\\v12_c06_g3_review.jpg"}
**Sampled visual review:** Take 3 sampled review: the opening now shows the boy's full body and bed with projection already covering all visible ceiling panels and the back wall at 0.0, 0.1 and 0.3 seconds. The previous bare upper panel is absent. The child and projected sleigh keep moving. The opening remains slightly tighter than the supplied still, but is lower than take 2. One replacement generated; awaiting Daniel's review.
**References, in order:**
- {"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png"}
- {"role": "image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png", "purpose": "Same approved frame locks the already-projected look."}
**Backend adjustments:** {"medias[1].role": {"requested": "image", "used": "image_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v12 C06 video take 2 - changed only the lines documented below to address the new user review. Same starting frame, references, model, resolution and five-second duration.
**User review of take 2:** Rejected - Opening camera is too high and half the ceiling lacks projection.

```text
OPENING FRAMING AND COVERAGE - PRIMARY CORRECTION: use the approved starting image itself as the exact first camera frame, not merely a room reference. The camera must not begin tilted upward, close to the ceiling or above the supplied viewpoint. Show the whole jumping boy, full bed and foot bench from frame zero in the same composition as @Image 1. Every visible flat ceiling panel AND every visible sloping ceiling panel already carries the dense Christmas artwork at full brightness. Do not invent a new pale foreground ceiling, soffit, overhang or blank triangular panel. The camera does not reveal any extra unprojected space above the source framing. The full projection is already playing before filming and never fades in. Keep the same starting frame and existing physical room; correct the camera angle, not the architecture.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - START AT THE SUPPLIED IMAGE'S EXISTING LOWER COMPOSITION, then make a very small downward tilt followed by a gentle physical pull back. Never re-aim upward before frame zero.
0.0-2.2s the camera begins at EXACTLY @Image 1's angle and framing: the boy's whole body and the full mattress are clearly visible around the middle and lower half, with the foot-of-bed bench and floor visible below, while the already projected wall and ceiling occupy the upper half. Do not start above this framing or crop the boy at the bottom. From this exact view, tilt downward only about 3 degrees in one slow steady move, retaining the fully projected ceiling in the upper part of the frame. The ribbons ripple, gold light waves travel and the sleigh flies across the existing projected ceiling. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small physical backward step with the same fixed focal length, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

**Exact changes and reasons:**
```json
[
  {
    "from": "TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.",
    "to": "TIMELINE - START AT THE SUPPLIED IMAGE'S EXISTING LOWER COMPOSITION, then make a very small downward tilt followed by a gentle physical pull back. Never re-aim upward before frame zero.",
    "reason": "Remove high-start instruction responsible for new bare ceiling entering the opening."
  },
  {
    "from": "0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the cream plaster wall and the asymmetric attic ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the asymmetric attic ceiling as it goes, until the bed and THE BOY fill the lower half.",
    "to": "0.0-2.2s the camera begins at EXACTLY @Image 1's angle and framing: the boy's whole body and the full mattress are clearly visible around the middle and lower half, with the foot-of-bed bench and floor visible below, while the already projected wall and ceiling occupy the upper half. Do not start above this framing or crop the boy at the bottom. From this exact view, tilt downward only about 3 degrees in one slow steady move, retaining the fully projected ceiling in the upper part of the frame. The ribbons ripple, gold light waves travel and the sleigh flies across the existing projected ceiling.",
    "reason": "Lower opening to actual starting frame and remove invented high ceiling view."
  },
  {
    "from": "a small gentle zoom out, nothing sudden.",
    "to": "a small physical backward step with the same fixed focal length, nothing sudden.",
    "reason": "Keep gentle wider view without lens zoom."
  },
  {
    "from": "",
    "to": "OPENING FRAMING AND COVERAGE - PRIMARY CORRECTION: use the approved starting image itself as the exact first camera frame, not merely a room reference. The camera must not begin tilted upward, close to the ceiling or above the supplied viewpoint. Show the whole jumping boy, full bed and foot bench from frame zero in the same composition as @Image 1. Every visible flat ceiling panel AND every visible sloping ceiling panel already carries the dense Christmas artwork at full brightness. Do not invent a new pale foreground ceiling, soffit, overhang or blank triangular panel. The camera does not reveal any extra unprojected space above the source framing. The full projection is already playing before filming and never fades in. Keep the same starting frame and existing physical room; correct the camera angle, not the architecture.",
    "reason": "User rejects high opening and bare half-ceiling."
  }
]
```


### Video prompt - take 4 (2026-09-22, resumed after credits refill)

**Clip:** clips/v12_c06_g4.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}, {"role": "image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}]}
**Job ID:** 71426913-f33c-4db7-9725-96c5b6c9970c
**Status:** Completed, saved and added to board for review. One generation after credits refill.
**Output verification:** {"width": 720, "height": 1280, "duration": 5.05, "frames": "121", "fps": "24/1", "audio": true, "bytes": 4020937, "review_sheets": ["C:\\Users\\<user>\\AppData\\Local\\Temp\\v12_c06_g4_review_1.jpg", "C:\\Users\\<user>\\AppData\\Local\\Temp\\v12_c06_g4_review_2.jpg"]}
**Sampled visual review:** Take 4 sampled every 0.25 seconds: repeated short bounce cycles replace the prolonged jump timing, with prompt landings and rebounds. The lower opening and already projected wall/ceiling remain intact. One five-second generation at 720p; awaiting Daniel's playback review.
**References, in order:**
- {"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png"}
- {"role": "image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png", "purpose": "Same approved frame locks the already-projected look."}
**Backend adjustments:** {"medias[1].role": {"requested": "image", "used": "image_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v12 C06 take 3 - changed the speed instruction and child bounce timing only. User rejected take 3 as slowed down; preserve its lower opening and full projected ceiling.

```text
REAL-TIME SPEED - PRIMARY CORRECTION: this is an ordinary phone recording played at exactly 1x speed, never slow motion or high-frame-rate footage played back slowly. The boy makes five to six small lively mattress bounces across the five-second clip, roughly one complete bounce every 0.8-1.0 second. Each bounce has a quick knee bend, brief push-off, only about 0.3 second in the air, a prompt gravity-driven landing and immediate rebound. No long hang-time, suspended pose, languid arm swing, frozen apex, speed ramp or time stretching. He is already bouncing at frame zero and continues at the same natural cadence through the last frame. The camera's gentle movement is independent of the child's brisk normal-speed movement and must never slow him down. All projection motion also runs continuously at normal playback speed. Preserve the corrected lower opening and already complete ceiling coverage.

OPENING FRAMING AND COVERAGE - PRIMARY CORRECTION: use the approved starting image itself as the exact first camera frame, not merely a room reference. The camera must not begin tilted upward, close to the ceiling or above the supplied viewpoint. Show the whole jumping boy, full bed and foot bench from frame zero in the same composition as @Image 1. Every visible flat ceiling panel AND every visible sloping ceiling panel already carries the dense Christmas artwork at full brightness. Do not invent a new pale foreground ceiling, soffit, overhang or blank triangular panel. The camera does not reveal any extra unprojected space above the source framing. The full projection is already playing before filming and never fades in. Keep the same starting frame and existing physical room; correct the camera angle, not the architecture.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - START AT THE SUPPLIED IMAGE'S EXISTING LOWER COMPOSITION, then make a very small downward tilt followed by a gentle physical pull back. Never re-aim upward before frame zero.
0.0-2.2s the camera begins at EXACTLY @Image 1's angle and framing: the boy's whole body and the full mattress are clearly visible around the middle and lower half, with the foot-of-bed bench and floor visible below, while the already projected wall and ceiling occupy the upper half. Do not start above this framing or crop the boy at the bottom. From this exact view, tilt downward only about 3 degrees in one slow steady move, retaining the fully projected ceiling in the upper part of the frame. The ribbons ripple, gold light waves travel and the sleigh flies across the existing projected ceiling. THE BOY is already making repeated small normal-speed bounces, completing about two to three bounce cycles during this interval. Knees bend quickly, feet briefly leave the quilt, then land with real weight and rebound. Arms react naturally and quickly for balance, mouth open laughing. The mattress compresses and springs back on every landing.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small physical backward step with the same fixed focal length, nothing sudden. THE BOY maintains exactly the same brisk cadence, completing about three more small bounce cycles during this interval with short airtime and prompt landings. No higher slow jump or prolonged knee tuck. His real-time body motion carries straight across the camera transition without any slowing, pose hold or pause.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

**Exact changes and reasons:**
```json
[
  {
    "from": "",
    "to": "REAL-TIME SPEED - PRIMARY CORRECTION: this is an ordinary phone recording played at exactly 1x speed, never slow motion or high-frame-rate footage played back slowly. The boy makes five to six small lively mattress bounces across the five-second clip, roughly one complete bounce every 0.8-1.0 second. Each bounce has a quick knee bend, brief push-off, only about 0.3 second in the air, a prompt gravity-driven landing and immediate rebound. No long hang-time, suspended pose, languid arm swing, frozen apex, speed ramp or time stretching. He is already bouncing at frame zero and continues at the same natural cadence through the last frame. The camera's gentle movement is independent of the child's brisk normal-speed movement and must never slow him down. All projection motion also runs continuously at normal playback speed. Preserve the corrected lower opening and already complete ceiling coverage.",
    "reason": "User rejected slowed-down take; require normal bounce cadence and gravity."
  },
  {
    "from": "THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.",
    "to": "THE BOY is already making repeated small normal-speed bounces, completing about two to three bounce cycles during this interval. Knees bend quickly, feet briefly leave the quilt, then land with real weight and rebound. Arms react naturally and quickly for balance, mouth open laughing. The mattress compresses and springs back on every landing.",
    "reason": "Prevent one jump being stretched across the opening 2.2 seconds."
  },
  {
    "from": "THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.",
    "to": "THE BOY maintains exactly the same brisk cadence, completing about three more small bounce cycles during this interval with short airtime and prompt landings. No higher slow jump or prolonged knee tuck. His real-time body motion carries straight across the camera transition without any slowing, pose hold or pause.",
    "reason": "Keep natural speed over the second camera movement."
  }
]
```


### Video prompt - take 5 (2026-09-22, projected motion correction)

**Clip:** clips/v12_c06_g5.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}, {"role": "image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10"}]}
**Job ID:** 95aedab1-cd54-41ed-9d14-400a8fb6c376
**Status:** Completed, saved and added to board for review. One generation this round.
**Output verification:** {"width": 720, "height": 1280, "duration": 5.05, "frames": "121", "fps": "24/1", "audio": true, "bytes": 4738822, "review_sheets": ["C:\\Users\\<user>\\AppData\\Local\\Temp\\v12_c06_g5_review_1.jpg", "C:\\Users\\<user>\\AppData\\Local\\Temp\\v12_c06_g5_review_2.jpg"]}
**Visual review:** Take 5 generated once at 720p/5s. Sampled-frame review: the child bounces and the sleigh travels relative to the ceiling artwork, but most wall figures and decorations still appear largely fixed. Clear, sustained chimney-smoke animation is not established. This does not yet meet the requested majority-of-elements motion; flagged for Daniel's review.
**References, in order:**
- {"role": "start_image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png"}
- {"role": "image", "value": "ad7bddc8-13d6-46cb-9af2-439134e2db10", "path": "starting_frames/v12_c06_g1.png", "purpose": "Same approved frame locks the already-projected look."}
**Backend adjustments:** {"medias[1].role": {"requested": "image", "used": "image_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v12 C06 take 4 - projection-animation blocks revised; camera and child choreography, starting frame, references and settings retained. User rejected the previous take for insufficient projected-element movement.

```text
PRIMARY REQUIREMENT: this is a continuously ANIMATED Christmas movie projected on real walls and ceiling. The sleigh travels, reindeer gallop and smoke actively billows from every illustrated house chimney. Most other existing illustrated subjects move too. A static decorative image behind moving children is a failed result. Apply the detailed PROJECTED FILM ACTION below at every instant; retain the existing camera and child choreography.

REAL-TIME SPEED - PRIMARY CORRECTION: this is an ordinary phone recording played at exactly 1x speed, never slow motion or high-frame-rate footage played back slowly. The boy makes five to six small lively mattress bounces across the five-second clip, roughly one complete bounce every 0.8-1.0 second. Each bounce has a quick knee bend, brief push-off, only about 0.3 second in the air, a prompt gravity-driven landing and immediate rebound. No long hang-time, suspended pose, languid arm swing, frozen apex, speed ramp or time stretching. He is already bouncing at frame zero and continues at the same natural cadence through the last frame. The camera's gentle movement is independent of the child's brisk normal-speed movement and must never slow him down. All projection motion also runs continuously at normal playback speed. Preserve the corrected lower opening and already complete ceiling coverage.

OPENING FRAMING AND COVERAGE - PRIMARY CORRECTION: use the approved starting image itself as the exact first camera frame, not merely a room reference. The camera must not begin tilted upward, close to the ceiling or above the supplied viewpoint. Show the whole jumping boy, full bed and foot bench from frame zero in the same composition as @Image 1. Every visible flat ceiling panel AND every visible sloping ceiling panel already carries the dense Christmas artwork at full brightness. Do not invent a new pale foreground ceiling, soffit, overhang or blank triangular panel. The camera does not reveal any extra unprojected space above the source framing. The full projection is already playing before filming and never fades in. Keep the same starting frame and existing physical room; correct the camera angle, not the architecture.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

PROJECTED FILM ACTION - THE MAIN SUBJECT IS THE MOVING CHRISTMAS ARTWORK. Animate the existing illustrated objects themselves, not just the camera, children, brightness or glitter. At every moment MOST visible illustrated subjects are visibly changing position or shape independently. Keep the physical room and the projection's overall footprint fixed.
SLEIGH AND REINDEER: the existing sleigh team travels along the plaster ceiling at roughly one fifth of the visible ceiling width per second, crossing architectural seams and passing the fixed central star. Every reindeer continuously cycles its legs in a running gallop; heads bob, harnesses flex and the sleigh rocks behind them. The team must move relative to the stationary beams, star and ceiling corners in every half-second interval. Do not rotate the ceiling picture as a single disc.
CHIMNEYS: each visible illustrated house chimney continuously emits a clearly visible cream-grey animated smoke plume, contained INSIDE the flat wall illustration. New curls emerge every 0.25 second, rise one roof-height per second, expand and deform, then dissolve as more curls follow. Several different plumes must be visibly evolving at once; none may remain a frozen drawn squiggle. These are moving pixels on the wall, never real smoke entering the room.
VILLAGE: the existing illustrated figures walk along the wall, take full alternating steps and swing arms. Gift carriers lift and pass the existing parcels. Existing animal drawings walk with articulating legs, toy processions advance and wheels turn where present. Existing house-window light flickers independently. Buildings stay fixed so the moving figures and chimney smoke read clearly.
RIBBONS, GARLANDS AND BELLS: successive waves visibly deform each existing ribbon along its length while bright gold crests travel from the central star toward the walls, covering half a ribbon length per second. Existing bell drawings swing left-right-left roughly once per second with independently swinging clappers. Existing ornament drawings rotate within the projected picture. Do not leave the wall decorations frozen while only the ceiling sleigh moves.
SNOW AND STARS: existing snowflake drawings translate along the ceiling planes and down the walls continuously, at different speeds. Ceiling snow stays flush to ceiling plaster and follows its slope, never drops into the air. Stars twinkle independently while existing shooting-star streaks traverse the surface. Nothing moves over the boy or children, furniture, floor or in the open room.
All these actions run simultaneously from the first visible projected frame until the final frame, at normal playback speed, without a fade-in, opening pause, final freeze or settling back into the reference image. The supplied visual references fix architecture, identities and artwork appearance ONLY; replace their static or weak artwork motion with the explicit motion above. The original full projection is already on at frame zero or behind the closed door. All animated pixels bend at actual wall and ceiling seams, remain flat on those surfaces and are occluded by real foreground objects.

TIMELINE - START AT THE SUPPLIED IMAGE'S EXISTING LOWER COMPOSITION, then make a very small downward tilt followed by a gentle physical pull back. Never re-aim upward before frame zero.
0.0-2.2s the camera begins at EXACTLY @Image 1's angle and framing: the boy's whole body and the full mattress are clearly visible around the middle and lower half, with the foot-of-bed bench and floor visible below, while the already projected wall and ceiling occupy the upper half. Do not start above this framing or crop the boy at the bottom. From this exact view, tilt downward only about 3 degrees in one slow steady move, retaining the fully projected ceiling in the upper part of the frame. The ribbons ripple, gold light waves travel and the sleigh flies across the existing projected ceiling. THE BOY is already making repeated small normal-speed bounces, completing about two to three bounce cycles during this interval. Knees bend quickly, feet briefly leave the quilt, then land with real weight and rebound. Arms react naturally and quickly for balance, mouth open laughing. The mattress compresses and springs back on every landing.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small physical backward step with the same fixed focal length, nothing sudden. THE BOY maintains exactly the same brisk cadence, completing about three more small bounce cycles during this interval with short airtime and prompt landings. No higher slow jump or prolonged knee tuck. His real-time body motion carries straight across the camera transition without any slowing, pose hold or pause.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

**Exact changes and reasons:**
```json
[
  {
    "from": "HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.\nTHE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:\n- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.\n- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.\n- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.\n- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.\n- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.\n- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.\n- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.\n- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.\n- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.\n- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.\n- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.\nBecause the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.",
    "to": "PROJECTED FILM ACTION - THE MAIN SUBJECT IS THE MOVING CHRISTMAS ARTWORK. Animate the existing illustrated objects themselves, not just the camera, children, brightness or glitter. At every moment MOST visible illustrated subjects are visibly changing position or shape independently. Keep the physical room and the projection's overall footprint fixed.\nSLEIGH AND REINDEER: the existing sleigh team travels along the plaster ceiling at roughly one fifth of the visible ceiling width per second, crossing architectural seams and passing the fixed central star. Every reindeer continuously cycles its legs in a running gallop; heads bob, harnesses flex and the sleigh rocks behind them. The team must move relative to the stationary beams, star and ceiling corners in every half-second interval. Do not rotate the ceiling picture as a single disc.\nCHIMNEYS: each visible illustrated house chimney continuously emits a clearly visible cream-grey animated smoke plume, contained INSIDE the flat wall illustration. New curls emerge every 0.25 second, rise one roof-height per second, expand and deform, then dissolve as more curls follow. Several different plumes must be visibly evolving at once; none may remain a frozen drawn squiggle. These are moving pixels on the wall, never real smoke entering the room.\nVILLAGE: the existing illustrated figures walk along the wall, take full alternating steps and swing arms. Gift carriers lift and pass the existing parcels. Existing animal drawings walk with articulating legs, toy processions advance and wheels turn where present. Existing house-window light flickers independently. Buildings stay fixed so the moving figures and chimney smoke read clearly.\nRIBBONS, GARLANDS AND BELLS: successive waves visibly deform each existing ribbon along its length while bright gold crests travel from the central star toward the walls, covering half a ribbon length per second. Existing bell drawings swing left-right-left roughly once per second with independently swinging clappers. Existing ornament drawings rotate within the projected picture. Do not leave the wall decorations frozen while only the ceiling sleigh moves.\nSNOW AND STARS: existing snowflake drawings translate along the ceiling planes and down the walls continuously, at different speeds. Ceiling snow stays flush to ceiling plaster and follows its slope, never drops into the air. Stars twinkle independently while existing shooting-star streaks traverse the surface. Nothing moves over the boy or children, furniture, floor or in the open room.\nAll these actions run simultaneously from the first visible projected frame until the final frame, at normal playback speed, without a fade-in, opening pause, final freeze or settling back into the reference image. The supplied visual references fix architecture, identities and artwork appearance ONLY; replace their static or weak artwork motion with the explicit motion above. The original full projection is already on at frame zero or behind the closed door. All animated pixels bend at actual wall and ceiling seams, remain flat on those surfaces and are occluded by real foreground objects.",
    "reason": "Replace verbose weak-motion block with coordinated independent actions and architecture-relative travel."
  },
  {
    "from": "",
    "to": "PRIMARY REQUIREMENT: this is a continuously ANIMATED Christmas movie projected on real walls and ceiling. The sleigh travels, reindeer gallop and smoke actively billows from every illustrated house chimney. Most other existing illustrated subjects move too. A static decorative image behind moving children is a failed result. Apply the detailed PROJECTED FILM ACTION below at every instant; retain the existing camera and child choreography.",
    "reason": "User's primary correction is visible movement across most projected objects."
  }
]
```

## C07 - starting frame

**Frame:** `starting_frames/v12_c07_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** 93f65259-c58c-4b78-9144-e90159f52d8e
**Status:** Completed and saved locally; awaiting Daniel's review.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c07_g1.png` - b5910d54-c9bd-4be4-9ae3-3b870ad2e793 - role image (backend image_references)
2. `references/v12_c05_r1.png` - 16ec0091-87a5-4b00-9673-799570413b29 - role image (backend image_references)

Reused from v11 C07 take 1 - changed: New children and clothing: a boy of about five with light skin, freckles and tousled auburn hair; a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids; warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Room: a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved barrel vault and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Projection story: Snowy Christmas village. Architecture-specific mapping rewritten for those surfaces. Camera/pose, density, contrast, single-origin light and sharpness wording retained. C05/C07 share the new house and children.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the new room and children; it is the same house viewed from farther inside. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids; a boy of about five with light skin, freckles and tousled auburn hair. Both fully dressed in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved barrel vault and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. The same room and decor as @Image 2, seen from the middle of the great room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the muted cranberry wool rug, the cream boucle sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the surface texture of the fieldstone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The later animation request and exact submitted take are archived below.

### Take history
Take 1 only. Awaiting Daniel's review. No prior generation overwritten. No reroll.



### Video prompt - take 1

**Clip:** clips/v12_c07_g1.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 4, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "93f65259-c58c-4b78-9144-e90159f52d8e"}]}
**Job ID:** 28e20c13-6f51-4af8-bfb9-fbeed0a92ecf
**Status:** Completed, saved locally and added to the board; awaiting Daniel's review. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested 4s; audio stream present; 4422474 bytes.
**Sampled visual review:** Projection is fully visible on walls and ceiling from the opening sample. The children bounce and turn while the projected sleigh and other light elements move. One generation; awaiting review.
**References, in order:**
- {"role": "start_image", "value": "93f65259-c58c-4b78-9144-e90159f52d8e", "path": "starting_frames/v12_c07_g1.png"}
**Backend adjustments:** {}

Reused from v11 C07 video take 2 - scene nouns changed to the existing video 12 images. All unchanged source motion/camera/timing text preserved verbatim. C02 contains the requested new one-handed lift, carton-hand and original-artwork corrections; its video reference was removed. C05 uses the approved g4 camera continuity and this video own C07 moving room reference. Full exact changes follow.

```text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, cathedral ceiling panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected Christmas village picture is PLAYING across the back wall and the entire cathedral ceiling and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved cathedral ceiling and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with light skin, freckles and tousled auburn hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole cathedral ceiling. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, wall material and ceiling details and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster ceiling details, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny village children keep passing gifts beside the village and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, wall material and ceiling details. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the muted cranberry wool rug, the cream boucle sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the cathedral ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the cathedral ceiling or an un-animated ceiling detail in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

#### Exact source edits - in application order

1. Physical scene nouns adapted to the existing starting frame.

Before:
```text
ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the smooth cream barrel-vault ceiling crossed by three shallow plaster arch ribs, the cream plaster walls, the tall warm limestone chimney breast and carved mantel, the two tall rectangular black-framed windows on the left with night outside, the recessed arched doorway on the right, the lit Christmas tree and its presents, the large ivory linen sectional sofa wrapping the foreground, the rectangular upholstered ottoman, the deep-red Persian rug, the pale oak plank floor, the children and the colour.
```

After / added:
```text
ASSET ROLES: @Image 1 is frame 0.0s and controls a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved barrel vault and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.
```

2. Physical scene nouns adapted to the existing starting frame.

Before:
```text
THE SMALLER CHILD - a boy of about six with warm brown skin and close-cropped dark curls, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
```

After / added:
```text
THE SMALLER CHILD - a boy of about five with light skin, freckles and tousled auburn hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
```

3. Physical scene nouns adapted to the existing starting frame.

Before:
```text
THE OTHER CHILD - a girl of about nine with light freckled skin and long copper-red hair in a loose braid, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
```

After / added:
```text
THE OTHER CHILD - a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
```

4. Physical scene nouns adapted to the existing starting frame.

Before:
```text
Both in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks, so their knitted jumpers read clearly. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
```

After / added:
```text
Both in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
```

5. Physical scene nouns adapted to the existing starting frame.

Before:
```text
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.
```

After / added:
```text
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.
```

6. Physical scene nouns adapted to the existing starting frame.

Before:
```text
SURFACE MAPPING - the moving picture follows the real curve of the barrel vault, steps across each shallow arch rib with the proper offset and occlusion shadow, and bends at the projecting limestone chimney corners. The ceiling, arch ribs, stone and walls themselves never move.
```

After / added:
```text
SURFACE MAPPING - The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

7. Physical scene nouns adapted to the existing starting frame.

Before:
```text
the whole curved barrel-vault ceiling and its shallow plaster arch ribs
```

After / added:
```text
the entire cathedral ceiling and its architectural details
```

8. Physical scene nouns adapted to the existing starting frame.

Before:
```text
curved barrel-vault ceiling
```

After / added:
```text
cathedral ceiling
```

9. Physical scene nouns adapted to the existing starting frame.

Before:
```text
barrel-vault ceiling
```

After / added:
```text
cathedral ceiling
```

10. Physical scene nouns adapted to the existing starting frame.

Before:
```text
barrel vault
```

After / added:
```text
cathedral ceiling
```

11. Physical scene nouns adapted to the existing starting frame.

Before:
```text
arch ribs
```

After / added:
```text
ceiling details
```

12. Physical scene nouns adapted to the existing starting frame.

Before:
```text
arch rib
```

After / added:
```text
ceiling detail
```

13. Physical scene nouns adapted to the existing starting frame.

Before:
```text
limestone and cream
```

After / added:
```text
wall material and
```

14. Physical scene nouns adapted to the existing starting frame.

Before:
```text
ivory linen sectional sofa
```

After / added:
```text
cream boucle sectional sofa
```

15. Physical scene nouns adapted to the existing starting frame.

Before:
```text
deep-red Persian rug
```

After / added:
```text
muted cranberry wool rug
```

16. Physical scene nouns adapted to the existing starting frame.

Before:
```text
North Pole Christmas workshop
```

After / added:
```text
Christmas village
```

17. Animate corresponding objects already present in this video's Christmas artwork.

Before:
```text
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
```

After / added:
```text
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
```

18. Physical scene nouns adapted to the existing starting frame.

Before:
```text
toy train
```

After / added:
```text
gift wagon
```

19. Physical scene nouns adapted to the existing starting frame.

Before:
```text
the train advances
```

After / added:
```text
the gift wagon advances
```

20. Physical scene nouns adapted to the existing starting frame.

Before:
```text
tiny elves
```

After / added:
```text
tiny village children
```

21. Physical scene nouns adapted to the existing starting frame.

Before:
```text
elves
```

After / added:
```text
villagers
```

22. Physical scene nouns adapted to the existing starting frame.

Before:
```text
workshop
```

After / added:
```text
village
```

#### Animation take history
Take 1 completed, saved and added to board for review. No reroll. C01 is separate work and unchanged by this B-roll round.


### Video prompt - take 2 (user-requested correction)

**Clip:** clips/v12_c07_g2.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 4, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "93f65259-c58c-4b78-9144-e90159f52d8e"}, {"role": "image", "value": "93f65259-c58c-4b78-9144-e90159f52d8e"}]}
**Job ID:** 9f034c55-78c5-4c5f-8b19-deff820a4099
**Status:** Completed and added to board for review. One replacement generation; no automatic reroll.
**Output verification:** {"width": 720, "height": 1280, "duration": 4.041667, "frames": "97", "fps": "24/1", "audio": true, "bytes": 4651262, "review_sheet": "C:\\Users\\<user>\\AppData\\Local\\Temp\\v12_c07_g2_review.jpg"}
**Sampled visual review:** Take 2 sampled review: the girl lands farther inside the sofa and continues bouncing while the boy moves on the rug. The sofa back partly hides her foot contacts, so the exact landing placement still needs playback review. Projection is present from the opening and moving. One replacement; awaiting Daniel's review.
**References, in order:**
- {"role": "start_image", "value": "93f65259-c58c-4b78-9144-e90159f52d8e", "path": "starting_frames/v12_c07_g1.png"}
- {"role": "image", "value": "93f65259-c58c-4b78-9144-e90159f52d8e", "path": "starting_frames/v12_c07_g1.png", "purpose": "Same approved frame locks the already-projected look."}
**Backend adjustments:** {"medias[1].role": {"requested": "image", "used": "image_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v12 C07 video take 1 - only the requested motion correction and explicitly recorded supporting changes below. Same starting frame, model, resolution, duration and camera choreography.
**User review of take 1:** Rejected - Girl jumped awkwardly on the sofa edge.

```text
SOFA CONTACT CORRECTION: the girl's opening airborne position must lead naturally inward onto the broad interior seat cushion, never onto the thin sofa back or outer edge. All later take-offs and landings stay centred on that same flat cushion, with both feet supported and realistic weight. @Image 1 fixes the original opening geometry; @Image 2 is the same frame and fixes the room and projection appearance.

OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, cathedral ceiling panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected Christmas village picture is PLAYING across the back wall and the entire cathedral ceiling and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved cathedral ceiling and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with light skin, freckles and tousled auburn hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids. Preserve her airborne opening pose, then complete that jump with a small natural inward landing on the broad flat seat cushion INSIDE the sofa, beyond the near backrest. Both feet land fully supported near the cushion centre. She continues small vertical bounces over this same broad cushion centre with natural knee flexion, balanced arms and visible cushion compression. She never lands or balances on the narrow top of the backrest, armrest, cushion seam or outer edge. Keep normal anatomy and consistent limb proportions; no twisting legs, floating feet or furniture intersection.
Both in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole cathedral ceiling. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, wall material and ceiling details and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster ceiling details, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny village children keep passing gifts beside the village and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, wall material and ceiling details. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the muted cranberry wool rug, the cream boucle sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD completes the opening jump with an inward landing onto the centre of the broad seat cushion, both feet fully supported, knees absorbing the landing, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD makes a small balanced vertical bounce directly above that same broad seat-cushion centre and lands there on both feet, her knees bending naturally and the cushion compressing. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the cathedral ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the cathedral ceiling or an un-animated ceiling detail in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All physical walls, ceiling planes, beams, seams and trim remain stationary.
```

**Exact changes and reasons:**
```json
[
  {
    "from": "THE OTHER CHILD - a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.",
    "to": "THE OTHER CHILD - a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids. Preserve her airborne opening pose, then complete that jump with a small natural inward landing on the broad flat seat cushion INSIDE the sofa, beyond the near backrest. Both feet land fully supported near the cushion centre. She continues small vertical bounces over this same broad cushion centre with natural knee flexion, balanced arms and visible cushion compression. She never lands or balances on the narrow top of the backrest, armrest, cushion seam or outer edge. Keep normal anatomy and consistent limb proportions; no twisting legs, floating feet or furniture intersection.",
    "reason": "Move landing and bounces onto supported cushion centre."
  },
  {
    "from": "THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing.",
    "to": "THE OTHER CHILD completes the opening jump with an inward landing onto the centre of the broad seat cushion, both feet fully supported, knees absorbing the landing, laughing.",
    "reason": "Clear opening landing."
  },
  {
    "from": "THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back.",
    "to": "THE OTHER CHILD makes a small balanced vertical bounce directly above that same broad seat-cushion centre and lands there on both feet, her knees bending naturally and the cushion compressing.",
    "reason": "Avoid unstable edge jump."
  },
  {
    "from": "",
    "to": "SOFA CONTACT CORRECTION: the girl's opening airborne position must lead naturally inward onto the broad interior seat cushion, never onto the thin sofa back or outer edge. All later take-offs and landings stay centred on that same flat cushion, with both feet supported and realistic weight. @Image 1 fixes the original opening geometry; @Image 2 is the same frame and fixes the room and projection appearance.",
    "reason": "Prioritise user correction with original frame."
  }
]
```

## Results and review notes - verified 2026-09-21

- starting_frames/v12_c02_g1.png | job 48f89cec-1b88-4bf9-bf8a-78bd0711a977 | 1520x2688 | 6259228 bytes | SHA256 589d82f0f801123e30fe8f22b014c078ca331ebea5b37b104996b5b9353d195b
  Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135609_48f89cec-1b88-4bf9-bf8a-78bd0711a977.png
- starting_frames/v12_c03_g1.png | job 0ee1c12a-5989-4980-b36a-a7efd0ddefe1 | 1520x2688 | 5144817 bytes | SHA256 0c9fb3e153ce96d94b81a407e3df349479cf999bad866b05c5bee18a2ff70b08
  Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135607_0ee1c12a-5989-4980-b36a-a7efd0ddefe1.png
- starting_frames/v12_c04_g1.png | job 36021679-fd7f-46b5-bb2c-70929fdee825 | 1520x2688 | 5433194 bytes | SHA256 57a40fb8ec47651e244a7e2b580296ecdb8c1e18e53f0afa8e4e226c6d53f346
  Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135607_36021679-fd7f-46b5-bb2c-70929fdee825.png
- starting_frames/v12_c05_g1.png | job eb4c35e2-309e-446d-aff5-9ffd9d6c4ed6 | 1520x2688 | 5333863 bytes | SHA256 b3366023024033fb9f096a081f76cacacc8f10d975cb10bbea83b22bb7d4f61e
  Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135609_eb4c35e2-309e-446d-aff5-9ffd9d6c4ed6.png
- references/v12_c05_r1.png | job 16ec0091-87a5-4b00-9673-799570413b29 | 1520x2688 | 7627286 bytes | SHA256 84142dd5553a0a68e36e23197a75b8b9ea5d2cfaa08f0c05df61920f5f3e7ed4
  Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135610_16ec0091-87a5-4b00-9673-799570413b29.png
- starting_frames/v12_c06_g1.png | job ad7bddc8-13d6-46cb-9af2-439134e2db10 | 1520x2688 | 7265228 bytes | SHA256 0598cb8a7fc86b1a54ee7a42d9a0dbea0ea165f1bf21d330ef96ae3f5cd48edf
  Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135609_ad7bddc8-13d6-46cb-9af2-439134e2db10.png
- starting_frames/v12_c07_g1.png | job 93f65259-c58c-4b78-9144-e90159f52d8e | 1520x2688 | 7313423 bytes | SHA256 4840ed078725e3c9b1cfe4c6a1245d33e61526522c2d65ec5b093c02457615bf
  Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135812_93f65259-c58c-4b78-9144-e90159f52d8e.png

All seven service jobs completed. One submission per image; no retry or reroll. Every downloaded image was staged outside the product folder, copied and verified by byte count and SHA256. All images were visually inspected at board-thumbnail scale; full-resolution micro-detail was not independently certified. Awaiting Daniel's selection.

- C02: The box wordmark appears on both lid and front, as in the supplied references. One take, awaiting review.
- C03: Original lifted pose and mesh lens retained; new marble counter, powder-blue kitchen and red sleeves.
- C04: Original cable approach retained with the socket specified at the dome-body rim. New hands, counter and kitchen.
- C05: Navy door and snowy village reveal. Some chimney stone is less covered by projected imagery than requested. One take for each image; no reroll.
- C06: New child, green Christmas knitwear and asymmetrical attic ceiling; snowy village projection. One take, awaiting review.
- C07: Same new house and children as C05, using its generated room as a reference. Chimney stone remains less covered by the projection. No reroll.

Added as a review lane on the existing hand-edited video_board.html. No C01, clips or final export were generated for this round.


## C01 - Hook recreation - 2026-09-21

**Current status:** image generated, downloaded and inspected; awaiting Daniel's review. No animation requested until the image is approved. Existing B-roll records above remain unchanged.

**Frame:** `starting_frames/v12_c01_g1.png` (downloaded and verified)
**Clip:** not generated.
**Settings:** Higgsfield `gpt_image_2_5`, `variant=sunburst`, `resolution=2k`, `quality=medium`, `aspect_ratio=9:16`, `count=1`. The user explicitly requested these settings, overriding the older source model where different. `use_unlim` omitted. Both canonical `image` roles were mapped by the backend to `image_references`.
**Job ID:** `94808c0a-842c-454d-aeab-104f3b6a2381`
**References (in submitted order):**
1. `../video_9_assets/starting_frames/v9_c01_g8.png`, completed generation ID `443746c4-8eeb-4ff2-a4da-e02a14293714`: owns geometry, framing, camera, pose and prop placement; confirmed selected frame on video_board.html.
2. `../video_9_assets/starting_frames/v9_c01_g7.png`, completed generation ID `449ed0de-a806-4966-b15f-53bac6662a33`: photographic look only, natural iPhone sharpness and materials, not room or people.

Reused from v9 C01 g8 - changed: people and room nouns only, plus reference-role wording needed for the new reference pair. Camera, framing, pose and quality blocks copied from the archived source. Historical edit instructions naming the people in the old source were adapted to the current selected reference where necessary. Every exact replacement is listed below.

### Image prompt
```text
REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality candid vertical iPhone photo taken from a hallway looking into a family's living room on a winter evening: a young mother kneels on the bare floor with a huge tangled knot of old multicoloured Christmas string lights in front of her, her arm stretched out to push the plug into a wall socket, while her two small children stand behind her watching the Christmas tree.

Use the attached reference photograph for BOTH the staging AND the camera position - the mother kneeling in the near foreground, the knot of lights on the floor beside her, her arm reaching out to the low wall socket, the two small children standing behind her, the tall Christmas tree on the right and the plain white wall corner the camera is looking past. COPY ITS CAMERA POSITION AND ITS COMPOSITION EXACTLY. Copy nothing else from it: the room, the mother and the children are all described below and are all different people in a different house.

FRAMING AND ANGLE - COPY THE CAMERA FROM THE REFERENCE: the camera is handheld at about the chest height of a standing adult, tilted very slightly down, standing in the next room and looking in through a doorway, so a plain white wall corner with a white skirting board runs floor to ceiling down the RIGHT EDGE of the frame and takes up roughly the right eighth of the picture - we are looking past it into the living room. The living room floor fills the bottom half of the frame and runs away into depth. The mother kneels in the lower LEFT of the frame, seen from behind at three quarters, close to the camera and large in the picture: her head and shoulders sit around the middle of the frame and the bottom edge of the picture cuts her just below the knees. The knot of lights lies on the bare floor immediately to her right, between her and that white wall corner, around the centre of the lower third of the picture. The Christmas tree stands on the RIGHT of the frame just inside the white corner, tall enough that the top edge of the picture cuts off its top. The two children stand on the floor in the middle distance between the mother and the tree, small in the frame, their heads in the middle third of the picture. Nobody is looking at the camera and nobody is posing. This is NOT a side angle, NOT a low floor-level angle and NOT a symmetrical composition.

THE KNOT AND THE PLUG: on the bare floorboards immediately to the mother's right lies a big ugly knot of old-fashioned Christmas string lights - dark green flex wound and knotted into a messy nest about the width of two floorboards across, studded with fat vintage multicoloured bulbs in red, green, blue and yellow, with a white in-line plug body and loops of slack wire lifting out of the top of it. She holds the end of that flex in her outstretched right hand and the two-pin plug is an inch from a white electrical socket set low on the white wall corner at the right of the frame. It is not plugged in yet and every bulb in the knot is dark.

THE CONNECTION - THIS IS THE IMPORTANT PART: one single continuous run of that SAME dark green flex with the SAME fat multicoloured bulbs leaves the far side of the knot, travels away across the floorboards to the right, passes behind the children, reaches the foot of the Christmas tree and climbs up into its lower branches, where it is plainly the very same string that is wound round and round the whole tree above. Same wire colour, same bulb size, same bulb spacing, one unbroken line. The eye must be able to follow the wire from the plug in her hand, through the knot on the floor, across the floor and up onto the tree without a single break or gap. The heap on the floor is NOT a separate loose pile with nothing leading out of it, and the tree is NOT wired to anything else.

THE TREE IS NOT SWITCHED ON: because the plug is still in her hand, every bulb on the tree is dark and unlit. The tree is not glowing, no light comes off it, and it throws no coloured light onto the floor, the walls or the children. It is still fully decorated and still reads as a beautiful Christmas tree - the baubles catch the warm lamplight in the room - it is simply not lit yet.

THE ROOM: a cosy American traditional living room. Walls of pale blue-grey painted plaster with white skirting, wide honey-oak floorboards running away from the camera, a rust-red velvet sofa along the left wall with a cream wool blanket folded over its back, a cream and blue Persian rug on the floor in front of it, a walnut side table behind the sofa carrying a brass table lamp with a white linen shade that is switched on and glowing, and a white-painted window with white muntins on the back wall showing a dark blue winter evening and snow on the sill outside.

THE TREE: a big real fir, dense and dark green, dressed with silver, white and pale blue glass baubles, cream knitted snowflakes, a wide cream linen ribbon wound down it and a silver star on top, with a heavy cream cable-knit tree skirt gathered round its base and four presents wrapped in white paper and green ribbon sitting on it.

THE MOTHER: about 34, shoulder-length curly dark-brown hair, warm olive skin and an oval face, an oversized forest-green chunky cable-knit sweater with the sleeves pushed up her forearms, charcoal grey joggers and thick oatmeal socks, no shoes. She kneels sitting back on her heels, her left hand flat on the floorboards taking her weight, her right arm stretched right out towards the socket with the plug pinched between her thumb and fingers, her head turned in profile watching the plug. She is concentrating, slightly fed up, not smiling.

THE CHILDREN: a boy of about seven standing on the rug behind his mother, short curly auburn hair and a freckled face, red-and-white striped pyjamas, barefoot, his mouth wide open in a huge exaggerated gasp of amazement and both hands up near his cheeks, staring at the tree. Beside him a girl of about four with dark-brown hair in two short pigtails and warm olive skin, a cream flannel nightgown printed with tiny red hearts, crouched down on one knee with her right arm flung out pointing straight at the tree. Neither child blocks the mother, the knot of lights or the tree.

COLOUR: warm domestic evening white balance, the way an iPhone renders a lamp-lit living room - warm but not orange. The picture is NOT sepia, NOT amber-washed and NOT heavily graded. Skin reads natural, the white wall corner reads clean white, the floorboards read as real wood and the sweater reads as true forest green.

LIGHTING AND QUALITY: the room is lit by the warm table lamp plus soft ambient light - cosy and warm, but still bright enough that every face, every twist of wire in the knot and the whole tree are clearly readable, with no dark corners where detail disappears and no blown highlights. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot somebody took of their family, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere from the mother in the foreground to the tree behind her, crisp detail in every individual bulb and every twist of flex in the tangle, realistic skin, hair and knitwear texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

FRAMING: leave the upper LEFT of the image - roughly the top eighth of the frame on the wall side - as plain uncluttered wall, free of pictures, shelves, garland, hanging decorations and lettering, so a caption can sit there. Do not pull the camera back or shrink the mother to make that room.

No captions, no watermarks, no added lettering anywhere in the image, no writing on any clothing, no user-interface elements, no mute or speaker icons and no social-media overlays.
```

### Video prompt
Not submitted. Awaiting Daniel's image approval.

**Result (2026-09-21):** completed; 1520 x 2688 pixels, PNG, 6663342 bytes; MD5 88b973a47b67788bd8289878fde0b35c. One generation only. Source URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_152601_94808c0a-842c-454d-aeab-104f3b6a2381.png

**Visual check:** Kneeling mother, both children, right-side socket, floor tangle and wire toward the tree preserved. People, wall finish, sofa, lamp and flooring changed. Small bright points remain on the tree, similar to the source, despite the copied prompt requesting an unlit tree; flag for Daniel, no reroll.

### Take history
- `starting_frames/v12_c01_g1.png`: one submission, unreviewed. No automatic reroll.
- Source full prompt retrieved from the source prompts.md; dated traceability notes checked. Earlier unresolved takes were not used.

### What changed and why
The user requested an extremely similar hook with different people and a different room. A reference-role paragraph was prepended to prevent the look reference from changing geometry.

#### Change 1
Before:
```text
THE ROOM: a cosy American farmhouse living room. Walls of cream-white painted shiplap boards with white skirting, wide pale grey-washed pine floorboards running away from the camera, a deep navy-blue slipcovered sofa along the left wall with a mustard wool blanket folded over its back, a cream and charcoal flat-weave rug on the floor in front of it, an oak side table behind the sofa carrying a black ceramic table lamp with a white linen shade that is switched on and glowing, and a white-painted window with black muntins on the back wall showing a dark blue winter evening and snow on the sill outside.
```
After:
```text
THE ROOM: a cosy American traditional living room. Walls of pale blue-grey painted plaster with white skirting, wide honey-oak floorboards running away from the camera, a rust-red velvet sofa along the left wall with a cream wool blanket folded over its back, a cream and blue Persian rug on the floor in front of it, a walnut side table behind the sofa carrying a brass table lamp with a white linen shade that is switched on and glowing, and a white-painted window with white muntins on the back wall showing a dark blue winter evening and snow on the sill outside.
```

#### Change 2
Before:
```text
about 28, long wavy honey-blonde hair falling loose past her shoulders
```
After:
```text
about 34, shoulder-length curly dark-brown hair, warm olive skin and an oval face
```

#### Change 3
Before:
```text
straight light-brown hair
```
After:
```text
short curly auburn hair and a freckled face
```

#### Change 4
Before:
```text
blonde hair in two short pigtails
```
After:
```text
dark-brown hair in two short pigtails and warm olive skin
```


### C01 animation - take 1 - 2026-09-21

**Status:** completed and saved; awaiting Daniel's review. Daniel approved all four starting frames in this conversation and requested the same animation as the corresponding source, Seedance 2.5, 1080p. One generation per shot.
**Frame:** `starting_frames/v12_c01_g1.png` - approved.
**Clip:** `clips/v12_c01_g1.mp4` (downloaded and verified).
**Job ID:** `88e284a9-c94a-488c-ad48-8bd3d61a7fd3`
**Settings:** `seedance_2_5`, `mode=omni_reference`, `resolution=1080p`, `duration=5`, `aspect_ratio=9:16`, `generate_audio=true`, `count=1`, `use_unlim=false`, `declined_preset_id=24bae836-2c4a-48e0-89b6-49fcc0b21612`. Other model defaults unchanged.
**References:** approved frame `starting_frames/v12_c01_g1.png`, image generation job `94808c0a-842c-454d-aeab-104f3b6a2381`, role `start_image`, the only attached media, matching the source's attachment strategy. No source video attached.
**Source:** `../video_9_assets/prompts.md`, C01 video take g6; selected clip `../video_9_assets/clips/v9_c01_g6.mp4`, source generation `be1f5aac-9f99-4dd8-bdab-d20b8f9607bf`, verified against the existing board. Source prompt and settings retrieved directly from the archive, including dated traceability notes.

Reused from v9 C01 g6 - changed: only appearance and room nouns to match the approved frame; exact substitutions below. Motion, camera, pacing, beat timing, audio and bans unchanged. Original duration and settings retained.

- `a blonde mother` -> `a dark-haired mother`
- `pale wooden floorboards` -> `honey-oak wooden floorboards`
- `navy sofa` -> `rust-red sofa`
- `cream shiplap walls` -> `pale blue-grey plaster walls`
- `shiplap walls` -> `plaster walls`
- `mustard blanket` -> `cream blanket`
- `pale floorboards` -> `honey-oak floorboards`

#### Video prompt
```text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, hyperrealistic. No cuts, no zoom, no slow motion, no speed ramp. The camera itself IS the phone being held by a man standing in the hallway doorway, so we see ONLY what he sees. No phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no device and no object ever appears in the foreground or along any edge of the frame.

Start frame: a dark-haired mother in a forest-green cable-knit sweater kneels on honey-oak wooden floorboards in the lower left, her right arm stretched out to a white wall socket on the white corner at the right of the frame, holding the plug of a big tangled knot of unlit multicoloured Christmas string lights that lies on the floor beside her. One continuous run of that same string leads away across the floor and up into the decorated but unlit Christmas tree standing on the right. A boy in red-and-white striped pyjamas and a small girl in a cream nightgown stand behind her near the rust-red sofa.

ACTION TIMELINE:
0.0-0.8s - The mother pushes the plug the last few centimetres into the socket. Her hand moves slowly and steadily, her head still turned in profile watching it. Everything else in the room is calm and still. The tree is dark. The camera is locked where it stands in the start frame, only natural handheld sway.

AT 0.8s - ONE SINGLE INSTANT, AND EVERYTHING IN IT HAPPENS ON THE SAME FRAME. The two pins seat in the socket; every bulb on the knot and on the tree flashes on for a split second; and in that same instant a burst of orange flame erupts low in the Christmas tree where the string meets the branches and the tree catches fire. On that exact same frame the man holding the camera shouts "Oh, shoot" and the whole frame jolts as he flinches backwards. The fire is not delayed, it does not build up, it does not start small and grow for a second first - the tree is already burning on the same frame the plug goes in.

0.8-2.0s - The flames climb the tree fast and realistically, running up through the dry branches, orange and yellow, throwing real flickering firelight across the plaster walls, the floorboards, the sofa and the three faces, with dark smoke rolling up off the top of the tree toward the ceiling. Ornaments glow and the branches blacken. The mother recoils hard away from the socket, twists round onto her hands and pushes herself up off the floor. The boy and the girl scream and turn toward the camera. The man with the camera takes ONLY TWO OR THREE SHORT STEPS BACKWARDS and then stops and stands his ground. That small retreat is finished by about 1.6s. He does not walk backwards down the hallway, he does not run, he does not retreat any further at any later point in the clip.

2.0-5.0s - The camera is now STANDING STILL in the hallway just behind the doorway, holding its position with only natural handheld sway, not moving backwards at all. The mother is on her feet and runs straight toward the camera with her arms out, scooping the two children ahead of her, all three sprinting toward the lens and growing rapidly larger in the frame, faces wide with panic, the boy's arms pumping, the little girl half carried. Because the camera is no longer backing away, they close the distance fast and come right up to the lens. End frame: the three of them very close and very large in the frame mid-run, almost filling it, the burning tree bright behind them through the doorway.

AUDIO: natural room sound only. One male voice, off camera behind the lens, shouting "Oh, shoot" exactly on the frame the tree catches fire - nothing else from him before it, nothing else after it. Then the crackle and roar of the fire, the mother shouting wordlessly, the two children screaming, bare feet running on wood. NO music, no score, no background song, no narration, no added sound effects beyond these.

REALISM - HARD RULES: the mother, the boy and the girl keep exactly the same faces, hair, clothes and body shapes as the start frame throughout. The room stays the same room - same pale blue-grey plaster walls, same rust-red sofa with the cream blanket, same honey-oak floorboards, same rug, same lamp, same window. The fire behaves like real fire on a real dry conifer: it spreads along branches, it does not float, it does not appear as a glowing overlay, it casts real moving light and real shadows on every surface, and it produces real dark smoke. Real phone-camera look with slight sensor noise and natural motion blur only from the handheld movement. No text overlays, no captions, no watermark, no on-screen graphics.

POSITIVE LOCKS: one continuous take from 0.0s to 5.0s with no cut anywhere. Everything plays at real-time speed. The camera never zooms. The ONLY camera movement in the entire clip is a short backwards flinch of two or three steps between 0.8s and 1.6s; before 0.8s the camera holds its start-frame position and after 1.6s the camera holds its new position and stays there until the end. BANNED: the camera walking or running backwards down the hallway, the camera retreating for more than three steps, the camera moving away from the family during their run, the family staying the same size in the frame as they run. Nobody stops moving once the fire starts.
```

#### Take history
`clips/v12_c01_g1.mp4`: generated once, saved, awaiting Daniel's review. No automatic reroll. No upscale requested.


**Result:** completed; 1080x1920, 5.050000s, 24/1 fps, hevc video, aac audio; 6158311 bytes; MD5 57f3db2fb2df4fae80fe33d2eb497476. Temporary download and final file sizes/hashes matched. Full video/audio decode exit 0. Service-returned prompt matches the submitted and archived prompt exactly.
**Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_153741_88e284a9-c94a-488c-ad48-8bd3d61a7fd3.mp4
**Visual check:** Sampled frames show plugging in, lights flashing, the tree igniting, a short camera retreat and the mother and both children approaching the lens. Ignition occurs later than the written 0.8s cue, similar to the recorded source delay. Kept for Daniel's review; no reroll.
**Review limits:** sampled visual frames inspected; audio stream presence and decoding verified, spoken wording not independently checked.


**Daniel's C01 review (2026-09-21):** clips/v12_c01_g1.mp4 approved in conversation ('They all camed out good'; only video 11 requested for regeneration). No changes to this clip.

## Upscaled derivatives — 2026-09-22

**Shared settings:** ByteDance Upscale, model version `Pro`, resolution `2K`, FPS `30 fps`. C01 used preset `AIGC`; C02-C07 used preset `Common`.

- `clips/upscaled/v12_c01_g1.mp4` from `clips/v12_c01_g1.mp4`; upscale job `video-job--4fccd581-6c16-4ebb-8005-a5a5102d4d46`; preset `AIGC`.
- `clips/upscaled/v12_c02_g1.mp4` from `clips/v12_c02_g1.mp4`; upscale job `video-job--8a81c700-12e6-4d63-aef9-aae3038d1966`; preset `Common`.
- `clips/upscaled/v12_c03_g1.mp4` from `clips/v12_c03_g1.mp4`; upscale job `video-job--a21b62f0-a18c-46cf-8e8f-d9427b51812f`; preset `Common`.
- `clips/upscaled/v12_c04_g1.mp4` from `clips/v12_c04_g1.mp4`; upscale job `video-job--b784d92d-7fe8-4164-9c1d-be2f36490e7a`; preset `Common`.
- `clips/upscaled/v12_c05_g1.mp4` from `clips/v12_c05_g1.mp4`; upscale job `video-job--a8a1d1ed-fc04-4f1e-879a-82d99ce4a95e`; preset `Common`.
- `clips/upscaled/v12_c06_g5.mp4` from `clips/v12_c06_g5.mp4`; upscale job `video-job--5d82b3b6-e0ca-4b93-8cc1-8aab476fadb3`; preset `Common`.
- `clips/upscaled/v12_c07_g2.mp4` from `clips/v12_c07_g2.mp4`; upscale job `video-job--20700436-d733-4c13-8518-9a9c79d9dc75`; preset `Common`.


---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

### C01 — Plug in the lights → tree fire

**In the cut:** `starting_frames/v12_c01_g1.png` → `clips/v12_c01_g1.mp4`

#### Image prompt — `starting_frames/v12_c01_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `94808c0a-842c-454d-aeab-104f3b6a2381`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_152601_94808c0a-842c-454d-aeab-104f3b6a2381.png
**References, in submission order**
- @Image 1: `content/video_9_assets/starting_frames/v9_c01_g8.png` · Higgsfield media `443746c4-8eeb-4ff2-a4da-e02a14293714`
- @Image 2: `content/video_9_assets/starting_frames/v9_c01_g7.png` · Higgsfield media `449ed0de-a806-4966-b15f-53bac6662a33`

````text
REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality candid vertical iPhone photo taken from a hallway looking into a family's living room on a winter evening: a young mother kneels on the bare floor with a huge tangled knot of old multicoloured Christmas string lights in front of her, her arm stretched out to push the plug into a wall socket, while her two small children stand behind her watching the Christmas tree.

Use the attached reference photograph for BOTH the staging AND the camera position - the mother kneeling in the near foreground, the knot of lights on the floor beside her, her arm reaching out to the low wall socket, the two small children standing behind her, the tall Christmas tree on the right and the plain white wall corner the camera is looking past. COPY ITS CAMERA POSITION AND ITS COMPOSITION EXACTLY. Copy nothing else from it: the room, the mother and the children are all described below and are all different people in a different house.

FRAMING AND ANGLE - COPY THE CAMERA FROM THE REFERENCE: the camera is handheld at about the chest height of a standing adult, tilted very slightly down, standing in the next room and looking in through a doorway, so a plain white wall corner with a white skirting board runs floor to ceiling down the RIGHT EDGE of the frame and takes up roughly the right eighth of the picture - we are looking past it into the living room. The living room floor fills the bottom half of the frame and runs away into depth. The mother kneels in the lower LEFT of the frame, seen from behind at three quarters, close to the camera and large in the picture: her head and shoulders sit around the middle of the frame and the bottom edge of the picture cuts her just below the knees. The knot of lights lies on the bare floor immediately to her right, between her and that white wall corner, around the centre of the lower third of the picture. The Christmas tree stands on the RIGHT of the frame just inside the white corner, tall enough that the top edge of the picture cuts off its top. The two children stand on the floor in the middle distance between the mother and the tree, small in the frame, their heads in the middle third of the picture. Nobody is looking at the camera and nobody is posing. This is NOT a side angle, NOT a low floor-level angle and NOT a symmetrical composition.

THE KNOT AND THE PLUG: on the bare floorboards immediately to the mother's right lies a big ugly knot of old-fashioned Christmas string lights - dark green flex wound and knotted into a messy nest about the width of two floorboards across, studded with fat vintage multicoloured bulbs in red, green, blue and yellow, with a white in-line plug body and loops of slack wire lifting out of the top of it. She holds the end of that flex in her outstretched right hand and the two-pin plug is an inch from a white electrical socket set low on the white wall corner at the right of the frame. It is not plugged in yet and every bulb in the knot is dark.

THE CONNECTION - THIS IS THE IMPORTANT PART: one single continuous run of that SAME dark green flex with the SAME fat multicoloured bulbs leaves the far side of the knot, travels away across the floorboards to the right, passes behind the children, reaches the foot of the Christmas tree and climbs up into its lower branches, where it is plainly the very same string that is wound round and round the whole tree above. Same wire colour, same bulb size, same bulb spacing, one unbroken line. The eye must be able to follow the wire from the plug in her hand, through the knot on the floor, across the floor and up onto the tree without a single break or gap. The heap on the floor is NOT a separate loose pile with nothing leading out of it, and the tree is NOT wired to anything else.

THE TREE IS NOT SWITCHED ON: because the plug is still in her hand, every bulb on the tree is dark and unlit. The tree is not glowing, no light comes off it, and it throws no coloured light onto the floor, the walls or the children. It is still fully decorated and still reads as a beautiful Christmas tree - the baubles catch the warm lamplight in the room - it is simply not lit yet.

THE ROOM: a cosy American traditional living room. Walls of pale blue-grey painted plaster with white skirting, wide honey-oak floorboards running away from the camera, a rust-red velvet sofa along the left wall with a cream wool blanket folded over its back, a cream and blue Persian rug on the floor in front of it, a walnut side table behind the sofa carrying a brass table lamp with a white linen shade that is switched on and glowing, and a white-painted window with white muntins on the back wall showing a dark blue winter evening and snow on the sill outside.

THE TREE: a big real fir, dense and dark green, dressed with silver, white and pale blue glass baubles, cream knitted snowflakes, a wide cream linen ribbon wound down it and a silver star on top, with a heavy cream cable-knit tree skirt gathered round its base and four presents wrapped in white paper and green ribbon sitting on it.

THE MOTHER: about 34, shoulder-length curly dark-brown hair, warm olive skin and an oval face, an oversized forest-green chunky cable-knit sweater with the sleeves pushed up her forearms, charcoal grey joggers and thick oatmeal socks, no shoes. She kneels sitting back on her heels, her left hand flat on the floorboards taking her weight, her right arm stretched right out towards the socket with the plug pinched between her thumb and fingers, her head turned in profile watching the plug. She is concentrating, slightly fed up, not smiling.

THE CHILDREN: a boy of about seven standing on the rug behind his mother, short curly auburn hair and a freckled face, red-and-white striped pyjamas, barefoot, his mouth wide open in a huge exaggerated gasp of amazement and both hands up near his cheeks, staring at the tree. Beside him a girl of about four with dark-brown hair in two short pigtails and warm olive skin, a cream flannel nightgown printed with tiny red hearts, crouched down on one knee with her right arm flung out pointing straight at the tree. Neither child blocks the mother, the knot of lights or the tree.

COLOUR: warm domestic evening white balance, the way an iPhone renders a lamp-lit living room - warm but not orange. The picture is NOT sepia, NOT amber-washed and NOT heavily graded. Skin reads natural, the white wall corner reads clean white, the floorboards read as real wood and the sweater reads as true forest green.

LIGHTING AND QUALITY: the room is lit by the warm table lamp plus soft ambient light - cosy and warm, but still bright enough that every face, every twist of wire in the knot and the whole tree are clearly readable, with no dark corners where detail disappears and no blown highlights. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot somebody took of their family, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere from the mother in the foreground to the tree behind her, crisp detail in every individual bulb and every twist of flex in the tangle, realistic skin, hair and knitwear texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

FRAMING: leave the upper LEFT of the image - roughly the top eighth of the frame on the wall side - as plain uncluttered wall, free of pictures, shelves, garland, hanging decorations and lettering, so a caption can sit there. Do not pull the camera back or shrink the mother to make that room.

No captions, no watermarks, no added lettering anywhere in the image, no writing on any clothing, no user-interface elements, no mute or speaker icons and no social-media overlays.
````

#### Video prompt — `clips/v12_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `88e284a9-c94a-488c-ad48-8bd3d61a7fd3`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_153741_88e284a9-c94a-488c-ad48-8bd3d61a7fd3.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v12_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c01_g1.png` · Higgsfield media `94808c0a-842c-454d-aeab-104f3b6a2381`

````text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, hyperrealistic. No cuts, no zoom, no slow motion, no speed ramp. The camera itself IS the phone being held by a man standing in the hallway doorway, so we see ONLY what he sees. No phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no device and no object ever appears in the foreground or along any edge of the frame.

Start frame: a dark-haired mother in a forest-green cable-knit sweater kneels on honey-oak wooden floorboards in the lower left, her right arm stretched out to a white wall socket on the white corner at the right of the frame, holding the plug of a big tangled knot of unlit multicoloured Christmas string lights that lies on the floor beside her. One continuous run of that same string leads away across the floor and up into the decorated but unlit Christmas tree standing on the right. A boy in red-and-white striped pyjamas and a small girl in a cream nightgown stand behind her near the rust-red sofa.

ACTION TIMELINE:
0.0-0.8s - The mother pushes the plug the last few centimetres into the socket. Her hand moves slowly and steadily, her head still turned in profile watching it. Everything else in the room is calm and still. The tree is dark. The camera is locked where it stands in the start frame, only natural handheld sway.

AT 0.8s - ONE SINGLE INSTANT, AND EVERYTHING IN IT HAPPENS ON THE SAME FRAME. The two pins seat in the socket; every bulb on the knot and on the tree flashes on for a split second; and in that same instant a burst of orange flame erupts low in the Christmas tree where the string meets the branches and the tree catches fire. On that exact same frame the man holding the camera shouts "Oh, shoot" and the whole frame jolts as he flinches backwards. The fire is not delayed, it does not build up, it does not start small and grow for a second first - the tree is already burning on the same frame the plug goes in.

0.8-2.0s - The flames climb the tree fast and realistically, running up through the dry branches, orange and yellow, throwing real flickering firelight across the plaster walls, the floorboards, the sofa and the three faces, with dark smoke rolling up off the top of the tree toward the ceiling. Ornaments glow and the branches blacken. The mother recoils hard away from the socket, twists round onto her hands and pushes herself up off the floor. The boy and the girl scream and turn toward the camera. The man with the camera takes ONLY TWO OR THREE SHORT STEPS BACKWARDS and then stops and stands his ground. That small retreat is finished by about 1.6s. He does not walk backwards down the hallway, he does not run, he does not retreat any further at any later point in the clip.

2.0-5.0s - The camera is now STANDING STILL in the hallway just behind the doorway, holding its position with only natural handheld sway, not moving backwards at all. The mother is on her feet and runs straight toward the camera with her arms out, scooping the two children ahead of her, all three sprinting toward the lens and growing rapidly larger in the frame, faces wide with panic, the boy's arms pumping, the little girl half carried. Because the camera is no longer backing away, they close the distance fast and come right up to the lens. End frame: the three of them very close and very large in the frame mid-run, almost filling it, the burning tree bright behind them through the doorway.

AUDIO: natural room sound only. One male voice, off camera behind the lens, shouting "Oh, shoot" exactly on the frame the tree catches fire - nothing else from him before it, nothing else after it. Then the crackle and roar of the fire, the mother shouting wordlessly, the two children screaming, bare feet running on wood. NO music, no score, no background song, no narration, no added sound effects beyond these.

REALISM - HARD RULES: the mother, the boy and the girl keep exactly the same faces, hair, clothes and body shapes as the start frame throughout. The room stays the same room - same pale blue-grey plaster walls, same rust-red sofa with the cream blanket, same honey-oak floorboards, same rug, same lamp, same window. The fire behaves like real fire on a real dry conifer: it spreads along branches, it does not float, it does not appear as a glowing overlay, it casts real moving light and real shadows on every surface, and it produces real dark smoke. Real phone-camera look with slight sensor noise and natural motion blur only from the handheld movement. No text overlays, no captions, no watermark, no on-screen graphics.

POSITIVE LOCKS: one continuous take from 0.0s to 5.0s with no cut anywhere. Everything plays at real-time speed. The camera never zooms. The ONLY camera movement in the entire clip is a short backwards flinch of two or three steps between 0.8s and 1.6s; before 0.8s the camera holds its start-frame position and after 1.6s the camera holds its new position and stays there until the end. BANNED: the camera walking or running backwards down the hallway, the camera retreating for more than three steps, the camera moving away from the family during their run, the family staying the same size in the frame as they run. Nobody stops moving once the fire starts.
````

### C02 — Hands on the box

**In the cut:** `starting_frames/v12_c02_g1.png` → `clips/v12_c02_g1.mp4`

#### Image prompt — `starting_frames/v12_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `48f89cec-1b88-4bf9-bf8a-78bd0711a977`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135609_48f89cec-1b88-4bf9-bf8a-78bd0711a977.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c02_g1.png` · Higgsfield media `bbfc652c-e9eb-4430-9b53-610b56917312`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 29, with fair freckled skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a cranberry-red ribbed wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a warmly lit Georgian Christmas dining room with powder-blue walls, white panel mouldings, a carved white fireplace with cranberry stockings, a dark mahogany sideboard, and a decorated fir tree with red tartan ribbons and warm gold lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v12_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `89534e88-5a63-46cd-bdbc-2abf89bffd40`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_183537_89534e88-5a63-46cd-bdbc-2abf89bffd40.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v12_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c02_g1.png` · Higgsfield media `48f89cec-1b88-4bf9-bf8a-78bd0711a977`
- image ref 1: `content/video_12_assets/starting_frames/v12_c02_g1.png` · Higgsfield media `48f89cec-1b88-4bf9-bf8a-78bd0711a977`

````text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a cranberry-red ribbed wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a warmly lit Georgian Christmas dining room with powder-blue walls, white panel mouldings, a carved white fireplace with cranberry stockings, a dark mahogany sideboard, and a decorated fir tree with red tartan ribbons and warm gold lights. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the dark smoked-walnut dining table with long straight chocolate-brown grain, a dead-matte finish and a clean square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
````

### C03 — The projector lifted

**In the cut:** `starting_frames/v12_c03_g1.png` → `clips/v12_c03_g1.mp4`

#### Image prompt — `starting_frames/v12_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `0ee1c12a-5989-4980-b36a-a7efd0ddefe1`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135607_0ee1c12a-5989-4980-b36a-a7efd0ddefe1.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c03_g1.png` · Higgsfield media `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`
- @Image 2: `content/video_10_assets/starting_frames/v10_c03_g1.png` · Higgsfield media `89ed549a-35bb-4e66-8865-c5a112bc239a`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 29, with fair freckled skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a cranberry-red ribbed wool sweater sleeve pushed back; right forearm enters from the right in the same cranberry-red ribbed wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v12_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `fb519a5f-f70d-40f1-bb13-356c7e92bb7d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_183537_fb519a5f-f70d-40f1-bb13-356c7e92bb7d.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v12_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c03_g1.png` · Higgsfield media `0ee1c12a-5989-4980-b36a-a7efd0ddefe1`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in cranberry-red ribbed wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge; behind it powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
````

### C04 — The cable going in

**In the cut:** `starting_frames/v12_c04_g1.png` → `clips/v12_c04_g1.mp4`

#### Image prompt — `starting_frames/v12_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `36021679-fd7f-46b5-bb2c-70929fdee825`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135607_36021679-fd7f-46b5-bb2c-70929fdee825.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c04_g1.png` · Higgsfield media `e243effc-2c21-4bed-9551-e592483315ca`
- @Image 2: `content/video_10_assets/starting_frames/v10_c04_g1.png` · Higgsfield media `1d69a04c-84ad-4a97-8d55-d5ce334848c1`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 29, with fair freckled skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a cranberry-red ribbed wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v12_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `3eab3881-bde4-4e25-8123-1edb15476884`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_183537_3eab3881-bde4-4e25-8123-1edb15476884.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v12_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c04_g1.png` · Higgsfield media `36021679-fd7f-46b5-bb2c-70929fdee825`

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
THE LEFT HAND - a woman's hand in a cranberry-red ribbed wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same cranberry-red ribbed wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a white Carrara marble counter with fine feathery cool-grey veining and a satin-honed surface, straight square edge; behind it powder-blue shaker cabinets with warm brass knobs, narrow ivory vertical tiles, a brushed stainless-steel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the stone and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the stone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
````

### C05 — The door opens on the room

**In the cut:** `starting_frames/v12_c05_g1.png`, `references/v12_c05_r1.png` → `clips/v12_c05_g1.mp4`

#### Image prompt — `starting_frames/v12_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `eb4c35e2-309e-446d-aff5-9ffd9d6c4ed6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135609_eb4c35e2-309e-446d-aff5-9ffd9d6c4ed6.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- @Image 2: `content/video_10_assets/starting_frames/v10_c05_g1.png` · Higgsfield media `c301edff-f38f-42fc-bdde-d914d68ab37d`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the cranberry-red ribbed wool sleeve and no jewellery, with fair freckled skin, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a midnight-navy painted two-panel door, one large recessed rectangular upper panel and one smaller lower panel, satin finish and delicate brush texture, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the midnight-navy paint reads clearly as deep blue rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Image prompt — `references/v12_c05_r1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `16ec0091-87a5-4b00-9673-799570413b29`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135610_16ec0091-87a5-4b00-9673-799570413b29.png
**References, in submission order**
- @Image 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`
- @Image 2: `content/video_9_assets/references/v9_c05_r4.png` · Higgsfield media `1c500339-2855-45b6-bd9b-4c3633b5a272`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about five with light skin, freckles and tousled auburn hair; the girl is of about eight with warm tan skin and straight dark-brown hair in two loose braids. Both children are fully dressed for winter in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved barrel vault and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Seen from the doorway; the new a midnight-navy painted two-panel door, one large recessed rectangular upper panel and one smaller lower panel, satin finish and delicate brush texture is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the muted cranberry wool rug, the cream boucle sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the surface texture of the fieldstone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v12_c05_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `232c05ca-ad58-48be-86ea-c2521722f045`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_184208_232c05ca-ad58-48be-86ea-c2521722f045.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v12_c05_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c05_g1.png` · Higgsfield media `eb4c35e2-309e-446d-aff5-9ffd9d6c4ed6`
- video ref 1: `content/video_12_assets/clips/v12_c07_g1.mp4` — earlier generated clip · Higgsfield media `28e20c13-6f51-4af8-bfb9-fbeed0a92ecf`

````text
CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.

CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the cathedral ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the gift wagon travels and the villagers work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a midnight-navy painted two-panel door, one large recessed rectangular upper panel and one smaller lower panel, satin finish and delicate brush texture fully closed with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, cathedral ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Inside the flat projected North Pole village picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny village children keep carrying and passing wrapped gifts beside the village, shooting stars streak and fade, the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit village windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the actual room surfaces. The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole cathedral ceiling and over every ceiling seam, right into all four corners. No bare un-animated patch of plaster and no bare ceiling detail anywhere in the closing framing.

BEATS
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera advances slowly through the doorway while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the gift wagon and the villagers keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl with warm tan skin and straight dark-brown hair in two loose braids runs a broad curving path across the rug and alongside the sofa; the boy with light skin, freckles and tousled auburn hair follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole cathedral ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, chimney surface and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and ceiling details. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.

ROOM AND IDENTITY - a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved cathedral ceiling and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. The children are a boy of about five with light skin, freckles and tousled auburn hair and a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Preserve these identities and this architecture from @Video 1.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v12_c06_g1.png` → `clips/v12_c06_g5.mp4`

#### Image prompt — `starting_frames/v12_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `ad7bddc8-13d6-46cb-9af2-439134e2db10`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135609_ad7bddc8-13d6-46cb-9af2-439134e2db10.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c06_g1.png` · Higgsfield media `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`
- @Image 2: `content/video_9_assets/starting_frames/v9_c06_g4.png` · Higgsfield media `480dee42-d78d-4dd4-b3b0-cca1aed16477`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about five with light skin, freckles and tousled auburn hair, fully dressed for winter in a warm forest-green and cream knitted Christmas jumper with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed has a cream wool duvet with red tartan throw, pillows and a knitted stocking. A small real Christmas tree with gold lights and red ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v12_c06_g5.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `95aedab1-cd54-41ed-9d14-400a8fb6c376`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_221510_95aedab1-cd54-41ed-9d14-400a8fb6c376.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v12_c06_g5.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`
- image ref 1: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`

````text
PRIMARY REQUIREMENT: this is a continuously ANIMATED Christmas movie projected on real walls and ceiling. The sleigh travels, reindeer gallop and smoke actively billows from every illustrated house chimney. Most other existing illustrated subjects move too. A static decorative image behind moving children is a failed result. Apply the detailed PROJECTED FILM ACTION below at every instant; retain the existing camera and child choreography.

REAL-TIME SPEED - PRIMARY CORRECTION: this is an ordinary phone recording played at exactly 1x speed, never slow motion or high-frame-rate footage played back slowly. The boy makes five to six small lively mattress bounces across the five-second clip, roughly one complete bounce every 0.8-1.0 second. Each bounce has a quick knee bend, brief push-off, only about 0.3 second in the air, a prompt gravity-driven landing and immediate rebound. No long hang-time, suspended pose, languid arm swing, frozen apex, speed ramp or time stretching. He is already bouncing at frame zero and continues at the same natural cadence through the last frame. The camera's gentle movement is independent of the child's brisk normal-speed movement and must never slow him down. All projection motion also runs continuously at normal playback speed. Preserve the corrected lower opening and already complete ceiling coverage.

OPENING FRAMING AND COVERAGE - PRIMARY CORRECTION: use the approved starting image itself as the exact first camera frame, not merely a room reference. The camera must not begin tilted upward, close to the ceiling or above the supplied viewpoint. Show the whole jumping boy, full bed and foot bench from frame zero in the same composition as @Image 1. Every visible flat ceiling panel AND every visible sloping ceiling panel already carries the dense Christmas artwork at full brightness. Do not invent a new pale foreground ceiling, soffit, overhang or blank triangular panel. The camera does not reveal any extra unprojected space above the source framing. The full projection is already playing before filming and never fades in. Keep the same starting frame and existing physical room; correct the camera angle, not the architecture.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

PROJECTED FILM ACTION - THE MAIN SUBJECT IS THE MOVING CHRISTMAS ARTWORK. Animate the existing illustrated objects themselves, not just the camera, children, brightness or glitter. At every moment MOST visible illustrated subjects are visibly changing position or shape independently. Keep the physical room and the projection's overall footprint fixed.
SLEIGH AND REINDEER: the existing sleigh team travels along the plaster ceiling at roughly one fifth of the visible ceiling width per second, crossing architectural seams and passing the fixed central star. Every reindeer continuously cycles its legs in a running gallop; heads bob, harnesses flex and the sleigh rocks behind them. The team must move relative to the stationary beams, star and ceiling corners in every half-second interval. Do not rotate the ceiling picture as a single disc.
CHIMNEYS: each visible illustrated house chimney continuously emits a clearly visible cream-grey animated smoke plume, contained INSIDE the flat wall illustration. New curls emerge every 0.25 second, rise one roof-height per second, expand and deform, then dissolve as more curls follow. Several different plumes must be visibly evolving at once; none may remain a frozen drawn squiggle. These are moving pixels on the wall, never real smoke entering the room.
VILLAGE: the existing illustrated figures walk along the wall, take full alternating steps and swing arms. Gift carriers lift and pass the existing parcels. Existing animal drawings walk with articulating legs, toy processions advance and wheels turn where present. Existing house-window light flickers independently. Buildings stay fixed so the moving figures and chimney smoke read clearly.
RIBBONS, GARLANDS AND BELLS: successive waves visibly deform each existing ribbon along its length while bright gold crests travel from the central star toward the walls, covering half a ribbon length per second. Existing bell drawings swing left-right-left roughly once per second with independently swinging clappers. Existing ornament drawings rotate within the projected picture. Do not leave the wall decorations frozen while only the ceiling sleigh moves.
SNOW AND STARS: existing snowflake drawings translate along the ceiling planes and down the walls continuously, at different speeds. Ceiling snow stays flush to ceiling plaster and follows its slope, never drops into the air. Stars twinkle independently while existing shooting-star streaks traverse the surface. Nothing moves over the boy or children, furniture, floor or in the open room.
All these actions run simultaneously from the first visible projected frame until the final frame, at normal playback speed, without a fade-in, opening pause, final freeze or settling back into the reference image. The supplied visual references fix architecture, identities and artwork appearance ONLY; replace their static or weak artwork motion with the explicit motion above. The original full projection is already on at frame zero or behind the closed door. All animated pixels bend at actual wall and ceiling seams, remain flat on those surfaces and are occluded by real foreground objects.

TIMELINE - START AT THE SUPPLIED IMAGE'S EXISTING LOWER COMPOSITION, then make a very small downward tilt followed by a gentle physical pull back. Never re-aim upward before frame zero.
0.0-2.2s the camera begins at EXACTLY @Image 1's angle and framing: the boy's whole body and the full mattress are clearly visible around the middle and lower half, with the foot-of-bed bench and floor visible below, while the already projected wall and ceiling occupy the upper half. Do not start above this framing or crop the boy at the bottom. From this exact view, tilt downward only about 3 degrees in one slow steady move, retaining the fully projected ceiling in the upper part of the frame. The ribbons ripple, gold light waves travel and the sleigh flies across the existing projected ceiling. THE BOY is already making repeated small normal-speed bounces, completing about two to three bounce cycles during this interval. Knees bend quickly, feet briefly leave the quilt, then land with real weight and rebound. Arms react naturally and quickly for balance, mouth open laughing. The mattress compresses and springs back on every landing.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small physical backward step with the same fixed focal length, nothing sudden. THE BOY maintains exactly the same brisk cadence, completing about three more small bounce cycles during this interval with short airtime and prompt landings. No higher slow jump or prolonged knee tuck. His real-time body motion carries straight across the camera transition without any slowing, pose hold or pause.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
````

**Other takes of C06 on disk (4)**

#### Video prompt — `clips/v12_c06_g1.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `548bef39-7dd5-43d5-993e-f95cda060c4b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_183537_548bef39-7dd5-43d5-993e-f95cda060c4b.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`

````text
Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the cream plaster wall and the asymmetric attic ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the asymmetric attic ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
````

#### Video prompt — `clips/v12_c06_g2.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `594b672b-c09a-4cd0-b706-1773cbeec10f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_191945_594b672b-c09a-4cd0-b706-1773cbeec10f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`
- image ref 1: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`

````text
OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the cream plaster wall and the asymmetric attic ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the asymmetric attic ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
````

#### Video prompt — `clips/v12_c06_g3.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `b264b66d-ba1a-460a-8d11-e6742eb73b13`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_193638_b264b66d-ba1a-460a-8d11-e6742eb73b13.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`
- image ref 1: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`

````text
OPENING FRAMING AND COVERAGE - PRIMARY CORRECTION: use the approved starting image itself as the exact first camera frame, not merely a room reference. The camera must not begin tilted upward, close to the ceiling or above the supplied viewpoint. Show the whole jumping boy, full bed and foot bench from frame zero in the same composition as @Image 1. Every visible flat ceiling panel AND every visible sloping ceiling panel already carries the dense Christmas artwork at full brightness. Do not invent a new pale foreground ceiling, soffit, overhang or blank triangular panel. The camera does not reveal any extra unprojected space above the source framing. The full projection is already playing before filming and never fades in. Keep the same starting frame and existing physical room; correct the camera angle, not the architecture.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - START AT THE SUPPLIED IMAGE'S EXISTING LOWER COMPOSITION, then make a very small downward tilt followed by a gentle physical pull back. Never re-aim upward before frame zero.
0.0-2.2s the camera begins at EXACTLY @Image 1's angle and framing: the boy's whole body and the full mattress are clearly visible around the middle and lower half, with the foot-of-bed bench and floor visible below, while the already projected wall and ceiling occupy the upper half. Do not start above this framing or crop the boy at the bottom. From this exact view, tilt downward only about 3 degrees in one slow steady move, retaining the fully projected ceiling in the upper part of the frame. The ribbons ripple, gold light waves travel and the sleigh flies across the existing projected ceiling. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small physical backward step with the same fixed focal length, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
````

#### Video prompt — `clips/v12_c06_g4.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `71426913-f33c-4db7-9725-96c5b6c9970c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_211642_71426913-f33c-4db7-9725-96c5b6c9970c.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`
- image ref 1: `content/video_12_assets/starting_frames/v12_c06_g1.png` · Higgsfield media `ad7bddc8-13d6-46cb-9af2-439134e2db10`

````text
REAL-TIME SPEED - PRIMARY CORRECTION: this is an ordinary phone recording played at exactly 1x speed, never slow motion or high-frame-rate footage played back slowly. The boy makes five to six small lively mattress bounces across the five-second clip, roughly one complete bounce every 0.8-1.0 second. Each bounce has a quick knee bend, brief push-off, only about 0.3 second in the air, a prompt gravity-driven landing and immediate rebound. No long hang-time, suspended pose, languid arm swing, frozen apex, speed ramp or time stretching. He is already bouncing at frame zero and continues at the same natural cadence through the last frame. The camera's gentle movement is independent of the child's brisk normal-speed movement and must never slow him down. All projection motion also runs continuously at normal playback speed. Preserve the corrected lower opening and already complete ceiling coverage.

OPENING FRAMING AND COVERAGE - PRIMARY CORRECTION: use the approved starting image itself as the exact first camera frame, not merely a room reference. The camera must not begin tilted upward, close to the ceiling or above the supplied viewpoint. Show the whole jumping boy, full bed and foot bench from frame zero in the same composition as @Image 1. Every visible flat ceiling panel AND every visible sloping ceiling panel already carries the dense Christmas artwork at full brightness. Do not invent a new pale foreground ceiling, soffit, overhang or blank triangular panel. The camera does not reveal any extra unprojected space above the source framing. The full projection is already playing before filming and never fades in. Keep the same starting frame and existing physical room; correct the camera angle, not the architecture.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the asymmetric attic ceiling, including both the flat and sloping panels. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the cream plaster wall behind the bed and the whole asymmetric attic ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy bedroom with an ASYMMETRIC ATTIC CEILING: one flat horizontal cream-plaster panel over the left half of the room and one broad plaster slope descending down the right side to a low knee wall, joined by a single long straight ceiling seam. A large white-painted spindle bed with a tall curved headboard stands against the flat back wall, a low recessed double window sits in the right knee wall, dark walnut bedside chests and honey-oak floorboards with a cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with light skin, freckles and tousled auburn hair, wearing warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole asymmetric attic ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny village children keep passing gifts outside the village, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - START AT THE SUPPLIED IMAGE'S EXISTING LOWER COMPOSITION, then make a very small downward tilt followed by a gentle physical pull back. Never re-aim upward before frame zero.
0.0-2.2s the camera begins at EXACTLY @Image 1's angle and framing: the boy's whole body and the full mattress are clearly visible around the middle and lower half, with the foot-of-bed bench and floor visible below, while the already projected wall and ceiling occupy the upper half. Do not start above this framing or crop the boy at the bottom. From this exact view, tilt downward only about 3 degrees in one slow steady move, retaining the fully projected ceiling in the upper part of the frame. The ribbons ripple, gold light waves travel and the sleigh flies across the existing projected ceiling. THE BOY is already making repeated small normal-speed bounces, completing about two to three bounce cycles during this interval. Knees bend quickly, feet briefly leave the quilt, then land with real weight and rebound. Arms react naturally and quickly for balance, mouth open laughing. The mattress compresses and springs back on every landing.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small physical backward step with the same fixed focal length, nothing sudden. THE BOY maintains exactly the same brisk cadence, completing about three more small bounce cycles during this interval with short airtime and prompt landings. No higher slow jump or prolonged knee tuck. His real-time body motion carries straight across the camera transition without any slowing, pose hold or pause.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The asymmetrical ceiling is clearly built from one flat plane and one sloping plane. The sleigh, garlands and stars kink at their single straight meeting seam, stretch across the right-hand slope, then bend onto the knee wall. The back wall-to-ceiling angle and recessed window jambs interrupt and foreshorten the picture at their real built edges. No floating flat picture in front of the ceiling. All physical walls, ceiling planes, beams, seams and trim remain stationary.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v12_c07_g1.png` → `clips/v12_c07_g2.mp4`

#### Image prompt — `starting_frames/v12_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `93f65259-c58c-4b78-9144-e90159f52d8e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_135812_93f65259-c58c-4b78-9144-e90159f52d8e.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`
- @Image 2: `content/video_12_assets/references/v12_c05_r1.png` · Higgsfield media `16ec0091-87a5-4b00-9673-799570413b29`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the new room and children; it is the same house viewed from farther inside. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids; a boy of about five with light skin, freckles and tousled auburn hair. Both fully dressed in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved barrel vault and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. The same room and decor as @Image 2, seen from the middle of the great room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the muted cranberry wool rug, the cream boucle sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the surface texture of the fieldstone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v12_c07_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `9f034c55-78c5-4c5f-8b19-deff820a4099`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_191946_9f034c55-78c5-4c5f-8b19-deff820a4099.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v12_c07_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c07_g1.png` · Higgsfield media `93f65259-c58c-4b78-9144-e90159f52d8e`
- image ref 1: `content/video_12_assets/starting_frames/v12_c07_g1.png` · Higgsfield media `93f65259-c58c-4b78-9144-e90159f52d8e`

````text
SOFA CONTACT CORRECTION: the girl's opening airborne position must lead naturally inward onto the broad interior seat cushion, never onto the thin sofa back or outer edge. All later take-offs and landings stay centred on that same flat cushion, with both feet supported and realistic weight. @Image 1 fixes the original opening geometry; @Image 2 is the same frame and fixes the room and projection appearance.

OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, cathedral ceiling panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected Christmas village picture is PLAYING across the back wall and the entire cathedral ceiling and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved cathedral ceiling and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with light skin, freckles and tousled auburn hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids. Preserve her airborne opening pose, then complete that jump with a small natural inward landing on the broad flat seat cushion INSIDE the sofa, beyond the near backrest. Both feet land fully supported near the cushion centre. She continues small vertical bounces over this same broad cushion centre with natural knee flexion, balanced arms and visible cushion compression. She never lands or balances on the narrow top of the backrest, armrest, cushion seam or outer edge. Keep normal anatomy and consistent limb proportions; no twisting legs, floating feet or furniture intersection.
Both in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole cathedral ceiling. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, wall material and ceiling details and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster ceiling details, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny village children keep passing gifts beside the village and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, wall material and ceiling details. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the muted cranberry wool rug, the cream boucle sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD completes the opening jump with an inward landing onto the centre of the broad seat cushion, both feet fully supported, knees absorbing the landing, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD makes a small balanced vertical bounce directly above that same broad seat-cushion centre and lands there on both feet, her knees bending naturally and the cushion compressing. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the cathedral ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the cathedral ceiling or an un-animated ceiling detail in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All physical walls, ceiling planes, beams, seams and trim remain stationary.
````

**Other takes of C07 on disk (1)**

#### Video prompt — `clips/v12_c07_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `28e20c13-6f51-4af8-bfb9-fbeed0a92ecf`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_183537_28e20c13-6f51-4af8-bfb9-fbeed0a92ecf.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_12_assets/starting_frames/v12_c07_g1.png` · Higgsfield media `93f65259-c58c-4b78-9144-e90159f52d8e`

````text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, cathedral ceiling panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected Christmas village picture is PLAYING across the back wall and the entire cathedral ceiling and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a tall double-height New England Christmas great room with a simple steep CATHEDRAL CEILING: two broad smooth cream-plaster roof planes meeting in one straight high central ridge, crossed by three dark stained-oak horizontal collar beams at even intervals, no curved cathedral ceiling and no coffer grid. The back wall is a tall triangular gable with a central chimney breast of small warm-grey fieldstones and a thick oak mantel; three tall rectangular white-framed windows stand on the left and a square opening into a dining room is on the right. Natural honey-oak floorboards, a large cream boucle sectional sofa, a low rectangular upholstered ottoman and a muted cranberry wool rug. Preserve the exact furniture placement, child identities, clothing, room colours and framing in that supplied image.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with light skin, freckles and tousled auburn hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about eight with warm tan skin and straight dark-brown hair in two loose braids, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in warm forest-green and cream knitted Christmas jumpers with red holly berries and white reindeer, cream knitted lounge trousers and thick red socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole cathedral ceiling. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, one continuous SNOWY CHRISTMAS VILLAGE ON CHRISTMAS EVE: glowing red-and-cream wooden houses, a tall candlelit village church, little shops dressed in holly and scarlet bows, garland-lined cobbled lanes, children in winter coats carrying wrapped presents and a tiny choir with songbooks beneath a gold-lit Christmas tree. A horse-drawn red gift wagon loaded with ribboned parcels passes the village square. The whole lower panorama is packed with festive detail, snowy firs, frosted shop windows, candy canes and candle lanterns. High on the walls, enormous ornate gold Christmas bells and evergreen wreaths tied with crimson velvet bows. ACROSS THE CEILING, Santa's red sleigh and eight gold-lit reindeer follow a graceful arc around one brilliant eight-point Christmas star; long woven trails of holly, red ribbon, gilded baubles and tiny ivory snowflakes spread across both roof planes. The dominant colours are deep Christmas crimson and ruby red, rich gold, evergreen green and cream-white detail against deep midnight sky. No Ferris wheel, no carousel, no nebula, no abstract space vortex. This is one coherent Christmas story illustrated as projected light, not physical props. Every projected shape and flake lies on the walls or ceiling only.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, wall material and ceiling details and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE GIFT WAGON AND THE VILLAGERS. The red gift wagon travels along the lower wall; its wheels turn and its horse walks at a steady pace, about one wagon length every second. The projected village children walk through the lanes carrying parcels, while the tiny choir gestures with songbooks. All are flat moving drawings on the wall. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster ceiling details, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny village children keep passing gifts beside the village and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, wall material and ceiling details. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the muted cranberry wool rug, the cream boucle sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the cathedral ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a gift wagon that does not travel or villagers that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the cathedral ceiling or an un-animated ceiling detail in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the gift wagon advances along the wall; villagers move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The two sloping ceiling planes remain plainly visible. Projected garlands, the sleigh trail and snowflakes change perspective at the straight roof ridge, folding across it and foreshortening differently on the left and right roof slopes. Each dark oak collar beam catches light on its near face and casts a narrow real shadow on the plaster beyond; projected elements break and resume with a visible offset across the beam. Imagery bends again at each wall-to-roof junction and both corners of the projecting fieldstone chimney; tiny stone faces and recessed mortar retain their texture under the luminous image. All physical walls, ceiling planes, beams, seams and trim remain stationary.
````
