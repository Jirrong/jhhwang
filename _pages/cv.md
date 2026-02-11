---
title: "CV"
layout: gridlay
excerpt: "Jiho Hwang's Curriculum Vitae"
sitemap: false
permalink: /cv/
---

# CV (Curriculum Vitae)
<p style="text-align: right; color: gray;"><b>Last Updated on 13 February 2026</b></p>

---

<div class="row" style="margin-top: 2em; display: flex; flex-wrap: wrap; align-items: center;">
  
  <div class="col-sm-4" style="text-align: center; margin-bottom: 20px;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/profile.jpg" 
         style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover; border: 4px solid #eee; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
         alt="Jiho Hwang">
  </div>

  <div class="col-sm-8">
    <h2 style="margin-top: 0; font-weight: bold;">Jiho Hwang (황지호)</h2>
    <p style="font-style: italic; color: #666; font-size: 1.1em; margin-bottom: 15px;">"What we find changes who we become."</p>
    <p style="line-height: 1.6;">Student and Researcher in Chemistry, Materials Science, and Physics at <b>Seoul National University</b>.</p>
    
    <style>
      .info-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-top: 20px; }
      .info-item { display: flex; align-items: center; font-size: 0.92em; color: #333; }
      .info-item img { width: 20px; height: 20px; margin-right: 12px; flex-shrink: 0; }
      .info-item a { color: inherit; text-decoration: none; }
      .info-item a:hover { color: #007bff; text-decoration: underline; }
      @media (max-width: 768px) { .info-grid { grid-template-columns: 1fr; } }
    </style>

    <div class="info-grid">
      <div class="info-item">
        <img src="https://cdn.simpleicons.org/icloud/0059FF" alt="Phone">
        <span>(+82) 10-8239-3780</span>
      </div>
      <div class="info-item">
        <img src="https://cdn.simpleicons.org/googlemaps/4285F4" alt="Location">
        <span>Daejeon, Rep. of Korea</span>
      </div>
      <div class="info-item">
        <img src="https://cdn.simpleicons.org/cakephp/D33C43" alt="Birth">
        <span>2009. 01. 16</span>
      </div>
      <div class="info-item">
        <img src="https://cdn.simpleicons.org/gmail/EA4335" alt="Email">
        <a href="mailto:jhhwang16@snu.ac.kr">jhhwang16@snu.ac.kr</a>
      </div>
      <div class="info-item">
        <img src="https://cdn.simpleicons.org/linkedin/0A66C2" alt="LinkedIn">
        <a href="https://linkedin.com/in/jirrong">LinkedIn Profile</a>
      </div>
      <div class="info-item">
        <img src="https://cdn.simpleicons.org/googlescholar/4285F4" alt="Scholar">
        <a href="#">Google Scholar</a>
      </div>
      <div class="info-item">
        <img src="https://cdn.simpleicons.org/orcid/A6CE39" alt="ORCID">
        <a href="#">ORCID ID</a>
      </div>
      <div class="info-item">
        <img src="https://cdn.simpleicons.org/github/181717" alt="GitHub">
        <a href="https://github.com/jirrong">jirrong</a>
      </div>
    </div>
  </div>
</div>

---

## Education
* **B.S. in Chemistry**, Seoul National University | *Mar 2026 – Current*
    * In progress
* **High School Diploma**, Gyeonggi Science High School for the Gifted (GSHS) | *Mar 2023 – Jan 2026*
    * **Total GPA: 4.19 / 4.30**
    * Graduated with a **Certificate of Excellence in Chemistry**
    * 2023-2025 President of *Alchemist* (Experimental Chemistry Club)
    * 2024 Vice President of *TeXperT* (LaTeX Club) & GSHS TeX Society

## Experiences
* **2025 Creative R&E** | *Apr 2025 – Jan 2026*
    * GSHS & KOFAC | *Computational organic chemistry for organometallic systems*
    * Applied Activation/strain model and Energy decomposition analysis to elucidate kinetic driving forces.
* **GSHS Advanced R&E** | *Mar 2024 – Nov 2024*
    * Dept. of Chemistry, GSHS | *SPS Polarity Conversion Modeling*
    * Studied structural fluctuations of sterically constrained molecules and excited state calculations (TD-DFT, EOM-CC).

## Publications
* **Jiho, H.**; Seungchan H.; Doyoung K.; Jaehoon M. "Uncovering origins of the reaction driving force in an Aromatic Ring-Opening/Ring-Closing Metathesis cascade," *Scimeetings*, 2026.

## Awards
* **Silver Prize (2nd Place)**, 32nd Samsung Humantech Paper Awards | *Feb 2026*
* **Talent Award of Future Chemist**, Korean Union of Chemical Science & Technology | *Jan 2026*
* **Gold Prize (1st Place)**, 31st Samsung Humantech Paper Awards | *Feb 2025*
* **National Representative Candidate** (Top 8), 57th Int'l Chemistry Olympiad (IChO) | *Feb 2025*
* **Excellence Prize**, 2024 Best R&E Joint Presentation, President of KENTECH | *Jan 2025*

## Presentations
* **ACS Spring Meeting 2026** (Poster) | *Mar 2026*
    * "Uncovering origins of the reaction driving force in an Aromatic Ring-Opening/Ring-Closing Metathesis cascade."
    * Selected as **Sci-Mix presentation** (Top 10% of total posters).

## Skills & Languages
* **Software**: Gaussian, ORCA, CFOUR, Multiwfn, Linux/SLURM (HPC clusters).
* **Programming**: C++, Python.
* **Languages**: Korean (Native), English (Advanced), Chinese (Intermediate; HSK 4).

<br>
<figure class="fifth" style="display: flex; gap: 30px; align-items: center; justify-content: center; opacity: 0.7; padding: 20px 0;">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/snuscience.svg" style="height: 45px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/snuchem.png" style="height: 50px">
</figure>


<!---
title: "CV"
layout: gridlay
excerpt: "CV"
sitemap: false
permalink: /cv/
---

# CV (Curriculum Vitae)

 **Last Updated on 13 February 2026**


### Introdution
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> end 
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  <li> {{ member.education4 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  <li> {{ member.education4 | markdownify}} </li>
  <li> {{ member.education5 | markdownify}} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}




## Education
{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!-- <br>email: <{{ member.email }}></i> end 
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


## Experiences

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Former visitors, BSc/ MSc students
<div class="row">

<div class="col-sm-4 clearfix">
<h4>Visitors</h4>
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% for member in site.data.alumni_msc %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% for member in site.data.alumni_bsc %}
{{ member.name }}
{% endfor %}
</div>

</div>


<figure class="fifth">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/snuscience.svg" style="height: 53px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/snuchem.png" style="height: 58px">
</figure>-->