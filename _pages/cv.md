---
title: "CV"
layout: gridlay
excerpt: "Jiho Hwang's Curriculum Vitae"
sitemap: false
permalink: /cv/
---

<style>
  /* 기본 폰트 및 레이아웃 설정 */
  .cv-container {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 1.15em; /* 전체 글자 크기 확대 */
    line-height: 1.6;
    color: #333;
  }

  /* 상단 프로필 그리드 */
  .info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px 20px;
    margin-top: 25px;
  }
  .info-item {
    display: flex;
    align-items: center;
    font-size: 0.95em;
    color: #444;
  }
  .info-item img {
    width: 20px;
    height: 20px;
    margin-right: 10px;
  }
  .info-item a {
    color: inherit;
    text-decoration: none;
    border-bottom: 1px dashed #ccc;
  }
  .info-item a:hover {
    color: #007bff;
    border-bottom: 1px solid #007bff;
  }

  /* 섹션 스타일 */
  .cv-section {
    margin-top: 50px;
    margin-bottom: 20px;
  }
  .section-title {
    font-size: 1.8em;
    font-weight: 800;
    border-bottom: 3px solid #333;
    padding-bottom: 10px;
    margin-bottom: 25px;
    letter-spacing: -0.5px;
  }

  /* 리스트 스타일 (순수 HTML) */
  ul.custom-list {
    list-style: none; /* 기본 점 제거 */
    padding-left: 10px;
    margin: 0;
  }

  /* 메인 항목 (큰 덩어리) */
  li.main-item {
    margin-bottom: 30px; /* 항목 간 간격 넓힘 */
  }

  /* 항목 헤더 (제목 + 날짜 분리) */
  .item-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  .header-text {
    font-size: 1.25em; /* 큰 동그라미 글자 큼 */
    font-weight: 700;  /* 굵게 */
    color: #000;
    position: relative;
    padding-left: 25px;
  }
  /* 커스텀 큰 점 */
  .header-text::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #000;
    font-size: 1.2em;
    line-height: 1;
  }

  /* 날짜 스타일 (우측 정렬 고정) */
  .date-tag {
    font-size: 0.85em;
    color: #007bff;
    font-weight: 600;
    white-space: nowrap;
    margin-left: 20px;
    margin-top: 5px;
  }

  /* 서브 리스트 (작은 덩어리) */
  ul.sub-list {
    list-style: none;
    padding-left: 25px;
    margin-top: 8px;
  }
  li.sub-item {
    font-size: 0.9em; /* 작은 동그라미 글자 작음 */
    font-weight: 400;
    color: #555;
    position: relative;
    padding-left: 20px;
    margin-bottom: 6px;
  }
  /* 커스텀 작은 점 (빈 동그라미) */
  li.sub-item::before {
    content: "○";
    position: absolute;
    left: 0;
    font-size: 0.8em;
    color: #555;
    top: 2px;
  }

  /* Publication & Presentation 박스 스타일 */
  .pub-box {
    margin-bottom: 30px;
    padding-left: 15px;
    border-left: 4px solid #eee;
  }
  .pub-title {
    display: block;
    font-size: 1.2em;
    font-weight: 700;
    color: #000;
    margin-bottom: 6px;
    line-height: 1.4;
  }
  .pub-authors {
    display: block;
    font-size: 1.05em;
    color: #555;
    font-style: italic;
    margin-bottom: 6px;
  }
  .pub-journal {
    display: block;
    font-size: 1.0em;
    color: #007bff;
    font-weight: 600;
  }

  /* 모바일 최적화 */
  @media (max-width: 768px) {
    .info-grid { grid-template-columns: 1fr; }
    .item-header { flex-direction: column; }
    .date-tag { margin-left: 25px; margin-bottom: 5px; color: #666; }
  }
</style>

<div class="cv-container">

  <h1 style="display:none;">CV</h1> <div style="text-align: right; color: gray; margin-bottom: 20px;">
    <b>Last Updated on 13 February 2026</b>
  </div>
  <hr style="border-top: 1px solid #ddd; margin-bottom: 40px;">

  <div class="row" style="display: flex; flex-wrap: wrap; align-items: center;">
    <div class="col-sm-4" style="text-align: center; margin-bottom: 20px;">
      <img src="{{ site.url }}{{ site.baseurl }}/images/profile.jpg" 
           style="width: 220px; height: 220px; border-radius: 50%; object-fit: cover; border: 5px solid #f8f9fa; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" 
           alt="Jiho Hwang">
    </div>

    <div class="col-sm-8">
      <h1 style="margin-top: 0; font-weight: 800; font-size: 2.4em; letter-spacing: -1px; color: #000;">Jiho Hwang (황지호)</h1>
      <div style="border-left: 4px solid #007bff; padding-left: 15px; margin: 15px 0;">
        <p style="font-style: italic; color: #555; font-size: 1.1em; margin: 0;">“What we find changes who we become.”</p>
      </div>
      <p style="font-size: 1.1em; margin-top: 10px;">
        Student and Researcher in Chemistry & MSE & Physics at <b>Seoul National University</b>.
      </p>
      
      <div class="info-grid">
        <div class="info-item"><img src="https://cdn.simpleicons.org/icloud/0059FF"><span>(+82) 10-8239-3780</span></div>
        <div class="info-item"><img src="https://cdn.simpleicons.org/googlemaps/4285F4"><span>Daejeon, Rep. of Korea</span></div>
        <div class="info-item"><img src="https://cdn.simpleicons.org/cakephp/D33C43"><span>2009. 01. 16</span></div>
        <div class="info-item"><img src="https://cdn.simpleicons.org/gmail/EA4335"><a href="mailto:jhhwang16@snu.ac.kr">jhhwang16@snu.ac.kr</a></div>
        <div class="info-item"><img src="https://cdn.simpleicons.org/linkedin/0A66C2"><a href="https://linkedin.com/in/jirrong">LinkedIn Profile</a></div>
        <div class="info-item"><img src="https://cdn.simpleicons.org/googlescholar/4285F4"><a href="#">Google Scholar</a></div>
        <div class="info-item"><img src="https://cdn.simpleicons.org/orcid/A6CE39"><a href="#">ORCID ID</a></div>
        <div class="info-item"><img src="https://cdn.simpleicons.org/github/181717"><a href="https://github.com/jirrong">jirrong</a></div>
      </div>
    </div>
  </div>

  <div class="cv-section">
    <div class="section-title">Education</div>
    <ul class="custom-list">
      <li class="main-item">
        <div class="item-header">
          <span class="header-text">B.S. in Chemistry, Seoul National University</span>
          <span class="date-tag">Mar 2026 – Current</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">In progress</li>
        </ul>
      </li>
      <li class="main-item">
        <div class="item-header">
          <span class="header-text">High School Diploma, Gyeonggi Science High School for the Gifted (GSHS)</span>
          <span class="date-tag">Mar 2023 – Jan 2026</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item"><b>Total GPA: 4.19 / 4.30</b></li>
          <li class="sub-item">Graduated with a <b>Certificate of Excellence in Chemistry</b></li>
          <li class="sub-item">2023-2025 President of <i>Alchemist</i> (Experimental Chemistry Club)</li>
          <li class="sub-item">2024 Vice President of <i>TeXperT</i> (LaTeX Typesetting Club) & GSHS TeX Society</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="cv-section">
    <div class="section-title">Experiences</div>
    <ul class="custom-list">
      <li class="main-item">
        <div class="item-header">
          <span class="header-text">2025 Creative R&E (GSHS & KOFAC)</span>
          <span class="date-tag">Apr 2025 – Jan 2026</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">Computational organic chemistry calculations of reaction mechanism and thermochemistry, especially for organometallic systems.</li>
          <li class="sub-item">Activation/strain model, Energy decomposition analysis & QTAIM approaches for elucidating kinetic driving forces.</li>
        </ul>
      </li>
      <li class="main-item">
        <div class="item-header">
          <span class="header-text">GSHS Advanced R&E (Dept. of Chemistry)</span>
          <span class="date-tag">Mar 2024 – Nov 2024</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">Quantified polarity conversion ranges of SPS (Switchable Polarity Solvents) using implicit solvation model-based empirical computation model.</li>
          <li class="sub-item">Solvent polarity indexes and Solvatochromism, Fluorescent dyes.</li>
          <li class="sub-item">Structural fluctuations of a sterically constrained molecule & Conformer Search.</li>
          <li class="sub-item">Excited state calculations based on TD-DFT and EOM-CC methods.</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="cv-section">
    <div class="section-title">Interests</div>
    <ul class="custom-list" style="padding-left: 0;"> <ul class="sub-list">
        <li class="sub-item">Organic Synthesis, Asymmetric Synthesis & Synthetic Methodology Development</li>
        <li class="sub-item">Total Synthesis of Natural Compounds</li>
        <li class="sub-item">Organometallic catalysis, C-H/C-C bond activation</li>
        <li class="sub-item">Physical Organic Chemistry</li>
        <li class="sub-item">Computational Chemistry (Semi-empirical, DFT, Excited state, Coupled Cluster, EDA, QTAIM)</li>
      </ul>
    </ul>
  </div>

  <div class="cv-section">
    <div class="section-title">Skills</div>
    <ul class="custom-list" style="padding-left: 0;">
      <ul class="sub-list">
        <li class="sub-item"><b>Languages:</b> Korean (Native), English (Advanced), Chinese (Intermediate; HSK Level 4)</li>
        <li class="sub-item"><b>Software:</b> Gaussian, ORCA, CFOUR, Multiwfn packages</li>
        <li class="sub-item"><b>OS/Computing:</b> Linux/SLURM commands with HPC clusters (CPU/GPU servers)</li>
        <li class="sub-item"><b>Programming:</b> C++, Python</li>
      </ul>
    </ul>
  </div>

  <div class="cv-section">
    <div class="section-title">Publications</div>
    
    <div class="pub-box">
      <span class="pub-title">Uncovering origins of the reaction driving force in an Aromatic Ring-Opening/Ring-Closing Metathesis cascade</span>
      <span class="pub-authors"><b>Jiho, H.</b>; Seungchan H.; Doyoung K.; Jaehoon M.</span>
      <span class="pub-journal">Scimeetings (2026)</span>
    </div>

  </div>

  <div class="cv-section">
    <div class="section-title">Awards</div>
    <ul class="custom-list">
      
      <li class="main-item">
        <div class="item-header">
          <span class="header-text">Silver Prize, 32nd Samsung Humantech Paper Awards</span>
          <span class="date-tag">Feb 2026</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">Samsung Electronics Co.</li>
          <li class="sub-item">2nd Place in High School Chemistry Division; Granted 5,000,000 KRW</li>
        </ul>
      </li>

      <li class="main-item">
        <div class="item-header">
          <span class="header-text">Talent Award of Future Chemist</span>
          <span class="date-tag">Jan 2026</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">The Korean Union of Chemical Science and Technology Societies</li>
        </ul>
      </li>

      <li class="main-item">
        <div class="item-header">
          <span class="header-text">Certificate of Excellence in Chemistry (경기과학고 연구대상)</span>
          <span class="date-tag">Jan 2026</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">Headmaster of Gyeonggi Science High School</li>
        </ul>
      </li>

      <li class="main-item">
        <div class="item-header">
          <span class="header-text">National Representative Candidate (Korea) for the 57th IChO</span>
          <span class="date-tag">Feb 2025</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">2025 Winter School of Korean Chemistry Olympiad (Top 8)</li>
          <li class="sub-item">Excellent Completion, Sophomore Class</li>
        </ul>
      </li>

      <li class="main-item">
        <div class="item-header">
          <span class="header-text">Gold Prize, 31st Samsung Humantech Paper Awards</span>
          <span class="date-tag">Feb 2025</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">Samsung Electronics Co.</li>
          <li class="sub-item">1st Place in High School Chemistry Division; Granted 10,000,000 KRW</li>
        </ul>
      </li>

      <li class="main-item">
        <div class="item-header">
          <span class="header-text">Excellence Prize, 2024 Best R&E Joint Presentation</span>
          <span class="date-tag">Jan 2025</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">President of KENTECH</li>
        </ul>
      </li>

      <li class="main-item">
        <div class="item-header">
          <span class="header-text">Excellence Prize in GSHS Advanced R&E (Chemistry)</span>
          <span class="date-tag">Dec 2024</span>
        </div>
      </li>
      
      <li class="main-item">
        <div class="item-header">
          <span class="header-text">Excellence Prize in GSHS Basic R&E (Chemistry)</span>
          <span class="date-tag">Dec 2023</span>
        </div>
      </li>

    </ul>
  </div>

  <div class="cv-section">
    <div class="section-title">Honors & Scholarship</div>
    <ul class="custom-list">
      <ul class="sub-list">
        <li class="sub-item">N/A</li>
      </ul>
    </ul>
  </div>

  <div class="cv-section">
    <div class="section-title">Presentations</div>
    
    <div class="pub-box">
      <span class="pub-title">“Uncovering origins of the reaction driving force in an Aromatic Ring-Opening/Ring-Closing Metathesis cascade”</span>
      <span class="pub-journal">ACS Spring Meeting 2026, ORGN: Poster In-Person</span>
      <ul class="sub-list">
        <li class="sub-item">Physical Organic Chemistry: Calculations, Mechanisms, Photochemistry & High-Energy Species Symposium</li>
        <li class="sub-item"><b>Selected as Sci-Mix presentations (Top 10% posters of the total)</b></li>
        <li class="sub-item" style="color:#007bff">Mar 2026</li>
      </ul>
    </div>

    <div class="pub-box">
      <span class="pub-title">“Uncovering origins of the reaction driving force in an Aromatic Ring-Opening/Ring-Closing Metathesis cascade”</span>
      <span class="pub-journal">2025 Fall Conference of The Korean Chemical Society</span>
      <ul class="sub-list">
        <li class="sub-item">Future Chemist Research Presentation (Poster)</li>
        <li class="sub-item" style="color:#007bff">Sep 2025</li>
      </ul>
    </div>

    <div class="pub-box">
      <span class="pub-title">“ET(30) quantification of Switchable Polarity Solvents using implicit solvation model and TD-DFT”</span>
      <span class="pub-journal">2024 Fall Conference of The Korean Society for the Gifted</span>
      <ul class="sub-list">
        <li class="sub-item">Youth Creative Research Presentation (Poster)</li>
        <li class="sub-item" style="color:#007bff">Nov 2024</li>
      </ul>
    </div>
  </div>

  <div class="cv-section">
    <div class="section-title">Professional Affiliations</div>
    <ul class="custom-list">
      <ul class="sub-list">
        <li class="sub-item">American Chemistry Society (ACS) Undergraduate Member</li>
        <li class="sub-item">ACS Division of Organic Chemistry (ORGN) Undergraduate Member</li>
      </ul>
    </ul>
  </div>

  <div class="cv-section">
    <div class="section-title">Others</div>
    <ul class="custom-list">
      <li class="main-item">
        <div class="item-header">
          <span class="header-text">English Proficiency (TEPS)</span>
          <span class="date-tag">13 Feb 2026</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">Level 4</li>
        </ul>
      </li>
      <li class="main-item">
        <div class="item-header">
          <span class="header-text">Chinese Proficiency (TEPS)</span>
          <span class="date-tag">13 Feb 2026</span>
        </div>
        <ul class="sub-list">
          <li class="sub-item">Level 4</li>
        </ul>
      </li>
    </ul>
  </div>

</div>

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