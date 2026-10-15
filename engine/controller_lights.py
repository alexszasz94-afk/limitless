"""Telecomandă cu luminițe exacte 1→5 (prințesa): poza plăcii + lumină compusă + clicuri reale.
Rulare: python3 engine/controller_lights.py PLACA.png AUDIO.mp4 OUT.mp4
Pozițiile cristalelor sunt pentru placa 16b4e3e8 (1080x1920): x=542, y 1104/975/858/743/635.
Motiv: Genjutsu și Kling nu numără corect luminițele (15 oct)."""
import sys, math, random, subprocess, tempfile, os
from PIL import Image, ImageDraw, ImageFilter, ImageChops
plate, audio, out = sys.argv[1:4]
base = Image.open(plate).convert('RGB').resize((1080, 1920), Image.LANCZOS)
cx = 542; ys = {1: 1104, 2: 975, 3: 858, 4: 743, 5: 635}
def glow(img, y):
    lay = Image.new('RGB', img.size, (0, 0, 0)); d = ImageDraw.Draw(lay)
    for r, a in [(70, 25), (50, 45), (34, 80), (22, 140), (14, 220)]:
        d.ellipse([cx-r, y-r, cx+r, y+r], fill=(int(a*.95), int(a*.55), int(a*1.0)))
    o = ImageChops.add(img, lay.filter(ImageFilter.GaussianBlur(9)))
    ImageDraw.Draw(o).ellipse([cx-9, y-9, cx+9, y+9], fill=(255, 235, 255)); return o
states = {k: glow(base, ys[k]) for k in ys}
fps, dur, changes = 24, 5.0, [0.6, 1.7, 2.8, 3.9]
tmp = tempfile.mkdtemp()
for i in range(int(fps*dur)):
    t = i/fps; k = 1 + sum(t >= c for c in changes)
    dip = 3 if any(c-0.05 <= t < c+0.12 for c in changes) else 0
    dx = 2.2*math.sin(t*1.7)+1.1*math.sin(t*4.3); dy = 1.8*math.sin(t*1.3+1)+0.9*math.sin(t*3.7)+dip
    f = states[k].rotate(0.25*math.sin(t*1.1), resample=Image.BICUBIC, translate=(dx, dy))
    f.crop((24, 43, 1056, 1877)).resize((1080, 1920), Image.LANCZOS).save(f'{tmp}/f{i:04d}.png')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(fps), '-i', f'{tmp}/f%04d.png', '-i', audio, '-map', '0:v', '-map', '1:a',
                '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest', out], check=True)
