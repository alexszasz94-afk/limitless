"""Facebook REELS search across robe niches (public, Apify apify~facebook-search-scraper, searchType reels)."""
import json, os, datetime, urllib.request, urllib.parse, concurrent.futures as cf
T = os.environ["APIFY_TOKEN"]
KW = {"Grinch": ["grinch robe", "heated grinch robe"], "Snoopy": ["snoopy robe"], "Princess & Disney": ["princess robe", "disney robe", "pooh robe"],
      "Stitch": ["stitch robe"], "Heated robes (other)": ["heated robe", "wearable blanket hoodie", "giant hooded blanket", "goth robe", "harry potter robe", "hello kitty robe", "bluey robe"]}
def run(kw):
    q = urllib.parse.urlencode({"token": T, "timeout": 280, "maxItems": 40})
    req = urllib.request.Request(f"https://api.apify.com/v2/acts/apify~facebook-search-scraper/run-sync-get-dataset-items?{q}",
                                 data=json.dumps({"categories": [kw], "searchType": "reels", "resultsLimit": 40}).encode(), headers={"Content-Type": "application/json"})
    try: return kw, json.load(urllib.request.urlopen(req, timeout=300))
    except Exception as e: return kw, []
jobs = [(n, k) for n, ks in KW.items() for k in ks]
out = []
with cf.ThreadPoolExecutor(2) as ex:
    for (n, k), (_, items) in zip(jobs, ex.map(lambda j: run(j[1]), jobs)):
        for it in items:
            if it.get("error") or not it.get("url"): continue
            out.append({"niche": n, "kw": k, "url": it["url"], "handle": it.get("authorName"), "author_id": it.get("authorId"), "views": it.get("viewCount"),
                        "likes": it.get("reactionCount"), "shares": it.get("shareCount"), "comments": it.get("commentCount"),
                        "posted": it.get("createdAt"), "caption": (it.get("caption") or "")[:200], "thumb_src": it.get("thumbnailUrl"), "duration_ms": it.get("durationMs")})
        print(k, len(items), flush=True)
p = f"data/comp/fb-reels-{datetime.date.today()}.json"; json.dump(out, open(p, "w"), indent=1, ensure_ascii=False); print(p, len(out))
