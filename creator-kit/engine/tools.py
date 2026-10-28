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
  python3 engine/tools.py speech-times <video> [seconds]                  -> when the voice bursts are (start-end), to put each spoken word on its exact second
  python3 engine/tools.py cleantext <video> <clean.jpg> <out.mp4> <l> <t> <r> <b> [...more boxes]  -> covers their on-screen text with the same spot from a clean photo (static camera only) - no blur for Kling to copy
  python3 engine/tools.py broll-check <broll.mp4> <motion.mp4> <out-folder>   -> B-roll safety check: shot count vs the motion clip, glitch spikes inside shots, safe segments, one sheet per shot to look at
  python3 engine/tools.py vocals <hook.mp4> <out.mp4>                    -> keeps ONLY the voice of a copied hook (Demucs) - Kling copies the original music, never deliver it (rule 28 Oct)
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
    for kind in ("characters", "rooms"):
        left = len([p for p in glob.glob(os.path.join(ROOT, "library", kind, "*.jpg")) if os.path.basename(p) not in used[kind]])
        if left < 5:
            print(f"ONLY {left} {kind.upper()} LEFT: after this video run the skill find-sets to add new ones (automatic Pinterest search).")


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
    elif c == "next-set": next_set()
    elif c == "reject": reject(a[1])
    elif c == "transcribe": transcribe(a[1])
    elif c == "voice-mix": voice_mix(*a[1:6])
    elif c == "crop": crop(*a[1:7])
    elif c == "compare": compare(*a[1:6])
    elif c == "log": log(a[1], a[2:])
    elif c == "speech-times": speech_times(a[1], a[2] if len(a) > 2 else "6")
    elif c == "vocals": vocals(a[1], a[2])
    elif c == "cleantext": cleantext(a[1], a[2], a[3], a[4:])
    elif c == "broll-check": broll_check(a[1], a[2], a[3])
    elif c == "hook-audio": hook_audio(a[1], a[2] if len(a) > 2 else "8")
    elif c == "compare-audio": compare_audio(a[1], a[2], a[3] if len(a) > 3 else "8")
    elif c == "history": history(a[1] if len(a) > 1 else "5")
    else: print(__doc__)
