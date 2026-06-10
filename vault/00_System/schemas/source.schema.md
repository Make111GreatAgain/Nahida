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
managed_by: "nahida"
```

Required sections:

- `Summary`
- `Why It Matters`
- `Extracted Facts`
- `Linked Claims`
- `Processing Log`
