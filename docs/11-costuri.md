# Costuri LIMITLESS

Calculatorul: `python3 engine/costs.py <produse> <videouri/zi/produs> [rețetă]`, cu prețurile din `config/costs.json` (marcate „observat” din tranzacțiile reale sau „estimat”). Se actualizează din tranzacțiile Higgsfield și din QA (factorul de reîncercări).

Concluzia de pornire (10 oct 2026): **reutilizarea decide bugetul.** Cu B-roll făcut o dată pe produs și doar hook-ul nou per video, 10 produse × 5 videouri/zi costă de ~5 ori mai puțin decât rețeta standard și de ~10 ori mai puțin decât totul nou.

De măsurat înainte de scalare: prețul real al creditului pe planul „scale”, costul GPT Image 2.5 pe calitate/rezoluție, factorul real de reîncercări, Seedance 2.5 pe durată/rezoluție, draft 480p → 1080p.

## Prețuri exacte Higgsfield (get_cost, 10 oct 2026, fără a genera)
| Unealtă | Setare | Credite |
|---|---|---|
| Genjutsu | 1080p, referință ≤ ~4 s | **44** (minimul — orice clip mai scurt plătește tot 44) |
| Genjutsu | 1080p, ~5 s | 55 (~11 credite/s) |
| Genjutsu | 720p, ~5 s | 35 |
| Genjutsu | 480p, ~5 s | 15 (bun pentru teste de mișcare) |
| Seedance 2.5 | 5 s, 1080p, 9:16 | 60 (12 credite/s; 15 s = 180) |
| Seedance 2.5 | omni_reference, 4 s, 720p | 28 |
| Seedance 2.5 | draft 480p, 5 s (finalizabil la 1080p) | 15 |
| Seedance 2.5 | video_edit pe un clip de ~5 s, 1080p | 57 |
| Genjutsu replace_object | 1080p, ~5 s | 55 |
| GPT Image 2.5 | 1k low / 2k medium / 4k high / 4k max | 0,25 / 1 / 4,25 / 15 |
Consecințe: bucățile Genjutsu se fac de ~4 s (sub 4 s se plătește oricum minimul); testele de mișcare la 480p (15 cr), finalul la 1080p.

## Apify: scanare zilnică (estimare 10 oct 2026)
Prețuri pe rezultat: IG 0,0027 $, TikTok 0,0037 $, FB 0,005 $, Ad Library 0,00075 $, descărcare video 0,02 $.

| Scenariu | Ce scanează | ~$/zi | ~$/lună |
|---|---|---|---|
| **Start** (1–2 produse) | 30 competitori × 5 postări noi × 2/zi; 100 rezultate descoperire/zi; Ad Library săptămânal; 20 conturi proprii × 2/zi; ~10 descărcări video/zi | ~3 | **~80–100** |
| **Plin** (10 produse) | 300 competitori × 5 × 2/zi; 1.000 descoperire/zi; Ad Library săptămânal; 200 conturi proprii × 2/zi; ~30 descărcări/zi | ~26 | **~750–800** |
| **Plin, optimizat** | ca mai sus, dar conturile proprii prin Meta Graph API (gratuit pentru conturi business) și doar postările noi | ~12 | **~350–400** |

Economii: se cer doar postările noi (nu tot profilul), viteza se calculează din 2 treceri pe zi, se descarcă video doar pentru cele care trec pragul de 100k/24 h.
