#!/bin/bash
# mkproof.sh robe take.mp4 out.mp4 cS cE rS rE song drop  — edit: fabric conn/remote swapped in, music only, 720p
set -e
R=/home/user/limitless/creator-kit; robe=$1; t=$2; o=$3; cS=$4; cE=$5; rS=$6; rE=$7; song=$8; ms=$9
D=/home/user/limitless/products/broll-new/demo
if [ "$robe" = princess ]; then
  ffmpeg -v error -y -ss 0.15 -t 1.1 -i $R/products/princess/fixed/remote-fabric-1.mp4 -vf "fps=30,tpad=stop_mode=clone:stop_duration=3" -t $(python3 -c "print($rE-$rS)") -an -c:v libx264 -crf 20 -pix_fmt yuv420p /tmp/prf-rem.mp4
else
  ffmpeg -v error -y -ss 0.25 -i $R/products/snoopy/fixed/remote-fabric-1.mp4 -vf "fps=30,tpad=stop_mode=clone:stop_duration=1" -t $(python3 -c "print($rE-$rS)") -an -c:v libx264 -crf 20 -pix_fmt yuv420p /tmp/prf-rem.mp4
fi
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$t")
$D/swap-seg.sh "$t" /tmp/prf-v.mp4 $cS $cE $R/products/$robe/fixed/connector-fabric-1.mp4 0.3 $rS $rE /tmp/prf-rem.mp4 0
e=$(python3 -c "print(float('$dur')-0.1)")
ffmpeg -v error -y -t $e -i /tmp/prf-v.mp4 -ss $ms -i $R/music/xmas/$song -filter_complex "[0:v]scale=720:1280[v];[1:a]volume=0.75,atrim=0:$e,afade=t=out:st=$(python3 -c "print($e-0.6)"):d=0.6[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -b:a 110k -shortest "$o"
rm -f /tmp/prf-rem.mp4 /tmp/prf-v.mp4
