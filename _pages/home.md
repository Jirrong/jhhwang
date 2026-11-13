---
title: "Jiho Hwang"
heading: "Jiho Hwang"
layout: homelay
excerpt: "Jiho Hwang, undergraduate student in Chemistry at Seoul National University."
permalink: /
---

<div class="row home-profile" markdown="0"><div class="col-sm-8"><p>I am an undergraduate student in the <a href="{{ site.data.cv.identity.department_url }}">Department of Chemistry</a> at <a href="https://www.snu.ac.kr/">Seoul National University</a>.</p><p>My interests include organic synthesis, reaction mechanisms, and computational chemistry. My research experience includes computational studies of reaction thermochemistry, molecular conformations, and excited states.</p><p>I graduated from Gyeonggi Science High School, where I worked on chemistry R&amp;E projects.</p><p class="profile-contact"><a href="{{ site.cv_pdf | relative_url }}" download="Jiho_Hwang_CV.pdf" type="application/pdf"><strong>Curriculum Vitae (PDF)</strong></a><br><a href="mailto:{{ site.email }}">{{ site.email }}</a> · <a href="{{ site.data.cv.identity.github }}">GitHub</a></p></div><div class="col-sm-4"><img class="img-responsive profile-photo" src="{{ site.data.cv.identity.portrait | relative_url }}" alt="Jiho Hwang" width="354" height="472"></div></div>

## Research Interests

<ul class="home-research-list" markdown="0">{% for area in site.data.cv.research_interests %}<li><a href="{{ '/interests/' | relative_url }}#{{ area.id }}"><strong>{{ area.title }}</strong></a> — {{ area.description }}</li>{% endfor %}</ul>

[Research interests and experience →]({{ '/interests/' | relative_url }})

## Recent Posts

<ul class="list-unstyled home-posts" markdown="0">{% for post in site.posts limit:3 %}<li><a href="{{ post.url | relative_url }}"><strong>{{ post.title }}</strong></a><small class="text-muted post-date">{{ post.date | date: '%B %-d, %Y' }}</small><p>{{ post.description | default: post.excerpt | strip_html | normalize_whitespace | truncate: 180 }}</p></li>{% endfor %}</ul>

[All blog posts →]({{ '/blog/' | relative_url }})
