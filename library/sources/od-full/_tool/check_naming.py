#!/usr/bin/env python3
"""Enforce _tool/NAMING.md. Exit 0 = clean.

    python3 _tool/check_naming.py            # every product
    python3 _tool/check_naming.py MERRY      # products whose name contains MERRY
    python3 _tool/check_naming.py --quiet    # only the summary line
"""
import os, re, sys, fnmatch, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRODUCT_RE = re.compile(r'^[A-Z0-9]+[A-Z0-9 ]* - [A-Z0-9][A-Z0-9 ]*$')
ASSETS_RE  = re.compile(r'^video_(\d+)_assets$')
NAME_RE    = re.compile(r'^v(\d+)_c(\d{2})_(g|r)(\d+)$')

ALLOWED_IN_ASSETS = {'starting_frames', 'clips', 'references'}
ALLOWED_FILES_IN_ASSETS = {'prompts.md'}
EXT_FOR = {'starting_frames': {'.png'}, 'references': {'.png', '.mp4'},
           'clips': {'.mp4'}, 'upscaled': {'.mp4'}}

# things we deliberately do not police
SKIP_DIRS = {'_board_thumbs', 'to_delete', 'competition', 'product_images',
             'videos_to_post', 'songs', 'stories', 'upscaled_videos', 'references', 'node_modules',
             '.git', '_tool', 'x_systems', 'x_research'}

# NAMING.md §2: what a product folder holds, and nothing else
PRODUCT_ENTRIES = {'video_board.html', 'references', 'product_images', 'competition', 'content',
                   'videos_to_post', 'notes.txt'}
# dated exceptions Daniel chose to keep - remove the line when the folder goes
TOLERATED = set()   # (product, entry) pairs allowed outside the NAMING.md layout - none in this copy
# NAMING.md §2: what content/ holds besides video_N_assets/
CONTENT_ENTRIES = {'_board_thumbs', 'lost_takes.txt', 'stories', 'upscaled_videos'}   # upscaled_videos: Daniel 2026-10-06
TAKE_RE = re.compile(r'\bv(\d+)_c(\d\d)_[gr]\d+\.(?:png|mp4)\b')

BANNED_SUFFIX = re.compile(r'_(2k|upscaled|final|new|old|best|copy|v\d+)$', re.I)
LETTER_TAKE   = re.compile(r'^v\d+_c\d+_[gr]\d+[a-z]+$', re.I)


class Report:
    def __init__(self):
        self.errors = []   # (product, path, message)
        self.ok = 0

    def err(self, product, path, msg):
        self.errors.append((product, path, msg))


def check_lowercase(rep, product, rel, name):
    if name != name.lower():
        rep.err(product, rel, 'not lowercase')
        return False
    if ' ' in name:
        rep.err(product, rel, 'contains a space')
        return False
    return True


def check_asset_file(rep, product, rel, fname, bucket):
    stem, ext = os.path.splitext(fname)
    if not check_lowercase(rep, product, rel, fname):
        return
    if LETTER_TAKE.match(stem):
        rep.err(product, rel, 'letter suffix on take (g1b/g3c) - banned, use the next number')
        return
    if BANNED_SUFFIX.search(stem):
        rep.err(product, rel, 'banned suffix (_2k/_final/_new/...) - the folder is the suffix')
        return
    m = NAME_RE.match(stem)
    if not m:
        rep.err(product, rel, 'does not match v<N>_c<NN>_<g|r><K>')
        return
    _, cc, kind, k = m.groups()
    if k.lstrip('0') != k or k == '0':
        rep.err(product, rel, 'take number must not be zero-padded and starts at 1')
        return
    want = EXT_FOR.get(bucket, set())
    if want and ext not in want:
        rep.err(product, rel, f'extension {ext} not allowed in {bucket}/ (want {"/".join(sorted(want))})')
        return
    if bucket == 'references' and kind != 'r':
        rep.err(product, rel, 'files in references/ must use the r<K> kind')
        return
    if bucket in ('clips', 'upscaled', 'starting_frames') and kind != 'g':
        rep.err(product, rel, f'files in {bucket}/ must use the g<K> kind')
        return
    rep.ok += 1


def check_assets_folder(rep, product, adir, rel_base):
    for entry in sorted(os.listdir(adir)):
        p = os.path.join(adir, entry)
        rel = os.path.join(rel_base, entry)
        if os.path.isdir(p):
            if entry not in ALLOWED_IN_ASSETS:
                rep.err(product, rel, 'unexpected folder - only starting_frames/ clips/ references/ allowed')
                continue
            for sub in sorted(os.listdir(p)):
                sp = os.path.join(p, sub)
                srel = os.path.join(rel, sub)
                if os.path.isdir(sp):
                    if entry == 'clips' and sub == 'upscaled':
                        for f in sorted(os.listdir(sp)):
                            if os.path.isdir(os.path.join(sp, f)):
                                rep.err(product, os.path.join(srel, f), 'no folders inside clips/upscaled/')
                            else:
                                check_asset_file(rep, product, os.path.join(srel, f), f, 'upscaled')
                    else:
                        rep.err(product, srel, f'unexpected folder inside {entry}/')
                else:
                    check_asset_file(rep, product, srel, sub, entry)
        else:
            if entry not in ALLOWED_FILES_IN_ASSETS:
                rep.err(product, rel, 'unexpected file - only prompts.md belongs here')
    if not os.path.exists(os.path.join(adir, 'prompts.md')):
        rep.err(product, rel_base, 'missing prompts.md')
    for sub in sorted(ALLOWED_IN_ASSETS):
        if not os.path.isdir(os.path.join(adir, sub)):
            rep.err(product, os.path.join(rel_base, sub), 'missing folder - every video_N_assets/ holds '
                    'starting_frames/ clips/ references/ and prompts.md (NAMING.md §3); create it, empty is fine')

def load_lost(product):
    """Names in content/lost_takes.txt are known-destroyed; the numbering holes
    they leave are expected and must not be reported forever."""
    p = os.path.join(ROOT, product, 'content', 'lost_takes.txt')
    out = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            line = line.strip()
            if line and not line.startswith('#'):
                out.add(os.path.splitext(line)[0])
    return out


def orphan_checks(rep, product, adir, rel_base, lost=frozenset()):
    """Cross-checks that catch real mistakes, not just name shapes."""
    def stems(sub):
        d = os.path.join(adir, sub)
        if not os.path.isdir(d):
            return set()
        return {os.path.splitext(f)[0] for f in os.listdir(d)
                if os.path.isfile(os.path.join(d, f))}

    clips = stems('clips')
    ups = stems(os.path.join('clips', 'upscaled'))
    for s in sorted(ups - clips):
        rep.err(product, os.path.join(rel_base, 'clips/upscaled', s + '.mp4'),
                'upscale has no source clip of the same name')

    refs_dir = os.path.join(adir, 'references')
    if os.path.isdir(refs_dir):
        refs = {}
        for f in os.listdir(refs_dir):
            stem = os.path.splitext(f)[0]
            if NAME_RE.match(stem):
                if stem in refs:
                    rep.err(product, os.path.join(rel_base, 'references', f),
                            'reference number reused across formats: ' + refs[stem])
                refs[stem] = f

    by_shot = {}
    for sub in ('starting_frames', 'clips', 'references'):
        for s in stems(sub):
            m = NAME_RE.match(s)
            if m:
                by_shot.setdefault((sub, m.group(1), m.group(2), m.group(3)), []).append(int(m.group(4)))
    for (sub, v, c, kind), nums in sorted(by_shot.items()):
        nums = sorted(nums)
        missing = [n for n in range(1, max(nums) + 1)
                   if n not in nums and f'v{v}_c{c}_{kind}{n}' not in lost]
        if missing:
            rep.err(product, os.path.join(rel_base, sub),
                    f'v{v}_c{c}_{kind}: missing take(s) {", ".join(map(str, missing))} '
                    f'(have {", ".join(map(str, nums))}) - a take was deleted or overwritten')


def archive_checks(rep, product, lost):
    """Every take named in a video's prompts.md, and every content/ path on the board, must exist
    on disk or be listed in lost_takes.txt. This is what catches a deleted LATEST take (a numbering
    hole below the highest take is caught by orphan_checks; the highest one leaves no hole)."""
    content = os.path.join(ROOT, product, 'content')
    on_disk = set()
    for d, dirs, files in os.walk(content):
        dirs[:] = [x for x in dirs if x != '_board_thumbs']
        on_disk.update(files)
    lost_names = {l + ext for l in lost for ext in ('.png', '.mp4')}
    for entry in sorted(os.listdir(content)):
        m = ASSETS_RE.match(entry)
        pm = os.path.join(content, entry, 'prompts.md')
        if not m or not os.path.isfile(pm):
            continue
        text = open(pm, encoding='utf-8', errors='replace').read()
        missing = sorted({t.group(0) for t in TAKE_RE.finditer(text)
                          if t.group(1) == m.group(1) and t.group(0) not in on_disk and t.group(0) not in lost_names})
        for name in missing:
            rep.err(product, os.path.join('content', entry, 'prompts.md'),
                    f'{name} is named in the archive but is not on disk and not in lost_takes.txt - '
                    'a take was deleted (record it in lost_takes.txt with Daniel) or the name is a typo')
    bd = os.path.join(content, '_board_thumbs', 'board_data.json')
    if os.path.isfile(bd):
        try:
            data = json.load(open(bd, encoding='utf-8'))
        except ValueError as e:
            rep.err(product, 'content/_board_thumbs/board_data.json', f'not valid JSON: {e}')
            return
        seen = set()

        def walk(o):
            if isinstance(o, dict):
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
            elif isinstance(o, str) and o.startswith('content/') and TAKE_RE.search(o):
                n = os.path.basename(o)
                if n not in on_disk and n not in lost_names and o not in seen:
                    seen.add(o)
                    rep.err(product, o, 'on the board but not on disk and not in lost_takes.txt - '
                            'a take was deleted (record it) or the path is wrong')
        walk(data)


def check_product(rep, product):
    pdir = os.path.join(ROOT, product)
    if not PRODUCT_RE.match(product):
        rep.err(product, product, 'product folder must be "BRAND - PRODUCT" in caps')

    for entry in sorted(os.listdir(pdir)):
        if entry not in PRODUCT_ENTRIES and not entry.startswith('.') and (product, entry) not in TOLERATED:
            rep.err(product, entry, 'not part of the product folder layout (NAMING.md §2) - '
                    'move it out of the product folder (to_delete/ if it is junk)')

    content = os.path.join(pdir, 'content')
    if not os.path.isdir(content):
        rep.err(product, 'content', 'missing content/ folder')
        return
    lost = load_lost(product)

    for entry in sorted(os.listdir(content)):
        p = os.path.join(content, entry)
        rel = os.path.join('content', entry)
        if not ASSETS_RE.match(entry) and entry not in CONTENT_ENTRIES and not entry.startswith('.'):
            rep.err(product, rel, 'not part of content/ (NAMING.md §2: video_N_assets/, _board_thumbs/, '
                    'lost_takes.txt, stories/, upscaled_videos/) - move it out')
        if not os.path.isdir(p) or entry in SKIP_DIRS:
            continue
        if not ASSETS_RE.match(entry):
            check_lowercase(rep, product, rel, entry)
            if re.search(r'round\d|final|new_|_old|temp|test', entry, re.I):
                rep.err(product, rel, 'junk folder name - move it to to_delete/ at the drive root')
            continue
        check_assets_folder(rep, product, p, rel)
        orphan_checks(rep, product, p, rel, lost)
    archive_checks(rep, product, lost)

    prefs = os.path.join(pdir, 'references')
    if os.path.isdir(prefs):
        for f in sorted(os.listdir(prefs)):
            if os.path.isfile(os.path.join(prefs, f)):
                check_lowercase(rep, product, os.path.join('references', f), f)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    quiet = '--quiet' in sys.argv
    products = sorted(d for d in os.listdir(ROOT)
                      if os.path.isdir(os.path.join(ROOT, d)) and ' - ' in d)
    if args:
        pat = args[0]
        products = [p for p in products
                    if fnmatch.fnmatch(p, pat) or pat.upper() in p.upper()]
        if not products:
            print(f'no product matches {pat!r}')
            return 2

    rep = Report()
    for p in products:
        check_product(rep, p)

    if rep.errors and not quiet:
        cur = None
        for product, path, msg in rep.errors:
            if product != cur:
                print(f'\n{product}')
                cur = product
            print(f'  {path}\n      -> {msg}')
        print()

    n = len(rep.errors)
    print(f'{rep.ok} files conform, {n} violation{"" if n == 1 else "s"}'
          f' across {len(products)} product{"" if len(products) == 1 else "s"}')
    return 1 if n else 0


if __name__ == '__main__':
    sys.exit(main())
