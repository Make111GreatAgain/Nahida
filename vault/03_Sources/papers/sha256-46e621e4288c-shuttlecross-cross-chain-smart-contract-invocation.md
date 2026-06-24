---
id: "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
title: "ShuttleCross: An Efficient Cross-Chain Smart Contract Invocation Framework"
original_title: "ShuttleCross: An Efficient Cross-Chain Smart Contract Invocation Framework"
source_kind: "paper"
source_type: "academic_paper"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
status: "absorbed"
lifecycle: "active"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
file_slug: "sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation"
authors:
  - "Rongkai Zhang"
  - "Qiuyu Ding"
  - "Shengjie Guan"
  - "Pengze Li"
  - "Shenglin Yin"
  - "Zhen Xiao"
  - "Jieyi Long"
  - "Mingchao Wan"
  - "Sen Liu"
  - "Jin Dong"
year: 2025
venue: "IEEE Transactions on Services Computing (manuscript proof)"
doi: ""
arxiv_id: ""
url: ""
local_pdf_path: "~/Desktop/paper/TSC-2025-05-0651_Proof_hi (1).pdf"
raw_text_path: "vault/02_Raw/pdf/extracted/tsc-2025-05-0651_proof_hi-1-46e621e4288c-pages.txt"
pdf_sha256: "46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
pages: 13
primary_domain: "blockchain-systems"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation"
secondary_ontology_paths:
  - "blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions"
  - "blockchain-systems/execution-and-transactions/transaction-processing"
  - "distributed-systems/transaction-processing/distributed-transactions"
knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
  - "nahida-knowledge-blockchain-interoperability"
  - "nahida-knowledge-cross-chain-protocols"
  - "nahida-knowledge-cross-chain-smart-contract-invocation"
  - "nahida-knowledge-atomic-cross-chain-transactions"
  - "nahida-knowledge-blockchain-transaction-processing"
  - "nahida-knowledge-distributed-transactions"
bridge_refs:
  - "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
  - "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
topics:
  - "cross-chain smart contract invocation"
  - "cross-chain transactions"
  - "two-phase commit"
  - "hybrid concurrency control"
  - "strict two-phase locking"
  - "optimistic concurrency control"
  - "read-write separation"
  - "serializability"
  - "ChainMaker"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "blockchain-systems/interoperability"
  - "cross-chain-smart-contract-invocation"
freshness_status: "fresh"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_id: "nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0068"
confidence: "high"
trust_tier: "primary"
---

# ShuttleCross: An Efficient Cross-Chain Smart Contract Invocation Framework

## Source Identity

- Source: Zhang et al. "ShuttleCross: An Efficient Cross-Chain Smart Contract Invocation Framework." IEEE Transactions on Services Computing manuscript proof, 2025.
- DOI/arXiv: not recorded in the PDF text or metadata.
- Manuscript ID: `TSC-2025-05-0651`.
- Local PDF: `~/Desktop/paper/TSC-2025-05-0651_Proof_hi (1).pdf`.
- Extraction: existing extracted text `tsc-2025-05-0651_proof_hi-1-46e621e4288c-pages.txt`, readable across cover plus paper pages.

## One-Sentence Summary

ShuttleCross is a cross-chain smart contract invocation framework that uses origin-chain-coordinated 2PC for atomicity, hybrid OCC/S2PL concurrency control for serializability and lower abort rates, and dual-processing read-write separation to reduce latency for read-only cross-chain invocations.

## Absorption Decision

This paper should not become a top-level ShuttleCross knowledge node. Its reusable layer is [[cross-chain-smart-contract-invocation|cross-chain smart contract invocation]]: the problem of executing multi-step smart contract logic across several independent blockchains while preserving atomicity, serializability, liveness and performance.

The paper also strengthens three adjacent nodes:

- [[atomic-cross-chain-transactions|Atomic cross-chain transactions]], because ShuttleCross uses a 2PC-style commit/abort decision for all invocations in one cross-chain transaction.
- [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]], because its HCC mechanism is a blockchain-specific concurrency-control route.
- [[distributed-transactions|Distributed transactions]], because 2PC, S2PL, OCC, commit/abort and serializability vocabulary are translated into a multi-chain execution setting.

## Problem Framing

The paper starts from a service-computing example: a loan workflow spans bank, market, supply and asset blockchains. A bank-chain function invokes market-chain and supply-chain checks, then invokes an asset-chain mortgage function before transferring funds. This is more expressive than token transfer or atomic swap: cross-chain logic can call multiple contracts, trigger sub-invocations and depend on returned values.

The required properties are:

| Property | Meaning in this paper | Why it matters |
| --- | --- | --- |
| Atomicity | All invocations in the same cross-chain transaction commit or all abort. | A loan or service workflow cannot leave some chains updated and others rolled back. |
| Serializability | Concurrent cross-chain transactions should behave as if executed in a serial order. | Multiple cross-chain transactions may read/write the same on-chain state. |
| Liveness | A cross-chain transaction should eventually terminate as commit or abort. | Inter-chain message loss or origin/target delay should not leave target chains waiting forever. |
| Performance | Cross-chain invocation should avoid high abort rates and long consensus-wait latency. | Existing 2PC/OCC/S2PL routes can be correct but inefficient. |

The two performance challenges are:

- A single concurrency-control strategy is not robust: S2PL loses concurrency under low contention; OCC causes high abort rates under high contention.
- Every cross-chain invocation normally waits in the target-chain transaction pool and consensus path, which stretches multi-step transaction latency.

## Related Work Position

The paper categorizes cross-chain smart contract invocation routes into three families:

| Family | Examples in paper | What it provides | Limitation identified by ShuttleCross |
| --- | --- | --- | --- |
| RPC-like invocation | TrustCross, Cosmos/IBC, Polkadot/XCMP | Origin-chain contract asynchronously invokes a target-chain function and receives callbacks. | Lacks atomicity for complex cross-chain transaction execution. |
| 2PC-based invocation | 2PC4BC, GPACT | A client or chain acts as 2PC manager and coordinates target chains with lock or read/write-set records. | Existing variants rely on a single concurrency-control strategy and can have high latency/abort rates. |
| Smart contract portability | Westerkamp/SmartSync, Canton | Migrates contracts and states to a single blockchain so local transaction atomicity applies. | Requires compatible participating chains and adds inter-chain migration overhead. |

For concurrency control, the paper uses 2PC4BC/GPACT as S2PL-style baselines, and EOVPC/Avalon as OCC-style baselines. ShuttleCross's claim is not that one strategy dominates; it dynamically maps different states to different strategies.

## System Model

The system contains a finite set of blockchains `B1...Bn`.

- Each blockchain runs a Byzantine-fault-tolerant consensus protocol.
- Each chain has `N` consensus nodes and tolerates at most `f` Byzantine nodes, with `N >= 3f + 1`.
- A secure PKI and signature scheme allow verification of signatures generated by each chain's consensus committee.
- The network is partially synchronous. After GST, honest-node messages arrive within a bounded delay `Delta`.
- Inter-chain messages finalized on a source chain are sent to at least `f + 1` target-chain nodes through a peer-to-peer network.

In a cross-chain transaction `CTX`, the origin chain is where the user submits the transaction. Target chains execute invoked functions. A transaction is modeled as `CTX := {invoke_i | i = 1..k}` and succeeds only if all invocations execute and commit on their respective chains.

## ShuttleCross Design

### 2PC Atomicity

ShuttleCross uses the origin chain as coordinator.

Phase 1:

- The origin chain executes the cross-chain transaction and emits events containing invocation parameters.
- Target chains execute requested invocations.
- If an invocation writes state, the modified state is stored as cached dirty state instead of being committed immediately.
- Target chains return execution results to the origin chain.
- Target chains may themselves trigger sub-invocations, so workflows can be recursive or multi-step.

Phase 2:

- If every invocation succeeds, the origin chain sends commit to all target chains.
- If any invocation fails, the origin chain sends abort.
- On abort, target chains revert cached dirty states.

The paper's liveness mechanism is timeout/status polling:

- The origin chain uses block-height timers. If expected execution results do not arrive, it aborts.
- If target chains have executed an invocation but do not receive a commit/abort decision, they repeatedly query the origin chain until they obtain the final decision.

### Hybrid Concurrency Control

HCC classifies states into:

| State type | Concurrency strategy | Intended contention regime |
| --- | --- | --- |
| `occState` | Optimistic concurrency control with an append-only `opList`. | Low contention, where speculative execution improves concurrency. |
| `lockState` | Strict two-phase locking with a `lockList`. | High contention, where locks reduce cascading aborts. |

Each state starts as an `occState`.

For `occState`:

- Each state maintains an append-only `opList` of read/write operations and intermediate values.
- Invocations on `occState` execute immediately.
- Write operations get monotonically increasing versions; reads inherit the most recent preceding version.
- An operation can commit only when all preceding operations in its `opList` have committed.
- If a newly appended operation exposes a read-write conflict, the affected cross-chain transaction is aborted and the state is converted to `lockState`.

For `lockState`:

- Invocations acquire read/write locks using S2PL.
- Read locks can be shared; write locks are exclusive.
- Unlike 2PC4BC/GPACT-style immediate abort, failed lock acquisition is placed in a per-state `lockList`.
- When a transaction commits and releases locks, queued invocations are moved to `ReExecList` and re-executed in the next block.

This `lockList` design is the paper's main change to high-contention S2PL: it delays execution until lock availability instead of immediately aborting the whole cross-chain transaction.

### Deadlock Detection

HCC can still introduce waits through both `opList` dependencies and `lockList` lock waits. ShuttleCross periodically builds transaction wait-for graphs:

- Vertices are cross-chain transactions.
- Edges are wait-for relationships.
- Chains exchange local graphs and build a complete transaction wait-for graph.
- If a cycle is found, the most recent transaction in the cycle is aborted, and its origin chain initiates the abort.

Timeouts would eventually terminate deadlocks, but explicit cycle detection reduces waiting overhead.

### Dynamic State Classification

State conversion is local and recent-contention-driven:

- `occState -> lockState`: if a transaction aborts due to a conflict while accessing the state, the paper infers recent high contention and switches the state to `lockState`.
- If an `occState` has uncommitted operations in its `opList`, conversion waits until these operations commit before processing `lockList`.
- `lockState -> occState`: if the state does not hold any write lock and receives no write-lock requests within `lambda` blocks, the paper infers lower contention and converts it back.
- During conversion back to OCC, existing read locks are converted into read operations and added to the `opList`.

The evaluated best threshold in one setting is `lambda = 10` blocks, but the paper treats it as workload-dependent.

### Read-Write Separation

Read-only cross-chain invocations call functions that read `occState` and do not modify on-chain state. ShuttleCross accelerates them by bypassing target-chain transaction-pool waiting and consensus on the fast path.

The final design is dual-processing:

1. Target-chain nodes execute the read-only invocation off-chain immediately and return `readResult = (ctxId, output, readSet)` to the origin chain.
2. The same read-only invocation also enters the target-chain transaction pool for formal on-chain execution.
3. When formal execution appends read operations to `opList`, it produces official versions.
4. If official versions match the versions in the off-chain `readResult`, the origin chain can commit the cross-chain transaction.
5. If versions mismatch, some state changed before the read-only invocation became visible, so the cross-chain transaction aborts.

The origin chain accepts the off-chain read result only after receiving `2f + 1` matching return values. If it cannot get enough matching responses, it waits for the official on-chain result; the read-only invocation then effectively falls back to the normal path.

The subtle point is visibility: the off-chain result can accelerate dependent invocations, but the invocation must still become visible in the target-chain order before commit, otherwise later transactions could commit before it and break serializability.

## Correctness Arguments

The paper proves three properties:

| Lemma | Claim | Proof intuition |
| --- | --- | --- |
| Lemma 1 | ShuttleCross guarantees atomicity. | The origin chain makes exactly one final decision for a `CTX`; target chains commit or abort based on that decision. |
| Lemma 2 | ShuttleCross guarantees liveness. | Missing invocation requests or execution results trigger origin timeout and abort; missing final decisions cause target chains to poll the origin until they learn commit/abort. |
| Lemma 3 | HCC schedules are serializable. | In the conflict graph, an edge `CTX_i -> CTX_j` implies `CTX_i` commits before `CTX_j`; a cycle would require contradictory commit order. |

These arguments cover protocol-level correctness under the stated partial synchrony and BFT-chain assumptions. They do not prove performance under arbitrary workload skew; that is evaluated experimentally.

## Implementation

The prototype is implemented on ChainMaker.

Implementation components include:

- A state management contract implementing `opList` and `lockList`.
- A cross-chain management contract coordinating cross-chain transaction execution.
- ChainMaker chains with TBFT consensus in the reported experiments.

The evaluation environment uses 32 physical machines, each with 16 Intel Xeon Platinum CPU cores and 64 GB RAM. Each blockchain has 10 nodes. The network is configured with 50 Mbps bandwidth, 100 ms latency on all communication links, 1 second block intervals and up to 1000 transactions per block. Clients inject 1000 cross-chain transactions per second to each chain.

## Evaluation

Metrics:

- Throughput: cross-chain transactions committed per second by each chain.
- Latency: time from client submission to transaction commit; aborted transactions are excluded.
- Abort rate: fraction of cross-chain transactions aborted.

Baselines:

| Baseline | Role |
| --- | --- |
| 2PC4BC | S2PL-based cross-chain coordination baseline. |
| Avalon | OCC-based baseline using version validation without locks. |
| ShuttleRW | ShuttleCross variant with HCC but without read-write separation. |

Datasets:

- Synthetic contracts with read/write functions; 50% of functions are read-only.
- Contention is varied by changing the number of accessible states.
- Realistic cross-chain transaction data generated with XChainDataGen from Ethereum, Avalanche, Binance Smart Chain, Arbitrum, Base, Optimism, Linea and Polygon for October 1 to December 31, 2024, totaling about 4 million generated cross-chain transactions.

Main results:

| Scenario | Result |
| --- | --- |
| No state contention | For 16 chains, ShuttleCross reduces latency by 28% and increases throughput by 26% compared with ShuttleRW, showing the benefit of read-write separation. |
| Varying read-only function ratio | Higher read-only percentage lowers latency and raises throughput, consistent with the off-chain fast path. |
| Threshold `lambda` | In the reported 16-chain, 3000-state setting, `lambda = 10` gives highest throughput. Too small keeps states mostly optimistic and raises aborts; too large keeps them locked too long and hurts concurrency. |
| State contention | ShuttleCross has lower abort rate than 2PC4BC/Avalon because it combines HCC and `lockList` queueing; compared with 2PC4BC it reduces latency by up to 36% and increases throughput by up to 46%. |
| Realistic cross-chain data | Compared with ShuttleRW, ShuttleCross reduces latency by up to 24% and raises throughput by up to 31%; compared with Avalon, latency improves by up to 36% and throughput by up to 47%; compared with 2PC4BC, latency improves by up to 55% and throughput by up to 56%. |
| Robustness | Under dropped cross-chain messages, all transactions eventually commit or abort consistently, but latency rises with higher drop percentage due to polling and timeouts. |

## Limitations and Boundaries

- The PDF is a manuscript proof; no DOI is recorded in the local text or metadata.
- ShuttleCross relies on BFT-secure chains, PKI, committee signatures, partial synchrony and bounded post-GST communication.
- Origin-chain coordination is a central protocol role. The paper handles liveness with timeout/status polling, but this is not the same as a permissionless witness network or fully decentralized atomic-commit service.
- Read-write separation accelerates only read-only invocations over `occState`; modifying invocations and high-contention `lockState` accesses remain on the normal path.
- Off-chain read results are safe only with `2f + 1` matching outputs and later official-version matching.
- The ChainMaker/TBFT prototype and synthetic/realistic generated datasets are strong evaluation evidence, but production heterogeneous-chain deployment would add finality, fee, relayer and contract-language compatibility concerns.
- HCC state classification uses recent contention heuristics; workload shifts can make `lambda` tuning important.

## Knowledge Handoff

| Target | Update |
| --- | --- |
| [[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]] | New problem node: multi-chain smart-contract workflows need atomicity, serializability, liveness and low-latency invocation. |
| [[cross-chain-protocols|Cross-chain protocols]] | Add CCSCI as child under interoperability, distinct from atomic swaps, bridges, relayers and dynamic data consistency. |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Add HCC/dual-processing read-only invocation as a transaction-processing route with cross-chain scope. |
| [[distributed-transactions|Distributed transactions]] | Add ShuttleCross as adaptation evidence for 2PC, S2PL/OCC and serializability in independent blockchain settings. |
| [[distributed-transactions-to-cross-chain-smart-contract-invocation|Distributed transactions -> cross-chain smart contract invocation]] | New bridge: 2PC/OCC/S2PL vocabulary transfers, but origin-chain coordination, BFT-chain signatures and on-chain visibility change the boundary. |

## Update Log

| Date | Run ID | Change |
| --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation | Deep-read source note created and absorbed into Source + Knowledge + Bridge architecture. |
