#!/bin/bash
# only controller replaced: assemble_ctl.sh CODE GEN OUT b c
S=/tmp/claude-0/-home-user/d10e41e8-67eb-5ee5-9e56-7eba5b90f258/scratchpad/g3
K=$1; G=$2; O=$3; B=$4; C=$5
ffmpeg -v error -y -i "$G" -i $S/ctl_$K.mp4 -i $S/drv_$K.mp4 -filter_complex "\
[0:v]fps=30,scale=720:1280,setsar=1,split[g1][g2];[g1]trim=0:$B,setpts=PTS-STARTPTS[p1];[g2]trim=start=$C,setpts=PTS-STARTPTS[p3];\
[1:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p2];[p1][p2][p3]concat=n=3:v=1:a=0[v]" -map "[v]" -map 2:a -c:v libx264 -crf 18 -c:a aac -b:a 192k -shortest -movflags +faststart "$O"
