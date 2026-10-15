#!/bin/bash
# assemble_rush2.sh OUT.mp4 — hook magazin (Kling) + B-roll aprobat reel26 (halatul real HeatGrump) + conector gri + telecomandă albă + cozy
S=/tmp/claude-0/-home-user/d10e41e8-67eb-5ee5-9e56-7eba5b90f258/scratchpad
R=${R:-/home/user/heatgrump/output/reel26}
ffmpeg -v error -y -i $S/g5/hook_kling.mp4 -i $R/b1.mp4 -i $R/${B2:-b2fast}.mp4 -i $S/g5/conn_seg.mp4 -i $S/g5/ctl_seg.mp4 -i $R/cozy.mp4 -i $S/rh/src/Ddzo8i9ymGW.mp4 -filter_complex "\
[0:v]fps=30,scale=720:1280,setsar=1,trim=0.4:3.4,setpts=PTS-STARTPTS[h];\
[1:v]fps=30,scale=720:1280,setsar=1,trim=0:1.2,setpts=PTS-STARTPTS[p1];\
[2:v]fps=30,scale=720:1280,setsar=1,trim=0:3.0,setpts=PTS-STARTPTS[p2];\
[3:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p3];[4:v]fps=30,setsar=1,setpts=PTS-STARTPTS[p4];\
[5:v]fps=30,scale=720:1280,setsar=1,trim=0:1.4,setpts=PTS-STARTPTS[p5];\
[h][p1][p2][p3][p4][p5]concat=n=6:v=1:a=0[v];\
[0:a]atrim=0.4:3.4,asetpts=PTS-STARTPTS,volume=0.8,afade=t=out:st=2.6:d=0.4[ka];\
[6:a]asetpts=PTS-STARTPTS[oa];[oa][ka]amix=inputs=2:duration=first:normalize=0[a]" \
-map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k -shortest -movflags +faststart "$1"
