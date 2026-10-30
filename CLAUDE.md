# LIMITLESS — instrucțiuni pentru Claude Code

Proprietar: Szasz. Vorbește cu el în română, simplu, fără jargon. Textul de marketing (replici, text pe ecran, caption-uri) e în engleză.

Citește în ordinea asta:
1. `docs/00-viziune.md` — ținta și cifrele.
2. `docs/01-pipeline.md` — fiecare pas și modulul care îl face.
3. `docs/02-reguli.md` — regulile absolute (cea mai recentă câștigă).
4. `playbooks/` — metodele dovedite, cu sursa.
5. `docs/04-produs-universal.md` — cum se detectează produsul și se alege strategia.
6. `docs/05-motorul-autonom.md` — cum lucrează aplicația singură, agenții, scara de cost, stilul.
7. `docs/08-competitori-on-the-rise.md` — pe cine urmărim (≥100k/zi = dovedit) și variațiile de produs.
8. `docs/09-reguli-produs.md` — ce produs merită încercat, test order, scor, când facem variații.
9. `docs/10-site-shopify.md` — site-ul automat pe Shopify (plăți prin alt procesator).
10. `products/<produs>.md` — profilul produsului pe care lucrăm.

Distribuție și cifre: `distribution/` (portalul de postare) și `social_tracker/` (tracker-ul). Instalare și rețete zilnice: `SETUP-DISTRIBUTIE.md`; fiecare are propriul `CLAUDE.md`. Orice push pe `main` ajunge pe server în ~2 minute (după instalare).

Unelte de producție (regula 24 oct, înlocuiește 10 oct): video DOAR **Kling 4.0 (`kling4_0`) la 1080p** (30 oct: și hook-urile + vocea DOAR Kling, Seedance deloc) — `video-edit` pe clipurile noastre de mișcare, `image-to-video` din start frame; imagini DOAR GPT Image 2.5 (`gpt_image_2_5`, regula 28 oct). Seedance și Genjutsu nu se mai folosesc.

Platforma (sursa de adevăr) e Artifactul publicat din `dashboard/index.html` (linkul e în istoricul sesiunii / lista de artifacte). UI MEREU în engleză (regula din 10 oct), creier 3D. Datele stau în baza de date a artifactului (ArtifactData):
- `products`, `virals`, `finder` (103 produse din product finder-ul arhivei), `inbox` (cererile lui Szasz; la „cereri” le rezolvi și scrii `raspuns` + `status`).
- `config/main` (buget, cost_video_est, prices_en, rules_en, demo), `config/agents` (stare + ultima_en), `config/strategy` (raportul Strategului, în engleză).
La `start`/`panou`: citește inbox-ul și actualizează config/agents. O regulă nouă intră și în `rules_en`. Republică pagina doar când se schimbă codul.
`engine/limitless.py` + `state/` rămân pentru calcule offline; `engine/costs.py` pentru costuri.

Comenzi noi (13 oct):
- `produs nou` / `concept nou de produs` → skill `product-sheet` (referințe generate cu Higgsfield, Szasz aprobă; variațiile ca la HeatGrump, doar la concept nou).
- Primul video la orice produs → skill `pilot-video` (obligatoriu).
- `rezultate` → skill `results` (Apify pe conturile noastre → `posts` → ce hook-uri merg la noi).
- Ceva a picat / Szasz corectează → skill `log-lesson` (Mistakes log). Citește `lessons` înainte de orice producție.

Reguli de lucru:
- LUMINA, regulă pe viață (23 oct): MEREU foarte moale și foarte naturală la orice imagine/video — blocul `prompts/blocks/light-soft-natural.txt` în fiecare prompt.
- Orice regulă nouă de la Szasz (`regula: ...`) → linie datată în `docs/02-reguli.md`.
- Orice afirmație de tip „merge” trebuie legată de o cifră (retenție, views, CTR, comenzi). Fără cifră e ipoteză și se marchează ca atare.
- Nu inventa date despre competitori: în `playbooks/` intră doar ce e observat (link, captură, cifră) sau spus explicit de Szasz.
- După fiecare lot: commit + push, ca Szasz să-și ia fișierele din GitHub.
- Ghidul creatorilor (regula 27 oct, Szasz): după ORICE schimbare în creator-kit, actualizează `creator-kit/HOW-IT-WORKS.html` (explicat în detaliu, pentru cineva care nu știe nimic: toate posibilitățile, hook-uri, audio, Pinterest, verificări, limite), regenerează PDF-ul, republică artifactul (https://claude.ai/artifact/XaMT7HjPTjwkP81XEcyUZG) și refă zip-ul + bucățile.
- Rețete fixe (29 oct, Szasz: „ce a ieșit bine trebe să iasă bine mereu”): când un hook sau B-roll iese bine, promptul EXACT + referințele + setările se salvează în `recipes/` (cu corecturile învățate) și de atunci se folosește cuvânt cu cuvânt. Înainte de orice generare, caută întâi în `recipes/`.
- Calitatea camerelor și personajelor (29 oct, Szasz): MEREU 4K când se poate, minim Full HD, clare, reale, din orice sursă. Le verific singur înainte (`creator-kit/engine/tools.py photo-ok` + ochii mei: AI/neclar/înscenat = afară), nu aștept să-mi spună Szasz.
- Cadre noi (29 oct, Szasz): în fiecare prompt de cadru nou (start frame, image-to-video, Seedance) — cald, Full HD, iPhone 16, realist: blocul `prompts/blocks/new-shot-warm-iphone16.txt`.
- B-roll Grinch (29 oct, Szasz): MEREU rețeta setului 8 din `recipes/grinch-broll-classic-cozy.md`, cuvânt cu cuvânt (se schimbă doar ținuta și rug/floor).
- PAS OBLIGATORIU la orice hook copiat (29 oct, Szasz: „ți-am zis că e regulă și nu o folosești”): ÎNAINTE de orice generare rulez analiza Higgsfield (`video_analysis_create` pe hook-ul original) + transcrierea locală, și salvez rezultatul în `products/<lot>/ref/analysis-<id>.json` (cine vorbește, cuvintele exacte, secundele). Fără fișierul ăsta NU pornesc nicio generare. Cuvintele din prompt se iau din analiză, nu din ghicit.
