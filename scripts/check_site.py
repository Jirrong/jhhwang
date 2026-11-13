#!/usr/bin/env python3
"""Check new notebook routes without changing inherited template behavior."""
import json
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
from xml.etree import ElementTree

root=Path(sys.argv[1] if len(sys.argv)>1 else '_site').resolve()
base='/jhhwang'
errors=[]
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__(convert_charrefs=True);self.path=path;self.ids=[];self.links=[];self.h1=0;self.rows=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag in ('a','link') and a.get('href'):self.links.append(a['href'])
  if tag in ('script','img') and a.get('src'):self.links.append(a['src'])
  if tag=='article' and a.get('data-post-url'):self.rows.append(a['data-post-url'])

def local_target(url,current):
 u=urlsplit(url)
 if u.scheme in ['mailto','tel','data'] or (u.netloc and u.netloc!='jirrong.github.io'):return None
 if not u.path:return current
 path=unquote(u.path)
 if path.startswith(base+'/'):path=path[len(base):]
 if path.startswith('/'):
  target=root/path.lstrip('/')
 else:target=current.parent/path
 if target.is_dir():target=target/'index.html'
 return target

pages={}
for path in root.rglob('*.html'):
 p=Page(str(path.relative_to(root)));p.feed(path.read_text());pages[path]=p
new_routes=['blog/index.html','guide/index.html','writing/index.html']
new_routes += [str(p.relative_to(root)) for p in (root/'blog').rglob('index.html') if p!=root/'blog/index.html']
for route in new_routes:
 path=root/route
 if not path.is_file():errors.append('missing new route: '+route);continue
 page=pages[path]
 if page.h1!=1:errors.append(f'{route}: expected one H1')
 for identity,count in Counter(page.ids).items():
  if count>1:errors.append(f'{route}: duplicate ID {identity}')
 for url in page.links:
  target=local_target(url,path)
  if target is None:continue
  if not target.is_file():errors.append(f'{route}: missing local asset or page {url}');continue
  fragment=unquote(urlsplit(url).fragment)
  if fragment and target in pages and fragment not in pages[target].ids:errors.append(f'{route}: missing anchor {url}')
 html=path.read_text()
 if 'assets/css/academic.css' in html or 'site-header' in html:errors.append(f'{route}: redesign markup remains')
index=json.loads((root/'search.json').read_text())
urls=[p['url'] for p in index]
if set(pages[root/'blog/index.html'].rows)!=set(urls):errors.append('blog list and search disagree')
for post in index:
 if not local_target(post['url'],root/'index.html').is_file():errors.append('missing published post '+post['url'])
feed=ElementTree.parse(root/'feed.xml')
ns={'a':'http://www.w3.org/2005/Atom'}
feed_urls=[urlsplit(n.attrib['href']).path for n in feed.findall('a:entry/a:link',ns) if n.attrib.get('rel')=='alternate']
if set(feed_urls)!=set(urls[:10]):errors.append('RSS entries disagree with published posts')
ElementTree.parse(root/'sitemap.xml')
for name in ['AGENTS.md','node_modules','scripts','tests','docs','package.json','CNAME']:
 if (root/name).exists():errors.append('non-public source unexpectedly published: '+name)
if (root/'assets/css/academic.css').exists():errors.append('redesign stylesheet was published')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(new_routes)} notebook/guide routes, local links/anchors, {len(index)} published posts, RSS, sitemap, and no redesign assets.')
