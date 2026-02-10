---
title: "News"
layout: textlay
excerpt: "Jiho Hwang at Seoul National University."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br> {{ article.headline | markdownify}}</p>
{% endfor %}
