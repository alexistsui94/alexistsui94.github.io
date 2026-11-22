---
title: "Business & Finance"
title_zh: "商业与财务"
description: "Business logic, corporate finance, market observation and decision frameworks. English with Chinese reference lines."
permalink: /finance/
layout: single
---
<section class="archive-hero wrap">
  <p class="eyebrow">Business &amp; Finance</p>
  <h1>Behind the numbers,<br><em>the business logic.</em><span class="h-zh" lang="zh-Hans">在数字背后，寻找商业逻辑。</span></h1>
  <p>Market observation, corporate finance and decision frameworks — separating facts, mechanisms and judgement.</p>
  <p class="deck-zh" lang="zh-Hans">市场观察、企业财务与决策框架，把事实、机制和判断分开，建立经得起变化的认识。</p>
</section>
<section class="archive-list wrap">
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'finance'" %}
{% for post in posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span><span>{{ post.tags | join: " · " }}</span></div><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.title_zh %}<span class="list-zh" lang="zh-Hans">{{ post.title_zh }}</span>{% endif %}</h2><p>{{ post.summary | strip_html | truncate: 170 }}</p><a class="card-more" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">Read more →</a></article>{% endfor %}
</section>
