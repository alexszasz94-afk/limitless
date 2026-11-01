"""Latest reels of known competitor Instagram accounts (public, Apify instagram-scraper~instagram-profile-reels-scraper)."""
import json, os, sys, datetime, urllib.request, urllib.parse, concurrent.futures as cf
T = os.environ["APIFY_TOKEN"]
H = sys.argv[1].split(","); N = int(sys.argv[2]) if len(sys.argv) > 2 else 12
def run(h):
    q = urllib.parse.urlencode({"token": T, "timeout": 200, "maxItems": N})
    req = urllib.request.Request(f"https://api.apify.com/v2/acts/instagram-scraper~instagram-profile-reels-scraper/run-sync-get-dataset-items?{q}",
                                 data=json.dumps({"instagramUsernames": [h], "postsPerProfile": N}).encode(), headers={"Content-Type": "application/json"})
    try: items = json.load(urllib.request.urlopen(req, timeout=220))
    except Exception as e: return h, [], str(e)[:80]
    out = []
    for it in items:
        m = it.get("metrics") or it; code = it.get("code") or it.get("shortcode")
        v = m.get("ig_play_count") or m.get("play_count")
        if not code or v is None: continue
        cap = it.get("caption"); cap = cap if isinstance(cap, str) else (cap or {}).get("text")
        u = it.get("user") or it.get("owner") or {}
        img = (((it.get("image_versions2") or {}).get("candidates") or [{}])[0]).get("url") or it.get("display_uri") or it.get("thumbnail_url")
        out.append({"url": f"https://www.instagram.com/p/{code}/", "handle": h, "views": int(v), "likes": m.get("like_count"), "comments": m.get("comment_count"),
                    "shares": m.get("share_count"), "saves": m.get("save_count"), "posted": it.get("taken_at"), "caption": (cap or "")[:200],
                    "followers": u.get("follower_count"), "thumb_src": img})
    return h, out, None
res = {}
with cf.ThreadPoolExecutor(2) as ex:
    for h, out, err in ex.map(run, H):
        res[h] = out; print(f"{h:<24} {len(out):>3} {err or ''} best={max([p['views'] for p in out], default=0)}", flush=True)
p = f"data/comp/ig-profiles-{datetime.date.today()}.json"
old = json.load(open(p)) if os.path.exists(p) else {}
old.update(res); json.dump(old, open(p, "w"), indent=1, ensure_ascii=False)
