---
title: Research
layout: notebook
notebook_class: record-index
excerpt: "Research projects in reaction mechanisms, thermochemistry, and computational chemistry."
permalink: /research/
lang: en
---

# Research

Projects in reaction mechanisms, thermochemistry, and computational chemistry.

[Research interests and background →]({{ '/interests/' | relative_url }})

<div class="record-stack" markdown="0">
{% assign projects = site.research | where_exp: 'project', 'project.published != false' | sort: 'order' | reverse %}
{% for project in projects %}
<article class="well record-card research-card" aria-labelledby="project-{{ forloop.index }}">
  <div class="record-heading">
    <h2 id="project-{{ forloop.index }}"><a href="{{ project.url | relative_url }}">{{ project.title | escape }}</a></h2>
    {% if project.status and project.status != '' %}<span class="label label-default">{{ project.status | escape }}</span>{% endif %}
  </div>
  <p class="text-muted record-meta">{{ project.period | escape }}{% if project.program and project.program != '' %}<br>{{ project.program | escape }}{% endif %}{% if project.institution and project.institution != '' %} · {{ project.institution | escape }}{% endif %}</p>
  <p class="record-summary">{{ project.summary | escape }}</p>
  {% include record-topics.html topics=project.topics %}
  <p class="record-read"><a href="{{ project.url | relative_url }}">Read project <span aria-hidden="true">→</span><span class="sr-only">: {{ project.title | escape }}</span></a></p>
</article>
{% else %}
<div class="well record-card"><p>No research projects have been published yet.</p></div>
{% endfor %}
</div>
