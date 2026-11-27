# Start frames — Tornado Vortex Lamp (27 nov 2026)

Concept (Szasz): THE PROBLEM (cameră de supraveghere, noaptea, copilul agitat trage de mama care doarme) vs. unboxing (close-up pe masă, cutie faină) → THE SOLUTION (copilul doarme liniștit lângă lampă).
Model: `gpt_image_2_6`, 2k, 9:16, quality high, 2 credite / imagine (cerut de Szasz pentru cadrele astea).

| Fișier | Job Higgsfield | Referințe |
|---|---|---|
| `problem-v1.png` | dd7c7b6a-f12a-4582-afe5-bec1d2af817d | fără |
| `solution-v1.png` | 70084c75-84ed-4339-8912-eafbdcd2c62d | Image 1 = problem-v1 (job), Image 2 = `ref/lamp-12.jpg` (media 33e071bd-80ce-413a-85b8-5ef77fee15b8) |

## Prompt problem-v1
A real frame from a home security / baby monitor camera at night, infrared night-vision mode: black and white only, slightly soft, fine sensor noise, mild wide-angle lens distortion, flat grey infrared light with no visible lamps on, eyes slightly reflective like real IR footage. The camera is mounted high in the corner of the ceiling and looks down at the whole room. A real, ordinary master bedroom: a large bed with a duvet, two pillows, a nightstand with a phone and a glass of water, a dresser, the door slightly open. A woman in her late 30s is fast asleep on her side under the duvet, exhausted, mouth slightly open. A 5-year-old boy in pajamas, wide awake and restless, kneels on the bed beside her and pulls her arm with both hands, trying to wake her up. Messy sheets, a stuffed toy fallen on the floor. Completely realistic, candid, unstaged, looks like a screenshot from real monitor footage, nothing AI-looking. Vertical 9:16. No text, no timestamp, no logos, no watermarks, no borders.

## Prompt solution-v1
Edit Image 1. Keep EXACTLY the same room, the same camera position high in the ceiling corner, the same wide-angle framing, the same bed, headboard, dresser, door, rug, nightstand, phone and glass of water, the same woman and the same 5-year-old boy in the same dinosaur pajamas. CHANGES: 1) The camera is now in COLOUR low-light mode, not infrared: a real home security camera image in a dim bedroom at night, natural muted colours, slightly soft, fine sensor noise, no black and white. 2) The boy is now fast asleep, lying calmly on his side under the duvet next to his mother, head on the pillow, relaxed face, eyes closed, facing the nightstand. The mother sleeps peacefully on her side as before, both arms relaxed. The duvet is smooth and tidy; the stuffed toy is tucked beside the boy; nothing on the floor. 3) On the nightstand, next to the phone and the glass, stands the lamp of Image 2, switched on: REPRODUCE IT ONE TO ONE from Image 2 - the same straight clear cylinder, the same flat metal lid, the same round black base with the glowing light ring under it, the same thin funnel of tiny beads inside the water, wide at the top and thin at the bottom, glowing the same cyan-blue. Real size: about 28 cm tall, a small table lamp, clearly smaller than the pillow. Never a different lamp, never a bigger vortex, the funnel stays inside the cylinder. The lamp is the only light on in the room: a very soft, gentle cyan-blue glow that reaches only the nightstand, the edge of the pillow and faintly the two sleeping faces; the rest of the room stays dim. Very soft, very natural light, low contrast, no HDR, no bloom halos, no light rays, no CGI look. Completely realistic, candid, looks like a screenshot from real monitor footage. Vertical 9:16. No text, no timestamp, no logos, no watermarks, no borders.

## Verificare (Claude)
- problem-v1: unghi de sus, alb-negru IR, copil în genunchi trage de brațul mamei, mâini corecte, fără text. OK.
- solution-v1: aceeași cameră și mobilă; lampa = cilindru + capac metalic + bază neagră + inel de lumină + pâlnie de mărgele, ca în `ref/lamp-12.jpg`. Abateri: lampa e puțin mai scundă/lată decât cea reală și fără cablu; noptiera s-a mutat puțin în cadru; băiatul e de partea cealaltă a mamei.

## Clip „problema” (27 nov)
- `clips/problem-v1.mp4` — Kling 4.0 image-to-video, 1080p, 9:16, 6 s, 22,5 credite, job 8ddcb0d3-e259-4553-ba27-8563fee655e3, start_image = problem-v1.
- Verificare pe cadre (0,25 s): 0–1,3 trage de braț; 1,5–2,2 sare pe pat cu mâinile sus; 2,3–2,9 sare jos din pat și iese din cadru (stânga-jos); 3,0–4,2 camera goală (copilul nu se vede); 4,3–4,8 revine din spatele patului cu jucăria; 5,0–6,0 se urcă pe pat, mama își pune perna pe cap. Camera fixă, alb-negru, fără text. Minusuri: 1,2 s fără copil; nu se vede alergatul până la ușă; finalul puțin neclar.
- `clips/problem-v1-cut.mp4` — tăiat local (fără credite): 0–2,95 + 4,2–6,04, fără sunet.
- Prompt: vezi jobul (TIMING pe secunde: braț / sărit / fugă la ușă + jucărie / aruncă jucăria, perna pe cap).

## Logo VortiGlow (27 nov)
`logo/logo-1..4.png` (gpt_image_2_6, 1:1, 2k, high, 8 credite; joburi 3d1f0b5e, f8ecf0fa, 5677ac1f, cea14d8f), grilă `logo/logo-options.jpg` (1 sus-stânga, 2 sus-dreapta, 3 jos-stânga, 4 jos-dreapta).

## Unboxing + soluția close-up (27 nov)
| Fișier | Job | Referințe |
|---|---|---|
| `unboxing-v1.png` | d4000071-b208-439f-8e35-1cf19944d142 | Image 1 = `ref/lamp-0.3.jpg` (media eae2cd9a-dee7-4e6e-9cf0-4939e4a566fb, lampa oprită), Image 2 = logo-3 (job 5677ac1f) |
| `solution-closeup-v1.png` | 936f9f0a-0eea-4678-9833-374927b44018 | Image 1 = `ref/lamp-12.jpg` (media 33e071bd), Image 2 = problem-v1 (job dd7c7b6a) |

Logo ales de Szasz: nr. 3 (`logo/logo-3.png`). Prompturile exacte sunt în joburile Higgsfield de mai sus (gpt_image_2_6, 2k, 9:16, high, 2 credite fiecare).

Verificare (Claude):
- unboxing-v1: logo și nume corecte pe capac; lampa = cilindru, capac metalic, bază neagră, mărgele colorate, oprită. Abateri: lampa stă culcată în cutie (cerusem în picioare) și mărgelele stau la capătul cu capacul, deși culcată ar pluti de-a lungul părții de sus; nu știm dacă lampa reală vine cu apă în ea.
- solution-closeup-v1: lampa ca în referință (pâlnie cu inele, inel de lumină la bază), copilul același, lumina moale, fără raze. Capacul pare mai închis la culoare decât metalul real (e în penumbră).

## Refaceri după corecturile lui Szasz (27 nov)
- `unboxing-v2.png` — job 4afe5bc4-bafd-4fe9-9429-0023413b688d. Szasz: „n-are sens cutia, și trebuie să fie de sus”. Acum: cadru drept de sus, capac și bază de aceeași formă, lampa culcată în spumă, cablu USB. v1 rămâne doar ca istoric, nu se folosește. Abatere: mărgelele stau la capătul cu capacul (culcată ar pluti de-a lungul tubului).
- `solution-closeup-off-v1.png` — job 825e6008-d5c2-4179-b8bb-202f8b4fc83a (edit pe solution-closeup-v1 + `ref/lamp-0.3.jpg`). Szasz: în close-up lampa NU e pornită încă; pornește în video și se vede tot efectul. Copilul e treaz, se uită la lampă; lumină caldă slabă din hol.
- Regulă pentru video (din `ref/how-it-works.md`): de la apăsare la tornadă completă ~6 s reale; nu se scurtează.

## Cadre + clipuri pornite (27 nov, seara)
- `unboxing-closed-v1.png` — job fdf9d5a0-b0d4-4753-a2ed-3e7df36c30c4 (edit pe unboxing-v2): cutia închisă, de sus, mâinile pe capac. Szasz: „de sus să fie cutia închisă în primă instanță, după deschide și ia produsul afară”.
- `usb-plug-v1.png` — job e9649a1c-1045-44f8-bda3-640964343462: priza de lângă pat, mâna bagă USB-ul negru în încărcătorul alb. Szasz: „un cadru de la priză lângă pat cum bagă în USB”.
- Clip unboxing: Kling job 34203cbe-9db1-4e7a-8a79-13058f8b5bb0, 6 s, start = unboxing-closed-v1, cadru de mijloc = unboxing-v2 (22,5 credite).
- Clip soluția close-up (lampa pornește): Kling job 82492b75-7d07-453c-b3ac-67c8b6aa6122, 10 s, start = solution-closeup-off-v1, end = solution-closeup-v1 (37,5 credite). Timpi: 0–1 apasă butonul, 1–4 lumină + apa se învârte, 4–7 pâlnia coboară, 7–10 tornadă completă.
