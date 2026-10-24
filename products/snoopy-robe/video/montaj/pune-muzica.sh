#!/bin/bash
# Pune muzica Snoopy pe montajul HeatPup, cu „drop-ul” piesei fix la tăietura spre unboxing (4,04 s).
# Folosire: bash pune-muzica.sh <piesa.mp3|m4a> <secunda drop-ului în piesă>
set -e
cd "$(dirname "$0")"
SONG="$1"; DROP="$2"; CUT=4.04
START=$(python3 -c "print(max(0,$DROP-$CUT))")
ffmpeg -v error -y -i heatpup-montaj-fara-muzica.mp4 -ss "$START" -i "$SONG" -filter_complex \
 "[1:a]atrim=0:16.1,asetpts=PTS-STARTPTS,volume='if(lt(t,$CUT),0.25,1.0)':eval=frame,afade=t=out:st=15.3:d=0.8[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k heatpup-montaj.mp4
echo "gata: heatpup-montaj.mp4"
