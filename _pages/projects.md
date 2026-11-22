---
title: "ERP & Delivery"
title_zh: "ERP 与交付"
description: "ERP implementation, requirements analysis, solution design and project delivery notes. English with Chinese reference lines."
permalink: /projects/
layout: single
---
<section class="archive-hero wrap">
  <p class="eyebrow">ERP &amp; Delivery</p>
  <h1>From a business blueprint<br><em>to real delivery.</em><span class="h-zh" lang="zh-Hans">从业务蓝图，走到真实交付。</span></h1>
  <p>ERP, requirements analysis, solution design and project governance — methods for landing complex systems, plus one AI application case.</p>
  <p class="deck-zh" lang="zh-Hans">ERP、需求分析、方案设计与项目治理，记录复杂系统落地的方法，并附一个 AI 应用案例。</p>
  <p class="notes-hint"><a href="/notes/">← All writing</a></p>
</section>
<section class="archive-list wrap">
<article><div><span>2026.04</span><span>Case study</span></div><h2><a href="/projects/hk-food-label-checker/">Food Label AI: recognition and Traditional Chinese proofreading</a><span class="list-zh" lang="zh-Hans">食品标签 AI 识别与香港繁体校对</span></h2><p>Starting from a real import-business checking task: image recognition, knowledge matching, Traditional Chinese proofreading and Excel export, delivered to business users.</p><a class="card-more" href="/projects/hk-food-label-checker/" aria-label="Read the food label AI case">Read the case →</a></article>
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'projects'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.title_zh %}<span class="list-zh" lang="zh-Hans">{{ post.title_zh }}</span>{% endif %}</h2><p>{{ post.summary | strip_html | truncate: 170 }}</p><a class="card-more" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">Read more →</a></article>{% endfor %}
</section>
