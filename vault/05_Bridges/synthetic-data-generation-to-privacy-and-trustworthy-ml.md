---
id: "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
title: "Synthetic data generation -> privacy and trustworthy ML"
original_title: ""
file_slug: "synthetic-data-generation-to-privacy-and-trustworthy-ml"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_direction"
bridge_status: "active_seed"
endpoint_paths:
  - "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
  - "ml-systems/privacy-and-trustworthy-ml"
endpoint_knowledge_refs:
  - "nahida-knowledge-synthetic-data-privacy-evaluation"
  - "nahida-knowledge-collaborative-synthetic-data-generation"
  - "nahida-knowledge-privacy-and-trustworthy-ml"
from_domain: "ml-systems"
to_domain: "ml-systems"
from_direction: "synthetic-data-generation"
to_direction: "privacy-and-trustworthy-ml"
from_topic: "synthetic-data-privacy-evaluation"
to_topic: ""
relation_types:
  - "tension"
  - "privacy_boundary"
  - "evaluation_transfer"
  - "trustworthiness_dependency"
  - "construction_route"
directionality: "two_way"
relationship_thesis: "Synthetic data generation can be used for data sharing and privacy-sensitive workflows, but privacy/trustworthiness does not follow from fidelity, utility, or similarity metrics; it must be established through process-level guarantees such as Differential Privacy, explicit threat-model-specific attack evaluation, and in collaborative settings a separate input-privacy boundary such as MPC."
transferability: "medium"
non_transfer_boundary: "Data-generation fidelity, downstream ML utility, train/synthetic distance metrics, and MPC secrecy over inputs do not automatically transfer into final release privacy. Privacy claims depend on the full release pipeline, metric/filter access, adversary query ability, outlier behavior, DP budget accounting, private preprocessing/evaluation/tuning, and governance controls."
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
knowledge_refs:
  - "nahida-knowledge-synthetic-data-privacy-evaluation"
  - "nahida-knowledge-collaborative-synthetic-data-generation"
  - "nahida-knowledge-ml-systems-synthetic-data-generation"
  - "nahida-knowledge-tabular-synthetic-data-generation"
  - "nahida-knowledge-privacy-and-trustworthy-ml"
representative_source_refs:
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
query_keys:
  - "synthetic data privacy trustworthy ML bridge"
  - "synthetic data generation privacy boundary"
  - "similarity metrics anonymity synthetic data"
  - "DP synthetic data release boundary"
  - "ReconSyn synthetic data privacy"
  - "collaborative synthetic data input privacy output privacy"
  - "MPC DP synthetic data release"
aliases:
  - "Synthetic data privacy boundary"
  - "Collaborative synthetic data privacy boundary"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "synthetic-data-privacy-evaluation"
  - "privacy-and-trustworthy-ml"
  - "differential-privacy"
  - "membership-inference"
  - "reconstruction-attacks"
  - "collaborative-synthetic-data-generation"
  - "secure-multiparty-computation"
tags:
  - "nahida/bridge"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-synthetic-data-privacy-metrics"
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
source_refs:
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
confidence: "high"
trust_tier: "primary"
---

# Synthetic data generation -> privacy and trustworthy ML

## 命名与路径

- Original title: Synthetic data generation -> privacy and trustworthy ML
- File slug: `synthetic-data-generation-to-privacy-and-trustworthy-ml`
- Path safety check: endpoints are existing/new knowledge IDs in `04_Knowledge`, not source-only entities.

## 连接命题

- From: [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] under [[synthetic-data-generation|Synthetic data generation]]
- To: [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]]
- Endpoint knowledge paths: `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation`; `ml-systems/privacy-and-trustworthy-ml`
- Relation types: tension, privacy_boundary, evaluation_transfer, trustworthiness_dependency, construction_route
- Directionality: two_way
- Relationship thesis: Synthetic data generation is often used to support data sharing and privacy-sensitive workflows, but fidelity/utility/similarity metrics do not imply anonymity. The privacy claim must be checked at the ML trust boundary with process-level guarantees, explicit threat model, attack evaluation, and for collaborative release a separate input-privacy design.
- 层级路径: `ml-systems/synthetic-data-generation` connects to `ml-systems/privacy-and-trustworthy-ml` through the reusable problem nodes `synthetic-data-privacy-evaluation` and `collaborative-synthetic-data-generation`.
- Standalone completeness check: 本 bridge 独立说明 synthetic data generation 能迁移到 privacy/trustworthy ML 的部分、不能迁移的部分、证据和查询入口。

## 端点范围

| Endpoint | Path | Scope in bridge | Evidence | Notes |
| --- | --- | --- | --- | --- |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | synthetic data release privacy, metric leakage, membership/attribute/reconstruction attacks, DP boundary | SBPM attacks paper | Specific endpoint because privacy evaluation is now source-backed. |
| [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]] | `ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation` | multi-custodian input/output privacy, private preprocessing/evaluation/tuning, final-output-only release | EndSDG | Specific subproblem showing constructive MPC + DP pipeline route. |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | `ml-systems/privacy-and-trustworthy-ml` | broader ML trust boundary: privacy, integrity, auditability, adversarial behavior and process guarantees | existing trustworthy ML node + SBPM paper | Direction endpoint remains broad until DP/private-data-release children are built. |

## 端点基础说明

Synthetic data generation creates artificial records to support training, testing, simulation or sharing. Its native evaluation axes include fidelity and downstream utility, but those axes do not decide whether a release process protects individuals in the training data.

Privacy and trustworthy ML asks what data, model behavior, updates, outputs or evaluation processes can be trusted under an explicit threat model. For synthetic data, the relevant trust boundary includes not only the generator, but also filters, metrics, metric outputs, repeated queries, train-data access, preprocessing, hyperparameter tuning, threshold votes and privacy-budget accounting.

## 可迁移知识/模式

| 概念/模式 | 来源方向 | 目标方向 | 可迁移部分 | 不可迁移部分 |
| --- | --- | --- | --- | --- |
| Fidelity/utility evaluation | synthetic data generation | privacy/trustworthy ML | Helps describe whether data is useful and distributionally close. | Does not imply anonymity or train-record protection. |
| Similarity-based metrics | synthetic data generation | privacy evaluation | Can serve as weak debugging/auditing signals. | Cannot become formal privacy guarantee; metrics can leak. |
| Attack-based auditing | privacy/trustworthy ML | synthetic data generation | Brings membership, attribute and reconstruction threat models into release evaluation. | Attack failure is not a formal proof of safety. |
| Differential Privacy | privacy/trustworthy ML | synthetic data release | Provides process-level route for privacy guarantee when implemented end-to-end. | Utility tradeoff and downstream filters/metrics must still preserve the guarantee. |
| MPC input privacy | privacy/trustworthy ML / secure computation | collaborative synthetic data release | Lets multiple data custodians compute over combined data without revealing raw inputs to a single party. | Does not by itself make the released synthetic data private; output privacy still needs DP or equivalent guarantee. |
| Private evaluation/tuning | synthetic data release workflow | privacy/trustworthy ML | Keeps metrics, thresholds and intermediate models/data inside the trust boundary during hyperparameter search. | Governance, auditability and accidental side-channel/log leakage still need explicit controls. |
| Outlier analysis | synthetic data evaluation | privacy/trustworthy ML | Highlights worst-case records at high privacy risk. | Outlier distance depends on representation and domain semantics. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Synthetic-data release workflow | `ml-systems/synthetic-data-generation` | `ml-systems/privacy-and-trustworthy-ml` | Treat release as a trust boundary containing generator, metrics, filters and query access. | SBPM paper Sections 2, 5 | Workflow details differ across products. |
| Metric vulnerability | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | `ml-systems/privacy-and-trustworthy-ml` | DifferenceAttack and ReconSyn show metric outputs can leak membership, attributes and outliers. | SBPM paper Sections 5-6 | Requires metric/generator access assumptions. |
| Formal guarantee demand | `ml-systems/privacy-and-trustworthy-ml` | `ml-systems/synthetic-data-generation` | DP or equivalent process-level reasoning should bound privacy claims. | SBPM paper DP discussion | DP utility/freshness tradeoff not solved here. |
| Collaborative release construction | `ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation` | `ml-systems/privacy-and-trustworthy-ml` | EndSDG shows that input privacy and output privacy must be separately designed: MPC for secret-shared combined computation, DP for final synthetic data release, private evaluation/tuning for metrics and thresholds. | EndSDG Algorithm 1 and §3 | DP preprocessing and optimized MPC remain open; code not analyzed. |
| Worst-case privacy focus | `privacy/trustworthy ML` | `synthetic data evaluation` | Evaluate low-density records and outliers rather than average similarity only. | ReconSyn experiments | Outlier definition may be metric-dependent. |

## 类比、依赖或关系边界

- 可迁移: threat model discipline, privacy guarantee vocabulary, attack auditing, privacy-budget reasoning, outlier-oriented risk analysis, MPC-style input privacy separation, private evaluation/tuning discipline.
- 不可迁移: generator fidelity, downstream ML utility, nearest-neighbor distance, visual/statistical similarity, MPC input secrecy, or vendor pass/fail privacy reports do not automatically transfer to anonymity.
- 关键假设: adversary capabilities are explicit; metric/filter access is included in the release process; source evidence remains scoped to tabular/collaborative synthetic data until more sources arrive.
- 失效条件: metrics are treated as proof, train-data-dependent filters are exposed without budget accounting, repeated queries are allowed without threat modeling, or outlier leakage is ignored.

## 证据

| Source/Note | 支撑内容 | 置信度 | 局限 |
| --- | --- | --- | --- |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] Abstract and Section 1 | Synthetic data privacy claims often rely on SBPMs rather than DP; authors challenge that practice. | high | Source-authored motivation; focused on tabular data. |
| Same source Sections 2.3-4 | IMS/DCR/NNDR/SF/OF and counterexamples show similarity metrics can pass despite severe leakage. | high | Counterexamples are constructed, not production incidents. |
| Same source Sections 5-6 | DifferenceAttack and ReconSyn demonstrate membership, attribute and reconstruction attacks through metric/generator access. | high | Requires attack interface assumptions. |
| Same source Section 6.4 and discussion | DP on the generator alone can be broken by downstream metric/filter access; mitigations carry budget/transparency/call-limit tradeoffs. | high | Not a full DP synthetic data construction paper. |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] Abstract and §1 | Collaborative SDG needs input privacy and output privacy, not just local training of a synthesizer. | high | ArXiv preprint; framework evidence, not production proof. |
| Same source Algorithm 1 and §3 | Private preprocessing, k-fold evaluation, threshold voting and final-output-only release define a constructive pipeline boundary. | high | Requires no intermediate output leakage. |
| Same source Appendix A.5 | DP quantile binning remains open; exact MPC quantiles are not sufficient for output DP. | high | Important limitation for release guarantee. |

## 路径传播

| Endpoint path | Knowledge update | Relation/index update | Bridge/refresh action | Status |
| --- | --- | --- | --- | --- |
| `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | Created active seed evaluation-axis node. | Added `bridges_to` and `evidenced_by` relations. | Created this bridge. | done |
| `ml-systems/synthetic-data-generation` | Added child/evaluation axis and source extension. | Added source and bridge refs. | Bridge link row. | done |
| `ml-systems/privacy-and-trustworthy-ml` | Added synthetic data release privacy as method/problem route. | Added source and bridge refs. | Bridge link row. | done |
| `ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation` | Created active seed problem node. | Added `bridges_to` and `evidenced_by` relations. | Bridge link row. | done |
| `ml-systems/research-dynamics` | Added current-vault dynamic for synthetic data privacy boundary. | Added source evidence. | Refresh trigger updated. | done |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | New node | The source creates a reusable evaluation axis/problem. | done |
| [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]] | New node | EndSDG creates a reusable multi-custodian release problem. | done |
| [[synthetic-data-generation|Synthetic data generation]] | Child structure, methods, source extension, gaps | Synthetic data direction now includes privacy release boundary. | done |
| [[tabular-synthetic-data-generation|Tabular synthetic data generation]] | Problems, methods, source extension | Current evidence is tabular synthetic data. | done |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | Methods, sources, bridge links | Privacy/trustworthy ML must include synthetic data release risks. | done |

## 查询入口

- Query keys:
  - synthetic data privacy boundary
  - synthetic data similarity metrics anonymity
  - SBPM privacy attack
  - ReconSyn
  - DP synthetic data release
  - collaborative synthetic data input privacy
  - MPC DP synthetic data release
- Aliases:
  - Synthetic data privacy boundary
- 典型问题:
  - 合成数据只要和训练数据距离远就匿名吗?
  - Similarity-based privacy metrics 有什么问题?
  - 为什么 DP generator 之后再跑 train-data-dependent metrics 会破坏端到端隐私?
  - ReconSyn 说明了合成数据发布流程中的什么风险?
  - 多个机构协作生成合成数据时 input privacy 和 output privacy 怎么分开?

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers:
  - 新 DP synthetic data、privacy-preserving synthetic data、synthetic data attack/audit source 被吸收。
  - 新 commercial synthetic data privacy report/web source 被吸收。
  - 后续 queue 中 collaborative synthetic data generation 或 privacy-preserving preprocessing/evaluation source 被吸收。
  - 用户询问最新 synthetic data privacy practice，需要 daily-fetch/research-search。

## 复核笔记

- 本 bridge 是 active_seed，因为当前只有一篇直接 source 深读，但它与 CTGAN/FTS-Diffusion 形成清晰的 evaluation-axis extension。
- 不应把 SBPM 写成 safe privacy mechanism；本 bridge 的用途正是防止 fidelity/utility/similarity 结论被错误迁移到 privacy guarantee。
- Endpoint `privacy-and-trustworthy-ml` 仍偏宽；后续若 DP/private-data-release sources 增多，可拆出 `privacy-preserving data release` 或 `DP synthetic data release` 子节点并收窄本 bridge。
- EndSDG 添加的是 constructive route，不抵消 SBPM 的攻击结论；它说明 metrics/tuning 必须保持私有，且 DP preprocessing caveat 仍需补 source。

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-synthetic-data-privacy-metrics | Created bridge from synthetic data privacy evaluation to privacy/trustworthy ML using SBPM attack evidence. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-collaborative-synthetic-data-generation | Refreshed bridge with EndSDG as collaborative input/output privacy construction route. | 1 source note | codex |
