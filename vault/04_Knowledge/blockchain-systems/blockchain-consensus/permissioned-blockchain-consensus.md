---
id: "nahida-knowledge-permissioned-blockchain-consensus"
title: "Permissioned blockchain consensus"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "permissioned-blockchain-consensus"
domain_id: "blockchain-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-consensus"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "permissioned-blockchain-consensus"
primary_ontology_path: "blockchain-systems/consensus/permissioned-blockchain-consensus"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-consensus"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus/permissioned-blockchain-consensus.md"
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "bridges_to"
    to: "nahida-bridge-crash-fault-consensus-to-permissioned-blockchains"
    evidence_refs:
      - "vault/05_Bridges/crash-fault-consensus-to-permissioned-blockchains.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "bridges_to"
    to: "nahida-bridge-bft-consensus-to-permissioned-blockchains"
    evidence_refs:
      - "vault/05_Bridges/bft-consensus-to-permissioned-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "bridges_to"
    to: "nahida-bridge-permissioned-consensus-to-transaction-execution"
    evidence_refs:
      - "vault/05_Bridges/permissioned-consensus-to-transaction-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-permissioned-blockchain-consensus"
    relation: "bridges_to"
    to: "nahida-bridge-permissioned-consensus-to-cross-chain-bridges"
    evidence_refs:
      - "vault/05_Bridges/permissioned-consensus-to-cross-chain-bridges.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-crash-fault-consensus-to-permissioned-blockchains"
  - "nahida-bridge-bft-consensus-to-permissioned-blockchains"
  - "nahida-bridge-permissioned-consensus-to-transaction-execution"
  - "nahida-bridge-permissioned-consensus-to-cross-chain-bridges"
source_note_refs:
  - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
  - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
  - "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
representative_source_refs:
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
  - "sha256:9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
query_keys:
  - "Permissioned blockchain consensus"
  - "permissioned-blockchain-consensus"
  - "permissioned CFT consensus"
  - "permissioned BFT consensus"
  - "SRaft"
  - "SRaft scalable CFT consensus"
  - "Block Replicating Tree"
  - "Stretch-BFT"
  - "workload-adaptive BFT consensus"
  - "leaderless consensus execution"
  - "consensus execution co-design"
  - "consensus signatures for bridges"
  - "permissioned cross-chain bridge"
  - "sigBridge"
aliases:
  - "permissioned CFT consensus"
  - "permissioned BFT consensus"
  - "SRaft"
  - "Scalable CFT consensus for permissioned blockchain"
  - "Stretch-BFT"
  - "Workload-adaptive BFT consensus"
  - "sigBridge"
  - "permissioned cross-chain bridge"
domains:
  - "blockchain-systems"
topics:
  - "permissioned-blockchain-consensus"
  - "permissioned cross-chain bridges"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-22"
created: "2026-06-20"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-sraft-scalable-cft"
  - "nahida-knowledge-20260620-stretch-bft"
  - "nahida-knowledge-20260620-tell-leaderless-consensus-execution"
  - "nahida-knowledge-20260622-sigbridge"
source_refs:
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "sha256:9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
confidence: "medium"
trust_tier: "primary"
---

# Permissioned blockchain consensus

## 定义与范围

- 定义: Permissioned blockchain consensus 关注已知成员或许可环境中如何用 CFT/BFT 协议排序区块/交易并满足链式数据结构需求。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `permissioned-blockchain-consensus`
- Aliases/query keys: permissioned CFT consensus, SRaft
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `permissioned-blockchain-consensus`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source seed 包含两条 permissioned consensus 路线和一条跨方向用途：SRaft 系列说明 CFT/Raft 进入许可链后，问题不只是 log ordering，而是完整区块复制、peer 数扩张和 workload skew 共同造成的 leader/overloaded-peer 带宽瓶颈；Stretch-BFT 则说明在 Byzantine setting 中，HotStuff-style BFT 可通过 workload sensing 和 multi-instance reconfiguration 在吞吐与 latency 之间动态折中；sigBridge 说明 permissioned consensus 的 signatures、public keys 和 threshold rules 还可以作为 cross-chain header verification 的输入。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[blockchain-consensus|blockchain-consensus]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在许可链场景下维持 ordering/replication/finality，同时避免 CFT leader 或 BFT proposer 被完整区块复制、workload fluctuation、slow proposer 和 failed instance 拖垮。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[blockchain-consensus|blockchain-consensus]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Raft/CFT baseline | 在已知成员、crash-fault setting 中复用 majority replicated-log / ordering 思路。 | 许可链准入较强、主要关心 crash/recovery。 | 不覆盖 Byzantine 行为、开放成员和经济安全。 | [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|Raft]]; [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft scalable CFT]] |
| Replication/order split | 完整 block 先由多 initiators 复制到多数 peers，leader 只排序 hash。 | block 较大、peer 数多、leader 带宽容易成为瓶颈。 | 需要处理本地缺失 block 的 pull、复制完成与排序之间的异步边界。 | [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft scalable CFT]] |
| Workload-adaptive relay | 高负载 initiator 使用 Tree-based/BRT 转发，让轻负载 peers 分担上传。 | workload skew 明显，且 peers 可报告/估计可用带宽。 | relay failure、sluggish relay 和带宽估计误差会影响延迟。 | [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft scalable CFT]] |
| Hash ordering pipeline | ordering leader 广播 hash order，并把上一轮 commit 与下一轮 proposal/collection 合并。 | blocks 已经安全复制，ordering 网络负载主要是 hash metadata。 | leader 仍是 hash ordering 协调者；安全性仍依赖 CFT/多数假设。 | [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft scalable CFT]] |
| HotStuff/BFT baseline | 在 `N >= 3f + 1`、partial synchrony 和 PKI 身份下复用 BFT quorum/QC/SAFENODE 思路排序 sub-block。 | 节点已知、需要容忍 Byzantine proposer 或 equivocation。 | 比 CFT 成本更高；仍会遇到 proposer bandwidth 和 slow proposer latency。 | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] |
| Workload-adaptive multi-instance BFT | 在 heavy workload 下增加 BFT instances/proposers，在 light workload 下减少 instances，按 Era 用 workload/throughput 反馈调整。 | workload 波动明显，且系统能通过身份和 consistent hashing 收集 workload reports。 | 需要 trimmed report aggregation、deterministic Era switch、failed instance recovery；盲目增加 instances 会受 download/verify bottleneck 限制。 | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] |
| Consensus-aware execution boundary | 共识的 instance/order/timestamp 结构成为 execution scheduling 和 commit unit 的输入。 | leaderless/multi-instance permissioned consensus 已输出确定 block/order 元数据。 | 这是 execution 依赖 consensus 的边界，不是新的 consensus safety 路线。 | [[permissioned-consensus-to-transaction-execution|Permissioned consensus -> transaction execution]] |
| Consensus-signature verification for bridges | 把源链 consensus signatures、public keys 和 threshold rules 暴露给目标链 updater contract，作为 cross-chain header synchronization 的 verification material。 | 源链和目标链是许可链，membership/keys/consensus rules 可被安全初始化或治理更新。 | 不自动解决 relayer liveness、trusted setup、signature count scaling 或 heterogeneous consensus abstraction；抽样验证会引入 `epsilon` 概率边界。 | [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain]] | paper | 将 SRaft 从 demo 级设计扩展为完整机制与实验来源：BRT、workload-adaptive replication、失败恢复、Sending-Receiving pipeline、FISCO BCOS Raft 对比 | CFT-only；LAN 模拟；不计 transaction execution；无完整形式化证明 | `p1-p16` |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | paper | 增加 permissioned BFT 路线：HotStuff-based multi-instance consensus、BFT workload sensing、Era-level reconfiguration、failed instance recovery | permissioned/known-membership；LAN prototype；不代表 permissionless validator economics | `p1-p13` |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus]] | paper | 作为 bridge evidence 说明 permissioned leaderless consensus 的 instance 结构会影响 transaction execution；不把 TELL 归类为 consensus protocol | execution-focused; RCC+PBFT evaluation; consensus latency excluded | `p1-p13` |
| [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control]] | paper | 作为 bridge evidence 说明 permissioned consensus signatures 可以成为 cross-chain header verification material，并支持 updater contract 抽样验证 | bridge/interoperability-focused; trusted initialization; single PoA/private-Ethereum prototype | `p1-p10` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-22`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: SRaft、Stretch-BFT 和 sigBridge 都是 source/protocol/application instances，不是 foundation。父问题是 permissioned blockchain consensus: 在已知成员系统中，用 CFT 或 BFT 保证 ordering/replication/finality，同时控制完整 block dissemination、leader/proposer bandwidth、workload skew/fluctuation 和 failed/sluggish participants。当前可复用路线分两支: CFT route 是 replication/order split + workload-adaptive relay + hash ordering pipeline；BFT route 是 HotStuff-style multi-instance consensus + BFT workload sensing + Era-level reconfiguration + failed instance recovery。sigBridge 新增的 synthesis 是: permissioned consensus 输出的 signatures 和 threshold rules 还可被跨链桥复用为 header verification evidence，但这是 interoperability/application route，不改变 consensus safety foundation。

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
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain]] | 完整 SRaft source extension：用 leaderless Block Replicating、workload-adaptive BRT 和 hash-only Block Ordering 解决许可链中 Raft leader/full-block replication 瓶颈，并给出 workload skew、scalability、sluggish peers 和 FISCO BCOS 对比实验 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 Fabric/FISCO/CRaft/Stretch-BFT 时比较 CFT/BFT 与 relay/adaptive route |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | 完整 Stretch-BFT source extension：将 HotStuff-style BFT 扩展为按 Era 伸缩的多实例 permissioned consensus，并用 workload sensing、trimmed reports、deterministic proposer selection 和 recovery 处理 workload fluctuation 与 proposer failure | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 HotStuff/Mir-BFT/RCC source 时复核 BFT 多实例分支 |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus]] | bridge-only source extension：TELL 不是 consensus 协议，但说明 leaderless consensus instance 结构、block interval 和 ordering unit 会成为 execution 层的设计输入 | 方法族与解决路线; Bridge Links; 关系图谱 | no | 后续吸收 RCC/MIR-BFT/Nezha/SChain 时比较 consensus-execution 边界 |
| [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control]] | bridge-only source extension：sigBridge 不是 consensus 协议，但说明 permissioned consensus signatures/threshold rules 可作为 cross-chain updater contract 的 verification material | 方法族与解决路线; Bridge Links; 关系图谱 | no | 后续吸收 permissioned bridge/IBC/PoA sources 时比较 signature-based 和 proof-based bridge routes |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[crash-fault-consensus-to-permissioned-blockchains|Crash-fault consensus -> permissioned blockchains]] | `distributed-systems/consensus/crash-fault-tolerance; blockchain-systems/consensus/permissioned-blockchain-consensus` | application, translation, implementation_reuse | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 | active_seed |
| [[bft-consensus-to-permissioned-blockchains|BFT consensus -> permissioned blockchains]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/consensus/permissioned-blockchain-consensus` | application, translation, implementation_reuse | BFT quorum/HotStuff-style safety transfers; permissioned workload sensing, client identity, deterministic Era reconfiguration, and resource-aware proposer selection are application-specific. | active_seed |
| [[permissioned-consensus-to-transaction-execution|Permissioned consensus -> transaction execution]] | `blockchain-systems/consensus/permissioned-blockchain-consensus; blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution` | dependency, co_evolution, implementation_reuse, tension | Consensus instance/order metadata can guide execution scheduling and commit units; execution optimization does not prove consensus safety. | active_seed |
| [[permissioned-consensus-to-cross-chain-bridges|Permissioned consensus -> cross-chain bridges]] | `blockchain-systems/consensus/permissioned-blockchain-consensus; blockchain-systems/interoperability/cross-chain-protocols` | dependency, application, verification_material | Consensus signatures and known validator sets can verify remote headers; bridge liveness, setup, transaction proofs and heterogeneous consensus abstraction remain outside consensus itself. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-permissioned-blockchain-consensus | is_a | nahida-knowledge-blockchain-consensus | vault/04_Knowledge/blockchain-systems/blockchain-consensus/permissioned-blockchain-consensus.md; vault/04_Knowledge/blockchain-systems/blockchain-consensus.md | medium | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | medium | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md | high | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md | vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md | high | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | bridges_to | nahida-bridge-crash-fault-consensus-to-permissioned-blockchains | vault/05_Bridges/crash-fault-consensus-to-permissioned-blockchains.md | medium | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | bridges_to | nahida-bridge-bft-consensus-to-permissioned-blockchains | vault/05_Bridges/bft-consensus-to-permissioned-blockchains.md | high | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | bridges_to | nahida-bridge-permissioned-consensus-to-transaction-execution | vault/05_Bridges/permissioned-consensus-to-transaction-execution.md | high | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md | sigBridge source note | high | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | bridges_to | nahida-bridge-permissioned-consensus-to-cross-chain-bridges | vault/05_Bridges/permissioned-consensus-to-cross-chain-bridges.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Fabric/Quorum/IBFT/HotStuff-based permissioned chains 缺 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |
| permissioned consensus as interoperability evidence 仍只有 sigBridge 一个 source。 | 需要更多 permissioned bridge 或 light-client sources 验证该 route 的一般性。 | nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-sraft-scalable-cft | Added 16-page SRaft full paper as source extension; refined permissioned CFT bottleneck and workload-adaptive replication route. | 1 source note | codex |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 2 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-stretch-bft | Added Stretch-BFT as permissioned BFT source extension; separated CFT/Raft and BFT/HotStuff-style solution routes. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-tell-leaderless-consensus-execution | Added bridge-only extension showing permissioned leaderless consensus structure as transaction execution input. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-sigbridge | Added bridge-only extension showing permissioned consensus signatures as cross-chain bridge verification material. | 1 source note | codex |
