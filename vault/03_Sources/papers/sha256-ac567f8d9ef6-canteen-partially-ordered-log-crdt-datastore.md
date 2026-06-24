---
id: "sha256-ac567f8d9ef6"
title: "Canteen: A Partially-Ordered Log Abstraction for the Emerging CRDT Datastore"
type: "source"
source_kind: "paper"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
hierarchy_level: "source"
created: "2026-06-23"
updated: "2026-06-23"
authors:
  - "Preston McCrary"
year: 2022
venue: "unknown"
publisher: "unknown"
source_refs:
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
canonical_url: ""
doi: ""
arxiv_id: ""
local_pdf_path: "~/Desktop/paper/crdts_ucb.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/canteen-a-partially-ordered-log-abstraction-for-the-emerging-crdt-datastore-ac567f8d9ef6-pages.txt"
pages: 10
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
primary_domain: "distributed-systems"
primary_direction: "data-management-and-storage"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
primary_ontology_path: "distributed-systems/data-management-and-storage/conflict-free-replicated-data-types"
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "conflict-free-replicated-data-types"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
topic_ids:
  - "conflict-free-replicated-data-types"
  - "crdts"
  - "eventual-consistency"
  - "partially-ordered-logs"
  - "crdt-garbage-collection"
  - "non-commutative-crdts"
  - "equivocation-tolerant-crdts"
domains:
  - "distributed-systems"
topics:
  - "CRDTs"
  - "eventual consistency"
  - "strong eventual consistency"
  - "partially-ordered logs"
  - "Concurrent Operation Groups"
  - "equivocation tolerance"
aliases:
  - "Canteen"
  - "Canteen CRDT datastore"
  - "Partially-Ordered Log Abstraction for CRDT Datastore"
tags:
  - "nahida/source"
  - "paper"
  - "crdts"
  - "distributed-systems"
classification_status: "absorbed"
classification_confidence: "high"
knowledge_node_refs:
  - "[[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]"
  - "[[conflict-free-replicated-data-types|Conflict-free replicated data types]]"
bridge_refs:
  - "[[byzantine-fault-tolerance-to-conflict-free-replicated-data-types|Byzantine fault tolerance -> CRDTs]]"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "item0103"
run_id: "nahida-paper-intake-20260623-canteen-crdt-datastore"
managed_by: "nahida"
confidence: "high"
trust_tier: "primary"
---

# Canteen: A Partially-Ordered Log Abstraction for the Emerging CRDT Datastore

## Paper Identity

| 字段 | 内容 |
| --- | --- |
| 论文 | Canteen: A Partially-Ordered Log Abstraction for the Emerging CRDT Datastore |
| 作者 | Preston McCrary |
| 机构 | University of California, Berkeley |
| 年份 | 2022 |
| 会议/期刊 | unknown; PDF 只显示 ACM article template 与 `Publication date: December 2022` |
| DOI | unknown in PDF |
| arXiv | unknown in PDF |
| URL | unknown in PDF |
| 本地 PDF | `~/Desktop/paper/crdts_ucb.pdf` |
| 校验和 | `sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84` |

## Reading Coverage

| 范围 | 覆盖 |
| --- | --- |
| PDF extraction | `pypdf` extraction usable; 10 pages. |
| 覆盖章节 | Title/abstract, §1 Introduction, §2 CRDT Background, §3 Canteen, §4 Evaluation, §5 Conclusion and Future Work, References. |
| 元数据修正 | PDF metadata title matches first-page title; queue title is usable. DOI/venue/canonical URL not present in PDF, so kept as `unknown`. |
| safe_for_absorption | yes. 问题、CRDT 背景、Canteen mechanism、BFT/equivocation boundary、evaluation 与 limitations 均已覆盖。 |

## One-Sentence Takeaway

Canteen 把 CRDT 的更新组织成 hash-chained partially-ordered log，并用 roots-as-logical-clocks、delta swaps、Concurrent Operation Groups (COGs) 和 COG-Interpreter 来支持 generalized garbage collection、non-commutative operations 与 equivocation tolerance。

## Cold-Start Hierarchy Discovery

| Facet | Result | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | distributed systems | consistency, replication, partitions, CRDTs, Byzantine/equivocation fault discussion | high | existing domain |
| Direction | data management and storage | replicated datatypes/datastore, metadata garbage collection, persistence/recovery/buffer concerns | high | existing direction |
| Research problem | conflict-free replicated data types (CRDTs) as coordination-free replicated state | Abstract, §1, §2 | high | create/update problem node |
| Foundation concepts | eventual consistency, strong eventual consistency, CvRDT, CmRDT, delta-CRDTs, causal order, join-semilattice | §2.1-§2.6 | high | seed foundation-thin node; queue canonical sources |
| Method family | partially ordered log abstraction; hash-chained operation DAG; COG-based compaction/interpreter | §3.1-§3.5 | high | source extension under CRDTs |
| Application/evaluation context | emerging CRDT datastore; simulation of swaps/log compaction; OR-Set and 0-bounded counter interpreter examples | §3.6, §4 | medium | source-only evaluation evidence |
| Bridge endpoint | Byzantine fault tolerance / equivocation tolerance | §2.7, §3.2 | high | create narrow bridge to BFT with non-transfer boundary |
| Source instance | Canteen | Title, abstract, §3 | high | representative source extension, not standalone knowledge node |

## Structured Summary

### Problem

CRDTs 让 replicas 可以不协调地本地更新，并在最终收到相同更新后达到相同状态。论文认为它们有三个实践瓶颈：大量 metadata 很难通用 garbage collect；缺乏一个统一的 fault-tolerant abstraction；很多 CRDT 要求内部状态或并发操作满足数学约束，使 non-commutative application logic 难以表达。

论文特别指出 production-quality CRDT 不只是几十行数学定义，还需要考虑 fault tolerance、persistence、recovery、buffer management 以及内存放不下时的数据管理。因此研究新 CRDT specification 时，如果每次都要重写完整实现，比较和迭代成本会很高。

### Background

论文从 strong consistency 与 CAP tradeoff 切入，说明 eventual consistency 允许 replicas 暂时不同，但最终收敛。CRDTs 提供更强的 strong eventual consistency (SEC)：correct replicas 交付相同 updates 时立即具有 equivalent state，不需要 rollback 或 conflict recovery。

State-based CRDTs (CvRDTs) 依赖 join-semilattice 与 monotonic operations。它们只需 reliable broadcast，但通常要 gossip entire local state，网络开销可能很高。Operation-based CRDTs (CmRDTs) 通过 causal broadcast 传播操作，payload 更小，但要求所有操作按 causal order 交付，且 concurrent operations 必须 commutative。Delta state-based CRDTs 减少 state payload，但在高连通/cyclic topology 中 delta groups 可能被冗余发送，需要额外 metadata 和优化。

### Method

Canteen 的核心是一个 grow-only DAG/partially-ordered log。每个 node 表示一个 operation invocation，边表示 immediate happens-before dependency；每个 node 还包含其 immediate ancestors 的 hashes，因此 node hash 同时承诺 operation metadata 和 causal history。所有 replicas 从 genesis node 开始。

本地 append 时，replica 创建一个包含 operation metadata 的新 node，并把 outgoing edges 指向当前 roots，从而让新 operation 成为新的 root。收到 remote log 后，replica 先遍历验证 hash-chain integrity，再把 unseen nodes 追加到本地 DAG。查询时，不直接依赖接收顺序，而是通过 deterministic interpreter 重放 log，得到底层 CRDT 的 serial logical state。

这个 separation of physical log and logical state 带来两个效果：append 的 critical path 不需要判断 operation validity，只要保存完整性；其次，因为 logical state 由 deterministic replay 生成，same log 的 replicas 可以得到 same state，即使 operations 本身不是 commutative。

### Roots As Fault-Tolerant Logical Clocks

Canteen roots 可以作为 logical clock。如果一个 replica 的 roots 被另一个 replica 的 DAG 包含，后者知道前者落后；如果 roots 相同，二者有相同 log；如果收到的 roots 本地没有，则说明缺失 operations。

论文强调 roots 是 fault-tolerant logical clocks，因为 root hash 由其全部 causal history 递归决定。Byzantine replica 试图 equivocate 给两个 correct replicas 发送不同 operations 时，两个 correct replicas 的 roots 会不同，随后交换 DAG 并发现差异。若只用 vector clocks，两边可能看到相同 clock 而不交换 DAG。

### Delta Swaps, Stability, COGs And Compaction

Canteen 不做传统单向 gossip，而是 pair-wise delta swaps。一次 swap 先发送自上次 swap 以来的 delta，接收方追加 unseen nodes 后把新 roots 和自己的 delta 回发。每对 replicas 记住 last known common subgraph roots，之后只传需要的差量。

Operation stability 的定义是：每个 replica 都已交付依赖该 operation 的 update，因此该 operation 已在所有 logs 中。Canteen 通过取所有 replicas last-known subgraphs 的 intersection 来找 stable set。稳定节点可用于 garbage collection。

Gossip protocol 会让 replicas 周期性和所有 available replicas swap，并 atomically 把收到的 nodes 放到 graph 上。这样 log 会被乐观地切分成若干 concurrent operation threads，再由 swap 后的单个 node join。论文把这些 partitioned concurrent operations 称为 Concurrent Operation Groups (COGs)。

COG-Interpreter 将 partially ordered log 视作一个 totally ordered list of COGs，并逐个 COG 生成 logical state。稳定 COG 可以 compact：把该 COG 产生的 logical state 存成 serial format，然后删去不再需要的 operation metadata。`getNextStableCOG()` 从 `compactedLogNode` 出发检查 sole dependents 是否稳定；`compactLog()` 更新 dependents/dependencies 并从 graph 中移除已 compacted nodes。

### Proposed Architecture

论文不把 Canteen 定义为完整 DBMS，而建议把 Canteen 或类似 partially-ordered log abstraction 放在现有 domain-specific DBMS 之上，作为 highly concurrent replication and mutation layer。稳定数据可以写入下层 serial datastore；query 可以选择查询 stable data 或 live data；新 replicas 可用 previous snapshot 与 `compactedLogNode` bootstrap，而不必重放完整 log history。

## Detailed Outline

| Section/Page | 内容角色 | 关键内容 | Evidence value |
| --- | --- | --- | --- |
| p1 Abstract | 论文主张 | CRDT 的 metadata overhead、fault tolerance、commutativity limitations；Canteen/COG 解决方向 | identity and problem |
| p1-p2 §1 Introduction | 背景与动机 | strong consistency/CAP/eventual consistency/CRDTs；实践瓶颈；Canteen proof-of-concept 与 evaluation questions | problem framing |
| p2-p4 §2 CRDT Background | Foundation | EC/SEC、CvRDT、join-semilattice、CmRDT、delta-CRDT、BFT/equivocation tolerance | foundation seed |
| p4-p7 §3 Canteen | Main mechanism | hash-chained DAG、roots logical clocks、delta swaps、operation stability、COGs、COG interpreter、log truncation、architecture | technical core |
| p7-p9 §4 Evaluation | Evaluation | simulation N=3/5/10，log compactness, partition recovery, swap sizes, OR-Set and zero-bounded counter interpreters | evidence and caveat |
| p9 §5 Conclusion | Claims/future work | Canteen validates COG concept but needs optimized implementation and further non-commutative CRDT work | limitation/future |
| p9-p10 References | Related work | Delta-CRDTs, Dynamo, Cassandra, CAP, BFT CRDTs, Kleppmann BFT CRDTs, Shapiro CRDTs | foundation gap list |

## Technical Content

### Definitions And Assumptions

| Term | Paper meaning | Anchor |
| --- | --- | --- |
| Eventual consistency (EC) | Eventual Delivery, Convergence, Termination. | §2.1 Definition 1 |
| Strong eventual consistency (SEC) | EC plus Strong Convergence: correct replicas that delivered same updates have equivalent state. | §2.1 Definition 2 |
| CvRDT | State-based CRDT with states `S`, bottom state, join-semilattice ordering, monotonic operations, query methods, and merge/join operation. | §2.3 |
| CmRDT | Operation-based CRDT with prepare/effect/query methods, causal delivery, and commutative concurrent operations. | §2.5 |
| Delta state-based CRDT | Delta-decomposition of CvRDT, sending delta groups instead of full state. | §2.6 |
| BFT CRDT | CRDT that provides SEC despite Byzantine nodes; paper highlights direct correct-node communication and equivocation tolerance. | §2.7 |
| COG | Concurrent Operation Group, formed by Canteen's swap protocol partitioning concurrent operation threads. | §3.4 |

### Algorithms

| Algorithm/Procedure | Role | Notes |
| --- | --- | --- |
| `appendLog` | Add an underlying CRDT operation to the DAG. | New node points to current roots and embeds ancestor hashes. |
| Join / remote log verification | Merge remote log into local DAG. | Traverses received DAG, verifies hash integrity, appends unseen nodes. |
| Delta swap | Pairwise exchange of unseen nodes since last common subgraph. | Stores common-subgraph roots for future deltas and stability inference. |
| `getNextStableCOG()` | Identify next stable COG starting from `compactedLogNode`. | Returns none if any sole dependent is not stable. |
| `compactLog()` | Remove compacted nodes while preserving dependency information in compacted node. | Enables metadata garbage collection while keeping serialized state. |

## Evaluation

### Setup And Metrics

| Aspect | Detail |
| --- | --- |
| Environment | Simulation environment for Canteen clusters. |
| Cluster sizes | `N=3`, `N=5`, `N=10`. |
| Workload | Mean operations per time step = 3, distributed among replicas; gossip/swap every 400 time steps; noise added to avoid constant-value artifacts. |
| Approximation | With <200ms RTT and <400ms per swap, authors interpret this as about 3000 operations/second for the cluster. |
| Network partition | Simulated by stopping deltas among selected nodes. |
| Metrics | Average non-compacted operations per replica, recovery multiples of gossip frequency after partition, 50th/90th/99th percentile swap sizes. |

### Results

| Finding | Evidence | Caveat |
| --- | --- | --- |
| Average non-compacted log size increases sub-linearly with cluster size. | N=3 about 232 nodes, N=5 about 307, N=10 about 410. | Simulation only; no real storage engine integration. |
| Partition recovery is quick in gossip-frequency units. | About 2x for N=3, 3x for N=5, 4x for N=10. | Assumes propagation delay dominates transmission delay for short partitions. |
| Swap sizes do not grow linearly with replicas. | Authors state 50th/90th percentile swap sizes remain same despite partition. | Figures are not numerically tabulated in extracted text. |
| COG-Interpreter can express existing and novel CRDTs compactly. | zero-bounded counter interpreter took 5 lines; Observed-Remove Set about 20. | Additional logic needed to reconcile compacted vs non-compacted data. |
| The evaluation intentionally does not focus on throughput/latency. | §1 and §4 say evaluation targets potential indicators, not latency/throughput. | Production viability remains future work. |

## Limitations And Review Notes

- The PDF does not provide DOI, arXiv ID, venue, canonical URL, code URL, or dataset URL.
- Canteen is evaluated as proof-of-concept simulation, not as a production DBMS or full system deployment.
- Evaluation focuses on log compactness, swap size, and interpreter ergonomics; it does not measure full latency/throughput or persistence overhead in a real database stack.
- The compacted/non-compacted boundary made OR-Set interpreter logic more complicated than expected, so generalized garbage collection is not free.
- Canteen's BFT/equivocation tolerance claim relies on hash-chained causality and correct-node communication assumptions; it should not be conflated with BFT consensus quorum protocols.

## Evidence Table

| Claim | Source anchor | Confidence |
| --- | --- | --- |
| Canteen targets CRDT metadata garbage collection, fault tolerance, and non-commutative operations. | Abstract, §1 | high |
| CvRDTs rely on join-semilattice and monotonic operations; CmRDTs rely on causal delivery and commutative concurrent operations. | §2.2-§2.5 | high |
| Canteen uses hash-chained DAG nodes so roots embed causal history and resist equivocation. | §3.1-§3.2 | high |
| Delta swaps produce common subgraphs and allow stability detection. | §3.3 | high |
| COGs allow Canteen to compact stable operation metadata and support non-commutative interpreter logic. | §3.4-§3.5 | high |
| Simulation shows sub-linear increase in non-compacted log size over N=3/5/10 and rapid partition recovery. | §4.1 | medium |
| COG-Interpreter examples are compact but require extra logic for compacted/non-compacted state. | §4.2 | high |

## Knowledge Handoff

| Target | Handling | Rationale |
| --- | --- | --- |
| [[conflict-free-replicated-data-types|Conflict-free replicated data types (CRDTs)]] | create/update problem node | CRDTs are reusable foundation/problem under distributed data management; Canteen is representative source extension. |
| [[data-management-and-storage|Data management and storage]] | add child node and source extension | CRDTs add replicated data consistency and datastore-metadata management path to existing storage/query/repair structure. |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | add bridge/source extension | Paper distinguishes equivocation tolerance for CRDTs from BFT consensus threshold/quorum setting. |
| [[byzantine-fault-tolerance-to-conflict-free-replicated-data-types|Byzantine fault tolerance -> CRDTs]] | create active_seed bridge | Explicit cross-path relation with transfer and non-transfer boundary. |

## Foundation Candidate Judgment

| Candidate | Judgment | Why |
| --- | --- | --- |
| CRDTs | `foundation_thin` knowledge node | Reusable distributed-systems concept; current vault lacks direct canonical Shapiro/Preguiça source notes, but Canteen provides enough background to create a seed. |
| Canteen | source instance/source extension | Named system from this paper; should not become upper foundation node. |
| COGs | source-specific method primitive | Useful Canteen mechanism; can stay inside source note and CRDT method row until more sources reuse it. |
| BFT CRDTs / equivocation-tolerant CRDTs | bridge/source-extension candidate | Important boundary with BFT, but currently one local direct source. |

## Retrieval Optimization

- Future query "CRDT 是什么" can start at the CRDT knowledge node rather than this paper.
- Future query "Canteen 解决了 CRDT 什么问题" can read CRDT node source-extension row, then this source note if detail is needed.
- Future query "BFT CRDT 和 BFT consensus 有什么区别" can use the BFT->CRDT bridge.
- Source-only details: exact delta-swap implementation, compactLog pseudocode, simulation parameters, line counts of example interpreters.

## Review Items

| Item | Reason | Next action |
| --- | --- | --- |
| Canonical CRDT sources missing | Canteen cites CRDT overview and Shapiro 2011 but those papers are not separately absorbed. | future `nahida-research-search` or paper intake foundation pack |
| Venue/DOI unknown | Not present in local PDF extraction or metadata. | external metadata verification only if user requests/source needs canonicalization |
| Production viability | Simulation-only evaluation. | wait for implementation/repo/production source |
