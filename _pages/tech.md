---
title: "Technology & Systems"
permalink: /tech/
layout: single
---
<section class="archive-hero wrap"><p class="eyebrow">01 / Technology & Systems</p><h1>理解技术，<br><em>不止于工具。</em></h1><p>AI、数据、自动化与系统逻辑——记录技术如何真正进入工作流。</p></section>
<section class="archive-list wrap">
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'tech'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2><p>{{ post.excerpt | strip_html | truncate: 170 }}</p><a class="card-arrow" href="{{ post.url | relative_url }}">↗</a></article>{% endfor %}
</section>
