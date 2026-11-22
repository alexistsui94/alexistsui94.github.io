---
title: "All Notes"
description: "Alexis Tsui 的全部文章：技术、项目交付、商业分析与随笔。"
layout: single
permalink: /notes/
---
<section class="archive-hero wrap">
  <p class="eyebrow">全部文章 · 共 {{ site.posts.size }} 篇</p>
  <h1>所有文章，<br><em>一条持续更新的轨迹。</em></h1>
  <p>把技术、项目、商业与阅读笔记放在这里，按时间回看问题、方法与判断如何变化。</p>
</section>
<section class="archive-list wrap">
{% for post in site.posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.categories.first }} · {{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2><p>{{ post.excerpt | strip_html | truncate: 170 }}</p><a class="card-more" href="{{ post.url | relative_url }}" aria-label="阅读 {{ post.title }}">阅读全文 →</a></article>{% endfor %}
</section>
