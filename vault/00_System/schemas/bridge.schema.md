---
title: "Nahida Bridge Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Bridge Schema

Required properties:

```yaml
id: "nahida-bridge-..."
title: "..."
original_title: ""
file_slug: "path-safe-slug"
type: "bridge"
hierarchy_level: "bridge"
bridge_kind: "cross_path|cross_domain|cross_direction|cross_topic|application|analogy|dependency"
bridge_status: "candidate|active_seed|active|evergreen|stale|rejected|review"
endpoint_paths: []
endpoint_knowledge_refs: []
from_domain: ""
to_domain: ""
from_direction: ""
to_direction: ""
from_topic: ""
to_topic: ""
relation_types:
  - "application|analogy|dependency|tension|translation|shared_pattern|co_evolution|evaluation_transfer|implementation_reuse"
directionality: "one_way|two_way|cyclic|uncertain"
relationship_thesis: ""
transferability: "low|medium|high|unknown"
non_transfer_boundary: ""
status: "draft|review|evergreen|stale|retired"
source_refs: []
source_note_refs: []
knowledge_refs: []
managed_by: "nahida"
```

Required sections:

- `命名与路径`
- `连接命题`
- `端点范围`
- `可迁移知识/模式`
- `迁移矩阵`
- `类比、依赖或关系边界`
- `证据`
- `路径传播`
- `影响的 Knowledge Nodes`
- `查询入口`
- `刷新规则`
- `复核笔记`

New durable bridge notes live under `05_Bridges/`. Legacy `06_Bridges/` notes may be read or migrated by `nahida-consolidate`.

Bridge file names must use `file_slug`, not raw `title`. Preserve punctuation-heavy names such as `AI/ML x Zero-Knowledge Proofs` in `title` or `original_title`, but sanitize `/` and other path separators out of the filename. Bridge notes must include endpoint knowledge refs, endpoint paths, typed relation, transfer matrix, evidence, and limits of the analogy or relationship. Note body should be Chinese-first while preserving canonical English technical terms.

Bridge notes must be independently readable. Each endpoint should have a short local background explanation and a link to the full knowledge node. Do not make readers open both endpoint notes before they can understand the bridge thesis.
