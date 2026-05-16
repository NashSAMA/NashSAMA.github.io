---
title: LeWorldModel
description: Reading note on Stable End-to-End Joint-Embedding Predictive Architecture from Pixels.
---

# LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

[Back to World Model Index]({{ '/world-model/' | relative_url }})

## Metadata

| Field | Value |
|---|---|
| Year | 2026 |
| Authors | Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero |
| Venue | arXiv:2603.19312v2 |
| Area | Embodied AI / World Models / JEPA |
| Paper | https://arxiv.org/abs/2603.19312v2 |
| Code | https://github.com/lucas-maes/le-wm |
| Project | https://le-wm.github.io |

## One-Sentence Summary

LeWM 是一个从像素端到端训练的 JEPA latent world model，用 next-embedding prediction 加 SIGReg 高斯分布正则稳定学习 action-conditioned dynamics，并在 latent space 中用 CEM/MPC 做快速规划。

## Core Idea

LeWM 的核心是把 JEPA 的 anti-collapse 问题变成 latent distribution matching：预测损失让模型学习可预测的环境动态，SIGReg 让 latent embeddings 在随机一维投影上匹配标准高斯，从而避免所有输入映射到常数向量。

![Training Pipeline](./figures/fig1_training_pipeline.png)

## Architecture And Data Flow

```text
pixel observation o_t
-> ViT encoder
-> latent z_t
-> action-conditioned predictor with a_t
-> predicted next latent hat z_{t+1}
-> MSE to z_{t+1} + SIGReg anti-collapse
```

测试时：

```text
current observation + goal observation
-> encode to z_1 and z_g
-> CEM samples action sequences
-> latent rollout to horizon H
-> minimize ||hat z_H - z_g||^2
-> MPC execution and replanning
```

![Latent Planning](./figures/fig4_latent_planning.png)

## Main Results

![Planning Performance](./figures/fig6_planning_performance.png)

- LeWM 在 PushT 和 Reacher 上优于 PLDM 和 DINO-WM。
- 在 OGBench-Cube 上，DINO-WM 略优，论文认为 3D 视觉复杂度使端到端 encoder 训练更难。
- 在 TwoRoom 上，LeWM 弱于 PLDM/DINO-WM，可能因为低内在维环境与高维高斯 SIGReg 先验不匹配。
- LeWM full planning 约 0.98s，而 DINO-WM 约 47s，规划速度提升约 48x。

![Planning Time](./figures/fig3_planning_time_fixed_compute.png)

## Physical Understanding

LeWM 通过 probing、decoder visualization、t-SNE 和 violation-of-expectation 评估 latent 是否捕捉物理结构。

![Predictor Rollouts](./figures/fig7_predictor_rollouts.png)

![Violation of Expectation](./figures/fig10_violation_expectation_lewm.png)

## Key Limitations

- 仍依赖动作标签和覆盖充分的离线轨迹。
- 规划 horizon 较短，autoregressive latent rollout 会累积误差。
- 真实机器人、多视角、长时序任务尚未验证。
- goal-image cost 表达能力有限，不一定覆盖复杂语言任务或约束任务。

## Why It Matters

LeWM 说明端到端像素 world model 不一定需要冻结基础视觉模型或复杂多项正则。对机器人和具身智能研究，它提供了一个轻量、reward-free、可规划的 latent dynamics 路线。
