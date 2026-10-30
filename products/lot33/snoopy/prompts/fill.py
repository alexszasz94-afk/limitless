import sys,json
n,hair,outfit=sys.argv[1],sys.argv[2],sys.argv[3]
for p in ("P1","P2","P3","P4"):
    t=open(p+".txt").read().replace("<HAIR>",hair).replace("<OUTFIT>",outfit)
    open(f"S{n}-{p}.txt","w").write(t)
