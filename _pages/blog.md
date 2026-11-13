---
title: Notebook
layout: page
eyebrow: NOTES, PAPERS & OPEN QUESTIONS
subtitle: A working notebook, with room for unfinished thoughts.
permalink: /blog/
wide: true
blog_index: true
lang: ko
description: 황지호의 학술 블로그. 논문 읽기, 화학과 계산, 공부와 연구 과정에서 생기는 질문을 기록합니다.
---
<div class="notebook-intro"><p>논문을 읽다 생긴 질문부터 계산 기록과 공부 노트까지.<br>결론에 도달하기 전의 생각도 이곳에 남깁니다.</p><div class="notebook-links"><a href="{{ '/feed.xml' | relative_url }}">RSS 구독 ↗</a><a href="{{ '/writing/' | relative_url }}">글쓰기 안내 ↗</a></div></div>
<div id="blog-tools" class="blog-tools" hidden data-index-url="{{ '/search.json' | relative_url }}"><form id="blog-search-form" role="search"><label for="blog-search">노트 검색</label><div class="search-input-wrap"><span aria-hidden="true">⌕</span><input type="search" id="blog-search" name="q" placeholder="제목, 내용, 태그로 찾아보세요" autocomplete="off"><button class="search-clear" type="button" id="clear-search" aria-label="검색과 태그 초기화">초기화</button></div></form><div class="filter-row" role="group" aria-label="태그 필터"><button type="button" class="filter-chip is-active" data-tag="" aria-pressed="true">All notes</button>{% assign sorted_tags = site.tags | sort %}{% for tag in sorted_tags %}<button type="button" class="filter-chip" data-tag="{{ tag[0] | escape }}" aria-pressed="false">{{ tag[0] | escape }} <span>{{ tag[1].size }}</span></button>{% endfor %}</div></div>
<div class="notebook-list-heading"><h2>All notes</h2><p id="search-status" role="status" aria-live="polite">{{ site.posts.size }}개의 노트</p></div>
<div id="post-list">{% for post in site.posts %}{% include post-card.html post=post %}{% endfor %}</div>
<div id="no-results" class="empty-state" hidden><span aria-hidden="true">∅</span><h2>아직 찾지 못했어요.</h2><p>다른 검색어를 입력하거나 태그를 초기화해 보세요.</p><button type="button" class="button button-secondary" id="reset-filters">모든 노트 보기</button></div>
<noscript><p class="quiet-note">검색과 태그 필터에는 JavaScript가 필요합니다. 모든 글은 위 목록에서 바로 읽을 수 있습니다.</p></noscript>
