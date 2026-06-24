---
id: nahida-knowledge-graph-partitioning
title: "Graph partitioning"
type: knowledge
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: active
node_kind: problem
hierarchy_level: topic
status: active
file_slug: graph-partitioning
domain_id: algorithm-engineering
direction_id: graph-algorithms
topic_id: graph-partitioning
parent: "[[graph-algorithms]]"
parent_knowledge_refs:
  - nahida-knowledge-graph-algorithms
child_knowledge_refs: []
ontology_path:
  - algorithm-engineering
  - graph-algorithms
  - graph-partitioning
primary_ontology_path: algorithm-engineering/graph-algorithms/graph-partitioning
secondary_ontology_paths:
  - algorithm-engineering/graph-algorithms/sparse-matrix-ordering
source_refs:
  - "sha256:5d282518468247e122f341e5318171d3cd40a0f4c3b8ac424bcaff8754c5bfc7"
  - "doi:10.1145/2339530.2339722"
  - "sha256:204bff1f6801b8e5764e2fac54252b59cea1dbf3ac666072cf2eb1e750fce647"
representative_sources:
  - "[[sha256-5d2825184682-fast-high-quality-multilevel-graph-partitioning|A Fast and High Quality Multilevel Scheme for Partitioning Irregular Graphs]]"
  - "[[doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs|Streaming Graph Partitioning for Large Distributed Graphs]]"
relation_edges:
  - from: nahida-knowledge-graph-partitioning
    relation: part_of
    to: nahida-knowledge-graph-algorithms
    evidence_refs:
      - "vault/04_Knowledge/algorithm-engineering/graph-algorithms.md"
      - "vault/04_Knowledge/algorithm-engineering/graph-algorithms/graph-partitioning.md"
    confidence: high
    status: active_seed
  - from: nahida-knowledge-graph-partitioning
    relation: evidenced_by
    to: "vault/03_Sources/papers/sha256-5d2825184682-fast-high-quality-multilevel-graph-partitioning.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5d2825184682-fast-high-quality-multilevel-graph-partitioning.md"
    confidence: high
    status: active_seed
  - from: nahida-knowledge-graph-partitioning
    relation: evidenced_by
    to: "vault/03_Sources/papers/doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs.md"
    confidence: high
    status: active_seed
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/sha256-5d2825184682-fast-high-quality-multilevel-graph-partitioning.md"
  - "vault/03_Sources/papers/doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs.md"
representative_source_refs:
  - "sha256:5d282518468247e122f341e5318171d3cd40a0f4c3b8ac424bcaff8754c5bfc7"
  - "doi:10.1145/2339530.2339722"
query_keys:
  - graph partitioning
  - balanced graph partitioning
  - multilevel graph partitioning
  - streaming graph partitioning
  - Linear Deterministic Greedy
  - LDG graph partitioning
  - graph data layout
  - heavy edge matching
  - boundary Kernighan-Lin refinement
  - METIS
aliases:
  - Balanced graph partitioning
  - Multilevel graph partitioning
  - Streaming graph partitioning
  - Linear Deterministic Greedy
  - LDG
domains:
  - algorithm-engineering
topics:
  - graph partitioning
  - multilevel graph partitioning
  - streaming graph partitioning
  - graph data layout
  - graph separators
  - sparse matrix ordering
freshness_status: fresh
last_synthesized: 2026-06-23
valid_until: 2026-07-23
created: 2026-06-23
updated: 2026-06-23
tags:
  - nahida/knowledge/problem
  - nahida/domain/algorithm-engineering
  - nahida/graph-algorithms/graph-partitioning
---

# Graph partitioning

## Definition

Graph partitioning asks how to divide a graph into balanced parts while minimizing the coupling between parts.

In the source-backed formulation from [[sha256-5d2825184682-fast-high-quality-multilevel-graph-partitioning|Karypis and Kumar]], the k-way partitioning problem divides vertices into k subsets of roughly equal size or weight while minimizing the edge cut between subsets. Weighted variants use vertex weights for work and edge weights for communication or coupling cost.

## Why the Problem Matters

Graph partitioning appears when a computation or data structure has to be split without creating too much cross-part communication.

Source-backed examples include:

- scientific computing,
- VLSI layout,
- task scheduling,
- sparse matrix-vector multiplication,
- sparse matrix factorization ordering.

The recurring problem shape is:

1. computation must be divided,
2. each part should receive similar work,
3. cross-part edges create communication, synchronization, fill, or coupling,
4. the partitioner tries to balance local work and minimize cross-boundary cost.

## Method Families

### Spectral Partitioning

Spectral partitioning uses eigenvectors of a graph Laplacian, especially the Fiedler vector, to divide the graph. The source treats it as a high-quality but expensive baseline. Multilevel spectral bisection improves runtime but remains slower than the proposed multilevel heuristic pipeline.

### Geometric Partitioning

Geometric methods use coordinates to partition spatial graphs. They can be fast, but they require geometric coordinates and may produce lower-quality partitions on irregular graphs where coordinates are unavailable or not strongly predictive of connectivity.

### Kernighan-Lin and Fiduccia-Mattheyses Refinement

KL/FM-style refinement moves vertices between partitions according to gain: the reduction in edge cut from moving a vertex, usually measured from external versus internal edge weights. The source uses this family as the local optimization stage during uncoarsening.

### Multilevel Graph Partitioning

Multilevel graph partitioning solves the problem by moving across graph scales:

1. coarsen the graph while preserving partition cut structure,
2. partition the small coarse graph,
3. project the partition back to finer graphs,
4. refine after each projection.

The key intuition is that coarse graphs expose global structure cheaply, while fine graphs provide local degrees of freedom for improvement.

### Streaming Graph Partitioning

Streaming graph partitioning solves the same balance-versus-cut problem while vertices are being loaded into a distributed system. Instead of assuming the whole graph is already available to an offline partitioner, a streaming partitioner assigns each arriving vertex to one partition and usually cannot move it later.

The source-backed setting from [[doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs|Stanton and Kliot]] is graph data layout for large distributed graph computation. The partitioner sees a vertex stream with incident edges and tries to reduce cross-machine communication while keeping partitions balanced.

The important boundary is that streaming methods are preprocessing/data-layout heuristics, not replacements for full-information partitioning. They are attractive when the graph must be loaded anyway and an offline partitioning pass would cost too much before the real graph computation starts.

## Source-Backed Design: METIS-Style Multilevel Partitioning

The Karypis-Kumar source selects the following practical recipe:

- **Heavy-edge matching for coarsening:** contract strongly connected vertex pairs first.
- **Greedy graph growing for initial coarse partitioning:** generate a cheap but good initial split.
- **Boundary KL refinement with a coarse-to-fine switch:** refine mostly around separator boundaries and avoid maintaining gains for every vertex on large fine graphs.

This design is implemented by the METIS graph partitioning and sparse matrix ordering system according to the paper's first-page implementation note.

## Source-Backed Design: LDG-Style Streaming Partitioning

The Stanton-Kliot source adds a second representative route: **Linear Deterministic Greedy (LDG)** for one-pass streaming graph partitioning.

LDG scores a candidate partition by combining:

- how many already-placed neighbors of the arriving vertex are in that partition,
- how much spare capacity the partition still has.

The paper's linear penalty is:

```text
score(i) = |P_t(i) cap Gamma(v)| * (1 - |P_t(i)| / C)
```

This makes the method more structure-aware than hashing while still lightweight enough to run during graph loading. In the KDD 2012 experiments, LDG is the most robust heuristic across BFS, DFS and random stream orders, and its edge-balanced variant improves Spark PageRank runtime on LiveJournal and Twitter graphs by reducing cross-partition edges.

## Sparse Matrix Ordering Connection

Graph partitioning also supports sparse matrix ordering through nested dissection.

The source-backed connection is:

- partition the graph,
- convert edge separators into vertex separators,
- recursively order subgraphs before separators,
- reduce fill and operation count in sparse matrix factorization.

This is a strong candidate for a future sibling/child node such as `sparse-matrix-ordering` if more sources enter the vault.

## Current Synthesis

Graph partitioning should be treated as a problem node, not as a paper-specific node. METIS, the Karypis-Kumar multilevel scheme, and Stanton-Kliot's LDG streaming heuristic are representative solutions under this problem.

The most useful abstraction for future absorption is:

- **problem:** balanced graph partitioning,
- **objective:** minimize edge cut under balance constraints,
- **offline method family:** multilevel coarsening + coarse partition + uncoarsening/refinement,
- **streaming method family:** loading-time vertex placement using local neighborhood and load information,
- **representative offline method:** HEM + GGGP + BKL(*,1),
- **representative streaming method:** LDG / Linear Deterministic Greedy,
- **application paths:** sparse matrix ordering through graph separators; distributed graph processing through data layout and communication reduction.

## Bridge Candidates

- Graph partitioning to sparse matrix ordering is source-backed by the paper and can become a durable bridge once the sparse matrix ordering endpoint exists.
- Graph partitioning to distributed graph processing is source-backed by Stanton-Kliot through Spark/PageRank experiments, but the endpoint `distributed-systems/distributed-graph-processing` does not yet exist. Keep this as a bridge candidate rather than creating a broad bridge to generic distributed systems.
- Graph partitioning to scalable proof generation or circuit partitioning is plausible but not yet source-backed in the current vault; it should remain a review candidate unless a source explicitly uses graph partitioning for proof/circuit workload decomposition.

## Representative Sources

- [[sha256-5d2825184682-fast-high-quality-multilevel-graph-partitioning|A Fast and High Quality Multilevel Scheme for Partitioning Irregular Graphs]]
- [[doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs|Streaming Graph Partitioning for Large Distributed Graphs]]

## Source Extensions

| Source | Delta | Evidence | Handling |
| --- | --- | --- | --- |
| [[sha256-5d2825184682-fast-high-quality-multilevel-graph-partitioning|A Fast and High Quality Multilevel Scheme for Partitioning Irregular Graphs]] | Adds METIS-style multilevel offline partitioning: HEM coarsening, GGGP initial partitioning, boundary KL refinement, and sparse matrix ordering via nested dissection. | source note p1-p28 | representative offline method |
| [[doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs|Streaming Graph Partitioning for Large Distributed Graphs]] | Adds streaming/loading-time graph partitioning and LDG as a lightweight data-layout heuristic for large distributed graph computation. | source note p2-p10 | representative streaming method; bridge candidate to distributed graph processing |

## Update Record

| Date | Run ID | Change | Sources |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-paper-intake-20260623-streaming-graph-partitioning | Added streaming graph partitioning and LDG as source-backed method family under graph partitioning. | [[doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs|Stanton and Kliot 2012]] |
