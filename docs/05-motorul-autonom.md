# Motorul autonom LIMITLESS

(10 oct 2026, Szasz) O aplicație care lucrează **singură** și **în paralel**: găsește cele mai virale videouri, le reproduce cu Higgsfield (Genjutsu și restul uneltelor) la **cel mai mic cost**, cu alt personaj și altă cameră, le montează complet, respectă toate regulile ca toate videourile să aibă **același stil**, le trimite la postare și învață din cifre.

**Formatul principal (10 oct): UGC.** Vânătorul caută în primul rând videouri UGC reale care au mers (persoană reală, filmat cu telefonul, recenzie / demonstrație / reacție / unboxing); Planificatorul le reface cadru cu cadru cu Genjutsu motion control, cu personajul, camera și produsul nostru.

## Bucla (rulează continuu)
```
 VÂNĂTOR ─► ANALIST ─► PLANIFICATOR ─► PRODUCĂTOR ─► QA ─► MONTAJ ─► QA final ─► DISTRIBUȚIE ─► TRACKER
    ▲                                                                                              │
    └──────────────────────────────── ÎNVĂȚARE (scor, reguli, prețuri) ◄────────────────────────────┘
```

| Agent | Ce face | Intrare → ieșire |
|---|---|---|
| **Vânător** | caută zilnic videourile outlier (views ≥ 3× media contului) pe IG / TikTok / FB / YT Shorts, în nișa produsului | conturi + cuvinte cheie → `queue/virale` |
| **Analist** | taie viralul pe cadre: hook, acțiune, ritm, text, audio, structură; dă scor de potrivire cu produsul | viral → fișă de cadre |
| **Planificator** | pentru fiecare cadru alege **unealta cea mai ieftină care trece QA** (vezi mai jos), alege setul (personaj + cameră) din rotație, estimează costul | fișă → rețetă de producție + cost |
| **Producător** | trimite generările în paralel, în limita bugetului zilnic de credite | rețetă → clipuri brute |
| **QA** | verifică vizual fiecare clip (produs identic, personaj = referința, fără text / branduri, format 9:16) — max 3 încercări, apoi trece la unealta următoare | clip → acceptat / refă |
| **Montaj** | tăieturi, ritm, text pe ecran, emoji, muzică, durată — după **Cartea de stil** | clipuri → MP4 final + caption |
| **Distribuție** | pune MP4-ul în coada portalului (`distribution/`), pe conturi, fără repetări | MP4 → postat |
| **Tracker + Învățare** | cifrele la 24 h / 7 zile → scor pe hook, pe unealtă, pe set, pe cont; actualizează regulile și prețurile | cifre → reguli noi |

Toți agenții lucrează **în același timp** pe videouri diferite (coadă comună, fiecare video are o stare: `găsit → analizat → planificat → produs → verificat → montat → postat → măsurat`).

## Cel mai mic cost: scara uneltelor
Pentru fiecare cadru, Planificatorul încearcă în ordinea costului și urcă doar când QA pică:
**Baza de unelte (regula din 10 oct): EXCLUSIV Genjutsu, Seedance 2.5 și GPT Image 2.5. La început totul se face FULL GENJUTSU: viralul întreg refăcut cu Genjutsu, bucată cu bucată, cu personajul și camera noastră (de pe Pinterest, 0 credite). Celelalte trepte intră doar când Genjutsu e respins.**
1. **Reutilizare** — clip din bibliotecă deja aprobat (0 credite).
2. **Montaj fără AI** — apropiere lentă / mișcare din imagine statică cu ffmpeg (0 credite).
3. **Genjutsu motion control** (`hf_mult_motion_control`, singurul mod Genjutsu folosit) — mișcarea din viral + personajul + camera noastră.
4. **GPT Image 2.5 → Seedance 2.5** — imagine de start, apoi animație `omni_reference` (când Genjutsu e respins, ex. `ip_detected`, sau când viralul nu are mișcare reutilizabilă).
5. **Seedance 2.5 video_edit** — editarea directă a unui clip existent (de testat costul față de Genjutsu).

Se măsoară **costul pe secundă acceptată** (credite / secunde care trec QA) pe fiecare unealtă și tip de cadru; scara se reordonează singură după cifre. Prețurile exacte se completează din research-ul Higgsfield și din tranzacțiile reale.

## Același stil: Cartea de stil
Fișier unic (`library/stil.json` + `docs/06-carte-de-stil.md`) pe care îl citesc Planificatorul, Montajul și QA:
- durată, structură (hook → demonstrație → detaliu → final), ritm de tăiere;
- font, mărime, poziție, contur, emoji pentru textul de pe ecran;
- reguli de muzică și sunet;
- lumină, culori, cameră fixă, fără zoom, fără text ars, fără branduri;
- regulile per categorie de produs (`docs/04-produs-universal.md`).
Orice regulă nouă de la Szasz intră aici și se aplică automat la toate videourile următoare.

## Cum rulează singur
- **Creierul**: sesiuni Claude Code programate (Routines) — dimineața research + plan, apoi loturi de producție la câteva ore, seara raport. Fiecare sesiune folosește Higgsfield prin MCP și agenți în paralel.
- **Mâinile**: scripturi Python în `engine/` (descărcare, tăiere, montaj ffmpeg, cozi, buget) — deterministe, ieftine, fără AI unde nu e nevoie.
- **Memoria**: starea în repo (`state/`), commit după fiecare lot.
- **Frâne**: buget zilnic de credite Higgsfield și Apify; oprire și raport când se atinge; niciodată același viral / set / hook prea des.
- **Szasz** primește doar raportul zilnic și poate interveni cu `regula: ...`.

## Ordinea de construcție
1. Cozi + stări + buget (`engine/queue`, `engine/budget`).
2. Vânător + Analist (Apify + cadre + audio).
3. Cartea de stil + Montaj automat.
4. Planificator cu scara uneltelor + Producător + QA.
5. Legătura cu `distribution/` și `social_tracker/`.
6. Învățarea (scoruri, reordonarea scării, promovarea hook-urilor).
7. Programarea (Routines) — sistemul pornește singur.

## Ținta: 10 produse în paralel, fără Szasz (10 oct 2026)
Fiecare produs e o „linie” separată, cu propria fișă (`products/`), propriile conturi, propria coadă și propriul buget. Agenții lucrează pe toate liniile odată.

| Ce se automatizează complet | Ce rămâne în afara aplicației |
|---|---|
| research, analiză, plan, producție, QA, montaj, caption-uri | crearea conturilor noi și postarea din telefon: le fac posterii, prin portal (`distribution/`), sau un serviciu de postare programată, dacă alegem unul |
| scorul, rotația, regulile noi din cifre | banii: bugetul lunar (Higgsfield, Apify, server) îl aprobă Szasz o dată pe lună |
| alegerea produselor care primesc mai mult volum, după cifre | adăugarea unui produs nou: un link (sau, mai târziu, scout-ul automat propune, Szasz zice da/nu) |

**Bugetul e frâna principală.** Ordin de mărime, din producția anterioară (sept–oct 2026): un video complet generat cu AI ≈ 300–400 credite. 10 produse × 10 videouri/zi = 100 videouri/zi ≈ 30.000–40.000 credite/zi dacă totul se generează de la zero. De aceea:
- reutilizarea (clipuri aprobate, B-roll per produs făcut o dată, hook-uri refolosite pe alt produs) e treapta 1 a scării de cost;
- bugetul se împarte automat între produse după cifre: produsele care vând primesc mai multe videouri, cele care nu, mai puține sau se opresc;
- ținta de cost pe video se fixează după research-ul Higgsfield și primele loturi.
