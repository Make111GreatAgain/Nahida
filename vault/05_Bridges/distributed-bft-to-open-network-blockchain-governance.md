---
id: "nahida-bridge-distributed-bft-to-open-network-blockchain-governance"
title: "Distributed BFT -> open-network blockchain governance"
original_title: "Distributed BFT -> open-network blockchain governance"
file_slug: "distributed-bft-to-open-network-blockchain-governance"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active"
hierarchy_level: "bridge"
bridge_kind: "cross_path"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
  - "blockchain-systems/consensus/open-network-bft-governance"
endpoint_knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-open-network-bft-governance"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "consensus"
to_direction: "consensus"
from_topic: "byzantine-fault-tolerance"
to_topic: "open-network-bft-governance"
relation_types:
  - "translation"
  - "application"
  - "tension"
directionality: "one_way"
relationship_thesis: "Cobalt translates BFT broadcast/agreement primitives into blockchain governance under non-uniform local trust, trading global participant agreement for essential-subset configuration and local consistency."
transferability: "medium"
non_transfer_boundary: "Classical BFT agreement/reliable-broadcast reasoning transfers only after adapting quorums to local UNL/essential-subset support; governance Full-Knowledge, transaction-network delegation, randomizing-key CRS, and operator trust configuration are blockchain/open-network-specific."
evidence_window_start: "1982"
evidence_window_end: "2018"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "byzantine-fault-tolerance"
  - "open-network-bft-governance"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
  - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
  - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-open-network-bft-governance"
query_keys:
  - "BFT to open-network governance"
  - "Cobalt essential subsets Byzantine agreement"
  - "UNL consensus local consistency"
created: "2026-06-11"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
source_refs:
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "arxiv:1802.07240"
confidence: "medium"
trust_tier: "primary"
---

# Distributed BFT -> open-network blockchain governance

## 命名与路径

- Original title: Distributed BFT -> open-network blockchain governance
- File slug: `distributed-bft-to-open-network-blockchain-governance`
- Path safety check: migrated to `05_Bridges/distributed-bft-to-open-network-blockchain-governance.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/distributed-bft-to-open-network-blockchain-governance.md` 迁移而来。端点 knowledge refs 为: nahida-knowledge-byzantine-fault-tolerance, nahida-knowledge-open-network-bft-governance。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: Distributed BFT -> open-network blockchain governance

## 连接命题

- From: `distributed-systems/consensus/byzantine-fault-tolerance`
- To: `blockchain-systems/consensus/open-network-bft-governance`
- Relation types: application, translation, tension
- Directionality: one_way
- Relationship thesis: Cobalt translates BFT broadcast/agreement primitives into blockchain governance under non-uniform local trust, trading global participant agreement for essential-subset configuration and local consistency.

## 端点范围

| Endpoint | Path | Scope in bridge | Evidence | Notes |
| --- | --- | --- | --- | --- |
| Distributed BFT | `distributed-systems/consensus/byzantine-fault-tolerance` | arbitrary faults, quorum intersection, reliable broadcast, Byzantine agreement, state-machine replication | Byzantine Generals, PBFT seeds | foundation_thin |
| Open-network governance | `blockchain-systems/consensus/open-network-bft-governance` | no global membership, UNL/essential subsets, democratic atomic broadcast, governance amendments | Cobalt p1-p49 | source-backed seed |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | Evidence | 风险 |
| --- | --- | --- | --- | --- | --- |
| Quorum intersection intuition | BFT | Cobalt essential subsets | one global quorum becomes per-node `tS/qS` support over essential subsets | Cobalt §2, §4 | thresholds are local and operator-configured |
| Reliable broadcast | BFT/RBC family | DRBC | Bracha-style INIT/ECHO/READY becomes weak/strong support and support/opposition | Cobalt §4.2 | Bracha source not directly absorbed yet |
| Async binary agreement | BFT/ABBA family | Cobalt ABBA | Mostefaoui-style ABBA gains FINISH/CONF and CRS assumptions | Cobalt §4.3 | Mostefaoui/common coin sources missing |
| Atomic broadcast | distributed systems | DABC governance | ordering values becomes ratifying amendments with activation times and Full-Knowledge | Cobalt §2, §4.5 | governance semantics are not generic transaction ordering |
| View change | PBFT | transaction-network delegation | Cobalt Appendix A uses PBFT-like view change to preserve accepted transaction batches across views | Cobalt Appendix A | proof omitted by paper; implementation evidence needed |

## 不可迁移边界

- Classical complete-network BFT assumes a known participant set; Cobalt explicitly removes that assumption.
- Cobalt's liveness depends on strong connectivity/unblocked nodes and CRS, not only pairwise local consistency.
- Governance amendments need Full-Knowledge and activation times; ordinary transaction ordering usually does not.
- Transaction-network delegation introduces system architecture assumptions outside classical BFT: Cobalt nodes validate transactions, views are governed by amendments, and fallback Cobalt ordering is slow.
- Randomizing-key CRS and AVSS setup are extra cryptographic/system assumptions.

## 路径传播

| Endpoint path | Pack update | Relation/index update | Synthesis action | Status |
| --- | --- | --- | --- | --- |
| `distributed-systems/consensus/byzantine-fault-tolerance` | Add Cobalt as open-network BFT application/source extension | bridge row indexed | BFT topic synthesis refreshed with Cobalt extension | active_seed |
| `blockchain-systems/consensus/open-network-bft-governance` | Create topic map/synthesis and Cobalt concepts | relation rows indexed | create topic synthesis | active_seed |

## 查询入口

- Cobalt 如何把 BFT 带到没有全局参与者集合的网络?
- UNL overlap 和 essential subsets 的关系是什么?
- 为什么 Cobalt 把治理层和交易排序层分开?

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `translation, application, tension` | endpoint paths above | source notes and legacy bridge detail | Classical BFT agreement/reliable-broadcast reasoning transfers only after adapting quorums to local UNL/essential-subset support; governance Full-Knowledge, transaction-network delegation, randomizing-key CRS, and operator trust configuration are blockchain/open-network-specific. |


## 类比、依赖或关系边界

Classical BFT agreement/reliable-broadcast reasoning transfers only after adapting quorums to local UNL/essential-subset support; governance Full-Knowledge, transaction-network delegation, randomizing-key CRS, and operator trust configuration are blockchain/open-network-specific.


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[doi-10-1145-357172-357176-byzantine-generals-problem|doi-10-1145-357172-357176-byzantine-generals-problem]] | source_note_refs | active_seed |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|doi-10-5555-296806-296824-practical-byzantine-fault-tolerance]] | source_note_refs | active_seed |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|arxiv-1802-07240-cobalt-bft-governance-in-open-networks]] | source_note_refs | active_seed |


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |

## 刷新规则

- Last checked: `2026-06-20`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
