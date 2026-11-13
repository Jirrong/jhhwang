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

test('original theme bases and approved layout additions satisfy the theme guard', () => {
  const { execFileSync } = require('node:child_process');
  const result = execFileSync('python3', ['scripts/check_template.py'], { encoding: 'utf8' });
  assert.match(result, /92 original theme bases/);
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
  const { document } = parseHTML('<html><body><div class="notebook-layout"><div id="post-content"><h2 id="question">질문</h2><h3>분석</h3><pre><code>print("hello")\n</code></pre></div><aside class="table-of-contents" hidden><nav id="toc-links"></nav></aside></div></body></html>');
  let copied = '';
  vm.runInNewContext(source('post'), { document, window: {}, navigator: { clipboard: { writeText: async text => { copied = text; } } }, setTimeout: () => {} });
  assert.equal(document.querySelector('.table-of-contents').hidden, false);
  assert.ok(document.querySelector('.notebook-layout').classList.contains('has-toc'));
  assert.equal(document.querySelectorAll('#toc-links a').length, 2);
  document.querySelector('.copy-code').click(); await settle();
  assert.equal(copied, 'print("hello")\n');
  assert.match(document.querySelector('[role="status"]').textContent, /Code copied/);
});

test('CV menu and profile links download the actual PDF without a JavaScript dependency', () => {
  const { document } = parseHTML(fs.readFileSync('_site/index.html', 'utf8'));
  const nav = [...document.querySelectorAll('#navbar-collapse-1 a')].find(link => link.textContent === 'CV');
  assert.equal(nav.getAttribute('href'), '/jhhwang/assets/pdf/Jiho_Hwang_CV.pdf');
  assert.equal(nav.getAttribute('download'), 'Jiho_Hwang_CV.pdf');
  assert.equal(nav.getAttribute('type'), 'application/pdf');
  const profile = document.querySelector('.profile-contact a[download]');
  assert.equal(profile.getAttribute('href'), nav.getAttribute('href'));
  const data = fs.readFileSync('_site/assets/pdf/Jiho_Hwang_CV.pdf');
  assert.equal(data.subarray(0, 5).toString(), '%PDF-');
  assert.match(data.subarray(-20).toString(), /%%EOF/);
});

test('legacy CV page triggers a single PDF download and retains a normal fallback link', () => {
  const { document } = parseHTML(fs.readFileSync('_site/cv/index.html', 'utf8'));
  const link = document.getElementById('cv-download-link');
  let clicks = 0; link.click = () => { clicks += 1; };
  vm.runInNewContext(source('cv-download'), { document });
  assert.equal(clicks, 1);
  assert.equal(link.getAttribute('download'), 'Jiho_Hwang_CV.pdf');
  assert.equal(link.getAttribute('href'), '/jhhwang/assets/pdf/Jiho_Hwang_CV.pdf');
  assert.equal(document.getElementById('education'), null);
});

test('blog controls and writing template use English by default', () => {
  const { document } = parseHTML(fs.readFileSync('_site/blog/index.html', 'utf8'));
  assert.equal(document.querySelector('label[for="blog-search"]').textContent, 'Search posts');
  assert.equal(document.getElementById('clear-search').textContent, 'Reset');
  assert.match(document.getElementById('no-results').textContent, /No posts found/);
  assert.match(fs.readFileSync('_drafts/academic-post-template.md', 'utf8'), /lang: en/);
  assert.doesNotMatch(fs.readFileSync('_includes/writing-guide.md', 'utf8'), /[가-힣]/);
});

test('compiled CSS makes the outer container fill the screen and provides a wide responsive notebook', () => {
  const { document } = parseHTML(fs.readFileSync('_site/blog/index.html', 'utf8'));
  const styleURL = new URL(document.querySelector('link[rel="stylesheet"]').getAttribute('href'));
  assert.match(styleURL.searchParams.get('v'), /^\d+$/);
  const cssom = require('cssom');
  const sheet = cssom.parse(fs.readFileSync('_site/css/main.css', 'utf8'));
  const value = (selector, property) => [...sheet.cssRules].filter(rule => rule.selectorText === selector).map(rule => rule.style.getPropertyValue(property)).filter(Boolean).at(-1);
  assert.equal(value('.container-fluid', 'width'), '100%');
  assert.equal(value('.notebook-page', 'max-width'), '1360px');
  assert.equal(value('.notebook-layout.has-toc', 'grid-template-columns'), 'minmax(0, 1fr) 240px');
  assert.equal(value('.notebook-content', 'min-width'), '0');
  assert.equal(value('.notebook-content pre code', 'white-space'), 'pre');
  assert.equal(value('.home-profile .profile-photo', 'width'), '100%');
  const mobile = [...sheet.cssRules].find(rule => rule.conditionText === '(max-width: 991px)' && [...rule.cssRules].some(r => r.selectorText === '.notebook-layout.has-toc'));
  assert.ok(mobile, 'the TOC must stack rather than narrow mobile text');
});

test('an article without enough headings does not reserve an empty TOC column', () => {
  const { document } = parseHTML('<html><body><div class="notebook-layout"><div id="post-content"><h2>One section</h2><p>Text.</p></div><aside class="table-of-contents" hidden><ul id="toc-links"></ul></aside></div></body></html>');
  vm.runInNewContext(source('post'), { document });
  assert.equal(document.querySelector('.table-of-contents').hidden, true);
  assert.equal(document.querySelector('.notebook-layout').classList.contains('has-toc'), false);
});

test('research and resources have their own navigation and retain original wells', () => {
  const { document } = parseHTML(fs.readFileSync('_site/research/index.html', 'utf8'));
  const links = [...document.querySelectorAll('#navbar-collapse-1 a')];
  assert.equal(links.find(a => a.textContent === 'Research').getAttribute('href'), '/jhhwang/research/');
  assert.equal(links.find(a => a.textContent === 'Resources').getAttribute('href'), '/jhhwang/resources/');
  assert.equal(document.querySelectorAll('.record-stack > .well.research-card').length, 2);
  assert.match(document.querySelector('.research-card h2').textContent, /Reaction mechanisms/);
  for (const link of document.querySelectorAll('.research-card h2 a')) {
    assert.ok(fs.existsSync(`_site/${link.getAttribute('href').replace('/jhhwang/', '')}index.html`));
  }
  const { document: resources } = parseHTML(fs.readFileSync('_site/resources/index.html', 'utf8'));
  assert.equal(resources.querySelectorAll('.resource-card').length, 0);
  assert.match(resources.querySelector('.resource-empty').textContent, /No seminar materials have been published yet/);
  assert.equal(resources.querySelector('#footer a[href="/jhhwang/guide/"]').textContent, 'Site guide');
});

test('research and seminar shortcuts prepare draft records and the next stacking order', () => {
  const { document } = parseHTML(fs.readFileSync('_site/guide/index.html', 'utf8'));
  vm.runInNewContext(source('site'), { document, URL, Intl, Date });
  for (const [id, folder, filename, order] of [
    ['new-research-link', '_research', 'project-title.md', 3],
    ['new-resource-link', '_resources', 'seminar-title.md', 1]
  ]) {
    const url = new URL(document.getElementById(id).getAttribute('href'));
    assert.equal(url.pathname, `/Jirrong/jhhwang/new/gh-pages/${folder}`);
    assert.equal(url.searchParams.get('filename'), filename);
    const content = url.searchParams.get('value');
    assert.match(content, new RegExp(`\\norder: ${order}\\n`));
    assert.match(content, /\npublished: false\n---\n/);
    assert.match(content, /## References/);
  }
  const resource = new URL(document.getElementById('new-resource-link').getAttribute('href')).searchParams.get('value');
  assert.match(resource, /url: \/assets\/resources\/your-seminar.pdf/);
  assert.ok(document.querySelector('a[href="https://github.com/Jirrong/jhhwang/upload/gh-pages/assets/resources"]'));
});
