---
name: aliexpress-research
description: Caută pe AliExpress produse noi bune de dropshipping, care trezesc o emoție puternică în video și se pot exagera vizual. Folosește la „research produse”, „produse noi”, „caută pe AliExpress”, „ce produs mai încercăm”.
---
# Research de produse pe AliExpress (emoție + exagerare)

Scop: o listă scurtă (5–10) de produse pe care **nu le rulează aproape nimeni organic**, care lovesc o emoție în primele 3 secunde și se pot exagera în video. Szasz alege; nimic nu intră în producție fără „da” de la el.

Argumente opționale: o nișă / un sezon / o emoție (ex. `aliexpress-research cadouri de Crăciun pentru mame`). Fără argument → sezonul de acum + evergreen.

## 0. Înainte
- Citește `docs/09-reguli-produs.md` (filtrul) și, din platformă, colecțiile `products` și `finder` — ca să nu propui ce avem deja sau ce rulează deja mulți.
- Citește `lessons` (Mistakes log).
- Research-ul e gratis (doar căutări web). Nu genera imagini/video aici și nu folosi Apify fără acordul lui Szasz pe cost.

## 1. Semințe de căutare (15–25 de căutări, în engleză)
Pornește de la **emoție**, nu de la categorie. Câte 2–4 căutări pe fiecare:

| Emoție | Ce cauți | Exemple de cuvinte |
|---|---|---|
| Cozy / căldură | senzație care se „simte” prin ecran | heated, plush, oversized, weighted, glowing |
| Cadou + reacție | cadou care scoate o reacție mare (mamă, iubită, bunic, copil) | gift for mom, personalized, surprise, keepsake |
| Nostalgie / copilărie | obiect care aduce înapoi o amintire | retro, 90s, childhood, vintage toy |
| Grijă / protecție | bebeluș, animal, părinte în vârstă | baby safety, pet, anti-fall, night light |
| Animale de companie | reacția animalului e vârful | cat, dog, pet bed, interactive pet |
| Umor / absurd | produs amuzant sau ciudat la prima vedere | funny, prank, giant, weird, novelty |
| „Prea bun ca să fie adevărat” | efect vizibil pe loc, satisfăcător | instant, magic, self-, automatic, satisfying |
| Nișă pasionată | fani care se recunosc imediat | racing, fishing, gym, golf, camping, gamer |
| Nesiguranță / problemă | problemă vizibilă + rezolvare vizibilă | posture, snoring, hair, sleep, back |
| Sezon | fereastra de acum (iarnă, Black Friday, Crăciun, Valentine's…) | christmas, winter, valentine |

Cum cauți (verificat 12 nov 2026 — merge cu WebFetch):
`https://www.aliexpress.com/w/wholesale-<cuvinte-cu-liniuță>.html?SortType=total_tranpro_desc` (sortat după comenzi).
Cere din pagină: titlu, preț, „sold”, rating, link. Dacă pagina dă captcha/login → încearcă alte cuvinte sau WebSearch (`site:aliexpress.com <cuvinte>`); nu inventa cifre.

Învățat la prima rulare (13 nov 2026):
- Paginile de produs (`/item/<id>.html`) cer login → nu se pot citi. Prețul, „sold” și ratingul se iau din pagina de căutare; livrarea rămâne „neverificat” până o verifică Szasz sau comandăm.
- Maxim ~6 căutări deodată; la mai multe, unele pagini vin goale (se reiau).
- „Nou pe piață” (estimare): numărul listării e mare (în nov 2026 cele mai noi încep cu `32568130…`–`32568134…`) ȘI apar deodată multe listări noi pentru același produs. Caută apoi numele exact al produsului ca să vezi tot valul.
- Căutarea web NU vede Instagram/TikTok → concurența organică se scrie „neverificat”; numărătoarea reală cere Apify (cu acordul lui Szasz pe cost).
- Board: pagina se generează în `products/ideas/board/` și se publică drept artifact (UI în engleză).

Surse în plus (WebSearch): „trending dropshipping products <luna anul>”, „tiktok made me buy it <nișă>”, Google Trends pe numele produsului. Astea dau doar idei — cifra de comenzi se ia tot de pe AliExpress.

## 2. Triere rapidă (aruncă imediat)
- Personaje / branduri / echipe / celebrități (IP) — afară. Forma generică e OK.
- Afirmații medicale (dureri, circulație, slăbit) — afară.
- Produse pentru adolescenți / școală / anime / scule de muncă — public fără bani.
- Fragil, foarte mare, cu baterii problematice, cu mărimi complicate (retururi).
- Rating sub 4,5 sau sub ~100 de comenzi fără nicio altă dovadă de cerere.
- Nu se poate vinde cu ≥ 38,99 $ (singur sau ca set).
- E deja în `products` / îl rulează > 4 conturi organice.

## 3. Scorul de emoție și exagerare (0–10 fiecare, total /50)
Pentru fiecare produs rămas, răspunde scurt și dă nota:

1. **Emoție în 3 secunde** — ce simte omul și cine anume (mama, proprietarul de pisică…)? Dacă nu poți spune într-o propoziție → max 3.
2. **Se poate exagera** — există o versiune „la maximum” a scenei, care rămâne adevărată despre produs? (vezi §4)
3. **Reacție filmabilă** — față de om / animal / copil care reacționează mare la produs.
4. **Se înțelege fără sunet** — în 1–3 s se vede ce e și ce face.
5. **Comentarii și share** — stârnește „îmi trebuie”, „trimite-i lui X”, ceartă sau râs.

Sub 30/50 → nu intră în listă.

## 4. Exagerare cinstită (regulă)
Exagerăm **scena, reacția și situația**, niciodată **ce face produsul**.
- DA: reacție uriașă, problemă dusă la absurd (doarme pe balcon de frig), scară comică, numărătoare 3-2-1, „Do NOT let a ___ mom see this”, 10 bucăți în loc de una, comparație cu alternativa ridicolă.
- NU: efect pe care produsul nu-l are, before/after fals, cifre neverificate, poveste falsă de „handmade”, magazin real în imagine.
- Testul: *un client care revede videoul după ce a primit produsul se simte păcălit?* Dacă da → ideea de exagerare se schimbă sau produsul iese.

Pentru fiecare produs scrie **2 idei de hook exagerat** (în engleză, text pe ecran + ce se vede), fiecare legată de un concept dovedit din `playbooks/carti-marketing-psihologie.md` §3 (3-2-1 reveal, gifting, pattern interrupt, problem/solution, reacție + unboxing…).

## 5. Verificări de dropshipping (pe ce a trecut de §3)
Deschide pagina produsului (WebFetch) și notează, cu link:
- **Cerere:** comenzi („sold”), rating, nr. de recenzii. Google Trends dacă e clar numele.
- **Cost:** preț + livrare în SUA; termenul de livrare (ideal ≤ 12 zile; peste 20 → risc de chargeback).
- **Marjă:** preț de vânzare propus (≥ 38,99 $) − cost − livrare. Țintă: costul total ≤ ~1/3 din preț.
- **Concurență organică:** WebSearch `site:instagram.com/reel <nume produs>` și `site:tiktok.com <nume produs>` + colecția `finder`. Notează câte conturi ai găsit. E o estimare grosieră → scrie „estimare”, nu cifră sigură. > 4 conturi active → doar dacă avem un unghi pe care ei nu-l fac.
- **Se poate produce:** Kling 4.0 + Nano Banana Pro îl pot reda fidel din poze? (fără text mărunt, fără mecanisme fine care driftează, fără IP)
- **Variante:** culori / teme / personalizare posibile (pentru mai târziu).

## 6. Ce livrezi
Fișier `products/ideas/aliexpress-<AAAA-LL-ZZ>.md` + rezumat în chat, în română, simplu. Pentru fiecare produs:

```
## <N>. <Nume scurt> — scor <xx>/50
Link AliExpress: …
Emoția: <o propoziție: cine simte ce>
Cifre (de pe pagină, data): preț … · livrare … · sold … · rating …
Preț de vânzare propus: … $ → marjă ≈ … $
Concurență organică (estimare): … conturi — linkuri
Hook exagerat 1 (EN): "…" — ce se vede
Hook exagerat 2 (EN): "…" — ce se vede
Riscuri: …
Ce NU știm încă: $/1M views (test order), …
```

Sus de tot: **top 3 recomandate** și de ce, într-o frază fiecare.

Reguli la livrare:
- Orice cifră are link și dată. Ce nu ai putut verifica se scrie „neverificat”.
- „Va merge” nu se scrie. Produsele sunt **ipoteze** până la cifrele noastre (pilot → `results`).
- Verifică singur lista înainte s-o trimiți: fiecare link se deschide, produsul din link e cel descris, niciun IP scăpat.
- Commit + push.

## 7. După ce alege Szasz
- Produsul ales → skill `product-sheet` (referințe), apoi `pilot-video` (obligatoriu).
- Dacă zice el: adaugă-l în colecția `products` din platformă.
- Ce a ieșit prost în research (link mort, cifră greșită, produs cu IP) → skill `log-lesson`.
