# 09 — Customer support

**What it is:** a proven system for a Shopify store's support email.

- Customers write to and hear from `support@<store-domain>`, never a personal Gmail.
- The owner reads and answers everything for every store in **one Gmail inbox** (Shopify
  forwards the store address there; replies go out through Gmail's "Send mail as" with
  Gmail SMTP and an App Password).
- An AI **scheduled task** goes through the inbox once a day. It labels every email, looks
  each customer up in Shopify, and leaves one complete, ready-to-send **draft** reply per
  customer per topic. It never sends anything: the owner reads the draft and presses Send.

**Folder:** `x_systems/customer_support/kit/`. This is the generic version, with every
personal value replaced by a `<placeholder>`:

| File | What it is |
|---|---|
| `README.md` | Start here: how the mail flows, the rules, which tools the AI needs |
| `SETUP.md` | The setup playbook, Phase 0 (collect the owner's values) → Phase 7 (the scheduled task) |
| `REPLYING.md` | How to answer customers: tone, labels, Shopify lookups, refunds |
| `INBOX_PASS.md` | The scheduled inbox pass prompt, as a template |
| `STORES_TEMPLATE.md` | The per-store settings record. Copy it to `stores.md` and fill it |

`build_shared_card.py` turns the kit into a single shareable HTML page (it needs
`pip install markdown`). It refuses to write if the kit contains a personal value; the
pattern it checks is near the top of the file. Optional.

**To set it up for your user:** read `kit/README.md`, then follow `kit/SETUP.md` in order
and record the result in a new `x_systems/customer_support/stores.md`. It needs the Claude
in Chrome extension, a Gmail connector and a Shopify connector (the kit's README lists what
to do without each).

The original owner's filled-in version (his inbox, store handles, customer threads) was
removed. Only the kit is here.
