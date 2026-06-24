---
id: "nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation"
title: "Synthetic data evaluation -> synthetic data privacy evaluation"
original_title: ""
file_slug: "synthetic-data-evaluation-to-synthetic-data-privacy-evaluation"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_topic"
bridge_status: "active_seed"
endpoint_paths:
  - "ml-systems/synthetic-data-generation/synthetic-data-evaluation"
  - "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
endpoint_knowledge_refs:
  - "nahida-knowledge-synthetic-data-evaluation"
  - "nahida-knowledge-synthetic-data-privacy-evaluation"
from_domain: "ml-systems"
to_domain: "ml-systems"
from_direction: "synthetic-data-generation"
to_direction: "synthetic-data-generation"
from_topic: "synthetic-data-evaluation"
to_topic: "synthetic-data-privacy-evaluation"
relation_types:
  - "tension"
  - "evaluation_transfer"
  - "privacy_boundary"
directionality: "two_way"
relationship_thesis: "Synthetic data utility evaluation can rank generators across fidelity and application dimensions, but those dimensions do not establish release privacy; privacy evaluation must add an explicit threat model, Differential Privacy or attack auditing, and private handling of metrics, filters and tuning outputs."
transferability: "medium"
non_transfer_boundary: "Attribute fidelity, bivariate fidelity, population fidelity, propensity indistinguishability and downstream ML accuracy do not transfer into anonymity, membership protection, attribute protection, reconstruction resistance, or end-to-end release privacy."
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
  - "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
knowledge_refs:
  - "nahida-knowledge-synthetic-data-evaluation"
  - "nahida-knowledge-synthetic-data-privacy-evaluation"
  - "nahida-knowledge-ml-systems-synthetic-data-generation"
representative_source_refs:
  - "doi:10.1109/ACCESS.2022.3144765"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "pmlr:162:alaa22a"
query_keys:
  - "synthetic data utility privacy tradeoff"
  - "synthetic data evaluation privacy boundary"
  - "fidelity metrics privacy synthetic data"
  - "utility metrics do not imply anonymity"
  - "synthetic data privacy evaluation"
  - "authenticity synthetic data privacy"
  - "data copying synthetic data evaluation"
aliases:
  - "Synthetic data utility/privacy boundary"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "synthetic-data-evaluation"
  - "synthetic-data-privacy-evaluation"
  - "privacy-and-trustworthy-ml"
tags:
  - "nahida/bridge"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation"
  - "nahida-knowledge-20260623-how-faithful-synthetic-data"
source_refs:
  - "doi:10.1109/ACCESS.2022.3144765"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "pmlr:162:alaa22a"
confidence: "high"
trust_tier: "primary"
---

# Synthetic data evaluation -> synthetic data privacy evaluation

## 命名与路径

- Original title: Synthetic data evaluation -> synthetic data privacy evaluation
- File slug: `synthetic-data-evaluation-to-synthetic-data-privacy-evaluation`
- Path safety check: endpoints are existing knowledge IDs in `04_Knowledge`, not source-only metrics or paper titles.

## 连接命题

- From: [[synthetic-data-evaluation|Synthetic data evaluation]]
- To: [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]]
- Endpoint knowledge paths: `ml-systems/synthetic-data-generation/synthetic-data-evaluation`; `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation`
- Relation types: tension, evaluation_transfer, privacy_boundary
- Directionality: two_way
- Relationship thesis: Synthetic data evaluation can compare generator utility through fidelity and application dimensions, but those dimensions cannot establish privacy or anonymity. Privacy evaluation must add explicit adversary capabilities, release-process modeling, DP or attack auditing, and private handling of train-data-dependent metrics and filters.
- 层级路径: 两个 endpoint 都是 [[synthetic-data-generation|Synthetic data generation]] 下的 evaluation axes；bridge 的作用是防止 utility/fidelity 结论被误迁移成 privacy 结论。
- Standalone completeness check: 本 bridge 独立说明 utility evaluation 和 privacy evaluation 的可迁移部分、不可迁移边界和证据。

## 端点范围

| Endpoint | Path | Scope in bridge | Evidence | Notes |
| --- | --- | --- | --- | --- |
| [[synthetic-data-evaluation|Synthetic data evaluation]] | `ml-systems/synthetic-data-generation/synthetic-data-evaluation` | fidelity, diversity, population indistinguishability, application utility, benchmark comparison, sample-level auditing | Dankar et al.; Alaa et al.; CTGAN/SDGym | Provides generator-quality and sample-quality signals. |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | membership/attribute/reconstruction risk, data-copying/generalization risk, DP release boundary, metric leakage, private evaluation/tuning | SBPM attacks paper; EndSDG; Alaa et al. Authenticity | Provides release-safety and copying-risk signals. |

## 端点基础说明

Synthetic data evaluation measures whether generated data preserves useful properties of real data. In the current vault this includes attribute fidelity, bivariate fidelity, population fidelity, application fidelity, ML efficacy, time-series structure, benchmark comparability, sample-level `α-Precision/β-Recall`, and `Authenticity`.

Synthetic data privacy evaluation asks whether the generation and release process leaks training records, attributes or outliers under an explicit threat model. A dataset may be high utility and still unsafe to release if metrics, filters, query access, generator behavior, authenticity checks, or tuning outputs expose train-data information.

## 可迁移知识/模式

| 概念/模式 | 来源方向 | 目标方向 | 可迁移部分 | 不可迁移部分 |
| --- | --- | --- | --- | --- |
| Multi-dimensional utility | synthetic data evaluation | privacy evaluation | Helps state what utility is being traded away when adding privacy mechanisms. | Does not define privacy loss or adversary power. |
| Population indistinguishability | synthetic data evaluation | privacy evaluation | Can flag whether synthetic rows are easily distinguished from real rows. | Indistinguishability from a classifier is not anonymity or DP. |
| Application fidelity | synthetic data evaluation | privacy evaluation | Useful for measuring utility under privacy-preserving generation. | High accuracy/F1 can coexist with membership or reconstruction risk. |
| Authenticity / copying diagnostic | synthetic data evaluation | privacy evaluation | Flags whether a generator may be memorizing or copying training samples. | It is not DP, anonymity, or a complete privacy attack model. |
| Attack auditing | privacy evaluation | synthetic data evaluation | Adds worst-case and adversarial checks to quality reports. | Attack failure is not a complete guarantee. |
| Private evaluation/tuning | privacy evaluation | synthetic data evaluation | Shows that evaluation metrics themselves may need privacy protection in collaborative release. | Adds computation/governance cost and may reduce observability. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Utility metric taxonomy | `synthetic-data-evaluation` | `synthetic-data-privacy-evaluation` | Use attribute/bivariate/population/application fidelity to describe utility side of privacy trade-off. | Dankar et al. p2-p4, p10 | Could be mistaken for privacy proof. |
| No-single-metric caveat | `synthetic-data-evaluation` | `synthetic-data-privacy-evaluation` | If no single utility metric captures quality, no single similarity metric should be trusted as privacy guarantee either. | Dankar et al.; SBPM attacks paper | Analogy is structural; privacy requires direct evidence. |
| Authenticity as bridge signal | `synthetic-data-evaluation` | `synthetic-data-privacy-evaluation` | Use low authenticity to flag copying/generalization risk and tune privacy-utility decisions. | Alaa et al. p1-p8 | Does not prove privacy and may itself require train-data access. |
| Metric leakage discipline | `synthetic-data-privacy-evaluation` | `synthetic-data-evaluation` | Treat train-data-dependent metrics/filters as part of release process when outputs are exposed. | SBPM attacks paper; EndSDG | May make evaluation harder to audit publicly. |
| Private threshold/evaluation workflow | `synthetic-data-privacy-evaluation` | `synthetic-data-evaluation` | Keep quality thresholds and votes inside MPC/DP boundary in collaborative release. | EndSDG Algorithm 1 | Requires implementation evidence and DP preprocessing. |

## 类比、依赖或关系边界

- 可迁移: metric taxonomy, benchmark discipline, application-specific utility reporting, explicit trade-off language, attack-aware evaluation mindset.
- 不可迁移: Hellinger, PCD, propensity score, accuracy/F1, SDGym score, SP-np/CTGAN benchmark rank, or high Authenticity cannot be reinterpreted as anonymity, DP, membership safety, attribute safety or reconstruction resistance.
- 关键假设: source evidence remains scoped to tabular/microdata and collaborative synthetic data until more modality-specific sources arrive.
- 失效条件: a report treats utility/fidelity/similarity metrics as sufficient privacy evidence, exposes train-data-dependent metric APIs, or optimizes generator quality without accounting for privacy budget and adversary queries.

## 证据

| Source/Note | 支撑内容 | 置信度 | 局限 |
| --- | --- | --- | --- |
| [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]] | Utility metrics split into attribute, bivariate, population and application fidelity; no single metric predicts multi-dimensional quality; paper does not decide acceptable privacy-utility thresholds. | high | Utility paper; no privacy attack or DP mechanism. |
| [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]] | `Authenticity` measures whether synthetic samples are likely copied from training data; `α-Precision/β-Recall` and auditing provide sample-level utility/fidelity diagnostics. | high | Generative-model evaluation paper; Authenticity is not a formal privacy guarantee and can introduce metric/filter exposure. |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics]] | Similarity/privacy metrics and filters can leak training records; synthetic data privacy needs threat model and attack/DP reasoning. | high | Tabular-focused attack evidence. |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | Evaluation, thresholds, votes and tuning must remain private in collaborative SDG pipeline; final-output-only release boundary matters. | high | ArXiv preprint; DP preprocessing caveat. |

## 路径传播

| Endpoint path | Knowledge update | Relation/index update | Bridge/refresh action | Status |
| --- | --- | --- | --- | --- |
| `ml-systems/synthetic-data-generation/synthetic-data-evaluation` | Created active_seed node and source extension. | Added `bridges_to` and `evidenced_by` relations. | Created this bridge. | done |
| `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | Added bridge link boundary. | Added bridge relation through index. | Created this bridge. | done |
| `ml-systems/synthetic-data-generation` | Added synthetic-data-evaluation as child and utility/privacy bridge. | Added source and relation refs. | Bridge link row. | done |
| `ml-systems/synthetic-data-generation/synthetic-data-evaluation` | Added Alaa et al. sample-level route. | Added `Authenticity` as privacy-boundary evidence. | Refreshed this bridge. | done |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[synthetic-data-evaluation|Synthetic data evaluation]] | New node | Dankar et al. creates reusable utility evaluation axis. | done |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | Bridge link | Privacy evaluation must remain separate from utility metrics. | done |
| [[synthetic-data-generation|Synthetic data generation]] | Child structure and bridge links | Direction now has both utility evaluation and privacy evaluation axes. | done |
| [[tabular-synthetic-data-generation|Tabular synthetic data generation]] | Evaluation route | Current source is tabular/microdata-style evaluation evidence. | done |

## 查询入口

- Query keys:
  - synthetic data utility privacy tradeoff
  - synthetic data evaluation privacy boundary
  - utility metrics do not imply anonymity
  - fidelity versus privacy synthetic data
  - propensity score synthetic data privacy
- Aliases:
  - Synthetic data utility/privacy boundary
- 典型问题:
  - 合成数据在 utility metric 上表现好，能说明它匿名吗?
  - Hellinger、PCD、propensity score 和 accuracy 分别能说明什么，不能说明什么?
  - Authenticity 高能不能说明 synthetic data 没有隐私风险?
  - 为什么 synthetic data evaluation 和 privacy evaluation 要分开?
  - 多方合成数据中 evaluation/tuning 为什么也可能泄露隐私?

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers:
  - 新 synthetic data evaluation、SDMetrics/SDGym、utility benchmark source 被吸收。
  - 新 synthetic data privacy attack、DP synthetic data、private evaluation/tuning source 被吸收。
  - 用户询问 utility/privacy trade-off 或 synthetic data evaluation standards。

## 复核笔记

- 本 bridge 是 active_seed，因为当前 utility side 有一篇直接多维评价 source，privacy side 有 SBPM attacks 与 EndSDG 两条 source。
- 不应把 Dankar et al. 的 SP-np 结果推广为所有场景的最佳 generator；它是本文 tabular/microdata setup 下的 source-specific result。
- 不应把 propensity score indistinguishability 误读为 privacy guarantee；这是 bridge 的主要防误用目标。

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation | Created bridge separating utility/fidelity evaluation from privacy evaluation. | 3 source notes | codex |
| 2026-06-23 | nahida-knowledge-20260623-how-faithful-synthetic-data | Refreshed bridge with Authenticity/data-copying signal and its non-transfer boundary to formal privacy. | 1 source note | codex |
