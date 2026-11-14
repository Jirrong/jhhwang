#!/usr/bin/env python3
"""Verify the author's original CV bytes without modifying the document."""
from pathlib import Path
from hashlib import sha256
from urllib.parse import urlsplit, parse_qs
import json, re
root=Path(__file__).resolve().parents[1]
original=json.loads((root/'scripts/cv-original.json').read_text())
text=(root/'_config.yml').read_text()
match=re.search(r'^cv_pdf:\s*(/assets/pdf/[^\s]+)\s*$',text,re.M)
if not match:raise SystemExit('cv_pdf must point to a same-origin file under /assets/pdf/.')
url=urlsplit(match[1])
if url.path!=original['path']:raise SystemExit('CV URL must point to the recorded author-supplied PDF.')
if parse_qs(url.query).get('v')!=[original['sha256'][:12]]:raise SystemExit('CV URL version must match the author-supplied PDF fingerprint.')
pdf=root/url.path.lstrip('/')
if not pdf.is_file():raise SystemExit('Configured CV PDF is missing.')
data=pdf.read_bytes()
if not data.startswith(b'%PDF-') or not data.rstrip().endswith(b'%%EOF') or len(data)<1000:raise SystemExit('CV asset is not a complete PDF file.')
if len(data)!=original['size_bytes'] or sha256(data).hexdigest()!=original['sha256']:
 raise SystemExit('CV differs from the author-supplied original. Restore the original bytes; do not regenerate or reformat the PDF.')
print(f'PASS: CV matches the author-supplied original exactly ({len(data)} bytes; SHA-256 verified).')
