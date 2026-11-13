---
title: "Research Interests"
layout: textlay
excerpt: "Organic synthesis, reaction mechanisms, and computational chemistry."
permalink: /interests/
---

# Research Interests

My interests lie in organic synthesis and the use of computation to understand molecular structure and reactivity.

{% for area in site.data.cv.research_interests %}
## {{ area.title }}
{: #{{ area.id }} }

{{ area.description }}
{% endfor %}

## Research Experience

{% for project in site.data.cv.research_experience %}
### {{ project.title }}

**{{ project.institution }}**<br>
{{ project.dates }}

{% for point in project.points %}
- {{ point }}
{% endfor %}
{% endfor %}

## Methods and Software

My research experience includes activation/strain analysis, energy decomposition analysis, QTAIM, conformational analysis, and excited-state calculations with TD-DFT and EOM-CC methods. The software listed in my CV includes Gaussian, ORCA, CFOUR, and Multiwfn; I also use Python and C++.

## Conference Presentations

My conference presentations include work on the driving force of an aromatic ring-opening/ring-closing metathesis cascade.

<p><a href="{{ site.cv_pdf | relative_url }}" download="Jiho_Hwang_CV.pdf" type="application/pdf">Download the CV (PDF)</a> for the presentation record.</p>

[Contact me](mailto:{{ site.email }})
