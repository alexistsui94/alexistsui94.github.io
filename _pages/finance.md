---
title: "Economics & Finance"
permalink: /finance/
layout: single
classes: wide
author_profile: true
---

This section contains writing on business, markets, investment logic, and economic analysis.

---

{% assign finance_posts = site.posts | where_exp: "post", "post.categories contains 'finance'" %}

{% if finance_posts.size > 0 %}
  {% for post in finance_posts %}
### [{{ post.title }}]({{ post.url | relative_url }})

*{{ post.date | date: "%Y-%m-%d" }}*

{{ post.excerpt | strip_html | truncate: 180 }}

---

  {% endfor %}
{% else %}
No posts yet in this section.
{% endif %}
