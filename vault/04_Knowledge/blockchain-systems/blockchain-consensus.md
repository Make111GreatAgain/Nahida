---
id: "nahida-knowledge-blockchain-consensus"
title: "Blockchain consensus"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "blockchain-consensus"
domain_id: "blockchain-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
child_knowledge_refs:
  - "nahida-knowledge-open-network-bft-governance"
  - "nahida-knowledge-permissioned-blockchain-consensus"
  - "nahida-knowledge-proof-of-stake-finality"
ontology_path:
  - "blockchain-systems"
  - "consensus"
primary_ontology_path: "blockchain-systems/consensus"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-systems"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus.md"
      - "vault/04_Knowledge/blockchain-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "has_child"
    to: "nahida-knowledge-open-network-bft-governance"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus.md"
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus/open-network-bft-governance.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "has_child"
    to: "nahida-knowledge-permissioned-blockchain-consensus"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus.md"
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus/permissioned-blockchain-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "has_child"
    to: "nahida-knowledge-proof-of-stake-finality"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus.md"
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus/proof-of-stake-finality.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
  - "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
  - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
  - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
  - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
  - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
  - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
  - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
representative_source_refs:
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1710.09437v4"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
  - "arxiv:1802.07240"
  - "arxiv:2203.05158"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
query_keys:
  - "Blockchain consensus"
  - "blockchain-consensus"
  - "区块链共识"
  - "permissioned BFT consensus"
  - "workload-adaptive BFT"
  - "FedChain"
  - "federated-blockchain systems"
  - "FedChain PoS consensus"
  - "PVSS FTS PoS"
aliases:
  - "区块链共识"
domains:
  - "blockchain-systems"
topics:
  - "blockchain-consensus"
  - "cross-chain-incentives"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
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
  - "nahida-knowledge-20260622-fedchain"
source_refs:
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1710.09437v4"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
  - "arxiv:1802.07240"
  - "arxiv:2203.05158"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
  - "doi:10.1109/tsc.2023.3240235"
confidence: "medium"
trust_tier: "primary"
---

# Blockchain consensus

## 定义与范围

- 定义: Blockchain consensus 是把分布式共识应用到区块链 ordering、finality、validator/governance 和开放网络安全边界中的方向。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `blockchain-consensus`
- Aliases/query keys: 区块链共识
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `blockchain-consensus`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

它复用 CFT/BFT/SMR，但会加入 stake、slashing、unbonding、validator churn、client sync、open membership、network load 等区块链特有假设。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[blockchain-systems|blockchain-systems]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在开放或许可链中让节点对区块/交易顺序和最终性达成可验证、可追责或可恢复的决定。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[blockchain-systems|blockchain-systems]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[proof-of-stake-finality|proof-of-stake-finality]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[permissioned-blockchain-consensus|permissioned-blockchain-consensus]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[open-network-bft-governance|open-network-bft-governance]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| PoS finality | PoS finality: Tendermint/Casper | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Permissioned CFT | Permissioned CFT: SRaft | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Permissioned BFT | 在已知成员许可链中复用 BFT/HotStuff-style safety，并用 workload-adaptive multi-instance 控制 proposer bottleneck。 | 需要容忍 Byzantine proposer，且 workload 有明显波动。 | 依赖 permissioned identity/workload reports；不等同 permissionless validator economics。 | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] |
| Open-network governance | Open-network governance: Cobalt | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Asynchronous BFT | Asynchronous BFT: MyTumbler/SuperMA/EPIC | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Federated PoS with PVSS/FTS | 用 PVSS randomness、FTS stake-proportional leader/committee selection、empty blocks 和 longest-valid-fork rule 支撑 federated-chain security。 | PoS chains 需要为 cross-chain transfer 提供 source-chain finality/security substrate。 | stake centralization 和 adversary >50% stake 会破坏安全；Stackelberg incentives 是 FedChain-specific route。 | [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1710-09437v4-casper-friendly-finality-gadget|Casper the Friendly Finality Gadget]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain]] | paper | 为 permissioned CFT branch 增加完整机制与实验证据：replication/order split、BRT、workload skew、FISCO BCOS Raft 对比 | CFT-only；不代表 BFT 或 permissionless consensus | `p1-p16` |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | paper | 为 permissioned BFT branch 增加 HotStuff-based multi-instance workload-adaptive consensus evidence | permissioned/known-membership；LAN prototype；不代表 permissionless validator economics | `p1-p13` |
| [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] | paper | 为 blockchain consensus 增加 federated PoS source extension：PVSS/FTS、CP/CG/CQ、attack-prevention 和 confirmation-time analysis | not full PoS foundation; simulation/analysis; supplemental proofs not local | `p1-p13` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-20`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: 区块链共识不应直接等同经典 BFT；它是经典故障模型向经济/网络/数据路径的 translation。Stretch-BFT 补充了 permissioned BFT route: BFT safety 可复用，但 workload sensing、实例伸缩和 proposer recovery 是许可链工作负载控制层。

- FedChain delta: blockchain consensus 的 PoS branch 还可以作为 cross-chain transfer 的 security substrate；source-chain confirmation/finality 和 stake distribution 是跨链系统安全的一部分，而不是单纯链内性能指标。

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
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1710-09437v4-casper-friendly-finality-gadget|Casper the Friendly Finality Gadget]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain]] | strengthens permissioned CFT branch with block replication/order split and workload-adaptive relay evidence | 代表 Sources; Source Extensions; relation graph | no | compare with next BFT/adaptive consensus sources |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | strengthens permissioned BFT branch with workload-adaptive multi-instance consensus evidence | 方法族与解决路线; 代表 Sources; Source Extensions; relation graph | no | compare with future HotStuff/Mir-BFT/RCC sources |
| [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] | 新增 federated PoS source extension，说明 PoS consensus security 与 cross-chain transfer/SPV proof 安全耦合。 | 方法族与解决路线; 代表 Sources; 当前综合 | no | route details through [[proof-of-stake-finality|Proof-of-stake finality]] and [[proof-of-stake-finality-to-cross-chain-protocols|Proof-of-stake finality -> cross-chain protocols]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| none | not_applicable | not_applicable | no bridge currently targets this node | review |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-blockchain-consensus | is_a | nahida-knowledge-blockchain-systems | vault/04_Knowledge/blockchain-systems/blockchain-consensus.md; vault/04_Knowledge/blockchain-systems.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | has_child | nahida-knowledge-open-network-bft-governance | vault/04_Knowledge/blockchain-systems/blockchain-consensus.md; vault/04_Knowledge/blockchain-systems/blockchain-consensus/open-network-bft-governance.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | has_child | nahida-knowledge-permissioned-blockchain-consensus | vault/04_Knowledge/blockchain-systems/blockchain-consensus.md; vault/04_Knowledge/blockchain-systems/blockchain-consensus/permissioned-blockchain-consensus.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | has_child | nahida-knowledge-proof-of-stake-finality | vault/04_Knowledge/blockchain-systems/blockchain-consensus.md; vault/04_Knowledge/blockchain-systems/blockchain-consensus/proof-of-stake-finality.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md | vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md | high | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | medium | active_seed |
| nahida-knowledge-blockchain-consensus | evidenced_by | vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md | vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 现代 HotStuff/CometBFT/Narwhal-Tusk/Bullshark 仍缺 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-sraft-scalable-cft | Added SRaft full paper as representative source under permissioned CFT consensus branch. | 1 source note | codex |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 7 source notes; 1 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-stretch-bft | Added Stretch-BFT as representative source under permissioned BFT consensus branch. | 1 source note | codex |
