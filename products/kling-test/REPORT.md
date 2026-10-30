# Kling 4.0 hook test — picture + sound from ONE generation (30 Oct)

Same 4 hooks, same sets as the kit test (kit-test/output/*). Each hook: silent input (ffmpeg -an), cut at the
original hook end, last frame frozen up to the next whole second (all 4 hooks end on a hard cut).
Higgsfield video_analysis + local transcribe / hook-audio / speech-times / energy envelope BEFORE any generation
-> `<name>/analysis.json`. Kling made the voice and the real sounds itself from the prompt; no music asked, none came.

Files per reel: `hook-kling.mp4` (1080x1920, own sound), `compare.mp4` (original | old kit Kling hook | new Kling hook,
1080 wide, sound of the new one), `analysis.json` (words + seconds of the original + what our take says).

**Important:** the link given for reel 2 (Deui1RKgYWF) is an IKEA pallet reveal, not a rolled robe. The kit's
"snoopy-rollrobe" hook was really made from DfGoo7qyJ9o (folder collision, see kit notes). So reels 2 and 4 use the
same original hook (DfGoo7qyJ9o, 0-2.733 s), once with the Snoopy set, once with the Princess set (Seedance side did the same).

## Results per reel (kept take)

| Reel | Motion / timing vs original | Robe / box | Face | Sound (ours vs original) | Credits |
|---|---|---|---|---|---|
| 1 snoopy-frozen (char-02, outdoors like the original) | Same single shot; tugs ~1.0/2.0 s, blanket pulled 3.75-4.2 s, box shown from 4.25 s (orig 4.2) | HEATPUP box spelled right, robe in window; blanket with our dog face | ~ character-02 (brunette, beanie) | "Three" 0.1-0.7 (orig 0.0-0.45), "Two" 1.4-2.0 (1.05-1.9), "One" 2.6-3.4 (2.55-3.9, less stretched), "Oh!" 4.4 (orig 4.2, half cut by hook end). No extra words, no music | 20 |
| 2 snoopy-rollrobe (char-07, room-18) | Roll overhead, drops DOWN ~1.7 s, hangs full 2.0 s = original | Snoopy robe one to one (back, hood, ears, hat), hangs empty. Hood sticks out on top of the roll from frame 0 | Face hidden by roll/robe (as original); hair/body = char-07 | No voice (correct, song-only original); fabric whoosh 1.6-2.7 s, room tone. No music | 12 |
| 3 princess-countdown (char-01, room-14) | Cloth whipped off 2.55-2.75 s (orig 2.6-2.75), box to lens from 3.75 s (orig 3.5) | Princess / HEATED ROBE box crisp, spelled right | = character-01 | "Three" 0.2 (0.23), "two" 1.1 (1.23), "one" 2.0 (2.09) on time; "Let's see how it comes out!" 3.5-4.5 vs 3.1-3.92 = 0.4 s LATE -> hook kept to 4.6 s (orig 4.07) so the words are not cut. No music | 20 (+20 try 2, same lateness) |
| 4 princess-unroll (char-11, room-22) | Both tries drop the roll 0.5 s EARLY (1.25 vs 1.75). Kept try 2, slowed the static first 1.25 s x1.4 (invisible) -> drop 1.75, full 2.25 = original | Princess robe back one to one; try 1 had a re-roll morph at 1.75 s, try 2 clean | = character-11 | No voice (correct); whoosh at drop, room tone. No music | 12 (+12 try 1) |

All four: caption + emojis removed by Kling with no smudge, no text added, no end flash inside the hook length
(outputs 3.04 / 5.04 s, trimmed to the hook end), 9:16 1080p, soft natural light.

## video-edit vs start frame (gpt_image_2_5 first frame -> kling4_0 image-to-video), tried on all 4

| Reel | Start-frame result | Better |
|---|---|---|
| frozen | Face closest to char-02, but reveal at 3.5 s (orig 4.2), tugs different, and at 4.75 s it JUMPS to a product photo of the box | video-edit |
| rollrobe | Unrolls early (1.0 s), shows the FRONT, then the robe turns/morphs to the back | video-edit |
| countdown | Sentence pacing best (3.0-4.3), but reveal early (2.5 s), push to lens late (4.25 s), camera jump 4.5 s | video-edit (start frame only better on the sentence) |
| unroll | Unrolls early (1.0 s), robe spins back -> front (morph) | video-edit |

video-edit wins 4/4: the silent input video gives Kling the exact seconds; with only a start frame + text timeline
Kling moves things 0.5-0.7 s early and invents turns. The start frame only helps face likeness a little.

## Credits (Kling 4.0 1080p = 4 cr/s, GPT Image 2.5 4k = 4.25)
video-edit try 1 x4 = 64; video-edit try 2 (countdown + unroll) = 32; 4 start frames = 17; image-to-video x4 = 64
-> 177 credits (balance fell 171.4 in the same window, shared with the Seedance agent).

## Not perfect yet
1. Kling speaks a full sentence ~0.4 s slower than the original (2 tries); counting words are on time.
2. Unroll: Kling drops the roll ~0.5 s early even in video-edit -> retime of the static start needed.
3. Frozen: our "Oh!" 0.2 s late, half cut by the 4.533 hook end.
4. Snoopy roll: hood sits on top of the roll from the first frame.

## Best settings + prompt template (video-edit)
Settings: kling4_0, mode video-edit, resolution 1080p, aspect_ratio 9:16, duration = silent input length (whole s),
declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612; medias: silent hook as video_references, then image_references
in order: character photo (face crop), room photo, product refs (box and/or robe). Input: hook cut at its end, last
frame frozen to the next whole second, -an. Output: trim to the hook end.

```
Edit the input video. Image 1 = OUR WOMAN (the person who must appear). Image 2 = OUR ROOM (the place). Image 3 = OUR PRODUCT BOX (<short name>). Image 4 = our robe, seen through the window of the box.   [robe hooks: Images 3-N = OUR ROBE (back, hood, front...)]

The output has exactly the same length as the input video (<N> seconds) and copies its camera, framing and timing frame by frame: one single static shot, no cuts. Follow the timing of the input exactly - nothing happens earlier than in the input.

ACTION, second by second, exactly like the input: <t1-t2 s what she does, how each object is held, which hand, where it goes, the reveal second. Roll: "the roll stays closed - nothing unrolls before 1.75 s; at 1.75 s (not earlier) she keeps holding the top edge and lets the rest drop DOWNWARD under its own weight; the top never rises up; the robe hangs EMPTY and FLAT like on a hanger, sleeves limp, no invisible body, hood flat, her fingers visible at the top">.

PRODUCT: the box is Image 3 reproduced ONE TO ONE - same shape and colours, the word <BRAND> spelled exactly <B-R-A-N-D>; through its window the robe of Image 4 one to one. Only one box. Sharp and readable.   [robe: REPRODUCE IT ONE TO ONE from Images 3-N - never described in words]

PERSON: the woman is Image 1 exactly - her face, eyes, nose, lips, skin, hair colour and hairstyle - a completely different person from the woman in the input video. She wears <outfit>. She stays in the foreground, centred, the same size as the woman in the input.

PLACE: Image 2 exactly - the same room, furniture, Christmas tree, floor and walls as Image 2. Nothing of the input room remains.

TEXT: the white caption and the emojis of the input are removed completely - the background behind them is clean. No text, no subtitles, no watermark anywhere except the logo printed on the box.

SOUND (made by you, with the picture) - the timing of the words is very important: the woman herself says out loud, on camera, <tone>, lips in perfect sync: "<word 1>" from <s> s to <e> s; "<word 2>" from ...; [sentence: "starting at <s> s she says quickly in one breath "<sentence>" and has finished the last word by <e> s - nothing is said after <e> s"]. Real sounds of each action at its second: <cloth whoosh at x s, cardboard tap, room tone / outdoor ambience>. Only these words, no other words, no other voice, no narrator. No music, no song, no jingle.
   [song-only original: "nobody speaks. Real sounds only: a quiet steady room tone; <whoosh at x s>. No voice, no words, no breathing, no hum, no narrator. No music, no song."]

LOOK AND LIGHT: very soft, very natural light - diffuse daylight from a window and the warm glow of real lamps and string lights, gentle low-contrast wrap-around light, soft shadow edges, true slightly warm colours; never harsh light, no spotlight, no dramatic contrast, no HDR, no glow or bloom, no glossy CGI look, no over-sharpening. Warm cozy colours, Full HD sharpness, shot on an iPhone 16 main camera, handheld-steady like the input, completely realistic UGC: a real unedited phone video of a real person in a real American home, nothing AI-looking. Natural human movements at natural speed, no sudden jumps, no morphing, no warping hands, five fingers on each hand, fabric moves with real weight and gravity. Vertical 9:16, no zoom, no extra cuts, no transition, no fade, and the last frame stays on the same scene (never jump to a product photo or a white frame at the end).
```
Exact prompts used: `prompts/` (local, not committed).

Lessons: for a sentence, ask it ~0.3-0.4 s EARLIER than the original (Kling speaks it late); for a roll/unroll write
the drop second as "(not earlier)" and still check - retime the static start if early; local whisper tools invent words
on song-only hooks ("You", "Thanks for watching", "A. 4 3 5") - trust video_analysis for speech yes/no.
