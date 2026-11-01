# Storyboard v2: fiecare cadru al lor, îmbunătățit (1 nov 2026, cererea lui Szasz)

Regula nouă (Szasz, 1 nov): **ÎNAINTE de generare** studiez fiecare cadru din original, notez ce e GREU de generat, fac **referință (start frame / end frame) în nișa noastră pentru fiecare cadru**, generez cadru cu cadru, apoi lipesc. Totul e în prompt. Ce nu iese bine trebuie să-l văd eu, înainte să-l vadă Szasz.

## De ce v1 a avut cadrele de la final proaste (trebuia văzut de mine)
- În original, fiecare model apare când **brațul deschide ușa**, iar cadrul e larg: mașina, ușa, casa și proiecția ies din partea de jos a ușii. În v1, de la 8,5 s încolo, proiecția plutea singură pe asfalt, fără ușă și fără mișcare, ca un abțibild. Așa nu arată real și nu se vede ACȚIUNEA (deschizi ușa, apare logo-ul), adică exact ce vinde.
- Proiecția din v1 era prea curată, ca un ecran. Una reală e întinsă în perspectivă (vine dintr-o lentilă de jos de pe ușă), are marginile moi, iar textura asfaltului se vede prin lumină.
- **Decizia lui Szasz (1 nov): TOT videoul dintr-o singură generare Seedance 2.5, nu pe bucăți.** Soluția: câte o referință făcută de noi pentru FIECARE cadru (image 1…8), toate în aceeași generare, iar în prompt fiecare secvență spune ce imagine folosește („shot 6 = image 7”). Originalul (cu fața estompată) rămâne video_reference pentru ritm.

## Cadrele (original → noi)
| # | secunde orig. | original | noi (îmbunătățit) | greutate | referința (image N) |
|---|---|---|---|---|---|
| S1 | 0,0–1,0 | POV șofer intră la drive-thru, mâna pe volan | POV, mașină neagră, drive-thru negru cu galben cu liliacul nostru; angajata se vede deja la geam cu cutia (hook din primul cadru) | mică (risc: text stricat pe firme) | image 2 (F1) |
| S2 | 1,0–2,4 | angajata dă cutia pe geam | la fel, cutia neagră cu liliac vine spre lentilă | medie (mâini, mânerul cutiei) | image 3 (F2) |
| S3 | 2,5–4,9 | cutia pe scaun, se deschide, punguța | cutia se deschide dintr-o mișcare, se scoate punguța neagră cu liliac și proiectorul se vede imediat | medie (capacul) | image 4 (F3) |
| S4 | 5,0–5,9 | proiectorul în două mâini, întors | proiectorul negru cu liliac galben, întors spre lentilă | medie (produsul identic) | image 5 (F4) + image 1 (produsul) |
| S5 | 6,0–6,9 | stick-ul mic (cu desen) ținut între degete, apoi băgat în proiectorul de pe ușă | la fel, stick negru cu liliac galben | **MARE** (obiect mic, mâini, aliniere) | image 6 (F5): mâna duce stick-ul sub proiectorul de pe ușă; în prompt: întâi stick-ul ținut aproape de lentilă, apoi băgat |
| S6 | 7,0–13,9 | noaptea, brațul deschide ușa, iar la fiecare deschidere apare alt model (5) | la fel, mașină neagră lucioasă, asfalt ud, 5 modele: liliac galben → castel cu lună → liliac cu inimă → liliac cu ochi galbeni → liliac de Crăciun | **MARE** (ușa, proiecția din ușă, modelul exact, fără să se transforme) | image 7 (F6): cadrul LARG ca în original (mașina, ușa, casa, brațul care deschide, proiecția din ușă) + image 8 (grila de modele). În prompt: la fiecare model, brațul închide pe jumătate și redeschide ușa, cadrul rămâne larg, proiecția iese din ușă. |

## Blocul de proiecție realistă (în fiecare prompt de noapte)
"Real LED car door puddle light: the image comes from a small lens at the bottom edge of the open door, so it is stretched a little in perspective on the ground, with soft slightly blurry edges and light falloff, the wet asphalt texture and small puddles visible through the light, colours a bit washed like real projected light - not a sticker, not a screen, not glowing neon."
