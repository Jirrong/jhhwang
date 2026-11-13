(() => {
  'use strict';
  const content = document.getElementById('post-content');
  if (!content) return;
  const toc = document.querySelector('.table-of-contents');
  const tocLinks = document.getElementById('toc-links');
  const headings = [...content.querySelectorAll('h2, h3')];
  if (toc && tocLinks && headings.length > 1) {
    const used = new Set([...document.querySelectorAll('[id]')].map(node => node.id));
    headings.forEach((heading, index) => {
      if (!heading.id) { let id = `section-${index + 1}`; while (used.has(id)) id += '-x'; heading.id = id; used.add(id); }
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.href = `#${encodeURIComponent(heading.id)}`;
      link.textContent = heading.textContent;
      item.append(link); tocLinks.append(item);
    });
    toc.hidden = false;
    const layout = content.closest('.notebook-layout');
    if (layout) layout.classList.add('has-toc');
  }
  content.querySelectorAll('pre').forEach(pre => {
    const code = pre.querySelector('code');
    if (!code) return;
    const controls = document.createElement('p');
    const button = document.createElement('button');
    button.type = 'button'; button.className = 'btn btn-default btn-xs copy-code'; button.textContent = 'Copy code';
    const status = document.createElement('span'); status.className = 'sr-only'; status.setAttribute('role', 'status');
    button.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(code.textContent); button.textContent = 'Copied!'; status.textContent = 'Code copied.'; }
      catch (_) { const range = document.createRange(); range.selectNodeContents(code); const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range); status.textContent = 'Code selected. Press Ctrl+C or Command+C to copy.'; }
      setTimeout(() => { button.textContent = 'Copy code'; status.textContent = ''; }, 3000);
    });
    controls.append(button, status); pre.insertAdjacentElement('afterend', controls);
  });
})();
