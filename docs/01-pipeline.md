# Pipeline-ul: fiecare pas manual → modul automat

Stare: ✅ metoda e dovedită, trebuie doar construit modulul · 🟡 parțial / cu Szasz în buclă · ⬜ de descoperit

| # | Pas | Metoda | Modul LIMITLESS | Stare |
|---|---|---|---|---|
| 0 | Detectare produs | link / poze → profil + strategie | `engine/product-profile` | ⬜ |
| 1a | Competitori on the rise | conturi în creștere pe nișă, verificate de 2 ori/zi; ≥ 100k în 24 h = dovedit (`docs/08`) | `engine/hunter` | ⬜ |
| 1 | Research virale | Apify IG/FB/Ad Library, outlier ≥ 3× media contului | `engine/research` | ✅ |
| 2 | Analiză viral | 8 cadre + audio, hook descris în format standard | `engine/analyze` | ✅ |
| 3 | Alegere hook | virale nefolosite din conturile de referință + hook-urile lui Szasz | `engine/hooks` (scor + rotație) | 🟡 |
| 4 | Seturi (personaj + cameră) | Pinterest, poze ≥ 1080 px | `engine/sets` | ✅ |
| 5 | Producție B-roll | Genjutsu motion control, clipuri de mișcare rotite | `engine/produce` | ✅ |
| 6 | Clipuri fixe | demonstrații de produs făcute o dată, refolosite după gen și piele | `library/fixed` | ✅ |
| 7 | Hook video | viral tăiat → Genjutsu cu setul nostru; fallback placă + seedance | `engine/produce` | ✅ |
| 8 | QA vizual | Claude cu vedere, reguli per clip, max 3 regenerări | `engine/qa` | ✅ |
| 9 | Montaj | tăieturi, text TikTok Sans, emoji, muzică de la secunda competitorului | `engine/edit` | ✅ |
| 10 | Postare | echipă de posteri, fiecare cu link secret și lista zilei; videourile se împart în ordine, niciunul de două ori | `distribution/` | 🟡 cod gata, de instalat |
| 11 | Multi-cont | conturi noi pe persoană: creare → încălzire 2 zile → profil → 3 videouri/zi pe IG + TikTok + FB | `distribution/` (`config/schedule.json`, `personas.json`) | 🟡 cod gata, de instalat |
| 12 | Feedback cifre | tracker orar prin Apify: vizualizări, câștig zilnic, urmăritori, top videouri, cifre la 24 h și 7 zile | `social_tracker/` | 🟡 cod gata, de instalat |
| 13 | Promovare hook | scor > mediană → dovedit | `engine/hooks` | 🟡 |
| 14 | Conversie | — | `engine/store` (pagina, oferta, A/B) | ⬜ |
| 15 | Produse noi | Meta Ad Library: produse cu reclame plătite care rulează de mult, cu multe variante (`docs/07-scout-meta-ads.md`) | `engine/product-scout` | ⬜ |
| 15b | Variații de produs | idei custom fezabile + mockup + test (`docs/08`) | `engine/variations` | ⬜ |
| 16 | Raport zilnic | tabla HTML | `engine/report` (dashboard + Telegram) | 🟡 |
