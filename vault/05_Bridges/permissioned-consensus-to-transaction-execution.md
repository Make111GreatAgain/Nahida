---
id: "nahida-bridge-permissioned-consensus-to-transaction-execution"
title: "Permissioned consensus -> transaction execution"
original_title: "Permissioned consensus -> transaction execution"
file_slug: "permissioned-consensus-to-transaction-execution"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_direction_method_dependency"
bridge_status: "active_seed"
endpoint_paths:
  - "blockchain-systems/consensus/permissioned-blockchain-consensus"
  - "blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution"
endpoint_knowledge_refs:
  - "nahida-knowledge-permissioned-blockchain-consensus"
  - "nahida-knowledge-leaderless-consensus-execution"
from_domain: "blockchain-systems"
to_domain: "blockchain-systems"
from_direction: "consensus"
to_direction: "execution-and-transactions"
from_topic: "permissioned-blockchain-consensus"
to_topic: "leaderless-consensus-execution"
relation_types:
  - "dependency"
  - "co_evolution"
  - "implementation_reuse"
  - "tension"
directionality: "two_way_with_execution_depending_on_consensus_structure"
relationship_thesis: "Permissioned consensus determines the block/instance/order structure that transaction execution must respect. TELL shows that execution can exploit leaderless consensus instance status, block-producing intervals, and deterministic ordering boundaries to reduce commit waiting and merge conflicts, while consensus safety remains outside the execution protocol."
transferability: "medium"
non_transfer_boundary: "Consensus safety/liveness proofs, quorum assumptions, validator membership, and Byzantine resilience do not transfer from transaction execution. TELL's SHT, speculative execution, merging, and DCE are execution-layer optimizations that require a deterministic consensus output and consensus-confirmed timing/order metadata."
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
domains:
  - "blockchain-systems"
topics:
  - "permissioned-blockchain-consensus"
  - "leaderless-consensus-execution"
  - "transaction-processing"
  - "consensus-execution co-design"
source_note_refs:
  - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
  - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
knowledge_refs:
  - "nahida-knowledge-permissioned-blockchain-consensus"
  - "nahida-knowledge-leaderless-consensus-execution"
query_keys:
  - "consensus execution co-design"
  - "permissioned consensus to transaction execution"
  - "leaderless consensus transaction execution"
  - "TELL"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-tell-leaderless-consensus-execution"
source_refs:
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
confidence: "high"
trust_tier: "primary"
---

# Permissioned consensus -> transaction execution

## 命名与路径

- Original title: Permissioned consensus -> transaction execution
- File slug: `permissioned-consensus-to-transaction-execution`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

`blockchain-systems/consensus/permissioned-blockchain-consensus` 关注许可链中 CFT/BFT/leaderless/multi-instance consensus 如何排序区块并提供 finality。`blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution` 关注在这种多实例 ordering 结构之上，执行层如何处理并行执行、乱序 block、跨实例冲突和 commit latency。

这个 bridge 不是把 consensus 和 execution 合并成同一个节点，而是记录二者的依赖和张力: consensus 输出 block/instance/order/timestamp 等结构，execution 必须保持确定性；execution 可以减少等待和冲突开销，但不能替代 consensus 的 safety/liveness 论证。

## 连接命题

- From: `blockchain-systems/consensus/permissioned-blockchain-consensus`
- To: `blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution`
- Relation types: dependency, co_evolution, implementation_reuse, tension
- Directionality: `two_way_with_execution_depending_on_consensus_structure`
- Relationship thesis: Permissioned consensus determines the block/instance/order structure that transaction execution must respect. TELL shows that execution can exploit leaderless consensus instance status, block-producing intervals, and deterministic ordering boundaries to reduce commit waiting and merge conflicts, while consensus safety remains outside the execution protocol.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | `blockchain-systems/consensus/permissioned-blockchain-consensus` | consensus instances, leaderless/multi-leader structure, block-producing intervals, ordering/finality boundary | SRaft/Stretch-BFT existing node; TELL uses RCC+PBFT as experimental consensus setting | active_seed |
| [[leaderless-consensus-execution|Leaderless consensus execution]] | `blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution` | execution scheduling, speculative execution, inter-instance merging, DCE | TELL source note | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Consensus instance status | execution scheduling and merge timing | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] §1-§4 | The execution layer observes/uses instance behavior; it does not change consensus safety. |
| Deterministic ordering boundary | local execution and re-execution | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] §3-§4 | Requires every node to derive the same order/visibility rules. |
| Multi-instance parallelism | per-instance independent execution | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] §4 | Cross-instance conflicts still need deterministic merging. |
| Workload/instance adaptivity | dynamic commitment epoch | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] §4.F | Needs consensus-confirmed timestamps and threshold checks; not a general wall-clock assumption. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Leaderless consensus instance model | `blockchain-systems/consensus/permissioned-blockchain-consensus` | `blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution` | Treat each consensus instance as an independent execution stream before deterministic merge. | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | If consensus protocol has different ordering/finality semantics, execution protocol must be rechecked. |
| Block-producing interval | consensus runtime metadata | Dynamic Commitment Epoch | Compute DCE from confirmed timestamps/intervals to reduce waiting. | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | Malicious timestamp or weak clock assumptions require protocol safeguards. |
| Conflict metadata | execution layer | merge/re-execution control | Use SHT bucket intersections to detect cross-instance conflicts. | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | High skew and many instances increase abort rate and latency. |

## 类比、依赖或关系边界

TELL exposes a useful cross-layer pattern: if consensus has parallelism, execution should not blindly collapse it back into a fixed global epoch. However, this bridge has a hard boundary. Consensus proves or assumes agreement on blocks/order; execution optimizes how local state transitions are produced from that order. If a future source changes the consensus model, the bridge should be refreshed rather than reusing TELL's DCE/SHT unchanged.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus]] | direct evidence for consensus-aware transaction execution under leaderless consensus | active_seed |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | endpoint context for permissioned multi-instance/workload-adaptive consensus; not direct execution evidence | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `blockchain-systems/consensus/permissioned-blockchain-consensus` | add reciprocal Bridge Links and relation edge | active_seed |
| `blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution` | add bridge as primary cross-direction relation | active_seed |

## 查询入口

- consensus execution co-design
- permissioned consensus to transaction execution
- leaderless consensus transaction execution
- TELL / State Hash Table / Dynamic Commitment Epoch

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: Nezha, SChain, RCC/MIR-BFT execution, DAG/blockchain execution, parallel EVM, or permissioned-chain source changes endpoint assumptions or transfer boundary.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | Bridge Links, relation graph, source extension boundary | TELL is not a consensus protocol but depends on permissioned leaderless consensus structure | active_seed |
| [[execution-and-transactions|Blockchain execution and transactions]] | New direction and bridge link | TELL activates execution layer as its own direction | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Methods, child node, bridge link | TELL adds consensus-aware transaction processing route | active_seed |
| [[leaderless-consensus-execution|Leaderless consensus execution]] | Primary bridge endpoint | Bridge explains dependency on permissioned consensus | active_seed |

## 刷新规则

- Last checked: `2026-06-20`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
