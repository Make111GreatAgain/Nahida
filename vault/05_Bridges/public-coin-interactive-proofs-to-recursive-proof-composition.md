---
id: "nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition"
title: "Public-coin interactive proofs -> recursive proof composition"
original_title: "Public-coin interactive proofs -> recursive proof composition"
file_slug: "public-coin-interactive-proofs-to-recursive-proof-composition"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "method_transfer"
bridge_status: "active_seed"
endpoint_paths:
  - "verifiable-computation/interactive-proofs"
  - "zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition"
endpoint_knowledge_refs:
  - "nahida-knowledge-interactive-proofs"
  - "nahida-knowledge-recursive-proof-composition"
from_domain: "verifiable-computation"
to_domain: "zero-knowledge-proofs"
from_direction: "interactive-proofs"
to_direction: "recursion-and-folding"
from_topic: "public-coin-interactive-proofs"
to_topic: "recursive-proof-composition"
relation_types:
  - "method_transfer"
  - "dependency"
  - "verification_embedding"
  - "fiat_shamir_boundary"
  - "performance_compression"
directionality: "from_to"
relationship_thesis: "Public-coin arguments such as GKR can become a recursive proof-composition component when their verifier is embedded in an outer SNARK and the Fiat-Shamir challenge is bound to a short SNARK-verifier public-input computation value instead of the full public-coin statement."
transferability: "medium"
non_transfer_boundary: "This bridge transfers the public-coin-verifier embedding pattern, not a general claim that every interactive proof can be cheaply recursed. The public-coin argument must fit the one-round/compiler assumptions, the outer SNARK verifier must expose a compatible splittable computation step, and the concrete GKR instantiation in the source is heuristic after replacing later random-oracle calls with in-circuit concrete hashes."
evidence_window_start: "2026-06-22"
evidence_window_end: "2026-06-22"
domains:
  - "verifiable-computation"
  - "zero-knowledge-proofs"
topics:
  - "interactive-proofs"
  - "GKR"
  - "sum-check-protocol"
  - "recursive-proof-composition"
  - "hash-verification"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
knowledge_refs:
  - "nahida-knowledge-interactive-proofs"
  - "nahida-knowledge-sum-check-protocol"
  - "nahida-knowledge-recursive-proof-composition"
query_keys:
  - "Public-coin interactive proofs -> recursive proof composition"
  - "GKR inside SNARK"
  - "public-coin proof recursion"
  - "short Fiat-Shamir hash recursion"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-public-coin-proof-recursion"
source_refs:
  - "iacr:2022/1072#sections-4-6"
  - "sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
confidence: "high"
trust_tier: "primary"
---

# Public-coin interactive proofs -> recursive proof composition

## 命名与路径

- Original title: Public-coin interactive proofs -> recursive proof composition
- File slug: `public-coin-interactive-proofs-to-recursive-proof-composition`
- Path safety check: current bridge lives under `05_Bridges`.

## 端点基础说明

This bridge connects [[interactive-proofs|Interactive proofs]] and the recursive-proof problem node [[recursive-proof-composition|Recursive proof composition]]. The direct source evidence is [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification]].

The bridge is intentionally about the transferable method pattern, not about treating GKR as a new top-level note from this source. GKR and sum-check stay as verifiable-computation dependencies; recursive composition receives the reusable route.

## Relationship Thesis

Public-coin argument systems can be used as inner proof systems for recursive proof composition when the expensive bulk computation is proved by the public-coin argument and only the public-coin verifier is represented inside an outer SNARK. The source paper shows this concretely for GKR-based batched hash verification.

The main obstacle is Fiat-Shamir: if the outer SNARK circuit has to hash a full GKR statement/transcript, in-circuit hashing may erase the performance gain. The bridge pattern is to bind the Fiat-Shamir challenge to a short value derived from the outer SNARK verifier's public-input computation, while separately proving that this short value corresponds to the hidden statement component.

## Endpoints

| Endpoint | Role | Evidence |
| --- | --- | --- |
| `verifiable-computation/interactive-proofs` | supplies public-coin argument/verifier structure; GKR is the concrete tool | source `§3-§5` |
| `verifiable-computation/interactive-proofs/sum-check-protocol` | supplies the GKR layer reduction mechanism | source `§3`, appendices |
| `zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | uses the public-coin verifier as the component embedded in an outer SNARK | source `§4-§7` |

## Transfer Matrix

| From | To | Transfer | Boundary |
| --- | --- | --- | --- |
| public-coin verifier | recursive SNARK circuit | verify a compact public-coin proof inside an outer SNARK while the public-coin proof handles bulk computation | requires one-round/compiler-compatible public-coin argument |
| GKR/sum-check route | hash verification proving | batch many layered arithmetic hash computations with logarithmic verifier work | not a universal route for arbitrary circuits without suitable representation |
| SNARK verifier computation step | Fiat-Shamir transcript design | derive challenges from a short binding value instead of hashing the full statement in-circuit | requires a proof that the short value is tied to the hidden statement |
| Groth16 public-input MSM | statement binding | use the MSM contribution as the short statement commitment and prove its correctness | Groth16-specific instantiation; PLONK needs a modified transcript/public-input split |

## Non-Transfer Boundary

- Do not infer that every interactive proof can be embedded efficiently in every SNARK.
- Do not treat the concrete GKR instantiation as fully proven in the standard random oracle model; the source marks it heuristic after the one-round conversion.
- Do not infer a canonical definition of GKR or sum-check from this source alone.
- Do not transfer the MiMC benchmark speedups to Poseidon, Keccak, SHA256, PLONK, Halo2 or production systems without a dedicated source/benchmark.

## Evidence

| Source | Evidence | Confidence |
| --- | --- | --- |
| [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification]] `Abstract`, `§4-§6` | Defines the recursive technique, explains the full-transcript Fiat-Shamir bottleneck, and builds the short-input compiler. | high |
| Same source `§6` | Gives Groth16 binding through the verifier public-input computation/MSM and an auxiliary proof of correctness. | high |
| Same source `Appendix H-I` | Explains so-far digest and one-round GKR boundary, including the heuristic concrete instantiation. | high |

## Propagation Targets

- [[interactive-proofs|Interactive proofs]]
- [[sum-check-protocol|Sum-check protocol]]
- [[recursive-proof-composition|Recursive proof composition]]
- [[recursion-and-folding|Recursion and folding]]

## 连接命题

- From: `verifiable-computation/interactive-proofs`
- To: `zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition`
- Relation types: method_transfer, dependency, verification_embedding, fiat_shamir_boundary, performance_compression
- Directionality: `from_to`
- Relationship thesis: public-coin argument verifier embedding can make recursive proof composition practical for data-parallel hash verification when Fiat-Shamir is bound to a short SNARK-verifier computation value.

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| public-coin verifier inside SNARK | recursive proof composition | source `§4-§5` | verifier must be small enough and compiler-compatible |
| short Fiat-Shamir input via SNARK computation step | transcript/circuit design | source `§5-§6` | short value must be statement-binding |
| GKR for batched hash computations | prover-time optimization | source `§3`, `§8` | workload must fit layered/data-parallel arithmetic structure |

## 查询入口

- Public-coin interactive proofs -> recursive proof composition
- GKR inside SNARK
- public-coin proof recursion
- short Fiat-Shamir hash recursion

## 复核笔记

- Maturity: `active_seed`.
- Keep this bridge separate from [[polynomial-commitments-to-recursive-proof-composition|Polynomial commitments -> recursive proof composition]]: Halo transfers amortized PCS verification; this bridge transfers public-coin verifier embedding and transcript binding.

## 刷新规则

- Last checked: `2026-06-22`
- Valid until: `2026-07-22`
- Refresh triggers: new source changes public-coin recursion security proof, one-round GKR boundary, compatible SNARK verifier structures, Fiat-Shamir binding, or hash-verification benchmarks.

