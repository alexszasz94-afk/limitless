# Scout de produse din Meta Ads (Facebook / Instagram)

(10 oct 2026, Szasz) Studiem reclamele plătite din Meta Ad Library ca să găsim produsele care **deja vând** cu bani, apoi le aducem în organic cu LIMITLESS.

## De ce merge
Un magazin nu ține o reclamă plătită pornită luni de zile dacă nu face profit. Ad Library e publică: arată fiecare reclamă activă, de când rulează, câte variante are, iar pentru UE și numărul de oameni atinși.

## Semnalele unui produs câștigător (se calculează automat)
| Semnal | De ce contează |
|---|---|
| Reclama rulează de ≥ 30 de zile | o plătesc de mult → e profitabilă |
| Multe variante active pentru același produs | scalează: testează și adaugă creative |
| Mai mulți advertiseri cu același produs | piața e dovedită, nu e noroc |
| Acoperire mare în UE (reach din Ad Library) | volum real de vânzări |
| Pornire recentă + multe variante | produs în creștere acum (trend) |
| Potrivire cu sezonul (iarnă, Black Friday, Crăciun) | intră în fereastra noastră de 5 M$ |

Pragurile exacte se fixează după primul research și se ajustează din cifrele noastre (care produse luate de aici au mers și în organic).

## Fluxul
1. **Căutare:** cuvinte cheie pe nișe + pagini de magazine cunoscute, SUA + UE (Apify, scraper Ad Library).
2. **Grupare:** reclamele se grupează pe produs (aceeași imagine / același titlu / același link de magazin).
3. **Scor:** semnalele de mai sus → listă ordonată de produse.
4. **Fișa:** produsele de top primesc automat fișa din `docs/04-produs-universal.md` (categorie, wow, demonstrație, public, sezon).
5. **Creativele:** videourile reclamelor câștigătoare intră în coada Vânătorului: hook-urile și unghiurile care vând, refăcute organic cu personajele și camerele noastre.
6. **Decizia:** Szasz primește top 10 cu motivul și zice da / nu (mai târziu, automat după cifre).

## Ce studiem în plus
- cum își scriu reclamele câștigătoare primele 3 secunde, oferta, textul;
- ce tip de video folosesc (UGC, demonstrație, înainte / după) per categorie → intră în Cartea de stil, per categorie.
