# KIT-NOTES — princess-rollpov (first run of a fresh kit, 31 Oct)

## What was made
- Reference: FB reel 1790743905460572 — yt-dlp download WORKED (inbox copy not needed). 17.03 s, cuts 3.03 / 5.47 / 6.8 / 10.83 / 12.33 / 14.53.
- Hook = shot 1 only (0–3.03 s): POV lying on a sofa, feet in slippers behind a rolled robe, she pushes it with her feet, it unrolls flat (roll moves 1.6 s, flat ~2.2–2.6 s). Their 2nd shot (box unboxing 3.03–5.47) is NOT in our edit order, so hook end = 3.03.
- Sound: Higgsfield analysis = song only (Mariah "All I Want for Christmas"), nobody speaks → audio3 `--no-voice`; our hook asks for room tone + fabric sounds; our song (next-set picked the same Mariah song) drop 53.4 on the cut.
- Set: character-27 + room-4k-21 (cream L-sofa, sage wall, tree), B-roll v4, connector-fabric-1 (0.15→1.7), remote-fabric-1 (0.3→3.0), mariah-all-i-want.mp3 (music_start 50.37, duck 3.03). Cozy = classic.
- Final: output/princess-rollpov/princess-rollpov-FINAL.mp4, 14.59 s, 1080x1920, cuts at 3.033 / 8.466 / 10.033 / 12.766.

## Job ids / tries
| part | job id | credits | note |
|---|---|---|---|
| clean frame (gpt_image_2_5, text removal) | 1bb63c16-ca2d-4763-8261-af405a2d7ee0 | 4.25 | made, then NOT used (camera moves, see 5) |
| B-roll v4 try 1 | d6135a9c-1df4-433f-abbf-c8dc03c34595 | 32 | rejected: face = a different, paler, thinner woman than character-27 |
| B-roll v4 try 2 (USED) | 4c66aacd-8c3b-4cdf-8a76-cd837e170493 | 32 | same frozen prompt; face/hair/earrings now match much better |
| hook video-edit try 1 (USED) | cb7c32e4-d4a7-438b-968d-32a06077d045 | 16 | timing matched; no hold needed |
| video_analysis | a83b28de-be3d-434e-a5e3-402a98faa3cc | 0 | |
Total for this video ≈ **84.25 credits** (32+32+16+4.25), matched by time in `transactions` (20:37:2x, 20:38:4x, 20:41:04, 20:42:21). Tries: hook 1, B-roll 2 (1 regen), images 1.
Uploads (media ids): princess_v4 71231f58…, princess_v5 8d180eef…, front 5d84491c…, back 7f162cd5…, pouch_open 9cf10d17…, pouch_feet f68e8594…, character-27 8ea9f651…, room-4k-21 658d356d…, hook-part 81cdc1fc…, hook-in (BAD, see 1) 9337fc50…, hook-in2 ea840a41…, frame ba968127… (all in state/media.json or here).

## Kit problems / unclear points / my own decisions
1. **BUG in the kit's freeze command (CLAUDE.md 9f.2 + HOOKS.md "Best way" 1):** `ffmpeg -i ref.mp4 -t <hook end> -vf tpad=... -t <ceil> ...` — the second `-t` overrides the first, so the clip is simply the first <ceil> seconds of the reference, INCLUDING the next scene (my first hook-in.mp4 had the unboxing scene at 3.03–4.0). Nothing is frozen. Fix: put `-t <hook end>` BEFORE `-i` (input option): `ffmpeg -t 3.03 -i ref.mp4 -vf tpad=stop_mode=clone:stop_duration=1 -t 4 -an hook-in.mp4`. I caught it by looking; first upload wasted (no credits).
2. **montage.py fails when the disk is nearly full**: segments at crf 16 + base + final in /tmp, and on a crash (`concat` exit 228) the temp dir is NOT deleted (rmtree only on success) → it leaves garbage that fills the disk further (there are many old `tmp*` dirs in /tmp from earlier runs). Work-around: `output/princess-rollpov/montage_patched.py` (copy, ROOT fixed, segment crf 20, segments deleted right after concat, rmtree in `finally`). Same output format.
3. **compare-audio says "sustained music 1.5–3.0 s" in our hook — false.** Stems show it is the drums stem only (fabric thumps of the robe landing, peak −0.4 dB at ~2.1 s); bass/vocals −56…−81 dB. Advice ignored (as the kit allows). The kit's audio3 also labels the original's beat at 2.91 as a "low thump/step" action.
4. **Rule 2 vs a POV hook:** "character photo ALWAYS a direct reference" — but in a POV hook only legs are seen. I attached it anyway (Image 1); no face appeared. The kit says nothing about POV/no-face hooks.
5. **cleantext vs a moving camera:** the camera here is static until ~1.5 s, then tilts. cleantext pasted the clean patch at wrong positions in the moving part (I checked: misaligned sofa pieces). Followed the kit fallback: text left in the input, "remove the caption" in the prompt → Kling removed it fully. The 4.25-credit clean frame was wasted; the kit should say "check the camera first with a 5 fps strip BEFORE making the clean frame".
6. **Outfit vs footwear:** outfit.txt must be copied word for word into hook and B-roll, but the original hook is all about feet in white fluffy slippers, and the frozen B-roll prompt says "never a sock". I kept socks/slippers OUT of outfit.txt and added "with white fluffy slippers on her feet" only in the hook prompt. Kit doesn't cover footwear.
7. **Hook result flaw I accepted:** the pajama pants are plain cream on the thighs and red-heart print only on the shins (Kling mixed two garments). Timing, robe, room, text removal were all right, so I did not spend 16 more credits; the B-roll pants are heart-print all over, so hook→B-roll clothing is close but not identical.
8. **B-roll v4 shot 3 hood:** frozen prompt says "hood DOWN" in the foot-pocket shot; both tries keep it UP (the motion clip has it up). Kit prompt contradicts its own motion clip; not a fail per the check list, left as is.
9. **broll-check always reports "SHOT COUNT 3 vs 4"**: the motion clip's cut at 0.77 is a whip/swoop that Kling renders as a continuous move. Both tries looked fine there (10 fps). The warning is a false alarm for v4 and should be documented.
10. **Fixed connector clip has a jump at ~0.13 s** (hands reposition, hard jump visible at 30 fps; `cuts` finds it). PRODUCT.md says use 0 → 1.7. I used **0.15 → 1.7** (my decision).
11. **Character skin rule:** "light skin only" — character-27 is light-medium/olive (Latina). Borderline; I accepted her (face sharp, real, full HD only — not 4K). The kit gives no measurable threshold.
12. **Room is AI-made** (room-4k-21, kit's own 4K rooms) with a warm/orange evening grade, while rule 1 says rooms must be "real (never AI)" and rule 8 says no orange cast. Rule 31 Oct says the 4K rooms are the default — contradiction inside CLAUDE.md. Followed the newer rule.
13. **Coffee table rule 7b** ("table in the middle of the floor → make the room without it first"): room-4k-21 has a round coffee table in front of the sofa. Not applied: in the POV hook nobody stands in the room, and in the B-roll the camera angle doesn't put it in front of her. Kit is unclear whether 7b applies to every room or only when she stands there.
14. **Fresh install, but state/used.json already lists 20 rooms + 4 characters as used** (it ships with the kit). next-set started at room-4k-21 / character-27; history was empty. Probably intended, but confusing for "fresh".
15. **Drop tool vs kit value:** `tools.py drop mariah-all-i-want.mp3` lists no jump near 53.4 (it lists 16.5, 42.5…). I used PRODUCT.md's 53.4 as instructed.
16. **Prices:** GPT Image 2.5 is 4.25 credits, not "≈4"; Kling 1080p = 4/s confirmed (8 s = 32, 4 s = 16). Transactions have no job id, and two other tests spent identical 32-credit Kling jobs at the same second — attribution by time only is ambiguous (I matched by submit time + amount).
17. **Blocks:** rule 4b says paste look.txt (iPhone 17 Pro Max) into every video prompt; HOOKS.md's video-edit template ends with its own short look line; new-shot-warm-iphone16 is "for new shots (start frame, image-to-video)" — unclear for video-edit. I pasted look+light+motion+no-text and NOT the iPhone 16 block.
18. **9e SOUND block template** has no variant for "nobody speaks"; I wrote `VOICE (layer 1): nobody speaks; no words at all.` audio3's own draft (with --no-voice) prints a broken sentence ("nobody speaks, <tone>, lips in perfect sync … these words: nobody speaks").
19. setup step 3 uploads BOTH motion clips (v4 and v5) although next-set only needs one per video (v5 upload unused this time; free).
20. Disk: ~400 MB shared went to 0 twice during this run (other tests). Deleted my stems, try-1 B-roll, hook-1 raw, clean frame, bad hook-in.

## Verdict (honest)
- Hook vs original, 10 fps side by side: same framing (POV over the legs), roll starts moving on the same frame (~1.6 s), unrolls flat by ~2.2–2.6 s like theirs, no cut, ends 3.04→retimed to 3.03. **No `hold` needed** (< 0.1 s off). Robe reads clearly as the princess robe (hood + tiara, sleeves, belt, yellow skirt, crown border). Their caption gone. Room = our room. Flaw: pants pattern (point 7); roll outside is blue/striped instead of yellow (fine). Sound: fabric taps/whoosh + room tone, no voice, no music; our song plays quiet under it.
- B-roll (try 2): same woman in every front shot, face/hair/earrings close to character-27; back shot cut 1.75 s; jerk cut clean; cozy WIDE sitting on the real L-sofa with the sage wall + leaf prints + lamp; no connector/remote/text. Hood stays up in the pocket shot (point 8). Brief socks visible while stepping in (allowed, rule 3b).
