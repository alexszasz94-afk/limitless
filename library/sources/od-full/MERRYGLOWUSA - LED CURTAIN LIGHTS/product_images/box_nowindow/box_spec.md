# Canonical box spec — MerryGlowUSA LED Curtain Lights

Locked 2026-09-12. Every future generation that shows the box must match this.
No transparent window anywhere. The front is fully printed, opaque, closed cardboard.

## Reference to attach
Always pass the approved packshot as a `medias` entry with role `image`:

- source file: `product_images/box_nowindow/box_nowindow_g5.png` (approved packshot, oversized box)
- previous window version (do NOT use as reference anymore): `product_images/box5_cream_window.png`

Re-upload the approved file with `media_upload` at the start of a session and reuse
that media_id for every call in the session, so the artwork can't drift between shots.

## Physical form
- Matte black rigid retail box, large and flat
- ~55 cm wide x 42 cm tall x 10 cm deep — much wider than the span of two outstretched
  hands; each hand spans less than a quarter of the box width
- Closed and sealed. No lid gap, no cutout, no clear plastic panel
- Same size as the box used in the unboxing starting frames, so packshots and
  unboxing shots now agree

## Front panel, top to bottom
1. Large white condensed uppercase headline: LED CURTAIN LIGHTS
2. Warm gold subline: Create Your Own Magic
3. Red diagonal BEST SELLER ribbon flag, top-right corner
4. One large photographic panel with a thin gold hairline border, filling the middle
   and lower two thirds: night photo of a suburban house facade, glowing pixel LED
   Christmas tree on the garage door, warm fairy-lit trees either side
5. Bottom row of five small gold line icons with white captions:
   DIY Designs / App Control / IP65 Waterproof / Timer Function / Connectable

## Scale lock
The box has no intrinsic scale cue on its own, so every packshot-style shot puts it in
human hands. Two hands, front presentation, stretched wide because the box is big: left
hand on the far left edge near the lower corner, right hand on the far right edge near
the lower corner, thumbs flat on the front face, fingers wrapped around the sides toward
the back, wrists angled slightly outward under the weight, forearms cropped at the wrists
at the bottom of frame, no body and no face. The hands must read as SMALL relative to the
box — that contrast is what sells the size.

For in-scene shots where hands aren't possible, pair the box with a fixed scale anchor
that appears in the same position each time (sofa cushion, doormat, kitchen counter edge)
rather than letting the model choose the size.

## Generation settings
model `gpt_image_2`, `resolution: 2k`, `quality: medium`, `use_unlim: false`,
`aspect_ratio: 1:1` for packshots, `9:16` for ad frames.

## Negatives that must stay in the prompt
NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible
inside, NO glowing lights showing through, box closed and sealed.
