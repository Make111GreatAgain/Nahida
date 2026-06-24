---
id: "nahida-knowledge-transaction-processing"
title: "Transaction processing"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "transaction-processing"
domain_id: "distributed-systems"
direction_id: "transaction-processing"
parent_knowledge_refs:
  - "nahida-knowledge-distributed-systems"
child_knowledge_refs:
  - "nahida-knowledge-distributed-transactions"
  - "nahida-knowledge-replicated-database-concurrency-control"
ontology_path:
  - "distributed-systems"
  - "transaction-processing"
primary_ontology_path: "distributed-systems/transaction-processing"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-transaction-processing"
    relation: "is_a"
    to: "nahida-knowledge-distributed-systems"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/transaction-processing.md"
      - "vault/04_Knowledge/distributed-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "has_child"
    to: "nahida-knowledge-distributed-transactions"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/transaction-processing.md"
      - "vault/04_Knowledge/distributed-systems/transaction-processing/distributed-transactions.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "has_child"
    to: "nahida-knowledge-replicated-database-concurrency-control"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/transaction-processing.md"
      - "vault/04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control.md"
      - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "bridges_to"
    to: "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
    evidence_refs:
      - "vault/05_Bridges/database-transactions-to-byzantine-sharded-ledgers.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "bridges_to"
    to: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    evidence_refs:
      - "vault/05_Bridges/database-transaction-processing-to-blockchain-execution.md"
      - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "bridges_to"
    to: "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
    evidence_refs:
      - "vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-transaction-processing"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-atomic-cross-chain-transactions.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
  - "nahida-bridge-database-transaction-processing-to-blockchain-execution"
  - "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
  - "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
  - "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
  - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
  - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
  - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
  - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
  - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
  - "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
  - "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
representative_source_refs:
  - "doi:10.14778/3476249.3476275"
  - "arxiv:1804.00399v4"
  - "arxiv:1903.01919v2"
  - "arxiv:2003.10064v1"
  - "doi:10.1145/3299869.3319883"
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "arxiv:2207.02746"
  - "sha256:e1d0bc04b53e5702d2f0d52b5bb1e561ff25fdf3490402c98abdb94c81281818"
  - "doi:10.14778/3561261.3561268"
query_keys:
  - "transaction processing"
  - "distributed transaction processing"
  - "database transaction protocols"
  - "serializable snapshot isolation"
  - "MVCC"
  - "block-height SSI"
  - "optimistic concurrency control"
  - "serializability"
  - "EOV transaction processing"
  - "transaction reordering"
  - "early abort"
  - "Hyperledger Fabric transaction processing"
  - "atomic commit across blockchains"
  - "atomic cross-chain transactions"
  - "witness network atomic commitment"
  - "cross-chain deals"
  - "adversarial commerce"
  - "address-based conflict graph"
  - "DAG blockchain concurrency control"
  - "replicated database concurrency control"
  - "primary-backup replication"
  - "cloned concurrency control"
  - "monotonic prefix consistency"
  - "bounded replication lag"
  - "Calvin"
  - "deterministic database systems"
  - "deterministic transaction scheduling"
  - "deterministic locking"
  - "transaction input replication"
  - "contention footprint"
  - "sequencer scheduler storage architecture"
  - "OLLP"
  - "Starry"
  - "semi-leader transaction commit"
  - "multi-master transaction processing"
  - "storage-layer transaction commit"
  - "conflict-path reordering"
aliases:
  - "distributed transaction processing"
  - "database transaction processing"
  - "atomic commit"
  - "adversarial commerce"
  - "primary-backup concurrency control"
  - "cloned concurrency control"
  - "deterministic transaction scheduling"
  - "deterministic database systems"
domains:
  - "distributed-systems"
topics:
  - "transaction-processing"
  - "serializable-snapshot-isolation"
  - "database-backed-blockchain-execution"
  - "optimistic-concurrency-control"
  - "execute-order-validate"
  - "transaction-reordering"
  - "early-abort"
  - "atomic-commit"
  - "conflict-graph-scheduling"
  - "replicated-database-concurrency-control"
  - "primary-backup-replication"
  - "deterministic-transaction-scheduling"
  - "transaction-input-replication"
  - "multi-master-transaction-processing"
  - "semi-leader-commit-protocol"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-repair-pass"
  - "nahida-knowledge-20260621-ahl-sharding"
  - "nahida-knowledge-20260622-blockchain-meets-database"
  - "nahida-knowledge-20260622-transactional-perspective-eov"
  - "nahida-knowledge-20260622-fabric-plus-plus-transaction-processing"
  - "nahida-knowledge-20260622-atomic-cross-chain-transactions"
  - "nahida-knowledge-20260622-cross-chain-deals"
  - "nahida-knowledge-20260622-nezha-dag-transaction-processing"
  - "nahida-knowledge-20260623-c5-cloned-concurrency-control"
  - "nahida-paper-intake-20260623-calvin"
  - "nahida-knowledge-20260623-starry-multi-master-transaction-processing"
source_refs:
  - "doi:10.14778/3476249.3476275"
  - "arxiv:1804.00399v4"
  - "arxiv:1903.01919v2"
  - "arxiv:2003.10064v1"
  - "doi:10.1145/3299869.3319883"
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "arxiv:2207.02746"
  - "sha256:e1d0bc04b53e5702d2f0d52b5bb1e561ff25fdf3490402c98abdb94c81281818"
  - "doi:10.14778/3561261.3561268"
confidence: "medium"
trust_tier: "primary"
---

# Transaction processing

## 定义与范围

- 定义: Transaction processing 是分布式系统中组织读写操作、提交/中止决策、并发控制、隔离级别与恢复边界的方向。
- 当前 vault 覆盖: 来自 ByShard 对 two-phase commit、two-phase locking 和 sharded resilient systems 的复用，AHL 对 BFT reference committee coordinator route 的复用，Blockchain Meets Database 对 SSI/MVCC/stored procedures 在 permissioned blockchain execution 中的迁移，C5 对 primary-backup replicated databases 中 cloned concurrency control / bounded replication lag 的补入，Calvin 对 deterministic transaction scheduling / transaction input replication 的直接分布式数据库证据，Starry 对 multi-master cloud database storage-layer commit / conflict-path reordering 的直接证据，Atomic Commitment Across Blockchains 对 atomic commit / commit-abort decision 在 independent ledgers 中的改写，以及 Cross-chain Deals 对 atomic transaction correctness 在 adversarial commerce 中的重写。
- 不包含: 单个数据库系统、单个 ledger 协议或 ByShard 的完整协议细节；这些保留在 source note 或 child problem/source-extension 行里。
- Retrieval role: 让查询能从 distributed systems 进入 transaction-processing，再到 distributed transactions，而不是让 `database-transactions-to-byzantine-sharded-ledgers` bridge 指向不存在的端点。
- Update scope: 新吸收的 2PC、2PL、serializability、distributed database、cross-shard transaction source 应刷新本节点。
- Source drill-down boundary: 需要 ByShard 的 OEM、orchestration、execution 细节时再打开 source note。

## 背景

model_prior_background: transaction processing 通常处理 ACID 语义、atomic commit、concurrency control、isolation 和 recovery。Calvin 现在补入一条直接的分布式数据库系统证据：把事务输入排序和复制前移到执行前，再用确定性锁管理减少 2PC 在锁持有期间造成的竞争足迹。Starry 又补入另一条直接数据库证据：在 disaggregated cloud database 的 storage layer，用 semi-leader commit 把无冲突事务的去中心化 fast path 和冲突事务的 sequencer conflict graph reordering 分开。但当前 vault 仍缺经典 2PC/2PL/OCC/serializability/recovery 的系统 foundation pack。ByShard 是一个从 Byzantine sharded systems 反向暴露出该方向缺口的 source extension。Blockchain Meets Database 不是经典事务教材，但它直接展示了 SSI/MVCC、stored procedures、transaction logs 和 provenance tables 如何在新的 trust model 中迁移到 blockchain execution。Fabric++ 和 A Transactional Perspective on Execute-Order-Validate Blockchains 也不是数据库事务 foundation，但它们分别把 block-local conflict-graph reordering/early abort 与 OCC、snapshot consistency、serializability dependency graph、transaction reordering 迁移到 Fabric-style EOV ordering service。Nezha 同样是 blockchain adaptation evidence：它把 conflict graph / concurrency control 迁移到 DAG-based blockchain epoch-level execution，用 address-based conflict graph 替代交易对依赖图。C5 则补入一条非区块链的数据库复制 evidence：在异步 primary-backup replication 中，备库 cloned concurrency control 必须同时满足 monotonic prefix consistency 和 bounded replication lag。Atomic Commitment Across Blockchains 同样不是经典 foundation；它把 atomic commit 迁移到 open blockchain 跨链交易，说明 trusted coordinator、shared recovery log 和 crash-only assumptions 都需要重写。Cross-chain Deals 进一步说明，在自治且可恶意参与者的商业交互里，transaction atomicity/isolation/liveness 只能作为结构启发，正确性本身必须换成 acceptable payoff safety 与 escrow liveness。

## 解决的问题

本节点解决的是“分布式系统中多个参与方或多个副本如何在故障、并发和跨分区状态下达成一致的事务结果或可见状态”。在当前 vault 里，它服务于六类路径: Calvin 直接说明分区数据库如何通过确定性输入序列、确定性锁管理和输入日志减少分布式事务的提交时协调成本；Starry 说明 multi-master cloud database 如何把 replica consensus、OCC conflict detection 和 conflict reordering 放进 storage-layer commit；ByShard/AHL 把 2PC/2PL 类数据库协议翻译到 Byzantine sharded ledgers；Blockchain Meets Database、Fabric++、A Transactional Perspective 和 Nezha 把 SSI/MVCC/OCC/serializability/reordering/early-abort 思想翻译到 blockchain execution；C5 把 backup-side cloned concurrency control 放在 replicated database 中，强调一致性和复制滞后边界；Atomic Commitment 和 Cross-chain Deals 把 atomic commit、escrow、validation 和 commit/abort decision 翻译到多条独立区块链之间，同时必须重写 all-or-nothing correctness。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[distributed-systems|Distributed systems]] | child_of | ByShard secondary path and bridge endpoint | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[distributed-transactions|Distributed transactions]] | problem | 跨参与方 atomic commit / isolation 是当前 bridge 的实际端点 | ByShard source note | active_seed |
| [[04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control|Replicated database concurrency control]] | problem | primary-backup replicated databases 的备库并发控制和 read visibility 不是 distributed transaction atomic commit，应拆成独立检索入口 | C5 | active_seed |
| concurrency control | candidate | 2PL、deterministic locking 与 isolation 需要更完整 foundation | ByShard mentions 2PL; direct sources missing | review |
| atomic commit | candidate | 2PC 是 ByShard 的核心迁移对象 | ByShard mentions 2PC; direct sources missing | review |
| deterministic transaction scheduling | method candidate | Calvin 提供直接证据，但单篇 source 仍不足以拆成独立完整节点；先作为 transaction-processing / distributed-transactions 的方法路线保留 | Calvin | source_extension |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| two-phase commit | 协调 vote 和 global commit/abort 决策 | 多参与方需要 atomicity | blocking/failure-handling foundation 仍缺直接 source | [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] as adaptation evidence |
| two-phase locking | 用锁顺序约束并发交易的隔离性 | 需要 serializable 或更强 isolation | 高 contention 下可能增加等待或 abort | [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] as adaptation evidence |
| orchestrate-execute adaptation | 把 transaction protocol steps 包进 shard-level consensus/cluster-sending | Byzantine sharded resilient systems | 不是传统数据库协议本身，需要 BFT shard assumptions | [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] |
| BFT reference committee adaptation | 把 2PC coordinator state machine 放进 BFT replicated committee，并让 tx-committees 等待 quorum messages | permissioned sharded blockchain general workloads | reference committee bottleneck、partial synchrony 和 chaincode refactoring 边界仍在 | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL]] |
| Serializable Snapshot Isolation / MVCC adaptation | 用多版本行、rw-conflict tracking 和 abort during commit 提供 serializable execution，再用 block order/block height 改造成区块链可确定提交 | permissioned blockchain execution with rich SQL smart contracts | 普通 SSI 不处理互不信任副本与不同 current-block；需要 block-height SSI 和 block-aware abort rules | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] |
| Transaction reordering / early-abort adaptation | 用 read/write set 构建 conflict graph，重排可保留交易并提前 abort 已经 doomed 的交易 | Fabric-style execute-order-validate blockchains with visible readsets/writesets | 只在 block/orderer pipeline 中迁移方法；不提供通用数据库事务理论，也不解决 consensus safety | [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] |
| OCC / serializability dependency analysis adaptation | 用 snapshot timestamp、read/write dependency graph、cycle detection 和 reorderability theorem 判断哪些 pending transactions 可重排，哪些应提前 abort | execute-order-validate blockchains with readset/writeset and deterministic orderer-side processing | 已提交 blocks 不可重排；Bloom filter false positives 和 stale snapshot pruning 会带来额外 abort；交易细节披露会影响 liveness/security | [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]] |
| Address-level conflict graph adaptation | 用 address read/write sets 和 address dependency 替代 transaction-pair dependency graph，并用 hierarchical sorting 输出 deterministic commit order | DAG-based account-model blockchains with epoch-level concurrent blocks | 这是区块链执行层 adaptation；不提供通用 concurrency-control foundation，也不解决 DAG consensus safety | [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] |
| Row-granularity cloned concurrency control | 在备库按 row 维护 primary-log-ordered FIFO，让 backup 并行应用 safe writes，同时通过 snapshotter 只向 reads 暴露事务前缀 | asynchronous primary-backup database replication with read-only backups | 依赖 row-level log、snapshot/timestamp API 和 prompt log delivery；不是 distributed atomic commit | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] |
| Deterministic transaction scheduling / input replication | 先对事务输入达成全局顺序并复制输入日志，再按该顺序确定性申请锁和执行，从而把提交时协调移出锁持有窗口 | 分区数据库事务能提前声明读写集；副本必须按同一输入序列确定性执行 | dependent transactions 需要 OLLP；范围锁/phantom、磁盘预取预测、故障恢复 hiccup 仍是边界 | [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin]] |
| Semi-leader transaction commit | 无冲突事务由任意 proposer 收集 super quorum 后 fast commit；冲突事务交给 sequencer 用 conflict graph reorder/abort/re-commit。 | multi-master cloud databases with `2F+1` crash-fault replicas and visible read/write sets | sequencer conflict path 仍可能成为高竞争瓶颈；模型不是 Byzantine；reordering 是启发式 | [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry]] |
| Witness-network atomic commit adaptation | 用 witness-chain smart contract 的互斥 redeem/refund authorization state 表示全局 commit/abort decision，让多条 asset chains 接受同一 evidence。 | open blockchain cross-chain asset movement needs all-or-nothing semantics without trusted exchange/coordinator | 这是跨链协议 adaptation；需要 witness-chain finality/fork-depth、evidence validation、attack economics 和额外合约成本 | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment]] |
| Adversarial-commerce transaction-semantics adaptation | 将 classical atomic transaction 的 atomicity、isolation、recovery 和 liveness 词汇重写为 compliant/deviating parties、acceptable payoff、escrow anti-double-spending、weak liveness 与 strong liveness。 | autonomous parties across independent ledgers need complex deals beyond atomic swaps | 这是语义迁移边界而非数据库事务 foundation；不能保留 global all-or-nothing 或 crash-only assumptions。 | [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | paper | 将 2PC/2PL 类 transaction-processing 方法迁移到 Byzantine sharded systems | 这是 adaptation evidence，不是数据库事务 foundation survey | source note sections on OEM, orchestration, execution |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | 将 2PC/2PL 类 transaction-processing 方法迁移到 permissioned sharded blockchain，并用 BFT reference committee 替代脆弱 coordinator | adaptation evidence; TEE/reference committee assumptions | §6.1-§6.4 |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database: Design and Implementation of a Blockchain Relational Database]] | paper | 将 SSI/MVCC、stored procedures、ACL、transaction logs 和 provenance queries 迁移到 permissioned blockchain execution | adaptation evidence; not a general database transaction survey | §2-§4 |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Blurring the Lines between Blockchains and Database Systems: the Case of Hyperledger Fabric]] | paper | 将 transaction reordering、conflict graph 和 early abort 迁移到 Fabric simulate-order-validate pipeline | adaptation evidence; not a general database transaction survey | §2-§4 |
| [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on Execute-Order-Validate Blockchains]] | paper | 将 OCC、snapshot consistency、serializability/reorderability dependency analysis 迁移到 Fabric/FastFabric EOV ordering service | adaptation evidence; not a general database transaction survey | §3-§5 |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha: Exploiting Concurrency for Transaction Processing in DAG-based Blockchains]] | paper | 将 conflict graph/concurrency control 迁移到 DAG-based blockchain execution，用 address dependency 降低高并发块下的冲突检测和排序开销 | adaptation evidence; not a general database transaction survey | §III-§VI |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5: Cloned Concurrency Control That Always Keeps Up]] | paper | 将 transaction-processing 重新连接到 replicated database backup-side concurrency control，建立 monotonic prefix consistency + bounded replication lag 问题 | direct database replication evidence; not a distributed transaction atomic-commit source | §2-§7 |
| [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin: Fast Distributed Transactions for Partitioned Database Systems]] | paper | 提供直接分布式数据库证据：确定性输入序列、deterministic locking、transaction input replication、prefetch 和 checkpoint/replay 组合成高吞吐分布式事务路线 | 需要提前声明读写集；dependent transactions 依赖 OLLP；不是完整并发控制理论综述 | §1-§9 |
| [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry: Multi-master Transaction Processing on Semi-leader Architecture]] | paper | 提供直接 cloud database 证据：semi-leader commit 将 fast path 和 sequencer conflict path 分离，在 multi-master storage layer 同时处理 ACID、replica consensus 和 serializability | crash-fault model only；sequencer conflict path 高竞争下会带来 tail latency；不是完整 transaction theory foundation | §2-§5 |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | paper | 将 atomic commit/2PC framing 迁移到 cross-chain asset movement，用 witness-network authorization 替代 trusted coordinator | adaptation evidence; not a general database transaction survey | §3-§6 |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | paper | 将 transaction correctness vocabulary 迁移到 adversarial commerce，明确 compliant-party safety 替代 global all-or-nothing | adaptation evidence; not a general database transaction survey | §1-§8 |

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`。
- Freshness: `fresh` for repair structure; not a latest-current claim.
- 综合: 当前 vault 需要 `transaction-processing` 作为 distributed-systems 下的 L2 方向，主要为了给跨路径 bridge 提供真实端点；Calvin 和 Starry 让它拥有两条直接分布式数据库系统 evidence，但它仍不能替代经典 transaction-processing foundation。Calvin 补充 deterministic transaction scheduling / input replication 路线；Starry 补充 semi-leader storage-layer commit 路线，说明 multi-master database 可把无冲突 fast path 与冲突 sequencer reordering 分开。AHL 补充了 reference-committee route，Blockchain Meets Database 补充了 SSI/MVCC/stored procedure route，Fabric++ 补充了 transaction reordering/early abort route，A Transactional Perspective on EOV Blockchains 补充了 OCC/serializability dependency-analysis route，Nezha 补充了 address-level conflict graph / hierarchical sorting 到 DAG blockchain execution 的迁移路线，C5 补充了 primary-backup replicated database 中 backup-side cloned concurrency control 路线，Atomic Commitment Across Blockchains 补充了 atomic commit to independent-ledger route，Cross-chain Deals 补充了 adversarial-commerce correctness rewrite route。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] | 暴露 distributed transaction protocols 与 Byzantine sharded ledgers 的 bridge 端点 | 下级结构 / 方法族 / Bridge Links | yes, creates thin endpoint | 补直接 2PC/2PL/database transaction source |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] | 增加 reference committee 作为 2PC coordinator 的 Byzantine adaptation route | 方法族 / 代表 Sources / Bridge Links | no | 补直接 2PC/2PL/database transaction source |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] | 增加 SSI/MVCC/stored procedures 到 blockchain execution 的迁移路线，并建立新的 bridge。 | 方法族 / 代表 Sources / Bridge Links | yes | 补直接 SSI/OCC/serializability foundation source |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] | 增加 transaction reordering、conflict graph 和 early abort 到 Fabric EOV execution pipeline 的迁移路线。 | 方法族 / 代表 Sources / Bridge Links | no, strengthens bridge | 补直接 transaction reordering/OCC/serializability foundation source |
| [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]] | 增加 OCC/serializability/reorderability 到 Fabric-style EOV transaction processing 的迁移路线。 | 方法族 / 代表 Sources / Bridge Links | no, strengthens bridge | 补直接 OCC/serializability foundation source |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] | 增加 conflict graph/concurrency control 到 DAG-based blockchain execution 的迁移路线。 | 方法族 / 代表 Sources / Bridge Links | no, strengthens bridge | 补直接 concurrency-control/serializability foundation source |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] | 增加 replicated database backup-side concurrency control 路线，并拆出 `replicated-database-concurrency-control` 子节点。 | 下级结构 / 方法族 / 代表 Sources / Bridge Links | yes | 补 KuaFu、Query Fresh、parallel replication、database recovery/replication foundation source |
| [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin]] | 增加直接分布式数据库事务路线：先复制/排序事务输入，再用确定性锁管理执行，减少 2PC 在高竞争下的锁持有成本。 | 背景 / 方法族 / 代表 Sources / Bridge Links / 关系图谱 | no, strengthens endpoint and bridge | 补 deterministic database systems 对照源；补 2PC/2PL/serializability foundation source |
| [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry]] | 增加直接 cloud database multi-master transaction route：用 semi-leader commit 分离 non-conflict fast path 和 sequencer conflict graph reordering。 | 背景 / 解决的问题 / 方法族 / 代表 Sources / 关系图谱 | no, strengthens distributed-transactions and replicated-CC endpoints | 补 TAPIR、MDCC、Janus、Rococo、Paxos Commit 等对照源 |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | 增加 atomic commit/commit-abort decision 到 atomic cross-chain transactions 的迁移路线，并建立新的 bridge。 | 方法族 / 代表 Sources / Bridge Links | yes | 补直接 atomic commit/2PC foundation source；下一篇 Cross-chain Deals 后复核 bridge |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | 增加 adversarial-commerce route，说明 transaction correctness vocabulary 可迁移但必须重写为 acceptable payoff safety 与 escrow liveness。 | 方法族 / 代表 Sources / Bridge Links | no, strengthens bridge | 补直接 atomic commit/2PC foundation source；继续吸收 universal atomic swaps |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[database-transactions-to-byzantine-sharded-ledgers|Database transaction protocols -> Byzantine sharded ledgers]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/scaling-and-sharding/sharded-ledgers` | translation, implementation_reuse, dependency | 2PC/2PL structure transfers; Byzantine voting, shard consensus, cluster-sending or reference committees, faulty clients, validator assignment, trusted hardware, permissionless incentives, and data availability remain sharded-ledger-specific concerns. | active_seed |
| [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] | `distributed-systems/transaction-processing; blockchain-systems/execution-and-transactions/transaction-processing` | translation, implementation_reuse, dependency, trust_model_shift | SSI/MVCC/stored procedures/provenance transfer as execution mechanisms; consensus safety, Byzantine ordering and open-network assumptions do not transfer. | active_seed |
| [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | translation, trust_model_shift, coordination, dependency | Atomic commit structure transfers; trusted coordinator, shared recovery log, crash-only failures and blocking assumptions do not transfer unchanged to adversarial independent ledgers. | active_seed |
| [[05_Bridges/replicated-database-concurrency-control-to-storage-engines|Replicated database concurrency control -> storage engines]] | `distributed-systems/transaction-processing/replicated-database-concurrency-control; distributed-systems/data-management-and-storage/storage-engines` | dependency, implementation_boundary, interface_constraint | Backup-side cloned CC depends on row log, snapshot, timestamp and commit APIs; storage-engine interfaces do not themselves guarantee MPC or bounded lag. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-transaction-processing | is_a | nahida-knowledge-distributed-systems | vault/04_Knowledge/distributed-systems/transaction-processing.md; vault/04_Knowledge/distributed-systems.md | medium | active_seed |
| nahida-knowledge-transaction-processing | has_child | nahida-knowledge-distributed-transactions | vault/04_Knowledge/distributed-systems/transaction-processing.md; vault/04_Knowledge/distributed-systems/transaction-processing/distributed-transactions.md | medium | active_seed |
| nahida-knowledge-transaction-processing | has_child | nahida-knowledge-replicated-database-concurrency-control | vault/04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control.md; C5 source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | medium | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | high | active_seed |
| nahida-knowledge-transaction-processing | bridges_to | nahida-bridge-database-transactions-to-byzantine-sharded-ledgers | vault/05_Bridges/database-transactions-to-byzantine-sharded-ledgers.md | medium | active_seed |
| nahida-knowledge-transaction-processing | bridges_to | nahida-bridge-database-transaction-processing-to-blockchain-execution | vault/05_Bridges/database-transaction-processing-to-blockchain-execution.md | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md | Blockchain Meets Database source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md | Fabric++ source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md | A Transactional Perspective on EOV Blockchains source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md | Nezha source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md | C5 source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md | Calvin source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md | Starry source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md | Atomic Commitment source note | high | active_seed |
| nahida-knowledge-transaction-processing | evidenced_by | vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md | Cross-chain Deals source note | high | active_seed |
| nahida-knowledge-transaction-processing | bridges_to | nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions | vault/05_Bridges/distributed-transactions-to-atomic-cross-chain-transactions.md | high | active_seed |
| nahida-knowledge-transaction-processing | bridges_to | nahida-bridge-replicated-database-concurrency-control-to-storage-engines | vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 缺少经典 2PC/2PL/atomic commit/SSI/OCC/serializability/concurrency control/transaction reordering 直接 foundation source。 | Calvin 已补一个直接 distributed database system source，但当前节点还不能升级为完整 transaction-processing foundation。 | `nahida-research-search` foundation_pack 或继续 paper intake | high | queued |
| primary-backup database replication / recovery / parallel replication foundation source 缺失 | C5 给出强 source seed，但 KuaFu、Query Fresh、MySQL parallel replication 和 recovery lineages 仍只作为 C5 中的对照出现。 | `nahida-research-search` foundation_pack 或继续 paper intake | medium | queued |
| multi-master/leaderless database commit 对照源缺失 | Starry 引入 semi-leader route，但需要 TAPIR、MDCC、Janus、Rococo、Paxos Commit 等 sources 才能比较 commit/consensus/reordering 谱系。 | `nahida-research-search` foundation_pack 或继续 paper intake | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-repair-pass | Created missing L2 endpoint for database-transactions bridge. | ByShard source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-ahl-sharding | Added AHL reference-committee route as additional blockchain adaptation evidence for 2PC/2PL. | arxiv:1804.00399v4 | codex |
| 2026-06-22 | nahida-knowledge-20260622-blockchain-meets-database | Added SSI/MVCC/stored procedure migration route and bridge to blockchain transaction processing. | arxiv:1903.01919v2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-transactional-perspective-eov | Added OCC/serializability dependency-analysis route for EOV blockchain execution. | arxiv:2003.10064v1 | codex |
| 2026-06-22 | nahida-knowledge-20260622-fabric-plus-plus-transaction-processing | Added Fabric++ transaction reordering and early-abort adaptation evidence for Fabric EOV blockchain execution. | doi:10.1145/3299869.3319883 | codex |
| 2026-06-22 | nahida-knowledge-20260622-nezha-dag-transaction-processing | Added Nezha address-based conflict graph as DAG blockchain execution adaptation evidence. | doi:10.1109/icdcs54860.2022.00034 | codex |
| 2026-06-23 | nahida-knowledge-20260623-c5-cloned-concurrency-control | Added replicated database concurrency-control child node and C5 as primary-backup cloned CC evidence. | arxiv:2207.02746 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-calvin | Added Calvin as direct distributed database evidence for deterministic transaction scheduling, input replication and distributed transaction contention-footprint reduction. | sha256:e1d0bc04b53e5702d2f0d52b5bb1e561ff25fdf3490402c98abdb94c81281818 | codex |
| 2026-06-23 | nahida-knowledge-20260623-starry-multi-master-transaction-processing | Added Starry as direct cloud database evidence for semi-leader multi-master transaction commit and conflict-path reordering. | doi:10.14778/3561261.3561268 | codex |
| 2026-06-22 | nahida-knowledge-20260622-atomic-cross-chain-transactions | Added atomic commit adaptation evidence and bridge to atomic cross-chain transactions. | arxiv:1905.02847v2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-cross-chain-deals | Added adversarial-commerce correctness rewrite as adaptation evidence for cross-chain transaction semantics. | doi:10.14778/3364324.3364326 | codex |
