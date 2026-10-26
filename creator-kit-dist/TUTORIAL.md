# Robe Studio — make finished robe videos with Claude Code

You send Claude an Instagram/TikTok link (or just an idea). Claude makes the whole video for you: the hook, a new girl in a new room trying on the robe, the heating remote, the cozy ending, the text on screen and the music. You get one MP4, ready to post. Each video takes about 15–25 minutes and costs about 40–60 Higgsfield credits.

You do NOT need to know how to code. You only type normal sentences.

---

## One-time setup (about 15 minutes)

### 1. Accounts you need
- **Claude** — a Claude Pro or Max subscription (claude.ai). Claude Code is included.
- **Higgsfield** — an account at higgsfield.ai with credits (any paid plan; Ultra is cheapest per video). This is where the images and videos are made.

### 2. Install Claude Code
- **Mac**: open the app **Terminal** and paste:
  ```
  curl -fsSL https://claude.ai/install.sh | bash
  ```
- **Windows**: open **PowerShell** and paste:
  ```
  irm https://claude.ai/install.ps1 | iex
  ```
Close the window and open it again when it finishes.

### 3. Unzip the kit
Unzip `robe-studio.zip` (the single big file — the `cloud-upload` pieces are only for Option B) somewhere easy, for example your Desktop. You get a folder called `robe-studio`.

### 4. Open Claude Code inside the folder
- **Mac**: in Terminal type `cd ` (with a space), drag the `robe-studio` folder into the window, press Enter, then type `claude` and press Enter.
- **Windows**: open the `robe-studio` folder, click the address bar, type `powershell`, press Enter, then type `claude` and press Enter.

The first time, Claude asks you to log in (use your Claude account) and asks if you trust this folder → choose **Yes**. If it asks to use the MCP server **higgsfield** → choose **Yes**.

### 5. Connect Higgsfield (once)
In Claude type:
```
/mcp
```
Choose **higgsfield**, press Enter. A browser window opens: log in to your Higgsfield account and allow access. Go back to Claude.

### 6. Let Claude set everything up
Type:
```
start
```
Claude checks your computer, installs what is missing (ffmpeg, yt-dlp…), checks your credits and uploads the robe pictures to your Higgsfield account. If it asks permission to run something, choose **Yes** (or "Yes, don't ask again"). When it says everything is ready, you're done with setup forever.

---

## Option B — no installing: run it in the browser (claude.ai/code)

Use this if you can't install anything on your computer. Everything runs on a cloud computer.

1. **GitHub** (free account at github.com): click **New repository**, name it `robe-studio`, choose **Private**, click **Create**. On the new page click **uploading an existing file**, drag in ALL the files from the `cloud-upload` folder you received (`robe-studio.zip.part-aa`, `robe-studio.zip.part-ab`, … — GitHub accepts max 25 MB per file, that's why the kit is in pieces) and click **Commit changes**. Wait until all pieces are uploaded.
2. Go to **claude.ai/code**, connect your GitHub account and pick the `robe-studio` repository.
3. **Higgsfield connector** (once): open https://claude.ai/customize/connectors, find **Higgsfield**, click **Connect** and log in to Higgsfield.
4. **Cloud environment** (once): in claude.ai/code click the cloud icon / environment menu → **Add environment** (or **Edit**):
   - **Name**: `robe-studio`
   - **Network access**: **Limited** (or **Custom**) with **Allow package managers** ticked, and in **Allowed domains** paste the whole list from `setup/allowed-domains.txt`:
     ```
     *.higgsfield.ai
     *.cloudfront.net
     *.instagram.com
     *.cdninstagram.com
     *.fbcdn.net
     *.facebook.com
     *.tiktok.com
     *.tiktokcdn.com
     *.tiktokv.com
     *.pinterest.com
     *.pinimg.com
     *.youtube.com
     *.googlevideo.com
     *.ytimg.com
     huggingface.co
     *.huggingface.co
     *.hf.co
     ```
   - **Setup script**: paste the whole content of `setup/cloud-setup.sh`:
     ```
     #!/usr/bin/env bash
     set -e
     apt-get update -qq && apt-get install -y -qq ffmpeg >/dev/null
     pip install -q --break-system-packages yt-dlp pillow numpy faster-whisper || pip install -q yt-dlp pillow numpy faster-whisper
     ```
   - Save.
5. Start a new session in that environment (with the Higgsfield connector on) and send as the first message:
   > join the pieces with `cat robe-studio.zip.part-* > robe-studio.zip`, unzip it and move everything from the robe-studio folder into the root of the repo (including the hidden .claude folder and .mcp.json), delete the zip, the pieces and the empty folder, commit and push, then read CLAUDE.md and run start
   After that first time, start every new session with just `start`.
6. From then on just type `start` and `new video ...` like everywhere else. Each finished video (`output/<name>/<name>-FINAL.mp4` + `caption.txt`) is committed and pushed by Claude — open your repo on github.com → `output` → the video → **Download** (the ⬇ button).

If a download fails with a "network"/"domain" error, Claude tells you which domain to add to **Allowed domains** — add it, then start a new session.

---

## Making a video

Type one line, for example:
```
new video https://www.instagram.com/reel/XXXXXXXX/ snoopy
```
or
```
new video princess — girl at a Christmas market unwraps a big gift and it's the robe
```
That's it. Claude tells you what it's doing step by step. At the end you get:
- `output/<name>/<name>-FINAL.mp4` — the video, ready to post (1080x1920, text and music included)
- `output/<name>/caption.txt` — a caption with hashtags

Want a change? Just say it in normal words, e.g. `fix: make the text smaller`, `fix: the hood looks wrong in the last shot`, `use another song`. Claude redoes only that part.

### Other things you can type
- `credits` — how many credits you have left and how many videos that is.
- `new video <link> snoopy` / `... princess` — choose the robe.
- Before each video Claude asks which cozy ending you want: the classic one (free) or your own idea — just write it. Changing it often keeps your account fresh. You can also write it right away: e.g. `new video <link> princess cozy: reading a book on the bed` — use a different one each time, the account stays fresh.
- `what can you do?` — Claude explains.

### Tips for great results
- The best links are short reels (10–20 s) with a clear hook in the first 3 seconds.
- Each video automatically uses a new girl and a new room. The kit comes with 13 of each; when they run out, Claude finds new ones on Pinterest by itself, looks at them and keeps only the good ones. Only if Pinterest doesn't work will it ask you for photos (about 20 women + 20 cozy Christmas rooms, real, bright, high quality). You can also type `new people` or `new rooms` anytime.
- Don't close Claude while it's working. If your computer sleeps, just type `continue`.

### If something goes wrong
- "Higgsfield not connected" → type `/mcp`, choose higgsfield, log in again.
- "Not enough credits" → add credits on higgsfield.ai.
- Anything else → type `what happened?` and Claude explains and fixes it.
