---
id: "nahida-knowledge-conflict-free-replicated-data-types"
title: "Conflict-free replicated data types (CRDTs)"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "conflict-free-replicated-data-types"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
parent_knowledge_refs:
  - "nahida-knowledge-data-management-and-storage"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "conflict-free-replicated-data-types"
primary_ontology_path: "distributed-systems/data-management-and-storage/conflict-free-replicated-data-types"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
relation_edges:
  - from: "nahida-knowledge-conflict-free-replicated-data-types"
    relation: "part_of"
    to: "nahida-knowledge-data-management-and-storage"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-conflict-free-replicated-data-types"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-conflict-free-replicated-data-types"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-conflict-free-replicated-data-types"
    relation: "bridges_to"
    to: "nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types"
    evidence_refs:
      - "vault/05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "vault/05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types.md"
source_note_refs:
  - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
  - "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
representative_source_refs:
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
  - "arxiv:2210.12605v1"
query_keys:
  - "CRDT"
  - "CRDTs"
  - "Conflict-free replicated data types"
  - "strong eventual consistency"
  - "state-based CRDT"
  - "operation-based CRDT"
  - "delta CRDT"
  - "CRDT garbage collection"
  - "equivocation tolerant CRDT"
  - "CALM theorem"
  - "monotone CRDT queries"
  - "CRDT query model"
  - "coordination-free queries"
  - "non-monotone CRDT queries"
aliases:
  - "CRDTs"
  - "Conflict-free replicated datatypes"
  - "冲突自由复制数据类型"
domains:
  - "distributed-systems"
topics:
  - "CRDTs"
  - "eventual consistency"
  - "replicated data types"
  - "coordination-free replication"
  - "metadata garbage collection"
  - "CALM theorem"
  - "monotone queries"
  - "CRDT query safety"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-24"
valid_until: "2026-07-24"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-24"
created: "2026-06-23"
updated: "2026-06-24"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260623-canteen-crdt-datastore"
  - "nahida-knowledge-20260624-keep-calm-crdt-query-model"
source_refs:
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
  - "arxiv:2210.12605v1"
confidence: "medium"
trust_tier: "primary"
---

# Conflict-free replicated data types (CRDTs)

## 定义与范围

- 定义: Conflict-free replicated data types (CRDTs) 是一类复制数据类型，让多个 replicas 可以在不协调的情况下本地更新，并在交付相同 updates 后 deterministic convergence。当前节点把 CRDTs 作为 distributed data management 中的 replicated datatype / coordination-free consistency 问题，而不是单个数据库系统或单篇论文。
- 核心保证: strong eventual consistency (SEC)，即 correct replicas 交付相同 updates 时具有 equivalent state，不需要 rollback 或 conflict recovery。
- 不包含: 单个 CRDT 实现、Canteen、COG、OR-Set、0-bounded counter 或某次 simulation result；这些作为 source extension 或代表方案。
- Canonical terms: `CRDT`, `Conflict-free replicated data type`, `strong eventual consistency`, `state-based CRDT`, `operation-based CRDT`, `delta-CRDT`.
- Standalone completeness check: 本节点解释 CRDT 的一致性目标、主要类型、方法路线、Canteen 的增量、BFT/equivocation 边界和当前 gaps；但 canonical CRDT foundation sources 仍未单独导入，因此状态为 `foundation_thin`。
- Retrieval role: 让查询从 CRDT/SEC/coordination-free replication 入口进入，而不是直接扫 Canteen source note 或误入 consensus。
- Update scope: 新的 CRDT foundation paper、collaborative editing source、delta-CRDT、BFT CRDT、metadata GC、CRDT datastore 或 implementation source 可挂到本节点。

## 背景

source-backed seed: [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] 从 strong consistency/CAP/eventual consistency 出发，把 CRDTs 定位为 availability-first distributed systems 中避免 coordination 与 conflict rollback 的复制数据类型。论文覆盖了 EC/SEC、CvRDT、CmRDT、delta-CRDT 与 Byzantine/equivocation-tolerant CRDTs 的基础定义，但这些定义来自 Canteen 对 prior work 的回顾；Shapiro 2011、Preguiça 2018、Delta-CRDT 等 canonical sources 仍应后续补入。

[[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] 补上另一个 CRDT 核心缺口: CRDT guarantees 只保证 updates/merge 最终收敛，不保证任意 observations/queries 都安全。该文把 CALM theorem 的 monotonicity criterion 用到 CRDT state/query 上，说明 monotone queries 可以在 local replica 上无协调执行，而 set difference、absence、checkout 这类 non-monotone queries 需要协调、预协调或明确作为 weak/stale read 处理。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `foundation_thin`。
- 为什么足够通用: CRDTs 组织 eventual consistency、replicated datatype、coordination-free updates、metadata garbage collection、collaborative editing、BFT/equivocation tolerance 等多类 source，而不是 Canteen 一篇论文的专有机制。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Canteen 是一个 partially-ordered log abstraction/source instance；CRDTs 是它依赖和扩展的上层问题族。
- 需要引用的更基础 Knowledge: [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]；与 [[byzantine-fault-tolerance|Byzantine fault tolerance]] 有窄桥。
- 不应拆出的实例/来源: Canteen、COG、0-bounded counter、Observed-Remove Set 示例暂不建独立上层节点。

## 解决的问题

- 在 network partition、高延迟或多副本部署中，如何让 replicas 本地接受更新而不等待全局协调。
- 如何保证 replicas 最终收敛，并在交付相同 updates 时得到相同 state。
- 如何减少 CRDT metadata、versioning/causality tracking 和 garbage collection 的长期成本。
- 如何表达非交换或业务约束较强的操作，同时保持 deterministic convergence。
- 当 Byzantine/equivocating replica 存在时，如何保持 CRDT 的 SEC 边界。
- 如何判断 CRDT 上的 query/observation 是否可以本地无协调执行，并仍然给出不会被未来 updates 推翻的结果。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | `part_of` | Canteen treats CRDTs as replicated datatype/datastore abstraction with metadata, persistence and recovery implications. | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| State-based CRDTs / CvRDTs | method family candidate | join-semilattice + monotonic operations 是 CRDT 的经典路线 | Canteen §2.2-§2.3 | queued until canonical sources |
| Operation-based CRDTs / CmRDTs | method family candidate | causal broadcast + commutative concurrent operations 是另一条核心路线 | Canteen §2.4-§2.5 | queued until canonical sources |
| Delta state-based CRDTs | optimization candidate | 针对 CvRDT full-state gossip 开销，但需要处理 redundant delta propagation | Canteen §2.6 | queued until direct delta-CRDT sources |
| Equivocation-tolerant CRDTs | bridge/method candidate | Byzantine/equivocation setting 与 BFT consensus 有重要边界 | Canteen §2.7, §3.2 | bridge active_seed |
| Partially-ordered-log CRDT datastores | method/source-extension candidate | Canteen 展示把 CRDT operations 组织成 hash-chained DAG/COGs | Canteen §3 | source extension |
| CRDT query models / monotone observations | method family candidate | CRDT update convergence 不自动保证 read/query safety，需要独立判断 observation 是否 monotone | Keep CALM and CRDT On §3-§4 | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| State-based CRDTs (CvRDTs) | replicas gossip states 并用 join/least upper bound 合并；operations 必须 monotonic | reliable broadcast 足够，适合简单/稳健 convergence | full-state gossip 网络开销可能高 | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] §2.3 |
| Operation-based CRDTs (CmRDTs) | local prepare 后 causal broadcast operation message；remote effect 按 causal order 应用 | payload 小于 full state，适合操作传播 | 需要 causal broadcast；concurrent operations 必须 commutative | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] §2.5 |
| Delta state-based CRDTs | 发送 delta groups 而不是完整 state | 希望降低 CvRDT payload | 高连通/cyclic topology 中 naive delta propagation 可能更差，需要额外 metadata/analysis | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] §2.6 |
| Partially ordered log + COG compaction | 用 hash-chained operation DAG 保存 causality；通过 delta swaps 形成 COGs，稳定后 compact metadata | 需要通用 CRDT datastore abstraction、GC 和 non-commutative operations | 当前为 proof-of-concept simulation；COG interpreter 需要处理 compacted/non-compacted 边界 | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] §3-§4 |
| Equivocation-tolerant CRDTs | 用 hash-chained graph/operation IDs 让 equivocation 反映在 causality roots/DAG divergence 中 | Byzantine/equivocating replicas，但 correct nodes 可直接通信 | 不等同 BFT consensus 的 quorum/total order；需要 bridge 边界 | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] §2.7, §3.2 |
| CALM-based monotone query model | 把 CRDT state 看作 semilattice；若 query 对 lattice order 单调，则 local replica 的 partial state 足以给出不会被未来 state 推翻的 safe result | threshold/positive information queries、append/grow-only observations、可被语法或类型系统识别的 monotone logic | set difference、absence、checkout 等 non-monotone queries 需要 coordination、pre-coordination 或 weak/stale API | [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] §3-§4 |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen: A Partially-Ordered Log Abstraction for the Emerging CRDT Datastore]] | paper | 创建 CRDTs seed 节点；补入 SEC/CvRDT/CmRDT/delta-CRDT 背景；提出 partially ordered log + COG route 支持 generalized GC、non-commutative operations 和 equivocation tolerance | proof-of-concept simulation；venue/DOI unknown；canonical CRDT papers 未单独导入 | Abstract, §2, §3, §4 |
| [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] | paper / research agenda | 补入 CRDT query-safety 问题；用 CALM monotonicity 区分 local-safe queries 和需要 coordination 的 non-monotone observations；提出 CRDT data-store/query-language agenda | 没有实现完整 data store 或 optimizer；CALM/Bloom/Datafun 等 foundation source 仍可单独补 | Abstract, §3, §4 |

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-24`。
- Freshness: `fresh` for current vault absorption; not external latest check.
- Valid until: `2026-07-24`。
- 综合: 当前 vault 将 CRDTs 建为 data-management-and-storage 下的复制数据类型问题，并且已经覆盖两类互补问题。Canteen 的价值不在于替代 CRDT foundation，而在于暴露 metadata garbage collection、non-commutative operations、fault/equivocation tolerance 和 datastore integration。Keep CALM and CRDT On 则补上 observation/query safety: CRDT update convergence 不等于任意 read 都一致；monotone queries 可以 local-safe，non-monotone queries 需要 coordination 或显式弱一致语义。当前节点足以作为 CRDT/SEC/coordination-free query 的入口，但还不能宣称完整 CRDT foundation，因为 Shapiro/Preguiça/Delta-CRDT/协同编辑/CALM 直接 sources 尚未系统吸收。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] | 新建 CRDTs problem node；补入 SEC/CvRDT/CmRDT/delta-CRDT 背景；把 Canteen 作为 partially-ordered-log/COG source extension；建立 BFT/equivocation bridge。 | 定义、背景、解决的问题、方法族、代表 Sources、Bridge Links、缺口 | yes | 补 canonical CRDT foundation pack；未来若更多 source 使用 COG/partially ordered logs，再考虑拆 child node |
| [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] | 补入 CRDT query-safety 和 CALM-based monotone observation 模型；把 non-monotone queries 的 coordination/stale-read 边界加入方法族。 | 背景、解决的问题、下级结构、方法族、代表 Sources、当前综合、缺口 | no | 补 CALM/Bloom/Datafun/CRDT query systems foundation；若更多来源复用再拆 `crdt-query-models` child node |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types|Byzantine fault tolerance -> CRDTs]] | `distributed-systems/consensus/byzantine-fault-tolerance` -> `distributed-systems/data-management-and-storage/conflict-free-replicated-data-types` | adaptation, equivocation_boundary, non_transfer_boundary | Byzantine/equivocation threat transfers; BFT consensus quorum/total-order protocol does not automatically transfer to SEC/CRDT convergence. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-conflict-free-replicated-data-types | part_of | nahida-knowledge-data-management-and-storage | Canteen source note; data-management parent | high | active_seed |
| nahida-knowledge-conflict-free-replicated-data-types | evidenced_by | vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md | Canteen Abstract, §2-§4 | high | active_seed |
| nahida-knowledge-conflict-free-replicated-data-types | evidenced_by | vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md | Keep CALM and CRDT On Abstract, §3-§4 | high | active_seed |
| nahida-knowledge-conflict-free-replicated-data-types | bridges_to | nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types | bridge note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Shapiro 2011 CRDT paper / Preguiça overview 未导入 | 需要 canonical foundation source，而不是只依赖 Canteen 的背景回顾 | `nahida-research-search` or future paper intake | high | queued |
| Delta-CRDT、pure operation-based CRDT、efficient synchronization direct sources 缺失 | 当前方法族来自 Canteen 转述，不能替代直接 foundation | `nahida-research-search` or future papers | medium | queued |
| Collaborative editing CRDT sources 缺失 | Canteen 提到 WOOT/Peritext，但没有形成应用/benchmark 覆盖 | future paper/web/repo sources | medium | queued |
| Production CRDT datastore/repo evidence 缺失 | Canteen 只是 proof-of-concept simulation | `nahida-github-repo-analyze` or future source | medium | queued |
| CALM theorem / monotone query language direct sources 缺失 | Keep CALM 使用 CALM/BloomL/Lasp/Datafun 作为 query-safety foundation，但这些目前还不是本 vault 的独立 source notes | `nahida-research-search` foundation_pack | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-paper-intake-20260623-canteen-crdt-datastore | Created CRDTs problem node from Canteen; added SEC/CvRDT/CmRDT/delta-CRDT background, Canteen source extension, and BFT/equivocation bridge. | sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84 | codex |
| 2026-06-24 | nahida-knowledge-20260624-keep-calm-crdt-query-model | Added CALM-based CRDT query-safety method family, monotone/non-monotone observation boundary, and CRDT data-store query agenda. | arxiv:2210.12605v1 | codex |
