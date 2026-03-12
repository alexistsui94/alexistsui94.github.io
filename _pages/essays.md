---
title: "Essays"
permalink: /essays/
layout: single
classes: wide
author_profile: true
---

This section is for more personal writing: growth, work, reading, learning, and reflection.

---

{% assign essay_posts = site.posts | where_exp: "post", "post.categories contains 'essays'" %}

{% if essay_posts.size > 0 %}
  {% for post in essay_posts %}
### [{{ post.title }}]({{ post.url | relative_url }})

*{{ post.date | date: "%Y-%m-%d" }}*

{{ post.excerpt | strip_html | truncate: 180 }}

---

  {% endfor %}
{% else %}
No posts yet in this section.
{% endif %}
