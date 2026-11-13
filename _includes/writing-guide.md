The blog uses Markdown posts. The publication list and CV use editable data records, following the [Allan Lab template](https://www.allanlab.org/aboutwebsite.html).

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

## Update the CV and research sections
{: #update-the-cv }

Edit the [CV data file](https://github.com/{{ site.repository }}/edit/{{ site.github_branch }}/_data/cv.yml) to update education, research experience, honors, presentations, skills, and affiliations. The home and research pages use the same record. The CV's **Print / Save as PDF** button opens the browser's print dialog.

[Read the blog →]({{ '/blog/' | relative_url }})

{% include notebook-math.html %}
<script src="{{ '/assets/js/site.js' | relative_url }}" defer></script>
