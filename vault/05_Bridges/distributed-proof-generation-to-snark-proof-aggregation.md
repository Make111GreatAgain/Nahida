---
id: "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
title: "Distributed proof generation -> SNARK proof aggregation"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
bridge_kind: "cross_direction_method_composition"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "distributed-proof-generation"
  - "snark-proof-aggregation"
endpoint_knowledge_refs:
  - "nahida-knowledge-distributed-proof-generation"
  - "nahida-knowledge-snark-proof-aggregation"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
  - "zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation"
relation_types:
  - "method_transfer"
  - "scalability_enabler"
  - "performance_compression"
  - "implementation_reuse"
relation_edges:
  - from: "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
    relation: "connects"
    to: "nahida-knowledge-distributed-proof-generation"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
    relation: "connects"
    to: "nahida-knowledge-snark-proof-aggregation"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation.md"
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
  - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
representative_source_refs:
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
query_keys:
  - "distributed proving proof aggregation"
  - "divide-and-aggregate zkSNARK"
  - "Hekaton"
  - "proof aggregation as distributed prover fan-in"
  - "DIZK vs Hekaton"
aliases:
  - "distributed proving via proof aggregation"
  - "DNA zkSNARK bridge"
domains:
  - "zero-knowledge-proofs"
topics:
  - "distributed-proof-generation"
  - "snark-proof-aggregation"
  - "divide-and-aggregate"
tags:
  - "nahida/bridge"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-21"
evidence_window_end: "2026-06-22"
created: "2026-06-21"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-hekaton-proof-aggregation"
  - "nahida-knowledge-20260622-dizk-distributed-zkp"
source_refs:
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
confidence: "high"
trust_tier: "primary"
---

# Distributed proof generation -> SNARK proof aggregation

## 关系摘要

- From: [[distributed-proof-generation|Distributed proof generation]]
- To: [[snark-proof-aggregation|SNARK proof aggregation]]
- Relation types: `method_transfer`, `scalability_enabler`, `performance_compression`, `implementation_reuse`
- Relationship thesis: Distributed proof generation reduces per-worker prover time and memory by splitting one large computation into many chunk proofs; SNARK proof aggregation supplies the fan-in layer that compresses those chunk proofs and commitments into one verifier-facing proof. Hekaton is the current source-backed seed for this bridge.
- Evidence scope: positive bridge evidence is currently source-backed by [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton]]; [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]] is recorded as a contrast source because it distributes Groth setup/prover without using Hekaton-style proof aggregation. Compare against deVirgo, Pianist, SnarkPack/TIPP and aPlonk sources as they enter the vault.

## Endpoint 背景

| Endpoint | Path | Local meaning | Status |
| --- | --- | --- | --- |
| [[distributed-proof-generation|Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation` | 把大 proving task 分摊到多台机器或多个参与者，同时尽量控制 proof size、verifier time、communication 和 worker memory。 | foundation_thin |
| [[snark-proof-aggregation|SNARK proof aggregation]] | `zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation` | 把多个 SNARK instance-proof pairs 或 chunk proofs 合成更小、更便宜验证的聚合对象。 | foundation_thin |

## Transfer Matrix

| 从 Distributed proof generation 迁移的东西 | 到 SNARK proof aggregation 的作用 | Evidence | 不迁移/需重做的边界 |
| --- | --- | --- | --- |
| Chunk/subcircuit proof production | 给 aggregation layer 提供可独立生成的 inner proofs。 | Hekaton p3-p4, p26-p27 | 怎样 partition circuit、怎样分 witness、怎样调度 worker 是 distributed-prover 问题，不由 aggregation 自动解决。 |
| Per-worker memory/time reduction | 让每个 worker 只处理一个子电路和对应 trace。 | Hekaton p27, p30-p33 | Coordinator aggregation time 仍可能成为瓶颈，当前 Hekaton 未并行化 aggregation。 |
| Trace/witness commitment phase | Aggregation must compress commitments before deriving memory-check challenges. | Hekaton p8-p10, p26-p27 | Commitment-carrying support需要 proof-system-specific 设计；普通 proof aggregation 不一定足够。 |
| Heterogeneous subcircuits | Multi-circuit aggregation lets arbitrary subcircuit structures be aggregated, not only repeated uniform chunks. | Hekaton p4, p8-p10, p24-p25 | Different SNARKs/commitment backends need new verification-key and setup handling. |
| Final succinct verification target | Proof aggregation prevents the final verifier from checking many subproofs. | Hekaton p26-p28 | Hekaton proof size/verifier time is logarithmic in subcircuit count, not constant; exact tradeoff is source-specific. |

## Non-Transfer Boundary

- Distributed proving and proof aggregation are not identical. A system can distribute prover work without using a SNARK proof aggregation scheme, and a proof aggregation scheme can aggregate independently produced proofs without reducing the cost of generating any one proof.
- Hekaton’s route depends on commit-carrying inner SNARKs and a Mirage-specific aggregation construction. This does not automatically transfer to Plonk, STARK, Nova-style folding, SnarkPack, aPlonk or future zkVM provers.
- Hekaton’s evaluation evidence is source-local. Hardware, OpenMPI/SLURM setup, curve choice, circuit partitioning and the fact that aggregation is single-machine in the implementation all limit direct production claims.
- The bridge does not merge endpoint nodes: [[distributed-proof-generation|Distributed proof generation]] remains the prover-side scalability family; [[snark-proof-aggregation|SNARK proof aggregation]] remains the verifier/fan-in compression problem.

## Evidence

| Source | 支持了什么 | Anchor | Confidence |
| --- | --- | --- | --- |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | Shows a concrete divide-and-aggregate zkSNARK where workers produce subcircuit proofs and a coordinator aggregates both commitments and proofs into one final proof. | p1-p35, Appendix C | high |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | Contrast source: shows distributed Groth setup/prover via Spark, distributed FFT/Lag/MSM and QAP dense row/column handling, without making proof aggregation the fan-in mechanism. | p1-p19 | high |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | Endpoint contrast: distributed proving can also be built via bivariate Plonk/KZG rather than Hekaton-style proof aggregation. | existing source note | medium |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | Endpoint contrast: proof aggregation can be folding/IVC-based without being a distributed prover for a partitioned circuit. | existing source note | medium |

## Query Use

- For “怎么把 ZKP prover 横向扩展到多机?” read [[distributed-proof-generation|Distributed proof generation]] first, then this bridge if the route uses aggregation.
- For “proof aggregation 能不能用于大电路分布式证明?” read this bridge and Hekaton.
- For “Hekaton 和 Pianist/SnarkFold 的区别?” use this bridge as the comparison hinge: Pianist is distributed proving without Hekaton’s Mirage aggregation route; SnarkFold is proof aggregation via split IVC rather than distributed circuit partitioning.

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation | connects | nahida-knowledge-distributed-proof-generation | Hekaton source note; distributed proof generation node | high | active_seed |
| nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation | connects | nahida-knowledge-snark-proof-aggregation | Hekaton source note; SNARK proof aggregation node | high | active_seed |
| nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation | evidenced_by | vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md | Hekaton source note | high | active_seed |

## Refresh Triggers

| Trigger | Action |
| --- | --- |
| aPlonk/deVirgo source absorbed | Calibrate distributed-proving routes that do not use Hekaton's exact fan-in. |
| SnarkPack/TIPP source absorbed | Calibrate the proof aggregation side of Hekaton's Mirage/TIPP lineage. |
| Hekaton repository analyzed | Add implementation evidence and revise source-local benchmark caveats. |
| New distributed aggregation paper/source absorbed | Revisit Hekaton's single-machine aggregation bottleneck and bridge maturity. |

## 更新记录

| Date | Run ID | Change | Sources |
| --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-hekaton-proof-aggregation | Created bridge from Hekaton evidence. | 1 source note |
| 2026-06-22 | nahida-knowledge-20260622-dizk-distributed-zkp | Added DIZK as a non-aggregation distributed-proving contrast source. | 1 source note |
