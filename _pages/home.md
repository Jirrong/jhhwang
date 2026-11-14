---
title: "Jiho Hwang"
heading: "Jiho Hwang"
layout: homelay
excerpt: "Jiho Hwang, undergraduate student in Chemistry at Seoul National University."
permalink: /
---

<div class="row home-profile" markdown="0">
  <div class="col-sm-8">
    <p>I am a first-year undergraduate student in the <a href="{{ site.data.cv.identity.department_url }}">Department of Chemistry</a> at <a href="https://www.snu.ac.kr/">Seoul National University</a>.</p>
    <p>My interests span organic and organometallic chemistry, synthetic methodology, and computational approaches to reaction mechanisms. I enjoy understanding why reactions work the way they do through both experimental and computational approaches.</p>
    <p>I am currently an undergraduate student researcher in the <a href="https://chem.snu.ac.kr/en/research-faculty/faculty/fulltime?mode=view&amp;profidx=65">Inorganic Molecular Conversion Laboratory</a>, advised by Prof. Yunho Lee. My work involves PNP pincer ligands and cobalt complexes for open-shell NO<sub>x</sub> conversion.</p>
    <p class="profile-contact"><a href="{{ site.cv_pdf | relative_url }}" download="Jiho_Hwang_CV.pdf" type="application/pdf"><strong>Curriculum Vitae (PDF)</strong></a><br><a href="mailto:{{ site.email }}">{{ site.email }}</a> · <a href="{{ site.data.cv.identity.github }}">GitHub</a> · <a href="{{ site.data.cv.identity.linkedin }}" rel="me">LinkedIn</a></p>
    {% include home-affiliations.html %}
  </div>
  <div class="col-sm-4"><img class="img-responsive profile-photo" src="{{ site.data.cv.identity.portrait | relative_url }}" alt="Jiho Hwang" width="600" height="847"></div>
</div>

## Research Interests

<ul class="home-research-list" markdown="0">{% for area in site.data.cv.research_interests %}<li><a href="{{ '/interests/' | relative_url }}#{{ area.id }}"><strong>{{ area.title }}</strong></a> — {{ area.description }}</li>{% endfor %}</ul>

[Research projects →]({{ '/research/' | relative_url }}) · [Seminar resources →]({{ '/resources/' | relative_url }})

## Recent Posts

<ul class="list-unstyled home-posts" markdown="0">{% for post in site.posts limit:3 %}<li><a href="{{ post.url | relative_url }}"><strong>{{ post.title | escape }}</strong></a><small class="text-muted post-date">{{ post.date | date: '%B %-d, %Y' }}</small><p>{% if post.linkedin_id %}{{ post.description | normalize_whitespace | truncate: 180 | escape }}{% else %}{{ post.description | default: post.excerpt | strip_html | normalize_whitespace | truncate: 180 }}{% endif %}</p></li>{% endfor %}</ul>

[All blog posts →]({{ '/blog/' | relative_url }})
