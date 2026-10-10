# LIMITLESS — instrucțiuni pentru Claude Code

Proprietar: Szasz. Vorbește cu el în română, simplu, fără jargon. Textul de marketing (replici, text pe ecran, caption-uri) e în engleză.

Citește în ordinea asta:
1. `docs/00-viziune.md` — ținta și cifrele.
2. `docs/01-pipeline.md` — fiecare pas și modulul care îl face.
3. `docs/02-reguli.md` — regulile absolute (cea mai recentă câștigă).
4. `playbooks/` — metodele dovedite, cu sursa.
5. `docs/04-produs-universal.md` — cum se detectează produsul și se alege strategia.
6. `docs/05-motorul-autonom.md` — cum lucrează aplicația singură, agenții, scara de cost, stilul.
7. `products/<produs>.md` — profilul produsului pe care lucrăm.

Distribuție și cifre: `distribution/` (portalul de postare) și `social_tracker/` (tracker-ul). Instalare și rețete zilnice: `SETUP-DISTRIBUTIE.md`; fiecare are propriul `CLAUDE.md`. Orice push pe `main` ajunge pe server în ~2 minute (după instalare).

Unelte de producție: EXCLUSIV Genjutsu, Seedance 2.5, GPT Image 2.5 (regula din 10 oct).

Reguli de lucru:
- Orice regulă nouă de la Szasz (`regula: ...`) → linie datată în `docs/02-reguli.md`.
- Orice afirmație de tip „merge” trebuie legată de o cifră (retenție, views, CTR, comenzi). Fără cifră e ipoteză și se marchează ca atare.
- Nu inventa date despre competitori: în `playbooks/` intră doar ce e observat (link, captură, cifră) sau spus explicit de Szasz.
- După fiecare lot: commit + push, ca Szasz să-și ia fișierele din GitHub.
