# Higgsfield — manual de lucru (Genjutsu · Seedance 2.5 · GPT Image 2.5)

Sursa: canalul YouTube oficial Higgsfield (notițe în `library/sources/higgsfield-yt/notes-part1…5.md`), experiența noastră din HeatGrump (`heatgrump/CLAUDE.md`, sept–oct 2026) și tranzacțiile reale din contul nostru (9 oct 2026, plan „scale”). Data: 10 oct 2026.
Pentru: agenții care reproduc videouri de produs virale (alt personaj, altă cameră), ultra-realist, la cost minim.

**Regula de bază (Szasz, 10 oct):** în producție folosim EXCLUSIV `hf_mult_motion_control` (Genjutsu), `seedance_2_5` (Seedance 2.5) și `gpt_image_2_5` (GPT Image 2.5). Sfaturile din video spuse pentru Seedance 2.0 / GPT Image 2 sunt aplicate la versiunile noastre și marcate „(spus pentru …)”. Ce e marcat **ipoteză** nu are încă cifră de la noi: se testează și se trece cifra aici.

**Costuri reale (tranzacții 9 oct 2026):**

| Unealtă | Credite | ≈ $ (1 credit ≈ 0,04–0,06 $ [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M)) |
|---|---|---|
| Genjutsu | 28 / 44 / 55 / 66 per clip (variază cu durata/rezoluția; 44 la 1080p ~4 s) | 1,1–4 $ |
| Seedance 2.5 | 35 (clip scurt) | 1,4–2,1 $ |
| GPT Image 2 | 6,5 sau 11 per imagine (GPT Image 2.5: de citit din primele tranzacții) | 0,26–0,66 $ |
| Efecte sonore | < 1,5 | < 0,1 $ |

---

## 1. Cele 10 reguli de aur

1. **Imaginea de start face rezultatul.** „Start frame-ul face 80% din rezultat”, garbage in = garbage out; Seedance copiază în video imperfecțiunile imaginii → perfecționezi placa (ieftină) înainte de video (scump) [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8) [Y59LwQNmRJY](https://youtu.be/Y59LwQNmRJY) [-scKERL7PK0](https://youtu.be/-scKERL7PK0).
2. **Arată, nu descrie.** Referință de personaj, produs, cameră, schiță de poziții > 10 propoziții [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
3. **O singură față de urmărit.** Character sheet pe fundal gri, fața ștearsă din panoul full-body [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA).
4. **Produsul are sheet propriu** (față, 3/4, spate, sus) și fraza de blocare în prompt — o singură poză „halucinează la jumătatea scenei” [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [fmgVm-fxPDM](https://youtu.be/fmgVm-fxPDM).
5. **Primele ~20% din prompt contează cel mai mult**; restul e respectat tot mai slab [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).
6. **Cifre, nu adjective** (secunde, cm, metri, % din cadru); „photorealistic, cinematic, high quality” nu fac nimic [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
7. **Scrie ce vrei, nu ce nu vrei** — excepție: constrângeri tehnice scurte de cameră/audio („no cuts, no zooms”, „no music”) [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss) [PsQovs2FwqQ](https://youtu.be/PsQovs2FwqQ) (vezi §3.3).
8. **Un clip = o idee, o acțiune, o strategie de cameră** [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8).
9. **Testează scurt, apoi scalează:** 5 s, o generare (sau draft 480p), abia apoi 1080p și loturi [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
10. **Toate variantele greșite la fel = promptul/sursa e de vină, nu norocul** → oprești și repari; mișcarea corectă dar un detaliu ratat = re-rulezi același prompt [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss).

---

## 2. Genjutsu (`hf_mult_motion_control`)

**Ce face:** transferă mișcarea (corp + cameră) dintr-un video de referință pe personajul/obiectele din imagini, în decorul din imagini — „motion transfer” [l5BvSCfu7jQ](https://youtu.be/l5BvSCfu7jQ). Funcționează pe filmare reală, chiar din studio gol, fără green screen [FW_tIpEBJ0U](https://youtu.be/FW_tIpEBJ0U).

**Când îl alegi (prima unealtă generativă din scară):**
- viralul are o mișcare umană/de produs pe care o vrem identică (hook, îmbrăcat, desfăcut, folosit) — mișcarea precisă „imposibil de descris” se rezolvă cu clip de mișcare, nu cu text [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8);
- vrei aceeași acțiune cu alt personaj + altă cameră (schimbarea de locație cu păstrarea mișcării și reluminarea omului e cazul clasic) [Y59LwQNmRJY](https://youtu.be/Y59LwQNmRJY) (spus pentru motion control din Cinema Studio 3.0).

**Intrări (roluri):**
- `video_references` = segmentul din viral (doar bucata cu mișcarea, tăiat cu ffmpeg).
- `image_references` = personajul (pereche cu camera), camera (încăperea), referințele produsului (la HeatGrump: 4 ref. produs) (`heatgrump/CLAUDE.md`).
- Referințele de personaj/cameră doar din poze ≥ 1080 px (`docs/02-reguli.md`, 2 oct).

**Setări:** singurul parametru e `resolution` (480p / 720p / 1080p). Producție = 1080p. Durata o dă clipul de referință (HeatGrump: 4 s B1/cozy, 5 s B2) (`heatgrump/CLAUDE.md`).

**Trucuri:**
- Corpul din clipul de referință trebuie să se vadă suficient: „dacă modelul nu-ți înțelege referința, probabil nu vede destul din ea” → alege segmente cu subiectul întreg, cameră nu prea aproape [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8) (spus pentru video-referință în Seedance).
- Acțiunea trebuie să existe în clipul sursă; transferul nu inventează un moment care nu e acolo (iese slop) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) (spus pentru Seedance v2v).
- Camera (imaginea de cameră) aleasă după lumină: lumina proastă = slop; 3/4, nu frontal [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
- Clipurile de mișcare se ROTESC între videouri (același clip pe toate = același video) (`heatgrump/CLAUDE.md`).
- Poți filma tu acțiunea (telefon) când viralul nu are segment curat [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8) [FW_tIpEBJ0U](https://youtu.be/FW_tIpEBJ0U).

**Limite și refuzuri (experiența noastră, `heatgrump/CLAUDE.md`, 2 oct):**
- Clipuri de mișcare **sub 2 s pică fără motiv afișat** (0,9 s și 1,7 s au picat) → minim 2 s, ideal 4–5 s.
- Un personaj + un clip anume pot fi respinse de 2 ori → schimbi clipul de mișcare, nu promptul.
- `ip_detected` → treci pe GPT Image 2.5 → Seedance 2.5 `omni_reference` (treapta următoare, `docs/05-motorul-autonom.md`).
- Refuzurile nu se taxează [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [DcoBYbytZp8](https://youtu.be/DcoBYbytZp8).

---

## 3. Seedance 2.5 (`seedance_2_5`)

Setări fixe la noi: `aspect_ratio "9:16"` + width 1080 / height 1920, `resolution "1080p"`, `bitrate_mode "high"`, `generate_audio true`. Fără `aspect_ratio` iese 16:9, fără `resolution` iese 720p (`heatgrump/CLAUDE.md`). Bitrate high = 10-bit, fără banding [bY8RDKoBwU0](https://youtu.be/bY8RDKoBwU0) (spus pentru Seedance 4K / 2.0).
Ce aduce 2.5 față de 2.0: ține mișcarea în loc să o ascundă în tăieturi, anatomie și haine stabile între tăieturi și schimbări de lumină, reflexii corecte, ~jumătate din batch-uri pentru aceeași scenă [jvkdHdeWICM](https://youtu.be/jvkdHdeWICM) [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs). La UGC înțelege telefonul ca obiect fizic (tremur în mână, panoramare din încheietură) [jvkdHdeWICM](https://youtu.be/jvkdHdeWICM).

### 3.1 Pe moduri

**`omni_reference` (modul principal)** — `start_image` (placa GPT Image 2.5) + `image_references` (personaj, produs) [+ `end_image`].
- I2V e cel mai consistent; T2V doar pentru teste [nnGFEUeL-P0](https://youtu.be/nnGFEUeL-P0) [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8).
- Primul cadru e păstrat puternic (texturi, logica luminii), 12 s fără drift [Y59LwQNmRJY](https://youtu.be/Y59LwQNmRJY) (spus pentru Cinema Studio 3.0 video).
- `end_image` pentru tranziții: start fără element, end cu element [em66Mvt8QLc](https://youtu.be/em66Mvt8QLc).
- Lanț de clipuri: ultimul cadru al clipului devine `start_image` pentru următorul („build, animate, extract, repeat”) [McwoKOIxIPY](https://youtu.be/McwoKOIxIPY) [em66Mvt8QLc](https://youtu.be/em66Mvt8QLc).

**`t2v`** — „slot machine” [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8). Doar pentru test rapid de idee sau un viral izolat fără personaj recurent [PsQovs2FwqQ](https://youtu.be/PsQovs2FwqQ) (spus pentru 2.0).

**`video_edit` (video → video)** — recast pe un clip existent.
- Prompt dovedit: „replace the character in this video with the person in this image. Keep the video one-to-one and only swap out the person.” Lumina/umbrele se potrivesc singure [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ).
- **Minim 4 s la intrare**; segment mai scurt → freeze-frame pe ultimul cadru până la 4 s; durata = durata referinței („anything longer and the AI starts guessing”) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ).
- Scrie lista cu ce rămâne neatins (fața, mersul, gesturile, mișcarea camerei handheld) și secunda exactă a schimbării [Yte-UGhYkPQ](https://youtu.be/Yte-UGhYkPQ) (spus pentru 2.0); păstrarea filmării cere direcție mult mai precisă decât generarea liberă [uZkGA1EuIHI](https://youtu.be/uZkGA1EuIHI).
- Schimbă locația, ținuta, aspectul, unghiul (high/low/Dutch) pe filmare de telefon [U7UP0Eq_Mm0](https://youtu.be/U7UP0Eq_Mm0) [biDzR-ExEu8](https://youtu.be/biDzR-ExEu8) [aXPrQw1gfj8](https://youtu.be/aXPrQw1gfj8) [UlBDRHLAfUY](https://youtu.be/UlBDRHLAfUY); adaugă adâncime cu poze de recuzită + screenshot al cadrului [YdZbUA0JO28](https://youtu.be/YdZbUA0JO28).
- Pică dacă momentul cerut nu e în sursă → I2V din captura locației și lipire la montaj [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ).
- La 1080p schimba detalii mici, la 4K le păstra [bY8RDKoBwU0](https://youtu.be/bY8RDKoBwU0) (spus pentru 2.0) → la recast verifică detaliile produsului cadru cu cadru.
- **Ipoteză:** alternativă la Genjutsu pentru recast; costul pe secundă acceptată se compară (`docs/05-motorul-autonom.md`, treapta 5).

**`video_extension`** — prelungești un clip; continuarea cu videoul anterior ca context păstrează fața, hainele, atmosfera fără start frame nou [pThgGdlO58I](https://youtu.be/pThgGdlO58I) [Y59LwQNmRJY](https://youtu.be/Y59LwQNmRJY).

**Referințe video / audio (în orice mod care le acceptă):**
- `video_references` pentru mișcarea camerei: o atașezi, o numești „video 1” și ceri să copieze mișcarea [cL0RT2OA5Is](https://youtu.be/cL0RT2OA5Is) (spus pentru 2.0). Spune în prompt ce face fiecare referință: „videoul ghidează mișcarea și camera, imaginile arată aspectul” [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).
- Video care rulează în scenă (ex. pe un ecran): durata generării EXACT cât clipul [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s).
- `audio_references`: melodie fredonată → personajul cântă exact notele; piesă → mișcările cad pe beat; lipsync automat dacă urci audio [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [cL0RT2OA5Is](https://youtu.be/cL0RT2OA5Is).

### 3.2 Structura promptului
Ordinea echipei Higgsfield (primele ~20% contează cel mai mult) [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8):
1. **Context + stil** (prefix de stil comun tuturor clipurilor: lumină, cameră, culoare, audio) [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
2. **Referințe active** („call sheet”): ce e fiecare imagine/video; fără descriere vizuală (e treaba imaginilor). Linia: „characters, environments and props 100% match the reference” [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).
3. **Structura cadrului**: acțiunea beat cu beat, cu timpi.
4. **Locks & constraints**: reguli stricte, mereu „no music, SFX only” [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).

Reguli de scris:
- **Cifre, nu adjective:** acțiune pe jumătăți de secundă (mâna la 0,5 s, obiectul la 1,5 s, în picioare la 3 s), distanțe în cm/m, viteză prin comparație („de 3× mai rapid decât un dolly obișnuit”) [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss); poziții ca % din cadru („personajul la 20% pe X, 30% pe Y”) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M); dimensiunile produsului („22 cm”) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) [uZkGA1EuIHI](https://youtu.be/uZkGA1EuIHI).
- **Fizica, nu rezultatul:** ce face forța asupra corpului/obiectului (greutate, inerție, unde aterizează); „make it more natural” nu face nimic [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs) [LUWMI0zy0BQ](https://youtu.be/LUWMI0zy0BQ) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA).
- **Coregrafie mișcare cu mișcare:** „dances” nu înseamnă nimic; scrie fiecare gest [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ). Excepție: un termen cunoscut („K-pop”) poate ajunge [LUWMI0zy0BQ](https://youtu.be/LUWMI0zy0BQ).
- **Descrie ce vede camera**, nu doar ce se întâmplă [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4); descrie imaginea, apoi pui referința („woman in robe [ref] in the bedroom [ref]”) [tW40b122Rbs](https://youtu.be/tW40b122Rbs).
- **Nu descrie aspectul personajului dacă ai atașat sheet-ul** (inventează alte fețe) — doar hainele; nu descrie camera dacă ai atașat-o [-scKERL7PK0](https://youtu.be/-scKERL7PK0).
- **Acțiuni explicite:** „he opens it himself with a clear action”; dă „aer” între acțiuni (întâi se uită, apoi zâmbește) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4). Începe în mijlocul acțiunii, fără intro gol [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ).
- **Interpretare literală:** „mushroom-shaped explosion” a dat o ciupercă → numește lucrul direct; culoarea nespecificată o alege modelul [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8) [uZkGA1EuIHI](https://youtu.be/uZkGA1EuIHI).
- **Plan continuu:** dacă împarți promptul pe secunde/beats, Seedance taie → pentru clipurile noastre de 4–5 s scrie o singură mișcare continuă, „one continuous shot” [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [vUYq38wC_xI](https://youtu.be/vUYq38wC_xI). *Contradicție:* Hell Grind spune că în single shot poți defini fiecare secundă [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M), iar timestamp-urile sunt bune când CHIAR vrei mai multe cadre [cL0RT2OA5Is](https://youtu.be/cL0RT2OA5Is). Regula noastră: timpi pe acțiune da, cuvinte de tăietură („shot 2”, „cut to”) nu.
- **Prompt prea lung / contradictoriu** → „sanitizează” sau rescrie de la zero; promptul supraîncărcat arde credite [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4). Lasă modelului loc de decizii unde nu contează [036jyFZWppw](https://youtu.be/036jyFZWppw).

### 3.3 Negații — contradicția din surse
- **Contra:** modelul ignoră „not”: „not a game, no CGI” scris de 12 ori a dat exact aspect de joc; „no held objects, no handle” tot a pus o sabie în mână [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss); „he's not crying” → opusul [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) (spus pentru 2.0).
- **Pentru (au mers):** „no cuts, no zooms” la POV [PsQovs2FwqQ](https://youtu.be/PsQovs2FwqQ) [c4ddLt57aQ4](https://youtu.be/c4ddLt57aQ4); „no 3D, no cartoon, no VFX” contra pielii plastic [PsQovs2FwqQ](https://youtu.be/PsQovs2FwqQ); „no music, SFX only” [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8); „no other cars front/behind” [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA); „runs forward, natural smile, alive eyes, no color change” [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4); avertismentele de failure mode puse ÎN prompt [-scKERL7PK0](https://youtu.be/-scKERL7PK0).
- **Cum aplicăm (interpretarea noastră, de confirmat cu cifre):** negații scurte doar pentru cameră/montaj/audio (cuts, zoom, music, subtitles). Pentru stil și obiecte → formulare pozitivă: în loc de „no CGI” descrii lumina și textura dorite; în loc de „no object in hand” ceri o acțiune care ține mâinile ocupate/vizibile [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss). Nu numi obiectul pe care nu-l vrei.

### 3.4 Audio
- Un singur track: muzica adăugată de model nu se mai poate scoate → în prefix: „only environmental sound effects, no music, no subtitles” [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4). La noi muzica se pune la montaj; doar hook-ul are sunet propriu (`docs/02-reguli.md`, 5 oct).
- Vocea e legată de aspectul personajului: blochezi imaginea → blochezi vocea [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) (spus pentru 2.0).
- Replică: descrie tonul și pauzele („micro pauses”); cuvintele grele scrise fonetic [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).

### 3.5 Durată, fps
- Seedance 2.5: 4–30 s per generare [jvkdHdeWICM](https://youtu.be/jvkdHdeWICM). Clipurile noastre: 4–5 s; testul: 5 s [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4).
- Video→video și referințe video: durata = durata referinței [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s).
- Scenă înghesuită → împarte în 2 prompturi, ca emoția să aibă timp [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA).
- FPS: scrie „24 fps” în prefix; dacă iese sacadat (~18 fps) → ștergi cadrele duplicate la montaj [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) (ipoteză: `ffmpeg mpdecimate` face asta automat).
- Mișcare rapidă care morfează → generezi mai lent și accelerezi la montaj [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8).

### 3.6 Consistență în Seedance
- Plan de stabilire la început (cine unde stă) → pozițiile rămân tot clipul [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) [kFKpcCHkuPI](https://youtu.be/kFKpcCHkuPI).
- Ancoră fizică în cameră („lângă lampă, în stânga patului”) [kFKpcCHkuPI](https://youtu.be/kFKpcCHkuPI) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- Screenshot din take-ul bun → referință/start pentru următoarele; trebuie să corespundă sheet-ului (altfel detaliul lipsă dispare peste tot) [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
- Elementele care lipsesc în unele take-uri → lock explicit „X on both shoulders in every single cut” [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).

### 3.7 Draft → 1080p
- `seedance_2_5` are draft 480p finalizabil la 1080p (specificația uneltei). Notițele nu-l menționează.
- Regula noastră: mișcarea și compoziția se validează pe draft; la 1080p merge doar draftul care trece QA de mișcare. **Ipoteză:** costul draft + finalizare < două rulări 1080p — se măsoară la primul lot și se trece aici.

---

## 4. GPT Image 2.5 (`gpt_image_2_5`)

Rol: plăci de start, character sheet, product sheet, schițe — și editare. „Cel mai bun model pentru editare de produs / editare de imagine” [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) și pentru character sheet fotorealist când ai deja referință [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) (spus pentru GPT Image 2). Parametri: variante flare/sunburst (ce face fiecare — de testat, notițele nu spun), `quality` low…max, `resolution` 1k/2k/4k, `background`, `image_references`. Producție: 9:16, 4k, quality high; „cu cât e mai bun inputul, cu atât e mai clar videoul” [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s).

**Plăci de start (start_image):**
- Scrie ca un fotograf: obiectiv, diafragmă, granulație, sursa luminii, ce se vede în cadru [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8).
- Unghi 3/4, nu frontal (adâncime; Seedance nu înțelege adâncimea frontal) [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
- „Clean your plate”: șterge text, dezordine, obiecte care levitează înainte de video [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA) [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s); mijloc curat, puțină recuzită (obiectele multe se contopesc) [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs) [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc).
- Atenție: la locații GPT „strică spre galben” (dominantă galbenă) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) (spus pentru GPT Image 2) → cere culorile explicit (la noi: vii, semicalde, nu auriu/portocaliu).
- Imaginea trebuie să fie deja 9:16 (altfel benzi negre) [FSQ_IIIbtVI](https://youtu.be/FSQ_IIIbtVI) [DcoBYbytZp8](https://youtu.be/DcoBYbytZp8).

**Character sheet:**
- Fundal **gri** simplu („după multe teste, gri merge mult mai bine decât alb sau negru”; „am ars o grămadă de credite până am învățat asta”) [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc).
- Panouri: close-up față (fața pe care se blochează) + full body față și spate (înălțimea, constituția); lumină moale, fără umbre dure pe față [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- **O singură față**: „Erase the face from the full body shot on the right panel” [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) — altfel personajul derivă [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
- Fără text pe haine [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA). Recuzita mică „coaptă” în sheet → mai puține imagini de urcat [i55bUFB3lFs](https://youtu.be/i55bUFB3lFs).
- Păstrează 2 candidați: o față bună în poză poate cădea în mișcare [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- Stare nouă (altă ținută, ud) = sheet nou, nu cuvinte în promptul video [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- Ținută: GPT „se descurcă cel mai bine cu hainele”, dar poate face hainele albăstrui → verifică culoarea [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) (spus pentru GPT Image 2).

**Planșă produs multi-unghi:**
- „Make a product sheet with front and 3/4 views of the [product] from image 1” (+ spate, sus) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4).
- Produs pe fundal gri neutru (se integrează oriunde) [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA). Pentru obiecte cu interior: exterior + interior [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
- Prop sheet-ul GPT a ieșit plat, fără volum/umbre [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s) (spus pentru GPT Image 2) → cere explicit volum, umbre de contact, reflexii.

**Schițe / hărți de poziție:**
- „Textul nu poate fixa o locație.” GPT: „Make a schematic. Mark the [obiect] and lock the [obiect 2] to its right. Two times a person's height, on the same line” + camera atașată [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- Variantă: „high angle wide shot of the location” → puncte desenate unde stau obiectele → „put [obiect] into image 1 where the circles are, create a location scheme” → plan cu distanțe; în prompt: „obiectele apar exact conform schemei” [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4).
- Hartă de sus cu culori (o culoare = un personaj) [kFKpcCHkuPI](https://youtu.be/kFKpcCHkuPI) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M); traseu desenat (linie albastră = drum, roșu = obstacole) + „fără liniile din diagramă în video” [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA).
- Schiță de proporții (chiar urâtă) pentru mărimi [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs) [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc); imagine „size fit” cu personaj + obiect la scară [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ).

**Săgeți pe referință:** săgeată roșie pe prop sheet → apasă butonul corect [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s); semn roșu pe imaginea camerei pentru poziție [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA).

**Degradarea la editări repetate:**
- Fiecare editare scade calitatea, imaginea „se înmoaie”, aspect plastic [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- Nu edita aceeași imagine de multe ori; când editările se bat cap în cap → prompt complet nou și regenerezi de la zero [-scKERL7PK0](https://youtu.be/-scKERL7PK0).
- Salvare: pui originalul peste versiunea editată și mascezi doar zona schimbată [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) (ipoteză la noi: compunere cu ffmpeg/PIL).
- Prompt de editare directiv, nu descriptiv („keep everything else the same”, „recreate this exact image”) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [FSQ_IIIbtVI](https://youtu.be/FSQ_IIIbtVI).

---

## 5. Consistență personaj + produs

- **„Elements” = referințe cu nume.** În interfața Higgsfield, elementul numit exact ca tag-ul din prompt (@nume) se atașează singur [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4). Prin MCP: îl dai explicit în `image_references` și îl numești în prompt cu un rezumat fizic scurt („robe, green fleece lining, ankle length”) [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4).
- **Ordinea referințelor:** image 1 = personajul (descris primul în prompt), image 2 = camera, apoi produsul; obiectul pe care îl apucă numit explicit „image 4” [-scKERL7PK0](https://youtu.be/-scKERL7PK0) (spus pentru 2.0).
- **Scoate referințele de care nu ai nevoie** — referința în plus „trage” cadrul spre ea [-scKERL7PK0](https://youtu.be/-scKERL7PK0). (HeatGrump: `ip_detected` la multe referințe de produs → 1 referință, apoi doar cutia, `heatgrump/CLAUDE.md`.)
- **Fraza de blocare a produsului** (o punem în orice prompt cu produs):
  `Use the products from the attached image exactly as shown. Preserve their shape, design, and proportions. Do not redesign them.` [fmgVm-fxPDM](https://youtu.be/fmgVm-fxPDM)
  + `characters, environments and props 100% match the reference` [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8) + `lock [produs] as exact reference` [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- Recuzita recurentă = prop sheet propriu; obiectele care apar o singură dată nu primesc asset (modelul le inventează) [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).
- Mărimea produsului fixată în prompt dacă variază [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s).
- Ținuta blocată ca referință separată când combini take-uri diferite [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- Camera (încăperea) din două vederi (față + spate) → batch-urile nu mai derivă; „pentru tăietura N folosește imaginea X” [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc).
- Fundal care pare clona produsului (obiecte asemănătoare în fundal) → șterge-le din placă [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA).
- Recast cu față reală: păstrezi corpul/ținuta din sheet și pui poza reală în panoul de portret [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs).

---

## 6. Realism

- **Lumină:** „practical light only” (ferestre, lămpi din cadru); lumina artificială „din spate” = plastic, personaje lipite [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M). Prefix: „natural light only, key light from sky and windows only” [-scKERL7PK0](https://youtu.be/-scKERL7PK0). Pentru cadre luminoase: „soft even daylight from the camera side, bright and clean”; contre-jour întunecă fețele [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ). Pe piele: „no harsh shadows”, „soft flat lighting” [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA). Detaliile mici de lumină (raze) fac imaginea reală [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc). Lumina e criteriul de alegere a camerei [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ).
  *Atenție la stilul nostru:* „golden hour, low warm sun” dă volum [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8), dar regula noastră e culori vii, semicalde, NU auriu/portocaliu → nu folosim golden hour.
- **Culoare:** 60-30-10 (dominantă / secundară / accent) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M); paleta fixată în prefix, aceeași pe tot videoul [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y).
- **Cameră și lentile:** numește obiectivul și diafragma („35 mm, f/2.8”) — „photorealistic, cinematic” nu fac nimic [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M); „anamorphic lens, shallow depth of field, film grain” scoate aspectul digital prea curat [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4); camerele numite dau un aspect apropiat, nu identic [FSQ_IIIbtVI](https://youtu.be/FSQ_IIIbtVI). Nu scrie „cinematic camera movement” (iese slop) [OiULPvTJ-0E](https://youtu.be/OiULPvTJ-0E). Handheld subtil (respirație, mers) = realism [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA); la UGC, Seedance 2.5 imită telefonul ținut în mână [jvkdHdeWICM](https://youtu.be/jvkdHdeWICM). (Cartea noastră de stil: cameră fixă, fără zoom.)
- **Grain / anti-plastic:** „light atmospheric haze”, „film grain”, „crush the blacks” [-scKERL7PK0](https://youtu.be/-scKERL7PK0) (spus pentru Nano Banana Pro); „no 3D, no cartoon, no VFX” [PsQovs2FwqQ](https://youtu.be/PsQovs2FwqQ).
- **Cadru strâns:** „the tighter the frame, the less slop” [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA); locația frontală = fără adâncime [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M).
- **Mișcare descrisă fizic:** umeri, greutate, inerție, pas, aterizare [QfylrxtQSSs](https://youtu.be/QfylrxtQSSs) [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA); căderi „cu greutate reală” [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4); emoție prin anatomie (maxilar, degete, respirație) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ); micile reacții fac scena reală [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc).
- **Ce strică realismul:** text pe ecrane/ambalaje mici devine „mush” [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA) [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s) (la noi: fără text în imagine); acting subtil e mai slab decât acțiunea mare [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8).

---

## 7. Cost minim

### 7.1 Scara de decizie (per cadru din viral)
Urci o treaptă doar când QA pică de 3 ori (`docs/05-motorul-autonom.md`).

| # | Treaptă | Cost | Când |
|---|---|---|---|
| 0 | Reutilizare clip aprobat din bibliotecă | 0 | există clip cu același rol (conector, telecomandă, B-roll per produs) |
| 1 | Montaj fără AI (ffmpeg din placă/clip existent) | 0 | cadru static, detaliu |
| 2 | **Genjutsu** 1080p | 28–66 (44 la ~4 s) | viralul are mișcarea; segment ≥ 2 s, ideal 4–5 s |
| 3 | **GPT Image 2.5 → Seedance 2.5 `omni_reference`** | 6,5–11 + 35 | Genjutsu respins (`ip_detected`, refuz dublu) sau mișcarea nu e reutilizabilă |
| 4 | **Seedance 2.5 `video_edit`** | de măsurat | recast direct pe clipul viral ≥ 4 s; comparat cu treapta 2 pe cost/secundă acceptată |

Se măsoară **credite / secundă acceptată** pe unealtă și tip de cadru; scara se reordonează după cifre (`docs/05-motorul-autonom.md`).

### 7.2 Testare înainte de producție
- Test personaj + cameră: **5 s, o singură generare** — „exact cum eviți să arzi credite”; take-ul de test a ajuns chiar în montaj [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- O variabilă pe test (doar personajul SAU doar camera) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ).
- Draft 480p pentru mișcare, 1080p doar pentru ce trece (§3.7, ipoteză de cost).
- **Ipoteză:** explorarea plăcilor la GPT Image 2.5 `quality low` / `1k`, finalul la high/4k — de verificat dacă prețul scade (tranzacțiile arată deja 6,5 vs 11).
- Perfecționezi imaginea (ieftină), nu videoul: „fă variante de imagine în loc să ceri modelului video schimbarea din cuvinte” [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [-scKERL7PK0](https://youtu.be/-scKERL7PK0).
- Fixează întâi camera/unghiul, abia apoi pui persoana [em66Mvt8QLc](https://youtu.be/em66Mvt8QLc).
- Primele prompturi „leneșe” ca să fixezi ieftin vibe-ul și culorile, apoi detaliezi [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA).

### 7.3 Re-rulezi FĂRĂ să schimbi promptul când
- mișcarea e corectă și doar un detaliu iese prost („roll” prost, nu prompt prost) [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss) [-scKERL7PK0](https://youtu.be/-scKERL7PK0);
- un singur take din lot e ciudat — lotul îți arată imediat dacă e glitch sau prompt [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss);
- textul/un detaliu mic s-a mâzgălit o dată [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y).

### 7.4 Schimbi promptul (sau sursa) când
- **toate variantele greșesc la fel** — „problema e promptul, nu norocul”; a continua „arde credite degeaba” [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) [-scKERL7PK0](https://youtu.be/-scKERL7PK0);
- îi spui ce s-a stricat în cuvinte simple și repari DOAR aia; nu rescrii tot [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4); iterarea unui prompt de 3 ori bate 3 prompturi separate [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ);
- primele secunde sunt bune → ceri schimbarea doar pe restul [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M);
- același eșec pe toate loturile la `video_edit` → treci pe I2V din captură [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ).

### 7.5 Alte economii
- **Refuzurile (NSFW / IP / guidelines) nu se taxează** [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [DcoBYbytZp8](https://youtu.be/DcoBYbytZp8) → un refuz nu e pierdere de bani, doar de timp; rescrii promptul sau schimbi imaginea (blocarea poate veni din imagine) [DcoBYbytZp8](https://youtu.be/DcoBYbytZp8).
- Dintr-o generare ratată poți tăia 1–2 s perfecte [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M); reutilizezi cadre bune în alte videouri [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4).
- Pentru un moment nou: iei promptul care a mers și adaugi doar acțiunea nouă [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4).
- Nu crea asset pentru obiecte/locuri care apar o singură dată [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4).
- Schema de poziții scoate din „loteria de 20 de generări” [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc).
- Aprobare pe lot (porți de buget) [l7W3QzU8w5s](https://youtu.be/l7W3QzU8w5s); verifică `balance` înainte de loturi mari (`heatgrump/CLAUDE.md`).
- Ofertele „unlimited” (ex. Seedance 2.5 33 de zile, aug 2026) → folosește-le pentru teste când apar [nnGFEUeL-P0](https://youtu.be/nnGFEUeL-P0) [6l3Nt0T2Kow](https://youtu.be/6l3Nt0T2Kow).
- Randamentul real e mic (1 din ~64 de generări utilizabilă la film; 1,6% la alt film) [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [i55bUFB3lFs](https://youtu.be/i55bUFB3lFs) → la noi ținta e clip scurt, simplu, cu referințe; dar bugetul include reîncercări.

---

## 8. Probleme → soluții

| Problemă | Soluție | Sursa |
|---|---|---|
| Fața derivă între clipuri | o singură față pe sheet (șterge fața din full-body); nu descrie aspectul în prompt | [CHHH8tNioSc](https://youtu.be/CHHH8tNioSc) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [-scKERL7PK0](https://youtu.be/-scKERL7PK0) |
| Produsul halucinat din unghiuri nevăzute | product sheet față/3/4/spate/sus + fraza de blocare | [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [fmgVm-fxPDM](https://youtu.be/fmgVm-fxPDM) |
| Produs/recuzită diferă între take-uri | prop sheet + „lock X as exact reference” | [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) |
| Element lipsă în unele take-uri | „X … in every single cut” | [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) |
| Mărimea obiectului variază | dimensiune în cm în prompt; imagine „size fit” | [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s) [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) |
| Obiectul/personajul își schimbă poziția sau direcția | schemă de poziții + ancoră fizică + coordonate % | [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) |
| Apasă/apucă locul greșit | săgeată roșie pe referință; „image 4” numit explicit | [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s) [-scKERL7PK0](https://youtu.be/-scKERL7PK0) |
| Referința în plus trage cadrul / apare pe tot ecranul | scoate referința; schemă + „folosește X ca referință în keyframe” | [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) |
| Tăieturi nedorite în clip | „one continuous shot”, fără împărțire pe beats; „no cuts, no zooms” | [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [PsQovs2FwqQ](https://youtu.be/PsQovs2FwqQ) |
| Modelul mută obiectele în loc de cameră | ancorezi camera de un element + „critical” | [-scKERL7PK0](https://youtu.be/-scKERL7PK0) |
| Muzică adăugată de model | „no music, only environmental sound effects” în prefix; alegi take-ul curat | [-scKERL7PK0](https://youtu.be/-scKERL7PK0) |
| Video sacadat (~18 fps) | „24 fps” în prefix; ștergi cadrele duplicate | [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) |
| Piele plastic / lumină de studio | „practical light only”, grain, „no 3D, no cartoon, no VFX” | [6aJ2BneDB5M](https://youtu.be/6aJ2BneDB5M) [PsQovs2FwqQ](https://youtu.be/PsQovs2FwqQ) |
| Fețe în umbră | cameră mai luminoasă; lumină frontală din partea camerei | [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) |
| Dominantă galbenă la plăci GPT | culori cerute explicit (vii, semicalde) | [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) |
| Haine albăstrui / logo deformat după GPT | verifici culoarea; regenerezi (la noi fără branduri) | [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) |
| Prop sheet plat | cere volum, umbre de contact, reflexii | [HSON-SoFz7s](https://youtu.be/HSON-SoFz7s) |
| Imagine „înmuiată” după multe editări | regenerezi de la zero cu prompt complet; mască doar pe zona editată | [-scKERL7PK0](https://youtu.be/-scKERL7PK0) [3rDs6FhFoUQ](https://youtu.be/3rDs6FhFoUQ) |
| Mișcare nenaturală, rigidă | descrii fizica concretă, nu „more natural” | [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) |
| Acțiune grăbită / pași săriți | timpi pe jumătăți de secundă; „aer” între acțiuni | [s-eeHOkkLss](https://youtu.be/s-eeHOkkLss) [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) |
| Obiectul „se face singur” (se deschide) | „he opens it himself with a clear action” | [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) |
| Obiecte apar din aer | „sunt deja în cadru de la început” | [ODNzk5x2tR4](https://youtu.be/ODNzk5x2tR4) |
| Mișcare rapidă morfează | slow-mo + accelerare la montaj | [IAswRvWjdD8](https://youtu.be/IAswRvWjdD8) |
| `video_edit` refuzat / clip scurt | freeze-frame până la 4 s, durata = 4 s | [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) |
| `video_edit` dă slop (momentul nu e în sursă) | I2V din captura locației, lipire la montaj | [Hn8A8D4-SpQ](https://youtu.be/Hn8A8D4-SpQ) |
| Video-referința nu e înțeleasă | segment cu subiectul întreg, cameră mai departe | [reFzEtCG_m8](https://youtu.be/reFzEtCG_m8) |
| Genjutsu pică fără motiv | clip de mișcare < 2 s → alt clip ≥ 2 s | `heatgrump/CLAUDE.md` |
| Genjutsu respinge de 2 ori același personaj | schimbă clipul de mișcare | `heatgrump/CLAUDE.md` |
| `ip_detected` | mai puține referințe de produs (1, apoi doar cutia) / treapta GPT→Seedance | `heatgrump/CLAUDE.md` |
| Refuz NSFW/guidelines fără motiv | rescrii promptul (cuvinte violente, nume de persoane, versuri); fața care seamănă cu o celebritate → schimbi persoana; nu se taxează | [DcoBYbytZp8](https://youtu.be/DcoBYbytZp8) [-scKERL7PK0](https://youtu.be/-scKERL7PK0) |
| Iese 16:9 / 720p | `aspect_ratio "9:16"` + width/height; `resolution "1080p"` explicit | `heatgrump/CLAUDE.md` |
| Text pe ecrane/ambalaje = mâzgăleli | fără text în imagine; regenerezi | [GNxmt_4IifA](https://youtu.be/GNxmt_4IifA) [0HIRIT7px9Y](https://youtu.be/0HIRIT7px9Y) |

---

## 9. Ce NU folosim (regula din 10 oct)

Menționate în notițe, dar **interzise în producție** — nu le apelați, chiar dacă un video le laudă:
- **Video:** Kling (2.5, 2.6, 3.0, O1 Edit, Kling Motion Control / `motion_control`), Veo 3 / 3.1, Sora 2 / Pro (+ enhancer), Wan 2.5 / 2.6, Minimax Hailuo, Seedance 1.5 / 2.0 (folosim 2.5).
- **Imagine:** Soul / Soul 2 / Soul Cinema / Soul ID, Nano Banana (2, 2.1, Pro), Seedream (4.x, 5.0), Flux, Reve, Z-Image, Niji, GPT Image 2 (folosim 2.5).
- **Platforme/presets:** Marketing Studio (UGC, Hyper Motion, TV Spot, Wild Card…), Cinema Studio cast/scenes/multi-shot, AI Cast, AI Influencer, Recast / Shots / Transitions apps, Shorts Studio, Supercomputer, 3D Jutsu / pluginuri Blender-Premiere-AE-DaVinci, Katana, Vibe Motion, Higgsfield Audio change voice, upscale/reframe/relight.
- **Efecte sonore** (`generate_audio`, < 1,5 credite) apar în tranzacții, dar nu sunt în baza de 3 unelte → doar cu acordul lui Szasz.
De ce: Szasz a fixat baza de unelte ca toate videourile să aibă același stil, costurile să fie măsurabile pe 3 unelte și scara de cost să fie una singură (`docs/02-reguli.md`, 10 oct).
