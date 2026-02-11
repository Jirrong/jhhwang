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

## **Jiho Hwang (황지호)**
> “What we find changes who we become.”
>
> Student and Researcher in Chemistry & MSE & Physics at **Seoul National University**.

<br>

| | |
| :--- | :--- |
| 📱 **Phone** : (+82) 10-8239-3780 | 📍 **Address** : Daejeon, Rep. of Korea |
| 🎂 **Birth** : 2009. 01. 16 | 📧 **Email** : [jhhwang16@snu.ac.kr](mailto:jhhwang16@snu.ac.kr) |
| 🔗 **LinkedIn** : [Profile Link](#) | 🎓 **Scholar** : [Google Scholar](#) |
| 🆔 **ORCID** : [ORCID ID](#) | 💻 **GitHub** : [jirrong](https://github.com/jirrong) |

<br>

---

## **Education**

### **B.S. in Chemistry**, Seoul National University `Mar 2026 – Current`
* ○ In progress

<br>

### **High School Diploma**, Gyeonggi Science High School (GSHS) `Mar 2023 – Jan 2026`
* ○ **Total GPA: 4.19 / 4.30**
* ○ Graduated with a **Certificate of Excellence in Chemistry**
* ○ 2023-2025 President of *Alchemist* (Experimental Chemistry Club)
* ○ 2024 Vice President of *TeXperT* (LaTeX Club) & GSHS TeX Society

<br>

---

## **Experiences**

### **2025 Creative R&E (GSHS & KOFAC)** `Apr 2025 – Jan 2026`
* ○ Computational organic chemistry calculations of reaction mechanism and thermochemistry.
* ○ Activation/strain model, Energy decomposition analysis & QTAIM approaches.

<br>

### **GSHS Advanced R&E (Dept. of Chemistry)** `Mar 2024 – Nov 2024`
* ○ Quantified polarity conversion ranges of SPS using implicit solvation model.
* ○ Structural fluctuations of a sterically constrained molecule & Conformer Search.
* ○ Excited state calculations based on TD-DFT and EOM-CC methods.

<br>

---

## **Interests**
* ○ Organic Synthesis, Asymmetric Synthesis & Synthetic Methodology Development
* ○ Total Synthesis of Natural Compounds / Organometallic catalysis
* ○ Computational Chemistry (DFT, Coupled Cluster, EDA, QTAIM)

<br>

---

## **Skills**
* ○ **Languages:** Korean (Native), English (Advanced), Chinese (HSK Level 4)
* ○ **Software:** Gaussian, ORCA, CFOUR, Multiwfn
* ○ **Programming:** C++, Python

<br>

---

## **Publications**

1. **Uncovering origins of the reaction driving force in an Aromatic Ring-Opening/Ring-Closing Metathesis cascade**
   * *Jiho, H.; Seungchan H.; Doyoung K.; Jaehoon M.*
   * **Scimeetings (2026)**

<br>

---

## **Awards**

### **Silver Prize, 32nd Samsung Humantech Paper Awards** `Feb 2026`
* ○ 2nd Place in High School Chemistry Division; **Granted 5,000,000 KRW**

<br>

### **Talent Award of Future Chemist** `Jan 2026`
* ○ The Korean Union of Chemical Science and Technology Societies

<br>

### **Certificate of Excellence in Chemistry (경기과학고 연구대상)** `Jan 2026`
* ○ Headmaster of Gyeonggi Science High School

<br>

### **National Representative Candidate (Korea) for the 57th IChO** `Feb 2025`
* ○ 2025 Winter School of Korean Chemistry Olympiad (**Top 8**)

<br>

### **Gold Prize, 31st Samsung Humantech Paper Awards** `Feb 2025`
* ○ 1st Place in High School Chemistry Division; **Granted 10,000,000 KRW**

<br>

---

## **Presentations**

### **“Uncovering origins of the reaction driving force...”**
* **ACS Spring Meeting 2026, ORGN: Poster In-Person**
* ○ Selected as **Sci-Mix presentations (Top 10% posters)**
* ○ `Mar 2026`

<br>

### **“Uncovering origins of the reaction driving force...”**
* **2025 Fall Conference of The Korean Chemical Society**
* ○ Future Chemist Research Presentation (Poster)
* ○ `Sep 2025`

<br>

---

## **Professional Affiliations**
* ○ American Chemistry Society (ACS) Undergraduate Member
* ○ ACS Division of Organic Chemistry (ORGN) Undergraduate Member

<br>

---

## **Others**

### **English Proficiency (TEPS)** `13 Feb 2026`
* ○ Level 4

### **Chinese Proficiency (HSK)** `13 Feb 2026`
* ○ Level 4

<br>

<figure class="fifth">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/snuscience.svg" style="height: 53px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/snuchem.png" style="height: 58px">
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