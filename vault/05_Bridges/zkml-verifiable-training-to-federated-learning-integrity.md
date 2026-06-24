---
id: "nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity"
title: "zkML verifiable training -> federated learning integrity"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
topic_ids:
  - "zkml"
  - "verifiable-training"
  - "federated-learning-integrity"
endpoint_knowledge_refs:
  - "nahida-knowledge-zkml-verifiable-training"
  - "nahida-knowledge-federated-learning-integrity"
endpoint_paths:
  - "zero-knowledge-proofs/zkml/verifiable-training"
  - "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
relation_types:
  - "application"
  - "integrity"
  - "privacy"
  - "cross_domain_mapping"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
representative_source_refs:
  - "arxiv:2304.05590v2"
query_keys:
  - "verifiable federated training"
  - "PZKP-FL federated learning integrity"
  - "ZK proof of local FL training"
aliases:
  - "ZK training proofs for FL integrity"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
topics:
  - "zkml"
  - "verifiable-training"
  - "federated-learning-integrity"
  - "blockchain-verification"
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

# zkML verifiable training -> federated learning integrity

## 关系命题

[[verifiable-training|zkML verifiable training]] is a cryptographic route for one part of [[federated-learning-integrity|Federated learning integrity]]: proving that a participant's submitted local model parameters were computed by the agreed training algorithm over local data, rather than fabricated by a lazy trainer. PZKP-FL also combines this with secure-sum aggregation verification, so it maps both local-computation integrity and global-aggregation integrity into the FL system layer.

This bridge preserves the boundary between proof-system correctness and ML trustworthiness. A valid training proof says the encoded training relation was followed; it does not say the trainer's data are clean, representative, legal, non-poisoned, or that the resulting model is accurate or fair.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[verifiable-training|Verifiable ML training]] | `zero-knowledge-proofs/zkml/verifiable-training` | proof of training computation and intermediate-state continuity | zkML problem |
| [[federated-learning-integrity|Federated learning integrity]] | `ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | FL system problem: participants, aggregator and round state behave according to protocol | ML systems problem |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `application` | ZK training proof is applied to FL local computation | PZKP-FL §4-§5 | active_seed |
| `integrity` | Proof prevents lazy trainers from submitting arbitrary parameters that fail the training relation | PZKP-FL threat model and Theorem 1 | active_seed |
| `privacy` | Modified statements, ZK proofs and secure sum reduce local-data/intermediate leakage | PZKP-FL §5, §7.3 | active_seed |
| `cross_domain_mapping` | ZKP node explains proof mechanics; ML node preserves trainer/publisher threat model | source classification | active_seed |

## Transfer Matrix

| From zkML verifiable training | Transfers to FL integrity? | How | Boundary |
| --- | --- | --- | --- |
| Local training computation proof | yes | trainer supplies Groth16 proofs for training pieces | only checks encoded algorithm pieces |
| Piece continuity | yes | Sigma proofs bind previous output to next input | protocol-specific and proof-count heavy |
| Privacy of intermediate state | partially | noise-modified statements and ZK proofs hide explicit values from publisher | gradient leakage through other channels not fully covered |
| Global aggregation support | partially | secure sum + smart contract + Sigma proofs verify aggregation input consistency | production chain assumptions remain |
| Numeric adaptation | partially | fixed-point scaling and Taylor approximation allow practical ML operators | approximation affects exact ML semantics |

## Non-Transfer Boundary

- Does not solve malicious-client poisoning when the poisoned update is honestly trained.
- Does not prove data quality, representativeness, legality, fairness, convergence or model safety.
- Does not fully solve secure aggregation/privacy; it gives one masked secure-sum route under paper assumptions.
- Does not prove publisher/trainer incentive design, reward correctness, or production deployment feasibility.
- Does not make blockchain finality or smart-contract correctness internal to the proof system.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] §4.2 | lazy but curious trainer and unreliable publisher threat model | source-authored threat model |
| Same source §4.3 | three explicit goals: local computation verification, global aggregation verification, local data privacy | high-confidence classification |
| Same source §5 | ZKP-FL protocol combines Groth16, continuity proofs and secure sum | protocol-specific |
| Same source §7 | security proof sketches for local/global/privacy goals | depends on underlying assumptions |
| Same source §8 | practicality is shown on small ML tasks | not production-scale evidence |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[verifiable-training|Verifiable ML training]] | Add PZKP-FL as federated neural-network/iterative training proof route | done |
| [[federated-learning-integrity|Federated learning integrity]] | Add lazy-trainer local computation verification route | done |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | Add source extension row and bridge link | done |
| [[zkml|zkML]] | Add cross-domain bridge and source extension | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkml-verifiable-training | applies_to | nahida-knowledge-federated-learning-integrity | PZKP-FL §4-§7 | high | active_seed |
| nahida-knowledge-federated-learning-integrity | bridges_to | nahida-knowledge-zkml-verifiable-training | PZKP-FL protocol | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | bridges_to | nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-federated-learning-integrity | bridges_to | nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity | bridge note | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| RoFL or neural-network proof-of-training source absorbed | Compare local training proof, malicious clients and blockchain assumptions | `nahida-update` |
| Secure aggregation source absorbed | Separate privacy-preserving aggregation from training integrity | `nahida-update` |
| Large-model zkML training source absorbed | Revisit whether PZKP-FL's fixed-point/Taylor route generalizes | `nahida-knowledge-get` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Created bridge from zkML verifiable training to federated learning integrity using PZKP-FL. | 1 source note | codex |
