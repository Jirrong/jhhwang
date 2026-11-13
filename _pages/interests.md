---
title: Research & interests
layout: page
eyebrow: MOLECULES, MECHANISMS & METHODS
subtitle: The questions I’m learning to ask.
permalink: /interests/
wide: true
---
<p class="research-intro">My interests connect synthetic organic chemistry with tools for understanding molecular structure, reactivity, and reaction energetics.</p>
<div class="research-detail-list">{% for area in site.data.research %}<section class="research-detail" id="area-{{ area.number }}"><span class="item-number">{{ area.number }}</span><div><h2>{{ area.title }}</h2><p class="research-subtitle">{{ area.subtitle }}</p><p>{{ area.description }}</p><div class="tag-list">{% for topic in area.topics %}<span class="tag">{{ topic }}</span>{% endfor %}</div></div></section>{% endfor %}</div>
<section class="content-section"><p class="eyebrow">SELECTED EXPERIENCE</p><h2>Learning through research.</h2><div class="timeline"><div class="timeline-item"><p class="timeline-date">APR 2025 — JAN 2026</p><div><h3>Creative R&E</h3><p class="timeline-place">Gyeonggi Science High School · KOFAC</p><p>Computational investigation of organic reaction mechanisms and thermochemistry using activation/strain analysis, energy decomposition analysis, and QTAIM.</p></div></div><div class="timeline-item"><p class="timeline-date">MAR — NOV 2024</p><div><h3>Advanced R&E in Chemistry</h3><p class="timeline-place">Gyeonggi Science High School</p><p>Implicit-solvation models, conformational analysis of a sterically constrained molecule, and excited-state calculations with TD-DFT and EOM-CC methods.</p></div></div></div></section>
<div class="inline-callout"><div><h2>Research output</h2><p>Conference contributions and a record of work.</p></div><a class="text-link" href="{{ '/publications/' | relative_url }}">View research output →</a></div>
<p class="quiet-note">Experience details follow the CV currently maintained on this site.</p>
