# Higgsfield — mecanica uneltelor (Genjutsu · Seedance 2.5 · GPT Image 2.5)

> **Regula din 10 oct (Szasz):** din Genjutsu folosim DOAR motion control (`hf_mult_motion_control`). Secțiunile despre `hf_mult_replace_object` rămân doar ca informație — nu intră în producție.

Manual tehnic pentru agenții LIMITLESS (Planificator, Producător, QA) care refac virale de produs cu alt personaj și altă cameră. Arată ce face fiecare unealtă cu fiecare intrare: prompt, imagini, video, audio. Data: 10 oct 2026.
Completează `playbooks/higgsfield.md` (sinteza YouTube): acolo sunt regulile generale, aici sunt mecanismele și rețetele.

**Cum se citesc sursele**
- `HG:<fișier>` = experiența REALĂ HeatGrump (sept–oct 2026, ~30 de reel-uri, sute de generări), în `/home/user/heatgrump/`. Produsul era un halat. Regulile specifice halatului apar doar ca exemplu de mecanism.
- `[ID](https://youtu.be/ID)` = canalul YouTube oficial Higgsfield, preluat din `playbooks/higgsfield.md`. Ce s-a spus acolo pentru Seedance 2.0 sau GPT Image 2 e marcat „(spus pentru 2.0)”.
- `C` = prețuri măsurate cu `get_cost` pe 10 oct 2026, fără generare (`docs/11-costuri.md`).
- **Etichete:** **[confirmat]** = am văzut asta în producție. **[YT]** = spus de Higgsfield, netestat la noi. **[ipoteză]** = dedus de noi, de verificat cu cifre (§10).
- Atenție la versiuni: în HeatGrump s-au folosit `gpt_image_2` și `seedance_2_5`. Tot ce scrie aici despre `gpt_image_2_5` vine din experiența cu `gpt_image_2`. Comportamentul ar trebui să fie apropiat, dar e **[ipoteză]** până la primele generări.

---

## 0. Specificații și prețuri (C, 10 oct 2026)

| Unealtă | Model / rol | Parametri | Preț (credite) |
|---|---|---|---|
| Genjutsu motion transfer | `hf_mult_motion_control` | doar `resolution` 480p/720p/1080p. `medias`: `image_references` (personaj, cameră, produs) + **exact un** `video_references` (clipul de mișcare) | 1080p: **44 minim** pentru o referință ≤ ~4 s, **55** la ~5 s (~11 cr/s). 720p ~5 s = 35. 480p ~5 s = 15 |
| Genjutsu object replacement | `hf_mult_replace_object` | înlocuiește obiect, produs, haină sau personaj într-un video sursă, din imagini. Cere cel puțin o imagine | 1080p ~5 s = 55 |
| Seedance 2.5 | `seedance_2_5` | `mode`: `t2v` / `omni_reference` (start_image, end_image, image_references, video_references, audio_references) / `video_edit` / `video_extension` (backward/forward). duration 4–30 s, 480p/720p/1080p, `generate_audio`, `bitrate_mode` standard/high, draft 480p finalizabil la 1080p în 7 zile (`draft_job_id`) | 1080p 5 s = 60 (12 cr/s), 15 s = 180. omni 720p 4 s = 28 (7 cr/s). Draft 480p 5 s = 15. `video_edit` ~5 s 1080p = 57 (se taxează după durata videoului de intrare) |
| GPT Image 2.5 | `gpt_image_2_5` | variant flare/sunburst, quality low/medium/high/xhigh/max, resolution 1k/2k/4k, background auto/opaque/transparent, image_references, aspect ratios inclusiv 9:16 | 1k low 0,25 · 2k medium 1 · 4k high 4,25 · 4k max 15 |

1 credit ≈ 0,04–0,06 $ (estimare).

**Ce rezultă direct din prețuri**
- Genjutsu plătește minim 44 la 1080p pentru orice clip ≤ ~4 s. Bucata ideală de mișcare are deci **3,5–4,0 s**: un clip de 2 s costă la fel ca unul de 4 s, deci lasă-i rezervă la capete și taie la montaj. Peste 4 s plătești ~11 cr/s în plus.
- Seedance 4 s la 1080p ≈ 48 cr (12 cr/s, valoare calculată, nemăsurată). Genjutsu 4 s ≈ 44. Cele două unelte costă cam la fel pe secundă, deci alegerea între ele se face după calitate și după rata de refuz, nu după preț.
- GPT Image 2.5 la 4k high costă 4,25 cr. `gpt_image_2` la 4k costa ~15 (HG:CLAUDE.md). Placa e acum de ~10× mai ieftină decât videoul, așa că merită perfecționată placa înainte de video [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8).

**Parametri obligatorii pe care i-am învățat pe pielea noastră** [confirmat]
- Seedance cu `start_image` cere `mode: "omni_reference"`. Altfel primești 422, pentru că e tratat ca t2v (HG:docs/04-lessons.md).
- Seedance: pune și `aspect_ratio: "9:16"`, și `width: 1080, height: 1920`. Doar cu width/height a ieșit 16:9 o dată. Fără `resolution: "1080p"` iese 720p (HG:docs/04-lessons.md, HG:CLAUDE.md).
- ID-urile media se dau mereu ca UUID complet. ID-urile scurte nu merg în API (HG:docs/04-lessons.md).
- Upload din Claude Code: `media_upload` → PUT pe `upload_url` → `media_confirm` (HG:docs/04-lessons.md).
- La video s-a trimis mereu `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`, care refuză presetul „IN THE DARK”. `gpt_image_2` îl ignoră (HG:CLAUDE.md, HG:docs/04-lessons.md).
- La Genjutsu, HeatGrump a trimis și `aspect_ratio`, `duration`, `bitrate_mode` (HG:engine/batches/broll18.json). Specificația de azi acceptă doar `resolution`. **[ipoteză]** Parametrii în plus sunt ignorați, iar durata și formatul vin din clipul de mișcare. Trimite doar `resolution` și verifică formatul ieșirii.

---

## 1. Modelul mental: ce ia fiecare unealtă din fiecare intrare

Principiul de bază: **fiecare intrare câștigă un lucru**. Clipul de mișcare dă mișcarea și camera. Imaginea de personaj dă fața. Imaginea de cameră dă decorul. Imaginile de produs dau produsul. Promptul arbitrează și repară scurgerile. Problemele apar când o intrare „scapă” în alt rol: părul din viral ajunge pe personajul nostru, costumul din viral declanșează filtrul IP, textul ars din viral apare în rezultat.

### 1.1 Genjutsu motion transfer (`hf_mult_motion_control`)

| Intrare | Ce copiază | Ce ignoră / unde nu ajunge | Ce poate strica | Sursa |
|---|---|---|---|---|
| **Clipul de mișcare** (`video_references`) | Mișcarea corpului, ritmul, durata, cadrajul și mișcarea camerei (de ex. B2 „C_new” filmat doar pe corp → rezultat fără față) | Sunetul: Genjutsu pune **muzică proprie** pe ieșire | **Scurgeri:** părul, hainele și textul ars din viral trec în rezultat. **Costum** (Grinch, prințesă, Albă-ca-Zăpada) sau produsul competitorului mare în cadru → `ip_detected`. **Sub 2 s** → pică fără motiv afișat | [confirmat] HG:03-rules (2 oct reel 8 păr; 2 oct C_new; 2, 3, 5 oct ip; 5 oct delogo), HG:engine/final.py r.93 (muzica), HG:library/media.json (`_rezultate` B1) |
| **Imaginea de personaj** (`image_references`, Image 1) | Fața, pielea, vârsta, constituția, genul | Părul și hainele, dacă promptul nu le fixează (le ia din viral) | Poză sub ~1080 px → clip moale | [confirmat] HG:03-rules (2 oct calitatea referințelor; 2 oct reel 8) |
| **Imaginea de cameră** (Image 2) | Pereții, mobila, decorul, culorile | Unghiul camerei, care vine din clipul de mișcare **[ipoteză, coerent cu C_new]** | Camera fără mobila de care are nevoie acțiunea: cozy „întins în pat” într-un living fără pat iese ciudat | [confirmat] HG:03-rules (2 oct cozy după tipul camerei) |
| **Imaginile de produs** (Image 3–6) | Forma, culorile, materialul | Detaliile fine cu risc de „transfer” (fața de pe glugă a migrat pe buzunare) | Prea mult produs „recognoscibil” sau protejat → `ip_detected`. La unboxing-ul Seedance, 4 referințe au fost respinse 6/6. La B2 Genjutsu, ip → 2 referințe | [confirmat] HG:03-rules (2 oct buzunare), HG:library/media.json (nota B2) |
| **Promptul** | Rolurile imaginilor (după ordine), hainele, părul, detaliile produsului, lumina, scoaterea textului | **Nu** controlează mișcarea, ritmul sau cadrajul (le dă clipul). Marcajele pe secunde sunt doar „ghidaj soft” | Regula critică pusă la coadă e respectată slab: fața pe buzunare a dispărut abia când regula a urcat **prima** în prompt | [confirmat] HG:03-rules (2 oct). [YT] primele ~20% din prompt contează [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8). HG:.claude/skills/product-video-recast/references/genjutsu-production.md (timestamp = soft) |
| **Lumina** | Vine din combinația cameră + prompt | — | Cameră întunecată → clip întunecat. Blocul „LOOK — BRIGHT, EVERYDAY UGC” e în toate B-roll-urile aprobate | [confirmat ca practică] HG:prompts/b1-motion-control.txt. [YT] lumina proastă = slop [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) |

### 1.2 Genjutsu replace_object (`hf_mult_replace_object`)

| Intrare | Ce copiază / păstrează | Ce poate strica | Sursa |
|---|---|---|---|
| Video sursă | Tot ce nu e numit ca înlocuit: mișcarea, camera, decorul, personajul | Clip scurt → **422** (B1 de ~1–3 s refuzat; clipul întreg de 15,8 s acceptat la 104 cr pe 17 sept) | [confirmat] HG:docs/memory-export-heatgrump.md r.145, HG:docs/04-lessons.md |
| Imagini (min. 1) | Aspectul obiectului / produsului / hainei / personajului nou | Produs cu altă formă decât originalul → prinderea din mână nu se mai potrivește | [YT/skill] HG:…/genjutsu-production.md („Product swaps need … the original grasp”) |
| Prompt | Ce se înlocuiește și ce rămâne | — | [ipoteză] (folosit o singură dată în HG) |

### 1.3 Seedance 2.5 (`seedance_2_5`)

| Intrare | Ce copiază | Ce poate strica | Sursa |
|---|---|---|---|
| `start_image` (omni) | **Foarte puternic** primul cadru: compoziția, identitatea, camera, lumina. Imperfecțiunile plăcii trec și ele în video | Placa proastă → video prost („80% din rezultat”) | [confirmat] toate clipurile fixe din HG pornesc din placă (HG:engine/batches/fixed_video_params.json). [YT] [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8) [Y59LwQNmRJY](https://youtu.be/Y59LwQNmRJY) |
| `image_references` | Fidelitatea obiectului: telecomanda reală, conectorul, cutia, produsul | Multe referințe de produs → `ip_detected`: 4 ref. respins 6/6, 2 ref. trec 3/4, 1 ref. sau doar cutia trec. Referința în plus „trage” cadrul spre ea | [confirmat] HG:docs/04-lessons.md, HG:prompts/unboxing-video.txt. [YT] [-scKERL7PK0](https://youtu.be/-scKERL7PK0) |
| `end_image` | Starea finală a acțiunii | — (suportat, nefolosit în HG) | HG:docs/04-lessons.md. [YT] [em66Mvt8QLc](https://youtu.be/em66Mvt8QLc) |
| `video_references` (omni) | Mișcarea și camera, dacă le ceri explicit („video 1 guides motion”) | Subiectul nu se vede întreg → nu înțelege mișcarea | [YT] [cL0RT2OA5Is](https://youtu.be/cL0RT2OA5Is) [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8) (spus pentru 2.0) |
| `audio_references` | Ritmul (mișcarea cade pe beat), lipsync, notele fredonate | — | [YT] [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs) |
| Video de intrare (`video_edit`) | Totul, minus ce ceri să schimbe | Intrare sub 4 s. Momentul cerut nu există în sursă → slop. La 1080p schimbă detalii mici | [YT] [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) [bY8RDKoBwU0](https://youtu.be/bY8RDKoBwU0) (spus pentru 2.0) |
| Prompt | Acțiunea, timpii, camera blocată, logica de stare (lumini, cutie, conector), audio-ul | Negația pentru obiecte e ignorată des. Cuvintele „crouching/kneeling” dau un fals `nsfw` | [confirmat] HG:docs/04-lessons.md. [YT] [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss) |
| `generate_audio` | Sunet diegetic descris (click-uri, foșnet) | Muzica adăugată de model nu se mai poate scoate → scrie „No music” | [confirmat] HG:prompts/controller-video.txt. [YT] [-scKERL7PK0](https://youtu.be/-scKERL7PK0) |

### 1.4 GPT Image 2.5 (`gpt_image_2_5`) — în HG s-a lucrat cu `gpt_image_2`

| Intrare | Ce copiază | Ce poate strica | Sursa |
|---|---|---|---|
| Image 1 cu „REPRODUCE ONE TO ONE” | Obiectul sau cadrul-țintă aproape identic | Dacă obiectul e descris cu **cuvinte proprii** în loc de referință, iese alt obiect (conectorul a devenit altă mufă) | [confirmat] HG:docs/memory-export-heatgrump.md r.180, HG:prompts/connector-plate.txt |
| Personaj | Fața, pielea, genul. Mâna din macro urmează personajul | Mâini cu piele închisă: mai multe încercări picate (`tb-inchis-v1/v2-pica`, `cb-inchis-v1-pica`) | [confirmat] HG:output/fixed/ (nume fișiere) |
| Cameră | Decorul. Cu instrucțiune explicită poate alege **alt unghi** al aceleiași camere („BEST ANGLE”) | Dominantă galbenă; fără regulă explicită, obiectul ajunge pe mobilă în loc de podea | [confirmat] HG:prompts/unboxing-image.txt + blocks/box-on-floor.txt. [YT] [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) |
| Prompt | Numărul de elemente (5 luminițe), starea (toate stinse), cadrajul (macro, % din cadru) | Elementul de la margine dispare (luminița de jos lipsea → s-a cerut explicit). Branduri reale pe haine (The North Face) dacă nu scrie „no logo” | [confirmat] HG:docs/memory-export-heatgrump.md r.182, HG:03-rules (2 oct) |
| Editări repetate | — | Imaginea „se înmoaie” și capătă aspect plastic | [YT] [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [-scKERL7PK0](https://youtu.be/-scKERL7PK0) |

---

## 2. Genjutsu motion transfer în detaliu

### 2.1 Alegerea clipului de mișcare
- **Acțiunea trebuie să fie în clip.** Transferul nu inventează un moment care lipsește [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ). La hook-uri, caută după **acțiune + audio**, nu după textul de pe ecran [confirmat] (HG:03-rules, 3 oct).
- **Corpul trebuie să se vadă cât cere rezultatul.** Clipul care filmează doar corpul dă rezultat fără față: B2 „C_new” → s-a trecut la „B_face” (HG:03-rules, 2 oct). Dacă vrei fața la vedere, alege un clip cu fața la vedere: dB2 9896b250 „stă cu fața la cameră” (HG:03-rules, 5 oct). [YT] „dacă nu-ți înțelege referința, nu vede destul din ea” [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).
- **Ce e în clip trebuie să existe și în camera noastră.** Mișcarea „întins în pat” merge doar în camere cu pat; pe canapea se folosește clipul de canapea (HG:03-rules, 2 oct).
- **Fără costume sau personaje protejate în clip.** Costumul de Grinch, de prințesă, gluga de Albă-ca-Zăpada și halatul cu față Grinch mare în cadru dau `ip_detected` (HG:03-rules, 2, 3 și 5 oct). Asemenea virale merg direct pe rețeta 6(b).
- **Rotește clipurile.** Același clip pe toate videourile = același video (HG:CLAUDE.md, HG:03-rules 29 sept).
- **Încearcă înainte să elimini un clip.** Un clip respins de 2 ori cu un anumit personaj poate trece cu altul → schimbă clipul doar la shot-ul acela (HG:CLAUDE.md, „Capcane”).

### 2.2 Pregătirea clipului (ffmpeg, 0 credite)
1. **Taie la tăieturile exacte ale viralului.** Uită-te întâi la primele 6 s la fps 2, apoi caută tăietura exactă la fps 10 (HG:.claude/skills/make-video/SKILL.md pas 4). Pentru hook taie **doar** partea de hook. La produse cu IP riscant, partea fără produs (HG:03-rules, 2 oct).
2. **Durata.** Fiecare bucată trebuie să aibă **≥ 2 s** [confirmat]:
   - 0,9 s și 1,7 s → au picat fără motiv (HG:CLAUDE.md).
   - 1,8 s (dublat) → **a picat**. 2,7 s (triplat) și 2,9 s (dublat) → au mers (HG:library/media.json `B1_x2._rezultate`).
   - Regula practică: **≥ 2,5 s, ideal 3,5–4,0 s** (prețul minim e același până la ~4 s, §0).
3. **Clipuri scurte → multiplicare.** Lipește clipul de 2–3 ori (concat) și taie la montaj doar prima trecere (HG:03-rules, 2 oct „B1 dublat”). Efectul secundar: la a doua trecere se vede repetiția. Cozy dublat s-a repetat la 1,7 s și „halatul arată ciudat” (HG:03-rules, 2 oct feedback reel 9), deci tăietura de montaj trebuie să cadă înainte de lipitură. Alternativa „ping-pong” (înainte + înapoi) a fost folosită la `cozy_pingpong` (HG:engine/batches/jobs-copie-DeDAprJSrPO.json). Rezultat neevaluat → **[ipoteză]**, vezi §10.
4. **Textul ars se șterge ÎNAINTE de upload.** Textul trece prin Genjutsu, așa că se aplică `ffmpeg delogo` pe zona textului (HG:03-rules, 5 oct). Excepție: dacă textul acoperă fața, `delogo` strică fața. Atunci nu folosi `delogo` și cere scoaterea textului în prompt („any text in the driving video is removed”). Așa a mers dB2f (HG:03-rules, 5 oct, Dd9h35Ly2Ca). Doar promptul nu ajunge când textul e vizibil în sursă (HG:…/genjutsu-production.md §Text handling).
5. **Upload.** `media_upload` → PUT → `media_confirm`, apoi notezi UUID-ul complet în biblioteca de clipuri.

### 2.3 Imaginile de referință: câte, care, în ce ordine
Ordinea folosită în toate joburile aprobate (HG:engine/batches/broll18.json, broll_b.json):

| Poziție | Rol | Regulă |
|---|---|---|
| Image 1 | **Personajul** | Poza exactă (Pinterest), cu latura mică ≥ 1080 px, o singură persoană, fața mare și clară (HG:03-rules 1 și 2 oct; HG:.claude/skills/new-sets/SKILL.md) |
| Image 2 | **Camera** | Luminoasă, fără oameni, fără text sau logo, cu mobila pe care o cere acțiunea |
| Image 3–6 | **Produsul** (4 ref.) | Plăcile de corp întreg merg primele, ca produsul să iasă întreg (HG:docs/memory-export r.85). Numai dacă produsul apare în shot |
| ultimul | `video_references` | Exact un clip |

- **Hook fără produs:** doar personaj + cameră, fără referințe de produs (HG:make-video pas 4; HG:prompts/hook-image-template.txt).
- **Dacă primești `ip_detected`:** reduci produsul la 2 referințe, apoi treci la următorul clip din rotație (HG:library/media.json, nota B2).
- [YT] Fiecare referință în plus „trage” cadrul spre ea, deci scoți ce nu e necesar [-scKERL7PK0](https://youtu.be/-scKERL7PK0).

### 2.4 Promptul: ce controlează și ce nu
**Controlează** [confirmat, din prompturile aprobate HG:prompts/b1-…, b2-…, cozy-…, engine/batches/broll18.json]:
- **Rolurile imaginilor, după ordine:** „Image 1 is the PERSON … Image 2 is the ROOM … Images 3-6 are THE PRODUCT”.
- **Părul, scris explicit.** Altfel îl copiază din viral (HG:03-rules, 2 oct reel 8). Formula care a mers (HG:engine/batches/sets18.json): `a young woman with long, loose, voluminous curly light-brown hair (no bun, no ponytail) … do NOT copy the hair or the face of the person in the driving video`.
- **Hainele**, într-un bloc „ABSOLUTE RULE, HIGHEST PRIORITY”: „Do NOT copy any clothing from the driving video” (HG:prompts/blocks/clothes-underneath.txt).
- **Detaliile produsului**, cu descriere pozitivă exactă. Regula care se strică urcă **prima** (HG:03-rules, 2 oct buzunare).
- **Lumina și aspectul** (blocul LOOK UGC).
- **Scoaterea textului:** „NO TEXT ANYWHERE … any text in the driving video is removed”.
- **Excepții de lumină pe tip de shot:** „Still no flash and no light source at the camera position” la cozy (HG:prompts/cozy-motion-control.txt).

**Nu controlează:**
- Mișcarea, ritmul, cadrajul și unghiul. Pentru altă mișcare, schimbi clipul, nu promptul.
- Marcajele pe secunde sunt „soft guidance” (HG:…/genjutsu-production.md).
- Nu adăuga acțiuni noi într-o sarcină de păstrare (același fișier).

### 2.5 Sunetul Genjutsu
Ieșirea vine cu muzică proprie, deci la montaj toate bucățile Genjutsu se pun pe **mute** (HG:engine/final.py r.93; HG:03-rules, 2 oct). Sunetul hook-ului s-a făcut separat: `generate_audio` din Seedance sau SFX (HG:03-rules, 5 oct). În LIMITLESS, SFX în afara celor 3 unelte cere acordul lui Szasz (`playbooks/higgsfield.md` §9). Până atunci hook-ul folosește sunetul original al viralului sau doar muzica.

### 2.6 Refuzuri și reparații

| Simptom | Cauza constatată | Reparația | Sursa |
|---|---|---|---|
| Pică fără motiv afișat | Clip < 2 s | Multiplici clipul la ≥ 2,5 s | HG:CLAUDE.md, HG:media.json |
| `ip_detected` la B-roll | Prea multe referințe de produs / produs recognoscibil | 4 → 2 ref.; apoi alt clip din rotație | HG:media.json nota B2 |
| `ip_detected` la hook din viral | Costum / personaj protejat în clip | Nu se repară în Genjutsu → rețeta 6(b) | HG:03-rules 2, 3, 5 oct |
| Refuz repetat pe un personaj (cozy) | Neclar | Schimbi clipul de mișcare sau personajul doar la shot-ul acela | HG:CLAUDE.md |
| Păr / haine din viral | Scurgere din clip | Bloc explicit pentru păr + „Do NOT copy …” | HG:03-rules 2 oct, sets18.json |
| Text din viral în rezultat | Textul ars trece | `delogo` înainte de upload | HG:03-rules 5 oct |
| Detaliu de produs mutat (față pe buzunar) | Regula e prea jos în prompt | Regula urcă prima, cu descriere pozitivă | HG:03-rules 2 oct |
| Fața lipsește | Clipul filmează doar corpul | Alt clip, cu fața la vedere | HG:03-rules 2 și 5 oct |
| Durata sau fps-ul ieșirii diferă de sursă | Comportament raportat | Măsori ieșirea (`ffprobe`) înainte de montaj | HG:…/genjutsu-production.md (Choigpt) |

**Cifre de refuz** [confirmat]: în lotul 24 (3 virale princesscomfortt refăcute 100% Genjutsu) s-au trimis ~17 joburi. 7 au fost marcate `_ip` și unul `_forma_gresita` (HG:engine/batches/jobs24.json). Pe virale cu halate sau costume, **~40% refuz**. [YT] Refuzurile (IP/NSFW) **nu se taxează** [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [DcoBYbytZp8](https://youtu.be/DcoBYbytZp8): pierzi timp, nu credite. De confirmat în tranzacții.

### 2.7 Unde merge și unde nu
- **Merge** [confirmat]: mișcări umane de corp întreg, de 2–5 s, într-o cameră obișnuită: îmbracă haina, o desface sau închide, se cuibărește pe canapea, mers, gesturi de hook. Exemple: B1, B2 și cozy din toate reel-urile 7–26, plus hook-urile lotului 18–26.
- **Nu merge / riscant** [confirmat]:
  - clipuri < 2 s;
  - virale cu costume sau personaje IP;
  - mișcări care cer mobilă inexistentă în camera noastră;
  - clipuri cu doar corpul, când vrei fața;
  - micro-acțiuni de produs cu stare logică (luminițe care urcă 1→5, mufă care intră complet). Acestea s-au făcut **pe Seedance din placă**, iar Szasz a decis: „ia-le pe ale noastre, că e mai bine” (HG:03-rules, 6 oct).
- **Viral întreg dintr-o bucată:** un clip de 15,8 s s-a rulat pe 17 sept (144 cr motion control / 104 cr replace_object). A doua zi s-a decis „NU se mai face reel-ul întreg dintr-o bucată — doar clipuri separate” (HG:docs/memory-export r.145, r.149). Motivul nu e notat. Montajul întreg poate introduce tăieturi în plus sau schimbă fundalul prea devreme (HG:…/genjutsu-production.md §Montage). Se retestează, vezi §10.

---

## 3. Genjutsu replace_object

**Când e mai bun decât motion transfer** [ipoteză, nefolosit în producție HG]:
- Clipul e deja **al nostru** (ieșire Genjutsu sau Seedance aprobată) și vrei alt produs sau altă variantă de culoare fără să refaci mișcarea. Tipic: același B-roll pentru varianta 2 a produsului.
- Shot lung (≥ ~5 s), cu mișcare bună, în care doar produsul sau haina e greșită.
- Variații de produs (`docs/02-reguli.md`, 10 oct, variații custom): același video, produsul schimbat.

**Limite**
- Refuză clipurile scurte cu **422** [confirmat]: B1 refuzat, 15,8 s acceptat (HG:docs/memory-export r.145). Pragul exact nu se știe, vezi §10.
- Cere cel puțin o imagine (HG:docs/04-lessons.md).
- Produs de altă formă sau mărime decât originalul → prinderea din mână devine nefirească. Alege virale cu produs de formă apropiată (HG:…/genjutsu-production.md).
- **Atenție: nu îl folosi pe viralul competitorului ca să schimbi doar produsul.** Personajul și camera competitorului rămân, iar asta e conținut „repurposed”. Pagina Facebook HeatGrump a primit „Your Page is no longer recommended” pentru conținut neoriginal (HG:docs/memory-export r.17). Regula LIMITLESS cere alt personaj și altă cameră (`docs/05-motorul-autonom.md`). Pe un viral, replace_object vine **după** motion transfer, nu în locul lui.
- Cost: 55 cr la 1080p ~5 s, la fel ca motion transfer. Merită doar dacă evită o rulare completă cu risc de refuz.

---

## 4. Seedance 2.5 pe moduri

### 4.1 Structura promptului (ce a mers în HG)
Ordinea din prompturile aprobate (HG:prompts/connector-video.txt, controller-video.txt, unboxing-video.txt):
1. **Blocul critic, primul, marcat „— ABSOLUTE RULE, HIGHEST PRIORITY”.** E lucrul care trebuie să iasă perfect: cadrul blocat, luminile care urcă, mufa care intră complet. Principiu validat de Szasz (HG:03-rules §Principii; HG:docs/memory-export r.33). [YT] primele ~20% contează cel mai mult [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).
2. **Blocarea obiectului:** „the connector stays EXACTLY the object shown in the start frame … never turns into a different kind of plug”.
3. **Logica de stare**, formulată ca reguli numerotabile: „EXACTLY ONE LIGHT IS LIT AT ANY MOMENT”, „ONE PRODUCT ONLY … the box is EMPTY”, „FACE RULE — NEVER COVERED”.
4. **FORBIDDEN:** lista scurtă de eșecuri văzute deja (gol rămas, tăietură la final, schimbare de tip).
5. **Timeline pe secunde:** „0.0-1.5s … 1.5-2.3s … 2.3-4.0s”, sau apăsări la „0.6s, 1.7s, 2.8s, 3.9s”.
6. **AUDIO:** sunete diegetice sincronizate („one firm plastic CLICK at the exact frame they seat”), „No voice, no music”.
7. **Coada de realism:** „Human-paced movement, correct number of fingers … Candid raw iPhone 12, film grain, no AI glow”. Fără reglaje de tip „-7 contrast, +3 exposure”, scoase la cererea lui Szasz (HG:03-rules).

**Timeline pe secunde vs. plan continuu.** Sursele YouTube se contrazic: împărțirea pe beats poate produce tăieturi [-scKERL7PK0](https://youtu.be/-scKERL7PK0), dar timpii pot fi definiți într-un single shot [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
- **La noi** [confirmat]: timeline pe secunde **+** cadru blocat declarat primul a dat clipurile fixe aprobate (telecomandă, conector, unboxing). Clipurile au trecut QA cu tăieturile cerute (HG:library/media.json `fixed_clips._taieturi`).
- Promptul de conector insistă pe „NO cut … and above all NOT at the end. THE LAST FRAME … SAME COMPOSITION AS THE FIRST FRAME”. Asta sugerează că a apărut o tăietură sau o reîncadrare la final (inferență din prompt; QA cere ultimul cadru mărit: HG:03-rules, 2 oct).
- **Regula:** timpi pe acțiune da, cuvinte de montaj („shot 2”, „cut to”) nu. Plus o propoziție explicită că ultimul cadru are aceeași compoziție.

**Cifre, nu adjective.** Secunde, numărul de apăsări, „five lights”, „three quarters of the frame height” (HG:prompts/controller-plate.txt). [YT] [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss).

**Negațiile: unde au mers și unde nu.**
- **Au mers** [confirmat]: negațiile de cameră, montaj și audio („no zoom, no cut, no music”), cu clipurile fixe aprobate drept dovadă. La fel listele FORBIDDEN de eșecuri concrete, puse după regula pozitivă.
- **Nu au ajuns singure** [confirmat]:
  - „no face on pockets” fără descriere pozitivă și fără poziția 1 în prompt (HG:03-rules, 2 oct);
  - descrierea în cuvinte a unui obiect, care a produs alt obiect (conectorul). Soluția e referința „Image 1, reproduce one to one”, nu mai multe cuvinte.
- [YT] Modelul ignoră „not” la stil și obiecte [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss). Formula: **regula pozitivă exactă întâi, apoi negațiile scurte**.

**Cuvinte-capcană** [confirmat]: „crouching/kneeling” → fals `nsfw` la unboxing. Se reformulează „bends forward” (HG:docs/04-lessons.md).

### 4.2 `omni_reference` (modul principal)
- **`start_image`** = placa GPT. Rolul trebuie scris exact `start_image` (HG:engine/batches/unbox_retry.json: `['start_image','image_references','image_references']`).
- **`image_references`, ordinea:** obiectul care trebuie să rămână identic pe prima poziție (telecomanda reală cb73364c / conectorul 2774615c), apoi produsul (1–2 ref.) (HG:engine/batches/fixed_video_params.json; HG:prompts/unboxing-video.txt).
- **Start fără referințe când e risc IP:** doar `start_image`, fără referință de produs. Așa au trecut hook-urile cu virale-costum (HG:03-rules, 2 și 5 oct). Dacă și așa refuză, refaci placa cu elementul problematic ascuns (gluga / fața) (HG:03-rules, 3 oct).
- **Escaladarea pentru `ip_detected` cu produs:** 2 ref. → 1 ref. → doar cutia sau doar start_image (HG:prompts/unboxing-video.txt, antet).
- **`end_image`:** pentru acțiuni cu punct final fix (mufa complet intrată, cutia goală). Nefolosit în HG → experiment în §10 (HG:docs/04-lessons.md).
- **`video_references` în omni:** varianta de rezervă pentru mișcare când Genjutsu refuză din cauza **produsului**, nu a costumului. Netestat, §10. Spune în prompt ce face fiecare intrare: „video 1 guides motion and camera; the images define appearance” [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).
- **Ce Seedance refuză și cum ocolești fără AI:** a refuzat raftul de magazin cu produse. Soluția a fost o apropiere lentă din placa 4k cu `ffmpeg zoompan` (HG:03-rules, 2 oct). Asta e treapta „montaj fără AI” (`docs/05-motorul-autonom.md`).
- **Setări fixe** [confirmat]: `mode: "omni_reference"`, `aspect_ratio: "9:16"`, `width: 1080`, `height: 1920`, `resolution: "1080p"`, `bitrate_mode: "high"`, `generate_audio: true`, `duration` 4–5, `declined_preset_id` (HG:engine/batches/fixed_video_params.json).

### 4.3 Audio
- `generate_audio: true` cu sunet descris diegetic: numai sunetele a căror sursă se vede mișcându-se, fără muzică, fără voce unde nu e replică (HG:docs/memory-export r.34).
- Sincronizarea pe cadru („CLICK at exactly the frame of each press”) a dat clipuri acceptate [confirmat].
- La montaj, toate bucățile în afară de hook se pun pe mute (HG:03-rules, 2 și 5 oct). **[ipoteză]** Pentru B-roll, `generate_audio: false` poate fi mai ieftin. Se verifică cu `get_cost` (§10).
- Replica hook-ului: tonul și pauzele se descriu; cuvintele grele se scriu fonetic [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc). Vocea e legată de aspectul personajului [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) (spus pentru 2.0).

### 4.4 `video_edit`: îmbunătățire peste Genjutsu [YT + ipoteză]
- **Ce face:** ia un clip existent (de ex. ieșirea Genjutsu) și schimbă doar ce ceri, păstrând restul. Prompt dovedit [YT]: „replace the character in this video with the person in this image. Keep the video one-to-one and only swap out the person” [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ).
- **Folosiri candidate la noi:**
  1. detaliu de produs greșit pe un B-roll altfel perfect;
  2. text rezidual;
  3. lumină prea întunecată;
  4. personajul derivat spre fața din viral.
- **Reguli:** intrare minimă 4 s, altfel freeze-frame pe ultimul cadru până la 4 s [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ). Prompt cu lista a ce rămâne neatins [Yte-UGhYkPQ](https://youtu.be/Yte-UGhYkPQ). Se taxează după durata videoului de intrare (~5 s 1080p = 57, C). La 1080p poate schimba detalii mici [bY8RDKoBwU0](https://youtu.be/bY8RDKoBwU0), deci verifici produsul cadru cu cadru.
- **Merită?** Costă cât o rulare Genjutsu nouă (55). Merită doar dacă rulările noi repetă același defect. Prima evaluare se face în §10.

### 4.5 `video_extension`
Prelungește înainte sau înapoi păstrând fața, hainele și atmosfera, fără start frame nou [pThgGdlO58I](https://youtu.be/pThgGdlO58I). La noi rezolvă cazul „audio-ul / ritmul cere 1–2 s în plus”, în locul buclei la montaj (HG:03-rules, 3 oct, bucla audio) **[ipoteză]**. Costul se măsoară cu `get_cost` înainte.

### 4.6 Draft 480p → 1080p
Draft 480p 5 s = 15 cr, finalizabil la 1080p în 7 zile cu `draft_job_id` (C). Mișcarea și compoziția se validează pe draft, apoi se finalizează doar drafturile care trec. **[ipoteză]** Finalizarea păstrează take-ul (asta spune specificația). Costul finalizării se măsoară la primul lot (§10).

---

## 5. GPT Image 2.5

### 5.1 Placa de start 9:16 (pentru Seedance)
- **Setări de producție:** `gpt_image_2_5`, `aspect_ratio "9:16"`, `resolution "4k"`, `quality "high"` (4,25 cr). În HG: `gpt_image_2`, 9:16, high, 4k, cu medias pe rol `image` (HG:engine/batches/plates13.json). Pentru 2.5 se folosește `image_references` conform specificației; verifică rolul acceptat la primul apel.
- **Imaginea trebuie să fie deja 9:16**, altfel apar benzi negre [FSQ_IIIbtVI](https://youtu.be/FSQ_IIIbtVI).
- **Ordinea referințelor** = ordinea importanței:
  - ținta de reprodus întâi: placa aprobată sau obiectul real;
  - apoi personajul, camera, produsul (HG:prompts/connector-plate.txt: `1 approved frame, 2 obiect, 3 personaj, 4 cameră, 5-8 produs`);
  - la scene cu personaj: `@Image 1 = personaj, @Image 2 = cutie/produs, @Image 3 = cameră` (HG:prompts/unboxing-image.txt).
- **Regulile de poziționare se scriu ca bloc ABSOLUTE RULE:** „THE BOX IS ON THE FLOOR … its shadow and contact with the floor must be visible” (HG:prompts/blocks/box-on-floor.txt).
- **Camera „BEST ANGLE”:** aceeași cameră, dar „choose the BEST camera angle of this room …” dă cadre mai bune decât copia poziției din poză (HG:prompts/unboxing-image.txt). Pentru reproducerea unui viral cerem în schimb unghiul cadrului din viral (șablonul 7.4).
- **Lumina:** blocul `light-ultra-real` (o sursă motivată, umbre de contact, pori, „vivid, slightly warm colours — not golden, not orange”) (HG:prompts/blocks/light-ultra-real.txt). [YT] GPT trage spre galben [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ). [YT] Unghi 3/4, nu frontal [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc).
- **„Clean your plate”:** fără text, fără obiecte care plutesc, puțină recuzită [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA). Pe haine: „no logo, no brand” (HG:03-rules, 2 oct, The North Face).
- **Starea inițială corectă** pentru ce urmează în video: toate luminițele stinse, jumătățile de mufă cu gol între ele, mâinile în cutie și produsul ascuns (HG:prompts/controller-plate.txt, connector-plate.txt, unboxing-image.txt).

### 5.2 „Reproduce one to one”: cum se cere
Formula care a mers [confirmat] (HG:prompts/connector-plate.txt; HG:docs/heatgrump-grinch-reel-spec.md „Promptul universal de swap”):
1. Primul bloc: `REPRODUCE IMAGE 1 ONE TO ONE — ABSOLUTE RULE, HIGHEST PRIORITY`, cu enumerarea a ce rămâne identic (formă, proporții, culoare, nervuri, cablu).
2. `Do NOT redesign it … do NOT add …`, cu lista exactă a invențiilor tipice.
3. `If a detail is unclear, copy Image 1 rather than inventing anything.`
4. `WHAT CHANGES compared to Image 1:` — **listă numerotată** cu exact ce se schimbă: mâna = personajul X, cadrul mai strâns, fundalul.
5. `Everything else … stays as in Image 1.`

Nu descrie obiectul cu cuvinte proprii. Descrierea inventată (pini, găuri) a produs altă mufă (HG:docs/memory-export r.180).

### 5.3 Character sheet
Regula în vigoare: personajul și camera = **poza exactă** de pe Pinterest. Nu se generează personaje „inspirate” (HG:03-rules, 1 oct). Un character sheet din aceeași poză (fundal gri, close-up + corp întreg, o singură față) e recomandat de YouTube [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ). La noi nu e testat și ar putea fi considerat „generat” → doar ca experiment, cu acordul lui Szasz (§10).

### 5.4 Planșa de produs multi-unghi
- Din pozele reale ale produsului, niciodată inventate (HG:docs/memory-export r.23). Unghiuri: față, 3/4, spate, sus, detaliu, plus interior dacă are [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
- **Plăcile de corp întreg (produsul întreg) merg primele** în lista de referințe (HG:docs/memory-export r.85).
- Fundal gri neutru [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA); cere volum, umbre de contact, reflexii (prop sheet-ul GPT iese plat) [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s).
- Modificarea care trebuie să se propage peste tot (de ex. „buzunarul mai mare”) se face **în referința de produs**, nu în fiecare prompt (HG:docs/memory-export r.49).
- Produsul „nu driftează”: aceleași referințe la toate generările. Referințele validate nu se înlocuiesc cu „ceva asemănător” (HG:03-rules; HG:docs/memory-export r.30, r.36).

### 5.5 Obiect sau cutie pe podea, macro cu mână
- Cutia: blocul box-on-floor + „The person bends forward … to reach into it” (HG:prompts/blocks/box-on-floor.txt).
- Macro cu mână: „the ONLY part of the [garment] that appears is …”, fundalul „centimetres behind the hands” în bokeh, „five fingers, natural anatomy”, „whole object … never cropped” (HG:prompts/controller-plate.txt).
- Numără explicit elementele de la margine: luminița de jos a lipsit până când s-a cerut (HG:docs/memory-export r.182).
- Variantă pentru alt ton de piele: „placa = placa aprobată (Image 1), doar mâna schimbată” (HG:03-rules, 2 oct feedback reel 10).

### 5.6 Degradarea la editări repetate
Fiecare editare înmoaie imaginea [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ). **Regula:** maxim 1–2 editări pe aceeași imagine. După aceea regenerezi de la zero, cu promptul complet, din referințele originale [-scKERL7PK0](https://youtu.be/-scKERL7PK0). În HG, plăcile noi s-au făcut mereu din placa **aprobată** + referințele originale, nu din editări în lanț (HG:prompts/connector-plate.txt).

### 5.7 Calitate: teste vs. final
| Scop | Setare | Cost |
|---|---|---|
| Explorare compoziție, unghi, culori (mai multe variante) | 1k low | 0,25 |
| Verificare detalii (mâini, număr de elemente, text) | 2k medium | 1 |
| Placă finală pentru Seedance / planșă produs | 4k high | 4,25 |
| Doar planșa master de produs, dacă high pierde detalii | 4k max | 15 |

**[ipoteză]** Seedance iese la 1080p, deci o placă 4k high ar putea fi peste necesar. Comparația 2k medium vs. 4k high ca start_image e în §10. Flare vs. sunburst: necunoscut, §10.

---

## 6. Rețete complete

Notație: `P` = personaj (Pinterest, ≥1080 px), `R` = camera, `PR1..4` = referințe de produs, `D` = clipul de mișcare (bucata din viral). Costuri la 1080p.

### (a) Viral refăcut FULL GENJUTSU (regula de pornire, `docs/02-reguli.md` 10 oct)
1. **Analiză (0 cr).** Descarci viralul și găsești tăieturile (scene detect + fps 10 în jurul lor). Faci harta shot-urilor: durată, acțiune, produs vizibil da/nu, costum / brand / text ars, mobila necesară (HG:make-video pas 4; HG:…/genjutsu-production.md §Source).
2. **Triere pe shot:**
   - costum / personaj IP / produsul competitorului dominant → marchezi pentru rețeta (b);
   - shot static / detaliu → treapta „montaj fără AI”;
   - restul → Genjutsu.
3. **Pregătirea clipurilor (0 cr), §2.2:**
   - tai la tăieturile exacte;
   - < 2 s → ×2/×3 până la ≥ 2,5 s;
   - 2–4 s → rămâne așa, ideal cu rezervă până la ~4 s;
   - 4–5 s → OK (55 cr);
   - > 5 s → tai la un punct natural;
   - `delogo` pe text (cu excepția textului pe față);
   - upload, UUID.
4. **Setul:** P + R din rotație (o pereche nefolosită pe acest concept). Hainele de dedesubt și părul se aleg și se scriu o dată pentru tot videoul (HG:engine/batches/sets18.json).
5. **Joburi (în paralel, un job pe shot):**
   ```
   model: hf_mult_motion_control
   params: { resolution: "1080p" }
   medias: [ {P, image_references}, {R, image_references},
             {PR1..PR4, image_references}   # doar dacă produsul e în shot
             {D, video_references} ]         # exact unul
   prompt: șablonul 7.1 (cu produs) sau 7.2 (fără produs)
   ```
6. **QA (§9.1).** Pică → încă o rulare cu același prompt dacă e „roll prost”, sau reparația din §2.6 dacă e eșec sistematic. Maxim 3 încercări, apoi (b).
7. **Montaj:** tai prima trecere la clipurile multiplicate, pui Genjutsu pe mute, măsori durata cu `ffprobe`.
8. **Cost tipic:** viral de 15 s în 4 shot-uri ≈ 2×44 + 2×55 = **~200 cr** (8–12 $). Estimarea din HG pentru hook + B1 + B2 + cozy în Genjutsu 1080p era ~190 cr/reel, ~200–240 cu reîncercări (HG:docs/plan-reels-18-22.md).

### (b) Viral unde Genjutsu e respins → placă GPT Image 2.5 + Seedance omni
1. **Diagnostic întâi** (refuzurile nu se taxează [YT]):
   - dacă ai trimis referințe de produs → reîncerci o dată cu 1–2;
   - dacă clipul are costum sau personaj IP → treci direct la pasul 2 (HG:03-rules, 2, 3 și 5 oct).
2. **Cadrul-țintă:** extragi cadrul de start al shot-ului din viral (frame 0 al bucății).
3. **Placa (4,25 cr):**
   ```
   model: gpt_image_2_5, aspect_ratio 9:16, resolution 4k, quality high
   image_references: [cadru viral (compoziție), P, R, PR1 (opțional; 0 dacă IP)]
   prompt: șablonul 7.4
   ```
   - Explorare ieftină înainte, dacă unghiul e incert: 2–3 variante la 1k low (0,75 cr total).
   - Dacă GPT refuză din cauza cadrului viral → scoți cadrul și descrii compoziția în cifre (% din cadru, înălțimea camerei).
4. **Video (draft opțional 15 cr → finalizare; altfel ~48–60 cr):**
   ```
   model: seedance_2_5, mode: omni_reference
   medias: [ {placa, start_image}, {PR1, image_references}? ]   # 0 ref. dacă IP
   aspect_ratio "9:16", width 1080, height 1920, resolution "1080p",
   bitrate_mode "high", generate_audio true, duration 4|5,
   declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
   prompt: șablonul 7.5 (acțiunea viralului pe secunde)
   ```
5. **Dacă Seedance refuză:**
   - refaci placa cu elementul problematic ascuns (HG:03-rules, 3 oct);
   - dacă refuză tot → apropiere lentă din placă cu `ffmpeg zoompan` (HG:03-rules, 2 oct).
6. **Cost:** ~55–65 cr/shot (placă + video), adică cam cât Genjutsu.

### (c) Schimbi doar produsul într-un clip (`replace_object`)
- **Folosire corectă:** pe un clip deja refăcut de noi (P + R ai noștri), ca să pui alt produs sau altă variantă. Nu pe viralul brut al competitorului (§3).
- **Pași:**
  1. clipul ≥ ~5 s (sub prag → 422; pragul se determină în §10);
  2. upload;
  3. `model: hf_mult_replace_object`, `resolution: "1080p"`, medias: clipul sursă + 1–4 imagini cu produsul nou (cel puțin una);
  4. prompt: șablonul 7.3;
  5. QA §9.2 (forma, prinderea, eticheta).
- **Cost:** 55 cr la ~5 s.

### (d) Îmbunătățire cu Seedance `video_edit`
- **Când:** clip Genjutsu cu mișcare și identitate bune, dar cu **un** defect local: detaliu de produs, text rezidual, lumină. Două rulări Genjutsu noi au repetat defectul.
- **Pași:**
  1. intrarea ≥ 4 s (freeze-frame dacă e mai scurtă);
  2. `seedance_2_5`, `mode: video_edit`, intrarea = clipul, `image_references` = PR1–2 (sau P);
  3. aceleași setări fixe 9:16 / 1080p / high;
  4. prompt: șablonul 7.6.
- **QA:** compari cadru cu cadru cu intrarea. Nimic altceva nu trebuie să se fi schimbat [bY8RDKoBwU0](https://youtu.be/bY8RDKoBwU0).
- **Cost:** ~57 cr / 5 s de intrare. Dacă nu repară din prima, renunți (nu repeți).

### (e) Test ieftin de mișcare la 480p înainte de 1080p
- **Genjutsu:** același job ca la (a), cu `resolution: "480p"` (~15 cr / 5 s).
  - **Validează:** acceptarea clipului (fără refuz), transferul mișcării, scurgerile de păr / haine / text, forma produsului în mare.
  - **Nu validează:** fața și detaliile fine. Rularea la 1080p e o **generare nouă**, nu o mărire, deci poate ieși diferit (HG:…/genjutsu-production.md §Cost and execution).
  - Merită pentru **clipuri noi** (primul viral al unui produs, tip nou de mișcare). Nu merită pentru clipuri deja aprobate în bibliotecă. Testul (15) se justifică dacă probabilitatea ca rularea la 1080p să pice e peste ~27% (15/55).
- **Seedance:** draft 480p (15 cr / 5 s) → dacă trece QA de mișcare, finalizare la 1080p cu `draft_job_id` (≤ 7 zile). Aici take-ul se păstrează [ipoteză, din specificație].
- **GPT:** variantele de compoziție la 1k low (0,25), finalul la 4k high.

---

## 7. Șabloane de prompt (EN, cu [INSERT ...])

Derivate din prompturile aprobate HG. Ordinea blocurilor contează: regula care se strică cel mai des urcă prima.

### 7.1 Genjutsu motion transfer — shot cu produs
(din HG:prompts/b1-motion-control.txt + engine/batches/broll18.json)
```
[INSERT SHOT NAME, e.g. "PUTTING THE PRODUCT ON"]. Transfer the movement and camera work from the driving video onto the subject in the reference images.

[INSERT THE ONE RULE THAT FAILED LAST TIME, if any — ABSOLUTE RULE, HIGHEST PRIORITY]

LOOK — BRIGHT, EVERYDAY UGC: a normal person filming on their own phone in a well-lit room. Bright, evenly lit, colours clearly readable, no dark corners, no moody grade, no orange tint, no vignette. Ordinary phone sharpness.

IMAGE ROLES: Image 1 is the PERSON — [INSERT HAIR: e.g. "a young woman with long, loose, wavy chestnut-brown hair (no bun, no ponytail)"]; face, hair, skin tone, age, build and gender exactly as in Image 1 in every frame, do NOT copy the hair or the face of the person in the driving video. Image 2 is the ROOM — same walls, furniture and decor. Images 3-[N] are THE PRODUCT.

CLOTHES — ABSOLUTE RULE: they wear [INSERT OUTFIT: colour, type, length, socks/shoes] — the same in every clip of this video. Do NOT copy any clothing from the driving video.

THE PRODUCT, identical to the reference images in every frame: [INSERT POSITIVE, EXACT DESCRIPTION: colours, materials, parts, where each print/logo is and is NOT]. [INSERT SIZE: "about [X] cm, in true proportion to the hands"]. The product must not drift between frames. [INSERT "visible in full, never cropped" if relevant]

Vertical 9:16. NO TEXT ANYWHERE: no captions, no burned-in text, no emoji, no watermarks — any text in the driving video is removed.
```

### 7.2 Genjutsu motion transfer — hook fără produs
```
HOOK — [INSERT ACTION IN ONE LINE, e.g. "she shivers under a blanket and turns the thermostat up"]. Transfer the movement and camera work from the driving video onto the subject in the reference images.

IMAGE ROLES: Image 1 is the PERSON — [INSERT HAIR]; face, hair, skin tone, age, build and gender exactly as in Image 1, do NOT copy the hair, face or clothing of the person in the driving video. Image 2 is the ROOM — same walls, furniture and decor; [INSERT THE FURNITURE THE ACTION NEEDS, e.g. "the sofa from Image 2"].

CLOTHES — ABSOLUTE RULE: [INSERT OUTFIT], no logos, no brand names.

NO PRODUCT: no [INSERT PRODUCT CATEGORY] anywhere in the frame. [INSERT ANY PROP FROM THE VIRAL that must stay, described plainly, no brands]

LOOK: [INSERT prompts/blocks/light-ultra-real.txt adapted: one motivated light, vivid slightly warm colours, not golden, not orange].

Vertical 9:16. NO TEXT ANYWHERE — any text in the driving video is removed.
```

### 7.3 Genjutsu replace_object
```
Replace ONLY the [INSERT OBJECT, e.g. "robe the woman is wearing"] in the source video with the product from the reference images. Keep everything else one to one: the person, face, hair, clothing underneath, gestures, timing, camera framing and movement, room, lighting.

THE NEW PRODUCT, exactly as in the reference images: [INSERT POSITIVE EXACT DESCRIPTION + SIZE]. It sits on the body / in the hands exactly where the old one was, with the same folds, grip and contact, and moves with the same physics. Use the product from the attached images exactly as shown. Preserve its shape, design and proportions. Do not redesign it.

No other change. No text, no logos, no watermarks. Vertical 9:16.
```
(fraza de blocare din [fmgVm-fxPDM](https://youtu.be/fmgVm-fxPDM))

### 7.4 GPT Image 2.5 — placă de start după cadrul din viral
(din promptul universal de swap, HG:docs/heatgrump-grinch-reel-spec.md, și HG:prompts/connector-plate.txt)
```
REPRODUCE THE COMPOSITION OF IMAGE 1 — ABSOLUTE RULE, HIGHEST PRIORITY. Image 1 is the target frame: keep the same camera height, distance and angle, the same framing (the person at [INSERT % position] of the frame, [INSERT "full body" / "waist up"]), the same pose and hand positions, the same action moment.

WHAT CHANGES compared to Image 1:
1. The PERSON is the person from Image 2 — identical face, skin tone, hair ([INSERT HAIR]), age, build and gender. Natural skin texture, correct hands with five fingers.
2. The ROOM is the room from Image 3 — same walls, furniture, floor, decor and colours, seen from the camera position of Image 1. [INSERT FURNITURE THE ACTION NEEDS]
3. They wear [INSERT OUTFIT], no logos, no brand names.
4. [IF PRODUCT IN SHOT] The product is the product from Image 4, reproduced one to one — same shape, colours, materials and proportions, at true real-world size ([INSERT cm]). Do not redesign it. [IF NOT] No product in the frame.

STATE AT THIS MOMENT: [INSERT EXACT START STATE, e.g. "box open on the floor, hands inside, product still hidden"; "all lights OFF"].

[INSERT prompts/blocks/light-ultra-real.txt]

Everything else stays as in Image 1. Vertical 9:16. Candid phone photo. No text, no readable writing, no logos, no watermarks.
```

### 7.5 Seedance 2.5 omni_reference — din placă
(din HG:prompts/connector-video.txt, unboxing-video.txt, controller-video.txt)
```
ONE SINGLE SHOT, FRAME LOCKED — ABSOLUTE RULE, HIGHEST PRIORITY: [INSERT "static phone propped at chest height" / "handheld with tiny natural micro-shake"], one continuous take for the whole [INSERT 4|5] seconds. No cut, no second shot, no zoom, no push-in, no pull-out, no re-frame, above all not at the end. The last frame has the same composition as the first.

[INSERT THE CRITICAL OUTCOME as its own ABSOLUTE RULE, positive and exact, e.g. "THE TWO HALVES GO INTO EACH OTHER COMPLETELY … ZERO gap" / "EXACTLY ONE LIGHT IS LIT AT ANY MOMENT"]

THE [INSERT OBJECT] stays EXACTLY the object in the start frame and in Image 1 in every frame — same shape, colour, size relative to the hands. Nothing morphs, nothing new appears.

Identity, outfit, room and lighting stay exactly as in the start frame.

ACTION TIMELINE:
0.0–[t1]s — [INSERT physical action: weight, inertia, where it lands]
[t1]–[t2]s — [INSERT]
[t2]–[end]s — [INSERT end state, held still until the clip ends]

FORBIDDEN: [INSERT the 3–5 failures already seen on this shot, concrete].

AUDIO: [INSERT diegetic sounds synced to the action, e.g. "one soft CLICK at the exact frame …"]. Quiet room tone. No voice[INSERT unless a line], no music.

Human-paced movement, correct number of fingers, no extra limbs, no morphing. Candid raw iPhone, film grain, no AI glow, no smoothing. No text overlays, no watermark.
```

### 7.6 Seedance 2.5 video_edit — reparare locală
```
Keep this video one to one: the same person, face, hair, clothing, gestures, timing, camera framing and movement, room and lighting — frame for frame.

CHANGE ONLY: [INSERT ONE LOCAL FIX, positive and exact, e.g. "the two front pockets become plain [colour] fabric with a white trim band, nothing printed on them" / "remove the floating caption text in the top third"]. [IF PRODUCT] The product matches the reference image exactly — same shape, design and proportions; do not redesign it.

Nothing else changes. No text, no logos, no music. Vertical 9:16.
```

### 7.7 GPT Image 2.5 — planșă produs multi-unghi
```
Make a product sheet of the product from Image 1 (and Images 2-[N], the same product from other angles): [INSERT views: front, 3/4, back, top, detail of [part], interior] on a plain neutral grey background, each view sharp, at the same scale. Reproduce it one to one — same shape, colours, materials, seams and proportions; do not redesign it, do not add any logo, print or part that is not in the references. Real volume: soft contact shadows, true material texture and reflections. No text, no labels, no watermarks.
```

---

## 8. Arborele de decizie (Planificator)

```
VIRAL ──► harta shot-urilor (tăieturi, durate, produs?, costum/brand/text?, mobilă necesară)
   │
   ├─ shot are un clip APROBAT în bibliotecă (același rol + produs)? ─► REFOLOSEȘTE (0 cr)
   ├─ shot static / detaliu fără mișcare umană? ───────────────────► ffmpeg din placă/clip (0 cr)
   ├─ shot cu costum / personaj IP / produs competitor dominant? ──► rețeta (b) direct
   ├─ shot = micro-acțiune de produs cu stare logică (lumini, mufă, ecran)? ─► (b), 0–1 ref. obiect
   └─ altfel ─► GENJUTSU (a)
         │
         ├─ clip nou pentru biblioteca noastră / primul viral al produsului? ─► test 480p (e), 15 cr
         │        └─ trece ─► 1080p
         ├─ durată: <2 s ×2/×3 ; ≤4 s = 44 cr ; ~5 s = 55 cr ; >5 s taie
         ├─ refuz ip_detected:
         │        ├─ am trimis ref. produs? ─► 4→2→1 ref., o dată
         │        └─ altfel / tot refuz ─► (b)
         ├─ QA pică:
         │        ├─ detaliu local, mișcare ok ─► re-rulează ACELAȘI prompt (o dată)
         │        ├─ același defect de 2 ori ─► repară promptul (regula urcă prima) SAU (d) video_edit
         │        └─ 3 eșecuri ─► (b)
         └─ (b) pică de 3 ori ─► ffmpeg din placă sau shot scos/înlocuit la montaj
```

**Rezoluție:** producția se face la 1080p (Genjutsu, Seedance). Testele la 480p, numai la clipuri noi. 720p nu se folosește: costă 35 vs. 55, dar nu e nici test, nici final.

**Câte variante pe shot** (HG:CLAUDE.md §QA):
- hook nou (adaptat sau creativ): **2 variante**, se alege cea mai bună;
- hook dovedit și B-roll: **1**, plus reîncercări la QA;
- plăci GPT: 2–3 variante la 1k low pentru unghi, apoi **1** la 4k high.

**Când urci treapta:**
- după 3 eșecuri QA pe aceeași treaptă (`docs/05-motorul-autonom.md`);
- imediat, la `ip_detected` din cauza clipului (costum);
- niciodată pentru un singur take ciudat. Mai întâi re-rulezi [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss).

**Buget maxim per video** [propunere, de calibrat cu cifre]:
- **țintă ~200 cr** (viral de 15–18 s, full Genjutsu);
- **plafon tare 300 cr** (~12–18 $), reîncercările incluse;
- la plafon: Producătorul se oprește, livrează ce a trecut QA și marchează shot-urile lipsă.

Referință HG: un reel complet cu toate clipurile generate ≈ 400 cr + hook-uri (HG:docs/04-lessons.md). Lotul 18–22 a fost estimat la ~190 cr/reel (HG:docs/plan-reels-18-22.md). Se urmărește **credite / secundă acceptată** pe unealtă și tip de shot, iar scara se reordonează după cifre (`docs/05-motorul-autonom.md`).

---

## 9. Lista de verificare QA pe unealtă

Pentru video extragi cadre la 0/20/40/60/80/100% plus **ultimul cadru mărit** (HG:.claude/skills/qa-check/SKILL.md; HG:03-rules, 2 oct). La tăieturi compari câteva cadre de o parte și de alta (HG:…/genjutsu-production.md §Review).

### 9.1 Genjutsu motion transfer
- [ ] **Format:** 9:16, durata și fps-ul ieșirii măsurate cu `ffprobe` (pot diferi de sursă).
- [ ] **Fața = Image 1**, nu fața din viral. Se verifică separat de haine.
- [ ] **Părul = cel scris**, nu cel din viral (coc, coadă, păr lung „furat”).
- [ ] **Hainele = cele scrise**, nu cele din viral.
- [ ] **Camera = Image 2** (mobila, pereții), iar mobila cerută de acțiune există.
- [ ] **Fața se vede** acolo unde trebuie (clipurile filmate doar pe corp o taie).
- [ ] **Produs:** forma, culorile, printurile numai unde trebuie (fără migrare pe alte părți), întreg dacă se cere, nu se schimbă între cadre.
- [ ] **Fără text rezidual** sau litere inventate în zona unde era textul din viral.
- [ ] **Fără repetiție vizibilă** la clipurile multiplicate în partea folosită la montaj.
- [ ] **Audio:** muzică Genjutsu → mute la montaj.

### 9.2 Genjutsu replace_object
- [ ] Doar obiectul cerut s-a schimbat; personajul, mișcarea și camera sunt identice cu sursa.
- [ ] Prinderea și contactul arată fizic (mâna nu trece prin produs), mărimea e constantă.
- [ ] Etichete și printuri corecte, fără text inventat.

### 9.3 Seedance 2.5 (omni / edit / extension)
- [ ] **9:16 și 1080p reale** (nu 16:9 / 720p din parametri lipsă).
- [ ] **Fără tăietură sau reîncadrare**, mai ales la final. Ultimul cadru are aceeași compoziție ca primul.
- [ ] **Obiectul nu se transformă** (alt tip de mufă, altă formă, etichete care se schimbă).
- [ ] **Logica de stare:** numărul de elemente (de ex. 5 luminițe), o singură lumină aprinsă, ordinea 1→N, acțiunea dusă **complet** (mufa complet intrată, fără gol), cutia se golește, un singur produs.
- [ ] **Fața nu e acoperită** de produs (s-a întâmplat: `unboxing-v1-fata-acoperita`, HG:output/reel18/).
- [ ] **Identitate, haine, cameră, lumină** = placa de start.
- [ ] **Mâini:** 5 degete, gen și piele = personajul.
- [ ] **Audio:** sunetele sincronizate pe acțiune, fără muzică, fără voce nedorită.
- [ ] **video_edit:** nimic în afara zonei cerute nu s-a schimbat, comparat cadru cu cadru cu intrarea.

### 9.4 GPT Image 2.5
- [ ] **9:16 nativ**, rezoluția cerută.
- [ ] **Obiectul de reprodus = Image 1:** aceeași formă, același număr de elemente (numărate), nimic adăugat.
- [ ] **Starea inițială corectă** (lumini stinse, gol între jumătăți, produs ascuns în cutie).
- [ ] **Poziția:** obiectul pe podea / pe suprafața cerută, cu umbră de contact.
- [ ] **Persoana = referința;** mâinile anatomic corecte; tonul pielii potrivit.
- [ ] **Fără branduri sau logo pe haine,** fără text în imagine.
- [ ] **Lumina:** o sursă motivată, fără dominantă galbenă sau portocalie, fără „AI glow” sau piele de plastic.
- [ ] **Imaginea nu e „înmuiată”** (dacă e rezultatul a 2+ editări, regenerezi).

---

## 10. Experimente de făcut la primul produs

Ce nu știm sigur. Fiecare test are o singură variabilă și un cost mic. Rezultatul (cifra) se trece înapoi aici și în `config/costs.json`.

| # | Întrebarea | Cum testăm | Cost estimat | Decizia pe care o schimbă |
|---|---|---|---|---|
| 1 | **Un singur Genjutsu de 15 s vs. 3×5 s?** (HG a renunțat la 15,8 s întreg pe 17 sept, fără motiv notat) | Același viral, același P + R + prompt: o rulare pe tot clipul vs. 3 bucăți, ambele la **480p**. Comparăm identitatea pe toată durata, tăieturile în plus, schimbarea timpurie a fundalului, timpul de montaj | ~45 + ~45 cr (480p) | Dacă bucata lungă trece QA, ne scutește de montajul pe bucăți și de clipurile < 2 s |
| 2 | **Este 480p predictiv pentru 1080p?** | 5 clipuri: 480p și apoi 1080p, același input. Notăm câte verdicte QA coincid | 5×(15+55) = 350 cr (folosim clipurile oricum) | Dacă < 4/5 coincid, testul 480p rămâne doar pentru refuzuri și scurgeri, nu pentru calitate |
| 3 | **Clipuri < 2 s: dublare vs. ping-pong vs. încetinire** | Același clip de 1,5 s pregătit în 3 feluri, Genjutsu 480p | 3×~12–15 cr | Metoda standard din §2.2 |
| 4 | **Câte referințe de produs în Genjutsu: 1 / 2 / 4?** | Același shot cu produs, 3 rulări la 1080p | 3×44 = 132 cr | Numărul implicit de referințe (fidelitate vs. rata `ip_detected`) |
| 5 | **GPT Image 2.5: flare vs. sunburst** | Același prompt de placă (7.4), 3 variante din fiecare la 2k medium. Notăm realismul pielii, dominanta, fidelitatea produsului | 6×1 = 6 cr | Varianta implicită |
| 6 | **Calitatea plăcii contează în Seedance?** | Aceeași placă la 2k medium și la 4k high, apoi Seedance draft 480p din fiecare. Comparăm (după finalizare) detaliile produsului | 1 + 4,25 + 2×15 (+ finalizare) | Dacă 2k medium e echivalent → economie la fiecare placă |
| 7 | **Draft Seedance 480p → finalizare 1080p: cost și identitate** | 2 drafturi finalizate. Măsurăm costul finalizării și dacă take-ul rămâne identic | 2×15 + finalizare | Dacă draft + finalizare < 60 și take-ul se păstrează → toate shot-urile Seedance trec prin draft |
| 8 | **Merită `video_edit` peste Genjutsu?** | 2 clipuri Genjutsu cu un defect local (produs / text). `video_edit` vs. o rulare Genjutsu nouă | 2×57 + 2×44 | Dacă repară fără drift → intră în scară ca reparație locală |
| 9 | **`end_image` la acțiuni cu final fix** (mufa intrată, cutia goală) | Placa de start + placa de final (GPT, 2 plăci) vs. doar start, Seedance draft | ~9 + 2×15 cr | Rata de „acțiune dusă complet” la clipurile de produs |
| 10 | **Seedance omni cu `video_references` = bucata din viral** ca rezervă când Genjutsu refuză din cauza produsului | 2 shot-uri refuzate de Genjutsu → placă + Seedance cu vs. fără video_references | ~2×(4,25 + 2×15) | Dacă mișcarea se transferă → rețeta (b) păstrează mișcarea viralului |
| 11 | **Pragul de 422 la `replace_object`** | Același clip tăiat la 3 / 4 / 5 / 6 s (refuzurile nu ar trebui taxate) | ~0–55 cr | Durata minimă pentru rețeta (c) |
| 12 | **Character sheet din poza Pinterest vs. poza brută în Genjutsu** (doar cu acordul lui Szasz, §5.3) | Același shot, P = poză brută vs. sheet gri (față + corp, o singură față) | ~4 + 2×44 cr | Stabilitatea feței la personaje cu poză mai slabă |
| 13 | **`generate_audio: false` reduce prețul la Seedance?** | Doar `get_cost`, fără generare | 0 | Pentru B-roll (care se pune pe mute), dacă e mai ieftin |
| 14 | **Refuzurile chiar nu se taxează?** | Comparăm `transactions` cu joburile `ip_detected` din primul lot | 0 | Dacă se taxează, testul 480p devine obligatoriu pe clipurile riscante |

**Prioritate la primul produs:**
- obligatoriu: **14, 13, 5, 7, 1, 4** (ieftine, schimbă rețeta standard);
- după primele 10 videouri: **2, 6, 8, 9, 10**;
- la nevoie: **3, 11, 12**.
