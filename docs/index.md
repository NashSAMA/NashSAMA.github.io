---
title: Home
description: Paper reading notes and research pages.
---

{% assign papers = site.pages | where: "paper", true | sort: "added" | reverse %}
{% assign latest_paper = papers | first %}

<section class="hero">
  <p class="eyebrow">Research Notes</p>
  <h1>NashSAMA</h1>
  <p class="lead">A compact reading space for embodied AI, world models, VLA systems, reinforcement learning, and recommendation research.</p>
</section>

<section class="section-grid" aria-label="Research areas">
  <a class="topic-card" href="{{ '/world-model/' | relative_url }}">
    <span>01</span>
    <strong>World Models</strong>
    <p>Latent dynamics, predictive representations, planning, and model-based control.</p>
  </a>
  <a class="topic-card" href="{{ '/vla/' | relative_url }}">
    <span>02</span>
    <strong>VLA</strong>
    <p>Vision-language-action models, robotic policies, and multimodal grounding.</p>
  </a>
  {% if latest_paper %}
  <a class="topic-card" href="{{ latest_paper.url | relative_url }}">
    <span>Latest</span>
    <strong>{{ latest_paper.short_title | default: latest_paper.title }}</strong>
    <p>{{ latest_paper.summary }}</p>
  </a>
  {% endif %}
</section>

## Recent Notes

<ul class="note-list">
  {% for paper in papers limit: 5 %}
  <li>
    <a href="{{ paper.url | relative_url }}">{{ paper.full_title | default: paper.title }}</a>
    <div class="meta">{{ paper.area_label }}，{{ paper.year }}</div>
  </li>
  {% endfor %}
</ul>
