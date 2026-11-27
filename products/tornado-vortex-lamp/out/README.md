# VortiGlow (Tornado Vortex Lamp) — pilot v1 (27 nov 2026)

`vortiglow-pilot-v1-silent.mp4` — 19,3 s, 1080x1920, 30 fps, FĂRĂ sunet (muzica se pune la postare).

| Secunde | Sursa | Text pe ecran |
|---|---|---|
| 0–4,8 | `clips/problem-v1-cut.mp4` (cameră de supraveghere, alb-negru) + ștampilă „CAM 02 11-27 02:47:13 AM” | 2:47 AM. / Every. Single. Night. |
| 4,8–8,1 | `clips/unboxing-v1-cut.mp4` (de sus) | So I tried this... |
| 8,1–9,6 | `frames/usb-plug-v1.png` (poză cu zoom lent, neanimată) | So I tried this... |
| 9,6–17,4 | `clips/solution-closeup-v1-realtime.mp4` 0,4–8,2 (formarea tornadei ~5,7 s) | He couldn't stop / watching it |
| 17,4–19,3 | `frames/solution-v1.png` (poză cu zoom lent) | Comment "TORNADO" / for the link |

Caption propus: He would not stay in bed. Now he just lies there watching it. Comment "TORNADO" and I'll send you the link.

Textul descrie reacția copilului, nu promite că lampa adoarme copiii. Text: `montage-text.py` (font TikTokSans din creator-kit); asamblare cu ffmpeg (scale/crop 1080x1920, concat).
Cost total sesiune: 112,5 credite Higgsfield. Totul e ipoteză până la cifre.

## Pilot v2 (27 nov, după corecturile lui Szasz)
`vortiglow-pilot-v2-silent.mp4` — 20,2 s, fără sunet. Schimbări față de v1: (1) clipul cu lampa = ORIGINALUL `clips/solution-closeup-v1.mp4` 0,3–10,0 (Szasz îl preferă celui încetinit; în el tornada se formează în ~2,5 s, la lampa reală ~6 s); (2) fără cadrul final cu camera de sus color; CTA „Comment "TORNADO" for the link” sus, peste ultimele 2,5 s; (3) priza cu USB e animată: `clips/usb-plug-v1.mp4` (Kling 4.0, 3 s, job 03b15484-8908-44e9-8bb9-549e109b3e67, start = usb-plug-v1.png), folosit 0–2,3 s.
Ordine: problemă 0–4,8 · unboxing 4,8–8,1 · USB 8,1–10,4 · lampa 10,4–20,2.

## Pilot v3 (27 nov) — scurtat la 17,3 s
`vortiglow-pilot-v3-silent.mp4`. Szasz: „mai scurtează spațiile moarte, vreo 17–18 secunde”. Tăieturi: problemă 0–4,3 (fără ultima jumătate de secundă neclară) · unboxing 0,3–1,2 + 1,9–3,3 din original (fără cutia nemișcată) = 2,3 s · USB 0,2–1,8 = 1,6 s · lampa 0,4–9,4 = 9,0 s, CTA de la 6,8 s.

## Pilot v4 (27 nov) — 15,3 s
`vortiglow-pilot-v4-silent.mp4`. Szasz: „taie ultimele 2 secunde”. Lampa 0,4–7,4 (7,0 s), CTA de la 4,8 s; restul ca în v3.

## Pilot v4 la 4K (27 nov)
`vortiglow-pilot-v4-4k.mp4` — 2160x3840, 15,3 s, fără sunet. Upscale Topaz 2160p în Higgsfield pe `vortiglow-pilot-v4-notext.mp4` (job 68b738c3-fd5a-41f5-a371-9ad237623c4b, ~240 credite după sold — unealta nu are estimare de cost înainte), apoi textul pus local la 4K. Verificat lângă 1080p: partea alb-negru arată tot a cameră de supraveghere, lampa și fețele neschimbate, doar mai clare. Fișierul 4K fără text (68 MB) nu e în git.
Muzică (propuneri, ipoteză): „Gonna Make You Sweat (Everybody Dance Now)” pe hook, tăiată la 4,3 s; se pune din aplicație la postare.

## Pilot v5 (27 nov) — cu close-up în mișcare, 15,9 s
`vortiglow-pilot-v5-silent.mp4` (1080p, fără sunet). Szasz: „mai trebuie un cadru close-up în timp ce merge, cum se mișcă pe lângă el camera… și dă-mi montajul”.
Ordine: problemă 0–4,33 · unboxing 4,33–6,63 · USB 6,63–8,27 · lampa pornește (`solution-closeup-v1.mp4` 0,4–4,8) 8,27–12,67 · close-up în arc (`clips/lamp-macro-v1.mp4` 0,6–3,8, Kling job 480a0298, 5 s, ~19 credite) 12,67–15,9, cu CTA jos, pe baza lămpii, în ultimele 2,2 s.
Verificare lamp-macro-v1: lampa neschimbată, camera alunecă lin ~40°, fundalul se mișcă; pâlnia se îngroașă puțin față de cadrul de start, rămâne în tub. 4K-ul existent (v4) NU conține cadrul ăsta.

## Pilot v5 cu muzică (27 nov)
`vortiglow-pilot-v5-music.mp4` — același montaj v5 + piesa aleasă de Szasz: Sean Paul feat. Keyshia Cole – „Give It Up To Me” (mp3 urcat de el; nu e în git). Piesa de la 5,62 s: sub hook (0–4,3 s) intro-ul la volum 0,45, pauza scurtă a piesei cade chiar înainte de tăietură, beat-ul intră la 4,33 s (tăietura problemă → unboxing), volum 1,0; fade-out în ultima jumătate de secundă. Piesă cu drepturi: pusă în fișier poate fi scoasă/limitată de platformă.
