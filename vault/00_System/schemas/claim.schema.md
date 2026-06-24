---
title: "Nahida Claim Schema"
type: "schema"
managed_by: "nahida"
schema_version: "1.0"
ontology_version: "1.0"
---

# Claim Schema

Legacy schema. Routine Nahida updates must not create new `04_Claims/` notes. Keep source-local evidence in `03_Sources/`, reusable structure in `04_Knowledge/`, and cross-node relations in `05_Bridges/`.

Required properties:

```yaml
id: "nahida-claim-..."
title: "..."
type: "claim"
statement: "..."
claim_kind: "definition|mechanism|theorem|empirical_result|implementation_pattern|comparison|limitation|trend|benchmark|design_principle"
status: "tentative|supported|contested|retired"
confidence: "low|medium|high"
evidence_status: "needs_source|source_backed|model_prior_tentative|contested"
hierarchy_level: "claim"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
source_refs: []
managed_by: "nahida"
```

Every claim must link to at least one source unless it is explicitly tentative. Claim notes should be Chinese-first while preserving canonical English technical terms.

Claim notes should be atomic, reusable, and rare. Do not create a claim for every sentence in a source. Create claim notes only when an assertion is cross-source, contested, comparative, foundation-level, repeatedly cited, or needed as bridge/synthesis evidence. Source-local facts about one paper, repository, webpage, experiment, theorem detail, or architecture finding should stay in that source/project/concept meta note's evidence table.

Recommended extra field:

```yaml
claim_creation_reason: "cross_source|contested|comparative|foundation_level|repeatedly_cited|bridge_evidence"
```

Required sections:

- `陈述`
- `Claim 类型`
- `证据`
- `背景与上下文`
- `反例或争议`
- `含义`
- `适用边界`
- `来源增量`
- `相关概念或综合`
- `复核历史`

Supported claims require source refs and evidence anchors. Codex/model-prior claims without sources must use `status: tentative` or `review` and `evidence_status: model_prior_tentative`.
