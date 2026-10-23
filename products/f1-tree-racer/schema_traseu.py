import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
Ro,Ri,H,h0=60,45,45,50
# crossover sector at the back: theta 250..290 deg (back = 270)
c0,c1=np.radians(70),np.radians(110)
def path():
    pts=[]
    # up spiral outer: from theta=c1 to c0+2pi, h 50->95
    t=np.linspace(c1,c0+2*np.pi,400); f=(t-c1)/(c0+2*np.pi-c1)
    pts.append(np.c_[Ro*np.cos(t),Ro*np.sin(t),h0+H*f,np.zeros_like(t)])
    # top S: c0->c1 (next turn), R 60->45 at h 95
    t=np.linspace(c0,c1,60); s=(1-np.cos(np.pi*(t-c0)/(c1-c0)))/2
    R=Ro+(Ri-Ro)*s; pts.append(np.c_[R*np.cos(t),R*np.sin(t),np.full_like(t,h0+H),np.ones_like(t)])
    # down spiral inner: c1 -> c0+2pi, h 95->50
    t=np.linspace(c1,c0+2*np.pi,400); f=(t-c1)/(c0+2*np.pi-c1)
    pts.append(np.c_[Ri*np.cos(t),Ri*np.sin(t),h0+H*(1-f),2*np.ones_like(t)])
    # bottom S: R 45->60 at h 50
    t=np.linspace(c0,c1,60); s=(1-np.cos(np.pi*(t-c0)/(c1-c0)))/2
    R=Ri+(Ro-Ri)*s; pts.append(np.c_[R*np.cos(t),R*np.sin(t),np.full_like(t,h0),3*np.ones_like(t)])
    return pts
P=path(); col=['#d62828','#555555','#f77f00','#555555']; lab=['UP: outer lane Ø120, +45 cm (12%)','Top S-crossover (h 95 cm)','DOWN: inner lane Ø90, -45 cm (16%)','Bottom S-crossover (h 50 cm)']
fig=plt.figure(figsize=(12,6.5))
ax=fig.add_subplot(1,2,1,projection='3d')
# tree cone
z=np.linspace(0,213,40); th=np.linspace(0,2*np.pi,40); Z,T=np.meshgrid(z,th); Rr=70*(1-Z/213)+3
ax.plot_surface(Rr*np.cos(T),Rr*np.sin(T),Z,color='#2d6a4f',alpha=0.12,linewidth=0)
for p,c,l in zip(P,col,lab): ax.plot(p[:,0],p[:,1],p[:,2],color=c,lw=3.5,label=l)
ax.set_xlim(-80,80);ax.set_ylim(-80,80);ax.set_zlim(0,213);ax.set_box_aspect((160,160,213))
ax.view_init(elev=12,azim=-90); ax.set_title('Front view (3D), cm'); ax.set_xlabel('cm');ax.set_zlabel('height cm')
ax.legend(loc='upper left',fontsize=8,bbox_to_anchor=(-0.1,1.02))
ax2=fig.add_subplot(1,2,2)
for p,c in zip(P,col): ax2.plot(p[:,0],p[:,1],color=c,lw=3.5)
ax2.add_patch(plt.Circle((0,0),3,color='saddlebrown')); ax2.text(0,6,'trunk',ha='center',fontsize=8)
ax2.annotate('2 S-crossovers, back of tree\n(top one 45 cm above the bottom one)',xy=(0,55),xytext=(0,22),ha='center',fontsize=9,arrowprops=dict(arrowstyle='->'))
ax2.annotate('car direction',xy=(42,-42),xytext=(58,-75),fontsize=9,arrowprops=dict(arrowstyle='->'))
ax2.set_aspect('equal'); ax2.set_xlim(-75,75); ax2.set_ylim(-80,75); ax2.set_title('Top view: outer lane Ø120, inner lane Ø90 (5 cm apart)'); ax2.set_xlabel('cm')
ax2.text(0,-72,'FRONT of tree (camera side)',ha='center',fontsize=9)
plt.tight_layout(); plt.savefig('schema-traseu.png',dpi=130)
