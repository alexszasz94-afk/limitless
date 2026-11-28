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

## Pilot v6 (27 nov) — pornirea lămpii la 1,1x
`vortiglow-pilot-v6-music.mp4` / `-silent.mp4`, 15,5 s. Szasz: „pune 1.1x acolo când aprinde produsul”. Bucata `solution-closeup-v1.mp4` 0,4–4,8 redată la 1,1x (4,0 s în loc de 4,4); restul ca în v5, aceeași piesă, beat la 4,33 s.

## Pilot v6 — piesa schimbată (27 nov)
Szasz: „piesa asta de fapt” → Lady Gaga & Bruno Mars – „Die With A Smile” (mp3 urcat de el; nu e în git) în `vortiglow-pilot-v6-music.mp4` (înlocuiește Sean Paul). Piesa de la 36,32 s: sub hook finalul strofei + „If the world was ending” la volum 0,5; intrarea plină a refrenului (40,65 s în piesă) cade pe tăietura de la 4,33 s; fade-out 0,5 s la final. Potrivirea e făcută după nivelul sunetului, neascultată.

## Muzica la volum constant + B-roll master (27 nov)
- `vortiglow-pilot-v6-music.mp4` refăcut: „Die With A Smile” la același volum tot videoul (Szasz: „lasă piesa același volum tot videoul”).
- `broll/broll-master-v1.mp4` — 11,2 s, fără text și fără sunet: tot ce vine după hook (unboxing 2,3 s · USB 1,6 s · lampa pornește la 1,1x 4,0 s · close-up în arc 3,2 s). E referința video pentru variantele Seedance cerute de Szasz (5 B-roll-uri cu alte camere / alți copii). Estimări Seedance 2.5 omni_reference, 11 s, 9:16, fără audio: draft 480p = 33 credite; final 1080p = 176 credite.

## Montaje cu hook-urile noi + B-roll 1080p (27 nov, noaptea)
- `vortiglow-store-v1.mp4` (16,8 s) = `hooks/store-v1` + `broll/broll-2-1080p`; text hook „The only thing that stopped the tantrum”; vocea din hook păstrată.
- `vortiglow-cctv2-v1.mp4` (16,0 s) = `hooks/cctv2-v1` + `broll/broll-1-1080p`; „2:47 AM. Every. Single. Night.” + „She couldn't stop watching it”.
- `vortiglow-reveal321-v1.mp4` (15,9 s) = `hooks/reveal321-v1` + `broll/broll-master-v1`; text hook jos („3... 2... 1... his reaction”), vocea păstrată.
Toate: „Die With A Smile” la volum constant, refrenul pe tăietura hook → B-roll; B-roll: „So I tried this...” 0–3,9 · „He/She couldn't stop watching it” 3,9–8,8 · CTA „Comment "TORNADO" for the link” 8,8–11. Montajele de probă cu ciorne (`*-preview.mp4`) au fost șterse. B-roll-urile 3, 4, 5 sunt gata și nefolosite încă.

## Text nou la hook-urile care nu sunt problemă → soluție (27 nov, noaptea)
Szasz: „textul să fie la hook în aceeași poziție sus: DON'T SHOW THIS TO YOUR CHILDREN, cu emojiuri; dacă nu e problemă–soluție nu băga aia cu «I tried this»”.
- `vortiglow-store-v2.mp4`, `vortiglow-reveal321-v2.mp4` (înlocuiesc v1): sus, tot videoul până la CTA: „DON'T SHOW THIS / TO YOUR CHILDREN 😳🌪” (2 emoji, regula 7 nov); fără „So I tried this...” și fără „He couldn't stop watching it”; CTA jos în ultimele 3,1 s. Text: `montage-text-emoji.py` (font emoji: fonts-noto-color-emoji, instalat cu apt).
- Hook-urile problemă → soluție (camerele de supraveghere: `vortiglow-pilot-v6-music.mp4`, `vortiglow-cctv2-v1.mp4`) rămân cu „2:47 AM. Every. Single. Night.” + „So I tried this...”.
- 27 nov, corectură Szasz („textul îi acoperă ochiul”): la `vortiglow-reveal321-v2.mp4` textul de sus e urcat la y=90 (font 60), deasupra capului mamei, tot videoul. Verificat pe 4 cadre din hook: ochii și fața sunt libere. De reținut: la hook-uri cu fața mare în cadru, textul de sus se pune deasupra capului, nu la y=250.

## cctv2 la 4K (28 nov)
`vortiglow-cctv2-v1-4k.mp4` — 2160x3840, 16,0 s, cu piesa. Upscale Topaz 2160p (job c66192c0-b4d0-4e38-a311-b1749bde18a3) pe varianta fără text, textul și muzica puse local la 4K. Verificat lângă 1080p: hook-ul arată tot a cameră de supraveghere, fața fetiței și lampa neschimbate; câștigul de detaliu e mic.
COST REAL, din sold: 6381,84 înainte → 6341,58 imediat după pornire → 5877,58 la final = 504 credite (~31,5 credite/secundă). Topaz taxează puțin la pornire și restul la final. Estimarea dată lui Szasz (≈250) a fost greșită. Refăcut calculul și pentru upscale-ul din 27 nov (15,3 s): cel mai probabil ~470 credite, nu 240.
REGULĂ DE PREȚ: Topaz 4K ≈ 31 credite/s (un video de 16 s ≈ 500 credite). Finalizarea Seedance la 1080p = 16 credite/s.
