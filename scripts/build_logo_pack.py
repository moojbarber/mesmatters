import re, os, json, asyncio
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","brand")
FONT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","public","fonts","")+"space-grotesk-latin-700-normal.woff2"
os.makedirs(OUT,exist_ok=True)
for d in ["mark","lockup-horizontal","lockup-stacked","social","icons"]: os.makedirs(f"{OUT}/{d}",exist_ok=True)
font=TTFont(FONT); gs=font.getGlyphSet(); cmap=font.getBestCmap(); upm=font["head"].unitsPerEm; hmtx=font["hmtx"]
CAP=font["OS/2"].sCapHeight if hasattr(font["OS/2"],"sCapHeight") else 700
def text_path(txt, size, tracking_em, x0=0, baseline=0):
    s=size/upm; x=x0; d=[]
    for ch in txt:
        g=cmap.get(ord(ch))
        if ch==" ": x+=hmtx[g][0]*s+tracking_em*size; continue
        pen=SVGPathPen(gs); tp=TransformPen(pen,(s,0,0,-s,x,baseline)); gs[g].draw(tp)
        d.append(pen.getCommands()); x+=hmtx[g][0]*s+tracking_em*size
    return " ".join(d), x - tracking_em*size - x0, CAP*s
mark_full=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","public","logo-mark.svg")).read()
vb=[float(v) for v in re.search(r'viewBox="([^"]+)"',mark_full).group(1).split()]
mx,my,mw,mh=vb
inner=mark_full.split(">",1)[1].rsplit("</svg>",1)[0]
def mark_group(x,y,h):
    s=h/mh
    return f'<g transform="translate({x} {y}) scale({s:.5f}) translate({-mx} {-my})">{inner}</g>'
GRAD='<linearGradient id="wg" gradientUnits="userSpaceOnUse" x1="{x1}" y1="0" x2="{x2}" y2="0"><stop offset="0" stop-color="#8b6cff"/><stop offset="1" stop-color="#33d4e0"/></linearGradient>'
def svgdoc(w,h,body,bg=None,defs=""):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><defs>{defs}</defs>{b}{body}</svg>'
files={}
# --- mark
files["mark/shopfloor-matters-mark.svg"]=svgdoc(mw*1.0,mh*1.0,mark_group(0,0,mh))
# --- horizontal lockup
def horizontal(textfill, mark_h=120):
    size=mark_h*0.36; gap=mark_h*0.32
    d,tw,ch=text_path("SHOPFLOOR MATTERS",size,0.24,x0=0,baseline=0)
    W=mark_h*mw/mh+gap+tw; H=mark_h
    tx=mark_h*mw/mh+gap; base=H/2+ch/2
    d,tw,ch=text_path("SHOPFLOOR MATTERS",size,0.24,x0=tx,baseline=base)
    fill='url(#wg)' if textfill=="grad" else textfill
    return svgdoc(round(W+2),H,mark_group(0,0,mark_h)+f'<path d="{d}" fill="{fill}"/>',defs=GRAD.format(x1=tx,x2=tx+tw))
files["lockup-horizontal/shopfloor-matters-horizontal-dark-bg.svg"]=horizontal("grad")
files["lockup-horizontal/shopfloor-matters-horizontal-light-bg.svg"]=horizontal("#0a0820")
files["lockup-horizontal/shopfloor-matters-horizontal-white.svg"]=horizontal("#ffffff")
# --- stacked lockup (SHOPFLOOR over MATTERS)
def stacked(dark=True, mark_h=150):
    gap=mark_h*0.26; s1=mark_h*0.24; s2=mark_h*0.30
    tx=mark_h*mw/mh+gap
    d1,w1,c1=text_path("SHOPFLOOR",s1,0.26,x0=tx,baseline=0); d2,w2,c2=text_path("MATTERS",s2,0.2,x0=tx,baseline=0)
    lg=mark_h*0.12; total=c1+lg+c2; top=(mark_h-total)/2
    d1,w1,c1=text_path("SHOPFLOOR",s1,0.26,x0=tx,baseline=top+c1)
    d2,w2,c2=text_path("MATTERS",s2,0.2,x0=tx,baseline=top+c1+lg+c2)
    W=tx+max(w1,w2)
    if dark:
        defs='<linearGradient id="w1" gradientUnits="userSpaceOnUse" x1="%s" x2="%s" y1="0" y2="0"><stop offset="0" stop-color="#8b6cff"/><stop offset="1" stop-color="#a77bff"/></linearGradient><linearGradient id="w2" gradientUnits="userSpaceOnUse" x1="%s" x2="%s" y1="0" y2="0"><stop offset="0" stop-color="#b9a9ff"/><stop offset="1" stop-color="#33d4e0"/></linearGradient>'%(tx,tx+w1,tx,tx+w2)
        f1,f2="url(#w1)","url(#w2)"
    else: defs="";f1,f2="#6b4fe0","#0a0820"
    return svgdoc(round(W+2),mark_h,mark_group(0,0,mark_h)+f'<path d="{d1}" fill="{f1}"/><path d="{d2}" fill="{f2}"/>',defs=defs)
files["lockup-stacked/shopfloor-matters-stacked-dark-bg.svg"]=stacked(True)
files["lockup-stacked/shopfloor-matters-stacked-light-bg.svg"]=stacked(False)
# --- square icon on navy (LinkedIn profile/company logo, app icon)
def icon(size=400, pad=0.17, rounded=False):
    h=size*(1-2*pad)*1.0; w=h*mw/mh
    bg=f'<rect width="{size}" height="{size}" rx="{size*0.22 if rounded else 0}" fill="#0a0820"/>'
    glow=f'<radialGradient id="ig" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="#8b6cff" stop-opacity=".35"/><stop offset="1" stop-color="#8b6cff" stop-opacity="0"/></radialGradient>'
    return svgdoc(size,size,bg+f'<rect width="{size}" height="{size}" rx="{size*0.22 if rounded else 0}" fill="url(#ig)"/>'+mark_group((size-w)/2,(size-h)/2,h),defs=glow)
files["icons/shopfloor-matters-icon-square.svg"]=icon()
files["icons/shopfloor-matters-icon-rounded.svg"]=icon(rounded=True)
# --- banners
def banner(W,H,logo_h,tag_size,right=True,tag=True):
    dots="".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#ffffff" opacity=".10"/>' for x in range(13,W,26) for y in range(13,H,26))
    defs=('<radialGradient id="b1" cx="1" cy="0" r="1"><stop offset="0" stop-color="#8b6cff" stop-opacity=".45"/><stop offset="1" stop-color="#8b6cff" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="b2" cx=".35" cy="1.1" r=".8"><stop offset="0" stop-color="#33d4e0" stop-opacity=".25"/><stop offset="1" stop-color="#33d4e0" stop-opacity="0"/></radialGradient>'
          '<linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="#8b6cff" stop-opacity="0"/><stop offset=".5" stop-color="#8b6cff"/><stop offset="1" stop-color="#33d4e0"/></linearGradient>')
    st=stacked(True,logo_h); sw=float(re.search(r'viewBox="0 0 ([\d.]+)',st).group(1))
    stin=st.split("<defs>",1)[1]; sdefs,sbody=stin.split("</defs>",1); sbody=sbody.rsplit("</svg>",1)[0]
    pad=W*0.06
    lx=W-pad-sw if right else pad
    ly=H*0.30 if tag else (H-logo_h)/2
    body=f'<rect width="{W}" height="{H}" fill="#0a0820"/><rect width="{W}" height="{H}" fill="url(#b1)"/><rect width="{W}" height="{H}" fill="url(#b2)"/>{dots}<g transform="translate({lx:.1f} {ly:.1f})">{sbody}</g>'
    if tag:
        t1="Smart factory  /  Shopfloor AI  /  MES & MOM"
        d,tw,ch=text_path(t1,tag_size,0.08,0,0); tx=W-pad-tw if right else pad
        d,tw,ch=text_path(t1,tag_size,0.08,tx,ly+logo_h+tag_size*2.2)
        body+=f'<path d="{d}" fill="#a9a4d6"/>'
        u="shopfloormatters.com"; d2,uw,_=text_path(u,tag_size*0.95,0.06,0,0); ux=W-pad-uw if right else pad
        d2,uw,_=text_path(u,tag_size*0.95,0.06,ux,ly+logo_h+tag_size*4.2)
        body+=f'<path d="{d2}" fill="#33d4e0"/>'
    body+=f'<rect x="0" y="{H-4}" width="{W}" height="4" fill="url(#ln)"/>'
    return svgdoc(W,H,body,defs=defs+sdefs)
files["social/linkedin-personal-banner-1584x396.svg"]=banner(1584,396,120,22)
files["social/linkedin-company-cover-1128x191.svg"]=banner(1128,191,70,0,tag=False)
files["social/linkedin-company-logo-400x400.svg"]=icon(400)
files["social/x-twitter-header-1500x500.svg"]=banner(1500,500,140,24)
for k,v in files.items(): open(f"{OUT}/{k}","w").write(v)
json.dump(list(files),open(OUT+"/../files.json","w"))
# --- PNG renders
from playwright.async_api import async_playwright
renders=[("mark/shopfloor-matters-mark.svg",[256,512,1024,2048],"h"),
 ("lockup-horizontal/shopfloor-matters-horizontal-dark-bg.svg",[120,240,480],"h"),
 ("lockup-horizontal/shopfloor-matters-horizontal-light-bg.svg",[120,240,480],"h"),
 ("lockup-horizontal/shopfloor-matters-horizontal-white.svg",[240],"h"),
 ("lockup-stacked/shopfloor-matters-stacked-dark-bg.svg",[150,300,600],"h"),
 ("lockup-stacked/shopfloor-matters-stacked-light-bg.svg",[150,300,600],"h"),
 ("icons/shopfloor-matters-icon-square.svg",[32,180,512,1024],"h"),
 ("icons/shopfloor-matters-icon-rounded.svg",[180,512,1024],"h"),
 ("social/linkedin-personal-banner-1584x396.svg",[396],"h"),
 ("social/linkedin-company-cover-1128x191.svg",[191],"h"),
 ("social/linkedin-company-logo-400x400.svg",[400],"h"),
 ("social/x-twitter-header-1500x500.svg",[500],"h")]
async def go():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        for f,hs,_ in renders:
            src=open(f"{OUT}/{f}").read(); w,h=[float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',src).groups()]
            for H in hs:
                W=round(w*H/h)
                await pg.set_viewport_size({"width":W,"height":H})
                await pg.set_content(f'<html><body style="margin:0;background:transparent">{src.replace("<svg ",f"<svg style=\"display:block;width:{W}px;height:{H}px\" ",1)}</body></html>')
                name=f[:-4]+(f"-{H}px.png" if len(hs)>1 else ".png")
                await pg.screenshot(path=f"{OUT}/{name}",omit_background=True)
        await b.close()
asyncio.run(go())
