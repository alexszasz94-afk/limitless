---
name: results
description: Firul datelor — ia cifrele postărilor noastre cu Apify, le scrie în `posts`, și învață ce hook-uri merg la noi. Folosește la „rezultate”.
---
# Rezultate → învățare

1. Citește conturile din colecția `accounts` și postările din `posts`.
2. Cost: instagram-reel-scraper ≈ $0,0026/reel. Spune-i lui Szasz costul estimat și cere acordul dacă trece de $0,50. Pune mereu `maxTotalChargeUsd`. Nu afișa niciodată APIFY_TOKEN. Fără Facebook/Meta Ads scraping.
3. Rulează scrape-ul pe conturile noastre (ultimele 30 de zile). Pentru fiecare reel: views, likes, comments, data. Leagă-l de postarea din `posts` după link; postările noi le adaugi (fără `action` dacă nu știi hook-ul — întreabă-l pe Szasz).
4. Actualizează `posts/<id>` (views, likes, comments, checked) și `accounts/<id>` (followers, checked).
5. Învățare: pe acțiune de hook calculează media de views și comenzile; scrie concluzia în `config/strategy` (EN). Orice „merge” are cifra lângă; altfel e marcat ipoteză.
6. Prag go/kill: $ la 1M views. Sub prag după pilot + 5 postări → propune schimbarea hook-ului sau a produsului.
7. Greșeli → `log-lesson`.
