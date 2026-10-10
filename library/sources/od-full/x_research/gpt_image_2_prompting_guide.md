# GPT Image 2 — Complete Prompting Guide & Research Report

**Model:** `gpt-image-2` (snapshot `gpt-image-2-2026-04-21`)
**Compiled:** 10 September 2026
**Scope:** Exhaustive reference + practitioner playbook. General-purpose — not tuned to any single vertical.
**Ends with:** A general-purpose prompt structure (Part 15).

---

## How to read this document

This report has two halves that serve different needs.

Parts 1–4 are the **reference layer**: what the model is, what the API will and won't accept, what the official prompting doctrine actually says, and where the documentation contradicts itself. Read these once; come back to them when something breaks.

Parts 5–13 are the **playbook layer**: how to actually write prompts, what the community has found breaks in practice, and how to debug a bad output. Part 14 records sourcing and confidence. Part 15 is the prompt structure itself — the thing to keep on screen while you work.

**On sourcing.** Everything here is marked for confidence. Claims drawn from OpenAI's own documentation are cited to the specific page. Claims from third-party vendors are timestamped, because several of them have already gone stale. Claims from practitioner forums are attributed to the person who made them and labelled with how many independent people reported the same thing. Where two sources disagree, both are reported and neither is averaged — a merged claim is a fabricated claim.

---

# PART 1 — What GPT Image 2 actually is

## 1.1 Identity and lineage

GPT Image 2 was released on **21 April 2026**. Its API model ID is `gpt-image-2`, which is an alias pinned to the snapshot `gpt-image-2-2026-04-21`. At the time of writing there is only one snapshot behind that alias, so the alias and the snapshot are effectively the same thing.

The model is autoregressive rather than diffusion-based, and it incorporates a reasoning step into generation — which is the mechanical reason it is slower than diffusion models and also the reason it handles world knowledge, in-image text, and multi-part instructions considerably better than they do.

The family tree matters, because a great deal of the advice circulating online is about the wrong member of it:

| Model | Status | Notes |
|---|---|---|
| `gpt-image-1` | Superseded | The origin of the "yellow cast" and over-sharpening reputation |
| `gpt-image-1.5` | Superseded, deprecated | Exposed as `chatgpt-image-latest`; fixed the warm cast and premature cropping |
| `gpt-image-2` | **Current, this document** | Released 2026-04-21 |
| `gpt-image-2.5-flare` | Newer sibling | Released 2026-09-08. Speed-oriented |
| `gpt-image-2.5-sunburst` | Newer sibling | Released 2026-09-08. Quality/precision-oriented |

Two traps follow from that table, and both of them catch people constantly.

**Trap one: `chatgpt-image-latest` is not GPT Image 2.** It resolves to the gpt-image-1.5 family and is deprecated. Several forum threads compare "Image 2" unfavourably against "Image Latest" — those are 2-vs-1.5 comparisons, not 2-vs-2.5, and they are not evidence that GPT Image 2 regressed.

**Trap two: the live OpenAI prompting guide has moved on.** As of September 2026 the page at `developers.openai.com/api/docs/guides/image-prompting` is titled *"GPT Image 2.5 prompting guide"* and is written around the 2.5 models, with a tab selector for 2.5 / 2 / 1.5 / 1. Its parameter tables list `xhigh` and `max` quality tiers **that GPT Image 2 does not have**. If you read that page casually you will come away believing GPT Image 2 supports things it does not. The OpenAI Cookbook prompting guide, by contrast, is still gpt-image-2-centric and is the better primary source for this model.

## 1.2 What it is genuinely good at

Drawing on OpenAI's own use-case gallery and corroborating practitioner reports, the model's real strengths are: rendering legible text inside images (the single biggest advance over the 1.x line); using world knowledge to fill in specifics you didn't state — give it "Bethel, New York, August 1969" and it will produce Woodstock; following long, structured, multi-clause instructions without collapsing them; compositing multiple reference images into one coherent scene; and producing multi-panel layouts where the same person stays the same person across panels, which the 1.x models could not do reliably.

## 1.3 What it is not good at — stated by OpenAI

OpenAI documents these limitations directly. Latency can reach **up to two minutes** for complex prompts. Text placement and clarity remain imperfect even though legibility improved. Character and brand consistency drifts across generations. And precise element placement in layout-sensitive compositions is difficult — you can tell it *what* to include far more reliably than *where* to put it.

To that official list, the practitioner record adds a fourth that is arguably more important than any of them, covered in depth in Part 8: **the model optimises for looking coherent over being correct**, and no amount of additional prompting overrides that.

---

# PART 2 — The mechanical layer

Prompting does not happen in a vacuum. A large fraction of "the model ignored my prompt" reports are actually parameter problems, size-constraint violations, or the wrong API surface. This part is the substrate.

## 2.1 Two API surfaces, and they behave differently

**The Images API** — `POST /v1/images/generations` and `POST /v1/images/edits`, reached via `client.images.generate()` and `client.images.edit()`. Your prompt goes to the model **verbatim**. What you write is what it sees.

**The Responses API hosted `image_generation` tool** — the model is called as a tool from inside a conversation. This surface performs **automatic prompt rewriting**. Your prompt is rephrased before it reaches the image model, and the rewritten version comes back to you in a `revised_prompt` field. It supports `action` (`auto` / `generate` / `edit`), multi-turn continuation via `previous_response_id`, and `input_image_mask`.

This distinction is strategically important and under-appreciated. If you have spent effort crafting an exact prompt — precise text strings, a careful preserve-list, deliberate word order — the Responses API may undo that work before the model ever sees it. **For controlled, repeatable, prompt-engineered output, use the raw Images API.** For conversational, iterative, "make it more autumnal" work where you want an assistant to interpret intent, the Responses API is the better fit.

Two additional gotchas on the Responses surface: the tool's `model` parameter **defaults to `gpt-image-1`**, not GPT Image 2 — an easy and expensive mistake, since you can burn a whole session on the old model without noticing. And `revised_prompt` is absent from the published output schema in the API reference even though it is returned, so don't be surprised when your typed client doesn't know about it.

## 2.2 Parameters

| Parameter | Values for `gpt-image-2` | Notes |
|---|---|---|
| `model` | `gpt-image-2` | Explicitly set it. Never rely on defaults |
| `prompt` | string, **reported max 32,000 characters** | Widely cited; see §2.3 — and note it is not an invitation |
| `n` | integer | Multiple variants in one call; cheaper than N calls |
| `size` | `auto`, presets, or custom | Constraints in §2.4 |
| `quality` | `auto` (default) \| `low` \| `medium` \| `high` | **`xhigh` and `max` are 2.5-only** |
| `background` | `auto` \| `transparent` \| `opaque` | Transparent is **preview** on this model, enabled 2026-08-20. See Part 7 |
| `output_format` | `png` \| `jpeg` \| `webp` | Transparency requires PNG or WebP |
| `output_compression` | 0–100 | JPEG/WebP only |
| `moderation` | `auto` \| `low` | `low` does **not** disable output-stage moderation. See §9.3 |
| `stream` | boolean | Partial-image streaming |
| `partial_images` | 0–3 (docs also say 1–3 elsewhere) | Contradiction flagged in Part 4 |
| `input_fidelity` | **Omit it.** | See §2.5 — this is a live trap |
| `mask` | RGBA PNG | Same format and dimensions as source, <50 MB. See Part 8 |

## 2.3 The prompt-length ceiling is not a target

GPT image models are widely reported to accept prompts up to 32,000 characters. (Flagging honestly: that figure could not be confirmed in either of the two primary OpenAI prompting documents consulted for this report — treat it as ecosystem consensus rather than a quoted spec.) Either way, it is not permission to write 32,000 characters. OpenAI's own guidance is explicit that overloading a single prompt degrades results, and the practitioner evidence in Part 8 is emphatic: escalating prompt length and constraint count past a certain point does not improve adherence, and in edit workflows it actively makes things worse. Treat a few hundred to a couple of thousand characters as the productive working range for a single generation, and reach for iteration rather than length when a prompt isn't landing.

## 2.4 Size constraints — the hard rules

These are the best-corroborated numbers in the whole document — OpenAI's Cookbook, OpenAI's live guide, a community-maintained validation library, and an independently written forum post all state substantively the same rules:

- Each edge must be **no more than 3,840 pixels**
- Both edges must be **multiples of 16 pixels**
- The ratio of longer edge to shorter edge must **not exceed 3:1**
- Total pixel count must be between **655,360 and 8,294,400**

**One genuine ambiguity, in OpenAI's own documentation.** The live guide says "no more than 3,840." The Cookbook says maximum edge length must be **less than** `3840px` — a strict inequality — and then, in the same document, lists `3840x2160` as a popular size while separately advising: *"If the max-edge rule is enforced literally as `< 3840`, round down to the nearest valid size such as `3824x2144`."* If you are working at the very top of the range and getting rejections, that is why. `3824x2144` is the safe answer.

Anything above 2560×1440 is documented as experimental. Reported working aspect ratios span 1:1, 4:3, 3:4, 3:2, 2:3, 16:9, 9:16, 2:1, 1:2, 21:9, 9:21, 3:1 and 1:3 — but a well-regarded forum contributor's practical advice is to **stay under 2:1 where possible**, on the reasoning that extreme ratios sit outside the bulk of the training distribution and quality suffers before the hard 3:1 limit bites.

There is an unresolved conflict on defaults: one vendor guide states the default resolution is 2K; a community CLI wrapper encodes `1024x1024`. Both are reported here; neither is confirmed. **Set `size` explicitly and the question disappears.**

## 2.5 `input_fidelity` — a documentation trap

OpenAI's own model table states that `input_fidelity` is **Disabled** for `gpt-image-2`, with the explanation that it "does not work for this model because output is already high fidelity by default." The live prompting guide says it plainly: *"For `gpt-image-2`, omit `input_fidelity`; image inputs are always processed at high fidelity."*

And yet **OpenAI's own Cookbook passes `input_fidelity="high"` to `gpt-image-2` in four of its editing examples.** And OpenAI's API reference describes the parameter as supported for "`gpt-image-1` and `gpt-image-1.5` and later models" — which reads as *including* GPT Image 2. That is three first-party statements pointing in two directions. Azure's documentation of the same model indicates that sending the parameter causes the request to fail.

This is an unresolved internal contradiction in first-party documentation. The safe reading — and the one this guide recommends — is to **omit the parameter entirely**. You lose nothing, because high fidelity is already the default behaviour, and you avoid a possible hard failure. If you are copying code from the Cookbook, strip this line.

## 2.6 Pricing and provenance

Pricing is token-based: **$8 per 1M image input tokens**, **$2 per 1M cached image input tokens**, **$30 per 1M image output tokens**, and **$5 per 1M text input tokens**. (Figures as read from OpenAI's pricing page during this research; verify against the live page before budgeting, since pricing moves.) The practical consequence is that `n=4` in one call is meaningfully cheaper than four separate calls, since text input is billed once.

Every output carries **C2PA Content Credentials** metadata and a **SynthID-variant watermark embedded in the image surface itself**. A provenance-check endpoint exists at `POST /v1/content_provenance_checks`.

The watermark has a consequence that catches people out: if you composite a transparent GPT Image 2 asset into hand-made artwork, the watermark travels with it and the **entire composite** can be flagged as AI-generated. This matters for any workflow where AI assets are one layer among many.

---

# PART 3 — The official prompting doctrine

Two official documents matter, and they organise the same underlying advice differently.

## 3.1 The Cookbook's eleven fundamentals

From OpenAI's *GPT Image Generation Models Prompting Guide* (Cookbook, 21 April 2026), the model-specific source of truth for GPT Image 2. Its eleven headings, with the operative content:

**1. Structure + goal.** Verbatim: *"Write prompts in a consistent order (background/scene → subject → key details → constraints) and include the intended use (ad, UI mock, infographic) to set the 'mode' and level of polish."* Two ideas are bundled here and both are load-bearing. The consistent ordering gives you a repeatable template — which matters more than the specific order chosen. And stating the **intended use** is a genuine shortcut: "for a UI mockup" or "for a magazine advertisement" pulls in a whole cluster of conventions about polish, framing, and typography that you would otherwise have to spell out clause by clause.

**2. Prompt format.** Structured, readable prose. Sections or short labelled lines outperform a single undifferentiated block.

**3. Specificity + quality cues.** Concrete detail beats adjectives. For photorealism, verbatim: *"include the word 'photorealistic' directly in the prompt to strongly engage the model's photorealistic mode."* This is one of the few genuine magic words in the model.

**4. Latency vs fidelity.** `quality` is a real dial, not a cosmetic one. Draft at `low` or `medium`, finalise at `high`. OpenAI's own position on `low` is notably positive — the Cookbook describes it as "especially strong" and says it "works just as well" for many cases. *(Practitioner counterpoint, not OpenAI's view: several API users independently report `low` degrading over the course of 2026 to the point where they treat `medium` as the practical floor for anything containing human anatomy. Their words, not the vendor's — but worth a test before you commit a pipeline to `low`.)*

**5. Composition.** State camera framing, angle, and shot type explicitly. The model responds well to photographic vocabulary — focal length, depth of field, shot distance — and poorly to vague spatial language.

**6. People, pose, and action.** Describe pose and action concretely rather than naming an emotion and hoping. See §8.6 for the left/right failure mode that ambushes anyone doing this seriously.

**7. Constraints — what to change vs preserve.** Verbatim: *"For edits, use 'change only X' + 'keep everything else the same,' and repeat the preserve list on each iteration to reduce drift."* This is the official position. **Part 8 documents extensive practitioner evidence that it does not work as reliably as stated**, and offers a better-supported alternative.

**8. Transparent backgrounds.** Request explicitly; use PNG or WebP. See Part 7, which has grown considerably more complicated than this heading suggests.

**9. Text in images.** Verbatim: *"Put literal text in quotes or ALL CAPS ... For tricky words (brand names, uncommon spellings), spell them out letter-by-letter."*

**10. Multi-image inputs.** Verbatim: *"Reference each input by index and description ('Image 1: product photo… Image 2: style reference…')."* Without indexing, the model decides for itself what role each image plays, and it decides badly.

**11. Iterate instead of overloading.** The most under-followed rule in the list. One change per turn beats one enormous prompt.

## 3.2 The live guide's eight fundamentals

The `developers.openai.com` prompting guide — now written around 2.5, but its fundamentals are model-agnostic — restructures the same doctrine into eight: define the result; choose a maintainable format; describe visible details; specify people and actions; specify exact text; separate changes from constraints; assign roles to references; iterate deliberately.

The two documents agree substantively. Where the live guide adds value is in framing: **"describe visible details"** is a sharper instruction than "be specific," because it tells you the test to apply. If a detail would not be visible in the final image, it is not earning its place in the prompt. Backstory, mood-as-abstraction, and intent-that-isn't-visual are all prompt weight with no output effect.

**"Choose a maintainable format"** is likewise a better argument for structure than "prompts should be structured." A prompt you will edit twenty times should be laid out so that you can find and change one thing without rewriting the whole.

## 3.3 The official checklist

The live guide closes with a four-point verification pass. Check that any text and labels are accurate. Check that identities, product shapes, labels, and reference details survived intact. Check that an edit changed **only** what you asked it to change. And if you needed transparency, check that the file actually contains a real alpha channel rather than a painted-on white or checkerboard background.

Ordinary as a list, but the discipline of actually running it is what separates people who converge in three iterations from people who churn for twenty. Note how much of it is about *unintended* change — that emphasis is not accidental, and Part 8 explains why.

---

# PART 4 — Documentation contradictions and known traps

Collected in one place, because each of these has cost someone a debugging session.

**`input_fidelity`.** Model table says Disabled for gpt-image-2. Live guide says omit it. Cookbook code examples pass it anyway, four times. The API reference describes it as supported for "gpt-image-1.5 and later models." Azure says sending it fails. **Resolution: omit it.**

**Maximum edge length: `≤ 3840` or `< 3840`?** The live guide says "no more than 3,840." The Cookbook says "less than `3840px`" while elsewhere listing `3840x2160` as a popular size and advising a round-down to `3824x2144` if the rule is enforced strictly. Use `3824x2144` at the top of the range.

**`partial_images` range.** Documented as 0–3 in one place and 1–3 in another.

**Streaming support.** The model page states "Streaming: Not supported" while the streaming parameters are documented for the model elsewhere.

**Quality enum drift.** `xhigh` and `max` appear in tables on the shared prompting-guide page. They belong to 2.5. GPT Image 2 has `low` / `medium` / `high` only.

**`revised_prompt` undocumented.** Returned by the Responses API image tool; absent from the reference output schema.

**Responses-tool model default.** Defaults to `gpt-image-1`. Set it explicitly.

**Transparency: documentation and observed behaviour disagree on timing.** OpenAI's Cookbook has documented transparency as available in preview for `gpt-image-2` since its 21 April 2026 publication. Yet three separate third-party guides published between April and August 2026 state flatly that transparency is unsupported, and API users reported the parameter being **refused** until an announcement on **20 August 2026** that it was "now available in preview." The most likely reading is a staged rollout — documented early, enabled generally later — but this guide cannot resolve it definitively. Practical consequence: **it works now**, and any third-party statement to the contrary is stale regardless of which date you believe.

**One popular GitHub prompt collection carries gpt-image-1-era parameters** (`quality: standard | high`, which is not the GPT Image 2 enum). Use community prompt libraries for prompt *text*; never for parameter guidance.

---

# PART 5 — Deep dive: writing the generation prompt

## 5.1 Order and why it works

The recommended ordering is **background/scene → subject → key details → constraints**, and it is worth understanding why rather than just following it.

An autoregressive image model builds an output conditioned on everything it has read. Establishing the scene first gives every later clause a context to attach to: "wearing a heavy wool coat" resolves differently after "a February street in Reykjavík" than it does in a vacuum. Putting the subject second means the subject is described into an already-established world rather than floating. Details third refine what already exists. Constraints last are the model's final adjustment before it commits.

The stronger argument, though, is consistency rather than optimality. Because you will iterate, a fixed slot order means you always know which line to edit. A prompt whose structure changes every revision cannot be debugged.

## 5.2 State the intended use

This is the highest-leverage single clause available and it is routinely omitted. "For a print magazine advertisement," "as a UI mockup," "as an editorial photograph," "as a children's book illustration," "as a technical infographic" — each of these pulls in an entire cluster of conventions: typical framing, typographic treatment, level of finish, colour handling, negative-space budget.

Without it, the model picks a mode from whatever cues it can find in the rest of your prompt, and its default mode tends toward generic stock-image polish.

## 5.3 Describe visible things

The test: **would this appear in the frame?** If not, cut it.

Backstory ("she has just received bad news") only works to the degree it implies visible posture and expression, and you will get a more reliable result by describing the posture and expression directly. Abstract mood words ("ethereal," "powerful," "premium") are the weakest tokens in a prompt — they mean different things in different training contexts and the model averages them into blandness.

The substitution discipline that vendor guides converge on is to replace every aesthetic adjective with a physical or photographic specification. "Beautiful lighting" becomes "low sun from camera left, long shadows, warm rim light on the subject's right cheek." "Premium look" becomes "matte black surface, shallow depth of field, single softbox at 45 degrees, seamless dark grey backdrop." The prompt gets longer and the output gets dramatically more controlled.

## 5.4 Specificity, and the point where it stops helping

Concrete beats vague, up to a point. Part 8 documents that point in detail: past a certain density of specification, additional detail stops improving adherence and starts competing with itself. The model resolves competing constraints by favouring overall visual coherence, which means the constraint you cared about most may be the one it drops.

The practical guidance: specify the two to four things that must be right, in detail. Leave the rest for the model. Then iterate on whatever came out wrong. Trying to nail everything in one pass is the single most common cause of the twenty-iteration death spiral.

## 5.5 Photorealism

Include the literal word **"photorealistic"** — OpenAI states this engages a distinct mode in the model, and it is one of the few keyword effects the vendor documents directly.

Layer photographic vocabulary on top of it: camera position and height, lens character or focal length, depth of field, light sources with direction and quality, surface materials, time of day, weather. The model has strong priors for all of these.

A caution: the model is documented as producing **plastic-looking, over-smoothed skin in editing workflows** (§8.7). "Photorealistic" helps in generation. It does not reliably fix that particular problem in edits.

## 5.6 Composition and camera

Camera framing is one of the areas where the model responds best to being told exactly what you want. Shot distance (extreme close-up through wide establishing), camera height (ground level, eye level, high angle, overhead), lens behaviour (wide-angle distortion, compressed telephoto), and focal plane all land reliably.

Precise **placement**, by contrast, is documented by OpenAI as a weakness. "A red mug in the lower-left third, exactly 200 px from the edge" will not be honoured as a measurement. If your layout is genuinely precision-critical, the right move is to generate the elements and compose them yourself, or to supply a layout reference image — not to escalate the prompt.

## 5.7 People, pose and action

Describe the body, not the feeling. "Shoulders squared to camera, weight on the back foot, chin slightly lowered, arms loose at the sides" produces a controlled result. "Confident" produces the model's average of confidence.

For anything involving limb-specific instructions, read §8.6 first — the anatomical left/right failure mode is a genuine landmine.

## 5.8 Iterate rather than overload

Both official documents say this and it is the rule most often broken. Change one thing per turn. Re-read the output against your intent before writing the next prompt. When something is wrong, the correct question is "what single clause fixes this?" not "what can I add?"

The evidence in Part 8 for this is unusually strong: three independent practitioners, working in completely different domains, escalated their prompts through four or five increasingly elaborate versions and got **identical failures every time**. Escalation is not a strategy.

---

# PART 6 — Deep dive: text in images

Text rendering is GPT Image 2's headline improvement over the 1.x line, and notably, it is the area where community complaints have largely **stopped**. Extensive searching turned up no first-person reports of systematic text-rendering failure with this model — a meaningful negative finding.

That said, OpenAI itself still lists text placement and clarity as a standing limitation, and dense typography remains a genuine weak point. The accurate statement is: **legibility is largely solved; placement and density are not.**

The technique, per OpenAI:

**Put literal strings in quotation marks or ALL CAPS.** This marks them unambiguously as text-to-render rather than description-to-interpret. Without the marker, "a sign saying open" may produce a sign that communicates openness rather than one that says OPEN.

**Spell out difficult words letter by letter.** Brand names, invented words, unusual spellings, anything the model has weak priors for. `"LUMORA" — L, U, M, O, R, A` is a real technique, not a superstition.

**State placement and typographic treatment.** Where on the image, at what size relative to other elements, in what weight and style. The model handles this well for a small number of text elements and degrades as the count rises.

**Keep the total volume of text low per generation.** Dense typography — a full page of body copy, a complex chart with many labels — remains where placement and clarity break down, which is exactly what OpenAI's stated limitation predicts.

**One unverified lead worth knowing about.** A technique circulating under the name "underdrawings" proposes rendering text and numbers *deterministically* first — via SVG, a plotting library, or a diagram tool — exporting that as an image, and then passing it to the image model as a base layer to paint over. The logic is sound: it moves the one thing generative models are unreliable at into a system that is exact. **However, the published demonstration was done on a different vendor's model, not GPT Image 2, and this guide has not verified it here.** Treat it as a promising experiment rather than an established technique.

---

# PART 7 — Deep dive: transparency

This section is longer than the official documentation implies it needs to be, because transparency on GPT Image 2 turns out to have a genuinely surprising behaviour.

## 7.1 Status

`background: "transparent"` is **available in preview for `gpt-image-2`**. It works today.

The history is murkier than it should be, and it is worth knowing about because it explains why the internet contradicts itself here. OpenAI's Cookbook has documented transparency preview for this model since 21 April 2026. But three separate third-party guides published between April and August state that transparency is unsupported, and API users reported the parameter being refused, until an OpenAI announcement on **20 August 2026** that it was "now available in preview." Most likely a staged rollout — documented before it was generally enabled. This guide cannot resolve it definitively, and it does not much matter now, except as a reason to distrust undated third-party claims about this model.

Transparency requires `output_format` of `png` or `webp`. JPEG has no alpha channel.

## 7.2 The surprise: transparency changes the rendering style

A controlled test posted to the OpenAI developer forum in August 2026 held everything constant — same prompt, same model, `quality="low"`, `output_format="png"`, `size="1024x1024"` — and varied only the `background` parameter. The result, verbatim:

> - WITHOUT the parameter: smooth stylized 3D cartoon rendering, which is what the prompt asks for
> - WITH the parameter: noticeably more photorealistic output — skin texture, finer detail, less stylization

And critically: *"The prompt wording makes no difference … The control run (original prompt, no parameter) reliably produced the cartoon style again, so this isn't run-to-run variance."*

The best available explanation, from another forum contributor:

> `background="transparent"` is not best thought of as "generate the same image, then delete the background." It is a generation condition. Asking for transparency can influence the whole image because the model has to render the subject without a normal scene/background context.

Dimensions reported as affected: lighting and shadows, edge treatment and antialiasing, object silhouette, composition and framing, a "sticker/cutout/product-render appearance," and perceived style or realism. The effect direction is also endpoint-dependent — reported as a regression on `/images/edits` and an improvement on `/images/generations`.

**Practical consequence:** if you have dialled in a style and then switch on transparency, expect the style to move. Re-tune after enabling it, not before. If the shift is unwanted, counter it in the prompt — the mitigation pattern reported as working is to restate the style you want alongside the transparency request and explicitly negate the cutout look:

> *"Photorealistic product photo of X, natural studio lighting, realistic material texture, transparent background, no sticker style, no cartoon edges, no drop shadow."*

## 7.3 Two known bugs in preview transparency

**The opaque areas are not fully opaque.** Independent measurement of returned PNGs found alpha values of **252–254 out of 255** in regions that should be solid, with 253 most common. For most uses this is invisible. For compositing against high-contrast backgrounds it is not — extremes of black and white will bleed through. **If you are compositing, normalise or clip the alpha channel before use.**

**A grey halo.** A thin grey border appears at the transparency boundary — the RGB data behind the alpha edge contains a grey fringe wider than the alpha channel itself, a colour-key artifact. The mitigation is a halo-removal pass that erodes or expands existing alpha, of the kind standard in compositing tools.

## 7.4 The watermark caveat, again

Because the SynthID-variant watermark is embedded in the image surface rather than in metadata, a transparent asset dropped into a larger composition carries it along and can cause the whole composite to register as AI-generated. Worth knowing before it becomes a surprise.

---

# PART 8 — Deep dive: editing, masks, and the preservation problem

This is the most important part of the document, because it is where the official guidance and the practitioner record diverge most sharply — and where the practitioner record is better supported.

## 8.1 The foundational fact: there is no partial edit

The single most consequential sentence found in the entire research corpus, from a highly-regarded contributor on the OpenAI developer forum:

> The entire image must be regenerated as a new output with gpt-image models. You cannot have perfect preservation - and cannot avoid it being watermarked. The mask is an image prompt, and the AI model acts on that prompt, but it has agency to do what it wants.

Everything else in this part follows from that. A mask is **not** a region lock. It does not confine the model's changes to the masked area. It is a strong hint delivered as an image, and the model treats it the way it treats every other input: as something to consider, not something to obey.

Once you internalise this, a large class of frustrations becomes predictable rather than mysterious.

## 8.2 How the mask is actually seen by the model

Detailed analysis by the same contributor describes the mechanism:

> The **base `image[]`** is the current canvas as RGBA. Image/key transparency stays transparent. Loaded-image outfill transparency is also transparent, but its hidden RGB is changed to checkerboard as a hint.
> The **`mask`** is a separate RGBA PNG. Its alpha is transparent where the model should edit: user-painted mask areas plus outfill areas. Its RGB is sepia/grayscale context, with user-painted regions shown in gray.

And the conclusion:

> Mask is used in the API to "damage" the input image ... Seems OpenAI is sending the model a mask as transparency, and your transparent input doesn't work.

There is also a specific note that for `gpt-image-2` the model *"apparently receives no input transparency"* in this path — meaning if your source image already has an alpha channel that carries meaning, the mask mechanism may destroy that meaning.

## 8.3 The failure modes, as reported

From a detailed August 2026 bug report, four failure modes stated verbatim:

> 1. Changes parts of the image outside the masked area. 2. Changes objects that were not part of the requested edit. 3. Leaves parts of the masked area transparent/empty instead of preserving the original content. 4. Re-generates more of the selected region than necessary, even though I only requested a color/texture change.

The prompt that **failed** to prevent this — note how thorough it is:

> Only modify the orange cushions inside the editable area. / Change their fabric to green. / Do not modify any other object. / Keep the sofa, table, floor, walls, lighting, perspective, composition, shadows and all other elements unchanged.

That prompt is essentially a perfect execution of OpenAI's official "change only X, keep everything else the same" advice. It did not work.

## 8.4 The escalation trap, documented three times independently

This is the strongest consensus finding in the whole corpus, and it arrives from three practitioners in three unrelated domains.

**A product-photography user** ran five prompt variants against the same task — recolour a garment, preserve the face — from a one-line minimal prompt up to a fully structured production prompt with explicit task/input/expected-result/keep-consistent/scope sections. **All five failed identically.** His summary of the underlying problem, from thousands of generations since April: *"an unnatural, plastic-like layer appears over the face and other exposed skin areas."*

**A game-art user** working on sprite sheets concluded: *"the more I try I see that gpt-image-2 was not trained to follow certain details, it emphasizes overall good looks."*

**A user running a deliberate boundary test** escalated through four levels — aesthetic baseline, physics constraints, structural demands, conflicting real-world constraints — and concluded:

> Prompting can steer appearance, but it does not create underlying structure. No matter how precise the prompt becomes, the system prioritizes what looks coherent over what is physically consistent.

**The lesson is not "prompt harder."** There is a class of failure that more prompt does not fix. Recognising which class you are in — and switching to a different tool, a different workflow, or manual compositing — is worth more than another five iterations.

## 8.5 What actually works better: positive statements over negative constraints

The best-supported counter-technique in the corpus, and it inverts common practice:

> Something I've noticed is that using factual positive or neutral statements work much better for images than resorting to negatives and constraints. Use the constraints and negations only if really needed.

The failure loop this addresses is described precisely by another user:

> **Get 95% correct → attempt the final 5% → lose 30% of the previous work → rebuild → repeat.**

And the specific phrasings reported as **not working**: *"Do not change anything else."* / *"Preserve the existing image exactly."* / *"Only add this one element."* Annotated images, incremental stepping, and removing references were all also tried without success.

So: rather than *"do not change the background,"* describe the background you want as a positive fact. Rather than *"keep her expression,"* describe the expression. The model handles description far better than prohibition. Reserve negations for the two or three things you genuinely cannot tolerate.

The same contributor adds three procedural techniques: assign an explicit ID to each image within the conversation; prefer conversational editing in an ongoing chat over handing files back and forth through a library; and branch the conversation rather than continuing a degraded thread. Plus: *"always start a chat with your intention"* and assign a working persona (art director, retoucher) at the top.

## 8.6 The anatomical left/right trap

Verbatim from a practitioner doing pose work:

> Even the latest model, `gpt-image-2`, can struggle with left/right limb distinction. For example, it may interpret 'left leg' as the leg on the left side of the screen, rather than the character's actual left leg.

His advice: *"If the model consistently misinterprets left/right, it can be more effective to work with its bias rather than fight it."* In other words, if the model is reliably reading screen-left, phrase your prompt in screen-space and stop insisting on anatomical space.

Additional practical notes from the same source: *"Hallucinations still happen. Retrying the same prompt 2–3 times often fixes the issue."* *"Avoid generating a full sprite sheet all at once. Working frame by frame tends to produce better results."* And a 3D mannequin-style reference image helps substantially, because it supplies unambiguous joints, shadows, and structure.

## 8.7 Over-smoothed skin in edits

Reported consistently since launch by a user with thousands of generations behind the claim:

> With GPT Image 2, the edited images frequently produce faces that look visibly plastic, overly smooth and artificial. The face loses natural skin texture and realistic facial detail, even when the prompt explicitly requires preserving the original model and changing only the garment color.

This is dated to April launch, not to any later regression, and is described as model-specific — the older 1.5-family model reportedly produced more natural facial realism in edits. Only one strongly-documented independent voice, so it sits at moderate rather than high confidence, but it is unusually well-evidenced for a single report.

**Practical workaround:** if the face must not change, do not send the face through the edit. Crop, edit the region that needs changing, and composite the original face back. This is more work and it is also the only reliable answer.

## 8.8 Technical mitigations that do help

A six-point list from the mask-mechanism analysis, verbatim:

> Constraining input image + mask to the exact output resolution also specified; Make that exact image sent one that is supported in the 16px increments; Understand the downsizing rules automatically applied to large or upscaling to undersized input images; Do not exceed 3:1 or 1:3 ratios, and better, keep the ratios constrained to within likely training, under 2:1.; Avoid padding or unnecessary outfill hints in a mask, instead, trim up the input image by any excess to align the two dimensions within the 16px capability.; Use quality:high for the finest resolution in having the AI create the most faithful output.

There is also an alignment trick worth knowing: if the output resolution matches the input exactly, you can composite the API's output back over the original and keep only the region you wanted changed — but *"the prompt must not have any contrary instructions (such as 'zoom out')"* or the alignment breaks.

Note also that internal image patching is limited to roughly 1536 token-equivalents at fixed size increments, which is the mechanical reason very large inputs lose detail regardless of what you ask for.

## 8.9 Multi-reference blending

When several reference images are involved, the model *blends* rather than treating each as an authority:

> when several references are involved, the generator can also start blending them rather than treating them as strict technical authorities … We could get a beautiful expression from one reference, but then the identity would drift.

The mitigation is the official one and it does help: **index and role-assign every reference explicitly** — "Image 1: the character, this is the identity authority. Image 2: pose reference only, do not take identity from it. Image 3: colour palette only." Without role assignment the model assigns roles itself and blends freely.

There is an unresolved conflict on how many references are accepted: one vendor guide says **up to 4**, another says **up to 16**. Neither was confirmable against primary documentation. Both are reported here; do not assume either.

## 8.10 Session degradation — a procedural bug with a procedural fix

A well-documented issue: **image quality degrades after roughly three to five generations within a single session**, with a noise/speckle pattern accumulating. The reported fix is not a prompt change:

> **FIX**: Restart the session, load the page new.

The same session-state bug also produces the opposite symptom — **identical images from the same prompt within a session**, and in a related report, near-identical compositions across supposedly fresh chats even when the prompt explicitly said not to reference prior generations.

On the underlying noise pattern itself, the assessment is blunt:

> **NO FIX POSSIBLE**: The issue is technical and cannot be fixed with prompting! **Partial workaround:** Since details and small objects in the image, as well as complex natural surface structures trigger the effect, there is a possibility to partially remove it by reducing the image complexity.

The suggested prompt-side lever is simply **"LESS DETAILS."** A related observation: the artifact is associated with reference images and background style-searches, and *"if you do not use any reference images or previous images in the chat, it can do very high quality without any artifacts"* — though at least one other practitioner reports seeing it on first generation with a reference image, so this is not universal. A repair prompt reported as working on an already-affected image: **"Remove the noise from the image, while keeping all the lines."**

---

# PART 9 — Moderation, refusals, and why rewording often won't help

## 9.1 The asymmetry

Multiple API developers report that **moderation on the API is materially stricter than in ChatGPT** for the same content. Documented examples of prompts that were blocked on the API and generated without issue in ChatGPT include *"A woman getting ready for a party"* and *"two women whispering secrets to each other."*

The complaint as originally framed:

> Either the AI model is making bad outputs or the moderation being used on images is far more strict than what is being applied to anyone on ChatGPT, disadvantaging any API developer or product.

## 9.2 Refusals fire at the *output* stage

This is the mechanically important part. The error payload on a blocked request looks like:

```
safety_violations = [sexual]
moderation_details: {"moderation_stage": "output", "categories": ["sexual"]}
Type: image_generation_user_error
Code: moderation_blocked
```

Note `"moderation_stage": "output"`. The block is being applied to the **generated image**, not to your prompt text. Reported cases include `n=6` requested and **zero images returned**, with `"moderation": "low"` already set.

The consequence is stated bluntly by an experienced contributor:

> Refinements in prompt language won't make an image request succeed.

And the mechanism:

> It's all in the *output*. Believable photographs being output are what are killed with zero regrets.

## 9.3 What `moderation: "low"` does and doesn't do

Setting `moderation: "low"` relaxes the input-side filter. It does **not** disable the output-stage classifier. Requests will still fail after generation — meaning you can be billed for output tokens on images you never receive.

## 9.4 The one reported workaround, honestly labelled

One developer reports that prefixing prompts with **"A surrealistic image of"** and then filtering out unwanted surrealistic effects via the rest of the prompt gets otherwise-blocked requests through. The reasoning is consistent with the mechanism above: the output classifier is hardest on photorealistic human imagery, so nudging the output away from believable photography moves it out of the danger zone.

The same experienced contributor who explained the mechanism also rejects this as a general technique: *"It is not universally applicable as a technique, but a happenstance."*

**Treat it as a diagnostic rather than a solution.** If "surrealistic" unblocks your prompt, that tells you the block was photorealism-driven, which tells you the real fix is to change what you are asking for — not to keep fighting the filter.

---

# PART 10 — ChatGPT is not the API

A great deal of published "GPT Image 2 has gotten worse" content is, on examination, about ChatGPT's image pipeline rather than about the model. This distinction is worth understanding because it determines whether a problem is yours to fix.

Recurring "sudden quality collapse" threads appeared on a roughly monthly cadence from June 2026 onward — well before the 2.5 release. The decisive evidence that these are not model properties comes from a control test in September 2026: a user posted a prompt producing degraded, near-identical outputs in ChatGPT; another user ran **the identical prompt through the API against `gpt-image-2`** at `quality: medium` and `quality: high` and got good results. The degradation was in ChatGPT's routing, not the model.

A structural explanation offered by an experienced observer is that *"OpenAI seems to be running some 'simple' image maker in front of a more complex one"* — with evidence of two distinct generating paths and visible A/B model trials inside ChatGPT. OpenAI's own support response to the September wave was simply: *"Sorry about the drop in quality. We haven't confirmed a cause or fix."*

**Practical implications.** If you need repeatability, use the API. ChatGPT provides no guarantee about which pipeline handles your request. If you are benchmarking or evaluating the model, benchmark through the API or you are measuring the wrong thing. And when you read a complaint online, check whether the person was using ChatGPT or the API before you update your beliefs about the model.

One ChatGPT-side technique worth knowing, since ChatGPT rewrites prompts before dispatch. A reported anti-rewrite formula:

```
(format 1536x1024.) (don't change the prompt, send it as it is.)
```

With its author's own honest caveat: *"it could be that, in the background after ChatGPT has sent the prompt, the prompt is improved a second time if it is considered insufficient."* Partial control at best. If prompt fidelity matters, the API is the answer.

---

# PART 11 — The third-party ecosystem

## 11.1 Higgsfield

**Direct answer to the question asked: Higgsfield hosts GPT Image 2 but publishes no dedicated GPT Image 2 prompting guide.**

Higgsfield exposes the model as `gpt_image_2`, with a landing page at `higgsfield.ai/gpt-2` and CLI-style controls including `--aspect_ratio`, `--quality`, and `--resolution` at `1k` / `2k` / `4k`. What it publishes on prompting is a **generic, model-agnostic help-centre article** advising you to state subject, action, setting, lighting, and camera in one or two sentences, and to avoid vague adjectives such as "beautiful." It also offers an `/ai-prompt-generator` tool.

That generic advice is compatible with everything in this guide but adds nothing model-specific. **Confidence note: these findings come from search-engine result summaries; direct fetching of higgsfield.ai pages was blocked in this research environment.** The absence of a dedicated guide is a negative finding from repeated searching rather than an exhaustive audit of the site.

**Important correction.** An early search attributed a "five-slot framework, 100–300 words for Instant Mode, up to 500 words for Thinking Mode" to Higgsfield. That framework belongs to **fal.ai**, not Higgsfield. Search-engine result blending caused the misattribution and it is corrected here so it does not propagate.

## 11.2 fal.ai — the strongest third-party guidance found

fal.ai publishes the most substantive model-specific prompting material of any third-party host. Its scaffold is a five-slot template:

```
Scene: [what is happening, where, when]
Subject: [who/what is the focus, described concretely]
Important details: [the 2-4 things that must be right]
Use case: [what this image is for — poster, hero image, product shot]
Constraints: [what must not appear]
```

Alongside it, a set of "anti-slop" rules whose common thread is replacing aesthetic adjectives with physical specifications. This is a real contribution — the substitution discipline described in §5.3 comes from here, and it is not in OpenAI's documentation in this form.

The "important details: the 2–4 things that must be right" slot deserves particular attention. It encodes exactly the constraint budget that Part 8's evidence supports: specify a small number of things precisely, let the model handle the rest, iterate on failures.

## 11.3 Luma AI

Luma publishes "GPT Image 2: The Complete Guide" (3 June 2026), which uses the same five-slot template. Its useful original contributions are a set of adjective-to-specification substitution pairs and a candid weaknesses list: *"Brand logos are hit-or-miss"*; *"High quality at 4K can take 3+ minutes"*; *"Quality degrades in edit chains — use upscale between successive edits."*

Its stated specs include a **7,000-character prompt maximum** and **up to 4 input images**, both of which conflict with other sources (32,000 characters is the widely-cited figure elsewhere; another vendor says 16 images) and neither of which was independently confirmable. Its "Transparency: NOT supported" line is **now wrong** — see Part 7, which also covers why it may have been accurate in observed behaviour on the day it was written even though OpenAI's own Cookbook said otherwise.

A section of the Luma guide is explicitly self-attributed to the OpenAI Cookbook and adds nothing beyond it.

## 11.4 Replicate, Azure/Foundry, and resellers

Replicate and Microsoft Foundry/Azure both host the model. Their documentation is primarily mechanical rather than prompting-focused, and it is where the `input_fidelity` failure behaviour and some transparency-support disagreements surface. Because all of it predates the August transparency change, check dates.

A broad ecosystem of API resellers publishes latency figures and artifact analyses. These are marketing-adjacent and should be discounted accordingly. The one latency claim that survives cross-checking is roughly **three minutes at high quality / 4K**, corroborated across independent sources. Note that this **exceeds** OpenAI's stated "up to two minutes for complex prompts" — most plausibly because 4K output is documented as experimental and sits outside whatever OpenAI benchmarked. Budget three minutes, not two, if you are working at that resolution.

## 11.5 GitHub prompt libraries

A community skill/validation library encodes the size constraints as executable checks — multiples of 16, longest side under 3840, ratio cap 3:1, total pixels 655,360–8,294,400 — and independently corroborates those figures. Its CLI default is `1024x1024`.

A widely-starred "awesome prompts" collection carries **gpt-image-1-era parameters** (`quality: standard | high`) and heavy commercial affiliation to a paid API reseller. **Use it for prompt text only. Never for parameters.**

A very large community-curated collection (roughly 400 KB of README) exists and was not minable within this research environment. It is flagged here as an unexplored resource rather than summarised on faith.

## 11.6 Two persistent myths worth killing

**The yellow/sepia cast.** No evidence was found that this is a GPT Image 2 problem. The warm colour bias, over-sharpening, and pose/overlap errors belong to **gpt-image-1**; gpt-image-1.5 is documented as having addressed the warm bias. Zero first-person gpt-image-2-era complaints surfaced. Note also that several of the sites keeping this belief alive sell tint-correction products.

**Aspect-ratio drift.** Not supported by evidence either — the opposite is documented, including an observation of *"absolute conformance to the aspect ratio instead of a request for a resolution."* The real constraints are the 3:1 cap and the 16-pixel multiple rule, plus the practical advice to stay under 2:1.

---

# PART 12 — The debugging playbook

When an output is wrong, work through this in order rather than rewriting the prompt from scratch.

**Step 1 — Is it a parameter problem?** Check `model` is explicitly `gpt-image-2`. Check `size` satisfies all four constraints. Check you are not sending `input_fidelity`. Check `quality` — if you are on `low`, move to `medium` before concluding anything about prompt quality. If you are on the Responses API, check whether `revised_prompt` shows your prompt was rewritten.

**Step 2 — Is it a session problem?** If this is your third to fifth generation in one session and quality has dropped, or you are getting near-identical outputs from varied prompts, restart the session. Do not debug the prompt.

**Step 3 — Is it ChatGPT, not the model?** If you are in ChatGPT and quality seems broadly degraded, reproduce through the API before diagnosing further.

**Step 4 — Is it a class of failure prompting cannot fix?** Physical or structural correctness, precise pixel placement, plastic skin in edits, guaranteed region preservation, complex dense typography. If yes, change the workflow — crop and composite, supply a layout reference, render text deterministically, use a different tool for that layer. More prompt will not help.

**Step 5 — Only now, the prompt.** And when you edit it:

- Change **one thing**. Re-read the result against intent before the next change.
- Convert prohibitions into positive descriptions. "Do not include text" → describe the clean surface you want.
- Check every abstract adjective and replace it with a physical specification.
- Check that your intended use is stated.
- Check that references are indexed and role-assigned.
- Check that literal text is quoted or capitalised.
- Count your hard constraints. If there are more than four, you are over budget — split into two generations or accept that some will be dropped.
- If the model is reading left/right in screen space, phrase it in screen space.

**Step 6 — Retry.** Two or three retries of the same prompt genuinely resolve a meaningful fraction of failures. This is not superstition; it is what practitioners report and it is consistent with a sampled generative process.

---

# PART 13 — Worked patterns

Four patterns worth having in muscle memory. Each is a shape, not a script.

## 13.1 Generation from nothing

```
[Intended use]. [Scene: setting, time, atmosphere as physical facts.]
[Subject: concrete physical description.]
[Key details: the 2–4 things that must be right, specified precisely.]
[Camera: shot distance, height, lens behaviour, depth of field.]
[Light: sources, direction, quality, colour.]
[Text, if any: "IN QUOTES", with placement and treatment.]
[Constraints: the 1–3 things that genuinely must not appear.]
```

## 13.2 Multi-reference composition

Index and role-assign first, then instruct. The role assignment is what prevents blending:

```
Image 1: [description] — this is the identity/subject authority.
Image 2: [description] — use for [pose / style / palette] ONLY. Do not take identity from it.
Image 3: [description] — use for [background / layout] ONLY.

[Then the instruction, describing the desired result as a positive fact.]
```

## 13.3 Editing

Given Part 8, the edit prompt that has the best odds looks less like a legal contract and more like a description of the finished image:

```
[Describe the desired final image as a complete positive statement —
 including the parts you want unchanged, described as facts rather than as prohibitions.]

Change: [the one thing that differs from the input.]
```

Rather than: *"change the cushions to green, do not modify the sofa, do not modify the floor, keep the lighting…"* — which is the pattern documented as failing — write: *"The same room, same camera position, same soft window light from the left, same walls and wooden floor and glass coffee table. The sofa is unchanged in shape and material. The cushions are deep green woven fabric."*

Same information. Positive framing. Better-supported odds.

## 13.4 A note on the elaborate-preserve-list pattern

Some published community templates run to thirty or forty explicit preserve and negation clauses — for example, exhaustive anatomical lists for pose transfer specifying which arm is forward, which foot is planted, which limbs cross in front. These are worth knowing about because they represent a real practitioner attempt at a hard problem, and they sometimes work.

But the evidence in §8.4 is that this pattern hits a ceiling: the same practitioners who write these lists also report the model overriding them in favour of overall coherence. Use them when nothing else has worked, not as a default. The default should be shorter, positive, and iterative.

---

# PART 14 — Sources and confidence

**Primary, first-party (highest confidence).** OpenAI Cookbook, *GPT Image Generation Models Prompting Guide* (21 April 2026) — the model-specific source of truth, fully extracted. OpenAI developer documentation: the image-prompting guide (now 2.5-titled), the image-generation guide, the tools/image-generation guide, the API reference, the model page, the pricing page, and the content-provenance page.

**First-party but contradictory (flagged individually in Part 4).** The `input_fidelity` conflict, the maximum-edge inequality, the `partial_images` range, streaming support, the quality enum, and the undocumented `revised_prompt`.

**First-party but extracted separately, and re-verified only once.** The pricing figures, the C2PA/SynthID provenance claims, the `/v1/content_provenance_checks` endpoint, the mask 50 MB limit, and the `partial_images` and streaming contradictions come from OpenAI's pricing, model, API-reference and provenance pages rather than from the two prompting documents that anchor most of this report. They were read once, carefully, but a second verification pass against those specific pages was not possible in this environment. Check pricing against the live page before you budget against it — pricing changes.

**Reported but not confirmable here.** The 32,000-character prompt maximum is ecosystem consensus and appears in neither primary prompting document. One vendor guide states 7,000 instead. The architecture description in §1.1 (autoregressive, with a reasoning step), the identity of `chatgpt-image-latest`, the ~1536-token internal patching limit in §8.8, and Azure's `input_fidelity` failure behaviour are all reported from secondary sources and are not independently verified.

**Practitioner reports from the OpenAI developer forum (attributed, moderate-to-high confidence).** Sixteen threads were read in full. Findings are weighted by how many *independent* people reported the same thing; that count is stated in each case. The strongest consensus items — mask non-confinement, the failure of negative-constraint escalation, session degradation, and coherence-over-correctness — each have three or more independent reporters across unrelated domains.

**Third-party vendor guides (moderate confidence, timestamp-sensitive).** fal.ai, Luma AI, Higgsfield, Replicate, Azure/Foundry, and community GitHub repositories. Every one of these that predates late August 2026 contains at least one now-false claim about transparency, which is the reason this guide timestamps them.

**Known gaps, stated plainly.** Higgsfield's own pages could not be fetched directly in this environment; the finding that it publishes no dedicated GPT Image 2 prompting guide rests on repeated search-engine evidence rather than a site audit. Reddit, Hacker News, and X were unreachable, so community sentiment from those platforms is absent rather than negative. Two vendor guides (Atlabs, PixVerse) are thinly covered. One very large community prompt collection was not minable. The "underdrawings" deterministic-text technique is unverified against this model.

**Things this guide deliberately does not claim.** That GPT Image 2 has a yellow cast (it does not — that was gpt-image-1). That it drifts on aspect ratio (the opposite is documented). That text rendering is systematically broken (no first-person reports found). That the September 2026 ChatGPT quality complaints reflect the model (a control test through the API says otherwise). That any of the September 2026 material about gpt-image-2.5 applies here.

---

# PART 15 — THE PROMPT STRUCTURE

This is the general-purpose structure. It is not domain-specific and it is designed to be filled in the same way every time, so that when an output is wrong you know which line to change.

## 15.1 The structure

```
[1] PURPOSE      — What this image is for.
[2] SCENE        — Where and when. The world the subject sits in.
[3] SUBJECT      — Who or what the image is of, described physically.
[4] KEY DETAILS  — The 2–4 things that must be right. Nothing else goes here.
[5] CAMERA       — Shot distance, height, angle, lens behaviour, depth of field.
[6] LIGHT        — Sources, direction, quality, colour temperature.
[7] TEXT         — Any literal strings, in quotes, with placement and treatment.
[8] CONSTRAINTS  — The 1–3 things that genuinely must not appear.
```

Slots 7 and 8 are omitted when empty. Slots 1 through 6 are always present.

## 15.2 What goes in each slot

**[1] PURPOSE.** One phrase naming the artefact type: *photorealistic editorial photograph*, *flat vector UI mockup*, *print magazine advertisement*, *children's book illustration*, *technical infographic*, *product packshot*. This sets the model's mode and level of polish, and it is the highest-leverage line in the prompt. Include the word **"photorealistic"** here literally if that is what you want — it engages a distinct mode.

**[2] SCENE.** Place, time of day, season, weather, atmosphere — as physical facts, not moods. Established first so that every later clause has a world to attach to.

**[3] SUBJECT.** Physical description only. Shape, material, colour, scale, condition, posture. For people: build, clothing, hair, expression described as facial mechanics, body position described as limb placement. Not emotions, not backstory.

**[4] KEY DETAILS.** The constraint budget, and it is small on purpose. Two to four things, each specified precisely. This is where you spend your specificity. Everything you leave out here, the model fills in — and it fills in competently. Overloading this slot is the primary cause of the model dropping the constraint you cared about most.

**[5] CAMERA.** Extreme close-up / close / medium / wide / establishing. Ground level / low / eye level / high / overhead. Wide-angle with visible distortion / normal / compressed telephoto. Shallow or deep focus, and where the focal plane sits. The model has strong priors for all of this. Note that camera *framing* is reliable while precise element *placement* is not — describe the shot, not a coordinate grid.

**[6] LIGHT.** Named sources with direction and quality: *single softbox at 45 degrees from camera left*, *overcast diffuse daylight*, *low sun behind the subject creating rim light*, *practical tungsten lamps in frame*. Add colour temperature and shadow behaviour. Light is where "looks amateur" and "looks professional" actually live.

**[7] TEXT.** Literal strings in **"quotation marks"** or **ALL CAPS**. Spell difficult words letter by letter. State position, relative size, weight, and typographic style. Keep total text volume low — this is still where the model degrades.

**[8] CONSTRAINTS.** One to three, maximum. Every constraint you add competes with the others, and the model resolves competition in favour of overall coherence. **Prefer converting a constraint into a positive statement in slots 2–6 wherever you can** — describing the clean background you want beats prohibiting the clutter you don't.

## 15.3 The template, ready to fill

```
A [PURPOSE] of [SUBJECT, one line].

Scene: [place, time, conditions — physical facts].

Subject: [physical description — form, material, colour, scale, condition;
          for people: build, clothing, posture as limb placement,
          expression as facial mechanics].

Key details: [detail 1, specified precisely].
             [detail 2, specified precisely].
             [detail 3, if needed].
             [detail 4, if needed].

Camera: [shot distance], [camera height/angle], [lens behaviour],
        [depth of field and focal plane].

Light: [source and direction], [quality — hard/soft/diffuse],
       [colour temperature], [shadow behaviour].

Text: "[LITERAL STRING]" — [position], [relative size], [weight and style].

Constraints: [the 1–3 things that must not appear].
```

## 15.4 The same structure for editing

Editing inverts the emphasis, because the model regenerates the whole image every time and cannot be region-locked. Describe the finished image as a positive fact, then name the single change:

```
[Describe the complete desired image using slots 2–6 above, including
 everything you want unchanged — stated as description, not as prohibition.]

Change: [the one thing that differs from the input].

References:
Image 1: [description] — identity/subject authority.
Image 2: [description] — [pose / style / palette] only; do not take identity from it.
```

Role-assigning every reference is what stops the model blending them. And note the shape: the preserve-list has become description rather than a list of "do not" clauses, which is the pattern with the better evidence behind it.

## 15.5 The compact form

For quick work, the structure collapses to one line without losing its logic:

```
[Purpose] of [subject] in [scene], [key detail], [key detail],
[camera], [light].
```

Example shape: *"A photorealistic editorial photograph of a weathered brass compass resting on a folded nautical chart, the needle pointing north-northeast, salt crystals visible on the glass, close-up at eye level with shallow depth of field, single window light from camera left with soft falloff."*

Same eight slots, same order, no headings.

## 15.6 Rules of use

**One change per iteration.** Identify which slot is wrong, edit that slot, regenerate. This is the difference between converging in three passes and churning for twenty.

**Keep slot 4 under five items.** If you have more than four things that must be right, you have two images, or you have an item that belongs in slots 2–6 as ordinary description.

**Prefer description to prohibition everywhere.** Slot 8 is a last resort, not a workspace.

**Keep the slot order fixed.** The specific order matters less than the fact that it never changes. A prompt with stable structure is a prompt you can debug.

**Set your parameters deliberately.** `model="gpt-image-2"` explicitly, an explicit `size` that satisfies all four constraints, `quality` at `medium` or above, and no `input_fidelity`. A perfect prompt against wrong parameters produces a wrong image.

**When the structure stops helping, stop prompting.** Physical correctness, exact placement, guaranteed preservation, skin texture in edits, dense typography — these have a documented ceiling that no prompt clears. Change the workflow instead.


