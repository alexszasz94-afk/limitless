# Customer support — set up one store

The playbook for "set up customer support for store X". Do the phases in
order. Each ends with a **Check** — run it and report what it showed; a phase
is not done until its check passes. Everything here was learned setting up a
live store; the traps are real.

Tools: the **Claude in Chrome** extension (the owner's real Chrome, already
signed in to Shopify admin and Gmail), the **Shopify connector** (Admin
GraphQL) and the **Gmail connector**. The Shopify connector acts on whichever
store it is connected to — check with `get-shop-info` that it is the right
store before any write. "The owner" below is the person you work for.

Placeholders used below — every value comes from the owner (Phase 0):

| placeholder | what it is | example |
|---|---|---|
| `<STORE>` | label / store name, one word | `MyStore` |
| `<Brand>` | the "From" display name customers see | `My Store` |
| `<domain>` | the store's primary domain | `mystore.com` |
| `<handle>` | Shopify admin handle, from `admin.shopify.com/store/<handle>` | `ab12cd-3e` |
| `<inbox>` | the one Gmail account where all support mail is read | a dedicated business Gmail |
| `<N>` | that Gmail's account slot in the owner's Chrome (`/u/<N>/`) | `0`, `1`, `2` … |
| `<Owner>` | the owner's first name, for the sign-off | `Alex` |

---

## Phase 0 — Gather and confirm

1. If there is no `stores.md` yet, copy `STORES_TEMPLATE.md` to `stores.md`.
   If the store already has a section, continue from its open items; if not,
   add one now with what you know.
2. Ask the owner, in one message, only what you cannot find yourself:
   - which store (name + domain);
   - `<inbox>` — the Gmail account that will receive and answer all support
     mail (one inbox for all their stores; a dedicated business Gmail is best);
   - `<Brand>` — the display name customers should see on replies;
   - the sign-off for replies (e.g. `<Owner> — <Brand>`);
   - whether the domain was bought through Shopify (Phase 1 needs it);
   - their time zone (for the inbox pass schedule).
3. Open `https://admin.shopify.com` → pick the store → note `<handle>` from
   the URL and the store name top-right. Run `get-shop-info` on the Shopify
   connector and confirm it returns the same store.
4. Find `<N>`: open `https://mail.google.com/mail/?authuser=<inbox>` and read
   the URL it lands on (`/mail/u/<N>/`) and the tab title (must show
   `<inbox>`). If the inbox is not signed in to this Chrome, the owner signs
   in first.
5. Check the connectors: the Gmail connector must be connected to `<inbox>`
   (search `in:inbox` and compare with what the browser shows); the Shopify
   connector to this store.
6. Tell the owner the plan in one message and list the steps that need them:
   turning on 2-Step Verification if it is off, the App Password, the Gmail
   popup, publishing the theme, sending the test email, approving the
   scheduled task.

**Check:** store name, `<handle>`, `<domain>`, `<inbox>`, `<N>`, `<Brand>` and
the sign-off written in the store's section of `stores.md`.

---

## Phase 1 — Forwarding in Shopify (support@ → inbox)

1. Shopify admin → **Settings → Domains** → click `<domain>`.
2. The header must say **"Managed by Shopify"**. If it does not, **stop**:
   there is no Shopify email forwarding for a third-party domain. Tell the owner
   where the domain's DNS is managed (Domains page → the domain → DNS
   settings / the registrar shown) and do not guess a workaround.
3. Scroll to **Email forwarding** → **Add forwarding email**.
   - Forwarding email address: `support` (the `@<domain>` suffix is fixed)
   - Receiving email address: `<inbox>`
   - **Save**.

**Trap:** typing into this dialog with screen clicks landed the Gmail address
in the wrong field once. Fill fields by their element refs (`find` →
`form_input`), then zoom a screenshot of the dialog to read both fields
before pressing Save.

**Check:** the Email forwarding table shows
`support@<domain> → <inbox>`.

---

## Phase 2 — Gmail: send as support@, file it, never Spam

All in `<inbox>`. Open it with
`https://mail.google.com/mail/?authuser=<inbox>#settings/accounts`
and confirm the tab title shows `<inbox>` (the default
account in the owner's Chrome may be a different one).

### 2a — Google App Password (the owner)

Gmail sends as `support@<domain>` through Google's own SMTP server, logged in
as `<inbox>`, which needs an **App Password**.

- App Passwords only exist when **2-Step Verification** is on. The page
  `myaccount.google.com/u/<N>/apppasswords` shows *"The setting you are looking
  for is not available for your account"* when it is off. Open
  `https://myaccount.google.com/u/<N>/signinoptions/twosv` for the owner — turning
  it on is a security setting, **the owner does it**.
- Then open `https://myaccount.google.com/u/<N>/apppasswords` for the owner. They
  type an app name (`Gmail SMTP - <STORE>`), press Create and copy the
  16-letter code. It must never be pasted into chat.
- One App Password per store, so revoking one never breaks another store.

### 2b — "Add another email address" (the owner fills the popup)

Settings → **Accounts and Import** → Send mail as → **Add another email
address**. Gmail opens a **separate popup window that Claude in Chrome cannot
see or control** (trying to capture it froze the Gmail tab). Give the owner
these values:

| field | value |
|---|---|
| Name | `<Brand>` |
| Email address | `support@<domain>` |
| Treat as an alias | **unticked** |
| SMTP Server | `smtp.gmail.com` |
| Port | `587` |
| Username | `<inbox>` |
| Password | the App Password — **no spaces anywhere** |
| Connection | Secured connection using **TLS** |

**Traps (both happened):**
- Gmail pre-fills the SMTP page with a guess —
  `mx.<domain>.cust.b.hostedemail.com` and username `support`. Both must be
  replaced with `smtp.gmail.com` and `<inbox>`.
- *"Authentication error. Check your username and password."* = the password
  field holds the wrong thing: Chrome autofilled a saved password, or the
  pasted code carried an extra space. Clear the field, paste the code, delete
  any space, Add Account again.

Success screen: *"Congratulations, we successfully located your other server
and verified your credentials… An email with a confirmation link was sent to
support@<domain>."* The owner clicks **Close window**.

### 2c — Confirm the address

1. In `<inbox>` search `"Gmail Confirmation" newer_than:1d` — it arrives
   through the Phase 1 forwarding within a minute, from
   `gmail-noreply@google.com`, subject
   *"Gmail Confirmation - Send Mail as support@<domain>"*.
2. Take the confirmation link from the body (`https://mail.google.com/mail/f-…`)
   and open it **with the account slot inserted**:
   `https://mail.google.com/mail/u/<N>/f-…`.
   **Trap:** without `/u/<N>/` it opens under the default account and pressing
   Confirm does nothing.
3. Press **Confirm**. If the click does not register, submit the page's form
   (`form.requestSubmit()`). The page must change to
   **"Confirmation Success!"**.

**Check:** reload Settings → Accounts and Import: `<Brand> <support@<domain>>`
is listed with no *unverified* tag.

### 2d — Reply settings

Same page, **When replying to a message** →
**Reply from the same address the message was sent to**. This is what makes
each store answer from its own address. Optionally **make default** the
store's address, so new emails also start from it (ask the owner).

**Trap:** a Gmail tab or the phone app that was open before this change keeps
using the old From until it is reloaded. Tell the owner: press F5 on every Gmail
tab, fully close and reopen the Gmail app.

**Check:** open any email sent to `support@<domain>`, press Reply, read the
From field — it shows `<Brand> <support@<domain>>`. Do not type, do not send;
close the reply (an empty reply can still save a draft — tell the owner).

### 2e — Label + filter (never Spam)

The first real test landed in **Spam**. The filter fixes that for good.

1. Settings → **Filters and Blocked Addresses** → **Create a new filter**.
2. **To:** `support@<domain>` (the second field; the first is From) →
   **Create filter**.
3. Tick **Apply the label** → Choose label → **New label…** → `<STORE>`
   (top level, not nested) → Create.
4. Tick **Never send it to Spam**, tick **Also apply filter to N matching
   conversations**. Leave everything else unticked (no archive, no mark as
   read, no delete, no forward).
5. **Create filter**.

**Trap:** Gmail ignores synthetic clicks on these checkboxes and on the
filter/label buttons often. Set checkboxes by clicking the `<input>` whose
`<label>` has the text, dispatch `mousedown/mouseup/click` on buttons, and
read back every checkbox state before saving.

**Check:** the Filters list shows exactly
`Matches: to:(support@<domain>)  Do this: Apply label "<STORE>", Never send it to Spam`.

---

## Phase 3 — Shopify: Store email and Sender email

1. Read the current values and **show them to the owner; wait for their yes.**
   - Settings → General → **Store contact details** → Store email.
   - Settings → **Notifications** → Sender email (a Gmail sender shows the
     note *"Public domains like Gmail don't support custom sending. Customers
     will see your email as store+…@shopifyemail.com"*).
2. Settings → General → Store contact details → **Store email** =
   `support@<domain>` → **Save** (in the top *Unsaved changes* bar).
3. What happened on our store: Shopify **switched the Sender email to
   `support@<domain>` by itself** (status *Unverified*) and sent a
   *"Verify your email address"* email to `support@<domain>`. If the Sender
   did not change, set it in Settings → Notifications → Sender email.
4. In `<inbox>` open *"Verify your email address"* (from the store via
   `mailer@shopify.com`). Its **Verify email** link points to
   `https://<handle>.myshopify.com/admin/sender_emails/verify?token=…` —
   check the handle matches, then open it.
5. For a domain managed by Shopify, **Email domain authentication** goes from
   *Propagating* to *Authenticated* on its own (minutes).

**Traps:** Shopify admin form fields live inside shadow DOM — `find` and
`read_page` do not see them, and screen clicks may not focus them. Locate the
input by walking `shadowRoot`s in JS, `focus()` + `select()` it, then type
with real keystrokes; click Save the same way. Screenshots of the admin
sometimes time out — wait and retry, never act blind.

**Check:** `get-shop-info` returns `email: support@<domain>`; Settings →
Notifications shows the sender without *Unverified* and domain
authentication **Authenticated**.

---

## Phase 4 — Storefront: every address a customer can see

### 4a — Scan

Open `https://<domain>/` in Chrome and run this in the page (javascript
tool); read `window.__scan` ~10 s later. It fetches every page, product and
collection and lists every email address found.

```js
window.__scan='running';(async()=>{const urls=new Set(['/','/pages/contact','/cart','/search?q=a','/collections/all','/404-test','/policies/privacy-policy','/policies/refund-policy','/policies/shipping-policy','/policies/terms-of-service']);
for(const [j,k,p] of [['/products.json?limit=250','products','/products/'],['/collections.json','collections','/collections/'],['/pages.json','pages','/pages/']]){try{(await (await fetch(j)).json())[k].forEach(x=>urls.add(p+x.handle))}catch(e){}}
const out=[];for(const u of urls){try{const r=await fetch(u+(u.includes('?')?'&':'?')+'_='+Date.now(),{cache:'no-store'});if(r.status===404&&u!=='/404-test'){continue}const t=await r.text();
const all=(t.match(/[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z.]{2,}/g)||[]).filter(e=>!/\.(png|jpe?g|webp|svg|gif|js|css)$/i.test(e)&&!/sentry|example|@2x|@3x/i.test(e));
out.push(u+' | '+([...new Set(all)].join(', ')||'-'))}catch(e){out.push(u+' ERR')}}window.__scan=out.join('\n')})();'started'
```

Every address found must be `support@<domain>`. A Gmail (or any other)
address that shows on **every** page, even `/404-test`, is in the theme; one
that shows on a single page is in that page's or policy's text.

### 4b — Pages and policies (Shopify connector)

- `pages(first: 50) { nodes { id handle body } }` → every body containing the
  old address → `pageUpdate(id, page: { body })` with **only the address
  changed** (both the `mailto:` and the visible text). Copy the rest of the
  body byte for byte.
- `shop { shopPolicies { type body } }` → Shopify's generated privacy policy
  already uses the Store email. A custom policy with an old address is fixed
  in Settings → Policies.

On our store the Shipping, Refund and Terms of Service **pages** had the
old Gmail written out 5 times in total — pages made from templates or apps
often hard-code the address the store was created with.

### 4c — Theme (duplicate → edit → prove → the owner publishes)

Find the file: query the live theme's files and search the text, e.g.
`theme(id) { files(filenames: ["sections/*","snippets/*","blocks/*","layout/*","templates/*","config/settings_data.json"], first: 250) { nodes { filename body { ... on OnlineStoreThemeFileBodyText { content } } } } }`.
On our store it was a custom footer section, the footer's *Contact us*
link: `<a href="mailto:<old gmail>">`.

The fix is always `{{ shop.email }}`, never another hard-coded address:
`<a href="mailto:{{ shop.email }}">Contact us</a>`.

Writing the **live** theme is impossible: the Shopify connector refuses
`themeFilesUpsert` on the MAIN theme, and the Shopify code editor in Chrome
does not reliably take typed input. The procedure:

1. `themeDuplicate(id: <live>, name: "<live name> - support email")`.
2. Poll `theme(id) { processing processingFailed }` until
   `processing: false` (took ~3 minutes).
3. Prove the copy is identical: compare `filename` + `checksumMd5` of every
   file of both themes (paginate `files(first: 250, after: …)`).
4. `themeFilesUpsert` on the **copy** with the corrected file — the whole
   file content, one line changed.
5. Prove it on the real storefront with
   `https://<domain>/<path>?preview_theme_id=<copy id>` against the live
   page, for home, contact, cart, a product, collections, search, 404 and
   every policy page: visible text identical, every link identical, the only
   difference the contact address; zero `Liquid error`.
6. Hand over to the owner: Shopify admin → **Online Store → Themes** → the copy →
   **⋯ → Publish**. The old theme stays in the library as the rollback.

**Check (after publish):** run the 4a scan again — every page lists only
`support@<domain>`. Query `themes { nodes { name role } }` and confirm the
copy is `MAIN`.

---

## Phase 5 — End-to-end test (the owner sends)

1. Ask the owner to send a **new** email (not a reply in an old thread) from
   another account to `support@<domain>`.
2. In `<inbox>`: it is in the Inbox (not Spam) with the `<STORE>` label.
   Optional proof — Show original shows `To: support@<domain>` and
   `X-Forwarded-For: support@<domain>`.
3. The owner reloads Gmail, replies, and before sending checks the From line
   says `<Brand> <support@<domain>>`. In the receiving account the reply
   shows `<Brand> <support@<domain>>`, not `<inbox>`.
4. Cleanup only when the owner asks: search the test sender(s) `newer_than:2d`,
   list the threads to them, select exactly those, **Delete** (moves to Trash,
   recoverable 30 days). Check Drafts for empty reply drafts left by 2d.

What went wrong in our first test, and why:
- test landed in Spam → fixed by the 2e filter;
- reply went out from the plain Gmail → the Gmail tab had not been reloaded
  after 2d;
- a reply written *inside the Spam folder* also went from the plain Gmail.

---

## Phase 6 — Labels and the scheduled inbox pass

Skip 6a when the owner's inbox already has the labels from an earlier store,
and in 6c add the new store to the existing inbox pass instead of making a
second one.

### 6a — Topic labels (once per inbox)

Create these Gmail labels in `<inbox>` if they do not exist (Gmail connector
`create_label`, or Gmail → Settings → Labels → Create new label). The names
must be exactly these — the inbox pass looks them up by name:

```
Customer/Needs Reply            Customer/Answered
Customer/Pre-Sale Question      Customer/Order Issue
Customer/Product Request        Customer/Shipping & Tracking
Orders/Shopify                  Orders/Cancellation Request
Payments      Payments/PayPal      Payments/Unclaimed - ACTION
Suppliers     Platform Admin       Marketing      Suspicious      Personal
```

Create a parent (`Customer`, `Orders`, `Payments`) before its children if
Gmail asks for it. `<STORE>` was made in 2e.

**Check:** the Gmail connector's `list_labels` shows every name above plus
`<STORE>`.

### 6b — Fill in the inbox pass prompt

Open `INBOX_PASS.md`, copy the prompt block, and replace every
`<placeholder>` with the owner's values: the stores (name, domain, support
address, `<STORE>` label, sign-off), the **Store facts** (price of every
variant, shipping cost, delivery time, when tracking is sent, return /
refund terms), `<inbox>`, `<N>` and the owner's name. Take prices from the
Shopify connector (`search_products`) and shipping / refund terms from the
store's policy pages — never guess them. Show the owner the filled
**Store facts** block and wait for their yes: every draft will state these
facts to customers.

### 6c — Schedule it

1. Create a Claude **scheduled task** named `Customer support inbox` with the
   filled prompt, once a day in the owner's time zone (e.g. 09:30; if another scheduled task also drives the owner's Chrome, run them at least 30 minutes apart, or they click over each other), with the Gmail and Shopify connectors, allowed to use the
   owner's computer (the Spam check runs in their Chrome), push
   notifications on. The owner approves it. If scheduled tasks are not
   available, give the owner the filled prompt to paste into a chat whenever
   they want a pass.
2. A second store later: do not make a second task — add the store to the
   **Stores** and **Store facts** blocks of the same prompt and update it.
3. Run it once now (fire the task, or run the prompt in this chat) and read
   its report with the owner.

**Check:** the first run reports 0 unlabeled threads and that Spam was read,
and every customer who needs an answer has exactly one draft. Open one
draft with the owner: complete, correct facts, right sign-off; pressing
Reply shows From `<Brand> <support@<domain>>`.

---

## Phase 7 — Record

1. Fill the store's section in `stores.md`: every id, address, date and
   check result, the inbox pass schedule, and any open item.
2. Tell the owner in a short checklist what was done and what is theirs from
   now on: read each draft and press Send; press **Not spam** on real emails
   the pass finds in Spam; tell the AI new facts the drafts should know (a
   policy or price change, a customer not to answer) so the prompt is
   updated — the prompt is the pass's only memory.

---

## Troubleshooting

| symptom | cause → fix |
|---|---|
| No *Email forwarding* on the domain page | domain not managed by Shopify → stop, report where DNS lives |
| App passwords page: "not available for your account" | 2-Step Verification off → the owner turns it on (2a) |
| Popup: "Authentication error" | wrong password in the field or a space in it (2b) |
| Popup: SMTP server `mx.<domain>.cust.b.hostedemail…` | Gmail's guess → `smtp.gmail.com`, user `<inbox>` |
| "Grrr! A popup blocker may be preventing…" | page script patched earlier or a blocker → reload Gmail (F5); allow pop-ups for mail.google.com |
| Confirm button does nothing | link opened without `/u/<N>/` → reopen with it |
| Reply From shows `<inbox>` | Gmail not reloaded after 2d → F5 / reopen app; or From dropdown |
| Customer email in Spam | filter missing or wrong (2e) |
| Sender email "Unverified" | open *Verify your email address* in the inbox (Phase 3) |
| Old address on every storefront page | hard-coded in the theme → 4c |
| Chrome tool calls time out / screenshots freeze | Gmail popup or a modal holds focus → ask the owner to close it; never keep retrying blind |
| Inbox pass: `label:<label id>` finds nothing | search queries need label **names** in quotes (`label:"Customer/Needs Reply"`); `label_thread` needs **ids** |
| Inbox pass: `in:spam` returns nothing | the Gmail connector cannot see Spam — the pass reads it in Chrome |
| Inbox pass: two drafts for one customer | the one-reply rule was skipped (`REPLYING.md`) — keep one, delete the other |
| Draft lost its thread after an edit | `update_draft` detaches it — create a new reply draft, delete the old one |
