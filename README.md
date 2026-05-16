# NashSAMA Research Notes

Personal research-reading workspace and GitHub Pages site for AI papers, especially embodied AI, world models, VLA, reinforcement learning, recommendation, search, ads, and ranking. The repository is continuously evolving, and the skill is actively being tested and refined.

Site: [https://NashSAMA.github.io](https://NashSAMA.github.io)

## What This Repo Is

- Private workspace for full paper reading notes, PDFs, metadata, and extracted figures.
- Public GitHub Pages site for selected technical notes under `docs/`.
- Local Codex skill for paper deep reading and public page generation.

## Structure

```text
.
├── .codex/skills/paper-deep-reading/   # Codex skill and helper scripts
├── docs/                               # GitHub Pages site
│   ├── index.md
│   ├── world-model.md
│   ├── vla.md
│   └── papers/{paper_id}/
│       ├── index.md
│       └── figures/
├── 01_Embodied_AI/                     # private local paper library
├── 02_Recommendation/
├── 03_Foundation_Model/
├── 04_Reinforcement_Learning/
└── 05_Literature_Review/
```

Private paper folders usually follow:

```text
{major_area}/{sub_area}/{paper_title}/
├── paper.pdf
├── note.md
├── summary.md
├── metadata.md
└── figures/
```

## Public Paper Page

Each public note lives at:

```text
docs/papers/{paper_id}/index.md
docs/papers/{paper_id}/figures/
```

Required front matter:

```yaml
---
title: LeWorldModel
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

`paper: true` lets the homepage, latest note, recent notes, and area pages update automatically.

Use `$$...$$` for display math:

```markdown
$$
L_{\mathrm{pred}} = \left\lVert \hat{z}_{t+1} - z_{t+1} \right\rVert_2^2
$$
```

## Add A Paper

1. Put the PDF in a private paper folder.
2. Ask Codex to use `paper-deep-reading`.
3. Review `note.md`, `summary.md`, `metadata.md`, and extracted figures.
4. Review the public page under `docs/papers/{paper_id}/index.md`.
5. Commit and push.

```powershell
git status --short
git add .codex docs README.md .gitignore
git commit -m "Add {paper_id} reading note"
git push
```

GitHub Pages rebuilds automatically from `docs/`.

## Prompt Templates

General:

```text
使用 paper-deep-reading skill，精读这个论文文件夹：
E:\NashSAMA\{paper_folder}

生成 note.md、summary.md、metadata.md，提取关键图到 figures/。
重点解释问题动机、模型架构、训练数据流、推理数据流、核心公式、实验结果、局限和复现难点。
同时生成 GitHub Pages 发布页到 docs/papers/{paper_id}/index.md。
发布页不要只是摘要，要包含核心函数、公式和完整架构详解。
```

VLA:

```text
重点分析视觉输入、语言输入、动作输出、action tokenizer、action head、训练数据配方、高层任务分解、闭环控制、跨机器人迁移和开放世界泛化。
```

World Model:

```text
重点分析 Observation -> Representation -> Prediction -> Planning -> Action -> Feedback 闭环，解释 latent dynamics、训练目标、anti-collapse 正则、规划算法、MPC/CEM 流程、实验和局限。
```

## Git Notes

Tracked:

- `.codex/skills/paper-deep-reading/`
- `docs/`
- `README.md`
- `.gitignore`

Ignored:

- private full paper libraries
- PDFs
- raw extracted figures
- videos and slide decks
- `.vscode/`

Do not commit original PDFs unless explicitly needed.
