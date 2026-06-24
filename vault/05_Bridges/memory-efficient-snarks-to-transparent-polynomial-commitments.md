---
id: "nahida-bridge-memory-efficient-snarks-to-transparent-polynomial-commitments"
title: "Memory-efficient SNARKs -> transparent polynomial commitments"
original_title: "Memory-efficient SNARKs -> transparent polynomial commitments"
file_slug: "memory-efficient-snarks-to-transparent-polynomial-commitments"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_direction"
bridge_status: "active_seed"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
  - "zero-knowledge-proofs/polynomial-commitments"
endpoint_knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-polynomial-commitments"
from_domain: "zero-knowledge-proofs"
to_domain: "zero-knowledge-proofs"
from_direction: "proof-systems"
to_direction: "polynomial-commitments"
from_topic: "memory-efficient-snarks"
to_topic: "polynomial-commitments"
relation_types:
  - "dependency"
  - "method_transfer"
  - "transparent_commitment_route"
  - "post_quantum_candidate"
directionality: "one_way"
relationship_thesis: "HOBBIT shows that memory-efficient SNARK construction can depend on a transparent, plausibly post-quantum multilinear polynomial commitment layer rather than only on KZG-style streaming PCS."
transferability: "medium"
non_transfer_boundary: "The PCS route transfers commitment/opening support into low-memory SNARK construction, but does not by itself provide execution-trace streaming, gate/wiring checks, lookup arguments, zero knowledge, or small proof size."
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
domains:
  - "zero-knowledge-proofs"
topics:
  - "memory-efficient-snarks"
  - "polynomial-commitments"
  - "transparent-polynomial-commitments"
  - "post-quantum-zksnarks"
source_note_refs:
  - "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-polynomial-commitments"
query_keys:
  - "transparent polynomial commitments for low-memory SNARKs"
  - "post-quantum space-efficient zkSNARK"
  - "HOBBIT PCS"
  - "transparent PCS memory-efficient SNARK"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-hobbit-space-efficient-zksnark"
source_refs:
  - "sha256:51c6a37d5caa894a133dae1ede4631ad35dc729675c6ac9a4caf00be5ecfc6ff"
confidence: "high"
trust_tier: "primary"
---

# Memory-efficient SNARKs -> transparent polynomial commitments

## 命名与路径

- Original title: Memory-efficient SNARKs -> transparent polynomial commitments
- File slug: `memory-efficient-snarks-to-transparent-polynomial-commitments`
- Path safety check: no raw slash or unsafe punctuation in filename.

## 连接命题

- From: [[memory-efficient-snarks|Memory-efficient SNARKs]]
- To: [[polynomial-commitments|Polynomial commitments]]
- Endpoint knowledge paths:
  - `zero-knowledge-proofs/proof-systems/memory-efficient-snarks`
  - `zero-knowledge-proofs/polynomial-commitments`
- Relation types: `dependency`, `method_transfer`, `transparent_commitment_route`, `post_quantum_candidate`
- Directionality: one_way
- Relationship thesis: HOBBIT shows that a low-memory zkSNARK for arbitrary arithmetic circuits can use a transparent and plausibly post-quantum multilinear PCS as its commitment/opening layer, instead of relying on KZG-family streaming PCS. This gives the memory-efficient SNARKs node a sibling route to the existing [[memory-efficient-snarks-to-kzg-commitments|KZG bridge]].
- 层级路径: proof-system problem -> PCS direction dependency
- Standalone completeness check: 本 bridge 本地解释 HOBBIT 的 PCS route、端点范围、可迁移内容、不可迁移边界和证据；端点链接用于深入，不作为唯一解释。

## 端点范围

| Endpoint | Path | Scope in bridge | Evidence | Notes |
| --- | --- | --- | --- | --- |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | prover memory / streaming proof-system problem | HOBBIT Abstract, Table 1, §5 | HOBBIT is a source extension, not a foundation node |
| [[polynomial-commitments|Polynomial commitments]] | `zero-knowledge-proofs/polynomial-commitments` | commitment/opening primitive used to compile PIOP claims into zkSNARK proof | HOBBIT §4 | HOBBIT PCS is not KZG |

## 端点基础说明

[[memory-efficient-snarks|Memory-efficient SNARKs]] 关注 SNARK prover 的内存、pass、streaming access 和 total-space accounting。这个问题不等于 distributed proving，也不等于 proof aggregation；它问的是单个 proof-generation pipeline 如何少持有 witness、trace、polynomial buffers 或 public parameters。

[[polynomial-commitments|Polynomial commitments]] 是 SNARK/PIOP 编译中的承诺与点评估证明层。不同 PCS 的 setup、proof size、verifier cost、quantum assumption、streamability 和实现常数不同；因此低内存 SNARK 需要单独说明它依赖哪一种 PCS route。

## 可迁移知识/模式

| 概念/模式 | 来源方向 | 目标方向 | 可迁移部分 | 不可迁移部分 |
| --- | --- | --- | --- | --- |
| Transparent setup | polynomial commitments | memory-efficient SNARKs | avoids trusted setup / SRS assumptions for the PCS layer | does not make all SNARK components transparent automatically |
| Plausibly post-quantum PCS | polynomial commitments | memory-efficient SNARKs | replaces elliptic-curve KZG assumptions with code/hash-style assumptions in HOBBIT's PCS | "plausibly" is not a standardized PQ guarantee |
| Streaming commit/open | polynomial commitments | memory-efficient SNARKs | commit/evaluate can run with `O(B)` working buffer over coefficient streams | execution-trace generation and PIOP checks are separate |
| Tensor-code proof composition | polynomial commitments | memory-efficient SNARKs | reduces SNARK-unfriendly Spielman encoding overhead inside the PCS proof-composition step | source-specific; needs WHIR/Brakedown/BrakingBase/Orion primary comparison |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| multilinear PCS commit/open | `zero-knowledge-proofs/polynomial-commitments` | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | HOBBIT uses its PCS to replace PIOP polynomial oracles with commitments and openings | HOBBIT §4-§5 | larger proof size than curve-based PCS |
| transparent/PQ assumption profile | `zero-knowledge-proofs/polynomial-commitments` | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | Table 1 positions HOBBIT as transparent and plausibly post-quantum while prior arithmetic-circuit low-memory zkSNARKs are not | HOBBIT Table 1 | assumption maturity still requires follow-up |
| proof-size/buffer tradeoff | `zero-knowledge-proofs/polynomial-commitments` | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | `B` tunes working buffer versus proof/verification size | HOBBIT §4, §6 | verifier/proof may be too large for some applications |

## 类比、依赖或关系边界

- 可迁移: PCS 的 streaming commit/open pattern、transparent setup property、plausible post-quantum assumption profile。
- 不可迁移: HOBBIT 的 execution-trace oracle、memory-checking wiring consistency、lookup embedding、zero-knowledge wrapper、full SNARK theorem。
- 关键假设: HOBBIT can stream the required polynomial coefficients and can replay/evaluate circuit traces with `O(S_eval)` space.
- 失效条件: 应用要求 tiny curve-style proof size，或不能提供/replay evaluation algorithm，或需要 formally standardized post-quantum assumptions。

## 证据

| Source/Note | 支撑内容 | 置信度 | 局限 |
| --- | --- | --- | --- |
| [[sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time|HOBBIT]] Abstract/Table 1 | First transparent and plausibly post-quantum space-efficient zkSNARK with `O(|C|)` prover time for arithmetic circuits | high | source-authored novelty claim; full proofs in full version |
| HOBBIT §4 | transparent linear-time multilinear PCS with streaming variant | high | PCS details condensed in conference version |
| HOBBIT §5 | PCS compiles HOBBIT PIOP claims into zkSNARK while maintaining low total space | high | full formal theorem proof in full version |
| HOBBIT §6 | proof-size and verifier tradeoff measured; HOBBIT is faster/lower-space but proof is MB-level | high | single implementation/hardware |

## 路径传播

| Endpoint path | Knowledge update | Relation/index update | Bridge/refresh action | Status |
| --- | --- | --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | Add HOBBIT as transparent/PQ optimal-time route | `bridges_to` this bridge | created | done |
| `zero-knowledge-proofs/polynomial-commitments` | Add HOBBIT PCS source extension | `evidenced_by` source and bridge ref | created | done |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | methods, representative sources, synthesis, bridge links | HOBBIT changes low-memory SNARK route map | done |
| [[polynomial-commitments|Polynomial commitments]] | methods, representative sources, source extensions, bridge links | HOBBIT adds transparent/PQ PCS usage evidence | done |
| [[sum-check-protocol|Sum-check protocol]] | source extension | HOBBIT adds product-form optimal-time streaming sumcheck | done |

## 查询入口

- Query keys:
  - transparent polynomial commitments for low-memory SNARKs
  - post-quantum space-efficient zkSNARK
  - HOBBIT PCS
  - HOBBIT vs Gemini KZG route
- Aliases:
  - HOBBIT transparent PCS route
- 典型问题:
  - “低内存 SNARK 一定要用 KZG 吗?”
  - “HOBBIT 和 Gemini/Epistle 的 PCS 路线区别是什么?”
  - “透明、抗量子候选的低内存 zkSNARK 有什么代价?”

## 刷新规则

- Last checked: 2026-06-23
- Valid until: 2026-07-23
- Refresh triggers:
  - WHIR/Brakedown/BrakingBase/Orion primary sources absorbed.
  - HOBBIT repository or full version analyzed.
  - New transparent/FRI/IPA/DARK low-memory SNARK source absorbed.

## 复核笔记

- 当前只有 HOBBIT 一个主证据，bridge 状态保持 `active_seed`。
- 不要把 HOBBIT PCS 误写到 [[kzg-commitments|KZG commitments]] child；它属于 broader [[polynomial-commitments|Polynomial commitments]] direction。

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-hobbit-space-efficient-zksnark | Created bridge from memory-efficient SNARKs to transparent/PQ polynomial commitments using HOBBIT. | 1 source note | codex |
