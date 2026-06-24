---
id: "nahida-knowledge-storage-engines"
title: "Storage Engines"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "storage-engines"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "storage-engines"
parent_knowledge_refs:
  - "nahida-knowledge-data-management-and-storage"
child_knowledge_refs:
  - "nahida-knowledge-lsm-tree-storage-engines"
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "storage-engines"
primary_ontology_path: "distributed-systems/data-management-and-storage/storage-engines"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-storage-engines"
    relation: "part_of"
    to: "nahida-knowledge-data-management-and-storage"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-storage-engines"
    relation: "has_child"
    to: "nahida-knowledge-lsm-tree-storage-engines"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md"
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-storage-engines"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-storage-engines"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
    confidence: "high"
    status: "active"
  - from: "nahida-knowledge-storage-engines"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-storage-engines"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-storage-engines"
    relation: "bridges_to"
    to: "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
    evidence_refs:
      - "vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "vault/05_Bridges/storage-engines-to-blockchain-state-storage.md"
  - "vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
  - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
  - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
  - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
representative_source_refs:
  - "doi:10.1007/s002360050048"
  - "arxiv:1812.07527v3"
  - "arxiv:2306.10739v1"
  - "arxiv:2207.02746"
query_keys:
  - "storage engine"
  - "storage engines"
  - "database storage engine"
  - "NoSQL storage engine"
  - "存储引擎"
  - "deferred index maintenance"
  - "history table index"
  - "rolling merge"
  - "blockchain state storage engine"
  - "authenticated state index"
  - "learned index blockchain"
  - "snapshot API"
  - "MVCC timestamp storage engine"
  - "replication concurrency control storage engine"
aliases:
  - "存储引擎"
  - "Database storage engines"
domains:
  - "distributed-systems"
topics:
  - "storage engines"
  - "deferred index maintenance"
  - "history table indexing"
  - "authenticated state storage"
  - "blockchain storage"
  - "replication snapshot API"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-20"
evidence_window_start: "1996"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260620-item-0033"
  - "nahida-knowledge-20260622-cole-blockchain-storage"
  - "nahida-knowledge-20260623-c5-cloned-concurrency-control"
  - "nahida-paper-intake-20260623-lsm-tree"
source_refs:
  - "doi:10.1007/s002360050048"
  - "sha256:8fe1d3206fe8eb151e9d8c54e0772a46786e2ec40e4c2b7782995067d6b938c6"
  - "arxiv:1812.07527v3"
  - "arxiv:2306.10739v1"
  - "arxiv:2207.02746"
confidence: "medium"
trust_tier: "primary"
---

# Storage Engines

## 定义与范围

- 定义: 存储引擎（storage engine）是数据库、NoSQL 系统或 key-value store 中负责持久化数据布局、索引、写入路径、读取路径、恢复和后台维护的系统层。它不是某一个数据库产品，而是一组可以由不同数据结构和策略实现的核心系统问题。
- 不包含: 上层 SQL 优化器、完整事务协议、共识协议或某个具体产品的全部架构；这些可通过 bridge 或父/邻节点连接。
- Canonical terms: `storage engine`, `database storage engine`, `NoSQL storage engine`
- Standalone completeness check: 本节点给出存储引擎问题边界、主要权衡和当前 child `LSM-tree Storage Engines`；更细 LSM 机制在子节点。
- Retrieval role: 作为“存储层怎么解决写读空间恢复问题”的入口，避免 query 直接落入一篇 LSM survey。
- Update scope: B-tree、LSM-tree、append-only/value-log、secondary indexing、recovery、buffer/cache、cloud storage placement 等 source 均可挂到这里。

## 背景

model_prior_background: 存储引擎通常处在查询/事务层之下，直接面对磁盘/SSD/NVM、内存缓冲、索引结构、日志、恢复和后台维护。[[doi-10-1007-s002360050048-log-structured-merge-tree|原始 LSM-tree 论文]] 为当前 vault 提供 source-backed 的第一条 access-method foundation: 当 history table / transaction log 的 secondary index 是随机 key、高插入率、低查询频率时，B-tree 立即定位会把插入变成昂贵随机 I/O；LSM 用内存 `C0`、磁盘 `C1..CK` 和 rolling merge 延迟最终定位。LSM survey 将这条原始路线扩展为现代 LSM storage-engine taxonomy。COLE 作为 source extension 表明这些机制迁移到区块链状态存储时，还必须处理 integrity/provenance proofs 和 state-root determinism。C5 作为 secondary source extension 表明，storage-engine 的 snapshot/log/timestamp API 还会反过来限制上层 replicated database concurrency control 的实现粒度。

## 解决的问题

- 写入如何落盘，同时保持崩溃恢复能力。
- 点查和范围查如何通过索引、过滤器和组件元数据降低 I/O。
- 更新、删除和旧版本如何清理。
- 后台维护如何控制 write amplification、read amplification、space amplification 和 latency variance。
- 存储结构如何适配 workload、硬件和分布式部署。
- 存储引擎向事务/复制层暴露的 snapshot、log、timestamp 和 commit API 如何影响上层协议。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | `part_of` | LSM survey §1/§4 | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines|LSM-tree Storage Engines]] | method family/topic | LSM-tree 是已由 deep-read survey 支撑的可复用存储引擎方法族 | LSM survey §2-§5 | active |
| B-tree-like storage engines | candidate | 与 LSM 形成常见对照，需要 source 支撑后再建 | model_prior_background + LSM survey contrast | queued |
| Secondary index maintenance | candidate/application axis | LSM survey §3.7 有较多材料，但更像跨 engine 的索引维护问题 | LSM survey §3.7 | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| In-place update indexes | 直接在原位置更新或维护主结构 | 读优化、点查/范围查稳定的系统 | 随机写、碎片和更新成本 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §2.1 |
| Out-of-place/log-structured storage | 写入新位置，后续通过 merge/GC 维护 | 写密集、顺序 I/O 优先 | 读放大、空间放大、后台维护 | [[doi-10-1007-s002360050048-log-structured-merge-tree|Original LSM paper]] §2-§3; [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §2 |
| Deferred index maintenance | 新 index entry 先进入内存组件，再批量 merge 到磁盘组件，避免随机 B-tree leaf update | history/log index、append-heavy secondary indexes | immediate find 可能更贵；需要 checkpoint/recovery 支撑 | [[doi-10-1007-s002360050048-log-structured-merge-tree|Original LSM paper]] §1-§4 |
| Hybrid/tunable storage engines | 通过参数、策略或 workload adaptation 调节 read/write/space | workload 变化或云硬件差异明显 | 调参复杂，评估必须使用 tuned baseline | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §3.6/§5 |
| Authenticated storage-engine adaptation | 将 column layout、learned index、Bloom filters、LSM-like runs 和 Merkle files 组合到需要可验证 state root 的系统中 | blockchain full-node state storage、auditable/provenance storage | 普通索引和 compaction 不能自动提供证明完整性、抗篡改或确定性 digest 更新 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] |
| Replication-facing snapshot/log API | 将 row-level log identity、snapshot creation、timestamp/MVCC visibility 和 commit path 暴露给备库并发控制 | primary-backup databases whose backups serve read-only transactions | API 约束可能迫使理论上 row-granular 的协议降级为 transaction/current-state 粒度 | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-s002360050048-log-structured-merge-tree|The Log-Structured Merge-Tree (LSM-Tree)]] | paper | 给出写密集 history/log index 的原始 LSM access method、rolling merge、成本模型、并发/恢复 sketch | 成本模型基于 1990s disk/memory；不是现代 LSM implementation survey | Abstract, §1-§6 |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | paper survey | 将 LSM-tree 作为存储引擎方法族，解释成本模型和工程系统 | 只覆盖 LSM-based 技术，不是完整 storage engine textbook | §2-§5 |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE: A Column-based Learned Storage for Blockchain Systems]] | paper | 展示 storage-engine mechanisms 在 blockchain authenticated state storage 中的适配边界：learned index 定位、Merkle file 认证、checkpoint merge 保持 state-root determinism | 主路径在 blockchain-state-storage；不是通用 storage-engine survey | §3-§8 |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5: Cloned Concurrency Control That Always Keeps Up]] | paper | 展示 storage-engine snapshot/log/timestamp API 如何约束备库 cloned concurrency control 的工程实现 | 主路径在 replicated-database-concurrency-control；不是通用 storage-engine survey | §5-§7 |

## 当前综合

- Evidence window: `1996` to `2026-06-23`
- Freshness: `fresh` for seed hierarchy; not current industrial state.
- Valid until: `2026-07-20`
- 综合: 当前本节点以 LSM-tree 为第一条 source-backed 方法族。原始 LSM paper 说明 storage engine/access method 的一个核心问题轴是高插入率 index maintenance: 写入不是只要持久化，还要避免 secondary index 的随机 I/O 成本。LSM survey 把这个轴扩展成现代 write/read/space amplification、recovery、index maintenance 和 background maintenance 设计空间。COLE 新增了一个跨域适配信号: 当 storage-engine 机制用于 blockchain state storage 时，必须把 layout/index/merge 与 Merkle proof、state root 和 deterministic checkpoint 绑定。C5 新增了一个 transaction-storage interaction 信号: 当备库需要同时追 log 和服务 read-only transactions 时，storage engine 的 snapshot/log/timestamp API 会决定 cloned concurrency control 的实际可行粒度。需要后续 source 让 B-tree、buffer/cache、recovery、cloud/object storage、replication-facing storage interface 等路线不再只依赖 model_prior_background。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-s002360050048-log-structured-merge-tree|The Log-Structured Merge-Tree (LSM-Tree)]] | 补入 high-insert-rate history/log index 和 deferred index maintenance 作为 storage-engine 问题轴；原始 LSM 细节留在子节点和 source note | 背景、方法族、代表 Sources、当前综合 | no | 继续补 B-tree/buffer/WAL recovery foundations |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | 补入 storage engine 问题轴与 LSM-tree child | 定义、方法族、下级结构 | yes | use as representative source |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] | 补入 storage-engine mechanisms 的 blockchain authenticated-state adaptation，并连接 bridge | 方法族、代表 Sources、当前综合、Bridge Links | no | keep source details in blockchain-state-storage and bridge |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] | 补入 storage-engine snapshot/log/timestamp API 对 replicated database CC 的实现约束，并连接 bridge | 方法族、代表 Sources、当前综合、Bridge Links | no | keep source details in replicated-database-concurrency-control and bridge |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[05_Bridges/storage-engines-to-blockchain-state-storage|Storage engines -> blockchain state storage]] | `distributed-systems/data-management-and-storage/storage-engines` -> `blockchain-systems/data-management-and-storage/blockchain-state-storage` | method_translation | storage-engine layout/index/merge/filtering can transfer only with added integrity/provenance/state-root constraints | active_seed |
| [[05_Bridges/replicated-database-concurrency-control-to-storage-engines|Replicated database concurrency control -> storage engines]] | `distributed-systems/transaction-processing/replicated-database-concurrency-control` -> `distributed-systems/data-management-and-storage/storage-engines` | dependency, implementation_boundary | snapshot/log/timestamp API constrains backup-side cloned CC; storage engines do not themselves provide MPC or bounded lag | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-storage-engines | part_of | nahida-knowledge-data-management-and-storage | vault/04_Knowledge/distributed-systems/data-management-and-storage.md; vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | medium | active_seed |
| nahida-knowledge-storage-engines | has_child | nahida-knowledge-lsm-tree-storage-engines | vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md; vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines.md | high | active_seed |
| nahida-knowledge-storage-engines | evidenced_by | vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md | original LSM-tree source note | high | active |
| nahida-knowledge-storage-engines | evidenced_by | vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | high | active_seed |
| nahida-knowledge-storage-engines | evidenced_by | vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md | COLE source note | medium | active_seed |
| nahida-knowledge-storage-engines | evidenced_by | vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md | C5 source note | medium | active_seed |
| nahida-knowledge-storage-engines | bridges_to | nahida-bridge-replicated-database-concurrency-control-to-storage-engines | vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| B-tree / buffer manager / WAL recovery foundation source 缺失 | 需要和 LSM 路线形成真正对照 | `nahida-research-search` / future papers | medium | queued |
| 二级索引维护是否拆独立节点 | LSM survey 中材料丰富，但当前只有一篇 survey | `nahida-consolidate` after more sources | low | review |
| replication-facing snapshot/log/timestamp interface source 缺失 | C5 只给出 MyRocks/RocksDB 和 Cicada 对照，仍缺更完整 recovery/replication/storage API 谱系 | `nahida-research-search` / future papers | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-paper-intake-20260620-item-0033 | Created storage-engine seed node and attached LSM survey as first representative source. | arxiv:1812.07527v3 | codex |
| 2026-06-22 | nahida-knowledge-20260622-cole-blockchain-storage | Added blockchain authenticated-state-storage adaptation as a source extension and bridge. | arxiv:2306.10739v1 | codex |
| 2026-06-23 | nahida-knowledge-20260623-c5-cloned-concurrency-control | Added replication-facing snapshot/log/timestamp API as a source extension and bridge. | arxiv:2207.02746 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-lsm-tree | Added original LSM-tree paper as foundational storage-engine/access-method evidence. | doi:10.1007/s002360050048 | codex |
