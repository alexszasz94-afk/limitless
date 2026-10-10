# Note — automatizări Claude Code, partea 2 (15 videouri, 10 sept – 8 oct 2026)

Sursă: `chunks/part2.txt`, citit integral. Doar fapte spuse explicit în videouri; cifrele lor sunt **declarate** (nu verificate de noi). Ce e marcat **(derivat)** e concluzia noastră, nu a lor. Ofertele și linkurile de cumpărat din videouri au fost ignorate.

Surse (codurile din text sunt linkuri):
[A] RoboNuggets, Artcraft (8 oct) · [B] WorldofAI, știri (7 oct) · [C] Christian Peverelli, montaj automat (4 oct) · [D] WorldofAI, știri (3 oct) · [E] Nate Herk, Claude Code Mods (2 oct) · [F] Calum Johnson cu Nate Herk, „AI OS” (28 sept) · [G] Nate Herk, montaj cu Opus 5.5 (25 sept) · [H] Chase AI, Jev + Claude OS (25 sept) · [I] Nate Herk, Opus 5.5 pe toate nivelurile de effort (24 sept) · [J] Rafa Voss, Jev (22 sept) · [K] Caleb Writes Code, Jev (19 sept) · [L] Nate Herk, business de o persoană (18 sept) · [M] Ray Fu, bot de trading (17 sept) · [N] Ishan Sharma cu Sanskar Tiwari, business cu Claude Code (13 sept) · [O] Money Talk With Leon, ghiduri PDF (10 sept)

---

## 1. Arhitectură de sisteme autonome

**„AI OS”: cele 4 C (Nate Herk)** [F]
- **Context**: tot ce știe despre tine și business, ca să nu mai repeți nimic. **Connections**: email, calendar, Slack, YouTube etc. **Capabilities**: skill-uri și automatizări. **Cadence**: pornite singure (programate sau declanșate de evenimente), ca să lucreze cât dormi.
- `CLAUDE.md` e „system prompt” și **ruter**: spune unde e fiecare lucru (wiki de strategie, voce/stil etc.). Regulile (ex. „verifică de 2 ori orice livrabil înainte să mi-l dai”) stau într-o secțiune de reguli din `CLAUDE.md`.
- Același director de fișiere merge în Claude Code, Codex, Hermes Agent, OpenClaw; „fișierele și folderele astea sunt tot IP-ul meu”.
- Primul pas recomandat: skill-ul **„grill me”** — te intervievează necontenit (până la ~50 de întrebări) până știe totul, apoi salvează contextul.
- Agenții „nu așteaptă comenzi, acționează proactiv”: cât a fost el în spital o lună, veniturile și vizualizările nu au scăzut (declarat).

**„Agentic OS” în 3 straturi (Chase AI)** [H]
- **Vizual**: dashboard propriu (web app sau plugin Obsidian) cu metrici, calendar, rapoarte; butoanele pornesc skill-uri printr-un Claude Code / Codex **headless**, deci oricine din echipă le poate rula fără să deschidă terminalul.
- **Memorie**: Obsidian e doar un vizualizator de markdown, „nu e RAG și nu dă memorie mai bună”. Contează doar structura de foldere. Modelul Karpathy: `raw/` (date brute) → `wiki/` (articole organizate) → `outputs/` (livrabile). În `CLAUDE.md` / `AGENTS.md` descrii structura și cum se adaugă fișiere noi, ca să nu se strice în timp.
- **Skill-uri (stratul cel mai important)**: (1) îi ceri să citească istoricul ultimelor 30+ zile de sesiuni și să propună skill-uri; (2) vorbești 10–20 min despre ce faci zi de zi și îi ceri să transforme sarcinile în skill-uri / automatizări. Livrabilele skill-urilor se întorc în dashboard.
- **Rutare cu Jev**: nivel 1 = comenzi simple, fără AI deloc („sute de milisecunde”); nivel 2 = model mic (Haiku / Luna); nivel 3 = Claude Code / Codex în terminal. Jev clasifică cererea. Voce locală: Whisper (ascultă) + Kokoro (vorbește).

**Skill = rețetă care se îmbunătățește singură** [C][F][G]
- Peverelli: skill-ul „YouTube-Edit” are ~1.400 de rânduri și 36 de reguli, scris de Claude. Metoda: începe cu bucăți mici (doar hook-ul), dă feedback cu timestamp („la secunda 22…”), apoi „salvează în skill ce ai învățat” → „nu a mai repetat greșeala” [C].
- Nate: metoda „bicicletei” — stai lângă el la primele rulări, corectezi, apoi „update the skill”; feedback pe ce e bun **și** pe ce e rău [F][G]. Fără pasul „update the skill” pierzi timp repetând [F].
- Skill-ul poate porni dintr-un exemplu: „analizează videoul ăsta, de ce e atât de bun?” → „transformă-l în skill” (așa a făcut skill-ul „motion show reel”) [G].

**Bucla de verificare (cel mai des repetat sfat)** [F][G][L]
- Prima trecere ≈ 60% din ce vrei; cu feedback + verificări ajungi la 100% [F].
- 3 tipuri: **screenshot** (orice e vizual: cadre video, HTML, site-uri), **fact-check cu sub-agent separat** (raport: 18 din 21 de afirmații confirmate, 1 depășită, 2 cu probleme), **browser / computer use** (agenții dau click în aplicație) [F].
- Leads: 9 agenți de research + **2 verificatori adversari** au prins 5 probleme reale înainte de livrare [F]. Clona Calendly: „cel puțin 50 de agenți” au testat UI-ul în 50 de browsere, apoi au reparat și au retestat [F].
- Ultimul pas din cei 5 pentru montaj: agentul se uită la propriul output, găsește greșeli și livrează versiunea 5–6, nu prima [G].
- Agenții sunt nedeterminiști: după o reparație, alt test pică (scor 88 → 88 → 94 pe un set de 16 teste „golden”). Cu cât setul de teste e mai mare, cu atât încrederea e mai mare [L].

**Programare și rulări lungi**
- `/goal` (în Claude Code, Codex, Hermes): lucrează „până e îndeplinită condiția”. Declarat: obiective de 10 min până la 6 zile; clona Calendly a rulat ~4,5 zile; montajul unui video lung 6–10 h, peste noapte [F]. Fără conexiuni și permisiuni setate dinainte, se blochează și cere aprobare [F].
- Automatizări săptămânale: rezumatul comentariilor („300 de comentarii → 3 probleme mari → idei de videouri”) și al întrebărilor din comunitate [F].
- Routines / scheduled tasks există, dar sistemul poate face și automatizări declanșate de mașina locală [H]. Botul de trading rulează cu un program local L–V la 9:30, cu log zilnic, dar **calculatorul trebuie să stea pornit** [M].
- Claude Code ≥ 2.1.292: se poate seta **effort separat pe fiecare sub-agent** (mic pentru sarcini simple, mare doar pentru partea grea; „economisește tokeni”) [B].
- Rulare paralelă manuală: Sanskar ține ~10 terminale Claude Code deschise, câte unul pe fiecare funcție sau aplicație, și trece pe la fiecare cu feedback; a ajuns de la 5 programatori la 0 (declarat) [N].

**Business de o persoană (Nate, după Dario Amodei)** [L]
- 3 filtre: (1) capital propriu (eliminat de el), (2) software, (3) vânzările și suportul se pot automatiza fără să strice experiența.
- Structură: produsul + agent de vânzări/suport + flux de găsit clienți. Agentul **califică** lead-urile și **redactează**, dar orice ține de bani sau date (refund, ștergere cont, trimitere email) ajunge la fondator.

## 2. Montaj video automat cu Claude

**Fluxul Peverelli (de la filmare brută la video final, „cât dormeam”)** [C]
| Rol | Unealtă |
|---|---|
| editor / coordonator | Claude Code desktop, **local** (are acces la fișiere și programe) |
| transcriere cu timestamp | **Parakeet** (NVIDIA, gratuit) |
| animații / titluri | **Hyperframes** (HeyGen, gratuit): Claude scrie animația ca pe o mică pagină web → video 4K |
| B-roll / dovezi | Chrome: capturi și înregistrări de pagini, evidențiere, zoom pe surse reale |
| ecran + cameră | Tella prin MCP |
| sunet / muzică | Epidemic Sound conectat la Claude; reguli: hook cu suspans, apoi lo-fi foarte încet |
| finisare | **ffmpeg**: lipire, taie ecranele negre, verifică sincronul audio |
- Rezultat: 2:46 de material brut → 31 s într-o singură trecere, în 10–20 min pentru un hook. Setup: permisiuni pe „auto”, model puternic pentru construcție, apoi poate merge pe unul mai ieftin.
- Ce a mers greu: efectele sonore alese la început erau „prea aglomerate”; a testat 8–10 sunete pe același hook până i-a plăcut unul.

**Fluxul Nate (Hyperframes + Opus 5.5)** [G][F]
- Instalare: îi dai lui Claude Code linkul repo-ului Hyperframes și îi spui „set it up”.
- Cei 5 pași: **transcrie** (Whisper local, gratuit dar lent; ElevenLabs API, plătit dar rapid) → **taie** greșelile și pauzele → **planifică momentele** („când spun X, să apară Y”) → **skill-uri** → **buclă de verificare** cu capturi.
- În pipeline-ul lui: transcriere → mai mulți agenți dezbat ce animație să apară în fiecare segment → randare Hyperframes în browser → **captură la fiecare ~3 s** → „vizionează” tot videoul, caută elemente ieșite din cadru sau nepotrivite cu brandul → refă. Exemplul livrat era **V8**; folderul are `assets`, `compositions`, `script`, `QA` [F].
- Generează singur imagini, apoi le trimite la Kling (prin key.ai) ca să devină video și le integrează în montaj [G]. Reclamă Lululemon: a luat imagini reale din catalog → video AI cu modelul în haine → montaj cu muzică pe beat [G].
- Toate exemplele au rulat pe effort **high** [G].
- Ce nu a ieșit bine: în sizzle reel-ul făcut din 105 GB de înregistrări au rămas tăieturi stângace în vorbire (3 prompturi, V2.1); în animația cu toast, ouăle erau prea mici și sosul doar pe o bucată (detaliile de conținut au scăpat) [G].

**Alte observații**
- Pentru ce produce AI-ul dintr-un singur prompt, „e mult mai greu să rafinezi”; uneltele cu straturi (After Effects / Premiere) dau drafturi mai slabe, dar ușor de rafinat [A].
- Reclame video și grafică din **HTML / Hyperframes**, fără model de imagine; 10 reclame recreate după cele care rulează de mult în Meta Ad Library [N].
- „Hyperframes + Chatterbox” = sute de videouri, „până la 200 într-o zi” (declarat), programate apoi prin API [N].

## 3. Unelte / extensii noi

| Unealtă | Ce face concret (spus în video) | Ne-ar ajuta? **(derivat)** |
|---|---|---|
| **Jev** (Typesafe, de la Diogo Almeida) [H][J][K] | Nu e LLM, ci clasificator: primește intrare structurată și dă **probabilități**, nu text. Tipuri: choice (o opțiune din listă), score (0–1 / 0–10), da/nu. Declarat: plătești doar tokenii de intrare; 40–200× mai rapid, 70–500 ms; ~20× mai ieftin decât Haiku la sortat emailuri (0,55 s față de 2,6 s Haiku și 5,8 s Sonnet). Acces: console.typesafe sau OpenRouter. Există o alternativă open-source pe Reddit (BERT, 421M parametri, rulează pe hardware obișnuit) [K]. | Da, pentru decizii ieftine în masă: scorul de potrivire viral ↔ produs, categoria hook-ului, rutarea între unelte. **Nu** s-a spus că primește imagini, deci nu poate face QA vizual. |
| **Mods** Claude Code [D][E] | Pluginuri (`/plugin`), câteva rânduri de TypeScript, sau îi ceri lui Claude să le facă. Exemple: *token weather* (cât de plin e contextul), *blast radius* (arată ce ar șterge, înainte să șteargă), *replay theater* (reia editările pas cu pas), *next steps*, *cache keeper*, *recording mode* (ascunde datele sensibile), tracker pentru `/goal`, *collision guard* (dacă alt chat a modificat fișierul în ultimele 30 min, te întreabă: continui / mut în worktree / anulezi). | Puțin: sunt mai ales de interfață (desktop), iar noi rulăm în cloud. Ideea de collision guard și cea de cache sunt utile în motor (vezi §6). |
| **Hyperframes** (HeyGen, gratuit) [C][F][G][N] | HTML animat → video, până la 4K, local, cost 0. Nate oferă gratuit un „Student Kit” cu skill-uri. | Da, pentru textul pe ecran, emoji și mici animații în Montaj, fără credite. Video generat tot doar cu uneltele noastre (Kling/key.ai sunt în afara regulii din 10 oct). |
| Parakeet / Whisper / ElevenLabs [C][G][H] | Transcriere cu timestamp: Parakeet și Whisper gratuite, ElevenLabs plătit și rapid. | Da: Analistul transcrie audio-ul viralelor (replici, beat-uri). |
| Epidemic Sound (connector), Tella (MCP) [C] | Muzică și SFX căutate de Claude; înregistrare ecran + cameră controlată din Claude. | Epidemic Sound: posibil, pentru muzică licențiată în Montaj (de verificat licența pentru reels). Tella: nu. |
| Artcraft (FilmCraft, EffectCraft, PhotoCraft…) [A][B] | Clone open-source (Rust) ale aplicațiilor Adobe, făcute cu Opus 5.5, cu **CLI + `agents.md`** ca să le poată conduce agenții. Încă la început, cu bug-uri. | Nu acum. Ideea de **CLI + agents.md** pentru uneltele noastre din `engine/` e utilă. |
| Claude in Chrome (`/chrome`) [N][C] | Deschide pagini, testează aplicația singur, face capturi și extrage reclame din Meta Ad Library. | Da: Vânătorul, pe Ad Library și pe paginile fără API. |
| post-bridge [N] | Programează postări pe multe platforme; Claude publică prin API key (Sanskar are ~15 conturi conectate). | Candidat pentru Distribuție, dacă alegem un serviciu de postare programată. |
| Zapier MCP / Zapier SDK [B][F] | Conectează la Claude aplicații fără connector propriu (ex. YouTube); SDK pentru 9.000+ aplicații. **Reclamă plătită** în ambele videouri. | Rezervă pentru conectori care lipsesc. |
| OpenRouter / OpenCode [J][N] | O singură cheie pentru multe modele; modele noi uneori gratuite o perioadă. | Doar pentru clasificatori ieftini (ex. Jev). |
| Cloudflare (Wrangler CLI) [N] | Hosting și bază de date gratuite, cu limite mari; deploy prin CLI. | Posibil, pentru portalul `distribution/`. |

## 4. Business (toate cifrele sunt declarate)

- **Montaj intern în loc de editor**: ~$27/video (≈$24 tokeni pe planul Max de $200, Tella ~$2, Epidemic ~$1), față de $250–1.000+ la un editor; publică în aceeași zi, nu în 3–7 zile [C].
- **Servicii AI pentru firme mici** e calea recomandată de Nate; unii au făcut „$10.000+/lună” predând ChatGPT firmelor. Prefixul „AI” va dispărea („AI consultant” → „consultant”). Nate: freelancer până la ~$10K/lună, apoi a angajat [F][L]. Gazda spune că Nate a avut o agenție de „sute de mii de dolari pe lună” [F].
- **Aritmetica SaaS**: „Agent Report Card” la $499/lună are nevoie de 168 de clienți pentru $1M ARR. **Nu are încă niciun client**; primul obiectiv sunt 5 agenții. Ofertă: durere → persoană → promisiune, nișă îngustă (agenți de suport clienți) [L].
- **Sanskar** [N]: 28+ produse, ~$20K MRR (vârf $26–29K); MagicSlides ≈ $695K încasări totale, celelalte aplicații > $100K. Un business nou de 45 de zile: „5 lakh+”. Reclame Meta: a pornit cu 500 INR/zi, a ajuns la 50.000 INR venit/zi la 6–7.000 INR cheltuiți.
  - Metoda: copiezi ce deja face bani (TrustMRR, CopyMRR) cu **un unghi nou**. Exemplu: o clonă Cal AI localizată pentru Rusia face „48 lakh/lună”.
  - SEO: cuvinte cheie ușoare (dificultate ≤ 20 în Ahrefs), apoi **video** pe tema lor, pentru că Google arată acum videouri YouTube / Instagram, tweet-uri și LinkedIn.
  - Instagram **trial reels**: Claude face videourile și le postează ca trial; le face publice doar pe cele care merg.
  - **Meta Ad Library**: o reclamă care rulează de luni de zile = convertește; o reproduci.
  - „Găsești câștigătorul și îl scalezi: același script în fiecare reel, cu altă persoană și altă locație.”
  - „Pune mai multe butoane de cumpărare pe internet; 9 din 10 produse eșuează, deci construiește 10.”
- **Ghiduri PDF** făcute cu Claude: „$600 într-o zi” pe un magazin Shopify nou, promovat gratuit pe X cu postări numerotate (1, 2, 3… cu link pe la mijloc). Unealta de idei recomandată e reclamă cu link afiliat [O].
- **AI OS ca produs**: dashboard-ul cu butoane care pornesc skill-uri se poate vinde echipelor și clienților [H].

## 5. Capcane

- **Costul crește repede cu effort-ul.** Același `/goal` (lume 3D din 105 GB de înregistrări) [I]:

  | effort | durată | cost API | tokeni | verificări |
  |---|---|---|---|---|
  | low | 16 min | $3,91 | 191K | 22 |
  | medium | 1 h 13 min | $12,44 | 419K | 23 |
  | high | 1 h 7 min | $16,31 | ~559K | 22 |
  | extra | 1 h 30 min | $25,92 | ~732K | 34 |
  | max | 2 h 28 min | $50,38 | 1,18M | 51 |
  | ultra code | 1 h 35 min | $18,69 | — | 42 |

  - Câștigător pentru calitate: **extra**, la jumătate din costul și timpul lui max. **Max** a avut mai multe verificări, dar mai multe bug-uri, și a trecut prin compactare. Max costă 12,9× cât low.
  - Ultra code „părea buggy” și nu a pornit workflow-urile dinamice.
  - Anthropic recomandă să pornești de la medium; medium îi ajunge pentru munca obișnuită.
  - **Niciuna** dintre rulări nu a folosit singură sub-agenți.
- **Cache-ul promptului expiră după ~60 min fără mesaj**; la următorul mesaj plătești din nou tot contextul. Pentru context lung: handoff + `/clear`, ca să eviți „context rot” [E].
- **Permisiunile**: fără „auto” / „bypass”, sesiunea se oprește la fiecare aprobare [C][M]; fără conexiuni setate dinainte, `/goal` se blochează [F].
- **Program local = calculatorul trebuie să stea pornit** [M].
- **Prima trecere ≈ 60%**; fără verificare ies afirmații false (3 din 21 de afirmații aveau probleme) [F]. Agenții sunt nedeterminiști: o reparație poate strica alt test [L].
- **Prea multe skill-uri sau reguli generale** produc efecte nedorite (ex. „fără albastru” aplicat și unde nu trebuia); citește skill-urile pe care le instalezi, nu le copia orbește [N]. Pentru design, dă exemple concrete (Dribbble, Pinterest) în loc de skill-uri lungi [N].
- **Montajul AI greșește la detalii de conținut** (tăieturi stângace în vorbire, obiecte prea mici sau puse greșit), chiar dacă tehnic e corect [G]. Cu prea multe SFX, sunetul devine aglomerat [C].
- **Supabase** pune proiectul pe pauză după 7 zile fără activitate și dă doar 2 proiecte gratuite [N].
- **Un rezultat dintr-un singur prompt e greu de rafinat** [A].
- **Atenție la sursă**: multe dintre aceste videouri vând comunități sau cursuri, sau au sponsori (Zapier, Hostinger, Vanta, Printify, Whisper Flow, Juni, PDF Trend Lab, Shopify); cifrele de venit nu sunt verificabile.

## 6. Ce preluăm în LIMITLESS **(derivat — propunerile noastre, legate de `docs/05-motorul-autonom.md`)**

1. **QA — verificator separat de producător.** QA-ul să fie alt agent (sau sub-agent) decât Producătorul, cu instrucțiunea „caută ce e greșit” (după cei 2 verificatori adversari care au prins 5 probleme [F]).
2. **QA final pe MP4 montat**, ca la Nate [F]:
   - `ffmpeg` extrage un cadru la ~3 s, plus primul și ultimul cadru;
   - agentul cu vedere le verifică după Cartea de stil;
   - înainte, un pas fără AI în `engine/`: `blackdetect` / `silencedetect` și verificarea sincronului audio [C], ca să nu plătim vederea pe clipuri stricate.
3. **Set „golden” pentru QA**: 20–30 de clipuri deja judecate (acceptate sau respinse, cu motivul), pe care rulăm QA-ul la fiecare schimbare de prompt sau model, ca să știm dacă îl putem lăsa nesupravegheat [L].
4. **Cartea de stil = skill care învață.** După fiecare feedback de la Szasz sau din cifre, pasul fix „scrie regula în `docs/06-carte-de-stil.md` / `library/stil.json`” (modelul „update the skill”, 36 de reguli la Peverelli [C][F][G]). Feedbackul cu timestamp („la 0:03 textul e prea jos”) se transformă direct în regulă.
5. **Analist — „de ce e bun viralul?”.** Pentru fiecare viral: transcriere cu timestamp (Whisper/Parakeet, gratuit), cadre, apoi întrebarea explicită „de ce funcționează?”. Rezultatul se salvează ca șablon reutilizabil, nu doar ca fișă [G].
6. **Montaj — Hyperframes pentru textul de pe ecran, emoji și mici animații** (HTML → MP4, 0 credite), lipite cu `ffmpeg`. Rămâne treapta „fără AI” din scara de cost. De testat: cât arată a CapCut și cât durează randarea.
7. **Vânător / Planificator — clasificator ieftin (Jev sau un model mic)** pentru decizii în masă: scorul de potrivire viral ↔ produs, tipul hook-ului, unealta din scară. Claude și vederea rămân doar pentru ce trece de filtru [H][J][K]. De testat prețul real; nu e dovedit că primește imagini.
8. **Effort pe agent**, nu global [B][I]:
   - low / medium: Vânător, Distribuție, Tracker;
   - medium / high: Analist, Planificator;
   - extra doar pentru lotul greu de montaj sau QA;
   - niciodată max în Routines (cost dublu față de extra, fără câștig [I]).
   - Sub-agenții paraleli trebuie ceruți explicit, altfel nu apar [I].
9. **Routines — sesiuni scurte, fără context lung.** Fiecare Routine citește starea din `state/`, lucrează, scrie un handoff în `state/` și se închide. Evităm cache-ul expirat (~60 min) și „context rot” [E]. Rulările lungi se fac ca `/goal` cu condiție de oprire clară („N videouri trecute de QA” **sau** „buget atins”) [F].
10. **Cozi paralele — „collision guard” în `engine/queue`.** Fiecare video are un singur agent-proprietar (lock în fișierul de stare); un alt agent nu scrie peste el [E].
11. **Memorie — structura `raw/` → `wiki/` → `outputs/`** pentru `library/` (virale brute → fișe/șabloane → MP4-uri), descrisă în `CLAUDE.md` ca să nu se strice în timp; `CLAUDE.md` rămâne ruter [H][F].
12. **Distribuție — testare cu trial reels.** Variantele (hook-uri sau texte diferite) se postează ca trial reels pe Instagram; doar câștigătoarele devin publice și se repostează pe alte conturi [N]. De verificat dacă se poate prin API sau doar din telefon (posterii).
13. **Învățare — „scalează câștigătorul”**: același script câștigător, refăcut cu alt personaj și altă cameră pe mai multe conturi [N]. Se potrivește exact cu rotația de seturi; câștigătorul îl alegem după cifre.
14. **Vânător — semnalul „reclamă care rulează de mult”** din Meta Ad Library (citită cu Claude in Chrome), pe lângă outlier-ii organici [N].
15. **Tracker — rezumat săptămânal al comentariilor** (obiecții, întrebări, ce cer oamenii) → idei de hook-uri și răspunsuri în caption [F].
16. **Skill-uri din istoric**: o dată pe lună, un agent citește sesiunile din ultimele 30 de zile și propune skill-uri noi sau reguli pentru ce se repetă [H].
17. **Unelte din `engine/` cu CLI + un `AGENTS.md` scurt**, ca orice agent să le poată folosi fără explicații lungi [A].
18. **Portalul pentru Szasz = „stratul vizual”**: rapoartele zilnice și câteva butoane care pornesc skill-uri headless (ex. „regula: …”, „oprește produsul X”) [H].
19. **Banii trec mereu pe la om**: agenții redactează și propun, dar bugetul și orice cheltuială nouă o aprobă Szasz [L]. E deja în docs/05.

**Ce NU preluăm:**
- Kling / key.ai / Nano Banana pentru generare: regula din 10 oct permite **doar** Genjutsu, Seedance 2.5 și GPT Image 2.5.
- Ca reper de preț: GPT Image 2.5 ≈ $0,07/imagine și ~50 s, față de Nano Banana 2.1 ≈ $0,04 și ~11 s [B].

---

## Sărite (fără învățături aplicabile, sau doar parțial folosite)
- [B] WorldofAI 7 oct: GPT „Bel” / matematică, Mistral Large 4, Mythos 5.1, Gemini Embedding 2. Folosite doar: effort per sub-agent, prețul GPT Image 2.5 și Zapier SDK.
- [D] WorldofAI 3 oct: scurgeri Fable 5.5, Gemini 4 Argon, DeepSeek harness, Ling 3.1 Flash. Folosite doar: anunțul Mods și faptul că Fable 5.5 a generat prin cod o animație de 15 s în ~1 h.
- [M] Ray Fu, bot de trading cu Alpaca MCP. Folosit doar ca exemplu de capcană (program local).
- [O] Leon, ghiduri PDF. Folosit doar în §4; în rest e promovare de unelte cu link afiliat.
- [A] Artcraft: folosită doar ideea CLI + agents.md.

[A]: https://www.youtube.com/watch?v=Fuo1i_-9Frc
[B]: https://www.youtube.com/watch?v=-mv1Tf26Vms
[C]: https://www.youtube.com/watch?v=HzXD4GVqXwM
[D]: https://www.youtube.com/watch?v=N3REfH4N9Dg
[E]: https://www.youtube.com/watch?v=9hetShMMp2s
[F]: https://www.youtube.com/watch?v=DD-SiFV93sQ
[G]: https://www.youtube.com/watch?v=7jHXoPGnA4c
[H]: https://www.youtube.com/watch?v=EOdXR6lU5ZA
[I]: https://www.youtube.com/watch?v=QCkHIyEPIYo
[J]: https://www.youtube.com/watch?v=hp6kG1bLMc4
[K]: https://www.youtube.com/watch?v=vj7hysh0mOI
[L]: https://www.youtube.com/watch?v=QDsenEcAJIk
[M]: https://www.youtube.com/watch?v=oQdkFPhqaGk
[N]: https://www.youtube.com/watch?v=4z_RDr5py10
[O]: https://www.youtube.com/watch?v=-pp851qDmOY
