---
name: nahida-knowledge-get
description: Use when Nahida source notes already exist and must be absorbed into the Source + Knowledge + Bridge knowledge base.
---

# Nahida Knowledge Get

Read `vault/00_System/NAHIDA_SPEC.md` before writing. This skill is Nahida's bottom-up absorption layer. It takes complete source notes from papers, GitHub repositories, web research, daily fetches, or pasted/direct sources, then updates the durable knowledge tree and bridge layer.

## Current Architecture

New writes use only the sequential main lanes:

- `03_Sources/`: external evidence notes. Papers, GitHub repositories, web pages, web research notes, daily freshness notes, datasets, PDFs, and other source artifacts live here.
- `04_Knowledge/`: recursive knowledge nodes. This lane replaces routine `claim`, `concept`, `map`, and `synthesis` writes.
- `05_Bridges/`: typed cross-node relationships. Bridges connect knowledge nodes and cite sources for evidence.

Legacy lanes may be read but must not receive routine new absorption output:

- `04_Claims/`
- `05_Concepts/`
- `06_Bridges/`
- `07_Maps/`
- `08_Projects/`
- `09_Syntheses/`

If older notes or templates mention claims, concepts, maps, projects, or syntheses, interpret them as legacy context. Normalize new durable output into `04_Knowledge/` and `05_Bridges/`.

## Core Standard

Do not summarize a source into a new source-shaped upper page. Preserve the source as detailed evidence, then update the smallest useful knowledge node(s). A good absorption pass makes the vault easier to query top-down:

```text
Knowledge node -> child knowledge node -> source extensions -> source note
Bridge -> endpoint knowledge nodes -> source evidence
```

Use Chinese as the main writing language. Preserve paper titles, repository names, protocols, APIs, code symbols, file paths, URLs, identifiers, and canonical English technical terms when they are retrieval keys.

Every durable note must be independently readable:

- Source notes must be detailed enough that future agents can answer ordinary questions about the paper/repo/webpage without reopening the raw artifact.
- Knowledge notes must completely explain their concept/direction/problem/method within the note. They may link to prerequisite knowledge, but they must still include a concise local definition and boundary explanation.
- Bridge notes must fully explain the relationship, endpoint scopes, transfer matrix, non-transfer boundary, evidence, and maturity. Endpoint links are references, not substitutes for explanation.

Do not create a knowledge node that requires the reader to open two other notes before the concept itself becomes understandable.

## Inputs

Accept:

- Paper reading notes under `03_Sources/papers/`.
- GitHub repository analysis/source notes under `03_Sources/github/`.
- Web research/source notes under `03_Sources/web/`.
- Daily freshness notes or reports.
- Existing Nahida source notes that still need first-time absorption.
- Existing legacy notes only when the task is explicitly migration/consolidation-like; otherwise use `nahida-consolidate`.

If the user asks to optimize existing notes without rereading PDFs/repos/web pages, use `nahida-consolidate` first. If a paper/repository/web item has not yet been read into a source note, route through `nahida-update` and the appropriate source skill first.

## Source Readiness Gate

Before durable absorption, classify each source:

- `ready_for_absorption`: detailed source note exists, evidence anchors are clear, and deep reading/deep repo read is adequate for the stated scope.
- `scoped_partial`: source note is useful but limited; downstream knowledge must be marked `seed`, `tentative`, or `review`.
- `not_ready`: metadata-only, abstract-only, README-only, extraction gap, unverified news, or queued source. Update indexes/review queues only; do not produce confident knowledge.

Papers and repositories require deep reading before they can support confident durable knowledge:

- Paper source notes should have `reading_depth: deep_read` and a suitable `reading_status`, or explicitly state scoped coverage and limitations.
- Repository source notes should have `analysis_depth: deep_repo_read` and a suitable `analysis_status`, or explicitly state scoped coverage and skipped modules.

## Hierarchy Classification

Every absorbed source must be placed into a bounded recursive path:

```text
domain / direction / problem-or-topic / optional-subproblem-or-method
```

Use this sequence:

1. Resolve L1 `domain_id`: independent field, such as `blockchain-systems`, `zero-knowledge-proofs`, `ai-agents`, `ml-systems`, or `ai-safety-and-evaluation`.
2. Resolve L2 `direction_id`: stable direction inside the domain, such as `consensus`, `proof-systems`, `polynomial-commitments`, `agent-memory`, or `multi-agent-orchestration`.
3. Resolve L3 `topic_ids`: reusable problem, mechanism family, method family, application cluster, or evaluation axis, such as `byzantine-fault-tolerance`, `kzg-commitments`, `folding-schemes`, or `episodic-memory`.
4. Consider L4 knowledge children only when the split gate passes. A source itself is not a knowledge child; it remains under `03_Sources/`.

Broad labels are not final placements. `AI`, `Blockchain`, and `ZKP` are parent hints. For example, a Raft/SRaft source should be classified toward `blockchain-systems or distributed-systems -> consensus -> crash-fault-tolerance`, not turned into an isolated top-level node.

If placement is uncertain, set `classification_status: review`, record alternatives and evidence, and avoid settled upper-layer claims.

## Cold-Start Hierarchy Discovery

When source notes reveal a useful area but the vault has no usable parent hierarchy, infer a parent-first structure before writing durable nodes. Use only source note content, existing vault notes, and explicitly allowed update/research context:

```text
research field/domain -> direction -> research problem or method family -> optional subproblem/method -> source instance
```

Extract and record these facets:

| Facet | Meaning | Durable handling |
| --- | --- | --- |
| Research field/domain | Independent field or practice area, not just a keyword | domain seed or review |
| Research background | Why the area exists, historical/practical motivation, constraints | background section in nearest node |
| Research problem | Reusable problem or task, not a paper title | problem node or parent section |
| Foundation concepts | Broad prerequisites such as CFT, BFT, zk-SNARKs, polynomial commitments | foundation node, foundation_thin, or foundation_gap |
| Method family | Protocol/model/proof/system/architecture family | method node or method section |
| Application/evaluation context | Applications, benchmarks, datasets, deployments, metrics | application/evaluation node or section |
| Source instance | Paper/repo/system/protocol instance/module/benchmark/release | source extension, representative source, alias, or review |

Correct examples:

| Source cue | Correct path | Wrong path |
| --- | --- | --- |
| SRaft/Raft variant in blockchain setting | `blockchain-systems or distributed-systems -> consensus -> crash-fault-tolerance`; SRaft/Raft as source instance | `SRaft` as domain/direction/foundation |
| Groth16 paper or repo | `zero-knowledge-proofs -> proof-systems -> zk-SNARKs`; Groth16 as representative instance | `Groth16` as the foundation of ZKP |
| KZG paper/source | `zero-knowledge-proofs -> polynomial-commitments -> kzg-commitments` when reusable; otherwise parent section plus source extension | only a paper summary with no reusable commitment concept |

The test is retrieval cost. A new node should let future agents answer or summarize by reading fewer source notes, and should make the update scope for a field/direction/problem clearer. If it does not, do not create a standalone node.

## Domain Research Dynamics

Each active L1 domain should have one living domain dynamics note:

```text
04_Knowledge/<domain>/research-dynamics.md
```

Use `vault/00_System/templates/domain_research_dynamics.md` when creating it. The note is a domain-level synthesis of latest recorded research dynamics, academic focus, industrial/practice focus, emerging topics, open problems, and directional tendencies.

When absorbing sources, evaluate the affected domain dynamics note:

- Create it when a domain node becomes active and the note is missing.
- Refresh it when new absorbed sources change domain-level priorities, active research questions, industrial practice, open problems, emerging terms, or freshness.
- Keep it unchanged when the source only adds a narrow delta to a child problem/method.
- Mark or queue it when freshness has expired but the current run lacks enough evidence to refresh.

The domain dynamics note must cite lower source/knowledge/bridge notes and use evidence windows. Do not use model memory as "latest".

## Knowledge Node Split Gate

Create a new `04_Knowledge/` node only when all checks pass:

- The candidate is an independent, reusable research/practice problem, method family, application area, or evaluation axis.
- It is useful beyond one source, or the single source is canonical/foundational enough to justify a seed node.
- It has a clear parent and clear boundaries.
- It improves retrieval or maintenance compared with keeping the content as a section in the parent node.
- It is likely to collect multiple sources, repeated questions, bridge endpoints, daily signals, or future updates.

If the candidate fails, keep it as one of:

- source-extension row,
- evidence paragraph,
- representative-source entry,
- alias/query key,
- watchlist item,
- review item.

Do not create knowledge nodes for one-off experiments, one repository module, local implementation tricks, single benchmark results, artifact-specific terms, or shallow hot terms.

## Foundation Concept Gate And Examples

Foundational knowledge nodes are broad, reusable prerequisites or method families. They should not be merely "what a paper proposes." Before creating/updating a foundational node, ask whether the concept is needed across multiple sources, subtopics, or future queries.

Correct vs incorrect:

| Candidate | Correct handling | Incorrect handling |
| --- | --- | --- |
| `CFT` / `Crash-Fault Tolerance` | Create/update a complete knowledge node under consensus; explain fault model, guarantees, limits, relation to Raft/Paxos-like protocols, and representative sources. | Create `Raft` as the foundation and leave CFT undefined. |
| `BFT` / `Byzantine Fault Tolerance` | Create/update a complete consensus knowledge node; PBFT/Tendermint/HotStuff-like systems are representatives or child instances. | Let one PBFT paper define the whole BFT direction. |
| `Raft` | Treat as protocol instance, representative source, or source extension under CFT/consensus unless repeated user need justifies a scoped instance node. | Promote Raft as an independent foundational concept from one paper. |
| `zk-SNARKs` | Create/update a complete foundational proof-system knowledge node; explain succinctness, non-interactivity, arguments, setup assumptions, prover/verifier roles, applications, and major families. | Force readers to infer zk-SNARKs from Groth16 or one application paper. |
| `Groth16` | Treat as representative proving system/protocol instance under zk-SNARKs; split only with enough sources or repeated queries. | Treat Groth16 as the foundation of zk-SNARKs. |
| `KZG commitments` | Create/update knowledge node when evidence spans polynomial commitments, SNARKs, data availability, or multiple sources. | Record only the KZG paper contribution without explaining KZG's reusable role. |

If a source mentions an important foundation that the vault lacks, create a `foundation_missing` or `foundation_thin` knowledge node and run/queue focused foundation research rather than pretending the paper invented the concept.

## Foundation Policy

Before creating or upgrading a knowledge node, judge its foundation status:

- `foundation_ready`: the node already has useful definitions, prerequisites, background, method families, boundaries, representative sources, and gaps.
- `foundation_thin`: there are source notes or short explanations, but no durable foundation.
- `foundation_missing`: the parent domain/direction/problem is absent or too thin to support the update.

When foundation is thin or missing:

1. Use Codex/model-prior knowledge only to outline what must be explained; label it as `model_prior_background` or `tentative` unless source-backed.
2. Use or queue `nahida-research-search` with `foundation_pack` when stable external grounding is needed. Web supplementation is allowed in update/research/knowledge-get mode when the user has authorized knowledge updating, but not in query mode.
3. Create a `seed` or `foundation_thin` knowledge node with explicit gaps when the parent should be visible immediately.
4. Attach the incoming source as a source extension, not as the whole node.

## Required Procedure

1. Read context:
   - Read relevant source notes and existing `04_Knowledge/`, `05_Bridges/`, generated indexes, ledgers, review queues, and legacy notes when needed.
   - Do not reopen raw PDFs, reclone repositories, browse the web, or fetch external metadata unless the user explicitly switches to update/research mode.
2. Check readiness:
   - Mark each source as `ready_for_absorption`, `scoped_partial`, or `not_ready`.
   - If not ready, write only index/review/queue updates.
3. Discover cold-start hierarchy when needed:
   - Extract research field/domain, background, research problem, foundation concepts, method family, application/evaluation context, and source instance.
   - Separate reusable layers from paper/repo/web-specific instances.
   - Record retrieval benefit and update scope for each proposed node/section.
4. Classify hierarchy:
   - Resolve domain, direction, topic/problem, optional subproblem/method.
   - Record alternatives, evidence, confidence, and review status.
5. Materialize knowledge path:
   - Select existing target knowledge nodes or propose new ones parent-first.
   - Use path-safe slugs. Keep logical paths in frontmatter; do not move source notes because classification changed.
6. Run promotion gate:
   - Classify source-derived candidates as `knowledge_node`, `knowledge_section`, `source_extension`, `bridge_candidate`, `alias_query_key`, `watchlist_item`, `review_only`, or `not_promotable`.
   - Create/update standalone knowledge nodes only if the split gate passes.
7. Update knowledge nodes:
   - Patch managed sections only: `定义与范围`, `背景`, `解决的问题`, `上层位置`, `下级结构`, `方法族与解决路线`, `代表 Sources`, `当前综合`, `Source Extensions`, `Bridge Links`, `关系图谱`, `缺口与队列`, `更新记录`.
   - Keep knowledge nodes organized by reusable structure, not by a single paper/repo.
   - If a node's `valid_until` is still fresh and the new source does not materially change it, add a small source-extension/update row instead of rewriting the whole node.
8. Update domain dynamics:
   - For each affected L1 domain, create/refresh/mark stale/queue `04_Knowledge/<domain>/research-dynamics.md`.
   - Include academic focus, industrial focus, emerging topics, open problems, trend judgment, evidence window, and refresh triggers.
   - Skip rewriting when the source does not change domain-level movement; record `unchanged`.
9. Extract relation edges:
   - Create candidate edges such as `is_a`, `instance_of`, `part_of`, `has_child`, `depends_on`, `contrasts_with`, `applies_to`, `used_in`, `implements`, `implemented_by`, `bridges_to`, and `evidenced_by`.
   - Promote only `active` or `active_seed` edges into knowledge nodes and generated indexes.
   - Put weak, broad, or ontology-changing edges into review queues.
10. Detect bridges:
   - Create or update a bridge only when at least two endpoint knowledge paths and a typed relation exist.
   - Prefer specific topic/problem endpoints over broad domain endpoints.
   - Required bridge fields: endpoint knowledge refs, endpoint paths, relation types, relationship thesis, transfer matrix, non-transfer boundary, source evidence, maturity, refresh triggers.
   - Store new durable bridges under `05_Bridges/` with path-safe filenames. Read old `06_Bridges/` only as legacy context.
11. Update generated support:
   - Append indexes, ledgers, query keys, freshness markers, and review queue items as rebuildable support.
   - Record every created/updated note path and every skipped/queued item.

## Output Contract

A knowledge absorption report must include:

- `Input Set`: source notes processed and source refs.
- `Source Readiness`: readiness status, coverage, gaps, absorption decision.
- `Cold-Start Hierarchy Discovery`: research field/domain, background, research problem, foundation concepts, method family, application/evaluation context, source instance, evidence, confidence, and handling.
- `Hierarchy Classification`: domain, direction, topic/problem, optional method/subproblem, alternatives, evidence, confidence.
- `Retrieval Optimization`: future query types helped, source notes avoided, summary/update benefit, create/merge/section/source-only decision, reason.
- `Knowledge Path`: target `04_Knowledge/` path(s), missing parent nodes, split-gate decisions.
- `Promotion Decisions`: candidate, generality class, target handling, reason.
- `Knowledge Updates`: nodes created/updated/skipped, sections patched, source-extension rows, freshness status, valid-until.
- `Domain Dynamics`: created/refreshed/stale/unchanged/queued domain dynamics notes, evidence window, academic focus, industrial focus, emerging topics, open problems, and refresh triggers.
- `Bridge Updates`: bridge candidates/notes, endpoint knowledge nodes, relation types, transfer boundary, evidence.
- `Relation Extraction`: candidate/promoted/pending/review/rejected edges.
- `Foundation Gaps`: missing background, needed searches, representative papers/repos to add.
- `Expansion Candidates`: bounded child directions/problems, adjacent nodes, watch terms, future source tasks.
- `Index/Ledger Updates`: generated files touched or intentionally skipped.
- `Review Queue`: uncertain taxonomy, weak evidence, risky migration, stale legacy notes.
- `Capability Usage`: Obsidian skills, Bases, Canvas, CodeGraph, web/search, or fallbacks used.

## Quality Gate

Before finishing, verify:

- No routine new note was written to legacy `04_Claims/`, `05_Concepts/`, `06_Bridges/`, `07_Maps/`, `08_Projects/`, or `09_Syntheses/`.
- Every durable knowledge update cites source notes or marks background as `model_prior_background`/`tentative`.
- Source-specific details stayed in source notes or source-extension rows.
- New/updated knowledge nodes identify retrieval role and update scope, or the material stayed in a parent section/source extension.
- Active L1 domains have a domain dynamics note or a recorded reason/queue item.
- Every new knowledge node passed the split gate or is explicitly marked `seed`/`review`.
- Every bridge has endpoint knowledge refs, relation types, evidence, and transfer limits.
- Important parent/child/application relations were written as relation edges or queued for review.
- Generated filenames are path-safe and did not create unintended nested directories.
- The report names changed files and unresolved items.

## Boundaries

- May write `04_Knowledge/`, `05_Bridges/`, generated indexes, ledgers, reports, and review queues.
- May read legacy lanes for migration context.
- Must not edit raw artifacts or source identity fields.
- Must not delete, rename, merge, retire, or bulk migrate legacy notes without explicit confirmation.
