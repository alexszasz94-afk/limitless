---
name: log-lesson
description: Scrie o greșeală în Mistakes log (colecția `lessons` din platformă). Folosește de fiecare dată când ceva pică, costă degeaba sau Szasz corectează ceva.
---
# Jurnal de greșeli

- Înainte de producție: citește colecția `lessons` (ArtifactData list) și respectă fiecare `rule`.
- Când ceva pică: scrie un document nou `lessons/lNN` (următorul număr liber) cu câmpurile: `date` (AAAA-LL-ZZ), `area` (video / hooks / app / research / process / store), `product` (opțional), `what` (ce s-a întâmplat, EN), `cause` (de ce, EN), `rule` (regula de acum încolo, EN), `cost` (opțional), `by: "Claude"`.
- Dacă regula e de producție, adaug-o datată și în `docs/02-reguli.md` și în `config/main.rules_en`.
- O greșeală se scrie o singură dată; dacă se repetă, actualizează documentul existent.
