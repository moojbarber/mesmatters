#!/usr/bin/env python3
"""Generate on-brand hero artwork for every article.

Writes public/images/art/<slug>.svg (1600x900). Each piece shares the house
background (navy, three glowing blobs, fading dot grid, a gradient "production
line" thread) with a topic-specific motif drawn in violet->cyan line work.
Deterministic: the same slug always gives the same picture.

Usage: python scripts/art.py            (all posts in content/seo.yaml)
       python scripts/art.py <motif> <slug>
"""
import math
import random
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "images" / "art"
W, H = 1600, 900
CX, CY = 800, 440

CYAN, VIOLET, PINK = "#33d4e0", "#8b6cff", "#ff6fd8"


def f(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


# ---------------------------------------------------------------- primitives
class Art:
    def __init__(self, seed):
        self.r = random.Random(seed)
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def line(self, x1, y1, x2, y2, w=2, stroke="url(#g)", op=1, dash=None, cls=""):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{stroke}" stroke-width="{w}" opacity="{op}" stroke-linecap="round"{d}/>')

    def path(self, d, w=2.5, stroke="url(#g)", fill="none", op=1, dash=None, glow=False):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        fl = ' filter="url(#glow)"' if glow else ""
        self.add(f'<path d="{d}" stroke="{stroke}" stroke-width="{w}" fill="{fill}" opacity="{op}" stroke-linecap="round" stroke-linejoin="round"{da}{fl}/>')

    def rect(self, x, y, w, h, rx=14, fill="url(#glass)", stroke="url(#g)", sw=1.5, op=1, glow=False):
        fl = ' filter="url(#glow)"' if glow else ""
        self.add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"{fl}/>')

    def circle(self, x, y, r, fill="none", stroke="url(#g)", sw=2, op=1, glow=False):
        fl = ' filter="url(#glow)"' if glow else ""
        self.add(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"{fl}/>')

    def node(self, x, y, r=7, color=CYAN):
        self.circle(x, y, r * 2.6, fill=color, stroke="none", op=.18)
        self.circle(x, y, r, fill="#0a0820", stroke=color, sw=2.5, glow=True)

    def dot(self, x, y, r=4, color=CYAN, op=1):
        self.circle(x, y, r, fill=color, stroke="none", op=op)

    def hexagon(self, x, y, r, **kw):
        pts = " ".join(f"{f(x + r * math.cos(math.radians(60 * i - 30)))},{f(y + r * math.sin(math.radians(60 * i - 30)))}" for i in range(6))
        fill = kw.get("fill", "url(#glass)")
        stroke = kw.get("stroke", "url(#g)")
        sw = kw.get("sw", 2)
        op = kw.get("op", 1)
        fl = ' filter="url(#glow)"' if kw.get("glow") else ""
        self.add(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"{fl}/>')

    def person(self, x, y, s=1, color=CYAN, op=1):
        self.circle(x, y - 14 * s, 9 * s, fill="#0a0820", stroke=color, sw=2.2, op=op)
        self.path(f"M{f(x - 16 * s)},{f(y + 16 * s)} Q{f(x)},{f(y - 8 * s)} {f(x + 16 * s)},{f(y + 16 * s)}", w=2.2, stroke=color, op=op)


def smooth(points):
    """Catmull-Rom -> cubic Bezier path through points."""
    d = f"M{f(points[0][0])},{f(points[0][1])}"
    for i in range(len(points) - 1):
        p0 = points[i - 1] if i else points[i]
        p1, p2 = points[i], points[i + 1]
        p3 = points[i + 2] if i + 2 < len(points) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{f(c1[0])},{f(c1[1])} {f(c2[0])},{f(c2[1])} {f(p2[0])},{f(p2[1])}"
    return d


def arc(cx, cy, r, a0, a1):
    a0r, a1r = math.radians(a0), math.radians(a1)
    x0, y0 = cx + r * math.cos(a0r), cy + r * math.sin(a0r)
    x1, y1 = cx + r * math.cos(a1r), cy + r * math.sin(a1r)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{f(x0)},{f(y0)} A{f(r)},{f(r)} 0 {large} 1 {f(x1)},{f(y1)}"


# ---------------------------------------------------------------- motifs
def m_hexcore(a):
    R = 118
    ring = [(CX + 2 * R * 0.95 * math.cos(math.radians(60 * i)), CY + 2 * R * 0.95 * math.sin(math.radians(60 * i))) for i in range(6)]
    for i, (x, y) in enumerate(ring):
        a.line(CX, CY, x, y, w=1.5, op=.5, dash="4 8")
    outer = [(CX + 3.7 * R * math.cos(math.radians(60 * i + 30)), CY + 3.0 * R * math.sin(math.radians(60 * i + 30))) for i in range(6)]
    for (x, y), (ox, oy) in zip(ring, outer):
        a.line(x, y, ox, oy, w=1.2, op=.3)
        a.dot(ox, oy, 4, op=.7)
    for i, (x, y) in enumerate(ring):
        hot = i == 4
        a.hexagon(x, y, R * .78, fill="url(#hot)" if hot else "url(#glass)", stroke=PINK if i == 1 else "url(#g)", glow=hot)
    a.hexagon(CX, CY, R * 1.05, fill="url(#hot)", sw=3, glow=True)
    a.hexagon(CX, CY, R * .55, fill="none", stroke=CYAN, sw=1.5, op=.7)
    a.node(CX, CY, 9)


def m_hexgrid(a):
    r = 46
    dx, dy = r * math.sqrt(3), r * 1.5
    for row in range(-4, 5):
        for col in range(-7, 8):
            x = CX + col * dx + (dx / 2 if row % 2 else 0)
            y = CY + row * dy
            dist = math.hypot((x - CX) / 1.4, y - CY)
            if dist > 470:
                continue
            fade = max(.12, 1 - dist / 480)
            lit = a.r.random() < .16 and dist < 330
            a.hexagon(x, y, r * .9, fill="url(#hot)" if lit else "url(#glass)", sw=1.4, op=fade, glow=lit)
    a.hexagon(CX, CY, r * .9, fill="url(#hot)", sw=3, glow=True)
    a.node(CX, CY, 7)


def m_stack(a):
    labels = 5
    w, h, skew = 620, 74, 120
    top = CY - 250
    for i in range(labels):
        y = top + i * 108
        hot = i == 2
        x = CX - w / 2
        d = f"M{f(x + skew)},{f(y)} L{f(x + w + skew)},{f(y)} L{f(x + w)},{f(y + h)} L{f(x)},{f(y + h)} Z"
        a.path(d, w=3 if hot else 1.8, fill="url(#hot)" if hot else "url(#glass)", glow=hot)
        # level ticks
        for k in range(4 + i):
            tx = x + 60 + k * (w - 80) / (4 + i)
            a.line(tx + skew * .5, y + h / 2 - 6, tx + skew * .5 + 30, y + h / 2 - 6, w=2, stroke=CYAN if hot else VIOLET, op=.8 if hot else .35)
        a.dot(x + skew * .5 + 26, y + h / 2 + 12, 5, CYAN if hot else VIOLET, op=1 if hot else .6)
    # up/down data arrows
    ax = CX + w / 2 + skew + 70
    a.path(f"M{ax},{top + 20} L{ax},{top + 4 * 108 + h - 20}", w=2.5, dash="2 10")
    a.path(f"M{ax - 12},{top + 36} L{ax},{top + 20} L{ax + 12},{top + 36}", w=2.5, stroke=CYAN)
    ax2 = ax + 40
    a.path(f"M{ax2},{top + 20} L{ax2},{top + 4 * 108 + h - 20}", w=2.5, dash="2 10", stroke=VIOLET, op=.7)
    a.path(f"M{ax2 - 12},{top + 4 * 108 + h - 36} L{ax2},{top + 4 * 108 + h - 20} L{ax2 + 12},{top + 4 * 108 + h - 36}", w=2.5, stroke=VIOLET)


def m_wheel(a):
    n, r1, r2 = 11, 170, 290
    for i in range(n):
        a0 = -90 + i * 360 / n + 2.2
        a1 = -90 + (i + 1) * 360 / n - 2.2
        hot = i in (0, 4, 7)
        p0 = arc(CX, CY, r2, a0, a1)
        x2, y2 = CX + r1 * math.cos(math.radians(a1)), CY + r1 * math.sin(math.radians(a1))
        inner = f"L{f(x2)},{f(y2)} A{r1},{r1} 0 0 0 {f(CX + r1 * math.cos(math.radians(a0)))},{f(CY + r1 * math.sin(math.radians(a0)))} Z"
        a.path(p0 + " " + inner, w=3 if hot else 1.6, fill="url(#hot)" if hot else "url(#glass)", glow=hot, stroke=PINK if i == 9 else "url(#g)")
        mid = math.radians((a0 + a1) / 2)
        a.dot(CX + (r2 + 34) * math.cos(mid), CY + (r2 + 34) * math.sin(mid), 4, op=.7)
    a.circle(CX, CY, 120, fill="url(#hot)", sw=3, glow=True)
    a.circle(CX, CY, 78, stroke=CYAN, sw=1.5, op=.6)
    a.node(CX, CY, 9)


def m_rings(a):
    vals = [(.86, 270), (.71, 215), (.93, 160)]
    for (v, r) in vals:
        a.circle(CX, CY, r, stroke="rgba(255,255,255,.08)", sw=26)
        a.path(arc(CX, CY, r, -90, -90 + 360 * v), w=26, glow=True)
        end = math.radians(-90 + 360 * v)
        a.dot(CX + r * math.cos(end), CY + r * math.sin(end), 6, "#fff")
    a.circle(CX, CY, 100, fill="url(#hot)", stroke="none")
    a.node(CX, CY, 10)
    # A x P x Q tick marks
    for i, x in enumerate((CX - 520, CX + 470)):
        for k in range(5):
            a.line(x, CY - 120 + k * 60, x + 50, CY - 120 + k * 60, w=2, op=.25 + .12 * k, stroke=VIOLET if i else CYAN)


def m_timeline(a):
    y0 = CY + 130
    xs = [CX - 600 + i * 240 for i in range(6)]
    a.path(f"M{CX - 700},{y0} L{CX + 700},{y0}", w=3, glow=True)
    for i, x in enumerate(xs):
        h = 70 + i * 52
        op = .35 + i * .13
        a.line(x, y0, x, y0 - h, w=2, op=op)
        bw = 120 + i * 8
        a.rect(x - bw / 2, y0 - h - 70, bw, 64, rx=12, fill="url(#hot)" if i == 5 else "url(#glass)", op=min(1, op + .2), glow=i == 5)
        for k in range(2):
            a.line(x - bw / 2 + 18, y0 - h - 50 + k * 22, x - bw / 2 + 18 + (bw - 36) * (.9 - .3 * k), y0 - h - 50 + k * 22, w=3, stroke=CYAN if i == 5 else VIOLET, op=.6)
        a.node(x, y0, 8 if i == 5 else 6, PINK if i == 0 else CYAN)


def m_signal(a):
    rows = [CY - 170, CY, CY + 170]
    for ri, y in enumerate(rows):
        pts = []
        for i in range(17):
            x = CX - 640 + i * 80
            amp = 50 if ri != 1 else 70
            v = y - a.r.uniform(-amp, amp) * (0.6 + .4 * math.sin(i / 2))
            if ri == 1 and 8 <= i <= 10:
                v = y + 70  # downtime dip
            pts.append((x, v))
        a.line(CX - 660, y + 80, CX + 660, y + 80, w=1, stroke="rgba(255,255,255,.12)")
        a.path(smooth(pts), w=3 if ri == 1 else 2, op=1 if ri == 1 else .55, glow=ri == 1)
        if ri == 1:
            a.rect(CX - 0 + 0, y + 40, 160, 50, rx=10, fill="rgba(255,111,216,.12)", stroke=PINK, sw=1.5)
            for x, v in pts[::4]:
                a.node(x, v, 6)


def m_gantt(a):
    rows = 6
    x0, x1 = CX - 620, CX + 620
    for i in range(rows):
        y = CY - 250 + i * 92
        a.line(x0, y + 66, x1, y + 66, w=1, stroke="rgba(255,255,255,.08)")
        x = x0 + a.r.uniform(0, 80)
        while x < x1 - 120:
            wbar = a.r.uniform(120, 300)
            wbar = min(wbar, x1 - x)
            hot = (i == 2 and x < CX < x + wbar)
            pink = (i == 4 and a.r.random() < .5)
            a.rect(x, y + 10, wbar - 18, 46, rx=12,
                   fill="url(#hot)" if hot else ("rgba(255,111,216,.12)" if pink else "url(#glass)"),
                   stroke=PINK if pink else "url(#g)", sw=2.5 if hot else 1.4, glow=hot)
            x += wbar + a.r.uniform(10, 60)
    a.path(f"M{CX + 40},{CY - 280} L{CX + 40},{CY + 300}", w=2.5, stroke=CYAN, dash="6 8", glow=True)
    a.node(CX + 40, CY - 290, 7)


def m_spc(a):
    x0, x1 = CX - 620, CX + 620
    ucl, cl, lcl = CY - 170, CY, CY + 170
    a.line(x0, cl, x1, cl, w=2, stroke=CYAN, op=.6)
    a.line(x0, ucl, x1, ucl, w=2, stroke=VIOLET, dash="10 10", op=.8)
    a.line(x0, lcl, x1, lcl, w=2, stroke=VIOLET, dash="10 10", op=.8)
    a.rect(x0, ucl, x1 - x0, lcl - ucl, rx=0, fill="rgba(51,212,224,.04)", stroke="none")
    pts = []
    for i in range(20):
        x = x0 + 30 + i * 62
        y = cl + a.r.gauss(0, 60)
        y = max(ucl + 20, min(lcl - 20, y))
        if i == 14:
            y = ucl - 70
        pts.append((x, y))
    a.path("M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts), w=2.5, glow=True)
    for i, (x, y) in enumerate(pts):
        if i == 14:
            a.circle(x, y, 26, stroke=PINK, sw=2, op=.6)
            a.circle(x, y, 9, fill=PINK, stroke="none", glow=True)
        else:
            a.circle(x, y, 6, fill="#0a0820", stroke=CYAN, sw=2.2)


def m_bins(a):
    # isometric rack of boxes
    s = 80
    iso = lambda gx, gy, gz: (CX + (gx - gy) * s * .87, CY + 20 + (gx + gy) * s * .5 - gz * s * .9)
    cells = []
    for gz in range(3):
        for gy in range(4):
            for gx in range(5):
                cells.append((gx, gy, gz))
    cells.sort(key=lambda c: (c[2], c[0] + c[1]))
    for gx, gy, gz in cells:
        if a.r.random() < .28:
            continue
        top = [iso(gx, gy, gz + 1), iso(gx + 1, gy, gz + 1), iso(gx + 1, gy + 1, gz + 1), iso(gx, gy + 1, gz + 1)]
        left = [iso(gx, gy + 1, gz + 1), iso(gx + 1, gy + 1, gz + 1), iso(gx + 1, gy + 1, gz), iso(gx, gy + 1, gz)]
        right = [iso(gx + 1, gy, gz + 1), iso(gx + 1, gy + 1, gz + 1), iso(gx + 1, gy + 1, gz), iso(gx + 1, gy, gz)]
        hot = (gx, gy, gz) in ((2, 1, 2), (4, 0, 1))
        pink = (gx, gy, gz) == (0, 3, 0)
        for face, fill in ((left, "rgba(139,108,255,.16)"), (right, "rgba(51,212,224,.10)"), (top, "url(#hot)" if hot else "rgba(255,255,255,.06)")):
            d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in face) + " Z"
            a.path(d, w=2.4 if hot else 1.2, fill=fill, stroke=PINK if pink else "url(#g)", glow=hot)


def m_flow(a, simple=False):
    left = [(CX - 560, CY - 160 + i * 110) for i in range(4)] if not simple else [(CX - 520, CY - 110 + i * 110) for i in range(3)]
    mid = (CX - 60, CY - 40)
    right = [(CX + 440, CY - 200 + i * 140) for i in range(4)] if not simple else [(CX + 440, CY - 110 + i * 110) for i in range(3)]
    for (x, y) in left:
        a.rect(x - 70, y - 34, 140, 68, rx=12)
        for k in range(3):
            a.rect(x - 52 + k * 36, y - 14, 26, 28, rx=5, fill="rgba(51,212,224,.12)", stroke=CYAN, sw=1, op=.7)
    if not simple:
        a.rect(mid[0] - 130, mid[1] - 110, 260, 220, rx=18, fill="url(#hot)", sw=3, glow=True)
        for r in range(3):
            for c in range(4):
                a.rect(mid[0] - 104 + c * 54, mid[1] - 82 + r * 56, 42, 42, rx=7, fill="rgba(51,212,224,.16)", stroke=CYAN, sw=1.2)
    for (x, y) in right:
        a.rect(x - 110, y - 34, 220, 68, rx=12)
        for k in range(3):
            a.circle(x - 66 + k * 66, y, 14, stroke=VIOLET, sw=2)
            if k < 2:
                a.line(x - 50 + k * 66, y, x - 18 + k * 66, y, w=2, stroke=CYAN)
    hub = mid if not simple else (CX - 40, CY)
    if simple:
        a.circle(hub[0], hub[1], 70, fill="url(#hot)", sw=3, glow=True)
        a.node(hub[0], hub[1], 9)
    for (x, y) in left:
        d = smooth([(x + 70, y), ((x + hub[0]) / 2, y), ((x + hub[0]) / 2 + 40, hub[1]), (hub[0] - (130 if not simple else 70), hub[1])])
        a.path(d, w=2, op=.8, dash="1 0")
        a.dot((x + hub[0]) / 2 + 10, (y + hub[1]) / 2, 5, CYAN)
    for i, (x, y) in enumerate(right):
        d = smooth([(hub[0] + (130 if not simple else 70), hub[1]), ((x + hub[0]) / 2, hub[1]), ((x + hub[0]) / 2 + 40, y), (x - 110, y)])
        a.path(d, w=2, op=.8, stroke=PINK if i == len(right) - 1 else "url(#g)")
        a.dot((x + hub[0]) / 2 + 30, (y + hub[1]) / 2, 5, CYAN)


def m_steps(a):
    n = 6
    bw = 150
    for i in range(n):
        h = 80 + i * 70
        x = CX - n * bw / 2 + i * bw + 10
        hot = i == n - 1
        a.rect(x, CY + 250 - h, bw - 24, h, rx=14, fill="url(#hot)" if hot else "url(#glass)", sw=2.5 if hot else 1.4, glow=hot, op=.45 + i * .11)
        a.node(x + (bw - 24) / 2, CY + 250 - h - 30, 7 if hot else 5, CYAN)
    pts = [(CX - n * bw / 2 + i * bw + 10 + (bw - 24) / 2, CY + 250 - (80 + i * 70) - 30) for i in range(n)]
    a.path(smooth(pts), w=2.5, dash="3 9")
    ex, ey = pts[-1]
    a.path(f"M{ex + 30},{ey - 60} L{ex + 90},{ey - 120}", w=3, stroke=CYAN, glow=True)
    a.path(f"M{ex + 62},{ey - 120} L{ex + 90},{ey - 120} L{ex + 90},{ey - 92}", w=3, stroke=CYAN)
    # a cycle loop for PDCA
    a.path(arc(CX - 420, CY - 170, 70, 200, 520 - 30), w=2.5, op=.8)
    a.path(f"M{f(CX - 420 + 70 * math.cos(math.radians(130)) - 6)},{f(CY - 170 + 70 * math.sin(math.radians(130)) - 14)} l8,14 l14,-6", w=2.5, stroke=CYAN)


def m_orbits(a):
    for k, (rx, ry) in enumerate(((210, 120), (370, 210), (540, 300))):
        a.add(f'<ellipse cx="{CX}" cy="{CY}" rx="{rx}" ry="{ry}" fill="none" stroke="url(#g)" stroke-width="1.6" opacity="{.75 - k * .18}"/>')
        count = 3 + k * 2
        for i in range(count):
            t = math.radians(i * 360 / count + k * 23)
            x, y = CX + rx * math.cos(t), CY + ry * math.sin(t)
            a.circle(x, y, 30, fill="#0a0820", stroke="url(#g)", sw=1.5)
            a.person(x, y + 4, .8, color=PINK if (k == 2 and i == 3) else CYAN)
    a.circle(CX, CY, 82, fill="url(#hot)", sw=3, glow=True)
    a.hexagon(CX, CY, 40, fill="none", stroke=CYAN, sw=2)
    a.node(CX, CY, 7)


def m_growth(a):
    x0, x1, base = CX - 620, CX + 620, CY + 240
    a.line(x0, base, x1, base, w=1.5, stroke="rgba(255,255,255,.15)")
    pts = [(x0 + i * (x1 - x0) / 12, base - 40 - (i ** 1.45) * 14 - a.r.uniform(0, 30)) for i in range(13)]
    area = smooth(pts) + f" L{x1},{base} L{x0},{base} Z"
    a.path(area, w=0, stroke="none", fill="url(#area)")
    a.path(smooth(pts), w=3.5, glow=True)
    for x, y in pts[::3]:
        a.node(x, y, 6)
    cost = [(x0 + i * (x1 - x0) / 12, CY - 220 + i * 22 + a.r.uniform(-10, 10)) for i in range(13)]
    a.path(smooth(cost), w=2, stroke=PINK, dash="8 10", op=.8)
    for i in range(6):
        a.rect(x0 + 40 + i * 200, base + 30, 120, 10, rx=5, fill="rgba(255,255,255,.08)", stroke="none")


def m_bridge(a):
    lx, rx = CX - 470, CX + 470
    a.rect(lx - 180, CY - 230, 360, 460, rx=22)
    for i in range(7):
        a.line(lx - 140, CY - 180 + i * 58, lx - 140 + a.r.uniform(160, 270), CY - 180 + i * 58, w=6, stroke=VIOLET, op=.45)
    a.rect(rx - 180, CY - 230, 360, 460, rx=22, fill="url(#hot)", sw=2.5, glow=True)
    for r in range(4):
        for c in range(3):
            hot = (r, c) == (1, 1)
            a.rect(rx - 140 + c * 98, CY - 190 + r * 98, 82, 82, rx=12, fill="rgba(51,212,224,.2)" if hot else "rgba(255,255,255,.04)", stroke=CYAN if hot else "url(#g)", sw=1.4, glow=hot)
    for i in range(5):
        y = CY - 160 + i * 80
        d = smooth([(lx + 180, y), (CX - 120, y), (CX + 120, y + (i - 2) * 18), (rx - 180, y + (i - 2) * 18)])
        a.path(d, w=2, op=.85)
        a.dot(CX + a.r.uniform(-140, 140), y + (i - 2) * 9, 5, CYAN)
    a.node(CX, CY, 8)


def m_network(a):
    nodes = [(CX, CY)]
    for ring, cnt, rx, ry in ((1, 6, 260, 170), (2, 9, 520, 300)):
        off = a.r.uniform(0, 40)
        for i in range(cnt):
            t = math.radians(off + i * 360 / cnt)
            nodes.append((CX + rx * math.cos(t) + a.r.uniform(-30, 30), CY + ry * math.sin(t) + a.r.uniform(-20, 20)))
    edges = set()
    for i in range(1, 7):
        edges.add((0, i))
    for i in range(7, len(nodes)):
        near = sorted(range(1, 7), key=lambda j: math.dist(nodes[i], nodes[j]))[:2]
        for j in near:
            edges.add((j, i))
    for i in range(1, 7):
        edges.add((i, 1 + i % 6))
    for i, j in edges:
        a.line(*nodes[i], *nodes[j], w=1.6, op=.55)
    for k, (x, y) in enumerate(nodes):
        if k == 0:
            a.circle(x, y, 64, fill="url(#hot)", sw=3, glow=True)
            a.person(x, y + 6, 1.4)
        elif k <= 6:
            a.circle(x, y, 40, fill="#0a0820", stroke="url(#g)", sw=2)
            a.person(x, y + 4, 1.0)
        else:
            a.circle(x, y, 26, fill="#0a0820", stroke=PINK if k == 11 else "url(#g)", sw=1.6, op=.85)
            a.person(x, y + 4, .7, color=PINK if k == 11 else VIOLET)


def m_bars(a):
    n = 10
    bw = 92
    base = CY + 260
    trend = []
    for i in range(n):
        h = 90 + i * 42 + a.r.uniform(-20, 20)
        x = CX - n * bw / 2 + i * bw + 14
        hot = i == n - 1
        a.rect(x, base - h, bw - 28, h, rx=10, fill="url(#hot)" if hot else "url(#barfill)", sw=2.4 if hot else 1.2, glow=hot)
        trend.append((x + (bw - 28) / 2, base - h - 46))
    a.path(smooth(trend), w=3, stroke=CYAN, glow=True)
    for x, y in trend[::3]:
        a.node(x, y, 6)
    a.line(CX - n * bw / 2, base, CX + n * bw / 2, base, w=1.5, stroke="rgba(255,255,255,.2)")


def m_mesh(a):
    cols = [4, 7, 7, 5, 2]
    pos = []
    for ci, cnt in enumerate(cols):
        x = CX - 560 + ci * 280
        col = [(x, CY + (i - (cnt - 1) / 2) * 92) for i in range(cnt)]
        pos.append(col)
    hot_path = [1, 3, 2, 2, 0]
    for ci in range(len(cols) - 1):
        for i, p in enumerate(pos[ci]):
            for j, q in enumerate(pos[ci + 1]):
                hot = hot_path[ci] == i and hot_path[ci + 1] == j
                a.line(*p, *q, w=3.5 if hot else 1.2, op=1 if hot else .26, stroke=CYAN if hot else "url(#g)")
    for ci, col in enumerate(pos):
        for i, (x, y) in enumerate(col):
            if hot_path[ci] == i:
                a.node(x, y, 10)
            else:
                a.circle(x, y, 15, fill="#0a0820", stroke=PINK if (ci == 0 and i == 3) else "url(#g)", sw=2)


def m_tanks(a):
    xs = [CX - 430, CX - 60, CX + 310]
    levels = [.62, .38, .8]
    for i, (x, lv) in enumerate(zip(xs, levels)):
        w, h, top = 220, 400, CY - 220
        hot = i == 1
        a.rect(x - w / 2, top, w, h, rx=50, sw=2.5 if hot else 1.6, glow=hot)
        fy = top + h * (1 - lv)
        a.add(f'<clipPath id="tc{i}"><rect x="{f(x - w / 2)}" y="{f(top)}" width="{w}" height="{h}" rx="50"/></clipPath>')
        a.add(f'<rect x="{f(x - w / 2)}" y="{f(fy)}" width="{w}" height="{f(top + h - fy)}" fill="url(#liquid{"p" if i == 2 else ""})" clip-path="url(#tc{i})"/>')
        a.path(f"M{f(x - w / 2 + 10)},{f(fy)} Q{f(x - 50)},{f(fy - 12)} {f(x)},{f(fy)} T{f(x + w / 2 - 10)},{f(fy)}", w=2.5, stroke=PINK if i == 2 else CYAN, glow=True)
        for k in range(5):
            a.line(x + w / 2 - 34, top + 60 + k * 64, x + w / 2 - 16, top + 60 + k * 64, w=2, stroke="rgba(255,255,255,.3)")
        a.line(x, top + h, x, top + h + 60, w=4, stroke=VIOLET, op=.7)
    y = CY + 240
    a.path(f"M{xs[0]},{y} L{xs[2] + 200},{y}", w=4, glow=True)
    for x in xs[:2]:
        mx = x + 185
        a.circle(mx, y, 18, fill="#0a0820", stroke=CYAN, sw=2.5)
        a.line(mx - 10, y - 10, mx + 10, y + 10, w=2.5, stroke=CYAN)
    a.node(xs[2] + 200, y, 8)


def m_worker(a):
    tiles = []
    for i in range(6):
        t = math.radians(-90 + i * 60 + 30)
        tiles.append((CX + 470 * math.cos(t), CY + 250 * math.sin(t)))
    for i, (x, y) in enumerate(tiles):
        ang = math.atan2(y - CY, x - CX)
        a.line(CX + 152 * math.cos(ang), CY + 152 * math.sin(ang), x, y, w=2 if i != 4 else 1.5, op=.7 if i != 4 else .5, dash=None if i != 4 else "4 8", stroke=PINK if i == 4 else "url(#g)")
        a.dot((CX + x) / 2, (CY + y) / 2, 5, PINK if i == 4 else CYAN)
    for i, (x, y) in enumerate(tiles):
        hot = i in (0, 2)
        a.rect(x - 95, y - 42, 190, 84, rx=16, fill="url(#hot)" if hot else "url(#glass)", stroke=PINK if i == 4 else "url(#g)", sw=2.4 if hot else 1.5, glow=hot)
        a.rect(x - 72, y - 22, 26, 26, rx=7, fill="rgba(51,212,224,.18)" if i != 4 else "rgba(255,111,216,.15)", stroke=CYAN if i != 4 else PINK, sw=1.2)
        a.line(x - 34, y - 14, x + 70, y - 14, w=4, stroke=VIOLET, op=.55)
        a.line(x - 34, y + 2, x + 40, y + 2, w=4, stroke=VIOLET, op=.35)
        a.line(x - 72, y + 22, x + 70, y + 22, w=2, stroke="rgba(255,255,255,.12)")
    a.circle(CX, CY, 118, fill="url(#hot)", sw=3, glow=True)
    a.circle(CX, CY, 150, stroke=CYAN, sw=1.2, op=.35)
    a.person(CX, CY + 28, 3.4)


def m_gates(a):
    y = CY + 60
    a.path(f"M{CX - 700},{y} L{CX + 700},{y}", w=4, glow=True)
    xs = [CX - 450, CX - 150, CX + 150, CX + 450]
    for i, x in enumerate(xs):
        blocked = i == 1
        c = PINK if blocked else "url(#g)"
        a.rect(x - 50, y - 210, 100, 260, rx=18, fill="rgba(255,111,216,.10)" if blocked else ("url(#hot)" if i == 3 else "url(#glass)"), stroke=c, sw=2.4 if blocked or i == 3 else 1.5, glow=blocked or i == 3)
        a.line(x - 50, y - 150, x + 50, y - 150, w=1.2, stroke=PINK if blocked else CYAN, op=.5)
        a.node(x, y - 250, 7, PINK if blocked else CYAN)
        if blocked:
            a.line(x - 30, y - 120, x + 30, y - 60, w=4, stroke=PINK)
            a.line(x + 30, y - 120, x - 30, y - 60, w=4, stroke=PINK)
    # product units moving along the line, queuing before the blocked gate
    for k, x in enumerate([CX - 660, CX - 600, CX - 330, CX - 282, CX - 234]):
        a.rect(x - 18, y - 46, 36, 36, rx=8, fill="rgba(139,108,255,.25)", stroke=VIOLET, sw=1.5)
    for x in (CX + 10, CX + 300, CX + 600):
        a.rect(x - 18, y - 46, 36, 36, rx=8, fill="rgba(51,212,224,.22)", stroke=CYAN, sw=1.5, op=.9)


MOTIFS = {
    "hexcore": m_hexcore, "hexgrid": m_hexgrid, "stack": m_stack, "wheel": m_wheel,
    "rings": m_rings, "timeline": m_timeline, "signal": m_signal, "gantt": m_gantt,
    "spc": m_spc, "bins": m_bins, "flow": m_flow, "flow2": lambda a: m_flow(a, True),
    "steps": m_steps, "orbits": m_orbits, "growth": m_growth, "bridge": m_bridge,
    "network": m_network, "bars": m_bars, "mesh": m_mesh, "tanks": m_tanks,
    "worker": m_worker, "gates": m_gates,
}


# ---------------------------------------------------------------- background
def background(r):
    def blob(x, y, rad, color, op):
        return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rad)}" fill="url(#bl-{color})" opacity="{op}"/>'
    jitter = lambda v, s: v + r.uniform(-s, s)
    blobs = [
        blob(jitter(120, 80), jitter(80, 60), jitter(560, 60), "v", .95),
        blob(jitter(1500, 80), jitter(140, 60), jitter(480, 60), "t", .8),
        blob(jitter(980, 160), jitter(880, 40), jitter(360, 40), "m", .6),
    ]
    # production-line thread across the lower third
    y = r.uniform(740, 800)
    pts = [(-20, y)]
    x = -20
    while x < W + 40:
        x += r.uniform(180, 300)
        y += r.choice([-1, 1]) * r.uniform(0, 40)
        y = max(700, min(840, y))
        pts.append((x, y))
    thread = smooth(pts)
    return "\n".join(blobs), thread, pts


DEFS = """
<defs>
  <linearGradient id="g" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="1400" y2="0">
    <stop offset="0" stop-color="#8b6cff"/><stop offset="1" stop-color="#33d4e0"/>
  </linearGradient>
  <linearGradient id="hot" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#8b6cff" stop-opacity=".38"/><stop offset="1" stop-color="#33d4e0" stop-opacity=".22"/>
  </linearGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".07"/><stop offset="1" stop-color="#ffffff" stop-opacity=".025"/>
  </linearGradient>
  <linearGradient id="barfill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#8b6cff" stop-opacity=".3"/><stop offset="1" stop-color="#8b6cff" stop-opacity=".04"/>
  </linearGradient>
  <linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#33d4e0" stop-opacity=".28"/><stop offset="1" stop-color="#8b6cff" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="liquid" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#33d4e0" stop-opacity=".35"/><stop offset="1" stop-color="#8b6cff" stop-opacity=".2"/>
  </linearGradient>
  <linearGradient id="liquidp" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ff6fd8" stop-opacity=".3"/><stop offset="1" stop-color="#8b6cff" stop-opacity=".18"/>
  </linearGradient>
  <radialGradient id="bl-v"><stop offset="0" stop-color="#6a3df0" stop-opacity=".62"/><stop offset=".7" stop-color="#6a3df0" stop-opacity="0"/></radialGradient>
  <radialGradient id="bl-t"><stop offset="0" stop-color="#12b5c9" stop-opacity=".5"/><stop offset=".7" stop-color="#12b5c9" stop-opacity="0"/></radialGradient>
  <radialGradient id="bl-m"><stop offset="0" stop-color="#c53fb8" stop-opacity=".45"/><stop offset=".7" stop-color="#c53fb8" stop-opacity="0"/></radialGradient>
  <pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1.1" fill="#fff" fill-opacity=".13"/></pattern>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".9" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <mask id="dotmask"><rect width="1600" height="900" fill="url(#fade)"/></mask>
  <radialGradient id="vignette" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#0a0820" stop-opacity="0"/><stop offset="1" stop-color="#0a0820" stop-opacity=".7"/></radialGradient>
  <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
    <feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>"""


def render(slug, motif):
    a = Art(slug)
    blobs, thread, pts = background(a.r)
    MOTIFS[motif](a)
    tn = pts[len(pts) // 2]
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">
{DEFS}
<rect width="{W}" height="{H}" fill="#0a0820"/>
{blobs}
<rect width="{W}" height="{H}" fill="url(#dots)" mask="url(#dotmask)"/>
<path d="{thread}" fill="none" stroke="url(#g)" stroke-width="2.5" opacity=".55"/>
<circle cx="{f(tn[0])}" cy="{f(tn[1])}" r="5" fill="#33d4e0" filter="url(#glow)" opacity=".8"/>
<g>
{chr(10).join(a.parts)}
</g>
<rect width="{W}" height="{H}" fill="url(#vignette)"/>
</svg>
"""
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{slug}.svg").write_text(svg, encoding="utf-8")
    return OUT / f"{slug}.svg"


def main():
    if len(sys.argv) == 3:
        print(render(sys.argv[2], sys.argv[1]))
        return
    seo = yaml.safe_load((ROOT / "content" / "seo.yaml").read_text())
    for slug, meta in seo.items():
        render(slug, meta["art"])
        print(f"{meta['art']:9} {slug}")
    for p in sorted((ROOT / "content" / "posts").glob("*.md")):
        fm = yaml.safe_load(p.read_text().split("---")[1])
        render(fm.get("slug", p.stem), fm.get("art", "hexgrid"))
        print(f"{fm.get('art'):9} {p.stem}")
    # generic art for site pages
    for slug, motif in (("home", "hexgrid"), ("about", "network"), ("education", "wheel"), ("advice", "bridge"), ("thought-leadership", "bars")):
        render(f"page-{slug}", motif)


if __name__ == "__main__":
    main()
