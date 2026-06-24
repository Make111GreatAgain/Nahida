---
id: "doi-10-1109-sp-2015-23"
title: "Geppetto: Versatile Verifiable Computation"
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
  - "p1-p2 abstract, introduction, contributions, system motivation"
  - "p2-p5 MultiQAP intuition, proof schedules, state-sharing alternatives"
  - "p5-p7 verifiable cryptography, bounded bootstrapping, energy-saving circuits"
  - "p6-p9 commit-and-prove definitions, scheduled knowledge soundness, Geppetto CP protocol"
  - "p9-p10 QAP-friendly cryptography and nested curve construction"
  - "p10-p14 compiler/toolchain, programming model, MultiQAP patterns, LLVM interpretation, bootstrapping compilation, energy-saving implementation"
  - "p14-p17 microbenchmarks, MultiQAP evaluation, bootstrapping, energy-saving circuits, compiler scale, related work, conclusions"
  - "p17-p18 references"
canonical_url: "https://doi.org/10.1109/SP.2015.23"
pdf_url: ""
doi: "10.1109/SP.2015.23"
arxiv_id: ""
venue: "2015 IEEE Symposium on Security and Privacy"
year: "2015"
authors:
  - "Craig Costello"
  - "Cedric Fournet"
  - "Jon Howell"
  - "Markulf Kohlweiss"
  - "Benjamin Kreuter"
  - "Michael Naehrig"
  - "Bryan Parno"
  - "Samee Zahur"
affiliations:
  - "Microsoft Research"
  - "University of Virginia"
local_pdf: "~/Desktop/paper/Geppetto_Versatile_Verifiable_Computation.pdf"
sha256: "fe3de073007d0c4553b190e213e286b350a11ef02f6ee1af35008ce193dddbf3"
pages: 18
pdf_extractor: "pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/geppetto-versatile-verifiable-computation-fe3de073007d-pages.txt"
hierarchy_level: "source"
domain_id: "verifiable-computation"
direction_id: "verifiable-computation-systems"
topic_ids:
  - "qap-based-vc-systems"
  - "qap-state-sharing"
ontology_path:
  - "verifiable-computation"
  - "verifiable-computation-systems"
  - "qap-based-vc-systems"
primary_ontology_path: "verifiable-computation/verifiable-computation-systems/qap-based-vc-systems/doi-10-1109-sp-2015-23"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/modular-zksnarks/doi-10-1109-sp-2015-23"
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-snarks/doi-10-1109-sp-2015-23"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "verifiable-computation"
    - "zero-knowledge-proofs"
  directions:
    - "verifiable-computation-systems"
    - "proof-systems"
  topics:
    - "qap-based-vc-systems"
    - "qap-state-sharing"
    - "commit-and-prove-schemes"
    - "proof-composition-and-aggregation"
domains:
  - "verifiable-computation"
  - "zero-knowledge-proofs"
topics:
  - "Geppetto"
  - "MultiQAPs"
  - "commit-and-prove schemes"
  - "bounded proof bootstrapping"
  - "energy-saving circuits"
aliases:
  - "Geppetto"
  - "MultiQAP"
  - "MultiQAPs"
  - "bounded bootstrapping"
  - "energy-saving circuits"
tags:
  - "nahida/source"
  - "paper"
  - "verifiable-computation"
  - "commit-and-prove"
  - "qap"
direction_facets:
  parent_domain:
    - "verifiable-computation"
  subdomain:
    - "verifiable computation systems"
    - "compiled verifiable computation"
    - "commit-and-prove systems"
  problem:
    - "reduce prover overhead for outsourced computation"
    - "share state across multiple verifiable computations without verifier-linear intermediate state"
    - "compress multiple proofs into a constant-size proof under bounded schedules"
  method_family:
    - "MultiQAPs"
    - "commit-and-prove schemes"
    - "bounded proof bootstrapping"
    - "QAP-friendly elliptic-curve cryptography"
    - "energy-saving circuits"
  proof_model:
    - "QAP/Pinocchio-style pairing-based arguments"
    - "knowledge sound commit-and-prove"
    - "binding bus digests"
    - "perfect zero-knowledge option"
  evaluation_context:
    - "C/LLVM compiler"
    - "F# compiler"
    - "C++ cryptographic runtime"
    - "MapReduce, matrix exponentiation, bootstrapping and branch microbenchmarks"
  bridge:
    - "Geppetto to modular zkSNARKs and commit-and-prove SNARKs"
created: "2026-06-11"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-geppetto"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0013"
safe_for_absorption: true
source_refs:
  - "doi:10.1109/SP.2015.23"
  - "eprint:2014/976"
  - "sha256:fe3de073007d0c4553b190e213e286b350a11ef02f6ee1af35008ce193dddbf3"
  - "pdf:~/Desktop/paper/Geppetto_Versatile_Verifiable_Computation.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "verifiable-computation-systems"
secondary_directions:
  - "proof-systems"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract explicitly introduce a verifiable computation compiler/runtime"
  - "Sections 2-4 define MultiQAPs and a commit-and-prove protocol"
  - "Sections 6-7 implement and evaluate Geppetto as a system"
taxonomy_version: "1.0"
---

# Geppetto: Versatile Verifiable Computation

## 论文身份

- Title: Geppetto: Versatile Verifiable Computation
- Authors: Craig Costello, Cedric Fournet, Jon Howell, Markulf Kohlweiss, Benjamin Kreuter, Michael Naehrig, Bryan Parno, Samee Zahur
- Visible affiliations: Microsoft Research; University of Virginia
- Venue/year: 2015 IEEE Symposium on Security and Privacy
- DOI: `10.1109/SP.2015.23`
- Local PDF: `~/Desktop/paper/Geppetto_Versatile_Verifiable_Computation.pdf`
- Stable local identity: `sha256:fe3de073007d0c4553b190e213e286b350a11ef02f6ee1af35008ce193dddbf3`
- Related full paper reference in bibliography: Cryptology ePrint `2014/976`
- Code link visible in the paper: `https://vc.codeplex.com`
- Extractor: `pypdf`; extraction usable across all 18 pages, with minor ligature and table formatting noise.

## 精读状态

- Reading status: `deep_read_complete`
- Coverage: introduction, definitions, protocol, implementation, evaluation, related work, conclusion, and references were read.
- Skipped sections: none intentionally skipped. Proofs for Theorems 1-4 are deferred by the paper to its full version, so this note records theorem statements and proof boundaries rather than reconstructing missing proofs.
- Extraction gaps: Figure/table formatting is lossy but core values in Figures 6-8 and section claims are readable.
- Safe for absorption: yes. The note supports durable claims about MultiQAPs, scheduled commit-and-prove soundness, bounded bootstrapping, QAP-friendly cryptography, compiler design, and evaluation tradeoffs.

## 章节地图

| 序号 | 覆盖范围 | 证据来源 |
| --- | --- | --- |
| 1 | p1-p2 abstract, introduction, contributions, system motivation | frontmatter reading_coverage |
| 2 | p2-p5 MultiQAP intuition, proof schedules, state-sharing alternatives | frontmatter reading_coverage |
| 3 | p5-p7 verifiable cryptography, bounded bootstrapping, energy-saving circuits | frontmatter reading_coverage |
| 4 | p6-p9 commit-and-prove definitions, scheduled knowledge soundness, Geppetto CP protocol | frontmatter reading_coverage |
| 5 | p9-p10 QAP-friendly cryptography and nested curve construction | frontmatter reading_coverage |
| 6 | p10-p14 compiler/toolchain, programming model, MultiQAP patterns, LLVM interpretation, bootstrapping compilation, energy-saving implementation | frontmatter reading_coverage |
| 7 | p14-p17 microbenchmarks, MultiQAP evaluation, bootstrapping, energy-saving circuits, compiler scale, related work, conclusions | frontmatter reading_coverage |
| 8 | p17-p18 references | frontmatter reading_coverage |

## Hierarchy Candidate Classification

| Layer | Candidate | Confidence | Evidence |
| --- | --- | --- | --- |
| L1 Domain | `verifiable-computation` | high | paper targets outsourced computation verification and implements a VC compiler/runtime |
| L2 Direction | `verifiable-computation-systems` | high | main artifact is an engineered system over QAP/Pinocchio-style proofs |
| L3 Topic | `geppetto` | high | paper introduces the named Geppetto toolchain |
| L3 Topic | `multiqaps` | high | MultiQAPs are the central proof representation for shared state |
| Secondary | `zero-knowledge-proofs/proof-systems` | medium | protocol supports zero-knowledge and commit-and-prove proof composition |

Alternative placements considered: `interactive-proofs` is relevant historically, but Geppetto's concrete system is non-interactive/argument-style and compiler-oriented. `zero-knowledge-proofs` alone is too broad because the paper's primary framing is verifiable computation.

## One-Sentence Contribution

Geppetto makes QAP-based verifiable computation more practical and flexible by decomposing programs into MultiQAPs connected by succinct bus digests, then adding bounded bootstrapping, QAP-friendly cryptography, energy-saving circuits, and an LLVM-based compiler/runtime.

## 核心精读笔记

以下内容由原 source note 的 problem setting、method overview、evaluation/security sections 组成，保留论文机制、假设、证据与限制。

## Problem Setting

Verifiable computation lets a weak client outsource computation to an untrusted worker and verify the result faster than recomputing. Systems such as Pinocchio and Zaatar made verification nearly practical, but proof generation remained expensive, often 3-6 orders of magnitude above native execution.

Geppetto focuses on prover-side practicality and flexibility. The paper identifies three recurring sources of waste:

- repeated program structure from loops and function calls,
- expensive state sharing across multiple computations,
- worst-case branch execution in circuit/QAP compilation.

The paper's core answer is not a new asymptotic IP like GKR, but a practical QAP-based system design: split a large computation into smaller related QAPs, use commit-and-prove digests to connect their state, and compile C/LLVM programs into those proof schedules.

## Method Overview

### 1. MultiQAPs and Banks/Buses

Geppetto partitions variables into banks. Some banks represent program input/output, some represent local variables for one sub-computation, and some are buses that share values across sub-QAPs.

Instead of sending intermediate state `z` to the verifier, the prover sends a succinct digest `Dz`. That digest is used when verifying both the producer sub-proof and the consumer sub-proof, forcing consistency without making verifier work linear in `|z|`.

The paper formalizes a proof schedule as a sequence of sub-function instances plus bank instance indexes. A proof for a schedule contains one proof per step and one digest per bank instance.

### 2. MultiQAP Construction

Starting from QAPs for sub-functions, Geppetto builds one MultiQAP `Q*`. Shared variables are routed through bus variables. For example, if `z0` from one QAP and `z1` from another must be equal, a bus variable `zhat` is introduced with an equation like `z0 + z1 = zhat`. When verifying one sub-QAP at a time, unused local banks are set to zero, so the same bus digest enforces the intended equality.

This gives state sharing without collapsing everything back into one huge QAP. The degree increases by bus variables, but the active sub-QAP remains close to the original sub-QAP size.

### 3. Commit-and-Prove Security Model

Section 3 defines succinct commit-and-prove schemes with digest generation, digest verification, proof generation, and proof verification. Bus digests must be binding because they are reused across proofs; local digests need not be binding when they appear in only one proof.

Theorem 1 states that a CP scheme that is knowledge sound and binding for the binding digest subset is scheduled knowledge sound. Intuitively, extraction obtains openings for all accepted subproofs, and binding bus digests enforce consistency across repeated uses.

### 4. Geppetto CP Protocol

Protocol 1 adapts Pinocchio/QAP techniques to MultiQAPs. The prover computes digests for banks and a proof polynomial witness `h(s)` for divisibility. The verifier first checks digest well-formedness and then combines the digests in a QAP divisibility check.

Theorems 2-4 state that Protocol 1 has binding digests, is knowledge sound, and is perfectly zero-knowledge. The paper defers proofs to the full version.

### 5. QAP-Friendly Cryptography and Bounded Bootstrapping

Geppetto needs to verify cryptographic operations inside QAPs, especially when bootstrapping proofs. The paper chooses curve parameters so operations on an embedded elliptic curve fit naturally in the QAP field, making signatures, pairings, and proof verification much cheaper than naive big-integer embedding.

For bootstrapping, Geppetto chooses bounded schedules: the client fixes a maximum number of proofs to aggregate. This sacrifices the generality of unbounded bootstrapping but enables smaller/faster curve choices and multiple nested levels.

### 6. Energy-Saving Circuits

Geppetto observes that variables with value zero have no cryptographic exponentiation cost in its protocol. The compiler therefore rewrites branches so untaken branches have zero inputs and zero intermediate variables. The prover still pays some polynomial/QAP overhead, but avoids most cryptographic work for dead branches.

### 7. Compiler and Runtime

The system includes:

- a C/LLVM front end via clang,
- an F# symbolic interpreter and compiler,
- C libraries for banks, buses, MultiQAP patterns, and QAP-friendly cryptography,
- a C++ cryptographic runtime (`FFLib`),
- generated verifier code that replaces `OUTSOURCE` calls with proof/digest checks.

The programming model is explicit: programmers mark outsourced functions and control bank/bus structure through library calls. This exposes cost control but is not yet high-level automatic synthesis.

## Innovations

| Innovation | What changes | Evidence |
| --- | --- | --- |
| MultiQAPs | Replace one huge QAP or hash-based state transfer with sub-QAPs connected by bus digests | §2.1, §4 |
| Scheduled CP soundness | Extends CP soundness to multiple proofs sharing digests according to schedules | §3.2 |
| Bounded bootstrapping | Compresses many proofs using nested curves and bounded schedules rather than fully general unbounded recursion | §2.2, §5, §7.3.1 |
| QAP-friendly cryptography | Chooses curves/fields so cryptographic verification embeds cheaply in QAPs | §5, §7.3 |
| Energy-saving circuits | Uses zeroed untaken branches to reduce cryptographic prover work | §2.3, §6.5, §7.4 |
| LLVM-based VC compiler | Compiles C/LLVM into banked outsourced functions, digests, proofs, and generated verifier code | §6 |

## Experiments And Results

Evaluation environment:

- HP Z420 desktop.
- Single core of 3.6 GHz Intel Xeon E5-1620.
- 16 GB RAM.

Main results:

- Figure 6 reports cryptographic microbenchmarks for BN and Cocks-Pinch curves. The paper notes Geppetto's protocol keeps most work on the cheaper BN base group.
- Section 7.2 compares MultiQAP state sharing with Pantry-style hashing. At micro level, Pantry hashing increases QAP degree by about `11.25/byte`, while MultiQAPs cost about `0.03/byte` for full field elements or `0.25/byte` for 32-bit values.
- Figure 7 reports MapReduce dot-product and nucleotide substring examples. For the 10K dot-product mapper, Pantry has about `103x` QAP degree, `114x` keygen, and `1169x` prover overhead relative to Geppetto; larger rows use simulated Pantry values when it runs out of memory.
- Matrix exponentiation loop examples show smaller but still meaningful savings because the actual computation dominates state-sharing cost more strongly.
- Section 7.3 estimates naive pairing embedding at QAP degree 44M, while matching curves bring a pairing to degree 14K, about `3100x` smaller.
- Section 7.3.1 states one bootstrapping example can produce a single constant-size proof for a useful QAP degree over 50M in 152 minutes, roughly five orders of magnitude faster than the cited unbounded BCTV comparison.
- Figure 8 shows an energy-saving runtime condition with one matrix multiplication costs `1.68x` the static one-multiplication circuit instead of `5x`; the five-multiplication case costs about `5.06x`, almost the same as static.
- Section 7.5 reports the compiler handles non-trivial cryptographic libraries, including a largest library of 4,159 SLOC.

## Core Detailed Reading

### Introduction and Motivation

The paper is positioned after Pinocchio and related QAP-based VC systems. Verification is already compact, but prover cost is the bottleneck. Geppetto's name is intentional: instead of one large Pinocchio, it coordinates many smaller proof components.

The key practical observation is that compilers for QAPs often unroll loops and inline functions. This replicates subcircuits and forces costs to track worst-case static circuit size. Geppetto's MultiQAPs let the prover reuse one loop-body or function QAP across many scheduled instances while linking state through digests.

### MultiQAPs as State-Sharing

Hash-based state transfer is treated as a baseline: commit to state by hashing it inside the computation. That reduces verifier IO but forces the prover to prove hash computations. Geppetto instead uses digest material already close to what Pinocchio computes. For shared state that is mostly used by the next computation, bus digests are much cheaper than hashing.

The paper explicitly notes a boundary: hashing is still better when a computation touches only a small part of a large input, or when state crosses keys generated by mutually distrusting parties.

### Commit-and-Prove Definitions

The CP formalism is tailored to succinct digests. Since succinct digests cannot be information-theoretically binding against unbounded adversaries, binding is computational and applies to selected bus digest keys. Knowledge soundness requires an extractor to recover values/openings consistent with accepted digest/proof evidence.

Scheduled knowledge soundness is the key multi-proof property. It says that if all digest verifications and all scheduled proof verifications accept, then all scheduled assignments are in the relation, except with negligible probability.

### Protocol 1

The protocol splits work into digest computation and proof computation. Digest keys carry encoded polynomial evaluations for a bank. For commitment-compatible buses, parts of the digest simplify because the bus variables appear only in the `Y` polynomial component. This is what makes bus digests usable as succinct state commitments.

The protocol supports non-interactive zero-knowledge by randomizing with multiples of the target polynomial `delta(s)`. When only verifiable computation is needed, those randomization terms can be omitted.

### Bounded Bootstrapping

The bootstrapping strategy recursively outsources verification of proof schedules. A level-2 proof checks a bounded number of level-1 proofs and digests; further levels can repeat the pattern. This creates a tree of proof schedules where each node condenses evidence below it.

The design is pragmatic rather than universal. It performs well when the maximum schedule length can be chosen in advance, and energy-saving circuits reduce wasted work when fewer proofs are actually used. It is less general than unbounded bootstrapping over a cycle of curves.

### Compiler

The compiler has two related symbolic interpreters. The compile-time interpreter constructs QAP variables/equations from LLVM. The prove-time interpreter replays the program on concrete values to generate witnesses, bank digests, and proofs. Verification mode generates C code that loads digests/proofs and checks them.

This structure makes Geppetto a system paper, not only a protocol paper: programmers use C bank abstractions and `OUTSOURCE` annotations to steer how state and proof schedules are formed.

## Limitations

- The paper states that Geppetto imposes semantic restrictions on C programs, including almost no pointer support.
- Programmer-directed partitioning is powerful but low-level; higher-level syntax and abstractions are left as future work.
- Proofs for some theorems and construction details are deferred to the full paper/ePrint version.
- Bounded bootstrapping requires committing in advance to maximum proof counts; unbounded bootstrapping is more general and eventually wins for sufficiently large schedules.
- MultiQAPs are less advantageous when a computation touches only a tiny part of a large state, where hashing/Merkle-style approaches can be better.
- Geppetto's compilation-based implementation sacrifices some generality compared with CPU-instruction interpretation systems.
- The evaluation is from a single-core desktop setting and compares against Pantry/BCTV with some simulated or estimated values where implementations/code were unavailable.

## Reusable Ideas

- Treat state-sharing cost as a first-class dimension of verifiable computation systems.
- Split a computation into proof-scheduled subcomputations instead of forcing one monolithic circuit.
- Use binding commitments/digests only where reuse across proofs requires consistency.
- Separate native computation cost, QAP degree, cryptographic exponentiation cost, and verifier IO when evaluating VC systems.
- Use compiler rewrites to align cryptographic prover cost with actual execution paths, not worst-case branches.
- Consider bounded practical recursion when unbounded recursion imposes high curve or interpreter overhead.

## Terminology

| Term | Meaning |
| --- | --- |
| Verifiable computation | Client outsources computation and verifies result with cryptographic evidence |
| QAP | Quadratic Arithmetic Program, a polynomial representation of arithmetic-circuit constraints |
| MultiQAP | Geppetto's combination of sub-QAPs plus bus variables/digests for shared state |
| Bank | Partition of variables with digest/key material, e.g. IO, local variables, or buses |
| Bus | Bank used to share state across multiple sub-QAP/proof steps |
| Proof schedule | Sequence describing which sub-function instance is proved and which bank instances it uses |
| Commit-and-prove scheme | Proof system where digests/commitments to messages are used inside proofs |
| Bounded bootstrapping | Proof aggregation/recursion with a preselected bound on proofs per level |
| Energy-saving circuit | Circuit/QAP transformation that makes untaken branches evaluate to zero and reduces cryptographic prover work |

## Connections

- Extends [[delegated-computation|Delegated computation]] from asymptotic IP foundations toward practical compiler/runtime systems.
- Creates [[verifiable-computation-systems|Verifiable computation systems]] and [[qap-based-verifiable-computation-systems|Geppetto]] as a systems-oriented path.
- Connects to [[modular-zksnarks|Commit-and-prove SNARKs]] and [[modular-zksnarks|Modular zkSNARKs]]: LegoSNARK later treats Geppetto as a relevant commit-carrying/CP-style ancestor.
- Depends on QAP/Pinocchio foundations, which are still missing as standalone Nahida concepts.
- Touches [[polynomial-commitments|Polynomial commitments]] only indirectly through QAP/SNARK lineage; not a PCS paper.

## Evidence Table

| Claim | Evidence | Type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| MultiQAPs share state using succinct bus digests instead of sending intermediate state | §2.1, Figure 1 | mechanism | high | verifier avoids linear work in intermediate state |
| MultiQAP state sharing is cheaper than Pantry-style hashing when most shared state is used | §2.1.4, §7.2, Figure 7 | empirical_result | high | hashing remains better for sparse access |
| Scheduled CP soundness follows from knowledge soundness plus binding bus digests | §3.2, Theorem 1 | theorem | high | proof deferred to full paper |
| Protocol 1 adapts Pinocchio/QAPs into a commit-and-prove MultiQAP protocol | §4.2, Theorems 2-4 | construction | high | binding, knowledge soundness, perfect ZK stated |
| QAP-friendly curve choices reduce cryptographic verification cost inside QAPs | §5, §7.3 | mechanism/empirical | high | pairing degree estimate 44M vs 14K |
| Bounded bootstrapping trades universality for practical proof aggregation | §2.2, §5, §7.3.1 | design_tradeoff | high | requires schedule bounds |
| Energy-saving circuits reduce prover cryptographic work on untaken branches | §2.3, §6.5, §7.4, Figure 8 | mechanism/empirical | high | one-multiply runtime case 1.68x static |
| Geppetto's compiler handles C/LLVM programs but has semantic restrictions | §6, §7.5 | implementation/limitation | high | pointer support limited |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| Geppetto's bounded proof bootstrapping compresses many scheduled proofs into a constant-size proof under a preselected schedule bound, improving practical performance relative to unbounded bootstrapping while sacrificing some universality. | `doi:10.1109/SP.2015.23#p2,p5-p6,p15-p16` | folded_into_meta_note |
| Geppetto implements a C/LLVM-based verifiable-computation toolchain where programmers mark outsourced functions and define banks/buses to control proof schedules, state sharing, and cryptographic costs. | `doi:10.1109/SP.2015.23#p10-p14,p17` | folded_into_meta_note |
| Geppetto's energy-saving circuits rewrite runtime branches so untaken branch variables evaluate to zero, reducing cryptographic prover work toward the actually executed path rather than the worst-case branch structure. | `doi:10.1109/SP.2015.23#p6,p14,p16` | folded_into_meta_note |
| For shared-state workloads where most transferred state is used, Geppetto reports MultiQAP buses as much cheaper than Pantry-style hash-based state transfer, including about 0.03 QAP degree per byte for full field elements versus about 11.25 per byte for hashing. | `doi:10.1109/SP.2015.23#p5,p14-p15` | folded_into_meta_note |
| Geppetto's MultiQAPs decompose a computation into sub-QAPs connected by bus digests, allowing the verifier to check consistent intermediate state without receiving that state explicitly. | `doi:10.1109/SP.2015.23#p2-p4` | folded_into_meta_note |
| Geppetto's Protocol 1 adapts Pinocchio-style QAP proofs to MultiQAP relations by separating bank digest computation from the proof polynomial, yielding stated binding, knowledge-sound, and perfectly zero-knowledge commit-and-prove properties. | `doi:10.1109/SP.2015.23#p7-p9` | folded_into_meta_note |
| Geppetto reduces the cost of verifying cryptographic operations inside QAPs by selecting curve and field parameters that let elliptic-curve operations embed naturally in the QAP field; the paper estimates a pairing at QAP degree 14K instead of 44M under naive embedding. | `doi:10.1109/SP.2015.23#p9-p10,p15-p16` | folded_into_meta_note |
| Geppetto's scheduled knowledge soundness follows when the underlying commit-and-prove scheme is knowledge sound and its reused bus digests are binding, so accepted scheduled proofs share consistent committed state. | `doi:10.1109/SP.2015.23#p6-p7` | folded_into_meta_note |

## Knowledge Handoff

可吸收的来源内判断:

- `[[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto MultiQAPs share state with succinct bus digests]]`
- `[[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto MultiQAPs reduce state-sharing overhead versus hashing]]`
- `[[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto scheduled soundness relies on binding bus digests]]`
- `[[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto protocol extends Pinocchio QAPs to commit-and-prove]]`
- `[[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto QAP-friendly crypto reduces embedded crypto cost]]`
- `[[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto bounded bootstrapping trades universality for performance]]`
- `[[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto energy-saving circuits align prover cost with executed paths]]`
- `[[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto compiler targets C/LLVM with programmer-guided banks]]`

Concepts to create/update:

- Create [[qap-based-verifiable-computation-systems|Geppetto]] as a system concept.
- Create [[qap-based-verifiable-computation-systems|MultiQAPs]] as a state-sharing/proof representation concept.
- Create [[qap-based-verifiable-computation-systems|Bounded proof bootstrapping]] as a recursion/aggregation concept.
- Create [[qap-based-verifiable-computation-systems|Energy-saving circuits]] as a compiler/prover-cost concept.
- Update [[delegated-computation|Delegated computation]] with Geppetto as a system extension.

Maps/synthesis/bridge actions:

- Create `vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md`.
- Create `vault/04_Knowledge/verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems.md`.
- Create `vault/04_Knowledge/verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems.md`.
- Create `vault/05_Bridges/qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove.md`.
- Update `vault/04_Knowledge/verifiable-computation.md`.

Review/follow-up:

- Absorb Pinocchio, Pantry, Zaatar, BCTV, Buffet, and QAP/QSP foundations to calibrate comparisons.
- Confirm the full ePrint 2014/976 if theorem proofs or construction details matter.
- Treat CodePlex repository link as historical; a repo analysis is likely not actionable unless an archive is located.

## Synthesis Handoff

Geppetto should initialize `verifiable-computation/verifiable-computation-systems/geppetto`. It also strengthens the bridge from practical VC systems to modular/commit-and-prove ZKP proof systems. The topic remains `foundation_thin` because it currently has one deep system paper and needs Pinocchio/Pantry/Zaatar/BCTV foundation sources.
