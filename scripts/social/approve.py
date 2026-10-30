#!/usr/bin/env python3
"""Approve (or unapprove) queued social posts.

  python scripts/social/approve.py w1            # every post in week 1
  python scripts/social/approve.py w1-tue w2-x1  # specific posts
  python scripts/social/approve.py --undo w2     # take approval back
  python scripts/social/approve.py --list        # show what's queued

Posts that still need your own words stay blocked on that platform even when
approved: fill in the text in the queue file and set needs_text: false.
"""
import glob
import os
import re
import sys

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
QUEUE = os.path.join(ROOT, "social", "queue")


def items():
    for f in sorted(glob.glob(os.path.join(QUEUE, "*.yaml"))):
        yield f, yaml.safe_load(open(f))


def matches(item, sel):
    return item["id"] == sel or (re.fullmatch(r"w\d+", sel) and f"w{item['week']}" == sel)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--list" in sys.argv or not args:
        for f, d in items():
            blocked = [p for p in ("linkedin", "x", "instagram") if d.get(p, {}).get("needs_text") or d.get(p, {}).get("manual") or d.get(p, {}).get("kind") == "manual_reel"]
            print(f"{d['date']}  {d['id']:<8} {'APPROVED' if d.get('approved') else 'waiting ':<8}  {d['title'][:50]}"
                  + (f"  (you post yourself: {', '.join(blocked)})" if blocked else ""))
        return
    value = "--undo" not in sys.argv
    n = 0
    for f, d in items():
        if any(matches(d, s) for s in args):
            text = open(f).read()
            new = re.sub(r"^approved: (true|false)$", f"approved: {str(value).lower()}", text, count=1, flags=re.M)
            open(f, "w").write(new)
            n += 1
    print(f"{'Approved' if value else 'Unapproved'} {n} posts")


if __name__ == "__main__":
    main()
