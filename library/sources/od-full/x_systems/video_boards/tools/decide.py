#!/usr/bin/env python3
"""Apply Daniel's Approve / Reject lines to the board.

    python3 x_systems/video_boards/tools/decide.py PRODUCT decisions.txt
    python3 x_systems/video_boards/tools/decide.py PRODUCT "APPROVE v18_c02_g1.png" "REJECT v18_c03_g1.mp4 — hands too big"

Each line is exactly what the board copied: `APPROVE <file>` or `REJECT <file> — <reason>`.
The card whose file under review is <file> gets status approved / rejected; a rejection's
reason is added to the card's notes as Daniel's words. Cards that are not waiting for review
are left alone and reported. Rebuilds video_board.html. Nothing is written if any line fails.

After a REJECT, re-roll the take (next take number), then add_card.py ... --replaced "<reason>".
After every frame of a video is APPROVED, animate them (WORKFLOWS.md §5).
A motion-transfer run (stage "refs") is approved on its first reference picture (the woman, vN_cNN_r2.png):
APPROVE means the woman and the room of that run are good to generate with.
"""
import datetime, json, os, re, sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_board as B


def card_file(c):
    if c.get('file'):
        return c['file']
    if c['stage'] == 'clip' and c.get('take'):
        return os.path.basename(c['take']['file'])
    if c['stage'] == 'refs' and c.get('looks'):          # motion transfer: the reference pictures under review
        return os.path.basename(c['looks'][0]['file'])
    return os.path.basename(c['frames'][0]['file']) if c.get('frames') else ''


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    ps = B.products(B.ROOT, sys.argv[1])
    if len(ps) != 1:
        print(f'need exactly one product with a board_data.json, matched {ps}')
        return 1
    prod = ps[0]
    lines = []
    for a in sys.argv[2:]:
        lines += open(a, encoding='utf-8').read().splitlines() if os.path.isfile(a) else [a]
    lines = [l.strip() for l in lines if l.strip()]
    dp = os.path.join(B.ROOT, prod, B.DATA_REL)
    D, seen = B.load_data(dp)
    by_file = {}
    for L in D['lanes']:
        for g in L['groups']:
            for c in g['cards']:
                by_file.setdefault(card_file(c), []).append((L, c))
    bad, done = [], []
    today = datetime.date.today().isoformat()
    for l in lines:
        m = re.match(r'^(APPROVE|REJECT)\s+(\S+)(?:\s+[—-]+\s+(.*))?$', l)
        if not m:
            bad.append(f'not a decision line: {l}')
            continue
        verb, f, why = m.group(1), m.group(2), (m.group(3) or '').strip()
        hits = by_file.get(f, [])
        if len(hits) != 1:
            bad.append(f'{f}: {"no card" if not hits else "several cards"} under review with this file')
            continue
        L, c = hits[0]
        if c['status'] != 'review':
            bad.append(f'{f}: card v{L["n"]} {c["clip"]} is {c["status"]}, not waiting for review - skipped')
            continue
        c['status'] = 'approved' if verb == 'APPROVE' else 'rejected'
        if c.get('take'):
            if verb == 'APPROVE':
                c['take'].pop('label', None)          # back to "Clip in the cut"
            else:
                c['take']['label'] = 'Rejected clip'
        if verb == 'REJECT':
            html = (f'<div class="learn"><span class="r-lbl">Daniel · rejected {B.E(f)} · {today}</span>'
                    f'<p>{B.E(why or "no reason given")}</p></div>')
            det = c.setdefault('det', [])
            at = next((i for i, b in enumerate(det) if b.get('k') == 'arch'), len(det))
            det.insert(at, {'k': 'notes', 'title': 'Daniel\'s review', 'html': html})
        done.append(f'v{L["n"]} {c["clip"]} {f} -> {c["status"]}')
    if bad:
        print('\n'.join(bad))
        if any(not b.endswith('skipped') for b in bad):
            print('nothing written')
            return 1
    if not done:
        print('no card changed - nothing written')
        return 0
    page, ctx = B.build(prod, data=D)
    if ctx.errors:
        print('NOT written:\n' + '\n'.join(ctx.errors))
        return 1
    try:
        B.save_data(dp, D, seen)
        md5 = B.write_verified(os.path.join(B.ROOT, prod, 'video_board.html'), page)
    except B.BoardError as e:
        print(f'NOT written - {e}')
        return 1
    print('\n'.join(done))
    print(f'{prod}: board rebuilt, md5 {md5}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
