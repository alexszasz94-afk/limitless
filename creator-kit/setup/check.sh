#!/bin/bash
# Checks everything the kit needs. Prints OK / MISSING for each item.
ok(){ echo "OK       $1"; }; miss(){ echo "MISSING  $1"; M=1; }
PY=python3; command -v python3 >/dev/null || PY=py
command -v ffmpeg  >/dev/null && ok ffmpeg  || miss "ffmpeg"
command -v ffprobe >/dev/null && ok ffprobe || miss "ffprobe (comes with ffmpeg)"
command -v yt-dlp  >/dev/null && ok yt-dlp  || miss "yt-dlp"
command -v curl    >/dev/null && ok curl    || miss "curl"
command -v $PY     >/dev/null && ok "$PY"   || miss "python3"
$PY -c "import PIL" 2>/dev/null && ok "python pillow" || miss "python pillow (pip install pillow)"
$PY -c "import numpy" 2>/dev/null && ok "python numpy" || miss "python numpy (pip install numpy)"
cd "$(dirname "$0")/.."
for f in motion/broll-motion.mp4 products/snoopy/refs/front-closed.jpg products/princess/refs/front.jpg engine/fonts/TikTokSans-w700-semicond.ttf; do [ -f "$f" ] && ok "$f" || miss "$f (the zip was not fully extracted)"; done
[ -z "$M" ] && echo "ALL GOOD" || echo "SOMETHING IS MISSING"
