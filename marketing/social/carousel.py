import sys, os, json, html, asyncio, math, importlib.util, random
from playwright.async_api import async_playwright
FONTS="/home/claude/mesmatters/public/fonts"
LOGO="/home/claude/mesmatters/public/logo-mark.svg"
ART="/home/claude/mesmatters/public/images/art"
ARTSLUG=[None]
OUT=os.environ.get("OUTDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)),"carousels")
W,H=1080,1350
REEL=os.environ.get('REEL')=='1'
if REEL: H=1920
def load(n):
    s=importlib.util.spec_from_file_location(n,f"{n}.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m.WEEK
CSS=f"""
@font-face{{font-family:SG;font-weight:500;src:url(file://{FONTS}/space-grotesk-latin-500-normal.woff2)}}
@font-face{{font-family:SG;font-weight:700;src:url(file://{FONTS}/space-grotesk-latin-700-normal.woff2)}}
@font-face{{font-family:In;font-weight:400;src:url(file://{FONTS}/inter-latin-400-normal.woff2)}}
@font-face{{font-family:In;font-weight:500;src:url(file://{FONTS}/inter-latin-500-normal.woff2)}}
@font-face{{font-family:In;font-weight:600;src:url(file://{FONTS}/inter-latin-600-normal.woff2)}}
:root{{--bg:#0a0820;--bg2:#120f33;--card:rgba(255,255,255,.055);--line:rgba(255,255,255,.12);--tx:#e9e6ff;--mut:#a9a4d6;--dim:#7d78ad;--a:#8b6cff;--b:#33d4e0;--c:#ff6fd8;
--g:linear-gradient(120deg,#8b6cff,#33d4e0);--disp:SG,sans-serif;--body:In,sans-serif}}
@page{{size:{W}px {H}px;margin:0}}
*{{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box}}
html,body{{margin:0;background:var(--bg);color:var(--tx);-webkit-font-smoothing:antialiased}}
.slide{{position:relative;width:{W}px;height:{H}px;overflow:hidden;break-after:page;background:var(--bg)}}
.strip{{position:absolute;top:0;height:100%}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.11) 1.4px,transparent 1.4px);background-size:28px 28px;-webkit-mask-image:linear-gradient(#000 0%,rgba(0,0,0,.55) 55%,transparent 92%)}}
.blob{{position:absolute;border-radius:50%}}
.safe{{position:relative;z-index:2;height:100%;padding:{'250px 96px 380px' if REEL else '110px 96px 120px'};display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.tag{{display:inline-flex;align-items:center;gap:14px;font:700 20px/1 var(--disp);letter-spacing:.2em;text-transform:uppercase;color:var(--b);border:1px solid rgba(51,212,224,.4);background:rgba(51,212,224,.08);padding:12px 20px 12px 14px;border-radius:99px}}
.tag img{{height:34px}}
.count{{font:700 26px var(--disp);color:var(--dim);font-variant-numeric:tabular-nums}} .count b{{color:#fff}}
.body{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:34px}}
.foot{{display:flex;justify-content:space-between;align-items:center;font:500 24px var(--body);color:var(--dim)}}
.swipe{{color:var(--b);font:700 24px var(--disp);letter-spacing:.06em}}
.h1{{font:700 112px/1.0 var(--disp);letter-spacing:-.035em;background:linear-gradient(100deg,#fff 20%,#c9bcff 60%,#7fe9f2);-webkit-background-clip:text;background-clip:text;color:transparent;text-wrap:balance;margin:0}}
.kick{{font:500 44px/1.35 var(--body);color:var(--mut);margin:0;text-wrap:pretty}}
.h2{{font:700 84px/1.04 var(--disp);letter-spacing:-.03em;margin:0;color:#fff;text-wrap:balance}}
.p{{font:400 44px/1.42 var(--body);color:#d8d3ff;margin:0;text-wrap:pretty}}
.big{{font:700 260px/0.9 var(--disp);letter-spacing:-.05em;background:var(--g);-webkit-background-clip:text;background-clip:text;color:transparent;font-variant-numeric:tabular-nums}}
.big.sm{{font-size:200px}}
.lab{{font:700 22px var(--disp);letter-spacing:.24em;text-transform:uppercase;color:var(--b)}}
.list{{list-style:none;margin:0;padding:0;display:grid;gap:26px}}
.list li{{display:flex;gap:28px;align-items:flex-start;font:500 46px/1.28 var(--body);color:#cfcbf5}}
.list li:before{{content:"";flex:none;width:18px;height:18px;margin-top:20px;border-radius:3px;transform:rotate(45deg);background:var(--g)}}
.quote{{border-left:6px solid;border-image:linear-gradient(#8b6cff,#33d4e0) 1;padding-left:44px}}
.quote .q{{font:700 88px/1.08 var(--disp);letter-spacing:-.03em;color:#e4dfff;margin:0;text-wrap:balance}}
.quote .cite{{font:700 22px var(--disp);letter-spacing:.16em;text-transform:uppercase;color:var(--b);margin-top:30px}}
.panel{{border-radius:30px;padding:40px 44px;display:grid;gap:14px}}
.they{{background:rgba(255,111,216,.08);border:1px solid rgba(255,111,216,.5)}}
.they .lab{{color:var(--c)}}
.real{{background:linear-gradient(160deg,rgba(139,108,255,.24),rgba(51,212,224,.1));border:1px solid rgba(51,212,224,.5);box-shadow:0 0 50px -12px rgba(51,212,224,.5)}}
.panel .t{{font:700 58px/1.12 var(--disp);letter-spacing:-.02em;color:#fff;margin:0}}
.turn{{padding:3px;border-radius:34px;background:var(--g)}}
.turn>div{{background:#0d0a28;border-radius:31px;padding:60px 56px;display:grid;gap:26px}}
.turn .h2{{font-size:76px}}
.art{{width:80%;margin-top:6px;border-radius:30px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 70px -30px rgba(139,108,255,.6)}}.art img{{display:block;width:100%;height:auto}}
.levelrow{{display:flex;align-items:flex-end;gap:36px}}
"""
def strip_svg(n, seed, ys):
    # continuous production-line thread across the strip + nodes
    Wt=n*W
    pts=[]
    for i,y in enumerate(ys):
        pts.append((i*W+120,y)); pts.append((i*W+W-120,y))
    d=f"M0,{ys[0]+40} "
    prev=(0,ys[0]+40)
    for (x,y) in pts:
        cx=(prev[0]+x)/2
        d+=f"C{cx},{prev[1]} {cx},{y} {x},{y} "
        prev=(x,y)
    d+=f"L{Wt},{ys[-1]}"
    nodes="".join(f'<circle cx="{i*W+W-150}" cy="{y}" r="9" fill="#33d4e0" filter="url(#gl)"/><circle cx="{i*W+W-150}" cy="{y}" r="22" fill="#33d4e0" opacity=".14"/>' for i,y in enumerate(ys))
    return f'''<svg width="{Wt}" height="{H}" style="position:absolute;inset:0" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="#8b6cff"/><stop offset="1" stop-color="#33d4e0"/></linearGradient><filter id="gl" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<path d="{d}" fill="none" stroke="url(#tg)" stroke-width="3" opacity=".75"/>{nodes}</svg>'''
def strip(n, seed):
    rnd=random.Random(seed)
    cols=[(106,61,240),(18,181,201),(197,63,184)]
    blobs=[]
    # one blob per seam (varied heights) + one inside each slide
    for i in range(n+1):
        c=cols[i%3]; size=rnd.randint(620,880); y=[-260,820,300,1000,-120,600][i%6]
        op=.5 if i in (0,n) else .38
        blobs.append((i*W-size/2,y,size,c,op))
    for i in range(n):
        c=cols[(i+1)%3]; size=rnd.randint(480,640); x=i*W+rnd.randint(200,600)-size/2; y=rnd.choice([1050,1150,-200])
        blobs.append((x,y,size,c,.22))
    bh="".join(f'<div class="blob" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;background:radial-gradient(circle,rgba({c[0]},{c[1]},{c[2]},{o}) 0%,rgba({c[0]},{c[1]},{c[2]},0) 70%)"></div>' for x,y,s,c,o in blobs)
    ys=[rnd.choice([250,290,330,1090,1130]) for _ in range(n)]
    ys[0]=222
    return f'<div class="dots"></div>{bh}{strip_svg(n,seed,ys)}'
def esc(t): return html.escape(t)
def content(kind,a,b,i,n):
    if kind=="cover":
        art=f'<div class="art"><img src="file://{ART}/{ARTSLUG[0]}.svg"></div>' if ARTSLUG[0] else ""
        return f'<h1 class="h1">{esc(a)}</h1>'+(f'<p class="kick">{esc(b)}</p>' if b else "")+art
    if kind=="stat":
        return f'<div class="big{" sm" if len(a)>5 else ""}">{esc(a)}</div><p class="h2" style="font-size:54px">{esc(b)}</p>'
    if kind=="num":
        return f'<div class="big">{int(a):02d}</div><p class="h2" style="font-size:58px">{esc(b)}</p>'
    if kind=="level":
        name,rest=(b.split(". ",1)+[""])[:2]
        return f'<div class="lab">Level</div><div class="levelrow"><div class="big">{esc(a)}</div><p class="h2" style="padding-bottom:30px">{esc(name)}</p></div><p class="p">{esc(rest)}</p>'
    if kind=="list":
        items="".join(f"<li>{esc(x)}</li>" for x in b.split("|"))
        return f'<h2 class="h2">{esc(a)}</h2><ul class="list">{items}</ul>'
    if kind=="quote":
        return f'<div class="quote"><p class="q">{esc(a)}</p>'+(f'<p class="p" style="margin-top:34px;font-weight:500;background:var(--g);-webkit-background-clip:text;background-clip:text;color:transparent">{esc(b)}</p>' if b and b!="mesmatters.com" else "")+'</div>'
    if kind=="myth":
        r=b[len("Reality: "):] if b.startswith("Reality: ") else b
        r=r[:1].upper()+r[1:]
        return f'<div class="panel they"><div class="lab">They say</div><p class="t">{esc(a)}</p></div><div class="panel real"><div class="lab">Reality</div><p class="t">{esc(r)}</p></div>'
    if kind=="cta":
        sub="" if b=="mesmatters.com" else b
        return f'<div class="turn"><div><div class="lab">{"Your turn" if "?" in a else "Next"}</div><h2 class="h2">{esc(a)}</h2>'+(f'<p class="p" style="color:var(--mut)">{esc(sub)}</p>' if sub else "")+'</div></div>'
    # point
    return f'<h2 class="h2">{esc(a)}</h2>'+(f'<p class="p">{esc(b)}</p>' if b else "")
def page(cid, slides, seed):
    n=len(slides); st=strip(n,seed); out=[]
    for i,(k,a,b) in enumerate(slides):
        cnt=f'<div class="count"><b>{i+1:02d}</b> / {n:02d}</div>' if n>1 and not REEL else ""
        sw='<span class="swipe">Swipe →</span>' if i<n-1 else '<span class="swipe" style="color:var(--dim)">mesmatters.com</span>'
        if n==1 or REEL: sw=""
        out.append(f'''<section class="slide"><div class="strip" style="width:{n*W}px;left:{-i*W}px">{st}</div><div class="safe">
<div class="top"><span class="tag"><img src="file://{LOGO}">MES Matters</span>{cnt}</div>
<div class="body">{content(k,a,b,i,n)}</div>
<div class="foot"><span>Matt Barber · mesmatters.com</span>{sw}</div></div></section>''')
    return f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(out)}</body></html>"
async def render(items):
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":W,"height":H})
        for cid,slides,art in items:
            ARTSLUG[0]=art
            d=os.path.join(OUT,cid,'reel') if REEL else os.path.join(OUT,cid); os.makedirs(d,exist_ok=True)
            f=os.path.join(d,"_src.html"); open(f,"w").write(page(cid,slides,hash(cid)%9999))
            await pg.goto("file://"+f); await pg.wait_for_timeout(400)
            n=len(slides)
            for i in range(n):
                el=(await pg.query_selector_all("section.slide"))[i]
                await el.screenshot(path=os.path.join(d,f"{cid}-{i+1:02d}.png"))
            if n>1 and not REEL: await pg.pdf(path=os.path.join(d,f"{cid}-linkedin.pdf"),width=f"{W}px",height=f"{H}px",print_background=True)
            os.remove(f)
        await b.close()
if __name__=="__main__":
    items=[]
    for w in sys.argv[1:]:
        for p in load(w)["posts"]:
            if p.get("slides") and (not os.environ.get("ONLY") or p["id"] in os.environ["ONLY"].split()): items.append((p["id"],p["slides"],load(w)["url"].rsplit('/',1)[1] if p["type"]=="Article" else None))
    asyncio.run(render(items)); print(len(items),"rendered")
