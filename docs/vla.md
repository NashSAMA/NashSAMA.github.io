---
title: VLA Papers
description: Notes on vision-language-action models and embodied policies.
---

# VLA Papers

This section will collect notes on vision-language-action models, robotic foundation models, multimodal policy learning, and embodied instruction following.

{% assign papers = site.pages | where: "paper", true | where: "area", "vla" | sort: "added" | reverse %}

<ul class="note-list">
  {% for paper in papers %}
  <li>
    <a href="{{ paper.url | relative_url }}">{{ paper.full_title | default: paper.title }}</a>
    <div class="meta">{{ paper.area_label }}，{{ paper.year }}</div>
  </li>
  {% endfor %}
</ul>
