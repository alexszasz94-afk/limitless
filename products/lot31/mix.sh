#!/bin/bash
# mix.sh NAME CUT DROP MODE  (MODE quiet = 0.2 under hook then 1.1 from CUT; MODE full = song from 0 at 1.0, drop on CUT)
cd /home/user/limitless/products/lot31/final
S=/home/user/heatgrump/library/music/xmas/mean-one-grinch.mp3
ST=$(python3 -c "print(max(0,$3-$2))")
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 nomusic-$1.mp4)
FO=$(python3 -c "print(round($D-0.8,2))")
if [ "$4" = "full" ]; then V="1.0"; else V="if(lt(t,$2),0.2,if(lt(t,$2+0.12),0.2+0.9*(t-$2)/0.12,1.1))"; fi
ffmpeg -v error -y -i nomusic-$1.mp4 -ss $ST -i $S -filter_complex "[1:a]atrim=0:$D,asetpts=N/SR/TB,volume='$V':eval=frame,afade=t=out:st=$FO:d=0.8[m];[0:a][m]amix=2:duration=first:normalize=0,alimiter=limit=0.95[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k grinch-$1-FINAL.mp4
echo grinch-$1-FINAL.mp4 $D
