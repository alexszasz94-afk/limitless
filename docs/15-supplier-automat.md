# 15 — Supplier automat pentru fiecare produs aprobat

Regula (10 oct): la fiecare produs pe care Szasz îl aprobă pentru test, căutăm direct supplierul, înainte de orice video.

Pașii (agentul Supplier):
1. Caută produsul EXACT (aceeași variantă ca în viralele din categorie) pe AliExpress, Alibaba, agenți (CJ, Zendrop) și depozite US.
2. Pentru fiecare sursă: preț unitar, transport, taxă vamală US estimată, cost aterizat, timp de livrare, link.
3. Calculează marja la prețul propus (1 / 2 / 3 bucăți) după 3,5% comisioane și 5% retururi.
4. Riscuri: certificări (electrice, copii), IP, baterii, sezon.
5. Scrie rezultatul în `docs/supplier-<produs>.md` și în profilul produsului din platformă.

Exemplu complet: `docs/14-supplier-heated-poncho.md`.
Costurile vamale sunt estimări până la prima comandă reală.
