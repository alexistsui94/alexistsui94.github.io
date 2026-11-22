---
title: "Essays & Notes"
title_zh: "随笔与笔记"
description: "Long-form notes on work, reading, expression, growth and everyday life. English with Chinese reference lines."
permalink: /essays/
layout: single
---
<section class="archive-hero wrap">
  <p class="eyebrow">Essays &amp; Notes</p>
  <h1>Keep observing.<br><em>Stay honest.</em><span class="h-zh" lang="zh-Hans">保持观察，也保持诚实。</span></h1>
  <p>A long-running record of work, reading, growth and everyday life.</p>
  <p class="deck-zh" lang="zh-Hans">关于工作、阅读、成长与日常生活的长期记录。</p>
</section>
<section class="archive-list wrap">
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'essays'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.title_zh %}<span class="list-zh" lang="zh-Hans">{{ post.title_zh }}</span>{% endif %}</h2><p>{{ post.summary | strip_html | truncate: 170 }}</p><a class="card-more" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">Read more →</a></article>{% endfor %}
</section>
