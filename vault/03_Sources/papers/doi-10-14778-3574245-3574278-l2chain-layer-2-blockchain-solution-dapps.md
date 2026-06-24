---
id: "doi:10.14778/3574245.3574278"
title: "L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications"
original_title: "L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications"
source_kind: "paper"
source_type: "academic_paper"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
status: "absorbed"
lifecycle: "active"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
file_slug: "doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps"
authors:
  - "Zihuan Xu"
  - "Lei Chen"
year: 2022
venue: "Proceedings of the VLDB Endowment, Vol. 16, No. 4"
doi: "10.14778/3574245.3574278"
arxiv_id: ""
url: "https://doi.org/10.14778/3574245.3574278"
artifact_urls:
  - "https://github.com/xzhflying/L2chain"
local_pdf_path: "~/Desktop/paper/VLDB 2023 L2 Chain.pdf"
raw_text_path: "vault/02_Raw/pdf/extracted/vldb-2023-l2-chain-ca9ee606e039-pages.txt"
pdf_sha256: "ca9ee606e039da81c81263b7cc1e0ff772c78151498455e78f9a4de1b74f512d"
pages: 14
primary_domain: "blockchain-systems"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing"
secondary_ontology_paths:
  - "blockchain-systems/data-management-and-storage/blockchain-state-storage"
  - "blockchain-systems/scaling-and-sharding"
  - "blockchain-systems/execution-and-transactions/smart-contract-execution"
knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
  - "nahida-knowledge-blockchain-execution-and-transactions"
  - "nahida-knowledge-blockchain-transaction-processing"
  - "nahida-knowledge-blockchain-data-management-and-storage"
  - "nahida-knowledge-blockchain-state-storage"
  - "nahida-knowledge-scaling-and-sharding"
  - "nahida-knowledge-smart-contract-execution"
bridge_refs:
  - "nahida-bridge-blockchain-state-storage-to-transaction-processing"
topics:
  - "layer-2 blockchain scaling"
  - "blockchain transaction processing"
  - "confidential DApp execution"
  - "split-execute-merge workflow"
  - "RSA accumulator"
  - "state digest commitment"
  - "witness cache"
  - "trusted execution environment"
  - "rollback attack mitigation"
  - "off-chain smart-contract execution"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "blockchain-systems"
  - "transaction-processing"
  - "layer-2"
  - "state-storage"
freshness_status: "fresh"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_id: "nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0117"
confidence: "high"
trust_tier: "primary"
---

# L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications

## Source Identity

- Source: Xu and Chen. "L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications." PVLDB 16(4), 2022.
- DOI: `10.14778/3574245.3574278`.
- Artifact signal: the PDF lists `https://github.com/xzhflying/L2chain`; the repository was not analyzed in this intake.
- Local PDF: `~/Desktop/paper/VLDB 2023 L2 Chain.pdf`.
- Extraction: `pypdf` text extraction, 14 pages. Pages 5-6 had weak text extraction, so they were rendered and visually checked; they contain the threat model, current L2 limitations, L2chain architecture, layer-1 ledger layout, and the SEM workflow figure.
- Metadata correction: the queue/file label says `VLDB 2023`, but the PDF reference line says `PVLDB, 16(4): 986-999, 2022`; this note records year `2022` and venue `PVLDB`.
- Queue correction: the DOI had been detected correctly, while the queue's arXiv-like value came from the DOI suffix and is not an arXiv ID.

## One-Sentence Summary

L2chain scales DApp transaction processing by letting DApps execute ordered encrypted batches in a layer-2 network, while layer-1 validators keep only compact state digests, split and merge affected state subsets through an RSA accumulator, and rely on TEE-backed two-step execution to prevent rollback-based privacy and consistency attacks.

## Abstract-Level Contribution

The paper frames DApps as needing three properties at once: high throughput, transaction confidentiality, and security of execution/order correctness. Its proposed framework has four linked contributions:

- A layer-2 architecture where DApps process transactions off-chain and layer-1 keeps only state digests and integrity evidence.
- A split-execute-merge transaction workflow that uses an RSA accumulator to lock and update only the affected state subset.
- A witness cache that reduces RSA membership witness generation overhead for DApp executors.
- A TEE-backed two-step execution process that first simulates ordered batches to determine read/write sets and then executes after the split transaction is committed on-chain, preventing rollback attacks from breaking privacy or state consistency.

This places the paper primarily under [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]], with a strong bridge to [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain state storage]].

## Problem Framing

L2chain is not just another rollup-style or sidechain-style scaling paper. Its core problem is the boundary between transaction execution and state commitment:

- Layer-1 consensus is a throughput bottleneck if every DApp transaction must be ordered and executed directly on-chain.
- Existing L2 designs can still expose transaction contents to executors or validators, weakening confidentiality.
- If L2 executors can choose or replay execution order, a rollback attack can leak private transaction behavior or produce inconsistent L1/L2 states.
- If the on-chain state digest is represented by a Merkle Patricia Trie root, parallel state-subset updates are difficult because DApps contend on the same root and may need to reveal too much state-update material.

The reusable insight is that off-chain execution cannot be designed independently from the state commitment. L2chain changes the commitment format to let independent DApp batches split state subsets, execute in TEEs, and merge updated digests back to L1.

## Threat Model and Challenges

The paper assumes nodes in both layers may behave maliciously.

| Actor | Threat | L2chain response |
| --- | --- | --- |
| Layer-1 validators | A validator may crash or try to subvert ledger consistency. | L2chain inherits the chosen L1 consensus protocol and lets validators process state digests rather than private transaction contents. |
| Layer-2 executors | Executors may deviate from service-level agreements, execute wrong code, ignore transaction order, or try rollback attacks. | DApp SLAs define code/authority/consensus rules; TEE simulation and execution signatures bind order, read/write sets and committed state inputs. |
| Cross-DApp workload | Different DApps may try to split overlapping state subsets concurrently. | L1 validators discard conflicting split transactions so each available L1 state is split at most once per L1 block. |

The paper highlights three design challenges:

- L1 validators no longer keep all system states or actual L2 transaction contents, so they need compact evidence for state updates.
- Confidential transactions require protection from both L1 and L2 nodes, including rollback attacks against TEE black-box execution.
- State consistency must be maintained between L1 and L2 even though DApps process batches independently.

## System Architecture

L2chain uses an account-based state model. Each state is an address-value pair, and DApps are deployed through layer-1 smart contracts with service-level agreements. These SLAs specify:

- DApp business logic and executable code,
- which on-chain states a DApp can access or update,
- which consensus protocol the DApp executors use,
- how the consensus result should be verified.

The architecture has two layers:

| Layer | Responsibility | Stored data |
| --- | --- | --- |
| Layer-1 blockchain | Maintains the ledger, consensus metadata, DApp contracts/SLAs, split and merge transactions, and available-state digest. | Compact digest of available states plus Merkle roots for split/merge transaction sets. |
| Layer-2 DApps | Order transactions with DApp-specified consensus, execute encrypted transactions inside TEEs, and submit split/merge transactions. | Local states accessible to the DApp, encrypted if privacy requires it, and witness caches for state digest operations. |

Transactions are either intra-DApp or inter-DApp. Intra-DApp transactions can be handled within one DApp's executor group. Inter-DApp transactions require cross-app SLAs on L1 and then execution by involved DApps in the L2 network.

## State Commitment Route

The paper's main state-storage move is to replace an MPT-style state root with an RSA accumulator digest for available states.

For every state `S_i`, L2chain hashes the address-value pair into a prime and accumulates all currently available states:

```text
D = g ^ product(H_p({S_i, S_i.v}))
```

This removes the structural coupling of an MPT root. Instead of requiring a DApp update to expose or recompute a large trie path, executors can:

1. Generate a membership witness for the subset of states they want to process.
2. Submit a split transaction proving that the subset is currently included in the available-state digest.
3. Execute the batch off-chain.
4. Submit a merge transaction with the updated subset digest.

For the knowledge base, this is a direct source extension to [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain state storage]]: state commitments are not merely a storage detail; they determine which transaction-processing protocol is possible.

## Split-Execute-Merge Workflow

L2chain's split-execute-merge workflow has three phases.

### Split Phase

L2 executors collect user transactions, categorize them into intra-DApp and inter-DApp transactions, and order them using the consensus protocol specified by DApp SLAs. The ordered batch is organized as a Merkle tree whose root is signed by involved executors.

Executors then simulate the batch in a TEE to obtain read/write sets and a TEE simulation signature. They build an L1 split transaction containing:

- affected states `S_T`,
- digest `D_T` for those states,
- membership witness `w_T`,
- transaction Merkle root `T_root`,
- TEE simulation proof/signature.

L1 validators verify the DApp's authority over the states and check membership in the current available-state digest. If two split transactions try to split overlapping states in the same L1 block, at least one is discarded.

### Execute Phase

After the split transaction is committed on L1, L2 executors obtain the block header and L1 consensus proof showing that the split transaction is included in a block. The TEE executes the ordered batch using the committed input states and produces:

- updated state set `S_T'`,
- updated digest `D_T'`,
- TEE execution correctness proof/signature.

The important boundary is timing: execution happens after L1 has committed the split transaction. This prevents an executor from repeatedly rolling back and probing private state transitions against uncommitted input states.

### Merge Phase

Executors submit an L1 merge transaction containing:

- the hash of the block containing the split transaction,
- the hash of the split transaction,
- updated digest `D_T'`,
- TEE execution proof/signature.

L1 validators retrieve the split transaction, verify integrity and TEE proof, and update the available-state digest. Blocks may contain multiple split and merge transactions; validators aggregate their effects using accumulator operations and record separate Merkle roots for split and merge transaction sets.

The paper also pipelines split and merge transactions to reduce latency by letting L2 executors propagate merge transactions and combine updated digest merging with future splitting.

## Witness Cache

Membership witness generation is expensive without the accumulator trapdoor. L2chain therefore maintains witness caches.

Without a witness cache, the average cost of generating witnesses over `n` accessible states grows with almost all other states. With `tau` cache groups, the paper bounds the amortized witness generation cost by reducing each witness to a smaller group-level operation while paying a block-by-block witness update cost.

The paper gives a cost model:

```text
cost_without_cache = alpha * (n - 1) * sum(f_i)
cost_with_cache = alpha * (n / tau - 1) * sum(f_i) + beta * tau
```

The optimal cache group count is derived from this tradeoff, and the paper uses dynamic programming to partition states by access frequency. The algorithm sorts states by access frequency, chooses partition points for `tau` cache groups, and reruns or incrementally adjusts when access frequencies change.

For absorption, witness cache is a source-specific optimization. It is not promoted to a standalone knowledge node yet because the vault lacks independent RSA accumulator or accumulator-maintenance sources.

## Two-Step TEE Execution

The two-step execution process exists because encrypted general-purpose transactions have unknown read/write sets until simulated, but executing them before L1 commits the input state gives attackers a rollback oracle.

| Step | Purpose | Key checks |
| --- | --- | --- |
| Simulation in split phase | Determine read/write sets and bind the ordered batch before L1 split. | Verify the batch Merkle root signature and ordering; output `S_T`, `D_T`, and TEE simulation signature. |
| Execution after split commit | Execute the committed ordered batch on committed input states. | Verify L1 consensus proof, split-transaction inclusion, transaction membership, and input-state consistency. |

This design makes TEE execution depend on an L1 commitment boundary. The TEE is not merely a speed or confidentiality component; it is part of an order-correctness and rollback-mitigation protocol.

## Security and Correctness Boundary

L2chain's security argument is a composition of several assumptions:

- L1 consensus must provide block commitment or probabilistic finality depending on the configured protocol.
- DApp SLAs must correctly specify access authority, code, and L2 consensus verification rules.
- TEEs must enforce code integrity and sign only correct simulation/execution statements.
- The accumulator membership and update logic must ensure split subsets and merged digest updates are consistent.
- L1 validators must reject conflicting split transactions on overlapping states in the same block.

The paper does not solve every L2-system problem. It does not replace data availability, does not remove TEE trust assumptions, does not analyze modern rollup validity/fraud proofs, and does not remove state-contention latency. Its narrower contribution is a layer-2 DApp execution workflow where state commitments, TEE-backed execution and L1 split/merge transactions are co-designed.

## Evaluation

The evaluation compares L2chain against Quorum, a CAPER-based cross-DApp permissioned blockchain, and SlimChain.

| Evaluation dimension | Details |
| --- | --- |
| Workload | BLOCKBENCH KVStore smart contract with YCSB read-write, read-only, and write-only mixes. |
| DApp count | 4, 8, 16, 32 DApps; each DApp has four nodes. |
| Consensus | Raft for permissioned L1 and L2 local consensus; PoW for permissionless L1 with Raft inside L2. |
| State count | `2^26` states, approximating unique Ethereum address scale in the paper's setting. |
| Witness cache parameters | `tau` values 256, 512, 1024, 2048; multi-threaded cache maintenance. |
| Environment | Microsoft Azure Standard_DC16s_v3 machines with 1500 Mbps network bandwidth. |

Reported results:

- In permissioned settings, L2chain-R improves throughput by 1.5x-2.6x over the CAPER-based baseline and 21.9x-42.2x over Raft Quorum.
- In permissionless settings, L2chain-P improves throughput by 7.1x-8.9x over PoW Quorum and 1.7x-2.2x over SlimChain.
- Compared with Raft Quorum, L2chain saves 63%-75% processing time.
- L2chain has higher latency than CAPER, PoW Quorum and PoW SlimChain in the reported breakdowns because RSA accumulator operations and cross-DApp consensus add overhead.
- Multi-threaded witness-cache maintenance reduces overhead.

The paper's evaluation should be read as evidence for this particular design envelope, not as a general proof that all L2 architectures dominate L1 execution. Its gains come with TEE assumptions, accumulator overhead and workload-dependent contention.

## Comparison to Adjacent Sources

| Source | Similarity | Difference |
| --- | --- | --- |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | Both reduce consensus-node state/execution burden and use off-chain execution with authenticated state commitments. | SlimChain keeps consensus nodes stateless with off-chain storage nodes and partial Merkle trie/write proofs; L2chain organizes DApp execution as SEM split/merge over an RSA accumulator and adds rollback-resistant TEE two-step execution. |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] | Both use TEE-backed off-chain execution for smart-contract workloads and authenticated state inputs. | LightCross is about cross-shard smart-contract execution with R-shard/S-shard validation; L2chain is about layer-2 DApp transaction processing and L1 state digest split/merge. |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] | Both touch blockchain scaling and commitments. | Fraud Proofs focuses on data availability/fraud proof light-client security; L2chain focuses on confidential DApp execution and state-subset digest updates, not DA sampling or fraud-proof architecture. |

## Knowledge Absorption Routing

| Target | Action | Rationale |
| --- | --- | --- |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Add layer-2 SEM route and L2chain representative source. | L2chain changes how DApp transactions are ordered, split, executed, conflict-checked and committed. |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain state storage]] | Add RSA-accumulator state-subset commitment route. | State digest design is the mechanism that makes parallel split/merge transaction processing possible. |
| [[05_Bridges/blockchain-state-storage-to-transaction-processing|Blockchain state storage -> transaction processing]] | Strengthen bridge with L2chain evidence. | The paper directly demonstrates that a commitment format can constrain or enable transaction-processing protocols. |
| [[04_Knowledge/blockchain-systems/scaling-and-sharding|Scaling and sharding]] | Add only as source extension, not a child split. | L2chain is layer-2 scaling rather than validator sharding; current node should note the route without pretending the vault has a full rollup/L2 foundation. |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/smart-contract-execution|Smart contract execution]] | Treat as secondary/supporting evidence. | TEE executes DApp transactions, but the paper's primary novelty is transaction processing plus state commitment, not VM semantics. |

## Source-Level Takeaways

| Takeaway | Evidence anchor | Confidence | Absorption status |
| --- | --- | --- | --- |
| Layer-2 DApp execution can be framed as a state-subset split/execute/merge protocol rather than only as global batch posting. | Abstract, §3-§4 | high | absorbed into transaction-processing |
| RSA accumulators allow affected state subsets to be split from and merged into an available-state digest, avoiding MPT structural contention for this protocol. | §3.2-§5, pages 5-9 | high | absorbed into state-storage and bridge |
| Confidential off-chain execution needs an order/finality boundary; TEE alone is vulnerable to rollback-style probing. | §2.1, §6 | high | absorbed into source note and transaction-processing route |
| Witness cache reduces accumulator witness overhead but remains a source-specific optimization until more accumulator-maintenance sources exist. | §5 | medium-high | kept in source note |
| L2chain improves throughput in the paper's setup but adds RSA/cross-DApp latency and relies on TEE assumptions. | §7 | high | absorbed as limits |

## Open Review Notes

- The paper's code repository was not analyzed; implementation details in this note come only from the PDF.
- The technical report referenced by the paper was not read.
- The vault still lacks a foundation node for RSA accumulators and a broader layer-2/rollup architecture foundation. L2chain should not be treated as a complete L2 taxonomy source by itself.
- Pages 5-6 were visually checked because text extraction was incomplete; no OCR transcript was generated for those pages.

