---
title: Curriculum vitae
layout: page
eyebrow: EDUCATION & EXPERIENCE
subtitle: An academic record, in progress.
permalink: /cv/
---
<div class="cv-toolbar"><p class="quiet-note">CV record · {{ site.data.profile.cv_updated }}</p><div>{% if site.data.profile.cv_pdf != '' %}<a class="button button-primary" href="{{ site.data.profile.cv_pdf | relative_url }}">Download CV ↓</a>{% endif %}<button class="button button-secondary" type="button" data-print-cv hidden>Print / Save as PDF ↗</button></div></div>
<div class="cv-identity"><img src="{{ '/assets/images/jiho-hwang.jpg' | relative_url }}" alt="" width="77" height="103"><div><h2>Jiho Hwang <span lang="ko">황지호</span></h2><p>Chemistry · Seoul National University</p><p><a href="mailto:{{ site.email }}">{{ site.email }}</a> · <a href="{{ site.github_url }}">GitHub ↗</a></p></div></div>
{% assign sections = 'education,experience,awards' | split: ',' %}
{% for section in sections %}<section class="cv-section"><h2>{{ section | capitalize }}</h2>{% for entry in site.data.cv[section] %}<div class="timeline-item"><p class="timeline-date">{{ entry.period }}</p><div><h3>{{ entry.title }}</h3><p class="timeline-place">{{ entry.place }}</p>{% if entry.notes %}<ul>{% for note in entry.notes %}<li>{{ note }}</li>{% endfor %}</ul>{% endif %}</div></div>{% endfor %}</section>{% endfor %}
<section class="cv-section"><h2>Research interests</h2><p>Organic and asymmetric synthesis, synthetic methodology development, natural-product synthesis, organometallic catalysis, and computational chemistry (DFT, coupled cluster, EDA, QTAIM).</p></section>
<section class="cv-section"><h2>Skills</h2><dl class="cv-skills">{% for skill in site.data.cv.skills %}<dt>{{ skill.label }}</dt><dd>{{ skill.value }}</dd>{% endfor %}</dl></section>
<section class="cv-section"><h2>Conference contributions</h2><p><strong>Uncovering origins of the reaction driving force in an Aromatic Ring-Opening/Ring-Closing Metathesis cascade</strong><br>Jiho Hwang, Seungchan Hong, Doyoung Kim, and Jaehoon Min<br>SciMeetings / ACS Spring Meeting 2026 · ORGN poster · Sci-Mix selection.</p><p>Korean Chemical Society Fall Conference, September 2025 · Future Chemist Research Presentation (poster).</p><a class="text-link" href="{{ '/publications/' | relative_url }}">Research output →</a></section>
<section class="cv-section"><h2>Professional affiliations</h2><ul>{% for affiliation in site.data.cv.affiliations %}<li>{{ affiliation }}</li>{% endfor %}</ul></section>
