#!/bin/bash
# make-demo.sh <take.mp4> <out.mp4> <end_s> <music.mp3> <music_start_s>
# B-roll demo: trimmed take + Christmas music (no Kling/room sound), no text
t=$1; o=$2; e=$3; m=$4; ms=$5
ffmpeg -v error -y -ss 0.04 -t $e -i "$t" -ss $ms -i "$m" -filter_complex "[1:a]volume=0.75,atrim=0:$e,afade=t=out:st=$(python3 -c "print($e-0.6)"):d=0.6[a]" -map 0:v -map "[a]" -c:v libx264 -crf 21 -pix_fmt yuv420p -c:a aac -b:a 128k -shortest "$o"
