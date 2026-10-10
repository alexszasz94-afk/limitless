---
name: "instagram-competitor-research"
description: "Find every Instagram seller of a product (exact or all niche variations), drop inactive/weak accounts, rank by real reel views, open them in Chrome. For market research and competitor hunts."
---

<!-- A procedure the original owner ran as a Claude skill (copied 2026-10-07). "Daniel" = the original owner: read it as your user. To use it as a skill again, save this file as SKILL.md in a skill folder named instagram-competitor-research. -->


# Instagram competitor research

Daniel runs organic (no-ads) dropshipping with AI short-form video. This skill answers one question
completely: **who sells this product on Instagram, and how well is each of them doing?** The answer is
every real, active seller, ranked by the views their reels actually get, each opened in its own Chrome
tab. Follow the steps in order. Every rule exists because breaking it already produced a bad result:
sellers missed, wrong products shown, lists ranked by followers.

## What Daniel gets

1. Every account selling the product (EXACT mode) or any variation of it (VARIATIONS mode), found
   through every channel in Steps 3, 4 and 8, in every language (English first in the summary).
2. Removed before he sees anything, with counts: inactive accounts (no reel in the last 30 days), weak
   accounts (average views of the last 10 reels under 5,000), wrong product, multi-product shops,
   resellers, creators, the reference brand's own accounts.
3. The rest ranked by average views of the last 10 reels, opened in Chrome tabs in that order, 5 at a
   time (his laptop cannot take more Instagram tabs at once).
4. A short chat summary: ranking table, the market in 3-5 lines, a niche map (VARIATIONS), what was
   removed and why, what was searched.
5. Nothing goes onto the Product Finder board until he says so (Step 10).

**Two modes** - pick from his words, ask if unclear:
- **EXACT** (e.g. the posture bra): only accounts selling the same product. Allowed differences:
  colour, print, brand name, price, size. Look-alikes (braces, vests, other bras) are out.
- **VARIATIONS** (e.g. the heated robe): every themed version of the product idea - Grinch, princess,
  football teams, sports, nurse, firefighter, weed, pets, kids... Map which niches exist, who sells
  them and how well each does.

## Hard rules

1. **Browser: Claude in Chrome** (`mcp__claude-in-chrome__*`), Daniel's real Chrome, logged in to
   Instagram. Read the `chrome-browser` skill if it is listed, and load every Chrome tool in one ToolSearch call
   (tabs_context_mcp, tabs_create_mcp, tabs_close_mcp, navigate, computer, javascript_tool,
   browser_batch, get_page_text, find). Never the built-in browser pane (it caps at 9 tabs). If the
   extension does not respond, stop and ask Daniel to open Chrome.
2. **Never measure from search results.** Search hits are a random sample of an account's posts: in
   Oct 2026 @the_vitalys looked like 10K views in search while its real best reel had 902K. Every
   number Daniel sees comes from the account's own newest reels (Step 5).
3. **Never hand-pick.** Every candidate the tier rule selects is measured; every account that passes
   the numbers is looked at. Thresholds apply only to measured numbers.
4. **Rank by performance, never by followers.** Followers are shown, never used to order or filter.
5. **Nothing is presented without being seen.** Every account in the tabs has had its newest reel
   covers looked at (Step 6) and carries a one-line verdict.
6. **A competitor sells the product and its recent feed is mostly that product** (a dedicated store or
   page). Multi-product shops, lingerie/clothing boutiques, wholesalers and "buyer" resellers,
   creators/UGC, health or tai-chi pages and viral-gadget pages that also push it go in the summary,
   not in the tabs (Daniel's correction on @rasafine, Oct 2026). Accounts with the same store link as
   his reference belong to the reference brand.
7. **Board only on his go.** No Product Finder edit, no media download, no file in his folders during
   research. Scratch data lives in browser storage (`icr_*` keys) and this session's workspace. No
   report page unless he asks for one.
8. **His account stays untouched:** never type his password; never follow, like, comment or DM.
9. **Pace and stop.** The library spaces Instagram calls (one every ~2 s, ~28 a minute) and stops
   itself on a block. Never lower `ICR.gap` under 900. On a stop: wait 10 minutes, resume once; if it
   stops again, tell Daniel and finish with what is already measured.

## Step 0 - Set up (5 minutes)

- `tabs_context_mcp` (createIfEmpty), then work in three tabs of that group:
  - **DATA** on `https://www.instagram.com/` - runs the library and holds all the data.
  - **AUX** - Meta Ad Library, Google, Lens, single-reel checks.
  - **OUT** on `https://www.instagram.com/robots.txt` - text dumps and contact sheets.
  Paste **Snippet W** in OUT and in AUX right after opening them (the library does it for DATA): a
  hidden Chrome tab otherwise gets one timer wake-up a minute, snippets time out and screenshots fail.
- Logged in? `document.cookie.includes('ds_user_id')` in DATA. If not, ask Daniel to log in himself.
- One line to Daniel: what you are sweeping, that a full run takes 1.5-3 hours mostly unattended, and
  that Chrome only has to stay open (a covered or minimised window still works).
- `navigate` DATA to the reference account's profile (any profile with 13+ reels works), THEN paste
  **Library A** (Technical reference), then `ICR.reset()` (a new run starts clean), then **Snippet B**:
  it clicks the Reels tab and then another profile so Instagram shows the four request templates the
  library replays. It must answer `templates 4/4` (fix for a missing `_connection` under Snippet B).
  Never `navigate` DATA after pasting A - a page load wipes the library; inside DATA only click.
- **Recovery.** Everything the run learns is saved in DATA's localStorage after every step. A page
  load of DATA, a crash, or a vanished tab group (it happens) loses only the library, the templates and
  the cover images: `navigate` a tab of the group to a profile with 13+ reels, paste A (it reloads the
  saved state - do NOT reset), run B, restart the jobs with `ICR.bg(...)`. Re-pasting A mid-run is
  always safe.
- **Waiting.** Between polls wait with Bash `sleep 100` (the Bash tool stops at 120 s) and do Step 4
  or Step 6 work meanwhile; poll with short `ICR.poll()` calls.

## Step 1 - Lock the product definition and the settings

Open the reference (his link, the store product page, the reference account's top reels), look at the
product images and two or three top reels, then write the definition:

- **EXACT:** must-haves, allowed differences, rejected look-alikes. Example, the Vareny/Swanlift posture
  bra (confirmed 2026-10-05): pull-over, wire-free, seamless V-neck bra with wide straps, open/keyhole
  back, straps that cross and pull forward to an under-bust band that hooks in front; Daniel also
  includes crossed X-back front-closure posture bras. Rejected: brace vests and strap harnesses worn
  over clothes (@luxe.posture - its views come from an X-strap brace vest, even though it also posts a
  few bras -, @espalda_firme, the MONTA corrector creators), lumbar braces, chest compression bands,
  plain seamless/jelly bras, front-zip "magic" vest bras, fajas with a full vertical hook column,
  posture gadgets. Keep the named examples of every definition Daniel confirms in this list.
- **VARIATIONS:** the base every variation shares (e.g. a wearable hooded robe with a heating element),
  the variation axes (theme/character, licensed brand, sport/team, profession, hobby, audience - kids,
  men, pets, couples -, holiday, print/colour), and what is out of scope (a normal non-heated robe).

Settings, stated in the same question: active = a reel in the last 30 days; weak = average views of the
last 10 reels under 5,000 (Daniel's default since 2026-10-07; he may pick another number); all
languages. For seasonal products (Christmas, Halloween, winter wear) the summary also lists "dormant"
sellers - strong last season, quiet now.

Check the reference handle really exists before anything else (Daniel's spelling can be off:
@thevereny was @thevareny) - open it, or `ICR.add('user',['<handle>'])` and look for "handle not found"
in the log.

Send definition + mode + settings in one AskUserQuestion (if he is away, go ahead with your definition
and these defaults and say so in the first line of the summary). Then configure DATA (the match rules decide
who gets measured, so make the word lists wide and multilingual; worked examples in the Technical
reference):

```js
ICR.S.mode='exact';            // or 'variations'
ICR.S.product='posture bra: pull-over V-neck, under-bust hook band, keyhole/X back';
ICR.S.cfg={days:30,minAvg:5000,maxAge:365};
ICR.S.rx={A:'<product noun, every language>', B:'<defining feature/problem words>',
          NEG:'<look-alike product words>', SELL:'<seller cues>'};
```

Write `\\b` (two backslashes) inside these JS strings. Then test the rules: `ICR.tierOf('<product
noun> <feature word> link in bio',false)` must return 1 and `ICR.tierOf('<a look-alike>',false)` 3 or 4;
a "BAD RX" error means a pattern does not compile - fix it before queuing anything.

The library tiers every account from captions, handle and name: **1** = A and B (the product named),
**2** = A plus a seller cue, a hit on the first 3 pages of a core query, or an account found outside
search (ads, Google, handles), **3** = first-3-page hits of a core query without the product noun
(silent sellers hide here), **4** = noise. Tiers 1-3 are measured.

## Step 2 - Build the search vocabulary

Instagram's web search only returns posts for phrasings it has indexed: "bra posture" gives 25+ pages,
"bra for posture" gives nothing. Cover every phrasing, not just the obvious one.

**EXACT mode**
- **Core terms** (searched deep): the product name and every way buyers and sellers write it - both
  word orders ("posture bra", "bra posture"), plurals and joined forms ("posture bras", "posturebra"),
  feature + noun ("posture corrector bra", "posture support bra", "front closure posture bra", "cross
  back posture bra", "wireless posture bra"), what it does ("bra that corrects posture", "bra that
  fixes your posture", "hunchback bra"), "best ...", "... before and after". 15-25 terms.
- **Other terms** (shallow): hook phrases ("this bra fixed my posture", "never going back to a regular
  bra"), review/try-on/plus size, and **every language** with each market's own noun - for a bra:
  sütyen (TR), sujetador/sostén (ES), brasier (MX/CO/VE), corpiño (AR), sutiã (BR), soutien-gorge (FR),
  BH (DE), reggiseno (IT), biustonosz (PL), sutien (RO), бюстгальтер (RU), büstqalter (AZ), حمالة صدر
  (AR) - combined with the feature word (duruş, postura, осанка, Haltung...). The biggest market is
  often not English (for the posture bra: Turkey, then Kazakhstan/Azerbaijan, Latin America); find it.
- **Instagram's own phrasings:** Step 4B collects instagram.com/popular/<topic>/ pages from Google -
  each topic is a phrase Instagram indexes; queue them as kw.
- **Hashtags:** joined core terms in every language (#posturebra, #duruşsütyeni, #brasiercorrector...).
- **Account searches:** "<product>", "<product> shop/store/official", brand-like stems.

**VARIATIONS mode**
- **Base nouns:** every name sellers use for the product - for the heated robe: heated robe, heated
  hoodie blanket, wearable heated blanket, heated blanket hoodie, heated onesie, plus brand-like words
  from handles (therma/heat hug/cozy). Read the captions and handles of the first results and extend.
- **Core terms** (deep): every phrasing of the base ("heated robe", "heated hoodie blanket", "wearable
  heated blanket", "heated blanket hoodie", "heated bathrobe"). Not every phrasing is indexed: on
  2026-10-07 "kids heated robe", "heated robe for men" and "usb heated robe" returned nothing.
- **Theme terms** (`{core:true,max:4}` - see Step 3): "<theme> <base>" for a wide starter list, then for
  every theme sellers show. Starter list: christmas, grinch, santa, elf, gingerbread, reindeer,
  halloween, skeleton, pumpkin, valentine, princess, disney, stitch, hello kitty, barbie, unicorn,
  mermaid, dinosaur, bear, cat, dog, paw, cow print, leopard, camo, tie dye, football, soccer, basketball,
  baseball, hockey, nfl, nba, college, game day, team names (cowboys, eagles, chiefs, packers, steelers,
  49ers, bills, ravens, lions, patriots, barcelona, real madrid...), golf, fishing, hunting, gamer,
  anime, star wars, harry potter, lord of the rings, marvel, nurse, firefighter, police, teacher,
  trucker, farmer, veteran, mom, dad, grandma, couples, kids, baby, dog mom, weed, beer, wine, coffee,
  books, plants, zodiac, birthday.
- **Account searches:** "<theme> <short noun>" for the themes that produce sellers - their handles
  carry the niche (footballrobes, nbaonesies, gamedayrobes, nflcouchh, princesscomfortt).
- Hashtags: the base tags, then "#<theme><base>" for themes that produced sellers.
- The niche map comes from what sellers actually show (Step 6), not from which queries ran.

## Step 3 - Sweep Instagram (DATA, runs in the background)

```js
ICR.add('kw',[/* core terms */],{core:true});            // up to 40 pages each
ICR.add('kw',[/* theme terms (VARIATIONS) */],{core:true,max:4});
ICR.add('kw',[/* other and language terms */]);          // up to 12 pages each
ICR.add('tag',[/* hashtags without # */],{max:8});
ICR.add('acc',[/* account searches */]);
ICR.bg('step'); ICR.bg('measure');   // both return at once and keep running inside the page
```

Run `ICR.bg('step'); ICR.bg('measure')` again after EVERY later `ICR.add` (Steps 4 and 8): a job that
ran out of work has ended, and calling `bg` on a running job does nothing.

- On the first 3 pages of a `core` query, accounts become candidates even when their caption never names
  the product ("Comment NFL if you want one" - most heated-robe sellers write only that), as long as at
  least a fifth of that page does name it. That is why theme terms run as `core` with only 4 pages.
- `measure` measures candidates (Step 5) while the sweep is still finding them and waits for the sweep
  before finishing. Check with `ICR.poll()` every few minutes. Any call that waits on Instagram while
  jobs run can pass the ~45 s tool limit: start such work in the background and read a global later.
- A keyword keeps paging while Instagram has more and the last 3 pages still brought a new tier-1/2
  account. Deep pages matter: on "posture bra" new sellers were still appearing on pages 30-40.
- `STOPPED` = the library stopped itself and kept the item it was on: `HTTP 429` or `FAIL ...` = rate
  limit, network errors and `HTTP 5xx` = Instagram trouble: wait 10 minutes (do Step 4 meanwhile), then
  `ICR.retry()` (puts back accounts and searches that failed with an error) and `ICR.bg(...)` again.
  `NOT JSON`, `HTTP 401/403` = login wall or block: screenshot DATA, ask Daniel. `no template` = run
  Snippet B again. `BAD RX` = fix `ICR.S.rx`. A second stop after resuming: tell Daniel, finish with
  what is measured.

## Step 4 - Channels outside Instagram (AUX, while Step 3 runs)

**A. Meta Ad Library** - every active advertiser for the product, all countries. It finds stores whose
captions never use the product words (Oct 2026: 217 advertisers for the posture bra, some running over
a thousand ads).
1. Open `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=%22<core
   term>%22&search_type=keyword_exact_phrase&media_type=all`, paste Snippet C, then scroll the page
   once (computer scroll down 15) so it reveals its template (`template true`).
2. `FB.run(['"posture bra"','"posture corrector bra"', ... exact phrases in every language ...], 8)`
   (8 pages of 30 ads each); poll `FB.prog`. Then `FB.dump('<A>','<B>')` and read it with get_page_text.
   A full navigation of AUX (e.g. a new Ad Library search) wipes C and W: paste W, then C, again.
3. Copy the `PAIRS` array into DATA: `ICR.add('brand',PAIRS)`. The library searches each brand on
   Instagram and keeps at most 2 accounts whose handle matches the store's domain (the page name only
   when the ads have no store link) - loose name matches flooded the 2026-10-06 run with bakeries and
   sculptors.

**B. Google** - `https://www.google.com/search?q=site%3Ainstagram.com+%22<term>%22` (and `&start=10`) for
the 4-6 strongest core terms and the top non-English term. Run Snippet D on every results page (it
accumulates reel codes, handles and instagram.com/popular/<topic> pages), then `Gdump()` + get_page_text,
and in DATA: `ICR.add('code',codes.map(c=>c+'|google'))`, `ICR.add('user',users)`,
`ICR.add('kw',topics.map(t=>t.replace(/-/g,' ')))` (codes, users and topics are the three lists Gdump
shows). Review `users` first: drop Instagram's own pages and obvious non-sellers.

**C. Google Lens** (EXACT mode) - for 2-3 clean product photos (the reference store's images:
`<store>/products/<handle>.js` lists them): open `https://lens.google.com/uploadbyurl?url=<encoded image
url>`, click "Exact matches", run Snippet D2 - stores using the same supplier photos. Add the
independent stores as `ICR.add('brand',hosts.map(h=>h+'|'+h))` (marketplaces are already skipped).

**D. Shop app search** - WebFetch `https://shop.com/search/results?query=<core term>` (shop.app redirects
there) for 2-3 core terms: it lists Shopify stores and their product titles (Oct 2026: 30 posture-bra
products - big brands plus small stores like Elory, VellCurve, Lovelira, AlignMe). Queue the stores
as `ICR.add('brand',['Store name|',...])`.

**E. Store footers** (optional): for big advertisers the log says have "no IG for brand", WebFetch the
store homepage, read its instagram.com/<handle> link, `ICR.add('user',[handle])`.

Not useful, don't spend time: TikTok search (not logged in, noise), Instagram's similar-accounts list
(empty unless Daniel follows the account), `fbsearch/reels_serp` and keyword typeahead (400/404 on web).

## Step 5 - Measure every candidate (DATA, background)

`ICR.bg('measure')` (already running from Step 3) reads, for every tier 1-3 account, its 12 newest
reels (24 when pinned reels push older ones in) with exact views and dates: average and median of the 10
newest, best of the 10, newest reel date, reels in the last 30 days. Accounts whose newest search hit
is more than a year old are measured only when they also came from the Ad Library, Google or an
account search (`cfg.maxAge`). It costs ~1.3 requests an account: 900 candidates take ~45 minutes.
"Reels in the last 30 days" counts only among the 12-24 reels fetched. Accounts that failed with an
error keep `mErr` and are skipped until `ICR.retry()`. Then:

```js
ICR.judge()      // -> {"pass":..,"inactive":..,"low":..,"none":..} with Daniel's settings
ICR.dormant()    // seasonal products only (summary, not tabs)
```

## Step 6 - Look at every account that passed (OUT tab) - the step that makes or breaks the result

Start as soon as the first few hundred candidates are measured; repeat when measuring ends (accounts
with a verdict never come back).

1. DATA: `ICR.judge(); ICR.bg('sheet')` - collects, for every `pass` account without a verdict, its
   reel covers and its profile (followers, bio, store link - one request each), best first. Poll until
   the sheet job says `N accounts in sheet <stamp>`.
2. OUT: Snippet F, `computer` wait 2 s, screenshot - 8 accounts a screen (fewer on a narrow window),
   each with its 8 newest covers and views, and the bio and link on its title line. F returns the
   exact handles of the page: mark exactly those, then run F again for the next page (one
   browser_batch: the `ICR.mark` calls in DATA, F in OUT, wait, screenshot). If a screenshot fails,
   step back one page before retrying: `sessionStorage.setItem('pg',String(+sessionStorage.getItem('pg')-1))`.
3. After the last page run `ICR.judge(); ICR.bg('sheet')` again and repeat until it reports 0
   accounts (measuring may have added more).

Write a verdict and one line of evidence for every account:
`ICR.mark('velossamco','yes','nude/black V-neck bra, keyhole back, front hook band; TR')`

- **EXACT** - `yes`: the product is in most covers (colour/print/brand may differ). `mixed`: it appears
  but most covers are other products - boutiques, shapewear brands, gadget pages (summary only). `no`:
  look-alike or other product, exercise/physio creators, gadgets. `unclear`: covers don't show it -
  Step 7 decides.
- **VARIATIONS** - `yes` when the base product is in most covers; the note lists the variations seen
  ("Grinch, Stitch, Eagles, plain grey"). These notes build the niche map.
- **The numbers must come from the product.** Before marking `yes`, zoom on the 2-3 most-viewed covers
  of the 8: if the views come from a look-alike or another product, the account is `mixed` or `no`
  whatever its other reels show (@luxe.posture: 2M-view reels of an X-strap brace vest, its bras far
  lower).
- Same store link or same videos across several accounts = a network: `yes` each, note "network:
  <domain>"; the summary groups them under the store. "Comment X for the link" pages that push many
  stores are affiliates: `no`. The reference brand itself and its second accounts: `no`, "reference
  brand".
- Most accounts that pass the numbers are NOT sellers (posture bra, Oct 2026: 21 of 337 - the rest were
  creators, lingerie and shapewear shops, clinics, gadget pages, namesakes of advertisers). That is
  expected - the sweep is wide on purpose and this step is the filter. Judge each one; never skip a
  page. 337 accounts took ~45 minutes of sheets.
- Use `computer` zoom on a cell when a cover is too small to judge.

## Step 7 - Enrich the winners (DATA, background)

`ICR.bg('enrich')` fetches, for every `yes` and `unclear` account: followers, bio, store link, category,
and from its 12 newest posts the share of captions naming the product, top hashtags, audios and tagged
accounts. Dump them (`ICR.out(ICR.table(a=>['yes','unclear'].includes(a.vis)))`, Snippet E,
get_page_text) and settle every `unclear`: the bio or store link names the product -> look at one reel
(Snippet G; reel codes are in `ICR.C['<handle>']` or `ICR.S.acc['<handle>'].m.top`) and decide;
nothing points to it -> `mixed` or `no`.

## Step 8 - Snowball until nothing new

`ICR.seeds()` lists what the `yes` accounts use that was not searched yet: hashtags, store domains,
audios shared by 2+ of them, accounts they tag or collab with. Queue the relevant ones (`tag`,
`brand` as "domain|domain", `aud`, `user`) plus 3-10 hook phrases from their captions (`kw`), then
Steps 3 -> 5 -> 6 -> 7 for the new candidates only. Stop when a round adds no new `yes` (usually after
2 rounds).

## Step 9 - Rank, open the tabs, summarize

1. `ICR.out(ICR.table(a=>a.st==='pass'&&a.vis==='yes'))`, Snippet E, get_page_text = every `yes`, best
   average views first (outputs longer than ~1,000 characters - final, seeds, dormant, tables - always
   go through `ICR.out` + Snippet E). Seasonal products: `ICR.out(ICR.dormant())`, then look at those
   accounts too (`ICR.sheetList=[...handles]; ICR.bg('sheet')`, Snippet F, then `ICR.sheetList=null`) -
   name only the dormant sellers, not dormant creators.
2. First close DATA, AUX and OUT (heavy Instagram pages). Then open the `yes` accounts in rank order,
   **5 at a time** - Daniel's laptop crashes with many Instagram tabs open (Oct 2026): a browser_batch
   of 5 `tabs_create_mcp`, read the Tab IDs, a browser_batch of 5 `navigate` to
   `https://www.instagram.com/<handle>/`, then stop and tell him which ranks are open. Open the next 5
   only when he says so ("next"). No cap overall - every `yes` gets its turn, even if there are only a
   few (say so; never pad). "Tabs cannot be edited right now" = he is moving tabs: wait and retry.
3. Reply in chat:
   - Table: # | Account | Avg views (last 10) | Median | Best of last 10 | Last reel | Reels in 30 days |
     Followers | Market | What it sells (the verdict note).
   - 3-5 lines: who wins and with what kind of reel, how crowded the market is, the English-language
     leaders, the reference account's own numbers, networks.
   - VARIATIONS: niche map - Niche | Sellers | Best avg views | Accounts - and flag licensed or
     trademarked themes (Grinch, Disney, NFL/team logos, cannabis brands): copying them risks takedowns.
   - Removed, one line each with counts: inactive (+ notable ones, e.g. a big seller that stopped
     posting), under 5,000 average views, wrong product, mixed shops/creators/resellers (name the big ones).
   - Coverage in one line: searches and pages, posts and accounts seen, accounts measured, advertisers
     and Google results checked, blind spots (Stories, private accounts, ads-only stores with no Instagram).
4. Then wait. Daniel closes the tabs he doesn't want; the tabs still open are his approved list. Leave
   `icr_state` in the browser for follow-up questions (paste A in any instagram.com tab to reach it);
   the next run starts with `ICR.reset()`. If he asks for a written report, make it a private artifact
   page (load artifact-design): sellers, niche map, networks, big mixed shops, inactive, rejected
   look-alikes, coverage. Never a file in his folders.

## Step 10 - Board import (only when Daniel says "add them")

- Read the open tabs with `tabs_context_mcp`: those handles are the approved list.
- Follow the `product-finder-import` skill from its step 1, with these differences: the links come from
  the kept tabs, not WhatsApp (skip its step 2); the evidence file is
  `raw/research/update_<mon><dd>_competitors_review.json` with
  `"source": "instagram-competitor-research (<reference product>)"`, and `audit.latestImport.source`
  says the same. Everything else is the same: triage (existing accounts keep their card), Apify
  histories, latest-run boundary from footage (an account that interleaves another product is
  `review`, not ranked), second-opinion subagent, media, one dated batch, `product_finder.py all`
  exit 0, browser check, report.
- The Chrome extension cannot open `file://` pages unless Daniel allows file URLs for it; otherwise
  check the board in a headless Chromium in the workspace (it cannot play H.264 - say so).

## Talking to Daniel during the run

- He is often away and impatient. One line at the start ("Sweeping Instagram for X, ~N hours").
- Mid-run updates only with measured, verified facts. Never send a "top competitors" list before Step 6
  is done; if he asks, say what is confirmed and what is still being checked.
- If he corrects an item ("that's not the same product", "that shop sells other stuff"), apply it to
  every account with the same pattern, and fold it into this skill when he asks.

---

# Technical reference

Paste every block exactly as written. The library keeps its state in DATA's localStorage (`icr_state`),
so re-pasting it mid-run is safe.

### Library A (DATA)

```js
await (async()=>{
const I=window.ICR=window.ICR||{};
I.IG='https://www.instagram.com';
I.csrf=()=>(document.cookie.match(/csrftoken=([^;]+)/)||[])[1]||'';
I.H=()=>({'x-ig-app-id':'936619743392459','x-requested-with':'XMLHttpRequest','x-csrftoken':I.csrf()});
I.sleep=ms=>new Promise(r=>{const ch=new MessageChannel();ch.port1.onmessage=()=>setTimeout(r,ms);ch.port2.postMessage(0)}); // the message hop avoids chained-timer clamping; I.awake below stops hidden-tab throttling
I.awake=async()=>{if(I.rtc&&I.rtc.a.connectionState==='connected')return 'awake';try{const a=new RTCPeerConnection(),b=new RTCPeerConnection(); // a local WebRTC loopback, no network: Chrome stops throttling a hidden tab's timers to one a minute while WebRTC is in use
 a.onicecandidate=e=>e.candidate&&b.addIceCandidate(e.candidate);b.onicecandidate=e=>e.candidate&&a.addIceCandidate(e.candidate);const dc=a.createDataChannel('icr');
 await a.setLocalDescription(await a.createOffer());await b.setRemoteDescription(a.localDescription);await b.setLocalDescription(await b.createAnswer());await a.setRemoteDescription(b.localDescription);I.rtc={a,b,dc};return 'awake'}catch(e){return 'awake failed: '+e.message}};
I.gap=I.gap||1000;I.last=I.last||0;
I.q0=I.q0||Promise.resolve();
I.wait=()=>{const p=I.q0.then(async()=>{const d=I.last+I.gap+Math.random()*1000-Date.now();if(d>0)await I.sleep(d);I.last=Date.now()});I.q0=p.catch(()=>{});return p};
I.T=I.T||{};I.C=I.C||{};
I.fresh=()=>({posts:{},acc:{},q:[],done:{},log:[],n:{req:0,bad:0,err:0},rx:{},mode:'exact',tags:{},cfg:{days:30,minAvg:5000,maxAge:365}});
I.S=I.S||(()=>{try{return JSON.parse(localStorage.getItem('icr_state'))}catch(e){return null}})()||I.fresh();
for(const k in I.S.posts){const p=I.S.posts[k];if(!Array.isArray(p))I.S.posts[k]=[p.u,p.t]} // posts keep only [handle, time]: localStorage holds ~5 MB
I.S.n.err=I.S.n.err||0;
I.save=()=>{try{const s=JSON.stringify(I.S);localStorage.setItem('icr_state',s);I.saveErr='';return Math.round(s.length/1024)+'KB'}catch(e){I.saveErr='SAVE FAILED '+e.name;return I.saveErr}};
I.reset=()=>{I.stop();I.S=I.fresh();I.C={};['icr_state','icr_out','icr_sheet'].forEach(k=>localStorage.removeItem(k));return 'clean'};
if(!I.hooked){I.hooked=1;
 const keep=(u,b)=>{try{const n=new URLSearchParams(String(b)).get('fb_api_req_friendly_name');if(n&&/\/graphql/.test(String(u)))I.T[n]={u:String(u),b:String(b)}}catch(e){}};
 const of=window.fetch;window.fetch=function(i,o){try{if(o&&o.body)keep(typeof i==='string'?i:i.url,o.body)}catch(e){}return of.apply(this,arguments)};
 const oo=XMLHttpRequest.prototype.open,os=XMLHttpRequest.prototype.send;
 XMLHttpRequest.prototype.open=function(m,u){this.__u=u;return oo.apply(this,arguments)};
 XMLHttpRequest.prototype.send=function(b){try{if(b)keep(this.__u,b)}catch(e){}return os.apply(this,arguments)};}
const err=(m,s)=>{const e=new Error(m);e.status=s;return e};
I.stopErr=e=>{const s=e.status;return s===undefined||s===0||s===-1||s===401||s===403||s===429||s>=500}; // block, login wall, network or our own setup: stop and keep the item
I.gqlBad=0;
I.rest=async(path,opt={})=>{await I.wait();I.S.n.req++;const r=await fetch(I.IG+path,{credentials:'include',...opt,headers:{...I.H(),...(opt.headers||{})}});const t=await r.text();
 if(r.status!==200){I.S.n.bad++;throw err('HTTP '+r.status,r.status)}
 let j;try{j=JSON.parse(t.replace(/^for \(;;\);/,''))}catch(e){I.S.n.bad++;throw err('NOT JSON (login wall or block)',0)}
 if(j&&j.status==='fail'){I.S.n.bad++;throw err('FAIL '+String(j.message||j.feedback_message||'').slice(0,80),429)}return j};
I.gq=async(name,patch)=>{const t=I.T[name];if(!t)throw err('no template '+name+' - paste Snippet B again',-1);const p=new URLSearchParams(t.b);p.set('variables',JSON.stringify(patch(JSON.parse(p.get('variables')||'{}'))));
 await I.wait();I.S.n.req++;
 const r=await fetch(t.u.startsWith('http')?t.u:I.IG+t.u,{method:'POST',credentials:'include',headers:{'content-type':'application/x-www-form-urlencoded','x-csrftoken':I.csrf(),'x-ig-app-id':'936619743392459','x-fb-lsd':p.get('lsd')||'','x-fb-friendly-name':name},body:p.toString()});
 const txt=await r.text();if(r.status!==200){I.S.n.bad++;throw err('HTTP '+r.status,r.status)}
 let j;try{j=JSON.parse(txt.split('\n')[0].replace(/^for \(;;\);/,''))}catch(e){I.S.n.bad++;throw err('NOT JSON',0)}
 if(!j.data){I.S.n.bad++;I.gqlBad++;throw err('GQL '+JSON.stringify(j.errors||j).slice(0,100),I.gqlBad>=3?-1:-2)}I.gqlBad=0;return j.data};
I.tokens=()=>{const t=I.T['PolarisProfilePostsQuery']||Object.values(I.T)[0];const p=new URLSearchParams(t.b);['fb_api_caller_class','fb_api_req_friendly_name','variables','doc_id','server_timestamps'].forEach(k=>p.delete(k));return p};
I.medias=(o,out=[],seen=new Set())=>{if(!o||typeof o!=='object')return out;if(o.code&&o.user&&o.user.username&&o.taken_at){if(!seen.has(o.code)){seen.add(o.code);out.push(o)}return out}for(const k in o){const v=o[k];if(v&&typeof v==='object')I.medias(v,out,seen)}return out};
I.views=m=>m.play_count??m.ig_play_count??m.view_count??null;
I.pkTime=pk=>Math.round(Number((BigInt(pk)>>23n)+1314220021721n)/1000);
I.mid=c=>{const A='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';let n=0n;for(const ch of c.slice(0,11))n=n*64n+BigInt(A.indexOf(ch));return n.toString()};
I.norm=s=>String(s||'').toLowerCase().normalize('NFKD').replace(/[^a-z0-9]/g,'');
I.rootOf=h=>{const L=String(h||'').toLowerCase().replace(/^www\./,'').split('.');let i=L.length-2;while(i>0&&['myshopify','mitiendanube','com','co','net','org','shop','store'].includes(L[i]))i--;return L[Math.max(i,0)]||''};
I.aff=/^s?(?:the|my|get|try|shop|shopp|store|official|oficial|online|brand|co|inc|llc|ltd|hq|wear|bra|bras|shapewears?|lingerie|intimates|boutique|beauty|care|fashion|clothing|collection|apparel|wellness|health|club|house|hub|world|global|life|style|usa|uae|ksa|brasil|mexico)*(?:[a-z]{2})?$/;
I.brandHit=(x,name,dom)=>{const un=I.norm(x.username),fn=I.norm(x.full_name),r=I.norm(I.rootOf(dom));const keys=r.length>=4?[I.norm(dom),r]:[I.norm(name)];
 return keys.some(k=>k.length>=4&&(un===k||(r.length>=4&&fn===k)||((un.startsWith(k)||un.endsWith(k))&&I.aff.test(un.replace(k,'')))))}; // the store domain decides; the page name only when there is no domain
I.audioOf=m=>{const c=m.clips_metadata||{};return c.original_sound_info?.audio_asset_id||c.music_info?.music_asset_info?.audio_cluster_id||null};
I.rx=()=>{const key=JSON.stringify(I.S.rx||{});if(I._rx&&I._rxk===key)return I._rx;const r=I.S.rx||{},o={};
 for(const k of ['A','B','NEG','SELL']){try{o[k]=r[k]?new RegExp(r[k],'i'):null}catch(e){throw err('BAD RX '+k+': '+e.message,-1)}}I._rx=o;I._rxk=key;return o};
I.tierOf=(txt,core)=>{const R=I.rx();const a=!!(R.A&&R.A.test(txt)),b=!!(R.B&&R.B.test(txt)),s=!!(R.SELL&&R.SELL.test(txt)),n=!!(R.NEG&&R.NEG.test(txt));
 let t=(a&&b)?1:(a&&(s||core))?2:core?3:4;if(n&&!(a&&b)&&t===2)t=3;return t};
I.acc=(u,pk,fn)=>{const a=I.S.acc[u]=I.S.acc[u]||{pk:'',fn:'',src:[],n:0,tier:9,best:0};if(pk&&!a.pk)a.pk=String(pk);if(fn&&!a.fn)a.fn=String(fn).slice(0,60);return a};
I.bump=(a,tier,src)=>{a.n++;if(src&&a.src.length<10&&!a.src.includes(src))a.src.push(src);const was=a.tier;a.tier=Math.min(a.tier,tier);return (was>2&&a.tier<=2)?1:0};
I.addMedia=(m,src,core)=>{const u=m.user.username;const cap=(m.caption?.text||'').replace(/\s+/g,' ');
 const tier=I.tierOf(cap+' '+u+' '+(m.user.full_name||''),core);
 if(!I.S.posts[m.code])I.S.posts[m.code]=[u,m.taken_at];
 const a=I.acc(u,m.user.pk||m.user.id||m.user.pk_id,m.user.full_name);const v=I.views(m)??0;if(v>a.best)a.best=v;return I.bump(a,tier,src)};
I.addUser=(x,src,force)=>{const s=x.username+' '+(x.full_name||''),R=I.rx();let t=I.tierOf(s,!!((R.A&&R.A.test(s))||(R.B&&R.B.test(s)))); // a handle with the product noun = tier 2, with only the feature word = tier 3
 if(force)t=Math.min(t,2);return I.bump(I.acc(x.username,x.pk||x.pk_id||x.id,x.full_name),t,src)};
I.add=(k,qs,o={})=>{let n=0;for(let q of [].concat(qs)){q=String(q).trim();if(!q)continue;const key=k+':'+q.toLowerCase();if(I.S.done[key]||I.S.q.some(x=>x.k+':'+x.q.toLowerCase()===key))continue;I.S.q.push({k,q,core:!!o.core,max:o.max||(o.core?40:12),p:0,dry:0,rel:0});n++}return n+' queued, queue '+I.S.q.length};
I.finish=it=>{const d=I.S.done[it.k+':'+it.q.toLowerCase()]={p:it.p,rel:it.rel,mc:it.mc,ng:it.noGrid};if(it.err)d.err={k:it.k,q:it.q,core:it.core,max:it.max,e:it.err};I.S.q.shift()};
I.summary=()=>{const A=Object.values(I.S.acc);const c=t=>A.filter(a=>a.tier===t).length;return 'posts '+Object.keys(I.S.posts).length+' | accounts '+A.length+' (t1 '+c(1)+', t2 '+c(2)+', t3 '+c(3)+') | measured '+A.filter(a=>a.m).length+' | queue '+I.S.q.length+' | requests '+I.S.n.req+' bad '+I.S.n.bad+' | errors '+I.S.n.err};
I.step=async(budget=30000)=>{const t0=Date.now();let req=0;const S=I.S;
 while(S.q.length&&Date.now()-t0<budget){const it=S.q[0];
  try{
   if(it.k==='kw'){let p='/api/v1/fbsearch/web/top_serp/?enable_metadata=true&query='+encodeURIComponent(it.q)+'&search_session_id='+(it.ss||(it.ss=crypto.randomUUID()));
    if(it.nm)p+='&next_max_id='+encodeURIComponent(it.nm)+'&rank_token='+encodeURIComponent(it.rt||'');
    const j=await I.rest(p);req++;
    if(!j.media_grid&&Array.isArray(j.list)){let nu=0;j.list.forEach(x=>{if(x.user)nu+=I.addUser(x.user,'kw:'+it.q);if(x.hashtag)S.tags[x.hashtag.name]=x.hashtag.media_count});it.p++;it.rel+=nu;it.noGrid=1;I.finish(it);continue}
    const g=j.media_grid||{};let nr=0;const ms=I.medias(g.sections||[]);
    const on=ms.filter(m=>I.tierOf((m.caption?.text||'')+' '+m.user.username+' '+(m.user.full_name||''),false)<=2).length; // a core page is trusted only when 20%+ of it names the product
    ms.forEach(m=>nr+=I.addMedia(m,'kw:'+it.q,it.core&&it.p<3&&on>=0.2*ms.length));
    it.p++;it.rel+=nr;it.dry=nr?0:it.dry+1;
    if(g.has_more&&g.next_max_id&&it.p<it.max&&!(it.p>=3&&it.dry>=3)){it.nm=g.next_max_id;it.rt=g.rank_token||j.rank_token}else I.finish(it)}
   else if(it.k==='tag'){let ms,nx;const tg=encodeURIComponent(it.q.replace(/^#/,''));
    if(!it.nm){const j=await I.rest('/api/v1/tags/web_info/?tag_name='+tg);req++;const d=j.data||{};ms=I.medias([d.top?.sections,d.recent?.sections]);nx=d.top||{};it.mc=d.media_count}
    else{const body=new URLSearchParams({max_id:it.nm,page:it.pg,surface:'grid',tab:'top',include_persistent:'0',next_media_ids:JSON.stringify(it.mids||[])});
     nx=await I.rest('/api/v1/tags/'+tg+'/sections/',{method:'POST',headers:{'content-type':'application/x-www-form-urlencoded'},body});req++;ms=I.medias(nx.sections||[])}
    let nr=0;ms.forEach(m=>nr+=I.addMedia(m,'tag:'+it.q,false));it.p++;it.rel+=nr;it.dry=nr?0:it.dry+1;
    if(nx.more_available&&nx.next_max_id&&it.p<it.max&&!(it.p>=3&&it.dry>=3)){it.nm=nx.next_max_id;it.pg=nx.next_page;it.mids=nx.next_media_ids}else I.finish(it)}
   else if(it.k==='acc'){const j=await I.rest('/web/search/topsearch/?context=blended&include_reel=true&query='+encodeURIComponent(it.q));req++;
    let nr=0;(j.users||[]).forEach(x=>nr+=I.addUser(x.user,'acc:'+it.q));(j.hashtags||[]).forEach(h=>S.tags[h.hashtag.name]=h.hashtag.media_count);it.rel=nr;I.finish(it)}
   else if(it.k==='user'){const j=await I.rest('/web/search/topsearch/?context=user&query='+encodeURIComponent(it.q));req++;
    const x=(j.users||[]).map(y=>y.user).find(y=>y.username.toLowerCase()===it.q.toLowerCase());if(x)I.addUser(x,'user:'+it.q,true);else S.log.push('handle not found: '+it.q);I.finish(it)}
   else if(it.k==='brand'){const [name,dom]=it.q.split('|');const tries=[name,I.rootOf(dom)].filter((x,i,a)=>x&&x.length>=3&&a.indexOf(x)===i);let nr=0,hit=0;
    for(const q of tries){const j=await I.rest('/web/search/topsearch/?context=user&query='+encodeURIComponent(q));req++;
     (j.users||[]).map(y=>y.user).filter(x=>I.brandHit(x,name,dom)).slice(0,2).forEach(x=>{hit++;nr+=I.addUser(x,'ad:'+name.slice(0,30),true)});if(hit)break}
    it.rel=nr;if(!hit)S.log.push('no IG for brand: '+name);I.finish(it)}
   else if(it.k==='code'){const [code,src]=it.q.split('|');const j=await I.rest('/api/v1/media/'+I.mid(code)+'/info/');req++;const m=(j.items||[])[0];
    if(m){I.addMedia(m,'web:'+(src||'google'),true);const a=I.S.acc[m.user.username];if(a&&a.tier>2)a.tier=2}I.finish(it)}
   else if(it.k==='aud'){const p=I.tokens();p.set('audio_cluster_id',it.q);p.set('original_sound_audio_asset_id',it.q);p.set('max_id',it.nm||'');
    const j=await I.rest('/api/v1/clips/music/',{method:'POST',headers:{'content-type':'application/x-www-form-urlencoded','x-fb-lsd':p.get('lsd')||''},body:p.toString()});req++;
    const pl=j.payload||j;let nr=0;I.medias(pl.items||[]).forEach(m=>nr+=I.addMedia(m,'aud:'+it.q,false));it.p++;it.rel+=nr;
    const pi=pl.paging_info||{};if(pi.more_available&&pi.max_id&&it.p<4){it.nm=pi.max_id}else I.finish(it)}
   else I.finish(it);
  }catch(e){S.log.push(it.k+':'+it.q+' p'+it.p+' '+e.message);
   if(I.stopErr(e)){I.save();return 'STOPPED on '+it.k+':'+it.q+' -> '+e.message+' | '+I.summary()}
   S.n.err++;it.tries=(it.tries||0)+1;if(it.tries<2)S.q.push(S.q.shift());else{it.err=e.message.slice(0,60);I.finish(it)}}}
 return req+' req this step | '+I.summary()+' | saved '+I.save()};
I.stats=(reels)=>{const now=Date.now()/1000;const s=reels.slice().sort((x,y)=>y.t-x.t);const l=s.slice(0,10);const vs=l.map(r=>r.v||0);const srt=vs.slice().sort((a,b)=>a-b);
 return {n:s.length,avg10:vs.length?Math.round(vs.reduce((a,b)=>a+b,0)/vs.length):0,med10:srt.length?srt[Math.floor(srt.length/2)]:0,max10:vs.length?Math.max(...vs):0,
  last:s[0]?s[0].t:0,d30:s.filter(r=>now-r.t<30*86400).length,top:s.slice().sort((x,y)=>(y.v||0)-(x.v||0)).slice(0,3).map(r=>r.c+':'+r.v),at:Math.round(now)}};
I.reels=async(a,after)=>{const pk=a.pk;
 const d=after?await I.gq('PolarisProfileReelsTabContentQuery_connection',v=>({...v,after,first:12,id:pk,data:{...(v.data||{}),target_user_id:pk}}))
  :await I.gq('PolarisProfileReelsTabContentQuery',v=>({...v,data:{...(v.data||{}),page_size:12,target_user_id:pk},user_id:pk}));
 const cc=(d.fetch__XDTUserDict||d.node||Object.values(d)[0]||{}).clips_connection||{};
 return {rs:(cc.edges||[]).map(e=>e.node.media||e.node).map(m=>({c:m.code,v:I.views(m),t:I.pkTime(m.pk),pin:!!(m.clips_tab_pinned_user_ids||[]).length,img:(()=>{const cs=m.image_versions2?.candidates||[];return (cs.filter(c=>(c.width||0)>=320).slice(-1)[0]||cs[0]||{}).url||''})()})),next:cc.page_info?.has_next_page?cc.page_info.end_cursor:null}};
I.measureOne=async(u,a)=>{if(!a.pk){const j=await I.rest('/web/search/topsearch/?context=user&query='+encodeURIComponent(u));const x=(j.users||[]).map(y=>y.user).find(y=>y.username===u);if(!x){a.mErr='not found';return}a.pk=String(x.pk||x.pk_id||x.id)}
 const r=await I.reels(a);let rs=r.rs;if(rs.filter(x=>!x.pin).length<10&&r.next&&rs.length>=12){const r2=await I.reels(a,r.next);rs=rs.concat(r2.rs)}
 I.C[u]=rs.slice().sort((x,y)=>y.t-x.t).slice(0,8).map(x=>[x.c,x.v,x.img]);a.m=I.stats(rs)};
I.hitAge=()=>{const now=Date.now()/1000,h={};for(const [u,t] of Object.values(I.S.posts))h[u]=Math.max(h[u]||0,t||0);const o={};for(const u in h)o[u]=(now-h[u])/86400;return o};
I.todo=(maxTier=3,maxAge=365)=>{const age=I.hitAge();return Object.entries(I.S.acc).filter(([u,a])=>a.tier<=maxTier&&!a.m&&!a.mErr&&(!(u in age)||age[u]<=maxAge||a.src.some(s=>/^(acc|user|ad|web|handle):/.test(s)))).sort((x,y)=>x[1].tier-y[1].tier||(age[x[0]]??0)-(age[y[0]]??0))};
I.measure=async(budget=30000,maxTier=3)=>{const t0=Date.now();let n=0;const S=I.S;const todo=I.todo(maxTier,S.cfg?.maxAge||365);
 for(const [u,a] of todo){if(Date.now()-t0>budget)break;
  try{await I.measureOne(u,a);n++}
  catch(e){S.log.push('measure '+u+' '+e.message);if(I.stopErr(e)){I.save();return 'STOPPED measuring at '+u+' -> '+e.message}a.mErr=e.message.slice(0,50);S.n.err++}}
 return n+' measured this step, '+Math.max(0,todo.length-n)+' left | saved '+I.save()};
I.judge=(days=I.S.cfg?.days||30,minAvg=I.S.cfg?.minAvg||5000)=>{I.S.cfg={...(I.S.cfg||{}),days,minAvg};const now=Date.now()/1000;const c={pass:0,inactive:0,low:0,none:0};for(const a of Object.values(I.S.acc)){if(!a.m)continue;
 a.st=!a.m.n?'no-reels':(now-a.m.last>days*86400)?'inactive':(a.m.avg10<minAvg)?'low':'pass';c[a.st==='no-reels'?'none':a.st]++}I.save();return JSON.stringify(c)};
I.dormant=(minAvg=I.S.cfg?.minAvg||5000)=>Object.entries(I.S.acc).filter(([u,a])=>a.st==='inactive'&&a.m.avg10>=minAvg&&Date.now()/1000-a.m.last<365*86400).sort((x,y)=>y[1].m.avg10-x[1].m.avg10).map(([u,a])=>u+' avg10 '+I.fmt(a.m.avg10)+' last '+I.day(a.m.last)).join('\n');
I.prof=async(u,a)=>{const d=await I.gq('PolarisProfilePageContentQuery',v=>({...v,id:a.pk}));const x=d.user||{};const link=(x.bio_links||[]).map(b=>b.url).concat(x.external_url||[]).filter(Boolean)[0]||'';
 a.p={...(a.p||{}),fol:x.follower_count??null,bio:(x.biography||'').replace(/\s+/g,' ').slice(0,160),link:link.replace(/^https?:\/\/(www\.)?/,'').slice(0,80),cat:x.category||'',posts:x.media_count??null,ver:!!x.is_verified}};
I.toEnrich=a=>a.st==='pass'&&['yes','unclear'].includes(a.vis)&&!(a.p&&(a.p.full||a.p.caps||a.p.err));
I.enrich=async(budget=30000)=>{const t0=Date.now();let n=0;const R=I.rx();
 for(const [u,a] of Object.entries(I.S.acc)){if(Date.now()-t0>budget)break;if(!I.toEnrich(a))continue;
  try{if(!a.p||a.p.fol===undefined)await I.prof(u,a);
   const t=await I.gq('PolarisProfilePostsQuery',v=>({...v,username:u}));const ed=(t.xdt_api__v1__feed__user_timeline_graphql_connection?.edges||[]).map(e=>e.node);
   const caps=ed.map(m=>(m.caption?.text||'').replace(/\s+/g,' '));const hit=caps.filter(c=>(R.A&&R.A.test(c))||(R.B&&R.B.test(c))).length;const withCap=caps.filter(c=>c.length>3).length;
   const tags={};caps.forEach(c=>(c.match(/#[\p{L}\p{N}_]+/gu)||[]).forEach(h=>{h=h.toLowerCase();tags[h]=(tags[h]||0)+1}));
   a.p={...a.p,full:1,
    share:withCap?Math.round(100*hit/withCap):null,caps:caps.slice(0,6).map(c=>c.slice(0,70)),tags:Object.entries(tags).sort((p,q)=>q[1]-p[1]).slice(0,12).map(e=>e[0]),
    auds:[...new Set(ed.map(I.audioOf).filter(Boolean))].slice(0,12),ut:[...new Set(ed.flatMap(m=>(m.usertags?.in||[]).map(z=>z.user?.username).concat((m.coauthor_producers||[]).map(z=>z.username))).filter(Boolean))].filter(z=>z!==u).slice(0,12)};n++}
  catch(e){I.S.log.push('enrich '+u+' '+e.message);if(I.stopErr(e)){I.save();return 'STOPPED enriching at '+u+' -> '+e.message}a.p={...(a.p||{}),err:e.message.slice(0,50)};I.S.n.err++}}
 const left=Object.values(I.S.acc).filter(I.toEnrich).length;return n+' enriched, '+left+' left | saved '+I.save()};
I.retry=()=>{let a=0,q=0;for(const x of Object.values(I.S.acc)){if(x.mErr&&x.mErr!=='not found'){delete x.mErr;a++}if(x.p&&x.p.err){delete x.p.err;a++}}
 for(const [k,d] of Object.entries(I.S.done))if(d.err){delete I.S.done[k];I.S.q.push({k:d.err.k,q:d.err.q,core:d.err.core,max:d.err.max,p:0,dry:0,rel:0});q++}
 I.save();return a+' accounts and '+q+' searches back in line - start the jobs again'};
I.jobs=I.jobs||{};
I.bg=(what)=>{const J=I.jobs[what];if(J&&J.on)return what+' already running';const j=I.jobs[what]={on:1,t0:Date.now(),last:'started'};
 (async()=>{try{while(j.on){let r;
   if(what==='step'){if(!I.S.q.length)break;r=await I.step(30000)}
   else if(what==='measure'){r=await I.measure(30000,I.S.maxTier||3);if(/ 0 left/.test(r)){if(I.jobs.step&&I.jobs.step.on){j.last='waiting for the sweep';await I.sleep(20000);continue}j.last=r;break}}
   else if(what==='enrich'){r=await I.enrich(30000);if(/ 0 left/.test(r)){j.last=r;break}}
   else if(what==='sheet'){r=await I.sheet(I.sheetList);if(!/still need/.test(r)){j.last=r;break}}
   else break;
   j.last=r;if(/STOPPED/.test(r))break}}catch(e){j.last='CRASH '+e.message}
  j.on=0;j.end=Date.now()})();return what+' started'};
I.stop=(what)=>{for(const k in I.jobs)if(!what||k===what)I.jobs[k].on=0;return 'stopping after the current call'};
I.poll=()=>(I.saveErr?I.saveErr+' !! ':'')+Object.entries(I.jobs).map(([k,j])=>k+(j.on?' RUNNING ':' done ')+Math.round(((j.end||Date.now())-j.t0)/60000)+'min: '+String(j.last).slice(0,110)).join(' || ')+' || '+I.summary()+' | log: '+I.S.log.slice(-2).join(' ; ').slice(0,160);
I.mark=(u,verdict,note='')=>{const a=I.S.acc[u];if(!a)return 'no such account '+u;a.vis=verdict;a.note=String(note).slice(0,140);I.save();return u+' -> '+verdict};
I.seeds=()=>{const P=Object.entries(I.S.acc).filter(([u,a])=>a.vis==='yes'&&a.p&&!a.p.err);const cnt=f=>{const c={};P.forEach(([u,a])=>new Set(f(a)).forEach(x=>c[x]=(c[x]||0)+1));return c};
 const tags=Object.entries(cnt(a=>a.p.tags||[])).filter(([t])=>!I.S.done['tag:'+t.slice(1)]).sort((x,y)=>y[1]-x[1]).slice(0,40).map(([t,c])=>t+'('+c+')');
 const doms=Object.entries(cnt(a=>[(a.p.link||'').split('/')[0]])).filter(([d])=>d&&!/linktr|beacons|bio\.|instagram|wa\.me|whatsapp|tiktok|youtube|facebook|lnk|bit\.ly/.test(d)).map(([d,c])=>d+'('+c+')');
 const auds=Object.entries(cnt(a=>a.p.auds||[])).filter(([x,c])=>c>=2&&!I.S.done['aud:'+x]).map(([x,c])=>x+'('+c+')');
 const ut=[...new Set(P.flatMap(([u,a])=>a.p.ut||[]))].filter(u=>!I.S.acc[u]);
 const seen=Object.entries(I.S.tags||{}).filter(([t])=>!I.S.done['tag:'+t.toLowerCase()]).sort((x,y)=>y[1]-x[1]).slice(0,30).map(([t,c])=>t+'('+c+')');
 return 'TAGS '+tags.join(' ')+'\nDOMAINS '+doms.join(' ')+'\nAUDIOS(2+) '+auds.join(' ')+'\nTAGGED '+ut.join(' ')+'\nTAGS SEEN IN SEARCH '+seen.join(' ')};
I.out=(text,key='icr_out')=>{try{const st=String(Date.now());localStorage.setItem(key,text);localStorage.setItem(key+'_stamp',st);return 'wrote '+text.length+' chars, stamp '+st+' - show it in OUT with Snippet E'}catch(e){return 'OUT FAILED '+e.name}};
I.fmt=n=>n==null?'-':n>=1e6?(n/1e6).toFixed(1)+'M':n>=1e3?(n/1e3).toFixed(1)+'K':String(n);
I.day=t=>t?new Date(t*1000).toISOString().slice(0,10):'-';
I.row=(u,a)=>[u,'avg10 '+I.fmt(a.m?.avg10)+(a.m&&a.m.n<10?' (n'+a.m.n+')':''),'med '+I.fmt(a.m?.med10),'max '+I.fmt(a.m?.max10),'last '+I.day(a.m?.last),'30d '+(a.m?.d30??'-'),'fol '+I.fmt(a.p?.fol),'share '+(a.p?.share??'-')+'%','cat '+(a.p?.cat||''),'t'+a.tier,(a.vis?a.vis+': '+(a.note||''):''),'src '+a.src.slice(0,3).join(','),'link '+(a.p?.link||''),'bio '+(a.p?.bio||'').slice(0,100),'caps '+(a.p?.caps||[]).slice(0,3).join(' / ')].join(' | ');
I.table=(f=a=>a.st==='pass')=>Object.entries(I.S.acc).filter(([u,a])=>f(a)).sort((x,y)=>(y[1].m?.avg10||0)-(x[1].m?.avg10||0)).map(([u,a])=>I.row(u,a)).join('\n');
I.final=()=>Object.entries(I.S.acc).filter(([u,a])=>a.st==='pass'&&a.vis==='yes').sort((x,y)=>y[1].m.avg10-x[1].m.avg10).map(([u])=>u);
I.sheet=async(list,budget=30000)=>{const t0=Date.now();list=list||Object.entries(I.S.acc).filter(([u,a])=>a.st==='pass'&&!a.vis).sort((x,y)=>y[1].m.avg10-x[1].m.avg10).map(([u])=>u);let miss=0;const bad=[];
 for(const u of list){const a=I.S.acc[u];if(!a){bad.push(u);continue}const needC=!(u in I.C),needP=!a.p||a.p.fol===undefined;if(!needC&&!needP)continue;if(Date.now()-t0>budget){miss++;continue}
  try{if(needC)await I.measureOne(u,a);if(needP&&a.pk)await I.prof(u,a)}catch(e){if(I.stopErr(e)){I.save();return 'STOPPED building the sheet at '+u+' -> '+e.message}if(!(u in I.C))I.C[u]=[];if(!a.p)a.p={err:e.message.slice(0,50)};bad.push(u)}}
 if(miss)return miss+' accounts still need covers or a profile - the sheet job keeps going';
 const out=list.filter(u=>I.S.acc[u]).map(u=>{const a=I.S.acc[u];return {u,line:'avg10 '+I.fmt(a.m?.avg10)+' | last '+I.day(a.m?.last)+' | fol '+I.fmt(a.p?.fol)+' | '+(a.p?.link||'').slice(0,40)+' | '+(a.p?.bio||'').slice(0,90),covers:I.C[u]||[]}});
 const st=String(Date.now());try{localStorage.setItem('icr_sheet',JSON.stringify(out));localStorage.setItem('icr_sheet_stamp',st)}catch(e){return 'SHEET NOT SAVED '+e.name}
 I.save();return out.length+' accounts in sheet '+st+(bad.length?' | no covers/profile: '+bad.join(','):'')+' - draw it in OUT with Snippet F'};
const aw=await I.awake();
return 'ICR ready | '+aw+' | templates '+['PolarisProfileReelsTabContentQuery','PolarisProfileReelsTabContentQuery_connection','PolarisProfilePageContentQuery','PolarisProfilePostsQuery'].filter(k=>I.T[k]).length+'/4 | '+I.summary();
})()
```

What it gives you: `ICR.add(kind, list, opts)` queues searches (`kw`, `tag`, `acc`, `user`, `brand`
"Name|domain", `code` "reelcode|source", `aud` audio id); `ICR.bg('step'|'measure'|'sheet'|'enrich')`
runs a job inside the page; `ICR.poll()` reports; `ICR.stop()` stops all jobs after their current call;
`ICR.retry()` puts back what failed with an error; `ICR.judge(days,minAvg)`, `ICR.dormant()`,
`ICR.mark(handle,verdict,note)`, `ICR.seeds()`, `ICR.table(filter)`, `ICR.final()`, `ICR.out(text)` (for
Snippet E), `ICR.tierOf(text,false)` (test the match rules), `ICR.summary()`, `ICR.reset()`. State keys:
`ICR.S.acc[handle]` = {tier, src, m: measured numbers, st: pass/inactive/low/no-reels, vis/note: verdict,
p: profile}; `ICR.C[handle]` = the 8 newest reels as [code, views, cover url] (memory only).

### Snippets

**Snippet W - keep a tab awake** (paste once in OUT and in AUX right after opening them; Library A does
the same for DATA). Chrome throttles timers in a tab hidden for 5+ minutes to one wake-up a minute -
snippets then time out and screenshots fail ("Script injection timed out") - unless WebRTC is in use.
This opens a WebRTC connection between two endpoints inside the page itself (no network traffic, no prompt):

```js
await (async()=>{if(window.__rtc)return 'awake';const a=new RTCPeerConnection(),b=new RTCPeerConnection();a.onicecandidate=e=>e.candidate&&b.addIceCandidate(e.candidate);b.onicecandidate=e=>e.candidate&&a.addIceCandidate(e.candidate);a.createDataChannel('w');
 await a.setLocalDescription(await a.createOffer());await b.setRemoteDescription(a.localDescription);await b.setLocalDescription(await b.createAnswer());await a.setRemoteDescription(b.localDescription);window.__rtc={a,b};return 'awake'})()
```

**Snippet B - capture the request templates** (DATA, while it shows any profile that has reels):

```js
await (async()=>{const w=ms=>new Promise(r=>setTimeout(r,ms));
 const rl=[...document.querySelectorAll('a[href]')].find(a=>/^\/[^/]+\/reels\/?$/.test(a.getAttribute('href')));
 if(!rl)return 'open a profile that has reels first';rl.click();await w(4000);scrollTo(0,document.body.scrollHeight);await w(3000);
 const cur=location.pathname.split('/')[1];
 const me=[...document.querySelectorAll('a[href]')].find(a=>{const h=a.getAttribute('href');return /^\/[A-Za-z0-9_.]+\/$/.test(h)&&!['/reels/','/explore/','/popular/','/'+cur+'/'].includes(h)});
 if(me){me.click();await w(4000)}
 const need=['PolarisProfileReelsTabContentQuery','PolarisProfileReelsTabContentQuery_connection','PolarisProfilePageContentQuery','PolarisProfilePostsQuery'];
 return 'templates '+need.filter(k=>ICR.T[k]).length+'/4 '+need.filter(k=>!ICR.T[k]).join(' ')})()
```
`_connection` is often missing in a background window, because a script scroll does not make Instagram
load more reels there. Then: `history.back()` (or open the profile's Reels tab again), two `computer`
scrolls of 10 ticks down over the reel grid with 3 s waits (real wheel events do load more), and check
`!!ICR.T.PolarisProfileReelsTabContentQuery_connection`. The templates carry Daniel's session tokens:
they stay in page memory only, never in storage or chat.

**Snippet C - Meta Ad Library collector** (AUX, on an Ad Library results page; scroll once after pasting):

```js
window.FB=window.FB||{T:null,ads:{},prog:[]};
if(!FB.h){FB.h=1;
 const keep=(u,b,r)=>{try{if(new URLSearchParams(String(b)).get('fb_api_req_friendly_name')==='AdLibrarySearchPaginationQuery'){FB.T={u:String(u),b:String(b)};if(r)FB.parse(r)}}catch(e){}};
 const oo=XMLHttpRequest.prototype.open,os=XMLHttpRequest.prototype.send;
 XMLHttpRequest.prototype.open=function(m,u){this.__u=u;return oo.apply(this,arguments)};
 XMLHttpRequest.prototype.send=function(b){const x=this;x.addEventListener('load',()=>keep(x.__u,b,x.responseText));return os.apply(this,arguments)};
 const of=window.fetch;FB.of=of.bind(window);window.fetch=async function(i,o){const res=await of.apply(this,arguments);try{if(o&&o.body){const c=res.clone();c.text().then(t=>keep(typeof i==='string'?i:i.url,o.body,t))}}catch(e){}return res}}
FB.parse=txt=>{let n=0;String(txt).split('\n').forEach(l=>{try{const c=JSON.parse(l).data?.ad_library_main?.search_results_connection;if(!c)return;FB.cursor=c.page_info?.has_next_page?c.page_info.end_cursor:null;
 (c.edges||[]).forEach(e=>(e.node.collated_results||[]).forEach(r=>{const s=r.snapshot||{};let d='';try{d=new URL(s.link_url||'').hostname.replace(/^www\./,'')}catch(x){}
  const a=FB.ads[r.page_id]=FB.ads[r.page_id]||{name:r.page_name,dom:{},n:0,first:9e9,q:{},txt:''};a.n+=(r.collation_count||1);if(d)a.dom[d]=1;a.first=Math.min(a.first,r.start_date||9e9);a.q[FB.curQ||'?']=1;
  const tx=v=>typeof v==='string'?v:(v&&v.text)||'';const t=[tx(s.body),s.title,s.link_description,s.caption,...(s.cards||[]).map(k=>tx(k.body)+' '+(k.title||''))].filter(Boolean).join(' ').replace(/\s+/g,' ');
  if(t&&a.txt.length<600&&!a.txt.includes(t.slice(0,40)))a.txt+=' '+t.slice(0,200);n++}))}catch(e){}});return n};
FB.page=async(q,cursor)=>{const p=new URLSearchParams(FB.T.b);const v=JSON.parse(p.get('variables'));v.queryString=q;v.cursor=cursor||null;v.searchType=/^".*"$/.test(q)?'keyword_exact_phrase':'keyword_unordered';v.sessionID=crypto.randomUUID();p.set('variables',JSON.stringify(v));
 const r=await (FB.of||fetch)(FB.T.u.startsWith('http')?FB.T.u:'https://www.facebook.com'+FB.T.u,{method:'POST',credentials:'include',headers:{'content-type':'application/x-www-form-urlencoded','x-fb-lsd':p.get('lsd')||'','x-fb-friendly-name':'AdLibrarySearchPaginationQuery'},body:p.toString()});FB.curQ=q;return FB.parse(await r.text())};
FB.run=(qs,max=8)=>{FB.on=1;(async()=>{for(const q of qs){let cur=null,pg=0;do{let n=0;try{n=await FB.page(q,cur)}catch(e){FB.prog.push(q+' ERR '+e.message);break}pg++;if(!n)break;cur=FB.cursor;await new Promise(r=>setTimeout(r,1500+Math.random()*1000))}while(cur&&pg<max);FB.prog.push(q+':'+pg+'p')}FB.on=0})();return 'started'};
FB.dump=(A,B)=>{const ra=A?new RegExp(A,'i'):null,rb=B?new RegExp(B,'i'):null;const skip=/(^|\.)(whatsapp|instagram|facebook|fb|amzn|amazon|tinyurl|linktr|bit|wa|tiktok|youtube|google|apple)\./;
 const seen=new Set(),pairs=[],lines=[],off=[];
 Object.values(FB.ads).sort((a,b)=>b.n-a.n).forEach(a=>{const host=Object.keys(a.dom).find(h=>!skip.test(h+'.'))||'';const k=(a.name+'|'+host).toLowerCase();if(seen.has(k))return;seen.add(k);
  const t=a.txt+' '+a.name,rel=(!ra||ra.test(t))&&(!rb||rb.test(t));
  const line=a.name+' | '+a.n+' ads | '+Object.keys(a.dom).slice(0,2).join(',')+' | since '+new Date(a.first*1000).toISOString().slice(0,10)+' | '+a.txt.trim().slice(0,90);
  if(rel){pairs.push(a.name.replace(/\|/g,' ')+'|'+host);lines.push(line)}else off.push(line)});
 document.body.innerHTML='<pre id=o style="white-space:pre-wrap"></pre>';document.getElementById('o').textContent=lines.join('\n')+'\n\nOFF-PRODUCT, not queued ('+off.length+')\n'+off.join('\n')+'\n\nPAIRS '+JSON.stringify(pairs);
 return pairs.length+' advertisers on the product, '+off.length+' off-product - read with get_page_text'};
'Ad Library collector ready - template '+!!FB.T
```
`FB.run([...])` then poll `'on '+FB.on+' '+Object.keys(FB.ads).length+' | '+FB.prog.join(' ; ')`. When
`on 0`: `FB.dump('<rx A>','<rx B>')` with the A and B strings from Step 1 (an advertiser is kept only when
its ad text names the product), get_page_text, skim the OFF-PRODUCT list for stores the words missed,
then copy the `PAIRS` array into `ICR.add('brand', PAIRS)` in DATA.

**Snippet D - Google collector** (AUX, run on each Google results page; results add up across pages):

```js
window.G=JSON.parse(sessionStorage.getItem('G')||'{"codes":{},"users":{},"topics":{}}');
[...document.querySelectorAll('a[href*="instagram.com/"]')].forEach(a=>{const p=a.href.replace(/^https?:\/\/([a-z]+\.)?instagram\.com\//,'').split(/[?#]/)[0];let m;
 if(m=p.match(/^(?:[A-Za-z0-9_.]+\/)?(?:reel|reels|p|tv)\/([A-Za-z0-9_-]{10,})/))G.codes[m[1]]=1;else if(m=p.match(/^popular\/([^/]+)/))G.topics[m[1]]=1;else if(m=p.match(/^([A-Za-z0-9_.]{3,30})\/?$/))G.users[m[1]]=1});
sessionStorage.setItem('G',JSON.stringify(G));
window.Gdump=()=>{document.body.innerHTML='<pre id=o style="white-space:pre-wrap"></pre>';document.getElementById('o').textContent=JSON.stringify({codes:Object.keys(G.codes),users:Object.keys(G.users).filter(u=>!/^(explore|accounts|about|legal|developer|reels|stories|popular)$/.test(u)),topics:Object.keys(G.topics)});return 'read with get_page_text'};
'codes '+Object.keys(G.codes).length+' users '+Object.keys(G.users).length+' topics '+Object.keys(G.topics).length
```

**Snippet D2 - Lens exact matches** (AUX, after clicking "Exact matches"; if the list is cut off,
`__d2.join(' ').slice(900)` shows the rest):

```js
const skip=/google|gstatic|youtube|amazon|ebay|walmart|aliexpress|alibaba|temu|shein|etsy|mercadoli|mercadoliv|ubuy|desertcart|tiendamia|ozon|wildberries|trendyol|hepsiburada|facebook|instagram|tiktok|pinterest|reddit/;
window.__d2=[...new Set([...document.querySelectorAll('a[href^="http"]')].map(a=>{try{return new URL(a.href).hostname.replace(/^www\./,'')}catch(e){return ''}}).filter(h=>h&&!skip.test(h)))];
__d2.length+' hosts: '+__d2.join(' ').slice(0,900)
```

**Snippet E - show a text dump** (OUT, on instagram.com/robots.txt; then get_page_text). Tabs see each
other's localStorage with a short delay, so it waits for the new stamp:

```js
await (async()=>{let st='';for(let i=0;i<30;i++){st=localStorage.getItem('icr_out_stamp')||'';if(st&&st!==sessionStorage.getItem('shown'))break;await new Promise(r=>setTimeout(r,300))}
 sessionStorage.setItem('shown',st);const v=localStorage.getItem('icr_out')||'(empty)';
 document.body.innerHTML='<pre id=o style="white-space:pre-wrap;font:12px monospace;margin:4px"></pre>';document.getElementById('o').textContent=v;return 'shown '+v.length+' chars, stamp '+st})()
```

**Snippet F - contact sheet** (OUT; screenshot after each run). Eight accounts a screen, two per row,
each with its 8 newest reel covers and their views. It returns at once with the handles shown, in order -
use those exact handles in `ICR.mark` (they often end in `_` or `.`):

```js
(()=>{const st=localStorage.getItem('icr_sheet_stamp')||'';if(st!==sessionStorage.getItem('sheet')){sessionStorage.setItem('sheet',st);sessionStorage.setItem('pg','0')}
 const all=JSON.parse(localStorage.getItem('icr_sheet')||'[]');const pg=+(sessionStorage.getItem('pg')||0);
 const W=Math.max(900,innerWidth-4),H=Math.max(480,innerHeight-4),K=8,pr=W>=1300?2:1,bw=Math.floor(W/pr),cw=Math.floor(bw/K),ch=Math.floor(cw*1.45),rowH=ch+19,rows=Math.max(1,Math.floor(H/rowH)),per=rows*pr;
 const list=all.slice(pg*per,pg*per+per);document.body.innerHTML='';document.body.style.cssText='margin:0;background:#fff;overflow:hidden';
 const cv=document.createElement('canvas');cv.width=W;cv.height=rows*rowH;document.body.appendChild(cv);const x=cv.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,W,cv.height);
 const fmt=n=>n==null?'-':n>=1e6?(n/1e6).toFixed(1)+'M':n>=1e3?Math.round(n/1e3)+'K':String(n);
 list.forEach((a,i)=>{const bx=(i%pr)*bw,y=Math.floor(i/pr)*rowH;
  x.save();x.beginPath();x.rect(bx,y,bw-6,rowH);x.clip();x.fillStyle='#000';x.font='bold 13px Arial';x.fillText((pg*per+i+1)+'. @'+a.u+'  '+a.line,bx+2,y+14);x.restore();
  a.covers.slice(0,K).forEach((c,k)=>{const cx=bx+k*cw,cy=y+17;const lab=()=>{x.fillStyle='rgba(0,0,0,.75)';x.fillRect(cx,cy+ch-15,cw-2,15);x.fillStyle='#fff';x.font='11px Arial';x.fillText(fmt(c[1]),cx+2,cy+ch-4)};
   x.fillStyle='#ddd';x.fillRect(cx,cy,cw-2,ch);lab();
   if(c[2]){const im=new Image();im.onload=()=>{const s=Math.max((cw-2)/im.width,ch/im.height),sw=(cw-2)/s,sh=ch/s;x.drawImage(im,(im.width-sw)/2,(im.height-sh)/2,sw,sh,cx,cy,cw-2,ch);lab()};im.src=c[2]}})});
 x.fillStyle='#d00';for(let r=1;r<rows;r++)x.fillRect(0,r*rowH-2,W,2);if(pr>1)x.fillRect(bw-4,0,3,cv.height);
 sessionStorage.setItem('pg',String(pg+1));
 return 'page '+(pg+1)+'/'+Math.ceil(all.length/per)+' of sheet '+st+' | '+list.map((a,i)=>(pg*per+i+1)+'.'+a.u).join(' ')})()
```
Then `computer` wait 2 s and screenshot. The returned sheet stamp must equal the one `ICR.sheet`
reported; if it is older, wait 2 s and run F again (`sessionStorage.setItem('pg','0')` restarts a
sheet, `'pg','N'` jumps to page N+1). It draws on a canvas, so Daniel's "Download All" extension cannot
cover the covers with its arrows. Use `computer` zoom on a row when a cover is too small to judge.

**Snippet G - look inside a reel** (AUX, on `https://www.instagram.com/reel/<code>/`; run, screenshot, run
again for the next moment):

```js
await (async()=>{const v=document.querySelector('video');if(!v)return 'no video yet - wait and retry';v.muted=true;
 v.style.cssText='position:fixed;inset:0;width:100vw;height:100vh;object-fit:contain;z-index:2147483647;background:#000';
 if(v.readyState<1)await new Promise(r=>{v.onloadedmetadata=r;setTimeout(r,6000)});v.pause();
 window.__f=((window.__f||0)+0.3)%1;v.currentTime=(v.duration||10)*window.__f;await new Promise(r=>setTimeout(r,800));
 return 'readyState '+v.readyState+', at '+Math.round(v.currentTime)+'s of '+Math.round(v.duration||0)+'s'})()
```
Videos do not load while the Chrome window is minimized or covered (readyState stays 0): then ask
Daniel to bring Chrome to the front for a minute, or judge from the covers.

### Match rules that worked (adapt to the product)

Posture bra (EXACT, Oct 2026):

```js
ICR.S.rx={
A:"\\bbras?\\b|bralette|brassiere|s[uü]tyen|sujetador|sost[eé]n|brasier|corpi[ñn]o|suti[ãa]|soutien|reggiseno|\\bbh\\b|biustonosz|podprsenk|melltart|sutien|бюстгальтер|лифчик|бра[- ]корр|büstqalter|حمال|ستيان|σουτι|חזי",
B:"postur|duru[sş]|dik dur|kambur|haltung|houding|осанк|corrector|corrett|correct(ing|or|ion|eur)|hunch|slouch|shoulders? back|rounded shoulder|back support|back ?pain|keyhole|front (hook|clos|buckle)|cross.?back|x.?back|s[ıi]rt|spine|scolio|skolio|joroba|chepa|corcunda|gobba|kyphos|toparlay",
NEG:"\\bbelts?\\b|brace\\b|harness|corset|faja|lumbar|knee|neck (brace|support|stretch)|pillow|insole|vibrat|sensor|smart posture|massag|exercise|workout|yoga|pilates|chiropract|physio|kemer|корсет",
SELL:"link in (bio|profile)|\\bshop|order|buy|\\bsale\\b|discount|% ?off|price|\\$|€|£|₺|₹|free shipping|shipping|delivery|\\bcod\\b|cash on|whatsapp|\\bdm\\b|comment|stok|sipari|kargo|kap[ıi]da|pedido|env[ií]o|compr|tienda|precio|заказ|доставк|цен|loja|frete|commande|livraison|bestell|versand|ordina|spedizion"};
```

Heated robe (VARIATIONS, Oct 2026) - sellers say "onesie", "hoodie blanket", "therma", "heat hug" as
often as "robe"; many captions are only "Comment NFL if you want one":

```js
ICR.S.rx={
A:"robe|onesie|hoodie blanket|blanket hoodie|wearable blanket|blanket robe|snuggie|poncho|kigurumi|bornoz|albornoz|peignoir|bademantel|accappatoio|roup[aã]o|халат|sabah[ıi]k",
B:"heat|hei(ss|ß)|warm|w[äa]rm|therm|usb|battery|cozy|cosy|ısıtmal|isitmal|beheiz|calefact|chauff|riscald|aquecid|подогрев",
NEG:"heated (vest|jacket|gloves|socks|insoles|seat|pad|mattress)|electric blanket|space heater|hand warmer",
SELL:"link in (bio|profile)|\\bshop|order|buy|\\bsale\\b|discount|% ?off|price|\\$|€|£|free shipping|shipping|delivery|whatsapp|\\bdm\\b|comment|pedido|env[ií]o|compr|tienda|precio|commande|livraison|bestell|versand|kommentier"};
```

### Quirks and fallbacks (Chrome, verified Oct 2026)

- `javascript_tool` returns at most ~1,000 characters and hides text that looks like cookies or query
  strings ("[BLOCKED: Cookie/query string data]"). Return short summaries; bulk text goes
  `ICR.out()` -> OUT tab Snippet E -> `get_page_text` (up to 50,000 characters per read).
- A `javascript_tool` call fails after ~45 s and a `browser_batch` after ~60 s, but the page keeps
  running the code. Long work always goes through `ICR.bg()` + `ICR.poll()`; a one-off call to
  Instagram while jobs run waits in the same queue, so start it without `await`, store the result in a
  global (`window.__x`) and read it a minute later. Write `await (async()=>{...})()` - a bare async
  function returns `{}`.
- A full page load of DATA, a crash or a vanished tab group wipes `window.ICR` and its in-memory
  templates and covers; the data survives in localStorage: re-paste A (never reset), B, `ICR.bg(...)`.
- A screenshot that fails with "Script injection timed out": paste Snippet W in that tab and retry; if
  it still fails, ask Daniel to bring Chrome to the front for a minute.
- A hidden or covered Chrome window keeps fetches going, images load, videos do not, and a script
  scroll does not make Instagram load more reels - use `computer` scroll for that. After 5 minutes
  hidden, Chrome lets a tab's timers wake only once a minute (requests stalled 40-60 s, three times
  slower runs) unless WebRTC is in use: Library A and Snippet W open a WebRTC loopback inside the page
  (no traffic leaves it). With it, one request every ~2 s, steady.
- Instagram's web keyword search answers some phrasings with a short account list instead of posts
  (no index for that phrase); the library records those accounts and moves on. Some return nothing.
- Works: `/api/v1/fbsearch/web/top_serp/` (15-24 posts a page, 40+ pages deep), `/api/v1/tags/web_info/`
  + `/api/v1/tags/<tag>/sections/`, `/web/search/topsearch/` (users per query),
  `/api/v1/media/<id>/info/` (reel code -> owner), `/api/v1/clips/music/` (audio page, needs the
  template tokens), and the replayed GraphQL queries `PolarisProfileReelsTabContentQuery` (12 reels with
  play counts and pins; the date comes from the media id), `..._connection` (next 12),
  `PolarisProfilePageContentQuery` (followers, bio, link) and `PolarisProfilePostsQuery` (12 posts with
  captions).
- Blocked or useless - don't spend calls: `/api/v1/users/web_profile_info/`, `/api/v1/feed/user/...`,
  `/api/v1/clips/user/`, `/api/v1/usertags/...`, `/api/v1/fbsearch/reels_serp/` (400),
  `/api/v1/fbsearch/web/keyword_typeahead/` (404); "similar accounts" (`discover/chaining`) is empty
  unless the logged-in account follows the target, and following from Daniel's account is not allowed;
  Instagram's "Not personalised" tab on web just opens the general Explore page.
- If Instagram ships a new web version and `gq` calls fail with `GQL ...` errors: run Snippet B again.
  If they still fail, print the captured variables
  (`JSON.parse(new URLSearchParams(ICR.T.PolarisProfileReelsTabContentQuery.b).get('variables'))`) and
  adapt `ICR.reels`. Last resort for numbers: open `/<handle>/reels/` in AUX and read
  `[...document.querySelectorAll('main a[href*="/reel/"]')].map(a=>a.innerText)` (rounded views).
- Pace: one request every ~2 s ran 2,000+ requests in one session with no block (Oct 2026). Keep
  `ICR.gap` at 1000 (never under 900).