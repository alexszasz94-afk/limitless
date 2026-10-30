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
  python3 engine/tools.py next-set <robe>                                 -> next unused character + room from library/ (and marks them used) + which B-roll variant (rotation: classic, motion2 (Princess), variants 3-5)
  python3 engine/tools.py add-rooms <rooms.zip>                           -> Alex's rooms zip (the ONLY source of rooms, rule 28 Oct) -> library/rooms/room-NN.jpg (next free numbers)
  python3 engine/tools.py photo-ok <photo>                               -> True/False + reason: short side >= 1080 (4K preferred) and sharp (rule 29 Oct)
  python3 engine/tools.py reject <library/characters/x.jpg>               -> photo breaks the rules: moves it to library/rejected/ (then run next-set again)
  python3 engine/tools.py transcribe <video>                            -> what people SAY in the video, with seconds (first run downloads a small speech model, ~150 MB)
  python3 engine/tools.py voice-mix <clip.mp4> <voice.wav> <out.mp4> <delay_s> [orig_vol]   -> puts a voice line over a clip (clip sound lowered)
  python3 engine/tools.py crop <in.jpg> <out.jpg> <left> <top> <right> <bottom>   -> crop (fractions 0-1), e.g. character head+shoulders for the B-roll
  python3 engine/tools.py compare <original.mp4> <ours.mp4> <from_s> <to_s> <out.jpg>   -> original (top) vs ours (bottom), 10 frames/s, to check the motion is identical
  python3 engine/tools.py log <video-name> key=value ...                 -> remembers what this video used (hook, outfit, music, text, motion, robe)
  python3 engine/tools.py speech-times <video> [seconds]                  -> when the voice bursts are (start-end), to put each spoken word on its exact second
  python3 engine/tools.py cleantext <video> <clean.jpg> <out.mp4> <l> <t> <r> <b> [...more boxes]  -> covers their on-screen text with the same spot from a clean photo (static camera only) - no blur for Kling to copy
  python3 engine/tools.py broll-check <broll.mp4> <motion.mp4> <out-folder>   -> B-roll safety check: shot count vs the motion clip, glitch spikes inside shots, safe segments, one sheet per shot to look at
  python3 engine/tools.py retime <our-hook.mp4> <reference-hook.mp4> <out.mp4> [hook end s] -> puts every cut/action on the EXACT second of the original and ends exactly where it ends (rule 28 Oct)
  python3 engine/tools.py vocals <hook.mp4> <out.mp4>                    -> keeps ONLY the voice of a copied hook (Demucs) - Kling copies the original music, never deliver it (rule 28 Oct)
  python3 engine/tools.py audit-sound <hook.mp4> <hook end> "<expected line>" -> ALWAYS after making a hook/video: every word + second, missing words, music check
  python3 engine/tools.py blur-for-sound <hook.mp4> <out.mp4> <x,y,w,h|none> [face until s] -> input for the Seedance SOUND pass (product blurred, lips sharp)
  python3 engine/tools.py voice-to-lips <seedance.mp4> <out.wav> <hook end> <its word onsets> <original word onsets> [last phrase speed, e.g. 0.85] [background gain, default 0.5; lower if the background covers the voice] -> voice on the lips, no cut word, background untouched
  python3 engine/tools.py onsets <file> [0.2]                            -> seconds where each word starts; on `vocals` of the REFERENCE = where our voice must go. No onsets in the vocals = the original has only a song (no voice)
  python3 engine/tools.py place-voice <seedance.mp4> <out.wav> <hook end> <t1,t2,..> <s1,s2,..> [cap] -> puts Seedance words (onsets s) on the reference seconds (t)
  python3 engine/tools.py hook-audio <reference.mp4> [seconds]            -> MANDATORY on every reference: is there speech? every word WITH its second + a ready "Sound:" line for the Kling prompt
  python3 engine/tools.py compare-audio <reference.mp4> <our-hook.mp4> [seconds]   -> words + seconds of both, to prove our hook says the same thing at the same time
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


BROLL_VARIANTS = {   # rule 30 Oct (Alex): the B-roll rotates between these motions, never the same twice in a row
    "motion":  ("motion/broll-motion.mp4",   7, "classic B-roll (PRODUCT.md 'B-roll' prompt); connector + remote = the fixed tree clips"),
    "motion2": ("motion/broll-motion-2.mp4", 6, "Princess only: motion2 paragraph in PRODUCT.md (hem sentence); connector + remote = the fixed tree clips"),
    "motion3": ("motion/broll-motion-3.mp4", 12, "PRODUCT.md 'B-roll variant 3' (from DdZxYkctpt1) - its OWN connector + remote are inside the B-roll"),
    "motion4": ("motion/broll-motion-4.mp4", 12, "PRODUCT.md 'B-roll variant 4' (from Dc3sRnKtTw0) - its OWN connector + remote are inside the B-roll"),
    "motion5": ("motion/broll-motion-5.mp4", 11, "PRODUCT.md 'B-roll variant 5' (from Dco0N-Ctps-) - its OWN connector + remote are inside the B-roll"),
}


XMAS_SONGS = {   # rule 30 Oct (Alex): rotating Christmas songs, shared pool for both robes - file in music/xmas/, drop second (the full-band/chorus entry, LISTEN-checked)
    "mariah-all-i-want.mp3": 53.4,
    "buble-beginning.mp3": 35.35,
    "wham-last-christmas.mp3": 0.0,   # steady from the start, no clear drop
    "let-it-go.mp3": 58.5,            # chorus; Alex: fits the Princess robe best
}


def next_song(robe):
    """rule 30 Oct (Alex): next-set also rotates the Christmas song - never the same as the last 2 videos (any robe)."""
    f = os.path.join(ROOT, "state/used.json")
    vids = (json.load(open(f)) if os.path.exists(f) else {}).get("videos", [])
    recent = [v.get("song", "") for v in vids[-2:]]
    keys = list(XMAS_SONGS)
    for k in keys:
        if k not in recent:
            return k
    return keys[0]


def broll_variants(robe):
    return [k for k in BROLL_VARIANTS if k != "motion2" or robe.lower() == "princess"]


def next_motion(robe):
    """rule 30 Oct (Alex): the B-roll rotates over all variants of the robe (Snoopy: motion, motion3-5; Princess: also motion2) - never the same twice in a row."""
    keys = broll_variants(robe)
    f = os.path.join(ROOT, "state/used.json")
    vids = [v for v in (json.load(open(f)) if os.path.exists(f) else {}).get("videos", []) if v.get("robe", "").lower() == robe.lower()]
    last = vids[-1].get("motion", "") if vids else ""
    return keys[(keys.index(last) + 1) % len(keys)] if last in keys else keys[0]


def next_fixed(robe, kind):
    """rule 30 Oct (Alex): connector and remote are reused - the NEW fabric close-ups (fixed/<kind>-fabric-N.mp4, v4 style, on the robe fabric) are the DEFAULT/first in rotation; the old tree close-ups (fixed/<kind>-tree-N.mp4, 4K) stay as alternates."""
    f = os.path.join(ROOT, "state/used.json")
    vids = [v for v in (json.load(open(f)) if os.path.exists(f) else {}).get("videos", []) if v.get("robe", "").lower() == robe.lower()]
    names = [os.path.basename(h) for h in sorted(glob.glob(os.path.join(ROOT, "products", robe.lower(), "fixed", f"{kind}-fabric-*.mp4"))) + sorted(glob.glob(os.path.join(ROOT, "products", robe.lower(), "fixed", f"{kind}-tree-*.mp4")))]
    if not names:
        return None
    last = vids[-1].get(kind, "") if vids else ""
    return names[(names.index(last) + 1) % len(names)] if last in names else names[0]


def next_remote(robe):
    return next_fixed(robe, "remote")


def photo_ok(f, min_side=1080, min_sharp=150):
    """rule 29 Oct (Alex): rooms/characters ALWAYS high quality - short side >= 1080 (4K preferred), sharp. Returns (ok, reason)."""
    from PIL import Image, ImageFilter, ImageStat
    try: im = Image.open(f).convert("L")
    except Exception: return False, "broken file"
    w, h = im.size
    if min(w, h) < min_side: return False, f"low resolution {w}x{h} (needs short side >= {min_side}, 4K preferred)"
    im = im.resize((1080, max(2, round(1080 * h / w))))
    var = ImageStat.Stat(im.filter(ImageFilter.Kernel((3, 3), (0, -1, 0, -1, 4, -1, 0, -1, 0), 1, 128))).var[0]
    if var < min_sharp: return False, f"blurry (sharpness {var:.0f} < {min_sharp})"
    return True, f"{w}x{h}" + (" 4K" if min(w, h) >= 2160 else " full HD")


def next_set(robe=""):
    used_f = os.path.join(ROOT, "state/used.json")
    used = json.load(open(used_f)) if os.path.exists(used_f) else {"characters": [], "rooms": []}
    pick = {}
    for kind in ("characters", "rooms"):
        free = [p for p in sorted(glob.glob(os.path.join(ROOT, "library", kind, "*.jpg"))) if os.path.basename(p) not in used[kind]]
        for p in list(free):
            ok, why = photo_ok(p, min_sharp=150 if kind == "rooms" else 0)
            if not ok: free.remove(p); reject(p); print(f"REJECTED {os.path.basename(p)}: {why}")
        if not free:
            print(f"NO_{kind.upper()}_LEFT: " + ("ask the creator for Alex's new ROOMS ZIP and run `tools.py add-rooms <zip>`; only if they have none, run find-sets (rooms that look EXACTLY like library/rooms: real phone photos, never AI)." if kind == "rooms" else "run the skill find-sets now (Pinterest search, you pick the good ones), then run next-set again. Ask the creator for photos ONLY if Pinterest fails."))
            return
        pick[kind] = free[0]; used[kind].append(os.path.basename(free[0]))
    json.dump(used, open(used_f, "w"), indent=1)
    print("character:", os.path.relpath(pick["characters"], ROOT)); print("room:", os.path.relpath(pick["rooms"], ROOT))
    if robe:
        m = next_motion(robe)
        mf, dur, how = BROLL_VARIANTS[m]
        if m in ("motion", "motion2"):
            for kind in ("connector", "remote"):
                r = next_fixed(robe, kind)
                if r: print(f"{kind}:", f"products/{robe.lower()}/fixed/{r} (whole clip; log it with {kind}={r})")
        else:
            print("connector + remote: generated INSIDE this B-roll (no fixed tree clips for this video)")
        print(f"motion: {m} -> B-roll from {mf} (duration {dur}) = {how}; edit times in PRODUCT.md; log it with motion={m}")
        song = next_song(robe)
        drop = XMAS_SONGS[song]
        start = f"{drop} - <hook end>" if drop else "0"
        print(f"song: music/xmas/{song} (drop at {drop} s; log it with song={song}) -> edit.json: \"music\": \"music/xmas/{song}\", \"music_start\": {start}, \"music_duck\": <hook end>")
    for kind in ("characters", "rooms"):
        left = len([p for p in glob.glob(os.path.join(ROOT, "library", kind, "*.jpg")) if os.path.basename(p) not in used[kind]])
        if left < 5:
            print(f"ONLY {left} {kind.upper()} LEFT: " + ("ask the creator for Alex's next rooms zip (`tools.py add-rooms <zip>`)." if kind == "rooms" else "after this video run the skill find-sets to add new ones (automatic Pinterest search)."))


def transcribe(f):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("Missing: run  pip install faster-whisper  (Mac/Linux: python3 -m pip install --user faster-whisper; Windows: py -m pip install faster-whisper)"); return
    try:
        m = WhisperModel("base.en", device="cpu", compute_type="int8")
    except Exception as e:
        print("TRANSCRIBE_BLOCKED: cannot download the speech model (needs huggingface.co). In the cloud add *.huggingface.co, huggingface.co, *.hf.co to Allowed domains. Error:", e); return
    import numpy as np
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0   # decode with ffmpeg: works with every PyAV version
    segs, _ = m.transcribe(audio, word_timestamps=True)
    out = []
    for s in segs:
        out.append(f"{s.start:5.2f}-{s.end:5.2f}  {s.text.strip()}")
        out += [f"      {w.start:5.2f}  {w.word.strip()}" for w in (s.words or [])]
    print("\n".join(out) if out else "(no speech - music/sounds only)")


def voice_mix(clip, voice, out, delay, orig_vol="0.3"):
    ms = int(float(delay) * 1000)
    has_a = run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", clip]).stdout.strip()
    if has_a:
        fc = f"[0:a]volume={orig_vol}[o];[1:a]adelay={ms}|{ms},volume=1.6[v];[o][v]amix=inputs=2:duration=first:normalize=0[a]"
    else:
        fc = f"[1:a]adelay={ms}|{ms},volume=1.6,apad[a]"
    run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-i", voice, "-filter_complex", fc, "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-ar", "48000", "-shortest", out]); print(out)


def add_rooms(z):
    """rule 28 Oct (Alex): rooms come from the zips Alex gives (real phone photos of real American homes, picked by him)."""
    import zipfile, io
    from PIL import Image
    d = os.path.join(ROOT, "library/rooms"); os.makedirs(d, exist_ok=True)
    nums = [int(os.path.basename(p)[5:7]) for p in glob.glob(os.path.join(d, "room-*.jpg")) + glob.glob(os.path.join(ROOT, "library/rejected/*room-*.jpg")) if os.path.basename(p)[5:7].isdigit()]
    nums += [int(x[-6:-4]) for x in glob.glob(os.path.join(ROOT, "library/rejected/*room-[0-9][0-9].jpg"))]
    n = max(nums + [0]) + 1; added = []
    with zipfile.ZipFile(z) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().replace("\\", "/").rsplit(".", 1)[-1] in ("jpg", "jpeg", "png", "webp"): continue
            try: im = Image.open(io.BytesIO(zf.read(name))).convert("RGB")
            except Exception: continue
            out = os.path.join(d, f"room-{n:02d}.jpg"); im.save(out, quality=95)
            ok, why = photo_ok(out)
            if not ok: reject(out); print(f"REJECTED {name}: {why}"); n += 1; continue
            added.append((os.path.basename(out), im.size)); n += 1
    for a, sz in added: print(a, f"{sz[0]}x{sz[1]}")
    print(len(added), "rooms added - LOOK at each one (real, sharp, tree, floor free); reject only a broken file")


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


def speech_times(f, until="6"):
    r = run(["ffmpeg", "-v", "error", "-t", str(until), "-i", f, "-af", "highpass=f=300,lowpass=f=3000,astats=metadata=1:reset=2,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-", "-f", "null", "-"]).stdout
    import re
    pts = [(float(a), float(b)) for a, b in zip(re.findall(r"pts_time:([0-9.]+)", r), re.findall(r"RMS_level=(-?[0-9.]+|-inf)", r)) if b != "-inf"]
    if not pts:
        print("no sound"); return
    lv = sorted(v for _, v in pts); thr = lv[len(lv) // 2] + 3
    bursts, cur = [], None
    for t_, v in pts:
        if v >= thr:
            cur = [t_, t_] if cur is None else [cur[0], t_]
        elif cur:
            bursts.append(cur); cur = None
    if cur: bursts.append(cur)
    print("voice bursts:", "  ".join(f"{a:.2f}-{b:.2f}" for a, b in bursts if b - a >= 0.05))


def vocals(f, out):
    import tempfile, shutil
    d = tempfile.mkdtemp(); w = os.path.join(d, "a.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vn", "-ac", "2", "-ar", "44100", w])
    subprocess.run([sys.executable, "-m", "demucs", "--two-stems=vocals", "-n", "htdemucs", "-o", d, w], check=True, capture_output=True)
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-i", os.path.join(d, "htdemucs", "a", "vocals.wav"), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-shortest", out])
    shutil.rmtree(d, ignore_errors=True); print(out, "- only the voice is left; check it with hook-audio")


def _env(f):
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; n = len(x) // 160
    e = np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1)); return np.convolve(e, np.ones(3) / 3, "same")   # 10 ms


def onsets(f, fac="0.2"):
    """seconds where each spoken word/scream starts (energy rising edges). Run it on `vocals` output of the
    REFERENCE hook: our copied hook has the same lip seconds, so these are the targets for the voice."""
    e = _env(f); thr = e.max() * float(fac); out, on, last = [], False, -9
    for i, v in enumerate(e):
        if v > thr and not on and i / 100 - last > 0.3: out.append(round(i / 100, 2)); last = i / 100
        on = v > thr * 0.6 if on else v > thr
    print(out); return out


def place_voice(src, out, dur, targets, starts, cap="0.8"):
    """rule 28 Oct: cut the Seedance voice at `starts` (its own word onsets, from `onsets`) and put each piece
    on `targets` (the reference's word onsets). The last piece runs to the end (the full last phrase).
    A silent bed from 0 s keeps every word on its second (without it amix shifts everything early)."""
    T = [float(x) for x in targets.split(",")]; S = [float(x) for x in starts.split(",")]; dur = float(dur); cap = float(cap)
    assert len(T) == len(S), "targets and starts need the same count"
    sr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=sample_rate", "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip() or "48000"
    full = duration(src); fc = []
    for i, (s, t) in enumerate(zip(S, T)):
        s0 = max(0, s - 0.04); en = min(S[i + 1] - 0.02, s + cap) if i < len(S) - 1 else full
        d = int(max(0, t - 0.04) * 1000)
        fc.append(f"[0:a]atrim={s0:.3f}:{en:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={max(0, en - s0 - 0.03):.3f}:d=0.03,adelay={d}|{d}[p{i}]")
    fc.append(f"aevalsrc=0|0:d={dur}:s={sr}[z]")
    fc.append("[z]" + "".join(f"[p{i}]" for i in range(len(S))) + f"amix=inputs={len(S) + 1}:duration=first:normalize=0,apad,atrim=0:{dur}[o]")
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", ";".join(fc), "-map", "[o]", "-ac", "2", "-ar", "48000", out])
    print(out, "- now check: tools.py onsets", out, "must give the targets", T)


def audit_sound(f, end, expected=""):
    """rule 28 Oct: ALWAYS after a hook/video is made. Separates the sound (Demucs), writes every word with its
    second (Whisper small on the voice only), lists missing/extra words against the expected line, and flags music
    (bass/drums). Extra words in a song-only original = sung lyrics."""
    import tempfile, shutil, re, numpy as np
    d = tempfile.mkdtemp(); w = os.path.join(d, "a.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-t", str(end), "-vn", "-ac", "2", "-ar", "44100", w])
    subprocess.run([sys.executable, "-m", "demucs", "-n", "htdemucs", "-o", d, w], check=True, capture_output=True)
    st = os.path.join(d, "htdemucs", "a")
    def load(p):
        r = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
        return np.frombuffer(r, np.int16).astype(np.float32) / 32768
    rms = lambda x: float(np.sqrt((x ** 2).mean()) + 1e-9)
    mix, v, b, dr = load(w), load(os.path.join(st, "vocals.wav")), load(os.path.join(st, "bass.wav")), load(os.path.join(st, "drums.wav"))
    from faster_whisper import WhisperModel
    segs, _ = WhisperModel("small.en", device="cpu", compute_type="int8").transcribe(v, word_timestamps=True, language="en")
    words = [(round(x.start, 2), x.word.strip()) for sg in segs for x in sg.words]
    norm = lambda t: re.sub(r"[^a-z0-9' ]", "", t.lower().replace("3", "three").replace("2", "two").replace("1", "one")).split()
    got, exp = norm(" ".join(x[1] for x in words)), norm(expected)
    print("words:", " ".join(f"{t}:{x}" for t, x in words))
    print("missing:", [x for x in exp if x not in got] or "none", "| extra:", [x for x in got if x not in exp] or "none",
          "| music:", "CHECK (bass %.2f drums %.2f of the mix; a single thump on an action is a sound effect)" % (rms(b) / rms(mix), rms(dr) / rms(mix)) if rms(b) / rms(mix) > 0.15 or rms(dr) / rms(mix) > 0.25 else "no")
    shutil.rmtree(d, ignore_errors=True)


def blur_for_sound(f, out, box="none", until="99", dur=None):
    """rule 28 Oct: Seedance refuses our robe (ip_detected). For the SOUND pass give it our hook with everything blurred
    except the speaker's face (box = x,y,w,h as fractions; 'none' = all blurred, e.g. POV), face sharp only until <until> s.
    480p, padded to whole seconds (min 4)."""
    import math
    d = float(dur) if dur else max(4, math.ceil(duration(f)))
    if box == "none":
        vf = ["-vf", "tpad=stop_mode=clone:stop_duration=1.5,scale=480:854,boxblur=22:3"]
    else:
        x, y, w, h = box.split(",")
        vf = ["-filter_complex", f"[0:v]tpad=stop_mode=clone:stop_duration=1.5,scale=480:854,split[a][b];[a]boxblur=22:3[bl];[b]crop=iw*{w}:ih*{h}:iw*{x}:ih*{y}[f];[bl][f]overlay=W*{x}:H*{y}:enable='lt(t,{until})'"]
    run(["ffmpeg", "-v", "error", "-y", "-i", f] + vf + ["-t", str(d), "-an", "-c:v", "libx264", "-crf", "22", out])
    print(out, f"- {d:.0f} s; look at one frame: product unrecognisable, the speaker's lips sharp")


def voice_to_lips(seedance, out, end, starts, targets, last_speed="1.0", bg_gain="0.5"):
    """rule 28 Oct: Seedance sound -> voice exactly on the lips with NO cut word and NO gap: Demucs splits voice /
    background; only the PAUSES of the voice are shortened/lengthened so each word starts on its target (the original's
    seconds); the background (ambience + sound effects) stays untouched on our actions; mixed and loudness-normalised."""
    import tempfile, numpy as np
    end = float(end); S = [float(v) for v in starts.split(",")]; T = [float(v) for v in targets.split(",")]
    d = tempfile.mkdtemp(); w = os.path.join(d, "a.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", seedance, "-vn", "-ac", "2", "-ar", "44100", w])
    subprocess.run([sys.executable, "-m", "demucs", "-n", "htdemucs", "-o", d, w], check=True, capture_output=True)
    st = os.path.join(d, "htdemucs", "a"); voc = os.path.join(st, "vocals.wav"); bg = os.path.join(d, "bg.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(st, "drums.wav"), "-i", os.path.join(st, "bass.wav"), "-i", os.path.join(st, "other.wav"), "-filter_complex", "amix=inputs=3:normalize=0", bg])
    db = duration(bg)
    if db < end:   # Seedance often returns ~3.7 s for a 4 s input: continue the room tone (mirrored tail) so the hook never ends in dead silence
        L = min(0.3, db); bg2 = os.path.join(d, "bg2.wav")
        run(["ffmpeg", "-v", "error", "-y", "-i", bg, "-filter_complex",
             f"[0:a]asplit=3[m][t1][t2];[t1]atrim={db - L:.3f},asetpts=PTS-STARTPTS,areverse,asplit=2[r1][r2];[t2]atrim={db - L:.3f},asetpts=PTS-STARTPTS[f];[m][r1][f][r2]concat=n=4:v=0:a=1[o]", "-map", "[o]", bg2])
        bg = bg2
    e = _env(voc); thr = e.max() * 0.06; full = duration(voc); E = []
    for i, s0 in enumerate(S):   # end of each word = voice quiet for 80 ms
        lim = S[i + 1] - 0.05 if i + 1 < len(S) else full; k = int(s0 * 100) + 10
        while k < int(lim * 100) and not all(e[k:k + 8] < thr): k += 1
        E.append(min(lim, k / 100 + 0.05))
    segs, pos, prev = [], 0.0, 0.0
    for i, (s0, t) in enumerate(zip(S, T)):
        ps, pe = prev, max(prev, s0 - 0.02); want = max(0.04, (t - 0.02) - pos); have = pe - ps
        if have > 0.03:
            r = min(4.0, max(0.5, have / want)); segs.append((ps, pe, r)); pos += have / r
        segs.append((pe, E[i], 1.0)); pos += E[i] - pe; prev = E[i]
    if float(last_speed) != 1.0:   # the last phrase spoken faster/slower than the original: stretch only that phrase (pitch kept)
        a0, b0, _ = segs[-1]; segs[-1] = (a0, b0, float(last_speed))
    if full - prev > 0.05: segs.append((prev, full, 1.0))   # a zero-length tail (voice runs to the end) made acrossfade hang
    fc = []
    for j, (a, b, r) in enumerate(segs):
        tempo = []
        while r > 2.0: tempo.append("atempo=2.0"); r /= 2.0
        tempo.append(f"atempo={r:.4f}")
        fc.append(f"[0:a]atrim={a:.3f}:{b + 0.03:.3f},asetpts=PTS-STARTPTS,{','.join(tempo)}[p{j}]")
    ch = "[p0]"
    for j in range(1, len(segs)):
        fc.append(f"{ch}[p{j}]acrossfade=d=0.03:c1=tri:c2=tri[c{j}]"); ch = f"[c{j}]"
    fc.append(f"{ch}apad,atrim=0:{end}[v];[1:a]atrim=0:{end},apad,volume={bg_gain}[b];[v][b]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-16:TP=-1.5,afade=t=out:st={end - 0.05}:d=0.05[o]")
    run(["ffmpeg", "-v", "error", "-y", "-i", voc, "-i", bg, "-filter_complex", ";".join(fc), "-map", "[o]", "-ac", "2", "-ar", "48000", out])
    print(out, "- now audit-sound + onsets + the spectrogram")


def retime(ours, ref, out, end=None):
    """rule 28 Oct: our hook must have EXACTLY the original's seconds. Matches every cut of ours to the
    nearest cut of the reference and speeds/slows each piece so every cut lands on the original's second;
    the result ends exactly where the original hook ends."""
    rc, oc = cuts(ref), cuts(ours)
    end = float(end) if end else duration(ref)
    pairs = []
    for o in oc:   # each of our cuts -> the nearest cut of the original (same shot change)
        c = min(rc, key=lambda x: abs(x - o)) if rc else None
        if c is None or c >= end - 0.05 or abs(c - o) > 1.0: continue
        if not pairs or (c > pairs[-1][0] and o > pairs[-1][1]): pairs.append((c, o))
    src, dst = [0.0] + [p[1] for p in pairs], [0.0] + [p[0] for p in pairs]
    od = duration(ours); last_src = min(od, end * (src[-1] / dst[-1]) if len(src) > 1 and dst[-1] > 0 else end)
    src.append(min(od, max(last_src, src[-1] + 0.1))); dst.append(end)
    parts, fc = [], []
    for i in range(len(src) - 1):
        f = (dst[i + 1] - dst[i]) / max(0.01, src[i + 1] - src[i])
        fc.append(f"[0:v]trim={src[i]:.3f}:{src[i+1]:.3f},setpts=(PTS-STARTPTS)*{f:.4f}[v{i}]"); parts.append(f"[v{i}]")
        print(f"piece {src[i]:.2f}-{src[i+1]:.2f}s -> {dst[i]:.2f}-{dst[i+1]:.2f}s (speed x{1/f:.2f})")
    fc.append("".join(parts) + f"concat=n={len(parts)}:v=1:a=0,fps=30[v]")
    run(["ffmpeg", "-v", "error", "-y", "-i", ours, "-filter_complex", ";".join(fc), "-map", "[v]", "-an", "-t", f"{end:.3f}", "-c:v", "libx264", "-crf", "16", out])
    print(out, "- now every cut is on the original's second; check with compare and cuts")


def cleantext(f, clean, out, boxes):
    w, h = map(int, run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height", "-of", "csv=p=0", f]).stdout.strip().split(","))
    fc, last = [f"[1:v]scale={w}:{h},split={len(boxes) // 4}" + "".join(f"[c{i}]" for i in range(len(boxes) // 4))], "0:v"
    for i in range(len(boxes) // 4):
        l, t_, r, b = (float(x) for x in boxes[i * 4:i * 4 + 4])
        cw, ch, cx, cy = int((r - l) * w) // 2 * 2, int((b - t_) * h) // 2 * 2, int(l * w), int(t_ * h)
        fc.append(f"[c{i}]crop={cw}:{ch}:{cx}:{cy}[p{i}]"); fc.append(f"[{last}][p{i}]overlay={cx}:{cy}[o{i}]"); last = f"o{i}"
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-loop", "1", "-i", clean, "-filter_complex", ";".join(fc), "-map", f"[{last}]", "-map", "0:a?", "-c:a", "copy", "-shortest", out])
    print(out, "- look at a frame: the text must be gone and nothing else covered (faces move into the box? make the box smaller)")


def frame_diffs(f):
    """mean absolute difference between consecutive frames (0-255), with times"""
    import numpy as np
    w, h = 96, 170
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", f"scale={w}:{h},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.int16)
    fps = len(fr) / duration(f)
    return [(round((i + 1) / fps, 2), float(np.abs(fr[i + 1] - fr[i]).mean())) for i in range(len(fr) - 1)], fps


def broll_check(f, motion, folder):
    os.makedirs(folder, exist_ok=True)
    ours, ref = cuts(f), cuts(motion)
    d = duration(f)
    diffs, fps = frame_diffs(f)
    rdiffs, _ = frame_diffs(motion)
    rv = sorted(v for _, v in rdiffs); rmed = rv[len(rv) // 2]
    ref_jumps = [t_ for t_, v in rdiffs if v > max(rmed * 3.5, rmed + 8)]
    scale = d / duration(motion)
    bounds = [0.0] + ours + [d]
    problems, safe = [], []
    if len(ours) != len(ref):
        problems.append(f"SHOT COUNT: ours has {len(ours) + 1} shots, the motion clip {len(ref) + 1} -> Kling merged/added a shot; look at the sheets, redo if a shot is missing or invented")
    for i in range(len(bounds) - 1):
        a, b = bounds[i], bounds[i + 1]
        inside = [v for t_, v in diffs if a + 0.12 < t_ < b - 0.12]
        if inside:
            med = sorted(inside)[len(inside) // 2]
            spikes = [t_ for t_, v in diffs if a + 0.12 < t_ < b - 0.12 and v > max(med * 3.5, med + 12)
                      and not any(abs(t_ - rt * scale) < 0.2 for rt in ref_jumps)]   # jumps the motion clip also has = their own jump cuts, fine
            if spikes:
                problems.append(f"shot {i + 1} ({a:.2f}-{b:.2f}s): sudden jump at {', '.join(str(s) for s in spikes[:5])}s -> possible glitch/morph, look at the sheet")
        sa, sb = round(a + 0.12, 2), round(b - 0.12, 2)
        safe.append((sa, sb))
        sheet_f = os.path.join(folder, f"shot{i + 1}.jpg")
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-t", str(b - a), "-i", f, "-vf", "fps=6,scale=150:-1,tile=8x3", "-frames:v", "1", sheet_f])
    print("cuts ours:", ours, " motion clip:", ref)
    print("SAFE SEGMENTS (use only these in edit.json, 0.12 s away from every cut):", "  ".join(f"{a}-{b}" for a, b in safe))
    print("sheets:", ", ".join(f"{folder}/shot{i + 1}.jpg" for i in range(len(safe))))
    print("PROBLEMS:" if problems else "no automatic problems found - still LOOK at every sheet (person in every frame, face, hands, robe, pouches)")
    for p_ in problems: print(" -", p_)


def words(f, until="8"):
    """[(start, word)] with Whisper, or None if Whisper can't run"""
    try:
        from faster_whisper import WhisperModel
        import numpy as np
        m = WhisperModel("base.en", device="cpu", compute_type="int8")
    except Exception as e:
        print("WHISPER_UNAVAILABLE:", str(e)[:120]); return None
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-t", str(until), "-i", f, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    segs, _ = m.transcribe(np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0, word_timestamps=True)
    return [(round(w.start, 2), w.word.strip()) for s in segs for w in (s.words or [])]


def hook_audio(f, until="8"):
    ws = words(f, until)
    speech_times(f, until)
    if ws is None:
        print("-> Use Higgsfield video_analysis_create on the uploaded hook part (WHO says WHAT), and the voice bursts above for WHEN. Do not skip this.")
        return
    if not ws:
        print("SPEECH: none (music/sounds only) -> no voice in the hook; keep their kind of sounds in the prompt.")
        return
    print("SPEECH: yes")
    for s, w in ws: print(f"  {s:5.2f}s  {w}")
    line = ", ".join(f'"{w}" at {s} s' for s, w in ws)
    print('PUT THIS IN THE HOOK PROMPT (add who says it, from Higgsfield video_analysis or the frames):')
    print(f'Sound: <who> says out loud, <tone>, exactly like in the input video: {line}; <other real sounds>; no music. Their lips move in sync with their words.')


def compare_audio(ref, ours, until="8"):
    a, b = words(ref, until), words(ours, until)
    if a is None or b is None:
        print("Whisper unavailable: compare the voice bursts instead:"); speech_times(ref, until); speech_times(ours, until); return
    print("REFERENCE:", "  ".join(f"{s}:{w}" for s, w in a)); print("OURS:     ", "  ".join(f"{s}:{w}" for s, w in b))
    nums = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}
    def norm(x):
        x = "".join(ch for ch in x.lower() if ch.isalnum()); return nums.get(x, x)
    bad = [w for (s, w) in a if not any(norm(w) == norm(w2) and abs(s - s2) < 0.4 for s2, w2 in b)]
    score = 1 - len(bad) / max(len(a), 1)
    if score >= 0.8:
        print(f"OK - {round(score * 100)}% of the words match at the same seconds" + (f" (Whisper missed: {bad} - listen-check by the voice bursts)" if bad else ""))
    else:
        print(f"NOT OK - only {round(score * 100)}% match. Missing/late in ours: {bad} -> regenerate the hook with every word and its second in the Sound: line")


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
    elif c == "next-set": next_set(a[1] if len(a) > 1 else "")
    elif c == "reject": reject(a[1])
    elif c == "photo-ok": print(*photo_ok(a[1]))
    elif c == "add-rooms": add_rooms(a[1])
    elif c == "transcribe": transcribe(a[1])
    elif c == "voice-mix": voice_mix(*a[1:6])
    elif c == "crop": crop(*a[1:7])
    elif c == "compare": compare(*a[1:6])
    elif c == "log": log(a[1], a[2:])
    elif c == "speech-times": speech_times(a[1], a[2] if len(a) > 2 else "6")
    elif c == "retime": retime(a[1], a[2], a[3], a[4] if len(a) > 4 else None)
    elif c == "vocals": vocals(a[1], a[2])
    elif c == "audit-sound": audit_sound(a[1], a[2], a[3] if len(a) > 3 else "")
    elif c == "blur-for-sound": blur_for_sound(*a[1:6])
    elif c == "voice-to-lips": voice_to_lips(*a[1:8])
    elif c == "onsets": onsets(a[1], a[2] if len(a) > 2 else "0.2")
    elif c == "place-voice": place_voice(*a[1:7])
    elif c == "cleantext": cleantext(a[1], a[2], a[3], a[4:])
    elif c == "broll-check": broll_check(a[1], a[2], a[3])
    elif c == "hook-audio": hook_audio(a[1], a[2] if len(a) > 2 else "8")
    elif c == "compare-audio": compare_audio(a[1], a[2], a[3] if len(a) > 3 else "8")
    elif c == "history": history(a[1] if len(a) > 1 else "5")
    else: print(__doc__)
