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
      const link = document.createElement('a');
      link.href = `#${encodeURIComponent(heading.id)}`;
      link.textContent = heading.textContent;
      if (heading.tagName === 'H3') link.classList.add('toc-sub');
      tocLinks.append(link);
    });
    toc.hidden = false;
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(entries => {
        const visible = entries.find(entry => entry.isIntersecting);
        if (!visible) return;
        tocLinks.querySelectorAll('a').forEach(link => {
          const active = decodeURIComponent(link.hash.slice(1)) === visible.target.id;
          active ? link.setAttribute('aria-current', 'location') : link.removeAttribute('aria-current');
        });
      }, { rootMargin: '-100px 0px -60% 0px' });
      headings.forEach(heading => observer.observe(heading));
    }
  }
  const bar = document.getElementById('reading-progress-bar');
  if (bar) {
    let ticking = false;
    const update = () => {
      const start = content.getBoundingClientRect().top + window.scrollY - 130;
      const distance = Math.max(1, content.offsetHeight - window.innerHeight + 180);
      bar.style.width = `${Math.min(100, Math.max(0, ((window.scrollY - start) / distance) * 100))}%`;
      ticking = false;
    };
    window.addEventListener('scroll', () => { if (!ticking) { requestAnimationFrame(update); ticking = true; } }, { passive: true });
    window.addEventListener('resize', update);
    update();
  }
  content.querySelectorAll('pre').forEach(pre => {
    const code = pre.querySelector('code');
    if (!code) return;
    const button = document.createElement('button');
    button.type = 'button'; button.className = 'copy-code'; button.textContent = 'Copy code';
    const status = document.createElement('span'); status.className = 'code-status'; status.setAttribute('role', 'status');
    button.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(code.textContent); button.textContent = 'Copied!'; status.textContent = '코드를 복사했습니다.'; }
      catch (_) { const range = document.createRange(); range.selectNodeContents(code); const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range); status.textContent = '코드를 선택했습니다. Ctrl+C 또는 ⌘C로 복사하세요.'; }
      setTimeout(() => { button.textContent = 'Copy code'; status.textContent = ''; }, 3000);
    });
    pre.append(button); pre.insertAdjacentElement('afterend', status);
  });
})();
