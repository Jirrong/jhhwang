(() => {
  'use strict';
  const link = document.getElementById('cv-download-link');
  if (link && link.hasAttribute('download')) link.click();
})();
