# 12 — Strategul LIMITLESS: piața acum și ce putem face mai bine

Data: 10 oct 2026 · Autor: agentul Strateg (la cererea lui Szasz: „studiază piața, uită-te la ce vreau să fac și vino cu idei”).
Surse: planul din `docs/00`–`docs/11`, `playbooks/esteban.md`, `playbooks/carti-marketing-psihologie.md`, `playbooks/higgsfield-mecanica.md`, `library/sources/claude-code-automations/notes-part1/2.md`, `config/costs.json` + research web (linkuri la fiecare afirmație).

> **Cum se citește.** **[sursă]** = cifră găsită pe web (link). **[declarat]** = spus de Esteban / clienții lui, neverificat. **[calcul]** = socoteala noastră din cifrele de mai sus. **[nesigur]** = n-am găsit sursă bună. Multe surse web sunt bloguri de firme care vând servicii; unde e așa, scrie. Regula din `CLAUDE.md` rămâne: fără cifra noastră, totul e ipoteză.

---

## Rezumat în 10 puncte (pentru Szasz)

1. **Piața e mare și crește**: americanii vor cheltui online ~275 miliarde $ în noiembrie–decembrie (+6,7%), iar rețelele sociale cresc mai repede ca vânzări decât Google. Ai ales sezonul bun.
2. **Calendarul e mai scurt decât pare.** Black Friday e pe 27 nov, Cyber Monday pe 30 nov. Dacă trimitem din China, ultima comandă care ajunge sigur de Crăciun e pe la **1–5 decembrie**. Din depozit în SUA, până pe 17 decembrie. Practic avem **~7 săptămâni bune**, nu 10.
3. **5 M$ înseamnă ~1 miliard de vizualizări** la cifrele lui Esteban (~5.000 $ la 1M de vizualizări). E de ~50 de ori cea mai bună lună declarată de el. Se poate apropia doar dacă prindem **2–3 produse câștigătoare** până la 1 noiembrie și le dăm tot.
4. **Cea mai mare schimbare propusă: mai puține produse, mai repede.** Testăm 5 produse acum (nu 10), alegem câștigătorii până pe 1 noiembrie, iar platforma „creier” completă o construim după Crăciun. Până atunci construim doar drumul de bani: video → postare → vânzare → livrare.
5. **Câștigătorul trece în depozit SUA.** Livrare în 3–7 zile în loc de 2–4 săptămâni: mai puține plângeri „unde e coletul”, mai puține dispute la bancă și vânzări de Crăciun până pe 17 decembrie.
6. **Banii pot fi blocați.** Un magazin nou care crește brusc primește des „rezervă” (o parte din bani ținută 60–180 de zile). Peste un anumit procent de dispute, Visa penalizează. Ne trebuie un procesator de rezervă, livrare rapidă și răspuns rapid la clienți.
7. **Atenție la „recenzia” făcută cu AI.** În SUA e interzis (regula FTC, din 2024) să arăți o recenzie de la cineva care nu există. Videourile noastre UGC trebuie să fie **demonstrații**, nu „am cumpărat și îmi place”.
8. **Platformele cer etichetă de AI** pentru videouri realiste (TikTok, YouTube, iar Meta pune eticheta singură). Nu ștergem eticheta: riscăm conturile. Pe Meta, eticheta pare să nu scadă vizualizările; copierea pur și simplu le scade.
9. **Taxele vamale au crescut.** Scutirea de 800 $ pentru colete nu mai există, iar produsele din China plătesc ~20–40% taxă vamală. Prețul și marja trebuie recalculate pe fiecare produs.
10. **Ce face un video să ajungă departe pe Instagram** acum: cât e privit, câte trimiteri (share în DM) și câte like-uri primește, raportat la câți l-au văzut. De Crăciun, cel mai bun unghi e „**trimite-i asta cuiva**” (cadoul). Pe deasupra, un **cod de reducere pe fiecare cont** ne arată exact ce cont și ce hook aduce bani.

---

## Piața acum (oct 2026)

### Sezonul Q4 în SUA
| Ce | Cifra | Sursa |
|---|---|---|
| Cheltuieli online 1 nov – 31 dec 2026 | **275,1 mld $, +6,7%** | [Adobe, 28 sept 2026](https://www.businesswire.com/news/home/20260928285775/en/Adobe-U.S.-Holiday-Shopping-Season-to-Hit-Record-$275.1-Billion-Online-Rising-6.7-YoY) · [Digital Commerce 360](https://www.digitalcommerce360.com/2026/09/29/adobe-projection-2026-online-holiday-sales-275-billion/) |
| Cyber Week (Thanksgiving → Cyber Monday) | 47,5 mld $, **17,3% din sezon**; Cyber Monday > 15 mld $ | [Adobe via Digital Commerce 360](https://www.digitalcommerce360.com/2026/09/29/adobe-projection-2026-online-holiday-sales-275-billion/) |
| Octombrie | 95,8 mld $ (+8%) — reducerile încep devreme | [Common Thread Collective (citând Adobe)](https://commonthreadco.com/blogs/coachs-corner/adobes-275-billion-holiday-forecast-is-here-what-ecommerce-brands-must-do-before-black-friday) |
| Categorii care cresc cel mai repede | cosmetice +9,5%, jucării +9,6%, mobilă/casă +7,3%, alimente +10,3%; îmbrăcămintea doar +4,7%, electronicele +5,9% | [ppc.land / Adobe](https://ppc.land/adobe-puts-us-online-holiday-spend-at-275-1-billion-up-6-7/) |
| Din ce surse vin vânzările | social media **+17%** ca venituri, afiliați +12%, căutare plătită +4%; traficul din AI +130% | [Digital Commerce 360](https://www.digitalcommerce360.com/2026/09/29/adobe-projection-2026-online-holiday-sales-275-billion/) · [ppc.land](https://ppc.land/adobe-puts-us-online-holiday-spend-at-275-1-billion-up-6-7/) |
| E-commerce total sărbători (altă metodă) | 316–319 mld $, +7,5–8,4% | [Deloitte via MarketScale](https://www.marketscale.com/industries/retail/holiday-e-commerce-will-reach-up-to-319-billion-this-season-deloitte-forecasts) |
| Buget mediu de cadouri / persoană | 708 $ (−2% față de 2025); 79% spun că reducerile decid când cumpără | [PwC Holiday Outlook 2026](https://www.pwc.com/us/en/industries/consumer-markets/library/holiday-outlook-trends.html) |
| De unde iau idei de cadouri | social media **46%** (la egalitate cu magazinele fizice); Gen Z 54%, milenialii 50%, boomerii 31%; codul promo e motivul nr. 1 de cumpărare de pe social (30%) | [Sprout Social Q3 2026](https://sproutsocial.com/insights/holiday-shopping-trends/) |
| Unde cumpără efectiv | doar **9%** pe social media, 38% pe site-uri | [PwC](https://www.pwc.com/us/en/industries/consumer-markets/library/holiday-outlook-trends.html) |

**Ce înseamnă pentru noi:** oamenii descoperă cadourile pe Reels / TikTok, dar cumpără pe site. Asta se potrivește cu planul nostru (video organic → magazin propriu). Cosmeticele/beauty și casa cresc mai repede decât hainele.

### Calendarul real (calcul)
- Thanksgiving **26 nov**, Black Friday **27 nov**, Cyber Monday **30 nov** 2026 [calcul, calendar].
- Termenele USPS pentru livrare de Crăciun (din depozit SUA): Ground Advantage **17 dec**, Priority **18 dec**, Express **19 dec** ([USPS via Dakota News Now](https://www.dakotanewsnow.com/2026/09/23/usps-announces-recommended-2026-holiday-mailing-shipping-deadlines/)).
- China → SUA: YunExpress 5–15 zile anunțat, **12–26 zile** în practică după o sursă; ePacket 7–30+ zile în sezon ([elextensions](https://elextensions.com/yunexpress-shipping-times-to-the-us/), [oneshippros](https://oneshippros.com/china-dropshipping-shipping-methods/)) → ultima comandă livrată din China înainte de Crăciun ≈ **1–5 decembrie** [calcul, nesigur: depinde de furnizor].

### Tarife și de minimis
- Scutirea de 800 $ a dispărut pentru China din mai 2025 și pentru toate țările din aug 2025; CBP a făcut-o pe termen nedefinit din iunie 2026 ([CMGM](https://www.cmgm.net/us-de-minimis-exemption-ended-2026-china/), [china-fulfillment](https://www.china-fulfillment.com/us-de-minimis-ended-2026-china-sellers-guide.html)). Împărțirea comenzii în colete mici nu mai ajută.
- Curtea Supremă a anulat tarifele IEEPA (20 feb 2026); rămân Section 301 (7,5–25% după listă), plus un nou tarif de 12,5% (sursele se contrazic). Rata totală estimată pentru un produs de consum chinezesc: **~21% până la ~37,5%** ([China Briefing](https://www.china-briefing.com/news/supreme-court-tariff-ruling-china-impact/), [hsrates](https://hsrates.com/en/guides/us-tariffs-on-china-2026/), [tariffstool](https://www.tariffstool.com/tariffs-from-china)). **[nesigur]**: rata exactă depinde de codul HTS al fiecărui produs.
- Livrarea „DDP” a furnizorului include deja taxa în preț; trebuie cerută explicit.

### Platformele: algoritm și politici
| Subiect | Ce am găsit | Sursa |
|---|---|---|
| **Instagram: ce contează** | timpul de vizionare, **trimiterile raportate la câți l-au văzut** (cel mai legat de cei care nu te urmăresc) și like-urile raportate la vizualizări. Ponderea „3–5× un like” circulată pe net **nu are sursă** | [dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers), [creatorlanehq](https://creatorlanehq.com/blog/instagram-algorithm-2026-mosseri-vs-measured) |
| **Trial Reels (IG)** | merg doar la cei care nu te urmăresc; conturi publice cu ≥ 1.000 urmăritori; se pot programa | [ucompares](https://ucompares.com/social-media/instagram/instagram-trial-reels/), [lesliemlyon](https://lesliemlyon.com/can-trial-reels-go-viral-algorithm/) |
| **Conținut neoriginal (IG)** | repostările sunt înlocuite cu originalul în recomandări; pragul „10 în 30 de zile” **n-are sursă primară** | [creatorlanehq](https://creatorlanehq.com/blog/instagram-algorithm-2026-mosseri-vs-measured) |
| **Conținut neoriginal (FB)** | din iul. 2025: conturile care refolosesc repetat conținutul altora pierd monetizarea și primesc **distribuție redusă pe TOT ce postează**; „editările minore” nu contează ca original; 500.000 de conturi penalizate în S1 2025; vizualizările Reels originale ~×2 în S2 2025 | [Social Media Today](https://www.socialmediatoday.com/news/meta-adds-more-measures-to-ensure-original-creators-get-credit/814764/), [Influencer Marketing Hub](https://influencermarketinghub.com/facebook-push-against-unoriginal-content/), [CineRads](https://www.cinerads.com/blog/facebook-ai-content-monetization-policy) |
| **Eticheta AI la Meta** | „AI info” pus automat din metadate sau manual; o sursă spune că Meta a declarat că eticheta **nu scade reach-ul**; conținutul realist înșelător primește etichetă mai vizibilă și distribuție redusă | [Metricool](https://metricool.com/how-to-label-ai-content/), [Coinis](https://coinis.com/blog/meta-ai-content-labeling-facebook-instagram-ads-2026), [Primotech](https://primotech.com/meta-to-labe/) |
| **Eticheta AI la TikTok** | „realist = etichetă” obligatoriu; citește C2PA și pune eticheta singur; nedeclarat → etichetă pusă de TikTok → ștergere → strike pe cont | [CineRads](https://www.cinerads.com/blog/tiktok-ai-content-policy), [hypelive](https://www.hypelive.io/en/blog/tiktok-ai-content-rules-2026) |
| **YouTube** | clarificare 16 iul 2026: conținutul „produs în masă / după șablon” nu e monetizabil; AI-ul realist trebuie declarat („altered or synthetic”) | [TechCrunch, 20 iul 2026](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/) |
| **„Comment WORD” (ManyChat)** | n-am găsit regula oficială Meta. Anecdotă: același cuvânt n-a avut probleme pe IG, dar pe **Facebook** a primit avertisment „Engagement Baiting” pe 3 postări. Răspunsurile publice identice sub fiecare comentariu = risc | [ManyChat community](https://community.manychat.com/general-q-a-43/facebook-comment-automation-engagement-baiting-3481), [dealism](https://dealism.ai/blog/is-manychat-safe-for-instagram-a-clear-objective-guide) — **[nesigur]** |
| **Link în bio TikTok** | de regulă ≥ 1.000 urmăritori sau cont Business înregistrat | [outfy](https://www.outfy.com/blog/?p=14299) — bloguri |

### Lege (SUA): recenzii și testimoniale
- Regula FTC 16 CFR 465 (în vigoare din 21 oct 2024) interzice recenziile și testimonialele **de la persoane care nu există, inclusiv generate cu AI**, sau de la cineva fără experiență reală cu produsul. Amenzile ajung la ~52.000 $ **pe încălcare** ([Hunton](https://hunton.com/hunton-retail-law-resource/ftc-issues-final-rule-targeting-fake-consumer-reviews-and-testimonials-including-those-generated-by-artificial-intelligence-ai-and-online-bots), [Freshfields](https://blog.freshfields.us/post/102jh9p/ftc-announces-final-rule-on-deceptive-reviews)). Regula interzice și cumpărarea de urmăritori sau vizualizări false.
- **Asta ne atinge direct:** refacem UGC reale cu un personaj AI. Dacă personajul spune „I bought this and it changed my winter”, avem un testimonial de la o persoană inexistentă. Detalii în §Riscuri.

### TikTok Shop vs magazin propriu
- TikTok Shop cere **expediere în 2 zile lucrătoare** (scanare „In Transit”). Peste 10% întârzieri înseamnă sancțiuni. Pentru coletele transfrontaliere există o listă albă de curieri din feb 2026 ([hereweship](https://hereweship.com/en/tiktok-shop-shipping-2026-meet-2-day-dispatch-sla/), [shoplazza](https://www.shoplazza.com/blog/tiktok-shop-policy-update), [looperbuy](https://looperbuy.com/blog/tiktok-shop-dropshipping-policy-2026-a-b2b-experts-guide-to-compliant-global-sourcing-with-looperbuy.html)). Cu dropshipping clasic din China nu se poate. Cu stoc în SUA, da.
- Sursele se contrazic dacă dropshipping-ul mai e permis; **[nesigur]**.
- **Concluzie:** magazinul propriu pe Shopify rămâne baza. TikTok Shop e o opțiune **doar pentru câștigătorul cu stoc în SUA**: aduce afiliați și coș în aplicație.

### Plăți și dispute
- Shopify acceptă procesatori externi, dar pe planul Basic adaugă un **comision de 2%** peste comisionul procesatorului (1% pe Shopify, 0,5% pe Advanced) ([Shopify Community](https://community.shopify.com/t/why-does-shopify-charge-a-2-transaction-fee-for-third-party-providers/246613/44), [firstpier](https://www.firstpier.com/resources/shopify-merchant-fees)). La 5 M$ venit, diferența dintre 2% și 0,5% = **75.000 $** [calcul].
- Procesatorii „high-risk” costă ~4–7,5% total, față de ~2,6–2,9%. Rezervele tipice: **20% din venit ținut 60 de zile**, sau sume blocate 30–180 de zile; o creștere bruscă a disputelor poate aduce rezervă în 48 h ([Chargeflow](https://www.chargeflow.io/blog/best-shopify-payment-gateways), [Tailoredpay](https://tailoredpay.com/blog/high-risk-merchant-account-shopify/)). Sursele sunt firme care vând aceste servicii.
- Visa VAMP: pragul „excesiv” pentru comercianți a scăzut la **1,5%** din 1 apr 2026 (fraude + dispute / tranzacții, de la 1.500 de evenimente/lună). Procesatorii au praguri mai mici, 0,5–0,7% ([Justt](https://justt.ai/blog/visa-vamp-threshold-changes-april-2026/), [Redo](https://redo.com/resources/articles/chargebacks/vamp-2026-shopify)).

### Benchmark-uri de conversie
- Shopify: mediana ~**1,4%** conversie (date Littledata, 2023), top 20% ~3,2%, top 10% ~4,5% ([popupsmart](https://popupsmart.com/blog/shopify-conversion-rate-statistics), [cartylabs](https://cartylabs.com/blog/good-shopify-conversion-rate/)). Pe categorii, sursele diferă mult: beauty ~4,5–4,9%, fashion ~1,6–3,1%, casă ~1,4% ([growthsuite](https://www.growthsuite.net/resources/shopify-conversion-rate/complete-guide/benchmarks-by-industry)).
- AOV pe categorii: **[nesigur]**, nu există un set de date credibil pentru 2026. AOV-ul mediu general citat e ~80–120 $.
- „CPM organic”: nu se aplică. Măsura noastră este **$ la 1M de vizualizări**: 2–6k $ în mod obișnuit, 20k $+ la transformare [declarat, Esteban].

---

## Ce face bine planul tău (scurt)

- **Măsoară totul în cifre** („fără cifră = ipoteză”) și are bucla de învățare scrisă (`docs/05`).
- **Validează produsul cu bani reali** (test order, $/1M, ≤ 4 concurenți, „edge” obligatoriu — `docs/09`).
- **Costul de producție e mic față de venit**: ~44 de credite pe bucată Genjutsu, iar biblioteca refolosită coboară costul pe video de ~5–10 ori (`docs/11`).
- **Refacerea cu alt personaj și altă cameră** e mult mai sigură decât repostarea, pe care Meta o penalizează explicit.
- **Interdicțiile din „Ce NU facem”** (`playbooks/carti-marketing-psihologie.md` §5) sunt deja corecte: fără urgență falsă, fără experți falși, fără IP.
- **Accentul pe SUA 25+, pe Facebook și pe cadou** se potrivește cu datele: social media e sursa nr. 1 de idei de cadouri.

---

## Ce poți face mai bine

Ordinea de mai jos e după **impact × ușurință**: primele sunt cele cu cel mai mult câștig pentru cel mai puțin efort.

### 1. Calendar „de război”: mai puține produse, mai repede, construim doar drumul de bani
- **Ce:** 5 produse în test între 13 și 26 oct (nu 10). Până pe **1 nov** alegem 1–2 câștigători, care primesc tot volumul și conturile. Încă 1–2 produse noi intră în test pe săptămână. Platforma completă (customer support, fulfillment, dashboard futurist) se construiește după 15 dec. Până atunci construim doar: produs → video → postare → vânzare → livrare.
- **De ce:** Esteban: „5+ produse în test, în ~2 săptămâni unul lovește, apoi all-in” [declarat, A11]. La el viralul vine după 2–4 săptămâni de postare [declarat, A10][B12]. Cyber Week aduce 17,3% din sezon ([Adobe](https://www.digitalcommerce360.com/2026/09/29/adobe-projection-2026-online-holiday-sales-275-billion/)). Azi `products/` e gol, iar distribuția nu e instalată. Fiecare săptămână de construcție înainte de primul post e o săptămână pierdută din cele ~7.
- **Cum în LIMITLESS:** `docs/03-roadmap.md` se reordonează: Faza 1 (produce + edit) și Faza 2 (instalarea `distribution/`) înainte de orice altceva. `engine/product-scout` și `engine/variations` rulează manual (Claude + Szasz) până în decembrie.
- **Cost/efort:** 0 $. Efort: o decizie.
- **Risc:** ratăm un produs bun din cele 5 lăsate deoparte. Îl reducem cu scout-ul care rulează în paralel.

### 2. Atribuire: cod de reducere + link UTM pe fiecare cont și unghi
- **Ce:** fiecare cont (și fiecare unghi) primește codul lui de reducere (ex. `COZY10`, `GIFT15`) și linkul lui din bio cu UTM. Shopify ne spune câte comenzi a adus fiecare cont și fiecare hook.
- **De ce:** codul promo e motivul nr. 1 de cumpărare de pe social (30%, [Sprout](https://sproutsocial.com/insights/holiday-shopping-trends/)). Tracker-ul nostru măsoară doar vizualizări, iar Esteban arată că 600k views pot aduce mai puțin decât 200k [declarat, B8]. Fără atribuire, optimizăm vizualizările, nu banii.
- **Cum în LIMITLESS:** `engine/store` creează codurile prin Shopify Admin API. `distribution/config/personas.json` primește câmpul `discount_code`. `social_tracker/` + `engine/report` adaugă **$ pe 1M de vizualizări pe fiecare cont și hook**, ca scor principal în `engine/hooks`, în locul vizualizărilor.
- **Cost/efort:** 0 $; ~1 zi de cod.
- **Risc:** codurile ajung pe site-uri de cupoane. Le facem cu durată limitată și le schimbăm.

### 3. Hook-uri pentru „trimiteri” (share în DM), cu unghiul de cadou
- **Ce:** fiecare video are un motiv clar ca privitorul să-l **trimită cuiva**. Exemple de text: „send this to the one who's always cold”, „he'd never buy this for himself”. Caption-ul cere „send”, nu „comment YES”.
- **De ce:** pe IG trimiterile raportate la vizualizări sunt semnalul cel mai legat de cei care nu te urmăresc ([dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers)). În Q4, 46% iau idei de cadouri de pe social ([Sprout](https://sproutsocial.com/insights/holiday-shopping-trends/)). Cererea de share către o persoană anume e mai blândă decât „tag 5 friends”, pe care Meta o retrogradează (vezi „Ce NU facem”). **[ipoteză]**: n-avem încă cifra noastră.
- **Cum în LIMITLESS:** `engine/hooks` primește câmpul `share_trigger` (pentru cine e trimis). `engine/edit` pune textul. `social_tracker/` măsoară share/save acolo unde API-ul le dă.
- **Cost/efort:** 0; o regulă în Cartea de stil.
- **Risc:** dacă formula se repetă în fiecare video, devine engagement bait. O rotim cu alte formule.

### 4. Câștigătorul trece în depozit SUA (stoc de 2–3 săptămâni)
- **Ce:** când un produs trece pragul (de ex. ≥ 50 de comenzi/zi, 3 zile la rând), comandăm stoc în vrac la un depozit din SUA (CJ US sau un 3PL). Pe site afișăm „Ships from USA, 3–5 days”. Păstrăm China doar ca rezervă.
- **De ce:** (a) ultima zi de vânzare de Crăciun se mută de la ~1–5 dec la ~**15 dec** (USPS 17 dec, [sursă](https://www.dakotanewsnow.com/2026/09/23/usps-announces-recommended-2026-holiday-mailing-shipping-deadlines/)), adică ~10 zile de vârf în plus; (b) livrarea lungă crește disputele ([Chargeflow](https://www.chargeflow.io/blog/best-shopify-payment-gateways)), iar disputele duc la bani blocați; (c) deschide TikTok Shop (expediere în 2 zile); (d) „livrare rapidă” crește conversia [nesigur, afirmație de vânzător: [dropified](https://www.dropified.com/blog/top-dropshipping-suppliers-usa-boost-your-online-business-today/)]. Furnizorii mari spun 2–7 zile din stoc SUA.
- **Cum în LIMITLESS:** un câmp nou în `products/<produs>.md`: `fulfillment: china | us_stock`. `engine/store` schimbă textul de livrare și data limită de Crăciun. `engine/report` dă alarma de stoc.
- **Cost/efort:** capital blocat în stoc (de ex. 2.000 de bucăți × 15 $ = 30.000 $ [calcul, exemplu]). Efort: 1–2 zile de negociere.
- **Risc:** rămâi cu stoc dacă trendul moare. Comandăm doar 2–3 săptămâni de vânzări, pe datele ultimelor 3 zile.

### 5. „Demonstrație”, nu „recenzie”: UGC refăcut legal
- **Ce:** păstrăm stilul UGC (telefon, cameră reală, reacție), dar personajul AI **nu spune** că l-a cumpărat, că îl folosește de 3 săptămâni sau că l-a vindecat. Formatul este **POV / demonstrație / reacție la produs**. Textul descrie produsul, nu experiența unui client care nu există. Pe site punem doar recenzii de la clienți reali.
- **De ce:** regula FTC interzice testimonialele de la persoane care nu există, inclusiv cele făcute cu AI; până la ~52.000 $ pe încălcare ([Hunton](https://hunton.com/hunton-retail-law-resource/ftc-issues-final-rule-targeting-fake-consumer-reviews-and-testimonials-including-those-generated-by-artificial-intelligence-ai-and-online-bots)). Un videoclip „recenzie” refăcut cu AI și postat pe 100 de conturi poate deveni 100 de încălcări [calcul].
- **Cum în LIMITLESS:** `engine/analyze` marchează în fișa viralului dacă e „testimonial” (persoană care vorbește despre experiența ei). `engine/hooks` și `engine/edit` rescriu replica în formă de demonstrație. `engine/qa` respinge textul la persoana I despre cumpărare sau rezultate. Regula intră în `docs/02-reguli.md`.
- **Cost/efort:** 0; o regulă și un filtru în QA.
- **Risc:** unele virale „recenzie” pierd puțin din forță. E mai bine decât amenzi și conturi închise.

### 6. Etichetarea AI corectă, nu ascunderea ei
- **Ce:** pe TikTok și YouTube bifăm eticheta „AI-generated” / „altered or synthetic” la fiecare video realist. Pe Meta lăsăm eticheta automată. **Nu ștergem metadatele** ca s-o evităm.
- **De ce:** pe TikTok, conținutul nedeclarat ajunge la etichetă forțată, apoi ștergere, apoi strike pe cont ([CineRads](https://www.cinerads.com/blog/tiktok-ai-content-policy)). Pe Meta, o sursă spune că eticheta nu scade reach-ul ([Coinis](https://coinis.com/blog/meta-ai-content-labeling-facebook-instagram-ads-2026)), dar conținutul înșelător e tăiat ([Primotech](https://primotech.com/meta-to-labe/)). Pe YouTube, AI-ul realist trebuie declarat ([TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)).
- **Cum în LIMITLESS:** `distribution/` adaugă bifa în lista de postare a fiecărui poster (platformă → etichetă). Câmpul `ai_label: true` în manifestul videoului. Testăm cu cifre: același tip de video, cu etichetă vs. eticheta automată.
- **Cost/efort:** 0.
- **Risc:** o posibilă scădere de reach **[nesigur]**. Riscul invers (conturi pierdute) e mai mare.

### 7. Originalitate peste refacere: „același concept, alt video”
- **Ce:** fiecare video refăcut primește cel puțin 2 elemente proprii: text de hook propriu (nu cel al competitorului), alt sunet sau voce, ordinea cadrelor, un cadru în plus (detaliu de produs, cadoul împachetat). Fără watermark de la altă platformă. Fiecare MP4 se exportă curat pentru platforma lui.
- **De ce:** Meta penalizează „editările minore” ale conținutului altora și taie distribuția pe **tot** contul ([Social Media Today](https://www.socialmediatoday.com/news/meta-adds-more-measures-to-ensure-original-creators-get-credit/814764/)). Mișcarea și sunetul identice cu viralul pot fi detectate ca reupload **[ipoteză]**. YouTube tratează șabloanele produse în masă ca neoriginale ([TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)).
- **Cum în LIMITLESS:** `engine/edit` aplică variațiile din `library/stil.json` (nu repetă combinația text + sunet + ordine pe două conturi). `engine/qa` are pasul „diferă de sursă în ≥ 2 elemente”.
- **Cost/efort:** mic (montaj).
- **Risc:** variația poate slăbi un hook dovedit. O testăm A/B pe Trial Reels (ideea 8).

### 8. Testarea hook-urilor cu Trial Reels în loc de conturi noi
- **Ce:** pe conturile IG cu ≥ 1.000 de urmăritori, variantele de hook (text, sunet, prima secundă) se postează întâi ca **Trial Reels**, care merg doar la necunoscuți. Câștigătoarea se postează normal.
- **De ce:** Trial Reels există exact pentru asta ([ucompares](https://ucompares.com/social-media/instagram/instagram-trial-reels/)). Testul nu „strică” contul principal cu postări slabe și scade nevoia de 10–30 de conturi pe produs, adică riscul de ban în lanț pe același IP [declarat, Esteban A11][B9].
- **Cum în LIMITLESS:** `distribution/config/schedule.json` primește tipul de postare `trial`. `engine/hooks` decide care variante merg la test. Tracker-ul compară la 24 h.
- **Cost/efort:** 0; regulă de programare.
- **Risc:** disponibilitatea și regulile Trial Reels sunt descrise doar de bloguri **[nesigur]**; le verificăm din aplicație.

### 9. Ofertă care ridică AOV-ul: pachet de cadou + upsell după plată
- **Ce:** pe fiecare produs: 1 bucată / **„2-pack: one for you, one to gift”** / pachet familie. Plus un bonus ieftin și real (ambalaj de cadou, felicitare) și un upsell cu un clic după plată. Ținta: AOV ≥ 70 $ în loc de 55 $.
- **De ce:** AOV-ul de 55 $ din plan e sub ce declară Esteban (halat ~150 $ → AOV ~180 $; huse auto 110–140 $) [declarat, A2][A3]. Fiecare 10 $ în plus la AOV scade numărul de vizualizări necesare cu ~15% [calcul]. Hormozi (stivuirea valorii) e deja în `playbooks/carti-marketing-psihologie.md` §4.
- **Cum în LIMITLESS:** `engine/store` generează variantele de pachet. `docs/10` primește regula „pachet de cadou obligatoriu în Q4”.
- **Cost/efort:** mic. Aplicațiile de upsell costă de obicei 10–50 $/lună **[nesigur]**.
- **Risc:** prea multe opțiuni scad conversia. Maxim 3.

### 10. Plăți: planul Shopify potrivit + doi procesatori + scut anti-dispute
- **Ce:** (a) un procesator principal și unul **de rezervă**, aprobat înainte de Black Friday; (b) planul Shopify ales după comisionul de 2% / 1% / 0,5%; (c) pagină de urmărire a coletului + email automat la fiecare pas de livrare; (d) alertă de dispute în raportul zilnic, cu pragul **0,5%** (procesatorii reacționează înainte de 1,5%-ul Visa); (e) descriere de facturare (billing descriptor) cu numele magazinului, ca oamenii să recunoască plata.
- **De ce:** banii blocați sunt cel mai mare risc declarat de Esteban (30k $ blocați, 20 de chargeback-uri) [declarat, A9][A10]. Rezervele apar repede la creșteri bruște ([Chargeflow](https://www.chargeflow.io/blog/best-shopify-payment-gateways)). Pragurile Visa ([Justt](https://justt.ai/blog/visa-vamp-threshold-changes-april-2026/)).
- **Cum în LIMITLESS:** `engine/store` + `engine/report`: modulul „bani” (încasat, ținut în rezervă, dispute, rambursări), cu o singură alarmă roșie.
- **Cost/efort:** 1–3 zile pentru aprobări. Comisionul diferă după procesator (2,9% vs. 4–7,5%).
- **Risc:** procesatorul de rezervă poate refuza dropshipping-ul. Aplicăm la 2–3 procesatori.

### 11. Captarea emailului și SMS-ului din prima zi
- **Ce:** pop-up pentru reducere (email/SMS), coș abandonat, „ultima zi pentru livrare de Crăciun”, „Cyber Monday”. Lista de vizitatori din octombrie devine bani în Cyber Week.
- **De ce:** traficul organic e gratuit, dar se pierde dacă nu-l păstrăm. Esteban folosește email/retargeting la scalare [declarat, A11][B6]. Octombrie e deja o lună de cumpărături timpurii (95,8 mld $, [CTC](https://commonthreadco.com/blogs/coachs-corner/adobes-275-billion-holiday-forecast-is-here-what-ecommerce-brands-must-do-before-black-friday)); 2 din 5 americani încep să caute înainte de Black Friday ([The Trade Desk](https://www.thetradedesk.com/insights/holiday-shopping-data-2026-success)).
- **Cum în LIMITLESS:** `engine/store` instalează fluxurile standard. Claude scrie emailurile în stilul produsului.
- **Cost/efort:** aplicație de email ~0–100 $/lună la început **[nesigur]**. 1 zi.
- **Risc:** emailurile pot ajunge în spam. Domeniu separat de trimitere, verificat.

### 12. Alegerea produselor: beauty/transformare + casă + cadou, cu preț ≥ 39 $ și taxă vamală calculată
- **Ce:** în cele 5 teste intră cel puțin 1 produs **beauty/îngrijire cu demonstrație vizibilă** (fără promisiuni medicale), 2 de **casă/cozy de iarnă** și 1 de **cadou** pentru bărbați sau părinți. Pe fiecare se calculează **taxa vamală pe codul HTS** înainte de preț.
- **De ce:** cosmeticele (+9,5%) și casa (+7,3%) cresc mai repede decât îmbrăcămintea (+4,7%) ([Adobe/ppc.land](https://ppc.land/adobe-puts-us-online-holiday-spend-at-275-1-billion-up-6-7/)). Beauty convertește mai bine pe Shopify ([growthsuite](https://www.growthsuite.net/resources/shopify-conversion-rate/complete-guide/benchmarks-by-industry)). Transformarea aduce 20k $+/1M [declarat, A11]. Tarifele de 21–37,5% pot topi marja la produsele sub 30 $ ([tariffstool](https://www.tariffstool.com/tariffs-from-china)).
- **Cum în LIMITLESS:** `docs/09` §1 primește regula 11: „marja după taxă vamală + livrare + 5% procesator + 5% rambursări ≥ 50%”. `engine/product-profile` calculează câmpul `landed_cost`.
- **Cost/efort:** 0. Codul HTS îl cere furnizorul.
- **Risc:** la beauty, riscul de afirmații de sănătate e mai mare. QA strict pe text.

### 13. Prelungim „iarna” până în februarie pentru produsele de frig
- **Ce:** produsele de căldură (nu cele doar de cadou) continuă în **ianuarie–februarie**, cu unghi „cold” în loc de „gift”.
- **De ce:** frigul real în SUA ține până în februarie [raționament]. După Crăciun dispare termenul de livrare, iar conturile câștigate în Q4 sunt deja „încălzite”. Calculul de 5 M$ pe 68 de zile ignoră lunile cele mai reci. **[nesigur]**: n-am găsit date de vânzări pe ianuarie pentru categoria asta.
- **Cum în LIMITLESS:** `docs/00` primește un al doilea orizont. `engine/hooks` comută automat unghiul după 20 dec.
- **Cost/efort:** 0.
- **Risc:** cererea scade după sărbători. Măsurăm $/1M pe săptămână și oprim când scade sub prag.

### 14. Cardul cadou „arrives after Christmas”, după data limită
- **Ce:** după ultima zi de livrare, oferta devine „Give it today”: clientul primește imediat un **card cadou printabil/digital**, iar produsul vine în ianuarie. Totul spus clar pe pagină.
- **De ce:** vânzările din 6–24 dec nu se pierd, iar data adevărată de livrare evită disputele [raționament]. Urgența rămâne reală, nu falsă (regula din `carti-marketing` §5).
- **Cum în LIMITLESS:** `engine/store`: șablon de card generat cu GPT Image 2.5. Textul de pe pagină se schimbă automat la data limită.
- **Cost/efort:** mic.
- **Risc:** clienți nemulțumiți dacă nu citesc. Termenul se scrie în checkout și pe card.

### 15. Rutarea modelelor și bugetul pe „$ încasat”, nu pe credite
- **Ce:** bugetul de producție pe produs = un procent din venitul lui din ultimele 3 zile (de ex. 5%), nu 2.000 de credite fixe pe zi. Opus planifică, modelele mai ieftine fac pașii mecanici.
- **De ce:** azi `config/budget.json` = 2.000 cr/zi ≈ 7–10 videouri pe zi, pentru tot. Ținta din plan cere ~100/zi. Producția costă ~100–250 $/zi la 10 videouri [calcul din `config/costs.json`: ~200–300 cr × 0,04–0,06 $], neglijabil față de 1.000 $/zi venit. Rutarea modelelor e în notițele de automatizări [B][D][H].
- **Cum în LIMITLESS:** `engine/budget` citește venitul din Shopify. Formula se aprobă de Szasz o singură dată.
- **Cost/efort:** 1 zi.
- **Risc:** cheltuială care fuge. Plafon zilnic absolut + oprire la eșecuri repetate.

---

## Riscuri mari și cum le reducem

| Risc | Cât de grav | Semnale | Cum îl reducem |
|---|---|---|---|
| **Bani blocați** (rezervă, payout înghețat, cont de plăți închis) | Foarte grav: poți avea vânzări fără bani în cont în ianuarie | rezervă anunțată, dispute > 0,5% | idei 4, 10; doi procesatori; livrare rapidă; răspuns la emailuri în < 24 h; nicio promisiune falsă; **planul de cash presupune că 20% din venit poate fi ținut 60–180 de zile** ([Tailoredpay](https://tailoredpay.com/blog/high-risk-merchant-account-shopify/)) |
| **Ban de conturi / shadowban în lanț** | Grav: un produs câștigător poate ajunge la 0 peste noapte [declarat, A2][B10] | scădere bruscă a reach-ului pe mai multe conturi deodată | max ~5 conturi pe telefon/IP [declarat]; niciun video identic pe două conturi; Trial Reels pentru teste; fără urmăritori cumpărați (interzis și de FTC); conturi de rezervă încălzite din timp |
| **Politici AI și originalitate** | Mediu–grav | etichete forțate, strike-uri, reach tăiat pe tot contul | idei 5, 6, 7; regula FTC; etichetare corectă; ≥ 2 elemente proprii pe video |
| **Engagement bait la „comment WORD”** | Mediu, mai ales pe **Facebook** | notificare „Engagement Baiting” | pe FB linkul în comentariul fixat sau în bio, fără „comment X”; pe IG un singur CTA la final, cu răspunsuri variate ([ManyChat community](https://community.manychat.com/general-q-a-43/facebook-comment-automation-engagement-baiting-3481), anecdotă) |
| **Livrare și tarife** | Grav în decembrie | colete blocate în vamă, termene depășite | DDP cerut explicit; taxa vamală calculată în preț; stoc SUA pentru câștigători; data de Crăciun afișată cinstit; card cadou după termen |
| **Sezon scurt** | Grav | primul viral vine după 2–4 săptămâni [declarat] | test acum (13 oct), nu după ce e gata platforma; câștigători până pe 1 nov; prelungire până în februarie pentru produsele de frig |
| **Volum de clienți** (la 1.000+ comenzi/zi: „unde e coletul?”) | Mediu–grav | emailuri fără răspuns → dispute | pagină de urmărire, emailuri automate de livrare, asistent AI pentru suport cu răspunsuri verificate, o persoană care verifică zilnic |
| **Publicul greșit** (India etc.) | Mediu | țări non-SUA > 30% în statistici | regula din `esteban.md` (avatar și context american, sunete din SUA) + alarmă în tracker |

---

## Calculul de 5 M$ revăzut

### Ce schimbăm față de `docs/00`
| Ipoteză | În plan | Revăzut | De ce |
|---|---|---|---|
| Fereastra | 68 de zile (15 oct – 22 dec) | **~45 de zile productive**: primele vânzări serioase ~25 oct–1 nov; China până la ~5 dec, SUA până la ~15 dec; plus 6–24 dec cu card cadou | ramp-up de 2–4 săptămâni [declarat], livrare, USPS |
| Bani la 1M vizualizări | implicit 5,5k $ (0,5% click × 2% conversie × 55 $) | **3k (prudent) / 5k (bază) / 8k (cu pachete + beauty)** | Esteban 3–6k obișnuit, 20k+ transformare [declarat] |
| AOV | 55 $ | **70 $** cu pachet de cadou | ideea 9 |
| Conversie | 2% | 1,4% mediană, 2–3% în Q4 cu ofertă bună | [popupsmart](https://popupsmart.com/blog/shopify-conversion-rate-statistics); Q4 ×2–3 [declarat, Matas] |
| Bani încasați în Q4 | 100% | **~80%** (restul în rezervă până în T1 2027) | rezerve tipice 20% / 60 de zile — surse de vânzători |
| Marjă netă | ~70% (Esteban organic) | **~35–50%** după produs, livrare, taxă vamală 20–37%, procesator 3–7%, Shopify 0,5–2%, rambursări ~5% | [calcul] din sursele de mai sus; **[nesigur]** pe fiecare produs |

### Vizualizări necesare pentru 5 M$ [calcul]
| $/1M vizualizări | Vizualizări totale | Pe zi (45 de zile) | Comenzi totale (AOV 70 $) | Comenzi/zi |
|---|---|---|---|---|
| 3.000 $ | 1,67 mld | **37 M/zi** | ~71.000 | ~1.590 |
| 5.000 $ | 1,00 mld | **22 M/zi** | ~71.000 | ~1.590 |
| 8.000 $ | 0,63 mld | **14 M/zi** | ~71.000 | ~1.590 |

### Câte videouri și conturi înseamnă asta [calcul, ipoteză de lucru]
- La 22 M/zi: cu 150 de videouri postate pe zi, fiecare trebuie să facă în medie ~**150.000** de vizualizări. Cu 300/zi, ~75.000. La conturi noi, media e mult sub asta. Câștigul vine din câteva virale de milioane **[nesigur]**: n-avem încă media noastră.
- Producție: 150 de videouri/zi × ~200 de credite ≈ 30.000 cr/zi ≈ **1.200–1.800 $/zi** [calcul din `config/costs.json`]. E ok la 100k $/zi venit, dar nu înainte de validare.

### Scenarii realiste pentru Q4 [calcul + raționament, nu promisiune]
| Scenariu | Ce trebuie să se întâmple | Venit Q4 (ordin de mărime) |
|---|---|---|
| **A — un câștigător** | 1 produs la ~5k $/1M, crescut la ~5–8 M vizualizări/zi din nov | ~0,5–1 M$ |
| **B — doi câștigători + stoc SUA** | 2 produse, unul beauty/transformare, Cyber Week puternic, livrare până la 15 dec | ~1,5–2,5 M$ |
| **C — ținta de 5 M$** | 3+ câștigători până la 1 nov, ~20 M vizualizări/zi susținut, plăți fără blocaj, stoc SUA, prelungire în ian–feb | 5 M$ (posibil doar cu ian–feb inclus) |

Ca reper: cea mai bună lună declarată de Esteban pe un produs e ~100k $ în 2 săptămâni, cu vârf de 15k $/zi [declarat]. Ținta cere ~110k $/zi în medie, timp de 45 de zile. **Concluzie:** ținta e foarte agresivă. Planul trebuie construit ca să maximizeze **B**, cu opțiunea de a ajunge la **C** dacă apar câștigătorii devreme. Asta înseamnă totul pe viteză în octombrie, stoc SUA în noiembrie și plăți sigure înainte de Black Friday.

---

## Întrebări pentru Szasz (max 7)

1. **Câte produse pornim pe 13 oct: 5 sau 10?** Recomandarea mea: 5, cu câștigătorii aleși pe 1 nov.
2. **Ce capital poți bloca în stoc SUA** pentru un câștigător (de ex. 20–50k $)? Și accepți ca 20% din încasări să poată sta 2–6 luni în rezervă la procesator?
3. **Ce procesator de plăți ai deja aprobat** (și unul de rezervă)? Și ce plan Shopify (2% / 1% / 0,5% comision extern)?
4. **Câți posteri și câte telefoane/IP-uri ai efectiv** pe 1 noiembrie? De aici iese câte conturi putem rula sigur.
5. **Accepți regula „demonstrație, nu recenzie”** (fără personaj AI care spune că a cumpărat) și etichetarea AI pe TikTok/YouTube?
6. **Ținta de 5 M$ e pe oct–dec strict, sau putem include ianuarie–februarie** pentru produsele de frig?
7. **Ce înseamnă „câștig” pentru tine: venit sau profit?** La marjă de 35–50%, 5 M$ venit ≈ 1,75–2,5 M$ profit înainte de taxe [calcul].
