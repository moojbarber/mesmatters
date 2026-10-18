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
SITE = "https://www.mesmatters.com"
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
    {"key": "start", "label": "Start here", "desc": "What is MES/MOM? The essential guide", "href": "/post/what-is-mes-and-why-is-it-important-in-manufacturing"},
    {"key": "articles", "label": "Articles", "desc": "Everything, newest first", "href": "/articles"},
    {"key": "thought-leadership", "label": "Smart Factory & AI", "desc": "Strategy, shopfloor AI, connected worker", "href": "/thought-leadership"},
    {"key": "mes-education", "label": "Foundations", "desc": "MES, MOM, OEE, ISA-95 explained", "href": "/mes-education"},
    {"key": "mes-advice", "label": "Implementation", "desc": "Selecting, deploying and adopting MES", "href": "/mes-advice"},
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
    # links to articles that aren't released yet become plain text until they are
    live = set(seen)
    pat = re.compile(r'<a href="' + re.escape(base) + r'/post/([\w-]+)"[^>]*>(.*?)</a>', re.S)
    for p in posts:
        p["body"] = pat.sub(lambda m: m.group(0) if m.group(1) in live else m.group(2), p["body"])
    return posts


def jsonld(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


# ------------------------------------------------------------------ build
def relativise(page_html, rel):
    """Rewrite root-relative links for a static preview with no server rewrites."""
    depth = rel.count("/")
    prefix = "." if depth == 0 else "/".join([".."] * depth)
    def fix(m):
        attr, path, tail = m.group(1), m.group(2), m.group(3)
        if not path:
            path = "index.html"
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

    person = {"@type": "Person", "name": "Matt Barber", "url": f"{SITE}/about", "sameAs": [LINKEDIN],
              "jobTitle": "VP & General Manager, MES", "image": f"{SITE}/images/matt-barber.jpg"}
    org = {"@type": "Organization", "name": "MES Matters", "url": SITE, "logo": f"{SITE}/favicon.svg"}

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

    # home
    write("index.html", "home.html", active="home",
          seo_title="MES Matters | The smart factory, shopfloor AI and MES",
          description="Practical, vendor-neutral writing on the smart factory and shopfloor AI, and the MES and MOM systems underneath them. By Matt Barber.",
          canonical=f"{SITE}/", posts=posts, series=series, start=start, latest=posts[:5],
          start_minutes=sum(p["read_time"] for p in start), total_words_k=round(total_words / 1000),
          jsonld=[jsonld({"@context": "https://schema.org", "@type": "WebSite", "name": "MES Matters", "url": SITE,
                          "description": "Practical guides to MES, MOM and smart manufacturing", "author": person, "publisher": org})])

    # all articles
    write("articles.html", "list.html", active="articles",
          seo_title="All articles | MES Matters", description="Every article on the smart factory, shopfloor AI, implementation and the MES and MOM foundations underneath them.",
          canonical=f"{SITE}/articles", eyebrow=f"Library / {len(posts)} articles", heading="Every article, in one place",
          kicker="Guides, explainers and opinion on the smart factory, shopfloor AI and MES/MOM. Newest first.",
          all_count=len(posts), featured=posts[0], groups=[{"label": "Everything else", "posts": posts[1:]}])

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
          description="Matt Barber went from writing MES code to running a global MES business. Why he writes about the smart factory and shopfloor AI.",
          canonical=f"{SITE}/about", eyebrow="About", heading="Hi, I'm Matt.",
          kicker="I've spent my career on the shopfloor side of software. This is where I write down what I've learnt about making factories smarter.",
          content=Markup(about), show_cta=True, og_image=f"{SITE}/images/og/page-about.png",
          jsonld=[jsonld({"@context": "https://schema.org", "@type": "ProfilePage", "mainEntity": person})])
    contact = (ROOT / "content" / "pages" / "contact.html").read_text(encoding="utf-8").replace("{{base}}", base).replace("{{linkedin}}", LINKEDIN)
    write("contact.html", "page.html", active="contact", seo_title="Contact | MES Matters",
          description="Get in touch with Matt Barber about the smart factory, shopfloor AI, MES and MOM, or something you've read here.",
          canonical=f"{SITE}/contact", eyebrow="Contact", heading="Let's talk shopfloor",
          kicker="The quickest way to reach me is a message on LinkedIn. I read everything, even if replies sometimes take a few days.",
          actions=Markup(f'<a class="btn" href="{LINKEDIN}" target="_blank" rel="me noopener">Message me on LinkedIn →</a>'),
          content=Markup(contact), show_cta=False)
    write("subscribe.html", "page.html", active="subscribe", seo_title="Subscribe to the newsletter | MES Matters",
          description="A practical newsletter on the smart factory, shopfloor AI and MES/MOM. New articles and lessons from real implementations, straight to your inbox.",
          canonical=f"{SITE}/subscribe", eyebrow="Newsletter", heading="Smart factory thinking, in your inbox",
          kicker="New articles and practical lessons on the smart factory, shopfloor AI and MES/MOM. Written from real implementations. No hype, no spam.",
          actions=Markup(env.get_template("macros.html").module.signup(base, KIT_FORM_ID, big=True)),
          content=Markup((ROOT / "content" / "pages" / "subscribe.html").read_text(encoding="utf-8")), show_cta=False)
    privacy = (ROOT / "content" / "pages" / "privacy.html").read_text(encoding="utf-8").replace("{{base}}", base)
    write("privacy.html", "page.html", active=None, seo_title="Privacy | MES Matters",
          description="How MES Matters handles your data, including newsletter sign-ups.",
          canonical=f"{SITE}/privacy", eyebrow="Privacy", heading="Your data, plainly",
          kicker="What I collect, why, and how to get it removed.", content=Markup(privacy), show_cta=False)
    write("404.html", "page.html", active=None, seo_title="Page not found | MES Matters", description="This page doesn't exist.",
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

    # sitemap, robots
    urls = [(f"{SITE}/", posts[0]["updated"]), (f"{SITE}/articles", posts[0]["updated"]), (f"{SITE}/about", None), (f"{SITE}/subscribe", None)]
    urls += [(f"{SITE}/{c['slug']}", None) for c in CATEGORIES]
    urls += [(p["canonical"], p["updated"]) for p in posts]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, d in urls:
        sm.append(f"  <url><loc>{u}</loc>" + (f"<lastmod>{d.date().isoformat()}</lastmod>" if d else "") + "</url>")
    sm.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

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
