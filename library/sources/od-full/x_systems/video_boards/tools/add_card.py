#!/usr/bin/env python3
"""Add or update one shot card from the Higgsfield job records - prompts are copied byte for byte.

    python3 x_systems/video_boards/tools/add_card.py PRODUCT --video 18 --shot c02 \\
        --group "B-roll 1" --title "Hands on the box" --desc "Two hands on the carton" \\
        --frame content/video_18_assets/starting_frames/v18_c02_g1.png=/path/image_job.json \\
        [--frame "FRAME 2 · ROOM REFERENCE:content/video_18_assets/references/v18_c02_r1.png=/path/job.json"] \\
        [--clip content/video_18_assets/clips/v18_c02_g1.mp4=/path/video_job.json] \\
        [--driver content/video_18_assets/references/v18_c01_r1.mp4]   (motion transfer: clip, no frame) \\
        [--media <media id>=<path shown for that attachment>] ... \\
        [--status review|approved|rejected] [--replaced "why the previous take lost"] \\
        [--lane-title "Hook name"] [--caption "on-screen text"] [--note "<p>html</p>"]

PRODUCT is a substring of the product folder. A job .json is ONE generation record exactly as
Higgsfield returns it (show_generation_by_ids / job_display): {"id", "model", "params", "results", ...}.

What it does to content/_board_thumbs/board_data.json:
  * creates the lane (video N) and the group when missing
  * writes the card: stage "frame" without --clip, "clip" with it; status review by default
  * the Prompts drawer gets, per frame and for the clip, the attachments in submission order
    and the exact params.prompt of the job, with the settings line and job id
  * if the card already existed and --replaced is given, its previous frame/clip go to
    "Other takes on disk" with that reason (a re-roll after Daniel's REJECT)
  * then it rebuilds video_board.html. Nothing is written when the build finds a problem.
  * without --frame it keeps the card's current frames (and their prompts) - e.g. for the clip round
  * attachment names given once with --media are remembered on the card
  * --driver: a clip made straight from a driving video (Genjutsu motion transfer and the like)
    has no start frame. Give --clip and --driver, no --frame: only our generated clip is shown - where the
    start frame would be (GENERATED CLIP) and again in the clip strip; the driving video is not shown
    on the card, only in the Prompts drawer's attachments; the clip goes straight to CLIP FOR REVIEW - its one
    approval. The driving video must already sit in the shot's references/ as vN_cNN_rK.mp4.
  * refuses: a new take without --replaced; a clip on a frame that is not approved (unless --force)
It never renames, moves or downloads media: put the files in place first (NAMING.md).
"""
import argparse, json, os, re, sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_board as B

GROUP_COLOR = {'hook': '#E8452C', 'b-roll 1': '#2D6BF0', 'b-roll 2': '#1F9D6B'}


def img_settings(r):
    p = r.get('params', {})
    parts = [r.get('model', '')]
    if r.get('model') == 'gpt_image_2_5' and p.get('model'):
        parts.append(p['model'])
    parts += [p.get('aspect_ratio', ''), p.get('resolution', ''), p.get('quality', '')]
    if p.get('width'):
        parts.append(f"{p['width']}×{p['height']}")
    return [str(x) for x in parts if x]


def clip_settings(r):
    p = r.get('params', {})
    out = [r.get('model', '')]
    for k in ('resolution',):
        if p.get(k):
            out.append(str(p[k]))
    if p.get('duration'):
        out.append(f"{p['duration']} s")
    if p.get('aspect_ratio'):
        out.append(p['aspect_ratio'])
    ga = p.get('generate_audio')
    if str(r.get('model', '')).startswith('hf_mult_motion'):
        out.append('sound of the driving video')   # Genjutsu motion transfer copies the reference's audio, whatever generate_audio says
    elif ga is not None:
        out.append('audio on' if str(ga).lower() in ('true', '1') else 'audio off')
    return [x for x in out if x]


def refs(r, kind, media_names):
    items, ni, nv = [], 0, 0
    for m in r.get('params', {}).get('medias') or []:
        role, mid = m.get('role'), m['data']['id']
        if kind == 'image':
            ni += 1
            lab = f'@Image {ni}'
        elif role == 'start_image':
            lab = 'start frame'
        elif role == 'video':
            nv += 1
            lab = f'video ref {nv}'
        else:
            ni += 1
            lab = f'image ref {ni}'
        it = {'n': lab, 'note_html': f'<i>media {mid[:8]}</i>'}
        if mid[:8] in media_names:
            it['file'] = media_names[mid[:8]]
        else:
            it['note_html'] = 'attachment not named on the drive &middot; ' + it['note_html']
        items.append(it)
    return {'k': 'refs', 'items': items, **({'vid': True} if kind == 'clip' else {})}


def probe_size(p):
    try:
        import subprocess
        r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height',
                            '-of', 'csv=p=0:s=x', p], capture_output=True, text=True, timeout=30)
        wh = r.stdout.strip()
        return ' ' + wh.replace('x', '×') if re.fullmatch(r'\d+x\d+', wh) else ''
    except Exception:
        return ''


def load_job(p):
    j = json.load(open(p, encoding='utf-8'))
    if isinstance(j, dict) and 'items' in j:
        j = j['items'][0]
    if isinstance(j, list):
        j = j[0]
    if not j.get('params', {}).get('prompt'):
        raise SystemExit(f'{p}: no params.prompt in this job record')
    return j


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('product')
    ap.add_argument('--video', type=int, required=True)
    ap.add_argument('--shot', required=True)
    ap.add_argument('--group', required=True)
    ap.add_argument('--group-sub', default='')
    ap.add_argument('--title', required=True)
    ap.add_argument('--desc', required=True)
    ap.add_argument('--frame', action='append', default=[])
    ap.add_argument('--clip')
    ap.add_argument('--media', action='append', default=[])
    ap.add_argument('--status', default='review', choices=B.STATUSES)
    ap.add_argument('--replaced')
    ap.add_argument('--lane-title')
    ap.add_argument('--caption')
    ap.add_argument('--note', action='append', default=[])
    ap.add_argument('--driver', help='motion transfer: the driving video (a references/ mp4); card has no start frame')
    ap.add_argument('--force', action='store_true', help='allow --clip on a frame that is not approved yet')
    a = ap.parse_args()
    ps = [p for p in B.products(B.ROOT, a.product)]
    if len(ps) != 1:
        raise SystemExit(f'need exactly one product with a board_data.json, matched {ps}')
    prod = ps[0]
    dp = os.path.join(B.ROOT, prod, B.DATA_REL)
    D, seen = B.load_data(dp)
    shot = a.shot.lower()
    if not re.fullmatch(r'c\d\d', shot):
        raise SystemExit('--shot must look like c01')
    media_names = dict(x.split('=', 1) for x in a.media)
    # the card as it is now (if any): its attachment names and frames carry over
    lane = next((L for L in D['lanes'] if L['n'] == a.video), None)
    old, old_grp = None, None
    for g in (lane['groups'] if lane else []):
        for c in g['cards']:
            if c['clip'] == shot:
                old, old_grp = c, g
    known = {}
    for b in (old or {}).get('det', []):
        if b.get('k') == 'refs':
            for it in b.get('items', []):
                m = re.search(r'media ([0-9a-f]{8})', it.get('note_html', ''))
                if m and it.get('file'):
                    known[m.group(1)] = it['file']
    for mid, f in media_names.items():
        known[mid[:8]] = f
    frames, det = [], []
    for i, spec in enumerate(a.frame):
        label = 'START FRAME' if i == 0 else f'FRAME {i + 1}'
        if ':' in spec.split('=', 1)[0] and not spec.startswith('content/'):
            label, spec = spec.split(':', 1)
        path, job_p = spec.split('=', 1)
        r = load_job(job_p)
        frames.append({'label': label, 'file': path})
        det += [{'k': 'head', 'text': f'{label} — {os.path.basename(path)}'}, refs(r, 'image', known),
                {'k': 'prompt', 'label': f'Image prompt · {os.path.basename(path)}',
                 'meta': ' · '.join(img_settings(r) + [f'job {r["id"][:8]}']), 'text': r['params']['prompt']},
                {'k': 'split'}]
    image_tag = load_job(a.frame[0].split('=', 1)[1])['model'] if a.frame else ''
    driver = a.driver or ((old or {}).get('driver') if not a.frame else None)
    if a.driver:
        if a.frame or not a.clip:
            raise SystemExit('--driver goes with --clip and without --frame (a motion-transfer clip has no start frame)')
        if not re.search(r'/references/v\d+_c\d\d_r\d+\.mp4$', a.driver):
            raise SystemExit('--driver must be the shot reference video: content/video_N_assets/references/vN_cNN_rK.mp4')
        if not os.path.exists(os.path.join(B.ROOT, prod, a.driver)):
            raise SystemExit(f'--driver not found: {a.driver}')
    if driver:
        frames = []
    elif not a.frame:
        if not old:
            raise SystemExit('a new card needs --frame')
        # keep the frames and their drawer blocks exactly as they are
        frames = old['frames']
        image_tag = old.get('tags', {}).get('image', '')
        for b in old.get('det', []):
            if b.get('k') == 'head' and b['text'].startswith('CLIP'):
                break
            if b.get('k') in ('head', 'refs', 'prompt', 'split'):
                det.append(b)
        if det and det[-1]['k'] != 'split':
            det.append({'k': 'split'})
    new_files = {f['file'] for f in frames} | ({a.clip.split('=', 1)[0]} if a.clip else set())
    old_files = ({f['file'] for f in old.get('frames') or []} |({old['take']['file']} if old.get('take') else set())) if old else set()
    if old and old.get('driver') and old['driver'] != driver:
        old_files.add(old['driver'])
    if old and (old_files - new_files) and not a.replaced:
        raise SystemExit(f'{shot} already shows {sorted(old_files - new_files)}; a new take needs --replaced "<why the old one lost>" '
                         '(the old take then moves to Other takes on disk)')
    if a.clip and driver and old and old.get('stage') == 'refs' and old.get('status') != 'approved' and not a.force:
        # columns layout: a run's references (the woman and the room) are approved before anything is generated
        raise SystemExit(f'{shot}: its references are {old.get("status")} - generate only after Daniel approved the '
                         'woman and the room (decide.py). Pass --force only if Daniel said so.')
    if a.clip and not a.force and not driver:
        # the approval belongs to the exact frame files on the card: a clip is accepted only when
        # the card keeps the frames Daniel approved (stage frame + approved, or a clip card - its
        # frames were approved before its first clip). New frame files need their own approval first.
        same_frames = bool(old) and [f['file'] for f in old.get('frames') or []] == [f['file'] for f in frames]
        approved = bool(old) and (old['stage'] == 'clip' or old['status'] == 'approved')
        if not (same_frames and approved):
            raise SystemExit(f'{shot}: animate only an APPROVED frame (two approvals per video). '
                             + ('These frame files are not the ones on the approved card - add them with --frame alone, '
                                'let Daniel approve, then --clip. ' if old and not same_frames else
                                'Approve the frame first (decide.py). ')
                             + 'Pass --force only if Daniel said so.')
    card = {'clip': shot, 'stage': 'clip' if a.clip else 'frame', 'status': a.status,
            'title': a.title, 'desc': a.desc, 'frames': frames, 'tags': {'image': image_tag}}
    if old:
        # details that were added by hand stay unless this call gives new ones
        for k in ('variant', 'tip', 'count_note', 'looks'):
            if old.get(k):
                card[k] = old[k]
        if old.get('chip') and (old['stage'], old['status']) == (card['stage'], card['status']):
            card['chip'] = old['chip']
        if (old.get('tags') or {}).get('extra'):
            card['tags']['extra'] = old['tags']['extra']
    if driver:
        card['driver'] = driver
    if a.clip:
        path, job_p = a.clip.split('=', 1)
        r = load_job(job_p)
        cs = clip_settings(r)
        p_ = r.get('params', {})
        card['tags']['clip'] = ' · '.join(x for x in [r.get('model', ''), str(p_.get('resolution') or ''),
                                                      f"{p_['duration']} s" if p_.get('duration') else ''] if x)
        audio = [x for x in cs if x.startswith('audio') or x.startswith('sound')]
        line1 = ' · '.join(x for x in [r.get('model', ''), str(p_.get('resolution') or ''),
                                        f"{p_['duration']} s" if p_.get('duration') else ''] + audio if x)
        up = path.replace('/clips/', '/clips/upscaled/')
        line2 = f'job {r["id"][:8]}'
        take = {'file': path, 'info': [line1, line2]}
        if os.path.exists(os.path.join(B.ROOT, prod, up)):
            take['play'] = up
            take['info'][1] += ' · 2K' + probe_size(os.path.join(B.ROOT, prod, up))
        if a.status == 'review':
            take['label'] = 'Clip for review'
        elif a.status == 'rejected':
            take['label'] = 'Rejected clip'
        card['take'] = take
        det += [{'k': 'head', 'text': f'CLIP — {os.path.basename(path)}'}, refs(r, 'clip', known),
                {'k': 'prompt', 'label': f'Clip prompt · {os.path.basename(path)}',
                 'meta': ' · '.join(cs + [f'job {r["id"][:8]}']), 'text': r['params']['prompt']}]
    elif det and det[-1]['k'] == 'split':
        det.pop()
    card['tags'] = {k: v for k, v in card['tags'].items() if v}
    # lane / group
    if lane is None:
        lane = {'n': a.video, 'title': a.lane_title or f'Video {a.video}', 'final': None,
                'meta': [['Status', 'In production'], ['Hook', a.lane_title or 'not recorded'], ['Song', 'not recorded'],
                         ['Runtime', 'not recorded'], ['Resolution', 'not recorded']],
                'groups': []}
        if a.caption:
            lane['caption'] = a.caption
        D['lanes'].append(lane)
    if old:
        old_grp['cards'].remove(old)
        if old.get('take') and card.get('take') and old['take']['file'] == card['take']['file'] and old['take'].get('poster'):
            card['take']['poster'] = old['take']['poster']
    grp = next((g for g in lane['groups'] if g['name'].lower() == a.group.lower()), None)
    if grp is None:
        grp = {'name': a.group, 'sub': a.group_sub, 'color': GROUP_COLOR.get(a.group.lower(), '#5b6472'), 'cards': []}
        lane['groups'].append(grp)
    alts = []
    notes = []
    if old:
        for b in old.get('det', []):
            if b.get('k') == 'alts':
                alts += b['rows']
            elif b.get('k') in ('notes', 'learn'):
                notes.append(b)
        gone = sorted(old_files - new_files)
        alts += [{'media': g_, 'why_html': B.E(a.replaced)} for g_ in gone]
    if alts:
        det.append({'k': 'alts', 'rows': alts})
    for n in a.note:
        notes.append({'k': 'notes', 'html': n})
    det += notes
    det.append({'k': 'arch', 'html': f'Every take of this shot &rarr; <code>content/video_{a.video}_assets/prompts.md</code> '
                                     f'&sect; C{shot[1:]}'})
    card['det'] = det
    grp['cards'].append(card)
    grp['cards'].sort(key=lambda c: c['clip'])
    order = ['hook', 'b-roll 1', 'b-roll 2']
    lane['groups'].sort(key=lambda g: order.index(g['name'].lower()) if g['name'].lower() in order else len(order))
    lane['groups'] = [g for g in lane['groups'] if g['cards']]
    page, ctx = B.build(prod, data=D)
    if ctx.errors:
        print('NOT written - fix these first:')
        print('\n'.join('  ' + e for e in ctx.errors))
        return 1
    try:
        B.save_data(dp, D, seen)
        md5 = B.write_verified(os.path.join(B.ROOT, prod, 'video_board.html'), page)
    except B.BoardError as e:
        raise SystemExit(f'NOT written - {e}')
    print(f'{prod}: v{a.video} {shot} {card["stage"]}/{card["status"]} written; board rebuilt, md5 {md5}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
