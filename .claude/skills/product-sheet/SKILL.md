---
name: product-sheet
description: Fișa produsului când Szasz bagă un produs în My products — referințe generate cu Higgsfield, aprobate de Szasz. Folosește la „produs nou” sau „concept nou de produs”.
---
# Fișa produsului (regula din 13 oct)

1. Citește `docs/02-reguli.md` și Mistakes log (colecția `lessons`) înainte de orice.
2. Strânge pozele reale ale produsului (link-urile virale / pagina furnizorului). Nu comandăm probe.
3. Propune setul de referințe, ca la HeatGrump (`/home/user/heatgrump/library/media.json`): produs față, spate, detaliu, în uz, ambalaj, accesorii (telecomandă, conector etc. dacă există).
4. Spune costul estimat (gpt_image_2 4k ≈ 15 credite/imagine) și cere aprobarea lui Szasz ÎNAINTE de generare. Verifică `balance`.
5. Generează: gpt_image_2, 9:16, quality high, 4k, fără text, fără branduri reale, declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`.
6. Arată-i rezultatele; păstrează doar ce aprobă. Scrie ID-urile Higgsfield în `products/<produs>.md` și în documentul produsului din baza de date (`products/<id>.refs`).
7. Variații noi (alt model/culoare) se fac la fel, DOAR când Szasz zice „concept nou de produs”.
8. Orice greșeală → skill `log-lesson`.
