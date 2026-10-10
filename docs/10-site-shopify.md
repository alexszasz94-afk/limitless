# Site-ul automat (Shopify) pentru fiecare produs

(10 oct 2026, Szasz) Pentru fiecare produs care trece regulile (`docs/09`), LIMITLESS face automat site-ul pe **Shopify**, pe baza întrebărilor pe care le dă Szasz. **Plățile: alt procesator, nu Shopify Payments** (se conectează la checkout-ul Shopify ca gateway extern).

## Ce face automat
1. **Întrebările lui Szasz** → răspunsurile (din fișa produsului + research + întrebări către el unde lipsește ceva) → `products/<produs>/site.json`.
2. **Magazinul** prin Shopify Admin API: produs, variante, prețuri, imagini (GPT Image 2.5, 4k, pe produsul real), descriere, FAQ, recenzii, politici (livrare, retur), domeniu.
3. **Pagina produsului** după reguli de conversie: explică în primele ecrane cum funcționează (ca în video), video demonstrativ sus, ofertă (bundle / cadou), urgență de sezon, garanție, livrare SUA.
4. **Pagini pe unghi**: când un unghi devine viral, primește landing page propriu (Esteban: doar după viral, nu înainte).
5. **Upsell / recurență**: produs complementar sau consumabil, email marketing de la prima zi.
6. **Legătura cu videourile**: link în bio + „comment WORD” (ManyChat) → link în DM.

## De la Szasz
- Lista lui de întrebări (le scrie el; fiecare devine un câmp în `site.json`).
- Contul Shopify + acces API (Admin API token, în variabilele mediului, niciodată în repo).
- Procesatorul de plăți ales.

## Regula din 10 oct: competitor + îmbunătățire
Pentru fiecare produs aprobat: (1) găsim 2–3 site-uri ale competitorilor care îl vând deja (din linkurile „Store” din Product finder); (2) notăm structura lor (ordinea secțiunilor, oferta, pachete, garanție, FAQ, prețuri); (3) construim pagina noastră pe aceeași structură, dar mai bună la fiecare punct — video UGC real sus, ofertă mai clară, demo, unghiul din „Why it sells · how to win”, mobil mai rapid; (4) textele, pozele și recenziile sunt ale noastre (fără copiere cuvânt cu cuvânt, fără recenzii false, fără prețuri „înainte” false).
