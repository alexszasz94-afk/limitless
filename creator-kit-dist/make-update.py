"""Builds a small weekly update for creators: python3 creator-kit-dist/make-update.py "what changed, one line per item"
Output: creator-kit-dist/robe-studio-update-<date>.zip (rules, skills, tools, prompts, guides — no big media, no creator state)."""
import os, sys, zipfile, datetime
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "creator-kit")
EXT = {".md", ".py", ".sh", ".json", ".txt", ".html", ".pdf"}
SKIP_DIRS = {"output", "state", "__pycache__", "library"}
date = datetime.date.today().isoformat()
notes = sys.argv[1] if len(sys.argv) > 1 else "Improvements to the rules and tools."
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"robe-studio-update-{date}.zip")
n = 0
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(SRC):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if os.path.splitext(f)[1] in EXT and f != ".env":
                p = os.path.join(root, f); z.write(p, os.path.relpath(p, SRC)); n += 1
    z.writestr("UPDATE-NOTES.md", f"# Robe Studio update {date}\n\n{notes}\n")
print(out, n, "files", os.path.getsize(out) // 1024, "KB")
