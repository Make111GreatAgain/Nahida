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

Run notes should list inputs, outputs, changed paths, ledger entries, and failures.
