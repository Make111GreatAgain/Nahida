---
id: "sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes"
title: "Arc: Accumulation for Reed-Solomon Codes"
original_title: "ARC: Accumulation for Reed-Solomon Codes"
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
  - "p1-p6 abstract, introduction, results, related work and Table 1 efficiency comparison"
  - "p7-p13 techniques: IOR motivation, RS proximity accumulation, R1CS/NP accumulation and PCD from reductions"
  - "p14-p17 preliminaries: relations, Reed-Solomon codes, list decoding, quotients, proximity gaps and Merkle trees"
  - "p18-p23 non-interactive reductions and interactive oracle reductions"
  - "p24-p27 RS proximity accumulation construction, soundness and optimizations"
  - "p28-p35 R1CS/NP accumulation construction, soundness, arbitrary-polynomial extension and FFT/list-decoding notes"
  - "p36-p39 references for prior PCD, folding, FRI/STIR and hash-based accumulation context"
  - "p40-p57 appendices: reductions-to-ARG/ACC wrapper and IOR-to-noninteractive reduction proof boundary"
canonical_url: ""
canonical_url_note: "Possible IACR ePrint 2024/1731 inferred from filename `2024-1731.pdf`, but no external URL was fetched or verified in this run."
pdf_url: ""
doi: ""
arxiv_id: ""
venue: "unknown; local PDF does not expose a venue block"
year: "2024"
authors:
  - "Benedikt Bunz"
  - "Pratyush Mishra"
  - "Wilson Nguyen"
  - "William Wang"
affiliations:
  - "New York University"
  - "University of Pennsylvania"
  - "Stanford University"
local_pdf: "~/Desktop/paper/2024-1731.pdf"
sha256: "12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
pages: 57
pdf_extractor: "codex-bundled-python:pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/arc-accumulation-for-reed-solomon-codes-12ffa8e928a8-pages.txt"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
topic_ids:
  - "accumulation-schemes"
  - "reed-solomon-proximity-accumulation"
  - "recursive-proof-composition"
  - "fri-iopps"
  - "proof-carrying-data"
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "accumulation-schemes"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/accumulation-schemes/sha256-12ffa8e928a8"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/fri-iopps"
  - "zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  directions:
    - "recursion-and-folding"
    - "proof-systems"
  topics:
    - "accumulation-schemes"
    - "Reed-Solomon proximity"
    - "interactive oracle reductions"
    - "proof-carrying-data"
    - "IVC"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "accumulation schemes"
  - "Reed-Solomon codes"
  - "Reed-Solomon proximity claims"
  - "interactive oracle reductions"
  - "proof-carrying data"
  - "IVC"
  - "PCD"
  - "random oracle model"
  - "Merkle commitments"
  - "list decoding"
aliases:
  - "ARC"
  - "Arc"
  - "Accumulation for Reed-Solomon Codes"
  - "hash-based accumulation"
  - "RS proximity accumulation"
  - "2024-1731"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "recursion"
  - "accumulation-schemes"
  - "reed-solomon"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "recursive proof systems"
    - "transparent/hash-based proof systems"
  problem:
    - "build unbounded-depth accumulation without homomorphic vector commitments"
    - "accumulate Reed-Solomon proximity claims while preserving distance"
    - "derive PCD/IVC-friendly accumulation for NP/R1CS using only random oracles"
  method_family:
    - "Reed-Solomon proximity accumulation"
    - "interactive oracle reductions"
    - "Merkle-committed oracle reductions"
    - "out-of-domain list-decoding binding"
    - "quotient-based distance-preserving reduction"
  proof_model:
    - "random oracle model"
    - "round-by-round soundness"
    - "straightline knowledge soundness"
    - "Fiat-Shamir transformation for IORs"
  evaluation_context:
    - "formal asymptotic comparison"
    - "Table 1 IVC overhead comparison"
    - "concrete verifier-circuit estimate for R1CS accumulation"
  bridge:
    - "FRI IOPPs to accumulation schemes"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260623-arc-accumulation-reed-solomon"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0071"
safe_for_absorption: true
source_refs:
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
  - "pdf:~/Desktop/paper/2024-1731.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "recursion-and-folding"
secondary_directions:
  - "proof-systems"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The title and abstract identify the contribution as accumulation for Reed-Solomon codes."
  - "Sections 2, 6 and 7 define accumulation schemes rather than a standard folding scheme."
  - "The paper repeatedly positions accumulation as a PCD/IVC route adjacent to folding schemes."
  - "The RS proximity machinery creates a bridge to FRI/IOPPs, but the primary durable path is accumulation schemes under recursion-and-folding."
taxonomy_version: "1.0"
---

# Arc: Accumulation for Reed-Solomon Codes

## 论文身份

- Title: ARC: Accumulation for Reed-Solomon Codes
- Authors: Benedikt Bunz, Pratyush Mishra, Wilson Nguyen, William Wang
- Date shown in PDF: October 25, 2024
- Local PDF: `~/Desktop/paper/2024-1731.pdf`
- Stable local identity: `sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c`
- External identity: possible IACR ePrint `2024/1731` inferred only from filename; this run did not fetch or verify external metadata.
- Extractor: Codex bundled Python `pypdf`; text is readable across all 57 pages, with formula/subscript degradation typical of PDF extraction.

## 精读状态

- Reading status: `deep_read_complete`
- Coverage: abstract, introduction/results, related work, techniques, preliminaries, formal constructions, security arguments, optimizations, comparison table, and appendices were read.
- Skipped sections: none intentionally skipped.
- Extraction gaps: mathematical notation, superscripts/subscripts, and some set/field symbols are degraded. Section boundaries, theorem statements, protocol steps, and efficiency comparisons remain usable.
- Safe for absorption: yes. The paper supports durable updates about accumulation schemes, RS proximity accumulation, IORs, and the FRI/IOPP-to-accumulation bridge.

## 章节地图

| Section/Page | 内容 | 作用 |
| --- | --- | --- |
| p1-p6, `1 Introduction` | PCD/IVC motivation, prior accumulation routes, homomorphic vector commitment cost, BMNW24 bounded-depth limitation, main results and Table 1 | establishes problem and contribution |
| p7-p13, `2 Techniques` | IOR motivation; RS proximity accumulation sketch; R1CS/NP accumulation; reductions-to-PCD route | explains mechanism before formalization |
| p14-p17, `3 Preliminaries` | indexed/promise relations, Reed-Solomon codes, list decoding, quotients, proximity gaps, Merkle commitments | defines formal ingredients |
| p18-p19, `4 Non-interactive reductions` | reductions in ROM and theorem turning cast/fold reductions into ARG/ACC | formal bridge from reductions to accumulation |
| p20-p23, `5 Interactive oracle reductions` | IOR definition, round-by-round soundness/knowledge, committed relations, IOR-to-noninteractive theorem | proof model for oracle-message reductions |
| p24-p27, `6 Accumulation for Reed-Solomon proximity claims` | Construction 6.3, Theorem 6.2, soundness, delayed FFT and list-decoding conjecture optimization | core RS proximity accumulator |
| p28-p35, `7 Accumulation for NP` | R1CS accumulator relation, Construction 7.2 and 7.5, soundness, arbitrary-polynomial extension, practical OOD sample note | lifts RS proximity accumulation into NP/R1CS accumulation |
| p40-p46, Appendix A | definitions of non-interactive arguments and accumulation; wrapper construction from reductions | supports Theorem 4.3 |
| p47-p57, Appendix B | IOR-to-noninteractive construction with Merkle commitments and Fiat-Shamir | supports Theorem 5.9 |

## Hierarchy Candidate Classification

| Layer | Candidate | Confidence | Evidence |
| --- | --- | --- | --- |
| L1 Domain | `zero-knowledge-proofs` | high | the paper targets SNARK/PCD/IVC proof systems |
| L2 Direction | `recursion-and-folding` | high | PCD, accumulation/folding, IVC and recursive proof construction are the central motivation |
| L3 Topic | `accumulation-schemes` | high | the contribution is a new accumulation scheme and the paper compares accumulation routes |
| Secondary | `zero-knowledge-proofs/proof-systems/fri-iopps` | high | RS proximity, quotients, list decoding and STIR/FRI-style IOPP tools are reused |
| Secondary | `zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | high | accumulation schemes are used to build PCD/IVC and recursive proof systems |
| Source instance | `ARC` | high | paper-specific named construction; stays as source extension, not a foundation node |

The queue placed this paper under `folding-schemes`. That was close but too broad: the paper treats folding as adjacent prior work while its actual contribution is accumulation schemes, especially hash-based RS proximity accumulation.

## 一句话贡献

ARC constructs unbounded-depth, hash-based accumulation schemes by reducing many Reed-Solomon proximity claims into one distance-preserving proximity claim, then lifting that primitive into accumulation for NP/R1CS and PCD/IVC without relying on homomorphic vector commitments.

## Problem Setting

Proof-carrying data (PCD) and incrementally verifiable computation (IVC) need a way to keep verifying an ever-growing computation without making the verifier or recursive circuit grow with the number of steps. Accumulation schemes address this by combining many proof obligations or accumulator instances into a new accumulator whose final check is independent of the accumulated history length.

The paper positions prior routes as having three pain points:

- Homomorphic vector commitment based accumulation is expensive and usually rests on number-theoretic assumptions such as discrete logarithm or lattice assumptions.
- IOP/SNARK recursion can use hash-based transparent proofs, but putting the whole SNARK verifier inside another circuit can create high overhead.
- The prior hash-based accumulation route BMNW24 avoids homomorphic commitments but has a fixed bound on consecutive accumulation steps; exceeding it affects both efficiency and security.

ARC aims to keep the hash/random-oracle benefits of IOP-based systems while removing the bounded-depth restriction.

## Core Method

### RS Proximity Accumulation

The core primitive is a many-to-one reduction for claims of the form: a word is close to a Reed-Solomon code. A naive random linear combination of two words creates a virtual object and does not by itself produce a compact new claim. The prior spot-check route can reduce size but degrades the distance parameter, which forces bounded-depth accumulation.

ARC changes the new claim. After the verifier samples a random linear-combination challenge and in-domain query points, the prover sends a new word. The verifier computes the claimed combined evaluations at sampled points and forms a quotient. The new claim is that this quotient is close to a lower-degree Reed-Solomon code. Because the quotient carries only the new word and sampled auxiliary values, the claim size does not grow with the number of inputs.

The crucial property is distance preservation: if an input is far from the code, then with high probability the quotient remains far from the corresponding lower-degree code. This is what makes unbounded accumulation possible.

### List-Decoding Radius and Out-of-Domain Binding

The simple explanation assumes the unique-decoding radius. To move closer to the list-decoding radius, ARC uses out-of-domain samples: after the prover sends the new word, the verifier samples points outside the evaluation domain and asks for evaluations. Under list-decoding assumptions/bounds, these samples bind the prover to a unique nearby codeword in the list. This enables better query complexity and concrete efficiency, but the note should keep it as a stated source claim tied to Sections 2, 3, 6 and 7 rather than a general theorem for all codes.

### Accumulation for NP/R1CS

The paper lifts RS proximity accumulation into accumulation for R1CS/NP. It defines an accumulator relation with oracle strings and rational constraints:

- one oracle string behaves like the RS proximity accumulator;
- another represents accumulated witness material;
- the relaxed relation uses list-decoding/proximity conditions rather than exact codeword equality.

Construction 7.2 casts an R1CS claim into the accumulator relation by encoding the witness as a Reed-Solomon word and using a random evaluation of the R1CS constraint polynomial. Construction 7.5 reduces multiple accumulator instances into one using Lagrange interpolation over input instances, a quotient polynomial, random linear combinations, out-of-domain samples and in-domain queries.

The paper also states that the route extends beyond R1CS to more general polynomials, including higher-degree/customizable constraint systems, at the cost of a higher-degree quotient polynomial and a corresponding soundness term.

### Interactive Oracle Reductions

ARC introduces interactive oracle reductions (IORs) to formalize protocols where:

- instances may include oracle strings;
- verifier messages/query access interact with prover oracle messages;
- the verifier outputs a new instance instead of only accepting/rejecting.

IORs are the proof-model layer that makes the RS proximity and R1CS accumulation protocols modular. The paper then compiles IORs to non-interactive reductions in the random oracle model using Merkle commitments plus a Fiat-Shamir style transformation. This is important because the final accumulation/PCD story needs non-interactive reductions, not only interactive oracle protocols.

### Reductions to ARG/ACC and PCD

The paper uses a reduction blueprint:

- `RDXCAST`: cast the original relation into an accumulator relation.
- `RDXFOLD`: reduce many accumulator instances into one accumulator instance.

Theorem 4.3 and Appendix A show how these reductions produce a non-interactive argument and an accumulation scheme. Prior PCD constructions can then use the accumulation scheme, assuming the required succinct verifier conditions.

## Efficiency and Evidence

| Claim | Evidence anchor | Note |
| --- | --- | --- |
| ARC removes the bounded-depth restriction of BMNW24 | p3-p6 intro/results; p7-p9 technique | source claim, supported by distance-preserving reduction |
| RS proximity accumulator uses a small number of Merkle openings relative to code rate | p4, p24-p27 | theorem-level/asymptotic statement; exact constants depend on parameters and conjectures |
| Table 1 compares IVC overhead against PIOP+STIR and BMNW24 | p5 | formal comparison, not an implementation benchmark |
| Direct R1CS accumulation route is simpler/more efficient than the PIOP replacement route for new systems | p4-p5, p28-p35 | source claim based on construction shape and estimates |
| Delayed FFT optimization can avoid recomputing codeword fills every step | p27, p34-p35 | optimization with probability/parameter caveats |
| Security is in the random oracle model, then heuristically instantiated with concrete hashes | p18-p19, p47-p57 | important deployment boundary |

### Comparison Table Interpretation

The table on p5 compares IVC schemes for PCD over a tree of depth `d` and arity `m`. The important retrieval-level takeaway is:

- BMNW24 has overhead that depends on the bounded depth parameter.
- ARC's direct route has per-step Merkle-opening overhead depending mainly on the code rate/security parameter, not on a predeclared maximum IVC length.
- All rows except BMNW24 rely on conjectures about proximity gaps in the list-decoding radius.

This is not an experimental table. It is an asymptotic/design comparison and should not be used as a production benchmark.

## Assumptions and Boundaries

- Random oracle model: constructions and transformations are analyzed in ROM; concrete hash instantiation is heuristic in the usual Fiat-Shamir/random-oracle sense.
- Reed-Solomon/list-decoding conditions: field size, rate, distance, out-of-domain samples and proximity-gap/list-decoding assumptions matter.
- Merkle commitments: the noninteractive compilation relies on Merkle commitment completeness and multi-extractability.
- Not a general polynomial commitment result: ARC uses Merkle commitments to RS codewords, not homomorphic vector commitments or full arbitrary-point polynomial commitment APIs.
- Not a folding scheme: folding schemes are adjacent prior work; ARC is better routed through `accumulation-schemes`.
- No implementation benchmark: the paper gives formal/protocol efficiency and rough gate estimates, but no end-to-end implementation evaluation.

## Knowledge Handoff

| Target | Handling | Delta |
| --- | --- | --- |
| [[accumulation-schemes|Accumulation schemes]] | create/update knowledge node | define accumulation schemes as a reusable method family under recursion/folding; add hash-based RS proximity route |
| [[recursion-and-folding|Recursion and folding]] | update parent direction | add accumulation schemes as child node and Arc as representative source extension |
| [[recursive-proof-composition|Recursive proof composition]] | update route | add accumulation-based PCD/IVC route and note that ARC provides an unbounded hash-based accumulation path |
| [[fri-iopps|FRI IOPPs]] | update adjacent method family | add source extension for RS proximity/list-decoding tools transferred into accumulation |
| [[fri-iopps-to-accumulation-schemes|FRI IOPPs -> accumulation schemes]] | create bridge | record typed method-transfer/dependency from FRI/IOPP RS proximity machinery to accumulation schemes |
| [[polynomial-commitments|Polynomial commitments]] | no direct patch | ARC is a contrast against homomorphic vector commitments; not a PCS foundation source |

## Cold-Start Hierarchy Discovery

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | zero-knowledge-proofs | SNARKs, PCD, IVC, accumulation/folding throughout | high | existing domain |
| Background | PCD/IVC and recursive proof systems | p3-p6 | high | update parent direction and recursive composition |
| Research problem | unbounded accumulation without homomorphic vector commitments | p1-p6 | high | new `accumulation-schemes` node |
| Foundation concepts | Reed-Solomon codes, IOPPs/FRI, Merkle commitments, random oracle model | p14-p17, p20-p27 | high | bridge/update existing FRI node; foundation gaps remain |
| Method family | RS proximity accumulation, IOR-to-noninteractive reductions | p7-p13, p20-p35, appendices | high | knowledge route/source extension |
| Application/evaluation context | PCD/IVC, recursive proof systems, IOP-based SNARK deployments | p3-p6, p12-p13 | high | recursive-proof-composition update |
| Source instance | ARC | title/abstract | high | source note only |

## Retrieval Optimization

This source should help future queries such as:

- "hash-based accumulation schemes 是什么?"
- "Arc 解决了 BMNW24 bounded-depth 的什么问题?"
- "FRI/RS proximity 和 accumulation schemes 有什么关系?"
- "accumulation 和 folding 在递归证明里怎么区分?"
- "PCD/IVC 不用 homomorphic vector commitments 的路线是什么?"

Future agents should answer these first from [[accumulation-schemes|Accumulation schemes]] and [[fri-iopps-to-accumulation-schemes|FRI IOPPs -> accumulation schemes]], opening this source note only for Arc-specific protocol steps, theorem conditions, and efficiency constants.

## Domain Dynamics Impact

- L1 domain: `zero-knowledge-proofs`
- Action: `unchanged`
- Reason: the source materially improves a child method family but does not by itself change the domain-level research dynamics note. It should be considered in a future ZKP dynamics refresh together with the remaining queue items on recursive/accumulation/FRI proof systems.

## Foundation Candidate Judgment

| Candidate | Judgment | Reason |
| --- | --- | --- |
| Accumulation schemes | knowledge_node | reusable method family; Arc plus prior source context make it a useful retrieval node |
| ARC | source_instance | paper-specific construction; details stay here |
| Reed-Solomon proximity accumulation | source-backed route / possible future child | currently one deep source; keep as method route under accumulation schemes |
| Interactive oracle reductions | source-backed method/formalism | useful, but currently source-specific enough to stay inside accumulation schemes and source note |
| FRI IOPPs | existing method-family node | Arc provides adjacent RS proximity transfer evidence, not FRI foundation |
| Homomorphic vector commitments | foundation gap/review | important contrast, but no dedicated source in vault in this run |

## Review Items

| Item | Reason | Suggested action |
| --- | --- | --- |
| Verify external identity for `2024/1731` | filename suggests IACR ePrint, but this run stayed local-PDF-only | future metadata cleanup may verify ePrint URL |
| Original FRI/STIR/DEEP-FRI sources | Arc depends on RS proximity/list-decoding literature; vault FRI node remains foundation-thin | queue foundation/source updates |
| Accumulation/folding taxonomy | Arc creates a separate accumulation node; future Protostar/ProtoGalaxy/HyperNova sources may refine boundaries | revisit after queued sources |
| Homomorphic VC vs Merkle/RS route | current note uses Arc's contrast only | add foundation sources if this becomes a repeated query |
