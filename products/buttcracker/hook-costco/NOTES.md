# Buttcracker — hook „reveal în Costco” (6 nov 2026, Szasz)
Start frame v1: GPT Image 2.6 Sunburst job `f5ce43c1-9d8c-486f-843b-b11eda87062a` (high, 9:16, 4k) → `start-frame-v1.jpg`.
6 angajați (personaje noi, toate photo-ok): character-05 (`cb0bfeb1`), character-30 (`3184e046`), character-35 (`712260bb`), Pinterest young-22 (`723863e6`), young-24 (`02bbc968`), gpa-23 (`f9aaca34`).
Verificat: depozit Costco (semne Costco, rafturi industriale, brazi), mantie roșie de catifea cu franjuri peste un raft înalt, 6 angajați în uniformă cu ecusoane, corp întreg, mâini OK.
De observat: mantia e ținută ridicată în față ca o cortină, nu stă căzută peste raft.
(Prima încercare cu personajele vechi, job 0b42f747 cu GPT 2.5, nefolosită — Szasz a cerut alte personaje.)

## v2 / v3 (Szasz: „poză dintr-un Costco adevărat”, „doar doi angajați”, „să aibă sens cum prind mantia”)
- v2: GPT 2.6 edit pe poza Pinterest c1-14 (job `0765d6ea`) — ❌ poza era de fapt WALMART (semne „Low Price”), nefolosit.
- v3 (BUN): GPT Image 2.6 edit pe poza reală Costco c2-21 (Pinterest pin e1_AfqPShyT6wbfT6UNfTY0hly21XZlmxiX3Ic_fp6nwnK8Q4YtKUL7, media `6e877149-8470-43d5-9070-d7de97e737aa`) — job `6c196050-1147-47b7-b0e5-c77258b159ab` → `start-frame-v3-costco-real.jpg`. Rafturi portocalii + paleți reali păstrați, căruciorul scos; mantia roșie aruncată peste un raft, căzută până jos; 2 angajați (blonda character-30, bărbatul cu barbă young-22) țin fiecare un colț de jos.
LECȚIE: verifici că poza „de la X” e chiar de la X (semne, coșuri, rafturi) înainte s-o folosești.

## Video v10 (7 nov) — hook Costco + B-roll 3 scene
Hook: Seedance 2.5 draft 480p 8 s, job `cf347ee6-bf03-4f70-97e9-1ba81ad2987e` (start = v3 `6c196050`, refs blonda, bărbatul, produsul): „One, two, three… Let's see how it comes out!” → trag mantia (zboară în sus) → raft cu Buttcracker cu spatele → râd, el cade pe jos ~5,5–6,5. Folosit 0–7,2 s.
B-roll (rețeta `recipes/buttcracker-broll-3scene.md`): Kling video-edit 720p job `f7d20dcb-61e9-4265-a99f-80572b7d5431` (pat: brunetă char-05; birou: young-24 + colegi; familie: gpa-23). Familia nu scotea șervețelul → refăcut image-to-video din cadrul 5,95 (media `2933a2ce`), DOAR start_image, job `6bb53b2e-2ebf-4e1d-acd4-f4bf0db2dd11` (iese la 0,9 s).
Montaj: hook 0–7,2 + br3 0–5,95 + fam2 0–3,5 = 16,65 s; bășini: fart-02 la 8,25 (pat, iese 8,3), fart-05 la 10,15 (birou, 10,2), fart-04 la 14,0 (familie, 14,05) — verificat pe spectrogramă; „White Christmas” de la 0 (0,22 sub hook, 0,55 după); text 🇩🇪. → `products/buttcracker/video/buttcracker-v10-costco.mp4`.
De observat: în pat produsul stă pe pat lângă ea (nu pe noptieră) și nu arată foarte răcită.

## v4 / v5 (7 nov)
- v4 (GPT 2.6, job `b3a9f48c`): aceleași 2 personaje, poziție naturală (drepți) → animat Seedance draft `1eda2e43-2c80-46f8-b351-3ea1284125a9` (bun: stau natural, trag mantia, raftul, râd, el cade ~6–7 s).
- v5 (Szasz: „alt start frame, alte personaje, alt Costco, editat de Crăciun”): Nano Banana Pro job `8f583000-458c-4e00-bf83-1b03bea306a4` pe poza reală Costco c2-11 (media `85b876b6`), personaje character-37 (roșcată, `934bdbe5`) + Pinterest gpa-24 (`cf295390`) → `start-frame-v5-craciun.jpg` (3072x5504). Decor de Crăciun (brazi în cutii, ghirlande cu luminițe, Moși gonflabili, semne Christmas Sale), mantia peste raft, amândoi drepți, câte un colț în mână.

## Video v11 (7 nov) — hook Costco de Crăciun + B-roll 3 scene + text nou
- Hook: Seedance draft 480p 9 s, job `ca85cd83-f235-4a78-b55e-32c59ed44242` (start v5 `8f583000`), numărătoare rară: „One” ~1,0 / „two” ~2,4 / „three” ~3,5 / „Let's see how it comes out!” 4,1–5,0; mantia ~5,3–6,0; râd ~7,8–9,0. Tăiat la 9,0 (Szasz: „se taie fix după ce râd puțin”).
- Pat (Szasz: „să tragă de pe servantă”): start Nano Banana Pro `2a9b18fe` → Kling i2v 720p 3 s, DOAR start_image, job `54245135-161e-4b2a-90ad-107a3efb95d0`; șervețelul iese ~0,75, își suflă nasul.
- Birou: br3 2,08–5,95; familie: fam2 0–3,0.
- Text (Szasz): „Nutcracker? No” / „Meet the Buttcracker 😂🎄💩🇩🇪”.
- Bășini mai încet (0,7): fart-02 la 9,70 (pat), fart-05 la 12,07 (birou), fart-04 la 16,22 (familie). White Christmas de la 0 (0,2 sub hook, 0,55 după).
→ `products/buttcracker/video/buttcracker-v11.mp4` (18,1 s).

## Video v12 (7 nov, Szasz: „produsul mai mare la fata cu servanta”, „hook mai natural, fără pauze”)
- Hook: Seedance draft 480p 7 s, job `8e85f35a-7774-445c-b975-eb1c27a78eb8` (start v5), mișcări naturale, „One, two, three!” 1,2–2,5, „Let's see how it comes out!” 2,6–3,6, reveal ~3,5, râd de la ~4,6. Folosit 0,9–7,0 (fără liniștea de la început).
- Pat: Nano Banana Pro nu a apropiat camera (a2/a64a… identic) → zoom LOCAL pe poza bună (crop 60 %, 1440x2560, media `b5b83bee`) → Kling i2v 720p 3 s, job `fe65f0cc-ef52-45ae-a0d3-53aea4d8d518`; șervețelul iese ~0,9.
- Montaj: hook 6,1 + pat 2,4 + birou 3,87 + familie 3,0 = 15,4 s; text „Nutcracker? No / Meet the Buttcracker 😂🎄💩🇩🇪”; bășini 0,7 la 6,95 / 9,30 / 13,25; White Christmas de la 0.
→ `products/buttcracker/video/buttcracker-v12.mp4`.
LECȚIE: ca să mărești produsul în cadru, decupează (zoom) local poza bună în loc să ceri modelului „camera mai aproape”.
