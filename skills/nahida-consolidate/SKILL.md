---
name: nahida-consolidate
description: Use when Nahida must judge whether existing vault notes need integration, schema repair, knowledge-node refresh, bridge cleanup, migration, or no-op handling without rereading raw PDFs, repos, or web sources.
---

# Nahida Consolidate

Read `vault/00_System/NAHIDA_SPEC.md` before writing. This skill maintains Nahida from existing notes only. It should decide whether integration is needed, then perform the smallest safe action.

## Existing-Notes-Only Principle

Do not reopen raw PDFs, reclone repositories, browse the web, fetch DOI/arXiv/GitHub metadata, or reread external sources unless the user explicitly switches to update/research/deep-read mode. Treat existing source notes as the evidence boundary.

Use this skill when the user asks to:

- optimize the existing knowledge base,
- consolidate existing notes,
- avoid rereading papers/repos,
- repair a source-centric upper layer,
- migrate legacy claim/concept/map/synthesis content into the new architecture,
- decide whether Nahida should do nothing.

## Current Architecture

The canonical write lanes are:

- `03_Sources/`: complete external source notes.
- `04_Knowledge/`: recursive knowledge nodes. This is the target for useful legacy concept/map/synthesis content.
- `05_Bridges/`: cross-node bridge notes.

Legacy lanes are readable context only unless this run is explicitly a migration/repair task:

- `04_Claims/`
- `05_Concepts/`
- `06_Bridges/`
- `07_Maps/`
- `08_Projects/`
- `09_Syntheses/`

Routine consolidation should not delete, rename, or move legacy notes without explicit confirmation. Prefer creating/updating `04_Knowledge/` nodes and adding legacy refs/backlinks.

## Decision States

Every candidate note or scope must be classified before editing:

| State | Meaning | Allowed action |
| --- | --- | --- |
| `no_op` | Knowledge node/bridge is fresh, covered, and structurally valid | Report/ledger only |
| `metadata_patch` | YAML, source refs, ontology paths, aliases, freshness fields, or index rows are missing/inconsistent | Patch metadata/support only |
| `knowledge_refresh` | A `04_Knowledge/` node is missing, stale, too thin, or too source-centric | Create/update smallest affected knowledge node |
| `domain_dynamics_refresh` | An active L1 domain lacks `research-dynamics.md`, or the note is stale/thin/missing academic or industrial focus/open problems | Create/update `04_Knowledge/<domain>/research-dynamics.md` from existing notes only |
| `bridge_refresh` | A cross-node relation exists but endpoint refs, relation type, thesis, transfer boundary, or reciprocal links are weak | Create/update `05_Bridges/` and endpoint links |
| `legacy_migration` | Useful legacy claim/concept/map/synthesis content should be represented in Source + Knowledge + Bridge | Create/update new-lane notes; leave old note as legacy context |
| `question_memory` | Repeated/user-important query deserves reusable knowledge section or query report | Create/update knowledge section or generated query memory |
| `foundation_queue` | Existing notes reveal missing foundation that cannot be responsibly filled locally | Write review/follow-up; do not invent evergreen content |
| `deep_source_required` | Needed evidence is only in raw PDFs/repos/web, not in source notes | Stop that item and route to source skill |
| `review_only` | Merge, rename, taxonomy movement, or confidence upgrade is risky | Write review queue; no destructive changes |

Default to `no_op` unless evidence shows a useful, safe improvement.

## Promotion And Split Gate

Before creating or refreshing a knowledge node, classify content:

- `knowledge_node`: reusable domain/direction/problem/method/application node; split gate passes.
- `knowledge_section`: useful explanation inside an existing node; split gate does not pass.
- `source_extension`: one source's reusable delta, assumption, limitation, or representative example.
- `bridge_candidate`: cross-node relationship with at least two endpoint knowledge paths.
- `alias_query_key`: retrieval term, synonym, benchmark/dataset/tool name, or watch term.
- `review_only`: plausible but ambiguous taxonomy/bridge/foundation change.
- `not_promotable`: weak, noisy, duplicate, unsupported, or too source-specific.

Create a standalone knowledge node only when it is reusable beyond one source, has a clear parent and boundaries, improves retrieval, and is likely to collect more sources/questions/bridges. Otherwise fold the material into the nearest existing node.

Every retained knowledge/bridge note must be independently readable. If consolidation migrates legacy concept/map/synthesis content into `04_Knowledge/`, the resulting node must include its own definition, background, problem, boundaries, methods, representative sources, current synthesis, gaps, and update history. Do not create a note that only says "see old concept/map/synthesis."

Foundation examples:

- CFT/BFT/zk-SNARKs can be complete foundation knowledge nodes.
- Raft/PBFT/Groth16 are usually protocol instances or representative sections unless existing evidence/repeated queries justify scoped instance nodes.
- If a legacy note treats Raft or Groth16 as the whole foundation, repair by creating/updating the parent foundation node and demoting the instance to source extension or instance section.

## Cold-Start Hierarchy Repair

When existing notes contain sources but no usable hierarchy, consolidate must infer a parent-first structure from existing notes only:

```text
research field/domain -> direction -> research problem or method family -> optional subproblem/method -> source instance
```

Extract from source notes, legacy notes, generated indexes, and query reports:

- research/practice field,
- background and motivation,
- reusable problem,
- foundation concepts,
- method/protocol/model/architecture family,
- application/evaluation context,
- source instance.

Use this to reduce future query cost. A repair is valuable when it lets a future domain/direction/problem query read a knowledge node and a small source set instead of scanning many source notes. If the evidence is too weak, write a review item or `foundation_queue`; do not invent a confident taxonomy.

## Domain Research Dynamics Repair

Consolidate may create or refresh domain dynamics notes without rereading raw PDFs/repos/webpages:

```text
04_Knowledge/<domain>/research-dynamics.md
```

Use existing source notes, knowledge nodes, bridge notes, daily reports, watchlists, query gaps, and ledgers only. The note should cover latest recorded research dynamics, academic focus, industrial/practice focus, emerging topics, open problems, and directional tendency.

Refresh when:

- an active L1 domain lacks the note;
- `valid_until` is expired;
- new source notes exist after `evidence_window_end`;
- a domain has many source notes but no single place to answer latest/trend/open-problem questions;
- academic and industrial signals are mixed into scattered child notes.

If evidence is stale or too thin, mark the note `stale`/`review` and queue `nahida-daily-fetch` or `nahida-research-search` rather than inventing current trends.

## Candidate Discovery

Build the candidate table from:

- `03_Sources/` source notes.
- `04_Knowledge/` current nodes.
- `05_Bridges/` current bridges.
- Legacy notes in `04_Claims/`, `05_Concepts/`, `06_Bridges/`, `07_Maps/`, `08_Projects/`, `09_Syntheses/`.
- Generated indexes, ledgers, reports, review queues, and Bases.

Evaluate:

1. **Freshness**: `valid_until` expired, missing freshness fields, newer source extensions exist.
2. **Coverage**: source notes exist but no matching knowledge node or bridge exists.
3. **Hierarchy**: missing domain/direction/problem path, parent/child links, relation edges.
4. **Layer shape**: upper content is centered on one paper/repo instead of a reusable problem/method.
5. **Bridge quality**: endpoint knowledge refs, relation type, thesis, transfer matrix, or limits are missing.
6. **Query impact**: a top-down query would need to read many sources because the node is absent or stale.
7. **Cold-start hierarchy**: sources reveal reusable field/background/problem/foundation/method/application structure that has not been represented.
8. **Domain dynamics**: active L1 domains lack current trend/open-problem/focus notes or their evidence windows are stale.
9. **Risk**: destructive migration, broad taxonomy rename, or weak evidence needs review.

## Action Selection

Choose the smallest safe action:

- Prefer patching one knowledge node over rewriting a domain.
- Prefer adding a source-extension row over creating a child node when the split gate fails.
- Prefer creating a seed parent node when the parent path is absent and clearly needed.
- Prefer bridge notes for cross-node relations; do not mix cross-domain synthesis into endpoint nodes.
- Prefer review queues over brittle taxonomy merges.
- Prefer no-op when the existing node is fresh and sufficient.

Never create one direction per paper. Never create a standalone upper note merely because a source contains a named mechanism, experiment, dataset, theorem, optimization, or implementation detail.

## Legacy Migration Shape

When useful legacy notes exist:

- `05_Concepts/*` -> migrate durable explanations into a nearest `04_Knowledge/` node or section.
- `07_Maps/*` -> migrate navigation/taxonomy into knowledge node parent/child sections and relation edges.
- `09_Syntheses/*` -> migrate current-state content into the `当前综合` section of the matching knowledge node, preserving freshness fields.
- `06_Bridges/*` -> migrate or mirror into `05_Bridges/` when endpoint knowledge nodes can be resolved.
- `04_Claims/*` -> normally keep as legacy evidence refs; do not recreate claim files. Fold reusable assertions into knowledge text with source refs if supported.
- `08_Projects/*` -> keep as legacy source context; future repo analyses go to `03_Sources/github/`.

Do not delete or rename the old note unless the user explicitly asks. Add migration/review backlinks when useful.

## Pack Refresh Standard

For a `knowledge_refresh`, update/create a `knowledge` node using `vault/00_System/templates/knowledge_node.md` and include:

- `定义与范围`
- `背景`
- `解决的问题`
- `上层位置`
- `下级结构`
- `方法族与解决路线`
- `代表 Sources`
- `当前综合`
- `Source Extensions`
- `Bridge Links`
- `关系图谱`
- `缺口与队列`
- `更新记录`

If a section lacks evidence, write `gap` with a concrete next action. Do not fill the gap with unsourced confidence.

## Bridge Refresh Standard

Create or patch a bridge only when existing notes support at least two endpoint knowledge paths and a typed relationship. Required:

- `endpoint_knowledge_refs`
- `endpoint_paths`
- `relation_types`
- `relationship_thesis`
- `transfer_matrix`
- `non_transfer_boundary`
- `source_note_refs`
- `refresh_triggers`

New durable bridges live under `05_Bridges/`. Old `06_Bridges/` notes are legacy context until migrated.

## Report Contract

Every consolidation report must include:

- `Scope`: notes/paths considered and why.
- `Mode`: `existing_notes_only`.
- `Decision Table`: candidate, state, reason, evidence, risk.
- `Cold-Start Hierarchy Repair`: extracted field, background, problem, foundations, method family, application/evaluation context, source instance, confidence, handling.
- `Retrieval Optimization`: future queries helped, source notes avoided, summary/update benefit, create/merge/section/source-only decisions.
- `Knowledge Actions`: nodes created/updated/skipped, sections changed, freshness.
- `Domain Dynamics Actions`: domain dynamics notes created/refreshed/stale/unchanged/queued, evidence window, academic/industrial focus, emerging topics, open problems.
- `Bridge Actions`: bridge notes/candidates and endpoint knowledge paths.
- `Legacy Handling`: legacy notes read, migrated, left as-is, or queued.
- `No-op Justification`: when no write is needed.
- `Review Queue`: risky taxonomy, migration, stale evidence, missing source/deep-read.
- `Changed Files`: exact files touched.
- `Capability Usage`: Obsidian skills, Bases/Canvas, indexes, filesystem search, or fallbacks.

## Quality Gate

Before finishing:

- No raw PDFs/repos/webpages were reread in existing-notes-only mode.
- New routine upper memory landed in `04_Knowledge/` or `05_Bridges/`.
- Legacy notes were not destructively moved/deleted/renamed without confirmation.
- Source-specific details were not promoted into standalone knowledge nodes.
- Missing/thin hierarchy was repaired or explicitly reported with exact next action.
- Active L1 domains have `research-dynamics.md` or a stale/queued reason.
- Cross-node relations are in bridge notes or bridge-candidate review items.
- The report clearly distinguishes `no_op`, `knowledge_refresh`, `bridge_refresh`, `legacy_migration`, and `review_only`.

## Boundaries

- May write `04_Knowledge/`, `05_Bridges/`, generated reports, indexes, ledgers, review queues, and managed Obsidian Bases/Canvas files.
- May patch metadata in source/knowledge/bridge notes when safe.
- May read legacy lanes.
- Must not perform external research, repo clone, or PDF reread unless the user explicitly changes mode.
