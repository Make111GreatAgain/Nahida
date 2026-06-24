---
id: "nahida-knowledge-folding-schemes"
title: "Folding schemes"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "folding-schemes"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
parent_knowledge_refs:
  - "nahida-knowledge-recursion-and-folding"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "folding-schemes"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/folding-schemes"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-folding-schemes"
    relation: "is_a"
    to: "nahida-knowledge-recursion-and-folding"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-folding-schemes"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-folding-schemes"
    relation: "bridges_to"
    to: "nahida-bridge-folding-schemes-to-sum-check-and-polynomial-commitments"
    evidence_refs:
      - "vault/05_Bridges/folding-schemes-to-sum-check-and-polynomial-commitments.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-folding-schemes"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-folding-schemes"
    relation: "bridges_to"
    to: "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
    evidence_refs:
      - "vault/05_Bridges/folding-schemes-to-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-folding-schemes"
    relation: "applies_to"
    to: "nahida-knowledge-memory-efficient-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
      - "vault/05_Bridges/folding-schemes-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-folding-schemes"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-folding-schemes"
    relation: "bridges_to"
    to: "nahida-bridge-folding-schemes-to-memory-efficient-snarks"
    evidence_refs:
      - "vault/05_Bridges/folding-schemes-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-folding-schemes-to-sum-check-and-polynomial-commitments"
  - "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
  - "nahida-bridge-folding-schemes-to-memory-efficient-snarks"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md"
  - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
  - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
representative_source_refs:
  - "iacr:2021/370"
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
query_keys:
  - "Folding schemes"
  - "folding-schemes"
  - "Nova"
  - "folding scheme"
  - "relaxed R1CS"
  - "IVC"
  - "split IVC"
  - "SnarkFold"
  - "SNARK proof aggregation"
  - "commit-and-fold"
  - "folding-based SNARKs"
  - "memory-efficient SNARKs"
  - "Mangrove"
aliases:
  - "Nova"
  - "folding scheme"
  - "relaxed R1CS"
  - "IVC"
  - "split IVC"
  - "commit-and-fold"
  - "folding-based SNARKs"
domains:
  - "zero-knowledge-proofs"
topics:
  - "folding-schemes"
  - "snark-proof-aggregation"
  - "memory-efficient-snarks"
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
  - "nahida-knowledge-20260620-snarkfold"
  - "nahida-knowledge-20260620-mangrove"
source_refs:
  - "iacr:2021/370"
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
confidence: "medium"
trust_tier: "primary"
---

# Folding schemes

## 定义与范围

- 定义: Folding schemes 将多个计算实例或约束系统递归折叠成较小的累积实例，用于 incrementally verifiable computation。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `folding-schemes`
- Aliases/query keys: Nova, folding scheme, relaxed R1CS, IVC
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `folding-schemes`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

Nova 是当前 foundation seed；relaxed R1CS 与 IVC 是本节点内的方法/机制，不拆成 source-shaped foundation。SnarkFold 增加 split IVC source extension: folding 不只用于递归计算本身，也可以作为 SNARK proof aggregation 的 aggregation function。Mangrove 增加 commit-and-fold/polynomial relation folding extension: folding 也可以作为低内存 SNARK 构造内部机制，用来折叠 uniform chunks 和 committed leaf relations。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[recursion-and-folding|recursion-and-folding]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

降低递归证明每步生成/验证成本，让长计算链保持可持续证明。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[recursion-and-folding|recursion-and-folding]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| relaxed R1CS accumulation | relaxed R1CS accumulation | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| folding two instances into one | folding two instances into one | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| IVC and recursive arguments | IVC and recursive arguments | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| split IVC | 同时维护 F-friendly 和 Fold-friendly running instances，让递归电路只证明 folding/hash claim，避免把 pairing-heavy relation 转成同一电路结构。 | F 的自然 relation 与 Fold-circuit relation 不同，直接转换代价过高。 | 当前由 SnarkFold 单一 source 支撑；对其他 proof systems 需要重新设计 relation/folding。 | [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] |
| commit-and-fold over polynomial relations | 在 committed values 上折叠 leaf polynomial relation，避免把 expensive commitment opening constraints 编进递归电路。 | 目标 relation 可表示为 polynomial map，commitment/linear maps 满足 binding 和线性结构。 | 当前由 Mangrove 单一 source 支撑；PCD 中 standard-model folding 有 heuristic security boundary。 | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova: Recursive Zero-Knowledge Arguments from Folding Schemes]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | paper | split IVC source extension：用不同类型 running instances 避免昂贵 relation transformation，并应用到 SNARK proof aggregation | 单一 source；Groth16 构造是专门化实例 | `p7-p19`, `p22-p29` |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | paper | commit-and-fold / polynomial relation folding source extension：用 folding/PCD 构造 low-memory SNARK | 单一 source；Mangrove 是 memory-efficient SNARK source，不是 folding foundation | `p1-p69` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-20`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: Folding schemes 是 recursion/folding 方向的核心 problem node。Nova 覆盖 relaxed R1CS/folding-based IVC 基础 seed；SnarkFold 补充 split IVC 路线，说明 folding 可以服务 SNARK proof aggregation，并通过多类型 running instances 避免 pairing-heavy relation transformation；Mangrove 补充 commit-and-fold 路线，说明 folding 还可以服务 low-memory SNARK construction，把 uniform chunks 和 committed polynomial relations 压成可验证的 root obligation。

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
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova: Recursive Zero-Knowledge Arguments from Folding Schemes]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | source extension | split IVC, folding as proof aggregation route | 方法族与解决路线; Bridge Links; 当前综合 | no | keep SnarkFold as source, not node |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | source extension | commit-and-fold, polynomial relation folding, PCD tree for low-memory SNARK construction | 方法族与解决路线; Bridge Links; 当前综合 | no | keep Mangrove as source, route problem through [[memory-efficient-snarks|Memory-efficient SNARKs]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[folding-schemes-to-sum-check-and-polynomial-commitments|Folding schemes -> sum-check and polynomial commitments]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/polynomial-commitments` | dependency, shared_pattern | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 | active_seed |
| [[folding-schemes-to-snark-proof-aggregation|Folding schemes -> SNARK proof aggregation]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation` | applies_to, method_transfer, performance_compression | Folding/IVC 可作为 aggregation route；具体 SNARK relation、curve/setup 和 final verifier duties 不自动迁移。 | active_seed |
| [[folding-schemes-to-memory-efficient-snarks|Folding schemes -> memory-efficient SNARKs]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | application, method_transfer, performance_compression, dependency | Folding/PCD 可作为 low-memory SNARK construction route；具体 arithmetization、commitment maps、PCD overhead 和 heuristic assumptions 不自动迁移。 | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-folding-schemes | is_a | nahida-knowledge-recursion-and-folding | vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md; vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md | medium | active_seed |
| nahida-knowledge-folding-schemes | evidenced_by | vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md | vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md | medium | active_seed |
| nahida-knowledge-folding-schemes | bridges_to | nahida-bridge-folding-schemes-to-sum-check-and-polynomial-commitments | vault/05_Bridges/folding-schemes-to-sum-check-and-polynomial-commitments.md | medium | active_seed |
| nahida-knowledge-folding-schemes | evidenced_by | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-folding-schemes | bridges_to | nahida-bridge-folding-schemes-to-snark-proof-aggregation | vault/05_Bridges/folding-schemes-to-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-folding-schemes | applies_to | nahida-knowledge-memory-efficient-snarks | Mangrove source note; bridge | high | active_seed |
| nahida-knowledge-folding-schemes | evidenced_by | vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md | Mangrove source note | high | active_seed |
| nahida-knowledge-folding-schemes | bridges_to | nahida-bridge-folding-schemes-to-memory-efficient-snarks | vault/05_Bridges/folding-schemes-to-memory-efficient-snarks.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| SuperNova、HyperNova、Nebula、Protostar 等缺 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |
| split IVC 目前只有 SnarkFold source 支撑。 | 需要更多 source 校准它是否应从 route 升级为独立 child method | nahida-update | medium | queued |
| commit-and-fold / polynomial relation folding 目前只有 Mangrove source 支撑。 | 需要 Protostar/ProtoGalaxy/PCD sources 校准是否应拆成独立 child method | nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 3 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-snarkfold | Added split IVC as source-backed folding route and bridge to SNARK proof aggregation. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-mangrove | Added commit-and-fold / polynomial relation folding route and bridge to memory-efficient SNARKs. | 1 source note | codex |
