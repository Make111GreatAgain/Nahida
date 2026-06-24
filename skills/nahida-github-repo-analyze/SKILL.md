---
name: nahida-github-repo-analyze
description: Use when the user provides a specific GitHub repository URL, owner/repo, branch, commit, release tag, or local checkout that should become a Nahida GitHub source analysis note.
---

# Nahida GitHub Repo Analyze

Read `vault/00_System/NAHIDA_SPEC.md` before writing. This skill deeply analyzes one repository as implementation/practice evidence and writes a complete source note under `03_Sources/github/`.

## Current Architecture

- Output lane: `03_Sources/github/`.
- Temporary clone lane: outside the Nahida vault/repository, preferably `.nahida/tmp/repos/` or a system temp directory.
- Handoff lane: `nahida-knowledge-get` updates `04_Knowledge/` and `05_Bridges/`.
- Legacy `08_Projects/github/` may be read for prior analyses but is not the primary new write lane.

## Core Standard

The output is a durable deep repository analysis note, not a README digest, popularity summary, issue triage, or social-metadata report. Issues, PRs, discussions, stars, and social metrics are out of scope unless the user explicitly asks or they are required to explain implementation practice.

Do not place cloned repositories, source trees, vendored dependencies, build artifacts, or `.git/` directories inside the Nahida vault or repo. Keep only metadata, analyzed ref, file/symbol references, architecture summaries, evidence, limitations, and handoff candidates.

The repository source note must be complete enough to answer ordinary architecture and implementation questions without recloning. It must not promote repository-specific names, modules, APIs, or implementation tricks into foundational knowledge. Mark them as source extensions unless they are clearly reusable across multiple sources.

Examples:

- Correct: a BFT implementation repo updates `byzantine-fault-tolerance` or `consensus` as implementation evidence.
- Wrong: a repo's internal module name becomes a foundational knowledge node.
- Correct: a zk-SNARK library may be representative evidence for `zk-SNARKs`, `arithmetization`, or `polynomial commitments`.
- Wrong: one library's API layout becomes the definition of zk-SNARKs.

## Cold-Start Handoff Standard

When the vault has no clear hierarchy for this repository, infer reusable candidates from README, docs, manifest files, examples, tests, public APIs, module boundaries, dependencies, and traced code flows. The source note must identify:

- research/practice field,
- background and ecosystem context,
- reusable problem solved,
- foundation concepts the repo depends on,
- method/protocol/model/architecture family,
- application/evaluation/deployment context,
- repository/source instance, including owner/repo, modules, APIs, CLI commands, benchmarks, or implementation tricks.

The handoff should say which candidates would reduce future source/code reads. Repository names, internal modules, one-off flags, and local implementation tricks stay as `source_extension`, `alias_query_key`, or `source_only` unless repeated evidence justifies a scoped knowledge node.

## Deep Repository Reading

Default depth is `deep_repo_read`. Durable repo evidence requires docs plus code:

- repository purpose, users, ecosystem, license, package managers, build/test/runtime assumptions;
- README/docs/examples/tutorials/manifests/configs/tests;
- core modules, entry points, public APIs, CLI/config surface, schemas, storage/state;
- main control/data/protocol/model/proof/agent flow when identifiable;
- representative source files and symbols;
- tests/examples that reveal expected behavior and edge cases;
- README-vs-code mismatches, missing docs, inferred design tradeoffs.

For very large repositories, use `scoped_deep_analysis` and state exact coverage. Do not imply full-repo coverage when only a subarea was read.

## CodeGraph Discipline

Prefer CodeGraph when available:

- `codegraph_context` for architecture/module overview.
- `codegraph_explore` for related symbols/files.
- `codegraph_trace` for main flow/path questions.
- `codegraph_callers`, `codegraph_callees`, or `codegraph_impact` when appropriate.

If CodeGraph is unavailable, inspect a bounded file tree, manifests, docs, examples, tests, and representative source files. Do not blindly read every file.

## Required Procedure

1. Establish identity:
   - Normalize owner/repo, URL, branch/tag/commit, analyzed ref, license, languages, package ecosystem, local path, docs path.
   - Check `03_Sources/github/`, legacy `08_Projects/github/`, and ledgers for prior analysis.
2. Prepare code access:
   - Clone only outside the vault/repository when needed.
   - Record the temporary path and delete it after analysis unless the user explicitly asks to keep a checkout outside the vault.
3. Read outward-facing material:
   - README, docs, examples, tutorials, package manifests, config samples, tests, benchmarks when relevant.
4. Analyze implementation:
   - Identify entry points, modules, APIs, data/control flow, storage formats, protocols, external services, extension points, dependencies.
   - Trace at least one main happy path, core algorithm/protocol pipeline, or user-specified focus area when code is available.
   - Compare docs claims with code evidence.
5. Classify handoff candidates:
   - L1 domain, L2 direction, L3 problem/topic/method, implementation category, algorithm/protocol family, adjacent directions.
   - Cold-start hierarchy facets: field, background, problem, foundations, method/architecture family, application/evaluation context, source instance.
   - Source-extension targets in `04_Knowledge/`.
   - Bridge endpoint candidates in `05_Bridges/`.
6. Write source note:
   - Use `vault/00_System/templates/github_repo_analysis.md` or `source.md`.
   - Store under `03_Sources/github/` with a path-safe slug based on owner/repo/ref.
   - Include `analysis_depth`, `analysis_status`, coverage, skipped areas, CodeGraph usage, and `safe_for_absorption`.
7. Handoff:
   - Run/follow `nahida-knowledge-get` if safe.
   - If README-only/scouting-only, write review/queue items and do not produce confident durable knowledge.

## Output Contract

The repo note must include:

- `Repository Identity`: owner/name, URL, analyzed ref, license, languages, ecosystem, package manager, docs, primary entry points.
- `Deep Reading Coverage`: files/modules/docs/tests/examples inspected, CodeGraph usage, skipped areas, safety for absorption.
- `Problem And Value`: concrete problem solved, audience, assumptions, non-goals.
- `Architecture`: runtime shape, components, boundaries, data/control flow, storage, protocols, deployment assumptions.
- `Main Modules`: module purpose, key files/symbols, public interfaces, dependencies, evidence refs.
- `API CLI Config Surface`: commands, APIs, schemas, config, env vars, extension points, generated artifacts.
- `Implementation Patterns`: algorithms, data structures, concurrency, caching, persistence, proof/model/agent pipeline, error handling, tests.
- `Critical Flow Traces`: primary flow with file/symbol evidence.
- `Evidence Matrix`: docs-backed, code-backed, test-backed, example-backed, inferred.
- `README vs Code`: confirmed, unclear, contradicted, missing docs.
- `Knowledge Handoff`: target knowledge nodes/sections, source-extension deltas, bridge candidates, aliases/query keys, gaps.
- `Cold-Start Hierarchy Discovery`: field, background, problem, foundation concepts, method/architecture family, application/evaluation context, source instance, evidence, confidence.
- `Retrieval Optimization`: future queries helped, source/code reads avoided, content that remains source-only.
- `Domain Dynamics Impact`: whether the repository affects L1 domain industrial/practice focus, tooling, adoption, open engineering problems, or should remain only a source extension.
- `Foundation Candidate Judgment`: reusable foundations vs repository-specific instances/modules.

## Quality Gate

Before finishing:

- No cloned repository remains in the vault/repo.
- The analyzed ref is recorded.
- The note is not README-only unless explicitly staged and not safe for absorption.
- Core modules and at least one main flow/focus area have evidence.
- Docs claims and code evidence are distinguished.
- Handoff uses Source + Knowledge + Bridge terms.

## Boundaries

- May write `03_Sources/github/`, generated repo reports, ledgers, indexes, review queues.
- Must delete temporary clones or record why an external non-vault checkout was kept.
- Must not write repository source trees into Nahida.
- Must not update `04_Knowledge/` or `05_Bridges/` directly; use `nahida-knowledge-get`.
