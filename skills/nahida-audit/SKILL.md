---
name: nahida-audit
description: Use when checking a Nahida vault for structural validity, provenance, duplicate sources, weak knowledge nodes, bridge quality, stale indexes, unsafe writes, or incomplete skill outputs.
---

# Nahida Audit

Read `vault/00_System/NAHIDA_SPEC.md` before inspecting. This skill checks Nahida quality and writes actionable audit reports/review items.

## Current Architecture

Audit the canonical write lanes first:

- `03_Sources/`: complete source notes.
- `04_Knowledge/`: recursive knowledge nodes.
- `05_Bridges/`: cross-node bridge notes.
- `90_Generated/`: indexes, ledgers, reports, review queues.

Legacy lanes may exist and should be audited as legacy context:

- `04_Claims/`
- `05_Concepts/`
- `06_Bridges/`
- `07_Maps/`
- `08_Projects/`
- `09_Syntheses/`

Do not flag legacy directories merely for existing. Flag them when new routine writes are still targeting them, when useful legacy content has no migration/review path, or when query/update skills are treating them as the current primary structure.

## Output Language

Write audit reports and review queue items primarily in Chinese. Preserve note IDs, paths, schema keys, source IDs, URLs, and exact broken refs in original form.

## Audit Scope

Check:

- Required YAML properties on managed notes.
- Duplicate IDs and duplicate source identities.
- Unsafe path slugs, raw `/` in filenames, unexpected nested directories, punctuation-heavy titles not separated from safe file names.
- Source notes missing identity, provenance, reading/analysis coverage, evidence anchors, dates, URLs, checksums, or safe-for-absorption status.
- PDF intake queues with false duplicate risk from title similarity, boilerplate/proceedings headings, weak metadata, or citation text.
- Repo notes that are README-only but marked durable; missing analyzed commit/ref, modules, flows, CodeGraph/source evidence, or temp clone cleanup.
- Research/daily notes missing source classification, access dates, deepening decisions, dedupe, freshness limits, or next skill owner.
- Knowledge nodes missing definition, background, solved problem, parent/child structure, methods, representative sources, current synthesis, source extensions, bridge links, relation edges, gaps, or update records.
- Active L1 domain knowledge nodes missing `04_Knowledge/<domain>/research-dynamics.md`.
- Domain dynamics notes missing academic focus, industrial/practice focus, emerging topics, open problems, trend judgment, evidence window, freshness fields, or refresh triggers.
- Domain dynamics notes that answer "latest/current/trends" from model memory or uncited news instead of source-backed evidence windows.
- Knowledge nodes that are not independently readable, such as definitions replaced by "see X", missing local boundary explanation, or concepts that require opening another note before the current node is understandable.
- Knowledge nodes centered on one paper/repo/artifact when they should organize a reusable problem/method/application layer.
- Knowledge nodes created for one-off source-specific details that should be source extensions.
- Missing cold-start hierarchy discovery in source notes or runs: no research field, background, problem, foundation concepts, method family, application/evaluation context, or source instance handoff.
- Knowledge nodes without retrieval role/update scope, or nodes that do not reduce future source-note reads.
- Source-rich areas where a query would still need to scan many source notes because no domain/direction/problem/method node exists.
- Foundational concept mistakes: CFT/BFT/zk-SNARKs missing or thin while Raft/PBFT/Groth16/protocol instances are treated as foundations.
- Source notes that are too thin to answer ordinary questions about the source without reopening the raw PDF/repo/webpage.
- Bridge notes that require opening endpoint notes to understand the relation thesis, because endpoint background, transfer matrix, or non-transfer boundary is missing.
- Broad labels such as `AI`, `Blockchain`, or `ZKP` used as final placement without precise domain/direction/problem.
- Missing parent chain, for example CFT/BFT/Raft/PBFT not connected to consensus and blockchain/distributed-system contexts when evidence supports it.
- Relation edges missing type, evidence, confidence, status, or using broad `related_to` instead of precise relations.
- Bridge notes missing endpoint knowledge refs, endpoint paths, relation types, relationship thesis, transfer matrix, non-transfer boundary, evidence, maturity, refresh triggers, or reciprocal knowledge links.
- Cross-domain/cross-problem content embedded only in a knowledge node instead of represented as a bridge.
- Query answers that rely on source notes while claiming full coverage even though relevant knowledge nodes are missing/thin/stale.
- Update/knowledge-get runs that still create routine legacy claim/concept/map/project/synthesis notes.
- Serial queues marked complete while pending items remain.
- Stale `valid_until`/freshness fields, stale indexes, broken wikilinks, broken source refs.
- Missing capability usage records for substantial runs.
- Review queue items that remain unresolved.

## Procedure

1. Read spec, relevant schemas/templates, and target notes.
2. Inspect canonical lanes first, then legacy lanes for compatibility/migration issues.
3. Group findings by severity:
   - `blocking`: provenance loss, duplicate ID/source identity, unsafe path escaping lane, destructive migration risk.
   - `major`: unsupported durable knowledge, missing source coverage, wrong lane, stale/missing knowledge node, broken bridge.
   - `minor`: metadata drift, stale cache/index, formatting issue, optional dashboard gap.
4. For every finding, include path, note ID when available, invariant violated, evidence, and proposed fix.
5. Write audit report under `90_Generated/reports/audit/` or a dated audit report.
6. Put risky fixes into `90_Generated/review-queues/`; do not silently repair durable knowledge.

## Quality Gate

An audit is useful only if actionable:

- No vague "needs cleanup" findings without path and invariant.
- Distinguish canonical-lane defects from legacy migration opportunities.
- Identify whether the fix belongs to `nahida-update`, `nahida-knowledge-get`, `nahida-consolidate`, a source skill, or manual review.

## Boundaries

- Read broadly.
- May write audit reports and review queue items.
- Must not modify source/knowledge/bridge notes, raw artifacts, or indexes unless the user explicitly asks for repair.
