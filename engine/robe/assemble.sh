#!/bin/bash
# usage: assemble.sh CODE GEN.mp4 OUT.mp4 a b c
S=/tmp/claude-0/-home-user/d10e41e8-67eb-5ee5-9e56-7eba5b90f258/scratchpad/g3
K=$1; G=$2; O=$3; A=$4; B=$5; C=$6
D=$S/drv_$K.mp4
ffmpeg -v error -y -i "$G" -i $S/conn_$K.mp4 -i $S/ctl_$K.mp4 -i $D -filter_complex "\
[0:v]fps=30,scale=720:1280,setsar=1,split[g1][g2];\
[g1]trim=0:$A,setpts=PTS-STARTPTS[p1];\
[g2]trim=start=$C,setpts=PTS-STARTPTS[p3];\
[1:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p2a];[2:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p2b];\
[p1][p2a][p2b][p3]concat=n=4:v=1:a=0[v]" -map "[v]" -map 3:a -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k -shortest -movflags +faststart "$O"
