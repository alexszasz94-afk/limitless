"""Builds the creator zips (rule 31 Oct, Alex). Two modes:

  python3 creator-kit-dist/make-update.py "what changed, one line per item"          -> robe-studio-update-<date>.zip
      weekly UPDATE for creators who already have the kit: rules, skills, tools, prompts, guides, products/, motion/, music/
      - NEVER state/, output/ or library/ (their history, videos and photos stay).
  python3 creator-kit-dist/make-update.py --full                                      -> robe-studio-<date>.zip
      the FULL kit for a NEW creator: everything above + library/characters + library/rooms, with EMPTY state files
      (state/used.json = {"characters": [], "rooms": [], "videos": []}, state/media.json = {}), never output/,
      library/rejected, library/candidates, library/rooms-old, library/incoming-rooms.
  add --dry to only count the files and the size (nothing written).
"""
import os, sys, zipfile, datetime, json

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "creator-kit")
EXT = {".md", ".py", ".sh", ".json", ".txt", ".html", ".pdf", ".ttf", ".png"}
FULL = "--full" in sys.argv; DRY = "--dry" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
SKIP_DIRS = {"output", "state", "__pycache__", "rejected", "candidates", "rooms-old", "incoming-rooms", ".git"}
LIB_KEEP = {"characters", "rooms"}
date = datetime.date.today().isoformat()
notes = args[0] if args else "Improvements to the rules and tools."
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"robe-studio-{date}.zip" if FULL else f"robe-studio-update-{date}.zip")
EMPTY_STATE = {"state/used.json": json.dumps({"characters": [], "rooms": [], "videos": []}, indent=1) + "\n", "state/media.json": "{}\n"}

files = []
for root, dirs, fs in os.walk(SRC):
    rel_root = os.path.relpath(root, SRC)
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    if rel_root == "library":
        dirs[:] = [d for d in dirs if FULL and d in LIB_KEEP]
    if rel_root == "." and not FULL:
        dirs[:] = [d for d in dirs if d != "library"]
    for f in fs:
        rel = os.path.normpath(os.path.join(rel_root, f))
        if f == ".env" or rel.startswith("library" + os.sep) and not FULL:
            continue
        media = rel.startswith(("products" + os.sep, "motion" + os.sep, "music" + os.sep, "library" + os.sep, "engine" + os.sep))
        if os.path.splitext(f)[1].lower() in EXT or media or f in (".gitignore", ".mcp.json"):
            files.append(rel)
size = sum(os.path.getsize(os.path.join(SRC, f)) for f in files)
if DRY:
    print(("FULL" if FULL else "UPDATE"), len(files), "files,", size // (1024 * 1024), "MB before compression ->", out)
    print("state files:", list(EMPTY_STATE) if FULL else "none (update keeps the creator's state)")
    sys.exit()
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for rel in files:
        z.write(os.path.join(SRC, rel), rel)
    if FULL:
        for rel, txt in EMPTY_STATE.items():
            z.writestr(rel, txt)
        z.writestr("output/.keep", "")
    else:
        z.writestr("UPDATE-NOTES.md", f"# Robe Studio update {date}\n\n{notes}\n")
print(out, len(files), "files", os.path.getsize(out) // 1024, "KB")
