# decisions.md — what was decided, and why

Append-only, newest at the bottom. One line per decision: date, decision, reason.
A decision stands until a later line reverses it. Never delete a line; reverse it with
a new one. The reason is what stops a future agent from "improving" something that
was already decided against.

2026-09-17  TheXmasGlow box: festive green design (`box_festive_green_g2.png`), 15×15×24 cm.
            Why: Daniel wanted a bigger package than 12×12×20.
2026-09-21  PNG and MP4 shot references are allowed; they share the same r<K> sequence.
2026-09-23  RETROMYPHONE retro handset deleted. Never recreate. Why: it was a test.
2026-09-23  UBU Christmas projector renamed MERRYGLOWUSA - CHRISTMAS PROJECTOR.
2026-09-23  Every video board is generated from `board_data.json` by one template.
            Never hand-edit a board. Why: one system that can rebuild any board.
2026-09-23  Two approvals per video: all frames first, then clips. Never animate an
            unapproved frame.
2026-09-23  Each product keeps its own songs folder; the same song in two products is fine.
2026-09-24  One generation per shot, then wait for Daniel's review. Why: extra takes burn
            credits and he wants to judge each one.
2026-09-24  No sample orders from suppliers. A photo or dark-room video of the real unit
            instead.
2026-09-24  Alibaba: pay only through Alibaba (Trade Assurance only covers orders paid there).
2026-09-25  Every store gets support@<store-domain>, all read and answered in one Gmail
            ((email removed)). TheXmasGlow live 2026-09-26.
2026-09-25  Turn PayPal off on the stores once the current PayPal issue is resolved.
            Why: 8 MerryGlow PayPal orders ($899) were never collected; Daniel doesn't
            want to deal with PayPal anymore.
2026-09-27  Shared systems go in `x_systems_shared/` (only what friends may see);
            personal systems stay in `x_systems/`.
2026-09-27  Shared Systems Board: a private claude.ai artifact, read-only for friends.
            Replaces the Hetzner / Coolify / GitHub / board.merryglowusa.com setup from the
            same day, which Daniel is shutting down. Never recreate it.
2026-09-27  MerryGlowUSA LED curtains and MerryGlowUSA Christmas projector: stopped.
2026-09-27  `x_context/` created with business.md, priorities.md, decisions.md.
            Scope: AI organic dropshipping only.

2026-09-29  Product Finder: each account should show its all-time highest-viewed video,
            with product labels checked against the footage. Keep the approved tree layout.
            Why: Daniel wants reliable product comparisons without extra board sections.
2026-09-29  Product Finder: rank weak accounts using both followers and average views
            of their newest 20 videos. Why: follower count alone does not measure performance.

2026-09-30  Product Finder: exclude the accounts Daniel selected from the weakest-account
            ranking. Keep these deliberate exclusions during future research refreshes.
            Why: Daniel is narrowing the research shortlist while keeping its tree organized.

2026-09-30  Product Finder: remove both unverified accounts from the Needs access branch
            and the source list; preserve this exclusion on future refreshes.
            Why: Daniel explicitly chose to remove them from the board.

2026-09-30  Systems Board (own + partner): every card is a template, no personal data (no name,
            store/brand names, emails, ids, suppliers, money). Fulfillment added as System 7 (kit).
            Why: the board is for seeing all systems and for partners' AI to set them up for their own store.

2026-09-30  Product Finder: show only the latest product promoted by each account.
            Group by recent footage and chronology. Use the highest-viewed observed video
            within that continuous run and average its newest up to 20 videos, showing the
            real sample size. Keep account-wide followers, and flag mixed or uncertain
            products instead of blending them. This supersedes the account-wide all-time
            video selection rule. Why: accounts change products; old success can mislead.
2026-09-30  Product Finder: add a left-side Notes card matching the video boards.
            Why: Daniel wants the same familiar place for his private working notes.

2026-09-30  Product Finder Notes: place the editable card at a fixed location on the left
            of the canvas so it pans and zooms with the board; seed it with Daniel's
            supplied niche checklist. This replaces the screen-pinned Notes panel.
            Why: Daniel wants notes to occupy board space rather than follow the screen.

2026-09-30  Songs: all songs live in one folder, `x_assets/songs/`, for every product.
            Reverses 2026-09-23 ("each product keeps its own songs folder"), which was
            never applied. Why: Daniel confirmed 2026-09-30 that one folder is how it is kept.
2026-09-30  The five checks only check; nothing edits a generated board (`mark_lost.py` is a
            check now). The approval of a frame belongs to the exact frame file. Why: the
            2026-09-30 audit found the old mark_lost broke the "never hand-edit a board"
            rule and that a clip could be added on a frame nobody had approved.
2026-09-30  TheXmasGlow fulfillment: CJ Dropshipping (SKU CJYD288794304DW) for the 268 paid orders,
            not Zendrop. Pay in CJ only. Why: Daniel checked both factory videos - the product is
            exactly the same - and CJ is ~$1,030-1,050 cheaper ($2,620-2,641 vs $3,672.06).
2026-10-01  TheXmasGlow fulfillment: ZENDROP, not CJ. Reverses 2026-09-30 (CJ). Pay in Zendrop only.
            Why: Zendrop audit 10-01 - total now $3,459.86 (gap to CJ ~$770, not ~$1,050), every order
            already priced and shippable, EU tax included; CJ needed 35 lines, 34 slow lines, EU IOSS and
            phone fixes first.
2026-10-01  Systems Board retired as Daniel's own board: x_systems/systems.html became the Hooks Board
            (x_systems/hooks_board.html) - the 14 hooks + Text on screen + Upscale; Video boards,
            Folders & files, Customer support and Fulfillment cards removed (their kits stay in their
            folders). The hooks board is the one future systems get built on. The partner Systems
            Board stays as it is (frozen). Why: Daniel - the board will be replaced by a full business
            dashboard; partners still benefit from the shared board.
2026-10-01  Hooks Board files live together in x_systems/hooks/: hooks_board.html and upscale_prompt.txt
            moved in next to text_on_screen.txt, assets/ and thumbs/. Why: Daniel - keep everything organized.

2026-10-01  Product Finder: split the existing canvas into Real UGC products and Other products,
            keeping the product / variation / account organization within each section.
            Why: Daniel wants a clear place for real UGC examples among existing and new products.
            Working classification uses natural person-led demonstrations, try-ons, unboxings or
            product use; mixed or uncertain footage stays in Other products. It does not certify
            customer authorship or original footage. The latest-product-per-account policy remains.

2026-10-02  Skills live in x_skills/<name>/SKILL.md, found through the Skills section of CLAUDE.md /
            AGENTS.md, not in .claude/skills/. Why: Daniel - Claude can write x_skills/ from any session
            (remote sessions are blocked from .claude/), and Claude Code will only be used inside this
            folder. Revisit once he starts working in Claude Code.

2026-10-02  Hooks Board: the Upscale section is removed and x_systems/hooks/upscale_prompt.txt deleted;
            the board is the hooks + Text on screen. Why: Daniel.
2026-10-02  ideas.txt is gone, replaced by guides.txt at the root - private, like notes.txt (see
            Private files in CLAUDE.md). Why: Daniel.

2026-10-05  Product Finder imports move from ChatGPT to Claude: the procedure is the skill
            x_skills/product-finder-import, the permanent build path is
            x_systems/video_boards/tools/product_finder.py (rank, links.txt, board, checks, Apify runs).
            Same rules as before (latest product run, one card per account, dated batches, never restore
            removals). Why: Daniel - the old generator lived in AppData\Local\Temp and could vanish.
2026-10-05  Claude may use the Apify keys in keys.txt, only through product_finder.py, never printed;
            the rest of keys.txt stays private. WhatsApp (a product-hunting group) is read through the
            Chrome extension. Why: Daniel.
2026-10-05  x_skills/ deleted. Skills live only in Daniel's Claude account (product-finder-import,
            instagram-competitor-research), changed through the skill-proposal card. Why: Daniel - the
            folder only duplicated the account copies.

2026-10-05  Product Finder: the Real UGC products / Other products split is removed. The board is one
            tree again: category -> product -> variation -> accounts (contentSection, ugcReview and
            ugcPolicy dropped from the data; the old split is kept in
            raw/research/update_oct05_relabel_review.json). Every account was re-labelled from its
            footage: the same physical product always sits in one product and one variation (designs,
            fandoms, niches and seasons are variations), and a new category Health & beauty holds the
            body-care products. Why: Daniel - AI and real UGC footage can no longer be told apart, and
            labels had drifted (e.g. @thevareny and @backalign.official sell the same posture bra).
2026-10-05  Shared systems: the Product Finder is the only shared system, and Daniel shares it with
            his competitors too, not only partners. The Systems Board and the MerryGlowUSA projector
            video board artifacts were deleted (links dead, not restorable); their local copies went
            to to_delete/x_systems_shared_2026_10_05/. Why: Daniel - he wants the Product Finder to be
            the only thing shared for now.
2026-10-05  The customer support system is shared with partners: the kit (x_systems/customer_support/kit/)
            is published as its own read-only artifact "Customer Support System", copy in
            x_systems_shared/customer_support/, built by build_shared_card.py. The Product Finder is no
            longer the only shared system. Why: Daniel - technical call with a partner; the partner's AI
            must be able to implement the whole system from the page ("Copy the full kit").

2026-10-05  SWANLIFT - POSTURE CORRECTOR BRA board uses a new columns layout of the board kit ("layout": "columns",
            x_systems/video_boards/SYSTEM.md §2.6): one column per Genjutsu motion-transfer run, rows 1 reference
            reel / 2 new woman + room / 3 final video, plus the prompts drawer. Each run's references are approved
            before anything is generated (stage "refs"). Same data file, tools and review lines as every board.
            Why: Daniel - see each reference next to its new character and room, and later its result, and
            review faster.

2026-10-05  New system: Distribution - x_systems/distribution/, the posting portal (Next.js) ported from
            an earlier project: one private daily checklist per poster, /admin for Daniel.
            Restyled in the blue palette (#0E1014 tile, #4D8DFF glow). Built and checked locally first;
            GitHub + Hetzner only once the local version is right. The day-by-day steps, posts per day and
            personas are still to be decided (placeholders in config/). Why: Daniel - posting ~50 videos a day
            needs a team of posters and one system that tells each of them exactly what to do.

2026-10-05  New GitHub account <github-account> ((email removed)) for the business; the old
            <old-github-account> account (repos posting-portal, social-tracker) is left as it is. Distribution
            code lives in the private repo <github-account>/distribution. Why: Daniel - start clean under the
            business name before deploying Distribution to a new Hetzner account.

2026-10-05  Distribution portal goes live on a new Hetzner account: server <server-name>, CX23 (2 vCPU,
            4 GB, 40 GB), Falkenstein, Ubuntu 24.04, daily Hetzner backups, firewall with only 22/80/443
            open; about $10.15/month incl. VAT. Plain Docker Compose + Caddy, no control panel; the
            server pulls new commits from GitHub every 2 minutes. Why: Daniel - cheapest option that
            works; deep research ruled out Coolify/Dokploy (2026 security record, SQLite/video risks).
            Address for now https://distribution.<server-ip>.nip.io (sslip.io is blocked by Daniel's ISP);
            a real domain before posters start.
2026-10-06  WBW posture corrector bra renamed SWANLIFT - POSTURE CORRECTOR BRA. Why: Daniel found the brand name
            (swanlift). Board key stays wbw_posture_corrector_bra so saved board notes/review marks are kept.
2026-10-06  SWANLIFT: content/upscaled_videos/video_N.mp4 holds one ByteDance upscale (Pro, 2K, 30fps, AIGC) per finished
            video. Why: Daniel asked for it; NAMING.md section 2 and check_naming.py now allow the folder. Source + job are in each prompts.md.
2026-10-06  Distribution goes real with SWANLIFT (poster: Poster 1). Schedule for every persona: day 1
            accounts + privacy + warm-up, day 2 warm-up + profiles, days 3-4 warm-up + 3 reels, from day 5 on
            5 reels a day. Platforms: Instagram, TikTok, Facebook only (YouTube Shorts dropped). Handle
            swanliftofficial everywhere, bio "The bra that fixes your posture 🦢", no pinned comment, the same
            video and caption on all platforms, warm-up accounts = the posture-bra stores on the Product Finder.
            Why: Daniel's call.
2026-10-06  Distribution: day 1 no longer has the privacy lockdown step (accounts + warm-up only), and the
            one-day-per-calendar-day lock is off - a finished day offers the next one right away. Why: Daniel,
            on momentum days he may do the posting many times in one day.
2026-10-06  Distribution, Swanlift: videos post newest first (video_16 down to video_3), and every day from day 3
            has 3 reels (no step up to 5). Why: Daniel - start at 3 a day and raise it based on performance.

2026-10-06  New system: Social Tracker - x_systems/social_tracker/, tracking every product's accounts
            (views, views gained per day, followers, every post, every Distribution video) from public
            data via Apify. Runs on a server (the Distribution server, next to the portal), not as an
            artifact: it needs an hourly scheduler, the Apify keys and a growing database, which an
            artifact cannot hold. Same blue palette and deploy pattern as Distribution (private repo
            <github-account>/social_tracker, push to main deploys). First product Swanlift (swanlift.official,
            swan.lift, SwanLiftOfficial), no YouTube. Shopify stats later, not now. Why: Daniel.
2026-10-06  Social Tracker uses the Apify keys in keys.txt (the same ones the Product Finder uses) with a
            hard ceiling of $400 a month for the tracker's own spend. Why: Daniel's call.
2026-10-06  Social Tracker reads Instagram numbers from the live profile-reels scraper (profile crawl),
            not the by-URL scrapers: those return cached counts hours old (live test: 374 for over an
            hour while the reel had 828, then 890). Instagram views = Instagram plays only, never the
            Facebook plays some scrapers add for reels shared to Facebook. Why: correct numbers.
2026-10-06  Distribution's Caddy is shared: it imports /srv/caddy-sites/*.caddy and joins the Docker
            network edge, so other apps on the server (the Social Tracker) get HTTPS from it. Why: one
            server, one front door, no second Caddy fighting for ports 80/443.
2026-10-06  Product picks are ranked on video performance only: average views of the last 20 videos (posts at least
            12 h old), the median video, this week's trend and selling season left. No score for AI-video fit or for
            how many stores sell a product. Why: Daniel - his AI video model can run any product, and he can make
            new niches and concepts, so competition is not a problem.
2026-10-06  TheXmasGlow Christmas projector: Daniel stopped running it. The whole product folder (board,
            prompts, exports, competition) goes to a partner who sells the same product, as
            `x_systems_shared/THEXMASGLOW - CHRISTMAS PROJECTOR SHARED/`, without keys, passwords or
            Daniel's private notes. Why: Daniel no longer runs the product and doesn't mind sharing it.
