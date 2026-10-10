# Sistemele unei operațiuni reale de organic dropshipping (x_systems)

Sursa: `library/sources/od-full/x_systems/` (copia unui drive de lucru, „ORGANIC DROPSHIPPING”) · Data analizei: 10 oct 2026 · Datele din sursă: 21 sept – 7 oct 2026.
Rezultate vizibile în sursă: 4 magazine/produse în producție (2 proiectoare de Crăciun, perdea LED, sutien corector de postură), 4 table video cu 83 de videouri și ~527 de cadre (cifre din `video_boards/README.md`, la 30 sept / 5 oct), un magazin cu „sute de comenzi” (`customer_support/kit/README.md`) și ~330–350 de comenzi plătite care așteptau un furnizor (`fulfillment/aliexpress_top3_2026-09-24.md`, `dsers_search_2026-09-25.md`).

Ce **nu** e în sursă (lipsesc intenționat sau n-au fost copiate): datele brute ale product finder-ului (`raw/research/*`, `keys.txt`), skill-ul `product-finder-import` la care trimite `product_finder.py`, folderul `_tool/` (verificări de nume, miniaturi, `check_board.py`), fișierele de produs (`<PRODUCT>/content/...`), `stores.md`, `status.md`, `tracker.xlsx`. Nu există `product_finder/README.md`: modul de lucru se deduce din `video_boards/tools/product_finder.py` și din `product_finder/board_data.json`.

Regulă de citire: tot ce urmează e observat în fișiere. Unde scrie „ipoteză” e concluzia noastră, nu a sursei. Cheile, emailurile și datele de clienți sunt [omis].

---

## 1. Product finder (cercetarea de produse prin conturi concurente)

Fișiere: `product_finder/links.txt`, `product_finder/board_data.json`, `product_finder/product_board.html`, `product_finder/board_notes.txt` (gol), `video_boards/tools/product_finder.py`, `video_boards/template/product_finder.html` + `product_finder_favicon.txt`.

### Ce face
Ține o bibliotecă de **conturi organice care vând un produs** (IG / TikTok / FB), le grupează pe un arbore **categorie → produs → variație → conturi**, arată pentru fiecare cont videoul cel mai bun din „rularea curentă” a produsului și clasează conturile după performanță. Este o tablă de inspirație și de comparație, nu un selector automat de produse.

### Cum funcționează
**Intrări**
- Linkuri trimise de om, pe loturi datate (`links.txt`: 8 loturi, 29 sept – 7 oct, 282 de conturi). Sursa declarată a loturilor: „private WhatsApp product-hunting group” (`board_data.json → audit.latestImport.source`) și, o dată, conturile de concurenți ținute deschise în Chrome pentru sutienul de postură (`audit.importHistory`, 5 oct).
- Apify pentru profile, reel-uri și istoricul videourilor (dovezi `raw/research/<label>_items.json`; 23.395 de înregistrări video în auditul din 29 sept).

**Pași (comenzile din `product_finder.py`)**
1. `triage FILE` — clasifică fiecare link lipit: `present` (deja pe tablă), `removed <data>` (scos de om, nu se mai readuce), `new`, `needs_resolution` (reel fără proprietar cunoscut, linkuri scurte TikTok), `other`. Parserul `parse_url()` normalizează IG / TikTok / FB (inclusiv `profile.php?id=`), iar `resolved_reels()` rezolvă un reel la contul care l-a postat din istoricul rulărilor Apify.
2. `apify-run ACTOR INPUT.json LABEL [--max-usd 1.0]` — pornește un actor Apify cu **plafon de cost per rulare** (`maxTotalChargeUsd`), pe cheia cu cei mai puțini bani rămași care încă acoperă plafonul („best fit”), cu trecere la cheia următoare la eroare; `apify-balance` arată soldul tuturor cheilor. Etichetele de rulare nu se refolosesc niciodată, iar fiecare rulare își păstrează `_run.json` / `_status.json` / `_items.json` ca dovadă.
3. Etichetare manuală (om + Claude): produsul curent al contului „după filmare și cronologie, nu după numele contului sau linkuri vechi” (`latestProductPolicy`), granița rulării curente (`latestRun.boundaryStatus`), video principal = cel mai văzut din rularea curentă. Pe 5 oct, 209 conturi au fost re-etichetate cadru cu cadru (9 cadre / video) și s-a renunțat la împărțirea „UGC / alte produse” (`audit.latestRelabel`).
4. `rank` — recalculează câmpurile derivate: scor = media a două percentile midrank (urmăritori totali + media vizualizărilor ultimelor ≤ 20 de videouri din rularea curentă), `100*(L+(E-1)/2)/(N-1)`, cu fracții exacte; lista celor mai slabe 50 de conturi; numărătorile.
5. `links` / `build` / `all` — rescrie `links.txt` din loturi și reconstruiește `product_board.html` (șablon + date încorporate). `check` validează tot: chei duplicate, conturi scoase care au revenit, numerotarea loturilor, consistența arborelui, eșantionul de clasare (1–20 de videouri, toate din rularea curentă), media existentă pe disc, pagina construită din datele curente.

**Ieșiri**: `product_board.html` — pânză infinită cu căutare, filtru pe lot, video local redabil per cont, note sincronizate cu `board_notes.txt`, temă dark.

**Unelte / API**: Python standard library, Apify REST (`/acts/{actor}/runs`, `/actor-runs/{id}`, `/datasets/{id}/items`, `/users/me/limits`), mai multe chei Apify citite dintr-un fișier local (la noi: [omis]). Actorii folosiți nu sunt numiți în cod (vin ca argument).

**Programare**: nu există. Importurile sunt manuale, la fiecare lot nou (aproape zilnic între 29 sept și 7 oct).

### Automat vs uman
| Automat (script) | Uman / Claude în sesiune |
|---|---|
| triere linkuri, rezolvarea reel-urilor la cont, rulare Apify cu plafon și rotire chei, clasare, validare, construirea paginii | adunarea linkurilor (grup WhatsApp, Chrome), alegerea actorilor, etichetarea produsului și a variației, granița rulării, ștergerile („Removals… never restored”), decizia ce produs se lucrează |

### Cifre și praguri (din `board_data.json`, 7 oct)
- 282 de conturi (262 IG, 14 FB, 6 TikTok), 103 produse, 8 categorii; 258 eligibile la clasare, 24 excluse („Mixed or ambiguous recent products”, „Incomplete follower or recent-video evidence”).
- Mediana conturilor eligibile: ~10,3k urmăritori, ~69,6k vizualizări medii / video; 107 conturi au media ≥ 100k, 19 au media ≥ 1M.
- Eșantion de clasare: maxim 20 de videouri, doar din rularea curentă; `smallSample` sub 20.
- Cele mai multe conturi pe produs: halate încălzite cu glugă 18, calendare advent 14, proiectoare de scenă 14, măști de schi novelty 9, hanorace-cangur pentru animale 9, mini-proiectoare video 9, echipament sportiv luminos 9, sutiene de postură 9.
- Cele mai mari medii pe produs (≥ 3 conturi): folie auto smart ~1,67M, măști de schi novelty ~873k, costume gonflabile ~726k, onesie-uri cu personaje ~655k, haine novelty ~611k, accesorii de somn pentru călătorie ~526k.
- Relevant pentru HeatGrump (halate încălzite): `ig:princesscomfortt` ~1,38M medie (video principal 21,1M), `ig:kushkozy_` ~298k, `ig:_budcozy` ~277k, `ig:cozy.snoop` ~135k, `ig:thecozykitty.us` ~33k. Toate variațiile sunt teme pe același halat (prințese, Snoopy, Hello Kitty, Harry Potter, cluburi de fotbal…) — confirmare directă a regulii „temele sunt variații ale aceluiași produs”.
- Nu există un prag „produs bun / produs slab”: clasarea e **relativă** și scopul declarat e să arate cei mai slabi 50 (`WORST_N = 50`).

### Puncte forte
- Disciplina dovezilor: fiecare cifră are fișier sursă și dată; ștergerile sunt definitive și verificate la fiecare `check`.
- „Rularea curentă” a produsului: performanța se măsoară doar pe videourile produsului de acum, nu pe tot istoricul contului — elimină conturile mari care au vândut altceva.
- Arborele produs → variație: numărul de conturi pe produs/variație e exact „câți concurenți organici” (criteriul 2 din `docs/09`).
- Cost Apify controlat per rulare și distribuit pe chei.
- Script determinist, fără dependențe, scriere verificată (`write_verified`), protecție la două sesiuni care scriu simultan (md5 citit vs scris).

### Puncte slabe
- **Nicio măsură de viteză**: nu există vizualizări în 24 h sau creștere între treceri; media pe 20 de videouri e o fotografie, nu un semnal „on the rise”.
- Intrarea depinde de oameni (grupul WhatsApp); nu descoperă singur conturi noi.
- Fără bani: nu știe prețul produsului, $/1M, reclamele plătite sau furnizorul.
- Etichetarea produsului e manuală și scumpă (re-etichetarea din 5 oct = 209 conturi revăzute cadru cu cadru).
- Pagina e de 1,4 MB cu toate datele încorporate; funcționează local (file://), nu ca serviciu.

### Cum îl integrăm în LIMITLESS → `engine/hunter` + `engine/product-scout`
**Ce reutilizăm direct ca cod** (stdlib, se copiază și se adaptează căile):
- `parse_url()` și `triage()` → `engine/hunter/links.py`: orice link trimis de Szasz („ia contul ăsta”, un reel) intră prin triere; rezolvarea reel → cont din istoricul Apify.
- Rularea Apify cu plafon `maxTotalChargeUsd`, rotirea cheilor „best fit”, salvarea `_run/_status/_items` cu etichete unice → `engine/hunter/apify.py`; cheile din variabilele mediului (ex. `APIFY_TOKENS`, listă), nu din fișier. Legăm plafonul de `config/budget.json`.
- `ranking()` (percentile midrank) → rămâne ca scor secundar „mărimea contului” în `engine/product-scout`.
- Modelul de date `accounts / products / variations / batches / removals` și regulile din `check()` → schema pentru `library/competitori/<nisa>.json` (`docs/08`) și pentru `state/products.json`.
- Datele în sine: cele 282 de conturi publice (`links.txt`) + eticheta produs/variație → lista de start a Vânătorului, pe nișe; cele 18 conturi de halate încălzite → lista de concurenți HeatGrump.

**Ce rescriem**
- Semnalul principal devine **viteza** (`docs/08`): Vânătorul trece pe la conturi de 2 ori pe zi și salvează vizualizările pe video cu ora; „dovedit” = ≥ 100k în ~24 h. Folosim colectorul din `social_tracker/` (deja face citiri orare prin Apify) în loc să scriem altul.
- Clasarea relativă devine scorul absolut din `docs/09` §3 ($/1M 40 %, viteză 20 %, puțini concurenți 15 %, marjă 15 %, ușurința producției 10 %). Numărul de concurenți = conturile active din aceeași variație/produs din arbore.
- Etichetarea produsului: o facem cu Analistul (cadre + bio + link magazin), cu revizie a lui Szasz doar la produsele noi, nu la fiecare cont.

**Ce lipsește și construim**
- Meta Ad Library (`docs/07`) — sursa din care product finder-ul nu citește deloc.
- Prețul de vânzare (din linkul din bio / magazin), test order și $/1M (`docs/09` §2).
- Descoperirea automată de conturi noi (hashtag-uri, sunete, „conturi similare”), ca intrarea să nu mai depindă de un grup de chat.
- Panou servit (nu fișier local) în `dashboard/`.

---

## 2. Hooks (biblioteca de hook-uri dovedite + textul de pe ecran)

Fișiere: `hooks/hooks_board.html` (tabla, 14 hook-uri cu toate prompturile), `hooks/text_on_screen.txt` (caption-urile care au mers).

### Ce face
O bibliotecă de **hook-uri (cadrul C01, primele 4–5 s)** care au mers pe produsele operațiunii, fiecare cu tot ce trebuie ca să fie refăcut pe alt produs la prima încercare: prompt de imagine și prompt de clip **verbatim**, model și setări, ID-uri de job, referințele în ordinea atașării și rolul fiecăreia, lista „ce schimbi pentru un produs nou”, lecții și un tabel „Reuses” (fiecare refolosire: dată, produs, ce s-a schimbat, rezultat, lecție).

### Cum funcționează
**Intrări**: hook-uri care au trecut la postare pe produsele proprii (BRANDA / BRANDB în tablă = cele două proiectoare), uneori refăcute după un reel de la alt cont.
**Pași**: „Do hook 08 for video 5 of PRODUCT X” e toată instrucțiunea. Se copiază promptul, se schimbă **doar substantivele** care diferă fizic (produsul, cutia, camera, persoana) după lista „Swap for a new product”; mișcarea, camera, ritmul, încadrarea și listele de interdicții rămân identice la byte. O generare, apoi review uman; după port se adaugă un rând în „Reuses”.
**Ieșiri**: clipul hook (720p–1080p, upscale 2K pentru hook-uri cu preset AIGC), caption ars în CapCut.
**Unelte**: Higgsfield — `gpt_image_2` / `gpt_image_2_5` (2k, medium, 9:16) pentru cadrul de start, `seedance_2_5` (720p–1080p, 4–5 s, 9:16, audio on, `mode: omni_reference` trimis explicit, cadrul de start ca rol `start_image` în `medias`), `nano_banana_2` apare la un hook; `declined_preset_id 24bae836-…` trimis preventiv.
**Programare**: niciuna; tabla e editată de mână (are propriul bloc dark generat de `video_boards/tools/make_dark_css.py --page`).

### Conținutul (4 concepte, 14 hook-uri, 29 de prompturi verbatim)
| Concept | Hook-uri | Mecanica | Durată |
|---|---|---|---|
| 1. Descoperire în magazin | 01–07 | cineva găsește produsul pe raft / palet / endcap: plimbare cu căruciorul + whip pan, familie, coș, reacție cu băutura scăpată, „stampede” la palet, plimbare calmă cu cafea, POV doar vârfurile degetelor | 4–5 s |
| 2. Dezvăluire 3-2-1 | 08–09 | „Three... two... one!”, trei flexări de genunchi, cearșaf / pătură trasă de pe produs (magazin / dormitor) | 5 s |
| 3. Cadou POV | 10 | cadoul cade în poala ta, camera = cel care primește | 4 s |
| 4. Pattern interrupt | 11–14 | decorarea merge prost: scara cade, mezanin, steaua din vârful bradului, bradul ia foc la priză („Oh, shoot”) | 4–5 s |

Hook-ul 14 (bradul ia foc) a fost portat de 3 ori (v12, v17, v22) cu cadru + clip trecute **la prima încercare**, schimbând doar camera, bradul, mama, copiii și o clauză de culoare; master-ul (`v9_c01_g8.png`) e mereu `@Image 1`. Caption: „Christmas Decor in 19X5🤮 / Vs.. / Christmas Decor in 2026🎄🎁”.

Text pe ecran (`hooks/text_on_screen.txt`, 8 replici): „Do NOT let a Christmas mom see this 🎄🎁”, „Every Christmas mom NEEDS this 🎄🎁”, „Christmas Parents...don't walk RUN to Costco...🎅🎄”, „Christmas Parents🎅❄️ X IKEA”, variantele „Christmas lover”, „Christmas Decor in 1965🤮 - Vs.. - Christmas Decor in 2026 🎄🎁”.

### Lecțiile tehnice (direct aplicabile la noi)
- **Bătăile au nevoie de intervale de timp** („0.0–1.5s — …”). Un beat care lipsește e o problemă de durată, nu de formulare: 3-2-1 ieșea cu două flexări la 4 s și cu trei la 5 s, prima încercare.
- **O referință video își importă sunetul** și uneori conținutul: se atașează o copie fără sunet și se spune în prompt că e mută; blocul AUDIO stă primul (seedance cântărește mai mult începutul promptului). Referințele video trebuie să aibă ≥ 2 s (aceeași capcană ca la noi, `CLAUDE.md` HeatGrump).
- **„No cuts” în proză nu oprește o tăietură**; o oprește mișcarea corpului care trece peste granița dintre bătăi + o clauză HARD RULES.
- **Numără explicit**: „mulțimea se repede” a dat 2–3 oameni; număr + direcție pentru fiecare persoană a dat „stampede”-ul.
- **Camera ESTE telefonul**: „held iPhone” desenează un telefon în cadru; se interzic separat telefon, ecran, mână, degete, braț, mânecă. La POV se interzic pe rând încheietura, antebrațul, palma, mâna întreagă, brațul.
- **O mișcare de cameră are nevoie de oră de oprire** (camera a fugit pe tot holul până s-a scris „terminat pe la 1,6 s” + „STANDING STILL”).
- **O clauză schimbată pe re-roll**; rescrierea întregului prompt pierde ce era bun.
- Ce trebuie să se miște trebuie să existe deja în cadrul de start; promptul de imagine deține geometria, cel de clip doar mișcarea.
- Ordinea referințelor contează: prima deține geometria, a doua aspectul.
- Hook-ul cu coșul (03) e „cel mai portabil”: se testează primul pe un produs nou — dacă pică, problema e grafica cutiei.

### Automat vs uman
Uman: alegerea hook-ului, review-ul, caption-ul și montajul în CapCut, completarea „Reuses”. Claude: copierea prompturilor, schimbarea substantivelor, generarea. Nimic nu rulează singur.

### Cifre
Pe tablă nu există vizualizări per hook — succesul e notat ca „approved · posted” și „first take”. 3 goluri de arhivă marcate (hook-urile 03 și 10 fără prompt de imagine; 11 fără prompt propriu), nereconstruite intenționat.

### Puncte forte
- Rețete complete și reproductibile; separarea „ce se schimbă” / „ce e portant” e cea mai valoroasă idee din toată sursa.
- Tabelul „Reuses” transformă fiecare port într-o dovadă.
- Hook-urile sunt mecanici independente de produs (03, 04, 08–09 „mută mecanica, păstrează formularea, camera e doar un substantiv”).

### Puncte slabe
- Fără cifre de performanță legate de hook (nu știm care a adus vânzări).
- Tot conținutul e de Crăciun / proiector, multe concepte sunt „magazin” — nu toate se potrivesc unui produs purtabil (halat).
- Tabla e un HTML scris de mână (285 KB), nu date structurate.
- Folosesc `gpt_image_2` și `nano_banana_2`; la noi uneltele sunt exclusiv Genjutsu, Seedance 2.5, GPT Image 2.5 (regula din 10 oct) — prompturile de imagine trebuie retestate pe GPT Image 2.5.

### Cum îl integrăm în LIMITLESS → `engine/hooks`
**Reutilizăm direct**
- Cele 14 rețete, ca date: `library/hooks/od-<NN>.json` cu câmpurile tablei — `id` stabil (nu se refolosește), `concept`, `durata`, `referinte[]` (ordine + rol), `prompt_imagine`, `prompt_clip` (verbatim), `setari`, `swap` (ce se schimbă) vs `portant` (ce nu se atinge), `lectii`, `reutilizari[]`. Extragem prompturile întregi din `hooks_board.html` cu un script (pe tablă sunt complete, cu buton Copy).
- Cele 8 caption-uri → `library/text-pe-ecran.json`, adaptate pe public (ex. „Every Christmas mom NEEDS this” → varianta pentru halat), marcate „dovedit la sursă, neverificat la noi”.
- Lecțiile tehnice → reguli în Cartea de stil (`library/stil.json`) și în QA: intervale de timp obligatorii, referință video mută ≥ 2 s, „camera e telefonul”, interdicții pe părți ale brațului la POV, oră de oprire pentru mișcarea camerei, o clauză per re-roll, `omni_reference` explicit + `start_image` în `medias`.

**Ce rescriem**
- Tabelul „Reuses” devine automat: fiecare port scrie rândul singur (`engine/hooks`), iar `social_tracker/` adaugă cifrele la 24 h / 7 zile → scorul hook-ului și promovarea „scor > mediană → dovedit” (pipeline pas 13).
- Rotația: un hook nu revine pe același cont / produs mai des decât regula (la HeatGrump: o dată la 3 zile).
- Portarea pe uneltele noastre: întâi Genjutsu `hf_mult_motion_control` cu viralul ca mișcare (formatul principal din 10 oct), rețetele imagine → seedance de aici sunt treapta 4 din scara de cost.

**Ce lipsește**
- Legătura hook ↔ cifre ↔ vânzări (nu există la sursă).
- Hook-uri pentru produse purtabile / UGC (recenzie, demonstrație, reacție) — vin din Vânător, nu din această bibliotecă.

---

## 3. Video boards (tabla de producție per produs)

Fișiere: `video_boards/README.md`, `SYSTEM.md`, `WORKFLOWS.md`, `template/` (`page.html`, `board.css`, `board.js`, `example_board_data.json`, `example_board.html`, `product_finder.html`, favicon-uri), `tools/` (`build_board.py`, `add_card.py`, `decide.py`, `new_board.py`, `extract_board.py`, `match_media.py`, `make_dark_css.py`, `product_finder.py`).

### Ce face
O tablă per produs cu **o bandă per video și un card per cadru (shot)**. Are două roluri (`README.md`): pentru Claude, păstrează fiecare prompt care a mers exact cum a fost trimis la Higgsfield, ca orice cadru să poată fi refăcut la prima încercare; pentru om, review rapid (Approve / Reject), note și toate videourile produsului într-un loc.

### Cum funcționează
**Sursa de adevăr**: `<PRODUCT>/content/_board_thumbs/board_data.json` (schema `video-board/1`, documentată câmp cu câmp în `SYSTEM.md` §2). Pagina `video_board.html` e generată de `build_board.py` și nu se editează niciodată de mână.

**Modelul de date**: `lanes` (video N: titlu = hook, caption, export final, meta Status → Hook → Song → Runtime → Resolution, sursa = reel-ul concurentului copiat cu cont / vizualizări / durată) → `groups` (Hook, B-roll 1, B-roll 2) → `cards` (shot `cNN`, `stage` frame / clip / refs, `status` review / approved / rejected, cadre, `driver` = video de mișcare, `looks` = persoana nouă + camera nouă, `take` = clipul, `det` = sertarul de prompturi: referințe în ordinea trimiterii, prompt verbatim, setări, alte take-uri cu motivul respingerii, note, trimitere în `prompts.md`).

**Fluxul (`WORKFLOWS.md`)**
1. Produs nou: `new_board.py`; panouri cu specul cutiei și regulile învățate.
2. Plan video: C01 hook, C02–C04 B-roll 1, C05–C07 B-roll 2; un cadru repetat se ia verbatim din `prompts.md § Verified record`.
3. Runda 1 — cadre: o generare per shot, descărcare `vN_cNN_gK.png` (nimic nu se suprascrie, re-roll = take-ul următor), salvarea JSON-ului jobului Higgsfield, `add_card.py --frame … --media <id>=<fișier>` → card „FRAME FOR REVIEW”.
4. Omul apasă Approve / Reject, apoi **Copy decisions** și lipește liniile `APPROVE vN_cNN_gK.png` / `REJECT … — motiv` în chat; `decide.py` le aplică. La reject: re-roll care schimbă doar ce spune motivul, `--replaced "motiv"`.
5. Runda 2 — clipuri: doar când **toate** cadrele videoului sunt aprobate; animare pe cadrul aprobat cu promptul dovedit al slotului; `add_card.py --clip` refuză un clip dacă fișierele cadrului nu sunt exact cele aprobate.
6. Motion transfer (Genjutsu `hf_mult_motion_control`): fără cadru, o singură aprobare (clipul); în **layout-ul pe coloane** (`SYSTEM.md` §2.6, din 5 oct): rândul 1 viralul de referință, rândul 2 persoana nouă + camera nouă (aprobate înainte de generare, stadiul `refs`), rândul 3 clipul nostru sau exportul final, cu „Side by side” (referința mută lângă clipul nostru, sincronizate), rândul 4 prompturile.
7. Export: `videos_to_post/video_N.mp4`, meta prin `ffprobe`, `## Verified record` în `prompts.md`, rebuild + 4 verificări (`_tool/`, nu sunt în sursă).
8. Audit (`match_media.py`): leagă fișierele de joburile Higgsfield din istoricul `show_generations` — clip = md5 identic, imagine = aceeași mărime în bytes, atașament = bytes identici sau imagine 40×72 gri cu diferență ≤ 0,10; unde Higgsfield și tabla nu se potrivesc, câștigă Higgsfield.

**Unelte / API**: Python stdlib (Pillow + numpy doar pentru `match_media.py --media`), JSON-urile de job Higgsfield (`show_generation_by_ids` / `job_display`: `id`, `model`, `params.prompt`, `params.medias[].role`, `results`), ffprobe. Pagina: pânză cu pan / zoom, facade video (max. un `<video>` viu), lazy load, note în browser + sincronizare cu `board_notes.txt` prin File System Access API, decizii în `localStorage`, dark/light.

**Programare**: niciuna — totul la cererea omului, în sesiuni Claude.

### Automat vs uman
| Automat (scripturi) | Uman |
|---|---|
| validarea datelor, construirea paginii, cardul din jobul Higgsfield (prompt byte cu byte, setări, referințe), aplicarea deciziilor, salvarea take-urilor respinse, salvarea datelor din HTML, auditul fișier ↔ job, tema dark | aprobarea fiecărui cadru și a fiecărui clip (2 aprobări / video), motivul respingerii, montajul, „postat” |

### Garanții (`SYSTEM.md` §6)
Build-ul refuză să scrie dacă: schema / numele produsului greșite, câmp necunoscut, shot repetat, prompt gol, un fișier generat `gK` fără bloc de prompt (sau fără nota explicită „No prompt on record”), fișier lipsă nelistat în `lost_takes.txt`. Scrie printr-un fișier `.building` creat exclusiv (două sesiuni nu pot scrie aceeași tablă) și citește înapoi ce a scris (drive-ul trunchia scrieri). `add_card.py` și `decide.py` refuză să salveze dacă datele s-au schimbat de la citire.

### Cifre
4 table: Swanlift (coloane) 10 videouri / 12 rulări; TheXmasGlow 30 / 210 carduri; MerryGlow perdea LED 35 / 265; MerryGlow proiector 8 / 40 (30 sept / 5 oct). Constante de design fixe (card 372 px, culori pe grup). Setări văzute pe carduri: `gpt_image_2_5` 2k medium 1520×2688, `seedance_2_5` 720p 4 s, upscale ByteDance 2K 1440×2560.

### Puncte forte
- Trasabilitate completă: orice clip din export → jobul, promptul exact, referințele, take-urile respinse și de ce.
- „Verified record”: refacerea unui cadru reușit = copiere, nu reinventare.
- Layout-ul pe coloane = exact fluxul nostru FULL GENJUTSU (viral → set nou → clip), cu comparație „side by side”.
- Robustețe: build idempotent, salvare din HTML, refuz la date invalide, nimic suprascris.

### Puncte slabe
- Gâtul de sticlă e omul: două runde de aprobare pe fiecare video; deciziile circulă prin copy-paste în chat.
- Pagină statică locală (file://), stare per browser; nu e multi-utilizator.
- Fără cost (credite) pe card, fără verdict QA automat, fără cifre după postare.
- Legată de structura drive-ului (`<PRODUCT>/content/video_N_assets/…`, `_tool/NAMING.md`).

### Cum îl integrăm în LIMITLESS → panoul de producție al platformei
**Reutilizăm direct ca cod**
- `build_board.py` + `template/` (`page.html`, `board.css`, `board.js`) + `add_card.py` + `decide.py` + `new_board.py` + `extract_board.py` → `engine/board/` (stdlib, deja testate pe ~500 de carduri). Adaptăm doar căile: `products/<id>/videos/vN/…` în loc de `<PRODUCT>/content/video_N_assets/…`.
- Schema `video-board/1` + layout-ul pe coloane ca format implicit (viral de referință / personaj + cameră / clip final).
- `add_card.py` primește direct JSON-ul jobului Higgsfield → Producătorul îl apelează după fiecare descărcare (prompt verbatim garantat).
- `match_media.py` pentru auditul creditelor și al fișierelor.
- Convenția de nume `vN_cNN_gK` / `rK` și regula „nimic nu se suprascrie”.

**Ce rescriem**
- Cine aprobă: `status` îl pune **QA automat** (Claude cu vedere, regulile per clip, max 3 încercări — pipeline pas 8); butoanele Approve / Reject rămân pentru Szasz ca verificare prin sondaj și ca sursă de reguli noi (motivul unui reject → `regula:`).
- Stările cardului se leagă de stările din `state/virals.json` (`găsit → … → măsurat`).
- Câmpuri noi pe card: credite consumate, unealta din scară, verdict QA cu motiv, încercări; pe bandă: cifrele din `social_tracker/` la 24 h / 7 zile.
- Servire prin `dashboard/` (sau ca artifact cu bază de date partajată pentru decizii), în loc de fișier local + copy-paste.
- O vedere peste toate produsele (10 linii în paralel, `docs/05`).

**Ce lipsește**
- Coada și bugetul (`engine/queue`, `engine/budget`) care alimentează tabla.
- Verificările din `_tool/` (nume, miniaturi `make_thumbs.py`, `check_board.py`) — le rescriem minimal (miniaturi cu ffmpeg).

---

## 4. Customer support (inbox-ul de suport al magazinului)

Fișiere: `customer_support/kit/README.md`, `SETUP.md`, `REPLYING.md`, `INBOX_PASS.md`, `STORES_TEMPLATE.md`, `customer_support/build_shared_card.py`.

### Ce face
Suport pe email pentru unul sau mai multe magazine Shopify: clienții scriu la `support@<domain>`, proprietarul citește tot într-un singur inbox Gmail, iar o **sarcină programată zilnic** etichetează fiecare email, caută clientul în Shopify și lasă **un singur draft complet per client per subiect**. Nu trimite nimic niciodată.

### Cum funcționează
**Setup (`SETUP.md`, faze 0–7, fiecare cu o verificare)**: 0 date de la proprietar; 1 redirecționare email în Shopify (`support@` → inbox; doar pentru domenii gestionate de Shopify); 2 Gmail „Send mail as” prin `smtp.gmail.com:587` TLS cu App Password (făcută de proprietar), confirmare, „Reply from the same address”, filtru `to:support@<domain>` → etichetă magazin + „Never send to Spam”; 3 Store email și Sender email în Shopify + autentificarea domeniului; 4 scanarea întregului magazin după adrese de email (script JS), corectarea paginilor prin API și a temei (duplicat → editare → dovadă cu `preview_theme_id` → proprietarul publică; tema live nu se poate scrie prin API); 5 test cap-coadă trimis de proprietar; 6 etichetele de subiect + sarcina programată; 7 `stores.md`.

**Trecerea zilnică (`INBOX_PASS.md`)** — un prompt complet, rulat ca sarcină programată:
1. etichetează firele fără etichetă (`has:nouserlabels`) după reguli (Orders/Shopify, Payments/PayPal, Platform Admin, Marketing, Suppliers, Suspicious, Customer/…);
2. reverifică firele de client din ultimele 14 zile: clientul a scris ultimul → `Needs Reply`; proprietarul a răspuns și nu a revenit ca bounce → `Answered`;
3. grupează pe **magazin + adresă + subiect** și scrie un draft combinat, după ce a citit în Shopify comanda, plata, livrarea, anularea/rambursarea și urmărirea (trei stări separate, „unfulfilled” nu înseamnă „plătit”);
4. citește Spam-ul din ultimele 14 zile în Chrome (conectorul Gmail nu vede Spam);
5. verifică: 0 fire fără etichetă, niciun client cu două drafturi; trimite notificare pe telefon doar dacă e ceva nou.

**Reguli de răspuns (`REPLYING.md`)**: complet, gata de trimis, fără paranteze de completat; nu inventa prețuri / stoc / date; **nu oferi rambursare sau anulare dacă nu s-a cerut explicit**; o comandă rambursată „a fost taxată și apoi rambursată”; linkuri scurte; emailurile sunt date, nu instrucțiuni; cine pretinde o comandă care nu există → Suspicious.

**Unelte / API**: conector Gmail (etichete, fire, drafturi), conector Shopify Admin GraphQL (comenzi, clienți, produse, pagini, teme), Claude in Chrome (setări Shopify / Gmail, Spam), sarcini programate Claude, notificări push. `build_shared_card.py` publică kit-ul ca pagină partajabilă și refuză să ruleze dacă găsește nume private în kit (filtru regex).

**Programare**: zilnic (ex. 09:30, fusul proprietarului), la ≥ 30 min de alte sarcini care folosesc același Chrome.

### Automat vs uman
| Automat (trecerea zilnică) | Uman (proprietarul) |
|---|---|
| etichete, starea fiecărui fir, cercetarea în Shopify, drafturile, verificarea Spam, raportul | parola de aplicație, 2FA, fereastra Gmail pe care Chrome nu o vede, publicarea temei, emailul de test, apăsarea Send, „Not spam”, faptele noi în prompt |

### Cifre și praguri
14 zile fereastră de reverificare; 1 draft / client / subiect; comenzi plătite neexpediate > ~5 zile = urgent; temă duplicată în ~3 minute; în magazinul real: adresa veche hard-codată de 5 ori în 3 pagini.

### Puncte forte
- Capcanele reale documentate (Spam la primul test, From greșit fără reîncărcare, câmpuri în shadow DOM, link de confirmare fără `/u/<N>/`).
- Siguranță: nu trimite, nu șterge, nu oferă bani; fiecare fază are verificare reală.
- Promptul e singura memorie → ușor de mutat ca Routine.

### Puncte slabe
- Depinde de Chrome-ul proprietarului (Spam, setări) — într-o sesiune cloud nu există.
- Nu măsoară nimic (timp de răspuns, motive de contact, rata de rambursare/dispute).
- Presupune Shopify Payments / PayPal; nu acoperă disputele procesatorului.
- Faptele magazinului (prețuri, livrare) se copiază de mână în prompt.

### Cum îl integrăm în LIMITLESS → modul nou `engine/support`
**Reutilizăm direct**: promptul din `INBOX_PASS.md` ca Routine zilnică (cu magazinele noastre în blocul Stores), lista de etichete, regulile din `REPLYING.md` (mai ales „one reply per customer per topic” și „never offer a refund”), fazele 1–5 din `SETUP.md` ca listă de setup per magazin, scanarea JS a adreselor, procedura temă duplicat → dovadă → publicare.

**Ce rescriem**
- Blocul **Store facts** se generează automat din `products/<produs>/site.json` (`docs/10`) și din Shopify, nu de mână.
- Starea plății: la noi procesatorul nu e Shopify Payments (`docs/10`) — adăugăm citirea statusului din procesatorul extern și o etichetă `Payments/Dispute`.
- Spam: în cloud, fără Chrome, raportul spune „Spam neverificat” (cum prevede kit-ul) sau rulăm pasul de Spam pe calculatorul lui Szasz.
- Un singur inbox pentru toate cele 10 linii de produs, etichetă per magazin.

**Ce lipsește**
- Metrici în raportul zilnic: emailuri/zi, % „unde e comanda”, rambursări, dispute → intră în criteriul 9 („risc mic de chargeback”) din `docs/09` și pot opri un produs.
- Răspunsurile frecvente → FAQ-ul de pe pagina produsului (`docs/10`, pas 2).

---

## 5. Fulfillment (furnizori și agenți)

Fișiere: `fulfillment/kit/README.md`, `SETUP.md`, `LOGGING.md`, `SUPPLIER_CHECK.md`, `STATUS_TEMPLATE.md`, `CONVERSATION_TEMPLATE.md`; cercetări: `fulfillment/alibaba_top5_2026-09-24.md`, `aliexpress_top3_2026-09-24.md`, `dsers_search_2026-09-25.md`.

### Ce face
Alegerea furnizorului / agentului care livrează comenzile și urmărirea fiecărei conversații fără să se piardă un mesaj, o ofertă sau o promisiune: un jurnal verbatim per furnizor, o tablă de stare (`status.md`), un tracker Excel cu oferte comparabile prin formule și o **verificare zilnică programată** care citește toate canalele și raportează. Nu trimite, nu răspunde, nu plătește.

### Cum funcționează
**Setup (`SETUP.md`, faze 0–7)**
0. Varianta exactă care trebuie livrată, poze reale, țări, dropshipping vs stoc, furnizori deja contactați, **bugetul maxim per comandă livrată (secret)**, termen; numărarea comenzilor **plătite și neexpediate** din Shopify, pe mărimea comenzii (1 / 2 / 3 bucăți) și pe țară.
1. Folderul + `status.md`. 2. `tracker.xlsx` (Suppliers, Quotes cu `=Total/Units`, Backlog, Message Log, Key Facts, To-Do; numere de la furnizor albastru, formule negru, neconfirmat galben).
3. Candidați (agenți / CJ / Zendrop, fabrici Alibaba — de obicei doar en-gros, vânzători AliExpress — puțin stoc) → **poarta pozelor**: candidatul iese dacă pozele lui nu arată exact același obiect și aceeași variantă („spec tables lie”) → folder per furnizor → primul mesaj (draft; proprietarul îl trimite) cu întrebări numerotate: preț la cantitate, transport și zile pentru 1/2/3 bucăți pe țară, DDP, tracking, cum primesc comenzile, QC cu poze, colete pierdute, comision, cât de repede pornesc, ambalaj custom.
4. Jurnal zilnic (`LOGGING.md`): mesaj verbatim cu `## data oră — Expeditor → Destinatar (canal)`, în același pas status + tracker; drafturile marcate „DRAFT, not confirmed sent”. Etape: To contact → First message drafted → Sent, waiting reply → Quoting → Quote received → Negotiating → Chosen / Rejected.
5. Verificarea programată (`SUPPLIER_CHECK.md`): WhatsApp Web, chat-urile platformelor, dashboard-uri, Gmail `newer_than:1d`; adaugă doar ce e nou, raport scurt pe telefon.
6. Comparație pe **cost per comandă livrată** ponderat cu mixul real de comenzi + **zile până la primul colet**; raport datat cu reputație (Trustpilot) și politici de colete pierdute; proprietarul decide. Lista înainte de plată: produsul legat corect în dashboard cu **fiecare variantă** (bundle de 2 la preț de 1 = greșeală reală), totalul = oferta × mixul real, doar comenzi plătite, o singură aplicație care expediază, stoc real („in stock” de la vânzător nu e un număr din depozit), sărbători chinezești (Golden Week, Anul Nou), costuri extra în scris, video cu unitatea reală.
7. După plată: datele promise, urmărirea care se sincronizează în magazin, verificarea continuă până are fiecare comandă tracking.

**Unelte / API**: Claude in Chrome (WhatsApp Web, Alibaba Messenger, DSers, site-uri de furnizori), conector Gmail, conector Shopify, python3 + openpyxl, sarcini programate.

**Programare**: zilnic în orele de lucru, la ≥ 30 min de trecerea de suport.

### Cifre din cercetările reale (proiector de Crăciun, 24–25 sept 2026)
- Alibaba: 7 căutări (~140 de anunțuri) → 13 deschise → 5 furnizori cu aceeași matriță; $1,65–2,95 / buc. (MOQ 10) până la $2,50 @500; excluși pentru livrare la timp ≥ 76 % sau 1–2 ani / puține recenzii. **Niciun anunț nu declară dropshipping pe bucată** — fabricile au refuzat comenzile individuale.
- AliExpress: 6 căutări (~930 de anunțuri) → filtru titlu 264 → ~48 cu aceeași matriță → top 3; criteriul decisiv a fost stocul pe variantă (998 disponibile vs „only 3 left”); furnizorul curent avea doar 10 bucăți.
- DSers: 3 surse (AliExpress, 1688, Alibaba); variantele cu aceeași matriță $4,7–10 + transport SUA $1,99, 6–8 zile; 1688 și Alibaba prin DSers inutilizabile pentru acest produs; nicio versiune premium $10–20 a aceleiași matrițe. Risc notat: niciun anunț nu are destule vânzări ca să dovedească ~330 de bucăți rapid.
- Necesar real: ~330–350 de bucăți pentru comenzile plătite în așteptare.

### Automat vs uman
Automat: citirea canalelor, jurnalul verbatim, actualizarea status / tracker, raportul, cercetarea de listări cu poarta pozelor. Uman: trimiterea mesajelor, negocierea, decizia, plata, legarea produsului în aplicația de fulfillment.

### Puncte forte
- „Verbatim sau nimic” + „numerele vin din cuvintele furnizorului” → comparații corecte.
- Compararea pe comandă livrată și pe zile până la expediere, nu pe preț per bucată.
- Lista de verificare dinainte de plată, din greșeli reale.
- Poarta pozelor (aceeași carcasă cu alt interior / altă priză e alt produs).

### Puncte slabe
- Construit reactiv: furnizorul s-a căutat **după** ce existau sute de comenzi plătite neexpediate.
- Depinde de Chrome + WhatsApp Web; nu automatizează rutarea comenzilor (DSers e doar menționat).
- „Still being improved” (declarat în README).

### Cum îl integrăm în LIMITLESS → modul nou `engine/fulfillment`
**Reutilizăm direct**: șabloanele `STATUS_TEMPLATE.md` și `CONVERSATION_TEMPLATE.md`, formatul de jurnal din `LOGGING.md`, structura foilor din tracker, promptul `SUPPLIER_CHECK.md` ca Routine, lista dinainte de plată, metoda de cercetare (căutări → filtru titlu → poarta pozelor → stoc pe variantă) și formatul rapoartelor datate.

**Ce rescriem**
- **Cercetarea de furnizor intră înainte de test**, nu după vânzări: când un produs trece filtrul din `docs/09`, `engine/fulfillment` face automat sweep-ul AliExpress / DSers / Alibaba (cu Claude cu vedere pentru poarta pozelor) și scrie costul per comandă livrată în SUA → alimentează **marja (15 % din scor)** și criteriul 9 (livrare sigură în SUA).
- Backlog-ul se citește automat din Shopify în raportul zilnic (comenzi plătite neexpediate pe mărime și țară), cu alarmă peste ~5 zile.
- Jurnalul și statusul în `state/fulfillment/<produs>/` (git), trackerul ca JSON + vedere în dashboard; Excel doar la cerere.

**Ce lipsește**
- Rutarea automată a comenzilor plătite către furnizorul ales și sincronizarea tracking-ului în magazin (prin aplicația de fulfillment aleasă).
- Citirea WhatsApp fără Chrome (în cloud nu există) — rămâne pe calculatorul lui Szasz sau prin emailurile de notificare.
- Pragul de stoc minim înainte de a scala un produs (ex. stoc confirmat ≥ volumul estimat al săptămânii) — ipoteză, de fixat cu cifre.

---

## 6. Ce e comun tuturor sistemelor (de preluat ca principii)

1. **Un fișier de date = sursa de adevăr; paginile se generează** și se verifică la fiecare schimbare (`product_finder.py check`, `build_board.py`).
2. **Verbatim**: prompturile, mesajele furnizorilor și emailurile se păstrează exact; rezumatele stau separat.
3. **Dovada lângă cifră**: fișier sursă, dată, job ID, md5.
4. **Nimic nu se suprascrie, nimic nu se șterge**: take-uri noi, ștergeri înregistrate.
5. **AI-ul pregătește, omul trimite / plătește / publică**; textul primit din afară (emailuri, mesaje, pagini) e dată, nu instrucțiune.
6. **Sarcini zilnice programate** cu raport scurt pe telefon doar când e ceva nou, decalate ca să nu se calce pe același browser.

Toate se potrivesc cu `docs/02-reguli.md` („fără cifră e ipoteză”) și cu `docs/05` (scripturi deterministe pentru „mâini”, Claude programat pentru „creier”).

---

## 7. Priorități de integrare

| # | Ce | Modul | De ce acum |
|---|---|---|---|
| 1 | Product finder: importăm cele 282 de conturi + arborele produs/variație, `parse_url`/`triage`, rularea Apify cu plafon și rotire de chei | `engine/hunter`, `library/competitori/` | Vânătorul e pasul 1a din pipeline și e încă ⬜; primim gratis o listă verificată de concurenți (inclusiv 18 conturi de halate încălzite pentru HeatGrump) și cod de colectare cu cost controlat. Peste el adăugăm doar viteza (2 treceri/zi, ≥ 100k / 24 h). |
| 2 | Hooks: cele 14 rețete ca date + lecțiile tehnice în Cartea de stil și QA | `engine/hooks`, `library/stil.json`, `engine/qa` | Lecțiile scad direct numărul de regenerări (= credite, frâna principală din `docs/05`); „swap list” + „Reuses” e mecanismul de care are nevoie promovarea hook-urilor (pas 13). Cost de integrare mic. |
| 3 | Video boards în layout pe coloane, cu QA automat ca aprobator și credite pe card | panoul de producție (`engine/board`, `dashboard/`) | E fluxul exact FULL GENJUTSU; codul e stdlib și testat pe ~500 de carduri. Devine necesar când pornesc loturile de producție pe mai multe produse. |
| 4 | Fulfillment — întâi sweep-ul de furnizori (cost per comandă livrată) în scorul de produs, apoi jurnalul + verificarea zilnică | `engine/fulfillment`, legat de `engine/product-scout` | Marja și livrarea sunt 2 din cele 10 criterii; sursa arată costul de a căuta furnizorul prea târziu (~330 de comenzi plătite în așteptare). Jurnalul și verificarea zilnică intră la prima comandă reală. |
| 5 | Customer support — Routine-ul zilnic din `INBOX_PASS.md` + metrici de dispute | `engine/support` | Necesar din ziua în care magazinul (`docs/10`) primește comenzi; până atunci nu are pe ce rula. Setup-ul cere pași ai lui Szasz (App Password, publicarea temei). |

Ordinea urmează `docs/05` §„Ordinea de construcție”: întâi intrarea (Vânător) și calitatea producției (hooks + QA), apoi panoul, apoi partea de business care pornește doar după primul produs validat.
