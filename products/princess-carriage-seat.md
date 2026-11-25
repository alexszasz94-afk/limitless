# Princess Carriage Seat — concept nou de produs (25 nov 2026)

Scaun auto de câine mic, pus pe cotieră, în formă de trăsură de prințesă (roz pal, auriu, blană albă, luminițe, roți aurii). Variația pe nișa Prințesă a saniei din reelul @itsbottomspup (`products/grinch-sleigh-seat/ref/`, 49.156 like-uri / 2.249 comentarii în prima zi, 24 nov).

De ce Prințesă: cea mai bună nișă de personaj la halate (`library/insights/variations.json`: Snow White 21,1M top, 1,38M medie). La scaune de câine nu avem încă cifră → ipoteză.

Furnizor: nu am găsit modelul pe Chewy / PetSmart / Walmart (căutat 25 nov) → probabil producție custom; nu ajunge până la Crăciun. Testăm cererea cu mockup-ul (docs/08 §2) înainte de comandă.

## Referințe Higgsfield
| Ce | Job ID | Fișier |
|---|---|---|
| concept v1 (Maltez în trăsură roz, consolă Tesla) | 7058704d-8bdc-4120-aa42-1895ff7096f1 | refs/concept-v1.png |
Ref formă: sleigh-front.jpg din reel, media e8e25599-c7bf-411b-979c-9d61da4732f9.
Notă: am cerut `nano_banana_pro`; jobul raportează `nano_banana_2` la backend.
| v2a mai pufos: fundă mare roz în spate, perne rotunde | 3b072469-bd53-4bf3-b585-98c6511760d6 | refs/concept-v2a.png |
| v2b cel mai pufos: bordură de blană albă groasă jur-împrejur, perle | 0bd5f56e-4877-4982-9cd4-a5586fc2fada | refs/concept-v2b.png |
(Prima încercare v2, jobs b9517b2f / eacb3c97, a picat ca „nsfw” fals; prompt reformulat simplu → a mers.)

## 25 nov — ALES de Szasz: v3a (fața normală, fundă mare)
| v3a ALES = imaginea principală | 24bbba15-ba32-4ec1-a337-d8d98c2e537e | refs/concept-v3a.png |
| v3b (alternativă) | 26bbc835-a743-4cac-875c-cfbb1321c825 | refs/concept-v3b.png |
(Upscale bytedance 7577063d → 2294x4096, nu e mai clar; șters. Master rămâne v3a 3072x5504.)

## Fișa de referințe (nano_banana_pro 4k, din v3a)
| Ce | Job ID | Fișier |
|---|---|---|
| față, gol, pe consolă | e8a11b96-e6be-42ae-9ccf-e8fe2e9cad90 | refs/ref1-front-empty.png |
| spate, din bancheta din spate, cu Maltezul | b08fa6db-96bc-4a4d-9ee1-bf1369c44041 | refs/ref2-back-dog.png |
| în folie, mâini în pulover roșu | 66782ffd-1db5-40dc-8c07-bb0b4d849387 | refs/ref5-plastic.png |
| lateral 3/4 + detaliu broderie | 1f08af1e / 2e4d0709 — picate „nsfw” fals, de refăcut | — |

Câinele: Maltez alb cu fundiță roz (din concept-v1/v3a).

## Pilot video 1 (25 nov) — Seedance 2.5 video_edit, draft 480p, fără sunet
Original: `ref/original.mp4` (@itsbottomspup DgJJXq2JkbD), analiza `ref/analysis-ce165c30.json`. Input = `original-silent.mp4` (media 772ac4d4-ff67-4885-8823-39a93eef4594).
Job: af865a00-78ac-44ff-8d0d-fce25e7abd80 (39 credite).
Montaj: `video/princess-pilot1-480p.mp4` — draftul mărit la 1080x1920 local, textul originalului cuvânt cu cuvânt (sus) + „Me:😂” (stânga), sunetul originalului („It's the Most Wonderful Time of the Year”).
Verificare (25 nov): produsul = referința în toate cadrele, Maltezul OK, acțiunile și tăieturile ca la original (1.54/3.5/5/6.5/7.9/9.3 vs 1.63/…/9.5).
Probleme: (1) ultimul cadru nu are șofer și pare mașina oprită (a copiat ref2 în loc de scena originalului); (2) căciula de Moș plutește pe tetieră la 6.5–8 s; (3) câinele nu poartă puloverul roz cerut.

## 25 nov — Szasz: funda e pe INTERIORUL spătarului (se vede doar din față); în spate broderie de prințesă
| spate corectat A (panou roz cu coroniță + volute aurii) | ae607926-251f-41b1-94b6-5c21b8b3b308 | refs/ref2b-back-a.png |
| spate corectat B | eca422a7-b901-471d-8d64-5cab41078802 | refs/ref2b-back-b.png |
ref2-back-dog.png (fundă pe spate) = GREȘIT, nu se mai folosește.

## Pilot 2 (25 nov) — job e27714ba-cfb2-49f9-a067-b335e0f30051: spate corectat, șofer la final, pulover roz. Probleme: a PĂSTRAT textul originalului (deși i s-a cerut să-l scoată) + câinele în folie la început (Szasz: „n-are sens”).
## Pilot 3 (25 nov) — job 802f6b14-63fc-4c30-93db-30d9426e160b — `video/princess-pilot3-480p.mp4`
- Input fără text: `ref/original-notext.mp4` (ffmpeg delogo pe text sus x110 y330 860x180 + „Me:” x160 y915 200x80), media 2df7218b-126b-4de2-a4ad-6071ea654b66. LECȚIE: Seedance video_edit copiază textul ars din input chiar dacă promptul zice să-l scoată → textul se șterge ÎNAINTE din input (delogo).
- Început: scaunul GOL în folie (fără câine).
- Text nou (Szasz: alt text, emoji de prințesă): sus „“Babe she’s a DOG, not a princess”🙄”, stânga „Me: 👑🎀” (`video/cap2.png`, montage.text_png 72px).
- Sunet: piesa originalului (de schimbat înainte de postare).
