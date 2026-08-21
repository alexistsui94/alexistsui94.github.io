---
title: "Essays & Notes"
permalink: /essays/
layout: single
---
<section class="archive-hero wrap"><p class="eyebrow">04 / Essays & Notes</p><h1>保持观察，<br><em>也保持诚实。</em></h1><p>关于工作、阅读、成长与日常生活的长期记录。</p></section>
<section class="archive-list wrap">
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'essays'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2><p>{{ post.excerpt | strip_html | truncate: 170 }}</p><a class="card-arrow" href="{{ post.url | relative_url }}">↗</a></article>{% endfor %}
</section>
