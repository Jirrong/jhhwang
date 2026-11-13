(() => {
  'use strict';
  const button = document.getElementById('print-cv');
  if (!button) return;
  button.hidden = false;
  button.addEventListener('click', () => window.print());
})();
