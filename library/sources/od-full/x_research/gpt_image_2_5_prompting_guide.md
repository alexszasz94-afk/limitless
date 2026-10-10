# GPT Image 2.5 — Complete Prompting Guide

**Models covered:** `gpt-image-2.5-flare` and `gpt-image-2.5-sunburst`
**Compiled:** 2026-09-11
**Scope:** general-purpose prompting — generation and editing, across every domain OpenAI documents plus the domains they omit.

---

## 1. Scope and method

This guide is assembled from primary sources first and secondary sources only where the primary sources are silent.

**Primary sources (authoritative, read end-to-end):**

- OpenAI's official image-prompting guide (`developers.openai.com` — image prompting). Read in full, including all 24 settings-bearing worked examples with their exact API settings.
- OpenAI's official image-generation guide (`developers.openai.com/api/docs/guides/image-generation.md`). Read in full — parameters, masking, limitations, error handling, pricing, rate limits.
- The OpenAI model pages for both models (source of the rate-limit table in section 10).
- The live Higgsfield model schema for `gpt_image_2_5`, queried directly from their API rather than read off a marketing page.

**Secondary sources (used for gap-filling and independent verification):**

- fal.ai's model pages, which supply verbatim example prompts for domains OpenAI does not cover (food, architecture, poster design, portraiture, packaging) plus independently measured per-image costs.
- MindStudio's hands-on review — the only genuine independent testing found, and the source of the most useful behavioural insight in this document.
- A third-party technical breakdown ("Decoded") which independently corroborated the official guide without adding new claims — useful as a signal that the primary source was captured completely.

**A warning about sourcing.** Search-engine AI summaries currently attribute a "GPT Image 2.5 prompting guide" to Higgsfield. That guide does not exist. The text those summaries reproduce originates from aggregator sites (promptessor.com, tosea.ai, pixazo.ai, canirunit.net, wavespeed.ai) and appears on no Higgsfield page. Section 13 documents what Higgsfield actually publishes, which is roughly forty words of advice. Do not cite invented guidance to a vendor.

Where sources conflict, this guide follows OpenAI's documentation and says so explicitly.

---

## 2. The two models, and how model choice affects prompting

OpenAI's framing, verbatim:

> GPT Image 2.5 Flare is the small model, optimized for speed, with image quality comparable to GPT Image 2. GPT Image 2.5 Sunburst is the base model, optimized for quality, with higher image quality than GPT Image 2. Both models offer improvements in precise editing and subject preservation.

And the routing rule:

> Choose Sunburst for workflows where editing precision matters most, and Flare for fast, high-quality everyday image generation.

**The single most important prompting fact about these two models: OpenAI does not differentiate prompt wording between them.** Every worked example in the official prompting guide runs on *both* models with an identical prompt and identical settings. There is no Flare dialect and no Sunburst dialect. Everything in sections 4 through 12 of this guide applies to both.

What the model choice does change is your *workflow*, and OpenAI prescribes a specific procedure: establish the quality bar with Sunburst first, then re-test Flare on the identical prompt and identical inputs, and switch to Flare only if quality holds *and* latency actually improves. Do not start on Flare and hope; you will not know whether a disappointing result is the prompt's fault or the model's.

One trap worth internalising:

> The same quality label does not imply the same image quality or response time across models.

`quality="high"` on Flare and `quality="high"` on Sunburst are not the same thing. Quality labels are per-model, not absolute.

Both models support generation, editing, and transparent backgrounds. Both are priced at identical token rates (section 10).

---

## 3. Rule zero — parameters are not prose

This is the first thing OpenAI tells you and the most commonly violated rule in practice: **set API parameters separately from the prompt.**

Aspect ratio, resolution, quality tier, output format and transparency are *fields in the request*, not sentences in the prompt. Writing "make it 16:9, 4K, transparent background, PNG" into your prose does three harmful things: it wastes the model's attention on instructions it cannot act on, it risks the model rendering those words as literal text in the image, and it leaves the actual parameter unset so you get the default instead.

### Parameter reference (confirmed in both official documents)

| Parameter | Values | Notes |
|---|---|---|
| `model` | `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` | |
| `quality` | `auto` (default), `low`, `medium`, `high`, `xhigh`, `max` | Per-model meaning — not comparable across models |
| `size` | `auto`, or `WIDTHxHEIGHT` | Common: 1024x1024, 1536x1024, 1024x1536, 2048x2048, 2048x1152, 3840x2160, 2160x3840 |
| `background` | `auto`, `opaque`, `transparent` | Transparent requires PNG or WebP output |
| `output_format` | `png` (default), `jpeg`, `webp` | JPEG returns faster than PNG |
| `output_compression` | 0–100 | JPEG and WebP only — never PNG |
| `n` | integer, default 1 | Multiple variations from one prompt |
| `moderation` | `auto` (default), `low` | Two values only |
| `partial_images` | 0–3 | Each costs +100 image output tokens |
| `stream` | boolean | Supported on both APIs |
| `action` | `auto`, `generate`, `edit` | **Responses API tool only** |
| `mask` | image file | `images.edits` — inpainting |
| `input_image_mask` | `{file_id}` | The Responses-tool equivalent of `mask` |

**`input_fidelity` does not apply to GPT Image 2.5.** It appears only in the earlier-models section of the documentation. Do not send it.

**Not mentioned anywhere in the official documentation:** `seed`, `negative_prompt`, `style`, `response_format`, `user`. There is no reproducibility seed and no negative-prompt field — exclusions go in the prompt prose as constraints (section 5, fundamental 6).

### Custom resolutions

Each edge must be ≤ 3840 and a multiple of 16. The aspect ratio must fall between 1:3 and 3:1. Total pixel count must fall between 655,360 and 8,294,400. **Anything above 2560×1440 (3,686,400 px) is flagged experimental by OpenAI** — treat 4K output as unproven for production until you have tested it on your own prompts.

### Transparency

Set `background="transparent"` and `output_format="png"` or `"webp"`. Then actually verify the decoded alpha channel — check hair edges, glass, and cast shadows specifically, since those are where alpha most often fails. And note OpenAI's warning about the failure mode where the model *draws* transparency instead of producing it:

> A drawn checkerboard is not transparency.

Your prompt should explicitly exclude a checkerboard pattern when requesting cutouts.

### Which API endpoint

This matters more than it looks:

> the mainline model (for example, `gpt-5.5`) will automatically revise your prompt for improved performance

The Responses API rewrites your prompt before it reaches the image model, and returns the rewrite as `revised_prompt`. If you have carefully engineered a prompt — especially one with exact text or a long preservation list — that rewrite can undo your work. **For literal control, use the `images.generations` and `images.edits` endpoints.** (OpenAI documents the rewrite only for the mainline Responses path and never claims it for the images endpoints; that those endpoints send your prompt through unmodified is a reasonable inference from the documentation rather than an explicit statement. If literalness is critical, log `revised_prompt` on any Responses call and compare.) Use the Responses tool when you want the convenience of a conversational agent doing the prompting for you.

### Reference images

Neither official document states a maximum number of reference images. OpenAI's largest example uses four. Higgsfield's marketing claims sixteen — that is a Higgsfield claim, not an OpenAI one, and should not be attributed to OpenAI.

---

## 4. How the model actually behaves — the mental model

Before the rules, the intuition. GPT Image 2.5 is a *reasoning* image model rather than a pure diffusion model, and that single fact explains most of its characteristic behaviour.

**It is literal.** MindStudio's independent testing put this beyond doubt: asked for a wine glass "filled to the top," it produced a wine glass filled to the top — a request diffusion models have famously failed for years. Asked for a clock reading 5:15, it rendered 5:15. Their summary is the best one-line description of the model class:

> Newer "thinking" image models… reason through the literal request instead, trading some aesthetic polish for accuracy.

The practical consequence is that **specific instructions work.** "Full body visible, feet included" is not a hopeful incantation; it is an instruction the model follows. Stop hedging your prompts.

**It does not invent art direction.** This is the flip side of the same trait, and it is the single most important adjustment for anyone coming from Midjourney or earlier DALL·E. MindStudio's finding: bare-bones outputs are correct but can feel flat. The model will not decide on a beautiful lighting setup for you. It will render what you asked for, competently, and nothing more. **Whatever aesthetic you want, you must supply.** A prompt that names film stock, shot size, camera height, focal length, light source, depth of field and grain will produce a photograph; a prompt that says "a nice photo of an old sailor" will produce something correct and forgettable.

**It fills gaps with defaults.** Anything you leave unspecified gets a generic value. That is not a bug to complain about, it is a lever: every under-specified element is a place where you have delegated the decision to the model.

**Its register is contagious.** Ask for a "cinematic" anything and you get orange-and-teal grading and dramatic rim light whether you wanted them or not. OpenAI's own documentation counters this with an explicit anti-cinematic clause in its photo-insertion example — `Avoid cinematic lighting, dramatic color grading, or stylized composition.` — and with a parallel anti-retouching clause in its portrait example. If you want a plain photograph, you must actively suppress the model's stylistic default.

**Compounding constraints degrade.** MindStudio stacked four independent constraints (a pelican, a bicycle, a clock reading 5:15, a full wine glass) and the result showed strain: both an analog and a stray digital clock, flamingo-like legs, pedals on the same side of the frame. Each constraint you add raises the chance that one of the others slips. For high-constraint images, generate a base and then apply constraints one at a time as edits.

**The comped look persists.** Foreground subjects can still read as pasted onto the background — an inheritance from GPT Image 1. Grain is reduced from earlier models and background crowds are much improved, but the subject-integration weakness remains. This is precisely why OpenAI's insertion examples all include an explicit integration clause telling the model to match lighting, shadow direction and colour temperature.

**Drift is real across turns.** OpenAI is candid about this:

> Repeated edits can still change details you intended to preserve… If a region must remain pixel-identical, composite the approved edit into the original image instead of relying on prompting alone.

Prompting is not a guarantee. For anything legally or commercially load-bearing — a logo, a label, a face — composite in post.

**Text is still the weak point.** OpenAI's own limitations section:

> the model can still struggle with precise text placement and clarity

…and on consistency:

> may occasionally struggle to maintain visual consistency for recurring characters or brand elements across multiple generations

…and on layout:

> may have difficulty placing elements precisely in structured or layout-sensitive compositions.

Latency reaches up to two minutes on complex prompts. Plan timeouts accordingly.

---

## 5. The eight fundamentals, verbatim — with commentary

These are OpenAI's own eight principles, quoted exactly, each followed by what it means in practice.

### 1. Define the result

> Name the subject and intended use, such as a product photograph, advertisement, or diagram. Specify the composition, aspect ratio, and important placement constraints. For complex requests, organize the prompt as scene, subject, details, and constraints, using labeled sections.

**In practice:** open with a one-line statement of what artifact you are producing and what it is for. "A product photograph for an e-commerce listing" primes an entirely different set of conventions than "a product photograph." The model knows what those artifact categories look like; naming one buys you a large amount of unstated context for free.

Note the internal tension in OpenAI's own documentation: the overview says order your prompt *subject, composition, style, constraints*, while this fundamental says *scene, subject, details, constraints*. The two orderings disagree about everything except one thing — **constraints go last.** That is the only ordering rule the documentation asserts consistently, and section 14 honours it.

### 2. Choose a maintainable format

> Short prompts, descriptive paragraphs, JSON-like structures, instructions, and tags can all express the same intent. Choose the format that makes the requirements easiest to read and update rather than relying on special syntax.

**In practice:** this is the most misread principle in the document. It is explicitly telling you that **format is not a quality lever.** JSON prompts are not magic. Tag soup is not magic. Labeled sections are not magic. They are all equivalent in the model's eyes; you choose among them for *your* benefit — because a labeled prompt is easier to diff, hand to a colleague, and edit six months later than a 200-word paragraph.

The corollary: stop hunting for the secret syntax. There isn't one. Invest that effort in describing the image better.

### 3. Describe visible details

> Name materials, lighting, colors, and the visual medium. Request "photorealistic" or "real photograph" explicitly when that is the goal, and describe framing and texture. Treat camera specifications as cues for appearance, not a guarantee of exact physical simulation. For wide, cinematic, low-light, rainy, or neon scenes, specify scale, atmosphere, and color instead of relying on mood words alone.

**In practice:** two distinct instructions hide in here. First, **say "photorealistic" or "real photograph" out loud** — do not assume photography is the default, because it isn't. Second, and more subtly: camera specs are *appearance cues*. Writing "85mm f/1.4" does not invoke a physical lens simulation; it invokes the *look* the model associates with that notation — compressed background, shallow focus falloff. Useful, but do not expect optical accuracy, and do not stack six camera specs expecting compounding precision.

The last sentence is the one people skip. Mood words like "moody," "atmospheric," and "epic" are close to worthless on this model. Replace each one with its physical cause: not "moody" but "single low-key source from camera left, deep falloff into shadow, no fill." Not "rainy atmosphere" but "wet asphalt with specular reflections of neon signage, fine rain visible against the dark background."

### 4. Specify people and actions

> Describe body framing, relative scale, gaze, and interaction with objects. Instructions such as "full body visible, feet included," "looking down at the open book," or "hands naturally gripping the handlebars" make the intended pose and action clearer.

**In practice:** four named variables — **framing, scale, gaze, contact.** Gaze and contact are the ones everyone forgets, and they are where the uncanny results come from. Hands that don't quite touch the object they're holding and eyes pointed nowhere in particular are the signature of an under-specified human. Say where the eyes go. Say what the hands are physically in contact with.

"Full body visible, feet included" is worth memorising verbatim — cropped feet are one of the most common framing failures.

### 5. Specify exact text

> Put required wording in quotes and describe its position and typography. Spell unusual words or brand names letter by letter when needed. Ask for no extra text, then check spelling and legibility in the output. Compare medium or high quality for small text, dense information, or multiple fonts.

**In practice:** a five-part protocol, and text is the area where sloppiness costs you the most reruns.

1. **Quote the exact string.** Put it on its own line if it is long.
2. **Spell out anything unusual** letter by letter — invented brand names, foreign words, unusual proper nouns.
3. **Describe position and typography** separately from the string itself.
4. **Ban extra text explicitly.** The model's instinct is to decorate with additional plausible-looking words. `No extra text, no watermarks, no unrelated logos.` is OpenAI's own recurring boilerplate.
5. **Raise the quality tier.** OpenAI's own examples use `quality="medium"` as the norm but switch to `quality="high"` specifically for dense-text cases — a translation edit, a science diagram, a pitch slide.

OpenAI's billboard example adds a sixth technique worth stealing: **assert the occurrence count.** "Render the tagline exactly once" prevents the model from helpfully repeating your tagline in a corner.

### 6. Separate changes from constraints

> For edits, say "change only X" and list the details to preserve, such as identity, geometry, layout, lighting, or labels. State exclusions such as unwanted text, logos, or watermarks. For precise local edits, also identify saturation, contrast, arrows, camera angle, and surrounding objects that must remain unchanged.

**In practice:** this is the highest-leverage principle in the entire document and the one that most distinguishes GPT Image 2.5 from earlier models. Editing precision is the headline capability, and this is how you access it.

The pattern has two halves that must both be present. The **change statement** — "change only X," "replace ONLY the white chairs" — and the **preservation list**, enumerated explicitly rather than gestured at. "Keep everything else the same" is much weaker than naming the things: identity, facial features, hair, pose, body proportions, camera angle, framing, background, lighting direction, shadows, colour temperature, saturation, contrast, labels, text.

Yes, it feels redundant. It works. OpenAI's clothing-swap example — the single highest-value prompt in their documentation — is essentially one sentence of instruction followed by a long, boring, exhaustive keep-list, and OpenAI explicitly notes the same pattern transfers to product images.

Note the final sentence: for *precise local* edits, extend the list to saturation, contrast, camera angle and surrounding objects. These are the things that drift silently while you're watching the thing you asked to change.

### 7. Assign roles to references

> Identify each input by number and purpose: subject, style, clothing, or background. Explain how the inputs should combine and which elements should move where.

**In practice:** never pass multiple references and hope the model infers your intent. Address them ordinally and assign each a job: "image 1 provides the scene, image 2 is the subject, image 3 is the style reference." Then state the *combination rule* — what moves from where to where. OpenAI's own example does exactly this, taking the dog from the second image and placing it into the setting of the first, while preserving the dog's markings and the setting's lighting.

Two references with no roles assigned is an invitation for the model to average them.

### 8. Iterate deliberately

> Pass the previous output as the next edit input, request one change, and repeat the details to preserve. References such as "same style as before" can carry context, but restate critical constraints if the result drifts. Compare results before adding more instructions.

**In practice:** one change per turn. Feed the previous output back in as the input. **Repeat the preservation list every single turn** — it does not persist, and this is exactly where drift creeps in.

"Compare results before adding more instructions" is a discipline point: the common failure is stacking three more clauses onto a prompt that failed, when the right move is to look carefully at what actually went wrong and change one thing.

---

## 6. Prompt anatomy — length, order, and format

**Length.** OpenAI gives no numbers. Their examples span the full range: single-sentence edits ("Remove the flower from man's hand. Do not change anything else.") up to roughly twenty lines for complex labeled generations. The operative principle is *sufficiency, not length* — every element you care about should be specified, and nothing else should be there. Padding a prompt with adjectives does not improve it; on a literal model, it adds noise.

**Order.** Constraints last. That is the one rule both of OpenAI's competing orderings agree on. Of their four labeled examples, two carry a dedicated exact-text block, and in both it lands last with constraints immediately before it. The working order that satisfies everything the documentation says:

deliverable statement → scene → subject → style/medium → constraints → exact text

**Format.** Per fundamental 2, choose for maintainability. Three formats appear in OpenAI's own examples:

*Labeled sections* — used for their most complex prompts. The label sets they actually use:

- `Character: / Theme: / Style: / Constraints:`
- `Scene: / Character Consistency: / Style: / Constraints:`
- `Scene: / Mood: / Style: / Constraints: / Include ONLY this card text (verbatim):`
- one-line subject spec + `Concept: / Style: / Constraints: / Include ONLY this packaging text (verbatim):`
- `Output:` appears as a label in the transparent-cutout prompt

*Descriptive paragraphs* — used for photography and for the identity-preservation clothing swap. Prose works well where the elements interlock and a bulleted breakdown would fragment them.

*Single-line instructions* — used for simple edits.

**Emphasis.** OpenAI uses all-caps sparingly and consistently, reserved for inviolable rules: `ONLY`, `EXACT`, `verbatim`. Use the same discipline. All-caps everywhere means all-caps nowhere.

---

## 7. Generation playbook by domain

This section consolidates the domain-specific guidance from OpenAI's 24 worked examples, plus fal.ai's examples for the domains OpenAI omits.

### Photorealism

The load-bearing example in OpenAI's guide is an elderly sailor portrait, and its structure is worth copying wholesale: **film stock + shot size + camera height + focal length + light source + depth of field + grain**, then an anti-retouching clause — `No glamorization, no heavy retouching.`

That last clause is doing real work. The model's default for a human face trends toward flattering. If you want weathered skin, visible pores, and asymmetry, ban the retouching explicitly.

fal's portrait example adds the concrete-craft version: a ceramicist, "Shot on 50mm at f/2.8, 35mm film colour" — naming a specific practice and a specific optical signature rather than a mood.

### Advertising and campaign imagery

OpenAI's "Thread" tagline ad demonstrates the occurrence-count technique: "Render the tagline exactly once." Ad layouts are where the model's urge to add plausible extra text is strongest — a second tagline, a fake URL, a legal line. Ban them.

### Logos and marks

The Field & Flour example combines transparency with an originality clause: `original, non-infringing`, `clean alpha edges`, plus an explicit checkerboard ban. All three matter. The originality clause reduces the chance of drifting toward an existing mark; the alpha clause targets the specific technical failure; the checkerboard ban targets the specific misunderstanding of what transparency means.

### Text-heavy layouts — billboards, cards, packaging

OpenAI's billboard prompt is the text-lockdown formula in its purest form, and it is worth reproducing as a structure:

```
Billboard text (EXACT, verbatim, no extra characters):
"<your string on its own line>"
Typography: <typeface character, weight, case, alignment>
<occurrence and legibility assertion>
<exclusions>
```

Every element earns its place. The label declares exactness three ways. The string is isolated on its own line so it cannot bleed into surrounding prose. Typography is separated from content. The occurrence assertion stops repetition. The exclusions stop decoration.

### World knowledge

The Bethel NY 1969 example is two lines long and produces a period-accurate scene. The model carries substantial world knowledge; naming a specific place and year is far more efficient than describing the period's visual signifiers yourself. Use this — but verify, since the model will confidently render a plausible rather than accurate period when its knowledge is thin.

### Infographics and explainers

The Jura coffee-machine infographic is short, casual, and first-person. A notable finding: OpenAI did *not* write a formal spec for it. Register matches output — a casual prompt produced a friendly explainer.

The science diagram ("Cellular Respiration at a Glance") goes the other way, and OpenAI's framing is explicit:

> Prompt them like an instructional design brief: define the audience, lesson objective, visual format, required labels, and scientific constraints.

Five named variables. Note `quality="high"` and landscape `1536x1024` for this one.

### Slide design

The "Market Opportunity" pitch slide is written, in OpenAI's words, *like an artifact spec rather than an illustration request*. It uses Markdown bold and nested bullets inside the prompt to convey hierarchy, names a specific typeface, and sets quality by analogy to a known design standard. Settings: `1536x864`, `quality="high"`.

### Interface mockups

OpenAI's farmers-market UI example, with their framing:

> describe the product as if it already exists… avoid concept art language so the result looks like a usable, shipped interface rather than a design sketch.

Present tense, real product. fal's SaaS dashboard example adds the framing instruction that fixes the most common UI-mockup failure: "filling the whole frame edge to edge, no browser chrome." Without it you get a screenshot of a browser window instead of a design.

### Comics and sequential art

> define the narrative as a sequence of clear visual beats, one per panel. Keep descriptions concrete and action-focused.

One beat per panel. Concrete actions, not emotional states.

### Character consistency

The children's-book example is a two-part structure: a character sheet first, then scenes that carry a dedicated `Character Consistency:` block plus the instruction `Do not redesign the character.` Build the sheet once, then reference it in every subsequent generation.

MindStudio's testing found GPT Image 2.5 beat both Nano Banana 2 and Nano Banana Pro on four-angle character consistency — this is a genuine strength, but it still requires the explicit block.

### Transparent cutouts

The product-cutout prompt uses the `Output:` label and a stack of precise technical constraints: "no halos/fringing," "Preserve product geometry and label legibility exactly," "Add only light polishing," "Do not restyle the product." Plus `no solid backdrop, scenery, checkerboard, or watermark`.

Note the structure: it grants one narrow permission ("light polishing") and bans everything adjacent. That asymmetry is the whole technique.

### Domains OpenAI does not cover

The official guide has no food, poster/print, architecture or dedicated portrait section. fal's examples fill these:

- **Food:** "Hard midday sunlight with crisp shadows" — food photography lives or dies on light quality, and naming it specifically beats any amount of appetising-adjective stacking.
- **Print/poster:** a Swiss-style poster reading "FORM / COUNTERFORM" — naming a design tradition imports its whole grammar.
- **Architecture:** a concrete and timber house at dusk — material naming plus time of day.
- **Editorial:** a magazine cover with the masthead treated as exact text.
- **Packaging/e-commerce:** a four-line copy block ("NORTHBOUND / facial oil / rosehip + sea buckthorn / 30 ml") treated as exact text with a stated hierarchy.

---

## 8. Editing playbook

Editing precision is the headline capability of both 2.5 models. This section is where the return on careful prompting is highest.

### The core pattern

Three parts, all required:

1. **The single change**, stated restrictively. "Change only X." "Replace ONLY the white chairs." The word ONLY, capitalised, is OpenAI's own convention.
2. **The preservation list**, enumerated. Not "keep everything else" — name them: identity, facial features, hair, pose, proportions, camera angle, framing, background, lighting direction, shadows, colour temperature, saturation, contrast, labels, text, surrounding objects.
3. **The addition ban.** "Do not add new elements or text." The model's instinct when editing is to improve; that instinct is your enemy.

### Identity preservation

The clothing-swap example is the reference implementation. Its shape: one sentence naming the garment change, then an exhaustive keep-list covering the person's identity, then an *integration clause* — the new garment must match the scene's lighting, shadows and colour temperature so it does not look pasted on — then an explicit ban on adding accessories.

The integration clause is not optional. Recall from section 4 that the comped look is this model's persistent weakness; the clause is the direct countermeasure.

OpenAI notes that the same pattern applies to products, not just people. Swapping a label, a colourway or a component follows the identical structure.

### Insertion

The bear-campsite example inserts a subject into an existing photograph using a three-paragraph structure and states the anti-cinematic clause *twice*. That repetition is deliberate: inserting a dramatic subject is exactly when the model reaches for dramatic lighting, and one mention is evidently not enough.

### Local edits

"Remove the flower from man's hand. Do not change anything else." — one sentence and a lock. For local removal, brevity plus an absolute lock outperforms elaborate description.

### Successive edits

fal's three-step sequence demonstrates the discipline of changing one thing and locking the rest:

> Reupholster the sofa in a deep forest green velvet. Change nothing else in the room.

> Hang a large framed abstract landscape print on the bare wall above the sofa. Leave the rest of the room exactly as it is.

> Change the time of day to evening: warm lamplight inside, blue dusk through the window. Keep the furniture, the artwork and the layout identical.

Three turns, three changes, three locks. Note that each lock is phrased freshly rather than copy-pasted — the model has no requirement for a magic phrase, only for the constraint to be present.

### Sketch to render

The technique is asymmetric permission: preserve the geometry, grant the materials. Plus `Do not add new elements or text` — OpenAI's note:

> Include "do not add new elements/text" to avoid creative reinterpretations.

### Style transfer

The pixel-art example converts medium while preserving content. State both halves: what the new medium is, and what content survives the conversion.

### Text edits

The Spanish translation example runs at `quality="high"` — consistent with fundamental 5's instruction to raise quality for dense text. Translating text inside an image is one of the strongest demonstrations of editing precision, and also one of the easiest to get subtly wrong at low quality.

### Masking

Masking (inpainting) is supported on both paths: `images.edits` takes a `mask` file, and the Responses tool takes `input_image_mask` with a `file_id`. OpenAI's caveats are important:

> Masking with GPT Image is entirely prompt-based. The model uses the mask as guidance, but may not follow its exact shape with complete precision.

> If you provide multiple input images, the mask will be applied to the first image.

The mask must match the source image's format and dimensions, must be under 50MB, and must carry an alpha channel. **Treat the mask as a hint that narrows the model's attention, not as a geometric boundary.** You still need the prose constraints. And if a region must be pixel-identical, composite in post — OpenAI says so directly.

Note that Higgsfield's implementation of GPT Image 2.5 exposes no mask support at all (section 13).

---

## 9. Multi-turn refinement and consistency

**Feed the output back in.** Each turn's input is the previous turn's approved output.

**One change per turn.** Stacking changes multiplies drift.

**Restate constraints every turn.** They do not carry. "Same style as before" can carry *some* context — OpenAI says so — but it is a weaker signal than restating the constraint, and when drift appears, restating is the fix.

**Compare before adding.** Look at what actually changed versus what you asked to change. The gap between those two is your drift, and it tells you which preservation clause to add next turn.

**Know when to stop prompting and start compositing.** OpenAI's own guidance, repeated because it is the most practically important sentence in their limitations section:

> If a region must remain pixel-identical, composite the approved edit into the original image instead of relying on prompting alone.

For character consistency across many images, build a character sheet first, then carry a `Character Consistency:` block plus `Do not redesign the character` into every scene. Higgsfield claims edit stability holds across stacked edits — *"a change made three edits ago doesn't degrade as new edits stack on top of it"* — but that is a vendor claim, and OpenAI's own documentation is more cautious. Verify on your own content.

---

## 10. Quality, size and cost — a decision procedure

### Quality

OpenAI's own 24 examples are the best available guidance on real settings:

- **`quality="medium"` is the norm.** Most examples use it.
- **`quality="high"` appears in exactly three examples, all of them dense-text** — the Spanish translation edit, the science diagram, the pitch deck slide.
- `xhigh` and `max` exist but appear in no official example.

And the warning that keeps people from reflexively maxing everything:

> A higher setting doesn't guarantee a better result for every prompt.

### Size

From the same 24 examples: `1024x1536` (portrait) for 21 of them. `1536x1024` for the science diagram and the room edit — both layout-heavy, landscape-native subjects. `1536x864` for the pitch deck slide.

Portrait is the practical default. Go landscape when the content is genuinely horizontal — diagrams, interiors, slides.

### Cost

Token rates are **identical** for both models:

| Token type | Rate |
|---|---|
| Image input | $8 / 1M |
| Cached image input | $2 / 1M |
| Image output | $30 / 1M |
| Text input | $5 / 1M |
| Cached text input | $1.25 / 1M |

But — and this resolves a discrepancy circulating in third-party coverage:

> Equal token rates don't mean equal cost per image: token consumption can differ by model and quality setting.

Several third-party articles claim GPT Image 2.5 costs double GPT Image 2. The official documentation says the two 2.5 variants are priced identically to *each other*, and that 2.5 and GPT Image 2 share the same price per image *output* token. It does not assert that all five rates match GPT Image 2 — so treat "2.5 costs the same as 2" as true for the output-token rate specifically, not as a blanket claim. What rises at `xhigh` and `max` is token *consumption*, not the rate.

fal's independently measured per-image costs at `quality="high"` give a concrete feel for the scale:

| Size | Cost |
|---|---|
| 1024×768 | $0.0362 |
| 1024×1024 | $0.0528 |
| 1024×1536 | $0.0413 |
| 1920×1080 | $0.0395 |
| 2560×1440 | $0.0554 |
| 3840×2160 | $0.1002 |

Editing adds roughly $0.008 per 1024² reference image. `medium` runs about a quarter of `high`. `low` starts around $0.0041.

### Rate limits

Identical for both models. Free tier: unsupported. Tier 1: 100k TPM / 5 images per minute. Tier 2: 250k / 20. Tier 3: 800k / 50. Tier 4: 3M / 150. Tier 5: 8M / 250. (Source: the OpenAI model pages, not the image-generation guide.)

### The decision procedure

1. Start on **Sunburst at `quality="medium"`**, portrait `1024x1536` unless the content is horizontal.
2. Get the prompt right before touching any setting. Most disappointing outputs are prompt problems wearing a settings costume.
3. Raise to `high` **only** if the image contains dense text, multiple fonts, or small type.
4. Once quality is locked, re-test **Flare on the identical prompt and inputs**. Adopt it only if quality holds *and* latency actually improves.
5. Treat resolutions above 2560×1440 as experimental.

---

## 11. Failure modes and QA checklist

Run this against every output before you ship it.

**Text.** Spelling correct? Rendered exactly the number of times you specified? Any extra text the model invented? Legible at final display size? — Text remains the documented weak point.

**Transparency.** Decode the alpha channel and inspect it. Check hair edges, glass, and cast shadows. Confirm you got real transparency and not a drawn checkerboard.

**Framing.** Feet in frame if you asked for full body? Anything clipped at an edge that shouldn't be?

**Hands and contact.** Are hands actually in contact with the objects they're holding? This is the highest-frequency uncanny-detail failure.

**Gaze.** Are the eyes pointed where you specified?

**Integration.** On insertions and swaps — does the subject share the scene's light direction, shadow length and colour temperature, or does it read as pasted on?

**Drift.** On edits — diff against the input. What changed beyond what you asked for? Saturation and contrast shift silently.

**Layout.** OpenAI documents difficulty placing elements precisely in layout-sensitive compositions. Check alignment and margins on anything structured.

**Consistency.** Across a set — same character, same brand elements, same palette? Documented as an occasional weakness.

**Constraint compounding.** If you stacked several independent requirements, verify each one individually. MindStudio's pelican test showed exactly how one constraint quietly fails while you are checking another.

### Error handling

Errors return `error.type = "image_generation_user_error"`. Use `error.code` as the stable discriminator — not the message string. Moderation failures carry `moderation_details.moderation_stage`, one of `input`, `output`, or `unknown`, which tells you whether your prompt or the generated image tripped the filter.

OpenAI's explicit instruction:

> Don't automatically retry these errors without modifying the prompt or input images.

A blind retry loop on a moderation failure burns quota and will not succeed.

---

## 12. Anti-patterns

**Putting parameters in the prose.** "16:9, 4K, PNG, transparent" belongs in the request body. In the prompt it wastes attention, risks being rendered as literal text, and leaves the real parameter at its default.

**Hunting for magic syntax.** Fundamental 2 says formats are equivalent and to choose *"rather than relying on special syntax."* JSON prompts are not a quality unlock.

**Mood words as a substitute for physical description.** "Moody," "epic," "atmospheric," "aesthetic." Replace each with its cause — light position, contrast ratio, colour temperature, atmospheric medium.

**Assuming photorealism is the default.** It is not. Ask for it explicitly.

**"Keep everything else the same."** Far weaker than an enumerated list. Name the things.

**Multiple references with no assigned roles.** The model will average them.

**Stacking new clauses onto a failed prompt.** Diagnose what actually went wrong, change one thing, re-run.

**Trusting prompting for pixel-identical regions.** Composite instead. OpenAI says so directly.

**Blind retries on moderation errors.** Explicitly warned against.

**Sending `input_fidelity`.** It does not apply to 2.5.

**Using the Responses API when you need literal control.** It rewrites your prompt.

**Defaulting to `max` quality.** No official example uses it, and a higher setting does not guarantee a better result.

**Letting "cinematic" in by accident.** If you want a plain photograph, suppress the default explicitly.

**Citing prompting advice to Higgsfield.** The guide that search summaries attribute to them does not exist.

---

## 13. Platform notes — where you run this matters

### OpenAI images endpoints (`images.generations`, `images.edits`)

Full parameter control, including `mask` on `images.edits` for inpainting. This is the correct endpoint for engineered prompts: OpenAI documents prompt rewriting only for the mainline Responses path, not here (see section 3 — this is an inference, so log and compare if literalness is critical).

### OpenAI Responses API image tool

Adds `action` (`auto` / `generate` / `edit`) and takes the mask as `input_image_mask` (a `file_id`) rather than as an uploaded file. **Rewrites your prompt** and returns the rewrite as `revised_prompt`. Convenient for agentic use, wrong for precision work. If you use it, log `revised_prompt` so you can see what was actually sent.

### Higgsfield

**Higgsfield publishes no GPT Image 2.5 prompting guide** — not for 2.5, not for any earlier GPT Image version. This was verified directly on their pages, not inferred from search results. What exists is a launch blog post and a marketing landing page.

The blog post's entire prompting content is one sentence:

> Step 3: Write the prompt. Describe the subject, the setting, the lighting, and the composition directly.

Their FAQ is the totality of the rest:

> Specify what should stay, such as the subject, lighting, or background.

> Describe the subject, setting, lighting, and composition. Add a reference when it helps. For edits, keep each request focused on a clear change.

Roughly forty words in total. Consistent with OpenAI's guidance, just far thinner.

Their positioning: Flare is *"the default choice for most tasks… higher output quality than GPT Image 2 at about 50% less latency"*; Sunburst is *"built for premium work that needs precise control during edits"* — recommended for production ad campaigns, polished product photography, and multi-step edits. Behavioural claims: *"Edits land precisely, changing only what got asked for"*; *"Visual choices like cinematic lighting and specific camera settings carry over from one generation to the next."*

Their landing page does ship 13 copy-paste prompts, which reveal a consistent house style: a shot-type and lighting preamble, then comma-dense visual facts. Their two edit prompts include explicit keep-lists ("keep outfit, pose and expression") — the same pattern OpenAI documents.

**The live API schema, verified directly, contains the most important Higgsfield finding:**

| Field | Values | Default |
|---|---|---|
| `variant` | `flare`, `sunburst` | **flare** |
| `quality` | `low`, `medium`, `high`, `xhigh`, `max` | **low** |
| `resolution` | `1k`, `2k`, `4k` | **1k** |
| `background` | `auto`, `opaque`, `transparent` | nullable |
| media role | `image_references` only | — |
| aspect ratios | auto, 1:1, 3:2, 2:3, 4:3, 3:4, 16:9, 9:16, 21:9, 27:16, 16:27, 9:8, 8:9, 4:5, 5:4 | — |

Two consequences that are easy to miss:

**There is no mask or inpaint support on Higgsfield's GPT Image 2.5.** Their `nano_banana_2` integration exposes a `mask` role and an `is_inpaint` flag; GPT Image 2.5 exposes neither. Nor is there custom `WIDTHxHEIGHT` — you get an aspect ratio and a resolution tier only.

**The defaults are the cheapest possible settings.** Unless you override, you are running flare / low / 1k. If your Higgsfield output looks worse than the API, check this first — it is almost certainly the explanation.

Their credit pricing: 1K Low = 1.5 credits ($0.075); 2K High = 5.5 credits ($0.275); 4K Max = 26.5 credits ($1.325).

What Higgsfield *does* publish is a real, detailed prompt guide for **Google's Nano Banana Pro** — the site-wide footer "Prompt Guide" link. It is a genuine six-variable guide (Subject / Composition / Action / Location / Style) with good advice like *"Remove polite phrases like 'please'"* and *"isolating string literals in double quotes."* Useful, but it is about a different model, and its advice should not be assumed to transfer.

### fal.ai

Endpoints follow the pattern `openai/gpt-image-2.5/flare/text-to-image`, called via `fal.subscribe(endpoint, { input: { prompt, image_size, quality } })`. Their model pages carry the best domain-example coverage outside OpenAI's own guide, and their per-image cost table (section 10) is the most concrete pricing data available.

### ChatGPT and Codex

MindStudio measured default output at roughly 1672×941 — sub-1080p. Anything produced there needs upscaling before production use. OpenAI does not document which variant these surfaces default to; testing suggests Flare.

---

## 14. THE PROMPT STRUCTURE

Everything above converges here. This section gives you the general-purpose skeletons, how to fill them, and worked examples.

Two reminders before the templates, because both are easy to forget under pressure:

**Format is a maintainability choice, not a quality lever.** Fundamental 2 is explicit — short prompts, paragraphs, JSON-like structures and tags all express the same intent, and you choose among them *"rather than relying on special syntax."* Labels are used below because they are easy to read, diff and edit, not because labels make the model perform better. A well-written paragraph carrying the same information performs the same.

**Parameters never go in the prose.** Aspect ratio, resolution, quality, output format and transparency live in the API call.

---

### A. The general-purpose generation structure

```
<One-line deliverable statement: what artifact this is and what it is for.>

Scene:
<Setting, time, place, environment, atmosphere described physically —
 surfaces, weather, light sources and their positions, spatial depth.>

Subject:
<The main subject in specific terms. For people: body framing, relative
 scale, gaze direction, and what the hands are physically in contact with.
 For products or objects: geometry, materials, finish, orientation, scale
 relative to surroundings.>

Style:
<Visual medium first — photograph, illustration, 3D render, diagram, UI.
 Say "photorealistic" or "real photograph" explicitly if that is the goal.
 Then: lighting quality and direction, palette, texture, and camera cues
 (shot size, height, focal length, depth of field, film stock or grain)
 treated as appearance cues rather than physical simulation.>

Constraints:
- <Composition and placement requirements>
- <Things that must be present>
- <Things that must be absent — cinematic grading, extra text, watermarks,
  logos, clip art, stylistic defaults you do not want>
- <Originality requirements where relevant: original design only, no
  trademarks, no copyrighted characters>

Include ONLY this text (verbatim):
"<exact string, on its own line>"
Typography: <typeface character, weight, case, alignment, position>
<Occurrence assertion, e.g. "Render this exactly once." Plus a legibility
 requirement if the type is small.>
```

**Omit any block you do not need.** A prompt with no text in the image drops the final two blocks entirely and ends on `Constraints:`. A simple subject may not need a `Scene:` block. The structure is a checklist, not a form to complete.

**Ordering rationale.** Constraints last is the one ordering rule OpenAI's documentation asserts consistently — the overview and fundamental 1 disagree about everything else. Text after constraints matches three of OpenAI's four labeled examples. The deliverable statement goes first because naming the artifact category ("a product photograph for an e-commerce listing," "a diagram for a high-school biology lesson") imports a large amount of convention for free.

---

### B. The general-purpose edit structure

```
<The single change, stated restrictively.
 "Change only the X." / "Replace ONLY the Y with Z." / "Remove the W.">

Preserve exactly:
- Identity: <facial features, hair, skin, expression, body proportions>
- Geometry: <shape, structure, scale, perspective of everything unchanged>
- Layout: <positions and spatial relationships of all other elements>
- Camera: <angle, height, framing, crop, focal length feel>
- Light: <direction, quality, shadow position and length, colour temperature>
- Colour: <palette, saturation, contrast, overall grade>
- Text and labels: <all existing wording, logos, markings — unchanged>
- Background and surrounding objects: <unchanged>

Integration:
<The changed element must match the scene's existing lighting direction,
 shadow behaviour, colour temperature and grain so that it does not look
 pasted on.>

Do not add:
<New elements, accessories, text, logos, or watermarks. Do not restyle,
 redesign, or "improve" anything not named in the change above.>
```

**Prune the preservation list to what is actually at risk.** A pure colour change on a flat object does not need the identity line. But err toward including a line rather than omitting it — the cost of a redundant line is nothing, and the cost of a missing one is a rerun. The `Camera` and `Colour` lines are the most commonly omitted and the most commonly needed, because angle, saturation and contrast drift silently while you are inspecting the thing you asked to change.

**Do not skip the `Integration` block on insertions and swaps.** The comped-subject look is this model's documented persistent weakness, and this block is the direct countermeasure.

**One change per invocation.** For multiple changes, run multiple turns, feed each output back in as the next input, and restate the full preservation list every turn.

---

### C. Multi-reference addendum

When you supply reference images, prepend this to either structure:

```
Inputs:
- Image 1: <role — subject / style / clothing / background / product>
- Image 2: <role>
- Image 3: <role>

Combination:
<Explicitly what moves from where to where, and what each input
 contributes. Name what is taken from each and what is ignored.>
```

Never pass multiple references without assigned roles.

---

### D. How to fill each block

**Deliverable statement.** Name a real artifact category. "A product photograph for an e-commerce listing." "A diagram for a high-school biology lesson." "A pitch-deck slide." "A shipped mobile app screen." This single line does more work than any other, because it imports the conventions of that category.

**Scene.** Physical causes, not moods. Not "moody warehouse" — "a warehouse lit by a single skylight overhead, deep shadows in the corners, dust visible in the shaft of light." Every mood word you can replace with its cause, replace.

**Subject.** For people, cover the four named variables: framing, scale, gaze, contact. "Full body visible, feet included" is worth using verbatim. For objects, cover geometry, material, finish, orientation and scale.

**Style.** Medium first — the model does not default to photography. Then lighting direction and quality, palette, texture, and camera cues. Remember camera specs are appearance cues, not optical simulation; two or three are useful, six are noise.

**Constraints.** This is where exclusions live, because there is no negative-prompt parameter. OpenAI's own recurring boilerplate is worth keeping on hand:

```
No extra text, no watermarks, no unrelated logos.
Original design only. No trademarks. No copyrighted characters.
Avoid cinematic lighting, dramatic color grading, or stylized composition.
No glamorization, no heavy retouching.
Do not add new elements or text.
```

**Text block.** Quote the exact string on its own line. Spell unusual words letter by letter. Separate typography from content. Assert the occurrence count. Raise `quality` to `high` in the API call.

---

### E. Worked example — generation

```
A product photograph for an e-commerce listing.

Scene:
A seamless light-grey studio backdrop with a soft gradient from
upper-left to lower-right. The product sits on a matte white surface
with a short, soft contact shadow falling to the lower right.

Subject:
A 30ml amber glass dropper bottle standing upright, centred, occupying
roughly 60% of the frame height. Matte black dropper cap. The label
faces the camera squarely and is fully legible. Glass shows a warm
internal glow where light passes through it.

Style:
Photorealistic product photograph. Large soft key light from upper left
at roughly 45 degrees, white bounce fill from camera right, no hard
speculars on the glass. Shot size: medium close-up. Camera at product
mid-height, dead level. 100mm macro look, f/8, everything from cap to
base in sharp focus. Clean commercial finish, no grain.

Constraints:
- Product centred with even margins on all sides
- Label fully legible, no perspective distortion
- No props, hands, or secondary objects
- No cinematic grading, no dramatic rim lighting
- No extra text, no watermarks, no unrelated logos
- Original packaging design only, no trademarks

Include ONLY this label text (verbatim):
"NORTHBOUND
facial oil
rosehip + sea buckthorn
30 ml"
Typography: clean geometric sans, all lowercase except the brand name,
left-aligned, brand name largest and at the top, volume smallest at the
bottom.
Render this text exactly once, on the front label only, and keep every
line legible at full resolution.
```

API settings: `model="gpt-image-2.5-sunburst"`, `quality="high"` (dense small text), `size="1024x1536"`.

---

### F. Worked example — edit

```
Replace ONLY the model's grey knit sweater with a dark navy wool
overcoat, open at the front.

Preserve exactly:
- Identity: face, facial structure, skin tone and texture, expression,
  hair style and hair position
- Geometry: body pose, shoulder line, arm position, hand position,
  body proportions
- Layout: the model's position in the frame and all background elements
  in their current positions
- Camera: angle, height, framing, crop, and depth of field
- Light: key light direction from camera left, shadow position and
  softness, overall colour temperature
- Colour: existing palette, saturation, contrast, and grade
- Text and labels: all signage in the background, unchanged
- Background and surrounding objects: unchanged

Integration:
The overcoat must be lit by the same key from camera left, with shadows
falling in the same direction and at the same softness as the rest of
the image, and must carry the same colour temperature and grain as the
original photograph so it does not look pasted on.

Do not add:
No scarf, no gloves, no bag, no jewellery, no new accessories of any
kind. No new text, logos, or watermarks. Do not restyle the background
or adjust the overall grade.
```

API settings: `model="gpt-image-2.5-sunburst"`, `quality="medium"`, size matched to the source.

---

### G. The structure in one sentence

**Name the artifact, describe the scene and subject physically, specify the medium and light, put every exclusion in a constraints block, quote exact text last — and for edits, state one change, enumerate everything that must not move, and tell the model to match the existing light so the result does not look pasted on.**

---

## Sources

**Primary — OpenAI**

- OpenAI image prompting guide — `https://developers.openai.com/api/docs/guides/image-prompting` (the eight fundamentals, 23 worked examples with settings, domain sections)
- OpenAI image generation guide — `https://developers.openai.com/api/docs/guides/image-generation.md` (parameters, masking, transparency, limitations, errors, pricing, rate limits)

*Note for future fetches: appending `.md` to an OpenAI docs URL returns clean markdown without navigation boilerplate. Both documents are long enough that fetch tools may truncate them silently — image-generation.md runs ~3,621 lines and image-prompting.md ~1,556. Confirm the line count before assuming you have the whole file; the truncation point falls mid-sentence with no error.*

**Primary — Higgsfield**

- Higgsfield GPT Image 2.5 launch blog post and product landing page
- Higgsfield FAQ
- Higgsfield live model schema for `gpt_image_2_5`, queried via their API (variant/quality/resolution defaults, absence of mask support)
- Higgsfield Nano Banana Pro Prompt Guide (different model — cited for contrast only)

**Secondary**

- fal.ai GPT Image 2.5 model pages — domain example prompts, measured per-image costs, successive-edit sequence
- MindStudio hands-on review — literalism testing, compounding-constraint failure, character-consistency comparison, default resolution measurement
- Independent technical breakdown ("Decoded") — used as corroboration of the primary source, contributed no unique claims
