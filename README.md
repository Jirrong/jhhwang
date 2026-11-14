# Jiho Hwang's academic website

A personal academic website based on the [Allan Lab template](https://www.allanlab.org/aboutwebsite.html). The restrained palette and Bootstrap foundation are retained. The author's requested typography refinement uses self-hosted Source Sans 3 for body/UI and Source Serif 4 for major headings; card titles stay in the body family. Font licenses are in `fonts/licenses/`. [Design notes](docs/academic-design.md) explain the reference sites and shared layout.

## CV viewer

The navigation's **CV** link and profile CV link open the same-origin file `assets/pdf/Jiho_Hwang_CV.pdf` in a new tab. They have no forced-download attribute or automatic-download script. The browser uses its configured PDF viewer, including an Adobe Acrobat extension when enabled as the default. The old `/cv/` address remains a small page with an Open PDF link. There is no full HTML CV to maintain.

To use an updated/original CV, replace that PDF in the repository. `cv_pdf` in `_config.yml` specifies its path. Deployments preserve the checked-in document and never regenerate it automatically.

The initial two-page PDF was exported from the existing `_data/cv.yml` record, using the same previously public facts. To explicitly export that record again:

```sh
python3 -m pip install -r scripts/requirements-cv.txt
python3 scripts/build_cv_pdf.py
```

The optional exporter requires DejaVu Serif fonts. It is not part of the publication/deployment pipeline, so uploading an author-supplied PDF will not be overwritten. `_data/cv.yml` remains the factual source for home and research content; keep it consistent with the PDF.

## Layout and blog

All page layouts share a 1360px maximum container, including Home, Publications, and notebook pages. Research, Publications, Conferences, and News also share the same full-width card, inner padding, and body type. Home has a portrait aligned to the right content edge, clear section dividers, and balanced visible logo heights. Grey cards use compact line spacing and separate title, author/context, metadata, and supporting material. The navbar title is **Personal Webpage of Jiho Hwang**; section links use a left-to-right background highlight on hover or keyboard focus, with a current-section indicator. The menu collapses at tablet widths to fit the longer title and honors reduced-motion preferences.

Notebook pages keep a desktop contents sidebar and a single-column mobile layout. Code, tables, images, and equations remain within the available width. Scoped responsive refinements live in `_sass/_site-layout.scss` and `_sass/_academic-ui.scss`, appended to the original theme. Font loading is local, with no Google Fonts request.

Open **Blog → Write a post** or **Guide → New post** for the dated English Markdown template. Commit to `gh-pages` to publish, or use a branch/PR to review first. Posts use `_posts/YYYY-MM-DD-title.md`; a fuller scientific-note template is in `_drafts/academic-post-template.md`.

MathJax, code copying, TOC, tables/footnotes, full-text search, tag filters, and RSS are supported. Node is needed only for development tests. Drafts and `published: false` posts are omitted from the built site/search/feed, while their source remains readable in this public repository. Future-dated posts need a build at or after their date.

## Publications

Copy an entry from [docs/publication-template.yml](docs/publication-template.yml) into `_data/publist.yml` (replace `[]` for the first entry). Fill the fields and set `published: true` when ready. Every paper appears once in a full-width card; `highlight: 1` adds a Selected badge. Optional figure files belong in `images/pubpic/`. Both papers and conferences accept `images` galleries and an `abstract` Markdown text block. Abstracts start closed and use a native disclosure that works with keyboard input and without JavaScript. The legacy single `image` filename still works.

Each image record has a local `file`, descriptive `alt`, optional `caption`, and optional `kind: photo|graphical`. Figures are displayed whole and link to the full-size original. Missing images or abstracts produce no empty frames or controls. The Site guide includes the complete authoring format; upload validation catches missing files and missing alt text.

The journal list starts empty. The separate **Conferences** section below it uses `_data/conferences.yml`, with a template in `docs/conference-template.yml`. It contains the sourced ACS Spring 2026 and KCS Fall 2025 poster records. The source lab's papers and fictional examples are not shown as the author's work.

## Profile and LinkedIn

The smaller portrait and both institution logos are the author's original uploaded files. The profile and current IMC Lab research entry use the author's supplied LinkedIn screenshots. Historical CV facts remain sourced separately; deployments preserve the checked-in CV PDF.

The home-page LinkedIn link points to `jirrong0116`. `scripts/sync_linkedin.py` and the **Sync LinkedIn posts** workflow can mirror original public post text and images with deduplication and source links. Live fetching remains inactive until approved `r_member_social` access and repository credentials are configured. See [docs/linkedin-sync.md](docs/linkedin-sync.md) for setup, limitations, and offline API JSON imports. Posting-only LinkedIn permissions are insufficient.

## Research and resources

**Research** stacks one grey rounded box per Markdown file in `_research/`, with a separate project page for longer notes and updates. The two historical projects come from the repository CV; the current IMC Lab project uses the author's LinkedIn screenshots. Copy [docs/research-template.md](docs/research-template.md) to add another; higher `order` values appear first. Optional `images` use the shared media format.

**Resources** uses `_resources/` for course notes, assignments, reports, seminar slides, handouts, and supporting code. Upload files to `assets/resources/`, then copy [docs/resource-template.md](docs/resource-template.md). Each record supports a type (`kind`), optional `course`/`term` and event information, multiple downloads or external HTTP(S) links, a description, and references. No sample material is published.

Open **Site guide** in the footer for pre-filled **New research project**, **New course material**, **New report**, and **New seminar** buttons, plus an upload link. Templates start with `published: false`; change it to `true` when ready. Unpublished entries are omitted from the site and sitemap, while source files and uploaded materials remain public on GitHub. Keep filenames stable to preserve their URLs. The original Research Interests page remains available from Research and the home-page topic links.

## News

Home uses the full content width, with a brief News list below its main content. The latest three entries come from `_data/news.yml` in file order. Add new entries at the top; use `date`, full Markdown `headline`, and an optional short `summary`. The dedicated `/news/` page and original `/allnews.html` address share the full archive, with one grey card per item. Optional `title`, stable `id`, and `images` add headings, direct links, and photo galleries. Use [docs/news-template.yml](docs/news-template.yml) and upload photos to `images/news/`. Home stays brief and links to each full item; `published: false` omits a draft.

## Build and validate

```sh
bundle install
python3 scripts/check_template.py
python3 scripts/check_cv_pdf.py
python3 -m unittest discover -s tests -p 'test_*.py'
bundle exec ruby scripts/check_content.rb
bundle exec ruby scripts/check_publication_rendering.rb
bundle exec ruby scripts/check_records.rb
bundle exec ruby scripts/check_record_rendering.rb
bundle exec ruby scripts/check_linkedin_rendering.rb
bundle exec jekyll build --safe --strict_front_matter --trace
python3 scripts/check_site.py _site
npm ci
npm test
```

The theme guard checks original theme bases against `f25f182c00dbd1e625bb355571cc352bb9f40612`, with the approved Sass append, local font-loading hook, and preload hook recorded in `scripts/template-baseline.json`. Rendering tests exercise image validation, galleries, initially closed abstracts, missing optional fields, and draft filtering using isolated fixtures. Production uses the existing GitHub Pages `gh-pages` branch and `/jhhwang` base path. Content provenance is in `docs/content-sources.md`.
