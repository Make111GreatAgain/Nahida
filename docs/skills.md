# Nahida Skills

Nahida starts with a small skill surface. Each skill is intentionally strict: it defines input assumptions, required procedure, output contract, quality gate, and boundaries.

All generated notes should be Chinese-first. Keep canonical English technical terms, paper/repo names, APIs, protocols, code symbols, file paths, and URLs in English when they are the precise retrieval keys.

## Capability Requirements

Nahida should use existing Codex skills/plugins/connectors intelligently:

- Required for Obsidian note writing/querying: `obsidian-markdown`, `obsidian-note`
- Preferred for richer vault surfaces: `obsidian-bases`, `json-canvas`
- Task-specific: CodeGraph for repository code, GitHub connector/`gh` for GitHub context, `load_workspace_dependencies` for PDFs/documents, browser/web search for current source verification

Substantial runs should record capability usage. Missing hard prerequisites should produce `prerequisite_gap` instead of silent low-quality fallback.

## Intelligent Entry Skills

- `nahida-update`: use for adding, importing, organizing, refreshing, queueing, or updating knowledge. It routes PDFs, folders, URLs, pasted text, GitHub repos, web searches, daily refreshes, and existing notes to the right lower-level skill. Multiple PDFs/repos become an intake queue by default; deep processing stays one source at a time, but the queue should continue serially until exhausted, explicitly limited, or blocked.
- `nahida-query`: use for vault-only questions about what Nahida already knows, retrieving sources, comparing directions, finding gaps, and deciding whether an update is needed. It must say when the vault lacks evidence instead of searching externally.

## Specialized Skills

- `nahida-paper-read`: use for one specific paper PDF or metadata record. It creates a deep structured academic reading note and hands it to `nahida-knowledge-get` only when reading coverage is adequate or explicitly scoped.
- `nahida-github-repo-analyze`: use for one specific GitHub repository or local checkout. It performs deep repo reading across docs, code, modules, APIs, tests/examples, and primary flows, then hands the result to `nahida-knowledge-get` only when coverage is adequate or explicitly scoped.
- `nahida-research-search`: use for a specific web research query. It classifies sources, deduplicates them, synthesizes a research note, and hands it to `nahida-knowledge-get`.
- `nahida-daily-fetch`: use for current-interest freshness passes. It reads maps/watchlists, builds non-duplicative queries, accepts only high-signal items, and creates follow-up tasks.
- `nahida-knowledge-get`: use to absorb source notes into claims, concepts, directions, aliases, bridges, maps, synthesis notes, indexes, and review queues.
- `nahida-audit`: use to inspect the vault for structural, provenance, duplication, link, and output-quality issues.

## Normal Flow

```text
user input ----------> nahida-update -------------> specialized skills ----> lower notes ----> nahida-knowledge-get ----> maps/syntheses/indexes
user question -------> nahida-query --------------> query memory + fresh syntheses/maps ----> lower notes only as needed
```

## Quality Principle

Every durable knowledge object must preserve provenance. If a claim, direction, map update, or concept cannot point back to evidence, it should remain tentative or enter a review queue.

Claims and concepts have different jobs. A `claim` is an atomic, reusable assertion with evidence; create it only when future notes may cite it. A `concept` is a foundation/explainer note: it may use Codex prior knowledge for structure, but durable content should be calibrated by vault sources or stable web/reference sources. Papers and repos should be recorded as `source_extension` entries that extend, implement, challenge, or refine the existing concept.

Nahida is layered memory. Lower-layer notes must be independently useful and detailed; upper-layer `09_Syntheses/` notes summarize direction state, cross-direction relationships, emerging directions, hot topics, and recurring questions. Synthesis notes should cite lower-layer notes and carry freshness fields such as `last_synthesized`, `valid_until`, and `freshness_status`.

Queries preserve provenance by staying vault-only by default. `nahida-query` should not browse, fetch metadata, clone repositories, or inspect local files outside Nahida. For missing papers, repositories, directions, or latest-progress evidence, it reports `知识库没有记录`, `知识库只有部分记录`, or `知识库没有足够新近资料`, then suggests a concrete `nahida-update` command.

Queries should be semantic and facet-based. Source notes are stored by stable identity and source type, while directions live in frontmatter, tags, maps, links, indexes, ledgers, and query reports. `nahida-query` should normalize the question, expand aliases from the vault, check prior query reports, and synthesize across sources rather than relying on direction folders.

Queries should be top-down. Reuse fresh synthesis notes when they cover the question; drill into lower-layer source/project notes only when the upper layer is stale, missing, contested, or insufficient.

Papers and repositories require deep reading before they become confident durable evidence. Abstract-only, metadata-only, README-only, file-tree-only, or scouting notes can support indexes, ledgers, and review queues, but should not produce confident claims, concepts, maps, or bridges.

Directions should be precise but not fragmented. Do not create one direction per paper. Use existing maps when possible, create new direction candidates when terminology and evidence justify it, and fill missing foundations through `nahida-research-search` plus `nahida-knowledge-get`.

Nahida should self-upgrade. Every non-trivial update should produce bounded expansion candidates: child directions, adjacent directions, missing foundations, representative papers/repos, standards, datasets, benchmarks, tools, bridge candidates, and daily-fetch watch terms.

Classification should be stable. Source note identity should be based on DOI, arXiv, checksum, canonical URL, or normalized title, while mutable direction placement lives in frontmatter, maps, indexes, and classification ledgers. Low-confidence classifications should stay staged or in review instead of causing immediate folder churn.
