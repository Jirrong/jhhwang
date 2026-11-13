# Jiho Hwang's personal academic website

The original Jekyll / Bootstrap / Bootswatch design is preserved exactly. Do not redesign the site or change its typography, colors, spacing, header, footer, or existing home/CV layouts. The user explicitly requires the original template's visual design.

The design baseline is commit `f25f182c00dbd1e625bb355571cc352bb9f40612`. `scripts/template-baseline.json` records 100 original design files; `python3 scripts/check_template.py` checks their Git blob identities byte for byte. Functional blog additions use the existing Bootstrap classes and original `textlay`/`default` layouts. There is no override stylesheet.

## Write a post

Open **Blog Posts → 새 글 쓰기 / 글쓰기 안내 → 새 글 쓰기**. The existing **Guide** menu opens the same instructions. The shortcut opens GitHub's editor with a dated Markdown template. Commit to `gh-pages` to publish, or use a branch and pull request to review first.

Posts live in `_posts/YYYY-MM-DD-title.md`. A full template is in `_drafts/academic-post-template.md`.

```yaml
---
title: "My academic note"
date: 2026-11-13 00:00:00 +0900
description: "A short introduction."
categories: [Study notes]
tags: [Chemistry]
lang: en
math: true
toc: true
---
```

Write Markdown below the front matter. `##` and `###` generate a table of contents. LaTeX math, fenced code with a copy button, tables, footnotes, full-text search, tag filters, and RSS are supported.

`_drafts/` and `published: false` are omitted from the built site and its search/feed. The repository is public, so draft source is still visible on GitHub. Future-dated posts require a rebuild at or after their date; GitHub Pages does not schedule that rebuild.

## Checks

```sh
bundle install
python3 scripts/check_template.py
bundle exec jekyll build --safe --strict_front_matter --trace
python3 scripts/check_site.py _site
npm ci
npm test
```

Node is used only for tests. Posting requires no Node tooling. Production uses the existing GitHub Pages `gh-pages` branch and `/jhhwang` base path.

The original CV and original page content are retained. The requested Google Drive CV has not been identified; no other person's CV has been substituted.

## Attribution

The site retains the [Allan Lab template](https://www.allanlab.org/aboutwebsite.html), powered by Jekyll, Bootstrap, and Bootswatch. Its original attribution remains unchanged in the original footer. MathJax 3.2.2 loads only on notebook/guide pages that request math.
