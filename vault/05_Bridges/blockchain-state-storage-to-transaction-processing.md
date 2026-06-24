---
id: "nahida-bridge-blockchain-state-storage-to-transaction-processing"
title: "Blockchain state storage -> transaction processing"
original_title: "Blockchain state storage -> transaction processing"
file_slug: "blockchain-state-storage-to-transaction-processing"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "intra_domain_dependency"
bridge_status: "active_seed"
endpoint_paths:
  - "blockchain-systems/data-management-and-storage/blockchain-state-storage"
  - "blockchain-systems/execution-and-transactions/transaction-processing"
endpoint_knowledge_refs:
  - "nahida-knowledge-blockchain-state-storage"
  - "nahida-knowledge-blockchain-transaction-processing"
from_domain: "blockchain-systems"
to_domain: "blockchain-systems"
from_direction: "data-management-and-storage"
to_direction: "execution-and-transactions"
from_topic: "blockchain-state-storage"
to_topic: "transaction-processing"
relation_types:
  - "dependency"
  - "shared_state_commitment"
  - "implementation_reuse"
  - "tension"
directionality: "bidirectional_with_primary_storage_to_execution"
relationship_thesis: "Blockchain transaction processing is constrained by how state is stored, committed, and proven: if consensus nodes keep only state roots or compact commitments, transaction validation must carry read/write evidence, conflict metadata, and update proofs that let stateless validators decide commit/abort and compute the next root without full state."
transferability: "high_within_blockchain_execution_storage_boundary"
non_transfer_boundary: "State commitments and authenticated storage structures can support transaction validation and deterministic root updates, but they do not by themselves provide consensus safety, data availability, storage-node liveness, execution correctness, privacy, or incentive compatibility. Conversely, transaction scheduling and OCC/SSI rules do not eliminate the need for a verifiable state commitment and data-serving layer."
evidence_window_start: "2021"
evidence_window_end: "2026-06-23"
domains:
  - "blockchain-systems"
topics:
  - "blockchain state storage"
  - "blockchain transaction processing"
  - "stateless blockchain"
  - "authenticated state commitments"
  - "partial Merkle trie"
  - "off-chain storage"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
knowledge_refs:
  - "nahida-knowledge-blockchain-state-storage"
  - "nahida-knowledge-blockchain-transaction-processing"
relation_edges:
  - from: "nahida-bridge-blockchain-state-storage-to-transaction-processing"
    relation: "connects"
    to: "nahida-knowledge-blockchain-state-storage"
    evidence_refs:
      - "vault/05_Bridges/blockchain-state-storage-to-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-blockchain-state-storage-to-transaction-processing"
    relation: "connects"
    to: "nahida-knowledge-blockchain-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/blockchain-state-storage-to-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-blockchain-state-storage-to-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-blockchain-state-storage-to-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    confidence: "high"
    status: "active_seed"
query_keys:
  - "blockchain state storage transaction processing"
  - "stateless blockchain transaction processing"
  - "off-chain storage on-chain commitment"
  - "partial Merkle trie transaction commit"
  - "authenticated state commitment execution"
  - "RSA accumulator state digest transaction processing"
  - "split-execute-merge state commitment"
  - "L2chain state digest"
created: "2026-06-22"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-slimchain-stateless-execution-storage"
  - "nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution"
source_refs:
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
confidence: "high"
trust_tier: "primary"
---

# Blockchain state storage -> transaction processing

## 命名与路径

- Original title: Blockchain state storage -> transaction processing
- File slug: `blockchain-state-storage-to-transaction-processing`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

[[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain state storage]] 关注状态如何存储、索引、承诺和证明。[[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] 关注交易如何执行、检测冲突、commit/abort，并形成确定性状态。

这条 bridge 记录的不是“存储优化会自然带来执行优化”，而是更窄的命题: 当区块链把 full state、full transaction data 或可访问状态集合移出 consensus layer 时，交易处理协议必须携带更多证明和元数据，才能让 stateless、light 或 digest-only validators 在不持有全量状态的情况下验证执行、检查冲突并计算新 state root/digest。

## 连接命题

- From: `blockchain-systems/data-management-and-storage/blockchain-state-storage`
- To: `blockchain-systems/execution-and-transactions/transaction-processing`
- Relation types: dependency, shared_state_commitment, implementation_reuse, tension
- Directionality: `bidirectional_with_primary_storage_to_execution`
- Relationship thesis: Blockchain transaction processing is constrained by how state is stored, committed, and proven: if consensus nodes keep only state roots or compact commitments, transaction validation must carry read/write evidence, conflict metadata, and update proofs that let stateless validators decide commit/abort and compute the next root without full state.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] | `blockchain-systems/data-management-and-storage/blockchain-state-storage` | state root, MPT/partial trie, authenticated proofs, off-chain full state, storage-layer sharding | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] | `blockchain-systems/data-management-and-storage/blockchain-state-storage` | RSA accumulator available-state digest, state-subset membership witness, split/merge digest update | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | `blockchain-systems/execution-and-transactions/transaction-processing` | off-chain execution, read/write set validation, OCC/SSI conflict checks, stateless commit, proof compression, layer-2 split-execute-merge | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]]; [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| State-root-only consensus storage | Consensus nodes store blocks, transaction digests and roots rather than full state. | SlimChain system model and block structure | A state root is only a commitment; it does not guarantee data availability or storage-node service. |
| Read/write evidence as execution boundary | Off-chain execution result carries read set, write set and execution attestation. | SlimChain off-chain execution | Execution correctness still needs TEE/VC/policy proof; the storage proof alone is not enough. |
| Write proof for stateless root update | Stateless validators update the root using `pi_write` and a partial Merkle trie. | SlimChain on-chain commitment | Proof format and partial trie logic are source-specific; not a generic storage engine abstraction. |
| Recent-window conflict metadata | Consensus nodes keep only last `k` blocks of read/write maps. | SlimChain temporary state | Bounded metadata rejects stale submissions and shifts some latency/availability pressure to storage/client behavior. |
| Storage-layer sharding | Full state can be divided among storage nodes while consensus remains unsharded. | SlimChain sharding section | This reduces storage-node burden but does not scale consensus throughput like validator sharding. |
| Accumulator state-subset split | DApp executors prove a chosen state subset belongs to the available-state digest before L2 execution. | L2chain split transaction | Accumulator membership does not prove execution correctness or data availability. |
| Split-execute-merge digest lifecycle | L1 validators split affected states, L2 executors execute after split commit, and merge transactions update the available digest. | L2chain SEM workflow | Requires TEE/order proof and careful conflict discard for overlapping state subsets. |
| Witness cache as commitment-performance adapter | Executors cache accumulator witnesses to lower repeated membership-witness cost. | L2chain witness cache | Source-specific optimization; should not be generalized without accumulator foundation sources. |

## 迁移矩阵

| From storage mechanism | To transaction-processing mechanism | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- |
| `H_state_root` commitment | Transaction validity against a past state | Storage node signs/proves execution against `H_old`; consensus maps `H_old` to a recent block height. | SlimChain Algorithm 1 and 2 | Old roots outside the `k` window are rejected. |
| Merkle read multiproof | Read integrity validation | TEE verifies read values against `H_old` before signing the execution statement. | SlimChain off-chain execution | TEE trust or alternative VC assumptions remain outside storage layer. |
| Merkle write proof | Stateless root update | Consensus node verifies `pi_write` and updates partial Merkle trie with new writes. | SlimChain Algorithm 2 and 3 | Incorrect or incomplete proof blocks commitment; proof bandwidth can dominate without compression. |
| Partial Merkle trie | Compact validator state | Consensus node materializes only recent write paths and compresses old subtrees back to digests. | SlimChain Algorithm 3 and 4 | Source-specific data structure; future Verkle/state-expiry designs may alter the bridge. |
| Off-chain full MPT storage | Parallel execution and storage-layer sharding | Storage nodes execute and store full state; consensus sees compact evidence. | SlimChain sharding/evaluation | Storage node liveness and data service incentives are not solved by consensus root alone. |
| RSA accumulator available-state digest | Parallel L2 DApp execution | DApp executors split a provable state subset from L1, execute in L2, then merge the updated subset digest back into the available-state digest. | L2chain §3-§5 | Accumulator witness cost, TEE trust and overlapping state subsets become transaction-processing bottlenecks. |
| Split transaction membership witness | L1 validation before off-chain execution | Validators verify DApp authority and subset membership before allowing a batch to execute over those states. | L2chain Definition 4.1 | Membership proof only says the states are currently available; it does not certify business logic. |
| Merge transaction updated digest | L1 commitment after off-chain execution | Validators verify the split transaction reference and TEE execution proof before updating the digest. | L2chain Definition 4.2 | Merge safety depends on correct split reference and TEE proof, not on storage commitment alone. |

## 类比、依赖或关系边界

SlimChain shows a tight coupling between state commitments and transaction processing. The transaction-processing protocol cannot be specified independently of the state-storage design because validators need a proof format that supports both conflict checks and root updates. L2chain strengthens the same bridge from the opposite direction: it designs the state digest so that transaction processing can split and merge state subsets instead of serializing every DApp update through one MPT root.

At the same time, authenticated storage does not replace transaction execution. SlimChain still needs a TEE/VC/policy proof for off-chain execution, and L2chain still needs TEE simulation/execution signatures plus L1 split commitment to prevent rollback attacks. State commitments can say what state was accessed or updated; they do not by themselves prove that the right code ran in the right order.

The bridge also separates storage-layer sharding from consensus sharding. SlimChain shards storage but leaves consensus global, so cross-shard transactions can be atomic at the consensus layer without chain-level two-phase commit. This is not the same tradeoff as OmniLedger/AHL-style validator sharding.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing]] | Direct evidence that off-chain state storage and authenticated commitments reshape smart-contract transaction validation, OCC/SSI conflict checks, proof compression, and storage-layer sharding. | active_seed |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications]] | Direct evidence that accumulator-based state digest split/merge can enable layer-2 DApp transaction processing while moving confidentiality/order-correctness checks into TEE-backed two-step execution. | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `blockchain-systems/data-management-and-storage/blockchain-state-storage` | Add method row for stateless on-chain commitments and partial Merkle trie maintenance; add bridge link. | active_seed |
| `blockchain-systems/data-management-and-storage/blockchain-state-storage` | Add method row for accumulator-based split/merge state digest. | active_seed |
| `blockchain-systems/execution-and-transactions/transaction-processing` | Add method row for stateless off-chain execution with OCC/SSI and write-proof root update; add layer-2 SEM route; add bridge link. | active_seed |

## 查询入口

- stateless blockchain 的交易如何验证?
- on-chain consensus node 不存 full state 时如何更新 state root?
- partial Merkle trie 和交易 commit 有什么关系?
- off-chain storage 如何影响 blockchain transaction processing?
- SlimChain 为什么不等于 consensus sharding?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: future sources on stateless clients, Verkle/state expiry, proof-carrying data, authenticated databases, storage-node incentives, or off-chain execution proofs.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] | Methods, representative sources, bridge links | SlimChain adds partial commitment maintenance and off-chain state storage. | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Methods, representative sources, bridge links | SlimChain adds stateless validation, OCC/SSI over recent metadata, and proof-based root update. | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain Data Management and Storage]] | Source extension | Places off-chain state storage under storage direction rather than as a source-shaped note. | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions|Blockchain execution and transactions]] | Source extension | Places off-chain execution and on-chain commitment under execution direction. | active_seed |

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: new source changes either endpoint, relation type, transfer boundary, or maturity; especially stateless-client/state-expiry/Verkle/off-chain execution/storage-incentive sources.

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-slimchain-stateless-execution-storage | Created bridge from SlimChain evidence. | doi:10.14778/3476249.3476283 | codex |
| 2026-06-23 | nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution | Strengthened bridge with L2chain RSA-accumulator split-execute-merge evidence. | doi:10.14778/3574245.3574278 | codex |
