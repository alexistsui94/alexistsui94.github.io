---
title: "All Notes"
title_zh: "全部文章"
description: "Every article by Alexis Tsui: technology, project delivery, business analysis and essays. Written in English with Chinese reference lines."
layout: single
permalink: /notes/
---
<section class="archive-hero wrap">
  <p class="eyebrow">All Notes · {{ site.posts.size }} articles</p>
  <h1>Every note,<br><em>one continuous trail.</em><span class="h-zh" lang="zh-Hans">所有文章，一条持续更新的轨迹。</span></h1>
  <p>Technology, projects, business and reading notes in one place — a way to look back at how questions, methods and judgements have changed.</p>
  <p class="deck-zh" lang="zh-Hans">把技术、项目、商业与阅读笔记放在这里，按时间回看问题、方法与判断如何变化。</p>
  <p class="notes-hint">Each article is written in English with sense-group pauses marked (<code>/</code> and <code>//</code>) and a Chinese reference line below every passage.</p>
</section>
<section class="archive-list wrap">
{% for post in site.posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.categories.first }} · {{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.title_zh %}<span class="list-zh" lang="zh-Hans">{{ post.title_zh }}</span>{% endif %}</h2><p>{{ post.summary | strip_html | truncate: 170 }}</p><a class="card-more" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">Read more →</a></article>{% endfor %}
</section>
