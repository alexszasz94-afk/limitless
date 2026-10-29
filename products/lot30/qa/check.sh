#!/bin/bash
# check.sh N -> qa/chk N.jpg : full sheet + floor zoom at pocket shot
cd /home/user/limitless/products/lot30
C=$(python3 ../../creator-kit/engine/tools.py cuts broll/b$1.mp4 | tail -1)
echo "b$1 $C"
c1=$(python3 -c "print($C[0])")
ffmpeg -v error -y -t 5.2 -i broll/b$1.mp4 -vf "fps=2.5,scale=110:-1,tile=13x1" -frames:v 1 qa/s$1.jpg
for k in 1.3 1.7 2.1 2.5; do ffmpeg -v error -y -ss $(python3 -c "print($c1+$k)") -i broll/b$1.mp4 -frames:v 1 -vf "crop=iw:ih*0.4:0:ih*0.6,scale=330:-1" qa/z$1_$k.jpg; done
ffmpeg -v error -y -i qa/z$1_1.3.jpg -i qa/z$1_1.7.jpg -i qa/z$1_2.1.jpg -i qa/z$1_2.5.jpg -filter_complex hstack=4 qa/zz$1.jpg
ffmpeg -v error -y -i qa/s$1.jpg -i qa/zz$1.jpg -filter_complex "[1]scale=1430:-1[b];[0][b]vstack" qa/chk$1.jpg
