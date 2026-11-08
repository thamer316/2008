# -*- coding: utf-8 -*-
"""Helpers for lesson 3 (locus): book-style steps + figures."""
import math
from fractions import Fraction as Fr
from lib import *

PI = math.pi


def num(v):
    """latex of a number (int / Fraction / float / str)."""
    if isinstance(v, str): return v
    if isinstance(v, Fr):
        if v.denominator == 1: return str(v.numerator)
        s = "-" if v < 0 else ""
        return rf"{s}\frac{{{abs(v.numerator)}}}{{{v.denominator}}}"
    if isinstance(v, float) and v.is_integer(): return str(int(v))
    return str(v)


def shift(var, c):
    """'x-3', 'x+3' or 'x' for var - c."""
    if isinstance(c, str):
        if c.startswith("-"): return f"{var}+{c[1:]}"
        return f"{var}-{c}"
    if c == 0: return var
    return f"{var}-{num(c)}" if c > 0 else f"{var}+{num(-c)}"


def cnum(a, b):
    """latex of a+bi."""
    A = num(a) if not (isinstance(a, (int, Fr)) and a == 0) else ""
    if isinstance(b, (int, Fr)) and b == 0:
        return A or "0"
    bb = num(b)
    if bb == "1": bt = "i"
    elif bb == "-1": bt = "-i"
    else: bt = bb + "i"
    if not A: return bt
    return A + (bt if bt.startswith("-") else "+" + bt)


def zminus(a, b):
    """latex of z-(a+bi) simplified, e.g. z-2+8i."""
    s = "z"
    if a: s += (f"-{num(a)}" if (a > 0 if not isinstance(a, str) else not a.startswith("-")) else f"+{num(-a) if not isinstance(a, str) else a[1:]}")
    if b:
        if isinstance(b, str):
            s += (f"+{b[1:]}i" if b.startswith("-") else f"-{b}i")
        else:
            mag = "" if abs(b) == 1 else num(abs(b))
            s += (f"-{mag}i" if b > 0 else f"+{mag}i")
    return s


def frange(pts, pad=1.0, minspan=6):
    xs = [p[0] for p in pts] + [0]
    ys = [p[1] for p in pts] + [0]
    x0, x1 = math.floor(min(xs) - pad), math.ceil(max(xs) + pad)
    y0, y1 = math.floor(min(ys) - pad), math.ceil(max(ys) + pad)
    if x1 - x0 < minspan: x1 = x0 + minspan
    if y1 - y0 < minspan: y1 = y0 + minspan
    return (x0, x1), (y0, y1)


def unit_for(xr, yr, maxw=300, maxh=300):
    return min(maxw / (xr[1] - xr[0]), maxh / (yr[1] - yr[0]), 26)


# ------------------------------------------------------------------ circle
def circle_steps(a, b, r, r2, given, cart=True, rtex=None):
    """a, b numbers (center), r float radius, r2 latex of r^2, given latex equation."""
    rt = rtex or num(r)
    c = cnum(a, b)
    rows = [STEP("الخطوة 1: أجد المحل الهندسي."),
            T(rf"عندما أكتب المعادلة في صورة: $|z-(a+ib)|=r$ ، فإنَّ: $|z-({c})|={rt}$ ، وهذه معادلة دائرة مركزها $({num(a)},\,{num(b)})$ ، وطول نصف قطرها ${rt}$ وحدات.")]
    if cart:
        sx, sy = shift("x", a), shift("y", b)
        inner = f"x+iy{'' if not a else ('-' + num(a) if a > 0 else '+' + num(-a))}"
        if b:
            inner += (f"-{num(b) if abs(b) != 1 else ''}i" if b > 0 else f"+{num(-b) if abs(b) != 1 else ''}i")
        rows += [STEP("الخطوة 2: أكتب المعادلة بالصيغة الديكارتية."),
                 S(given, "", "المعادلة المعطاة"),
                 S(rf"|{inner}|", f"={rt}", r"باستبدال $z$ بالصيغة $x+iy$"),
                 S(rf"|({sx})+({sy})i|", f"={rt}", "بتجميع الحدود المتشابهة"),
                 S(rf"\sqrt{{({sx})^2+({sy})^2}}", f"={rt}", "صيغة مقياس العدد المركّب"),
                 S(rf"({sx})^2+({sy})^2", f"={r2}", "بتربيع الطرفين")]
    return [tidy(r) for r in rows]


def tidy(row):
    """(x)^2 -> x^2, |(x)+(y)i| -> |x+yi|."""
    if row[0] != "row":
        return row
    fix = lambda s: s.replace("(x)^2", "x^2").replace("(y)^2", "y^2").replace("(x)+", "x+").replace("+(y)i", "+iy")
    return ("row", fix(row[1]), fix(row[2]), row[3])


def circle_fig(name, a, b, r, extra=(), dash=False, center_lab=None):
    xr, yr = frange([(a - r, b - r), (a + r, b + r)])
    items = [("circle", a, b, r, {"c": BLUE, "dash": dash}), ("pt", a, b, center_lab or f"({fmt(a)}, {fmt(b)})", {"c": BLUE})] + list(extra)
    return cplane(name, xr, yr, items, unit=unit_for(xr, yr))


# ------------------------------------------------------------------ perpendicular bisector
def bis_eq(p, q):
    """|z-p| = |z-q|  ->  A x + B y + C = 0 (integers, reduced)."""
    (a, b), (c, d) = p, q
    A = Fr(-2 * a + 2 * c); B = Fr(-2 * b + 2 * d); C = Fr(a * a + b * b - c * c - d * d)
    from math import gcd
    den = 1
    for v in (A, B, C): den = den * v.denominator // gcd(den, v.denominator)
    A, B, C = A * den, B * den, C * den
    g = 0
    for v in (A, B, C): g = gcd(g, int(abs(v)))
    g = g or 1
    A, B, C = int(A / g), int(B / g), int(C / g)
    if A < 0 or (A == 0 and B < 0): A, B, C = -A, -B, -C
    return A, B, C


def lin_tex(A, B, C):
    s = ""
    for coef, var in ((A, "x"), (B, "y"), (C, "")):
        if coef == 0: continue
        mag = abs(coef)
        t = (("" if mag == 1 and var else str(mag)) + var)
        if not s: s = ("-" if coef < 0 else "") + t
        else: s += ("-" if coef < 0 else "+") + t
    return s + "=0"


def bisector_steps(p, q, given, cart=True):
    (a, b), (c, d) = p, q
    rows = [STEP("الخطوة 1: أجد المحل الهندسي."),
            T(rf"عندما أكتب المعادلة في صورة: $|z-(a+ib)|=|z-(c+id)|$ ، فإنَّ: $|z-({cnum(a, b)})|=|z-({cnum(c, d)})|$ ، "
              rf"وهذه معادلة المُنصِّف العمودي للقطعة المستقيمة التي تصل بين النقطتين: $({num(a)},\,{num(b)})$ ، و $({num(c)},\,{num(d)})$.")]
    if cart:
        A, B, C = bis_eq(p, q)
        def grp(a, b):
            return rf"|({shift('x', a)})+({shift('y', b)})i|"
        def sq(a, b):
            return rf"\sqrt{{({shift('x', a)})^2+({shift('y', b)})^2}}"
        def expand(a, b):
            parts = ["x^2"]
            if a: parts.append(("-" if a > 0 else "+") + f"{num(abs(2 * a))}x")
            if a: parts.append(f"+{num(a * a)}")
            parts.append("+y^2")
            if b: parts.append(("-" if b > 0 else "+") + f"{num(abs(2 * b))}y")
            if b: parts.append(f"+{num(b * b)}")
            return "".join(parts)
        def lin_side(a, b):
            t = ""
            if a: t += ("-" if a > 0 else "+") + f"{num(abs(2 * a))}x"
            if b: t += ("-" if b > 0 else "+") + f"{num(abs(2 * b))}y"
            k = a * a + b * b
            if k: t += f"+{num(k)}"
            t = t.lstrip("+")
            return t or "0"
        rows += [STEP("الخطوة 2: أكتب المعادلة بالصيغة الديكارتية."),
                 S(given, "", "المعادلة المعطاة"),
                 S(grp(a, b), "=" + grp(c, d), r"باستبدال $z$ بالصيغة $x+iy$ ، وبتجميع الحدود المتشابهة"),
                 S(sq(a, b), "=" + sq(c, d), "صيغة مقياس العدد المركّب"),
                 S(expand(a, b), "=" + expand(c, d), "بتربيع الطرفين، وفكّ الأقواس"),
                 S(lin_side(a, b), "=" + lin_side(c, d), r"بطرح $x^2$ و $y^2$ من الطرفين"),
                 S(lin_tex(A, B, C)[:-2], "=0", r"بكتابة المعادلة في صورة: $Ax+By+C=0$")]
        rows = [tidy(r) for r in rows]
    return rows


def bisector_fig(name, p, q, extra=(), region=None, dash=False, labels=None):
    (a, b), (c, d) = p, q
    xr, yr = frange([p, q], pad=2)
    mx, my = (a + c) / 2, (b + d) / 2
    dx, dy = c - a, d - b
    l1, l2 = (mx, my), (mx - dy, my + dx)
    items = []
    if region:
        items.append(("region", region))
    items += [("seg", p, q, {"c": "#7a8ea8", "dash": True, "w": 1.2}),
              ("line", l1, l2, {"c": RED, "dash": dash}),
              ("pt", a, b, (labels or {}).get("p", f"({fmt(a)}, {fmt(b)})"), {"c": BLUE}),
              ("pt", c, d, (labels or {}).get("q", f"({fmt(c)}, {fmt(d)})"), {"c": BLUE})] + list(extra)
    return cplane(name, xr, yr, items, unit=unit_for(xr, yr))


# ------------------------------------------------------------------ ray
def ang_tex(t):
    return t


def ray_steps(a, b, th_tex, given):
    return [T(rf"عندما أكتب المعادلة في صورة: $\text{{Arg}}(z-(a+bi))=\theta$ ، فإنَّ: $\text{{Arg}}(z-({cnum(a, b)}))={th_tex}$ ، "
              rf"وهذه معادلة شعاع يبدأ بالنقطة $({num(a)},\,{num(b)})$ ، ولا يشملها، ويصنع زاوية قياسها ${th_tex}$ مع المستقيم الذي يوازي المحور الحقيقي.")]


def ray_fig(name, a, b, th, th_lab, extra=(), span=5):
    ex, ey = a + span * math.cos(th), b + span * math.sin(th)
    xr, yr = frange([(a, b), (ex, ey)], pad=1.5)
    items = [("ref", (a, b), {"len": 3}), ("ray", (a, b), th, {"c": BLUE}),
             ("angle", (a, b), 0, th, th_lab, {"r": 16}), ("pt", a, b, f"({fmt(a)}, {fmt(b)})", {"c": DARK, "mark": "none", "dx": 6, "dy": 14})] + list(extra)
    return cplane(name, xr, yr, items, unit=unit_for(xr, yr))


def bis_raw(p, q):
    """coefficients of |z-p|^2 - |z-q|^2 = A x + B y + C (sign preserved)."""
    (a, b), (c, d) = p, q
    return (2 * c - 2 * a, 2 * d - 2 * b, a * a + b * b - c * c - d * d)


def closer_to(p, q):
    """half-plane shape of the points with |z-p| <= |z-q|."""
    A, B, C = bis_raw(p, q)
    return ("half", -A, -B, -C)
