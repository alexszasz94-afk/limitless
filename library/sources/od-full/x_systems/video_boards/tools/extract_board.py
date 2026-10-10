#!/usr/bin/env python3
"""Rescue tool: read a built video_board.html back into board_data.json.

    python3 x_systems/video_boards/tools/extract_board.py THEX            # prints a summary, writes nothing
    python3 x_systems/video_boards/tools/extract_board.py THEX --write    # writes content/_board_thumbs/board_data.json

Use it only when board_data.json is lost or damaged and video_board.html is
still good. It understands boards produced by build_board.py (the template in
x_systems/video_boards/template); a columns-layout board carries its data inside the page and is
read back byte for byte. After --write, run build_board.py and compare:
the rebuilt page must match the old one card for card.
Standard library only.
"""
import html, json, os, re, sys
from html.parser import HTMLParser

sys.dont_write_bytecode = True
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(KIT))
DATA_REL = os.path.join('content', '_board_thumbs', 'board_data.json')
VOID = {'img', 'br', 'hr', 'meta', 'link', 'input', 'source', 'path', 'circle', 'rect', 'stop', 'polygon', 'line', 'use'}


class Node:
    __slots__ = ('tag', 'attrs', 'kids', 'parent', 's', 'e', 'is_', 'ie')

    def __init__(self, tag, attrs, parent, s):
        self.tag, self.attrs, self.kids, self.parent, self.s = tag, dict(attrs), [], parent, s
        self.e = self.is_ = self.ie = None

    @property
    def cls(self):
        return (self.attrs.get('class') or '').split()

    def has(self, c):
        return c in self.cls

    def find(self, pred):
        for k in self.kids:
            if pred(k):
                return k
            r = k.find(pred)
            if r:
                return r
        return None

    def findall(self, pred, out=None):
        out = [] if out is None else out
        for k in self.kids:
            if pred(k):
                out.append(k)
            k.findall(pred, out)
        return out

    def child(self, c):
        for k in self.kids:
            if k.has(c) or k.tag == c:
                return k
        return None


class Tree(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.lines = [0]
        for m in re.finditer('\n', src):
            self.lines.append(m.end())
        self.root = Node('#root', {}, None, 0)
        self.cur = self.root
        self.feed(src)
        self.close()

    def off(self):
        l, c = self.getpos()
        return self.lines[l - 1] + c

    def handle_starttag(self, tag, attrs):
        s = self.off()
        n = Node(tag, [(k, v or '') for k, v in attrs], self.cur, s)
        n.is_ = s + len(self.get_starttag_text())
        self.cur.kids.append(n)
        if tag not in VOID:
            self.cur = n
        else:
            n.e = n.ie = n.is_

    def handle_startendtag(self, tag, attrs):
        s = self.off()
        n = Node(tag, [(k, v or '') for k, v in attrs], self.cur, s)
        n.is_ = n.e = n.ie = s + len(self.get_starttag_text())
        self.cur.kids.append(n)

    def handle_endtag(self, tag):
        s = self.off()
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is self.root:
            return
        n.ie = s
        n.e = self.src.index('>', s) + 1
        self.cur = n.parent


def inner(src, n):
    return src[n.is_:n.ie]


def text(src, n):
    return html.unescape(re.sub(r'<[^>]+>', '', inner(src, n)))


def plain(src, n):
    """inner text with the builder's ' &middot; ' separators turned back into ' · '"""
    return text(src, n)


def split_label(lbl):
    """'START FRAME · v1_c01_g1.png' -> ('START FRAME', 'v1_c01_g1.png')"""
    if ' · ' in lbl:
        a, b = lbl.rsplit(' · ', 1)
        return a, b
    return lbl, ''


def embedded(src):
    """a columns-layout board carries its own board_data.json (build_board.py puts it in
    <script type="application/json" id="board-data">) - read that, exactly, instead of parsing the page"""
    m = re.search(r'<script type="application/json" id="board-data">(.*?)</script>', src, re.S)
    return json.loads(m.group(1)) if m else None


def extract(src):
    D = embedded(src)
    if D is not None:
        return D
    T = Tree(src)
    R = T.root
    D = {'schema': 'video-board/1'}
    title = R.find(lambda n: n.tag == 'title')
    D['brand'] = text(src, title).replace(' — Video Board', '').strip()
    icon = R.find(lambda n: n.tag == 'link' and n.attrs.get('rel') == 'icon')
    if icon:
        try:
            default = open(os.path.join(KIT, 'template', 'favicon.txt'), encoding='utf-8').read().strip()
        except OSError:
            default = None
        if html.unescape(icon.attrs.get('href') or '') != default:
            D['favicon'] = icon.attrs.get('href')
    nb = R.find(lambda n: n.attrs.get('id') == 'nb')
    if nb:
        D['key'] = nb.attrs.get('data-key')
    h1 = R.find(lambda n: n.tag == 'h1')
    sub = h1.child('span') if h1 else None
    if sub:
        parts = text(src, sub).split(' · ')
        extra = [p for p in parts if not re.match(r'^\d+ (videos?|shots?|waiting|posted)|^\d+ videos? posted|^\d+ posted', p)]
        if extra:
            D['subtitle_extra'] = ' · '.join(extra)
    leg = R.find(lambda n: n.has('legend'))
    D['legend'] = []
    for i in (leg.kids if leg else []):
        b = i.child('b')
        col = re.search(r'background:\s*([^;"]+)', b.attrs.get('style', '')).group(1).strip()
        D['legend'].append({'color': col, 'text': text(src, i).strip()})
    # panels
    rules = R.find(lambda n: n.has('rules') and n.tag == 'div')
    D['panels'] = []
    for box in (rules.kids if rules else []):
        h3 = box.find(lambda n: n.tag == 'h3')
        t = text(src, h3).strip() if h3 else ''
        if t == 'How this board works':
            items = [inner(src, li) for li in box.findall(lambda n: n.tag == 'li')]
            if len(items) > 4:
                D['source_note_html'] = items[4]
            continue
        if box.has('spec'):
            im = box.find(lambda n: n.tag == 'img')
            p = {'type': 'spec', 'title': t, 'image': im.attrs.get('data-full') or
                 re.sub(r'^content/_board_thumbs/', '', im.attrs['src']).rsplit('.', 1)[0] + '.png'}
            k = box.find(lambda n: n.has('kicker'))
            if k:
                p['kicker'] = text(src, k)
            ld = box.find(lambda n: n.has('lead'))
            if ld:
                p['lead_html'] = inner(src, ld)
            p['rows_html'] = [[text(src, d.child('dt')), inner(src, d.child('dd'))]
                              for d in box.find(lambda n: n.tag == 'dl').kids]
            r_ = box.find(lambda n: n.has('sp-rules'))
            if r_:
                p['rules_html'] = inner(src, r_)
        elif box.find(lambda n: n.has('specs')):
            p = {'type': 'specs', 'title': t,
                 'rows': [[text(src, s) for s in row.kids] for row in box.findall(lambda n: n.has('specs'))]}
        else:
            lst = box.find(lambda n: n.tag in ('ol', 'ul'))
            p = {'type': 'list', 'title': t, 'items_html': [inner(src, li) for li in lst.kids if li.tag == 'li']}
            if lst.tag == 'ul':
                p['ordered'] = False
        if box.has('wide'):
            p['wide'] = True
        D['panels'].append(p)
    # lanes
    D['lanes'] = []
    for ln in R.findall(lambda n: n.tag == 'section' and n.has('lane')):
        L = {}
        side = ln.child('lane-side')
        L['n'] = int(re.sub(r'\D', '', text(src, side.child('lane-n'))))
        L['title'] = text(src, side.child('h2'))
        hk = side.child('lane-hook')
        if hk:
            L['caption'] = text(src, hk).strip().strip('\u201c\u201d')
        fin = side.find(lambda n: n.has('final') and n.has('vfac'))
        if fin is not None:
            L['final'] = fin.attrs.get('data-src') or ('videos_to_post/video_%d.mp4' % L['n'])
        else:
            L['final'] = None
        L['meta'] = [[text(src, d.child('dt')), text(src, d.child('dd'))] for d in side.child('dl').kids]
        sn = side.child('lane-note')
        if sn:
            L['side_note'] = inner(src, sn)
        L['groups'] = []
        for g in ln.child('lane-body').kids:
            gh = g.child('group-h')
            G = {'name': text(src, gh.child('g-name')), 'sub': text(src, gh.child('g-sub')),
                 'color': re.search(r'--a:\s*([^;"]+)', g.attrs.get('style', '')).group(1).strip(), 'cards': []}
            for c in g.child('cards').kids:
                G['cards'].append(card(src, c))
            L['groups'].append(G)
        # the builder adds the Shots row itself
        auto = 'Shots'
        L['meta'] = [m for m in L['meta'] if m[0] != auto]
        D['lanes'].append(L)
    return D


def media_path(n):
    """the real file behind an <img class=mimg> or a .vfac"""
    if n.attrs.get('data-full'):
        return n.attrs['data-full']
    if n.attrs.get('data-src'):
        return n.attrs['data-src']
    if n.attrs.get('data-lost'):
        return n.attrs['data-lost']
    img = n if n.tag == 'img' else n.find(lambda k: k.tag == 'img')
    s = re.sub(r'^content/_board_thumbs/', '', img.attrs['src'])
    return s.rsplit('.', 1)[0] + ('.mp4' if n.has('vfac') else '.png')


def card(src, c):
    C = {'clip': c.attrs['data-clip'], 'stage': c.attrs['data-stage'], 'status': c.attrs['data-status']}
    h = c.child('card-h')
    ct = h.child('card-t')
    C['title'] = text(src, ct.child('h4'))
    C['desc'] = text(src, ct.child('p'))
    tip = html.unescape(ct.attrs.get('title', ''))
    if tip and tip != C['desc']:
        C['tip'] = tip
    chip = text(src, h.child('fin'))
    va = c.child('variant')
    if va:
        C['variant'] = text(src, va)
    C['frames'] = []
    if c.attrs.get('data-driver'):
        # motion transfer: no start frame; the media column plays our generated clip, not a frame
        C['driver'] = html.unescape(c.attrs['data-driver'])
    for col in c.child('media').kids:
        if C.get('driver'):
            break
        lbl, _ = split_label(text(src, col.child('m-lbl')))
        im = col.find(lambda n: n.tag == 'img')
        if im is None:
            continue
        C['frames'].append({'label': lbl, 'file': media_path(im)})
    tg = c.child('tagbar')
    tags = {}
    for t in tg.kids:
        if t.has('vid'):
            tags['clip'] = text(src, t)
        elif t.has('note'):
            tags.setdefault('extra', []).append(text(src, t))
        else:
            tags['image'] = text(src, t)
    C['tags'] = tags
    cs = c.child('clipst')
    fac = cs.find(lambda n: n.has('vfac')) if cs else None
    if fac is not None:
        info = cs.child('cinfo')
        play = media_path(fac)
        cfile = text(src, info.child('c-file'))
        folder = play.rsplit('/', 1)[0]
        if folder.endswith('/upscaled'):
            folder = folder[:-len('/upscaled')]
        T = {'file': folder + '/' + cfile}
        if fac.has('lost'):
            # a lost take shows another file's thumbnail as its poster
            T = {'file': fac.attrs['data-lost']}
            img = fac.find(lambda k: k.tag == 'img')
            poster = re.sub(r'^content/_board_thumbs/', '', img.attrs['src']).rsplit('.', 1)[0]
            if poster != T['file'].rsplit('.', 1)[0]:
                T['poster'] = poster + ('.png' if '/starting_frames/' in poster or '/references/' in poster else '.mp4')
        elif play != T['file']:
            T['play'] = play
        lbl = text(src, info.child('c-lbl'))
        if lbl != 'Clip in the cut':
            T['label'] = lbl
        T['info'] = [text(src, k) for k in info.kids if k.has('c-2k')]
        C['take'] = T
    file_ = html.unescape(c.attrs.get('data-file', ''))
    default = os.path.basename(C['take']['file']) if (C['stage'] == 'clip' and C.get('take')) else \
        (os.path.basename(C['frames'][0]['file']) if C['frames'] else '')
    if file_ != default:
        C['file'] = file_
    # chip: keep only if it is not what the builder would print
    from_builder = {('frame', 'review'): 'FRAME FOR REVIEW', ('frame', 'approved'): 'FRAME APPROVED',
                    ('frame', 'rejected'): 'FRAME REJECTED', ('clip', 'review'): 'CLIP FOR REVIEW',
                    ('clip', 'approved'): 'APPROVED', ('clip', 'rejected'): 'REJECTED'}[(C['stage'], C['status'])]
    m = re.search(r'_([gr]\d+)\.\w+$', file_)
    if m:
        from_builder += ' · ' + m.group(1)
    if chip != from_builder:
        C['chip'] = chip
    dn = c.child('d-head')
    if dn is not None:
        n_ = text(src, dn.child('d-n')).split(' · ')
        extra = [x for x in n_ if not re.match(r'^\d+ (prompts?|other takes?)$', x)]
        if extra:
            C['count_note'] = ' · '.join(extra)
    det = c.child('det')
    C['det'] = blocks(src, det) if det is not None else []
    return C


def blocks(src, det):
    out = []
    for k in det.kids:
        if k.has('dfr'):
            out.append({'k': 'head', 'text': text(src, k)})
        elif k.has('refs'):
            items = []
            for li in k.find(lambda n: n.tag == 'ol').kids:
                rn = li.child('rn')
                body = [x for x in li.kids if x is not rn][0]
                if text(src, rn) == 'none' and 'nothing attached' in text(src, body):
                    continue
                rf = body.child('rf')
                it = {'n': text(src, rn)}
                raw = inner(src, body)
                if rf is not None:
                    it['file'] = text(src, rf)
                    raw = src[rf.e:body.ie]
                    raw = re.sub(r'^ &mdash; ', '', raw)
                if raw:
                    it['note_html'] = raw
                items.append(it)
            b = {'k': 'refs', 'items': items}
            t = text(src, k.child('r-lbl'))
            if t != 'Attached, in this order':
                b['title'] = t
            if k.has('vid'):
                b['vid'] = True
            out.append(b)
        elif k.has('prompt'):
            ph = k.child('p-head')
            out.append({'k': 'prompt', 'label': text(src, ph.child('p-lbl')), 'meta': text(src, ph.child('p-n')),
                        'text': text(src, k.find(lambda n: n.has('p-text')))})
        elif k.has('dsplit'):
            out.append({'k': 'split'})
        elif k.has('alts'):
            rows = []
            for r in k.kids:
                if not r.has('row'):
                    continue
                th = r.child('th')
                media = th.find(lambda n: n.has('vfac') or n.has('mimg'))
                why = r.child('why')
                b_ = why.child('b')
                if media is None or media.has('lost') or b_ is None or text(src, b_) != os.path.basename(media_path(media)):
                    rows.append({'html': src[r.s:r.e]})
                    continue
                rows.append({'media': media_path(media), 'why_html': src[b_.e:why.ie]})
            b = {'k': 'alts', 'rows': rows}
            t = text(src, k.child('r-lbl'))
            if t != f'Other takes on disk ({len(rows)})':
                b['title'] = t
            out.append(b)
        elif k.has('notes'):
            lbl = k.child('r-lbl')
            b = {'k': 'notes', 'html': src[lbl.e:k.ie]}
            if text(src, lbl) != 'Notes from the round':
                b['title'] = text(src, lbl)
            out.append(b)
        elif k.has('learn'):
            lbl = k.child('r-lbl')
            b = {'k': 'learn', 'title': text(src, lbl), 'html': src[lbl.e:k.ie]}
            out.append(b)
        elif k.has('arch'):
            out.append({'k': 'arch', 'html': inner(src, k)})
        else:
            out.append({'k': 'html', 'html': src[k.s:k.e]})
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    if not args:
        print(__doc__)
        return 1
    ps = [d for d in sorted(os.listdir(ROOT)) if ' - ' in d and args[0].upper() == d.upper()] or \
         [d for d in sorted(os.listdir(ROOT)) if ' - ' in d and args[0].upper() in d.upper()]
    if len(ps) != 1:
        print('need exactly one product, matched: ' + str(ps))
        return 1
    p = ps[0]
    src = open(os.path.join(ROOT, p, 'video_board.html'), encoding='utf-8').read()
    D = extract(src)
    D = {'schema': D.pop('schema'), 'product': p, **D}
    n = sum(len(g['cards']) for L in D['lanes'] for g in L['groups'])
    print(f'{p}: {len(D["lanes"])} lanes, {n} cards read back')
    if '--write' in sys.argv:
        out = os.path.join(ROOT, p, DATA_REL)
        if os.path.exists(out) and '--force' not in sys.argv:
            print(f'{out} exists - pass --force to replace it')
            return 1
        txt = json.dumps(D, ensure_ascii=False, indent=1) + '\n'
        open(out, 'w', encoding='utf-8').write(txt)
        if open(out, encoding='utf-8').read() != txt:
            print('write verification FAILED')
            return 1
        print('written ' + out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
