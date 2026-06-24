---
title: "Nahida Knowledge Schema"
type: "system"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Nahida Knowledge Schema

`type: knowledge` 是 Nahida 的主要上层记忆对象。它统一承接旧 `concept`、`map`、`synthesis` 的职责，但不承接跨领域关系；跨领域或跨问题关系属于 `type: bridge`。

## Required Fields

- `id`
- `title`
- `type: knowledge`
- `schema_version`
- `ontology_version`
- `lifecycle`
- `status`
- `node_kind`
- `hierarchy_level`
- `domain_id`
- `ontology_path`
- `source_note_refs`
- `bridge_refs`
- `query_keys`
- `aliases`
- `created`
- `updated`
- `managed_by: nahida`
- `confidence`

## Node Kinds

- `domain`
- `domain_dynamics`
- `direction`
- `problem`
- `subproblem`
- `method_family`
- `application_area`
- `evaluation_axis`

## Canonical Location

```text
04_Knowledge/<domain>/index.md
04_Knowledge/<domain>/research-dynamics.md
04_Knowledge/<domain>/<direction>/index.md
04_Knowledge/<domain>/<direction>/<problem-or-topic>.md
04_Knowledge/<domain>/<direction>/<problem-or-topic>/<subproblem-or-method>.md
```

Do not place source notes inside this tree. Sources remain under `03_Sources/` and are linked through `source_note_refs`, `representative_source_refs`, and `Source Extensions`.

## Domain Dynamics Node

Every active L1 domain should have one `node_kind: domain_dynamics` note at:

```text
04_Knowledge/<domain>/research-dynamics.md
```

It is a living, source-backed note for latest recorded research dynamics, academic focus, industrial/practice focus, emerging terms, open problems, and directional tendency. It is not a paper list and not a web-news dump.

Required sections:

- `领域范围与新鲜度`
- `研究动态摘要`
- `学术关注`
- `工业与工程关注`
- `新兴方向与热词`
- `待解决问题`
- `方向倾向判断`
- `证据窗口`
- `刷新触发器`
- `更新记录`

Query should read the domain dynamics note before scanning many sources for "latest/current/progress/trends/open problems" questions. If the note is missing or stale, report the coverage gap and suggest `nahida-daily-fetch`, `nahida-research-search`, or `nahida-consolidate`.

## Split Gate

Create a new knowledge node only when it is reusable beyond one source, has clear boundaries, has a clear parent, improves retrieval/maintenance, and is likely to collect multiple sources, queries, bridge endpoints, or freshness signals.

If the gate fails, keep the material as a section, source-extension row, evidence paragraph, alias, watchlist item, or review item inside the nearest existing knowledge node.

## Retrieval Role

Every knowledge node should act as a retrieval filter. The node should make future query cheaper by letting an agent read the domain/direction/problem/method synthesis before opening source notes. If a proposed node does not reduce source reads, clarify update scope, or anchor multiple future sources/queries, it should usually remain a section, source-extension row, alias, or review item.

Knowledge nodes should include:

- `Retrieval role`: the kinds of questions this node answers before source drill-down.
- `Update scope`: which incoming source types or topics should refresh the node.
- `Source drill-down boundary`: when an agent should stop at this node versus open source notes.

## Cold-Start Hierarchy

When no useful parent hierarchy exists, create or queue parent-first seed nodes from source metadata and existing notes:

```text
research field/domain -> direction -> research problem or method family -> optional subproblem/method -> source instance
```

Cold-start candidates must distinguish reusable structure from source instances. For example, CFT/BFT/zk-SNARKs are foundation candidates; Raft/PBFT/Groth16/repository modules/paper systems are usually representatives or source extensions unless repeated evidence or explicit user scope justifies a scoped instance node.

## Completeness Gate

A knowledge node must be independently readable. It must contain enough definition, background, problem statement, boundaries, approaches, representative sources, current synthesis, gaps, and links for a reader to understand the concept/direction/problem without opening another note first.

Links to other foundational notes are allowed, but the current note must include a concise local explanation. Do not write only "see X".

## Foundation Concept Examples

- `CFT`, `BFT`, and `zk-SNARKs` are foundation candidates when source evidence or user scope supports them.
- `Raft`, `PBFT`, `Groth16`, one benchmark, one repository, or one paper-specific system are instance/source-extension candidates by default.
- A protocol instance may become a scoped knowledge node only when multiple sources, repeated queries, or explicit user scope justify it; it must still point to the parent foundation node.

## Bridge Boundary

Knowledge nodes do not own cross-domain/cross-problem synthesis. They may link to bridge notes, but durable transfer claims, analogies, dependencies, tensions, and cross-node relationships belong under `05_Bridges/`.
