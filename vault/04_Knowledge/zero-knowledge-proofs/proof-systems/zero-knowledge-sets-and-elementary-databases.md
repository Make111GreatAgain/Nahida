---
id: "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
title: "Zero-knowledge sets and elementary databases"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "zero-knowledge-sets-and-elementary-databases"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "zero-knowledge-sets-and-elementary-databases"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/verifiable-database-queries"
relation_edges:
  - from: "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
    relation: "applies_to"
    to: "nahida-knowledge-verifiable-database-queries"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
      - "vault/05_Bridges/zero-knowledge-sets-to-verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
    relation: "bridges_to"
    to: "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
    evidence_refs:
      - "vault/05_Bridges/zero-knowledge-sets-to-verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
representative_source_refs:
  - "iacr:2023/156"
query_keys:
  - "Zero-knowledge sets and elementary databases"
  - "zero-knowledge sets"
  - "ZKS"
  - "zero-knowledge elementary database"
  - "ZK-EDB"
  - "ZK-EEDB"
  - "ZK-FEDB"
  - "set-operation ZKS"
  - "zero-knowledge database commitments"
aliases:
  - "ZKS"
  - "ZK-EDB"
  - "zero-knowledge database commitments"
domains:
  - "zero-knowledge-proofs"
topics:
  - "zero-knowledge-sets"
  - "zero-knowledge-elementary-databases"
  - "set-operation-queries"
  - "groups-of-unknown-order"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-zk-functional-elementary-databases"
source_refs:
  - "iacr:2023/156"
confidence: "medium"
trust_tier: "primary"
---

# Zero-knowledge sets and elementary databases

## 定义与范围

- 定义: Zero-knowledge sets 允许 prover 承诺一个有限集合，并随后证明元素属于或不属于该集合，同时不泄露额外集合信息，包括集合大小。Zero-knowledge elementary databases 把集合承诺扩展到 key-value partial function，证明某个 key 的 value 或不存在性。
- 不包含: 具体论文名、某个 Merkle tree 实现、普通 authenticated data structure、普通数据库事务或 SQL engine；这些留在 source notes 或应用节点中。
- Canonical terms: `zero-knowledge sets`, `zero-knowledge elementary databases`, `ZKS`, `ZK-EDB`
- Standalone completeness check: 本节点给出本地定义、问题、方法族、代表 source、桥接和边界；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 ZKS、ZK-EDB、ZK-FEDB、set-operation ZKS、database-size hiding 时优先读本节点，再进入 source note。
- Update scope: 后续吸收 Micali-Rabin-Kilian ZKS、Libert et al. ZK-EEDB、authenticated data structures、ZKSQL/private query papers 后应刷新。

## 背景

ZKS/ZK-EDB 位于 proof-system primitive 与数据库应用之间。它不像普通 SNARK 那样证明一个通用 circuit 的 witness relation，而是把 set/database 本身作为 committed object，并支持后续 membership、non-membership 或 query-result proof。

当前 vault 的主 source 是 [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]]。该论文在本地定义并回顾了 ZKS、ZK-EDB、ZK-EEDB 的表达力边界，并新增支持 combined set operations 的 ZKS，再用它构造 ZK-FEDB。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family`。
- 为什么足够通用: ZKS、ZK-EDB、ZK-FEDB、ZKSQL、private aggregate query 等都会复用“承诺数据结构 + 查询证明 + 隐藏未返回信息”的问题结构。
- 为什么不是单篇论文/单个协议: 当前 source 提供一个 construction，但本节点保存的是 primitive family 和查询能力层级。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[zero-knowledge-proofs|Zero-knowledge proofs]]。
- 不应拆出的实例/协议/来源: ZK-FEDB 先保留为 method route；MRK03、LNTW19 等未深读来源只作为后续补源线索。

## 解决的问题

ZKS/EDB 解决的是“对承诺集合或数据库回答查询时，如何同时保证正确性、完整性和零知识隐藏”的问题:

- Membership proof 要保证属于集合或 database support。
- Non-membership proof 要保证不存在性，而不暴露其他元素。
- EDB proof 要绑定 key 与唯一 value。
- Expressive query proof 要保证返回结果完整，不遗漏满足谓词的记录。
- Zero-knowledge 要隐藏集合/数据库大小和未返回记录。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of | ZKS/ZK-EDB are cryptographic proof/database-commitment primitives | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| ZKS membership/non-membership | 承诺集合后证明元素属于或不属于集合，同时隐藏集合大小。 | 查询只需要 membership semantics。 | 不直接支持 richer database queries。 | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| ZK-EDB point query | 把 key-value database 视为 partial function，证明 `D(x)=v` 或 `x` 不在 support。 | 需要查单个 key 的 value。 | 只支持点查询，表达力弱。 | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| ZK-EEDB range-style query | 在 key/value range 上返回满足条件的 records。 | 查询能表达为 range query 或简单组合。 | 无法支持一般 Boolean predicate。 | mentioned in [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| Set-operation ZKS | 用 union、intersection、difference 的可验证组合支持 set algebra queries。 | 查询能被转为 set-operation circuit。 | 当前 source 依赖 unknown-order groups、random oracle 和 generic group model。 | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| Functional EDB route | 把 Boolean predicate query 转换为 bit-position support sets 上的 set-operation query。 | 数据记录能编码为 fixed-length bits，谓词能表示为 Boolean circuit。 | Prover work 仍随数据库大小和 circuit size 增长。 | [[verifiable-database-queries|Verifiable database queries]] |

## 当前综合

- Evidence window: `2026-06-23`，仅覆盖当前已吸收 source。
- Freshness: `fresh` for current-vault synthesis; not a latest-trend claim.
- Valid until: `2026-07-23`。
- 综合: 当前节点是 `foundation_thin`。它足以说明 ZKS/ZK-EDB 的本地定义、set-operation extension 和 ZK-FEDB 的 proof primitive 路线，但还不足以覆盖完整 ZKS/ADS/ZK database 历史。ZK-FEDB 新增的关键知识是: 通用 functional query 的难点不只是证明 `returned rows satisfy f`，还要证明所有未返回行都不满足 `f`，同时隐藏数据库大小。set-operation ZKS 给出一条避免 witness-length leakage 的路线。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]] | 创建 ZKS/ZK-EDB primitive seed；新增 set-operation ZKS 和 ZK-FEDB route | 定义与范围; 方法族; 当前综合; Bridge Links | yes | 后续吸收 MRK03、LNTW19、ZKSQL/private aggregate query sources 后复核 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zero-knowledge-sets-to-verifiable-database-queries|Zero-knowledge sets -> verifiable database queries]] | `zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases; zero-knowledge-proofs/applications/verifiable-database-queries` | dependency, method_transfer, application | Set commitment/query proof transfers; real database execution, SQL optimization, transaction isolation and storage layout do not. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zero-knowledge-sets-and-elementary-databases | is_a | nahida-knowledge-proof-systems | this note | high | active_seed |
| nahida-knowledge-zero-knowledge-sets-and-elementary-databases | applies_to | nahida-knowledge-verifiable-database-queries | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] | high | active_seed |
| nahida-knowledge-zero-knowledge-sets-and-elementary-databases | evidenced_by | vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md | source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| MRK03 ZKS and Libert et al. ZK-EEDB not deep-read | 当前 foundation only comes through ZK-FEDB paper's related work and definitions | nahida-update / nahida-research-search | high | queued |
| ZKSQL and private aggregate query sources pending in queue | Need compare SQL/database application routes with ZK-FEDB set-operation route | nahida-update | high | pending_queue |
| Authenticated data structures boundary thin | Need distinguish three-party ADS from two-party malicious-committer ZK-EDB security | nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-zk-functional-elementary-databases | Created method-family seed from ZK-FEDB source; added set-operation ZKS and functional EDB route. | 1 source note | codex |
