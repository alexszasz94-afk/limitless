# Operațiunea „Organic Dropshipping” (OD) — sistemul cap-coadă
Sursa: arhiva `library/sources/od-full/` (copie completă a drive-ului unui operator, dată unui partener; instantaneu din 7 oct 2026). Citite integral: `CLAUDE.md`, `AGENTS.md` (identic cu `CLAUDE.md`), `START_HERE.md`, `x_context/` (3 fișiere), `x_instructions/` (README + 01–10 + 12 + `skills/` 3 fișiere), `_tool/` (`NAMING.md` + 4 verificatoare). Pentru context am citit și textul din `x_systems/hooks/hooks_board.html` și `text_on_screen.txt`. · Data playbook-ului: 10 oct 2026

> **Atenție la sursă.** E o operațiune reală, dar cifrele sunt **declarate în arhivă** (nu verificate de noi). Proprietarul original apare în arhivă cu prenume; aici îl numim „proprietarul” [omis]. Cheile, emailurile, serverele, handle-urile personale au fost deja șterse din arhivă și nu le reproducem. `x_instructions/11_accounts_and_keys.md` e citat de mai multe fișiere, dar **lipsește din arhivă**.
> Căile sursă de mai jos sunt relative la `library/sources/od-full/`.

Rezultate declarate / vizibile:
- **Proiector de Crăciun (TheXmasGlow):** 25.817 $ și 259 comenzi în primele 6 zile (20–25 sept 2026), ~2k $ în primele 24 h; preț 79,99 $; cost ~2–3 $ la fabrică, ~8–10 $ livrat în SUA prin agent [`x_context/business.md`, `x_instructions/01_business_and_model.md`]. Oprit pe 6 oct 2026 [`x_context/decisions.md`].
- **Perdele LED (MerryGlowUSA, magazinul unui partener):** 126 comenzi în sept 2026 — 117 cu cardul (10.965,60 $), 8 PayPal (899,25 $, niciodată încasați), ~18M vizualizări pe conturi; preț 59,95 $ apoi pachete 79,99 / 139,99 / 189,99 $ [`x_context/business.md`, `x_instructions/01_business_and_model.md`]. Calculul nostru (nu al lor): ~11,9k $ / 18M ≈ **~660 $ / 1M vizualizări** — sub pragul nostru de 2.000 $/1M din `docs/09-reguli-produs.md`.
- **Proiector MerryGlowUSA:** 0 vânzări, oprit [`x_context/business.md`].
- **Concurenții** din nișa proiectorului: conturi IG noi ajung la 1–2M vizualizări pe un reel în câteva zile, cu CTA „Comment <WORD> to get the link” [`x_context/business.md`].

---

## 1. Modelul de business
- **Doar organic, fără reclame plătite.** Videouri scurte UGC-style generate cu AI (~11–18 s, 9:16) pe Instagram, Facebook, TikTok (YouTube Shorts renunțat pe 6 oct) → „Link in bio” → magazin Shopify [`x_context/business.md`, `x_context/decisions.md` 2026-10-06].
- Nișa: decor de Crăciun, public SUA întâi (comenzi și din UK, UE, AU, CA + ~20 țări); public „Christmas moms / parents / Christmas lovers”. Swanlift (sutien corector de postură) = primul produs non-Crăciun, făcut prin motion transfer [`x_instructions/01_business_and_model.md`].
- Ce au în comun cei doi câștigători (observație, nu regulă): decor de Crăciun, un „wow” vizual într-o cameră întunecată care merge fără sunet, unitate ieftină (~2–3 $) vândută la 60–80 $, ușoară și mică la livrare [`x_context/business.md`].
- Plăți: card prin Shopify Payments; PayPal scos (8 comenzi PayPal neîncasate) [`x_context/business.md`, `x_context/decisions.md` 2026-09-25].
- Omul conduce singur; prietenii din același business văd doar sistemele partajate (Product Finder, kit-ul de customer support) [`x_context/business.md`, `x_context/decisions.md` 2026-10-05].

## 2. Rolurile („agenții”)
OD **nu** e o buclă autonomă; e un om + un asistent AI pe un drive cu reguli stricte, plus câteva sarcini programate. Rolurile reale:

| Rol | Cine | Ce face | Sursa |
|---|---|---|---|
| Proprietarul | om | aprobă fiecare cadru și fiecare clip, alege produsul, alege personajul din shortlist, montează în CapCut, decide furnizorul, apasă „Send” la emailuri | `CLAUDE.md` §How a generation round runs; `x_instructions/03_video_pipeline.md` |
| Asistentul principal | Claude (sau Codex) în folderul drive-ului | generează cadre și clipuri în Higgsfield, arhivează prompturile, actualizează board-urile, rulează cele 5 verificări, face research | `CLAUDE.md`, `START_HERE.md` §4 |
| Subagent „a doua opinie” | Claude proaspăt | verifică etichetele de produs propuse pe Product Finder (contact sheet nou vs. cele existente) înainte de scriere | `x_instructions/skills/product-finder-import.md` §6 |
| Trecerea zilnică prin inbox | sarcină AI programată | etichetează emailurile, caută clientul în Shopify, lasă **o ciornă** per client per subiect; nu trimite niciodată | `x_instructions/09_customer_support.md` |
| Verificarea zilnică a furnizorilor | sarcină AI programată | citește WhatsApp / platforme / email, loghează ce e nou, spune ce cere decizie; nu trimite, nu răspunde, nu plătește | `x_instructions/10_fulfillment.md` |
| Scraper-ul orar | Social Tracker (Next.js + Apify) | vizualizări, câștig pe zi, urmăritori, fiecare postare la 24 h și 7 zile, ce video din Distribution merge | `x_instructions/08_social_tracker.md` |
| Posterii | oameni, fiecare cu link secret | creează conturi, încălzesc, postează videourile zilei cu caption-ul dat | `x_instructions/07_distribution_portal.md` |

## 3. Fluxul pas cu pas (produs → video postat → comenzi)
1. **Găsirea produsului — Product Finder.** Board de conturi concurente (IG/TikTok/FB), organizat **categorie → produs → variație → conturi**, un card per cont, cu cel mai văzut video al produsului pe care contul îl vinde **acum**, urmăritori și media vizualizărilor celor mai noi ≤20 videouri din acel „run”. Clasament pe percentile egale urmăritori + media vizualizărilor; cele mai slabe 50 listate separat [`x_instructions/05_product_finder.md`]. Linkurile veneau dintr-un grup privat WhatsApp de vânători de produse [`x_instructions/skills/product-finder-import.md`]. Din 6 oct: alegerea produsului se face **doar pe performanța video** (media ultimelor 20 videouri cu postări ≥12 h, mediana, trendul săptămânii, sezonul rămas) — fără scor pentru „potrivire AI” sau număr de magazine, „concurența nu e o problemă” [`x_context/decisions.md` 2026-10-06].
2. **Research de concurenți pentru un produs** — skill `instagram-competitor-research` (detalii §6) [`x_instructions/skills/instagram-competitor-research.md`].
3. **Furnizor.** Rapoarte Alibaba / AliExpress / DSers, apoi audit între agenți (CJ vs Zendrop); fără mostre (cer poză / video în cameră întunecată a unității reale); pe Alibaba plată doar prin Alibaba (Trade Assurance); niciodată DDU la consumator, doar DDP [`x_instructions/10_fulfillment.md`, `x_context/decisions.md` 2026-09-24, 09-30, 10-01].
4. **Magazin + suport:** fiecare magazin primește `support@<domeniu>`, totul citit într-un singur Gmail, ciorne AI zilnice [`x_instructions/09_customer_support.md`, `x_context/decisions.md` 2026-09-25].
5. **Folderul produsului** `BRAND - PRODUCT/` creat cu `new_board.py` [`x_instructions/02_drive_layout.md`].
6. **Plan video:** forma fixă — **C01 = hook (4–5 s, „decide tot”)**, C02–C04 B-roll 1 (produsul), C05–C07 B-roll 2 (recompensa); fiecare produs are o listă fixă de sloturi (ex. proiector: C02 mâini pe cutie, C03 proiectorul ridicat, C04 cablul intră, C05 ușa se deschide spre cameră, C06 săritura în pat, C07 camera întreagă de Crăciun) [`x_instructions/03_video_pipeline.md`, `_tool/NAMING.md` §6]. Hook-ul se ia de pe Hooks Board, textul de pe ecran din `text_on_screen.txt` [`x_instructions/06_hooks_board.md`].
7. **Cadre (start frames):** Higgsfield `gpt_image_2` / `gpt_image_2_5`; 2 referințe atașate — prima fixează geometria, a doua aspectul (packshot-ul canonic din `product_images/`) → card **FRAME FOR REVIEW** [`x_instructions/03_video_pipeline.md`].
8. **Aprobarea 1:** omul apasă Review pe board, Approve/Reject, „Copy decisions”, lipește liniile în chat → `decide.py` [`x_instructions/04_video_boards.md`].
9. **Clipuri:** doar din cadre aprobate, `seedance_2_5` (de obicei 720p/5 s) → **CLIP FOR REVIEW**; `add_card.py` refuză un clip pe un cadru neaprobat [`x_instructions/03_video_pipeline.md`, `CLAUDE.md`].
10. **Aprobarea 2** pentru clipuri, la fel.
11. **Upscale** (ByteDance din Higgsfield; Swanlift: Pro, 2K, 30 fps) în `clips/upscaled/` cu același nume [`x_instructions/03_video_pipeline.md`, `x_context/decisions.md` 2026-10-06].
12. **Montaj în CapCut** (om): textul hook-ului + melodie → `videos_to_post/video_<N>.mp4`, apoi se marchează pe board [`x_instructions/03_video_pipeline.md`].
13. **Cele 5 verificări** — toate exit 0 [`CLAUDE.md` regula 1].
14. **Postare prin Distribution:** persona per produs, manifest de conținut în ordinea de postare; program: ziua 1 conturi + încălzire, ziua 2 încălzire + profiluri, din ziua 3 câte 3 reel-uri/zi; același video și caption pe toate platformele; conturile de încălzire = magazinele concurente de pe Product Finder; videourile se postează de la cel mai nou spre cel mai vechi [`x_instructions/07_distribution_portal.md`, `x_context/decisions.md` 2026-10-06].
15. **Măsurare — Social Tracker:** date publice prin Apify, orar; postările se leagă de videouri **după caption**; plafon 400 $/lună [`x_instructions/08_social_tracker.md`, `x_context/decisions.md` 2026-10-06].
16. **Comenzi → fulfillment** prin agentul ales (Zendrop pentru 268 comenzi plătite) [`x_context/decisions.md` 2026-10-01].

**Varianta Swanlift (motion transfer):** board în coloane — rândul 1 reel-ul concurentului, rândul 2 femeia + camera nouă (de pe Pinterest), rândul 3 videoul final făcut cu Genjutsu `hf_mult_motion_control`; referințele fiecărei rulări se aprobă (stadiul `refs`) **înainte** de orice generare [`x_instructions/03_video_pipeline.md`, `x_context/decisions.md` 2026-10-05].

## 4. Convenții
**Naming (legea e `_tool/NAMING.md`):**
- Folder produs: `BRAND - PRODUCT`, ALL CAPS; înăuntru totul lowercase cu `_`; fără foldere `round1/ final/ new/ old/`, fără date în nume [`_tool/NAMING.md` §1].
- Fișiere: `v<N>_c<NN>_<g|r><K>.<ext>` — `g` = generare, `r` = referință; `c` mereu 2 cifre; K de la 1, nepadat, **niciodată refolosit**; cadrele și clipurile se numerotează separat; referințele PNG și MP4 împart aceeași secvență `r` [`_tool/NAMING.md` §4].
- O generare **nu se suprascrie niciodată** (nu-ți place `g1` → `g2`); fără sufixe-literă (`g1b`), fără nume descriptive (`final`, `best`), upscale-ul păstrează numele exact, folderul `clips/upscaled/` e sufixul [`_tool/NAMING.md` §4].
- Excepție: ancore la nivel de produs în `<PRODUS>/references/` cu nume descriptive stabile (`box_front.png`, `product_anchor.png`) [`_tool/NAMING.md` §4].
- Fișiere dispărute definitiv → `content/lost_takes.txt`; gunoiul → `to_delete/` la rădăcină [`_tool/NAMING.md` §3, §7].

**Foldere:** `video_N_assets/` conține exact `starting_frames/`, `clips/`, `references/`, `prompts.md`; produsul are `content/`, `product_images/`, `competition/<cont>/data.md`, `videos_to_post/`, `references/` și nimic altceva [`_tool/NAMING.md` §2–3, `x_instructions/02_drive_layout.md`].

**`prompts.md` = arhiva completă:** fiecare take, inclusiv eșecurile (motivul eșecului e „cel mai valoros lucru din fișier”): blocuri reutilizabile verbatim, per shot setări / job id / referințe în ordine / prompt imagine / prompt video / istoric, și la final `## Verified record — Higgsfield` (textul exact rulat de Higgsfield, care bate orice altceva din fișier). „Dacă nu poți re-crea un shot doar din prompts.md, e incomplet.” Golurile istorice se marchează explicit, nu se reconstruiesc [`_tool/NAMING.md` §5].

**Board-uri:**
- Board video per produs = **generat** din `content/_board_thumbs/board_data.json` de `build_board.py`; nu se editează niciodată HTML-ul; aspectul trăiește doar în `template/` [`CLAUDE.md` regula 2, `x_instructions/04_video_boards.md`]. O bandă per video, un card per shot, sertar „Prompts” cu textul exact + buton Copy; statusuri review / approved / rejected; take-urile respinse rămân în „Other takes on disk” cu motivul [`_tool/NAMING.md` §6].
- Board Product Finder (generat din `board_data.json` de `product_finder.py`) [`x_instructions/05_product_finder.md`].
- Hooks Board (manual): 14 hook-uri dovedite în 4 concepte + lista „Text on screen” [`x_instructions/06_hooks_board.md`].
- Panou Notes pe fiecare board, care scrie singur în `board_notes.txt` (privat; AI-ul nu-l citește niciodată) [`CLAUDE.md` §Private files].
- Concurență: unelte scriu printr-un fișier exclusiv `<file>.building` și refuză salvarea dacă `board_data.json` s-a schimbat de la citire (gardă md5 anti-pierdere) [`CLAUDE.md` §Two facts].

## 5. Deciziile din `x_context/decisions.md` (cu motivele)
Jurnal **append-only**: o linie = dată, decizie, de ce; o decizie se anulează doar cu o linie nouă; motivul „oprește un agent viitor să «îmbunătățească» ceva deja respins”.

| Data | Decizia | De ce |
|---|---|---|
| 09-17 | Cutie TheXmasGlow verde festivă, 15×15×24 cm | proprietarul a vrut pachet mai mare |
| 09-21 | Referințe PNG și MP4 permise, aceeași secvență `r<K>` | — |
| 09-23 | Produsul-test „retro handset” șters, nu se recreează | era test |
| 09-23 | Toate board-urile generate din `board_data.json`, un singur template | un sistem care poate reconstrui orice board |
| 09-23 | Două aprobări per video: toate cadrele, apoi clipurile | — |
| 09-24 | O generare per shot, apoi aștepți review-ul | take-urile în plus ard credite; vrea să judece fiecare |
| 09-24 | Fără comenzi de mostre; poză / video în întuneric al unității reale | — |
| 09-24 | Alibaba: plată doar prin Alibaba | Trade Assurance acoperă doar ce se plătește acolo |
| 09-25 | `support@<domeniu>` per magazin, totul într-un Gmail | — |
| 09-25 | PayPal oprit | 899 $ din 8 comenzi neîncasați |
| 09-27 | Sisteme partajate separat de cele personale; board de sisteme ca artifact privat read-only (renunțat la server/Coolify) | doar ce pot vedea prietenii |
| 09-27 | Perdele LED și proiector MerryGlowUSA oprite | — |
| 09-29 | Product Finder: cel mai văzut video, etichete verificate pe footage; clasament pe urmăritori **+** media ultimelor 20 | urmăritorii singuri nu măsoară performanța |
| 09-30 | Doar **ultimul produs promovat** de fiecare cont (run continuu), media ≤20 videouri cu eșantionul real afișat; conturile mixte marcate | conturile schimbă produsul; succesul vechi induce în eroare |
| 09-30 | Excluderile manuale și conturile neverificate nu revin la refresh | proprietarul îngustează lista |
| 09-30 | Toate melodiile într-un singur folder (anulează 09-23) | așa se ținea de fapt |
| 09-30 | Verificările doar verifică; aprobarea aparține fișierului exact | auditul a găsit un clip adăugat pe un cadru neaprobat |
| 09-30 → 10-01 | Fulfillment: CJ (2.620–2.641 $ vs 3.672,06 $) → apoi **Zendrop** (3.459,86 $) | auditul Zendrop: diferența reală ~770 $, toate comenzile deja prețuite și livrabile, taxa UE inclusă; CJ cerea 35 linii, 34 lente, IOSS și corecturi de telefon |
| 10-01 | Hooks Board devine baza viitoarelor sisteme | va fi înlocuit de un dashboard complet |
| 10-01 / 10-05 | Product Finder: split „Real UGC / Other”, apoi **scos** | AI și UGC real nu se mai pot deosebi; etichetele derivaseră |
| 10-02 / 10-05 | Skill-urile: întâi în folder, apoi doar în contul Claude | folderul doar dubla copiile din cont |
| 10-05 | Importul Product Finder mutat de la ChatGPT la Claude, cu unealtă permanentă; Apify doar prin unealtă, cheile nu se tipăresc | vechiul generator stătea într-un folder temporar |
| 10-05 | Swanlift: board în coloane, referințele aprobate înainte de generare | vede referința lângă personajul nou și rezultat, review mai rapid |
| 10-05 | Distribution: portal de postare pentru o echipă | ~50 videouri/zi cer o echipă și un sistem care spune fiecăruia exact ce să facă |
| 10-05 | Server Hetzner CX23 (~10,15 $/lună), Docker Compose + Caddy, pull din GitHub la 2 min | cea mai ieftină variantă care merge; Coolify/Dokploy respinse (securitate, riscuri SQLite/video) |
| 10-06 | Distribution live pe Swanlift; program pe zile; fără blocarea „o zi pe zi calendaristică”; 3 reel-uri/zi, cel mai nou primul | în zilele bune postează de mai multe ori; crește după performanță |
| 10-06 | Social Tracker pe server (nu artifact), plafon Apify 400 $/lună | cere scheduler orar, chei, bază de date în creștere |
| 10-06 | Cifrele IG din scraper-ul **live** de profil, nu din cele „by URL”; vizualizări IG = doar redări IG | scraperele by-URL dau cifre vechi de ore (374 timp de o oră când reel-ul avea 828, apoi 890) |
| 10-06 | Produsele se aleg doar pe performanța video | modelul AI poate face orice produs, concurența nu e o problemă |
| 10-06 | Proiectorul oprit și dat partenerului | nu-l mai rulează |

## 6. Skill-urile (procedurile rulate ca skill-uri Claude)
### `pinterest-casting` [`x_instructions/skills/pinterest-casting.md`]
- **Intrare:** reel-ul concurentului (`vN_c01_r1.mp4`). **Ieșire:** femeia + camera alese, salvate ca `vN_c01_rK.png`, înregistrate în `prompts.md`, puse pe board în stadiul `refs`. **0 credite** Higgsfield.
- Pași: analiza reel-ului cadru cu cadru (ffprobe/ffmpeg pentru tăieturi, foi 2 fps, cadrul de început / mijloc / sfârșit al fiecărui shot) → **brief de casting** (listă de shot-uri, femeia, garderoba, camera, riscuri, plan de căutare) → căutare Pinterest în Chrome („30 year old woman” + trăsături; camere „real bedroom interior iphone”), „More like this” e cea mai bună căutare, 60–120 candidați / rol → primă tăiere pe miniaturi (12–20) → inspecție la mărime completă cu decupaje față / mâini / linia părului → shortlist 4–6 femei, 3–4 camere → omul alege → salvare PNG fără redimensionare, md5.
- Reguli: femei realiste ~30 de ani, **nu căuta „AI”** (alegerile găsite așa au fost respinse ca nerealiste); fără celebrități; **o femeie și o cameră pe tot videoul**; **hainele din poză „curg” în video** (tricoul alb a apărut sub sutien în unele shot-uri) → haine minime, simple, mulate; corp asemănător cu femeia din reel (motion transfer păstrează pozele; un corp diferit se deformează); fără lenjerie / decolteu (risc nsfw); ≥ ~1000 px; camera: fără oameni, fără randări, lumina potrivită (zi/noapte, cald/rece), loc liber pe podea la distanța camerei din reel.
- În prompt: descrierea femeii doar față / păr / piele / corp, niciodată haine; linie separată pentru partea de jos; descrierea camerei cu lumina.
- La respingere: motivul exact devine regulă în brief („prea perfectă” → verificare de realism mai strictă).

### `product-finder-import` [`x_instructions/skills/product-finder-import.md`]
- **Intrare:** linkuri noi (din WhatsApp sau tab-urile păstrate după research). **Ieșire:** un lot datat de conturi noi pe board + fișier de evidență `raw/research/update_<lunăzi>_review.json` + raport.
- Pași: `check` exit 0 și copie de siguranță → colectare linkuri → `triage` (present / removed / new / needs_resolution) → rezolvare reel → cont prin Apify → istoric 60 reel-uri prin Apify (`videoPlayCount` exact) → **run-ul continuu cel mai recent** (foaie 3×3 per video, footage-ul decide, nu numele / bio / caption-ul) → etichetare + a doua opinie de la un subagent → video prezentat = cel mai văzut din run, media pe ≤20 → descărcare media yt-dlp + verificare ffprobe → scriere cu gardă md5 → `product_finder.py all` exit 0 → verificare în browser → raport.
- Reguli: același produs fizic = același produs și aceeași variație; designurile, fanii, nișele, sezoanele sunt variații; „necunoscut nu e zero”; nu se readuce un cont șters; ~0,003 $ / profil sau reel pe Apify, rulări mici (≤6 conturi, plafon 1 $).

### `instagram-competitor-research` [`x_instructions/skills/instagram-competitor-research.md`]
- **Intrare:** un produs de referință + modul **EXACT** (același produs) sau **VARIATIONS** (toate temele: Grinch, echipe NFL, profesii etc.). **Ieșire:** toți vânzătorii reali activi, clasați după media vizualizărilor ultimelor 10 reel-uri, deschiși în Chrome câte 5, + rezumat (tabel, piața în 3–5 rânduri, harta nișelor, ce s-a scos și de ce, acoperire). Nimic pe board până la „add them”.
- Setări implicite: activ = reel în ultimele 30 de zile; slab = media ultimelor 10 sub 5.000; toate limbile; la sezoniere se listează și vânzătorii „adormiți”.
- Canale: căutare IG pe cuvinte cheie (toate formulările și ordinea cuvintelor — „posture bra” dă 25+ pagini, „bra for posture” nimic; vânzători noi încă apăreau la paginile 30–40), hashtag-uri, căutare de conturi, **Meta Ad Library** (217 advertiseri pentru sutienul de postură), Google `site:instagram.com`, Google Lens pe pozele produsului (magazine cu aceleași poze de furnizor), căutare în Shop app, footer-ul magazinelor; apoi „bulgăre de zăpadă” din hashtag-urile / audio-urile / tag-urile câștigătorilor până nu mai apare nimic nou.
- Reguli: **niciodată nu măsura din rezultatele căutării** (un cont părea 10K în căutare și avea 902K pe cel mai bun reel); clasează după performanță, niciodată după urmăritori; fiecare cont care trece cifrele e **văzut** (copertele ultimelor 8 reel-uri) și primește verdict yes / mixed / no / unclear cu o linie de dovadă; cifrele trebuie să vină din produsul respectiv (un cont avea 2M pe un look-alike, nu pe produs); majoritatea conturilor care trec cifrele **nu** sunt vânzători (21 din 337); semnalează temele licențiate (Grinch, Disney, NFL) ca risc de takedown; contul omului nu se atinge (fără follow / like / DM), ritm ~1 cerere / 2 s, oprire la blocare.
- Durată: 1,5–3 ore, mai ales nesupravegheat; ~900 candidați ≈ 45 min de măsurare.

## 7. Regulile de calitate
**Cele trei reguli absolute** [`CLAUDE.md`]:
1. Nu inventa un nume de fișier (`_tool/NAMING.md`); după orice schimbare, cele 5 comenzi (build board, check_naming, make_thumbs, mark_lost, check_board) trebuie să iasă cu 0, iar codurile de ieșire se raportează; un filtru care nu prinde nimic iese cu 2 = „nimic verificat”.
2. Nu construi nimic ce nu s-a cerut (mai ales HTML, dashboard-uri, scripturi noi) — „spune într-un rând și așteaptă”.
3. „Animează la fel” = **copiezi promptul, nu ideea**: iei textul `— IN THE CUT` din Verified record, îl lipești byte cu byte (bloc CAMERA, ritmurile cu intervale de timp, lista de interdicții), schimbi doar substantivele care diferă fizic (camera, produsul, persoana, culoarea), păstrezi setările (alt model = altă animație) și notezi `Reused from v20 C02 — changed: …`. „Două prompturi care înseamnă același lucru pentru un om produc videouri diferite.”

**Regulile de generare** [`CLAUDE.md` §How a generation round runs; `x_systems/hooks/hooks_board.html`]:
- Atașează cadrul care deține geometria; 2 referințe: una pentru layout, una pentru aspect, **ordinea contează**; repetă geometria și în textul promptului, altfel revine un bug deja reparat.
- O corectură de mișcare / timp / număr = **editare de prompt** pe același cadru, nu cadru nou.
- **Tot ce se mișcă trebuie să existe în cadrul de start** (altfel apare din nimic și pare fals).
- Ritmuri cu intervale explicite („0.0–1.5s — …”); un ritm care lipsește e de obicei o problemă de durată (hook-ul 08 și-a pierdut a treia numărătoare la 4 s, a recuperat-o la 5 s).
- O referință video **importă și audio-ul și conținutul ei** și trebuie să aibă ≥ 2 s: atașezi o copie fără sunet și spui în prompt că e mută (hook-ul 13 a amestecat două clipuri și a trebuit refăcut fără referință video).
- Fără text în cadru, niciodată; textul se pune în CapCut.
- Descrie produsul exact ca unitatea reală (ex. proiector alb, lentilă neagră din plasă, USB-C, fără baterie) [`x_context/business.md`].
- Regulile creative specifice (firul negru al perdelei, cutia fără fereastră, cadrul canonic C02) stau în `prompts.md` și în panourile board-ului; se citesc **înainte** de generare [`CLAUDE.md`, `x_instructions/03_video_pipeline.md`].

**Disciplina de lucru:** o generare per shot, apoi stop — fără auto-review și re-roll nesolicitat [`x_context/decisions.md` 2026-09-24]; nu spune „verificat” pentru un pas sărit [`x_instructions/skills/product-finder-import.md` §11]; scrieri verificate cu md5 (drive-urile sincronizate trunchiază scrierile) [`CLAUDE.md` §Two facts].

## 8. Hook-urile dovedite [`x_instructions/06_hooks_board.md`, `x_systems/hooks/hooks_board.html`]
14 hook-uri C01 (4–5 s) în 4 concepte, fiecare cu prompt imagine + prompt clip verbatim, setări, referințe în ordine, listă „ce schimbi pentru alt produs” și un tabel „Reuses” (o linie la fiecare refolosire: dată, produs, ce s-a schimbat, a mers?, lecția):
1. **Store discovery (01–07)** — produsul găsit pe raft / palet / capăt de raft; „credibilitatea e tot trucul: un străin care reacționează la marfa din magazin pare filmare accidentală, nu reclamă”.
2. **3-2-1 reveal (08–09)** — numărătoare + cearșaf / pătură trasă de pe produs.
3. **Gifting POV (10)** — cutia împachetată îți e aruncată pe picioare, în pat.
4. **Pattern interrupt (11–14)** — ceva merge prost (cade de pe scară, bradul ia foc).
Text pe ecran care a mers: „Do NOT let a Christmas mom see this 🎄🎁”, „Every Christmas mom NEEDS this 🎄🎁”, „Christmas Parents...don't walk RUN to Costco...🎅🎄”, „Christmas Decor in 1965🤮 - Vs.. - Christmas Decor in 2026 🎄🎁” [`x_systems/hooks/text_on_screen.txt`]. Setări pe board: cadre 2k, clipuri 1080p, modele `gpt_image_2`, `gpt_image_2_5`, `nano_banana_2`, `seedance_2_5`.

## 9. Cifre și costuri
| Ce | Cifra | Sursa |
|---|---|---|
| Server Distribution + Tracker | Hetzner CX23, ~10,15 $/lună cu TVA | `x_context/decisions.md` 2026-10-05 |
| Apify Tracker | plafon 400 $/lună | `x_context/decisions.md` 2026-10-06 |
| Apify Product Finder | ~0,003 $ / profil sau reel; rulări ≤ 1 $ | `x_instructions/skills/product-finder-import.md` |
| Fulfillment 268 comenzi | Zendrop 3.459,86 $ (CJ 2.620–2.641 $) | `x_context/decisions.md` 2026-09-30, 10-01 |
| Produs | ~2–3 $ fabrică, ~8–10 $ livrat SUA, vândut 79,99 $ | `x_context/business.md` |
| Volum țintă postare | ~50 videouri/zi (echipă de posteri) | `x_context/decisions.md` 2026-10-05 |
| Producție | 35 + 30 + 8 videouri finale pe 3 produse | `CLAUDE.md` |
Costul în credite Higgsfield per video **nu apare** în fișierele citite.

## 10. Ce e automatizat și ce face omul
| Automat (AI / scripturi) | Omul |
|---|---|
| generarea cadrelor și clipurilor la cerere; arhivarea prompturilor; board-urile generate; cele 5 verificări | aprobă fiecare cadru și fiecare clip (2 aprobări per video) |
| research de concurenți, importul pe Product Finder, clasamentul | alege produsul; închide tab-urile pe care nu le vrea (cele rămase = lista aprobată) |
| casting Pinterest până la shortlist | alege femeia și camera |
| ciorne zilnice pentru suport; verificarea zilnică a furnizorilor | trimite emailurile; decide și plătește furnizorul |
| tracker orar de cifre; portalul spune posterilor ce să facă | montajul în CapCut (text + melodie); postarea (posterii, din telefon); crearea conturilor |

---

## Ce preluăm în LIMITLESS
Legenda: **[adoptăm direct]** · **[adaptăm]** · **[conflict cu regulile noastre: …]** (`docs/02-reguli.md`). Tot ce e aici rămâne ipoteză până îl confirmă cifrele noastre (`social_tracker/`).

1. **[adoptăm direct]** „Copiezi promptul, nu ideea”: refolosirea unui clip/hook pornește din promptul exact rulat, lipit byte cu byte, cu doar substantivele schimbate și setările păstrate, plus linia de proveniență `Reused from … — changed: …`. Intră în `engine/produce` și e baza treptei 1 „Reutilizare” din `docs/05-motorul-autonom.md`. — `CLAUDE.md` regula 3; `x_systems/hooks/hooks_board.html`.
2. **[adoptăm direct]** Arhivă completă per video (`prompts.md` cu toate take-urile, inclusiv eșecurile și motivul, + „Verified record” = textul exact de pe jobul Higgsfield). La noi: `state/` (o fișă per video, citită de Învățare ca să știe ce a eșuat și de ce). — `_tool/NAMING.md` §5.
3. **[adaptăm]** Naming strict și imuabil (`v<N>_c<NN>_g<K>`, niciodată suprascris, fără sufixe) → pentru noi cu prefix de produs și stare (`<produs>/v<N>/c<NN>_g<K>`), pentru `engine/queue` și `output/`. — `_tool/NAMING.md` §4.
4. **[adoptăm direct]** Regulile de generare: tot ce se mișcă există în cadrul de start; 2 referințe (geometrie întâi, aspect al doilea, ordinea contează); ritmuri cu intervale de timp explicite; o corectură de mișcare = editare de prompt pe același cadru. Intră în `engine/produce` și în Cartea de stil (`docs/06-carte-de-stil.md` / `library/stil.json`). — `CLAUDE.md` §How a generation round runs; `x_systems/hooks/hooks_board.html`.
5. **[adoptăm direct]** Referința video la Genjutsu / Seedance: ≥ 2 s, copie **fără sunet**, spus în prompt că e mută; ea importă și conținut, nu doar mișcare. Verificare automată în `engine/produce` înainte de trimitere (confirmă și capcana noastră cu clipurile de mișcare sub 2 s). — `x_systems/hooks/hooks_board.html`.
6. **[adoptăm direct]** Casting Pinterest pentru motion control: brief din reel-ul tăiat pe shot-uri; „30 year old woman” + trăsături, niciodată „AI”; corp asemănător cu cel din viral; haine minime și simple (hainele din poză apar în video); o singură persoană și o singură cameră pe tot videoul; inspecție la mărime completă (față, mâini, linia părului). Intră în `engine/sets`. — `x_instructions/skills/pinterest-casting.md`.
7. **[adaptăm]** Pragul de rezoluție de la casting (~1000 px) → păstrăm pragul nostru de ≥ 1080 px; alegerea finală o face QA + scorul, nu omul (Szasz poate interveni). `engine/sets`. — `x_instructions/skills/pinterest-casting.md` Hard rules 2, Step 4; `docs/02-reguli.md` (2 oct).
8. **[adaptăm]** Analiza viralului pentru casting (tăieturi cu `ffmpeg select=gt(scene,0.25)`, foi 2 fps, cadrul de început / mijloc / sfârșit per shot, riscuri nsfw/păr/rotiri) → devine fișa de cadre a Analistului (`engine/analyze`). — `x_instructions/skills/pinterest-casting.md` Step 1.
9. **[adoptăm direct]** Regula „run-ul continuu cel mai recent”: un cont concurent se judecă doar pe produsul pe care îl vinde **acum**; footage-ul decide eticheta (nu numele / bio / magazinul); același produs fizic = același produs; necunoscut ≠ zero. Intră în `engine/hunter` și `library/competitori/<nisa>.json`. — `x_instructions/05_product_finder.md`; `x_context/decisions.md` 2026-09-30.
10. **[adaptăm]** Metrica de clasare a concurenților (media ultimelor 10–20 reel-uri, mediana, prag „slab” < 5.000, „activ” = reel în 30 de zile, niciodată după urmăritori) → completează semnalul nostru de viteză (≥ 100k în 24 h) din `docs/08-competitori-on-the-rise.md`, ca filtru de bază în `engine/hunter`. — `x_instructions/skills/instagram-competitor-research.md` Step 1, 5; `x_context/decisions.md` 2026-10-06.
11. **[adoptăm direct]** „Nu măsura niciodată din rezultatele căutării” — cifrele vin doar din reel-urile proprii ale contului; și „cifrele trebuie să vină din produs” (nu dintr-un look-alike al aceluiași cont). `engine/hunter`, `engine/research`. — `x_instructions/skills/instagram-competitor-research.md` Hard rules 2, Step 6.
12. **[adaptăm]** Canalele de descoperire a vânzătorilor: Meta Ad Library (advertiseri activi, toate țările), Google `site:instagram.com`, Google Lens pe pozele produsului, Shop app, toate formulările și limbile cuvântului cheie, „bulgăre de zăpadă” din hashtag-uri / audio-uri / tag-uri. La noi prin Apify în `engine/hunter` și `engine/product-scout` (`docs/07-scout-meta-ads.md`), nu prin Chrome-ul lui Szasz. — `x_instructions/skills/instagram-competitor-research.md` Step 2, 4, 8.
13. **[conflict cu regulile noastre: aplicația lucrează singură, nu în sesiunea logată a lui Szasz]** Biblioteca JS care reia endpoint-urile private Instagram din Chrome-ul logat al omului (ritm 1 cerere / 2 s, risc de blocare a contului). Nu o preluăm; dacă Apify nu acoperă ceva, decide Szasz. — `x_instructions/skills/instagram-competitor-research.md` Hard rules 1, 8–9, Technical reference.
14. **[adoptăm direct]** Verdictul vizual pe fiecare cont care trece cifrele (yes / mixed / no / unclear + o linie de dovadă; rețele cu același magazin grupate; afiliații „comment X” = no) — majoritatea conturilor cu cifre bune nu sunt vânzători (21 din 337). Pas de QA al Vânătorului în `engine/hunter`. — `x_instructions/skills/instagram-competitor-research.md` Step 6.
15. **[adoptăm direct]** Harta nișelor în modul VARIATIONS + semnalarea temelor licențiate (Grinch, Disney, NFL) ca risc de takedown → alimentează `engine/variations` (`docs/08-competitori-on-the-rise.md` §2). — `x_instructions/skills/instagram-competitor-research.md` Step 2, 9.
16. **[adaptăm]** Tiparul de hook-uri dovedite (4 concepte: descoperire în magazin, 3-2-1, cadou POV, „ceva merge prost”) + tabelul „Reuses” per hook (unde a fost refolosit și cu ce rezultat) → în `engine/hooks` ca format al fișei de hook și scor de încredere; dar hook-urile le luăm din UGC reale, nu le generăm de la zero. — `x_instructions/06_hooks_board.md`; `x_systems/hooks/hooks_board.html`; `docs/02-reguli.md` (10 oct, UGC).
17. **[adaptăm]** Formatele de text pe ecran care au mers („Do NOT let a <public> see this”, „Every <public> NEEDS this”, „<public>... don't walk RUN to <magazin>”, „<produs> in 1965 vs 2026”) → șabloane în `library/stil.json` pentru Montaj, ca ipoteze cu public înlocuibil, legate de acțiunea hook-ului (regula 2 oct). — `x_systems/hooks/text_on_screen.txt`.
18. **[adaptăm]** Forma fixă a videoului: C01 hook 4–5 s + listă fixă de sloturi B-roll per produs → la noi „B-roll per produs făcut o dată” (`library/fixed`, treapta 1 de cost) + durată 15–18 s din regula noastră (ei: 11–18 s). — `x_instructions/03_video_pipeline.md`; `_tool/NAMING.md` §6; `docs/02-reguli.md` (2 oct).
19. **[conflict cu regulile noastre: aplicația lucrează singură, QA vizual max 3 încercări]** „Două aprobări umane per video” și „o generare per shot, fără auto-review / re-roll”. Păstrăm doar ideea că o aprobare aparține fișierului exact (un clip nu se face pe un cadru neverificat): în `engine/qa`, aprobarea = verdictul QA pe acel fișier. — `CLAUDE.md`; `x_context/decisions.md` 2026-09-23, 09-24, 09-30.
20. **[conflict cu regulile noastre: baza de unelte e EXCLUSIV Genjutsu, Seedance 2.5, GPT Image 2.5]** Prompturile lor folosesc `gpt_image_2` și `nano_banana_2`, iar upscale-ul ByteDance e altă unealtă. Le putem refolosi textul doar re-rulat pe `gpt_image_2_5`; upscale-ul nu intră fără decizia lui Szasz. — `x_instructions/03_video_pipeline.md`; `x_systems/hooks/hooks_board.html`; `x_context/decisions.md` 2026-10-06.
21. **[adaptăm]** Clipurile lor la 720p / 5 s → pentru noi 720p / 480p doar ca test de mișcare, finalul la 1080p (`docs/11-costuri.md`). `engine/produce`. — `x_instructions/03_video_pipeline.md`.
22. **[adoptăm direct]** Board-uri **generate din date**, niciodată editate de mână; aspectul trăiește într-un singur template; o reconstrucție refă orice board. Pentru `dashboard/` și `engine/report`. — `CLAUDE.md` regula 2; `x_context/decisions.md` 2026-09-23.
23. **[adoptăm direct]** Garda anti-pierdere pentru agenți în paralel: scriere printr-un fișier exclusiv `.building` + refuz dacă fișierul s-a schimbat de la citire (md5); verificare md5 după fiecare scriere. Esențial pentru coada comună din `engine/queue`. — `CLAUDE.md` §Two facts; `x_instructions/skills/product-finder-import.md` §9.
24. **[adaptăm]** Verificatoare care doar verifică și ies cu cod (0 = curat, 1 = de reparat, 2 = filtrul n-a prins nimic), rulate după fiecare lot, codurile raportate, nimic declarat „verificat” dacă a fost sărit → `engine/` (verificări de stare, fișiere, linkuri) înainte de commit. — `CLAUDE.md` regula 1; `_tool/mark_lost.py`; `_tool/check_naming.py`.
25. **[adaptăm]** Jurnal de decizii append-only cu **motivul** fiecărei decizii (o decizie se anulează doar cu o linie nouă) → adăugăm „de ce” la liniile din `docs/02-reguli.md`, ca Învățarea să nu „îmbunătățească” ce a fost deja respins. — `x_context/decisions.md` (antet).
26. **[adoptăm direct]** Tracker: cifrele IG din scraper-ul **live** de profil, nu din cele „by URL” (cifre vechi de ore); vizualizări IG = doar redări IG; postarea se leagă de video după caption (deci caption unic per video). `social_tracker/`. — `x_context/decisions.md` 2026-10-06; `x_instructions/08_social_tracker.md`.
27. **[adoptăm direct]** Distribuția: program pe zile (ziua 1 conturi + încălzire, ziua 2 încălzire + profil, din ziua 3 câte 3 reel-uri/zi, crescut după cifre), același video și caption pe IG / TikTok / FB, conturile de încălzire = conturile concurente din research, fără blocarea „o zi pe zi calendaristică”. Deja în `distribution/config/schedule.json` și `personas.json`; legăm lista de încălzire de `library/competitori/`. — `x_context/decisions.md` 2026-10-06; `x_instructions/07_distribution_portal.md`.
28. **[adoptăm direct]** Plafon lunar dur pe cheltuiala Apify a tracker-ului și plafon per rulare (ei: 400 $/lună, ≤ 1 $/rulare) → `engine/budget` și `config/costs.json`. — `x_context/decisions.md` 2026-10-06; `x_instructions/skills/product-finder-import.md` §4.
29. **[adoptăm direct]** Server: un VPS mic (~10 $/lună), Docker Compose + Caddy comun pentru ambele aplicații, deploy prin push pe `main`; Coolify/Dokploy respinse. Confirmă ce avem în `SETUP-DISTRIBUTIE.md`. — `x_context/decisions.md` 2026-10-05, 10-06.
30. **[adaptăm]** Customer support: `support@<domeniu>` per magazin, un singur inbox, trecere AI zilnică cu etichete + căutare în Shopify + **ciornă** per client; pentru noi modulul „customer support” al platformei, cu ciorne pe care Szasz le aprobă la început și trimitere automată doar pe categorii sigure, după decizia lui. — `x_instructions/09_customer_support.md`; `docs/02-reguli.md` (10 oct, platformă).
31. **[adaptăm]** Fulfillment: un jurnal de conversație verbatim per furnizor, un tabel de stare, verificare AI zilnică care nu trimite și nu plătește; comparație pe cost per comandă livrată în SUA + zile până la expediere. Modulul „fulfillment” al platformei. — `x_instructions/10_fulfillment.md`; `x_context/priorities.md`.
32. **[adoptăm direct]** Reguli de furnizor: pe Alibaba plată doar prin Alibaba; niciodată DDU la consumator, doar DDP (altfel taxe vamale → chargeback); auditul real al costului total, nu prețul afișat (CJ părea cu ~1.050 $ mai ieftin, diferența reală ~770 $ plus 35 de linii de reparat). Intră la criteriul 9 „Livrare și risc” din `docs/09-reguli-produs.md`. — `x_instructions/10_fulfillment.md`; `x_context/decisions.md` 2026-09-24, 09-30, 10-01.
33. **[conflict cu regulile noastre: `docs/08` §2 spune „se comandă mostra” după test]** OD: fără comenzi de mostre, doar poză / video în întuneric al unității reale. De decis de Szasz care regulă rămâne. — `x_context/decisions.md` 2026-09-24.
34. **[conflict cu regulile noastre: plățile prin alt procesator, nu Shopify Payments (`docs/10`)]** OD încasează cu cardul prin Shopify Payments și a scos PayPal. Preluăm doar lecția: un procesator care nu încasează (899 $ pierduți la PayPal) se oprește repede. `engine/store`. — `x_context/business.md`; `x_context/decisions.md` 2026-09-25.
35. **[conflict cu regulile noastre: filtrul 2 din `docs/09` cere ≤ 4 concurenți organici]** OD (6 oct) a scos concurența din scorul de produs („modelul AI poate face orice produs”). Notăm ca ipoteză opusă; o testăm pe cifrele noastre înainte să schimbăm filtrul. — `x_context/decisions.md` 2026-10-06.
36. **[adaptăm]** Benchmark-ul lor ca reper pentru test order: perdelele LED ≈ ~660 $ / 1M vizualizări (calculat de noi din 11,9k $ / ~18M) — sub pragul nostru de 2.000 $/1M, deci produsul ar fi fost respins de filtrul nostru; proiectorul: 25.817 $ în 6 zile, fără vizualizări în arhivă. Intră ca date de calibrare în `docs/09-reguli-produs.md` §2. — `x_instructions/01_business_and_model.md`; `x_context/business.md`.
37. **[adaptăm]** Criteriile observate la câștigători (wow vizual într-o cameră întunecată fără sunet, cost 2–3 $ vândut la 60–80 $, mic și ușor de livrat) → câmpuri în profilul produsului (`engine/product-profile`, `docs/04-produs-universal.md` §2). — `x_context/business.md`.
38. **[adoptăm direct]** Comunicare cu Szasz în timpul lucrului lung: un rând la început cu ce rulează și cât durează, pe parcurs doar fapte măsurate și verificate, niciun „top” înainte de verificarea vizuală. Pentru raportul zilnic (`engine/report`, Telegram). — `x_instructions/skills/instagram-competitor-research.md` §Talking to Daniel.
39. **[conflict cu regulile noastre: LIMITLESS trebuie să fie o platformă completă, cu pagini]** Regula OD „nu construi nimic ce nu s-a cerut, mai ales HTML / dashboard-uri”. Preluăm doar spiritul pentru agenți: niciun fișier / pagină / script în afara modulelor din `docs/01-pipeline.md` fără să fie cerut. — `CLAUDE.md` regula 2.
