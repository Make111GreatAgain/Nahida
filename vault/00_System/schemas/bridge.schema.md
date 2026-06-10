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
type: "bridge"
from_domain: ""
to_domain: ""
relation_type: "application|analogy|dependency|tension|translation|shared_pattern"
status: "draft|review|evergreen|stale|retired"
source_refs: []
managed_by: "nahida"
```

Bridge notes must include limits of the analogy or relationship.
