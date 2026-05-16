---
title: World Model Papers
description: Notes on latent world models, predictive learning, and planning.
---

# World Model Papers

Notes on models that learn compact predictive representations of environment dynamics and use them for planning or control.

{% assign papers = site.pages | where: "paper", true | where: "area", "world-model" | sort: "added" | reverse %}

| Paper | Year | Area | Key Idea |
|---|---:|---|---|
{% for paper in papers %}
| [{{ paper.full_title | default: paper.title }}]({{ paper.url | relative_url }}) | {{ paper.year }} | {{ paper.area_label }} | {{ paper.summary }} |
{% endfor %}
