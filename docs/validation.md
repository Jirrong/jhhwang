# Validation

Validated with Ruby 3.3.6, Jekyll 3.10.0, and the checked-in Bundler lockfile.

- Production `jekyll build --safe --strict_front_matter --trace`.
- Built-site checks: all public routes, one H1 per page, alt text, main landmarks, canonical/description metadata, local assets and anchors, search/list/feed agreement, valid RSS/sitemap XML, and development/legacy source exclusions.
- Nine Node DOM tests: full-text search, Korean queries, shared tag URLs including reserved characters, empty/reset states, index-download failure, history changes, no-JavaScript links, mobile-menu state, Seoul-date post templates, and article TOC/code-copy behavior.
- An isolated safe build with sample math, code, footnotes, image paths, a draft, an unpublished post, and a future-dated post. MathJax delimiters, highlighting, footnotes, and source exclusions were checked in generated output. This specimen is not included in the published repository.
- MathJax 3.2.2 CDN returned HTTP 200.

The session did not offer a browser-control tool. Visual rendering, physical viewport layouts, clipboard permission prompts, and actual MathJax layout were not tested in a browser. DOM/build checks do not establish those results.

Content follows the existing repository CV pending identification of the intended Google Drive CV; see `content-sources.md`.
