---
id: "doi:10.14778/3476249.3476283"
title: "SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing"
original_title: "SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing"
source_kind: "paper"
source_type: "academic_paper"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
status: "absorbed"
lifecycle: "active"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
file_slug: "doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing"
authors:
  - "Cheng Xu"
  - "Ce Zhang"
  - "Jianliang Xu"
  - "Jian Pei"
year: 2021
venue: "Proceedings of the VLDB Endowment, Vol. 14, No. 11"
doi: "10.14778/3476249.3476283"
arxiv_id: ""
url: "https://doi.org/10.14778/3476249.3476283"
artifact_urls:
  - "https://github.com/hkbudb/slimchain"
local_pdf_path: "~/Desktop/paper/p2314-xu.pdf"
raw_text_path: "vault/02_Raw/pdf/extracted/p2314-xu-5eb0835c7d40-pages.txt"
pdf_sha256: "5eb0835c7d40b17fd17869b852197d7ad8ae9be572323b349801be794433b8cb"
pages: 13
primary_domain: "blockchain-systems"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing"
secondary_ontology_paths:
  - "blockchain-systems/data-management-and-storage/blockchain-state-storage"
  - "distributed-systems/transaction-processing"
knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
  - "nahida-knowledge-blockchain-execution-and-transactions"
  - "nahida-knowledge-blockchain-transaction-processing"
  - "nahida-knowledge-blockchain-data-management-and-storage"
  - "nahida-knowledge-blockchain-state-storage"
bridge_refs:
  - "nahida-bridge-database-transaction-processing-to-blockchain-execution"
  - "nahida-bridge-blockchain-state-storage-to-transaction-processing"
topics:
  - "stateless blockchain"
  - "off-chain storage"
  - "blockchain transaction processing"
  - "parallel smart-contract execution"
  - "authenticated state commitments"
  - "Merkle Patricia Trie"
  - "optimistic concurrency control"
  - "serializable snapshot isolation"
  - "TEE-based verifiable execution"
  - "storage sharding"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "blockchain-systems"
  - "transaction-processing"
  - "state-storage"
freshness_status: "fresh"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_id: "nahida-knowledge-20260622-slimchain-stateless-execution-storage"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0066"
confidence: "high"
trust_tier: "primary"
---

# SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing

## Source Identity

- Source: Xu, Zhang, Xu, Pei. "SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing." PVLDB 14(11), 2021.
- DOI: `10.14778/3476249.3476283`.
- Artifact signal: paper lists `https://github.com/hkbudb/slimchain`; the repository was not re-read in this intake.
- Local PDF: `~/Desktop/paper/p2314-xu.pdf`.
- Extraction: `pypdf` text extraction, 13 pages, usable for deep reading. `pdfinfo/pdftotext` capability was unavailable in this environment, so the existing extracted text was used.
- Queue correction: the intake queue contained a noisy arXiv-like value `6249.34762`; this source is DOI-backed and has no arXiv ID recorded from the paper.

## One-Sentence Summary

SlimChain makes smart-contract blockchains stateless at the consensus layer: consensus nodes keep transaction digests and state commitments, while off-chain storage nodes store full transaction/state data, execute transactions with verifiable execution, and submit read/write evidence that lets consensus nodes validate, order, and update state roots with OCC/SSI-style concurrency control.

## Abstract-Level Contribution

The paper argues that existing blockchains require every full node to store all transaction data, all state data, and re-execute every transaction, which creates storage and computation pressure and can push ordinary users out of consensus participation. SlimChain targets this bottleneck by splitting node roles:

- Consensus nodes keep blocks, transaction digests, consensus metadata, and a state root.
- Storage nodes keep full transactions and the full Merkle Patricia Trie state, execute smart contracts, and provide proofs.
- Clients send signed transactions to storage nodes.

This creates a stateless blockchain architecture for smart contracts. The consensus layer remains responsible for transaction ordering and commitment, but it validates off-chain execution through proofs and updates only a compact authenticated state commitment. The reported evaluation claims 97%-99% reduction in on-chain consensus-node storage and peak throughput improvements from 1.4x to 15.6x over the paper's baselines, depending on workload and chain mode.

## Problem Framing

The central problem is not merely "make blockchain storage smaller." SlimChain couples three problems:

- Storage replication: every consensus node storing all transaction/state data increases disk requirements.
- Execution replication: every consensus node re-executing all smart contracts limits throughput.
- Stateful validation: if consensus nodes do not store state, they still need enough evidence to verify transaction execution, detect conflicts, and update state roots.

SlimChain therefore belongs to both [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] and [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain state storage]]. Its reusable insight is that a state commitment design can change the transaction-processing protocol itself.

## System Model

SlimChain has three node roles:

| Role | Responsibilities | Trust/verification boundary |
| --- | --- | --- |
| Client | Issues a signed transaction request `<tx_input, sigma_tx>` to a storage node. | Signature binds request to the client. |
| Storage node | Stores transaction data and full state, simulates smart-contract execution, records read/write sets, generates proofs, and submits execution results. | May be faulty; execution result must be verifiable by consensus nodes. |
| Consensus node | Participates in consensus, validates submitted transactions, orders transactions into blocks, stores transaction digests and state roots. | Does not store full state; relies on proofs and temporary state to validate and update commitments. |

The paper further distinguishes block proposers and block observers among consensus nodes. A proposer includes transactions in a block and computes the new state root; observers validate the proposed block using the same validation logic and reject invalid proposals.

## Stateless Block Structure

SlimChain's block stores compact commitments rather than full payloads:

- Previous block hash `H_prev_blk`.
- Consensus data.
- Transaction root over transaction digests.
- State root `H_state_root`.

Full transaction data and the full Merkle Patricia Trie are stored off chain by storage nodes. This is the key storage saving: consensus nodes keep enough to verify block continuity and state commitments, but not the full data needed to answer every state query locally.

## Transaction Lifecycle

SlimChain's transaction flow is:

1. A client sends a signed transaction request to a storage node.
2. The storage node executes the smart contract against the latest state root it observes.
3. During execution, the storage node records the read set and write set.
4. The storage node builds proofs for read integrity and write-root update.
5. It submits a transaction package to consensus nodes.
6. Consensus nodes validate execution evidence, check conflicts against recently committed transactions, update a partial state commitment, and append the transaction if valid.
7. Storage nodes observe the committed block order and commit their local state accordingly.

The transaction submitted to consensus nodes has the form:

```text
tx_submit = <tx_input, {r}_tx, {w}_tx, H_old, pi_TEE, pi_write>
```

Here `H_old` is the state root used for off-chain execution, `{r}_tx` is the read set, `{w}_tx` is the write set, `pi_TEE` attests the execution/read-set result in the paper's main implementation, and `pi_write` lets stateless consensus nodes update the authenticated state commitment.

## Off-Chain Execution

SlimChain discusses three routes to verifiable off-chain execution:

- Cryptographic verifiable computation, such as SNARK-style proofs.
- Secure hardware, mainly Intel SGX in the prototype.
- Policy-based verification in some permissioned-chain settings.

The implementation uses a TEE. The storage node executes the smart contract locally, but the enclave signs an execution statement only after checking:

- the client's transaction signature,
- the smart-contract execution result,
- the read set and write set,
- the Merkle multiproof for the read set against `H_old`.

The TEE signature covers `<tx_input, {r}_tx, {w}_tx, H_old>`, so a consensus node can validate that the submitted read/write sets came from an attested execution against a committed state root. Outside the enclave, the storage node also generates `pi_write`, a Merkle proof for write addresses, so consensus nodes can update the state root without holding the full trie.

This is a clean source-layer detail: SlimChain is not only an execution outsourcing system and not only a storage outsourcing system. The off-chain proof format exists because stateless consensus nodes still need deterministic commitment updates.

## On-Chain Commitment and Temporary State

Consensus nodes maintain compact temporary state for only the last `k` blocks:

| Structure | Meaning |
| --- | --- |
| `M_i->r` | Block height to addresses read in that block. |
| `M_i->w` | Block height to addresses written in that block. |
| `M_r->i` | Read address to ordered block heights that read it. |
| `M_w->i` | Written address to ordered block heights that wrote it. |
| `T_w` | Partial Merkle trie containing recent write addresses and needed Merkle paths. |

Transactions whose `H_old` is older than the `k`-block temporary window are rejected. For an accepted transaction, consensus nodes:

1. Locate the block height `j` corresponding to `H_old`.
2. Reject if `i - j > k`.
3. Verify the TEE signature.
4. Verify the write proof.
5. Check conflicts under OCC or SSI.
6. Update the partial Merkle trie with `{w}_tx` and `pi_write`.
7. Update temporary read/write maps.
8. Compute the new state root and generate the block.
9. Remove temporary state older than `k` blocks and tidy the partial trie.

This temporary-state design is central: consensus nodes do not recover the whole historical state. They only remember the recent read/write footprint needed to decide whether an off-chain execution based on an old root can still be safely committed.

## Partial Merkle Trie

The partial Merkle trie `T_w` has the same root digest as the full trie for the portion needed by recent writes, but it materializes only:

- write-set addresses from transactions in the recent window,
- authentication paths needed to update those writes,
- digest placeholders for suppressed subtrees.

Algorithmically, SlimChain updates the partial trie by traversing the write proof and partial trie top-down. If a child exists only as a digest placeholder, the algorithm uses proof nodes and write-set entries to materialize just enough subtree state to apply the update. When old addresses leave the `k`-block window, the tidy procedure compresses no-longer-needed subtrees back to digests.

This is the most direct state-storage contribution: the data structure is not a generic storage engine like COLE. It is a commitment-maintenance structure specifically designed for stateless transaction commitment.

## Concurrency Control

SlimChain offers two conflict-checking modes:

| Mode | Rule | Isolation claim in paper | Tradeoff |
| --- | --- | --- | --- |
| OCC | Abort if the transaction read or wrote a key that has been updated since `H_old`. | Strong serializability. | Simpler and stricter; more aborts. |
| SSI | Abort if write set has been updated since `H_old`; track rw-dependencies pointing to and from the transaction and abort when both dependency directions exist. | Serializability. | Less conservative; higher success rate but weaker than strong serializability. |

The paper's example shows a transaction that OCC aborts because it read a key later updated by another committed transaction, while SSI can allow it when the dependency pattern remains serializable. The paper also gives an example transaction that neither OCC nor SSI can serialize.

For the knowledge base, the important migration is not "SlimChain equals database SSI." Rather, database-style OCC/SSI logic is adapted to a stateless blockchain context where the consensus nodes keep only block-window read/write metadata and a partial authenticated state structure.

## Proof Compression and Observer Validation

Block observers must validate proposed blocks. If every observer received full write proofs for each transaction, the proof bandwidth would become a bottleneck. SlimChain compresses proofs by:

- generating proofs against the latest block rather than the transaction's original `H_old`,
- omitting proof parts already shared with the observer's existing partial trie,
- bundling transaction proofs into a Merkle multiproof.

This proof-compression route matters because the paper's throughput gains partly depend on keeping observer validation efficient. It also shows another coupling between state-storage proof format and transaction-processing throughput.

## Storage-Node Synchronization

Storage nodes store full transactions and the full MPT. After observing committed blocks, they apply the committed transactions in consensus order and update their local state. SlimChain states that storage nodes do not need to store `pi_write` after commitment because they already maintain the full state data.

New consensus nodes retrieve blocks from storage nodes and validate from genesis. They need only keep temporary maps for the last `k` blocks. The paper suggests batching validation with a large Merkle multiproof for the next `m` blocks to reduce bandwidth during bootstrapping.

## Sharding Design

SlimChain shards only the off-chain storage layer. It does not shard the on-chain consensus layer.

This design has a clear tradeoff:

- Benefit: the consensus security model is not weakened by splitting validators into shards, and cross-shard transactions do not need a chain-level two-phase commit.
- Cost: consensus throughput remains bounded by the single consensus layer, while storage-node collaboration must fetch remote shard data for execution.

Cross-shard transactions can be handled by a storage node that stores all needed shards, or by collaboration among storage nodes where the executing node fetches remote data. Because the on-chain commitment protocol sees only submitted read/write/proof packages, the paper claims cross-shard transactions add no extra on-chain latency and commit atomically under the global consensus layer.

## Implementation

The prototype is about 26k lines of Rust. The paper reports:

- RocksDB for local storage.
- A Merkle Patricia Trie with BLAKE2b.
- HTTP networking for permissioned settings and libp2p for permissionless settings.
- Intel SGX enclave support via Rust SGX SDK.
- A transaction engine based on Rust EVM for Solidity smart contracts.
- Raft in permissioned mode and proof-of-work in permissionless mode.
- Hierarchical PKI where an enclave ephemeral key is signed after Intel SGX attestation.

Default parameters include 16 consensus nodes and 4 storage or endorsement nodes, 1024 max transactions per block for permissioned mode, 4096 for permissionless mode, and a temporary-state window `k = 16`.

## Evaluation Setup

The experiments use Azure US-East:

- Consensus nodes: `Standard_D2_v2`.
- Storage/endorsement nodes: `Standard_DC4s_v2`.
- Default deployment: 16 consensus nodes and 4 storage/endorsement nodes.
- Bandwidth: 1500 Mbps.
- Storage nodes use three parallel transaction-engine threads.
- Workloads: Blockbench micro workloads `DoNothing`, `CPUHeavy`, `IOHeavy`, plus macro workloads `KVStore` and `SmallBank`.
- Transaction requests: 300k random requests and 100k sender accounts.

Baselines:

| Baseline | Meaning |
| --- | --- |
| Classic | Traditional stateful blockchain where all on-chain consensus nodes execute sequentially and replicate transaction/state data. |
| Stateful | SlimChain counterpart without the partial Merkle trie; all nodes store full transaction/state data. |
| Fabric# | Permissioned baseline similar to Fabric endorsement/ordering/commit flow with stateful nodes and a single endorsement policy. |

## Evaluation Results

### Storage

SlimChain consensus-node storage is about 65 bytes per transaction in permissioned mode and about 63 bytes per transaction in permissionless mode across workloads. The baselines store thousands of bytes per transaction. The paper summarizes this as a 97%-99% reduction in on-chain storage.

### Permissioned Throughput

The paper reports the following permissioned throughput numbers:

| Workload | Classic | Fabric# | Stateful | SlimChain |
| --- | ---: | ---: | ---: | ---: |
| DoNothing | 790 | 1277 | 489 | 1284 |
| CPUHeavy | 111 | 1221 | 487 | 1259 |
| IOHeavy | 188 | 562 | 465 | 685 |
| KVStore | 387 | 753 | 440 | 987 |
| SmallBank | 413 | 858 | 462 | 1022 |

SlimChain's permissioned throughput improvement is especially large over Classic on CPU-heavy and IO-heavy workloads because consensus nodes no longer execute every transaction locally.

### Permissionless Throughput

The paper reports the following permissionless throughput numbers:

| Workload | Classic | Stateful | SlimChain |
| --- | ---: | ---: | ---: |
| DoNothing | 177 | 444 | 462 |
| CPUHeavy | 29 | 441 | 454 |
| IOHeavy | 58 | 299 | 316 |
| KVStore | 92 | 337 | 342 |
| SmallBank | 102 | 317 | 321 |

The paper summarizes this as 2.6x-15.6x throughput improvement over Classic in permissionless mode.

### OCC vs SSI

For KVStore and SmallBank:

| Workload | OCC success rate | SSI success rate | OCC throughput / latency | SSI throughput / latency |
| --- | ---: | ---: | --- | --- |
| KVStore | 90.49% | 95.34% | 923 tps / 2.70s | 987 tps / 2.53s |
| SmallBank | 99.62% | 99.75% | 945 tps / 2.95s | 1022 tps / 2.44s |

SSI improves throughput by roughly 7%-8% and latency by roughly 6%-21% in the reported workloads.

### Proof Compression

Proof compression improves KVStore throughput from 656 tps to 987 tps and SmallBank throughput from 641 tps to 1022 tps. Reported latency falls from 3.97s to 2.53s for KVStore and from 3.92s to 2.44s for SmallBank.

### Storage-Layer Sharding

For KVStore in permissioned mode:

| Storage shards | Throughput | Latency | Storage-node size |
| ---: | ---: | ---: | ---: |
| 1 | 987 tps | 2.53s | 5959 B/tx |
| 2 | 962 tps | 2.76s | 5071 B/tx |
| 3 | 941 tps | 2.77s | 4782 B/tx |
| 4 | 972 tps | 2.87s | 4624 B/tx |

The paper explains that storage savings are not linear because all storage nodes keep upper MPT layers, while throughput/latency are only mildly affected because sharding is transparent to the on-chain commitment protocol.

## Limitations and Assumptions

- The main prototype relies on Intel SGX for verifiable execution. The paper mentions cryptographic verifiable computation and policy-based alternatives, but the reported implementation/evaluation is TEE-centered.
- Consensus nodes accept only transactions whose execution root is within a recent `k`-block window. This bounds metadata but rejects stale submissions.
- Off-chain storage availability is a separate operational concern. A state root proves commitment, but it does not guarantee storage nodes will serve full data.
- Sharding is at the storage layer, not the consensus layer. It reduces storage pressure but does not scale the consensus layer itself.
- Bootstrapping a new consensus node still requires retrieving and validating blocks from storage nodes.
- The paper leaves further reduction of on-chain state, storage-node operation cost, and data provenance under stateless design as future work.

## Knowledge Absorption Decisions

| Candidate | Decision | Reason |
| --- | --- | --- |
| `SlimChain` | Keep as source instance, not a knowledge node. | It is a named paper/system, and its full details belong in this source note. |
| `stateless blockchain transaction processing` | Review candidate under transaction processing. | SlimChain provides strong evidence, but a reusable child node needs additional stateless-client/state-expiry/state-commitment sources. |
| `partial Merkle trie for stateless commitment` | Method row inside state-storage and transaction-processing nodes. | It is a source-specific mechanism but exemplifies the bridge between state commitments and transaction processing. |
| `blockchain state storage -> transaction processing` | Create bridge. | The paper directly shows state commitment format and storage placement constrain validation, conflict detection, and throughput. |
| `OCC/SSI in stateless blockchain` | Add to existing database-transaction-processing bridge. | It adapts database concurrency-control ideas but under a different trust and storage model. |

## Source-To-Knowledge Handoff

| Target | Absorbed delta |
| --- | --- |
| [[blockchain-systems|Blockchain systems]] | Add stateless/off-chain execution-storage split as a blockchain-system route. |
| [[execution-and-transactions|Blockchain execution and transactions]] | Add stateless off-chain smart-contract execution and on-chain commitment as an execution route. |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Add OCC/SSI over a recent-window metadata structure and partial Merkle trie commitment updates. |
| [[data-management-and-storage|Blockchain Data Management and Storage]] | Add off-chain full-state storage with on-chain commitments as a state-storage route. |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] | Add partial MPT/commitment-maintenance method and storage-layer sharding signal. |
| [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] | Add SlimChain as evidence that OCC/SSI can migrate to stateless smart-contract commitment. |
| [[blockchain-state-storage-to-transaction-processing|Blockchain state storage -> transaction processing]] | New bridge: storage commitments and proof structures constrain transaction validation/commit. |

## Review Questions

- Should future stateless-client, Verkle, state-expiry, or proof-carrying data sources promote `stateless blockchain` into an independent child under state storage or transaction processing?
- Should SGX/TEE-based blockchain execution become a separate method family if more sources appear?
- Should the artifact repository be analyzed later under `nahida-github-repo-analyze` to verify implementation architecture beyond paper claims?

## Update Record

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-slimchain-stateless-execution-storage | Deep-read source note created and absorbed into Source + Knowledge + Bridge architecture. | codex |
