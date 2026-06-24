---
id: "nahida-knowledge-verifiable-computation"
title: "Verifiable computation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "domain"
hierarchy_level: "domain"
file_slug: "verifiable-computation"
domain_id: "verifiable-computation"
direction_id: ""
parent_knowledge_refs:
  []
child_knowledge_refs:
  - "nahida-knowledge-interactive-proofs"
  - "nahida-knowledge-verifiable-computation-research-dynamics"
  - "nahida-knowledge-verifiable-computation-systems"
ontology_path:
  - "verifiable-computation"
primary_ontology_path: "verifiable-computation"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-verifiable-computation"
    relation: "has_child"
    to: "nahida-knowledge-interactive-proofs"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation"
    relation: "has_child"
    to: "nahida-knowledge-verifiable-computation-research-dynamics"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation.md"
      - "vault/04_Knowledge/verifiable-computation/research-dynamics.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation"
    relation: "has_child"
    to: "nahida-knowledge-verifiable-computation-systems"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation.md"
      - "vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation"
    relation: "bridges_to"
    to: "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
    evidence_refs:
      - "vault/05_Bridges/sum-check-protocol-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/gkr-protocols.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
  - "vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md"
  - "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
  - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
representative_source_refs:
  - "doi:10.1145/1374376.1374396"
  - "sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd"
  - "doi:10.1109/SP.2015.23"
  - "doi:10.1145/3658644.3690318"
  - "arxiv:1304.3812v4"
query_keys:
  - "Verifiable computation"
  - "verifiable-computation"
  - "可验证计算"
  - "sum-check to memory-efficient SNARKs"
  - "space-efficient sumcheck"
  - "time-optimal GKR"
  - "verifiable circuit evaluation"
aliases:
  - "可验证计算"
domains:
  - "verifiable-computation"
topics:
  - "sum-check-protocol"
  - "memory-efficient-snarks"
  - "gkr-protocols"
  - "time-optimal-gkr"
tags:
  - "nahida/knowledge"
  - "nahida/domain"
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
  - "nahida-knowledge-20260620-sparrow-space-efficient-snarks"
  - "nahida-knowledge-20260623-time-optimal-interactive-proofs"
source_refs:
  - "doi:10.1145/1374376.1374396"
  - "sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd"
  - "doi:10.1109/SP.2015.23"
  - "doi:10.1145/3658644.3690318"
  - "arxiv:1304.3812v4"
confidence: "medium"
trust_tier: "primary"
---

# Verifiable computation

## 定义与范围

- 定义: Verifiable computation 关注把计算委托给外部 prover/worker 后，verifier 如何低成本检查结果正确性。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `verifiable-computation`
- Aliases/query keys: 可验证计算
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `verifiable-computation`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: [[04_Knowledge/verifiable-computation/research-dynamics|Research dynamics]]

## 背景

当前 evidence seed 来自 Sum-check Protocol、Interactive Proofs for Muggles、Geppetto 与 Thaler time-optimal GKR；它和 ZKP proof systems 共享 sum-check、polynomial commitments、QAP 等机制。Sparrow 作为 secondary evidence 说明 sum-check/GKR 可被迁移到低内存 SNARK 构造，但主归属仍在 ZKP proof systems。Thaler 2017 则把 GKR 的 prover overhead 问题纳入可验证计算域内的直接方法族。

## 基础概念判断

- 是否是基础概念/方向/问题: `domain` / `domain`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: root domain。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

降低验证复杂度，让弱 verifier 能检查复杂计算，同时区分 interactive proof、SNARK、QAP-based system 等路线。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| root | L1 domain/root | canonical current architecture | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[interactive-proofs|interactive-proofs]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[verifiable-computation-systems|verifiable-computation-systems]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| interactive proofs and sum-check | interactive proofs and sum-check | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| GKR/delegated computation | 用 layered circuit、multilinear extensions 和 sum-check 做低成本验证；time-optimal route 进一步压低 regular circuits 的 prover overhead。 | Delegated circuit evaluation, regular/data-parallel computation, and proof-system components that can reuse GKR-style checks. | Arbitrary irregular circuits、compiler automation、SNARK non-interactivity 仍需其他组件或来源。 | [[gkr-protocols|GKR-style interactive proofs]]; [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] |
| QAP-based verifiable computation systems | QAP-based verifiable computation systems | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Sum-check/GKR to low-memory SNARKs | 将 product-form sumcheck 和 GKR-style layer checks 特化为 streaming/low-buffer prover route，再通过 commitments 与 Fiat-Shamir 进入 SNARK 系统。 | Layered data-parallel circuits and prover-memory bottleneck. | Sum-check 本身不是 SNARK；电路结构与 commitment backend 限制很强。 | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]]; [[sum-check-protocol-to-memory-efficient-snarks|bridge]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles|Delegating Computation: Interactive Proofs for Muggles]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-dfbe6c185c1b-sum-check-protocol|The Sum-Check Protocol]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto: Versatile Verifiable Computation]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | paper | 作为 secondary source extension，展示 sum-check/GKR 如何迁移为 low-memory SNARK building block | primary path is ZKP/proof-systems; not a full VC foundation source | `p1-p15` |
| [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | paper | 作为 direct VC source extension，展示 GKR-style circuit evaluation 的 prover overhead 可在 regular circuits 上降到 `O(S)` | regular/data-parallel assumptions; not a universal VC compiler | `p1-p50`, `Theorem 1-3` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前覆盖 delegated computation、sum-check、GKR-style interactive proofs 和 QAP-based VC systems；Sparrow 新增一条 secondary bridge，说明 sum-check/GKR 在 ZKP proof-system engineering 中可作为低内存 SNARK 构件。Thaler 2017 新增 direct VC evidence，说明 GKR 在 regular/data-parallel circuit evaluation 中可以把 prover overhead 降到接近直接计算。该更新让 [[gkr-protocols|GKR-style interactive proofs]] 成为 VC 域内的明确方法族节点；仍缺 PCP、IOP、SNARK 编译链、modern VC systems 的完整来源。

## 领域态势

- Research dynamics note: [[04_Knowledge/verifiable-computation/research-dynamics|Research dynamics]]
- Dynamics freshness: stale/queued because no daily-fetch evidence exists
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles|Delegating Computation: Interactive Proofs for Muggles]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-dfbe6c185c1b-sum-check-protocol|The Sum-Check Protocol]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto: Versatile Verifiable Computation]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | secondary source extension | sum-check/GKR transfer into memory-efficient SNARKs | 方法族与解决路线; Bridge Links; 关系图谱 | no | keep primary details in [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | direct source extension | time-optimal GKR for verifiable circuit evaluation and data-parallel computation | 方法族与解决路线; 代表 Sources; 当前综合; 关系图谱 | yes | keep details in [[gkr-protocols|GKR-style interactive proofs]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[sum-check-protocol-to-memory-efficient-snarks|Sum-check protocol -> memory-efficient SNARKs]] | `verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | dependency, method_transfer, prover_space_reduction | Sum-check/GKR ideas transfer into low-memory SNARK construction, but sumcheck alone is not a SNARK and does not provide commitments/non-interactivity. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-verifiable-computation | has_child | nahida-knowledge-interactive-proofs | vault/04_Knowledge/verifiable-computation.md; vault/04_Knowledge/verifiable-computation/interactive-proofs.md | medium | active_seed |
| nahida-knowledge-verifiable-computation | has_child | nahida-knowledge-verifiable-computation-research-dynamics | vault/04_Knowledge/verifiable-computation.md; vault/04_Knowledge/verifiable-computation/research-dynamics.md | medium | active_seed |
| nahida-knowledge-verifiable-computation | has_child | nahida-knowledge-verifiable-computation-systems | vault/04_Knowledge/verifiable-computation.md; vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md | medium | active_seed |
| nahida-knowledge-verifiable-computation | evidenced_by | vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md | vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md | medium | active_seed |
| nahida-knowledge-verifiable-computation | evidenced_by | vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md | vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md | medium | active_seed |
| nahida-knowledge-verifiable-computation | evidenced_by | vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md | vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md | medium | active_seed |
| nahida-knowledge-verifiable-computation | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md | secondary source note | medium | active_seed |
| nahida-knowledge-verifiable-computation | bridges_to | nahida-bridge-sum-check-protocol-to-memory-efficient-snarks | bridge note | high | active_seed |
| nahida-knowledge-verifiable-computation | evidenced_by | vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md | Thaler 2017 source note p1-p50 | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| PCP/IOP foundations、SNARK 编译器、modern VC/zkVM 实现仍缺。 | 影响本节点 foundation 完整性；GKR 已有 seed 与 time-optimal source，但 VC 域还不完整。 | nahida-research-search or nahida-update | medium | queued |
| Space-efficient/time-optimal GKR / sumcheck comparison sources 仍缺。 | Sparrow 和 Thaler 提供两条路线，但 GKR/IOP/streaming foundations 仍需独立来源校准。 | nahida-update / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 3 source notes; 1 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-sparrow-space-efficient-snarks | Added secondary bridge from sum-check/GKR to memory-efficient SNARKs. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-time-optimal-interactive-proofs | Added direct VC source extension for time-optimal GKR and created the GKR method-family child node. | 1 source note | codex |
