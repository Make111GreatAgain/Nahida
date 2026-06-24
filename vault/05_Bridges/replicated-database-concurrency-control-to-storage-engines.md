---
id: "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
title: "Replicated database concurrency control -> storage engines"
original_title: "Replicated database concurrency control -> storage engines"
file_slug: "replicated-database-concurrency-control-to-storage-engines"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "intra_domain_dependency"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/transaction-processing/replicated-database-concurrency-control"
  - "distributed-systems/data-management-and-storage/storage-engines"
endpoint_knowledge_refs:
  - "nahida-knowledge-replicated-database-concurrency-control"
  - "nahida-knowledge-storage-engines"
from_domain: "distributed-systems"
to_domain: "distributed-systems"
from_direction: "transaction-processing"
to_direction: "data-management-and-storage"
from_topic: "replicated-database-concurrency-control"
to_topic: "storage-engines"
relation_types:
  - "dependency"
  - "implementation_boundary"
  - "interface_constraint"
directionality: "one_way_with_feedback"
relationship_thesis: "Backup-side replicated database concurrency control depends on storage-engine interfaces: row-level log identity, snapshot creation, timestamp visibility, and commit ordering determine whether a cloned-concurrency-control protocol can expose prefix-consistent read snapshots while applying replicated writes fast enough to bound lag."
transferability: "high_within_database_replication"
non_transfer_boundary: "Storage-engine snapshots, logs, MVCC versions, or timestamps can support cloned concurrency control, but they do not by themselves provide monotonic prefix consistency, bounded replication lag, primary log delivery, failover policy, or application-level invariant preservation. Conversely, a cloned CC protocol may be theoretically row-granular but still become coarser when the storage engine exposes only transaction- or current-state snapshot APIs."
evidence_window_start: "2022"
evidence_window_end: "2026-06-23"
domains:
  - "distributed-systems"
topics:
  - "replicated database concurrency control"
  - "storage engines"
  - "primary-backup replication"
  - "snapshot API"
  - "MVCC timestamps"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
knowledge_refs:
  - "nahida-knowledge-replicated-database-concurrency-control"
  - "nahida-knowledge-storage-engines"
relation_edges:
  - from: "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
    relation: "connects"
    to: "nahida-knowledge-replicated-database-concurrency-control"
    evidence_refs:
      - "vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
    relation: "connects"
    to: "nahida-knowledge-storage-engines"
    evidence_refs:
      - "vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    confidence: "high"
    status: "active_seed"
query_keys:
  - "C5 MyRocks snapshot API"
  - "storage engine snapshot cloned concurrency control"
  - "primary backup replication storage engine"
  - "Cicada timestamp C5"
  - "RocksDB snapshot replication lag"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-c5-cloned-concurrency-control"
source_refs:
  - "arxiv:2207.02746"
confidence: "medium"
trust_tier: "primary"
---

# Replicated database concurrency control -> storage engines

## 命名与路径

- Original title: Replicated database concurrency control -> storage engines
- File slug: `replicated-database-concurrency-control-to-storage-engines`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

[[04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control|Replicated database concurrency control]] 关注备库如何应用 primary log、控制并发并服务 read-only transactions。[[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] 关注底层数据布局、log、snapshot、timestamp/MVCC、commit 和恢复接口。

这条 bridge 记录的不是“存储引擎等于复制协议”，而是一个实现边界: cloned concurrency control 的理论粒度和正确性目标，必须通过 storage-engine 暴露的 row identity、snapshot、timestamp 和 commit API 落地。接口越粗，备库协议越可能被迫回到 transaction/page/current-state 粒度。

## 连接命题

- From: `distributed-systems/transaction-processing/replicated-database-concurrency-control`
- To: `distributed-systems/data-management-and-storage/storage-engines`
- Relation types: dependency, implementation_boundary, interface_constraint
- Directionality: `one_way_with_feedback`
- Relationship thesis: Backup-side replicated database concurrency control depends on storage-engine interfaces: row-level log identity, snapshot creation, timestamp visibility, and commit ordering determine whether a cloned-concurrency-control protocol can expose prefix-consistent read snapshots while applying replicated writes fast enough to bound lag.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control|Replicated database concurrency control]] | `distributed-systems/transaction-processing/replicated-database-concurrency-control` | cloned CC, monotonic prefix consistency, bounded replication lag, row-granularity backup scheduling | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] | active_seed |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | `distributed-systems/data-management-and-storage/storage-engines` | snapshot API, row log format, MVCC/timestamp visibility, write commit path | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Row identity in replicated log | per-row FIFO scheduling for cloned CC | C5 scheduler | Requires log records to identify row-level writes. |
| Snapshot API | current/next/future prefix exposure | C5 snapshotter and C5-MyRocks | If the engine only exposes current read-only snapshots, ideal C5 must add blocking or coarser constraints. |
| MVCC timestamp model | logical prefix snapshots without physical snapshot copies | C5-Cicada | Prototype lacks full network/logging/persistence, so it is interface evidence rather than production evidence. |
| Commit-order worker constraints | compatibility with existing logging assumptions | C5-MyRocks | One-thread-per-transaction weakens ideal row-granularity because of MyRocks log assumptions. |

## 迁移矩阵

| Storage-engine mechanism | CC mechanism enabled/constrained | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- |
| Row-based primary log | row-granularity cloned CC | Scheduler builds per-row FIFO queues from log records. | C5 §5 | If log groups writes only by transaction or page, backup loses necessary granularity. |
| RocksDB current snapshots | prefix read exposure | C5-MyRocks uses current snapshot + database as next. | C5 §6 | Creating snapshot boundary can block future writes beyond `n`. |
| Cicada timestamps/MVCC | logical current/next/future snapshots | Snapshotter advances `c` and `n` using timestamps rather than physical snapshot merging. | C5 §7 | Prototype emulates replication on one server. |
| Storage worker commit path | safe-write execution | Workers apply safe writes while read-only transactions use a stable snapshot. | C5 §5-§7 | Read load can contend for spare cycles; worker priority matters. |

## 类比、依赖或关系边界

C5 的两个实现给出清晰对照。MyRocks/RocksDB 的 production constraints 让 ideal C5 必须降级: 同一事务 writes 由同一 worker 执行，snapshotter 需要在选择 `n` 后阻止更后面的 writes commit。Cicada 的 timestamp/MVCC 接口则让 snapshotter 的 current/next/future 边界更自然，说明 storage-engine interface 能决定 replicated CC 的实际并行度。

这条 bridge 不把 C5 变成 storage-engine source。C5 的主贡献仍是 transaction-processing / backup concurrency control；storage-engine 只作为实现约束端点出现。

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5: Cloned Concurrency Control That Always Keeps Up]] | Direct evidence that MyRocks/RocksDB snapshots and Cicada timestamp/MVCC interfaces constrain or enable backup-side cloned CC. | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/transaction-processing/replicated-database-concurrency-control` | Created as new problem node with bridge link and C5 as representative source. | active_seed |
| `distributed-systems/data-management-and-storage/storage-engines` | Add source extension for snapshot/log/timestamp API as transaction-processing dependency. | active_seed |

## 查询入口

- C5 为什么需要 storage-engine snapshot API?
- MyRocks 版本的 C5 为什么不完全等于理想 C5?
- Cicada 的 timestamp model 如何帮助 cloned concurrency control?
- 备库复制协议如何受 RocksDB snapshot 限制?
- replication lag 和 storage engine interface 有什么关系?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: direct sources on KuaFu, Query Fresh, MySQL parallel replication, RocksDB/MyRocks replication internals, Cicada/MVCC replication, or database recovery foundations.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control|Replicated database concurrency control]] | all sections | C5 creates the problem node. | active_seed |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | methods, representative sources, bridge links | C5 adds storage-engine API as a replication CC implementation boundary. | active_seed |
| [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | child nodes, methods, representative sources | C5 adds non-blockchain database replication evidence. | active_seed |

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: new source changes either endpoint, relation type, transfer boundary, or maturity.

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-c5-cloned-concurrency-control | Created bridge from C5 implementation evidence. | arxiv:2207.02746 | codex |
