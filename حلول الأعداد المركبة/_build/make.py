# -*- coding: utf-8 -*-
"""Build all pages of the complex-numbers unit.

    python make.py            -> writes the pages into the parent folder
"""
import os, sys, shutil, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib

OUT = os.path.dirname(HERE)
lib.OUT = OUT

NAV = [("index.html", "الرئيسية"), ("prep.html", "أستعدّ"), ("lesson1.html", "الدرس 1"), ("lesson2.html", "الدرس 2"),
       ("lesson3.html", "الدرس 3"), ("test.html", "اختبار الوحدة")]

PAGES = []

def page_lesson1():
    import l1_check, l1_ex, l1_wb, methods
    pg = lib.Page("lesson1", "الوحدة 4 · الدرس 1 · كتاب الطالب ص 150–164 · كتاب التمارين ص 40–41",
                  "الأعداد المركّبة", "Complex Numbers",
                  "حلول «أتحقّق من فهمي» و«أتدرّب وأحلّ المسائل» وأسئلة كتاب التمارين بأسلوب الكتاب")
    pg.method(methods.L1)
    pg.part("check", "أتحقّق من فهمي", "أسئلة «أتحقّق من فهمي» التي تلي كل مثال في الدرس، محلولة بخطوات المثال نفسه.")
    l1_check.build(pg)
    pg.part("ex", "أتدرّب وأحلّ المسائل (1–60)", "كتاب الطالب، الصفحات 162–164.")
    l1_ex.build(pg)
    pg.part("wb", "كتاب التمارين (1–42)", "كتاب التمارين، الصفحتان 40–41.")
    l1_wb.build(pg)
    return pg

def page_lesson2():
    import l2_check, l2_ex, l2_wb, methods
    pg = lib.Page("lesson2", "الوحدة 4 · الدرس 2 · كتاب الطالب ص 165–177 · كتاب التمارين ص 42–43",
                  "العمليات على الأعداد المركّبة", "Operations with Complex Numbers",
                  "حلول «أتحقّق من فهمي» و«أتدرّب وأحلّ المسائل» وأسئلة كتاب التمارين بأسلوب الكتاب")
    pg.method(methods.L2)
    pg.part("check", "أتحقّق من فهمي", "أسئلة «أتحقّق من فهمي» التي تلي كل مثال في الدرس، محلولة بخطوات المثال نفسه.")
    l2_check.build(pg)
    pg.part("ex", "أتدرّب وأحلّ المسائل (1–53)", "كتاب الطالب، الصفحات 175–177.")
    l2_ex.build(pg)
    pg.part("wb", "كتاب التمارين (1–32)", "كتاب التمارين، الصفحتان 42–43.")
    l2_wb.build(pg)
    return pg

def page_lesson3():
    import l3_check, l3_ex, l3_wb, methods
    pg = lib.Page("lesson3", "الوحدة 4 · الدرس 3 · كتاب الطالب ص 178–189 · كتاب التمارين ص 44–45",
                  "المحل الهندسي في المستوى المركّب", "Locus in the Complex Plane",
                  "حلول «أتحقّق من فهمي» و«أتدرّب وأحلّ المسائل» وأسئلة كتاب التمارين بأسلوب الكتاب")
    pg.method(methods.L3)
    pg.part("check", "أتحقّق من فهمي", "أسئلة «أتحقّق من فهمي» التي تلي كل مثال في الدرس، محلولة بخطوات المثال نفسه.")
    l3_check.build(pg)
    pg.part("ex", "أتدرّب وأحلّ المسائل (1–36)", "كتاب الطالب، الصفحات 187–189.")
    l3_ex.build(pg)
    pg.part("wb", "كتاب التمارين (1–22)", "كتاب التمارين، الصفحتان 44–45.")
    l3_wb.build(pg)
    return pg

def page_test():
    import u_test
    pg = lib.Page("test", "الوحدة 4 · كتاب الطالب ص 190–191", "اختبار نهاية الوحدة", "Unit Test",
                  "حلول أسئلة اختبار نهاية الوحدة (1–27) بأسلوب الكتاب")
    pg.part("t", "اختبار نهاية الوحدة (1–27)")
    u_test.build(pg)
    return pg

def page_prep():
    import prep
    pg = lib.Page("prep", "الوحدة 4 · كتاب التمارين ص 38–39", "أستعدّ لدراسة الوحدة", "Unit Readiness",
                  "حلول تدريبات «أستعدّ لدراسة الوحدة» (1–6) بأسلوب الأمثلة المحلولة")
    pg.part("p", "أستعدّ لدراسة الوحدة (1–6)")
    prep.build(pg)
    return pg

BUILDERS = {"lesson1": page_lesson1, "lesson2": page_lesson2, "lesson3": page_lesson3, "test": page_test, "prep": page_prep}

if __name__ == "__main__":
    which = sys.argv[1:] or list(BUILDERS)
    os.makedirs(os.path.join(OUT, "css"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "js"), exist_ok=True)
    shutil.copy(os.path.join(HERE, "style.css"), os.path.join(OUT, "css", "style.css"))
    shutil.copy(os.path.join(HERE, "main.js"), os.path.join(OUT, "js", "main.js"))
    for w in which:
        if w == "index":
            continue
        pg = BUILDERS[w]()
        n = pg.write(NAV)
        print(w, "ok", n)
    import index
    index.write(OUT, NAV)
    print("index ok")
