---
name: pilot-video
description: Primul video la fiecare produs = pilot obligatoriu. Folosește înainte de orice lot pe un produs nou.
---
# Pilot (regula din 13 oct)

1. Fără pilot aprobat nu se face lot pe produsul ăsta.
2. Alege un viral dovedit al produsului (Product finder) și hook-ul cu cel mai mare now_score din familia potrivită.
3. Test ieftin întâi: Genjutsu la 480p (~3–4 credite/s). Verifică `get_cost:true` și `balance`; cere aprobarea lui Szasz cu costul exact.
4. QA vizual: 9:16, produsul = referința, fără text/branduri, look iPhone 18 Pro Max UGC, camera nu „fuge” după tăieturi.
5. Doar dacă trece: varianta finală 1080p. Salvează jobul în colecția `jobs` (status pilot) și promptul ca șablon.
6. După postare: skill `results` ca să vedem cifrele. Ce a mers prost → `log-lesson`.
