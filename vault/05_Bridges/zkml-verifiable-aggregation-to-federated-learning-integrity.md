---
id: "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
title: "zkML verifiable aggregation -> federated learning integrity"
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
  - "verifiable-aggregation"
  - "federated-learning-integrity"
endpoint_knowledge_refs:
  - "nahida-knowledge-zkml-verifiable-aggregation"
  - "nahida-knowledge-federated-learning-integrity"
endpoint_paths:
  - "zero-knowledge-proofs/zkml/verifiable-aggregation"
  - "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
relation_types:
  - "application"
  - "integrity"
  - "verification_transfer"
  - "cross_domain_mapping"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
  - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
representative_source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
query_keys:
  - "zkML verifiable aggregation and federated learning integrity"
  - "ZK proofs for federated learning aggregator"
  - "zkFL problem mapping"
  - "PZKP-FL secure sum aggregation"
  - "RiseFL secure aggregation input validation"
  - "relaxed SAVI"
aliases:
  - "ZK aggregation proofs for FL integrity"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
topics:
  - "zkml"
  - "verifiable-aggregation"
  - "federated-learning-integrity"
tags:
  - "nahida/bridge"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation"
  - "nahida-knowledge-20260621-pzkp-fl"
  - "nahida-knowledge-20260623-risefl-low-cost-zkp"
source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
confidence: "high"
trust_tier: "primary"
---

# zkML verifiable aggregation -> federated learning integrity

## 关系命题

[[verifiable-aggregation|zkML verifiable aggregation]] 是 [[federated-learning-integrity|Federated learning integrity]] 的一条 cryptographic solution route: 用 commitments、signatures、secure sum、Sigma proofs、Bulletproofs-style bound proofs 或 zk-SNARK proofs 证明 global update 的来源、求和关系、secure-sum consistency 或 client update predicate，从而降低对 central aggregator、publisher 或 individual clients 的正确性信任。

这条 bridge 的转移边界很重要: ZKP 能验证“aggregate 是否等于这些 signed updates 的合法聚合”或“client update 是否满足公开 predicate”，但不能验证 predicate-passing updates 是否有毒、client selection 是否公平、local data 是否合规、模型是否会收敛或输出是否安全。RiseFL 还提醒一个负边界: 并非所有 verifiable aggregation 都应走 zkSNARK；secure aggregation 需要 commitment/additive-homomorphic compatibility 时，Sigma/Bulletproofs-style route 可能更合适。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[verifiable-aggregation|Verifiable aggregation]] | `zero-knowledge-proofs/zkml/verifiable-aggregation` | proof-system route for aggregation relation | zkML problem |
| [[federated-learning-integrity|Federated learning integrity]] | `ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | ML systems problem: malicious aggregator and aggregation auditability | ML systems problem |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `application` | ZKP aggregation proof is applied to an FL system problem | zkFL §I-§IV | active_seed |
| `integrity` | Proof prevents abandoned/replaced/inserted updates from passing verification | zkFL §V | active_seed |
| `verification_transfer` | Trust shifts from aggregator behavior to proof verification and circuit correctness | zkFL protocol | active_seed |
| `cross_domain_mapping` | ZKP node explains method; ML node preserves threat model and system boundaries | source classification correction | active_seed |
| `input_validation` | Proof checks client update predicate before secure aggregation | RiseFL §3-§5 | active_seed |

## Transfer Matrix

| From zkML verifiable aggregation | Transfers to FL integrity? | How | Boundary |
| --- | --- | --- | --- |
| Aggregation relation soundness | yes | invalid sum or fake commitments fail proof verification | only checks encoded relation |
| Commitment/signature binding | yes | ties local updates to client identities/statements | PKI/signature assumptions remain |
| Privacy toward external verifiers | partially | blockchain miners need not see plaintext updates | aggregator privacy not solved |
| Succinct verification | yes | clients/miners verify proof instead of reconstructing full witness | prover time and communication may dominate |
| Public audit trail | partially | chain stores hash of committed aggregate | finality/data availability are external assumptions |
| Secure-sum consistency | yes, in PZKP-FL route | Sigma proof binds secure-sum inputs to previously submitted modified local outputs | assumes Paillier/security-sum and smart contract execution |
| Probabilistic input validation | yes, in RiseFL route | Pedersen/VSSS/Sigma/Bulletproofs prove random-projection predicates and bounds before aggregation | relaxed SAVI allows slight out-of-bound pass probability; predicate-passing poisoning remains ML-specific |
| Commitment/additive homomorphism compatibility | yes, in RiseFL route | proof system is chosen around secure aggregation and Pedersen commitment homomorphism | ordinary zkSNARK bridge does not transfer here; proof-family choice is protocol-specific |

## Non-Transfer Boundary

- FL robustness against poisoned but valid client updates is outside this bridge.
- Secure aggregation privacy is outside this bridge unless a new source combines it.
- RiseFL combines secure aggregation and input validation, but does not make secure aggregation foundation complete for the whole vault.
- Model convergence, accuracy and fairness are not proven by aggregation correctness.
- Blockchain verification does not mean on-chain aggregation.
- The source-specific Halo2/Pedersen implementation is evidence, not the abstract bridge itself.
- zkSNARK-specific assumptions from zkFL do not transfer to RiseFL; RiseFL explicitly uses non-SNARK ZKP building blocks for its secure aggregation interface.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] §I | malicious aggregator problem in FL | source-authored threat model |
| zkFL §IV | base and blockchain protocol route | implementation/protocol-specific |
| zkFL §V | attack analysis and privacy boundary | aggregator model inversion future work |
| zkFL §VI | cost/accuracy/convergence evaluation | prototype, hardware, paper numeric caveats |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] §5.3 | secure sum, Paillier encryption, smart contract aggregation and Sigma consistency proof | local-training proof is primary; aggregation route is protocol-specific |
| PZKP-FL §7.2 | proof sketch for public verification of global aggregation | depends on smart contract and consensus assumptions |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|RiseFL]] §3.3 | relaxed SAVI formalizes privacy + probabilistic input integrity | input integrity is predicate/probability bounded, not strict semantic poisoning defense |
| RiseFL §4.3-§4.5 | hybrid Pedersen/VSSS commitment, ZKP proof generation/verification and secure aggregation | single-server, `m < n/2` malicious-client assumption |
| RiseFL §5-§6 | security/cost analysis and experiments vs RoFL/EIFFeL/ACORN | source-local implementation and benchmark caveats |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[verifiable-aggregation|Verifiable aggregation]] | Create zkML-side problem node | done |
| [[federated-learning-integrity|Federated learning integrity]] | Create ML systems-side problem node | done |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | Add FL integrity child route | done |
| [[ml-systems|ML systems]] | Create cold-start domain seed | done |
| [[verifiable-aggregation|Verifiable aggregation]] | Add non-SNARK secure aggregation input-validation route | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkml-verifiable-aggregation | applies_to | nahida-knowledge-federated-learning-integrity | zkFL §I-§V | high | active_seed |
| nahida-knowledge-federated-learning-integrity | bridges_to | nahida-knowledge-zkml-verifiable-aggregation | zkFL protocol | high | active_seed |
| nahida-knowledge-zkml-verifiable-aggregation | bridges_to | nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-federated-learning-integrity | bridges_to | nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-aggregation | applies_to | nahida-knowledge-federated-learning-integrity | RiseFL §3-§6 | high | active_seed |
| nahida-knowledge-federated-learning-integrity | evidenced_by | vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md | RiseFL source note | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| RoFL/ACORN/EIFFeL sources absorbed | Need compare strict check vs probabilistic check and Byzantine robustness | `nahida-update` |
| Secure aggregation source absorbed | May add privacy bridge or split privacy route | `nahida-update` |
| Blockchain FL implementation/repo analyzed | Need validate production feasibility and data availability assumptions | `nahida-github-repo-analyze` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Created cross-domain bridge between zkML verifiable aggregation and FL integrity using zkFL. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Added PZKP-FL secure-sum aggregation consistency route. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risefl-low-cost-zkp | Added RiseFL secure aggregation input-validation route and explicit non-SNARK transfer boundary. | 1 source note | codex |
