#!/bin/bash
# assemble.sh N COZY_START COZY_END -> final/broll-N.mp4 (master) + page/v/N.mp4 (light)
set -e
cd /home/user/limitless/products/lot30
mkdir -p final page/v page/img
read c1 c2 c3 <<< $(python3 -c "import json;c=json.load(open('cuts.json'))['$1'];print(*c)")
E=$(python3 -c "print(round($c2-0.08,2))")
F="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p"
ffmpeg -v error -y -ss 0.15 -to $E -i broll/b$1.mp4 -ss $2 -to $3 -i cozy/v$1.mp4 \
 -filter_complex "[0:v]$F[a];[1:v]$F[b];[a][b]concat=n=2:v=1:a=0[v]" -map "[v]" -an -c:v libx264 -crf 18 -preset medium final/broll-$1.mp4
ffmpeg -v error -y -i final/broll-$1.mp4 -c:v libx264 -crf 26 -preset medium -movflags +faststart -an page/v/$1.mp4
ffmpeg -v error -y -ss 1.5 -i final/broll-$1.mp4 -frames:v 1 -vf scale=540:-1 -q:v 4 page/img/p$1.jpg
echo "broll-$1 $(ffprobe -v error -show_entries format=duration -of csv=p=0 final/broll-$1.mp4)s page $(du -h page/v/$1.mp4 | cut -f1)"
