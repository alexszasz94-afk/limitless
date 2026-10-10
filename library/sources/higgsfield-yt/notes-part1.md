# Note Higgsfield YT — part1 (47 videouri, 2025-03 → 2026-10-07)

Sursa: `chunks/part1.txt`, citit integral. Doar fapte spuse explicit în transcrieri; fiecare cu linkul videoului.
Videouri fără nimic util (filme/trailere/shorts doar cu muzică): Oneiric, MORK, Museum Heist, Mechanic, Time Travel 1883, Anime opening, VFX duel, Figma, Higgsfield x Adobe, Mini-Apps, Start&End Frame, Effects Pack 1, DoP launch, Ranking models, How did we get AI.

**Atenție:** în part1 NU apar deloc Genjutsu, motion control, Marketing Studio, UGC/Ads, Speak, relight sau reframe ca unelte numite. Partea asta acoperă mai ales Seedance 2.0/2.5, Cinema Studio, Soul Cinema, Nano Banana Pro, Seedream 5.0 Pro, GPT Image 2, Kling 2.6, Veo 3.1, Sora 2, Wan 2.5, MCP și pluginurile.

---

## 1. Unelte / modele

**Seedance 2.5** (pe transcriere apare „Cance/Cedance/CD 2.5”)
- Numit „hands down the best model right now” pentru video, folosit în Cinema Studio; dacă lipiți promptul, referințele se atașează automat ca „elements” (https://youtu.be/kFKpcCHkuPI).
- Acceptă video de referință (un gray-box randat din Blender) + prompt scris secundă cu secundă; durată setată la 30 s ca să se potrivească blocajului (https://youtu.be/OiULPvTJ-0E).

**Seedance 2.0**
- Disponibil pentru toată lumea pe Higgsfield, fără waitlist și fără cont business, din 2026-04-11 (https://youtube.com/shorts/xQF-EFnB3Gw, https://youtube.com/shorts/cL0RT2OA5Is).
- Multi-reference: urci decorul + personajele, iar modelul se ocupă de încadrare, poveste și stilul de montaj (https://youtube.com/shorts/PtBAkPhrfcs).
- Copiază o mișcare de cameră dintr-un clip: îl atașezi ca referință, îl etichetezi „video 1” și ceri să copieze mișcarea. Lipsync automat dacă urci audio. Mai multe cadre (wide / medium / close-up) într-o singură generare, cu timestamp-uri în prompt, ca să economisești credite (https://youtube.com/shorts/cL0RT2OA5Is).
- Video-to-video în 4K pe filmare reală: schimbă fundalul, adaugă elemente (foc, creaturi), transformă o mână. Păstrează fața, mersul și mișcarea camerei handheld dacă promptul le „blochează” explicit. Reaprinde automat lumina pe subiect după mediul generat: neonul și lava se reflectă pe față/mașină, apare vânt în păr (https://youtu.be/Yte-UGhYkPQ).
- Un singur track audio: muzica adăugată de model nu se mai poate separa în post (https://youtu.be/-scKERL7PK0).
- La început a avut limită de 3.000 de caractere pe prompt; echipa scria în chineză ca să încapă mai multă informație (https://youtu.be/-scKERL7PK0).
- Ordinea referințelor contează: image 1 = personajul (descris primul în prompt), image 2 = locația etc. (https://youtu.be/-scKERL7PK0).
- Înțelege personalitatea și emoțiile dacă îi dai limbajul potrivit. Pentru coregrafie e suficient un termen („K-pop”); cu cât controlezi mai puțin, cu atât iese mai bine. Muzica se urcă drept element, împreună cu versurile (https://youtu.be/LUWMI0zy0BQ).

**Seedance 1.5** (test din 2026-01-08)
- Cel mai bun la emoție + audio: lipsync corect, ambient care se schimbă singur între locații. Limitat la 720p. Suportă end frame. Are probleme să genereze medii noi la mișcări agresive de cameră. Singurul care a făcut un pan „adevărat” (Kling și Veo au făcut arc) (https://youtu.be/x0FdaH0fDpQ).

**Kling 2.6**
- „Best value” pentru image-to-video cu audio nativ: rapid, ieftin. Cel mai bun la fizică, mecanica corpului, mișcări de cameră complexe și geometrie stabilă, fără morphing. Vocea sună robotic/sintetic. Uneori adaugă vorbire nedorită, așa că scrie în prompt că nu vorbește nimeni. NU suportă end frame (pentru asta s-a folosit Kling 2.5) (https://youtu.be/XdK93RhPFAo, https://youtu.be/x0FdaH0fDpQ).
- „Kling typically needs more detailed prompts”; enhancer-ul Higgsfield îmbunătățește automat promptul, citind și imaginea (https://youtu.be/AdjllfZuqYM).

**Veo 3.1**: cel mai bun la voce, șoaptă și ambient; scump; output ușor comprimat; maximum 8 s (față de 10 s la alții); îi deformează fețele (https://youtu.be/XdK93RhPFAo, https://youtu.be/x0FdaH0fDpQ).

**Sora 2**: text-to-video premium, cu editare integrată, dar scump. Nu permite keyframe-uri cu oameni reali. Câștigă la text-to-video fără keyframe (https://youtu.be/XdK93RhPFAo).

**Wan 2.5** („One” în transcriere): rezultate decente, dar nișat și „supra-evaluat la preț” față de Kling 2.6; sunet mai slab; artefacte (https://youtu.be/XdK93RhPFAo).

**Soul Cinema**
- Prima alegere pentru personaje și locații: 8 imagini = 1 credit, deci ideal pentru explorare ieftină (https://youtu.be/kFKpcCHkuPI).
- Generează fața și ținuta SEPARAT, apoi le combini în Nano Banana Pro (https://youtu.be/LUWMI0zy0BQ).
- Problemă: pielea iese prea netedă și lumina prea dură; se corectează în Seedream (https://youtu.be/kFKpcCHkuPI).

**Seedream 5.0 Pro** („Cream 5 Pro”): „cel mai bun model acum pentru editare de imagine”. Schimbă detalii (layout, obiecte, pistrui) și păstrează lumina și textura originalului. A redat textura pielii și o lumină mai blândă (https://youtu.be/kFKpcCHkuPI).

**Nano Banana Pro**
- Bun la text în imagine (numele produsului pe borcan, logo păstrat la close-up). Are un LLM în spate: prompturile simple + câteva cuvinte de stil merg. 21:9 dă compoziția cea mai cinematică. Generează 4K, câte 4 rezultate odată (https://youtu.be/AdjllfZuqYM).
- Slab la relații spațiale: dacă îi dai poza unui oraș, încearcă să o bage în cadru („cameră în aer liber”). Textura iese plasticoasă (https://youtu.be/-scKERL7PK0).
- Bun la fuziunea față + ținută într-un singur asset „screen test” și la amestecarea a 2 generări într-una nouă (https://youtu.be/LUWMI0zy0BQ).

**GPT Image 2**: bun la editarea unei imagini existente. A fost folosit pentru a genera un obiect de referință (șopârlă), urcat apoi în Seedance: „când știi exact ce vrei, e mai bine să-i arăți decât să-i descrii” (https://youtu.be/-scKERL7PK0, https://youtu.be/Yte-UGhYkPQ).

**Cinema Studio 3.0 / 3.5**
- Cinema Studio 3.0 construiește scena (mișcare de cameră, mediu, compoziție) din 6–10 imagini. Primește listă de cadre, audio și video (https://youtube.com/shorts/4h-mLecRgf4).
- Cinema Studio 3.5 (2026-05-28): asistent AI integrat, presets, sau mod manual (cadre, setări de cameră, stil, gen) (https://youtube.com/shorts/gXpInRWSiSc).
- În Cinema Studio poți face proiecte și foldere pe tipuri de asset (https://youtu.be/kFKpcCHkuPI).

**Collab (proiecte partajate)**: proiecte partajate prin link sau email, cu permisiuni (viewer/collaborator, aprobare). Păstrează inputurile, prompturile și unealta folosită pentru fiecare generare. Comentarii, chat, apel video (https://youtu.be/-scKERL7PK0).

**MCP / plugin-uri**
- Higgsfield MCP: conector custom în Claude (Settings → Connectors → add custom connector, linkul de la `higgsfield.ai/mcp`) sau plugin în ChatGPT (https://youtu.be/iOwKylW8c5Q, https://youtu.be/NuvA32_dmtg, https://youtube.com/shorts/WzkUQoynkFQ).
- Prin MCP poți genera sute de videouri în paralel. Poate face și un site live cu formular și admin panel (https://youtu.be/iOwKylW8c5Q).
- Agent care postează pe Instagram pe pilot automat (stories/posts/reels). Calitatea vine din skill-urile urcate în conector (https://youtube.com/shorts/JaEpj9OB3Ek).
- Plugin Blender: bridge URL pus în Claude Connectors; plugin-ul gratuit (https://youtu.be/OiULPvTJ-0E).
- Pluginuri DaVinci Resolve (generare pe timeline, LUT din referință, upscale pe footage vechi) și Premiere Pro / After Effects, gratuit: outpaint la orice raport, unghiuri noi, ștergere și adăugare de obiecte (https://youtube.com/shorts/H1hQFOV0LAI, https://youtube.com/shorts/G12IJY2p7QY).

**Vibe Motion** (2026-02-04): motion design din prompt, cu proiect editabil live (font, culori, layout). Primește SVG/PNG. Are presets (ex. poster) și poate face prototip de UI (https://youtu.be/yvuVH6Zg5Vk).

**Extend video**: prelungești un video cât vrei (https://youtube.com/shorts/pThgGdlO58I). **Presets estetice**: peste 20 de „taste layers” aplicate pe personaj (https://youtube.com/shorts/oFv0iQG0sGk).

---

## 2. Costuri și credite

- **Soul Cinema:** 8 imagini = 1 credit (https://youtu.be/kFKpcCHkuPI).
- **Seedance 2.5:** un take de ~17 s cu referințe a costat ~200 de credite. Toată reclama de 30 s, cu iterații, ~2.100 de credite (https://youtu.be/kFKpcCHkuPI).
- **Fără blocaj 3D:** o scenă de dialog cu 6 oameni făcută doar din prompt a ars ~5.000 de credite fără niciun cadru bun. Cu blocaj în Blender a ieșit din 3 iterații (https://youtu.be/OiULPvTJ-0E).
- **Lungmetraj (bugetul echipei):**
  - 4.441.352 de credite ≈ $260.000, adică ~$0,059/credit, pentru 48.336 de generări în 4 zile.
  - 1 din ~64 de generări video e utilizabilă. Un cadru de 10 s a cerut 72 de generări. Din ~800 de asset-uri, 8 au intrat în montaj.
  - ~100.000 de credite au fost aruncate pe o scenă de 2,5 min pentru că s-a schimbat scenariul.
  (https://youtu.be/-scKERL7PK0)
- **Generările eșuate (eroare NSFW/IP) nu se taxează** (https://youtu.be/-scKERL7PK0).
- **Imaginile sunt mult mai ieftine decât videoul:** fă multe batch-uri de imagini și perfecționează keyframe-ul înainte. Seedance copiază imperfecțiunile imaginii în video (https://youtu.be/-scKERL7PK0, https://youtube.com/shorts/1yhwLCoY5Cc, https://youtube.com/shorts/H8TGDBETpzM).
- **Economisire:**
  - mai multe cadre într-o singură generare cu timestamp-uri (https://youtube.com/shorts/cL0RT2OA5Is);
  - blocaj 3D în Blender înainte de generare (https://youtu.be/OiULPvTJ-0E);
  - testează întâi un sample scurt, apoi împarte textul în take-uri scurte, ca să regenerezi doar take-ul greșit (https://youtu.be/NuvA32_dmtg).
- **Planuri:**
  - „MCP unlimited” pentru utilizatori noi, ofertă limitată (2026-07-29) (https://youtu.be/iOwKylW8c5Q);
  - „Nano Banana Unlimited” (2025-09-01, doar titlu) (https://youtu.be/a4Jfijlrxbo);
  - Kling 2.6 + Nano Banana Pro „cu discount mare” (2025-12) (https://youtu.be/AdjllfZuqYM);
  - planul Creator anual „valorează ~$3.000” (https://youtu.be/yvuVH6Zg5Vk).
- **Kling 2.6 vs alții:** cel mai ieftin la calitatea lui; Veo 3.1 și Sora 2 sunt scumpe; Wan 2.5 e „overpriced” (https://youtu.be/XdK93RhPFAo).
- **Model Claude:** Opus 5 e recomandat față de Fable 5 („aproape la fel, mult mai ieftin”) (https://youtu.be/iOwKylW8c5Q).

---

## 3. Fluxuri de lucru

**A. Reclamă ultra-realistă cu personaje consistente (Seedance 2.5)** (https://youtu.be/kFKpcCHkuPI)
1. Proiect în Cinema Studio, cu foldere pe tipuri de asset.
2. Character sheet făcut cu Claude: portret close-up + ținuta din față și din spate, pe **fundal gri simplu**. Panourile de la gât în jos lasă modelului o singură față de folosit, ceea ce e obligatoriu pentru consistență.
3. Variante ieftine în Soul Cinema, apoi corecturi în Seedream 5.0 Pro (pielea, lumina, detalii). Salvezi personajul ca „character X”.
4. Locații în Soul Cinema, la **unghi de 3/4** (adâncimea dă camerei ceva de prins). Ce încurcă le cureți în Seedream: micșorezi mobila din prim-plan, eliberezi masa.
5. Pui mâncarea și produsele direct în imaginea locației, ca să nu ai referințe separate. Recuzita care trece de la un personaj la altul (telefonul, ambalajul cu logo spre cameră) primește referință proprie. Figuranții se fac toți într-o singură imagine.
6. Prompt video pe cadre, cu dialog cronometrat și mișcări de cameră; referințele poartă aceleași nume ca în prompt.
7. Adaugi un plan wide la început ca keyframe care fixează pozițiile, apoi îl tai la montaj.
8. Packshot: începi aproape de logo, camera se retrage și coboară; o mișcare de 4 s; o acțiune concretă (mușcă, mestecă) exact când se oprește camera.

**B. Reclamă din keyframe-uri (Nano Banana Pro → Kling 2.6)** (https://youtu.be/AdjllfZuqYM)
1. Imagine 21:9, 4K, 4 variante, cu cuvinte cheie „commercial shot, shot on RED, anamorphic”.
2. Editări simple pe aceeași imagine: scoți un element, schimbi numele produsului, schimbi expresia.
3. Image-to-video pentru consistență (altfel modelul inventează alt personaj). O singură mișcare de cameră care accentuează reacția. Fără audio dacă pui muzică după.
4. Produsul intră în poveste („a mai rămas o singură bomboană”). Close-up pe mușcătură cu logo păstrat. Packshot cu spotlight pe produs.
5. Post: reordonezi cadrele, crop ca să ascunzi artefacte, speed ramp pe beat, zoom pe produs.

**C. Blocaj 3D în Blender → Seedance** (https://youtu.be/OiULPvTJ-0E)
1. Claude + plugin-ul Higgsfield construiesc scena gray-box și traseul camerei (shot list concret: șine, ținte, tăieturi; poți cere handheld subtil).
2. Playblast la 1920×1080, 24 fps, MPEG-4.
3. Claude citește videoul și scrie promptul Seedance secundă cu secundă.
4. Generezi cu aceeași durată ca blocajul.
- Regula: gray-box-ul dă timing-ul și camera, referințele dau aspectul.
- Promptul are 2 jumătăți: structura (rămâne la fel) + stratul de stil (îl schimbi ca să ai alt „univers” cu aceeași montare).
- Lichidele le lași negre în blocaj; le umple AI-ul.

**D. VFX pe filmare reală (Seedance 2.0, 4K)** (https://youtu.be/Yte-UGhYkPQ)
1. Urci clipul în Claude (îl citește ca frame-uri) și ceri o singură schimbare.
2. Skill-ul scrie lista cu ce rămâne neatins (fața, mersul, inelele, gesturile, mișcarea camerei handheld; la mașină: centura, încadrarea rig-ului) și secunda exactă a schimbării.
3. Pentru un obiect nou, generezi o imagine de referință (GPT Image 2) și o atașezi împreună cu clipul.
4. Cel mai greu caz e handheld-ul (parallax, tremur). Filmezi deja știind ce vrei să adaugi.

**E. Consistența personajului (3 pași)** (https://youtu.be/LUWMI0zy0BQ)
- Fața în Soul Cinema → ținuta separat în Soul Cinema (detaliile mici scrise explicit, ex. plasture pe nas) → fuziune în Nano Banana Pro = „screen test”, master asset-ul pe care Seedance îl verifică la fiecare apariție.

**F. Locație consistentă pentru multe cadre** (https://youtu.be/-scKERL7PK0)
- Iterezi promptul de imagine în batch-uri de 4. Cu un prompt detaliat, Nano Banana Pro dă rezultate consistente, deci dacă ceva e greșit, problema e în prompt.
- Nu edita aceeași imagine de multe ori (se pierd detalii). Când editările încep să se bată cap în cap, ceri lui Claude prompt complet și regenerezi de la zero.
- Faci a doua vedere (reverse angle) din referință și le combini pe amândouă într-o singură imagine de referință 16:9 (sus wide, jos contraunghi).
- Recuzita cu multe fețe (perete cu poze) o generezi pe bucăți și o asamblezi în Photoshop. Într-o singură imagine fețele „derapează”.
- Faci un keyframe separat pentru close-up (ex. frigiderul cu poze) și urci separat fiecare element care trebuie să rămână consistent la close-up.
- Fluxul de lucru: batch de 8; dacă toate greșesc la fel, oprești și repari promptul. Dacă mișcarea e bună dar mici detalii nu ies, mai faci batch-uri cu același prompt. Montezi pe timeline în timp ce generezi.

**G. Prezentator generat dintr-un clip scurt (MCP)** (https://youtu.be/NuvA32_dmtg)
- Referință: clip cu fața vizibilă, lumină constantă, voce clară.
- Prompt în 2 secțiuni: (1) cum arată și sună (haine, decor, unghi) și (2) doar replica.
- Ceri să înceapă prompt, să termine propoziția și să lase o mică pauză curată.
- Livrezi fără muzică și fără grafică. Primul take îl testezi (fața, vocea, ochii, buzele, pronunția numelor de produs), apoi folosești aceeași direcție pentru restul. Ții un registru: take / prompt / rezultat.

**H. Agenție de reclame cu MCP** (https://youtu.be/iOwKylW8c5Q)
- Claude Project cu instrucțiuni de „ops manager” + Gmail. Ceri 5 stiluri de reclamă: before/after cinematic, amuzant, testimonial, centrat pe problemă, premium. Fiecare are hook în primele 3 s și CTA la final.
- În fiecare luni: 3 variații noi per client, cu evidența hook-urilor și unghiurilor deja folosite, ca să nu se repete.
- Un agent de QA verifică fiecare video față de profilul clientului (nume, oraș, telefon, afirmații riscante) și îți arată doar ce pică.

---

## 4. Prompting

- **Ancore (repere).** Pentru poziționare dă repere din fundal: fiecare loc legat de un reper (luminator, rafturi, lampă roșie). La contraunghiuri spune explicit ce trebuie să se vadă din acel unghi, altfel modelul pune un perete. Pune poziția fiecărui personaj explicit (https://youtu.be/kFKpcCHkuPI).
- **Hartă de blocaj color-codată.** Pentru plan de sus, generezi în Seedream harta de poziții, fiecare personaj cu o culoare, și o atașezi alături de referințe; în prompt fiecare culoare = un personaj. Lași loc în jurul capetelor pentru rotația camerei (https://youtu.be/kFKpcCHkuPI).
- **Tranziții.** Taie pe acțiune (tap pe telefon) cu aceeași încadrare și aceeași mișcare de cameră; se schimbă doar locația. Ascunde tăietura după spatele unui personaj. Audio: noul ambient intră înaintea imaginii (https://youtu.be/kFKpcCHkuPI).
- **Camera.** Nu scrie „cinematic camera movement” (iese „slop”); dă o listă de cadre ca unui operator. Pentru mișcări complexe, înșiră mișcările cu săgeți (→) (https://youtu.be/OiULPvTJ-0E, https://youtu.be/x0FdaH0fDpQ). Adaugă cuvinte cheie pentru mișcare și lumină (https://youtu.be/XdK93RhPFAo).
- **Un singur cadru continuu.** Dacă împarți promptul pe secunde sau pe „beats”, Seedance face tăieturi. Pentru un plan continuu, descrie-l ca o singură mișcare continuă. Folosește o singură mișcare de cameră în momentele emoționale (https://youtu.be/-scKERL7PK0). (Invers: timestamp-urile sunt bune când CHIAR vrei mai multe cadre într-o generare (https://youtube.com/shorts/cL0RT2OA5Is).)
- **Bloc de layout spațial.** Un bloc separat descrie camera (încăperea) și unde stă camera de filmat. A rezolvat intrarea pe ușa greșită. Când modelul mută obiectele în loc să mute camera, ancorează camera de un element (holul întunecat) și spune „critical” (https://youtu.be/-scKERL7PK0).
- **Emoții, nu doar acțiuni.** Descrie ce simte personajul („heartbroken… atât de încet încât abia pare mers, târât de durere”) plus micro-detalii (buza care tremură). Seedance răspunde bine (https://youtu.be/-scKERL7PK0). Personalitatea scrisă în prompt dă livrarea corectă (https://youtu.be/LUWMI0zy0BQ).
- **Fizica.** Nu scrie „mech punches the monster” (asta e o legendă de poză, nu regie). Scrie ce face forța asupra corpului: greutatea, consecința impactului, urmele vizuale. Așa modelul înțelege masa și impulsul (https://youtu.be/LUWMI0zy0BQ).
- **Style prefix comun** (stil, lumină, culoare, compoziție, audio) la începutul fiecărui prompt, pentru consistență. Ex.: „natural light only, key light from sky and windows only”; audio: „only environmental sound effects, no music, no subtitles” (https://youtu.be/-scKERL7PK0).
- **Failure modes în prompt.** Avertismentele (ex. „nu muta Polaroidul”) se pun ÎN prompt; funcționează mai bine (https://youtu.be/-scKERL7PK0).
- **Anti-plastic la Nano Banana Pro:** „light atmospheric haze”, „film grain”, „crush the blacks” (adâncime de umbră), tonuri mai reci (https://youtu.be/-scKERL7PK0).
- **Look de reclamă:** „commercial shot, shot on RED, anamorphic shot”, la 21:9 (https://youtu.be/AdjllfZuqYM).
- **Fără descrieri de aspect dacă atașezi character sheet.** Dacă promptul descrie prea detaliat aspectul, modelul inventează alte fețe chiar cu sheet-ul atașat. Descrie doar hainele. Dacă atașezi locația, nu o mai descrie în prompt (https://youtu.be/-scKERL7PK0).
- **Prompt prea lung = model copleșit.** Când promptul devine foarte lung din editări succesive, „scrap and start from scratch” (https://youtu.be/-scKERL7PK0).
- **Exemple simple:** dacă un concept merge greu din text, arată-l cu o imagine de referință (https://youtu.be/Yte-UGhYkPQ).
- **Prompt scurt pentru acțiuni cunoscute:** „reindeer dancing” a mers din două cuvinte în Kling (https://youtu.be/AdjllfZuqYM). Termenul „K-pop” a fost suficient pentru coregrafie (https://youtu.be/LUWMI0zy0BQ).
- **Brief pentru asistent:** descrii rezultatul final, numești fiecare fișier de input și rolul lui, stilul, unde se salvează, ceri proiecte editabile, ceri verificarea afirmațiilor tehnice (https://youtu.be/NuvA32_dmtg).

---

## 5. Probleme și soluții

| Problemă | Soluție | Sursa |
|---|---|---|
| Personajul își schimbă locul între cadre / se încalcă regula de 180° | wide inițial ca keyframe + locuri legate de repere; blocaj 3D | https://youtu.be/kFKpcCHkuPI, https://youtu.be/OiULPvTJ-0E |
| La plan de sus apare un loc în plus la masă (4 în loc de 3) | hartă color-codată generată separat și atașată | https://youtu.be/kFKpcCHkuPI |
| Contraunghiul pune perete în loc de peisaj | descrii explicit ce e la cameră, ce e în mijloc, ce e în fundal | https://youtu.be/kFKpcCHkuPI |
| Tăieturi nedorite într-un plan „continuu” | scoți împărțirea pe secunde/beats; „one continuous shot” | https://youtu.be/-scKERL7PK0 |
| Modelul mută obiectele (frigiderul) în loc să mute camera | ancorezi camera de alt element; reurci referința; arăți poziția pe sheet („colțul dreapta-sus al panoului de sus”) | https://youtu.be/-scKERL7PK0 |
| Uși/camere inventate, decor care se „rupe” | keyframe-ul are prea multe elemente: muți camera mai în interior; elimini din referință ce încurcă | https://youtu.be/-scKERL7PK0 |
| FPS scăzut (~12–18 în loc de 24), sacadat | scrii explicit „24 fps” + style prefix la început; în post tai cadrele duplicate (pierzi audio, rămâne B-roll) | https://youtu.be/-scKERL7PK0 |
| Eroare NSFW fără motiv evident | imaginile trecuseră de IP check, deci problema era în prompt: îl rescrii; eșecurile nu se taxează | https://youtu.be/-scKERL7PK0 |
| Apucă obiectul greșit (Polaroidul greșit) | îl numești explicit „image 4”; adaugi obiectul în keyframe printr-o editare (GPT Image 2 a reușit unde Nano Banana a stricat fețele) | https://youtu.be/-scKERL7PK0 |
| Referința în plus „trage” cadrul (alunecare spre imaginea frigiderului) | scoți referința de care nu ai nevoie | https://youtu.be/-scKERL7PK0 |
| Seedance adaugă muzică deși ai interzis-o | nu se poate separa (un singur track); alegi take-ul unde se poate folosi; interzici muzica din style prefix | https://youtu.be/-scKERL7PK0 |
| Imagine plasticoasă în Nano Banana Pro | haze / film grain / crush blacks; sau editare în GPT Image 2 | https://youtu.be/-scKERL7PK0 |
| Piele prea netedă, lumină dură (Soul Cinema) | corecție în Seedream 5.0 Pro | https://youtu.be/kFKpcCHkuPI |
| Kling/Veo „narează” când nu e nimeni în cadru | scrii în prompt că nu vorbește nimeni | https://youtu.be/XdK93RhPFAo |
| Prea multe instrucțiuni → morphing (Kling, Veo) | mai puține acțiuni pe clip | https://youtu.be/x0FdaH0fDpQ |
| Mișcare agresivă de cameră cu medii noi → halucinații / scară greșită (personaj minuscul) | evită-le sau dă end frame / blocaj | https://youtu.be/x0FdaH0fDpQ |
| Referința nu se etichetează automat când adaugi imaginea după prompt | lipești din nou promptul | https://youtu.be/-scKERL7PK0 |
| Take generat care sare cuvinte sau se termină brusc | asculți la viteză normală, compari cu scriptul; regenerezi doar take-ul acela | https://youtu.be/NuvA32_dmtg |

---

## 6. Noutăți recente (2026)

| Data | Ce e nou | Sursa |
|---|---|---|
| 2026-01-08 | Seedance 1.5 pe Higgsfield (720p, end frames) | https://youtu.be/x0FdaH0fDpQ |
| 2026-02-04 | Vibe Motion (motion design editabil, bazat pe skill-uri Claude) | https://youtu.be/yvuVH6Zg5Vk |
| 2026-03-07 | Extend video fără limită de lungime | https://youtube.com/shorts/pThgGdlO58I |
| 2026-04-11 | Seedance 2.0 global, fără waitlist; Cinema Studio 3.0 | https://youtube.com/shorts/xQF-EFnB3Gw, https://youtube.com/shorts/4h-mLecRgf4 |
| 2026-05-27 | Agent care postează pe Instagram pe pilot automat, prin MCP + skills | https://youtube.com/shorts/JaEpj9OB3Ek |
| 2026-05-28 | Cinema Studio 3.5 | https://youtube.com/shorts/gXpInRWSiSc |
| 2026-06-05 / 06-16 | Plugin gratuit Premiere/After Effects; plugin DaVinci Resolve | https://youtube.com/shorts/G12IJY2p7QY, https://youtube.com/shorts/H1hQFOV0LAI |
| 2026-06-29 | Seedance 2.0 în 4K, video-to-video pe filmare reală | https://youtu.be/Yte-UGhYkPQ |
| 2026-07-29 | MCP unlimited pentru utilizatori noi (temporar) | https://youtu.be/iOwKylW8c5Q |
| 2026-08-28 | Plugin Blender + bridge spre Claude (blocaj 3D → Seedance) | https://youtu.be/OiULPvTJ-0E |
| 2026-08-30 | Seedance 2.5 | https://youtube.com/shorts/zzGw5PHOvj0 |
| 2026-09-04 / 09-06 | Plugin ChatGPT; GPT-6 Astra + MCP: un video întreg dintr-un chat, inclusiv prezentator generat dintr-un clip scurt | https://youtube.com/shorts/WzkUQoynkFQ, https://youtu.be/NuvA32_dmtg |
| 2026-10-07 | Tutorial Seedance 2.5 în Cinema Studio, cu Soul Cinema + Seedream 5.0 Pro | https://youtu.be/kFKpcCHkuPI |
