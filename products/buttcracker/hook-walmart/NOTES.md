# Buttcracker — hook nou „doamna cu cafeaua în Walmart” (6 nov 2026, cerut de Szasz)

Start frame v1: GPT Image 2.5 job `f2e9e654-95e5-4296-80de-fdbe4ea42889` (high, 9:16, 4k) — `start-frame-v1.jpg`.
Personaj: `creator-kit/library/characters/character-25.jpg` (media `5e18cbb5-f993-4fde-9d40-006c7df4767b`), verificat photo-ok 1080x1920.
Verificat: aceeași față, în prim-plan, cafea mare roșie de Crăciun fără logo, holul de Crăciun Walmart (semnele Walmart sus), mâini OK, lumină moale.
Urmează: Szasz aprobă / corectează, apoi animare Kling 4.0 image-to-video + restul videoului ca la v1–v3.

## v2 (Szasz: „mai de la distanță, o fată și un băiat”)
GPT Image 2.5 job `4dea3580-2be3-4af7-9066-04adea5e0734` → `start-frame-v2-cuplu.jpg`.
Fata: `creator-kit/library/characters/character-07.jpg` (media `43a36543-f52d-4897-bbbf-a39570ad2651`). Băiatul: Pinterest „candid photo young man christmas sweater” (media `3203f00b-0acf-42a1-bdb4-4f29177231ec`, 1366x1707, photo-ok).
Verificat: ambele fețe ca în referințe, corp întreg, în prim-plan, semnele Walmart sus, pahar roșu de Crăciun fără logo, mâini OK, fără text lizibil pe pulover.

v2 cald (Szasz: „fă mai caldă imaginea”): același cadru, doar culoare mai caldă local (ffmpeg colortemperature 4300 mix 0.55 + colorbalance spre roșu/galben), fără regenerare → `start-frame-v2-cuplu-cald.jpg`. Fețele rămân identice.

v3 (Szasz: „din Higgsfield mai caldă” + „mai clară”): GPT Image 2.5 edit pe v2 (job `7cfa249e-5a52-496b-8d3a-67ab2905bd04`, refs: v2 + fata + băiatul) → lumină caldă aurie, luminițe pe brazi; apoi upscale bytedance 4k (job `b9ae5bfb-74df-4030-bb6f-b6759ad1c43a`, 2304x4096) → `start-frame-v3-cald-clar.jpg`. Verificat: aceleași fețe, aceeași încadrare, pielea naturală, semnele Walmart rămân.

## Hook animat + video v4 (6 nov)
Szasz: „merg spre cameră, se opresc, ea scapă cafeaua, arată spre raft, amândoi râd tare, apoi camera arată raftul cu produsul”.
Kling 4.0 image-to-video 1080p 6 s, job `e407e20c-f9cb-414a-9da3-15238b963e20` (start_image = v3 cald-clar `b9ae5bfb`, refs: produs bed865e3, fata, băiatul), sunet în 3 straturi, fără muzică (spectro OK).
Verificat la 4 fps: 0–1,75 merg; ~2,0 cafeaua cade și se varsă; ea arată; 2,5–3,7 râd tare amândoi; ~3,75 whip-pan. ❌ raftul din hook (4–6 s): spărgătorii cu fața, șervețelul prin față → NEFOLOSIT.
Montaj v4: hook 0–3,8 + v3 3,7–6,72 (whip-pan → raftul cu spatele, mașina) + v3 7,96–15,04 (spital, bucătărie); text 🇩🇪, râsete 0.8 + muzica originalului 0.7. 13,9 s → `products/buttcracker/video/buttcracker-v4-walmart.mp4`.

## Hook Seedance + video v5 (6 nov, Szasz: „fă cu Seedance, mai realist, ea să cadă pe spate”)
Seedance 2.5 omni_reference, start_image = v3 cald-clar (`b9ae5bfb`), refs fata + băiatul, 5 s, audio generat. Draft 480p `223271d7-c09b-41c0-b63d-1455f7cbf5d6` → final 1080p `d098d805-79d5-439c-8c84-db9d68b4b824` (`hook-seedance-1080p.mp4`). Prompt = cel din job (timeline pe secunde + SOUND fără muzică).
Verificat la 4 fps: merg 0–1,7; cafeaua cade ~1,8 și se varsă; ea arată spre dreapta; râde și cade pe spate ~2,8–3,7; el se îndoaie și arată spre dreapta 4,2–5. Fețe constante, fără muzică. Camera NU face whip-pan la final → tăiat direct pe whip-pan-ul din v3.
Montaj v5: hook 0–5,0 + v3 3,7–6,72 + v3 7,96–15,04; text 🇩🇪; râsete 0.8 + muzica originalului 0.7 (fade 13,2–14). 15,1 s → `products/buttcracker/video/buttcracker-v5-walmart-seedance.mp4`. Tăieturi 5,0 / 6,08 / 8,04 / 11,5.

## v6 (6 nov, Szasz: primul start frame cu culoarea inițială, aceeași acțiune, raftul frumos din aceeași filmare; B-roll nou cu persoane/acțiuni noi; fără 1080p)
Hook: Seedance 2.5 omni_reference DRAFT 480p, 7 s, job `be6dbe98-f97a-4d47-9faa-50e5ba145d98`; start_image = `4dea3580` (v2 cuplu, culoarea inițială), refs fata, băiatul, produsul bed865e3. O singură filmare: merg → cafeaua cade ~1,8 → ea cade pe spate ~2,5–3,5 → el arată → camera se întoarce 4,5–5,3 → raft Walmart de metal cu spărgătorii cu spatele, șervețelele afară.
B-roll: Kling 4.0 video-edit 720p, 10 s, job `72e974e6-3880-4fbd-b852-8e30520531b3`, input = original 4,6–14 s fără sunet (media `7338f6d7`); refs produs, femeie roșcată (character-13, media `1a4f1b3a`), bunic cu ochelari (Pinterest gpa-04, media `3b6fe2d5`). Scene: mașină bej + mână cu unghii roșii; femeia la birou trage șervețelul și râde; bunicul pe canapea lângă brad râde și își șterge ochii. Tăieturi 2,08 / 5,54 (original 2,0 / 5,5).
Montaj: hook 0–6,6 + B-roll 0–10, scalat local la 1080x1920 (fără generare 1080p), text 🇩🇪, râsete 0.8 + muzica originalului 0.7 (prelungită cu crossfade). 16,6 s → `products/buttcracker/video/buttcracker-v6.mp4`.

## v7 (6 nov, Szasz: „bășinile pe momentul când scoate” + „la unul nu i-a ieșit șervețelul”)
- Bășinile din sunetul originalului: 5,55–5,85 / 6,2 (mașina), 7,4–7,8 / 8,1 (spital), 10,8–11,1 (masa) — găsite cu energia 40–250 Hz.
- B-roll-ul Kling e video-edit pe originalul 4,6–14 s → tragerile cad pe aceleași secunde ⇒ sunetul originalului se pune DECALAT: video = original + 2,0 s (hook 6,6 s − 4,6 s).
- Bunicul (șervețelul nu ieșea) refăcut: Kling 720p 4 s, job `80ac0d37-dead-4b77-aeec-58469134a993`, input original 10,07–14 (media `c5ac3b12`); șervețelul iese la 1,4 s → folosit 0,69–4,04 ca ieșirea să cadă pe bășina de la 10,8.
- Verificat: mașina iese 7,7 ↔ bășină 7,6–7,75; biroul 9,6 ↔ 9,4–9,8; bunicul ~13,0 ↔ 12,8–13,05. 15,5 s → `products/buttcracker/video/buttcracker-v7.mp4`.
REGULĂ de metodă: la orice B-roll Buttcracker făcut cu video-edit pe original, sunetul originalului se pune decalat cu (lungimea hook-ului − secunda din original unde începe B-roll-ul), apoi se verifică fiecare tragere ↔ bășină.

## v8 = v7 la 1080p (6 nov, Szasz: „e ok, dă upscale la 1080”)
Hook: Seedance final 1080p din draft-ul aprobat be6dbe98 → job `eca72ebe-a076-45c3-88a8-13e33a8792ab` (aceeași mișcare). B-roll: upscale bytedance 1080p aigc 24fps → `05ab9a6e-9132-46af-afd3-f69a470de743` (mașină/birou/bunic) + `8198d5a8-0672-49a6-a8cc-5ec2c5b79a50` (bunicul refăcut). Montaj identic cu v7. Verificat: tăieturi 6,62/8,71/12,17, bășini 7,6 / 9,4–9,8 / 12,8–13,0. → `products/buttcracker/video/buttcracker-v8-1080p.mp4` (FINAL aprobat).

## v9 (6 nov, Szasz: „la bătrân tot nu iese bine șervețelul”)
Problema (zoom 8 fps): șervețelul era apucat din lateral, se deforma și rămânea agățat de spate.
- Încercarea 1: Kling image-to-video din primul cadru + refs produs & bunic (job `7a5852d6`) → ❌ Kling a tăiat spre o masă și spre fotoliul roșu din poza bunicului; șervețelul ca o panglică.
- Încercarea 2 (BUNĂ): Kling 4.0 image-to-video 720p, 4 s, job `66c9f9b2-7b2c-4475-9611-6ad8004e155d`, DOAR start_image (cadrul cu mâna pe vârful șervețelului, media `b1e95efa`), fără alte referințe, prompt „ONE single continuous shot… never cut to another place” + „one normal square white facial tissue… never a long ribbon”. Upscale 1080p `38371284-7849-4d36-a323-c979eb5274f0`.
LECȚIE: la image-to-video NU pune poza persoanei ca referință dacă are alt decor (Kling sare în decorul pozei). Startul ajunge.
Montaj ca v8, bunicul = gp3[0:3,34]; șervețelul iese la 12,9 ↔ bășina 12,8–13,05. → `products/buttcracker/video/buttcracker-v9-1080p.mp4`.
