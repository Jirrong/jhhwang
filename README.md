# Jiho Hwang's academic website

A personal academic website built from the [Allan Lab template](https://www.allanlab.org/aboutwebsite.html), with its original Bootstrap/Bootswatch typography, colors, navigation, grid, and stylesheets.

The CV has been rebuilt as a chronological academic record. Home, research, and CV content share `_data/cv.yml`; the blog and its authoring tools default to English.

## Update personal information

Edit `_data/cv.yml` for the profile, education, research experience, interests, honors, conference presentations, activities, skills, and affiliations. The home and research summaries update from the same record. The CV has a print-only stylesheet and a **Print / Save as PDF** button; these do not modify the screen theme.

The source is the existing repository CV (record dated 13 February 2026). No other person's Drive CV, journal papers, degrees, or research positions have been substituted. See [content sources](docs/content-sources.md).

## Write a blog post

Open **Blog → Write a post**, or **Guide → New post**. The button opens GitHub's editor with a dated English Markdown template. Commit to `gh-pages` to publish, or use a branch/PR to review first.

Posts use `_posts/YYYY-MM-DD-title.md`. A full scientific-note template is available at `_drafts/academic-post-template.md`. MathJax equations, fenced code and copy buttons, headings/TOC, tables, footnotes, full-text search, tag filters, and RSS are supported. Node is not needed to write or publish.

Draft files and `published: false` posts are omitted from the built site/search/RSS, but the source remains readable in this public repository. Future-dated posts require a build at or after their date; GitHub Pages does not schedule that build automatically.

## Add a publication

1. Copy an entry from [docs/publication-template.yml](docs/publication-template.yml) into `_data/publist.yml` (replace `[]` for the first entry).
2. Fill in `title`, `authors`, and the citation/link. Leave `published: false` while editing; set it to `true` when ready.
3. Use `highlight: 1` for the original selected-paper card as well as the full list, or `highlight: 0` for the full list only.
4. Optional fields are `image`, `description`, `news1`, and `news2`; the original Allan Lab names are retained. Place image files in `images/pubpic/`.

The list starts empty. Conference presentations remain in the CV; template example papers and the source lab's publications are not displayed as the author's work. Full instructions are under **Guide → Add a publication**.

## Build and validate

With Ruby 3.3, Bundler, and Node 22 for development tests:

```sh
bundle install
python3 scripts/check_template.py
bundle exec ruby scripts/check_content.rb
bundle exec ruby scripts/check_publication_rendering.rb
bundle exec jekyll build --safe --strict_front_matter --trace
python3 scripts/check_site.py _site
npm ci
npm test
```

The theme guard preserves 92 original theme/layout files against commit `f25f182c00dbd1e625bb355571cc352bb9f40612`. The explicitly authorized CV and personal-content templates are recorded separately. Do not replace the original screen theme or add a global override stylesheet.

Production uses the existing GitHub Pages `gh-pages` branch and `/jhhwang` base path. `_pages/pictures.md`, copied vacancy downloads, and duplicate research drafts are excluded. Analytics is unconfigured; no source-lab tracking ID is used.
