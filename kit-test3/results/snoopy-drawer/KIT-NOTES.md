# KIT-NOTES — snoopy-drawer (first run of Robe Studio, fresh install)

Request: "make this with snoopy https://www.facebook.com/reel/1242292615234243 thanks! classic ending"
Result: `output/snoopy-drawer/snoopy-drawer-FINAL.mp4` (1080x1920, 30 fps, 16.87 s, no on-screen text) + `caption.txt` + `text.txt`.

## What was used
- Reference: FB reel, downloaded fine with `tools.py download` (yt-dlp worked; inbox copy not needed). 15.74 s, hook = 0–5.13 s (hard cut at 5.13 to the back/hood shot).
- Hook concept: woman holds a rolled-up robe like a cake, a black baking tray on top as a lid, counts "One, two, three. Let's see how it comes out." and flips the tray off at 4.6 s. (Close to the proven "Yule log" concept.) Copied with Kling 4.0 video-edit on her own shot.
- Set (next-set): character-26.jpg (after rejecting character-40), room-4k-32.jpg (after rejecting room-4k-31), B-roll **v4**, connector-fabric-1.mp4 (0→1.7), remote-fabric-1.mp4 (0.3→3.0), song mariah-all-i-want.mp3 (drop 53.4 → music_start 48.27, duck 5.13).
- Outfit: "a red and white Fair Isle long pajama set" (outfit.txt, pasted in hook and B-roll).
- Cozy: classic (B-roll's own wide sitting shot).

## Job ids / media ids
| what | id | credits |
|---|---|---|
| B-roll v4 (Kling 4.0 video-edit, 8 s, 1080p) | 73c4e67e-e7a0-443a-a279-9e49b2f54b2e | 32 |
| clean frame (GPT Image 2.5, caption removed) | a014b433-c528-4c47-a90d-ea610481f386 | 4.25 |
| hook try 1 (Kling 4.0 video-edit, 6 s, 1080p, sound) | 8dc1448f-12cb-49d0-8523-549ca237f9bb | 24 |
| video_analysis (free) | db99e16f-b088-4927-8f12-3d553e8445bb | 0 |
| **total** | | **60.25** |
Uploads: hook-part 26abe914…, hook-in 24213ed2…, frame 9737b28d…, snoopy_v4 65837d83…, snoopy_v5 fddef122…, 5 robe refs, character-26 dded0edb…, room-4k-32 839c154b… (all in state/media.json).
Credits counted from `transactions` by time and amount (32 at 20:37:2x, 4.25 at 20:39:06, 24 at 20:41:2x). The workspace is shared: at the same seconds there are other identical Kling 32 / 24 and GPT 4.25 spends from the other tests, and `transactions` shows NO job id, so "your own jobs, by time" cannot be told apart exactly — I matched by submit time + amount.

## Tries per part
- B-roll v4: 1 try, accepted. broll-check said "SHOT COUNT: ours 3, motion clip 6" — false alarm: the motion clip's 0.63/0.77/1.13 cuts are tiny hood cuts that Kling played as one continuous move; all 5 shots/actions are there. Face = character (hair a bit more auburn than her chestnut photo under warm light), dog face never seen from behind, she SITS on the real cream sofa in the wide cozy shot, no connector/remote/text. cutjerk run, 2.7–3.5 s at 15 fps: clean.
- Hook: 1 try, accepted. No `hold` needed (tray flip starts ~0.1 s later than the original, < 0.3 s). retime → 5.17 s file, edit uses 0→5.13.
- Start frames: none (video-edit route).

## Where the kit was unclear / contradictory / missing / I decided myself
1. **"Fresh install" is not fresh**: `state/used.json` already listed 6 characters and rooms 01–30 as used, and `library/rejected/` was full of Alex's rejects. So next-set started at room-4k-31 / character-40. Fine for me, but a creator's first video skips the first 30 rooms.
2. **next-set gave a dark-skinned character first (character-40)** although rule 1 says characters are light-skinned only — the pool still contains photos the kit itself forbids; next-set does not filter skin tone. Rejected by hand (also eyes half-closed).
3. **Rooms 31/32 are evening/dusk rooms**, while the frozen B-roll prompt says "soft daylight" and look.txt says "BRIGHT… no moody or dim grade". I rejected room-4k-31 (night, sofa cut at the edge) as "dark room"; room-4k-32 is also dusk-lit but brighter with the sofa clearly visible, so I kept it. The kit gives no threshold for "dark" — my judgement. Kling made it a warm, well-lit room anyway.
4. **Order of new-video steps vs setup**: setup step 3 says upload BOTH motion clips (v4+v5) of the robe; CLAUDE.md says "upload only what THIS video needs". I followed setup (uploads are free). Contradiction.
5. **Folder name**: step 1 downloads to `output/_new/ref`, step 2 renames — but the analysis/audio3 paths in step 1a already use `output/<name>/…`. I renamed right after download.
6. **cleantext vs a moving object through the caption box**: the tray flies up through the caption area at 4.6–5.1 s. A static clean-photo patch would have erased the tray. The kit has no time-range option. Workaround (in output/, no kit edit): cleantext on the whole hook-part, then ffmpeg-concat 0–4.55 s cleaned + 4.55–5.13 s original (caption visible only for the last 0.58 s) + `tpad` freeze to 6 s; the prompt says the caption is removed completely. Result: no caption or smudge in our hook.
7. **ceil(hook end) + freeze**: hook ends at 5.13 on a hard cut → froze the last frame to 6.0 s as rule 9f.2 says. Worked; Kling kept the still end.
8. **Which robe refs in the hook**: HOOKS.md "Best way" says Image 3 = front, Image 4 = back; "Start frame" says front + hood for Snoopy; PRODUCT.md says front_closed/front_open/back/hood "every robe shot". I used front_closed, back, hood, detail (Images 3–6). Unclear which set is meant.
9. **Sound block "sentence after a pause 0.4 s earlier"**: "Let's see how it comes out" follows "three" with no pause (3.23 → 3.25), so I asked it at its measured second. The rule does not say how long a "pause" is.
10. **video_analysis finished in ~3 s** (doc says 5–20 min) and its words matched Whisper exactly — good, but the HOOKS.md example sentence is the same phrase, which made me double-check with an independent Whisper run.
11. **compare-audio**: words all correct, no extra words, no music; "two" +0.34 s (tool's own margin is ±0.1–0.2), "Let's" −0.22 s. My own Whisper/energy check put every word within ~0.15 s of the original. Not regenerated (rule: advice only). BUT our hook has near digital SILENCE (−60…−70 dB) between phrases and from 4.3 s to the hook end — Kling did not make the requested continuous room tone, nor the tray "whoosh/clank". In the final mix the 4.5–5.13 s stretch is −50 dB (Mariah's intro at 0.2 is almost inaudible) — a small dead-air dip right before the drop. Not a regeneration reason per the kit, so delivered; noted.
12. **retime gave 5.17 s and montage made the hook segment 5.167 s** (first cut at 5.167 instead of 5.13; the 24 fps Kling file rounded to 30 fps). Drop lands ~0.04 s (1 frame) before the cut. Negligible.
13. **broll-check "SHOT COUNT 3 vs 6" warning** is misleading for v4: the motion clip's micro-cuts in the hood part are counted as shots. The kit says "redo if a shot is missing" — none was; I accepted.
14. **Disk full (tool/environment failure)**: `montage.py` failed with "No space left on device" (its temp segments at crf 16 go to /tmp on the full disk; the disk went to 0 MB because of the other tests). Workaround: moved broll-cut.mp4 + hook-exact.mp4 to `/dev/shm/sd/` (RAM tmpfs) with symlinks in output/, ran `TMPDIR=/dev/shm/sd python3 engine/montage.py` with a copy of edit.json whose "out" pointed to /dev/shm, then copied the FINAL into output/. **broll-cut.mp4 and hook-exact.mp4 in output/snoopy-drawer are symlinks to /dev/shm** (they vanish on reboot — the B-roll for "2 more hooks" would then have to be re-downloaded from job 73c4e67e…). Also deleted: broll.mp4 (uncut, after broll-check), reference.mp4, hook-in.mp4, hook-clean.mp4, frame-clean.jpg, a3 stems, the raw hook-1.mp4 (re-encoded crf 19 before retime to save space).
15. `faster_whisper` with a file path crashes (PyAV `metadata_errors` TypeError) when called directly; audio3.py itself works. Only hit this in my own double-check; worked around by decoding to wav first.
16. **Budget numbers**: GPT Image 2.5 is 4.25 credits, not "≈4". Kling 4.0 = 4/s confirmed (8 s = 32, 6 s = 24). A copied hook with ceil() input is 6 s here = 24, above the kit's "hook ≈ 16–20".
17. **On-screen text**: rule 9 says copy the original word for word (no product name in it, so nothing to swap): "Every Christmas lover / NEEDS this..🥺🎄🇺🇸", on screen for the whole original video → suggested for the whole video.
18. Upload flow: copying 2 KB presigned URLs by hand into `tools.py put` for 11 files is slow and error-prone; `put` could take the media_upload JSON or the kit could ship a helper.

## Checked (final)
1080x1920, 16.87 s, cuts at 5.17 / 10.57 / 12.27 / 15.0 = hook → B-roll part 1 → connector → remote → cozy; no on-screen text; no flash frame at the hook → B-roll cut (12 frames checked at 15 fps); loudness −13.2 LUFS integrated, B-roll part never quieter than the hook (−12…−19 dB vs −16…−18 dB); music fades at the end; connector fully joined, remote one light climbing.
