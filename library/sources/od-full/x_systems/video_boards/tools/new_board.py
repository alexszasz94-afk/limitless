#!/usr/bin/env python3
"""Start the board for a new product.

    python3 x_systems/video_boards/tools/new_board.py "BRAND - PRODUCT" "Brand Product"

Creates, inside the product folder (which must already exist):
    content/_board_thumbs/board_data.json   the board's data, with no videos yet
    content/_board_thumbs/board_notes.txt   empty - Daniel's notes file
then builds video_board.html. Refuses to touch a product that already has a
board_data.json. Standard library only.
"""
import json, os, sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_board as B


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    product, brand = sys.argv[1], sys.argv[2]
    base = os.path.join(B.ROOT, product)
    if ' - ' not in product or product != product.upper():
        print('product folder must be ALL CAPS "BRAND - PRODUCT" (see _tool/NAMING.md)')
        return 1
    if not os.path.isdir(base):
        print(f'no folder {base} - create the product folder first')
        return 1
    data_p = os.path.join(base, B.DATA_REL)
    if os.path.exists(data_p):
        print(f'{data_p} already exists - this product already has a board')
        return 1
    os.makedirs(os.path.dirname(data_p), exist_ok=True)
    D = {
        'schema': 'video-board/1',
        'product': product,
        'brand': brand,
        'key': B.slug(product),
        'legend': [{'color': '#E8452C', 'text': 'Hook — C01'},
                   {'color': '#2D6BF0', 'text': 'B-roll 1 — the product'},
                   {'color': '#1F9D6B', 'text': 'B-roll 2 — the payoff'}],
        'panels': [{'type': 'list', 'title': 'Frame rules — what the image rounds taught', 'items_html': []},
                   {'type': 'list', 'title': 'Clip rules — what the animation rounds taught', 'items_html': []}],
        'lanes': [],
    }
    txt = json.dumps(D, ensure_ascii=False, indent=1) + '\n'
    open(data_p, 'w', encoding='utf-8').write(txt)
    notes = os.path.join(base, 'content', '_board_thumbs', 'board_notes.txt')
    if not os.path.exists(notes):
        open(notes, 'w', encoding='utf-8').close()
    page, ctx = B.build(product)
    if ctx.errors:
        print('\n'.join(ctx.errors))
        return 1
    md5 = B.write_verified(os.path.join(base, 'video_board.html'), page)
    print(f'{product}: board started - {data_p}, video_board.html md5 {md5}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
