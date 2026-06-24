---
id: "nahida-knowledge-time-series-synthetic-data-generation"
title: "Time-series synthetic data generation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "time-series-synthetic-data-generation"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems-synthetic-data-generation"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "time-series-synthetic-data-generation"
primary_ontology_path: "ml-systems/synthetic-data-generation/time-series-synthetic-data-generation"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-time-series-synthetic-data-generation"
    relation: "is_a"
    to: "nahida-knowledge-ml-systems-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/time-series-synthetic-data-generation.md"
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-time-series-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
    confidence: "high"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
representative_source_refs:
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
query_keys:
  - "time-series synthetic data generation"
  - "synthetic time series"
  - "financial time series generation"
  - "irregular scale-invariant time series"
  - "FTS-Diffusion"
  - "TMTR"
  - "TATR"
aliases:
  - "synthetic time series"
  - "time-series data synthesis"
  - "金融时序合成数据"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "time-series-synthetic-data-generation"
  - "financial-time-series-generation"
  - "diffusion-models-for-time-series"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-fts-diffusion-financial-time-series"
source_refs:
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
confidence: "medium"
trust_tier: "primary"
---

# Time-series synthetic data generation

## 定义与范围

- 定义: Time-series synthetic data generation 关注如何生成带有时间顺序、动态依赖、重复模式、状态转移或非平稳结构的合成序列，使其既保留真实时序的重要统计/结构特征，又能服务训练、测试、仿真或下游预测。
- 不包含: 普通静态 tabular/image synthetic data；单个 financial asset 数据集；某个 generator 的具体伪代码；这些保留在 source note 或父级方向的其他 child。
- Canonical terms: `time-series synthetic data generation`, `synthetic time series`
- Aliases/query keys: synthetic financial time series, time-series data synthesis, FTS-Diffusion, TimeGAN, CSDI
- Standalone completeness check: 本节点解释了时间序列合成数据的核心问题、评价轴、当前方法 seed 和边界；由于只有一个直接 source，仍为 `active_seed`。
- Retrieval role: 查询“怎样生成合成时序数据”“金融时序合成数据如何评估”“FTS-Diffusion 属于什么方法”时，读本节点可避免直接扫描 ML systems 或全部 paper notes。
- Update scope: 新 source 若涉及 TimeGAN/CSDI/TimeVAE/QuantGAN、synthetic financial data、temporal data augmentation、time-series fidelity/utility/privacy evaluation，应刷新本节点。
- Domain dynamics note: not_applicable; parent domain dynamics is [[research-dynamics|ML systems Research Dynamics]].

## 背景

model_prior_background: 时间序列合成数据比静态数据生成更难，因为样本不是独立点集；生成结果需要保留 temporal dependence、lag structure、seasonality/irregular recurrence、state transitions、distribution tails 和任务相关信号。固定窗口生成可能破坏 variable-length patterns，单纯分布拟合也可能无法改善预测或控制任务。

source_backed_background: [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] 把金融时序的难点具体化为 irregularity and scale-invariance，并提出 pattern recognition -> pattern generation -> pattern evolution 的路线。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem/topic`
- 为什么足够通用: 它可组织金融、医疗、电力、网络流量、传感器等多类 temporal data 的合成数据生成和评价。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: FTS-Diffusion 是一个 representative source；time-series synthetic data generation 是更通用的任务。
- 需要引用的更基础 Knowledge: [[synthetic-data-generation|Synthetic data generation]], [[ml-systems|ML systems]]。
- 不应拆出的实例/协议/来源: FTS-Diffusion、SISC、TMTR/TATR 先作为 source extension/评价术语，不单独建 foundational node。

## 解决的问题

| 问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Temporal dependence preservation | 生成序列必须保持时间相关性、状态转移、长短期动态，而不只是边际分布相似。 | FTS-Diffusion pattern evolution module. |
| Variable-length pattern discovery | 真实时序可能包含长短不同、间隔不固定的重复模式。 | FTS-Diffusion SISC and DTW route. |
| Scale variation | pattern 形状相似但 duration/magnitude 不同，需要对 scale-invariance 建模。 | FTS-Diffusion financial time-series setting. |
| Fidelity evaluation | 合成时序应保留真实数据分布和领域 stylized facts。 | FTS-Diffusion KS/AD, heavy tails, autocorrelation decay. |
| Downstream utility | 合成数据要在预测/控制/检测等任务上有用。 | FTS-Diffusion TMTR/TATR and LSTM MAPE. |
| Robustness and privacy | 合成数据是否跨 regime 泛化、是否泄露训练序列。 | not covered by current source. |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[synthetic-data-generation|Synthetic data generation]] | child_of | FTS-Diffusion source absorption | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| financial time-series generation | application_area candidate | 金融 return series 有 heavy tails、volatility clustering、market regime shifts、limited history 等特殊问题；当前只有 FTS-Diffusion 一篇 source，暂不单独建节点。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] | source_extension |
| time-series synthetic data evaluation | evaluation_axis candidate | Fidelity、utility、privacy、forecasting robustness 需要专门评价。 | FTS-Diffusion only covers fidelity/utility | queued |
| multivariate time-series generation | subproblem candidate | 多变量依赖是 FTS-Diffusion future work；后续 source 足够时可拆。 | FTS-Diffusion §6 | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Fixed-window time-series generation | 将序列切成固定窗口后用 GAN/VAE/diffusion 等生成。 | 周期性或窗口边界与真实模式一致。 | 对 irregular/variable-length patterns 可能切碎或混合多个 pattern。 | FTS-Diffusion related-work contrast |
| Latent generative models | 用 VAE/GAN/diffusion 学习 sequence distribution。 | 需要可训练的 temporal representation。 | 可能只拟合表层分布，不保留下游任务结构。 | TimeVAE/RCGAN/TimeGAN/CSDI as related work in FTS-Diffusion |
| Pattern-recognition-generation-evolution | 先识别 reusable temporal patterns，再生成 segment，再学习 pattern transition。 | 时序有 irregular recurrence 和 scale-invariance。 | 依赖 pattern recognition 质量；multivariate/transition shift 仍待扩展。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] |
| Fidelity + utility evaluation | 同时用统计相似度和 downstream task performance 评估合成时序。 | 生成数据用于训练或 augmentation。 | 任务选择会影响结论；不能替代 privacy/robustness evaluation。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]] | paper | 提出 FTS-Diffusion: SISC + pattern-conditioned diffusion + pattern evolution；在金融 return series 上评估 fidelity and downstream utility。 | Anonymous under-review; appendices unavailable; no multivariate modeling/privacy/production evaluation. | `p1-p12` |

## 正反例约束

- 正确: 本节点解释的是“时序合成数据生成”问题，FTS-Diffusion 是一个 pattern-aware 方法实例。
- 正确: 评价必须区分 distribution fidelity、stylized facts、downstream utility 和 privacy/robustness。
- 错误: 把金融 return series 的方法直接推广到所有时间序列。
- 错误: 只看 KS/AD 就宣称合成数据对任务有用。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`
- Freshness: `fresh` for local source absorption; not an external latest claim.
- Valid until: `2026-07-23`
- 综合: 当前 seed 显示 time-series synthetic data generation 的关键不是简单采样，而是保留 temporal structure。FTS-Diffusion 的 source delta 是把金融时序的 irregularity/scale-invariance 显式建模，并用 SISC、diffusion generation 和 Markov-style evolution 把 segment-level generation 连接成完整序列。该节点仍缺 TimeGAN/CSDI/TimeVAE/QuantGAN 等基础对照 source，也缺 privacy and robustness 评价。

## 领域态势

- Research dynamics note: not_applicable at topic level; see [[research-dynamics|ML systems Research Dynamics]].
- Dynamics freshness: fresh.
- Latest academic focus summary: current-vault seed focuses on financial time-series pattern-aware diffusion generation.
- Latest industrial focus summary: unknown; no implementation/repo source.
- Open-problem summary: multivariate dependencies, transition distribution shifts, generation quality theory, privacy leakage and reproducibility.
- Next refresh trigger: TimeGAN/CSDI/TimeVAE/QuantGAN or synthetic time-series evaluation sources absorbed.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]] | 创建本 topic seed；记录 irregular/scale-invariant financial time-series generation、SISC、pattern-conditioned diffusion、TMTR/TATR。 | 定义; 解决的问题; 方法族; 代表 Sources; 当前综合 | yes | 后续吸收 broader time-series generation sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| time-series synthetic data generation -> financial ML | `ml-systems/synthetic-data-generation/time-series-synthetic-data-generation; future financial-ml path` | application | Financial returns provide a demanding application context; finance-specific market/risk claims do not transfer to generic time-series generation. | candidate |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-time-series-synthetic-data-generation | is_a | nahida-knowledge-ml-systems-synthetic-data-generation | vault/04_Knowledge/ml-systems/synthetic-data-generation/time-series-synthetic-data-generation.md | high | active_seed |
| nahida-knowledge-time-series-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md | source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| broader time-series generation foundations | 当前只有 FTS-Diffusion 一篇直接 source，related work 未被深读。 | nahida-update / nahida-research-search | high | queued |
| appendices unavailable | SISC pseudo-code、ablation、network structure、extra metrics 无法复核。 | nahida-paper-read / source verification | medium | review |
| multivariate generation | 金融和真实系统常有多变量依赖，FTS-Diffusion 正文只列为 future work。 | nahida-update | medium | queued |
| privacy and leakage evaluation | Synthetic time series 可能泄露训练片段或隐私属性。 | nahida-update / nahida-research-search | high | queued |
| implementation evidence | 无代码/repo，难判断复现与工程成本。 | nahida-github-repo-analyze / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-fts-diffusion-financial-time-series | Created topic seed from FTS-Diffusion; separated source instance details from reusable time-series synthetic data generation problem. | 1 source note | codex |
