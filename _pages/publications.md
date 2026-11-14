---
title: "Publications"
layout: gridlay
excerpt: "Publications and conference presentations by Jiho Hwang."
permalink: /publications/
---

# Publications

<div markdown="0">
{% assign publications = site.data.publist | where_exp: 'paper', 'paper.published != false' %}
{% assign highlights = publications | where: 'highlight', 1 %}
{% if publications.size == 0 %}
<p>No publications listed.</p>
{% else %}
{% if highlights.size > 0 %}
<h2>Selected Publications</h2>
{% for paper in highlights %}
{% assign parity = forloop.index0 | modulo: 2 %}{% if parity == 0 %}<div class="row">{% endif %}
<div class="col-sm-6 clearfix"><div class="well publication-highlight">
<pubtit>{{ paper.title | escape }}</pubtit>
{% if paper.image and paper.image != '' %}<img src="{{ '/images/pubpic/' | append: paper.image | relative_url }}" class="img-responsive" width="33%" style="float: left" alt="Figure for {{ paper.title | escape }}">{% endif %}
{% if paper.description and paper.description != '' %}<div>{{ paper.description | markdownify }}</div>{% endif %}
<p><em>{{ paper.authors | escape }}</em></p>
{% if paper.link.url and paper.link.url != '' %}<p><strong><a href="{{ paper.link.url | escape }}">{{ paper.link.display | default: 'Read publication' | escape }}</a></strong></p>{% elsif paper.link.display and paper.link.display != '' %}<p>{{ paper.link.display | escape }}</p>{% endif %}
{% if paper.news1 and paper.news1 != '' %}<div class="text-danger">{{ paper.news1 | markdownify }}</div>{% endif %}
{% if paper.news2 and paper.news2 != '' %}<div>{{ paper.news2 | markdownify }}</div>{% endif %}
</div></div>
{% if parity == 1 or forloop.last %}</div>{% endif %}
{% endfor %}
{% endif %}
<h2 id="full-list-of-publications">Full Publication List</h2>
{% for paper in publications %}
<p class="publication-entry"><strong>{{ paper.title | escape }}</strong><br>{{ paper.authors | escape }}{% if paper.link.display and paper.link.display != '' %}<br>{% if paper.link.url and paper.link.url != '' %}<a href="{{ paper.link.url | escape }}">{{ paper.link.display | escape }}</a>{% else %}{{ paper.link.display | escape }}{% endif %}{% elsif paper.link.url and paper.link.url != '' %}<br><a href="{{ paper.link.url | escape }}">Read publication</a>{% endif %}</p>
{% endfor %}
{% endif %}
</div>

<section id="conferences" class="conference-section" aria-labelledby="conferences-heading" markdown="0">
<h2 id="conferences-heading">Conferences</h2>
{% assign conferences = site.data.conferences | where_exp: 'entry', 'entry.published != false' %}
{% for conference in conferences %}
<article class="well record-card conference-card" aria-labelledby="{{ conference.id | escape }}">
  <div class="record-heading">
    <h3 id="{{ conference.id | escape }}">{{ conference.meeting | escape }}</h3>
    <span class="label label-default">{{ conference.type | escape }}</span>
  </div>
  <p class="text-muted record-meta">{{ conference.date | escape }}{% if conference.location and conference.location != '' %} · {{ conference.location | escape }}{% endif %}</p>
  <h4 class="conference-title">{{ conference.title | escape }}</h4>
  <p>{{ conference.authors | escape }}</p>
  {% if conference.session and conference.session != '' %}<p>{{ conference.session | escape }}</p>{% endif %}
  {% if conference.distinction and conference.distinction != '' %}<p><strong>{{ conference.distinction | escape }}</strong></p>{% endif %}
  {% if conference.abstract_number and conference.abstract_number != '' %}<p class="text-muted">Abstract #{{ conference.abstract_number | escape }}</p>{% endif %}
  {% if conference.event_url and conference.event_url != '' %}<p class="record-read"><a href="{{ conference.event_url | escape }}">Meeting information <span aria-hidden="true">→</span></a></p>{% endif %}
</article>
{% else %}
<p>No conference presentations listed.</p>
{% endfor %}
</section>
