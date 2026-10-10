# Seedance 2.5 — Complete Prompting Guide

**Research report.** Compiled 10 September 2026.
**Model under study:** ByteDance Seedance 2.5 — API model ID `dreamina-seedance-2-5-260628` on BytePlus ModelArk / Volcano Engine Ark. Announced 23 June 2026 at Volcano Engine FORCE; launched 31 July 2026.

---

## 0. Scope, method, and how to read this document

This report was assembled from three layers of evidence, kept deliberately separate because they do not always agree.

**Layer 1 — first-party.** Five BytePlus ModelArk documents were retrieved in full text: the Seedance 2.5 prompt guide (2607689, last updated 31 Aug 2026), the Seedance 2.5 tutorial (2607688, last updated 9 Sep 2026), the portrait-video / real-face compliance page (2608626), the Seedance 2.0 series prompt guide (2222480, which the 2.5 guide explicitly defers to for reference examples), and the Seedance-1.5-pro prompt guide (2168087, the only official source with a real voice-direction vocabulary). Two supporting pages were checked: the digital character library (2223965) and seedance-1.0-lite model effects (1553576). These pages are client-rendered, so plain HTTP fetching returns an empty shell; they had to be read through a JavaScript-executing browser. Anything sourced here is marked **OFFICIAL**.

**Layer 2 — Higgsfield.** Higgsfield's "Seedance 2.5: Complete Prompting Guide (Full Prompt Library)" (13 Aug 2026, ~67,600 characters) was read end to end. It is the single most substantial third-party artefact: ten prompt categories, each tested across multiple generations, with the platform settings used and a written rationale for each. Marked **HIGGSFIELD**.

**Layer 3 — practitioner and platform layer.** fal.ai's developer prompting guide, OpenArt's syntax guide, Dreamina/CapCut's own consumer guide, Replicate's model card, CometAPI, MindStudio's hands-on production review, and two GitHub prompt libraries (`stimQQ/awesome-seedance2.5-prompts`, `AtlasCloudAI/awesome-seedance-2.5-prompts-skills`). Marked **THIRD-PARTY**, and where a claim comes from someone who demonstrably ran the model rather than resold it, that is noted.

One methodological note that shapes everything below. Several widely-repeated "facts" about Seedance 2.5 trace back to the June FORCE announcement rather than to any shipped endpoint, and several official rules are stated once and then never demonstrated in ByteDance's own worked examples. Section 15 is a ledger of every such contradiction. Where the layers conflict, this report reports the conflict rather than picking a winner — but it does say which evidence is stronger and why.

There is also an official prompt-optimisation Skill, `sd25-pe`, published by ByteDance. It installs with:

```
npx --yes skills@latest add "https://arkdocs-en.tos-ap-southeast-1.volces.com/skills/" --skill sd25-pe --yes
```

and is invoked as `/sd25-pe + your prompt`. Direct retrieval of the underlying `SKILL.md` was attempted through every plausible path on that bucket and all returned `NoSuchKey` with directory listing denied, so its internal rules could not be inspected. The install command is documented here for completeness; its content is not represented in this report.

---

## 1. What Seedance 2.5 actually is

Seedance 2.5 is a single model that generates video **and its audio in the same pass** — ambience, foley, score, and spoken dialogue with lip movement are produced together, not layered afterwards. That one fact drives most of the prompting differences from earlier models: the prompt is not a description of pictures, it is a description of a *timeline* that has a sound track.

Around that core, four capabilities distinguish it from Seedance 2.0:

It accepts **up to 50 multimodal references** in one generation — images, videos, and audio simultaneously — against 2.0's 15. It understands **integer-second timestamps** as an addressing scheme, where 2.0 only understood "Shot 1 / Shot 2". It accepts **flexible aspect ratios** across the range [0.4, 2.5] and multi-view images, which 2.0 does not. And it exposes **region and frame-level editing** plus **video extension** as first-class task types rather than separate products.

### Verified specification table

| Property | Value | Confidence |
|---|---|---|
| Max duration | 4–30 s, or `-1` / `auto` for model-chosen duration | OFFICIAL, corroborated everywhere |
| Aspect ratios | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, `adaptive` | OFFICIAL |
| Input image ratio range | [0.4, 2.5] | OFFICIAL |
| Max references | 50 total = 30 images + 10 videos + 10 audio | OFFICIAL, corroborated by fal.ai |
| Video reference limits | 480p/720p, [2,30] s each (editing [4,30] s), ≤200 MB, FPS [24,60], total ≤30 s | OFFICIAL |
| Audio reference limits | wav/mp3, [2,30] s each, ≤15 MB, total ≤30 s | OFFICIAL |
| Image reference limits | jpeg/png/webp/bmp/tiff/gif/heic/heif, 300–6000 px, <30 MB | OFFICIAL |
| Request body | ≤64 MB | OFFICIAL |
| Output formats | mp4, mov (mov = H.264 + yuv444p + PCM) | OFFICIAL |
| Output resolution | **Disputed — see §15.1.** Official docs say 480p/720p/1080p (10-bit, H.265). Every hands-on tester reports a 720p ceiling. Marketing sites claim 4K. | CONTESTED |
| Native audio languages | 11: Chinese, English, Spanish, Indonesian, Malay, Thai, Arabic, Portuguese, Vietnamese, Japanese, Korean | OFFICIAL |
| Task record retention | 7 days | OFFICIAL |
| Video URL validity | 24 hours, max 100 downloads | OFFICIAL |
| Rate limits | Enterprise 600 RPM / 10 concurrent; individual 180 RPM / 3 concurrent | OFFICIAL |

Resolution pixel dimensions at 1080p: 16:9 = 1920×1080, 9:16 = 1080×1920, 21:9 = 2206×946.

---

## 2. The task taxonomy — and why it constrains your prompt before you write a word

Seedance 2.5 is not one endpoint with one prompt style. It is four task families, and the family you are in silently overrides parameters you thought you controlled.

**Text-to-video.** No assets. Full control of ratio and duration.

**First-frame / first-last-frame.** You supply `first_frame` and optionally `last_frame`. The model interpolates.

**Omni reference-to-video.** The broadest family, subdivided by ByteDance into three sub-types: pure **reference** (subject, style, motion, audio references drive a new generation), **edit** (you modify an existing video), and **extend** (you continue an existing video forward or backward).

**One-click creation and seamless transition.** Convenience modes layered on the above.

### Locked vs unlocked tasks — the rule that causes most silent parameter overrides

**OFFICIAL.** Certain task types are *locked*: they force `ratio=adaptive` and, in some cases, `duration=-1`, regardless of what you sent. Editing, first/last-frame, and extension are all locked — the output inherits geometry and length from the source asset. Reference generation, storyboards, and keyframe sequences are *unlocked*: your ratio and duration are honoured.

This matters because the model infers your task type from your *prompt wording*. ByteDance publishes the trigger keywords:

- **Editing triggers:** "edit video", "add", "insert", "remove", "delete", "modify", "replace", "change to"
- **Extension triggers:** "extend forward", "extend backward", "continue", "continue from", "extend the story"

So the word "add" in a purely descriptive sentence can flip your generation into locked edit mode and quietly discard your aspect ratio.

**The fix — `omni_reference_task_type`.** This parameter takes `auto` | `reference` | `edit` | `extend`. Setting it explicitly moves validation earlier in the pipeline and converts a class of confusing asynchronous failures (`InvalidParameter.TaskTypeMismatch`, `InvalidParameter.TaskTypeConstraint`) into immediate, legible errors. **Set it explicitly on every non-trivial call.** This is the single highest-leverage parameter in the API and it is easy to miss.

**THIRD-PARTY, measured (stimQQ, 8 Aug 2026):** `first_frame_url` / `last_frame_url` are **mutually exclusive** with `reference_*_urls`. Sending both is rejected outright, not silently ignored.

---

## 3. Assets — what they cost you and how to name them

### The referencing syntax problem

**OFFICIAL.** The 2.5 tutorial (2607688) says to reference assets as `@Image 1`, `@Video 1`, `@Audio 1`, numbered in upload order, and to "specify what each asset provides, such as appearance, action, or timbre, and what should not be referenced."

**OFFICIAL, but inconsistent.** The 2.5 *prompt guide* (2607689) writes the same references without the `@`, as `Image 1` and `Audio 1`, and uses angle brackets for assets: `<video1>`, `<2pic>`. This is a direct internal inconsistency, and it collides with the sound-marker convention where `<>` means sound effect (§8).

**THIRD-PARTY, split.** fal.ai, OpenArt, Dreamina and AtlasCloud all use `@Image1`. Replicate and CometAPI use `[Image1]`. No source explains the divergence; the most likely reading is that each platform normalises to its own convention before hitting the API.

**Practical recommendation.** Use `@Image 1` / `@Video 1` / `@Audio 1` when calling BytePlus/Ark directly — it is the convention in the more recently updated official page and the majority third-party convention. When calling through an aggregator, use whatever that aggregator's docs show. In all cases, **also name the asset's job in plain language in the same sentence**, because every source agrees the role assignment carries more weight than the token format.

### The reference idiom that actually works

**THIRD-PARTY (fal.ai), the most reusable line in the entire corpus:**

> `@Image1 controls only [identity, product design, clothing, or another invariant]. Do not copy [pose, background, lighting, camera angle, or text] from @Image1.`

The word **"only"** is load-bearing. OpenArt independently arrives at the same pattern (`@Image 1 defines … only`) and adds a nuance from ByteDance's own guidance: prefer saying which part of an asset to *use* rather than enumerating what to exclude — reserve blunt "do not" phrasing for captions, logos, watermarks, background music, and overall look.

### Don't max out the ceiling

Three independent sources converge on this and it is the most consistently repeated practical warning in the corpus.

**OFFICIAL** recommends 1–5 subjects for audio/video references (5–10 s each), 1–8 subjects for image references, ≤15 storyboard panels, ≤20 s videos for editing, and 1–5 reference images for video editing.

**OFFICIAL (2.0 guide, still applicable)** goes further and prescribes a *functional* asset strategy: four roles — character anchoring, scene tone-setting, camera-movement reference, rhythmic atmosphere — filled by roughly 4–5 assets total (1–2 character images, 1 scene image, 1 camera-movement video, 1 audio). It says explicitly: do not use the full asset limit.

**HIGGSFIELD**, from testing: "50 references is a ceiling worth using deliberately, not maxing out by default. A cluttered reference set with too many competing faces, props, or locations produces a less coherent result than a smaller, carefully chosen set."

**THIRD-PARTY (stimQQ):** attaching more assets *lowers* stability.

The one dissenting data point is worth noting: **MindStudio** ran a 50-image wardrobe stress test and reported identity held across outfit changes. So the ceiling is not a trap — but 50 competing *subjects* is different from 50 views of one subject.

### Don't let two references do the same job

**THIRD-PARTY (fal.ai).** A video reference carries camera path and rhythm; an image reference carries look and identity. Assigning both to the same aspect produces incoherence. Give each asset one job and say what that job is.

### The duplicate-object trap

**THIRD-PARTY (OpenArt).** Multiple angles of one product are frequently read as *several* products. The fix is an explicit count statement: *"All three images show one lamp. The video must contain only one lamp."* This generalises — see §11 on count locks.

---

## 4. The official prompt architecture

**OFFICIAL.** The 2.5 tutorial gives a compact formula:

> Organize the prompt in the order of **"subject + action/event + scene and environment + visual style + camera movement/shot cuts + sound"**; unnecessary parts may be omitted.

**OFFICIAL.** The 2.5 prompt guide gives the fuller three-part architecture, which is the one to build on:

**Part 1 — Asset Referencing** (reference-to-video only). State which asset supplies what.

**Part 2 — One-Sentence Summary.** Verbatim from the docs: *"Subject + Location + Event + Genre/Style + Camera movement…"* One sentence, the whole film in miniature.

**Part 3 — Detailed Plot Description.** Either a shot sequence or a timeline. Use timestamps (2.5) or "Shot N" (2.0-compatible). Per segment, describe visuals, camera movement, actions, dialogue, and sound effects.

**Part 4 — Additional Notes.** Persistent details that apply across the whole clip.

**OFFICIAL (2.0 guide), the advanced formula** — more granular, and the one to reach for on hard shots:

> **precise subject + action details + scene/environment + lighting & colour tone + camera movement + visual style + image quality + constraints**

**OFFICIAL.** On polarity: *"Use positive descriptions whenever possible. Negative constraints are supported for subtitles and audio control, such as 'no subtitles' and 'no BGM.'"* Note carefully what this says — negation is *sanctioned* for exactly two domains. It is not a blanket prohibition on negative constraints elsewhere, but it is the only place ByteDance guarantees they are honoured.

### The independently-derived structures

Four different parties, working separately, converged on strikingly similar section-based architectures. That convergence is itself evidence.

**HIGGSFIELD** (from testing ten categories): `GLOBAL STYLE → SCENE → CHARACTERS → LOCATION → FIRST FRAME AND BLOCKING → shot-by-shot breakdown → OPTICS → CAMERA → PHYSICS → LIGHTING → AUDIO`. Its stated rule: "Labeled sections outperform one continuous paragraph." And the diagnostic insight: "Skip a section and the output tends to fail in a specific, predictable way."

**fal.ai** (nine blocks): `FORMAT / REFERENCE ROLES / STARTING STATE / TIMELINE / CAMERA / CONTINUITY / AUDIO / ENDING STATE / CONSTRAINTS` — with the caveat to delete any section that isn't solving a real problem.

**Dreamina/CapCut** (eight parts): `format → subject → action → environment → camera → look → timing → audio and constraints`.

**stimQQ**: `subject → action → location → camera work → lighting → picture texture → sound`, with only the first two mandatory.

The common skeleton across all of them: **a global rule at the top, a timeline in the middle, a sound rule and a constraint block at the bottom.** Higgsfield states it most compactly: "one visual rule at the top, one sound rule at the bottom, and everything in between broken into shots."

---

## 5. Time control — timestamps and their rules

This is the capability that most distinguishes 2.5 from 2.0, and it has sharp edges.

**OFFICIAL rules:**

Timestamps operate at **1-second intervals** — whole seconds only. Written forms `0-3s` and `[1s-4s]` are both attested.

**Avoid gaps.** A timeline reading `0-3s… 5-6s…` leaves 3–5s undefined and the model fills it unpredictably.

**Do not use timestamps for high-frequency actions.** OpenArt sharpens this into the best available phrasing: *"Timestamps are also not a counter"* — "nods three times in one second" fails.

Three addressing modes are supported: intervals (`0-3s`), time-point control (an event at an instant), and relative time control.

**One action per range.**

**THIRD-PARTY (fal.ai), the most important insight about duration:**

> *"The 30-second setting only changes the available duration. It does not add more events to the prompt."*

Under-specified long clips do not become richer; they become "waiting, repetition, or slow motion." A 30-second generation needs roughly 5–8 defined beats, not one idea stretched thin. Higgsfield's tested prompts bear this out — its 30-second examples define five segments with per-second event tracks.

**THIRD-PARTY (fal.ai), the causality rule:** write **cause before reaction**, as separate actions — contact, resulting movement, sound, then reaction. Compressed into one sentence, reactions fire before their cause.

---

## 6. Camera language

**OFFICIAL vocabulary**, which the model is trained to recognise:

**Shot size:** extreme wide, wide, medium, medium close-up, close-up.

**Movement:** push in, pull out, pan, track, follow, orbit, dive, pull back, tilt up, handheld shake.

**Angle:** low angle, overhead, first-person.

**Techniques:** one-shot / long take, Hitchcock (dolly) zoom, aerial, FPV, bullet time, handheld, speed ramp.

**OFFICIAL rule for unusual terms:** use the form `[term + descriptive explanation]`. Niche cinematography vocabulary is unreliable alone; explain what it does.

**OFFICIAL (2.0 guide):** **only one movement type per shot.** Compound moves degrade.

**THIRD-PARTY (fal.ai), the sharpest camera advice in the corpus:** give the camera a **screen-space position**, not just a move, and tie each move to a visible event. *"The word 'dynamic' is close to useless here."*

**HIGGSFIELD** demonstrates the extreme version, and it works: lens locks stated as diagonal field of view per segment (`84°` wide, `47°` normal, `29°` short telephoto, `18°` telephoto) with explicit camera-to-subject distances in metres, plus `No lens drift mid-segment`. Its documentary category goes further and replaces shot description entirely with a distance table: "Segment 1, 5 metres. Segment 2, 2 metres. Segment 3, 3 metres…"

**Dreamina** adds an ordering rule: if the camera is being ignored, put shot size and movement **before** lighting and mood in the sentence.

Note for completeness: there is **no dedicated "lens language" documentation page for 2.5**. The phrase appears only on the seedance-1.0-lite effects page, listing orbiting, aerial photography, zooming, panning, following, handheld. Camera direction for 2.5 lives inside the shot-timeline structure.

---

## 7. Action, physics, and performance

**OFFICIAL (2.0 guide, carried forward).** Per shot, sequence the description in this order: camera movement or transition → subject actions and expressions → position and spatial changes → audio information.

Action rules: be **body-part specific**; prefer **slow, small movements** over fast large ones; describe **transitions between poses**, not just endpoints; and **externalise emotion physically**. ByteDance publishes a mapping table — sadness, joy, nervousness, anger, relief — each translated into concrete physical detail rather than named as a feeling. Write what the body does, not what the character feels.

**HIGGSFIELD** contributes the most transferable technique here: **decompose a repeated action into a fixed mechanical sequence.** Its fantasy-action prompt breaks every sword strike into four parts (load → sweep edge-first → edge enters and keeps moving → arm finishes fully extended) and adds a terminal constraint: "The sword never stops inside a body." Giving the model one grammar to repeat beats letting it invent a fresh motion per cut.

It also demonstrates **physical quantification as a style lever** — 65 m/s, wings open "only five times in the whole film," 24 fps with normal motion blur — and an **enumerated action budget**: exactly five sword actions, each pinned to a timestamp.

**THIRD-PARTY (fal.ai) on fluids and physics:** name where motion **ends**. *"'Realistic physics' does not contain that information."*

**THIRD-PARTY (stimQQ) on stillness:** "Freeze means freeze" — if you want something motionless, say *no drift, no wobble, no micro-motion*. The model's default is to add life everywhere.

**THIRD-PARTY (stimQQ) on realism:** ask for the imperfections you want — shake, late autofocus, exposure breathing — or you get a clean commercial look by default.

**HIGGSFIELD** micro-acting checklist, used to defeat the mannequin problem: "real blinking, chest heaving, throat swallows, tears welling without falling."

---

## 8. Sound design — the four markers

**OFFICIAL**, verbatim from the 2.5 tutorial:

> Use special characters to distinguish sounds: Use **()** for music, **<>** for sound effects, **{}** for dialogue, and **【】** for subtitles. For non-Chinese dialogue, it is recommended to specify the language before the dialogue.

The 2.0 guide restates the same table and adds: *"If the dialogue is in a less common language (neither Chinese nor English), the language must be marked, such as: says in Japanese {こんにちは}"* — and a hard rule: *"The language of dialogue must be consistent, and mixing Chinese and English should be avoided (except for proper nouns)."*

**A critical caveat, and it is the single most important finding in this report about syntax.** A full-text extraction of both official 2.5 pages (1,804 lines combined) found that `{` appears **exactly once** — inside the rule that defines it. **Not one official worked example uses `{}` for dialogue.** The same is true of `【】`. And the 2.5 prompt guide uses `<...>` for *asset references* (`<video1>`, `<2pic>`), meaning the same bracket carries two incompatible official meanings across two official pages.

What ByteDance actually runs, in every worked example, is `Speaker: "line"` under a language header. See §9.

**Practical position.** The markers are documented but never demonstrated. Treat them as **disambiguators rather than requirements**: reach for them when a line is leaking into the wrong channel — dialogue being drawn as on-screen text, a sound effect being read aloud — and otherwise use the plain forms that ByteDance itself uses. This is also Morphic's reading: the brackets "are optional, since plain language works too, but they stop a line of dialogue being drawn as a caption or a sound effect being read aloud."

**OFFICIAL negative constraints for audio:** `no subtitles` and `no BGM` are explicitly sanctioned. Use them literally.

**Subtitles, when you do want them (OFFICIAL, 2.0 guide):** *"Render the narration as subtitles at the bottom-center. Subtitles must be perfectly synchronized with audio timing."*

---

## 9. Prompting a character who speaks

This section deserves its own treatment because it is where the official documentation and the official examples diverge most sharply, and where the most reproducible practitioner rules exist.

### 9.1 The syntax that ByteDance actually uses

Every dialogue example in the official corpus follows the same shape: a **language header**, then **`Speaker label: "line"`**.

From the Seedance-1.5-pro prompt guide (2168087):

```
...camera moves with a slight lateral slide. English dialogue:
Indian woman: "This place looks sketchy, but the food smells amazing."
```

Three speaker-label styles are attested officially:

| Style | Example |
|---|---|
| Role descriptor | `Indian woman:` / `Black man:` / `Japanese man:` |
| Bare letter | `Korean dialogue:` → `A: "측정값이 불안정해..."` / `B: "알겠어..."` |
| Numbered role | `Girl 1:` / `Girl 2:` / `Boy:` |

The 2.5 storyboard example uses `Dialogue (elderly woman): "…"` per panel. The portrait-video page uses `Character speaks in real-time: "I found my holy grail face cream! …"`. The 2.0 dormitory drama example is the one place braces appear in the wild, as `{How did the exam go? Did you pass?}`.

**Recommendation: use `Speaker: "line"`.** It matches every official worked example, it is what Replicate documents, and it is what the majority of practitioner guides report using. Add `{}` only as a corrective when a line is being rendered as on-screen text instead of spoken.

### 9.2 The rules that make lip sync hold

**Line length vs duration (THIRD-PARTY, videoai.me).** A comfortable spoken line runs roughly **2.5–3 words per second**. An 8-second clip holds about **twenty words** with room to breathe. Thirty words in eight seconds produces rushed delivery.

**Shot discipline (THIRD-PARTY, seedance.tv and oakgen, in agreement).** Use a **medium close-up**. Keep lips and jaw visible and unoccluded. Hold the camera steady. Ask for "subtle blinking and head motion rather than many gestures." Do not put dialogue over a whip pan, a face occlusion, or an extreme profile. Avoid reference images with glossy retouched skin or an already-open mouth.

**The attention-budget theory of failure (THIRD-PARTY, seedance.tv).** Over-directed prompts divide the model's attention among acting, lighting, camera motion, sound effects, and dialogue simultaneously. The prescription: keep the *visual* brief compact, then specify **speaker, language, exact line, tone, and pause** precisely. In other words, spend your specificity budget on the speech, not on the scenery, when speech is the point.

**The baseline test recipe (THIRD-PARTY, oakgen).** Before attempting anything complex, verify the pipeline with: one speaker, a five-word line, stable medium close-up, one visible action effect, one ambience bed, no music during dialogue.

**Do not use phonetic respellings (THIRD-PARTY, seedance.tv).** They can fix one word while damaging the rhythm of the whole sentence. The official 2.0 guide does endorse a related but narrower trick — **homophone substitution** for inaccurate Chinese pronunciation specifically.

**Say `no subtitles`.** Unwanted burned-in captions are a common enough failure that ByteDance sanctioned the negative constraint for it. The 2.0 guide adds that **landscape orientation lowers the probability** of spurious subtitles appearing.

### 9.3 Multiple speakers

**Bind voices to characters explicitly (OFFICIAL).** The mapping idiom from the 2.5 prompt guide:

```
Images 1-2 are Character 1 and correspond to Audio 1;
Images 3-4 are Character 2 and correspond to Audio 2.
```

and

```
Image 1 depicts the protagonist John and uses the voice timbre from Audio 1.
```

**Attribute every line.** Label each quoted line with its speaker. When two faces are on screen and a line is unattributed, the wrong character speaks it — this is a documented failure mode.

**Suppress the non-speaker (THIRD-PARTY, oakgen).** An explicit exclusivity clause works: *"No other character speaks. Preserve her face and mouth framing through 22 seconds."* Note that the more intuitive phrasing — "keep the other character's mouth closed" — appears in no source and is unverified.

**Don't overlap turns (THIRD-PARTY, seedance.tv).** For bilingual or fast exchanges, name the language beside each speaker and avoid overlapping dialogue. If identity or pronunciation drifts, **generate each turn separately and assemble in the edit.**

**OFFICIAL worked example of a two-hander**, from the 2.0 guide's appendix: *"The woman speaks first with a playful tone: '…' followed by the man's smiling reply: '…'"* — note that turn order is stated in prose, not left to inference.

### 9.4 Voice, timbre, and emotional delivery

The only real voice-direction vocabulary in the official corpus lives on the Seedance-1.5-pro page, and it is a clean three-slot template — **emotional state + tone + speaking pace**:

```
In a calm emotional state, with an even tone and a normal speaking pace,
say: "Let's begin with what matters most."

In a gentle emotional state, with a soft tone and a slow speaking pace,
say: "You can take your time. I'm not rushing you."

In a restrained emotional state, with a low tone and a very slow speaking pace,
say: "If you want an answer, listen carefully."
```

**Referencing a voice from an audio asset (OFFICIAL, 2.0 guide).** The recommended phrasing is richly adjectival and worth copying as a pattern:

```
Use the low, thick, warm, and finely grainy middle-aged male voice of @Audio 1 to say: "…"
```

**Accent is inferred from image references — and that will surprise you (THIRD-PARTY, MindStudio, hands-on).** In production, an unprompted British accent appeared. Prompting `"American"` fixed it; prompting `"American English"` did **not**, because the word "English" pulled the model back toward British. This is the sharpest single piece of accent advice available: **name the accent, not the language, when they conflict.**

**Language binding inline (OFFICIAL, 1.5-pro):** `He said in Cantonese, "你好靓呀！我好中意你呀"` / `He said in Mandarin: "你好漂亮呀，我好喜欢你呀"`.

**There is no preset voice library.** The digital character library (asset IDs) is **image-only**. Timbre must come from an Audio reference or from text description.

### 9.5 Dubbing, translation, and lip-sync retiming

**OFFICIAL**, the canonical example from the 2.5 prompt guide — this is the exact phrasing for translating an existing video:

```
Translate the spoken dialogue in the video into Chinese, with no subtitles.
Precisely adjust the lip movements to match the translated speech,
while keeping everything else unchanged.
```

The structure generalises: state the target language, state `no subtitles`, state `precisely adjust the lip movements to match`, and close with `keeping everything else unchanged` to prevent collateral edits.

**Singing and lyrics (OFFICIAL).** The multilingual rap example uses per-shot `Lyric line N (Language "text")` plus an explicit `precise lip sync` instruction.

**Speech bubbles (OFFICIAL, 2.0 guide template):** `[Character] says, '[Dialogue].' Speech bubbles appear around the character containing the spoken text.`

### 9.6 Speaking-character failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| Mouth starts late | Intro silence, or unclear who speaks | Trim lead-in; name the speaker explicitly |
| Timing drifts across the line | Line too long or paced too fast | Split into shorter shots; check words-per-second |
| Generic, non-specific mouth motion | Face too small, angled, or obscured | Move to medium close-up |
| Weak plosives / mushy consonants | Compression, or blurred mouth region | Cleaner source; higher-quality reference |
| Wrong character speaks | Two faces, unattributed line | Attribute every quoted line to a named speaker |
| Muddy speech | Reverb, competing music, clipping | Isolate the voice; add `no BGM` |
| Dialogue rendered as on-screen text | Channel ambiguity | Add `no subtitles`; consider `{}` markers |
| Wrong accent | Inferred from image reference | Name the accent, not the language |

**Debugging discipline (THIRD-PARTY, oakgen).** Change **one variable at a time** — never audio, source frame, and prompt together. Review at normal speed, half speed, and muted. And regenerate rather than patch when dialogue begins at the wrong point, the wrong character speaks, or lip-sync mismatch persists across the whole line.

**Post-extension desync is unverified.** No source documents a specific mechanism by which audio desynchronises after a video extension. Treat it as a risk to test, not a known behaviour.

---

## 10. Compliance — the real-face restriction

This constraint is easy to trip over and there is no way to prompt around it.

**OFFICIAL.** Seedance 2.5 and 2.0 **cannot accept uploaded reference images or videos containing real human faces.** **THIRD-PARTY (stimQQ, measured):** Volcengine rejects raw http(s) reference images that appear to contain a real person **at create time** — it is a hard rejection, not a silent filter.

Three sanctioned workarounds:

**Trusted model outputs.** Images or videos the model itself generated, used within a **30-day** window.

**The preset digital character library.** Reference by `asset://<asset ID>`. Each character consists of an image and a corresponding asset ID.

**Authorised real-person assets**, through the appropriate approval channel.

**A critical detail that breaks generations silently (OFFICIAL, portrait page).** When using a digital-character asset ID, the **prompt text must still refer to it as "Image 1"**, not by the asset ID. The ID goes in the API call; the prompt uses positional naming.

---

## 11. Consistency and anti-drift

Character drift over 30 seconds is the defining difficulty of this model, and there is a well-developed body of technique for it.

**Name your subjects and reuse the token (THIRD-PARTY, stimQQ).** The single best line on this: *"Over 30 seconds, 'she' and 'the man' drift onto the wrong body. A named token is the cheapest identity lock there is."* Higgsfield does exactly this — `THE DETECTIVE`, `THE WOMAN`, `THE SEDAN` — and never uses a pronoun where a token will do.

**Define subjects formally (OFFICIAL, 2.0 guide).** `Define [Core_Subject_Features] in <Image/Video_N> as <Subject_N>`, using **2–3 stable static features**, then bind with `<Subject_N>@<Image_N>`. Two or three anchors, not ten — over-specification competes with itself.

**Describe each action exactly once (THIRD-PARTY, stimQQ).** Repeating an action in different words **degrades** it rather than reinforcing it. Compare with **Dreamina's** slightly softer version, which is probably the better rule in practice: state an essential instruction *"once near the beginning and reinforce it in the relevant timed beat instead of repeating it everywhere."*

**Restate through occlusion (THIRD-PARTY, fal.ai).** When a subject is hidden and returns, say how long it is hidden and repeat the traits that must survive. *"'The same woman emerges' is weaker than repeating the few details you cannot afford to lose."*

**Count locks.** The duplicated-character problem is real and has an official fix (a global anti-twin constraint) and a superb Higgsfield demonstration:

```
MEMBER COUNT LOCK (critical): The group has exactly four members, never five,
never six. No fifth member, no extra unnamed dancer, no background double,
no duplicated or cloned member. Each of the four appears once and only once
in any frame, no mirror, glass, or reflection showing an extra copy.
```

**stimQQ** adds the reference-sheet variant to your negative list: *"never render a reference sheet or duplicate the subject."*

**The `… LOCK` idiom.** Higgsfield's documentary prompt makes this a system: `TIME AND CROWD PROGRESSION LOCK`, `BEAUTY WITHOUT RETOUCHING LOCK`, `FRAMING RESPECT LOCK`, `IDENTITY LOCK`, `NO-IP LOCK`, `CLEAN-AIR LOCK`, `SINGLE-LENS LOCK`. Naming each constraint gives it scope and makes it addressable when debugging.

**`POSITIVE LOCKS` as a closing block.** Higgsfield's two most complex prompts both end by restating every rule affirmatively. This directly serves ByteDance's "use positive descriptions whenever possible" instruction while still functioning as a constraint list.

**Spatial maps.** Higgsfield's `LOCATION MAP` and `BEACH MAP` sections establish a persistent geography — the same dune line, the same two fire pits, the camera always on the south sidewalk facing north — so every segment shares one space. Its noir prompt adds an explicit screen-direction lock: "the sedan arrives from screen-right, the woman travels right-to-left," and "the camera never crosses to the north side of the street."

**Reference images beat text descriptions (HIGGSFIELD, from testing).** "Once a face or a product is locked as a reference, it survives hard cuts, lighting changes, and camera moves that would otherwise cause drift." Text descriptions do not survive the same treatment.

**More than four reference characters (OFFICIAL, 2.0 guide).** Group them into composite images of ≤4 faces each rather than supplying many single portraits.

**Multi-character scenes are the hardest category (HIGGSFIELD).** "The more faces in a single shot, the more reference material each one needs to avoid drifting into a generic face by the third or fourth cut."

**Body proportions can drift even when faces hold (THIRD-PARTY, Virse).** Lock wardrobe and build, not just face.

---

## 12. Advanced modes

**3D clay-model previsualisation.** A white-box render pass used to establish blocking and camera before committing to a final look. The official guide carries two full worked examples, including a 30-second girl-and-airplane film. The 2.0 guide also documents a "white-model conversion trick" to counter quality degradation during extension.

**Multi-panel storyboards.** Up to ~15 panels. The official 9-panel robot-and-grandmother example is the best template for dialogue-per-panel work, using `Dialogue (elderly woman): "…"` inside each shot block.

**Keyframe references.** Syntax: `Use Images X to X in order as keyframes.`

**Region / frame-level editing.** Trigger words are listed in §2. Two official templates exist — instruction editing (`Video edit: remove everyone in @Video1 except the protagonist.`) and editing guided by reference images. **OpenArt:** region edits preserve the input's shape and length — no crop or trim in the same step — and clips **≤20 s edit more reliably**. Official recommendation is 1–5 reference images for editing.

**Video extension.** Extend forward or backward. **OFFICIAL warning (2.0 guide):** for edit and extend, refer to the source as `<Video_N>` **directly** — do *not* write "reference `<Video_N>`", which flips the task type. Known artefacts: jump cuts at the seam (the official workaround is trimming 6 frames off the end and 1 frame off the start in an editor) and progressive quality degradation. **fal.ai** recommends **final-frame chaining** for continuations and warns not to retell the first clip in the second prompt. **THIRD-PARTY (stimQQ):** reference-video jobs bill source seconds *plus* output seconds, roughly 20–25% more.

**Seamless transition** and **one-click creation** both have official worked examples.

**End-of-video audio noise (OFFICIAL, 2.0 guide).** A known artefact; the fix is a volume-envelope fade applied in post.

---

## 13. Higgsfield-specific notes

Higgsfield exposes Seedance 2.5 as a platform rather than raw API, and the differences matter if that is where you generate.

The workflow is **references first, then creative-direction selectors, then prompt**. Genre, era, lighting, physics, and emotional control are set **outside** the prompt text as UI selectors — and Higgsfield's testing found these do disproportionate work: *"Genre and lighting settings do more work than most of the prompt text itself. Changing genre alone shifts pacing, contrast, and camera behavior even when the written scene description stays identical."* Its FAQ confirms: yes, genre matters even when your scene description is already detailed.

Four generation modes: **t2v, omni_reference, video_edit, video_extension**. Reported constraints: **720p cap**, no separate `start_image`/`end_image` media roles, no genre hint parameter, no 4K lane. Aspect ratios 9:16 through 21:9; standard duration 30 s.

Its six tested findings, condensed: references beat text for identity; genre and lighting settings outweigh prompt prose; multi-character is hardest; shot-by-shot beats continuous description for anything multi-angle; 50 references is a ceiling not a target; and — the most quotable — *"The GLOBAL STYLE and AUDIO sections function as guardrails more than instructions. Explicitly excluding what shouldn't appear — modern artifacts, music, dialogue — prevents more failures than adding more positive description does."*

Its ten tested categories, for reference: dramatic exterior, action sequence, commercial product, epic landscape, noir, multi-character, fantasy action, UGC-style ad, horror, documentary. Two are worth singling out for technique. The **UGC ad** is the only category that deliberately *opts out* of genre ("no genre-specific visual logic imposed"), uses lowercase plain-language labels instead of caps, and builds a two-level time hierarchy — three 10-second Segments each containing named, timecoded Shots with dramaturgical names ("Turbulence Hook", "The Pivot", "First Bite"). Its dialogue idiom puts voice direction inline before the colon: `…and talks to the lens through it in a tight controlled voice: "…"`, with silent shots explicitly marked "no speech." The **horror** category inverts the whole structure — technical constraints first, characters last — and expresses a focus lock as camera behaviour: "she is never in sharp focus until the final second… the autofocus refuses to lock on her."

---

## 14. Consolidated failure-mode table

| Symptom | Cause | Fix |
|---|---|---|
| Aspect ratio or duration silently ignored | Prompt wording triggered a locked task type | Set `omni_reference_task_type` explicitly |
| Character identity drifts across cuts | Pronouns; too few or too many references | Named subject tokens; 2–3 stable anchors; reference images over text |
| Duplicated / cloned character | Model reads multiple angles as multiple subjects | Explicit count lock; "never render a reference sheet" |
| Multiple products from one product's angles | Same cause | "All N images show one X. The video must contain only one X." |
| Long clip feels empty, repetitive, or slow-mo | Duration raised without adding events | 5–8 defined beats for 30 s; timestamped event track |
| Reaction fires before its cause | Cause and effect compressed into one action | Split into contact → movement → sound → reaction |
| Camera instruction ignored | Vague move words; move stated after mood | Screen-space position + one move per shot; put camera before lighting |
| Sequence falls apart between shots | Vague transitions | Label every shot; end each with `Hard cut.`; specify distance and framing per shot |
| Unwanted subtitles | Channel ambiguity | `no subtitles`; landscape orientation lowers probability |
| Unwanted logo / watermark | Default behaviour | "do not generate a logo", "do not generate a watermark" |
| Style drifts mid-clip | Global rule stated once, weakly | GLOBAL STYLE block at top + POSITIVE LOCKS restatement at bottom |
| Jump cut at extension seam | Extension artefact | Trim 6 frames off end, 1 frame off start in an editor |
| Extension quality degrades | Known artefact | White-model conversion trick (2.0 guide) |
| Noise burst at end of audio | Known artefact | Volume-envelope fade in post |
| Everything looks like a clean commercial | Model's default polish | Explicitly request shake, autofocus hunting, grain, exposure breathing |
| Objects render at wrong scale | Known weakness (MindStudio: book rendered suitcase-sized) | State real-world dimensions; expect several attempts |
| Morphing during fast action | Known weakness | Slow the action; *cannot* be fixed by upscaling |
| Shots produced in wrong order | First-frame + omni-reference sequencing ambiguity | Restate sequence in prompt text; don't rely on input order |
| Seedance 2.0 prompt produces glitchy 2.5 output | 2.5 resists rapid-cut prompting | Let scenes breathe; rewrite rather than port |

---

## 15. Contradictions ledger

Reported honestly rather than resolved, because the evidence does not support resolution.

### 15.1 Output resolution — a three-way split

**Official BytePlus docs (2607688):** Seedance 2.5 outputs 480p / 720p / **1080p (10-bit, H.265/HEVC)**, and **4K belongs to Seedance 2.0**.

**Marketing and aggregator sites** (imagine.art, kie.ai, Pollo, and MindStudio's own features page): **4K**.

**Everyone who demonstrably ran the model:** fal.ai's API docs state "It supports 480p and 720p output." CometAPI: 480p/720p. MindStudio's hands-on review, contradicting its own marketing page: "Output currently caps at 720p." stimQQ, measured 8 Aug 2026: 480p/720p only. Higgsfield: 720p cap. Dreamina treats 4K as a **post-process upscale**, not native output.

**Assessment.** This looks like an **announced-versus-exposed gap**. The 4K figure traces to the 23 June FORCE announcement and is being resold by sites that never called the endpoint. Two independent hands-on testers (stimQQ and MindStudio) arrive at 720p separately — the strongest evidence in the set. A further wrinkle: stimQQ asserts the *reverse* of the official reading, claiming 2.5 was announced with native 4K 10-bit while 2.0 tops out at 1080p, then concedes the 4K "is not a resolution the API exposes." And CometAPI documents the model ID as `seedance-2-5-260628` while Ark uses `dreamina-seedance-2-5-260628`; apimodels lists `dreamina-seedance-2-0` as a distinct "international line, native up to 4K 10-bit." The `dreamina-` prefix may denote a separate SKU, which would explain the confusion entirely. **Open question. Plan for 720p; verify 1080p on your own account before promising it.**

### 15.2 Dialogue syntax — `{}` versus `""`

Documented as `{}` on the 2.5 tutorial and the 2.0 guide. Used as `Speaker: "line"` in **every** official worked example across all five pages. `{` appears once in 1,804 lines of official 2.5 documentation — in the rule that defines it. Prompt Architects insists braces remain live on both 2.0 and 2.5; Morphic calls them optional disambiguators. **No side-by-side A/B test of the two forms exists in any source.** Position taken in this report: use quotes, keep braces as a corrective.

### 15.3 Asset token syntax

`@Image 1` (2.5 tutorial, fal.ai, OpenArt, Dreamina, AtlasCloud) versus bare `Image 1` and `<video1>` (2.5 prompt guide) versus `[Image1]` (Replicate, CometAPI). Unresolved; most likely per-platform normalisation, but no source says so.

### 15.4 Prompt length

CometAPI: *"Target 60–120 words for a 30-second clip."* fal.ai and stimQQ both publish production prompts running 2,000–4,576 characters; Higgsfield's tested prompts run longer still. Higgsfield's FAQ takes the sensible middle: "As long as the scene needs. A single shot can run a few sentences with a reference covering the visual detail. A multi-shot sequence needs every section filled out." **The 60–120 word claim is contradicted by everyone who published tested prompts.**

### 15.5 Negative constraint blocks

CometAPI advises against long negative lists. fal.ai, stimQQ, Dreamina and Higgsfield all mandate a closing constraint block, and Higgsfield's testing found exclusions "prevent more failures than adding more positive description does." **Weight of evidence favours keeping a constraint block** — but keep it short, concrete, and grouped at the end (Dreamina), not a generic blacklist.

### 15.6 Language counts

Seedance 2.5 is documented with 11 native audio languages. Seedance-1.5-pro publishes a different list (Mandarin, Cantonese, Shaanxi, Sichuan, Taiwanese-accented, English, Japanese, Korean, Spanish, Indonesian) with "millisecond-level lip-sync precision." **Do not merge the two lists.**

---

## 16. General-purpose prompt structure

This is the deliverable: one template that works across task types, synthesised from the official three-part architecture, the official advanced formula, Higgsfield's tested section order, and fal.ai's block system — reconciled where they differ, with the disputed syntax resolved toward what ByteDance's own examples actually run.

**How to use it.** Fill top to bottom. Delete any block that is not solving a real problem — an unused block is noise, and fal.ai, Dreamina and Higgsfield all independently warn against filling sections for the sake of it. Blocks 1, 4, 9 and 10 are the load-bearing ones: a global rule at the top, a timeline in the middle, a sound rule and a constraint block at the bottom. Everything else is optional weight.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] ONE-SENTENCE SUMMARY
    <Subject> + <Location> + <Event> + <Genre/Style> + <Camera movement>,
    <duration>s, <shot count> shots.

[2] GLOBAL STYLE
    Genre. Colour grade. Film stock or digital look. Texture and grain.
    Frame rate and motion character. What must never appear anywhere.

[3] ASSET ROLES                              (omit for pure text-to-video)
    @Image 1 controls only <invariant: identity / product design / wardrobe>.
      Do not copy <pose / background / lighting / camera angle / text> from @Image 1.
    @Video 1 controls only <camera path / rhythm / motion>.
    @Audio 1 controls only <voice timbre / music bed>.
    <If several angles of one object:> All N images show one <object>.
      The video must contain only one <object>.
    <If voices:> @Image 1 is <Character A> and uses the voice timbre of @Audio 1.

[4] CHARACTERS                    (NAMED TOKENS — never pronouns after this)
    <TOKEN_A>: age, build, face, hair, wardrobe, 2–3 stable anchor features.
      Screen position and facing.
    <TOKEN_B>: same.
    COUNT LOCK: exactly N characters. No extra, no double, no reflection copy.
      Never render a reference sheet.

[5] LOCATION / SPATIAL MAP
    The space, its props, its geometry. Camera side and facing, held for the
    whole clip. Foreground / midground / background. Screen-direction rule.

[6] FIRST FRAME AND BLOCKING
    Exactly what is on screen at 0.0s. Who is where, facing which way.
    No empty establishing frame, no delayed reveal.

[7] TIMELINE                                          ← the load-bearing block
    0-Xs   — camera <one move only, from a screen-space position>;
             <TOKEN_A> <specific body-part action>;
             <sound event>;
             <TOKEN_A> speaks: "<line>"       ← see block 8
    Hard cut.
    X-Ys   — ...
    Hard cut.
    Y-Zs   — ...

    Rules: whole seconds only. No gaps. One action per range. Not a counter.
    5–8 defined beats per 30s. Cause stated before reaction, as separate actions.
    Restate identity traits after any occlusion.

[8] DIALOGUE                                           (omit if no one speaks)
    <Language> dialogue.  Spoken language: <language + ACCENT, e.g. "American">.
    <TOKEN_A>: "<line, ~2.5–3 words per second of screen time>"
    Delivery: in a <emotional state> state, with a <tone> tone and a
      <pace> speaking pace.
    Framing: medium close-up, lips and jaw visible, camera steady, no head turn
      while speaking.
    No other character speaks. No subtitles.
    <If dubbing:> Precisely adjust the lip movements to match the speech,
      keeping everything else unchanged.

[9] CAMERA AND OPTICS
    Per shot: shot size, one movement type, angle, and a screen-space position.
    Optional lens lock: <focal length or diagonal FOV> and camera-to-subject
      distance in metres. No lens drift mid-shot.

[10] LIGHTING
    Source and where it is motivated from. Direction. Quality. How it falls on
    faces. Held constant, or its stated progression.

[11] PHYSICS
    How fabric, hair, smoke, liquid, and impacts behave. Where each motion ENDS.
    Weight and inertia. Anything that must be motionless: no drift, no wobble,
    no micro-motion.
    <For a repeated action:> decompose it into a fixed mechanical sequence and
      state the terminal constraint.

[12] AUDIO                                                    ← second guardrail
    Ambience bed. Sound effects with timestamps. Music or (no BGM).
    What must not be heard.
    Markers if a channel is leaking: () music, <> sound effect,
      {} dialogue, 【】 subtitles.

[13] POSITIVE LOCKS                                          ← closing guardrail
    Restate every rule affirmatively: identity holds across every cut; wardrobe
    by segment; geography and screen direction hold; exactly N characters;
    real-time motion, no speed ramps; all text unreadable, everything unbranded.
    Short, concrete, grouped here — not scattered through the prompt.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Minimal variant — single shot, one reference

For simple work, most of the above is dead weight. This is the whole thing:

```
<Subject> <action> in <location>, <style>, camera <one move>.
@Image 1 controls only <invariant>. Do not copy <pose/background> from @Image 1.
<Lighting in one clause.> <Physics in one clause.>
Audio: <ambience>. (no BGM). No subtitles.
```

### Ten rules that survive every source

1. **Set `omni_reference_task_type` explicitly.** Otherwise your trigger words choose your task type, and your aspect ratio and duration may be discarded without warning.
2. **Label your sections.** Every party that tested at scale converged on labelled blocks over continuous prose.
3. **Name your subjects and never use a pronoun again.** The cheapest identity lock there is.
4. **Give every asset exactly one job, and say the word "only".**
5. **Use fewer references than the ceiling allows.** Four or five well-chosen beats fifty competing ones.
6. **Duration is not content.** Thirty seconds needs 5–8 defined beats, or you get waiting and slow motion.
7. **One camera movement per shot, from a stated screen-space position.** "Dynamic" is useless.
8. **Say each thing once.** Repetition in different words degrades rather than reinforces — reinforce in the relevant timed beat instead.
9. **Guardrails at the top and bottom beat more description in the middle.** A global style rule and an audio/constraint block prevent more failures than extra adjectives fix.
10. **Change one variable per iteration.** Rewrite only the physical state where the bad behaviour begins.

---

## Sources

**Official — BytePlus ModelArk**
- [Dreamina Seedance 2.5 prompt guide (2607689)](https://docs.byteplus.com/en/docs/ModelArk/2607689)
- [Dreamina Seedance 2.5 tutorial (2607688)](https://docs.byteplus.com/en/docs/ModelArk/2607688)
- [Create portrait videos with Dreamina Seedance models (2608626)](https://docs.byteplus.com/en/docs/ModelArk/2608626)
- [Dreamina Seedance 2.0 series prompt guide (2222480)](https://docs.byteplus.com/en/docs/ModelArk/2222480)
- [Seedance-1.5-pro prompt guide (2168087)](https://docs.byteplus.com/en/docs/ModelArk/2168087)
- [Digital character library (2223965)](https://docs.byteplus.com/en/docs/ModelArk/2223965)
- [seedance-1.0-lite model effects (1553576)](https://docs.byteplus.com/en/docs/modelark/1553576)

**Higgsfield**
- [Seedance 2.5: Complete Prompting Guide (Full Prompt Library)](https://higgsfield.ai/blog/seedance-2-5-prompting-guide)

**Third-party — practitioner and platform**
- [fal.ai — Seedance 2.5 prompting guide](https://fal.ai/learn/devs/seedance-2-5-prompting-guide) · [model page](https://fal.ai/seedance-2.5)
- [OpenArt — Seedance 2.5 prompt guide](https://openart.ai/blog/seedance-2-5-prompt-guide/)
- [Dreamina (CapCut) — Seedance 2.5 prompt guide](https://dreamina.capcut.com/seedance/seedance-2-5-prompt)
- [Replicate — bytedance/seedance-2.5](https://replicate.com/bytedance/seedance-2.5)
- [CometAPI — How to prompt Seedance 2.5](https://www.cometapi.com/how-to-prompt-seedance-2-5/)
- [MindStudio — Seedance 2.5 review and guide](https://www.mindstudio.ai/blog/seedance-2-5-review-guide)
- [GitHub — stimQQ/awesome-seedance2.5-prompts](https://github.com/stimQQ/awesome-seedance2.5-prompts)
- [GitHub — AtlasCloudAI/awesome-seedance-2.5-prompts-skills](https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills)
- [Morphic — How to use Seedance 2.5](https://morphic.com/resources/how-to/seedance-2-5-guide)
- [Oakgen — Seedance 2.5 audio and lip-sync guide](https://oakgen.ai/blog/seedance-2-5-audio-lip-sync-scene-editing)
- [Seedance.tv — Seedance 2.5 lip sync issues](https://www.seedance.tv/blog/seedance-2-5-lip-sync-issues)
- [VideoAI.me — Seedance 2.5 audio](https://videoai.me/blog/seedance-2-5-ai-video-with-sound)
- [Prompt Architects — dialogue and lip sync in AI video](https://prompt-architects.com/blog/310-dialogue-and-lip-sync-in-ai-video)
- [Virse — Seedance 2.5 Reddit review](https://www.virse.ai/blog/seedance-2-5-reddit-review)
