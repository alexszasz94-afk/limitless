# Hook-uri noi VortiGlow (27 nov 2026, seara)

Szasz a cerut 4 hook-uri: (1) store hook cu mama și copilul agitat în Walmart, (2) încă unul ca cel cu camera de supraveghere, (3) „problem” cu copilul care fuge și cade pe scări, (4) reveal 3-2-1 „let's see what comes out” cu lampa acoperită de o mantie.

Decizii Claude, spuse lui Szasz: (1) magazin mare FĂRĂ nume/logo (nu Walmart: lampa nu se vinde acolo, branduri reale nu se preiau); (3) NEPORNIT — copil care cade pe scări = accident cu copil (playbook: fără accidente reale) și ar sugera că lampa previne așa ceva; propus: copilul coboară scările pe fund, fără căzătură — aștept răspuns.

Cadre: gpt_image_2_6, 2k, 9:16, high, 2 credite/buc. Video: Kling 4.0 image-to-video 1080p.

| Hook | Cadru start (job) | Clip Kling (job) | Durată / cost |
|---|---|---|---|
| Store | `store-frame-v1.png` (32b1adff-62c8-4bce-bfb7-87e4df753787; ref lampă 33e071bd + cutie fdf9d5a0) | 34dfd72f-3b47-44ab-8315-1cc6ff90e10e | 6 s / 22,5 |
| Cameră de supraveghere 2 | `cctv2-frame-v1.png` (76557d90-ea5d-4e8d-93b4-650bdf4e1854) | 5ad7d45c-ebd1-4cdb-aaa2-5a9aee68278b | 6 s / 22,5 |
| Reveal 3-2-1 | `reveal321-frame-v1.png` (03b8686b-71c6-4f07-a606-4ae17dbb4cef) + cadru final `reveal321-end-v1.png` (312b23d7-bcba-4c51-a48d-321d248a3f74, ref lampă 33e071bd) | f9d97be3-03d8-45fa-b247-baab9b078e99 | 5 s / ~19 |

Replici (în prompt, voce Kling): store — „Wait... what is that?” la ~1,8 s; reveal — „Three,” 0,2 · „two,” 1,1 · „one,” 2,0 · „let's see what comes out!” 2,8–3,8 · copilul „Whoa!” ~4,0.

## Rezultate (27 nov, seara)
- `store-v1.mp4` (6 s, cu sunet): 0–1,3 copilul trage de cardigan; 1,5–2,5 mama se întinde la raft; 3,0–4,5 ia o cutie VortiGlow și o întoarce; 4,5–6 zâmbește, copilul arată spre lampă. Fără nume de magazin. Lampa de pe raft e acoperită o secundă de cutie, apoi reapare neschimbată.
- `cctv2-v1.mp4` (6 s): fetița sare pe pat, o scutură pe mamă, sare jos, aleargă pe covor, ia perna, se urcă înapoi; mama își pune cartea pe față. Fetița rămâne în cadru tot clipul. Cel mai curat dintre hook-uri.
- `reveal321-v1.mp4` (5 s, cu voce): numără 0–2,2, trage pânza la ~2,3 (cerusem 2,9), lampa revelată = cadrul final (din referința reală), copilul cu mâinile pe obraji. Vocea neascultată de Claude — doar nivelul sunetului arată vorbire la ~0,3 / 1,1 / 1,8 / 2,5–3,2 / 3,8.
- Scările: cadrul de start blocat de filtrul de siguranță Higgsfield (`nsfw`, job 1911bab5-a2bc-49bd-978c-75c4b44a00a8), deși ceream varianta fără rănire. Abandonat.

## Montaje de probă (hook + B-roll + text + „Die With A Smile”, refrenul pe tăietură)
- `out/vortiglow-store-preview.mp4` (16,8 s) = store-v1 + `broll/draft-2` (480p mărit local)
- `out/vortiglow-cctv2-preview.mp4` (16,0 s) = cctv2-v1 + `broll/draft-1` (480p mărit local), text „She couldn't stop watching it”
- `out/vortiglow-reveal321-preview.mp4` (15,9 s) = reveal321-v1 + `broll/broll-master-v1` (1080p)
Ciornele 3, 4, 5 de B-roll sunt încă nefolosite.
