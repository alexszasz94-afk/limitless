#!/bin/bash
# assemble_store.sh HOOK.mp4 OUT.mp4 : hook 0-4 + broll Sofia 4.0-8.3 + conector 1.7 + telecomanda 2.0 + cozy 8.5-10.7, sunet original DdU_WB_zSb5
S=/tmp/claude-0/-home-user/d10e41e8-67eb-5ee5-9e56-7eba5b90f258/scratchpad
B=/home/user/limitless/output/princess-test/sofia/broll-sofia-720p.mp4
ffmpeg -v error -y -i "$1" -i $B -i $S/g3/conn_store.mp4 -i $S/g3/ctl_store.mp4 -i $S/rh/src/DdU_WB_zSb5.mp4 -filter_complex "\
[0:v]fps=30,scale=720:1280,setsar=1,trim=0:4.0,setpts=PTS-STARTPTS[h];\
[1:v]fps=30,scale=720:1280,setsar=1,split[b1][b2];[b1]trim=4.0:8.3,setpts=PTS-STARTPTS[p1];[b2]trim=8.5:10.7,setpts=PTS-STARTPTS[p4];\
[2:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p2];[3:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p3];\
[h][p1][p2][p3][p4]concat=n=5:v=1:a=0[v]" -map "[v]" -map 4:a -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k -shortest -movflags +faststart "$2"
