"""Text pe ecran cu steaguri (perechi de litere regionale) — patch pentru montage.clusters.
Folosire: python3 buttcracker_cap.py '<text>' out.png"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import montage
_orig = montage.clusters
def clusters(text):
    out = []
    for e, s in _orig(text):
        if e and out and out[-1][0] and len(out[-1][1]) == 1 and 0x1F1E6 <= ord(out[-1][1][0]) <= 0x1F1FF and 0x1F1E6 <= ord(s[0]) <= 0x1F1FF:
            out[-1] = (True, out[-1][1] + s)
        else:
            out.append((e, s))
    return out
montage.clusters = clusters
if __name__ == "__main__":
    montage.text_png(sys.argv[1], sys.argv[2], 62, 0.10)
