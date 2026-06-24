---
title: "Nahida Source Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Source Schema

Required properties:

```yaml
id: "nahida-src-..."
title: "..."
type: "source"
source_kind: "web|pdf|github|book|newsletter|dataset"
source_subtype: "web_reference|web_concept|web_blog|web_news|paper_local|paper_emerging|github_repo|github_release|unknown"
canonical_url: ""
content_hash: ""
source_fingerprint: ""
trust_tier: "unknown|primary|secondary|tertiary|personal"
status: "raw|normalized|review|archived"
hierarchy_level: "source"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
primary_ontology_path: ""
secondary_ontology_paths: []
path_update_status: "not_propagated|propagated|queued|review"
hierarchy_candidates: {}
direction_facets: {}
managed_by: "nahida"
```

Required sections:

- `来源身份`
- `范围与阅读状态`
- `摘要结论`
- `为什么重要`
- `冷启动分层发现`
- `检索优化判断`
- `结构化内容`
- `证据记录`
- `Knowledge/Bridge 候选`
- `基础概念候选判断`
- `层级候选与标签`
- `可复用记忆`
- `处理日志`

Paper source optional properties:

```yaml
reading_depth: "deep_read|inventory|scoped_deep_read|unknown"
reading_status: "deep_read_pending|deep_read_complete|scoped_deep_read|extraction_gap|needs_human_review"
reading_coverage: []
```

Paper source notes should include `精读状态`, `章节地图`, `核心精读笔记`, and `证据记录` as their own complete source evidence. Routine absorption must hand reusable material to `04_Knowledge/` nodes and `05_Bridges/`, not to legacy claim/concept/map/synthesis lanes.

`deep_read_complete` requires evidence density, not only full-text extraction. The note should reconstruct the paper's mechanism, assumptions, evaluation/proof logic, limitations, and reusable ideas with page/section/table/figure/theorem anchors. If it only contains identity, abstract-level summary, broad page ranges, or a few generic observations, use `scoped_deep_read`, `deep_read_pending`, or `needs_human_review`.

Source notes must be independently useful memories of the source. They should identify foundation candidates versus instance/source-extension candidates. A paper/repo/web source may mention CFT/BFT/zk-SNARKs as foundations, but Raft/Groth16/single modules/single results are source extensions or instances by default.

Cold-start hierarchy discovery is required when the current vault does not yet contain a usable parent path. A source note must extract research/practice field, background, reusable problem, foundation concepts, method family, application/evaluation context, and artifact/source instance from metadata and content evidence. This extraction is a handoff, not a durable taxonomy decision.

Retrieval optimization judgment is required. The source note should state which future queries the extracted hierarchy would help answer with fewer source reads, which content should remain source-only, and which missing/thin parent knowledge nodes should be queued for `nahida-knowledge-get` or `foundation_pack` research.
