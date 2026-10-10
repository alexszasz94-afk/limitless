#!/usr/bin/env python3
"""Build a product's video board from its data file.

    python3 x_systems/video_boards/tools/build_board.py THEX          # one product
    python3 x_systems/video_boards/tools/build_board.py               # every product that has a data file
    python3 x_systems/video_boards/tools/build_board.py THEX --check  # validate only, write nothing
    python3 x_systems/video_boards/tools/build_board.py --example     # render template/example_board.html

Source of truth : <PRODUCT>/content/_board_thumbs/board_data.json
Output          : <PRODUCT>/video_board.html   (never edit this file by hand)
Template        : x_systems/video_boards/template/  (page.html, board.css, board.js)

The data format is documented in x_systems/video_boards/SYSTEM.md.
Standard library only. Exit code 0 = built (or valid), 1 = errors.
"""
import html, json, os, re, sys, hashlib, datetime

sys.dont_write_bytecode = True
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # x_systems/video_boards
ROOT = os.path.dirname(os.path.dirname(KIT))                           # the drive
TPL = os.path.join(KIT, 'template')
DATA_REL = os.path.join('content', '_board_thumbs', 'board_data.json')

E = lambda s: html.escape(str(s), quote=False)
EA = lambda s: html.escape(str(s), quote=True)
DOT = ' &middot; '
CHEV = '<svg class="chev" viewBox="0 0 10 10"><path d="M3 1l4 4-4 4"/></svg>'
STAGES = ('frame', 'clip', 'refs')    # refs: motion transfer, the reference pictures wait for review, nothing generated yet
STATUSES = ('review', 'approved', 'rejected')
LAYOUTS = ('lanes', 'columns')         # columns: one column per motion-transfer run (SYSTEM.md §2.6)
CARD_KEYS = {'clip', 'stage', 'status', 'file', 'title', 'desc', 'tip', 'chip', 'variant',
             'frames', 'driver', 'looks', 'tags', 'take', 'det', 'count_note', 'blocked'}
LANE_KEYS = {'n', 'title', 'caption', 'final', 'meta', 'groups', 'side_note', 'source'}


class BoardError(Exception):
    pass


# ---------------------------------------------------------------- helpers
def thumb(p):
    """poster/thumbnail path for a media file (built by _tool/make_thumbs.py)"""
    return 'content/_board_thumbs/' + os.path.splitext(p)[0] + '.webp'


def take_of(name):
    m = re.search(r'_([gr]\d+)\.\w+$', name or '')
    return m.group(1) if m else ''


class Ctx:
    """per-product state: where files live and which ones are known lost"""

    def __init__(self, base, strict=True, example=False):
        self.base, self.strict, self.example = base, strict, example
        self.errors, self.warnings = [], []
        self.lost = set()
        self.files = None            # every file under the product folder, listed once (see exists)
        p = os.path.join(base, 'content', 'lost_takes.txt')
        if os.path.exists(p):
            self.lost = {l.strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')}

    def exists(self, rel):
        # one directory walk per build instead of one stat per path: on this mount a stat costs
        # a few ms and a board asks for thousands of paths
        if self.files is None:
            self.files = set()
            for d, dirs, fs in os.walk(self.base):
                dirs[:] = [x for x in dirs if x != '_board_thumbs']
                r = os.path.relpath(d, self.base).replace(os.sep, '/')
                for f in fs:
                    self.files.add(f if r == '.' else r + '/' + f)
        rel = rel.replace('\\', '/')
        if rel.startswith('content/_board_thumbs/'):
            return os.path.exists(os.path.join(self.base, rel))
        return rel in self.files

    def is_lost(self, rel):
        n = os.path.basename(rel)
        return n in self.lost or re.sub(r'_g\d+(_g\d+)(\.\w+)$', r'\1\2', n) in self.lost

    def need(self, rel, where):
        """a path the page will load: must exist, or be listed as lost"""
        if not rel:
            return 'none'
        if self.example:
            return 'example'
        if self.exists(rel):
            return 'ok'
        if self.is_lost(rel):
            return 'lost'
        (self.errors if self.strict else self.warnings).append(f'{where}: file not found: {rel}')
        return 'missing'


def img_tag(ctx, p, where, w=480, h=849):
    st = ctx.need(p, where)
    if st == 'example':
        return f'<div class="m-todo">example image<br>{E(os.path.basename(p))}</div>'
    if st == 'lost':        # the thumb survives, the full-resolution file does not
        return f'<img class="mimg" loading="lazy" decoding="async" width="{w}" height="{h}" src="{EA(thumb(p))}" alt="">'
    if st == 'missing':
        return f'<div class="m-todo">missing<br>{E(os.path.basename(p))}</div>'
    return (f'<img class="mimg" loading="lazy" decoding="async" width="{w}" height="{h}" '
            f'src="{EA(thumb(p))}" data-full="{EA(p)}" alt="">')


def vfac(ctx, p, where, final=False, alt='', poster=None):
    st = ctx.need(p, where)
    if st == 'example':
        return f'<div class="m-todo">example clip<br>{E(os.path.basename(p))}</div>'
    cls = 'vfac final' if final else 'vfac'
    img = (f'<img loading="lazy" decoding="async" width="480" height="854" src="{EA(thumb(poster or p))}" alt="{EA(alt)}">')
    if st == 'lost':
        return (f'<span class="{cls} lost" data-lost="{EA(p)}" title="take lost - {EA(os.path.basename(p))}">{img}'
                '<i class="lostx">take lost</i></span>')
    if st == 'missing':
        return f'<div class="m-todo">missing<br>{E(os.path.basename(p))}</div>'
    return f'<button class="{cls}" type="button" data-src="{EA(p)}">{img}<i class="pbtn"></i></button>'


# ---------------------------------------------------------------- dropdown blocks
def refs_html(b):
    lis = []
    for it in b.get('items', []):
        name = it.get('file') or ''
        shown = f'<span class="rf">{E(name)}</span>' if name else ''
        note = it.get('note_html', '')
        body = shown + (' &mdash; ' + note if shown and note else note)
        lis.append(f'<li><span class="rn">{E(it.get("n", ""))}</span><span>{body}</span></li>')
    if not lis:
        lis = ['<li><span class="rn">none</span><span>text-only generation, nothing attached</span></li>']
    return (f'<div class="refs{" vid" if b.get("vid") else ""}"><span class="r-lbl">{E(b.get("title", "Attached, in this order"))}</span>'
            '<ol>' + ''.join(lis) + '</ol></div>')


def prompt_html(b):
    meta = b.get('meta', '')
    return ('<div class="prompt open"><button class="p-head" type="button">' + CHEV +
            f'<span class="p-lbl">{E(b.get("label", "Prompt"))}</span><span class="p-n">{E(meta)}</span>'
            '<span class="copy">Copy</span></button><div class="p-body"><div class="p-text">' +
            E(b['text']) + '</div></div></div>')


def alts_html(ctx, b, where):
    rows = []
    for r in b.get('rows', []):
        if 'html' in r:                       # a pre-rendered row (e.g. a lost take with its thumb)
            rows.append(r['html'])
            continue
        m = r['media']
        th = vfac(ctx, m, where) if m.endswith('.mp4') else img_tag(ctx, m, where)
        rows.append(f'<div class="row"><div class="th">{th}</div><div class="why"><b>{E(os.path.basename(m))}</b>'
                    f'{r.get("why_html", "")}</div></div>')
    title = b.get('title') or f'Other takes on disk ({len(rows)})'
    return f'<div class="alts"><span class="r-lbl">{E(title)}</span>' + ''.join(rows) + '</div>'


def det_html(ctx, blocks, where):
    out = []
    for b in blocks:
        k = b.get('k')
        if k == 'head':
            out.append(f'<span class="dfr">{E(b["text"])}</span>')
        elif k == 'refs':
            out.append(refs_html(b))
        elif k == 'prompt':
            if not (b.get('text') or '').strip():
                ctx.errors.append(f'{where}: empty prompt "{b.get("label", "")}"')
            out.append(prompt_html(b))
        elif k == 'split':
            out.append('<div class="dsplit"></div>')
        elif k == 'alts':
            out.append(alts_html(ctx, b, where))
        elif k == 'notes':
            out.append(f'<div class="notes"><span class="r-lbl">{E(b.get("title", "Notes from the round"))}</span>{b["html"]}</div>')
        elif k == 'learn':
            out.append(f'<div class="learn"><span class="r-lbl">{E(b.get("title", "Note"))}</span>{b["html"]}</div>')
        elif k == 'arch':
            out.append(f'<p class="arch">{b["html"]}</p>')
        elif k == 'html':
            out.append(b['html'])
        else:
            ctx.errors.append(f'{where}: unknown dropdown block kind {k!r}')
    return ''.join(out)


def other_takes(blocks):
    n = 0
    for b in blocks:
        if b.get('k') == 'alts':
            n += len(b.get('rows', []))
    return n


# ---------------------------------------------------------------- card
CHIP = {('frame', 'review'): 'FRAME FOR REVIEW', ('frame', 'approved'): 'FRAME APPROVED',
        ('frame', 'rejected'): 'FRAME REJECTED', ('clip', 'review'): 'CLIP FOR REVIEW',
        ('clip', 'approved'): 'APPROVED', ('clip', 'rejected'): 'REJECTED',
        ('refs', 'review'): 'REFS FOR REVIEW', ('refs', 'approved'): 'REFS APPROVED',
        ('refs', 'rejected'): 'REFS REJECTED'}


def card_core(ctx, lane, c):
    """validate one card (every layout) and work out what the page needs: the shot id, the file under
    review, the status chip. Errors go to ctx.errors - the build then refuses to write the board."""
    n = lane['n']
    where = f'video {n} {c.get("clip")}'
    extra = set(c) - CARD_KEYS
    if extra:
        ctx.errors.append(f'{where}: unknown card field(s) {sorted(extra)}')
    if not re.fullmatch(r'c\d\d', c.get('clip', '')):
        ctx.errors.append(f'{where}: clip id must look like c01, got {c.get("clip")!r}')
    stage, status = c.get('stage'), c.get('status')
    if stage not in STAGES or status not in STATUSES:
        ctx.errors.append(f'{where}: stage/status must be one of {STAGES}/{STATUSES}, got {stage}/{status}')
        stage, status = 'clip', 'approved'
    frames = c.get('frames') or []
    clip = c.get('take')
    driver = c.get('driver')
    looks = c.get('looks') or []
    if stage == 'clip' and not clip:
        ctx.errors.append(f'{where}: stage "clip" needs a "take" (the clip)')
    if driver and (frames or stage == 'frame'):
        ctx.errors.append(f'{where}: "driver" (motion transfer, no start frame) needs stage "refs" or "clip" and no "frames"')
    if stage == 'refs' and (not driver or not looks or clip):
        ctx.errors.append(f'{where}: stage "refs" needs a "driver" and "looks", and no "take" yet')
    if looks and not driver:
        ctx.errors.append(f'{where}: "looks" (character / room pictures) belong to a motion-transfer card with a "driver"')
    for lk in looks:
        if not lk.get('file') or not lk.get('label'):
            ctx.errors.append(f'{where}: every "looks" entry needs a "label" and a "file"')
    file_ = c.get('file') or (os.path.basename(clip['file']) if (stage == 'clip' and clip) else
                              (os.path.basename(frames[0]['file']) if frames else
                               (os.path.basename(looks[0]['file']) if (stage == 'refs' and looks) else '')))
    if not file_:
        ctx.errors.append(f'{where}: no file under review (data-file)')
    # the file under review must be one of the card's own files - a decision line names it
    own = [os.path.basename(f['file']) for f in frames] + ([os.path.basename(clip['file'])] if clip else [])
    if stage == 'refs':
        own += [os.path.basename(lk['file']) for lk in looks if lk.get('file')]
    if c.get('file') and c['file'] not in own:
        ctx.errors.append(f'{where}: "file" {c["file"]!r} is not one of this card\'s files {own}')
    chip = c.get('chip') or CHIP[(stage, status)]
    if not c.get('chip') and stage != 'refs' and take_of(file_):
        chip += ' · ' + take_of(file_)
    return dict(shot=f'v{n}_{c.get("clip")}', where=where, stage=stage, status=status, frames=frames,
                clip=clip, driver=driver, looks=looks, file=file_, own=own, chip=chip)


def card_html(ctx, lane, grp, c, idx_color):
    k = card_core(ctx, lane, c)
    shot, where, stage, status = k['shot'], k['where'], k['stage'], k['status']
    frames, clip, driver, file_, own = k['frames'], k['clip'], k['driver'], k['file'], k['own']
    # every frame and the clip must carry its exact prompt, or an explicit "No ... prompt on record" note
    det_blocks = c.get('det') or []
    labels = ' '.join(b.get('label', '') for b in det_blocks if b.get('k') == 'prompt')
    gaps = ' '.join(b.get('html', '') for b in det_blocks if b.get('k') in ('notes', 'learn'))
    for name in own:
        if not re.search(r'_g\d+\.\w+$', name):
            continue                     # references (r<K>) may be photos - no prompt required
        if name not in labels and 'prompt on record' not in gaps:
            ctx.errors.append(f'{where}: no prompt block for {name} - add the Higgsfield prompt, '
                              'or a "No image/clip prompt on record" note for a historical gap')
    looks = k['looks'] if stage == 'refs' else []
    two = len(frames) > 1 or len(looks) > 1
    chip = k['chip']
    idx = int(c['clip'][1:]) if re.fullmatch(r'c\d\d', c.get('clip', '')) else 0
    h = [f'<article class="card{" two" if two else ""}" data-clip="{EA(c["clip"])}" data-shot="{EA(shot)}" '
         f'data-stage="{stage}" data-status="{status}" data-file="{EA(file_)}"'
         + (f' data-driver="{EA(driver)}"' if driver else '') + '>']
    tip = c.get('tip') or c.get('desc', '')
    chip_html = E(chip).replace(' · ', DOT)
    h.append(f'<header class="card-h"><span class="idx" style="background:{EA(idx_color)}">{idx}</span>'
             f'<div class="card-t" title="{EA(tip)}"><h4>{E(c.get("title", ""))}</h4><p>{E(c.get("desc", ""))}</p></div>'
             f'<span class="fin {status}">{chip_html}</span></header>')
    if c.get('variant'):
        h.append(f'<span class="variant">{E(c["variant"])}</span>')
    # frames
    cols = []
    for i, f in enumerate(frames):
        lbl = f.get('label') or ('START FRAME' if i == 0 else f'FRAME {i + 1}')
        cols.append(f'<div class="m-col"><span class="m-lbl">{E(lbl)}{DOT}{E(os.path.basename(f["file"]))}</span>'
                    + img_tag(ctx, f['file'], where) + '</div>')
    for lk in looks:                   # refs stage in the lanes layout: the reference pictures wait for review
        cols.append(f'<div class="m-col"><span class="m-lbl">{E(lk["label"].upper())}{DOT}{E(os.path.basename(lk["file"]))}</span>'
                    + img_tag(ctx, lk['file'], where) + '</div>')
    if driver:
        ctx.need(driver, where)
    if not cols and driver and clip:   # motion transfer: no start frame. Only OUR generated clip is shown,
        # where the start frame would be (and again in the clip strip below). The driving video is never
        # shown on the card - it is listed in the Prompts drawer's attachments only (Daniel, 2026-09-25).
        ctx.need(driver, where)
        gen = clip.get('play') or clip['file']
        cols.append(f'<div class="m-col"><span class="m-lbl">GENERATED CLIP{DOT}{E(os.path.basename(clip["file"]))}</span>'
                    + vfac(ctx, gen, where, poster=clip.get('poster')) + '</div>')
    if not cols:
        cols.append('<div class="m-col"><span class="m-lbl">START FRAME</span><div class="m-todo">no frame yet</div></div>')
    h.append('<div class="media">' + ''.join(cols) + '</div>')
    # tags
    tags = c.get('tags') or {}
    tb = []
    if tags.get('image'):
        tb.append(f'<span class="tag">{E(tags["image"])}</span>')
    if tags.get('clip'):
        tb.append(f'<span class="tag vid">{E(tags["clip"])}</span>')
    for t in tags.get('extra', []):
        tb.append(f'<span class="tag note">{E(t)}</span>')
    h.append('<div class="tagbar">' + ''.join(tb) + '</div>')
    # clip / review strip
    rv = ('<span class="rv"><button class="rv-b ok" type="button" title="Copy an approval line for Claude">&#10003; Approve</button>'
          '<button class="rv-b no" type="button" title="Copy a rejection line for Claude">&#10007; Reject</button></span>')
    if clip:
        play = clip.get('play') or clip['file']
        if play != clip['file']:
            ctx.need(clip['file'], where)
        info = [f'<span class="c-lbl">{E(clip.get("label", "Clip in the cut"))}</span>',
                f'<span class="c-file">{E(os.path.basename(clip["file"]))}</span>']
        info += [f'<span class="c-2k">{E(x)}</span>' for x in clip.get('info', [])]
        info.append(rv)
        h.append(f'<div class="clipst"><div class="cv">{vfac(ctx, play, where, poster=clip.get("poster"))}</div><div class="cinfo">{"".join(info)}</div></div>')
    else:
        msg = (REFS_TODO if stage == 'refs' else
               {'review': 'Clip comes after this frame is approved', 'approved': 'Frame approved &mdash; clip not made yet',
                'rejected': 'Frame rejected &mdash; next take coming'})[status]
        lbl = ('References for review' if stage == 'refs' else 'Frame for review') if status == 'review' else 'No clip yet'
        h.append(f'<div class="clipst"><div class="cv"><div class="c-todo">{msg}</div></div><div class="cinfo">'
                 f'<span class="c-lbl">{lbl}</span>'
                 f'<span class="c-file">{E(file_)}</span>{rv}</div></div>')
    # dropdown
    det = c.get('det') or []
    if det:
        np_ = sum(1 for b in det if b.get('k') == 'prompt')
        no = other_takes(det)
        dn = [f'{np_} prompt{"s" if np_ != 1 else ""}']
        if no:
            dn.append(f'{no} other take{"s" if no != 1 else ""}')
        if c.get('count_note'):
            dn.append(c['count_note'])
        h.append('<button class="d-head" type="button">' + CHEV + '<span class="d-lbl">Prompts</span>'
                 f'<span class="d-n">{DOT.join(E(x) for x in dn)}</span><span class="d-x"></span></button>')
        h.append('<div class="det">' + det_html(ctx, det, where) + '</div>')
    h.append('</article>')
    return ''.join(h)


# ---------------------------------------------------------------- lane
def plural(n, w):
    return f'{n} {w}{"s" if n != 1 else ""}'


def status_word(cards):
    st = {(c.get('stage'), c.get('status')) for c in cards}
    rv = sum(1 for c in cards if c.get('status') == 'review')
    if rv:
        return f'{rv} for review'
    if st == {('clip', 'approved')}:
        return 'approved'
    if all(c.get('status') == 'approved' for c in cards):
        return 'frames approved'
    return 'in progress'


def lane_html(ctx, L):
    extra = set(L) - LANE_KEYS
    n = L.get('n')
    if extra:
        ctx.errors.append(f'video {n}: unknown lane field(s) {sorted(extra)}')
    allc = [c for g in L['groups'] for c in g['cards']]
    nframes = sum(len(c.get('frames') or []) for c in allc)
    nclips = sum(1 for c in allc if c.get('take'))
    meta = [list(m) for m in L.get('meta', [])]
    if not any(k == 'Shots' for k, _ in meta):
        meta.append(['Shots', f'{plural(nclips, "clip")} · {plural(nframes, "frame")}'])
    side = [f'<aside class="lane-side"><span class="lane-n">Video {n}</span><h2>{E(L["title"])}</h2>']
    if L.get('caption'):
        side.append(f'<p class="lane-hook" title="On-screen text">&ldquo;{E(L["caption"])}&rdquo;</p>')
    fin = L.get('final')
    if fin:
        side.append(vfac(ctx, fin, f'video {n} final', final=True, alt=f'Video {n} final cut'))
    else:
        side.append('<div class="final-todo">Not cut yet</div>')
    side.append('<dl class="meta">' + ''.join(
        f'<div><dt>{E(k)}</dt><dd>{E(v).replace(" · ", DOT)}</dd></div>' for k, v in meta) + '</dl>')
    if L.get('side_note'):
        side.append(f'<p class="lane-note">{L["side_note"]}</p>')
    side.append(f'<span class="lane-file">{E(fin or f"videos_to_post/video_{n}.mp4 - not exported yet")}</span></aside>')
    body = []
    for g in L['groups']:
        cs = g['cards']
        nf = sum(len(c.get('frames') or []) for c in cs)
        ncl = sum(1 for c in cs if c.get('take'))
        cnt = [plural(ncl, 'clip') if ncl else None, plural(nf, 'frame'), status_word(cs)]
        body.append(f'<section class="group" style="--a:{EA(g["color"])}"><header class="group-h"><span class="dot"></span>'
                    f'<span class="g-name">{E(g["name"])}</span><span class="g-sub">{E(g.get("sub", ""))}</span>'
                    f'<span class="g-count">{DOT.join(x for x in cnt if x)}</span></header>'
                    '<div class="cards">' + ''.join(card_html(ctx, L, g, c, g['color']) for c in cs) + '</div></section>')
    return (f'<section class="lane" id="v{n}">' + ''.join(side) + '<div class="lane-body">' + ''.join(body)
            + '</div></section>')


# ---------------------------------------------------------------- columns layout (SYSTEM.md §2.6)
# One column per motion-transfer run, three rows that line up across the whole board:
#   1 the reference reel (the driving video)   2 the new woman + room (the card's "looks")
#   3 the final video (the lane's export, else our generated clip, else what it is waiting for)
# plus the Prompts drawer of every run. The rows are one CSS grid, so they align by construction.
REFS_TODO = {'review': 'Not generated yet &mdash; approve the woman and the room first',
             'approved': 'References approved &mdash; ready to generate',
             'rejected': 'References rejected &mdash; new picks coming'}
ROWS = [('Reference', 'the reel we copy: motion, cuts, timing'),
        ('New woman + room', 'who and where, from the pictures'),
        ('Final video', 'our clip, then the export'),
        ('Prompts', 'exact prompt and attachments')]


def rv_html():
    return ('<span class="rv"><button class="rv-b ok" type="button" title="Copy an approval line for Claude">&#10003; Approve</button>'
            '<button class="rv-b no" type="button" title="Copy a rejection line for Claude">&#10007; Reject</button></span>')


def review_attrs(k):
    return (f' data-shot="{EA(k["shot"])}" data-stage="{k["stage"]}" data-status="{k["status"]}" data-file="{EA(k["file"])}"'
            + (f' data-driver="{EA(k["driver"])}"' if k['driver'] else ''))


def vid_head_html(L, n_runs, color):
    n = L['n']
    src = L.get('source') or {}
    h = [f'<header class="cell vh" id="v{n}" data-vid="{n}" style="grid-column:span {n_runs};--a:{EA(color)}">'
         f'<span class="vh-n">Video {n}{DOT}{plural(n_runs, "run")}</span><h2>{E(L["title"])}</h2>']
    bits = [E(x) for x in (src.get('account'), src.get('views'), src.get('length')) if x]
    if src.get('url'):
        bits.append(f'<a class="vh-a" href="{EA(src["url"])}" target="_blank" rel="noopener">Open reel &#8599;</a>')
    if bits:
        h.append('<p class="vh-src">' + DOT.join(bits) + '</p>')
    if L.get('caption'):
        h.append(f'<p class="vh-cap" title="On-screen text in the reference">&ldquo;{E(L["caption"])}&rdquo;</p>')
    meta = [m for m in L.get('meta', []) if m[0] != 'Shots']
    if meta:
        h.append('<dl class="vh-meta">' + ''.join(f'<div><dt>{E(k)}</dt><dd>{E(v).replace(" · ", DOT)}</dd></div>'
                                                  for k, v in meta) + '</dl>')
    if L.get('side_note'):
        h.append(f'<p class="lane-note">{L["side_note"]}</p>')
    h.append('</header>')
    return ''.join(h)


def ref_cell(ctx, L, c, k):
    where = k['where']
    vid = (vfac(ctx, k['driver'], where, alt=f'Reference for {k["shot"]}') if k['driver']
           else '<div class="m-todo">no reference video</div>')
    return (f'<div class="cell ref" data-col="{EA(k["shot"])}"><div class="c-top"><span class="c-id">{E(c["clip"].upper())}</span>'
            f'<span class="c-t" title="{EA(c.get("tip") or c.get("desc", ""))}">{E(c.get("title", ""))}</span></div>'
            f'{vid}<span class="c-cap">{E(os.path.basename(k["driver"] or ""))}{DOT if c.get("desc") else ""}{E(c.get("desc", ""))}</span></div>')


def look_cell(ctx, L, c, k):
    looks = k['looks']
    figs = ''.join(f'<figure><span class="m-lbl">{E(lk["label"].upper())}</span>{img_tag(ctx, lk["file"], k["where"])}'
                   f'<figcaption>{E(os.path.basename(lk["file"]))}</figcaption></figure>' for lk in looks)
    if not figs:                       # same footprint as a Woman + Room pair, so every card in the row is the same size
        figs = ''.join(f'<figure><span class="m-lbl">{lb}</span><div class="m-todo look-todo">not on record</div>'
                       '<figcaption>&mdash;</figcaption></figure>' for lb in ('WOMAN', 'ROOM'))
        looks = [None, None]
    if k['stage'] == 'refs':           # the pictures are what Daniel reviews right now
        return (f'<div class="cell look" data-col="{EA(k["shot"])}"{review_attrs(k)}>'
                f'<div class="looks" style="--k:{max(1, len(looks))}">{figs}</div>'
                f'<div class="c-foot"><span class="fin {k["status"]}">{E(k["chip"]).replace(" · ", DOT)}</span>{rv_html()}</div></div>')
    return (f'<div class="cell look" data-col="{EA(k["shot"])}"><div class="looks" style="--k:{max(1, len(looks))}">{figs}</div>'
            '<div class="c-foot"><span class="fin approved">REFS APPROVED</span></div></div>')


def out_cell(ctx, L, c, k):
    clip = k['clip']
    if k['stage'] == 'refs' or not clip:
        msg = REFS_TODO[k['status']] if k['stage'] == 'refs' else 'Not generated yet'
        if c.get('blocked'):                   # a run that was submitted but produced no clip (e.g. refused by Higgsfield)
            msg = E(c['blocked'])
        return (f'<div class="cell out" data-col="{EA(k["shot"])}"><div class="c-todo big">{msg}</div>'
                '<span class="c-cap">our clip lands here, then the export</span></div>')
    play = clip.get('play') or clip['file']
    if play != clip['file']:
        ctx.need(clip['file'], k['where'])
    info = ''.join(f'<span class="c-2k">{E(x)}</span>' for x in clip.get('info', []))
    pair = (f'<button class="pair" type="button" data-col="{EA(k["shot"])}" title="Play the reference and our clip together">'
            '&#9654; Side by side with the reference</button>') if k['driver'] else ''
    return (f'<div class="cell out" data-col="{EA(k["shot"])}"{review_attrs(k)}>'
            f'<span class="m-lbl">{E(clip.get("label", "Generated clip").upper())}{DOT}{E(os.path.basename(clip["file"]))}</span>'
            f'{vfac(ctx, play, k["where"], poster=clip.get("poster"))}{pair}<div class="c-info">{info}</div>'
            f'<div class="c-foot"><span class="fin {k["status"]}">{E(k["chip"]).replace(" · ", DOT)}</span>{rv_html()}</div></div>')


def final_cell(ctx, L, n_runs):
    n, fin = L['n'], L['final']
    return (f'<div class="cell out fincell" data-vid="{n}" style="grid-column:span {n_runs}">'
            f'<span class="m-lbl">FINAL VIDEO{DOT}{E(os.path.basename(fin))}</span>'
            f'<div class="fin-w">{vfac(ctx, fin, f"video {n} final", final=True, alt=f"Video {n} final cut")}</div>'
            f'<span class="c-cap">{E(fin)}</span></div>')


def drawer_cell(ctx, L, c, k):
    det = c.get('det') or []
    if not det:
        return f'<div class="cell drw empty" data-col="{EA(k["shot"])}"></div>'
    np_ = sum(1 for b in det if b.get('k') == 'prompt')
    no = other_takes(det)
    dn = [f'{np_} prompt{"s" if np_ != 1 else ""}']
    if no:
        dn.append(f'{no} other take{"s" if no != 1 else ""}')
    if c.get('count_note'):
        dn.append(c['count_note'])
    tags = c.get('tags') or {}
    tb = ''.join(f'<span class="tag{" vid" if t == "clip" else ""}">{E(tags[t])}</span>' for t in ('image', 'clip') if tags.get(t))
    tb += ''.join(f'<span class="tag note">{E(t)}</span>' for t in tags.get('extra', []))
    return (f'<div class="cell drw" data-col="{EA(k["shot"])}">' + (f'<div class="tagbar">{tb}</div>' if tb else '')
            + '<button class="d-head" type="button">' + CHEV + '<span class="d-lbl">Prompts</span>'
            f'<span class="d-n">{DOT.join(E(x) for x in dn)}</span><span class="d-x"></span></button>'
            '<div class="det">' + det_html(ctx, det, k['where']) + '</div></div>')


def columns_html(ctx, lanes):
    runs = []                          # (lane, card, core) in board order: video by video, shot by shot
    for L in lanes:
        extra = set(L) - LANE_KEYS
        if extra:
            ctx.errors.append(f'video {L.get("n")}: unknown lane field(s) {sorted(extra)}')
        for g in L['groups']:
            for c in g['cards']:
                if not c.get('driver'):
                    ctx.errors.append(f'video {L["n"]} {c.get("clip")}: the columns layout shows motion-transfer runs only - '
                                      'every card needs a "driver"')
        for c in sorted((c for g in L['groups'] for c in g['cards']), key=lambda c: c.get('clip', '')):
            runs.append((L, c, card_core(ctx, L, c)))
    by_lane = {}
    for L, c, k in runs:
        by_lane.setdefault(L['n'], []).append((L, c, k))
    color = lambda L: (L['groups'][0].get('color') if L['groups'] else None) or '#5b6472'

    def label(i):
        t, sub = ROWS[i]
        return f'<div class="cell rl"><span class="rl-n">{i + 1 if i < 3 else "&#9776;"}</span><b>{t}</b><span>{sub}</span></div>'
    # a wider gap between videos than between the runs of one video (Daniel, 2026-10-05): the first column of
    # every video but the first is VGAP wider and its cells carry data-vs (margin-left) - the cells keep 324 px
    starts = {id(rs[0][1]) for n_, rs in by_lane.items()} - {id(runs[0][1])} if runs else set()
    def vs(html, on):
        if not on:
            return html
        i = html.index('>')
        return html[:i] + ' data-vs' + html[i:]
    tracks = ' '.join('calc(324px + var(--vgap))' if id(c) in starts else '324px' for L, c, k in runs)
    out = [f'<section class="cgrid" style="--runs:{len(runs)};grid-template-columns:168px {tracks}"><div class="cell rl rl0"></div>']
    for L in lanes:
        if by_lane.get(L['n']):
            out.append(vs(vid_head_html(L, len(by_lane[L['n']]), color(L)), id(by_lane[L['n']][0][1]) in starts))
    out.append(label(0) + ''.join(vs(ref_cell(ctx, L, c, k), id(c) in starts) for L, c, k in runs))
    out.append(label(1) + ''.join(vs(look_cell(ctx, L, c, k), id(c) in starts) for L, c, k in runs))
    out.append(label(2))
    for L in lanes:
        rs = by_lane.get(L['n']) or []
        if not rs:
            continue
        if L.get('final'):
            out.append(vs(final_cell(ctx, L, len(rs)), id(rs[0][1]) in starts))
        else:
            out.append(''.join(vs(out_cell(ctx, L, c, k), id(c) in starts) for L, c, k in rs))
    out.append(label(3) + ''.join(vs(drawer_cell(ctx, L, c, k), id(c) in starts) for L, c, k in runs))
    out.append('</section>')
    return ''.join(out), len(runs)


# ---------------------------------------------------------------- header + panels
HOW = [
    '<b>Notes</b> (left) stay put while you pan and zoom and save themselves as you type. Drag the bottom-right corner to resize; '
    'click the title to fold. Everything is also written into <code>content/_board_thumbs/board_notes.txt</code> &mdash; connect it '
    'once with <b>Connect board_notes.txt</b>; after a Chrome restart one click on the notes reconnects it.',
    '<b>One lane per video</b>, oldest first. Every card = one shot: its start frame, its clip, and under <b>Prompts</b> the exact '
    'image prompt, clip prompt, attachments, other takes and notes.',
    '<b>Two approvals per video.</b> Frames first: <span class="fin review">FRAME FOR REVIEW</span> &rarr; '
    '<span class="fin approved">FRAME APPROVED</span>. Then clips, animated only from approved frames: '
    '<span class="fin review">CLIP FOR REVIEW</span> &rarr; <span class="fin approved">APPROVED</span> '
    '(or <span class="fin rejected">REJECTED</span> &rarr; re-rolled as the next take). Take numbers always match the file name.',
    '<b>Approve / Reject</b> appear only on cards waiting for you. Each click copies one line for Claude; <b>Review</b> '
    '(bottom right) shows only the waiting cards; <b>Copy decisions</b> copies all your lines at once &mdash; paste them to Claude.',
]


HOW_COLUMNS = [
    '<b>Notes</b> (left) stay put while you pan and zoom and save themselves as you type. Drag the bottom-right corner to resize; '
    'click the title to fold. Everything is also written into <code>content/_board_thumbs/board_notes.txt</code> &mdash; connect it '
    'once with <b>Connect board_notes.txt</b>; after a Chrome restart one click on the notes reconnects it.',
    '<b>One column per run</b> (one Genjutsu motion-transfer generation), videos left to right, oldest first. A video split into '
    'two runs has two columns under one heading. Read each column top to bottom: <b>1 Reference</b> &rarr; '
    '<b>2 New woman + room</b> &rarr; <b>3 Final video</b>; the rows line up across the whole board.',
    '<b>Two approvals per run.</b> The references first: <span class="fin review">REFS FOR REVIEW</span> &rarr; '
    '<span class="fin approved">REFS APPROVED</span> &mdash; nothing is generated before that. Then our clip: '
    '<span class="fin review">CLIP FOR REVIEW</span> &rarr; <span class="fin approved">APPROVED</span> '
    '(or <span class="fin rejected">REJECTED</span> &rarr; re-rolled as the next take). <b>&#9654; Side by side</b> plays the '
    'reference and our clip together.',
    '<b>Approve / Reject</b> appear only where something waits for you. Each click copies one line for Claude; <b>Review</b> '
    '(bottom right) dims everything else; <b>Copy decisions</b> copies all your lines at once &mdash; paste them to Claude.',
]


def panels_html(ctx, D):
    how = HOW_COLUMNS if D.get('layout') == 'columns' else HOW
    how = how + [D['source_note_html']] if D.get('source_note_html') else how
    out = ['<div class="rules"><div class="box wide"><h3>How this board works</h3><ul class="plain">'
           + ''.join(f'<li>{x}</li>' for x in how) + '</ul></div>']
    for p in D.get('panels', []):
        t = p.get('type', 'list')
        wide = ' wide' if p.get('wide') else ''
        if t == 'list':
            if not p.get('items_html'):
                continue                      # nothing learned yet - no empty box
            tag = 'ol' if p.get('ordered', True) else 'ul class="plain"'
            end = 'ol' if p.get('ordered', True) else 'ul'
            out.append(f'<div class="box{wide}"><h3>{E(p["title"])}</h3><{tag}>'
                       + ''.join(f'<li>{x}</li>' for x in p['items_html']) + f'</{end}></div>')
        elif t == 'spec':
            img = p['image']
            ctx.need(img, 'panel ' + p['title'])
            rows = ''.join(f'<div><dt>{E(k)}</dt><dd>{v}</dd></div>' for k, v in p.get('rows_html', []))
            out.append(f'<div class="box spec{wide}"><div class="sp-img">{img_tag(ctx, img, "panel", 480, 480)}'
                       f'<span class="cap">{E(img)}</span></div><div class="sp-info">'
                       f'<span class="kicker">{E(p.get("kicker", ""))}</span><h3>{E(p["title"])}</h3>'
                       f'<p class="lead">{p.get("lead_html", "")}</p><dl>{rows}</dl>'
                       + (f'<p class="sp-rules">{p["rules_html"]}</p>' if p.get('rules_html') else '') + '</div></div>')
        elif t == 'gallery':          # a row of reference pictures, e.g. the product photos every prompt attaches
            figs = []
            for it in p.get('items', []):
                f = it['file']
                st = ctx.need(f, 'panel ' + p['title'])
                # product-level pictures have no board thumbnail (make_thumbs covers content/ and videos_to_post/):
                # use the thumb when it exists, else the picture itself, lazily
                src = thumb(f) if ctx.exists(thumb(f)) else f
                im = (f'<img class="mimg" loading="lazy" decoding="async" src="{EA(src)}" data-full="{EA(f)}" alt="">'
                      if st in ('ok', 'lost') else f'<div class="m-todo">{E(os.path.basename(f))}</div>')
                figs.append(f'<figure>{im}<figcaption title="{EA(f)}"><b>{E(it.get("label", ""))}</b>{E(os.path.basename(f))}</figcaption></figure>')
            out.append(f'<div class="box gallery{wide}"><h3>{E(p["title"])}</h3>'
                       + (f'<p class="g-lead">{p["lead_html"]}</p>' if p.get('lead_html') else '')
                       + '<div class="gal">' + ''.join(figs) + '</div></div>')
        elif t == 'specs':
            out.append(f'<div class="box{wide}"><h3>{E(p["title"])}</h3>' + ''.join(
                '<div class="specs">' + ''.join(f'<span>{E(s)}</span>' for s in row) + '</div>' for row in p['rows'])
                + '</div>')
        else:
            ctx.errors.append(f'unknown panel type {t!r}')
    out.append('</div>')
    return ''.join(out)


def header_html(D, lanes):
    cards = [c for L in lanes for g in L['groups'] for c in g['cards']]
    posted = sum(1 for L in lanes if any(k == 'Status' and str(v).startswith('Posted') for k, v in L.get('meta', [])))
    appr = sum(1 for c in cards if c.get('stage') == 'clip' and c.get('status') == 'approved')
    rv = sum(1 for c in cards if c.get('status') == 'review')
    nl = len(lanes)
    cols = D.get('layout') == 'columns'
    parts = [f'{nl} videos posted' if posted == nl and nl else (f'{plural(nl, "video")} &middot; {posted} posted' if posted else plural(nl, 'video'))]
    if cols:
        parts += [plural(len(cards), 'run'), f'{appr} clips approved']
    else:
        parts.append(f'{appr} shots approved')
    if rv:
        parts.append(f'{rv} waiting for review')
    if D.get('subtitle_extra'):
        parts.append(E(D['subtitle_extra']))
    legend = ''.join(f'<i><b style="background:{EA(l["color"])}"></b>{E(l["text"])}</i>' for l in D.get('legend', []))
    if cols:
        note = ('Drag to pan &middot; scroll to move &middot; &#8984;/Ctrl + scroll to zoom &middot; <b>0</b> fit all &middot; '
                '<b>1</b> home &middot; <b>2</b> newest video &middot; <b>E</b> open every Prompts drawer. Each column is one run, read top to bottom: '
                'reference &rarr; new woman + room &rarr; final video. Click a picture for full resolution, a clip to play it. '
                '<b>Approve / Reject</b> copies a one-line decision for Claude; <b>Copy decisions</b> (bottom right) copies all of them at once.')
    else:
        note = ('Drag to pan &middot; scroll to move &middot; &#8984;/Ctrl + scroll to zoom &middot; <b>0</b> fit all &middot; '
                '<b>1</b> home &middot; <b>2</b> newest video &middot; <b>E</b> open every card. Click a frame for full resolution, a clip to play it. '
                '<b>Approve / Reject</b> on a card copies a one-line decision for Claude; <b>Copy decisions</b> (bottom right) copies all of them at once.')
    return (f'<div class="title"><h1>{E(D["brand"])} &mdash; Video Board<span>{DOT.join(parts)}</span></h1>'
            f'<div class="legend">{legend}</div><p class="note">{note}</p></div>')


# ---------------------------------------------------------------- page
def slug(product):
    return re.sub(r'[^a-z0-9]+', '_', product.lower()).strip('_')


def build(product, root=ROOT, strict=True, data=None, example=False):
    base = os.path.join(root, product)
    if data is None:
        p = os.path.join(base, DATA_REL)
        if not os.path.exists(p):
            raise BoardError(f'{product}: no {DATA_REL}')
        data = json.load(open(p, encoding='utf-8'))
    if data.get('schema') != 'video-board/1':
        raise BoardError(f'{product}: board_data.json schema must be "video-board/1"')
    if data.get('product') != product:
        raise BoardError(f'{product}: board_data.json says product {data.get("product")!r}')
    ctx = Ctx(base, strict, example)
    lanes = sorted(data['lanes'], key=lambda L: L['n'])
    ns = [L['n'] for L in lanes]
    if len(set(ns)) != len(ns):
        ctx.errors.append('duplicate video numbers: ' + str(ns))
    for L in lanes:
        seen = set()
        for g in L['groups']:
            for c in g['cards']:
                if c.get('clip') in seen:
                    ctx.errors.append(f'video {L["n"]}: shot {c.get("clip")} appears twice')
                seen.add(c.get('clip'))
    key = data.get('key') or slug(product)
    layout = data.get('layout', 'lanes')
    if layout not in LAYOUTS:
        ctx.errors.append(f'layout must be one of {LAYOUTS}, got {layout!r}')
        layout = 'lanes'
    if layout == 'columns':
        grid, n_runs = columns_html(ctx, lanes)
        # the data rides along inside the page, so extract_board.py can rebuild board_data.json from a columns
        # board exactly (the lanes layout is parsed back from its HTML instead)
        blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
        body = grid + f'\n<script type="application/json" id="board-data">{blob}</script>'
    else:
        body = '\n'.join(lane_html(ctx, L) for L in lanes)
    parts = {
        'TITLE': E(data['brand']) + ' — Video Board',
        'FAVICON': EA(data.get('favicon') or open(os.path.join(TPL, 'favicon.txt'), encoding='utf-8').read().strip()),
        'CSS': open(os.path.join(TPL, 'board.css'), encoding='utf-8').read().strip('\n'),
        'JS': open(os.path.join(TPL, 'board.js'), encoding='utf-8').read().strip('\n'),
        'KEY': EA(key),
        'HEADER': header_html(data, lanes),
        'PANELS': panels_html(ctx, data),
        'LANES': body,
    }
    # dark / light switch on every board: remembered per board, applied before the first paint
    parts['THEME_HEAD'] = ('<script>try{if(localStorage.getItem("vb.theme.' + key + '")==="dark")'
                           'document.documentElement.setAttribute("data-theme","dark")}catch(e){}</script>')
    parts['THEME_BTN'] = '<button class="fit" id="ztheme" type="button" title="Dark / light (D)">Dark</button>'
    page = open(os.path.join(TPL, 'page.html'), encoding='utf-8').read()
    for k, v in parts.items():
        page = page.replace('{{' + k + '}}', v)
    left = re.findall(r'\{\{[A-Z]+\}\}', page)
    if left:
        ctx.errors.append(f'template placeholders not filled: {left}')
    return page, ctx


def write_verified(path, text):
    """write through <path>.building, read it back, then rename it over <path> - this drive's mount
    has truncated writes before. The temporary file is created exclusively: two sessions writing
    the same file at the same time cannot both get it, so the second one stops instead of
    overwriting the first (a crash can leave the file behind - move it to to_delete/ and rerun)."""
    data = text.encode('utf-8')
    tmp = path + '.building'
    try:
        fd = os.open(tmp, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise BoardError(f'{tmp} already exists - another session is writing this file right now, '
                         'or an interrupted run left it behind. Wait, or move it to to_delete/, then rerun.')
    with os.fdopen(fd, 'wb') as f:
        f.write(data)
    if open(tmp, 'rb').read() != data:
        raise BoardError(f'write verification failed for {tmp} - {os.path.basename(path)} was left untouched')
    os.replace(tmp, path)
    if hashlib.md5(open(path, 'rb').read()).hexdigest() != hashlib.md5(data).hexdigest():
        raise BoardError(f'write verification failed for {path}')
    return hashlib.md5(data).hexdigest()


def load_data(dp):
    """board_data.json + a fingerprint of the bytes read, for save_data's lost-update check"""
    raw = open(dp, 'rb').read()
    return json.loads(raw.decode('utf-8')), hashlib.md5(raw).hexdigest()


def save_data(dp, D, seen):
    """write board_data.json only if it is still the version that was read (seen = load_data's
    fingerprint). Two sessions editing the same board: the second one is refused, not lost."""
    if hashlib.md5(open(dp, 'rb').read()).hexdigest() != seen:
        raise BoardError('board_data.json changed since this command read it (another session?) - '
                         'nothing written. Run the command again.')
    return write_verified(dp, json.dumps(D, ensure_ascii=False, indent=1) + '\n')


def products(root, arg=None):
    out = sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and ' - ' in d
                 and os.path.exists(os.path.join(root, d, DATA_REL)))
    if arg:
        exact = [p for p in out if p.upper() == arg.upper()]
        out = exact or [p for p in out if arg.upper() in p.upper()]
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    check_only = '--check' in sys.argv
    if '--example' in sys.argv:
        # render template/example_board_data.json (a made-up product) - shows every card state
        D = json.load(open(os.path.join(TPL, 'example_board_data.json'), encoding='utf-8'))
        page, ctx = build(D['product'], data=D, example=True)
        if ctx.errors:
            print('\n'.join(ctx.errors))
            return 1
        md5 = write_verified(os.path.join(TPL, 'example_board.html'), page)
        print(f'template/example_board.html built - {page.count("<article class=")} cards, md5 {md5}')
        return 0
    root = ROOT
    for a in sys.argv[1:]:
        if a.startswith('--root='):
            root = a.split('=', 1)[1]
    ps = products(root, args[0] if args else None)
    if args and len(ps) > 1:
        print(f'{args[0]!r} matches several products {ps} - give more of the name')
        return 1
    if not ps:
        print('no product with a ' + DATA_REL + (f' matching {args[0]!r}' if args else ''))
        return 1
    bad = 0
    for p in ps:
        try:
            page, ctx = build(p, root)
        except Exception as e:          # one broken board must never stop the others from building
            print(f'{p}: FAILED - {e!r}')
            bad += 1
            continue
        for w in ctx.warnings:
            print('  warning  ' + w)
        if ctx.errors:
            print(f'{p}: {len(ctx.errors)} error(s) - board NOT written')
            for e in ctx.errors[:60]:
                print('  ' + e)
            bad += 1
            continue
        n_cards = page.count('<article class="card')
        runs = page.count('<div class="cell look')
        what = f'{runs} runs (columns layout)' if '<section class="cgrid"' in page else f'{n_cards} cards'
        if check_only:
            print(f'{p}: valid - {what}')
            continue
        try:
            md5 = write_verified(os.path.join(root, p, 'video_board.html'), page)
        except BoardError as e:
            print(f'{p}: NOT written - {e}')
            bad += 1
            continue
        print(f'{p}: video_board.html built - {what}, {len(page.encode())} bytes, md5 {md5}')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
