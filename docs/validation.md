# Validation

The latest user request is a PDF-first CV and wider, more polished blog/profile layout, with Junseo Lee's site as a reference.

- Original theme bases and fonts are checked against the original commit. The recorded Sass append adds only the authorized responsive/profile/notebook refinements.
- The CV is a real two-page PDF exported from the existing record. Its page count, extracted text, embedded fonts, and rendered pages were inspected locally. Main CV links use the direct same-origin asset and a download attribute; `/cv/` retains a fallback.
- Deployments validate the PDF and preserve it. They never run the optional exporter or overwrite an uploaded original.
- Fourteen Node tests cover search/filter/history behavior, English templates, direct PDF links, the compatibility download, compiled width/responsive rules, code copying, and TOC layout with/without enough headings.
- The Jekyll safe build, all ten HTML routes, local links/anchors, publication rendering, CV data, RSS/search/sitemap, and source exclusions are checked.

Browser-control tools were not offered in this environment. No interactive website viewport or browser-download dialog verification is claimed. The PDF pages were rendered and viewed; responsive website sizing is verified through the compiled stylesheet and DOM contracts.
