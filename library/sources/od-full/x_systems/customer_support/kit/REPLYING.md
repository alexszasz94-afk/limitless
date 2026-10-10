# Customer support — answering customers

How customer emails are read, labelled and answered once a store is set up
(`SETUP.md`). Store facts and sign-offs are in `stores.md` and in the
inbox pass prompt (`INBOX_PASS.md`). Most of this is done automatically by
the scheduled inbox pass; the same rules apply when you answer by hand.

## Where the mail is

- One inbox for every store: `<inbox>` — open it as
  `https://mail.google.com/mail/?authuser=<inbox>` and check the tab title.
- Every email sent to a store's support address carries that store's
  top-level label (`<STORE>`) and never goes to Spam (the Gmail filter).
  One store's mail: search `label:"<STORE>"`.
- Spam still catches real customers who wrote to `<inbox>` directly instead
  of the support address. The inbox pass reads every spam message of the
  last 14 days on each run (in Chrome — the Gmail connector cannot see Spam)
  and tells the owner which ones to mark **Not spam**.

## Labels

Two kinds of label on every customer email — **which store** and **what it is**:

| label | use |
|---|---|
| `<STORE>` | set automatically by the store's filter |
| `Customer/Needs Reply` | the customer wrote last and is waiting |
| `Customer/Answered` | answered, nothing open (remove *Needs Reply*) |
| `Customer/Pre-Sale Question` | asked before buying |
| `Customer/Product Request` | asks for a version or design the store does not sell |
| `Customer/Order Issue` | cancel, refund, wrong / damaged item, payment or price complaint |
| `Customer/Shipping & Tracking` | where is my order / tracking / delivery time |
| `Orders/Shopify`, `Orders/Cancellation Request` | Shopify order and cancellation notifications |
| `Payments`, `Payments/PayPal`, `Payments/Unclaimed - ACTION` | payouts, PayPal, unclaimed payments to accept |
| `Suppliers`, `Platform Admin`, `Marketing`, `Suspicious`, `Personal` | non-customer mail |

`Suspicious` is for cold outreach, "is this store active?" one-liners from
random addresses, fake order inquiries, SEO / website-review offers, and
anyone claiming an order that does not exist in Shopify. They get no reply.

## How a reply is written

- **Complete as written.** Ready to send with no placeholders, brackets or
  "[insert …]" for the owner to fill in. The owner should not have to think.
  If a fact is truly missing: answering by hand, ask the owner before
  drafting, never inside the draft; the unattended inbox pass may leave one
  `[<OWNER>: …]` placeholder only as a last resort (`INBOX_PASS.md`).
- **Answer what was asked**, warmly and briefly.
- **Look it up before writing it.** Find the customer in Shopify (orders,
  variant, amount paid, payment / fulfillment / refund status, tracking) and
  check current prices before stating any fact. Never invent prices, stock,
  ship dates, tracking numbers or refund status.
- **Order status wording:** Shopify keeps payment, fulfillment and
  cancellation/refund as three separate states — read all three first.
  Paid + unfulfilled + not cancelled → confirmed, paid and being prepared; a
  tracking email comes when it ships; the store's delivery time. Fulfilled →
  give the tracking. Payment pending / authorized / voided → not paid yet,
  never say it is. Cancelled → say so, and whether it was refunded.
  "Unfulfilled" alone never means "paid".
- **Never offer a refund or a cancellation** unless the customer explicitly
  asked for one. A delay complaint, "when will it arrive?" or "otherwise I'll
  cancel" is not a request: answer the status question only. When they do
  ask, never promise a refund that is not confirmed in Shopify; flag it to
  the owner.
- **Refunds:** a refunded order was charged and then refunded — say "the full
  $X was refunded to your original payment method", never "you haven't been
  charged".
- **Price complaints:** if a customer says the store's price dropped, check
  the price history in Shopify before answering; they may have seen another
  seller or a copy of the store.
- **Short links:** write the store as short clickable text
  (`<a href="https://<domain>"><domain></a>`), never a raw long URL.
- **Sign-off** as in `stores.md` (e.g. `<Owner> — <Brand>`), in the
  customer's language, matching the tone of the owner's past replies.
- A request for something the store does not sell: say it is not available
  right now and that the request has been noted.
- No invented policies: shipping, refunds and cancellations follow the
  store's policy pages.

## One reply per customer per topic

Customers often write several times about the same thing — a follow-up, the
same question twice, a new email plus a reply to the order confirmation, one
copy in the inbox and one in Spam. The owner must end up with **exactly one
reply per customer per topic**, never one per email.

- **Check by store + email address + topic, not by thread.** Before drafting,
  look for any existing draft to that address for that store and any reply the
  owner already sent to it from that store's address, in every thread. With
  several stores the same address can be a customer of two stores; a draft for
  one never counts for the other.
- **Already answered** after their latest message on that topic → no new
  draft; the customer's threads get `Customer/Answered`.
- **A draft already exists** on that topic → do not make another. If a newer
  email adds something, write one new combined draft and delete the old one.
- **Several unanswered emails on one topic** → one combined draft that answers
  everything they asked across all of them, as a reply to their latest
  message. Report the customer once ("3 emails, 1 draft").
- **Duplicate drafts** (e.g. from an earlier run) → keep the most complete,
  most recent one, delete the rest, and say so. Only drafts the pass made may
  be deleted: a reply draft in the customer's thread ending with the exact
  store sign-off. Anything else is the owner's own draft — leave it and report it.
- A genuinely different topic from the same customer (a new order question
  after a pre-sale question was answered) may get its own reply.

Why: on our store a customer sent two emails about the same address change,
both landed in Spam, two runs drafted twice, and the second draft was almost
sent after the first had already gone out.

## Bounces and customers not to answer

- A delivery failure (mailer-daemon, "Recipient inbox full") in a customer
  thread means the reply did **not** arrive: keep `Customer/Needs Reply`, do
  not draft again, tell the owner.
- When the owner decides not to answer someone, that address goes in the
  inbox pass prompt's **Do not reply** list; it keeps its topic label only.

## Before any reply goes out — the From check

The From line must read `<Brand> <support@<domain>>` for that store.
Gmail picks it automatically (*Reply from the same address the message was
sent to*), but:

- a Gmail tab or the phone app opened before a settings change keeps the old
  From until it is reloaded / reopened;
- if it shows `<inbox>`, click the From line and choose the store's address;
- a reply written from inside the Spam folder can go out from `<inbox>` —
  mark the email **Not spam** first, then reply.

An AI drafting replies never sends them: it leaves drafts and the owner sends.
