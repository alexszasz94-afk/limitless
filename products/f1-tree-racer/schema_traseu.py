"""Schema traseului F1 Tree Racer (v2, 23 oct): pista urmează conul bradului, S-uri pe 60°, verificare de coliziuni."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
TREE_H, TREE_R = 213, 70                      # brad 7 ft, raza la bază 70 cm
tree = lambda h: TREE_R * (1 - h / TREE_H)
H0, H1 = 50, 85                               # jos / sus (cm de la podea)
OUT_GAP, LANE_SEP = 8, 15                     # pista exterioară la 8 cm de vârful crengilor; interioara cu 15 cm mai înăuntru
c0, c1 = np.radians(60), np.radians(120)      # sectorul S-urilor, în spate (90°)
span = c0 + 2 * np.pi - c1
Rout = lambda h: tree(h) + OUT_GAP
Rin = lambda h: tree(h) + OUT_GAP - LANE_SEP
def seg(t, R, h, kind): return np.c_[R * np.cos(t), R * np.sin(t), h, np.full_like(t, kind)]
def ease(t, a, b): return (1 - np.cos(np.pi * (t - a) / (b - a))) / 2
N = 600
t = np.linspace(c1, c0 + 2 * np.pi, N); f = (t - c1) / span
up = seg(t, Rout(H0 + (H1 - H0) * f), H0 + (H1 - H0) * f, 0)
t = np.linspace(c0, c1, 120); e = ease(t, c0, c1)
topS = seg(t, Rout(H1) + (Rin(H1) - Rout(H1)) * e, np.full_like(t, H1), 1)
t = np.linspace(c1, c0 + 2 * np.pi, N); f = (t - c1) / span
down = seg(t, Rin(H1 - (H1 - H0) * f), H1 - (H1 - H0) * f, 2)
t = np.linspace(c0, c1, 120); e = ease(t, c0, c1)
botS = seg(t, Rin(H0) + (Rout(H0) - Rin(H0)) * e, np.full_like(t, H0), 3)
segs = [up, topS, down, botS]

def length(p): return np.sum(np.linalg.norm(np.diff(p[:, :3], axis=0), axis=1))
def grade(p): return (p[-1, 2] - p[0, 2]) / np.sum(np.linalg.norm(np.diff(p[:, :2], axis=0), axis=1)) * 100
# coliziuni: puncte din bucăți diferite, nevecine, prea aproape (bandă 10 cm, gabarit vertical 12 cm)
allp = np.vstack(segs); idx = np.arange(len(allp)); worst = 1e9; where = None
for i in range(0, len(allp), 3):
    d_xy = np.hypot(allp[:, 0] - allp[i, 0], allp[:, 1] - allp[i, 1]); d_z = np.abs(allp[:, 2] - allp[i, 2])
    far = np.abs(idx - i) > 60; far &= np.abs(idx - i) < len(allp) - 60
    bad = far & (d_xy < 11) & (d_z < 12)
    if bad.any(): worst = 0; where = allp[i]
    m = np.min(np.where(far, np.maximum(d_xy - 11, 0) + np.maximum(d_z - 12, 0), 1e9))
    worst = min(worst, m)
report = [
    f"Up (outer lane): {length(up):.0f} cm, grade {grade(up):.1f}%",
    f"Down (inner lane): {length(down):.0f} cm, grade {abs(grade(down)):.1f}%",
    f"S-crossovers: {length(topS):.0f} cm each, over {np.degrees(c1-c0):.0f} deg",
    f"Outer lane radius: {Rout(H0):.0f} cm (bottom) -> {Rout(H1):.0f} cm (top)",
    f"Inner lane radius: {Rin(H0):.0f} cm (bottom) -> {Rin(H1):.0f} cm (top), 7 cm into the branch tips",
    "Collision check: " + ("OK, the track never touches itself (lanes 10 cm, 12 cm vertical clearance)" if where is None else f"PROBLEM at {where[:3].round(0)}"),
]
print("\n".join(report))

col = ['#d62828', '#444444', '#f77f00', '#444444']
lab = ['UP: outer lane', 'Top S (85 cm)', 'DOWN: inner lane', 'Bottom S (50 cm)']
fig = plt.figure(figsize=(16, 7))
ax = fig.add_subplot(1, 3, 1, projection='3d')
z = np.linspace(0, TREE_H, 40); th = np.linspace(0, 2 * np.pi, 40); Z, T = np.meshgrid(z, th)
ax.plot_surface(tree(Z) * np.cos(T), tree(Z) * np.sin(T), Z, color='#2d6a4f', alpha=0.10, linewidth=0)
for p, c, l in zip(segs, col, lab): ax.plot(p[:, 0], p[:, 1], p[:, 2], color=c, lw=3.5, label=l)
ax.set_xlim(-75, 75); ax.set_ylim(-75, 75); ax.set_zlim(0, 213); ax.set_box_aspect((150, 150, 213))
ax.view_init(elev=15, azim=-70); ax.set_title('3D view (cm)'); ax.legend(loc='upper left', fontsize=8)
ax2 = fig.add_subplot(1, 3, 2)
for p, c in zip(segs, col): ax2.plot(p[:, 0], p[:, 1], color=c, lw=3)
ax2.add_patch(plt.Circle((0, 0), 3, color='saddlebrown'))
ax2.text(0, 66, 'BACK: 2 S-crossovers,\nthe top one 35 cm above the bottom one', ha='center', fontsize=8)
ax2.text(0, -72, 'FRONT of tree', ha='center', fontsize=9)
ax2.set_aspect('equal'); ax2.set_xlim(-75, 75); ax2.set_ylim(-78, 78); ax2.set_title('Top view')
ax3 = fig.add_subplot(1, 3, 3)
for p, c, l in zip(segs, col, lab):
    ang = (np.degrees(np.arctan2(p[:, 1], p[:, 0])) - 90) % 360
    ax3.scatter(ang, p[:, 2], s=2, color=c)
ax3.set_xlabel('angle around tree (0 = back, 180 = front)'); ax3.set_ylabel('height (cm)')
ax3.set_title('Height vs position around the tree')
ax3.annotate('at the front both lanes pass\nSIDE BY SIDE at the same height,\n15 cm apart (like a 2-lane road):\nthey never touch', xy=(180, 67.5), xytext=(95, 92), fontsize=8, arrowprops=dict(arrowstyle='->'))
ax3.set_ylim(40, 105)
fig.text(0.5, 0.005, "   |   ".join(report[:3]) + "\n" + "   |   ".join(report[3:]), ha='center', fontsize=9)
plt.tight_layout(rect=(0, 0.07, 1, 1)); plt.savefig('/home/user/limitless/products/f1-tree-racer/schema-traseu.png', dpi=120)
