---
id: "nahida-knowledge-byzantine-fault-tolerance"
title: "Byzantine fault tolerance"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "byzantine-fault-tolerance"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-consensus"
child_knowledge_refs:
  - "nahida-knowledge-asynchronous-bft-consensus"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "byzantine-fault-tolerance"
primary_ontology_path: "distributed-systems/consensus/byzantine-fault-tolerance"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "is_a"
    to: "nahida-knowledge-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md"
      - "vault/04_Knowledge/distributed-systems/consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "has_child"
    to: "nahida-knowledge-asynchronous-bft-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "bridges_to"
    to: "nahida-bridge-bft-consensus-to-sharded-ledgers"
    evidence_refs:
      - "vault/05_Bridges/bft-consensus-to-sharded-ledgers.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "bridges_to"
    to: "nahida-bridge-bft-consensus-to-shared-mempool-scaling"
    evidence_refs:
      - "vault/05_Bridges/bft-consensus-to-shared-mempool-scaling.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-blockchain-finality"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-blockchain-finality.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-open-network-blockchain-governance"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-open-network-blockchain-governance.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "bridges_to"
    to: "nahida-bridge-bft-consensus-to-permissioned-blockchains"
    evidence_refs:
      - "vault/05_Bridges/bft-consensus-to-permissioned-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-byzantine-fault-tolerance"
    relation: "bridges_to"
    to: "nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types"
    evidence_refs:
      - "vault/05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-bft-consensus-to-sharded-ledgers"
  - "nahida-bridge-bft-consensus-to-shared-mempool-scaling"
  - "nahida-bridge-bft-consensus-to-permissioned-blockchains"
  - "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
  - "nahida-bridge-distributed-bft-to-blockchain-finality"
  - "nahida-bridge-distributed-bft-to-open-network-blockchain-governance"
  - "nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types"
source_note_refs:
  - "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
  - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
  - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
  - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
  - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
  - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
  - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
  - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
  - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
  - "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
  - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore.md"
representative_source_refs:
  - "hal:hal-00944019v2"
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1802.07240"
  - "arxiv:2203.05158"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "doi:10.1145/3293611.3331612"
  - "doi:10.1145/167088.167105"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
  - "arxiv:1804.00399v4"
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
query_keys:
  - "Byzantine fault tolerance"
  - "byzantine-fault-tolerance"
  - "BFT"
  - "Byzantine agreement"
  - "Byzantine fault tolerant consensus"
  - "HotStuff-based BFT"
  - "multi-instance BFT"
  - "workload-adaptive BFT"
  - "Stretch-BFT"
  - "validated asynchronous Byzantine agreement"
  - "VABA"
  - "optimal asynchronous Byzantine agreement"
  - "asynchronous verifiable secret sharing"
  - "AVSS"
  - "BFT CRDT"
  - "equivocation tolerant CRDT"
aliases:
  - "BFT"
  - "Byzantine agreement"
  - "Byzantine fault tolerant consensus"
  - "workload-adaptive BFT"
  - "VABA"
  - "AVSS-backed async BA"
  - "Byzantine fault tolerant CRDTs"
domains:
  - "distributed-systems"
topics:
  - "byzantine-fault-tolerance"
  - "equivocation-tolerant-crdts"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-stretch-bft"
  - "nahida-paper-intake-20260620-item-0034"
  - "nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement"
  - "nahida-knowledge-20260621-ahl-sharding"
  - "nahida-knowledge-20260623-canetti-rabin-optimal-async-ba"
  - "nahida-paper-intake-20260623-canteen-crdt-datastore"
source_refs:
  - "hal:hal-00944019v2"
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1802.07240"
  - "arxiv:2203.05158"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "doi:10.1145/3293611.3331612"
  - "doi:10.1145/167088.167105"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
  - "arxiv:1804.00399v4"
  - "sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84"
confidence: "medium"
trust_tier: "primary"
---

# Byzantine fault tolerance

## 定义与范围

- 定义: Byzantine fault tolerance (BFT) 处理参与者可任意偏离协议、发送冲突消息、沉默或恶意协作时仍要获得一致决定或一致顺序的问题。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `byzantine-fault-tolerance`
- Aliases/query keys: BFT, Byzantine agreement, Byzantine fault tolerant consensus
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `byzantine-fault-tolerance`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

source-backed seed 包含 Byzantine Generals 与 PBFT，并通过 Canetti-Rabin AVSS/global coin、VABA、Tendermint、Cobalt、Stratus、MyTumbler/SuperMA、EPIC、ByShard/RingBFT、Stretch-BFT、AHL 展开到异步协议和区块链应用。Canetti-Rabin 补上最优 resilience asynchronous BA 的 AVSS-backed randomness route；VABA 补上 externally valid multi-valued asynchronous agreement 这一层；Stretch-BFT 补上 permissioned blockchain 中 HotStuff-style BFT 如何处理 proposer bottleneck、workload fluctuation 和 multi-instance recovery；AHL 补上 TEE-assisted non-equivocating BFT 如何把 shard-level fault threshold 和 committee sizing 连接起来。Canteen 新增一个非 consensus 边界: CRDT 也会遇到 Byzantine/equivocation，但目标是 SEC/convergence，而不是 total-order agreement。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[consensus|consensus]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在 arbitrary faulty participants 和 equivocation 存在时保障 agreement、safety、SMR 或应用层 finality/governance。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[consensus|consensus]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[asynchronous-bft-consensus|asynchronous-bft-consensus]] | child/problem | 异步网络中 BFT progress 需要 common coin、RBC/BA、VABA、ACS 等专门结构 | existing source-backed child | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| oral/signed-message Byzantine agreement | oral/signed-message Byzantine agreement | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| PBFT-style practical BFT SMR | PBFT-style practical BFT SMR | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| stake-weighted blockchain finality | stake-weighted blockchain finality | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| open-network local trust | open-network local trust | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| asynchronous/randomized BFT | asynchronous/randomized BFT | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| AVSS-backed randomized async BA | 用 AVSS 构造 global coin，再通过 Vote + Global-Coin 迭代获得最优 resilience asynchronous BA。 | 完全异步私有信道，dynamic/unbounded Byzantine adversary，`n >= 3t+1`。 | extended abstract 省略部分完整证明；不处理系统实现或区块链 workload。 | [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Canetti-Rabin 1993]] |
| Validated asynchronous Byzantine agreement | 在异步 BFT 中加入外部有效性和多值决定，使 agreement 可作为 Atomic Broadcast/SMR primitive。 | authenticated async BFT，`f < n/3`，可验证 application-level validity。 | 需要 threshold signatures/coin/setup；不等同完整 blockchain 或 mempool 协议。 | [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|VABA 2019]] |
| Workload-adaptive multi-instance BFT | 用多个 BFT instances 分摊 proposer 负载，并按 workload/throughput 在 Era 边界伸缩实例数。 | permissioned/known-membership setting，工作负载波动明显，且能收集可信身份下的 workload reports。 | 需要处理 Byzantine reports、failed instances、slow proposers；不能绕过每个节点接收/验证交易的稳定吞吐上限。 | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] |
| TEE-assisted non-equivocating BFT | 用 enclave 内 attested append-only memory 约束 Byzantine 节点不能 equivocate，从而把 quorum/fault-threshold route 推向 `N=2f+1`。 | 每个 replica 有可信 TEE；TEE keys/signatures/integrity 和 rollback recovery 可信。 | 不消除通信/view-change 瓶颈；硬件信任和 SGX deployment 约束很强。 | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL]] |
| Equivocation-tolerant CRDT replication | 用 hash-chained causal history/DAG roots 暴露 Byzantine replica 的 conflicting histories，让 CRDT 在 SEC 语境下处理 equivocation。 | coordination-free replicated data types, correct replicas eventually communicate | 不提供 BFT consensus 的 total-order/quorum protocol；目标是 convergence，不是 agreement on one ordered log。 | [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-357172-357176-byzantine-generals-problem|The Byzantine Generals Problem]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|Practical Byzantine Fault Tolerance]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT: Resilient Consensus over Sharded Ring Topology]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Fast Asynchronous Byzantine Agreement with Optimal Resilience]] | paper | 把 BFT agreement 扩展到完全异步、dynamic/unbounded adversary、`n>=3t+1` 的 fast randomized BA；核心路线是 AVSS-backed global coin | private channels；extended abstract；不含实现评测 | Abstract, Theorem 1-2, §5-§9 |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|Asymptotically Optimal Validated Asynchronous Byzantine Agreement]] | paper | 把 BFT agreement 扩展到 externally-valid multi-valued asynchronous agreement：expected `O(1)` time, expected `O(n^2)` word communication, `f<n/3` | authenticated setting；threshold signatures/coin；不含系统实现 | Definition 4, Theorem 1, §3.1-§3.6 |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | paper | 将 HotStuff-style BFT source extension 到 permissioned blockchain 的 workload-adaptive multi-instance route：workload sensing、instance reconfiguration、failed instance recovery | permissioned/known-membership；LAN prototype；不代表 permissionless validator economics | `p1-p13` |
| [[hal-00944019v2-signature-free-asynchronous-byzantine-consensus|Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages]] | paper | 补入 asynchronous binary BFT 的 common-coin/BV-broadcast baseline，展示 signature-free、`t<n/3`、每轮 `O(n^2)` messages 可同时成立 | 依赖 common coin 抽象；只处理 binary consensus | Abstract, Table 1, §3-§4 |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | 补入 AHL/AHL+：通过 TEE append-only log 消除 equivocation，并把 non-equivocating BFT 用于 shard committee sizing 和 throughput scaling | TEE/SGX trust assumptions；simulation-mode evaluation；AHL 是应用 source extension 不是 BFT foundation 替代 | §4.1, §5.2, §7.1 |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen: A Partially-Ordered Log Abstraction for the Emerging CRDT Datastore]] | paper | 补入 CRDT 语境下的 equivocation-tolerant route：hash-chained operation DAG 和 roots-as-logical-clocks 可暴露 conflicting causal histories | 主路径是 CRDT/data-management；不是 BFT consensus protocol | §2.7, §3.1-§3.2 |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: BFT 是 fault model/problem family；PBFT、Canetti-Rabin、VABA、Tendermint、Cobalt、EPIC、Stretch-BFT、AHL、Mostefaoui-Moumen-Raynal 2014 等是 source extensions 或应用/方法分支。Canetti-Rabin 新增的结构性信号是最优 resilience async BA 需要可共同生成随机性的 AVSS/global-coin 层；VABA 新增的结构性信号是 async BFT 需要 external validity 和 quality property 才能服务 Atomic Broadcast/SMR；async binary consensus source 补强了 common-coin/BV-broadcast foundation；Stretch-BFT 说明 BFT 在 permissioned blockchain 中还要把 proposer bandwidth、workload fluctuation、sluggish proposer 和 failed instance recovery 纳入运行时控制；AHL 说明 trusted hardware 可以改变 equivocation model 和 shard committee sizing，但代价是硬件信任与 rollback 防御。Canteen 则把 equivocation threat 带到 CRDT/SEC 语境，强调 BFT vocabulary 可迁移，但 consensus quorum/total-order protocol 不能直接迁移。

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
| [[doi-10-1145-357172-357176-byzantine-generals-problem|The Byzantine Generals Problem]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|Practical Byzantine Fault Tolerance]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT: Resilient Consensus over Sharded Ring Topology]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Fast Asynchronous Byzantine Agreement with Optimal Resilience]] | 增加 AVSS-backed randomized async BA source extension，并通过 async BFT child 节点新建 AVSS method/concept | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes, through async BFT child method | 后续补 Canetti-Rabin technical report、Bracha A-cast/RBC、modern AVSS/common-coin source |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|Asymptotically Optimal Validated Asynchronous Byzantine Agreement]] | 增加 VABA source extension：externally-valid multi-valued async Byzantine agreement 的 `O(n^2)` route 和 Atomic Broadcast/SMR primitive 关系 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes, through async BFT child node | 后续补 Cachin 2001、HoneyBadger/BEAT/RBC/common coin source |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | 增加 permissioned BFT source extension：HotStuff-based multi-instance 共识通过 BFT workload sensing、Era-level reconfiguration 和 failed instance recovery 适配 workload 波动 | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 HotStuff/Mir-BFT/RCC source 时复核 multi-instance BFT 分支是否需要拆 child node |
| [[hal-00944019v2-signature-free-asynchronous-byzantine-consensus|Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages]] | 增加 asynchronous BFT foundation source：BV-broadcast + common coin 的 signature-free binary Byzantine consensus | 代表 Sources; 当前综合; 关系图谱 | no | 保持在 async BFT child 节点为主 |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | 增加 TEE-assisted non-equivocating BFT source extension：AHL/AHL+ 用 attested append-only memory 降低 equivocation，并影响 shard committee size 与吞吐。 | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 后续补 TrInc/MinBFT/Hybrids on Steroids 等 trusted-hardware BFT foundations |
| [[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] | 增加 CRDT 语境下的 equivocation-tolerant source extension，并创建 BFT -> CRDT bridge。 | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 后续补 Making CRDTs Byzantine Fault Tolerant、equivocation-tolerant CmRDT 等 direct sources |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[bft-consensus-to-sharded-ledgers|BFT consensus -> sharded ledgers]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/scaling-and-sharding/sharded-ledgers` | application, dependency, translation | BFT quorum and shard-level consensus transfer; secure random validator assignment, cross-shard atomicity, transaction isolation, proof storage, workload locality, and economic incentives are sharded-ledger-specific. | active_seed |
| [[bft-consensus-to-shared-mempool-scaling|BFT consensus -> shared mempool scaling]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/mempool-and-networking/shared-mempool` | application, dependency, implementation_reuse | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 | active_seed |
| [[bft-consensus-to-permissioned-blockchains|BFT consensus -> permissioned blockchains]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/consensus/permissioned-blockchain-consensus` | application, translation, implementation_reuse | BFT quorum/HotStuff-style safety transfers; permissioned workload sensing, client identity, deterministic Era reconfiguration, and resource-aware proposer selection are application-specific. | active_seed |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | `distributed-systems/consensus/byzantine-fault-tolerance; distributed-systems/consensus/asynchronous-bft-consensus` | application, translation, dependency | The BFT fault threshold and quorum-intersection safety intuition transfer; fixed-slot overhead, pass/skip advancement, timestamp efficiency, adaptive corruption, threshold-crypto setup, common-coin liveness, transaction selection, and WAN workload behavior are asynchronous blockchain consensus-specific. | active_seed |
| [[distributed-bft-to-blockchain-finality|Distributed BFT -> blockchain finality]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/consensus/proof-of-stake-finality` | application, dependency, translation | Classical BFT quorum and safety arguments transfer; token economics, validator churn, unbonding periods, light-client trust, and long-range attacks require blockchain-specific assumptions. | active_seed |
| [[distributed-bft-to-open-network-blockchain-governance|Distributed BFT -> open-network blockchain governance]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/consensus/open-network-bft-governance` | translation, application, tension | Classical BFT agreement/reliable-broadcast reasoning transfers only after adapting quorums to local UNL/essential-subset support; governance Full-Knowledge, transaction-network delegation, randomizing-key CRS, and operator trust configuration are blockchain/open-network-specific. | active_seed |
| [[05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types|Byzantine fault tolerance -> CRDTs]] | `distributed-systems/consensus/byzantine-fault-tolerance; distributed-systems/data-management-and-storage/conflict-free-replicated-data-types` | adaptation, equivocation_boundary, non_transfer_boundary | Byzantine/equivocation threat model transfers to CRDT causal histories; BFT consensus quorum/total-order protocol does not automatically transfer to SEC. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-byzantine-fault-tolerance | is_a | nahida-knowledge-consensus | vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md; vault/04_Knowledge/distributed-systems/consensus.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | has_child | nahida-knowledge-asynchronous-bft-consensus | vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md | vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md | high | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md | vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md | vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | high | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md | vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md | high | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md | vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md | high | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | high | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | bridges_to | nahida-bridge-bft-consensus-to-sharded-ledgers | vault/05_Bridges/bft-consensus-to-sharded-ledgers.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | bridges_to | nahida-bridge-bft-consensus-to-shared-mempool-scaling | vault/05_Bridges/bft-consensus-to-shared-mempool-scaling.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | bridges_to | nahida-bridge-bft-consensus-to-permissioned-blockchains | vault/05_Bridges/bft-consensus-to-permissioned-blockchains.md | high | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | bridges_to | nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus | vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | bridges_to | nahida-bridge-distributed-bft-to-blockchain-finality | vault/05_Bridges/distributed-bft-to-blockchain-finality.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | bridges_to | nahida-bridge-distributed-bft-to-open-network-blockchain-governance | vault/05_Bridges/distributed-bft-to-open-network-blockchain-governance.md | medium | active_seed |
| nahida-knowledge-byzantine-fault-tolerance | bridges_to | nahida-bridge-byzantine-fault-tolerance-to-conflict-free-replicated-data-types | vault/05_Bridges/byzantine-fault-tolerance-to-conflict-free-replicated-data-types.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| FLP、DLS、Bracha RBC、HotStuff、HoneyBadgerBFT、BEAT、Narwhal/Tusk 缺 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |
| Common coin 与 AVSS/BV-broadcast/RBC/ACS 的关系仍需更多 source。 | Canetti-Rabin 给出 AVSS-backed global coin；其他 sources 使用 common/threshold coin 抽象，需决定是否拆独立节点 | nahida-research-search or future papers | medium | queued |
| Cachin et al. 2001 VABA source 与 weak-termination 问题缺直接 source。 | VABA 2019 的 baseline 和 open question 目前只由该 source 转述 | nahida-research-search or future papers | high | queued |
| BFT CRDT direct sources 仍缺。 | Canteen 提供应用边界，但 Kleppmann 2022 / equivocation-tolerant CRDTs direct source 未单独吸收 | nahida-research-search or future papers | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 9 source notes; 3 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-stretch-bft | Added Stretch-BFT as permissioned BFT source extension and created BFT-to-permissioned-blockchain bridge. | 1 source note | codex |
| 2026-06-20 | nahida-paper-intake-20260620-item-0034 | Added Mostefaoui-Moumen-Raynal signature-free asynchronous binary BFT source as foundation evidence. | hal:hal-00944019v2 | codex |
| 2026-06-20 | nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement | Added VABA as externally-valid multi-valued async BFT source extension and child-node evidence through async BFT. | doi:10.1145/3293611.3331612 | codex |
| 2026-06-21 | nahida-knowledge-20260621-ahl-sharding | Added AHL/AHL+ as TEE-assisted non-equivocating BFT source extension for sharded-ledger committee sizing. | arxiv:1804.00399v4 | codex |
| 2026-06-23 | nahida-knowledge-20260623-canetti-rabin-optimal-async-ba | Added Canetti-Rabin as AVSS-backed optimal-resilience async BA source extension. | doi:10.1145/167088.167105 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-canteen-crdt-datastore | Added Canteen as equivocation-tolerant CRDT boundary evidence and linked BFT to CRDTs through a non-transfer bridge. | sha256:ac567f8d9ef660c15e5aab965f44ef032223b6a9180697cc4ad8c2ec61c7cf84 | codex |
