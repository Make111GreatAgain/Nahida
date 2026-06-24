---
name: nahida-update
description: Use when the user wants to add, import, organize, consolidate, refresh, queue, or update Nahida from PDFs, folders, URLs, webpages, text, GitHub repositories, keywords, existing notes, or mixed inputs.
---

# Nahida Update

Read `vault/00_System/NAHIDA_SPEC.md` before writing. This is Nahida's primary write router. It chooses the correct source adapter, makes sure the source note is complete, then hands the result to `nahida-knowledge-get` or `nahida-consolidate`.

## Current Architecture

New managed writes use the sequential main lanes:

- `03_Sources/`: complete source notes from papers, GitHub repositories, web pages/research, daily freshness, datasets, PDFs, and direct user material.
- `04_Knowledge/`: recursive knowledge nodes for domains, directions, problems, subproblems, method families, application areas, evaluation axes, and current synthesis sections.
- `05_Bridges/`: typed cross-node relationships between knowledge nodes.

Legacy lanes (`04_Claims/`, `05_Concepts/`, `06_Bridges/`, `07_Maps/`, `08_Projects/`, `09_Syntheses/`) are read-only compatibility context unless the user explicitly asks for migration, audit, or legacy repair.

## Core Standard

Do not ask the user to choose a low-level skill when intent is clear. Identify the input type, preserve provenance, write Chinese-first notes, and keep the knowledge tree clean. A good update pass:

1. Creates or updates a complete source note in `03_Sources/`.
2. Resolves a bounded domain/direction/problem path.
3. Uses `nahida-knowledge-get` to update `04_Knowledge/` and `05_Bridges/`.
4. Records queues, gaps, freshness, and review items.

Do not make the whole knowledge base source-centric. Papers, repositories, and webpages are source evidence. Durable understanding lives in knowledge nodes and bridges.

Every durable note must be standalone:

- `03_Sources/*` notes must be complete source memories, not pointers.
- `04_Knowledge/*` notes must be complete explanations of their concept/direction/problem/method. A linked prerequisite can provide deeper detail, but the current note still needs a concise local definition and boundary.
- `05_Bridges/*` notes must be complete cross-node relation notes, including endpoint background, relation type, evidence, transfer limits, and non-transfer boundary.

## Input Router

| Input | Route |
| --- | --- |
| Single paper PDF, DOI, arXiv, paper URL, XiaoLvJing/Zotero metadata | `nahida-paper-read` -> `nahida-knowledge-get` |
| Folder containing many PDFs | build conservative serial queue, process one paper at a time through `nahida-paper-read` -> `nahida-knowledge-get`, checkpoint, continue |
| GitHub URL, `owner/repo`, branch, commit, release tag, local checkout | `nahida-github-repo-analyze` -> `nahida-knowledge-get` |
| Multiple GitHub repos | build serial repo queue, analyze one repo at a time, checkpoint, continue |
| Web URL, article, docs page, pasted webpage text | `nahida-research-search` or direct `03_Sources/web/` note -> `nahida-knowledge-get` |
| Research keyword, concept, technical question, "帮我调研" | `nahida-research-search` -> `nahida-knowledge-get` |
| "最新", "最近", "每天", "定时", "更新一下" | `nahida-daily-fetch` -> deeper source skills or `nahida-knowledge-get` |
| Existing Nahida notes, "优化现有知识库", "整合已有笔记", "不要重新读论文/仓库" | `nahida-consolidate` |
| User asks a question rather than adding/updating | `nahida-query` |

When input is ambiguous and low risk, proceed with the most likely route and record the assumption. Ask one concise clarification only when the route changes what sources will be read or written.

## Capability Orchestration

Use existing skills/plugins/connectors before ad hoc file handling:

- `obsidian-markdown` and `obsidian-note` are hard prerequisites for high-quality Obsidian Markdown/YAML/wikilink writes.
- `obsidian-bases` should be used for dashboards, queues, review tables, or filtered source/knowledge views.
- `json-canvas` should be used for high-value visual bridge or knowledge graphs, not every small update.
- Codex bundled workspace dependencies should be used for PDF/document extraction before requiring system tools.
- CodeGraph should be used for repository structure and code-flow analysis when available.
- GitHub connector or `gh` may be used for repository metadata when available.
- Web search/browser is used only for update/research/freshness tasks, not for `nahida-query` vault-only answers.

Record capability usage and fallbacks in update reports. If Obsidian writing skills are unavailable, stop with `prerequisite_gap` unless the user explicitly accepts a plain Markdown fallback.

## PDF Runtime Policy

When processing PDFs in Codex App:

1. Call `load_workspace_dependencies` to locate bundled Python and packages.
2. Prefer bundled `pypdf`, then `pdfplumber`, then `PyMuPDF/fitz` for inventory/extraction.
3. Inventory at minimum: path, size, SHA-256, metadata title/authors, page count, first-page text, abstract-like text, DOI/arXiv hints, extractor, extraction errors.
4. Do not mutate original PDFs.
5. Mark scanned/poor extraction as `extraction_gap` and keep it in queue.

## Conservative Deduplication

Avoid losing distinct papers or repos:

- Automatic PDF duplicates require exact DOI, exact arXiv ID, exact checksum/content hash, or another strong canonical ID.
- Title similarity, same venue header, publisher boilerplate, generic proceedings title, or filename similarity is review-only.
- Weak or generic titles must not create high-confidence identities, classifications, or priorities.
- Record `identity_key`, `dedupe_evidence`, `dedupe_confidence`, and review status.

## Serial Queue Policy

Folder/list updates are resumable serial queues, not one-shot samples.

- Default mode is `serial_auto` unless the user sets a hard item limit.
- Process exactly one high-quality source at a time, then continue to the next pending item after the source note and knowledge handoff checkpoint.
- Checkpoint after every item: `queue_id`, `item_id`, status, processed count, remaining count, current item, last processed item, next item, failure reason, resume command, and `continuation_required`.
- Do not mark a queue `succeeded` while pending items remain. Use `partial_serial_pending`, `blocked`, or `complete`.
- Stop only for queue exhaustion, explicit `user_item_limit`, repeated blocker, human disambiguation, extraction/access failure, or safety/storage issue.
- If a soft turn/context budget is reached, write a checkpoint and use a continuation mechanism when available; it is a pause, not completion.

## Source Quality Gates

Papers and repositories need deep source notes before durable knowledge:

- Paper inventory may be shallow, but source absorption needs `nahida-paper-read` with deep or explicitly scoped reading.
- Repo scouting may be shallow, but implementation knowledge needs `nahida-github-repo-analyze` with deep or explicitly scoped code analysis.
- Web/search notes must distinguish stable reference, blog/practice, paper candidate, repo candidate, and news/freshness signal.
- Daily/news signals are freshness evidence, not evergreen foundation unless corroborated.

## Knowledge Path Discipline

For every non-trivial source, derive a candidate path:

```text
domain / direction / problem-or-topic / optional-subproblem-or-method
```

Examples:

- `blockchain-systems/consensus/byzantine-fault-tolerance`
- `blockchain-systems/consensus/crash-fault-tolerance`
- `zero-knowledge-proofs/polynomial-commitments/kzg-commitments`
- `zero-knowledge-proofs/proof-systems/folding-schemes`
- `ai-agents/agent-memory/episodic-memory`

Use the split gate from the spec before creating a new knowledge node. A source-specific mechanism, one benchmark result, or a single repository module usually becomes a source-extension row, not a new node.

If a parent domain/direction/problem is missing or thin, ask `nahida-knowledge-get` to create a seed/foundation-thin knowledge node or queue a `foundation_pack` search.

## Cold-Start Hierarchy Discovery

When Nahida has no useful hierarchy for an incoming source, do not stop at broad labels such as `AI`, `Blockchain`, or `ZKP`. First extract a provisional hierarchy from source metadata, content evidence, and existing vault hints:

```text
research field/domain -> direction -> research problem or method family -> optional subproblem/method -> source instance
```

For every new source or source set, require the source skill to hand off:

- research/practice field,
- research background and motivation,
- reusable research/practice problem,
- foundation concepts the source depends on,
- method/protocol/model/architecture family,
- application or evaluation context,
- artifact/source instance such as paper system, protocol instance, repository, module, benchmark, or release.

The purpose of hierarchy discovery is retrieval and maintenance. A good path lets future `nahida-query` answer from domain/direction/problem nodes first, open fewer source notes, and refresh a whole field/direction without rereading every paper or repo.

Create parent-first seed nodes only when they improve retrieval or update scope. Otherwise keep the material as a section, source-extension row, alias/query key, watch term, or review item.

## Domain Research Dynamics

For every active L1 domain, Nahida should maintain one living domain dynamics note:

```text
04_Knowledge/<domain>/research-dynamics.md
```

This note tracks the domain's latest recorded research dynamics, academic focus, industrial/practice focus, emerging topics, open problems, and directional tendencies. It is the first retrieval target for questions about "最新进展", "研究趋势", "学术/工业界关注什么", and "还有哪些待解决问题".

During update runs, decide for each affected L1 domain:

- `created`: domain is new/active and no dynamics note exists.
- `refreshed`: new source materially changes domain-level movement, priorities, open problems, or academic/industrial focus.
- `unchanged`: source only adds a narrow source extension and does not affect domain-level dynamics.
- `stale`: `valid_until` expired or newer sources exist but synthesis is not refreshed.
- `queued`: more source reading/research is needed before refreshing responsibly.

Do not rewrite a domain dynamics note for every source. Refresh it when the source changes domain-level understanding or when freshness expires.

## Foundation Concept Examples

Use these examples when deciding whether to create a knowledge node:

| Correct | Wrong |
| --- | --- |
| `CFT` and `BFT` are foundational consensus concepts; create complete knowledge nodes when missing and attach Raft/PBFT/Tendermint-like sources as representatives or instances. | Treat `Raft` or one BFT paper as the foundational concept and leave CFT/BFT unexplained. |
| `zk-SNARKs` is a foundational ZKP proof-system concept; write a complete node and cite sources. | Treat `Groth16` as the definition of zk-SNARKs or require readers to open one paper to understand SNARKs. |
| `KZG commitments` can be a knowledge node when it supports polynomial commitments, SNARKs, or data availability across sources. | Only summarize the KZG paper without explaining the reusable commitment concept. |

Paper/repo-specific systems, protocol instances, benchmark results, implementation tricks, and one-off optimizations usually become source extensions, not foundational nodes.

Knowledge-building updates may use web research to fill missing foundations when the user asked to add/update/research. Prefer canonical sources such as surveys, official docs/specs, standards, textbooks, or widely cited papers. `nahida-query` remains vault-only and must not use web research.

## Required Procedure

1. Establish run context:
   - Record request, date, input paths/URLs/text, scope, mode, and run ID.
   - Inspect existing `03_Sources/`, `04_Knowledge/`, `05_Bridges/`, generated indexes, ledgers, review queues, and relevant legacy notes.
2. Route and dedupe:
   - Split mixed inputs.
   - Apply conservative duplicate rules.
   - Build queue if multiple papers/repos/sources exist.
3. Produce source notes:
   - Use the appropriate source skill.
   - Ensure each source note is detailed, Chinese-first, path-safe, and stable under `03_Sources/`.
   - Do not store cloned repositories or raw PDFs inside the vault except managed raw/extraction metadata.
4. Handoff to knowledge:
   - Run or follow `nahida-knowledge-get` on completed source notes.
   - For incomplete source notes, write review/queue records instead of confident knowledge.
5. Consolidate when needed:
   - If the task is existing-note optimization or the new source reveals stale/fragmented upper memory, call/follow `nahida-consolidate`.
6. Report:
   - Explain source notes created, knowledge nodes/bridges updated or queued, pending items, gaps, and exact next action.

## Output Contract

An update report should include:

- `Input Recognition`: input types, routes, assumptions.
- `Queue State`: for multi-source runs, including next item and continuation status.
- `Source Outputs`: created/updated source notes and readiness.
- `Knowledge Handoff`: target knowledge paths, source-extension intent, bridge candidates.
- `Cold-Start Hierarchy Discovery`: field, background, problem, foundations, method family, application/evaluation context, source instance, evidence, confidence.
- `Retrieval Optimization`: future queries helped, source reads avoided, summary/update benefit, create/merge/section/source-only decisions.
- `Knowledge Updates`: nodes created/updated/queued by `nahida-knowledge-get`.
- `Domain Dynamics`: affected L1 domains, `research-dynamics.md` status, evidence window, academic focus, industrial focus, emerging topics, open problems, and next refresh action.
- `Bridge Updates`: bridge notes/candidates and endpoint knowledge paths.
- `Foundation Gaps`: missing parent nodes or foundation searches to run.
- `Deduplication`: strong duplicates and possible-duplicate review items.
- `Capability Usage`: skills/tools used and fallbacks.
- `Review Queue`: uncertain classifications, weak extraction, risky migrations.
- `Changed Files`: exact managed files touched.

## Quality Gate

Before finishing:

- New routine writes landed in `03_Sources/`, `04_Knowledge/`, `05_Bridges/`, or `90_Generated/`.
- No cloned repo or large code checkout is inside the Nahida vault/repo.
- Source notes are complete enough for their declared depth.
- Knowledge nodes are not one-paper/one-repo summaries unless explicitly marked seed and justified.
- Cold-start updates identify reusable hierarchy before writing durable upper memory.
- The resulting hierarchy would reduce future source-note reads for at least one likely query or it stays as source-only/review material.
- Each affected active L1 domain has a `research-dynamics.md` note, or the run records why it is queued/stale/not needed.
- Bridges have endpoint knowledge refs and transfer limits.
- Multi-source queues are not reported complete while pending items remain.
- The final user-facing message says whether work is complete, partial, blocked, or queued.

## Boundaries

- May write source notes, knowledge nodes, bridges, generated reports, indexes, ledgers, review queues, and managed Bases/Canvas files when useful.
- May read legacy lanes for context.
- Must not routinely write new notes to legacy claim/concept/map/project/synthesis lanes.
- Must not delete, rename, bulk migrate, or retire existing notes without explicit confirmation.
