#!/bin/bash
# check.sh take.mp4 outprefix variant(v3|v4|v5) — sheets for detail verification
t=$1; p=$2; v=$3; S=/tmp/claude-0/-home-user/d10e41e8-67eb-5ee5-9e56-7eba5b90f258/scratchpad
python3 /home/user/limitless/creator-kit/engine/tools.py cuts "$t"
ffmpeg -v error -y -i "$t" -vf "fps=2,scale=140:-1,drawtext=text='%{pts\:flt}':x=3:y=3:fontsize=13:fontcolor=yellow:box=1:boxcolor=black,tile=12x2" -frames:v 1 $S/$p-all.jpg
case $v in
 v4) ffmpeg -v error -y -ss 1.7 -t 4.1 -i "$t" -vf "fps=6,crop=iw:ih*0.55:0:ih*0.45,scale=150:-1,drawtext=text='%{pts\:flt}':x=3:y=3:fontsize=13:fontcolor=yellow:box=1:boxcolor=black,tile=13x2" -frames:v 1 $S/$p-feet.jpg;;
 v3) ffmpeg -v error -y -ss 1.1 -t 5.6 -i "$t" -vf "fps=6,crop=iw:ih*0.55:0:ih*0.45,scale=150:-1,drawtext=text='%{pts\:flt}':x=3:y=3:fontsize=13:fontcolor=yellow:box=1:boxcolor=black,tile=12x3" -frames:v 1 $S/$p-feet.jpg;;
 v5) :;;
esac
