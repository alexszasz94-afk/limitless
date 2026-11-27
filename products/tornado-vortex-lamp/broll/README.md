# B-roll VortiGlow — variante Seedance (27 nov 2026)

Szasz: „ia ăla ca B-roll de după hook și refă-l cu Seedance să fie la fel, doar că cu alte camere, alți copii, să am 5 B-rolluri gata… fă-mi schița la B-rolluri și le dăm upscale abia la montaj”. Excepție cerută de el de la regula „doar Kling” — doar pentru B-roll-urile astea.

- Referință video: `broll-master-v1.mp4` (11,2 s) → media Higgsfield 114babe1-80d9-4c8f-8b5f-6a8f9b4b3458.
- Referințe imagine: 1 = lampa oprită (media eae2cd9a…), 2 = lampa aprinsă (media 33e071bd…), 3 = logo-3 (job 5677ac1f…), 4 = cutia deschisă de sus (job 4afe5bc4…), 5 = close-up lampă (job 74392c68…).
- Setări: `seedance_2_5`, `omni_reference`, 11 s, 9:16, `draft: true` (480p, 33 credite), `generate_audio: false`. Final 1080p = 176 credite/buc, doar la montaj, pe ciornele alese.
- Promptul: identic la toate, se schimbă doar blocul „NEW PEOPLE AND PLACES” (vezi jobul primei ciorne).

| Set | Copil / cameră / masă / mâneci | Job ciornă | Stare |
|---|---|---|---|
| 1 | fetiță 4 ani, bucle blonde, pijama lavandă cu stele, miel de pluș · cameră crem, pat alb · blat de marmură albă · mâneci gri | a24d9bd5-951c-4ab0-a7d1-530c4b035efe | GATA: `draft-1.mp4` — cele 4 planuri la aceiași timpi, lampa/cutia/logoul ca în referințe; unboxing-ul ține ~0,3 s mai mult |
| 2 | băiat 7 ani, păr castaniu, pijama bleumarin cu rachete, dinozaur de pluș · pereți albastru deschis, pat supraetajat · masă de stejar deschis · mâneci verde închis | a5c13f7a-4fe6-4f5f-beef-37d77b7c7458 | GATA: `draft-2.mp4` |
| 3 | fetiță 6 ani, codițe șaten, pijama galben pal, vulpe de pluș · mansardă cu tavan înclinat alb · blat de piatră gri · mâneci albe | 3eb13f79-e153-4fb2-ad70-a0689fa825cc | GATA: `draft-3.mp4` |
| 4 | băiat 3 ani, blond, pijama crem cu ursuleți, elefant de pluș · pereți gri deschis, pat mic alb · masă albă rotundă · mâneci roz pudră | 9b5791e9-468a-4f65-a601-3405227b33ca | GATA: `draft-4.mp4` |
| 5 | băiat 9 ani, păr negru scurt, pijama gri, cățel de pluș · perete de cărămidă albă, pat de lemn închis · masă de nuc · mâneci negre | af619a0b-f98e-4df1-b3e7-8422fb8de989 | GATA: `draft-5.mp4` |

De la setul 2 încolo, în TIMELINE scrie „the child” în loc de „the girl”, ca promptul să rămână fix; se schimbă doar blocul NEW PEOPLE AND PLACES.

## Verificare ciorne 2–5 (27 nov, foaie de cadre lângă master)
Toate: cele 4 planuri în aceeași ordine, lampa (cilindru, capac metalic, bază neagră, inel cyan, pâlnie în tub), cutia neagră și logoul VortiGlow păstrate; 11,0 s. Abateri comune: unboxing-ul ține până la ~2,6 s (în master 2,3) și planul cu priza e mai scurt (~1,3 s). Set 2: camera e luminată ca ziua în planul în care pornește lampa (nu noapte). Set 3: mansarda ia mult albastru de la lampă. La 480p detaliile fine (mărgele, litere mici) nu se pot judeca — se verifică din nou la 1080p.
Cost: 5 × 33 = 165 credite. Finalul 1080p (176 credite/buc) doar la montaj, pe cele alese de Szasz.

## B-roll-urile la 1080p (27 nov, noaptea)
`broll-1-1080p.mp4` … `broll-5-1080p.mp4` — finalizări Seedance ale ciornelor (joburi af752c58, c5e81e81, 5ce13e58, fa8df252, fe8b94de), 1080x1920, 11,0 s. Finalizarea cere același apel ca la ciornă (prompt complet + cele 6 medias) + `draft_job_id` + `resolution: 1080p`.
Verificat lângă ciorne: aceeași filmare cadru cu cadru, doar clară. La 1080p: literele „VortiGlow” curate, lampa = referința (cilindru, capac metalic, bază neagră, mărgele colorate, pâlnie în tub), mâini corecte.
Cost: 5 × 176 = 880 credite. GREȘEALĂ de proces: Szasz voia upscale Topaz, nu finalizare Seedance → regula 27 nov din `docs/02-reguli.md` (niciun credit fără „da” explicit; „upscale” = Topaz).
