"""Randare-ghid exactă a cercului (un singur cerc, 23 oct) pentru generarea pozelor realiste. Folosire: python3 render_ghid.py <az_grade> <out.png>"""
import sys, numpy as np
from PIL import Image, ImageDraw
sys.argv += [] ; AZ = float(sys.argv[1]) if len(sys.argv) > 1 else 0; OUT = sys.argv[2] if len(sys.argv) > 2 else "ghid.png"
TREE_H, TREE_R = 213, 70
tree = lambda h: TREE_R * (1 - h / TREE_H)
H0, H1, OUT_GAP, SEP = 50, 85, 8, 15
c0, c1 = np.radians(60), np.radians(120); span = c0 + 2*np.pi - c1
Rout = lambda h: tree(h) + OUT_GAP; Rin = lambda h: tree(h) + OUT_GAP - SEP
ease = lambda t, a, b: (1 - np.cos(np.pi*(t-a)/(b-a))) / 2
pts = []
RING_H = 70; RING_R = tree(RING_H) + 8          # un singur cerc: 70 cm de la podea, raza 55 cm (Ø 110)
t = np.linspace(0, 2*np.pi, 1400); pts.append(np.c_[RING_R*np.cos(t), RING_R*np.sin(t), np.full_like(t, RING_H)])
C = np.vstack(pts)
# rotate so the camera looks from azimuth AZ (0 = front = -y)
a = np.radians(AZ); rot = np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]])
C = C @ rot.T
W, Hh = 1080, 1920; cam = np.array([0, -230, 125]); look = np.array([0, 0, 72]); fov = np.radians(46)
fwd = (look-cam)/np.linalg.norm(look-cam); right = np.cross(fwd, [0, 0, 1]); right /= np.linalg.norm(right); up = np.cross(right, fwd)
fpx = (Hh/2)/np.tan(fov/2)
def proj(P):
    d = P - cam; x = d@right; y = d@up; z = d@fwd
    return np.c_[W/2 + fpx*x/z, Hh/2 - fpx*y/z], z
quads = []
tang = np.gradient(C, axis=0); tang[:, 2] = 0; tang /= np.linalg.norm(tang, axis=1)[:, None]
nrm = np.c_[tang[:, 1], -tang[:, 0], np.zeros(len(C))]   # horizontal normal
def band(o1, o2, colfn):
    A = C + nrm*o1; B = C + nrm*o2
    for i in range(len(C)-1):
        q = np.array([A[i], A[i+1], B[i+1], B[i]]); quads.append((q, colfn(i)))
band(-5, 5, lambda i: (70, 70, 72))                              # lane
band(-0.4, 0.4, lambda i: (20, 20, 20))                          # slot
band(-1.0, -0.6, lambda i: (200, 200, 205)); band(0.6, 1.0, lambda i: (200, 200, 205))  # rails
band(-5.8, -5, lambda i: (210, 30, 30) if (i//6) % 2 else (240, 240, 240))
band(5, 5.8, lambda i: (210, 30, 30) if (i//6) % 2 else (240, 240, 240))
CORE = lambda z: tree(z) - 12          # visible "solid" part of the tree, branch tips are softer
def hidden(P):
    ts = np.linspace(0.02, 0.98, 60)[:, None]; R = cam + (P - cam) * ts
    r = np.hypot(R[:, 0], R[:, 1]); return np.any((R[:, 2] > 0) & (R[:, 2] < TREE_H) & (r < CORE(R[:, 2])))
img = Image.new("RGB", (W, Hh), (235, 228, 215)); dr = ImageDraw.Draw(img)
dr.rectangle([0, int(Hh*0.80), W, Hh], fill=(190, 160, 120))
# tree silhouette (front faces of the cone, branch-tip radius)
zs = np.linspace(0, TREE_H, 120); ths = np.linspace(0, 2*np.pi, 180)
for i in range(len(zs)-1):
    for j in range(len(ths)-1):
        thm = (ths[j]+ths[j+1])/2
        if np.sin(thm - np.radians(0)) > 0.15: continue   # back faces (camera at -y)
        pz = lambda z, th: np.array([tree(z)*np.cos(th), tree(z)*np.sin(th), z])
        q = np.array([pz(zs[i], ths[j]), pz(zs[i], ths[j+1]), pz(zs[i+1], ths[j+1]), pz(zs[i+1], ths[j])])
        g = 60 + int(40*max(0, -np.sin(thm))); xy, _ = proj(q); dr.polygon([tuple(v) for v in xy], fill=(25, g, 40))
order = sorted(quads, key=lambda qc: -np.mean((qc[0]-cam)@fwd))
for q, col in order:
    if hidden(q.mean(axis=0)): continue
    xy, z = proj(q)
    if (z <= 0).any(): continue
    dr.polygon([tuple(v) for v in xy], fill=col)
img.save(OUT); print(OUT)
