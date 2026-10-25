# How to make the hook (first 2–5 seconds)

The hook is copied from a reference reel (Instagram/TikTok link) or built from the user's idea. The robe video after the hook is always the same structure (see `products/<robe>/PRODUCT.md`).

## Step by step
1. `python3 engine/tools.py download <url> output/<name>/ref` → reference.mp4, its length and its cuts.
2. `python3 engine/tools.py sheet output/<name>/ref/reference.mp4 output/<name>/ref/sheet.jpg 1.5` and LOOK at the sheet (Read the jpg). Write down: each shot of the hook (what happens, where, camera angle), where the hook ends and the robe part starts, the on-screen text (copy its wording and emojis, swap the product name), how long the hook is.
3. For every hook shot pull one frame: `python3 engine/tools.py frame output/<name>/ref/reference.mp4 <second> output/<name>/ref/shot1.jpg` and upload it (it is the composition reference).
4. Make one START FRAME per hook shot (image), check it, then ANIMATE it (video), check it, trim it.
5. Make it make sense for OUR robe: replace their product with ours (folded robe, robe on a hanger, our gift box, people wearing our robe). Brands from the reference (H&M, Burger King, McDonald's, Walmart…) may stay if the reference had them.

## Start frame = image
`generate_image_batch` with `model: "gpt_image_2"`, `aspect_ratio: "9:16"`, `resolution: "4k"`, `quality: "high"`, every media with role `"image"`, in this order: reference frame (composition), character photo (if a person is visible), then the robe refs needed (front + hood for Snoopy; front + back for the princess), box/pouch refs if they appear.
Prompt pattern:
```
A new real candid photo with the SAME composition, framing and camera angle as the FIRST image: <where, what is around, people in the background, Christmas details>. THE WOMAN: exactly the woman of the SECOND image, same face one to one, <hair>, wearing <clothes>. <what she does / holds, with sizes>. THE ROBE: reproduced one to one from the <THIRD/FOURTH> image(s): <short robe description from PRODUCT.md>; copy it, do not design it. <expression: natural, spontaneous, not posing>. Real iPhone 17 Pro Max photo, UGC style, very soft natural light, true colours, low contrast, natural skin; no HDR, no glow, no CGI look. Correct hands with five fingers. No text.
```
CHECK every start frame before animating (Read the image): same face as the character photo, robe matches the refs (hood, colours, trim, embroidery), hands have five fingers, no text, box/props big and realistic, nothing weird. If something is wrong → generate again with the fix written in the prompt.

## Animate = video
`generate_video_batch` with `model: "kling4_0"`, `mode: "image-to-video"`, `resolution: "1080p"`, `aspect_ratio: "9:16"`, `duration: 3` (5 for longer actions), `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`, medias: start frame job id with role `"start_image"` + the character photo with role `"image_references"` when a face is visible. Do NOT add white-background product photos here (Kling jumps to them at the end).
Prompt pattern:
```
One continuous real handheld phone video, starting exactly on the start image, no cuts, no zoom. <exact action, step by step, natural>. <what must stay the same: the robe/box/place exactly as in the start image>. Natural real movements with real weight, no morphing, no flicker, correct hands with five fingers. Very soft natural light, true colours, low contrast; no HDR, no glow, no CGI look. Sound: <real sound>. No text.
```
Never ask for snow/dust blowing in the wind (it makes a fake steam cloud).

## Trim (always)
Kling often ends the clip by jumping to one of the reference photos or fading to black. Run `python3 engine/tools.py safe-end <clip>` AND look at `sheet <clip> ... 4`; cut the clip before the jump. Also cut slow starts and anything unnatural.

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
