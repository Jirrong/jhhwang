---
title: Research
layout: notebook
notebook_class: record-index research-page
excerpt: "Research projects in reaction mechanisms, thermochemistry, and computational chemistry."
permalink: /research/
lang: en
---

<header class="page-heading" markdown="0">
  <h1>Research</h1>
  <p class="page-lede">Projects in reaction mechanisms, thermochemistry, and computational chemistry.</p>
  <p class="page-tools"><a href="{{ '/interests/' | relative_url }}">Research interests and background <span aria-hidden="true">→</span></a></p>
</header>

<div class="record-stack" markdown="0">
{% assign projects = site.research | where_exp: 'project', 'project.published != false' | sort: 'order' | reverse %}
{% for project in projects %}
<article class="well record-card research-card" aria-labelledby="project-{{ forloop.index }}">
  <div class="record-main">
    <div class="record-topline"><span>{{ project.period | escape }}</span>{% if project.status and project.status != '' %}<span class="record-badge status-{{ project.status | slugify }}">{{ project.status | escape }}</span>{% endif %}</div>
    <h2 id="project-{{ forloop.index }}" class="record-title"><a href="{{ project.url | relative_url }}">{{ project.title | escape }}</a></h2>
    <p class="record-context">{% if project.program and project.program != '' %}<strong>{{ project.program | escape }}</strong>{% endif %}{% if project.institution and project.institution != '' %}<span>{% if project.program and project.program != '' %} · {% endif %}{{ project.institution | escape }}</span>{% endif %}</p>
    <p class="record-body record-summary">{{ project.summary | escape }}</p>
    {% include record-topics.html topics=project.topics %}
    {% include entry-media.html record=project folder='/images/research/' %}
    <div class="record-links"><a href="{{ project.url | relative_url }}">Project notes <span aria-hidden="true">→</span><span class="sr-only">: {{ project.title | escape }}</span></a></div>
  </div>
</article>
{% else %}
<p class="empty-note">No research projects have been published yet.</p>
{% endfor %}
</div>
