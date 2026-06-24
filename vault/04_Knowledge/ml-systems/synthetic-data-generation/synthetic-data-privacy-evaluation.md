---
id: "nahida-knowledge-synthetic-data-privacy-evaluation"
title: "Synthetic data privacy evaluation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "evaluation_axis"
hierarchy_level: "problem"
file_slug: "synthetic-data-privacy-evaluation"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems-synthetic-data-generation"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "synthetic-data-privacy-evaluation"
primary_ontology_path: "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
secondary_ontology_paths:
  - "ml-systems/synthetic-data-generation/tabular-synthetic-data-generation"
  - "ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation"
  - "ml-systems/privacy-and-trustworthy-ml"
relation_edges:
  - from: "nahida-knowledge-synthetic-data-privacy-evaluation"
    relation: "is_a"
    to: "nahida-knowledge-ml-systems-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation.md"
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-privacy-evaluation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-privacy-evaluation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-privacy-evaluation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
    evidence_refs:
      - "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-privacy-evaluation"
    relation: "bridges_to"
    to: "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/05_Bridges/synthetic-data-generation-to-privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-synthetic-data-privacy-evaluation"
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
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
  - "vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md"
representative_source_refs:
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "pmlr:162:alaa22a"
query_keys:
  - "synthetic data privacy evaluation"
  - "privacy evaluation for synthetic data"
  - "similarity-based privacy metrics"
  - "SBPM"
  - "synthetic tabular data privacy"
  - "membership inference synthetic data"
  - "attribute inference synthetic data"
  - "reconstruction attack synthetic data"
  - "ReconSyn"
  - "DifferenceAttack"
  - "differential privacy synthetic data release"
  - "input privacy output privacy synthetic data"
  - "privacy-preserving synthetic data evaluation"
  - "private hyperparameter tuning synthetic data"
  - "DP-in-MPC synthetic data release"
  - "authenticity synthetic data"
  - "data copying generative models"
  - "generative model overfitting synthetic data"
  - "model auditing synthetic data privacy"
aliases:
  - "synthetic data privacy auditing"
  - "privacy evaluation of synthetic data"
  - "synthetic data authenticity auditing"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "synthetic-data-privacy-evaluation"
  - "tabular-synthetic-data-generation"
  - "collaborative-synthetic-data-generation"
  - "privacy-and-trustworthy-ml"
  - "differential-privacy"
  - "membership-inference"
  - "reconstruction-attacks"
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
  - "nahida-knowledge-20260623-synthetic-data-privacy-metrics"
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
  - "nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation"
  - "nahida-knowledge-20260623-how-faithful-synthetic-data"
source_refs:
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "pmlr:162:alaa22a"
confidence: "medium"
trust_tier: "primary"
---

# Synthetic data privacy evaluation

## 定义与范围

- 定义: Synthetic data privacy evaluation 指评估合成数据生成、过滤、发布和度量流程是否泄露训练数据中个体记录、属性或低密度 outliers 的问题域。它不同于 fidelity/utility evaluation，也不同于单个 generator 的生成质量评估。
- 不包含: 某篇论文的攻击名、某个 vendor 的隐私报告、某个 generator 的完整实现、或者把 similarity/fidelity 指标直接当成匿名证明。
- Canonical terms: `synthetic data privacy evaluation`, `privacy evaluation for synthetic data`
- Aliases/query keys: synthetic data privacy auditing, similarity-based privacy metrics, SBPM, membership inference, reconstruction attack, ReconSyn
- Standalone completeness check: 本节点给出合成数据隐私评估的定义、边界、威胁、方法路线、负例和当前 source-backed seed；攻击伪代码和完整实验数值留在 source note。
- Retrieval role: 查询“合成数据是不是匿名”“相似性指标能否证明隐私”“合成表格数据怎样做隐私评估”“DP generator 为什么仍会泄露”时，先读本节点。
- Update scope: 新 source 若涉及 DP synthetic data、synthetic data auditing、membership/attribute inference、reconstruction attacks、similarity privacy metrics、data release governance，应刷新本节点。
- Domain dynamics note: not_applicable；本节点是 direction 下的问题/评价轴，领域态势由 [[research-dynamics|ML systems Research Dynamics]] 维护。

## 背景

model_prior_background: 合成数据常被用于缓解数据共享和隐私合规压力，但“生成的数据看起来不像训练数据”并不等于“发布流程不会泄露训练数据”。隐私评价需要先定义 adversary 能看到什么、能否查询 generator 或 metrics、能否多次生成数据、是否能观察 pass/fail 或距离分数，再判断是否存在 membership inference、attribute inference 或 reconstruction risk。

当前 source-backed seeds 是 [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]]、[[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] 和 [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]]。SBPM attacks paper 说明 similarity-based privacy metrics (SBPMs) 只能作为脆弱的经验信号，不能替代 end-to-end Differential Privacy 或明确威胁模型下的攻击审计。EndSDG 给出建设性路线: 在多 data custodians 场景中，把 preprocessing、evaluation、threshold voting 和 hyperparameter tuning 都放在 MPC/DP pipeline 内，尽量只发布最终 synthetic data。Alaa et al. 则把 training-data copying 作为生成模型 generalization 维度，用 `Authenticity` 提醒 high-fidelity/high-utility synthetic data 仍可能只是训练样本的近复制。

## 基础概念判断

- 是否是基础概念/方向/问题: `evaluation_axis/problem`
- 为什么足够通用: 它可组织 DP synthetic data、membership/attribute inference、reconstruction attacks、metric leakage、outlier protection、release-pipeline privacy budget 和商业匿名性声明审计。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: DifferenceAttack 和 ReconSyn 是本文攻击实例；合成数据隐私评估是跨论文、跨 generator、跨部署场景的问题层。
- 需要引用的更基础 Knowledge: [[synthetic-data-generation|Synthetic data generation]], [[tabular-synthetic-data-generation|Tabular synthetic data generation]], [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]]。
- 不应拆出的实例/协议/来源: SBPM、DifferenceAttack、ReconSyn、IMS/DCR/NNDR/SF/OF 默认作为 method/risk route 或 source extension，不作为 foundation 节点。

| 候选 | 判断 | 正确处理 | 错误处理 |
| --- | --- | --- | --- |
| Synthetic data privacy evaluation | reusable problem/evaluation axis | 独立节点，连接 synthetic data generation 与 privacy/trustworthy ML | 只写成单篇论文摘要 |
| Similarity-based privacy metrics | heuristic/risk route | 作为方法族和反例路线 | 写成可靠匿名证明 |
| DifferenceAttack / ReconSyn | source-backed attack instances | 留在 source 并作为代表攻击路线引用 | 提升为上层分类主干 |
| Differential Privacy | foundation/privacy guarantee route | 作为可靠路线和待补 foundation | 与 SBPM 混同 |

## 解决的问题

| 问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Fidelity/privacy mismatch | 合成数据与真实数据统计相似或不完全重复，不等于不会泄露训练记录。 | SBPM paper Sections 3-4 |
| Release-process privacy | 隐私是 generator、metric、filter、query access 和 release workflow 的 process property，不是单个 synthetic dataset 的静态属性。 | SBPM paper Issue I5 and DP discussion |
| Metric leakage | 需要访问 train data 的 privacy metrics 或 filters 本身可能成为泄露通道。 | DifferenceAttack and ReconSyn |
| Outlier protection | 低密度训练记录更容易被 generator/metric interaction 暴露。 | ReconSyn evaluation |
| Threat model clarity | 必须说明 adversary 是否可查询 generator、metric scores、pass/fail signals 或多次生成数据。 | SBPM adversarial model |
| Formal guarantee boundary | 如果要声称隐私保证，需要 end-to-end DP 或等价 process-level guarantee；attack auditing 不能替代 guarantee。 | DP experiment and mitigation discussion |
| Private tuning/evaluation boundary | 如果要多轮调参，需要避免公开中间 synthetic data、models、metrics、thresholds 或 votes，否则 privacy budget 或 metric leakage 会重新进入发布流程。 | EndSDG Algorithm 1 and §3 |
| Input/output privacy split | 多方合成数据发布同时需要保护输入数据和最终输出，MPC secrecy 与 DP release guarantee 是不同属性。 | EndSDG §1-§3 |
| Data copying/generalization | 生成模型可能复制训练记录，尤其在敏感数据建模中需要把 overfitting/copying 单独测出来。 | Alaa et al. Authenticity metric |
| Auditing metric leakage | 用训练数据判断 sample authenticity/precision 可以帮助过滤，但若这些 metric/filter 暴露给外部，也属于发布流程的一部分。 | Alaa et al. model auditing; SBPM/EndSDG privacy boundary |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[synthetic-data-generation|Synthetic data generation]] | child_of / evaluation_axis | synthetic data generation 已有 privacy evaluation gap；本 source 直接填补该 gap。 | active_seed |
| [[tabular-synthetic-data-generation|Tabular synthetic data generation]] | scoped_topic | 当前 source 主要针对 synthetic tabular data。 | active_seed |
| [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]] | scoped_topic | EndSDG 说明 collaborative SDG 的 privacy evaluation 不只看最终数据，还包括 preprocessing、evaluation、thresholds 和 tuning loop。 | active_seed |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | bridge_target | 本问题把 synthetic data release 接入 ML privacy/trust boundary。 | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP synthetic data release | method/foundation candidate | 多篇 sources 支撑后应单独解释 DP generator、privacy budget、post-processing 和 utility tradeoff。 | current source references DP as boundary only | queued |
| synthetic data membership and reconstruction attacks | attack-family candidate | 若后续有多篇攻击/evaluation papers，可从 source instances 抽成 attack-family。 | DifferenceAttack and ReconSyn seed | review |
| similarity-based privacy metrics | heuristic metric family | 当前只有一篇强批判 source；先保留为方法/风险路线。 | SBPM paper | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| End-to-end Differential Privacy | 对生成/发布流程提供 process-level 隐私保证，并跟踪 privacy budget。 | 需要可接受的 utility/privacy tradeoff 和严格机制设计。 | 会降低 utility 或限制重复生成；当前 vault 缺 foundation source。 | SBPM paper uses as boundary |
| DP-in-MPC collaborative release | 在 MPC 内执行会影响最终发布的 preprocessing/training，并只 reveal DP-protected final synthetic data。 | 多数据持有方不能集中原始数据，但需要全局统计质量。 | MPC 成本高；DP preprocessing 和 optimized protocols 未成熟；中间输出必须严格不泄露。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] |
| Private evaluation and tuning | Evaluation metrics、custodian thresholds 和 votes 保持 secret-shared，用 pass condition 决定是否发布。 | 需要调参和质量门槛，但 metrics/thresholds 本身敏感。 | 可解释性、审计和 policy 需要额外治理；pass/fail signal 也要纳入 threat model。 | EndSDG Algorithm 1 |
| Attack-based auditing | 用 membership inference、attribute inference、reconstruction attack 测试 pipeline 是否泄露。 | 需要验证具体 threat model 下的风险。 | 只能发现问题，不提供完整 guarantee。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] |
| Authenticity / data-copying diagnostic | 用 nearest-neighbor style test 判断 synthetic sample 是否疑似训练样本复制，把 overfitting 作为 privacy-sensitive quality signal。 | 需要评估 generator 是否真正 generalize，尤其是临床/敏感数据。 | 不是 DP guarantee；依赖 embedding、distance metric 和训练数据访问；filter output 也可能泄露。 | [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|Alaa et al.]] |
| Similarity-based privacy metrics | 用 train/test/synthetic 距离、最近邻和重复率判断风险。 | 作为弱 heuristic 或 debugging signal。 | 无理论保证；metric API/filter 可能泄露；不应作为匿名证明。 | same source |
| Outlier-focused evaluation | 特别检查 low-density train records 是否被生成器或指标暴露。 | 数据包含稀有群体、异常值或高敏感个体记录。 | outlier 定义依赖数据表示和距离度量。 | ReconSyn evaluation |
| Release-pipeline governance | 把 generator、filters、metrics、scores、pass/fail、query limits 和 train-data access 放入同一威胁模型。 | 工具/产品提供合成数据发布或隐私报告。 | 需要工程/合规 evidence；当前只有 paper source。 | SBPM mitigation discussion |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | paper | 创建 synthetic data privacy evaluation seed；证明 SBPMs 不能作为匿名保证；提出 DifferenceAttack 和 ReconSyn；显示 DP generator 若接 metric leakage 仍可破坏 end-to-end pipeline。 | 主要是 tabular synthetic data；攻击界面依赖 generator/metric access；不是 DP synthetic data 构造论文。 | `p1-p19` |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | paper | 补充建设性 privacy-evaluation/publishing route：MPC input privacy、DP output privacy、private preprocessing/evaluation/tuning 和 final-output-only release boundary。 | arXiv preprint；exact quantile binning not DP yet；code not analyzed；genomic experiment preliminary。 | `p1-p15` |
| [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]] | paper | 补充 Authenticity/copying diagnostic：high-fidelity synthetic data 可能来自 memorization；sample-level auditing 可过滤 unauthentic samples。 | Generative-model evaluation paper, not formal privacy paper; no DP guarantee; metric/filter release must still be threat-modeled. | `p1-p17` |

## 正反例约束

- 正确: 把隐私评估与 fidelity/utility evaluation 分开写。
- 正确: 在合成数据发布场景里先写 threat model，再讨论 metrics、filters 或 attacks。
- 正确: 把 DP 视为 process-level guarantee route，把 SBPM 视为 heuristic/audit signal。
- 错误: 把 synthetic data 默认写成匿名数据。
- 错误: 因为 synthetic records 与 train records 不完全相同，就推断没有 membership/attribute/reconstruction risk。
- 错误: 把通过 IMS/DCR/NNDR/SF/OF 写成 GDPR/anonymization proof。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`
- Freshness: `fresh` for local source absorption; not an external latest claim.
- Valid until: `2026-07-23`
- 综合: 当前节点是 active_seed。SBPM attacks paper 明确推动 Nahida 的 synthetic data generation 从 fidelity/utility 评价扩展到 privacy release boundary：合成数据隐私评估的核心不是“synthetic data 距离 train data 多远”，而是“整个生成、过滤、度量和发布流程是否在给定 adversary 能力下泄露训练信息”。EndSDG 又补充了建设性路线：在多 data custodians 场景中，preprocessing、evaluation、thresholds、votes 和 hyperparameter tuning 也必须纳入 privacy boundary；MPC input privacy 与 DP output privacy 需要同时成立。Alaa et al. 补充一个更靠近 generative-model evaluation 的 copying signal：`Authenticity` 可以发现 synthetic samples 是否疑似训练样本近复制，并把 privacy-utility tradeoff 画成 precision/authenticity tradeoff。三类 source 合起来说明: SBPMs 和 Authenticity 都可以作为调试/审计信号，但不能替代 DP 或严格攻击评估；而 DP/MPC pipeline 也不能忽视中间结果泄露、DP preprocessing 和治理可解释性。

## 领域态势

> not_applicable for this L3 problem/evaluation axis. See [[research-dynamics|ML systems Research Dynamics]].

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | 新建 synthetic data privacy evaluation 节点；把 SBPM、DifferenceAttack、ReconSyn 和 DP pipeline boundary 纳入 synthetic data generation。 | 定义; 解决的问题; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 DP synthetic data、collaborative synthetic data 和 attack/audit sources 后刷新 |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | 补充 collaborative SDG 的 private preprocessing/evaluation/tuning 与 final-output-only release route；明确 input privacy 和 output privacy 是不同 trust properties。 | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 DP preprocessing、CaPS/FLAIM 和 DP synthetic data foundation 后刷新 |
| [[pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data|How Faithful is your Synthetic Data?]] | 补充 `Authenticity` 作为 training-data copying/generalization diagnostic；明确它是隐私相关 signal 而不是匿名/DP 证明。 | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 若后续分析代码仓库或 DP synthetic data sources，可校准 metric leakage 边界 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]] | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation; ml-systems/privacy-and-trustworthy-ml` | tension, privacy_boundary, evaluation_transfer | Synthetic data can support data sharing, but privacy/trustworthiness does not transfer from similarity metrics; it requires DP or threat-model-specific attack evaluation. | active_seed |
| [[synthetic-data-evaluation-to-synthetic-data-privacy-evaluation|Synthetic data evaluation -> synthetic data privacy evaluation]] | `ml-systems/synthetic-data-generation/synthetic-data-evaluation; ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | tension, evaluation_transfer, privacy_boundary | Utility/fidelity metrics such as attribute/bivariate/population/application fidelity help quantify usefulness but cannot prove release privacy. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-synthetic-data-privacy-evaluation | is_a | nahida-knowledge-ml-systems-synthetic-data-generation | vault/04_Knowledge/ml-systems/synthetic-data-generation.md | high | active_seed |
| nahida-knowledge-synthetic-data-privacy-evaluation | evidenced_by | vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md | source note | high | active_seed |
| nahida-knowledge-synthetic-data-privacy-evaluation | evidenced_by | vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md | source note | high | active_seed |
| nahida-knowledge-synthetic-data-privacy-evaluation | evidenced_by | vault/03_Sources/papers/pmlr-v162-alaa22a-how-faithful-is-your-synthetic-data.md | source note | high | active_seed |
| nahida-knowledge-synthetic-data-privacy-evaluation | bridges_to | nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml | bridge note | high | active_seed |
| nahida-knowledge-synthetic-data-privacy-evaluation | bridges_to | nahida-bridge-synthetic-data-evaluation-to-synthetic-data-privacy-evaluation | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| DP synthetic data foundation | 当前 source 只把 DP 作为边界和对照，需要独立理解 DP synthetic data release。 | nahida-research-search / nahida-update | high | queued |
| DP preprocessing and private tuning | EndSDG 说明 exact quantile binning 仍未 DP；private tuning 的 pass/fail/governance signal 也需更多来源。 | nahida-update / nahida-research-search | high | active_seed_gap |
| broader attack evaluation | 需要更多 membership/reconstruction/privacy audit sources 支撑 attack-family taxonomy。 | nahida-update | high | active_seed_gap |
| production/privacy reports | 商业 synthetic data workflows 的 metric exposure、query limits 和 compliance claims 需要 web/repo evidence。 | nahida-research-search | medium | queued |
| non-tabular synthetic data privacy | 当前 source 主要是 tabular；image/time-series/relational privacy 可能不同。 | nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-synthetic-data-privacy-metrics | Created synthetic data privacy evaluation active seed and linked it to synthetic data generation and privacy/trustworthy ML. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-collaborative-synthetic-data-generation | Added EndSDG as a constructive collaborative SDG privacy pipeline route. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation | Added bridge boundary showing utility/fidelity evaluation does not imply privacy evaluation. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-how-faithful-synthetic-data | Added Authenticity/data-copying diagnostic from Alaa et al. as a privacy-relevant but non-guarantee audit signal. | 1 source note | codex |
