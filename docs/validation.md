# Validation

The user's latest instruction permits rebuilding the CV and personal content while retaining the Allan Lab visual foundation.

- **Theme:** 92 protected CSS, Sass, font, grid, and layout files match `f25f182c00dbd1e625bb355571cc352bb9f40612` byte for byte. The explicitly editable content/CV templates are recorded separately. No replacement screen theme is loaded; the added CV stylesheet is print-only.
- **Content:** the CV record and publication schema pass validation. The initial publication list is empty. An in-memory fixture verifies original-style selected-paper cards, the full list, optional images/links, and draft exclusion without writing example papers to the live data.
- **Build:** Jekyll 3.10 safe production build succeeds. Ten rendered pages pass route, local-link/anchor, image-alt, original-navigation/footer, stylesheet, RSS/search, sitemap, and source-exclusion checks.
- **Behavior:** eleven Node DOM tests pass, including full-text/tag search, Unicode and reserved-character URLs, reset/empty/failure states, no-JavaScript navigation, Seoul-date English post templates, TOC, code copying, and CV printing.
- **Language:** the current blog entry, controls, status/error messages, draft template, GitHub editor prefill, and writing/publication guide are English. The CV retains the author's Korean name as a proper name.

The session does not offer browser-control tools; no screenshot or interactive viewport/print-layout comparison is claimed. Source and generated-document checks do not establish those browser results.

Factual content follows the existing repository CV; its provenance and the unresolved Drive CV reference are recorded in `content-sources.md`.
