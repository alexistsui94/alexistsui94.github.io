---
title: "Projects"
permalink: /projects/
layout: single
classes: wide
author_profile: true
---

This section documents implementation work, project delivery, solution design, and case-based reflections.

---

{% assign project_posts = site.posts | where_exp: "post", "post.categories contains 'projects'" %}

{% if project_posts.size > 0 %}
  {% for post in project_posts %}
### [{{ post.title }}]({{ post.url | relative_url }})

*{{ post.date | date: "%Y-%m-%d" }}*

{{ post.excerpt | strip_html | truncate: 180 }}

---

  {% endfor %}
{% else %}
No posts yet in this section.
{% endif %}
