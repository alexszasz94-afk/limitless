# How to make the hook (first 2–5 seconds)

The hook is copied from a reference reel (Instagram/TikTok link) or built from the user's idea. The robe video after the hook is always the same structure (see `products/<robe>/PRODUCT.md`).

## Step by step
1. `python3 engine/tools.py download <url> output/<name>/ref` → reference.mp4, its length and its cuts.
2. `python3 engine/tools.py transcribe output/<name>/ref/reference.mp4` — ALWAYS. Write down every line people say (and when). The hook must say the same thing (swap the product name), e.g. "3, 2, 1… let's see how it comes out!" — see "Hook sound" below.
   `python3 engine/tools.py sheet output/<name>/ref/reference.mp4 output/<name>/ref/sheet.jpg 1.5` and LOOK at the sheet (Read the jpg). Write down: each shot of the hook (what happens, where, camera angle), where the hook ends and the robe part starts, the on-screen text (copy its wording and emojis, swap the product name), how long the hook is.
3. For every hook shot pull one frame: `python3 engine/tools.py frame output/<name>/ref/reference.mp4 <second> output/<name>/ref/shot1.jpg` and upload it (it is the composition reference).
4. Make one START FRAME per hook shot (image), check it, then ANIMATE it (video), check it, trim it.
5. Make it make sense for OUR robe: replace their product with ours (folded robe, robe on a hanger, our gift box, people wearing our robe). Brands from the reference (H&M, Burger King, McDonald's, Walmart…) may stay if the reference had them.

## Best way: copy the reference shot itself (motion stays exactly like theirs)
When a hook shot is a simple person+object action (holding/dropping the robe, unrolling, throwing it on), copy it 1:1 with Kling video-edit:
1. Cut that shot from the reference (min 3 s; if shorter, slow it with `setpts=1.45*PTS` and speed the result back up with `setpts=PTS/1.45`).
2. Blur their on-screen text so Kling doesn't copy it: `ffmpeg -i ref.mp4 -filter_complex "[0:v]split[a][b];[b]crop=iw*0.8:ih*0.12:iw*0.1:ih*0.15,boxblur=20:5[t];[a][t]overlay=W*0.1:H*0.15" hook-ref.mp4` (move the box to where their text is; check a frame).
3. Upload it, `generate_video` `kling4_0`, `mode: "video-edit"`, `video_references` = that clip, `image_references` = character photo (head+shoulders crop), room photo, robe front + back. Prompt: `Edit the input video. Keep EXACTLY the same shot, framing, camera position, body movements and timing: <one line of what happens>. Change only: the person to the woman of Image 1 (...), the room to Image 2, and the robe to Image 3 (front) and Image 4 (back) reproduced one to one: <robe words from PRODUCT.md>. Remove the blurred patch at the top, no text anywhere. UGC style, real iPhone video, soft natural light, true colours. No text. Silent.`
3b. BEFORE writing the prompt, analyze the original at 10 fps (`ffmpeg -i hook-ref.mp4 -vf "fps=10,scale=110:-1,tile=10x4" sheet.jpg`, Read it) and write a timeline of EVERY action with its seconds and speed, then put that timeline in the prompt, e.g. `0.0–2.7 s: she holds the rolled robe at face height and sways it slowly left and right. 2.8 s: she lets go of the bottom; the robe unrolls downward SLOWLY and softly with real fabric weight, taking about 0.4 s, fully hanging at 3.1 s. Every action at exactly the same speed and second as the input video, never faster, never rushed.` Kling tends to speed actions up (the robe falls too fast) — the timeline with seconds + `slowly, with real weight, same speed as the input` is what holds it.
4. Write the voice into this same prompt (see "Hook sound — cheapest first"): replace `Silent.` with `Sound: she says out loud, <tone>, exactly like in the input video: "<word 1>" at <s> s, "<word 2>" at <s> s ... <real sounds>; quiet room, no music.` — this is the approved method (princess 3-2-1 hook, 26 Oct: "perfect").
5. MOTION MUST BE IDENTICAL, never rushed: make a 10 fps strip of the original and of ours for the key moment (e.g. the robe dropping) and put them one above the other (`ffmpeg ... -vf "fps=10,scale=110:-1,tile=14x1"` for both, then `vstack`). The robe must start falling on the same frame, fall at the same speed and hang the same way; the cut must be at the same second as the original (find it with `cuts` on both). Off by more than 0.1 s → trim our clip to the original's cut second; action faster/different → generate again with `Keep the exact speed of the input video, not faster` and the exact second of the action in the prompt.
6. Check the end on a 10 fps sheet and trim before anything strange (e.g. a hood suddenly filled like a mannequin).
Use start frame + animate (below) only when the shot needs a new place or object that the reference doesn't have.

## Start frame = image
`generate_image_batch` with `model: "nano_banana_pro"`, `aspect_ratio: "9:16"`, `resolution: "4k"`, every media with role `"image_references"`, in this order: reference frame (composition), character photo (if a person is visible), then the robe refs needed (front + hood for Snoopy; front + back for the princess), box/pouch refs if they appear.
Prompt pattern:
```
A new real candid photo with the SAME composition, framing and camera angle as the FIRST image: <where, what is around, people in the background, Christmas details>. THE WOMAN: exactly the woman of the SECOND image, same face one to one, <hair>, wearing <clothes>. <what she does / holds, with sizes>. THE ROBE: reproduced one to one from the <THIRD/FOURTH> image(s): <short robe description from PRODUCT.md>; copy it, do not design it. <expression: natural, spontaneous, not posing>. Correct hands with five fingers. <then the quality blocks: prompts/blocks/look.txt + light.txt + no-text.txt, word for word>
```
Shot WITHOUT the robe visible (wrapped gift, bundle, closed box, line outside a store, selfie before the reveal): same pattern, but drop the "THE ROBE" sentence and attach NO robe refs; describe the object instead with its size and material, e.g. `She holds in both arms a big soft bundle (about 50 cm wide) wrapped in cream satin and tied with a red ribbon; it is clearly a separate object from her dress, held in front of her chest.` If the next shot reveals the robe, say what colour the wrap is so it can never be mistaken for the robe.

CHECK every start frame before animating (Read the image): same face as the character photo, robe matches the refs (hood, colours, trim, embroidery), hands have five fingers, no text, box/props big and realistic, nothing weird. If something is wrong → generate again with the fix written in the prompt.

## Animate = video
`generate_video_batch` with `model: "kling4_0"`, `mode: "image-to-video"`, `resolution: "1080p"`, `aspect_ratio: "9:16"`, `duration: 3` (5 for longer actions), `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`, medias: start frame job id with role `"start_image"` + the character photo with role `"image_references"` when a face is visible. Do NOT add white-background product photos here (Kling jumps to them at the end). The character photo can ALSO make Kling jump to it in the last 0.3–1 s — that is normal, you just trim it (see Trim). Objects held against clothes (a wrapped bundle against a dress) tend to melt into the clothes: write `the bundle stays a separate object with its own shape and colour the whole time; it never merges with her dress` and keep the action short (duration 3).
Prompt pattern:
```
One continuous real handheld phone video, starting exactly on the start image, no cuts, no zoom. <exact action, step by step, natural>. <what must stay the same: the robe/box/place exactly as in the start image>. No flicker, correct hands with five fingers. <quality blocks: prompts/blocks/look.txt + light.txt + motion.txt + no-text.txt, word for word>. Sound: <real sound>.
```
Never ask for snow/dust blowing in the wind (it makes a fake steam cloud).

## Hook sound — cheapest first
1. **Write the line into the hook's own Kling prompt** (instead of `Silent`): `Sound: <who> says "<exact line>" <with the reference timing>, <other real sounds>.` One generation, no extra cost. Keep `"audio": true` for that segment.
2. Only if that voice sounds wrong/robotic → make it in Seedance as below and mix it on.

## Hook sound in Seedance (fallback, like the original)
Every hook gets its sound from Seedance, matching the reference: the same line people say, the same tone, the same sounds.
1. `transcribe` the reference (step 2 above) — if it fails, upload only the hook (first 3–5 s) and use Higgsfield `video_analysis_create` / `video_analysis_status` (takes 3–5 min) — and write the exact line WITH its seconds, e.g. `Three... two... one... let's see how it comes out!`.
2. Make it in Higgsfield with `generate_video`: `model: "seedance_2_5"`, `mode: "t2v"`, `duration: 4`, `resolution: "480p"`, `aspect_ratio: "9:16"`, `generate_audio: true`, NO images (a start image with arms/skin gets refused as `nsfw`). Prompt: a simple scene with no people that fits the hook + `Sound: a cheerful young American woman off camera, <tone like the reference>, clearly says "<exact line>". Quiet room, no music. No text.` It can take 5–30 minutes; keep waiting with `jobs_wait`.
3. Fetch the mp4, keep only the sound: `ffmpeg -i seedance.mp4 -vn -ac 2 -ar 48000 output/<name>/voice.wav`. Find where each word is (loudness every 0.05 s) and, if needed, cut the words apart and place each one on the matching movement of our clip (ffmpeg `atrim` + `adelay` + `amix`), e.g. each count on a bounce.
4. Put it on the clip with `python3 engine/tools.py voice-mix <hook.mp4> output/<name>/voice.wav <hook-voice.mp4> <delay>` (or mix it onto the final video if the line runs past the hook), `"audio": true` in edit.json. Listen-check by loudness: the words must sit on the right moments.
No speech in the reference (music only) → no voice; the song from PRODUCT.md is enough.

## Trim (always)
Kling often ends the clip by jumping to one of the reference photos or fading to black. Run `python3 engine/tools.py safe-end <clip>` AND look at `sheet <clip> ... 4`; cut the clip before the jump. Also cut slow starts and anything unnatural. safe-end only finds hard cuts: always check the end on a 10 fps sheet yourself (zoom jumps, melting, a face that changes).

## Short hook (only a little of a clip is usable)
The hook should be 3–7 s, each shot 1.2–3.5 s. If a clip is only usable for ~1.2 s:
1. Try once more with the fix in the prompt (shorter action, "stays a separate object").
2. Still short → keep the good 1.2 s and make the NEXT shot longer (up to 3.5 s), or add one extra simple shot from the same start frame (e.g. a closer framing of the same moment, `generate_image` with the first start frame as composition ref + "closer, waist up"), animated 3 s.
3. A 2.5–3 s hook that looks real is better than a 4 s hook with a glitch — never keep a melting/morphing frame to reach the length.

## Proven hook concepts (all made and approved)
| concept | shots (start frames) | text |
|---|---|---|
| Castle gift reveal | 1) woman in a long cream dress in front of a snowy Christmas castle holding a soft bundle wrapped in satin/linen with a ribbon → animate: pulls the ribbon. 2) same place, she holds the robe up by the shoulders, wrap hanging from her arm → animate: shakes it, hugs it | `Snoopy girlies, pls\ndon't hate... 🥺🐶` / `Princess girlies, pls\ndon't hate...🥺👑` |
| Fast-food collab | 1) restaurant outside: long line of people in Christmas sweaters, poster of our robe in the window 2) POV at the counter: cashier pushes a tray with a drink + our big gift box 3) POV carrying the tray to a table, lifting the box | `Burger King\nX\nSNOOPY 🐶🎄` then `Jk, we make them 🤭\n(Link in bio)` |
| Store opening | 1) ribbon cutting at an H&M entrance, balloon arch, staff clapping, mannequins in our robe, phones filming 2) line at the store 3) POV taking our robe off a rail | `H&M X SNOOPY\n🤩🐶` |
| Store curtains | 1) two sales assistants open cream curtains → shelves full of folded robes 2) POV unfolding a folded robe on a fluffy rug, cat in the back | `Don't show this to a\nSnoopy lover...🥺🐶` |
| Mall run | 1) front-camera selfie in a mall with a coffee, shocked face, drops the coffee 2) look down from the railing at a huge line 3) line at the store 4) POV grabbing the robe from the rail | `DONT Show this to a\nSNOOPY LOVER...❄️🎄` |
| Yule log | woman holds a platter with the robe rolled up like a Christmas yule-log cake, a wooden board on top → lifts the board and tosses it | `DONT Show this to a\nSNOOPY LOVER...🎄🐶` |
| Two friends | two women hold rolled robes in front of their faces (hood on top) → they let the robes drop open to full length | `DONT Show this to a\nSNOOPY LOVER...🎄❄️` |
| Bag + trash | 1) hand holds the robe folded in a clear plastic bag in a home library 2) woman in the robe walks out the front door (from behind, robe trailing) 3) woman in the robe rolls the trash bin down the driveway | `Do NOT show this to a\nSnoopy lover 😍🐶` |
| Car gift | 1) at night in the car, woman with a BIG wrapped gift on her lap, laughs 2) top-down POV tearing the paper → our big gift box | `Do NOT let a Snoopy\nlover see this... 🐶💕` |
| "It's just a robe" (whole clip, no B-roll) | top-down from the ceiling: 1) woman lying on a rug in pyjamas, bored 2) same place in the robe, hood up, dreamy 3) wrapped in the robe hugging herself. Add `fanwipe` at each cut | `"It's just a robe..🙄"` then `The robe: ...🥺🐶` (y 0.42) |
