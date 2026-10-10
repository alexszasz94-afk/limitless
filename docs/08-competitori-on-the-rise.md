# Competitori „on the rise” și variații de produs

## 1. Pe cine urmărim (Szasz, 10 oct 2026)
Pe nișă, cel mai important sunt conturile organice **în creștere acum**, nu cele mari și vechi.

**Semnalul de bază: un video cu ≥ 100.000 de vizualizări în prima zi = DOVEDIT.** La viteza asta, videoul vinde. Se ia imediat în coada Vânătorului.

| Semnal | Prag de pornire (se ajustează din cifre) |
|---|---|
| Viteza videoului | ≥ 100k vizualizări în ~24 h de la postare |
| Contul e în creștere | mai multe videouri peste media lui în ultimele 7–14 zile; cont tânăr cu vizualizări mari |
| Repetabilitate | același produs / același tip de hook a mers de ≥ 2 ori la el |
| Ce vinde | link în bio / magazin / TikTok Shop vizibil → produsul intră și în scout (`docs/07`) |

Cum se măsoară viteza: Vânătorul trece pe la conturile urmărite de 2 ori pe zi și compară vizualizările între treceri (vizualizări / ore de la postare). Un video care trece pragul declanșează: analiză → plan → producție, cu prioritate maximă.

Lista de conturi „on the rise” per nișă: `library/competitori/<nisa>.json` (cont, platformă, de când îl urmărim, cel mai bun video, viteza maximă, produse văzute).

## 2. Idei de variații custom ale produsului (mereu, în aplicație)
Pentru fiecare produs activ, aplicația propune continuu **variații care se pot realiza** și care pot deveni produse sau unghiuri noi.

| Tip de variație | Exemple |
|---|---|
| Personaj / temă | alt personaj sau stil (sărbători, sezon, nișă de fani — fără IP protejat fără licență) |
| Culoare / material | alte culori, alt pluș, ediție premium |
| Public | copii, cupluri, animale, mărimi mari, „pentru el / pentru ea” |
| Personalizare | nume brodat, inițiale, poză, mesaj de cadou |
| Pachet | set cuplu / familie, bundle cu accesoriu, ambalaj de cadou |
| Funcție | o funcție în plus (încălzire, buzunar, glugă, LED, etc. după categorie) |

Fiecare idee vine cu:
- **de ce**: din ce semnal (comentarii „vreau în altă culoare”, competitor, trend, căutări);
- **fezabilitate**: se poate face la furnizor / print-on-demand / broderie? cost estimat și timp;
- **mockup**: o imagine GPT Image 2.5 cu varianta (pentru test de reacție înainte de comandă);
- **test**: 1–3 videouri cu mockup-ul → dacă trece pragul de cifre, se comandă mostra.

Ideile apar în raportul zilnic, ordonate după potențial; Szasz zice da / nu.
