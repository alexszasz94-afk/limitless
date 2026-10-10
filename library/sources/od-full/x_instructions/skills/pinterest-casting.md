---
name: "pinterest-casting"
description: "Cast the new woman and room for a motion-transfer remake of a competitor reel - analyse the reel shot by shot, search Pinterest in Chrome, inspect finalists full-size, shortlist for Daniel, save the pick."
---

<!-- A procedure the original owner ran as a Claude skill (copied 2026-10-07). "Daniel" = the original owner: read it as your user. To use it as a skill again, save this file as SKILL.md in a skill folder named pinterest-casting. -->


# Pinterest casting for reel remakes

Daniel remakes competitor reels with Higgsfield Genjutsu motion transfer (`hf_mult_motion_control`):
the reel drives the motion, and two pictures decide how the new video looks - **the new woman** and
**the new room**. This skill finds those two pictures on Pinterest. Use it when Daniel says "find a
new woman / character / room for video N", "better character", "more realistic woman", or before
any new remake. Every rule here exists because breaking it already produced a bad video once.

**The flow:** analyse the reel -> write the casting brief -> search Pinterest in Chrome -> first cut
from thumbnails -> inspect finalists at full size -> shortlist to Daniel -> Daniel picks -> save as
the next reference, record it, put it on the board. No Higgsfield call and no credits in this skill.

## Hard rules

1. **Daniel's casting rule (2026-10-05):** "Use terms like 30 years old women, don't look for
   specifically ai generated, we can use any image from pinterest." Hyperrealistic, natural women
   around 30. Real photos are fine. Never search for "AI", "AI generated", "AI model", "virtual
   influencer" - the v11-v15 picks found that way were rejected as not realistic. (An earlier round,
   v1-v10, used only AI faces; that rule is replaced.) Never pick a celebrity or a known influencer.
2. **Daniel makes the final pick.** Claude delivers a shortlist with a recommendation. Only if Daniel
   already said "just pick" or he is away and said to proceed, use the recommended pick and say so.
3. **One woman and one room per video, used in every clip and every part of it.** v1 and v5 were
   split into parts and the room changed at the cut - that is a failed video. Different videos get
   different women and rooms unless Daniel says otherwise.
4. **The photo's clothes leak into the video.** Genjutsu copies what the woman wears in her picture:
   the white T-shirt in v4 and the black T-shirt in v12 appeared under the bra in some shots and not
   in others. Pick photos whose upper-body clothing is minimal, plain and fitted, or already close to
   what she wears in the reel.
5. **Browser: Claude in Chrome** (`mcp__claude-in-chrome__*`), Daniel's real Chrome, logged in to
   Pinterest. Read the `chrome-browser` skill first and load the tools in one ToolSearch call
   (tabs_context_mcp, tabs_create_mcp, tabs_close_mcp, navigate, computer, javascript_tool,
   browser_batch, find). If the extension does not respond, stop and ask Daniel; the fallback below
   (Pinterest's web endpoints from the workspace with curl) is only for when he says so.
6. **Nothing is shortlisted without being seen at full size** (Step 4). A thumbnail is a lead.
7. **Tell Daniel every decision that changes what he gets** (a compromise on body type, a room
   that does not match the reel's light) - in one line, before or with the shortlist.
8. **Drive rules:** never overwrite, never reuse an `r` number, never open notes.txt / guides.txt /
   keys.txt / board_notes.txt. Unwanted files go to `to_delete/` at the drive root. Verify every
   write with md5 (the mount can corrupt writes).

## Step 1: Analyse the reference reel (do this extremely carefully)

The brief decides everything that follows. A woman who looks great but cannot play this reel is
a bad pick.

**Get the reel.** It is `<PRODUCT>/content/video_N_assets/references/vN_c01_r1.mp4` (byte copy of
the competitor reel) or `<PRODUCT>/competition/selected/rank_XX_<account>_<code>.mp4`. Stage it
into the workspace (`device_stage_files`) - images must be looked at in the workspace with Read.

**Find every cut** (adjust the threshold until the list matches what you see):
```bash
ffprobe -v error -show_entries stream=width,height,r_frame_rate,nb_frames,duration -of csv=p=0 reel.mp4
ffmpeg -i reel.mp4 -vf "select='gt(scene,0.25)',showinfo" -f null - 2>&1 | grep -o 'pts_time:[0-9.]*'
```

**Look at all of it, not a sample:**
- A 2-frames-per-second overview: `ffmpeg -i reel.mp4 -vf "fps=2,scale=180:-1,tile=8x4" -q:v 3 ov_%02d.jpg`
  and Read every sheet.
- For every shot: its first, middle and last frame at full resolution
  (`ffmpeg -ss T -i reel.mp4 -frames:v 1 shotK_mid.png`). Read them.
- If a moment is unclear (a hand on the chest, a turn, the hair), extract every frame of that half
  second and look again.

**Write the casting brief** (keep it in the workspace; it goes into prompts.md in Step 6):

| Section | What to write down |
|---|---|
| Shot list | Per shot: time range (s and frame), framing (close-up / waist-up / full body), camera (handheld selfie, phone on a stand, mirror), camera height and distance, what she does, front or back view, bra colour |
| Woman | Apparent age, build (slim / athletic / curvy / plus-size), bust size, height in frame, skin tone, hair length + style + colour, what she does with her hair (ties it, flips it, it covers her face), glasses, jewellery, tattoos, makeup, does she talk to camera (then the face must be clear and frontal in the photo) |
| Wardrobe | Lower body in every shot (this becomes the prompt's garment line), upper body before the bra goes on (bare, tank, T-shirt) |
| Room | Room type, what is behind her (bed, wall, window, wardrobe, mirror, door), where the light comes from, day or night, warm or cool light, how much floor space she uses, how much of the room the camera sees, ceiling visible or not, furniture she touches or sits on |
| Risks | Shots with bare skin or hands on the chest (Higgsfield refuses these as nsfw), hair that hides the face, fast spins, extreme angles |
| Search plan | 4-6 woman queries and 3-4 room queries built from the brief (Step 2) |

Send Daniel a 3-4 line summary of the brief at the start ("Video N: slim brunette ~30, long hair she
ties up, talks to camera; warm evening bedroom, bed behind her, window left. Searching now.") and
carry on - do not wait for an answer unless something is truly ambiguous.

## Step 2: Search Pinterest in Chrome

`tabs_context_mcp` (createIfEmpty), work in one new tab, close it at the end.

**Woman queries** - always start from "30 year old woman", then add brief traits, one or two at a
time: hair ("long dark hair", "messy bun", "curly"), build ("curvy", "petite", "plus size"), skin or
ethnicity if the brief calls for it, and a real-photo setting ("selfie at home", "mirror selfie",
"natural no makeup", "candid", "iphone photo"). Good photos are usually real-life selfies or casual
shots with even light; avoid studio fashion shoots, heavy filters and anything "aesthetic".

**Room queries** - describe what the camera sees in the reel: "<cozy / bright / minimalist> bedroom
<daylight / evening lamp light>", "apartment bedroom vertical photo", "real bedroom interior iphone",
plus one distinctive element (big window, fairy lights, wooden floor, white walls). Real lived-in
rooms beat 3D renders and showroom catalogues.

**Collect pins from a search page** (URL `https://www.pinterest.com/search/pins/?q=<query>`; the
grid is virtualised, so collect while scrolling). Strip the `https://i.pinimg.com/` prefix from
returned text - long URLs and some strings get blocked by the extension.
```js
await (async()=>{window.PC=window.PC||{};
 const grab=()=>document.querySelectorAll('a[href*="/pin/"]').forEach(a=>{const m=(a.getAttribute('href')||'').match(/\/pin\/(\d+)/);const im=a.querySelector('img');
   if(m&&im&&!PC[m[1]])PC[m[1]]=(im.currentSrc||im.src).replace('https://i.pinimg.com/','')});
 for(let i=0;i<8;i++){grab();scrollBy(0,1200);await new Promise(r=>setTimeout(r,900))}grab();
 return Object.entries(PC).map(([id,p])=>id+' '+p).join('\n')})()
```
Each line is `<pin id> <size>/<aa>/<bb>/<cc>/<hash>.<ext>`. Save the lines into a workspace file per
query (navigation wipes `window.PC`).

**"More like this" is the best search.** When a hit is close to the brief, open its pin page
(`https://www.pinterest.com/pin/<id>/`), scroll twice, and collect the related pins:
```js
await (async()=>{for(let i=0;i<3;i++){scrollBy(0,1200);await new Promise(r=>setTimeout(r,900))}
 const R=document.querySelector('[data-test-id="relatedPins"]');const out=[];
 R&&R.querySelectorAll('a').forEach(a=>{const m=(a.getAttribute('href')||'').match(/\/pin\/([0-9]+)/);const im=a.querySelector('img');
   if(m&&im)out.push(m[1]+' '+(im.currentSrc||im.src).replace('https://i.pinimg.com/',''))});
 return out.join('\n')})()
```
Do 2-3 rounds of this from the best hits. Aim for 60-120 candidates per role.

## Step 3: First cut from thumbnails

Build numbered contact sheets in the workspace (Pinterest images download fine with curl from the
workspace) and Read every sheet. Script (input: lines `n pinid path`):
```python
import sys, os, subprocess
from PIL import Image, ImageDraw
idx=[l.split() for l in open(sys.argv[1]) if l.strip()]; T=sys.argv[2]+'_t'; os.makedirs(T,exist_ok=True)
for n,pid,p in idx:
    out=f'{T}/{n}.jpg'; h=p.split('/',1)[1].rsplit('.',1)[0]
    if not os.path.exists(out): subprocess.run(['curl','-sSf','-o',out,f'https://i.pinimg.com/236x/{h}.jpg'])
W,H,cols,per=236,330,10,40
for s in range(0,len(idx),per):
    ch=idx[s:s+per]; sh=Image.new('RGB',(cols*W,((len(ch)+cols-1)//cols)*H),'white'); d=ImageDraw.Draw(sh)
    for k,(n,pid,p) in enumerate(ch):
        try: im=Image.open(f'{T}/{n}.jpg').convert('RGB')
        except Exception: continue
        im.thumbnail((W-4,H-4)); x,y=(k%cols)*W,(k//cols)*H; sh.paste(im,(x+2,y+2))
        d.rectangle([x,y,x+34,y+18],fill='black'); d.text((x+3,y+3),n,fill='white')
    sh.save(f'{sys.argv[2]}_{s//per}.jpg',quality=85)
```
Cut to 12-20 per role. At thumbnail size judge only: one person, face visible, age, build, hair,
framing, clothing, obvious filters or text. Realism is judged in Step 4, not here.

## Step 4: Inspect the finalists at full size

**Download the original:** `https://i.pinimg.com/originals/<aa>/<bb>/<cc>/<hash>.jpg`; if that is
not 200, try `.png`, then `.webp`, then the `1200x/` and `736x/` sizes. Record which one worked and
its pixel size. Optional extra info per pin (pinner, board, source link, Pinterest's own AI label):
```bash
curl -s -H 'X-Pinterest-PWS-Handler: www/pin/[id].js' -H 'X-Requested-With: XMLHttpRequest' -H 'Accept: application/json' \
 "https://www.pinterest.com/resource/PinResource/get/?source_url=%2Fpin%2F<ID>%2F&data=%7B%22options%22%3A%7B%22id%22%3A%22<ID>%22%2C%22field_set_key%22%3A%22detailed%22%7D%2C%22context%22%3A%7B%7D%7D"
```
(`resource_response.data`: `images.orig.url/width/height`, `ai_disclosures`, `pinner.username`,
`board.name`, `link`.) An AI label is information, not a reason to drop the image.

**Look at each finalist:** Read the full image, then 1:1 crops (PIL) of the face, both hands, the
hairline and the background edges around her.

Woman - drop it if any of these fail:
- **Realism:** real skin texture (pores, small marks, natural shine), not plastic or airbrushed; eyes,
  teeth and earrings consistent; fingers and hands correct; hair strands that do not melt into the
  background; no warped lines behind her; no beauty filter. Ask: would Daniel scroll past this as a
  real person's photo?
- **Fit with the brief:** about 30; the same build and bust size as the reel's woman (motion
  transfer keeps the reel's poses - a very different body gets distorted); hair that can do what the
  reel's hair does (a short bob cannot tie a bun); face fully visible, frontal or three-quarter, eyes
  open, no sunglasses or hat, not hidden by a phone.
- **Photo:** one person; at least about 1000 px on the short side; nothing written on the image, no
  watermark, no logo; upper-body clothing minimal, plain and fitted (a plain tank, a sports top,
  fitted plain T-shirt only if the reel starts in one) - no prints, jackets, bulky knits; no
  lingerie, bikini or strong cleavage (keeps the nsfw risk down); lower body ideally neutral.

Room - drop it if: people in it; a render or showroom look; light that cannot match the reel (day vs
night, warm vs cool); no free floor where she would stand at the reel's camera distance; the camera
angle is far from the reel's (shot from the ceiling, fisheye, extreme wide angle); text, posters
with words, logos or watermarks; too small (under about 1000 px on the short side).

Keep 4-6 women and 3-4 rooms. Write one line per finalist: what it matches and its trade-off.

## Step 5: Shortlist for Daniel

- Make one contact sheet per role at a readable size (about 480 px tall per image), numbered, and
  send it with `SendUserFile`. Under it, one line per finalist and your recommended pick with the
  reason. Mention any compromise against the brief.
- Open each finalist's pin in its own Chrome tab so he can look at the original.
- Ask which ones (AskUserQuestion with the numbers, or his reply). Then close the tabs you opened.

## Step 6: Save, record, put on the board (after Daniel picks)

**Next free reference number:** look at `video_N_assets/references/`, the video's prompts.md and
`content/lost_takes.txt`; image and video references share one `r` sequence per shot (NAMING.md).
Woman first, then room.

**Save:** download the original on the device (`curl` into `$HOME/work`), convert to PNG with PIL
without resizing (`Image.open(f).convert('RGB').save(out,'PNG')`), copy to
`video_N_assets/references/vN_c01_rK.png`, check md5 of source and copy match. Never overwrite.
If the video has more than one clip, the same pictures are used for every clip (reference them;
record that in each clip's section).

**Record in the video's prompts.md** (a section "New character and room (picked <date>)"):
- File, pixel size, md5; Pinterest pin URL, board, pinner, source link; original image URL and
  that it was converted to PNG with pixels unchanged.
- The search queries that found it and why it was picked (one line, from Step 4).
- **Prompt description of the woman** - face, hair, skin and build only, never clothing, in the house
  style: "a woman around thirty with dark brown hair in a messy updo with loose face-framing
  strands, warm olive skin, a soft confident smile and a slim figure".
- **Lower body in every shot:** the garment from the brief (e.g. "light blue wide-leg jeans").
- **Room description** for the prompt: what the camera sees and the light, e.g. "a cosy bedroom in
  the evening: sloped white ceiling with warm fairy lights, sheer white curtains, a bed with cream
  knit bedding, a wooden chest of drawers and a warm lamp glow".
- The casting brief from Step 1 (shot list + risks), short.
- Rejected picks (if Daniel rejected earlier ones) with his words and their `r` numbers.

**Board:** set the card's `looks` to the new woman and room (`{"label":"Woman","file":...}`,
`{"label":"Room","file":...}`) in `content/_board_thumbs/board_data.json` (read-modify-write with
the board kit's `load_data`/`save_data`), stage `refs` / status `review` until Daniel approves, then
run `x_systems/video_boards/tools/build_board.py "<PRODUCT>"` and the four `_tool/` checks
(check_naming, make_thumbs, mark_lost, check_board) - all must exit 0.

**Report:** one or two lines - what was picked, where it is, and anything he should know (e.g. "her
photo has a grey tank top - prompt keeps her bare-shouldered, watch for the top leaking in").

## When Daniel rejects a pick

Record the rejected file with his exact words, keep it on disk (never reuse its number), turn his
words into a rule for the brief ("too perfect" -> stricter realism check; "too young" -> older
queries), and run Steps 2-5 again. If the same complaint repeats across videos, ask whether to add
it to this skill.

## Technical notes (verified 2026-10-06)

- Pinterest in Daniel's Chrome is logged in (www.pinterest.com). Search
  thumbnails come as `474x/`; related pins as `236x/`; the pin page's main image as `1200x/`.
- `i.pinimg.com` downloads with plain curl from both the workspace and the device - no cookies
  needed. Originals were 714x1280 to 2316x3088 in the test.
- Keep browser batches short (2-4 navigations); a long batch times out but still runs - re-read the
  state afterwards. Returned text with long URLs or encoded strings can be blocked by the extension:
  return ids and short paths.
- Fallback without Chrome (only when Daniel agrees; used for v2/v11-v15 on 2026-10-05): curl
  `https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=<urlencoded /search/pins/?q=<q>>&data=<urlencoded {"options":{"query":"<q>","scope":"pins","page_size":50,"bookmarks":[],"rs":"typed"},"context":{}}>`
  with headers `X-Pinterest-PWS-Handler: www/search/[scope].js`, `X-Requested-With: XMLHttpRequest`,
  `Accept: application/json`. Pins are in `resource_response.data.results[]` (`id`,
  `images.orig.url/width/height`); next page: put `resource_response.bookmark` into `bookmarks`
  until it is `-end-`.
- Viewing: Read shows an image to Claude; very large images are scaled down, so crop the face and
  hands to judge realism.