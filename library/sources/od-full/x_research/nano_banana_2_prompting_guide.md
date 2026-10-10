# Nano Banana 2 — Deep Prompting Research & Universal Prompt Structure

**Model:** Gemini 3.1 Flash Image ("Nano Banana 2") · sibling: Gemini 3 Pro Image ("Nano Banana Pro")
**Compiled:** 10 September 2026
**Scope:** General-purpose prompting.

**On sourcing.** Specs, model IDs, parameters, pricing and safety behaviour were taken from primary Google sources (`ai.google.dev` model and API pages, the Gemini API changelog, the pricing page, and DeepMind model cards) and are quoted where the wording matters. Craft advice — how to phrase a lighting brief, how to lock a character across frames — is partly derived from those sources and partly from testing and community practice, and is labelled where it is not directly attributable. Two things to treat as *reconstructed rather than quoted*: the full pixel-dimension table in §2 (Google publishes the ratios and the tier names; the complete per-ratio grid below is assembled from the documented tiers and should be verified against a live render before you rely on an exact number), and any place this document paraphrases Google's positioning of a model rather than quoting it.

---

## 0. How to read this document

Sections 1–4 are **facts you need before you write a single prompt** — what the model actually is, which model ID is live, what it costs (§2a), and what parameters exist. Sections 5–13 are the **craft**: the levers, in rough order of how much they move the output. Section 14 is a **failure-mode lookup table**, and §14a covers **safety filters and how to tell a refusal from a bad prompt**. Section 15 covers **Higgsfield specifically**, since that is where these prompts get run — note that Higgsfield exposes a narrower parameter set than the raw API, so §17.6 gives separate workflows for each path. Section 16 debunks the widely-copied nonsense. Section 17 is the payoff: **the universal prompt structure**.

If you only read two sections, read 4 (why this model is not Midjourney) and 17 (the structure).

---

## 1. The model family, and which ID is actually live

There are four models in the Nano Banana line as of September 2026. Third-party guides are riddled with dead `-preview` model IDs — those were deprecated 28 May 2026 and shut down 25 June 2026. Using them today returns an API error.

| Marketing name | Technical name | **Live stable API ID** | Position (quoted where in quote marks, otherwise paraphrased) |
|---|---|---|---|
| Nano Banana | Gemini 2.5 Flash Image | `gemini-2.5-flash-image` | Legacy, **shutting down 2 October 2026**. Google: "we strongly recommend that customers transition to Nano Banana 2 Lite" |
| Nano Banana Pro | Gemini 3 Pro Image | `gemini-3-pro-image` | "The premium choice for the most complex visual tasks" |
| **Nano Banana 2** | **Gemini 3.1 Flash Image** | **`gemini-3.1-flash-image`** | "Serves as the most versatile model, generalist workhorse model for all tasks" |
| Nano Banana 2 Lite | Gemini 3.1 Flash Lite Image | `gemini-3.1-flash-lite-image` | Speed/volume tier. "Not optimized for multiple reference inputs or multi-turn sequential editing" |

**Release timeline** (from the official Gemini API changelog):

- 26 Aug 2025 — Gemini 2.5 Flash Image preview · GA 2 Oct 2025
- 20 Nov 2025 — Gemini 3 Pro Image preview (Nano Banana Pro)
- 26 Feb 2026 — Gemini 3.1 Flash Image preview (Nano Banana 2)
- **28 May 2026 — both Gemini 3 image models go GA**, `-preview` IDs deprecated
- 25 Jun 2026 — `-preview` IDs shut down
- **2 Oct 2026 — `gemini-2.5-flash-image` shuts down.** That is three weeks from this document's compile date. Anything still pointed at the original Nano Banana breaks then; migrate to `gemini-3.1-flash-lite-image` or `gemini-3.1-flash-image` now.

The "June 18, 2026" launch date circulating in several blog posts is wrong.

### Which one should you actually use?

| Job | Model | Why |
|---|---|---|
| Default for almost everything | **Nano Banana 2** | Best price/quality; 512px draft tier; image-search grounding; extreme aspect ratios; `thinking_level` control |
| Text-heavy posters, infographics, diagrams, dense layout logic | **Nano Banana Pro** | Highest text fidelity, 3 dedicated style-reference slots, 5 character slots, interleaved text+image output |
| High-volume batch drafts, thumbnails, variations | **Nano Banana 2 Lite** | Cheapest, 14 object-reference slots, but no grounding, no character/style slots, 1K only |
| Anything at all | **Not 2.5 Flash Image** | Superseded on every axis |

The practical NB2 workflow: generate cheap at 512px, pick the winner, re-render or upscale that one at 2K/4K. Never burn 4K credits on exploration — §2a shows the arithmetic that makes this the obvious default rather than a matter of taste.

---

## 2. Verified technical specifications

Everything in this table is confirmed against `ai.google.dev` model pages or the image-generation doc.

| Spec | Nano Banana 2 (3.1 Flash Image) | Nano Banana Pro (3 Pro Image) | NB2 Lite (3.1 Flash Lite Image) |
|---|---|---|---|
| Input token limit | **131,072** | 65,536 | — |
| Output token limit | 32,768 | 32,768 | — |
| Input modalities | Text, Image, **Video**, PDF | Text, Image | Text, Image, Video |
| Resolutions | **512px**, 1K, 2K, 4K | 1K, 2K, 4K | 1K only |
| Default resolution | 1K | 1K | 1K |
| Object refs (high fidelity) | up to **10** | up to **5** † | up to **14** |
| Character refs (consistency) | up to **4** | up to **5** | — |
| Style refs | — | up to **3** | — |
| Total reference images | **14 max** | **14 max** | 14 max |
| Web Search grounding | ✅ | ✅ | ❌ |
| **Google Image Search grounding** | ✅ **only NB2** | ❌ | ❌ |
| `thinking_level` control | ✅ `minimal` (default) / `high` | ❌ not exposed | ✅ |
| Knowledge cutoff | January 2025 | January 2025 | January 2025 |
| Watermark | SynthID (always) | SynthID (always) | SynthID (always) |

† Google's own limitation text is the authority here: *"gemini-3-pro-image supports 5 images with high fidelity, and up to 14 images in total."* Some secondary summaries say 6 for Pro. Plan for 5; if a sixth holds, treat it as a bonus.

**Aspect ratios.** Both Pro and NB2 support: `1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9`. **NB2 additionally supports the extreme ratios `1:4, 4:1, 1:8, 8:1`** — these are on the *stable* model, confirmed on the `gemini-3.1-flash-image` model page ("New 1:4, 4:1, 1:8 and 8:1 aspect ratios"). Those extremes are genuinely useful for web banners, side rails, and vertical strip creatives.

**Exact pixel dimensions (Nano Banana 2).** Worth knowing because "2K" is not 2048 wide on every ratio. Treat this grid as a working reference reconstructed from the documented resolution tiers, not as a verbatim copy of a Google table — check an actual render before you build a pipeline that depends on an exact width.

A note on the 512px tier's spelling: Google's own docs render it inconsistently as `512px`, `0.5K` and even `05.K` depending on the page. The string the API accepts is what the current image-generation doc shows in its parameter table; if a call is rejected on `image_size`, that inconsistency is the first thing to check.

| Ratio | 512px | 1K | 2K | 4K |
|---|---|---|---|---|
| 1:1 | 512×512 | 1024×1024 | 2048×2048 | 4096×4096 |
| 4:5 | 464×576 | 928×1152 | 1856×2304 | 3712×4608 |
| 9:16 | 384×688 | 768×1376 | 1536×2752 | 3072×5504 |
| 16:9 | 688×384 | 1376×768 | 2752×1536 | 5504×3072 |
| 3:4 | 448×600 | 896×1200 | 1792×2400 | 3584×4800 |
| 4:3 | 600×448 | 1200×896 | 2400×1792 | 4800×3584 |
| 2:3 | 424×632 | 848×1264 | 1696×2528 | 3392×5056 |
| 3:2 | 632×424 | 1264×848 | 2528×1696 | 5056×3392 |
| 5:4 | 576×464 | 1152×928 | 2304×1856 | 4608×3712 |
| 21:9 | 792×336 | 1584×672 | 3168×1344 | 6336×2688 |
| 1:4 | 256×1024 | 512×2048 | 1024×4096 | 2048×8192 |
| 4:1 | 1024×256 | 2048×512 | 4096×1024 | 8192×2048 |
| 1:8 | 192×1536 | 384×3072 | 768×6144 | 1536×12288 |
| 8:1 | 1536×192 | 3072×384 | 6144×768 | 12288×1536 |

Nano Banana Pro produces the same pixel dimensions for the ten ratios it supports, but has **no 512px tier and none of the four extreme ratios**.

**Two API gotchas worth internalising:**

1. `image_size` **must be uppercase K**. The doc is explicit: "You must use an uppercase 'K' (e.g. 512px, 1K, 2K, 4K). Lowercase parameters (e.g., 1k) will be rejected."
2. Default behaviour when you set nothing: "the model matches the output image size to that of your input image, or otherwise generates 1:1 squares." So an image-to-image edit silently inherits the input's ratio. If you want a different ratio out of an edit, you must say so *and* handle the recompose (see §11).

**Provenance.** The Gemini API doc states only: "All generated images include a SynthID watermark." The word C2PA appears zero times in that page. Google Cloud's enterprise blog separately claims "C2PA content credentials and imperceptible SynthID watermarks are enabled by default." **Verdict: SynthID is certain and universal; C2PA is real but appears to be surface-dependent (Vertex / consumer app), not guaranteed on every API path.** Do not build a compliance claim on C2PA without checking your specific surface.

**Language support.** Best performance is officially limited to: EN, ar-EG, de-DE, es-MX, fr-FR, hi-IN, id-ID, it-IT, ja-JP, ko-KR, pt-BR, ru-RU, ua-UA, vi-VN, zh-CN. (`ua-UA` is reproduced as Google prints it; the correct ISO code for Ukrainian is `uk-UA`. It is Google's typo, not this document's.)

---

## 2a. What it costs, and how fast it is

Prompting strategy is partly an economic question — the "draft cheap, finish expensive" workflow in §17.6 only makes sense if you know the actual spread. These are Gemini API list prices from Google's pricing page. **There is no free tier for any image model.** The Batch API halves everything.

| Model | Resolution | Output tokens | $/image standard | $/image batch |
|---|---|---|---|---|
| `gemini-3.1-flash-image` (NB2) | 0.5K | 747 | **$0.045** | $0.022 |
| | 1K | 1,120 | $0.067 | $0.034 |
| | 2K | 1,680 | $0.101 | $0.050 |
| | 4K | 2,520 | **$0.151** | $0.076 |
| `gemini-3-pro-image` (Pro) | 1K–2K | 1,120 | $0.134 | $0.067 |
| | 4K | 2,000 | $0.24 | $0.12 |
| `gemini-3.1-flash-lite-image` (Lite) | 1K | 1,120 | **$0.0336** | $0.0168 |

**Input side**, per 1M tokens: NB2 $0.50, Pro $2.00, Lite $0.25. An input image is 560 tokens, so attaching a reference to a Pro call costs about $0.0011 — reference images are essentially free relative to the output. Attach them liberally.

**Text and thinking output**, per 1M tokens: NB2 $3.00, Pro $12.00, Lite $1.50. This is the number that matters for §3: **thinking tokens bill at the text-output rate, not the image rate.** Raising `thinking_level` to `high` does not multiply your image cost; it adds a text charge on top of it. On NB2 that charge is small in absolute terms, which is why "raise thinking when the prompt gets structurally complex" is cheap advice to follow.

Pro additionally offers **Flex** pricing (identical to the batch column) and **Priority** ($3.60 input / $21.60 text output / $216.00 image output per 1M).

**Practical consequences.**

- A 4K NB2 render costs about **3.4× a 512px draft**. Eight drafts at 512px cost less than two-and-a-half finals at 4K. The exploration-then-upscale workflow isn't fastidiousness, it's arithmetic.
- Lite at $0.0336 is roughly **half** NB2's 1K price and **a quarter** of Pro's — genuinely the volume tier, provided you can live without grounding, character slots and style slots.
- Pro at 4K is **$0.24**, over 1.5× NB2 at the same resolution. Reserve it for what it's actually better at: dense text, complex layout, style references.
- Batch halves everything. If your work is not interactive — overnight variant generation, catalogue passes — batch is free money.

**Latency.** Google publishes a figure for exactly one model: Lite, described as **"sub-2 second end-to-end latency."** No published latency figures exist for NB2 or Pro, and anyone quoting one is guessing. Directionally, Pro with default deep reasoning is the slowest of the three, and NB2 at `thinking_level: high` is slower than at `minimal` — but treat any specific number you see as unverified.

---

## 3. Thinking: what it is, what it costs, how it changes your prompt

This is the single most misunderstood part of the model, and two "contradictory" claims in circulation are actually both true.

**Fact 1:** "Gemini 3 image models are thinking models that use a reasoning process ('Thinking') for complex prompts. This feature is enabled by default and **cannot be disabled** in the API."

**Fact 2:** "With Gemini 3.1 Flash Image and Gemini 3.1 Flash Lite Image, you can control the **amount** of thinking... The default `thinking_level` is `minimal`, and the supported levels are `minimal` and `high`."

So: you cannot turn thinking off, but on NB2 you can dial it between `minimal` and `high`. Nano Banana Pro does **not** expose `thinking_level` at all — its reasoning is always implicit and always full.

What thinking physically does: "The model generates up to two interim images to test composition and logic. The last image within Thinking is also the final rendered image." Those interim "thought images" are not charged. **Thinking text tokens are billed** regardless of whether you look at them.

### Consequences for prompt writing

This is where the practical payoff is:

- **The model reasons about your intent before drawing.** So stating *purpose* is a legitimate, high-leverage instruction. Google's own best-practice text: *"Explain the purpose of the image... 'Create a logo for a high-end, minimalist skincare brand' will yield better results than just 'Create a logo.'"* One clause of context can replace ten clauses of technical specification, because the model derives the technical implications itself.
- **Raise `thinking_level` to `high`** when the prompt contains layout logic, multiple text elements, several reference images, numerical/factual content, or any "A must be to the left of B" spatial constraint. Leave it at `minimal` for a single-subject render where speed matters.
- **Verbose, grammatical prose beats keyword soup.** Because the reasoning stage parses your prompt as language, a comma-salad of tags is read as literal content, not as weights.

---

## 4. The one architectural fact that invalidates most of your instincts

Nano Banana 2 is **an autoregressive multimodal LLM that emits image tokens**. It is *not* a diffusion model with a CLIP text encoder. Everything you learned prompting Stable Diffusion, SDXL, or Midjourney is either neutral or actively harmful here.

**Specifically, these do not work and should be deleted from your prompts:**

| Diffusion habit | What NB2 does with it | Confidence |
|---|---|---|
| Weighted tokens: `(neon:1.4)`, `[blurry:0.6]` | Reads the punctuation and numbers as literal scene content | High |
| `::` separators, `--ar 16:9`, `--stylize 250` and other CLI flags | Treated as text — may even try to *render* them | High |
| Quality boosters: `masterpiece, 8k, trending on artstation, ultra detailed, award winning` | Adds nothing; dilutes attention across meaningless tokens | High |
| Tag soup: `dog, park, sunset, 4k, realistic, bokeh` | Named as an anti-pattern in Google AI's own developer write-up: *"stop using 'tag soups'"* | High (semi-official — Google AI DEV post, not the API reference) |
| A trailing `Avoid: blurry, deformed hands, extra fingers, watermark` | Injects those concepts into context. At best inert, plausibly harmful | Medium-high |
| `steps`, `guidance_scale`, `cfg`, `denoising_strength`, `seed` in a JSON blob | **These parameters do not exist.** "Denoising steps" is definitionally meaningless for an autoregressive model | High |

**The replacement mental model:** you are writing a **creative brief for a competent art director**, not a query for a search index. Full sentences. Proper grammar. Named intent. Concrete nouns.

The before/after below is quoted verbatim from Google AI's developer write-up on prompting the Nano Banana models — an official Google channel, but a blog post rather than the API reference, so treat it as semi-official:

> ❌ **Bad:** "Cool car, neon, city, night, 8k."
> ✅ **Good:** "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. The neon signs reflect off the wet pavement and the car's metallic chassis."

---

## 5. The official core principles

Seven rules, stated by Google across the Cloud blog, the API docs and the DeepMind guide. The first four are the ones Google leads with; they are boring and they are correct.

**1. Be hyper-specific.** *"Instead of 'fantasy armor,' describe it: 'ornate elven plate armor, etched with silver leaf patterns, with a high collar and pauldrons shaped like falcon wings.'"* Specificity is control. Every adjective you don't supply is one the model invents.

**2. Use positive framing.** Google calls this "semantic negative prompts": *"Instead of saying 'no cars,' describe the intended scene positively: 'an empty, deserted street with no signs of traffic.'"* Describe the state you want the world to be in, not the thing you're forbidding.

**3. Control the camera.** *"Use photographic and cinematic language to control the composition. Terms like wide-angle shot, macro shot, low-angle perspective."* The model has learned photographic semantics deeply — a real lens spec resolves a dozen downstream ambiguities in one phrase.

**4. Iterate conversationally, don't re-roll.** *"If an image is 80% correct, do not generate a new one from scratch."* Follow-ups like *"That's great, but can you make the lighting a bit warmer?"* are cheaper and preserve everything you already liked.

Three more that are equally load-bearing but less often quoted:

**5. Provide context and intent.** Covered in §3. *"Create an image of a sandwich for a Brazilian high-end gourmet cookbook"* — the model infers professional plating, shallow depth of field, and studio lighting on its own.

**6. Use step-by-step instructions for complex scenes.** *"First, create a background of a serene, misty forest at dawn. Then, in the foreground, add a moss-covered ancient stone altar. Finally, place a single, glowing sword on top of the altar."* Sequencing the build order is a real compositional control, not a stylistic quirk.

**7. Start with a strong verb.** Google Cloud: *"The key is to start a prompt with a strong verb that tells the model the primary operation you want to perform."* — `Create`, `Generate`, `Edit`, `Replace`, `Transform`, `Combine`, `Restyle`, `Extend`. This single word routes the model into the right operating mode.

---

## 6. Google's official prompt frameworks

These are the canonical formulas. Memorise the first one.

### 6.1 Text-to-image (the master formula)

```
[Subject] + [Action] + [Location/context] + [Composition] + [Style]
```

Google's own worked example, annotated:

> **[Subject]** A striking fashion model wearing a tailored brown dress, sleek boots, and holding a structured handbag. **[Action]** Posing with a confident, statuesque stance, slightly turned. **[Location/context]** A seamless, deep cherry red studio backdrop. **[Composition]** Medium-full shot, center-framed. **[Style]** Fashion magazine style editorial, shot on medium-format analog film, pronounced grain, high saturation, cinematic lighting effect.

DeepMind's official guide expresses the same idea as five axes with slightly different names — **Style, Subject, Setting, Action, Composition** — and frames each as a question to answer:

- *Style* — "Are you creating an illustration, a photograph – or a watercolor painting?"
- *Subject* — "Who, or what, is in your image? What do they look like? What are they wearing? How are they posed?"
- *Setting* — "Where does your scene take place?"
- *Action* — "What's happening? Is something falling? Floating?"
- *Composition* — "Portrait or landscape? Is it an extreme close-up, a wide shot, a low angle shot?"

blog.google's version adds a sixth for edit turns: **Subject, Composition, Action, Location, Style, Editing Instructions.**

They are the same framework. Use whichever ordering you like — the model doesn't care about order nearly as much as it cares about *coverage*. Missing axes get invented.

### 6.2 Generation with reference images

```
[Reference images] + [Relationship instruction] + [New scenario]
```

> "Using the attached napkin sketch as the structure and the attached fabric sample as the texture **[References]**, transform this into a high-fidelity 3D armchair render **[Relationship]**. Place it in a sun-drenched, minimalist living room **[New Scenario]**."

The "relationship instruction" is the part people skip and it's the part that matters. Don't just attach images — say what role each one plays.

### 6.3 Grounded / real-time generation

```
[Source/Search request] + [Analytical task] + [Visual translation]
```

> "**[Search for current weather and date in San Francisco]** + **[Analytically, use this data to modify the scene (e.g., if raining, make it look grey and rainy)]** + **[Visualize this in a miniature city-in-a-cup concept embedded within a realistic, modern smartphone UI]**"

### 6.4 The official API templates, verbatim

These come straight from `ai.google.dev/gemini-api/docs/image-generation`. Treat them as fill-in-the-blank.

**Photorealistic scenes**
> "Describe a scene in rich detail. The more specific you are, the more control you have over the results."
```
A photorealistic [type of shot] of a [subject description] in a [setting
description]. [Description of the light]. Shot from a [camera angle]
with a [lens type].
```

**Stylized illustrations & stickers**
> "Describe the artistic style, subject, and medium. Be specific about the visual detail (bold lines, colors, etc.) for consistent results."
```
A [style] of a [subject, with details about accessories or actions]
doing [activity]. The design features [visual qualities, e.g., bold outlines,
cel-shading, etc.] and [color/background preference].
```

**Accurate text in images**
```
Create a [image type] for [brand/concept] with the text "[text to render]"
in a [font style]. The design should be [style description], with a
[color scheme].
```

**Product mockups & commercial photography**
> "Perfect for creating clean, professional product shots for ecommerce, advertising, or branding."
```
A high-resolution, studio-lit product photograph of a [product description]
on a [background surface/description]. The lighting is a [lighting setup,
e.g., three-point softbox setup] to [lighting purpose]. The camera angle is
a [angle type] to showcase [specific feature]. Ultra-realistic, with sharp
focus on [key detail]. [Aspect ratio].
```

**Minimalist & negative space design**
> "Excellent for creating backgrounds for websites, presentations, or marketing materials where text will be overlaid."
```
A minimalist composition featuring a single [subject] positioned in the
[bottom-right/top-left/etc.] of the frame. The background is a vast, empty
[color] canvas, creating significant negative space. Soft, subtle lighting.
[Aspect ratio].
```

**Sequential art / comic panel / storyboard**
```
Make a 3 panel comic in a [style]. Put the character in a [type of scene].
```

**Adding / removing elements (editing)**
```
Using the provided image of [subject], please [add/remove/modify] [element]
to/from the scene. Ensure the change is [description of how the change should
integrate].
```

**Inpainting via semantic masking**
```
Using the provided image, change only the [specific element] to [new
element/description]. Keep everything else in the image exactly the same,
preserving the original style, lighting, and composition.
```

**Style transfer**
```
Transform the provided photograph of [subject] into the artistic style of
[artist/art style]. Preserve the original composition but render it with
[description of stylistic elements].
```

**Multi-image composition**
```
Create a new image by combining the elements from the provided images. Take
the [element from image 1] and place it with/on the [element from image 2].
The final image should be a [description of the final scene].
```
> Example: *"Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."*

**High-fidelity detail preservation** — the most useful template in the whole doc for product work:
```
Using the provided images, place [element from image 2] onto [element from
image 1]. Ensure that the features of [element from image 1] remain
completely unchanged. The added element should [description of how the
element should integrate].
```
> Example: *"Take the first image of the woman with brown hair, blue eyes, and a neutral expression. Add the logo from the second image onto her black t-shirt. Ensure the woman's face and features remain completely unchanged. The logo should look like it's naturally printed on the fabric, following the folds of the shirt."*

---

## 7. Prompting like a creative director — the four control levers

Google's framing: "stop typing keywords and start directing the scene." These four levers, used together, are the difference between a stock-looking image and a shot.

### 7.1 Lighting

Name the *setup*, not the mood.

| Instead of | Say |
|---|---|
| "good lighting" | "three-point softbox setup, key light camera-left at 45°, subtle rim light separating the subject from the background" |
| "dramatic" | "chiaroscuro lighting with harsh, high contrast, single hard source, deep falloff into black" |
| "warm" | "golden hour backlighting creating long shadows, warm rim on the subject's hair, lens flare from the low sun" |
| "soft" | "overcast north-facing window light, large diffuse source, no visible catchlight hotspot" |

Other genuinely useful named setups: `Rembrandt lighting`, `butterfly/beauty lighting with a reflector below`, `split lighting`, `high-key on a white sweep with the background blown to pure white`, `low-key with a single practical in frame`, `hard direct on-camera flash, harsh shadow behind the subject`, `bounced light off a warm brick wall`, `neon practicals as the only source`.

### 7.2 Camera, lens, focus

**Naming real hardware changes the visual DNA of the image.** Google's prompt guide makes this point and supplies the first three examples below; the rest are added here from practice:

- *GoPro* → immersive, wide, barrel-distorted, action feel
- *Fujifilm* → its specific colour science
- *Cheap disposable camera* → raw, nostalgic, direct-flash aesthetic
- Add: *iPhone 15 Pro* (clean computational look), *Hasselblad medium format* (huge tonality, shallow falloff), *Canon 5D + 50mm f/1.2* (classic portrait), *security camera / CCTV* (low-res, timestamp, fisheye), *webcam* (soft, noisy, front-lit), *drone* (top-down, geometric)

Lens language that reliably lands:
- `"low-angle shot with a shallow depth of field (f/1.8)"` — forces perspective *and* separation
- `"wide-angle lens"` / `"14mm"` — for scale and environment
- `"macro lens"` / `"100mm macro at 1:1 magnification"` — for texture and product detail
- `"85mm portrait compression"` — flattering facial geometry
- `"tilt-shift"` — miniature effect
- Shot scale is its own lever: `extreme close-up`, `close-up`, `medium shot`, `medium-full`, `full body`, `wide`, `extreme wide`, `over-the-shoulder`, `Dutch angle`, `top-down flat lay`, `worm's eye`, `aerial`

### 7.3 Colour grading and film stock

*"The texture and color of the final image set the emotional tone."*

- Nostalgic/gritty: *"as if on 1980s color film, slightly grainy"*
- Modern moody: *"cinematic color grading with muted teal tones"*
- Named stocks that carry real meaning: `Kodak Portra 400` (warm, forgiving skin), `Kodak Gold 200` (nostalgic, yellow-warm), `Fuji Velvia` (saturated, punchy), `CineStill 800T` (tungsten-blue, halated highlights), `Ilford HP5` (grainy black and white)
- Grade vocabulary: `crushed blacks`, `lifted matte shadows`, `split-toned`, `desaturated with one accent colour`, `high-contrast bleach bypass`

### 7.4 Materiality and texture

*"Don't just ask for a suit jacket; ask for 'navy blue tweed.'"*

This is the cheapest quality upgrade available. Every physical object in your scene should have a named material: `brushed anodised aluminium`, `matte recycled kraft board with a visible fibre grain`, `hand-thrown stoneware with an uneven glaze pool`, `wet-look patent leather`, `frosted borosilicate glass`, `raw linen with a slub weave`, `soft-touch matte plastic with faint fingerprints`.

---

## 8. Text rendering

Both Gemini 3 image models are strong here; Pro is the strongest. Google describes the family as offering "state-of-the-art multilingual text generation in over 10 languages."

**The official rules:**

1. **Enclose your desired words in quotes.** `"Happy Birthday"`, `"URBAN EXPLORER"`. Non-negotiable — it's how the model separates literal strings from scene description.
2. **Describe the typography, or name the font.** *"a bold, white, sans-serif font"* or *"Century Gothic 12px font"* or *"neon cursive signage"*.
3. **Localise by instruction.** "Write your prompt in one language and specify a target language for the text output." For exact wording, supply the translated string yourself in quotes.
4. **The text-first hack** — stated twice in Google's docs, so take it seriously: *"When generating text for an image, Gemini Image models work best if you first converse with it to generate the text concepts, and then ask for an image with that text."* Two turns: (a) "give me three headline options for X", (b) "now make the poster using option 2."

**Google's own multi-element example, showing the pattern of one typographic spec per line:**

> "A high-end, glossy commercial beauty shot of a sleek, minimalist nude-colored face moisturizer jar resting on a warm studio background. The lighting is soft and radiant. Next to the product, render three lines of text with the following exact styling: For the top line, the word 'GLOW' in a flowing, elegant Brush Script font. For the middle line, the text '10% OFF' in a heavy, blocky Impact font. For the bottom line, the text 'Your First Order' in a thin, minimalist Century Gothic font."

**Community additions** (medium-high confidence, consistent across independent sources):

- **Cap yourself at 3–5 discrete text elements per image.** Accuracy collapses past that. If strings are coming back misspelled, drop to three or fewer — that's the recovery number, not the working limit (§14).
- **Keep each string short.** Under about five words per string is where reliability lives.
- **Reserve the space first.** Describe the negative space or text plate as part of the composition, so the layout isn't retrofitted around the type.
- **For 100% accuracy, go hybrid.** Generate the composition with placeholder or no text, then overlay real type programmatically. This is what professionals actually do and no amount of prompting beats it. Google's own admitted limitation: the model "can still struggle with... accurate spelling."

A worked example of the multi-element pattern done well:

> "A bold headline at the top of the frame reads 'FUTURE STACK 2026' in a thick condensed sans-serif, with a smaller subtitle directly below in a light italic serif reading 'The AI Creators Summit', and a thin line at the bottom left in all caps reading 'SAN FRANCISCO · JUNE 10-12'."

---

## 9. Reference images and consistency

### 9.1 The slot budget

Fourteen images total, but the *slots are typed* and the typing matters:

- **NB2:** 10 object slots + 4 character slots
- **Pro:** 5 object slots + 5 character slots + 3 style slots
- **Lite:** 14 object slots, nothing else

If you need three style references, you need Pro. If you need many product objects held with high fidelity, NB2 or Lite. If you need five people to stay consistent, Pro.

Official limitation text: *"gemini-3-pro-image supports 5 images with high fidelity, and up to 14 images in total. gemini-3.1-flash-image supports character resemblance of up to 4 characters and the fidelity of up to 10 objects in a single workflow."*

### 9.2 Name your references — this is the single highest-value consistency technique

DeepMind, verbatim: *"Upload clear reference images, and assign a distinct name to each character or object in your prompt. That way, the model can follow along and maintain their look as you build out your scenes."*

In practice this means writing things like:

> "Reference 1 is MAYA. Reference 2 is the PRODUCT BOX. Reference 3 is the KITCHEN. Place MAYA in the KITCHEN holding the PRODUCT BOX at chest height, angled so the printed lid faces camera."

Without named references, multi-reference prompts suffer **attribute bleed** — the model smears traits from one reference onto another. Naming is the fix — Google's own multi-image composition template does it, and community sources report the same thing consistently.

A lighter version of the same trick, for when you don't want to name things: refer to them positionally — *"the person in the first image," "the car in the second image."*

### 9.3 Identity locking

The phrase that recurs across Google's own developer guide and community testing:

> "Keep the person's facial features exactly the same as Image 1."

And Google's high-fidelity template phrasing:

> "Ensure that the features of [element from image 1] remain **completely unchanged**."

### 9.4 Anchor strings for text-only consistency

When you have no reference image, consistency comes from **reusing an identical descriptive block, word for word**, in every generation. Not "the same woman" — a fixed 10–20 word string:

> *"a woman in her early 30s, dark curly shoulder-length hair, visible pores, subtle freckles, and natural skin grain"*

Copy-paste it character for character. Paraphrasing it breaks the anchor.

### 9.5 Drift, and how to stop it

The most reliable community finding, high confidence: **after roughly three to four sequential edits, quality and identity drift**. The fix is to **re-anchor to the original generation, not to the most recent output**. Feed generation #1 back in as the reference, apply the accumulated change set in one prompt, and start a fresh chain.

Also useful: **pseudo-code variable binding** — a community technique, not a documented feature — for stopping attributes smearing across objects:

> "Define SHAPE_X as a tall cylindrical tower with ribbed sides. Define TEXTURE_Y as frosted glass. Create an illustration where SHAPE_X incorporates TEXTURE_Y across its full surface."

Binding an attribute to a named token *before* you use it prevents the model from applying it to everything in the frame.

---

## 10. Structural / layout control

Two techniques worth having in your pocket.

**Logical layout anchors.** Treat canvas regions as semantic zones and say so explicitly: *"The logo always sits in the footer, centred, at 8% of frame height. The headline occupies the top third. The product occupies the centre 50% of the frame with clear space on all sides."* The reasoning stage respects declared spatial constraints far better than diffusion models did.

**Sketch/wireframe as skeleton.** Upload a rough sketch, wireframe, or a grid as a reference image and describe the render that should sit on top of it. The model respects the geometry. This is the most reliable way to get an exact layout — you draw the boxes, it fills them.

**Multi-output asks.** DeepMind: *"Ask for 'three distinct variations of a product mock up' or 'four different color palettes' to quickly compare ideas side-by-side."* Note the admitted limitation: *"The model won't always follow the exact number of image outputs that the user explicitly asks for."*

---

## 11. Editing and inpainting

There is **no brush and no mask** in the Gemini API — masking is *semantic*, done purely in language. (Higgsfield does add a real mask input; see §15.) So preservation is entirely a prompting problem.

**The three mechanics that make edits stick:**

**1. Enumerate what is preserved, specifically.** "Keep everything else the same" is weaker than naming the elements. The best-constructed community template:

> *"Preserve the face, sitting position, and natural window lighting exactly as they are. Replace the denim jacket with a fitted charcoal knit sweater with visible ribbed texture. **No other changes.**"*

**2. Close the door with a terminal constraint.** `"No other changes."` as the final sentence reliably improves compliance. (Medium-high confidence; consistent across independent community sources, but no controlled public test exists.)

**3. One edit per call.** Stacking several changes into one prompt causes the model to silently drop some. For complex revisions, chain single edits — and remember the drift rule from §9.5.

**Changing aspect ratio during an edit.** Because an edit inherits the input's ratio by default, use an explicit recompose instruction. DeepMind's own recipe, repeated across ratios:

> *"change aspect ratio to 1:1 by reducing background. The character remains exactly locked in its current position"*

Say whether you want the extra canvas *outpainted* or the existing frame *cropped*, and state that the subject must not move.

**The five editing levers** (DeepMind's official taxonomy) — useful as a checklist for what's actually editable:

- **Change the character** — swap the subject, add characters, keep style/setting/composition
- **Adjust the composition** — new angle on the same subject and setting, generating detail only visible from the new perspective
- **Alter the action** — change pose or activity
- **Swap the setting** — whole backdrop or individual features and textures
- **Rethink the style** — reinterpret between photographic, illustration, cartoon, or a specific art style

---

## 12. Search grounding (NB2's genuine differentiator)

Two distinct capabilities, and third-party guides get this wrong in both directions:

- **Web Search grounding** — supported on **both** Nano Banana 2 and Nano Banana Pro. Not on Lite.
- **Google *Image* Search grounding** — **Nano Banana 2 only.** Official note: *"This feature is only available for the Gemini 3.1 Flash Image model."* It "allows models to use web images retrieved via Google Image Search as visual context for image generation."

Enable via `"search_types": ["web_search", "image_search"]`.

**Three things to know:**

1. With plain Web Search grounding, *"image-based search results are not passed to the generation model and are excluded from the response"* — you get facts, not visuals. Image Search grounding is what gets you visuals.
2. **Display obligation:** *"When you use Image Search within Grounding with Google Search, you must display the `search_suggestions` from the `google_search_result` step."* This is a terms requirement, not a suggestion.
3. Limitation: *"gemini-3.1-flash-image Grounding with Google Search does not support using real-world images of people from web search at this time."*

Prompt pattern: retrieve → analyse → visualise (§6.3). Example: *"Make a simple but stylish graphic of last night's Arsenal game in the Champions League."*

Grounding is also the workaround for the **January 2025 knowledge cutoff** — anything newer than that, the model only knows if you ground it.

---

## 13. Negative prompting without a negative prompt field

There is no `negative_prompt` parameter anywhere in the Gemini image API, and no Higgsfield equivalent. Four things actually work:

**1. Positive restatement (Google's "semantic negative prompts").** Describe the desired state of the world.
- ❌ "no clutter" → ✅ "a clean seamless white sweep, zero props"
- ❌ "no cars" → ✅ "an empty, deserted street with no signs of traffic"

**2. Absolute scene facts.** Phrases like *"zero text anywhere in the frame,"* *"no logos or branding of any kind,"* *"an empty room"* work because they assert a property of the scene rather than issue a prohibition. Excluding **text** specifically is the most reliable exclusion — the model appears to have a discrete text-rendering pathway it can switch off.

**3. Preservation lists + "No other changes."** (§11.)

**4. One instruction at a time**, so there's nothing available to drop.

**What does not work:** an SDXL-style avoid-tail (`Avoid: blurry, low quality, deformed hands, extra fingers, watermark`). At best it's inert; the architectural argument that it *injects* those concepts is strong, and community reports of summoning-the-thing are consistent with it. Delete these from your prompts. (Medium-high confidence — no controlled public test exists either way.)

---

## 14. Failure modes and fixes

| Symptom | Fix | Confidence |
|---|---|---|
| Output looks generic / stock | Add intent + audience ("hero image for a DTC skincare landing page"), and name materials for every object | High |
| Plastic, waxy, airbrushed skin | Request named imperfections: "visible pores, subtle freckles, natural skin grain, slight flyaway hairs" | High |
| "Too clean to be real" | Ask for *specific* physical imperfections: "minor overexposure in bright areas and a subtle vignette as if taken with an aging compact camera," "slight handheld shake consistent with a hurried capture," "minor dust particles on the lens catching stray light" | High |
| Over-saturated / HDR look | Name a film stock, or "muted, slightly desaturated, natural contrast," plus "minor underexposure" | Medium |
| Aspect ratio ignored or drifting | Set the parameter **and** restate the ratio as a trailing sentence in the prompt text | Medium (Higgsfield officially advises this) |
| Unrequested text or fake watermarks appear | "zero text anywhere in the frame" as a positive scene fact | Medium-high |
| Attribute bleed between reference images | Name each reference, or refer to them positionally ("the person in the first image") | High |
| Attribute smearing across objects in one scene | Pseudo-code variable binding (§9.5) | Medium-high |
| Edit ignored, or unrelated things change | Split into single edits; enumerate preserved elements; end with "No other changes." | High |
| Identity drift over a sequence | Re-anchor to generation #1, not to the last output. Reset every 3–4 edits | High |
| Misspelled text | Shorten the string; reduce to ≤3 text elements; use the text-first two-turn hack; or overlay type programmatically | High (Google admits the limitation) |
| Wrong facts in an infographic/diagram | Verify manually. Google: "it may misinterpret information or produce factually incorrect results. Always verify data-driven outputs." | High (official) |
| Small faces in a crowd are mangled | Official known limitation — compose so no critical face is small, or generate the face separately and composite | High (official) |
| Day→night or heavy relight looks fake | Official known limitation on "major lighting changes" — regenerate rather than edit | High (official) |
| Wrong number of variations returned | Official limitation: "The model won't always follow the exact number of image outputs" — ask again or generate individually | High (official) |
| Prompt seems ignored on a complex layout | Break the prompt into ordered steps. On the direct API, also raise `thinking_level` to `high` — that knob is not available for `nano_banana_2` on Higgsfield, so there you compensate in the prompt text instead (§17.6) | High |

**Google's officially admitted limitations, verbatim, worth reading once.** These are drawn from Google's own limitations copy for the Gemini 3 image models — chiefly the DeepMind Nano Banana Pro model page and the Gemini API image-generation doc. They are stated for the family and hold for NB2 as well as Pro:

> "Not every image Gemini generates will be perfect – it can still struggle with small faces, accurate spelling, and fine details in images."
> "The model's real-world knowledge is extensive but not infallible... Always verify data-driven outputs."
> "It may struggle with grammar, spelling, cultural nuances, or idiomatic phrases."
> "Advanced features like masked editing, major lighting changes (like day to night), or blending multiple images may sometimes produce unnatural results, visual artifacts, or disjointed scenes."
> "The model excels at character consistency, but it may not always get it right."

---

## 14a. Safety filters and refusals

A blocked prompt looks like a failure, and people misdiagnose it constantly — rewriting the creative brief when the actual problem was a filter. Worth understanding the mechanics.

**Four adjustable categories.** Harassment, hate speech, sexually explicit, and dangerous content. Each takes a threshold: `OFF`, `BLOCK_NONE`, `BLOCK_ONLY_HIGH`, `BLOCK_MEDIUM_AND_ABOVE`, `BLOCK_LOW_AND_ABOVE`. The default is the surprising part — Google states: *"If the threshold is not set, the default block threshold is Off for Gemini 2.5 and 3 models."* So on a default API call the four adjustable filters are not the thing stopping you.

**What is always on, and cannot be adjusted:** *"the Gemini API has built-in protections against core harms, such as content that endangers child safety. These types of harm are always blocked and cannot be adjusted."* The Gemini 3 Pro Image model card enumerates six prohibited categories: CSAM and child exploitation, hate speech, dangerous content, harassment, sexually explicit material, and medical advice contrary to scientific consensus. No `safetySettings` value opens these.

**How to detect a refusal in code.** The response carries `promptFeedback.blockReason`. Its enum includes `SAFETY`, `OTHER`, `BLOCKLIST`, `PROHIBITED_CONTENT`, and — specific to this family — **`IMAGE_SAFETY`**, documented as *"Candidates blocked due to unsafe image generation content."* That last one is the tell that the *output* tripped a filter rather than the prompt. Note also: *"The content that was blocked is not returned"* — you get no partial image to inspect.

A robust detector treats a call as refused if any of these hold: `blockReason` is set, **or** zero candidates came back, **or** a candidate has a `finishReason` other than `STOP` and contains no inline image part. Checking only `blockReason` will miss cases; checking only for a missing image will misattribute network failures.

**No `person_generation` parameter.** Several guides tell you to set `person_generation: allow_adult` on Nano Banana. That parameter belongs to the separate **Imagen** endpoint (`dont_allow` / `allow_adult` / `allow_all`) and does not exist on the Gemini 3 image models. Sending it does nothing.

**Rights on uploaded references**, verbatim from Google: *"Make sure you have the necessary rights to any images you upload..."* The obligation sits with you, not the platform.

**What could not be verified**, and where you should test rather than assume:

- Whether `safetySettings` thresholds actually govern *image output* or only the text path. The `IMAGE_SAFETY` block reason implies a separate image-side classifier that the four categories may not reach.
- The documented policy on generating real, identifiable people and public figures. There is observable model behaviour here, but no policy statement this research could locate on a primary page.
- The policy on brand logos, trademarks, and copyrighted characters — same situation.
- The complete `FinishReason` enum.
- Whether Vertex AI's pricing or filter defaults differ from the Gemini API's. Do not assume the §2a numbers or the `OFF` default carry over to Vertex.

**Practical rule.** If a prompt refuses, first establish *whether* it refused (the detector above) before you touch the wording. If it did, the fix is almost never adjectival — rephrasing "a woman in a swimsuit" seventeen ways is wasted effort if the block came from an unadjustable category. Change the subject matter, or accept it isn't available.

---

## 15. Running Nano Banana 2 on Higgsfield

Higgsfield **does** publish a prompting guide — but it is for **Nano Banana Pro**, not Nano Banana 2. There is no NB2-specific guide; the NB2 pages are marketing. Their Academy "prompt bank" is video camera-move prompts, irrelevant here.

**What the Higgsfield Pro guide adds that Google doesn't say:**

- Their prompt skeleton is the same five slots: **Subject / Composition / Action / Location / Style**
- **State the aspect ratio numerically inside the prompt text**, not just in the parameter — explicitly framed as redundancy against composition drift
- **Strip conversational filler** — "remove polite phrases like 'please'"; write command-style
- **List failure modes explicitly** in the prompt (negative constraints written inline) — **adopt this one with care.** §4 and §13 argue an avoid-list is inert at best and concept-injecting at worst. Take Higgsfield's underlying point (name what tends to go wrong) but convert each item into a positive scene fact before it goes in the prompt.
- **Logical layout anchors** — canvas regions treated as semantic zones. This is the same technique as §10; Higgsfield's contribution is showing it applied at length in production prompts.
- **JSON-structured prompts with multiple input images**, including an explicit rules array, e.g. *"Do not describe their physical appearance / Do not modify their identity"*
- Pipeline positioning: use Nano Banana Pro for the **layout and logic stage** (who stands where, what text appears), then refine style elsewhere, then push to video

**The actual Higgsfield model catalogue** (read directly from their API, not from marketing pages):

| id | resolution param | aspect ratios | extra |
|---|---|---|---|
| `nano_banana` | none | 10 standard | image_references |
| `nano_banana_pro` | `1k`/`2k`/`4k`, **default 2k** | 10 standard, **no `auto`** | image_references |
| `nano_banana_2` | `1k`/`2k`/`4k`, **default 1k** | `auto` + 10 standard | image_references, **`mask`**, `is_inpaint` |
| `nano_banana_2_lite` | **1k only** | `auto` + 10 standard | `thinking`: MINIMAL/HIGH (**default HIGH**), mask, is_inpaint |
| `nano_banana_2_shots` | none | auto + standard | displayed as "Nano Banana Pro" — pin the id, not the name |

**Higgsfield-specific gotchas that change how you work:**

1. **`nano_banana_2` defaults to `1k`.** Pro defaults to `2k`. If you don't pass `resolution` explicitly you get a silent quality downgrade on NB2. Always pass `4k` for hero frames.
2. **Higgsfield adds a real `mask` input + `is_inpaint` flag** — a capability Google's API does not have. But it exists **only on `nano_banana_2` and `_lite`, not on `nano_banana_pro`.** So regional/masked editing forces you onto NB2. This is a genuine reason to prefer NB2 over Pro.
3. **`thinking` is exposed only on Lite** on Higgsfield, defaulting to HIGH — the inverse of Google's API default of `minimal`. You cannot dial reasoning on `nano_banana_2` or `nano_banana_pro` through Higgsfield, so all structure must come from prompt text.
4. **No seed parameter.** Higgsfield's own guide says "lock the seed for series consistency" — that advice is not actionable on their nano-banana endpoints. Consistency must come from re-feeding `image_references`.
5. **No reference-weight parameter**, despite their guide mentioning "assign specific weight values." Steer reference influence in prose instead ("keep the packaging exactly as in reference 1; treat reference 2 as lighting mood only").
6. **No negative_prompt field.** Their "negative constraints" advice means writing exclusions inline (§13).
7. **Soul ID does not work with nano banana.** `soul_id` exists only on the Soul models. For avatar consistency: generate identity in Soul, then carry it into nano banana as a reference image.
8. **`auto` aspect ratio exists on NB2/Lite but not on NB1/Pro** — useful for image-to-image where you want the input ratio preserved exactly.
9. The media role is `image_references`, not `image`. No documented max count on the nano-banana entries — treat Google's 14 as the practical ceiling.
10. Higgsfield's opinionated *image ad* path is `marketing_studio_image` / `ms_image` (requires a `style_id`, supports `brand_kit_id`, up to 4 `product_ids`, `batch_size` 1–20) — a different product from nano banana entirely.
11. **The extreme aspect ratios are not available here.** §2 lists `1:4, 4:1, 1:8, 8:1` as a real NB2 advantage on the Gemini API, but Higgsfield's `nano_banana_2` entry offers `auto` plus the ten standard ratios only. If you need a strip banner or a tall side rail at those proportions, generate the nearest standard ratio and crop, or go to the direct API.
12. **There is no 512px tier.** Higgsfield's cheapest NB2 rung is `1k`. The "draft at 512px" advice throughout this document is an API-path instruction; on Higgsfield, `1k` is your draft tier (§17.6).

---

## 16. Myths, debunked

Things widely repeated in blog posts that are false. Strip these from any prompt template you inherit.

**"Use this JSON schema with `steps`, `guidance_scale`, `seed`, `negative_prompt`, `denoising`, `strength`."** — Fabricated. None of these parameters exist in the Gemini image API. "Denoising steps" is meaningless for an autoregressive model. The widely-shared "Ultimate Image Schema" gist invents all of them, including per-reference `usage_type` enums like `face_id`, `pose_copy`, `depth_map` and a `strength` float. The model reads the JSON as plain text, ignores the fake knobs, and you get a small benefit from the *real* descriptive fields — which people then misattribute to the schema. **High confidence.**

**Does JSON prompting help at all?** Yes, but only as *organisation*, not as a magic mode. It's genuinely useful for batch repeatability (swap one field, hold the rest) and for team handoff. A defensible schema contains only semantic content fields:

```json
{ "goal": "", "subject": "", "context": "", "style": "", "composition": "",
  "lighting": "", "color_palette": "", "background": "", "camera_or_lens": "",
  "mood": "", "text_space": "", "scene_facts": [],
  "preserve": [], "change_only": "" }
```

Note what is **not** in that schema: there is no `negative_constraints` or `avoid` array. An avoid-list is inert at best and concept-injecting at worst (§4, §13), and wrapping it in a JSON field does not change that. `scene_facts` does the same job with *positive* assertions: `["empty street, no traffic", "zero text anywhere in the frame", "seamless white background, no props"]` — same intent, phrasing the model can act on.

**"92% vs 68% instruction precision", "40% faster iteration", "82% of prompt failures".** — No methodology exists anywhere for any of these. They propagate between SEO blogs. **High confidence unverifiable.**

**"Search grounding is Pro-only" / "Search grounding is NB2-only."** — Both wrong. Web search: both. Image search: NB2 only. (§12.)

**"Nano Banana 2 text rendering is basic and prone to errors, and it uses static training data."** — Wrong on both counts. NB2's text rendering is strong — close to Pro's, and nowhere near "basic" (Pro still leads on dense typographic layout, §8) — and NB2 is the *only* model with image-search grounding, so "static training data" is exactly backwards.

**"Thinking can be turned off on Gemini 3 image models."** — Half-true and worth stating precisely: thinking cannot be disabled; on NB2 and Lite only, its *level* can be set to `minimal` or `high`.

**Model IDs with `-preview`.** — Dead since 25 June 2026. Anything you copy from a pre-June-2026 tutorial will fail.

**"1M token context window."** — That's the DeepMind *model card* describing the underlying model. The **API surface** is 131,072 in / 32,768 out for NB2 and 65,536 / 32,768 for Pro. Use the API numbers.

---

## 17. The universal prompt structure

This is the deliverable. It synthesises Google's five-axis formula, the API templates, the creative-director levers, and the community's tested preservation and consistency phrasings into one general-purpose scaffold.

### 17.1 The eleven blocks

Write in **flowing natural-language prose**, not as a labelled list — but make sure every block that applies is *covered*. The block names below are a checklist for you, not literal text to type. (The exception is multi-reference work, where explicit labelling genuinely helps — see 17.4.)

```
1.  OPERATION      Strong opening verb + output type + medium.
2.  SUBJECT        Who/what, in concrete physical detail — named materials,
                   textures, garments, age, condition, expression.
3.  ACTION / STATE What is happening, or how the subject is posed.
4.  SETTING        Where. Surface, environment, background depth, props.
5.  COMPOSITION    Shot scale, camera angle, subject placement in frame,
                   negative space, and the aspect ratio stated in words.
6.  LIGHT          The named setup, direction, quality, and resulting shadows.
7.  CAMERA & OPTICS Body/format, lens, aperture, focus point, depth of field.
8.  STYLE & GRADE  Genre reference, film stock or colour grade, texture/grain.
9.  TEXT           Every string in "double quotes", each with its own
                   typographic spec and position. Or: "zero text in frame."
10. BUILD ORDER    For layered or compositional images: the order in which
                   elements should be constructed. "Start with X, then place
                   Y on top of it, then add Z behind both."
11. INTENT & CONSTRAINTS  What the image is FOR, plus preservation rules,
                   exclusions phrased positively, and technical specs.
```

**Why block 10 exists.** Because the model generates autoregressively, the order in which you describe a build is not cosmetic — earlier tokens condition later ones, so stating a construction sequence is a genuine compositional lever rather than stylistic garnish (§5, principle 6). It does nothing for a single-subject portrait, so skip it there. It matters a great deal for layered scenes, exploded diagrams, collages, stacked or nested objects, before/after panels, and anything where one element must sit demonstrably in front of, behind, or on top of another. Phrase it as a sequence of placements: *"Begin with the seamless white sweep. Place the open notebook flat at centre. Set the pen diagonally across the right-hand page. Add the coffee cup behind and to the left, partially cropped by the frame edge."* Left to itself the model will guess at depth ordering; told explicitly, it usually obeys.

### 17.2 The fill-in template

```
Create a [medium: photorealistic photograph / 3D render / flat vector
illustration / oil painting / product mockup] of [SUBJECT — concrete
physical description with named materials and textures].

[SUBJECT] is [ACTION or POSE], in [SETTING — surface, environment,
background, props, depth cues].

Composition: [shot scale] from a [camera angle], with the subject
[placement in frame] and [description of negative space]. [Aspect ratio
stated in words, e.g. "Vertical 9:16 format."]

Lighting: [named setup] from [direction], producing [quality of shadow
and highlight].

Shot on [camera body or format] with a [focal length] lens at [aperture],
focused on [key detail], giving [depth of field description].

Style: [genre or art-direction reference], graded like [film stock or
colour treatment], with [texture, grain, or finish].

Text: render "[EXACT STRING]" in [weight + family + case + colour],
positioned [where]. [Repeat per string, max 3–5 total.]
— or —
Text: zero text anywhere in the frame.

[Layered or compositional images only — build order:] Begin with
[base layer / surface]. Place [element] at [position]. Then add
[element] [in front of / behind / on top of] it.

This image is for [purpose and audience]. [Preservation rules if editing.]
[Exclusions phrased as positive scene facts.] [Aspect ratio + resolution.]
```

### 17.3 Worked example — the template filled in

> Create a photorealistic product photograph of a matte black insulated water bottle with a brushed stainless steel lid and a faint fingerprint on the shoulder. The bottle stands upright, slightly angled so the embossed logo catches the light, on a raw travertine slab with a single eucalyptus sprig lying to its left. The background is a warm off-white plaster wall about a metre behind, softly out of focus.
>
> Composition: medium close-up from a slightly low angle, product centred and occupying the middle 55% of the frame, with generous empty space along the top third for a headline. Vertical 4:5 format.
>
> Lighting: a large softbox key camera-left at 45 degrees with a white bounce card camera-right, producing a soft directional shadow falling to the right and a single clean specular highlight running down the lid.
>
> Shot on a Canon EOS R5 with a 100mm f/2.8 macro lens at f/5.6, focused on the embossed logo, with the background falling gently out of focus.
>
> Style: modern minimalist ecommerce hero, graded warm and slightly desaturated with lifted matte shadows, natural contrast and a gentle filmic rolloff in the highlights.
>
> Text: zero text anywhere in the frame.
>
> This image is the hero shot for a premium DTC drinkware landing page. Keep the surface finish matte with no plastic sheen. 4K, 4:5.

### 17.4 The multi-reference variant

When you attach reference images, switch to explicit labelling — this is the one place structure beats prose.

```
REFERENCES
  Reference 1 = [NAME]. Role: [subject identity / object to reproduce
                exactly / style only / lighting mood only].
  Reference 2 = [NAME]. Role: [...]
  Reference 3 = [NAME]. Role: [...]

RELATIONSHIP
  [Explicitly state what each reference contributes and what it must NOT
  contribute. e.g. "Use REF-2 for the packaging artwork only; ignore its
  lighting and background entirely."]

SCENE
  [Full scene description — blocks 2–8 of the universal structure.]

FIDELITY LOCKS
  The features of [NAME] must remain completely unchanged.
  Keep the printed artwork and text on [NAME] exactly as in Reference 2 —
  do not redraw, re-letter, or reinterpret it.

OUTPUT
  [Aspect ratio] · [Resolution] · [Purpose]
```

### 17.5 The edit variant

```
[VERB: Replace / Remove / Add / Restyle / Extend] [precise target element]
with [precise replacement].

PRESERVE EXACTLY: [enumerate — face, pose, hands, lighting direction,
background, colour grade, framing, the printed label, camera angle].

[If the edit implies a knock-on change, state it: "adjust the shadow under
the new object to match the existing key light from camera-left."]

No other changes.
```

### 17.6 Order of operations

The two paths diverge, because Higgsfield does not expose everything the Gemini API does. Steps 4–7 are identical either way; steps 1–3 are not.

**If you are calling the Gemini API directly:**

1. **Draft cheap.** `image_size: 512px` on `gemini-3.1-flash-image`, `thinking_level: minimal`, 4–8 variations. Explore here, not at 4K. At roughly $0.045 a draft versus $0.151 at 4K, exploring at the top tier costs you more than three times as much per look (§2a).
2. **Pick one.** Then iterate *conversationally* on that one. Never re-roll a prompt that's 80% right.
3. **Raise `thinking_level` to `high`** the moment layout logic, multiple text strings, or several references enter the prompt. Remember thinking tokens bill at the *text* output rate, not the image rate.

**If you are running on Higgsfield (§15):**

1. **Draft at `1k`.** Higgsfield's `nano_banana_2` offers `1k / 2k / 4k` only — there is no 512px tier to draft in, and it silently defaults to `1k` if you set nothing. `1k` is your cheap tier by default; set it explicitly anyway so the default never surprises you.
2. **Pick one**, then iterate conversationally — same as above.
3. **You cannot raise thinking on `nano_banana_2`.** Higgsfield exposes a `thinking` parameter on `nano_banana_2_lite` only. So for layout-heavy or multi-string-text work you compensate in the prompt rather than in the parameter: state the layout logic more explicitly, describe positions in absolute terms, and cut the number of text strings per pass. If a job genuinely needs deep reasoning, either run it through `nano_banana_pro` (which reasons hard by default and is the better text/layout model anyway) or take it to the direct API where `thinking_level` exists.

**Both paths, from here:**

4. **One change per edit turn.**
5. **Re-anchor to the original every 3–4 edits** to kill drift.
6. **Upscale the winner** to 2K or 4K last.
7. **Overlay critical type programmatically** if the copy has to be perfect.

### 17.7 Pre-flight checklist

Before you hit generate, check that you have:

- [ ] Opened with a strong verb naming the operation
- [ ] Given every object a **named material**, not just a name
- [ ] Stated shot scale, camera angle, and **aspect ratio in words** as well as in the parameter
- [ ] Named a **lighting setup**, not a mood
- [ ] Named a **camera/lens/aperture**, not "professional photography"
- [ ] Named a **film stock or grade**, not "cinematic"
- [ ] Put every literal string in **"double quotes"** with its own typographic spec, or said "zero text in frame"
- [ ] Stated the **purpose and audience** of the image
- [ ] Phrased every exclusion as a **positive scene fact**
- [ ] Deleted all diffusion residue: weights, `--flags`, `::`, quality boosters, `Avoid:` tails, tag soup
- [ ] For layered or compositional scenes: stated an explicit **build order** with depth relationships
- [ ] Set `resolution` explicitly (Higgsfield NB2 silently defaults to 1k)
- [ ] For edits: enumerated preserved elements and ended with **"No other changes."**
- [ ] Confirmed the model ID is a **live stable ID**, not a dead `-preview` one

---

## 18. Sources

**Primary — Google / DeepMind**

- [The ultimate Nano Banana prompting guide — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) (6 Mar 2026)
- [Nano Banana image generation — Gemini API docs](https://ai.google.dev/gemini-api/docs/image-generation)
- [Gemini 3.1 Flash Image model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image)
- [Gemini 3 Pro Image model page](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image)
- [Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) — §2a
- [Safety settings](https://ai.google.dev/gemini-api/docs/safety-settings) — §14a
- [`generateContent` API reference](https://ai.google.dev/api/generate-content) — `blockReason` / `IMAGE_SAFETY` enum, §14a
- [Gemini 3 Pro Image model card — DeepMind](https://deepmind.google/models/model-cards/gemini-3-pro-image/) — prohibited-use categories, §14a
- [How to create effective image prompts with Gemini Image — DeepMind](https://deepmind.google/models/gemini-image/prompt-guide/)
- [Gemini Image model family — DeepMind](https://deepmind.google/models/gemini-image/)
- [Gemini 3 Pro Image — DeepMind](https://deepmind.google/models/gemini-image/pro/)
- [Prompting tips for Nano Banana Pro — blog.google](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/)
- [Nano Banana Pro announcement — blog.google](https://blog.google/innovation-and-ai/products/nano-banana-pro/)
- [Bringing Nano Banana 2 to enterprise — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/bringing-nano-banana-2-to-enterprise)
- [Getting the most out of Nano Banana 2 — Google AI on DEV](https://dev.to/googleai/getting-the-most-out-of-nano-banana-2-502k)
- [Nano Banana Pro prompting guide: strategies — Google AI on DEV](https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n)

**Higgsfield**

- [Nano Banana Pro: High-Control Prompting & Templates](https://higgsfield.ai/nano-banana-pro-prompt-guide)
- [Nano Banana Pro: Expert Use Cases with Prompts](https://higgsfield.ai/blog/Nano-Banana-Pro-Expert-Use-Cases)
- [Nano Banana Pro is Here: Full Review with a Guide](https://higgsfield.ai/blog/Nano-Banana-Pro-is-Here-Full-Review-and-Guide)
- [Nano Banana Pro & Nano Banana 2](https://higgsfield.ai/nano-banana-intro)
- [Higgsfield API docs](https://docs.higgsfield.ai/docs)
- Higgsfield MCP `models_explore` — model catalogue read directly from the API, 10 Sep 2026

**Third-party, used with scepticism**

- [Nano Banana 2 Prompting Guide — Fliki](https://fliki.ai/blog/nano-banana-2-prompting-guide)
- [Nano Banana 2 prompt guide — invideo](https://invideo.io/blog/nano-banana-2-prompt-guide/)
- [Nano Banana 2 Prompt Guide — ImagineArt](https://www.imagine.art/blogs/nano-banana-2-prompt-guide)
- [Nano Banana 2 guide — Magnific](https://www.magnific.com/blog/nano-banana-2/)
- [Ultimate Nano Banana Pro Prompting Guide — Atlabs](https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image)
- [Nano Banana Prompt Guide — Leonardo.Ai](https://www.leonardo.ai/news/nano-banana-prompt-guide) *(comparison table found unreliable)*
- [Nano Banana 2 Prompt Guide — AIMLAPI](https://aimlapi.com/blog/banana-prompt-guid)
