# Test 01 — reel-ul „Snoopy x In-N-Out” → nișa Batman (1 nov 2026)

## Originalul (observat, nu ghicit)
- Link: https://www.facebook.com/reel/2405071133364459 — pagina „Snoopy Beams”.
- Cifre: titlul paginii spune **1.3M views · 15K reactions**; yt-dlp a citit `view_count` = 586.126 (Facebook raportează diferit; luăm 586k ca minim sigur).
- Produs: **proiector LED de portieră** (logo pe asfalt când deschizi ușa), cu mai multe modele. Montaj cu adeziv, 1 secundă.
- 13,9 s, 9:16, fără voce, doar muzică. Text fix tot timpul: „Snoopy 🐶💕 X In-N-Out”.
- Caption: „Just kidding!! We sell these 😍🥹 Comment “Snoopy” for the link 🐶💕”.
- Fișiere: `ref/original-snoopy-innout.mp4`, `ref/contact-sheet-original.jpg` (cadru la 0,5 s).

## Pe secunde
| s | ce se vede |
|---|---|
| 0–1 | POV din mașină, intri la drive-thru-ul In-N-Out, soare, palmieri |
| 1–2,5 | angajata zâmbitoare îți dă pe geam o cutie „In-N-Out” cu Snoopy |
| 2,5–4,5 | unboxing pe scaunul pasagerului: punguță cu Snoopy, apoi proiectorul |
| 5–6,5 | proiectorul în mână, apoi lipit pe interiorul portierei (1 s) |
| 7–14 | NOAPTE, stradă de cartier: deschizi ușa, apare Snoopy pe asfalt. Închizi și deschizi, alt model (flori, Woodstock, ochelari), la final **Snoopy de Crăciun** |

## De ce a mers (ipoteze; cifra e doar a lor, nu a noastră)
1. **Colaborare falsă „X x Y”**: „există așa ceva?!”. Oamenii comentează și dau share, iar caption-ul „Just kidding” mai bagă un val de comentarii. Plus „Comment Snoopy for the link”.
2. **Poveste în prima secundă**: drive-thru și cineva care îți dă un cadou, deci recompensă și curiozitate („ce e în cutie?”).
3. **Ambalaj = valoare percepută**: o cutie frumoasă face să pară un produs de colecție.
4. **Montaj ușor**, arătat în 1 s.
5. **Reveal-ul pe repetiție**: fiecare deschidere de ușă arată alt model, așa că te uiți până la capăt (retenție). Se termină pe Crăciun, în sezon.
6. **Nișă cu identitate**: fanii Snoopy (mame, femei) își cumpără „personalitatea”.

## ATENȚIE — drepturi (de decis de Szasz)
- Batman e marcă DC / Warner Bros. Un proiector cu logo-ul Batman fără licență înseamnă risc de blocare a magazinului (Shopify, procesatorul de plăți), postări șterse și cont TikTok/Meta penalizat. Concurentul face la fel cu Snoopy și In-N-Out, dar asta nu ne protejează.
- Propunerea mea: **nișa „dark knight / bat” fără marcă**. Liliac stilizat propriu (nu logo-ul oficial), oraș gotic noaptea, ploaie, negru și galben. Fanii Batman îl recunosc ca „vibe”, dar nu e logo-ul lor. Nu facem colaborare falsă cu un brand real.
- Alternativa: produs cu licență oficială (furnizor licențiat). Altfel nu folosim numele „Batman” în video sau caption.

## Hook-ul NOU (nu clonă) — 3 variante de test
Păstrăm motorul: **recompensă/curiozitate în secunda 1 → montaj 1 s → reveal la noapte pe repetiție → final de sezon**. Schimbăm vizualul.

**A — „Semnalul”** (cel mai puternic, după mine)
0–1,5 s: noapte, ploaie, oraș. Pe cer se vede un semnal în formă de liliac, apoi camera coboară și se vede că vine de la o portieră de mașină neagră, pe asfaltul ud. Text: „POV: your car finally matches your personality 🦇”.
1,5–3 s: cineva lipește proiectorul pe portieră (1 s).
3–10 s: deschide și închide ușa, alt model de fiecare dată (liliac, liliac peste skyline, liliac cu ochi galbeni). La final liliac cu căciulă de Moș Crăciun.

**B — „Livrarea”** (păstrează mecanismul cutiei-cadou)
0–1,5 s: un majordom în smoking îți dă pe geamul mașinii, noaptea, o cutie neagră lăcuită cu liliac. Text: „When your butler knows you better than anyone 🦇”. Apoi unboxing, montaj, reveal.

**C — „Garajul”** (POV fan)
0–1,5 s: garaj întunecat, se aprinde o singură lumină și se vede o mașină mată neagră. Ușa se deschide și liliacul uriaș se reflectă pe beton. Text: „Every night when I get to my car 🖤”. Apoi montaj și reveal.

Caption (pentru toate): „Comment “BAT” for the link 🦇🖤” — fără numele Batman.

## Referințe necesare (Seedance 2.5, mod omni_reference)
1. **Produs**: proiectorul real (poze de la furnizor: corp, lipit pe ușă, proiecția).
2. **Proiecțiile**: 4–5 imagini cu modelele de liliac (le fac cu GPT Image 2.5, apoi le verific).
3. **Personaj**: brațul/mâna, mâneca neagră, fără față (ca în original), plus majordomul doar la varianta B.
4. **Loc**: stradă udă noaptea, mașină neagră (Dodge Charger / Mustang negru mat, fără logo vizibil).
5. Mișcarea: originalul ca `video_reference` doar pentru ritm (7–14 s, deschide/închide ușa), nu pentru look.

## Setări propuse
- `seedance_2_5`, `mode: omni_reference`, 9:16, întâi **draft 480p** (ieftin), apoi finalizare 1080p doar pentru draftul bun.
- Bucăți de 5–8 s: hook (5 s), montaj (4 s), reveal (8 s), lipite cu ffmpeg. Text pe ecran pus de noi, nu de AI.
- Lumina: blocul `prompts/blocks/light-soft-natural.txt` adaptat la noapte (moale, fără contrast dur, felinare calde).

## Verificare înainte să-i arăt lui Szasz
- Contact sheet la 0,5 s, original lângă al nostru: ritm, unde e produsul, ce parte se vede, fără logo-uri reale, liliacul clar pe asfalt.
- Higgsfield `virality_predictor` pe fiecare variantă, doar ca filtru (ipoteză).
- Decizia finală: postăm toate 3 și câștigă cea cu retenția la 3 s și vizualizările cele mai mari.
