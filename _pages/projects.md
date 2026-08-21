---
title: "Projects & Delivery"
permalink: /projects/
layout: single
---
<section class="archive-hero wrap"><p class="eyebrow">02 / Projects & Delivery</p><h1>从业务蓝图，<br><em>走到真实交付。</em></h1><p>ERP、需求分析、方案设计与项目治理——记录复杂系统落地的方法。</p></section>
<section class="archive-list wrap">
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'projects'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2><p>{{ post.excerpt | strip_html | truncate: 170 }}</p><a class="card-arrow" href="{{ post.url | relative_url }}">↗</a></article>{% endfor %}
</section>
