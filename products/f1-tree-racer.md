# F1 Tree Racer — concept nou de produs (23 oct 2026)

Ideea lui Szasz: ca trenulețul de sub brad, dar o mașină de Formula 1 care merge pe o pistă **agățată în brad**, în spirală printre crengi.
Culori ca mașinile reale de F1, **fără logouri / sponsori / numere** (regula lui Szasz, 23 oct).

Stare: concept. Pe web nu există încă produsul (căutat 23 oct) → fără furnizor, fără dovadă de cerere; de verificat filtrul din `docs/09`.

## Referințe Higgsfield (gpt_image_2, 9:16, 4k) — de aprobat de Szasz
| Culoare | Job ID | Fișier |
|---|---|---|
| roșu + negru | 75dd9289-498a-4198-9683-d0275244109d | refs/rosu.jpg |
| papaya + negru | 8f8a1716-6e2c-4b51-9591-9d9a4203c9e3 | refs/papaya.jpg |
| albastru închis + roșu/galben | 45cbcbe5-98f8-45b1-8eb8-e115679e5a10 | refs/albastru.jpg |
| argintiu + turcoaz | 3dd7722f-3dfb-4238-a950-4480abf47099 | refs/argintiu.jpg |
| (respinse: livrea de Crăciun cu nr. 25) | 5e9339bd…, ddef86eb… | — |

## Urmează (după ce alege culoarea)
Restul setului (~7 × 15 credite): față, spate, lateral, detaliu, pista întreagă în brad, mașina pe pistă cu lumini, cutia, telecomanda/pornirea.

## Produsul întreg (23 oct) — pentru furnizor
Fișa tehnică: `products/f1-tree-racer/supplier-spec.md` (EN).
| Ce | Job ID | Fișier |
|---|---|---|
| bradul cu toată pista | a45207b6-d6b7-4d0c-8cda-54d21dfbbe5e | refs/1-brad-intreg.jpg |
| setul complet | 9371bef6-1b20-4842-abf3-995b12931f73 | refs/2-setul-complet.jpg |
| mașina de dedesubt | 5ac8da95-02c3-4adf-8b0d-ea3f8c1f9435 | refs/3-dedesubt.jpg |
| pista detaliu | f6435f55-7c44-4ea5-b064-0ab9ad8f0c0c | refs/4-pista-detaliu.jpg |
| cutia | ecb44d9d-8502-4a1e-9608-d020e4d5c8f2 | refs/5-cutia.jpg |

## 23 oct — Szasz: pista pe UN SINGUR CERC (nu în spirală de sus până jos)
Inel orizontal de ~100 cm la 1/3 din înălțimea bradului, 12 curbe, colier pe trunchi + 6 brațe. Fișa pentru furnizor actualizată.
| bradul cu cercul | be51153e-7aea-45eb-a365-fd73d8da7681 | refs/1-brad-cerc.jpg |
| setul (cerc) | 47dc7524-a8db-4a2f-9503-8e45095c7666 | refs/2-setul-cerc.jpg |
(1-brad-intreg și 2-setul-complet = varianta veche cu spirală, renunțat.)

## 23 oct — Szasz: DOUĂ CERCURI (pe două rânduri)
Jos ~120 cm, sus ~85 cm, la ~40–50 cm unul de altul, câte o mașină pe fiecare (roșu jos, papaya sus). Fișa pentru furnizor actualizată.
| bradul cu 2 cercuri | a13cc587-230d-42c8-99d3-5f148875ea18 | refs/1-brad-2cercuri.jpg |
| 2 cercuri aproape | b74a1103-740d-45d1-8ed6-d742afd50e76 | refs/2-2cercuri-aproape.jpg |
Look: Szasz zice că pozele vechi par „foarte procesate”. Cauza: promptul cerea „ultra-realistic product photography, crisp, vivid”. De acum la produs: „casual unedited phone snapshot… no HDR, no over-sharpening, no glossy CGI look, a little phone noise”.

## 23 oct — SETUL CORELAT (folder `set/`) — sursa de adevăr
Toate făcute din aceleași referințe (brad a13cc587 + mașina roșie 75dd9289 + papaya 8f8a1716) și același bloc de produs `prompts/product-block.txt` (dimensiuni fixe: cercuri Ø120/Ø90 cm, 45 cm între ele, bandă 10 cm, mașină 16×6 cm).
| 1 brad | a13cc587-230d-42c8-99d3-5f148875ea18 |
| 2 două cercuri | e4b13ee3-f4e2-48a8-9970-34758ea3aa0a |
| 3 ce e în cutie | ec1db43e-01fe-4299-9e73-e4ce926ffe64 |
| 4 dedesubt | 786d3045-8ab5-4450-9950-74ffb04fb86c |
| 5 pista aproape | 4ea81109-ca50-4e75-b5e0-6bd3264bdc04 |
| 6 curent | 62794a16-262a-492d-ad2c-5ed8a86a8363 |
| 7 cutia | b890fdbf-ad94-42d7-9ef4-98f77b07afb6 |
Diferențe rămase: brațele de susținere (în 3 = suporți triunghiulari scurți, în 5 = tijă neagră); în 3 nu se pot număra exact 12+12 bucăți. refs/ = variante vechi.

## 23 oct — poza de bază refăcută (deformări + mașina nu stătea pe șanț — Szasz)
- master-v3b (aproape): 7e3b7ef8-0285-4b54-aa26-44d105af20b7 — NOUA REFERINȚĂ pentru pista (șanț + șine pe mijloc, mașina centrată)
- master-v3a (tot bradul): 8bb8c981-0163-4455-85ec-f1e146e26196
- (v2a/v2b 0fd05282 / ade0039a: cercuri bune dar fără șanț — nu se folosesc)
Szasz a cerut mașina lui Verstappen: NU replica (Red Bull/F1 = mărci, risc juridic + plăți + ip_detected). Propus: mașina navy/roșu/galben fără logo (45cbcbe5).

## 23 oct — Szasz: cele două cercuri trebuie LEGATE (urcă până sus, coboară, la nesfârșit)
Soluția (fără să se ciocnească pista cu ea însăși): exterior Ø120 urcă 1 tură (+45 cm, 12%), S sus în spate → interior Ø90 coboară 1 tură (−45 cm, 16%), S jos în spate (la 45 cm sub cel de sus) → înapoi pe exterior.
- Schema exactă: `schema-traseu.png` (generată de `schema_traseu.py`) — asta se trimite la furnizor.
- Poze AI aproximative (nu respectă exact geometria): set/spirala-fata.jpg d32c24a1-e27e-47e6-885b-26932433d341, set/spirala-spate.jpg 5ffa2356-b942-4460-84eb-45a0eb63ab85
- Fișa furnizor actualizată (secțiunile 3, 4, 5, 7, 8).

## 23 oct — schema verificată (v2) după „verifică și vezi că nu e ok”
Greșeli găsite în v1: pista nu urma conul bradului (21 cm în aer sus, 9 cm în crengi jos); pante subestimate (13,4% / 17,9%, nu 12/16); S-uri prea strânse (rază 26 cm); pozele AI arătau pistele unindu-se.
v2: pista urmează conul, urcă 50→85 cm (35 cm), urcare 12%, coborâre 16,4%, S-uri 60° (rază ~36 cm), verificare automată de coliziuni = OK. Poze AI spirala-* = NU se folosesc (geometrie greșită).

## 23 oct — poze cu traseul urcă/coboară (după randarea exactă `render_ghid.py`)
Metoda care merge: randez eu geometria exactă (ghid-0.png / ghid-35.png, încărcate fa3b62c7 / 06462855) și o dau la gpt_image_2 ca singura referință de traseu. Dacă pun și poze vechi cu cercuri plate, le copiază pe alea (713e0119 / 1c3f0b9f = greșite, cercuri plate).
- set/traseu-lateral.jpg d90fa312-3527-4185-9bc4-fb759653c10d (cea mai clară)
- set/traseu-fata.jpg cd2464ec-c0ea-46ba-9a7b-261c2b2a6e09

## 23 oct — DECIZIE FINALĂ Szasz: UN SINGUR CERC (folder `cerc/` = sursa de adevăr)
Cerc Ø110 cm la ~70 cm de la podea, 12 bucăți de 30°, bandă 10 cm, 1 colier + 6 brațe, 1 mașină, 1 mâner. Fișa furnizor actualizată.
Făcut din randarea exactă `render_cerc.py` (cerc-intreg bfda5818 / cerc-aproape 731fe882).
| 1 brad cu cercul | 9a60026b-843b-4ebd-81c4-578fa0c32a8b (mașina centrată; vechi 180d6df0) |
| 2 cerc aproape | bee6a0a9-d6d5-4380-960b-8345444e1a4b (mașina centrată; vechi 468225f3) |
| 3 ce e în cutie | 17630469-9f09-4202-bf3a-17b4c65cf1a5 |
| 4 dedesubt | 786d3045-8ab5-4450-9950-74ffb04fb86c |
| 5 curent + mâner | d5a295ab-c68d-4f89-87a7-3693a3ec6c3d (mașina centrată; vechi 7f2cd52a) |
| 6 cutia | c4605339-6346-43bd-8cc2-ccd10f7cc489 |
Variantele cu 2 cercuri / spirală (set/, schema_traseu.py) = abandonate.

**REGULĂ (23 oct, Szasz): mașina stă mereu FIX pe mijlocul șinei** (centrată pe șanț, spațiu egal stânga-dreapta). Se pune în prompt (vezi `prompts/product-block.txt`) și se verifică mărit la QA.
| 7 close-up (lumină extra moale) | 94587f16-cea0-4f79-b76c-94e617767dad (prima variantă 9f85ad5e = mașina descentrată) |
| 8 POV pilot | 6029104c-6c0e-4d1b-83a4-259b7c01ca88 |

### Idei ca produsul să fie mai spectaculos (propuse 23 oct, de confirmat cu Szasz)
1. LED-uri în marginea transparentă a pistei, care se aprind în urma mașinii (efect „circuit de noapte”).
2. Semafor de start F1 (5 lumini roșii care se sting → mașina pleacă).
3. Sunet de motor F1 care crește cu viteza.
4. Faruri + lumină roșie de ploaie pe mașină.
5. Linie start/sosire în carouri + garaj de boxe în formă de cadou.
