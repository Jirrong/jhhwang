#!/usr/bin/env python3
"""Mirror an owner's public LinkedIn posts using the official, authorized API.

An API JSON response can also be imported offline with --input. No scraping,
translation, summarization, or generated post content is used.
"""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
from html import escape
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.parse import urlencode, quote, urlsplit
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo


class LinkedInClient:
    def __init__(self, token, version):
        if not token:
            raise ValueError('LINKEDIN_ACCESS_TOKEN is required; it must include approved r_member_social access.')
        if not re.fullmatch(r'20\d{4}', version):
            raise ValueError('LINKEDIN_API_VERSION must be YYYYMM.')
        self.token, self.version = token, version

    def get(self, path):
        request = Request('https://api.linkedin.com' + path, headers={
            'Authorization': 'Bearer ' + self.token,
            'Linkedin-Version': self.version,
            'X-Restli-Protocol-Version': '2.0.0',
            'X-RestLi-Method': 'FINDER' if path.startswith('/rest/posts?') else 'GET',
            'Accept': 'application/json',
        })
        try:
            with urlopen(request, timeout=30) as response:
                return json.load(response)
        except HTTPError as error:
            raise ValueError(f'LinkedIn API returned HTTP {error.code}. Check token expiry, approved read permissions, and API version.') from None

    def posts(self, author):
        records, start = [], 0
        for _ in range(100):
            query = urlencode({'author': author, 'q': 'author', 'count': 50, 'start': start, 'sortBy': 'LAST_MODIFIED'})
            page = self.get('/rest/posts?' + query)
            elements = page.get('elements', [])
            if not isinstance(elements, list):
                raise ValueError('The Posts API returned an invalid elements list.')
            records.extend(elements)
            more = any(link.get('rel') == 'next' for link in page.get('paging', {}).get('links', []))
            if not elements or (len(elements) < 50 and not more):
                return records
            start += len(elements)
        raise ValueError('Pagination exceeded 100 pages; no changes were published.')

    def image(self, image_urn):
        metadata = self.get('/rest/images/' + quote(image_urn, safe=''))
        return download_image(metadata.get('downloadUrl', ''))


def download_image(url):
    """Download public media separately; never send the API token to a CDN."""
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or not parsed.hostname or not parsed.hostname.endswith('.licdn.com') or parsed.username or parsed.password:
        raise ValueError('LinkedIn returned an unexpected media host; the image was not downloaded.')
    with urlopen(Request(url, headers={'User-Agent': 'JihoHwangBlogSync/1.0'}), timeout=30) as response:
        final_host = urlsplit(response.url).hostname or ''
        if not final_host.endswith('.licdn.com'):
            raise ValueError('LinkedIn media redirected outside its CDN.')
        extensions = {'image/jpeg': 'jpg', 'image/png': 'png', 'image/webp': 'webp', 'image/gif': 'gif'}
        extension = extensions.get(response.headers.get_content_type())
        if not extension:
            raise ValueError('The image response is not a supported image type.')
        data = response.read(20 * 1024 * 1024 + 1)
        if len(data) > 20 * 1024 * 1024:
            raise ValueError('An image exceeds the 20 MiB import limit.')
        return data, extension


def visible_text(text):
    """Expand LinkedIn's visible hashtag/mention tokens without rewriting prose."""
    if not isinstance(text, str):
        raise ValueError('LinkedIn commentary must be text.')
    text = re.sub(r'\{hashtag\|\\?#\|([^{}]+)\}', lambda match: '#' + match[1], text)
    text = re.sub(r'@\[([^\]]+)\]\(urn:li:[^)]+\)', lambda match: match[1], text)
    return text


def image_records(post):
    content = post.get('content') or {}
    images = list((content.get('multiImage') or {}).get('images', []))
    media = content.get('media') or {}
    if str(media.get('id', '')).startswith('urn:li:image:'):
        images.append({'id': media['id'], 'altText': media.get('altText', '')})
    return images


def mirror_posts(root, posts, author, client=None):
    if not re.fullmatch(r'urn:li:person:[A-Za-z0-9_-]+', author or ''):
        raise ValueError('Set LINKEDIN_AUTHOR_URN to your own urn:li:person:... identifier.')
    root = Path(root).resolve()
    posts_dir = root / '_posts'
    assets_dir = root / 'assets/linkedin'
    posts_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)
    changed, unchanged, skipped = [], [], 0
    for post in posts:
        if not isinstance(post, dict):
            raise ValueError('Every imported post must be a JSON object.')
        if post.get('author') != author or post.get('visibility') != 'PUBLIC' or post.get('lifecycleState') != 'PUBLISHED' or post.get('reshareContext'):
            skipped += 1
            continue
        identity = re.fullmatch(r'urn:li:(share|ugcPost):(\d+)', post.get('id', ''))
        if not identity:
            raise ValueError('A published post has an unsupported or missing ID.')
        kind, number = identity.groups()
        key = kind + '-' + number
        timestamp = post.get('publishedAt') or post.get('createdAt')
        if not isinstance(timestamp, int) or isinstance(timestamp, bool) or timestamp <= 0:
            raise ValueError('A published post is missing its original publication timestamp.')
        published = datetime.fromtimestamp(timestamp / 1000, timezone.utc).astimezone(ZoneInfo('Asia/Seoul'))
        text = visible_text(post.get('commentary') or '')
        images = image_records(post)
        if not text.strip() and not images and not post.get('content'):
            skipped += 1
            continue
        digest = sha256(json.dumps({k: post.get(k) for k in ('id', 'publishedAt', 'createdAt', 'commentary', 'content')}, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        existing = list(posts_dir.glob('*-linkedin-' + key + '.md'))
        if len(existing) > 1:
            raise ValueError('Multiple blog files use the same LinkedIn ID; resolve the duplicate before syncing.')
        target = existing[0] if existing else posts_dir / (published.strftime('%Y-%m-%d') + '-linkedin-' + key + '.md')
        if target.exists():
            original = target.read_text()
            asset_match = re.search(r'^linkedin_assets: (\[.*\])$', original, re.M)
            stored_assets = json.loads(asset_match[1]) if asset_match else []
            if 'linkedin_source_hash: "' + digest + '"' in original and all((root / path.lstrip('/')).is_file() for path in stored_assets):
                unchanged.append(target.name)
                continue
        source = 'https://www.linkedin.com/feed/update/' + post['id'] + '/'
        local_images = []
        for index, image in enumerate(images, 1):
            image_urn = image.get('id', '')
            if not re.fullmatch(r'urn:li:image:[A-Za-z0-9_-]+', image_urn):
                raise ValueError('A post image has an invalid LinkedIn image ID.')
            if not client:
                raise ValueError('This post has images. An authorized API client is required to download their originals.')
            data, extension = client.image(image_urn)
            image_path = assets_dir / f'{key}-{index}.{extension}'
            image_path.write_bytes(data)
            local_images.append(('/assets/linkedin/' + image_path.name, image.get('altText') or 'Image from the original LinkedIn post'))
        compact = ' '.join(text.split())
        title = next((line.strip() for line in text.splitlines() if line.strip()), 'LinkedIn post')[:100]
        metadata = {
            'title': title, 'date': published.strftime('%Y-%m-%d %H:%M:%S %z'),
            'description': compact[:180], 'categories': ['LinkedIn'], 'tags': ['LinkedIn'],
            'excerpt': escape(compact[:160], quote=True),
            'lang': 'en', 'math': False, 'toc': False,
            'linkedin_id': post['id'], 'linkedin_url': source,
            'linkedin_source_hash': digest, 'linkedin_assets': [path for path, _ in local_images],
        }
        # Encode braces as well as HTML so imported text cannot execute Liquid.
        safe_text = escape(text).replace('{', '&#123;').replace('}', '&#125;')
        body = f'<div class="linkedin-text" markdown="0">{safe_text}</div>\n'
        if local_images:
            body += '\n<div class="linkedin-media" markdown="0">\n'
            for path, alt in local_images:
                body += '<img src="{{ \'' + path + '\' | relative_url }}" alt="' + escape(alt, quote=True) + '" loading="lazy">\n'
            body += '</div>\n'
        article = (post.get('content') or {}).get('article') or {}
        article_url = article.get('source', '')
        if article_url:
            parsed = urlsplit(article_url)
            if parsed.scheme in ('http', 'https') and parsed.hostname:
                body += '\n<p><a href="' + escape(article_url, quote=True) + '">' + escape(article.get('title') or 'Linked article') + '</a></p>\n'
        body += '\n<p class="text-muted post-source">Originally published on <a href="' + source + '">LinkedIn</a>.'
        media = (post.get('content') or {}).get('media') or {}
        if media and not str(media.get('id', '')).startswith('urn:li:image:'):
            body += ' View the original post for its video or document attachment.'
        body += '</p>\n'
        front = '\n'.join(key + ': ' + json.dumps(value, ensure_ascii=False) for key, value in metadata.items())
        target.write_text('---\n' + front + '\n---\n\n' + body)
        changed.append(target.name)
    return {'changed': changed, 'unchanged': unchanged, 'skipped': skipped}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--input', type=Path, help='Import an official Posts API JSON response instead of fetching it.')
    parser.add_argument('--author', default=os.environ.get('LINKEDIN_AUTHOR_URN', ''))
    parser.add_argument('--version', default=os.environ.get('LINKEDIN_API_VERSION', '202610'))
    args = parser.parse_args()
    try:
        token = os.environ.get('LINKEDIN_ACCESS_TOKEN', '')
        client = LinkedInClient(token, args.version) if token else None
        if args.input:
            data = json.loads(args.input.read_text())
            posts = data.get('elements') if isinstance(data, dict) else data
            if not isinstance(posts, list):
                raise ValueError('Input must be an array of posts or a Posts API response with an elements array.')
        else:
            if not client:
                raise ValueError('Set LINKEDIN_ACCESS_TOKEN with approved r_member_social access, or use --input for an API JSON export.')
            posts = client.posts(args.author)
        print(json.dumps(mirror_posts(args.root, posts, args.author, client), ensure_ascii=False))
    except (ValueError, OSError) as error:
        parser.exit(1, f'LinkedIn sync failed: {error}\n')


if __name__ == '__main__':
    main()
