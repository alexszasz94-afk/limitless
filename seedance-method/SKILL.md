---
name: seedance-method
description: Produs dovedit + viralul concurenței + nișă nouă din SUA → video Seedance 2.5 din referințe, cu hook-ul păstrat dar fără timp mort. Proiect separat de halate.
---

# Metoda Seedance (1 nov 2026, Szasz)

Ideea lui Szasz: pui videoul viral în Higgsfield ca **video_reference**, scrii promptul **pe fiecare secvență** ca să iasă perfect și mai bun (fără „dead spaces”), cu **produsul nostru**, pentru care faci referințele dinainte.

## Pașii (în ordinea asta, fără să sari)
1. **Ia viralul.** `python3 -m yt_dlp -o reel.%(ext)s --write-info-json <link>` (merge pe Facebook/TikTok; YouTube cere „not a bot” de pe server). Notează cifrele (views, reacții) din `info.json` și din titlu.
2. **Analiza (obligatoriu înainte de orice generare).**
   - Foaie cu cadre la 0,5 s: `ffmpeg -i reel.mp4 -vf "fps=2,scale=216:-1,drawtext=text='%{pts\:flt}':x=4:y=4:fontsize=20:fontcolor=yellow:box=1:boxcolor=black,tile=7x4" -frames:v 1 sheet.jpg`
   - Higgsfield: `media_upload` → curl PUT → `media_confirm` → `video_analysis_create(video_input_id)`. Poate sta mult la coadă; nu blochează: scriu analiza locală pe cadre.
   - Audio: voce sau doar muzică? Textul de pe ecran, caption-ul.
   - Salvează `ref/analysis-*.json`: pe secunde ce se vede, unde e timp mort, de ce a mers (marcat ca ipoteză).
3. **Ce păstrăm și ce îmbunătățim.** Păstrăm hook-ul și motorul psihologic. Tăiem: secunde fără produs, obiecte care nu sunt produsul, cadre cu ușa sau cutia închisă, produsul mic în cadru. Produsul trebuie să apară în primele ~1,5 s.
4. **Referințele noastre (GPT Image 2.5, ~0,25 credite/buc).** Câte una pentru: produs (3 unghiuri), ambalaj, cadrul hook-ului (persoană + loc), toate modelele/variantele produsului (grilă), locul reveal-ului. Le verific cu ochii mei, alăturate.
   - **Fără logo-uri sau personaje cu drepturi** (Batman, Snoopy, mărci reale). AI-ul tinde să deseneze logo-ul oficial: cere explicit „realistic natural X, NOT a logo shape, NOT the famous … emblem” și refă prin edit pe imaginea bună.
   - Dacă Higgsfield blochează pe „nsfw” din greșeală: scurtează promptul, scoate detaliile despre mâini/unghii și „adhesive”.
5. **Promptul Seedance 2.5** (`seedance_2_5`, `mode: omni_reference`): 1 `video_references` = viralul + `image_references` = referințele noastre, numerotate în prompt (image 1…). Structura promptului:
   1. „Use the reference video ONLY for story structure, POV camera style and pacing” + lista pașilor.
   2. „Replace every brand, logo and character … with OUR references (image N = …)”. Plus „No <brandurile originalului>, no readable text”.
   3. „Make it tighter than the reference, no dead time, every second shows the product”.
   4. **Timeline pe secunde**, câte o linie pe secvență, cu acțiunea exactă.
   5. Lumina: foarte moale, naturală (ziua difuză; noaptea felinare calde, fără bloom), iPhone 16 real, mâini cu 5 degete.
   - `generate_audio: false` (muzica și textul de pe ecran le punem noi la montaj). Dacă apare `preset_recommendation`, îl refuzi cu `declined_preset_id`.
6. **Întâi draft** (`draft: true`, 480p, ~42 credite / 14 s). Verific cadru cu cadru lângă original. Doar draftul bun îl finalizez la 1080p (`draft_job_id`, ~224 credite / 14 s). Spune-i lui Szasz costul înainte.
7. **Verificarea înainte să-i arăt lui Szasz:** foaie de cadre original | al nostru, la aceleași secunde. Verific: hook-ul în prima secundă, produsul arată ca referința, nu apare niciun logo real sau text stricat, mâinile sunt OK, nu există timp mort, modelele vin în ordinea cerută.
8. **Montaj:** text pe ecran (engleză), muzică, caption cu „Comment “X” for the link”.
9. **Testul real:** 2–3 variante postate. Câștigă retenția la 3 s, views și comenzile. Promptul câștigător + referințele + setările intră în `recipes/` și de atunci se copiază cuvânt cu cuvânt.

## Teste
- `tests/01-snoopy-to-batman/`: reel Snoopy x In-N-Out (586k–1,3M views) → nișa „bat” fără marcă.

## Lecții
- 1 nov: Seedance a picat fără motiv (creditele s-au întors) cu viralul brut ca `video_references`. Cauza probabilă: chipul real al unei persoane în videoul de referință. Soluția: estompezi fața cu ffmpeg (`crop` + `boxblur` + `overlay` doar pe secundele cu fața) și reîncerci.
- 1 nov (test 02 Grinch): **Seedance refuză personajele protejate (`ip_detected`)**. Pentru ele: Kling 4.0 `video-edit` (decizia lui Szasz). Video-edit păstrează tăieturile originalului la ±0,1 s.
- Referințele = **cadrele LOR** (unul pe fiecare plan, extras la secunda exactă) refăcute cu GPT Image 2.5 edit: aceeași încadrare, fără text, obiectele noastre. Câte o referință pentru FIECARE variantă de produs care apare pe ecran (nu grilă).
- Kling cu 9–10 imagini mai „alunecă” o referință pe planul vecin. Verifici la 0,1 s, și pentru că toate variantele au aceleași tăieturi, **îmbini planurile bune din variante diferite exact la tăieturi** (ffmpeg trim + concat), fără credite în plus.
- Studiul: cadre la 0,1 s + `ffmpeg -vf "select='gt(scene,0.25)',showinfo"` pentru tăieturi + logica produsului + lista obiectelor.
