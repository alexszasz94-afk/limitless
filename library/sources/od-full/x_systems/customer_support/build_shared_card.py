#!/usr/bin/env python3
"""Build the shareable Customer Support System page from the kit.

Reads x_systems/customer_support/kit/*.md (the generic kit - no personal data) and
writes ONE self-contained page in the boards' look (dotted canvas, lanes, cards, light
and dark): x_systems_shared/customer_support/customer_support.html, published as the
"Customer Support System" claude.ai artifact (see x_systems_shared/CLAUDE.md).

Every word of the kit is on the page, and the page can copy the whole kit (or any file,
or any section) as markdown so a partner can paste it into their own AI.

Usage: python3 build_shared_card.py <ORGANIC DROPSHIPPING root> <out file> [snapshot date]
Write <out file> to ~ first, then cp onto the drive and compare md5sum (the mount truncates).
Needs the python-markdown package (pip install markdown) - not in the standard library.
Deterministic: the same kit + date + markdown version gives the same bytes.
"""
import sys, os, re, html, json
try:
    import markdown            # pip install markdown  (python-markdown; not in the standard library)
except ImportError:
    raise SystemExit("this tool needs the python-markdown package: pip install markdown")

root, out = sys.argv[1], sys.argv[2]
date = sys.argv[3] if len(sys.argv) > 3 else '2026-10-05'
kit = os.path.join(root, 'x_systems/customer_support/kit')
ORDER = ['README.md', 'SETUP.md', 'REPLYING.md', 'INBOX_PASS.md', 'STORES_TEMPLATE.md']
src = {f: open(os.path.join(kit, f), encoding='utf-8').read().replace('\r\n', '\n') for f in ORDER}

PRIVATE = re.compile(r'thexmasglow|merryglow|xmas ?glow|daniel|Label_\d', re.I)
for f, t in src.items():
    m = PRIVATE.search(t)
    if m:
        raise SystemExit(f'{f}: personal value in the kit ({m.group(0)!r}) - fix the kit first')


# ---------------------------------------------------------------- markdown
def escape_placeholders(t):
    """Prose is full of <placeholder>s. Outside code (fences and `spans`, which markdown escapes
    itself) a bare <Owner> would reach the page as an HTML tag and vanish - escape it."""
    out, fence = [], False
    item = re.compile(r'^\s*(?:[-*+]|\d+\.) ')
    for line in t.split('\n'):
        prev = out[-1] if out else ''
        if (not fence and item.match(line) and prev.strip() and not prev[:1].isspace()
                and not item.match(prev) and not prev.startswith(('#', '|'))):
            out.append('')        # a list straight after a paragraph line: markdown needs a blank line
        if line.lstrip().startswith('```'):
            fence = not fence
            out.append(line)
            continue
        if fence:
            out.append(line)
            continue
        line = re.sub(r'^ {2,3}(?=(?:[-*+]|\d+\.) )', '    ', line)   # nested list: markdown needs 4 spaces
        parts = line.split('`')
        for i in range(0, len(parts), 2):
            parts[i] = parts[i].replace('<', '&lt;').replace('>', '&gt;')
        out.append('`'.join(parts))
    return '\n'.join(out)


PH = re.compile(r'(&lt;[A-Za-z][^&<>\n]{0,60}?&gt;)')


def mark_placeholders(h):
    # only in text, never inside a tag
    parts = re.split(r'(<[^>]+>)', h)
    return ''.join(p if p.startswith('<') else PH.sub(r'<span class="ph">\1</span>', p) for p in parts)


def boxes(h):
    """**Check:** paragraphs -> green box, **Trap(s)...** paragraphs (+ the list after) -> red box."""
    h = re.sub(r'<p><strong>(Check[^<]*?):?</strong>\s*(.*?)</p>',
               lambda m: f'<div class="box chk"><span class="b-lbl">{m.group(1).rstrip(":")}</span><p>{m.group(2)}</p></div>',
               h, flags=re.S)
    h = re.sub(r'<p><strong>(Traps?[^<]*?):?</strong>\s*(.*?)</p>(\s*<ul>.*?</ul>)?',
               lambda m: (f'<div class="box trap"><span class="b-lbl">{m.group(1).rstrip(":")}</span>'
                          + (f'<p>{m.group(2)}</p>' if m.group(2).strip() else '') + (m.group(3) or '') + '</div>'),
               h, flags=re.S)
    return h


def md(t):
    h = markdown.markdown(escape_placeholders(t), extensions=['tables', 'fenced_code'])
    h = h.replace('<table>', '<div class="tw"><table>').replace('</table>', '</table></div>')
    return mark_placeholders(boxes(h))


def sections(text):
    """Split a kit file on '## ' headings (outside code fences). Returns [(title, body)]; the text
    before the first '## ' comes first with title None (its '# ' title line removed)."""
    out, title, buf, fence = [], None, [], False
    for line in text.split('\n'):
        if line.lstrip().startswith('```'):
            fence = not fence
        if not fence and line.startswith('## '):
            out.append((title, '\n'.join(buf)))
            title, buf = line[3:].strip(), []
        else:
            buf.append(line)
    out.append((title, '\n'.join(buf)))
    first = out[0][1].split('\n')
    if first and first[0].startswith('# '):
        first = first[1:]
    out[0] = (None, '\n'.join(first))
    # the '---' rules that separate sections in the files are not content
    clean = lambda b: re.sub(r'(?:^\s*---\s*\n)+|(?:\n\s*---\s*)+$', '', b.strip('\n')).strip('\n')
    return [(t, clean(b)) for t, b in out if t or b.strip()]


def esc(t):
    return html.escape(t, quote=True)


def kb(t):
    return f'{len(t.encode("utf-8")) / 1024:.1f} KB'


# ---------------------------------------------------------------- copy data
SECS = []          # markdown source of every section, for the per-card Copy buttons


def sec_id(md_text):
    SECS.append(md_text)
    return f's:{len(SECS) - 1}'


STARTER = ("Set up this customer support system for my Shopify store(s). Read README.md first, then follow "
           "SETUP.md from Phase 0 to Phase 7, in order, and run every check. Ask me only for what you cannot "
           "find yourself, and tell me which steps are mine.")

BRIEF = ("You were given the CUSTOMER SUPPORT KIT to set up a branded support email and an AI-drafted support "
         "inbox for YOUR owner's Shopify store(s). Nothing in it belongs to anyone else: every <placeholder> is "
         "filled with your owner's own values, which you ask them for in Phase 0. Read README.md first (what the "
         "system is, the tools you need, the rules - they outrank convenience), then follow SETUP.md Phase 0 to 7 "
         "in order, running every check and reporting what it showed. Hand your owner the steps that are theirs "
         "(2-Step Verification, the App Password, the Gmail popup, publishing the theme, the test email, approving "
         "the scheduled task). Save these files where your owner keeps their work, copy STORES_TEMPLATE.md to "
         "stores.md and record everything there. INBOX_PASS.md is the scheduled task that drafts replies once a "
         "day; REPLYING.md is how customers are answered.")

ALL = ('# Customer support kit (complete: 5 files)\n\n' + BRIEF + '\n\n'
       'Save each file below under its own name in a folder called customer_support/, '
       'then start with README.md.\n\n'
       + '\n\n'.join(f'======== FILE {i + 1}/5: customer_support/{f} ========\n\n{src[f].strip()}\n\n======== END OF {f} ========'
                     for i, f in enumerate(ORDER)) + '\n')

# the inbox pass prompt: everything between the two '---' lines after its heading
ip = src['INBOX_PASS.md']
pm = re.search(r'## The prompt[^\n]*\n+---\n(.*)\n---\s*$', ip, re.S)
if not pm:
    raise SystemExit('INBOX_PASS.md: could not find the prompt between the --- lines')
PROMPT = pm.group(1).strip('\n')

# ---------------------------------------------------------------- cards
def card(title, body_html, copy_key, *, eyebrow, cid, size='', idx=None, extra=''):
    num = f'<span class="idx">{esc(idx)}</span>' if idx is not None else ''
    return (f'<article class="card {size}" id="{cid}">'
            f'<header class="card-h">{num}<div class="ct"><span class="eyebrow">{eyebrow}</span>'
            f'<h3>{esc(title)}</h3></div>'
            f'<button class="copy" type="button" data-copy="{copy_key}" title="Copy this section as markdown">'
            f'<span class="lbl">Copy</span></button></header>{extra}'
            f'<div class="md sel">{body_html}</div></article>')


def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:40]


FLOW = '''<div class="flow sel" aria-label="How the mail flows">
<div class="fl"><span class="fl-k">Inbound</span><div class="fl-c">
<span class="nd">Customer</span><i class="ar">writes to</i><span class="nd hi">support@<span class="ph">&lt;domain&gt;</span></span>
<i class="ar">Shopify email forwarding</i><span class="nd"><span class="ph">&lt;inbox&gt;</span> Gmail</span>
<i class="ar">Gmail filter</i><span class="nd">label <span class="ph">&lt;STORE&gt;</span> · never Spam</span></div></div>
<div class="fl"><span class="fl-k">Outbound</span><div class="fl-c">
<span class="nd">Owner presses Send</span><i class="ar">Gmail “Send mail as”</i><span class="nd">smtp.gmail.com : 587 : TLS · App Password</span>
<i class="ar">delivered</i><span class="nd hi">From: <span class="ph">&lt;Brand&gt;</span> &lt;support@<span class="ph">&lt;domain&gt;</span>&gt;</span></div></div>
<div class="fl"><span class="fl-k">Shopify emails</span><div class="fl-c">
<span class="nd">Order confirmation, shipping updates</span><i class="ar">Sender = support@, domain authenticated</i><span class="nd">Customer</span>
<i class="ar">any reply</i><span class="nd hi">support@<span class="ph">&lt;domain&gt;</span> → inbox</span></div></div>
<div class="fl"><span class="fl-k">Storefront</span><div class="fl-c">
<span class="nd">Theme: <code>mailto:{{ shop.email }}</code></span><span class="nd">Pages &amp; policies: support@ written out</span><span class="nd">Contact form → Store email</span></div></div>
<div class="fl"><span class="fl-k">Every day</span><div class="fl-c">
<span class="nd hi">Scheduled inbox pass</span><i class="ar">labels + researches in Shopify</i><span class="nd">1 draft per customer per topic</span>
<i class="ar">only when needed</i><span class="nd">Push report to the owner</span></div></div>
</div>'''

OWNER = {  # what the owner does in each phase (from SETUP.md Phase 0 step 6)
    '0': ['answers the setup questions', 'signs the inbox into Chrome if needed'],
    '1': [],
    '2': ['turns on 2-Step Verification', 'creates the App Password', 'fills the Gmail popup'],
    '3': ['says yes before the Store email changes'],
    '4': ['publishes the theme copy'],
    '5': ['sends the test email', 'checks the From line'],
    '6': ['confirms the Store facts', 'approves the scheduled task'],
    '7': ['sends the drafts from now on'],
}
WIDE = {'What the AI needs', 'Rules — these outrank convenience', 'Labels', 'Troubleshooting',
        'One reply per customer per topic', 'How a reply is written'}

lanes = []

# --- 00 the system (README)
cards = []
for t, b in sections(src['README.md']):
    title = t or 'What it is'
    body = md(b)
    size = 'wide' if title in WIDE else ''
    if title == 'How the mail flows':
        body = FLOW + '<details class="ascii"><summary>The same, as text</summary>' + body + '</details>'
        size = 'xwide'
    raw = (f'## {t}\n\n' if t else '') + b
    cards.append(card(title, body, sec_id(raw), eyebrow='README.md', cid='system-' + slug(title), size=size))
rules_n = len(re.findall(r'^\d+\. \*\*', src['README.md'].split('## Rules')[1].split('\n## ')[0], re.M))
lanes.append(dict(id='system', n='00', file='README.md', color='sys', name='The system',
                  desc='What it is, how the mail flows, which tools the AI needs, and the rules that outrank convenience.',
                  meta=[('Rules', str(rules_n)), ('Inbox', '1 for every store'), ('Address', 'support@domain')],
                  cards=cards))

# --- 01 setup
cards, checks, owner_n, phases = [], 0, 0, 0
for t, b in sections(src['SETUP.md']):
    raw = (f'## {t}\n\n' if t else '') + b
    body = md(b)
    checks += body.count('class="box chk"')
    m = re.match(r'Phase (\d+) — (.*)', t or '')
    if m:
        phases += 1
        n, title = m.group(1), m.group(2)
        who = OWNER.get(n, [])
        owner_n += len(who)
        extra = ('<div class="who"><span class="w-k">Owner</span>' + ''.join(f'<span class="w-o">{esc(w)}</span>' for w in who) + '</div>'
                 if who else '<div class="who"><span class="w-k">Owner</span><span class="w-ai">nothing: the AI does this phase</span></div>')
        size = 'wide' if n in ('2', '4') else ''
        cards.append(card(title, body, sec_id(raw), eyebrow=f'SETUP.md · Phase {n}', cid=f'setup-phase-{n}',
                          size=size, idx=n, extra=extra))
    else:
        title = t or 'Placeholders'
        size = 'wide' if (title in WIDE or title == 'Placeholders') else ''
        cards.append(card(title, body, sec_id(raw), eyebrow='SETUP.md', cid='setup-' + slug(title), size=size))
labels_block = re.search(r'### 6a.*?```\n(.*?)```', src['SETUP.md'], re.S).group(1)
labels = [x for x in re.split(r'\s{2,}|\n', labels_block) if x.strip()]
lanes.append(dict(id='setup', n='01', file='SETUP.md', color='setup', name='Set up one store',
                  desc='Phase 0 to 7, in order. Every phase ends with a check the AI actually runs, and the steps that need the owner are marked.',
                  meta=[('Phases', str(phases)), ('Checks', str(checks)), ('Owner steps', str(owner_n))],
                  cards=cards))

# --- 02 replying
cards = []
for t, b in sections(src['REPLYING.md']):
    title = t or 'Before you answer'
    raw = (f'## {t}\n\n' if t else '') + b
    cards.append(card(title, md(b), sec_id(raw), eyebrow='REPLYING.md', cid='replying-' + slug(title),
                      size='wide' if title in WIDE else ''))
lanes.append(dict(id='replying', n='02', file='REPLYING.md', color='reply', name='Answering customers',
                  desc='How mail is labelled and how every reply is written, by the inbox pass or by hand. One reply per customer per topic, never one per email.',
                  meta=[('Gmail labels', f'{len(labels)} + 1 per store'), ('Replies sent by AI', '0'), ('Drafts', '1 per customer per topic')],
                  cards=cards))

# --- 03 inbox pass
cards = []
for t, b in sections(ip[:ip.index('\n## The prompt')]):
    title = t or 'What each run does'
    raw = (f'## {t}\n\n' if t else '') + b
    cards.append(card(title, md(b), sec_id(raw), eyebrow='INBOX_PASS.md', cid='pass-' + slug(title),
                      size='wide' if title == 'What each run does' else ''))
ptext = mark_placeholders(esc(PROMPT))
ptext = re.sub(r'^(## [^\n]*)$', r'<b class="ph-h">\1</b>', ptext, flags=re.M)
cards.append(f'''<article class="card prompt" id="pass-prompt">
<header class="card-h"><div class="ct"><span class="eyebrow">INBOX_PASS.md · the scheduled task</span><h3>The prompt</h3></div>
<button class="copy strong" type="button" data-copy="prompt"><span class="lbl">Copy prompt</span></button></header>
<p class="lead">Fill in every highlighted <span class="ph">&lt;placeholder&gt;</span>, then schedule it once a day (SETUP.md Phase 6). The prompt is the pass's whole memory: every new fact, price, store or “don't answer this person” goes into it. {len(PROMPT):,} characters.</p>
<div class="ptext sel">{ptext}</div></article>''')
lanes.append(dict(id='pass', n='03', file='INBOX_PASS.md', color='pass', name='The daily inbox pass',
                  desc='A Claude scheduled task that labels everything, looks every customer up in Shopify and leaves one ready-to-send draft. It never sends.',
                  meta=[('Runs', 'once a day'), ('Looks back', '14 days + Spam'), ('Emails sent', '0')],
                  cards=cards))

# --- 04 record
st = src['STORES_TEMPLATE.md']
st_body = st.split('\n', 1)[1] if st.startswith('# ') else st
cards = [card('stores.md template', md(st_body), sec_id(st), eyebrow='STORES_TEMPLATE.md', cid='record-template', size='xwide')]
lanes.append(dict(id='record', n='04', file='STORES_TEMPLATE.md', color='rec', name='The record',
                  desc='Copy it to stores.md. One section per store: read it before touching anything, update it after every change, with the date.',
                  meta=[('Sections', 'inbox + 1 per store'), ('Updated', 'after every change')],
                  cards=cards))


def toc(cards):
    items = []
    for c in cards:
        cid = re.search(r'id="([^"]+)"', c).group(1)
        title = re.search(r'<h3>(.*?)</h3>', c).group(1)
        n = re.search(r'<span class="idx">(.*?)</span>', c)
        num = f'<span class="tn">{n.group(1)}</span>' if n else '<span class="tn dot"></span>'
        items.append(f'<li><button type="button" data-go="{cid}">{num}<span class="tt">{title}</span></button></li>')
    return ''.join(items)


def lane_html(L):
    meta = ''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in L['meta'])
    return (f'<section class="lane" id="{L["id"]}" style="--a:var(--c-{L["color"]})">'
            f'<div class="lane-h"><span class="lane-n">{L["n"]} · {esc(L["file"])}</span><h2>{esc(L["name"])}</h2>'
            f'<p>{esc(L["desc"])}</p><dl class="meta">{meta}</dl>'
            f'<nav class="toc" aria-label="In this lane"><span class="toc-k">In this lane · {len(L["cards"])} cards</span><ol>{toc(L["cards"])}</ol></nav>'
            f'<button class="copy" type="button" data-copy="f:{L["file"]}"><span class="lbl">Copy {esc(L["file"])}</span></button></div>'
            f'<div class="cards">{"".join(L["cards"])}</div></section>')


legend = ''.join(f'<button class="lg" type="button" data-go="{L["id"]}" style="--a:var(--c-{L["color"]})"><b></b>{L["n"]} {esc(L["name"])}</button>'
                 for L in lanes)
filechips = ''.join(f'<button class="fchip" type="button" data-copy="f:{f}"><span class="lbl">{f}</span><em>{kb(src[f])}</em></button>'
                    for f in ORDER)
total_kb = kb(ALL)

DATA = json.dumps({'all': ALL, 'starter': STARTER, 'prompt': PROMPT, 'files': src, 'secs': SECS},
                  ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

CSS = r'''
/* Layout: the boards' dotted canvas. A title, a row of three playbook cards, then one lane per kit
   file, read left to right. Under 820px the canvas becomes a normal scrolling page. */
:root{
 --bg:#f2f2ef;--dot:#dcdcd5;--surface:#fff;--surface-2:#fbfbf9;--sunk:#f6f6f2;--line:#e7e7e2;--line-2:#eeeeea;
 --ink:#15171a;--ink-2:#2a2b2e;--body:#4f4f49;--muted:#8b8b85;--faint:#a5a59f;--code:#f1f1ec;
 --ok:#2f7a52;--ok-bg:#f4faf5;--ok-line:#d5e9da;
 --warn:#b0431a;--warn-bg:#fdf6f4;--warn-line:#f3ddd8;
 --own:#8a5a0b;--own-bg:#fdf5e0;--own-line:#f0dfb1;
 --ph:#5b3fb5;--ph-bg:#f1edfc;
 --c-sys:#4338CA;--c-setup:#2D6BF0;--c-reply:#1F9D6B;--c-pass:#8A4FD1;--c-rec:#B45309;
 --btn:#15171a;--btn-ink:#fff;--sel:#cfd9ff;
 --shadow:0 1px 2px rgba(20,20,10,.05);--shadow-2:0 2px 6px rgba(20,20,10,.05),0 18px 44px rgba(20,20,10,.08);
 --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;
 --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --bg:#181a1d;--dot:#363b43;--surface:#1f2126;--surface-2:#1c1e22;--sunk:#1a1c20;--line:#34373f;--line-2:#2d3036;
 --ink:#e1e3e8;--ink-2:#d4d7dc;--body:#b3b8c2;--muted:#8f96a3;--faint:#7f8693;--code:#16181b;
 --ok:#7acca0;--ok-bg:#18221d;--ok-line:#28473a;
 --warn:#ec8f6b;--warn-bg:#271a16;--warn-line:#55301f;
 --own:#e3c36d;--own-bg:#251f10;--own-line:#5b4c22;
 --ph:#c3b2f5;--ph-bg:#2a2340;
 --c-sys:#8b93f0;--c-setup:#6f9bf5;--c-reply:#4fc79a;--c-pass:#b38be6;--c-rec:#f0a05a;
 --btn:#e1e3e8;--btn-ink:#15171a;--sel:#2b3a6b;
 --shadow:0 1px 2px rgba(0,0,0,.25);--shadow-2:0 2px 6px rgba(0,0,0,.2),0 18px 44px rgba(0,0,0,.3);color-scheme:dark}}
:root[data-theme="dark"]{
 --bg:#181a1d;--dot:#363b43;--surface:#1f2126;--surface-2:#1c1e22;--sunk:#1a1c20;--line:#34373f;--line-2:#2d3036;
 --ink:#e1e3e8;--ink-2:#d4d7dc;--body:#b3b8c2;--muted:#8f96a3;--faint:#7f8693;--code:#16181b;
 --ok:#7acca0;--ok-bg:#18221d;--ok-line:#28473a;
 --warn:#ec8f6b;--warn-bg:#271a16;--warn-line:#55301f;
 --own:#e3c36d;--own-bg:#251f10;--own-line:#5b4c22;
 --ph:#c3b2f5;--ph-bg:#2a2340;
 --c-sys:#8b93f0;--c-setup:#6f9bf5;--c-reply:#4fc79a;--c-pass:#b38be6;--c-rec:#f0a05a;
 --btn:#e1e3e8;--btn-ink:#15171a;--sel:#2b3a6b;
 --shadow:0 1px 2px rgba(0,0,0,.25);--shadow-2:0 2px 6px rgba(0,0,0,.2),0 18px 44px rgba(0,0,0,.3);color-scheme:dark}

*{box-sizing:border-box}
html,body{height:100%;overflow:hidden}
body{margin:0;font:14px/1.5 var(--sans);color:var(--ink);background:var(--bg);-webkit-font-smoothing:antialiased;
 user-select:none;-webkit-user-select:none;-webkit-tap-highlight-color:transparent}
::selection{background:var(--sel)}
button{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--c-setup);outline-offset:2px}
.sel{user-select:text;-webkit-user-select:text;cursor:text}

#vp{position:fixed;inset:0;overflow:hidden;cursor:grab;touch-action:none;
 background-image:radial-gradient(var(--dot) 1px,transparent 1px);background-size:32px 32px}
#vp.drag{cursor:grabbing}
#world{position:absolute;top:0;left:0;transform-origin:0 0;padding:70px 90px 120px 70px;width:max-content}
#vp.moving #world{will-change:transform}

/* ---------- title ---------- */
.title{max-width:1180px;margin:0 0 34px}
.kicker{font-size:11px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--c-sys)}
.title h1{font-size:44px;line-height:1.05;letter-spacing:-.03em;font-weight:760;margin:10px 0 0;text-wrap:balance}
.title h1 span{display:block;color:var(--muted);font-size:21px;line-height:1.35;font-weight:600;letter-spacing:-.01em;margin-top:10px;max-width:980px}
.legend{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}
.lg{display:inline-flex;align-items:center;gap:8px;background:var(--surface);border:1px solid var(--line);border-radius:999px;
 padding:6px 14px;font-size:12px;font-weight:650;color:var(--body);cursor:pointer;transition:border-color .13s,color .13s}
.lg b{width:8px;height:8px;border-radius:50%;background:var(--a)}
.lg:hover{border-color:var(--a);color:var(--ink)}
.stats{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.stats span{font:11.5px var(--mono);color:var(--muted);background:var(--sunk);border:1px solid var(--line);border-radius:6px;padding:4px 9px;font-variant-numeric:tabular-nums}
.stats b{color:var(--ink);font-weight:700}

/* ---------- playbook row ---------- */
.pbrow{display:flex;gap:22px;align-items:stretch;margin:0 0 88px;width:1520px}
.pb{flex:1 1 0;min-width:0;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:22px 24px;box-shadow:var(--shadow)}
.pb.give{flex:1.25 1 0;border-top:4px solid var(--btn);box-shadow:var(--shadow-2)}
.pb h3{margin:0 0 12px;font-size:12px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;color:var(--muted)}
.pb.give h3{color:var(--ink)}
.pb p{margin:0 0 12px;font-size:13px;line-height:1.6;color:var(--body)}
.pb p b{color:var(--ink)}
.big{display:flex;align-items:center;gap:12px;width:100%;border:0;border-radius:12px;background:var(--btn);color:var(--btn-ink);
 padding:13px 16px;cursor:pointer;text-align:left;transition:transform .12s,background .15s}
.big:hover{transform:translateY(-1px)}
.big .lbl{font-size:15px;font-weight:750;letter-spacing:-.01em}
.big em{margin-left:auto;font:11.5px var(--mono);font-style:normal;opacity:.7}
.big.ok{background:#1f9d6b;color:#fff}
.fchips{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0 16px}
.fchip{display:inline-flex;align-items:baseline;gap:7px;background:var(--sunk);border:1px solid var(--line);border-radius:7px;padding:5px 9px;cursor:pointer}
.fchip .lbl{font:600 11.5px var(--mono);color:var(--ink)}
.fchip em{font:10.5px var(--mono);font-style:normal;color:var(--faint)}
.fchip:hover{border-color:var(--ink)}
.fchip.ok{background:#1f9d6b;border-color:#1f9d6b}.fchip.ok .lbl,.fchip.ok em{color:#fff}
.starter{border:1px solid var(--line);border-radius:10px;background:var(--surface-2);padding:11px 12px}
.starter .s-h{display:flex;align-items:center;gap:8px;margin-bottom:6px}
.starter .s-k{font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.starter .copy{margin-left:auto}
.starter p{margin:0;font-size:12.5px;line-height:1.55;color:var(--ink-2)}
.steps{list-style:none;counter-reset:st;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.steps li{counter-increment:st;position:relative;padding-left:30px;font-size:13px;line-height:1.55;color:var(--body)}
.steps li::before{content:counter(st);position:absolute;left:0;top:2px;width:20px;height:20px;border-radius:6px;background:var(--btn);color:var(--btn-ink);
 font-size:11px;font-weight:750;display:flex;align-items:center;justify-content:center}
.steps b{color:var(--ink)}
.brief{background:color-mix(in srgb,var(--c-sys) 7%,var(--surface));border-color:color-mix(in srgb,var(--c-sys) 24%,var(--line))}
.brief h3{color:var(--c-sys)}
.brief p{color:var(--ink-2)}
.keys{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px;padding-top:14px;border-top:1px solid var(--line-2)}
.keys span{font:11px var(--mono);color:var(--muted);background:var(--sunk);border:1px solid var(--line);border-radius:6px;padding:3px 8px}
.keys kbd{font:inherit;color:var(--ink);font-weight:700}
.legend2{display:flex;flex-direction:column;gap:7px;margin-top:4px}
.legend2 div{display:flex;align-items:center;gap:9px;font-size:12.5px;color:var(--body)}
.sw{flex:none;width:30px;height:16px;border-radius:4px;border:1px solid}
.sw.c{background:var(--ok-bg);border-color:var(--ok-line)}
.sw.t{background:var(--warn-bg);border-color:var(--warn-line)}
.sw.o{background:var(--own-bg);border-color:var(--own-line)}
.sw.p{background:var(--ph-bg);border-color:transparent}

/* ---------- how it works ---------- */
.how{width:1520px;margin:0 0 26px;padding:26px 30px 24px;border-radius:18px;background:var(--surface);
 border:1px solid var(--line);border-top:4px solid var(--c-sys);box-shadow:var(--shadow-2)}
.how-h h2{margin:8px 0 0;font-size:28px;line-height:1.15;letter-spacing:-.025em;font-weight:770;text-wrap:balance}
.how-steps{list-style:none;margin:24px 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:34px}
.how-steps li{position:relative;min-width:0}
.how-steps li+li::before{content:"→";position:absolute;left:-26px;top:7px;font-size:18px;font-weight:700;color:var(--faint)}
.hn{display:flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:10px;
 background:color-mix(in srgb,var(--c-sys) 12%,var(--surface));color:var(--c-sys);font-size:16px;font-weight:800;margin-bottom:12px}
.how-steps li.you .hn{background:var(--btn);color:var(--btn-ink)}
.how-steps b{display:block;font-size:16px;line-height:1.3;font-weight:740;letter-spacing:-.01em;color:var(--ink)}
.how-steps p{margin:6px 0 0;font-size:13.5px;line-height:1.55;color:var(--body)}
.mono{font:600 12.5px var(--mono);color:var(--ink);overflow-wrap:anywhere}
.how-f{margin:22px 0 0;padding-top:16px;border-top:1px solid var(--line-2);font-size:13.5px;color:var(--body)}
.how-f b{color:var(--ink)}

/* ---------- lanes ---------- */
.lane{display:flex;gap:26px;align-items:flex-start;margin-bottom:90px}
.lane-h{flex:0 0 300px;width:300px;position:relative;padding:18px 20px 20px;border-radius:16px;
 background:color-mix(in srgb,var(--a) 8%,var(--surface));border:1px solid color-mix(in srgb,var(--a) 26%,var(--line));
 border-top:4px solid var(--a);box-shadow:var(--shadow)}
.lane-n{display:block;font:800 11px var(--mono);letter-spacing:.06em;color:var(--a)}
.lane-h h2{margin:8px 0 8px;font-size:26px;line-height:1.1;letter-spacing:-.028em;font-weight:780;text-wrap:balance}
.lane-h p{margin:0 0 14px;font-size:13px;line-height:1.55;color:var(--body)}
.meta{margin:0 0 14px;border-radius:10px;padding:1px 11px;background:var(--surface);border:1px solid color-mix(in srgb,var(--a) 18%,var(--line))}
.meta>div{display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-bottom:1px solid var(--line-2)}
.meta>div:last-child{border-bottom:0}
.meta dt{font-size:12px;color:var(--muted);font-weight:600}
.meta dd{margin:0;font-size:12px;font-weight:700;text-align:right;font-variant-numeric:tabular-nums}
.toc{margin:0 0 14px}
.toc-k{display:block;margin:0 0 6px;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.toc ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1px}
.toc button{display:flex;align-items:baseline;gap:9px;width:100%;text-align:left;background:none;border:0;border-radius:7px;
 padding:5px 7px;margin-left:-7px;cursor:pointer;font-size:12.5px;line-height:1.35;color:var(--ink-2)}
.toc button:hover{background:color-mix(in srgb,var(--a) 12%,transparent);color:var(--ink)}
.tn{flex:none;width:16px;font:700 11px var(--mono);color:var(--a);text-align:right}
.tn.dot::before{content:"";display:inline-block;width:5px;height:5px;border-radius:50%;background:var(--a);opacity:.7;vertical-align:middle;margin-right:3px}
.tt{min-width:0}
.cards{display:flex;gap:18px;align-items:flex-start}

/* ---------- cards ---------- */
.card{flex:0 0 430px;width:430px;background:var(--surface);border:1px solid var(--line);border-radius:13px;padding:16px 18px 18px;box-shadow:var(--shadow)}
.card.wide{flex-basis:580px;width:580px}
.card.xwide{flex-basis:700px;width:700px}
.card.prompt{flex-basis:1040px;width:1040px;border-top:4px solid var(--a);box-shadow:var(--shadow-2)}
.card-h{display:flex;gap:11px;align-items:flex-start;padding-bottom:12px;margin-bottom:12px;border-bottom:1px solid var(--line-2)}
.idx{flex:none;width:26px;height:26px;border-radius:8px;background:var(--a);color:var(--surface);font-size:13px;font-weight:780;
 display:flex;align-items:center;justify-content:center;margin-top:2px;font-variant-numeric:tabular-nums}
.ct{flex:1;min-width:0}
.eyebrow{display:block;font:700 10.5px var(--mono);letter-spacing:.04em;color:var(--a)}
.card h3{margin:3px 0 0;font-size:16px;line-height:1.3;font-weight:720;letter-spacing:-.012em;text-wrap:balance}
.copy{flex:none;font-size:10.5px;font-weight:750;letter-spacing:.04em;background:var(--surface);color:var(--muted);
 border:1px solid var(--line);border-radius:6px;padding:4px 10px;cursor:pointer;transition:border-color .13s,color .13s}
.copy:hover{border-color:var(--ink);color:var(--ink)}
.copy.strong{background:var(--btn);color:var(--btn-ink);border-color:var(--btn);padding:6px 12px;font-size:11.5px}
.copy.ok,.copy.strong.ok{background:#1f9d6b;border-color:#1f9d6b;color:#fff}
.lane-h .copy{display:block;width:100%;padding:8px 10px;font-size:12px;color:var(--ink);border-color:color-mix(in srgb,var(--a) 30%,var(--line))}
.lane-h .copy:hover{border-color:var(--a)}
.lane-h .copy.ok{color:#fff}
.who{display:flex;flex-wrap:wrap;align-items:center;gap:5px;margin:0 0 12px}
.w-k{font-size:9.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--own);margin-right:3px}
.w-o{white-space:nowrap;font-size:11px;font-weight:650;color:var(--own);background:var(--own-bg);border:1px solid var(--own-line);border-radius:5px;padding:2px 7px}
.w-ai{font-size:11px;font-weight:600;color:var(--muted)}
.lead{margin:0 0 12px;font-size:12.5px;line-height:1.55;color:var(--body)}

/* ---------- the kit's text ---------- */
.md{font-size:13px;line-height:1.62;color:var(--ink-2);overflow-wrap:anywhere}
.md>:first-child{margin-top:0}
.md>:last-child{margin-bottom:0}
.md p{margin:0 0 10px}
.md h3{margin:20px 0 8px;font-size:13.5px;font-weight:760;color:var(--ink);padding-top:12px;border-top:1px dashed var(--line)}
.md h4{margin:16px 0 6px;font-size:13px;font-weight:740;color:var(--ink)}
.md ul,.md ol{margin:0 0 12px;padding-left:20px}
.md li{margin:4px 0}
.md li>p{margin:0 0 4px}
.md strong{color:var(--ink);font-weight:700}
.md a{color:var(--c-setup)}
.md code{font:11.8px var(--mono);background:var(--code);border:1px solid var(--line);border-radius:4px;padding:0 4px;overflow-wrap:anywhere}
.md pre{margin:0 0 12px;padding:11px 13px;background:var(--surface-2);border:1px solid var(--line);border-radius:9px;
 font:11.5px/1.6 var(--mono);color:var(--ink-2);white-space:pre-wrap;overflow-wrap:anywhere}
.md pre code{background:none;border:0;padding:0;font:inherit}
.tw{overflow-x:auto;margin:0 0 12px;border:1px solid var(--line-2);border-radius:9px}
.md table{border-collapse:collapse;width:100%;font-size:12.3px;overflow-wrap:normal}
.md td code{overflow-wrap:normal;word-break:normal}
.md th,.md td{text-align:left;vertical-align:top;padding:6px 9px;border-bottom:1px solid var(--line-2)}
.md tr:last-child td{border-bottom:0}
.md th{font-size:10px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);background:var(--surface-2)}
.ph{color:var(--ph);background:var(--ph-bg);border-radius:4px;padding:0 2px;font-weight:600}
.md code .ph{padding:0}
.box{margin:12px 0;border-radius:9px;padding:10px 12px;border:1px solid}
.box p{margin:0}
.box ul{margin:4px 0 0}
.b-lbl{display:block;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px}
.chk{background:var(--ok-bg);border-color:var(--ok-line)}
.chk .b-lbl{color:var(--ok)}
.trap{background:var(--warn-bg);border-color:var(--warn-line)}
.trap .b-lbl{color:var(--warn)}

/* mail flow */
.flow{display:flex;flex-direction:column;gap:10px;margin:0 0 14px}
.fl{display:flex;gap:12px;align-items:flex-start;padding:10px 12px;border:1px solid var(--line-2);border-radius:10px;background:var(--surface-2)}
.fl-k{flex:0 0 92px;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--a);padding-top:5px}
.fl-c{flex:1;min-width:0;display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.nd{font-size:12px;font-weight:650;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:7px;padding:4px 8px}
.nd.hi{border-color:color-mix(in srgb,var(--a) 45%,var(--line));background:color-mix(in srgb,var(--a) 7%,var(--surface))}
.nd code{font:11px var(--mono)}
.ar{font:10.5px var(--mono);font-style:normal;color:var(--muted);white-space:nowrap}
.ar::before{content:"→ "}
.ar::after{content:" →"}
.ascii summary{cursor:pointer;font-size:12px;font-weight:700;color:var(--muted);padding:4px 0;list-style:none}
.ascii summary::-webkit-details-marker{display:none}
.ascii summary::before{content:"+ "}
.ascii[open] summary::before{content:"− "}
.ascii pre{white-space:pre;overflow-x:auto;overflow-wrap:normal;margin-top:8px;font-size:11px}

/* the prompt */
.ptext{font:12px/1.65 var(--mono);color:var(--ink-2);white-space:pre-wrap;overflow-wrap:anywhere;background:var(--surface-2);
 border:1px solid var(--line);border-radius:10px;padding:16px 18px}
.ph-h{display:inline-block;color:var(--a);font-weight:800;margin-top:6px}

.foot{margin-top:10px;font:11px var(--mono);color:var(--faint);max-width:1100px;line-height:1.7}

/* ---------- chrome ---------- */
#zoom{position:fixed;bottom:calc(18px + env(safe-area-inset-bottom,0px));right:18px;display:flex;align-items:center;gap:2px;
 background:color-mix(in srgb,var(--surface) 92%,transparent);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
 border:1px solid var(--line);border-radius:12px;padding:5px;box-shadow:0 4px 18px rgba(0,0,0,.08);z-index:10}
#zoom button{font-size:13px;font-weight:700;color:var(--body);background:none;border:0;border-radius:8px;min-width:32px;height:30px;padding:0 8px;cursor:pointer}
#zoom button:hover{background:var(--sunk);color:var(--ink)}
#zl{font:11px var(--mono);color:var(--muted);min-width:44px;text-align:center;font-variant-numeric:tabular-nums}
#zoom .sep{width:1px;height:18px;background:var(--line);margin:0 3px}
#hint{transition:opacity .4s;position:fixed;bottom:calc(20px + env(safe-area-inset-bottom,0px));left:18px;font-size:11.5px;color:var(--muted);z-index:10;
 background:color-mix(in srgb,var(--bg) 85%,transparent);padding:5px 10px;border-radius:8px}

#cpx{position:fixed;inset:0;z-index:50;display:flex;align-items:center;justify-content:center;padding:24px;background:rgba(12,12,14,.55)}
#cpx[hidden]{display:none}
.cpx-b{width:min(760px,100%);background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:var(--shadow-2)}
.cpx-b p{margin:0 0 10px;font-size:13px;color:var(--body)}
.cpx-b textarea{width:100%;height:46vh;resize:vertical;font:11.5px/1.5 var(--mono);color:var(--ink-2);background:var(--surface-2);
 border:1px solid var(--line);border-radius:9px;padding:10px;user-select:text;-webkit-user-select:text}
.cpx-f{display:flex;justify-content:flex-end;margin-top:10px}
.cpx-f button{border:0;border-radius:8px;background:var(--btn);color:var(--btn-ink);font-weight:700;padding:8px 14px;cursor:pointer}

/* ---------- phone / narrow: a normal scrolling page ---------- */
@media (max-width:820px){
 html,body{height:auto;overflow:auto}
 body{user-select:text;-webkit-user-select:text}
 #vp{position:static;overflow:visible;cursor:auto;touch-action:auto;background-size:24px 24px}
 #world{position:static;transform:none!important;width:auto;padding:28px 16px 90px}
 .title h1{font-size:34px}.title h1 span{font-size:17px}
 .pbrow{flex-direction:column;width:auto;margin-bottom:56px}
 .lane{flex-direction:column;gap:14px;margin-bottom:56px}
 .lane-h{width:auto;flex:none;align-self:stretch}
 .cards{flex-direction:column;gap:14px;width:100%}
 .card,.card.wide,.card.xwide,.card.prompt{flex:none;width:100%;min-width:0}
 .how{width:auto;padding:22px 18px}
 .how-h h2{font-size:22px}
 .how-steps{grid-template-columns:1fr;gap:18px}
 .how-steps li{display:grid;grid-template-columns:34px 1fr;column-gap:12px}
 .how-steps li .hn{grid-row:span 2;margin:0}
 .how-steps li+li::before{display:none}
 #hint,#zoom .zc{display:none}
 .fl{flex-direction:column;gap:6px}.fl-k{flex:none;padding:0}
 .ptext{padding:12px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
'''

JS = r'''
(()=>{
const D=JSON.parse(document.getElementById('kitdata').textContent);
const vp=document.getElementById('vp'),w=document.getElementById('world'),zl=document.getElementById('zl');
const narrow=matchMedia('(max-width:820px)'),reduced=matchMedia('(prefers-reduced-motion:reduce)');
let x=0,y=0,s=1,anim=0,mt=0;
const MIN=.06,MAX=2.2;
function apply(){if(narrow.matches){w.style.transform='';return}
 w.style.transform='translate3d('+x+'px,'+y+'px,0) scale('+s+')';zl.textContent=Math.round(s*100)+'%'}
const hint=document.getElementById('hint');
function moving(){if(hint)hint.style.opacity='0';vp.classList.add('moving');clearTimeout(mt);mt=setTimeout(()=>vp.classList.remove('moving'),180)}
function zoomAt(f,cx,cy){const ns=Math.min(MAX,Math.max(MIN,s*f)),k=ns/s;x=cx-(cx-x)*k;y=cy-(cy-y)*k;s=ns;apply()}
function go(nx,ny,ns){cancelAnimationFrame(anim);if(reduced.matches){x=nx;y=ny;s=ns;apply();return}
 const x0=x,y0=y,s0=s,t0=performance.now();moving();
 const st=t=>{let p=Math.min(1,(t-t0)/440);p=1-Math.pow(1-p,3);x=x0+(nx-x0)*p;y=y0+(ny-y0)*p;s=s0+(ns-s0)*p;apply();
  if(p<1){anim=requestAnimationFrame(st);moving()}};anim=requestAnimationFrame(st)}
function pos(el){let l=0,t=0;while(el&&el!==w){l+=el.offsetLeft;t+=el.offsetTop;el=el.offsetParent}return{l,t}}
function home(){go(0,0,1)}
function fit(){const W=w.offsetWidth,H=w.offsetHeight,ns=Math.max(MIN,Math.min(innerWidth/W,innerHeight/H)*.97);
 go((innerWidth-W*ns)/2,Math.max(0,(innerHeight-H*ns)/2),ns)}
function focusEl(el){if(!el)return;if(narrow.matches){el.scrollIntoView({behavior:reduced.matches?'auto':'smooth',block:'start'});return}
 const p=pos(el),ns=Math.min(1,Math.max(.5,s));go(48-p.l*ns,48-p.t*ns,ns)}
// wheel: scroll pans, Ctrl/Cmd + scroll (or a trackpad pinch) zooms
vp.addEventListener('wheel',e=>{if(narrow.matches)return;e.preventDefault();cancelAnimationFrame(anim);moving();
 const m=e.deltaMode===1?18:e.deltaMode===2?innerHeight:1;
 if(e.ctrlKey||e.metaKey){zoomAt(Math.exp(-e.deltaY*m*.0024),e.clientX,e.clientY)}
 else if(e.shiftKey&&!e.deltaX){x-=e.deltaY*m;apply()}
 else{x-=e.deltaX*m;y-=e.deltaY*m;apply()}},{passive:false});
// drag to pan (text blocks stay selectable with a mouse); two fingers pinch
const pts=new Map();let last=null,pinch=null;
vp.addEventListener('pointerdown',e=>{if(narrow.matches)return;
 if(e.target.closest('button,a,input,textarea,summary,select'))return;
 if(e.pointerType==='mouse'&&e.button===0&&e.target.closest('.sel'))return;
 if(e.pointerType==='mouse'&&e.button>1)return;
 cancelAnimationFrame(anim);pts.set(e.pointerId,{x:e.clientX,y:e.clientY});vp.setPointerCapture(e.pointerId);
 if(pts.size===1){last={x:e.clientX,y:e.clientY};vp.classList.add('drag')}
 if(pts.size===2){const [a,b]=[...pts.values()];pinch={d:Math.hypot(a.x-b.x,a.y-b.y),s0:s}}
 e.preventDefault()});
vp.addEventListener('pointermove',e=>{if(!pts.has(e.pointerId))return;pts.set(e.pointerId,{x:e.clientX,y:e.clientY});moving();
 if(pts.size>=2&&pinch){const [a,b]=[...pts.values()],d=Math.hypot(a.x-b.x,a.y-b.y),cx=(a.x+b.x)/2,cy=(a.y+b.y)/2;
  zoomAt((pinch.s0*d/pinch.d)/s,cx,cy);return}
 if(last){x+=e.clientX-last.x;y+=e.clientY-last.y;last={x:e.clientX,y:e.clientY};apply()}});
function up(e){pts.delete(e.pointerId);if(pts.size<2)pinch=null;
 if(pts.size===1){const [a]=[...pts.values()];last={x:a.x,y:a.y}}else if(!pts.size){last=null;vp.classList.remove('drag')}}
vp.addEventListener('pointerup',up);vp.addEventListener('pointercancel',up);
// keys: 0 fit all, 1 home, + / - zoom, arrows pan
addEventListener('keydown',e=>{if(narrow.matches||e.target.closest('input,textarea')||e.ctrlKey||e.metaKey||e.altKey)return;
 const k=e.key,cx=innerWidth/2,cy=innerHeight/2;
 if(k==='0')fit();else if(k==='1')home();else if(k==='+'||k==='=')zoomAt(1.2,cx,cy);else if(k==='-'||k==='_')zoomAt(1/1.2,cx,cy);
 else if(k==='ArrowLeft'){x+=120;apply()}else if(k==='ArrowRight'){x-=120;apply()}
 else if(k==='ArrowUp'){y+=120;apply()}else if(k==='ArrowDown'){y-=120;apply()}else return;e.preventDefault()});
document.getElementById('zin').onclick=()=>zoomAt(1.2,innerWidth/2,innerHeight/2);
document.getElementById('zout').onclick=()=>zoomAt(1/1.2,innerWidth/2,innerHeight/2);
document.getElementById('zfit').onclick=fit;document.getElementById('zhome').onclick=home;
document.querySelectorAll('[data-go]').forEach(b=>b.addEventListener('click',()=>focusEl(document.getElementById(b.dataset.go))));
// theme: the viewer's own choice, else the system setting
const tb=document.getElementById('ztheme'),R=document.documentElement;
function dark(){const t=R.getAttribute('data-theme');return t?t==='dark':matchMedia('(prefers-color-scheme:dark)').matches}
function label(){tb.textContent=dark()?'Light':'Dark'}
try{const t=localStorage.getItem('cs.theme');if(t)R.setAttribute('data-theme',t)}catch(_){}
label();matchMedia('(prefers-color-scheme:dark)').addEventListener('change',label);
tb.onclick=()=>{const t=dark()?'light':'dark';R.setAttribute('data-theme',t);try{localStorage.setItem('cs.theme',t)}catch(_){}label()};
// copy
const cpx=document.getElementById('cpx'),cta=cpx.querySelector('textarea');
function text(k){if(k==='all')return D.all;if(k==='starter')return D.starter;if(k==='prompt')return D.prompt;
 if(k.slice(0,2)==='f:')return D.files[k.slice(2)];if(k.slice(0,2)==='s:')return D.secs[+k.slice(2)];return''}
function done(b){const l=b.querySelector('.lbl')||b,o=l.dataset.o||l.textContent;l.dataset.o=o;l.textContent='Copied';b.classList.add('ok');
 clearTimeout(b._t);b._t=setTimeout(()=>{l.textContent=o;b.classList.remove('ok')},1700)}
function fallback(t,b){cta.value=t;cpx.hidden=false;cta.focus();cta.select();
 try{if(document.execCommand('copy')){done(b)}}catch(_){}}
document.addEventListener('click',e=>{const b=e.target.closest('[data-copy]');if(!b)return;e.preventDefault();
 const t=text(b.dataset.copy);
 try{navigator.clipboard.writeText(t).then(()=>done(b),()=>fallback(t,b))}catch(_){fallback(t,b)}});
cpx.querySelector('button').onclick=()=>{cpx.hidden=true};
cpx.addEventListener('click',e=>{if(e.target===cpx)cpx.hidden=true});
addEventListener('keydown',e=>{if(e.key==='Escape')cpx.hidden=true});
// start: a deep link (#setup, #setup-phase-2 ...) or home
narrow.addEventListener('change',apply);
// the browser scrolls a hidden-overflow box to a #link or a focused control: the canvas moves by transform only
vp.addEventListener('scroll',()=>{if(!narrow.matches&&(vp.scrollTop||vp.scrollLeft)){vp.scrollTop=0;vp.scrollLeft=0}});
function fromHash(){const h=decodeURIComponent(location.hash.slice(1)),el=h&&document.getElementById(h);
 if(el){vp.scrollTop=0;vp.scrollLeft=0;requestAnimationFrame(()=>focusEl(el));return true}return false}
addEventListener('hashchange',fromHash);
if(!fromHash())apply();
})();
'''

page = f'''<title>Customer Support System</title>
<meta name="description" content="The complete customer support system for a Shopify store: a branded support address, one Gmail inbox for every store, and a daily AI pass that drafts every reply.">
<style>{CSS}</style>
<div id="vp"><div id="world">

<header class="title" id="top">
<span class="kicker">Shared system · Customer support</span>
<h1>Customer Support System<span>One branded support address per store, every customer email read in one Gmail inbox, and an AI that drafts every reply once a day. Built and run on a live Shopify store with hundreds of orders.</span></h1>
<nav class="legend" aria-label="Lanes">{legend}</nav>
<div class="stats"><span><b>5</b> files</span><span><b>{phases}</b> setup phases</span><span><b>{checks}</b> checks</span><span><b>{rules_n}</b> rules</span><span><b>{len(labels)}</b> Gmail labels + 1 per store</span><span><b>1</b> scheduled task</span><span><b>0</b> emails sent by the AI</span></div>
</header>

<section class="how" id="how-it-works" aria-label="How it works">
<div class="how-h"><span class="kicker">How it works</span><h2>Customers email your store. The AI writes the answers. You press Send.</h2></div>
<ol class="how-steps">
<li><span class="hn">1</span><b>A customer emails your store</b><p>They write to <span class="mono">support@yourstore.com</span>, your store's own address.</p></li>
<li><span class="hn">2</span><b>It lands in your Gmail</b><p>Mail from all your stores arrives in one inbox, labelled by store, never in Spam.</p></li>
<li><span class="hn">3</span><b>The AI writes the replies</b><p>Once a day it reads every email, checks the order in Shopify and leaves a ready answer as a draft.</p></li>
<li class="you"><span class="hn">4</span><b>You press Send</b><p>The customer gets the reply from <span class="mono">support@yourstore.com</span>. The AI never sends anything itself.</p></li>
</ol>
<p class="how-f"><b>Set it up once</b> with your AI: 8 phases, in the lanes below. <b>After that</b>, your only job is step 4.</p>
</section>

<section class="pbrow" aria-label="Start here">
<div class="pb give">
<h3>Give it to your AI</h3>
<p>The copied text is the <b>complete kit</b>: all five files, word for word, ready to paste into a chat. A link alone may only give an AI a summary, so paste the text.</p>
<button class="big" type="button" data-copy="all"><span class="lbl">Copy the full kit</span><em>5 files · {total_kb}</em></button>
<div class="fchips" aria-label="Copy one file">{filechips}</div>
<div class="starter"><div class="s-h"><span class="s-k">Then send this</span><button class="copy" type="button" data-copy="starter"><span class="lbl">Copy</span></button></div>
<p class="sel">{esc(STARTER)}</p></div>
</div>
<div class="pb">
<h3>How to set it up</h3>
<ol class="steps">
<li><b>Connect the tools</b> in Claude: the Gmail and Shopify connectors, Claude in Chrome signed in to Shopify admin and Gmail, and scheduled tasks.</li>
<li><b>Copy the full kit</b> and paste it into a new chat, then send the message under it.</li>
<li><b>Answer the Phase 0 questions</b>: store, domain, the one inbox, the display name, the sign-off, the time zone.</li>
<li><b>Do the owner steps</b> when the AI asks. They are marked <span class="w-o">like this</span> on every phase card.</li>
<li><b>From then on</b>, read each draft and press Send. Tell the AI any new fact so it goes into the prompt.</li>
</ol>
<div class="keys"><span><kbd>drag</kbd> pan</span><span><kbd>scroll</kbd> move</span><span><kbd>Ctrl</kbd>+scroll zoom</span><span><kbd>0</kbd> fit all</span><span><kbd>1</kbd> home</span></div>
</div>
<div class="pb brief">
<h3>For the AI reading this page</h3>
<p class="sel">{mark_placeholders(esc(BRIEF))}</p>
<div class="legend2" aria-label="What the colours mean">
<div><span class="sw c"></span>a check the AI runs before a phase is done</div>
<div><span class="sw t"></span>a trap that happened on the live store</div>
<div><span class="sw o"></span>a step only the owner can do</div>
<div><span class="sw p"></span><span><span class="ph">&lt;placeholder&gt;</span>: filled with the owner's own value</span></div>
</div>
</div>
</section>

{"".join(lane_html(L) for L in lanes)}

<p class="foot">Snapshot {date} · made from the kit files {" · ".join(f"{f} {kb(src[f])}" for f in ORDER)} · every word of the kit is on this page and in “Copy the full kit”.</p>
</div></div>

<div id="hint">Drag to pan · Ctrl + scroll to zoom · 0 fits all</div>
<div id="zoom" role="toolbar" aria-label="View">
<button class="zc" id="zout" type="button" aria-label="Zoom out">−</button><span class="zc" id="zl">100%</span><button class="zc" id="zin" type="button" aria-label="Zoom in">+</button>
<span class="sep zc"></span><button class="zc" id="zfit" type="button">Fit</button><button class="zc" id="zhome" type="button">Home</button>
<span class="sep zc"></span><button id="ztheme" type="button">Dark</button>
</div>
<div id="cpx" hidden><div class="cpx-b" role="dialog" aria-label="Copy">
<p>Your browser blocked automatic copying. The text is selected: press <b>Ctrl+C</b> (<b>⌘C</b> on a Mac).</p>
<textarea id="cpx-t" readonly></textarea><div class="cpx-f"><button type="button">Close</button></div></div></div>
<script type="application/json" id="kitdata">{DATA}</script>
<script>{JS}</script>
'''

# final privacy check on the whole page, embedded data included
m = PRIVATE.search(page)
if m:
    raise SystemExit(f'page: personal value found ({m.group(0)!r}) - not written')
open(out, 'w', encoding='utf-8', newline='\n').write(page)
print(f'wrote {out}: {len(page.encode("utf-8")):,} bytes · {len(lanes)} lanes · '
      f'{sum(len(L["cards"]) for L in lanes)} cards · {len(SECS)} copyable sections · full kit {total_kb}')
