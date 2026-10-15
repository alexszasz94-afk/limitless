#!/bin/bash
# addtext.sh IN.mp4 TEXT.png OUT.mp4
ffmpeg -v error -y -i "$1" -i "$2" -filter_complex "[1]scale=720:1280[t];[0:v][t]overlay=0:0" -c:v libx264 -crf 18 -c:a copy -movflags +faststart "$3"
