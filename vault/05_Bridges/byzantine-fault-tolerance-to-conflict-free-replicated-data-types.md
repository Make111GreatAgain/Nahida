---
id: "nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types"
title: "Byzantine fault tolerance -> conflict-free replicated data types"
original_title: "Byzantine fault tolerance -> conflict-free replicated data types"
file_slug: "byzantine-fault-tolerance-to-conflict-free-replicated-data-types"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "intra_domain_boundary"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
  - "distributed-systems/data-management-and-storage/conflict-free-replicated-data-types"
endpoint_knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-conflict-free-replicated-data-types"
from_domain: "distributed-systems"
to_domain: "distributed-systems"
from_direction: "consensus"
to_direction: "data-management-and-storage"
from_topic: "byzantine-fault-tolerance"
to_topic: "conflict-free-replicated-data-types"
relation_types:
  - "adaptation"
  - "equivocation_boundary"
  - "non_transfer_boundary"
directionality: "one_way_with_boundary"
relationship_thesis: "Byzantine/equivocation reasoning applies to CRDTs when malicious replicas can fork causal histories, but the goal changes from consensus on a total order to strong eventual consistency of replicated data; hash-chained causality can expose equivocation without importing the full BFT consensus quorum protocol."
transferability: "medium_for_fault_model_low_for_protocol_structure"
non_transfer_boundary: "BFT consensus techniques reason about agreement or state-machine replication under quorum and ordering assumptions. CRDTs instead target coordination-free local updates and convergence under eventual delivery; Canteen's BFT-relevant mechanism is hash-chained causal history/equivocation detection, not a PBFT/HotStuff-style total-order protocol."
evidence_window_start: "2022"
evidence_window_end: "2026-06-23"
domains:
  - "distributed-systems"
topics:
  - "byzantine fault tolerance"
  - "CRDTs"
  - "equivocation tolerance"
  - "strong eventual consistency"
source_note_refs:
  - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-conflict-free-replicated-data-types"
relation_edges:
  - from: "nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types"
    relation: "connects"
    to: "nahida-knowledge-byzantine-fault-tolerance"
    evidence_refs:
      - "vault/05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types"
    relation: "connects"
    to: "nahida-knowledge-conflict-free-replicated-data-types"
    evidence_refs:
      - "vault/05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
    confidence: "high"
    status: "active_seed"
query_keys:
  - "BFT CRDT"
  - "equivocation tolerant CRDT"
  - "Byzantine fault tolerance and CRDT"
  - "hash chained CRDT causal history"
  - "Canteen BFT CRDT"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260623-canteen-crdt-datastore"
source_refs:
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
confidence: "medium"
trust_tier: "primary"
---

# Byzantine fault tolerance -> conflict-free replicated data types

## 命名与路径

- Original title: Byzantine fault tolerance -> conflict-free replicated data types
- File slug: `byzantine-fault-tolerance-to-conflict-free-replicated-data-types`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

[[04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance|Byzantine fault tolerance]] 关注 arbitrary faulty participants、equivocation、恶意协作或沉默时系统如何仍保持 safety/agreement/SMR/finality。[[04_Knowledge/distributed-systems/data-management-and-storage/conflict-free-replicated-data-types|Conflict-free replicated data types (CRDTs)]] 关注 replicas 如何在不协调的情况下本地更新并在最终交付相同 updates 后收敛。

这条 bridge 记录一个边界: Byzantine/equivocation threat model 可以迁移到 CRDT 语境，但协议目标不再是 total-order consensus，而是 strong eventual consistency (SEC) 和 causality-preserving convergence。

## 连接命题

- From: `distributed-systems/consensus/byzantine-fault-tolerance`
- To: `distributed-systems/data-management-and-storage/conflict-free-replicated-data-types`
- Relation types: adaptation, equivocation_boundary, non_transfer_boundary
- Directionality: `one_way_with_boundary`
- Relationship thesis: Byzantine/equivocation reasoning applies to CRDTs when malicious replicas can fork causal histories, but the goal changes from consensus on a total order to strong eventual consistency of replicated data; hash-chained causality can expose equivocation without importing the full BFT consensus quorum protocol.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance|Byzantine fault tolerance]] | `distributed-systems/consensus/byzantine-fault-tolerance` | Byzantine/equivocation fault model, malicious conflicting histories, non-equivocation mechanisms | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] §2.7, §3.2 | foundation_thin |
| [[04_Knowledge/distributed-systems/data-management-and-storage/conflict-free-replicated-data-types|Conflict-free replicated data types (CRDTs)]] | `distributed-systems/data-management-and-storage/conflict-free-replicated-data-types` | SEC, eventual delivery, replicated data convergence, causality DAG/hash-chained operations | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] §2-§3 | foundation_thin |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Equivocation as conflicting history | CRDT replicas can detect divergent causal roots/logs when malicious nodes fork operations. | Canteen roots as fault-tolerant logical clocks | Detection does not automatically impose a single total order. |
| Hash-chained causality | Operation IDs commit to operation metadata and immediate ancestors. | Canteen §3.1-§3.2 | Requires replicas to exchange DAG/log information; not a quorum certificate. |
| Correct-node communication assumption | BFT SEC for CRDTs needs correct replicas to eventually communicate. | Canteen §2.7 | Different from `3f+1` BFT consensus quorum assumption. |
| Non-equivocation abstraction | Similar to trusted append-only logs in BFT-related systems, but implemented via cryptographic causal history. | Canteen; AHL is adjacent but different | Canteen does not depend on TEE in this source. |

## 迁移矩阵

| BFT concept | CRDT adaptation | 证据 | 不迁移的部分 |
| --- | --- | --- | --- |
| Byzantine node may send conflicting messages | Byzantine CRDT replica may send divergent operations/log histories. | Canteen §2.7 | PBFT/HotStuff prepare/commit/vote protocol. |
| Equivocation detection | Hash-chained DAG roots expose different causal histories. | Canteen §3.2 | Consensus view-change/finality/quorum certificates. |
| Fault tolerance objective | Preserve SEC despite malicious replicas. | Canteen §2.7 | Agreement on one total operation order. |
| Replication model | Append local operations without coordination, then converge. | Canteen §2-§3 | State-machine replication with ordered log decided by consensus. |

## 类比、依赖或关系边界

Canteen explicitly states that BFT CRDTs do not follow the same threshold framing as standard BFT consensus. The source says BFT SEC can be achieved with arbitrary Byzantine nodes only under the unavoidable assumption that every pair of correct nodes can directly communicate. This means the bridge is about an adapted fault model and equivocation boundary, not about importing consensus protocol mechanics.

The practical implication is that a future query about "BFT CRDT" should not start from PBFT quorum protocols alone. It should start from CRDT SEC, causal history, operation delivery, and then open BFT only for the adversarial/equivocation vocabulary.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen: A Partially-Ordered Log Abstraction for the Emerging CRDT Datastore]] | Direct evidence for BFT/equivocation discussion in CRDT setting and for hash-chained partially ordered logs. | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/data-management-and-storage/conflict-free-replicated-data-types` | Created CRDT problem node with bridge link and Canteen source extension. | foundation_thin |
| `distributed-systems/consensus/byzantine-fault-tolerance` | Add bridge link and source-extension row for equivocation-tolerant CRDTs. | active_seed |

## 查询入口

- BFT CRDT 和 BFT consensus 有什么区别?
- Canteen 如何用 hash-chained DAG 处理 equivocation?
- CRDT 的 SEC 为什么不是 total-order consensus?
- Byzantine replica 在 CRDT 中会造成什么问题?
- Equivocation-tolerant CRDTs 需要哪些假设?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: direct sources on Making CRDTs Byzantine Fault Tolerant, equivocation-tolerant CmRDTs, Byzantine SEC definitions, or implementation sources for BFT CRDT datastores.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage/conflict-free-replicated-data-types|Conflict-free replicated data types (CRDTs)]] | bridge links, methods, source extensions | Canteen creates the CRDT problem node and BFT boundary. | foundation_thin |
| [[04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance|Byzantine fault tolerance]] | bridge links and source extension | Canteen adds a non-consensus equivocation-tolerance application boundary. | active_seed |

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: new source changes either endpoint, relation type, transfer boundary, or maturity.

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-paper-intake-20260623-canteen-crdt-datastore | Created bridge from Canteen's BFT/equivocation-tolerant CRDT evidence. | sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84 | codex |
