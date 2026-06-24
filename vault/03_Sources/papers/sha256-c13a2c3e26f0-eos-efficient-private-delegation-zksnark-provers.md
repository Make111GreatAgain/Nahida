---
id: "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
title: "EOS: Efficient Private Delegation of zkSNARK Provers"
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
paper_title: "EOS: Efficient Private Delegation of zkSNARK Provers"
authors:
  - "Alessandro Chiesa"
  - "Ryan Lehmkuhl"
  - "Pratyush Mishra"
  - "Yinuo Zhang"
year: "2023"
publication_date: "2023-08"
venue: "32nd USENIX Security Symposium"
doi: ""
arxiv_id: ""
canonical_url: "https://www.usenix.org/conference/usenixsecurity23/presentation/chiesa"
local_pdf: "~/Desktop/paper/usenixsecurity23-chiesa.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/usenixsecurity23-chiesa-c13a2c3e26f0-pages.txt"
sha256: "c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
page_count: 18
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "private-delegated-proving"
  - "distributed-proof-generation"
  - "zk-snarks"
  - "piop-based-zksnark-delegation"
  - "kzg-commitments"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "distributed-proof-generation"
  - "private-delegated-proving"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/sha256-c13a2c3e26f0"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation/sha256-c13a2c3e26f0"
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-c13a2c3e26f0"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments/sha256-c13a2c3e26f0"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "The queue title was USENIX proceedings boilerplate; page 1 and paper page 2 identify the paper as EOS: Efficient Private Delegation of zkSNARK Provers."
  - "Abstract, Introduction and Sections 2-6 frame the durable problem as privacy-preserving delegation of universal-setup zkSNARK proving."
  - "Sections 4-5 and 6.3 show the reusable method: efficient MPC circuits for PIOP/PCS prover operations plus PIOP consistency checking."
source_relation_edges:
  - from: "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
    relation: "evidences"
    to: "nahida-knowledge-private-delegated-proving"
    confidence: "high"
    status: "active_seed"
  - from: "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
    relation: "evidences"
    to: "nahida-knowledge-distributed-proof-generation"
    confidence: "high"
    status: "active_seed"
  - from: "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
    relation: "evidences"
    to: "nahida-knowledge-zk-snarks"
    confidence: "medium"
    status: "active_seed"
  - from: "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
    relation: "evidences"
    to: "nahida-knowledge-kzg-commitments"
    confidence: "medium"
    status: "active_seed"
  - from: "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
    relation: "evidences"
    to: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    confidence: "high"
    status: "active_seed"
domains:
  - "zero-knowledge-proofs"
topics:
  - "EOS"
  - "Efficient Outsourcing of SNARKs"
  - "private delegated proving"
  - "privacy-preserving zkSNARK delegation"
  - "universal-setup zkSNARKs"
  - "PIOP consistency checker"
  - "additive secret sharing"
  - "KZG commitments"
  - "MARLIN"
  - "malicious workers"
aliases:
  - "Eos"
  - "Efficient Outsourcing of SNARKs"
  - "private delegation of zkSNARK provers"
  - "witness-hiding prover delegation"
query_keys:
  - "EOS Efficient Private Delegation of zkSNARK Provers"
  - "Efficient Outsourcing of SNARKs"
  - "private delegated proving"
  - "universal setup zkSNARK delegation"
  - "PIOP consistency checker"
  - "isolated delegated SNARK protocol"
  - "collaborative delegated SNARK protocol"
  - "malicious worker zkSNARK delegation"
  - "EOS vs Siniel"
  - "EOS vs OB22 collaborative zkSNARKs"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "zk-snarks"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-eos-private-delegated-proving"
source_refs:
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
confidence: "high"
trust_tier: "primary"
---

# EOS: Efficient Private Delegation of zkSNARK Provers

## Source Identity

| Field | Value |
| --- | --- |
| Title | EOS: Efficient Private Delegation of zkSNARK Provers |
| Authors | Alessandro Chiesa; Ryan Lehmkuhl; Pratyush Mishra; Yinuo Zhang |
| Venue | 32nd USENIX Security Symposium, 2023 |
| Canonical URL | `https://www.usenix.org/conference/usenixsecurity23/presentation/chiesa` |
| Local PDF | `~/Desktop/paper/usenixsecurity23-chiesa.pdf` |
| SHA-256 | `c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4` |
| Pages | 18 |
| Metadata caveat | Queue metadata used USENIX cover-page boilerplate as the title. The corrected title/authors/venue come from the paper title page and body text. |

## Reading Coverage

| Section | Pages | Coverage |
| --- | --- | --- |
| USENIX cover and title page | p1-p2 | Corrected noisy metadata; identified title, authors, venue, URL. |
| Abstract and Introduction | p2-p3 | Problem, threat model, contribution summary, smartphone/cloud motivation. |
| Related Work | p3-p4 | Comparison with Trinocchio, Kanjalkar et al., OB22 collaborative proving, DIZK-like distributed proving, FHE/other routes. |
| Construction Overview | p4-p5 | Delegator/worker roles, preprocessing vs online phase, isolated vs collaborative modes, witness reduction boundary. |
| Preliminaries | p5-p6 | Circuit model, additive sharing, polynomial commitments, PIOP + PCS zkSNARK structure. |
| Efficient Circuits | p6-p8 | Low-depth circuits for FFT/IFFT, polynomial arithmetic, group arithmetic and KZG PC operations. |
| PIOP Consistency Checkers | p8-p9 | Definition, MARLIN checker, random-point witness LDE check, soundness intuition. |
| Delegated SNARKs | p9-p10 | Delegated SNARK definition, ideal functionality, protocol construction and theorem. |
| Implementation | p10-p11 | Rust/arkworks EOS library, abstractions, optimizations for parallelism, communication and memory. |
| Evaluation | p11-p14 | Laptop/mobile setups, larger-instance results, end-to-end time, delegator online time, preprocessing and communication, OB22 comparison. |
| Proof Appendices | p17-p18 | Simulation, leakage argument, correctness/soundness boundary, MARLIN consistency checker details. |

## One-Sentence Memory

EOS is a delegated zkSNARK proving framework for universal-setup PIOP+PCS systems: a weak delegator secret-shares the witness to multiple powerful workers, and as long as at least one worker is honest the workers can produce a proof without learning the witness, while malicious deviations are checked through delegation-specific PIOP/PCS consistency checks.

## Problem Setting

The paper targets the prover bottleneck of zkSNARKs. Verification is succinct, but proving requires arithmetizing a relation into a large circuit and then doing polynomial and group operations whose cost is at least linear in the circuit size. A phone, browser client or ordinary user machine may be able to hold the witness but unable to run the prover fast enough or with enough memory. Sending the witness to a cloud machine would solve resource pressure but breaks the privacy goal of applications such as private payments, anonymous credentials and private smart contracts.

The durable problem is therefore not generic distributed proving. It is private delegated proving for zkSNARKs: the delegator wants cloud-scale prover resources while retaining witness privacy and still detecting malicious workers. EOS makes this concrete for universal-setup zkSNARKs built from a polynomial interactive oracle proof and a polynomial commitment scheme.

## Threat Model And Protocol Shape

EOS has one honest delegator `D` and `n` remote workers. The delegator performs witness reduction locally, then secret-shares the low-level witness and proving randomness. Privacy holds if at least one worker is honest and does not collude with the others. Dishonest workers may deviate arbitrarily, so the protocol must prevent invalid or witness-leaking proof-generation behavior from being accepted.

The protocol has two operational modes:

| Mode | Communication Pattern | Security/Usability Meaning |
| --- | --- | --- |
| Isolated | Workers communicate only with the delegator. | Stronger operational isolation: workers need not know or talk to one another, but delegator online work and communication are higher. |
| Collaborative | Workers communicate directly with one another and the delegator. | Better latency/communication for many settings, but workers are aware of one another and network assumptions are stronger. |

Both modes are split into preprocessing and online phases. Preprocessing is witness-independent; online work starts after the delegator provides public input and secret shares of the witness. The paper is explicit that the delegator still performs witness reduction locally: compiling high-level witness generation itself into MPC could cost more than just doing that reduction on the weak client.

## Main Contributions

| Contribution | What It Adds | Evidence Anchor | Reusable Placement |
| --- | --- | --- | --- |
| Delegation protocol for PIOP+PCS zkSNARKs | Builds a private delegation layer for popular universal-setup zkSNARK architecture. | Abstract; §1.1; §6 | [[private-delegated-proving|Private delegated proving]] |
| Delegation-specific MPC | Starts from SPDZ-style ideas but uses an honest delegator and specialized consistency checks to remove heavyweight public-key cryptography and authenticated-share overhead in the hot path. | §2.2; §6.3 | source-local mechanism |
| PIOP consistency checker | Checks that worker-produced polynomial oracles match what the honest PIOP prover would produce for the same witness and verifier messages. | §5; Appendix B | [[private-delegated-proving|Private delegated proving]] |
| Efficient circuits for prover operations | Gives low-depth circuits for PIOP polynomial arithmetic and KZG commitment/opening operations, so MPC execution is not forced through a naive generic circuit. | §4 | [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] |
| EOS Rust library | Generalizes arkworks-style plaintext PIOP/PC code to secret-shared field elements and polynomials; instantiates the approach for a MARLIN-like zkSNARK. | §7 | implementation evidence, source-local |
| Mobile/cloud evaluation | Shows smartphone/laptop delegation can prove larger instances and reduce end-to-end latency and delegator online time. | §8 | benchmark evidence, source-local |

## Mechanism Detail

### Why Generic MPC Is Not Enough

A strawman would run the entire zkSNARK prover inside a malicious-secure MPC protocol. EOS argues this is too expensive because generic malicious MPC would pay for public-key cryptography, authentication machinery and circuitized elliptic-curve/polynomial work that the prover already has efficient algebraic structure for. EOS instead uses the delegator as a source of correlated randomness in preprocessing and relies on proof-system-specific consistency checks.

This specialization is also why final SNARK verification is not sufficient by itself. A malicious worker could alter witness-dependent polynomials in ways that reveal a bit of the witness through whether the final proof accepts or rejects. EOS adds consistency checking before accepting the worker computation so the delegator does not use final validity as an accidental leakage channel.

### PIOP + PCS Target

EOS targets zkSNARKs with this shape:

1. A PIOP prover produces polynomial oracles over an arithmetized relation.
2. A polynomial commitment scheme commits to those polynomials and later proves evaluations.
3. Fiat-Shamir turns the interaction into a non-interactive SNARK.

The concrete implementation follows the PIOP/PC structure behind MARLIN and uses KZG-style commitment/opening circuits. The reusable classification is broader than MARLIN, but the performance evidence is source-local to this implementation route.

### Efficient Circuits For Prover Work

The paper identifies prover operations whose secret-shared computation is much cheaper than a generic circuit would suggest:

| Operation Family | EOS Observation | Delegation Effect |
| --- | --- | --- |
| FFT/IFFT and linear polynomial operations | Linear over the field, so they do not require multiplication depth in the secret-shared circuit. | Round complexity and MPC cost stay low. |
| Polynomial multiplication | Can be implemented via FFT, pointwise multiplication and IFFT; the private multiplications concentrate in one pointwise phase. | Avoids deep generic multiplication circuits. |
| KZG commitment and opening | Multi-scalar multiplication and group operations can be handled with linear structure; commitment/opening circuits avoid unnecessary private multiplication depth. | Makes PIOP/PCS prover work delegatable rather than only theoretically expressible in MPC. |

### PIOP Consistency Checker

The checker asks whether polynomial oracles supplied by the delegated prover are the same oracles that the honest prover would have emitted under the same verifier messages. For the MARLIN-style PIOP, the delegator samples a random point and compares:

- a local evaluation of the witness low-degree extension at that point, computed in `O(|w|)` field work, with
- the worker-opened evaluation of the committed witness polynomial at the same point.

Other prover polynomials are covered by the PIOP verifier and holographic lincheck structure. The key idea is that the delegator checks a small, targeted consistency relation rather than recomputing the whole prover.

### Isolated And Collaborative Multiplication

Private multiplications are handled differently in the two modes:

| Mode | Multiplication Handling | Consequence |
| --- | --- | --- |
| Isolated | Workers send shares to the delegator; the delegator reconstructs and reshares the product. | More delegator communication and online presence, but no direct worker-worker channel. |
| Collaborative | Workers use preprocessing triples and communicate among themselves. | Less delegator online work and better performance where worker-worker links are available. |

## Formal Evidence

| Formal Item | What It Supports | Evidence Anchor |
| --- | --- | --- |
| Delegated SNARK ideal functionality | Defines what it means for a weak delegator to outsource proving to workers while receiving either a valid proof or abort. | §6.2 |
| Theorem 6.1 | Shows the delegated protocol realizes the desired delegation for PIOP-based zkSNARKs under the stated circuit/checker assumptions. | §6.3 |
| Simulator proof sketch | Corrupted workers learn shares consistent with simulated witness values; linear/multiplication/RO/reveal gates do not expose the real witness beyond allowed outputs. | Appendix A |
| Consistency soundness argument | Rejection or incorrect output would imply failure of the PIOP consistency checker, PC evaluation/randomness binding, PC extractability or SNARK soundness. | Appendix A |
| MARLIN checker algorithm | Gives the concrete random-point check for the witness LDE and relies on MARLIN completeness plus holographic lincheck soundness. | Appendix B |

## Implementation And Evaluation

| Area | Source-Local Detail | Caveat |
| --- | --- | --- |
| Implementation | Rust library built around arkworks abstractions for secret-shared field elements and polynomials. | The PDF names the library but this run did not inspect a repository. |
| Target SNARK | Instantiates the PIOP + PC approach for a MARLIN-like universal-setup zkSNARK. | Exact generality beyond that implementation remains source-stated, not independently verified. |
| Delegator environments | Midgrade laptop emulation and Google Pixel 4a mobile setup. | Hardware/network details are source-local and should not be treated as universal speedups. |
| Workers | Two large AWS workers in separate regions/trust domains. | Economic/trust-domain assumptions are evaluation setup choices. |
| Larger instances | For the same time or memory budget, delegation lets weak clients handle substantially larger R1CS sizes; the abstract reports up to 256x larger instances under a memory budget. | The improvement depends on witness streaming, worker memory and network. |
| End-to-end latency | Mobile collaborative mode reports up to 26x latency reduction over local proving. | Preprocessing is excluded because it is witness-independent and can be amortized. |
| Delegator online work | The paper reports large reductions in active online computation, up to 1447x. | Online time is a role-specific metric and should not be confused with total worker CPU cost. |
| OB22 comparison | EOS is reported 6-8x faster and uses less communication than OB22-style collaborative proving in the tested setting. | Comparison is tied to the authors' implementations and configurations. |

## Comparisons And Boundaries

| Neighbor | EOS Position | Knowledge Handling |
| --- | --- | --- |
| Trinocchio | Circuit-specific setup and Shamir/MPC route with different corruption assumptions and semi-honest boundary. | historical related work; not absorbed as source here |
| OB22 collaborative proving | Similar high-level collaborative-proving goal but uses heavier information-theoretic MAC machinery; EOS reports lower cost. | source-local comparison; no separate source note yet |
| DIZK | Distributes prover work but does not hide witness portions from machines. | belongs under [[distributed-proof-generation|Distributed proof generation]], not private delegation by itself |
| Siniel | Later source removes delegator online interaction by moving consistency checks to workers, but weakens/changes adversary model to honest majority secure-with-abort. | compare in [[private-delegated-proving|Private delegated proving]] |
| FHE-based single-server delegation | Hides witness from one server but with high computation overhead in this paper's framing. | watchlist/foundation gap |

## Evidence Table

| Claim / Finding | Anchor | Confidence | Handling |
| --- | --- | --- | --- |
| Corrected title is EOS, not USENIX proceedings boilerplate. | cover/title page | high | metadata correction |
| EOS addresses private delegation of zkSNARK prover computation for PIOP+PCS universal-setup systems. | Abstract; §1; §2 | high | primary classification |
| Privacy holds against worker collusion as long as at least one worker is honest. | Abstract; §2; Appendix A | high | threat model |
| Malicious worker behavior is handled without generic heavyweight crypto by specialized PIOP/PCS consistency checking. | §2.2; §5; §6 | high | method route |
| KZG/PC opening machinery is used as part of the delegated prover/checker design, but it is not the entire private-delegation protocol. | §3.3; §4.3; §6.3 | medium | bridge update |
| EOS remains online-interactive for the delegator, especially compared with Siniel's later worker-side checking route. | §2; §6; Siniel comparison already in vault | high | taxonomy update |
| Benchmark gains are significant on weak clients but source-local to MARLIN/arkworks, AWS workers and selected networks. | §8 | high | benchmark caveat |

## Knowledge Handoff

| Target | Handling | Delta |
| --- | --- | --- |
| [[private-delegated-proving|Private delegated proving]] | update existing node | Replace the prior "EOS primary source missing" gap with a source-backed EOS route: strong worker-collusion privacy with delegator online consistency checks. |
| [[distributed-proof-generation|Distributed proof generation]] | update parent method family | Clarify EOS as privacy-preserving delegated proving, distinct from cluster/data-parallel distributed prover scaling. |
| [[zk-snarks|zk-SNARKs]] | source extension only | EOS is a prover-delegation engineering source for universal-setup SNARKs, not a foundation definition source. |
| [[kzg-commitments|KZG commitments]] | source extension only | Adds another KZG/PC usage: commitment/opening circuits and checker binding inside private delegated proving. |
| [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] | refresh bridge | EOS shows the same dependency from a different angle than Siniel: PC/KZG operations help make delegated PIOP consistency checkable. |

## Cold-Start Hierarchy Discovery

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `zero-knowledge-proofs` | zkSNARK/PIOP/PCS/KZG throughout | high | existing domain |
| Durable problem | `private-delegated-proving` | Abstract and construction focus on private delegation of proof generation | high | existing child node |
| Parent method family | `distributed-proof-generation` | Multiple workers jointly compute a proof, but with witness privacy | high | existing parent |
| Foundation concepts | zk-SNARKs, PIOP, PCS, KZG commitments, additive secret sharing, MPC triples | §§3-4 | high | source note plus knowledge links |
| Method route | PIOP consistency checking with isolated/collaborative MPC execution | §§5-6 | high | update method table |
| Source instance | EOS | entire paper | high | representative source |

## Retrieval Optimization

- Future queries helped: "EOS zkSNARK delegation", "private delegation of zkSNARK provers", "worker cannot learn witness but cloud proves SNARK", "Siniel vs EOS", "PIOP consistency checker", "KZG in delegated proving".
- Source reads avoided: future agents can start at [[private-delegated-proving|Private delegated proving]] for the taxonomy and only open this source for EOS-specific protocol or benchmark details.
- Source-only content: exact pseudocode in Figure 3/Figure 4, line-by-line gate semantics, all evaluation plots and low-level appendix simulator cases remain here.
- Classification correction: queue path `proof-system-foundations` was narrowed to `distributed-proof-generation/private-delegated-proving`; KZG and zk-SNARKs are secondary paths.

## Domain Dynamics Impact

This paper does not change the whole zero-knowledge-proofs research-dynamics note by itself. It closes a queued foundation gap inside private delegated proving and strengthens the local taxonomy around outsourced prover privacy.

## Review Items

| Type | Item | Status |
| --- | --- | --- |
| metadata_correction | Queue title was noisy USENIX boilerplate; title/authors/year/venue corrected from the PDF. | done |
| source_gap | DOI/arXiv were not present in the PDF extraction and were not externally fetched. | recorded |
| implementation_gap | EOS repository/code artifact was not analyzed in this paper-intake turn. | queued_if_repo_known |
| comparison_gap | OB22 collaborative zkSNARKs and zkSaaS primary sources remain unabsorbed. | queued |
| benchmark_scope | Performance values are source-local to MARLIN/arkworks, selected AWS/mobile devices and networks. | recorded |
