---
id: "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
title: "Distributed transactions -> cross-chain smart contract invocation"
original_title: "Distributed transactions -> cross-chain smart contract invocation"
file_slug: "distributed-transactions-to-cross-chain-smart-contract-invocation"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_domain_method_translation"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/transaction-processing/distributed-transactions"
  - "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation"
endpoint_knowledge_refs:
  - "nahida-knowledge-distributed-transactions"
  - "nahida-knowledge-cross-chain-smart-contract-invocation"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "transaction-processing"
to_direction: "interoperability"
from_topic: "distributed-transactions"
to_topic: "cross-chain-smart-contract-invocation"
relation_types:
  - "translation"
  - "coordination"
  - "concurrency_control"
  - "trust_model_shift"
directionality: "one_way_with_feedback"
relationship_thesis: "Distributed transaction mechanisms such as 2PC, commit/abort coordination, S2PL, OCC, wait-for graphs and serializability analysis can be translated into cross-chain smart contract invocation, but independent Byzantine ledgers require origin-chain coordination, committee-signature verification, target-chain cached states, timeout/status polling, and on-chain visibility rules for off-chain read results."
transferability: "medium_high"
non_transfer_boundary: "The coordination and concurrency-control vocabulary transfers, but trusted coordinator recovery logs, crash-only failure assumptions, shared lock managers, private database schedules and immediate local visibility do not transfer unchanged. Cross-chain smart contract invocation adds per-chain consensus finality, inter-chain message delay/loss, malicious chain nodes within BFT thresholds, origin-chain decision finality, target-chain transaction-pool/consensus latency, and the need for off-chain read results to become officially visible before commit."
evidence_window_start: "2025"
evidence_window_end: "2025"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "distributed-transactions"
  - "cross-chain-smart-contract-invocation"
  - "two-phase-commit"
  - "serializability"
  - "hybrid-concurrency-control"
source_note_refs:
  - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
knowledge_refs:
  - "nahida-knowledge-distributed-transactions"
  - "nahida-knowledge-cross-chain-smart-contract-invocation"
relation_edges:
  - from: "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
    relation: "connects"
    to: "nahida-knowledge-distributed-transactions"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
    relation: "connects"
    to: "nahida-knowledge-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
query_keys:
  - "distributed transactions cross-chain smart contract invocation"
  - "2PC cross-chain smart contract invocation"
  - "S2PL OCC cross-chain transactions"
  - "hybrid concurrency control cross-chain invocation"
  - "ShuttleCross"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation"
source_refs:
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
confidence: "high"
trust_tier: "primary"
---

# Distributed transactions -> cross-chain smart contract invocation

## 命名与路径

- Original title: Distributed transactions -> cross-chain smart contract invocation
- File slug: `distributed-transactions-to-cross-chain-smart-contract-invocation`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

[[distributed-transactions|Distributed transactions]] 关注一个 logical transaction 跨多个参与方、分区或 shard 时如何保持 atomicity、isolation、serializability 和共同的 commit/abort 结果。[[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]] 关注一条链上的 smart contract workflow 如何调用其他链上的 contract functions，并把这些调用组织成一个可提交或可中止的 cross-chain transaction。

这条 bridge 记录的不是“2PC 原样等于跨链调用协议”。它记录的是更窄的迁移命题: 2PC、S2PL、OCC、wait-for graph、serializability conflict graph 等 transaction-processing 机制可以迁移到 cross-chain smart contract invocation，但必须补上独立 BFT ledgers、origin-chain coordinator、target-chain cached dirty states、committee signatures、timeout/status polling 和 off-chain read result 的链上可见性。

## 连接命题

- From: `distributed-systems/transaction-processing/distributed-transactions`
- To: `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation`
- Relation types: translation, coordination, concurrency_control, trust_model_shift
- Directionality: `one_way_with_feedback`
- Relationship thesis: Distributed transaction mechanisms such as 2PC, commit/abort coordination, S2PL, OCC, wait-for graphs and serializability analysis can be translated into cross-chain smart contract invocation, but independent Byzantine ledgers require origin-chain coordination, committee-signature verification, target-chain cached states, timeout/status polling, and on-chain visibility rules for off-chain read results.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[distributed-transactions|Distributed transactions]] | `distributed-systems/transaction-processing/distributed-transactions` | 2PC, commit/abort, S2PL, OCC, serializability, wait-for graph, deadlock detection | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] as adaptation evidence | active_seed |
| [[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]] | `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | origin-chain-coordinated CCSCI, target-chain cached states, HCC, dual-processing read-only invocation | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| 2PC coordinator decision | origin-chain commit/abort decision | ShuttleCross §IV-B | Origin chain is itself a blockchain; decision visibility/finality and target-chain polling matter. |
| Dirty state before commit | cached dirty state on target chains | ShuttleCross §IV-B | Target chains must revert on abort and commit only after origin decision. |
| S2PL locks | `lockState` with read/write locks and `lockList` | ShuttleCross §IV-C | Unlike database/local lock managers, failed locks can be queued and re-executed in later blocks. |
| OCC operation history | `occState` with append-only `opList` | ShuttleCross §IV-C | Operation order and version visibility are embedded in target-chain state-management contracts. |
| Wait-for graph deadlock detection | cross-chain transaction wait-for graph across chains | ShuttleCross §IV-C.3 | Chains must exchange local graphs; timeout remains fallback. |
| Serializability conflict graph | proof that HCC schedules are acyclic | ShuttleCross §V-C | Commit order is constrained by cross-chain transaction dependencies and chain commits. |
| Read-only fast path | off-chain execution with later official on-chain version | ShuttleCross §IV-D | Off-chain reads can accelerate only if `2f + 1` outputs match and official versions later match. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Atomic commit | `distributed-systems/transaction-processing/distributed-transactions` | `cross-chain-smart-contract-invocation` | origin chain coordinates target-chain invocation results and broadcasts commit/abort | ShuttleCross §IV-B | Origin-chain failure/delay requires timeout and status polling; not a shared recovery log. |
| Isolation via locking | S2PL | `lockState` cross-chain invocation execution | high-contention state uses read/write locks and queues failed lock attempts | ShuttleCross Algorithm 1 | Waiting and re-execution increase latency; deadlock detection needed. |
| Optimistic execution | OCC | `occState` opList execution | low-contention state appends read/write operations and checks read-write conflicts early | ShuttleCross Algorithm 1 | High contention causes cascading aborts and state conversion. |
| Adaptive concurrency control | workload-aware CC selection | HCC state classification | conflict-induced abort converts to lockState; no write-lock request for `lambda` blocks converts back | ShuttleCross §IV-C.4 | Threshold tuning is workload-dependent. |
| Read-only optimization | read-only transaction fast path | off-chain read-only invocation | target-chain nodes execute off-chain first, then formal on-chain execution assigns official versions | ShuttleCross §IV-D | If off-chain and official versions mismatch, CTX must abort. |

## 类比、依赖或关系边界

Distributed transaction concepts provide ShuttleCross's language, but the execution substrate is different. A database participant can often rely on a coordinator/recovery log and a local lock manager; a cross-chain invocation participant is a separate blockchain with its own consensus, transaction pool and finality. ShuttleCross therefore externalizes the coordinator role to the origin chain, stores writes as cached dirty states until the second phase, uses state-management contracts to track `opList`/`lockList`, and relies on timeout/status polling for liveness.

The most important boundary is read visibility. A read-only invocation can execute off-chain first, but this cannot be treated as a committed database read until the invocation also appears in target-chain order with matching versions. This is why ShuttleCross's read-write separation is dual-processing rather than pure off-chain execution.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross: An Efficient Cross-Chain Smart Contract Invocation Framework]] | direct evidence for translating 2PC/OCC/S2PL/serializability into cross-chain smart contract invocation | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/transaction-processing/distributed-transactions` | add bridge link, source extension and method row for cross-chain smart contract invocation adaptation | active_seed |
| `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | new problem node with bridge link and ShuttleCross source extension | active_seed |
| `blockchain-systems/execution-and-transactions/transaction-processing` | add secondary source extension for cross-chain HCC/read-write separation | active_seed |

## 查询入口

- 2PC 如何迁移到 cross-chain smart contract invocation?
- ShuttleCross 为什么需要同时用 OCC 和 S2PL?
- read-only cross-chain invocation 为什么还要进入 target-chain tx pool?
- 跨链合约调用里的 serializability 和数据库 serializability 有什么关系?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: GPACT、2PC4BC、EOVPC、Avalon、IBC/XCMP callback invocation、production CCSCI 或 classic distributed transactions foundation source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[distributed-transactions|Distributed transactions]] | Methods, representative sources, bridge links | ShuttleCross adapts 2PC/OCC/S2PL/serializability to independent blockchain invocations | active_seed |
| [[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]] | New node | ShuttleCross introduces the first direct CCSCI seed source in the vault | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Source extension | HCC/read-write separation are transaction-processing mechanisms in a cross-chain context | active_seed |

## 刷新规则

- Last checked: `2026-06-22`
- Valid until: `2026-07-22`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity；尤其 GPACT/2PC4BC/EOVPC/Avalon、IBC/XCMP callback invocation、heterogeneous-chain finality 或 production relayer/invocation sources。
