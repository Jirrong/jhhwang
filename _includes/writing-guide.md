Blog posts, research projects, and seminar resources use Markdown files. Publications use the [Allan Lab template](https://www.allanlab.org/aboutwebsite.html) data fields; the CV is a downloadable PDF.

[Research](#add-research) · [Resources](#add-resources) · [Blog](#write-a-post) · [Publications](#add-a-publication) · [CV](#update-the-cv)

## Add a research project
{: #add-research }

<div class="form-group" markdown="0"><a id="new-research-link" data-next-order="{{ site.research | map: 'order' | sort | last | plus: 1 }}" class="btn btn-primary" href="https://github.com/{{ site.repository }}/new/{{ site.github_branch }}/_research?filename=project-title.md">New research project</a> <a class="btn btn-default" href="https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/research-template.md">Research template</a></div>

Each Markdown file in [`_research/`](https://github.com/{{ site.repository }}/tree/{{ site.github_branch }}/_research) becomes one grey rounded box on **Research** and its own project page. The initial two entries are based on the existing CV. Edit a project file to expand its notes, add results, or record progress over time.

1. Choose **New research project** for a pre-filled English template, or copy the full template into `_research/your-project.md`.
2. Fill in `title`, `period`, `summary`, and optional `program`, `institution`, `status`, and `topics`. A larger `order` puts the box nearer the top. The button supplies the next number.
3. Write the project below the closing `---`. Use headings, lists, figures, references, and equations as in a blog post. Keep updating the same file for ongoing work.
4. Change `published: false` to `published: true` and commit when ready. The filename determines the project URL, so keep it stable after publishing.

To attach a poster or other supporting file, upload it to `assets/resources/` and add an optional `files` list using the same format as seminar resources below.

## Add seminar resources
{: #add-resources }

<div class="form-group" markdown="0"><a class="btn btn-default" href="https://github.com/{{ site.repository }}/upload/{{ site.github_branch }}/assets/resources">Upload seminar files</a> <a id="new-resource-link" data-next-order="{{ site.resources | map: 'order' | sort | last | plus: 1 }}" class="btn btn-primary" href="https://github.com/{{ site.repository }}/new/{{ site.github_branch }}/_resources?filename=seminar-title.md">New seminar resource</a> <a class="btn btn-default" href="https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/resource-template.md">Resource template</a></div>

1. Upload your PDF, PPTX, handout, or supporting files to [`assets/resources/`](https://github.com/{{ site.repository }}/tree/{{ site.github_branch }}/assets/resources). Use simple filenames such as `reaction-mechanisms-seminar.pdf`.
2. Choose **New seminar resource**. Give the Markdown file a stable name such as `_resources/reaction-mechanisms-seminar.md`.
3. Fill in the title, summary, topics, and optional `event` and `event_date` (for example, `"November 2026"`). Set `kind` to `Seminar`, `Reading group`, or another useful label. Larger `order` values appear first.
4. List one or more files under `files`, then add an overview, outline, and references below the front matter. Local file paths start with `/assets/resources/`; the site adds `/jhhwang` automatically. External HTTPS links are also supported.

```yaml
files:
  - label: "Slides (PDF)"
    url: /assets/resources/reaction-mechanisms-seminar.pdf
  - label: "Presentation (PPTX)"
    url: /assets/resources/reaction-mechanisms-seminar.pptx
  - label: "Supporting code"
    url: https://github.com/your-account/your-repository
```

5. After uploading the real files, set `published: true` and commit. One resource becomes one grey box with download buttons and a separate notes page. Missing local files fail the site check so a published entry does not silently point to a nonexistent upload.

Research and resource files with `published: false` are omitted from the site and sitemap. Their source and any uploaded files remain readable in this public repository. Templates in `docs/` are excluded from the site. Resources starts empty until you add your own materials.

## Write a post
{: #write-a-post }

<div class="form-group" markdown="0"><a id="new-post-link" class="btn btn-primary" href="https://github.com/{{ site.repository }}/new/{{ site.github_branch }}/_posts?filename={{ site.time | date: '%Y-%m-%d' }}-your-title.md">New post</a> <a class="btn btn-default" href="https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/_drafts/academic-post-template.md">Full post template</a></div>

The **New post** button opens the GitHub editor with a dated English template. Sign in with an account that can write to this repository.

Use a filename such as `_posts/2026-11-13-your-title.md`. Change the title, description, tags, and body. The filename's date and the `date` field should agree.

```yaml
---
title: "A question from a paper"
date: 2026-11-13 00:00:00 +0900
description: "A short introduction to the question."
categories: [Paper notes]
tags: [Organic chemistry, Reaction mechanisms]
lang: en
math: true
toc: true
---
```

Write the post below the front matter. `categories` gives a broad topic; `tags` supports more specific filtering. `##` and `###` headings generate a table of contents. The blog list, search index, and RSS feed update when the site builds.

### Equations, code, and references

Inline math uses `$\Delta G$`. Display equations use:

```tex
$$
\Delta G = \Delta H - T\Delta S
$$
```

$$
\Delta G = \Delta H - T\Delta S
$$

Use fenced code blocks with a language such as `python`, `bash`, or `cpp`. Posts provide a code-copy button. Tables, blockquotes, and footnotes are supported. Add references or DOI links where appropriate.

Upload figures to `images/posts/` and use a path relative to the site's base URL:

{% raw %}
```liquid
![Describe what the figure shows]({{ '/images/posts/figure.png' | relative_url }})
```
{% endraw %}

### Publish or keep a draft

Choose **Commit changes** in GitHub. A commit to `gh-pages` rebuilds the site; a new branch and pull request lets you review the change first. Existing posts can be edited in the [posts folder](https://github.com/{{ site.repository }}/tree/{{ site.github_branch }}/_posts).

Use `_drafts/` or `published: false` to omit a post from the built site, search, and RSS. This is a public repository, so draft source files are still readable on GitHub. A future-dated post is hidden until its date, but publishing then requires another build; GitHub Pages does not automatically schedule that build.

## Add a publication
{: #add-a-publication }

The Publications page keeps the original Allan Lab fields and highlighted-paper layout. It starts with an empty list, so no sample paper is shown as your work.

1. Open the [publication template](https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/publication-template.yml).
2. Copy an entry into the [publication data file](https://github.com/{{ site.repository }}/edit/{{ site.github_branch }}/_data/publist.yml). For the first entry, replace the empty `[]` list.
3. Fill in the title, authors, citation, and link. Leave `published: false` while editing, then set it to `true` to display the entry.
4. Set `highlight: 1` to show a paper in **Selected Publications** as well as the full list. `highlight: 0` shows it in the full list only.
5. An optional `image` is a filename in `images/pubpic/`. `description`, `news1`, and `news2` provide the original template's summary and news fields.

An image and link are optional; missing fields do not create broken placeholders. List conference presentations in the CV separately from journal publications.

## Update the CV
{: #update-the-cv }

The **CV** menu downloads the PDF directly. Replace `assets/pdf/Jiho_Hwang_CV.pdf` with your own updated PDF to keep every CV link working. Deployments preserve this file and never regenerate it automatically.

The initial PDF was exported from the existing website CV record. An optional builder, `scripts/build_cv_pdf.py`, can export that record again when explicitly run. `_data/cv.yml` continues to hold the factual profile and research information used on the site; keep it consistent with your PDF.

[Read the blog →]({{ '/blog/' | relative_url }})

{% include notebook-math.html %}
<script src="{{ '/assets/js/site.js' | relative_url }}" defer></script>
