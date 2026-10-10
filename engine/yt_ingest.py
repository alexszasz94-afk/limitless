"""Preia un dataset Apify (streamers/youtube-scraper) și îl salvează ca sursă de studiu.

Folosire: python3 engine/yt_ingest.py <dataset_id> <nume-sursa> [nr_parti]
Scrie library/sources/<nume-sursa>/videos.jsonl (toate videourile, cu transcriere unde există)
și chunks/partN.txt (doar cele cu transcriere, împărțite egal pe cuvinte, pentru agenții care citesc).
"""
import json, os, sys, urllib.request

def main():
    dataset, name = sys.argv[1], sys.argv[2]
    parts = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    url = f"https://api.apify.com/v2/datasets/{dataset}/items?format=json&clean=1&token={os.environ['APIFY_TOKEN']}"
    items = json.load(urllib.request.urlopen(url))
    out = os.path.join(os.path.dirname(__file__), "..", "library", "sources", name)
    os.makedirs(os.path.join(out, "chunks"), exist_ok=True)

    def transcript(x):
        return next((s.get("plaintext") for s in (x.get("subtitles") or []) if s.get("plaintext")), None)

    keys = ("id", "type", "title", "channelName", "date", "viewCount", "likes", "duration", "url")
    rows = [{k: x.get(k) for k in keys} | {"transcript": transcript(x)} for x in items]
    rows.sort(key=lambda r: r["date"] or "", reverse=True)
    with open(os.path.join(out, "videos.jsonl"), "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    with_text = [r for r in rows if r["transcript"]]
    chunks, sizes = [[] for _ in range(parts)], [0] * parts
    for r in sorted(with_text, key=lambda r: -len(r["transcript"])):
        i = sizes.index(min(sizes))
        chunks[i].append(r)
        sizes[i] += len(r["transcript"].split())
    for i, c in enumerate(chunks, 1):
        c.sort(key=lambda r: r["date"] or "", reverse=True)
        with open(os.path.join(out, "chunks", f"part{i}.txt"), "w") as f:
            for r in c:
                f.write(f"=== [{r['type']}] {r['title']} | {r.get('channelName')} | {(r['date'] or '')[:10]} | views {r['viewCount']} | {r['url']}\n{r['transcript']}\n\n")
    print(f"{name}: {len(rows)} videouri, {len(with_text)} cu transcriere, cuvinte pe parte: {sizes}")

if __name__ == "__main__":
    main()
