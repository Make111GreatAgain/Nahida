---
title: "Nahida Claim Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Claim Schema

Required properties:

```yaml
id: "nahida-claim-..."
title: "..."
type: "claim"
statement: "..."
status: "tentative|supported|contested|retired"
confidence: "low|medium|high"
source_refs: []
managed_by: "nahida"
```

Every claim must link to at least one source unless it is explicitly tentative.
