---
id: "nahida-bridge-storage-engines-to-blockchain-state-storage"
title: "Storage engines -> blockchain state storage"
original_title: "Storage engines -> blockchain state storage"
file_slug: "storage-engines-to-blockchain-state-storage"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_domain_method_translation"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/data-management-and-storage/storage-engines"
  - "blockchain-systems/data-management-and-storage/blockchain-state-storage"
endpoint_knowledge_refs:
  - "nahida-knowledge-storage-engines"
  - "nahida-knowledge-blockchain-state-storage"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "data-management-and-storage"
to_direction: "data-management-and-storage"
from_topic: "storage-engines"
to_topic: "blockchain-state-storage"
relation_types:
  - "method_translation"
  - "implementation_reuse"
  - "integrity_boundary"
  - "determinism_boundary"
directionality: "one_way_with_feedback"
relationship_thesis: "Storage-engine mechanisms such as column-oriented layout, learned indexes, Bloom filters, LSM-style immutable runs, and asynchronous merge scheduling can reduce blockchain full-node state-storage overhead, but they become valid blockchain state-storage mechanisms only after integrity proofs, provenance completeness, and deterministic state-root updates are added."
transferability: "high_for_layout_indexing_and_merge_patterns_medium_for_integrity_semantics"
non_transfer_boundary: "Learned indexes, LSM merge, Bloom filters, and disk layout optimizations do not by themselves provide blockchain consensus safety, data availability, fork/rewind handling, authenticated query completeness, or state-root determinism. In COLE, learned models locate data but are not authenticated; Merkle files and root_hash_list provide integrity, and checkpointed merge is required so nodes do not commit different root digests at the same block height."
evidence_window_start: "2019"
evidence_window_end: "2023"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "storage engines"
  - "blockchain state storage"
  - "LSM-tree"
  - "learned indexes"
  - "authenticated indexes"
  - "provenance queries"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
  - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
knowledge_refs:
  - "nahida-knowledge-storage-engines"
  - "nahida-knowledge-lsm-tree-storage-engines"
  - "nahida-knowledge-blockchain-data-management-and-storage"
  - "nahida-knowledge-blockchain-state-storage"
query_keys:
  - "storage engines blockchain state storage"
  - "LSM blockchain storage"
  - "learned indexes blockchain state"
  - "COLE blockchain storage"
  - "authenticated state storage learned index"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-cole-blockchain-storage"
source_refs:
  - "arxiv:1812.07527v3"
  - "arxiv:2306.10739v1"
confidence: "high"
trust_tier: "primary"
---

# Storage engines -> blockchain state storage

## 命名与路径

- Original title: Storage engines -> blockchain state storage
- File slug: `storage-engines-to-blockchain-state-storage`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

`distributed-systems/data-management-and-storage/storage-engines` 关注数据如何落盘、索引、更新、查询、恢复和后台维护。`blockchain-systems/data-management-and-storage/blockchain-state-storage` 关注区块链全节点如何保存状态和历史版本，并通过 state root、Merkle proofs 和 provenance proofs 保持可验证性。

这条 bridge 的命题很窄: 存储引擎的 layout/index/merge 技术可以迁移到 blockchain state storage，但必须补上区块链特有的 integrity、provenance 和 deterministic root-digest 边界。

## 连接命题

- From: `distributed-systems/data-management-and-storage/storage-engines`
- To: `blockchain-systems/data-management-and-storage/blockchain-state-storage`
- Relation types: method_translation, implementation_reuse, integrity_boundary, determinism_boundary
- Directionality: `one_way_with_feedback`
- Relationship thesis: Storage-engine mechanisms such as column-oriented layout, learned indexes, Bloom filters, LSM-style immutable runs, and asynchronous merge scheduling can reduce blockchain full-node state-storage overhead, but they become valid blockchain state-storage mechanisms only after integrity proofs, provenance completeness, and deterministic state-root updates are added.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | `distributed-systems/data-management-and-storage/storage-engines` | layout, indexes, filters, immutable runs, merge/compaction, write/read/space tradeoffs | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]]; [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] | `blockchain-systems/data-management-and-storage/blockchain-state-storage` | state history, authenticated indexes, state root digest, provenance query, proof completeness | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Column-oriented/history-aware layout | group one account/state key's historical versions by compound key `<addr, blk>` | COLE §3-§4 | Layout helps provenance queries but does not itself authenticate completeness. |
| Learned index / PGM-like model | locate records in on-disk sorted value files | COLE §4.3 | Model corruption affects lookup/performance; integrity must come from Merkle files. |
| LSM-style immutable runs | manage writes as L0 memory tree plus on-disk levels | COLE §3-§4; LSM survey | Ordinary LSM merge can change structure asynchronously; blockchain needs checkpointed root updates. |
| Bloom-filter-assisted lookup | skip runs that cannot contain an address | COLE §4.2 | Bloom filters are included with digest/proof material but can have false positives. |
| Merkle tree over value files | authenticate data records located by the index | COLE §4.4 | Merkle file proves value-file records, not consensus validity or DA. |
| Async merge scheduling | reduce long-tail write latency | COLE §5; LSM survey merge-scheduling background | In blockchain, async merge must wait at commit checkpoint and update root_hash_list synchronously. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Immutable sorted runs | storage engines / LSM-tree | blockchain state storage | L0 MB-tree flushes to sorted value/index/Merkle run files | COLE §3-§4 | 多 run state root 需要 root_hash_list 组合，而不是单个 trie root |
| Learned index positioning | storage engines / learned indexes | blockchain state index | 用误差有界模型预测 value-file position，再读相邻页验证 | COLE §4.3 | learned model 不认证，必须依赖 Merkle proof |
| Merge/compaction scheduling | LSM-tree storage engines | blockchain state storage write path | 用 writing/merging group 和 checkpoints 控制后台 merge | COLE §5 | 不同步 root updates 会让节点在同一高度看到不同 digest |
| Range/provenance scan | storage/query layout | state history proof | 用 compound key boundary proof 验证区间完整性 | COLE §6 | 小区间 proof size 可能因 Merkle path sharing 不足而偏大 |

## 类比、依赖或关系边界

普通 storage engine 的目标通常是吞吐、延迟、空间和恢复；blockchain state storage 多了 state root 和 adversarial verification。COLE 的重要边界是把“定位”和“证明”分开: learned index 只加速定位，Merkle file 认证 data，root_hash_list 承诺当前有效 runs，checkpointed merge 让节点间的 digest 更新保持确定性。

因此，这条 bridge 不表示“LSM-tree 天然适合区块链”，而是表示存储引擎机制在经过 authenticated-state adaptation 后可以成为区块链状态存储路线。

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | background evidence for LSM-like storage-engine tradeoffs and merge scheduling vocabulary | active_seed |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE: A Column-based Learned Storage for Blockchain Systems]] | direct evidence for adapting storage-engine mechanisms to authenticated blockchain state storage | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/data-management-and-storage/storage-engines` | add bridge link and source extension for blockchain-specific integrity/determinism adaptation | active_seed |
| `distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines` | add source extension for LSM-like run/merge/checkpoint adaptation | active_seed |
| `blockchain-systems/data-management-and-storage` | new direction from COLE | active_seed |
| `blockchain-systems/data-management-and-storage/blockchain-state-storage` | new problem node from COLE | active_seed |

## 查询入口

- storage engine 技术如何迁移到区块链状态存储?
- COLE 为什么需要 Merkle file，而不能只用 learned index?
- LSM-style async merge 在 blockchain state root 下为什么要 checkpoint?
- MPT 和 column-based state storage 的区别是什么?
- Provenance query 如何证明区间内没有漏掉历史状态?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: 后续读取 PGM/LIPP/ALEX、MPT/Verkle/ForkBase/stateless/state-pruning source，或 COLE artifact repo 后，复核 endpoint、non-transfer boundary 和 transferability。

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | Bridge Links, Source Extensions | COLE shows storage-engine mechanisms under blockchain integrity/determinism boundary | active_seed |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines|LSM-tree Storage Engines]] | Source Extensions | COLE specializes LSM-like runs and merge scheduling for blockchain state roots | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain Data Management and Storage]] | new direction | Adds blockchain storage layer under blockchain systems | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] | new problem | Adds state storage/authenticated index/provenance query problem | active_seed |

## 刷新规则

- Last checked: `2026-06-22`
- Valid until: `2026-07-22`
- Refresh triggers: new source changes either endpoint, relation type, transfer boundary, learned-index status, MPT/Verkle comparison, or fork/rewind/state-pruning assumptions。

