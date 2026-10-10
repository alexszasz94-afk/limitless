# Note Higgsfield YouTube — part4 (videouri 2025-04 → 2026-10-08)

Sursă: `chunks/part4.txt`, citit integral. Doar ce e spus explicit în transcrieri. Transcrierile automate stâlcesc numele („Kixel / Hixel / Kick sell / Pixele” = Higgsfield; „C2.5 / Seed AST 2.5 / CDS 2.5 / SeaArt's / Z Dance / Cinder” = Seedance; „Astra” = GPT-6 Astra din ChatGPT). Unde transcrierea e neclară, scrie „neclar”.

Videouri fără conținut util (doar muzică, scene de film, promo): Katana (-LNDXx__ZT0, doar trailer), Ads Studio in ChatGPT (zephnQwGbBE), Effects 2.0 in ChatGPT (tx3pcpC_0qA), The Trigger, Hell Grind (filmul), Helen of Troy, „Animation like this…”, Cannes x2, music video, KION, Soul 2025, Draw-To-Edit launch (doar muzică), Effects Pack 5, Higgsfield x OpenAI.

---

## 1. Unelte / modele

### Seedance 2.5 (model video principal în 2026)
- Lansat pe Higgsfield în jurul datei de 2026-08-07 („C2.5 just went live… most anticipated model of the year”) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- **Video-to-video (înlocuire personaj)**: urci clipul original + character sheet și ceri „replace the character in this video with the person in this image. Keep the video one-to-one and only swap out the person”. Modelul potrivește automat lumina, umbrele și contrastul cu mediul (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- **Cerință: minimum 4 s de video la intrare** pentru video-to-video; dacă un segment e mai scurt, se îngheață ultimul cadru (freeze-frame) până la 4 s. Durata generării se setează egal cu referința (4 s): „anything longer and the AI starts guessing” (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Limită: v2v pică dacă sursa nu conține momentul cerut (ex. sărituri care nu există în clipul sursă) → iese slop; soluția e image-to-video din captură de ecran a locației, apoi lipire la montaj (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Schimbare de look/haine pe un video al tău: (1) cauți poze de referință cu ținute, (2) dai referințele + videoul la ChatGPT să scrie promptul, (3) urci în Higgsfield video + referințe + prompt la Seedance 2.5 și generezi (https://www.youtube.com/shorts/UlBDRHLAfUY).
- Durate lungi: s-au generat cadre continue de 15 s și 30 s, 16:9, „one continuous shot”, cu 2 variante per cerere ca să alegi (https://www.youtube.com/watch?v=vUYq38wC_xI).
- Primește blocking 3D (video) ca referință de mișcare + character sheet + imagini de locație; poate urma tăieturile și mișcările de cameră din blocking; muzica și vocea pot fi cerute în același request și se generează odată cu videoul (https://www.youtube.com/watch?v=vUYq38wC_xI).
- Gestionează bine lumina natural, „zero compositing” (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Are dificultăți cu adâncimea când locația e privită frontal (vezi Prompting) (https://www.youtube.com/watch?v=6aJ2BneDB5M).
- Uneori iese sacadat (18 fps sau mai puțin) deși în prefixul de stil scrie 24 FPS → se șterg manual cadrele duplicate (https://www.youtube.com/watch?v=6aJ2BneDB5M).

### Seedance 2.0 / 1.5 Pro
- Pentru UGC, agentul Supercomputer folosește **Soul pentru personaj + Seedance 2.0 pentru animație**; rezultatul e consistent și realist chiar cu prompt simplu (https://www.youtube.com/watch?v=ttFWPdNInqg).
- Seedance 2.0 „went global” pe 2026-04-11 (https://www.youtube.com/shorts/wn64gYE73JY).
- Seedance 1.5 Pro (ianuarie 2026): bun la emoții umane și dialog, dar slab la generarea de medii noi când camera se mișcă → tier B (https://www.youtube.com/watch?v=nnGFEUeL-P0).

### Kling
- Kling 2.6 (ianuarie 2026): tier S, „go-to pentru aproape orice”, cele mai curate videouri, cel mai mult control pe cameră și realism (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Kling O1 Edit: urci videoul și schimbi detalii cu imagini de referință sau text, fără regenerare de la zero (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Kling Motion Control: urci un video de referință și copiază mișcarea subiectului / camera (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Câștigătorul concursului ($150k) a animat cu Kling + Seedance, imagini cu Nano Banana în Higgsfield + Cinema Studio, montaj în Premiere, upscale cu Topaz (https://www.youtube.com/watch?v=babNcxpwnx0).

### Sora 2 / Sora 2 Pro (stream oct. 2025)
- Sora 2: până la 12 s, 720p. Sora 2 Pro: 1080p, 12 s, 9:16 sau 16:9; generează mai lent (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Imaginea de start **nu trebuie să conțină oameni realiști sau animale** — sistemul Sora o blochează (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Fața ta nu se poate folosi în Sora pe Higgsfield (cameos doar pe site-ul Sora, cu watermark); alternativa: Veo 3 sau Wan 2.5 (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Are model de raționament/prompt enhancer intern → și prompturi scurte dau videouri bune (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- „Sora Trends”: 25+ preseturi (crazy situation, ads, luxury, Japanese ad, street interview, streamer, POV, motivational, unpacking, minimalist corporate, epic fails etc.), fiecare cu prompt enhancer propriu; setări: craziness, ritm montaj, limbă, tempo vorbire, stil (realistic), „no cut safe” (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Transferă bine identitatea produsului; face UGC tip reacție cu text dictat (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Seed fix nu reproduce rezultatul (promptul trece prin enhancer) (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Ian. 2026: tier S, „gold standard” fizică și consistență, sub Kling pentru că nu acceptă fețe umane ca referință și e mai scump (https://www.youtube.com/watch?v=nnGFEUeL-P0).

### Alte modele video (clasament ian. 2026)
- Veo 3.1: tier A, realism și audio foarte bune (https://www.youtube.com/watch?v=nnGFEUeL-P0). Veo 3 pe Higgsfield din 2025-07-11 (https://www.youtube.com/watch?v=FHSaNEcD-B0).
- Minimax Hailuo 2.3: tier C. Wan 2.6: tier D, nesigur (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Seedance / „Dale” (neclar) = „immersion kings” pentru emoții și vorbire (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Wan 2.5: unlimited o săptămână la lansare (2025-09-26) (https://www.youtube.com/watch?v=tmh_BBctfvk).

### Modele de imagine
- **Nano Banana 2**: „cel mai bun acum la potrivirea fețelor” pentru character sheet (aug. 2026); și modelul care „ține cel mai bine inputul” → bun pentru corecturi mici (logo) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- **Nano Banana Pro**: tier S (ian. 2026): urmează promptul, logică, cunoștințe reale, cel mai bun text (https://www.youtube.com/watch?v=nnGFEUeL-P0); probă haine pe persoană, inserare în scene, emulează aparatul foto urcat, screenshot-uri desktop, postere (https://www.youtube.com/shorts/51LAQ2Ntnrs).
- **GPT Image 2**: „se descurcă cel mai bine cu hainele” (schimbare ținută) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ); text mic fără glitch-uri, carduri de produs Amazon/Shopify, postere, postări (2026-05-28) (https://www.youtube.com/shorts/7YUTjb27Mto). Limite: poate deforma logo-ul, hainele ies albăstrui (https://www.youtube.com/watch?v=Hn8A8D4-SpQ); la locații „GPT always screws yellow” (dominantă galbenă) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ). În ian. 2026 GPT image și nano banana (non-Pro) erau tier C (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- **Soul Cinema**: „pentru locații folosesc mereu Soul Cinema” — cele mai cinematice cadre; Nano Banana face locații prea curate și simetrice (https://www.youtube.com/watch?v=Hn8A8D4-SpQ). Generează și locații din text (https://www.youtube.com/watch?v=vUYq38wC_xI).
- **Soul** (nativ Higgsfield): tier A, ultra-realist pentru fashion și UGC, „go-to pentru fețe perfecte” (https://www.youtube.com/watch?v=nnGFEUeL-P0); aspect „Pinterest” mai estetic decât NB/Seedream (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- **Soul 2** (2026-02-20): identitatea antrenată o dată rămâne stabilă (Soul 1 avea drift de maxilar/textură piele, pe anumite tipuri de fețe/etnii/lumini); înțelege limbaj de modă; 20+ preseturi curate („taste layers”); generează și obiecte, mobilier, medii; aceeași identitate pe billboard, catalog, social ads, bannere, conținut UGC (https://www.youtube.com/watch?v=BnYFwQEAJls, https://www.youtube.com/shorts/uWML1q2O-XI).
- **Soul ID**: urci minimum ~20 de poze din unghiuri diferite; în câteva minute învață fața (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- **Seedream**: Seedream 5.0 = cel mai bun pentru creaturi fantastice (aug. 2026) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ); Seedream 4.5 tier A (consistență fețe) (https://www.youtube.com/watch?v=nnGFEUeL-P0); Seedream 4.0 recomandat pentru refacerea unei imagini în 9:16 (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Flux 2 Pro: tier B. Reve: tier D (grafică). Z-Image: tier D, rapid și ieftin, dar nu acceptă imagini de referință. Kling O1 image și Wan 2.2 image: tier E (https://www.youtube.com/watch?v=nnGFEUeL-P0).

### Unelte de editare (ian. 2026)
- Inpaint (pensulă + „hand with five fingers”), Relight (culoare/direcție lumină), Insta Dump (multe poze dintr-un selfie), Photo Dump (la fel, pe Soul ID, mai consistent), Face Swap fără prompt, Mixed Media Studio (20+ preseturi pentru music video) (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Apps (fără prompt): Transitions, **Recast** (schimbă personajul din orice video în câteva secunde), **Shots** (9 cadre cinematice dintr-o imagine) (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Explore: poți clona toate asset-urile unui proiect publicat și să-l refaci (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Cele trei „efecte” de bază: **motion transfer** (mișcarea camerei + a personajului din orice video pe personaj nou în decor nou), **object swap** (schimbă un element: personaj, ținută, locație sau produs), **infinite camera angles** (o dublă → oricâte unghiuri) (https://www.youtube.com/shorts/l5BvSCfu7jQ).

### Cinema Studio 2 (2026-02-17)
- Imagine: alegi corp de cameră, obiectiv, focală, diafragmă (sau combinație recomandată); rezoluție 1K–4K; **grid 2×2 / 3×3 / 4×4 (până la 16 variante) plătind o singură generare** (https://www.youtube.com/watch?v=McwoKOIxIPY).
- Mod 3D (Gaussian splatting) din imagine: te miști în cadru și capturezi compoziția exactă (https://www.youtube.com/watch?v=McwoKOIxIPY).
- Multishot: auto sau manual — până la 6 scene, total max 12 s; pe scenă: durată, mișcare cameră (tracking, orbit, dolly), gen (action/comedy/horror…), speed ramp; personaje ca referință (fără drift de identitate) cu emoție per personaj; obiecte ca referință (inserează oameni/obiecte care nu sunt în cadrul de start) (https://www.youtube.com/watch?v=McwoKOIxIPY).
- Extragi cadrul de start/sfârșit din orice video → folosești ultimul cadru ca start pentru clipul următor (https://www.youtube.com/watch?v=McwoKOIxIPY).
- Calitatea videoului depinde mult de keyframe; reiterează keyframe-ul (https://www.youtube.com/watch?v=McwoKOIxIPY).

### 3D Jutsu / Blender / plugins
- 3D Jutsu (în browser): construiești blocking-ul scenei sau îl extragi (blocking + mișcare de cameră) dintr-un video de referință, apoi îl trimiți la Seedance; „economisești credite pe reroll-uri nesfârșite” (https://www.youtube.com/watch?v=vUYq38wC_xI).
- Plugin Blender + MCP: GPT-6 Astra construiește blocking cu cale de cameră editabilă; Nano Banana folosește cadrul din blocking ca referință de layout (https://www.youtube.com/watch?v=vUYq38wC_xI).
- Plugin Premiere Pro (2026-06-05): Edit video („remove the car”; „add an old man” + character sheet), selectezi zona și „change the outfit to pajamas”, „change the background…”, tranziție din cadru start + final („make a dynamic transition”), multi-shot cu alte unghiuri, **Reframe** în 9:16/4:3/21:9 (mai multe opțiuni), **Upscale** fără prompt (https://www.youtube.com/watch?v=DvRGamF7uRo).
- Plugin After Effects + skill-uri: motion graphics, localizare în alte limbi (inclusiv clipuri vorbite regenerate în Higgsfield), adaptare la vertical pentru reels (~50 min vs. 2–3 h manual) (https://www.youtube.com/watch?v=W3-RIZ-Ps64).
- Vibe Motion (2026-02-03): animație logo din imagine/prompt, editare fonturi/culori/stil (https://www.youtube.com/shorts/gslMMfs5SjM).

### Agenți / MCP
- Higgsfield MCP instalabil în ChatGPT/Claude (Higgsfield → „MCP and CLI” → install) (https://www.youtube.com/watch?v=7SZ76s-nqpQ); poate împărți scriptul în clipuri, genera, potrivi voce și muzică și monta singur (https://www.youtube.com/watch?v=7SZ76s-nqpQ).
- Supercomputer (mai 2026): agent cu 40+ unelte, 3 straturi de memorie; analizează videouri „cu adevărat” (audio, timing hook, căderi de retenție); conectori (ex. Telegram) (https://www.youtube.com/watch?v=4mT8s_09DRM).

---

## 2. Costuri și credite
- Hell Grind (film 90 min): 108.859 generări în 14 zile, **9.540.147 credite ≈ $400.000** cost de generare; total cu echipă ~$500k (https://www.youtube.com/watch?v=6aJ2BneDB5M). Calcul nostru (nu spus): ≈ $0,042 / credit.
- **Soul Cinema vs GPT: 7 credite = 1 generare GPT; aceleași 7 credite = 56 variante în Soul Cinema** → poți face batch-uri mari de locații (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Character sheet de dragon: „în 1 minut, cam 40 de cenți” (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Cinema Studio 2: grid până la 16 variante = preț de o singură generare (https://www.youtube.com/watch?v=McwoKOIxIPY).
- Modelele marcate „unlimited” → folosește-le pentru teste, nu arzi credite (https://www.youtube.com/watch?v=nnGFEUeL-P0). Exemple: Sora 2 unlimited o săptămână (oct. 2025) (https://www.youtube.com/watch?v=FSQ_IIIbtVI); Wan 2.5 unlimited o săptămână (https://www.youtube.com/watch?v=tmh_BBctfvk); Nano Banana Pro unlimited la lansare (https://www.youtube.com/shorts/51LAQ2Ntnrs).
- Dacă aceeași problemă apare în toate cele 4 batch-uri, de vină e promptul sau sursa — a continua batch-ul „arde credite degeaba” (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Character sheet pe fundal gri simplu: „am ars o grămadă de credite până am învățat asta” (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Lipstick brand complet (produs, site, videouri, lansare) = $121 credite Supercomputer, inclusiv generările ratate (https://www.youtube.com/watch?v=ttFWPdNInqg).
- Shot list: cere-i lui Claude să actualizeze doar ce s-a schimbat → −80% tokeni (https://www.youtube.com/watch?v=6aJ2BneDB5M).
- Promo 50% pe orice plan (doar în timpul streamului din oct. 2025) (https://www.youtube.com/watch?v=FSQ_IIIbtVI).

---

## 3. Fluxuri de lucru

### A. Recast personaj pe un video existent (Seedance v2v) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ)
1. Poză cu tine pe perete simplu → Claude scrie prompt de character sheet: „gray background, three angles: full body front, back, one close-up”.
2. Generezi în Cinema Studio cu Nano Banana 2 (fețe) și salvezi ca element („Adil hiking”) → e inclus automat în prompturi.
3. Tai clipul sursă în segmente; segmentele sub 4 s → freeze-frame pe ultimul cadru până la 4 s.
4. Dai clipul + sheet-ul lui Claude: „replace the character… keep the video one-to-one” (cu un skill de prompt pentru Seedance: unghiuri, lumină, mișcare).
5. Seedance, durata = 4 s ca referința, atașezi video + sheet → generezi.
6. Dacă pică în toate batch-urile → image-to-video din captura locației și lipești la montaj.

### B. Schimbare ținută / logo (https://www.youtube.com/watch?v=Hn8A8D4-SpQ)
1. Character sheet + logo → Claude → prompt pentru haine noi.
2. GPT Image 2 generează ținuta.
3. Verifici slop (logo deformat, culori albăstrui).
4. Corectură mică cu Nano Banana + prompt scurt: „Change the logo to the one in image two.”
5. Decupezi capul din cadrul full-body ca AI-ul să ia fața dintr-un singur loc (close-up).

### C. Scară corectă între personaje/obiecte („size fit frame”) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ)
- Combini un cadru din sheet-ul creaturii/obiectului cu sheet-ul personajului într-o singură imagine (Nano Banana 2) și o salvezi ca sheet separat → Seedance nu mai schimbă mărimile.
- Alternativ: captură din cadrul anterior + ambele sheet-uri → Claude → prompt pentru un asset nou de scară.

### D. Locații (https://www.youtube.com/watch?v=Hn8A8D4-SpQ)
1. Atașezi captura primului cadru din video original → Soul Cinema în batch.
2. Testezi candidații în video și alegi după lumină (lumina proastă = slop).
3. Blochezi locația ca element („waterfall location V1”).
4. Pentru unghi invers (camera/strada din partea opusă): descrii perspectiva lui Claude, atașezi asset-ul blocat, rulezi în Soul Cinema.
5. Locație din text: Claude scrie prompt „similar location based on this photo… same angle…”, Soul Cinema text-to-image fără imagini atașate.

### E. Lanț de clipuri consistente (https://www.youtube.com/watch?v=McwoKOIxIPY)
- Keyframe → animare (multishot) → extragi ultimul cadru → start frame pentru single shot-ul următor → repeți („build, animate, extract, repeat”).

### F. Fabrica de conținut UGC pentru produs (https://www.youtube.com/watch?v=ttFWPdNInqg, https://www.youtube.com/watch?v=4mT8s_09DRM)
1. Agentul caută produse (Amazon, Etsy, Shopify, Meta Ads) și citește recenziile ca să găsească plângerea comună → unghiul de vânzare.
2. Analizează conținutul top din ultimele 30 de zile din nișă → formate care merg (la ruj: ASMR, aplicare machiaj, GRWM, unboxing, talking/gossip).
3. Product sheet pe fundal curat, din mai multe unghiuri = ancora pentru toate vizualurile (listări, lifestyle, infografice).
4. Analiza reclamelor top Meta/TikTok/YouTube → 15 concepte (5 TikTok, 5 Meta, 5 Shorts), fiecare cu hook și format propriu.
5. UGC: Soul (personaj) + Seedance 2.0 (animație).
6. Datele de analytics se dau înapoi agentului → „double down” pe ce merge (la ei: mai mult ASMR).
- Rezultat raportat: 500.000 views pe un cont IG de 3 zile, 0 followeri, fără reclame plătite; 833 înscrieri pe waitlist (https://www.youtube.com/watch?v=ttFWPdNInqg).

### G. Sora 2 pentru reclame produs (https://www.youtube.com/watch?v=FSQ_IIIbtVI)
1. Imaginea produsului pe fundal alb.
2. Dacă imaginea nu e 9:16 → apar benzi negre chiar dacă alegi 9:16. Soluție: Seedream 4.0, 9:16, „recreate this exact image. Do not change anything.”
3. Preset din Sora Trends + prompt scurt SAU prompt structurat (shot list / detaliat, vezi Prompting).

### H. Format viral „banal → transformare” (https://www.youtube.com/shorts/_U66oOC4_Tc)
1. Scenă banală intenționat (fată la volan). 2. O amenințare care rupe calmul. 3. Transformarea — arăți CUM se întâmplă (mișcarea camerei în acel moment). 4. O singură acțiune puternică, curată. 5. Revenire la normal.

### I. Blocking 3D → video (https://www.youtube.com/watch?v=vUYq38wC_xI)
- Blocking (forme simple, cale de cameră) → export video ca referință de mișcare + imagine de locație (Nano Banana pe cadrul de blocking) + character sheet → Seedance 2.5. Coregrafia o pui în prompt ca să nu copieze mișcarea rigidă a blocking-ului. La reclame: finalul pe produs.

---

## 4. Prompting

### Cele 28 de sfaturi ale echipei Hell Grind (https://www.youtube.com/watch?v=6aJ2BneDB5M)
1. Scene emoționale: context situațional + comportament anatomic (braț întins, degete răsfirate, maxilar căzut, dinți vizibili, „no tears”, distanța „2 in”, aterizează în mâini și genunchi). Fără asta reacțiile ies robotice.
2. La imagini scrie ca un fotograf: obiectiv, diafragmă („stopped down two stops from wide open”, deep focus), granulație, film stock, halation, bokeh, sursa luminii („cool blue light spills through the curtains…”). „Photorealistic, cinematic, high quality” nu fac nimic. Dacă nu știi echipamentul: dai lui Claude un cadru din film și întrebi ce cameră și ce obiectiv s-au folosit.
3. System prompt pentru aderență (cu link în descriere): reguli de seed și limbaj sigur; reguli pentru text pe ecran; densitate: **un cadru = o idee, o acțiune, o strategie de cameră**; disciplina referințelor; alegerea modului (text→video, imagine→video, referință→video, video→video); setări de output; **sistem de coordonate al cadrului** (ex. „personajul la 20% pe X, 30% pe Y” — modelul respectă).
4. Prima rundă aproape niciodată nu iese; iterezi. Dacă primele 5 s din 15 sunt bune, spui să schimbe doar ultimele 10 s.
5. Single shot pentru aproape tot; multi-shot doar pentru acțiune/dialog dinamic. În single shot poți defini ce se întâmplă la fiecare secundă.
6. Multi-shot: o generare cu mai multe tăieturi în aceeași locație ține lumina și pozițiile consistente; tai apoi bucățile bune.
7. Dialog: transcriere fonetică pentru cuvinte grele.
8. Cât mai detaliat (când tai, ce unghi, la cine) → mai puțin loc de halucinat mișcarea greșită.
9. Captură din momentul bun al unui video ratat → la Claude ca referință de poziționare/lumină pentru promptul următor.
10. Shot list: actualizezi doar ce s-a schimbat.
11. Prompt prea lung, cu instrucțiuni care se contrazic → ceri lui Claude să-l optimizeze/„sanitizeze”.
12. Regula culorilor 60-30-10 (dominantă / secundară / accent).
13. Lumină artificială „ca din spate” = aspect plastic, personaje lipite → scrie „practical light only” (soare, ferestre, lămpi din cadru).
14. Dialog: începi cu un cadru de stabilire (wide/medium) → tăieturile următoare păstrează pozițiile.
15. Fiecare locație are o ancoră (copac, cărți) → „pune-l pe X în stânga copacului”, „camera lângă cărți”.
16. **Nu genera locații din față** — Seedance nu înțelege adâncimea; folosește trei sferturi sau colț de tavan tip CCTV.
17. Împarte locația pe vederi (față / spate ca imagini separate) și spune în prompt „pentru tăietura 1 folosește vederea asta”.
18. Desenează scena înainte: Claude face o hartă de sus (top-down), o iterezi, apoi pui prefixul de poziționare în prompt.
19. Acțiune: scenariu pe bătăi — cine, unde, ce armă, coregrafia, pe fiecare tăietură.
20. Decupează fața din cadrul wide al character sheet-ului (acolo e plastică / nu seamănă).
21. Prop sheet pentru recuzita dificilă (exterior + interior) — a rezolvat „gheara ținută ca o sabie”.
22. Urmărește starea fiecărui personaj (răni, haine, recuzită) și blochează-le înainte să generezi.
23–24. Echipe de câte doi; un „slop director” care validează; toate asset-urile pe un canvas.
25. Verificare cadru cu cadru („un cadru prost strică tot planul”).
26. Dacă scad FPS-urile → ștergi cadrele duplicate.
27. O generare ratată poate avea 1–2 s perfecte → le tai și le folosești.
28. Treci mai departe și revii mai târziu cu ochi proaspeți.

### Alte reguli de prompt
- Nu scrie „make it more natural” (nu face nimic); descrie imaginea fizică a mișcării (viteză normală, se împinge din apă, se mișcă ca un șarpe) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Emoție reală: descrie fața în detaliu, ce trăiește personajul, ce spune, cum îi sună vocea, ce fac mâinile (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Începe în mijlocul acțiunii: fără apropiere, fără intro gol (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Cadre rapide: „180-degree camera orbit”, „speed shake”, „lens droplets”; specifică mereu fizica mișcării (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Primul cadru trebuie să prindă atenția; dacă e static, începe cu o mișcare (ex. camera iese din nori) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Creatură complexă: două close-up-uri (gura deschisă / închisă) în sheet ca să nu „glitch-uiască” fața (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- Voce consistentă între generări: Seedance „blochează” vocea dintr-un element de referință (numele exact e neclar în transcriere: „cap kishi”) (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- POV: spune explicit ce NU face camera: „no cuts, no zooms”, eventual „natural head movement” (https://www.youtube.com/shorts/c4ddLt57aQ4).
- Sora 2: stilul se scrie la început (UGC iPhone raw, cinematic ad, anime opening, Lego, 3D…) (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Sora 2 shot list cu timecode, bucăți de 2–3 s → tăieturi bune; hook în primele 3 s, apoi bază, climax, rezolvare (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Promptul Sora detaliat are secțiunile: format & ton, subiect principal, garderobă, recuzită (+ secundară), locație, încadrare, lumină, reguli de continuitate, acțiuni cu timestamp, plan de montaj, logo/produs, dialog, foley, finisaj (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Shot list → control tăietură cu tăietură; prompt detaliat → control pe cum arată subiectul, haine, loc, stil (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Modelele de editare cu raționament (Seedream, NB): prompt directiv, nu descriptiv („recreate this exact image”) (https://www.youtube.com/watch?v=FSQ_IIIbtVI).
- Cerere pentru o compoziție anume: nu te baza doar pe text, trage o imagine de referință; start frame / end frame = ancore (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Image-to-video dă cel mai consistent rezultat; text-to-video doar pentru teste rapide (https://www.youtube.com/watch?v=nnGFEUeL-P0).
- Camere/obiective numite (Alexa, anamorfic) dau un aspect apropiat, nu identic (https://www.youtube.com/watch?v=FSQ_IIIbtVI).

---

## 5. Probleme și soluții
| Problemă | Soluție | Sursă |
|---|---|---|
| v2v Seedance refuză/clip prea scurt | Freeze-frame până la 4 s; durata = 4 s | https://www.youtube.com/watch?v=Hn8A8D4-SpQ |
| Aceeași eroare în toate 4 batch-urile | Oprește-te; schimbă promptul/sursa sau treci pe image-to-video | https://www.youtube.com/watch?v=Hn8A8D4-SpQ |
| Fața derapează în video | Decupezi capul din full-body; Seedance ia fața din close-up | https://www.youtube.com/watch?v=Hn8A8D4-SpQ, https://www.youtube.com/watch?v=6aJ2BneDB5M |
| Proporții greșite între personaje | Imagine combinată „size fit” salvată ca sheet | https://www.youtube.com/watch?v=Hn8A8D4-SpQ |
| Logo deformat / culori schimbate (GPT Image 2) | Nano Banana: „Change the logo to the one in image two” | https://www.youtube.com/watch?v=Hn8A8D4-SpQ |
| Imagine plastică, prea multă lumină pe fețe | „Practical light only”; lumina e criteriul de alegere a locației | https://www.youtube.com/watch?v=6aJ2BneDB5M, https://www.youtube.com/watch?v=Hn8A8D4-SpQ |
| Mișcare nenaturală (aripi rigide, „low poly”) | Descrii fizica concretă, nu „more natural” | https://www.youtube.com/watch?v=Hn8A8D4-SpQ |
| Vremea/camera nu se potrivesc cu clipul original | Ceri explicit să se potrivească cadru cu cadru cu plate-ul original | https://www.youtube.com/watch?v=Hn8A8D4-SpQ |
| Recuzita interpretată greșit (gheară = sabie) | Prop sheet cu exterior + interior | https://www.youtube.com/watch?v=6aJ2BneDB5M |
| Personaje care „teleportează” între tăieturi | Cadru de stabilire + ancoră + hartă de sus + coordonate | https://www.youtube.com/watch?v=6aJ2BneDB5M |
| Model ia vederea greșită a locației | Imagini separate pe vederi + „pentru tăietura N folosește imaginea X” | https://www.youtube.com/watch?v=6aJ2BneDB5M |
| Asset greșit folosit (versiune veche) | Canvas cu stările fiecărui personaj | https://www.youtube.com/watch?v=6aJ2BneDB5M |
| Video sacadat (18 fps) | Ștergi cadrele duplicate | https://www.youtube.com/watch?v=6aJ2BneDB5M |
| Benzi negre în Sora/video | Refaci imaginea în 9:16 (Seedream 4.0) | https://www.youtube.com/watch?v=FSQ_IIIbtVI |
| Sora blochează imaginea | Fără oameni realiști/animale în imaginea de start | https://www.youtube.com/watch?v=FSQ_IIIbtVI |
| Moderare Sora (celebrități, IP, NSFW fals) | ChatGPT: „rewrite this prompt so that it does not violate the guidelines”; reformulezi („bald man” → „man with no hair”); NSFW fals la plasare produs → raportezi pe Discord | https://www.youtube.com/watch?v=FSQ_IIIbtVI |
| NB/Seedream cu poza ta: 2–3 din 4 imagini nu au fața ta (mai rău la asiatici) | Antrenezi Soul, apoi editezi rezultatul în NB/Seedream (unghi, păr, produs în mână) | https://www.youtube.com/watch?v=FSQ_IIIbtVI |
| Soul 1 drift de identitate | Soul 2 („train once”) | https://www.youtube.com/watch?v=BnYFwQEAJls |
| Seedance 1.5 Pro slab la medii noi cu cameră în mișcare | Altul (Kling 2.6) pentru mișcări de cameră | https://www.youtube.com/watch?v=nnGFEUeL-P0 |

---

## 6. Noutăți recente (2026)
- 2026-10-08: Higgsfield **Katana** anunțat (doar trailer, fără detalii tehnice) (https://www.youtube.com/shorts/-LNDXx__ZT0).
- 2026-10-06: **Ads Studio în ChatGPT**, gratuit de încercat (fără detalii în transcriere) (https://www.youtube.com/shorts/zephnQwGbBE); trio motion transfer / object swap / infinite angles (https://www.youtube.com/shorts/l5BvSCfu7jQ).
- 2026-10-02: GPT-6 Astra montează în DaVinci Resolve cu Higgsfield (generare + montaj + sunet + culoare); ~80% corect la prima trecere (https://www.youtube.com/watch?v=kOoC3yhUyDQ).
- 2026-09-21: plugin After Effects + skill-uri (localizare, resize vertical) (https://www.youtube.com/watch?v=W3-RIZ-Ps64).
- 2026-09-12: plugin Blender, 3D Jutsu în browser, Seedance 2.5 cu blocking până la 30 s (https://www.youtube.com/watch?v=vUYq38wC_xI); Effects 2.0 în ChatGPT (https://www.youtube.com/shorts/tx3pcpC_0qA).
- 2026-09-04: Higgsfield MCP în ChatGPT (GPT-6) (https://www.youtube.com/watch?v=7SZ76s-nqpQ).
- ~2026-08-07: **Seedance 2.5** lansat pe Higgsfield; Seedream 5.0 și Nano Banana 2 în Cinema Studio (https://www.youtube.com/watch?v=Hn8A8D4-SpQ).
- 2026-07-16/17: construire de aplicații cu Higgsfield MCP + concurs $100k; scenă 3D cu cale de cameră → video care urmează exact calea (https://www.youtube.com/shorts/sMVZgSMMZ4I).
- 2026-06-05: plugin Premiere Pro (edit, reframe, upscale) (https://www.youtube.com/watch?v=DvRGamF7uRo).
- 2026-06-03: preseturi virale (Kung Fu Hit, Race Track, Football Invader, Android Assemble): poza ta → generate (https://www.youtube.com/shorts/VXShPRPlfu0).
- 2026-05-28: **GPT Image 2** (text fin, carduri de produs) (https://www.youtube.com/shorts/7YUTjb27Mto).
- 2026-05-19: **Supercomputer** (agent cu 40+ unelte) (https://www.youtube.com/watch?v=4mT8s_09DRM).
- 2026-04-11: Seedance 2.0 global (https://www.youtube.com/shorts/wn64gYE73JY).
- 2026-03-17: concursul Action Scene: 8.752 înscrieri din 139 de țări (https://www.youtube.com/watch?v=babNcxpwnx0).
- 2026-02-20: **Soul 2** (https://www.youtube.com/watch?v=BnYFwQEAJls); 2026-02-17: **Cinema Studio 2** (https://www.youtube.com/watch?v=McwoKOIxIPY); 2026-02-03: Vibe Motion (https://www.youtube.com/shorts/gslMMfs5SjM).
- 2026-01-29: clasamentul modelelor (Kling 2.6 S, Sora 2 S, Veo 3.1 A, Seedance 1.5 Pro B; imagini: Nano Banana Pro S, Soul A, Seedream 4.5 A) (https://www.youtube.com/watch?v=nnGFEUeL-P0).
