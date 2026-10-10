# Note Higgsfield YT — part2 (oct 2026 → mai 2025)

Sursa: `chunks/part2.txt` (49 videouri, citit integral). Doar ce e spus explicit în transcrieri.
Atenție: transcrierile automate stâlcesc numele („Hixel”, „Kicksfield”, „HeyGen”, „Picsel” = Higgsfield; „Cedance/C dance/Cance” = Seedance; „Cadream/Cream” = Seedream; „Clot/Claw” = Claude).
Fără conținut util (sărite): Creator Partnership, K-Drama/API shorts, Motion Designer short, Adiliada, Zephyr, Hell Grind, Arena Zero, knocker-up, Empire State, Cannes, DaVinci plugin, Museum Heist, PhotoDump, Lipsync Studio (doar teaser), Product-To-Video (doar muzică), GPT-5 launch, Soul teaser, Canvas teaser, Effects Pack 3.
**Nu apar deloc în part2:** Genjutsu, Kling motion control, Wan, Katana, upscale, relight, reframe (ca unealtă detaliată), Speak.

---

## 1. Unelte / modele

### Seedance 2.5 (în Cinema Studio)
- Folosit pentru scene de 30 s, 1080p; înțelege mai bine promptul decât 2.0 → mai puține batch-uri; „pe 2.0 lupta asta m-ar fi costat de două ori mai multe generări”; fizică bună la mișcări rapide, membrele nu se deformează ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).
- Acceptă **referință audio** (ex. memo vocal cu o melodie fredonată) → personajul cântă exact notele; fără ea, modelul inventează altă melodie la fiecare take ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).
- Ofertă „33 Days of Unlimited Seedance 2.5” (short din 2026-08-07) ([6l3Nt0T2Kow](https://www.youtube.com/shorts/6l3Nt0T2Kow)).

### Seedance 2.0 / „Seedance 4K”
- Parametri folosiți: 21:9 sau 16:9, **4K**, **15 s**, 4 batch-uri per prompt ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- 4K merită: explozii clare, „aproape zero slop pe obiecte”, toate take-urile din primul batch utilizabile ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Generează automat o **voce unică per personaj**, potrivită cu aspectul din character sheet → dacă blochezi imaginea, blochezi și vocea ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- **Nu înțelege prompturile negative** („he's not crying” → face opusul / se încurcă) ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Planifică scenariul cu shot-uri de max 15 s = o generare Seedance per shot ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Schimbă stilul unui video, construiește video din prompt de 7 cuvinte, fizică bună la obiecte mari, slow-mo; poate pune un personaj desen 2D într-o scenă live-action ([tSBhlLc5CpA](https://www.youtube.com/shorts/tSBhlLc5CpA), [gWJUYRS2ri0](https://www.youtube.com/shorts/gWJUYRS2ri0)).

### Cinema Studio (2.5)
- Proiecte cu foldere/subfoldere per scenă și per asset ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs), [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
- **Characters**: gen, buget (ex. 100 mil), eră, arhetip (fără prompt), identitate, aspect fizic, ținută custom → 4 imagini la **0,5 credite**, vine cu character sheet complet ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- **Locations**: 4 imagini la 0,5 credite ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- **Scenes**: selectezi personaje + locație + prompt → keyframe (16 credite pentru câteva încercări) ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- **Video**: single shot; **multi-shot auto** (unghiuri diferite, ~96 credite/rulare); **multi-shot manual** (durate per shot, ex. 5 s + 7 s); start frame + end frame; mișcări de cameră predefinite (ex. „zoom in” cu prompt gol) ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- **Re-camera pe video existent**: urci un clip static, alegi mișcarea (handheld, POV etc.) → aceeași scenă, cameră nouă, reflexiile se mișcă natural ([fw5WXmArO1I](https://www.youtube.com/shorts/fw5WXmArO1I)).

### Soul Cinema (imagini)
- Cel mai bun pentru locații (varietate mare dintr-un prompt); „8 imagini = 1 credit” / „sub jumătate de credit pe rulare”; bun pentru personaje inventate și „raw pass” de recuzită ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs), [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Setare folosită pentru character sheet: 16:9, 2K ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).

### Soul 2.0 / Soul ID
- Supercomputer folosește Soul 2.0 pentru personaje; Soul ID = model de identitate antrenat care ține fața în toate generările ([YX7nE-3rYEQ](https://www.youtube.com/watch?v=YX7nE-3rYEQ)).

### GPT Image 2.0 (și 2.5)
- „Cel mai bun model acum pentru editare și character sheet fotorealist când ai deja referință” ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
- Rol: editări finale și sheet curat după raw pass-ul din Soul Cinema; schimbă logo/număr pe tricou; combină ținuta + character sheet („create a character in this uniform”) ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Logo/produse/brand kit: 4K, 16:9, 4 variante; ajunge o direcție scurtă, nu un paragraf ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).
- Desen-schiță de proporții (creion) pentru a fixa înălțimi ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).
- În skill-ul de ads din GPT-6 Astra: GPT Image 2.5 pentru static, Seedance pentru video, Seedream pentru personaje ([gVPZU1btFA8](https://www.youtube.com/watch?v=gVPZU1btFA8)).

### Seedream (5 Pro)
- Bun la fețe și texturi de haine; Seedream 5 Pro = costum cu cea mai multă textură, consistent în toate panourile; GPT Image 2 a ținut mai bine buclele părului. „Fiecare model are punctul lui forte, alege per job” ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).

### Marketing Studio
- **UGC**: alegi avatar, urci produsul (câte unul per ad), prompt scurt + o replică; setări 9:16, 1080p, 15 s ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).
- **Hook presets** (update nou, mai 2026): ex. „Epic fail”, „Product crush”, „spicy”, „Random object mic”; **Settings** (locații: acoperiș, vulcan, aripă de avion); se combină hook + setting + avatar → ad diferit pe alt public; merge și fără prompt deloc ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM), [spB-F47ZNJM](https://www.youtube.com/shorts/spB-F47ZNJM)).
- Avatar custom din prompt („elegant 60-year-old woman”) ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).
- **Hyper motion**: produs + locație ca al doilea input + prompt scurt de mișcare; look de campanie luxury ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM), [2OwMjg5As2g](https://www.youtube.com/watch?v=2OwMjg5As2g)).
- **Wildcard** (commercial, ~9 $) și **TV spot** (personaj + locație + prompt de 5 cuvinte; 16:9, 15 s, 1080p) ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).
- Limită: un singur avatar per generare → al doilea personaj se atașează ca referință ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).
- Preset SaaS ales automat din link-ul site-ului; textul nu se mai topește/deformează ([2OwMjg5As2g](https://www.youtube.com/watch?v=2OwMjg5As2g)).

### Higgsfield MCP / Supercomputer
- MCP: în Claude (sau alt LLM) → Settings → Connectors → lipești link-ul → toate uneltele Higgsfield în chat ([RQck4CUKu5g](https://www.youtube.com/shorts/RQck4CUKu5g), [2OwMjg5As2g](https://www.youtube.com/watch?v=2OwMjg5As2g)).
- Supercomputer (lansat ~mai 2026): agent cu skills făcute de echipa Higgsfield; analiză vizuală directă pe cadre (hook, ritm); **Model Orchestrator** rutează fiecare pas la modelul potrivit, nu cel mai scump → „reducere de 15x a costului”; **Elements** = strat de referințe (personaje, locații, recuzită, brand) refolosit în toate shot-urile; skill „Cinematic Flow” (Soul Cinema → elemente → Seedance 2.0 → lipire); 27+ conectori (Telegram, Gmail, Slack…); programare zilnică (ex. 9:00) ([YX7nE-3rYEQ](https://www.youtube.com/watch?v=YX7nE-3rYEQ), [qiTfvA1u0Hs](https://www.youtube.com/shorts/qiTfvA1u0Hs)).

### Kling 3.0 (lansat pe Higgsfield ~feb 2026)
- Video de până la 15 s, **multi-shot** până la 6 tăieturi într-o generare; i2v e ce folosești „95% din timp” ([jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8)).
- La i2v „less is better” (ex. doar „strong emotions”); emoții/fizică/dialog mult mai bune ca 2.6; lip sync bun pe mai multe unghiuri ([jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8)).
- **Referință de față**: urci fața separat → o inserează și nu o deformează chiar dacă în start frame persoana e cu spatele ([jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8)).
- Mișcări de cameră complexe executate exact (lateral pass, crash push-in, pull back); zoom handheld care se oprește exact pe acțiune; start + end frame ([jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8)).
- Cele mai bune rezultate la **≤12 s**, deși permite 15 ([jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8)).

### Veo 3.1 (lansat oct 2025)
- Durate doar 4/6/8 s (nu 30); 720p/1080p; „fast” = mai rapid, calitate mai mică ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)).
- **Ingredients**: până la 3 imagini referință (persoană, produs, scenă), doar 16:9; start/end frames ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)).
- Bun pentru scene lente: reclame de produs UGC sau cinematice; ~4 tăieturi merg; text pe ecran redat bine chiar la 720p ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)).
- Slab: asemănarea feței cu poza încărcată („nu arată ca mine”); sunetele de fundal „ieftine”; Sora 2 mai bun la tăieturi, ritm, continuitate ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)).

### Sora 2
- Sketch-to-video pe Higgsfield (din desene → storyboard → film) ([6PToCT9nocc](https://www.youtube.com/watch?v=6PToCT9nocc)).
- Are „diffusion boiling”/flicker → se repară cu „Sora 2 enhancer” de pe Higgsfield ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)).

### Nano Banana Pro (lansat nov 2025)
- Până la **14 imagini referință** într-un output consistent; 4K; raționament (stări în timp, planuri, exploded view) ([II9AdFNgzpU](https://www.youtube.com/watch?v=II9AdFNgzpU)).
- Use case-uri utile: „unpack the items” din pungi pe pat; outfit breakdown; magazin online/brand book dintr-o poză de produs ([II9AdFNgzpU](https://www.youtube.com/watch?v=II9AdFNgzpU)).

---

## 2. Costuri și credite
- Soul Cinema: 8 imagini = 1 credit; personaj/locație Cinema Studio: 4 imagini = 0,5 credite; o imagine de perete = 0,125 credite; Nano Banana = 2 credite/generare ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- Cinema Studio video: multi-shot auto ≈ 96 credite; o scenă grea ≈ 192 credite cu ratări; start+end frame simplu = 8 credite; reclamă completă (perfum, ~3 min) = **5.420 credite, 6 ore, plan Creator** ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- Motion graphics: ~1.800 credite ≈ 70 $ pentru toate stilurile cu tot cu ratări ≈ 5 $/video ([2OwMjg5As2g](https://www.youtube.com/watch?v=2OwMjg5As2g)).
- Ads ecom/servicii statice + video, cu iterații: ~100 $ total ([gVPZU1btFA8](https://www.youtube.com/watch?v=gVPZU1btFA8)). Commercial Wildcard ≈ 9 $ ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).
- Generările blocate de ghiduri **nu consumă credite** ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)).
- Unlimited periodic: Veo 3.1 o săptămână pentru Creator/Ultimate (oct 2025); Kling 3.0 unlimited la lansare (feb 2026); Nano Banana Pro „un an unlimited” (nov 2025); „7 days unlimited” (iul 2026); Seedance 2.5 „33 days unlimited” (aug 2026) ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8), [jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8), [II9AdFNgzpU](https://www.youtube.com/watch?v=II9AdFNgzpU), [F0rbPLjBnns](https://www.youtube.com/shorts/F0rbPLjBnns), [6l3Nt0T2Kow](https://www.youtube.com/shorts/6l3Nt0T2Kow)).
- **Trucuri de economie:**
  - Storyboard de 9 cadre întâi; repari la imagine, apoi o folosești ca referință la video ([2OwMjg5As2g](https://www.youtube.com/watch?v=2OwMjg5As2g)).
  - Prompt detaliat de keyframe scris de LLM („Give me a detailed prompt to generate a keyframe. I want a …”) → mai puține generări ratate ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
  - Fixează întâi locația/unghiul corect, abia apoi adaugi persoana ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
  - În aceeași locație, nu genera start frame-uri noi: ia un unghi bun din multi-shot și continuă de acolo ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
  - Fundal gri la character sheet → rată de reușită mai mare ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
  - Desen de geometrie în loc de descriere: „fiecare batch ratat evitat = credite salvate” ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
  - Dacă toate 4 din batch sunt greșite, problema e promptul, nu norocul ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
  - Seedance 2.5 vs 2.0: ~jumătate din batch-uri pentru aceeași scenă ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).
  - Testează creativele ca reels organice înainte de buget plătit ([gVPZU1btFA8](https://www.youtube.com/watch?v=gVPZU1btFA8)).

---

## 3. Fluxuri de lucru

**A. Personaj consistent (fără drift de față)**
1. Character sheet pe **fundal gri**: față + spate + close-up separat (close-up = fața pe care se blochează; full body = înălțimea) ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
2. Lumină moale, fără umbre dure pe față, fără reflexii în păr ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
3. **O singură față pe sheet**: șterge fața din panoul full-body (GPT Image 2) — altfel Seedance nu știe ce față să ia și personajul derivă până la scena 5 ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
4. Persoană reală: păstrezi costumul/corpul din sheet-ul generat, ștergi capul din panoul principal și lipești poza reală în panoul de portret → fețe naturale + ținută consistentă ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).
5. Salvează ca **Element** cu nume; folosește același nume în prompt → se atașează automat ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
6. Schimbare de stare (haine rupte, altă ținută) → sheet nou cu personajul deja în starea nouă ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
7. Figuranți: 10 personaje pe fundal gri într-un singur element („crew”) ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)). Un personaj care apare o singură dată poate veni doar din prompt ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).

**B. Locație / cameră consistentă**
- Locația face „~70% din calitatea video-ului”; generează mai multe în Soul Cinema și alege: spațiu liber pentru acțiune, laturi aglomerate, mijloc curat; fără nuanțe de culoare care se scurg în toate scenele ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).
- Scrie „**3/4 angle**” în prompt → profunzime, mai multe reușite decât cadrul frontal plat ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Prompt de locație = detalii + lumină + sentimentul imaginii ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- Pentru contraunghiuri: generează **imagini cu ambele părți ale camerei** ca referință → fundalul nu mai sare între tăieturi ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
- Atașează texturile peretelui și podelei pentru unghiuri noi în aceeași cameră ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- Un sub-loc important (ex. oaza) = asset de locație separat ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).

**C. Produs consistent**
- Prompt: „Use the products from the attached image exactly as shown. Preserve their shape, design, and proportions. Do not redesign them.” → logo-uri și produse păstrate ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).
- Recuzita recurentă = prop sheet separat pe fundal gri; fixează explicit mărimea obiectului în prompt dacă variază ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y), [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).

**D. Ad UGC rapid (Marketing Studio)**: avatar → produs (unul) → prompt scurt + replică („Okay, I finally got it.”) → opțional hook preset + setting → 9:16, 1080p, 15 s ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).

**E. Reclamă cinematică (Cinema Studio)**: personaje → locații → keyframe (scenes) → video din start frame → ultimul cadru devine start frame-ul următor → multi-shot auto, alegi unghiurile → montaj ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)). Tranziție: start frame fără element + end frame cu element (ex. lasere apar) ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)). Match cut: atașează ultimul cadru al scenei anterioare ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).

**F. Reproducere 1:1 după referință**: urci videoul de referință în Claude + MCP, ceri prompt pentru exact același video → rezultat aproape identic (la ei a pornit din imagini statice; se pot anima după) ([2OwMjg5As2g](https://www.youtube.com/watch?v=2OwMjg5As2g)).

**G. Ads din cercetare (Meta Ad Library)**: reclamele care rulează de mult și au reach mare = cele care convertesc; analizează ce au în comun în nișă; cele mai simple vizual convertesc cel mai bine; format UGC citit de algoritm drept conținut, nu reclamă → CPA mai mic; A/B: schimbă un singur element o dată (hook, vizual, bonus); urmărește hook rate, CTR, cost per lead ([gVPZU1btFA8](https://www.youtube.com/watch?v=gVPZU1btFA8)).

**H. Asamblare**: nu există render perfect de 30 s; generezi material brut (4 take-uri/prompt) și combini cele mai bune bucăți din batch-uri diferite ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs), [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).

**I. Voce proprie (Sora 2 / Veo)**: generezi video → extragi audio → separi vocea de zgomote → ElevenLabs speech-to-speech cu vocea ta → înlocuiești în montaj ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)). Replica cu emoție se poate genera într-un clip separat și se pune peste altul ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).

---

## 4. Prompting
- Promptul video îl scrie un LLM cu skill de „director”, din descriere simplă + asset-uri atașate; iterezi: rulezi, te uiți, ceri modificări exacte, rulezi iar ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- **Descrie mecanica fizică**, nu rezultatul: nu „se ciocnesc”, ci „umerii se lovesc, valizele se balansează, inerția îi duce o jumătate de pas, se întorc pe picioare” ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).
- Toți figuranții „mereu în mijlocul unei acțiuni” în fiecare cadru (altfel stau și se holbează) ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs)).
- **Spațiu/proporții → desenează**: schiță simplă (chiar urâtă) salvată ca element; „un desen spune ce nu spun 10 propoziții” ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs), [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
- Fără negații: scrie ce vrei („anxious look”), nu ce nu vrei ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Împarte: acțiune/fizică și actorie în prompturi separate; 30 s → 2-3 prompturi de 15 s, ca să aibă timp emoția ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Începe cu **plan larg de stabilire** → Seedance așază personajele și le ține pe poziție tot clipul ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Personajul să reacționeze la ce se întâmplă (micile reacții fac scena reală) ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
- Cameră: push-in, Dutch angle (cadru strâns = personaj „prins”), **handheld** (mișcări subtile de mers/respirație = realism), speed ramp (slow-mo în momentul cheie), whip pan (dă-i durata, etichetează subiecții A, B, C; trebuie să se termine pe același tip de cadru cu care a început) ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Dialog: regula 180°, cameră statică, același unghi pentru fiecare vorbitor, contracâmp peste umăr; descrie tonul și pauzele (ex. „micro pauses, trembling voice”) ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- Lumină și culoare: setează în prompt cald/rece, vreme, ora din zi; paleta se fixează la fiecare locație nouă/flashback; detalii mici de lumină (raze) fac imaginea reală ([0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y), [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc)).
- Text-to-video (Kling 3.0): cine, unde, ce face, ce face camera ([jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8)). Image-to-video: mai puțin e mai bine ([jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8)).
- Marketing Studio: prompturi foarte scurte („a dreamy pearl world ad”); mișcare: „camera orbits to a slow-mo hero shot, no cuts, one continuous motion” ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM)).
- Veo 3/3.1: merg bine prompturile structurate cu **timeline pe secunde** (0–2 s, 2–4 s…); schemă JSON: shot, compoziție, mișcare cameră, frame rate, grain, subiect, garderobă, locație, ora, acțiune, recuzită, fizică, lumină, paletă, audio (voce, limbă, accent, replici exacte, sunete), muzică=false dacă nu ceri, fără subtitrări, elemente interzise ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)).
- Veo: nu scrie replicile cu MAJUSCULE (le citește ca abrevieri); pentru vorbire rapidă, scoate toată punctuația ([DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8)).
- Pentru „hook” în primele 2 secunde: senzație de pericol, imagine fascinantă sau frază provocatoare pe ecran ([spB-F47ZNJM](https://www.youtube.com/shorts/spB-F47ZNJM)).

---

## 5. Probleme și soluții
| Problemă | Soluție | Sursa |
|---|---|---|
| Fața derivă de la scenă la scenă | O singură față pe sheet (șterge fața din full-body) | [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc) |
| Fața arată ca „un actor sosie” | Hibrid: costum din sheet + poza reală lipită pe portret | [QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs) |
| Fața nu e vizibilă în start frame (Kling) | Referință de față separată | [jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8) |
| Mărimi inconsistente (gigant, obiect) | Schiță de proporții ca referință; mărime fixată în prompt | [QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs), [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc) |
| Obiecte multe pe masă se contopesc / dezordine devine „mush” | Mai puțină recuzită; locație cu mijloc curat | [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs) |
| Fundal care sare între contracâmpuri | Referințe cu ambele părți ale camerei | [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc) |
| Haina ruptă „se coase la loc” | Sheet nou cu starea schimbată | [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc) |
| Aspect cartoon/plastic (animale, mâini) | Schimbi asset-ul cu unul mai simplu/realist; ține variante pregătite; regenerezi mâinile | [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y) |
| Multi-shot POV eșuează | Un singur shot continuu, apoi rafinezi | [CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc) |
| Scenă grăbită în 15 s | Împarte în 2-3 prompturi | [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y) |
| Text scris = mâzgăleli | Regenerezi shot-ul | [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y) |
| Imagine non 9:16/16:9 la Veo → benzi negre | Încarcă exact raportul cerut | [DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8) |
| webp/avif nu sunt acceptate (Veo) | Convertește în jpg/png | [DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8) |
| Refuz „against guidelines” | Fața seamănă cu o celebritate → schimbi persoana; nu numi oameni, descrie-i; versuri recunoscute; cuvinte ca crash/violență → rescrie cu LLM; blocarea poate veni din imagine, nu din prompt. Branduri ca Red Bull/Prada pe produs au trecut | [DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8) |
| Sora 2 flicker | Sora 2 enhancer | [DcoBYbytZp8](https://www.youtube.com/watch?v=DcoBYbytZp8) |
| Melodia inventată la cântat | Referință audio | [QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs) |

---

## 6. Noutăți recente (2026)
- 2026-10-03: GPT-6 Astra + Higgsfield MCP pentru ads (skill: GPT Image 2.5 static / Seedance video / Seedream personaje) ([gVPZU1btFA8](https://www.youtube.com/watch?v=gVPZU1btFA8)); Creator Partnership Program ([EP5jfyCnPu8](https://www.youtube.com/shorts/EP5jfyCnPu8)).
- 2026-09-19/21: Higgsfield API pentru aplicații ([RUXYWv40QTk](https://www.youtube.com/shorts/RUXYWv40QTk)).
- 2026-09-02: Claude Fable 5.1 + Marketing Studio video presets (SaaS, hypermotion, 3D real-estate, explainer, editorial) prin MCP; text pe ecran stabil ([2OwMjg5As2g](https://www.youtube.com/watch?v=2OwMjg5As2g)).
- 2026-08: Seedance 2.5 (30 s, 1080p, referință audio), 33 zile unlimited ([QfylrxtQSSs](https://www.youtube.com/watch?v=QfylrxtQSSs), [6l3Nt0T2Kow](https://www.youtube.com/shorts/6l3Nt0T2Kow)); Cinema Studio re-camera pe video existent ([fw5WXmArO1I](https://www.youtube.com/shorts/fw5WXmArO1I)).
- 2026-07: Seedance 2.0 în 4K; GPT Image 2.0 ca editor de sheet-uri ([CHHH8tNioSc](https://www.youtube.com/watch?v=CHHH8tNioSc), [0HIRIT7px9Y](https://www.youtube.com/watch?v=0HIRIT7px9Y)).
- 2026-06: marketplace Higgsfield pentru jocuri/aplicații, găzduire automată (3 jocuri = 68 $) ([XzEgfmesG8c](https://www.youtube.com/watch?v=XzEgfmesG8c)).
- 2026-05: Supercomputer (agent, Model Orchestrator „15x mai ieftin”, Elements, Soul 2.0/Soul ID, 27+ conectori) ([YX7nE-3rYEQ](https://www.youtube.com/watch?v=YX7nE-3rYEQ)); MCP pentru orice LLM ([RQck4CUKu5g](https://www.youtube.com/shorts/RQck4CUKu5g)); Marketing Studio hook presets + settings ([fmgVm-fxPDM](https://www.youtube.com/watch?v=fmgVm-fxPDM), [spB-F47ZNJM](https://www.youtube.com/shorts/spB-F47ZNJM)).
- 2026-03: Cinema Studio 2.5 (characters cu arhetipuri, locations, scenes, multi-shot auto/manual) ([em66Mvt8QLc](https://www.youtube.com/watch?v=em66Mvt8QLc)).
- 2026-02: Kling 3.0 (multi-shot 6 tăieturi, referință față, start/end frame) ([jQvHqKrGhy8](https://www.youtube.com/watch?v=jQvHqKrGhy8)).
