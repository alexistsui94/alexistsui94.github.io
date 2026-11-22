---
title: "Technology & Systems"
title_zh: "技术与系统"
description: "AI, APIs, data, automation and system logic — notes on how technology enters real work. English with Chinese reference lines."
permalink: /tech/
layout: single
---
<section class="archive-hero wrap">
  <p class="eyebrow">Technology &amp; Systems</p>
  <h1>Understanding technology,<br><em>beyond the tools.</em><span class="h-zh" lang="zh-Hans">理解技术，不止于工具。</span></h1>
  <p>AI, data, automation and system logic — notes on how technology actually enters a workflow.</p>
  <p class="deck-zh" lang="zh-Hans">AI、数据、自动化与系统逻辑，记录技术如何真正进入工作流。</p>
</section>
<section class="archive-list wrap">
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'tech'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.title_zh %}<span class="list-zh" lang="zh-Hans">{{ post.title_zh }}</span>{% endif %}</h2><p>{{ post.summary | strip_html | truncate: 170 }}</p><a class="card-more" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">Read more →</a></article>{% endfor %}
</section>
