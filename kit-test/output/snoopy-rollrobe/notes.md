# Kit test notes — video 2: snoopy-rollrobe (ref https://www.instagram.com/reels/Deui1RKgYWF/)

Setup was already done in video 1 (see ../snoopy-frozen/notes.md for setup + general problems; not repeated here).

## Start (new-video step 0a)
- The kit asked (step 0a) "Which cozy ending do you want? classic or something new" — answered "classic" as a typical creator would. Note: this question blocks the whole run until the creator answers; with a link-only message the creator has to come back before anything starts. Could default to classic and offer the change at delivery.

## Reference + sound
- Reference: woman in a living room holds the robe ROLLED UP horizontally above her head 0–1.75 s, lets it unroll 1.75–2.0 s, holds it full length (back side, hood on top) 2.0–2.73 s; cut at 2.73 to their own B-roll. Caption "Do NOT let a Princess fan\nsee this...😳👑". Same product category as ours (robe) — perfect copy candidate.
- Hook length 2.73 s: the kit says "total hook 3–7 s" (new-video step 1) but 9f says "the hook = the original's hook end, never longer, never shorter". Contradiction for short hooks. Followed 9f (2.73 s).
- `hook-audio` on the hook: "SPEECH: yes … 1.70s MUSIC" — whisper hallucinated the word "MUSIC" from the song; there is NO speech. `audit-sound` on vocals: no words. So hook-audio's SPEECH flag is unreliable both ways (video 1 it listed song lyrics as speech). → song-only original (9e.1): no voice in ours, music from 0 with the drop on the reveal.
- video_analysis not run (no speech; 9d says "every reference" — skipped as pointless, kit should say "only if speech").
- 9e.1 for song-only says "our music from 0 s with the drop on the REVEAL", 9e.7 / PRODUCT.md say the drop goes on the hook → B-roll CUT with music quiet under the hook. Two different rules for where the drop goes. Here the reveal (2.0 s) and the cut (2.73) are 0.7 s apart.

## Text removal
- Their 2nd caption line sits ON TOP of the rolled robe, which sways and then drops. cleantext pastes a STATIC patch → it would freeze a piece of the roll on screen after it drops. HOOKS.md only covers "camera moves a lot → leave text in"; it does not cover "the object moves under the text". Used that fallback: text left in the input + "Remove the caption text … completely" in the prompt.

## Set
- next-set → character-07 (real, natural, face visible, sweater) + room-18 (real American basement living room, black leather sofa, gifts, tree, 1200x1600). Both OK first time. Room check: sofa yes, floor space yes.
- Input for Kling: 2.73 s + frozen tail to 3.0 s (same "cut at a whole second" problem as video 1: 2.73–3.0 of the reference is already their next shot).

## B-roll (28 credits, try 1)
- broll-check: 3 cuts (0.96, 3.58, 4.92) = motion clip, no problems. Shot 1 back with hood/ears/hat; shot 2 hood face, ONE wide pouch this time (video 1 had two cones), she steps over the top edge right then left, feet stay in; lying + sitting on the black leather sofa, legs covered. Face ≈ character-07. Accepted.

## Hook (Kling video-edit 3 s = 12 credits, try 1)
- Our camel roll with white trim at both ends held overhead in room-18, woman = character-07 in the B-roll pajamas (9i), unroll starts on the SAME frame as the original (1.83 s), robe hangs full length showing the back + hood with ears and Santa hat — reads as a hooded robe, not a blanket. Their caption removed by Kling with no smudge. No cuts → retime x1.00.
- `tools.py compare` could not be used meaningfully (one 30-frame row); my own `vstack` of the two strips crashed because the reference is 720 px wide and ours 1080 px — compare.py handles it, but its output is a single row again.
- Kling video-edit returns 3.04 s; fine.
- Rule 13 budget line says "hook 4 s = 16"; real hook here 3 s = 12.

## Edit
- Connector: next-set printed connector-tree-1 for this video, but only because I ran next-set before logging video 1 (rotation reads the LAST logged video). Used connector-tree-2 = the real rotation. Kit should say: run `log` immediately at delivery, before the next next-set (or next-set should look at what is in progress).
- Song-only original → music from 0 (Bublé, quiet intro −35 dB) with the drop (35.35) on the reveal at 2.0 s → loud −12.6 dB from the reveal. No voice, no `audio: true`.
- Final 13.95 s, cuts 2.733 / 6.1 / 8.933 / 10.833 / 11.967 = montage line. 12 frames around hook→B-roll cut: clean, no flash, and the story flows (she holds the robe up → next shot she is wearing it from behind).

## My own frame-by-frame check of the FINAL vs the reference
OK: hook action + timing identical (roll overhead, unroll at 1.83, full length at 2.0, cut at 2.73), product = our robe one to one (back embroidery, hood, ears, hat, white trim), woman/room continue into the B-roll (9i), no text, B-roll robe/hood right, feet in and staying in, lying/sitting legs covered, connector fully joined, remote lights, cozy end clean, 13.95 s.
WRONG / not perfect:
1. Suggested text says "Princess fan" on a SNOOPY video (rule 9 "word for word" vs "swap the product").
2. In the B-roll pocket shot her bare foot is briefly on the floor next to the pouch before stepping in (approved Snoopy action per 9k, but it is visible).
3. During the unroll (frames ~1.9 s) the hood flips/morphs for ~2 frames (ears appear before the hat) — Kling interpolation, only visible frame by frame.
4. Her face is hidden behind the hanging robe at the end of the hook (same as theirs) — fine, but the first time we see her face clearly is in the B-roll.
5. Hook is 2.73 s: shorter than the kit's own "hook 3–7 s" rule.

## Credits (estimate, kit prices; balance shared with the parallel session)
B-roll 28 + hook 12 = ≈ 40 credits. No Seedance (no speech), no images, no redo.
