---
id: "nahida-knowledge-snark-proof-aggregation"
title: "SNARK proof aggregation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "snark-proof-aggregation"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
parent_knowledge_refs:
  - "nahida-knowledge-recursion-and-folding"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "snark-proof-aggregation"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
relation_edges:
  - from: "nahida-knowledge-snark-proof-aggregation"
    relation: "is_a"
    to: "nahida-knowledge-recursion-and-folding"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-snark-proof-aggregation"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-snark-proof-aggregation"
    relation: "uses"
    to: "nahida-knowledge-folding-schemes"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md"
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-snark-proof-aggregation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-snark-proof-aggregation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-snark-proof-aggregation"
    relation: "bridges_to"
    to: "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
    evidence_refs:
      - "vault/05_Bridges/folding-schemes-to-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-snark-proof-aggregation"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
    evidence_refs:
      - "vault/05_Bridges/distributed-proof-generation-to-snark-proof-aggregation.md"
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
  - "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
source_note_refs:
  - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
  - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
representative_source_refs:
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
query_keys:
  - "SNARK proof aggregation"
  - "proof aggregation"
  - "SnarkFold"
  - "split IVC"
  - "SnarkPack"
  - "TIPP"
  - "GIPA"
  - "Groth16 aggregation"
  - "Hekaton"
  - "divide-and-aggregate"
  - "Mirage aggregation"
  - "commit-carrying aggregation"
aliases:
  - "proof aggregation"
  - "SNARK aggregation"
  - "Groth16 aggregation"
  - "Mirage aggregation"
domains:
  - "zero-knowledge-proofs"
topics:
  - "snark-proof-aggregation"
  - "folding-schemes"
  - "zk-snarks"
  - "distributed-proof-generation"
  - "divide-and-aggregate"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-21"
valid_until: "2026-07-21"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-21"
created: "2026-06-20"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-snarkfold"
  - "nahida-knowledge-20260621-hekaton-proof-aggregation"
source_refs:
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
confidence: "medium"
trust_tier: "primary"
---

# SNARK proof aggregation

## 定义与范围

- 定义: SNARK proof aggregation 研究如何把多个 SNARK instance-proof pairs 合并为一个更小、更便宜验证的聚合对象，同时保持所有输入 proofs 的有效性可追溯。
- 不包含: 单篇论文、单个系统名、单个 proof-system instance、一次 gas/latency 数字；这些留在 source note 或 Source Extensions。
- Canonical terms: `snark-proof-aggregation`
- Aliases/query keys: proof aggregation, SNARK aggregation, Groth16 aggregation, SnarkFold, SnarkPack
- Standalone completeness check: 本节点本地解释问题、边界、方法族、代表 source、bridge 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“多个 SNARK proofs 怎么聚合/怎么降低验证成本”时先读本节点，再打开 SnarkFold/SnarkPack/Hekaton 等少量 source。
- Update scope: 新 source 若提出 aggregation scheme、改变 proof size/verifier cost route、补充 benchmark 或改变安全边界，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

SNARK 本身让 verifier 用短 proof 验证大计算，但在 rollup、anonymous transaction、zkEVM、batch verification 等系统里，verifier 可能需要验证大量 proofs。若逐个验证，链上 gas、节点 CPU 和用户费用会近似线性增长。Proof aggregation 的维护对象不是“生成一个更快的 SNARK”，而是“给多个已存在 proofs 建立一个可验证的聚合过程”。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它能承接 SnarkFold、SnarkPack、TIPP/GIPA、Hekaton 等 proof-aggregation sources，未来 query 也会围绕 proof size、verification cost、prover overhead 和适配 proof system 的边界展开。Pianist 已深读并归入 [[distributed-proof-generation|Distributed proof generation]]，Mangrove 已深读并归入 [[memory-efficient-snarks|Memory-efficient SNARKs]]；Hekaton 同时刷新 distributed proving 和 proof aggregation，因此通过 bridge 连接。
- 为什么不是单篇论文/协议实例: SnarkFold 只是当前代表 source；本节点组织的是多 proof verification/aggregation 这一类问题。
- 需要引用的更基础 Knowledge: [[recursion-and-folding|Recursion and folding]], [[folding-schemes|Folding schemes]], [[zk-snarks|zk-SNARKs]]。
- 不应拆出的实例/协议/来源: SnarkFold、SnarkPack、TIPP implementation、单个 Groth16 relation trick 默认作为 source/representative instance，除非多来源证明需要独立 method-instance 节点。

## 解决的问题

当系统产生多个 SNARK proofs 时，怎样让 verifier 不必线性验证每个 proof，同时仍能确信所有输入 proofs 都有效。核心评价维度是:

- aggregation proof size 是否随 `n` 增长；
- verifier work 是否随 `n` 增长；
- prover/aggregator local work 是否可接受；
- 是否适配 Groth16/Plonk 等具体 SNARK；
- 是否引入额外 setup、trusted relation、random oracle 或 implementation constraint。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[recursion-and-folding|Recursion and folding]] | child_of | SnarkFold frames proof aggregation as folding/IVC application | active_seed |
| [[zk-snarks|zk-SNARKs]] | depends_on | Aggregation input/output are SNARK instance-proof pairs | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| folding/IVC-based aggregation | section | SnarkFold 提供 split IVC + Groth16 folding route。 | SnarkFold | active_seed |
| commit-carrying heterogeneous aggregation | section | Hekaton 提供 Mirage/TIPP-style multi-circuit aggregation route，并把 commitments 与 proofs 一起聚合。 | Hekaton | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| GIPA/TIPP/SnarkPack-style aggregation | 将 Groth16 verification 转成 generalized inner product，再用 compression/KZG 等工具降低证明和验证成本。 | pairing-based SNARK aggregation，且能接受对数级 proof/verifier overhead。 | SnarkFold 论文描述为 `O(log n)` proof size 和 verification cost；需要吸收 primary sources 校准。 | [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] related-work summary |
| IVC/folding-based aggregation | 把每个 proof 当作 folding input，通过 IVC 保持 aggregation proof size/verifier cost 不随 iteration 增长。 | proof aggregation 可表达为 repeated folding computation。 | 传统 folding 需要把新 proof/instance 转成同一种 relation，可能导致昂贵 transformation。 | [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] |
| split IVC | 同时维护 F-friendly 与 Fold-friendly running instances，递归电路只证明 folding/hash claim，避免把 pairing-heavy relation 转成电路。 | `F` 的自然表示和 Fold-circuit 关系类型不同，尤其是 pairing/Groth16 场景。 | 构造更复杂；安全依赖底层 folding schemes；应用到其他 SNARK 需要专门适配。 | [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] |
| augmented relaxed Groth16 folding | 为 Groth16 proof relation 加入 `mu/H/E/R/S/kappa`，吸收 cross-terms 并延迟部分 pairings。 | Groth16 proofs 聚合。 | Groth16-specific；不自动迁移到 Plonk/STARK；论文只给 operation-count comparison。 | [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] |
| Hekaton/Mirage commit-carrying aggregation | 为 Mirage commit-carrying zkSNARK 聚合 heterogeneous subcircuit proofs，同时聚合 commitments，使 memory-check challenge 可以从 succinct aggregate commitment 派生。 | 分布式证明生成中有许多 chunk proofs/commitments，且 subcircuits 可能不同。 | Mirage/Groth16-style route；final proof/verifier 随 subcircuit count logarithmic；aggregation 当前单机。 | [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | paper | 建立 split IVC + Groth16 folding 的 source-backed aggregation route；给出常数 proof size/verifier cost 的 operation-count claim | DOI/Venue unknown；无 wall-clock benchmark；Groth16 folding 是专门构造 | `p1-p19`, Appendices `p22-p29` |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | paper | 建立 divide-and-aggregate source-backed route：用 commit-carrying aggregation fan in distributed chunk proofs and commitments | Hekaton 是 distributed prover source；Mirage/TIPP aggregation 和 benchmark details 留在 source note | `p1-p35`, Appendix `p36-p44` |

## 正反例约束

- 正确: 本节点解释 proof aggregation 问题、路线和评价轴；SnarkFold 是代表 source，不是节点本体。
- 正确: Hekaton 作为 source extension 进入本节点，同时通过 [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]] 表达它和 distributed proving 的组合关系；SnarkPack/TIPP 仍需后续 primary source 校准。Pianist 这类 distributed proving source 应走 [[distributed-proof-generation|Distributed proof generation]]，Mangrove 这类 low-memory SNARK construction source 应走 [[memory-efficient-snarks|Memory-efficient SNARKs]]。
- 错误: 把 SnarkFold、SnarkPack 或 augmented relaxed Groth16 当作整个 proof aggregation 的定义。
- 错误: 把 SnarkFold §6 operation counts 当作生产 gas/latency benchmark。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-21`，覆盖当前 vault 已深读 SnarkFold 和 Hekaton。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-21`。
- 综合: 当前节点是 foundation_thin seed，但已不再只有 SnarkFold 一条路线。SnarkFold 说明 proof aggregation 可以走 folding/IVC route，并通过 split IVC 把 pairing-heavy relation 留在 algebraic-friendly instance 里，把递归电路负担降到 folding/hash claim。Hekaton 说明 proof aggregation 也可以作为 distributed prover 的 fan-in layer: worker 证明 partitioned subcircuits，coordinator 聚合 commitments 和 Mirage proofs，并用 aggregation commitment 派生 memory-check challenge。两条路线共同提示: proof aggregation 的核心边界不是“某个 SNARK 名字”，而是如何把多个 proof/commitment obligations 压缩成一个 verifier-facing proof，同时控制 aggregator work、setup、relation adaptation 和 shared-data handling。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Academic focus summary: vault 当前只记录 SnarkFold seed；不可声称该问题的最新外部趋势。
- Industrial focus summary: 缺 implementation/repo/gas benchmark source。
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: SnarkPack/TIPP/Hekaton/proof aggregation benchmark source；distributed proving sources 走 [[distributed-proof-generation|Distributed proof generation]]，low-memory SNARK sources 走 [[memory-efficient-snarks|Memory-efficient SNARKs]]。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | 创建本问题节点；补充 split IVC、augmented relaxed Groth16 和 aggregation complexity comparison | 方法族与解决路线; 代表 Sources; 当前综合 | yes | 吸收 SnarkPack/TIPP/Hekaton 等 sources 后校准 |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | 补充 commit-carrying heterogeneous aggregation route；证明 proof aggregation 可作为 distributed proving 的 fan-in layer；新增 bridge 到 [[distributed-proof-generation|Distributed proof generation]] | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 吸收 SnarkPack/TIPP/DIZK/aPlonk primary sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[folding-schemes-to-snark-proof-aggregation|Folding schemes -> SNARK proof aggregation]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation` | applies_to, method_transfer, performance_compression | Folding/IVC 可以迁移为 aggregation route；具体 SNARK relation、curve、pairing、setup 和 final verifier duties 不自动迁移。 | active_seed |
| [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation; zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation` | method_transfer, scalability_enabler, performance_compression, implementation_reuse | Proof aggregation 可作为 distributed prover 的 fan-in/compression layer；partitioning、witness distribution、worker scheduling 和具体 aggregation scheme 不自动迁移。 | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-snark-proof-aggregation | is_a | nahida-knowledge-recursion-and-folding | vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation.md; vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md | high | active_seed |
| nahida-knowledge-snark-proof-aggregation | depends_on | nahida-knowledge-zk-snarks | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md; vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-snark-proof-aggregation | uses | nahida-knowledge-folding-schemes | vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md; vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-snark-proof-aggregation | evidenced_by | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-snark-proof-aggregation | bridges_to | nahida-bridge-folding-schemes-to-snark-proof-aggregation | vault/05_Bridges/folding-schemes-to-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-snark-proof-aggregation | evidenced_by | vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md | Hekaton source note | high | active_seed |
| nahida-knowledge-snark-proof-aggregation | bridges_to | nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation | [[distributed-proof-generation-to-snark-proof-aggregation|bridge]]; Hekaton source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| SnarkPack/TIPP/GIPA primary sources 缺。 | 当前对既有路线的描述来自 SnarkFold related work，不能替代原文证据。 | nahida-update or nahida-research-search | high | queued |
| SnarkPack/TIPP/GIPA primary sources 仍缺；Hekaton 已作为 commit-carrying heterogeneous aggregation route 吸收。 | 这些 sources 可校准 Hekaton/SnarkFold 对既有 aggregation 路线的比较。 | nahida-update or nahida-research-search | high | queued |
| 缺 implementation/gas/wall-clock benchmark source。 | SnarkFold 只有 operation-count comparison，不能回答生产性能。 | nahida-github-repo-analyze or nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-snarkfold | Created SNARK proof aggregation problem node from SnarkFold and linked it to folding schemes and zk-SNARKs. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-hekaton-proof-aggregation | Added Hekaton as commit-carrying heterogeneous aggregation route and linked proof aggregation to distributed proof generation. | 1 source note | codex |
