import sys
from PIL import Image, ImageDraw, ImageFont
F="/home/user/limitless/creator-kit/engine/fonts/TikTokSans-w700-semicond.ttf"
E="/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
def emoji(ch,h):
    f=ImageFont.truetype(E,109); im=Image.new("RGBA",(160,160),(0,0,0,0)); ImageDraw.Draw(im).text((10,10),ch,font=f,embedded_color=True)
    im=im.crop(im.getbbox()); return im.resize((int(im.width*h/im.height),h),Image.LANCZOS)
def cap(path, lines, y=250, size=64):
    im=Image.new("RGBA",(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im); f=ImageFont.truetype(F,size)
    for i,(txt,emos) in enumerate(lines):
        es=[emoji(e,int(size*1.05)) for e in emos]; tw=d.textlength(txt,font=f); w=tw+sum(e.width+10 for e in es)
        x=(1080-w)/2; yy=y+i*(size+18)
        d.text((x,yy),txt,font=f,fill="white",stroke_width=6,stroke_fill="black"); x+=tw+10
        for e in es: im.alpha_composite(e,(int(x),int(yy+size*0.08))); x+=e.width+10
    im.save(path)
o=sys.argv[1]
cap(o+"/h_dont.png",[("DON'T SHOW THIS",[]),("TO YOUR CHILDREN",["😳","🌪"])])
