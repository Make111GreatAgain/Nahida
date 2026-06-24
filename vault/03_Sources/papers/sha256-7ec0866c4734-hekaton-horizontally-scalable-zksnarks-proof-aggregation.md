---
id: "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
title: "Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
source_kind: "paper"
source_subtype: "local_pdf"
reading_depth: "deep_read"
paper_title: "Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation"
authors:
  - "Michael Rosenberg"
  - "Tushar Mopuri"
  - "Hossein Hafezi"
  - "Ian Miers"
  - "Pratyush Mishra"
year: "2024"
publication_date: "2024-08-09"
doi: ""
arxiv_id: ""
eprint_id: "2024/1208 (inferred from filename; not externally verified)"
canonical_url: ""
local_pdf: "~/Desktop/paper/2024-1208.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/hekaton-horizontally-scalable-zksnarks-via-proof-aggregation-7ec0866c4734-pages.txt"
sha256: "7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
page_count: 49
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "distributed-proof-generation"
  - "snark-proof-aggregation"
  - "proof-system-benchmarking"
  - "zk-snarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "distributed-proof-generation"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation/sha256-7ec0866c4734"
secondary_ontology_paths:
  - "zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation/sha256-7ec0866c4734"
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking/sha256-7ec0866c4734"
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-7ec0866c4734"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "Abstract and Introduction frame the durable problem as prover-side time/space scalability for large zkSNARK computations."
  - "Sections 1.2 and 6.2 compare Hekaton with distributed zkSNARK systems and describe a coordinator/worker prover workflow."
  - "Sections 2, 5 and 6 show proof aggregation is the main method, not the only problem domain."
source_relation_edges:
  - from: "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
    relation: "evidences"
    to: "nahida-knowledge-distributed-proof-generation"
    confidence: "high"
    status: "active_seed"
  - from: "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
    relation: "evidences"
    to: "nahida-knowledge-snark-proof-aggregation"
    confidence: "high"
    status: "active_seed"
  - from: "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
    relation: "evidences"
    to: "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
    confidence: "high"
    status: "active_seed"
domains:
  - "zero-knowledge-proofs"
topics:
  - "Hekaton"
  - "divide-and-aggregate"
  - "distributed zkSNARKs"
  - "SNARK proof aggregation"
  - "Mirage"
  - "commit-carrying zkSNARKs"
  - "partition-friendly memory checking"
  - "verifiable key directories"
  - "verifiable RAM computation"
aliases:
  - "HEKATON"
  - "Hekaton"
  - "DNA zkSNARK"
  - "divide-and-aggregate zkSNARK"
query_keys:
  - "Hekaton horizontally scalable zkSNARK"
  - "divide-and-aggregate zkSNARK"
  - "distributed proof generation via proof aggregation"
  - "partition-friendly memory checking"
  - "Mirage proof aggregation"
  - "heterogeneous commit-carrying aggregation"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "zk-snarks"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-hekaton-proof-aggregation"
source_refs:
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
confidence: "high"
trust_tier: "primary"
---

# Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation

## Source Identity

| Field | Value |
| --- | --- |
| Title | Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation |
| Authors | Michael Rosenberg; Tushar Mopuri; Hossein Hafezi; Ian Miers; Pratyush Mishra |
| Date in PDF | 2024-08-09 |
| Local PDF | `~/Desktop/paper/2024-1208.pdf` |
| SHA-256 | `7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11` |
| Pages | 49 |
| Metadata caveat | Filename suggests IACR ePrint `2024/1208`, but no external metadata lookup was performed in this run. |

## Reading Coverage

| Section | Pages | Coverage |
| --- | --- | --- |
| Abstract and Introduction | p1-p5 | Problem, contributions, relation to DIZK/deVirgo/Pianist/Mangrove, application claims. |
| Techniques | p6-p10 | Divide-and-aggregate blueprint, partition-friendly memory checking, heterogeneous commit-carrying aggregation, optimizations. |
| Preliminaries | p11-p13 | Commitment schemes, commit-carrying zkSNARKs, aggregation relation. |
| Partitioning circuits via memory checking | p14-p19 | k-CSAT to k-RCSAT, ROM circuits, memory traces, Merkle-root public input, Lemmas 4.1/4.8. |
| Aggregation scheme for Mirage | p20-p25 | Mirage background, multiple pairing product protocol, multi-circuit aggregation construction. |
| Divide-and-aggregate zkSNARKs | p26-p28 | DNA.G/P/V, distributed prover workflow, SRS/public-input optimization. |
| Implementation and Evaluation | p29-p35 | Rust/arkworks/OpenMPI implementation, cluster setup, scaling experiments, VKD and RAM applications. |
| Appendices | p36-p44 | Cluster architecture choices, zero-finding lemma, completeness/soundness/zero-knowledge proof of Theorem 6.1. |
| References | p45-p47 | Related prior work used for routing and follow-up gaps. |

## One-Sentence Memory

Hekaton constructs a distributed zkSNARK by partitioning a large circuit into subcircuits, proving chunks in parallel with a commit-carrying inner SNARK, and aggregating the chunk proofs and trace commitments into one succinct proof; its reusable contribution is the composition of distributed proof generation with proof aggregation plus a partition-friendly memory checker for shared wires.

## Problem Setting

The paper targets a prover-side scalability bottleneck in zkSNARKs: realistic computations can generate very large arithmetic circuits, and conventional provers pay roughly linear time and memory in circuit size. The authors highlight two practical pain points in p3: expensive operations have diminishing parallelization once cores, processors and clusters communicate, and prover memory can become the hard limit.

The durable research problem is therefore not “define zk-SNARKs” and not “benchmark one Rust implementation.” It is: how can a proof system horizontally scale the proving of one very large computation while keeping final proof size and verifier work succinct?

## Contributions

| Contribution | What It Adds | Evidence Anchor | Reusable Placement |
| --- | --- | --- | --- |
| Divide-and-aggregate (DNA) framework | Partition circuit `C` into subcircuits, prove each with an inner zkSNARK, then aggregate chunk proofs into one proof. | p3-p4, p6, p26-p27 | [[distributed-proof-generation|Distributed proof generation]] and [[snark-proof-aggregation|SNARK proof aggregation]] |
| Multi-circuit aggregation | Extends proof aggregation so different subcircuits/circuits can be aggregated, rather than only repeated uniform circuits. | p4, p8-p10, p22-p25 | [[snark-proof-aggregation|SNARK proof aggregation]] |
| Shared wires through global memory | Replaces cross-subcircuit wires with memory accesses and verifies memory consistency with a partitionable trace checker. | p4, p6-p7, p14-p19 | [[distributed-proof-generation|Distributed proof generation]] |
| Commit-carrying aggregation | Aggregates both inner proofs and commitments so random challenges can be derived from succinct aggregate commitments. | p8-p10, p24-p27 | [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]] |
| Mirage instantiation | Instantiates DNA using Mirage, a commit-carrying Groth16-style SNARK, plus a new aggregation scheme based on multiple pairing product/TIPP machinery. | p8-p10, p20-p25 | [[snark-proof-aggregation|SNARK proof aggregation]] |
| Distributed implementation | 5400 lines of Rust over arkworks with OpenMPI and SLURM, using scatter-gather commit and proving phases. | p29, p36-p37 | Source-local implementation evidence |
| Evaluation and applications | Shows horizontal scaling, reports proof/verifier/communication behavior, and applies Hekaton to VKD updates and RAM computations. | p30-p35 | [[proof-system-benchmarking|Proof-system benchmarking]] as source-local benchmark evidence |

## Mechanism Detail

### DNA Workflow

Hekaton’s DNA construction has a fan-out/fan-in shape:

1. Partition the original circuit into subcircuits.
2. Replace wires crossing subcircuit boundaries with accesses to a global read-only memory bank.
3. Generate memory traces and split them across subcircuits.
4. Each worker commits to its subtrace and later proves its augmented subcircuit with the inner commit-carrying SNARK.
5. A coordinator aggregates commitments to derive challenges, then aggregates proofs into a single final proof.

This is why Hekaton belongs primarily to [[distributed-proof-generation|Distributed proof generation]]: it is trying to reduce per-worker time and memory by distributing a single large proving task. It also belongs to [[snark-proof-aggregation|SNARK proof aggregation]] because proof aggregation is the fan-in mechanism that prevents the verifier from checking many subproofs.

### Partition-Friendly Memory Checking

The main obstacle in partitioned circuits is shared wires. A naive approach would pass many shared values between neighboring chunks; proof aggregation schemes remain succinct only when neighboring chunks share a small amount of data. Hekaton instead stores shared wire values in a global memory bank and has subcircuits read them.

The memory-checking route:

- Converts circuit partitions into ROM circuits, replacing shared wires with read gates.
- Builds two memory traces: subcircuit-sorted trace `TTT` and address-sorted trace `AAA`.
- Checks local ordering/consistency inside each subtrace.
- Uses randomized fingerprinting to check that `TTT` and `AAA` are permutations.
- Maintains running products across subcircuits and records boundary state in a Merkle tree so each subcircuit only needs neighboring leaf/path data.

The paper states that this costs 13 constraints per shared wire in the technique overview, which is a source-local implementation/evaluation claim, not a general evergreen property of all distributed proving systems.

### Commit-Carrying Aggregation

The memory checker needs challenges derived after committing to traces. If the verifier had to inspect all subcircuit commitments, the final proof would lose succinctness. Hekaton defines a commit-carrying aggregation scheme that aggregates the commitments themselves and uses the aggregate commitment to derive random challenges.

This is a key bridge point: distributed proving produces many chunk commitments and proofs; SNARK proof aggregation supplies the mechanism that compresses both proof validity and commitment consistency into a single verifier-facing object.

### Mirage Aggregation

Hekaton instantiates the inner proof with Mirage, a commit-carrying Groth16-style zkSNARK. The paper adapts Groth16/SnarkPack-style inner-pairing product ideas to Mirage and heterogeneous circuits:

- A Mirage proof has Groth16-like `(A, B, C)` plus a commitment `D`.
- Aggregation must account for different verifying-key components across subcircuits.
- Verifier-supplied vectors such as `delta` and `eta` cannot be committed by the prover; commitments are computed at setup and included in the verifying key.
- Multiple pairing products are batched into a single TIPP instance, reducing the number of TIPP proofs.

This is not the same route as SnarkFold. SnarkFold uses split IVC/folding for proof aggregation; Hekaton uses a Mirage/TIPP-style aggregation scheme as part of a distributed prover.

## Formal Evidence

| Formal Item | What It Supports | Notes |
| --- | --- | --- |
| Lemma 4.1 | Reduces partitioned circuit satisfiability into multiple CSAT instances while preserving completeness and knowledge soundness under committed traces. | p14-p15 |
| Lemma 4.6 | Shared-wire elimination from k-CSAT to k-RCSAT. | p15-p16 |
| Lemma 4.8 | Memory-trace transformation yields satisfiable subcircuits iff the ROM circuit is satisfiable, with random challenges derived from commitments. | p18-p19 |
| Theorem 5.4 | Multiple pairing product protocol is a SNARK for the required relation and runs one TIPP prover. | p22-p23 |
| Theorem 6.1 | DNA construction is a zkSNARK for CSAT with a horizontally scalable distributed prover. | p26, proof p39-p44 |
| Zero-knowledge proof sketch | DNA can be zero-knowledge when the inner commit-carrying SNARK has multi-instance zero-knowledge and the Merkle commitments hide leaves. | p43-p44 |

## Implementation And Evaluation

| Area | Source-Local Detail | Handoff Caution |
| --- | --- | --- |
| Code | 5400 lines of Rust using arkworks; implements partitionable circuit API, Mirage cc-zkSNARK, Mirage aggregation, OpenMPI coordinator/workers and applications. | The PDF says code will be open-sourced shortly; repository was not analyzed. |
| Cluster | AMD EPYC 7763 nodes with 128 cores and 512GB RAM; OpenMPI and SLURM; two scatter-gather rounds. | Hardware and cluster pricing are source-local. |
| Worker configuration | Each MPI node runs 32 provers, each using one core and about 4GB memory; subcircuit size fixed around 1.3M constraints in experiments. | Not a universal optimal configuration. |
| Scaling | Evaluation reports latency/throughput scaling across 128 to 4096 cores and circuit sizes up to `2^35` constraints; abstract says `2^35` gates can be proved in under an hour. | Exact graph values require figure inspection; use the source note before quoting numbers. |
| Communication | Table 2 reports less than 1MB per subcircuit communication in the measured settings, with proof/commit response sizes not varying with circuit parameters. | Table numbers are for this implementation/configuration. |
| Proof/verifier | Largest test at `2^18` subcircuits reports 32kB proof and 83ms verification. | Proof size and verifier time grow logarithmically for Hekaton; Pianist has constant proof/verifier in Table 1. |
| Aggregation | Aggregation happens on one machine in the current implementation and grows with number of subproofs. | Paper leaves distributed aggregation as future work. |
| Pianist comparison | Authors could not run Pianist stably beyond certain sizes on their cluster and provide extrapolated comparison; they also note curve/constraint-count caveats. | Treat this as source-local comparison, not a settled benchmark ranking. |
| VKD application | Shows invariant proofs for Merkle-tree/SHA-256 based Verifiable Key Directories, proving batched updates. | Application evidence, not a general VKD survey. |
| RAM computation | Adapts memory-checking to RAM/TinyRAM-style traces and compares permutation-based memory checking with Merkle-tree memory checking. | ALU module uses dummy constraints matching reported cost; not a full zkVM implementation. |

## Limitations And Boundaries

- Hekaton’s final proof size and verifier time are logarithmic in the number of subcircuits, while Pianist’s table row reports constant proof/verifier costs; Hekaton’s advantage is different: arbitrary computations, small communication and SRS dependence on unique subcircuits rather than total circuit size in favorable settings.
- Aggregation is not yet parallelized in the implementation. The coordinator’s aggregation time can become non-trivial.
- Circuit partitioning quality matters. The paper leaves optimal partitioning to future work and relies on practical circuits having a manageable number of shared wires.
- The worker model is coordinated by a central node. The paper’s robust-worker/adversarial scheduling story is not the same as Pianist’s robust collaborative proving section; Hekaton focuses on the proof-system construction and implementation.
- Performance claims are tied to a specific Rust/arkworks/OpenMPI/HPC setup and should be treated as source-local until repository/current benchmark evidence is absorbed.
- This paper is not a foundation definition for zk-SNARKs, Groth16, Mirage, TIPP, DIZK, deVirgo, Pianist, Mangrove or Verifiable Key Directories. It is a strong source extension for distributed proving plus proof aggregation.

## Knowledge Promotion

| Candidate | Handling | Reason |
| --- | --- | --- |
| Hekaton | Source instance only | Named system/paper; all system-local mechanisms and benchmarks stay in this source note. |
| Divide-and-aggregate zkSNARKs | Source extension / method route | Useful method pattern, but currently one primary source; keep as section under distributed proof generation and proof aggregation until more sources accumulate. |
| Distributed proof generation | Refresh existing knowledge node | Hekaton directly compares to DIZK/deVirgo/Pianist and adds a new route for arbitrary circuits via proof aggregation. |
| SNARK proof aggregation | Refresh existing knowledge node | Hekaton contributes heterogeneous commit-carrying Mirage aggregation, distinct from SnarkFold’s folding route. |
| Distributed proof generation -> SNARK proof aggregation | Create bridge | Hekaton provides direct evidence that proof aggregation can be the fan-in/compression layer for distributed proving. |
| Proof-system benchmarking | Refresh as source-local benchmark evidence | Hekaton’s evaluation is important but not a general benchmarking methodology like zk-Bench. |
| zk-SNARKs | Secondary source extension only | Hekaton is a zkSNARK construction but does not fill the missing foundation-pack gap for zk-SNARKs. |

## Links

- Primary knowledge: [[distributed-proof-generation|Distributed proof generation]]
- Secondary knowledge: [[snark-proof-aggregation|SNARK proof aggregation]], [[proof-system-benchmarking|Proof-system benchmarking]], [[zk-snarks|zk-SNARKs]]
- Bridge: [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]]

## Open Questions And Follow-Ups

| Gap | Why It Matters | Suggested Owner |
| --- | --- | --- |
| Hekaton repository not analyzed | Need current code architecture, whether code was released, reproducibility scripts, and implementation maturity. | `nahida-github-repo-analyze` if repo URL is known/found |
| DIZK and aPlonk primary sources pending | Hekaton’s Table 1 and related-work comparisons should be calibrated against primary notes. | Continue queue |
| SnarkPack/TIPP primary sources missing | Hekaton’s aggregation scheme depends on this lineage; source note currently records Hekaton’s use, not full foundation. | `nahida-update` / `nahida-research-search` |
| Distributed aggregation future work | Current aggregation bottleneck may matter for larger clusters. | Watchlist / future paper search |
| Optimal circuit partitioning | Hekaton assumes useful partitions; partitioner quality affects overhead and load balance. | Search/queue circuit partitioning sources such as Ou |

## Update Log

| Date | Run ID | Change |
| --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-hekaton-proof-aggregation | Deep-read source note created and absorbed into Source + Knowledge + Bridge architecture. |
