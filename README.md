# Nahida

Nahida is an AI-native Obsidian knowledge-base protocol.

It is not primarily an application. The core deliverable is a vault structure plus Codex skills that let AI agents read, write, retrieve, audit, and maintain knowledge safely.

Nahida notes are Chinese-first. Canonical English technical terms, paper titles, project names, APIs, protocols, code symbols, file paths, and URLs should stay in English when that preserves precision and retrieval quality.

## What This Repository Contains

- `vault/` - an Obsidian-compatible Nahida vault template.
- `vault/00_System/NAHIDA_SPEC.md` - the operating contract every agent should read before writing.
- `vault/00_System/schemas/` - note type schemas for managed notes.
- `vault/00_System/templates/` - starter templates for source, claim, concept, map, synthesis, and review notes.
- `vault/09_Syntheses/` - upper-layer synthesis notes for direction state, cross-direction relationships, emerging directions, hot topics, and recurring questions.
- `skills/` - Codex skill definitions using the `nahida-*` prefix.
- `scripts/install-skills.sh` - copies Nahida skills into the local Codex skills directory.
- `docs/` - planning notes and implementation guidance.
- `examples/` - small examples of expected Nahida outputs.

## Core Skills

- `nahida-update` - intelligent write/update router for PDFs, folders, URLs, pasted text, GitHub repos, searches, daily refreshes, intake queues, and mixed inputs.
- `nahida-query` - vault-only read/query router for answering from existing Nahida knowledge, retrieving sources, finding related directions, and identifying gaps.
- `nahida-paper-read` - one paper PDF to one deep structured academic reading note.
- `nahida-github-repo-analyze` - one GitHub repo to one deep structured repository analysis note.
- `nahida-research-search` - one research query to structured web research notes.
- `nahida-daily-fetch` - current-interest freshness fetch with dedupe and handoffs.
- `nahida-knowledge-get` - absorbs notes into claims, concepts, directions, maps, bridges, synthesis notes, indexes, and review queues.
- `nahida-audit` - checks structure, provenance, duplicates, links, and incomplete outputs.

Most daily work should start with `nahida-update` or `nahida-query`. The other skills are specialized tools that the entry skills route to.

`nahida-query` does not search externally by default. If Nahida has no record of a paper, repository, direction, or recent progress, it should say the knowledge base lacks that evidence and suggest a concrete `nahida-update` action instead of browsing, fetching metadata, cloning repositories, or answering from model memory.

Nahida is designed to self-upgrade. Lower-layer notes stay detailed and independently useful; upper-layer synthesis notes summarize direction state, cross-direction relationships, emerging directions, hot topics, and recurring questions.

Claims, concepts, and sources have different jobs. A claim is an atomic source-backed assertion. A concept is a readable foundation note that explains existing knowledge, prerequisites, mechanisms, variants, boundaries, and examples. Papers and repositories are source extensions that add evidence, methods, implementations, limitations, or challenges to those concepts.

`nahida-update` works bottom-up: create or refresh high-quality lower-layer notes first, then update affected claims, concepts, maps, bridges, and `09_Syntheses/` notes. `nahida-query` works top-down: check query memory, fresh synthesis notes, and maps first, then read lower-layer notes only when the upper layer is missing, stale, ambiguous, or the user asks for evidence.

Synthesis notes have freshness metadata. By default, a synthesis is fresh for about 30 days; stale synthesis should be refreshed from lower-layer notes rather than reused blindly.

For paper folders or multiple candidate sources, Nahida builds an intake queue and processes it serially. It should not shallow-absorb everything at once, but it also should not stop after one item unless explicitly limited or blocked. Source identity stays stable, and direction classification remains mutable metadata. Reclassification should update frontmatter, maps, indexes, and ledgers rather than moving notes by default.

For GitHub analysis, Nahida does not store cloned repositories. Clones should live only in temporary non-vault paths and be deleted after analysis; the vault keeps structured analysis notes and evidence references.

Papers and repositories should be deeply read before they become durable evidence. Metadata-only, abstract-only, README-only, or scouting notes are staging artifacts; they should not produce confident claims, concepts, maps, or bridges.

Nahida does not store source notes by direction. Directions are views expressed through frontmatter facets, tags, wikilinks, maps, Bases/Canvas, generated indexes, and ledgers. Query reports under `90_Generated/reports/queries/` can cache previously asked questions so future queries reuse retrieval context without treating the cache as truth.

## Typical Use

```text
Add one paper:
Use nahida-update on /path/to/paper.pdf and deeply read it into Nahida.

Import a paper folder:
Use nahida-update on /path/to/papers to inventory, prioritize, then serially deep-read and absorb the queue one paper at a time with checkpoints.

Add a repo:
Use nahida-update on https://github.com/owner/repo.

Add a webpage or pasted paragraph:
Use nahida-update to classify and absorb this source.

Ask what Nahida knows:
Use nahida-query to explain <topic> with sources and gaps.

Ask latest progress from the vault only:
Use nahida-query to summarize the latest recorded progress for <topic>. If Nahida has no fresh evidence, say so.
```

## Install Skills

```bash
./scripts/install-skills.sh
```

Nahida expects these prerequisite skills for full-fidelity Obsidian work:

- Required: `obsidian-markdown`, `obsidian-note`
- Preferred: `obsidian-bases`, `json-canvas`

Use strict prerequisite checking when desired:

```bash
NAHIDA_STRICT_PREREQS=1 ./scripts/install-skills.sh
```

After installing, ask Codex to use one of the `nahida-*` skills from this repository. Open `vault/` as the Obsidian vault.
