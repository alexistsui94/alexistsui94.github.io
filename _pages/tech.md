---
title: "Technology & Systems"
permalink: /tech/
layout: single
classes: wide
author_profile: true
---

This section focuses on AI, SQL, Python, automation, and data-related workflows.

---

{% assign tech_posts = site.posts | where_exp: "post", "post.categories contains 'tech'" %}

{% if tech_posts.size > 0 %}
  {% for post in tech_posts %}
### [{{ post.title }}]({{ post.url | relative_url }})

*{{ post.date | date: "%Y-%m-%d" }}*

{{ post.excerpt | strip_html | truncate: 180 }}

---

  {% endfor %}
{% else %}
No posts yet in this section.
{% endif %}
