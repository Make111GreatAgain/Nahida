---
id: "nahida-knowledge-tabular-synthetic-data-generation"
title: "Tabular synthetic data generation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "topic"
file_slug: "tabular-synthetic-data-generation"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems-synthetic-data-generation"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "tabular-synthetic-data-generation"
primary_ontology_path: "ml-systems/synthetic-data-generation/tabular-synthetic-data-generation"
secondary_ontology_paths:
  - "ml-systems/synthetic-data-generation/synthetic-data-evaluation"
  - "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
  - "ml-systems/privacy-and-trustworthy-ml"
relation_edges:
  - from: "nahida-knowledge-tabular-synthetic-data-generation"
    relation: "is_a"
    to: "nahida-knowledge-ml-systems-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/tabular-synthetic-data-generation.md"
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-tabular-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-tabular-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-tabular-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-tabular-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-tabular-synthetic-data-generation"
    relation: "bridges_to"
    to: "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/05_Bridges/synthetic-data-generation-to-privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-tabular-synthetic-data-generation"
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
  - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
  - "vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md"
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
representative_source_refs:
  - "arxiv:1907.00503v2"
  - "doi:10.1109/ACCESS.2022.3144765"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
query_keys:
  - "tabular synthetic data generation"
  - "synthetic tabular data"
  - "CTGAN"
  - "conditional tabular GAN"
  - "mode-specific normalization"
  - "training-by-sampling"
  - "SDGym"
  - "machine learning efficacy synthetic data"
  - "multi-dimensional synthetic data evaluation"
  - "attribute fidelity"
  - "bivariate fidelity"
  - "population fidelity"
  - "application fidelity"
  - "propensity score synthetic data"
  - "synthetic tabular data privacy"
  - "similarity-based privacy metrics"
  - "ReconSyn"
  - "synthetic data privacy evaluation"
  - "Private-PGM"
  - "select-measure-generate synthetic data"
  - "privacy-preserving tabular synthetic data"
aliases:
  - "synthetic tabular data"
  - "tabular data synthesis"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "tabular-synthetic-data-generation"
  - "conditional-tabular-gan"
  - "synthetic-data-evaluation"
  - "synthetic-data-privacy-evaluation"
  - "privacy-and-trustworthy-ml"
tags:
  - "nahida/knowledge"
  - "nahida/topic"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-ctgan-tabular-synthetic-data"
  - "nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation"
  - "nahida-knowledge-20260623-synthetic-data-privacy-metrics"
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
source_refs:
  - "arxiv:1907.00503v2"
  - "doi:10.1109/ACCESS.2022.3144765"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
confidence: "medium"
trust_tier: "primary"
---

# Tabular synthetic data generation

## 定义与范围

- 定义: Tabular synthetic data generation 指生成结构化表格 rows，使合成数据在列类型、联合分布、类别比例、约束关系和下游 ML utility 上足够接近真实表格数据。
- 不包含: 某个具体 generator 名称、单篇 benchmark 的全部数值、数据库事务/存储系统、或者未经证明的隐私发布保证。
- Canonical terms: `tabular synthetic data generation`, `synthetic tabular data`, `tabular data synthesis`
- Aliases/query keys: CTGAN, conditional tabular GAN, mode-specific normalization, training-by-sampling, SDGym
- Standalone completeness check: 本节点给出问题定义、边界、主要难点、方法路线、评价轴和当前 source-backed seed；由于当前只有 CTGAN 一篇直接 source，仍是 `active_seed` 而非完整综述。
- Retrieval role: 当查询涉及“表格合成数据怎么生成”“CTGAN 解决什么问题”“合成表格数据如何评估”时，先读本节点，再进入 CTGAN source note。
- Update scope: 新 source 若涉及 CTGAN/TVAE/PrivBN/PATE-GAN/tabular diffusion/tabular LLM/synthetic data evaluation/privacy release，应刷新本节点。
- Parent: [[synthetic-data-generation|Synthetic data generation]]

## 背景

model_prior_background: 表格数据与图像、文本、时序不同。表格 rows 往往混合连续列、二元列、多类别离散列和业务约束；连续列可能多峰且非 Gaussian，离散列可能高度不平衡。合成表格数据的系统目标通常不是“肉眼像”，而是让数据能服务训练、测试、共享、仿真或 benchmark，同时不破坏关键统计结构和任务信号。

当前 vault 的直接 source-backed seeds 是 [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]]、[[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]]、[[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] 和 [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]]。CTGAN 把 tabular synthetic data 的核心问题整理为 mixed data types、multimodal continuous distributions、sparse one-hot vectors 和 imbalanced categorical columns，并用 CTGAN/TVAE/SDGym benchmark 给出代表性生成路线；Dankar et al. 比较 DS、SDV、Synthpop parametric 和 Synthpop nonparametric，补上 tabular/microdata 风格 generator 的 attribute/bivariate/population/application 四维 utility evaluation；SBPM attacks paper 说明合成表格数据的相似性指标和 filters 不能作为匿名/隐私发布保证；EndSDG 则用 Private-PGM/select-measure-generate route 展示离散化 genomic tabular data 在多 custodian 场景中的 privacy-preserving publishing pipeline。

## 基础概念判断

- 是否是基础概念/方向/问题: `topic/problem`
- 为什么足够通用: 它可组织 CTGAN、TVAE、Bayesian network synthesizers、DP synthetic data、tabular diffusion、tabular LLM、synthetic data evaluation 等多个 source/method。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: CTGAN 是代表性实现；tabular synthetic data generation 是更宽的静态结构化数据生成问题。
- 需要引用的更基础 Knowledge: [[synthetic-data-generation|Synthetic data generation]], [[ml-systems|ML systems]]
- 不应拆出的实例/协议/来源: CTGAN、TVAE adaptation、SDGym、mode-specific normalization、training-by-sampling 默认作为 source extension/method route，不作为 foundation 节点。

## 解决的问题

| 问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Mixed data types | 同一 row 混合连续、binary、多类别离散变量，generator 需要同时输出 tanh-like continuous value 与 softmax-like discrete value。 | CTGAN §3.1 |
| Multimodal continuous columns | 连续列可能由多个 modes 组成，单一 min-max normalization 容易造成 vanishing gradients 或抹掉局部结构。 | CTGAN §3.2 and §4.1 |
| Sparse one-hot artifacts | 离散变量 one-hot 后会让 discriminator 利用稀疏形态识别 fake data。 | CTGAN §3.3 |
| Imbalanced categorical columns | 少数类别出现少，普通 sampling 让 generator 难以学到 minor categories。 | CTGAN §3.4 and §4.3 |
| Evaluation mismatch | Synthetic data 看起来像真实分布，不等于能训练有用模型；任务效用也不等于隐私安全。 | CTGAN §5 |
| Multi-dimensional utility | 表格合成数据评价需要同时看单变量分布、变量相关性、整体分布可区分性和下游分类任务。 | Dankar et al. four-dimensional utility framework |
| Privacy release boundary | 合成表格数据常被用于数据共享，但没有 end-to-end DP 或攻击审计时不能声称匿名；相似性指标本身可能泄露。 | SBPM attacks paper; CTGAN mentions DP as adjacent only |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[synthetic-data-generation|Synthetic data generation]] | child_of | CTGAN source absorption | active_seed |
| [[ml-systems|ML systems]] | part_of | synthetic data supports ML training/evaluation/data sharing workflows | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Statistical/Bayesian synthesizers | 用 Bayesian networks、copulas、decision-tree-style models 等估计 joint distribution。 | 结构关系相对可建模、需要可解释或轻量 statistical route。 | 连续列离散化、多峰分布、高维依赖和复杂 utility 可能受限。 | CTGAN related work; CLBN/PrivBN baselines |
| GAN/VAE tabular synthesizers | 用 latent/noise 生成 rows，并通过 decoder/generator 输出混合列。 | 有足够训练数据，需要 flexible nonlinear generation。 | 可能 mode collapse、overfit、minor category 学不到、隐私泄露。 | CTGAN; TVAE baseline |
| Mode-specific continuous normalization | 为连续列估计 modes，用 mode-local scalar + mode indicator 表示数值。 | 连续列非 Gaussian、多峰或长尾。 | mode estimation 错误会传递到 generator；不是普适理论保证。 | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] |
| Conditional generation for discrete values | 让 generator 接收 discrete condition，支持按指定类别生成 rows。 | 需要控制类别覆盖、数据增强或 rare-category generation。 | 条件正确不保证整行因果/业务约束正确。 | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] |
| Training-by-sampling for imbalance | 训练时提高 rare categories 曝光，并让 critic 比较同条件 real/fake distributions。 | 类别极度不平衡，普通 batch sampling 学不到少数类。 | 可能改变训练关注点；不自动修复 noisy/invalid rare categories。 | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] |
| Synthetic data benchmark/evaluation | 用 simulated likelihood fitness 与 real-data ML efficacy 检查 fidelity/utility。 | 需要比较 synthesizers 或判断生成数据是否可用于 ML。 | 仍需 privacy/fairness/robustness 与真实业务指标。 | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN/SDGym]] |
| Multi-dimensional tabular utility evaluation | 用 attribute fidelity、bivariate fidelity、population fidelity 和 application fidelity 同时比较多个 tabular/microdata synthesizers。 | 合成数据用于泛化数据共享，具体下游分析未知或多样。 | 代表指标和 classification task 不能覆盖所有业务分析；不提供 privacy guarantee。 | [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|Dankar et al.]] |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | 把 generator、similarity metrics、filters、metric API 和 release workflow 一起纳入威胁模型。 | 表格合成数据被用于共享、匿名化、合规或敏感数据发布。 | SBPM/IMS/DCR/NNDR/SF/OF 是 heuristic/risk surface，不是隐私证明；攻击失败也不是 formal guarantee。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] |
| Privacy-preserving select-measure-generate route | 先对表格/离散化数据测量 noisy marginals，再用图模型等方法生成 synthetic rows，并把 preprocessing/evaluation/tuning 放入 privacy boundary。 | 数据可离散化，任务需要发布共享且涉及敏感多方数据。 | 高维/连续数据需要谨慎预处理；DP quantile binning 和 MPC cost 是关键限制。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | paper | 创建 tabular synthetic data generation topic seed；提出 CTGAN mode-specific normalization、conditional generator 和 training-by-sampling；提供 SDGym benchmark。 | no privacy guarantee; no theory for mixed GAN success; TVAE competitive; repo not analyzed in this run | `p1-p15` |
| [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]] | paper | 补充 tabular/microdata generator utility evaluation：DS、SDV、SP-p、SP-np 在 19 个数据集上用四维指标比较；SP-np 在该设置下总体最好。 | no privacy guarantee; one representative metric per dimension; application fidelity only classification. | `p1-p10` |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | paper | 补充 synthetic tabular data privacy evaluation seed；证明 similarity-based privacy metrics/filtering 不足以保证匿名，并提出 DifferenceAttack/ReconSyn。 | attack model assumes generator/metric access; not a DP synthetic data construction; broader non-tabular privacy still需补 source | `p1-p19` |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | paper | 作为 tabular/离散化 genomic synthetic data 的二级 evidence，补充 Private-PGM/select-measure-generate 在多 custodian privacy-preserving release pipeline 中的使用方式。 | 不是 tabular foundation paper；DP quantile binning not complete; genomic use case preliminary。 | `p1-p15` |

## 正反例约束

- 正确: 把 tabular synthetic data generation 作为 synthetic data generation 下的静态结构化数据问题。
- 正确: 对生成质量同时区分 distribution fidelity、downstream utility、privacy leakage、fairness、robustness 和业务约束。
- 正确: 把 CTGAN/TVAE/SDGym 作为 source-backed method/artifact，而不是上层概念本身。
- 错误: 把 CTGAN 归到 distributed learning 或 privacy-preserving ML 主方向。
- 错误: 把 synthetic tabular data 自动视为 anonymized/private data release。
- 错误: 把 IMS/DCR/NNDR/SF/OF 等 similarity-based privacy metrics 当作 synthetic tabular data 的正式匿名证明。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`
- Freshness: `fresh` for local source absorption; not an external latest claim.
- Valid until: `2026-07-23`
- 综合: 当前 tabular synthetic data generation 的 source-backed seeds 来自 CTGAN、Dankar et al.、SBPM attacks paper 和 EndSDG。CTGAN 给出的核心结构是: 表格数据生成的难点来自列类型混合、连续列多峰、离散列稀疏 one-hot 表示和类别不平衡；解决路线不能只换成更强 generator，而要把 representation、conditional sampling、batch construction 和 evaluation protocol 一起设计。Dankar et al. 补上泛化 tabular/microdata utility evaluation: attribute fidelity、bivariate fidelity、population fidelity 和 application fidelity 可能给出不同 ranking，不能用单一指标代表整体质量。SBPM attacks paper 补上发布/隐私侧的边界: 表格合成数据通过相似性指标、重复率或最近邻距离并不意味着匿名；metric API 与 filters 可能成为 membership、attribute 和 outlier reconstruction 攻击通道。EndSDG 则补充建设性 privacy-preserving route: 对离散化表格/基因数据，可用 select-measure-generate/Private-PGM 式 noisy marginals，并把预处理、评估和调参都放入 MPC/DP pipeline。因此本节点要把 generation quality、utility evaluation、privacy release boundary 和 multi-custodian pipeline 分开写。

## 领域态势

- Research dynamics note: [[research-dynamics|ML systems Research Dynamics]]
- Dynamics freshness: fresh for current-vault evidence only.
- Latest academic focus summary: 当前 vault 记录到的 tabular synthetic data seed 同时覆盖 CTGAN/TVAE/SDGym 式混合类型表格生成、fidelity/utility benchmark，以及 SBPM/ReconSyn 暴露的 privacy release boundary。
- Latest industrial focus summary: unknown; no repo/production evidence was analyzed in this run.
- Open-problem summary: DP synthetic tabular data、attack/audit taxonomy、rare subgroup fidelity、relational/multi-table data、business constraints、modern tabular diffusion/LLM routes、benchmark reproducibility。
- Next refresh trigger: 后续 tabular synthetic data、DP synthetic data、synthetic-data evaluation 或 SDV/SDGym repo source 被吸收。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | 新增 tabular synthetic data generation topic；纠正队列误分到 privacy/distributed learning；补充 synthetic data evaluation 候选轴。 | 定义; 问题; 方法族; 代表 Sources; 当前综合 | yes | 吸收后续 tabular/DP/evaluation sources 后补全 taxonomy |
| [[doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators|A Multi-Dimensional Evaluation of Synthetic Data Generators]] | 补充 tabular/microdata generator utility comparison；把 synthetic data evaluation 从候选轴提升为 active_seed；纠正队列误分到 privacy/distributed learning。 | 背景; 问题; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 下一篇 `How Faithful is your Synthetic Data?` 应接到 synthetic-data-evaluation |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | 补充 synthetic tabular data privacy boundary；新增 synthetic data privacy evaluation 节点和 bridge；纠正队列误分到 ZK proof foundations。 | 背景; 问题; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 DP/collaborative synthetic data sources 后校准 |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | 补充 privacy-preserving select-measure-generate route；把 tabular/离散化数据的 preprocessing/evaluation/tuning 放入 collaborative release boundary。 | 背景; 方法族; 代表 Sources; 当前综合 | no | 后续吸收 DP tabular synthetic data primary sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]] | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation; ml-systems/privacy-and-trustworthy-ml` | tension, privacy_boundary, evaluation_transfer | Synthetic tabular data may support data sharing, but privacy does not transfer from similarity/fidelity metrics; it requires DP or threat-model-specific attack evaluation. | active_seed |
| [[synthetic-data-evaluation-to-synthetic-data-privacy-evaluation|Synthetic data evaluation -> synthetic data privacy evaluation]] | `ml-systems/synthetic-data-generation/synthetic-data-evaluation; ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | tension, evaluation_transfer, privacy_boundary | Tabular utility metrics such as Hellinger/PCD/propensity/accuracy can rank generator quality but do not establish anonymity. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-tabular-synthetic-data-generation | is_a | nahida-knowledge-ml-systems-synthetic-data-generation | vault/04_Knowledge/ml-systems/synthetic-data-generation.md | high | active_seed |
| nahida-knowledge-tabular-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md | source note | high | active_seed |
| nahida-knowledge-tabular-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators.md | source note | high | active_seed |
| nahida-knowledge-tabular-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md | source note | high | active_seed |
| nahida-knowledge-tabular-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md | source note | medium | active_seed |
| nahida-knowledge-tabular-synthetic-data-generation | bridges_to | nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml | bridge note | high | active_seed |
| nahida-knowledge-tabular-synthetic-data-generation | bridges_to | nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| tabular synthetic data foundation breadth | 当前只有 CTGAN，缺更现代/更基础的 tabular generation sources。 | nahida-update / nahida-research-search | high | active_seed_gap |
| privacy-preserving synthetic tabular data | 已有 SBPM attacks seed，但仍缺 DP synthetic tabular data 和更多 attack/audit taxonomy。 | nahida-update / nahida-research-search | high | active_seed_gap |
| synthetic data evaluation taxonomy | fidelity/utility/privacy/fairness/robustness 需要跨 source 组织。 | nahida-update / nahida-research-search | high | queued |
| repo/benchmark reproducibility | CTGAN/SDGym 代码未在本次作为 repo source 分析。 | nahida-github-repo-analyze | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-ctgan-tabular-synthetic-data | Created tabular synthetic data generation topic seed from CTGAN and attached it under synthetic data generation. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-synthetic-data-privacy-metrics | Added SBPM attacks paper as privacy-evaluation evidence for synthetic tabular data and linked it to privacy/trustworthy ML. | 1 source note | codex |
