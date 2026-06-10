---
title: "Nahida Spec"
type: "system"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Nahida Spec

Nahida is an AI-native Obsidian knowledge base. Obsidian is the human interface; Markdown/YAML is the durable knowledge layer; Codex skills maintain the system.

## Naming Contract

- System name: `Nahida`.
- Managed note marker: `managed_by: nahida`.
- New managed note IDs should start with `nahida-` unless the canonical identity is a DOI, arXiv ID, GitHub repo, release tag, commit SHA, or another stable external ID.
- New skills must use the `nahida-*` prefix.
- Historical `kb-*` names are planning aliases only.

## Canonical Topology

```text
00_System/
01_Inbox/
02_Raw/
03_Sources/
04_Claims/
05_Concepts/
06_Bridges/
07_Maps/
08_Projects/
90_Generated/
99_Archive/
```

## Managed Zone

Automation may create or append only under these paths unless explicitly confirmed:

- `01_Inbox/`
- `02_Raw/`
- `03_Sources/`
- `04_Claims/`
- `05_Concepts/`
- `06_Bridges/`
- `07_Maps/`
- `08_Projects/` for managed projects only
- `90_Generated/`

Any user-authored path outside the managed zone is read-only by default.

## Universal Properties

Every managed note should include:

```yaml
---
id: "nahida-..."
title: "..."
type: "source|claim|concept|bridge|map|project|run|review_queue"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active|review|stale|retired|archived"
status: "<type-specific status>"
domains: []
topics: []
aliases: []
tags: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
managed_by: "nahida"
run_ids: []
source_refs: []
confidence: "unknown|low|medium|high"
trust_tier: "unknown|primary|secondary|tertiary|personal"
---
```

## Note Types

- `source` - a standardized wrapper around external evidence.
- `claim` - an atomic source-backed assertion.
- `concept` - durable explanation of a reusable idea.
- `bridge` - explicit cross-domain relationship.
- `map` - entry point for a domain, topic, or cross-domain area.
- `project` - watched project or repo knowledge.
- `run` - automation run log.
- `review_queue` - uncertain or destructive proposals awaiting review.

## Data Source Lanes

### Web

Classify web sources before distillation:

- `web_reference` - official docs, standards, API docs.
- `web_concept` - evergreen explainers and tutorials.
- `web_blog` - engineering posts, opinions, field notes.
- `web_news` - launches, announcements, time-sensitive coverage.

`web_news` should not directly update evergreen concept notes unless corroborated.

### GitHub

GitHub repositories are practice evidence. A Nahida pass should capture repo purpose, maturity, modules, entry points, implementation patterns, dependencies, releases, and README-vs-code gaps. If a CodeGraph index exists, prefer codegraph-backed summaries.

### Papers

Treat local PDFs, XiaoLvJing exports, Zotero exports, and emerging paper feeds as adapters into the same normalized paper candidate shape. Deduplicate by DOI, arXiv ID, checksum, title/authors/year, then soft similarity.

### Direction Evolution

Nahida should discover finer directions from the evidence stream. Broad domains such as `AI` should self-refine into subdirections such as `memory`, `multi-agent`, `subagent`, `tool use`, or `context engineering` when source support is strong enough.

## Write Modes

- `read_only` - inspect and report only.
- `suggest` - write proposals to review queues.
- `managed_append` - append managed sections and ledgers.
- `managed_patch` - patch known machine-owned sections.
- `confirmed_refactor` - rename, split, merge, move, or retire after confirmation.

Daily automation defaults to `managed_append` and `suggest`.

## Safety Rules

- Do not delete, merge, rename IDs, bulk rewrite, or cross zones without confirmation.
- Every automated write must produce a run record or write-ledger entry.
- All claims must trace to sources or be marked tentative.
- Generated indexes are rebuildable caches, not the source of truth.
