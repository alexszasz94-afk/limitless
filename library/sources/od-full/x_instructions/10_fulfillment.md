# 10 — Fulfillment (suppliers and agents)

**What it is:** a system for choosing and working with the suppliers and fulfillment agents
that ship a store's orders, without losing a message, quote or promise.

- Every supplier or agent gets **one conversation log**
  (`agents/<name>/conversation.md`): every message in and out, verbatim, dated, with
  direction, newest at the bottom. A drafted message is marked
  `DRAFT, not confirmed sent` until the owner confirms they sent it.
- One **status board** (`status.md`) has one row per supplier: stage, what we're waiting
  on, next step, plus what the store needs and known facts per supplier.
- One **tracker spreadsheet** holds the same data in tables (suppliers, quotes, backlog,
  message log, key facts, to-do), so quotes can be compared by formula. Update it in the
  same step as the `.md` files.
- An AI **scheduled supplier check** runs once a day. It reads every channel (WhatsApp,
  supplier platforms, email), logs what's new and tells the owner what needs a decision.
  It never sends, replies or pays.

**Folder:** `x_systems/fulfillment/kit/` is the generic version (`README.md`,
`SETUP.md` Phase 0 → 7, `LOGGING.md`, `SUPPLIER_CHECK.md` = the scheduled check as a
template, `STATUS_TEMPLATE.md`, `CONVERSATION_TEMPLATE.md`). To set it up, read
`kit/README.md` and follow `kit/SETUP.md`. The live files it creates (`status.md`,
`agents/`, the tracker) go in `x_systems/fulfillment/`.

**Research reports** in `x_systems/fulfillment/` (sourcing for the TheXmasGlow dome
projector, Sept 2026): `alibaba_top5_2026-09-24.md`, `aliexpress_top3_2026-09-24.md`,
`dsers_search_2026-09-25.md`. The decision: fulfil
through Zendrop, chosen over CJ Dropshipping after an audit (see
`x_context/decisions.md`, 2026-09-30 and 2026-10-01). `x_research/dropshipping_sourcing_playbook.md`
is the general method.

Rules learned: no sample orders (ask for a photo or dark-room video of the real unit
instead). On Alibaba, pay only through Alibaba (Trade Assurance only covers orders paid
there). Never ship DDU to a consumer: insist on DDP, or customers get a customs bill and
charge back.

The original owner's supplier conversations (and the comparison built from them), status
board, tracker spreadsheet and supplier screenshots were removed. Only the kit and the research
are here.
