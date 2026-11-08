# -*- coding: utf-8 -*-
"""Hub page of the unit."""
import os

CARDS = [
    ("prep.html", "أستعدّ لدراسة الوحدة", "كتاب التمارين ص 38–39", "حلّ معادلات كثيرات الحدود، المتجهات، معادلة الدائرة (1–6)."),
    ("lesson1.html", "الدرس 1: الأعداد المركّبة", "كتاب الطالب ص 150–164 · كتاب التمارين ص 40–41",
     "الجذر الرئيس، قوى $i$، التساوي، التمثيل والمُرافِق، المقياس، السعة، الصورة المثلثية."),
    ("lesson2.html", "الدرس 2: العمليات على الأعداد المركّبة", "كتاب الطالب ص 165–177 · كتاب التمارين ص 42–43",
     "الجمع والطرح والضرب والقسمة، الصورة المثلثية، الجذور التربيعية، جذور كثيرات الحدود."),
    ("lesson3.html", "الدرس 3: المحل الهندسي في المستوى المركّب", "كتاب الطالب ص 178–189 · كتاب التمارين ص 44–45",
     "الدائرة، المُنصِّف العمودي، الشعاع، تمثيل المتباينات وأنظمتها."),
    ("test.html", "اختبار نهاية الوحدة", "كتاب الطالب ص 190–191", "حلول الأسئلة (1–27)."),
]

def write(out, nav):
    cards = "".join(
        f'<a class="card" href="{h}"><h2>{t}</h2><div class="card-src">{src}</div><p>{d}</p></a>' for h, t, src, d in CARDS)
    nav_html = " ".join((f'<a class="cur" href="{h}">{l}</a>' if h == "index.html" else f'<a href="{h}">{l}</a>') for h, l in nav)
    page = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>وحدة الأعداد المركّبة – حلول بأسلوب الكتاب</title>
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
      <div class="kicker">الرياضيات · الصف الثاني عشر · المسار الأكاديمي · الفصل الدراسي الأول</div>
      <h1>الوحدة 4: الأعداد المركّبة <span class="en">Complex Numbers</span></h1>
      <div class="sub">حلول جميع المسائل غير المحلولة في الوحدة، بطريقة الكتاب المدرسي نفسها</div>
    </div>
    <div class="author">Homam Alkrad<br><span dir="ltr">0791089960</span></div>
  </div>
  <nav class="pages">{nav_html}</nav>
</header>
<main>
<section class="sec intro">
  <p>يحتوي كل درس على ثلاثة أجزاء: <b>أتحقّق من فهمي</b>، و<b>أتدرّب وأحلّ المسائل</b>، و<b>كتاب التمارين</b>.
  وفي أول صفحة كل درس جدول بعنوان «طريقة الكتاب» يلخّص الخطوات التي تعتمدها الأمثلة المحلولة، وعلى هذه الخطوات بُني كل حل:
  كل خطوة في سطر مستقل وبجانبها سببها، ويُختم الحل بعبارة «إذن».</p>
</section>
<div class="cards">{cards}</div>
</main>
<footer class="foot">Homam Alkrad · <span dir="ltr">0791089960</span></footer>
</body>
</html>
"""
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
