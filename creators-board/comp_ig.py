"""Competitor research on Instagram (hashtags) - public data, Apify. python3 comp_ig.py -> data/comp/ig-hashtags-<date>.json"""
import json, os, datetime, urllib.request, urllib.parse
T = os.environ["APIFY_TOKEN"]
def run(actor, inp, n):
    q = urllib.parse.urlencode({"token": T, "timeout": 290, "maxItems": n})
    req = urllib.request.Request(f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items?{q}", data=json.dumps(inp).encode(), headers={"Content-Type": "application/json"})
    try: return json.load(urllib.request.urlopen(req, timeout=300))
    except urllib.error.HTTPError as e: print(actor, e.code, e.read()[:200]); return []
TAGS = {"grinch": ["grinchrobe"], "snoopy": ["snoopyrobe"], "princess": ["princessrobe", "disneyrobe"], "stitch": ["stitchrobe"],
        "generic": ["heatedrobe", "wearableblanket", "hoodedblanket", "heatedblanket"]}
out = []
for niche, tags in TAGS.items():
    items = run("apify~instagram-hashtag-scraper", {"hashtags": tags, "resultsType": "reels", "resultsLimit": 25}, 25 * len(tags))
    for it in items:
        if not it.get("url") or it.get("error"): continue
        out.append({"niche": niche, "url": it["url"], "handle": it.get("ownerUsername"), "views": it.get("videoPlayCount") or it.get("videoViewCount") or it.get("igPlayCount"),
                    "likes": it.get("likesCount"), "comments": it.get("commentsCount"), "posted": it.get("timestamp"), "caption": (it.get("caption") or "")[:200],
                    "thumb_src": it.get("displayUrl"), "type": it.get("type"), "hashtags": (it.get("hashtags") or [])[:12]})
    print(niche, len(items), flush=True)
p = f"data/comp/ig-hashtags-{datetime.date.today()}.json"; json.dump(out, open(p, "w"), indent=1, ensure_ascii=False); print(p, len(out))
