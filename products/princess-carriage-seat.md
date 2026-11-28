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

## 4K (25 nov, Szasz: „dă-i upscale la 4K”)
- Finalizarea Seedance din draft: 4K = 373 credite, 1080p = 220 (sold 182) → NU. S-a făcut upscale bytedance 4K aigc 30 fps pe pilot 3: job 10ef5946-879d-41c1-a467-3f8280baf5da → `video/pilot3-4k-upscale.mp4` (2160x3840).
- `video/princess-v1-4k-letitgo.mp4` — text de prințesă + „Let It Go” (creator-kit/music/xmas, refrenul 58.5 s pe tăietura de la 1.54 → start 56.96).
- `video/princess-v1-4k-nomusic.mp4` — fără muzică, pentru sunetul pus din aplicație.
- Szasz vrea piesa cu „across my memory” = „Once Upon a December” (Anastasia) — nu e în repo; se pune din aplicație sau o trimite Szasz ca mp3.

## 27 nov — cont Higgsfield nou (alt workspace): ID-urile vechi nu mai merg; referințe reîncărcate
concept-v3a 2dbed5e6-287b-4b7c-b899-7d0cc5b83c0d · logo-b 2ec48442-d5de-4147-b6e1-606d605e0806 · ref1 66c28e09-2a16-41bc-bae4-19994ad82552 · ref2b-back-a e556eebf-9fc2-4a3f-822c-35662f07b802 · ref5-plastic 9face17e-a09f-4c68-b107-af787e0d3173 · original-notext.mp4 19f4b7b6-3073-4db2-970f-c944d22a5cb5 · character-44 (Unsplash, eșarfă roșie) 7894a551-7605-44b3-be6f-50762e4b97ca · character-45 (Unsplash, blondă pungi) ad5d8d97-79ef-489d-9fc3-6e853b8332e2

## Cutia produsului
| box-a (cutie dreptunghiulară, text „Princess” stricat) | 54d78369-acd5-4f8c-b8f8-b097431bc9a1 | box/box-a.png |
| box-b (trăsură, avea câine înăuntru) | c4552914-8778-4ac3-8784-8659353dc31d | box/box-b.png |
| **box-b-empty = ALES** (trăsură, doar scaunul) | 9d034530-59c3-4334-ad57-54e2b524dbfc | box/box-b-empty.png |

## Hook Target (Szasz 27 nov: fată „de pe Pinterest” în Target de Crăciun vede cutia, se minunează, cadrul trece pe raft)
Szasz: „mai caută și alte fete, tu tot astea le folosești” → fete noi de pe Unsplash (character-44/45 în creator-kit/library/characters, sursa în SOURCES.md).
| start frame v1 (character-44 în Target, raft cu box-b) | 71697fd1-7dea-4595-b27a-f478fb654de6 | hook-target/startframe-v1.png |

## B-roll 2 (alt interior + alt câine): SUV crem + Pomeranian lila
| ref6 SUV crem + Pomeranian | aae34eb1-033b-48c6-95d7-329dd89d2bfb | refs/ref6-suv-pomeranian.png |
Video: Seedance video_edit draft 480p, job ce7589c6-50ca-4c59-ba71-fc9966b7db70 (în lucru).
- B-roll 2 GATA: `video/broll2-suv-480p-draft.mp4` (SUV crem, Pomeranian lila, fără text; la final nu se vede șoferul).
- Start frame v2 fără produs (Szasz: „să nu se vadă cutia la început”): job 40a3ab53-a6b8-441a-ad19-19399e87c9d6 → hook-target/startframe-v2-noproduct.png
- Hook animat: Seedance 2.5 omni_reference, start_image = v2, refs = box-b-empty + startframe-v1 (raftul), 5 s, draft 480p, cu sunet. A = 6f95a492-b09c-4f67-a748-2cf238285fde (ALES: merge, observă, mâinile la gură, camera pe raft, aproape de cutii), B = eb906cb9-9303-4da7-9403-a4eb0bbd0b74 (mai lent).
- Montaj: `hook-target/princess-target-v1-480p.mp4` = hook A 0–5 s + B-roll 2; text hook „Dog moms… RUN to Target 🏃‍♀️👑”, text B-roll „Jk, we make them 🤭 (link in bio) 🎀” (pattern dovedit „RUN to Costco” + „Jk, we make them” din library/insights). Sunet: doar sunetul hook-ului; muzica („Once Upon a December”) se pune din aplicație.

## 27 nov — FINAL Target 4K (Szasz: „al doilea e bun dar trage prima secundă”, text ca înainte, 4K = upscale)
- Hook B (eb906cb9) tăiat de la 1.0 s → upscale bytedance 4k aigc 30 fps: c21118ed-3900-4ae2-afa2-58bd330a268b → hook-target/hook-b-4k.mp4
- B-roll SUV upscale 4k: ce441a06-1d6d-42ac-bd2c-610f651cf54e → video/broll2-suv-4k.mp4
- `hook-target/princess-target-4k-letitgo.mp4` (2160x3840, 14.6 s): hook 4 s + B-roll 10.6 s; text „“Babe she’s a DOG, not a princess”🙄” + „Me: 👑🎀” tot videoul; sunetul fetei din hook + „Let It Go” (încet sub hook, refrenul 58.5 s pe tăietura de la 4 s → start 54.5).
- „Once Upon a December”: YouTube cere login (bot check) → nu se descarcă; Szasz poate trimite mp3-ul.
- Finalizarea Seedance la 4K (140 + 373 credite) NU s-a pornit (Szasz: „nu da drumu”, „mereu upscale facem”).

## 27 nov — Gift reel (copiat după @ruhrohrides DgOo043xRwT, Scooby van seat, 32.354 like-uri / 246 comentarii)
- Original + analiză: `ref2/original.mp4`, `ref2/analysis-23d86586.json`; input fără text `ref2/original-notext.mp4` (delogo x10 y215 1060x225), media d065aea5-4a36-4479-a333-9e247aba2474.
- Seedance video_edit draft 480p: cce7691a-6039-4561-a90c-c26398c8f10f — dormitor roz de prințesă, blonda character-45 aruncă un cadou roz cu fundă aurie, Cavalier King Charles în pulover roz, mașină cu interior gri, fără text.
- Upscale 4K: 2987b065-098d-4c87-b443-b92c917033db → `gift-reel/gift-4k-upscale.mp4`
- FINAL: `gift-reel/princess-gift-4k-letitgo.mp4` (2160x3840, 12 s): text „“The perfect gift for a dog mom doesn’t exi-” 🤭👑” până la 10.33 s, apoi „Comment “PRINCESS” to get one 🎀 or tap the link in bio”; „Let It Go” cu refrenul pe deschiderea cadoului (2.67 s → start 55.83).
- Atenție: tabloul cu castel din dormitor seamănă cu castelul Disney.

## 28 nov — încă 3 videouri (Szasz: store hook + gifting + problem vs solution; doar fete americane, poze la rezoluție mare)
Personaje noi Unsplash (rezoluție completă): character-46 (store, căciulă neagră) 23cf12b9-ff19-4d3f-9fea-0156797d09ca · character-47 (gift, pulover verde) 565ca987-164f-4119-a153-1098d5a0dfea · character-48 (mașină, hanorac mentă) 4b6f1e8a-97ef-4984-86f7-e65ebfcf445e.
LECȚIE: concept-v3a (cu Maltezul alb) ca referință de produs face ca TOȚI câinii să iasă albi (Yorkie și Maltipoo au ieșit albi). De acum ca referință de produs: ref1-front-empty (scaun gol), nu concept-v3a.
1. `v3-store2/princess-store2-4k.mp4` (14.85 s): start frame 3b82a510 (fără produs) → hook Seedance omni 480p A 1c074095 (tăiat de la 0.75 s) + B-roll mașină albă (video_edit 10b2185e; câinele a ieșit alb, nu Yorkie). Upscale 4K: bd360163 / da8be90a. Text: „POV: Target finally made a princess car seat for your dog 😭👑” → „Jk, we make them 🤭 (link in bio) 🎀”. Let It Go cu refrenul pe tăietura de la 4.25 s.
2. `v4-gift2/princess-gift2-4k.mp4` (12 s): video_edit c1bbd6a7 pe reelul Scooby (living cu brad, character-47, cadou alb cu fundă roșie, mașină neagră; câinele alb, nu Maltipoo). Upscale 82ba1c2b. Text: „When your bestie knows you’re a dog mom 😭🎀” → „Comment “PRINCESS” to get one 👑 or tap the link in bio”.
3. `v5-problem/princess-problem-solution-4k.mp4` (15.6 s): problema = start frame a6075dd6 (SUV crem, character-48 în dreapta cu Pomeranianul în brațe) → Seedance omni 480p A dfc3a8c5 (cățelul sare spre geam în mers, ea îl prinde) + soluția = B-roll SUV crem 4K (ce441a06). Upscale 20f4275e. Text: „The problem 😩” → „The solution 👑🎀”. Sunet: drumul + vocea ei în problemă, Let It Go din soluție.
- 28 nov — problem v2 (Szasz: geamul deschis, cățelul sare pe geam din mers, stăpâna deschide ușa și se aruncă după el; ea stă pe telefon, altfel n-are sens): start frame f231ce83-a214-495a-91e8-dee4aeefc84e (ea pe telefon, geam deschis, zăpadă) → Seedance omni 7 s A a45ad9a8-9dd3-4b13-bb85-92bf9bd0c64b (cățelul zboară în nămete, ea scapă telefonul, deschide ușa din mâner și sare după el) → upscale 4ba18574. FINAL: `v5-problem/princess-problem-solution-4k-v2.mp4` (17.6 s). Încercări respinse: f9248c2f (mașina încet, gazon), 924aede6/c1107f68 (fără telefon).
