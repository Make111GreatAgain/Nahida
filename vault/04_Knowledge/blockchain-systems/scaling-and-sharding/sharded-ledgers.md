---
id: "nahida-knowledge-sharded-ledgers"
title: "Sharded ledgers"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "sharded-ledgers"
domain_id: "blockchain-systems"
direction_id: "scaling-and-sharding"
parent_knowledge_refs:
  - "nahida-knowledge-scaling-and-sharding"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "scaling-and-sharding"
  - "sharded-ledgers"
primary_ontology_path: "blockchain-systems/scaling-and-sharding/sharded-ledgers"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "is_a"
    to: "nahida-knowledge-scaling-and-sharding"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/scaling-and-sharding/sharded-ledgers.md"
      - "vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "bridges_to"
    to: "nahida-bridge-bft-consensus-to-sharded-ledgers"
    evidence_refs:
      - "vault/05_Bridges/bft-consensus-to-sharded-ledgers.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "bridges_to"
    to: "nahida-bridge-data-availability-to-sharded-ledgers"
    evidence_refs:
      - "vault/05_Bridges/data-availability-to-sharded-ledgers.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-sharded-ledgers"
    relation: "bridges_to"
    to: "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
    evidence_refs:
      - "vault/05_Bridges/database-transactions-to-byzantine-sharded-ledgers.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-bft-consensus-to-sharded-ledgers"
  - "nahida-bridge-data-availability-to-sharded-ledgers"
  - "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
source_note_refs:
  - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
  - "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
  - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
representative_source_refs:
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1905.09274v4"
  - "arxiv:1804.00399v4"
  - "arxiv:1809.09044v1"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
query_keys:
  - "Sharded ledgers"
  - "sharded-ledgers"
  - "blockchain sharding"
  - "分片账本"
  - "fraud proofs sharding"
  - "data availability proofs sharding"
  - "cross-shard smart contract execution"
  - "smart contract migration"
  - "LightCross"
aliases:
  - "blockchain sharding"
  - "分片账本"
domains:
  - "blockchain-systems"
topics:
  - "sharded-ledgers"
  - "fraud-proofs"
  - "light-client-security"
  - "cross-shard-transaction-execution"
  - "smart-contract-sharding"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-21"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-22"
created: "2026-06-20"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260621-ahl-sharding"
  - "nahida-knowledge-20260621-fraud-proofs-data-availability"
  - "nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts"
source_refs:
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1905.09274v4"
  - "arxiv:1804.00399v4"
  - "arxiv:1809.09044v1"
  - "doi:10.48550/arxiv.1809.09044"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
confidence: "medium"
trust_tier: "primary"
---

# Sharded ledgers

## 定义与范围

- 定义: Sharded ledgers 把账本状态、交易或验证者集合划分为多个 shard，以提高吞吐并降低每个节点处理负担。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `sharded-ledgers`
- Aliases/query keys: blockchain sharding, 分片账本
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `sharded-ledgers`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source seed 包含 OmniLedger、ByShard、RingBFT、LazyLedger、AHL、Fraud Proofs 和 LightCross，分别覆盖 Atomix/ByzCoinX、Byzantine multi-shard transactions、ring-topology cross-shard consensus、data-availability ledger split、TEE-assisted permissioned/general-workload sharding、no-single-node-validates-all-shards 时的 fraud/DA proof light-client safety pattern，以及 smart-contract CSTx 的 TEE executor/R-shard/contract migration route。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[scaling-and-sharding|scaling-and-sharding]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在分片扩容时保持 shard 内安全、跨 shard 原子性/隔离、状态 checkpoint 和通信复杂度可控。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[scaling-and-sharding|scaling-and-sharding]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[cross-shard-transaction-execution|Cross-shard transaction execution]] | adjacent problem | sharded ledgers 需要这个执行层问题才能支持 multi-shard smart-contract workloads；主路径放在 execution-and-transactions 下 | LightCross, AHL, ByShard, RingBFT | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| OmniLedger Atomix and trust-but-verify | OmniLedger Atomix and trust-but-verify | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| ByShard OEM + 2PC/2PL | ByShard OEM + 2PC/2PL | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| RingBFT linear cross-shard communication | RingBFT linear cross-shard communication | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| AHL+ with BFT reference committee | 用 TEE-assisted non-equivocating BFT 缩小 shard committee，用 TEE beacon 组片，并把 2PC/2PL coordinator 放进 BFT reference committee。 | permissioned blockchain、general workload、每节点具备 TEE、无 DoS。 | TEE 假设和 SGX simulation 边界明显；reference committee 可能瓶颈；应用需要 chaincode refactoring。 | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] |
| fraud/DA proof light-client safety | 当没有单个节点验证所有 shards 时，用 data availability proofs 确保数据可恢复，再让 fraud proofs 传播无效 shard/状态转换反证。 | sharded blockchain/light-client setting；至少一个 honest full node 或 shard observer 能看到数据并传播 proof。 | 不解决 shard assignment、cross-shard atomicity 或 execution semantics；网络 sampling/gossip 假设强。 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] |
| LightCross TEE executor + R-shard route | 将任意智能合约 CSTx 放入 TEE executor 执行，R-shard 批量排序，S-shards 验证 stale reads 并提交；用 TCG/Metis contract migration 降低跨片比例。 | permissioned smart-contract sharding; shard-level BFT and TEE accepted. | R-shard/executor availability、TEE trust 和 workload-locality assumptions；不解决 validator assignment 或 permissionless incentives。 | [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT: Resilient Consensus over Sharded Ring Topology]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | 把 sharded ledger 扩展到 permissioned/general workloads，组合 AHL+、TEE beacon、batch reconfiguration 与 BFT reference committee 事务协调 | TEE 信任假设重；评估不等同真实 SGX production；reference committee scaling 未完整解决 | Abstract, §3-§7 |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities]] | paper | 为 sharding 场景补充 fraud/DA proof light-client safety pattern：无单节点验证所有 shards 时，反证依赖数据可用 | 不是完整 sharding protocol；不处理 shard assignment/cross-shard transaction protocol | Abstract, §1, §3-§7 |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts]] | paper | 补入 smart-contract cross-shard execution route：TEE executors, R-shard schedule generation, S-shard bitmap validation and contract migration. | TEE/R-shard/executor assumptions; permissioned prototype; migration benefit depends on workload locality. | §III-§V, Appendix |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-21`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-21`。
- 综合: Sharded ledgers 是 scaling direction 的核心 problem node，不应以单个 protocol 命名。AHL 补充了 permissioned/general-workload 分支：通过 TEE 减少 shard-level BFT committee size，并用 reference committee 把数据库 2PC/2PL 的事务语义迁移到 Byzantine shard 环境。Fraud Proofs 不提供新的 shard assignment 或 cross-shard commit 协议，但补充了重要安全模式：当没有单个节点验证所有 shard 时，light-client invalidity detection 必须把 data availability 和 fraud proofs 绑定分析。LightCross 新增 smart-contract sharding 分支：跨片执行的 bottleneck 不只来自共识或组片，还来自任意合约逻辑如何跨 shard 执行；它用 TEE executor 和 R-shard batch validation 避免多轮 shard-to-shard execution，并用 contract migration 降低 CSTx ratio。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT: Resilient Consensus over Sharded Ring Topology]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | 增加 AHL route：TEE-assisted non-equivocating BFT + TEE RandomnessBeacon + batch reconfiguration + BFT reference committee for 2PC/2PL。 | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 后续补 TEE-assisted BFT 和 distributed transaction foundation sources |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] | 增加 sharded/light-client safety boundary：fraud proofs 需要 DA 才能让无效 shard/state 被挑战。 | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 细节留在 [[fraud-proofs|Fraud proofs]] 和 [[fraud-proofs-to-data-availability-sampling|Fraud proofs -> data availability sampling]] |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] | 增加 smart-contract sharding source extension：TEE executor + R-shard schedule generation + bitmap validation + smart contract migration。 | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合 | yes, adjacent child under execution direction | 细节留在 [[cross-shard-transaction-execution|Cross-shard transaction execution]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[bft-consensus-to-sharded-ledgers|BFT consensus -> sharded ledgers]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/scaling-and-sharding/sharded-ledgers` | application, dependency, translation | BFT quorum and shard-level consensus transfer; secure random validator assignment, cross-shard atomicity, transaction isolation, proof storage, workload locality, and economic incentives are sharded-ledger-specific. | active_seed |
| [[data-availability-to-sharded-ledgers|Data availability -> sharded ledgers]] | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling; blockchain-systems/scaling-and-sharding/sharded-ledgers` | dependency, shared_pattern | DA/fraud proofs help light-client invalidity detection; shard-level execution, cross-shard atomicity and validator assignment remain separate. | active_seed |
| [[database-transactions-to-byzantine-sharded-ledgers|Database transaction protocols -> Byzantine sharded ledgers]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/scaling-and-sharding/sharded-ledgers` | translation, implementation_reuse, dependency | 2PC/2PL structure transfers; Byzantine voting, shard consensus, cluster-sending, faulty clients, validator assignment, permissionless incentives, and data availability remain sharded-ledger-specific concerns. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-sharded-ledgers | is_a | nahida-knowledge-scaling-and-sharding | vault/04_Knowledge/blockchain-systems/scaling-and-sharding/sharded-ledgers.md; vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md | medium | active_seed |
| nahida-knowledge-sharded-ledgers | evidenced_by | vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md | vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md | medium | active_seed |
| nahida-knowledge-sharded-ledgers | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | medium | active_seed |
| nahida-knowledge-sharded-ledgers | evidenced_by | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | medium | active_seed |
| nahida-knowledge-sharded-ledgers | evidenced_by | vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md | vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md | medium | active_seed |
| nahida-knowledge-sharded-ledgers | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | high | active_seed |
| nahida-knowledge-sharded-ledgers | evidenced_by | vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md | Fraud Proofs source note | medium | active_seed |
| nahida-knowledge-sharded-ledgers | evidenced_by | vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md | LightCross source note | high | active_seed |
| nahida-knowledge-sharded-ledgers | bridges_to | nahida-bridge-bft-consensus-to-sharded-ledgers | vault/05_Bridges/bft-consensus-to-sharded-ledgers.md | medium | active_seed |
| nahida-knowledge-sharded-ledgers | bridges_to | nahida-bridge-data-availability-to-sharded-ledgers | vault/05_Bridges/data-availability-to-sharded-ledgers.md | medium | active_seed |
| nahida-knowledge-sharded-ledgers | bridges_to | nahida-bridge-database-transactions-to-byzantine-sharded-ledgers | vault/05_Bridges/database-transactions-to-byzantine-sharded-ledgers.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| modern execution sharding、rollup-centric scaling、Danksharding 缺 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts | Added LightCross as smart-contract CSTx route and linked adjacent cross-shard transaction execution node. | sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2 | codex |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 4 source notes; 3 legacy notes | codex |
| 2026-06-21 | nahida-knowledge-20260621-ahl-sharding | Added AHL as a sharded-ledger source extension for permissioned/general workload sharding, TEE-assisted committee sizing and BFT reference-committee transaction coordination. | arxiv:1804.00399v4 | codex |
| 2026-06-21 | nahida-knowledge-20260621-fraud-proofs-data-availability | Added Fraud Proofs as sharded/light-client safety boundary, routed through DA/fraud-proof bridges. | arxiv:1809.09044v1 | codex |
