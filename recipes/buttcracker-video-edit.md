# Rețetă Buttcracker — Kling 4.0 video-edit pe un viral cu alt produs (6 nov 2026, v1/v2 aprobate de Szasz ca test)

## Setări
`kling4_0`, mode `video-edit`, 1080p, 9:16, duration = lungimea inputului (secunde întregi; `tools.py hookinput ref.mp4 <durata> in.mp4` → fără sunet, ultimul cadru înghețat până la secunda întreagă), `declined_preset_id` dacă apare. ~4 credite/s (15 s ≈ 60).
Media în ordine: video_references = inputul; Image 1 = produsul `bed865e3-a7cf-4d7f-b400-b44b9a190afe`; Image 2..N = oamenii (Pinterest, ≥1080, reali), apoi camerele.

## Înainte (OBLIGATORIU — la v1/v2 s-a sărit, nu se mai sare)
Analiza Higgsfield `video_analysis_create` pe original + cuts + foaie 4 fps → `products/buttcracker/ref/analysis-<id>.json`. Harta obiectelor: produsul lor → nutcracker-ul nostru; scenele și timpii din analiză.

## Prompt v1 (de pe originalul cu alt produs) — cuvânt cu cuvânt, se schimbă doar <...>
Blocul PRODUCT (nu se schimbă):
"PRODUCT, in every shot: the <green plush toy> of the input becomes the plush nutcracker tissue holder of Image 1, reproduced one to one - tall black velvet hat with gold braid and a gold leaf emblem with a red jewel, peach face with black curled moustache, blue eyes, white teeth, fluffy white hair and beard, red velvet jacket with gold trim and gold fringed epaulettes, white plush trousers, black boots with gold bands; a white tissue sticks out from between the two halves of its white trousers at the back. Nothing <green>, no <green character> anywhere."

Prompt complet v1 (originalul @grinchtissue DfFlgmHhxAJ, tăieturi 2.0/3.5/4.6/6.6/10.1):
"Edit the input video. The output has exactly the same length as the input video, with the same five scenes, the same camera moves, the same actions and the same cuts at 2.0, 3.5, 4.6, 6.6 and 10.1 s. Change the product, the people and the places; keep the comedy and the timing one to one.

PRODUCT, in every shot: the green plush toy of the input becomes the plush nutcracker tissue holder of Image 1, reproduced one to one - tall black velvet hat with gold braid and a gold leaf emblem with a red jewel, peach face with black curled moustache, blue eyes, white teeth, fluffy white hair and beard, red velvet jacket with gold trim and gold fringed epaulettes, white plush trousers, black boots with gold bands; a white tissue sticks out from between the two halves of its white trousers at the back. Nothing green, no green character anywhere.

SCENES, second by second, identical to the input:
0-3.5 s: a big Christmas aisle in a home-goods store with tall shelves full of red and gold Christmas decorations and garlands (a different store from the input, warm white light): the man of Image 2 - a completely different person from the input: his face, curly brown hair, his blue-green-orange Christmas sweater, jeans - laughs so hard he bends over, sinks down and rolls on the floor laughing, then points at something off camera.
3.5-4.6 s: fast pan to a wall display: many of the plush nutcrackers of Image 1 hanging in rows on a pegboard, their backs to the camera, a white tissue sticking out of each one's trousers, red gift bags below.
4.6-6.6 s: inside a car with a black leather seat: the plush nutcracker of Image 1 hangs by its straps on the back of the front seat headrest, its back to us; a hand pulls a white tissue out from between the two halves of its white trousers and the next tissue pops up.
6.6-10.1 s: a different hospital room (white walls, a window with blinds, a small Christmas tree on the windowsill): the old man of Image 3 - his face, grey hair and stubble - sits in the hospital bed in a light blue gown; the plush nutcracker lies on the bed tray table in front of him; he pulls a tissue out of its trousers, looks at it and bursts out laughing, throwing his head back.
10.1-15 s: a cosy dining room with a dark wooden table, a Christmas garland and candles on the table, a window behind: the man of Image 4 - his face, glasses, grey hair and short grey beard, wearing a dark green sweater - sits at the table; the plush nutcracker lies on the table in front of him with a tissue sticking out; he laughs and laughs, wiping his eyes.

NO OVERLAY TEXT: remove the white caption text at the top of the input completely in every frame - no captions, no emoji. No store logos.

SOUND - made by you, with the picture, in three layers. VOICE (layer 1): no words, only real laughter exactly where the people laugh: 0-3.5 s the man of Image 2 laughs hysterically; 7.5-10.1 s the old man of Image 3 bursts out laughing; 10.5-15 s the man of Image 4 laughs warmly. ACTION SOUNDS (layer 2): 4.8-6.6 s the soft swish of the tissue being pulled. BACKGROUND (layer 3): the quiet room tone of each place (store hum, car interior, hospital room, dining room), continuous. ABSOLUTELY NO MUSIC: no song, no beat, no melody, no jingle bells.

Natural real movements with real weight, correct hands with five fingers, no morphing, the toy keeps its exact look. Very soft natural light, true colours, no HDR, no CGI look. Everyday UGC phone video, shot on an iPhone 17 Pro Max."

(Corectură de la 29 oct, de aplicat: finalul se scrie cu blocul `prompts/blocks/new-shot-warm-iphone16.txt` + `prompts/blocks/light-soft-natural.txt` în loc de „iPhone 17 Pro Max”.)

## v2 (doar alți oameni + camere, pe ieșirea v1)
Input = ieșirea v1 (primele 15 s, fără sunet). Prima frază: "... The plush nutcracker tissue holder stays EXACTLY as it is in the input in every shot (Image 1). Only the people and the places change; keep the comedy and the timing one to one." Fără blocul PRODUCT. Camerele = poze Pinterest ca Image 5, 6 („the dining room of Image 5 (...)”).

## Montaj
- Text = textul originalului, cuvânt cu cuvânt, + 🇩🇪 (regula 6 nov), sus, tot videoul: `montage.text_png(text, cap.png, 62, 0.10)` (creator-kit/engine/montage.py) cu patch-ul pentru steag (`creator-kit/engine/buttcracker_cap.py`).
- Sunet: râsetele Kling 0.8 + muzica originalului 0.7:
`ffmpeg -ss 0.07 -i out.mp4 -i ref.mp4 -i cap.png -t <L> -filter_complex "[0:v][2:v]overlay=0:0[v];[0:a]volume=0.8[a0];[1:a]atrim=0:<L>,asetpts=PTS-STARTPTS,volume=0.7[a1];[a0][a1]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 17 -preset medium -c:a aac -b:a 192k buttcracker-vN.mp4`
