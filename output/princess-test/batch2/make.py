"""Princess batch 2 (American, B-roll copied from princesscomfortt DeAepvaSfSf): full edits = hook (voice) -> B-roll B1+B2 -> connector -> controller -> B-roll cozy; text + Bublé after the hook."""
import json, os, subprocess, sys
P = "/home/user/limitless/output/princess-test"
HG = "/home/user/heatgrump"
BR = {"b4": f"{P}/batch2/b4-1080p.mp4", "b5": f"{P}/batch2/b5-1080p.mp4"}
CUT = 5.25   # open-robe shot ends here (scene change at 5.33 s)
COZY = 5.4   # cozy starts after the scene change, no flash of the standing shot
# (broll, hook, file, hook end = first scene only, on-screen text copied EXACTLY from the competitor's viral (Szasz 18 oct: no changes); a pair = hook text, then text from the product on)
MUSIC, DROP = f"{HG}/library/music/xmas/buble-beginning.mp3", 35.38   # the song's drop (energy jump), measured
DRESSED = 0.05  # the song starts on its drop the moment the hook ends (Szasz 18 oct: "sa inceapa cantatul cand dispare hookul"); 0.05 s pre-roll keeps the attack
HOOKS = [
 ("b4", "h1", f"{P}/batch2/b4-h1-1080p.mp4", 4.0, "I made this for the cold-aholics.. 🤩💕"),   # princesscomfortt DeDAprJSrPO (3-2-1 rolled robe drop)
 ("b5", "h1", f"{P}/batch2/b5-h1-1080p.mp4", 4.0, "I made this for the cold-aholics.. 🤩💕"),
]
only = sys.argv[1:]
for b, h, hook, hend, text in HOOKS:
    name = f"princess-{b}-{h}"
    if only and name not in only: continue
    hd = hend
    segs = [{"file": hook, "start": 0, "end": hd, "audio": True},
            {"file": BR[b], "start": 0, "end": CUT},
            {"file": f"{P}/connector-seedance25-720p.mp4", "start": 1.0, "end": 2.6},
            {"file": f"{P}/controller-arata-final.mp4", "start": 0, "end": 3.1},
            {"file": BR[b], "start": COZY, "end": 8.0}]
    total = hd + CUT + 1.6 + 3.1 + (8.0 - COZY)
    spec = {"out": f"{os.getcwd()}/{name}-nomusic.mp4", "segments": segs, "texts": [{"t0": 0, "t1": round(total, 2), "text": text}] if isinstance(text, str) else
            [{"t0": 0, "t1": hd, "text": text[0]}, {"t0": hd, "t1": round(total, 2) if len(text) < 3 else hd + CUT, "text": text[1]}] +
            ([{"t0": hd + CUT, "t1": round(total, 2), "text": text[2]}] if len(text) > 2 else [])}
    json.dump(spec, open(f"{os.getcwd()}/{name}.json", "w"), ensure_ascii=False, indent=1)
    subprocess.run(["python3", f"{HG}/engine/final.py", f"{os.getcwd()}/{name}.json"], check=True, cwd=HG)
    nm = spec["out"]; D = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",nm],capture_output=True,text=True).stdout)
    ms = int(hd * 1000)
    subprocess.run(["ffmpeg","-loglevel","error","-y","-i",nm,"-ss",str(DROP - DRESSED),"-i",MUSIC,"-filter_complex",
        f"[1:a]atrim=0:{D},asetpts=PTS-STARTPTS,volume=0.85,afade=t=in:st=0:d=0.05,adelay={ms}|{ms},afade=t=out:st={D-0.6}:d=0.6[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]",
        "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k",f"{name}-FINAL.mp4"], check=True)
    os.remove(nm); print(name, round(D, 2))
