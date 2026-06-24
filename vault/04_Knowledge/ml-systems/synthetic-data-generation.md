---
id: "nahida-knowledge-ml-systems-synthetic-data-generation"
title: "Synthetic data generation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "synthetic-data-generation"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems"
child_knowledge_refs:
  - "nahida-knowledge-time-series-synthetic-data-generation"
  - "nahida-knowledge-tabular-synthetic-data-generation"
  - "nahida-knowledge-synthetic-data-evaluation"
  - "nahida-knowledge-synthetic-data-privacy-evaluation"
  - "nahida-knowledge-collaborative-synthetic-data-generation"
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
primary_ontology_path: "ml-systems/synthetic-data-generation"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "is_a"
    to: "nahida-knowledge-ml-systems"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
      - "vault/04_Knowledge/ml-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "has_child"
    to: "nahida-knowledge-time-series-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/time-series-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "has_child"
    to: "nahida-knowledge-tabular-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/tabular-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "has_child"
    to: "nahida-knowledge-synthetic-data-evaluation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/synthetic-data-evaluation.md"
      - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
    evidence_refs:
      - "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "has_child"
    to: "nahida-knowledge-synthetic-data-privacy-evaluation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation.md"
      - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "has_child"
    to: "nahida-knowledge-collaborative-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation.md"
      - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "bridges_to"
    to: "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/05_Bridges/synthetic-data-generation-to-privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-synthetic-data-generation"
    relation: "bridges_to"
    to: "nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation"
    evidence_refs:
      - "vault/05_Bridges/synthetic-data-evaluation-to-synthetic-data-privacy-evaluation.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
  - "nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation"
source_note_refs:
  - "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
  - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
  - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
  - "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
representative_source_refs:
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
  - "arxiv:1907.00503v2"
  - "doi:10.1109/ACCESS.2022.3144765"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "pmlr:162:alaa22a"
query_keys:
  - "synthetic data generation"
  - "synthetic data for machine learning"
  - "data augmentation with generated data"
  - "time series synthetic data generation"
  - "financial time series generation"
  - "FTS-Diffusion"
  - "tabular synthetic data generation"
  - "synthetic tabular data"
  - "CTGAN"
  - "conditional tabular GAN"
  - "SDGym"
  - "synthetic data evaluation"
  - "synthetic data utility metrics"
  - "attribute fidelity"
  - "bivariate fidelity"
  - "population fidelity"
  - "application fidelity"
  - "sample-level synthetic data evaluation"
  - "alpha precision synthetic data"
  - "beta recall synthetic data"
  - "authenticity synthetic data"
  - "model auditing synthetic data"
  - "synthetic data privacy evaluation"
  - "similarity-based privacy metrics"
  - "SBPM"
  - "ReconSyn"
  - "Differential Privacy synthetic data release"
  - "collaborative synthetic data generation"
  - "privacy-preserving collaborative SDG"
  - "MPC synthetic data generation"
  - "DP-in-MPC synthetic data"
aliases:
  - "synthetic data"
  - "data synthesis"
  - "生成式合成数据"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "data-augmentation"
  - "time-series-synthetic-data-generation"
  - "tabular-synthetic-data-generation"
  - "synthetic-data-evaluation"
  - "synthetic-data-privacy-evaluation"
  - "collaborative-synthetic-data-generation"
  - "privacy-and-trustworthy-ml"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
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
  - "nahida-knowledge-20260623-ctgan-tabular-synthetic-data"
  - "nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation"
  - "nahida-knowledge-20260623-synthetic-data-privacy-metrics"
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
  - "nahida-knowledge-20260623-how-faithful-synthetic-data"
source_refs:
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
  - "arxiv:1907.00503v2"
  - "doi:10.1109/ACCESS.2022.3144765"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "pmlr:162:alaa22a"
confidence: "medium"
trust_tier: "primary"
---

# Synthetic data generation

## 定义与范围

- 定义: Synthetic data generation 指用生成模型、模拟器、统计机制或程序化方法生成训练、测试、评估或共享用数据，使其在某些分布、结构、任务效用或约束上近似真实数据。
- 不包含: 某个具体 generator 名称、某个 benchmark 数字、单篇论文的局部算法、真实数据采集流程；这些应留在 source note 或 topic source extension。
- Canonical terms: `synthetic data generation`, `data synthesis`, `synthetic data for machine learning`
- Aliases/query keys: synthetic data, data augmentation, generated data, synthetic time series
- Standalone completeness check: 本节点给出方向定义、边界、评价轴、下级主题和当前 source-backed seeds；由于 vault 当前只覆盖 time-series、tabular 和 privacy-evaluation 三条 seeds，本节点保持 `foundation_thin`。
- Retrieval role: 当查询涉及“用生成数据补数据不足”“合成数据是否像真实数据”“合成数据能否改善下游任务”时，先读本节点，再进入具体数据模态或应用。
- Update scope: 新 source 若涉及 GAN/VAE/diffusion synthetic data、tabular/time-series generation、synthetic data evaluation、data augmentation、privacy-preserving synthetic data release，应刷新本节点。
- Domain dynamics note: [[research-dynamics|ML systems Research Dynamics]].

## 背景

model_prior_background: Synthetic data generation 位于 generative modeling、data augmentation、privacy/data governance 和 evaluation 的交界。它不仅关心“模型能否生成看起来像的数据”，还关心生成数据是否保留重要统计结构、是否能改善下游任务、是否泄露敏感信息、是否引入偏差，以及生成数据适用于训练、测试、仿真还是发布共享。

当前 vault 的直接 source-backed seeds 是 [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]]、[[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]]、[[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]]、[[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]]、[[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] 和 [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]]。FTS-Diffusion 把数据稀缺问题具体化到 financial time series，并说明合成数据生成需要同时评估 distribution fidelity 和 downstream utility；CTGAN 把静态表格数据的问题拆成 mixed data types、multimodal continuous columns、imbalanced categorical columns 和 benchmark-based ML efficacy；Dankar et al. 把 utility evaluation 抽成 attribute、bivariate、population 和 application fidelity 四维，并说明单一指标不足以代表整体质量；Alaa et al. 把评价进一步细化到 sample-level fidelity、diversity、generalization 和 model auditing；SBPM attacks paper 补上 privacy release boundary，说明 similarity-based privacy metrics 不能替代 end-to-end DP 或攻击审计；EndSDG 则把合成数据发布扩展到多 data custodians 场景，要求 preprocessing、evaluation、hyperparameter tuning 和 final release 全部处在 input/output privacy 边界内。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction`
- 为什么足够通用: 它可组织 tabular synthetic data、time-series synthetic data、image/audio synthetic data、privacy-preserving synthetic data、simulation data、fidelity/utility/privacy evaluation 等多个 topic。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: FTS-Diffusion 只是一个 financial time-series source instance；Synthetic data generation 是更宽的 ML systems 数据层方向。
- 需要引用的更基础 Knowledge: [[ml-systems|ML systems]]；相邻但未建全的 generative modeling/time-series modeling foundations。
- 不应拆出的实例/协议/来源: FTS-Diffusion、SISC、CTGAN、TVAE adaptation、SDGym、某个单一 synthetic-data benchmark 默认作为 source extension，不作为方向节点。

## 解决的问题

| 问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Data scarcity | 真实数据少、昂贵、历史有限或难以重新采集时，用生成数据补充训练/评估。 | FTS-Diffusion 针对金融历史数据有限。 |
| Distribution fidelity | 生成数据是否保留真实数据的分布、时序依赖、尾部风险或领域特征。 | FTS-Diffusion 检查 heavy tails、absolute-return autocorrelation decay、KS/AD。 |
| Downstream utility | 生成数据是否真的改善或至少不伤害下游任务。 | FTS-Diffusion 使用 TMTR/TATR 与 LSTM prediction MAPE。 |
| Mixed-type tabular fidelity | 表格数据混合连续、binary、多类别离散列，且连续列可能多峰、类别列可能高度不平衡。 | CTGAN 提出 mode-specific normalization、conditional generator 和 training-by-sampling。 |
| Benchmark comparability | 不同 synthesizer 需要在相同 simulated/real datasets 与相同 fidelity/utility metrics 下比较。 | CTGAN/SDGym 使用 likelihood fitness 与 ML efficacy。 |
| Multi-dimensional utility evaluation | Attribute、bivariate、population 与 application fidelity 衡量不同质量对象，单一 metric 不能代表整体 utility。 | Dankar et al. 在 19 个数据集上比较 DS、SDV、SP-p、SP-np，并发现指标间相关性有限。 |
| Sample-level evaluation and auditing | 需要知道单个 synthetic sample 是否 realistic、是否覆盖真实变化、是否疑似复制训练样本，并能过滤低质量样本。 | Alaa et al. introduces α-Precision, β-Recall, Authenticity and model auditing. |
| Privacy and governance boundary | 合成数据是否会泄露训练数据、是否能发布共享。 | SBPM attacks paper shows similarity metrics can leak membership, attributes and outliers. |
| Evaluation mismatch | 看起来像真实数据不等于任务有用，任务有用也不等于安全可发布。 | FTS-Diffusion/CTGAN cover fidelity/utility; SBPM attacks paper covers privacy mismatch. |
| Collaborative multi-custodian release | 多个 data custodians 需要协作生成合成数据，但原始数据、质量阈值、评估 metrics 和调参中间结果都可能泄露隐私。 | EndSDG proposes MPC + DP-in-MPC end-to-end pipeline. |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[ml-systems|ML systems]] | child_of | FTS-Diffusion source absorption | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[time-series-synthetic-data-generation|Time-series synthetic data generation]] | problem/topic | Time series generation 需要保留 temporal dependence、pattern recurrence、transition dynamics 和下游时序任务 utility，评价方式不同于静态 tabular/image data。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] | active_seed |
| [[tabular-synthetic-data-generation|Tabular synthetic data generation]] | problem/topic | 静态表格数据需要同时处理 mixed data types、multimodal continuous columns、sparse one-hot artifacts、imbalanced categorical columns 和 ML efficacy 评估。 | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] | active_seed |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | evaluation_axis/problem | 合成数据的 privacy boundary 不能从 fidelity/utility/similarity 自动推出，需要 threat model、DP 或攻击审计。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] | active_seed |
| [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]] | problem/topic | 多数据持有方合成数据发布需要同时处理 input privacy、output privacy、preprocessing、private evaluation、tuning 和 final release budget。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] | active_seed |
| [[synthetic-data-evaluation|Synthetic data evaluation]] | evaluation_axis | Fidelity、utility、privacy、fairness 和 robustness 常常冲突，需要跨 source 评价轴；Dankar et al. 提供 utility/fidelity 四维框架，SBPM/EndSDG 约束 privacy 边界。 | [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|Dankar et al.]]; FTS-Diffusion; CTGAN; SBPM attacks paper | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| GAN/VAE/diffusion generators | 学习真实数据分布并从 latent/noise 采样新数据。 | 数据模态可被生成模型表示，且目标是 augmentation/simulation/sharing。 | 可能 mode collapse、overfit、泄露数据或无法保留任务相关结构。 | source queue / model-prior background |
| [[time-series-synthetic-data-generation|Time-series synthetic data generation]] | 生成数据时保留 temporal dependence、patterns、transition 和时序任务效用。 | 数据有时间顺序，任务依赖动态结构。 | 固定窗口方法容易切断 variable-length patterns；评估需要 fidelity + utility。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] |
| [[tabular-synthetic-data-generation|Tabular synthetic data generation]] | 生成 mixed-type rows，并保留连续/离散列的分布、类别覆盖和下游 ML utility。 | 数据是结构化表格，包含连续列和离散列。 | 类别不平衡、rare subgroups、业务约束、隐私泄露和 relational/multi-table data 仍需额外处理。 | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] |
| Pattern-aware generation | 先识别可重复 pattern，再生成 segment，再学习 transition。 | 时序包含 irregular recurrence 或 scale variation。 | pattern discovery 质量决定 generation；对 regime shifts 和 multivariate dependencies 仍薄。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] |
| Conditional tabular generation | 用 condition vector 指定 discrete column/category，并配合 training-by-sampling 提升 rare categories 训练曝光。 | 表格离散列高度不平衡，或需要按类别生成/增强数据。 | 不自动保证因果有效、隐私安全或业务规则一致。 | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] |
| Fidelity/utility evaluation | 同时检查统计相似度和下游任务表现。 | 合成数据用于训练或评估模型。 | 指标可能与真实业务目标不一致；privacy/fairness 需额外测量。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] |
| [[synthetic-data-evaluation|Synthetic data evaluation]] | 把 utility 拆成 attribute fidelity、bivariate fidelity、population fidelity 和 application fidelity，并用多指标 protocol 比较 generators。 | 需要评价 generic synthetic/masked data utility 或比较多个 synthesizers。 | 单个代表指标不能覆盖全部任务；utility 不能自动转成 privacy guarantee。 | [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|Dankar et al.]] |
| Sample-level synthetic data evaluation | 用 `α-Precision`、`β-Recall`、`Authenticity` 分别检查 fidelity、diversity 和 generalization/copying，并支持 post-hoc sample filtering。 | 需要诊断 generator failure modes、敏感数据 copying risk 或单样本质量。 | embedding/support/nearest-neighbor assumptions 影响结果；Authenticity 不是正式隐私保证。 | [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|Alaa et al.]] |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | 检查生成、过滤、度量和发布流程是否泄露训练记录、属性或 outliers。 | 合成数据用于共享、匿名化、合规或敏感数据发布。 | 相似性指标只是 heuristic；攻击失败也不是 formal guarantee；end-to-end DP/威胁模型仍必需。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] |
| [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]] | 用 MPC 保护多方输入，用 DP 保护最终输出，并把 preprocessing/evaluation/tuning 放进私有流水线。 | 多机构不能集中原始数据，但需要发布合成数据供共享或下游分析。 | MPC cost、DP preprocessing、质量阈值治理和中间结果泄露边界仍需谨慎处理。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]] | paper | 创建 synthetic data generation direction seed；补充 time-series/financial application，说明 synthetic data 应同时看 fidelity and downstream utility。 | Anonymous under-review; appendices unavailable; univariate financial assets; no privacy or production evaluation. | `p1-p12` |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | paper | 新增 tabular synthetic data generation topic seed；补充 mixed-type tabular generation、conditional GAN route 和 SDGym-style benchmark/evaluation。 | no privacy guarantee; no theory for mixed GAN success; TVAE competitive; repo not analyzed in this run. | `p1-p15` |
| [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]] | paper | 新增 synthetic data evaluation active_seed；补充 attribute/bivariate/population/application 四维 utility framework，并说明没有单一 metric 能预测多维质量。 | tabular/microdata style; application fidelity only classification; no privacy guarantee. | `p1-p10` |
| [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]] | paper | 补充 sample-level evaluation/auditing route：`α-Precision`、`β-Recall`、`Authenticity` 用于诊断 fidelity、diversity、generalization/copying，并支持过滤低质量 synthetic samples。 | 不是 generator 训练算法；Authenticity 不是 DP guarantee；code repo not analyzed. | `p1-p17` |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | paper | 新增 synthetic data privacy evaluation active seed；说明 SBPMs、metric APIs 和 filters 不能作为匿名保证，并给出 DifferenceAttack/ReconSyn。 | tabular-focused; attack model requires generator/metric access; not a DP synthetic data construction. | `p1-p19` |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | paper | 新增 collaborative synthetic data generation active seed；把多方合成数据发布组织成 MPC input privacy + DP output privacy + private preprocessing/evaluation/tuning pipeline。 | arXiv preprint; DP quantile binning not complete; code not analyzed; genomic experiment is preliminary. | `p1-p15` |

## 正反例约束

- 正确: 把 synthetic data generation 作为 ML systems 的数据层方向；具体生成框架作为 source extension。
- 正确: 对合成数据区分 fidelity、utility、privacy、fairness、robustness 等评价目标。
- 正确: 把 privacy release boundary 写成 process-level 问题，包含 generator、metrics、filters、query access 和 DP budget。
- 错误: 把 FTS-Diffusion 或 SISC 当作基础概念。
- 错误: 把 CTGAN、TVAE 或 SDGym 当作 synthetic data generation 上层概念本身。
- 错误: 把“合成数据”自动当作 privacy-preserving data release。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`
- Freshness: `fresh` for local source absorption; not an external latest claim.
- Valid until: `2026-07-23`
- 综合: 当前 synthetic data generation 仍是 foundation_thin direction，但已形成五个直接子问题/评价轴: time-series synthetic data generation、tabular synthetic data generation、synthetic data evaluation、synthetic data privacy evaluation 与 collaborative synthetic data generation。FTS-Diffusion 提供的关键结构是: 合成数据生成不能只做“数据看起来像”，还要根据数据模态保留关键结构并验证下游效用；对金融时序而言，关键结构是 irregular and scale-invariant temporal patterns。CTGAN 补充静态表格数据的另一组结构约束: mixed data types、multimodal continuous columns、imbalanced categorical columns 和 benchmark-based ML efficacy。Dankar et al. 把 utility evaluation 抽成 attribute、bivariate、population、application 四维，并说明指标之间可能冲突，单一指标不足以代表整体质量。Alaa et al. 补上 sample-level diagnostics：`α-Precision`、`β-Recall`、`Authenticity` 可以分别定位 fidelity、diversity、training-data copying，并用 auditing/filtering 改善已生成样本。SBPM attacks paper 补充 privacy boundary: similarity/fidelity/utility 指标不能推导匿名性，metrics、filters 和 query access 本身也可能泄露训练记录。EndSDG 则补充多数据持有方发布边界: 当合成数据来自多个 silos，preprocessing、evaluation、threshold voting 和 hyperparameter tuning 都必须进入 trust boundary，才能把 input privacy 与 output privacy 分开管理。

## 领域态势

- Research dynamics note: [[research-dynamics|ML systems Research Dynamics]]
- Dynamics freshness: fresh for current-vault evidence.
- Latest academic focus summary: 当前 vault 新增 synthetic data generation seeds，分别关注 time-series/financial data scarcity、mixed-type tabular data generation、synthetic data privacy evaluation 和 collaborative multi-custodian synthetic data publishing；共同强调 fidelity、utility、input privacy、output privacy 与 release-process boundary 必须分开处理。
- Latest industrial focus summary: unknown; no repo/production evidence in current run.
- Open-problem summary: foundation sources、DP synthetic data、collaborative/federated SDG taxonomy、attack/audit taxonomy、evaluation standards、multivariate/regime-shift robustness。
- Next refresh trigger: 后续 synthetic/tabular/time-series/privacy/collaborative synthetic data papers absorbed.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]] | 新增 synthetic data generation direction 和 time-series synthetic data generation topic seed；纠正队列误分到 blockchain/data availability。 | 定义; 下级结构; 方法族; 代表 Sources; 当前综合 | yes | 吸收后续 synthetic data evaluation/tabular/time-series sources 后补 foundation |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | 新增 tabular synthetic data generation topic；补充 CTGAN/TVAE/SDGym benchmark route；纠正队列误分到 privacy/distributed learning。 | 背景; 解决的问题; 下级结构; 方法族; 代表 Sources; 当前综合 | yes | 吸收后续 tabular/DP/evaluation sources 后补 taxonomy |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | 新增 synthetic data privacy evaluation 问题节点；纠正队列误分到 ZK proof foundations；补充 SBPM/DP/attack-auditing privacy boundary。 | 背景; 解决的问题; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 DP synthetic data 和 collaborative synthetic data sources 后校准 |
| [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]] | 新增 synthetic data evaluation 评价轴；纠正队列误分到 privacy/distributed-learning 和误识别 arXiv ID；补充四维 utility metric taxonomy。 | 背景; 解决的问题; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 下一篇 synthetic data fidelity/evaluation source 应优先吸收到该节点 |
| [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]] | 补充 sample-level fidelity/diversity/generalization 评价与 model auditing；纠正队列误分到 privacy/distributed-learning。 | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 若后续分析 paper-listed GitHub repos，可补 implementation evidence |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | 新增 collaborative synthetic data generation 问题节点；纠正队列中过宽 distributed-learning 归属；补充多 data custodians 下 input privacy、output privacy、private preprocessing/evaluation/tuning 的 pipeline route。 | 背景; 解决的问题; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 CaPS、FLAIM、DP synthetic data 和 DP quantile preprocessing sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]] | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation; ml-systems/privacy-and-trustworthy-ml` | tension, privacy_boundary, evaluation_transfer | Synthetic data may support data sharing, but privacy does not transfer from similarity/fidelity metrics; it requires DP or threat-model-specific attack evaluation. | active_seed |
| [[synthetic-data-evaluation-to-synthetic-data-privacy-evaluation|Synthetic data evaluation -> synthetic data privacy evaluation]] | `ml-systems/synthetic-data-generation/synthetic-data-evaluation; ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | tension, evaluation_transfer, privacy_boundary | Utility/fidelity metrics can rank generator quality, but do not transfer into anonymity or release privacy. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-ml-systems-synthetic-data-generation | is_a | nahida-knowledge-ml-systems | vault/04_Knowledge/ml-systems/synthetic-data-generation.md | medium | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | has_child | nahida-knowledge-time-series-synthetic-data-generation | vault/04_Knowledge/ml-systems/synthetic-data-generation/time-series-synthetic-data-generation.md | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | has_child | nahida-knowledge-tabular-synthetic-data-generation | vault/04_Knowledge/ml-systems/synthetic-data-generation/tabular-synthetic-data-generation.md | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | has_child | nahida-knowledge-synthetic-data-evaluation | vault/04_Knowledge/ml-systems/synthetic-data-generation/synthetic-data-evaluation.md | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | has_child | nahida-knowledge-synthetic-data-privacy-evaluation | vault/04_Knowledge/ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation.md | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | has_child | nahida-knowledge-collaborative-synthetic-data-generation | vault/04_Knowledge/ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation.md | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md | source note | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md | source note | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md | source note | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md | source note | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md | source note | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md | source note | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | bridges_to | nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml | bridge note | high | active_seed |
| nahida-knowledge-ml-systems-synthetic-data-generation | bridges_to | nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| synthetic data foundation sources | 当前只有 FTS-Diffusion source，不足以代表 synthetic data 全景。 | nahida-research-search / nahida-update | high | queued |
| tabular synthetic data sources | CTGAN 创建了 tabular seed，但仍缺 DP/tabular diffusion/tabular LLM/relational data synthesizers。 | nahida-update | high | active_seed_gap |
| synthetic data privacy evaluation | 已有 SBPM attacks seed，但 DP synthetic data、attack taxonomy、production/privacy-report evidence 仍不足。 | nahida-update / nahida-research-search | high | active_seed_gap |
| collaborative/federated synthetic data generation | EndSDG 是 strong active seed，但 CaPS/FLAIM/DP preprocessing 等 primary sources 还没吸收。 | nahida-update / nahida-research-search | high | active_seed_gap |
| production/repo evidence | 缺工具链、dataset release、benchmark implementation。 | nahida-github-repo-analyze / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-fts-diffusion-financial-time-series | Created synthetic data generation direction seed from FTS-Diffusion and attached time-series synthetic data generation child topic. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-ctgan-tabular-synthetic-data | Added tabular synthetic data generation child topic from CTGAN and refreshed evaluation/method routes. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation | Added synthetic data evaluation child/evaluation axis from Dankar et al. and linked utility evaluation to privacy evaluation. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-synthetic-data-privacy-metrics | Added synthetic data privacy evaluation child/evaluation axis from SBPM attacks paper and created bridge to privacy/trustworthy ML. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-collaborative-synthetic-data-generation | Added collaborative synthetic data generation child problem from EndSDG and refreshed the synthetic-data/privacy bridge. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-how-faithful-synthetic-data | Added sample-level synthetic data evaluation and auditing as a route under the existing evaluation axis. | 1 source note | codex |
