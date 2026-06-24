---
id: "iacr-eprint-2019-142"
title: "LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs"
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
  - "p1-p9 abstract, introduction, results, related work, roadmap"
  - "p10-p19 preliminaries, CP-SNARK definition, composition theorem, cc-SNARKs, lifting compiler"
  - "p20-p23 Pedersen-like commitments, CPlink, CPPed_lin"
  - "p23-p35 PolyCom building blocks, sum-check, Hadamard, self-permutation, linear and matrix multiplication gadgets"
  - "p35-p45 LegoAC, LegoUAC, LegoPar applications and experimental evaluation"
  - "p45 conclusions and limitations"
  - "p49-p81 appendices for composition, compiler, CPlink, PolyCom/CPpoly, internal product, and Groth16 cc-SNARK variants"
canonical_url: "https://eprint.iacr.org/2019/142"
pdf_url: "https://eprint.iacr.org/2019/142.pdf"
doi: ""
arxiv_id: ""
venue: "IACR ePrint 2019/142; full version of a CCS 2019 paper"
year: "2019"
authors:
  - "Matteo Campanelli"
  - "Dario Fiore"
  - "Anais Querol"
affiliations:
  - "IMDEA Software Institute"
  - "Universidad Politecnica de Madrid"
local_pdf: "~/Desktop/paper/2019-142.pdf"
sha256: "d97144a58449c34c697a12cdebc94d70ea28e57a62c3d9a7d43afe976047bcbf"
pages: 81
pdf_extractor: "pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2019-142-d97144a58449-pages.txt"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "modular-zksnarks"
  - "commit-and-prove-snarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "modular-zksnarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/modular-zksnarks/iacr-eprint-2019-142"
secondary_ontology_paths:
  - "zero-knowledge-proofs/polynomial-commitments/commit-and-prove/iacr-eprint-2019-142"
  - "verifiable-computation/interactive-proofs/sum-check-protocol/iacr-eprint-2019-142"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  directions:
    - "proof-systems"
    - "polynomial-commitments"
    - "interactive-proofs"
  topics:
    - "modular-zksnarks"
    - "commit-and-prove-snarks"
    - "polynomial-commitments"
    - "sum-check-protocol"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "LegoSNARK"
  - "modular-zkSNARKs"
  - "commit-and-prove SNARKs"
  - "commit-carrying SNARKs"
  - "CPlink"
  - "PolyCom"
  - "sum-check"
aliases:
  - "LegoSNARK"
  - "Modular Design and Composition of zkSNARKs"
  - "Commit-and-prove zkSNARKs"
  - "CP-SNARKs"
  - "cc-SNARKs"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "zkSNARK"
  - "commit-and-prove"
  - "modular-proof-systems"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "proof systems"
    - "modular zkSNARKs"
    - "commit-and-prove proof systems"
  problem:
    - "compose specialized SNARK gadgets without homogenizing computation"
    - "prove relations over pre-committed data efficiently"
    - "add commit-and-prove capabilities to existing SNARKs"
  method_family:
    - "commit-and-prove SNARK composition"
    - "commit-carrying SNARK lifting"
    - "linear-subspace SNARKs"
    - "sum-check over committed polynomial factors"
  proof_model:
    - "pairing-based instantiations"
    - "generic group model and random oracle model in selected gadgets"
    - "trusted setup for concrete instantiations"
  evaluation_context:
    - "C++ implementation"
    - "libsnark/libff pairing libraries"
    - "LegoGro16, CPmmp, LegoAC1, LegoPar benchmarks"
  bridge:
    - "modular zkSNARKs to polynomial commitments and sum-check"
created: "2026-06-11"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-legosnark"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0012"
safe_for_absorption: true
source_refs:
  - "iacr:2019/142"
  - "sha256:d97144a58449c34c697a12cdebc94d70ea28e57a62c3d9a7d43afe976047bcbf"
  - "pdf:~/Desktop/paper/2019-142.pdf"
  - "github:imdea-software/legosnark"
confidence: "high"
trust_tier: "primary"
primary_direction: "proof-systems"
secondary_directions:
  - "polynomial-commitments"
  - "interactive-proofs"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract define a framework for modular commit-and-prove zkSNARKs"
  - "Sections 3-6 define CP-SNARK composition, cc-SNARK lifting, gadgets, and applications"
  - "Experiments evaluate concrete proof-system instantiations such as LegoGro16 and LegoPar"
taxonomy_version: "1.0"
---

# LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs

## 论文身份

- Title in PDF: LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs
- Queue title: LegoSNARK: Modular Design and Composition of zkSNARKs
- Authors: Matteo Campanelli, Dario Fiore, Anais Querol
- Visible affiliations: IMDEA Software Institute; Universidad Politecnica de Madrid
- Local PDF: `~/Desktop/paper/2019-142.pdf`
- Stable local identity: `sha256:d97144a58449c34c697a12cdebc94d70ea28e57a62c3d9a7d43afe976047bcbf`
- External identity: IACR ePrint `2019/142`
- Code link visible on the first page: `https://github.com/imdea-software/legosnark`
- Extractor: `pypdf`; extraction usable across all 81 pages, with normal PDF math degradation.

## 精读状态

- Reading status: `deep_read_complete`
- Coverage: abstract, introduction, formal definitions, theorem statements, construction sketches, concrete gadgets, applications, experiments, conclusions, and security appendices were read.
- Skipped sections: no major technical section was intentionally skipped; appendices were read selectively for the security logic behind composition, compiler, CPlink, PolyCom/CPpoly, and Groth16 cc-SNARK variants.
- Extraction gaps: mathematical notation, subscripts, and table alignment are degraded by PDF extraction, but relation names, theorem dependencies, costs, and experimental claims remain readable.
- Safe for absorption: yes. The note supports durable claims about modular CP-SNARK composition, cc-SNARK lifting, specialized gadgets, empirical tradeoffs, and setup limitations.

## 章节地图

| 序号 | 覆盖范围 | 证据来源 |
| --- | --- | --- |
| 1 | p1-p9 abstract, introduction, results, related work, roadmap | frontmatter reading_coverage |
| 2 | p10-p19 preliminaries, CP-SNARK definition, composition theorem, cc-SNARKs, lifting compiler | frontmatter reading_coverage |
| 3 | p20-p23 Pedersen-like commitments, CPlink, CPPed_lin | frontmatter reading_coverage |
| 4 | p23-p35 PolyCom building blocks, sum-check, Hadamard, self-permutation, linear and matrix multiplication gadgets | frontmatter reading_coverage |
| 5 | p35-p45 LegoAC, LegoUAC, LegoPar applications and experimental evaluation | frontmatter reading_coverage |
| 6 | p45 conclusions and limitations | frontmatter reading_coverage |
| 7 | p49-p81 appendices for composition, compiler, CPlink, PolyCom/CPpoly, internal product, and Groth16 cc-SNARK variants | frontmatter reading_coverage |

## Hierarchy Candidate Classification

| Layer | Candidate | Confidence | Evidence |
| --- | --- | --- | --- |
| L1 Domain | `zero-knowledge-proofs` | high | paper is explicitly about zkSNARKs and zero-knowledge proof-system composition |
| L2 Direction | `proof-systems` | high | the main artifact is a framework, compiler, and gadgets for proof-system construction |
| L3 Topic | `modular-zksnarks` | high | LegoSNARK links specialized proof gadgets into larger zkSNARKs |
| Secondary | `zero-knowledge-proofs/polynomial-commitments` | medium | PolyCom and polynomial commitments provide several CP gadgets |
| Secondary | `verifiable-computation/interactive-proofs/sum-check-protocol` | medium | sum-check is adapted as a CP gadget over committed polynomial factors |

Alternative placements considered: `polynomial-commitments` alone is too narrow because PolyCom is a dependency rather than the primary contribution. `interactive-proofs` alone is also too narrow because the paper's organizing layer is non-interactive SNARK composition.

## One-Sentence Contribution

LegoSNARK turns commit-and-prove zkSNARKs into a modular design framework: specialized proof gadgets can be composed over shared committed values, and existing commit-carrying SNARKs can be lifted into interoperable CP-SNARKs with CPlink.

## 核心精读笔记

以下内容由原 source note 的 problem setting、method overview、evaluation/security sections 组成，保留论文机制、假设、证据与限制。

## Problem Setting

General-purpose zkSNARKs force heterogeneous computations into a single representation such as an arithmetic circuit, boolean circuit, or RAM model. That homogenization can dominate cost when a computation naturally has components better handled by different specialized proof systems.

The paper's target is modular proof design. A global proof should be assembled from smaller gadgets, each specialized to a relation such as arithmetic-circuit satisfiability, vector equality, Hadamard products, self-permutation, linear relations, or matrix multiplication. The linking mechanism is not a raw witness value but a commitment to shared data.

The central engineering tension is that ordinary SNARKs do not automatically speak the same commitment language. Encoding a commitment verifier inside a generic circuit can be very expensive; the paper reports a Pedersen-vector commitment of length 2048 encoded into Groth16 taking roughly 428 seconds to prove. LegoSNARK instead makes commitment equality and committed relations first-class proof obligations.

## Method Overview

### 1. Commit-and-Prove SNARKs

Definition 3.1 formalizes a CP-SNARK for relations whose witnesses include committed slots. A proof is checked against public input, commitments, and an ordinary auxiliary witness. The proof therefore asserts both that the commitments open to witness values and that the relation holds for those values.

Slot structure matters because it is the interface for composition. Two gadgets can be linked by sharing the commitment to an intermediate value rather than exposing that value or re-encoding it inside another circuit.

### 2. Composition Theorem

Theorem 3.1 gives the composition backbone. If two CP-SNARKs use a common computationally binding commitment scheme and share a committed slot, their conjunction is again a CP-SNARK. The paper also discusses sequential composition, OR-style composition, and bounded multi-gadget composition.

For Nahida's ontology this means CP-SNARKs are not just "SNARKs with commitments"; they are an interface discipline for composable proof gadgets.

### 3. Commit-Carrying SNARKs and Lifting

Commit-carrying SNARKs are SNARKs whose proofs carry a commitment to some witness portion. They are weaker as a composition abstraction because the commitment key can be relation-dependent or proof-tied.

Section 3.5 provides the lifting compiler. A cc-SNARK produces an internal commitment, and CPlink proves that this internal commitment and an external global commitment open to the same value. Theorem 3.2 states that, given the appropriate cc-SNARK and CPlink properties, the compiled scheme is a CP-SNARK. The result also covers weak-binding and double-binding variants.

### 4. Pedersen-Like Commitments and CPlink

For Pedersen-like commitments, commitment linking can be expressed as a linear subspace relation. CPlink therefore avoids encoding a full Pedersen verifier inside a general-purpose SNARK. It uses a Kiltz-Wee style QA-NIZK/linear-subspace SNARK and turns equality of openings across commitment keys into a succinct proof.

`CPPed_lin` similarly proves linear properties of committed vectors. This makes vector equalities and linear wiring constraints reusable components for later applications.

### 5. Polynomial Commitment Gadgets

Sections 5 and Appendix E extract PolyCom and CPpoly from zk-vSQL/VPD-style polynomial commitments. The paper then builds CP gadgets for:

- sum-check over committed polynomial factors (`CPsc`),
- Hadamard products (`CPhad`),
- self-permutation / vector equality (`CPsfprm`),
- linear properties (`CPlin`),
- matrix multiplication with committed or public output (`CPmm`, `CPmmp`).

These gadgets are the concrete "lego pieces": each handles a relation with structure that would be inefficient to flatten into a generic circuit.

## Applications

### LegoGro16

LegoGro16 compiles a Groth16 commit-carrying variant into a CP-SNARK over a classical Pedersen vector commitment. The point is to prove statements about pre-committed data without forcing the Groth16 circuit to verify the Pedersen commitment itself.

In the reported benchmark for committed vector length `n = 2048`, LegoGro16's commitment-handling prover cost is about 0.08 seconds compared with about 428 seconds for the circuit-encoded baseline CPGro16. The tradeoff is slightly larger proof size and modestly slower verification.

### LegoAC and LegoUAC

For arithmetic circuit satisfiability, the paper decomposes circuits into Hadamard-product and linear/wiring relations. LegoAC combines Hadamard and linear CP-SNARKs. LegoUAC uses a gate/wire representation with equality constraints and can be instantiated with universal, circuit-independent CRS components that are specialized deterministically.

The experiments show LegoAC1 is somewhat slower than Groth16 for generic arithmetic-circuit benchmarks, but it has native commit-and-prove capability over Pedersen-committed matrices that Groth16 lacks.

### LegoPar

For parallel computations on joint inputs, LegoPar separates a fully parallel relation from the consistency constraints needed to share inputs across repeated executions. This avoids the redistribution-layer verifier overhead in the Hyrax-style baseline. In the Merkle-tree benchmark, LegoPar is reported faster in both proving and verification on larger inputs.

### Matrix Multiplication

`CPmmp` proves correctness of public-output matrix multiplication using a sum-check/MLE strategy. The paper reports linear prover work in the number of matrix entries and a large empirical proving-time improvement over Groth16 for larger matrices, with a longer but still succinct proof.

## Key Theorems And Constructions

| Item | Role | Evidence |
| --- | --- | --- |
| Definition 3.1 | CP-SNARK syntax for committed witness slots | §3.1 |
| Theorem 3.1 | CP-SNARK conjunction/composition theorem | §3.2, Appendix A |
| Definitions 3.2-3.4 | cc-SNARK, weak binding, double binding | §3.3 |
| Theorem 3.2 | cc-SNARK lifting compiler to CP-SNARK | §3.5, Appendix B |
| Theorem 4.1 | CPlink for Pedersen-like commitments | §4.1, Appendix C |
| Theorem 4.2 | CP-SNARK for linear properties over Pedersen-like commitments | §4.2 |
| Theorems 5.1-5.6 | CP gadgets for sum-check, Hadamard, self-permutation, linear properties, matrix multiplication | §5 |
| Corollaries 6.1-6.3 | LegoAC, LegoUAC, LegoPar applications | §6 |
| Theorem H.1/H.2 | Groth16-based cc-SNARK variants | Appendix H |

## Experiments And Results

Implementation:

- C++ implementation.
- Polynomial operations and pairings use libsnark/libff-related libraries.
- Benchmarks run single-threaded on a Debian VM with 8 Xeon Gold 6154 cores and 30 GB RAM.

Reported results:

- LegoGro16 vs CPGro16: for `n = 2048`, proving overhead is about 0.084 seconds vs 428.7 seconds, CRS about 130 KB vs 935 MB, proof about 191 bytes vs 127 bytes, verification about 4.1 ms vs 3.4 ms.
- Matrix multiplication: `CPmmp` has prover time linear in matrix entries; for `128 x 128`, the reported prover time is about 84 ms vs 109 seconds for Groth16, while verification is about 28 ms vs 51 ms.
- LegoAC1: for SHA256 and matrix factoring, LegoAC1 is somewhat slower than Groth16, but has native commit-and-prove semantics over committed matrices.
- LegoPar: for parallel Merkle-tree checks with shared inputs, LegoPar is faster than the Hyrax RDL baseline on larger instances and has stronger verifier scaling.

## Limitations

- The concrete instantiations evaluated in the paper rely on pairing-based systems with trusted setup, even though the abstract framework in Section 3 is more general.
- Several security claims rely on model choices such as the generic group model, algebraic group model, or random oracle model depending on the gadget.
- Universal CRS support is not uniform: some instantiations have circuit-specific CRS, while universal variants can shift costs into other components.
- LegoAC1 does not beat optimized Groth16 on generic arithmetic-circuit benchmarks; the advantage appears when commit-and-prove modularity, committed-state reuse, or specialized relations matter.
- The implementation evaluates selected gadgets and applications; it is not a complete proof-system ecosystem comparison.
- Some comparative edges, such as relationships to Hyrax, Geppetto, Groth16, zk-vSQL, and GKM+18, should later be calibrated by absorbing those primary sources directly.

## Reusable Ideas

- Treat commitments as the public interface between proof gadgets.
- Use commitment-linking proofs instead of circuit-encoding commitment verification.
- Separate "native CP capability" from "generic SNARK expressiveness" when evaluating proof systems.
- Represent shared wiring/equality as vector equality or permutation relations rather than ad hoc glue circuits.
- Model proof-system composition along three axes: relation decomposition, commitment compatibility, and CRS/setup compatibility.

## Terminology

| Term | Meaning |
| --- | --- |
| CP-SNARK | Commit-and-prove SNARK proving a relation about committed witness slots |
| cc-SNARK | Commit-carrying SNARK whose proof carries a commitment to a witness portion |
| CPlink | CP-SNARK gadget proving that commitments under different keys/schemes open to the same value |
| LegoGro16 | CP version of Groth16 produced through the lifting compiler and CPlink |
| LegoAC | Arithmetic-circuit CP-SNARK built from Hadamard and linear-relation gadgets |
| LegoUAC | Universal-CRS arithmetic-circuit CP-SNARK variant using equality/permutation structure |
| LegoPar | Modular proof for parallel computations on joint/shared inputs |
| PolyCom | Polynomial commitment derived from zk-vSQL/VPD machinery and used by several CP gadgets |
| CPsc | CP-SNARK gadget for sum-check over committed polynomial factors |

## Connections

- Creates the ZKP direction [[proof-systems|Proof systems]] and topic [[modular-zksnarks|Modular zkSNARKs]].
- Adds concept pages [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]], [[modular-zksnarks|Commit-and-prove SNARKs]], [[modular-zksnarks|Commit-carrying SNARKs]], and [[modular-zksnarks|Modular zkSNARKs]].
- Extends [[polynomial-commitments|Polynomial commitments]] through PolyCom, CPpoly, and commitment-linking.
- Extends [[sum-check-protocol|Sum-check protocol]] through `CPsc`, `CPhad`, and `CPmm` gadgets.
- Bridges proof-system modularity to verifiable computation: LegoSNARK uses sum-check and polynomial commitments as specialized gadgets inside larger non-interactive proof systems.

## Evidence Table

| Claim | Evidence | Type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| LegoSNARK builds a modular framework for CP-SNARKs | abstract, §1.1, §3 | construction/framework | high | The paper explicitly presents definitions, composition, compiler, and gadgets |
| CP-SNARKs compose through shared committed slots | Definition 3.1, Theorem 3.1 | theorem/mechanism | high | Binding commitment scheme is central |
| cc-SNARKs can be lifted to CP-SNARKs with CPlink | §3.5, Theorem 3.2 | compiler | high | Covers weak/double-binding variants |
| CPlink avoids expensive circuit encoding for Pedersen-like commitment equality | §4.1, §7.1 | mechanism/empirical | high | LegoGro16 benchmark illustrates payoff |
| LegoSNARK supplies gadgets for sum-check, Hadamard, self-permutation, linear and matrix relations | §5 | construction inventory | high | Each gadget has theorem statement |
| CPmmp has linear prover work in matrix entries | §5.6, §7.2 | efficiency | high | Empirically compared to Groth16 |
| LegoGro16 is about 5000x faster than circuit-encoded commitment verification at `n=2048` | abstract, §7.1, Table 3 | empirical_result | high | Comparison is for commitment-handling overhead |
| Concrete instantiations rely on trusted setup | §8 | limitation | high | Paper says this is not inherent to framework |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| LegoSNARK's lifting compiler turns commit-carrying SNARKs, including weak-binding and double-binding variants, into CP-SNARKs for a global commitment scheme by adding a CPlink proof that internal and external commitments open to the same values. | `iacr:2019/142#p17-p19,p51-p55` | folded_into_meta_note |
| CP-SNARKs support secure conjunction and sequential composition when component relations share committed witness slots under a common computationally binding commitment scheme. | `iacr:2019/142#p12-p14,p49-p51` | folded_into_meta_note |
| For Pedersen-like commitments, CPlink expresses equality of openings across commitment keys as a linear subspace SNARK relation, avoiding the cost of circuit-encoding commitment verification. | `iacr:2019/142#p20-p22,p55-p59` | folded_into_meta_note |
| For Pedersen-committed vectors of length 2048, the LegoSNARK paper reports LegoGro16's commitment-handling prover overhead at about 0.08 seconds versus about 428 seconds for encoding Pedersen verification inside Groth16, roughly a 5000x speedup. | `iacr:2019/142#p1,p7,p41-p42` | folded_into_meta_note |
| LegoSNARK frames modular zkSNARK design around commit-and-prove SNARKs, so specialized proof gadgets can be linked over shared committed values instead of homogenizing all computation into one generic representation. | `iacr:2019/142#p1-p7,p12-p19` | folded_into_meta_note |
| The LegoSNARK framework is abstract, but the concrete instantiations evaluated in the paper rely on pairing-based systems with trusted setup. | `iacr:2019/142#p45` | folded_into_meta_note |
| LegoSNARK's CP-SNARK for matrix multiplication uses multilinear-extension and sum-check structure so the prover runs linearly in the number of matrix entries, improving over circuit encodings for the evaluated matrix multiplication task. | `iacr:2019/142#p33-p35,p41-p42` | folded_into_meta_note |
| LegoSNARK supplies CP-SNARK gadgets for sum-check, Hadamard products, self-permutation, linear properties, and matrix multiplication over committed data. | `iacr:2019/142#p23-p35` | folded_into_meta_note |

## Knowledge Handoff

可吸收的来源内判断:

- `[[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK builds a modular CP-SNARK framework]]`
- `[[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|CP-SNARKs enable composition over shared commitment slots]]`
- `[[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|cc-SNARK lifting compiler adds commit-and-prove capabilities]]`
- `[[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|CPlink links Pedersen-like commitments via a linear subspace SNARK]]`
- `[[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK provides CP gadgets for Hadamard, permutation, linear, and matrix relations]]`
- `[[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK matrix multiplication achieves linear prover complexity]]`
- `[[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoGro16 is faster than circuit-encoded commitment verification]]`
- `[[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK instantiations rely on pairing trusted setup]]`

Concepts to create/update:

- Create [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]] as a framework/system concept.
- Create [[modular-zksnarks|Commit-and-prove SNARKs]] as a proof-interface concept.
- Create [[modular-zksnarks|Commit-carrying SNARKs]] as a lifting source concept.
- Create [[modular-zksnarks|Modular zkSNARKs]] as the topic concept.
- Bridge to [[sum-check-protocol|Sum-check protocol]] and [[polynomial-commitments|Polynomial commitments]].

Maps/synthesis/bridge actions:

- Create `vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md`.
- Create `vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md`.
- Create `vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md`.
- Create `vault/05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md`.
- Update `vault/04_Knowledge/zero-knowledge-proofs.md`.

Review/follow-up:

- Absorb Geppetto, Groth16, Hyrax, zk-vSQL, GKM+18, Lipmaa Hadamard CP-SNARK, and Kiltz-Wee/QA-NIZK sources before making broad comparative history claims evergreen.
- Analyze `imdea-software/legosnark` repository later as implementation evidence if the code becomes important.
- Build foundation notes for SNARK syntax, QAP/R1CS, Pedersen commitments, and polynomial IOPs.

## Synthesis Handoff

LegoSNARK should initialize `zero-knowledge-proofs/proof-systems/modular-zksnarks`. It does not make the ZKP proof-systems direction complete; the direction remains `foundation_thin`. The high-value cross-path bridge is from modular zkSNARKs to polynomial commitments and sum-check, because LegoSNARK uses those components as reusable proof gadgets rather than as isolated protocol topics.
