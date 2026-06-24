---
id: "nahida-knowledge-synthetic-data-evaluation"
title: "Synthetic data evaluation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "evaluation_axis"
hierarchy_level: "problem"
file_slug: "synthetic-data-evaluation"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems-synthetic-data-generation"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "synthetic-data-evaluation"
primary_ontology_path: "ml-systems/synthetic-data-generation/synthetic-data-evaluation"
secondary_ontology_paths:
  - "ml-systems/synthetic-data-generation/tabular-synthetic-data-generation"
  - "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
relation_edges:
  - from: "nahida-knowledge-synthetic-data-evaluation"
    relation: "is_a"
    to: "nahida-knowledge-ml-systems-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
      - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-evaluation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-evaluation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-evaluation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
    evidence_refs:
      - "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-evaluation"
    relation: "bridges_to"
    to: "nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation"
    evidence_refs:
      - "vault/05_Bridges/synthetic-data-evaluation-to-synthetic-data-privacy-evaluation.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
  - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
  - "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
  - "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
representative_source_refs:
  - "doi:10.1109/ACCESS.2022.3144765"
  - "arxiv:1907.00503v2"
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "pmlr:162:alaa22a"
query_keys:
  - "synthetic data evaluation"
  - "synthetic data utility metrics"
  - "masked data utility evaluation"
  - "attribute fidelity"
  - "bivariate fidelity"
  - "population fidelity"
  - "application fidelity"
  - "Hellinger distance synthetic data"
  - "pairwise correlation difference"
  - "propensity score synthetic data"
  - "machine learning efficacy synthetic data"
  - "SDGym synthetic data evaluation"
  - "utility privacy tradeoff synthetic data"
  - "alpha precision synthetic data"
  - "beta recall synthetic data"
  - "authenticity synthetic data"
  - "sample-level generative model evaluation"
  - "model auditing synthetic data"
aliases:
  - "synthetic data utility evaluation"
  - "synthetic data quality evaluation"
  - "masked data utility metrics"
  - "sample-level synthetic data evaluation"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "synthetic-data-evaluation"
  - "tabular-synthetic-data-generation"
  - "synthetic-data-privacy-evaluation"
tags:
  - "nahida/knowledge"
  - "nahida/evaluation-axis"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation"
  - "nahida-knowledge-20260623-how-faithful-synthetic-data"
source_refs:
  - "doi:10.1109/ACCESS.2022.3144765"
  - "arxiv:1907.00503v2"
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "pmlr:162:alaa22a"
confidence: "medium"
trust_tier: "primary"
---

# Synthetic data evaluation

## 定义与范围

- 定义: Synthetic data evaluation 指评估合成数据是否保留真实数据中对共享、训练、测试、分析或发布有用的性质，并区分 distribution fidelity、dependency fidelity、population-level indistinguishability、downstream application utility、privacy leakage、fairness/robustness 等不同目标。
- 不包含: 某个 generator 的全部实验数值、单个 benchmark 排名、某篇论文的局部 metric，或把 utility/fidelity 指标直接当作 privacy guarantee。
- Canonical terms: `synthetic data evaluation`, `synthetic data utility metrics`, `masked data utility evaluation`
- Aliases/query keys: attribute fidelity, bivariate fidelity, population fidelity, application fidelity, Hellinger, PCD, propensity score, ML efficacy
- Standalone completeness check: 本节点解释合成数据评价的核心对象、四个 utility 维度、与 privacy evaluation 的边界、现有 source-backed routes 和缺口；具体 generator 数值留在 source notes。
- Retrieval role: 查询“合成数据怎么评估”“fidelity/utility 指标有哪些”“为什么单个指标不够”“utility 和 privacy 的关系是什么”时，先读本节点，再读具体数据模态或 source。
- Update scope: 新 source 若涉及 SDMetrics/SDGym、fidelity/utility/privacy/fairness/robustness metrics、synthetic data benchmark、generator comparison、utility-privacy trade-off，应刷新本节点。
- Domain dynamics note: not_applicable；本节点是 direction 下的评价轴，领域态势由 [[research-dynamics|ML systems Research Dynamics]] 维护。

## 背景

model_prior_background: 合成数据评价的难点在于“有用”不是单一性质。一个 synthetic dataset 可能单变量分布很像真实数据，却破坏变量间依赖；也可能训练出可用的下游模型，却泄露训练记录或丢失少数群体；还可能在一个任务上有用，在另一个任务上不可用。因此 evaluation node 必须把 fidelity、utility、privacy 和 task/application context 分开。

当前 source-backed seeds 是 [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]]、[[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]]、[[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]]、[[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]]、[[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics]] 和 [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]]。Dankar et al. 给出 utility 维度框架；Alaa et al. 给出 sample-level fidelity/diversity/generalization 评价与 auditing route；CTGAN/SDGym 给出 tabular benchmark route；FTS-Diffusion 给出 time-series fidelity + downstream utility route；SBPM attacks paper 说明 similarity/fidelity/privacy 不能混同；EndSDG 说明 private evaluation/tuning 也属于 release boundary。

## 基础概念判断

- 是否是基础概念/方向/问题: `evaluation_axis/problem`
- 为什么足够通用: 它可组织 tabular/time-series/relational synthetic data 的 fidelity、utility、benchmark、privacy、fairness、robustness 和 application-specific evaluation。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Dankar et al. 的四维框架只是一个 source-backed seed；evaluation axis 是跨 generator、跨数据模态、跨应用问题。
- 需要引用的更基础 Knowledge: [[synthetic-data-generation|Synthetic data generation]], [[tabular-synthetic-data-generation|Tabular synthetic data generation]], [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]]。
- 不应拆出的实例/协议/来源: Hellinger、PCD、propensity score、SDGym、SP-np、CTGAN、某个 dataset winner 默认作为方法/指标路线或 source extension，不作为基础节点。

## 解决的问题

| 问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Metric conflict | 不同 synthetic data metrics 可能给出不同 generator 排名。 | Dankar et al. reports exact-winner agreement from slight to moderate. |
| Evaluation dimensionality | 单变量分布、变量对依赖、整体分布可区分性和下游任务效用是不同对象。 | Dankar et al. four dimensions. |
| Benchmark comparability | 不同 synthesizer 需要同一数据集、同一 split、同一指标 protocol 才能比较。 | Dankar et al.; CTGAN/SDGym. |
| Data modality dependence | 表格、时序、金融、医疗等模态的关键结构不同，不能只复用一个视觉/文本式质量指标。 | CTGAN and FTS-Diffusion. |
| Utility/privacy mismatch | utility/fidelity 高不代表匿名或隐私安全；privacy evaluation 需要威胁模型、DP 或攻击审计。 | SBPM attacks paper; Dankar et al. p10 caveat. |
| Task-specific utility | 合成数据在一个下游任务上可用，不代表所有分析都可用。 | Dankar et al. uses classification only and marks limitation. |
| Sample-level diagnostics | Dataset-level score 不能指出哪个 synthetic sample 噪声、低 fidelity 或疑似复制训练样本。 | Alaa et al. p1-p6 |
| Generalization/copying risk | 生成模型可能通过 memorization 获得高 fidelity/diversity，却不真正生成新样本。 | Alaa et al. Authenticity metric |
| Post-hoc model auditing | 已训练 generator 的输出可通过 sample-level precision/authenticity 过滤来改善质量。 | Alaa et al. p2, p6-p8 |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[synthetic-data-generation|Synthetic data generation]] | child_of / evaluation_axis | Parent node already had synthetic data evaluation as candidate; Dankar et al. supplies dedicated multi-dimensional utility evidence. | active_seed |
| [[ml-systems|ML systems]] | part_of | Synthetic data evaluation governs ML data-sharing/training workflows. | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| fidelity and utility metrics taxonomy | method-family candidate | 若后续吸收 SDMetrics/SDGym/foundation sources，可拆为完整 metric taxonomy。 | Dankar et al.; CTGAN | queued |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | sibling evaluation axis | Privacy evaluation 与 utility/fidelity evaluation 强相关但不能合并；需要 threat model、DP、attack auditing。 | SBPM attacks paper; EndSDG; current bridge | active_seed as sibling/bridge |
| modality-specific evaluation | application/topic candidate | time-series、tabular、relational、image/text synthetic data 的评价轴不同。 | FTS-Diffusion; CTGAN | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Attribute fidelity | 比较每个属性的单变量分布、类型、范围或基础统计。 | 需要确认 synthetic columns 保留基本结构并可被同一代码处理。 | 不能捕捉变量间关系和下游任务。 | [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|Dankar et al.]] |
| Bivariate fidelity | 比较变量对之间的相关结构，例如 PCD。 | 表格/结构化数据中变量依赖重要。 | 主要捕捉 pairwise/linear dependency，不覆盖高阶关系。 | same source |
| Population fidelity | 合并真实/合成 rows，用 distinguishability/propensity 等测整体分布相似度。 | 需要 global distribution signal 或 generator comparison。 | 可能奖励过拟合；不能代表 privacy guarantee。 | same source |
| Application fidelity / ML efficacy | 在 synthetic data 上训练模型，在 real test data 上测试，观察 accuracy/F1/R2 等。 | synthetic data 用于训练、探索模型或辅助选择 classifier。 | 任务依赖强；一个应用表现不能代表所有应用。 | Dankar et al.; [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] |
| Benchmark protocol | 固定数据集、splits、generator settings、重复采样、metrics 与 aggregation。 | 比较多个 generator 或追踪模型改进。 | benchmark coverage 和默认设置会影响结论。 | Dankar et al.; CTGAN/SDGym |
| Modality-aware evaluation | 根据数据模态保留关键结构，例如时序 dependence、heavy tails、absolute-return autocorrelation。 | time-series/financial/relational 等非静态 tabular 场景。 | 需要领域指标，不能只用通用 Hellinger/PCD。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] |
| Sample-level fidelity/diversity/generalization | 用 `α-Precision`、`β-Recall` 和 `Authenticity` 分别评价 synthetic samples 是否落入真实典型区域、生成分布是否覆盖真实变化、以及样本是否疑似复制训练数据。 | 需要诊断生成模型 failure modes 或敏感数据场景的 copying risk。 | 依赖 embedding、support estimation 和 nearest-neighbor distance；Authenticity 不是 DP guarantee。 | [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|Alaa et al.]] |
| Post-hoc model auditing | 基于 sample-level precision/authenticity 丢弃低质量或 unauthentic samples，以不改 generator 的方式改善 synthetic dataset。 | 可访问 generated samples，且过滤本身不会泄露训练数据。 | 若 filtering/metric API 暴露给外部，也要纳入 privacy threat model。 | [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|Alaa et al.]] |
| [[synthetic-data-privacy-evaluation|Privacy evaluation boundary]] | 把 generator、metrics、filters、release workflow、queries 和 DP budget 放入 threat model。 | 合成数据用于共享、匿名化或敏感数据发布。 | utility/fidelity metrics 只能辅助，不构成隐私证明。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] |
| Private evaluation/tuning | 在 MPC/DP boundary 内评估 quality thresholds、votes 和 hyperparameter tuning。 | 多 custodian 共同生成合成数据，且中间 evaluation 输出敏感。 | 增加 MPC/DP 成本；DP preprocessing 仍有缺口。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]] | paper | 创建 synthetic data evaluation active_seed；把 utility 分成 attribute、bivariate、population、application 四维；证明单一指标不足以预测整体质量。 | tabular/microdata style; one representative metric per dimension; application fidelity only classification; no privacy guarantee. | `p1-p10` |
| [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]] | paper | 补充 sample-level evaluation route：`α-Precision` 评价 fidelity，`β-Recall` 评价 diversity，`Authenticity` 评价 generalization/copying，并支持 post-hoc auditing。 | 依赖 embedding/support estimator；Authenticity 是 copying diagnostic，不是 formal privacy guarantee；code repo not analyzed. | `p1-p17` |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | paper | 给出 tabular benchmark route: likelihood fitness + ML efficacy；SDGym/CTGAN 作为 generator comparison seed。 | no privacy guarantee; benchmark/data scope limited. | `p1-p15` |
| [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]] | paper | 说明 time-series synthetic data 评价要看 distribution fidelity 和 downstream utility，并保留领域结构。 | financial time-series only; no privacy. | `p1-p12` |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics]] | paper | 把 synthetic data evaluation 的 privacy boundary 独立出来，说明 similarity metrics 不能作为匿名保证。 | tabular attacks; attack interface assumptions. | `p1-p19` |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | paper | 补充 collaborative SDG 中 private evaluation/tuning 的工程边界。 | arXiv preprint; DP preprocessing gap. | `p1-p15` |

## 正反例约束

- 正确: 评价 synthetic data 时同时问 fidelity、utility、privacy、fairness/robustness、application context。
- 正确: 把 `Hellinger/PCD/propensity/accuracy` 等指标写成评价路线，而不是基础概念。
- 正确: 对表格数据和时序数据采用不同的领域结构指标。
- 错误: 用一个指标代表 synthetic data 的全部质量。
- 错误: 因为 synthetic data 在 utility metrics 上表现好，就推断它 privacy-safe。
- 错误: 把某个 generator 在某个 benchmark 上的第一名当成跨任务结论。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`
- Freshness: `fresh` for local source absorption; not an external latest claim.
- Valid until: `2026-07-23`
- 综合: 当前节点是 active_seed。Dankar et al. 把 synthetic/masked data utility 明确拆成四个维度: attribute fidelity、bivariate fidelity、population fidelity 和 application fidelity，并用 19 个数据集说明 exact winner 上的 metric agreement 并不稳定，指标间除 PCD-Hellinger 外相关性较低，因此不能用单一 metric 代表整体质量。Alaa et al. 进一步把 evaluation 推到 sample-level：`α-Precision` 诊断 fidelity，`β-Recall` 诊断 diversity，`Authenticity` 诊断 generator 是否复制训练数据，并由此支持 post-hoc model auditing。CTGAN/SDGym 提供 tabular benchmark route，FTS-Diffusion 提醒 time-series 评价必须保留时序/金融结构，SBPM attacks paper 和 EndSDG 则把 privacy release、private evaluation/tuning 从 utility evaluation 中拆出来。当前最稳的知识结论是: synthetic data evaluation 必须是多维且上下文相关的；dataset-level utility/fidelity 可以帮助选择 generator，sample-level metrics 可以诊断和过滤低质量样本，但它们都不能替代 privacy guarantee 或 threat-model-specific auditing。

## 领域态势

> not_applicable for this L3 evaluation axis. See [[research-dynamics|ML systems Research Dynamics]].

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]] | 新建 synthetic data evaluation 节点；把 queue 误分到 privacy/distributed-learning 的记录纠正为 utility evaluation；补充四维 metric framework 和 no-single-metric caveat。 | 定义; 解决的问题; 方法族; 代表 Sources; Bridge Links | yes | 下一篇 `How Faithful is your Synthetic Data?` 应优先吸收到本节点 |
| [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]] | 补充 sample-level fidelity/diversity/generalization 评价路线；把 `α-Precision`、`β-Recall`、`Authenticity` 和 model auditing 纳入本评价轴；纠正队列误分到 privacy/distributed-learning。 | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续若分析代码仓库，可补 implementation evidence |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | 作为 tabular benchmark/ML efficacy source 支撑本节点。 | 方法族; 代表 Sources | no | 若读取 SDGym repo，可刷新 benchmark implementation evidence |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics]] | 确认 privacy evaluation 与 utility/fidelity evaluation 必须分开。 | 背景; 方法族; Bridge Links | yes | 后续 DP synthetic data foundation 后收窄 bridge |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[synthetic-data-evaluation-to-synthetic-data-privacy-evaluation|Synthetic data evaluation -> synthetic data privacy evaluation]] | `ml-systems/synthetic-data-generation/synthetic-data-evaluation; ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | tension, evaluation_transfer, privacy_boundary | Utility/fidelity metrics can rank generator quality, but do not transfer into anonymity or release privacy; privacy evaluation needs DP or attack auditing. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-synthetic-data-evaluation | is_a | nahida-knowledge-ml-systems-synthetic-data-generation | source note + parent node | high | active_seed |
| nahida-knowledge-synthetic-data-evaluation | evidenced_by | vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md | source note | high | active_seed |
| nahida-knowledge-synthetic-data-evaluation | evidenced_by | vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md | source note | high | active_seed |
| nahida-knowledge-synthetic-data-evaluation | evidenced_by | vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md | source note | high | active_seed |
| nahida-knowledge-synthetic-data-evaluation | bridges_to | nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| evaluation foundation/survey sources | 当前节点主要由一篇 utility paper 和若干 generator/application papers 支撑，仍缺 SDMetrics/SDGym/foundation survey。 | nahida-research-search / nahida-update | high | queued |
| non-tabular evaluation | 当前 strong evidence 偏 tabular/time-series，缺 image/text/relational synthetic data evaluation。 | nahida-update | medium | queued |
| utility threshold and governance | Dankar et al. 明确不能回答 acceptable utility/privacy threshold，需要更多应用/治理来源。 | nahida-research-search | medium | queued |
| privacy/fairness/robustness integration | privacy 已有 bridge，但 fairness/robustness 还缺 source-backed nodes。 | nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation | Created synthetic data evaluation active_seed node and linked it to synthetic data privacy evaluation. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-how-faithful-synthetic-data | Added sample-level evaluation/auditing route from Alaa et al. and refreshed the utility/privacy boundary around Authenticity. | 1 source note | codex |
