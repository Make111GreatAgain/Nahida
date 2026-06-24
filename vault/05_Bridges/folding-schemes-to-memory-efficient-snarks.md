---
id: "nahida-bridge-folding-schemes-to-memory-efficient-snarks"
title: "Folding schemes -> memory-efficient SNARKs"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
topic_ids:
  - "folding-schemes"
  - "memory-efficient-snarks"
endpoint_knowledge_refs:
  - "nahida-knowledge-folding-schemes"
  - "nahida-knowledge-memory-efficient-snarks"
endpoint_paths:
  - "zero-knowledge-proofs/recursion-and-folding/folding-schemes"
  - "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
relation_types:
  - "application"
  - "method_transfer"
  - "performance_compression"
  - "dependency"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
  - "vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md"
representative_source_refs:
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "iacr:2021/370"
query_keys:
  - "folding schemes for low-memory SNARKs"
  - "folding-based SNARKs"
  - "commit-and-fold"
  - "Mangrove"
aliases:
  - "Folding-based low-memory SNARKs"
  - "Folding schemes to streaming SNARKs"
domains:
  - "zero-knowledge-proofs"
topics:
  - "folding-schemes"
  - "memory-efficient-snarks"
  - "proof-carrying-data"
tags:
  - "nahida/bridge"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-mangrove"
source_refs:
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "iacr:2021/370"
confidence: "high"
trust_tier: "primary"
---

# Folding schemes -> memory-efficient SNARKs

## 关系命题

Folding schemes 可以从 incrementally verifiable computation 的递归状态压缩工具，迁移为 memory-efficient SNARK construction 的内部机制: 先把大 NP statement 编译成 uniform chunks，再用 PCD tree 和 folding 把 chunk-level obligations 合并，使 prover 不必在一个 monolithic pass 中持有完整 computation trace。

这条 bridge 不表示所有 folding schemes 都自动产生低内存 SNARK，也不表示 Mangrove 是 folding scheme foundation。它记录的是 Mangrove 提供的 source-backed transfer: folding/PCD/commitment folding 能缓解 SNARK prover memory 和 global-check overhead。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[folding-schemes|Folding schemes]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes` | 把多个 relation instances 折叠成更少/更小的累积 instance，用于 IVC、proof aggregation 或其他递归证明结构 | recursion/folding problem node |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | 降低 SNARK prover peak memory、pass 数或单机资源，同时保持 succinct verification | proof-system prover-resource problem node |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `application` | folding 被应用到低内存 SNARK 构造 | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] §2-§6 | active_seed |
| `method_transfer` | IVC/folding 的 deferred checking 模式转移到 chunked Plonkish SNARK | Mangrove uniform compiler + PCD tree | active_seed |
| `performance_compression` | decoupled PCD 和 commit-and-fold 降低递归/commitment overhead | Mangrove §2.3, §4-§5 | active_seed |
| `dependency` | memory-efficient SNARK route 依赖 folding schemes、PCD、commitments 和 Plonkish arithmetization | Mangrove §3-§6 | active_seed |

## Transfer Matrix

| From folding schemes | Transfers to memory-efficient SNARKs? | How | Boundary |
| --- | --- | --- | --- |
| Deferred checking / accumulation | yes | chunk obligations 被 folding 成 root obligation，再由 succinct proof 验证 | 仍需 final SNARK/PCD proof；folding alone 不等于 SNARK |
| IVC-style step uniformity | yes | Mangrove uniform compiler 把 Plonkish relation 变成许多 identical simple steps | 依赖 arithmetization structure；arbitrary workloads 需要编译器支持 |
| Folding over polynomial relations | yes | Section 5 folding schemes handle homogeneous or arbitrary polynomial maps | security assumptions and prover cost depend on chosen protocol |
| Folding over committed values | yes | commit-and-fold avoids in-circuit opening constraints | requires binding linear commitment maps and polynomial witness testing |
| Tree-based recursion/PCD | yes | PCD tree makes proof generation parallelizable and streaming via TreeEval | control overhead must be decoupled; PCD assumptions remain |
| Proof aggregation route | no direct transfer | aggregation is a sibling application of folding | do not classify Mangrove as proof aggregation |

## Non-Transfer Boundary

- Folding schemes do not by themselves supply zero-knowledge; Mangrove notes zero-knowledge can be adapted from known transformations but does not fully instantiate it.
- Mangrove's low-memory results rely on Plonkish arithmetization, memory parameter `m`, PCD arity `k`, and specific commitment/folding assumptions.
- The standard-model folding scheme needed inside PCD uses a heuristic random-oracle-to-hash step in Section 5.3.
- Performance estimates are not a production prover implementation.
- This bridge should not merge [[folding-schemes|Folding schemes]] with [[memory-efficient-snarks|Memory-efficient SNARKs]]; folding is a method dependency, low-memory SNARKs are a proof-system problem layer.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] Abstract/§1 | problem framing: low memory, two passes, constant CRS, folding-based SNARKs | author claim and source framing |
| Mangrove §2.1 | uniform compiler from Plonkish NP to chunks | Plonkish-specific |
| Mangrove §2.3 | decoupling PCD and commit-and-fold reduce overhead | optimization-level evidence |
| Mangrove §5 | folding schemes for polynomial relations | theoretical route; heuristic standard-model issue in §5.3 |
| Mangrove §6.4 | `2^24` about 2 min/390 MB; `2^32` about 8h/800 MB; 34 MB proof, 12 KB after Spartan wrapping | estimate, not full production benchmark |
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova]] | existing folding/IVC seed endpoint context | Nova itself is IVC seed, not low-memory SNARK source |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[folding-schemes|Folding schemes]] | Add commit-and-fold / polynomial relation folding source extension and bridge link | done |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | Create problem node and attach Mangrove as representative source | done |
| [[proof-systems|Proof systems]] | Add Memory-efficient SNARKs as child problem | done |
| [[zk-snarks|zk-SNARKs]] | Add low-memory proving as source extension, not foundation replacement | done |
| [[modular-zksnarks|Modular zkSNARKs]] | Add Mangrove commit-and-prove extension as source extension | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-folding-schemes | applies_to | nahida-knowledge-memory-efficient-snarks | Mangrove §2-§6 | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | uses | nahida-knowledge-folding-schemes | Mangrove §4-§6 | high | active_seed |
| nahida-knowledge-folding-schemes | bridges_to | nahida-bridge-folding-schemes-to-memory-efficient-snarks | bridge note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | bridges_to | nahida-bridge-folding-schemes-to-memory-efficient-snarks | bridge note | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| Gemini/DARK/Spartan source absorbed | Compare streaming/chunked route against Mangrove | `nahida-update` |
| Proof-Carrying Data primary source absorbed | Strengthen PCD endpoint assumptions and transfer boundary | `nahida-update` |
| Protostar/ProtoGalaxy/HyperNova source absorbed | Update polynomial-relation folding comparison | `nahida-update` |
| Production Mangrove-like implementation/repo absorbed | Replace estimates with implementation evidence | `nahida-github-repo-analyze` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-mangrove | Created bridge from folding schemes to memory-efficient SNARKs using Mangrove as first source-backed transfer. | 2 source notes | codex |
