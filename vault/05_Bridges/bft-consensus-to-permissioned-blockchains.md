---
id: "nahida-bridge-bft-consensus-to-permissioned-blockchains"
title: "BFT consensus -> permissioned blockchains"
original_title: "BFT consensus -> permissioned blockchains"
file_slug: "bft-consensus-to-permissioned-blockchains"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_domain_method_transfer"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
  - "blockchain-systems/consensus/permissioned-blockchain-consensus"
endpoint_knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-permissioned-blockchain-consensus"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "consensus"
to_direction: "consensus"
from_topic: "byzantine-fault-tolerance"
to_topic: "permissioned-blockchain-consensus"
relation_types:
  - "application"
  - "translation"
  - "implementation_reuse"
  - "tension"
directionality: "from_bft_to_permissioned_blockchain"
relationship_thesis: "BFT quorum and HotStuff-style safety can be reused in permissioned blockchain consensus, but permissioned workloads expose proposer bandwidth, workload fluctuation, sluggish proposer, and recovery-control problems. Stretch-BFT translates BFT into a workload-adaptive multi-instance protocol by combining workload sensing, deterministic Era-level reconfiguration, and failed-instance recovery."
transferability: "medium-high"
non_transfer_boundary: "BFT quorum intersection, QC/highQC and safety reasoning transfer; client identity, consistent-hash transaction assignment, resource-aware proposer selection, trimmed workload reports, and Era-level workload control rely on permissioned/known-membership assumptions and should not be generalized to permissionless chains without new evidence."
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "byzantine-fault-tolerance"
  - "permissioned-blockchain-consensus"
  - "HotStuff"
  - "multi-instance BFT"
  - "workload-adaptive consensus"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
  - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-permissioned-blockchain-consensus"
query_keys:
  - "BFT consensus -> permissioned blockchains"
  - "permissioned BFT consensus"
  - "HotStuff to permissioned blockchain"
  - "Stretch-BFT workload-adaptive BFT"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-stretch-bft"
source_refs:
  - "doi:10.5555/296806.296824"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
confidence: "high"
trust_tier: "primary"
---

# BFT consensus -> permissioned blockchains

## 命名与路径

- Original title: BFT consensus -> permissioned blockchains
- File slug: `bft-consensus-to-permissioned-blockchains`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

`distributed-systems/consensus/byzantine-fault-tolerance` 是故障模型和共识问题族: 参与者可任意偏离协议，系统仍需保持 agreement、safety、SMR 或 finality。`blockchain-systems/consensus/permissioned-blockchain-consensus` 是应用端点: 已知成员或许可环境中的链式 ordering/replication/finality，需要同时处理 block payload、成员身份、资源配置和 workload 波动。

本 bridge 说明 BFT 不是直接“复制粘贴”到许可链。可迁移的是 quorum intersection、QC/highQC、HotStuff-style safety 和 Byzantine recovery 的基本推理；需要重新设计的是 block proposal 数据路径、workload sensing、instance 数量控制、proposer selection 和失败实例恢复。

## 连接命题

- From: `distributed-systems/consensus/byzantine-fault-tolerance`
- To: `blockchain-systems/consensus/permissioned-blockchain-consensus`
- Relation types: application, translation, implementation_reuse, tension
- Directionality: `from_bft_to_permissioned_blockchain`
- Relationship thesis: BFT quorum and HotStuff-style safety can be reused in permissioned blockchain consensus, but permissioned workloads expose proposer bandwidth, workload fluctuation, sluggish proposer, and recovery-control problems. Stretch-BFT translates BFT into a workload-adaptive multi-instance protocol by combining workload sensing, deterministic Era-level reconfiguration, and failed-instance recovery.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | `distributed-systems/consensus/byzantine-fault-tolerance` | source protocol/problem family | PBFT foundation; Stretch-BFT source extension | active_seed |
| [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | `blockchain-systems/consensus/permissioned-blockchain-consensus` | application/adaptation setting | Stretch-BFT and SRaft source extensions | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| BFT quorum and HotStuff-style safety | permissioned blockchain ordering/finality | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] p3-p10 | Safety reasoning transfers, but workload control is not implied by BFT alone. |
| Multi-instance proposer parallelism | high-workload permissioned deployments | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] p1-p6 | More instances help when proposer upload is bottleneck; they can hurt latency under light workload or sluggish proposers. |
| Workload sensing and deterministic reconfiguration | Era-level consensus configuration | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] p4-p6 | Requires permissioned identities, consistent transaction assignment, and agreed reports; public-chain transfer needs new evidence. |
| Failed instance recovery | BFT multi-instance availability | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] p6-p8 | Piggyback/replacement choices depend on whether spare proposers exist under the current workload. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| BFT safety/quorum logic | `distributed-systems/consensus/byzantine-fault-tolerance` | `blockchain-systems/consensus/permissioned-blockchain-consensus` | Use HotStuff-style QC/highQC and `N >= 3f + 1` assumptions for permissioned ordering. | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] | Does not solve proposer bandwidth by itself. |
| Multi-instance workload adaptation | `distributed-systems/consensus/byzantine-fault-tolerance` | `blockchain-systems/consensus/permissioned-blockchain-consensus` | Adjust number of parallel consensus instances by workload/throughput at Era boundary. | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] | Incorrect sensing or too many instances can increase latency or hit download/verify bottleneck. |
| Byzantine report filtering | BFT fault model | permissioned workload sensing | Collect at least `2f+1` reports, trim highest/lowest `f`, compute deterministic estimate. | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] | Assumes reports are committed consistently and transaction assignment limits duplicate counting. |

## 类比、依赖或关系边界

Classical BFT tells us how to preserve agreement under Byzantine participants; it does not decide how many proposers a blockchain should activate, how to estimate incoming workload, or how to route transactions to avoid duplicate reports. Stretch-BFT is useful because it exposes that missing control layer. The bridge should therefore preserve two layers: BFT as fault-model foundation, and permissioned blockchain consensus as workload/resource/application adaptation.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|Practical Byzantine Fault Tolerance]] | BFT/SMR foundation source already present in vault | active_seed |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | source-backed application/translation evidence for permissioned BFT | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/consensus/byzantine-fault-tolerance` | update Bridge Links and relation_edges | active_seed |
| `blockchain-systems/consensus/permissioned-blockchain-consensus` | update Bridge Links and relation_edges | active_seed |

## 查询入口

- BFT consensus -> permissioned blockchains
- permissioned BFT consensus
- HotStuff to permissioned blockchain
- Stretch-BFT workload-adaptive BFT

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: HotStuff, Mir-BFT, RCC, IBFT, Fabric/Quorum BFT, or production permissioned-chain source changes endpoint assumptions or transfer boundary.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | Methods, Source Extensions, Bridge Links, relation graph | Stretch-BFT adds workload-adaptive multi-instance BFT evidence | active_seed |
| [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | CFT/BFT route split, Source Extensions, Bridge Links | Need separate BFT route beside SRaft/CFT route | active_seed |
| [[blockchain-consensus|Blockchain consensus]] | Representative sources and source extension | Surface permissioned BFT branch under blockchain consensus | active_seed |
| [[consensus|Consensus]] | Representative sources and source extension | Surface BFT/multi-instance branch under consensus direction | active_seed |

## 刷新规则

- Last checked: `2026-06-20`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
