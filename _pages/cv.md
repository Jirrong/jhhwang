---
title: "Curriculum Vitae"
layout: gridlay
excerpt: "Education, research experience, honors, and presentations of Jiho Hwang."
permalink: /cv/
---

# Curriculum Vitae

<div class="cv-record" markdown="0">
<div class="row"><div class="col-sm-9"><h2>{{ site.data.cv.identity.name | escape }} <small lang="ko">{{ site.data.cv.identity.korean_name | escape }}</small></h2><p>{{ site.data.cv.identity.role | escape }}<br>{{ site.data.cv.identity.institution | escape }}</p><p><a href="mailto:{{ site.data.cv.identity.email | escape }}">{{ site.data.cv.identity.email | escape }}</a> · <a href="{{ site.data.cv.identity.github }}">GitHub</a></p></div><div class="col-sm-3 cv-tools"><p><button type="button" class="btn btn-default btn-sm" id="print-cv" hidden>Print / Save as PDF</button></p></div></div>
<p class="cv-tools"><a href="#education">Education</a> · <a href="#research-experience">Research experience</a> · <a href="#honors">Honors</a> · <a href="#presentations">Presentations</a> · <a href="#skills">Skills</a></p>
<section id="education"><h2>Education</h2>{% for entry in site.data.cv.education %}<div class="row"><div class="col-sm-3"><p class="text-muted">{{ entry.dates | escape }}</p></div><div class="col-sm-9"><h4>{{ entry.degree | escape }}</h4><p>{{ entry.institution | escape }}<br><span class="text-muted">{{ entry.detail | escape }}</span></p></div></div>{% endfor %}</section>
<section id="research-experience"><h2>Research Experience</h2>{% for entry in site.data.cv.research_experience %}<div class="row"><div class="col-sm-3"><p class="text-muted">{{ entry.dates | escape }}</p></div><div class="col-sm-9"><h4>{{ entry.title | escape }}</h4><p>{{ entry.institution | escape }}</p><ul>{% for point in entry.points %}<li>{{ point | escape }}</li>{% endfor %}</ul></div></div>{% endfor %}</section>
<section id="honors"><h2>Honors and Awards</h2>{% for award in site.data.cv.awards %}<div class="row"><div class="col-sm-3"><p class="text-muted">{{ award.date | escape }}</p></div><div class="col-sm-9"><h4>{{ award.title | escape }}</h4><p>{{ award.organization | escape }}</p></div></div>{% endfor %}</section>
<section id="presentations"><h2>Conference Presentations</h2>{% for work in site.data.cv.presentations %}<h4>{{ work.title | escape }}</h4><p>{{ work.authors | escape }}</p><ul>{% for event in work.events %}<li><strong>{{ event.meeting | escape }}</strong>, {{ event.date | escape }}.<br>{{ event.detail | escape }}</li>{% endfor %}</ul>{% endfor %}</section>
<section id="activities"><h2>Activities and Affiliations</h2>{% for activity in site.data.cv.activities %}<div class="row"><div class="col-sm-3"><p class="text-muted">{{ activity.dates | escape }}</p></div><div class="col-sm-9"><h4>{{ activity.title | escape }}</h4><p>{{ activity.institution | escape }}</p></div></div>{% endfor %}<ul>{% for affiliation in site.data.cv.affiliations %}<li>{{ affiliation | escape }}</li>{% endfor %}</ul></section>
<section id="skills"><h2>Skills</h2>{% for skill in site.data.cv.skills %}<div class="row"><div class="col-sm-3"><p><strong>{{ skill.label | escape }}</strong></p></div><div class="col-sm-9"><p>{{ skill.items | escape }}</p></div></div>{% endfor %}</section>
</div>
<link rel="stylesheet" media="print" href="{{ '/assets/css/cv-print.css' | relative_url }}">
<script src="{{ '/assets/js/cv.js' | relative_url }}" defer></script>
