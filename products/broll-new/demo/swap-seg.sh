#!/bin/bash
# swap-seg.sh in.mp4 out.mp4 cS cE connClip connOff rS rE remClip remOff
# Replaces video [cS,cE) with connClip (from connOff, same length) and [rS,rE) with remClip (from remOff); audio untouched.
in=$1; out=$2; cS=$3; cE=$4; cc=$5; co=$6; rS=$7; rE=$8; rc=$9; ro=${10}
cd1=$(python3 -c "print($cE-$cS)"); rd=$(python3 -c "print($rE-$rS)")
ffmpeg -v error -y -i "$in" -i "$cc" -i "$rc" -filter_complex "
[0:v]trim=0:$cS,setpts=PTS-STARTPTS,fps=30,scale=1080:1920,setsar=1[a];
[1:v]trim=$co:$(python3 -c "print($co+$cd1)"),setpts=PTS-STARTPTS,fps=30,scale=1080:1920,setsar=1[b];
[0:v]trim=$cE:$rS,setpts=PTS-STARTPTS,fps=30,scale=1080:1920,setsar=1[c];
[2:v]trim=$ro:$(python3 -c "print($ro+$rd)"),setpts=PTS-STARTPTS,fps=30,scale=1080:1920,setsar=1[d];
[0:v]trim=$rE,setpts=PTS-STARTPTS,fps=30,scale=1080:1920,setsar=1[e];
[a][b][c][d][e]concat=n=5:v=1:a=0[v]" -map "[v]" -map 0:a? -c:v libx264 -crf 21 -pix_fmt yuv420p -c:a copy "$out"
