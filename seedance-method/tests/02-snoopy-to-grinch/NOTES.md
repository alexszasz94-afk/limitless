# Test 02 — reel Snoopy x In-N-Out → nișa Grinch (1 nov 2026)

## Ce a cerut Szasz (în ordine)
1. Fiecare cadru de la ei, dar îmbunătățit; studiez dinainte ce cadre sunt greu de generat.
2. Tot videoul dintr-o singură generare, nu pe bucăți.
3. Studiez cadrele mai des: la 0,1 s + detectarea tăieturilor (`ffmpeg select='gt(scene,0.25)'`).
4. Referința fiecărui cadru = POZA LOR din acel cadru, refăcută mai bine în nișa noastră (edit GPT Image 2.5 pe cadrul lor).
5. Studiez mereu logica produsului și ce obiecte apar.
6. Seedance 2.5 refuză Grinch (`ip_detected`), deci **Grinch = Kling 4.0 video-edit** (decizia lui Szasz).

## Tăieturile originalului (precizie de 1 cadru, 30 fps)
0,83 · 2,5 · 3,37 · 4,23 · 5,1 · 5,5 · 5,97 · 6,67 · 7,1 · 8,73 · 10,6 · 12,07 → 13 planuri.
| plan | s | ce se vede |
|---|---|---|
| 1 | 0–0,8 | POV șofer intră la drive-thru |
| 2 | 0,8–2,5 | angajata dă cutia; la final cutia e în mâna șoferului, angajata zâmbește |
| 3 | 2,5–3,4 | cutia deschisă pe scaun, mâna ține capacul |
| 4 | 3,4–4,2 | mâna intră în cutie |
| 5 | 4,2–5,1 | ambalajul TRANSPARENT cu proiectorul, ridicat spre cameră |
| 6 | 5,1–5,5 | proiectorul în două mâini (latura neagră cu fanta) |
| 7 | 5,5–6,0 | apropiere pe proiector |
| 8 | 6,0–6,7 | stick-ul USB cu desen, între două degete, lângă bord |
| 9 | 6,7–7,1 | proiectorul pe ușă, stick-ul băgat dedesubt |
| 10–13 | 7,1–13,9 | noapte, 4 modele; fiecare: plan larg cu brațul care închide ușa, ușa se redeschide, camera coboară pe proiecție |

## Logica produsului și obiectele
- Cutie cu mâner (de la drive-thru) → ambalaj transparent cu fereastră → proiector pătrat alb (desen în față, latură neagră cu fantă) → **stick USB = bateria** (se încarcă, apoi se bagă sub proiector) → proiectorul se lipește pe interiorul ușii → la fiecare deschidere a ușii apare automat următorul model.
- Muzica: instrumental, apoi „Let It Snow” de la 7 s.

## Generări
- v2 Seedance (referințe proprii, nu din cadrele lor): job 2a732304 → **ip_detected** (Grinch). Creditele s-au întors.
- v3 Kling 4.0 video-edit, 1080p, 14 s, 56 credite: video = originalul (ac7bc714), Images 1–8 = cadrele lor refăcute (ec9e8c48, a87cb0e9, 69a29b0e, 8fbb062d, c29dc3d4, abee7d81, cfdc78e7, 6d7dfa88), Image 9 = grila de modele (9171c496). Job 7de338fa.
