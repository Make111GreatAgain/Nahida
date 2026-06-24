---
id: "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
title: "LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts"
original_title: "LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts"
source_kind: "paper"
source_type: "academic_paper"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
status: "absorbed"
lifecycle: "active"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
file_slug: "sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts"
authors:
  - "Xiaodong Qi"
  - "Yi Li"
year: 2024
venue: "unknown_from_pdf"
doi: ""
arxiv_id: ""
url: ""
artifact_urls:
  - "https://sites.google.com/view/infocom24"
local_pdf_path: "~/Desktop/paper/Qi2024LSL.pdf"
raw_text_path: "vault/02_Raw/pdf/extracted/qi2024lsl-565707d2339b-pages.txt"
pdf_sha256: "565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
pages: 13
primary_domain: "blockchain-systems"
primary_ontology_path: "blockchain-systems/execution-and-transactions/cross-shard-transaction-execution"
secondary_ontology_paths:
  - "blockchain-systems/execution-and-transactions/transaction-processing"
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers"
knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
  - "nahida-knowledge-blockchain-execution-and-transactions"
  - "nahida-knowledge-cross-shard-transaction-execution"
  - "nahida-knowledge-blockchain-transaction-processing"
  - "nahida-knowledge-scaling-and-sharding"
  - "nahida-knowledge-sharded-ledgers"
bridge_refs:
  - "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
topics:
  - "cross-shard transaction execution"
  - "smart contract sharding"
  - "blockchain transaction processing"
  - "TEE-assisted off-chain execution"
  - "cross-shard commit protocol"
  - "transaction validation"
  - "smart contract migration"
  - "Merkle proof state authentication"
  - "FISCO-BCOS"
  - "Intel SGX"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "blockchain-systems"
  - "cross-shard-transaction-execution"
  - "sharded-ledgers"
freshness_status: "fresh"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_id: "nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0067"
confidence: "high"
trust_tier: "primary"
---

# LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts

## Source Identity

- Source: Qi and Li. "LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts." 2024.
- DOI/arXiv: not recorded in the PDF text or PDF metadata.
- Venue: not reliably recorded in the local PDF metadata/text. The paper references an appendix URL at `https://sites.google.com/view/infocom24`, but this source note does not treat the venue as verified.
- Local PDF: `~/Desktop/paper/Qi2024LSL.pdf`.
- Extraction: existing extracted text `qi2024lsl-565707d2339b-pages.txt`, 13 pages, readable.

## One-Sentence Summary

LightCross scales smart-contract sharding by moving cross-shard contract execution into TEE-backed off-chain executors, using an R-shard to order and validate execution results in batches, and periodically migrating contracts according to historical co-invocation to reduce the cross-shard transaction ratio.

## Abstract-Level Contribution

The paper argues that cross-shard transaction protocols are a major bottleneck for blockchain sharding, especially for smart contracts whose execution may call multiple contracts and access state across shards. Existing protocols often either handle simple transfer transactions or require multi-round communication among involved shards. LightCross proposes three linked changes:

- Execute cross-shard smart-contract transactions in off-chain executors protected by TEEs.
- Replace multi-round shard-to-shard execution with a lightweight commit/validation protocol coordinated by a dedicated R-shard.
- Reduce the number of cross-shard smart-contract transactions by periodically migrating contracts according to a transaction call graph.

The reported prototype is built on FISCO-BCOS and uses Intel SGX/Occlum executors. In the paper's evaluation, LightCross reaches up to 4x throughput over ByShard, 1.6x over RingBFT in one scaling experiment, and at least 50% lower latency in the reported settings.

## Problem Framing

LightCross addresses a narrower problem than "blockchain sharding" as a whole: how a sharded smart-contract blockchain can execute transactions that invoke contracts or read/write state located in multiple shards.

The paper's problem framing has three parts:

- **Cross-shard execution overhead.** Existing cross-shard commit protocols require repeated communication among shards, which can dominate latency and throughput.
- **General smart-contract complexity.** Transfer-only protocols can split a payment into simple withdrawal/deposit steps, but arbitrary contracts can contain internal calls, unpredictable read/write sets, and inter-contract dependencies.
- **High cross-shard ratio.** Random or permanent contract placement makes many smart-contract transactions cross-shard; the paper states that the ratio can exceed 90% in a 10-shard setting.

This places LightCross primarily under [[cross-shard-transaction-execution|Cross-shard transaction execution]], with secondary relevance to [[sharded-ledgers|Sharded ledgers]] and [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]].

## Background and Related Work Position

The paper contrasts LightCross with three broad routes:

| Route | What it does | Limitation identified by LightCross |
| --- | --- | --- |
| Payment-oriented sharding such as Atomix-style protocols | Handles simple cross-shard asset transfer with input/output or lock/unlock style coordination. | Does not directly support arbitrary smart-contract invocation graphs. |
| Ordered shard-to-shard execution such as RingBFT-like designs | Involved shards execute or agree in sequence. | Communication rounds grow with involved shards and state locks last longer. |
| Reference-committee designs such as AHL/ByShard-like routes | A reference committee or coordinator dispatches tasks and collects shard messages. | Can require application refactoring, committee bottlenecks, and multi-round state/message exchange. |

LightCross's distinctive move is not to invent a new shard-level consensus protocol. It uses shard-level BFT consensus as an assumption and changes where the cross-shard smart-contract execution happens.

## System Model

LightCross has three main roles:

| Role | Responsibility | Notes |
| --- | --- | --- |
| S-shards | Store and execute contracts assigned to the shard, run BFT consensus, and commit intra-shard transactions and final cross-shard write sets. | Each smart contract has an entry S-shard. |
| Executors | TEE-backed off-chain nodes that execute cross-shard transactions, request authenticated state from involved shards, and return read/write sets plus a certificate. | Executors can be malicious outside TEE; correctness relies on TEE attestation and verified state inputs. |
| R-shard | Schedules and orders cross-shard transaction results, verifies executor certificates, coordinates validation bitmaps, and broadcasts final commit decisions. | It does not execute full smart contracts; it orders and validates batches. |

Users do not need to know contract locations. A transaction is routed to the entry S-shard of the recipient contract. If execution stays within that shard, it is intra-shard. If the contract calls another contract in a different shard, the entry S-shard identifies the transaction as cross-shard and sends it to an executor.

## Trust and Fault Assumptions

LightCross assumes shard-level BFT consensus, such as PBFT, with at most one-third malicious nodes per shard and no forks. The R-shard also uses BFT consensus.

Executors are TEE-backed. The paper assumes confidentiality and integrity of the TEE execution environment and treats side-channel attacks as orthogonal. Executors can fail or behave maliciously outside the enclave, but the protocol can reassign a transaction to more executors after timeouts, and the R-shard verifies the execution certificate before accepting a result.

This means LightCross's trust boundary is different from pure Byzantine sharding: cross-shard execution correctness partly depends on trusted hardware and remote attestation, while commit ordering and final state updates remain shard-consensus responsibilities.

## Cross-Shard Commit Protocol

The protocol has five phases:

1. **Raw transaction creation.** A user signs a transaction and sends it to the entry S-shard for the called contract.
2. **Cross-shard transaction identification.** The entry shard speculatively executes the entry contract enough to detect whether it will call a contract on another shard. If yes, it forwards the transaction and code to an executor.
3. **Cross-shard execution.** The executor initializes the TEE execution engine, loads contract code, requests authenticated states from involved shards, executes the transaction, and emits read/write sets plus a certificate.
4. **Schedule generation.** The R-shard verifies the certificate, packs certified transactions into a batch, runs BFT consensus on the batch, and sends the agreed batch to involved S-shards.
5. **Commitment.** Involved S-shards validate read freshness, send validation bitmaps to the R-shard, receive the final bitmap, and commit the valid write sets.

The important design point is that S-shards do not run multiple rounds of smart-contract execution among themselves. They provide authenticated state, validate read freshness, and apply final writes.

## State Authentication

Executors need state from S-shards without blindly trusting a single shard node. LightCross uses Merkle Patricia Trie proofs and threshold-signed state roots:

- An executor requests a state key from a random node in the entry shard.
- The node returns the value and an MPT proof.
- The shard signs the MPT root at each block height with a threshold signature.
- The executor verifies both the threshold signature on the root and the Merkle proof for the returned state.

This design lets an executor validate state inputs without synchronizing every shard's full root history. It also explains why state storage details appear inside a cross-shard execution protocol: authenticated state commitments become part of the transaction-execution boundary.

## Transaction Validation

Executors may run concurrently, so a transaction can read a state value that becomes stale before final commitment. LightCross handles this with R-shard coordinated validation:

1. The R-shard broadcasts an agreed batch to involved S-shards.
2. Each S-shard checks read-set entries against its latest state.
3. Each S-shard returns a bitmap marking which transactions remain valid and locks read states for valid transactions.
4. The R-shard combines bitmaps with logical AND to produce a final bitmap.
5. S-shards commit only transactions marked valid in the final bitmap and release locks.

The R-shard also needs to avoid serializability conflicts among transactions in the same batch. The paper describes a conservative timestamp-ordering route: if one transaction reads a key and another writes it, stale readers are aborted. It notes that more optimal scheduling is possible but not the paper's focus.

## Smart Contract Migration

LightCross reduces the cross-shard transaction ratio by periodically migrating contracts.

The paper constructs a transaction call graph (TCG):

| Graph element | Meaning |
| --- | --- |
| Vertex `<A,w>` | Contract `A`; weight `w` counts transactions that trigger the contract, including implicit calls. |
| Edge `<A1,A2,cnt>` | Contracts called in the same transaction; `cnt` counts co-invocation frequency. |

The TCG is partitioned into `m` subgraphs for `m` S-shards. The objectives are:

- balance workload across shards,
- minimize cross-shard edges,
- minimize state migration cost when assigning new partitions to physical shards.

The paper uses Metis for graph partitioning and then chooses a shard assignment that reduces migrated data. Migrations occur at epoch boundaries. The R-shard stops scheduling new cross-shard transactions, S-shards finish existing work, the R-shard commits migration transactions, and source shards move contract state to target shards. The paper also describes migration-skipping if the recent cross-shard ratio is already below a threshold and edge-weight adjustment to avoid moving large contracts unnecessarily.

## Account Segmentation and Routing

The appendix distinguishes contract accounts and user accounts:

- Contract accounts are assigned to S-shards because their code and persistent state define execution locality.
- User accounts can be segmented into sub-accounts across shards because user balances are fungible and do not contain executable code.

For routing, LightCross maintains a distributed routing table mapping contracts to entry shards. A full copy of the table on every shard is considered storage-heavy, so the table can be partitioned into subtables and located through address-based routing.

## Correctness Arguments

The paper states three main correctness properties:

| Property | Meaning in LightCross |
| --- | --- |
| Atomicity | If one involved S-shard commits a cross-shard transaction, every other involved S-shard eventually commits it. |
| Serializability | Committed intra-shard and cross-shard transactions can be serialized consistently with the R-shard order and shard-local orders. |
| Liveness | If shard BFT consensus progresses and honest executors eventually execute the transaction, submitted transactions eventually receive a processing result. |

The atomicity proof relies on the R-shard's final bitmap and read-lock behavior: after a transaction is marked valid and committed by any involved shard, it cannot later be selectively aborted by another involved shard. The serializability argument constructs a serialization by using the R-shard order for cross-shard transactions and filling intra-shard transactions into the gaps in a way that respects committed closure. Liveness relies on reassigning timed-out transactions to additional executors.

## Implementation

The prototype is based on FISCO-BCOS, a permissioned blockchain with EVM and PBFT support.

Implementation components include:

- S-shards that run consensus, manage contracts, and store states in Merkle trees.
- An R-shard that orders cross-shard transaction batches and runs Metis for graph partitioning.
- Intel SGX executors implemented with Occlum v0.28.0.
- Three enclave types: data transmission, key management, and contract execution.
- Local attestation among enclaves and remote attestation for executor certificates.
- Cluster-sending communication between R-shard and S-shards.

The paper's implementation is therefore a permissioned-chain prototype, not a permissionless validator-assignment design.

## Evaluation Setup

The paper evaluates LightCross against ByShard and RingBFT variants implemented on FISCO-BCOS.

Reported setup:

- Up to 16 S-shards.
- 22 nodes per S-shard.
- Up to 12 S-shard node instances per physical machine.
- Machines: Intel Xeon Silver 4210 CPUs, 96 GB memory, 4 TB disk, Ubuntu 20.04.1.
- SGX SDK v2.2 and Occlum v0.28.0.
- Nodes divided into six simulated geographic regions with bandwidth limits.
- Ethereum mainnet trace from Jan 1 2022 to Apr 30 2022 is used for workload generation: 769,020 blocks, 122M transactions, 84M contract calls, and more than 40% of contract-call transactions invoking at least two smart contracts.

The evaluation states that enough executors are deployed so executors are not the throughput bottleneck.

## Evaluation Results

### Scaling Number of Shards

With a fixed 30% cross-shard smart-contract transaction ratio and 2-16 shards:

- At 16 shards, LightCross reports 4x throughput over ByShard and 1.6x over RingBFT.
- LightCross latency increases from about 1.65s to 2.4s as shards grow from 3 to 16.
- RingBFT's throughput drops as communication rounds grow with involved shards.
- ByShard's throughput is limited by reference-committee and state-synchronization overhead.

### Varying Involved Shards

With 16 shards and transactions accessing 1-9 shards:

- When transactions access only one shard, all systems are similar at about 15.8K tps.
- As involved shards increase, LightCross's advantage grows from about 4% to 200%.
- ByShard and RingBFT latency increases sharply when transactions involve more than three shards because locks and cross-shard communication block more intra-shard work.

### Contract Migration

With 16 shards, about 50% of transactions accessing more than one smart contract, and epochs of roughly six hours:

- ByShard and RingBFT cross-shard ratios quickly rise to about 50%.
- LightCross keeps the cross-shard ratio around 25% after migration.
- ByShard and RingBFT throughput rises only about 3x when scaling from 3 to 16 shards, while LightCross reports a 6.4x speedup.
- At 16 shards, the paper reports ByShard latency around 21s, RingBFT around 15s, and LightCross up to 3.2s.
- Migration causes throughput dips near epoch boundaries and finishes in roughly 10-30 minutes; after about six epochs, distribution stabilizes and migration rarely triggers.

## Limitations and Assumptions

- The core off-chain execution route relies on Intel SGX/TEE assumptions. The paper explicitly treats side-channel attacks as orthogonal.
- The R-shard is a special scheduling component. The paper argues it is not a bottleneck because it orders and validates rather than executes contracts, but its availability and throughput are still system-level assumptions.
- Executor availability matters for liveness. The protocol responds to timeouts by assigning more executors, but the evaluation deploys enough executors to avoid executor bottlenecks.
- The system targets permissioned, FISCO-BCOS-like settings; validator assignment, open-network incentives, and permissionless Sybil resistance are not the paper's contribution.
- Contract migration depends on historical workload stability. Workload shifts can cause migration overhead or stale placement.
- Transaction validation can abort stale readers; the paper does not optimize batch scheduling for minimal aborts.
- The paper reports a real-world trace-driven workload generator, but the prototype is still an experimental system with simulated regional deployment.

## Knowledge Absorption Decisions

| Candidate | Decision | Reason |
| --- | --- | --- |
| `LightCross` | Keep as source instance, not a knowledge node. | It is a named paper/system; design and measurements belong in this source note. |
| `cross-shard transaction execution` | Promote to active problem node. | AHL, ByShard, RingBFT, OmniLedger and LightCross now give enough evidence that this is a reusable problem layer. |
| `TEE-assisted cross-shard execution` | Method row under cross-shard transaction execution. | The method is reusable but currently LightCross-specific in this vault. |
| `smart contract migration` | Method row under cross-shard transaction execution and sharded ledgers. | It solves workload-locality/cross-shard-ratio reduction, not the whole sharding problem. |
| `state authentication for off-chain executors` | Keep as source detail and possible bridge signal. | It may later strengthen a state-storage-to-execution bridge, but LightCross alone should not create a new storage node. |

## Source-To-Knowledge Handoff

| Target | Absorbed delta |
| --- | --- |
| [[blockchain-systems|Blockchain systems]] | Adds TEE-backed off-chain cross-shard execution and contract migration as a blockchain scaling/execution route. |
| [[execution-and-transactions|Blockchain execution and transactions]] | Promotes cross-shard transaction execution from candidate to child problem node. |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Adds LightCross as a cross-shard smart-contract execution method and updates the old gap. |
| [[cross-shard-transaction-execution|Cross-shard transaction execution]] | New active problem node with LightCross as the TEE/off-chain execution route. |
| [[scaling-and-sharding|Scaling and sharding]] | Adds smart-contract sharding with contract migration and R-shard/executor split. |
| [[sharded-ledgers|Sharded ledgers]] | Adds LightCross as a sharded-ledger route focused on arbitrary smart contracts rather than transfer-only transactions. |
| [[database-transactions-to-byzantine-sharded-ledgers|Database transaction protocols -> Byzantine sharded ledgers]] | Adds contrast: LightCross avoids exposing arbitrary smart-contract logic as 2PC/2PL fragments by offloading execution to TEE executors. |

## Review Questions

- Should `TEE-assisted blockchain execution` become a separate method family if more sources besides SlimChain, AHL and LightCross appear?
- Should `smart-contract placement and migration` become its own child node under sharded ledgers if OptChain or related placement papers are imported?
- Should the appendix URL or public artifact be fetched later to verify venue, artifact, and complete supplementary algorithms?

## Update Record

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts | Deep-read source note created and absorbed into Source + Knowledge + Bridge architecture. | codex |
