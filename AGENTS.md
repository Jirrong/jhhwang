# Keep the Allan Lab theme; personalize its content

The user chose the Allan Lab visual foundation, then explicitly requested a directly downloadable CV PDF, wider blog pages, and overall layout refinement using https://harris-junseo-lee.github.io/ as a reference. Follow these latest requests while retaining the existing palette, fonts, factual content, English blog, and editable publications.

- Keep the original palette, fonts, and Bootstrap foundation. Responsive width, spacing, profile presentation, and article-layout improvements are now explicitly authorized. Keep these in the scoped `_sass/_site-layout.scss` extension rather than replacing the theme.
- Refine profile/research content using the existing components. CV content is delivered as a PDF, not a full HTML page. Personalize wording without copying the reference author's facts, institutions, papers, or CV.
- The original design baseline is commit `f25f182c00dbd1e625bb355571cc352bb9f40612`. Protected source files and their Git blob identities are recorded in `scripts/template-baseline.json`.
- The CV menu and profile CV links must point directly to the same-origin PDF with a download attribute. `/cv/` is only a compatibility download page. Do not reintroduce a long HTML CV.
- The PDF may be replaced by an author-supplied original. Do not regenerate or overwrite it automatically in the deployment pipeline. The optional builder can export the current CV data when explicitly run.
- Blog posts, controls, templates, status messages, and writing/publication instructions must default to English. Keep the original Bootstrap navigation and footer structure.
- News belongs below the Home content as a brief list of the latest three entries. The complete list has its own `/news/` page and navigation link; `/allnews.html` remains a compatibility address. Keep `_data/news.yml` as their shared source, newest entries first.
- Run `python3 scripts/check_template.py` and the relevant build/functional checks before publishing changes.
- Content changes must be based on the user's sources. Use the existing repository CV for now; its data is recorded in `_data/cv.yml`. The intended Google Drive CV has not been identified. Do not invent or substitute other people's details, papers, degrees, or positions.
- Keep conference presentations distinct from journal publications. Publications data may remain empty until the user supplies an entry; preserve the Allan Lab YAML field names and provide a non-public template.
