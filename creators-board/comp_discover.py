"""Competitor discovery v1: TikTok hashtag search across robe niches (public data, Apify clockworks~tiktok-scraper).
  python3 comp_discover.py [results_per_hashtag] -> data/comp/tiktok-hashtags-<date>.json"""
import json, os, sys, datetime, urllib.request, urllib.parse
T = os.environ["APIFY_TOKEN"]; N = int(sys.argv[1]) if len(sys.argv) > 1 else 25
TAGS = {"grinch": ["grinchrobe", "grinchblanket"], "snoopy": ["snoopyrobe", "snoopyblanket"], "princess": ["princessrobe", "disneyrobe"],
        "stitch": ["stitchrobe"], "generic": ["heatedrobe", "wearableblanket", "hoodedblanket", "giantrobe"]}
out = []
for niche, tags in TAGS.items():
    q = urllib.parse.urlencode({"token": T, "timeout": 280, "maxItems": N * len(tags)})
    inp = {"hashtags": tags, "resultsPerPage": N, "shouldDownloadVideos": False, "shouldDownloadCovers": False, "shouldDownloadSubtitles": False, "shouldDownloadSlideshowImages": False}
    req = urllib.request.Request(f"https://api.apify.com/v2/acts/clockworks~tiktok-scraper/run-sync-get-dataset-items?{q}", data=json.dumps(inp).encode(), headers={"Content-Type": "application/json"})
    try:
        items = json.load(urllib.request.urlopen(req, timeout=300))
    except Exception as e:
        print(niche, "ERR", e); continue
    for it in items:
        if not it.get("webVideoUrl"): continue
        am = it.get("authorMeta") or {}; vm = it.get("videoMeta") or {}
        out.append({"niche": niche, "url": it["webVideoUrl"], "handle": am.get("name"), "followers": am.get("fans"), "views": it.get("playCount"),
                    "likes": it.get("diggCount"), "shares": it.get("shareCount"), "saves": it.get("collectCount"), "comments": it.get("commentCount"),
                    "posted": it.get("createTimeISO"), "caption": (it.get("text") or "")[:200], "duration": vm.get("duration"), "cover": vm.get("coverUrl"),
                    "hashtags": [h.get("name") for h in (it.get("hashtags") or [])][:12]})
    print(niche, len(items), flush=True)
p = f"data/comp/tiktok-hashtags-{datetime.date.today()}.json"
json.dump(out, open(p, "w"), indent=1, ensure_ascii=False); print(p, len(out))
