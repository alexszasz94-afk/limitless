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
