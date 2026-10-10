# business.md — what the business is

Evergreen context for any AI working on this drive. Changes rarely.
Rule: only facts that can't be read off the drive. No video counts, folder lists or
"what exists" — count those from disk when needed. Numbers below are dated snapshots.
Scope: AI organic dropshipping only (not the AI influencers, PDFs or YouTube).

## The model

- Organic only, no paid ads. AI-generated UGC-style short videos (~11–18 s, 9:16)
  posted on Instagram, Facebook, TikTok and YouTube Shorts → "Link in bio" → Shopify store.
- Every video: C01 hook (4–5 s, decides everything) + B-roll that tells a fixed story
  for that product. Frames in Higgsfield (gpt_image_2_5), animated with seedance 2.5,
  upscaled, cut in CapCut with captions + song. The how lives in `CLAUDE.md` and
  `x_systems/video_boards/`.
- Current niche: Christmas decor, US audience first (orders also come from UK, EU,
  AU, CA and ~20 more countries).
- Target audience so far: Christmas moms / parents / "Christmas lovers" (the on-screen
  hook texts in `x_systems/hooks/`).
- Daniel runs this solo. Friends in the same business swap information with him
  (no deal, no split); they see only `x_systems_shared/`. Since 2026-10-05 that is only
  the Product Finder, and Daniel shares it with competitors too.

## Stores

| Store | Product | Ownership | Status |
|---|---|---|---|
| TheXmasGlow — thexmasglow.com | Christmas dome projector | 100% Daniel | Stopped by Daniel 2026-10-06; folder shared with a partner |
| MerryGlowUSA — merryglowusa.com | LED curtain lights | A partner's store; Daniel made and posted the videos | Inactive (Sept 2026) |
| MerryGlowUSA | Christmas projector ($129.99) | Same partner's store | Dead: no sales |

- Keep TheXmasGlow and MerryGlowUSA settings completely separate.

## What has worked — benchmarks

**MerryGlowUSA LED curtains** (whole run, Sept 2026):
- 126 orders: 117 paid by card ($10,965.60), 8 PayPal ($899.25), 1 more.
- Price: started at $59.95, then bundles $79.99 / $139.99 / $189.99 (1 / 2 / 3 curtains).

**TheXmasGlow projector** (first order 2026-09-20):
- $25,817 and 259 orders in the first 6 days (20–25 Sept); ~$2k in the first 24 h.
- Price $79.99 for one unit. Product cost ~$2–3 at factory; ~$8–10 delivered to a
  US customer via an agent (quotes in `x_systems/fulfillment/`).

**Competitors** (projector niche, `competition/*/data.md`): brand-new IG accounts hit
1–2M views on a single reel within days. They use "Comment <WORD> to get the link" CTAs
and Christmas songs (Last Christmas, Rockin' Around the Christmas Tree) or original audio.

## Finding products

The **Product Finder** (`x_systems/product_finder/`, since 2026-09-29) is the system:
competitor accounts collected from Instagram / TikTok / Facebook, one product per
account (the latest one it promotes), ranked by followers and average views of the
newest videos; rules in `x_context/decisions.md`. The LED curtains came through the
partner, before it existed. Competitor research for a product lives in its
`competition/` folder.

What the two products have in common (observed, not a rule): Christmas decor, a visual
"wow" in a dark room that works without sound, a cheap unit (~$2–3) sold at $60–80,
light and small to ship.

## The product (TheXmasGlow)

- White dome projector, model XZTYD-01, black mesh lens on top, USB-C plug-in, no
  battery, swappable Christmas film discs. Describe it exactly as the real unit is.

## Money

- Payments by card through Shopify Payments. PayPal is being dropped.

## Where the details live

- How videos are made, naming, boards → `CLAUDE.md`, `x_systems/video_boards/`
- Suppliers and fulfillment → `x_systems/fulfillment/status.md`
- Customer support → `x_systems/customer_support/`
- Hooks and on-screen texts → `x_systems/hooks/`
- Research (prompting guides, sourcing playbook) → `x_research/`
