---
id: "nahida-knowledge-asynchronous-reliable-broadcast"
title: "Asynchronous reliable broadcast"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "concept"
hierarchy_level: "method"
file_slug: "asynchronous-reliable-broadcast"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-asynchronous-bft-consensus"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-reliable-broadcast"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast"
secondary_ontology_paths:
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination"
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing"
relation_edges:
  - from: "nahida-knowledge-asynchronous-reliable-broadcast"
    relation: "is_a_method_for"
    to: "nahida-knowledge-asynchronous-bft-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-reliable-broadcast"
    relation: "depends_on"
    to: "nahida-knowledge-asynchronous-data-dissemination"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-reliable-broadcast"
    relation: "supports"
    to: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-reliable-broadcast"
    relation: "supports"
    to: "nahida-knowledge-dual-threshold-asynchronous-vss"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-reliable-broadcast"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-reliable-broadcast"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md"
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
  - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
  - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
  - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
representative_source_refs:
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "arxiv:1802.07240"
query_keys:
  - "Asynchronous reliable broadcast"
  - "asynchronous-reliable-broadcast"
  - "RBC"
  - "Bracha reliable broadcast"
  - "long-message RBC"
  - "AVID reliable broadcast"
  - "ADD-based RBC"
  - "reliable broadcast in asynchronous BFT"
  - "RBC totality for AVSS"
  - "reliable broadcast for VSS transcripts"
aliases:
  - "RBC"
  - "reliable broadcast"
  - "Bracha RBC"
  - "long-message RBC"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "asynchronous-bft-consensus"
  - "asynchronous-reliable-broadcast"
  - "asynchronous-data-dissemination"
  - "asynchronous-verifiable-secret-sharing"
tags:
  - "nahida/knowledge"
  - "nahida/concept"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
  - "nahida-knowledge-20260623-verifiable-secret-sharing-simplified"
source_refs:
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "arxiv:1802.07240"
confidence: "medium"
trust_tier: "primary"
---

# Asynchronous reliable broadcast

## 定义与范围

- 定义: Asynchronous reliable broadcast (RBC) 是异步 Byzantine 网络中的 broadcast primitive；它要求 honest nodes 对同一 broadcaster 的消息满足 agreement、validity/totality 等可靠交付性质，即使 broadcaster 或部分 receivers 是 Byzantine。
- 不包含: 单篇 Bracha 论文全文、某个 ACS 协议、完整 consensus protocol、mempool 或 data availability scheme；这些分别留在 source notes 或上层节点。
- Canonical terms: `asynchronous-reliable-broadcast`, `RBC`
- Aliases/query keys: reliable broadcast, Bracha RBC, long-message RBC, AVID, ADD-based RBC
- Standalone completeness check: 本节点给出本地定义、问题、路线、代表 source、边界和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 RBC、Bracha broadcast、long-message broadcast、AVID/HoneyBadger/ACS 关系时先到本节点。
- Update scope: 新 source 若改变 RBC properties、Bracha lineage、long-message cost、AVID/Merkle route 或 ACS/AVSS usage，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

异步共识不能假定一个 honest receiver 看到的 broadcaster 消息会被其他 honest receivers 同步看到。RBC 把“某个 broadcaster 的消息是否可靠交付”从后续 agreement 中抽出，使上层 ACS、atomic broadcast、AVSS 和 asynchronous blockchain consensus 可以基于已可靠传播的 proposals 或 shares 继续运行。

当前 vault 中 RBC 已出现在 EPIC 的 ACS workflow、Cobalt 的 DRBC/open-network adaptation、Flexible Advancement 的 ARBC 以及 AVSS/ADKG 缺口里。VSS Simplified 2023/1196 又明确把 RBC totality 用作 A-VSS transcript 的异步终止条件: 一旦某个 honest node 输出 sharing transcript，其他 honest nodes 也会最终输出。本节点先建立 thin but source-backed 索引，把这些散落引用收敛到一个可检索的 method 节点。

## 基础概念判断

- 是否是基础概念/方向/问题: `concept` / `method`。
- 为什么足够通用: RBC 是多个 async BFT、AVSS、ACS、atomic broadcast 和 open-network governance source 共同复用的通信 primitive。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 2021/777 提供 long-message RBC route；EPIC 和 Cobalt 作为已读 source 显示 RBC 在不同协议栈中的复用。
- 需要引用的更基础 Knowledge: [[asynchronous-bft-consensus|asynchronous-bft-consensus]], [[asynchronous-data-dissemination|asynchronous-data-dissemination]]。
- 不应拆出的实例/协议/来源: Bracha RBC、AVID、DRBC、ARBC 先作为方法路线或子候选；direct source 到齐后再决定是否拆子节点。

## 解决的问题

RBC 解决的是: 在 broadcaster 可能 Byzantine、网络完全异步的情况下，如何保证 honest nodes 对某个 broadcast instance 的交付不会分裂。对长消息场景，额外问题是如何避免让大 payload 在所有边上重复传输。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | method_for | RBC is used by ACS, async atomic broadcast, AVSS and blockchain-oriented async BFT sources | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Bracha reliable broadcast | primitive candidate | Classic INIT/ECHO/READY RBC is the baseline source many notes reference | current notes only reference via secondary sources | queued |
| AVID / erasure-coded reliable broadcast | method candidate | Merkle/erasure-coded RBC is the comparison point for ADD-based long-message RBC | ADD 2021/777 related work; EPIC implementation mention | queued |
| democratic reliable broadcast | method candidate | Cobalt adapts RBC to open-network essential subsets and support/opposition | [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt]] | hold |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Bracha-style RBC | broadcaster sends INIT; receivers propagate ECHO/READY until quorum conditions force agreement and totality | asynchronous BFT, typically `t<n/3` | Classic direct source not yet absorbed; long messages naively cost `O(n^2 |M|)` | queued foundation |
| ADD-backed long-message RBC | RBC broadcasts a hash, while ADD disseminates payload from honest holders | long messages, collision-resistant hash, `t<n/3` main ADD | `O(n|M|+kappa n^2)`; removes `log n` vs prior AVID-style route | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| RBC totality for AVSS transcripts | Dealer transcript is delivered through reliable broadcast so one honest output implies eventual output by all honest nodes | asynchronous VSS/dual-threshold VSS with `n>=3t+1` | RBC is a dependency; VSS secrecy/public verifiability comes from commitments, signatures and VE | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] |
| ACS use of RBC | Each node RBC-broadcasts a proposal, then ABA instances decide which delivered proposals enter common subset | async BFT SMR and blockchain consensus | RBC handles proposal availability, ABA handles inclusion agreement | [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC]] |
| Open-network DRBC | Adds support/opposition and essential-subset quorum notions to reliable broadcast | non-uniform trust/open membership model | Not directly transferable to symmetric `n,t` BFT without trust-model translation | [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | paper | 给出 ADD-backed long-message RBC，成本 `O(n|M|+kappa n^2)`，并说明其对 async atomic broadcast、AVSS、ACSS、ADKG 的传播效应 | Uses collision-resistant hash for RBC; Bracha source still not direct | §4, Theorem 4.7 |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | paper | 展示 RBC totality 如何支撑 A-VSS 和 dual-threshold A-VSS transcript 终止 | Uses RBC as black box; not a foundational RBC paper | Algorithm 2, Algorithm 3, Theorems 2-3 |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | paper | 作为 async BFT/ACS 系统 source，展示 RBC + ABA 的 epoch workflow | Uses RBC as component; not a foundational RBC paper | §IV-§V |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | paper | 展示 Bracha-style RBC 在 open-network/non-uniform trust 中的 DRBC adaptation | Trust model differs from classical symmetric BFT | §4.2 |

## 正反例约束

- 正确: 把 RBC 作为 async BFT 的 broadcast primitive，解释它如何支撑 ACS、AVSS、ACSS 和 atomic broadcast。
- 正确: 把 ADD-backed RBC 记录为 long-message route，而不是替代所有 RBC lineage。
- 错误: 把 RBC 和共识/atomic broadcast 画等号；RBC 只处理单 broadcaster 的可靠交付。
- 错误: 把 Cobalt DRBC 的 non-uniform trust quorum 直接迁移到 classical `n=3f+1` BFT。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: RBC 是 async BFT 栈中比 consensus 更低一层的 reliable propagation primitive。当前 vault 已有多处使用证据，但 classic foundation 仍薄；2021/777 首先把 long-message RBC 的 payload 成本通过 ADD 降下来，EPIC 显示 RBC 在 ACS/区块链 BFT 工作流中承载 proposal availability，Cobalt 显示 RBC 可被改造成 open-network DRBC，VSS Simplified 2023/1196 显示 RBC totality 是 A-VSS transcript 终止的直接载体。后续需要 Bracha RBC、AVID/HoneyBadger 直接 source 来把本节点从 active seed 提升为 foundation。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: no implementation evidence in current source.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new Bracha, AVID, HoneyBadger, BEAT, ACS, ARBC/DRBC or long-message broadcast source.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | 新建 RBC method/concept 节点；补入 ADD-backed long-message RBC | 定义; 方法族; 代表 Sources; 当前综合 | yes, child/method under async BFT | 后续补 Bracha RBC and AVID direct sources |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | 补入 RBC totality for AVSS transcript termination | 背景; 方法族; 代表 Sources; 当前综合 | no | keep as dependency evidence |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | 作为 ACS workflow 中 RBC usage evidence | 背景; 方法族; 代表 Sources | no | keep linked |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | 作为 DRBC/open-network adaptation evidence | 背景; 方法族; 代表 Sources | no | keep linked |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | `distributed-systems/consensus/asynchronous-bft-consensus` | dependency, broadcast_transfer | RBC transfers as reliable proposal/payload propagation primitive; it does not specify transaction selection, data availability sampling, validator governance or execution. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-asynchronous-reliable-broadcast | is_a_method_for | nahida-knowledge-asynchronous-bft-consensus | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md | high | active_seed |
| nahida-knowledge-asynchronous-reliable-broadcast | depends_on | nahida-knowledge-asynchronous-data-dissemination | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination.md | high | active_seed |
| nahida-knowledge-asynchronous-reliable-broadcast | supports | nahida-knowledge-asynchronous-verifiable-secret-sharing | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md | high | active_seed |
| nahida-knowledge-asynchronous-reliable-broadcast | supports | nahida-knowledge-dual-threshold-asynchronous-vss | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss.md | high | active_seed |
| nahida-knowledge-asynchronous-reliable-broadcast | evidenced_by | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | high | active_seed |
| nahida-knowledge-asynchronous-reliable-broadcast | bridges_to | nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus | vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md; vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Bracha RBC direct source 尚缺。 | 本节点现在有 long-message RBC 和 usage evidence，但 classic RBC foundation 仍需原始来源。 | nahida-research-search or nahida-update | high | queued |
| AVID/HoneyBadger/BEAT direct sources 尚缺。 | 需要校准 ADD-backed RBC 与 erasure-coded/Merkle RBC 在 async BFT systems 中的关系。 | nahida-update | high | queued |
| ARBC/DRBC 是否拆独立节点待定。 | Flexible Advancement 和 Cobalt 分别使用 abortable/open-network broadcast variants；多源到齐后再拆。 | nahida-consolidate after more sources | medium | hold |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-asynchronous-data-dissemination | Created asynchronous reliable broadcast method node with ADD-backed long-message RBC and existing EPIC/Cobalt usage evidence. | iacr:2021/777; EPIC; Cobalt | codex |
| 2026-06-23 | nahida-knowledge-20260623-verifiable-secret-sharing-simplified | Added RBC totality as the termination carrier for publicly verifiable and dual-threshold A-VSS transcripts. | iacr:2023/1196 | codex |
