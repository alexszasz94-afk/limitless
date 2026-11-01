"""data/summary-<date>.json (+ picks.json written by Claude after watching the best videos) -> data/board-<date>.json,
the single document 'board/latest' of the artifact's database.
  python3 build_board.py data/summary-<date>.json"""
import json, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
s = json.load(open(sys.argv[1]))
cfg = json.load(open(os.path.join(HERE, "accounts.json")))
order = [c["name"] for c in cfg["creators"]]
creators = {n: {"name": n, "accounts": []} for n in order}
for a in s["accounts"]:
    acc = {k: a.get(k) for k in ("platform", "followers", "posts_scanned", "posts_24h", "posts_per_day", "views_total", "views_median",
                                 "best", "best_views", "last_post", "last7_by_day")}
    acc["error"] = None if a.get("posts_scanned") else (a.get("error") or "no videos found")
    acc["error"] = {"no videos found (not_available)": "private profile or not a public page",
                    "could not find the page of the reel": "only a reel link was given, not the page"}.get(acc["error"], acc["error"])
    acc_name = a.get("account")
    if acc_name and not str(acc_name).startswith("http"):
        acc["handle"] = acc_name
        acc["url"] = {"tiktok": f"https://www.tiktok.com/@{acc_name}", "instagram": f"https://www.instagram.com/{acc_name}/"}.get(a["platform"])
    else:
        acc["url"] = acc_name
    creators[a["creator"]]["accounts"].append(acc)
picks_f = os.path.join(HERE, "picks.json")
picks = json.load(open(picks_f)) if os.path.exists(picks_f) else []
board = {"scanned_at": s["scanned_at"], "target_per_day": s["target_per_day"], "posts_per_account": 15,
         "creators": list(creators.values()),
         "top_posts": [{k: p.get(k) for k in ("creator", "platform", "url", "posted", "views", "caption", "x_median")} for p in s["top_posts"][:15]],
         "picks": picks}
out = sys.argv[1].replace("summary-", "board-")
json.dump(board, open(out, "w"), indent=1, ensure_ascii=False)
print(out, len(json.dumps(board)) // 1024, "KB")
