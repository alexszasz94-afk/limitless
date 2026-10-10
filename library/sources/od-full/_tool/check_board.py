#!/usr/bin/env python3
"""Verify every path a generated board points at actually exists on disk,
and that every card on every board has the same skeleton.

The skeleton is the card that x_systems/video_boards/tools/build_board.py
writes for every board:

    article.card
      header.card-h      idx / card-t (h4 + p) / time
      span.variant       optional - "REUSED FROM LIBRARY" and friends
      div.media          one .m-col per starting frame
      div.tagbar         model chips and file names
      div.clipst         optional - the generated clip(s) underneath
      button.d-head      optional - "Prompt & notes"
      div.det            the dropdown body, required whenever d-head is there

Usage:
    python3 _tool/check_board.py            # every product
    python3 _tool/check_board.py MERRY
"""
import os, re, sys, html
sys.dont_write_bytecode = True
from make_thumbs import targets

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# data-clip is a lane id, not a path, so it is deliberately not in here
ATTR = re.compile(r'(?:src|href|data-src|data-full)="([^"]+)"')
TAG = re.compile(r'<(/?)(\w+)([^>]*)>')
VOID = {'img', 'br', 'hr', 'meta', 'link', 'input', 'path', 'source',
        'use', 'circle', 'rect', 'stop', 'polygon', 'line'}

# canonical order of a card's direct children; a card may skip an optional
# one but may never reorder them or repeat them
ORDER = ['card-h', 'variant', 'media', 'tagbar', 'clipst', 'd-head', 'det']
REQUIRED = {'card-h', 'media'}


def strip(doc):
    doc = re.sub(r'<style[^>]*>.*?</style>', '', doc, flags=re.S)
    return re.sub(r'<script[^>]*>.*?</script>', '', doc, flags=re.S)


def blocks(doc, tag, needle):
    """Balanced-tag spans of <tag ...needle...>, outermost only."""
    spans, stack = [], []
    for m in TAG.finditer(doc):
        close, name, attrs = m.groups()
        if name in VOID or attrs.rstrip().endswith('/'):
            continue
        if not close:
            stack.append((name, m.start(), attrs))
        else:
            while stack:
                t, s, a = stack.pop()
                if t == name:
                    if name == tag and needle in a:
                        spans.append((s, m.end()))
                    break
    spans.sort()
    out, last = [], -1
    for s, e in spans:
        if s >= last:
            out.append(doc[s:e])
            last = e
    return out


def children(card):
    """First-level class names inside a card element."""
    inner = card[card.index('>') + 1:card.rindex('</')]
    out, depth = [], 0
    for m in TAG.finditer(inner):
        close, name, attrs = m.groups()
        if name in VOID or attrs.rstrip().endswith('/'):
            continue
        if not close:
            if depth == 0:
                c = re.search(r'class="([^"]*)"', attrs)
                out.append(c.group(1).split()[0] if c else name)
            depth += 1
        else:
            depth -= 1
    return out


def check_shape(card, n):
    kids = children(card)
    label = f'card {n}'
    m = re.search(r'<h4>(.*?)</h4>', card, re.S)
    if m:
        label += f' "{re.sub(chr(60) + "[^>]+>", "", m.group(1))[:40]}"'
    out = []
    unknown = [k for k in kids if k not in ORDER]
    if unknown:
        out.append(f'  SHAPE  {label}: unexpected child {unknown}')
    known = [k for k in kids if k in ORDER]
    if len(set(known)) != len(known):
        out.append(f'  SHAPE  {label}: repeated child in {known}')
    if [k for k in ORDER if k in known] != known:
        out.append(f'  SHAPE  {label}: out of order {known} - want {ORDER}')
    for r in REQUIRED:
        if r not in known:
            out.append(f'  SHAPE  {label}: missing .{r}')
    if ('d-head' in known) != ('det' in known):
        out.append(f'  SHAPE  {label}: d-head and det must appear together')
    return out


def check_columns(body):
    """columns layout: every run (data-col vN_cNN) has its four cells - reference, new look, final
    video, prompts - and a video either shows a final video cell per run or one final export"""
    out = []
    cells = {k: re.findall(r'<div class="cell ' + k + r'\b[^"]*" data-col="([^"]+)"', body)
             for k in ('ref', 'look', 'out', 'drw')}
    runs = cells['ref']
    if len(set(runs)) != len(runs):
        out.append('  SHAPE  columns: a run appears twice in the reference row')
    finals = set(re.findall(r'<div class="cell out fincell" data-vid="(\d+)"', body))
    for k in ('look', 'drw'):
        if sorted(cells[k]) != sorted(runs):
            out.append(f'  SHAPE  columns: the {k} row does not have one cell per run '
                       f'({sorted(set(runs) ^ set(cells[k]))})')
    for r in runs:
        vid = re.match(r'v(\d+)_', r).group(1)
        if r not in cells['out'] and vid not in finals:
            out.append(f'  SHAPE  columns: run {r} has no final-video cell')
    return out


def check(product):
    base = os.path.join(ROOT, product)
    p = os.path.join(base, 'video_board.html')
    if not os.path.exists(p):
        return [f'{product}: no video_board.html'], 0
    doc = open(p, encoding='utf-8').read()
    bad, ok = [], 0
    # one walk of the product folder instead of one stat per referenced path (the mount is slow per call)
    on_disk = set()
    for d, dirs, files in os.walk(base):
        r = os.path.relpath(d, base).replace(os.sep, '/')
        for f in files:
            on_disk.add(f if r == '.' else r + '/' + f)
    for raw in set(ATTR.findall(doc)):
        u = html.unescape(raw)
        if u.startswith(('http:', 'https:', 'data:', '#', 'mailto:')):
            continue
        if u.replace('\\', '/') not in on_disk:
            bad.append(f'  MISSING  {u}')
        else:
            ok += 1

    # Full coverage, including exports even if a board never references their poster.
    for source, poster in targets(product):
        try:
            st = os.stat(poster)
        except OSError:
            bad.append('  MISSING THUMB  ' + os.path.relpath(poster, base))
            continue
        if st.st_size == 0:
            bad.append('  MISSING THUMB  ' + os.path.relpath(poster, base))
        elif st.st_mtime < os.stat(source).st_mtime:
            bad.append('  STALE THUMB  ' + os.path.relpath(poster, base))

    for a, b in (('<article', '</article>'), ('<section', '</section>'),
                 ('<div', '</div>'), ('<span', '</span>'),
                 ('<button', '</button>')):
        if doc.count(a) != doc.count(b):
            bad.append(f'  UNBALANCED  {doc.count(a)} {a} vs {doc.count(b)} {b}')

    body = strip(doc)
    if '<section class="cgrid"' in body:
        bad += check_columns(body)
    cards = blocks(body, 'article', 'class="card')
    if not cards and '<section class="lane"' in body:
        bad.append('  no cards found')          # a brand-new board has no lanes yet - that is fine
    for i, c in enumerate(cards, 1):
        bad += check_shape(c, i)
    return bad, ok


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    products = sorted(d for d in os.listdir(ROOT)
                      if os.path.isdir(os.path.join(ROOT, d)) and ' - ' in d)
    if args:
        products = [p for p in products if args[0].upper() in p.upper()]
        if not products:
            print(f'no product matches {args[0]!r} - nothing was checked')
            return 2
    tot_bad = 0
    for p in products:
        bad, ok = check(p)
        tot_bad += len(bad)
        print(f'{p}: {ok} paths resolve, {len(bad)} problem(s)')
        for b in bad[:40]:
            print(b)
        if len(bad) > 40:
            print(f'  ... and {len(bad) - 40} more')
    print(f'\n{tot_bad} problem(s)')
    return 1 if tot_bad else 0


if __name__ == '__main__':
    sys.exit(main())
