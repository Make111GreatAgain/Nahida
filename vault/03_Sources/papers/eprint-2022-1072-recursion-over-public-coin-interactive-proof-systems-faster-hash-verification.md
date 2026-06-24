---
id: "iacr-eprint-2022-1072"
title: "Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification"
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
  - "p1-p2 abstract, introduction, hash-in-SNARK bottleneck, GKR route and related work"
  - "p2-p6 preliminaries for SNARKs, MiMC, sum-check and the GKR protocol"
  - "p6-p10 recursive compiler motivation, protocol layers and the Groth16 two-step verifier structure"
  - "p10-p14 security reductions, Fiat-Shamir handling, Groth16 and PLONK instantiation details"
  - "p14-p15 implementation, parallelization, MiMC benchmark and limitations"
  - "p16-p20 references and appendices for so-far digest and one-round GKR"
canonical_url: "https://eprint.iacr.org/2022/1072"
pdf_url: "https://eprint.iacr.org/2022/1072.pdf"
doi: ""
arxiv_id: ""
venue: "IACR ePrint 2022/1072 inferred from local filename; extracted text shows no DOI or venue block"
year: "2023"
authors:
  - "Alexandre Belling"
  - "Azam Soleimanian"
  - "Olivier Begassat"
affiliations:
  - "Consensys, Linea-Cryptography"
local_pdf: "~/Desktop/paper/2022-1072.pdf"
sha256: "59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
pages: 20
pdf_extractor: "pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/recursion-over-public-coin-interactive-proof-systems-faster-hash-verification-59a20b778b53-pages.txt"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
topic_ids:
  - "recursive-proof-composition"
  - "public-coin-proof-recursion"
  - "hash-verification"
  - "sum-check-protocol"
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "recursive-proof-composition"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition/iacr-eprint-2022-1072"
secondary_ontology_paths:
  - "verifiable-computation/interactive-proofs"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  directions:
    - "recursion-and-folding"
    - "interactive-proofs"
    - "proof-systems"
  topics:
    - "recursive-proof-composition"
    - "public-coin-proof-recursion"
    - "GKR"
    - "sum-check-protocol"
    - "hash-verification"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "public-coin interactive proofs"
  - "recursive proof composition"
  - "GKR"
  - "sum-check protocol"
  - "Fiat-Shamir"
  - "so-far digest"
  - "hash verification"
  - "MiMC"
  - "Groth16"
  - "PLONK"
aliases:
  - "Recursion over Public-Coin Interactive Proof Systems"
  - "Faster Hash Verification"
  - "public-coin proof recursion"
  - "GKR inside SNARK"
  - "recursive hash verification"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "recursion"
  - "interactive-proofs"
  - "sum-check-protocol"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  subdomain:
    - "recursive proof systems"
    - "public-coin interactive proofs"
    - "SNARK prover performance"
  problem:
    - "avoid proving many SNARK-friendly hash computations directly inside one outer SNARK"
    - "embed a public-coin verifier inside a SNARK without hashing the whole interactive transcript inside the circuit"
    - "shorten Fiat-Shamir inputs while preserving the binding between the GKR statement and the SNARK public-input commitment"
  method_family:
    - "public-coin argument verifier recursion"
    - "GKR verifier inside SNARK"
    - "short-input Fiat-Shamir via SNARK verification computation"
    - "so-far digest transcript model"
    - "Groth16 public-input MSM commitment"
  proof_model:
    - "general compiler secure in the random oracle model for one-round public-coin arguments under stated assumptions"
    - "concrete GKR plus outer SNARK instantiation is heuristic because later GKR random oracles become concrete in-circuit hashes"
  evaluation_context:
    - "Go implementation"
    - "gnark and gnark-crypto"
    - "BN254"
    - "AWS hpc6a 96 physical cores"
  bridge:
    - "public-coin interactive proofs to recursive proof composition"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-public-coin-proof-recursion"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0070"
safe_for_absorption: true
source_refs:
  - "iacr:2022/1072"
  - "sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
  - "pdf:~/Desktop/paper/2022-1072.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "recursion-and-folding"
secondary_directions:
  - "interactive-proofs"
  - "proof-systems"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The abstract frames the contribution as proof recursion/proof composition for faster hash verification"
  - "Sections 4-6 define a compiler that embeds a public-coin argument verifier inside a SNARK and shortens Fiat-Shamir inputs"
  - "GKR and sum-check are the public-coin/verifiable-computation tools used in the concrete instantiation, not the paper's primary knowledge layer"
  - "The paper repeatedly states a recursive technique and provides Groth16/PLONK instantiations for the outer SNARK"
taxonomy_version: "1.0"
---

# Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification

## 论文身份

- Title: Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification
- Authors: Alexandre Belling, Azam Soleimanian, Olivier Begassat
- Visible affiliation: Consensys, Linea-Cryptography
- Local PDF: `~/Desktop/paper/2022-1072.pdf`
- Stable local identity: `sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a`
- External identity: IACR ePrint `2022/1072` inferred from local filename convention; extracted text does not expose a DOI or proceedings footer.
- Extractor: `pypdf`; extraction is readable across all 20 pages, with math notation and protocol symbols degraded in places.

## 精读状态

- Reading status: `deep_read_complete`
- Coverage: abstract, introduction, SNARK/GKR/sum-check preliminaries, recursive compiler, Groth16/PLONK instantiations, Fiat-Shamir handling, implementation, benchmark, and appendices were read.
- Skipped sections: none intentionally skipped.
- Extraction gaps: formula typography, subscripts and some protocol equations are degraded; section boundaries, assumptions, protocol flow and benchmark values remain readable.
- Safe for absorption: yes. The source supports durable knowledge about public-coin proof recursion, GKR verifier embedding, short-input Fiat-Shamir handling, and recursive hash verification.

## 章节地图

| 序号 | 覆盖范围 | 证据来源 |
| --- | --- | --- |
| 1 | p1-p2 abstract, introduction, hash-in-SNARK bottleneck, MiMC/Poseidon context, GKR route | `Abstract`, `1` |
| 2 | p2-p6 related work, SNARK preliminaries, MiMC, sum-check, GKR protocol | `1.1`, `2`, `3` |
| 3 | p6-p10 compiler motivation, protocol layers, Groth16 public-input computation, avoiding long Fiat-Shamir inputs | `4`, `5` |
| 4 | p10-p14 security reductions, Fiat-Shamir transform, Groth16/PLONK instantiations | `5.3`, `5.4`, `6`, `7` |
| 5 | p14-p15 implementation, parallelization, MiMC throughput table and limitations | `8`, `9` |
| 6 | p16-p20 appendices for so-far digest and one-round GKR | `Appendix H`, `Appendix I` |

## Hierarchy Candidate Classification

| Layer | Candidate | Confidence | Evidence |
| --- | --- | --- | --- |
| L1 Domain | `zero-knowledge-proofs` | high | the source is about SNARK proof recursion and proving hash computations faster |
| L2 Direction | `recursion-and-folding` | high | contribution is proof recursion/proof composition, not only a GKR primer |
| L3 Problem | `recursive-proof-composition` | high | the compiler embeds a public-coin verifier inside an outer SNARK and reasons about recursive soundness |
| Secondary | `verifiable-computation/interactive-proofs` | high | GKR is the concrete public-coin argument system |
| Secondary | `verifiable-computation/interactive-proofs/sum-check-protocol` | high | GKR layers rely on sum-check reductions |
| Secondary | `zero-knowledge-proofs/proof-systems/zk-snarks` | medium | Groth16 and PLONK instantiations are used, but the source does not define zk-SNARKs |

Alternative placements considered: the queue path `verifiable-computation/interactive-proofs/sum-check-and-gkr` captures the tool dependency but misses the paper's durable contribution. A separate `GKR` knowledge node is deferred because this is not the canonical GKR source; the note instead updates [[interactive-proofs|Interactive proofs]] and [[sum-check-protocol|Sum-check protocol]] as source extensions.

## 一句话贡献

The paper gives a compiler-style route for proving many SNARK-friendly hash computations faster: use a public-coin argument such as GKR to prove the bulk hash work, embed the public-coin verifier inside an outer SNARK, and exploit the outer SNARK verifier structure so Fiat-Shamir hashes inside the circuit have short inputs rather than the full GKR statement/transcript.

## Problem Setting

SNARK applications often need to prove many hash computations: Merkle paths, signature-related state, commitments and blockchain data structures all push hash verification into circuits. General CPU hashes such as SHA256, Blake2 and Keccak are expensive in arithmetic circuits, so systems use SNARK-friendly hashes such as MiMC or Poseidon. Even then, proving a large batch of hashes directly inside Groth16 or a similar SNARK remains expensive.

GKR is attractive because it verifies many parallel executions of a layered arithmetic circuit with verifier work logarithmic in the batch size. For MiMC/Poseidon-style hash permutations, GKR can prove the repeated arithmetic computation cheaply relative to putting every hash round directly into the outer SNARK circuit.

The obstacle is non-interactivity and recursion. GKR is public-coin interactive; applying Fiat-Shamir naively would require hashing a large GKR statement or transcript inside the outer SNARK. That can erase the prover-time benefit because in-circuit hashing is itself costly.

## Core Method

### 1. GKR Proves the Bulk Hash Computation

The concrete instantiation uses GKR for batched hash verification. The prover proves that many MiMC permutations were evaluated correctly, and the verifier only performs a logarithmic amount of work plus layer-by-layer checks derived from sum-check. This is why the method targets highly data-parallel arithmetic circuits rather than arbitrary application logic.

The source keeps GKR as the lower-level verifiable-computation tool. It does not redefine sum-check or GKR as the top-level contribution; those belong to [[interactive-proofs|Interactive proofs]] and [[sum-check-protocol|Sum-check protocol]].

### 2. The Public-Coin Verifier Is Embedded in an Outer SNARK

The general compiler targets a one-round public-coin argument and an outer SNARK whose verifier has a two-step structure:

- a computation step compresses the public input into a short verifier computation value;
- a justification step verifies the proof using that compressed value and the proof, without reading the entire public input again.

Groth16 naturally fits this pattern because public inputs are combined through an MSM before the final pairing check. The paper also sketches a PLONK variant where the public-input polynomial contribution can be split and committed before the challenge is derived.

### 3. Short-Input Fiat-Shamir

The key trick is to avoid hashing the whole GKR statement inside the outer SNARK. Instead, the prover supplies a short commitment-like value derived from the outer SNARK verifier's public-input computation. The Fiat-Shamir challenge is then bound to this short value rather than the full statement.

This is not a free compression assumption. The prover must also prove that the short value is correctly tied to the hidden part of the public input; otherwise the prover could mix a GKR proof for one statement with an outer SNARK statement for another. The Groth16 instantiation uses an additional argument of knowledge for the MSM relation.

### 4. Layered Compiler View

The paper describes the route in layers:

- Layer 1 puts the public-coin verifier inside the outer SNARK while leaving the public-coin statement public.
- Layer 2 moves the large public-coin statement component into the witness and exposes only the verifier-computation commitment.
- Layer 3 applies Fiat-Shamir using short public material and proof messages.

This layered view is the reusable knowledge: recursive composition can sometimes be made efficient not by making the inner verifier magically tiny, but by exploiting how the outer SNARK verifier already compresses public inputs.

### 5. So-Far Digest and One-Round GKR

The appendices supply an important transcript boundary. Instead of hashing an ever-growing transcript, the paper uses a so-far digest model where each digest absorbs the newest message and previous digest. This supports the short-input reasoning.

For concrete GKR, the paper needs a one-round public-coin form. It keeps the initial challenge public-coin/random-oracle derived, then derives later challenges from the previous challenge and prover message. Because later random oracle calls become concrete hashes inside the outer SNARK, the concrete GKR+SNARK instantiation is explicitly only heuristic, even though the abstract compiler is proved in the random oracle model.

## Groth16 and PLONK Instantiations

For Groth16, the public-input contribution is an MSM over verification-key elements. The short binding value is the MSM contribution for the GKR statement component. A separate proof shows knowledge of that component and correctness of the MSM relation. The pairing equation for that auxiliary proof relies on setup material tied to the split verification key.

For PLONK, the paper explains why the original verifier transcript is not directly compatible: the public-input polynomial evaluation is part of the Fiat-Shamir flow. The proposed variant commits to a split public-input polynomial contribution so the transcript can be made compatible with the compiler's short-input requirement.

The practical takeaway is that the compiler is generic only for SNARKs whose verifier computation can be split in the required way. It is not a blanket statement that every SNARK can cheaply recurse every public-coin proof.

## Evaluation

The implementation is in Go, uses gnark/gnark-crypto and BN254, and benchmarks on an AWS hpc6a machine with 96 physical cores and 384GB memory. The paper reports engineering work around parallelization overhead, memory pooling and arithmetic operation reduction.

Key reported benchmark facts:

- direct Groth16 for `2^18` MiMC permutations: 38.3s and about 6,835 permutations/s;
- recursive GKR+Groth16 route for `2^19` to `2^24` hashes: total proving time grows from 7.6s to 78.9s;
- reported throughput grows from about 68,400 hashes/s to 212,000 hashes/s over that range;
- the paper describes the speedup over direct MiMC-in-Groth16 proving as about 35x in the larger benchmark regime;
- dependency checks between hash instances are reported as negligible relative to permutation cost.

These numbers are source-local measurements. They should not be reused as current gnark/Groth16/BN254 performance without a fresh benchmark.

## 创新点

1. Uses public-coin argument recursion as a practical SNARK prover-performance route for batched hash verification.
2. Identifies the in-circuit Fiat-Shamir hash input length as the core obstacle when embedding GKR in a SNARK.
3. Uses the outer SNARK verifier's public-input computation step as a short binding value for the public-coin statement.
4. Supplies Groth16 and PLONK-style instantiation paths, with explicit assumptions on verifier structure.
5. Separates an abstract compiler proof in the random oracle model from the heuristic concrete one-round GKR instantiation.

## 局限与外推边界

- The concrete GKR+outer-SNARK instantiation is heuristic because later GKR random-oracle calls are replaced by concrete hashes inside the outer SNARK.
- The method targets one-round public-coin arguments or arguments that can be compiled into the required form.
- The outer SNARK must have a compatible two-step/splittable verifier computation; the paper gives Groth16 and a PLONK variant, not an exhaustive proof for all SNARKs.
- GKR is best suited to layered/data-parallel arithmetic circuits; arbitrary non-layered computation needs a suitable transformation or a different public-coin argument.
- The speedup claims are for MiMC/hash-verification workloads and one implementation/hardware setup.
- The method improves prover performance for hash verification; it does not by itself provide application-level soundness for Merkle semantics, signatures, bridge finality or data availability.

## Knowledge Absorption

| Target layer | Absorption decision |
| --- | --- |
| [[recursive-proof-composition|Recursive proof composition]] | Add method route: public-coin argument verifier recursion with short Fiat-Shamir inputs. |
| [[recursion-and-folding|Recursion and folding]] | Add source extension under recursive proof composition, separate from folding/Nova and Halo nested amortization. |
| [[interactive-proofs|Interactive proofs]] | Add source extension showing GKR/public-coin arguments as a tool embedded into SNARK recursion, not a new foundation definition. |
| [[sum-check-protocol|Sum-check protocol]] | Add source extension: GKR/sum-check supports batched hash verification, but the paper is not canonical sum-check evidence. |
| [[public-coin-interactive-proofs-to-recursive-proof-composition|Public-coin interactive proofs -> recursive proof composition]] | Create bridge for the transferable pattern and its non-transfer boundary. |

## Retrieval Notes

- Use this note for: public-coin proof recursion, GKR inside SNARK, short-input Fiat-Shamir for recursive composition, MiMC hash verification acceleration, and Groth16 public-input MSM binding.
- Do not use this note as the primary definition of GKR, sum-check, Groth16, PLONK or zk-SNARKs.
- Compare with [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Halo]]: Halo defers linear PCS verifier work through nested amortization; this paper embeds a public-coin verifier and shortens Fiat-Shamir inputs through SNARK verifier computation.
- Compare with [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] and [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]]: those focus on prover memory/elasticity; this source focuses on hash-verification prover time through public-coin recursion.

## Open Questions

| Question | Why it matters | Status |
| --- | --- | --- |
| Need canonical GKR source note. | Current GKR knowledge is applied through multiple sources, but the vault still lacks the primary GKR paper as a foundation source. | queued |
| Need comparison with accumulation schemes. | The next queue item Arc is likely relevant for distinguishing public-coin recursion from accumulation/folding routes. | next_pending |
| Need current implementation/repository status if used operationally. | Benchmarks are paper-local and should not be treated as current gnark/Linea performance. | optional |

