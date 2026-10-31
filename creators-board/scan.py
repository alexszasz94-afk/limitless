"""One scan of every creator account (public data, Apify). Field choices = social_tracker/lib/apify/actors.ts (checked live).
  python3 scan.py [posts_per_account]   -> data/scan-<UTC date>.json  (+ prints a summary and the Apify cost)
Never prints the token."""
import json, os, sys, time, datetime, urllib.request, urllib.parse, concurrent.futures as cf

TOKEN = os.environ["APIFY_TOKEN"]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
HERE = os.path.dirname(os.path.abspath(__file__))
ACT = {"tiktok": "clockworks~tiktok-profile-scraper",
       "instagram": "instagram-scraper~instagram-profile-reels-scraper",
       "instagram_alt": "data-slayer~instagram-profile-reels",
       "facebook": "apify~facebook-posts-scraper",
       "ig_post": "data-slayer~instagram-post-details"}
TT = {"shouldDownloadVideos": False, "shouldDownloadCovers": False, "shouldDownloadSubtitles": False, "shouldDownloadSlideshowImages": False}


def run(actor, inp, max_items):
    q = urllib.parse.urlencode({"token": TOKEN, "timeout": 300, "maxItems": max_items, "clean": "true"})
    req = urllib.request.Request(f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items?{q}",
                                 data=json.dumps(inp).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=330) as r:
        return json.load(r)


def num(v):
    try: return int(v)
    except Exception: return None


def iso(v):
    if v is None: return None
    if isinstance(v, (int, float)): return datetime.datetime.utcfromtimestamp(v).isoformat() + "Z"
    return str(v)


def p_tiktok(it):
    if not it.get("id") or not it.get("webVideoUrl"): return None
    return {"url": it["webVideoUrl"], "posted": iso(it.get("createTimeISO") or it.get("createTime")), "caption": it.get("text"),
            "views": num(it.get("playCount")), "likes": num(it.get("diggCount")), "comments": num(it.get("commentCount")),
            "shares": num(it.get("shareCount")), "saves": num(it.get("collectCount")), "duration": (it.get("videoMeta") or {}).get("duration"),
            "followers": num((it.get("authorMeta") or {}).get("fans")), "handle": (it.get("authorMeta") or {}).get("name")}


def p_instagram(it):
    m = it.get("metrics") or it
    code = it.get("code") or it.get("shortcode") or it.get("shortCode")
    views = num(m.get("ig_play_count")) if m.get("ig_play_count") is not None else num(m.get("play_count"))
    if not code or views is None: return None
    cap = it.get("caption"); cap = cap if isinstance(cap, str) else (cap or {}).get("text")
    u = it.get("user") or it.get("owner") or {}
    return {"url": f"https://www.instagram.com/p/{code}/", "posted": iso(it.get("taken_at") or it.get("taken_at_timestamp") or it.get("timestamp")),
            "caption": cap, "views": views, "likes": num(m.get("like_count")), "comments": num(m.get("comment_count")),
            "shares": num(m.get("share_count") or m.get("reshare_count")), "saves": num(m.get("save_count")),
            "duration": it.get("video_duration"), "followers": num(u.get("follower_count")), "handle": u.get("username")}


def p_facebook(it):
    if it.get("error"): return None
    views = num(it.get("viewsCount"))
    media = it.get("media") or []
    is_video = it.get("isVideo") is True or views is not None or any((x or {}).get("__typename") == "Video" for x in media)
    if not is_video or views is None or not (it.get("url") or it.get("topLevelUrl")): return None
    return {"url": it.get("url") or it.get("topLevelUrl"), "posted": iso(it.get("time") or it.get("timestamp")), "caption": it.get("text"),
            "views": views, "likes": num(it.get("likes") or it.get("topReactionsCount")), "comments": num(it.get("comments")),
            "shares": num(it.get("shares")), "saves": None, "followers": None,
            "handle": it.get("pageName") or (it.get("user") or {}).get("name"), "page_url": (it.get("user") or {}).get("profileUrl") or it.get("facebookUrl")}


def scan(creator, acc):
    pf = acc["platform"]
    out = {"creator": creator, **acc, "posts": [], "error": None}
    try:
        if acc.get("resolve"):
            if pf == "facebook":
                items = run(ACT["facebook"], {"startUrls": [{"url": acc["resolve"]}], "resultsLimit": 1}, 3)
                page = next((p.get("page_url") or p.get("handle") for p in map(p_facebook, items) if p), None)
                fb = next((i for i in items if not i.get("error")), {})
                page = (fb.get("user") or {}).get("profileUrl") or fb.get("facebookUrl") or page
                if not page: out["error"] = "could not find the page of the reel"; return out
                out["url"] = page
            else:
                items = run(ACT["ig_post"], {"postUrls": [acc["resolve"]]}, 2)
                h = next(((i.get("owner") or i.get("user") or {}).get("username") or i.get("ownerUsername") for i in items if isinstance(i, dict)), None)
                if not h: out["error"] = "could not find the owner of the reel"; return out
                out["handle"] = h
        if pf == "tiktok":
            items = run(ACT["tiktok"], {"profiles": [out["handle"]], "resultsPerPage": N, "profileScrapeSections": ["videos"], "profileSorting": "latest", **TT}, N)
            parse = p_tiktok
            prof = next((i.get("authorMeta") for i in items if i.get("authorMeta")), None) or {}
            out["followers"] = num(prof.get("fans"))
        elif pf == "instagram":
            items = run(ACT["instagram"], {"instagramUsernames": [out["handle"]], "postsPerProfile": max(5, N)}, N)
            if not [i for i in items if p_instagram(i)]:
                items = run(ACT["instagram_alt"], {"username": out["handle"], "maxResults": max(5, N)}, N)
            parse = p_instagram
        else:
            items = run(ACT["facebook"], {"startUrls": [{"url": out["url"]}], "resultsLimit": N}, N + 5)
            parse = p_facebook
        out["posts"] = [p for p in map(parse, items) if p]
        if pf == "instagram":
            out["followers"] = next((p["followers"] for p in out["posts"] if p.get("followers")), None)
        if not out["posts"]:
            out["error"] = "no videos found" + (f" ({items[0].get('error') or items[0].get('note')})" if items and isinstance(items[0], dict) and (items[0].get('error') or items[0].get('note')) else "")
    except Exception as e:
        out["error"] = f"{type(e).__name__}: {str(e)[:150]}"
    return out


def usage():
    with urllib.request.urlopen(f"https://api.apify.com/v2/users/me/limits?token={TOKEN}") as r:
        d = json.load(r)["data"]
    return d["current"]["monthlyUsageUsd"], d["limits"]["maxMonthlyUsageUsd"]


if __name__ == "__main__":
    cfg = json.load(open(os.path.join(HERE, "accounts.json")))
    jobs = [(c["name"], a) for c in cfg["creators"] for a in c["accounts"]]
    u0, lim = usage(); print(f"Apify before: {u0:.2f} of {lim} USD")
    with cf.ThreadPoolExecutor(5) as ex:
        res = list(ex.map(lambda j: scan(*j), jobs))
    u1, _ = usage()
    now = datetime.datetime.utcnow()
    path = os.path.join(HERE, "data", f"scan-{now:%Y-%m-%d}.json")
    json.dump({"scanned_at": now.isoformat() + "Z", "posts_per_account": N, "apify_cost_usd": round(u1 - u0, 3), "accounts": res}, open(path, "w"), indent=1, ensure_ascii=False)
    for r in res:
        print(f"{r['creator']:<9} {r['platform']:<9} {(r.get('handle') or r.get('url') or '')[:45]:<45} posts={len(r['posts']):>3} {r['error'] or ''}")
    print(f"Apify cost of this scan: {u1 - u0:.2f} USD -> {path}")
