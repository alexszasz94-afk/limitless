# Rețetă Grinch earbuds — Kling 4.0 video-edit pe reel-uri cu alte căști (19 nov 2026, PRIMUL TEST, încă nedovedit)

Stare: scrisă înainte de prima generare. Se marchează „dovedit” doar după ce Szasz aprobă rezultatul.

## Setări
`kling4_0`, mode `video-edit`, 1080p, 9:16, duration = lungimea inputului (secunde întregi; `tools.py hookinput` → fără sunet, ultimul cadru înghețat). Media: video_references = inputul; apoi imaginile în ordinea de mai jos.

## Reguli de produs (v2, Szasz 19 nov)
- Urechea DREAPTĂ a ei = capul de Grinch cu căciulă (Image 1). Urechea STÂNGĂ = fundul cu piciorușe (Image 2).
- Din ce locaș iese casca în original decide ce referință de carcasă folosesc: dacă iese din locașul DREPT și trebuie capul → carcasa oglindită (`case-pair-flipped.jpg`, cap în dreapta); dacă iese din STÂNGUL și trebuie fundul → tot cea oglindită; dacă iese din stângul și trebuie capul → cea normală.
- Personaje: fete albe, brunete sau blonde, din `creator-kit/library/characters`; haine de Crăciun. Fără căciulă/bentiță peste urechi.
- Cameră în original → camera Grinch (`room-grinch-bedroom`). Avion / aeroport / stradă rămân, dar alte persoane.
- Textul de pe ecran se scoate în Kling și se pune la montaj.

## Imagini (ID-uri Higgsfield)
- head-in-ear (Szasz) `b1e4b9c6-1411-403e-89ad-53ed984a501f`
- butt-in-ear (Szasz) `f6fe037e-b1d4-488c-b85c-3d0788e6aa1b`
- case-pair normal (cap stânga, fund dreapta) job `134c3b2b-0976-4e1e-93cb-58bccb36420c`
- case-pair oglindită (fund stânga, cap dreapta) `705b95ff-752d-49d4-8460-7832bd5fbdb6`
- held-head job `28257601-31da-4988-a6b7-eb3dee2c74b7`
- held-butt job `35b743a7-306b-414e-aeef-4ffc61ac6b70`
- room-grinch-bedroom job `1080c5c2-9cbe-48f5-9f64-6658a8aebb89`
- fete: character-05 `0de9cf61-9db9-4e1a-b942-1e4d1f67a3f9`, character-30 `4eb5b46e-839d-4ff7-94ec-4b842c34b853`, character-02 `6401e023-99a0-4fd4-8e4f-9521933e7c6c`

## Blocul PRODUCT (identic în toate)
"PRODUCT, in every shot: the <ORIGINAL EARBUDS> of the input become our novelty earbud pair, reproduced one to one from the reference images. The pair is NOT two identical earbuds: one earbud is the green furry Grinch head of Image 1 (yellow eyes, sly grin, red Santa hat with white fluffy trim and pom-pom); the other earbud is the furry bottom of Image 2 (a round ball of the same green fur with two tiny green feet, no face, no hat). She always wears the Grinch head in her RIGHT ear and the furry bottom in her LEFT ear. Each earbud is the size of a normal earbud and has a short nozzle with a white silicone tip on its hidden side, which goes into the ear. The charging case is the glossy forest-green rounded case with a cream interior of Image 3. Nothing of the original earbuds or the original case remains, no brand name on the case."

## A — Df5QWLKokSO (Hello Kitty → Grinch), input `252cc0d1-d119-4038-bc4e-1a7eb141ac44`, duration 12
Imagini: 1 head-in-ear, 2 butt-in-ear, 3 case oglindită, 4 held-head, 5 character-05, 6 room-grinch-bedroom.
Prompt: vezi PROMPTS-USED.md (se completează din job după generare, cuvânt cu cuvânt).

## B — Df4SMoEyWW5 (frog + muscle man), input `f76da41a-c7b1-4add-b278-82ce743b8fa1`, duration 12
Imagini: 1 head-in-ear, 2 butt-in-ear, 3 case oglindită, 4 held-butt, 5 character-30, 6 room-grinch-bedroom.

## C — Df1ry_FyQS6 (frog + grandma + airport), input `ecb45949-f633-47a3-a7d1-cddd085a3f87`, duration 13
Imagini: 1 head-in-ear, 2 butt-in-ear, 3 case normală, 4 held-head, 5 character-02.
