---
title: "Blog"
layout: textlay
excerpt: "Academic blog posts"
sitemap: false
permalink: /blog/
---

# Blog Posts

논문 읽기, 공부 노트, 계산 기록과 학술적인 생각을 자유롭게 남기는 공간입니다.

<div markdown="0">
<p><a href="{{ '/guide/' | relative_url }}">새 글 쓰기 / 글쓰기 안내</a> · <a href="{{ '/feed.xml' | relative_url }}">RSS 구독</a></p>
<div id="blog-tools" hidden data-index-url="{{ '/search.json' | relative_url }}">
<form id="blog-search-form" role="search">
<div class="form-group"><label for="blog-search">노트 검색</label><div class="input-group"><input class="form-control" type="search" id="blog-search" name="q" placeholder="제목, 내용, 태그 검색" autocomplete="off"><span class="input-group-btn"><button class="btn btn-default" type="button" id="clear-search">초기화</button></span></div></div>
</form>
<div class="form-group filter-row" role="group" aria-label="태그 필터"><button type="button" class="btn btn-primary btn-xs filter-chip" data-tag="" aria-pressed="true">All posts</button> {% assign sorted_tags = site.tags | sort %}{% for tag in sorted_tags %}<button type="button" class="btn btn-default btn-xs filter-chip" data-tag="{{ tag[0] | escape }}" aria-pressed="false">{{ tag[0] | escape }} ({{ tag[1].size }})</button> {% endfor %}</div>
</div>
<p id="search-status" class="text-muted small" role="status" aria-live="polite">{{ site.posts.size }}개의 글</p>
<div id="post-list">{% for post in site.posts %}{% include post-card.html post=post %}{% endfor %}</div>
<div id="no-results" hidden><h3>검색 결과가 없습니다.</h3><p>다른 검색어를 입력하거나 태그를 초기화해 보세요.</p><button type="button" class="btn btn-default" id="reset-filters">모든 글 보기</button></div>
<noscript><p>모든 글은 위 목록에서 읽을 수 있습니다. 검색과 태그 필터에는 JavaScript가 필요합니다.</p></noscript>
</div>
<script src="{{ '/assets/js/blog.js' | relative_url }}" defer></script>
