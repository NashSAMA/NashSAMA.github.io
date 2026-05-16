---
name: paper-deep-reading
description: Deeply analyze academic papers in AI, embodied intelligence, robotics, VLA, World Models, reinforcement learning, diffusion policy, multimodal models, recommendation systems, search, ads, and ranking. Use when the user asks to 精读论文, 解读论文, 分析论文, generate Chinese Markdown paper notes, extract or preserve key figures, explain architecture diagrams, reconstruct data flow, analyze training and inference, compare with related methods, or organize outputs inside a paper folder containing paper.pdf.
---
# Paper Deep Reading

Use this skill to turn an academic paper into a structured Chinese deep-reading note. Do more than summarize: explain the problem, motivation, method, architecture, data flow, training and inference processes, equations, experiments, novelty, limitations, and relevance to the user's research or engineering goals.

Default output language: Simplified Chinese.

Default output format: Markdown.

## Paper Folder Contract

Treat the current paper folder as the working directory unless the user gives a specific path. Keep every generated artifact inside that folder.

Expected single-paper layout:

```text
paper-folder/
├── paper.pdf
├── note.md
├── summary.md
├── metadata.md
└── figures/
```

If these outputs are missing, create them without asking:

```text
note.md
summary.md
metadata.md
figures/
```

If multiple PDFs exist, prefer `paper.pdf`. If no `paper.pdf` exists, choose the most likely main academic paper from filenames and folder context. If ambiguity remains, state the assumption in `note.md`.

Before changing existing notes, inspect them first. Preserve useful user-written content, update or append when possible, and overwrite only empty placeholders or clearly generated boilerplate.

## Workflow

1. Inspect the folder and identify the main paper PDF.
2. Create missing `note.md`, `summary.md`, `metadata.md`, and `figures/`.
3. Read the paper, including abstract, introduction, related work, method, figures, equations, experiments, conclusion, limitations, and appendix when available.
4. Extract or render key figures into `./figures/`.
5. Write the deep-reading note in `note.md`.
6. Write a short `summary.md`.
7. Write structured bibliographic and tagging data in `metadata.md`.
8. Report created or updated files, extracted figures, and any unreadable or uncertain content.

## Figure Handling

Figures are core evidence, not decoration. Preserve and explain important figures, especially:

- model architecture diagrams
- overall framework diagrams
- data-flow diagrams
- training and inference pipelines
- world model rollout diagrams
- policy architecture or action-head diagrams
- planner, MPC, or diffusion denoising diagrams
- recommendation recall, ranking, or serving diagrams
- main results and ablation figures

Save figures under `./figures/` with clear names:

```text
fig1_overview.png
fig2_architecture.png
fig3_training_pipeline.png
fig4_inference_pipeline.png
fig5_data_flow.png
fig6_results.png
fig7_ablation.png
```

Preserve the paper's figure number when known, for example `fig2_model_architecture.png`.

Insert figures in `note.md` with relative paths only:

```markdown
![Figure 2: Model Architecture](./figures/fig2_architecture.png)
```

If direct extraction fails because the figure is vector-based or embedded in a full page, render the relevant page as an image, crop when possible, save it under `./figures/`, and state when the image is a page screenshot rather than an original embedded image.

When a local helper is useful, run:

```text
python .codex/skills/paper-deep-reading/scripts/extract_figures.py <paper.pdf> --out figures
```

For every important architecture or method figure, include:

```markdown
### Figure {N}: {Figure Title}

![Figure {N}: {Figure Title}](./figures/{figure_filename})

#### 图中展示了什么？

#### 主要模块

| 模块 | 输入 | 输出 | 作用 |
|---|---|---|---|
| ... | ... | ... | ... |

#### 数据流通

1. ...
2. ...
3. ...

#### 训练阶段的数据流

#### 推理阶段的数据流

#### 这张图的关键理解
```

Follow arrows in the figure explicitly. Separate branches, training-time flow, and inference-time flow. If the figure is unclear, say so instead of inventing details.

## Output Files

### `note.md`

Make `note.md` the full deep-reading note. It should be detailed enough for later review in Obsidian, Typora, literature review writing, or technical discussion.

Use this structure, omitting only sections that are clearly irrelevant:

```markdown
# Paper Reading Note: {Paper Title}

## 1. 论文基本信息

- 标题：
- 年份：
- 作者：
- 机构：
- 会议 / 期刊 / arXiv：
- 论文链接：
- 代码 / 项目页：
- 研究领域：
- 关键词：

## 2. 研究背景与问题动机

### 2.1 这篇论文解决什么问题？
### 2.2 为什么这个问题重要？
### 2.3 过去方法的不足
### 2.4 本文的核心切入点
### 2.5 在当前 AI / 具身智能 / 推荐系统研究脉络中的位置

## 3. 核心思想

### 3.1 一句话总结
### 3.2 核心贡献
### 3.3 方法直觉

## 4. 架构图与数据流通

### 4.1 关键图列表
### 4.2 总体架构
### 4.3 模块、输入、输出与作用
### 4.4 训练阶段数据流
### 4.5 推理阶段数据流

## 5. 方法解析

### 5.1 模型组成
### 5.2 输入与输出
### 5.3 算法流程
### 5.4 关键公式
### 5.5 伪代码或步骤化解释

## 6. 训练方式

### 6.1 数据来源
### 6.2 监督信号 / 奖励 / 目标函数
### 6.3 训练流程
### 6.4 训练技巧与实现细节

## 7. 推理与部署过程

### 7.1 推理输入
### 7.2 推理步骤
### 7.3 输出形式
### 7.4 实时性、闭环控制或工程部署约束

## 8. 实验设计与结果分析

### 8.1 数据集 / 环境 / 任务
### 8.2 Baselines
### 8.3 Metrics
### 8.4 Main Results
### 8.5 Ablation Study
### 8.6 实验结论是否充分

## 9. 创新点总结

## 10. 优势与不足

## 11. 与相关工作的关系

## 12. 领域视角分析

## 13. 对用户研究方向的启发

## 14. 复现难点

## 15. 总结

## 16. 可能的改进方向
```

### `summary.md`

Include:

- paper title
- one-sentence summary
- core idea
- main contribution
- key limitation
- relevance to the user's research interests
- 3 to 5 PPT-ready bullet points

### `metadata.md`

Use this template:

```markdown
# Metadata

- Title:
- Year:
- Authors:
- Institutions:
- Venue / Journal / arXiv:
- Paper Link:
- Code:
- Project Page:
- Area:
- Sub-area:
- Keywords:
- Dataset:
- Robot Platform / Environment:
- Main Method:
- Training Paradigm:
- Inference Paradigm:
- Related Papers:
- Reading Status: unread / reading / finished
- Importance: high / medium / low
- Notes:
```

## Domain Checklists

Use these checklists selectively. Do not turn every checklist into a section in `note.md`.

First identify the paper's actual technical category, then expand only the relevant checklist(s). If a category is clearly irrelevant, omit it. If a category is commonly confused with the paper's topic, add at most one concise clarification sentence instead of a full "是否是 X" subsection.

Avoid rigid negative sections such as:

```text
是否是 VLA？不是...
是否是 Diffusion Policy？不是...
是否是 RL？不是...
```

Prefer a natural domain analysis paragraph that explains what the method actually is, what it is not only when useful, and why that distinction matters.

### Embodied AI / Robotics / World Models

Use this section when the paper involves robot control, embodied agents, navigation, manipulation, world models, planning, or action-conditioned prediction.

Analyze the full loop:

```text
Observation -> Representation -> Prediction -> Planning -> Action -> Feedback
```

Identify:

- observations: RGB, depth, point cloud, tactile signal, robot state, proprioception, language instruction, goal image, historical frames
- learned representations: visual tokens, language tokens, latent states, object-centric states, world model states, action-conditioned representations
- predictions: action, trajectory, next state, future latent, future image, reward, value, affordance, success probability
- planning method: direct policy, MPC, CEM, diffusion sampling, autoregressive rollout, tree search, latent planning, language planning
- action output: discrete action token, continuous action, end-effector pose, joint position, joint velocity, gripper command, force / torque, trajectory, latent action
- feedback: open-loop, closed-loop, receding horizon, online replanning, visual servoing

Discuss robotics deployment only at the level supported by the paper. Mention tabletop grasping, object placement, card picking, assembly, dual-camera manipulation, 5-DoF robotic arms, sim-to-real transfer, or real-time robot control only when:

- the paper evaluates them;
- the method directly targets them;
- the user explicitly asks about them; or
- they are a meaningful implication for the user's stated research context.

Otherwise, keep deployment discussion general: data coverage, sensing assumptions, action space, closed-loop frequency, safety constraints, sim-to-real gap, and long-horizon reliability.

### VLA

Use only when the paper is actually about Vision-Language-Action models, robot foundation models with language instructions, action tokenization, or VLM/LLM-conditioned policies. Do not add a VLA subsection merely because the paper is about robotics or vision.

If relevant, answer:

1. Is this truly a Vision-Language-Action model?
2. What are the visual input, language input, and action output?
3. How is the action represented or tokenized?
4. Does the model use an LLM or VLM backbone?
5. What is the action head?
6. Is the backbone frozen or fine-tuned?
7. Does it use SFT, imitation learning, behavior cloning, RL, or preference optimization?
8. What data does it use?
9. Does it support cross-task generalization, cross-robot transfer, and closed-loop control?
10. How does it compare with RT-1, RT-2, OpenVLA, π-series models, Diffusion Policy, and ACT?

If the paper is not VLA but may be confused with VLA, write one concise sentence in the relevant domain section, for example: "This is not a VLA model because it has no language-conditioned policy; it is better understood as an action-conditioned latent world model." Omit the rest.

### World Models

Use when the paper models environment dynamics, future observations/states/latents, rewards, values, or action-conditioned transitions.

If relevant, answer:

1. What does the world model model: pixels, latent representations, object states, robot states, future frames, rewards, values, action-conditioned dynamics, affordance, or language-conditioned future changes?
2. Is it action-conditioned?
3. What are the input and output?
4. Does it generate pixels or predict representations?
5. How is it used for decision-making: representation learning, planning, MPC, policy learning, imagination rollout, or reward-free pretraining?
6. How does it differ from Dreamer-style world models, JEPA-style representation prediction, and video generation models?
7. Does it actually support robot control, or is it mainly a visual prediction model?

### Diffusion Policy / Action Generation

Use only when the paper uses diffusion, score-based denoising, flow matching, rectified flow, action sequence generation, trajectory generation, or explicitly compares against diffusion policies.

If relevant, answer:

1. What is diffused: action sequence, trajectory, end-effector pose, latent action, image, point cloud, or state?
2. What is the conditioning input?
3. What is the denoising network?
4. How many future steps are predicted?
5. Is action execution open-loop or closed-loop?
6. What is the control frequency?
7. Why use diffusion instead of direct regression?
8. How does it compare with ACT, behavior cloning, and autoregressive policies?

If the paper does not use diffusion, do not create a standalone "not diffusion policy" section unless the user explicitly asks.

### Reinforcement Learning

Use only when the method trains with rewards, value functions, policy optimization, model-based RL, offline RL, online RL, exploration, replay buffers, or RL-specific evaluation. If RL appears only as a baseline, discuss it under experiments rather than as a full domain section.

If relevant, identify state space, observation space, action space, reward definition, policy architecture, value function, environment, online or offline training, model-free or model-based setting, exploration strategy, replay buffer, policy optimization objective, stability tricks, and evaluation protocol.

For robotics RL, also analyze sim-to-real gap, safety, sample efficiency, real robot data cost, reset mechanism, reward engineering, and deployment constraints.

### Recommendation / Search / Ads / Ranking

Use only when the paper is about recommendation, search, ads, ranking, retrieval, user modeling, or production serving.

If relevant, identify whether the paper targets recall, pre-ranking, ranking, re-ranking, CTR prediction, CVR prediction, CTCVR / ESMM-style modeling, sequential recommendation, multi-task learning, user modeling, item modeling, retrieval, or online serving.

Focus on:

- user, item, query, context, behavior sequence, and feature representations
- negative sampling and training objective
- sequence modeling, attention, graph, multi-task, contrastive, causal, or reinforcement learning components
- offline metrics: AUC, GAUC, LogLoss, NDCG, Recall@K, HitRate, calibration
- online metrics: CTR, CVR, CTCVR, revenue, latency, QPS, A/B test design
- production constraints: feature freshness, candidate generation size, ranking QPS, model compression, incremental update

## Equations

Do not skip important equations. For each important formula, explain:

1. what it is used for;
2. whether it belongs to training or inference;
3. what each symbol means;
4. what the objective encourages the model to learn;
5. how it affects the architecture or algorithm;
6. what assumptions or limitations it has.

Use this format:

````markdown
### Formula {N}: {Name}

公式：

```math
...
````

#### 符号解释

| 符号 | 含义 |
|---|---|
| ... | ... |

#### 公式作用

#### 用于训练还是推理？

#### 直观理解
````

If a formula is too complex, first give a plain-language explanation, then explain symbols.

## Experiments

Do not merely copy result numbers. Explain:

- what question the experiment answers
- what baselines are used
- whether the baselines are fair
- what metrics are used
- which result matters most
- what the ablation proves
- whether the conclusion is fully supported
- what experimental weaknesses remain

Use tables when useful:

```markdown
| 实验 | 目的 | 结果 | 说明 |
|---|---|---|---|
| Main results | ... | ... | ... |
| Ablation | ... | ... | ... |
```

## Critical Analysis

Always include critical thinking. Identify:

- what is truly novel
- what is mostly engineering integration
- what is mainly empirical validation
- what assumptions the method relies on
- what limitations are hidden or understated
- what would be hard to reproduce
- what would fail in real deployment
- what is useful for the user's own research

Avoid vague statements such as:

```text
该方法效果很好。
```

Prefer precise analysis:

```text
该方法的主要优势不是简单提高成功率，而是通过 action-conditioned latent prediction 将环境动力学建模与下游规划解耦，使模型可以在无奖励数据上学习可迁移的动态表征。但它仍依赖高质量视觉表征和动作覆盖充分的数据集，在长时序真实机器人任务中可能面临误差累积问题。
```

## Style and Accuracy

Write in Simplified Chinese by default.

Use clear, structured, graduate-level technical writing. Prefer precise explanations, tables, and step-by-step data-flow reconstruction. Explain technical terms briefly when first introduced.

Do not fabricate paper content. Do not claim that a figure, method, dataset, result, or limitation exists unless it is present in the paper or provided by the user.

If information is missing, write:

```text
论文中未明确说明。
```

If a statement is an inference, write:

```text
根据论文描述可以推测，...
```

If the paper cannot be fully read, produce a partial note and list what could not be analyzed. If the PDF is scanned or image-only and text extraction fails, use visible page images when possible and state the OCR or extraction limitation.


## GitHub Pages publishing rules

If the project contains a `docs/` directory, also generate a GitHub Pages compatible version of the paper note.

For each paper folder:

`{major_area}/{sub_area}/{paper_id}/note.md`

Create or update:

`docs/papers/{paper_id}/index.md`

Also copy paper-specific figures to:

`docs/papers/{paper_id}/figures/`

Do not copy `paper.pdf` into `docs/` unless the user explicitly requests it.

The GitHub Pages page must be a public technical reading page, not a short abstract. It should be concise enough for web reading but technically useful on its own. Do not publish only `summary.md`. Use `note.md` as the source of truth and compress it into a "core technical deep dive" page.

Minimum depth for `docs/papers/{paper_id}/index.md`:

- use relative image paths
- include paper title and metadata summary
- include links back to area index pages
- include a one-sentence summary and core idea
- include a key figures table
- preserve and explain important architecture, method, pipeline, and planning figures
- include complete architecture details: modules, inputs, outputs, and roles
- include training data flow and inference / deployment data flow as explicit step lists or code blocks
- include the core functions, objectives, or algorithms from `note.md`
- explain important formulas with symbol tables and plain-language interpretation
- include pseudocode or step-by-step algorithm flow when the method has a clear procedure
- include main results, ablations, physical / qualitative analysis, and key limitations
- preserve relative links to copied figures in `./figures/`

Recommended public page structure:

```markdown
---
title: {Short Paper Title}
description: Reading note on {Full Paper Title}.
---

# {Full Paper Title}

[Back to {Area} Index]({{ '/area-index/' | relative_url }})

## Metadata
## One-Sentence Summary
## Core Idea
## Architecture And Data Flow
### Key Figures
### Figure {N}: {Architecture / Pipeline / Planner}
### Overall Architecture
## Core Functions And Objectives
### 1. {Encoder / Predictor / Main Model}
### 2. {Training Loss / Objective}
### 3. {Regularizer / Planner / Policy Head}
### 4. {Inference / Optimization Objective}
### 5. Implementation Sketch
## Main Results
## Physical Understanding / Qualitative Analysis
## Key Limitations
## Why It Matters
```

For the `Core Functions And Objectives` section:

- include formulas or function signatures in fenced blocks so GitHub Pages renders them reliably
- include a `Symbol | Meaning` table for each important formula
- explain whether each function/objective is used for training, inference, planning, ranking, policy generation, or evaluation
- explain what the objective encourages the model to learn
- include assumptions and failure modes when relevant

For architecture figures and method figures, include:

````markdown
### Figure {N}: {Figure Title}

![Figure {N}: {Figure Title}](./figures/{figure_filename})

{Short explanation of what the figure shows.}

| Module | Input | Output | Role |
|---|---|---|---|
| ... | ... | ... | ... |

Training-time data flow:

```text
...
```

Inference-time data flow:

```text
...
```

Key interpretation:
...
````

Keep the public page shorter than the full `note.md`, but not shallow. As a rule of thumb, if `note.md` is long, the published page should still include the central 25-45% of the technical content, especially architecture, data flow, formulas, and algorithmic logic. If the paper is mostly empirical, replace formulas with experimental protocol, metrics, and production/deployment flow.

Also update the corresponding area index file when possible:

- `docs/vla.md`
- `docs/world-model.md`
- `docs/diffusion-policy.md`
- `docs/recommendation.md`
- `docs/ranking.md`
- `docs/reinforcement-learning.md`
