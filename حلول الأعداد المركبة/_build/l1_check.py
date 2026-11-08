# -*- coding: utf-8 -*-
"""Lesson 1 – أتحقّق من فهمي (book pages 151–162)."""
import math
from lib import *


def build(pg):
    pg.section("c1", "مثال 1: الجذر الرئيس بدلالة $i$", r"أجد قيمة الجذر الرئيس في كلٍّ ممّا يأتي بدلالة $i$:", [
        ("a", r"\sqrt{-75}", [
            S(r"\sqrt{-75}", r"=\sqrt{-1\times25\times3}", ANAL),
            S("", r"=\sqrt{-1}\times\sqrt{25}\times\sqrt{3}", MULT),
            S("", r"=i\times5\times\sqrt{3}=5i\sqrt{3}", ROOT_I),
            F(r"إذن: $\sqrt{-75}=5i\sqrt3$")]),
        ("b", r"\sqrt{-49}", [
            S(r"\sqrt{-49}", r"=\sqrt{-1\times49}", ANAL),
            S("", r"=\sqrt{-1}\times\sqrt{49}", MULT),
            S("", r"=i\times7=7i", ROOT_I),
            F(r"إذن: $\sqrt{-49}=7i$")]),
    ])

    pg.section("c2", "مثال 2: الضرب وقوى $i$", r"أجد ناتج كلٍّ ممّا يأتي في أبسط صورة بافتراض أنَّ $\sqrt{-1}=i$:", [
        ("a", r"\sqrt{-27}\times\sqrt{-48}", [
            S(r"\sqrt{-27}\times\sqrt{-48}", r"=\sqrt{-1\times27}\times\sqrt{-1\times48}", ANAL),
            S("", r"=(\sqrt{-1}\times\sqrt{27})\times(\sqrt{-1}\times\sqrt{48})", MULT),
            S("", r"=(i\times\sqrt{27})\times(i\times\sqrt{48})", DEF_I),
            S("", r"=(i\times i)\times(\sqrt{27}\times\sqrt{48})", COMM),
            S("", r"=i^2\times\sqrt{1296}", MULT),
            S("", r"=-1\times36=-36", I2),
            F(r"إذن: $\sqrt{-27}\times\sqrt{-48}=-36$")]),
        ("b", r"\sqrt{-50}\times-4i", [
            S(r"\sqrt{-50}\times-4i", r"=\sqrt{-1\times25\times2}\times-4i", ANAL),
            S("", r"=\sqrt{-1}\times\sqrt{25}\times\sqrt{2}\times-4i", MULT),
            S("", r"=i\times5\times\sqrt{2}\times-4i", DEF_I),
            S("", r"=(5\times-4)\times(i\times i)\times\sqrt{2}", "خاصيتا التبديل والتجميع"),
            S("", r"=-20\,i^2\sqrt{2}", "بالضرب"),
            S("", r"=-20\times-1\times\sqrt2=20\sqrt{2}", I2),
            F(r"إذن: $\sqrt{-50}\times-4i=20\sqrt2$")]),
        ("c", r"i^{2021}", [
            S(r"i^{2021}", r"=(i^2)^{1010}\times i", "خاصية قوّة القوّة"),
            S("", r"=(-1)^{1010}\times i", r"بالتبسيط: $i^2=-1$"),
            S("", r"=i", r"بالتبسيط: $(-1)^{1010}=1$"),
            F(r"إذن: $i^{2021}=i$")]),
    ])

    pg.section("c3", "مثال 3: تساوي الأعداد المركّبة",
               r"أجد قيمة $x$ وقيمة $y$ الحقيقيتين اللتين تجعلان المعادلة: $x+5+(4y-9)i=12-5i$ صحيحة.", [
        ("", "", [
            T("أُساوي الجزأين الحقيقيين، وأُساوي الجزأين التخيّليين، ثمَّ أحُلُّ المعادلتين الناتجتين:"),
            S(r"x+5", r"=12", "بمساواة الجزأين الحقيقيين"),
            S(r"x", r"=7", "بحلّ المعادلة"),
            S(r"4y-9", r"=-5", "بمساواة الجزأين التخيّليين"),
            S(r"4y", r"=4", r"بجمع $9$ للطرفين"),
            S(r"y", r"=1", "بحلّ المعادلة"),
            F(r"إذن: $x=7,\ y=1$")]),
    ])

    def conj(n, z, zb, pz, pzb, x, y):
        f = plot(f"c4{n}.svg", [P(x, y, "z = " + pretty(z), BLUE), P(x, -y, "z̄ = " + pretty(zb), GREEN)])
        return (n, "z=" + z, [
            T(rf"مُرافِق العدد المركّب: $z={z}$ هو: $\bar z={zb}$."),
            T(rf"يُمثِّل الزوج المرتّب ${pz}$ العدد المركّب $z$، ويُمثِّل الزوج المرتّب ${pzb}$ مُرافِقه $\bar z$."),
            FIG(f)])
    pg.section("c4", "مثال 4: تمثيل العدد المركّب ومرافقه", r"أُمثِّل العدد المركّب ومُرافِقه بيانيًّا في المستوى المركّب في كلٍّ ممّا يأتي:", [
        conj("a", "2+7i", "2-7i", r"(2,\,7)", r"(2,\,-7)", 2, 7),
        conj("b", "-3-2i", "-3+2i", r"(-3,\,-2)", r"(-3,\,2)", -3, -2),
        conj("c", "-3i", "3i", r"(0,\,-3)", r"(0,\,3)", 0, -3),
    ])

    pg.section("c5", "مثال 5: مقياس العدد المركّب", r"أجد مقياس كل عدد مركّب ممّا يأتي:", [
        ("a", r"z=-3-6i\sqrt{2}", [
            S(r"|z|", r"=\sqrt{a^2+b^2}", MOD),
            S("", r"=\sqrt{(-3)^2+(-6\sqrt2)^2}", r"بتعويض $a=-3,\ b=-6\sqrt2$"),
            S("", r"=\sqrt{9+72}=\sqrt{81}=9", SIMP),
            F(r"إذن: $|z|=9$")]),
        ("b", r"z=-2i", [
            S(r"|z|", r"=\sqrt{a^2+b^2}", MOD),
            S("", r"=\sqrt{0^2+(-2)^2}", r"بتعويض $a=0,\ b=-2$"),
            S("", r"=\sqrt{4}=2", SIMP),
            F(r"إذن: $|z|=2$")]),
        ("c", r"z=4+\sqrt{-20}", [
            S(r"z", r"=4+\sqrt{-1\times4\times5}=4+2i\sqrt5", "بكتابة العدد بالصورة القياسية"),
            S(r"|z|", r"=\sqrt{a^2+b^2}", MOD),
            S("", r"=\sqrt{4^2+(2\sqrt5)^2}", r"بتعويض $a=4,\ b=2\sqrt5$"),
            S("", r"=\sqrt{16+20}=\sqrt{36}=6", SIMP),
            F(r"إذن: $|z|=6$")]),
    ])

    def arg(n, z, q, a, b, frac, approx, x, y, exact=None, lab=None, yl=None):
        kw = {"yl": yl} if yl else {}
        f = plot(f"c6{n}.svg", [P(x, y, lab or ("z = " + pretty(z)), BLUE, **kw)], arc=True)
        body = [T(rf"بالنظر إلى التمثيل البياني للعدد المركّب: $z={z}$ في الشكل المجاور، أُلاحِظ أنَّه يقع في الربع {QN[q]}."),
                S(r"\text{Arg}(z)", "=" + ARG[q], Q[q]),
                S("", "=" + ARG[q].replace(r"\frac{b}{a}", frac), rf"بتعويض $a={a},\ b={b}$")]
        if exact:
            body.append(S("", "=" + exact, "بالتبسيط"))
        body += [S("", r"\approx " + approx, CALC), F(rf"إذن: $\text{{Arg}}(z)\approx {approx}$"), FIG(f)]
        return (n, "z=" + z, body)
    pg.section("c6", "مثال 6: سعة العدد المركّب", r"أجد سعة كلٍّ من الأعداد المركّبة الآتية، وأُقرِّب إجابتي إلى أقرب منزلتين عشريتين:", [
        arg("a", "8+2i", 1, 8, 2, r"\frac{2}{8}", "0.24", 8, 2),
        arg("b", "-5+12i", 2, 5, 12, r"\frac{12}{5}", "1.97", -5, 12),
        arg("c", "-2-3i", 3, 2, 3, r"\frac{3}{2}", "-2.16", -2, -3),
        arg("d", r"8-8i\sqrt3", 4, 8, r"8\sqrt3", r"\frac{8\sqrt3}{8}", "-1.05", 8, -8 * math.sqrt(3),
            exact=r"-\tan^{-1}(\sqrt3)=-\frac{\pi}{3}", lab="z = 8 − 8i√3", yl="−8√3"),
    ])

    pg.section("c7", "مثال 7: الصورة المثلثية", r"أكتب العدد المركّب $z$ في كلٍّ ممّا يأتي بالصورة المثلثية:", [
        ("a", r"|z|=4\sqrt2,\ \text{Arg}(z)=-\frac{3\pi}{4}", [
            S(r"z", r"=r(\cos\theta+i\sin\theta)", TRIG),
            S("", r"=4\sqrt2\left(\cos\left(-\frac{3\pi}{4}\right)+i\sin\left(-\frac{3\pi}{4}\right)\right)", r"بتعويض $r=4\sqrt2,\ \theta=-\frac{3\pi}{4}$"),
            F(r"إذن، الصورة المثلثية للعدد المركّب $z$ هي: $z=4\sqrt2\left(\cos\left(-\frac{3\pi}{4}\right)+i\sin\left(-\frac{3\pi}{4}\right)\right)$")]),
        ("b", r"z=-4-4i", [
            STEP(r"الخطوة 1: أجد مقياس العدد المركّب $z$."),
            S(r"r", r"=\sqrt{(-4)^2+(-4)^2}=\sqrt{32}=4\sqrt2", MOD),
            STEP(r"الخطوة 2: أجد سعة العدد المركّب $z$."),
            T(r"بما أنَّ العدد المركّب $z$ يقع في الربع الثالث، فإنَّ:"),
            S(r"\text{Arg}(z)", r"=-\left(\pi-\tan^{-1}\left(\frac{b}{a}\right)\right)", Q[3]),
            S("", r"=-\left(\pi-\tan^{-1}\left(\frac{4}{4}\right)\right)", r"بتعويض $a=4,\ b=4$"),
            S("", r"=-\left(\pi-\frac{\pi}{4}\right)=-\frac{3\pi}{4}", SIMP),
            STEP(r"الخطوة 3: أكتب العدد المركّب $z$ بالصورة المثلثية."),
            S(r"z", r"=4\sqrt2\left(\cos\left(-\frac{3\pi}{4}\right)+i\sin\left(-\frac{3\pi}{4}\right)\right)", r"بتعويض $r=4\sqrt2,\ \theta=-\frac{3\pi}{4}$"),
            F(r"إذن: $z=4\sqrt2\left(\cos\left(-\frac{3\pi}{4}\right)+i\sin\left(-\frac{3\pi}{4}\right)\right)$")]),
        ("c", r"z=2i", [
            STEP(r"الخطوة 1: أجد مقياس العدد المركّب $z$."),
            S(r"r", r"=\sqrt{0^2+2^2}=2", MOD),
            STEP(r"الخطوة 2: أجد سعة العدد المركّب $z$."),
            T(r"العدد $z=2i$ يقع على الجزء الموجب من المحور التخيّلي، إذن: $\text{Arg}(z)=\dfrac{\pi}{2}$."),
            STEP(r"الخطوة 3: أكتب العدد المركّب $z$ بالصورة المثلثية."),
            S(r"z", r"=2\left(\cos\frac{\pi}{2}+i\sin\frac{\pi}{2}\right)", r"بتعويض $r=2,\ \theta=\frac{\pi}{2}$"),
            F(r"إذن: $z=2\left(\cos\frac{\pi}{2}+i\sin\frac{\pi}{2}\right)$")]),
    ])
