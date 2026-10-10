# Note — automatizări cu Claude Code, partea 1 (chunks/part1.txt)

Citit integral: 15 transcrieri (YouTube, 10–30 sept 2026). Doar ce e spus explicit în clipuri; cifrele creatorilor sunt **declarate**, nu verificate de noi. Secțiunea 6 e **derivată** (concluziile noastre).

Surse (scurtături folosite mai jos):
- [C] JS Mastery, „Claude Code Full Course 2026” — https://www.youtube.com/watch?v=u2QqWkMv3Lg
- [G] Automation Orbit, „AI Operating System (4 Layers)” — https://www.youtube.com/watch?v=Zs3faMCDYNs
- [M] Nate Herk, „What to Build Instead of AI Agents” — https://www.youtube.com/watch?v=HIRDzMtuWFk
- [I] Eric Tech, „AI-Native SDLC Guide” — https://www.youtube.com/watch?v=6CaQ9ZFuuKI
- [K] Ben AI, „Claude for Small Businesses (44 Skills)” — https://www.youtube.com/watch?v=f_CC5GRbiYA
- [H] RoboNuggets, „Jev will 10x your Claude Code” — https://www.youtube.com/watch?v=tTnUcSj-QPA
- [J] Nate Herk, „I Tested Jev on 12 Real Use Cases” — https://www.youtube.com/watch?v=ymgH8jS6Wb8
- [N] MrAlexTech, „AI MCP in DaVinci Resolve 21.1” — https://www.youtube.com/watch?v=dA6DuxffnRo
- [F] Mark Ai Guy, „Stickman niche … Artlist” — https://www.youtube.com/watch?v=AXF8u5mjDbc
- [L] Wholesale Ted, „Making Money Online With AI” — https://www.youtube.com/watch?v=P-ULbNbV5IQ
- [D] Nate Herk, „Opus 5.5 vs GPT-6 Astra (12 use cases)” — https://www.youtube.com/watch?v=GmLcJVzkxPA
- [E] Nate Herk, „Opus 5.5 vs GPT-6 Sol (10 use cases)” — https://www.youtube.com/watch?v=eF3yeJuifoQ
- [B] Nate Herk, „Sonnet 5.5 vs Opus 5.5” — https://www.youtube.com/watch?v=7eo-11K2e3c
- [O] Chase AI, „You're Using GPT 6 Astra Wrong” — https://www.youtube.com/watch?v=5EhrMJ9HIfU

---

## 1. Arhitectură de sisteme autonome

**Model → runtime → skill-uri („nu mai construi agenți separați”)** [M]
- Creatorii Agent Skills de la Anthropic (Barry Zhang, Mahesh Murag) spun că au încetat să construiască câte un agent separat pentru fiecare job: modelul = procesorul, runtime-ul agentului = sistemul de operare, skill-urile = aplicațiile. Același agent general primește un skill cu procesul, contextul, scripturile și exemplele.
- 4 reguli: (1) **scripturile reușite se salvează în folderul skill-ului** ca „unealtă pentru viitorul tău eu” — altfel Claude rescrie același cod la fiecare rulare, cu tokeni în plus și rezultate inconsecvente; (2) **descrieri precise** (progressive disclosure: la pornire se încarcă doar numele + descrierea; SKILL.md și referințele doar la potrivire); două skill-uri nu au voie să concureze pe aceeași cerere; test: o cerere evidentă, una formulată altfel, una fără legătură care NU trebuie să-l declanșeze; (3) **fiecare corectare devine regulă durabilă** în skill (proces greșit → SKILL.md; lipsă de context → fișier de referință; aceeași greșeală repetată → regulă explicită), apoi se rulează din nou aceeași sarcină; (4) **verificare înainte de predare**: criterii de acceptare definite înainte, apoi dovadă externă (screenshot, test, sursă, recenzie de la sub-agenți-persona: începător, cumpărător sceptic, om din public). „Prima ta privire nu trebuie să fie prima privire a agentului.”

**MAPS — 4 straturi ale unui „AI operating system”** [G]
- **Memory**: CLAUDE.md de ~40 de rânduri care nu conține fapte, doar „unde stă ce” (o linie pe arie → fișier-indicator → documente reale; orice fapt la 2 pași). Reguli: fiecare fapt are exact o casă; o verificare nocturnă marchează indicatorii spre fișiere mutate. Primul draft al hărții: Claude te intervievează ~20 min, o întrebare pe rând.
- Măsurat de autor: aceeași întrebare fără hartă 1 min 2 s / 28.000 tokeni; cu hartă 30 s / 17.000 tokeni (~40% mai puțin) — **declarat**.
- **Agent**: același Claude Code pe 2 mașini (laptop + VPS Hostinger), același folder sincronizat la 5 min în ambele sensuri; acces din Telegram prin mesaj vocal; rețea privată Tailscale; pe server un singur fișier de setări blochează orice unealtă care trimite/partajează/șterge (poate scrie un email, nu îl poate trimite).
- Spune că termenii Anthropic nu permit folosirea abonamentului Claude printr-un harness terț (ex. Hermes); permis: Claude Code rulat pe server, logat cu contul tău.
- **Pulse**: `routines.yaml` (rutină, scop, program, mașina) — un scheduler pe fiecare mașină îl citește la 5 min; fiecare rulare lasă o înregistrare; **plafon** ca o rutină care tot pică să nu ardă bugetul lunii peste noapte. Skill-uri de întreținere: cleanup, brain-build nocturn, vault-lint.
- **Screen**: „arată, nu stoca” — dashboard-ul doar citește fișiere; o singură listă așteaptă omul („needs human”), Claude nu marchează niciodată un task ca terminat. A fost plecat 10 zile cu laptopul închis, rutinele au mers.

**Unelte de bază Claude Code** [C]
- CLAUDE.md = fapte de proiect (ținut sub 200 de rânduri, ideal 30–40; formulări concrete, nu „cod de calitate”); `.claude/rules/*.md` cu reguli pe căi de fișiere; skill = proces repetabil; sarcină unică = prompt simplu. Automemory separat (MEMORY.md per proiect).
- CLAUDE.md e doar ghidaj; ce NU trebuie să se întâmple se pune în **permisiuni** (`.claude/settings.json`, ordine deny → ask → allow) sau hooks.
- Sub-agenții = **izolare de context**, nu „angajați” cu titluri; exemplu: 5 investigatori în paralel, 3 min pentru ~15 min de muncă. Pentru construcție paralelă: **git worktrees**, fiecare agent pe copia lui.
- `claude -p` rulează o sarcină și iese (pentru automatizări/CI; se poate pune output prin pipe).
- Skill cu efecte (deploy, commit) → `disable-model-invocation: true` (doar omul îl pornește). 10 skill-uri utile sunt ok, 100 aleatorii nu (fiecare adaugă metadata în context). `skill-creator` rulează evaluări cu/fără skill.
- Context rot: degradare măsurabilă de la ~50k tokeni dintr-o fereastră de 200k → `/clear` la sarcină nouă.

**Ciclul Anthropic „AI-native SDLC”** [I]
- intent.md (de ce: problemă, rezultat, utilizatori, constrângeri, întrebări deschise; produs după un interviu „grilling”) → spec.md (ce) → plan.md (fișiere, ordine, riscuri, cum se dovedește că e gata).
- „Dă-i lui Claude o buclă de feedback”: nu raportează „gata” până nu sunt verzi test + lint + build.
- Evals continue: 20–50 de sarcini reale deja rezolvate (prompt + output așteptat) rulate headless în CI când schimbi modelul sau regulile.
- review.md scris de om (ce se raportează, ce se ignoră); hooks care blochează acțiuni (credențiale în cod, fișiere interzise, merge în producție).
- După lansare: Claude citește metrici (Sentry/Datadog), poate face rollback, iar problemele recurente din ultimele 30 de zile devin un nou intent.md.

**Programare / rulare autonomă** [K]
- Pluginul „Small Business” (44 skill-uri, 35 de conectori). Skill-ul `smb-onboard` intervievează și salvează un fișier de context de business în memorie (inclusiv culorile brandului) pe care îl citesc toate celelalte skill-uri.
- Orice skill se programează cu „scheduled task” („rulează zilnic la 9:00”). Skill-urile se personalizează spunându-i lui Claude regula („mailurile de sponsorizare → roșu, fără răspuns”) sau cu **„record a skill”** (înregistrezi ecranul + vocea făcând sarcina, Claude rescrie skill-ul).
- `hiring-screener` a pornit **loturi de sub-agenți** pentru 200+ CV-uri → 23 da / 38 poate / 134 nu.

**Alte observații**
- Persistent cloud agents cu „heartbeat” la 30 min și tab de aprobări (Muse/Dots) [A: https://www.youtube.com/watch?v=BvvfZKKz4Yo].
- Opus ca orchestrator care trimite instrucțiuni foarte precise la muncitori ieftini — sugestie a autorului [E].
- Codex: voice mode ca orchestrator care deschide și urmărește mai multe chat-uri; „cere aprobare doar după ce ai pregătit un rezultat concret, verificabil” [O].

## 2. Montaj video automat cu Claude

**Hyperframes + skill de reel (Nate Herk)** [D][E]
- Sizzle reel 30 s din 105 GB de înregistrări (link Frame.io), editat cu „hyperframes”: Opus 5.5 — 31 min, ~10 $ (API), „sincronizat pe beat”, straturi, overlay cu opacitate, umbre; Astra 39 min, ~22 $, intro lent, energie slabă [D]. Același test vs Sol: Opus mai rapid cu 5 min, ~2× cost, net mai bun [E].
- Reel Instagram din înregistrarea lui, cu hyperframes + un skill de reel: Opus ~11 $, animații de tip „typing”, efecte sonore (uneori prea multe); Sol ~3 $, fără muzică, zumzet de fond, „nu l-aș posta” [E]. Autorul: „nici Opus nu e de postat fără iterații” [E].
- Reel animat 30 s „povestea mea”: Opus a folosit clona lui de voce ElevenLabs + personaj stil Pixar, ~8 $; Astra fără clonă, ~11 $ [D].
- Concluzia lui: modelele Claude au gust/creativitate la montaj și sound design; modelele GPT execută bine specificații clare [D][B].

**DaVinci Resolve Studio 21.1 — server MCP** [N]
- File → Setup AI Assistants instalează MCP-ul pentru Claude Code / Claude Desktop / Codex (sau cale spre `resolve MCP.exe` pentru LLM local).
- MCP-ul NU „apasă butoane”: Claude citește API-ul și **scrie un script** care rulează pe timeline; la fiecare cerere nouă rescrie scriptul (5–15 min, rezultate diferite).
- „Magic Script” (gratuit, Win/Mac): manager de scripturi salvate cu variabile; AI scrie scriptul o dată, apoi rulează local, offline, fără cost, și din Stream Deck. Exemple: sincronizare audio extern + grade + normalizare YouTube + timeline 4K (fără AI); tăiere tăceri și „erm” (transcriere locală); tranziții pe fiecare tăietură; dynamic zoom pe un track; slideshow; captions → SRT; thumbnail-uri din markere; **shorts verticale din markere-interval**, cu subtitrări.
- Principiul lui: omul ia deciziile creative (ce bucată e short), scriptul face munca repetitivă; alegerea automată a short-urilor cere AI de fiecare dată (cost).

**Pipeline „stickman” 100% în Claude + MCP Artlist** [F]
- Un prompt lung, pe etape: 10 idei → scenariu voice-over → prompt de foaie de personaj (expresii, haine) → foaie generată → prompturi de scenă → **6 scene generate cu Seedance 2.5 prin Artlist** în coadă → thumbnail → voice-over cu link de descărcare.
- Montajul rămâne manual în CapCut: viteza clipurilor ușor redusă ca să se potrivească cu vocea, muzică sub voce, captions automate (template „quick”).
- **Capcană observată: uneori începutul clipului generat arată o bucată din storyboard / foaia de referință → se taie.**

**DaVinci/ffmpeg/Remotion**: în partea 1 nu apare Remotion sau ffmpeg explicit.

## 3. Unelte / extensii noi

- **Jev (TypeSafe)** [H][J] — model „System 1”, nu LLM: răspunde doar în 3 forme (da/nu cu încredere, alegere dintr-un meniu, scor pe scară). Declarat: 20–200× mai rapid, 40–400× mai ieftin; output gratuit, input ~0,04 $/M tokeni; context de intrare doar 64k. Disponibil prin TypeSafe, OpenRouter, Vercel gateway.
  - Teste [J]: 1.000 emailuri × 7 clasificări → 70 s / 9 cenți (paralelizat: 6 s / 9 cenți); Luna 5 min / 62 cenți. 1.000 de comentarii YouTube → 5 s / 5 cenți. ~20.000 de cereri = 0,85 $. A clasificat și **clipuri tăiate din videourile lui: „se poate posta singur?”, „forța hook-ului”, tip de clip, „are replică citabilă?”**.
  - Utilizări [H]: rutare automată a modelului per sarcină (12 prompturi: −70% cost, 9/12 nu aveau nevoie de modelul de top) cu skill `/jev on|off`; alegerea skill-ului potrivit din 145 în ~5 s vs ~30 s cu Opus; căutare de imagini/video după sens, nu după nume de fișier.
  - Avertisment [J]: nu te încrede orbește — set de aur de 100 de cazuri cu răspunsuri corecte, rulat pe Jev vs Opus vs Sol, alegi balanța acuratețe/cost.
  - **Ne-ar ajuta**: da — triaj ieftin în masă (vezi §6).
- **DaVinci Resolve MCP + Magic Script** [N] — vezi §2. Ne ajută doar dacă montăm în Resolve; principiul (script salvat cu variabile) e valabil oricum.
- **Artlist MCP** [F] — conectare cu un click la Claude; generează imagini, Seedance 2.5, voce. Pentru noi: echivalent cu MCP-ul Higgsfield pe care îl avem deja.
- **Higgsfield prin CLI în Claude Code** [L] — Higgsfield oferă un prompt de instalare CLI „copy-paste”; autoarea generează cu Nano Banana Pro prin Higgsfield.
- **Claude in Chrome** [L] — pentru aplicații unde conectorul oficial e limitat (conectorul Canva nu dă acces la background remover) Claude Code folosește Canva în browser; 20 de variante de design + remove bg + upscale + export în „puțin peste o oră”.
- **Plugin Small Business** (Anthropic, 44 skill-uri) [K] — inbox manager (profil de voce din răspunsurile vechi), report builder, month-end prep, proposal builder, invoice chase, speed to lead, hiring screener, marketing Monday, review reputation. Pentru noi: tiparul „onboard → fișier de context citit de toate skill-urile” și „record a skill”.
- **Plugins oficiale** (ex. Stripe: skill-uri + MCP) și skill-uri publicate de biblioteci (`npx skills add …`) [C]. Citește SKILL.md și scripturile înainte de instalare.
- **CodeRabbit AI Deep Scan** [C] — al doilea sistem care verifică securitatea codului scris de Claude (segment sponsorizat).
- **Skill audit** (Chase AI) [O] — bazat pe skill-creator: găsește skill-urile nefolosite din loguri, verifică descrierile, le grupează (fix now / retire / test / preserve).
- **Hostinger VPS + Tailscale + bot Telegram cu voce** [G] — Claude Code mereu pornit, accesibil de pe telefon.

## 4. Business (toate cifrele sunt **declarate** de creatori)

- Canal stickman: 90.000 de abonați în 30 de zile, >900 $ în prima lună de monetizare; video de ~5 min făcut „în sub 5 minute” [F].
- Print-on-demand pe Etsy (Wholesale Ted): „peste 1.000 $/zi” din business-ul AI one-person; primele 2 vânzări în 2 săptămâni [L].
  - Avantaj: nișa în care ești tu însuți client (îți folosești gustul ca etalon) + „gol în piață” (tricouri pe rasă de câine). Cercetare: AI caută discuții unde nișa se plânge de probleme.
  - Flux: idei → imagini Nano Banana Pro prin Higgsfield → Canva (bg remover, upscale, PNG transparent 2×) → Printify → Etsy. Automatizat cu Claude Code + Higgsfield CLI + Claude in Chrome.
  - Algoritm (descris de ea pentru Etsy, „la fel pe YouTube, TikTok, Instagram”): impresii de test pe un grup mic → evaluare → extindere „bulgăre” către useri similari (multi-armed bandit). Dacă algoritmul alege grupul greșit, testul se stinge → titlu/descriere/taguri optimizate ca să fie clar cui se arată.
  - Altă idee menționată: modele AI de modă pe Instagram cu linkuri afiliate Amazon.
- Agenții de automatizare: „speed to lead” e una dintre cele mai livrate automatizări la clienți [K]; Automation Orbit vinde audituri de vizibilitate în căutarea AI (scor 47 → 62 pe site-ul lor) [G]. Salarii de 200–300k $/an pentru ingineri de agenți [C].
- Costuri reale (API, declarate) pe sarcini creative: 12 sarcini Opus 5.5 = 214 $ / ~11 h; Astra 132 $ / ~6 h [D]; 10 sarcini Opus 213 $ vs Sol 74 $ [E].

## 5. Capcane

- **Agenți paraleli în același folder își suprascriu fișierele** — Nate Herk a pierdut 2 din 10 teste: Codex a preluat fișierele lui Claude în timpul lucrului. Soluția lui: worktrees separate sau instrucțiunea „nu atinge munca altui agent” [E][D].
- AI-ul rescrie același script la fiecare rulare → cost, timp, rezultate diferite [M][N].
- Prea multe skill-uri / descrieri vagi → skill-ul potrivit nu se declanșează („un skill pe care Claude nu-l găsește e un skill pe care nu-l ai”) [M][C][O]. Schelele grele (superpowers, GSD) pot încurca modelele noi; Boris Cherny: „șterge-ți CLAUDE.md și skill-urile” care erau schele pentru modele vechi [O].
- CLAUDE.md nu blochează nimic; doar permisiunile/hooks [C]. Skill-urile descărcate pot conține scripturi periculoase [C].
- Context rot de la ~50k tokeni [C].
- Efort maxim ≠ calitate: Astra low 67% la 2,19 $/sarcină vs max 73% la 12 $; high = același scor ca max la 5,72 $ [O]. Pe o pagină web, efort light 13 min / 91k tokeni vs max 30 min / 152k, diferență neclară [O].
- „Aceeași sarcină, același model” poate degrada în timp (Astra la montaj și Canva, după autor) — de retestat periodic [D].
- Opus: pe prompturi vagi câștigă, dar poate costa 4–7× mai mult (joc 3D: Opus 60 $ / 1 h 45 min vs Sol 8,55 $) [E]; pe sarcini cu specificații clare și un mod de verificare → Sonnet (2/10 $ per M vs Opus 4/20 $) [B].
- Rutinele care tot pică pot arde bugetul peste noapte → plafon [G]. Programarea pe laptop se oprește când îl închizi [G].
- Videourile generate pot începe cu cadre din storyboard/foaia de referință [F].
- Jev: context 64k, nu scrie/rezumă; are nevoie de evals pe set de aur [J]. Opus a sărit peste o verificare de date (n-a pus întrebări unde Astra a întrebat) [D].
- MCP oficial limitat (Canva) → browser-use ca ocoliș [L].

## 6. Ce preluăm în LIMITLESS (DERIVAT — propunerile noastre, nu spuse de surse)

Legat de modulele din `docs/05-motorul-autonom.md`:

1. **Vânător / Analist — triaj ieftin în masă (tip Jev)**: înainte să plătim analiza completă a unui viral, un clasificator ieftin dă da/nu/scor pe sute de candidați („se potrivește cu produsul?”, „hook vizual în primele 2 s?”, „are mișcare reutilizabilă pentru Genjutsu?”). Doar primii X merg la Analist. De validat pe un set de aur de ~100 de videouri etichetate de noi [J][H]. (Jev nu e în baza de unelte de producție; e doar pentru clasificare — de decis cu Szasz.)
2. **Montaj — scripturi salvate, nu regenerate**: fiecare operație de montaj (tăieturi, ritm, text pe ecran, muzică, export 9:16) = script ffmpeg în `engine/` cu parametri din `library/stil.json`; Claude scrie scriptul o singură dată, apoi doar îl rulează [M][N]. Decizia creativă (ce bucată, ce hook) rămâne la Planificator/Szasz, execuția e deterministă [N].
3. **QA — tăierea primelor cadre**: verificare automată a primului și ultimului cadru al fiecărui clip generat (cadre de storyboard/referință la început, gol la final) [F]; plus regula „nu raportezi gata până nu trec toate verificările” (dovadă externă: cadre extrase, nu autoevaluare) [M][I].
4. **QA subiectiv cu persone**: pentru hook/text, 2–3 sub-agenți (privitor din nișă, cumpărător sceptic, „unde dau scroll?”); se aplică doar observațiile care apar de mai multe ori [M].
5. **Cartea de stil = context unic citit de toate skill-urile** (ca `smb-onboard`) [K]; corectările lui Szasz (`regula: ...`) se pun în „cel mai mic loc durabil” și se rerulează aceeași sarcină [M].
6. **Programarea (Routines)**: `state/routines.yaml` + jurnal pe fiecare rulare + plafon de eșecuri/credite pe rutină (oprire automată) [G]; o singură listă „așteaptă omul” în raportul zilnic; agentul nu marchează singur lucruri ca aprobate [G].
7. **Paralelism pe 10 produse**: fiecare linie de produs / producător lucrează în director sau worktree propriu; niciun agent nu scrie în folderul altuia [E][C]. Sub-agenții primesc sarcini înguste și întorc rezumate (izolare de context), nu „roluri” [C].
8. **Planificator — rutarea modelelor**: Opus pentru plan creativ / alegerea hook-ului / judecata de montaj; model mai ieftin (Sonnet sau Haiku) pentru pași cu specificație clară și verificare (descărcare, tăiere, formatare caption, actualizare stări) [B][D][H]; efort mediu implicit, crescut doar la eșec [O].
9. **Evals la schimbări**: 20–50 de cazuri reale (virale analizate + clipuri aprobate/respinse de QA) rulate când schimbăm modelul, skill-urile sau regulile, ca să vedem dacă QA/Analistul se strică [I][J].
10. **CLAUDE.md scurt ca hartă**: CLAUDE.md al LIMITLESS rămâne indicator spre `docs/`, `products/`, `state/`; o verificare nocturnă a linkurilor moarte din hartă [G][C]. Permisiuni pe sesiunile programate: fără ștergere și fără trimitere în afară, în afară de coada `distribution/` [G][C].
11. **Distribuție / Învățare**: modelul „test pe grup mic → bulgăre” [L] susține postarea mai multor variante de hook și păstrarea câștigătorilor după cifrele de la 24 h (deja în bucla Tracker) — **ipoteză**, de confirmat cu cifrele noastre.

## Sărite (fără învățături aplicabile noi)
- „OpenAI's Dots vs Meta's Muse” — Nate Herk — https://www.youtube.com/watch?v=BvvfZKKz4Yo (comparație de aplicații de asistent personal; s-a reținut doar ideea de heartbeat/tab de aprobări, în §1).
- Din comparațiile de modele [B][D][E][O] s-au păstrat doar părțile despre montaj video, cost, rutarea modelelor și efort; restul (site-uri, jocuri 3D, itinerarii, desen în Canva, deck-uri) e sărit.
