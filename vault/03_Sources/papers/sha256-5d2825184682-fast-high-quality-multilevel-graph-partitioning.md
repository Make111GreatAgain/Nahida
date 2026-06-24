---
id: sha256-5d2825184682-fast-high-quality-multilevel-graph-partitioning
title: "A Fast and High Quality Multilevel Scheme for Partitioning Irregular Graphs"
type: source
source_kind: paper
source_subtype: local_pdf
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: active
hierarchy_level: source
authors:
  - George Karypis
  - Vipin Kumar
year: 1998
venue: "Technical Report 95-035; to appear in SIAM Journal on Scientific Computing"
publisher: "University of Minnesota, Department of Computer Science"
status: absorbed
reading_status: deep_read_complete
reading_depth: deep
safe_for_absorption: true
classification_status: corrected_from_noisy_metadata
classification_confidence: high
primary_domain: algorithm-engineering
primary_direction: graph-algorithms
domain_id: algorithm-engineering
direction_id: graph-algorithms
topic_ids:
  - graph-partitioning
  - multilevel-graph-partitioning
  - sparse-matrix-ordering
  - nested-dissection
  - metis
primary_knowledge_path: "[[graph-partitioning|Algorithm engineering / Graph algorithms / Graph partitioning]]"
primary_ontology_path: "algorithm-engineering/graph-algorithms/graph-partitioning"
ontology_path:
  - algorithm-engineering
  - graph-algorithms
  - graph-partitioning
secondary_knowledge_paths:
  - "algorithm-engineering/graph-algorithms/sparse-matrix-ordering"
secondary_ontology_paths:
  - "algorithm-engineering/graph-algorithms/sparse-matrix-ordering"
source_refs:
  - "sha256:5d282518468247e122f341e5318171d3cd40a0f4c3b8ac424bcaff8754c5bfc7"
local_path: "~/Desktop/paper/download.pdf"
local_pdf_path: "~/Desktop/paper/download.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/download-5d2825184682-pages.txt"
page_count: 28
pages: 28
canonical_url: ""
doi: ""
arxiv_id: ""
knowledge_node_refs:
  - "[[algorithm-engineering]]"
  - "[[graph-algorithms]]"
  - "[[graph-partitioning]]"
bridge_refs: []
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "item0104"
run_id: "nahida-paper-intake-20260623-metis-multilevel-graph-partitioning"
managed_by: nahida
confidence: high
trust_tier: primary
created: 2026-06-23
updated: 2026-06-23
domains:
  - algorithm-engineering
topics:
  - graph partitioning
  - multilevel graph partitioning
  - sparse matrix ordering
  - METIS
aliases:
  - METIS multilevel graph partitioning paper
  - Fast and High Quality Multilevel Scheme
tags:
  - nahida/source/paper
  - nahida/domain/algorithm-engineering
  - nahida/graph-algorithms/graph-partitioning
---

# A Fast and High Quality Multilevel Scheme for Partitioning Irregular Graphs

## Source Identity

- **Corrected title:** A Fast and High Quality Multilevel Scheme for Partitioning Irregular Graphs.
- **Authors:** George Karypis and Vipin Kumar.
- **Institution:** Department of Computer Science, University of Minnesota.
- **Report / publication state:** Technical Report 95-035; the first page says it is to appear in *SIAM Journal on Scientific Computing*.
- **Date evidence:** the PDF first page includes a March 27, 1998 update marker; the local PDF metadata creation date is 1999. This note uses 1998 as the source year because it is the paper-visible date.
- **Local file:** `~/Desktop/paper/download.pdf`.
- **Queue correction:** the queue title `The algorithms described in this paper are implemented by the` is a boilerplate sentence from the first page, not the paper title. The queue classification `distributed-systems/consensus/needs-review` is also incorrect; the paper is about graph partitioning and sparse matrix ordering.

## Reading Coverage

- Pages 1-4: title, abstract, implementation note, introduction, and graph partitioning problem definition.
- Pages 4-11: multilevel bisection, coarsening, initial partitioning, uncoarsening, and refinement choices.
- Pages 11-19: partitioning experiments on irregular graphs and sparse matrices.
- Pages 19-21: multilevel nested dissection for sparse matrix ordering.
- Pages 21-24: algorithm characterization, conclusions, and comparative positioning.
- Pages 24-28: references and implementation appendix for the graph/coarsening/refinement data structures.

## Abstract-Level Claim

The paper designs and evaluates a multilevel graph partitioning scheme for irregular graphs. Its central contribution is not a new consensus protocol or blockchain mechanism, but an engineering recipe for high-quality, fast graph bisection and recursive k-way partitioning: coarsen the graph using heavy-edge matching, compute an initial partition on the small coarse graph using greedy graph growing, then project and refine the partition with boundary-focused Kernighan-Lin style refinement.

## Problem Field

This source belongs under [[graph-partitioning|graph partitioning]] in [[graph-algorithms|graph algorithms]].

The target problem is the balanced k-way graph partitioning problem:

- Partition a graph's vertices into k roughly equal parts.
- Minimize the weight or number of edges crossing between parts.
- Support weighted variants where vertex weights model work and edge weights model communication.

The paper motivates this problem through scientific computing, VLSI layout, task scheduling, sparse matrix-vector multiplication, and sparse matrix ordering. The common systems intuition is that balanced parts reduce local work imbalance while small edge cuts reduce communication or coupling cost.

## Method: Multilevel Graph Bisection

The proposed method has three phases.

1. **Coarsening:** repeatedly collapse vertices to build a sequence of smaller graphs while preserving the edge-cut value of partitions projected back to the original graph.
2. **Initial partitioning:** partition the smallest graph, where expensive or randomized procedures are cheap enough.
3. **Uncoarsening and refinement:** project the coarse partition back through the graph sequence and refine at each level.

This structure lets the algorithm capture global graph structure at coarse levels and use local improvement once the partition has enough fine-grained degrees of freedom.

## Coarsening Choices

The paper compares four matching schemes.

- **Random Matching (RM):** builds a randomized maximal matching in linear time.
- **Heavy Edge Matching (HEM):** matches each unmatched vertex with an unmatched neighbor connected by the heaviest edge. Because contracted matched edges disappear from the coarse graph, choosing heavy edges reduces coarse graph edge weight and empirically helps quality and speed.
- **Light Edge Matching (LEM):** prefers light edges, which tends to leave heavier coarse edges and often makes refinement work harder.
- **Heavy Clique Matching (HCM):** approximates a clique-density criterion for choosing contractions.

The experiments select HEM as the default because it gives consistently strong partition quality with the best overall runtime profile.

## Initial Partitioning Choices

The paper compares several ways to cut the coarsest graph.

- **Spectral bisection:** uses the Fiedler vector of the Laplacian. It can produce reasonable cuts but is slower and does not dominate once multilevel coarsening/refinement is present.
- **Kernighan-Lin / Fiduccia-Mattheyses style refinement:** uses vertex gains based on external minus internal edge weight and rolls back to the best prefix of moves.
- **Graph Growing Partitioning (GGP):** grows a region from random starts, then refines.
- **Greedy Graph Growing Partitioning (GGGP):** grows using a frontier ordered by gain; it gives good initial cuts quickly and becomes the chosen default.

The paper's practical point is that the coarsest graph should not be over-solved with an expensive global method if a cheaper method plus refinement gives comparable or better final cuts.

## Refinement Choices

Refinement is based on Kernighan-Lin style vertex moves, but the paper emphasizes boundary-focused variants.

- **KL:** full refinement can improve quality but is expensive.
- **KL(1):** one pass through refinement, faster but sometimes weaker.
- **Boundary KL (BKL):** only maintains vertices incident to cut edges in refinement data structures.
- **BKL(1):** one boundary pass.
- **BKL(*,1):** uses full BKL at coarse levels while the boundary is small, then switches to one-pass boundary refinement on finer graphs.

The chosen refinement strategy is BKL(*,1). It is designed around the observation that most useful moves are near the separator, so maintaining every vertex is unnecessary.

## Main Experimental Findings

The final multilevel graph partitioning algorithm combines HEM, GGGP, and BKL(*,1).

Against multilevel spectral bisection, it produces lower edge cuts across the evaluated problems and is much faster, especially on larger graphs. Against multilevel spectral bisection followed by KL refinement, it remains competitive or better in cut quality while avoiding the runtime cost of spectral methods. Against Chaco's multilevel partitioner, it usually produces smaller cuts and commonly runs several times faster.

The paper's evidence is empirical and engineering-oriented. It does not claim a new approximation guarantee; it shows that specific local choices inside a multilevel template materially affect quality and runtime.

## Sparse Matrix Ordering Extension

The paper also applies the same partitioning machinery to sparse matrix ordering through multilevel nested dissection.

The workflow is:

1. recursively bisect the graph,
2. derive an edge separator,
3. compute a minimum vertex cover of the bipartite graph induced by separator edges,
4. use that vertex separator for nested dissection ordering.

In the reported sparse matrix ordering experiments, multilevel nested dissection often requires fewer factorization operations than minimum degree ordering and spectral nested dissection, especially on large finite-element meshes. The paper also notes that nested dissection is more naturally parallelizable than minimum degree ordering.

## Implementation Details

The appendix describes the implementation behind the reported algorithms.

- The graph is stored with vertex and adjacency arrays carrying vertex weights, internal/external degrees, adjacency offsets, edge weights, and contraction metadata.
- Coarsening records a `Match` array and a coarse-vertex `Map`, then builds the contracted adjacency structure.
- Projection computes internal and external degrees incrementally during uncoarsening.
- Boundary refinement avoids explicit gain maintenance for non-boundary vertices and uses hash-table style boundary tracking.
- KL-style gain buckets are implemented with different table/list variants depending on the coarsening level and degree range.

This matters for absorption because the paper is not only a high-level algorithm description; it is also a systems-style implementation note for METIS-like graph partitioning.

## What This Source Adds to Nahida

- It introduces [[graph-partitioning|graph partitioning]] as a reusable problem field outside the prior blockchain/consensus-heavy parts of the vault.
- It gives a concrete source-backed algorithm family: multilevel graph partitioning.
- It introduces METIS as a representative implemented system for unstructured graph partitioning and sparse matrix ordering.
- It adds a reusable distinction between problem node and method instance: the durable knowledge node should be graph partitioning; METIS and this multilevel scheme are examples under that node.
- It creates a candidate bridge to sparse matrix ordering and a weaker future bridge to scalable proof-generation/circuit partitioning, but the latter should not be promoted without an explicit source showing the connection.

## Source-Backed Takeaways

- Balanced graph partitioning trades off load balance and communication/cut minimization.
- Multilevel methods improve both runtime and cut quality by solving an easier coarse problem and refining after projection.
- Heavy-edge matching is a strong coarsening heuristic because it contracts high-communication/high-coupling edges.
- Boundary-only refinement is a major practical optimization: it preserves most cut-improvement opportunities while reducing refinement cost.
- Sparse matrix ordering can use graph separators from partitioning to reduce fill and improve parallelism.

## Absorption Targets

- [[algorithm-engineering]]
- [[graph-algorithms]]
- [[graph-partitioning]]

## Review Notes

- No DOI, arXiv id, or stable canonical URL was visible in the local PDF text.
- The first-page implementation sentence mentions METIS and a historical URL, but this intake did not read the METIS repository or website.
- A future consolidation pass can add a separate sparse matrix ordering node if additional source notes support that area.
