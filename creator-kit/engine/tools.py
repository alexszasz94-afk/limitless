"""Helper commands Claude uses while making a video. Run from the kit folder:

  python3 engine/tools.py download <instagram-or-tiktok-url> <folder>   -> <folder>/reference.mp4 (+ prints length and cuts)
  python3 engine/tools.py sheet <video> <out.jpg> [fps]                 -> contact sheet of frames (default 2 fps) to look at
  python3 engine/tools.py frame <video> <seconds> <out.jpg>             -> one full-size frame
  python3 engine/tools.py cuts <video>                                   -> times where the shot changes
  python3 engine/tools.py safe-end <video>                               -> last safe second before Kling appends a reference image / fades out
  python3 engine/tools.py fetch <url> <out-file>                          -> download a Higgsfield result (png results are saved as jpg)
  python3 engine/tools.py cozy <broll.mp4> <out.mp4> [start]             -> zoomed last cozy shot (default start 4.95 s, 2.1 s long)
  python3 engine/tools.py drop <song.mp3>                                 -> loud jumps in a song (where the beat/chorus drops)
  python3 engine/tools.py fanwipe <in.mp4> <out.mp4> <t1> [<t2> ...]       -> ceiling-fan blade wipe centred on each cut time
  python3 engine/tools.py next-set                                        -> next unused character + room from library/ (and marks them used)
  python3 engine/tools.py reject <library/characters/x.jpg>               -> photo breaks the rules: moves it to library/rejected/ (then run next-set again)
  python3 engine/tools.py transcribe <video>                            -> what people SAY in the video, with seconds (first run downloads a small speech model, ~150 MB)
  python3 engine/tools.py voice-mix <clip.mp4> <voice.wav> <out.mp4> <delay_s> [orig_vol]   -> puts a voice line over a clip (clip sound lowered)
  python3 engine/tools.py crop <in.jpg> <out.jpg> <left> <top> <right> <bottom>   -> crop (fractions 0-1), e.g. character head+shoulders for the B-roll
  python3 engine/tools.py compare <original.mp4> <ours.mp4> <from_s> <to_s> <out.jpg>   -> original (top) vs ours (bottom), 10 frames/s, to check the motion is identical
  python3 engine/tools.py log <video-name> key=value ...                 -> remembers what this video used (hook, outfit, music, text, motion, robe)
  python3 engine/tools.py history [n]                                     -> what the last n videos used (default 5), so the next one is different
"""
import json, math, os, subprocess, sys, tempfile, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def duration(f):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).stdout.strip() or 0)


def cuts(f, thr=0.2):
    out = run(["ffmpeg", "-i", f, "-vf", f"select='gt(scene,{thr})',showinfo", "-f", "null", "-"]).stderr
    return [round(float(x.split(":")[1]), 2) for x in out.split() if x.startswith("pts_time:") and float(x.split(":")[1]) > 0.1]


def download(url, folder):
    os.makedirs(folder, exist_ok=True)
    out = os.path.join(folder, "reference.mp4")
    for _ in range(3):
        run(["yt-dlp", "-q", "-f", "mp4/best", "-o", out, url])
        if os.path.exists(out):
            break
    if not os.path.exists(out):
        sys.exit("Download failed. Ask the user to save the video and put it in inbox/.")
    print(out, "length", round(duration(out), 2), "cuts", cuts(out, 0.25))


def sheet(f, out, fps="2"):
    d = duration(f); n = max(1, int(d * float(fps)))
    cols = min(n, 8); rows = math.ceil(n / cols)
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", f"fps={fps},scale=200:-1,tile={cols}x{rows}", "-frames:v", "1", out])
    print(out, f"({n} frames, {fps} per second, left to right, top to bottom)")


def frame(f, t, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", f, "-frames:v", "1", "-q:v", "2", out]); print(out)


def safe_end(f):
    """Kling image-to-video often ends with a jump to one of the reference images or a fade.
    Returns the last second before the first cut in the second half or before brightness collapses."""
    d = duration(f)
    late = [c for c in cuts(f, 0.12) if c > d * 0.4]   # sensitive: also catches zoom jumps
    out = run(["ffmpeg", "-i", f, "-vf", "signalstats,metadata=print:key=lavfi.signalstats.YAVG", "-f", "null", "-"]).stderr
    ys = [float(x.split("=")[1]) for x in out.split() if x.startswith("lavfi.signalstats.YAVG=")]
    fps = len(ys) / d if d else 24
    fade = None
    for i in range(int(len(ys) * 0.4), len(ys)):
        if ys[i] < ys[0] * 0.8:
            fade = i / fps; break
    ends = [x for x in late + ([fade] if fade else [])]
    end = round(min(ends) - 0.1, 2) if ends else round(d, 2)
    print("length", round(d, 2), "late cuts", late, "fade", round(fade, 2) if fade else None, "-> use end", end)
    return end


def fetch(url, out):
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    if url.lower().split("?")[0].endswith(".png") and out.lower().endswith(".jpg"):
        tmp = out + ".png"
        run(["curl", "-s", "-o", tmp, url]); run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-q:v", "2", out]); os.remove(tmp)
    else:
        run(["curl", "-s", "-o", out, url])
    print(out, os.path.getsize(out) if os.path.exists(out) else "FAILED")


def cozy(f, out, start="4.95"):
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-i", f, "-t", "2.1", "-vf",
         "crop=iw/1.3:ih/1.3:iw*0.5-iw/2.6:max(0\\,ih*0.42-ih/2.6),scale=1080:1920", "-an",
         "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", out]); print(out)


def drop(f):
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "8000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.int16).astype(float); w = 4000
    r = np.array([np.sqrt(np.mean(a[i:i + w] ** 2)) for i in range(0, len(a) - w, w)])
    hits = [(round(i * 0.5, 1), int(r[i])) for i in range(3, len(r)) if r[i] > 1.6 * np.mean(r[max(0, i - 6):i]) and r[i] > np.percentile(r, 60)]
    print("loud jumps (second, loudness):", hits[:15])


def fanwipe(f, out, times):
    from PIL import Image, ImageDraw, ImageFilter
    W, H = 1080, 1920; tmp = tempfile.mkdtemp(); hub = (-120, -160); L, w, n = 2600, 520, 12
    for i in range(n):
        a = math.radians(100 - i * (105 / (n - 1)))
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        dx, dy = math.cos(a), math.sin(a); px, py = -dy, dx
        p0 = (hub[0] + px * w * .25, hub[1] + py * w * .25); p1 = (hub[0] - px * w * .25, hub[1] - py * w * .25)
        q1 = (hub[0] + dx * L - px * w / 2, hub[1] + dy * L - py * w / 2); q0 = (hub[0] + dx * L + px * w / 2, hub[1] + dy * L + py * w / 2)
        d.polygon([p0, q0, q1, p1], fill=(92, 88, 84, 255))
        im.filter(ImageFilter.GaussianBlur(28)).save(f"{tmp}/b{i:02d}.png")
    inputs, chain, filt = ["-i", f], "[0:v]", []
    for k, t in enumerate(times):
        inputs += ["-framerate", "30", "-i", f"{tmp}/b%02d.png"]
        filt.append(f"[{k+1}]setpts=PTS+{float(t)-0.2}/TB[b{k}]")
        filt.append(f"{chain}[b{k}]overlay=eof_action=pass[x{k}]"); chain = f"[x{k}]"
    filt[-1] = filt[-1].replace(f"[x{len(times)-1}]", ",format=yuv420p[v]")
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-crf", "18", "-c:a", "copy", out])
    print(out)


def next_set():
    used_f = os.path.join(ROOT, "state/used.json")
    used = json.load(open(used_f)) if os.path.exists(used_f) else {"characters": [], "rooms": []}
    pick = {}
    for kind in ("characters", "rooms"):
        free = [p for p in sorted(glob.glob(os.path.join(ROOT, "library", kind, "*.jpg"))) if os.path.basename(p) not in used[kind]]
        if not free:
            print(f"NO_{kind.upper()}_LEFT: run the skill find-sets now (Pinterest search, you pick the good ones), then run next-set again. Ask the creator for photos ONLY if Pinterest fails.")
            return
        pick[kind] = free[0]; used[kind].append(os.path.basename(free[0]))
    json.dump(used, open(used_f, "w"), indent=1)
    print("character:", os.path.relpath(pick["characters"], ROOT)); print("room:", os.path.relpath(pick["rooms"], ROOT))


def transcribe(f):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("Missing: run  pip install faster-whisper  (Mac/Linux: python3 -m pip install --user faster-whisper; Windows: py -m pip install faster-whisper)"); return
    try:
        m = WhisperModel("base.en", device="cpu", compute_type="int8")
    except Exception as e:
        print("TRANSCRIBE_BLOCKED: cannot download the speech model (needs huggingface.co). In the cloud add *.huggingface.co, huggingface.co, *.hf.co to Allowed domains. Error:", e); return
    segs, _ = m.transcribe(f, word_timestamps=False)
    out = [f"{s.start:5.1f}-{s.end:5.1f}  {s.text.strip()}" for s in segs]
    print("\n".join(out) if out else "(no speech - music/sounds only)")


def voice_mix(clip, voice, out, delay, orig_vol="0.3"):
    ms = int(float(delay) * 1000)
    has_a = run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", clip]).stdout.strip()
    if has_a:
        fc = f"[0:a]volume={orig_vol}[o];[1:a]adelay={ms}|{ms},volume=1.6[v];[o][v]amix=inputs=2:duration=first:normalize=0[a]"
    else:
        fc = f"[1:a]adelay={ms}|{ms},volume=1.6,apad[a]"
    run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-i", voice, "-filter_complex", fc, "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-ar", "48000", "-shortest", out]); print(out)


def reject(f):
    d = os.path.join(ROOT, "library/rejected"); os.makedirs(d, exist_ok=True)
    os.replace(f, os.path.join(d, os.path.basename(os.path.dirname(f)) + "-" + os.path.basename(f))); print("moved to library/rejected/")


def crop(f, out, l, t, r, b):
    from PIL import Image
    im = Image.open(f).convert("RGB"); w, h = im.size
    im.crop((int(float(l) * w), int(float(t) * h), int(float(r) * w), int(float(b) * h))).save(out, quality=95); print(out)


def compare(ref, ours, t0, t1, out):
    tmp = tempfile.mkdtemp(); n = max(1, round((float(t1) - float(t0)) * 10)); strips = []
    for i, f in enumerate((ref, ours)):
        s = os.path.join(tmp, f"{i}.jpg"); strips.append(s)
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(t0), "-t", str(float(t1) - float(t0)), "-i", f, "-vf", f"fps=10,scale=110:-1,tile={n}x1", "-frames:v", "1", s])
    run(["ffmpeg", "-v", "error", "-y", "-i", strips[0], "-i", strips[1], "-filter_complex", "[0][1]scale2ref=iw:ih[a][b];[a][b]vstack", out])
    print(out, "- top = original, bottom = ours, one frame every 0.1 s from", t0, "s. Same action must be in the same column.")


def log(name, pairs):
    f = os.path.join(ROOT, "state/used.json")
    used = json.load(open(f)) if os.path.exists(f) else {"characters": [], "rooms": []}
    rec = {"video": name}
    for p in pairs:
        k, _, v = p.partition("="); rec[k] = v
    used.setdefault("videos", []).append(rec); json.dump(used, open(f, "w"), indent=1); print("logged", rec)


def history(n="5"):
    f = os.path.join(ROOT, "state/used.json")
    vids = (json.load(open(f)) if os.path.exists(f) else {}).get("videos", [])
    if not vids:
        print("no videos yet - anything goes"); return
    for r in vids[-int(n):]:
        print(" | ".join(f"{k}: {v}" for k, v in r.items()))
    print("The next video must NOT repeat the hook concept, outfit, music cue or on-screen text of the last 3 above.")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit()
    c = a[0]
    if c == "download": download(a[1], a[2])
    elif c == "sheet": sheet(a[1], a[2], a[3] if len(a) > 3 else "2")
    elif c == "frame": frame(a[1], a[2], a[3])
    elif c == "cuts": print(cuts(a[1]))
    elif c == "safe-end": safe_end(a[1])
    elif c == "fetch": fetch(a[1], a[2])
    elif c == "cozy": cozy(a[1], a[2], a[3] if len(a) > 3 else "4.95")
    elif c == "drop": drop(a[1])
    elif c == "fanwipe": fanwipe(a[1], a[2], a[3:])
    elif c == "next-set": next_set()
    elif c == "reject": reject(a[1])
    elif c == "transcribe": transcribe(a[1])
    elif c == "voice-mix": voice_mix(*a[1:6])
    elif c == "crop": crop(*a[1:7])
    elif c == "compare": compare(*a[1:6])
    elif c == "log": log(a[1], a[2:])
    elif c == "history": history(a[1] if len(a) > 1 else "5")
    else: print(__doc__)
