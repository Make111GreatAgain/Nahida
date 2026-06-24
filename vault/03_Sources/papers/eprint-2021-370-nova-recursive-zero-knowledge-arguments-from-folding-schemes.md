---
id: "iacr-eprint-2021-370"
title: "Nova: Recursive Zero-Knowledge Arguments from Folding Schemes"
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
  - "p1-p8 abstract, introduction, folding-scheme motivation, comparison with prior recursive proof work"
  - "p8-p12 preliminaries, IVC definition, folding-scheme definition, forking lemma variant"
  - "p13-p16 R1CS, relaxed R1CS, committed relaxed R1CS, interactive and Fiat-Shamir folding scheme"
  - "p17-p22 Nova IVC construction, augmented function F', proof compression, zero-knowledge boundary"
  - "p22-p27 Spartan-style polynomial IOP and zkSNARK for committed relaxed R1CS"
  - "p28-p31 references and implementation/code references"
  - "p32-p45 appendices for related work, completeness/soundness/ZK proofs, commitment definitions, optimization"
canonical_url: "https://eprint.iacr.org/2021/370"
pdf_url: "https://eprint.iacr.org/2021/370.pdf"
doi: "10.1007/978-3-031-15985-5_13"
arxiv_id: ""
venue: "IACR ePrint 2021/370; CRYPTO 2022 version"
year: "2021"
authors:
  - "Abhiram Kothapalli"
  - "Srinath Setty"
  - "Ioanna Tzialla"
affiliations:
  - "Carnegie Mellon University"
  - "Microsoft Research"
  - "New York University"
local_pdf: "~/Desktop/paper/2021-370.pdf"
sha256: "4a26b535f03a27be4ca37e4cbbedbd6ae70661c6506001368c115c0cabdb7931"
pages: 45
pdf_extractor: "pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2021-370-4a26b535f03a-pages.txt"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
topic_ids:
  - "folding-schemes"
  - "incrementally-verifiable-computation"
  - "recursive-snarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "folding-schemes"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/folding-schemes/iacr-eprint-2021-370"
secondary_ontology_paths:
  - "verifiable-computation/interactive-proofs/sum-check-protocol/iacr-eprint-2021-370"
  - "zero-knowledge-proofs/polynomial-commitments/vector-and-multilinear-commitments/iacr-eprint-2021-370"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  directions:
    - "recursion-and-folding"
    - "interactive-proofs"
    - "polynomial-commitments"
  topics:
    - "folding-schemes"
    - "incrementally-verifiable-computation"
    - "committed-relaxed-r1cs"
    - "sum-check-based-iops"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "folding-schemes"
  - "Nova"
  - "incrementally-verifiable-computation"
  - "relaxed-R1CS"
  - "recursive-SNARKs"
  - "Spartan"
aliases:
  - "Nova"
  - "Recursive Zero-Knowledge Arguments from Folding Schemes"
  - "folding schemes"
  - "relaxed R1CS"
  - "committed relaxed R1CS"
  - "IVC from folding schemes"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "recursion"
  - "folding-schemes"
  - "ivc"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "recursive proof systems"
    - "folding schemes"
    - "incrementally verifiable computation"
  problem:
    - "reduce recursion overhead in IVC"
    - "avoid per-step SNARK verification inside recursion"
    - "compress linear IVC proofs into succinct zero-knowledge proofs"
  method_family:
    - "non-interactive folding schemes"
    - "committed relaxed R1CS"
    - "Spartan-style polynomial IOP"
    - "Fiat-Shamir transform"
  proof_model:
    - "random oracle heuristic for non-interactive folding"
    - "DLOG or SXDH depending on commitment scheme"
  evaluation_context:
    - "Rust implementation"
    - "Pasta curve cycle"
    - "Poseidon hash"
    - "bellperson gadget interface"
  bridge:
    - "folding schemes to sum-check and polynomial commitments"
created: "2026-06-11"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-nova-folding-schemes"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0011"
safe_for_absorption: true
source_refs:
  - "iacr:2021/370"
  - "doi:10.1007/978-3-031-15985-5_13"
  - "sha256:4a26b535f03a27be4ca37e4cbbedbd6ae70661c6506001368c115c0cabdb7931"
  - "pdf:~/Desktop/paper/2021-370.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "recursion-and-folding"
secondary_directions:
  - "interactive-proofs"
  - "polynomial-commitments"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract explicitly introduce recursive zero-knowledge arguments from folding schemes"
  - "Sections 3-5 define folding schemes and construct Nova IVC from a non-interactive folding scheme"
  - "Section 6 connects the compression proof to sum-check and Spartan-style polynomial IOPs"
taxonomy_version: "1.0"
---

# Nova: Recursive Zero-Knowledge Arguments from Folding Schemes

## 论文身份

- Title: Nova: Recursive Zero-Knowledge Arguments from Folding Schemes
- Authors: Abhiram Kothapalli, Srinath Setty, Ioanna Tzialla
- Visible affiliations: Carnegie Mellon University, Microsoft Research, New York University
- Local PDF: `~/Desktop/paper/2021-370.pdf`
- Stable local identity: `sha256:4a26b535f03a27be4ca37e4cbbedbd6ae70661c6506001368c115c0cabdb7931`
- External identity: IACR ePrint `2021/370`, DOI `10.1007/978-3-031-15985-5_13`
- Code/reference link visible in paper references: `https://github.com/Microsoft/Nova`
- Extractor: `pypdf`; extraction usable across all 45 pages.

## 精读状态

- Reading status: `deep_read_complete`
- Coverage: abstract/introduction, definitions, constructions, theorem statements, proof intuitions, evaluation, related work, and appendices were read.
- Skipped sections: none intentionally skipped.
- Extraction gaps: mathematical notation is occasionally degraded by PDF text extraction, but theorem/construction structure and cost claims are readable.
- Safe for absorption: yes. The note supports durable claims about the paper's construction, assumptions, costs, limitations, and relation to existing Nahida concepts.

## 章节地图

| 序号 | 覆盖范围 | 证据来源 |
| --- | --- | --- |
| 1 | p1-p8 abstract, introduction, folding-scheme motivation, comparison with prior recursive proof work | frontmatter reading_coverage |
| 2 | p8-p12 preliminaries, IVC definition, folding-scheme definition, forking lemma variant | frontmatter reading_coverage |
| 3 | p13-p16 R1CS, relaxed R1CS, committed relaxed R1CS, interactive and Fiat-Shamir folding scheme | frontmatter reading_coverage |
| 4 | p17-p22 Nova IVC construction, augmented function F', proof compression, zero-knowledge boundary | frontmatter reading_coverage |
| 5 | p22-p27 Spartan-style polynomial IOP and zkSNARK for committed relaxed R1CS | frontmatter reading_coverage |
| 6 | p28-p31 references and implementation/code references | frontmatter reading_coverage |
| 7 | p32-p45 appendices for related work, completeness/soundness/ZK proofs, commitment definitions, optimization | frontmatter reading_coverage |

## Hierarchy Candidate Classification

| Layer | Candidate | Confidence | Evidence |
| --- | --- | --- | --- |
| L1 Domain | `zero-knowledge-proofs` | high | title, abstract, recursive ZK arguments, zkSNARK compression |
| L2 Direction | `recursion-and-folding` | high | folding schemes are introduced as the core primitive for IVC recursion |
| L3 Topic | `folding-schemes` | high | Sections 3-5 define folding schemes and build Nova from them |
| Secondary | `verifiable-computation/interactive-proofs/sum-check-protocol` | medium | Section 6 adapts Spartan polynomial IOP and invokes sum-check |
| Secondary | `zero-knowledge-proofs/polynomial-commitments` | medium | Section 6 compiles IOPs using PCBP/PCDory-style commitments |

Alternative placements considered: `verifiable-computation/interactive-proofs` alone is too broad because the paper's main durable contribution is a recursive ZK/IVC construction. `polynomial-commitments` is a dependency path, not the primary home.

## One-Sentence Contribution

Nova realizes incrementally verifiable computation by replacing per-step recursive SNARK verification with a folding scheme over committed relaxed R1CS, reducing recursion overhead while allowing optional Spartan-style proof compression.

## 核心精读笔记

以下内容由原 source note 的 problem setting、method overview、evaluation/security sections 组成，保留论文机制、假设、证据与限制。

## Problem Setting

The target primitive is incrementally verifiable computation (IVC): a prover repeatedly proves correct execution of `z_i = F(z_{i-1}, omega_{i-1})` while the final verifier checks only the latest proof, not all previous steps. Traditional recursive SNARK-based IVC asks the step circuit to verify a previous SNARK, which makes the verifier circuit expensive. Transparent SNARKs avoid trusted setup but can make recursion even more costly.

Nova's problem framing is: can IVC be built without producing or verifying a SNARK at every step? The proposed answer is to defer checking the NP instances themselves. A folding scheme turns the task of checking two instances into the task of checking one same-size instance; the running folded instance summarizes prior computation.

Assumptions and constraints:

- Each incremental step is represented with R1CS sharing the same coefficient matrices.
- The folding scheme uses succinct, hiding, additively homomorphic vector commitments; Pedersen commitments are the concrete example.
- Non-interactivity is obtained through Fiat-Shamir/random oracle; standard-model deployment uses a cryptographic hash heuristic.
- The optional succinct compression relies on a zkSNARK for committed relaxed R1CS, instantiated by adapting Spartan-style polynomial IOPs.
- The construction targets cycles of elliptic curves where discrete log is hard; PCDory-style variants rely on SXDH.

## Method Overview

### 1. Folding Schemes

Section 3 defines a folding scheme for an NP relation `R` as a protocol where prover and verifier take two instance-witness pairs and output one same-size folded instance, while the prover privately outputs a folded witness. The key guarantee is that a satisfying folded instance should imply that the original instances were satisfiable, up to knowledge soundness.

This primitive is weaker than a SNARK: it does not by itself produce a short argument of satisfiability for a statement. It only reduces two checks to one check. That weaker target is precisely why it can be much cheaper inside recursive IVC.

### 2. Relaxed R1CS

A direct random linear combination of two R1CS witnesses fails because multiplication creates cross terms and the constant `1` term does not combine correctly. Nova introduces relaxed R1CS:

```text
(A * Z) o (B * Z) = u * (C * Z) + E
Z = (W, x, u)
```

The error vector `E` absorbs cross terms and the scalar `u` tracks the folded constant term. Any ordinary R1CS instance embeds as relaxed R1CS with `u = 1` and `E = 0`, so the representation still characterizes NP.

### 3. Committed Relaxed R1CS Folding

To avoid sending witnesses, the final protocol uses committed relaxed R1CS. The instance contains commitments to `E` and `W`, plus public `u` and `x`; the witness contains openings.

Construction 1:

1. Prover computes a cross-term vector `T` and sends a hiding commitment to `T`.
2. Verifier samples random challenge `r`.
3. Both compute folded public pieces:
   - `E <- E1 + r*T + r^2*E2`
   - `u <- u1 + r*u2`
   - `W <- W1 + r*W2`
   - `x <- x1 + r*x2`
4. Prover computes corresponding folded witness openings.

Theorem 3 states this construction is public-coin and satisfies perfect completeness, knowledge soundness, and zero-knowledge. Appendix B proves completeness by expanding the relaxed R1CS equation, soundness by interpolation over three accepting transcripts plus commitment binding, and zero-knowledge from hiding commitments.

### 4. Nova IVC

Nova uses the Fiat-Shamir-transformed non-interactive folding scheme (NIFS). At each step, the augmented function `F'`:

- checks that the current one-step instance `u_i` is tied to `(vk, i, z_0, z_i, U_i)` by a hash,
- checks that `u_i` has ordinary R1CS shape embedded in relaxed R1CS, with `(E, u) = (0, 1)`,
- folds `u_i` into the running folded instance `U_i`,
- outputs a hash of the next public state and running instance.

The IVC proof `Pi_i` is two committed relaxed R1CS instance-witness pairs: one running folded instance and one instance for the latest invocation of `F'`. Lemmas 2-4 cover completeness, knowledge soundness, and efficiency.

### 5. Proof Compression

The raw IVC proof is linear in `|F|`. Section 5.2 compresses it by proving, with a zkSNARK for committed relaxed R1CS, that the prover knows a valid IVC proof. The key trick is to fold the two pairs inside `Pi` once more into `U'`, then prove knowledge of a witness for `U'`.

Section 6 supplies the needed zkSNARK by adapting Spartan:

- Construction 5 gives a polynomial IOP for idealized relaxed R1CS.
- The sum-check protocol reduces the relaxed R1CS identity to a few polynomial evaluations.
- PCBP or PCDory-style polynomial commitments compile the IOP into a zkSNARK.
- Theorem 6 gives a PCBP version with verifier time `O_lambda(n)` and proof length `O_lambda(log n)`.
- Corollary 1 gives a PCDory version with verifier time `O_lambda(log n)` under SXDH.
- Appendix H records a PCBP optimization when the verifier directly evaluates structure polynomials.

## Innovations

| Innovation | What changes | Evidence |
| --- | --- | --- |
| Folding scheme as a primitive | Uses a weaker two-to-one NP-instance reduction rather than per-step SNARK arguments | §1.1, §3 |
| Relaxed R1CS | Adds `E` and `u` so R1CS instances can be algebraically folded | §4.1 |
| Committed relaxed R1CS | Uses homomorphic commitments so folding is non-trivial and zero-knowledge as a folding protocol | Construction 1 |
| IVC from NIFS | The augmented step circuit folds prior computation instead of verifying a previous SNARK | §5.1, Fig. 4 |
| Tailored compression | Compresses linear IVC witnesses via a Spartan-style zkSNARK for committed relaxed R1CS | §5.2-§6 |

## Experiments And Results

Implementation:

- About 6,000 lines of Rust.
- Generic over curve cycle and hash function.
- Candidate implementation uses the Pasta curve cycle and Poseidon.
- The input step function `F` is accepted as a `bellperson` gadget.

Evaluation environment:

- Azure Standard F32s v2 VM.
- 16 physical CPUs, 2.70 GHz Intel Xeon Platinum 8168, 64 GB memory.
- Metrics: prover time, verifier time, proof size, with `|F|` varied.

Reported results:

- Fig. 1 reports Nova's verifier circuit at about 20,584 constraints on the primary curve and 21,124 constraints on the secondary curve. The largest block is scalar multiplications, with additional random-oracle, collision-resistant hash, non-native arithmetic, and glue-code costs.
- The paper claims this is `>10x` lower recursion overhead than SNARK-based IVC with a state-of-the-art per-circuit trusted setup SNARK, `>100x` smaller than with a transparent SNARK, `>7x` lower than Halo, and `>2x` lower than Bunz et al. at the time of comparison.
- Fig. 2 shows prover time, verifier time, and proof size as `|F|` grows from about `2^14` to `2^20` constraints.
- At `|F| ~= 2^20`, per-step IVC proving is reported at about `1 microsecond/constraint`; compressed proof generation is about `24 microseconds/constraint`.
- Compressed proofs are reported at about 8-9 KB and about `7400x` shorter than raw IVC proofs at `|F| ~= 2^20`.
- Verifying a compressed proof is reported as only about `2x` higher cost than verifying the longer raw IVC proof.

## Core Detailed Reading

### Abstract and Introduction

The paper's main move is to separate recursion from arguments of knowledge. Earlier recursive proof systems typically make the step circuit verify a proof from the previous step. Nova instead has the step circuit verify the update of a running folded instance. The result is an IVC design where recursion overhead is dominated by two group scalar multiplications rather than a full or partial SNARK verifier.

This is why the paper describes Nova as taking Halo's deferral idea "to the extreme": Halo defers expensive parts of polynomial-commitment verification, while Nova defers whole NP instances.

### Folding Scheme Definition

The folding scheme definition is intentionally not a proof system. It only transforms two satisfiability obligations into one. Non-triviality means verifier work and communication in the folding step plus one final witness check are cheaper than checking both original witnesses directly. This distinction matters for Nahida: `folding-schemes` should be modeled as a recursion primitive, not as synonymous with SNARKs.

The paper introduces a forking-lemma variant because the extractor needs both accepting transcripts and the folded instance-witness outputs. Appendix E gives the corresponding extractor argument.

### Why Relaxed R1CS Is Needed

The failed direct folding attempt is central. If `Z = Z1 + r*Z2`, the product `(AZ) o (BZ)` produces cross terms and changes the constant coordinate. Relaxed R1CS adds:

- an error vector `E` to absorb cross terms,
- a scalar `u` to let the constant coordinate fold consistently.

This design choice is reusable beyond Nova because many later folding systems also build around relaxed constraints or equivalent accumulators.

### Committed Folding Construction

The cross-term commitment `T` lets the verifier update commitments to the folded error vector without seeing witnesses. The random challenge `r` then binds the linear/quadratic combination. Completeness is pure algebra; soundness depends on extracting original witnesses from multiple accepting transcripts and on commitment binding; zero-knowledge depends on the hiding property of the single commitment sent by the prover.

Theorem 1 summarizes the efficiency: for N-sized relaxed R1CS instances with the same structure, prover work is `O_lambda(N)`, while verifier work and communication are `O_lambda(1)`, assuming succinct additively homomorphic vector commitments.

### Nova IVC Construction

The augmented function `F'` is the recursion carrier. It both executes one step of `F` and updates the running folded instance. Because the next invocation cannot directly pass a large public I/O object, `F'` outputs a collision-resistant hash of the public I/O. The next step receives the preimage as advice.

The raw IVC proof is not a short proof in the usual SNARK sense; it is the running instance-witness pair plus latest invocation pair. Its size is `O(|F|)`, but it does not grow with the number of steps. This is IVC succinctness with respect to step count, not necessarily succinctness with respect to step-circuit size.

### Compression SNARK

The compression stage turns a valid raw IVC proof into a succinct zero-knowledge proof. The paper avoids an off-the-shelf SNARK because proving commitment-opening relations naively would require many group scalar multiplications inside the circuit. Its Spartan-style construction instead treats committed relaxed R1CS with polynomial IOP and multilinear polynomial commitments.

The sum-check dependency appears here: it reduces a relaxed R1CS identity over the Boolean hypercube to evaluations of multilinear extensions of matrices, witness, and error polynomials.

### Appendices

Appendix A clarifies that folding is related to Bulletproofs-style split-and-fold, sum-check, batch verification, and instance compression, but differs because it targets arbitrary NP relations with a witness-aided two-to-one transformation.

Appendix B proves the folding scheme. Appendix C proves IVC completeness and knowledge soundness. Appendix D proves compression zero-knowledge by simulating running instances and final compression proof. Appendix F spells out vector-commitment properties and Pedersen commitments. Appendix H notes that PCBP can be simplified by directly evaluating structure polynomials, yielding Corollary 2.

## Limitations

- Nova is not itself a zero-knowledge IVC scheme; the raw IVC proof does not hide per-step witnesses. Zero-knowledge is obtained by an auxiliary compressed proof, and zero-knowledge IVC is left as future work.
- Non-interactive folding relies on Fiat-Shamir/random oracle modeling and a heuristic standard-model hash instantiation.
- The step computation is expressed as R1CS with shared coefficient matrices across steps; heterogeneous-step or multi-circuit recursion is outside this paper's direct construction.
- Raw IVC proof size and raw verification are linear in `|F|`; succinctness with respect to `|F|` comes from the optional compression stage.
- Knowledge soundness for recursive constructions uses a model where the number of steps `n` is fixed for the extractor; the paper notes no known attacks on arbitrary-depth recursion, but the proof model is still a boundary.
- Evaluation is an implementation/benchmark of the library and synthetic step sizes; application-level workloads such as blockchains or VDF deployments are not deeply benchmarked here.
- The foundation for the compression SNARK assumes Spartan-like IOP/commitment machinery; readers should not infer that folding alone gives all SNARK properties.

## Reusable Ideas

- Treat recursion as maintaining an accumulator/folded instance rather than recursively verifying a proof.
- Use relaxed constraints to absorb algebraic cross terms that block direct linear folding.
- Separate IVC succinctness in step count from succinct proof compression in circuit size.
- Keep folding schemes, accumulation schemes, and SNARKs distinct in the ontology; they overlap in usage but have different guarantees.
- Model proof-system cost along three axes: recursion circuit size, per-step prover work, and final proof compression.

## Terminology

| Term | Meaning |
| --- | --- |
| IVC | Incrementally verifiable computation; prove repeated applications of `F` while verifier checks only latest proof |
| Folding scheme | Protocol reducing two NP-instance checks to one same-size instance check |
| Relaxed R1CS | R1CS variant with error vector `E` and scalar `u` enabling algebraic folding |
| Committed relaxed R1CS | Relaxed R1CS where `E` and `W` are committed in the instance and opened by the witness |
| NIFS | Non-interactive folding scheme, obtained here via Fiat-Shamir/random oracle |
| Nova | The paper's IVC scheme built from NIFS over committed relaxed R1CS |
| PCBP | Polynomial commitment from Pedersen/Bulletproofs style inner-product arguments |
| PCDory | Polynomial commitment using Dory-style inner-product arguments under SXDH |
| Raw IVC proof | Nova proof pair before compression; not zero-knowledge and linear in `|F|` |
| Compressed IVC proof | zkSNARK proof of knowledge of a valid raw IVC proof |

## Connections

- Extends [[sum-check-protocol|Sum-check protocol]] through the Spartan-style polynomial IOP in Section 6.
- Extends [[polynomial-commitments|Polynomial commitments]] with PCBP/PCDory-style multilinear polynomial commitments rather than KZG.
- Creates the ZKP direction [[recursion-and-folding|Recursion and folding]] and topic [[folding-schemes|Folding schemes]].
- Adds concept pages [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova]], [[folding-schemes|Relaxed R1CS]], [[folding-schemes|Incrementally verifiable computation]], and [[folding-schemes|Folding schemes]].
- Bridges proof-system recursion to verifiable computation: folding schemes reuse interactive proof and polynomial IOP tools, but the user-facing protocol is a recursive ZK/IVC system.

## Evidence Table

| Claim | Evidence | Type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Folding schemes reduce two NP-instance checks to one same-size instance check | §1.1, §3, p2-p12 | definition/mechanism | high | Weaker than SNARKs |
| Relaxed R1CS enables folding by absorbing cross terms with `E` and `u` | §4.1, p13-p15 | mechanism | high | Ordinary R1CS embeds with `u=1`, `E=0` |
| Construction 1 is complete, knowledge-sound, and zero-knowledge for committed relaxed R1CS | Theorem 3, p15-p16; Appendix B | theorem | high | Assumes commitment properties |
| Nova realizes IVC by folding step instances into a running committed relaxed R1CS instance | §5.1, Fig. 4, p17-p20 | construction | high | NIFS verifier is inside `F'` |
| Nova's recursion overhead is constant and dominated by two group scalar multiplications | Theorem 2, Lemma 4, Fig. 1 | efficiency | high | Plus hash/RO costs |
| Nova can compress raw IVC proofs into succinct ZK proofs using a Spartan-style zkSNARK | §5.2-§6, Theorem 4 | construction | high | Raw IVC proof itself is not ZK |
| Implementation reports about 20k verifier-circuit constraints and 8-9 KB compressed proofs | Fig. 1, Fig. 2, p5-p6 | empirical_result | high | Benchmark environment specified |
| Non-interactive folding security relies on random oracle instantiation | §4.2, Assumption 1 | limitation/assumption | high | Heuristic standard-model hash |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| A folding scheme is a protocol that reduces the task of checking two NP instances in a relation to checking a single same-size folded instance, with soundness tying satisfiability of the folded instance back to the originals. | `iacr:2021/370#p2-p3,p10-p12` | folded_into_meta_note |
| Nova compresses a linear-size raw IVC proof by folding its two committed relaxed R1CS pairs once more and proving knowledge of a valid folded witness with a Spartan-style zkSNARK for committed relaxed R1CS. | `iacr:2021/370#p20-p27` | folded_into_meta_note |
| Nova's Rust implementation reports a verifier circuit of about 20k R1CS constraints and 8-9 KB compressed proofs in the evaluated Pasta/Poseidon setting. | `iacr:2021/370#p5-p6` | folded_into_meta_note |
| Nova's raw IVC proof is not zero-knowledge because it does not hide witnesses for incremental steps; zero-knowledge is provided by an auxiliary compressed proof, and zero-knowledge IVC is left as future work. | `iacr:2021/370#p17,p20-p22` | folded_into_meta_note |
| Nova realizes incrementally verifiable computation by using a non-interactive folding scheme to fold each step's committed relaxed R1CS instance into a running instance, rather than verifying a SNARK at every recursive step. | `iacr:2021/370#p3-p4,p17-p20` | folded_into_meta_note |
| Nova's verifier circuit for recursion is constant-sized with respect to the step circuit, dominated by two group scalar multiplications plus hash and random-oracle costs. | `iacr:2021/370#p4-p5,p20` | folded_into_meta_note |
| Nova's non-interactive folding and compression arguments rely on Fiat-Shamir/random-oracle modeling plus commitment assumptions such as discrete logarithm for Pedersen/PCBP or SXDH for PCDory-style commitments. | `iacr:2021/370#p16,p26-p27,p44-p45` | folded_into_meta_note |
| Relaxed R1CS adds an error vector E and scalar u so random linear combinations of R1CS-like instances can absorb cross terms and preserve a satisfiable folded constraint system. | `iacr:2021/370#p13-p15` | folded_into_meta_note |

## Knowledge Handoff

可吸收的来源内判断:

- `[[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova realizes IVC with folding schemes]]`
- `[[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Folding schemes reduce two NP instances to one]]`
- `[[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Relaxed R1CS enables folding by absorbing cross terms]]`
- `[[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova recursion overhead is constant]]`
- `[[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova compresses IVC proofs with a Spartan-style zkSNARK]]`
- `[[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova raw IVC proof is not zero-knowledge]]`
- `[[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova implementation shows low recursion overhead]]`
- `[[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova security relies on random oracle and DLOG or SXDH assumptions]]`

Concepts to create/update:

- Create [[folding-schemes|Folding schemes]] as a source-backed seed concept.
- Create [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova]] as a system/proof construction concept.
- Create [[folding-schemes|Relaxed R1CS]] as a constraints/arithmetization concept.
- Create [[folding-schemes|Incrementally verifiable computation]] as a source-backed seed.
- Update [[sum-check-protocol|Sum-check protocol]] as a dependency in the Spartan-style compression path.

Maps/synthesis/bridge actions:

- Create `vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md`.
- Create `vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md`.
- Create `vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md`.
- Create `vault/05_Bridges/folding-schemes-to-sum-check-and-polynomial-commitments.md`.
- Update `vault/04_Knowledge/zero-knowledge-proofs.md`.

Review/follow-up:

- Absorb Halo, Halo Infinite, BCLMS/accumulation schemes, Spartan, Dory, and later SuperNova/HyperNova papers to calibrate comparisons.
- Build foundation notes for R1CS, multilinear extensions, polynomial IOPs, and curve cycles.
- Treat the CRYPTO/ePrint metadata as external source identity; the local PDF itself is the evidence for all technical claims here.

## Synthesis Handoff

Nova should initialize `zero-knowledge-proofs/recursion-and-folding/folding-schemes`. It should not make the whole ZKP domain "solved"; the direction remains `foundation_thin`. It also opens a bridge from recursion/folding to `verifiable-computation/interactive-proofs/sum-check-protocol` and `zero-knowledge-proofs/polynomial-commitments`, because Nova's proof compression path depends on Spartan-style sum-check and multilinear commitments.
