---
title: "Nahida Run Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Run Schema

Required properties:

```yaml
id: "nahida-run-..."
run_id: "..."
title: "..."
type: "run"
status: "running|succeeded|partial|failed"
managed_by: "nahida"
```

Run notes should list inputs, outputs, changed paths, ledger entries, and failures. Note body should be Chinese-first while preserving exact IDs, paths, commands, and schema keys.

Runs that write managed notes should include path safety checks for generated filenames, especially when source titles contain `/`, `\`, `:`, or other reserved path characters.

Update and absorption runs that process papers or repositories should include:

- `分层记忆更新`: source, knowledge, bridge, navigation, freshness/query layers updated, skipped, or queued.
- `层级归属`: L1 domain, L2 direction, L3 topic/content clusters, ontology path, evidence, confidence, and review status.
- `冷启动分层发现`: research field/domain, background, reusable problem, foundation concepts, method family, application/evaluation context, source instance, evidence, confidence, and handling decision.
- `检索优化判断`: future queries helped, source-note reads avoided, summary/update benefit, create/merge/section/source-only decision, and reason.
- `精读覆盖`: item, type, depth/status, coverage, gaps, and safe-for-absorption decision.
- `Source Readiness`: whether each paper/repo source is ready, scoped partial, or not ready for durable absorption.
- `Knowledge Nodes`: missing/thin domains, directions, or problem clusters, foundation status, knowledge paths, representative papers/repos, freshness signals, and unresolved gaps.
- `Domain Dynamics`: per-L1-domain research-dynamics notes created/refreshed/stale/unchanged/queued, evidence window, academic focus, industrial focus, emerging topics, open problems, and refresh trigger.
- `跨路径桥接`: bridge candidates/notes, endpoint knowledge paths, relation types, evidence, transfer boundary, propagation targets, and review status.
- `Knowledge Synthesis`: created/refreshed/stale/unchanged synthesis sections inside knowledge nodes, lower-note refs, freshness status, and valid-until dates.

Query runs should include:

- `规范化查询`: original question, canonical question, query key, scope, time window, and answer shape.
- `查询记忆`: reused report, cache state, freshness check, and reuse decision.
- `Alias 与 Facet 展开`: input terms, canonical terms, aliases/facets, sources, and retrieval use.
- `上层记忆`: knowledge/bridge/query reports used, freshness, valid-until dates, and whether lower-layer drill-down was needed.
- `覆盖状态`: found, partial, missing, or stale.
