# 01 — The business and the model

## The model

- **Organic only, no paid ads.** AI-generated UGC-style short videos (about 11–18 s, 9:16)
  are posted on Instagram, Facebook and TikTok. "Link in bio" leads to a Shopify store.
- Every video is a **C01 hook** (4–5 s, which decides everything) plus B-roll that tells a
  fixed story for that product. Proven hooks are on the Hooks Board (`06_hooks_board.md`).
- Frames are made in Higgsfield (`gpt_image_2` / `gpt_image_2_5`), animated with
  `seedance_2_5`, upscaled, then cut in CapCut with captions and a song. The Swanlift
  product uses Genjutsu motion transfer instead: a competitor reel's motion recast onto a new
  woman and room.
- The niche so far is Christmas decor for a US audience first (orders also came from the
  UK, EU, AU, CA and about 20 more countries). The audience is Christmas moms, parents and
  "Christmas lovers". Swanlift (posture-corrector bra) is the first non-Christmas product.
- What the two Christmas winners had in common (an observation, not a rule): Christmas
  decor, a visual "wow" in a dark room that works without sound, a cheap unit (about $2–3)
  sold at $60–80, and light and small to ship.

## Products on this drive

| Folder | Product | State at the snapshot |
|---|---|---|
| `THEXMASGLOW - CHRISTMAS PROJECTOR` | White dome Christmas projector | 30 videos. The store ran from 2026-09-20 and was stopped 2026-10-06 |
| `MERRYGLOWUSA - LED CURTAIN LIGHTS` | LED curtain lights | 35 videos. Ran Sept 2026, now inactive |
| `MERRYGLOWUSA - CHRISTMAS PROJECTOR` | Christmas projector (other store) | 8 videos. No sales, stopped |
| `SWANLIFT - POSTURE CORRECTOR BRA` | Posture-corrector bra | Motion-transfer test; first product run through the Distribution portal |

## What worked (benchmarks, dated snapshots)

- **TheXmasGlow projector:** $25,817 and 259 orders in the first 6 days (20–25 Sept 2026),
  about $2k in the first 24 h. Price $79.99 per unit. Product cost about $2–3 at the
  factory, about $8–10 delivered to a US customer through an agent.
- **MerryGlowUSA LED curtains:** 126 orders in Sept 2026 (117 by card, $10,965.60).
  Started at $59.95, then bundles of $79.99 / $139.99 / $189.99 (1 / 2 / 3 curtains).
  About 18M views across the accounts.
- **Competitors** (projector niche, `competition/*/data.md`): brand-new Instagram accounts
  hit 1–2M views on a single reel within days. They use "Comment <WORD> to get the link"
  CTAs and Christmas songs or original audio.

## The product (TheXmasGlow)

The real unit is a white dome projector (model XZTYD-01) with a black mesh lens on top,
USB-C plug-in, no battery and swappable Christmas film discs. Describe a product exactly as
the real unit is: on the listing, the box and in the videos.

## Decisions and context

`x_context/` holds the original owner's business context:

- `business.md`: the model, stores, benchmarks, the real product.
- `priorities.md`: what mattered at the time of the snapshot.
- `decisions.md`: dated decisions with their reasons, append-only.

Read them as **history**: they explain why the systems are built the way they are. If
your user wants their own decision log, either keep appending to `decisions.md` (date,
decision, why; never delete a line, reverse it with a new one) or start fresh. Ask them which.
