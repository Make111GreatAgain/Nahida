---
id: "nahida-knowledge-cross-shard-transaction-execution"
title: "Cross-shard transaction execution"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "cross-shard-transaction-execution"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-execution-and-transactions"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "cross-shard-transaction-execution"
primary_ontology_path: "blockchain-systems/execution-and-transactions/cross-shard-transaction-execution"
secondary_ontology_paths:
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers"
  - "distributed-systems/transaction-processing/distributed-transactions"
relation_edges:
  - from: "nahida-knowledge-cross-shard-transaction-execution"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-execution-and-transactions"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/cross-shard-transaction-execution.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-shard-transaction-execution"
    relation: "is_adjacent_to"
    to: "nahida-knowledge-sharded-ledgers"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/scaling-and-sharding/sharded-ledgers.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/cross-shard-transaction-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-shard-transaction-execution"
    relation: "bridges_to"
    to: "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
    evidence_refs:
      - "vault/05_Bridges/database-transactions-to-byzantine-sharded-ledgers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-shard-transaction-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-cross-shard-transaction-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-cross-shard-transaction-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-cross-shard-transaction-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-shard-transaction-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
source_note_refs:
  - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
representative_source_refs:
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1804.00399v4"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
query_keys:
  - "cross-shard transaction execution"
  - "cross-shard smart contract execution"
  - "cross-shard commit protocol"
  - "blockchain sharding transaction processing"
  - "跨片交易执行"
  - "跨分片智能合约执行"
aliases:
  - "跨片交易执行"
  - "Cross-shard smart-contract execution"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "cross-shard-transaction-execution"
  - "cross-shard-transactions"
  - "smart-contract-sharding"
  - "sharded-ledgers"
  - "distributed-transactions"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-22"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts"
source_refs:
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1804.00399v4"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
confidence: "medium"
trust_tier: "primary"
---

# Cross-shard transaction execution

## 定义与范围

- 定义: Cross-shard transaction execution 关注一个区块链交易或智能合约调用需要访问多个 shard 的状态时，系统如何执行、排序、验证、提交或回滚这些跨片效果，并让所有正确 shard 对最终状态达成一致。
- 不包含: 分片验证者分配、随机组片、DA sampling、单个命名 sharding protocol 的完整设计；这些分别属于 [[sharded-ledgers|Sharded ledgers]]、[[data-availability-sampling|Data availability sampling]] 或 source note。
- Canonical terms: `cross-shard transaction execution`, `cross-shard smart-contract execution`, `cross-shard commit protocol`.
- Retrieval role: 查询“跨片交易怎么做”“LightCross/AHL/ByShard/RingBFT 的共同问题是什么”时先进入本节点，再打开具体 source。
- Update scope: 新 source 若涉及 cross-shard commit、cross-shard smart-contract execution、contract placement/migration、sharded transaction atomicity/isolation 或 shard-to-shard execution scheduling，应刷新本节点。

## 背景

Sharded ledger 的吞吐来自把交易和状态切到多个 shard，但这会制造一个执行层问题: 一笔交易可能同时读写多个 shard。简单资产转账可以被拆成输入/输出、lock/unlock 或 debit/credit 步骤；一般智能合约却可能在执行中调用多个合约、动态产生读写集，并且需要在多个 shard 上原子提交最终状态。

因此，cross-shard transaction execution 不是一个具体协议名，而是 sharding 与 execution-and-transactions 的交叉问题。当前 vault 的证据包括 OmniLedger、ByShard、RingBFT、AHL 和 LightCross。它们分别展示了 payment-oriented atomic commit、Byzantine multi-shard database-style transactions、ring-topology cross-shard consensus、reference-committee 2PC/2PL，以及 TEE-backed off-chain smart-contract execution。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 多个 source 都在解决同一类跨片原子性、隔离、执行位置和通信开销问题，而不是 LightCross 或 ByShard 的专名。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: LightCross、AHL、ByShard、RingBFT 和 OmniLedger 是不同方法族的 representative sources；系统细节留在 source note。
- 需要引用的更基础 Knowledge: [[execution-and-transactions|Blockchain execution and transactions]]、[[sharded-ledgers|Sharded ledgers]]、[[04_Knowledge/distributed-systems/transaction-processing/distributed-transactions|Distributed transactions]]。

## 解决的问题

本节点回答: 一个交易跨越多个 shard 时，如何在不让所有 shard 退化成单片链的情况下实现正确执行。

关键子问题:

- **Atomicity.** 部分 shard 不能提交、部分 shard abort。
- **Isolation/serializability.** 跨片读写与片内交易并发时，最终结果需要可序列化或满足系统声明的隔离级别。
- **Execution placement.** 智能合约逻辑应该在 involved shards、reference committee、off-chain executor 还是其他位置执行。
- **Communication complexity.** shard-to-shard 多轮通信、reference committee dispatch、ring order 或 batch validation 都会影响吞吐和延迟。
- **Workload locality.** 如果大量交易频繁跨片，分片收益会被跨片协议开销吞掉。
- **Fault model.** Byzantine shards、malicious clients、malicious coordinators、TEE executors 或 unavailable storage 都会改变协议边界。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[execution-and-transactions|Blockchain execution and transactions]] | child_of | multiple execution-layer sources now focus on cross-shard execution | active_seed |
| [[sharded-ledgers|Sharded ledgers]] | adjacent_problem | sharded ledgers require cross-shard transaction execution to support multi-shard workloads | active_seed |
| [[04_Knowledge/distributed-systems/transaction-processing/distributed-transactions|Distributed transactions]] | bridge/foundation | 2PC/2PL and serializability vocabulary transfer, but Byzantine and shard consensus do not | foundation_thin |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| payment-oriented-cross-shard-atomic-commit | method candidate | UTXO/payment transfer has simpler semantics than arbitrary smart contracts | OmniLedger / Atomix-style sources | review |
| byzantine-distributed-transaction-sharding | method candidate | ByShard/AHL translate database transaction protocols into Byzantine shards | [[database-transactions-to-byzantine-sharded-ledgers|Database transaction protocols -> Byzantine sharded ledgers]] | review |
| tee-assisted-cross-shard-execution | method candidate | LightCross moves arbitrary smart-contract execution to TEE executors | [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] | review |
| smart-contract-placement-and-migration | method candidate | LightCross shows contract migration can reduce the cross-shard ratio | LightCross plus future OptChain-like sources needed | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Payment-oriented atomic commit | 将资产转账拆成 input/output 或 debit/credit effects，用跨片 commit/abort 规则防止半提交。 | UTXO 或简单 payment ledger；交易逻辑可被拆成有限 shard effects。 | 不直接支持 arbitrary smart-contract call graph。 | [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger]] |
| Database-style 2PC/2PL in Byzantine shards | 将跨片事务拆成 prepare/commit/abort，并用锁保证隔离；Byzantine shard 内部用 consensus 包装 vote/commit steps。 | general workload sharded ledger；应用能暴露或重构事务步骤。 | 通信和锁开销高；coordinator/reference committee 可能成为瓶颈；需要处理 malicious coordinator/client。 | [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]]; [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] |
| Ring-order cross-shard consensus | 让涉及交易的 shards 按环形拓扑传播和确认跨片交易，减少全互连通信。 | shard set 可按拓扑组织，协议能接受 ring-based propagation。 | 延迟/吞吐随 involved shards 和环传播路径变化；仍需跨片协调。 | [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT]] |
| Reference committee coordination | 由 reference committee 排序、调度或推进跨片交易，避免单个 malicious coordinator indefinite blocking。 | permissioned/general workload；能承受 committee overhead。 | committee throughput 和 availability 成为系统边界；应用可能需要 chaincode refactoring。 | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] |
| TEE-backed off-chain execution plus batch validation | 将复杂智能合约 CSTx 放入 TEE executor 执行；executor 读取 Merkle/threshold-signed authenticated state；R-shard 批量排序结果，S-shards 用 bitmap 验证 stale reads 并提交 write sets。 | permissioned smart-contract sharding；TEE/attestation 可接受；R-shard 和 executors 可部署。 | 信任 TEE；R-shard 是特殊调度层；stale reads 可能 abort；executor availability 是 liveness 边界。 | [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] |
| Contract placement and migration | 根据历史交易调用图把经常共同调用的 contracts 放到同一 shard，降低 cross-shard ratio。 | workload locality 相对稳定；迁移窗口和状态迁移成本可控。 | workload shift 会降低收益；迁移需要暂停/降速窗口；不替代 commit protocol。 | [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding]] | paper | payment-ledger sharding and Atomix-style cross-shard atomic commit route | source note is older migration seed; details should be refreshed when needed | source note |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | paper | Byzantine multi-shard transactions with database protocol translation | consensus simulation/protocol-specific assumptions; not arbitrary off-chain execution | source note |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT: Resilient Consensus over Sharded Ring Topology]] | paper | ring-topology cross-shard consensus route | topology-dependent; not the same as LightCross's R-shard/executor split | source note |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | permissioned/general-workload sharding using TEE-assisted BFT and BFT reference committee for 2PC/2PL | TEE/reference committee assumptions; manual application refactoring | §6-§7 |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts]] | paper | arbitrary smart-contract CSTx route via TEE executor, R-shard scheduling, bitmap validation, and contract migration | TEE assumption; R-shard and executor availability; permissioned FISCO-BCOS setting | Abstract, §III-§V, Appendix |

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-22`。
- Freshness: `fresh` for current-vault evidence, not a latest-news claim。
- 综合: Cross-shard transaction execution 已经超过单篇论文范围，应该从 `transaction-processing` 的 candidate 提升为正式 problem node。AHL/ByShard 说明 database-style distributed transactions can transfer into Byzantine sharding only after adding shard consensus, BFT coordinator/reference committees and lock/abort handling。RingBFT 表明跨片通信拓扑本身可以成为优化对象。LightCross 则补上 arbitrary smart-contract execution 的新路线: 不把合约逻辑拆成 shard-local fragments，而是在 TEE executor 中一次执行，再由 R-shard 批量排序和各 S-shard 验证 stale reads 后提交。LightCross 同时说明跨片执行问题不能只靠 commit protocol 解决；contract placement/migration 也是减少问题规模的系统手段。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] | 将 `cross-shard-transaction-execution` 从 candidate 提升为 active problem node；新增 TEE-backed off-chain smart-contract execution、R-shard batch validation、contract migration 路线。 | 定义; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 OptChain/Chainspace/CAPER/SharPer 时复核 child split |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[database-transactions-to-byzantine-sharded-ledgers|Database transaction protocols -> Byzantine sharded ledgers]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/scaling-and-sharding/sharded-ledgers` | translation, implementation_reuse, dependency | 2PC/2PL structure transfers; Byzantine shard consensus, BFT reference committees, application refactoring, TEEs, and workload locality remain blockchain-sharding concerns. LightCross is a contrasting route that reduces direct 2PC/2PL exposure by offloading execution to TEEs. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-cross-shard-transaction-execution | is_a | nahida-knowledge-blockchain-execution-and-transactions | this note; execution-and-transactions note | high | active_seed |
| nahida-knowledge-cross-shard-transaction-execution | is_adjacent_to | nahida-knowledge-sharded-ledgers | sharded-ledgers note; LightCross source note | high | active_seed |
| nahida-knowledge-cross-shard-transaction-execution | bridges_to | nahida-bridge-database-transactions-to-byzantine-sharded-ledgers | bridge note | high | active_seed |
| nahida-knowledge-cross-shard-transaction-execution | evidenced_by | vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md | OmniLedger source note | medium | active_seed |
| nahida-knowledge-cross-shard-transaction-execution | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | ByShard source note | medium | active_seed |
| nahida-knowledge-cross-shard-transaction-execution | evidenced_by | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | RingBFT source note | medium | active_seed |
| nahida-knowledge-cross-shard-transaction-execution | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | AHL source note | high | active_seed |
| nahida-knowledge-cross-shard-transaction-execution | evidenced_by | vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md | LightCross source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 缺少 Chainspace/CAPER/SharPer/OptChain 等更多 cross-shard execution 与 contract placement sources。 | 当前方法族已成型，但还不足以细分多个 child method nodes。 | continue paper intake or `nahida-research-search` | high | queued |
| TEE-assisted execution 与 pure Byzantine execution 的安全边界需要更多 foundation。 | LightCross/AHL/SlimChain 都用 TEE，但作用不同，需要统一边界。 | continue paper intake or foundation search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts | Created active cross-shard transaction execution problem node and absorbed LightCross. | LightCross; existing AHL/ByShard/RingBFT/OmniLedger notes | codex |
