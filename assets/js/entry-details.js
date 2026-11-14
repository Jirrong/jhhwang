// Native <details> handles disclosure; only reflow optional equations on opening.
(() => {
  'use strict';
  document.querySelectorAll('.abstract-disclosure').forEach(detail => {
    detail.addEventListener('toggle', () => {
      const math = window.MathJax;
      if (!detail.open || !math || !math.startup || !math.typesetPromise) return;
      math.startup.promise.then(() => math.typesetPromise([detail])).catch(() => {});
    });
  });
})();
