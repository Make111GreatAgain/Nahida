---
name: nahida-paper-read
description: Use when the user provides a specific academic paper PDF, DOI/arXiv paper, local paper file, XiaoLvJing export, Zotero export, or paper metadata that should become a Nahida paper source note.
---

# Nahida Paper Read

Read `vault/00_System/NAHIDA_SPEC.md` before writing. This skill reads one paper into a complete source note under `03_Sources/papers/`. It does not create durable knowledge nodes or bridges by itself; it prepares evidence and handoff candidates for `nahida-knowledge-get`.

## Current Architecture

- Output lane: `03_Sources/papers/`.
- Handoff lane: `nahida-knowledge-get` updates `04_Knowledge/` and `05_Bridges/`.
- Do not write new routine notes to legacy `04_Claims/`, `05_Concepts/`, `07_Maps/`, or `09_Syntheses/`.

## Core Standard

The output is a deep academic reading note and bottom-layer memory unit, not an abstract digest. It must be precise, Chinese-first, source-grounded, and useful to future agents without reopening the PDF for ordinary questions.

If a detail is unavailable, write `unknown` and explain how it could be verified. Do not infer venue, result numbers, equations, theorem claims, or author claims without evidence from the PDF or reliable metadata.

The source note must preserve the paper in detail, but it must not treat every paper term as a new upper concept. Mark foundation candidates for `nahida-knowledge-get`:

- Foundation candidates: CFT, BFT, zk-SNARKs, polynomial commitments, consensus, verifiable computation, agent memory when they are used as reusable background.
- Instance/source-extension candidates: Raft, PBFT, Groth16, a named system, one benchmark, one theorem detail, one repository implementation, one optimization from this paper.

Correct: explain how the paper extends a foundation and hand off the foundation gap. Wrong: create a paper-centered concept where readers must read the paper note to understand the foundation.

## Cold-Start Handoff Standard

When the vault has no clear hierarchy for this paper, the paper note must still infer reusable candidates from metadata and paper content before handoff. Use title, abstract, keywords, venue, introduction, related work, problem formulation, method, evaluation, and conclusion to extract:

- research field/domain,
- research background and motivation,
- reusable research problem,
- foundation concepts the paper depends on,
- method/protocol/model/proof family,
- application or evaluation context,
- artifact/source instance, such as the paper's named system, protocol instance, theorem, benchmark, or dataset.

The handoff should explain how these candidates help future query read fewer notes. If a candidate is only paper-specific, mark it as `source_extension` or `source_only`; do not turn it into an upper knowledge node.

## PDF Runtime

In Codex App, use bundled workspace dependencies before system tools:

1. Call `load_workspace_dependencies` when available.
2. Use bundled Python and try `pypdf`, `pdfplumber`, then `PyMuPDF/fitz`.
3. Extract metadata, page count, table of contents/section hints, text, DOI/arXiv hints, figures/tables captions when accessible, and extraction errors.
4. Do not mutate original PDFs.
5. If extraction is poor/scanned, mark `reading_status: extraction_gap` or `deep_read_pending` and do not hand off as confident evidence.

## Deep Reading Requirement

For a normal paper, deep reading should cover:

- title, authors, venue/conference/journal if available, year, DOI/arXiv/canonical URL,
- abstract, introduction, background/related work,
- problem formulation and assumptions,
- method/protocol/algorithm/model/system design,
- theory/proofs/security/model arguments when relevant,
- experiments/evaluation: baselines, metrics, datasets, setup, results, ablations,
- limitations, threats, failure cases, future work,
- appendices when they contain core proofs, algorithms, extra evaluations, or implementation details.

Use `deep_read_complete` only when the coverage supports durable retrieval. For long papers or scoped requests, use `scoped_deep_read` and state exact coverage. Metadata-only, first-pages-only, or abstract-only notes are staging notes.

## Required Procedure

1. Establish identity:
   - Normalize title, authors, year, venue, DOI, arXiv, canonical URL, local path, checksum.
   - Deduplicate against `03_Sources/papers/` using strong identity first: DOI, arXiv, checksum, publisher/library ID. Weak title similarity goes to review.
2. Read the paper:
   - Build a section/page map.
   - Record reading coverage and extraction quality.
   - Anchor important points to page, section, theorem, algorithm, figure, table, appendix, or quote context.
3. Analyze:
   - Problem solved.
   - Key idea and mechanism.
   - Innovation relative to prior work as described by the paper.
   - Assumptions and threat/model boundaries.
   - Experimental/theoretical evidence.
   - Limitations and open questions.
   - Terms, methods, datasets, benchmarks, protocols, systems, and evaluation axes.
4. Classify handoff candidates:
   - L1 domain candidate.
   - L2 direction candidate.
   - L3 problem/topic/method candidates.
   - Cold-start hierarchy facets: research field/domain, background, problem, foundations, method family, application/evaluation context, source instance.
   - Possible source-extension targets in `04_Knowledge/`.
   - Possible bridge endpoints in `05_Bridges/`.
   - Foundation gaps and follow-up searches.
5. Write source note:
   - Use `vault/00_System/templates/paper_reading.md` or `source.md`.
   - Store under `03_Sources/papers/` with a path-safe stable filename.
   - Include `reading_depth`, `reading_status`, `safe_for_absorption`, `source_note_refs`, `primary_ontology_path` candidate, and `classification_status`.
6. Handoff:
   - If safe for absorption, run/follow `nahida-knowledge-get`.
   - If not safe, write review/queue items and do not promote the paper to durable knowledge.

## Output Contract

The paper note must include:

- `Paper Identity`: title, authors, venue, year, DOI/arXiv, canonical URL, local path, checksum.
- `Reading Coverage`: pages/sections covered, extraction quality, skipped areas, safe-for-absorption decision.
- `Structured Summary`: problem, motivation, method, innovation, evidence, limitations.
- `Detailed Outline`: section/page map with each section's role.
- `Technical Content`: algorithms, equations/protocol steps, architecture, assumptions, proofs, implementation details when relevant.
- `Evidence Table`: major findings with anchors and confidence.
- `Evaluation`: baselines, metrics, datasets, results, caveats.
- `Knowledge Handoff`: target knowledge nodes/sections, source-extension deltas, bridge candidates, aliases/query keys, foundation gaps.
- `Cold-Start Hierarchy Discovery`: field, background, problem, foundation concepts, method family, application/evaluation context, source instance, evidence, confidence.
- `Retrieval Optimization`: future queries helped, source reads avoided, content that remains source-only.
- `Domain Dynamics Impact`: whether the paper affects L1 domain research dynamics, academic focus, open problems, emerging terms, or should remain only a child source extension.
- `Foundation Candidate Judgment`: which terms are true foundations, which are protocol/source instances, and why.
- `Review Items`: uncertain metadata, weak extraction, classification uncertainty, needed follow-up.

## Quality Gate

Before finishing:

- The source note is detailed enough to answer ordinary paper questions.
- Every major author claim has a location or is marked as inference/abstract-only.
- Results include baselines/metrics when provided by the paper.
- The paper is not silently used as durable knowledge if reading is incomplete.
- The handoff uses Source + Knowledge + Bridge terms, not legacy claim/concept/map/synthesis as primary outputs.

## Boundaries

- May write `02_Raw/pdf/`, `03_Sources/papers/`, generated reports, ledgers, indexes, review queues.
- Must not create/update `04_Knowledge/` or `05_Bridges/` directly; use `nahida-knowledge-get`.
- Must not move source notes based on direction classification.
