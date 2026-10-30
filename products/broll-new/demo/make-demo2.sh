#!/bin/bash
# make-demo2.sh <video-only.mp4> <out.mp4> <music.mp3> <music_start> — music only, loudnorm -14, fade 0.6
v=$1; o=$2; m=$3; ms=$4
e=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$v")
ffmpeg -v error -y -i "$v" -ss $ms -i "$m" -filter_complex "[1:a]atrim=0:$e,loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=out:st=$(python3 -c "print(float('$e')-0.6)"):d=0.6[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 128k -shortest "$o"
