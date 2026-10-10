# Costuri LIMITLESS

Calculatorul: `python3 engine/costs.py <produse> <videouri/zi/produs> [rețetă]`, cu prețurile din `config/costs.json` (marcate „observat” din tranzacțiile reale sau „estimat”). Se actualizează din tranzacțiile Higgsfield și din QA (factorul de reîncercări).

Concluzia de pornire (10 oct 2026): **reutilizarea decide bugetul.** Cu B-roll făcut o dată pe produs și doar hook-ul nou per video, 10 produse × 5 videouri/zi costă de ~5 ori mai puțin decât rețeta standard și de ~10 ori mai puțin decât totul nou.

De măsurat înainte de scalare: prețul real al creditului pe planul „scale”, costul GPT Image 2.5 pe calitate/rezoluție, factorul real de reîncercări, Seedance 2.5 pe durată/rezoluție, draft 480p → 1080p.
