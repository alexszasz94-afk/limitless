# Rețetă — căști Grinch, hook „3, 2, 1” NOU (nu copiat) + B-roll (19 nov 2026, v1, NEAPROBAT încă de Szasz)

Ideea lui Szasz: fata, în camera de Crăciun, ține o „mantie” mică peste cutiuță, zice „3, 2, 1, let's see how it comes out”, trage mantia jos, se vede cutia; apoi B-roll (deschide, scoate, poartă); apoi cele două profiluri.

## Pași (toți au mers din prima, în afară de unde scrie)
1. START FRAME — `nano_banana_pro` 9:16 4K, ref: fata + camera. Job `6f0e8554-a38d-40e4-9125-4b85e4795c52`. ATENȚIE: prima variantă cu „Grinch-style cape” a fost blocată (nsfw) → NU scrie „Grinch” lângă acoperământ; descrie-l: „fluffy lime-green fur with a red velvet lining and a white fluffy trim, like a miniature Christmas cape”. A ieșit ca o căciuliță verde cu roșu și alb.
2. END FRAME — `nano_banana_pro`, ref: start frame + carcasa închisă `e944d603`. „The same video two seconds later… cape pulled off, held down in her right hand; closed case on her left palm.” Job `3b1452b0-0b65-48c5-8123-e1c63acb52a4`.
3. HOOK — `kling4_0` image-to-video, 1080p, 9:16, 5 s, `start_image` + `end_image`, vocea făcută de Kling. Job `cc11a8c1-5352-4ee5-953a-d44a9f039a9f`. Cuvinte cerute și CONFIRMATE cu transcriere locală: „3, 2, 1, let's see how it comes out!” (0.0–0.7 / 1.0–1.6 / 2.0–2.5 / 2.7–3.9 s). Dezvelirea a venit la ~3.0–3.2 s (cerusem 3.9) — în timpul replicii; merge, dar la următoarea cere replica mai devreme sau durată 6 s.
4. B-ROLL — `kling4_0` video-edit pe inputul A (reel Hello Kitty fără sunet, 12 s, media `252cc0d1`), cu referințele din fișă (cap în ureche, fund în ureche, pereche din spate, carcasă oglindită, cap ținut cu o mână) + aceeași fată + aceeași cameră. Job `3686799d-6a40-49d7-94ab-3c17722bdb0b`. Începe cu carcasa închisă în mână → se leagă de hook.
5. PROFILURI — still-uri `1260f597` (dreapta, cap) și `7cf9858b` (stânga, fund; prima încercare `9816c523` a picat) → Kling i2v 3 s: `459d3636`, `fcb7116e`.
6. MONTAJ — `products/grinch-earbuds/final/edit-321.json`: hook 0–5 → B-roll 0–11.28 → dreapta 2.5 → stânga 2.5; text sus tot videoul; CTA pe profiluri; muzică încet sub hook (0.2), mai tare de la tăietură (0.6).

Fata: character-21 (media `cf66731c-f970-443b-8059-6cba4911012a`). Camera: `creator-kit/library/rooms/room-4k-14.jpg` (media `8912ad53-3e76-4359-bd1f-6b583bc0ab5d`).

## De îmbunătățit
- Fata din hook (păr prins la spate) și cea din B-roll (păr lăsat) nu arată identic → cere aceeași coafură în ambele.
- B-roll 4.7–7.8 s: fundalul e mai deschis decât sufrageria.
- Carcasa din hook e puțin prea mare pe palmă.
- Acoperământul nu are nimic recognoscibil de Grinch (filtrul blochează).
Prompturile exacte stau în joburile de mai sus; se copiază aici cuvânt cu cuvânt când Szasz aprobă.

## Corectură 19 nov (Szasz: „când l-a arătat în mână a greșit cum arată produsul”)
În B-roll-ul Kling cadrul cu capul pe deget (3,46–4,79 s) avea două vârfuri albe. Înlocuit cu clip separat: start frame `hook321/finger-A_1e913e3d.png` (job `1e913e3d-ac1d-4550-8d61-0447bd3f9a66`, Nano Banana Pro din fișă) → Kling image-to-video 3 s job `2421e0aa-22db-4d7a-9d23-5985cfacf941` → `hook321/finger.mp4` 0,3–1,7 s. Montaj v3: `final/edit-321.json`. De acum prim-planul în mână se face MEREU separat.
