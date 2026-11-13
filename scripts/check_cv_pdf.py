#!/usr/bin/env python3
"""Check the real downloadable CV asset without regenerating an uploaded CV."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
text=(root/'_config.yml').read_text()
match=re.search(r'^cv_pdf:\s*(/assets/pdf/[^\s]+)\s*$',text,re.M)
if not match:raise SystemExit('cv_pdf must point to a same-origin file under /assets/pdf/.')
pdf=root/match[1].lstrip('/')
if not pdf.is_file():raise SystemExit('Configured CV PDF is missing.')
data=pdf.read_bytes()
if not data.startswith(b'%PDF-') or not data.rstrip().endswith(b'%%EOF') or len(data)<1000:raise SystemExit('CV asset is not a complete PDF file.')
print(f'PASS: downloadable CV PDF exists ({len(data)} bytes); uploaded PDFs are preserved.')
