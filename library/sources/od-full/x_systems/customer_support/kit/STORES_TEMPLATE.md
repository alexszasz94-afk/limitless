# Customer support — stores

Copy this file to `stores.md`. One section per store. Read a store's section
before touching anything, update it after every change (dated).

## Inbox

| item | value |
|---|---|
| Inbox | `<inbox>` · Chrome account slot `/u/<N>/` |
| Owner name / time zone | `<Owner>` · `<time zone>` |
| Topic labels | created YYYY-MM-DD (SETUP 6a) |
| Scheduled inbox pass | `Customer support inbox` · daily at … · created YYYY-MM-DD |

---

## <STORE> — <domain>

**Status: NOT SET UP / IN PROGRESS (phase N) / LIVE — every check passed YYYY-MM-DD**

| item | value |
|---|---|
| Shopify store | `<STORE>` · admin handle `<handle>` · `<handle>.myshopify.com` |
| Domain | `<domain>` — managed by Shopify? yes / no |
| Support address | `support@<domain>` |
| Forwarding | Shopify → Settings → Domains → `<domain>` → Email forwarding: `support@<domain> → <inbox>` (date) |
| Gmail Send mail as | `<Brand> <support@<domain>>` · not an alias · smtp.gmail.com:587 TLS · user `<inbox>` · App Password (owner's, named `Gmail SMTP - <STORE>`) · confirmed (date) |
| Gmail reply settings | *Reply from the same address the message was sent to* · default From: … (date) |
| Gmail label / filter | label `<STORE>` (top level) · filter `to:(support@<domain>)` → apply `<STORE>`, never Spam (date) |
| Shopify Store email | `support@<domain>` (was …; changed date with the owner's OK) |
| Shopify Sender email | `support@<domain>` · verified · domain authentication **Authenticated** (date) |
| Pages fixed | page ids and what changed (date) |
| Theme | live theme name + id; the file and line changed; published by the owner (date) |
| Rollback theme | name + id — what differs |
| Storefront scan | date: N pages — only `support@<domain>` found |
| End-to-end test | date: inbound in Inbox with label; reply From `<Brand> <support@<domain>>` |
| In the inbox pass | added (date) — prices and store facts confirmed by the owner (date) |

**Replying for this store**
- Sign-off: `<Owner> — <Brand>`
- Link the store as `<domain>`
- Facts the owner has given for answers: …

**Open items**
- …
