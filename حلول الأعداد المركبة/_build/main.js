// تحويل الرموز الرياضية المكتوبة بين $...$ إلى صيغ رياضية باستعمال KaTeX
document.addEventListener("DOMContentLoaded", function () {
  if (typeof renderMathInElement !== "function") return;
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false }
    ],
    throwOnError: false
  });
});
