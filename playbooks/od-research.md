# OD research — ce aflăm din operațiunea „Organic Dropshipping” (Genjutsu · Seedance 2.5 · GPT Image 2.5 · sourcing · upscale)

Sursa: ghidurile de research din `library/sources/od-full/x_research/` (o operațiune reală de organic dropshipping, copie din 7 oct 2026; ghidurile sunt compilate 10–19 sept 2026, rezumatele YouTube până pe 2 oct 2026). Data acestui playbook: 10 oct 2026.
Comparat cu: `playbooks/higgsfield.md` și `playbooks/higgsfield-mecanica.md` (al nostru), plus `docs/02-reguli.md`, `docs/11-costuri.md`.

**Prescurtări pentru surse** (toate în `library/sources/od-full/x_research/`):
- `SD` = `seedance_2_5_prompting_guide.md`
- `G25` = `gpt_image_2_5_prompting_guide.md`
- `G2` = `gpt_image_2_prompting_guide.md`
- `NB` = `nano_banana_2_prompting_guide.md`
- `MvO` = `genjutsu_motion_transfer_vs_object_swap.md`
- `SRC` = `dropshipping_sourcing_playbook.md`
- `UP` = `video_upscale_models_research.md`
- `GJ/NN` = `genjutsu/NN_*.md` (rezumatele de videouri YouTube; `GJ/00` = indexul)

**Cum se citește.** E material de la alții, deci nimic de aici nu e „dovedit la noi”. Etichetele: **[oficial]** = documentația producătorului, citată în ghid; **[testat de ei]** = rezultat raportat de cineva care a rulat modelul; **[creator]** = spus într-un video YouTube (adesea sponsorizat de Higgsfield); **[ipoteză]** = dedus de noi, de verificat cu cifre. Regula noastră de bază rămâne: în producție folosim EXCLUSIV `hf_mult_motion_control`, `seedance_2_5` și `gpt_image_2_5`; `hf_mult_replace_object` doar în testul A/B (`docs/02-reguli.md`, 10 oct).

---

## 1. Ce e NOU față de playbook-urile noastre

### 1.1 Genjutsu (`hf_mult_motion_control`; `replace_object` doar pentru A/B)

**Specificații și comportament**
- **Intrare oficială: 4–30 s, până la 30 de imagini de referință, prompt opțional, 480/720/1080p** [oficial, `MvO` §„Four conflicts”; `GJ/09`, `GJ/19`, `GJ/30`]. Playground-ul API spune 1–30 s. Prin MCP se setează doar `resolution` [`MvO` §„Costs”]. La noi au mers și bucăți de 2,7–2,9 s (vezi §5, contradicția 1).
- **Genjutsu copiază mișcarea exact, inclusiv tremurul camerei din mână. Seedance cu video de referință o „netezește” și o lasă să derive** [creator, `GJ/25`]. Genjutsu păstrează și efectele (fum, foc), pe care Seedance 2.5 le-a ignorat în același test [creator, `GJ/17`]. Mai mulți utilizatori cred că Genjutsu e „Seedance 2.5 edit cu alt ambalaj” [`MvO`; `GJ/17`].
- **Fără imagine de cameră, motion transfer păstrează locul din sursă.** Pilotul de F1 a ieșit în biroul autorului, pentru că promptul nu spunea unde are loc scena. Când a pus imaginea circuitului și a numit-o în prompt, a mers [creator, `GJ/25`]. La noi trimitem mereu camera, dar trebuie și **numită în prompt** („Image 2 is the ROOM”). Facem deja asta.
- **Fără imaginea personajului, modelul poate inventa altă persoană** [creator, `GJ/33`]. **Cu mai multe persoane în viral, fața ta poate apărea pe mai mulți oameni** dacă promptul nu spune pe cine înlocuiește [creator, `GJ/33`]. Videourile cu multe fețe „încurcă” modelul: maxim 1–2 personaje în sursă [creator, `GJ/28`].
- **Imaginea de persoană e implicit „complete look”.** Fața, părul, corpul, hainele, încălțămintea și accesoriile vin din ea, iar hainele din sursă „nu au autoritate” dacă nu există o imagine separată de haină sau o instrucțiune explicită [`MvO`, preluat din regulile Ad Multiplier ale Higgsfield, încredere medie]. Pentru noi asta înseamnă că hainele din poza de Pinterest pot trece în video. De aceea blocul CLOTHES din șablonul 7.1 (`higgsfield-mecanica.md`) e necesar.
- **„Reference images bring their whole frame with them”**: hainele, lumina și fundalul din referință se scurg în rezultat. Referințele curate și neutre bat pozele frumoase [`MvO`, Riffkit]. **O față într-o referință de haină poate fura identitatea:** modelul a folosit „omul întâmplător care purta hainele din referință” [`MvO`, r/Seedance_AI]. Regula lor: **referința de produs sau haină fără nicio față** („on display, white background. No person in the shot”) [`MvO`; `GJ/20`, promptul „isolate clothing”].
- **Imaginile bat textul când se contrazic** [`MvO`]. Textul care descrie persoana altfel decât arată poza strică rezultatul („never rename or restyle a reference”).
- **Sunetul: scoateți audio din video înainte de upload** (drepturi de autor), apoi îl puneți la loc la montaj [creator, `GJ/21`, `GJ/29`]. La noi Genjutsu e oricum pe mute, iar audio-ul se pune la montaj (`higgsfield-mecanica.md` §2.5). Pasul `-an` în ffmpeg e gratuit. **[ipoteză]** Poate reduce și refuzurile.
- **„Mask retention”:** într-o cameră cu oglindă se schimbă și omul, și reflexia lui. Nu poți păstra doar una dintre ele [creator, `GJ/30`]. Pentru noi: viralele cu oglinzi sunt OK, pentru că reflexia se schimbă corect.
- **Clipuri cu mai multe tăieturi trimise întregi:** tăieturile, identitatea între cadre și chiar un personaj care trece prin spatele unei coloane au ținut. Exemple: un film de 27 s cu 4 cadre, fără prompt [creator, `GJ/37`], și testele cu tăieturi multiple din `GJ/35`. `MvO` recomandă: întâi clipul întreg o dată (o singură identitate, cel mai ieftin), apoi, dacă se strică la tăieturi, blocuri de ≥ 4 s pe locație. Asta susține experimentul nostru #1 (`higgsfield-mecanica.md` §10).
- **Cadrul de start editat („anchor still”).** Varianta de Reddit: editezi persoana nouă într-un cadru extras din sursă și îl dai ca referință, ca modelul „să nu aleagă o persoană la întâmplare dacă i-ai făcut deja jumătate din treabă” [`MvO`]. Varianta TikTok Shop: întâi generezi modelul, apoi îl pui în **poza exactă din primul cadru** al viralului cu GPT Image („replace pose”), apoi faci motion transfer cu video + modelul pozat + haina izolată [creator, `GJ/20`]. Genjutsu nu are slot de `start_image`, deci cadrul merge ca `image_reference` în plus. Efectul e netestat (`MvO`, Run 5).
- **Character sheet multi-unghi:** față, spate, profil, 3/4, corp întreg. Aproape toți creatorii îl folosesc [`GJ/01`, `GJ/09`, `GJ/29`, `GJ/35`]. Vederea **din spate** e „obligatorie” când viralul filmează persoana din spate [`MvO`; `GJ/09`]. Când fața nu se vede, **părul e purtătorul identității** și se descrie exact [`MvO`]. La noi: personajul = poza exactă de pe Pinterest (regula din 1 oct). Sheet-ul rămâne experimentul #12, doar cu acordul lui Szasz.
- **Reparare locală cu Object Swap pe clipul NOSTRU:** pe un clip Genjutsu deja generat, „character is wearing hat” sau „Replace the helmet for the one with the closed visor” + imagine. A schimbat doar obiectul [creator, `GJ/25`]. E rețeta (c) din `higgsfield-mecanica.md`, ca alternativă la Seedance `video_edit` (rețeta d), și intră în testul A/B.
- **Seedance 2.5 edit după Genjutsu**, ca să adaugi o acțiune care lipsea din video [creator, `GJ/25`]. Tot cu Seedance edit s-au scos pietonii dintr-un plan real „în 3 minute” [creator, `GJ/14`].
- **Prompt scurt: spui doar ce se schimbă.** „Don't over-prompt” [creator, `GJ/35`]. „Prompt = visual context only (not movement)” [`MvO`, Reddit]. Mulți creatori au rulat **fără prompt**, doar cu video + 1–2 imagini, și au obținut rezultate bune [`GJ/05`, `GJ/23`, `GJ/37`, `GJ/39`]. Dar la **Object Swap / edit** promptul prea subțire duce la „no-op”: Seedance 2.5 edit „~90% din timp scoate exact videoul de intrare” [`MvO`].
- **Relumina la schimbarea locului:** „relight the character to match the environment” e „cheia”, altfel arată fals [creator, `GJ/13`]. Pentru plăcile de loc: lumina vine din aceeași direcție și are aceeași calitate ca în sursă, pentru că „no model will save the edges” dacă lumina nu se potrivește [`MvO`].
- **Unde se strică** [`MvO`]:
  - mâinile care intră în buzunare devin „melted stumps”;
  - picioare care plutesc sau alunecă;
  - margini care „curg” la mișcare rapidă;
  - elementele noi ies mai saturate și mai contrastate decât restul;
  - la Object Swap, fața iese „un amestec” între model și persoana originală;
  - personaje în plus, coregrafie schimbată.
- **Biblioteca de mișcări (Motion Library → „Recreate”)** arată promptul și asset-urile folosite de Higgsfield pentru fiecare exemplu [creator, `GJ/31`, `GJ/33`, `GJ/39`]. Prin MCP: instrucțiunile serverului Higgsfield din sesiunea de azi trimit la `get_presets source=genjutsu category=genjutsu-trending`. `MvO` spunea în septembrie că presetările nu sunt expuse în MCP, deci s-a schimbat.
- **Analiză gratuită de video** cu instrumentul MCP `video_analysis_create`: analizează un URL YouTube cadru cu cadru (dimensiunea cadrului, mișcarea camerei, subiectul, lumina, montajul) [creator, `GJ/24`, care spune că e gratuit; **neverificat la noi**]. Nu e unealtă de producție. Ne interesează pentru Analist.
- **Skill-uri de prompt publicate:** Higgsfield are un SKILL.md pentru prompturi Seedance, în Academy, cursul „Master AI Filmmaking”, lecția 4 [`GJ/24`]. Există și un SKILL.md pentru Genjutsu [`GJ/33`]. ByteDance are skill-ul `sd25-pe`, dar conținutul nu a putut fi citit [`SD` §0].

**Prețuri raportate** (toate de la alții; ale noastre din `get_cost` sunt în `docs/11-costuri.md`):

| Sursa | Ce | Credite |
|---|---|---|
| `MvO` (blog Higgsfield) | 15 s, 480p / 720p / 1080p, la fel pentru ambele moduri | 40 / 104 / 144 |
| `GJ/11` | referință de 16 s, 480p / 720p / 1080p | 42 / 110 / 153 (normal 272, redus) |
| `GJ/23` | 480p / 720p / 1080p | 39 / 91 / 143 (normal 208) |
| `GJ/13` | Object Swap 1080p | 72 („mai ieftin decât motion transfer”) |
| `GJ/17` | Object Swap 1080p, clip mai lung | 270 |
| `MvO` (API) | per secundă, 480p / 720p / 1080p | 0,318 $ / 0,681 $ / 1,632 $ (~2× aplicația) |

Refuzurile „de obicei se rambursează” [`MvO`, Riffkit].

**Șabloane de prompt copiate exact** (`MvO`, ordinea șablonului DETAILED al Higgsfield: referințele → ce rămâne neschimbat → operațiile numerotate → restul blocat):

*Template D — Motion Transfer, persoană nouă + loc nou* (cel mai apropiat de rețeta noastră):
```
@Image1 and @Image2: Mara, front and back full-body [hair description]. @Image3: the black hoodie, back view, rhinestone mesh back panel. @Image4: the white version. @Image5: location A, an underground parking garage. @Image6: location B, a rooftop parking deck at sunset. @Image7: how the first shot looks.

Use @Video1 only for motion, camera and timing: keep every shot, cut, camera move, walk, pose, turn and its timing exactly as in @Video1, in the same vertical framing.
Recast the woman as Mara from @Image1 and @Image2, wearing the black hoodie from @Image3 with its rhinestone mesh back panel identical (the white hoodie from @Image4 in the opening shot [0.0–1.0 s]).
Shots from [0.0–5.2 s] take place in @Image5; shots from [5.2–10.3 s] take place in @Image6.
Photorealistic handheld phone footage, natural light, real fabric texture.
```

*Template A — Object Swap, persoană nouă, aceleași fundaluri* (pentru brațul de test B''):
```
@Image1 and @Image2 are the same woman, Mara: @Image1 front full-body, @Image2 back full-body. [Hair: long straight dark-brown hair falling over the hood; slim build.] @Image3 is the black hoodie, back view, with the rhinestone mesh back panel. @Image4 is the white version of the same hoodie.

Video edit. Keep this @Video1 clip exactly as it is: the same shots and cuts, camera moves, framing, the parking-garage and rooftop backgrounds, lighting, pacing and timing. Change only the woman.

1. Replace the woman in @Video1 with Mara from @Image1 and @Image2 in every shot, through every cut, turn and motion blur. Mara performs the original walk, poses, hand movements, position and size in frame. The original woman must never appear in any frame.
2. Mara wears exactly the hoodie worn in @Video1: the white hoodie from @Image4 in the opening shot [0.0–1.0 s], and the black hoodie from @Image3 in every later shot, its rhinestone mesh back panel identical in pattern, size, position and sparkle.

Everything else (backgrounds, lighting, camera moves, cuts and all timing) stays exactly the same. Photorealistic phone footage, natural skin and hair, real fabric texture.
```

*Template B — Object Swap, doar locul* (operația cheie):
```
1. Replace the background in @Video1 with the location from @Image1 in every shot, at the same camera height, angle and perspective as each original shot. The ground meets the boots exactly where the original ground did, with soft contact shadows under every step.
```
*Template C* = Template A + operația:
```
3. Replace the underground parking garage in the shots from [0.0–5.2 s] with the location from @Image5, and the rooftop parking deck in the shots from [5.2–10.3 s] with the location from @Image6, keeping each shot's camera height, angle and perspective and the same light direction.
```

*Swap de personaj, varianta lungă* (`GJ/29`, folosită pe un trend viral, motion transfer + character sheet):
```
Replace only the main male character in the source video with the person shown in my reference images.
The source video should remain visually unchanged apart from the character replacement. Preserve the original scene, location, background, camera framing, lens perspective, camera movement, lighting, choreography, timing, props, atmosphere, and overall cinematic appearance.
Make the person from my reference perform the exact actions of the original male character. Follow the original character's body movements, poses, gestures, head direction, facial expressions, and timing as closely as possible.
Maintain the person's identity throughout the entire sequence. Keep the same facial structure, recognizable features, hairstyle, skin tone, physique, and overall appearance consistent from beginning to end.
The replacement must naturally follow the original character's head position and body movement from every camera angle. Ensure the face is properly aligned with the movement and perspective of each shot.
Do not modify the female character, environment, background, props, camera behavior, lighting, choreography, or any other part of the source footage.
The final video should look like the original scene was filmed with the reference person playing the male character, with a seamless and photorealistic result.
```

*Fraze scurte care au mers:*
- `Exact same character, same clothes, doing the moves in video one.` [`GJ/05`]
- `Swap the location and the background to the one in the image. Keep the camera movement and the character the same in the video reference, but just relight the character to match the environment.` [`GJ/13`]
- `Modify the environment completely to a New York rooftop. Keep the character intact.` [`GJ/23`]
- Mutarea unei haine pe persoană (GPT/NB), din `MvO`: `Put the outfit of img_2 on the person of img_1. Only swap the outfit, keep the pose and facial features… exactly the same`
- Specificația Higgsfield pentru poza de persoană [`MvO`, Ad Multiplier]: `a straight-on, eye-level, full-body portrait of exactly one adult` pe `a seamless matte-white studio backdrop`, 3:4, 2k, `soft, evenly diffused` light, `authentic skin detail, realistic human anatomy, natural hands and limbs, and no plastic retouching`. Contrazice fundalul gri de la noi, vezi §5.

### 1.2 Seedance 2.5 (`seedance_2_5`)

**Parametri și mecanică** [`SD`]
- **Tipul de sarcină se deduce din cuvintele promptului** [oficial, §2]. Cuvintele „edit video, add, insert, remove, delete, modify, replace, change to” trec generarea pe modul **edit**, iar „extend forward/backward, continue” pe **extend**. Modurile edit, first/last-frame și extend sunt „blocate”: forțează `ratio=adaptive` și uneori `duration=-1`. Pe API-ul brut se folosește `omni_reference_task_type` explicit. Prin Higgsfield trimitem `mode` explicit. **[ipoteză]** Asta probabil ne protejează, dar în promptul omni nu folosim cuvintele declanșatoare de mai sus. Rămâne de verificat cu `ffprobe` că 9:16 și durata se respectă.
- **Limite oficiale** [§1]:
  - până la 50 de referințe (30 de imagini + 10 video + 10 audio);
  - referințele video la 480p/720p, câte 2–30 s (4–30 s la edit), cel mult 30 s în total;
  - imaginile de referință între 300 și 6000 px;
  - linkul spre video e valabil 24 h, cu maxim 100 de descărcări → **descărcăm imediat**.
- **Fețe reale:** Seedance 2.5 și 2.0 **nu acceptă imagini sau videouri de referință cu fețe umane reale** [oficial, §10]. Pe Volcengine sunt respinse la creare [testat de ei]. Merg: ieșirile modelului din ultimele 30 de zile, biblioteca de personaje digitale (`asset://…`, iar în prompt tot „Image 1”) și persoanele autorizate. La noi `start_image` e placa GPT, adică o ieșire de model, deci intră la excepție. Vezi §5, contradicția 12.
- **Video-to-video cu o persoană reală în sursă** a dat eroarea „input video… may contain real person” [`MvO`]. Nu se știe dacă Genjutsu are același filtru.
- **Facturare:** joburile cu video de referință se taxează pe secundele sursei **plus** pe cele ale ieșirii, cu ~20–25% mai mult [testat de ei, §12].
- **Durata nu înseamnă conținut.** Setarea de 30 s doar mărește durata, nu adaugă evenimente. Fără evenimente noi apar „waiting, repetition, slow motion”. Pentru 30 s trebuie 5–8 momente [`SD` §5]. La 4–5 s ajunge o singură acțiune.
- **Extensie:** la îmbinare apare o tăietură bruscă → tai 6 cadre de la sfârșit și 1 cadru de la început. Calitatea scade progresiv. Sursa se scrie direct `<Video_N>`, nu „reference <Video_N>”, altfel se schimbă tipul de sarcină [oficial, §12].
- **Zgomot la sfârșitul audio-ului** [oficial, §12] → fade de volum în post. Pentru hook-urile cu sunet propriu.
- **Morfarea la acțiune rapidă nu se repară cu upscale.** Încetinești acțiunea [§14]. Confirmă regula noastră „generezi lent, accelerezi la montaj”.

**Structura promptului** [`SD` §4, §16]
- Patru surse au ajuns independent la aceeași structură: **regula globală sus, timeline-ul la mijloc, regula de sunet și blocul de constrângeri jos**. „Labeled sections outperform one continuous paragraph” [Higgsfield, testat]. „Sari peste o secțiune și eșecul vine previzibil.” Structura noastră din `higgsfield-mecanica.md` §4.1 se potrivește deja cu asta.
- **Fiecare referință are un singur rol, iar cuvântul „only” e esențial** [testat de ei, fal.ai; §3]:
```
@Image1 controls only [identity, product design, clothing, or another invariant]. Do not copy [pose, background, lighting, camera angle, or text] from @Image1.
```
- **Mai multe unghiuri ale aceluiași produs sunt citite ca mai multe produse.** Soluția e o propoziție de numărare [testat de ei, OpenArt; §3]:
```
All three images show one lamp. The video must contain only one lamp.
```
  Varianta lungă de „count lock” a Higgsfield [§11]:
```
MEMBER COUNT LOCK (critical): The group has exactly four members, never five, never six. No fifth member, no extra unnamed dancer, no background double, no duplicated or cloned member. Each of the four appears once and only once in any frame, no mirror, glass, or reflection showing an extra copy.
```
  plus `never render a reference sheet or duplicate the subject` [stimQQ].
- **Constrângeri cu nume („… LOCK”)**: `IDENTITY LOCK`, `NO-IP LOCK`, `SINGLE-LENS LOCK` etc. Plus un bloc final **`POSITIVE LOCKS`** care reia toate regulile la afirmativ [Higgsfield, §11]. Le poți găsi ușor la depanare.
- **Timpi** [oficial, §5]: doar **secunde întregi** (`0-3s`), fără goluri, o acțiune pe interval, iar timpul nu e numărătoare („nods three times in one second” nu merge). **Cauza înaintea reacției**, ca acțiuni separate: contactul, mișcarea rezultată, sunetul, apoi reacția [fal.ai]. Vezi §5, contradicția 6.
- **Camera:** o singură mișcare pe cadru [oficial 2.0]. Dai camerei o **poziție pe ecran**, nu doar o mișcare („dynamic” nu ajută la nimic) [fal.ai]. Dacă instrucțiunea de cameră e ignorată, mărimea cadrului și mișcarea se scriu **înaintea** luminii [Dreamina]. Termenii rari se scriu ca `[term + descriptive explanation]` [oficial]. Higgsfield blochează și obiectivul prin unghiul de câmp (84° / 47° / 29° / 18°) și distanța în metri: `No lens drift mid-segment`.
- **„Freeze means freeze”**: ce trebuie să stea nemișcat primește `no drift, no wobble, no micro-motion`, pentru că implicit modelul pune viață peste tot [stimQQ, §7]. Pentru realism UGC **ceri imperfecțiunile**: tremur, autofocus întârziat, „exposure breathing”. Altfel iese aspect curat de reclamă [§7, §14].
- **Acțiunea repetată se descompune într-o secvență mecanică fixă**, cu o constrângere de final („The sword never stops inside a body”) [Higgsfield, §7]. Pentru noi: apăsări repetate, îmbrăcatul pas cu pas.
- **Fiecare acțiune se descrie o singură dată.** Repetată cu alte cuvinte se strică [stimQQ]. Instrucțiunea esențială se spune o dată la început și se întărește doar în momentul ei din timeline [Dreamina; §11].
- **Subiecte cu nume** (`THE WOMAN`, `THE PRODUCT`) și apoi niciun pronume [stimQQ, §11]. E cea mai ieftină blocare de identitate.
- **Negații sancționate oficial doar pentru subtitrări și audio:** `no subtitles`, `no BGM` [oficial, §4, §8]. Blocul final de constrângeri e susținut de majoritate: scurt, concret, grupat la sfârșit [§15.5].
- **Marcaje de sunet:** `()` muzică, `<>` efect, `{}` dialog, `【】` subtitrare [oficial]. Niciun exemplu oficial nu le folosește, așa că se pun doar când un canal „curge” în altul [§8].
- **Dialog (hook-uri UGC care vorbesc)** [§9]:
  - forma `Speaker: "line"` sub antetul limbii;
  - **2,5–3 cuvinte pe secundă** (~20 de cuvinte la 8 s);
  - prim-plan mediu, buzele vizibile, camera stabilă;
  - `No other character speaks.`;
  - **pentru accent numești accentul, nu limba**: „American” a reparat un accent britanic, „American English” nu [testat de ei, MindStudio].
  - Șablonul de voce cu 3 sloturi [oficial 1.5-pro]:
```
In a calm emotional state, with an even tone and a normal speaking pace, say: "Let's begin with what matters most."
```
  - Dublaj sau traducere [oficial 2.5]:
```
Translate the spoken dialogue in the video into Chinese, with no subtitles. Precisely adjust the lip movements to match the translated speech, while keeping everything else unchanged.
```
- **Varianta minimă**, pentru un singur cadru cu o referință [`SD` §16]:
```
<Subject> <action> in <location>, <style>, camera <one move>.
@Image 1 controls only <invariant>. Do not copy <pose/background> from @Image 1.
<Lighting in one clause.> <Physics in one clause.>
Audio: <ambience>. (no BGM). No subtitles.
```
- **Pe Higgsfield, selectorii de gen și lumină din interfață** „fac mai mult decât textul promptului” [Higgsfield, §13]. Prin MCP nu-i avem, deci totul trebuie să vină din prompt.
- **Categoria „UGC ad” la Higgsfield**:
  - nu impune un gen;
  - etichetele sunt scrise cu litere mici;
  - segmentele au cadre numite („Turbulence Hook”, „The Pivot”);
  - tonul vocii se scrie înaintea replicii („in a tight controlled voice: "…"”);
  - cadrele fără vorbă sunt marcate „no speech” [§13].

### 1.3 GPT Image 2.5 (`gpt_image_2_5`)

- **Flare vs sunburst, răspunsul la experimentul nostru #5** [oficial, `G25` §2]:
  - **Sunburst** = modelul de bază, pentru calitate, peste GPT Image 2. E recomandat **când contează precizia editării**.
  - **Flare** = modelul mic, rapid, cu calitate „comparabilă cu GPT Image 2”.
  - Prompturile sunt identice pe ambele.
  - Procedura OpenAI: stabilești nivelul pe Sunburst, apoi reiei pe Flare cu același prompt și treci pe el doar dacă ține calitatea.
  - Atenție: `quality="high"` nu înseamnă același lucru pe cele două.
- **Valorile implicite pe Higgsfield sunt cele mai ieftine: `variant=flare`, `quality=low`, `resolution=1k`** [`G25` §13, schema citită direct din API]. Dacă nu le setezi, primești calitate redusă fără niciun avertisment → trimitem mereu explicit `variant`, `quality` și `resolution`.
- **Higgsfield nu are mască sau inpainting pentru GPT Image 2.5 și nici dimensiune custom.** Ai doar aspect ratio și treaptă de rezoluție. Singurul rol media e `image_references` [`G25` §13]. Asta confirmă ce scrie în mecanica noastră §5.1.
- **Parametrii nu se scriu în text.** „9:16, 4K, PNG” în prompt consumă atenție, poate fi desenat ca text și lasă parametrul real la valoarea implicită [oficial, `G25` §3].
- **Peste 2560×1440, rezoluția e „experimentală”** pentru OpenAI [`G25` §3]. Exemplele oficiale folosesc `medium` ca normă și `high` doar la text dens [§10]. „A higher setting doesn't guarantee a better result.” Asta susține experimentul nostru #6 (2k medium vs 4k high).
- **Comportamentul modelului** [`G25` §4]:
  - e literal;
  - **nu inventează direcție artistică**: lumina, obiectivul și granulația trebuie date de tine;
  - **„cinematic” e contagios** (dă gradare orange-teal);
  - **aspectul „lipit”** al subiectului persistă → **clauza de integrare** e obligatorie;
  - constrângerile adunate se degradează: generezi baza, apoi aplici constrângerile ca editări, una câte una.
- **Clauze oficiale bune pentru UGC-ul nostru:**
```
Avoid cinematic lighting, dramatic color grading, or stylized composition.
No glamorization, no heavy retouching.
No extra text, no watermarks, no unrelated logos.
Original design only. No trademarks. No copyrighted characters.
Do not add new elements or text.
```
  Plus `Full body visible, feet included.` și numirea explicită a **privirii** și a **contactului mâinilor** cu obiectul [oficial, §5 fundamentul 4]. Cuvântul „photorealistic” sau „real photograph” se scrie explicit: fotografia nu e implicită [§5; `G2` §5.5, „engages a distinct mode”].
- **Structura de editare** (oficială, copiată exact; `G25` §14.B):
```
<The single change, stated restrictively.
 "Change only the X." / "Replace ONLY the Y with Z." / "Remove the W.">

Preserve exactly:
- Identity: <facial features, hair, skin, expression, body proportions>
- Geometry: <shape, structure, scale, perspective of everything unchanged>
- Layout: <positions and spatial relationships of all other elements>
- Camera: <angle, height, framing, crop, focal length feel>
- Light: <direction, quality, shadow position and length, colour temperature>
- Colour: <palette, saturation, contrast, overall grade>
- Text and labels: <all existing wording, logos, markings — unchanged>
- Background and surrounding objects: <unchanged>

Integration:
<The changed element must match the scene's existing lighting direction,
 shadow behaviour, colour temperature and grain so that it does not look
 pasted on.>

Do not add:
<New elements, accessories, text, logos, or watermarks. Do not restyle,
 redesign, or "improve" anything not named in the change above.>
```
  Liniile **Camera** și **Colour** sunt „cele mai des omise și cele mai des necesare” [§14.B]. Lista de păstrat **se repetă la fiecare tură**, pentru că nu se transmite de la o tură la alta [§5 fundamentul 8].
- **Mai multe referințe** (oficial, se pune înaintea structurii):
```
Inputs:
- Image 1: <role — subject / style / clothing / background / product>
- Image 2: <role>

Combination:
<Explicitly what moves from where to where, and what each input
 contributes. Name what is taken from each and what is ignored.>
```
  Două referințe fără roluri = modelul face media lor [§5 fundamentul 7].
- **Consistența personajului:** blocul `Character Consistency:` + `Do not redesign the character.` în fiecare scenă [oficial, §7]. În testul MindStudio, GPT Image 2.5 a bătut Nano Banana 2 și Pro la consistența pe 4 unghiuri [§7].
- **Refuzuri de moderare** [`G25` §11]:
  - **nu se reîncearcă orbește**, pentru că nu trece și arde cota;
  - `moderation_details.moderation_stage` (`input` / `output`) arată dacă a picat promptul sau imaginea generată;
  - la GPT Image 2 blocajele vin des de la **ieșire**, adică imagini fotorealiste cu oameni, iar reformularea promptului nu ajută;
  - prefixul „A surrealistic image of” e doar un diagnostic, nu o soluție [`G2` §9].
- **Din ghidul GPT Image 2, valabil probabil și pentru 2.5** [`G2`]:
  - ≤ 4 constrângeri tari, iar slotul „key details” are 2–4 elemente [§12, §15.6];
  - **stânga/dreapta e citită ca ecran, nu ca anatomie** → scrii direct în spațiul ecranului [§8.6];
  - 2–3 reîncercări cu același prompt rezolvă o parte reală din eșecuri [§12 pasul 6];
  - fața trece „plastic” prin editări → **decupezi, editezi zona și pui fața originală la loc** [§8.7];
  - `background="transparent"` schimbă stilul întregii imagini: îl face mai fotorealist sau mai „sticker” → reglezi stilul după ce activezi transparența [§7.2].

---

## 2. Motion transfer vs object swap: concluzia lor și testul nostru A/B

**Concluzia lor** [`MvO`] pentru materialul lor: clipuri **proprii**, cu produsul real (un hanorac cu strasuri) purtat în cadru.
- **Object Swap e implicit, Motion Transfer e pentru cazuri speciale.**
- Motivul: Object Swap e o **editare**. Hanoracul real, lumina, camera și tăieturile rămân pixeli pe care modelul îi copiază.
- Motion Transfer păstrează doar mișcarea și **redesenează tot restul din imagini statice, inclusiv produsul**, poză cu poză. Produsul iese „approximate” [Reddit, test pe ambalaje cosmetice], iar „approximate” e eșec pentru un magazin care vinde exact acel produs.
- Motion Transfer e mai bun când lumea nouă nu are nimic comun cu sursa sau când sursa e o singură filmare continuă.
- Încrederea lor: **mică spre medie**. Nimeni nu a testat vreun mod pe o haină care trebuie să rămână identică.
- Singurul test Object Swap documentat (minge de golf → ou) a picat: mingea originală a rămas vizibilă [The Rundown].
- Toate exemplele lăudate din comunitate sunt Motion Transfer.

**De ce situația noastră e alta:**
- Sursa noastră e **viralul unui competitor**, nu filmarea noastră.
- Dacă Object Swap schimbă doar produsul, rămân persoana și camera competitorului, adică conținut neoriginal. HeatGrump a primit deja „Your Page is no longer recommended” (`higgsfield-mecanica.md` §3).
- Regula LIMITLESS cere alt personaj și altă cameră. Asta e exact ce face Motion Transfer.
- Argumentul lor despre fidelitate rămâne valabil și pentru noi: la Motion Transfer produsul e reconstruit din referințe. Acolo apar migrarea feței pe buzunare și refuzurile `ip_detected` (mecanica §2.6).

**Cum se potrivește cu testul nostru (`higgsfield-mecanica.md` §10.0).** Brațele A, B și B' rămân. Din `MvO` propunem să adăugăm sau să ajustăm următoarele **[ipoteză, de aprobat de Szasz, pentru că modifică testul]**:
1. **Brațul B'' — Object Swap pe viral, care schimbă persoana ȘI camera, dar păstrează produsul** (Template A + operația 3 din Template C).
   - Are sens doar când produsul competitorului e **identic** cu al nostru (dropshipping: același articol) și nu are logo sau brand vizibil.
   - Răspunde exact la întrebarea lor: rămâne produsul real mai fidel decât la Motion Transfer?
   - Riscuri de notat:
     - fața iese amestecată cu cea originală [`MvO`];
     - camera e limitată la înălțimea, perspectiva și lumina sursei [`MvO`];
     - originalitatea față de algoritmul Meta e necunoscută.
   - Rezultatul nu se postează fără decizia lui Szasz.
2. **Braț fără prompt** (Run 2 din `MvO`): aceleași referințe, doar `Replace the woman in @Video1 with the woman in @Image1.` sau niciun prompt. Răspunde la întrebarea „ajută sau strică promptul?”. Nimeni nu a testat asta pe Genjutsu.
3. **Braț cu cadru de start** (Run 5): pe lângă referințe, o placă GPT Image 2.5 (4,25 cr) cu persoana noastră în camera noastră, în poza din cadrul 0 al viralului.
4. **Protocol preluat:**
   - o singură variabilă pe rulare;
   - drafturile 480p se judecă pe **structură** (persoana corectă în fiecare cadru, produsul la locul și în forma lui, tăieturile intacte), nu pe detalii fine, pentru că „480p vs 720p se vede mai ales în păr și marginile țesăturii”;
   - rezoluția mai mare e o generare nouă, nu același take mărit, deci finalul poate diferi de draft;
   - porți de decizie între rulări: dacă iese no-op, adaugi o propoziție care descrie acțiunea; dacă produsul se strică, adaugi un macro al detaliului ca referință.
5. **Tabelul de verificare din `MvO`** se adaugă la QA: identitate la tăieturi, detaliul produsului care „respiră”, mâini, margini, picioare, lumină și saturație, structură (număr de tăieturi, 9:16, durată, fps, fără oameni sau text în plus).

**Costul brațelor noi:** la 480p (~15 cr / 5 s, `docs/11-costuri.md`), 3 virale × 3 brațe ≈ 135 cr, plus placa de start de ~13 cr.

---

## 3. Sourcing: furnizori, test, livrare SUA, marje

Ce spune `SRC`. E un singur document, fără cifre de vânzări proprii. Sursele sunt forumuri Shopify, App Store, Trustpilot și G2, pentru că Reddit era blocat.

- **Cinci niveluri:**

| Nivel | Ce e | Când |
|---|---|---|
| 1 | Aplicații-catalog: AliExpress/DSers, **CJ**, Zendrop, Spocket | 0–10 comenzi/zi, test |
| 2 | **Agenți de fulfillment**: HyperSKU, EPROLO, Sourcinbox, Wiio, NicheDropshipping | ≥ 10 comenzi/zi |
| 3 | Surse directe: 1688, Taobao, Yiwugo, Made-in-China, Global Sources | când ai câștigătorul |
| 4 | Agent privat sau fabrică direct | ≥ 100 comenzi/zi |
| 5 | Stoc în SUA + 3PL (ShipBob, ShipMonk, ShipCalm) | brand |

- **Dintre cei patru clasici, CJ e cel mai bun:** gratuit, depozite în SUA și UE, singurul cu agent uman. Zendrop e „o taxă pe comoditate”. Alibaba e pentru angro, nu dropshipping. AliExpress e unealtă de research.
- **Trecerea la un agent** taie costul produsului cu 20–40% și timpul de livrare la jumătate. 1688 e cu 30–70% mai ieftin decât Taobao, iar Taobao e cu 30–80% mai ieftin decât AliExpress. 1688 se folosește ca să verifici prețul agentului (căutare după imagine).
- **SUA, 2026:** scutirea de taxe vamale „de minimis” de 800 $ a dispărut pentru toate țările. Suspendarea e **pe termen nedefinit din 24 iunie 2026**, iar prin lege se termină în 2027. Orice colet plătește taxe (coletele din China de sub 800 $ au avut ~54% sau o taxă fixă pe articol). Consecințele:
  - costul real include taxa;
  - **depozitul din SUA** (CJ, HyperSKU, EPROLO, Zendrop, 3PL) plătește taxa o dată, pe importul en-gros;
  - Vietnam, India sau Mexic nu ocolesc taxa;
  - **întârzierile la vamă sunt sursa nr. 1 de chargeback-uri noi** → termene de livrare afișate onest.
- **Verificarea agentului:**
  1. Același link la 3–4 agenți; diferența de preț e adesea peste 40%.
  2. **O mostră comandată la tine înainte de orice comandă de client** („non-negotiable”).
  3. În scris: cine plătește coletul pierdut, spart sau varianta greșită.
  4. Ceri linkul sursă de pe 1688.
  5. Ambalaj custom la volumul tău actual.
  6. Testezi timpul de răspuns în weekend.

  Semnale de alarmă: taxă de „membership”, refuzul mostrelor, niciun om de contact cu nume, presiune de plată în avans, prețuri care se schimbă după ce te angajezi.
- **Stiva recomandată:**
  - test pe AliExpress/DSers sau CJ;
  - la 10+ comenzi/zi, **imediat** HyperSKU sau EPROLO („cea mai mare rentabilitate”);
  - livrare rapidă în SUA prin Spocket, Trendsi sau depozitul agentului;
  - la 100+ comenzi/zi, comandă en-gros + ShipBob.
- **Marje:** documentul **nu dă marje sau prețuri de vânzare**. Dă doar diferențe relative de cost și prețuri POD (tricou Printful ~11,69 $, Printify ~10,36 $, Gelato ~9,80–11,50 $). Nu inventăm cifre. Pragurile de preț și de bani la 1M vizualizări rămân cele din `docs/09-reguli-produs.md` (Esteban).

**Ce preluăm:** vezi §6, punctele 10–12. Regula 9 din `docs/09-reguli-produs.md` („furnizor cu livrare sigură în SUA”) primește criterii concrete: depozit în SUA, mostră, verificarea agentului.

---

## 4. Upscale video: ce recomandă și dacă intră la noi

**Recomandarea lor** [`UP`, pentru clipuri Seedance 1080×1920, 24 fps, 4–5 s]:
- **Implicit: ByteDance Upscale**, preset `aigc`, treapta standard, 2K, 30 fps.
  - E singurul **non-generativ**: ascute, curăță zgomotul și mărește, fără să inventeze textură, deci nu rescrie eticheta produsului.
  - E și cel mai ieftin: ~8 cr pentru 10 s la 4K, ~0,10 $ pe clip la 2K. Un creator raportează **0,43 cr** pe clip [`GJ/23`].
  - Prin MCP: `provider: "bytedance"`, `preset: "aigc"`, `resolution: "2k"`, `fps: 30`, plus `width`/`height` sursei.
  - Peste 30 fps costul se dublează.
- **Escaladare: Topaz** (Starlight Precise, corectiv), doar când o față a ieșit „plastic” sau clipul e moale. Costă ~4,4× (35 cr la 10 s, 4K; `GJ/23`: 16 cr la 2K). **Nu** se folosește pe produsul aprobat, pentru că modelul de difuzie e liber să-l reinterpreteze. Astra 2 e creativ și nu e pentru fidelitate.
- **FLUX.3: nu.** E de ~16,5× mai scump, modul implicit „Creative” rescrie detaliile produsului și nu e în MCP (care expune doar `bytedance` și `topaz`).
- **Argumentul principal:** sursa e deja 1080×1920, rezoluția la care servesc TikTok și Instagram. Upscale-ul dă rezervă pentru crop sau zoom în CapCut, nu o reclamă mai bună. Hook-ul, textul și constanța postărilor mută cifrele, nu finisajul.
- **Legat de Genjutsu** [`MvO`]: dacă sursa e 720p, finalul se face la 720p („1080p only upsamples a 720p source”), apoi un upscale conservator.

**Intră în fluxul nostru? Nu, deocamdată.**
- Upscale/reframe/relight sunt pe lista „Ce NU folosim” (regula din 10 oct, `playbooks/higgsfield.md` §9).
- Producem nativ la 1080p (setarea fixă), iar ghidul lor spune chiar că la 1080p vertical upscale-ul aproape nu contează.
- Singura situație în care ar conta e una de **cost**: Genjutsu la 720p (35 cr / 5 s) + ByteDance (~0,4 cr) în loc de 1080p (55 cr), adică ~35% mai puțin pe clip.
- **[ipoteză]** Se propune lui Szasz ca experiment: 3 clipuri, 720p + ByteDance vs 1080p nativ, cu QA orb pe telefon. Intră doar cu acordul lui, pentru că adaugă o unealtă în afara bazei de 3.

---

## 5. Contradicții cu ce știam

| # | Subiect | Noi (`higgsfield*.md`) | Ei (OD) | Ce pare mai solid și de ce |
|---|---|---|---|---|
| 1 | Durata minimă Genjutsu | sub 2 s pică; 1,8 s pică; 2,7 și 2,9 s merg; ideal 3,5–4,0 s [confirmat HG] | 4–30 s oficial; „minimul de 4 s rezolvă problema”, iar bucla sau freeze-ul „arde credite și inventează mișcare” [`MvO`] | **Al nostru** e empiric prin MCP. Practic nu e conflict: costul e același până la ~4 s, deci **ținta e 4,0 s**. Sub 4 s doar dacă viralul n-are altceva, iar multiplicarea se taie înainte de lipitură. |
| 2 | Prețul Genjutsu | 44 minim, 55 la ~5 s 1080p (`get_cost` pe contul nostru, 10 oct) | 144 pentru 15 s la 1080p (~9,6/s); 143–153 cu reducere / 208–272 normal; Object Swap 72 sau 270 [`MvO`, `GJ/11`, `GJ/13`, `GJ/17`, `GJ/23`] | **Al nostru**: măsurat pe contul nostru, mai nou. Promoțiile schimbă prețul, deci **`get_cost` înainte de fiecare lot**. Prețul Object Swap nu e clar → îl măsurăm în A/B. |
| 3 | Prețul GPT Image 2.5 | 1k low 0,25 · 2k medium 1 · 4k high 4,25 · 4k max 15 (`get_cost`, 10 oct) | 1K Low 1,5 · 2K High 5,5 · 4K Max 26,5 (pagina Higgsfield, 11 sept) [`G25` §13] | **Al nostru**: măsurat pe planul nostru, mai nou. Al lor e prețul de listă de pe pagina de marketing. |
| 4 | Rezoluția Seedance 2.5 | 1080p (treaptă în `get_cost`; producție HG la 1080×1920) | „Plan for 720p”: plafon 720p raportat de toți testerii, inclusiv Higgsfield în septembrie [`SD` §15.1] | **Al nostru**, mai nou, dar trebuie dovedit cu cifre: **`ffprobe` pe fiecare clip** (mecanica §9.3). Dacă iese 720p cu `resolution: "1080p"`, corectăm costurile. |
| 5 | `start_image` + `image_references` în Seedance | merge [confirmat HG, `unbox_retry.json`] | pe API-ul brut se exclud reciproc; „Higgsfield nu are roluri separate start/end” [`SD` §2, §13] | **Al nostru**: rulat efectiv prin Higgsfield. Ce scrie ei se referă la API-ul brut sau la o stare mai veche. |
| 6 | Timpi în prompt | intervale fracționare (0,0–1,5 s; apăsări la 0,6 / 1,7 s) au dat clipurile fixe aprobate [confirmat HG] | doar secunde întregi, fără goluri, timpul nu e numărătoare [oficial, `SD` §5] | **Ambele**. Prompturile aprobate se copiază cuvânt cu cuvânt (merg). La prompturi noi: intervale întregi, iar momentele precise doar ca sunet sincronizat. Se testează o pereche. |
| 7 | Negațiile | regula pozitivă întâi, apoi negații scurte; „do NOT copy the hair” a reparat scurgerea [confirmat HG] | „no X” strică (modelul vede X; scrii „bare earlobes”); imaginile bat textul [`MvO`]; la GPT, descriere pozitivă în loc de interdicții [`G2` §8.5]; la Seedance oficial doar `no subtitles` / `no BGM`, dar Higgsfield: excluderile previn mai multe eșecuri [`SD` §13, §15.5] | **Sinteza noastră (mecanica §4.1) rămâne**, pentru că e confirmată în producție și susținută de testele Higgsfield pe Seedance. Preluăm finețea lor: la obiecte și accesorii, starea pozitivă fizică („bare wrists”, „plain fabric pockets”), nu numele obiectului interzis. |
| 8 | Cuvintele grele în dialog | scrise fonetic [YT CHHH8tNioSc] | nu: respelling-ul repară un cuvânt și strică ritmul frazei [`SD` §9.2, seedance.tv] | Neclar: ambele sunt sfaturi de la terți, fără A/B. Implicit **fără** fonetic; fonetic doar pe un singur cuvânt care iese greșit de 2 ori. |
| 9 | Dominanta galbenă la GPT | GPT „strică spre galben” [YT Hn8A8D4-SpQ] | mit: galbenul era la gpt-image-1, nu la 2 [`G2` §11.6] | Dovadă slabă de ambele părți: un creator vs absența plângerilor. Linia noastră de culori („vivid, slightly warm, not golden, not orange”) nu costă nimic → rămâne. |
| 10 | Promptul de editare GPT | „REPRODUCE ONE TO ONE” + listă numerotată „WHAT CHANGES” [confirmat HG pe gpt_image_2] | 2.5 oficial: schimbare + listă „Preserve exactly” + Integration [`G25`]; la GPT 2 practicienii: listele de păstrat eșuează, descrii imaginea finală pozitiv [`G2` §8] | **Al nostru + blocul Integration**. Pentru 2.5 precizia editării e capacitatea principală (oficial). Contra-evidența e pe modelul vechi. |
| 11 | Viralul întreg într-o singură rulare Genjutsu | HG a renunțat pe 17 sept, fără motiv notat | tăieturile și identitatea țin; rulezi întâi clipul întreg [`MvO`; `GJ/35`, `GJ/37`] | **Al lor** e mai documentat (mai multe teste). Experimentul nostru #1 urcă în prioritate. Atenție: 15 s la 1080p ≈ 144–165 cr, deci se testează la 480p. |
| 12 | Personajul = poza reală de pe Pinterest | regula din 1 oct (poza exactă), a mers în Genjutsu la HG | Seedance oficial nu acceptă fețe reale ca referință; filtrul Genjutsu a blocat fețe licențiate; recomandă fețe generate de AI [`SD` §10; `MvO`] | **Practic, al nostru a mers.** Riscurile sunt reale: refuzuri (`ip`/`nsfw`/privacy) și dreptul la imagine al persoanei. **Nu schimbăm regula. O semnalăm lui Szasz** ca decizie de business. |
| 13 | Rezoluția finală | 1080p fix (regulă) | 480p pentru drafturi, final 720p dacă sursa e 720p, apoi upscale [`MvO`] | **Regula lui Szasz rămâne.** Experimentul de cost din §4 doar cu acordul lui. |
| 14 | Modul implicit Genjutsu | Motion Control (regula din 10 oct) | Object Swap (pe filmări proprii cu produsul real) [`MvO`] | **Contexte diferite, ambele corecte.** Pe viralul competitorului, originalitatea cere persoană și cameră noi. Testul A/B (§2) decide pe fidelitate, refuzuri și cost. |
| 15 | Promptul la Genjutsu | prompturi lungi, cu blocuri (păr, haine, produs, text) [confirmat HG] | mulți creatori: fără prompt sau cu un rând; „don't over-prompt” [`GJ/23`, `GJ/35`, `GJ/37`, `GJ/39`] | Pentru detaliile de produs și scurgerile de păr sau haine, **al nostru** (confirmat pe produs). Showcase-urile lor nu au un produs care trebuie să rămână identic. Brațul „fără prompt” din A/B măsoară diferența. |
| 16 | Fundalul referinței de persoană | gri („mult mai bine decât alb”) [YT HSON-SoFz7s, CHHH8tNioSc] | specificația Higgsfield Ad Multiplier: „seamless matte-white studio backdrop” [`MvO`] | Neclar: e o regulă de pipeline Seedance, nu un test A/B. Contează doar dacă Szasz aprobă character sheet-ul (experimentul #12). Atunci se testează gri vs alb. |

---

## 6. Ce preluăm în LIMITLESS

1. **Testul A/B Genjutsu** (`playbooks/higgsfield-mecanica.md` §10.0, `docs/02-reguli.md` după decizie). Se adaugă, cu acordul lui Szasz:
   - brațul **B''** (Object Swap pe viral: persoană + cameră noi, produsul real păstrat, doar dacă produsul e identic și fără brand);
   - brațul **fără prompt**;
   - brațul **cu cadru de start**.

   Plus protocolul din `MvO`: o variabilă pe rulare, drafturi la 480p judecate pe structură, porți de decizie. (§2)
2. **`engine/produce`, pregătirea clipului** (mecanica §2.2):
   - `ffmpeg -an`: fără audio la upload;
   - ținta bucății: **4,0 s**;
   - camera trimisă mereu ȘI numită în prompt;
   - la virale cu mai multe persoane, promptul spune exact pe cine înlocuim; viralele cu > 2 persoane sunt marcate „risc”. (§1.1)
3. **Referințe de produs fără față**: planșa de produs (mecanica §5.4 / șablonul 7.7) iese pe fundal neutru, fără persoană. Dacă avem doar poza cu un model care poartă produsul, izolăm întâi produsul cu GPT Image 2.5. (§1.1)
4. **Apeluri GPT Image 2.5** (`engine/produce`, mecanica §5):
   - mereu `variant` explicit (**sunburst** pentru plăci și editări, flare doar după ce trece testul identic), `quality`, `resolution`, `aspect_ratio`;
   - niciun parametru scris în text;
   - în șabloanele 7.4 și 7.7 se adaugă blocul **Integration**, clauzele anti-cinematic și anti-retuș, „Full body visible, feet included”, privirea și contactul mâinilor;
   - maxim 4 constrângeri tari;
   - la refuz de moderare: citim `moderation_stage`, nu reîncercăm orbește. (§1.3) Experimentul #5 se înlocuiește cu „sunburst vs flare pe același prompt”.
5. **Prompturi Seedance 2.5** (șabloanele 7.5 și 7.6):
   - `@Image N controls only …`;
   - propoziția de numărare `All N images show one [product]. The video must contain only one [product].` (ajută și la `ip_detected` cu mai multe referințe);
   - `no BGM, no subtitles` în blocul AUDIO;
   - în promptul omni, fără cuvintele „add / replace / remove / change to / continue”;
   - cauza înaintea reacției;
   - „no drift, no wobble, no micro-motion” pentru cameră fixă;
   - o singură mișcare de cameră, scrisă înaintea luminii;
   - pentru `video_edit`: schimbarea descrisă concret, ca să nu iasă no-op. (§1.2)
6. **Hook-uri care vorbesc** (`engine/hooks` + șablonul de dialog):
   - forma `Speaker: "line"`;
   - ≤ 2,5–3 cuvinte/s;
   - prim-plan mediu;
   - accentul „American” (nu „American English”);
   - `No other character speaks. No subtitles.`;
   - fade la sfârșitul audio-ului în `engine/edit`. (§1.2)
7. **QA** (`engine/qa`, mecanica §9.1–9.3). Se adaugă: mâini în buzunare, picioare care plutesc, margini care curg, elemente noi supra-saturate, față amestecată (Object Swap), produs duplicat (count lock), reflexii în oglindă. Plus `ffprobe` cu rezoluția reală (contradicția 4). (§2, §5)
8. **Costuri** (`config/costs.json`, `docs/11-costuri.md`):
   - prețurile OD se trec ca „raportat de terți, nemăsurat”;
   - regula `get_cost` înainte de fiecare lot;
   - se verifică factura Seedance cu video de referință (sursă + ieșire, +20–25%);
   - se compară cu `transactions` dacă refuzurile Genjutsu sunt rambursate. (§1.1, §1.2, §5)
9. **Analist** (`engine/analyze`, `docs/01-pipeline.md` pasul 2):
   - testăm `video_analysis_create` (MCP Higgsfield) pe 2 virale. Dacă e gratuit și corect, dă harta de cadre (tăieturi, mișcare, cameră) pe care o facem acum cu ffmpeg. Nu e unealtă de producție, dar cere confirmarea că nu consumă credite;
   - citim prompturile din Motion Library (`get_presets source=genjutsu`) și SKILL.md-ul Seedance din Higgsfield Academy, ca sursă de prompturi testate. (§1.1)
10. **Sourcing la test** (`docs/09-reguli-produs.md` regula 9, `engine/product-scout`):
    - furnizorul de test e CJ cu depozit în SUA, sau AliExpress/DSers doar pentru validare;
    - **o mostră la noi înainte de prima comandă de client**;
    - prețul se verifică pe 1688 (căutare după imagine). (§3)
11. **Sourcing la scalare** (`docs/09` §3, „câștigătorul primește tot”): la ≥ 10 comenzi/zi, oferte de la 2–3 agenți (HyperSKU, EPROLO, Sourcinbox) cu același link. Se aplică lista de verificare în 6 pași și semnalele de alarmă. La ≥ 100 comenzi/zi: comandă en-gros + 3PL în SUA. (§3)
12. **Cost real și livrare** (`docs/10-site-shopify.md`, `docs/09` regula 4): marja se calculează cu **taxele vamale incluse** (de minimis nu mai există), iar pe site se afișează termene de livrare oneste (chargeback-urile din vamă). Marjele exacte rămân de măsurat la primul produs. Ghidul nu le dă. (§3)
13. **Upscale**: nu intră în flux (regula din 10 oct). Propunem lui Szasz un singur experiment de cost: 720p + ByteDance `aigc` vs 1080p nativ, pe 3 clipuri. (§4)
14. **Decizii de cerut lui Szasz**:
    - fețele de pe Pinterest vs fețele generate (risc de filtre și drept la imagine, contradicția 12);
    - character sheet-ul cu vedere din spate pentru virale filmate din spate (experimentul #12);
    - brațele noi din A/B. (§5)

**Nano Banana (doar notă, nu e unealta noastră).** `NB` documentează Nano Banana 2 / Pro: referințe cu tipuri fixe (NB2: 10 obiecte + 4 personaje), Higgsfield implicit 1k pe `nano_banana_2`, mască doar pe NB2/Lite, fără seed și fără negative prompt. Două principii se aplică și la GPT Image 2.5: **referințe cu nume și rol** („Reference 1 is MAYA…”) și **reancorarea la generarea #1 după 3–4 editări**, nu la ultima ieșire. Unele surse OD (`GJ/20`, `MvO`) folosesc NB sau GPT pentru plăci și izolarea hainelor. La noi aceste pași se fac exclusiv cu GPT Image 2.5.
