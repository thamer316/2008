# -*- coding: utf-8 -*-
"""Shared helpers for the complex-numbers unit pages (book-style worked solutions)."""
import os, math

OUT = None          # set by make.py
PREFIX = ""         # image-name prefix of the page being built

BLUE, GREEN, RED, DARK, BROWN = "#1f4e8c", "#2e7d4f", "#c0392b", "#333", "#8a4b12"
FILL = "#cfe0f3"

def _img_dir():
    d = os.path.join(OUT, "images")
    os.makedirs(d, exist_ok=True)
    return d

def _save(name, svg):
    name = PREFIX + name
    with open(os.path.join(_img_dir(), name), "w", encoding="utf-8") as f:
        f.write(svg)
    return "images/" + name

def halo_text(x, y, s, c, anchor="start", italic=True, size=None):
    """text with a white outline drawn as a separate copy underneath (works in every SVG renderer)."""
    st = ' font-style="italic"' if italic else ""
    fs = f' font-size="{size}"' if size else ""
    common = f'x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}"{st}{fs}'
    return (f'<text {common} fill="#fff" stroke="#fff" stroke-width="3.5" stroke-linejoin="round">{s}</text>'
            f'<text {common} fill="{c}">{s}</text>')

# ====================================================================== simple vector plot (lesson 1 style)
def fmt(v):
    return ("%g" % v).replace("-", "−")

def plot(name, pts, arc=False, polygon=False, rect=None, vectors=True, dashed=True, W=330, H=260):
    xs = [0] + [p["x"] for p in pts]
    ys = [0] + [p["y"] for p in pts]
    if rect:
        xs += [rect[0], rect[2]]; ys += [rect[1], rect[3]]
    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
    # equal scale on both axes, so angles and lengths are drawn truthfully
    span = max(xmax - xmin, ymax - ymin)
    pad = 0.22 * span
    xmin_v, xmax_v = xmin - pad, xmax + pad
    ymin_v, ymax_v = ymin - pad, ymax + pad
    if xmax_v - xmin_v < 0.55 * span:          # keep room for labels on a thin plot
        c_ = (xmin_v + xmax_v) / 2; xmin_v, xmax_v = c_ - 0.3 * span, c_ + 0.3 * span
    if ymax_v - ymin_v < 0.45 * span:
        c_ = (ymin_v + ymax_v) / 2; ymin_v, ymax_v = c_ - 0.25 * span, c_ + 0.25 * span
    m = 26
    unit = min((W - 2 * m) / (xmax_v - xmin_v), (H - 2 * m) / (ymax_v - ymin_v))
    W = int((xmax_v - xmin_v) * unit + 2 * m)
    H = int((ymax_v - ymin_v) * unit + 2 * m)
    px = lambda x: m + (x - xmin_v) * unit
    py = lambda y: m + (ymax_v - y) * unit
    ox, oy = px(0), py(0)
    colors = sorted({p.get("c", BLUE) for p in pts} | {DARK})
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Cambria Math, Times New Roman, serif" font-size="13">', "<defs>"]
    for c in colors:
        o.append(f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                 f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    o.append("</defs>")
    o.append('<rect width="100%" height="100%" fill="#fff"/>')
    ax = f'stroke="{DARK}" stroke-width="1.1" marker-end="url(#a333)" marker-start="url(#a333)"'
    o.append(f'<line x1="{m-14}" y1="{oy}" x2="{W-m+14}" y2="{oy}" {ax}/>')
    o.append(f'<line x1="{ox}" y1="{H-m+14}" x2="{ox}" y2="{m-14}" {ax}/>')
    o.append(f'<text x="{W-m+10}" y="{oy+17}" text-anchor="end" font-style="italic">Re</text>')
    o.append(f'<text x="{ox-7}" y="{m-4}" text-anchor="end" font-style="italic">Im</text>')
    o.append(f'<text x="{ox-5}" y="{oy+15}" text-anchor="end" font-style="italic">O</text>')
    if rect:
        x1, y1, x2, y2 = px(rect[0]), py(rect[1]), px(rect[2]), py(rect[3])
        o.append(f'<rect x="{min(x1,x2)}" y="{min(y1,y2)}" width="{abs(x2-x1)}" height="{abs(y2-y1)}" '
                 f'fill="none" stroke="#888" stroke-dasharray="4 3"/>')
    if polygon:
        ptsstr = " ".join(f"{px(p['x'])},{py(p['y'])}" for p in pts)
        o.append(f'<polygon points="{ptsstr}" fill="#e8eef7" stroke="{BLUE}" stroke-width="1.6"/>')
    xt, yt = set(), set()
    for p in pts:
        x, y, c = p["x"], p["y"], p.get("c", BLUE)
        X, Y = px(x), py(y)
        if dashed and x != 0 and y != 0:
            o.append(f'<line x1="{X}" y1="{Y}" x2="{X}" y2="{oy}" stroke="#999" stroke-dasharray="3 3"/>')
            o.append(f'<line x1="{X}" y1="{Y}" x2="{ox}" y2="{Y}" stroke="#999" stroke-dasharray="3 3"/>')
        if x != 0 and x not in xt:
            xt.add(x)
            o.append(f'<line x1="{X}" y1="{oy-4}" x2="{X}" y2="{oy+4}" stroke="{DARK}"/>')
            ty = oy + 17 if y >= 0 else oy - 8
            o.append(f'<text x="{X}" y="{ty}" text-anchor="middle">{p.get("xl", fmt(x))}</text>')
        if y != 0 and y not in yt:
            yt.add(y)
            o.append(f'<line x1="{ox-3}" y1="{Y}" x2="{ox+3}" y2="{Y}" stroke="{DARK}"/>')
            if x >= 0 or p.get("ylside") == "left":
                o.append(f'<text x="{ox-8}" y="{Y+4}" text-anchor="end">{p.get("yl", fmt(y))}</text>')
            else:
                o.append(f'<text x="{ox+10}" y="{Y+4}" text-anchor="start">{p.get("yl", fmt(y))}</text>')
        if vectors and not polygon:
            o.append(f'<line x1="{ox}" y1="{oy}" x2="{X}" y2="{Y}" stroke="{c}" stroke-width="1.8" marker-end="url(#a{c[1:]})"/>')
        o.append(f'<circle cx="{X}" cy="{Y}" r="2.8" fill="{c}"/>')
        lab = p.get("label")
        if lab:
            w = 6.6 * len(lab)
            cx = min(max(X, w / 2 + 3), W - w / 2 - 3)
            ly = Y - 9 if y >= 0 else Y + 18
            if "lx" in p or "ly" in p:
                lx, ly2, anc = X + p.get("lx", 0), Y + p.get("ly", 0), p.get("anchor", "middle")
            elif x == 0:
                lx, ly2, anc = X + 9, Y + 4, "start"
            else:
                lx, ly2, anc = cx, ly, "middle"
            o.append(halo_text(lx, ly2, lab, c, anc, italic=True))
    if arc and pts:
        p = pts[0]
        X, Y = px(p["x"]), py(p["y"])
        phi = math.atan2(-(Y - oy), X - ox)
        r = 20
        ex_, ey_ = ox + r * math.cos(phi), oy - r * math.sin(phi)
        sweep = 0 if phi > 0 else 1
        if abs(phi) > 1e-9:
            o.append(f'<path d="M{ox+r},{oy} A{r},{r} 0 0 {sweep} {ex_:.2f},{ey_:.2f}" fill="none" stroke="{RED}" stroke-width="1.4"/>')
    o.append("</svg>")
    return _save(name, "\n".join(o))

def P(x, y, label=None, c=BLUE, **kw):
    d = dict(x=x, y=y, label=label, c=c); d.update(kw); return d

def pretty(s):
    s = s.replace("\\", "")
    out = ""
    for i, ch in enumerate(s):
        if ch in "+-" and i > 0:
            out += " " + ("−" if ch == "-" else "+") + " "
        elif ch == "-":
            out += "−"
        else:
            out += ch
    return out

# ====================================================================== grid plane (loci, regions, many points)
def cplane(name, xr, yr, items, unit=None, maxw=330, ticks=1, labels=None, gridlines=True):
    """Draw a squared complex plane.
    items:
      ("pt", x, y, label, {c, dx, dy, mark:'dot'|'x'|'open'})
      ("circle", cx, cy, r, {dash, c})
      ("line", (x1,y1), (x2,y2), {dash, c})            infinite line through two points
      ("seg", (x1,y1), (x2,y2), {dash, c, arrow})
      ("ray", (x0,y0), theta, {dash, c})               open circle at start
      ("angle", (x0,y0), t1, t2, label, {r})            angle mark
      ("ref", (x0,y0))                                   dashed half-line parallel to Re through start
      ("region", [shape, ...], {c})                      shaded intersection of shapes
           shape: ("disk",cx,cy,r) ("out",cx,cy,r) ("half",a,b,c)  [a x + b y + c >= 0]
                  ("wedge",x0,y0,t1,t2)
      ("text", x, y, s, {c, anchor})
      ("vec", (x1,y1), (x2,y2), {c})                    arrow segment
    """
    xmin, xmax = xr; ymin, ymax = yr
    if unit is None:
        unit = min(maxw / (xmax - xmin), 22.0)
    if ticks == 1 and max(xmax - xmin, ymax - ymin) > 12:
        ticks = 2
    m = 22
    W = int((xmax - xmin) * unit + 2 * m)
    H = int((ymax - ymin) * unit + 2 * m)
    px = lambda x: m + (x - xmin) * unit
    py = lambda y: m + (ymax - y) * unit
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Cambria Math, Times New Roman, serif" font-size="13">', "<defs>"]
    cols = {DARK, BLUE, GREEN, RED, BROWN}
    for it in items:
        if isinstance(it[-1], dict) and "c" in it[-1]:
            cols.add(it[-1]["c"])
    for c in cols:
        o.append(f'<marker id="m{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                 f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    clip_id = [0]
    box = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    BIG = 4 * max(xmax - xmin, ymax - ymin)

    def clip_half(poly, a, b, c):
        out = []
        n = len(poly)
        f = lambda p: a * p[0] + b * p[1] + c
        for i in range(n):
            P1, P2 = poly[i], poly[(i + 1) % n]
            f1, f2 = f(P1), f(P2)
            if f1 >= 0: out.append(P1)
            if (f1 >= 0) != (f2 >= 0):
                t = f1 / (f1 - f2)
                out.append((P1[0] + t * (P2[0] - P1[0]), P1[1] + t * (P2[1] - P1[1])))
        return out

    def path_of(shape):
        k = shape[0]
        if k == "disk":
            _, cx, cy, r = shape
            return f'<circle cx="{px(cx):.2f}" cy="{py(cy):.2f}" r="{r*unit:.2f}"/>'
        if k == "out":
            _, cx, cy, r = shape
            R = r * unit; X, Y = px(cx), py(cy)
            return (f'<path clip-rule="evenodd" fill-rule="evenodd" d="M0,0 H{W} V{H} H0 Z '
                    f'M{X-R:.2f},{Y:.2f} a{R:.2f},{R:.2f} 0 1,0 {2*R:.2f},0 a{R:.2f},{R:.2f} 0 1,0 {-2*R:.2f},0 Z"/>')
        if k == "half":
            _, a, b, c = shape
            poly = clip_half(box, a, b, c)
            return '<polygon points="' + " ".join(f"{px(x):.2f},{py(y):.2f}" for x, y in poly) + '"/>'
        if k == "wedge":
            _, x0, y0, t1, t2 = shape
            pts = [(x0, y0)]
            nseg = 60
            for j in range(nseg + 1):
                t = t1 + (t2 - t1) * j / nseg
                pts.append((x0 + BIG * math.cos(t), y0 + BIG * math.sin(t)))
            return '<polygon points="' + " ".join(f"{px(x):.2f},{py(y):.2f}" for x, y in pts) + '"/>'
        raise ValueError(k)

    defs_clip, body_regions = [], []
    for it in items:
        if it[0] == "region":
            shapes = it[1]
            col = it[2].get("c", FILL) if len(it) > 2 else FILL
            inner = f'<rect x="0" y="0" width="{W}" height="{H}" fill="{col}" fill-opacity="0.75"/>'
            for sh in shapes:
                clip_id[0] += 1
                cid = f"c{clip_id[0]}"
                defs_clip.append(f'<clipPath id="{cid}">{path_of(sh)}</clipPath>')
                inner = f'<g clip-path="url(#{cid})">{inner}</g>'
            body_regions.append(inner)
    o += defs_clip
    o.append("</defs>")
    o.append('<rect width="100%" height="100%" fill="#fff"/>')
    # grid
    if gridlines:
        x = math.ceil(xmin)
        while x <= xmax:
            o.append(f'<line x1="{px(x):.2f}" y1="{py(ymin):.2f}" x2="{px(x):.2f}" y2="{py(ymax):.2f}" stroke="#e3e3e3" stroke-width="0.8"/>')
            x += 1
        y = math.ceil(ymin)
        while y <= ymax:
            o.append(f'<line x1="{px(xmin):.2f}" y1="{py(y):.2f}" x2="{px(xmax):.2f}" y2="{py(y):.2f}" stroke="#e3e3e3" stroke-width="0.8"/>')
            y += 1
    o += body_regions
    # axes
    ax = f'stroke="{DARK}" stroke-width="1.1" marker-end="url(#m333)" marker-start="url(#m333)"'
    if ymin <= 0 <= ymax:
        o.append(f'<line x1="{px(xmin)-8:.2f}" y1="{py(0):.2f}" x2="{px(xmax)+8:.2f}" y2="{py(0):.2f}" {ax}/>')
        o.append(f'<text x="{px(xmax)+6:.2f}" y="{py(0)+15:.2f}" text-anchor="end" font-style="italic">Re</text>')
    if xmin <= 0 <= xmax:
        o.append(f'<line x1="{px(0):.2f}" y1="{py(ymin)+8:.2f}" x2="{px(0):.2f}" y2="{py(ymax)-8:.2f}" {ax}/>')
        o.append(f'<text x="{px(0)-6:.2f}" y="{py(ymax)+4:.2f}" text-anchor="end" font-style="italic">Im</text>')
        o.append(f'<text x="{px(0)-4:.2f}" y="{py(0)+13:.2f}" text-anchor="end" font-style="italic">O</text>')
    # tick labels
    if ticks:
        x = math.ceil(xmin)
        while x <= xmax:
            if x != 0 and x % ticks == 0 and xmin < x < xmax:
                o.append(f'<text x="{px(x):.2f}" y="{py(0)+13:.2f}" text-anchor="middle" font-size="11" fill="#555">{fmt(x)}</text>')
            x += 1
        y = math.ceil(ymin)
        while y <= ymax:
            if y != 0 and y % ticks == 0 and ymin < y < ymax:
                o.append(f'<text x="{px(0)-4:.2f}" y="{py(y)+4:.2f}" text-anchor="end" font-size="11" fill="#555">{fmt(y)}</text>')
            y += 1

    def clip_line(p1, p2, ray=False):
        (x1, y1), (x2, y2) = p1, p2
        dx, dy = x2 - x1, y2 - y1
        ts = []
        for (bx, by) in [(xmin, None), (xmax, None), (None, ymin), (None, ymax)]:
            if bx is not None and dx != 0:
                t = (bx - x1) / dx; yy = y1 + t * dy
                if ymin - 1e-9 <= yy <= ymax + 1e-9: ts.append(t)
            if by is not None and dy != 0:
                t = (by - y1) / dy; xx = x1 + t * dx
                if xmin - 1e-9 <= xx <= xmax + 1e-9: ts.append(t)
        if not ts: return None
        t0, t1 = min(ts), max(ts)
        if ray: t0 = 0
        return (x1 + t0 * dx, y1 + t0 * dy), (x1 + t1 * dx, y1 + t1 * dy)

    labels_after = []
    for it in items:
        k = it[0]
        opt = it[-1] if isinstance(it[-1], dict) else {}
        c = opt.get("c", BLUE)
        dash = ' stroke-dasharray="6 4"' if opt.get("dash") else ""
        if k == "circle":
            _, cx, cy, r = it[:4]
            o.append(f'<circle cx="{px(cx):.2f}" cy="{py(cy):.2f}" r="{r*unit:.2f}" fill="none" stroke="{c}" stroke-width="1.7"{dash}/>')
        elif k in ("line", "seg", "vec"):
            p1, p2 = it[1], it[2]
            if k == "line":
                r_ = clip_line(p1, p2)
                if not r_: continue
                p1, p2 = r_
                mk = f' marker-end="url(#m{c[1:]})" marker-start="url(#m{c[1:]})"'
            else:
                mk = f' marker-end="url(#m{c[1:]})"' if (k == "vec" or opt.get("arrow")) else ""
            w = opt.get("w", 1.7)
            o.append(f'<line x1="{px(p1[0]):.2f}" y1="{py(p1[1]):.2f}" x2="{px(p2[0]):.2f}" y2="{py(p2[1]):.2f}" stroke="{c}" stroke-width="{w}"{dash}{mk}/>')
        elif k == "ray":
            (x0, y0), th = it[1], it[2]
            r_ = clip_line((x0, y0), (x0 + math.cos(th), y0 + math.sin(th)), ray=True)
            if r_:
                p1, p2 = r_
                o.append(f'<line x1="{px(x0):.2f}" y1="{py(y0):.2f}" x2="{px(p2[0]):.2f}" y2="{py(p2[1]):.2f}" stroke="{c}" stroke-width="1.8"{dash} marker-end="url(#m{c[1:]})"/>')
            labels_after.append(f'<circle cx="{px(x0):.2f}" cy="{py(y0):.2f}" r="3.4" fill="#fff" stroke="{c}" stroke-width="1.5"/>')
        elif k == "ref":
            (x0, y0) = it[1]
            o.append(f'<line x1="{px(x0):.2f}" y1="{py(y0):.2f}" x2="{px(min(xmax, x0 + opt.get("len", 3))):.2f}" y2="{py(y0):.2f}" stroke="#777" stroke-dasharray="3 3"/>')
        elif k == "angle":
            (x0, y0), t1, t2, lab = it[1], it[2], it[3], it[4]
            r = opt.get("r", 18)
            X, Y = px(x0), py(y0)
            a1 = (X + r * math.cos(t1), Y - r * math.sin(t1))
            a2 = (X + r * math.cos(t2), Y - r * math.sin(t2))
            large = 1 if abs(t2 - t1) > math.pi else 0
            sweep = 0 if t2 > t1 else 1
            o.append(f'<path d="M{a1[0]:.2f},{a1[1]:.2f} A{r},{r} 0 {large} {sweep} {a2[0]:.2f},{a2[1]:.2f}" fill="none" stroke="{RED}" stroke-width="1.3"/>')
            if lab:
                tm = (t1 + t2) / 2
                rr = r + opt.get("lr", 14)
                labels_after.append(halo_text(X + rr * math.cos(tm), Y - rr * math.sin(tm) + 4, lab, RED, "middle", italic=False, size=11))
        elif k == "pt":
            _, x, y, lab = it[:4]
            X, Y = px(x), py(y)
            mark = opt.get("mark", "dot")
            if mark == "x":
                labels_after.append(f'<path d="M{X-4},{Y-4} L{X+4},{Y+4} M{X-4},{Y+4} L{X+4},{Y-4}" stroke="{c}" stroke-width="1.6"/>')
            elif mark == "none":
                pass
            elif mark == "open":
                labels_after.append(f'<circle cx="{X:.2f}" cy="{Y:.2f}" r="3.4" fill="#fff" stroke="{c}" stroke-width="1.5"/>')
            else:
                labels_after.append(f'<circle cx="{X:.2f}" cy="{Y:.2f}" r="3" fill="{c}"/>')
            if lab:
                dx, dy = opt.get("dx", 6), opt.get("dy", -6)
                anc = opt.get("anchor", "start")
                labels_after.append(halo_text(X + dx, Y + dy, lab, c, anc))
        elif k == "text":
            _, x, y, s = it[:4]
            labels_after.append(halo_text(px(x), py(y), s, c, opt.get("anchor", "middle")))
    o += labels_after
    o.append("</svg>")
    return _save(name, "\n".join(o))

# ====================================================================== content helpers
def S(lhs, rhs, why=""): return ("row", lhs, rhs, why)
def T(text): return ("p", text)
def F(text): return ("final", text)
def STEP(text): return ("step", text)
def NOTE(text, head="تنبيه"): return ("note", text, head)
def FIG(path): return ("fig", path)
def HTML(h): return ("html", h)

I2 = r"بالتبسيط: $i^2=-1$"
DEF_I = r"بافتراض أنَّ $\sqrt{-1}=i$"
ROOT_I = r"تعريف الجذر الرئيس للعدد $-1$"
MULT = "خاصية ضرب الجذور التربيعية"
ANAL = "بالتحليل"
COMM = "خاصيتا التبديل والتجميع للضرب"
MOD = "صيغة مقياس العدد المركّب"
CALC = "باستعمال الآلة الحاسبة"
TRIG = "الصورة المثلثية للعدد المركّب"
SIMP = "بالتبسيط"
DIST = "خاصية التوزيع"
Q = {1: "سعة العدد المركّب في الربع الأول", 2: "سعة العدد المركّب في الربع الثاني",
     3: "سعة العدد المركّب في الربع الثالث", 4: "سعة العدد المركّب في الربع الرابع"}
ARG = {1: r"\tan^{-1}\left(\frac{b}{a}\right)", 2: r"\pi-\tan^{-1}\left(\frac{b}{a}\right)",
       3: r"-\left(\pi-\tan^{-1}\left(\frac{b}{a}\right)\right)", 4: r"-\tan^{-1}\left(\frac{b}{a}\right)"}
QN = {1: "الأول", 2: "الثاني", 3: "الثالث", 4: "الرابع"}

# ====================================================================== page model
class Page:
    def __init__(self, slug, kicker, title, en, sub):
        self.slug, self.kicker, self.title, self.en, self.sub = slug, kicker, title, en, sub
        self.parts = []
        self.method_html = None
        global PREFIX
        PREFIX = slug + "-"

    def method(self, html):
        self.method_html = html

    def part(self, pid, title, note=None, answers_half=None):
        self.parts.append(dict(id=pid, title=title, note=note, sections=[], answers={}, half=answers_half))

    def section(self, sid, title, stem, exercises, after=None, tag=None):
        self.parts[-1]["sections"].append(dict(id=sid, title=title, stem=stem, ex=exercises, after=after or [], tag=tag))

    def ans(self, d):
        self.parts[-1]["answers"].update(d)

    # -------------------------------------------------------------- rendering
    @staticmethod
    def render_item(it):
        k = it[0]
        if k == "p": return f'<p class="txt">{it[1]}</p>'
        if k == "final": return f'<p class="final">{it[1]}</p>'
        if k == "step": return f'<p class="step">{it[1]}</p>'
        if k == "note": return f'<div class="note"><span class="note-h">{it[2]}</span> {it[1]}</div>'
        if k == "html": return it[1]
        raise ValueError(k)

    @staticmethod
    def split_long(r, w, limit=58):
        if len(r) <= limit:
            return [(r, w)]
        parts, depth, cur = [], 0, ""
        for ch in r:
            if ch in "{(": depth += 1
            elif ch in "})": depth -= 1
            if ch == "=" and depth == 0 and cur.strip():
                parts.append(cur); cur = "="
            else:
                cur += ch
        parts.append(cur)
        if len(parts) == 1:
            return [(r, w)]
        return [(p, w if i == 0 else SIMP) for i, p in enumerate(parts)]

    def render_ex(self, pid, sid, n, q, body):
        sol, figs, rows = [], [], []
        def flush():
            if rows:
                sol.append('<table class="steps" dir="ltr">' + "".join(rows) + "</table>")
                rows.clear()
        for it in body:
            if it[0] == "row":
                _, l, r, w = it
                for k, (rr, ww) in enumerate(self.split_long(r, w)):
                    ll = l if k == 0 else ""
                    rows.append(f'<tr><td class="lhs">{("$" + chr(92) + "displaystyle " + ll + "$") if ll else ""}</td>'
                                f'<td class="rhs">$\\displaystyle {rr}$</td><td class="why" dir="rtl">{ww}</td></tr>')
            elif it[0] == "fig":
                figs.append(f'<figure class="fig"><img src="{it[1]}" alt="تمثيل بياني للسؤال {n}"></figure>')
            else:
                flush(); sol.append(self.render_item(it))
        flush()
        figs_html = f'<div class="figs">{"".join(figs)}</div>' if figs else ""
        if q is None or q == "":
            qh = ""
        elif q.startswith("<"):
            qh = f'<span class="q qt">{q[1:]}</span>'
        else:
            qh = f'<span class="q" dir="ltr">${q}$</span>'
        aid = f"{pid}-{n}" if isinstance(n, int) else f"{pid}-{sid}-{n or 'x'}"
        return (f'<article class="ex" id="{aid}"><div class="ex-head"><span class="num">{n}</span>{qh}</div>'
                f'<div class="ex-body"><div class="sol">{"".join(sol)}</div>{figs_html}</div></article>')

    def ans_table(self, part):
        a = part["answers"]
        keys = list(a.keys())
        half = (len(keys) + 1) // 2
        def cell(k):
            if k is None: return '<td class="an"></td><td></td>'
            v = a[k]
            return f'<td class="an">{k}</td>' + (f'<td>{v[1:]}</td>' if v.startswith("<") else f'<td dir="ltr">${v}$</td>')
        head = '<thead><tr><th>السؤال</th><th>الإجابة النهائية</th><th>السؤال</th><th>الإجابة النهائية</th></tr></thead>'
        rows = "".join(f'<tr>{cell(keys[i])}{cell(keys[i+half] if i + half < len(keys) else None)}</tr>' for i in range(half))
        return f'<table class="answers">{head}<tbody>{rows}</tbody></table>'

    def write(self, nav):
        toc, body = [], []
        for part in self.parts:
            pid = part["id"]
            items = []
            secs = part["sections"]
            for idx, s in enumerate(secs):
                nums = [str(e[0]) for e in s["ex"]]
                if s["title"]:
                    j = idx + 1
                    while j < len(secs) and not secs[j]["title"]:
                        nums += [str(e[0]) for e in secs[j]["ex"]]; j += 1
                    rng = f"{nums[0]}–{nums[-1]}" if len(nums) > 1 else (nums[0] if nums else "")
                    items.append(f'<li><a href="#{pid}-{s["id"]}"><span>{s["title"]}</span><span class="rng">{rng}</span></a></li>')
                    s["rng"] = rng
            if part["answers"]:
                items.append(f'<li><a href="#{pid}-answers"><span>جدول الإجابات النهائية</span><span class="rng"></span></a></li>')
            toc.append(f'<div class="toc-part"><h3><a href="#{pid}">{part["title"]}</a></h3><ol>{"".join(items)}</ol></div>')

            out = [f'<div class="part" id="{pid}"><h2 class="part-h">{part["title"]}</h2>']
            if part["note"]:
                out.append(f'<p class="part-note">{part["note"]}</p>')
            for s in secs:
                sec = [f'<section class="sec" id="{pid}-{s["id"]}">']
                if s["title"]:
                    rng = s.get("rng", "")
                    rng_html = f' <span class="rng">({rng})</span>' if rng.strip("–") else ""
                    sec.append(f'<h2>{s["title"]}{rng_html}</h2>')
                if s["stem"]:
                    sec.append(f'<p class="stem">{s["stem"]}</p>')
                if s["tag"]:
                    sec.append(s["tag"])
                for e in s["ex"]:
                    sec.append(self.render_ex(pid, s["id"], *e))
                for it in s["after"]:
                    if it[0] == "fig":
                        sec.append(f'<figure class="fig wide"><img src="{it[1]}" alt="تمثيل بياني"></figure>')
                    else:
                        sec.append(self.render_item(it))
                sec.append("</section>")
                out.append("\n".join(sec))
            if part["answers"]:
                out.append(f'<section class="sec ans-sec" id="{pid}-answers"><h2>جدول الإجابات النهائية – {part["title"]}</h2>'
                           f'<div class="ans-wrap">{self.ans_table(part)}</div></section>')
            out.append("</div>")
            body.append("\n".join(out))

        nav_html = " ".join(
            (f'<a class="cur" href="{href}">{lab}</a>' if href == self.slug + ".html" else f'<a href="{href}">{lab}</a>')
            for href, lab in nav)
        method = f'<section class="method"><h2>طريقة الكتاب في هذا الدرس</h2>{self.method_html}</section>' if self.method_html else ""
        page = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{self.title} – الأعداد المركّبة</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<link rel="stylesheet" href="css/style.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script defer src="js/main.js"></script>
</head>
<body>
<header class="top">
  <div class="top-in">
    <div>
      <div class="kicker">{self.kicker}</div>
      <h1>{self.title} <span class="en">{self.en}</span></h1>
      <div class="sub">{self.sub}</div>
    </div>
    <div class="author">Homam Alkrad<br><span dir="ltr">0791089960</span></div>
  </div>
  <nav class="pages">{nav_html}</nav>
</header>
<main>
<nav class="toc">
  <h2>المحتويات</h2>
  <div class="toc-grid">{"".join(toc)}</div>
  <p class="howto">طريقة عرض الحل: كل خطوة في سطر مستقل وبجانبها سببها، ويُختم الحل بعبارة «إذن»، تمامًا كما في الكتاب المدرسي. الآلة الحاسبة على نظام الراديان (Radian)، وتُقرَّب السعة إلى منزلتين عشريتين.</p>
</nav>
{method}
{"".join(body)}
</main>
<footer class="foot">Homam Alkrad · <span dir="ltr">0791089960</span></footer>
</body>
</html>
"""
        with open(os.path.join(OUT, self.slug + ".html"), "w", encoding="utf-8") as f:
            f.write(page)
        return len(page)

# ====================================================================== book "table method" for polynomial division
def div_table(divisor, quotient, rows, rem="0"):
    """divisor: [first, second] terms (latex); quotient: list of latex terms;
    rows: two lists of products (latex); rem: remainder."""
    head = r'<tr><td class="dt-x">$\times$</td>' + "".join(f'<td class="dt-q">${q}$</td>' for q in quotient) + '<td class="dt-blank"></td></tr>'
    r1 = f'<tr><td class="dt-d">${divisor[0]}$</td>' + "".join(f'<td class="dt-p">${p}$</td>' for p in rows[0]) + f'<td class="dt-r">${rem}$</td></tr>'
    r2 = f'<tr><td class="dt-d">${divisor[1]}$</td>' + "".join(f'<td class="dt-p">${p}$</td>' for p in rows[1]) + '<td class="dt-blank"></td></tr>'
    return HTML(f'<table class="divtab" dir="ltr">{head}{r1}{r2}</table>')


def sqrt_steps(a, b, z_tex, x_vals, y_of, k_tex, quartic, factored, xsq, roots_tex, note_x=None):
    """Book method (example 5, lesson 2) for the square roots of z = a + bi.
    a, b: latex of real / imaginary parts; k_tex: latex of b/2 (so y = k/x);
    quartic: latex of 'x^4 ... = 0'; factored: latex of factorisation; xsq: latex 'x^2=p or x^2=-q';
    x_vals: list of (x_tex, y_tex) pairs; roots_tex: final roots."""
    rows = [
        T(r"أفترض أنَّ: $\sqrt{z}=x+iy$ ، حيث $x$ و $y$ عددان حقيقيان:"),
        S(r"\sqrt{z}", r"=x+iy", "بالفرض"),
        S(r"z", r"=(x+iy)^2", "بتربيع الطرفين"),
        S(z_tex, r"=(x+iy)^2", r"بتعويض قيمة $z$"),
        S(z_tex, r"=x^2+2ixy+i^2y^2", "بفكّ القوسين"),
        S(z_tex, r"=x^2-y^2+2ixy", r"بتعويض $i^2=-1$"),
        S(a, r"=x^2-y^2", "بمساواة الجزأين الحقيقيين"),
        S(b, r"=2xy", "بمساواة الجزأين التخيّليين"),
        T("إذن، ينتج النظام الآتي الذي يحوي معادلتين بمتغيّرين، ويُمكِن حلُّه بطريقة التعويض:"),
        S(r"y", rf"={k_tex}", r"بحلّ المعادلة الثانية لـ $y$"),
        S(r"x^2-\left(" + k_tex + r"\right)^2", "=" + a, r"بتعويض $y$ في المعادلة الأولى"),
        S(quartic.split("=")[0], "=0", r"بضرب طرفي المعادلة في $x^2$ وإعادة ترتيبها"),
        S(factored, "=0", "بالتحليل"),
        S("", xsq, "بحلّ المعادلتين"),
        T(note_x or r"بما أنَّ $x$ عدد حقيقي، فإنَّ: $x=" + (r"\pm " + x_vals[0][0]) + "$."),
        T(r"وبتعويض قيمتي $x$ في المعادلة: $y=" + k_tex + r"$ ، فإنَّ الناتج:"),
    ]
    for xv, yv in x_vals:
        rows.append(S(rf"x={xv}", rf"\to\ y={yv}", ""))
    rows.append(F(rf"إذن، الجذران التربيعيان للعدد المركّب: ${z_tex}$ هما: ${roots_tex}$"))
    return rows


def eq_from_roots(n, p, q, var="x"):
    """quadratic with roots p ± qi via the book's reverse steps. p, q are ints (q>0)."""
    pp = f"{p}" if p >= 0 else f"({p})"
    sub = f"{var}-{p}" if p > 0 else (f"{var}+{-p}" if p < 0 else var)
    b = -2 * p
    c = p * p + q * q
    lin = (f"-{-b}{var}" if b < 0 else (f"+{b}{var}" if b > 0 else ""))
    root = rf"{p}\pm {q}i" if p != 0 else rf"\pm {q}i"
    rows = [
        S(var, f"={root}", rf"${root}$ هما جذران للمعادلة"),
        S(sub, rf"=\pm {q}i", (rf"بطرح ${p}$ من طرفي المعادلة" if p > 0 else rf"بجمع ${-p}$ لطرفي المعادلة") if p != 0 else ""),
        S(f"({sub})^2", f"={-q*q}", "بتربيع الطرفين"),
        S(f"{var}^2{lin}+{c}", "=0", SIMP),
        F(rf"إذن، المعادلة التربيعية هي: ${var}^2{lin}+{c}=0$"),
    ]
    return (n, root, rows)
