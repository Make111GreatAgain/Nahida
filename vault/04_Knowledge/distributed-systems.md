---
id: "nahida-knowledge-distributed-systems"
title: "Distributed systems"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "domain"
hierarchy_level: "domain"
file_slug: "distributed-systems"
domain_id: "distributed-systems"
direction_id: ""
parent_knowledge_refs:
  []
child_knowledge_refs:
  - "nahida-knowledge-consensus"
  - "nahida-knowledge-data-management-and-storage"
  - "nahida-knowledge-distributed-systems-research-dynamics"
  - "nahida-knowledge-transaction-processing"
ontology_path:
  - "distributed-systems"
primary_ontology_path: "distributed-systems"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-distributed-systems"
    relation: "has_child"
    to: "nahida-knowledge-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems.md"
      - "vault/04_Knowledge/distributed-systems/consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "has_child"
    to: "nahida-knowledge-data-management-and-storage"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems.md"
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "has_child"
    to: "nahida-knowledge-distributed-systems-research-dynamics"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems.md"
      - "vault/04_Knowledge/distributed-systems/research-dynamics.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "has_child"
    to: "nahida-knowledge-transaction-processing"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems.md"
      - "vault/04_Knowledge/distributed-systems/transaction-processing.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
  - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
  - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
  - "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
  - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
  - "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
representative_source_refs:
  - "arxiv:1812.07527v3"
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
  - "arxiv:2210.12605v1"
query_keys:
  - "Distributed systems"
  - "distributed-systems"
  - "分布式系统"
  - "data management and storage"
  - "storage engines"
  - "LSM-tree"
  - "CRDT"
  - "CRDTs"
  - "eventual consistency"
  - "CALM theorem"
  - "CRDT query model"
aliases:
  - "分布式系统"
domains:
  - "distributed-systems"
topics:
  - "CRDTs"
  - "eventual consistency"
  - "CRDT query safety"
tags:
  - "nahida/knowledge"
  - "nahida/domain"
freshness_status: "fresh"
last_synthesized: "2026-06-24"
valid_until: "2026-07-24"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-24"
created: "2026-06-20"
updated: "2026-06-24"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-paper-intake-20260623-canteen-crdt-datastore"
  - "nahida-knowledge-20260624-keep-calm-crdt-query-model"
source_refs:
  - "arxiv:1812.07527v3"
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
  - "arxiv:2210.12605v1"
confidence: "medium"
trust_tier: "primary"
---

# Distributed systems

## 定义与范围

- 定义: 分布式系统研究多个节点在延迟、故障、并发和不完整信息下如何协同完成可靠计算。当前 Nahida 对该域的覆盖集中在 consensus、fault tolerance 和 state-machine replication。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `distributed-systems`
- Aliases/query keys: 分布式系统
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `distributed-systems`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: [[04_Knowledge/distributed-systems/research-dynamics|Research dynamics]]

## 背景

model_prior_background: 分布式系统通常围绕通信模型、故障模型、一致性、复制和可用性展开；当前 vault 的 source-backed seed 主要来自 Byzantine Generals、PBFT 和 Raft。后续 source 已把本域扩展到 data-management-and-storage，其中 Canteen 新增 CRDT/SEC/coordination-free replication 这一 replicated data branch，Keep CALM and CRDT On 进一步补入 CRDT observations/queries 的 safe local execution 边界。

## 基础概念判断

- 是否是基础概念/方向/问题: `domain` / `domain`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: root domain。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

为共识、复制服务、故障容忍和后续区块链共识应用提供父域入口。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| root | L1 domain/root | canonical current architecture | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[consensus|consensus]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | child | 新 source 明确补出分布式/数据系统的存储管理分支，避免本域只按 consensus 检索 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| 故障模型 | 故障模型: crash fault 与 Byzantine fault | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| 复制与排序 | 复制与排序: state-machine replication / replicated log | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| 时序假设 | 时序假设: synchrony、partial synchrony、asynchrony | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| 数据管理与存储 | 持久化数据布局、索引、写入路径、读取路径、恢复和后台维护 | data systems / NoSQL / storage engine sources | 当前只有 LSM survey seed，仍需 B-tree、recovery、database storage sources | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] |
| Coordination-free replicated data | 用 CRDT/SEC 让 replicas 本地更新并最终收敛，并用 monotonicity 判断哪些 observations 可 local-safe 执行 | availability-first replicated datatypes, CRDT datastores, monotone query workloads | metadata GC、non-commutative operations、fault/equivocation tolerance、persistence/recovery 与 non-monotone query coordination 仍需 source 扩展 | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]]; [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-357172-357176-byzantine-generals-problem|The Byzantine Generals Problem]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|Practical Byzantine Fault Tolerance]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|In Search of an Understandable Consensus Algorithm]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | paper survey | 补入 data-management-and-storage / storage-engines / LSM-tree 分支 | 2019 survey，不代表最新存储引擎趋势 | Abstract, §1-§5 |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen: A Partially-Ordered Log Abstraction for the Emerging CRDT Datastore]] | paper | 补入 CRDTs / coordination-free replicated datatype 分支，并桥接 BFT/equivocation tolerance 边界 | proof-of-concept simulation；canonical CRDT foundations 待补 | Abstract, §2-§4 |
| [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] | paper / research agenda | 补入 CRDT query-safety 边界: monotone queries 可 local-safe，non-monotone observations 需要 coordination 或弱一致声明 | 没有完整 datastore/optimizer 实现；CALM/query-language foundations 待补 | Abstract, §3-§4 |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-24`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: 当前本域从 consensus-heavy seed 扩展出 data-management-and-storage 路径。Consensus 与 transaction-processing 仍是主要已有覆盖；storage engines 目前由 LSM survey 支撑，Canteen 与 Keep CALM and CRDT On 又补入 CRDT/coordination-free replicated datatype branch，包括 update convergence、metadata/GC 和 query/observation safety。其他存储/数据库/CRDT/CALM foundations 仍缺。

## 领域态势

- Research dynamics note: [[04_Knowledge/distributed-systems/research-dynamics|Research dynamics]]
- Dynamics freshness: stale/queued because no daily-fetch evidence exists
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-357172-357176-byzantine-generals-problem|The Byzantine Generals Problem]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|Practical Byzantine Fault Tolerance]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|In Search of an Understandable Consensus Algorithm]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | 新增 storage/data-management 分支 | 下级结构/方法族/代表 Sources/当前综合 | yes | keep child path |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] | 新增 CRDT/coordination-free replicated data 分支，并通过子节点桥接 BFT/equivocation boundary | 方法族/代表 Sources/当前综合 | yes through data-management child | 补 canonical CRDT foundation sources |
| [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] | 补入 CRDT query/observation safety 和 CALM monotonicity route | 方法族/代表 Sources/当前综合 | no | 补 CALM/query-language foundations |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| none | not_applicable | not_applicable | no bridge currently targets this node | review |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-distributed-systems | has_child | nahida-knowledge-consensus | vault/04_Knowledge/distributed-systems.md; vault/04_Knowledge/distributed-systems/consensus.md | medium | active_seed |
| nahida-knowledge-distributed-systems | has_child | nahida-knowledge-data-management-and-storage | vault/04_Knowledge/distributed-systems.md; vault/04_Knowledge/distributed-systems/data-management-and-storage.md; vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | medium | active_seed |
| nahida-knowledge-distributed-systems | has_child | nahida-knowledge-distributed-systems-research-dynamics | vault/04_Knowledge/distributed-systems.md; vault/04_Knowledge/distributed-systems/research-dynamics.md | medium | active_seed |
| nahida-knowledge-distributed-systems | has_child | nahida-knowledge-transaction-processing | vault/04_Knowledge/distributed-systems.md; vault/04_Knowledge/distributed-systems/transaction-processing.md | medium | active_seed |
| nahida-knowledge-distributed-systems | evidenced_by | vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | high | active_seed |
| nahida-knowledge-distributed-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md | vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md | medium | active_seed |
| nahida-knowledge-distributed-systems | evidenced_by | vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md | vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md | medium | active_seed |
| nahida-knowledge-distributed-systems | evidenced_by | vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md | vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md | medium | active_seed |
| nahida-knowledge-distributed-systems | evidenced_by | vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md | Canteen source note | medium | active_seed |
| nahida-knowledge-distributed-systems | evidenced_by | vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md | Keep CALM and CRDT On source note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Paxos/Multi-Paxos、Viewstamped Replication、FLP、DLS partial synchrony 仍缺直接 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 3 source notes; 1 legacy notes | codex |
| 2026-06-20 | nahida-paper-intake-20260620-item-0033 | Added data-management-and-storage child path and LSM survey as representative storage-engine evidence. | arxiv:1812.07527v3 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-canteen-crdt-datastore | Added CRDTs/coordination-free replicated data as a data-management child branch and bridge boundary with BFT/equivocation tolerance. | sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84 | codex |
| 2026-06-24 | nahida-knowledge-20260624-keep-calm-crdt-query-model | Added CRDT query/observation safety as a domain-level retrieval signal under data management. | arxiv:2210.12605v1 | codex |
