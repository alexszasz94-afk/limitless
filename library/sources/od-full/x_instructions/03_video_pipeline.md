# 03 — How one ad is made

The detailed, command-by-command version is `x_systems/video_boards/WORKFLOWS.md`. This page
is the overview plus the creative rules learned the hard way.

## The shape of a video

- 9:16, about 11–18 s. Shot ids: **C01 = the hook** (4–5 s, decides everything), C02–C04
  B-roll 1 (the product), C05–C07 B-roll 2 (the payoff). Each product keeps one fixed slot
  list.
- On-screen hook text from the Hooks Board (`x_systems/hooks/text_on_screen.txt`), plus a
  song you have the rights to use (the original songs folder is not included) or original audio.
- Finished exports go to `<PRODUCT>/videos_to_post/video_<N>.mp4`.

## The round, step by step

1. **Plan.** Pick the hook and the shots. To repeat a shot from an earlier video, copy its
   prompt **verbatim** from that video's `prompts.md` → `## Verified record — Higgsfield`
   → `### C<NN>` → the `— IN THE CUT` entry, and change only the nouns that physically
   differ (CLAUDE.md rule 3).
2. **Frames.** Generate one starting frame per shot in Higgsfield (`gpt_image_2` /
   `gpt_image_2_5`, settings as in the source shot). Attach two references: the one that
   fixes the layout and the one that fixes the look (the canonical packshot from
   `product_images/` for anything showing the product or box). Save as
   `starting_frames/v<N>_c<NN>_g<K>.png`, write the take into `prompts.md`, then add a card
   with `x_systems/video_boards/tools/add_card.py`. It shows as **FRAME FOR REVIEW**.
3. **Review 1.** Your user opens the board, presses **Review**, approves or rejects each
   frame, clicks **Copy decisions** and pastes the lines to you. Apply them with
   `x_systems/video_boards/tools/decide.py` (WORKFLOWS.md §4).
4. **Clips.** Animate **only approved frames** (`seedance_2_5`, usually 720p/5s; settings
   as in the source shot). Anything that moves must already be in the frame. Save as
   `clips/v<N>_c<NN>_g<K>.mp4`, archive the prompt, add the card: **CLIP FOR REVIEW**.
5. **Review 2.** Same as review 1, for clips.
6. **Upscale** the chosen clips (same name, in `clips/upscaled/`). Higgsfield's ByteDance
   upscaler was used; `x_research/video_upscale_models_research.md` compares options.
7. **Cut** in CapCut with the hook text and song, export to `videos_to_post/`, and mark
   the cut on the board (WORKFLOWS.md §6).
8. **Run the five checks** (CLAUDE.md rule 1). All must exit 0.

One generation per shot, then stop and wait. Never re-roll on your own. Nothing is ever
overwritten: a new take is the next `g<K>`.

## Swanlift: motion transfer (the columns board)

The Swanlift board uses `"layout": "columns"` (SYSTEM.md §2.6). There is one column per run:
row 1 is the competitor reference reel, row 2 the new woman and room (cast from Pinterest,
see `skills/pinterest-casting.md`), row 3 the final video made with Higgsfield **Genjutsu**
motion transfer. Each run's references are approved (stage `refs`) before anything is
generated. Background: `x_research/genjutsu_motion_transfer_vs_object_swap.md` and
`x_research/genjutsu/`.

## Where the creative rules are

- Each board's top panels ("Frame rules — what the image rounds taught", "Clip rules", the
  product `spec` panel) hold the lessons for that product: canonical packshot, box
  dimensions, what leaks from a reference, what the model refuses.
- `x_research/*_prompting_guide.md`: how each model wants to be prompted.
- `prompts.md`: every take, including failures and why they failed.

Read the relevant panels and the last few `prompts.md` entries **before** generating.

## Higgsfield ids

The archive's job ids, media ids and `cloudfront.net` URLs belong to the original owner's
Higgsfield account. Your user's account can't open them. Re-upload the local file named
next to an id instead. WORKFLOWS.md §8 explains how ids map to files. New jobs on your
user's account work normally.
