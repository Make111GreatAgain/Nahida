---
id: "nahida-knowledge-mempool-and-networking"
title: "Mempool and networking"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "mempool-and-networking"
domain_id: "blockchain-systems"
direction_id: "mempool-and-networking"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
child_knowledge_refs:
  - "nahida-knowledge-shared-mempool"
ontology_path:
  - "blockchain-systems"
  - "mempool-and-networking"
primary_ontology_path: "blockchain-systems/mempool-and-networking"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-mempool-and-networking"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-systems"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/mempool-and-networking.md"
      - "vault/04_Knowledge/blockchain-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-mempool-and-networking"
    relation: "has_child"
    to: "nahida-knowledge-shared-mempool"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/mempool-and-networking.md"
      - "vault/04_Knowledge/blockchain-systems/mempool-and-networking/shared-mempool.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-mempool-and-networking"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
representative_source_refs:
  - "arxiv:2203.05158"
query_keys:
  - "Mempool and networking"
  - "mempool-and-networking"
  - "mempool"
  - "网络传播"
aliases:
  - "mempool"
  - "网络传播"
domains:
  - "blockchain-systems"
topics:
  - "mempool-and-networking"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
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
  - "arxiv:2203.05158"
confidence: "medium"
trust_tier: "primary"
---

# Mempool and networking

## 定义与范围

- 定义: Mempool and networking 关注交易数据在被排序前如何传播、可用、恢复和抗负载倾斜。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `mempool-and-networking`
- Aliases/query keys: mempool, 网络传播
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `mempool-and-networking`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前主要 source 是 Stratus/shared mempool，它把交易传播从 leader-based BFT ordering core 中分离。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[blockchain-systems|blockchain-systems]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

避免共识 leader 成为大 payload 传播瓶颈，让 consensus 只引用可用交易而不是承担完整数据传播。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[blockchain-systems|blockchain-systems]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[shared-mempool|shared-mempool]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| shared mempool | shared mempool | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| provable availability broadcast | provable availability broadcast | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| proxy/load balancing | proxy/load balancing | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| background recovery | background recovery | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-20`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: 当前是单 source seed，适合作为 shared mempool 问题入口，不足以覆盖完整 P2P networking/mempool 领域。

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
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| none | not_applicable | not_applicable | no bridge currently targets this node | review |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-mempool-and-networking | is_a | nahida-knowledge-blockchain-systems | vault/04_Knowledge/blockchain-systems/mempool-and-networking.md; vault/04_Knowledge/blockchain-systems.md | medium | active_seed |
| nahida-knowledge-mempool-and-networking | has_child | nahida-knowledge-shared-mempool | vault/04_Knowledge/blockchain-systems/mempool-and-networking.md; vault/04_Knowledge/blockchain-systems/mempool-and-networking/shared-mempool.md | medium | active_seed |
| nahida-knowledge-mempool-and-networking | evidenced_by | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Narwhal/Tusk、mempool DoS、gossip/P2P、MEV/mempool policy 缺 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 1 legacy notes | codex |
