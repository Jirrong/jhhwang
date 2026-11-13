# Jiho Hwang's academic website

A personal academic website based on the [Allan Lab template](https://www.allanlab.org/aboutwebsite.html). The existing fonts, palette, and Bootstrap foundation are retained. [Junseo Lee's site](https://harris-junseo-lee.github.io/) informed the compact profile, direct CV link, and restrained academic presentation; its biography, affiliations, papers, and CV are not reused.

## CV download

The navigation's **CV** link and the profile CV link download the same-origin file `assets/pdf/Jiho_Hwang_CV.pdf`. The old `/cv/` address is a compatibility download page with a normal fallback link. There is no full HTML CV to maintain.

To use an updated/original CV, replace that PDF in the repository. `cv_pdf` in `_config.yml` specifies its path. Deployments preserve the checked-in document and never regenerate it automatically.

The initial two-page PDF was exported from the existing `_data/cv.yml` record, using the same previously public facts. To explicitly export that record again:

```sh
python3 -m pip install -r scripts/requirements-cv.txt
python3 scripts/build_cv_pdf.py
```

The optional exporter requires DejaVu Serif fonts. It is not part of the publication/deployment pipeline, so uploading an author-supplied PDF will not be overwritten. `_data/cv.yml` remains the factual source for home and research content; keep it consistent with the PDF.

## Layout and blog

An explicit full-width content container fixes pages shrinking to the width of short text. Notebook pages use up to 1360px, with a desktop contents sidebar and a single-column mobile layout. Code, tables, images, and equations remain within the available width. Scoped responsive refinements live in `_sass/_site-layout.scss`, appended to the original theme; no replacement palette or font family is introduced.

Open **Blog → Write a post** or **Guide → New post** for the dated English Markdown template. Commit to `gh-pages` to publish, or use a branch/PR to review first. Posts use `_posts/YYYY-MM-DD-title.md`; a fuller scientific-note template is in `_drafts/academic-post-template.md`.

MathJax, code copying, TOC, tables/footnotes, full-text search, tag filters, and RSS are supported. Node is needed only for development tests. Drafts and `published: false` posts are omitted from the built site/search/feed, while their source remains readable in this public repository. Future-dated posts need a build at or after their date.

## Publications

Copy an entry from [docs/publication-template.yml](docs/publication-template.yml) into `_data/publist.yml` (replace `[]` for the first entry). Fill the fields and set `published: true` when ready. `highlight: 1` enables the original selected-paper card; `highlight: 0` shows the full-list citation only. Optional figure files belong in `images/pubpic/`.

The list starts empty; conference presentations remain in the CV. The source lab's papers and fictional examples are not shown as the author's work.

## Research and resources

**Research** stacks one grey rounded box per Markdown file in `_research/`, with a separate project page for longer notes and updates. The two initial projects come from the repository CV. Copy [docs/research-template.md](docs/research-template.md) to add another; higher `order` values appear first.

**Resources** works the same way using `_resources/`. Upload seminar slides, handouts, or other files to `assets/resources/`, then copy [docs/resource-template.md](docs/resource-template.md). Each record supports multiple local downloads or external HTTP(S) links, a seminar overview, and references. No sample seminar is published.

Open **Site guide** in the footer for pre-filled **New research project** / **New seminar resource** buttons and an upload link. Templates start with `published: false`; change it to `true` when ready. Unpublished entries are omitted from the site and sitemap, while source files and uploaded materials remain public on GitHub. Keep filenames stable to preserve their URLs. The original Research Interests page remains available from Research and the home-page topic links.

## Build and validate

```sh
bundle install
python3 scripts/check_template.py
python3 scripts/check_cv_pdf.py
bundle exec ruby scripts/check_content.rb
bundle exec ruby scripts/check_publication_rendering.rb
bundle exec ruby scripts/check_records.rb
bundle exec ruby scripts/check_record_rendering.rb
bundle exec jekyll build --safe --strict_front_matter --trace
python3 scripts/check_site.py _site
npm ci
npm test
```

The theme guard checks original theme bases against `f25f182c00dbd1e625bb355571cc352bb9f40612`, with the explicitly approved Sass append recorded in `scripts/template-baseline.json`. Production uses the existing GitHub Pages `gh-pages` branch and `/jhhwang` base path. Content provenance is in `docs/content-sources.md`.
