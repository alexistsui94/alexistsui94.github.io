---
title: "Business & Finance"
description: "商业逻辑、企业财务、市场观察与决策框架。"
permalink: /finance/
layout: single
---
<section class="archive-hero wrap"><p class="eyebrow">03 / Business & Finance</p><h1>在数字背后，<br><em>寻找商业逻辑。</em></h1><p>市场观察、企业财务与决策框架——把事实、机制和判断分开，建立经得起变化的认识。</p></section>
<section class="archive-list wrap">
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'finance'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2><p>{{ post.excerpt | strip_html | truncate: 170 }}</p><a class="card-arrow" href="{{ post.url | relative_url }}" aria-label="阅读 {{ post.title }}">↗</a></article>{% endfor %}
</section>
