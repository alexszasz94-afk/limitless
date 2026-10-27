---
name: check
description: Quality check + self-repair. Claude LOOKS at every start frame, every generated clip and the final video, finds anything that doesn't look real or breaks the rules, and fixes it alone (regenerate / re-trim / re-edit) before the creator ever sees it. Run automatically after every image, every video and before every delivery — never skip it, the creator should never have to point out a mistake.
---
You are the creator's quality control. Nothing goes to the creator until it passes. Never ask the creator "is this ok?" — decide yourself, fix it yourself.

## How to look
- Image: Read the jpg at full size. For faces/hands, also crop and zoom: `python3 engine/tools.py crop <img> <out> <l> <t> <r> <b>` and Read the crop.
- Clip: `python3 engine/tools.py sheet <clip> <out.jpg> 4` (whole clip) AND `sheet` at 10 fps on the last second (cut it first with ffmpeg `-ss <len-1>`), Read both. `safe-end` too.
- Final: `sheet` at 2 fps + `cuts`; compare cut times with the "cuts at" line montage printed.

## Checklist (every point, every time)
**Start frame (image)**
- Face = the character photo (same face shape, eyes, nose, hair colour/length). Different person → redo.
- Robe = refs one to one: colours, hood (shape, face/tiara/ears), trim, embroidery, pouches. Any invented detail → redo.
- Hands: 5 fingers each, natural grip, nothing fused. Objects have real size and weight.
- Composition matches the reference frame; place makes sense; no text; logos/signs that the reference had are still there (never removed), no invented ones.
- Light: soft and natural, true colours, no HDR/glow/orange cast, not CGI.

**Clip (video)**
- Starts on the start frame, no morph in the first frames.
- Movement natural, real weight, nothing melts, no objects merging with clothes, no flicker, no extra limbs, face stays the same the whole time.
- Robe stays correct in EVERY frame (hood always the right one, pouches correct in the B-roll, robe full length).
- End: no jump to a product/character photo, no sudden zoom, no fade → trim before it.
- Person in the FOREGROUND in every shot: nothing (table, plant, chair) between her and the camera → redo with the room photo without that object.
- Hook sound: when the reference has speech, `tools.py compare-audio <reference hook> <our hook>` must say OK, and the hook segment has `"audio": true` in the edit (check the final with `tools.py speech-times`: the voice bursts are there). A silent hook where the original speaks = redo.
- Copied hook: `tools.py compare` original vs ours on each key action — same column = same second; faster/slower or different → redo (HOOKS.md step 5). Spoken words land on the same seconds as the original (loudness check).
- B-roll pockets: at the start of the pocket shot BOTH feet are outside on the floor and she puts them in one after the other, from outside to inside. A foot already inside at the start → redo.
- B-roll: the person is in EVERY shot (never an empty robe, never a missing head in the back view) → else cut that shot or redo.
- B-roll: same 4 shots as the motion clip, she steps into the pouches, last shot lying cozy; face = character.

**Final video**
- 1080x1920, plays from 0 to the end, no black/frozen frames, no leftover flash of a reference photo at any cut.
- Text switches exactly on the cut, never over a face, readable, spelled right, emojis render.
- Music: present, chorus/drop on the reveal if planned, fades out at the end, no loud click at cuts.
- Order = PRODUCT.md edit order; nothing repeated by mistake; length 10–20 s.
- Variety: hook concept, outfit, music cue and text differ from the last 3 videos (`tools.py history`).

## Fixing (alone)
- Bad image → write the exact problem into the prompt as a fix ("her face is exactly the woman of the SECOND image", "the bundle is cream satin, separate from her dress", "both hands have five fingers") and regenerate. 
- Bad clip → first try a better trim; if the problem is in the middle, regenerate with the fix in the prompt (shorter action, "stays a separate object", "the face stays the same").
- `nsfw` / `ip_detected` → the steps in CLAUDE.md rule 10 and PRODUCT.md.
- Bad final → fix edit.json and run montage again.
- Max 3 tries per piece. If still not good: use the best version, and tell the creator in ONE line what is not perfect.

## Report
At delivery add a short "Checked:" line listing what you verified (face, robe, hands, trims, text, music) and what you fixed alone (e.g. "redid start frame 2 — wrong hood; trimmed hook 1 before a morph").
