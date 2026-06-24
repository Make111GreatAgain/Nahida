---
id: "nahida-bridge-smart-contract-execution-to-transaction-processing"
title: "Smart contract execution -> blockchain transaction processing"
original_title: "Smart contract execution -> blockchain transaction processing"
file_slug: "smart-contract-execution-to-transaction-processing"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "intra_domain_layer_dependency"
bridge_status: "active_seed"
endpoint_paths:
  - "blockchain-systems/execution-and-transactions/smart-contract-execution"
  - "blockchain-systems/execution-and-transactions/transaction-processing"
endpoint_knowledge_refs:
  - "nahida-knowledge-smart-contract-execution"
  - "nahida-knowledge-blockchain-transaction-processing"
from_domain: "blockchain-systems"
to_domain: "blockchain-systems"
from_direction: "execution-and-transactions"
to_direction: "execution-and-transactions"
from_topic: "smart-contract-execution"
to_topic: "transaction-processing"
relation_types:
  - "dependency"
  - "granularity_shift"
  - "conflict_modeling"
  - "execution_cost_substrate"
directionality: "bidirectional_with_boundaries"
relationship_thesis: "Smart-contract execution semantics influence blockchain transaction processing because contract calls, host/runtime costs, gas/trap outcomes and nested invocation structure determine the granularity at which transactions can be analyzed, rolled back and rescheduled. Conversely, transaction-processing constraints such as deterministic commit order, serializability, rollback policy and block snapshots constrain which smart-contract executions are safe to parallelize."
transferability: "high_for_execution_granularity_medium_for_runtime_costs"
non_transfer_boundary: "Smart-contract VM determinism, gas metering, trap semantics and ABI/runtime compatibility do not by themselves solve transaction ordering, conflict detection, serializability or consensus safety. Transaction-processing algorithms do not by themselves define VM semantics or make arbitrary host calls deterministic. Nested contract call structure can transfer as subtransaction scheduling information only when all nodes can capture the same invocation/read-write dependencies and apply deterministic rollback/reschedule rules."
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
domains:
  - "blockchain-systems"
topics:
  - "smart contract execution"
  - "blockchain transaction processing"
  - "nested contract transactions"
  - "deterministic runtime"
  - "deterministic concurrency control"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
  - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
knowledge_refs:
  - "nahida-knowledge-smart-contract-execution"
  - "nahida-knowledge-blockchain-transaction-processing"
  - "nahida-knowledge-nested-contract-transaction-execution"
relation_edges:
  - from: "nahida-bridge-smart-contract-execution-to-transaction-processing"
    relation: "connects"
    to: "nahida-knowledge-smart-contract-execution"
    evidence_refs:
      - "vault/05_Bridges/smart-contract-execution-to-transaction-processing.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-smart-contract-execution-to-transaction-processing"
    relation: "connects"
    to: "nahida-knowledge-blockchain-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/smart-contract-execution-to-transaction-processing.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-smart-contract-execution-to-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-smart-contract-execution-to-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
    confidence: "medium"
    status: "supporting_seed"
query_keys:
  - "smart contract execution transaction processing"
  - "nested contract transaction execution"
  - "smart contract concurrency control"
  - "contract call graph transaction conflicts"
  - "deterministic smart contract execution transaction processing"
  - "gas runtime cost transaction execution"
  - "Loom nested contract transactions"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260623-loom-nested-contract-transactions"
source_refs:
  - "arxiv:2504.16552v2"
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
confidence: "medium"
trust_tier: "primary"
---

# Smart contract execution -> blockchain transaction processing

## 命名与路径

- Original title: Smart contract execution -> blockchain transaction processing
- File slug: `smart-contract-execution-to-transaction-processing`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

`smart-contract-execution` 关注合约 VM/runtime、ABI、gas、trap、host API、调用语义和执行性能。`blockchain transaction processing` 关注交易在区块或 ordering unit 内如何并发执行、检测冲突、提交、中止、重执行，并让所有节点得到确定性状态。

这条 bridge 记录一个窄命题: 智能合约执行不是交易处理的同义词，但合约调用结构和 runtime 成本会改变交易处理的粒度与瓶颈。DTVM 给出 runtime-side evidence: gas/trap/JIT/host API 等决定单笔交易执行成本和 replay latency。Loom 给出 stronger structural evidence: nested contract calls 可以拆成 subtransactions，并直接影响冲突检测、部分回滚和重执行调度。

## 连接命题

- From: `blockchain-systems/execution-and-transactions/smart-contract-execution`
- To: `blockchain-systems/execution-and-transactions/transaction-processing`
- Relation types: dependency, granularity_shift, conflict_modeling, execution_cost_substrate
- Directionality: `bidirectional_with_boundaries`
- Relationship thesis: Smart-contract execution semantics influence blockchain transaction processing because contract calls, runtime costs and nested invocation structure determine the granularity at which transactions can be analyzed, rolled back and rescheduled. Transaction processing in turn constrains smart-contract execution through deterministic commit order, conflict resolution, rollback/re-execution rules and block snapshot boundaries.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[smart-contract-execution|Smart contract execution]] | `blockchain-systems/execution-and-transactions/smart-contract-execution` | VM/runtime determinism, gas/trap semantics, ABI/runtime compatibility, contract invocation structure | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]]; [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | active_seed |
| [[transaction-processing|Blockchain transaction processing]] | `blockchain-systems/execution-and-transactions/transaction-processing` | deterministic concurrent execution, conflict analysis, rollback/re-execution, block snapshots and serializability | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]]; existing transaction-processing sources | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Contract invocation tree | subtransaction decomposition and dependency graph | Loom §III-§IV | Requires deterministic capture of calls/read-write sets on all nodes. |
| Weak/strong child dependency | partial rollback and intra-transaction parallelism | Loom §III | Application/runtime semantics must make dependency type observable and deterministic. |
| Runtime cost substrate | transaction execution cost and replay latency | DTVM §3-§5 | Runtime speed does not solve ordering or conflict resolution. |
| Gas/trap/host determinism | safe replay of smart-contract transactions | DTVM §4 | Deterministic VM semantics are necessary but not sufficient for serializable transaction processing. |
| Block snapshot boundary | contract execution schedule and rollback/retry | Loom §IV-D-§V | Snapshot/provisional state handling belongs to transaction processing, not ordinary VM design. |

## 类比、依赖或关系边界

Smart-contract execution details become transaction-processing input only when they affect read/write sets, invocation ordering, cost, trap outcome or state transition. Loom demonstrates the strongest case: the nested call tree itself defines subtransactions, and weak/strong parent-child dependencies decide which computations can be moved, rolled back or reused. DTVM demonstrates a weaker but important case: VM/runtime determinism, JIT latency and gas/trap handling determine how expensive a transaction is to execute and replay.

The reverse direction is also bounded. Transaction-processing algorithms can schedule or roll back contract invocations, but they cannot make an unsafe host function deterministic, define ABI compatibility, or enforce VM memory safety. Consensus ordering is also outside this bridge: Loom assumes an ordering service, and DTVM does not provide consensus safety.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom: A Deterministic Execution Framework Towards Nested Contract Transactions]] | direct structural evidence that nested contract calls change transaction-processing conflict and rollback granularity | active_seed |
| [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM: Revolutionizing Smart Contract Execution with Determinism and Compatibility]] | supporting evidence that runtime determinism, gas/trap and JIT performance affect transaction execution cost and replay | supporting_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `blockchain-systems/execution-and-transactions/smart-contract-execution` | add bridge link and child problem link to nested contract transaction execution | active_seed |
| `blockchain-systems/execution-and-transactions/transaction-processing` | add bridge link and child problem link to nested contract transaction execution | active_seed |

## 查询入口

- 嵌套合约调用为什么会影响交易并发控制?
- Smart contract execution 和 transaction processing 的边界是什么?
- Loom 为什么不是 VM runtime paper?
- gas/trap/JIT 性能如何影响交易处理?
- nested contract transactions 如何从整笔 rollback 变成 subtransaction-level rollback?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: parallel EVM, Block-STM, SChain, EOR, smart-contract VM/runtime, gas semantics or transaction-processing sources that alter endpoint scope or transfer boundary.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[smart-contract-execution|Smart contract execution]] | Bridge links, child structure, method boundary | Loom shows contract invocation structure affects transaction processing. | active_seed |
| [[transaction-processing|Blockchain transaction processing]] | Bridge links, child structure, method boundary | Loom adds subtransaction-level deterministic execution. | active_seed |
| [[nested-contract-transaction-execution|Nested contract transaction execution]] | new node | Durable problem node that lives at the bridge of both endpoints. | active_seed |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-paper-intake-20260623-loom-nested-contract-transactions | Created bridge from smart-contract execution to blockchain transaction processing, with Loom as direct structural evidence and DTVM as runtime-cost support. | 2 source notes | codex |
