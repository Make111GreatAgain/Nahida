---
id: "nahida-knowledge-data-management-and-storage"
title: "Data Management and Storage"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "data-management-and-storage"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
parent_knowledge_refs:
  - "nahida-knowledge-distributed-systems"
child_knowledge_refs:
  - "nahida-knowledge-storage-engines"
  - "nahida-knowledge-privacy-preserving-database-queries"
  - "nahida-knowledge-erasure-coded-storage"
  - "nahida-knowledge-conflict-free-replicated-data-types"
  - "nahida-knowledge-content-addressed-storage"
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
primary_ontology_path: "distributed-systems/data-management-and-storage"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "part_of"
    to: "nahida-knowledge-distributed-systems"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems.md"
      - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-storage-engines"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-privacy-preserving-database-queries"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/privacy-preserving-database-queries.md"
      - "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-erasure-coded-storage"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/erasure-coded-storage.md"
      - "vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-conflict-free-replicated-data-types"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/conflict-free-replicated-data-types.md"
      - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-content-addressed-storage"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/content-addressed-storage.md"
      - "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
    confidence: "high"
    status: "active"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "bridges_to"
    to: "nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries"
    evidence_refs:
      - "vault/05_Bridges/privacy-preserving-database-queries-to-verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "bridges_to"
    to: "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
    evidence_refs:
      - "vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-management-and-storage"
    relation: "bridges_to"
    to: "nahida-bridge-content-addressed-storage-to-decentralized-storage-networks"
    evidence_refs:
      - "vault/05_Bridges/content-addressed-storage-to-decentralized-storage-networks.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "vault/05_Bridges/storage-engines-to-blockchain-state-storage.md"
  - "vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md"
  - "vault/05_Bridges/privacy-preserving-database-queries-to-verifiable-database-queries.md"
  - "vault/05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types.md"
  - "vault/05_Bridges/content-addressed-storage-to-decentralized-storage-networks.md"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
  - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
  - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
  - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
  - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
  - "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
  - "vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md"
  - "vault/03_Sources/papers/sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code.md"
  - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
  - "vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md"
  - "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
  - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
representative_source_refs:
  - "doi:10.1007/s002360050048"
  - "arxiv:1812.07527v3"
  - "arxiv:1903.01919v2"
  - "arxiv:2306.10739v1"
  - "arxiv:2207.02746"
  - "doi:10.5281/zenodo.10225325"
  - "doi:10.1109/INFOCOM53939.2023.10228984"
  - "usenix:fast18-vajha"
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
  - "arxiv:2210.12605v1"
  - "isbn:978-7-111-62880-4"
  - "doi:10.14778/3594512.3594513"
query_keys:
  - "data management and storage"
  - "distributed storage engines"
  - "NoSQL storage management"
  - "数据管理与存储"
  - "LSM-tree"
  - "deferred index maintenance"
  - "history table indexing"
  - "provenance queries"
  - "blockchain relational database"
  - "blockchain state storage"
  - "authenticated state storage"
  - "learned index blockchain storage"
  - "storage engine snapshot API"
  - "database replication storage engine"
  - "privacy-preserving database queries"
  - "private aggregate queries"
  - "private information retrieval"
  - "erasure-coded storage"
  - "repair bandwidth"
  - "sub-packetization"
  - "Reed-Solomon storage"
  - "MSR codes"
  - "OpenEC"
  - "Clay codes"
  - "Ceph vector codes"
  - "vector erasure codes"
  - "sub-chunk repair"
  - "CRDT"
  - "CRDTs"
  - "Conflict-free replicated data types"
  - "strong eventual consistency"
  - "CRDT garbage collection"
  - "equivocation tolerant CRDT"
  - "CRDT query model"
  - "CALM theorem"
  - "monotone CRDT queries"
  - "coordination-free CRDT queries"
  - "content-addressed storage"
  - "IPFS"
  - "CID"
  - "IPLD"
  - "Merkle DAG"
  - "BitSwap"
  - "pinning"
  - "verifiable SQL query evaluation"
  - "authenticated SQL queries"
aliases:
  - "数据管理与存储"
  - "Data systems storage"
domains:
  - "distributed-systems"
topics:
  - "data management"
  - "storage"
  - "history table indexing"
  - "deferred index maintenance"
  - "provenance queries"
  - "blockchain state storage"
  - "replicated database storage interface"
  - "privacy-preserving database queries"
  - "private aggregate queries"
  - "erasure-coded storage"
  - "storage repair optimization"
  - "vector erasure codes"
  - "MSR codes"
  - "CRDTs"
  - "eventual consistency"
  - "coordination-free replication"
  - "CRDT query safety"
  - "monotone query processing"
  - "content-addressed storage"
  - "peer-to-peer storage"
  - "distributed file systems"
  - "verifiable query processing"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-24"
valid_until: "2026-07-24"
evidence_window_start: "1996"
evidence_window_end: "2026-06-24"
created: "2026-06-20"
updated: "2026-06-24"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260620-item-0033"
  - "nahida-knowledge-20260622-blockchain-meets-database"
  - "nahida-knowledge-20260622-cole-blockchain-storage"
  - "nahida-knowledge-20260623-c5-cloned-concurrency-control"
  - "nahida-knowledge-20260623-private-aggregate-queries"
  - "nahida-knowledge-20260623-elastic-transformation-erasure-coded-storage"
  - "nahida-paper-intake-20260623-clay-codes"
  - "nahida-paper-intake-20260623-canteen-crdt-datastore"
  - "nahida-knowledge-20260624-keep-calm-crdt-query-model"
  - "nahida-knowledge-20260623-ipfs-principles-and-practice"
  - "nahida-paper-intake-20260623-lsm-tree"
  - "nahida-knowledge-20260623-zksql"
source_refs:
  - "doi:10.1007/s002360050048"
  - "sha256:8fe1d3206fe8eb151e9d8c54e0772a46786e2ec40e4c2b7782995067d6b938c6"
  - "arxiv:1812.07527v3"
  - "arxiv:1903.01919v2"
  - "arxiv:2306.10739v1"
  - "arxiv:2207.02746"
  - "doi:10.5281/zenodo.10225325"
  - "doi:10.1109/INFOCOM53939.2023.10228984"
  - "usenix:fast18-vajha"
  - "sha256:b04fe9944676db0a3a6da4091a54d6c57bce7ebee6f8058c4077c1b59e14880a"
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
  - "arxiv:2210.12605v1"
  - "isbn:978-7-111-62880-4"
  - "doi:10.14778/3594512.3594513"
confidence: "medium"
trust_tier: "primary"
---

# Data Management and Storage

## 定义与范围

- 定义: `data-management-and-storage` 是 distributed systems 下处理数据持久化、索引、冗余、更新、恢复、查询代价和系统存储层权衡的方向。它关注数据系统如何在分布式或大规模环境中组织数据，而不是共识协议本身。
- 不包含: 单个数据库系统、单篇 survey、单个 compaction trick 或 benchmark 结果；这些应作为 source extension 或代表实例。
- Canonical terms: `data management`, `storage management`, `storage engines`, `NoSQL storage`, `erasure-coded storage`, `content-addressed storage`
- Standalone completeness check: 本节点提供方向定义、边界、问题和下级结构；具体 LSM-tree 技术在子节点展开。
- Retrieval role: 让查询从 distributed systems 快速进入“数据如何存、索引如何维护、写读空间如何权衡”的路线，而不是误落到 consensus。
- Update scope: 新的存储引擎、分布式数据库、索引维护、云存储系统、纠删码存储修复、存储查询隐私、内容寻址/P2P 存储 source 可挂到本方向或其子节点。

## 背景

model_prior_background: 分布式系统除了共识和事务，还需要数据层支持高吞吐写入、可恢复持久化、索引、范围查询、冗余修复、复制数据收敛和后台维护。[[doi-10-1007-s002360050048-log-structured-merge-tree|原始 LSM-tree 论文]] 提供了当前 vault 中第一个强 source-backed storage-engine/access-method foundation，说明 history/log index 这类写密集负载为什么需要 defer-and-batch index maintenance；`LSM-based Storage Techniques: A Survey` 则把 LSM-tree 放在 NoSQL/data-system storage management 的现代脉络中。Blockchain Meets Database 作为 secondary evidence 展示了另一类数据管理信号: MVCC 历史版本和 ledger table 可以支持链上 provenance/audit SQL queries，但它的主路径仍在区块链执行层。COLE 进一步展示 storage-engine mechanisms 迁移到 blockchain state storage 时，需要额外处理 authenticated data、proof completeness 和 deterministic state-root updates。C5 新增一个数据库复制方向的 secondary signal: storage-engine 的 snapshot/log/timestamp API 会约束备库 cloned concurrency control 能否实现理想的 row-granularity 和 prefix snapshot exposure。Private Aggregate Queries 新增查询隐私方向: 不可信数据库服务下的 SUM/COUNT/MEAN/histogram 等分析查询需要隐藏查询条件和参与聚合的记录集合。ZKSQL 新增可验证查询处理的 secondary signal: SQL operator pipeline 可以成为证明对象，但其主路径在 [[verifiable-database-queries|Verifiable database queries]]，不是事务、存储引擎或普通 query optimizer。Elastic Transformation 新增纠删码存储修复方向: 低冗余容错不仅需要能重建数据，还要控制 repair bandwidth、sub-packetization 和 non-sequential I/O 之间的系统权衡。Clay Codes 进一步补入 Ceph/vector-code 实践路线，说明 MSR code 若要进入真实对象存储，还必须让系统支持 sub-chunk repair、helper selection 和 fragmented-read 边界。Canteen 新增 CRDT 方向: coordination-free replicated datatypes 不只要最终收敛，还要处理 metadata garbage collection、non-commutative operations、persistence/recovery 和 equivocation tolerance。[[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] 进一步把 CRDT 数据管理扩展到 query/observation safety: monotone queries 可以在 local replica 上无协调执行，non-monotone queries 需要协调、预协调或弱一致 API。`IPFS原理与实践` 新增内容寻址/P2P 存储方向: 数据身份由 CID/content hash 绑定，DHT/provider routing 与 BitSwap 负责定位和交换，Merkle DAG/IPLD 负责对象图与去重，pinning/replication/DSN 激励则是独立可用性问题。

## 解决的问题

- 数据在多节点或大规模系统中如何持久化和恢复。
- 索引结构如何平衡写入吞吐、查询延迟、空间利用率和后台维护。
- 存储层如何为上层事务、查询处理、NoSQL workload 或分析系统提供稳定成本边界。
- 数据库查询服务如何在不泄露用户查询条件、访问模式和聚合记录集合的前提下返回统计结果。
- SQL query service 如何证明 answer 对私有表和 query plan 是正确完整的，同时不把 input rows 和 intermediate results 暴露给 verifier。
- 低冗余存储如何在节点/块失效后降低修复带宽，同时避免高 sub-packetization 带来的 non-sequential I/O 反噬。
- Vector erasure code / MSR code 如何接入 Ceph 这类分布式对象存储，并在真实 repair 流程中降低 network traffic、disk read 和 repair time。
- Coordination-free replicated datatypes 如何在 eventual consistency 下保持 strong convergence，同时控制 causality metadata、garbage collection 和 Byzantine/equivocation 边界。
- CRDT 数据上的 query/observation 如何判断是否可以 local-safe 执行，哪些 non-monotone queries 必须引入 coordination、pre-coordination 或显式 stale-read 语义。
- 内容寻址/P2P 存储如何用 CID、DHT provider routing、BitSwap、Merkle DAG/IPLD 和 IPNS 组织对象身份、发现、交换、命名和缓存，同时避免把内容完整性误当作长期可用性。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems|Distributed systems]] | `part_of` | distributed systems domain + LSM survey | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | problem/direction child | storage engine 是可复用系统层，未来能容纳 LSM、B-tree、log-structured storage、index maintenance 等来源 | LSM survey §1-§4 | active_seed |
| [[04_Knowledge/distributed-systems/data-management-and-storage/privacy-preserving-database-queries|Privacy-preserving database queries]] | problem child | query privacy 是数据管理层面对不可信数据库主机的访问/语义泄露问题，不应归入 distributed transactions | Private Aggregate Queries §I-§VIII | active_seed |
| [[04_Knowledge/distributed-systems/data-management-and-storage/erasure-coded-storage|Erasure-coded Storage]] | problem child | erasure coding 是分布式存储的低冗余容错路线，修复时需要独立处理 repair bandwidth、disk reads 和 sub-packetization tradeoff | Elastic Transformation §I-§V | active_seed |
| [[04_Knowledge/distributed-systems/data-management-and-storage/conflict-free-replicated-data-types|Conflict-free replicated data types (CRDTs)]] | problem child | CRDTs 是复制数据类型/coordination-free consistency 路线，独立处理 SEC、causality metadata、GC、non-commutative operations 和 query/observation safety | Canteen §1-§4; Keep CALM and CRDT On §3-§4 | foundation_thin |
| [[04_Knowledge/distributed-systems/data-management-and-storage/content-addressed-storage|Content-addressed Storage and Distribution]] | problem child | 内容寻址/P2P 存储是对象身份、provider discovery、块交换、Merkle object graph 和可用性生命周期的组合问题，不应误归入 consensus | IPFS原理与实践 Chapter 1-8 | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Storage engine design | 在数据库/NoSQL 系统内部组织持久化、索引、更新、恢复和查询路径 | key-value stores、database systems、distributed data systems | 需要跨 workload 和硬件做 trade-off | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] |
| Write-optimized storage | 用 out-of-place/log-structured 写入降低随机更新成本 | 写多读少、写突发、append-heavy workload | 读放大、空间放大、后台维护和延迟方差 | [[doi-10-1007-s002360050048-log-structured-merge-tree|Original LSM-tree paper]]; [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] |
| Provenance-query storage | 保留历史版本并用 ledger/transaction metadata 连接用户、交易、block 和历史行版本 | audit/compliance/supply-chain provenance | 单节点查询结果仍可能被恶意 peer 篡改；需要多节点查询或 authenticated query | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] |
| Authenticated state storage adaptation | 把 learned index、LSM-like runs、Bloom filters、Merkle files 和 checkpointed merge 迁移到需要 state root/provenance proof 的区块链状态存储 | full-node state history、authenticated indexes、blockchain provenance queries | 普通 storage-engine 优化不会自动提供 integrity、proof completeness、fork/rewind 或 state-root determinism | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] |
| Replication snapshot/log interface | storage engine 暴露 row log、snapshot creation、timestamp/MVCC 和 commit path，决定备库并发控制能否同时应用 replicated writes 和服务 prefix-consistent reads | primary-backup replicated databases with read-only backups | storage API 只提供实现接口，不自动保证 monotonic prefix consistency 或 bounded replication lag | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] |
| Privacy-preserving aggregate query processing | 用 IT-PIR、standard aggregate vectors、indexes of aggregate queries 和 polynomial batch coding 隐藏查询条件与参与聚合的记录集合 | untrusted hosted databases, multi-server threshold PIR, aggregate analytics | 不证明结果正确性/完整性；依赖非串通阈值和离线 index 维护；JOIN 仍是 future work | [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] |
| Verifiable SQL query processing | 将 SQL operator pipeline 作为 cryptographic proof object，证明 answer correctness/completeness 并隐藏私有输入和中间结果。 | untrusted/proving database owner, public schema/cardinality/query/DAG/answer, private relational data | 不隐藏 query/access pattern；不证明事务隔离、并发控制、storage layout 或 optimizer 全局正确性。 | [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] |
| Erasure-coded storage repair optimization | 用 RS/LRC/MSR/piggybacking/code transformation 等路线，在低冗余容错、repair bandwidth、disk reads 和 sub-packetization 之间取系统折中 | distributed/cloud storage repair, HDFS/OpenEC-like erasure-coded storage | 理论最小 repair bandwidth 可能因 high sub-packetization 和 non-sequential I/O 在真实系统中变慢 | [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] |
| Vector-code/MSR implementation in object storage | 修改存储系统支持 sub-chunk repair，让 MSR/vector codes 不只停留在理论 construction | Ceph-like object storage with erasure-code plugins and fractional reads | sub-chunk layout、stripe size、PG reassignment 和 fragmented reads 会影响真实收益 | [[sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code|Clay Codes]] |
| CRDT / coordination-free replicated datatype | 让 replicas 本地更新并通过 SEC 收敛，避免强一致协调路径 | eventually consistent replicated datastores, collaborative data structures, availability-first systems | causality metadata、GC、operation commutativity、Byzantine/equivocation tolerance 与 persistence/recovery 都会变成工程约束 | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] |
| CALM-based CRDT query processing | 用 monotonicity 区分可以 local-safe 执行的 CRDT queries 和需要 coordination 的 non-monotone observations | CRDT data stores, SQL/Datalog/lattice-aware query languages, threshold/positive-information reads | 不是所有 CRDT reads 都安全；set difference/absence/checkout 等 non-monotone queries 需要协调、预协调或弱一致语义 | [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] |
| Content-addressed peer-to-peer storage | 用 CID/content hash 标识对象，用 DHT/provider routing 找来源，用 BitSwap 交换块，用 Merkle DAG/IPLD 组织对象图 | distributed file/content distribution, off-chain application assets, public/private IPFS networks | CID 只绑定内容完整性；长期可用性需要 pinning、replication 或 DSN 激励 | [[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-s002360050048-log-structured-merge-tree|The Log-Structured Merge-Tree (LSM-Tree)]] | paper | 补入 storage-engine/access-method foundation: history/log index 的高插入率随机索引维护、rolling merge 和成本模型 | 1996 paper；具体现代工程系统需要后续 sources | Abstract, §1-§6 |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | paper survey | 为本方向补入 storage management/storage engine 分支，并提供 LSM-tree 作为第一个 topic | 2019 survey，不代表最新趋势 | Abstract, §1, §4 |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database: Design and Implementation of a Blockchain Relational Database]] | paper | 补充 provenance-query storage secondary signal: MVCC 历史行版本 + `pgLedger` 支持复杂审计查询 | 主路径是 blockchain execution，不是 storage engine foundation | §2, §4.2 |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE: A Column-based Learned Storage for Blockchain Systems]] | paper | 补充 authenticated state storage adaptation signal: storage-engine 技术进入区块链时必须加上 Merkle proof、state root 和 deterministic merge boundary | 主路径是 blockchain state storage，不是通用 storage-engine foundation | Abstract, §1-§8 |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5: Cloned Concurrency Control That Always Keeps Up]] | paper | 补充 replication CC secondary signal: MyRocks/RocksDB snapshot API 和 Cicada timestamp model 影响备库并发控制实现 | 主路径是 transaction-processing/replicated-database-concurrency-control，不是 storage-engine foundation | §5-§7 |
| [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries to Untrusted Databases]] | paper + artifact | 补充 privacy-preserving query processing child: 让 SUM/COUNT/MEAN/histogram 等聚合查询在不可信数据库下隐藏查询条件和参与记录集合 | 需要多服务器阈值非串通假设；不提供结果正确性证明 | Abstract, §II-§VII, Appendix B-C |
| [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization in Erasure-Coded Storage via Elastic Transformation]] | paper | 新增 erasure-coded storage child: 把纠删码低冗余容错、repair bandwidth、sub-packetization 和 non-sequential I/O 折中纳入数据管理/存储方向 | 聚焦 single lost packet/block repair；HDFS/OpenEC/HDD testbed；代码未分析 | Abstract, §II-§V |
| [[sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code|Clay Codes: Moulding MDS Codes to Yield an MSR Code]] | paper | 强化 erasure-coded storage child: 把 MSR/vector-code 构造、Ceph sub-chunk support 和真实 repair 实验纳入存储修复优化路线 | single-node evidence strongest；multi-failure savings pattern-dependent；Clay plugin 当时尚未进入 Ceph master | Abstract, §3-§5, Appendix A |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen: A Partially-Ordered Log Abstraction for the Emerging CRDT Datastore]] | paper | 新增 CRDTs child: 把 coordination-free replicated datatype、SEC、metadata GC、non-commutative operation 与 equivocation-tolerant CRDT 边界纳入本方向 | proof-of-concept simulation；venue/DOI unknown；canonical CRDT foundations 未单独吸收 | Abstract, §2-§4 |
| [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] | paper / research agenda | 补充 CRDT query/observation safety: 用 CALM monotonicity 区分 local-safe monotone queries 和需要协调的 non-monotone queries | position/research agenda；未实现完整 datastore/optimizer；CALM/query-language foundations 待补 | Abstract, §3-§4 |
| [[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] | book / local PDF | 新增 content-addressed storage child: 把 IPFS/CID/IPLD/Merkle DAG/DHT/BitSwap/IPNS/pinning 与 Filecoin 边界纳入本方向 | 2019 书籍；具体 IPFS/Filecoin 版本和当前规范需未来来源核验 | Chapters 1-8 |
| [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs]] | paper | 补充 verifiable SQL query processing secondary signal: query plans/operators 可作为证明对象 | 主路径是 ZKP applications/verifiable database queries；不代表事务、存储引擎或分布式数据库 foundation | Abstract, §3-§5 |

## 当前综合

- Evidence window: `1996` to `2026-06-24`。
- Freshness: `fresh` for hierarchy seed; not a latest-news claim.
- Valid until: `2026-07-24`。
- 综合: 当前本方向是 seed/foundation_thin。它的第一条稳定子路径是 `storage-engines -> lsm-tree-storage-engines`，且现在由原始 LSM paper 与 2019 survey 共同支撑：原始 paper 给出 high-insert-rate history/log indexing 的 access-method problem，survey 给出现代 storage-engine taxonomy。Blockchain Meets Database 新增一个 secondary route: 历史版本和 ledger metadata 如何支撑 provenance queries。COLE 进一步补充一个 cross-domain signal: 存储引擎机制可以被迁移到 blockchain state storage，但需要附加 authenticated data、proof completeness 和 deterministic state-root update。C5 又补充了 transaction-storage interaction: 备库 cloned concurrency control 的实际粒度受 snapshot/log/timestamp API 约束。Private Aggregate Queries 新增 `privacy-preserving-database-queries` 子问题，说明 query processing 还包括隐藏用户查询意图和访问集合。ZKSQL 则作为 secondary route 表明 SQL query processing 也可能被加上 cryptographic correctness/completeness proof，但其主知识路径仍是 [[verifiable-database-queries|Verifiable database queries]]，不应被误归为 distributed transactions。Elastic Transformation 与 Clay 共同支撑 `erasure-coded-storage` 子问题：distributed storage 的恢复层不仅要能容错，还要在 repair bandwidth、disk reads、sub-packetization、sub-chunk layout 和真实 repair time 之间取折中。Canteen 与 Keep CALM and CRDT On 共同支撑 `conflict-free-replicated-data-types` 子问题：数据管理还包括 coordination-free replication、SEC、causality metadata、GC、fault/equivocation boundary，以及 CRDT observations 的 monotone/non-monotone query safety。IPFS 书籍新增 `content-addressed-storage` 子问题，说明数据管理还包括用内容标识、P2P provider routing、Merkle object graph 和 pinning/replication 生命周期组织内容分发。未来还需要 B-tree、分布式数据库存储、cloud/object storage、query processing、PIR/SSE/ORAM、erasure-code foundations、canonical CRDT foundations、CALM/query-language foundations、IPFS/CID/libp2p/IPLD direct specs 与 transaction-storage interaction 等 source 扩展。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-s002360050048-log-structured-merge-tree|The Log-Structured Merge-Tree (LSM-Tree)]] | 补入 LSM 原始论文，关闭 LSM 子节点中“原始 paper 未吸收”缺口，并把 high-insert-rate history/log indexing 记录为 storage-engine workload boundary。 | 背景、方法族、代表 Sources、当前综合、关系图谱 | no | 继续补 B-tree/buffer/WAL recovery foundations |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | 新增 data-management/storage 分支，纠正 distributed-systems 之前过度 consensus-heavy 的结构 | 定义、下级结构、代表 Sources | yes | keep child path and queue foundations |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] | 增加 provenance-query storage 作为 secondary signal，不改变主层级。 | 方法族、代表 Sources、当前综合 | no | 未来若出现更多 verifiable query / provenance storage sources 再复核是否拆节点 |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] | 增加 authenticated state storage adaptation 作为 cross-domain source extension，并创建 storage engines -> blockchain state storage bridge。 | 方法族、代表 Sources、当前综合、Bridge Links | no for this node | 通过 bridge 路由到 blockchain-state-storage；后续 learned-index/MPT source 到来后复核 |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] | 增加 storage-engine snapshot/log/timestamp API 作为 replicated database concurrency control 的实现边界。 | 方法族、代表 Sources、当前综合、Bridge Links | no for this node | 通过 bridge 路由到 replicated-database-concurrency-control；后续 replication/recovery source 到来后复核 |
| [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] | 新增 privacy-preserving database queries 子问题，并纠正 distributed-transactions 分类。 | 解决的问题、下级结构、方法族、代表 Sources、当前综合、Bridge Links | yes | 通过 bridge 路由到 verifiable-database-queries；后续 PIR/SSE/ORAM source 到来后复核 |
| [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] | 新增 erasure-coded storage 子问题，并纠正 queue 中 distributed-transactions 误分。 | 解决的问题、下级结构、方法族、代表 Sources、当前综合、缺口 | yes | 后续 `Clay.pdf`、OpenEC/production storage source 到来后复核是否拆 RS/MDS、MSR、production repair 子节点 |
| [[sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code|Clay Codes]] | 补入 MSR/vector-code/Ceph sub-chunk repair 路线，并纠正 queue 中 noisy title 与 distributed-transactions 误分。 | 背景、解决的问题、方法族、代表 Sources、当前综合、缺口 | no | 后续补 RS/MDS/LRC/MSR foundation pack 与生产存储 source |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] | 新增 CRDTs 子问题，记录 SEC/CvRDT/CmRDT/delta-CRDT 背景和 Canteen partially ordered log + COG source extension。 | 背景、解决的问题、下级结构、方法族、代表 Sources、Bridge Links、缺口 | yes | 补 Shapiro/Preguiça/Delta-CRDT/collaborative editing foundations |
| [[arxiv-2210-12605v1-keep-calm-and-crdt-on|Keep CALM and CRDT On]] | 补入 CRDT query/observation safety，把 CALM monotonicity、local-safe queries 与 non-monotone coordination boundary 加入 CRDT 子问题。 | 背景、解决的问题、下级结构、方法族、代表 Sources、当前综合、缺口 | no | 补 CALM/Bloom/Datafun/CRDT query language sources；更多来源到来后再考虑独立 query-processing bridge |
| [[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] | 新增 content-addressed storage 子问题，纠正 queue 中 consensus/needs-review 误分；补 IPFS/Filecoin 边界。 | 背景、解决的问题、下级结构、方法族、代表 Sources、Bridge Links、缺口 | yes | 补 IPFS/Kubo, CID, IPLD, libp2p, Filecoin current specs |
| [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] | 新增 verifiable SQL query processing secondary signal，并纠正 queue 中 distributed-transactions 误分。 | 背景、解决的问题、方法族、代表 Sources、当前综合、缺口 | no | SQL correctness/completeness 细节保留在 [[verifiable-database-queries|Verifiable database queries]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[05_Bridges/storage-engines-to-blockchain-state-storage|Storage engines -> blockchain state storage]] | `distributed-systems/data-management-and-storage/storage-engines` -> `blockchain-systems/data-management-and-storage/blockchain-state-storage` | method_translation | layout/index/merge/filtering transfer; consensus safety, DA, fork/rewind, and state-root determinism do not transfer automatically | active_seed |
| [[05_Bridges/replicated-database-concurrency-control-to-storage-engines|Replicated database concurrency control -> storage engines]] | `distributed-systems/transaction-processing/replicated-database-concurrency-control` -> `distributed-systems/data-management-and-storage/storage-engines` | dependency, implementation_boundary | snapshot/log/timestamp API constrains backup-side cloned CC; storage engines do not themselves provide MPC or bounded lag | active_seed |
| [[05_Bridges/privacy-preserving-database-queries-to-verifiable-database-queries|Privacy-preserving database queries -> verifiable database queries]] | `distributed-systems/data-management-and-storage/privacy-preserving-database-queries` -> `zero-knowledge-proofs/applications/verifiable-database-queries` | complement, boundary | query/access privacy and answer correctness/completeness are complementary; neither automatically implies the other | active_seed |
| [[05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types|Byzantine fault tolerance -> CRDTs]] | `distributed-systems/consensus/byzantine-fault-tolerance` -> `distributed-systems/data-management-and-storage/conflict-free-replicated-data-types` | adaptation, equivocation_boundary | Byzantine/equivocation threat transfers to CRDT causal histories; BFT consensus quorum/total-order protocol does not automatically transfer to SEC. | active_seed |
| [[05_Bridges/content-addressed-storage-to-decentralized-storage-networks|Content-addressed storage -> decentralized storage networks]] | `distributed-systems/data-management-and-storage/content-addressed-storage` -> `blockchain-systems/data-management-and-storage/decentralized-storage-networks` | substrate_to_incentive_layer, boundary | CID/Merkle/P2P primitives can support DSN data commitments and retrieval, but incentives, proofs, payments and long-term availability do not transfer automatically. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-data-management-and-storage | part_of | nahida-knowledge-distributed-systems | vault/04_Knowledge/distributed-systems.md; vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | medium | active_seed |
| nahida-knowledge-data-management-and-storage | has_child | nahida-knowledge-storage-engines | vault/04_Knowledge/distributed-systems/data-management-and-storage.md; vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md | medium | active_seed |
| nahida-knowledge-data-management-and-storage | has_child | nahida-knowledge-privacy-preserving-database-queries | vault/04_Knowledge/distributed-systems/data-management-and-storage/privacy-preserving-database-queries.md; Private Aggregate Queries source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | has_child | nahida-knowledge-erasure-coded-storage | vault/04_Knowledge/distributed-systems/data-management-and-storage/erasure-coded-storage.md; Elastic Transformation source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | has_child | nahida-knowledge-conflict-free-replicated-data-types | vault/04_Knowledge/distributed-systems/data-management-and-storage/conflict-free-replicated-data-types.md; Canteen source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | has_child | nahida-knowledge-content-addressed-storage | vault/04_Knowledge/distributed-systems/data-management-and-storage/content-addressed-storage.md; IPFS source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md | original LSM-tree source note | high | active |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | high | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md | Blockchain Meets Database source note | medium | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md | COLE source note | medium | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md | C5 source note | medium | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md | Private Aggregate Queries source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md | Elastic Transformation source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code.md | Clay Codes source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md | Canteen source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/arxiv-2210-12605v1-keep-calm-and-crdt-on.md | Keep CALM and CRDT On source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md | IPFS source note | high | active_seed |
| nahida-knowledge-data-management-and-storage | evidenced_by | vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md | ZKSQL source note as verifiable query-processing boundary | medium | active_seed |
| nahida-knowledge-data-management-and-storage | bridges_to | nahida-bridge-replicated-database-concurrency-control-to-storage-engines | vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md | medium | active_seed |
| nahida-knowledge-data-management-and-storage | bridges_to | nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries | vault/05_Bridges/privacy-preserving-database-queries-to-verifiable-database-queries.md | high | active_seed |
| nahida-knowledge-data-management-and-storage | bridges_to | nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types | vault/05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types.md | medium | active_seed |
| nahida-knowledge-data-management-and-storage | bridges_to | nahida-bridge-content-addressed-storage-to-decentralized-storage-networks | vault/05_Bridges/content-addressed-storage-to-decentralized-storage-networks.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| B-tree、buffer management、recovery、query processing 与 distributed databases 的 foundation source 缺失 | 当前方向过度依赖 LSM survey 作为 seed | `nahida-research-search` or future papers | medium | queued |
| Verifiable SQL/query-processing foundations 缺更宽 source | ZKSQL 给出可验证 SQL route，但 CorrectDB/VeriDB/IntegriDB/vSQL 与普通 query-processing foundation 仍未系统吸收 | `nahida-update` or `nahida-research-search` | medium | partially_covered |
| PIR/SSE/ORAM/database-query-privacy foundations 仍缺直接 source | Private Aggregate Queries 提供应用型 seed，但父概念还需要基础论文/系统补强 | `nahida-research-search` or future papers | medium | queued |
| RS/MDS、LRC、MSR、OpenEC 和 production erasure-coded storage foundations 仍缺系统 source | Elastic Transformation 和 Clay 提供修复优化/MSR 实践入口，但不能替代整个纠删码存储基础 | `nahida-research-search` foundation_pack or future sources | high | queued |
| CRDT canonical foundation sources 缺失 | Canteen 和 Keep CALM 提供 CRDT data-store/query agenda，但 Shapiro/Preguiça/Delta-CRDT/collaborative editing、CALM/Bloom/Datafun direct sources 仍未单独吸收 | `nahida-research-search` foundation_pack or future sources | high | queued |
| IPFS/CID/IPLD/libp2p/Filecoin direct specs 缺失 | IPFS 书籍提供强中文基础入口，但具体实现和当前规范需要后续直接来源补强 | `nahida-research-search` foundation_pack or future sources | high | queued |
| 是否需要独立 `database-systems` domain 尚未判定 | 存储引擎既属于数据系统也可属于分布式系统实践 | `nahida-consolidate` after more sources | low | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-paper-intake-20260620-item-0033 | Created direction seed from LSM survey and connected it under distributed systems. | arxiv:1812.07527v3 | codex |
| 2026-06-22 | nahida-knowledge-20260622-blockchain-meets-database | Added secondary provenance-query storage signal from blockchain relational database. | arxiv:1903.01919v2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-cole-blockchain-storage | Added blockchain authenticated state-storage adaptation signal and bridge to blockchain state storage. | arxiv:2306.10739v1 | codex |
| 2026-06-23 | nahida-knowledge-20260623-c5-cloned-concurrency-control | Added storage-engine snapshot/log/timestamp API as a secondary implementation boundary for replicated database concurrency control. | arxiv:2207.02746 | codex |
| 2026-06-23 | nahida-knowledge-20260623-private-aggregate-queries | Added privacy-preserving database queries as a child problem and linked it to verifiable database query boundaries. | doi:10.5281/zenodo.10225325 | codex |
| 2026-06-23 | nahida-knowledge-20260623-elastic-transformation-erasure-coded-storage | Added erasure-coded storage as a child problem and corrected the source away from distributed transactions. | doi:10.1109/INFOCOM53939.2023.10228984 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-clay-codes | Added Clay Codes as MSR/vector-code/Ceph repair evidence under erasure-coded storage and corrected noisy queue metadata. | usenix:fast18-vajha; sha256:b04fe9944676db0a3a6da4091a54d6c57bce7ebee6f8058c4077c1b59e14880a | codex |
| 2026-06-23 | nahida-paper-intake-20260623-canteen-crdt-datastore | Added CRDTs as a child problem and Canteen as partially-ordered-log/COG source extension, with BFT/equivocation bridge. | sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84 | codex |
| 2026-06-24 | nahida-knowledge-20260624-keep-calm-crdt-query-model | Added CRDT query-safety route, CALM-based monotone query model, and non-monotone coordination/stale-read boundary. | arxiv:2210.12605v1 | codex |
| 2026-06-23 | nahida-knowledge-20260623-ipfs-principles-and-practice | Added content-addressed storage as a child problem and linked it to decentralized storage networks. | isbn:978-7-111-62880-4 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-lsm-tree | Added the original LSM-tree paper as foundational storage-engine/access-method evidence. | doi:10.1007/s002360050048 | codex |
| 2026-06-23 | nahida-knowledge-20260623-zksql | Added ZKSQL as secondary verifiable SQL query-processing signal and corrected classification away from distributed transactions. | doi:10.14778/3594512.3594513 | codex |
