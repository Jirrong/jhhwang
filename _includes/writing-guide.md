Blog posts, research projects, and academic resources use Markdown files. Publications use the [Allan Lab template](https://www.allanlab.org/aboutwebsite.html) data fields; the CV opens as a PDF.

[Research](#add-research) · [Resources](#add-resources) · [Blog](#write-a-post) · [News](#update-news) · [Publications](#add-a-publication) · [CV](#update-the-cv)

## Add a research project
{: #add-research }

<div class="form-group" markdown="0"><a id="new-research-link" data-next-order="{{ site.research | map: 'order' | sort | last | plus: 1 }}" class="btn btn-primary" href="https://github.com/{{ site.repository }}/new/{{ site.github_branch }}/_research?filename=project-title.md">New research project</a> <a class="btn btn-default" href="https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/research-template.md">Research template</a></div>

Each Markdown file in [`_research/`](https://github.com/{{ site.repository }}/tree/{{ site.github_branch }}/_research) becomes one grey rounded box on **Research** and its own project page. The initial two entries are based on the existing CV. Edit a project file to expand its notes, add results, or record progress over time.

1. Choose **New research project** for a pre-filled English template, or copy the full template into `_research/your-project.md`.
2. Fill in `title`, `period`, `summary`, and optional `program`, `institution`, `status`, and `topics`. A larger `order` puts the box nearer the top. The button supplies the next number.
3. Write the project below the closing `---`. Use headings, lists, figures, references, and equations as in a blog post. Keep updating the same file for ongoing work.
4. Change `published: false` to `published: true` and commit when ready. The filename determines the project URL, so keep it stable after publishing.

To attach a poster or other supporting file, upload it to `assets/resources/` and add an optional `files` list using the same format as academic resources below.

## Add course materials, reports, or seminars
{: #add-resources }

<div class="form-group" markdown="0"><a class="btn btn-default" href="https://github.com/{{ site.repository }}/upload/{{ site.github_branch }}/assets/resources">Upload resource files</a> <a id="new-resource-link" data-next-order="{{ site.resources | map: 'order' | sort | last | plus: 1 }}" class="btn btn-primary" href="https://github.com/{{ site.repository }}/new/{{ site.github_branch }}/_resources?filename=course-notes.md">New course material</a> <a id="new-report-link" data-next-order="{{ site.resources | map: 'order' | sort | last | plus: 1 }}" class="btn btn-default" href="https://github.com/{{ site.repository }}/new/{{ site.github_branch }}/_resources?filename=report-title.md">New report</a> <a id="new-seminar-link" data-next-order="{{ site.resources | map: 'order' | sort | last | plus: 1 }}" class="btn btn-default" href="https://github.com/{{ site.repository }}/new/{{ site.github_branch }}/_resources?filename=seminar-title.md">New seminar</a> <a class="btn btn-default" href="https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/resource-template.md">Resource template</a></div>

Resources is the archive for materials you create while taking courses and doing research: lecture notes, assignments, lab reports, project reports, seminar slides, handouts, and supporting code.

1. Upload the PDF, PPTX, notebook, report, or supporting files to [`assets/resources/`](https://github.com/{{ site.repository }}/tree/{{ site.github_branch }}/assets/resources). Use simple filenames such as `organic-chemistry-notes.pdf`.
2. Choose **New course material**, **New report**, or **New seminar** for a matching template. Give the Markdown file a stable name such as `_resources/organic-chemistry-notes.md`.
3. Fill in the title, summary, and topics. `kind` is a free label, such as `Course material`, `Report`, `Seminar`, or `Assignment`. Optional `course` and `term` identify a course and semester; `event` and `event_date` describe a presentation or other context. Larger `order` values appear first.
4. List one or more files under `files`, then add context, contents, and references below the front matter. Local file paths start with `/assets/resources/`; the site adds `/jhhwang` automatically. External HTTPS links are also supported.

```yaml
files:
  - label: "Notes (PDF)"
    url: /assets/resources/organic-chemistry-notes.pdf
  - label: "Report (PDF)"
    url: /assets/resources/course-report.pdf
  - label: "Slides (PPTX)"
    url: /assets/resources/seminar-slides.pptx
  - label: "Supporting code"
    url: https://github.com/your-account/your-repository
```

5. After uploading the real files, set `published: true` and commit. Each resource becomes one grey box with its type, course/event information, file buttons, and a separate description page. Missing local files fail the site check so a published entry does not silently point to a nonexistent upload.

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

## Update news
{: #update-news }

Add entries at the top of [`_data/news.yml`](https://github.com/{{ site.repository }}/edit/{{ site.github_branch }}/_data/news.yml), newest first. Home shows the first three entries briefly; **News** shows every full `headline`. An optional `summary` gives Home a shorter version, while the full headline supports Markdown links.

Use the [news template](https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/news-template.yml) to add a short `title`, stable `id`, and photos. [Upload news photos](https://github.com/{{ site.repository }}/upload/{{ site.github_branch }}/images/news) before adding their paths to `images`. Each news item has its own grey card in the full archive. Home keeps the brief summary and links to that item.

```yaml
- date: "14 November 2026"
  id: your-news-id
  title: "A short news title"
  summary: "A brief announcement for the home page."
  headline: "The complete announcement, with any details and links."
```

## LinkedIn posts
{: #linkedin-posts }

The home-page **LinkedIn** link opens the author's profile. The repository also includes an importer and an automatic sync workflow for original public posts. **Automatic fetching stays inactive until an approved LinkedIn API read token is configured.** A profile URL, ordinary LinkedIn login, or `w_member_social` posting permission does not grant access to read personal posts.

See the [LinkedIn sync setup](https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/linkedin-sync.md) for the required approved `r_member_social` permission, repository secret, author identifier, and offline JSON import command. Never commit an access token or session cookie. Imported posts keep their original text, date, images, and source link; repeated runs avoid duplicates. Videos and documents remain linked to the original post.

## Add a publication
{: #add-a-publication }

The Publications page keeps the original Allan Lab data fields. Papers appear once in full-width cards using the same body geometry as Research. The journal list remains empty until you add your own paper.

1. Open the [publication template](https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/publication-template.yml).
2. Copy an entry into the [publication data file](https://github.com/{{ site.repository }}/edit/{{ site.github_branch }}/_data/publist.yml). For the first entry, replace the empty `[]` list.
3. Fill in the title, authors, citation, and link. Leave `published: false` while editing, then set it to `true` to display the entry.
4. Set `highlight: 1` to add a **Selected** badge; `highlight: 0` uses a standard card. Each paper is listed once.
5. `description` is a short summary. The optional `abstract` holds full text and starts collapsed behind an **Abstract — Read** control. `news1` and `news2` remain supported for short notes.
6. Upload a photo or graphical abstract to `images/pubpic/`, then use `images` as shown below. The legacy `image` filename field still works.

An image and link are optional; missing fields do not create broken placeholders.

### Add a conference presentation

The **Conferences** section appears below Publications. Add an entry to [`_data/conferences.yml`](https://github.com/{{ site.repository }}/edit/{{ site.github_branch }}/_data/conferences.yml), using the [conference template](https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/docs/conference-template.yml). Keep the newest meeting first. The title, authors, dates, poster/talk type, session, distinction, abstract number, and meeting link can be edited independently. `published: false` hides a draft entry. Conference abstracts and posters stay separate from journal publications.

Conference entries also support `abstract` and `images`. [Upload conference images](https://github.com/{{ site.repository }}/upload/{{ site.github_branch }}/images/conferences) first. `abstract_number` identifies a submission; `abstract` is its actual text. A missing abstract does not create an empty disclosure.

### Images, graphical abstracts, and full abstracts

The same image format works for News, Research, Publications, and Conferences:

```yaml
images:
  - file: /images/pubpic/your-graphical-abstract.png
    alt: "Describe the reaction scheme or scientific result."
    kind: graphical
    caption: "An optional figure caption."
  - file: /images/pubpic/your-photo.jpg
    alt: "Describe the photograph."
    kind: photo
    caption: ""
abstract: >-
  Paste the full abstract here. It is collapsed initially and opens when
  a reader chooses Abstract. Paragraphs and Markdown emphasis are supported.
```

Use the matching folder: `images/news/`, `images/research/`, `images/pubpic/`, or `images/conferences/`. Add more `images` items for a gallery. Every new image requires descriptive `alt` text. Images keep their complete aspect ratio, and clicking opens the original in a new tab; diagrams are not cropped. `kind: graphical` adds a Graphical abstract caption label. Image captions are plain text.

Full abstracts are optional on paper and conference records. Use `|` or `>-` YAML text blocks for long text and blank lines for separate paragraphs. Math uses the same `$...$` and `$$...$$` notation as the blog. The Abstract control works without JavaScript, including keyboard navigation. Preview examples are not published as real papers or news.

## Update the CV
{: #update-the-cv }

The **CV** menu opens the PDF in a new tab using the browser's preferred PDF viewer. An enabled Adobe Acrobat extension can handle it when configured as the default PDF viewer; the site does not select or install browser extensions. Replace `assets/pdf/Jiho_Hwang_CV.pdf` with an updated PDF to keep every CV link working. Deployments preserve this file and never regenerate it automatically.

The CV is the author's uploaded original, preserved exactly as supplied. Its content, layout, fonts, and metadata are not generated from website data. Replacing it requires an author-supplied PDF; maintainers should follow the original-file verification steps in the [repository README](https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/README.md#cv-viewer).

[Read the blog →]({{ '/blog/' | relative_url }})

{% include notebook-math.html %}
<script src="{{ '/assets/js/site.js' | relative_url }}" defer></script>
