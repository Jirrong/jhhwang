const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const { parseHTML } = require('linkedom');
const source = name => fs.readFileSync(`assets/js/${name}.js`, 'utf8');
const settle = () => new Promise(resolve => setImmediate(resolve));

function setupSearch(search = '', failIndex = false) {
  const { document } = parseHTML(fs.readFileSync('_site/blog/index.html', 'utf8'));
  const list = document.getElementById('post-list'); list.replaceChildren();
  const records = [
    { title: '분자와 계산', url: '/jhhwang/blog/molecules/', tags: ['화학', '계산'], description: '첫 번째 노트', content: '본문에만 있는 전이상태 기저함수 이야기' },
    { title: '논문 읽기', url: '/jhhwang/blog/papers/', tags: ['화학'], description: '두 번째 노트', content: '촉매와 선택성' },
    { title: '코드 노트', url: '/jhhwang/blog/code/', tags: ['Python & C++'], description: '세 번째 노트', content: '파이썬' }
  ];
  for (const record of records) {
    const row = document.createElement('article');
    row.className = 'note-row'; row.dataset.postUrl = record.url;
    row.dataset.search = `${record.title} ${record.description} ${record.tags.join(' ')}`;
    row.dataset.tags = JSON.stringify(record.tags); list.append(row);
  }
  const filters = document.querySelector('.filter-row'); filters.replaceChildren();
  for (const tag of ['', '화학', '계산', 'Python & C++']) {
    const chip = document.createElement('button'); chip.className = 'filter-chip'; chip.dataset.tag = tag; chip.textContent = tag || 'All'; filters.append(chip);
  }
  const location = new URL(`https://jirrong.github.io/jhhwang/blog/${search}`);
  const events = {};
  const ctx = { document, location, URL, URLSearchParams,
    history: { replaceState: (_state, _title, url) => { location.href = url.href; } },
    window: { addEventListener: (type, handler) => { events[type] = handler; } },
    fetch: async () => failIndex ? { ok: false } : { ok: true, json: async () => records }
  };
  vm.runInNewContext(source('blog'), ctx);
  return { document, location, events, visible: () => [...document.querySelectorAll('.note-row')].filter(row => !row.hidden).map(row => row.dataset.postUrl) };
}

test('search starts from a shared Korean tag + full-text query URL', async () => {
  const p = setupSearch('?tag=%ED%99%94%ED%95%99&q=%EC%A0%84%EC%9D%B4%EC%83%81%ED%83%9C'); await settle();
  assert.deepEqual(p.visible(), ['/jhhwang/blog/molecules/']);
  assert.match(p.document.getElementById('search-status').textContent, /Full-text search/);
  assert.equal(p.document.querySelector('[data-tag="화학"]').getAttribute('aria-pressed'), 'true');
});

test('tags containing spaces, ampersands, and plus signs survive URL round trips', async () => {
  const p = setupSearch('?tag=Python+%26+C%2B%2B'); await settle();
  assert.deepEqual(p.visible(), ['/jhhwang/blog/code/']);
  p.document.querySelector('[data-tag="Python & C++"]').click();
  assert.equal(p.location.searchParams.get('tag'), 'Python & C++');
});

test('no matches exposes an accessible empty state; reset restores all posts', async () => {
  const p = setupSearch('?q=not-found'); await settle();
  assert.equal(p.visible().length, 0);
  assert.equal(p.document.getElementById('no-results').hidden, false);
  p.document.getElementById('reset-filters').click();
  assert.equal(p.visible().length, 3);
  assert.equal(p.location.search, '');
  assert.equal(p.document.getElementById('no-results').hidden, true);
});

test('failed full-text download preserves title/tag search and reports its scope', async () => {
  const p = setupSearch('?q=분자', true); await settle();
  assert.deepEqual(p.visible(), ['/jhhwang/blog/molecules/']);
  assert.match(p.document.getElementById('search-status').textContent, /Searching titles, descriptions, and tags/);
});

test('browser back/forward re-reads the current query and selected tag', async () => {
  const p = setupSearch(); await settle();
  p.location.search = '?tag=계산'; p.events.popstate();
  assert.deepEqual(p.visible(), ['/jhhwang/blog/molecules/']);
  p.location.search = ''; p.events.popstate(); assert.equal(p.visible().length, 3);
});

test('all post links and navigation remain available before JavaScript', () => {
  const { document } = parseHTML(fs.readFileSync('_site/blog/index.html', 'utf8'));
  assert.ok(document.querySelector('#post-list .note-row h3 a'));
  assert.ok(document.querySelector('#navbar-collapse-1 a'));
  assert.equal(document.getElementById('blog-tools').hidden, true);
  assert.ok(document.querySelector('.navbar-toggle'));
  assert.equal(document.querySelector('link[href*="academic.css"]'), null);
});

test('original design files match the baseline exactly', () => {
  const { execFileSync } = require('node:child_process');
  const result = execFileSync('python3', ['scripts/check_template.py'], { encoding: 'utf8' });
  assert.match(result, /92 original design files/);
});

test('new post shortcut pre-fills a valid filename and Markdown using the Seoul date', () => {
  const { document } = parseHTML(fs.readFileSync('_site/writing/index.html', 'utf8'));
  class FixedDate extends Date { constructor(...args) { super(...(args.length ? args : ['2026-11-12T16:30:00Z'])); } }
  vm.runInNewContext(source('site'), { document, URL, Intl, Date: FixedDate });
  const url = new URL(document.getElementById('new-post-link').getAttribute('href'));
  assert.equal(url.hostname, 'github.com');
  assert.equal(url.pathname, '/Jirrong/jhhwang/new/gh-pages/_posts');
  assert.equal(url.searchParams.get('filename'), '2026-11-13-your-title.md');
  assert.match(url.searchParams.get('value'), /^---\ntitle: "Post title"\ndate: 2026-11-13 00:00:00 \+0900/);
  assert.match(url.searchParams.get('value'), /## References/);
});

test('post tools create a table of contents and copy only code text', async () => {
  const { document } = parseHTML('<html><body><div id="post-content"><h2 id="question">질문</h2><h3>분석</h3><pre><code>print("hello")\n</code></pre></div><aside class="table-of-contents" hidden><nav id="toc-links"></nav></aside></body></html>');
  let copied = '';
  vm.runInNewContext(source('post'), { document, window: {}, navigator: { clipboard: { writeText: async text => { copied = text; } } }, setTimeout: () => {} });
  assert.equal(document.querySelector('.table-of-contents').hidden, false);
  assert.equal(document.querySelectorAll('#toc-links a').length, 2);
  document.querySelector('.copy-code').click(); await settle();
  assert.equal(copied, 'print("hello")\n');
  assert.match(document.querySelector('[role="status"]').textContent, /Code copied/);
});

test('CV print control opens printing without adding a screen-theme override', () => {
  const { document } = parseHTML(fs.readFileSync('_site/cv/index.html', 'utf8'));
  let printed = 0;
  vm.runInNewContext(source('cv'), { document, window: { print: () => { printed += 1; } } });
  const button = document.getElementById('print-cv');
  assert.equal(button.hidden, false);
  button.click(); assert.equal(printed, 1);
  assert.equal(document.querySelector('link[href$="cv-print.css"]').getAttribute('media'), 'print');
  assert.equal(document.querySelector('a[href="#"]'), null);
  assert.ok(document.getElementById('education'));
  assert.ok(document.getElementById('presentations'));
});

test('blog controls and writing template use English by default', () => {
  const { document } = parseHTML(fs.readFileSync('_site/blog/index.html', 'utf8'));
  assert.equal(document.querySelector('label[for="blog-search"]').textContent, 'Search posts');
  assert.equal(document.getElementById('clear-search').textContent, 'Reset');
  assert.match(document.getElementById('no-results').textContent, /No posts found/);
  assert.match(fs.readFileSync('_drafts/academic-post-template.md', 'utf8'), /lang: en/);
  assert.doesNotMatch(fs.readFileSync('_includes/writing-guide.md', 'utf8'), /[가-힣]/);
});
