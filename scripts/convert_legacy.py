#!/usr/bin/env python3
"""Re-convert scraped Wix post HTML (content/legacy/raw/posts) into clean Markdown.

Keeps the front matter from scrape_wix.py, but rebuilds the body from Wix's
post container, fixes categories (taken from the post footer, not the nav)
and unescapes titles. Safe to re-run.
"""
import html as htmllib
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "content" / "legacy" / "raw" / "posts"
POSTS = ROOT / "content" / "legacy" / "posts"
IMG_PREFIX = "/images/legacy/"
WIX_IMG = re.compile(r"https://static\.wixstatic\.com/media/([A-Za-z0-9_]+~mv2[^/\"'\s?)]*)(?:/v1/[^\s\"')]*)?")


def clean_body(node):
    # drop Wix's empty marker divs and any scripts/styles
    for t in node.select('div[data-hook^="rcv-block"], script, style, noscript, button, svg'):
        t.decompose()
    # images: point at the original file
    for img in node.find_all("img"):
        src = img.get("src") or img.get("data-src") or ""
        m = WIX_IMG.search(src)
        if m:
            img["src"] = IMG_PREFIX + m.group(1).replace("~", "-")
        for a in list(img.attrs):
            if a not in ("src", "alt"):
                del img[a]
    # strip presentational attributes so markdownify output is clean
    for t in node.find_all(True):
        for a in list(t.attrs):
            if a not in ("href", "src", "alt", "colspan", "rowspan"):
                del t[a]
    # unwrap blockquote's inner divs to keep quote text inline
    return node


def to_markdown(node):
    md = markdownify(str(node), heading_style="ATX", bullets="-", strip=["span", "div"])
    md = md.replace(" ", " ")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"\*\*\s*\*\*", "", md)          # empty bold
    md = re.sub(r"^(#+)\s*\*\*(.+?)\*\*\s*$", r"\1 \2", md, flags=re.M)  # bold inside headings
    md = re.sub(r"^#+\s*$", "", md, flags=re.M)   # empty headings
    return md.strip() + "\n"


def split_front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (m.group(1), text[m.end():]) if m else ("", text)


def set_fm(fm, key, value):
    line = f"{key}: {json.dumps(value, ensure_ascii=False)}"
    if re.search(rf"^{key}:", fm, re.M):
        return re.sub(rf"^{key}:.*$", lambda _: line, fm, flags=re.M)
    return fm + "\n" + line


def main():
    for raw in sorted(RAW.glob("*.html")):
        slug = raw.stem
        md_path = POSTS / f"{slug}.md"
        soup = BeautifulSoup(raw.read_text(encoding="utf-8"), "html.parser")
        node = soup.select_one('[data-hook="post-description"]')
        if not node:
            print(f"!! no body container: {slug}")
            continue

        cats = sorted({a.get_text(strip=True) for a in soup.select('[data-hook="post-footer"] a[href*="/categories/"]')})
        tags = sorted({a.get_text(strip=True) for a in soup.select('[data-hook="post-footer"] a[href*="/tags/"]')})
        body = to_markdown(clean_body(node))

        fm, _ = split_front_matter(md_path.read_text(encoding="utf-8")) if md_path.exists() else ("", "")
        title_m = re.search(r'^title: (".*")$', fm, re.M)
        if title_m:
            fm = set_fm(fm, "title", htmllib.unescape(json.loads(title_m.group(1))))
        fm = set_fm(fm, "categories", cats)
        if tags:
            fm = set_fm(fm, "tags", tags)
        fm = set_fm(fm, "wordCount", len(re.findall(r"[A-Za-z0-9']+", body)))
        md_path.write_text(f"---\n{fm}\n---\n\n{body}", encoding="utf-8")
        print(f"{slug}: {len(body.split())} words, {cats}")


if __name__ == "__main__":
    main()
