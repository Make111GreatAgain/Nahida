---
title: "Nahida Synthesis Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Synthesis Schema

Legacy schema. Routine Nahida updates must not create new `09_Syntheses/` notes. Current synthesis belongs inside `04_Knowledge/` nodes or child knowledge notes when the split gate passes.

Required properties:

```yaml
id: "nahida-synthesis-..."
title: "..."
type: "synthesis"
synthesis_kind: "domain_state|direction_state|topic_state|research_program|cross_direction|emerging_direction|hot_topic|question_synthesis"
hierarchy_level: "domain|direction|topic|cross_domain|program|question"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
endpoint_paths: []
bridge_ids: []
relation_types: []
foundation_pack_scope: "foundation|taxonomy|applications|paper_extensions|repo_extensions|freshness|mixed"
source_streams: {}
status: "draft|active|stale|superseded|review|archived"
domains: []
topics: []
direction_facets: {}
source_note_refs: []
knowledge_refs: []
bridge_refs: []
relation_edges: []
evidence_window_start: "YYYY-MM-DD|unknown"
evidence_window_end: "YYYY-MM-DD|unknown"
last_synthesized: "YYYY-MM-DD"
valid_until: "YYYY-MM-DD"
freshness_status: "fresh|stale|needs_refresh|unknown"
supersedes: []
superseded_by: []
managed_by: "nahida"
```

Required sections:

- `范围与问题`
- `摘要结论`
- `证据基础`
- `Foundation Pack 覆盖`
- `综合判断`
- `结构化分解`
- `跨路径桥接`
- `关系图谱`
- `应用与实践生态`
- `变化与趋势`
- `不确定性与边界`
- `新兴信号或后续观察`
- `刷新规则`
- `反向链接`

Synthesis notes must cite lower-layer source, project, claim, concept, bridge, or map notes. Query reports and generated indexes may help retrieval, but they are not sufficient evidence. A synthesis that claims `domain_state`, `direction_state`, or `topic_state` must organize around the hierarchy node rather than a single source. A `cross_direction` synthesis must cite bridge notes or explicit cross-path relation evidence and include endpoint paths plus transfer boundaries.
