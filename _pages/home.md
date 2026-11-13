---
title: Home
layout: homelay
permalink: /
description: Jiho Hwang's academic home — chemistry at Seoul National University, research interests, and an open academic notebook.
---
<section class="home-hero row">
  <div class="col-md-8 hero-copy">
    <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> {{ site.data.profile.role }} · SNU</p>
    <h1>Jiho Hwang<span class="accent-dot">.</span><span class="hero-korean" lang="ko">황지호</span></h1>
    <p class="hero-statement">Chemistry, questions,<br>and the space in between.</p>
    <p class="hero-intro">{{ site.data.profile.intro }}</p>
    <div class="hero-actions"><a class="button button-primary" href="{{ '/interests/' | relative_url }}">Explore my interests <span aria-hidden="true">↗</span></a><a class="text-link" href="{{ '/cv/' | relative_url }}">Curriculum vitae <span aria-hidden="true">→</span></a></div>
  </div>
  <aside class="col-md-4 hero-aside" aria-label="Profile"><div class="profile-frame"><img src="{{ '/assets/images/jiho-hwang.jpg' | relative_url }}" alt="Jiho Hwang" width="520" height="650" fetchpriority="high"><span class="photo-corner" aria-hidden="true">JH / 01</span></div><div class="profile-caption"><span>Seoul National University</span><span>Seoul, KR <span aria-hidden="true">↗</span></span></div></aside>
</section>
<section class="home-about section-rule" aria-labelledby="about-heading"><div class="section-label"><p class="eyebrow">A LITTLE CONTEXT</p><h2 id="about-heading">A place to connect<br>the dots.</h2></div><div class="about-copy"><p>{{ site.data.profile.about }}</p><p>I’m especially drawn to how molecules are made, why reactions take the paths they do, and what computation can help us see.</p><a class="text-link" href="mailto:{{ site.email }}">Get in touch <span aria-hidden="true">↗</span></a></div></section>
<section class="research-section section-rule" aria-labelledby="research-heading"><div class="section-heading"><div><p class="eyebrow">RESEARCH INTERESTS</p><h2 id="research-heading">Three ways into a question.</h2></div><a class="text-link" href="{{ '/interests/' | relative_url }}">Research & experience <span aria-hidden="true">↗</span></a></div><div class="research-grid">{% for area in site.data.research %}<a class="research-item" href="{{ '/interests/' | relative_url }}#area-{{ area.number }}"><span class="item-number">{{ area.number }}</span><h3>{{ area.title }}</h3><p>{{ area.subtitle }}</p><span class="item-arrow" aria-hidden="true">↗</span></a>{% endfor %}</div></section>
<section class="notebook-section section-rule" aria-labelledby="notebook-heading"><div class="section-heading"><div><p class="eyebrow">THE OPEN NOTEBOOK</p><h2 id="notebook-heading">Notes along the way.</h2><p class="section-description" lang="ko">논문에서 만난 질문, 계산하며 배운 것, 아직 정리 중인 생각들.</p></div><a class="text-link" href="{{ '/blog/' | relative_url }}">All notes <span aria-hidden="true">→</span></a></div><div class="home-post-list">{% for post in site.posts limit: 3 %}{% include post-card.html post=post %}{% endfor %}</div></section>
<section class="contact-strip"><p>Have a question or an idea to share?</p><a href="mailto:{{ site.email }}">Let’s talk chemistry. <span aria-hidden="true">↗</span></a></section>
