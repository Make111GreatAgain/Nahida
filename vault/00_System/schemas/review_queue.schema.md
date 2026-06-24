---
title: "Nahida Review Queue Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Review Queue Schema

Required properties:

```yaml
id: "nahida-review-..."
title: "..."
type: "review_queue"
status: "open|resolved|rejected|archived"
owner: "human|agent|mixed"
managed_by: "nahida"
```

Review queue notes should include reason, affected paths/IDs, proposed action, risk, and resolution. Note body should be Chinese-first while preserving exact IDs, paths, and schema keys.
