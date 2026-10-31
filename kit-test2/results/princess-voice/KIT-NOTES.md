# KIT-NOTES - princess-unroll (first run of a fresh kit, princess robe, reel DfDZLLQyX0F)

## Result
- FINAL: output/princess-unroll/princess-unroll-FINAL.mp4 (1080x1920, 15.13 s) + caption.txt + text.txt
- Edit: hook 0-4.0 (hook-exact.mp4 from hook-1) -> B-roll v4 try 1 (broll-cut-try1.mp4) 0.10-1.63, 2.15-3.08, 3.30-5.50 -> connector-fabric-1 0-1.7 -> remote-fabric-1 0.3-3.0 -> cozy 5.74-7.60. Cuts in final: 4.0, 5.57, 6.53, 8.77, 10.47, 13.20.
- Set: character-01.jpg (head+shoulders crop, she wears a skirt in the photo), room-18.jpg (black leather sofa on the right). Song: mariah-all-i-want.mp3, music_start 49.4, music_duck 4.0.

## Credits
- Balance before 8562.24, after 8189.49 = -372.75, BUT the workspace is shared with the other parallel tests (the transaction list shows other Kling jobs in the same minutes). My own spend, from the transaction list matched to my submits: 32 + 16 + 32 + 16 = **96 credits** (Kling 4.0 1080p = 4 cr/s confirmed). No GPT Image used.
- => "balance before/after" (CLAUDE.md rule 13) is useless on a shared workspace; the kit should tell you to read `transactions` instead.

## Higgsfield ids
| what | id |
|---|---|
| princess_v4 / princess_v5 motion (setup) | ab8e8fd1-39f1-4393-99a3-9cdd83d84d32 / 1a3b7136-402c-4f4c-afa4-f0d22920c35e |
| princess_front / back / pouch_open / pouch_feet | 689fd0c9-... / 29dfa3a6-... / 1928ad22-... / 9216a678-... (full ids in state/media.json) |
| character-01 head+shoulders crop | 013dd5ed-bd83-4c2b-af24-4021292f7090 |
| room-18 | b590e614-56f6-42f5-961a-58e3ef9f92ab |
| hook part 0-4.0 with sound (for analysis) | 4ec23d5c-053a-46f8-9f22-6a7ca478197f |
| video_analysis | 631d77af-f9b5-4af6-9640-284151600e37 |
| hook input 0-4.0, no sound | dbb83b12-e146-4d6f-8859-85e7a85126a0 |
| B-roll v4 try 1 (USED) | 86133630-b945-4c1e-8d18-25b43332b58e |
| B-roll v4 try 2 (rejected, different woman) | f61178d7-2c63-407b-b3bd-d8ab5dd0bedc |
| hook try 1 (USED) | d6097f3c-0a51-4826-91e6-a4f7c0904010 |
| hook try 2 (rejected, worse) | 5db182ac-a094-462e-8348-082fd3457065 |
| unused upload slots (snoopy_v4, snoopy_v5 - URL asked, never PUT) | ec980d54-..., 685318a8-... |

## Tries per part
- Hook: 2 tries. Try 1: countdown on time, sentence 0.24-0.4 s early (because the kit's "ask a sentence 0.4 s earlier" rule), unroll ~0.25 s early. Try 2 (sentence at measured seconds, "stays rolled until 3.0 s", "never turns around"): much worse - robe unrolls at ~1.25 s (1.75 s early), "one" dropped, sentence even earlier, roll shows blue instead of yellow. Kept try 1 (rule 9e: "still off -> keep the better one").
- B-roll v4: 2 tries (same frozen prompt, as the kit says). Try 1: right woman, robe, room, sofa, cozy perfect; FAIL = white socks visible on the floor at 1.76-2.10 s and 3.12-3.27 s (broll-cut time). Try 2: feet cleaner, but a DIFFERENT woman (long loose hair, other face) in the front shot, back shot 0.9 s too long (cut 2.75), cozy only 1.3 s. Mixing tries (new-video 7d) impossible: the pocket shot is the only bad shot in try 1 and its woman is wrong in try 2. Workaround: try 1 with the sock frames cut out (pocket shot starts at 2.15; 3.08-3.30 removed, merged into the existing cutjerk jump at 3.10). No socks left in the final at 6 fps. Not done: a 3rd B-roll (would have broken the 110-credit test budget).
- Connector / remote: fixed clips, 0 tries, both look right (connector fully in, one light climbing).

## Problems in the kit (most important first)
1. **audio3.py PART 1 word seconds are wrong for this reel.** It put "Three" at 1.20 s and "two" at 1.26 s (0.06 s apart!), "one" 2.09 stretched 0.82 s, "let's" 3.19. Real (energy of the vocals stem + 2 independent faster-whisper runs): Three ~0.15, two ~1.0, one ~1.95, let's ~2.75, see 3.10, how 3.2, it 3.42, turns 3.48, out 3.64-3.90. Also "out." ends 4.23 s in a 4.0 s clip. Consequence: `compare-audio` compares against wrong numbers - it said "three -1.02 s EARLY" for a word that was on time, and would send you into a pointless regeneration. I wrote the prompt with my own measured seconds and judged with my own same-method comparison. The kit has no way to detect this; it should at least print the vocal-energy onsets next to the whisper words and flag two words < 0.15 s apart.
2. **video_analysis words disagree with what is said, and it hallucinates.** It returned "Three, two, one, let's go!" while both whisper passes hear "...one, let's see how it turn(s/ed) out" (≈6 syllables over 1.1 s; "let's go" cannot fill that). It also invented 4 more scenes (0:04-0:15) for a 4.0 s upload. Kit rule says "the words always come from the analysis". Following it would have made our voice say "let's go!" over 1.1 s of lip movement. I DEVIATED and used "Let's see how it turns out!" (HOOKS.md's own example line is almost the same). The kit needs a tie-break rule (analysis decides IF someone speaks; the words = what 2 transcriptions agree on).
3. **"Ask a sentence 0.4 s EARLIER" (rule 9e.3) made it worse here.** Asked at 2.35 for a measured 2.75, Kling said "Let's" at 2.50 (whisper) = 0.25 s early, the rest 0.3-0.4 s early. Asking at the measured second (try 2) gave an even earlier sentence, so Kling timing is just random +-0.4 s; the fixed offset is not reliable.
4. **The retry rule for copied hooks costs credits with no real control.** Try 2 with "stays rolled until exactly 3.0 s" unrolled at 1.25 s. One regeneration "with the fix" is not a fix; budget-wise the hook ended up 2x.
5. **`tools.py retime` drops the sound** (`-an`). The kit says the hook in the edit = hook-exact.mp4 with `"audio": true` -> the voice would silently vanish. I re-muxed hook-1's audio into hook-exact.mp4 in output/. (Here retime did nothing else: no cuts in the hook, speed x1.00.)
6. **B-roll frozen prompt can't be fixed when it fails the feet check.** Rule: "regenerate ONCE with the SAME prompt (never add words)", then mix tries; when the second try fails on a different point (wrong woman) there is no third option except paying again. The same-prompt retry also changed the woman completely (the crop with an updo -> long loose hair). Suggest: allow a 2nd retry, or allow cutting the bad frames out (what I did) explicitly.
7. **Princess v4 feet rule vs motion clip.** The v4 motion has both feet on the floor at the start of the pocket shot; Kling copies that, so "never visible, not even before they go in" fails by design ~50% of the time. A kit-level trim (start the pocket segment ~0.35 s later, skip 3.10-3.30) would fix it for free.
8. **Caption-text removal: kit has no answer for "camera still, but the subject moves through the text box".** cleantext would paste the empty background over the robe when she lifts it into the text (2.9-3.4 s). I used the fallback "remove the caption text completely" in the prompt -> it worked (no text in ours), saving the 4-credit clean frame.
9. **Setup uploads 15 files, ~8 of them useless for this creator.** I uploaded only princess refs + princess motion (and asked for snoopy motion URLs but did not PUT them). Each upload answer is ~3 KB of signed URL that has to be copied by hand into curl - very token-heavy; a `tools.py put <file> <url>` or an upload helper would help. HOOKS.md also says setup's `media_upload` "ONE file per call" - fine but slow.
10. **Outfit continuity hook -> B-roll (rule 9i) is not enforceable**: same text "red and white Christmas-print long pajama set" gave a fair-isle red/white set in the hook and a red floral set in the B-roll. Kit could make one outfit reference image and pass it to both.
11. **Shared-workspace credits** (see Credits): rule 13 "balance before/after" gives wrong numbers when several sessions share a workspace; `transactions` is the reliable way.
12. **broll-check SAFE SEGMENTS vs PRODUCT.md edit times** are given on the UNCUT broll.mp4 while the edit uses broll-cut.mp4 (0.30 s shift after 3.10) - easy to mix up; the kit should run broll-check (or cuts) on broll-cut too and print edit times directly.
13. ffmpeg sheet one-liners in HOOKS.md (`tile=...` without `-frames:v 1`) fail when the frame count exceeds the tile ("Cannot write more than one file"). Add `-frames:v 1`.
14. new-video step 1 says `download <url> output/_new/ref`, CLAUDE.md says the download fails -> "ask the user to put it in inbox/" - but no step says to then COPY inbox/<file> to ref/reference.mp4. I did it myself.
15. Hook "end" was easy here (hard cut at 4.0), so hook = 4.0 s, input duration 4 (Kling min 3) - OK.
16. faster-whisper `transcribe(path)` crashes with this PyAV version (`metadata_errors`); audio3 works because it passes arrays. Only matters if you transcribe by hand.

## Decisions I made myself
- Outfit: red and white Christmas-print long pajama set (long, per PRODUCT.md nsfw note).
- Kept caption text in the hook input and asked Kling to remove it (worked).
- Words: whisper's sentence instead of the analysis's "let's go!".
- Hook: kept try 1 (better than try 2).
- B-roll: try 1 with two sock moments cut out, instead of a third generation.
- Suggested text = the original's, whole video, top: "Do NOT let a Princess mom\nsee this... 🤩👑".

## Honest verdict
- Hook vs original: same shot, same framing, same action (rolled robe held out -> lifted -> unrolls to full length, back of the robe shown), our woman/room/robe, no caption. Timing: the lift starts ~2.6 s (orig 2.85-2.9), unroll at ~2.8-3.0 s fully hanging ~3.2 s (orig unroll 3.0, hanging 3.5) = 0.2-0.3 s early. Voice (same-method whisper on vocals stem, orig -> ours): Three 0.00->0.00, two 0.64->0.64, one 1.88->1.78, let's 2.76->2.52, see 3.12->2.74, how 3.24->2.84, it 3.42->3.02, turns 3.48->3.16, out 3.64->3.40. Countdown on time, sentence 0.24-0.40 s early. No music in our hook voice track (room tone), our song comes in under it.
- B-roll: woman = character in all front shots; robe = refs (blue/yellow, puffed striped sleeves, red belt, crown border, white sherpa, tiara hood); cozy WIDE, sitting on the real black sofa, legs covered. The v4 jerk is cut; my extra cut at 3.08->3.30 makes the robe-open jump a bit bigger. Pockets look like open yellow flaps rather than closed foot pockets. Hood DOWN in the pocket shot as the prompt says.
