---
id: "iacr-eprint-2019-1021"
title: "Recursive Proof Composition without a Trusted Setup"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1-p4 abstract, introduction, motivation for IVC, prior recursive proof composition, contributions and concurrent work"
  - "p5-p6 preliminaries for zero-knowledge arguments of knowledge and groups"
  - "p7-p10 inner-product-style polynomial commitment, opening protocol and amortization strategy"
  - "p10-p11 nested amortization strategy for recursive proof composition"
  - "p11-p16 Sonic-adapted main argument for arithmetic circuit satisfiability"
  - "p16-p21 Fiat-Shamir implementation, Tweedledum/Tweedledee curve cycle, endomorphism optimizations, evaluation and conclusion"
  - "p22-p31 references and appendices for protocol proofs and endomorphism correctness"
canonical_url: "https://eprint.iacr.org/2019/1021"
pdf_url: "https://eprint.iacr.org/2019/1021.pdf"
doi: ""
arxiv_id: ""
venue: "IACR ePrint 2019/1021; local PDF revision metadata 2020"
year: "2020"
authors:
  - "Sean Bowe"
  - "Jack Grigg"
  - "Daira Hopwood"
affiliations:
  - "Electric Coin Company"
local_pdf: "~/Desktop/paper/2019-1021.pdf"
sha256: "6814cb0cb866cdfe3af135c0edf4626a266b92e916edef9132c3912f7decbe0e"
pages: 31
pdf_extractor: "pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2019-1021-6814cb0cb866-pages.txt"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
topic_ids:
  - "recursive-proof-composition"
  - "nested-amortization"
  - "inner-product-polynomial-commitments"
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "recursive-proof-composition"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition/iacr-eprint-2019-1021"
secondary_ontology_paths:
  - "zero-knowledge-proofs/polynomial-commitments/inner-product-argument-polynomial-commitments/iacr-eprint-2019-1021"
  - "zero-knowledge-proofs/proof-systems/transparent-recursive-arguments/iacr-eprint-2019-1021"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  directions:
    - "recursion-and-folding"
    - "polynomial-commitments"
    - "proof-systems"
  topics:
    - "recursive-proof-composition"
    - "incrementally-verifiable-computation"
    - "nested-amortization"
    - "inner-product-argument-polynomial-commitments"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "Halo"
  - "recursive proof composition"
  - "incrementally verifiable computation"
  - "nested amortization"
  - "inner-product argument"
  - "polynomial commitments"
  - "transparent recursive arguments"
aliases:
  - "Halo"
  - "Recursive Proof Composition without a Trusted Setup"
  - "recursive proof composition without trusted setup"
  - "nested amortization"
  - "Tweedledum and Tweedledee"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "recursion"
  - "recursive-proof-composition"
  - "polynomial-commitments"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "recursive proof systems"
    - "incrementally verifiable computation"
    - "transparent arguments"
  problem:
    - "recursive proof composition without trusted setup"
    - "avoid verifying a linear-time commitment-opening check inside every recursive circuit"
    - "reduce recursive verifier circuit size without requiring a fully succinct argument system"
  method_family:
    - "nested amortization"
    - "inner-product-argument polynomial commitments"
    - "amortized polynomial opening verification"
    - "Fiat-Shamir transform"
    - "elliptic-curve cycles"
  proof_model:
    - "random oracle model after Fiat-Shamir"
    - "discrete-log assumption over normal cycles of elliptic curves"
  evaluation_context:
    - "Tweedledum/Tweedledee 2-cycle"
    - "endomorphism-optimized verification circuit"
    - "16-core Intel i9-7960X benchmark"
  bridge:
    - "polynomial commitments to recursive proof composition"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-halo-recursive-proof-composition"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0069"
safe_for_absorption: true
source_refs:
  - "iacr:2019/1021"
  - "sha256:6814cb0cb866cdfe3af135c0edf4626a266b92e916edef9132c3912f7decbe0e"
  - "pdf:~/Desktop/paper/2019-1021.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "recursion-and-folding"
secondary_directions:
  - "polynomial-commitments"
  - "proof-systems"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "PDF title and abstract explicitly frame recursive proof composition and IVC"
  - "Section 4 defines nested amortization as the core recursive-composition strategy"
  - "Section 3 supplies the amortized inner-product-style polynomial commitment dependency"
  - "Section 6 implements the recursive proof over a normal elliptic-curve 2-cycle"
taxonomy_version: "1.0"
---

# Recursive Proof Composition without a Trusted Setup

## 论文身份

- Title: Recursive Proof Composition without a Trusted Setup
- Common name: Halo
- Authors: Sean Bowe, Jack Grigg, Daira Hopwood
- Visible affiliation: Electric Coin Company
- Local PDF: `~/Desktop/paper/2019-1021.pdf`
- Stable local identity: `sha256:6814cb0cb866cdfe3af135c0edf4626a266b92e916edef9132c3912f7decbe0e`
- External identity: IACR ePrint `2019/1021` from local filename/report convention; local PDF metadata creation date is 2020.
- Extractor: `pypdf`; extraction is readable across all 31 pages, with math notation degradation in protocol formulae.

## 精读状态

- Reading status: `deep_read_complete`
- Coverage: abstract/introduction, contribution claims, polynomial commitment protocol, amortization, nested amortization, main argument, implementation, evaluation, conclusion and appendices were read.
- Skipped sections: none intentionally skipped.
- Extraction gaps: some formula formatting and superscripts/subscripts are degraded, but section structure, algorithms, assumptions and evaluation numbers are readable.
- Safe for absorption: yes. The source supports durable knowledge about recursive proof composition, nested amortization, transparent recursion without trusted setup, and an IPA-style polynomial commitment route.

## 章节地图

| 序号 | 覆盖范围 | 证据来源 |
| --- | --- | --- |
| 1 | p1-p4 abstract, introduction, IVC motivation, recursive proof composition, contributions and concurrent work | `Abstract`, `1`, `1.1`, `1.2` |
| 2 | p5-p6 zero-knowledge arguments of knowledge and group preliminaries | `2.1`, `2.2` |
| 3 | p7-p10 polynomial commitments, modified inner-product opening argument, amortization strategy | `3`, `3.1`, `3.2` |
| 4 | p10-p11 nested amortization and recursive verifier-state deferral | `4` |
| 5 | p11-p16 Sonic-adapted arithmetic-circuit satisfiability argument | `5`, `5.1`, `5.2` |
| 6 | p16-p21 implementation, Fiat-Shamir, curve cycle, endomorphism optimizations, evaluation and conclusion | `6`, `6.1`, `6.2`, `6.3`, `6.4`, `7` |
| 7 | p22-p31 references and appendices | `References`, `Appendix A-C` |

## Hierarchy Candidate Classification

| Layer | Candidate | Confidence | Evidence |
| --- | --- | --- | --- |
| L1 Domain | `zero-knowledge-proofs` | high | paper is a non-interactive zero-knowledge/argument-of-knowledge construction |
| L2 Direction | `recursion-and-folding` | high | abstract, introduction and Section 4 target recursive proof composition/IVC |
| L3 Problem | `recursive-proof-composition` | high | contribution is recursive composition without trusted setup, not a generic folding-scheme paper |
| Secondary | `zero-knowledge-proofs/polynomial-commitments` | high | Section 3 introduces an amortized inner-product-style polynomial commitment scheme |
| Secondary | `zero-knowledge-proofs/proof-systems/zk-snarks` | medium | the paper is adjacent to SNARKs but explicitly is not fully succinct because final verification remains linear |

Alternative placements considered: `folding-schemes` is too specific to the Nova-style route; Halo's core technique is nested amortization, not folding relaxed R1CS. `zk-snarks` alone is too broad and risks hiding the recursive-composition contribution.

## One-Sentence Contribution

Halo realizes practical recursive proof composition without a trusted setup by combining an inner-product-style polynomial commitment with amortized opening checks and nested amortization, so the expensive linear verification work is deferred to the final outside verifier rather than embedded in every recursive circuit.

## Problem Setting

The paper starts from incrementally verifiable computation: a long sequence of computations or state transitions should be represented by a single proof that can itself be extended. In a blockchain example, a participant should not need to download and verify every historical state transition or every proof; a current state plus one recursively composed proof should be enough to validate the chain history relevant to that state.

Prior practical recursive proof composition relied on pairing-based SNARKs over cycles of pairing-friendly elliptic curves. This creates two bottlenecks:

- Pairing-friendly cycles are rare and can require large fields, which hurts verifier-circuit performance.
- Pairing-based SNARKs require a trusted setup.

Transparent systems such as STARKs avoid trusted setup, but at the time of this paper their proof sizes and constants were too large for practical recursive composition. Halo's problem statement is therefore: how can a proof system with logarithmic proof size but a remaining linear verification operation be made recursively composable in practice?

## Method Overview

### 1. Inner-Product-Style Polynomial Commitment

Section 3 constructs a univariate polynomial commitment from a Pedersen vector commitment to polynomial coefficients. To prove that a committed polynomial evaluates to `v` at point `x`, the prover uses a modified inner product argument inspired by Bulletproofs and Bootle et al.

The commitment is hiding and additively homomorphic. The opening proof has logarithmic communication, but the verifier still needs a linear multiscalar multiplication to compute the generator combination determined by the inner-product challenges.

This is the first important boundary: Halo does not magically make the inner-product commitment fully succinct. It keeps the linear verifier operation, then changes where and how often that operation must be performed.

### 2. Amortized Opening Verification

The amortization observation is that the vector structure generated by the inner-product challenges has a smooth polynomial form. A helper can compute the claimed linear-time commitments for many opening proofs and then prove that the whole batch is correct through one additional commitment-opening argument.

The verifier trades `m` separate linear operations for one final linear operation plus logarithmic marginal work per proof. The helper is untrusted; soundness comes from random linear combination and the degree bound of the commitment scheme.

Reusable pattern: an expensive deterministic verification subroutine can sometimes be turned into a deferred state obligation, provided there is a succinct way to batch or amortize the deferred obligations.

### 3. Nested Amortization

Section 4 is the conceptual core. A recursive verifier circuit normally has to verify the previous proof completely. If full verification includes a linear operation, the recursive circuit grows with the size of the proof's underlying computation and arbitrary-depth recursion fails.

Halo instead lets the circuit take both the input and the claimed output of the expensive operation as public inputs. The circuit proceeds as if the output is correct, while the responsibility for checking it is passed to the outside verifier. As recursive proofs compose, the verifier state accumulates; nested amortization collapses multiple deferred checks into one fresh deferred check.

The ultimate verifier performs the linear operation once, outside the recursive circuit. This is why Halo can support arbitrary-depth recursive composition without a fully succinct proof system and without preprocessing/trusted setup.

### 4. Main Argument and Fiat-Shamir

Section 5 adapts Sonic's arithmetic-circuit satisfiability argument to the polynomial commitment scheme from Section 3. The verifier processes a stream of proofs with logarithmic-time marginal work and logarithmic-size state, then performs a final linear-time state check.

Section 6 applies Fiat-Shamir to obtain a non-interactive argument in the random oracle model. The implementation uses Rescue as an algebraic hash function over prime fields with a duplex sponge transcript.

### 5. Curve-Cycle Implementation

The recursive verifier circuit is dominated by group operations. Halo uses a 2-cycle of ordinary, non-pairing-friendly prime-order elliptic curves, named Tweedledum and Tweedledee. Each curve's base field is the scalar field of the other, so a proof over one curve can efficiently reason about verification over the other.

The paper reports 255-bit prime-order curves conjectured to approach 128-bit security; it later states both curves have 126-bit security against Pollard rho attacks after accounting for automorphisms. The curves use equations `y^2 = x^3 + 5` over two 255-bit primes and were chosen for high 2-adicity, multiplicative order-3 elements for endomorphisms, and Rescue hash compatibility.

### 6. Endomorphism Optimizations

The implementation uses curve endomorphisms to reduce the cost of scalar multiplication by verifier challenges inside the circuit. The paper gives an algorithm that costs about 3.5 multiplication constraints per bit for Tweedledum/Tweedledee challenge multiplication. Other optimizations avoid simulating scalar-field arithmetic over the wrong native field by carrying commitments through public inputs.

### 7. Evaluation

The benchmark uses a 16-core Intel i9-7960X CPU at 2.80 GHz with 16 threads. The paper reports:

- recursive composition cross-over just below `2^17` multiplication gates;
- fully recursive proofs of at least `3.5 KiB`;
- comparison against Fractal: Halo is not fully succinct because final verification is linear, but reported recursive proofs are far smaller than Fractal's over-120 KiB proofs at the 128-bit security level.

## Assumptions and Security Boundary

- Non-interactivity uses Fiat-Shamir in the random oracle model.
- Polynomial commitment soundness rests on the discrete-log assumption in the chosen elliptic-curve groups.
- Recursive implementation depends on a curve cycle so each verifier can express the other curve's group arithmetic in the native field.
- The paper explicitly notes a theoretical extractor concern for arbitrary-depth recursion: the number of transcripts needed by the knowledge extractor increases exponentially with depth, though the authors state no known attacks and note fixed-depth proof trees can sidestep this issue.
- The implementation uses incomplete short-Weierstrass addition formulae inside circuits with care; outside the circuit, complete constant-time formulae and immediate proof validation are recommended.

## What Stays in This Source Note

- Halo-specific protocol steps, exact equations, transcript order and implementation choices.
- Tweedledum/Tweedledee curve parameters, endomorphism algorithm and proof-size/threshold measurements.
- The exact claim that Halo is the first practical recursive proof composition without trusted setup, as framed by the paper.
- The non-transfer boundaries around linear final verification, random oracle use, curve cycles and implementation-specific optimizations.

## Absorption Handoff

| Knowledge target | Absorbed reusable delta | Boundary |
| --- | --- | --- |
| [[recursive-proof-composition|Recursive proof composition]] | Adds Halo as the nested-amortization route for transparent recursive composition without trusted setup. | Halo is a source instance; do not promote it to a foundation node. |
| [[recursion-and-folding|Recursion and folding]] | Adds recursive proof composition as a child problem beside folding schemes and SNARK proof aggregation. | Nested amortization is adjacent to but not the same as Nova-style folding schemes. |
| [[polynomial-commitments|Polynomial commitments]] | Adds an IPA-style PCS route whose expensive opening verification can be amortized across proofs. | This is not KZG and not a full PCS landscape survey. |
| [[polynomial-commitments-to-recursive-proof-composition|Polynomial commitments -> recursive proof composition]] | Creates bridge evidence: amortized PCS verification enables recursive verifier-state deferral. | Not every PCS automatically supports Halo-style recursion. |

## Non-Transfer Notes

- Do not infer that every recursive proof construction is a folding scheme. Halo's reusable mechanism is nested amortization over deferred verifier state.
- Do not infer that Halo is a fully succinct SNARK. The paper explicitly keeps a final linear-time verifier operation outside the recursive circuit.
- Do not infer that the Tweedledum/Tweedledee implementation parameters generalize to later Halo 2/Pasta systems without a separate source.
- Do not merge `trusted setup` avoidance into all zk-SNARKs. Halo avoids trusted setup by using a transparent inner-product-style commitment and ordinary curve cycle; pairing-based SNARKs retain their own setup assumptions.

## Queue and Provenance

- Queue: `nahida-paper-folder-20260611-domain-serial-v2`
- Item: `nahida-paper-folder-20260611-domain-serial-v2:item:0069`
- Original queue title hint: `Recursive Proof Composition without a Trusted`
- Corrected PDF title: `Recursive Proof Composition without a Trusted Setup`
- Absorption run: `nahida-knowledge-20260622-halo-recursive-proof-composition`
