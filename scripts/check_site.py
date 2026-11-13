#!/usr/bin/env python3
"""Validate public routes, inherited theme structure, and content links."""
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
  super().__init__(convert_charrefs=True);self.path=path;self.ids=[];self.links=[];self.h1=0;self.rows=[];self.attrs={};self.styles=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id']);self.attrs[a['id']]=a
  if tag=='h1':self.h1+=1
  if tag in ('a','link') and a.get('href'):self.links.append(a['href'])
  if tag in ('script','img') and a.get('src'):self.links.append(a['src'])
  if tag=='article' and a.get('data-post-url'):self.rows.append(a['data-post-url'])
  if tag=='img' and 'alt' not in a:errors.append(f'{self.path}: image lacks alt text')
  if tag=='link' and a.get('rel')=='stylesheet':self.styles.append(a)

def local_target(url,current):
 u=urlsplit(url)
 if u.scheme in ['mailto','tel','data'] or (u.netloc and u.netloc!='jirrong.github.io'):return None
 if not u.path:return current
 path=unquote(u.path)
 if path.startswith(base+'/'):path=path[len(base):]
 elif path.startswith('/') and path!=base:
  errors.append(f'{current.relative_to(root)}: URL escapes site base: {url}');return None
 if path.startswith('/'):
  target=root/path.lstrip('/')
 else:target=current.parent/path
 if target.is_dir():target=target/'index.html'
 return target

pages={}
for path in root.rglob('*.html'):
 p=Page(str(path.relative_to(root)));p.feed(path.read_text());pages[path]=p
required=['index.html','cv/index.html','interests/index.html','publications/index.html','blog/index.html','guide/index.html','writing/index.html','allnews.html','404.html']
for route in required:
 if root/route not in pages:errors.append('missing route: '+route)
for path,page in pages.items():
 if page.h1!=1:errors.append(f'{page.path}: expected one H1, found {page.h1}')
 for identity,count in Counter(page.ids).items():
  if count>1:errors.append(f'{page.path}: duplicate ID {identity}')
 for url in page.links:
  target=local_target(url,path)
  if target is None:continue
  if not target.is_file():errors.append(f'{page.path}: missing local asset or page {url}');continue
  fragment=unquote(urlsplit(url).fragment)
  if fragment and target in pages and fragment not in pages[target].ids:errors.append(f'{page.path}: missing anchor {url}')
 html=path.read_text()
 if 'assets/css/academic.css' in html or 'brand-mark' in html:errors.append(f'{page.path}: replacement-theme markup remains')
 if 'UA-82472331-1' in html:errors.append(f'{page.path}: source-lab analytics still enabled')
 if 'navbar-collapse-1' not in page.ids or 'footer' not in page.ids:errors.append(f'{page.path}: original navigation/footer structure missing')
 for style in page.styles:
  href=style.get('href','')
  if not urlsplit(href).path.endswith('/css/main.css'):
   errors.append(f'{page.path}: unexpected screen-theme stylesheet {href}')
home=pages.get(root/'index.html')
if home:
 if 'col-sm-8' not in home.attrs.get('homeid',{}).get('class',''):errors.append('home main column changed from original template')
 if 'col-sm-4' not in home.attrs.get('newsid',{}).get('class',''):errors.append('home news column changed from original template')
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
for name in ['AGENTS.md','node_modules','scripts','tests','docs','package.json','CNAME','downloads','pictures']:
 if (root/name).exists():errors.append('excluded source unexpectedly published: '+name)
if (root/'assets/css/academic.css').exists():errors.append('replacement stylesheet was published')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages, local links/anchors, original theme structure, {len(index)} published posts, RSS/sitemap, and source exclusions.')
