---
id: "nahida-knowledge-delegated-computation"
title: "Delegated computation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "delegated-computation"
domain_id: "verifiable-computation"
direction_id: "interactive-proofs"
parent_knowledge_refs:
  - "nahida-knowledge-interactive-proofs"
child_knowledge_refs: []
ontology_path:
  - "verifiable-computation"
  - "interactive-proofs"
  - "delegated-computation"
primary_ontology_path: "verifiable-computation/interactive-proofs/delegated-computation"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-delegated-computation"
    relation: "is_a"
    to: "nahida-knowledge-interactive-proofs"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/delegated-computation.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-delegated-computation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-delegated-computation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-delegated-computation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/gkr-protocols.md"
    confidence: "high"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
  - "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
  - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
representative_source_refs:
  - "doi:10.1145/1374376.1374396"
  - "doi:10.1109/SP.2015.23"
  - "arxiv:1304.3812v4"
query_keys:
  - "Delegated computation"
  - "delegated-computation"
  - "computation delegation"
  - "GKR protocol"
  - "time-optimal GKR"
  - "delegated circuit evaluation"
aliases:
  - "computation delegation"
  - "GKR protocol"
domains:
  - "verifiable-computation"
topics:
  - "delegated-computation"
  - "gkr-protocols"
  - "time-optimal-gkr"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260623-time-optimal-interactive-proofs"
source_refs:
  - "doi:10.1145/1374376.1374396"
  - "doi:10.1109/SP.2015.23"
  - "arxiv:1304.3812v4"
confidence: "medium"
trust_tier: "primary"
---

# Delegated computation

## 定义与范围

- 定义: Delegated computation 让弱 verifier 把计算交给强 prover，然后用低成本协议检查结果。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `delegated-computation`
- Aliases/query keys: computation delegation, GKR protocol
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `delegated-computation`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

Interactive Proofs for Muggles 是当前 source seed；它通过 circuit layering、multilinear extensions、sum-check/GKR 思路解释 delegated computation。Thaler time-optimal source 补充了一个直接实践化增量：在 regular circuit families 上，GKR-style delegated circuit evaluation 的 prover overhead 可以从 `O(S log S)` 降到 `O(S)`。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[interactive-proofs|interactive-proofs]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

降低 verifier 直接重算成本，同时保持对外包计算结果的可验证性。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[interactive-proofs|interactive-proofs]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| circuit layering | circuit layering | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| multilinear extension | multilinear extension | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| sum-check based verification | sum-check based verification | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| GKR-style protocols | GKR-style protocols | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Time-optimal GKR for delegated circuit evaluation | 对 regular layered circuits 复用 sum-check rounds 的计算，让 prover 接近直接求值成本，同时 verifier 保持低成本和 streaming-friendly。 | 电路 wiring 足够 regular；data-parallel super-circuit 具有重复结构。 | 不覆盖任意 irregular circuits；matrix multiplication 专用协议留在 source/GKR 节点。 | [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles|Delegating Computation: Interactive Proofs for Muggles]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto: Versatile Verifiable Computation]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | paper | 补充 delegated circuit evaluation 的 prover-cost 改进路线和 data-parallel batching route | 需要 regularity/data-parallel assumptions；不是通用 VC compiler | `p1-p50`, `Theorem 1-3` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: Delegated computation 是 interactive proofs 与 VC systems 的桥接问题。Thaler 2017 把该问题的一个瓶颈明确化: 即使 verifier 很便宜，prover 若比直接计算多 `log S` 因子也会限制实践。该 source 不改变 delegated computation 的定义，但给 [[gkr-protocols|GKR-style interactive proofs]] 增加了“prover overhead engineering”这条可复用解决路线。

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
| [[doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles|Delegating Computation: Interactive Proofs for Muggles]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto: Versatile Verifiable Computation]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | source extension | regular-circuit/data-parallel GKR improves prover overhead for delegated circuit evaluation | 方法族与解决路线; 当前综合; 关系图谱 | no | keep full method details in [[gkr-protocols|GKR-style interactive proofs]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| none | not_applicable | not_applicable | no bridge currently targets this node | review |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-delegated-computation | is_a | nahida-knowledge-interactive-proofs | vault/04_Knowledge/verifiable-computation/interactive-proofs/delegated-computation.md; vault/04_Knowledge/verifiable-computation/interactive-proofs.md | medium | active_seed |
| nahida-knowledge-delegated-computation | evidenced_by | vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md | vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md | medium | active_seed |
| nahida-knowledge-delegated-computation | evidenced_by | vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md | vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md | medium | active_seed |
| nahida-knowledge-delegated-computation | evidenced_by | vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md | Thaler 2017 source note p1-p50 | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Pepper/Pinocchio/modern VC implementations 与更多 GKR/IOP variants 缺 source。 | 影响本节点工程路线与 foundation 完整性；当前已覆盖 GKR seed 与 time-optimal GKR，但不是完整 VC landscape。 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 2 source notes; 3 legacy notes | codex |
| 2026-06-23 | nahida-knowledge-20260623-time-optimal-interactive-proofs | Added Thaler time-optimal GKR as a delegated computation source extension and routed detailed method content to the GKR method-family node. | 1 source note | codex |
