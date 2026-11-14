---
title: Publications
layout: notebook
notebook_class: record-index publications-page
excerpt: "Publications and conference presentations by Jiho Hwang."
permalink: /publications/
lang: en
math: true
---

<header class="page-heading" markdown="0">
  <h1>Publications</h1>
  <p class="page-lede">Journal publications and conference presentations.</p>
  <nav class="section-nav" aria-label="Publication sections"><a href="#full-list-of-publications">Publications</a><a href="#conferences">Conferences</a></nav>
</header>

<div markdown="0">
{% assign publications = site.data.publist | where_exp: 'paper', 'paper.published != false' %}
<section id="full-list-of-publications" class="page-section" aria-labelledby="publications-heading">
  <header class="section-heading"><h2 id="publications-heading">Publications</h2><span class="section-count" aria-label="{{ publications.size }} publications">{{ publications.size }}</span></header>
  <div class="record-stack">
    {% for paper in publications %}{% include publication-card.html paper=paper %}{% else %}<p class="empty-note">No journal publications listed yet.</p>{% endfor %}
  </div>
</section>

{% assign conferences = site.data.conferences | where_exp: 'entry', 'entry.published != false' %}
<section id="conferences" class="page-section" aria-labelledby="conferences-heading">
  <header class="section-heading"><h2 id="conferences-heading">Conferences</h2><span class="section-count" aria-label="{{ conferences.size }} conference presentations">{{ conferences.size }}</span></header>
  <div class="record-stack">{% for conference in conferences %}{% include conference-card.html conference=conference %}{% else %}<p class="empty-note">No conference presentations listed yet.</p>{% endfor %}</div>
</section>
</div>

{% include notebook-math.html %}
<script src="{{ '/assets/js/entry-details.js' | relative_url }}" defer></script>
