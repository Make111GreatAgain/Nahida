---
id: "nahida-knowledge-open-network-bft-governance"
title: "Open-network BFT governance"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "open-network-bft-governance"
domain_id: "blockchain-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-consensus"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "open-network-bft-governance"
primary_ontology_path: "blockchain-systems/consensus/open-network-bft-governance"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-open-network-bft-governance"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-consensus"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus/open-network-bft-governance.md"
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-open-network-bft-governance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-open-network-bft-governance"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-open-network-blockchain-governance"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-open-network-blockchain-governance.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-bft-to-open-network-blockchain-governance"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
representative_source_refs:
  - "arxiv:1802.07240"
query_keys:
  - "Open-network BFT governance"
  - "open-network-bft-governance"
  - "Cobalt"
  - "UNL governance"
  - "DABC"
aliases:
  - "Cobalt"
  - "UNL governance"
  - "DABC"
domains:
  - "blockchain-systems"
topics:
  - "open-network-bft-governance"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-20"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
source_refs:
  - "arxiv:1802.07240"
confidence: "medium"
trust_tier: "primary"
---

# Open-network BFT governance

## 定义与范围

- 定义: Open-network BFT governance 研究没有统一全局成员集合时，节点如何基于本地信任视图对治理 amendment 达成安全一致。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `open-network-bft-governance`
- Aliases/query keys: Cobalt, UNL governance, DABC
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `open-network-bft-governance`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

Cobalt 是当前 source seed；它用 UNL、essential subsets、DABC/MVBA 和 local consistency 表达 non-uniform trust。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[blockchain-consensus|blockchain-consensus]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在开放网络中避免全局 quorum 假设，同时让 linked honest nodes 的治理结果保持一致。

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
| UNL and essential subsets | UNL and essential subsets | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| DABC/DRBC | DABC/DRBC | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| local consistency | local consistency | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| separation from fast transaction network | separation from fast transaction network | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-20`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: Cobalt 应作为 BFT 到 open-network governance 的 source extension，不代表所有 federated/open consensus。

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
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-open-network-blockchain-governance|Distributed BFT -> open-network blockchain governance]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/consensus/open-network-bft-governance` | translation, application, tension | Classical BFT agreement/reliable-broadcast reasoning transfers only after adapting quorums to local UNL/essential-subset support; governance Full-Knowledge, transaction-network delegation, randomizing-key CRS, and operator trust configuration are blockchain/open-network-specific. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-open-network-bft-governance | is_a | nahida-knowledge-blockchain-consensus | vault/04_Knowledge/blockchain-systems/blockchain-consensus/open-network-bft-governance.md; vault/04_Knowledge/blockchain-systems/blockchain-consensus.md | medium | active_seed |
| nahida-knowledge-open-network-bft-governance | evidenced_by | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | medium | active_seed |
| nahida-knowledge-open-network-bft-governance | bridges_to | nahida-bridge-distributed-bft-to-open-network-blockchain-governance | vault/05_Bridges/distributed-bft-to-open-network-blockchain-governance.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Stellar SCP、XRPL LCP、federated Byzantine agreement sources 缺。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 2 legacy notes | codex |
