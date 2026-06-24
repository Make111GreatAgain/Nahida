---
title: "Nahida Project Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Project Schema

Legacy schema. New GitHub repository analysis notes should be `type: source` under `03_Sources/github/`. Use this schema only for existing `08_Projects/` compatibility or explicit legacy migration/audit tasks.

Required properties:

```yaml
id: "nahida-project-..."
project_id: "..."
title: "..."
type: "project"
status: "active|blocked|completed|archived"
write_policy: "managed|suggest|read_only"
hierarchy_level: "project"
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

Legacy managed projects live under `08_Projects/` and declare `write_policy`; routine new repository notes must not use this lane.

GitHub project optional properties:

```yaml
source_kind: "github"
source_subtype: "github_repo"
analysis_depth: "deep_repo_read|scouting|scoped_deep_analysis|unknown"
analysis_status: "deep_analysis_pending|deep_analysis_complete|scoped_deep_analysis|needs_followup"
analysis_scope: []
analyzed_ref: "commit|tag|branch|unknown"
```

Legacy repository analysis notes should include `精读状态`, `仓库阅读地图`, `关键流程追踪`, `证据矩阵`, and `README 与代码对照` as their own complete evidence. Routine new repository analysis should use `source.schema.md`.
