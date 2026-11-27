import sys
from PIL import Image, ImageDraw, ImageFont
F="/home/user/limitless/creator-kit/engine/fonts/TikTokSans-w700-semicond.ttf"
M="/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"
def cap(name, lines, y=250, size=64, cam=None):
    im=Image.new("RGBA",(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
    f=ImageFont.truetype(F,size)
    for i,l in enumerate(lines):
        w=d.textlength(l,font=f)
        d.text(((1080-w)/2, y+i*(size+18)), l, font=f, fill="white", stroke_width=6, stroke_fill="black")
    if cam:
        m=ImageFont.truetype(M,34)
        d.text((40,60), cam, font=m, fill=(255,255,255,230), stroke_width=2, stroke_fill="black")
        d.ellipse((960,62,990,92), fill=(255,255,255,230)); d.text((1000,58),"REC", font=m, fill=(255,255,255,230)) if False else None
    im.save(sys.argv[1]+"/"+name)
o=sys.argv[1]
cap("t1.png",["2:47 AM.","Every. Single. Night."], cam="CAM 02  11-27  02:47:13 AM")
cap("t2.png",["So I tried this..."])
cap("t3.png",["So I tried this..."])
cap("t4.png",["He couldn't stop","watching it"])
cap("t5.png",['Comment "TORNADO"',"for the link"], y=250, size=70)
cap("t6.png",["He couldn't stop","watching it"], y=1400)
cap("t7.png",['Comment "TORNADO"',"for the link"], y=1400, size=70)
