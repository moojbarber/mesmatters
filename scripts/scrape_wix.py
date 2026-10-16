#!/usr/bin/env python3
"""Scrape mesmatters.com (Wix) into Markdown + images.

Output (relative to repo root):
  content/legacy/posts/<slug>.md    one file per blog post, with front matter
  content/legacy/pages/<slug>.md    static pages (about, contact, category pages...)
  content/legacy/raw/<kind>/<slug>.html   untouched HTML, kept so we can re-convert later
  public/images/legacy/<file>       every image referenced, at original resolution
  content/legacy/inventory.csv      URL / title / date / word count / images per page

Run: python scripts/scrape_wix.py [--site https://www.mesmatters.com]
"""
import argparse
import csv
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
import trafilatura
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "legacy"
IMG_DIR = ROOT / "public" / "images" / "legacy"
IMG_URL_PREFIX = "/images/legacy/"

UA = "Mozilla/5.0 (compatible; MESMattersMigration/1.0; +https://www.mesmatters.com)"
session = requests.Session()
session.headers["User-Agent"] = UA

WIX_MEDIA = re.compile(r"https://static\.wixstatic\.com/media/([A-Za-z0-9_]+~mv2(?:_d_\d+_\d+_s_\d+)?\.[a-zA-Z0-9]+)")


def get(url, retries=3):
    for i in range(retries):
        try:
            r = session.get(url, timeout=30)
            if r.status_code == 200:
                return r
            print(f"  {r.status_code} {url}")
            if r.status_code == 404:
                return None
        except requests.RequestException as e:
            print(f"  error {e} {url}")
        time.sleep(2 * (i + 1))
    return None


def sitemap_urls(site):
    """Return {'posts': [...], 'pages': [...]} from the Wix sitemap index."""
    found = {"posts": [], "pages": []}
    idx = get(f"{site}/sitemap.xml")
    if not idx:
        sys.exit("Could not fetch sitemap.xml")
    child_maps = re.findall(r"<loc>(.*?)</loc>", idx.text)
    for sm in child_maps:
        if not sm.endswith(".xml"):
            continue
        r = get(sm)
        if not r:
            continue
        locs = re.findall(r"<loc>(.*?)</loc>", r.text)
        kind = "posts" if "blog-posts" in sm else "pages"
        if "blog-categories" in sm:
            kind = "pages"
        for loc in locs:
            if loc.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif")):
                continue  # image:loc entries
            found[kind].append(loc)
    for k in found:
        found[k] = sorted(set(found[k]))
    return found


def slug_for(url):
    path = urlparse(url).path.strip("/")
    if not path:
        return "home"
    return path.split("/")[-1] if path.startswith("post/") else path.replace("/", "__")


def json_ld(soup):
    data = {}
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            obj = json.loads(tag.string or "")
        except json.JSONDecodeError:
            continue
        items = obj if isinstance(obj, list) else [obj]
        for it in items:
            if isinstance(it, dict) and it.get("@type") in ("BlogPosting", "Article", "NewsArticle"):
                data.update(it)
    return data


def meta(soup, name):
    tag = soup.find("meta", attrs={"property": name}) or soup.find("meta", attrs={"name": name})
    return tag.get("content", "").strip() if tag else ""


downloaded = {}


def download_image(media_id):
    """Download original-resolution Wix image, return local URL."""
    if media_id in downloaded:
        return downloaded[media_id]
    local_name = media_id.replace("~", "-")
    dest = IMG_DIR / local_name
    if not dest.exists():
        r = get(f"https://static.wixstatic.com/media/{media_id}")
        if not r:
            downloaded[media_id] = None
            return None
        dest.write_bytes(r.content)
    downloaded[media_id] = IMG_URL_PREFIX + local_name
    return downloaded[media_id]


def localise_images(text):
    """Replace any Wix media URL (with or without /v1/... transforms) by a local path."""
    def repl(m):
        full = m.group(0)
        media_id = m.group(1)
        local = download_image(media_id)
        return local or full

    # swallow trailing transform segments like /v1/fill/w_740,h_.../name.png
    pattern = re.compile(WIX_MEDIA.pattern + r"(?:/v1/[^\s\)\"']*)?")
    return pattern.sub(repl, text)


def article_html(soup):
    """Best guess at the post body container in Wix's rendered HTML."""
    for sel in ['[data-hook="post-description"]', '[data-id="content-viewer"]',
                '[data-hook="rcv-block-first"]', "article", "main"]:
        node = soup.select_one(sel)
        if node and len(node.get_text(strip=True)) > 200:
            return str(node)
    return str(soup)


def yaml_str(s):
    return json.dumps(s or "", ensure_ascii=False)


def scrape(url, kind, writer):
    slug = slug_for(url)
    print(f"[{kind}] {slug}")
    r = get(url)
    if not r:
        writer.writerow([kind, url, slug, "FAILED", "", "", "", ""])
        return
    html = r.text
    raw_dir = OUT / "raw" / kind
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / f"{slug}.html").write_text(html, encoding="utf-8")

    soup = BeautifulSoup(html, "html.parser")
    ld = json_ld(soup)
    title = ld.get("headline") or meta(soup, "og:title") or (soup.title.string if soup.title else slug)
    title = re.sub(r"\s*\|\s*MES Matters.*$", "", title or "").strip()
    description = meta(soup, "description") or meta(soup, "og:description")
    published = ld.get("datePublished", "")
    modified = ld.get("dateModified", "")
    author = ld.get("author", {})
    if isinstance(author, list):
        author = author[0] if author else {}
    author = author.get("name", "") if isinstance(author, dict) else str(author)
    hero = meta(soup, "og:image")
    categories = sorted({a.get_text(strip=True) for a in soup.select('a[href*="/categories/"]') if a.get_text(strip=True)})

    body_md = trafilatura.extract(
        article_html(soup) if kind == "posts" else html,
        output_format="markdown",
        include_images=True,
        include_links=True,
        include_tables=True,
        include_formatting=True,
        favor_recall=True,
    ) or ""

    body_md = localise_images(body_md)
    hero_local = localise_images(hero) if hero else ""
    # also grab every image in the page body even if the extractor dropped it
    all_ids = sorted(set(WIX_MEDIA.findall(article_html(soup))))
    for mid in all_ids:
        download_image(mid)

    words = len(re.findall(r"\w+", body_md))
    fm = [
        "---",
        f"title: {yaml_str(title)}",
        f"slug: {yaml_str(slug)}",
        f"legacyUrl: {yaml_str(url)}",
        f"description: {yaml_str(description)}",
        f"published: {yaml_str(published)}",
        f"updated: {yaml_str(modified)}",
        f"author: {yaml_str(author)}",
        f"categories: {json.dumps(categories, ensure_ascii=False)}",
        f"heroImage: {yaml_str(hero_local)}",
        f"wordCount: {words}",
        "---",
        "",
    ]
    out_dir = OUT / kind
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{slug}.md").write_text("\n".join(fm) + body_md.strip() + "\n", encoding="utf-8")
    writer.writerow([kind, url, slug, title, published, words, len(all_ids), description])
    time.sleep(1)  # be polite


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="https://www.mesmatters.com")
    args = ap.parse_args()
    site = args.site.rstrip("/")

    OUT.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    urls = sitemap_urls(site)
    print(f"Found {len(urls['posts'])} posts, {len(urls['pages'])} pages")

    with open(OUT / "inventory.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["kind", "url", "slug", "title", "published", "words", "images", "meta_description"])
        for kind in ("posts", "pages"):
            for u in urls[kind]:
                scrape(u, kind, w)

    ok = sum(1 for v in downloaded.values() if v)
    print(f"Done. {ok} images downloaded, {len(downloaded) - ok} failed.")


if __name__ == "__main__":
    main()
