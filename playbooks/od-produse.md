# OD — 4 produse dintr-o operațiune reală de organic dropshipping

Sursa: arhiva `library/sources/od-full/` (copie a drive-ului unui operator, „Daniel”, dată unui partener; instantaneu din 2026-10-07). Prescurtare în tot fișierul: **`od/` = `library/sources/od-full/`**.
Fișiere citite: `od/CLAUDE.md`, `od/x_context/{business,decisions,priorities}.md`, `od/x_instructions/{01,03,05,06}_*.md`, `od/x_systems/hooks/{hooks_board.html,text_on_screen.txt}`, `od/x_systems/product_finder/board_data.json`, toate `competition/*/data.md`, toate `content/_board_thumbs/board_data.json` (structură + toate benzile, eșantioane de carduri), `content/lost_takes.txt`, `product_images/**/box_spec.md`, eșantioane de `content/video_N_assets/prompts.md` (TheXmasGlow v30; perdele v1, v6, v34; MerryGlow proiector v1, v6; Swanlift v1–v16 antet + v8 și v16 complet), `od/x_research/genjutsu_motion_transfer_vs_object_swap.md` (rezumat).
Data: 10 oct 2026.

Regula playbook-urilor: aici intră doar ce e în fișiere. Ce e deducția mea e marcat **[ipoteză]**. Fișierele media (.mp4, .png) nu sunt în arhivă: descrierile vizuale vin din prompturi și din notele de pe board-uri, nu din vizionare.

---

## 0. Pe scurt

| Produs | Magazin | Videouri | Preț | Rezultat (cifră din sursă) | Metodă |
|---|---|---|---|---|---|
| Proiector de Crăciun (dom alb) | TheXmasGlow | 30 | $79.99 | **$25,817, 259 comenzi în 6 zile** (20–25 sept); ~$2k în primele 24 h | GPT Image 2/2.5 → Seedance 2.5, 7 cadre |
| Perdea LED (pixel, cu aplicație) | MerryGlowUSA (al unui partener) | 35 | $59.95, apoi pachete $79.99 / $139.99 / $189.99 | **126 comenzi** (117 card = $10,965.60; 8 PayPal $899.25 neîncasate); ~18M views pe conturi | GPT Image 2 (+ Nano Banana) → Seedance 2.5, 7–10 cadre |
| Proiector de Crăciun (cilindru pe suport U) | MerryGlowUSA | 8 | $129.99 | **0 vânzări, „dead”** | aceleași hook-uri reciclate + 4 cadre B-roll; 1 hook Genjutsu |
| Sutien corector de postură | Swanlift | 16 (recast) | — (nu apare) | încă fără cifre (postare pornită 6 oct) | **Genjutsu motion transfer** pe reel-urile competitorilor |

Surse: `od/x_context/business.md`, `od/x_instructions/01_business_and_model.md`, `od/x_context/decisions.md` (2026-09-27, 2026-10-06).

Model comun (`od/x_context/business.md`): **doar organic, fără reclame plătite**; videouri UGC generate cu AI, ~11–18 s, 9:16, postate pe IG/FB/TikTok (YT Shorts abandonat la Swanlift) → „Link in bio” → Shopify. „Fiecare video = C01 hook (4–5 s, decide tot) + B-roll care spune o poveste fixă pentru acel produs.” Montaj în CapCut (text + melodie). Public: „Christmas moms / parents / Christmas lovers”, SUA întâi.
Observația lor despre cele două câștigătoare (o observație, nu o regulă): decor de Crăciun, un „wow” vizual într-o cameră întunecată care merge **fără sunet**, cost ~$2–3, vândut cu $60–80, ușor și mic la transport.

---

## 1. THEXMASGLOW — Christmas Projector (câștigătorul)

### De ce a fost ales
- Competitori observați pe 16–18 sept: conturi **noi-nouțe** cu 1–2M views pe un singur reel în câteva zile (`od/THEXMASGLOW - CHRISTMAS PROJECTOR/competition/*/data.md`; rezumat în `od/x_context/business.md` §Competitors).
- Cost ~$2–3 la fabrică, ~$8–10 livrat în SUA prin agent; vândut cu $79.99 (`od/x_context/business.md`). Furnizor final: Zendrop (decizia din 2026-10-01, `od/x_context/decisions.md`).

### Produsul și poziționarea
- Proiector alb tip dom, model XZTYD-01, **disc negru de plasă pe capac** (lumina iese pe sus), stativ alb separat cu 4 picioare, USB-C, fără baterie, discuri de film de Crăciun interschimbabile, telecomandă roșie (`od/x_context/business.md`, `od/THEXMASGLOW - CHRISTMAS PROJECTOR/product_images/box_spec.md`). Regula lor: „descrie produsul exact cum e unitatea reală”.
- Cutie: verde festiv, tuck-top 15×15×24 cm (mărită de la 12×12×20 la cererea lui Daniel), **fără fereastră**, text: `THEXMASGLOW` / `CHRISTMAS LIGHT PROJECTOR` / `16 Patterns · Remote Control · Timer` (`box_spec.md`).
- Promisiunea vizuală: camera întreagă (pereți + tavan) „îngropată” într-o proiecție animată de Crăciun; copiii fascinați.

### Competitorii (date Apify, `competition/<cont>/data.md`)
| Cont | Ce s-a măsurat | Cel mai bun reel | Durate | Audio | CTA în caption |
|---|---|---|---|---|---|
| @aquawish.us | cont nou, 6 reel-uri în 5 zile, total 3.48M views | 2,070,277 views / 3,453 comentarii | 13.5–15.5 s | original audio | „Comment “BLUE” to get yours today! 🎁🎅🏻” → apoi „Comment « Santa » if you want one!🎁🎅🏻” |
| @hollyglow.co | 22 reel-uri în 10 zile, 3.68M total | 1,237,900 / 92,324 likes | 11.0–13.1 s | „Last Christmas” (Wham!, Sophie Ghosn) + original | „Comment “Xmas” if you want this 🫣🎄✨” · „TAG A CHRISTMAS LOVER! 😱🫣” |
| @merrybeam.official | 46 reel-uri în 15 zile, 4.55M total | 1,903,012 / 146,260 likes | 10.1–14.3 s | original + „Somewhere in My Memory” (Home Alone) | „Comment "BEAM" and we'll send you the link! ✨ Turn any wall into a cozy Christmas window 🎄❄️” |
| @mymerryview | 42 reel-uri în 16 zile, 2.64M total | 1,521,290 | 12.1–17.2 s | „Rockin' Around The Christmas Tree” (Brenda Lee), „Last Christmas” | „Comment” Tree” if you want one😱🎄” |

Ce le merge (din cifre): volum mare (2–3 reel-uri/zi), 10–17 s, melodie clasică de Crăciun sau audio original, CTA „Comment <CUVÂNT>”; distribuția e extrem de inegală (1 reel face 50–60% din totalul contului).

### Structura video (fixă pe toate cele 30) — `od/.../content/_board_thumbs/board_data.json` (legend + lanes)
Durată 14.21–17.44 s, mediană 15.37 s; export 2160×3840, 30 fps. 7 cadre:

| Cadru | Rol | Ce se vede | Setări |
|---|---|---|---|
| C01 | **Hook** | vezi mai jos (magazin sau „pattern interrupt”) | Seedance 2.5, 1080p, 4–5 s |
| C02 | B-roll 1 — produsul | „Hands on the box”: două mâini pe cutia închisă, pe masă | 720p, 4 s |
| C03 | B-roll 1 | „The projector lifted”: proiectorul ținut în aer deasupra blatului, plasa neagră în sus | 720p, 4 s |
| C04 | B-roll 1 | „The cable going in”: USB-C intră în port | 720p, 4 s |
| C05 | B-roll 2 — payoff | „The door opens on the room”: mâna pe clanță → ușa se deschide pe camera deja în proiecție (2 cadre: start + referință cameră + cameră goală) | 720p, 5 s |
| C06 | B-roll 2 | „The bed bounce”: copil sărind în pat sub tavanul proiectat | 720p, 5 s |
| C07 | B-roll 2 | „The whole Christmas room”: plan larg, doi copii, tot volumul în proiecție | 720p, 4 s |

Varietatea dintre videouri stă **doar** în: camera (stil arhitectural: Craftsman, chalet alpin, Victorian, Japandi, Santa Fe…), tema proiecției (sat de Crăciun, tren, aurora, Polul Nord…), mâinile/puloverul, copiii. Geometria și prompturile rămân aceleași (vezi v30: „Every prompt is the video 24 verified-record prompt of the same slot … pasted verbatim with only the physically different nouns replaced”, `od/THEXMASGLOW - CHRISTMAS PROJECTOR/content/video_30_assets/prompts.md`).

### Hook-urile (C01) — 30 de videouri
| Concept | Hook | Videouri | Text pe ecran |
|---|---|---|---|
| Store discovery | „Store aisle walk → the pallet” (împinge căruciorul, gâfâie, arată, whip-pan pe paletul de cutii) | v1, v3, v26 | `Do not let a Christmas mom see this🎁🎄` (v1) · `Every Christmas mom NEEDS this🎄🎁` (v3) · `Do NOT let a Christmas mom see this🎄🎁` (v26) |
| Store discovery | „Family walk-in → the end-cap” (copilul merge singur la raft) | v2 | `Do NOT let a Christmas mom see this🎁🎄` |
| Store discovery | „Store end-cap reaction” | v7 | `Do NOT let a Christmas mom see this🎄🎁` |
| Pattern interrupt | „Ladder fail — taping Santa up” (lipește un Moș gonflabil de tavan și cade de pe scară) | v4, v5, v6, v11, v16, v18, v23, v28, v30 (9) | `Christmas Decor in 19XX🤮 · Vs.. · Christmas Decor in 2026🎄🎁` |
| Pattern interrupt | „Mezzanine tape — over the railing” | v8, v13, v19 | idem |
| Pattern interrupt | „Plug in the lights → tree fire” (bagă în priză un ghem de beculețe vechi → bradul ia foc, „Oh, shoot”, familia fuge spre cameră) | v9, v12, v17, v22, v27 | idem |
| Pattern interrupt | „Stair hall — reaching for the topper” | v10, v14, v15, v20 | idem |
| Pattern interrupt | „Painting the Christmas mural” / „Ladder — painting the ceiling” | v21, v25 / v24, v29 | idem |

Anii folosiți în text: 1925, 1935, 1955, 1965, 1975, 1979, 1985, 1995 (25 din 30 de videouri au formatul „Christmas Decor in 19XX vs 2026”). Prima variantă: `Christmas Decor in 1965🤮 · Vs.. · Christmas Decor in 2026🤩🎄` (v4).
Cronologie (`board_data.json` → meta Status): v1–v3 (magazin) postate 18–19 sept; din 20 sept aproape numai „pattern interrupt”; prima comandă 20 sept; $25,817 în 20–25 sept. **[ipoteză]** formatul „Decor 19XX vs 2026” a coincis cu vânzările; nu există cifre per video care să o dovedească.

### Cum s-au făcut
- Cadre: `gpt_image_2` (primele) → `gpt_image_2_5` variant `sunburst`, 9:16, 2k, quality medium (1520×2688). Clipuri: `seedance_2_5`, mode `omni_reference`, 720p 4–5 s pentru B-roll, **1080p pentru hook**, `generate_audio true`, `declined_preset_id 24bae836-…` (`od/x_systems/hooks/hooks_board.html`, hook 11 și 14). Upscale: ByteDance Upscale Pro · 2K · 30 fps · preset **AIGC** pe hook, **Common** pe B-roll.
- Referințe: cutia `box_festive_green_g2.png` pe orice cadru cu cutia; `references/ref04.png` (cadru de competitor) ca ancoră pentru capacul negru al proiectorului; cadrul aprobat anterior ca @Image 1 („Copy the FIRST attached reference photo EXACTLY…”).
- Hook „magazin” = imagine copiată după un cadru de competitor (`references/ref01.png`) cu „Change only two things” (femeia, decorul de Crăciun) + un clip de competitor **fără sunet** ca referință de mișcare pentru whip-pan.
- Prompturi video structurate: `AUDIO RULE` sus, `[1] SUMMARY`, `[2] GLOBAL STYLE`, `[3] ASSET ROLES`, `[4] CHARACTERS` (+ COUNT LOCK), `[5] LOCATION`, `[6] FIRST FRAME`, `[7] TIMELINE` pe secunde, apoi BANNED / MOTION GUARDRAILS (exemplu complet: C05 din `video_30_assets/prompts.md` — „AT EVERY MOMENT AT LEAST TWELVE DIFFERENT DRAWN THINGS ARE VISIBLY MOVING”, „at least SIX separate … white smoke columns”, „EXACTLY TWO CHILDREN”, „ONE slow, uninterrupted forward-and-upward glide … about 0.8 metres … about 18 degrees”).
- Proces: două aprobări (cadre, apoi clipuri), **o singură generare pe cadru, apoi review**; nimic suprascris; fiecare reutilizare are linia „Reused from vNN CNN — changed: …” (`od/CLAUDE.md` regula 3).

### Regulile învățate (panourile „Frame rules” / „Clip rules” din `board_data.json`)
- „Attach the medias, or the prompt is fiction” — un lot întreg a plecat fără referințe atașate și a fost facturat.
- „A framing reference leaks its content” — spune explicit că camera/oamenii/culorile sunt noi, altfel primești camera competitorului.
- Două referințe = două roluri numite („the FIRST … for framing, the SECOND … for the product”).
- Descrie referința citind-o din imagine, nu din memorie (2 generări arse pe C04).
- „Anything you do not name gets deleted” — numește tot ce trebuie să rămână.
- **„Children plus sleepwear trips the NSFW filter.”** „Christmas pyjamas” a omorât C5b și C6; „Knitted Christmas jumper and matching lounge trousers” + „wholesome family Christmas scene” trece.
- Proiecția are nevoie de fizică (plată, translucidă, se deformează pe colțuri), altfel iese tapet.
- Ține camera hrănind înapoi propriul cadru aprobat + „CHANGE 1 — …”.
- Variază gradarea între cele 3 cadre de payoff (cald-auriu / albastru).
- Fără text în cadru, niciodată; textul se pune în CapCut.
- Clip: „A video reference imports its own audio” → atașezi copie fără sunet; referința video trebuie să aibă **≥ 2 s**; proza singură nu animă o proiecție (doar un clip-referință mut a mișcat-o); „the take with no video reference won two of seven shots”; C06 a luat 10 încercări, C03 două.

### Ce a mers prost
- `lost_takes.txt`: cadre de hook v8 g1–g4, v9 g1–g5, v10 g1–g6 respinse și pierdute din staging (fără motiv verificat).
- Respingeri tipice (prompts.md): căderi „fake, unnatural” (v24, v29), proiecție care nu acoperă tot tavanul la început (v27/v28 C06), animație prea calmă — Daniel: „smoke must come out of the houses chimneys”, pasăre „looks like it's in real life”, fulgi care par „in the real room” (v30 C05), jumătate de proiector devine roșie la conectare (v26 C04), vopsea care apare „magically” (v21), „a floor tin flips and spills on its own” (v7), „șapte refuzuri `nsfw` la rând” pe gpt_image_2 la un cadru cu mâini/copii.
- Videoul 30 de cadre de ramă albă: multe cadre respinse „wooden frames not covered” (proiecția trebuie să acopere și lemnul).

---

## 2. MERRYGLOWUSA — LED Curtain Lights

### De ce a fost ales
- A venit prin partener, înainte de Product Finder (`od/x_context/business.md` §Finding products). În Product Finder, nișa „LED curtain · Christmas animations” are conturi ca @tryfestilight (66,115 urmăritori, medie 1,286,140 views pe ultimele 20, best 19.1M) și @jollyview.co (78,830 urmăritori, medie 167,554, best 7.55M) (`od/x_systems/product_finder/board_data.json`, produs `pixel_lights`). CTA-urile lor: „Comment “FESTIVAL” if you want your own 😌🎁”, „Comment: “Decor” if you want one!🎄👀”.

### Produsul și poziționarea
- Perdea de LED-uri pe plasă de sârmă neagră, programabilă din aplicație („100+ designs”), montată pe fațadă/garaj/fronton; cutie neagră mată ~55×42×10 cm, **fără fereastră**: `LED CURTAIN LIGHTS` / `Create Your Own Magic` / panglică `BEST SELLER` / iconuri `DIY Designs / App Control / IP65 Waterproof / Timer Function / Connectable` (`od/MERRYGLOWUSA - LED CURTAIN LIGHTS/product_images/box_nowindow/box_spec.md`).
- Poziționare: casa ta devine „ecranul” străzii; vecinii se opresc. Titlurile de story (`content/stories/_overlay_script.py`): `100+ DESIGNS. ONE TAP.` · `THE HOUSE EVERYONE STOPS FOR` · `THE NEIGHBOURS JUST STAND THERE` · `THIS IS THE PART YOU DO IT FOR` · `UP IN 20 MINUTES` / `ONE PERSON. NO TOOLS.` · `SNOW. RAIN. ICE.` / `IP65 rated - leave it up all season` · `SAME HOUSE. ONE BOX.` · `HE'LL REMEMBER THIS ONE` · `STORES ARE ALREADY OUT` / `WE STILL HAVE STOCK` · `FOUND THE EXACT KIT`.

### Structura video
35 de videouri, 6–19 sept; 12.75–18.04 s (mediană 15.07 s). Legend: **Hook → B-roll 1 „getting & mounting” → B-roll 2 „showcasing, the payoff”** (`board_data.json`). Trei generații de structură:

1. **v1–v11 (8–10 cadre)**: hook → `Store checkout` (POV self-checkout, „proof of retail”) → `Unboxing` → `Ladder install` → `Walk along wall` (scara) → 3–4 cadre cu animații pe fațadă (`Reindeer sleigh`, `Snowman cheers`, `Fireworks wall`, `Garage + phone app`, `Full house display`).
2. **v20–v33 (7 cadre, „same six B-roll beats”)**: hook → `Box over the couch` → `Fixing it to the wall` (scăunel, ghem de plasă în mână) → `Curtain up, lights off` (telefon cu aplicația, perdea stinsă) → `Path`/`Walkway approach` → `Neighbours at the garage` (siluete) → `Drive-by, car window`. Din v27: „gag” în trei bătăi pe beculețe (Moș Crăciun cu bere, renii în grevă, bătaie cu bulgări, Moșul blocat în horn, pisica dărâmă bradul, Moș vs. Grinch).
3. **v34–v35 (8 cadre)**: hook → `Scanning it at the till` → `Opened it in bed` / `on the couch` (POV) → `Up the ladder, wide` → `Same install, closer` → telefon + animație → 2 gag-uri pe fațadă.

### Hook-urile (meta „Hook” din `board_data.json`)
| Video | Hook (acțiunea) | Text pe ecran |
|---|---|---|
| v1 | „You drive past and the whole gable is a giant winking Santa.” | `Do NOT let a Christmas Lover see this..🎄🤶` |
| v2 / v5 | Televizor lipit cu bandă în geam („the concepts”), apoi produsul real | `The concepts🤮 vs` / `The concepts😂` |
| v3 | „A crowd stripping a warehouse pallet — social proof up front.” | `Christmas Parents...don't walk RUN to Costco...🤶🎄` |
| v4 | „She sees the box in-store and drops her drink” | `Every Christmas Lover NEEDS this!😨🎄` |
| v6 | „POV — the box lands in your lap” (refăcut după un reel de competitor) | `Every Christmas lover NEEDS this🎄🤶` |
| v7 | doi angajați trag pânza neagră de pe palet, mulțimea vede prețul | `Christmas Parents🎄🤶 x IKEA` |
| v8 | „You’re in bed and he walks in holding the box out to you” | `Every Christmas Lover NEEDS this..😱🤶` |
| v9 | raft întreg plin cu produsul | `Every Christmas Lover NEEDS this...😱🤶` |
| v10 | clienți care se bat pe ultimele cutii | `Every Christmas Lover NEEDS this...😱🤶` |
| v11 | „You round the corner and the entire house is a screen.” | `Christmas Parents...don't walk RUN to Costco...🤶🎄` |
| v12, v16, v20–v23, v25–v27, v30 | gonflabile care cad / nu se umflă / bărbat care cade de pe acoperiș, decor vechi urât | `Christmas Decor in 1965🤮` |
| v13 | „She can’t keep a straight face about what’s in the box” (3-2-1 pe pat) | `Christmas Parents... don't walk, RUN to Costco..🤶❄️` |
| v14 | „Two employees, one white sheet” (3-2-1 în magazin) | `Christmas Parents🤶❄️ X IKEA` |
| v15 | „Spotted on the shelf at $59.99” (POV degete) | `Do NOT let a Christmas Lover see this..🤶❄️` |
| v17 / v18 | cafea în mână pe culoar / pânză albă smulsă de pe palet | `Christmas lover don't walk RUN to costco...🎄🤶` |
| v19 | coadă în zăpadă la depozitul albastru-galben | `Christmas Parents🎄🤶 x IKEA` |
| v24, v28 | aruncă ghemul de beculețe pe canapea / 3-2-1 în depozit | `Every Christmas mom NEED THIS🤶🎄` |
| v29 | (nou gag: Moșul atacat de oameni de zăpadă) | `Every Christmas lover NEED THIS🤶🎄` |
| v31–v34 | pisica vs. bradul / Moș vs. Grinch / copilul scapă matcha-ul | `Do NOT let a Christmas lover see this🤶🎄`, `Do NOT let a Christmas mom see this🤶🎄`, `Do NOT let a Christmas mom see this🎁🎄` |
| v35 | strada privește, fațada se aprinde, Moșul pixelat face cu mâna | `Every Christmas lover NEEDS this🎁🎄` |

### Cum s-au făcut
- `gpt_image_2` 2k medium 9:16 (1520×2688) + `nano_banana_2` (raportat ca `nano_banana_flash`, rol `image_references`) pe unele cadre; clipuri `seedance_2_5` 720p 4–5 s (v7: 1080p), un cadru cu `kling3_0_turbo` (garaj + aplicație) (`board_data.json` tags + panoul „Model settings in use”).
- Referințe obligatorii: packshot-ul fără fereastră `box_nowindow_g5.png`, interiorul cutiei `box_interior_g5.png`, și **close-up-ul cu perdeaua stinsă ca REFERENCE IMAGE 1** pe orice cadru cu perdeaua + blocul „anti-panel” lipit textual (altfel produsul arată ca un ecran, nu ca beculețe).
- „Playbook — what holds a shot together” (panou din `board_data.json`): leagă cadrele prin job_id, nu prin adjective; fiecare referință primește un rol în primele două rânduri; „SURFACE OVERRIDE” în loc să editezi blocul; spațiul gol trebuie descris ca obiect + listă de interdicții („An empty sofa produces a full one”); „Switched off renders as absent”; descrie priza mâinii, nu obiectul; „NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS”; **„Comedy as a situation, not a punchline”**; culoarea peretelui e decizie de lumină (becurile albe dispar pe cărămidă neagră); „CHANGE ONE THING ONLY”; clauza de look („Hyper realistic, crisp real-estate-photography clarity … NOT cinematic …”).
- Daniel cere loc liber sus pentru text: „I want a little space at the top so when I add the text inside CapCut it will look good”.

### Ce a mers prost
- `ip_detected` ×4 pe cadrele v32 C05–C07 și v33 C07 („DEAD”) din cauza personajului verde tip Grinch; rezolvat în „RUN 6” cu un **personaj original** redesenat („short and stocky, SMOOTH hairless kelly-green skin … NOT tall/lanky, no fur, no long grinning muzzle, no pointed ears”) (`video_34_assets/prompts.md`, `video_32/33`).
- Respingeri: „I want all of them to fall. Right now it's looking very fake”, „she is not jumping on the bed”, „the box looks very unrealistic”, „the man should put some nails with the tools in his hand”, „the family should normally turn around, not jumping, and the cheering at the end with the applause it's very fake”, „it's winter outside so the delivery guy must be dressed properly”, „the crotch it's levitating” (prompts.md v24–v35).
- `lost_takes.txt`: 11 take-uri distruse la 2026-09-18 de un pas greșit de migrare a numelor (nu de AI) — lecție de arhivare.
- PayPal: 8 comenzi ($899) neîncasate → PayPal oprit (`decisions.md` 2026-09-25).

---

## 3. MERRYGLOWUSA — Christmas Projector (eșecul)

- Produs: proiector cilindric alb pe suport în U, grilă frontală neagră cu lentilă, telecomandă neagră; cutie verde cu artă „UBU” (nume vechi, redenumit 2026-09-23) (`od/.../video_6_assets/prompts.md`, `decisions.md`). Preț **$129.99**. Rezultat: **„Dead: no sales”**, oprit 2026-09-27 (`business.md`, `decisions.md`).
- 8 videouri, 22–26 sept, 10.87–14.54 s (mediană 12.75 s). Structură de **5 cadre**: Hook → `Hands on the box` → `Projector upright, lens up` → `Remote click → Christmas windows` (pan stânga spre reveal) → `Christmas view from bed` (`board_data.json`).
- Hook-uri reciclate de la TheXmasGlow (Moș gonflabil lipit, stea pe bradul din hol, priza cu beculețe, Moș lipit de pe palier, cutia luată de pe raft) + v6: **hook Genjutsu** `hf_mult_motion_control` 480p 5 s după un reel viral: camion supraîncărcat cu cutii lovește pasarela, cutiile zboară spre cameră, „cut down to our carton in a brown box” (prompt complet pe cardul v6 C01). Daniel l-a ales pe g1 („I like it better”).
- Texte: `Christmas Decor in 1995🤮`, `Christmas Decor in 1965🤮`, `Christmas Decor in 1985🤮`, `Do NOT let a Christmas lover see this🎄🎁`, `Christmas Decor in 1995🤢`, `Christmas Decor in 1975🤢`.
- Lecții tehnice: `gpt_image_2_5` schimbă singur rolul media `image` → `image_references`; o generare a picat pe „Out of credits … Shared workspace” (v1 C01); `ip_detected` pe un C05 (`lost_takes.txt`).
- **[ipoteză]** de ce n-a vândut: același format și aceleași hook-uri ca TheXmasGlow, dar preț de 1.6× ($129.99 vs $79.99), cutie cu artă veche și un produs care proiectează „ferestre” pe un perete, nu camera întreagă. Arhiva nu dă nicio cifră de views pentru acest magazin, deci nu se poate separa prețul de conținut.

---

## 4. SWANLIFT — Posture Corrector Bra (primul produs non-Crăciun, metoda Genjutsu)

### De ce a fost ales
- Product Finder, categoria „Health & beauty” → „Posture-corrector bras” → varianta „Pull-over posture bra with front hook band” (`od/x_systems/product_finder/board_data.json`, decizia din 2026-10-05 că @thevareny și @backalign.official vând același sutien).
- Regula lor de alegere din 2026-10-06: **doar performanța video** (media ultimelor 20 de videouri, mediana, trendul săptămânii, sezonul rămas); fără punctaj pentru potrivirea cu AI sau numărul de magazine, „competition is not a problem” (`decisions.md`).
- Nume de brand găsit pe 2026-10-06 (`swanlift`); bio: „The bra that fixes your posture 🦢”; handle `swanliftofficial` peste tot; IG + TikTok + FB; același video și caption pe toate; fără comentariu fixat; 3 reel-uri/zi din ziua 3 (`decisions.md` 2026-10-06).

### Produsul
Sutien fără sârmă, decolteu adânc în V, bretele late, cupe mulate, spate deschis cu decupaj rotund („keyhole”), două benzi lungi elastice care se încrucișează la spate și se închid în față sub bust cu cârlige; culori: leopard, nude, negru (blocul de produs din `SWANLIFT - POSTURE CORRECTOR BRA/content/video_8_assets/prompts.md`). Pozele de produs vin de pe Pinterest (listări AliExpress, fețe tăiate) pentru că `product_images/` e gol.

### Competitorii (`competition/*/data.md`, scrape 2026-10-05, ultimele 30 de zile)
| Cont | Limbă / piață | Reel-uri în 30 zile | Best reel | Durate | Ce face |
|---|---|---|---|---|---|
| @gercekform | TR | 18 | **9,874,973** (12,537 comentarii) | 18–37 s | mărturie la persoana I („BUNU İLK GİYDİĞİMDE GÖZLERİME İNANAMADIM…”), plată la livrare, transport gratuit, „%60 indirim” |
| @alynne.us | EN (SUA) | 96 | **9,724,399** (291,462 likes) | 32–36 s | probă vorbită, o singură priză, femeie ~50 („Finally gave the viral ALYNNE Back Support Bra a try... and WOW! 🤩”) |
| @thevareny | EN | 121 | **2,418,878** | 12.6–24 s | montaj rapid de probă, culoarea se schimbă la fiecare tăietură, text „POV:” ars în imagine |
| @backalign.official | EN | 7 | ~1.9M (age-restricted) | 8.8–22 s | explicație „kyphosis” vorbită, subtitrare cuvânt cu cuvânt, „33% OFF today. Link in bio” |
| @the_vitalys | ES | 27 | 710,112 | 8–10 s | demonstrație mută pas cu pas, nude/negru alternat |
| @marlein.co | ES | 55 | 330,233 | 8.8–20 s | descoperire în magazin → probă; text ars în spaniolă |
| @posture.corrector.hub | EN | 4 | 191,706 | 26–41 s | descriere lungă SEO pentru „older women” |
| @velossamco | TR | 11 | 68,728 | 13–27 s | unghi cadou pentru mamă („Anneme sütyen aldığımı sanıyordum…”) |

Total pe cele 82 de reel-uri cele mai bune: vezi `competition/all_competitors_ranked/data.md`. Observat: cele două reel-uri de ~10M sunt **lungi (27–36 s), vorbite, la persoana I**; reel-urile scurte mute (8–13 s) adună sute de mii, nu milioane.

### Ce s-a făcut: 16 „recast-uri” Genjutsu (board în coloane, `board_data.json` layout `columns`)
Fiecare video = un reel de competitor (top 36 din 82) refăcut cu **altă femeie + altă cameră** (din Pinterest, skill `od/x_instructions/skills/pinterest-casting.md`), păstrând mișcarea, tăieturile și timpii. Fără cadru de start; o singură aprobare (clipul) după aprobarea referințelor.

| V | Reel sursă | Views sursă | Text ars în reel-ul sursă (EXACT) | Stare |
|---|---|---|---|---|
| 1 | @alynne.us DdjVHAUugh- | 9.7M | — (vorbit) | partea 1 refuzată nsfw ×6; partea 2 OK |
| 2 | @thevareny DdvzMUoovet | 2.4M | `POV: your back has 30 years on your actual age.. 😮‍💨` | scos de Daniel („I still don't like it”); rularea neagră pică ×4 |
| 3 | @backalign.official Dd3e19aO65r | ~1.9M | subtitrare: „Have you ever seen this happen to women as they age… It's a condition called kyphosis… This posture bra goes over your… It comes in black and tan…” | clip pentru review |
| 4 | @the_vitalys Dc6gNS1KQvi | 710K | — | take 6 (cerut „hyper realistic character”) |
| 5 | @alynne.us Dd5KJHlOX7M | 433K | — | 2 părți (peste 30 s) |
| 6 | @marlein.co Dd6jTEIM-Eh | 330K | `CHICAS que siempre van encorvadas... TENÉIS que ver esto! 😭😮` → `Se pone en segundos ✨` → `Espalda recta sin pensar en ello 🙌` | cutii fără brand |
| 7 | @the_vitalys DdJvhwQKU9x | 295K | — | take 1 respins |
| 8 | @thevareny Ddg8W9eIHLA | 274K | `POV: you realize this is not a regular bra.. 😮‍💨` | trecut din prima |
| 9 | @marlein.co DdwvnJdMgfm | 251K | `Mucho tiempo con dolor de espalda hasta encontrar esto ❤️😮‍💨` | take 1 respins: „the bra color change it's very weird and fake” |
| 10 | @marlein.co DdroE93MnPx | 214K | — | nsfw ×5 până s-au tăiat secundele cu piele goală |
| 11 | @thevareny DdrfZrYogDl | 209K | `The perfect modest gym bra doesn't exist..` | 3 rulări |
| 12 | @the_vitalys DdZPCKsKaNv | 206K | — | tricoul apare/dispare la tăieturi |
| 13 | @gercekform DdWgodhFPg5 | 196K | `SAATLERCE BÖYLE DURDUĞUNUZU FARK ETMİYORSUNUZ!` (…) | versiune tăiată 14.2 s (întregul refuzat nsfw ×2) |
| 14 | @thevareny DdlrbzqoVcW | 182K | — (caption: „if you have a bigger chest this specific feeling needs no further explanation..”) | fără prim-planuri frontale (refuzate) |
| 15 | @thevareny DdhBZveIPNK | 181K | `POV: I found the only thing that can save my posture 😮‍💨` | toate 3 rulările din prima |
| 16 | @thevareny DdWBcKWof1b | 159K | — (caption „Posture up. Head high. Let them watch.”) | test pe alt cont, prompt nearhivat |

Sursa tabelului: antetele `content/video_N_assets/prompts.md` (N = 1–16) și `board_data.json`.

### Cum s-au făcut (rețeta)
- Unealta: **Genjutsu motion transfer `hf_mult_motion_control`, 720p**, max 30 s pe rulare (de aceea v1 și v5 sunt împărțite la o tăietură naturală). Atașamente, în ordine: video sursă (@Video1), femeia (@Image1), camera (@Image2), sutienul față (@Image3), sutienul spate (@Image4).
- Promptul fix (exemplu v8, cuvânt cu cuvânt în `video_8_assets/prompts.md`): „@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room…” → blocul de **motion lock** („Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing…”) → „Recast the woman as the woman from @Image1 … Take only her face, hair, skin and body from @Image1; her clothes come from this prompt” → blocul de produs → camera nouă → „Photorealistic handheld iPhone footage … No text of any kind anywhere in the frame … @Video1 has text burned into the picture; do not copy it”.
- Varianta „ultra-real” (v1 take 6): „Hyperrealistic, natural, unedited iPhone video … like a real person's TikTok: real skin with pores … no beauty filter, no skin smoothing, no glow, no cinematic colour grading …”.
- **O rulare per culoare de sutien** („In this whole clip the bra is leopard and only leopard … it never changes colour, even where the bra in @Video1 has a different colour”), apoi lipite înapoi pe tăieturile originale ale reel-ului. Motiv: schimbarea de culoare într-o singură rulare a ieșit „very weird and fake” (v9).
- Casting: femei generate/realiste ~30 de ani sau de aceeași vârstă/tip de corp ca originalul (50+, plus-size), „no real person's face goes into a bra ad”; camera „lived-in, warm … but a different, nicer room” (`video_1`, `video_8`).
- Sunetul: Genjutsu **păstrează sunetul reel-ului sursă** (inclusiv vocea) → se înlocuiește în CapCut.
- Upscale final: ByteDance Upscale Pro · 2K · 30 fps · AIGC → `content/upscaled_videos/video_N.mp4` (`decisions.md` 2026-10-06).

### Ce a mers prost
- **NSFW** e problema principală: orice secundă cu piele goală (bandou + piept, sutien nude privit din față, mâini pe cupe) → refuz; schimbarea promptului („A matter-of-fact product demonstration … filmed in a modest, non-sexual way”) sau a femeii **nu** a ajutat; doar **tăierea acelor secunde din video-sursă** a ajutat (v1, v10, v13, v14). Refuzurile nu au consumat credite.
- Haine din poza femeii „scapă” în clip: tricoul alb/negru din poză apare sub sutien într-o culoare și dispare în alta (v4, v11, v12) → regula: poza femeii cu haine neutre/ascunse și prompt „her clothes come from this prompt”.
- Erori Higgsfield (nu refuzuri) pe rularea neagră v2 ×4.
- `lost_takes.txt`: v2 take 6 scos definitiv de Daniel.
- Arhivă incompletă la v16 (făcut pe alt cont, fără prompt) — marcat explicit ca gol, nu reconstruit.

---

## 5. Tipare comune între produse

**Durate și ritm.** Videourile proprii: 10.9–18 s (TheXmasGlow mediană 15.37 s, perdele 15.07 s, MerryGlow proiector 12.75 s). Hook 4–5 s, cadre B-roll 4–5 s → 5–10 tăieturi pe video, fiecare cadru o singură acțiune (`board_data.json` din cele 3 produse). Competitorii de Crăciun: 10–17 s. La Swanlift lungimea urmează reel-ul copiat (7–35 s); reel-urile de ~10M ale nișei au 27–36 s.

**Structura.** Hook (problemă/accident sau descoperire în magazin) → produsul în mână (cutie, scoatere, montare/conectare) → **payoff vizual mare** (camera/casa transformată, oamenii reacționează) → final pe payoff. Nu există un cadru de CTA în video; CTA-ul e în caption/bio („Link in bio”; competitorii: „Comment <WORD>”).

**Hook-urile (4 concepte dovedite, `od/x_systems/hooks/hooks_board.html`, 14 hook-uri):**
1. *Store discovery* (01–07): cineva găsește produsul pe raft/palet; „believability is the whole trick”. Cel mai portabil: 03 „Store shelf wall” — „Use this one first when testing a new product”.
2. *3-2-1 reveal* (08–09): cearșaf/pătură trasă pe numărătoare; 5 s obligatoriu (la 4 s se pierde a treia numărătoare).
3. *Gifting POV* (10): cutia îți cade în poală; camera = cel care primește.
4. *Pattern interrupt* (11–14): decorul merge prost (cade de pe scară, bradul ia foc). **Produsul nu apare în hook** → portabil pe orice produs; hook 14 portat de 3 ori, toate din prima.

**Textul de pe ecran (`od/x_systems/hooks/text_on_screen.txt`).** Trei familii, toate cu identitate în primele cuvinte („Christmas mom / Christmas lover / Christmas Parents”) și 1–2 emoji: interdicție („Do NOT let a … see this”), nevoie („Every … NEEDS this”), contrast în timp („Christmas Decor in 19XX🤮 · Vs.. · Christmas Decor in 2026🎄🎁”). La Swanlift (de la competitori): „POV: …” + emoji „😮‍💨”.

**Sunet.** Melodia nu e înregistrată nicăieri la ei („Song: not recorded” pe toate benzile); prompturile cer doar sunet de cameră, fără muzică (muzica se pune în CapCut). Competitorii: „Last Christmas”, „Rockin' Around The Christmas Tree”, „Somewhere in My Memory” sau audio original.

**Producție.** O generare pe cadru, apoi review uman; două aprobări (cadre, apoi clipuri); copierea textuală a promptului aprobat și schimbarea doar a substantivelor; fiecare referință cu rol numit; fără text ars; tot ce se mișcă trebuie să existe în cadrul de start; timpi pe secunde („0.0-1.5s — …”); interdicții explicite (fără zoom, fără slow motion, fără cut).

**Filtre.** `nsfw`: copii + pijamale, piele goală în sutien. `ip_detected`: personaje recognoscibile (Grinch). Soluții: alte cuvinte pentru haine, tăiat secundele problemă, personaj original.

---

## 6. Biblioteca de hook-uri (text exact, EN)

Declanșatorii au denumirile din `playbooks/carti-marketing-psihologie.md` §2. Coloana „Folosit / cifră” spune doar ce e în sursă.

| Produs | Hook text (exact) | Tip (concept) | Declanșator psihologic | Folosit / cifră |
|---|---|---|---|---|
| TheXmasGlow, perdele, MerryGlow | `Christmas Decor in 1965🤮 · Vs.. · Christmas Decor in 2026🎄🎁` (și 1925–1995) | Pattern interrupt + before/after | Contrast · Umor / pattern interrupt | 25/30 videouri TheXmasGlow, 10/35 perdele, 6/8 MerryGlow |
| TheXmasGlow, perdele | `Do NOT let a Christmas mom see this🎄🎁` | Store discovery / reveal | Curiozitate / buclă deschisă · Identitate „oameni ca mine” | TheXmasGlow v1, v2, v7, v26; perdele v32–v34 |
| perdele, MerryGlow | `Do NOT let a Christmas Lover see this..🎄🤶` | Drive-by / store | Curiozitate · Identitate | perdele v1, v15, v31; MerryGlow v5, v6 |
| TheXmasGlow, perdele | `Every Christmas mom NEEDS this🎄🎁` / `Every Christmas mom NEED THIS🤶🎄` | Store / interrupt | Identitate · FOMO | TheXmasGlow v3; perdele v24, v28 |
| perdele | `Every Christmas Lover NEEDS this...😱🤶` | Store shock / shelf wall / rush | Identitate · Dovadă socială (rush) | v4, v6, v8, v9, v10, v35 |
| perdele | `Christmas Parents...don't walk RUN to Costco...🤶🎄` | Store rush / drive-by | FOMO · Dovadă socială | v3, v11, v13, v17, v18 — **brand real, nu se preia** |
| perdele | `Christmas Parents🎄🤶 x IKEA` | 3-2-1 / pallet reveal | Dovadă socială · Curiozitate | v7, v14, v19 — **brand real, nu se preia** |
| perdele | `The concepts🤮 vs` | Fail „improvizat” → produsul real | Contrast · Umor | v2, v5 |
| Swanlift (sursă @thevareny) | `POV: your back has 30 years on your actual age.. 😮‍💨` | Problemă / POV | Pierdere > câștig · Rușine / nesiguranță (autoironic) | 2,418,878 views |
| Swanlift (sursă @thevareny) | `POV: you realize this is not a regular bra.. 😮‍💨` | Try-on POV | „Prea bun ca să fie adevărat” · Curiozitate | 273,643 views |
| Swanlift (sursă @thevareny) | `POV: I found the only thing that can save my posture 😮‍💨` | Try-on POV | „Prea bun ca să fie adevărat” · Pierdere | 181,212 views |
| Swanlift (sursă @thevareny) | `The perfect modest gym bra doesn't exist..` | Contrazicere → probă | Curiozitate · Identitate | 208,524 views |
| Swanlift (sursă @backalign.official) | „Have you ever seen this happen to women as they age… It's a condition called kyphosis…” (vorbit) | Explicație problemă | Autoritate (mecanism) · Pierdere | ~1.9M views — **atenție la afirmații medicale** |
| Swanlift (caption @thevareny) | „your back pain is catching up with you because of the way you carry yourself every day.” | Problemă | Pierdere > câștig | 2,418,878 views (reel-ul de mai sus) |
| Swanlift (caption @elquari_) | „NEVER going back to a regular bra😲🤯🍒” | Probă / reacție | „Prea bun” · Contrast | best 1,149,503 (Product Finder) |
| Swanlift (caption @alynne.us) | „Finally gave the viral ALYNNE Back Support Bra a try... and WOW! 🤩” | Talk-through try-on | Dovadă socială („viral”) · Curiozitate | 9,724,399 views |
| Proiector — competitor @merrybeam.official | „Turn any wall into a cozy Christmas window 🎄❄️” (caption) | Transformare | Contrast · Nostalgie | 1,903,012 views |
| Proiector — competitor @hollyglow.co | „TAG A CHRISTMAS LOVER! 😱🫣” (caption) | Share | Identitate · (Contagious: tag) | 272,681 views — engagement bait, evitat |
| Perdele — story | `SAME HOUSE. ONE BOX.` | Before/after | Contrast · Specificitate | story, fără cifră |
| Perdele — story | `THE NEIGHBOURS JUST STAND THERE` | Reacția altora | Dovadă socială · Statut | story, fără cifră |
| Perdele — story | `UP IN 20 MINUTES` / `ONE PERSON. NO TOOLS.` | Obiecție înlăturată | Specificitate | story, fără cifră — cifra trebuie verificată |
| Perdele — story | `STORES ARE ALREADY OUT` / `WE STILL HAVE STOCK` | Raritate | FOMO | story — **raritate falsă dacă nu e adevărat, nu se preia** |

Hook-uri **vizuale** (acțiunea din C01, fără text), din `hooks_board.html`:

| # | Hook vizual | Concept | Declanșator | Dovadă |
|---|---|---|---|---|
| 01 | Culoar → whip-pan pe palet | Store discovery | Curiozitate · Dovadă socială | TheXmasGlow v1/v3/v26 |
| 03 | Cutie luată de pe raftul plin, pusă în coș | Store discovery | Dovadă socială | „almost never fails” |
| 04 | Îi cade băutura când vede produsul (în afara cadrului) | Store discovery | Curiozitate · „Prea bun” | product-agnostic |
| 05 | Mulțime care năvălește pe palet | Store rush | FOMO · Dovadă socială | perdele v10 |
| 07 | POV: vârful degetelor înclină cutia pe raft | Store POV | Curiozitate | perdele v15 |
| 08 / 09 | „Three... two... one!” — cearșaf/pătură trasă | 3-2-1 reveal | Curiozitate | ambele din prima |
| 10 | POV: cadoul îți cade pe picioare în pat | Gifting POV | Vină / cadou · Statut | o singură generare, livrat |
| 11 / 12 | Cade de pe scară lipind un Moș gonflabil | Pattern interrupt | Umor / pattern interrupt · Contrast | 9 + 3 videouri TheXmasGlow |
| 13 | Mama se apleacă peste balustradă să pună steaua | Pattern interrupt | Umor · Curiozitate | 4 videouri |
| 14 | Priza cu beculețe → bradul ia foc, „Oh, shoot” | Pattern interrupt | Umor / pattern interrupt · Pierdere | 5 videouri, 3 porturi din prima |
| — | Camion cu cutii lovește pasarela, cutia ajunge la tine | Pattern interrupt (Genjutsu din viral) | Umor · Curiozitate | MerryGlow v6 (magazin fără vânzări) |

---

## 7. Ce preluăm în LIMITLESS

Legat de agenții și treptele din `docs/05-motorul-autonom.md`. Unde ceva din OD intră în conflict cu regulile noastre (`docs/02-reguli.md`, `playbooks/carti-marketing-psihologie.md` §5), scrie explicit.

**Vânător**
- Pragul OD pentru „dovedit”: conturi noi cu 1–2M pe un reel în câteva zile; ierarhizare după media ultimelor 20 de videouri **din ciclul curent de produs** + urmăritori, nu după numărul de magazine (`od/x_instructions/05_product_finder.md`, `decisions.md` 2026-09-30, 2026-10-06). Se pune în coada `queue/virale` cu „latest product run only”.
- De urmărit ca surse imediate: @gercekform, @alynne.us, @thevareny (sutien); @tryfestilight, @jollyview.co (perdele); @aquawish.us, @merrybeam.official, @hollyglow.co, @mymerryview (proiector).

**Analist**
- Fișa de cadre după modelul Swanlift: tăieturi cu timpi (ex. v8: 10 tăieturi în 13.3 s), text ars exact, „original look”, culori de produs pe tăietură, secunde riscante (piele goală, branduri) marcate de la început.
- Clasificarea hook-ului în cele 4 concepte OD + declanșator (tabelul din §6).

**Planificator (scara uneltelor)**
- Treapta 3 (Genjutsu) se confirmă pentru recast UGC: rețeta Swanlift (video + femeie + cameră + 2 referințe de produs, motion lock, „her clothes come from this prompt”, o rulare per culoare, max 30 s, împărțire la tăietură naturală). Rezoluția lor: 720p; regula noastră e 1080p → de testat dacă 1080p schimbă rata de refuz.
- Înainte de a trimite: **taie din video-sursă secundele cu piele goală/branduri** (la ei a fost singurul lucru care a trecut de `nsfw`); refuzurile nu costă credite, dar costă timp.
- Treapta 4 (GPT Image 2.5 → Seedance 2.5) pentru B-roll-ul fix de produs, după rețeta TheXmasGlow (start frame + `omni_reference` trimis explicit + `declined_preset_id`).
- Hook-urile „pattern interrupt” fără produs în cadru (11–14) sunt reutilizabile pe orice produs → candidate directe la treapta 1 (reutilizare) după prima generare.
- Notă: cercetarea lor (`od/x_research/genjutsu_motion_transfer_vs_object_swap.md`) recomandă *Object Swap* (`hf_mult_replace_object`) pentru fidelitatea produsului. La noi e **exclus** (`CLAUDE.md`, regulile din 10 oct), așa că nu se preia. Fidelitatea produsului în motion transfer o asigurăm cu 2 referințe de produs (față + spate) și QA.

**Producător**
- O generare pe cadru, apoi QA; nimic suprascris; numerotare `v<N>_c<NN>_g<K>` (`od/_tool/NAMING.md`) — util pentru `state/` și pentru costul pe secundă acceptată.
- Prompturile se copiază cuvânt cu cuvânt și se schimbă doar substantivele; se loghează „Reused from … — changed: …”.

**QA**
- Lista lor de eșecuri recurente devine checklist: proiecție/animație care nu acoperă tot, animație prea calmă, figuri desenate care par reale, căderi „floaty”, obiecte care apar din nimic, haine din poza personajului care apar sub produs, schimbare de culoare la tăietură, telefon/mână în cadru la POV, cutie greșită (fereastră, mărime).
- „Extract frames and check the landing before reporting a slapstick take as good — the thumbnail almost always looks fine.”

**Montaj + Cartea de stil**
- Durată 12–18 s pentru produse vizuale; hook 4–5 s; cadre de 4–5 s, o acțiune pe cadru; loc liber sus pentru text (cerut explicit de Daniel); sunet de cameră în clipuri, muzica adăugată la montaj.
- Formula de text: identitate + interdicție/nevoie/contrast + 1–2 emoji (§6). **Fără „Costco” / „IKEA”** sau alt brand/magazin real (regula noastră, `carti-marketing-psihologie.md` §5) — se înlocuiesc cu „the store”, „the warehouse”.
- Pentru sutien: textul de tip „POV:” e dovedit la competitori, dar **fără promisiuni medicale** („fixes back pain”, „kyphosis”) — se formulează ca senzație/postură vizibilă, nu ca tratament (§5 „Afirmații medicale”).

**Distribuție**
- Rețeta lor Swanlift: ziua 1 conturi + încălzire, ziua 2 încălzire + profiluri, din ziua 3 câte 3 reel-uri/zi, cele mai noi primele, același video + caption pe IG/TikTok/FB (`decisions.md` 2026-10-06). Atenție: LIMITLESS interzice același video pe mai multe conturi (`carti-marketing-psihologie.md` §5) — se preia doar ritmul, nu duplicarea.
- CTA: competitorii folosesc „Comment <WORD>”; la noi o singură dată, la final, cu funcție reală.

**Tracker + Învățare**
- Lecția de date a lor: vizualizările IG se citesc din scraper-ul de profil (live), nu din cel pe URL (cifre vechi de ore) și **doar plays IG**, fără FB (`decisions.md` 2026-10-06).
- Ce nu au avut și noi trebuie să avem: legătura video → vânzări. Arhiva OD nu are views/comenzi per video, deci nu se poate spune care hook a vândut; scorul pe hook al Trackerului închide exact golul ăsta.

**Produs (`docs/09-reguli-produs.md`)**
- Profilul câștigătorilor OD: cost ~$2–3, preț $60–80, wow vizual fără sunet, ușor de trimis. Singurul produs din aceeași nișă la $129.99 n-a vândut nimic. **[ipoteză]** plafon de preț în jur de $80 pentru impuls organic de sezon — de verificat cu cifre proprii, nu regulă.
