# Fulfillment — logging and drafting

Day-to-day work once the system is set up.

## A message came in (the owner pasted it, or the check found it)

1. Find the supplier's `agents/<name>/conversation.md`. Check the message is
   not already there (same time + same first line).
2. Append it at the bottom, **verbatim**, with this header:

   ```
   ## YYYY-MM-DD HH:MM — <Sender> → <Receiver> (<channel>)
   <the message, exactly as written — typos, emojis, line breaks>
   ```

   Images and files they sent: save them into `agents/<name>/` with a
   descriptive lowercase name and the date (`quote_rates_2026-01-15.png`), and
   link the file under the message.
3. In the same step:
   - `status.md` → that supplier's row: Stage, Waiting on, Next step; and
     `Last updated` at the top (date, time, one line on what changed);
   - `status.md` → *Known facts* for that supplier, if it has a price, rate,
     stock count, date or policy (one line, dated);
   - tracker → Message Log row; Suppliers row; Quotes / Key Facts / To-Do if it
     has numbers or promises. Copy the row style from the row above; keep
     formulas.
4. Tell the owner in one or two lines what is new and what it means for the
   decision.

## The owner asks for a reply

1. Read `status.md` and that supplier's whole `conversation.md` first.
2. Draft it the way the owner writes: short, polite, numbered questions when
   there are several, one clear ask. Never promise a payment date, quantity or
   price the owner has not given. Never reveal the owner's budget.
3. Append it to `conversation.md` as:

   ```
   ## YYYY-MM-DD HH:MM — <Owner> → <Supplier> (<channel>) — DRAFT, not confirmed sent
   ```

4. When the owner says it went out: change `DRAFT, not confirmed sent` to
   `sent`, with the time he gives; if he changed the wording, replace the text
   with what he actually sent.

## Things that look like facts but are not

- A salesperson's "we have N in stock" — ask where the units are.
- A support bot's answer — useful for policies, never for dates or stock.
- "Shipping price for reference" — not a quote.
- A video of the product in a bright room — it does not show what the customer
  will see.
Record them as what they are: "<supplier> said …", not as facts.
