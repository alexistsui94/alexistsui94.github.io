---
title: "Projects & Delivery"
description: "ERP、需求分析、方案设计与项目交付，记录复杂系统落地的方法。"
permalink: /projects/
layout: single
---
<section class="archive-hero wrap"><p class="eyebrow">02 / Projects & Delivery</p><h1>从业务蓝图，<br><em>走到真实交付。</em></h1><p>ERP、需求分析、方案设计与项目治理——记录复杂系统落地的方法。</p></section>
<section class="archive-list wrap">
<article><div><span>项目时间 · 2026.04</span><span>AI APPLICATION · PYTHON</span></div><h2><a href="/projects/hk-food-label-checker/">食品标签 AI 识别与香港繁体校对</a></h2><p>从进口业务中的标签校验需求出发，独立完成图片识别、知识匹配、繁体校对和 Excel 导出，并交付真实业务用户使用。</p><a class="card-arrow" href="/projects/hk-food-label-checker/" aria-label="阅读食品标签 AI 项目">↗</a></article>
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'projects'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2><p>{{ post.excerpt | strip_html | truncate: 170 }}</p><a class="card-arrow" href="{{ post.url | relative_url }}" aria-label="阅读 {{ post.title }}">↗</a></article>{% endfor %}
</section>

