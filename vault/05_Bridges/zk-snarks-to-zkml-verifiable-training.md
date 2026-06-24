---
id: "nahida-bridge-zk-snarks-to-zkml-verifiable-training"
title: "zk-SNARKs -> zkML verifiable training"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
topic_ids:
  - "zk-snarks"
  - "zkml"
  - "verifiable-training"
endpoint_knowledge_refs:
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-zkml-verifiable-training"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/zkml/verifiable-training"
relation_types:
  - "application"
  - "verifiable_computation"
  - "privacy"
  - "training_integrity"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
representative_source_refs:
  - "arxiv:2304.05590v2"
query_keys:
  - "zk-SNARKs for verifiable ML training"
  - "Groth16 federated learning training proof"
  - "PZKP-FL"
  - "ZKP-FL"
aliases:
  - "SNARK-based verifiable training"
  - "Groth16-to-PZKP-FL"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
topics:
  - "zk-snarks"
  - "zkml"
  - "verifiable-training"
  - "federated-learning-integrity"
tags:
  - "nahida/bridge"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-pzkp-fl"
source_refs:
  - "arxiv:2304.05590v2"
  - "sha256:20bee0d6122e02ccd69ea2178675f4c51d9382fe40d1e95f63baf6b6ba267f7e"
confidence: "high"
trust_tier: "primary"
---

# zk-SNARKs -> zkML verifiable training

## 关系命题

zk-SNARKs can instantiate zkML verifiable training when the training computation is encoded as arithmetic-circuit constraints and the prover supplies a witness for local data plus intermediate training state. [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] uses Groth16 for each training piece, then adds Sigma-protocol continuity proofs so splitting the training process does not let a trainer splice inconsistent intermediate states.

This bridge does not mean a generic SNARK automatically makes ML training practical. It transfers soundness, succinct verification and zero-knowledge only to the encoded relation. Numeric semantics, circuit splitting, trusted setup, proof count, local-data privacy, model quality and deployment governance remain separate design constraints.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[zk-snarks|zk-SNARKs]] | `zero-knowledge-proofs/proof-systems/zk-snarks` | Groth16-style succinct argument for arithmetic circuit satisfiability | proof-system family |
| [[verifiable-training|Verifiable ML training]] | `zero-knowledge-proofs/zkml/verifiable-training` | proof that a model/training state was produced by a specified training algorithm and inputs | zkML problem |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `application` | Groth16 is applied to FL local-training pieces | PZKP-FL §5.1-§5.2 | active_seed |
| `verifiable_computation` | Publisher verifies training computation without rerunning local training | PZKP-FL §4-§5 | active_seed |
| `privacy` | Modified statements and ZK proofs hide local data/intermediate values | PZKP-FL §5.2, §7.3 | active_seed |
| `training_integrity` | Continuity Sigma proofs bind piece outputs to next-piece inputs | PZKP-FL Algorithm 2-3 | active_seed |

## Transfer Matrix

| From zk-SNARK/proof systems | Transfers to verifiable training? | How | Boundary |
| --- | --- | --- | --- |
| Soundness | yes | invalid per-piece circuit execution should fail verification | only for encoded circuit relation |
| Succinct verification | yes | verifier checks proofs rather than replaying local training | proof count can still be huge |
| Zero knowledge | yes, with protocol wrapper | proof hides witness and modified statements hide intermediate explicit values | numeric leakage and protocol metadata need separate care |
| Trusted setup | yes, as dependency | publisher runs Groth16 setup per piece/circuit | setup trust and CRS lifecycle are not solved |
| Arithmetic-circuit expressiveness | yes | training algorithm pieces become constraints | fractions/nonlinear ops need fixed-point/Taylor approximations |

## Non-Transfer Boundary

- Does not prove model accuracy, generalization, fairness, data legality, or resistance to poisoning.
- Does not make training proof cheap; PZKP-FL still produces many proofs and heavy setup/proving work.
- Does not by itself preserve FL privacy against all gradient-inference routes; the system also uses noise, secure sum and encryption.
- Does not remove blockchain finality, smart-contract correctness, or gas/deployment constraints.
- Does not settle numeric semantics for zkML broadly; fixed-point mapping and Taylor approximation are source-specific evidence.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] §5.1 | Training algorithm is split into identical pieces and converted to Groth16 circuits | source-authored design |
| Same source §5.2 | Modified statement/vk hides intermediate inputs and outputs while preserving verification equation | depends on noise handling |
| Same source Algorithm 2-3 | Sigma proofs bind modification and piece continuity | protocol wrapper, not plain Groth16 |
| Same source §6 | Fraction-Integer mapping and Taylor expansion make ML arithmetic circuit-friendly | approximation/scale trade-off |
| Same source §8 | Feasibility/cost in ZoKrates on small ML tasks | small tasks only |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[zk-snarks|zk-SNARKs]] | Add PZKP-FL as application-only verifiable-training source extension | done |
| [[verifiable-training|Verifiable ML training]] | Add neural-network/FL iterative training proof route | done |
| [[zkml|zkML]] | Refresh direction synthesis and source-extension row | done |
| [[federated-learning-integrity|Federated learning integrity]] | Connect local training verification to FL integrity through separate bridge | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zk-snarks | applies_to | nahida-knowledge-zkml-verifiable-training | PZKP-FL §5-§7 | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | depends_on | nahida-knowledge-zk-snarks | Groth16 local computation proof | high | active_seed |
| nahida-knowledge-zk-snarks | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-training | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-training | bridge note | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| RoFL or neural-network proof-of-training source absorbed | Compare threat model and proof relation | `nahida-update` |
| Numeric zkML/fixed-point/floating-point source absorbed | Decide whether to split a numeric semantics method node | `nahida-knowledge-get` |
| PZKP-FL implementation/repo appears | Validate protocol implementation architecture and cost claims | `nahida-github-repo-analyze` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Created bridge from zk-SNARKs/Groth16 to zkML verifiable training using PZKP-FL. | 1 source note | codex |
