---
title: "Jiho Hwang"
heading: "Jiho Hwang"
layout: homelay
excerpt: "Jiho Hwang, undergraduate student in Chemistry at Seoul National University."
permalink: /
---

<div class="row" markdown="0"><div class="col-sm-3"><img class="img-responsive" src="{{ site.data.cv.identity.portrait | relative_url }}" alt="Jiho Hwang" width="354" height="472"></div><div class="col-sm-9"><p>{{ site.data.cv.identity.introduction | escape }}</p><p>My research experience includes computational studies of organic reaction mechanisms, thermochemistry, molecular conformations, and excited states.</p><p><a href="{{ '/cv/' | relative_url }}">Curriculum vitae</a> · <a href="mailto:{{ site.email | escape }}">Email</a> · <a href="{{ site.data.cv.identity.github }}">GitHub</a></p></div></div>

## Research Interests

{% for area in site.data.cv.research_interests %}
### [{{ area.title }}]({{ '/interests/' | relative_url }}#{{ area.id }})

{{ area.description }}
{% endfor %}

## Research Experience

{% for project in site.data.cv.research_experience %}
**{{ project.title }}** — {{ project.institution }}<br>
{{ project.dates }}

{{ project.points | first }}
{% endfor %}

[Research interests and experience →]({{ '/interests/' | relative_url }})

## Recent Blog Posts

{% for post in site.posts limit:3 %}
### [{{ post.title }}]({{ post.url | relative_url }})

{{ post.date | date: '%d %B %Y' }}<br>
{{ post.description | default: post.excerpt | strip_html | normalize_whitespace | truncate: 180 }}
{% endfor %}

[All blog posts →]({{ '/blog/' | relative_url }})
