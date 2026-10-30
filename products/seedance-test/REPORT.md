# Seedance 2.5 hook test (30 oct)

Same character/room/robe as the kit's Kling versions (kit-test/output). Each `<name>/compare.mp4` = original | kit Kling hook | Seedance hook (Seedance audio).

| Reel | Result | Credits |
|---|---|---|
| snoopy-frozen (Deuu2AXyPPx) | Seedance wins: reveal 4.2 s (orig 4.2), HEATPUP sharp, voice "Three / twooo / ooone" stretched like the original, lips in sync. Video-ref variant refused (ip_detected); start-frame variant passed. | 99 |
| snoopy-rollrobe | Seedance refused all 3 tries (ip_detected) on the Snoopy robe. Note: Deui1RKgYWF is an IKEA reel; the kit's version came from DfGoo7qyJ9o (folder mix-up). | 0 |
| princess-countdown (DdGwGMEx-Uj) | Seedance start-frame wins: reveal 2.75 s, box "Princess / HEATED ROBE" sharp (Kling smeared it), face = character, words 0.32/1.28/2.14 + "Let's see how it comes out" 3.17-4.06 (orig 0.23/1.21/2.09/3.16-3.92). | 99 |
| princess-unroll (DfGoo7qyJ9o, song only) | About even: start-frame variant right timing (1.85 / 2.3 s), our robe from frame 1, but shows the sash side without the hood; Kling showed the hood back. Delivered as 480p draft. | 16 |

Total 246 credits.

## Findings
- Start frame (gpt_image_2_5) + Seedance `start_image` + original hook as `video_references` beats plain video reference: no leak of their product, face closer, passed IP filter once, better speech timing.
- Seedance refuses the Snoopy robe refs (ip_detected); Princess refs always passed.
- Prices: 1080p with video ref = 80 (5 s) / 64 (4 s); 480p draft 15/12; finalizing a draft is charged the full 1080p price. Min duration 4 s. Finalize needs the same prompt + media + `draft_job_id`.
- Video reference must be SILENT (else it copies their music).

## Recommendation
- Hooks with speech: Seedance, start-frame variant (one generation replaces Kling + blur-for-sound + Seedance sound pass + voice-to-lips). ~95-99 credits per 5 s hook vs ~40 for Kling.
- Song-only hooks: Kling (cheaper, shows the robe better).
- Snoopy hooks: Kling (Seedance refuses the robe).

## Settings
`seedance_2_5`, `omni_reference`, 9:16, duration = ceil(hook end) (min 4), `generate_audio: true`, declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612, `start_image` = GPT start frame, `video_references` = silent original hook (last frame frozen to the whole second), `image_references` = character (always), box if revealed, 2-4 robe refs (not Snoopy).

## Prompt template (princess-countdown)
```
The video starts EXACTLY on the start image: the same woman, the same <room/place>, the same <object in hand>, the same camera. Video 1 is ONLY the reference for the motion and the timing - copy its movement second by second, but never its woman, its room or its <their product>. Image 1 = the woman: her face, hair and skin tone stay exactly Image 1 and the start image. Image 2 = OUR box <under the cloth>: <short box description> - REPRODUCE THE BOX ONE TO ONE from Image 2, <BRAND> spelled <B-R-A-N-D>. Images 3-4 = the robe inside the window, REPRODUCE IT ONE TO ONE from Images 3-4. ACTION, second by second exactly like Video 1: <0.0-x s ...; at x s reveal ...; x-y s ...; push to lens ...>. She stays in the FOREGROUND, close to the camera, the camera does not move. SOUND: the woman speaks on camera, <tone>, lips in sync. EXACT TIMING: "<w1>" a-b s, "<w2>" c-d s, "<w3>" e-f s, then the <action sound> at x s, then IMMEDIATELY at <t> s she says quickly in one breath "<last line>" and FINISHES the last word by <t2> s at the latest; from <t3> s she is silent and smiles. Real sounds: <each action sound at its second>, quiet room tone. No other words, no music, no singing. LIGHT: very soft, very natural light - diffuse daylight and the warm glow of real lamps; gentle low-contrast light, soft shadow edges, true slightly warm colours; no harsh light, no HDR, no glow, no CGI look. LOOK: warm cozy colours, Full HD sharpness, shot on an iPhone 16 main camera, completely realistic UGC - a real unedited phone video, skin with real texture, correct hands with five fingers. MOTION: natural real movements with real weight and gravity, no morphing, no sudden jumps. Vertical 9:16, one continuous static shot, no cuts. No on-screen text, no captions, no emoji, no watermark.
```
Song-only: SOUND = "no voice and no words at all, nobody speaks. Real sounds only: <whoosh at x s>, quiet room tone. No music, no singing."
Unroll: add "It is the SAME robe as the roll in the start image - it only unrolls, it never changes colour or design, and it is never the <colour> robe of Video 1. The robe is never worn and never filled by an invisible body; her hands stay visible at the top."
