---
id: "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
title: "面向大规模计算的可扩展零知识证明生成方法"
english_title: "Scalable Zero-Knowledge Proof Generation for Large-Scale Computing"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "master_thesis"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "scalable-proof-generation"
  - "memory-efficient-snarks"
  - "distributed-proof-generation"
  - "proof-system-benchmarking"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "scalable-proof-generation"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/scalable-proof-generation"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
source_note_refs: []
knowledge_refs:
  - "nahida-knowledge-scalable-proof-generation"
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-distributed-proof-generation"
  - "nahida-knowledge-proof-system-benchmarking"
  - "nahida-knowledge-commit-and-prove-arguments"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-scalable-proof-generation"
  - "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
authors:
  - "叶哲名"
  - "Ye Zheming"
supervisor: "张召"
institution: "华东师范大学"
venue: "East China Normal University Master's Dissertation"
year: "2026"
publication_date: "2026-03"
doi: ""
arxiv_id: ""
canonical_url: ""
local_path: "~/Desktop/paper/51265903020 叶哲名 面向大规模计算的可扩展零知识证明生成方法.pdf"
sha256: "9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
pdf_pages: 138
extracted_text_path: "vault/02_Raw/pdf/extracted/51265903020-9c8b8a3f92ae-pdfplumber-pages.txt"
extractor: "codex-bundled-python:pdfplumber"
extraction_quality: "good_for_cjk_text"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Chinese/English title page and abstracts identify scalable ZK proof generation as the main problem."
  - "Chapters 3-5 provide automatic circuit partitioning, serializable ZK-SNARK generation, and Yoimiya pipeline framework."
  - "Experiments focus on prover memory, setup/prove time, CPU utilization, and partition/pipeline tradeoffs."
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0096"
queue_rank: 96
absorbed_run_id: "nahida-knowledge-20260623-scalable-zkp-generation"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "scalable-proof-generation"
  - "memory-efficient-snarks"
  - "distributed-proof-generation"
source_refs:
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
confidence: "high"
trust_tier: "primary"
---

# 面向大规模计算的可扩展零知识证明生成方法

## Source Identity

| Field | Value |
| --- | --- |
| Chinese title | 面向大规模计算的可扩展零知识证明生成方法 |
| English title | Scalable Zero-Knowledge Proof Generation for Large-Scale Computing |
| Author | 叶哲名 / Ye Zheming |
| Supervisor | 张召 |
| Institution | 华东师范大学 / East China Normal University |
| Degree | Master’s dissertation |
| Date | 2026-03 |
| Source file | `~/Desktop/paper/51265903020 叶哲名 面向大规模计算的可扩展零知识证明生成方法.pdf` |
| SHA-256 | `9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270` |
| Extraction note | `pypdf` produced CJK mojibake in the queue record; this source note uses `pdfplumber` extraction from `vault/02_Raw/pdf/extracted/51265903020-9c8b8a3f92ae-pdfplumber-pages.txt`. |

## Absorption Routing

| Layer | Decision | Reason |
| --- | --- | --- |
| Primary Knowledge | [[scalable-proof-generation|Scalable proof generation]] | The thesis is about reducing prover memory, improving resource utilization, and preserving sound proof generation for large computations. |
| Secondary Knowledge | [[memory-efficient-snarks|Memory-efficient SNARKs]] | Circuit partitioning and serial subproofs reduce peak memory for Groth16/Plonk-style proving. |
| Secondary Knowledge | [[distributed-proof-generation|Distributed proof generation]] | Yoimiya uses pipeline/subtask scheduling and cites distributed proving work, but it is mainly single-machine/multi-task pipeline parallelism rather than cluster proving. |
| Secondary Knowledge | [[proof-system-benchmarking|Proof-system benchmarking]] | The dissertation reports memory, setup, proof time, CPU utilization, partition count, and pipeline configurations. |
| Bridge | [[commit-and-prove-arguments-to-scalable-proof-generation|Commit-and-prove arguments -> scalable proof generation]] | Polynomial binding plays the consistency-binding role needed when one statement is split into multiple subproofs. |

The initial queue classification `proof-system-foundations` was too broad. This is not a new foundation for all ZK proofs; it is a prover-scalability dissertation centered on automatic circuit partitioning, serializable zk-SNARK generation, and pipeline scheduling.

## One-Paragraph Summary

This dissertation studies how to make zk-SNARK proof generation feasible for large-scale computations when monolithic proving is blocked by peak memory and poor CPU utilization. It proposes: a constraint dependency graph (CDG) method to automatically partition a large constraint system into serializable, load-balanced subcircuits; a polynomial-binding based serializable zk-SNARK construction that checks shared private variables across subcircuits without revealing them or adding heavy hash constraints; and Yoimiya, a proof-generation framework that combines partitioning with subcircuit-level pipelining so multiple proof tasks can overlap witness generation and proof computation. The durable idea for the knowledge base is not "Yoimiya" as a standalone concept, but the more general problem of scalable proof generation: circuit-level decomposition, consistency binding, backend adaptation, resource loading, scheduling, and benchmark discipline all have to be handled together.

## Problem Addressed

The dissertation starts from an application pressure point: outsourced/cloud computation, AI inference, blockchain privacy, verifiable database queries, and large ZK workloads need proofs that are small and fast to verify, but zk-SNARK provers often require memory and computation far beyond the native computation.

The core bottlenecks are:

- Peak memory: monolithic proving must hold the full witness/constraint/proving-key state; the thesis gives matrix multiplication examples where a modest native computation can require tens of GB of proving memory.
- Resource utilization: witness generation is often circuit-structure dependent and serial, while proof computation may be more parallelizable; on many-core CPUs the average utilization can remain low.
- Manual partitioning: splitting circuits by hand is error-prone, subjective, and hard to adapt to different memory budgets or hardware.
- Shared-variable consistency: after partitioning, a malicious prover could use inconsistent intermediate/private values in different subcircuits unless the proof system binds those values.
- Verification overhead: serial subproofs preserve low prover memory but increase proof count and verification work, which matters for on-chain use.

## Contributions

| Contribution | Thesis-local mechanism | Durable abstraction |
| --- | --- | --- |
| Automatic serializable circuit partitioning | Build a constraint dependency graph, topologically order constraints, and split into balanced subcircuits while tracking shared variables. | Circuit partitioning for prover memory reduction. |
| Serializable zk-SNARK proof generation | Add polynomial-binding constraints so shared private values across subcircuits are bound without being public. Adapt the method to Groth16 and Plonk. | Consistency binding for partitioned proofs. |
| Yoimiya framework | Compile, partition, setup, load resources, prove, verify, and schedule multiple proof tasks using witness/proof thread pools and subcircuit pipeline DAGs. | Resource-aware scalable proof-generation pipeline. |

## Technical Reading Notes

### Chapter 1: Motivation and Challenges

The introduction frames zero-knowledge proofs as a way to verify outsourced or hidden computations without revealing private inputs, model parameters, or intermediate state. zk-SNARKs are emphasized because they are non-interactive and succinct: proof size can be tiny and verifier work can be close to constant compared with the computation.

The thesis then identifies three research challenges:

1. Automatic partitioning of large circuits into serializable and balanced subcircuits.
2. Secure and efficient serial proof generation over partitioned subcircuits.
3. Improving resource utilization during proof generation under memory constraints.

The important knowledge-base point is that prover scalability is not one knob. A partition that saves memory may create consistency constraints; a consistency method may add constraints; a pipeline that uses CPU better may increase concurrent memory pressure.

### Chapter 2: Background and Related Work

The background covers zero-knowledge proof properties, non-interactive proofs via Fiat-Shamir, CRS/setup, and the standard zk-SNARK interface: `Setup`, `P`, and `V`. It compares Groth16, Plonk, Bulletproofs, HyperPlonk, Marlin, Spartan, and STARK-like systems along prover/verifier/proof/CRS/constraint-system axes.

The related-work structure is useful for routing:

- Memory optimization routes include domain-specific methods, space-efficient SNARKs such as Gemini/Epistle/Sparrow/Hobbit, folding-based approaches such as Nova, VOLE-based interactive protocols, and SPLIT-style hash-bound partitioning.
- Compute optimization includes witness generation, FFT, MSM, PCS operations, GPUs/accelerators, and distributed systems such as DIZK, Pianist, zkBridge/deVirgo, and Ou.
- The dissertation distinguishes witness generation from proof computation. Optimizing FFT/MSM alone does not solve circuit-dependent witness-generation bottlenecks.

### Chapter 3: CDG-Based Automatic Serializable Partitioning

The thesis defines a serializable circuit partition over a constraint system. Each subcircuit covers part of the original constraints, and dependencies are allowed only from earlier partitions to later partitions.

Core definitions:

- A constraint dependency exists from `c1` to `c2` when an output variable of `c1` is an input variable of `c2`.
- The constraint dependency graph `G=(V,E)` is a DAG whose vertices are constraints and whose edges are dependency relations.
- A partition is serializable when it respects a topological order of the CDG.
- The load of a subcircuit includes its own constraints plus inbound shared variables from earlier partitions; the optimization objective is to reduce the maximum subcircuit load.

Algorithmic route:

- Construct the CDG from constraint input/output relations.
- Use a Kahn-style topological ordering process rather than arbitrary DFS order.
- Use dependency complexity and dependency association heuristics to select constraints, avoiding partitions that create too much shared state.
- Split the ordered constraints into consecutive blocks, then construct subcircuits and shared-variable sets.

Experiments use Gnark, R1CS/Plonkish circuits, matrix multiplication workloads, and Merkle tree workloads. The most durable result is not a single number but the shape of the tradeoff: increasing partition count sharply reduces max load and peak memory potential, while shared variables remain small relative to total constraints in the tested workloads.

### Chapter 4: Polynomial-Binding Serializable zk-SNARKs

Partitioning alone is unsafe. If subcircuits share private intermediate variables, a prover could prove each subcircuit with locally valid but globally inconsistent values. Publishing shared variables would break zero-knowledge and bloat public inputs. Hashing shared variables inside circuits is secure but expensive, even with ZK-friendly hashes when many shared variables exist.

The dissertation introduces a serializable zk-SNARK abstraction with `Partition`, `Setup`, `P`, and `V` over extended subcircuits and consistency commitments. The main construction uses polynomial binding:

- Interpret shared variable sequences as coefficients of a polynomial-like binding.
- Evaluate at a challenge point so unequal shared-variable sequences collide with low probability.
- Bind public input/output first to derive a transcript seed.
- Commit private inputs before deriving the random point, preventing the prover from choosing inconsistent values after seeing the challenge.
- Add binding constraints to subcircuits and require matching consistency values across subproofs.

This is not identical to a full commit-and-prove SNARK framework, but it solves the same reusable interface problem: partitioned proof components need a hidden-value consistency handle. That is why this source updates [[commit-and-prove-arguments-to-scalable-proof-generation|Commit-and-prove arguments -> scalable proof generation]].

Backend adaptation:

- Groth16: each subcircuit has independent setup/proving/verifying keys; resource loading becomes a memory issue because proving keys can dominate memory.
- Plonk: universal SRS can be sized to the largest subcircuit, so partitioning can reduce SRS/setup pressure; verifying keys are small.
- Both backends need careful loading/unloading of constraint systems and proving material to preserve the memory win.

Security is stated as inheriting completeness, soundness, and zero-knowledge from the underlying subcircuit SNARK, plus polynomial-binding consistency for shared variables. The thesis calls the privacy property "weak zero-knowledge" because consistency evaluation values are public, though large fields leave many possible preimages for non-singleton shared sequences.

### Chapter 5: Yoimiya Pipeline Framework

Yoimiya combines the chapter 3 and 4 mechanisms into a framework for multi-task proof generation. Its front end compiles circuits, partitions them, extends them with binding constraints, sets up resources, loads artifacts, and schedules proof tasks.

The scheduling insight:

- Within one task, witness generation must precede proof computation for a subcircuit.
- Across tasks, witness generation for one task can overlap proof computation for another.
- Partitioning controls memory and exposes smaller scheduling units.
- Two thread pools, one for witness generation and one for proof computation, allow configurable resource allocation.
- An execution DAG tracks ready subcircuits and dependencies; it differs from the logical subcircuit dependency graph because already-known private inputs do not always impose runtime order.

The reported experiments use 20 Groth16 proof tasks over a large linear-recurrence circuit. A representative result is that increasing witness-generation threads under partitioning shortened total time substantially and raised CPU utilization, while partition count controlled memory. This supports the reusable principle that scalable proof generation is a scheduling and resource-management problem, not only a cryptographic-protocol problem.

### Chapter 6: Limitations and Future Work

The dissertation is explicit about limitations:

- The CDG partition heuristic is not globally optimal.
- Serial joint proofs increase verifier work because the verifier checks multiple subproofs and consistency hashes/bindings.
- Recursion or folding could compress verification overhead in future work.
- Current adaptation focuses on R1CS/Plonkish and Groth16/Plonk; AIR/STARK-style protocols are future work.
- Yoimiya currently improves Groth16 pipeline behavior more than Plonk due to implementation/backend characteristics.
- Configuration selection should eventually be adaptive to hardware and workload.

## Evaluation Evidence

| Area | Evidence captured | Knowledge use |
| --- | --- | --- |
| Partitioning cost | Partition/build time grows roughly linearly with circuit size; partition count mainly changes thresholds. | Supports automatic partitioning as an engineering stage with measurable overhead. |
| Load reduction | Increasing partition count reduces maximum subcircuit load; shared variables are small in the tested MM/Merkle workloads. | Supports memory-efficient SNARK route, with workload boundary. |
| Polynomial binding overhead | For matrix multiplication, polynomial binding has far lower overhead than hash-bound consistency; for Merkle tree, overhead can be higher when private inputs are bound broadly. | Supports bridge to consistency binding and warns against one-size-fits-all binding. |
| Setup behavior | Groth16 setup remains per subcircuit; Plonk SRS can shrink with smaller max subcircuit. | Backend-specific scalable proving tradeoff. |
| Proof memory/time | Partitioning reduces peak memory significantly while proof time and loading overhead vary by backend and partition count. | Source-local benchmark evidence, not universal ranking. |
| Pipeline scheduling | Multi-task pipelining raises CPU utilization and reduces batch proof time while memory is controlled by partitioning. | Supports scalable-proof-generation node and benchmark node. |

## Relationship to Existing Vault Sources

| Existing source/node | Relation |
| --- | --- |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] | Closest prior memory-partitioning route; this thesis replaces hash-bound shared-state checks with polynomial binding and automatic CDG partitioning. |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] / [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] | Same high-level prover-memory problem, but their route is elastic/streaming SNARK internals rather than front-end circuit partitioning. |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]] / [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou]] | Adjacent distributed/compiler routes. Yoimiya is not a cluster-distributed prover like DIZK and not a ZK-language compiler like Ou, but it shares the partition/scheduling/consistency problem. |
| [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] / [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP]] | Same prover-throughput problem, different layer: hardware acceleration versus software pipeline/circuit partitioning. |
| [[proof-system-benchmarking|Proof-system benchmarking]] | This thesis adds benchmark axes: partition count, max load, setup/SRS behavior, prove memory, total memory, loading time, CPU utilization, and task-pipeline throughput. |

## Knowledge Handoff

| Target | Action |
| --- | --- |
| [[scalable-proof-generation|Scalable proof generation]] | Create a reusable problem node above memory-efficient, distributed, hardware, and benchmark routes. |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | Treat this thesis as a front-end automatic circuit-partitioning and polynomial-binding source extension. |
| [[distributed-proof-generation|Distributed proof generation]] | Add as adjacent pipeline/partition contrast, not as cluster-distributed proving. |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | Add a bridge only at the consistency-binding interface; do not claim the thesis implements a general CP-SNARK. |
| [[proof-system-benchmarking|Proof-system benchmarking]] | Add source-local metrics and caution that exact values depend on Gnark, BN254, CPU hardware, workload, and partition config. |

## Cold-Start Queries

- "zk-SNARK prover 内存不够时有哪些路线?"
- "Yoimiya 和 Split/DIZK/Ou 有什么区别?"
- "为什么电路切分后的 subproof 需要 shared-variable consistency?"
- "多项式绑定和 hash-bound consistency 在 SNARK 电路里有什么取舍?"
- "证明生成流水线如何提高 CPU 利用率?"

## Absorption Checklist

- [x] Full PDF deep-read performed from local file.
- [x] Source note created as a standalone paper note.
- [x] Queue classification corrected from broad proof-system foundations to scalable proof generation.
- [x] New reusable knowledge node created.
- [x] Bridge created for consistency-binding transfer.
- [x] Paper-specific algorithm, evaluation, and limitations kept inside source note.
