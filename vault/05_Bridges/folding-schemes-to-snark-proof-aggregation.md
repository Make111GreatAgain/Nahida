---
id: "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
title: "Folding schemes -> SNARK proof aggregation"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
bridge_kind: "method_transfer"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
topic_ids:
  - "folding-schemes"
  - "snark-proof-aggregation"
endpoint_knowledge_refs:
  - "nahida-knowledge-folding-schemes"
  - "nahida-knowledge-snark-proof-aggregation"
endpoint_paths:
  - "zero-knowledge-proofs/recursion-and-folding/folding-schemes"
  - "zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation"
relation_types:
  - "applies_to"
  - "method_transfer"
  - "performance_compression"
relation_edges:
  - from: "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
    relation: "connects"
    to: "nahida-knowledge-folding-schemes"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md"
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
    relation: "connects"
    to: "nahida-knowledge-snark-proof-aggregation"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation.md"
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
representative_source_refs:
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
query_keys:
  - "folding schemes proof aggregation"
  - "split IVC proof aggregation"
  - "SnarkFold"
aliases:
  - "split IVC bridge"
  - "folding-based proof aggregation"
domains:
  - "zero-knowledge-proofs"
topics:
  - "folding-schemes"
  - "snark-proof-aggregation"
tags:
  - "nahida/bridge"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-snarkfold"
source_refs:
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
confidence: "high"
trust_tier: "primary"
---

# Folding schemes -> SNARK proof aggregation

## 关系摘要

- From: [[folding-schemes|Folding schemes]]
- To: [[snark-proof-aggregation|SNARK proof aggregation]]
- Relation types: `applies_to`, `method_transfer`, `performance_compression`
- Relationship thesis: Folding schemes can act as the aggregation function for a sequence of SNARK proofs. SnarkFold shows that wrapping this route in split IVC can keep aggregation proof size and verifier work constant while avoiding a costly transformation of pairing-heavy SNARK verification into a single recursive-circuit relation.
- Evidence scope: currently source-backed by [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] only; this is an active seed, not a complete proof-aggregation survey.

## Endpoint 背景

| Endpoint | Path | Local meaning | Status |
| --- | --- | --- | --- |
| [[folding-schemes|Folding schemes]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes` | 将多个计算/约束实例折叠为较小 running instance，用于 IVC/recursive proof compression。 | foundation_thin |
| [[snark-proof-aggregation|SNARK proof aggregation]] | `zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation` | 把多个 SNARK instance-proof pairs 合成低 verifier cost 的聚合对象。 | foundation_thin |

## Transfer Matrix

| 从 folding schemes 迁移的东西 | 到 SNARK proof aggregation 的作用 | Evidence | 不迁移/需重做的边界 |
| --- | --- | --- | --- |
| Running instance | 累积已经聚合过的 proofs，避免 verifier 逐个检查输入 proofs。 | SnarkFold §4-§5 | Running instance 的 relation 类型必须适配具体 SNARK proof relation。 |
| Folding verifier relation | 让 aggregation verifier 只检查最终 folded state 和压缩 proof。 | SnarkFold Fig. 5-6 | 最终 aggregated `(u, pi)` 仍要被真实应用 verifier 检查。 |
| IVC succinctness | 让 aggregation proof size/verifier work 不随 iteration count 线性增长。 | SnarkFold Theorem 1-2 | Prover/aggregator work 仍随 `n` 增长。 |
| Split instance design | F-friendly algebraic instance 和 Fold-friendly circuit instance 分开，避免 pairing relation 进入递归电路。 | SnarkFold §4.1-§4.3 | 对 Plonk/STARK/其他 SNARK 需要重新设计 relation/folding；Groth16 trick 不自动迁移。 |
| Hash claim binding | 用 hash 绑定 running states，保持 Fold-circuit output 结构可折叠。 | SnarkFold Fig. 2, Fig. 5 | Hash/RO instantiation 和 non-relaxed checks 是安全边界的一部分。 |

## Non-Transfer Boundary

- Folding schemes 的“可折叠性”不自动意味着任意 SNARK proof 都可高效聚合；每种 SNARK 需要可折叠 relation 或专门的 relaxed/augmented relation。
- SnarkFold 的 Groth16 aggregation 依赖 augmented relaxed Groth16 relation；不能直接把这个构造当成 Plonk/STARK aggregation。
- 常数 proof size/verifier work 是 aggregation proof 的性质；输入 proofs 的生成和 aggregator local work 仍然昂贵且随 `n` 增长。
- 论文没有提供生产 gas/wall-clock benchmark；bridge 不能回答部署性能，只能回答方法关系。

## Evidence

| Source | 支持了什么 | Anchor | Confidence |
| --- | --- | --- | --- |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | 将 split IVC 用于 SNARK proof aggregation；给出 Groth16 folding 和常数 proof/verifier operation-count claim。 | `p1-p19`, Appendices `p22-p29` | high |
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova: Recursive Zero-Knowledge Arguments from Folding Schemes]] | 提供 folding/IVC 背景；SnarkFold 作为后续应用路线而非 Nova 本身。 | existing source note | medium |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-bridge-folding-schemes-to-snark-proof-aggregation | connects | nahida-knowledge-folding-schemes | vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md; vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-bridge-folding-schemes-to-snark-proof-aggregation | connects | nahida-knowledge-snark-proof-aggregation | vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation.md; vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-bridge-folding-schemes-to-snark-proof-aggregation | evidenced_by | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |

## Refresh Triggers

| Trigger | Action |
| --- | --- |
| SnarkPack/TIPP source absorbed | Calibrate comparison route and update non-transfer boundary. |
| Hekaton or SnarkPack/TIPP absorbed | Decide whether to split folding-based aggregation children. Pianist has already been routed to [[distributed-proof-generation|Distributed proof generation]] and Mangrove to [[memory-efficient-snarks|Memory-efficient SNARKs]]. |
| Implementation/gas benchmark source absorbed | Add engineering evidence; do not infer from SnarkFold operation counts alone. |

## 更新记录

| Date | Run ID | Change | Sources |
| --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-snarkfold | Created bridge from folding schemes to SNARK proof aggregation. | 1 source note |
