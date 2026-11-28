---
title: "Writing"
description: "Every published note by Alexis Tsui, grouped into ERP, AI and everything else."
layout: single
permalink: /notes/
---
{% assign erp_posts = site.posts | where: "topic", "erp" %}
{% assign ai_posts = site.posts | where: "topic", "ai" %}
{% assign other_posts = site.posts | where: "topic", "other" %}
<section class="archive-hero wrap">
  <p class="eyebrow">Writing · {{ site.posts.size }} articles</p>
  <h1>Notes on ERP,<br><em>AI and everything else.</em></h1>
  <p>Everything published here, in three groups. ERP and delivery first, then AI and code, then the rest — the things I read, noticed or had to work out.</p>
  <nav class="topic-jump" aria-label="Jump to a topic">
    <a href="#erp">ERP<span class="topic-count">{{ erp_posts.size }}</span></a>
    <a href="#ai">AI<span class="topic-count">{{ ai_posts.size }}</span></a>
    {% if other_posts.size > 0 %}<a href="#other">Other<span class="topic-count">{{ other_posts.size }}</span></a>{% endif %}
  </nav>
</section>

<section class="archive-group wrap" id="erp" aria-labelledby="group-erp">
  <div class="group-head">
    <h2 id="group-erp">ERP</h2>
    <span class="group-count">{{ erp_posts.size }} articles</span>
  </div>
  <div class="archive-list">
  {% for post in erp_posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span></div><h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3><p>{{ post.summary | strip_html | truncate: 150 }}</p></article>{% endfor %}
  </div>
</section>

<section class="archive-group wrap" id="ai" aria-labelledby="group-ai">
  <div class="group-head">
    <h2 id="group-ai">AI</h2>
    <span class="group-count">{{ ai_posts.size }} articles</span>
  </div>
  <div class="archive-list">
  {% for post in ai_posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span></div><h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3><p>{{ post.summary | strip_html | truncate: 150 }}</p></article>{% endfor %}
  </div>
</section>

{% if other_posts.size > 0 %}
<section class="archive-group wrap" id="other" aria-labelledby="group-other">
  <div class="group-head">
    <h2 id="group-other">Other</h2>
    <span class="group-count">{{ other_posts.size }} articles</span>
  </div>
  <div class="archive-list">
  {% for post in other_posts %}<article><div><span>{{ post.date | date: "%Y.%m.%d" }}</span></div><h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3><p>{{ post.summary | strip_html | truncate: 150 }}</p></article>{% endfor %}
  </div>
</section>
{% endif %}
