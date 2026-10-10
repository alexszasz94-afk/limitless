#!/usr/bin/env python3
"""Product Finder - the one permanent build path for x_systems/product_finder/.

    python3 x_systems/video_boards/tools/product_finder.py check        # validate everything, write nothing
    python3 x_systems/video_boards/tools/product_finder.py rank         # recompute derived fields -> board_data.json
    python3 x_systems/video_boards/tools/product_finder.py links        # rewrite links.txt from the batches
    python3 x_systems/video_boards/tools/product_finder.py build        # rebuild product_board.html
    python3 x_systems/video_boards/tools/product_finder.py all          # rank + links + build, then check
    python3 x_systems/video_boards/tools/product_finder.py triage FILE  # classify submitted links against the board
    python3 x_systems/video_boards/tools/product_finder.py apify-balance [--json]
    python3 x_systems/video_boards/tools/product_finder.py apify-run ACTOR INPUT.json LABEL [--max-usd 1.0] [--wait 150]
    python3 x_systems/video_boards/tools/product_finder.py apify-fetch LABEL [--wait 150]

Source of truth : x_systems/product_finder/board_data.json (UTF-8, indent 2, no trailing newline)
Generated       : product_board.html = template + favicon + data  (never edit by hand)
                  links.txt          = one dated section per batch (CRLF)  (never edit by hand)
Template        : x_systems/video_boards/template/product_finder.html + product_finder_favicon.txt
Apify keys      : every apify_api_ token in keys.txt at the drive root - read here, never printed
Evidence        : x_systems/product_finder/raw/research/<label>_run.json / _status.json / _items.json
Removals        : raw/research/audit_removal_2026_09_30.json, update_oct01_manual_review.json and
                  raw/research/removals.json (list of {key, removedAt, request}) - never restored

"rank" recomputes only derived fields: performance score/rank, worstPerformingAccounts,
audit.rankingEligible, audit.excludedAccounts, sourceCount, playableCount. Ranking: equal-weight
midrank percentiles of followers and current-run average views, 100*(L+(E-1)/2)/(N-1), averaged;
exact fractions, ties broken by account key; lower = weaker.

The procedure that uses this tool is the product-finder-import skill (Daniel's Claude account).
Standard library only. Exit 0 = ok, 1 = errors found or command failed, 2 = usage.
"""
import concurrent.futures, copy, datetime, hashlib, json, os, re, sys, time
import urllib.error, urllib.parse, urllib.request
from fractions import Fraction

sys.dont_write_bytecode = True
TOOLS = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(TOOLS)                                   # x_systems/video_boards
ROOT = os.path.dirname(os.path.dirname(KIT))                   # the drive
PF = os.path.join(ROOT, 'x_systems', 'product_finder')
DATA = os.path.join(PF, 'board_data.json')
HTML = os.path.join(PF, 'product_board.html')
LINKS = os.path.join(PF, 'links.txt')
RESEARCH = os.path.join(PF, 'raw', 'research')
TPL = os.path.join(KIT, 'template', 'product_finder.html')
FAV = os.path.join(KIT, 'template', 'product_finder_favicon.txt')
KEYS = os.path.join(ROOT, 'keys.txt')
API = 'https://api.apify.com/v2'
WORST_N = 50
PREFIX = {'Instagram': 'ig', 'TikTok': 'tt', 'Facebook': 'fb'}
REMOVAL_FILES = ('audit_removal_2026_09_30.json', 'update_oct01_manual_review.json', 'removals.json')

sys.path.insert(0, TOOLS)
from build_board import BoardError, write_verified   # exclusive <file>.building write + read-back


def md5(b):
    return hashlib.md5(b).hexdigest()


def read_bytes(p):
    with open(p, 'rb') as f:
        return f.read()


def read_text(p):
    return read_bytes(p).decode('utf-8')


# ---------------------------------------------------------------- data in / out

def load():
    raw = read_bytes(DATA)
    return json.loads(raw.decode('utf-8')), md5(raw)


def dump(D):
    return json.dumps(D, ensure_ascii=False, indent=2)


def save(D, seen):
    """write board_data.json only if it is still the version that was read"""
    if md5(read_bytes(DATA)) != seen:
        raise BoardError('board_data.json changed since this command read it (another session?) - '
                         'nothing written. Run the command again.')
    return write_verified(DATA, dump(D))


def write_if_changed(path, text, name):
    if os.path.exists(path) and read_bytes(path) == text.encode('utf-8'):
        print(f'{name}: unchanged')
        return False
    h = write_verified(path, text)
    print(f'{name}: written, {len(text.encode("utf-8"))} bytes, md5 {h}')
    return True


# ---------------------------------------------------------------- derived fields

def ranking(D):
    """[(score Fraction, key, account)] for eligible accounts, weakest first"""
    el = [a for a in D['accounts'] if (a.get('performance') or {}).get('eligible')]
    for a in el:
        p = a['performance']
        if not isinstance(p.get('followers'), int) or not isinstance(p.get('averageViews'), (int, float)):
            raise BoardError(f'{a["key"]}: eligible but followers/averageViews missing - '
                             'fix the data or mark it ineligible with an excludedReason')
    n = len(el)

    def pct(field):
        vals = [Fraction(a['performance'][field]) for a in el]
        out = []
        for v in vals:
            lo = sum(x < v for x in vals)
            eq = sum(x == v for x in vals)
            out.append(Fraction(50) if n == 1 else Fraction(100) * (2 * lo + eq - 1) / (2 * (n - 1)))
        return out

    pf, pv = pct('followers'), pct('averageViews')
    rows = [((f + v) / 2, a['key'], a) for f, v, a in zip(pf, pv, el)]
    rows.sort(key=lambda r: (r[0], r[1]))
    return rows


def derive(D):
    """recompute every derived field in place"""
    A = D['accounts']
    rows = ranking(D)
    for i, (s, k, a) in enumerate(rows, 1):
        a['performance']['score'] = float(s)
        a['performance']['rank'] = i
    ranked = {k for _, k, _ in rows}
    for a in A:
        if a['key'] not in ranked and a.get('performance') is not None:
            for f in ('score', 'rank'):                 # clear, but never add keys an account does not have
                if f in a['performance']:
                    a['performance'][f] = None
    D['worstPerformingAccounts'] = [
        {'key': k, 'rank': i, 'score': float(s), 'followers': a['performance']['followers'],
         'averageViews': a['performance']['averageViews'], 'sampleCount': a['performance']['sampleCount'],
         'viewsApproximate': a['performance']['viewsApproximate'],
         'smallSample': a['performance']['smallSample']}
        for i, (s, k, a) in enumerate(rows[:WORST_N], 1)]
    D['audit']['rankingEligible'] = len(rows)
    D['audit']['excludedAccounts'] = [
        {'key': a['key'], 'reason': (a.get('performance') or {}).get('excludedReason') or ''}
        for a in A if a['key'] not in ranked]
    D['sourceCount'] = len(A)
    D['playableCount'] = sum(1 for a in A if a.get('media'))
    return D


def links_text(D):
    acc = {a['key']: a for a in D['accounts']}
    parts = []
    for b in sorted(D['batches'], key=lambda b: b['number']):
        day = datetime.date.fromisoformat(b['addedAt']).strftime('%d.%m.%Y')
        n = len(b['accountKeys'])
        parts.append(f'Batch {b["number"]}: {day} | {n} account{"" if n == 1 else "s"}\r\n\r\n'
                     + ''.join(acc[k]['sourceUrl'] + '\r\n' for k in b['accountKeys']))
    return '\r\n'.join(parts)


def page(D):
    tpl = read_text(TPL).replace('\r\n', '\n')          # the template may be saved with CRLF; the board is LF
    fav = read_text(FAV).strip()
    if tpl.count('__DATA__') != 1:
        raise BoardError('template/product_finder.html must contain __DATA__ exactly once')
    pre, post = tpl.split('__DATA__')
    data = json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return pre.replace('__FAVICON__', fav) + data + post.replace('__FAVICON__', fav)


# ---------------------------------------------------------------- links

def parse_url(u):
    """-> dict(kind, platform, key|None, code|None, url). kind: profile, video, unresolved, other"""
    u = u.strip().rstrip('.,;)')
    if not re.match(r'https?://', u):
        u = 'https://' + u
    p = urllib.parse.urlsplit(u)
    host = p.netloc.lower().split(':')[0]
    host = host[4:] if host.startswith('www.') else host
    host = host[2:] if host.startswith('m.') else host
    seg = [s for s in p.path.split('/') if s]
    q = urllib.parse.parse_qs(p.query)
    out = {'url': urllib.parse.urlunsplit(('https', host, '/' + '/'.join(seg) + ('/' if seg else ''), '', '')),
           'kind': 'other', 'platform': None, 'key': None, 'code': None}
    if host in ('instagram.com', 'instagr.am'):
        out['platform'] = 'Instagram'
        bare = {'p', 'reel', 'reels', 'tv', 'share', 'stories', 'explore', 'accounts', 's'}
        if seg and seg[0].lower() not in bare:
            h = seg[0].lower()
            out['key'] = 'ig:' + h
            if len(seg) >= 3 and seg[1] in ('reel', 'p', 'tv', 'reels'):
                out.update(kind='video', code=seg[2])
            else:
                out.update(kind='profile', url=f'https://www.instagram.com/{h}/')
        elif len(seg) >= 2 and seg[0] in ('p', 'reel', 'reels', 'tv'):
            out.update(kind='unresolved', code=seg[1])
        else:
            out['kind'] = 'unresolved'
    elif host.endswith('tiktok.com'):
        out['platform'] = 'TikTok'
        if seg and seg[0].startswith('@'):
            h = seg[0][1:].lower()
            out['key'] = 'tt:' + h
            if len(seg) >= 3 and seg[1] == 'video':
                out.update(kind='video', code=seg[2])
            else:
                out.update(kind='profile', url=f'https://www.tiktok.com/@{h}')
        else:
            out['kind'] = 'unresolved'                     # vm./vt. short links, /t/ links
    elif host in ('facebook.com', 'fb.com', 'fb.watch'):
        out['platform'] = 'Facebook'
        if seg[:1] == ['profile.php'] and q.get('id'):
            i = q['id'][0]
            out.update(kind='profile', key='fb:' + i, url=f'https://www.facebook.com/profile.php?id={i}')
        elif len(seg) == 1 and seg[0] not in ('share', 'watch', 'reel', 'reels', 'videos', 'groups'):
            out.update(kind='profile', url=f'https://www.facebook.com/{seg[0]}')   # vanity name, id unknown
        else:
            out['kind'] = 'unresolved'
    return out


def removed_keys():
    out = {}
    for name in REMOVAL_FILES:
        p = os.path.join(RESEARCH, name)
        if not os.path.exists(p):
            if name != 'removals.json':
                raise BoardError(f'removal record missing: raw/research/{name}')
            continue
        r = json.loads(read_text(p))
        if name == 'audit_removal_2026_09_30.json':
            for k in r.get('removedKeysInOriginalRankOrder', []):
                out[k] = '2026-09-30'
            for x in r.get('additionalRemovals', []):
                for k in x.get('removedKeys', []):
                    out[k] = '2026-09-30'
        elif name == 'update_oct01_manual_review.json':
            for k in r.get('removedKeys', []):
                out[k] = '2026-10-01'
        else:
            for x in r:
                out[x['key']] = x.get('removedAt', '?')
    return out


def resolved_reels():
    """shared-video code -> account key, from every earlier resolution on record:
    raw/reel_owner_map.txt (CODE=handle lines, Instagram) and sharedReelResolution in the
    raw/research/update_*_review.json files. New resolutions get appended to reel_owner_map.txt."""
    out = {}
    p = os.path.join(PF, 'raw', 'reel_owner_map.txt')
    if os.path.exists(p):
        for line in read_text(p).splitlines():
            code, _, h = line.strip().partition('=')
            if code and h and h != 'ERR':
                out[code] = h if ':' in h else 'ig:' + h.lower()
    for f in sorted(os.listdir(RESEARCH)):
        if f.startswith('update_') and f.endswith('_review.json'):
            try:
                r = json.loads(read_text(os.path.join(RESEARCH, f)))
            except Exception:
                continue
            m = (r.get('sharedReelResolution') if isinstance(r, dict) else None) or {}
            if 'url' in m and 'account' in m:                       # 2026-10-02 shape: one resolution
                m = {parse_url(m['url'])['code']: m['account']}
            for code, h in m.items():
                if code and isinstance(h, str):
                    out[code] = h if ':' in h else 'ig:' + h.lower()
        elif f.endswith('_run.json'):                                # Apify runs fed with video URLs
            try:
                run = json.loads(read_text(os.path.join(RESEARCH, f)))
                inp = run.get('input') or {}
                urls = [u for k in ('username', 'directUrls', 'postUrls') for u in (inp.get(k) or [])
                        if isinstance(u, str)]
                if not any(('/reel/' in u or '/p/' in u) for u in urls):
                    continue
                items_path = os.path.join(RESEARCH, f[:-len('_run.json')] + '_items.json')
                if not os.path.exists(items_path) or os.path.getsize(items_path) > 50_000_000:
                    continue
                for it in json.loads(read_text(items_path)):
                    if isinstance(it, dict) and it.get('shortCode') and it.get('ownerUsername'):
                        out.setdefault(it['shortCode'], 'ig:' + it['ownerUsername'].lower())
            except Exception:
                continue
    return out


def triage(D, text):
    """classify every URL in text: present / removed / new / needs_resolution / other"""
    acc = {a['key']: a for a in D['accounts']}
    by_url = {parse_url(a['sourceUrl'])['url'].lower(): a['key'] for a in D['accounts']}
    vid = {}
    for a in D['accounts']:
        for i in ((a.get('latestRun') or {}).get('videoIds') or []) + [((a.get('video') or {}).get('id'))]:
            if i:
                vid[str(i)] = a['key']
    vid.update(resolved_reels())
    gone = removed_keys()
    seen, rows = set(), []
    for u in re.findall(r'(?:https?://)?(?:www\.|m\.|vm\.|vt\.)?(?:instagram\.com|instagr\.am|tiktok\.com|'
                        r'facebook\.com|fb\.com|fb\.watch)/[^\s<>"\']*', text):
        r = parse_url(u)
        if r['url'] in seen:
            continue
        seen.add(r['url'])
        key = r['key'] or by_url.get(r['url'].lower()) or (vid.get(r['code']) if r['code'] else None)
        if key in gone:
            st = f'removed {gone[key]}'
        elif key in acc:
            st = 'present'
        elif key:
            st = 'new'
        elif r['kind'] in ('unresolved', 'profile'):
            st = 'needs_resolution'
        else:
            st = 'other'
        rows.append({**r, 'key': key, 'status': st})
    return rows


# ---------------------------------------------------------------- check

def check(D):
    errs = []
    E = errs.append
    A = D['accounts']
    acc = {}
    for a in A:
        k = a.get('key')
        if k in acc:
            E(f'duplicate account key {k}')
        acc[k] = a
        if PREFIX.get(a.get('platform')) != (k or '').split(':')[0]:
            E(f'{k}: key prefix does not match platform {a.get("platform")}')
    urls = [parse_url(a['sourceUrl'])['url'].lower() for a in A]
    for u in {u for u in urls if urls.count(u) > 1}:
        E(f'two accounts share the source URL {u}')

    try:
        gone = removed_keys()
        restored = set(D['audit'].get('restoredByDaniel', []))
        for k in acc:
            if k in gone and k not in restored:
                E(f'{k} was removed by Daniel on {gone[k]} and is back on the board')
    except BoardError as e:
        E(str(e))

    # batches
    B = sorted(D.get('batches', []), key=lambda b: b['number'])
    where = {}
    prev = None
    for i, b in enumerate(B, 1):
        if b['number'] != i or b.get('id') != f'batch-{i}':
            E(f'batch numbering broken at {b.get("id")} (expected batch-{i})')
        try:
            d = datetime.date.fromisoformat(b['addedAt'])
            if prev and d < prev:
                E(f'batch {i} is dated before batch {i - 1}')
            prev = d
        except Exception:
            E(f'batch {i}: addedAt {b.get("addedAt")!r} is not YYYY-MM-DD')
        if not b['accountKeys']:
            E(f'batch {i} is empty')
        for k in b['accountKeys']:
            if k in where:
                E(f'{k} is in batch {where[k]} and batch {i}')
            where[k] = i
            if k not in acc:
                E(f'batch {i} lists {k}, which is not on the board')
    for k in acc:
        if k not in where:
            E(f'{k} is in no batch')
    try:
        if read_bytes(LINKS) != links_text(D).encode('utf-8'):
            E('links.txt does not match the batches - run: product_finder.py links')
    except Exception as e:
        E(f'links.txt: {e}')

    # tree
    fam = {f['id']: f for f in D['families']}
    br = {b['id']: b['title'] for b in D['branches']}
    pids = [p['id'] for p in D['products']]
    if len(set(pids)) != len(pids):
        E('duplicate product ids')
    if set(pids) != set(fam):
        E(f'families and products differ: {sorted(set(pids) ^ set(fam))}')
    titles = [p['title'] for p in D['products']]
    for name in {x for x in titles if titles.count(x) > 1}:
        E(f'two products are both called {name!r}')
    mem = {}
    for p in D['products']:
        if p.get('branch') not in br:
            E(f'product {p["id"]}: unknown branch {p.get("branch")}')
        if p.get('title') != fam.get(p['id'], {}).get('title') or \
                fam.get(p['id'], {}).get('group') != br.get(p.get('branch')):
            E(f'product {p["id"]}: title or group disagrees with families/branches')
        if not p['variations']:
            E(f'product {p["id"]} has no variations')
        vt = [v['title'] for v in p['variations']]
        for name in {x for x in vt if vt.count(x) > 1}:
            E(f'product {p["id"]}: two variations are both called {name!r}')
        for v in p['variations']:
            if not v['accounts']:
                E(f'product {p["id"]} / {v["title"]}: empty variation')
            for k in v['accounts']:
                if k in mem:
                    E(f'{k} sits under two products/variations')
                mem[k] = (p, v)
                a = acc.get(k)
                if not a:
                    E(f'product {p["id"]} lists {k}, which is not on the board')
                    continue
                f = fam.get(p['id'], {})
                if (a.get('treeProduct'), a.get('family'), a.get('treeVariant'), a.get('variant'), a.get('branch')) != \
                        (p['id'], p['id'], v['title'], v['title'], p['branch']):
                    E(f'{k}: treeProduct/family/variant/treeVariant/branch disagree with its place in products')
                if (a.get('latestRun') or {}).get('product') != v['title']:
                    E(f'{k}: latestRun.product disagrees with its variation')
                if (a.get('treeProductTitle'), a.get('familyTitle'), a.get('group')) != \
                        (f.get('title'), f.get('title'), f.get('group')) or br.get(a.get('branch')) != a.get('group'):
                    E(f'{k}: product title / group fields disagree with families/branches')
    for k in acc:
        if k not in mem:
            E(f'{k} is under no product/variation')

    # one tree, no content sections (Daniel 2026-10-05); run, media, performance
    for f in ('contentSections', 'ugcPolicy'):
        if f in D:
            E(f'{f} is back in board_data.json - the board has one tree since 2026-10-05')
    media_seen = {}
    for k, a in acc.items():
        for f in ('contentSection', 'ugcReview'):
            if f in a:
                E(f'{k}: {f} is back - the board has one tree since 2026-10-05')
        run = a.get('latestRun') or {}
        if run.get('status') not in ('current', 'review'):
            E(f'{k}: latestRun.status {run.get("status")!r} (expected current or review)')
        vid = (a.get('video') or {}).get('id')
        if run.get('status') == 'current' and vid not in (run.get('videoIds') or []):
            E(f'{k}: featured video {vid} is not in its latest product run')
        if a.get('media'):
            for f in ('media', 'poster'):
                if not a.get(f) or not os.path.isfile(os.path.join(PF, a[f])):
                    E(f'{k}: {f} {a.get(f)!r} does not exist')
            if a['media'] in media_seen:
                E(f'{k} and {media_seen[a["media"]]} use the same media file')
            media_seen[a['media']] = k
        elif not a.get('availability'):
            E(f'{k}: no media and no availability note')
        p = a.get('performance') or {}
        if p.get('eligible'):
            ids = p.get('videoIds') or []
            if run.get('status') != 'current':
                E(f'{k}: ranked although its product run is under review')
            if p.get('followers') != a.get('followers'):
                E(f'{k}: performance.followers differs from followers')
            if p.get('sampleCount') != len(ids) or not 1 <= len(ids) <= 20:
                E(f'{k}: sampleCount {p.get("sampleCount")} vs {len(ids)} video ids (must be 1-20)')
            if not set(ids) <= set(run.get('videoIds') or []):
                E(f'{k}: ranking sample contains videos outside the latest product run')
            if p.get('smallSample') != (len(ids) < 20):
                E(f'{k}: smallSample flag wrong')
        elif not p.get('excludedReason'):
            E(f'{k}: not ranked and no excludedReason')

    # derived fields and outputs
    try:
        if dump(derive(copy.deepcopy(D))) != dump(D):
            E('derived fields (ranking, worst 50, counts) are stale - run: product_finder.py rank')
    except BoardError as e:
        E(str(e))
    try:
        if read_bytes(HTML) != page(D).encode('utf-8'):
            E('product_board.html is not built from the current data - run: product_finder.py build')
    except Exception as e:
        E(f'product_board.html: {e}')
    for f in os.listdir(PF):
        if f.endswith('.building'):
            E(f'leftover {f} (interrupted run) - move it to to_delete/ and rerun')
    return errs


# ---------------------------------------------------------------- Apify

class ApifyError(Exception):
    pass


def apify_keys():
    """every apify_api_ token in keys.txt, in file order (index = position, used as key_index)"""
    if not os.path.exists(KEYS):
        raise BoardError('keys.txt not found at the drive root')
    out = []
    for k in re.findall(r'apify_api_[A-Za-z0-9]+', read_text(KEYS)):
        if k not in out:
            out.append(k)
    if not out:
        raise BoardError('no apify_api_ keys in keys.txt')
    return out


def api(method, path, key, body=None, timeout=60):
    data = None if body is None else json.dumps(body).encode('utf-8')
    req = urllib.request.Request(API + path, data=data, method=method,
                                 headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        try:
            msg = json.loads(e.read().decode('utf-8')).get('error', {})
            msg = f'{msg.get("type", "")}: {msg.get("message", "")}'
        except Exception:
            msg = e.reason
        raise ApifyError(f'HTTP {e.code} {msg}') from None
    except (urllib.error.URLError, TimeoutError) as e:
        raise ApifyError(f'network: {e}') from None


def balance(i, key):
    try:
        d = api('GET', '/users/me/limits', key, timeout=30)['data']
        mx = d['limits']['maxMonthlyUsageUsd']
        used = d['current']['monthlyUsageUsd']
        return {'index': i, 'ok': True, 'limit': mx, 'used': round(used, 4),
                'remaining': round(max(0.0, mx - used), 4),
                'resets': d['monthlyUsageCycle']['endAt'][:10]}
    except (ApifyError, KeyError, TypeError) as e:
        return {'index': i, 'ok': False, 'error': str(e)}


def balances(keys):
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        return list(ex.map(lambda ik: balance(*ik), enumerate(keys)))


def evidence(label, part):
    return os.path.join(RESEARCH, f'{label}_{part}.json')


def save_json(path, obj):
    return write_verified(path, json.dumps(obj, ensure_ascii=False, indent=2))


def wait_and_fetch(label, wait):
    run = json.loads(read_text(evidence(label, 'run')))
    key = apify_keys()[run['key_index']]
    end = time.time() + wait
    while True:
        st = api('GET', f'/actor-runs/{run["id"]}', key)['data']
        if st['status'] not in ('READY', 'RUNNING', 'TIMING-OUT', 'ABORTING') or time.time() >= end:
            break
        time.sleep(8)
    if st['status'] in ('READY', 'RUNNING', 'TIMING-OUT', 'ABORTING'):
        print(f'{label}: still {st["status"]} - run again: product_finder.py apify-fetch {label}')
        return 3
    items, off = [], 0
    while True:
        chunk = api('GET', f'/datasets/{st["defaultDatasetId"]}/items?clean=true&format=json'
                           f'&offset={off}&limit=1000', key, timeout=120)
        items += chunk
        off += len(chunk)
        if len(chunk) < 1000:
            break
    if os.path.exists(evidence(label, 'items')):
        raise BoardError(f'raw/research/{label}_items.json already exists - this run was fetched before')
    save_json(evidence(label, 'status'), st)
    save_json(evidence(label, 'items'), items)
    cost = (st.get('usageTotalUsd') or 0)
    print(f'{label}: {st["status"]}, {len(items)} items, cost ${cost:.3f}, key #{run["key_index"]} -> '
          f'raw/research/{label}_items.json')
    return 0 if st['status'] == 'SUCCEEDED' else 1


def apify_run(actor, input_path, label, max_usd, wait, only_key=None):
    if not re.fullmatch(r'[a-z0-9_]+', label):
        raise BoardError('label must be lowercase letters, digits and underscores')
    for part in ('run', 'status', 'items'):
        if os.path.exists(evidence(label, part)):
            raise BoardError(f'raw/research/{label}_{part}.json exists - labels are never reused, pick a new one')
    inp = json.loads(read_text(input_path))
    keys = apify_keys()
    cands = [b for b in balances(keys) if b['ok'] and b['remaining'] >= max_usd]
    if only_key is not None:
        cands = [b for b in cands if b['index'] == only_key]
    if not cands:
        raise BoardError(f'no Apify key has ${max_usd:.2f} left this cycle - run apify-balance')
    cands.sort(key=lambda b: (b['remaining'], b['index']))       # best fit: use up the emptiest key that suffices
    last = None
    for b in cands[:6]:
        try:
            q = urllib.parse.urlencode({'maxTotalChargeUsd': f'{max_usd:.2f}'})
            d = api('POST', f'/acts/{actor.replace("/", "~")}/runs?{q}', keys[b['index']], inp)['data']
        except ApifyError as e:
            last = e
            print(f'key #{b["index"]}: {e} - trying the next key')
            continue
        save_json(evidence(label, 'run'), {
            'label': label, 'actor': actor.replace('/', '~'), 'key_index': b['index'], 'input': inp,
            'id': d['id'], 'dataset': d['defaultDatasetId'], 'store': d['defaultKeyValueStoreId'],
            'startedAt': d['startedAt']})
        print(f'{label}: started {d["id"]} on key #{b["index"]} (${b["remaining"]:.2f} left, cap ${max_usd:.2f})')
        return wait_and_fetch(label, wait)
    raise BoardError(f'could not start {actor}: {last}')


# ---------------------------------------------------------------- main

def opt(args, name, cast, default):
    if name in args:
        i = args.index(name)
        v = cast(args[i + 1])
        del args[i:i + 2]
        return v
    return default


def main():
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help'):
        print(__doc__)
        return 2
    cmd = args.pop(0)
    try:
        if cmd == 'check':
            D, _ = load()
            errs = check(D)
            for e in errs:
                print('ERROR', e)
            n_rank = sum(1 for a in D['accounts'] if (a.get('performance') or {}).get('eligible'))
            print(f'check: {"OK" if not errs else f"{len(errs)} error(s)"} - {len(D["accounts"])} accounts, '
                  f'{len(D["batches"])} batches, {n_rank} ranked, {len(D["products"])} products')
            return 1 if errs else 0
        if cmd in ('rank', 'links', 'build', 'all'):
            D, seen = load()
            if cmd in ('rank', 'all'):
                before = dump(D)
                derive(D)
                if dump(D) == before:
                    print('board_data.json: derived fields already current')
                else:
                    print(f'board_data.json: written, md5 {save(D, seen)}')
            if cmd in ('links', 'all'):
                write_if_changed(LINKS, links_text(D), 'links.txt')
            if cmd in ('build', 'all'):
                write_if_changed(HTML, page(D), 'product_board.html')
            if cmd == 'all':
                errs = check(load()[0])
                for e in errs:
                    print('ERROR', e)
                print(f'check: {"OK" if not errs else f"{len(errs)} error(s)"}')
                return 1 if errs else 0
            return 0
        if cmd == 'triage':
            if not args:
                return 2
            D, _ = load()
            rows = triage(D, read_text(args[0]))
            print(json.dumps(rows, ensure_ascii=False, indent=1))
            c = {}
            for r in rows:
                c[r['status']] = c.get(r['status'], 0) + 1
            print('triage:', len(rows), 'unique links -', ', '.join(f'{v} {k}' for k, v in sorted(c.items())),
                  file=sys.stderr)
            return 0
        if cmd == 'apify-balance':
            rows = balances(apify_keys())
            if '--json' in args:
                print(json.dumps(rows, indent=1))
            else:
                for r in rows:
                    print(f'#{r["index"]:>3}  ' + (f'${r["remaining"]:>5.2f} left of ${r["limit"]:.0f}  '
                          f'(used ${r["used"]:.2f}, resets {r["resets"]})' if r['ok'] else f'ERROR {r["error"]}'))
            ok = [r for r in rows if r['ok']]
            print(f'apify-balance: {len(rows)} keys, {len(ok)} working, ${sum(r["remaining"] for r in ok):.2f} '
                  f'left in total, {sum(1 for r in ok if r["remaining"] >= 1)} keys with $1 or more')
            return 0 if ok else 1
        if cmd == 'apify-run':
            max_usd = opt(args, '--max-usd', float, 1.0)
            wait = opt(args, '--wait', int, 150)
            only = opt(args, '--key', int, None)
            if len(args) != 3:
                return 2
            return apify_run(args[0], args[1], args[2], max_usd, wait, only)
        if cmd == 'apify-fetch':
            wait = opt(args, '--wait', int, 150)
            if len(args) != 1:
                return 2
            return wait_and_fetch(args[0], wait)
        print(f'unknown command {cmd}\n{__doc__}')
        return 2
    except (BoardError, ApifyError) as e:
        print('FAILED', e)
        return 1


if __name__ == '__main__':
    sys.exit(main())
