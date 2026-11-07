# START — citește doar asta la un chat nou (actualizat 6 nov 2026)

Fișier scurt, ca un chat nou să nu se blocheze citind tot. Nimic nu s-a șters: istoricul complet e în `docs/02-reguli.md` (toate regulile, datate) și în celelalte fișiere. Le deschizi DOAR când lucrul de acum le cere.

## Unde am rămas
- **7 nov — lot Snoopy (HeatPup), 3 videouri după reelul Grinch „Do NOT let a Grinch mom see this”** (metoda creatorilor: hook Kling video-edit + B-roll v4/v5 + conector + telecomandă + cozy): `products/snoopy-lot-nov7/snoopy-nov7-1..3.mp4` (720p mărit local la 1080x1920; 1080p din Higgsfield doar când zice Szasz).
- Ultimul lucru făcut: **proiectul `seedance-method/`** (separat de halate), testul 02 — reel Snoopy x In-N-Out → nișa **Grinch**.
  - FINAL gata, fără sunet: `seedance-method/tests/02-snoopy-to-grinch/out/FINAL-grinch-1080p-silent.mp4` (îmbinare v5/v4 la tăieturi, verificat la 0,1 s → `out/VERIFICARE-FINAL.md`).
  - **Pasul următor:** montajul (muzică, text pe ecran în engleză, caption „Comment “X” for the link”), apoi 2–3 variante postate și măsurate.
  - Metoda și lecțiile: `seedance-method/SKILL.md`; notițele testului: `.../02-snoopy-to-grinch/NOTES.md`.
- Halatele (Grinch / Snoopy-HeatPup / Prințesă) + kitul creatorilor: rețetele înghețate sunt în `recipes/`, metoda în `docs/11-metoda-one-click.md`.

## Regulile active (rezumat; „cea mai nouă câștigă”, detaliile în 02-reguli.md)
**Unelte**
- Halate / creator-kit: video DOAR **Kling 4.0 (`kling4_0`) 1080p** — `video-edit` pe clipul original FĂRĂ sunet; vocea o face tot Kling. Seedance și Genjutsu NU.
- Proiectul `seedance-method/`: Seedance 2.5 PERMIS; dacă dă `ip_detected` (Grinch, Snoopy) → Kling 4.0 `video-edit`.
- Imagini DOAR **Nano Banana Pro** (`nano_banana_pro`, 9:16, 4k) — regula 7 nov (înainte GPT Image 2.6 / 2.5).

**Înainte de orice generare**
1. Caută întâi în `recipes/` — ce a ieșit bine se copiază cuvânt cu cuvânt, se schimbă doar `<...>`. Orice modificare se scrie ÎNTÂI în rețetă, datată.
2. Hook copiat: analiza Higgsfield (`video_analysis_create`) + transcriere locală, salvate în `products/<lot>/ref/analysis-<id>.json`. Fără fișierul ăsta nu se generează nimic. Cuvintele vin din analiză.
3. Studiază originalul cadru cu cadru (0,1 s la tăieturi): încotro privește persoana, ce parte a produsului se vede, cine ține ce, harta obiectelor (produs / ambalaj / decor), logica scenei.
4. Citește `lessons` (Mistakes log) din platformă.

**În fiecare prompt**
- Lumina foarte moale și naturală: `prompts/blocks/light-soft-natural.txt`.
- Cadre noi: `prompts/blocks/new-shot-warm-iphone16.txt` (cald, Full HD, iPhone 16, realist).
- Produsul DOAR din referințe („REPRODUCE IT ONE TO ONE from Images N–M”), nu descris în cuvinte. Poza personajului mereu referință directă. Câte o referință pentru fiecare variantă de produs de pe ecran (nu grilă).
- Personajul în prim-plan; personaje doar cu piele deschisă; camere/personaje reale, ≥ Full HD (`creator-kit/engine/tools.py photo-ok` + ochii).

**După generare**
- Compar rezultatul cu originalul, una lângă alta, cadru cu cadru, ÎNAINTE de folosire sau trimis (și ce fac agenții). Nimic neverificat nu ajunge la Szasz.
- Cadrele bune din variante diferite se pot îmbina exact la tăieturi (ffmpeg), fără credite în plus.

**Montaj halate**
- Ordinea: hook → B-roll (îmbracă → săculeți → cozy) → conector → telecomandă. Textul de pe ecran = al originalului, sus, același tot videoul. Muzică de Crăciun în rotație, încet sub hook, drop la tăietura hook → B-roll.

**Lucru**
- Vorbesc cu Szasz în română, simplu. Text de marketing și UI în engleză.
- „Merge” = cifră. Fără cifră e ipoteză.
- Regulă nouă de la Szasz → linie datată în `docs/02-reguli.md` (și în `rules_en` din platformă).
- După fiecare lot: commit + push.
- Platforma = Artifactul din `dashboard/index.html` (date în ArtifactData). Ghidul creatorilor: actualizat după orice schimbare în creator-kit.

## Cum să nu se mai blocheze chatul
- Nu citi la pornire tot `docs/` + `playbooks/` (~500 KB). Citește acest fișier și apoi doar ce cere sarcina.
- Pozele și videourile mari: le verifici pe foi de cadre mici (scale=216), nu încărcate întregi.
- Un chat = un lot / un test. Când se termină, actualizează secțiunea „Unde am rămas” de mai sus, commit + push, și pornește un chat nou.
