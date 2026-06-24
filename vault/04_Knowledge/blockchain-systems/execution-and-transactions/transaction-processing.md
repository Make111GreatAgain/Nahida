---
id: "nahida-knowledge-blockchain-transaction-processing"
title: "Blockchain transaction processing"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "transaction-processing"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-execution-and-transactions"
child_knowledge_refs:
  - "nahida-knowledge-leaderless-consensus-execution"
  - "nahida-knowledge-cross-shard-transaction-execution"
  - "nahida-knowledge-nested-contract-transaction-execution"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing"
relation_edges:
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-execution-and-transactions"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "has_child"
    to: "nahida-knowledge-leaderless-consensus-execution"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "has_child"
    to: "nahida-knowledge-cross-shard-transaction-execution"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/cross-shard-transaction-execution.md"
      - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "has_child"
    to: "nahida-knowledge-nested-contract-transaction-execution"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/nested-contract-transaction-execution.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "bridges_to"
    to: "nahida-bridge-permissioned-consensus-to-transaction-execution"
    evidence_refs:
      - "vault/05_Bridges/permissioned-consensus-to-transaction-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "bridges_to"
    to: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    evidence_refs:
      - "vault/05_Bridges/database-transaction-processing-to-blockchain-execution.md"
      - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "bridges_to"
    to: "nahida-bridge-blockchain-state-storage-to-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/blockchain-state-storage-to-transaction-processing.md"
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
      - "vault/05_Bridges/blockchain-state-storage-to-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "supporting_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/smart-contract-execution.md"
    confidence: "medium"
    status: "supporting_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "bridges_to"
    to: "nahida-bridge-smart-contract-execution-to-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/smart-contract-execution-to-transaction-processing.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-permissioned-consensus-to-transaction-execution"
  - "nahida-bridge-database-transaction-processing-to-blockchain-execution"
  - "nahida-bridge-blockchain-state-storage-to-transaction-processing"
  - "nahida-bridge-smart-contract-execution-to-transaction-processing"
source_note_refs:
  - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
  - "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
  - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
  - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
  - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
  - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
  - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
  - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
representative_source_refs:
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "arxiv:1804.00399v4"
  - "arxiv:1903.01919v2"
  - "arxiv:2003.10064v1"
  - "doi:10.1145/3299869.3319883"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
  - "arxiv:2504.16552v2"
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
query_keys:
  - "blockchain transaction processing"
  - "transaction execution protocol"
  - "blockchain concurrency control"
  - "parallel blockchain execution"
  - "区块链交易处理"
  - "cross-shard transaction execution"
  - "blockchain relational database"
  - "block-height SSI"
  - "execute and order in parallel"
  - "execute-order-validate"
  - "EOV blockchains"
  - "FabricSharp"
  - "optimistic concurrency control blockchain"
  - "Fabric++"
  - "Hyperledger Fabric transaction reordering"
  - "early transaction abort"
  - "Nezha"
  - "DAG-based blockchain transaction processing"
  - "address-based conflict graph"
  - "hierarchical sorting"
  - "SlimChain"
  - "stateless blockchain transaction processing"
  - "off-chain smart contract execution"
  - "partial Merkle trie"
  - "on-chain state commitment"
  - "L2chain"
  - "layer-2 DApp transaction processing"
  - "split-execute-merge"
  - "SEM workflow"
  - "RSA accumulator state digest"
  - "TEE rollback attack mitigation"
  - "cross-shard smart contract execution"
  - "LightCross"
  - "cross-chain smart contract invocation"
  - "cross-chain hybrid concurrency control"
  - "ShuttleCross"
  - "read-write separation cross-chain invocation"
  - "smart contract execution"
  - "deterministic smart contract runtime"
  - "gas metering"
  - "DTVM"
  - "nested contract transaction execution"
  - "nested smart contract transaction"
  - "subtransaction-level rollback"
  - "fine-grained re-execution"
  - "hyper-dependency graph"
  - "Loom"
aliases:
  - "区块链交易处理"
  - "Blockchain transaction execution"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "transaction-processing"
  - "transaction-execution"
  - "cross-shard-transactions"
  - "blockchain-relational-databases"
  - "serializable-snapshot-isolation"
  - "execute-order-validate"
  - "optimistic-concurrency-control"
  - "transaction-reordering"
  - "early-abort"
  - "dag-based-blockchain-execution"
  - "address-based-conflict-graph"
  - "hierarchical-sorting"
  - "stateless-blockchain"
  - "off-chain-storage"
  - "partial-merkle-trie"
  - "verifiable-off-chain-execution"
  - "layer-2-dapp-transaction-processing"
  - "split-execute-merge"
  - "rsa-accumulator-state-digest"
  - "confidential-dapp-execution"
  - "cross-shard-transaction-execution"
  - "smart-contract-sharding"
  - "cross-chain-smart-contract-invocation"
  - "hybrid-concurrency-control"
  - "smart-contract-execution-secondary"
  - "nested-contract-transaction-execution"
  - "smart-contract-concurrency-control"
  - "subtransaction-level-rollback"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-tell-leaderless-consensus-execution"
  - "nahida-knowledge-20260621-ahl-sharding"
  - "nahida-knowledge-20260622-blockchain-meets-database"
  - "nahida-knowledge-20260622-transactional-perspective-eov"
  - "nahida-knowledge-20260622-fabric-plus-plus-transaction-processing"
  - "nahida-knowledge-20260622-nezha-dag-transaction-processing"
  - "nahida-knowledge-20260622-slimchain-stateless-execution-storage"
  - "nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution"
  - "nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts"
  - "nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation"
  - "nahida-knowledge-20260623-dtvm-smart-contract-execution"
  - "nahida-paper-intake-20260623-loom-nested-contract-transactions"
source_refs:
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "arxiv:1804.00399v4"
  - "arxiv:1903.01919v2"
  - "arxiv:2003.10064v1"
  - "doi:10.1145/3299869.3319883"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
  - "arxiv:2504.16552v2"
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
confidence: "medium"
trust_tier: "primary"
---

# Blockchain transaction processing

## 定义与范围

- 定义: Blockchain transaction processing 是执行层的问题节点，关注交易在区块链节点内如何被执行、检测冲突、提交、abort、重执行，并最终形成所有正确节点一致的状态。
- 不包含: 经典数据库 transaction processing 的完整 foundation；那属于 [[04_Knowledge/distributed-systems/transaction-processing|Distributed systems transaction processing]]。本节点只处理区块链语境中的 ordering/execution/finality/stateDB 边界。
- Canonical terms: `blockchain transaction processing`, `transaction execution protocol`, `parallel blockchain execution`.
- Retrieval role: 回答“某篇论文/系统如何处理区块链交易执行”时先从本节点进入，再按具体问题进入 child node 或 source。
- Update scope: 新资料涉及 parallel execution、ODCC、deterministic concurrency control、execution scheduling、commit epoch、stateDB、cross-shard transactions 时刷新。

## 背景

在 Ordering-Execution 范式中，consensus 通常先给交易或区块一个确定顺序，execution 再更新本地状态。但现代许可链和并行区块链不一定能把这两个步骤机械串联: 如果 consensus 是 leaderless/multi-leader，多条 instance 会并行产块；如果 execution 想利用多核，就需要并行执行交易并处理冲突；如果 blocks 到达顺序不稳定，还要保证 speculative execution 的最终状态与顺序执行一致。

因此，本节点聚焦的不是“数据库事务理论本身”，而是数据库/并发控制思想进入区块链后，与 consensus order、block height、stateDB、shard boundary 和 deterministic replay 的交界。AHL 补充了一个 cross-shard general-workload route: 把 2PC/2PL 拆入 prepare/commit/abort chaincode，并用 BFT reference committee 防止 malicious coordinator indefinite blocking。LightCross 把该 candidate 提升成独立问题节点: arbitrary smart-contract CSTx 可以由 TEE executor 执行，再由 R-shard 排序和 S-shards 验证 stale reads/commit write sets。Blockchain Meets Database 进一步补上数据库-backed execution route: 不是把数据库当作普通状态后端，而是让 PostgreSQL 的 SSI/MVCC/stored procedures/provenance 能力在外部 ordering service 和互不信任副本模型下成为执行层 substrate。Fabric++ 补上 Fabric EOV 管线内的原始数据库视角: vanilla Fabric 的 arrival order 会造成可避免的 validation abort，block-local transaction reordering 和 early abort 可以提高 successful throughput。A Transactional Perspective on Execute-Order-Validate Blockchains 则进一步把 EOV-specific route 推进到跨 pending transactions 的 OCC/serializability 依赖图分析。Nezha 补入 DAG-based blockchain 路线: 当多个 blocks 在同一 epoch 并发产生时，执行层可用 address-based conflict graph 和 hierarchical sorting 避免普通 transaction-pair conflict graph 在高冲突下的构图和 cycle removal 开销。SlimChain 补入 stateless blockchain 路线: 当 consensus nodes 不保存 full state 时，交易处理必须携带 off-chain execution evidence、read/write sets、write proofs 和 recent-window conflict metadata，才能完成 commit/abort 和 state-root update。L2chain 进一步补入 layer-2 DApp execution route: L1 validators 只维护可用状态摘要，DApp executors 通过 RSA accumulator split/merge 受影响状态子集，并在 TEE 中按 L1 已提交 split 事务执行加密批次。

ShuttleCross 是 supporting seed：它不改变本节点的主层次，但说明 transaction-processing 机制也会出现在 [[cross-chain-smart-contract-invocation|cross-chain smart contract invocation]] 中。它把 OCC/S2PL、wait-for graph、serializability conflict graph 和 read-only fast path 改写成跨链 invocation 的 HCC/read-write separation 机制。

DTVM 也是 supporting seed，但边界相反：它的 primary problem 是 [[smart-contract-execution|smart contract execution]]，而不是交易排序或并发控制。它进入本节点只用于说明 smart-contract runtime 的 gas metering、trap semantics、JIT first-invocation latency 和 EVM/Wasm execution performance 会影响交易执行成本与节点 replay latency。

## 解决的问题

本节点回答: 在已有或动态形成的区块/交易顺序下，节点如何高效执行交易并保持确定性状态一致。

关键子问题:

- block 内交易如何并行执行并保持 serializable/deterministic 结果。
- block 间或 instance 间如何处理 out-of-order、slow instance、merge/re-execution。
- 执行层何时应该感知 consensus 的实例状态或 ordering unit。
- execution optimization 的边界在哪里，哪些问题仍属于 consensus safety 或 mempool/data availability。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[execution-and-transactions|Blockchain execution and transactions]] | child_of | TELL source classification | active_seed |
| [[04_Knowledge/distributed-systems/transaction-processing|Distributed transaction processing]] | bridge/adjacent foundation | shared terms: transaction execution, concurrency control, commit/abort | review |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[leaderless-consensus-execution|Leaderless consensus execution]] | method_family/subproblem | TELL 明确将 execution protocol 绑定到 leaderless consensus instance 结构，且未来可承接 RCC/MIR-BFT/DAG execution sources | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | active_seed |
| optimistic-deterministic-concurrency-control | method candidate | TELL 使用 ODCC/backward dangerous structure；需要更多来源判断是否独立 | TELL only | review |
| [[cross-shard-transaction-execution|Cross-shard transaction execution]] | problem | AHL/ByShard/RingBFT/LightCross 已经形成跨片交易/智能合约执行的独立问题层 | [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]]; AHL/ByShard/RingBFT source notes | active_seed |
| [[nested-contract-transaction-execution|Nested contract transaction execution]] | problem | Loom 说明嵌套合约调用会把交易处理粒度从整笔交易推进到 subtransaction-level rollback/reschedule，且需要同时引用智能合约调用结构和确定性交易执行约束。 | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | active_seed |
| blockchain-relational-databases | method/system candidate | 关系数据库可作为 permissioned blockchain execution substrate，但目前只有 Blockchain Meets Database 作为直接强 source | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] | review |
| execute-order-validate | method/architecture candidate | Fabric++ 与 FabricSharp/FastFabricSharp 已形成 EOV transaction-processing 路线，但还需要 Nezha/parallel execution/modern Fabric 对照再决定是否拆出 child | [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]]; [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective]] | review |
| dag-based-blockchain-concurrency-control | method/problem candidate | Nezha 说明 DAG/main-chain/parallel-chain block concurrency 会把执行层冲突放大，需要地址级依赖和确定性排序；当前只有单篇强 source，先保留为 method row。 | [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] | review |
| stateless-blockchain-transaction-processing | method/problem candidate | SlimChain 说明当 consensus node 只保存 state root/transaction digests 时，执行层需要 off-chain execution proof、write proof、partial commitment 和 recent-window OCC/SSI；当前先保留为 method row，等待 stateless clients/Verkle/state expiry sources。 | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | review |
| layer-2-dapp-transaction-processing | method/problem candidate | L2chain 说明 DApp 交易处理可以通过 L1 state-digest split/merge、L2 local consensus、TEE two-step execution 和 witness cache 形成 L2 route；当前只有单篇 direct source，先保留为 method row。 | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Sequential replay | 按链上顺序逐个执行交易 | 低吞吐、低冲突或简单系统 | 无法充分利用并行硬件 | model_prior_background |
| Intra-block parallel execution | block 内交易并行执行，再用读写集合检测冲突并重执行 abort 交易 | block 内存在可并行交易，读写集合可被记录 | 高 skew 时 abort/re-execution 上升 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| Speculative block execution | 乱序收到 block 时先执行，再在缺失 block 到达后检测 WAR/WAW 并修正 | 网络导致同一 instance blocks out-of-order | 需要 deterministic MVCC 或等价机制防止 update lost | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| Inter-instance merge | 多个 consensus instances 独立执行后，周期性检测跨实例冲突并合并执行结果 | leaderless/multi-leader consensus | conflict skew 和实例数会推高 abort rate | [[leaderless-consensus-execution|Leaderless consensus execution]] |
| Dynamic commitment unit | ordering/merge unit 随 instance block-producing interval 调整，减少快 instance 等待慢 instance | instances 速度差异显著且 timestamp 可被确认 | 依赖 consensus-confirmed timestamps 和阈值检查 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| Cross-shard 2PC/2PL execution | 将一个跨 shard 交易拆成 prepare/commit/abort stages，用 locks 维持 isolation，用 BFT reference committee 推进 commit/abort decision | sharded permissioned blockchain general workload | 应用需要拆分 chaincode；reference committee 可能成为瓶颈；2PL contention 会导致 abort/latency | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] |
| TEE-backed cross-shard smart-contract execution | 将 arbitrary CSTx 放入 TEE executor，读取 authenticated shard state 并生成 read/write/certificate；R-shard 批量排序，S-shards bitmap validation 后提交。 | permissioned smart-contract sharding; shard-level BFT and TEE accepted | TEE/R-shard/executor availability; stale-read abort; contract migration depends on workload stability | [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] |
| Database-backed order-then-execute | consensus 先排序 block，数据库节点并行执行 block 内交易，再按 block 内顺序用 SSI commit/abort | permissioned blockchain; 关系数据库可执行 deterministic stored procedures | ordering service 仍是瓶颈；需要禁用非确定性 SQL/procedure 能力 | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] |
| Execute-and-order-in-parallel with block-height SSI | 交易按 snapshot-height 先执行，同时 ordering service 形成 block；commit 时用 creator/deleter block number 和 block-aware abort rule 保持所有节点一致 | 需要重叠执行与排序、支持复杂 SQL smart contracts | 不支持 blind updates；predicate reads 依赖索引；更保守 abort 换确定性一致 | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] |
| Fabric++ block-local reordering and early abort | 用 read/write set 构建 block 内 conflict graph，删除 cycle 中的部分交易并重排剩余交易；同时在 simulation/order 阶段提前 abort stale 或版本冲突交易 | Hyperledger Fabric-style simulate-order-validate pipeline with visible readsets/writesets | 只在 block 内重排；cycle breaking 启发式不保证最少 abort；交易访问集合可见性有隐私边界 | [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] |
| OCC-inspired EOV dependency reordering | 在 Fabric/FastFabric 的 execute-order-validate pipeline 中，把交易读写集映射为 snapshot transaction dependency graph；arrival 时提前丢弃不可重排 cycle，block formation 时拓扑排序 pending transactions 并恢复 `c-ww` 依赖 | permissioned EOV chains; endorsement/simulation 产生 readset/writeset；orderer 可确定性复制 reordering | Bloom filter false positives、`max_span` stale snapshot pruning、transaction-detail disclosure 的 liveness/security 边界；不替代 consensus safety | [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]] |
| DAG-based address-dependency scheduling | 对同一 epoch 的并发 blocks，先并发模拟交易并记录 read/write addresses，再构造 address-based conflict graph；用 hierarchical sorting 给地址和交易分配 deterministic sequence，避免普通 CG 的交易对构图和 cycle removal。 | main-chain/parallel-chain DAG-based blockchains，account-based data model，交易 read/write addresses 可记录。 | 不适用于 UTXO/natural-DAG irregular topology；不提供 consensus safety；高复杂 smart contract workload 需要额外实测。 | [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] |
| Stateless off-chain execution with on-chain commitment | Storage nodes 执行 smart contracts 并提交 read/write sets、TEE/VC/policy evidence 和 `pi_write`；consensus nodes 用 recent-window read/write maps、OCC/SSI 和 partial Merkle trie 验证交易并更新 state root。 | consensus nodes 不保存 full state/full transaction data，且 off-chain storage/execution nodes 可提供可验证 evidence。 | 依赖 TEE/VC/policy execution proof、storage-node availability、`k`-block freshness window 和 proof bandwidth；不等于 consensus sharding。 | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] |
| Layer-2 split-execute-merge DApp processing | DApp executors 先在 L2 排序并模拟交易批次，向 L1 split 受影响状态子集，待 split 事务上链后在 TEE 中执行加密批次，再把更新后的状态摘要 merge 回 L1。 | DApp 有 on-chain SLA、L2 executor group 和可被 accumulator 承诺的状态子集；L1 只需验证 split/merge 摘要和 TEE 证明。 | 依赖 TEE 和 RSA accumulator；witness generation/update 有成本；状态子集冲突会导致 split discard；不覆盖 DA、rollup fraud/validity proofs 或完整 L2 经济模型。 | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] |
| Cross-chain hybrid concurrency control | 对 target-chain states 动态选择 OCC `opList` 或 S2PL `lockList`，并用 wait-for graph 检测跨链事务死锁；read-only invocations 可先 off-chain 执行，再以正式链上版本匹配保持可见性。 | 跨链 smart-contract workflow 需要 serializability 且存在状态争用/读多写少场景。 | 属于跨链问题的 supporting evidence；origin-chain coordination、target-chain consensus latency 和 inter-chain messages 不属于普通本地执行层。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] |
| Deterministic smart-contract runtime as execution-cost substrate | VM/runtime 层定义 gas、trap、host API、memory bounds 和 JIT/interpretation 性能，从而影响交易执行成本和 replay latency。 | 交易负载主要由智能合约 VM 执行决定，且节点需要确定性 replay。 | 不处理交易排序、读写冲突、block commit 或 consensus safety；primary placement 是 [[smart-contract-execution|Smart contract execution]]。 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] |
| Nested contract subtransaction scheduling | 将跨合约调用树拆为 subtransactions，用 weak/strong dependency、HDG/SAT/GWG 选择部分 rollback，并在确定性序列下做 fine-grained re-execution。 | Permissioned blockchain 中已排序区块内存在长 nested contract call chains 和高冲突率。 | 不定义 VM gas/trap/ABI；依赖所有节点能确定性捕获调用树/读写集并应用相同 rollback/reschedule。 | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus]] | paper | 将 blockchain transaction processing 从普通并行执行推进到 consensus-aware execution: SHT、speculative execution、inter-instance merging、DCE | same-data-center; RCC+PBFT; throughput excludes consensus latency | p1-p13 |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | 将 cross-shard transaction execution 扩展到 general workload：2PC/2PL、BFT reference committee、prepare/commit/abort chaincode locks | TEE/reference committee assumptions; manual chaincode refactoring; GCP sharding result excludes reference committee in final large run | §6.1-§7.3 |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts]] | paper | 将 arbitrary smart-contract CSTx 路线补入交易处理层：TEE executor 执行、R-shard 排序、S-shard bitmap validation、contract migration 降低 CSTx ratio。 | TEE/R-shard/executor availability assumptions; permissioned FISCO-BCOS prototype; stale-read aborts remain possible. | §III-§V, Appendix |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database: Design and Implementation of a Blockchain Relational Database]] | paper | 将 PostgreSQL/SSI/MVCC/stored procedures/provenance 迁移到 permissioned blockchain execution，提出 order-then-execute 和 execute-and-order-in-parallel 两条路线 | checkpoint flow 未实现；只面向 permissioned setting；block-height SSI 对索引和确定性 SQL 有约束 | p1-p15 |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Blurring the Lines between Blockchains and Database Systems: the Case of Hyperledger Fabric]] | paper | 将 Fabric 的 simulate-order-validate 管线解释为数据库式事务管理问题，提出 Fabric++ block-local transaction reordering 和 early abort | Fabric/Fabric++ source instance; block-local scope; 评估基于 permissioned LAN 和 Fabric 当时实现 | p1-p18 |
| [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on Execute-Order-Validate Blockchains]] | paper | 将 EOV 区块链无效交易问题形式化为 OCC/serializability/reorderability 问题，提出 FabricSharp/FastFabricSharp 在 orderer 侧提前过滤不可重排交易并重排剩余交易 | permissioned EOV setting; liveness/security 依赖交易 hash 先排序后披露等约束；Bloom filter/pruning 可能导致额外 abort | p1-p17 |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha: Exploiting Concurrency for Transaction Processing in DAG-based Blockchains]] | paper | 将 DAG-based blockchain 并发块执行中的冲突控制抽象为地址依赖排序问题，提出 ACG + HS 以减少 CG 构图、cycle detection/removal 和串行提交开销。 | OHIE/EVM/LevelDB prototype；account-based model；Alibaba Cloud 14-node SmallBank workload；不覆盖 UTXO/natural DAG 或生产 parallel EVM。 | p1-p11 |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing]] | paper | 将 stateless blockchain 的交易处理抽象为 off-chain execution + read/write evidence + partial authenticated commitment update；用 OCC/SSI 在 recent-window metadata 上做 commit/abort。 | SGX-centered prototype；storage-node availability/serving incentives not solved；storage sharding does not scale consensus layer。 | p1-p13 |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications]] | paper | 将 layer-2 DApp transaction processing 抽象为 split-execute-merge：L2 排序/TEE 执行，L1 只 split/merge accumulator state digest。 | TEE trust; RSA accumulator witness overhead; state contention discards split transactions; not a full rollup/DA/fraud-proof architecture. | p1-p14 |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross: An Efficient Cross-Chain Smart Contract Invocation Framework]] | paper | supporting seed: 将 OCC/S2PL、wait-for graph 和 serializability 分析迁移到跨链合约调用执行，用 HCC 和 dual-processing read-only invocation 降低 abort/latency。 | Manuscript proof；ChainMaker/TBFT prototype；primary placement is cross-chain smart contract invocation rather than local blockchain transaction processing。 | p1-p12 |
| [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM: Revolutionizing Smart Contract Execution with Determinism and Compatibility]] | paper | supporting seed: 将 smart-contract VM/runtime 的确定性、gas/trap、JIT first-invocation latency 和 EVM/Wasm execution performance 作为交易执行成本底座补入。 | Primary placement is smart-contract-execution; not a transaction ordering/concurrency-control paper. | Abstract, §3-§5 |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom: A Deterministic Execution Framework Towards Nested Contract Transactions]] | paper | 将 nested contract transaction execution 拆为独立 active seed；补入 subtransaction-level deterministic rollback/reschedule 与跨区块 snapshot pipeline。 | Permissioned prototype; TPC-C-like smart contracts; assumes deterministic ordering service; not a VM runtime or consensus paper. | p1-p14 |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`。
- Freshness: `fresh` for current-vault evidence, not a latest-news claim。
- 综合: 当前节点是 `foundation_thin`。TELL 提供的可复用结构是: 在区块链中，transaction processing 不只是数据库式并发控制，还要尊重 consensus 所产生的 block/instance/epoch 结构。AHL 提供的可复用结构是: 在 sharded blockchain 中，跨片交易执行需要把 database-style 2PC/2PL 包进 shard consensus 和 BFT coordinator availability 之中。LightCross 证明这个问题已经足够独立: 任意智能合约 CSTx 不一定要拆成 shard-local fragments，可以由 TEE executor 执行，再由 R-shard/S-shards 完成排序、stale-read validation 和 write-set commit。Blockchain Meets Database 补充了更直接的 database-backed execution route: 关系数据库的 SSI/MVCC/stored procedures 可以迁移进许可链执行层，但必须用 block order、block-height visibility 和 block-aware abort rules 改造数据库默认信任模型。Fabric++ 与 A Transactional Perspective on EOV Blockchains 共同形成 EOV 路线: Fabric++ 先显示 block-local conflict graph reordering 和 early abort 能减少 invalid transactions，后者进一步用 OCC/serializability 依赖图扩展到更细粒度的 pending transaction scheduling。Nezha 新增 DAG-based blockchain 路线: 当 block concurrency 来自 DAG/parallel-chain block production 时，执行层可以按地址而不是按交易对构造 conflict graph，用 hierarchical sorting 输出带并发度的 deterministic commit order。SlimChain 新增 stateless/off-chain route: 当 consensus nodes 只保存 transaction digests 和 state roots 时，交易处理协议必须把 execution evidence、read/write sets、write proofs、partial Merkle trie 和 recent-window OCC/SSI 组合起来，才能在不保存 full state 的情况下验证并提交 smart-contract 交易。L2chain 新增 layer-2 DApp route: 当 L1 只维护可用状态摘要时，DApp 交易处理要把 L2 local ordering、L1 split/merge commitment、TEE two-step execution 和 accumulator witness maintenance 组合起来，才能在保密执行和状态一致性之间建立可验证边界。

- ShuttleCross delta: ShuttleCross 补充一个跨链 supporting route。transaction-processing 机制在多链调用里必须和 origin-chain 2PC、target-chain transaction-pool/consensus latency、inter-chain timeout/polling 结合，因此它的 primary placement 是 [[cross-chain-smart-contract-invocation|cross-chain smart contract invocation]]，在本节点只作为 HCC/read-write separation 的 secondary evidence。
- DTVM delta: DTVM 补充 runtime-side supporting evidence。transaction processing 的执行成本不只来自读写冲突或排序，还来自 VM 是否能确定地计费、处理 trap、执行 host API 并降低 first invocation latency；但这些机制的完整解释应进入 [[smart-contract-execution|Smart contract execution]]。
- Loom delta: Loom 把 smart-contract invocation structure 变成 transaction-processing granularity。它不是把 DTVM 的 runtime 问题继续展开，而是说明当合约调用形成 nested transaction tree 时，执行层需要按 subtransaction 记录依赖、选择部分 rollback、重调度并维护 deterministic serializability。因此它推动 [[nested-contract-transaction-execution|Nested contract transaction execution]] 成为本节点的 active child problem。
- L2chain delta: L2chain 不是 validator sharding，也不是完整 rollup foundation。它给本节点补的是 L2 DApp transaction processing route: split 事务把受影响状态从 L1 available-state digest 中锁出，execute 阶段只在 split 上链后由 TEE 执行加密批次，merge 事务再把更新后的 digest 并回 L1。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | 增加 leaderless-consensus-aware transaction processing 路线；SHT/DCE 作为 source-specific mechanisms 保留在 source note | 方法族; 下级结构; 代表 Sources; Bridge Links | yes | 后续吸收 Nezha/SChain/Fabric++/Harmony/parallel EVM 时复核 child split |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] | 增加 cross-shard transaction execution 路线：reference committee + 2PC/2PL + chaincode locks | 方法族; 下级结构; 代表 Sources | no | 已由 LightCross 触发独立节点，后续用 Chainspace/CAPER/SharPer 细分方法族 |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] | 新增 TEE executor + R-shard batch validation + contract migration 路线，并将 cross-shard transaction execution 提升为 active child problem。 | 下级结构; 方法族; 代表 Sources; 当前综合 | yes, promotes child node | 后续吸收 OptChain/Chainspace/CAPER/SharPer 时复核 child split |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] | 新增 database-backed blockchain execution route：order-then-execute with SSI、execute-and-order-in-parallel、block-height SSI、PostgreSQL provenance | 方法族; 代表 Sources; Bridge Links; 当前综合 | yes, creates bridge | 后续用 Fabric++/Veritas/BigchainDB/parallel execution sources 继续检验边界 |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] | 新增 Fabric EOV 原始路线：block-local read/write conflict graph reordering、cycle-breaking abort、simulation/order early abort、unique-key-aware batch cutting。 | 下级结构; 方法族; 代表 Sources; Bridge Links; 当前综合 | no, strengthens bridge | 与 FabricSharp/FastFabricSharp、Nezha 和 parallel execution sources 一起复核 `execute-order-validate` child split |
| [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]] | 新增 EOV-specific OCC route：snapshot consistency、Strong Serializability vs Serializability、dependency graph filtering、topological pending transaction reordering、FabricSharp/FastFabricSharp | 方法族; 代表 Sources; Bridge Links; 当前综合 | no, strengthens bridge | 等 Fabric++ 原论文和更多 parallel blockchain execution sources 后复核是否拆 `execute-order-validate` child |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] | 新增 DAG-based blockchain concurrency-control route：ACG 按地址收集 read/write units，HS 通过 address ranks 和 sequence numbers 输出 deterministic commit order，并在高 skew 下减少 CG latency/abort。 | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | no, strengthens bridge | 等 SlimChain/SChain/parallel EVM/DAG execution sources 后复核 `dag-based-blockchain-concurrency-control` 是否拆 child |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | 新增 stateless/off-chain transaction-processing route：storage nodes 执行并证明 smart contracts，consensus nodes 用 partial Merkle trie、write proof 和 recent-window OCC/SSI 更新 state root。 | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes, creates state-storage bridge | 等 stateless clients/Verkle/state expiry/off-chain execution sources 后复核是否拆 `stateless-blockchain-transaction-processing` child |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | 新增 layer-2 DApp SEM route：L2 排序/TEE 执行，L1 split/merge RSA accumulator state digest，并用 two-step execution 降低 rollback attack 风险。 | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | no, strengthens state-storage bridge | 等 rollup/L2 architecture、RSA accumulator foundation 和 TEE rollback-mitigation sources 后复核是否拆 child |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | 新增 cross-chain HCC/read-write separation supporting route：OCC/S2PL/wait-for graph/serializability 被改写到跨链合约调用执行。 | 方法族; 代表 Sources; 当前综合; 关系图谱 | no, supporting evidence | 后续吸收 GPACT/2PC4BC/EOVPC/Avalon 后复核是否需要 cross-chain invocation concurrency child。 |
| [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] | 新增 smart-contract runtime supporting route：gas/trap/JIT/VM determinism 影响交易执行成本，但 primary placement 保持在 smart-contract-execution。 | 方法族; 代表 Sources; 当前综合; 关系图谱 | no, supporting evidence | 通过 [[smart-contract-execution|Smart contract execution]] 维护，不拆 DTVM 节点 |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | 新增 nested contract transaction execution route：subtransaction-level rollback/reschedule 让交易处理显式依赖智能合约调用树。 | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links; 关系图谱 | yes, creates active child problem | 后续吸收 EOR/Block-STM/parallel EVM 后复核子方法拆分 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[permissioned-consensus-to-transaction-execution|Permissioned consensus -> transaction execution]] | `blockchain-systems/consensus/permissioned-blockchain-consensus; blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution` | dependency, co_evolution, implementation_reuse, tension | execution scheduling can depend on consensus instance structure; consensus safety does not come from execution protocol. | active_seed |
| [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] | `distributed-systems/transaction-processing; blockchain-systems/execution-and-transactions/transaction-processing` | translation, implementation_reuse, dependency, trust_model_shift | 可迁移的是 SSI/MVCC/stored procedures/provenance 等执行层机制；不可迁移的是共识 safety、开放网络身份/激励和 Byzantine ordering。 | active_seed |
| [[blockchain-state-storage-to-transaction-processing|Blockchain state storage -> transaction processing]] | `blockchain-systems/data-management-and-storage/blockchain-state-storage; blockchain-systems/execution-and-transactions/transaction-processing` | dependency, shared_state_commitment, implementation_reuse, tension | state commitment/proof format constrains validation and commit; it does not provide execution correctness, DA, storage-node liveness or consensus safety. | active_seed |
| [[smart-contract-execution-to-transaction-processing|Smart contract execution -> blockchain transaction processing]] | `blockchain-systems/execution-and-transactions/smart-contract-execution; blockchain-systems/execution-and-transactions/transaction-processing` | dependency, granularity_shift, conflict_modeling, execution_cost_substrate | Contract call structure and runtime costs can affect transaction-processing granularity and cost; VM semantics, consensus ordering and serializability remain separate boundaries. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-blockchain-transaction-processing | is_a | nahida-knowledge-blockchain-execution-and-transactions | vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | has_child | nahida-knowledge-leaderless-consensus-execution | vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution.md | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | has_child | nahida-knowledge-cross-shard-transaction-execution | vault/04_Knowledge/blockchain-systems/execution-and-transactions/cross-shard-transaction-execution.md | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | has_child | nahida-knowledge-nested-contract-transaction-execution | vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/nested-contract-transaction-execution.md | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | bridges_to | nahida-bridge-permissioned-consensus-to-transaction-execution | vault/05_Bridges/permissioned-consensus-to-transaction-execution.md | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | bridges_to | nahida-bridge-database-transaction-processing-to-blockchain-execution | vault/05_Bridges/database-transaction-processing-to-blockchain-execution.md | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md | TELL source note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | AHL source note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md | Blockchain Meets Database source note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md | Fabric++ source note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md | A Transactional Perspective on EOV Blockchains source note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md | Nezha source note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | bridges_to | nahida-bridge-blockchain-state-storage-to-transaction-processing | vault/05_Bridges/blockchain-state-storage-to-transaction-processing.md | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md | SlimChain source note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md | L2chain source note; state-storage bridge | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md | LightCross source note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md | ShuttleCross source note | high | supporting_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md | DTVM source note; smart-contract-execution node | medium | supporting_seed |
| nahida-knowledge-blockchain-transaction-processing | bridges_to | nahida-bridge-smart-contract-execution-to-transaction-processing | bridge note | high | active_seed |
| nahida-knowledge-blockchain-transaction-processing | evidenced_by | vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md | Loom source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 缺少更完整 blockchain parallel/stateless/nested/L2 execution source set。 | TELL、Blockchain Meets Database、Fabric++、A Transactional Perspective、Nezha、SlimChain、L2chain 和 Loom 已形成执行层并发/无状态/L2/嵌套执行路线，但仍需要 SChain、parallel EVM、Block-STM、EOR、stateless clients、Verkle/state-expiry、rollup/L2 architecture 等判断是否拆多个 child method families。 | continue paper intake or `nahida-research-search` | high | queued |
| 经典 SSI/OCC/serializability foundation 仍缺直接 source。 | Blockchain Meets Database 和 A Transactional Perspective 都提供强迁移证据，但不是数据库事务教材；后续需要直接 foundation source 支撑并发控制概念。 | `nahida-research-search` foundation_pack | medium | queued |
| cross-shard transaction execution 的方法族还薄。 | LightCross 已推动该问题成为 active node，但 Chainspace/CAPER/SharPer/OptChain 等 source 仍缺，暂不拆更细 child。 | continue paper intake | medium | queued |
| cross-chain invocation concurrency control 还是单 source supporting route。 | ShuttleCross 显示 HCC 在跨链调用中重要，但需要 GPACT/2PC4BC/EOVPC/Avalon direct sources 判断是否拆子节点。 | continue paper intake or `nahida-research-search` | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-tell-leaderless-consensus-execution | Created blockchain transaction-processing problem node and child leaderless-consensus execution method family. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-ahl-sharding | Added AHL as cross-shard transaction execution source extension under transaction processing. | arxiv:1804.00399v4 | codex |
| 2026-06-22 | nahida-knowledge-20260622-blockchain-meets-database | Added database-backed blockchain execution, block-height SSI, and bridge to distributed transaction processing. | arxiv:1903.01919v2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-transactional-perspective-eov | Added OCC-inspired EOV dependency reordering route and strengthened database transaction-processing bridge. | arxiv:2003.10064v1 | codex |
| 2026-06-22 | nahida-knowledge-20260622-fabric-plus-plus-transaction-processing | Added Fabric++ transaction reordering and early abort as the original Fabric EOV database-inspired source route. | doi:10.1145/3299869.3319883 | codex |
| 2026-06-22 | nahida-knowledge-20260622-nezha-dag-transaction-processing | Added Nezha as DAG-based blockchain concurrency-control source extension with ACG and hierarchical sorting route. | doi:10.1109/icdcs54860.2022.00034 | codex |
| 2026-06-22 | nahida-knowledge-20260622-slimchain-stateless-execution-storage | Added SlimChain as stateless off-chain execution and commitment-backed transaction-processing source; created state-storage bridge. | doi:10.14778/3476249.3476283 | codex |
| 2026-06-23 | nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution | Added L2chain as layer-2 split-execute-merge DApp transaction-processing route and strengthened state-storage bridge. | doi:10.14778/3574245.3574278 | codex |
| 2026-06-22 | nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts | Promoted cross-shard transaction execution to an active child problem and added LightCross as TEE-backed smart-contract CSTx route. | sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation | Added ShuttleCross as a supporting cross-chain HCC/read-write-separation transaction-processing route while keeping primary placement under interoperability. | sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72 | codex |
| 2026-06-23 | nahida-knowledge-20260623-dtvm-smart-contract-execution | Added DTVM as secondary runtime-cost evidence while keeping primary placement under smart-contract-execution. | arxiv:2504.16552v2 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-loom-nested-contract-transactions | Added Loom as nested-contract transaction execution source; created active child problem and smart-contract execution bridge. | sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd | codex |
