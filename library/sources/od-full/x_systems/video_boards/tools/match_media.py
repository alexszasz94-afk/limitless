#!/usr/bin/env python3
"""Match a product's files to the Higgsfield jobs that made them (audits and recovery).

You only need this when the link between a file and its Higgsfield job was lost -
new generations are recorded at the moment they are downloaded (WORKFLOWS.md §3).

    python3 x_systems/video_boards/tools/match_media.py PRODUCT HF_DIR OUT_DIR [--md5] [--media]

  PRODUCT  substring of the product folder, e.g. LED
  HF_DIR   folder of saved Higgsfield history pages: each file is the JSON that
           show_generations returns ({"items": [...], "next_cursor": ...}),
           videos and images both, as many pages as needed to cover the dates
  OUT_DIR  where the results go (use a scratch folder, not the product folder)
  --md5    also download every matched clip and compare md5 (slow, proves identity)
  --media  also resolve every attachment (media id) of the matched jobs to a local
           file: generated jobs through the matches, uploads by exact byte size,
           else by look (needs Pillow + numpy; a 40x72 grey thumbnail, mean
           difference <= 0.10 counts as the same picture)

Writes OUT_DIR/matches.json   {"relative/path": {"job": id, "type": ..., "model": ..., "md5": true|false|null}}
       OUT_DIR/media.json     {"media id": {"files": [...], "how": "job|bytes|look|none"}}   (--media)
       OUT_DIR/report.txt     what matched, what did not
A file matches a job when its byte size equals the job's result size and exactly
one job has that size. Clips that are re-encoded copies will not match - say so
on the card instead of guessing.
"""
import concurrent.futures as cf, glob, hashlib, io, json, os, sys, urllib.request

sys.dont_write_bytecode = True
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(KIT))
MEDIA_EXT = ('.png', '.jpg', '.jpeg', '.webp', '.mp4', '.mov')


def load_history(d):
    items = {}
    for p in sorted(glob.glob(os.path.join(d, '*'))):
        try:
            j = json.load(open(p, encoding='utf-8'))
        except (ValueError, OSError):
            continue
        for x in (j.get('items') if isinstance(j, dict) else j) or []:
            items[x['id']] = x
    return items


def result_url(x):
    r = x.get('results')
    r = r if isinstance(r, dict) else (r[0] if r else {})
    return r.get('rawUrl')


def head_size(u):
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=30) as r:
                return int(r.headers.get('Content-Length', -1))
        except Exception:
            pass
    return -1


def md5_url(u):
    for _ in range(3):
        try:
            h = hashlib.md5()
            with urllib.request.urlopen(u, timeout=120) as r:
                for ch in iter(lambda: r.read(1 << 20), b''):
                    h.update(ch)
            return h.hexdigest()
        except Exception:
            pass
    return None


def md5_file(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for ch in iter(lambda: f.read(1 << 20), b''):
            h.update(ch)
    return h.hexdigest()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 3:
        print(__doc__)
        return 1
    want, hf_dir, out = args
    ps = [d for d in sorted(os.listdir(ROOT)) if ' - ' in d and want.upper() == d.upper()] or \
         [d for d in sorted(os.listdir(ROOT)) if ' - ' in d and want.upper() in d.upper()]
    if len(ps) != 1:
        print('need exactly one product, matched ' + str(ps))
        return 1
    prod = ps[0]
    base = os.path.join(ROOT, prod)
    os.makedirs(out, exist_ok=True)
    H = load_history(hf_dir)
    print(f'{len(H)} Higgsfield jobs loaded')
    cache_p = os.path.join(out, 'sizes.json')
    sizes = json.load(open(cache_p)) if os.path.exists(cache_p) else {}
    todo = [(j, result_url(x)) for j, x in H.items() if j not in sizes and result_url(x)]
    with cf.ThreadPoolExecutor(24) as ex:
        for (j, u), s in zip(todo, ex.map(lambda t: head_size(t[1]), todo)):
            sizes[j] = s
    json.dump(sizes, open(cache_p, 'w'))
    by_size = {}
    for j, s in sizes.items():
        by_size.setdefault(s, []).append(j)
    local = {}
    for d, ds, fs in os.walk(base):
        ds[:] = [x for x in ds if x != '_board_thumbs']
        for f in fs:
            if f.lower().endswith(MEDIA_EXT):
                p = os.path.join(d, f)
                local[os.path.relpath(p, base).replace(os.sep, '/')] = os.path.getsize(p)
    M, rep = {}, []
    for rel, s in sorted(local.items()):
        c = by_size.get(s, [])
        if len(c) == 1:
            x = H[c[0]]
            M[rel] = {'job': c[0], 'type': x['type'], 'model': x['model'], 'md5': None}
        elif len(c) > 1:
            rep.append(f'AMBIGUOUS {rel}: {len(c)} jobs share its size')
    if '--md5' in sys.argv:
        clips = [r for r in M if r.endswith(('.mp4', '.mov'))]
        with cf.ThreadPoolExecutor(16) as ex:
            for r, h in zip(clips, ex.map(lambda r: md5_url(result_url(H[M[r]['job']])), clips)):
                M[r]['md5'] = (h == md5_file(os.path.join(base, r))) if h else None
    json.dump(M, open(os.path.join(out, 'matches.json'), 'w'), indent=1)
    un = [r for r in local if r not in M]
    rep.insert(0, f'{prod}: {len(M)} of {len(local)} media files matched to a Higgsfield job')
    rep += [f'no match  {r}' for r in sorted(un)]
    if '--media' in sys.argv:
        rep += resolve_media(H, M, base, local, out)
    open(os.path.join(out, 'report.txt'), 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
    print(rep[0])
    print(f'details: {os.path.join(out, "report.txt")}')
    return 0


def resolve_media(H, M, base, local, out):
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        return ['--media needs Pillow and numpy']
    job2files = {}
    for r, m in M.items():
        job2files.setdefault(m['job'], []).append(r)
    by_size = {}
    for r, s in local.items():
        by_size.setdefault(s, []).append(r)
    sig = {}
    for r in local:
        if r.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            try:
                im = Image.open(os.path.join(base, r))
                im.draft('L', (80, 144))
                sig[r] = np.asarray(im.convert('L').resize((40, 72)), dtype=np.float32) / 255
            except Exception:
                pass
    keys = list(sig)
    arr = np.stack([sig[k] for k in keys]) if keys else None
    need = {}
    for j in {m['job'] for m in M.values()}:
        for m in H[j]['params'].get('medias') or []:
            need[m['data']['id']] = m['data']

    def one(d):
        mid, typ, url = d['id'], d.get('type'), d.get('url')
        if typ in ('image_job', 'video_job'):
            fs = job2files.get(mid, [])
            return mid, {'files': fs, 'how': 'job' if fs else 'none'}
        s = head_size(url)
        if by_size.get(s):
            return mid, {'files': by_size[s], 'how': 'bytes'}
        if typ == 'video_input' or arr is None:
            return mid, {'files': [], 'how': 'none'}
        try:
            b = urllib.request.urlopen(url, timeout=60).read()
            a = np.asarray(Image.open(io.BytesIO(b)).convert('L').resize((40, 72)), dtype=np.float32) / 255
            dif = np.abs(arr - a).mean(axis=(1, 2))
            o = np.argsort(dif)[:3]
            ok = [keys[i] for i in o if dif[i] <= 0.10 and dif[i] <= dif[o[0]] + 0.005]
            return mid, {'files': ok, 'how': 'look' if ok else 'none', 'best': [[keys[i], round(float(dif[i]), 4)] for i in o]}
        except Exception as e:
            return mid, {'files': [], 'how': 'none', 'error': str(e)}

    res = {}
    with cf.ThreadPoolExecutor(16) as ex:
        for mid, r in ex.map(one, need.values()):
            res[mid] = r
    json.dump(res, open(os.path.join(out, 'media.json'), 'w'), indent=1)
    n = sum(1 for r in res.values() if r['files'])
    return [f'attachments: {n} of {len(res)} resolved to a local file (media.json)']


if __name__ == '__main__':
    sys.exit(main())
