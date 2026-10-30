# Kit test notes — video 1: snoopy-frozen (ref https://www.instagram.com/reels/Deuu2AXyPPx/)

Tested exactly as the creators got the kit (28 Oct). Each line: step — what happened — what to fix.

## Setup (skill `setup`)
- check.sh: ALL GOOD. It does NOT check `demucs` (needed by `vocals`, `audit-sound`) — on a fresh creator machine `vocals` will crash. Add demucs (+ torch) to check.sh and to the install lines in setup/SKILL.md.
- Uploads: 10 files (motion, motion2, 8 Snoopy refs) = 10 `media_upload` calls, each answer ~2 KB of presigned URL that has to be pasted back into a curl. Works (all 200), but it is slow and eats context. Fix: a `tools.py upload <file>` helper is impossible (needs MCP), but setup could tell Claude to put all PUTs in ONE bash call (I did that) — say so.
- setup/SKILL.md step 3 says "one media_confirm with type video for the motion clip" but there are 2 motion clips (motion + motion2). Minor wording.
- state/media.json is shared by everything in the folder; a parallel session (Princess) wrote princess_* keys at the same time. Kit has no locking — read-merge-write, never overwrite the file. Worth one line in CLAUDE.md "Uploading" step 4.
- setup step 4 (long explanation to the creator) skipped in this test (no creator present).

## Reference + sound (new-video step 1/1a, CLAUDE.md 9d/9e/9f)
- new-video says download to `output/_new/ref`, HOOKS.md says `output/<name>/ref`. Two parallel videos would both use `output/_new` and collide. Use a unique temp name or name the folder first.
- THREE tools gave THREE different word timings for the same 3 words:
  - `hook-audio` (whisper on full mix): Three 0.00, two 0.62, one 2.88 (+ lists "Let it go, let it go" from the SONG at 4.22+ as if it were speech)
  - `audit-sound` on the `vocals` output: Three 0.0, two 0.48, one 2.2
  - `onsets` on vocals: [0.01, 1.07, 1.95, 2.59, 4.47, 4.95] (6 onsets for 3 words; 1.95 is a breath, 4.47+ is the song)
  - energy plot (what is really there): "Three" 0.0–0.45, "twooo" 1.05–1.9 (stretched), "ooone" 2.6–3.9 (stretched).
  The kit never says which tool wins, and the whisper word starts are off by up to 0.7 s on stretched words. Fix: one command that prints word START+END from the vocals envelope, labelled with whisper words; tell Claude to trust it.
- `hook-audio` "SPEECH: yes" + "Let it go" words: song lyrics are reported as speech. CLAUDE.md 9e.1 mentions "only song lyrics" but hook-audio does not separate them; Higgsfield video_analysis did (scene 2 = "orchestral song").
- video_analysis_create finished in ~6 s (kit says 5–20 min "start it FIRST") — fine, just outdated.
- 9f.2 "input = reference cut at ceil(hook end)": hook ends at 4.53 with a HARD CUT to another scene (projector box). ceil = 5 s → the Kling input contains 0.47 s of the next scene. Kit does not say what to do. I froze the last frame of the hook from 4.50 to 5.0 (tpad) so Kling gets one continuous shot.

## Set (next-set, rule 1)
- next-set gave room-15: 736x981 px (rule 1 says "full HD") and dark (dusk). Rejected. Then room-16: 736 px, glossy/staged, not American. Rejected. room-17: real American living room (fan, TV, sofa), but still 736x981. Accepted (best of the low-res ones). The first rooms in the pool (14–17) are all 736 px Pinterest thumbnails — remove them or make next-set skip < 1080 px.
- BUG: `reject <room>` + `next-set` takes a NEW CHARACTER too (both are always advanced). Rejecting 2 rooms burned 2 good characters (character-05, -06 marked used without being used). Fix: `next-set` should only replace the rejected kind, or `reject` should un-mark the other.
- new-video step 3 says ALWAYS make the head+shoulders crop for the B-roll; Snoopy PRODUCT.md says crop only "if she wears a skirt/shorts/dress". Contradiction. Followed the skill (crop).
- next-set prints "connector ... (whole clip ...)" but PRODUCT.md says use connector 1.2–4.0. Contradiction in the tool's printout.

## B-roll
- Proven prompt has NO quality blocks (look/light/motion/no-text) while CLAUDE.md 4b says "paste them in EVERY video prompt, never shorten". PRODUCT.md says "never add a sentence". Followed PRODUCT.md. Say explicitly in 4b: "except the proven B-roll prompt".
- Outfit: rule 9i says the hook woman is "in the B-roll outfit", but the hook is OUTSIDE in the snow in a winter coat — pajamas outside makes no sense. Kit gives no exception.

## Hook (object map, 9g/9h)
- Object map: PERSON → our woman (character-02); PROP Elsa fleece blanket → light-blue fleece blanket with a big print of OUR hood's dog face (avoided the word "Snoopy" to dodge ip filters — kit literally says "Grinch/Snoopy blanket", which invites an IP refusal); PACKAGING Frozen box → snoopy_box_display (HEATPUP window box, existing ref); PLACE snowy house exterior → stays (9i only covers "at home").
- HOOKS.md clean-frame prompt has no quality blocks; 4b says every image prompt. Followed HOOKS (adding "bright UGC look" to a pixel-for-pixel edit would change the frame).
- `tools.py cleantext` BUG: runs FOREVER when the input clip has no audio track (looped clean photo + `-shortest` with no audio map). It wrote 103 s / 2.8 MB before I killed it — on a creator's laptop this silently fills the disk. Fix: add `-t <input duration>` (or `overlay=shortest=1`) in cleantext.
- My first attempt to build the 5 s input with `-t 4.5` + `tpad` produced 4.5 s (output -t cuts the tpad). Kit has no command for "cut hook to N s and freeze the tail" — needs a `tools.py hook-input <ref> <hook end>` that does cut + freeze + cleantext in one go.
- GPT "pixel for pixel" clean frame changed her face/expression slightly — harmless because cleantext only pastes the text box, but the HOOKS.md text implies the whole frame stays identical.

## Rule conflicts met while writing the hook prompt
- 9g says the branded object is "Image 1" for Kling; 9i / HOOKS "Best way" say the character is Image 1. Used: Image 1 = HEATPUP box, Image 2 = woman, Image 3 = blanket, Image 4 = hood.
- 4b says paste `no-text.txt` ("NO TEXT ANYWHERE") in every video prompt; 9g says NEVER write "no text anywhere" when our logo must show. Used 9g's ending instead of no-text.txt.
- HOOK SOUND — three different instructions in the kit:
  (a) HOOKS.md "Best way" step 4 + new-video 5b: write the words in the Kling prompt, `"audio": true`, Seedance only as fallback;
  (b) HOOKS.md "Hook sound" header: "Rule 28 Oct replaces everything below: Kling video-edit on our muted hook (720p, audio only) + place-voice";
  (c) CLAUDE.md 9e: "Seedance ONLY, never Kling for the voice", blur-for-sound + seedance video_edit + voice-to-lips.
  A creator's Claude cannot know which one is current. I put the Sound line in the Kling prompt (free) AND then followed 9e (newest, in CLAUDE.md).

## B-roll result (try 1, 28 credits)
- broll-check: "SHOT COUNT: ours 5, motion 4" because of a cut at 2.21 inside the pocket shot (framing jump between right and left foot). Rule 9j says to ignore cuts < 2.8 s, but broll-check still prints it as a PROBLEM and lists 1.08-2.09 / 2.33-3.55 as separate safe segments, so the PRODUCT.md edit (0.15 → cut2) crosses an "unsafe" zone. Tool and rule disagree.
- Visually: shot 1 hood back right (camel, ears, hat); shot 2 hood face right, she steps right then left foot over the top edge into the pouch, feet stay in; lying + sitting: legs fully covered. Room = room-17 (grey sectional, fan, tree). Face ≈ character-02. ACCEPTED on first try. The 2.21 framing jump will be visible as a small jump in the final.
- PRODUCT.md says expect 3 cuts (≈0.9, 3.5, 4.8); we got 4 (0.96, 2.21, 3.67, 4.96). Edit times "0.15 → first cut of shot 3", "cut2+0.05 → cut3-0.05" are therefore ambiguous (cut2 here = 2.21, the false one). Used the real shot boundaries 3.67 / 4.96.

## Hook try 1 (Kling video-edit, 5 s = 20 credits)
- Result: our woman (dark hair, beanie, cream coat), our blue blanket with the hood dog-face print, reveal of the HEATPUP window box at 4.25 s (original 4.2 s), HEATPUP spelled right, robe with dog hood visible in the window, house/snow kept. The box flashes under the blanket during the tugs (~1.0 and ~2.3 s) — the original does the same tease, so accepted. No cuts (single shot) → retime x1.00.
- `tools.py compare` prints ALL frames in ONE row (50 frames → 5500x392 px) — unreadable when displayed; the check skill tells Claude to "LOOK at every frame" with it. Fix: tile 10 per row (2 rows original/ours per second).
- `compare-audio` on Kling's own voice: NOT OK ("one" late). But whisper gave the REFERENCE yet another timing this time (two 0.7, one 1.94) — 4th different set of numbers for the same 3 words. The audio tools are not reliable enough to pass/fail on.
- montage.py: `orig_vol` defaults to 0.15 → the clip sound of the hook (the voice!) is mixed at 0.15 while music under the hook is 0.2 → voice BELOW the music, the opposite of rule 9e.7. The kit never tells Claude to set `orig_vol`; only the docstring example shows 1.0. Fix: default orig_vol 1.0 or document it in 9e.7 / PRODUCT.md edit section.

## Sound (rule 9e) — done as written
- blur-for-sound: my first face box (y 0.17) cut off the mouth — the kit gives no way to find the box; I had to guess from the sheet. A "face box" helper (or printing a frame with a grid) would avoid a wasted Seedance run. Second box OK (lips sharp, product unrecognisable).
- Seedance video_edit 480p 5 s: took ~8 min; came back 4.71 s long (input 5 s). Voice "Three / two / one" all there, no music. Its "two" is short (0.4 s) where the original stretches it (~0.85 s) even though the prompt said "stretched".
- voice-to-lips with starts 0.11,1.3,2.45 → targets 0.0,1.05,2.6: resulting onsets 0.05 / 1.10 / 2.63 (±0.05 OK). audit-sound: no missing word, no music. Spectrogram: background continuous, one thin vertical line ≈2.9 s (tiny click), no black gaps.
- Putting hook.wav on hook-exact with `-c:v copy -shortest` (the natural ffmpeg way; kit gives no command) made the VIDEO 4.433 s instead of 4.53 → montage silently shortened the hook by 0.1 s and the music drop (music_duck 4.53) landed 0.1 s after the cut. Had to re-encode. Fix: a `tools.py put-sound <video> <wav> <out>` that re-encodes and checks the length.

## Edit / montage
- PRODUCT.md "cuts ≈0.9, 3.5, 4.8" vs our 4 cuts — used broll-check safe segments: 0.15–3.55 (puts on + pouch, crosses the false 2.21 cut), 3.79–4.84 (lying), cozy-zoom from 5.11.
- Final: 15.75 s, 1080x1920, cuts at 4.533 / 7.967 / 10.8 / 12.7 / 13.8 = exactly the montage "cuts at" line. 12 frames around the hook→B-roll cut: clean, no flash. Loudness: hook −19.8 dB (voice on top, music quiet), B-roll −16.9 dB, rest −13.3 dB.
- `tools.py history` is shared with the parallel Princess session: the last video there was ALSO a 3-2-1 countdown cloth reveal, so this video breaks the "different from the last 3" rule — but the creator brought the link, the kit gives no way to refuse/adapt a link-based hook. Kit should say what to do when the creator's link repeats a recent concept.

## Delivery text (rule 9 vs new-video step 1)
- Rule 9: "ALWAYS the reference's ORIGINAL text, word for word ... never rewrite it". new-video step 1 + HOOKS.md step 2: "copy the reference wording, swap the product". The original says "DO NOT send this to a frozen girlie 😭❄️" — for a SNOOPY robe that is wrong (Frozen = their product). Followed rule 9 (word for word) → the suggested text is off-product. Fix rule 9: "word for word, only the product/fandom name swapped (frozen girlie → Snoopy girlie)".

## Other kit problems seen
- `refs/pouch.jpg` (snoopy_pouch, sent as Image 7 in EVERY Snoopy B-roll) is a screenshot of a DIFFERENT robe (cream/red-wine, not camel) with someone else's burned-in caption "DONT send this to your mom..." and a woman in short shorts (bare legs = nsfw risk). Replace with a clean photo of the camel Snoopy pouch.
- Result has TWO separate camel cone pouches (right/left) instead of "one wide pouch across the whole width" (PRODUCT.md). Probably because of the wrong pouch ref.
- tools.py header lists `transcribe` as the way to read speech; HOOKS.md step 2 says run `transcribe` ALWAYS; CLAUDE.md 9d/9e use hook-audio/vocals/audit-sound/onsets instead. Too many overlapping commands, none authoritative.

## My own frame-by-frame check of the FINAL vs the reference
OK: hook action and timing (tugs, reveal at 4.25 vs 4.2), single shot like theirs, woman = character-02, our blanket print, HEATPUP box spelled right with robe in window, house/snow kept, caption removed with no smudge; voice words on the original seconds; B-roll robe/hood right in every shot; feet go in and stay in; lying/sitting legs covered; connector fully joined; remote lights; cozy end clean; no text; 15.75 s.
WRONG / not perfect:
1. Suggested on-screen text says "frozen girlie" (rule 9 conflict, see above).
2. "two" not stretched like the original (0.4 s vs ~0.85 s).
3. Visible framing jump inside the pocket shot at ~6.6 s of the final (false cut 2.21 of the B-roll).
4. Two separate pouches instead of one wide pouch.
5. Hook is outdoors in a winter coat, B-roll indoors in pajamas → she changes place + clothes at the cut (rule 9i only covers "at home"); acceptable story-wise but not "one place".
6. Room source photo 736x981 (rule 1 says full HD).
7. Original uses the song only from the reveal; ours has Mariah quietly under the countdown too (as rule 9e.7 says) — fine, but differs from the original.

## Credits (estimates from the kit's price list; workspace balance is shared with the parallel session so before/after is not exact)
B-roll 28 + 2 GPT images (~8) + hook Kling 5 s (20) + Seedance 480p 5 s (~17) ≈ 73 credits. No redo needed.
