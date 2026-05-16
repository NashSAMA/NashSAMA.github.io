# NashSAMA Research Notes

This repository is a personal research-reading workspace and GitHub Pages site for AI papers, especially embodied AI, world models, VLA, reinforcement learning, recommendation, search, ads, and ranking. The repository is continuously evolving, and the skill is actively being tested and refined.

Public site:

```text
https://NashSAMA.github.io
```

## Project Purpose

The project has two layers:

1. Local paper-reading workspace
   - Keep original PDFs, full deep-reading notes, summaries, metadata, and extracted figures.
   - These folders are mainly for private research work and are ignored by Git.

2. Public GitHub Pages site
   - Publish selected technical reading pages from `docs/`.
   - Each public page should be readable on its own: metadata, core idea, architecture, data flow, formulas, results, limitations, and key figures.

The intended workflow is: read papers deeply locally, then publish a curated technical version to the website.

## Directory Layout

```text
.
├── .codex/
│   └── skills/
│       └── paper-deep-reading/
│           ├── SKILL.md
│           └── scripts/
│               └── extract_figures.py
├── docs/
│   ├── _config.yml
│   ├── _layouts/
│   │   └── default.html
│   ├── assets/
│   │   └── css/
│   │       └── style.css
│   ├── index.md
│   ├── world-model.md
│   ├── vla.md
│   └── papers/
│       └── {paper_id}/
│           ├── index.md
│           └── figures/
├── 01_Embodied_AI/
├── 02_Recommendation/
├── 03_Foundation_Model/
├── 04_Reinforcement_Learning/
├── 05_Literature_Review/
├── .gitignore
└── README.md
```

## Local Paper Folder Format

Use this layout for each paper in the private research folders:

```text
{major_area}/{sub_area}/{paper_title}/
├── paper.pdf
├── note.md
├── summary.md
├── metadata.md
└── figures/
```

`note.md` is the full deep-reading note. It should be detailed enough for later review, literature writing, or technical discussion.

`summary.md` is a short executive summary.

`metadata.md` stores bibliographic and tagging information.

`figures/` contains extracted architecture diagrams, training pipelines, result figures, ablations, and other evidence used in the note.

## Public Website Format

GitHub Pages publishes from:

```text
docs/
```

Each public paper page uses:

```text
docs/papers/{paper_id}/
├── index.md
└── figures/
```

The public `index.md` should include front matter like:

```yaml
---
title: LeWorldModel
description: Reading note on Stable End-to-End Joint-Embedding Predictive Architecture from Pixels.
paper: true
short_title: LeWorldModel
full_title: "LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels"
area: world-model
area_label: World Models / JEPA / Latent Planning
year: 2026
added: 2026-05-15
summary: End-to-end pixel JEPA world model with SIGReg anti-collapse and CEM/MPC latent planning.
---
```

The site automatically uses `paper: true` pages to populate:

- homepage `Latest`
- homepage `Recent Notes`
- top navigation `Latest Note`
- area index pages such as `world-model.md` and `vla.md`

Use these area values:

```text
world-model
vla
diffusion-policy
recommendation
ranking
reinforcement-learning
```

Add a matching area index page when a new area becomes public.

## Public Page Content Standard

A published paper page should not be a short abstract. It should be a compact technical deep dive.

Recommended structure:

```markdown
# {Paper Title}

## Metadata
## One-Sentence Summary
## Core Idea
## Architecture And Data Flow
### Key Figures
### Figure {N}: {Architecture / Pipeline / Planner}
### Overall Architecture
## Core Functions And Objectives
### 1. {Main Model / Encoder / Predictor}
### 2. {Training Loss / Objective}
### 3. {Regularizer / Planner / Policy Head}
### 4. {Inference / Optimization Objective}
### 5. Implementation Sketch
## Main Results
## Physical Understanding / Qualitative Analysis
## Key Limitations
## Why It Matters
```

Use MathJax display math with `$$`:

```markdown
$$
L_{\mathrm{pred}} = \left\lVert \hat{z}_{t+1} - z_{t+1} \right\rVert_2^2
$$
```

Use fenced code blocks only for data-flow traces, pseudocode, and implementation sketches.

## Using The Codex Skill

The project includes a local Codex skill:

```text
.codex/skills/paper-deep-reading/SKILL.md
```

Use it for Chinese deep reading of academic papers, figure extraction, architecture explanation, data-flow reconstruction, formula analysis, experiment analysis, and GitHub Pages publishing.

Typical prompt:

```text
使用 paper-deep-reading skill，精读这个论文文件夹：
E:\NashSAMA\01_Embodied_AI\World_Model\{paper_folder}

要求：
1. 生成 note.md、summary.md、metadata.md
2. 提取关键架构图、训练流程图、实验结果图到 figures/
3. 重点解释模型架构、训练数据流、推理数据流、核心公式、实验结论和局限
4. 同步生成 GitHub Pages 发布页到 docs/papers/{paper_id}/index.md
5. 发布页不要只是摘要，要包含核心函数、公式和完整架构详解
```

For VLA papers:

```text
使用 paper-deep-reading skill 精读这篇 VLA 论文。
重点分析视觉输入、语言输入、动作输出、action tokenizer、action head、训练数据配方、高层任务分解、闭环控制、跨机器人迁移和开放世界泛化。
同时生成 docs/papers/{paper_id}/index.md，并更新 docs/vla.md。
```

For world model papers:

```text
使用 paper-deep-reading skill 精读这篇 World Model 论文。
重点分析 Observation -> Representation -> Prediction -> Planning -> Action -> Feedback 闭环，解释 latent dynamics、训练目标、anti-collapse 正则、规划算法、MPC/CEM 流程、实验和局限。
同时生成 docs/papers/{paper_id}/index.md，并更新 docs/world-model.md。
```

## Prompt Style

Preferred prompt style:

- Be explicit about the paper folder path.
- State the target domain: VLA, World Model, Diffusion Policy, RL, Recommendation, Ranking, etc.
- Ask for architecture and data-flow reconstruction, not just summary.
- Ask for formula explanations with symbol tables.
- Ask for important figures to be preserved and explained.
- Ask for critical analysis: assumptions, limitations, reproducibility, and deployment risks.
- Ask for a GitHub Pages version when the result should be public.

Good prompt pattern:

```text
精读 {paper title}。
请生成中文 Markdown 笔记，重点不是泛泛总结，而是：
1. 论文解决的问题和动机
2. 完整模型架构和数据流
3. 训练阶段、推理阶段、部署阶段分别怎么运行
4. 核心公式逐项解释
5. 关键图逐图讲解
6. 实验设计、baselines、metrics、ablation
7. 创新点、局限、复现难点
8. 对我的具身智能 / VLA / world model 研究有什么启发
9. 生成公开发布页到 docs/papers/{paper_id}/index.md
```

Avoid vague prompts like:

```text
总结一下这篇论文。
```

That usually produces shallow notes and weak public pages.

## Adding A New Paper

1. Create a local paper folder under the matching private area directory.
2. Put the PDF in the folder as `paper.pdf` when possible.
3. Run Codex with `paper-deep-reading`.
4. Review `note.md`, `summary.md`, `metadata.md`, and extracted figures.
5. Review the generated public page under `docs/papers/{paper_id}/index.md`.
6. Ensure the public page front matter includes `paper: true`, `area`, `year`, `added`, and `summary`.
7. Commit and push.

```powershell
git status --short
git add .codex docs README.md .gitignore
git commit -m "Add {paper_id} reading note"
git push
```

GitHub Pages will rebuild automatically after pushing to `main`.

## Running Locally

GitHub Pages builds the site remotely. Local preview is optional.

If Ruby and Bundler are installed:

```powershell
cd docs
bundle exec jekyll serve
```

If local Jekyll is not installed, you can still edit Markdown and rely on GitHub Pages to build after push.

## Git And Ignore Rules

Tracked:

- `.codex/skills/paper-deep-reading/`
- `docs/`
- `.gitignore`
- `README.md`

Ignored:

- private full paper library directories such as `01_Embodied_AI/`
- original PDFs
- raw figure extraction folders
- videos and slide decks
- `.vscode/`

Do not commit original PDFs unless there is a clear reason. Public pages should copy only selected figures and Markdown into `docs/`.
