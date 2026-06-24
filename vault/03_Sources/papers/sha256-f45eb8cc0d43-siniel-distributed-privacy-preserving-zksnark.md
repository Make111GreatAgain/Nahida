---
id: "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
title: "Siniel: Distributed Privacy-Preserving zkSNARK"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
source_kind: "paper"
source_subtype: "local_pdf"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
paper_title: "Siniel: Distributed Privacy-Preserving zkSNARK"
authors:
  - "Yunbo Yang"
  - "Yuejia Cheng"
  - "Kailun Wang"
  - "Xiaoguo Li"
  - "Jianfei Sun"
  - "Jiachen Shen"
  - "Xiaolei Dong"
  - "Zhenfu Cao"
  - "Guomin Yang"
  - "Robert H. Deng"
year: "2024"
publication_date: "2024-11-11"
venue: "NDSS 2025 (to appear, stated in PDF)"
doi: ""
arxiv_id: ""
canonical_url: ""
local_pdf: "~/Desktop/paper/2024-1803.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/siniel-distributed-privacy-preserving-zksnark-f45eb8cc0d43-pages.txt"
sha256: "f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
page_count: 30
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "private-delegated-proving"
  - "distributed-proof-generation"
  - "zk-snarks"
  - "kzg-commitments"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "distributed-proof-generation"
  - "private-delegated-proving"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/sha256-f45eb8cc0d43"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation/sha256-f45eb8cc0d43"
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-f45eb8cc0d43"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments/sha256-f45eb8cc0d43"
  - "zero-knowledge-proofs/applications/blockchain-applications/sha256-f45eb8cc0d43"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "Title, abstract and Section 1 frame the durable problem as private delegation of zkSNARK prover computation."
  - "Sections 1.3 and 2.2 distinguish Siniel from distributed ZKP systems that do not hide witness shares."
  - "Sections 5-6 show the main reusable method is worker-side consistency checking for delegated PIOP/PCS proving."
source_relation_edges:
  - from: "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
    relation: "evidences"
    to: "nahida-knowledge-private-delegated-proving"
    confidence: "high"
    status: "active_seed"
  - from: "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
    relation: "evidences"
    to: "nahida-knowledge-distributed-proof-generation"
    confidence: "high"
    status: "active_seed"
  - from: "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
    relation: "evidences"
    to: "nahida-knowledge-kzg-commitments"
    confidence: "medium"
    status: "active_seed"
  - from: "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
    relation: "evidences"
    to: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    confidence: "high"
    status: "active_seed"
domains:
  - "zero-knowledge-proofs"
topics:
  - "Siniel"
  - "private delegated proving"
  - "privacy-preserving zkSNARK delegation"
  - "distributed zkSNARK provers"
  - "PIOP consistency checker"
  - "witness consistency checker"
  - "KZG commitments"
  - "Shamir secret sharing"
  - "authentication tags"
  - "honest-majority MPC"
aliases:
  - "Siniel"
  - "privacy-preserving zkSNARK delegation"
  - "private delegation of zkSNARK prover"
query_keys:
  - "Siniel distributed privacy-preserving zkSNARK"
  - "private delegated proving"
  - "zkSNARK prover delegation"
  - "non-interactive consistency checker"
  - "witness consistency checker"
  - "PIOP consistency checker"
  - "EOS zkSNARK delegation"
  - "zkSaaS"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "zk-snarks"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-siniel-private-delegated-proving"
source_refs:
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
confidence: "high"
trust_tier: "primary"
---

# Siniel: Distributed Privacy-Preserving zkSNARK

## Source Identity

| Field | Value |
| --- | --- |
| Title | Siniel: Distributed Privacy-Preserving zkSNARK |
| Authors | Yunbo Yang; Yuejia Cheng; Kailun Wang; Xiaoguo Li; Jianfei Sun; Jiachen Shen; Xiaolei Dong; Zhenfu Cao; Guomin Yang; Robert H. Deng |
| Date in PDF | 2024-11-11 |
| Venue statement | PDF states this is a preprint version and will appear in NDSS 2025. |
| Local PDF | `~/Desktop/paper/2024-1803.pdf` |
| SHA-256 | `f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552` |
| Pages | 30 |
| Metadata caveat | DOI/arXiv/canonical URL were not externally fetched in this run. |

## Reading Coverage

| Section | Pages | Coverage |
| --- | --- | --- |
| Abstract and Introduction | p1-p5 | Problem, contributions, use cases, related work, distinction from EOS/zkSaaS/DIZK/deVirgo/Pianist. |
| Technical Overview | p5-p9 | PIOP/PCS construction, EOS/zkSaaS baseline, Siniel architecture, threat examples, worker-side consistency checker idea. |
| Preliminaries | p10-p11 | Shamir secret sharing, authentication tags, Beaver triples, KZG, PIOP, zkSNARK construction. |
| Circuits for Common Operations | p12-p16 | Field/group gates, Reveal/RO/Output gates, PIOP circuits and KZG circuits. |
| Consistency Checkers | p14-p18 | Witness consistency checker and PIOP consistency checker protocols. |
| Siniel Construction | p17-p19 | Setup, offline phase, PIOP computation, proof generation. |
| Implementation and Performance | p20-p22 | Rust/arkworks/Marlin implementation, AWS setup, EOS comparison, bandwidth sensitivity. |
| References | p22-p24 | Prior work for EOS, zkSaaS, DIZK, deVirgo, Pianist, Marlin, KZG, MPC. |
| Appendices | p24-p30 | Beaver multiplication, ideal functionalities, security definitions, Theorem 1-3 proof sketches. |

## One-Sentence Memory

Siniel is a private delegated zkSNARK prover framework: a resource-limited delegator secret-shares its witness and offline authentication material to workers, then workers generate the PIOP/PCS proof and run witness/PIOP consistency checks themselves, so the delegator does not participate online while witness privacy and malicious-worker detection hold under an honest-majority, secure-with-abort model.

## Problem Setting

The paper starts from a practical zkSNARK bottleneck: proof generation requires large arithmetic circuits and high-degree polynomial operations such as FFT and MSM, which are hard for phones or other resource-constrained devices. The durable problem is not simply "distributed proving"; it is "private delegated proving": how can a weak delegator outsource prover work to stronger workers without revealing the private witness, without staying online throughout the proving phase, and while detecting malicious worker behavior.

The paper distinguishes four neighboring lines:

| Neighbor | Paper's distinction | Reusable lesson |
| --- | --- | --- |
| EOS | Stronger dishonest-majority style security, but delegator must participate in online consistency checks after PIOP rounds. | Security can be high, but delegator online interaction hurts usability. |
| zkSaaS | Outsources whole computation, but only semi-honest security under honest majority. | Full outsourcing alone is not enough if malicious workers are possible. |
| FHE-based delegation | Single untrusted server route, but homomorphic computation cost is high. | Witness privacy can be achieved without multi-worker MPC, but practicality is a separate axis. |
| DIZK/deVirgo/Pianist | Distributed ZKP scales prover work but does not hide each worker's witness share/plain witness portion. | Prover scalability and witness privacy are complementary axes. |

## Contributions

| Contribution | What It Adds | Evidence Anchor | Reusable Placement |
| --- | --- | --- | --- |
| General private delegation framework for zkSNARK provers | Applies to zkSNARKs built from PIOP + PCS; delegator can outsource prover computation to workers without leaking witness. | p1-p3, p5-p9 | [[private-delegated-proving|Private delegated proving]] |
| No delegator online interaction | Delegator performs offline sharing/authentication setup, then workers execute online computation and checks. | p3, p6-p9, p17-p19 | [[distributed-proof-generation|Distributed proof generation]] as privacy-aware subroute |
| Worker-side consistency checking | Witness consistency checker and PIOP consistency checker move malicious-behavior detection from delegator to workers. | p8-p9, p14-p18 | [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] |
| Malicious-worker security under honest majority | Uses Shamir secret sharing, authentication tags, Beaver triples, KZG openings, and secure-with-abort model. | p10-p11, p25-p30 | Source-local proof evidence |
| Implementation and evaluation | Rust/arkworks implementation over Marlin, comparing Siniel with EOS under different circuit sizes and bandwidths. | p20-p22 | Source-local benchmark evidence |

## System Model And Threat Boundary

Siniel has one delegator `D` and `n = 2t + 1` workers. The security model is honest majority with secure abort: no more than `t` workers collude or behave maliciously, and the protocol aborts if malicious behavior is detected. The paper explicitly says this is weaker than EOS's dishonest-majority setting, but argues it is sufficient for many decentralized systems that already assume honest-majority-style thresholds.

The delegator is honest in the offline phase. It distributes:

- Shamir shares of the private witness.
- Shares of `w(alpha)` and `alpha` for witness consistency checking.
- Authentication tags for witness shares and Beaver triples.
- Shares of authentication keys to other workers.
- Public instance `x` and enough Beaver triples for private multiplications.

After this, the delegator does not interact during the online proving phase. This is the main usability difference from EOS.

## Mechanism Detail

### PIOP + PCS Setting

Siniel targets zkSNARKs that follow the common PIOP + PCS + Fiat-Shamir design. The prover turns the relation into polynomial constraints, runs a PIOP prover to emit prover polynomials, commits to them using a PCS, opens them at verifier challenge points, and applies Fiat-Shamir for non-interactivity. The implementation focuses on KZG commitments, but the problem formulation is broader than one source system.

### Three Chunks Of Delegated Proving

The paper divides the delegated computation into:

1. Inputs to the PIOP circuit: workers receive witness shares and public instance.
2. PIOP computation: workers compute shares of prover polynomials and commitments.
3. Proof generation: workers evaluate prover polynomials, create opening proofs, reconstruct final proof, and verify it before returning it.

The attacks map exactly to these chunks: inconsistent witness-share commitments, altered inputs during PIOP computation, deviation from the PIOP protocol, inconsistent commitments to prover polynomials, and invalid final proofs.

### Witness Consistency Checker

The witness consistency checker verifies that commitments to witness shares are consistent with the actual shares. The delegator precomputes a random point `alpha`, `w(alpha)`, and shares of those values. Workers compute KZG openings for their witness-share polynomial at `alpha`, aggregate the commitments/evaluations/opening proofs, reconstruct `w(alpha)`, and check equality plus `KZG.Verify`.

This checker gives workers a way to validate witness-share consistency without asking the delegator online.

### PIOP Consistency Checker

The PIOP consistency checker verifies that a worker's prover polynomials are:

- consistent with the worker's authenticated witness share,
- correctly produced by the PIOP circuit,
- consistent with the public commitments to those prover polynomials.

The mechanism uses authentication tags of the form `tau = mu * share + v`. A worker holding a share and tag can update tags during linear operations, and other workers holding authentication-key shares can update corresponding keys. For multiplication, Siniel uses Beaver multiplication with authentication tags. At check time, other workers challenge the prover worker at a random `beta`, verify the tag equation at `f(beta)`, and use KZG opening verification to bind the evaluation to the committed polynomial.

### KZG Role

KZG is not the whole contribution. Its reusable role is as the commitment/opening layer that binds witness/prover polynomials to later consistency checks. The bridge-level lesson is: private delegated proving needs a commitment scheme whose openings let workers validate consistency of shared polynomial computation without giving the delegator an online verification role.

## Formal Evidence

| Formal Item | What It Supports | Evidence Anchor |
| --- | --- | --- |
| Witness consistency checker ideal functionality | Correctness of commitments to input shares and `w(alpha)` consistency. | Appendix B, Fig. 14, p25 |
| Theorem 1 | Witness consistency checker securely implements `F_wcc`. | Appendix D, p26-p27 |
| PIOP consistency checker ideal functionality | Correctness of PIOP computation, share authentication, and commitment consistency. | Appendix B, Fig. 15, p25 |
| Theorem 2 | PIOP consistency checker securely implements `F_pcc`. | Appendix E, p27 |
| Siniel ideal functionality | Delegated SNARK proof generation with honest-majority secure abort and witness hiding against up to `t` colluding workers. | Appendix C, Fig. 16, p25-p26 |
| Theorem 3 | Siniel securely implements `F_SNARK` in the `F_wcc`, `F_pcc` hybrid model with at most `t` corruptions and `n=2t+1` workers. | Appendix F, p27-p30 |

## Implementation And Evaluation

| Area | Source-Local Detail | Caveat |
| --- | --- | --- |
| Implementation | Rust implementation built on arkworks and Marlin; modifies arkworks to support Shamir sharing, shared group/scalar operations, Beaver multiplication, and shared polynomial arithmetization. | The PDF names arkworks/Marlin but does not provide a Siniel repository URL in the extracted text. |
| Deployment | One AWS `c5a.4xlarge` delegator and three AWS `c5a.8xlarge` workers. | Three workers is the minimum honest-majority setup and not necessarily optimal for all deployments. |
| Workload | Private delegation of Marlin prover for circuit sizes `2^12` to `2^20`; bandwidths 10MBps, 100MBps, 1000MBps; average over ten runs. | Only Marlin/arkworks route is evaluated. |
| Delegator cost | For circuit size `2^20` at 10MBps, Siniel reports 419s vs naive Marlin 1549s and EOS 503s. | Source-local hardware/network and implementation. |
| Abstract example | For SHA256 compression, abstract reports 6.5s vs EOS 8.8s at 10MBps; 0.17s vs EOS 2.07s at 1000MBps. | The precise circuit setting is source-local. |
| Worker cost | At circuit size `2^20`, workers spend about 130s for Siniel vs 400s for EOS at 10MBps, but 79s for Siniel vs 70s for EOS at 1000MBps. | Siniel worker-side checkers add work; low-bandwidth gains come partly from removing delegator waiting. |

## Evidence Table

| Claim / Finding | Anchor | Confidence | Handling |
| --- | --- | --- | --- |
| Siniel solves private delegation of zkSNARK prover computation, not generic SNARK foundation. | p1-p3, p5-p9 | high | primary classification |
| The delegator can stop interacting after offline material distribution. | p3, p6, p17-p19 | high | source extension to private delegated proving |
| Siniel is weaker than EOS in corruption threshold but improves usability/efficiency. | p4-p5, p21-p22 | high | boundary condition |
| Distributed ZKP systems like DIZK/deVirgo/Pianist are complementary because they do not hide witness portions from machines. | p4-p5 | high | parent-node comparison |
| KZG opening verification is used by both witness and PIOP consistency checks. | p10-p18 | high | bridge evidence |
| Performance gains depend on bandwidth and role; worker-side cost can be higher than EOS at high bandwidth. | p20-p22 | high | benchmark caveat |

## Knowledge Handoff

| Target | Handling | Delta |
| --- | --- | --- |
| [[private-delegated-proving|Private delegated proving]] | create seed/foundation-thin child node | Reusable subproblem: outsource proving while hiding witness and reducing delegator online work. |
| [[distributed-proof-generation|Distributed proof generation]] | update parent method-family | Add privacy-preserving delegated proving as a child/route distinct from DIZK/deVirgo/Pianist/Hekaton scaling routes. |
| [[kzg-commitments|KZG commitments]] | source extension and bridge endpoint | KZG openings support worker-side consistency checks in Siniel. |
| [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] | create bridge | Records how KZG commitment/opening semantics enable consistency checking without delegator online participation. |
| [[zk-snarks|zk-SNARKs]] | source-only/indirect | Siniel is a zkSNARK prover-delegation framework; no need to redefine zk-SNARKs. |

## Cold-Start Hierarchy Discovery

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `zero-knowledge-proofs` | Title, abstract, PIOP/PCS/KZG/zkSNARK construction | high | existing domain |
| Research background | Expensive zkSNARK proving on constrained devices; PIOP + PCS proof-system architecture | p1-p3, p5-p6 | high | parent/child knowledge background |
| Research problem | `private-delegated-proving` | Problem statement asks for no delegator online interaction, lightweight delegator operations, malicious-worker security | high | new child knowledge node |
| Foundation concepts | zk-SNARKs, PIOP, PCS, KZG commitments, Shamir secret sharing, authentication tags, Beaver triples | p5-p11 | high | source note + bridge/foundation gaps |
| Method family | Honest-majority MPC with worker-side consistency checking for delegated proving | p6-p19 | high | knowledge node method route |
| Application/evaluation context | Private payments, dApps/DID, Marlin prover benchmarks, AWS worker setup | p3-p4, p20-p22 | medium | source-local/application hints |
| Artifact/source instance | Siniel | entire paper | high | source extension / representative source |

## Retrieval Optimization

- Future queries helped: "怎样把 zkSNARK prover 外包但不泄露 witness?", "Siniel 和 EOS/zkSaaS/DIZK/Pianist 有什么区别?", "KZG 在 delegated proving 里起什么作用?", "distributed proving 是否保护 worker 看到的 witness?"
- Source reads avoided: future agents can read [[private-delegated-proving|Private delegated proving]] for the reusable problem and only open this source for exact protocol/evaluation details.
- Source-only content: exact circuit gate definitions, authentication-key distribution details, appendix simulator steps, AWS timings, and line-by-line protocol figures remain here.
- Foundation gaps: EOS, zkSaaS, collaborative zkSNARKs, and DIZK primary sources are needed before upgrading the child node from `foundation_thin`.

## Domain Dynamics Impact

`zero-knowledge-proofs/research-dynamics.md` remains unchanged. Siniel adds a narrow proof-system subproblem and a bridge to KZG commitments, but one source does not materially change domain-level research dynamics.

## Review Items

| Type | Item | Status |
| --- | --- | --- |
| metadata_gap | Canonical URL/DOI/open repository for Siniel was not externally fetched. | review |
| foundation_gap | EOS, zkSaaS, Ozdemir/Boneh collaborative zkSNARKs and DIZK primary sources are needed to mature private delegated proving. | queued |
| classification_correction | Queue path `proof-system-foundations` was corrected to `distributed-proof-generation/private-delegated-proving`. | recorded |
| benchmark_scope | Performance values are source-local to Marlin/arkworks, AWS c5a instances, three workers, and selected bandwidths. | recorded |

