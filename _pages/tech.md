---
title: "AI & Code"
title_zh: "AI 与代码"
description: "Practical notes on AI tools, LLM APIs, Python and small pieces of code that support real work. English with Chinese reference lines."
permalink: /tech/
layout: single
---
<section class="archive-hero wrap">
  <p class="eyebrow">AI &amp; Code</p>
  <h1>Using AI and code<br><em>on real work.</em><span class="h-zh" lang="zh-Hans">把 AI 与代码，用在真实工作上。</span></h1>
  <p>Notes on AI tools, API keys and tokens, language-model concepts and small scripts — kept practical, bounded and checkable.</p>
  <p class="deck-zh" lang="zh-Hans">关于 AI 工具、API Key 与 Token、大模型概念和小脚本的实用笔记，尽量边界清楚、结果可检查。</p>
  <p class="notes-hint"><a href="/notes/">← All writing</a></p>
</section>
<section class="archive-list wrap">
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'tech'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.title_zh %}<span class="list-zh" lang="zh-Hans">{{ post.title_zh }}</span>{% endif %}</h2><p>{{ post.summary | strip_html | truncate: 170 }}</p><a class="card-more" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">Read more →</a></article>{% endfor %}
</section>
