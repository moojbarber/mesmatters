#!/usr/bin/env python3
"""Build shopfloormatters.com into ./dist

    python scripts/build.py                    # production (served from the domain root)
    python scripts/build.py --base /mesmatters # preview on <user>.github.io/mesmatters

Content:
  content/posts/*.md         new articles (front matter + Markdown)
  content/legacy/posts/*.md  imported Wix articles
  content/seo.yaml           per-article title/description/category overrides
  content/blocks/*.html      reusable on-brand blocks, used in Markdown as `::block name`
"""
import argparse
import os
import datetime as dt
import html
import json
import math
import re
import shutil
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SITE = "https://www.shopfloormatters.com"
LINKEDIN = "https://www.linkedin.com/in/mattjbarber/"
# Kit (kit.com) form ID for the newsletter sign-up. Set the KIT_FORM_ID repo variable; empty = sign-ups not open yet.
KIT_FORM_ID = os.environ.get("KIT_FORM_ID", "").strip()

CATEGORIES = [
    {"key": "thought-leadership", "slug": "thought-leadership", "name": "Smart Factory & AI", "eyebrow": "Think", "art": "thought-leadership",
     "blurb": "Shopfloor AI, the connected worker and where manufacturing goes next.",
     "kicker": "Where AI really adds value on the shopfloor, how connected worker changes the frontline, and what both need underneath."},
    {"key": "education", "slug": "mes-education", "name": "Foundations", "eyebrow": "Learn", "art": "education",
     "blurb": "MES, MOM, ISA-95 and OEE: the systems and standards every smart factory runs on.",
     "kicker": "The systems and standards underneath every smart factory: what MES and MOM actually do, how ISA-95 fits together, how OEE is measured, and a function-by-function tour of MES."},
    {"key": "advice", "slug": "mes-advice", "name": "Implementation", "eyebrow": "Make it work", "art": "advice",
     "blurb": "Business cases, teams and getting shopfloor projects over the line.",
     "kicker": "Practical guidance for getting shopfloor projects over the line: building an honest business case, getting the team right, and avoiding the mistakes that sink implementations."},
]
CAT_BY_KEY = {c["key"]: c for c in CATEGORIES}

NAV = [
    {"key": "paths", "label": "Learning paths", "desc": "Guided routes through the articles", "href": "/paths/"},
    {"key": "articles", "label": "Articles", "desc": "Everything, by topic or newest first", "href": "/articles"},
    {"key": "featured", "label": "Featured", "desc": "Podcasts, interviews and press", "href": "/featured"},
    {"key": "faq", "label": "FAQ", "desc": "Straight answers to common questions", "href": "/faq/"},
    {"key": "glossary", "label": "Glossary", "desc": "Shopfloor jargon in plain English", "href": "/glossary/"},
    {"key": "about", "label": "About", "desc": "Who I am and why I write this", "href": "/about"},
]

# Old Wix URLs that should point somewhere new
REDIRECTS = {
    "home/categories/interfacing": "/mes-education",
    "home/categories/mes": "/thought-leadership",
    "home/categories/mes-advice": "/mes-advice",
    "copy-of-education": "/mes-advice",
    "blog": "/articles",
    "challenges": "/articles",
    "post/introduction-to-mes-and-smart-manufacturing": "/post/what-is-a-smart-factory",
    "post/mes-is-a-digital-twin": "/post/mes-and-digital-twins",
}


PLATFORMS = {"youtube": ("Watch on", "YouTube"), "spotify": ("Listen on", "Spotify"), "apple": ("Listen on", "Apple Podcasts"),
             "transcript": ("Read the", "Transcript"), "read": ("Read the", "Article"), "episode": ("Go to", "Episode page"),
             "event": ("See the", "Event page")}
TYPE_LABEL = {"podcast": "Podcast", "article": "Press", "webinar": "Webinar"}


def load_featured():
    data = yaml.safe_load((ROOT / "content" / "featured.yaml").read_text(encoding="utf-8"))
    items = []
    for it in data["items"]:
        d = it["date"] if isinstance(it["date"], dt.date) else dt.date.fromisoformat(str(it["date"]))
        it = dict(it, date_iso=d.isoformat(), date_text=it.get("date_label") or d.strftime("%B %Y"),
                  date_short=it.get("date_label") or d.strftime("%b %Y"), type_label=TYPE_LABEL[it["type"]],
                  outlet_line=it.get("card_outlet") or it["outlet"])
        links = []
        for l in it["links"]:
            verb, name = PLATFORMS[l["kind"]]
            if l.get("label"):
                verb, name = "Read the", l["label"]
            if l.get("show") and l["kind"] in ("spotify", "apple", "youtube"):
                verb = verb + " (show)"
            short = {"youtube": "YouTube", "spotify": "Spotify", "apple": "Apple Podcasts", "transcript": "Transcript",
                     "read": "Read", "episode": "Episode page", "event": "Event page"}[l["kind"]]
            if l.get("label"):
                short = l["label"]
            links.append(dict(l, verb=verb, name=name, short=short))
        it["links"] = links
        items.append(it)
    items.sort(key=lambda i: i["date_iso"], reverse=True)
    by_img = {i["image"]: i for i in items}
    return {"carousel": [by_img[k] for k in data["carousel"]], "items": items}


def load_paths(posts):
    """Learning paths: lines of articles. Adds hub-map geometry and per-post path context."""
    data = yaml.safe_load((ROOT / "content" / "paths.yaml").read_text(encoding="utf-8"))
    by_slug = {p["slug"]: p for p in posts}
    HX, HY, END, T = 190, 420, 880, 10
    paths = []
    for i, d in enumerate(data["paths"]):
        st = [by_slug[s] for s in d["stations"] if s in by_slug]
        y = 180 + i * 80
        dy, x0 = y - HY, HX + abs(y - HY)
        n = len(st)
        gap = (END - x0 - 80) / (n - 1)
        segs = []
        if dy:
            segs.append(f"left:{HX}px;top:{HY - T / 2}px;width:{abs(dy) * 2 ** .5:.1f}px;transform-origin:0 50%;transform:rotate({-45 if dy < 0 else 45}deg)")
        segs.append(f"left:{x0 - T / 2}px;top:{y - T / 2}px;width:{END - x0 + T}px")
        stations = [{"post": q, "n": k + 1, "x": round(x0 + 80 + k * gap, 1), "y": y} for k, q in enumerate(st)]
        paths.append(dict(d, stations=stations, n=n, minutes=sum(q["read_time"] for q in st), y=y, x0=x0, end=END,
                          segs=segs, flow=f"left:{x0}px;top:{y - 2}px;width:{END - x0}px", slugs=[q["slug"] for q in st]))
    for path in paths:
        for k, stn in enumerate(path["stations"]):
            q = stn["post"]
            q.setdefault("paths", []).append({"id": path["id"], "title": path["title"], "color": path["color"], "rgb": path["rgb"],
                                              "n": path["n"], "index": k + 1, "slugs": path["slugs"],
                                              "prev": path["stations"][k - 1]["post"] if k else None,
                                              "next": path["stations"][k + 1]["post"] if k + 1 < path["n"] else None})
    for path in paths:
        path["hub"] = {"x": HX, "y": HY}
    order = {k: i for i, k in enumerate(data["home_order"])}
    return paths, sorted(paths, key=lambda p: order.get(p["id"], 99))


# ------------------------------------------------------------------ helpers
def parse_md(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = yaml.safe_load(m.group(1)) if m else {}
    return fm or {}, text[m.end():] if m else text


def parse_date(s):
    if not s:
        return None
    if isinstance(s, (dt.date, dt.datetime)):
        return s if isinstance(s, dt.datetime) else dt.datetime(s.year, s.month, s.day)
    return dt.datetime.fromisoformat(str(s).replace("Z", "+00:00")).replace(tzinfo=None)


def long_date(d):
    return f"{d.day} {d:%B %Y}" if d else ""


def short_date(d):
    return f"{d.day} {d:%b %Y}" if d else ""


def slugify(value, separator="-"):
    value = re.sub(r"[^\w\s-]", "", html.unescape(value).lower())
    return re.sub(r"[\s_-]+", separator, value).strip(separator)


def render_body(md_text, base, blocks):
    md_text = md_text.replace("\\_", "_")
    # ::block name  ->  raw HTML block
    def blk(m):
        name = m.group(1)
        return "\n" + blocks.get(name, f"<!-- missing block {name} -->") + "\n"
    md_text = re.sub(r"^::block\s+([\w-]+)\s*$", blk, md_text, flags=re.M)
    conv = markdown.Markdown(extensions=["toc", "tables", "sane_lists", "attr_list"],
                             extension_configs={"toc": {"slugify": slugify, "toc_depth": "2"}})
    out = conv.convert(md_text)
    toc = [{"id": t["id"], "name": html.unescape(t["name"])} for t in conv.toc_tokens]
    # internal links -> site-relative, external links open in new tab
    out = re.sub(r'href="https?://(?:www\.)?(?:mesmatters|shopfloormatters)\.com(/[^"]*)?"', lambda m: f'href="{base}{m.group(1) or "/"}"', out)
    out = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', out)
    out = re.sub(r'(src|href)="/(?!/)', lambda m: f'{m.group(1)}="{base}/', out)
    out = re.sub(r"<table>", '<div class="table-wrap"><table>', out).replace("</table>", "</table></div>")
    out = re.sub(r"<img ", '<img loading="lazy" ', out)
    return out, toc


def load_schedule():
    """slug -> release date (UK) from content/schedule.yaml."""
    path = ROOT / "content" / "schedule.yaml"
    if not path.exists():
        return {}
    cfg = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    start = cfg.get("start")
    if isinstance(start, str):
        start = dt.date.fromisoformat(start)
    return {slug: start + dt.timedelta(weeks=i) for i, slug in enumerate(cfg.get("weekly") or [])}


def publish_all_now():
    path = ROOT / "content" / "schedule.yaml"
    cfg = yaml.safe_load(path.read_text(encoding="utf-8")) or {} if path.exists() else {}
    return bool(cfg.get("publish_all_now"))


def uk_today():
    override = os.environ.get("BUILD_DATE")
    if override:
        return dt.date.fromisoformat(override)
    try:
        from zoneinfo import ZoneInfo
        return dt.datetime.now(ZoneInfo("Europe/London")).date()
    except Exception:
        return dt.date.today()


ANSWERS = yaml.safe_load((ROOT / "content" / "answers.yaml").read_text(encoding="utf-8")) if (ROOT / "content" / "answers.yaml").exists() else {}
ANSWERS = ANSWERS or {}


def month_year(d):
    return d.strftime("%B %Y") if d else ""


def load_posts(base, blocks, seo, include_scheduled=False):
    posts = []
    schedule = {} if publish_all_now() else load_schedule()
    today = uk_today()
    sources = sorted((ROOT / "content" / "legacy" / "posts").glob("*.md")) + sorted((ROOT / "content" / "posts").glob("*.md"))
    seen = {}
    for path in sources:
        fm, body = parse_md(path)
        if fm.get("draft"):
            continue
        slug = fm.get("slug") or path.stem
        meta = {**fm, **seo.get(slug, {})}
        if slug in schedule:
            if schedule[slug] > today and not include_scheduled:
                continue
            meta["published"] = schedule[slug].isoformat()
            meta.pop("updated", None)
        published = parse_date(meta.get("published"))
        updated = parse_date(meta.get("updated")) or published
        cat = CAT_BY_KEY[meta.get("category", "education")]
        words = len(re.findall(r"[A-Za-z0-9']+", body))
        html_body, toc = render_body(body, base, blocks)
        extra = ANSWERS.get(slug, {})
        p = {
            "slug": slug,
            "title": html.unescape(meta.get("title", slug)),
            "short": meta.get("short") or html.unescape(meta.get("title", slug)),
            "description": meta.get("description", ""),
            "category_key": cat["key"], "category_slug": cat["slug"], "category_label": cat["name"],
            "art": meta.get("art", "hexgrid"),
            "series": meta.get("series"), "guide": bool(meta.get("guide")), "order": meta.get("order", 0), "start": meta.get("start"),
            "published": published, "updated": updated,
            "published_iso": published.date().isoformat() if published else "",
            "updated_iso": updated.date().isoformat() if updated else "",
            "date_long": long_date(published), "updated_long": long_date(updated) if updated and published and updated.date() != published.date() else "",
            "date_short": short_date(published),
            "words": words, "read_time": max(1, math.ceil(words / 230)),
            "body": html_body, "toc": toc,
            "canonical": f"{SITE}/post/{slug}",
            "md": body,
            "summary": extra.get("summary", ""), "summary_label": extra.get("label", "Summary"),
            "faq": extra.get("faq", []),
            "reviewed": parse_date(extra.get("reviewed")) or updated,
        }
        p["reviewed_long"] = month_year(p["reviewed"])
        seen[slug] = p
    posts = sorted(seen.values(), key=lambda p: p["published"] or dt.datetime(2000, 1, 1), reverse=True)
    # links to articles that aren't released yet become plain text until they are
    live = set(seen)
    pat = re.compile(r'<a href="' + re.escape(base) + r'/post/([\w-]+)"[^>]*>(.*?)</a>', re.S)
    for p in posts:
        p["body"] = pat.sub(lambda m: m.group(0) if m.group(1) in live else m.group(2), p["body"])
    return posts


def jsonld(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def load_glossary(posts):
    f = ROOT / "content" / "glossary.yaml"
    if not f.exists():
        return []
    data = yaml.safe_load(f.read_text(encoding="utf-8")) or []
    by_slug = {p["slug"]: p for p in posts}
    for g in data:
        g["slug"] = g.get("slug") or slugify(g["term"])
        g["articles"] = [by_slug[a] for a in g.get("articles", []) if a in by_slug]
    names = {g["slug"]: g for g in data}
    for g in data:
        g["see"] = [names[x] for x in g.get("see_also", []) if x in names]
    return sorted(data, key=lambda g: g["term"].lower())


FAQ_TOPICS = [
    {"id": "basics", "name": "MES, MOM and ERP basics", "blurb": "What the systems are, and how they differ.", "color": "#a594ff", "rgb": "165,148,255",
     "icon": "M4 6h16M4 12h16M4 18h10",
     "slugs": ["what-is-mes-and-why-is-it-important-in-manufacturing", "mes-vs-mom", "what-is-erp", "mes-vs-erp", "implementing-mes-can-simplify-your-erp", "mes-mom-erp-compared"]},
    {"id": "strategy", "name": "Smart factory strategy", "blurb": "Where to start, and the order that works.", "color": "#ff8fe0", "rgb": "255,143,224",
     "icon": "M4 20l5-6 4 3 7-9M15 8h5v5",
     "slugs": ["what-is-a-smart-factory", "smart-manufacturing-maturity-model", "smart-factory-where-to-start", "how-to-modernise-a-factory"]},
    {"id": "buying", "name": "Choosing and delivering", "blurb": "Selection, business cases, deployment and timelines.", "color": "#ffb86b", "rgb": "255,184,107",
     "icon": "M9 12l2 2 4-4M5 4h14v16H5z",
     "slugs": ["how-to-choose-an-mes", "mes-business-case", "build-vs-buy-mes", "cloud-vs-on-premises-mes", "how-long-does-mes-implementation-take"]},
    {"id": "shopfloor", "name": "Running the shopfloor", "blurb": "Operators, traceability and maintenance.", "color": "#3ddc97", "rgb": "61,220,151",
     "icon": "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21c1-4 4-6 8-6s7 2 8 6",
     "slugs": ["shopfloor-applications-explained", "connected-worker-one-app-not-five", "lot-vs-serial-traceability", "preventive-vs-predictive-maintenance"]},
    {"id": "performance", "name": "Measuring performance", "blurb": "OEE and the measures around it.", "color": "#ff8a70", "rgb": "255,138,112",
     "icon": "M12 21a9 9 0 1 1 9-9M12 12l5-5",
     "slugs": ["what-is-oee-overall-equipment-effectiveness", "oee-vs-teep"]},
    {"id": "architecture", "name": "Architecture and integration", "blurb": "ISA-95, connectivity and the systems around MES/MOM.", "color": "#7fa6ff", "rgb": "127,166,255",
     "icon": "M5 5h5v5H5zM14 14h5v5h-5zM10 7.5h4.5V14",
     "slugs": ["what-is-the-isa-95-model-and-where-does-mes-fit", "it-vs-ot", "opc-ua-vs-mqtt", "iiot-vs-mes", "scada-vs-mes", "historian-vs-mes"]},
]

GLOSSARY_SKIP = {"ai", "erp", "mes", "mom", "batch", "lot", "routing", "edge", "smart-factory", "bottleneck", "changeover", "cycle-time", "scrap-rate",
                 "shopfloor", "availability", "performance", "yield", "recall", "configuration", "customisation", "rework", "throughput",
                 "production-order", "recipe", "lean", "copilot", "validation", "quality-rate", "cavity", "andon", "gemba", "super-user",
                 "change-management", "process-mapping", "traveller", "time-series-data", "saas", "hypercare",
                 "defect", "deviation", "sensor", "barcode", "picking", "putaway", "batch-size", "simulation", "utilisation",
                 "continuous-improvement", "kpi", "spare-parts", "gateway", "goods-receipt", "shelf-life", "smart-manufacturing",
                 "procurement", "supply-chain", "lead-time", "master-data", "digital-transformation", "demand-planning", "capacity-planning"}


def autolink_glossary(posts, glossary, base, limit=6):
    """Link the first mention of glossary terms in each article's paragraphs and list items."""
    terms = []
    for g in glossary:
        if g["slug"] in GLOSSARY_SKIP:
            continue
        forms = [g["term"]] + ([g["term"].lower()] if not g["term"].isupper() and g["term"].lower() != g["term"] else [])
        rx = re.compile(r"(?<![\w/-])(" + "|".join(re.escape(f) for f in forms) + r")(?![\w/-])")
        terms.append((g, rx))
    block = re.compile(r"<(p|li)>(.*?)</\1>", re.S)
    for p in posts:
        if p["slug"] == "smart-factory-glossary":
            continue
        used, count = set(), [0]

        def fix_block(m):
            inner = m.group(2)
            parts = re.split(r"(<a\b.*?</a>|<[^>]+>)", inner, flags=re.S)
            for i, part in enumerate(parts):
                if not part or part.startswith("<"):
                    continue
                for g, rx in terms:
                    if count[0] >= limit:
                        break
                    if g["slug"] in used or (g["articles"] and g["articles"][0]["slug"] == p["slug"]):
                        continue
                    mm = rx.search(part)
                    if mm:
                        used.add(g["slug"]); count[0] += 1
                        link = f'<a class="gloss" href="{base}/glossary/{g["slug"]}" title="{html.escape(g["short"])}">{mm.group(1)}</a>'
                        part = part[:mm.start()] + link + part[mm.end():]
                        # don't re-scan inside the new link
                        before, after = part.split(link, 1)
                        parts[i] = before + link + after
                        break
                else:
                    continue
            return f"<{m.group(1)}>" + "".join(parts) + f"</{m.group(1)}>"

        p["body"] = block.sub(fix_block, p["body"])


def glossary_mentions(posts, glossary):
    """For each term, the articles that mention it, most mentions first."""
    for g in glossary:
        forms = []
        for f in [g["term"], g.get("stands")]:
            if not f:
                continue
            acronym = f.replace("&", "").replace(" ", "").isupper() or any(ch.isdigit() for ch in f)
            forms.append((f, 0 if acronym else re.I))
        found = []
        for p in posts:
            text = re.sub(r"\]\([^)]*\)", "]", p["md"])
            n = sum(len(re.findall(r"(?<![\w-])" + re.escape(f) + r"(?![\w-])", text, flags)) for f, flags in forms)
            if n:
                found.append((n, p))
        found.sort(key=lambda x: (-x[0], x[1]["title"]))
        g["mentions"] = [{"post": p, "n": n} for n, p in found]


def md_clean(md):
    md = re.sub(r"^::block\s+[\w-]+\s*$", "", md, flags=re.M)
    md = re.sub(r"\]\((/[^)]*)\)", lambda m: f"]({SITE}{m.group(1)})", md)
    return md.strip()


def write_llms(posts, paths, glossary):
    by_cat = {}
    for p in posts:
        by_cat.setdefault(p["category_label"], []).append(p)
    out = ["# Shopfloor Matters", "",
           "> Practical, vendor-neutral writing on the smart factory, shopfloor AI and the MES/MOM systems underneath them, "
           "by Matt Barber (VP & General Manager, MES at Infor; former MES developer, implementation lead and head of product). "
           "Covers MES, MOM, ISA-95, OEE, connected worker, integration with ERP, PLM, WMS, APS, QMS, LIMS and CMMS, implementation and the business case.", "",
           "Cite as: Matt Barber, Shopfloor Matters, " + SITE + ". Quoting with attribution and a link is welcome.", "",
           "## Start here", "",
           *[f"- [{g['title']}]({g['canonical']}): {g['summary'] or g['description']}" for g in posts if g.get("guide")],
           f"- [Learning paths]({SITE}/paths/): guided routes through the articles, in order",
           f"- [FAQ]({SITE}/faq/): short answers to common questions, each linked to the full article",
           f"- [Glossary]({SITE}/glossary/): definitions of MES, MOM, OEE, ISA-95, UNS and other shopfloor terms",
           f"- [About Matt Barber]({SITE}/about): background and credentials",
           f"- [Podcasts, interviews and press]({SITE}/featured)",
           f"- [Full text of every article]({SITE}/llms-full.txt)", ""]
    for cat, ps in by_cat.items():
        out += [f"## {cat}", ""]
        for p in ps:
            out.append(f"- [{p['title']}]({p['canonical']}): {p['summary'] or p['description']}")
        out.append("")
    out += ["## Learning paths", ""]
    for x in paths:
        out.append(f"- [{x['title']}]({SITE}/paths/{x['id']}): {x['blurb']}")
    (DIST / "llms.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    full = ["# Shopfloor Matters: full text", "", f"By Matt Barber. Source: {SITE}. Cite as: Matt Barber, Shopfloor Matters, with a link to the article.", ""]
    for p in posts:
        full += ["---", "", f"# {p['title']}", "", f"URL: {p['canonical']}", f"Author: Matt Barber", f"Published: {p['published_iso']}  Last updated: {p['reviewed'].date().isoformat() if p['reviewed'] else ''}", ""]
        if p["summary"]:
            full += [f"Summary: {p['summary']}", ""]
        full += [md_clean(p["md"]), ""]
        if p["faq"]:
            full += ["## Frequently asked questions", ""]
            for f in p["faq"]:
                full += [f"**{f['q']}**", "", f["a"], ""]
    if glossary:
        full += ["---", "", "# Glossary", "", f"URL: {SITE}/glossary/", ""]
        for g in glossary:
            name = g["term"] + (f" ({g['stands']})" if g.get("stands") else "")
            full += [f"## {name}", "", g["short"], "", g.get("body", ""), "", f"URL: {SITE}/glossary/{g['slug']}", ""]
    (DIST / "llms-full.txt").write_text("\n".join(full) + "\n", encoding="utf-8")


def write_feeds(posts, paths):
    from email.utils import format_datetime

    def rss(title, link, desc, items, path):
        x = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/">', "<channel>",
             f"<title>{html.escape(title)}</title>", f"<link>{link}</link>", f"<description>{html.escape(desc)}</description>", "<language>en-gb</language>",
             f'<atom:link href="{SITE}/{path}" rel="self" type="application/rss+xml"/>']
        for p in items:
            d = p["published"].replace(tzinfo=dt.timezone.utc) if p["published"] else None
            x += ["<item>", f"<title>{html.escape(p['title'])}</title>", f"<link>{p['canonical']}</link>", f"<guid>{p['canonical']}</guid>",
                  f"<description>{html.escape(p['summary'] or p['description'])}</description>",
                  f"<content:encoded><![CDATA[{p['body'].replace(']]>', ']]&gt;')}]]></content:encoded>",
                  f"<author>noreply@shopfloormatters.com (Matt Barber)</author>", f"<category>{html.escape(p['category_label'])}</category>"]
            if d:
                x.append(f"<pubDate>{format_datetime(d)}</pubDate>")
            x.append("</item>")
        x += ["</channel>", "</rss>"]
        out = DIST / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(x) + "\n", encoding="utf-8")
    rss("Shopfloor Matters", SITE + "/", "Practical writing on the smart factory, shopfloor AI and MES/MOM, by Matt Barber.", posts, "feed.xml")
    for x in paths:
        rss(f"Shopfloor Matters: {x['title']}", f"{SITE}/paths/{x['id']}", x["blurb"], [s["post"] for s in x["stations"]], f"paths/{x['id']}.xml")


# ------------------------------------------------------------------ build
def relativise(page_html, rel):
    """Rewrite root-relative links for a static preview with no server rewrites."""
    depth = rel.count("/")
    prefix = "." if depth == 0 else "/".join([".."] * depth)
    def fix(m):
        attr, path, tail = m.group(1), m.group(2), m.group(3)
        if not path:
            path = "index.html"
        elif path.endswith("/"):
            path = path + "index.html"
        elif "." not in path.rsplit("/", 1)[-1]:
            path = path.rstrip("/") + ".html"
        return f'{attr}="{prefix}/{path}{tail}"'
    page_html = re.sub(r'(href|src)="@REL@/([^"#?]*)([^"]*)"', fix, page_html)
    page_html = page_html.replace('"@REL@"', f'"{prefix}/index.html"')
    return page_html


def build(base, relative=False, include_scheduled=False):
    base = "@REL@" if relative else base.rstrip("/")
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "public", DIST, ignore=shutil.ignore_patterns("legacy"))
    # only ship legacy images that are actually referenced
    seo = yaml.safe_load((ROOT / "content" / "seo.yaml").read_text(encoding="utf-8")) or {}
    blocks = {p.stem: p.read_text(encoding="utf-8") for p in (ROOT / "content" / "blocks").glob("*.html")}
    posts = load_posts(base, blocks, seo, include_scheduled)
    for p in posts:
        for img in re.findall(r'/images/legacy/([^"\')\s]+)', p["body"]):
            src = ROOT / "public" / "images" / "legacy" / img
            if src.exists():
                (DIST / "images" / "legacy").mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, DIST / "images" / "legacy" / img)

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True, trim_blocks=True, lstrip_blocks=True)
    version = dt.datetime.now().strftime("%Y%m%d%H%M")
    common = {"base": base, "nav": NAV, "linkedin": LINKEDIN, "year": dt.date.today().year, "version": version, "kit_form": KIT_FORM_ID,
              "categories": [], "jsonld": []}

    for c in CATEGORIES:
        c["posts"] = [p for p in posts if p["category_key"] == c["key"]]
    common["categories"] = CATEGORIES

    featured = load_featured()
    person = {"@type": "Person", "@id": f"{SITE}/about#matt", "name": "Matt Barber", "url": f"{SITE}/about",
              "sameAs": [LINKEDIN, "https://www.industrysagemedia.com/matt-barber",
                         "https://manufacturingdigital.com/articles/lifetime-of-achievement-matt-barber"],
              "jobTitle": "VP & General Manager, MES", "worksFor": {"@type": "Organization", "name": "Infor"},
              "knowsAbout": ["Manufacturing Execution Systems (MES)", "Manufacturing Operations Management (MOM)",
                             "Smart factory", "Shopfloor AI", "Connected worker", "ISA-95", "OEE",
                             "ERP and MES integration", "Industry 4.0", "Manufacturing digital transformation"],
              "image": f"{SITE}/images/matt-barber.jpg",
              "award": "Infor Circle of Excellence, 2024", "alumniOf": [{"@type": "CollegeOrUniversity", "name": "The University of Sheffield"}, {"@type": "CollegeOrUniversity", "name": "The London School of Economics and Political Science"}], "hasOccupation": {"@type": "Occupation", "name": "MES software executive",
              "description": "Involved in hundreds of MES projects across food and beverage, automotive, packaging, metal and plastics fabrication and industrial manufacturing."}}
    person_full = {**person, "description": "Matt Barber studied computer science at the University of Sheffield, started as an MES software engineer and has been VP & General Manager, MES at Infor since 2024. He writes Shopfloor Matters, about the smart factory, shopfloor AI and MES/MOM.",
                   "subjectOf": [{"@type": {"podcast": "PodcastEpisode", "webinar": "CreativeWork"}.get(it.get("type"), "Article"),
                                  "name": it["title"], "url": next((l["url"] for l in it.get("links", [])), None),
                                  "publisher": {"@type": "Organization", "name": it.get("outlet", "")}}
                                 for it in featured["items"] if it.get("links")]}
    org = {"@type": "Organization", "name": "Shopfloor Matters", "url": SITE, "logo": f"{SITE}/favicon.svg"}

    def write(rel, tpl, **ctx):
        out = DIST / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        data = {**common, **ctx}
        data.setdefault("og_image", f"{SITE}/images/og/home.png")
        page = env.get_template(tpl).render(**data)
        if relative:
            page = relativise(page, rel)
        out.write_text(page, encoding="utf-8")

    from markupsafe import Markup

    series = sorted([p for p in posts if p["series"] == "functionality"], key=lambda p: p["order"])
    start = sorted([p for p in posts if p["start"]], key=lambda p: p["start"])
    total_words = sum(p["words"] for p in posts)

    paths, paths_home = load_paths(posts)
    glossary = load_glossary(posts)
    autolink_glossary(posts, glossary, base)
    glossary_mentions(posts, glossary)
    common["paths_home"] = paths_home
    common["paths_json"] = json.dumps([{"id": p["id"], "title": p["title"], "slugs": p["slugs"],
                                        "titles": [st["post"]["short"] for st in p["stations"]]} for p in paths], separators=(",", ":"))
    common["featured_carousel"] = featured["carousel"]

    # home
    write("index.html", "home.html", active="home",
          seo_title="Shopfloor Matters | The smart factory, shopfloor AI and MES",
          description="Practical, vendor-neutral writing on the smart factory and shopfloor AI, and the MES and MOM systems underneath them. By Matt Barber.",
          canonical=f"{SITE}/", posts=posts, series=series, start=start, latest=posts[:5],
          start_minutes=sum(p["read_time"] for p in start), total_words_k=round(total_words / 1000),
          jsonld=[jsonld({"@context": "https://schema.org", "@type": "WebSite", "name": "Shopfloor Matters", "url": SITE,
                          "description": "Practical guides to MES, MOM and smart manufacturing", "author": person, "publisher": org})])

    # all articles
    write("articles.html", "list.html", active="articles",
          seo_title="All articles | Shopfloor Matters", description="Every article on the smart factory, shopfloor AI, implementation and the MES and MOM foundations underneath them.",
          canonical=f"{SITE}/articles", eyebrow=f"Library / {len(posts)} articles", heading="Every article, in one place",
          kicker="Guides, explainers and opinion on the smart factory, shopfloor AI and MES/MOM. Newest first.",
          all_count=len(posts), featured=posts[0],
          groups=[g for g in ({"label": "The essential guides", "posts": [q for q in posts[1:] if q.get("guide")]},
                              {"label": "Everything else", "posts": [q for q in posts[1:] if not q.get("guide")]}) if g["posts"]])

    # categories (same URLs as the Wix site)
    for c in CATEGORIES:
        cposts = c["posts"]
        groups = []
        if c["key"] == "education":
            groups.append({"label": "Start here", "posts": start, "numbered": True})
            groups.append({"label": "The MES functionality series", "posts": series, "numbered": True})
            rest = [p for p in cposts if p not in start and p not in series]
            if rest:
                groups.append({"label": "More fundamentals", "posts": rest})
        else:
            groups.append({"label": None, "posts": cposts})
        write(f"{c['slug']}.html", "list.html", active=c["slug"],
              seo_title=f"{c['name']} | Shopfloor Matters", description=c["kicker"][:158],
              canonical=f"{SITE}/{c['slug']}", eyebrow=f"{c['eyebrow']} / {len(cposts)} articles",
              heading=c["name"], kicker=c["kicker"], all_count=len(posts), featured=None, groups=groups,
              og_image=f"{SITE}/images/og/page-{c['art']}.png")

    # posts
    for p in posts:
        same = [q for q in posts if q is not p]
        if p["series"]:
            seq = series
        elif p["start"]:
            seq = start
        else:
            seq = [q for q in reversed(posts) if q["category_key"] == p["category_key"]]
        i = seq.index(p)
        prev = seq[i - 1] if i > 0 else None
        nxt = seq[i + 1] if i + 1 < len(seq) else None
        related = [q for q in same if q["category_key"] == p["category_key"] and q not in (prev, nxt)]
        related = (related + [q for q in same if q not in related and q not in (prev, nxt)])[:3]
        ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["description"],
              "datePublished": p["published_iso"], "dateModified": p["updated_iso"], "author": person, "publisher": org,
              "mainEntityOfPage": p["canonical"], "url": p["canonical"], "image": f"{SITE}/images/og/{p['slug']}.png",
              "articleSection": p["category_label"], "wordCount": p["words"], "inLanguage": "en-GB"}
        if p["summary"]:
            ld["abstract"] = p["summary"]
        extra_ld = []
        if p["faq"]:
            extra_ld.append(jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in p["faq"]]}))
        crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": p["category_label"], "item": f"{SITE}/{p['category_slug']}"},
            {"@type": "ListItem", "position": 3, "name": p["short"], "item": p["canonical"]}]}
        write(f"post/{p['slug']}.html", "post.html", active=p["category_slug"], progress=True,
              seo_title=(p["title"] if len(p["title"]) > 42 else f"{p['title']} | Shopfloor Matters"), og_title=p["title"], og_type="article",
              description=p["description"], canonical=p["canonical"], og_image=f"{SITE}/images/og/{p['slug']}.png",
              p=p, body=Markup(p["body"]), toc=p["toc"], series_posts=series if p["series"] else None,
              prev=prev, next=nxt, related=related, jsonld=[jsonld(ld), jsonld(crumbs)] + extra_ld)

    # learning paths
    write("paths/index.html", "paths.html", active="paths", seo_title="Learning paths | Shopfloor Matters",
          description="Six guided learning paths through the smart factory, MES/MOM, shopfloor AI and implementation. Articles in the right order, with your progress saved as you read.",
          canonical=f"{SITE}/paths/", paths=paths, og_image=f"{SITE}/images/og/page-education.png")
    for path in paths:
        write(f"paths/{path['id']}.html", "path.html", active="paths", seo_title=f"{path['title']}: learning path | Shopfloor Matters",
              description=f"{path['blurb']} {path['n']} articles, about {path['minutes']} minutes.",
              canonical=f"{SITE}/paths/{path['id']}", path=path, integration_map=blocks.get("integration-map", ""), og_image=f"{SITE}/images/og/{path['image']}.png",
              jsonld=[jsonld({"@context": "https://schema.org", "@type": "ItemList", "name": path["title"],
                              "itemListElement": [{"@type": "ListItem", "position": s["n"], "url": s["post"]["canonical"], "name": s["post"]["title"]} for s in path["stations"]]})])

    # featured
    kinds = [("podcast", "Podcasts", "podcasts"), ("article", "Press", "press features"), ("webinar", "Webinars", "webinar")]
    counts = [{"key": k, "short": sh, "label": lab, "n": sum(1 for i in featured["items"] if i["type"] == k)} for k, sh, lab in kinds]
    write("featured.html", "featured.html", active="featured", seo_title="Podcasts, interviews and press | Shopfloor Matters",
          description="Matt Barber on podcasts, webinars and in the trade press, talking MES, the smart factory and shopfloor AI. Watch, listen or read.",
          canonical=f"{SITE}/featured", items=featured["items"], counts=[c for c in counts if c["n"]], og_image=f"{SITE}/images/og/page-about.png",
          jsonld=[jsonld({"@context": "https://schema.org", "@type": "ItemList", "name": "Matt Barber in the media",
                          "itemListElement": [{"@type": "ListItem", "position": n + 1, "url": i["links"][0]["url"], "name": f"{i['title']} ({i['outlet']})"}
                                              for n, i in enumerate(featured["items"])]})])

    # about / contact / 404
    about = (ROOT / "content" / "pages" / "about.html").read_text(encoding="utf-8").replace("{{base}}", base)
    write("about.html", "page.html", active="about", seo_title="About Matt Barber | Shopfloor Matters",
          description="Matt Barber went from writing MES code to running a global MES business. Why he writes about the smart factory and shopfloor AI.",
          canonical=f"{SITE}/about", eyebrow="About", heading="Hi, I'm Matt.",
          kicker="I've spent my career on the shopfloor side of software. This is where I write down what I've learnt about making factories smarter.",
          content=Markup(about), show_cta=True, og_image=f"{SITE}/images/og/page-about.png",
          jsonld=[jsonld({"@context": "https://schema.org", "@type": "ProfilePage", "mainEntity": person_full})])
    contact = (ROOT / "content" / "pages" / "contact.html").read_text(encoding="utf-8").replace("{{base}}", base).replace("{{linkedin}}", LINKEDIN)
    write("contact.html", "page.html", active="contact", seo_title="Contact | Shopfloor Matters",
          description="Get in touch with Matt Barber about the smart factory, shopfloor AI, MES and MOM, or something you've read here.",
          canonical=f"{SITE}/contact", eyebrow="Contact", heading="Let's talk shopfloor",
          kicker="The quickest way to reach me is a message on LinkedIn. I read everything, even if replies sometimes take a few days.",
          actions=Markup(f'<a class="btn" href="{LINKEDIN}" target="_blank" rel="me noopener">Message me on LinkedIn →</a>'),
          content=Markup(contact), show_cta=False)
    write("subscribe.html", "page.html", active="subscribe", seo_title="Subscribe to the newsletter | Shopfloor Matters",
          description="A practical newsletter on the smart factory, shopfloor AI and MES/MOM. New articles and lessons from real implementations, straight to your inbox.",
          canonical=f"{SITE}/subscribe", eyebrow="Newsletter", heading="Smart factory thinking, in your inbox",
          kicker="New articles and practical lessons on the smart factory, shopfloor AI and MES/MOM. Written from real implementations. No hype, no spam.",
          actions=Markup(env.get_template("macros.html").module.signup(base, KIT_FORM_ID, big=True)),
          content=Markup((ROOT / "content" / "pages" / "subscribe.html").read_text(encoding="utf-8")), show_cta=False)
    privacy = (ROOT / "content" / "pages" / "privacy.html").read_text(encoding="utf-8").replace("{{base}}", base)
    write("privacy.html", "page.html", active=None, seo_title="Privacy | Shopfloor Matters",
          description="How Shopfloor Matters handles your data, including newsletter sign-ups.",
          canonical=f"{SITE}/privacy", eyebrow="Privacy", heading="Your data, plainly",
          kicker="What I collect, why, and how to get it removed.", content=Markup(privacy), show_cta=False)
    write("404.html", "page.html", active=None, seo_title="Page not found | Shopfloor Matters", description="This page doesn't exist.",
          canonical=f"{SITE}/404", eyebrow="404", heading="This line has stopped.", noindex=True,
          kicker="The page you were looking for isn't here. It may have moved when the site was rebuilt.",
          actions=Markup(f'<a class="btn" href="{base}/articles">Browse all articles →</a><a class="btn ghost" href="{base}/">Home</a>'),
          content=Markup(""), show_cta=False)

    # redirects for old Wix URLs
    for old, new in REDIRECTS.items():
        out = DIST / f"{old}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        page = env.get_template("redirect.html").render(target=f"{base}{new}", canonical=f"{SITE}{new}")
        if relative:
            page = relativise(page, f"{old}.html").replace('"@REL@/', '"' + ("/".join([".."] * old.count("/")) or ".") + "/").replace(new + '"', new + '.html"')
        out.write_text(page, encoding="utf-8")

    # FAQ hub
    by_slug_all = {p["slug"]: p for p in posts}
    faq_topics, faq_all = [], []
    for t in FAQ_TOPICS:
        items = [{"q": f["q"], "a": f["a"], "post": by_slug_all[sl]} for sl in t["slugs"] if sl in by_slug_all for f in by_slug_all[sl]["faq"]]
        if items:
            faq_topics.append({**t, "items": items})
            faq_all += items
    if faq_all:
        write("faq/index.html", "faq.html", active="faq", seo_title="MES, MOM and smart factory FAQ | Shopfloor Matters",
              description=f"Straight answers to {len(faq_all)} common questions about MES, MOM, ERP, OEE, the smart factory and shopfloor systems, each linked to the full article.",
              canonical=f"{SITE}/faq/", topics=faq_topics, total=len(faq_all),
              jsonld=[jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": i["q"], "acceptedAnswer": {"@type": "Answer", "text": i["a"], "url": i["post"]["canonical"]}} for i in faq_all]})])

    # glossary
    if glossary:
        gset = {"@type": "DefinedTermSet", "@id": f"{SITE}/glossary/#set", "name": "Shopfloor Matters glossary", "url": f"{SITE}/glossary/"}
        for g in glossary:
            g["letter"] = "0–9" if g["term"][0].isdigit() else g["term"][0].upper()
        letters = sorted({g["letter"] for g in glossary}, key=lambda x: (x != "0–9", x))
        write("glossary/index.html", "glossary.html", active="glossary", seo_title="Smart factory and MES glossary | Shopfloor Matters",
              description="Plain-English definitions of MES, MOM, OEE, ISA-95, UNS and the other terms you'll hear in smart factory and shopfloor projects.",
              canonical=f"{SITE}/glossary/", terms=glossary, letters=letters,
              jsonld=[jsonld({"@context": "https://schema.org", **gset, "hasDefinedTerm": [
                  {"@type": "DefinedTerm", "name": g["term"], "description": g["short"], "url": f"{SITE}/glossary/{g['slug']}",
                   **({"alternateName": g["stands"]} if g.get("stands") else {})} for g in glossary]})])
        for g in glossary:
            name = g["term"] + (f" ({g['stands']})" if g.get("stands") else "")
            write(f"glossary/{g['slug']}.html", "term.html", active="glossary", seo_title=f"{name}: meaning in manufacturing | Shopfloor Matters",
                  description=g["short"], canonical=f"{SITE}/glossary/{g['slug']}", g=g,
                  jsonld=[jsonld({"@context": "https://schema.org", "@type": "DefinedTerm", "name": g["term"], "description": g["short"] + " " + g.get("body", ""),
                                  "url": f"{SITE}/glossary/{g['slug']}", "inDefinedTermSet": gset,
                                  **({"alternateName": g["stands"]} if g.get("stands") else {})}),
                          jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                              {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                              {"@type": "ListItem", "position": 2, "name": "Glossary", "item": f"{SITE}/glossary/"},
                              {"@type": "ListItem", "position": 3, "name": g["term"]}]})])

    # sitemap, robots
    urls = [(f"{SITE}/", posts[0]["updated"]), (f"{SITE}/articles", posts[0]["updated"]), (f"{SITE}/about", None), (f"{SITE}/subscribe", None)]
    urls += [(f"{SITE}/{c['slug']}", None) for c in CATEGORIES]
    urls += [(f"{SITE}/featured", None), (f"{SITE}/paths/", None)] + [(f"{SITE}/paths/{x['id']}", None) for x in paths]
    urls += [(f"{SITE}/faq/", None), (f"{SITE}/glossary/", None)] + [(f"{SITE}/glossary/{g['slug']}", None) for g in glossary]
    urls += [(p["canonical"], p["updated"]) for p in posts]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, d in urls:
        sm.append(f"  <url><loc>{u}</loc>" + (f"<lastmod>{d.date().isoformat()}</lastmod>" if d else "") + "</url>")
    sm.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai", "PerplexityBot",
            "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot", "Bingbot", "Googlebot", "meta-externalagent", "Amazonbot", "cohere-ai"]
    robots = ["# Shopfloor Matters welcomes search engines and AI assistants.", "# Quote freely with attribution: Matt Barber, Shopfloor Matters (shopfloormatters.com).", ""]
    for b in bots:
        robots += [f"User-agent: {b}", "Allow: /", ""]
    robots += ["User-agent: *", "Allow: /", "", f"Sitemap: {SITE}/sitemap.xml", ""]
    (DIST / "robots.txt").write_text("\n".join(robots), encoding="utf-8")
    write_llms(posts, paths, glossary)
    write_feeds(posts, paths)

    (DIST / ".nojekyll").write_text("")
    if relative:
        for f in DIST.rglob("*.html"):
            depth = len(f.relative_to(DIST).parts) - 1
            t = f.read_text(encoding="utf-8")
            if "@REL@" in t:
                f.write_text(t.replace("@REL@", "/".join([".."] * depth) or "."), encoding="utf-8")
    print(f"Built {len(posts)} posts into {DIST} (base='{base}')")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="")
    ap.add_argument("--relative", action="store_true", help="relative .html links, for previewing as static files")
    ap.add_argument("--all", action="store_true", help="include articles scheduled for future weeks")
    args = ap.parse_args()
    build(args.base, args.relative, args.all)
