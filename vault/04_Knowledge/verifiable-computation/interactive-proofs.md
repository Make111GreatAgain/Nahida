---
id: "nahida-knowledge-interactive-proofs"
title: "Interactive proofs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "interactive-proofs"
domain_id: "verifiable-computation"
direction_id: "interactive-proofs"
parent_knowledge_refs:
  - "nahida-knowledge-verifiable-computation"
child_knowledge_refs:
  - "nahida-knowledge-delegated-computation"
  - "nahida-knowledge-sum-check-protocol"
  - "nahida-knowledge-gkr-protocols"
ontology_path:
  - "verifiable-computation"
  - "interactive-proofs"
primary_ontology_path: "verifiable-computation/interactive-proofs"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-interactive-proofs"
    relation: "is_a"
    to: "nahida-knowledge-verifiable-computation"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs.md"
      - "vault/04_Knowledge/verifiable-computation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "has_child"
    to: "nahida-knowledge-delegated-computation"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/delegated-computation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "has_child"
    to: "nahida-knowledge-sum-check-protocol"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/sum-check-protocol.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "has_child"
    to: "nahida-knowledge-gkr-protocols"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/gkr-protocols.md"
      - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "bridges_to"
    to: "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
    evidence_refs:
      - "vault/05_Bridges/sum-check-protocol-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "bridges_to"
    to: "nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition"
    evidence_refs:
      - "vault/05_Bridges/public-coin-interactive-proofs-to-recursive-proof-composition.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-interactive-proofs"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/gkr-protocols.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
  - "nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
  - "vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
  - "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
  - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
representative_source_refs:
  - "doi:10.1145/1374376.1374396"
  - "sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd"
  - "doi:10.1145/3658644.3690318"
  - "iacr:2022/1072"
  - "sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
  - "arxiv:1304.3812v4"
query_keys:
  - "Interactive proofs"
  - "interactive-proofs"
  - "交互式证明"
  - "space-efficient sumcheck"
  - "GKR to SNARK"
  - "public-coin proof recursion"
  - "GKR inside SNARK"
  - "one-round public-coin argument"
  - "GKR-style interactive proofs"
  - "time-optimal GKR"
  - "verifiable circuit evaluation"
aliases:
  - "交互式证明"
domains:
  - "verifiable-computation"
topics:
  - "interactive-proofs"
  - "sum-check-protocol"
  - "memory-efficient-snarks"
  - "public-coin-proof-recursion"
  - "GKR"
  - "gkr-protocols"
  - "time-optimal-gkr"
  - "hash-verification"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-sparrow-space-efficient-snarks"
  - "nahida-knowledge-20260622-public-coin-proof-recursion"
  - "nahida-knowledge-20260623-time-optimal-interactive-proofs"
source_refs:
  - "doi:10.1145/1374376.1374396"
  - "sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd"
  - "doi:10.1145/3658644.3690318"
  - "iacr:2022/1072"
  - "sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
  - "arxiv:1304.3812v4"
confidence: "medium"
trust_tier: "primary"
---

# Interactive proofs

## 定义与范围

- 定义: Interactive proofs 让 prover 和 verifier 通过多轮交互证明计算或陈述正确性，是 delegated computation 和后续 proof systems 的基础路线。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `interactive-proofs`
- Aliases/query keys: 交互式证明
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `interactive-proofs`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source-backed seed 包含 Sum-check Protocol 与 Interactive Proofs for Muggles。Sparrow 作为 secondary evidence，展示 product-form sumcheck/GKR 如何被改造为 low-memory SNARK route。
Public-coin recursion source adds another applied route: GKR/public-coin verifier structure can be embedded inside an outer SNARK when Fiat-Shamir inputs are shortened and statement binding is handled explicitly.
Thaler time-optimal source adds a direct GKR method-family milestone: for regular layered circuits, prover work can be reduced from `O(S log S)` to `O(S)` while preserving the low-cost verifier shape.

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[verifiable-computation|verifiable-computation]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

让 verifier 用低于直接计算的成本检查大计算、低度多项式关系或 circuit evaluation。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[verifiable-computation|verifiable-computation]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[sum-check-protocol|sum-check-protocol]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[delegated-computation|delegated-computation]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[gkr-protocols|GKR-style interactive proofs]] | method_family | GKR recurs across delegated computation, sum-check, low-memory SNARKs, recursion, and now time-optimal circuit evaluation; a child node reduces source reads for GKR queries. | GKR seed source; Thaler 2017; downstream bridge sources | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| sum-check protocol | sum-check protocol | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| GKR-style delegated computation | GKR-style delegated computation | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| low-degree extensions | low-degree extensions | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Space-efficient sumcheck/GKR | 对 `sum f*g` 类 product-form claims 做低内存 sumcheck，并把每层 GKR claim 接到 streaming prover route。 | Layered data-parallel circuits and prover-memory bottleneck. | 不提供 SNARK 的全部部件；commitment、Fiat-Shamir、zero-knowledge 仍属于 proof-system layer。 | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]] |
| public-coin verifier recursion into SNARKs | 用 public-coin argument 证明 bulk computation，并把其 verifier 放进外层 SNARK；Fiat-Shamir challenge 绑定到短 statement commitment。 | Public-coin argument is one-round/compiler-compatible and outer SNARK verifier has a splittable computation step. | 这是递归证明应用路线，不是 GKR/IP foundation；concrete GKR instantiation is heuristic. | [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Public-coin recursion for hash verification]] |
| Time-optimal GKR for regular circuits | 重写 GKR 每层 sum-check polynomial，并缓存 `beta`/MLE 部分绑定值，让 prover 在 regular wiring 下总工作量接近直接电路求值。 | Layered arithmetic circuits with sufficiently regular wiring and similar in-neighbor functions. | 不是任意 irregular circuit 的通用优化；data-parallel 和 matrix multiplication 细节保留在 source/GKR 子节点。 | [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles|Delegating Computation: Interactive Proofs for Muggles]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-dfbe6c185c1b-sum-check-protocol|The Sum-Check Protocol]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | paper | 作为 secondary source extension，展示 space-efficient sumcheck/GKR 的 proof-system engineering 用法 | primary path is ZKP/proof-systems; not IP foundation evidence | `p1-p15` |
| [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification]] | paper | 作为 secondary source extension，展示 public-coin/GKR verifier can be embedded into SNARK recursion for hash verification | not a canonical GKR foundation source; concrete one-round GKR instantiation is heuristic | `Abstract`, `§3-§6`, `Appendix H-I` |
| [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | paper | 作为 GKR method-family source extension，展示 regular-circuit GKR prover 从 `O(S log S)` 到 `O(S)` 的实践化路线 | not a SNARK/ZK source; regularity assumptions matter | `p1-p50`, `Theorem 1-3`, `Tables 1-5` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前覆盖 sum-check/delegated computation seed；Sparrow 补充了 sum-check/GKR 在低内存 SNARK engineering 中的迁移用法。Public-coin recursion source 补充了另一种迁移用法：GKR/public-coin verifier can be embedded into SNARK recursion when Fiat-Shamir input and statement binding are controlled。Thaler 2017 则补上直接的 GKR 方法族节点，说明 GKR 的关键实践问题不只是 verifier 便宜，还包括 prover overhead 是否能接近直接求值。GKR 的 foundation 应由 [[gkr-protocols|GKR-style interactive proofs]] 承载；跨到 SNARK/recursion 的内容继续通过 bridges 表达，避免把 non-interactivity、commitment 或 zero-knowledge 混入 IP 本体。

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
| [[sha256-dfbe6c185c1b-sum-check-protocol|The Sum-Check Protocol]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | secondary source extension | space-efficient product-form sumcheck/GKR route | 方法族与解决路线; Bridge Links | no | keep primary details in [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification]] | secondary source extension + bridge | public-coin/GKR verifier recursion for faster SNARK-friendly hash verification | 方法族与解决路线; Bridge Links | no | keep primary details in [[recursive-proof-composition|Recursive proof composition]] |
| [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | source extension + child split | time-optimal GKR for regular circuit evaluation, data-parallel GKR batching, and matrix multiplication verification primitive | 下级结构; 方法族与解决路线; 代表 Sources; 关系图谱 | yes | keep source-local details in [[gkr-protocols|GKR-style interactive proofs]] and source note |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[sum-check-protocol-to-memory-efficient-snarks|Sum-check protocol -> memory-efficient SNARKs]] | `verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | dependency, method_transfer, prover_space_reduction | Product-form sumcheck transfers to low-memory SNARK construction, but sumcheck alone does not provide commitments, non-interactivity or zero knowledge. | active_seed |
| [[public-coin-interactive-proofs-to-recursive-proof-composition|Public-coin interactive proofs -> recursive proof composition]] | `verifiable-computation/interactive-proofs; zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | method_transfer, dependency, verification_embedding, fiat_shamir_boundary | Public-coin verifier embedding transfers to recursive proof composition; it does not define GKR or make all IPs recursively cheap. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-interactive-proofs | is_a | nahida-knowledge-verifiable-computation | vault/04_Knowledge/verifiable-computation/interactive-proofs.md; vault/04_Knowledge/verifiable-computation.md | medium | active_seed |
| nahida-knowledge-interactive-proofs | has_child | nahida-knowledge-delegated-computation | vault/04_Knowledge/verifiable-computation/interactive-proofs.md; vault/04_Knowledge/verifiable-computation/interactive-proofs/delegated-computation.md | medium | active_seed |
| nahida-knowledge-interactive-proofs | has_child | nahida-knowledge-sum-check-protocol | vault/04_Knowledge/verifiable-computation/interactive-proofs.md; vault/04_Knowledge/verifiable-computation/interactive-proofs/sum-check-protocol.md | medium | active_seed |
| nahida-knowledge-interactive-proofs | has_child | nahida-knowledge-gkr-protocols | vault/04_Knowledge/verifiable-computation/interactive-proofs/gkr-protocols.md; Thaler 2017 source note | high | active_seed |
| nahida-knowledge-interactive-proofs | evidenced_by | vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md | vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md | medium | active_seed |
| nahida-knowledge-interactive-proofs | evidenced_by | vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md | vault/03_Sources/papers/sha256-dfbe6c185c1b-sum-check-protocol.md | medium | active_seed |
| nahida-knowledge-interactive-proofs | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md | secondary source note | medium | active_seed |
| nahida-knowledge-interactive-proofs | bridges_to | nahida-bridge-sum-check-protocol-to-memory-efficient-snarks | bridge note | high | active_seed |
| nahida-knowledge-interactive-proofs | evidenced_by | vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md | public-coin recursion source note | medium | active_seed |
| nahida-knowledge-interactive-proofs | bridges_to | nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition | bridge note | high | active_seed |
| nahida-knowledge-interactive-proofs | evidenced_by | vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md | source note p1-p50 | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| IP=PSPACE/PCP/IOP foundations 仍缺 source。 | 影响 interactive proofs 方向的完整 foundation，而不是 GKR 子节点本身。 | nahida-research-search or nahida-update | medium | queued |
| GKR/streaming IP/IOP comparison sources 仍缺。 | 当前已有 GKR seed 和 time-optimal GKR，但跨 SNARK/IOP/streaming variants 的边界还需更多来源。 | nahida-update / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 2 source notes; 1 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-sparrow-space-efficient-snarks | Added secondary space-efficient sumcheck/GKR bridge to memory-efficient SNARKs. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-public-coin-proof-recursion | Added public-coin/GKR verifier recursion as a secondary applied route and bridge to recursive proof composition. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-time-optimal-interactive-proofs | Added GKR-style interactive proofs as a child method-family node and attached Thaler time-optimal GKR source extension. | 1 source note | codex |
