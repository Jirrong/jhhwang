#!/usr/bin/env python3
"""The original design is a fixed contract, not a framework-only preference."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'scripts/template-baseline.json').read_text())
errors = []
for name, expected in manifest['files'].items():
    path = root / name
    if not path.is_file():
        errors.append(f'missing original design file: {name}')
        continue
    data = path.read_bytes()
    for change in manifest.get('approved_substitutions', {}).get(name, []):
        current = change['current'].encode()
        if data.count(current) != 1:
            errors.append(f'missing approved substitution: {name}')
            continue
        data = data.replace(current, change['original'].encode(), 1)
    suffix = manifest.get('approved_appends', {}).get(name)
    if suffix:
        suffix = suffix.encode()
        if not data.endswith(suffix):
            errors.append(f'missing approved layout append: {name}')
            continue
        data = data[:-len(suffix)]
    actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if actual != expected:
        errors.append(f'original design changed: {name}')
if (root / 'assets/css/academic.css').exists():
    errors.append('redesign override stylesheet must not be present')
if errors:
    raise SystemExit('\n'.join(errors))
print(f"PASS: {len(manifest['files'])} original theme bases match {manifest['commit']} byte for byte.")
