---
id: "nahida-knowledge-scaling-and-sharding"
title: "Scaling and sharding"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "scaling-and-sharding"
domain_id: "blockchain-systems"
direction_id: "scaling-and-sharding"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
child_knowledge_refs:
  - "nahida-knowledge-sharded-ledgers"
ontology_path:
  - "blockchain-systems"
  - "scaling-and-sharding"
primary_ontology_path: "blockchain-systems/scaling-and-sharding"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-scaling-and-sharding"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-systems"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md"
      - "vault/04_Knowledge/blockchain-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-scaling-and-sharding"
    relation: "has_child"
    to: "nahida-knowledge-sharded-ledgers"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md"
      - "vault/04_Knowledge/blockchain-systems/scaling-and-sharding/sharded-ledgers.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-scaling-and-sharding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-scaling-and-sharding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-scaling-and-sharding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-scaling-and-sharding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-scaling-and-sharding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-scaling-and-sharding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    confidence: "medium"
    status: "supporting_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
  - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
representative_source_refs:
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1804.00399v4"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
  - "doi:10.14778/3574245.3574278"
query_keys:
  - "Scaling and sharding"
  - "scaling-and-sharding"
  - "sharding"
  - "区块链扩容"
  - "smart contract sharding"
  - "LightCross"
  - "layer-2 blockchain scaling"
  - "L2chain"
aliases:
  - "sharding"
  - "区块链扩容"
domains:
  - "blockchain-systems"
topics:
  - "scaling-and-sharding"
  - "cross-shard-transaction-execution"
  - "smart-contract-sharding"
  - "layer-2-scaling"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-21"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260621-ahl-sharding"
  - "nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts"
  - "nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution"
source_refs:
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1804.00399v4"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
  - "doi:10.14778/3574245.3574278"
confidence: "medium"
trust_tier: "primary"
---

# Scaling and sharding

## 定义与范围

- 定义: Scaling and sharding 研究如何让区块链通过分片、跨片事务、委员会和状态分区扩展吞吐。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `scaling-and-sharding`
- Aliases/query keys: sharding, 区块链扩容
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `scaling-and-sharding`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source 覆盖 OmniLedger、ByShard、RingBFT、AHL、LightCross 和 L2chain，重点是 sharded ledgers、Byzantine cross-shard transaction processing、TEE-assisted shard-level BFT、secure shard formation、general-workload transaction coordination、smart-contract cross-shard execution 的 TEE executor/R-shard/contract migration 路线，以及 L2 DApp execution 的 state-digest split/merge 扩容路线。L2chain 是 layer-2 scaling supporting seed，不改变 [[sharded-ledgers|sharded-ledgers]] 子节点。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[blockchain-systems|blockchain-systems]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在不让所有节点处理所有交易的情况下维持安全、原子性、隔离和可恢复性。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[blockchain-systems|blockchain-systems]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[sharded-ledgers|sharded-ledgers]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| validator sharding and shard-level BFT | validator sharding and shard-level BFT | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Atomix/cross-shard atomic commit | Atomix/cross-shard atomic commit | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| ByShard OEM and 2PC/2PL | ByShard OEM and 2PC/2PL | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Ring topology cross-shard consensus | Ring topology cross-shard consensus | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| TEE-assisted general-workload sharding | 用 AHL+ 提升 shard-level BFT fault scalability，用 TEE beacon 组片，并用 BFT reference committee + 2PC/2PL 处理非 UTXO 跨片事务。 | permissioned blockchain、每节点具备 TEE、adaptive corruption 非瞬时、无 DoS。 | TEE 信任假设重；SGX 评估为 simulation + latency injection；reference committee 可能成为瓶颈。 | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] |
| TEE-assisted smart-contract cross-shard execution | 将复杂 CSTx 交给 TEE executor，R-shard 排序 certified results，S-shards 只验证 stale reads 并提交 write sets；同时用合约迁移降低 CSTx ratio。 | permissioned smart-contract sharding; FISCO-BCOS-like setting; TEE accepted. | R-shard/executor availability and TEE trust become boundaries; migration assumes workload locality. | [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] |
| Layer-2 DApp split-execute-merge | 将 DApp 批处理放到 L2 排序/TEE 执行，L1 只维护可用状态摘要并验证 split/merge 事务。 | DApp 可通过 on-chain SLA 定义权限/代码/共识验证，状态可用 accumulator digest 承诺。 | 不是 validator sharding；依赖 TEE、RSA accumulator witness cache 和 L1 split/merge latency；不覆盖 DA/fraud/validity proof。 | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT: Resilient Consensus over Sharded Ring Topology]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | 补入 permissioned/general-workload sharding route：AHL+、TEE random beacon、batch reconfiguration、BFT reference committee + 2PC/2PL | 依赖 TEE；不覆盖 permissionless incentives；reference committee scaling 未完整解决 | Abstract, §3-§7 |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts]] | paper | 补入 smart-contract sharding route：TEE executor、R-shard batch validation、authenticated state reads、contract migration 降低 CSTx ratio | TEE/R-shard/executor assumptions; permissioned prototype; workload-dependent migration | §III-§V, Appendix |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications]] | paper | 补入 layer-2 scaling supporting route：DApp 在 L2 处理交易，L1 只 split/merge state digest。 | 不是 sharding source；依赖 TEE 和 accumulator state commitment；不覆盖完整 rollup/DA/security taxonomy | p1-p14 |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-21`。
- 综合: 当前可回答 sharded ledger seed 问题，并能区分 UTXO/payment-ledger sharding、Byzantine distributed transaction sharding、ring-topology cross-shard consensus、AHL 的 permissioned/general-workload TEE-assisted sharding，以及 LightCross 的 smart-contract CSTx execution route。L2chain 作为 supporting seed 显示另一类 layer-2 DApp execution 扩容路线：不分片 validator，而是让 L1 维护 state digest 并让 DApps 在 L2 split-execute-merge。当前仍不能覆盖 rollups、modular execution、parallel execution 或 full scaling landscape。

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
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | 增加 permissioned/general-workload sharding source extension：AHL+ 提升 shard-level BFT，TEE beacon 降低组片成本，BFT reference committee 将 2PC/2PL 用于非 UTXO 跨片事务。 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 后续比较 Chainspace、TEE-assisted BFT foundations 和 distributed transaction foundations |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] | 增加 smart-contract sharding source extension：TEE executor + R-shard batch validation + smart contract migration。 | 背景; 方法族与解决路线; 代表 Sources; 当前综合 | yes, promotes cross-shard execution child under execution direction | 后续比较 OptChain/Chainspace/CAPER/SharPer |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | 增加 layer-2 DApp execution supporting route：L1 state digest split/merge + L2 TEE execution。 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; 关系图谱 | no, supporting seed only | 后续吸收 rollup/L2 architecture、DA/fraud/validity proof source 后决定是否拆 layer-2 scaling child |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| none | not_applicable | not_applicable | no bridge currently targets this node | review |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-scaling-and-sharding | is_a | nahida-knowledge-blockchain-systems | vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md; vault/04_Knowledge/blockchain-systems.md | medium | active_seed |
| nahida-knowledge-scaling-and-sharding | has_child | nahida-knowledge-sharded-ledgers | vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md; vault/04_Knowledge/blockchain-systems/scaling-and-sharding/sharded-ledgers.md | medium | active_seed |
| nahida-knowledge-scaling-and-sharding | evidenced_by | vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md | vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md | medium | active_seed |
| nahida-knowledge-scaling-and-sharding | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | medium | active_seed |
| nahida-knowledge-scaling-and-sharding | evidenced_by | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | medium | active_seed |
| nahida-knowledge-scaling-and-sharding | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | high | active_seed |
| nahida-knowledge-scaling-and-sharding | evidenced_by | vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md | LightCross source note | high | active_seed |
| nahida-knowledge-scaling-and-sharding | evidenced_by | vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md | L2chain source note | medium | supporting_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| rollups、Danksharding、parallel execution、modern sharding practice 缺 source。 | 影响本节点 foundation 完整性；L2chain 只提供 layer-2 DApp execution supporting seed，不足以覆盖 rollup/L2 taxonomy。 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 3 source notes; 1 legacy notes | codex |
| 2026-06-21 | nahida-knowledge-20260621-ahl-sharding | Added AHL as permissioned/general-workload sharding source extension with TEE-assisted BFT, shard formation and BFT reference-committee transaction coordination. | arxiv:1804.00399v4 | codex |
| 2026-06-22 | nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts | Added LightCross as smart-contract sharding route with TEE executor, R-shard validation and contract migration. | sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2 | codex |
| 2026-06-23 | nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution | Added L2chain as supporting layer-2 DApp split-execute-merge scaling route without promoting a sharding child. | doi:10.14778/3574245.3574278 | codex |
