---
title: Resources
layout: notebook
notebook_class: record-index
excerpt: "Seminar slides, handouts, and supporting materials by Jiho Hwang."
permalink: /resources/
lang: en
---

# Resources

Seminar slides, handouts, and supporting materials.

<div class="record-stack" markdown="0">
{% assign materials = site.resources | where_exp: 'resource', 'resource.published != false' | sort: 'order' | reverse %}
{% for resource in materials %}
<article class="well record-card resource-card" aria-labelledby="resource-{{ forloop.index }}">
  <div class="record-heading">
    <h2 id="resource-{{ forloop.index }}"><a href="{{ resource.url | relative_url }}">{{ resource.title | escape }}</a></h2>
    {% if resource.kind and resource.kind != '' %}<span class="label label-default">{{ resource.kind | escape }}</span>{% endif %}
  </div>
  {% include resource-meta.html record=resource %}
  <p class="record-summary">{{ resource.summary | escape }}</p>
  {% include record-topics.html topics=resource.topics %}
  {% include record-files.html files=resource.files %}
  <p class="record-read"><a href="{{ resource.url | relative_url }}">Notes and details <span aria-hidden="true">→</span><span class="sr-only">: {{ resource.title | escape }}</span></a></p>
</article>
{% else %}
<div class="well record-card resource-empty">
  <h2>Seminar materials</h2>
  <p>No seminar materials have been published yet.</p>
</div>
{% endfor %}
</div>
