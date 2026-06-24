---
title: "Nahida Map Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Map Schema

Legacy schema. Routine Nahida updates must not create new `07_Maps/` notes. Navigation and taxonomy now belong in `04_Knowledge/` nodes.

Required properties:

```yaml
id: "nahida-map-..."
title: "..."
type: "map"
status: "active|stale|archived"
map_kind: "global|domain|direction|topic|cross_domain|emerging"
hierarchy_level: "global|domain|direction|topic|cross_domain"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
parent_map: ""
child_maps: []
direction_kind: "parent|child|cross_direction|emerging"
foundation_status: "foundation_missing|foundation_thin|foundation_ready"
foundation_pack_status: "seed|active|review|stale"
domains: []
topics: []
relation_edges: []
managed_by: "nahida"
```

Required sections:

- `范围`
- `入口`
- `层级定位`
- `Foundation Pack`
- `关系图谱`
- `基础调研`
- `下级研究方向`
- `研究内容/问题簇`
- `应用调研`
- `核心概念`
- `最新综合`
- `代表论文`
- `代表仓库`
- `新加入论文`
- `新加入仓库`
- `活跃来源`
- `待复核 Claim`
- `Cross-Path Bridges`
- `新闻与主流趋势`
- `可能的新内容`
- `Watchlist`
- `新兴方向`
- `近期更新`

Map relation edges should make parent/child, subtype, contrast, application, implementation, and cross-domain edges queryable. Do not rely only on prose for relations such as CFT/BFT -> consensus algorithms -> blockchain consensus. A map that claims to be a domain, direction, or topic map must not be organized around a single paper/repository as its primary axis.
