---
id: "sha256-ad4df792f387-loom-deterministic-nested-contract-transactions"
title: "Loom: A Deterministic Execution Framework Towards Nested Contract Transactions"
type: "source"
source_kind: "paper"
source_subtype: "local_pdf"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
hierarchy_level: "source"
created: "2026-06-23"
updated: "2026-06-23"
authors:
  - "Huan Zhang"
  - "Xiaodong Qi"
  - "Haibo Tang"
  - "Zhao Zhang"
  - "Cheqing Jin"
  - "Aoying Zhou"
year: 2025
venue: "ICDE 2025"
publisher: "IEEE"
source_refs:
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
canonical_url: ""
doi: ""
arxiv_id: ""
local_pdf_path: "~/Desktop/paper/Loom_ICDE2025.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/loom_icde2025-ad4df792f387-pages.txt"
pages: 14
page_count: 14
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
classification_status: "corrected_absorbed"
classification_confidence: "high"
primary_domain: "blockchain-systems"
primary_direction: "execution-and-transactions"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing/nested-contract-transaction-execution"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
  - "nested-contract-transaction-execution"
secondary_ontology_paths:
  - "blockchain-systems/execution-and-transactions/smart-contract-execution"
  - "distributed-systems/transaction-processing"
topic_ids:
  - "nested-contract-transaction-execution"
  - "deterministic-concurrency-control"
  - "smart-contract-concurrency-control"
  - "partial-rollback"
  - "fine-grained-rescheduling"
  - "multi-phase-parallelism"
domains:
  - "blockchain-systems"
topics:
  - "nested contract transactions"
  - "permissioned blockchain"
  - "transaction processing"
  - "smart contract execution"
  - "deterministic concurrency control"
  - "nested transactions"
aliases:
  - "Loom"
  - "Loom nested contract transactions"
tags:
  - "nahida/source"
  - "nahida/source/paper"
  - "blockchain-systems"
  - "transaction-processing"
  - "smart-contract-execution"
classification_evidence:
  - "local PDF deep read p1-p14"
  - "Title, abstract and index terms identify permissioned blockchain, nested contract transactions, concurrency control and transaction processing."
  - "Sections III-IV define nested contract transaction trees, intra-transaction dependency, hyper-dependency graph, two-phase rollback, fine-grained re-execution and multi-phase parallelism."
  - "Primary placement is blockchain transaction processing because the paper optimizes deterministic concurrent execution after transaction ordering; smart-contract execution is a secondary endpoint because nested contract calls define the execution granularity."
knowledge_node_refs:
  - "[[nested-contract-transaction-execution|Nested contract transaction execution]]"
  - "[[transaction-processing|Blockchain transaction processing]]"
  - "[[smart-contract-execution|Smart contract execution]]"
  - "[[execution-and-transactions|Blockchain execution and transactions]]"
bridge_refs:
  - "[[smart-contract-execution-to-transaction-processing|Smart contract execution -> blockchain transaction processing]]"
  - "[[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]]"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "item0108"
run_id: "nahida-paper-intake-20260623-loom-nested-contract-transactions"
managed_by: "nahida"
confidence: "high"
trust_tier: "primary"
---

# Loom: A Deterministic Execution Framework Towards Nested Contract Transactions

## Paper Identity

| 字段 | 内容 |
| --- | --- |
| 论文 | Loom: A Deterministic Execution Framework Towards Nested Contract Transactions |
| 作者 | Huan Zhang; Xiaodong Qi; Haibo Tang; Zhao Zhang; Cheqing Jin; Aoying Zhou |
| 机构 | East China Normal University; Nanyang Technological University |
| 年份 | 2025 |
| Venue | ICDE 2025, from local filename/queue metadata; extracted title page itself has no visible conference footer |
| 本地 PDF | `~/Desktop/paper/Loom_ICDE2025.pdf` |
| 校验和 | `sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd` |

## Reading Coverage

| 范围 | 覆盖 |
| --- | --- |
| PDF extraction | `pypdf` extraction usable; 14 pages. |
| 覆盖章节 | Abstract, §I Introduction, §II Background and Related Work, §III Motivation, §IV Loom Design, §V Analysis and Discussions, §VI Evaluation, §VII Conclusion, References. |
| 元数据修正 | Queue title/year match the first page and PDF metadata. Authors were restored from the extracted title page. DOI/arXiv are absent from PDF metadata and body extraction. |
| 分类修正 | Queue staged path `blockchain-systems/execution-and-transactions/transaction-processing` was too broad. Deep read shows a more specific child problem: [[nested-contract-transaction-execution|nested contract transaction execution]], with [[smart-contract-execution|smart contract execution]] as a secondary endpoint. |

## One-Sentence Takeaway

Loom 把已排序区块中的嵌套合约交易从“整笔交易并发/回滚”细化为 subtransaction-level deterministic execution：先在同一 snapshot 上并发预执行捕获调用树和读写集，再用 HDG/SAT/GWG 选择最小化重算的部分回滚，最后通过细粒度重调度和跨区块 multi-phase parallelism 提高并发度。

## Cold-Start Hierarchy Discovery

| Facet | Result | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | blockchain systems | permissioned blockchain, smart contracts, transaction processing | high | existing domain |
| Direction | execution and transactions | source optimizes execution after ordering, not consensus safety | high | existing direction |
| Research problem | nested contract transaction execution | whole paper centers cross-contract nested call chains, deterministic serializability, rollback and re-execution | high | create child problem node |
| Parent problem | blockchain transaction processing | deterministic concurrent execution, conflicts, rollback/re-execution and block-level resource utilization | high | update existing node |
| Secondary problem | smart contract execution | smart-contract invocation tree defines subtransaction boundaries and dependency types | high | update existing node |
| Bridge endpoint | database transaction processing | paper explicitly imports nested transaction ideas and compares linear/parallel nesting routes | medium | strengthen bridge |
| Source instance | Loom | named framework/prototype | high | source note only |

## Structured Summary

### Problem

Permissioned blockchain systems increasingly execute smart-contract transactions with cross-contract collaborations and long nested call chains. The paper calls these nested contract transactions. In these workloads, treating a transaction as one flat atomic unit creates two related bottlenecks:

- Cross-contract state access increases inter-transaction conflicts.
- Optimistic parallel execution often rolls back whole transactions, so a conflict late in a long call chain wastes all earlier computation and may trigger cascading rollback.

Blockchain execution cannot simply choose any convenient commit order like a local database scheduler. Replicas need deterministic serializability: all nodes must commit transactions in the same order and converge to the same state.

### Nested Contract Transaction Model

The paper models each nested contract transaction as a transaction tree. Each node is a subtransaction identified by invocation order. Parent-child edges are split into:

- **Strong dependency:** child success is required before the parent can progress.
- **Weak dependency:** child can execute independently without affecting the parent result.

This distinction creates a dependency tree and then a hyper-dependency graph (HDG), which records both intra-transaction dependencies and inter-transaction conflicts. The reusable idea is that nested smart-contract execution has more scheduling structure than a flat read/write set: some children can be retried or moved without aborting the whole parent transaction.

### Loom Pipeline

Loom executes each block through three main phases:

1. **Snapshot-based parallel pre-execution:** all transactions run on the same snapshot; the system captures nested structure, read/write sets, invocations and execution overhead.
2. **Two-phase deterministic rollback:** the system builds HDG plus state access table (SAT), then selects rollback subtransactions rather than whole transactions.
3. **Fine-grained re-execution:** rollback subtransactions are rescheduled at subtransaction granularity while preserving deterministic serialization order.

The prototype also adds multi-phase parallelism across consecutive blocks by using provisional and finalized snapshots.

### Two-Phase Rollback

The fast rollback phase uses SAT to detect complete conflict subgraphs around hot states. It keeps the subtransaction with the highest rollback overhead and rolls back the rest, pruning obvious dense conflicts before graph-level optimization.

The min-weight rollback phase maps HDG into a global-weight graph (GWG). Subtransactions in the same transaction become a hypervertex; inter-transaction dependencies become weighted hyperedges. The rollback decision becomes an approximate min-weight feedback arc set problem. Loom uses SCC detection and a greedy rule that selects the hypervertex with the lowest serialization overhead, recording both rollback subtransactions and partial serialization orders.

The key reusable abstraction is not the exact heuristic alone, but the layered conflict model: state-level hot conflicts are pruned first, then transaction-level cycles are broken using subtransaction-level rollback costs.

### Fine-Grained Re-Execution

Traditional re-execution often groups whole transactions, causing blocking when nested transactions have long strong-dependency chains. Loom instead treats rollback subtransactions as schedulable units and uses an execution spatiotemporal graph to move later non-conflicting subtransactions into earlier idle slots.

The reschedule strategy preserves:

- target time does not move a subtransaction later than its current schedule.
- required serialization order from rollback is respected.
- strong intra-transaction dependencies are respected.
- conflicting subtransactions are not partially interleaved in a way that breaks serializability.

This allows both intra-transaction parallelism among weak/no-dependency subtransactions and inter-transaction parallelism while a strongly dependent chain is blocked.

### Multi-Phase Parallelism

Loom defines provisional snapshots after rollback/partial commitment and finalized snapshots after full commitment. Idle threads can start pre-executing the next block on an older snapshot, then roll back or re-execute next-block transactions if they have read-write dependencies on writes from the previous block.

This optimization is a resource-utilization layer. It does not change the correctness boundary: final commitment still depends on deterministic snapshot and dependency handling.

### Correctness Argument

The paper argues consistency because every node starts from the same snapshot, constructs the same SAT/HDG, applies deterministic rollback strategy, derives the same `rbList`/`pOrders`, and builds the same re-execution schedule from `pOrders` and transaction IDs. With multi-phase parallelism, nodes may pre-execute on provisional/finalized snapshots, but dependency checks force affected transactions into rollback/retry.

The paper argues serializability by eliminating cycles in the read-write dependency graph. Rolling back tail vertices removes edges from cycles, and the recorded serialization order determines whether transactions that rollback outgoing or incoming edges commit last or first.

### Evaluation

| Dimension | Setup / Result | Interpretation |
| --- | --- | --- |
| Baselines | Serial, Aria, Harmony, HarmonyIB, Fractal, implemented in the same C++ framework | Compares flat deterministic snapshot approaches, inter-block parallelism and nested speculative execution |
| Workload | TPC-C-like smart contracts, variable warehouses/contention, default block size 1600 | Designed to trigger nested contract calls and contention |
| Overall throughput | 10.2x over Aria, 6x over HarmonyIB, 8.7x over Fractal; nearly 40x Serial with 48 threads | Supports the claim that subtransaction-level rollback/rescheduling matters under nested-call workloads |
| Latency | 83.2% to 90.7% lower than other snapshot-based schemes | Faster block execution reduces snapshot-based waiting |
| Re-execution overhead | 89.9% to 98.4% lower than Aria, 89.2% to 95.5% lower than Harmony | Two-phase rollback prevents whole-transaction retry from dominating |
| Re-execution concurrency | Under high contention, 8.7x Aria and 9.45x Harmony concurrency degree | Fine-grained rescheduling extracts intra/inter-transaction parallelism |
| Ablation | Fine-grained rescheduling and multi-phase parallelism each improve throughput/latency/CPU utilization | Rollback, reschedule and pipeline are separable contributions |

## Limitations And Boundary

- Loom is an execution framework for permissioned blockchain transaction execution, not a consensus protocol.
- It assumes transactions are already ordered by an ordering service and nodes can apply deterministic execution rules.
- Evaluation is on TPC-C-like smart contracts and a C++ prototype; production smart-contract workloads, adversarial contracts, stateDB/IO bottlenecks and contract-language runtime details may change performance.
- The framework handles nested call execution and rollback scheduling. It does not solve VM-level determinism/gas/trap semantics; that remains under [[smart-contract-execution|smart contract execution]].
- The database nested-transaction lineage is used as method inspiration; database trust assumptions, non-deterministic scheduling and local commit-order freedom do not transfer unchanged.

## What This Source Adds To Nahida

- Creates [[nested-contract-transaction-execution|Nested contract transaction execution]] as a reusable problem node under blockchain transaction processing.
- Strengthens [[transaction-processing|Blockchain transaction processing]] with a subtransaction-level deterministic concurrency route.
- Extends [[smart-contract-execution|Smart contract execution]] beyond VM/runtime determinism into contract invocation structure as execution granularity.
- Strengthens [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] with nested-transaction transfer evidence.
- Creates or strengthens [[smart-contract-execution-to-transaction-processing|Smart contract execution -> blockchain transaction processing]] as a bridge: contract call semantics influence transaction-processing conflict granularity.

## Source-Backed Takeaways

- Nested contract transactions should not be flattened by default when optimizing blockchain execution; the call tree itself carries scheduling and rollback information.
- Weak vs strong intra-transaction dependencies are the reusable abstraction that separates independent children from parent-critical children.
- Deterministic blockchain execution turns ordinary nested-transaction concurrency control into a stricter scheduling problem because all replicas must choose the same rollback and serialization order.
- Partial rollback has two roles: reducing recomputation and reducing graph complexity before fine-grained rescheduling.
- Cross-block execution parallelism is safe only when snapshot provenance and dependency-triggered rollback are explicit.

## Absorption Targets

- [[nested-contract-transaction-execution|Nested contract transaction execution]]
- [[transaction-processing|Blockchain transaction processing]]
- [[smart-contract-execution|Smart contract execution]]
- [[execution-and-transactions|Blockchain execution and transactions]]
- [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]]
- [[smart-contract-execution-to-transaction-processing|Smart contract execution -> blockchain transaction processing]]

## Review Notes

- Keep Loom as a source instance. Do not create `Loom` as a knowledge node unless a later repository/source analysis requires a source-specific implementation note.
- Potential future child split: `deterministic smart-contract concurrency control`, `parallel EVM execution`, or `subtransaction-level rollback`, but one direct Loom source is not enough to split those yet.
- Future sources to compare: Block-STM, SChain, EOR, parallel EVM, Fractal/JTF nested transaction sources, and database nested transaction foundations.
