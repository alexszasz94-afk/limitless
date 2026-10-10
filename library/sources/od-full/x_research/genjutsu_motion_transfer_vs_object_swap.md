# Object Swap keeps the product real

**Bottom line:** for Daniel's kind of clip, **Object Swap is the default mode and Motion Transfer is the specialist.** Use Object Swap for three of the four jobs: new person on the same background, same person on a new background, and product swaps. For the hardest job (new person *and* new backgrounds while keeping the hoodie), start with Object Swap too, and test Motion Transfer against it once. The reasoning is simple. Object Swap is a video *edit*: the real hoodie, light, camera and cuts stay in the frame as material the model copies from. Motion Transfer keeps only the movement and **redraws everything else from still images, the hoodie included**, one pose at a time. On a product ad, that redraw is exactly the risk you cannot afford. Motion Transfer is the better tool when the new world must be completely different from the source (a garage that becomes a beach), or when the source is one continuous take.

On inputs, **reference images beat text for identity and location** (high confidence). Text-only faces drift between shots, and the sources disagree on nothing here. For a character swap, **use video + reference images + a short, structured prompt** rather than images alone (medium confidence). The prompt should do three things: map each image to its job, state that the hoodie stays, and lock everything else. It hurts when it re-describes the person differently from the picture, uses "no X" phrasing, or grows into a long creative script. No one has published a controlled reference-only vs reference+prompt test for Genjutsu. Run 2 of the test plan below is that test, on his own clip.

Confidence varies because Genjutsu launched on **August 31, 2026** ([Higgsfield blog](https://higgsfield.ai/blog/higgsfield-genjutsu)). About a month of real-world evidence exists, and none of it covers a product-wearing, multi-cut fashion reel.

## Object Swap wins three of the four jobs

| Job | Mode | Confidence | Why |
|---|---|---|---|
| New person, same backgrounds | **Object Swap** (target: the woman) | Medium | Background, light, camera and cuts stay real pixels. The source hoodie stays in view as context. |
| Same person, new backgrounds | **Object Swap** (target: the location) | Medium | The woman and hoodie are not the edit target, so the product has the best chance of surviving. Motion Transfer would need her real face as a reference. |
| New person + new backgrounds, keep hoodie | **Object Swap first; Motion Transfer as one head-to-head test** | Low–medium | Object Swap keeps the real garment and the cut structure. Motion Transfer wins if the new world is radically different from the source. |
| Product/object swap (new colourway, different item) | **Object Swap** | Medium–high | This is the job Higgsfield explicitly routes to it. |

Higgsfield defines the modes cleanly. Motion Transfer: "The motion, camera, and timing stay the same, everything else is rebuilt from your references." Object Swap: "Say what should be different - a person, a product, the text - and the rest of the shot stays untouched" ([higgsfield.ai/genjutsu](https://higgsfield.ai/genjutsu)). Higgsfield's own routing (its MCP connector's `/genjutsu` recipe) sends any request to "replace, change, or swap an object, product, garment, or character in a source video using reference images" to Object Swap (`hf_mult_replace_object`). It sends requests to "copy… motion, actions, gestures, dance, or camera motion… to reference-image subjects" to Motion Transfer (`hf_mult_motion_control`) (Higgsfield MCP connector, `/genjutsu` recipe). The model cards tag Object Swap as `video-edit` and Motion Transfer as `image-to-video`/`motion-control`. That is the technical heart of the decision.

Open replacement models show what this means in practice. Wan 2.2 Animate's "replacement" mode masks out only the subject, keeps the environment, and relights the new character to the scene. Its "animation" mode takes the background from the reference *image*, "analogous to standard I2V generation" ([Wan-Animate paper](https://arxiv.org/html/2509.14055)). In any mode that regenerates the person, the hoodie sits inside the regenerated region and is **re-created, not kept**. Fine rhinestone mesh is exactly the high-frequency detail that drifts. The difference is what the model can see while it re-creates the hoodie. In Object Swap, the real hoodie's folds, sparkle and light are in every source frame. In Motion Transfer, the hoodie exists only in a still reference and must be re-solved in every pose and every cut.

### The "both" job is where the researchers disagree

The case for **Motion Transfer** is real and should be stated at full strength. Higgsfield's page positions it for "Recasting with different characters" and "Changing locations/settings entirely". It positions Object Swap for "Targeted edits where most of the scene works" ([higgsfield.ai/genjutsu](https://higgsfield.ai/genjutsu)). Every praised community showcase found is a Motion Transfer recast. One creator built a Joseon-era music-video remake from "multi-angle character references + a separate environment reference" and was "really happy with how the character consistency turned out" ([r/HiggsfieldAI](https://www.reddit.com/r/HiggsfieldAI/comments/1wjrtcp/storm_ii_in_joseon_korea_made_with_genjutsu/)). Object Swap's only documented hands-on test failed: swapping a golf ball for an egg left the original ball visible and misplaced the egg ([The Rundown](https://app.therundown.ai/guides/swap-the-product-and-keep-the-performance-with-higgsfield)).

Three facts specific to Daniel's footage tip the default the other way.

The first is product fidelity. A reference-driven recast reproduces products only approximately. A virtual-influencer creator running Genjutsu on a makeup routine conceded that "the cosmetic packaging is generated and approximate" ([r/HiggsfieldAI](https://www.reddit.com/r/HiggsfieldAI/comments/1wul7co/genjutsu_makeup_test_keeping_a_fictional/)). For a store selling that exact hoodie, "approximate" is a fail.

The second is the cuts. Object Swap carries the cut structure along with the untouched footage. Motion Transfer has to rebuild a different world on each side of each roughly 1 s cut. Kling and Runway's motion-transfer tools explicitly demand "a single continuous shot" ([Kling guide](https://kling.ai/quickstart/motion-control-user-guide); [Fuser Act-Two guide](https://fuser.studio/articles/runway-act-two-guide)).

The third is that the woman is mostly filmed from behind. The main Object Swap weakness users report on the suspected engine is face blending: "the face keeps looking like a mix of my model and the original person" ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1wjcrp3/seedance_25_keeps_blending_the_face/)). That matters least when the face is rarely on screen.

**Verdict:** run the combined job as one Object Swap pass with timed location operations. Then run Motion Transfer once with identical references, and let the footage decide. If Daniel wants a location that shares nothing with the source's geometry and light, go straight to Motion Transfer. Object Swap's location edit is bounded by the original camera height, perspective and lighting.

## Images carry identity; a short prompt carries the instructions

Every source points the same way on references versus text. Riffkit: "A face described in words alone will not hold", and "a reference-backed character is a different reliability class from a sentence" ([Riffkit](https://riffkit.ai/blog/how-to-use-higgsfield-genjutsu)). Higgsfield defines both modes as rebuilding "from your references". Its own edit workflow refuses to swap a person without a reference image and generates one first (Higgsfield MCP connector, Ad Multiplier workflow). Locations work the same way. Runway's Aleph docs say patterns and environments "drift between frames without reference images" ([Runware Aleph 2.0 docs](https://runware.ai/docs/models/runway-aleph-2-0/guides/editing-video)). Reddit's practical advice for background swaps is to "generate the studio as a still, clean it up in Magnific, and use that as a locked plate so it doesn't flicker" ([r/HiggsfieldAI](https://www.reddit.com/r/HiggsfieldAI/comments/1wpxcwc/first_time_using_higgsfield_ai_for_background/pc4we3u/)). Text-only edits do work for simple changes: one user swaps "the shirt or the background with just one prompt. It works pretty well" ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1wjdm66/which_do_you_think_is_the_most_costeffective_v2v/)). They are the fallback, not the realism path.

**References have a cost: "Reference images bring their whole frame with them."** Wardrobe, light and background bleed in, so "clean, neutral references beat pretty ones" ([Riffkit](https://riffkit.ai/blog/how-to-use-higgsfield-genjutsu)). The sharpest version of this is a face inside a clothing reference. A Seedance user explicitly told the model the protagonist was the original man, yet the output used "the random man who had the clothes on in the reference image". Their conclusion: use references "with the face erased" ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1vbmwxt/again_video_ruined_by_putting_faces_in_the/)). **Images override text when they conflict.** That is why the hoodie reference must be faceless, and why the character reference's outfit matters.

### Reference-only vs reference + prompt

Officially a prompt is optional: "A preset alone can drive the entire change, a short description is optional" ([Higgsfield blog](https://higgsfield.ai/blog/higgsfield-genjutsu)). But reference-only is risky for Object Swap on this job, for three reasons.

The first is the outfit. Higgsfield's detailed edit rules state that "a mapped person image is a **complete-look reference by default**". It controls face, hair, body "clothing, footwear… and accessories", and "the source wardrobe has no authority of its own" unless a separate garment image or an explicit instruction says to keep it (Higgsfield MCP connector, Ad Multiplier `prompt-writer.md`). Without a prompt, a new woman pictured in anything but the hoodie can take the hoodie with her.

The second is that edit-type models given too little instruction tend to do nothing. On Seedance 2.5 edit, "about 90% of the time… it'll just spit out the exact input video", and the diagnosis was "the prompt you're writing here is too thin" ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1v29ye4/trying_to_edit_video_but_outputs_are_identical_to/)).

The third is that every Higgsfield edit template is explicit about the target, the `@ImageN` binding and the keep-list.

The counter-evidence is that motion-transfer tools work fine with no prompt. A Kling Motion Control user who recast a viral TikTok reported "no prompt needed", with identity and background holding ([r/KlingAI_Videos](https://www.reddit.com/r/KlingAI_Videos/comments/1tmunrt/cloned_a_viral_tiktok_onto_a_completely_different/onpj7ko/)). The rule of thumb there is "Prompt = visual context only (not movement)" ([r/HiggsfieldAI](https://www.reddit.com/r/HiggsfieldAI/comments/1qe6m2j/kling_motion_control_is_one_of_my_favorites_on/)). So **reference-only is less dangerous in Motion Transfer than in Object Swap.**

A prompt makes things worse in three specific ways. The first is restyling the reference: Higgsfield's rule is "never rename or restyle a reference", so text must match the picture. The second is negation: "'She has no earrings' won't work because the clip will see 'earrings'", so write "bare earlobes" ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1rq9oj9/how_do_you_stop_wan_animate_from_hallucinating/o9rcbeo/)). The third is asking the prompt to do identity work alone. Strict and even JSON prompts did not stop face blending on Seedance 2.5 ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1wjcrp3/seedance_25_keeps_blending_the_face/)). What fixed it was visual pre-work: edit the new person into a frame extracted from the source and feed that in, so the model "will not pick a random person if you already did half the job for him" ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1vbmwxt/again_video_ruined_by_putting_faces_in_the/p0wmnbi/)).

One prompt habit specific to Daniel's footage: **because she is seen from behind, hair is the identity carrier.** Describe the hair precisely (length, colour, texture, how it falls over the hood), and only as it appears in the reference.

## Four conflicts in the evidence, resolved

**The detailed rules belong to a sibling model.** The official-docs researcher corrected itself. The complete-look rule, the cut-preservation contract and the DETAILED/COMPACT prompt templates come from Higgsfield's **Ad Multiplier** workflow, which Higgsfield says is "powered by Seedance 2.5". They do not come from Genjutsu's own text. The connector even says "never… ad-multiplier for one Genjutsu edit" (Higgsfield MCP connector, server instructions). The Genjutsu-specific official material is thin: the product page, the blog, the `/genjutsu` recipe and two model cards. Applying the Ad Multiplier rules to Genjutsu is therefore an inference, but a reasonable one. The internal IDs share the `hf_mult_` prefix, the 4–30 s range and 480/720/1080p tiers match, and several users independently believe "Genjutsu is just Seedance 2.5 edit with a fancy wrapper" ([r/aivideomaking](https://www.reddit.com/r/aivideomaking/comments/1wtwqh4/motion_transfer_ai/pd3wos6/)). Higgsfield names no model ([Riffkit](https://riffkit.ai/blog/how-to-use-higgsfield-genjutsu)). **Confidence that the Ad Multiplier rules apply: medium.** Treat them as the best available prompt grammar, not as guarantees.

**Motion Transfer vs Object Swap for the "both" job.** The community and creator researchers favoured Motion Transfer, based on Higgsfield's positioning and the showcases. The official and technical researchers favoured Object Swap, because it keeps the real garment and the cuts. The resolution is above: Object Swap first on multi-cut product footage, and a single Motion Transfer head-to-head. Motion Transfer becomes the first choice for continuous takes or radically new worlds. **Confidence: low–medium,** because nobody has tested either mode on a garment that must stay identical.

**Multi-cut sources: keep cuts or split.** The Ad Multiplier contract is written to keep cuts: "Keep this @Video1 clip exactly as it is — the same shots and cuts". It also forbids splitting: "Do not trim, split, loop, freeze, or clamp". Cachephoto's Higgsfield-affiliated test says the model "keeps camera movement, light, grain, lens character and cut points" ([Cachephoto](https://www.cachephoto.com/en/cineblog/higgsfield-genjutsu-video-a-video/)). On the other side, an independent guide says "Do not hand cuts to the model" ([ahmetbalaman.com](https://ahmetbalaman.com/en/blog/higgsfield-genjutsu-video-to-video-with-blender-en/)). The suspected engine also mishandles cut structure: Seedance 2.0 "puts in cuts… when previously there was just continuous motion" ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1vrkjv7/help_with_seedance_25_video_editing_with_face/)). The **4 s minimum settles the practical question.** About 1 s shots cannot be run individually, and looping or freezing them to reach 4 s wastes credits and invents motion.

The order is therefore:
1. Run the **whole 10.3 s clip** once (one identity across all shots; cheapest).
2. If identity or backgrounds break at cuts, split into **two ≥4 s blocks by location**: garage ≈ first half, rooftop ≈ second half.
3. Best of all, if the **raw uncut takes** still exist, process each continuous take (≥4 s), then re-cut in CapCut. This is the strongest option for Motion Transfer.

No one has published a multi-cut Genjutsu result. **Confidence: low–medium.**

**3–30 s vs 4–30 s, and 30 vs 40 references.** Press quoting an earlier product page reported 3 s and 40 images ([Bottle Rocket](https://www.bottlerocketcontent.com/higgsfield-genjutsu-motion-transfer/)). The live page read on 2026-10-02 and the blog both say **4–30 s and up to 30 reference images** ([higgsfield.ai/genjutsu](https://higgsfield.ai/genjutsu); [Higgsfield blog](https://higgsfield.ai/blog/higgsfield-genjutsu)). The API playground lists 1–30 s ([open.higgsfield.ai](https://open.higgsfield.ai/models/higgsfield/genjutsu/motion-transfer/v1.0/playground)). Plan on **4 s and 30 images** (high confidence). Neither limit binds a 10.3 s clip with four to seven references. Only the minimum matters, and only for splitting.

## A seven-run test plan for the three clips

The plan is a strict sequence. Each run is a single generation, inspected before the next. Every run is a 480p draft until a winner exists. Each run answers one question, so a failure is diagnosable, following the "refine one variable at a time" advice ([Media.io](https://www.media.io/video-effects/higgsfield-ai-genjutsu-tutorial.html)).

### Prep (no credits)

**Clean source.** From the CapCut project, hide the text track and export each clip at its native **720×1280, 30 fps**, with high bitrate and no transitions. Higgsfield's edit contract preserves on-screen text by default ("Never automatically remove, add, or regenerate captions"), and Motion Transfer would redraw it, probably garbled. Re-adding text in CapCut afterwards is cleaner either way. If no clean version exists, run the overlaid version and plan to cover the old caption with a new opaque text box in the same position. Confirm video_2 and video_3 are each ≥4 s. Note each clip's cut timestamps from the CapCut timeline (e.g. garage shots 0.0–5.x s, rooftop 5.x–10.3 s). The prompts reference real cut boundaries, and Higgsfield's own rule is that "location states follow real caption boundaries" (Higgsfield MCP connector, Ad Multiplier).

**Character reference (the new woman).** Mirror Higgsfield's own spec for person references: "a straight-on, eye-level, full-body portrait of exactly one adult" on "a seamless matte-white studio backdrop", 3:4, 2k, "soft, evenly diffused" light, "authentic skin detail, realistic human anatomy, natural hands and limbs, and no plastic retouching" (Higgsfield MCP connector, Ad Multiplier Stage 4). Make two images of the same woman in Nano Banana or GPT Image: **front full-body** and **back full-body**. The back view is not optional for footage shot from behind. Dress her **in the black hoodie itself**, using his real product photo as input and an outfit-transfer instruction such as "Put the outfit of img_2 on the person of img_1. Only swap the outfit, keep the pose and facial features… exactly the same" ([TikTok @learnwithkayo](https://www.tiktok.com/@learnwithkayo/video/7577005055123950855)). That way the person image's "complete look" authority agrees with the product instead of fighting it. Reject the reference if the rhinestone panel differs from the real photo. Use an AI-generated face, not a real person's: Genjutsu's filter blocked even a brand's licensed ambassador faces ([r/generativeAI](https://www.reddit.com/r/generativeAI/comments/1wo5yxt/higgsfields_genjutsu/)). The one picture already next to each test clip will likely need these extra angles.

**Product references (faceless).** These are the real product photos: black hoodie back view on white with **no person**, the white version the same way, and ideally a macro of the rhinestone panel. An outfit reference should be "on display, white background. No person in the shot" ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1vbmwxt/again_video_ruined_by_putting_faces_in_the/p18zp5g/)).

**Location plates.** Build each new location by editing an actual source frame in Nano Banana: remove the woman, then change the place. This keeps camera height, lens and perspective identical. Output 9:16, empty, with light from the same direction and of the same quality as the source (cool fluorescent garage; low warm sunset). References should be "visually compatible in perspective and light" ([Dreamina](https://dreamina.capcut.com/ai-video/higgsfield-ai-genjutsu)). Matching light at the plate stage beats asking the model to relight. Users warn that "no model will save the edges" when lighting disagrees ([r/HiggsfieldAI](https://www.reddit.com/r/HiggsfieldAI/comments/1wpxcwc/first_time_using_higgsfield_ai_for_background/pc4we3u/)).

### The runs

| # | Clip | Mode | Change | Question it answers |
|---|---|---|---|---|
| 1 | video_1 | Object Swap | Person only (Template A) | Does the hoodie survive a person swap across 9 cuts? |
| 2 | video_1 | Object Swap | Same refs, **no prompt** (or the one-liner "Replace the woman in @Video1 with the woman in @Image1.") | Does the prompt help or hurt? (direct A/B with Run 1) |
| 3 | video_2 (boots) | Object Swap | Location only (Template B) | How clean are background swaps: feet contact, edges, light? |
| 4 | video_1 | Object Swap | Person + both locations in one pass (Template C) | Can one pass do the full job? |
| 5 | video_1 | Motion Transfer | Same refs as Run 4 + one anchor still (Template D) | Head-to-head: is Motion Transfer more realistic, and does it keep the hoodie? |
| 6 | video_3 | Winner of 4 vs 5 | Full job | Does the winner generalise? (If video_3 is one continuous take, it is the fairest Motion Transfer test.) |
| 7 | Best clip | Same settings | **720p** final | Final quality |

Decision gates between runs:
- If Run 1 comes back nearly identical to the input (a no-op), add one sentence describing the source action and rerun before moving on.
- If Run 1 destroys the hoodie, add the rhinestone macro as another `@Image` and strengthen retention line 2 before Run 4.
- If Run 4 breaks at cuts, try the two-block location split before Run 5.

The anchor still in Run 5 is a Nano Banana composite: the new woman in the hoodie, from behind, in the new garage, posed like the first frame. It follows the cross-tool evidence that an edited first frame drives the best propagation ([AnyV2V](https://arxiv.org/html/2403.14468v3); [Luma Modify guide](https://lumalabs.ai/learning-hub/ray3-modify-user-guide)). Genjutsu has no dedicated start-frame slot, though, so its effect is one of the things Run 5 tests.

### Copy-ready prompts

The prompts follow Higgsfield's DETAILED template order: declare the references, state the keep-lock, number the operations, then lock everything else. Replace brackets with what is actually visible. The descriptions must match the images.

**Template A: Object Swap, new person, same backgrounds**
```
@Image1 and @Image2 are the same woman, Mara: @Image1 front full-body, @Image2 back full-body. [Hair: long straight dark-brown hair falling over the hood; slim build.] @Image3 is the black hoodie, back view, with the rhinestone mesh back panel. @Image4 is the white version of the same hoodie.

Video edit. Keep this @Video1 clip exactly as it is: the same shots and cuts, camera moves, framing, the parking-garage and rooftop backgrounds, lighting, pacing and timing. Change only the woman.

1. Replace the woman in @Video1 with Mara from @Image1 and @Image2 in every shot, through every cut, turn and motion blur. Mara performs the original walk, poses, hand movements, position and size in frame. The original woman must never appear in any frame.
2. Mara wears exactly the hoodie worn in @Video1: the white hoodie from @Image4 in the opening shot [0.0–1.0 s], and the black hoodie from @Image3 in every later shot, its rhinestone mesh back panel identical in pattern, size, position and sparkle.

Everything else (backgrounds, lighting, camera moves, cuts and all timing) stays exactly the same. Photorealistic phone footage, natural skin and hair, real fabric texture.
```

**Template B: Object Swap, same person, new location (boots clip)**
```
@Image1 is the new location: [empty city sidewalk at golden hour, light from the left].

Video edit. Keep this @Video1 clip exactly as it is: the same person, her outfit and the boots, every step, the same shots and cuts, camera moves, framing, lighting on her, pacing and timing. Change only the location.

1. Replace the background in @Video1 with the location from @Image1 in every shot, at the same camera height, angle and perspective as each original shot. The ground meets the boots exactly where the original ground did, with soft contact shadows under every step.

Everything else (the person, the boots, the motion, the camera and all timing) stays exactly the same. Photorealistic phone footage.
```

**Template C: Object Swap, new person + new locations.** Use Template A's reference block and add `@Image5` (new garage plate) and `@Image6` (new rooftop plate). Change the keep-lock to "Change only the woman and the two locations". Add this operation:
```
3. Replace the underground parking garage in the shots from [0.0–5.2 s] with the location from @Image5, and the rooftop parking deck in the shots from [5.2–10.3 s] with the location from @Image6, keeping each shot's camera height, angle and perspective and the same light direction.
```

**Template D: Motion Transfer, new person + new world**
```
@Image1 and @Image2: Mara, front and back full-body [hair description]. @Image3: the black hoodie, back view, rhinestone mesh back panel. @Image4: the white version. @Image5: location A, an underground parking garage. @Image6: location B, a rooftop parking deck at sunset. @Image7: how the first shot looks.

Use @Video1 only for motion, camera and timing: keep every shot, cut, camera move, walk, pose, turn and its timing exactly as in @Video1, in the same vertical framing.
Recast the woman as Mara from @Image1 and @Image2, wearing the black hoodie from @Image3 with its rhinestone mesh back panel identical (the white hoodie from @Image4 in the opening shot [0.0–1.0 s]).
Shots from [0.0–5.2 s] take place in @Image5; shots from [5.2–10.3 s] take place in @Image6.
Photorealistic handheld phone footage, natural light, real fabric texture.
```

### Resolution strategy

Draft every run at **480p**. A 1080p test "costs more than three times a 480p draft" ([Rekreate](https://rekreate.ai/news/higgsfield-genjutsu)), and one user unstuck a frozen job by switching "from 720p to 480p" ([r/generativeAI](https://www.reddit.com/r/generativeAI/comments/1wf9pwl/why_higgsfield_genjutsu_is_taking_so_long/paxsrjf/)). Judge 480p drafts on **structure**: is it the right person in every shot, is the panel there in the right place and shape, are the cuts intact. Do not judge them on sparkle. "480p vs 720p is mostly noticeable in fine textures like hair and fabric edges" ([r/generativeAI](https://www.reddit.com/r/generativeAI/comments/1wueuk6/why_is_genjutsu_so_expensive/pd69ho7/)).

A higher-resolution render is a **new generation, not the same take sharpened**, so the final may differ from the approved draft. Render the final at **720p**, which matches the source and is what Higgsfield's edit workflow calls "recommended/faster" (Higgsfield MCP connector, Ad Multiplier). 1080p only upsamples a 720p source. If the 720p final is soft, upscale conservatively: users report Magnific "cleans that up well" ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1wjdm66/which_do_you_think_is_the_most_costeffective_v2v/paxbdp8/)). A comparison found sharpness-first upscalers like Topaz can look "over-processed" ([fal.ai](https://blog.fal.ai/comparing-the-best-ai-upscalers-for-video-and-images/)). Then match colour and grain across shots in CapCut, re-add the text, and lay the original music back in, since Genjutsu's audio handling is undocumented ([Riffkit](https://riffkit.ai/blog/how-to-use-higgsfield-genjutsu)).

### What to check in each output

Put the output on the CapCut track above the source and toggle between them frame by frame. Stop at every cut and every moment of contact: "An object can look convincing in one frame and still be wrong" ([The Rundown](https://app.therundown.ai/guides/swap-the-product-and-keep-the-performance-with-higgsfield)).

| Check | What failure looks like |
|---|---|
| Identity across cuts | Hair length or colour, build or face changes from shot to shot; the original woman survives in any frame |
| Hoodie panel | Rhinestone pattern simplified, moved, resized or "breathing" between frames; wrong colour in shot 1 (white) |
| Hands | Hands into pockets or sleeves turn into "melted stumps" ([r/generativeAI](https://www.reddit.com/r/generativeAI/comments/1wueuk6/why_is_genjutsu_so_expensive/pd6ac8t/)) |
| Edges | Halo or crawling outline where the black hoodie meets a dark garage background |
| Feet (boots) | Floating feet, sliding steps, missing contact shadows |
| Light and colour | New elements "much more saturated and higher contrast" than the rest ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1woh8h6/seedance_25_and_edit_mode_even_regular_sd_2520/)); sunset rim light on her but not in the scene |
| Structure | Same number and timing of cuts, same camera moves, 9:16, same duration, 30 fps, no extra people, no invented text |

## Costs, limits and the ways it breaks

The app price is **40 / 104 / 144 credits for 15 s at 480p / 720p / 1080p** ($2.00 / $5.20 / $7.20), the same for both modes ([Higgsfield blog](https://higgsfield.ai/blog/higgsfield-genjutsu)). If the price scales linearly (unconfirmed), a 10.3 s clip costs about **27 / 71 / 99 credits**, and the Generate button shows the real figure first ([higgsfield.ai/genjutsu](https://higgsfield.ai/genjutsu)). The API charges per second, rounded up: $0.318, $0.681 or $1.632 ([open.higgsfield.ai](https://open.higgsfield.ai/models/higgsfield/genjutsu/motion-transfer/v1.0/playground)). That is about $3.50 / $7.49 / $17.95 for an 11 s billing unit, roughly double the app rate. **The seven-run plan costs roughly 235 app credits (about $12):** six 480p drafts at ~27 credits plus one 720p final at ~71. Re-rolls cost full price, and failed renders are usually refunded ([Riffkit](https://riffkit.ai/blog/how-to-use-higgsfield-genjutsu)).

Through the Higgsfield MCP connector, free Genjutsu attempts are unavailable, and the 30+ presets are not exposed. Only `resolution` is settable (Higgsfield MCP connector, `/genjutsu` recipe and model cards). Users report the biggest practical risk is queues, not quality: jobs "still processing… 4 days now", clustered on free generations ([r/generativeAI](https://www.reddit.com/r/generativeAI/comments/1wf9pwl/why_higgsfield_genjutsu_is_taking_so_long/)).

Known failure modes map directly onto his footage:
- Fine fabric texture softens at low resolution.
- Hands disappear into pockets.
- Edges break on "fast, complex motion" ([ahmetbalaman.com](https://ahmetbalaman.com/en/blog/higgsfield-genjutsu-video-to-video-with-blender-en/)), which fits quick cuts and walking.
- The listed set is "identity drift, extra characters, warped hands, floating feet, changing costumes, altered choreography" ([Media.io](https://www.media.io/video-effects/higgsfield-ai-genjutsu-tutorial.html)).
- Real-person source footage triggered privacy errors on Seedance 2.5 V2V elsewhere: "input video… may contain real person" ([r/Seedance_AI](https://www.reddit.com/r/Seedance_AI/comments/1wnveqr/seedance_25_videotovideo_workflow_reshoot_the/pcqzxpg/)). Whether Genjutsu shares that filter is unknown.

If Genjutsu fails on multi-cut material, the closest documented alternative is **Runway Aleph 2.0**. It "processes multi-shot reels as one composition and propagates edits across cuts" and accepts up to five pinned anchor stills ([Runware Aleph 2.0 docs](https://runware.ai/docs/models/runway-aleph-2-0/guides/editing-video)).

## What is still unknown, and what the tests will answer

Five questions have no published answer:
1. **Hoodie survival:** does either mode keep a worn product identical? Runs 1, 4 and 5 answer this for his hoodie.
2. **Does the prompt help?** No one has run reference-only against reference + prompt on Genjutsu. Runs 1 and 2 answer it.
3. **Cuts:** how does Genjutsu treat hard cuts with roughly 1 s shots? Runs 1 and 4 show whether identity and locations hold at cut boundaries. Run 5 shows whether Motion Transfer re-solves the world per shot.
4. **Back-view subjects:** do bodies seen mostly from behind confuse the motion signal? Pose estimators have front/back ambiguity, but no source tested this.
5. **Output format:** are 9:16, 30 fps and duration preserved exactly? Riffkit lists aspect-ratio handling as "unknown" ([Riffkit](https://riffkit.ai/blog/how-to-use-higgsfield-genjutsu)).

What the tests cannot settle is the underlying model. It stays unconfirmed, so behaviour can change without notice. Treat any winning recipe as dated to this month and re-check it after Higgsfield updates.

## Conclusion

Higgsfield frames Genjutsu as "keep the motion, rebuild the rest" versus "change one thing". For e-commerce the more useful question is **which pixels of the source you trust**. In a product ad, the real garment is the most valuable thing in the shot. Object Swap lets the model keep looking at it, while Motion Transfer asks the model to remember it from a still. That flips the intuitive choice: the "rebuild everything" mode is the riskier one for product videos, however good its showcases look.

The leverage is in the prep, not the prompt. A faceless product reference, a back-view character reference wearing the real hoodie, and location plates edited from his own frames do more for realism than any wording. The prompt's job is narrow: map, retain, lock. If Runs 1–5 confirm Object Swap, Daniel can make one character set and one set of location plates per product and reuse them across every clip. At about 27 credits per 480p check, a new person or location costs a few dollars per proven ad.
