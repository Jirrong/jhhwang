(() => {
  'use strict';
  const tools = document.getElementById('blog-tools');
  if (!tools) return;
  const input = document.getElementById('blog-search');
  const rows = [...document.querySelectorAll('#post-list .note-row')];
  const chips = [...document.querySelectorAll('.filter-chip')];
  const status = document.getElementById('search-status');
  const empty = document.getElementById('no-results');
  const normal = value => String(value || '').normalize('NFKC').toLocaleLowerCase();
  const searchText = new Map(rows.map(row => [row, normal(row.dataset.search)]));
  const tags = new Map(rows.map(row => { try { return [row, JSON.parse(row.dataset.tags)]; } catch (_) { return [row, []]; } }));
  let activeTag = '';
  let fullIndex = false;
  let indexFailed = false;
  tools.hidden = false;
  const syncFromURL = () => {
    const params = new URLSearchParams(location.search);
    input.value = params.get('q') || '';
    activeTag = params.get('tag') || '';
  };
  function filter(updateURL = true) {
    const terms = normal(input.value).trim().split(/\s+/).filter(Boolean);
    let count = 0;
    rows.forEach(row => {
      const text = searchText.get(row);
      const matches = (!activeTag || tags.get(row).includes(activeTag)) && terms.every(term => text.includes(term));
      row.hidden = !matches;
      if (matches) count += 1;
    });
    chips.forEach(chip => {
      const active = chip.dataset.tag === activeTag;
      chip.setAttribute('aria-pressed', String(active));
      chip.classList.toggle('btn-primary', active);
      chip.classList.toggle('btn-default', !active);
    });
    status.textContent = `${count}개의 노트${activeTag ? ` · ${activeTag}` : ''}${terms.length ? (fullIndex ? ' · 본문까지 검색' : indexFailed ? ' · 제목·설명·태그 검색' : ' · 본문 검색 준비 중') : ''}`;
    empty.hidden = count !== 0;
    if (updateURL) {
      const url = new URL(location.href);
      input.value.trim() ? url.searchParams.set('q', input.value.trim()) : url.searchParams.delete('q');
      activeTag ? url.searchParams.set('tag', activeTag) : url.searchParams.delete('tag');
      history.replaceState(null, '', url);
    }
  }
  function reset() { input.value = ''; activeTag = ''; filter(); input.focus(); }
  document.getElementById('blog-search-form').addEventListener('submit', event => { event.preventDefault(); filter(); });
  input.addEventListener('input', () => filter());
  chips.forEach(chip => chip.addEventListener('click', () => { activeTag = chip.dataset.tag; filter(); }));
  document.getElementById('clear-search').addEventListener('click', reset);
  document.getElementById('reset-filters').addEventListener('click', reset);
  window.addEventListener('popstate', () => { syncFromURL(); filter(false); });
  syncFromURL(); filter(false);
  fetch(tools.dataset.indexUrl).then(response => { if (!response.ok) throw new Error('Search index unavailable'); return response.json(); }).then(posts => {
    const byURL = new Map(posts.map(post => [post.url, post]));
    rows.forEach(row => {
      const post = byURL.get(row.dataset.postUrl);
      if (post) searchText.set(row, normal([post.title, post.description, post.content, ...(post.tags || [])].join(' ')));
    });
    fullIndex = true;
    filter(false);
  }).catch(() => { indexFailed = true; filter(false); });
})();
