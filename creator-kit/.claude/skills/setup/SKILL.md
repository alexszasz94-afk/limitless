---
name: setup
description: First run / "start" — checks the computer tools, the Higgsfield connection and credits, and uploads all reference files to Higgsfield once (IDs saved in state/media.json). Run when the creator types start, setup, or before the first video.
---
1. Run `bash setup/check.sh`. If something is missing, install it yourself:
   - macOS: `brew install ffmpeg yt-dlp` (if `brew` is missing, install Homebrew with the official one-line command from brew.sh, then retry), `python3 -m pip install --user pillow numpy`.
   - Windows: `winget install Gyan.FFmpeg` and `winget install yt-dlp.yt-dlp`, `py -m pip install pillow numpy`. On Windows use `py` where the docs say `python3`.
   - Linux: `sudo apt-get install -y ffmpeg python3-pip && pip install --user yt-dlp pillow numpy`.
   Run the check again until everything says OK.
2. Higgsfield: call `balance`. If the Higgsfield tools are missing or fail, tell the creator: "Type /mcp, choose higgsfield, press Enter and log in to your Higgsfield account in the browser that opens, then type start again." Stop until it works.
3. Read `state/media.json` (create `{}` if missing). For every file below that has no id yet, upload it (see "Uploading a local file" in CLAUDE.md) and save the id under the key shown:
   - `motion` ← `motion/broll-motion.mp4` (video)
   - Snoopy: `snoopy_front_closed`, `snoopy_front_open`, `snoopy_back`, `snoopy_hood`, `snoopy_pouch`, `snoopy_detail`, `snoopy_box` ← `products/snoopy/refs/*.jpg` (names in PRODUCT.md)
   - Princess: `princess_front`, `princess_back`, `princess_pouch_open`, `princess_pouch_feet` ← `products/princess/refs/*.jpg`
   Upload ONE file per `media_upload` call (exactly as in CLAUDE.md), PUT it with curl (must print 200), then confirm: one `media_confirm` with `type: "video"` for the motion clip and one with `type: "image"` for all the image ids. Save state/media.json after every file so nothing is uploaded twice if something stops.
4. Tell the creator in 3 lines: everything is ready, how many credits they have (≈ how many videos), and that they can now type `new video <Instagram link or idea>` and say `snoopy` or `princess`.
