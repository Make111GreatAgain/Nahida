---
id: "nahida-knowledge-collaborative-synthetic-data-generation"
title: "Collaborative synthetic data generation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "topic"
file_slug: "collaborative-synthetic-data-generation"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems-synthetic-data-generation"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "collaborative-synthetic-data-generation"
primary_ontology_path: "ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation"
secondary_ontology_paths:
  - "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
  - "ml-systems/synthetic-data-generation/tabular-synthetic-data-generation"
  - "ml-systems/privacy-and-trustworthy-ml"
relation_edges:
  - from: "nahida-knowledge-collaborative-synthetic-data-generation"
    relation: "is_a"
    to: "nahida-knowledge-ml-systems-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation.md"
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-collaborative-synthetic-data-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-collaborative-synthetic-data-generation"
    relation: "bridges_to"
    to: "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/05_Bridges/synthetic-data-generation-to-privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
representative_source_refs:
  - "arxiv:2412.03766v1"
query_keys:
  - "collaborative synthetic data generation"
  - "collaborative SDG"
  - "privacy-preserving synthetic data generation across silos"
  - "multi-custodian synthetic data publishing"
  - "input privacy output privacy synthetic data"
  - "DP in MPC synthetic data"
  - "MPC synthetic data generation"
  - "privacy-preserving synthetic genomic data"
aliases:
  - "collaborative private synthetic data generation"
  - "multi-silo synthetic data generation"
  - "privacy-preserving collaborative SDG"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "collaborative-synthetic-data-generation"
  - "privacy-preserving-synthetic-data"
  - "synthetic-data-privacy-evaluation"
  - "secure-multiparty-computation"
  - "differential-privacy"
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
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
source_refs:
  - "arxiv:2412.03766v1"
confidence: "medium"
trust_tier: "primary"
---

# Collaborative synthetic data generation

## 定义与范围

- 定义: Collaborative synthetic data generation 指多个 data custodians 在不集中原始数据的情况下协作生成、评估、调参并发布合成数据的系统问题。它同时处理 input privacy、output privacy、数据预处理、生成质量评估、hyperparameter tuning 和最终发布边界。
- 不包含: 某个具体 MPC protocol、某个 genomic 数据集、某个 synthesizer 名称、单次 runtime 表格或单篇论文系统名；这些保留在 source note。
- Canonical terms: `collaborative synthetic data generation`, `privacy-preserving collaborative synthetic data generation`
- Aliases/query keys: collaborative SDG, multi-silo synthetic data generation, DP-in-MPC synthetic data
- Standalone completeness check: 本节点给出问题定义、边界、为什么需要拆分、方法路线、代表 source、bridge 和缺口；读者不必打开论文也能理解该问题层。
- Retrieval role: 查询“多机构怎么协作生成合成数据”“合成数据 input privacy 和 output privacy 如何同时处理”“为什么 synthetic data tuning 不能公开 metrics”时，先读本节点。
- Update scope: 新 source 若涉及 federated/collaborative synthetic data、MPC/DP synthetic data release、privacy-preserving preprocessing/evaluation/tuning、multi-custodian data sharing，应刷新本节点。
- Domain dynamics note: not_applicable；本节点是 L3 problem/topic，领域态势由 [[research-dynamics|ML systems Research Dynamics]] 维护。

## 背景

model_prior_background: 合成数据经常被用来缓解数据共享限制，但单个机构的数据可能太少或覆盖不足。多机构协作能提升样本量和代表性，尤其适合 rare disease、跨医院 genomics、跨组织金融/风控和 regulated data sharing。然而协作式合成数据不是简单把数据拼起来训练 generator: 预处理、调参、评估和发布动作都可能暴露真实数据或消耗隐私预算。

当前 source-backed seed 是 [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]]。它把 collaborative SDG 从“隐私保护地训练 synthesizer”扩展成完整发布流水线: data custodians secret-share data 和 quality thresholds，MPC servers 在 combined secret-shared data 上做 preprocessing、SDG training、evaluation、threshold voting 和 final release，输出侧通过 DP 保护。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem/topic`
- 为什么足够通用: 它可组织 federated synthetic data、MPC-based SDG、DP synthetic release、private preprocessing、private evaluation、multi-custodian hyperparameter tuning 和 data release governance。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: EndSDG 只是第一个代表 source；持久问题是多个数据持有方如何在协作生成合成数据时同时保护输入和输出。
- 需要引用的更基础 Knowledge: [[synthetic-data-generation|Synthetic data generation]], [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]], [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]].
- 不应拆出的实例/协议/来源: `pi_BIN`, `pi_NOISY-MARG`, `pi_WLE`, Private-PGM leukemia experiment 默认留在 source note 或 method route。

| 候选 | 判断 | 正确处理 | 错误处理 |
| --- | --- | --- | --- |
| Collaborative synthetic data generation | reusable problem | 建成 synthetic data generation 下的问题节点 | 只作为 EndSDG 论文摘要 |
| MPC | foundation concept | 作为 input privacy route 短定义，未来补 foundation | 用本文协议细节替代 MPC 定义 |
| Differential Privacy | foundation/privacy route | 作为 output privacy 与 release budget route | 把 similarity/privacy metrics 混成 DP guarantee |
| Private-PGM | representative synthesizer route | 作为 select-measure-generate method instance | 当作合成数据生成方向本身 |

## 解决的问题

| 子问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Multi-custodian data scarcity | 单个 custodian 数据量不足或覆盖不足，但原始数据不能集中。 | EndSDG rare disease/genomic motivation |
| Input privacy | 数据持有方不希望向 central aggregator、其他 custodian 或单个服务器泄露原始数据。 | MPC secret-sharing setup |
| Output privacy | 最终发布的 synthetic data 或 generator 需要保护单条训练记录。 | DP preprocessing/training route |
| Privacy-preserving preprocessing | Quantile binning、discretization、normalization 等通常需要 combined data statistics。 | `pi_BIN`; DP quantile caveat |
| Private evaluation and tuning | Synthetic quality evaluation 需要真实数据；metrics、votes 或 thresholds 若公开会泄露信息或消耗 budget。 | Algorithm 1 k-fold evaluation and secret threshold voting |
| DP budget accounting | 多轮 hyperparameter tuning 若发布中间 outputs 会累加隐私损失；框架通过不发布中间结果把公开 release 限于最终输出。 | EndSDG §3 |
| Utility/privacy/performance tradeoff | MPC 和 DP 会增加 runtime 并影响 utility；高维 genomic data 尤其困难。 | EndSDG Tables 1-2 and conclusion |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[synthetic-data-generation|Synthetic data generation]] | child_of | Collaborative SDG 是合成数据生成在多数据持有方/隐私发布场景中的问题层。 | active_seed |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | scoped privacy axis | 该问题显式处理 input/output privacy、private metrics 和 release budget。 | active_seed_bridge |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | bridge target | MPC/DP/threat model 属于 ML trust boundary。 | active_seed_bridge |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Trusted central synthesizer | 多方把数据交给 trusted entity，由其训练和发布 synthetic data。 | 存在强可信第三方或法律/治理允许集中。 | 单点信任强；input privacy 不成立。 | PETs Prize motivation in EndSDG |
| Federated synthetic data generation | 各方本地训练或协作训练 generator，通常由 central server 协调。 | 数据不能集中但可接受 server/FL 信任假设。 | 可能 utility 低于 centralized global DP；常忽略 preprocessing/evaluation/tuning。 | EndSDG related work discussion |
| MPC + DP-in-MPC pipeline | Data custodians secret-share data；MPC servers 在 combined secret-shared data 上执行 preprocessing/training/evaluation；最终 release 由 DP 保护。 | 多方可部署 non-colluding MPC servers，且计算成本可接受。 | 协议成本高；DP preprocessing 与 optimized protocols 仍是 open work。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] |
| Private evaluation and threshold voting | Evaluation metrics 和 custodian thresholds 保持 secret-shared，只公开是否达到发布条件。 | 需要多方共同决定 release quality，且不希望泄露 metrics/thresholds。 | 可解释性和 governance 需要额外设计；threshold 设置本身仍是 policy 问题。 | EndSDG Algorithm 1 |
| Final-output-only privacy budget route | 调参阶段不发布 synthetic data、models、metrics 或 votes，只发布最终满足条件的数据，从而避免每轮 tuning 输出叠加预算。 | pipeline 能严格阻止中间输出泄露。 | 如果日志、metrics 或 filter signals 暴露，budget accounting 会失效。 | EndSDG §3; bridge to privacy evaluation |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | paper | 创建 collaborative synthetic data generation active seed；把 preprocessing、training、evaluation、hyperparameter tuning、MPC input privacy 和 DP output privacy 串成端到端发布流水线。 | arXiv preprint; code not analyzed; exact quantile binning not DP yet; generate step partially clear in experiments; genomic SDG quality still open。 | `p1-p15`; Algorithm 1; Tables 1-2; Appendix A.5 |

## 正反例约束

- 正确: 把多 custodian 合成数据发布视为 pipeline-level problem，而不是某个 synthesizer 的训练技巧。
- 正确: 区分 input privacy 和 output privacy；MPC 不自动给最终 synthetic data DP，DP 不自动解决输入集中问题。
- 正确: 把 preprocessing、evaluation metrics、thresholds 和 tuning loop 写入 trust boundary。
- 错误: 把 EndSDG 的 `pi_BIN`、`pi_NOISY-MARG` 或 leukemia experiment 升成上层概念。
- 错误: 因为框架使用 DP vocabulary，就忽略 DP quantile binning 尚未完成的 caveat。
- 错误: 把不发布中间结果误解为“无论怎样调参都没有隐私成本”；前提是中间 models、metrics、votes、logs 和 pass/fail signals 都不泄露训练信息。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`
- Freshness: `fresh` for local source absorption; not an external latest claim.
- Valid until: `2026-07-23`
- 综合: Collaborative synthetic data generation 当前是 active_seed。EndSDG 显示合成数据发布在多机构场景中必须被看作完整系统流水线: 数据不能集中，所以 input privacy 需要 MPC 或等价 secure computation；最终数据要发布，所以 output privacy 需要 DP 或等价过程保证；生成质量要评估和调参，所以 metrics、thresholds 和 tuning loop 也必须留在隐私边界内。这个问题与 synthetic data privacy evaluation 互补: SBPM attacks paper 说明相似性指标不能证明隐私，EndSDG 则给出一种把 metrics/tuning 私有化并限制公开输出的建设性路线。

## 领域态势

> not_applicable for this L3 problem/topic. See [[research-dynamics|ML systems Research Dynamics]].

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | 新建 collaborative synthetic data generation problem node；补充 synthetic data privacy evaluation 的建设性路线；纠正队列中的 distributed-learning 过宽分类。 | 全文; Bridge Links; 缺口与队列 | yes | 后续吸收 CaPS、FLAIM、DP synthetic data 和 DP quantile preprocessing sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]] | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation; ml-systems/privacy-and-trustworthy-ml` | privacy_boundary, trustworthiness_dependency, construction_route | Collaborative SDG can transfer MPC/DP/threat-model discipline into synthetic data release, but generation utility, MPC secrecy and DP output guarantees remain separate properties that must all hold in the actual pipeline. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-collaborative-synthetic-data-generation | is_a | nahida-knowledge-ml-systems-synthetic-data-generation | vault/04_Knowledge/ml-systems/synthetic-data-generation.md | high | active_seed |
| nahida-knowledge-collaborative-synthetic-data-generation | evidenced_by | vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md | source note | high | active_seed |
| nahida-knowledge-collaborative-synthetic-data-generation | bridges_to | nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| DP synthetic data release foundation | 当前节点引用 DP 作为 output privacy route，但 vault 缺系统 DP synthetic data foundation。 | nahida-research-search / nahida-update | high | queued |
| DP quantile preprocessing | EndSDG 自身说明 exact quantile binning 尚未 DP。 | nahida-update / nahida-research-search | high | active_seed_gap |
| CaPS/FLAIM primary sources | EndSDG related work 引用 collaborative/federated SDG prior work；需 primary source 稳定 taxonomy。 | nahida-update | high | queued |
| Non-genomic/multi-modal evaluation | 当前 use case 是 leukemia genomic tabularization，泛化需更多 sources。 | nahida-update | medium | queued |
| Production governance | 私有 metrics/thresholds 如何向用户解释、审计和合规仍需工程/治理 evidence。 | nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-collaborative-synthetic-data-generation | Created active_seed problem node and attached EndSDG source; linked to synthetic data privacy/trustworthy ML bridge. | 1 source note | codex |
