---
title: "Nahida Project Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Project Schema

Required properties:

```yaml
id: "nahida-project-..."
project_id: "..."
title: "..."
type: "project"
status: "active|blocked|completed|archived"
write_policy: "managed|suggest|read_only"
managed_by: "nahida"
```

Managed projects must live under `08_Projects/` and declare `write_policy`.
