#!/usr/bin/env python3
"""Check built routes, local links, metadata, feed, and published-post indexes."""
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
BASE = sys.argv[2] if len(sys.argv) > 2 else '/jhhwang'
ORIGIN = 'jirrong.github.io'
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.h1, self.canonical = path, [], [], 0, []
        self.description = False
        self.main = False
        self.blog_rows = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main = True
        if tag == 'meta' and a.get('name') == 'description': self.description = bool(a.get('content'))
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical.append(a.get('href', ''))
        if tag in ('a', 'link') and a.get('href'): self.links.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.links.append(a['src'])
        if tag == 'img' and 'alt' not in a: errors.append(f'{self.path}: image is missing alt text')
        if tag == 'article' and a.get('data-post-url'): self.blog_rows.append(a['data-post-url'])
    def handle_data(self, data):
        if re.search(r'</?(?:div|section|article|h1|h2|aside)(?:\s|>)', data):
            errors.append(f'{self.path}: HTML markup escaped into visible text')

def target_file(path):
    value = unquote(path)
    if BASE and value == BASE: value = '/'
    elif BASE and value.startswith(BASE + '/'): value = value[len(BASE):]
    elif BASE and value.startswith('/'):
        errors.append(f'local URL escapes the configured base path: {path}')
        return None
    candidate = ROOT / value.lstrip('/')
    if candidate.is_dir(): candidate /= 'index.html'
    return candidate

pages = {}
for path in ROOT.rglob('*.html'):
    p = Page(str(path.relative_to(ROOT)))
    p.feed(path.read_text(encoding='utf-8'))
    pages[path] = p
    if p.h1 != 1: errors.append(f'{p.path}: expected one H1, found {p.h1}')
    if not p.main: errors.append(f'{p.path}: missing main landmark')
    if not p.description: errors.append(f'{p.path}: missing description')
    if len(p.canonical) != 1: errors.append(f'{p.path}: missing or duplicate canonical URL')
    for identity, count in Counter(p.ids).items():
        if count > 1: errors.append(f'{p.path}: duplicate id {identity}')

for path, p in pages.items():
    for href in p.links:
        u = urlsplit(href)
        if u.scheme in ('mailto', 'tel', 'data'): continue
        if u.netloc and u.netloc != ORIGIN: continue
        if not u.path: target = path
        elif u.path.startswith('/'): target = target_file(u.path)
        else:
            target = path.parent / unquote(u.path)
            if target.is_dir(): target /= 'index.html'
        if target is None: continue
        if not target.is_file(): errors.append(f'{p.path}: broken local link {href}'); continue
        if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{p.path}: missing anchor {href}')

for route in ['index.html', 'blog/index.html', 'cv/index.html', 'interests/index.html', 'publications/index.html', 'writing/index.html', '404.html']:
    if not (ROOT / route).is_file(): errors.append(f'missing route: {route}')
for excluded in ['CNAME', 'docs', 'tests', 'scripts', 'node_modules', 'Gemfile', 'package.json', 'images', 'downloads']:
    if (ROOT / excluded).exists(): errors.append(f'non-public source unexpectedly published: {excluded}')

index = json.loads((ROOT / 'search.json').read_text())
urls = [entry['url'] for entry in index]
blog = pages.get(ROOT / 'blog/index.html')
if blog and set(blog.blog_rows) != set(urls): errors.append('blog listing and search index disagree')
if len(urls) != len(set(urls)): errors.append('duplicate search index URLs')
for entry in index:
    if not entry.get('title') or not isinstance(entry.get('tags'), list): errors.append('invalid search index shape')
    target = target_file(entry['url'])
    if target and not target.is_file(): errors.append(f'post is missing: {entry["url"]}')
feed = ElementTree.parse(ROOT / 'feed.xml')
ns = {'a': 'http://www.w3.org/2005/Atom'}
feed_urls = [node.attrib['href'] for node in feed.findall('a:entry/a:link', ns) if node.attrib.get('rel') == 'alternate']
if set(urlsplit(url).path for url in feed_urls) != set(urls[:10]): errors.append('RSS entries and newest published posts disagree')
ElementTree.parse(ROOT / 'sitemap.xml')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f'PASS: {len(pages)} HTML pages, local links and anchors, metadata, {len(index)} published posts, RSS, sitemap, and source exclusions.')
