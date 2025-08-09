---
title: 读书笔记
layout: archive
permalink: /notes/
author_profile: true
---

{% assign notes_posts = site.categories["读书笔记"] | sort: "date" | reverse %}
{% for post in notes_posts %}
  {% include archive-single.html type="post" %}
{% endfor %}
