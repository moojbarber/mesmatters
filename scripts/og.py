#!/usr/bin/env python3
"""Render 1200x630 social share cards (public/images/og/*.png) from the article art.
Needs: pip install playwright pyyaml && python -m playwright install chromium
"""
import html
from pathlib import Path

import yaml
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "images" / "og"
FONTS = (ROOT / "public" / "fonts").as_uri()
ART = (ROOT / "public" / "images" / "art").as_uri()
CATS = {"education": "Foundations", "advice": "Implementation", "thought-leadership": "Smart Factory & AI"}

TPL = """<!doctype html><html><head><style>
@font-face{{font-family:SG;font-weight:700;src:url({fonts}/space-grotesk-latin-700-normal.woff2)}}
@font-face{{font-family:Mo;font-weight:600;src:url({fonts}/montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:In;font-weight:500;src:url({fonts}/inter-latin-500-normal.woff2)}}
html,body{{margin:0;width:1200px;height:630px;background:#0a0820;overflow:hidden}}
.art{{position:absolute;inset:0;background:url({art}/{img}.svg) 170px 50%/1440px auto no-repeat}}
.shade{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,8,32,.97) 0%,rgba(10,8,32,.9) 44%,rgba(10,8,32,.15) 80%)}}
.c{{position:absolute;left:72px;top:64px;bottom:64px;width:640px;display:flex;flex-direction:column}}
.brand{{display:flex;align-items:center;gap:14px}}.wm{{display:flex;flex-direction:column;gap:4px;font:600 16px/1 Mo;letter-spacing:.2em}}.wm b{{font:inherit;color:#a865c4}}.wm b+b{{color:#c3b9e3;font-size:18px;letter-spacing:.16em}}
.tag{{align-self:flex-start;margin-top:auto;font:500 15px In;letter-spacing:.18em;text-transform:uppercase;color:#33d4e0;border:1px solid rgba(51,212,224,.45);background:rgba(51,212,224,.1);padding:9px 15px;border-radius:99px}}
h1{{font:700 {size}px/1.06 SG;letter-spacing:-.03em;margin:22px 0 0;background:linear-gradient(100deg,#fff 30%,#c9bcff 70%,#7fe9f2);-webkit-background-clip:text;color:transparent;padding-bottom:4px}}
.by{{margin-top:26px;font:500 19px In;color:#a9a4d6}}
.rule{{position:absolute;left:0;right:0;bottom:0;height:5px;background:linear-gradient(90deg,#8b6cff,#33d4e0)}}
</style></head><body><div class="art"></div><div class="shade"></div>
<div class="c"><div class="brand"><svg height="44" viewBox="0 0 420 480" aria-hidden="true"><g stroke="#9b51b0" stroke-width="13" stroke-linecap="round"><line x1="33" y1="136" x2="120" y2="190"/><line x1="33" y1="240" x2="120" y2="290"/><line x1="120" y1="290" x2="208" y2="342"/><line x1="33" y1="240" x2="33" y2="340"/><line x1="208" y1="240" x2="296" y2="190"/><line x1="296" y1="190" x2="386" y2="136"/><line x1="296" y1="290" x2="386" y2="240"/><line x1="386" y1="240" x2="386" y2="340"/></g><circle cx="208" cy="33" r="29" fill="#b4a9d4"/><circle cx="120" cy="85" r="29" fill="#b4a9d4"/><circle cx="296" cy="85" r="29" fill="#b4a9d4"/><circle cx="208" cy="138" r="29" fill="#b4a9d4"/><circle cx="120" cy="396" r="29" fill="#b4a9d4"/><circle cx="296" cy="396" r="29" fill="#b4a9d4"/><circle cx="208" cy="446" r="29" fill="#b4a9d4"/><circle cx="33" cy="136" r="29" fill="#9b51b0"/><circle cx="120" cy="190" r="29" fill="#9b51b0"/><circle cx="33" cy="240" r="29" fill="#9b51b0"/><circle cx="120" cy="290" r="29" fill="#9b51b0"/><circle cx="33" cy="340" r="29" fill="#9b51b0"/><circle cx="208" cy="342" r="29" fill="#9b51b0"/><circle cx="208" cy="240" r="29" fill="#9b51b0"/><circle cx="296" cy="190" r="29" fill="#9b51b0"/><circle cx="386" cy="136" r="29" fill="#9b51b0"/><circle cx="386" cy="240" r="29" fill="#9b51b0"/><circle cx="296" cy="290" r="29" fill="#9b51b0"/><circle cx="386" cy="340" r="29" fill="#9b51b0"/></svg><span class="wm"><b>MES</b><b>MATTERS</b></span></div>
<span class="tag">{tag}</span><h1>{title}</h1><div class="by">Matt Barber · mesmatters.com</div></div><div class="rule"></div></body></html>"""


def cards():
    seo = yaml.safe_load((ROOT / "content" / "seo.yaml").read_text())
    for slug, m in seo.items():
        yield slug, slug, CATS[m["category"]], m["title"]
    for p in sorted((ROOT / "content" / "posts").glob("*.md")):
        fm = yaml.safe_load(p.read_text().split("---")[1])
        yield fm.get("slug", p.stem), fm.get("slug", p.stem), CATS[fm["category"]], fm["title"]
    yield "home", "page-home", "Smart factory · Shopfloor AI", "Building the smart factory, from the shopfloor up"
    yield "page-about", "page-about", "About", "Hi, I'm Matt Barber"
    yield "page-education", "page-education", "Foundations", "The systems underneath the smart factory"
    yield "page-advice", "page-advice", "Implementation", "Getting shopfloor projects over the line"
    yield "page-thought-leadership", "page-thought-leadership", "Smart Factory & AI", "Shopfloor AI and the smart factory"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for name, img, tag, title in cards():
            size = 64 if len(title) < 40 else 54 if len(title) < 62 else 46
            tmp = OUT / "_card.html"
            tmp.write_text(TPL.format(fonts=FONTS, art=ART, img=img, pos="62% 50%", tag=html.escape(tag), title=html.escape(title), size=size), encoding="utf-8")
            pg.goto(tmp.as_uri(), wait_until="load")
            pg.wait_for_timeout(150)
            pg.screenshot(path=str(OUT / f"{name}.png"))
            print(name)
        b.close()
    (OUT / "_card.html").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
