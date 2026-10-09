# Sistem universal: produsul decide strategia

(9 oct 2026, Szasz) LIMITLESS funcționează pe **orice produs**. Primește produsul și detectează singur **ce** videouri să facă și **cum**.

## 1. Intrarea
Szasz dă doar una dintre ele:
- linkul produsului (magazin, AliExpress, Amazon, TikTok Shop), sau
- poze / un clip cu produsul.

## 2. Profilul produsului (generat automat → `products/<produs>.md`)
Claude analizează produsul (poze, descriere, recenzii, videouri virale existente) și completează:

| Câmp | Exemple |
|---|---|
| Categorie | îmbrăcăminte cozy, gadget de bucătărie, beauty, animale, casă, auto, fitness, copii |
| Problema rezolvată | „mi-e frig”, „durează prea mult”, „e murdar”, „mă doare” |
| Efectul „wow” | ce se vede în 1 secundă și nu se poate ignora |
| Tipul de demonstrație | se poartă / se folosește cu mâna / înainte-după / transformare / satisfying |
| Publicul | gen, vârstă, cine cumpără vs. cine folosește (cadou?) |
| Sezon și momente | iarnă, Black Friday, Crăciun, Ziua Mamei, back to school |
| Preț și ofertă | preț de vânzare, marjă, bundle |
| Riscuri la generare | branduri / IP asemănătoare, detalii fine care „driftează”, filtre |
| Referințe vizuale | ID-urile pozelor exacte ale produsului (produsul nu se schimbă niciodată) |

## 3. Strategia aleasă automat din profil
| Dacă produsul e… | Structura video | Hook-uri căutate | B-roll |
|---|---|---|---|
| **se poartă** | hook → îl pune → îl arată întreg → detaliu → momentul cozy / folosire | reacție, cadou, „POV”, magazin | personaj + cameră, motion control |
| **se folosește cu mâna** | hook → problema → produsul o rezolvă → close-up detaliu | „nu știam că am nevoie”, frustrare → soluție | mâini, macro, cadre fixe |
| **înainte / după** | hook → înainte → aplicare → după | rezultat șocant în prima secundă | split, același cadru înainte / după |
| **satisfying** | direct acțiunea, buclă | ASMR, sunet, mișcare | macro, sunet diegetic |
| **cadou** | reacția celui care îl primește | despachetare, surpriză | unboxing, reacție |

Tabelul e punctul de plecare. Se rafinează din:
- **research** (viralele outlier din categoria produsului);
- **playbook-uri** (ce fac cei mai buni pe produse similare);
- **cifrele reale** (ce structură a câștigat la produsele anterioare din aceeași categorie).

## 4. Ce rămâne la fel pentru orice produs
Research de virale, scor pe cifre, rotația hook-urilor, calitatea ultra-realistă, QA vizual, montaj gata de postat, feedback zilnic.

## 5. Memoria pe categorii
Fiecare produs lansat lasă în urmă reguli pe categoria lui (`library/categorii/<categorie>.md`). Al doilea produs dintr-o categorie pornește deja cu tot ce a învățat primul.
