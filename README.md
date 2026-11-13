# Jiho Hwang — Academic home & notebook

Jekyll / GitHub Pages personal academic website, retaining the Allan Lab template's Bootstrap grid and Sass foundation.

## Write a post

Open **Notebook → Writing guide → 새 글 쓰기** on the site. This opens GitHub's editor with a dated Markdown template. Commit to `gh-pages` to publish, or use a branch and pull request to review first.

Posts live at `_posts/YYYY-MM-DD-title.md`:

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

Write Markdown below the front matter. Use `##` / `###` for the table of contents, `$...$` or `$$...$$` for LaTeX math, fenced code for syntax highlighting, and Kramdown footnotes for citations. A full template is in `_drafts/academic-post-template.md`.

**Drafts:** `_drafts/` and `published: false` are omitted from the built site, search, and RSS. This is a public repository; draft source is still visible on GitHub. Future-dated posts require a rebuild at or after their date; GitHub Pages does not schedule that rebuild automatically.

## Update content

| Content | Source |
| --- | --- |
| Profile / contact / CV date | `_data/profile.yml` |
| Education, experience, awards, skills | `_data/cv.yml` |
| Research interests | `_data/research.yml` |
| Research output | `_pages/publications.md` |
| Home layout | `_pages/home.md` |
| Visual design | `assets/css/academic.css` |
| Blog posts | `_posts/` |

To link an author-approved CV PDF, put it at `assets/documents/jiho-hwang-cv.pdf` and set `cv_pdf: /assets/documents/jiho-hwang-cv.pdf` in `_data/profile.yml`. The PDF download button appears only when configured. The CV always supports browser printing / Save as PDF.

Current biography and accomplishments come from the original repository CV; see [content sources](docs/content-sources.md). Keep source facts and the displayed CV date in sync.

## Local build and checks

With Ruby 3.3 and Bundler:

```sh
bundle install
bundle exec jekyll build --strict_front_matter --trace
python3 scripts/check_site.py _site
npm ci
npm test
```

`bundle exec jekyll serve` serves the site at `http://127.0.0.1:4000/jhhwang/`. Node is used only for development checks; writing and publishing need no Node tooling.

The deployment target is the repository's existing GitHub Pages branch, `gh-pages`. The configured public base path is `/jhhwang`. The inherited `www.allanlab.org` CNAME has been removed; configuring a different domain also requires updating `url` / `baseurl` and the repository Pages settings.

## Features

Responsive layout, keyboard navigation, article search, shareable search and tag URLs, MathJax, code highlighting/copy, table of contents, article progress, RSS, sitemap, canonical/social metadata, and print-friendly CV. Search and navigation degrade gracefully when JavaScript is unavailable.

## Attribution

Based on the [Allan Lab website template](https://www.allanlab.org/aboutwebsite.html), originally released under the MIT License. The original template's source assets remain in the repository for reference; unused lab images, downloads, and legacy pages are excluded from the published site. Math is rendered with MathJax 3.2.2 from jsDelivr only on pages that enable it.
