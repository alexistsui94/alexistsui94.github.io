---
title: "Writing"
title_zh: "文章"
description: "Every published note by Alexis Tsui on ERP implementation, project delivery, AI tools and code. Written in English with Chinese reference lines."
layout: single
permalink: /notes/
---
<section class="archive-hero wrap">
  <p class="eyebrow">Writing · {{ site.posts.size }} articles</p>
  <h1>Notes on ERP,<br><em>AI and code.</em><span class="h-zh" lang="zh-Hans">关于 ERP、AI 与代码的笔记。</span></h1>
  <p>One continuous list of everything published here, newest first — ERP implementation, project delivery, AI tools and small pieces of code.</p>
  <p class="deck-zh" lang="zh-Hans">这里按时间收录全部已发布文章：ERP 实施、项目交付、AI 工具与代码实践。</p>
  <p class="notes-hint">Browse by topic: <a href="/tech/">AI &amp; Code</a> · <a href="/projects/">ERP &amp; Delivery</a>. Each article is in English with sense-group pauses marked (<code>/</code> and <code>//</code>) and a Chinese reference line below every passage.</p>
</section>
<section class="archive-list wrap">
{% for post in site.posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.categories.first }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.title_zh %}<span class="list-zh" lang="zh-Hans">{{ post.title_zh }}</span>{% endif %}</h2><p>{{ post.summary | strip_html | truncate: 170 }}</p><a class="card-more" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">Read more →</a></article>{% endfor %}
</section>
