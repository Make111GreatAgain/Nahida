---
title: "Nahida Concept Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Concept Schema

Legacy schema. Routine Nahida updates must not create new `05_Concepts/` notes. Migrate durable explanations into `04_Knowledge/` through `nahida-consolidate`.

Required properties:

```yaml
id: "nahida-concept-..."
title: "..."
type: "concept"
definition: ""
scope: ""
status: "draft|review|evergreen|stale|retired"
foundation_status: "foundation_missing|foundation_thin|foundation_ready|foundation_stale"
concept_quality: "seed|usable|high_quality|needs_rewrite"
hierarchy_level: "concept"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
knowledge_layers:
  foundation: []
  model_prior: []
  source_extension: []
  synthesis: []
parent_concepts: []
child_concepts: []
adjacent_concepts: []
application_domains: []
relation_edges: []
domains: []
topics: []
source_refs: []
managed_by: "nahida"
```

Concept notes should distinguish foundation knowledge, model-prior background, source extensions, sparse claim refs when justified, and synthesis. Note body should be Chinese-first while preserving canonical English technical terms.

Required sections:

- `摘要结论`
- `定义`
- `范围与边界`
- `知识来源与可信度`
- `心智模型`
- `前置知识`
- `核心机制`
- `主要类型、变体或方法族`
- `例子`
- `常见混淆`
- `有来源支撑的 Claim`
- `来源增量`
- `实践或研究意义`
- `评价维度`
- `相关概念`
- `关系图谱`
- `开放问题`

Quality rules:

- A concept should be a readable foundation/explainer meta note, not a list of claims extracted from one paper.
- `model_prior` may organize explanation, but source-backed fields and rare durable claims need source refs.
- If `foundation_status` is `foundation_missing` or `foundation_thin`, keep status `draft`, `review`, or `source_backed_seed`; do not promote to `evergreen`.
- Important parent/child/subtype/application/contrast relationships should appear as relation edges with evidence, confidence, and status.
