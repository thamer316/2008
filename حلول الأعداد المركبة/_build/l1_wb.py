# -*- coding: utf-8 -*-
"""Lesson 1 – كتاب التمارين (workbook pages 40–41, questions 1–42)."""
import math
from lib import *


def root(n, inside, steps, res):
    return (n, inside, steps + [F(rf"إذن: ${inside}={res}$")])


def ipow(n, k):
    q, r = divmod(k, 2)
    # i^k = (i^2)^q * i^r
    sign = -1 if q % 2 else 1
    val = {(1, 0): "1", (-1, 0): "-1", (1, 1): "i", (-1, 1): "-i"}[(sign, r)]
    rows = []
    if r == 0:
        rows.append(S(rf"i^{{{k}}}", rf"=(i^2)^{{{q}}}", "خاصية قوّة القوّة"))
        rows.append(S("", rf"=(-1)^{{{q}}}", r"بالتبسيط: $i^2=-1$"))
    else:
        rows.append(S(rf"i^{{{k}}}", rf"=(i^2)^{{{q}}}\times i", "خاصية قوّة القوّة"))
        rows.append(S("", rf"=(-1)^{{{q}}}\times i", r"بالتبسيط: $i^2=-1$"))
    rows.append(S("", "=" + val, rf"بالتبسيط: $(-1)^{{{q}}}={sign}$، لأنَّ الأُس {'فردي' if q % 2 else 'زوجي'}"))
    return (n, rf"i^{{{k}}}", rows + [F(rf"إذن: $i^{{{k}}}={val}$")]), val


def build(pg):
    # ------------------------------------------------------------ 1–6
    pg.section("w1", "الجذر الرئيس بدلالة $i$", r"أجد قيمة الجذر الرئيس في كلٍّ ممّا يأتي بدلالة $i$:", [
        root(1, r"\sqrt{-128}", [
            S(r"\sqrt{-128}", r"=\sqrt{-1\times64\times2}", ANAL),
            S("", r"=\sqrt{-1}\times\sqrt{64}\times\sqrt{2}", MULT),
            S("", r"=i\times8\times\sqrt2=8i\sqrt2", ROOT_I)], r"8i\sqrt2"),
        root(2, r"\sqrt{-14}", [
            S(r"\sqrt{-14}", r"=\sqrt{-1\times14}", ANAL),
            S("", r"=\sqrt{-1}\times\sqrt{14}", MULT),
            S("", r"=i\sqrt{14}", ROOT_I)], r"i\sqrt{14}"),
        root(3, r"\sqrt{-81}", [
            S(r"\sqrt{-81}", r"=\sqrt{-1\times81}", ANAL),
            S("", r"=\sqrt{-1}\times\sqrt{81}", MULT),
            S("", r"=i\times9=9i", ROOT_I)], "9i"),
        root(4, r"\sqrt{-125}", [
            S(r"\sqrt{-125}", r"=\sqrt{-1\times25\times5}", ANAL),
            S("", r"=\sqrt{-1}\times\sqrt{25}\times\sqrt{5}", MULT),
            S("", r"=i\times5\times\sqrt5=5i\sqrt5", ROOT_I)], r"5i\sqrt5"),
        root(5, r"3\sqrt{-32}", [
            S(r"3\sqrt{-32}", r"=3\sqrt{-1\times16\times2}", ANAL),
            S("", r"=3\times\sqrt{-1}\times\sqrt{16}\times\sqrt{2}", MULT),
            S("", r"=3\times i\times4\times\sqrt2", ROOT_I),
            S("", r"=12i\sqrt2", SIMP)], r"12i\sqrt2"),
        root(6, r"\sqrt{\dfrac{-28}{9}}", [
            S(r"\sqrt{\dfrac{-28}{9}}", r"=\sqrt{-1\times\dfrac{4\times7}{9}}", ANAL),
            S("", r"=\sqrt{-1}\times\dfrac{\sqrt4\times\sqrt7}{\sqrt9}", "خاصية ضرب الجذور التربيعية وجذر القسمة"),
            S("", r"=i\times\dfrac{2\sqrt7}{3}=\dfrac{2i\sqrt7}{3}", ROOT_I)], r"\dfrac{2i\sqrt7}{3}"),
    ])
    pg.ans({1: r"8i\sqrt2", 2: r"i\sqrt{14}", 3: "9i", 4: r"5i\sqrt5", 5: r"12i\sqrt2", 6: r"\frac{2i\sqrt7}{3}"})

    # ------------------------------------------------------------ 7–10
    exs, ans = [], {}
    for n, k in [(7, 7), (8, 12), (9, 98), (10, 121)]:
        e, v = ipow(n, k); exs.append(e); ans[n] = v
    pg.section("w2", "قوى $i$", r"أجد ناتج كلٍّ ممّا يأتي في أبسط صورة بافتراض أنَّ $\sqrt{-1}=i$:", exs)
    pg.ans(ans)

    # ------------------------------------------------------------ 11
    tbl = ('<table class="answers mini" dir="ltr"><thead><tr><th>$z$</th><th>$Re(z)$</th><th>$Im(z)$</th></tr></thead><tbody>'
           '<tr><td>$-4+6i$</td><td><b>$-4$</b></td><td><b>$6$</b></td></tr>'
           '<tr><td>$-3$</td><td><b>$-3$</b></td><td><b>$0$</b></td></tr>'
           '<tr><td>$8i$</td><td><b>$0$</b></td><td><b>$8$</b></td></tr>'
           '<tr><td><b>$-8+3i$</b></td><td>$-8$</td><td>$3$</td></tr></tbody></table>')
    pg.section("w3", "الجزء الحقيقي والجزء التخيّلي", "", [
        (11, "<أملأ الفراغ بما هو مناسب في الجدول الآتي:", [
            T(r"في العدد المركّب $z=a+ib$: الجزء الحقيقي $Re(z)=a$ ، والجزء التخيّلي $Im(z)=b$ (وليس $ib$)."),
            T(r"$-3=-3+0i$ ، و $8i=0+8i$ ، وإذا كان $Re(z)=-8$ و $Im(z)=3$ فإنَّ $z=-8+3i$."),
            HTML(tbl)]),
    ])
    pg.ans({11: r"-8+3i"})

    # ------------------------------------------------------------ 12–23
    pts = [(12, 5, 0), (13, -4, 0), (14, 0, 4), (15, 0, -3), (16, 4, -2), (17, -3, 5),
           (18, -3, -5), (19, 0, 1), (20, 7, -4), (21, -5, 4), (22, -7, -2), (23, 5, 5)]
    zs = {12: "5", 13: "-4", 14: "4i", 15: "-3i", 16: "4-2i", 17: "-3+5i", 18: "-3-5i", 19: "i",
          20: "7-4i", 21: "-5+4i", 22: "-7-2i", 23: "5+5i"}
    items = [("pt", x, y, str(n), {"c": BLUE, "dx": 5, "dy": -5}) for n, x, y in pts]
    f = cplane("w12-23.svg", (-8, 8), (-8, 8), items, unit=21)
    exs = []
    for n, x, y in pts:
        exs.append((n, "z=" + zs[n], [T(rf"$z={zs[n]}={x}{'+' if y >= 0 else '-'}{abs(y)}i$ ، يُمثِّله الزوج المرتّب $({x},\,{y})$، وهو النقطة المُرقَّمة بالرقم ${n}$ في الشكل.")]))
    pg.section("w4", "تمثيل الأعداد المركّبة", r"أُمثِّل كُلًّا من الأعداد المركّبة الآتية في المستوى المركّب. يُمثَّل العدد $a+ib$ بالزوج المرتّب $(a,\,b)$:",
               exs, after=[T("التمثيل البياني للأعداد (12–23) في المستوى المركّب نفسه، وكل نقطة مكتوب بجانبها رقم السؤال:"), FIG(f)])
    pg.ans({n: f"({x},{y})" for n, x, y in pts})

    # ------------------------------------------------------------ 24
    pts24 = [("A", 4, 5), ("B", 0, 3), ("C", 2, -6), ("D", 0, -2), ("E", -4, 0), ("F", -5, -4), ("G", -3, 4)]
    f24 = cplane("w24.svg", (-8, 8), (-8, 8), [("pt", x, y, L, {"mark": "x", "c": DARK}) for L, x, y in pts24], unit=18)
    body = [T("أقرأ إحداثيي كل نقطة من الشكل، فيكون العدد المركّب الذي تمثّله النقطة $(a,\\,b)$ هو $a+ib$، ثمَّ أجد المقياس $|z|=\\sqrt{a^2+b^2}$، والسعة حسب الربع الذي يقع فيه العدد:"),
            FIG(f24)]
    rows = [
        ("A", "4+5i", (4, 5), r"\sqrt{4^2+5^2}=\sqrt{41}", r"\tan^{-1}\left(\frac{5}{4}\right)\approx0.90", "الربع الأول"),
        ("B", "3i", (0, 3), r"\sqrt{0^2+3^2}=3", r"\frac{\pi}{2}\approx1.57", "على الجزء الموجب من المحور التخيّلي"),
        ("C", "2-6i", (2, -6), r"\sqrt{2^2+(-6)^2}=\sqrt{40}=2\sqrt{10}", r"-\tan^{-1}\left(\frac{6}{2}\right)\approx-1.25", "الربع الرابع"),
        ("D", "-2i", (0, -2), r"\sqrt{0^2+(-2)^2}=2", r"-\frac{\pi}{2}\approx-1.57", "على الجزء السالب من المحور التخيّلي"),
        ("E", "-4", (-4, 0), r"\sqrt{(-4)^2+0^2}=4", r"\pi\approx3.14", "على الجزء السالب من المحور الحقيقي"),
        ("F", "-5-4i", (-5, -4), r"\sqrt{(-5)^2+(-4)^2}=\sqrt{41}", r"-\left(\pi-\tan^{-1}\left(\frac{4}{5}\right)\right)\approx-2.47", "الربع الثالث"),
        ("G", "-3+4i", (-3, 4), r"\sqrt{(-3)^2+4^2}=5", r"\pi-\tan^{-1}\left(\frac{4}{3}\right)\approx2.21", "الربع الثاني"),
    ]
    for L, z, (x, y), m, a, where in rows:
        body.append(STEP(rf"النقطة ${L}$: الزوج المرتّب $({x},\,{y})$ ، إذن: ${L}={z}$ ({where})."))
        body.append(S(rf"|{L}|", "=" + m, MOD))
        body.append(S(rf"\text{{Arg}}({L})", "=" + a, "حسب ملخص سعة العدد المركّب" if "tan" in a else "موقع النقطة على أحد المحورين"))
    body.append(F(r"إذن: $A=4+5i$ ، $B=3i$ ، $C=2-6i$ ، $D=-2i$ ، $E=-4$ ، $F=-5-4i$ ، $G=-3+4i$ ، ومقاييسها وسعاتها كما في الخطوات أعلاه"))
    pg.section("w5", "قراءة الأعداد من المستوى المركّب",
               "", [(24, "<أكتب كُلًّا من الأعداد المركّبة المُمثَّلة بيانيًّا في المستوى المركّب المجاور بالصورة القياسية، ثمَّ أجد مقياسه وسعته.", body)])
    pg.ans({24: "<$A=4+5i$، $B=3i$، $C=2-6i$، $D=-2i$، $E=-4$، $F=-5-4i$، $G=-3+4i$"})

    # ------------------------------------------------------------ 25–26
    RE, IM = "بمساواة الجزأين الحقيقيين", "بمساواة الجزأين التخيّليين"
    pg.section("w6", "تساوي عددين مركّبين", r"أجد قيمة $x$ وقيمة $y$ الحقيقيتين اللتين تجعلان كل معادلة ممّا يأتي صحيحة:", [
        (25, r"(2x+1)+4i=7-i(y-3)", [
            S(r"(2x+1)+4i", r"=7+(3-y)i", "بكتابة الطرف الأيسر بالصورة القياسية"),
            S(r"2x+1", r"=7", RE),
            S(r"x", r"=3", "بحلّ المعادلة"),
            S(r"4", r"=3-y", IM),
            S(r"y", r"=-1", "بحلّ المعادلة"),
            F(r"إذن: $x=3,\ y=-1$")]),
        (26, r"i(2x-4y)+x+3y=26+32i", [
            S(r"(x+3y)+i(2x-4y)", r"=26+32i", "بكتابة الطرف الأيمن بالصورة القياسية"),
            S(r"x+3y", r"=26 \quad\cdots(1)", RE),
            S(r"2x-4y", r"=32 \quad\cdots(2)", IM),
            S(r"x-2y", r"=16 \quad\cdots(3)", r"بقسمة المعادلة $(2)$ على $2$"),
            S(r"5y", r"=10", r"بطرح المعادلة $(3)$ من المعادلة $(1)$"),
            S(r"y", r"=2", "بحلّ المعادلة"),
            S(r"x", r"=26-3(2)=20", r"بتعويض $y=2$ في المعادلة $(1)$"),
            F(r"إذن: $x=20,\ y=2$")]),
    ])
    pg.ans({25: "x=3,\\ y=-1", 26: "x=20,\\ y=2"})

    # ------------------------------------------------------------ 27–32  (trig form, 3 steps)
    def trig3(n, z, mod_rows, arg_rows, r, th, final_th=None):
        th2 = final_th or th
        return (n, z, [STEP(r"الخطوة 1: أجد مقياس العدد المركّب $z$.")] + mod_rows +
                [STEP(r"الخطوة 2: أجد سعة العدد المركّب $z$.")] + arg_rows +
                [STEP(r"الخطوة 3: أكتب العدد المركّب $z$ بالصورة المثلثية."),
                 S(r"z", rf"{'\\approx' if '.' in th2 else '='}{r}\left(\cos\left({th2}\right)+i\sin\left({th2}\right)\right)", rf"بتعويض $r={r},\ \theta={th2}$"),
                 F(rf"إذن: $z{'\\approx' if '.' in th2 else '='}{r}\left(\cos\left({th2}\right)+i\sin\left({th2}\right)\right)$")])

    pg.section("w7", "الصورة المثلثية", r"أكتب كُلًّا من الأعداد المركّبة الآتية بالصورة المثلثية:", [
        trig3(27, "z=6", [S("r", r"=\sqrt{6^2+0^2}=6", MOD)],
              [T(r"العدد $z=6$ يقع على الجزء الموجب من المحور الحقيقي، إذن: $\text{Arg}(z)=0$.")], "6", "0"),
        trig3(28, "z=-5i", [S("r", r"=\sqrt{0^2+(-5)^2}=5", MOD)],
              [T(r"العدد $z=-5i$ يقع على الجزء السالب من المحور التخيّلي، إذن: $\text{Arg}(z)=-\dfrac{\pi}{2}$.")], "5", r"-\frac{\pi}{2}"),
        trig3(29, r"z=-2\sqrt3-2i", [S("r", r"=\sqrt{(-2\sqrt3)^2+(-2)^2}=\sqrt{12+4}=4", MOD)],
              [T(r"بما أنَّ العدد المركّب $z$ يقع في الربع الثالث، فإنَّ:"),
               S(r"\text{Arg}(z)", "=" + ARG[3], Q[3]),
               S("", r"=-\left(\pi-\tan^{-1}\left(\frac{2}{2\sqrt3}\right)\right)", r"بتعويض $a=2\sqrt3,\ b=2$"),
               S("", r"=-\left(\pi-\frac{\pi}{6}\right)=-\frac{5\pi}{6}", r"بالتبسيط: $\tan^{-1}\left(\frac{1}{\sqrt3}\right)=\frac{\pi}{6}$")],
              "4", r"-\frac{5\pi}{6}"),
        trig3(30, r"z=-1+i", [S("r", r"=\sqrt{(-1)^2+1^2}=\sqrt2", MOD)],
              [T(r"بما أنَّ العدد المركّب $z$ يقع في الربع الثاني، فإنَّ:"),
               S(r"\text{Arg}(z)", "=" + ARG[2], Q[2]),
               S("", r"=\pi-\tan^{-1}\left(\frac{1}{1}\right)", r"بتعويض $a=1,\ b=1$"),
               S("", r"=\pi-\frac{\pi}{4}=\frac{3\pi}{4}", SIMP)],
              r"\sqrt2", r"\frac{3\pi}{4}"),
        trig3(31, r"z=4-2i", [S("r", r"=\sqrt{4^2+(-2)^2}=\sqrt{20}=2\sqrt5", MOD)],
              [T(r"بما أنَّ العدد المركّب $z$ يقع في الربع الرابع، فإنَّ:"),
               S(r"\text{Arg}(z)", "=" + ARG[4], Q[4]),
               S("", r"=-\tan^{-1}\left(\frac{2}{4}\right)", r"بتعويض $a=4,\ b=2$"),
               S("", r"\approx-0.46", CALC)],
              r"2\sqrt5", "-0.46"),
        trig3(32, r"z=2+8i", [S("r", r"=\sqrt{2^2+8^2}=\sqrt{68}=2\sqrt{17}", MOD)],
              [T(r"بما أنَّ العدد المركّب $z$ يقع في الربع الأول، فإنَّ:"),
               S(r"\text{Arg}(z)", "=" + ARG[1], Q[1]),
               S("", r"=\tan^{-1}\left(\frac{8}{2}\right)", r"بتعويض $a=2,\ b=8$"),
               S("", r"\approx1.33", CALC)],
              r"2\sqrt{17}", "1.33"),
    ])
    pg.ans({27: r"6(\cos0+i\sin0)", 28: r"5\left(\cos(-\frac{\pi}{2})+i\sin(-\frac{\pi}{2})\right)",
            29: r"4\left(\cos(-\frac{5\pi}{6})+i\sin(-\frac{5\pi}{6})\right)", 30: r"\sqrt2\left(\cos\frac{3\pi}{4}+i\sin\frac{3\pi}{4}\right)",
            31: r"2\sqrt5\left(\cos(-0.46)+i\sin(-0.46)\right)", 32: r"2\sqrt{17}\left(\cos1.33+i\sin1.33\right)"})

    # ------------------------------------------------------------ 33–36 (trig -> standard)
    def to_std(n, q, sub_row, vals_row, res):
        return (n, q, [S(r"z", "=" + q.split("=", 1)[1] if q.startswith("z=") else q, "العدد المعطى بالصورة المثلثية"),
                       S("", vals_row, sub_row),
                       S("", "=" + res, DIST),
                       F(rf"إذن: $z={res}$")])
    pg.section("w8", "من الصورة المثلثية إلى الصورة القياسية", r"أكتب كُلًّا من الأعداد المركّبة الآتية بالصورة القياسية:", [
        (33, r"6\left(\cos\frac{\pi}{6}+i\sin\frac{\pi}{6}\right)", [
            S(r"z", r"=6\left(\cos\frac{\pi}{6}+i\sin\frac{\pi}{6}\right)", "العدد المعطى بالصورة المثلثية"),
            S("", r"=6\left(\frac{\sqrt3}{2}+\frac{1}{2}i\right)", r"$\cos\frac{\pi}{6}=\frac{\sqrt3}{2}$ ، $\sin\frac{\pi}{6}=\frac12$"),
            S("", r"=3\sqrt3+3i", DIST),
            F(r"إذن: $z=3\sqrt3+3i$")]),
        (34, r"12\left(\cos\pi+i\sin\pi\right)", [
            S(r"z", r"=12\left(\cos\pi+i\sin\pi\right)", "العدد المعطى بالصورة المثلثية"),
            S("", r"=12\left(-1+0i\right)", r"$\cos\pi=-1$ ، $\sin\pi=0$"),
            S("", r"=-12", DIST),
            F(r"إذن: $z=-12$")]),
        (35, r"8\left(\cos\frac{2\pi}{3}+i\sin\frac{2\pi}{3}\right)", [
            S(r"z", r"=8\left(\cos\frac{2\pi}{3}+i\sin\frac{2\pi}{3}\right)", "العدد المعطى بالصورة المثلثية"),
            S("", r"=8\left(-\frac{1}{2}+\frac{\sqrt3}{2}i\right)", r"$\cos\frac{2\pi}{3}=-\frac12$ ، $\sin\frac{2\pi}{3}=\frac{\sqrt3}{2}$"),
            S("", r"=-4+4i\sqrt3", DIST),
            F(r"إذن: $z=-4+4i\sqrt3$")]),
        (36, r"3\left(\cos\frac{-\pi}{4}+i\sin\frac{-\pi}{4}\right)", [
            S(r"z", r"=3\left(\cos\left(-\frac{\pi}{4}\right)+i\sin\left(-\frac{\pi}{4}\right)\right)", "العدد المعطى بالصورة المثلثية"),
            S("", r"=3\left(\frac{\sqrt2}{2}-\frac{\sqrt2}{2}i\right)", r"$\cos\left(-\frac{\pi}{4}\right)=\frac{\sqrt2}{2}$ ، $\sin\left(-\frac{\pi}{4}\right)=-\frac{\sqrt2}{2}$"),
            S("", r"=\frac{3\sqrt2}{2}-\frac{3\sqrt2}{2}i", DIST),
            F(r"إذن: $z=\dfrac{3\sqrt2}{2}-\dfrac{3\sqrt2}{2}i$")]),
    ])
    pg.ans({33: r"3\sqrt3+3i", 34: "-12", 35: r"-4+4i\sqrt3", 36: r"\frac{3\sqrt2}{2}-\frac{3\sqrt2}{2}i"})

    # ------------------------------------------------------------ 37–42 conjugates, one plane
    cj = [(37, r"-1-i\sqrt5", r"-1+i\sqrt5", -1, -math.sqrt(5)), (38, "9-i", "9+i", 9, -1), (39, "2-8i", "2+8i", 2, -8),
          (40, "-9i", "9i", 0, -9), (41, "12", "12", 12, 0), (42, "i-8", "-8-i", -8, 1)]
    items = []
    exs = []
    for n, z, zb, x, y in cj:
        items.append(("pt", x, y, f"z{n}", {"c": BLUE, "dx": 5, "dy": -5}))
        if y != 0:
            items.append(("pt", x, -y, f"z̄{n}", {"c": GREEN, "dx": 5, "dy": 13}))
        extra = ""
        if n == 42:
            extra = r"أكتب العدد أولًا بالصورة القياسية: $z=i-8=-8+i$. "
        if n == 41:
            body = [T(r"$z=12=12+0i$ ، إذن مُرافِقه: $\bar z=12-0i=12$؛ فالعدد الحقيقي مُرافِق لنفسه، ويُمثِّل الزوج المرتّب $(12,\,0)$ كلًّا منهما.")]
        else:
            body = [T(extra + rf"مُرافِق العدد المركّب $z={z if n != 42 else '-8+i'}$ هو: $\bar z={zb}$."),
                    T(rf"يُمثِّل الزوج المرتّب $({x if not isinstance(x, float) else '-1'},\,{y if not isinstance(y, float) else '-\\sqrt5'})$ العدد $z$، "
                      rf"ويُمثِّل الزوج المرتّب $({x if not isinstance(x, float) else '-1'},\,{-y if not isinstance(y, float) else '\\sqrt5'})$ مُرافِقه $\bar z$.")]
        exs.append((n, "z=" + z, body))
    f = cplane("w37-42.svg", (-10, 13), (-10, 10), items, unit=16)
    pg.section("w9", "مُرافِق العدد المركّب", r"أجد مُرافِق كلٍّ من الأعداد المركّبة الآتية، ثمَّ أُمثِّلها جميعًا في المستوى المركّب نفسه:", exs,
               after=[T(r"التمثيل البياني للأعداد (باللون الأزرق) ومُرافِقاتها (باللون الأخضر) في المستوى المركّب نفسه؛ كل مُرافِق هو انعكاس العدد في المحور الحقيقي:"), FIG(f)])
    pg.ans({37: r"-1+i\sqrt5", 38: "9+i", 39: "2+8i", 40: "9i", 41: "12", 42: "-8-i"})
