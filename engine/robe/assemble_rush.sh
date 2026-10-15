#!/bin/bash
# assemble_rush.sh HOOK_KLING.mp4 BROLL_GENJUTSU.mp4 OUT.mp4
# hook 0.4-3.4 | broll 3.0-4.0 (se desface) | broll 4.0-7.2 (îmbracă+deschide) | conector gri 1.5 s | telecomandă albă 2.37 s | cozy 8.6-10.16
# sunet: originalul Ddzo8i9ymGW + sunetul Kling sub hook
S=/tmp/claude-0/-home-user/d10e41e8-67eb-5ee5-9e56-7eba5b90f258/scratchpad
ffmpeg -v error -y -i "$1" -i "$2" -i $S/g5/conn_seg.mp4 -i $S/g5/ctl_seg.mp4 -i $S/rh/src/Ddzo8i9ymGW.mp4 -filter_complex "\
[0:v]fps=30,scale=720:1280,setsar=1,trim=0.4:3.4,setpts=PTS-STARTPTS[h];\
[1:v]fps=30,scale=720:1280,setsar=1,split=3[b1][b2][b3];\
[b1]trim=3.0:4.0,setpts=PTS-STARTPTS[p1];[b2]trim=4.0:7.2,setpts=PTS-STARTPTS[p2];[b3]trim=8.6:10.16,setpts=PTS-STARTPTS[p5];\
[2:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p3];[3:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p4];\
[h][p1][p2][p3][p4][p5]concat=n=6:v=1:a=0[v];\
[0:a]atrim=0.4:3.4,asetpts=PTS-STARTPTS,volume=0.8,afade=t=out:st=2.6:d=0.4[ka];\
[4:a]asetpts=PTS-STARTPTS[oa];[oa][ka]amix=inputs=2:duration=first:normalize=0[a]" \
-map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k -shortest -movflags +faststart "$3"
