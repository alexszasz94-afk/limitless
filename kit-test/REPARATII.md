# Ce trebuie reparat în kitul creatorilor (test 30 oct, kitul din 28 oct)

4 videouri făcute strict cu kitul: `output/snoopy-frozen`, `output/snoopy-rollrobe`, `output/princess-countdown`, `output/princess-unroll`. Detalii în fiecare `notes.md`.

## Urgent (strică direct videoul)
1. **Textul de pe ecran** — regula 9 „copiază cuvânt cu cuvânt” → au ieșit texte cu Frozen / Princess pe Snoopy. Fix: păstrează cuvintele, schimbă numele produsului/personajului (CLAUDE.md regula 9, new-video pas 1, HOOKS.md pas 2).
2. **Sunetul hook-ului are 3 metode diferite** (Kling în prompt / Kling 720p + place-voice / Seedance) în CLAUDE.md 9d-9e, HOOKS.md, new-video 5b. Fix: o singură metodă (acum: vocea din Kling, din aceeași generare — regula Szasz 29 oct).
3. **Poza `products/snoopy/refs/pouch.jpg` e a altui halat** (roșu-crem, text ars pe ea, femeie în pantaloni scurți) → doi săculeți separați la Snoopy. Fix: poză curată cu săculețul nostru.
4. **Picioarele la săculeți (Princess motion2)**: în 2 din 2 încercări se vede călcâiul când intră; regula 9j „tăieturile din planul cu săculeții sunt false” e prea absolută (una era glitch real).
5. **Ținuta se schimbă între hook și B-roll** (pijamaua altfel) și camera din cozy diferită (princess-unroll) — lipsește pasul „aceeași ținută + aceeași cameră în tot videoul”.
6. **Volumul**: după hook videoul scade cu ~7 dB (montage.py nu normalizează), iar `orig_vol` implicit 0.15 pune vocea sub muzică.

## Reguli care se contrazic
7. Blocurile de calitate „în fiecare prompt” (4b, 7b) vs PRODUCT.md „copiază promptul B-roll cuvânt cu cuvânt, nu adăuga nimic”.
8. Camera doar cu pat: promptul dovedit inventează canapea → trebuie o variantă pentru pat în PRODUCT.md.
9. Ce e „Image 1” (9g zice obiectul cu logo, 9i/HOOKS zic personajul).
10. Unde cade refrenul muzicii: pe reveal (9e.1, PRODUCT.md) sau pe tăietura hook→B-roll (9e.7).
11. Lungimea hook-ului: 3–7 s (new-video) vs exact cât originalul (9f).
12. Timpii conectorului: next-set zice „tot clipul”, PRODUCT.md zice 1.2–4.0.
13. Decupajul fețelor: new-video zice mereu, PRODUCT.md Snoopy zice doar la fuste/pantaloni scurți.
14. Princess nu are cutie/logo de referință, deși 9g/9h cer „cutia noastră cu logo-ul nostru” → a inventat o cutie.

## Programe (engine/tools.py, montage.py)
15. `cleantext` rulează la nesfârșit dacă clipul n-are sunet (umple discul).
16. `next-set` + `reject`: respingi o cameră → arde și fata (3 fete pierdute degeaba).
17. Biblioteca: camerele 14–17 au 736 px, 19 n-are nici canapea nici pat, 20 are reclamă cu cod QR pe TV, 21 e noaptea cu masă în mijloc → next-set trebuie să le sară (regula de calitate din 29 oct nu e în kit).
18. Uneltele de sunet (`hook-audio`, `audit-sound`, `transcribe`, `onsets`) dau secunde diferite și „aud” voce în melodii (au inventat „3, 2, 1” și „Thanks for watching”). Fix: vocea doar dacă și analiza Higgsfield o aude; o singură comandă pentru secundele cuvintelor.
19. Lipsește comanda care pune sunetul Seedance înapoi pe hook fără să scurteze clipul.
20. `compare` face o fâșie de 5000 px — de pus pe rânduri.
21. `blur-for-sound` nu ajută la găsirea feței (prima cutie tăia gura).
22. Regula 9f.2 (tai la secunda întreagă) prinde scena următoare când hook-ul se termină pe tăietură — de pus „îngheață ultimul cadru”.
23. Ștergerea textului cu poză curată nu merge când ceva se mișcă sub text; „remove the caption” în promptul Kling a mers bine.

## Setup și flux
24. `setup/check.sh` nu verifică demucs.
25. Upload un fișier pe rând = zeci de mesaje lungi → un `tools.py upload`.
26. `output/_new` fix: două videouri în paralel se calcă (o sesiune a luat folderul celeilalte); media.json/used.json fără îmbinare.
27. Rotația conectorului depinde de `log` înainte de `next-set` — nescris.
28. Bugetul din regula 13 e vechi: un video real costă 70–100 credite (hook 5 s = 20, Seedance 5 s = 18, poza cutiei 4, o refacere de B-roll 28); limita de ~90 se depășește des.
29. Întrebarea „ce final cozy” blochează tot până răspunde creatorul — implicit „classic”.
30. `princess-trend.mp3` are 15 s (prea scurt); `cozy-zoom.mp4` e pomenit dar niciun pas nu-l face.
