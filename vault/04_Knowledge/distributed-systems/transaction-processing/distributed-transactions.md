---
id: "nahida-knowledge-distributed-transactions"
title: "Distributed transactions"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "distributed-transactions"
domain_id: "distributed-systems"
direction_id: "transaction-processing"
parent_knowledge_refs:
  - "nahida-knowledge-transaction-processing"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "transaction-processing"
  - "distributed-transactions"
primary_ontology_path: "distributed-systems/transaction-processing/distributed-transactions"
secondary_ontology_paths:
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers"
relation_edges:
  - from: "nahida-knowledge-distributed-transactions"
    relation: "is_a"
    to: "nahida-knowledge-transaction-processing"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/transaction-processing/distributed-transactions.md"
      - "vault/04_Knowledge/distributed-systems/transaction-processing.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "bridges_to"
    to: "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
    evidence_refs:
      - "vault/05_Bridges/database-transactions-to-byzantine-sharded-ledgers.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-atomic-cross-chain-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-transactions"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
  - "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
  - "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
  - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
  - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
  - "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
  - "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
representative_source_refs:
  - "doi:10.14778/3476249.3476275"
  - "arxiv:1804.00399v4"
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
  - "sha256:e1d0bc04b53e5702d2f0d52b5bb1e561ff25fdf3490402c98abdb94c81281818"
  - "doi:10.14778/3561261.3561268"
query_keys:
  - "distributed transactions"
  - "two-phase commit"
  - "two-phase locking"
  - "cross-shard transactions"
  - "reference committee"
  - "atomic commit across blockchains"
  - "atomic cross-chain transactions"
  - "witness network atomic commitment"
  - "cross-chain deals"
  - "adversarial commerce"
  - "cross-chain smart contract invocation"
  - "ShuttleCross"
  - "hybrid concurrency control"
  - "Calvin"
  - "deterministic distributed transactions"
  - "deterministic locking"
  - "transaction input replication"
  - "contention footprint"
  - "distributed transactions without 2PC"
  - "OLLP"
  - "Starry"
  - "semi-leader commit"
  - "multi-master transaction processing"
  - "storage-layer transaction commit"
  - "conflict graph reordering"
aliases:
  - "2PC"
  - "2PL"
  - "cross-shard transactions"
  - "atomic commit"
  - "adversarial commerce"
  - "cross-chain smart contract invocation"
  - "deterministic distributed transactions"
  - "deterministic transaction scheduling"
domains:
  - "distributed-systems"
topics:
  - "distributed-transactions"
  - "two-phase-commit"
  - "two-phase-locking"
  - "atomic-commit"
  - "atomic-cross-chain-transactions"
  - "cross-chain-smart-contract-invocation"
  - "hybrid-concurrency-control"
  - "deterministic-transaction-scheduling"
  - "transaction-input-replication"
  - "multi-master-transaction-processing"
  - "semi-leader-commit-protocol"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
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
  - "nahida-knowledge-20260622-atomic-cross-chain-transactions"
  - "nahida-knowledge-20260622-cross-chain-deals"
  - "nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation"
  - "nahida-paper-intake-20260623-calvin"
  - "nahida-knowledge-20260623-starry-multi-master-transaction-processing"
source_refs:
  - "doi:10.14778/3476249.3476275"
  - "arxiv:1804.00399v4"
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
  - "sha256:e1d0bc04b53e5702d2f0d52b5bb1e561ff25fdf3490402c98abdb94c81281818"
  - "doi:10.14778/3561261.3561268"
confidence: "medium"
trust_tier: "primary"
---

# Distributed transactions

## 定义与范围

- 定义: Distributed transactions 处理一个 logical transaction 跨多个参与方、分区或 shard 时如何保持 atomicity、isolation 和一致的 commit/abort 结果。
- 当前 vault 覆盖: Calvin 直接说明分区数据库如何用确定性输入排序、确定性锁管理和事务输入复制降低多分区 ACID 事务的 2PC 竞争成本；Starry 说明 multi-master cloud database 如何用 semi-leader commit 在 storage layer 同时处理 ACID、replica consensus、serializability 和跨 shard distributed transactions；ByShard 将 two-phase commit 和 two-phase locking 改写进 Byzantine sharded resilient systems；AHL 将 2PC coordinator state machine 放进 BFT reference committee，以避免 malicious coordinator indefinite blocking；Atomic Commitment Across Blockchains 将 atomic commit / commit-abort decision 改写进多条独立区块链之间的 witness-network coordination；Cross-chain Deals 进一步说明 adversarial commerce 中不能直接继承经典 all-or-nothing correctness，而要改写成 compliant-party acceptable payoff 与 escrow liveness；ShuttleCross 将 2PC/OCC/S2PL/wait-for graph/serializability 改写进 [[cross-chain-smart-contract-invocation|cross-chain smart contract invocation]]。
- 不包含: 传统数据库事务理论的完整 foundation、所有 concurrency-control 方法、或 ByShard 论文的每个 protocol variant；这些需要后续 source。
- Retrieval role: 作为 `database-transactions-to-byzantine-sharded-ledgers` bridge 的真实 endpoint，让 query 可以从 distributed transaction problem 进入 sharded-ledger adaptation。
- Update scope: 任何 2PC、2PL、atomic commit、distributed database、cross-shard transaction、isolation source 都应刷新本节点。

## 背景

source_backed_background: 分布式事务通常要在多节点、多分区或多服务之间协调写入结果；atomic commit 关注是否所有参与方一致提交或中止，concurrency control 关注并发事务之间的隔离。Calvin 提供一条直接数据库系统路线：先在事务边界外对输入顺序达成一致并复制输入日志，再按确定性顺序获取锁和执行，避免传统 2PC 在锁持有期间扩大竞争足迹。Starry 提供另一条直接数据库系统路线：在 storage layer 让无冲突事务由任意 proposer 通过 super quorum fast commit，把冲突事务交给 sequencer 做 conflict graph reordering，并将该机制扩展到跨 shard distributed transactions。当前 vault 的其他证据仍主要来自 blockchain adaptation：ByShard/AHL 展示 2PC/2PL 如何进入 Byzantine sharded ledgers，Atomic Commitment Across Blockchains 展示 atomic commit 如何进入 adversarial independent ledgers，Cross-chain Deals 展示经典事务正确性在自治且互不信任参与者下必须重写。因此本节点已从纯 `foundation_thin` 提升为 `active_seed`，但仍不是完整分布式事务理论综述。

## 解决的问题

本节点解决的问题是: 当一个 transaction 涉及多个参与方时，系统如何避免一部分提交、一部分中止，且如何控制并发导致的不可接受 interleaving。在 Calvin 语境下，这个问题变成: 如何把全局顺序、复制和故障恢复前移到执行前，使多分区事务在持锁期间不再运行传统分布式提交协议。在 Starry 语境下，这个问题变成: 如何让 multi-master storage replicas 同时提供就近提交、replica agreement、conflict resolution 和跨 shard commit，而不是在 leader bottleneck 与 leaderless conflict abort 之间二选一。在 ByShard 语境下，这个问题进一步变成: 如何把 2PC/2PL 的结构放进 Byzantine shard consensus 和 cluster-sending 之上。在 AHL 语境下，它变成: 如何让一个 BFT reference committee 代表 2PC coordinator，以免 client/coordinator 恶意导致跨片事务无限阻塞。在 Atomic Commitment Across Blockchains 语境下，它变成: 如何把 global commit/refund decision 变成所有独立 asset chains 都能验证的 witness evidence。在 Cross-chain Deals 语境下，它又变成: 如何保留 escrow/commit/validation 结构，同时放弃不可实现的全局 all-or-nothing，改用每个 compliant party 的 acceptable payoff 安全性。在 ShuttleCross 语境下，它进一步变成: origin chain 如何协调 target-chain smart contract invocations，并用 HCC 在 OCC/S2PL 之间动态切换以保证 serializability 和降低 abort/latency。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[transaction-processing|Transaction processing]] | child_of | ByShard secondary ontology path | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| two-phase commit | method candidate | ByShard 的 linear/centralized/distributed orchestration 都围绕 vote/commit/abort 决策 | ByShard §4 in source note | review |
| two-phase locking | method candidate | ByShard 的 lock-based execution 用它表达 isolation | ByShard §5 in source note | review |
| cross-shard transactions | application/problem candidate | blockchain sharding 中 distributed transactions 的主要应用形态 | ByShard source note | review |
| atomic commit across independent ledgers | method/problem candidate | Atomic Commitment 把 commit/abort 结构迁移到互不信任链之间，但经典 foundation source 仍缺 | Atomic Commitment source note | review |
| adversarial-commerce deals | application/problem candidate | Cross-chain Deals 把 distributed transaction vocabulary 转成自治参与者资产交换；当前作为 bridge/source extension，不单独拆分。 | Cross-chain Deals source note | source_extension |
| cross-chain smart contract invocation | application/problem candidate | ShuttleCross 把 distributed transaction vocabulary 转成多链合约调用执行；primary node 已放在 cross-chain protocols 下。 | ShuttleCross source note | source_extension |
| deterministic distributed transactions | method candidate | Calvin 是直接证据，但仍需要 H-Store、Hyder、deterministic database systems 等对照源后再拆独立节点。 | Calvin source note | source_extension |
| semi-leader transaction commit | method candidate | Starry 是直接证据，但仍需要 TAPIR/MDCC/Janus/Rococo/Paxos Commit 等对照源后再判断是否拆独立节点。 | Starry source note | source_extension |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| two-phase commit | 先收集 vote，再决定 commit/abort | 需要 atomic commit | 传统模型不自动容忍 Byzantine equivocation | [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] |
| two-phase locking | acquire/release locks 约束冲突事务顺序 | 需要 isolation / serializability 类语义 | 高 contention 影响 latency/abort | [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] |
| Byzantine adaptation | 将 vote/commit/abort 包装为 shard consensus steps 并通过 cluster-sending 跨 shard 传播 | sharded resilient systems | 需要每个 shard 内部 BFT consensus 和通信假设 | [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] |
| BFT reference committee coordinator | 把 2PC coordinator state machine 复制到一个 BFT committee，tx-committees 等待来自 `R` 的 quorum messages | permissioned sharded blockchain general workload | reference committee 可能成为瓶颈；liveness 依赖 partial synchrony 和 committee safety | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL]] |
| Witness-network atomic commit adaptation | 把 global commit/abort decision 外化为 witness-chain smart contract 的互斥 redeem/refund authorization state，asset chains 通过跨链 evidence 执行统一 redeem/refund。 | independent blockchains need all-or-nothing asset movement without trusted exchange/coordinator | 需要 witness-chain finality/fork-depth、51% attack economics、跨链 evidence validation 和额外合约成本 | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment]] |
| Cross-chain deal correctness adaptation | 将 transaction 的 atomicity/isolation/recovery vocabulary 改写为 payoff acceptability、escrow anti-double-spending、weak/strong liveness 和 deal-specific validation。 | autonomous mutually distrusting parties coordinate complex asset exchange | 不保留经典 global all-or-nothing；timelock route 依赖同步，CBC route 引入共享 ledger。 | [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals]] |
| Cross-chain smart contract invocation adaptation | 将 2PC、S2PL、OCC、wait-for graph 和 serializability conflict graph 改写为 origin-chain coordination、target-chain cached dirty states、`opList`/`lockList` 和 read-only invocation visibility rules。 | 多链 smart-contract workflow 需要 atomic multi-invocation execution。 | BFT-chain finality、inter-chain message delay/loss、target-chain tx pool/consensus latency 和 off-chain read official-version matching 是新增边界。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] |
| Deterministic input-order route | 在事务执行前复制并固定全局输入序列，随后按该序列确定性申请锁和执行，使 failure/replay 可由输入日志和副本承担，避免事务末尾 2PC 进入锁持有窗口。 | 分区数据库、事务可提前声明读写集、系统能约束非确定性执行。 | dependent transactions 需要 OLLP；范围锁/phantom、磁盘预取预测和无停顿恢复仍是边界。 | [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin]] |
| Semi-leader multi-master commit route | 无冲突事务在 storage replicas 中 decentralized pre-commit/commit；冲突事务由 sequencer 合并依赖、运行 conflict graph reordering，并对事务做 abort/re-commit/commit。 | multi-master cloud database；每 shard `2F+1` crash-fault replicas；read/write sets 在提交阶段可见。 | 不是 Byzantine；sequencer conflict path 高竞争下 tail latency 增大；跨 shard 仍需要 coordinator 聚合 participant decisions。 | [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | paper | 把 2PC/2PL 作为可迁移结构，组合出 Byzantine sharded transaction protocols | adaptation evidence only; direct DB foundation missing | source note: OEM, orchestration, lock-based execution, experiments |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | 用 BFT reference committee 承接 2PC coordinator logic，并用 2PL/chaincode locks 支持 general cross-shard transactions | adaptation evidence only; TEE/reference committee assumptions; direct DB foundation missing | §6.1-§6.4 |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | paper | 将 atomic commit/2PC framing 迁移到跨多条独立区块链的 AC2T/AC3：用 witness-network authorization 统一所有 asset contracts 的 redeem/refund | adaptation evidence only; open blockchain finality/evidence assumptions; direct classical atomic-commit foundation missing | §3-§6 |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | paper | 将 atomic transaction 的 atomicity/isolation/liveness 语义改写到 adversarial commerce，明确 all-or-nothing 不应直接迁移 | adaptation evidence only; direct classical transaction foundation missing | §1-§8 |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross: An Efficient Cross-Chain Smart Contract Invocation Framework]] | paper | 将 2PC/OCC/S2PL/serializability/deadlock detection vocabulary 迁移到 cross-chain smart contract invocation，并给出 HCC/read-write separation route | adaptation evidence only; direct classical transaction foundation missing | §III-§VI |
| [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin: Fast Distributed Transactions for Partitioned Database Systems]] | paper | 直接给出分区数据库中无传统事务尾部 2PC 的分布式 ACID 事务路线：input ordering、deterministic locking、input replication、prefetch、checkpoint/replay | direct database system evidence; not a complete transaction-theory foundation | §1-§9 |
| [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry: Multi-master Transaction Processing on Semi-leader Architecture]] | paper | 直接给出 multi-master cloud database 的 distributed transaction 路线：storage-layer semi-leader commit、conflict graph reordering、cross-shard extension 和 POS read-only optimization | direct database system evidence; crash-fault only; not a complete transaction-theory foundation | §2-§5 |

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`。
- Freshness: `fresh` for repair structure; not a latest-current claim.
- 综合: distributed transactions 是多个 blockchain bridge 的必要 foundation endpoint；Calvin 和 Starry 共同补入直接数据库系统证据。Calvin 说明一条关键路线是把全局输入顺序和复制协议前移，并用 deterministic locking 让并发执行等价于输入序列，从而缩短高竞争多分区事务的锁持有窗口。Starry 说明另一条路线是把 commit 分成 non-conflict decentralized fast path 与 conflict sequencer reordering path，从而在 multi-master storage layer 同时处理副本一致性和 serializability。它仍不能让本节点成为完整数据库事务综述。ByShard 展示 shard-step/cluster-sending route，AHL 展示 BFT reference committee coordinator route。Atomic Commitment Across Blockchains 增加第三条 route：把 atomic commit 的全局决定从 trusted coordinator 改写成 witness-network smart contract 的互斥状态，并让各 asset chains 通过 evidence 接受同一 redeem/refund decision。Cross-chain Deals 增加第四条 boundary evidence：当参与者自治、互不信任且可任意偏离协议时，distributed transaction 的 all-or-nothing、isolation 和 liveness 术语仍有启发，但必须被重写为 acceptable payoff、escrow anti-double-spending、weak liveness 和 strong liveness。ShuttleCross 增加第五条 route：跨链合约调用可以复用 2PC/OCC/S2PL/serializability，但需要把 coordinator、dirty state、lock manager、read visibility 和 liveness 全部改写到独立 BFT chains 的执行/共识边界内。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] | 将 distributed transaction protocols 翻译进 Byzantine sharded ledgers | 方法族 / Bridge Links / 关系图谱 | yes | 补 2PC/2PL foundation source |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] | 增加 BFT reference committee route：用 BFT-replicated coordinator state machine 处理 malicious coordinator liveness，并用 chaincode-level locks 实现 2PL。 | 方法族 / 代表 Sources / Bridge Links / 关系图谱 | no | 补经典 2PC/2PL foundation source；后续比较 Chainspace/CAPER/SharPer |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | 增加 atomic commit to independent-ledger route：用 permissionless witness network 作为共同 commit/refund authorization source。 | 方法族 / 代表 Sources / Bridge Links / 关系图谱 | yes, creates bridge | 下一篇 Cross-chain Deals 后复核 atomicity bridge 边界；补经典 atomic commit foundation source |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | 增加 adversarial-commerce boundary：atomic transaction vocabulary 可启发跨链 deal，但 global all-or-nothing 和 crash-only assumptions 不可直接迁移。 | 方法族 / 代表 Sources / Bridge Links / 关系图谱 | no new bridge | 补经典 atomic commit/transaction foundation source；继续吸收 universal atomic swaps |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | 增加 cross-chain smart contract invocation adaptation：2PC/OCC/S2PL/wait-for graph/serializability 可迁移，但要补 BFT-chain signatures、timeout polling、target-chain consensus 和 read visibility。 | 方法族 / 代表 Sources / Bridge Links / 关系图谱 | yes, creates bridge | 补 GPACT/2PC4BC/EOVPC/Avalon 和经典并发控制 foundation source |
| [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin]] | 增加 deterministic input-order route：把一致性排序/复制放到执行前，用确定性锁管理减少 2PC 竞争足迹。 | 背景 / 解决的问题 / 方法族 / 代表 Sources / 关系图谱 | no | 补 H-Store/Hyder/deterministic DB 对照源；补经典 2PC/2PL foundation source |
| [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry]] | 增加 semi-leader multi-master commit route：无冲突事务去中心化 fast commit，冲突事务交给 sequencer conflict graph reordering，并扩展到跨 shard distributed transactions。 | 背景 / 解决的问题 / 方法族 / 代表 Sources / 关系图谱 | no | 补 TAPIR、MDCC、Janus、Rococo、Paxos Commit 等对照源 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[database-transactions-to-byzantine-sharded-ledgers|Database transaction protocols -> Byzantine sharded ledgers]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/scaling-and-sharding/sharded-ledgers` | translation, implementation_reuse, dependency | 2PC/2PL structure transfers; Byzantine voting, shard consensus, cluster-sending or reference committees, faulty clients, validator assignment, trusted hardware, permissionless incentives, and data availability remain sharded-ledger-specific concerns. | active_seed |
| [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | translation, trust_model_shift, coordination, dependency | Atomic commit structure transfers; trusted coordinator, common recovery log, crash-only failures and blocking assumptions do not transfer unchanged to adversarial independent ledgers. | active_seed |
| [[distributed-transactions-to-cross-chain-smart-contract-invocation|Distributed transactions -> cross-chain smart contract invocation]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | translation, coordination, concurrency_control, trust_model_shift | 2PC/OCC/S2PL vocabulary transfers; independent BFT ledgers, origin-chain coordination, timeout polling and on-chain visibility change the correctness boundary. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-distributed-transactions | is_a | nahida-knowledge-transaction-processing | vault/04_Knowledge/distributed-systems/transaction-processing/distributed-transactions.md; vault/04_Knowledge/distributed-systems/transaction-processing.md | medium | active_seed |
| nahida-knowledge-distributed-transactions | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | medium | active_seed |
| nahida-knowledge-distributed-transactions | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | high | active_seed |
| nahida-knowledge-distributed-transactions | bridges_to | nahida-bridge-database-transactions-to-byzantine-sharded-ledgers | vault/05_Bridges/database-transactions-to-byzantine-sharded-ledgers.md | medium | active_seed |
| nahida-knowledge-distributed-transactions | evidenced_by | vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md | Atomic Commitment source note | high | active_seed |
| nahida-knowledge-distributed-transactions | evidenced_by | vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md | Cross-chain Deals source note | high | active_seed |
| nahida-knowledge-distributed-transactions | bridges_to | nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions | vault/05_Bridges/distributed-transactions-to-atomic-cross-chain-transactions.md | high | active_seed |
| nahida-knowledge-distributed-transactions | evidenced_by | vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md | ShuttleCross source note | high | active_seed |
| nahida-knowledge-distributed-transactions | bridges_to | nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation | vault/05_Bridges/distributed-transactions-to-cross-chain-smart-contract-invocation.md | high | active_seed |
| nahida-knowledge-distributed-transactions | evidenced_by | vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md | Calvin source note | high | active_seed |
| nahida-knowledge-distributed-transactions | evidenced_by | vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md | Starry source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 缺少 2PC/2PL/atomic commit/serializability/transaction-processing 系统 foundation source。 | Calvin 已补一个直接 database-system route，但不足以回答完整 distributed transactions 问题。 | `nahida-research-search` foundation_pack 或继续 paper intake | high | queued |
| ByShard/AHL 之外缺 cross-shard transaction 代表 source。 | 需要避免让少数 sharding papers 定义整个问题域。 | `nahida-update` serial intake | medium | queued |
| 缺 GPACT/2PC4BC/EOVPC/Avalon direct sources。 | ShuttleCross 建立了跨链合约调用迁移路线，但还需要对照 direct sources 判断 HCC/read-write separation 的差异。 | `nahida-update` serial intake or `nahida-research-search` | medium | queued |
| 缺 multi-master/leaderless distributed transaction 对照源。 | Starry 需要与 TAPIR、MDCC、Janus、Rococo、Paxos Commit 等路线比较，才能沉淀更稳定的 commit protocol 分类。 | `nahida-research-search` foundation_pack 或继续 paper intake | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-repair-pass | Created missing L3 endpoint for database-transactions bridge. | ByShard source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-ahl-sharding | Added AHL reference committee as second source extension for adapting 2PC/2PL to Byzantine sharded ledgers. | arxiv:1804.00399v4 | codex |
| 2026-06-22 | nahida-knowledge-20260622-atomic-cross-chain-transactions | Added witness-network atomic commit adaptation and bridge to atomic cross-chain transactions. | arxiv:1905.02847v2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-cross-chain-deals | Added adversarial-commerce deal correctness adaptation and strengthened the bridge boundary to atomic cross-chain transactions. | doi:10.14778/3364324.3364326 | codex |
| 2026-06-22 | nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation | Added cross-chain smart contract invocation adaptation and bridge to distributed transactions. | sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-calvin | Added Calvin as direct database evidence for deterministic distributed transactions and 2PC contention-footprint reduction. | sha256:e1d0bc04b53e5702d2f0d52b5bb1e561ff25fdf3490402c98abdb94c81281818 | codex |
| 2026-06-23 | nahida-knowledge-20260623-starry-multi-master-transaction-processing | Added Starry as direct database evidence for semi-leader multi-master commit, conflict graph reordering and cross-shard transaction extension. | doi:10.14778/3561261.3561268 | codex |
