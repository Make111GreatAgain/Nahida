---
id: "nahida-bridge-distributed-proof-generation-to-zkrollups"
title: "Distributed proof generation -> zkRollup prover scaling"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "distributed-proof-generation"
  - "zkrollup-prover-scaling"
endpoint_knowledge_refs:
  - "nahida-knowledge-distributed-proof-generation"
  - "nahida-knowledge-zkp-blockchain-applications"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
  - "zero-knowledge-proofs/applications/blockchain-applications"
relation_types:
  - "application"
  - "applies_to"
  - "scalability_enabler"
  - "implementation_reuse"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
representative_source_refs:
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
query_keys:
  - "zkRollup prover scaling"
  - "distributed proof generation for zkRollups"
  - "distributed ZKP rollup"
  - "Pianist zkRollup"
aliases:
  - "Distributed proving for zkRollups"
  - "zkRollup prover scaling"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "distributed-proof-generation"
  - "blockchain-applications"
  - "zkrollups"
tags:
  - "nahida/bridge"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-pianist"
source_refs:
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
confidence: "high"
trust_tier: "primary"
---

# Distributed proof generation -> zkRollup prover scaling

## 关系命题

Distributed proof generation 可以作为 zkRollup/zkEVM prover scaling 的技术路线: 它把 rollup batch proof 的 prover-side time/memory 压力分配到多台机器，同时目标是保持最终 proof size 和 verifier time 不随机器数增长。

这条 bridge 不表示 distributed proving 能解决 rollup 的全部系统问题。它只说明 prover generation bottleneck 可以从 proof-system engineering 侧被缓解。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[distributed-proof-generation|Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation` | 多机协作生成一个 ZKP proof，关注 prover time、memory、communication、proof size、verifier time 和 worker trust | ZKP proof-system engineering 方法族 |
| [[blockchain-applications|ZKP blockchain applications]] | `zero-knowledge-proofs/applications/blockchain-applications` | zkRollups/zkEVM 等区块链应用把大量交易或状态转换压缩为 proof，关注 proving throughput、on-chain verification、gas、liveness 和系统假设 | ZKP 在区块链系统问题上的应用层 |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `application` | distributed proving 被应用到 zkRollup/zkEVM proving | [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] title/abstract/§6.1 | active_seed |
| `scalability_enabler` | 它缓解 prover-side time/memory bottleneck，使更大 batch 成为可能 | Pianist 8192 tx/64 machines/313s and memory results | active_seed |
| `implementation_reuse` | data-parallel/distributed prover ideas 可从 bridge/light-client proving 迁移到 rollup-style workloads with caveats | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] deVirgo and Pianist related work | active_seed |

## Transfer Matrix

| From distributed proof generation | Transfers to zkRollups? | How | Boundary |
| --- | --- | --- | --- |
| Work partitioning by sub-circuit/machine | yes | rollup batch can be split across transactions or circuit partitions | only if workload/circuit structure supports partitioning |
| Constant or small proof/verifier overhead goal | yes | rollup needs on-chain verification cost not to scale with worker count | exact constants depend on proof system and chain verifier support |
| Bivariate constraint representation | yes for Plonk-like routes | Pianist uses `Y` for machine index and `X` for circuit position | not automatically reusable for all STARK/FRI/lookup-heavy systems |
| Distributed commitments/openings | yes | DKZG-style aggregation keeps communication/proof compact | depends on KZG/SRS/pairing assumptions |
| Robust collaborative proving | partly | prover pool participants may be faulty or malicious | Pianist only gives limited model; production incentives and slashing are outside |
| Recursive compression | adjacent | may make distributed proof chain-friendly | recursion is separate from distributed generation |

## Non-Transfer Boundary

- Rollup correctness, data availability, sequencer ordering, finality, bridge semantics, gas pricing and fee market do not transfer from distributed proving.
- Prover market incentives, worker scheduling, fault recovery, and payment distribution are not solved by Pianist's mining-pool analogy.
- A benchmark on converted Polygon Hermez/R1CS-to-Plonk circuits does not prove performance for production custom-gate zkEVM circuits.
- DKZG/KZG assumptions do not transfer to FRI/STARK-based rollups without a separate proof-system route.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] Abstract/§1 | zkRollup/zkEVM proof generation bottleneck and fully distributed ZKP goal | source claim |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] §3-§4.2 | bivariate Plonk/DKZG mechanism | protocol-specific to Plonk/KZG route |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] §6.1 | 8192 tx/64 machines/313s, 2144 bytes communication, 2208-byte proof, 3.5ms verifier | R1CS-to-Plonk conversion and BN254 caveats |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] §4-§5 | deVirgo as data-parallel distributed proof generation, recursive compression for on-chain verification | cross-chain workload, not rollup workload |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[distributed-proof-generation|Distributed proof generation]] | Add Pianist as representative source and application bridge | done |
| [[blockchain-applications|ZKP blockchain applications]] | Add zkRollup prover scaling route/source extension | done |
| [[proof-systems|Proof systems]] | Split distributed proof generation from parent source-extension row into child method-family node | done |
| [[kzg-commitments|KZG commitments]] | Add DKZG/bivariate KZG as usage extension, not foundation replacement | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-distributed-proof-generation | applies_to | nahida-knowledge-zkp-blockchain-applications | Pianist zkRollup evaluation | high | active_seed |
| nahida-knowledge-distributed-proof-generation | implementation_reuse | nahida-knowledge-zkp-blockchain-applications | zkBridge deVirgo plus Pianist transfer | medium | active_seed |
| nahida-knowledge-zkp-blockchain-applications | uses | nahida-knowledge-distributed-proof-generation | Pianist §6.1 | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| DIZK/aPlonk/deVirgo primary source absorbed | Update comparison matrix and method family boundaries | `nahida-update` |
| Production zkRollup prover repo or benchmark absorbed | Validate whether Pianist-like assumptions hold in real pipelines | `nahida-github-repo-analyze` or `nahida-research-search` |
| STARK/FRI distributed prover source absorbed | Decide whether KZG-specific route needs sibling node | `nahida-knowledge-get` |
| Prover network/market source absorbed | Split economics/scheduling from proof-system mechanics | bridge or application child |

## 更新记录

| Date | Run ID | Change | Sources |
| --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Created bridge from distributed proof generation to zkRollup prover scaling. | Pianist; zkBridge |
