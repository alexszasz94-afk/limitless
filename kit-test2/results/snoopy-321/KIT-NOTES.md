# KIT-NOTES - snoopy-mom (first run of a fresh kit, test 31 Oct)

Request: "do this one with snoopy https://www.facebook.com/reel/1106653841688023 , classic ending ok"
Result: `output/snoopy-mom/snoopy-mom-FINAL.mp4` (1080x1920, 16.8 s) + caption.txt + text.txt.

## Credits
- Balance before: 8562.24. Balance after: 8189.49. That difference (372.75) is NOT ours: the workspace is shared with 3 other tests running at the same time, so `balance` before/after (what the kit tells you to do, rule 13) can't measure one video's cost.
- Our real spend, from `transactions` matched to our submit times: **56 credits**
  - 18:54:35: -32, B-roll v4 (Kling 4.0, 8 s)
  - 18:58:08: -24, hook (Kling 4.0 video-edit, 6 s)
  - video_analysis: no charge shown
- No regenerations. Each part worked on the first try.

## Higgsfield ids
| id | what |
|---|---|
| 49afe5cb-354a-4fc9-8ffa-6fdfc75da2be | upload: ref hook part 0-5.1 s (for video_analysis) |
| d442ce6a-fc6e-4cf9-9cd7-a7238842eaed | video_analysis: "One, two, three." then festive music from ~3 s |
| 7368becc-b9d8-476e-bcbb-7c748ad6b8bf | upload: ref 0-6.0 s, no sound (Kling video-edit input) |
| 92565199-23ca-452b-a22c-619b0013d608 / 83d5f02d-fa4c-441b-a59d-817de38c956a | snoopy_v4 / snoopy_v5 motion |
| e4260b82-13dd-44f8-929a-0a0d34c0bc80 / 2f7d3132-9a34-4537-b4ac-8e553850aa72 | princess_v4 / princess_v5 motion |
| 2b3581fd-591c-488b-9575-7f6caab93bc2, 6dc1144b-89f0-4d13-ab8d-84304b0900de, 5030e9ae-ad56-4b25-ad14-f4256f608e8a, 3412cdd7-4071-4408-9699-dee3af4a596a, 1503eed2-b00e-4e99-a3c2-20dfd815241a | snoopy front_closed, front_open, back, hood, detail |
| d49cbd56-fa8e-4eb3-a132-4046c9167d8c | character-21.jpg |
| 988e15ed-7b38-426b-9c14-8e2bd73d2738 | room-31.jpg |
| **b0bb470e-1411-4257-af66-ef201202dfe5** | B-roll v4 (1 try, accepted) |
| **dc5baee4-adb6-4a9f-9334-e05032298998** | hook, Kling video-edit with the 3-layer SOUND (1 try, accepted) |

## Tries per part
- B-roll v4: 1 try. broll-check reported "SHOT COUNT: ours 3, motion 6". That's a false alarm, because the motion clip's micro-cuts at 0.63/0.77/1.13 are hood-lift jump cuts that Kling merges. All shots are there.
- Hook: 1 try. Word starts are within ±0.08 s of the original. The reveal is about 0.1-0.2 s early (inside the 0.3 s tolerance).
- Connector and remote: fixed clips, 0 tries.

## Problems / unclear spots / my own decisions (with what I did)
1. **`next-set` isn't idempotent and burns a set when you run it twice (biggest trap).** My first run was piped through `| head`, which caused BrokenPipe. Running it again to read the output picked a NEW character AND a NEW room and marked both pairs as used. Nothing warns you. Fix I applied (state/ only): I put `current` back to the pick I'd actually made (character-21 + room-31) and took character-22/room-32 out of `used`. The kit should make `next-set` print the current pick unless the previous one was used or rejected.
2. **The character quality gate is inconsistent.** Rule 1 says characters must be "sharp", but `next-set` calls `photo_ok(min_sharp=0)` for characters, so it handed me character-20, which `photo-ok` itself calls blurry (110 < 150). 11 of the 34 library characters fail `photo-ok` for blur. I rejected character-20 with `tools.py reject` and took the re-pick.
3. **audio3 puts the first word at 0.00 s.** It measured "One" at 0.00-1.16, but the real onset in the vocals stem is 0.875 s. It did the same on our hook (0.00). It also put "two" at 2.19 when the real onset is 2.05. Whisper's first-word timestamp isn't being snapped to energy. Because `compare-audio` compares two wrong numbers, it said OK by accident. I measured the onsets myself from the demucs vocals stem in 25 ms frames and used 0.88 / 2.05 / 3.40 in the prompt. I wrote a corrected copy to `a3-orig-fixed/audio3.json`. The kit has no way to override a wrong audio3 word time.
4. **audio3 false "MUSIC" on our hook.** It flagged 3.5-5.0 s as MUSIC, so `compare-audio` said NOT OK and told me to regenerate. The stems show a single percussive burst at 3.9-4.1 s (drums stem -14 dB, bass about -70 dB). That's the robe dropping, not a song. I didn't regenerate, which saved 24 credits. On the original, audio3 also missed the real music: it called 4.5-5.1 s "room tone" at -8.8 dB, while the Higgsfield analysis says music. Its music/room-tone call isn't reliable.
5. **`retime` drops the audio (`-an`).** CLAUDE.md 9f.4 says the hook in the edit = `hook-exact.mp4` from retime, and the same hook needs `"audio": true` with Kling's voice. Followed literally, you get a silent hook. Workaround: I muxed hook-1's audio back onto retime's video (speed was x1.00 anyway).
6. **`cleantext` doesn't work for this kind of reel.** The camera is static, but the robe moves through the caption area (the roll is behind the text, then drops through it). A static patch would freeze a ghost roll there. HOOKS.md only says "works when their camera stands still". I skipped it and used the kit's fallback ("remove the caption text completely" in the prompt). Kling removed the text completely. This also saved the ~4-credit clean-frame image.
7. **The frozen B-roll prompt says "soft daylight", but room-31 is a night photo** (black windows, lamps, fireplace). The rule says copy it word for word, so I did. Kling kept the night look anyway. The frozen prompt should say "the light of Image 2".
8. **The setup skill uploads more than this video needs.** Both robes, box and box_display; the instructions say "one file per call". I uploaded the 4 motion clips and the 5 Snoopy robe refs. I skipped the Princess images and both Snoopy box images because this video has no box or Princess (time and disk). `state/media.json` has no box ids yet, so a later box hook will upload them.
9. **The upload procedure is very heavy for an agent.** Every `media_upload` returns a ~2 KB presigned URL that has to be pasted back verbatim into curl, which means 3 calls per file (~40 calls for setup). Copy errors are the main risk. A small script that takes the JSON would be safer, but there's no MCP-to-shell bridge, so I pasted by hand.
10. **The hook's image order/refs weren't fully specified for Snoopy.** HOOKS.md video-edit says "front = Image 3, back = Image 4". The Start-frame section says "front + hood for Snoopy". Because the hood shows at the reveal, I gave front-closed (3), back (4) and hood (5).
11. **The reveal hood isn't visible.** Our dropped robe shows the collar and the white lining at the neck, not the dog face. That's physically right for a robe held by the shoulders, and it matches the original, where the Grinch face is barely seen. Rule 9h, though, wants "hood with face" wherever the robe appears. The robe does read as a robe (sleeves, belt, pockets, length). I kept it and flag it here.
12. **Face vs. original.** In the original the roll covers the top half of her face. In ours the roll sits higher, so her whole face shows while she counts. That makes the lip-sync visible and I'd call it an improvement, but it isn't an exact twin.
13. **Music vs. original.** In the original the song kicks in with the reveal (~4.0 s). Rule 9n puts our drop on the hook→B-roll cut (5.1). I followed the kit. Mariah's pre-drop break gives ~0.5 s of near-silence (−53 dB at 4.5-5.0 s) just before the cut. It's acceptable, but the kit's mix check doesn't catch a dip like that.
14. **The remote's fixed in/out never reaches light 5.** `remote-fabric-1.mp4` at 0.3 → 3.0 (as the kit fixes it) ends on light 4. Light 5 comes at ~3.25 s. The check list (HeatGrump legacy) says "1→5". I kept the kit's times.
15. **The B-roll cozy face is half-hidden.** "Arms crossed holding the collar" makes Kling pull the fluffy collar over her mouth from about 6.3 s. Her face is visible and smiling at the start of the cozy segment. I didn't regenerate: the rule says the same frozen prompt, and the budget would have gone over 110.
16. **Download.** `tools.py download` worked on the FB reel link. The inbox file is a different encode (AV1). I used the download.
17. **The broll-check shot-count warning is noise for v4.** The micro-cuts in snoopy-v4 mean the count always differs. The tool should ignore cuts under 0.5 s apart.
18. **Budget.** The kit estimate (≈ 45-60 for a new B-roll video) was right: 56.
19. **There's no simple way to verify "words at the same seconds"** without the creator's ears. I relied on stem energy.
