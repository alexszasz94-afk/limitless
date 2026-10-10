#!/usr/bin/env python3
"""Burn story headlines onto the round-2 base images."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = "/sessions/<session>/mnt/ORGANIC DROPSHIPPING/Content/Stories/round2_base"
OUT = "/sessions/<session>/mnt/ORGANIC DROPSHIPPING/Content/Stories/round2"
GF = "/usr/share/fonts/truetype/google-fonts"
F_BOLD = f"{GF}/Poppins-Bold.ttf"
F_MED = f"{GF}/Poppins-Medium.ttf"
F_ITAL = f"{GF}/Lora-Italic-Variable.ttf"

RED = (214, 40, 40)
WHITE = (255, 255, 255)

SPECS = [
    dict(f="01_grinch_phone_app.png", style="A",
         head="100+ DESIGNS.\nONE TAP.",
         sub="change the whole house from the couch"),
    dict(f="02_full_house_snowman.png", style="A",
         head="THE HOUSE\nEVERYONE STOPS FOR",
         sub="and it all comes out of one box"),
    dict(f="03_neighbours_filming.png", style="C",
         kicker="every single night now",
         head="THE NEIGHBOURS\nJUST STAND THERE"),
    dict(f="04_kids_driveway.png", style="A",
         head="THIS IS THE PART\nYOU DO IT FOR",
         sub="they would not come inside"),
    dict(f="05_ladder_install.png", style="B",
         head="UP IN 20 MINUTES",
         sub="ONE PERSON. NO TOOLS."),
    dict(f="06_macro_snow_net.png", style="A",
         head="SNOW. RAIN. ICE.",
         sub="IP65 rated - leave it up all season"),
    dict(f="07_before_after.png", style="A",
         head="SAME HOUSE.\nONE BOX.",
         sub="one evening of work"),
    dict(f="08_gifting_pov.png", style="C", y0=0.045, hscale=0.098,
         kicker="the gift nobody thinks of",
         head="HE'LL REMEMBER THIS ONE"),
    dict(f="09_empty_shelf.png", style="B",
         head="STORES ARE\nALREADY OUT",
         sub="WE STILL HAVE STOCK"),
    dict(f="10_car_pov.png", style="C",
         kicker="saw this on my street last night",
         head="FOUND THE EXACT KIT"),
]


def fit(text_lines, path, max_w, start):
    """Largest font size where every line fits max_w."""
    size = start
    while size > 20:
        fo = ImageFont.truetype(path, size)
        if all(fo.getbbox(l)[2] - fo.getbbox(l)[0] <= max_w for l in text_lines):
            return fo
        size -= 2
    return ImageFont.truetype(path, 20)


def scrim(img, height_frac=0.34, strength=150):
    w, h = img.size
    grad = Image.new("L", (1, h), 0)
    hh = int(h * height_frac)
    for y in range(hh):
        grad.putpixel((0, y), int(strength * (1 - y / hh) ** 1.5))
    grad = grad.resize((w, h))
    black = Image.new("RGB", (w, h), (0, 0, 0))
    return Image.composite(black, img, grad).convert("RGB") if False else Image.composite(black, img, grad)


def shadow_text(img, xy, text, font, fill, anchor="ma"):
    """Text with a soft dark shadow, drawn onto a copy for legibility."""
    w, h = img.size
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text(xy, text, font=font, fill=(0, 0, 0, 170), anchor=anchor)
    layer = layer.filter(ImageFilter.GaussianBlur(14))
    img.paste(Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB"), (0, 0))
    d2 = ImageDraw.Draw(img)
    d2.text(xy, text, font=font, fill=fill, anchor=anchor)


def render(spec):
    img = Image.open(os.path.join(BASE, spec["f"])).convert("RGB")
    W, H = img.size
    img = scrim(img, 0.34, 155).convert("RGB")

    cx = W // 2
    max_w = int(W * 0.86)
    y = int(H * spec.get("y0", 0.075))

    if spec["style"] == "C":
        kf = ImageFont.truetype(F_ITAL, int(W * 0.052))
        shadow_text(img, (cx, y), spec["kicker"], kf, (255, 255, 255))
        y += int(kf.size * 1.55)

    lines = spec["head"].split("\n")
    hf = fit(lines, F_BOLD, max_w, int(W * spec.get("hscale", 0.115)))
    for ln in lines:
        shadow_text(img, (cx, y), ln, hf, WHITE)
        y += int(hf.size * 1.14)

    if spec["style"] == "A":
        y += int(hf.size * 0.16)
        sf = fit([spec["sub"]], F_MED, max_w, int(W * 0.042))
        shadow_text(img, (cx, y), spec["sub"], sf, (238, 238, 238))

    elif spec["style"] == "B":
        y += int(hf.size * 0.34)
        sf = fit([spec["sub"]], F_BOLD, int(max_w * 0.9), int(W * 0.040))
        bb = sf.getbbox(spec["sub"])
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        padx, pady = int(sf.size * 0.72), int(sf.size * 0.52)
        x0, y0 = cx - tw // 2 - padx, y - pady // 2
        x1, y1 = cx + tw // 2 + padx, y + th + pady
        pill = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(pill).rounded_rectangle([x0, y0, x1, y1], radius=(y1 - y0) // 2, fill=RED + (255,))
        img.paste(Image.alpha_composite(img.convert("RGBA"), pill).convert("RGB"), (0, 0))
        ImageDraw.Draw(img).text((cx, y - bb[1] + pady // 2), spec["sub"], font=sf, fill=WHITE, anchor="ma")

    os.makedirs(OUT, exist_ok=True)
    name = "story_" + spec["f"]
    img.save(os.path.join(OUT, name), "PNG")
    return name


if __name__ == "__main__":
    for s in SPECS:
        print(render(s))
