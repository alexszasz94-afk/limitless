"""Randare-ghid exactă pentru Tree Prix (cerc + semafor + linie start + mașina ca bloc orientat corect).
Folosire: python3 render_scena.py <vedere> <out.png>   vederi: hero | aproape | pov
Sens de mers: trigonometric (văzut de sus), deci bradul e mereu în STÂNGA mașinii și pista se curbează spre stânga."""
import sys, numpy as np
from PIL import Image, ImageDraw
VIEW, OUT = sys.argv[1], sys.argv[2]
TREE_H, TREE_R = 213, 70
tree = lambda h: TREE_R * (1 - h / TREE_H)
RH, RR, LANE = 70, 55, 10                      # înălțime cerc, rază, lățime bandă
TH_G = np.radians(-55)                          # semaforul în față-dreapta (să se vadă din față)
TH_C = TH_G - np.radians(17)
import os
if os.environ.get('CAR_DEG'): TH_C = np.radians(float(os.environ['CAR_DEG']))
LIGHTS_ON = os.environ.get('LIGHTS', '1') == '1'                    # mașina: înainte de linie (sens trigonometric)
W, H = 1080, 1920
quads = []                                      # (puncte 3D, culoare, verificare_ocluzie)
def ringpt(th, off, z=RH): r = RR + off; return np.array([r*np.cos(th), r*np.sin(th), z])
def band(o1, o2, col, z=RH, n=720, colfn=None, th0=0, th1=2*np.pi):
    ts = np.linspace(th0, th1, n+1)
    for i in range(n):
        q = np.array([ringpt(ts[i], o1, z), ringpt(ts[i+1], o1, z), ringpt(ts[i+1], o2, z), ringpt(ts[i], o2, z)])
        quads.append((q, colfn(i) if colfn else col, True))
band(-5, 5, (72, 72, 74)); band(-0.35, 0.35, (15, 15, 15))
band(-1.0, -0.6, (205, 205, 210)); band(0.6, 1.0, (205, 205, 210))
kerb = lambda i: (200, 40, 40) if (i // 4) % 2 else (240, 240, 240)
band(-5.8, -5, None, colfn=kerb); band(5, 5.8, None, colfn=kerb)
band(5.8, 6.3, (255, 236, 190), z=RH+0.8)        # LED doar pe marginea exterioară
# linie în carouri peste toată banda, sub semafor
for k in range(10):
    for j in range(2):
        o1 = -5 + k; th = TH_G + np.radians(0.8*j); th2 = th + np.radians(0.8)
        q = np.array([ringpt(th, o1, RH+0.05), ringpt(th2, o1, RH+0.05), ringpt(th2, o1+1, RH+0.05), ringpt(th, o1+1, RH+0.05)])
        quads.append((q, (20, 20, 20) if (k + j) % 2 else (245, 245, 245), True))
def box(center, ax_t, ax_r, sx, sy, sz, col):
    c = center; ax_z = np.array([0, 0, 1])
    P = lambda a, b, d: c + ax_t*a*sx/2 + ax_r*b*sy/2 + ax_z*d*sz
    faces = [[(-1,-1,0),(1,-1,0),(1,1,0),(-1,1,0)], [(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)],
             [(-1,-1,0),(1,-1,0),(1,-1,1),(-1,-1,1)], [(-1,1,0),(1,1,0),(1,1,1),(-1,1,1)],
             [(-1,-1,0),(-1,1,0),(-1,1,1),(-1,-1,1)], [(1,-1,0),(1,1,0),(1,1,1),(1,-1,1)]]
    shade = [0.6, 1.0, 0.8, 0.8, 0.7, 0.9]
    for f, s in zip(faces, shade):
        quads.append((np.array([P(*v) for v in f]), tuple(int(x*s) for x in col), True))
def frame(th):
    radial = np.array([np.cos(th), np.sin(th), 0]); tang = np.array([-np.sin(th), np.cos(th), 0]); return tang, radial
# semafor: 2 picioare pe borduri + bară sus + 5 lumini
t, r = frame(TH_G)
for off in (-5.4, 5.4): box(ringpt(TH_G, off), t, r, 1, 1, 12, (25, 25, 25))
box(ringpt(TH_G, 0, RH+11), t, r, 1.6, 12, 2.5, (25, 25, 25))
for k in range(5):
    c = ringpt(TH_G, -3.6 + 1.8*k, RH+12.2) - t*0.85
    quads.append((np.array([c + r*0.6, c + r*0.6 + np.array([0,0,0.0]) + np.array([0,0,1.2])*0, c, c]) , (0,0,0), True)) if False else None
    q = np.array([c - r*0.6, c + r*0.6, c + r*0.6 + np.array([0, 0, 1.2]) - np.array([0,0,2.4]), c - r*0.6 - np.array([0, 0, 1.2])])
    quads.append((np.array([c - r*0.6 + [0,0,0.6], c + r*0.6 + [0,0,0.6], c + r*0.6 - [0,0,0.6], c - r*0.6 - [0,0,0.6]]), (230, 30, 30) if LIGHTS_ON else (60, 20, 20), True))
# mașina: bloc 16 x 6 x 4, orientat pe tangentă, centrat pe șanț; bot spre sensul de mers
t, r = frame(TH_C)
box(ringpt(TH_C, 0), t, r, 16, 6, 3, (190, 25, 25))
box(ringpt(TH_C, 0) + t*7.2, t, r, 1.6, 7.5, 0.8, (30, 30, 30))      # aripa față (în sensul de mers)
box(ringpt(TH_C, 0) - t*7.2, t, r, 1.6, 6.5, 3.8, (30, 30, 30))      # aripa spate
# camere
if VIEW in ("hero", "cursa"):
    cam = np.array([0, -340, 120]); look = np.array([0, 0, 95]); fov = np.radians(40)
elif VIEW == "aproape":                          # din spatele mașinii, la nivelul pistei, puțin în afara cercului
    t, r = frame(TH_C); cam = ringpt(TH_C, 4, RH + 13) - t*32; look = ringpt(TH_G, -6, RH + 3); fov = np.radians(60)
elif VIEW == "pov":                              # ochii pilotului, în cockpit, privind înainte pe tangentă
    t, r = frame(TH_C); cam = ringpt(TH_C, 0, RH + 6) - t*5; look = cam + t*50 - r*14 - np.array([0, 0, 7]); fov = np.radians(80)
fwd = (look - cam) / np.linalg.norm(look - cam); right = np.cross(fwd, [0, 0, 1]); right /= np.linalg.norm(right); up = np.cross(right, fwd)
fpx = (H / 2) / np.tan(fov / 2)
def proj(P):
    d = P - cam; return np.c_[W/2 + fpx*(d@right)/(d@fwd), H/2 - fpx*(d@up)/(d@fwd)], d@fwd
CORE = lambda z: tree(z) - 12
def hidden(P):
    ts = np.linspace(0.02, 0.98, 50)[:, None]; R = cam + (P - cam)*ts; rr = np.hypot(R[:, 0], R[:, 1])
    return np.any((R[:, 2] > 0) & (R[:, 2] < TREE_H) & (rr < CORE(R[:, 2])))
img = Image.new("RGB", (W, H), (236, 230, 218)); dr = ImageDraw.Draw(img)
# podea
if VIEW in ("hero", "cursa"): dr.rectangle([0, int(H*0.8), W, H], fill=(190, 160, 120))
# brad: con opac (fețele vizibile), desenat după adâncime împreună cu restul
zs = np.linspace(0, TREE_H, 90); ths = np.linspace(0, 2*np.pi, 160)
for i in range(len(zs)-1):
    for j in range(len(ths)-1):
        pz = lambda z, th: np.array([CORE(z)*np.cos(th) if VIEW not in ('hero','cursa') else tree(z)*np.cos(th), (CORE(z) if VIEW not in ('hero','cursa') else tree(z))*np.sin(th), z])
        q = np.array([pz(zs[i], ths[j]), pz(zs[i], ths[j+1]), pz(zs[i+1], ths[j+1]), pz(zs[i+1], ths[j])])
        n = np.array([np.cos((ths[j]+ths[j+1])/2), np.sin((ths[j]+ths[j+1])/2), 0])
        if (q.mean(0) - cam) @ n > 0: continue
        g = 70 + int(30*abs(n[0])); quads.append((q, (25, g, 40), False))
order = sorted(quads, key=lambda qc: -np.mean((qc[0] - cam) @ fwd))
for q, col, chk in order:
    xy, z = proj(q)
    if (z <= 1).any(): continue
    if chk and VIEW in ("hero", "cursa") and hidden(q.mean(0)): continue
    dr.polygon([tuple(v) for v in xy], fill=col)
img.save(OUT); print(OUT)
