---
title: Notes
layout: archive
permalink: /notes/
author_profile: true
---

{% assign notes_posts = site.categories["Notes"] | sort: "date" | reverse %}
{% for post in notes_posts %}
  {% include archive-single.html type="post" %}
{% endfor %}
