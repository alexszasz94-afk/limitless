"""Summary of a scan: per creator and account - posts per day vs the target (5/day per social), views, best videos.
  python3 analyze.py data/scan-<date>.json  -> data/summary-<date>.json + a printed table"""
import json, sys, datetime, statistics, os

TARGET = 5
scan = json.load(open(sys.argv[1]))
now = datetime.datetime.fromisoformat(scan["scanned_at"].rstrip("Z"))


def dt(s):
    if not s: return None
    s = s.rstrip("Z").split("+")[0].replace(" ", "T")
    try: return datetime.datetime.fromisoformat(s[:19])
    except Exception: return None


rows, allposts = [], []
for a in scan["accounts"]:
    ps = [dict(p, _t=dt(p.get("posted"))) for p in a["posts"]]
    ps = [p for p in ps if p["_t"]]
    last24 = [p for p in ps if now - p["_t"] <= datetime.timedelta(hours=24)]
    last7 = [p for p in ps if now - p["_t"] <= datetime.timedelta(days=7)]
    days = {}
    for p in last7: days[p["_t"].date().isoformat()] = days.get(p["_t"].date().isoformat(), 0) + 1
    oldest = min((p["_t"] for p in ps), default=None)
    covered_days = max(1.0, (now - oldest).total_seconds() / 86400) if oldest else None
    full = len(a["posts"]) >= scan["posts_per_account"]   # the scan may not reach back 7 days
    views = [p["views"] or 0 for p in ps]
    med = statistics.median(views) if views else 0
    for p in ps:
        allposts.append({"creator": a["creator"], "platform": a["platform"], "account": a.get("handle") or a.get("url"),
                         "url": p["url"], "posted": p["posted"], "views": p["views"], "likes": p["likes"], "comments": p["comments"],
                         "shares": p["shares"], "saves": p["saves"], "caption": (p.get("caption") or "")[:120], "x_median": round((p["views"] or 0) / med, 1) if med else None})
    rows.append({"creator": a["creator"], "platform": a["platform"], "account": a.get("handle") or a.get("url"), "error": a.get("error"),
                 "followers": a.get("followers"), "posts_scanned": len(ps), "posts_24h": len(last24),
                 "posts_per_day": round(len(ps) / covered_days, 1) if covered_days else 0, "covers_days": round(covered_days, 1) if covered_days else None,
                 "last7_by_day": days, "views_total": sum(views), "views_median": med, "best": max(ps, key=lambda p: p["views"] or 0)["url"] if ps else None,
                 "best_views": max(views) if views else 0, "last_post": max((p["posted"] for p in ps), default=None), "scan_reached_limit": full})

out = {"scanned_at": scan["scanned_at"], "target_per_day": TARGET, "accounts": rows,
       "top_posts": sorted(allposts, key=lambda p: -(p["views"] or 0))[:25],
       "outliers": sorted([p for p in allposts if (p["x_median"] or 0) >= 3 and (p["views"] or 0) >= 1000], key=lambda p: -p["views"])}
json.dump(out, open(sys.argv[1].replace("scan-", "summary-"), "w"), indent=1, ensure_ascii=False)

by = {}
for r in rows: by.setdefault(r["creator"], []).append(r)
for c, rs in by.items():
    print(f"\n{c}")
    for r in rs:
        if r["error"] and not r["posts_scanned"]:
            print(f"  {r['platform']:<9} {str(r['account'])[:34]:<34} ERROR {r['error']}"); continue
        print(f"  {r['platform']:<9} {str(r['account'])[:34]:<34} 24h={r['posts_24h']:>2} /day={r['posts_per_day']:>4} (over {r['covers_days']} d) "
              f"views tot={r['views_total']:>8} med={int(r['views_median']):>6} best={r['best_views']:>7} foll={r['followers']} last={str(r['last_post'])[:16]}")
print("\nTOP 10:")
for p in out["top_posts"][:10]:
    print(f"  {p['views']:>8} {p['creator']:<9} {p['platform']:<9} {p['posted'][:10]} {p['url']}")
