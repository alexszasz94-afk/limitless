# Fulfillment — set it up for one product

The playbook for "set up supplier tracking for product X" and "find me a
supplier for X". Do the phases in order. Each ends with a **Check** — run it
and report what it showed. Everything here was learned sourcing a real product
under time pressure; the traps are real.

Placeholders used below — every value comes from the owner (Phase 0):

| placeholder | what it is | example |
|---|---|---|
| `<STORE>` | the store name | `MyStore` |
| `<domain>` | the store's domain | `mystore.com` |
| `<PRODUCT>` | the product, in one line, with the exact variant | `LED desk lamp, USB-C plug-in, warm white` |
| `<Owner>` | the owner's first name, for drafts | `Alex` |
| `<inbox>` | the owner's business email | `(email removed)` |
| `<folder>` | where the files live | `…/My Business/fulfillment/` |
| `<name>` | one supplier's folder name, lowercase with underscores | `agent_sam`, `cj_dropshipping` |
| `<time zone>` | the owner's time zone, for the check schedule | `Europe/London` |

---

## Phase 0 — Gather and confirm

1. Ask the owner, in one message, only what you cannot find yourself:
    - the store and the product, and **the exact variant that must ship**
      (what is in the box, plug type, colour, pattern — whatever customers see);
    - photos of the real product (the store's listing photo is not enough if
      the listing over-promises — ask what the real unit does and does not do);
    - which countries the orders go to (a rough split is fine);
    - whether they want each order shipped from the supplier (dropshipping /
      agent) or bulk stock first;
    - suppliers already in contact, with the channel for each (WhatsApp number,
      platform chat, email);
    - budget: the highest price per delivered order they would accept (keep
      it private — never tell a supplier);
    - deadline: when the first parcels must ship;
    - their time zone.
2. Count what is owed, from the store (Shopify connector `list-orders`, or the
   owner's export): **paid, unfulfilled** orders only, split by units per order
   (1 / 2 / 3 …) and by country. Unpaid, pending and cancelled orders are
   counted separately — they must never be sent to a supplier.

**Check:** you can state the product + variant, the owed count
(`N orders = M units`, by parcel size), the country split and the deadline,
and the owner has confirmed them.

## Phase 1 — The folder and the status board

1. Make `<folder>` with `agents/` inside it. Copy the kit files in.
2. Copy `STATUS_TEMPLATE.md` to `status.md`. Fill in
   *What we need* from Phase 0.

**Check:** `status.md` opens, *What we need* shows the owed count and the
product variant, and the file reads back exactly as written.

## Phase 2 — The tracker spreadsheet

Make `tracker.xlsx` (openpyxl) with these sheets. Row 1 = title, row 2 = one
line saying what the sheet is for, row 4 = headers, data from row 5. Freeze the
header row, turn on filters. Typed numbers from suppliers in **blue**,
formulas in **black**, anything unconfirmed in a **yellow** fill.

| sheet | columns |
|---|---|
| **Suppliers** | Supplier / agent · Platform · Type (agent, 3PL, factory, marketplace) · Contact person(s) · Contact · Came from · Ships single orders to customers? · Stage · Unit price · US cost per 1-unit order delivered · Delivery days · Shipping quoted · Waiting on · Next step · Last message |
| **Quotes** | Supplier · Option · Carrier · Destination · Units in parcel · Product cost · Shipping · Total per parcel · Cost per unit (`=Total/Units`) · Avg delivery days · Delivery success % · Status · Source (which message) |
| **Backlog** | Order size · Orders · Units (`=Orders × size`) · totals — what is owed |
| **Message Log** | # · Date · Time · Supplier · From · To · Channel · Note · Message (verbatim) |
| **Key Facts** | Supplier · Topic · Fact (one line, with the date it was said) |
| **To-Do** | Supplier · Item · Who (us / them / owner) · Expected by · Status |

Add one sheet per research sweep if you do one (e.g. *Alibaba*, *AliExpress*):
the candidates, their listing, price, and whether they passed the photo check.

**Check:** the file opens, every sheet has its headers, a test formula in
Quotes calculates, and the Backlog totals equal the Phase 0 count.

## Phase 3 — Candidates and the first message

1. **Find candidates** where products actually come from: fulfillment agents
   and dropshipping platforms (e.g. CJ Dropshipping, Zendrop, private agents
   recommended by people the owner trusts), factories on Alibaba (usually bulk
   only — they rarely ship single orders), AliExpress sellers (few units in
   stock, fine for testing only).
2. **The photo gate, before anything else.** A candidate is out unless its
   own photos show the same physical object and the same variant as the
   owner's product. Open the photos; never judge from attribute tables. The
   same shell is often sold with different insides (a different disc, a
   battery version, another plug) — the variant is part of the product.
3. **Make one folder per supplier**: `agents/<name>/`, copy
   `CONVERSATION_TEMPLATE.md` into it as `conversation.md`, add the supplier's
   row to `status.md` (stage `To contact`) and to the Suppliers sheet.
4. **Draft the first message** (the owner sends it). What worked:
    - who the owner is and the store link; a photo + link of the exact product;
    - honesty that the videos look stronger than the real unit, and a request
      for any better version;
    - what is needed: `<M>` units, ship each order to customers, the country
      split, 2–3-unit orders in one parcel;
    - the exact variant that must be in the box, and a request for a photo of it;
    - numbered questions: price per unit at the quantity; shipping cost and days
      per parcel for 1 / 2 / 3 units to each main country; DDP (duties paid, the
      customer never gets a customs bill)?; tracking for every parcel?; how
      orders are sent (store connection or spreadsheet)?; quality check + photos
      before shipping?; lost or broken parcels?; their fee and payment method?;
      how fast they can start?; custom packaging later, and its minimum?
   Log it as `DRAFT, not confirmed sent` (see `LOGGING.md`).

**Check:** every candidate in `status.md` passed the photo gate (say how you
checked), has a folder and a conversation file, and every sent message is
logged verbatim.

## Phase 4 — Logging, every day

From now on every message in or out follows `LOGGING.md`. Stages move:

`To contact` → `First message drafted` → `Sent, waiting reply` → `Quoting` →
`Quote received` → `Negotiating` → `Chosen` / `Rejected`

**Check:** for each supplier, the last message in the channel is the last
entry in its `conversation.md`, and its row in `status.md` says what we are
waiting on.

## Phase 5 — The scheduled supplier check

1. Fill in `SUPPLIER_CHECK.md` with the owner's suppliers, channels, folder
   and time zone. Show it to the owner and confirm the supplier list.
2. Make sure the owner's Chrome is signed in to WhatsApp Web and each supplier
   site, and that Claude in Chrome can reach it.
3. Schedule it as a recurring task, once a day in the owner's working
   hours (e.g. 9:00 `<time zone>`; if the customer support inbox pass also
   runs, run the inbox pass and the supplier check at least 30 minutes apart: both use the owner's Chrome, and two runs driving it at once click over each other), with push notifications on.
4. Run it once by hand and read the report with the owner.

**Check:** the test run logged nothing twice, reported every supplier, and
named any source it could not reach.

## Phase 6 — Compare and decide

1. Put every quote in the Quotes sheet, per destination and parcel size.
   Compare **total per delivered parcel**, weighted by the real order mix from
   the Backlog, and **days until the first parcel ships**.
2. Write a dated comparison in the folder root (`<a>_vs_<b>_<date>.md`): cost
   for the whole backlog, firsthand evidence (how fast and how precisely each
   one answered, what they got wrong and how fast they fixed it), public
   reputation (Trustpilot, app store reviews — check whether the score itself
   is flagged), and their lost / damaged parcel policies. End with a verdict:
   safer vs cheaper.
3. The owner decides. Record the decision in `status.md` → *Decision*, with the
   reason.

**Before the owner pays — check every one of these:**
- [ ] The product in the supplier's dashboard is linked to the right store
      product, and **every variant** (1 / 2 / 3 units, bundles) maps to the
      right quantity — a 2-unit bundle priced as 1 unit is a real, common error.
- [ ] The total in their dashboard matches the quote × the real order mix.
- [ ] Only **paid** orders are in it: remove unpaid, pending, cancelled and
      refunded ones.
- [ ] Only one app will fulfil (auto-fulfil off everywhere else).
- [ ] Stock is real: "in stock" from a salesperson is not a warehouse count.
      Ask where the units are right now (their warehouse or the factory) and
      the date the first parcels ship. Answers from a support bot don't count.
- [ ] Holidays: China shuts for Golden Week (early October) and Chinese New
      Year; factories and sourcing teams stop, some warehouses keep shipping.
      Decide and pay before, or plan the wait.
- [ ] Extra charges: any plan, "account upgrade" or subscription — its price,
      in writing.
- [ ] A photo or video of the real unit that will ship, filmed the way the
      customer uses it.

**Check:** the decision, the reason and every ticked item are in `status.md`.

## Phase 7 — After paying

1. Log the payment (amount, date, what it covers) in `status.md` and Key Facts.
2. Track the promised dates: stock to warehouse, first parcel shipped, tracking
   numbers syncing back to the store.
3. Keep the supplier check running until every owed order has tracking; then
   reduce it to once a day or stop it.

**Check:** every owed order has tracking in the store, and `status.md` says so.

---

## Writing files

Some synced or mounted drives silently cut a file short when it is rewritten.
Write to a temporary location first, copy onto the drive, then compare
checksums (`md5sum`) of both copies. Never rebuild a file from a truncated
tool output — read it fresh, change only what changed.
