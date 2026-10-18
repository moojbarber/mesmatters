#!/usr/bin/env python3
"""Turn the weekly post sources (marketing/social/wN.py) into the publishing queue.

For every post it writes social/queue/<date>-<id>.yaml with the copy and media
for LinkedIn, X and Instagram, and prepares Instagram media (JPEG slides, and an
MP4 reel for carousels that run as reels). New posts are written unapproved;
existing queue files keep their approval and any edits.

Usage: python scripts/social/export.py w1 w2 w3 w4 [--force]
"""
import datetime as dt
import glob
import importlib.util
import os
import sys

import yaml
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(ROOT, "marketing", "social")
QUEUE = os.path.join(ROOT, "social", "queue")
sys.path.insert(0, os.path.dirname(__file__))
from reel import make_reel  # noqa: E402

YEAR_START = dt.date(2026, 10, 1)
TIMES = {"linkedin": "08:15", "x": "08:30", "x_extra": "12:30", "instagram": "18:30"}
# Instagram format per weekday, from the growth research: reels reach far more
# non-followers for small accounts, carousels convert. Tuesday stays a carousel.
IG_KIND = {"Mon": "reel", "Tue": "carousel", "Thu": "image", "Fri": "reel"}


def load(path, name="WEEK"):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, name)


def parse_day(label):
    d = dt.datetime.strptime(label + f" {YEAR_START.year}", "%a %d %b %Y").date()
    if d < YEAR_START:
        d = d.replace(year=d.year + 1)
    return d


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def media_dir(week, pid):
    hits = glob.glob(os.path.join(SRC, "weeks-*", pid))
    return hits[0] if hits else None


def ig_media(pid, kind):
    d = media_dir(None, pid)
    if not d:
        return None, []
    pngs = sorted(glob.glob(os.path.join(d, f"{pid}-[0-9][0-9].png")))
    jpgs = []
    for p in pngs:
        j = p[:-4] + ".jpg"
        if not os.path.exists(j):
            Image.open(p).convert("RGB").save(j, quality=92)
        jpgs.append(rel(j))
    if kind == "reel" and len(pngs) > 1:
        mp4 = os.path.join(d, f"{pid}-reel.mp4")
        tall = sorted(glob.glob(os.path.join(d, "reel", f"{pid}-[0-9][0-9].png")))
        if not os.path.exists(mp4):
            make_reel(tall or pngs, mp4)
        return "reel", [rel(mp4)]
    if len(jpgs) > 1:
        return "carousel", jpgs
    if jpgs:
        return "image", jpgs
    return None, []


def write(path, data, force):
    if os.path.exists(path) and not force:
        old = yaml.safe_load(open(path)) or {}
        data["approved"] = old.get("approved", False)
    with open(path, "w") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=1000)


def export_week(name, force=False):
    W = load(os.path.join(SRC, f"{name}.py"))
    out = []
    for p in W["posts"]:
        day = p["day"].split()[0]
        date = parse_day(p["day"])
        needs_text = "[Your story" in p["li"]
        item = {"id": p["id"], "week": W["n"], "date": date.isoformat(), "type": p["type"], "title": p["title"],
                "approved": False, "article": W["url"]}
        item["linkedin"] = {"at": TIMES["linkedin"], "text": p["li"], "needs_text": needs_text}
        if p.get("li_comment"):
            item["linkedin"]["comment"] = p["li_comment"]
        if p.get("li_poll"):
            q = [l for l in p["li"].strip().split("\n") if l.strip()][-1]
            item["linkedin"]["poll"] = {"question": q[:140], "options": p["li_poll"][:4]}
        d = media_dir(W["n"], p["id"])
        pdf = d and os.path.join(d, f"{p['id']}-linkedin.pdf")
        if pdf and os.path.exists(pdf) and not p.get("li_poll"):
            item["linkedin"]["document"] = rel(pdf)
            item["linkedin"]["document_title"] = p["title"]
        x = {"at": TIMES["x"], "posts": p["x"], "needs_text": needs_text or "[Short version" in p["x"][0]}
        if p.get("x_poll"):
            x["poll"] = p["x_poll"]
        item["x"] = x
        kind, media = ig_media(p["id"], IG_KIND.get(day, "carousel"))
        if p.get("reel"):
            item["instagram"] = {"at": TIMES["instagram"], "kind": "manual_reel", "caption": p["ig"],
                                 "script": p["reel"], "needs_text": True}
        elif kind:
            item["instagram"] = {"at": TIMES["instagram"], "kind": kind, "caption": p["ig"], "media": media}
        path = os.path.join(QUEUE, f"{date.isoformat()}-{p['id']}.yaml")
        write(path, item, force)
        out.append(path)
    return out


def export_extras(force=False):
    ex = load(os.path.join(SRC, "extras_w1_4.py"), "X_EXTRAS")
    out = []
    for week, items in ex.items():
        for i, (label, text) in enumerate(items, 1):
            date = parse_day(label)
            pid = f"w{week}-x{i}"
            item = {"id": pid, "week": week, "date": date.isoformat(), "type": "X only", "title": text.split("\n")[0][:60],
                    "approved": False, "x": {"at": TIMES["x_extra"], "posts": [text]}}
            path = os.path.join(QUEUE, f"{date.isoformat()}-{pid}.yaml")
            write(path, item, force)
            out.append(path)
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    os.makedirs(QUEUE, exist_ok=True)
    n = 0
    for w in args:
        n += len(export_week(w, force))
    if os.path.exists(os.path.join(SRC, "extras_w1_4.py")) and {"w1", "w2", "w3", "w4"} & set(args):
        n += len(export_extras(force))
    print(f"{n} queue files written to {rel(QUEUE)}")
