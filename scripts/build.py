#!/usr/bin/env python3
"""Build mesmatters.com into ./dist

    python scripts/build.py                    # production (served from the domain root)
    python scripts/build.py --base /mesmatters # preview on <user>.github.io/mesmatters

Content:
  content/posts/*.md         new articles (front matter + Markdown)
  content/legacy/posts/*.md  imported Wix articles
  content/seo.yaml           per-article title/description/category overrides
  content/blocks/*.html      reusable on-brand blocks, used in Markdown as `::block name`
"""
import argparse
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
SITE = "https://www.mesmatters.com"
LINKEDIN = "https://www.linkedin.com/in/mattjbarber/"

CATEGORIES = [
    {"key": "education", "slug": "mes-education", "name": "MES Education", "eyebrow": "Learn", "art": "education",
     "blurb": "What MES is, what it does and the standards behind it.",
     "kicker": "The fundamentals of Manufacturing Execution Systems: definitions, standards like ISA-95, KPIs like OEE, and a function-by-function tour of what an MES actually does."},
    {"key": "advice", "slug": "mes-advice", "name": "MES Advice", "eyebrow": "Implement", "art": "advice",
     "blurb": "Business cases, teams and getting projects over the line.",
     "kicker": "Practical guidance for MES and MOM projects: building the business case, getting the team right and avoiding the mistakes that sink implementations."},
    {"key": "thought-leadership", "slug": "thought-leadership", "name": "Thought Leadership", "eyebrow": "Think", "art": "thought-leadership",
     "blurb": "The market, AI and where the shopfloor goes next.",
     "kicker": "Where the MES market is heading, what AI really changes on the shopfloor, and the industry pressures shaping manufacturing systems."},
]
CAT_BY_KEY = {c["key"]: c for c in CATEGORIES}

NAV = [
    {"key": "start", "label": "Start here", "href": "/post/what-is-mes-and-why-is-it-important-in-manufacturing"},
    {"key": "articles", "label": "Articles", "href": "/articles"},
    {"key": "mes-education", "label": "Education", "href": "/mes-education"},
    {"key": "mes-advice", "label": "Advice", "href": "/mes-advice"},
    {"key": "thought-leadership", "label": "Thought Leadership", "href": "/thought-leadership"},
    {"key": "about", "label": "About", "href": "/about"},
]

# Old Wix URLs that should point somewhere new
REDIRECTS = {
    "home/categories/interfacing": "/mes-education",
    "home/categories/mes": "/thought-leadership",
    "home/categories/mes-advice": "/mes-advice",
    "copy-of-education": "/mes-advice",
    "blog": "/articles",
    "challenges": "/articles",
}


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
    out = re.sub(r'href="https?://(?:www\.)?mesmatters\.com(/[^"]*)?"', lambda m: f'href="{base}{m.group(1) or "/"}"', out)
    out = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', out)
    out = re.sub(r'(src|href)="/(?!/)', lambda m: f'{m.group(1)}="{base}/', out)
    out = re.sub(r"<table>", '<div class="table-wrap"><table>', out).replace("</table>", "</table></div>")
    out = re.sub(r"<img ", '<img loading="lazy" ', out)
    return out, toc


def load_posts(base, blocks, seo):
    posts = []
    sources = sorted((ROOT / "content" / "legacy" / "posts").glob("*.md")) + sorted((ROOT / "content" / "posts").glob("*.md"))
    seen = {}
    for path in sources:
        fm, body = parse_md(path)
        if fm.get("draft"):
            continue
        slug = fm.get("slug") or path.stem
        meta = {**fm, **seo.get(slug, {})}
        published = parse_date(meta.get("published"))
        updated = parse_date(meta.get("updated")) or published
        cat = CAT_BY_KEY[meta.get("category", "education")]
        words = len(re.findall(r"[A-Za-z0-9']+", body))
        html_body, toc = render_body(body, base, blocks)
        p = {
            "slug": slug,
            "title": html.unescape(meta.get("title", slug)),
            "short": meta.get("short") or html.unescape(meta.get("title", slug)),
            "description": meta.get("description", ""),
            "category_key": cat["key"], "category_slug": cat["slug"], "category_label": cat["name"],
            "art": meta.get("art", "hexgrid"),
            "series": meta.get("series"), "order": meta.get("order", 0), "start": meta.get("start"),
            "published": published, "updated": updated,
            "published_iso": published.date().isoformat() if published else "",
            "updated_iso": updated.date().isoformat() if updated else "",
            "date_long": long_date(published), "updated_long": long_date(updated) if updated and published and updated.date() != published.date() else "",
            "date_short": short_date(published),
            "words": words, "read_time": max(1, math.ceil(words / 230)),
            "body": html_body, "toc": toc,
            "canonical": f"{SITE}/post/{slug}",
        }
        seen[slug] = p
    posts = sorted(seen.values(), key=lambda p: p["published"] or dt.datetime(2000, 1, 1), reverse=True)
    return posts


def jsonld(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


# ------------------------------------------------------------------ build
def build(base):
    base = base.rstrip("/")
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "public", DIST, ignore=shutil.ignore_patterns("legacy"))
    # only ship legacy images that are actually referenced
    seo = yaml.safe_load((ROOT / "content" / "seo.yaml").read_text(encoding="utf-8")) or {}
    blocks = {p.stem: p.read_text(encoding="utf-8") for p in (ROOT / "content" / "blocks").glob("*.html")}
    posts = load_posts(base, blocks, seo)
    for p in posts:
        for img in re.findall(r'/images/legacy/([^"\')\s]+)', p["body"]):
            src = ROOT / "public" / "images" / "legacy" / img
            if src.exists():
                (DIST / "images" / "legacy").mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, DIST / "images" / "legacy" / img)

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True, trim_blocks=True, lstrip_blocks=True)
    version = dt.datetime.now().strftime("%Y%m%d%H%M")
    common = {"base": base, "nav": NAV, "linkedin": LINKEDIN, "year": dt.date.today().year, "version": version,
              "categories": [], "jsonld": []}

    for c in CATEGORIES:
        c["posts"] = [p for p in posts if p["category_key"] == c["key"]]
    common["categories"] = CATEGORIES

    person = {"@type": "Person", "name": "Matt Barber", "url": f"{SITE}/about", "sameAs": [LINKEDIN],
              "jobTitle": "VP & General Manager, MES", "image": f"{SITE}/images/matt-barber.jpg"}
    org = {"@type": "Organization", "name": "MES Matters", "url": SITE, "logo": f"{SITE}/favicon.svg"}

    def write(rel, tpl, **ctx):
        out = DIST / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        data = {**common, **ctx}
        data.setdefault("og_image", f"{SITE}/images/og/home.png")
        out.write_text(env.get_template(tpl).render(**data), encoding="utf-8")

    from markupsafe import Markup

    series = sorted([p for p in posts if p["series"] == "functionality"], key=lambda p: p["order"])
    start = sorted([p for p in posts if p["start"]], key=lambda p: p["start"])
    total_words = sum(p["words"] for p in posts)

    # home
    write("index.html", "home.html", active="home",
          seo_title="MES Matters | Practical guides to MES, MOM and smart manufacturing",
          description="Straight talk on Manufacturing Execution Systems, MOM and the smart factory. Practical, vendor-neutral guides by Matt Barber.",
          canonical=f"{SITE}/", posts=posts, series=series, start=start, latest=posts[:5],
          start_minutes=sum(p["read_time"] for p in start), total_words_k=round(total_words / 1000),
          jsonld=[jsonld({"@context": "https://schema.org", "@type": "WebSite", "name": "MES Matters", "url": SITE,
                          "description": "Practical guides to MES, MOM and smart manufacturing", "author": person, "publisher": org})])

    # all articles
    write("articles.html", "list.html", active="articles",
          seo_title="All articles | MES Matters", description="Every MES Matters guide: MES fundamentals, the functionality series, implementation advice and thought leadership on MOM and smart manufacturing.",
          canonical=f"{SITE}/articles", eyebrow=f"Library / {len(posts)} articles", heading="Every article, in one place",
          kicker="Guides, explainers and opinion on MES, MOM and the smart factory. Newest first.",
          all_count=len(posts), featured=posts[0], groups=[{"label": "Everything else", "posts": posts[1:]}])

    # categories (same URLs as the Wix site)
    for c in CATEGORIES:
        cposts = c["posts"]
        groups = []
        if c["key"] == "education":
            groups.append({"label": "Start here", "posts": start, "numbered": True})
            groups.append({"label": "The MES Functionality series", "posts": series, "numbered": True})
            rest = [p for p in cposts if p not in start and p not in series]
            if rest:
                groups.append({"label": "More fundamentals", "posts": rest})
        else:
            groups.append({"label": None, "posts": cposts})
        write(f"{c['slug']}.html", "list.html", active=c["slug"],
              seo_title=f"{c['name']} | MES Matters", description=c["kicker"][:158],
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
        crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": p["category_label"], "item": f"{SITE}/{p['category_slug']}"},
            {"@type": "ListItem", "position": 3, "name": p["short"], "item": p["canonical"]}]}
        write(f"post/{p['slug']}.html", "post.html", active=p["category_slug"], progress=True,
              seo_title=f"{p['title']} | MES Matters", og_title=p["title"], og_type="article",
              description=p["description"], canonical=p["canonical"], og_image=f"{SITE}/images/og/{p['slug']}.png",
              p=p, body=Markup(p["body"]), toc=p["toc"], series_posts=series if p["series"] else None,
              prev=prev, next=nxt, related=related, jsonld=[jsonld(ld), jsonld(crumbs)])

    # about / contact / 404
    about = (ROOT / "content" / "pages" / "about.html").read_text(encoding="utf-8").replace("{{base}}", base)
    write("about.html", "page.html", active="about", seo_title="About Matt Barber | MES Matters",
          description="Matt Barber went from writing MES code to running a global MES business. Why he writes MES Matters, and what you'll find here.",
          canonical=f"{SITE}/about", eyebrow="About", heading="Hi, I'm Matt.",
          kicker="I've spent my career on the shopfloor side of software. MES Matters is where I write down what I've learnt.",
          content=Markup(about), show_cta=True, og_image=f"{SITE}/images/og/page-about.png",
          jsonld=[jsonld({"@context": "https://schema.org", "@type": "ProfilePage", "mainEntity": person})])
    contact = (ROOT / "content" / "pages" / "contact.html").read_text(encoding="utf-8").replace("{{base}}", base).replace("{{linkedin}}", LINKEDIN)
    write("contact.html", "page.html", active="contact", seo_title="Contact | MES Matters",
          description="Get in touch with Matt Barber about MES, MOM, smart manufacturing or something you've read on MES Matters.",
          canonical=f"{SITE}/contact", eyebrow="Contact", heading="Let's talk shopfloor",
          kicker="The quickest way to reach me is a message on LinkedIn. I read everything, even if replies sometimes take a few days.",
          actions=Markup(f'<a class="btn" href="{LINKEDIN}" target="_blank" rel="me noopener">Message me on LinkedIn →</a>'),
          content=Markup(contact), show_cta=False)
    write("404.html", "page.html", active=None, seo_title="Page not found | MES Matters", description="This page doesn't exist.",
          canonical=f"{SITE}/404", eyebrow="404", heading="This line has stopped.", noindex=True,
          kicker="The page you were looking for isn't here. It may have moved when the site was rebuilt.",
          actions=Markup(f'<a class="btn" href="{base}/articles">Browse all articles →</a><a class="btn ghost" href="{base}/">Home</a>'),
          content=Markup(""), show_cta=False)

    # redirects for old Wix URLs
    for old, new in REDIRECTS.items():
        out = DIST / f"{old}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(env.get_template("redirect.html").render(target=f"{base}{new}", canonical=f"{SITE}{new}"), encoding="utf-8")

    # sitemap, robots, rss, favicon
    urls = [(f"{SITE}/", posts[0]["updated"]), (f"{SITE}/articles", posts[0]["updated"]), (f"{SITE}/about", None)]
    urls += [(f"{SITE}/{c['slug']}", None) for c in CATEGORIES]
    urls += [(p["canonical"], p["updated"]) for p in posts]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, d in urls:
        sm.append(f"  <url><loc>{u}</loc>" + (f"<lastmod>{d.date().isoformat()}</lastmod>" if d else "") + "</url>")
    sm.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

    def rfc822(d):
        return d.strftime("%a, %d %b %Y %H:%M:%S +0000")
    items = "".join(
        f"<item><title>{html.escape(p['title'])}</title><link>{p['canonical']}</link><guid>{p['canonical']}</guid>"
        f"<pubDate>{rfc822(p['published'])}</pubDate><category>{html.escape(p['category_label'])}</category>"
        f"<description>{html.escape(p['description'])}</description></item>" for p in posts if p["published"])
    (DIST / "feed.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>MES Matters</title><link>{SITE}/</link>'
        f"<description>Practical guides to MES, MOM and smart manufacturing</description><language>en-gb</language>{items}</channel></rss>\n",
        encoding="utf-8")
    (DIST / ".nojekyll").write_text("")
    print(f"Built {len(posts)} posts into {DIST} (base='{base}')")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="")
    args = ap.parse_args()
    build(args.base)
