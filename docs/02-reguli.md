# Reguli absolute LIMITLESS
Format: `- (data) regula — sursa`. Regula mai nouă bate regula mai veche.

## Dovedite (sept–oct 2026)
- (2 oct) Hook-ul trebuie să aibă sens: acțiunea se leagă de textul de pe ecran — Szasz.
- (2 oct) Reelul livrat e gata de postat: montat, text pe ecran, muzică, 15–18 s — Szasz.
- (2 oct) Referințele (personaj, cameră) doar din poze ≥ 1080 px — QA.
- (3 oct) Hook-ul se caută după ACȚIUNE + AUDIO din viral, nu după textul de pe ecran — Szasz.
- (5 oct) Hook-uri noi la fiecare lot, din virale încă nefolosite — Szasz.
- (5 oct) Muzica pornește de la secunda folosită de competitori; doar hook-ul are sunet propriu — Szasz.
- „A funcționat” = cifră (retenție / views peste mediană), nu impresie.

## Noi
- (9 oct) Sistemul e universal: funcționează pe orice produs și detectează singur ce și cum să facă în funcție de produs — Szasz.
- (10 oct) Distribuția (portal de postare cu echipă + conturi multiple) și tracker-ul de cifre fac parte din LIMITLESS — Szasz.
- (10 oct) Aplicația lucrează singură și în paralel: găsește viralele, le reproduce cu Higgsfield la cel mai mic cost (alt personaj, altă cameră), le montează complet, același stil la toate — Szasz.
- (10 oct) Produsele noi se caută în Meta Ads (Ad Library): ce vinde deja pe plătit aducem în organic — Szasz.
- (10 oct) BAZA DE UNELTE: folosim EXCLUSIV Genjutsu (`hf_mult_motion_control`), Seedance 2.5 (`seedance_2_5`) și GPT Image 2.5 (`gpt_image_2_5`). Alte modele Higgsfield (Kling, Veo, Sora, Soul, Nano Banana, Marketing Studio etc.) nu intră în producție — Szasz.
- (10 oct) Competitorii organici: prioritate conturile ON THE RISE pe nișă; un video cu ≥ 100k vizualizări într-o zi = dovedit că vinde → intră imediat în producție — Szasz.
- (10 oct) Aplicația propune mereu idei de variații custom ale produsului care se pot realiza (cu fezabilitate, mockup și test) — Szasz.
- (10 oct) Reguli clare pentru ce produs merită încercat și când facem variații, pornite din regulile lui Esteban (organic, ca noi) — `docs/09-reguli-produs.md` — Szasz.
- (10 oct) Site-ul fiecărui produs se face automat pe Shopify, pe baza întrebărilor lui Szasz; plățile prin alt procesator, nu Shopify Payments — `docs/10-site-shopify.md` — Szasz.
- (10 oct) La început TOTUL se face cu Genjutsu (cel mai ieftin): un video = viralul refăcut integral cu Genjutsu, personaj + cameră noi. Seedance 2.5 / GPT Image 2.5 doar când Genjutsu e respins sau nu se poate — Szasz.
- (10 oct) Din familia Genjutsu folosim MOTION CONTROL (`hf_mult_motion_control`): mișcarea din viral pe personajul + camera + produsul nostru. `hf_mult_replace_object` nu intră în producție — Szasz.
- (10 oct) Motion control rămâne implicit, dar la primul produs se TESTEAZĂ ambele (motion control vs replace_object) pe aceleași virale; câștigă cel cu calitate + rată de refuz + cost mai bune, apoi se decide definitiv — Szasz.
- (10 oct) Mergem mai ales pe videouri UGC: copiem videouri REALE (UGC care au mers) și le refacem cu personajul + camera + produsul nostru (Genjutsu motion control). Hook-urile și formatele se iau din UGC reale, nu se inventează — Szasz.
- (10 oct) LIMITLESS trebuie să fie o PLATFORMĂ (aplicație completă cu pagini: produse, virale, producție, distribuție, cifre, reguli), nu doar un panou — Szasz.
- (10 oct) Platforma LIMITLESS cuprinde TOATĂ afacerea la nivel mare (produse, conținut, distribuție, magazine, comenzi, customer support, fulfillment, bani). Szasz are controlul, dar totul se face automat — „ca un creier”. Design foarte șmecher, futuristic — Szasz.
- (10 oct) Hook-urile ating „butoanele sensibile” (psihologie din cele mai bune cărți de marketing) combinate cu tiparele competitorilor — `playbooks/carti-marketing-psihologie.md` — Szasz.
- (10 oct) Videourile trebuie să arate 100% naturale, ca UGC filmat cu telefonul de oameni reali; brandurile arată ca afaceri reale (site, pagini, ton). De aceea UGC e formatul principal — Szasz.
  Limite (Claude, 10 oct): fără testimoniale de la persoane care nu există (interzise de FTC 16 CFR 465 → videourile AI sunt demonstrație/POV, nu „am cumpărat și îmi place”); unde platforma cere eticheta de conținut AI realist, o respectăm (altfel risc de ștergere/ban). Recenziile de tip testimonial se fac cu creatori reali plătiți.
- 10 oct: la fiecare produs aprobat pentru test se caută automat supplierul (AliExpress / Alibaba / agenți / depozit US), cu cost aterizat și marjă — vezi docs/15-supplier-automat.md. Un singur site Shopify; fiecare produs testat primește propriul landing page.
- 10 oct: landing page-urile se fac după landing page-urile competitorilor care vând deja produsul (aceeași structură dovedită: ordinea secțiunilor, oferta, pachetele, garanția, FAQ), dar MEREU îmbunătățite: video UGC mai bun sus, ofertă mai clară, demonstrație, unghiul din insights, mobil mai rapid. Nu copiem textele, pozele sau recenziile lor cuvânt cu cuvânt; fără recenzii false și fără prețuri „înainte” false.
- 10 oct: tot ce generăm (imagini și video) arată filmat cu iPhone 18 Pro Max, stil UGC: telefon ținut în mână, lumină reală de cameră, încadrare de om obișnuit, fără look de studio sau de film. În prompt: „shot on iPhone 18 Pro Max, handheld UGC style”. Telefonul și logo-ul Apple nu apar în cadru.
- 10 oct: NU comandăm probe din produs. Videourile se fac după videourile virale: oamenii cu Genjutsu; cadrele unde „vedeta” e efectul (lumină, proiecție, transformare) se refac cu Seedance 2.5 folosind clipul viral ca referință de mișcare + start frame GPT Image 2.5 cu camera noastră; aspectul exact al produsului vine din pozele/videourile din listingul supplierului.
- 10 oct: la produsele cu B-roll greu de făcut cu Genjutsu (efecte: lumină, proiecție, transformare, produs fără om) analizăm TOATE videourile lor virale, găsim cadrele care se tot repetă între vânzători, facem pentru fiecare imagine de start (GPT Image 2.5, iPhone 18 Pro Max, UGC) și le animăm cu Seedance 2.5 după mișcarea din viral. Biblioteca de cadre e per produs și se refolosește în toate videourile.
- 10 oct: sistemul își dă seama SINGUR, la fiecare produs, care cadre sunt B-roll (fără om / efect) și care sunt cu om. Szasz nu marchează nimic: la orice produs nou, Analistul trece prin toate viralele, separă cadrele „om → Genjutsu” de cadrele „B-roll → imagine de start + Seedance”, găsește cele care se repetă și pregătește prompturile.
- 10 oct: în platformă NU găzduim videourile altora. Fiecare viral apare ca previzualizare (poză) cu link spre postarea originală (Instagram / Facebook / TikTok); ca să nu rămânem fără spațiu.
- 10 oct: Video boards pornesc de la zero, doar cu produsele noastre (tablele asociatului nu se mai afișează). În platformă e un chat („Ask the Brain”) căruia Szasz îi spune ce să facă; munca reală ajunge la Claude Code în „requests”.
