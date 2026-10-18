"""Princess batch 1: full edits = hook (voice) -> B-roll B1+B2 -> connector -> controller -> B-roll cozy; text + Bublé after the hook."""
import json, os, subprocess, sys
P = "/home/user/limitless/output/princess-test"
HG = "/home/user/heatgrump"
BR = {"b1": f"{P}/broll-17oct/b1-1080p.mp4", "b2": f"{P}/broll-17oct/b2-1080p.mp4", "b3": f"{P}/broll-17oct/b3v2-1080p.mp4"}
CUT = 5.6   # B2 ends / cozy starts in the reel24 template
HOOKS = [
 ("b1", "h1", f"{P}/hook-store/hook-store-1080p.mp4", "When the princess robe is finally in stores… 😱👑"),
 ("b1", "h3", f"{P}/hooks-batch1/b1-h3-1080p.mp4", "They finally restocked it… 😱👑"),
 ("b1", "h4", f"{P}/hooks-batch1/b1-h4-1080p.mp4", "Me vs. the thermostat every winter 🥶👑"),
 ("b2", "h3", f"{P}/hooks-batch1/b2-h3-1080p.mp4", "The princess robe just dropped… 😱👑"),
 ("b2", "h4", f"{P}/hooks-batch1/b2-h4-1080p.mp4", "Princess moms when it's back in stock 🏃‍♀️👑"),
 ("b3", "h3", f"{P}/hooks-batch1/b3-h3-1080p.mp4", "Plain blanket vs. princess robe 👑✨"),
 ("b3", "h4", f"{P}/hooks-batch1/b3-h4-1080p.mp4", "The perfect gift doesn't exist… 🎁👑"),
]
only = sys.argv[1:]
for b, h, hook, text in HOOKS:
    name = f"princess-{b}-{h}"
    if only and name not in only: continue
    hd = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",hook],capture_output=True,text=True).stdout)
    hd = min(hd, 4.0)
    segs = [{"file": hook, "start": 0, "end": hd, "audio": True},
            {"file": BR[b], "start": 0, "end": CUT},
            {"file": f"{P}/connector-seedance25-720p.mp4", "start": 1.0, "end": 2.6},
            {"file": f"{P}/controller-arata-final.mp4", "start": 0, "end": 3.1},
            {"file": BR[b], "start": CUT, "end": 8.0}]
    total = hd + CUT + 1.6 + 3.1 + (8.0 - CUT)
    spec = {"out": f"{os.getcwd()}/{name}-nomusic.mp4", "segments": segs, "texts": [{"t0": 0, "t1": round(total, 2), "text": text}]}
    json.dump(spec, open(f"{os.getcwd()}/{name}.json", "w"), ensure_ascii=False, indent=1)
    subprocess.run(["python3", f"{HG}/engine/final.py", f"{os.getcwd()}/{name}.json"], check=True, cwd=HG)
    nm = spec["out"]; D = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",nm],capture_output=True,text=True).stdout)
    ms = int(hd * 1000)
    subprocess.run(["ffmpeg","-loglevel","error","-y","-i",nm,"-ss","32.43","-i",f"{HG}/library/music/xmas/buble-beginning.mp3","-filter_complex",
        f"[1:a]atrim=0:{D},asetpts=PTS-STARTPTS,volume=0.85,afade=t=in:st=0:d=0.4,adelay={ms}|{ms},afade=t=out:st={D-0.6}:d=0.6[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]",
        "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k",f"{name}-FINAL.mp4"], check=True)
    os.remove(nm); print(name, round(D, 2))
