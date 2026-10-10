#!/usr/bin/env python3
"""Regenerate the dark theme at the end of template/board.css.

    python3 x_systems/video_boards/tools/make_dark_css.py
    python3 x_systems/video_boards/tools/make_dark_css.py --page x_systems/hooks/hooks_board.html

The dark theme is not hand-written: every light rule that sets a colour gets a
twin under html[data-theme="dark"] with the colour mapped - neutral surfaces to a
cool slate (page darkest, cards a step lighter, lines lighter still), ink to light
ink, accents keep their hue, dark chips stay dark with white text. Run it
after any colour change in board.css, then rebuild the boards (or with --page
after a colour change in hooks_board.html). Standard library only.
"""
import colorsys, os, re, sys

sys.dont_write_bytecode = True
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(KIT, 'template', 'board.css')
MARK = '/* ---------- dark theme:'
P = 'html[data-theme="dark"]'
COL = re.compile(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]*\)')
SLATE_H, SLATE_S = 0.61, 0.10
# things drawn over photos / video or the black lightbox already work in the dark: keep them
ON_MEDIA = re.compile(r'\.pbtn|#lb|\.lostx')

def parse(c):
    if c.startswith('#'):
        h = c[1:]
        if len(h) == 3: h = ''.join(x*2 for x in h)
        return int(h[0:2],16), int(h[2:4],16), int(h[4:6],16), None
    n = [x.strip() for x in c[c.index('(')+1:-1].split(',')]
    return int(n[0]), int(n[1]), int(n[2]), (float(n[3]) if len(n) > 3 else None)

def fmt(rgb, a=None):
    r,g,b = (max(0,min(255,int(round(v*255)))) for v in rgb)
    return f'#{r:02x}{g:02x}{b:02x}' if a is None else f'rgba({r},{g},{b},{a:g})'

def hls(c):
    r,g,b,a = parse(c); return colorsys.rgb_to_hls(r/255,g/255,b/255), a

def kind(prop):
    if prop.startswith('border') or prop.startswith('outline') or prop in ('background-image',):
        return 'line'
    if prop.startswith('background'): return 'surface'
    if 'shadow' in prop: return 'shadow'
    return 'ink'

def dark(c, prop, ctx):
    (h,l,s), a = hls(c)
    k = kind(prop)
    if a is not None:
        if l > 0.90: return fmt(colorsys.hls_to_rgb(SLATE_H, 0.14, SLATE_S), a)       # frosted white panels
        if l < 0.08: return fmt((0,0,0), min(0.8, a*2.4)) if k == 'shadow' else c     # shadows deeper, overlays same
        return fmt(colorsys.hls_to_rgb(h, min(0.72, l+0.18), s), a)
    if l == 0 and k != 'ink': return c                                                   # black video tiles
    r_, g_, b_, _ = parse(c)
    neutral = (max(r_, g_, b_) - min(r_, g_, b_)) <= 14      # greys, incl. the warm off-whites
    if k == 'ink':
        if l > 0.97:                                     # white text stays white (its chips stay dark or coloured)
            return c
        if l <= 0.30: l2 = 0.90 - l*0.3
        elif neutral: l2 = max(1.02 - l, 0.60)
        else: l2 = max(l, 0.64)
    elif k == 'surface':
        if l >= 0.80: l2 = 0.135 - (1-l)*0.55
        elif l <= 0.30: l2 = 0.27                        # dark ink used as a chip/bar background -> raised slate
        else: l2 = l if not neutral else 1.0 - l
    elif k == 'line':
        if l >= 0.80: l2 = 0.15 + (1-l)*0.72
        elif l <= 0.30: l2 = 0.33
        else: l2 = l if not neutral else max(0.30, 1.0 - l)
    else:
        l2 = l
    if neutral: h, s = SLATE_H, SLATE_S
    elif l >= 0.80 and k in ('surface', 'line'): s = min(s, 0.45)
    return fmt(colorsys.hls_to_rgb(h, max(0, min(1, l2)), s))



def generate(light):
    css_nc = re.sub(r'/\*.*?\*/', '', light, flags=re.S)
    out = []
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', css_nc):
        sel, block = m.group(1).strip(), m.group(2)
        if sel.startswith('@') or sel.startswith(P) or ON_MEDIA.search(sel):
            continue
        items = []
        for d in block.split(';'):
            if ':' in d:
                p, v = d.split(':', 1)
                items.append((p.strip(), v.strip()))
        bg = [v for p, v in items if p in ('background', 'background-color') and COL.search(v)]
        ctx = {}
        if bg:
            (h, l, s), a = hls(COL.search(bg[0]).group(0))
            ctx['bg_neutral_dark'] = (s < 0.2 and l <= 0.30 and a is None)
        decls = [p + ':' + COL.sub(lambda mm, p=p: dark(mm.group(0), p, ctx), v)
                 for p, v in items if COL.search(v) and not p.startswith('--')]
        if not decls:
            continue
        sels = [P + s[4:] if s.startswith('html') else P + ' ' + s
                for s in (x.strip() for x in sel.split(',')) if s != '*']
        if sels:
            out.append(','.join(sels) + '{' + ';'.join(decls) + '}')
    return (MARK + ' made by tools/make_dark_css.py from the rules above; applies when '
            '<html data-theme="dark"> ---------- */\n' + P + '{color-scheme:dark}\n' + '\n'.join(out) + '\n')


def page_mode(path):
    """A standalone page (x_systems/hooks/hooks_board.html): regenerate the dark block inside its <style>.
    Hand-tuned dark rules for that page live in its own CSS, above the generated block."""
    html = open(path, encoding='utf-8').read()
    i = html.index('<style>') + len('<style>'); j = html.index('</style>', i)
    light = html[i:j].split(MARK)[0].rstrip('\n') + '\n'
    new = html[:i] + light + generate(light) + EXTRA + html[j:]
    open(path, 'w', encoding='utf-8').write(new)
    if open(path, encoding='utf-8').read() != new:
        print('write verification failed')
        return 1
    print(f'{os.path.basename(path)}: dark theme regenerated ({new[i:].count(P)} dark rules)')
    return 0


def main():
    if len(sys.argv) > 2 and sys.argv[1] == '--page':
        return page_mode(sys.argv[2])
    css = open(CSS, encoding='utf-8').read()
    light = css.split(MARK)[0].rstrip('\n') + '\n'
    new = light + generate(light) + EXTRA
    open(CSS, 'w', encoding='utf-8').write(new)
    if open(CSS, encoding='utf-8').read() != new:
        print('write verification failed')
        return 1
    print(f'board.css: dark theme regenerated ({new.count(P)} dark rules)')
    return 0


# hand-tuned finishing touches the colour map cannot know about
EXTRA = """html[data-theme="dark"] mark{background:#5a4a0c;color:#fff3c4;box-shadow:0 0 0 1px #8a7414 inset}
html[data-theme="dark"] .mimg,html[data-theme="dark"] .vfac img{filter:brightness(.92)}
html[data-theme="dark"] #zoom #ztheme{min-width:74px}
html[data-theme="dark"] .cell.rl,html[data-theme="dark"] .cell.drw.empty{background:none;border:0;box-shadow:none}
html[data-theme="dark"] .vh{border-top:4px solid var(--a)}
"""

if __name__ == '__main__':
    sys.exit(main())
