#!/usr/bin/env python3
"""Generate the .webp poster for every media file the board shows.

    python3 _tool/make_thumbs.py            # every product
    python3 _tool/make_thumbs.py MERRY      # one product
    python3 _tool/make_thumbs.py --force    # rebuild even if present

Thumb path mirrors the asset tree:
    <PRODUCT>/content/_board_thumbs/<relpath-from-product-root>.webp
"""
import os, sys, subprocess, concurrent.futures as cf
import tempfile, shutil, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIDTH = 360          # 9:16 card tile is ~180 css px; 2x for retina
QUALITY = 72
SKIP = {'_board_thumbs', 'to_delete', 'node_modules', '.git'}


def targets(product):
    """(src, dst) for content assets and all finished exports."""
    base = os.path.join(ROOT, product)
    out = []
    for source_dir in ('content', 'videos_to_post'):
        for dirpath, dirnames, filenames in os.walk(os.path.join(base, source_dir)):
            dirnames[:] = [d for d in dirnames if d not in SKIP]
            for f in filenames:
                if os.path.splitext(f)[1].lower() not in ('.png', '.mp4'):
                    continue
                src = os.path.join(dirpath, f)
                rel = os.path.relpath(src, base)
                dst = os.path.join(base, 'content', '_board_thumbs',
                                   os.path.splitext(rel)[0] + '.webp')
                out.append((src, dst))
    return out


def build(job):
    src, dst, force = job
    if not force:
        try:
            sd = os.stat(dst)                    # one stat each instead of exists + size + mtime
            if sd.st_size > 0 and sd.st_mtime >= os.stat(src).st_mtime:
                return 'skip'
        except OSError:
            pass
    try:
        with tempfile.TemporaryDirectory(prefix='board_thumb_') as tmp:
            staged = os.path.join(tmp, 'poster.webp')
            cmd = ['ffmpeg', '-v', 'error', '-y']
            if src.lower().endswith('.mp4'):
                cmd += ['-ss', '0.4']
            cmd += ['-i', src, '-frames:v', '1', '-vf', f'scale={WIDTH}:-2',
                    '-q:v', str(QUALITY), staged]
            r = subprocess.run(cmd, capture_output=True)
            if (r.returncode != 0 or not os.path.exists(staged)
                    or os.path.getsize(staged) == 0):
                if src.lower().endswith('.mp4'):
                    r = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src,
                                        '-frames:v', '1', '-vf', f'scale={WIDTH}:-2',
                                        '-q:v', str(QUALITY), staged], capture_output=True)
                if (r.returncode != 0 or not os.path.exists(staged)
                        or os.path.getsize(staged) == 0):
                    return 'fail:' + os.path.basename(src)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(staged, 'rb') as f:
                expected = hashlib.sha256(f.read()).digest()
            shutil.copyfile(staged, dst)
            with open(dst, 'rb') as f:
                actual = hashlib.sha256(f.read()).digest()
            if os.path.getsize(staged) != os.path.getsize(dst) or actual != expected:
                return 'fail:' + os.path.basename(src) + ' (copy verification)'
        return 'made'
    except OSError as exc:
        return 'fail:' + os.path.basename(src) + ' (' + str(exc) + ')'


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    force = '--force' in sys.argv
    products = sorted(d for d in os.listdir(ROOT)
                      if os.path.isdir(os.path.join(ROOT, d)) and ' - ' in d)
    if args:
        products = [p for p in products if args[0].upper() in p.upper()]
        if not products:
            print(f'no product matches {args[0]!r} - nothing was built')
            return 2

    total_made = total_skip = 0
    fails = []
    for p in products:
        jobs = [(s, d, force) for s, d in targets(p)]
        with cf.ThreadPoolExecutor(max_workers=8) as ex:
            res = list(ex.map(build, jobs))
        made = res.count('made'); skip = res.count('skip')
        bad = [r for r in res if r.startswith('fail')]
        total_made += made; total_skip += skip; fails += bad
        print(f'{p}: {made} built, {skip} already current'
              + (f', {len(bad)} FAILED' if bad else ''))
    for f in fails:
        print('  ' + f)
    print(f'\n{total_made} thumbs built, {total_skip} current, {len(fails)} failed')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
