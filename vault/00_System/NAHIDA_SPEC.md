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

## Path Safety Contract

Distinguish display titles, stable IDs, and filesystem paths:

- `title` may preserve the human-facing title exactly, including specialist punctuation such as `AI/ML`, `C++`, `ZK/ML`, or `owner/repo`.
- File names and generated path segments must use a path-safe slug. Never write raw titles directly into file paths.
- Path-safe slugs must not contain `/`, `\`, NUL, control characters, `:`, `*`, `?`, `"`, `<`, `>`, `|`, leading/trailing spaces, or trailing dots.
- Replace separators and punctuation with a stable ASCII slug: lower-case where practical, collapse whitespace/punctuation to `-`, trim repeated `-`, and keep important retrieval tokens. For example `AI/ML x Zero-Knowledge Proofs` should become a filename like `ai-ml-x-zero-knowledge-proofs.md`, while `title` remains `AI/ML x Zero-Knowledge Proofs`.
- For GitHub `owner/repo`, DOI strings, URLs, and bridge titles, preserve the canonical value in frontmatter fields such as `title`, `canonical_url`, `project_id`, `doi`, `aliases`, or `original_title`; use a sanitized slug for the path.
- Wikilinks may use path-safe note names with display aliases, for example a link whose target is `ai-ml-x-zero-knowledge-proofs` and whose display alias is `AI/ML x Zero-Knowledge Proofs`.
- After writing any managed note, verify the final file landed in the intended type lane and did not create unintended nested directories because of a raw `/`.

## Language Contract

- Nahida notes should be written primarily in Chinese.
- Keep canonical technical terms, paper titles, project names, protocol names, API names, code symbols, file paths, identifiers, URLs, and quoted source titles in their original language when precision matters.
- For important English terms, prefer Chinese explanation plus the English term in parentheses on first use, for example `长期记忆（long-term memory）`.
- Do not force awkward translations of specialist terms if the English term is the standard search/retrieval key.
- Source metadata fields may preserve original-language values; analysis, synthesis, conclusions, review notes, and handoff tasks should be Chinese-first.
- When a source is English, summarize and synthesize in Chinese while preserving exact English terminology needed for retrieval.

## Capability Contract

Nahida should use existing Codex skills, plugins, connectors, and Obsidian-native formats before falling back to ad hoc file handling. Every substantial run should record which capabilities were used and which were missing.

Hard prerequisites for full-fidelity Nahida work:

- `obsidian-markdown` - required for Obsidian-flavored Markdown, YAML properties, wikilinks, embeds, callouts, tags, and note rendering discipline.
- `obsidian-note` - required for vault-ready note sets, living maps, source-backed research notes, wikilinks, and Obsidian knowledge graph organization.
- `nahida-update` and `nahida-query` - preferred user-facing entry points.
- `nahida-consolidate` - preferred maintenance entry point when existing notes should be judged for upper-layer integration, refresh, schema repair, or no-op handling without rereading raw PDFs, repositories, or web sources.

Preferred capabilities when the task calls for them:

- `obsidian-bases` - use for `.base` files, table/card/list views, filters, formulas, dashboards, and database-like browsing of sources, knowledge nodes, bridges, queues, or freshness records.
- `json-canvas` - use for `.canvas` visual knowledge graphs, direction graphs, source-to-knowledge relationship maps, and cross-domain bridge diagrams.
- CodeGraph - use for local repository architecture, symbol, module, and call-flow analysis.
- GitHub plugin/connector or `gh` - use for GitHub repository context when available and relevant.
- Codex bundled workspace dependencies via `load_workspace_dependencies` - use for PDFs, documents, sheets, slides, and other local document processing.
- Web search/browser capabilities - use for explicit update, research, freshness, or source-verification tasks; prefer primary sources. Do not use them from `nahida-query` unless the user explicitly switches from query to update/research mode.

If a hard prerequisite is unavailable and the task depends on it, stop and report a `prerequisite_gap` instead of silently producing lower-quality output. If a preferred capability is unavailable, continue with a recorded fallback only when the result remains trustworthy.

## Canonical Topology

New managed writes use the sequential Source -> Knowledge -> Bridge topology:

```text
00_System/
  bases/
01_Inbox/
02_Raw/
03_Sources/
04_Knowledge/
05_Bridges/
90_Generated/
99_Archive/
```

Legacy lanes may still exist in older vaults, but new skills must not use them as primary write targets:

```text
04_Claims/      legacy atomic assertion lane; read-only except explicit migration/audit
05_Concepts/    legacy concept lane; consolidate into 04_Knowledge
06_Bridges/     legacy bridge lane; consolidate into 05_Bridges
07_Maps/        legacy map lane; consolidate into 04_Knowledge nodes
08_Projects/    legacy repo-analysis lane; new repo notes live under 03_Sources/github/
09_Syntheses/   legacy synthesis lane; consolidate into synthesis sections or child notes inside 04_Knowledge
```

## Managed Zone

Automation may create or append only under these paths unless explicitly confirmed:

- `00_System/bases/` for managed Obsidian Bases views
- `01_Inbox/`
- `02_Raw/`
- `03_Sources/`
- `04_Knowledge/`
- `05_Bridges/`
- `90_Generated/`

Any user-authored path outside the managed zone is read-only by default.

Legacy lanes (`04_Claims/`, `05_Concepts/`, `06_Bridges/`, `07_Maps/`, `08_Projects/`, `09_Syntheses/`) are readable context. They may be patched only by explicit consolidation, migration, audit, or compatibility tasks and must not receive routine new source absorption output.

## Universal Properties

Every managed note should include:

```yaml
---
id: "nahida-..."
title: "..."
type: "source|knowledge|bridge|run|review_queue"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active|review|stale|retired|archived"
status: "<type-specific status>"
hierarchy_level: "global|domain|direction|problem|subproblem|method_family|application_area|source|bridge|run"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
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
- `knowledge` - a recursive domain/direction/problem/method/application node. It replaces routine `claim`, `concept`, `map`, and `synthesis` writes.
- `bridge` - explicit cross-domain or cross-problem relationship between knowledge nodes.
- `run` - automation run log.
- `review_queue` - uncertain or destructive proposals awaiting review.

Legacy note types remain readable for compatibility:

- `claim` - legacy exceptional assertion lane. Do not create new claim notes during routine absorption.
- `concept` - legacy concept lane. Consolidate useful content into `knowledge` nodes.
- `map` - legacy navigation lane. Consolidate useful content into `knowledge` nodes.
- `project` - legacy repository analysis lane. New repository analysis is a `source` note under `03_Sources/github/`.
- `synthesis` - legacy upper memory lane. New synthesis lives inside a `knowledge` node or as a child `knowledge` note when the split gate passes.

## Source + Knowledge + Bridge Model

Nahida's current memory model is deliberately small:

- `03_Sources/` stores complete external evidence notes: papers, GitHub repositories, web pages/research notes, daily freshness signals, datasets, documents, and local PDF-derived notes. Source notes are bottom-layer memory and should be detailed enough to answer ordinary questions about that source without reopening the raw artifact.
- `04_Knowledge/` stores recursive knowledge nodes. A node is a stable field, research direction, problem, subproblem, method family, evaluation axis, application area, or reusable practice layer. It contains definitions, background, solved problems, child nodes, solution routes, representative sources, current synthesis, gaps, and update history.
- `05_Bridges/` stores only cross-node relationships. Bridges connect two or more knowledge nodes and explain typed relations such as application, dependency, analogy, tension, translation, shared pattern, co-evolution, evaluation transfer, or implementation reuse. Bridge background references endpoint knowledge nodes and cites source evidence; it does not replace endpoint knowledge.

Routine writes must not create new `04_Claims/`, `05_Concepts/`, `07_Maps/`, `08_Projects/`, or `09_Syntheses/` notes. If older skill wording mentions claims, concepts, maps, projects, or syntheses, interpret it as legacy compatibility and normalize the durable output into `04_Knowledge/` plus `05_Bridges/`.

### Retrieval-Optimized Hierarchy Goal

Nahida's hierarchy exists to reduce future reading, not to decorate notes with labels. A good hierarchy lets `nahida-query` answer by reading the smallest useful set of notes:

```text
domain knowledge -> direction knowledge -> problem/method knowledge -> bridge if needed -> selected source notes
```

Every durable knowledge node should be a retrieval filter:

- It explains what belongs under the node and what does not.
- It points to the smaller child nodes and representative sources that matter.
- It lets a future agent summarize or refresh a domain/direction without rereading every source.
- It lets a future agent answer "latest progress / current focus / open problems" for a domain from one domain dynamics note before opening lower notes.
- It supports narrow queries by steering the agent to a few precise notes instead of scanning all papers/repos/web notes.

If a proposed hierarchy node does not reduce future retrieval cost, does not clarify update scope, or merely mirrors one source's title, do not create it as a standalone node.

### Domain Research Dynamics Notes

Every active L1 domain, the largest `knowledge` node for an independent problem field, should have one living domain dynamics note:

```text
04_Knowledge/<domain>/research-dynamics.md
```

This note is the first stop for questions such as:

- "这个领域最近有哪些研究进展?"
- "现在学术界更关注什么?"
- "工业界/开源实践更关注什么?"
- "还有哪些关键待解决问题?"
- "这个领域下一步可能往哪里走?"

It is not a source note and not a pile of paper summaries. It is a source-backed, time-windowed analysis of a whole domain's movement. It should synthesize lower-layer `03_Sources/` notes, domain/direction/problem knowledge nodes, bridge notes, daily reports, and watchlists.

Required scope:

- `研究动态摘要`: what changed in the evidence window.
- `学术关注`: papers, methods, benchmarks, evaluation axes, theoretical questions, and unresolved academic problems receiving attention.
- `工业/工程关注`: repositories, implementations, standards, production constraints, tooling, performance, security, UX, cost, and adoption signals.
- `新兴方向与热词`: emerging terms, repeated freshness signals, and whether they are durable, tentative, or hype-only.
- `待解决问题`: open problems grouped by foundation gap, method limitation, evaluation gap, implementation gap, safety/security gap, or adoption gap.
- `方向倾向判断`: careful synthesis of where the field appears to be moving, with evidence and uncertainty.
- `刷新触发器`: which new sources, daily signals, or stale dates should refresh the note.

Freshness:

- Default freshness window is 30 days for fast-moving domains, 60-90 days for slower domains.
- Use `evidence_window_start`, `evidence_window_end`, `last_synthesized`, `valid_until`, and `freshness_status`.
- If `valid_until` has expired, `nahida-query` may still use the note as historical context but must report it as stale.

Creation and refresh rules:

- When a domain node is created or first becomes active, create or queue its `research-dynamics.md`.
- When `nahida-daily-fetch` finds repeated high-quality signals for a domain, refresh or queue the dynamics note.
- When `nahida-knowledge-get` absorbs a source that changes a domain's priorities, open problems, representative directions, or academic/industrial focus, refresh the affected domain dynamics note.
- When only one source adds a narrow detail, add a small source-extension row to the relevant problem/direction and queue dynamics refresh only if it changes domain-level movement.
- Do not infer "latest" from model memory. Update/research/daily modes may use web; query mode stays vault-only.

### Cold-Start Hierarchy Discovery

When the vault has no useful hierarchy for an incoming source, the agent must infer a provisional hierarchy from metadata and source content before writing durable knowledge. Do not wait for the user to name every layer.

Run a cold-start discovery pass from:

- paper metadata: title, abstract, keywords, venue, introduction, problem statement, related work, method names, evaluation setup, conclusion;
- repository metadata: README, docs, package manifests, module names, examples, tests, APIs, primary flows, dependency ecosystem;
- web metadata: title, URL, author/org, headings, definitions, examples, source type, publication/update date;
- existing vault hints: source notes, aliases, review queues, watchlists, previous query gaps, legacy notes, generated indexes.

Extract these hierarchy candidates:

| Facet | Question | Examples |
| --- | --- | --- |
| Research field/domain | What broad field owns the vocabulary and maintenance cadence? | `blockchain-systems`, `zero-knowledge-proofs`, `ai-agents`, `ml-systems` |
| Research background | What prior context must exist for the source to make sense? | distributed consensus, proof systems, agent memory, verifiable computation |
| Research problem | What durable problem is being solved? | fault-tolerant agreement, succinct verification, long-term memory retrieval |
| Foundation concepts | Which reusable prerequisites should have complete notes? | CFT, BFT, consensus, zk-SNARKs, polynomial commitments |
| Method family | What general solution family is used? | state-machine replication, polynomial commitments, folding schemes, retrieval-augmented memory |
| Application/evaluation context | Where is the problem used or evaluated? | permissioned blockchain, data availability, zkML, coding agents |
| Artifact/instance | What is the specific paper/protocol/repo/system? | Raft, PBFT, Groth16, Nova, a GitHub repo |

The cold-start output must separate reusable layers from source instances:

```text
research field -> direction -> research problem/method family -> source instance
```

Correct:

```text
SRaft paper metadata
  field: blockchain-systems or distributed-systems
  direction: consensus
  research problem: crash-fault-tolerant consensus in permissioned blockchain settings
  foundation concepts: consensus, CFT, state-machine replication
  source instance: SRaft/Raft variant
```

Incorrect:

```text
SRaft paper metadata
  field: SRaft
  direction: SRaft
  concept: SRaft
```

Correct:

```text
Groth16-related paper/repo
  field: zero-knowledge-proofs
  direction: proof-systems
  research problem: succinct non-interactive arguments
  foundation concepts: zk-SNARKs, arithmetization, polynomial commitments
  source/protocol instance: Groth16
```

Incorrect:

```text
Groth16-related paper/repo
  foundation concept: Groth16
  zk-SNARKs: omitted because the source did not explain it fully
```

When confidence is low, create review candidates rather than brittle settled nodes. But even a review candidate should name the likely field, background, problem, foundation concepts, method family, and source instance so future agents can continue the structure.

### Knowledge Node Recursion

`knowledge` nodes form a bounded recursive tree. The tree is logical first and filesystem second.

Canonical path shape:

```text
04_Knowledge/<domain>/index.md
04_Knowledge/<domain>/<direction>/index.md
04_Knowledge/<domain>/<direction>/<problem-or-topic>.md
04_Knowledge/<domain>/<direction>/<problem-or-topic>/<subproblem-or-method>.md
```

Depth rules:

- `L1 domain`: independent broad field with its own vocabulary, foundations, applications, and maintenance cadence, such as `blockchain-systems`, `zero-knowledge-proofs`, `ai-agents`, or `ml-systems`.
- `L2 direction`: stable research/practice direction inside one domain, such as `consensus`, `proof-systems`, `polynomial-commitments`, `agent-memory`, or `multi-agent-orchestration`.
- `L3 problem/topic`: reusable problem, mechanism family, method family, evaluation axis, protocol family, or application cluster inside a direction, such as `byzantine-fault-tolerance`, `kzg-commitments`, `folding-schemes`, or `episodic-memory`.
- `L4 subproblem/method/application`: create only when the split gate passes. A paper, repository, webpage, dataset, benchmark, or news item is not an L4 knowledge child; it remains a source note linked as evidence.

### Knowledge Node Split Gate

Create a new knowledge node only when all required checks pass:

- It is an independent, reusable research/practice problem, method family, application area, or evaluation axis.
- It is useful beyond one source, or the single source is canonical/foundational enough to justify a seed node.
- It has a clear parent, clear boundaries, and specialist-readable terminology.
- It improves retrieval or maintenance compared with keeping the content as a section in the parent node.
- It is likely to collect multiple sources, repeated questions, bridge endpoints, or daily freshness signals.

Do not create a new node for a one-off experiment, artifact-specific optimization, single repository module, benchmark result, local theorem detail, paper-specific mechanism name, or passing news term. Keep those as source-extension rows, evidence paragraphs, aliases, watchlist items, or review items inside the nearest knowledge node.

### Knowledge Node Content Contract

Each durable `knowledge` note should contain:

- `定义与范围`: what the node means, what it excludes, and canonical aliases.
- `背景`: prerequisite concepts and historical/contextual motivation. Model-prior background must be labeled when not source-backed.
- `解决的问题`: the durable problem or need this node addresses.
- `上层位置`: parent domain/direction/problem and relation edges.
- `下级结构`: child problems, method families, application areas, and when they should be split.
- `方法族/解决路线`: major solution approaches and tradeoffs.
- `代表 Sources`: papers, repositories, web/foundation notes, daily signals, datasets, or standards with concise deltas.
- `当前综合`: current integrated understanding, evidence window, freshness status, and validity period.
- `Source Extensions`: what newly added sources changed, refined, contradicted, or failed to cover.
- `Bridge Links`: links to `05_Bridges/` for cross-node relations.
- `缺口与队列`: missing foundations, weak evidence, stale areas, papers/repos/searches to run next.
- `更新记录`: material changes with run IDs and source refs.

Knowledge nodes may be large enough to be useful. Split them only when a child node passes the split gate.

### Standalone Note Completeness

Every durable note must be useful as a standalone memory object:

- A `source` note is the complete local memory of one external source. It must contain identity, scope, reading/analysis coverage, important details, evidence anchors, limitations, and handoff candidates. Do not use a source note as a thin pointer to a PDF, repository, or webpage.
- A `knowledge` note is the complete local explanation of one concept, direction, problem, method family, or application area. A reader should understand the node's definition, background, solved problem, boundaries, key approaches, representative sources, gaps, and current synthesis from that note alone.
- A `bridge` note is the complete local explanation of one cross-node relationship. It must name endpoint knowledge nodes, relation type, thesis, transfer matrix, non-transfer boundary, evidence, maturity, and refresh triggers.

Links are allowed and encouraged, but they must not make a concept incomplete. If a knowledge note relies on another foundational concept, include a concise local definition and a precise link to the complete concept note. Do not write "see X" as the only explanation. The linked note may contain the full deep treatment; the current note must still be readable.

### Foundation Concept Gate

Foundational concepts are broad, reusable prerequisites or method families. They are not just names introduced by one paper, protocol, implementation, or repository.

Create or refresh a foundational `knowledge` node when the candidate is:

- widely used across multiple papers, repositories, standards, or subtopics;
- needed to understand many downstream notes;
- a stable problem, model, fault class, proof-system family, evaluation axis, or method family;
- useful as a query entry point even when no single source is being discussed.

Do not label a paper-specific system, one protocol instance, benchmark result, implementation trick, or named artifact as a foundational concept. It may still appear as a source extension, representative source, variant, protocol instance, or review candidate.

Examples:

| Candidate | Correct handling | Incorrect handling |
| --- | --- | --- |
| `Crash-Fault Tolerance (CFT)` | Foundational knowledge node under `blockchain-systems or distributed-systems / consensus`; explain fault model, problem, guarantees, typical protocols, relation to Raft/Paxos, limits. | Treat `Raft` as the foundation and leave CFT undefined. |
| `Byzantine Fault Tolerance (BFT)` | Foundational knowledge node under consensus; explain Byzantine model, quorum intuition, SMR, safety/liveness, PBFT/Tendermint/HotStuff-like representatives. | Create one source-centered BFT page for PBFT only. |
| `Raft` | Representative protocol/source extension or protocol-instance node only when useful; link to CFT/consensus. | Create a top-level foundational concept just because a Raft or SRaft paper was read. |
| `zk-SNARKs` | Foundational knowledge node under zero-knowledge proofs/proof systems; explain succinctness, non-interactivity, arguments, setup assumptions, prover/verifier roles, applications, major families. | Force readers to infer zk-SNARK meaning from a single Groth16 or application paper. |
| `Groth16` | Representative proving system/protocol instance or method-family section under zk-SNARKs; split only if many sources or repeated queries justify it. | Treat Groth16 as the foundation of all zk-SNARKs or create a standalone foundation note from one paper. |
| `KZG commitments` | Knowledge node when used across polynomial commitments, SNARKs, data availability, or many sources; explain pairing setting, commitment/opening intuition, trusted setup, limits. | Only record the KZG paper's contribution without explaining polynomial commitments or KZG's reusable role. |

### Correct And Incorrect Output Shapes

Correct:

```text
03_Sources/papers/<raft-paper>.md
  Detailed paper memory.

04_Knowledge/blockchain-systems/consensus/index.md
  Complete consensus direction note.

04_Knowledge/blockchain-systems/consensus/crash-fault-tolerance.md
  Complete CFT note; Raft/SRaft appear as representative source extensions.
```

Incorrect:

```text
04_Knowledge/raft.md
  Mostly a summary of one paper.
  CFT/consensus definitions missing or delegated elsewhere.
```

Correct:

```text
04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md
  Complete zk-SNARK concept/method-family note.

04_Knowledge/zero-knowledge-proofs/proof-systems/groth16.md
  Optional protocol-instance node only if justified; otherwise a section/source extension under zk-SNARKs.
```

Incorrect:

```text
04_Knowledge/zero-knowledge-proofs/proof-systems/groth16.md
  Used as the only explanation of zk-SNARKs.
  Reader must open a paper note to understand the foundational concept.
```

### Web Supplement Policy

During `nahida-update`, `nahida-research-search`, `nahida-daily-fetch`, and `nahida-knowledge-get`, Nahida may use web research to fill missing foundations, verify current metadata, or improve a knowledge node, when the task authorizes updating/researching. Prefer primary, canonical, official, survey, textbook, standard, or well-maintained technical sources for foundations.

During `nahida-query`, Nahida must not browse or fetch external material. Query answers are vault-only. If the needed foundation or latest evidence is absent, say the knowledge base lacks it and propose an update action.

## Legacy Compatibility Notes

The sections below this heading preserve older Nahida design language so existing notes can be interpreted and migrated. They are not the current write contract. When any statement below conflicts with the `Source + Knowledge + Bridge Model`, the current model wins:

- source notes stay under `03_Sources/`;
- upper memory is written to `04_Knowledge/`;
- cross-node relations are written to `05_Bridges/`;
- legacy lanes are read-only compatibility context unless a consolidation/migration/audit task explicitly targets them.

### Legacy Layered Memory Model

Nahida is a layered memory system, not a flat pile of summaries.

The bottom skills are source adapters and incremental updaters. `nahida-paper-read`, `nahida-github-repo-analyze`, `nahida-research-search`, and `nahida-daily-fetch` produce or queue lower-layer evidence. They do not, by themselves, define the knowledge base. The knowledge base is built by repeatedly integrating those increments into higher memory layers through `nahida-update` and `nahida-knowledge-get`, then using `nahida-consolidate` to decide whether existing notes need upper-layer refresh, metadata repair, bridge cleanup, review queueing, or no-op handling without rereading raw sources.

Layers:

- `L0 Raw/Staging`: raw inputs, extraction snippets, inventories, queues, and ledgers. These are operational artifacts, not knowledge.
- `03_Sources/` - high-quality source notes from papers, web, PDFs, datasets, and source documents.
- `03_Sources/github/` - current lane for high-quality repository/project analysis notes; legacy `08_Projects/` may be read as old context.
- `04_Knowledge/` - current lane for reusable assertions, concepts, maps, syntheses, foundation concepts, directions, problems, and method families.
- `05_Bridges/` - current lane for explicit relationships between knowledge nodes; legacy `06_Bridges/` may be read as old context.
- Legacy `04_Claims/`, `05_Concepts/`, `07_Maps/`, and `09_Syntheses/` are compatibility inputs only. Consolidate their useful content into `04_Knowledge/` or `05_Bridges/` rather than creating new routine notes there.
- Domain, direction, topic, and synthesis memory should now be represented as knowledge nodes and managed sections under `04_Knowledge/`, not as new map/synthesis files.
- `90_Generated/reports/queries/` - query memory and retrieval cache, not truth.

Every source-producing skill should create a standalone lower-layer note that is precise, detailed, human-readable, and useful without opening the synthesis layer. A paper note keeps the paper's problem, method, innovation, evidence, limitations, and terminology; a repository note keeps the repository's problem, architecture, flows, modules, APIs, implementation patterns, and limitations; a web/source note keeps the page's definitions, evidence, scope, and caveats. Every `nahida-knowledge-get` pass should update or create upper-layer synthesis only after reading the relevant lower-layer notes and preserving evidence links.

Upper-layer notes should have enough capacity to organize many lower-layer notes. They should not be source-centric unless the source is genuinely foundational. A single paper or repository can be richly recorded at the lower layer, but upper layers should usually absorb it as a delta: what changed in a concept, direction, application, trend, gap, representative-material list, or bridge.

Lower-layer source notes and foundation knowledge notes are both first-class anchors, but they are not the same lane. `03_Sources/` contains external artifacts: papers, webpages, PDFs, datasets, source documents, daily signals, repository analyses, and source metadata. `04_Knowledge/` contains reusable concepts, prerequisites, protocol families, method families, problem axes, and synthesis sections. Do not place a foundation concept under `03_Sources/` just because it was learned from a paper or webpage; put the external artifact in `03_Sources/` and the concept itself in `04_Knowledge/`.

Do not treat either anchor lane merely as extraction material to be exploded into claim files or source-named upper pages. A paper, repository, web source, or daily signal remains the detailed evidence record for that external source. A foundation concept remains the detailed explanatory record in a knowledge node, with references to the sources that support it. Upper layers should promote only reusable structure and relationships: domain/direction/topic structure, problem axes, solution families, bridge relations, representative-source deltas, evaluation axes, aliases/query keys, and freshness signals. Source-specific details should usually stay inside the source note and appear in knowledge nodes only as concise source-extension rows or evidence pointers.

Before creating or refreshing any upper-layer knowledge/bridge content from a lower-layer source, run an upper-layer promotion gate:

- `foundation_concept`: reusable concept, model, protocol family, prerequisite, or evaluation axis.
- `direction_structure`: domain/direction/topic taxonomy, parent-child path, method family, or retrieval facet.
- `cross_path_relation`: typed relation between ontology paths.
- `representative_extension`: a source that is a useful example or milestone for a pack.
- `source_specific_detail`: source-local experiment, implementation detail, assumption, artifact-specific term, or one-off variant.
- `index_only`: alias, keyword, benchmark/dataset name, or watch term.
- `not_promotable`: weak, noisy, duplicate, or unsupported content.

Only the first four classes can normally create or materially refresh upper-layer notes. `source_specific_detail` should stay in the source note and may be linked from a small pack subsection when it improves retrieval. `index_only` should update aliases/query keys/watchlists. `not_promotable` should not be written except as review context.

### Legacy Meta Note Model

Nahida's bottom memory is a set of complete meta notes. A meta note is the authoritative local home for one entity:

- User-provided paper, PDF, webpage, article, dataset, or document: `03_Sources/`.
- User-provided GitHub repository or local codebase analysis: `03_Sources/github/`; legacy `08_Projects/` is read-only compatibility context.
- Foundation concept, prerequisite, standard term, protocol family, or reusable technical idea such as `zk-SNARKs`, `CFT`, `BFT`, `consensus`, `polynomial commitments`, or `verifiable computation`: `04_Knowledge/`.

Each meta note should be complete enough that ordinary questions about that entity do not require chasing many small notes. Important entity-internal facts such as a paper's innovation, a repository's architecture, a protocol's local mechanism, an experiment, a theorem sketch, or a definition used inside the source belong in that meta note's detailed sections and evidence table.

Upper-layer notes are not encyclopedic duplicates of meta notes. They organize how a problem domain is structured and how problems are solved:

```text
paper/repo/web source note -> knowledge field/problem -> method family -> representative source extension -> bridge when needed
```

Examples:

- `paper: SRaft` -> `Crash-Fault Tolerance (CFT)` -> `Consensus` -> `Blockchain systems`.
- `paper/repo: zkSNARK framework` -> `zk-SNARK frameworks` -> `zk-SNARKs` -> `Verifiable computation`.
- `knowledge: zk-SNARKs` may be produced from a focused web/foundation search when papers use the term without defining it; a narrower `zk-SNARK frameworks` node links to it while still remaining locally readable.

References should mostly express hierarchy, representative extension, evidence provenance, or cross-path bridges. Avoid making readers hop through many tiny notes to understand one source or one concept. Exceptions are allowed for genuinely reusable cross-source assertions, formal relations, contested claims, or bridge evidence that many upper notes cite.

Protocol, system, repository, benchmark, dataset, implementation, and paper-specific names are instance candidates by default, not parent concepts. A named item such as SRaft, PBFT, EPIC, Stratus, Nova, Geppetto, or a GitHub repository should normally be attached as a representative source extension under a reusable parent concept/topic pack. The preferred shape is:

```text
parent knowledge node -> problem axis -> method family -> representative solution/source extension -> source note
```

A same-name upper-layer page may exist only as a scoped knowledge/index node when useful, and should declare fields such as `node_kind: protocol_instance`, `upper_layer_handling: source_extension_index`, and `parent_knowledge_refs`. It must point readers back to the parent knowledge node as the main entry point.

Synthesis should be scoped, not shallow. Prefer a managed synthesis section or child knowledge node for one coherent domain state, direction state, research program, emerging direction, hot topic, or recurring question. Cross-direction synthesis belongs in `05_Bridges/` when it is a relationship. When the scope is too broad, split into additional knowledge nodes instead of forcing everything into one note.

Completeness means structural coverage, not pretending the vault already knows everything. Every meaningful update should leave the affected area in one of these states:

- covered by enough lower-layer evidence and an upper-layer map/synthesis,
- explicitly marked `foundation_thin`, `foundation_missing`, `stale`, or `review`,
- queued with concrete next actions for papers, repos, research search, daily fetch, or synthesis refresh.

Do not let a single incoming paper/repository become the center of the whole memory unless the user specifically asks for a source-focused reading. Source details live below; durable understanding lives above.

### Legacy Domain-First Ontology

Nahida's durable ontology is domain-first. Sources are evidence; they are not the shape of the knowledge base.

The canonical hierarchy is:

1. `L1 Domain`: an independent broad field with its own vocabulary, foundations, application surface, and maintenance cadence. Examples: `blockchain-systems`, `zero-knowledge-proofs`, `ai-agents`, `ml-systems`, `ai-safety-and-evaluation`. Avoid a single undifferentiated `AI` domain when the evidence clearly belongs to a more precise AI domain.
2. `L2 Research Direction`: a stable research/practice direction inside one domain. Examples: under blockchain systems: `consensus`, `execution`, `data-availability-and-storage`, `mempool-and-networking`, `interoperability`, `cryptoeconomics`; under ZKP: `proof-systems`, `polynomial-commitments`, `arithmetization`, `lookup-arguments`, `recursion-and-folding`, `zkvm`, `zkml`; under AI agents: `agent-memory`, `tool-use`, `multi-agent-orchestration`, `subagents`, `context-engineering`.
3. `L3 Research Topic or Content Cluster`: a focused problem, mechanism family, method class, protocol family, benchmark, implementation pattern, or application cluster inside a direction. Examples: `Crash-Fault Tolerance`, `Byzantine Fault Tolerance`, `finality gadgets`, `view change`, `KZG commitments`, `IPA commitments`, `FRI commitments`, `folding schemes`, `long-term memory stores`, `episodic memory`, `agentic workflow orchestration`.
4. `L4 Source or Project Evidence`: one paper, repository, web source, daily signal, dataset, benchmark, standard, or local document. L4 notes are detailed and reusable, but they attach to L1/L2/L3; they do not define L1/L2/L3 alone.

Rules:

- Every durable source/project note must carry `domain_id`, `direction_id`, and `topic_ids` when the evidence is sufficient. If any level is uncertain, use `classification_status: review` and write a review item instead of forcing a brittle label.
- A broad domain label is never a sufficient final placement for a source. `AI`, `Blockchain`, and `ZKP` are domain hints; the update must find or propose a direction and topic cluster.
- A single paper/repository may propose a new L3 topic, but it should not promote a new L2 direction unless there is recognized terminology, multiple supporting sources, strong user interest, or a clear conceptual boundary.
- When a source introduces `CFT`, `BFT`, `PBFT`, or `Raft`, the automatic classification should look for the chain `blockchain-systems or distributed-systems -> consensus -> fault model/protocol family -> source`, not create isolated top-level notes.
- Relationship extraction is automatic and follows hierarchy classification. It should infer and record edges such as `Crash-Fault Tolerance is_a consensus fault model`, `Raft instance_of Crash-Fault Tolerant consensus protocol`, and `consensus used_in blockchain systems` when evidence supports them.
- Existing source locations remain stable. Reclassification updates frontmatter, maps, indexes, ledgers, and review queues; it does not move paper/repo notes by default.
- Upper-layer notes are organized by hierarchy: domain maps/syntheses, direction maps/syntheses, topic/content-cluster notes, then source/project evidence.
- If an incoming source reveals a missing parent domain, direction, or topic cluster, create or queue the missing pack first, then attach the source as an extension.

### Canonical Packs

Use packs as maintained memory objects:

- `Domain Pack` (`L1`): a domain knowledge node, including directions, prerequisites, representative sources, practice ecosystem, freshness/watchlists, gaps, and cross-domain bridges.
- `Direction Pack` (`L2`): a direction knowledge node nested under a domain, including foundation, taxonomy, applications, representative papers/repos, new source extensions, and freshness signals.
- `Topic Pack` (`L3`): a focused problem/method/application knowledge node inside a direction, including definitions, variants, representative sources, implementation patterns, and relation edges.
- `Source Extension` (`L4`): the delta contributed by one paper/repo/web/news item relative to the L1/L2/L3 packs.

Source Extension does not mean cloning the source note into the upper layer. It means recording the minimal reusable delta: contribution, assumptions, limitation, affected concept/topic, and link back to the detailed source memory.

Default lanes:

```text
04_Knowledge/<domain>/index.md
04_Knowledge/<domain>/<direction>/index.md
04_Knowledge/<domain>/<direction>/<problem-or-topic>.md
04_Knowledge/<domain>/<direction>/<problem-or-topic>/<subproblem-or-method>.md
```

Existing flat map/synthesis paths are allowed for backward compatibility only. New notes should declare `node_kind`, `hierarchy_level`, `domain_id`, `direction_id`, `topic_ids`, `parent_knowledge_refs`, and `child_knowledge_refs` so agents do not infer hierarchy from folders alone.

### Hierarchy Classification Pass

`nahida-update` and `nahida-knowledge-get` must run hierarchy classification before durable knowledge/bridge updates:

1. Normalize candidate L1 domain(s). Split overly broad AI-like labels into precise domains when possible.
2. Resolve or propose an L2 research direction under the domain.
3. Resolve or propose one or more L3 topic/content clusters under the direction.
4. Attach L4 source/project evidence with contribution, assumptions, evidence, limitations, and relation to existing L1/L2/L3 packs.
5. Run automatic relation extraction over the resolved hierarchy and affected notes.
6. Update or queue the relevant Domain Pack, Direction Pack, Topic Pack, indexes, ledgers, and review queues.

This pass must be evidence-aware and conservative. It may use Codex/model-prior knowledge to propose structure, but durable placement needs vault evidence, explicit user intent, or stable external foundation sources gathered during update/research mode.

### Path Materialization And Propagation

After a paper or repository has been deeply read, Nahida must materialize a logical update path and then update along that path. This is not a filesystem path and must not move the source note. It is the stable retrieval/update route through the ontology.

Canonical path shape:

```text
domain_id / direction_id / topic_id / source_or_project_id
```

Rules:

- Every deep-read paper note and deep-analyzed repository note should produce one `primary_ontology_path` and, when necessary, `secondary_ontology_paths` for cross-cutting evidence.
- The path must be grounded in the hierarchy classification result: L1 domain, L2 direction, L3 topic/content cluster, and L4 source/project evidence.
- If any path node is missing, the update should create or queue the missing Domain Pack, Direction Pack, or Topic Pack parent-first before writing the source as settled evidence.
- The path update plan should list the exact upper-layer notes to create, refresh, mark stale, or leave unchanged: domain map/synthesis, direction map/synthesis, topic map/synthesis/concepts, relation edges, indexes, ledgers, watchlists, and review queues.
- A source can be attached to multiple paths, but only one should be primary unless the source is genuinely cross-domain. Secondary paths should be explicit bridge or application paths, not silent duplicate placement.
- Path propagation is incremental. Do not rewrite the whole domain when a topic-level source only changes one topic; update the smallest affected pack and record whether parent synthesis refresh is needed.
- The update report must include `Path Materialization` and `Path Propagation` sections for every absorbed paper/repository.

Propagation order:

1. Validate or create the L1 Domain Pack.
2. Validate or create the L2 Direction Pack under that domain.
3. Validate or create the L3 Topic Pack under that direction.
4. Attach the L4 source/project as a source extension under the topic and, when useful, representative material under the direction/domain.
5. Update relation edges and generated indexes so query can traverse the path.
6. Refresh or mark stale affected syntheses based on freshness and materiality.

### Cross-Path Bridge Layer

Cross-direction content is represented as a structured relationship between ontology paths, not as a loose summary. A cross-direction note should answer: which paths are connected, what kind of relation exists, what evidence supports it, what transfers across the boundary, what does not transfer, and which upper-layer packs should be refreshed.

Canonical bridge shape:

```text
bridge_id:
  endpoint_paths:
    - domain_a/direction_a/topic_a
    - domain_b/direction_b/topic_b
  relation_types:
    - application|analogy|dependency|tension|translation|shared_pattern|co_evolution|evaluation_transfer|implementation_reuse
```

Bridge objects:

- `05_Bridges/<bridge>.md` - durable bridge note with endpoints, relation types, evidence, transfer limits, and query keys.
- `04_Knowledge/...` endpoint nodes - reciprocal bridge links and current synthesis sections when a bridge affects endpoint understanding.
- Generated reports/query memory - optional dated summaries when the bridge is broad, changing, or queried repeatedly.
- Relation edges in affected domain/direction/topic notes and `links.index.jsonl`.

Rules:

- A bridge must have at least two endpoint paths. Endpoints can be domains, directions, or topics, but topic-level endpoints are preferred when evidence is specific enough.
- A bridge must have a relation type. Do not use vague `related_to` when a precise type such as `dependency`, `application`, `shared_pattern`, or `tension` is available.
- A bridge must not merge the endpoint directions. It records a relationship while preserving each endpoint's own pack and path.
- A paper/repo that spans multiple directions should create one primary ontology path and one or more secondary paths, then either update an existing bridge or create/queue a bridge candidate.
- A bridge is durable only when it has evidence from source notes, knowledge nodes, or prior bridge/query reports that cite sources. Model-prior-only bridges stay `review` or `candidate`.
- Bridge propagation updates both endpoint packs with reciprocal links, relation edges, and freshness/staleness decisions.
- Cross-direction synthesis should be created when a bridge accumulates multiple sources, affects research strategy, is queried repeatedly, or has time-sensitive movement.

Bridge quality dimensions:

- `relationship_thesis`: the concise claim about why the paths are connected.
- `endpoint_scope`: exact domain/direction/topic endpoints and what part of each endpoint is involved.
- `transfer_matrix`: what concepts, methods, metrics, implementation patterns, or assumptions can transfer.
- `non_transfer_boundary`: where the analogy/application breaks.
- `evidence_set`: source/knowledge refs and confidence.
- `directionality`: one-way, two-way, cyclic, or uncertain.
- `maturity`: candidate, active_seed, active, evergreen, stale, or rejected.

### Deepening Gate For Search And Daily Inputs

`nahida-research-search` and `nahida-daily-fetch` often see candidates before they are deeply read. They must decide whether an item can update upper memory directly or needs a deeper bottom-layer skill first.

Deepening decisions:

- `deep_paper_required`: a paper candidate must go to `nahida-paper-read` before durable knowledge or bridges can use it.
- `deep_repo_required`: a GitHub repository candidate must go to `nahida-github-repo-analyze` before durable implementation knowledge or bridges can use it.
- `web_research_note_ok`: a web/reference/blog cluster may become a structured lower-layer research/source note if source quality and scope are adequate.
- `freshness_signal_only`: news, release chatter, hot terms, and weak recent signals may update watchlists, daily reports, or hot-topic review queues, but not evergreen knowledge.
- `foundation_pack_research_ok`: stable reference/survey/official sources gathered specifically for a missing foundation may update a Foundation Pack through `nahida-knowledge-get`.
- `discard_or_review`: low-quality, duplicate, ambiguous, or off-scope items should be skipped or placed in review.

Search and daily reports must include the deepening decision, target path candidates, and next skill owner for every accepted item. If a search/daily run finds a high-value paper or repository, it should queue or invoke the relevant deep skill rather than summarizing it shallowly as durable knowledge.

### Legacy Note Quality Contract

Every durable Nahida note should be usable by a human and by an AI agent:

- It states its scope and what it does not cover.
- It has enough detail to answer common follow-up questions without rereading the raw source.
- It preserves provenance with source refs, GitHub URLs, paper identifiers, section/page/file references, or lower-note links.
- It uses precise terminology, aliases, and direction facets for retrieval.
- It distinguishes evidence, author/source claims, synthesis, inference, uncertainty, and open questions.
- It is Chinese-first while preserving canonical English technical terms and IDs.
- It avoids vague one-paragraph summaries, duplicate note sprawl, and ungrounded broad claims.

Thin notes should stay in `review` or `staged` status and must not become confident evidence for upper-layer synthesis.

### Legacy Foundation Knowledge And Source Extensions

Nahida should not treat every paper or repository as if it were the whole world. Papers, repositories, webpages, and news items are evidence and extensions over an existing body of knowledge. A good concept/map/synthesis note should explain the existing concept clearly, then show how each source extends, challenges, applies, or refines that concept.

Use four knowledge layers explicitly:

- `foundation`: stable background knowledge needed to understand the topic. Prefer textbooks, surveys, standards, official docs, canonical papers, or stable explainers. During update/research tasks, use web/source search when the vault lacks foundation.
- `model_prior`: Codex's existing knowledge used for structure, terminology, examples, and initial explanation. It may guide writing, but it is not evidence by itself.
- `source_extension`: what a specific paper, repo, webpage, or dataset adds beyond the foundation.
- `synthesis`: Nahida's reasoned integration of foundation and source extensions, with uncertainty and provenance.

Rules:

- Knowledge nodes should be written as high-quality foundation/problem/method notes, not as a list of extracted paper bullets.
- If a knowledge node has no adequate foundation in the vault, `nahida-update`/`nahida-knowledge-get` should run or request `nahida-research-search` for stable foundation sources before promoting the node to `evergreen`.
- Codex/model-prior background can be included only when labeled as background explanation or synthesis. Confident factual claims still need source refs.
- Papers and repositories should appear in knowledge nodes as "source extensions": contribution, assumption, evidence, limitation, and relation to the foundation.
- Standalone claim files are legacy-only. A reusable assertion should normally be folded into the nearest knowledge node or bridge with source refs. A statement supported by only one source and mainly describing that source should stay inside that source's evidence table or the relevant source-extension row. Unsourced model-prior assertions must remain tentative/review and should not support knowledge or bridges as evidence.

### Legacy Foundation Packs

A domain, direction, or topic is a maintained knowledge object, not just a tag. When a source reveals that a reusable parent layer is missing or thin, Nahida should create or refresh the nearest missing Foundation Pack before letting one paper/repository define the field. For example, a KZG paper belongs under `zero-knowledge-proofs -> polynomial-commitments -> KZG commitments`; if `zero-knowledge-proofs` or `polynomial-commitments` is absent, Nahida should build or queue those packs and then attach KZG as a source/topic extension.

A Foundation Pack is a coordinated set:

- `04_Knowledge/<domain>/...` - stable entry point, navigation, foundation concepts, prerequisites, mechanisms, variants, boundaries, current synthesis, and freshness fields.
- `03_Sources/web/research/*` - foundation/application research notes produced by `nahida-research-search`.
- `03_Sources/papers/*` - new and representative paper notes linked as source extensions.
- `03_Sources/github/*` - new and representative repository/project analysis notes linked as implementation/practice evidence.
- `90_Generated/reports/daily/*` plus watchlists - news, mainstream trends, hot terms, releases, and possible new content signals.

Every pack should track four streams:

1. `基础调研`: stable definitions, prerequisites, historical context, canonical references, foundation concepts, and source quality.
2. `结构分类与应用调研`: child directions/topics, method families, problem classes, application areas, evaluation settings, representative papers, and representative repos/projects.
3. `新加入论文/仓库/来源`: lower-layer notes newly added to this hierarchy node, each as a source extension with contribution, assumptions, evidence, and limitations.
4. `相关新闻、主流方向、可能的新内容`: time-sensitive signals from daily fetch, releases, news, blogs, hot terms, and watch queries. These may update watchlists or hot-topic synthesis, but they are not evergreen foundation until corroborated.

The pack can start as `seed`, `foundation_thin`, or `review`. It should still expose gaps explicitly, so future updates know what to fetch next. Do not collapse all streams into one huge note; keep lower-layer evidence separate and let map/synthesis notes link to them.

### Legacy Relation Graph Layer

Nahida must make concept and direction relationships explicit. A relationship such as `CFT -> consensus algorithms -> blockchain consensus` should not live only in prose; it should be represented as graph edges that maps, query, synthesis, and audit can traverse.

Use relation edges for reusable conceptual or directional structure:

```yaml
relation_edges:
  - from: "nahida-knowledge-crash-fault-consensus"
    relation: "is_a"
    to: "nahida-knowledge-consensus-algorithms"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/crash-fault-consensus.md"
      - "doi:10.5555/2643634.2643666#sha256:0f53a6508592"
    confidence: "medium"
    status: "active"
```

Canonical relation types:

- `is_a` - subtype/classification, e.g. `Crash-Fault Consensus -> Consensus Algorithms`.
- `instance_of` - concrete protocol/project/source instantiates a concept, e.g. `Raft -> Crash-Fault Consensus`.
- `part_of` - component belongs to a system or method family.
- `has_child` - parent domain/direction/topic has child direction/topic.
- `depends_on` - prerequisite or mechanism dependency.
- `contrasts_with` - near term that must be distinguished.
- `applies_to` - concept/direction applies to an application area.
- `used_in` - concept/direction is used in a domain or system family.
- `implements` / `implemented_by` - repository/protocol implements concept.
- `bridges_to` - meaningful cross-domain relation.
- `evidenced_by` - relationship or concept supported by a source note.

Rules:

- Every important concept/direction note should record parent concepts, child concepts, adjacent concepts, and application domains when they are known.
- Domain, direction, and topic maps should include a `关系图谱` section for parent/child, subtype, application, contrast, and bridge edges.
- `nahida-knowledge-get` must run an automatic relation extraction pass whenever it creates/refines a source, concept, direction, map, bridge, or synthesis. Relation edges should be extracted from the current source note, existing related notes, frontmatter facets, aliases, map membership, claims, and synthesis context, not manually invented ad hoc after the user notices a missing relation.
- Relationship edges may be source-backed, synthesis-backed, or tentative. Do not present tentative/model-prior edges as durable truth.
- For cross-domain relations such as `consensus algorithms -> blockchain`, use `applies_to`/`used_in` and mark status `pending` or `source_backed_seed` when blockchain-specific sources have not yet been absorbed.
- Generated indexes such as `links.index.jsonl` should include relation edges so `nahida-query` can traverse from a child concept/topic to parent directions and adjacent domains.

### Automatic Relation Extraction Pass

This pass is mandatory for every non-trivial `nahida-knowledge-get` run and for `nahida-update` runs that route to it.

Inputs:

- newly created or updated source/project/research/daily notes,
- existing concepts/maps/syntheses matched by aliases, facets, tags, and source refs,
- generated indexes and ledgers as retrieval aids,
- explicit user corrections, if present.

Extraction procedure:

1. Collect candidate entities: knowledge nodes, directions, protocols, methods, applications, repositories, papers, datasets, benchmarks, standards, and domains mentioned in the input set.
2. Resolve candidates to canonical Nahida IDs when possible; create `unresolved_entity` review items when the target knowledge/direction does not exist.
3. Generate typed candidate edges using the canonical relation types above. Prefer precise relations over vague `related_to`.
4. Attach evidence for every candidate edge: source refs, note paths, section names, claim refs, frontmatter facets, map entries, or explicit user correction.
5. Score each edge:
   - `active`: supported by durable source/knowledge/bridge evidence and no known conflict.
   - `active_seed`: supported by a small but clear evidence set, usually one or two deep-read sources.
   - `pending`: plausible and useful, but key target sources are queued or not yet absorbed.
   - `review`: weak, ambiguous, model-prior-only, overly broad, or ontology-changing.
   - `rejected`: duplicate, unsupported, or wrong relation type.
6. Promote only `active` and `active_seed` edges into knowledge/bridge frontmatter/body and `links.index.jsonl`.
7. Write `pending` and `review` edges into the absorption report and, when useful, a review queue. Do not hide them in prose.

Outputs:

- a `关系图谱` section in the affected concept/map/synthesis or a clear statement that no durable edges were promoted,
- relation rows in `90_Generated/indexes/links.index.jsonl`,
- relation extraction summary in the knowledge/update report,
- review queue entries for ambiguous or missing parent/child/application edges.

### Legacy Storage And View Separation

Nahida stores notes by stable identity and source type, not by mutable research direction.

Storage paths should answer "what is this object?" rather than "which direction do we currently think it belongs to?":

- Papers live under `03_Sources/papers/` with stable IDs from DOI, arXiv ID, checksum, or normalized title.
- GitHub repository analyses live under `03_Sources/github/`, keyed by `owner/repo` and analyzed ref. Legacy `08_Projects/github/` may be read as old context only.
- Web source notes, knowledge nodes, bridge notes, run notes, and review notes live under their canonical current lanes.
- Synthesis lives inside `04_Knowledge/` nodes or as child knowledge nodes when the split gate passes. Legacy `09_Syntheses/` notes may be read as migration context.

Hierarchy membership is represented as views over notes:

- YAML facets: `domain_id`, `direction_id`, `topic_ids`, `hierarchy_level`, `ontology_path`, `domains`, `topics`, `primary_direction`, `secondary_directions`, `direction_facets`, `classification_*`, `taxonomy_version`.
- Obsidian affordances: `tags`, wikilinks, backlinks, Bases views, and Canvas maps.
- Nahida structures: knowledge nodes, bridge notes, generated indexes, ledgers, and query reports.

Do not move or duplicate a source note just because its domain/direction/topic placement changes. Reclassification updates metadata, maps, indexes, ledgers, and review queues. Folder hierarchy is not the ontology.

Use tags as ergonomic hints, not as the sole source of truth. Important tags should correspond to structured frontmatter or map entries. Prefer stable canonical direction IDs plus aliases/search terms for AI retrieval.

### Legacy Synthesis Layer

`09_Syntheses/` was the old upper memory layer. It is now compatibility context. Current synthesis should live in `04_Knowledge/` node sections or in child `knowledge` notes when the split gate passes. Cross-direction synthesis belongs in `05_Bridges/`.

Legacy lanes that may be read during migration:

```text
09_Syntheses/
  Domains/
  Directions/
  Topics/
  Programs/
  CrossDirection/
  Emerging/
  HotTopics/
  Questions/
```

Synthesis kinds:

- `domain_state` - broad L1 domain memory, such as zero-knowledge proofs, AI agents, or blockchain systems, spanning multiple direction packs.
- `direction_state` - development of one direction, including recent changes, core concepts, representative sources, gaps, and watch terms.
- `topic_state` - development of one L3 topic/content cluster inside a direction, including variants, mechanisms, representative sources, and implementation/evaluation details.
- `research_program` - a long-running theme or user-interest program that cuts across several directions and source streams.
- `cross_direction` - relationship between two or more directions, including transfer limits and bridge candidates.
- `emerging_direction` - a newly observed direction or term that may become a durable map entry later.
- `hot_topic` - recent/high-attention topic, explicitly time-sensitive and evidence-limited.
- `question_synthesis` - durable answer to a recurring user question when it deserves more than a query report.

Knowledge synthesis sections/notes must cite lower-layer notes or primary source refs. They should not cite only query reports or generated indexes. Query reports may be used as retrieval hints, not as evidence.

Freshness policy:

- Default synthesis freshness window: 30 days.
- Each synthesis note should include `last_synthesized`, `valid_until`, `freshness_status`, `evidence_window_start`, and `evidence_window_end`.
- If `valid_until` is in the future and no newer relevant lower-layer notes exist, query may reuse the knowledge synthesis and avoid deep source reads.
- If a synthesis section/node is older than 30 days, marked `stale`, or superseded by newer evidence, `nahida-query` should report that it may be stale and propose `nahida-update` or a knowledge refresh.
- `nahida-update` and `nahida-knowledge-get` should refresh only the knowledge nodes affected by new lower-layer notes, not the entire vault.

Obsidian usage:

- Use wikilinks from knowledge/bridge notes to lower-layer source notes and supporting knowledge/bridge refs.
- Use Bases views for dashboards over `type: source`, `type: knowledge`, `type: bridge`, stale knowledge nodes, review queues, and watchlists when useful.
- Use Canvas only for high-value direction graphs or cross-direction maps; do not require a Canvas for every update.

## Core Skill Set

Nahida starts with a small set of rigorous skills. Most daily use should go through the two intelligent entry points:

- `nahida-update` - primary bottom-up write/update router for PDFs, folders, URLs, pasted text, GitHub repos, web searches, daily refreshes, intake queues, and mixed inputs.
- `nahida-query` - primary top-down vault-only read/query router for answering from existing Nahida knowledge, retrieving sources, finding related directions, and detecting knowledge gaps.

The following skills are specialized capabilities that `nahida-update` may call or follow:

- `nahida-paper-read` - read one paper PDF or paper metadata record into a structured academic reading note.
- `nahida-github-repo-analyze` - analyze one specific GitHub repository into a structured implementation and architecture source note.
- `nahida-research-search` - search web sources for a keyword or research question and produce a structured lower-layer web research note.
- `nahida-daily-fetch` - run a freshness-oriented fetch from current knowledge nodes, bridges, watchlists, and query gaps, then hand accepted items to deeper skills.
- `nahida-knowledge-get` - absorb complete source notes into `04_Knowledge/` nodes, `05_Bridges/`, indexes, ledgers, and review queues.
- `nahida-consolidate` - decide whether existing notes need knowledge-node refresh, bridge cleanup, legacy migration, or no-op handling without rereading raw sources.
- `nahida-audit` - inspect the vault and skill outputs for structural and provenance problems.

Every source-producing skill should end with a `nahida-knowledge-get` handoff when the source is ready for absorption. `nahida-update` is responsible for routing and bottom-up orchestration; `nahida-query` is read-only and vault-only by default, works top-down from `04_Knowledge/` to `05_Bridges/` to `03_Sources/`, and should propose exact update/consolidation actions when it discovers missing or stale knowledge.

## Query Mode Contract

`nahida-query` is a retrieval surface over the existing Nahida vault, not an external research agent. Its default mode is `vault_only`.

In `vault_only` mode:

- Use existing knowledge nodes, bridges, source notes, generated indexes, reports, ledgers, review queues, and legacy notes as compatibility context.
- Do not browse the web, call external APIs, fetch DOI/arXiv/Crossref/GitHub metadata, clone repositories, inspect remote websites, or read local files outside the Nahida repository/vault to answer the question.
- Do not fill missing evidence with general model knowledge. General reasoning may only connect cited vault evidence and must be labeled as inference.
- If a paper, repository, knowledge node, bridge, or latest-progress request is not covered by the vault, say so explicitly.
- For time-sensitive questions such as "最新", "最近", "today", or "current progress", use only existing daily reports, dated source notes, freshness ledgers, and knowledge-node freshness fields. If current evidence is absent or stale, say `知识库没有足够新近资料`.
- For missing source coverage, say `知识库没有记录` or `知识库只有部分记录`, then suggest an explicit `nahida-update` action.

External retrieval is allowed only after explicit update/research authorization, for example when the user asks to use `nahida-update`, `nahida-research-search`, `nahida-daily-fetch`, `nahida-paper-read`, `nahida-github-repo-analyze`, or says to add, import, refresh, search, crawl, fetch latest, or research a topic.

### Query Memory

Nahida may record non-destructive query reports under `90_Generated/reports/queries/` and query ledger entries under `90_Generated/ledgers/`. These records reduce repeated retrieval cost and preserve what was already asked.

Query memory should include:

- original question,
- normalized/canonical question,
- query key or semantic fingerprint,
- aliases and expanded terms,
- retrieval plan,
- knowledge nodes, bridge notes, source notes, daily reports, and indexes used,
- coverage state: `found|partial|missing|stale`,
- freshness window and last source date,
- answer summary,
- gaps and suggested update actions.

Before broad retrieval, `nahida-query` should check query memory for exact or semantically similar questions. If a previous report is still fresh and its evidence set covers the new query, reuse it as a context bundle and only verify whether newer vault notes changed the answer. If the report is stale, partial, or based on a different scope, use it as a hint rather than as evidence.

Query reports and ledgers are caches. They are not the source of truth; final answers still need to cite knowledge nodes, bridge notes, source notes, or daily/freshness notes.

## Input Routing

`nahida-update` should infer routes from user input:

- PDF file, DOI, arXiv, paper URL, XiaoLvJing/Zotero metadata -> `nahida-paper-read`.
- Folder of PDFs -> inventory, deduplicate, cluster by research field, create an intake queue, then serially run `nahida-paper-read` one pending paper at a time with `nahida-knowledge-get` handoff and checkpointing until the queue is exhausted, user-limited, or blocked.
- GitHub URL, `owner/repo`, local checkout -> `nahida-github-repo-analyze`.
- Multiple GitHub URLs, repo lists, or checkout lists -> inventory and prioritize a repo intake queue, then serially run `nahida-github-repo-analyze` one pending repository at a time with `nahida-knowledge-get` handoff and checkpointing until the queue is exhausted, user-limited, or blocked.
- URL, webpage, pasted article, pasted paragraph -> source classification and `nahida-research-search` or direct source note.
- Research keyword or "帮我调研..." -> `nahida-research-search`.
- "最新", "最近", "每日", "更新一下" -> `nahida-daily-fetch`.
- Existing source notes needing integration -> `nahida-knowledge-get`.
- Existing notes needing optimization without source rereading -> `nahida-consolidate`.
- Questions about existing knowledge -> `nahida-query`.

## Data Source Lanes

### Web

Classify web sources before distillation:

- `web_reference` - official docs, standards, API docs.
- `web_concept` - evergreen explainers and tutorials.
- `web_blog` - engineering posts, opinions, field notes.
- `web_news` - launches, announcements, time-sensitive coverage.

`web_news` should not directly update evergreen knowledge nodes unless corroborated.

### GitHub

GitHub repositories are practice evidence. A Nahida pass should target one specific repository and capture repo purpose, docs, architecture, modules, entry points, implementation patterns, dependencies, APIs, data formats, and README-vs-code gaps. Prefer codegraph-backed summaries when a local checkout and CodeGraph index are available. Issues, PRs, discussions, stars, and social metrics are not default evidence; use them only when explicitly requested or when they are needed to explain repository practice.

Do not store cloned GitHub repositories in the Nahida vault or repository. Clone into a temporary non-vault path, analyze the repo, then delete the clone unless the user explicitly asks to keep an external checkout. Nahida should store only metadata, analyzed commit/ref, evidence summaries, file/symbol references, and structured analysis notes.

### Papers

Treat local PDFs, XiaoLvJing exports, Zotero exports, and emerging paper feeds as adapters into the same normalized paper candidate shape. Deduplicate conservatively: DOI, arXiv ID, checksum/content hash, and strong canonical IDs may auto-dedupe; title/authors/year and soft similarity should normally produce `possible_duplicate_review`, not skipped papers.

PDF title extraction is noisy. Metadata titles, first-page lines, proceedings headers, publisher/copyright text, template artifacts, and download banners must be filtered before dedupe, classification, or queue priority. If the best title is weak or generic, use checksum as the identity and keep both candidates in the queue.

### Deep Reading Contract

Papers and GitHub repositories are high-value evidence and should not be reduced to shallow summaries.

For papers:

- Durable paper notes require `reading_depth: deep_read`.
- `deep_read_complete` means the note covers the paper identity, section/page map, problem setting, assumptions, method/protocol/algorithm, experiments or formal evidence, limitations, reusable ideas, and evidence anchors.
- `deep_read_complete` also requires evidence density: the note should reconstruct the actual mechanism, proof/evaluation logic, assumptions, and limitations with page/section/table/figure/theorem anchors. Full-text extraction or broad page-range coverage alone is not sufficient.
- Metadata-only, abstract-only, first-page-only, or poor-extraction notes are staging artifacts. Mark them `deep_read_pending`, `extraction_gap`, or `needs_human_review`.

For GitHub repositories:

- Durable repo notes require `analysis_depth: deep_repo_read`.
- `deep_analysis_complete` means the note covers docs, manifests/configs, entry points, core modules, API/CLI/config surface, tests/examples, primary flows, README-vs-code checks, and file/symbol evidence.
- README-only, file-tree-only, social-metadata, or scouting notes are staging artifacts. Mark them `deep_analysis_pending` or `needs_followup`.

`nahida-knowledge-get` may absorb incomplete paper/repo notes only into indexes, ledgers, review queues, or clearly tentative inline evidence records. It must not create confident durable knowledge nodes or bridges from shallow paper/repo readings.

### Serial Queue Execution

Folder/list updates are resumable serial jobs, not one-item samples.

- Default queue mode is `serial_auto` unless the user explicitly requests queue-only, sample-only, or a fixed item limit.
- Deep-read or analyze exactly one source at a time, then run/follow `nahida-knowledge-get`, update knowledge nodes/bridges/ledgers/indexes as needed, checkpoint, and continue to the next pending item.
- Distinguish hard user limits from soft turn budgets. `user_item_limit` is an explicit user cap and may end the run in a terminal partial state. `turn_item_budget` is a per-turn/context quality budget and may only create a checkpoint; it is not a completion or stop condition for the overall queue.
- A queue run with pending items must use a partial state such as `partial_serial_pending`; it must not be reported as fully `succeeded` or `complete`.
- Queue checkpoints should record `queue_id`, `processed_count`, `remaining_count`, `current_item`, `last_processed_item`, `next_item`, item status, blocker, `turn_item_budget`, `continuation_required`, and resume command.
- If execution is interrupted by a soft batch budget, context limits, runtime failure, or user interruption, the report should say the queue is incomplete and identify the next item to process. For soft batch/context checkpoints with no blocker and no hard user limit, set `continuation_required: true` and arrange or request continuation rather than presenting the checkpoint as a finished answer.

### Hierarchy Evolution

Nahida should discover finer hierarchy nodes from the evidence stream. Broad domains such as `AI` should self-refine into precise L1 domains or L2 directions such as `ai-agents`, `agent-memory`, `multi-agent-orchestration`, `subagents`, `tool use`, or `context engineering` when source support is strong enough.

### Self-Upgrading Loop

Nahida is expected to upgrade itself during normal use. Every meaningful update should include an expansion pass that looks for:

- child directions and topic/content clusters,
- adjacent directions,
- prerequisite foundations,
- representative papers,
- representative GitHub repositories,
- standards, protocols, datasets, benchmarks, or tools,
- emerging aliases and search keywords,
- cross-domain bridge candidates,
- stale areas that need a freshness check.

Expansion must be bounded and evidence-aware. Do not recursively chase every related term. Prefer 3-10 high-signal candidates per update, record why each candidate matters, and route weak or uncertain candidates to watchlists or review queues instead of promoting them directly.

### Hierarchy Granularity

Domains, directions, and topics should be precise, reusable retrieval buckets. Do not create one permanent direction per paper or repo. A new direction is justified when it has recognized terminology, multiple supporting sources, strong user interest, or a clear conceptual boundary. Otherwise attach the source to the closest existing direction/topic and record a candidate for review.

Use layered labels when possible:

- L1 domain,
- L2 research direction,
- L3 topic/content cluster,
- task/problem,
- method family,
- implementation category,
- evaluation/application setting,
- aliases and near terms.

### Hierarchy Classification Stability

Paper identity and direction placement must be decoupled. A paper note should use a stable identity path based on DOI, arXiv ID, checksum, or normalized title; do not move or rename the paper note solely because its direction classification changes later.

Use hierarchy placement as metadata and map membership:

- `domain_id` - canonical L1 domain.
- `direction_id` - canonical L2 direction under the domain.
- `topic_ids` - one or more L3 topic/content clusters.
- `ontology_path` - ordered path such as `blockchain-systems/consensus/byzantine-fault-tolerance`.
- `primary_direction` - the best current canonical direction.
- `secondary_directions` - relevant but non-primary directions.
- `classification_status` - `staged|active|review|reclassified|retired`.
- `classification_confidence` - `low|medium|high`.
- `classification_evidence` - title, abstract, keywords, venue, local PDF sections, metadata, or human correction.
- `taxonomy_version` - the ontology version used for classification.

When a folder or many PDFs are provided, build an intake queue before durable map promotion:

1. Build an inventory from metadata, checksum, filename, title, abstract, first pages, DOI/arXiv hints, and extraction quality.
2. Enrich public metadata for DOI/arXiv items when useful.
3. Filter generic PDF titles and record `title_source`, `title_confidence`, and `title_warnings`.
4. Cluster with multi-label facets rather than a single folder guess.
5. Use title, abstract, DOI/arXiv metadata, venue, user scope, and existing vault gaps for classification/priority; do not promote a paper based on references, citation contexts, generic proceedings headings, or boilerplate text.
6. Assign `domain_id`, `direction_id`, and `topic_ids` only when evidence is strong enough.
7. Put ambiguous, cross-cutting, or possible-duplicate papers into review rather than forcing a brittle label or skipping them.
8. Record user corrections as classification evidence with higher priority than filename heuristics.
9. Deep-read and absorb one current queue item at a time, but continue serially through the pending queue by default; queued PDFs are not considered absorbed until their own deep-reading note and absorption handoff are complete.
10. If a per-turn/context budget is reached, checkpoint with `stop_reason: turn_budget_checkpoint`, `continuation_required: true`, and the exact `next_item`; then continue in the current turn if possible or schedule/request continuation. Do not treat this as a normal stop unless the user set a hard `user_item_limit`.

Reclassification should update frontmatter, maps, indexes, and ledgers. It should not delete old notes or silently rewrite history. Use review queues for bulk taxonomy changes.

### Foundation Gaps

When a source belongs to a domain/direction/problem with no foundation in the vault, do not let that source become the only explanation of the hierarchy node. Create the source note, mark `foundation_missing`, identify the nearest missing L1/L2/L3 node, run or queue a focused `nahida-research-search` with `foundation_pack` scope, then use `nahida-knowledge-get` to create or update the relevant `04_Knowledge/` node. Low-confidence foundations should stay in review.

The foundation pass should cover at least:

- foundations and prerequisites,
- core hierarchy, taxonomy, and applications,
- representative papers and repositories,
- newly added paper/repo extensions,
- freshness/news/watchlist signals.

If any lane is not covered, write the gap into the relevant knowledge node instead of silently omitting it.

### Expansion States

Expansion candidates should move through clear states:

- `candidate` - observed once or weakly supported; keep in reports or review queue.
- `watching` - worth daily fetch/watchlist monitoring.
- `active` - enough evidence or user interest to appear in knowledge nodes as an emerging direction/problem.
- `evergreen` - stable enough to have durable knowledge-node coverage.
- `rejected` - duplicate, too vague, off-scope, or unsupported.

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
- All durable knowledge statements must trace to sources or be marked tentative/model-prior background.
- Generated indexes are rebuildable caches, not the source of truth.
- Multi-user sync, pull, push, and conflict automation are out of scope for the initial repository.
