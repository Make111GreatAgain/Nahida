---
id: "sha256-4b56be6d2631"
title: "zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs"
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
  - "p1-p3 title, abstract, contributions, benchmark result summary"
  - "p3-p6 background: public-key cryptography, ZKPs, preprocessing SNARKs, frontend/backend split"
  - "p6-p9 architecture: goals, metrics, arithmetic backend, circuit backend, log parser, frontends"
  - "p9-p10 selected arithmetic libraries, curves, ZKP tools and hardware setups"
  - "p10-p17 benchmark results: arithmetic, circuits, proof size, hardware sensitivity"
  - "p18-p19 runtime estimation and Plonk prover estimation table"
  - "p19-p21 limitations, recommendations, related work and conclusion"
  - "p24-p26 appendices: library popularity table and coefficient-of-variation validation"
canonical_url: ""
pdf_url: ""
doi: ""
arxiv_id: ""
eprint_candidate: "2023/1503 inferred from local filename; not externally verified in this run"
venue: "unknown"
year: "2023"
authors:
  - "Jens Ernstberger"
  - "Stefanos Chaliasos"
  - "George Kadianakis"
  - "Sebastian Steinhorst"
  - "Philipp Jovanovic"
  - "Arthur Gervais"
  - "Benjamin Livshits"
  - "Michele Orrù"
affiliations:
  - "Technical University of Munich"
  - "Imperial College London"
  - "Ethereum Foundation"
  - "University College London"
  - "Centre National de la Recherche Scientifique"
local_pdf: "~/Desktop/paper/2023-1503.pdf"
sha256: "4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
pages: 26
pdf_extractor: "codex-bundled-python:pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2023-1503-4b56be6d2631-pages.txt"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "proof-system-benchmarking"
  - "zk-snarks"
  - "proof-system-tooling"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "proof-system-benchmarking"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/proof-system-benchmarking/sha256-4b56be6d2631"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-4b56be6d2631"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
  directions:
    - "proof-systems"
  topics:
    - "proof-system-benchmarking"
    - "zk-snarks"
    - "proof-system-tooling"
    - "runtime-estimation"
    - "arithmetic-library-benchmarks"
domains:
  - "zero-knowledge-proofs"
topics:
  - "zk-Bench"
  - "SNARK benchmarking"
  - "ZKP development tools"
  - "proof-system benchmarking"
  - "runtime estimation"
  - "arithmetic libraries"
  - "elliptic curves"
  - "BN254"
  - "BLS12-381"
  - "Groth16"
  - "Plonk"
  - "Halo2"
  - "STARKs"
aliases:
  - "zk-Bench"
  - "ZK Bench"
  - "SNARK benchmarking"
  - "proof-system benchmarking"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "zkSNARK"
  - "benchmarking"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "proof systems"
    - "ZKP tooling"
    - "benchmarking and evaluation"
  problem:
    - "compare ZKP tools and arithmetic libraries under reproducible and comparable conditions"
    - "estimate cryptographic protocol runtime before full implementation"
    - "standardize metrics across setup, proving, verification, memory and proof size"
  method_family:
    - "proof-system benchmarking framework"
    - "arithmetic microbenchmarking"
    - "circuit-level benchmark harness"
    - "runtime interpolation and extrapolation"
  evaluation:
    - "13 elliptic curves across 9 arithmetic libraries"
    - "5 ZKP development tools"
    - "Exponentiate and SHA-256 test vectors"
    - "commodity AWS hardware comparison"
  bridge:
    - "benchmarking as an evaluation axis for zk-SNARK method selection"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zk-bench-proof-system-benchmarking"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0043"
safe_for_absorption: true
source_refs:
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "pdf:~/Desktop/paper/2023-1503.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "proof-systems"
secondary_directions: []
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Abstract and Section 1 define zk-Bench as a benchmarking framework and estimator for practical ZKP/SNARK evaluation"
  - "Sections 3-6 cover architecture, benchmark methodology, arithmetic/circuit experiments, hardware sensitivity and runtime estimation"
  - "Section 7 frames limitations and community recommendations around benchmark standardization"
taxonomy_version: "1.0"
---

# zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs

## 论文身份

- Title in PDF: zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs
- Queue title: zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs
- Authors: Jens Ernstberger, Stefanos Chaliasos, George Kadianakis, Sebastian Steinhorst, Philipp Jovanovic, Arthur Gervais, Benjamin Livshits, Michele Orrù
- Visible affiliations: Technical University of Munich; Imperial College London; Ethereum Foundation; University College London; CNRS
- Local PDF: `~/Desktop/paper/2023-1503.pdf`
- Stable local identity: `sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526`
- External identity: unknown in the PDF metadata. The local filename suggests IACR ePrint `2023/1503`, but this run did not fetch external metadata.
- Extractor: `codex-bundled-python:pypdf`; extraction is usable across all 26 pages, with figure/table formatting noise but readable section text.

## 精读状态

- Reading status: `deep_read_complete`
- Coverage: abstract, introduction, SNARK/frontend/backend background, zk-Bench architecture, benchmark target selection, arithmetic results, circuit results, runtime estimation, limitations/recommendations, related work, conclusion and appendices were read.
- Skipped sections: no major section was intentionally skipped.
- Extraction gaps: plots and heatmaps are text-noisy; key values and author explanations are readable in surrounding prose. Appendix Table 6 is truncated/noisy in extraction, so exact coefficient-of-variation rows are not normalized here.
- Safe for absorption: yes. The paper supports a reusable knowledge node about proof-system benchmarking and selection, while exact benchmark values remain source-local evidence.

## 章节地图

| 覆盖范围 | 主要内容 | 作用 |
| --- | --- | --- |
| p1-p3 | Abstract, Introduction, contributions and result summary | 定位 zk-Bench as open-source benchmarking framework + estimator for ZKP/SNARK tooling. |
| p3-p6 | Background | 解释 public-key operations, elliptic curves, preprocessing SNARK algorithms, frontend/backend, circuit and constraint systems. |
| p6-p9 | Architecture | 给出 completeness/modularity/reproducibility/pragmatism goals, metrics, arithmetic/circuit backends, log parser, Zkalc and zk-Harness frontends. |
| p9-p10 | Selected libraries/tools | 说明 13 curves / 9 arithmetic libraries / 5 ZKP tools, and why libsnark was excluded. |
| p10-p17 | Benchmark results | 汇总 AWS hardware, field arithmetic, MSM/pairing, Exponentiate and SHA-256 circuits, setup/prove/verify/proof-size/memory tradeoffs. |
| p18-p19 | Runtime estimation | 用 interpolation/extrapolation and operation enumeration 估算 arithmetic/protocol runtime; Plonk prover estimates fall within reported 6-32% error in examples. |
| p19-p21 | Discussion, related work, conclusion | 记录硬件/测试向量/optimization limits，提出 standardized test vectors、interoperable IR 和 documentation 建议。 |
| p24-p26 | Appendices | library popularity table, framework frontend/backend grouping, coefficient-of-variation validation. |

## Hierarchy Candidate Classification

| Layer | Candidate | Confidence | Evidence |
| --- | --- | --- | --- |
| L1 Domain | `zero-knowledge-proofs` | high | 全文围绕 ZKP/SNARK tooling, proof systems and public-key cryptography benchmarks. |
| L2 Direction | `proof-systems` | high | 评测对象是 proof-system implementation stack: arithmetic backend, setup, prover, verifier, proof size and memory. |
| L3 Topic | `proof-system-benchmarking` | high | 论文核心贡献是 benchmarking framework and runtime estimator, not a new proof system. |
| Secondary | `zero-knowledge-proofs/proof-systems/zk-snarks` | high | 标题和实验主体覆盖 preprocessing SNARKs, Groth16, Plonk/Halo2, ZKP development tools. |
| Not primary | `proof-system-foundations` | medium | 背景章节解释 SNARKs，但 durable contribution is evaluation methodology/tooling, so the queue's old foundation path is too broad. |

Alternative placements considered: `zk-SNARKs` alone is too broad because zk-Bench is an evaluation and tooling source; `proof-system-tooling` is relevant but narrower than the reusable evaluation-axis node.

## One-Sentence Contribution

zk-Bench provides a modular benchmarking framework and estimator that compares arithmetic libraries and ZKP development tools across execution time, memory and proof size, then uses low-level benchmark data to estimate higher-level cryptographic protocol cost.

## Problem Setting

ZKP/SNARK developers face a tool-selection problem: many libraries expose different curves, finite-field implementations, arithmetizations, DSLs, proof backends and hardware behaviors. Individual papers or project READMEs often report performance in isolation, omit implementation details, or benchmark only one layer. As a result, choosing a proving stack can be expensive, irreproducible and easy to misjudge.

The paper's answer is not a new SNARK protocol. It introduces an evaluation surface that spans:

- low-level arithmetic operations over finite fields and elliptic curves;
- amortized operations such as MSM, multi-pairing and NTT;
- circuit-level setup/prove/verify execution time;
- memory consumption for proof-system phases;
- serialized proof size;
- hardware sensitivity across commodity AWS instances;
- estimator tooling for rough protocol runtime before implementation.

## Method Overview

### 1. Architecture Goals

The design goals are completeness, modularity, reproducibility and pragmatism. Completeness means covering both low-level arithmetic and high-level proof-system phases. Modularity means each arithmetic operation and circuit benchmark is separated so new libraries/circuits can be added with limited glue code. Reproducibility is handled through automated benchmarks and standardized cloud configurations. Pragmatism means benchmarks use optimization flags and all cores where practical, rather than artificial single-thread-only settings.

### 2. Metrics

The source normalizes three major evaluation metrics:

- execution time: measured through language-native benchmarking/profiling tools such as criterion.rs, Go benchmarking/profiling and tinybench;
- memory consumption: maximum resident set size for ZKP tool phases, including serialization/deserialization to mirror real usage;
- proof size: byte size of serialized proofs, with the caveat that proof objects generally cannot be substantially compressed.

This metric trio is the core durable idea for [[proof-system-benchmarking|Proof-system benchmarking]].

### 3. Arithmetic Backend

The arithmetic backend benchmarks field addition, multiplication, inversion; elliptic-curve addition and scalar multiplication; pairing operations; and amortized operations including inner products, MSM, multi-pairing and NTT. For amortized operations, sizes are sampled geometrically and measured using the upstream benchmarking libraries where possible.

The important reusable point is that proof-system performance depends heavily on arithmetic-library implementation, curve choice, operation size and hardware. Exact row values belong in this source note, while the knowledge layer should remember the evaluation axis.

### 4. Circuit Backend

The circuit backend creates setup/prover/verifier runners for each ZKP development tool. The configuration specifies the library or DSL, algebraic structure, backend and circuit inputs. The paper uses two initial test vectors:

- `Exponentiate`: manually implemented across tools so the functionality is comparable.
- `SHA-256`: uses maintained tool/library implementations and therefore better reflects real-world circuits, but is more affected by implementation-specific optimizations.

### 5. Log Parser and Frontends

Two parsers normalize benchmark outputs into CSV/JSON for frontends. `Zkalc` exposes cost estimates and graphs for public-key operations; `zk-Harness` visualizes execution time, memory and proof size for ZKP tools and configurations.

### 6. Runtime Estimation

The estimator interpolates between benchmark sizes and extrapolates outside measured ranges. For non-amortized operations it scales linearly; for amortized/nonlinear operations it uses regression or known asymptotic forms such as MSM near `n / log n` and FFT/NTT near `n log n`. The Plonk prover estimator enumerates key operation classes such as MSM and FFT and sums estimated costs. In the examples reported in Table 3, the estimate error is within the paper's 6-32% range for gnark Plonk prover runtimes up to one million gates.

## Benchmark Findings

### Arithmetic Layer

- BN254 is not uniformly faster than BLS12-381 despite smaller field size; implementation and hardware effects matter.
- For BN254 scalar-field addition/multiplication, the paper reports gnark-crypto as about 30% faster on average than the other compared implementations, while for BLS12-381 it is slower than some alternatives.
- ffjavascript is nearly two orders of magnitude slower in some field operations because exposed APIs include additional serialization overhead.
- For MSM of size `2^20`, the paper reports gnark-crypto at 0.22s in G1 and 0.53s in G2 over BN254, substantially ahead of the next implementation in those tests.
- For BLS12-381 large MSM, gnark-crypto outperforms blstrs in the paper's reported large-size setting, despite blstrs' assembly optimizations.
- ARM hardware underperforms x86 for some finite-field/MSM workloads in the tested configuration, making hardware selection part of the proof-system evaluation surface.

### Circuit Layer

- Setup for Plonk can be faster than Groth16 in some SHA-256 gnark settings, but Plonk uses more memory; gnark Plonk exceeded the 128 GB machine memory for larger SHA-256 preimages in the reported experiment.
- Groth16 remains faster than Plonk for proving in several reported gnark benchmarks. For SHA-256 at 8 kB, gnark Plonk is reported as 9.39x slower than gnark Groth16.
- Rust-based tools are substantially more memory efficient in some settings; bellman is slower than the fastest provers but uses much less memory on the 32 kB SHA-256 preimage example.
- gnark and rapidsnark are strong prover-performance points in the reported SHA-256 experiments, but gnark's speed comes with higher memory consumption.
- Groth16 and Plonk verification times remain small and approximately constant, while starky verification scales with input size in the tested circuit.
- STARK-style proof size from starky is much larger in the tested Exponentiate setting than Groth16/Plonk/Halo2 proof sizes, as expected from the proof-family design.

### Hardware Sensitivity

The paper compares CPU-optimized and memory-optimized machines at similar hourly price. Some tools benefit from compute-optimized machines; others benefit from memory-optimized machines. The durable takeaway is not the exact cost number, but that proof-system benchmarking must include hardware configuration as an explicit variable.

## Evidence Anchors

| Claim / detail | Evidence anchor | Evidence kind | Confidence | Notes |
| --- | --- | --- | --- | --- |
| zk-Bench is a benchmarking framework and estimator for public-key cryptography and practical ZKP systems | p1-p3 | author contribution | high | source-level contribution |
| Architecture has arithmetic backend, circuit backend, log parser and two frontends | Fig. 1, p2, p6-p9 | system architecture | high | `Zkalc` and `zk-Harness` are frontends |
| Metrics include execution time, memory consumption and proof size | p7 | methodology | high | reusable evaluation axis |
| Evaluation covers 13 curves, 9 arithmetic libraries and 5 ZKP development tools | p1, p9-p10 | experimental scope | high | exact versions in Table 1 |
| Exponentiate and SHA-256 are the initial circuit test vectors | p13-p14 | benchmark design | high | SHA-256 is implementation-dependent |
| Plonk prover runtime estimator errors are within the reported 6-32% examples | p18-p19, Table 3 | estimation evidence | medium | gnark Plonk only; not universal |
| Hardware can change prover performance materially | p16-p17, Fig. 10 | empirical result | high | commodity AWS instances only |
| Limitations include no GPU/FPGA/mobile, limited circuit set and implementation-specific optimizations | p19-p20 | limitation | high | important boundary |

## Limitations and Caveats

- Hardware scope is commodity cloud CPU machines only. The paper explicitly excludes GPUs, FPGAs and mobile devices.
- The circuit set is small: Exponentiate and SHA-256. SHA-256 implementations differ across tools, so results mix proof-system backend cost with circuit-optimization differences.
- Arithmetic microbenchmarks use exposed library APIs as-is, without isolating every representation/algorithm optimization such as coordinate form or constant-time constraint.
- Proof-system comparisons depend on exact versions, circuit implementations and hardware. Do not transfer numeric rankings blindly to newer libraries or production circuits.
- The paper reports an open-source evaluation platform and repository history, but this run did not analyze the repository itself; repository architecture and current maintenance remain a follow-up task.
- Runtime estimation is useful for approximate planning, not a replacement for implementing and benchmarking the target circuit/protocol.

## Reusable Ideas vs Source-Specific Details

| Candidate | Handling | Reason |
| --- | --- | --- |
| Proof-system benchmarking | Promote to knowledge node | Stable evaluation axis for many ZKP sources, repos and future queries. |
| zk-Bench | Keep as source instance | Named tool/paper; implementation details and exact values remain source-local. |
| Zkalc / zk-Harness | Source-local tooling; possible repo follow-up | They are components of the source artifact, not yet independently analyzed repositories. |
| Exact chart values | Source note only | Useful evidence but not durable knowledge claims across versions/hardware. |
| Standardized test vectors | Knowledge-node route/gap | Community-level problem beyond this single paper. |
| Interoperable intermediate representations | Knowledge-node gap/candidate | Important for future benchmarking, but not created as a node from this source alone. |

## Knowledge Impact

- Primary path: `zero-knowledge-proofs/proof-systems/proof-system-benchmarking`.
- New knowledge node: [[proof-system-benchmarking|Proof-system benchmarking]].
- Parent update: [[proof-systems|Proof systems]] gains a child/evaluation-axis row and a source extension.
- `zk-SNARKs` update: [[zk-snarks|zk-SNARKs]] gains a benchmarking/evaluation route without upgrading its foundation status.
- Bridge decision: no new durable bridge was created. This source mainly adds an intra-direction evaluation axis; bridge candidates should wait until there is enough evidence tying benchmarking to a cross-domain application such as rollup prover economics, zkML deployment, or hardware-accelerated proving.

## Path Materialization

```text
zero-knowledge-proofs / proof-systems / proof-system-benchmarking / sha256-4b56be6d2631
```

Secondary path:

```text
zero-knowledge-proofs / proof-systems / zk-snarks / sha256-4b56be6d2631
```

## Path Propagation

| Target | Action | Status |
| --- | --- | --- |
| [[proof-system-benchmarking|Proof-system benchmarking]] | create evaluation-axis knowledge node | done |
| [[proof-systems|Proof systems]] | add child, source extension and relation edge | done |
| [[zk-snarks|zk-SNARKs]] | add evaluation-only source extension | done |
| `05_Bridges` | no durable bridge | no-op |
| Generated indexes and queue | rebuild/checkpoint after absorption | pending in this run |

## Review Items

| Type | Item | Status |
| --- | --- | --- |
| metadata_gap | Venue/canonical URL unavailable in local PDF metadata; filename suggests ePrint `2023/1503`, but no external metadata was fetched. | review |
| repository_followup | zk-Bench/zk-Harness/Zkalc source repository was not analyzed; use `nahida-github-repo-analyze` if implementation architecture or current maintenance matters. | queued |
| benchmark_freshness | Tool versions and GitHub activity were as of 2023; numeric rankings should be refreshed before current engineering decisions. | queued |
| foundation_gap | Plonk/Groth16/STARK/benchmarking standard sources are still needed to complete proof-system benchmarking foundations. | queued |

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-zk-bench-proof-system-benchmarking | Deep-read source note created and absorbed into proof-system benchmarking. | codex |
