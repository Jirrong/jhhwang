---
title: "Blog"
layout: notebook
excerpt: "Notes on chemistry, papers, calculations, and methods by Jiho Hwang."
permalink: /blog/
lang: en
notebook_class: notebook-index
---

# Blog

Notes on chemistry, papers, calculations, and methods.

<div markdown="0">
<p><a href="{{ '/feed.xml' | relative_url }}">Subscribe via RSS</a> · <a href="{{ '/guide/' | relative_url }}#write-a-post">Write a post</a></p>
<div id="blog-tools" hidden data-index-url="{{ '/search.json' | relative_url }}">
<form id="blog-search-form" role="search">
<div class="form-group"><label for="blog-search">Search posts</label><div class="input-group"><input class="form-control" type="search" id="blog-search" name="q" placeholder="Search titles, content, or tags" autocomplete="off"><span class="input-group-btn"><button class="btn btn-default" type="button" id="clear-search" aria-label="Reset search and tags">Reset</button></span></div></div>
</form>
<div class="form-group filter-row" role="group" aria-label="Filter posts by tag"><button type="button" class="btn btn-primary btn-xs filter-chip" data-tag="" aria-pressed="true">All posts</button> {% assign sorted_tags = site.tags | sort %}{% for tag in sorted_tags %}<button type="button" class="btn btn-default btn-xs filter-chip" data-tag="{{ tag[0] | escape }}" aria-pressed="false">{{ tag[0] | escape }} ({{ tag[1].size }})</button> {% endfor %}</div>
</div>
<p id="search-status" class="text-muted small" role="status" aria-live="polite">{{ site.posts.size }} {% if site.posts.size == 1 %}post{% else %}posts{% endif %}</p>
<div id="post-list">{% for post in site.posts %}{% include post-card.html post=post %}{% endfor %}</div>
<div id="no-results" hidden><h3>No posts found</h3><p>Try a different search term or reset the filters.</p><button type="button" class="btn btn-default" id="reset-filters">Show all posts</button></div>
<noscript><p>All posts are available above. Search and tag filtering require JavaScript.</p></noscript>
</div>
<script src="{{ '/assets/js/blog.js' | relative_url }}" defer></script>
