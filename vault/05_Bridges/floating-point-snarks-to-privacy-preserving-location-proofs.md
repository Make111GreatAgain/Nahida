---
id: "nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs"
title: "Floating-point SNARKs -> privacy-preserving location proofs"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
topic_ids:
  - "floating-point-snarks"
  - "privacy-preserving-location-proofs"
endpoint_knowledge_refs:
  - "nahida-knowledge-floating-point-snarks"
  - "nahida-knowledge-privacy-preserving-location-proofs"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/floating-point-snarks"
  - "zero-knowledge-proofs/applications/privacy-preserving-location-proofs"
relation_types:
  - "application"
  - "method_transfer"
  - "numerical_soundness"
  - "dependency"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
representative_source_refs:
  - "arxiv:2404.14983v2"
query_keys:
  - "floating-point SNARKs for location privacy"
  - "ZKLP floating point"
  - "IEEE 754 location proofs"
  - "geospatial ZKP floating point"
aliases:
  - "Floating-point SNARKs for ZKLP"
  - "IEEE 754 circuits for location privacy proofs"
domains:
  - "zero-knowledge-proofs"
topics:
  - "floating-point-snarks"
  - "privacy-preserving-location-proofs"
  - "location-privacy"
tags:
  - "nahida/bridge"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zklp-floating-point-snarks"
source_refs:
  - "arxiv:2404.14983v2"
confidence: "high"
trust_tier: "primary"
---

# Floating-point SNARKs -> privacy-preserving location proofs

## 关系命题

Floating-point SNARKs 可以作为 privacy-preserving location proofs 的数值语义层: geospatial libraries 使用 IEEE 754 floating-point 和复杂坐标变换，如果电路用 fixed-point 或不兼容 rounding，就可能破坏 proof completeness 或 numeric soundness。ZKLP 论文显示，IEEE 754 compliant floating-point circuits 与 trigonometric elimination 可以把 H3/DGGS 位置约束变成可验证且实用的 SNARK statement。

这条 bridge 不表示 floating-point SNARKs 自动解决 location authenticity。它只说明准确浮点电路如何支撑 geospatial proof 的正确性和效率；位置来源真实性仍要依赖 offline finding networks、authenticated GNSS、TLS oracles 或其他 provenance systems。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[floating-point-snarks|Floating-point SNARKs]] | `zero-knowledge-proofs/proof-systems/floating-point-snarks` | IEEE 754 arithmetic circuits, rounding, abnormal/subnormal handling, lookup/hint optimizations | proof-system method family |
| [[privacy-preserving-location-proofs|Privacy-preserving location proofs]] | `zero-knowledge-proofs/applications/privacy-preserving-location-proofs` | 证明地理区域、cell membership 或 proximity relation，同时隐藏精确位置 | ZKP application problem |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `application` | floating-point SNARK circuits 被用于 ZKLP application circuit | ZKLP §3-§5 | active_seed |
| `method_transfer` | IEEE 754 arithmetic method transfer 到 H3/DGGS geospatial transform | ZKLP §4 | active_seed |
| `numerical_soundness` | 与 H3/IEEE 754 数值语义一致可避免 fixed-point mismatch | ZKLP §1, §5.2 | active_seed |
| `dependency` | ZKLP 的 utility/completeness 依赖准确 floating-point operations | ZKLP Abstract, §1.1 | active_seed |

## Transfer Matrix

| From floating-point SNARKs | Transfers to location proofs? | How | Boundary |
| --- | --- | --- | --- |
| IEEE 754 representation | yes | 经纬度和 H3 transform 使用 FP32/FP64 语义 | only as accurate arithmetic layer |
| Correct rounding | yes | 与 existing geospatial libraries 输出保持一致 | rounding correctness does not prove physical location |
| Lookup range checks | yes | 降低 range/shift/comparison cost | lookup overhead/backend-specific |
| Nondeterministic hints | yes | sqrt/division/trig-derived values 可由 hints 计算并验证 | hint predicates must be sound |
| Trigonometric elimination | yes | 用恒等式和 half-angle hints 避免直接三角函数电路 | application-specific, not a general trig SNARK |
| TestFloat compliance | partially | 支撑 primitive FP operation correctness | not a proof of full H3 implementation equivalence beyond tested cases |
| Location provenance | no | outside arithmetic layer | requires Appendix C-style sources |

## Non-Transfer Boundary

- Accurate floating-point arithmetic does not authenticate the source of latitude/longitude.
- ZKLP's P2P proximity policy depends on resolution, cell boundary and application semantics.
- FP64 passing H3 tests in ZKLP does not automatically prove all geospatial libraries are safe.
- Groth16/Plonk proof size and verification properties transfer from backend assumptions, not from floating-point arithmetic itself.
- Future ML use is only suggested by the ZKLP discussion and must not be treated as absorbed zkML evidence.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]] Abstract/§1 | location privacy proof goal and IEEE 754 circuit need | source-authored framing |
| ZKLP §3 | primitive FP circuits and edge-case handling | backend/circuit implementation specific |
| ZKLP §4 | H3/DGGS transform and trigonometric elimination | application-specific route |
| ZKLP §5.1 | TestFloat compliance and primitive operation constraints | test suite, not formal proof of all software libraries |
| ZKLP §5.2 | end-to-end Groth16/Plonk constraints, prover time, FP64 correctness | empirical results |
| ZKLP Appendix C | authenticity gap and possible provenance integrations | future routes, not implemented main protocol |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[floating-point-snarks|Floating-point SNARKs]] | Create method-family node and attach ZKLP as representative source | done |
| [[privacy-preserving-location-proofs|Privacy-preserving location proofs]] | Create application problem node and attach ZKLP as representative source | done |
| [[applications|ZKP applications]] | Add location privacy proof child route | done |
| [[proof-systems|Proof systems]] | Add floating-point SNARKs child route | done |
| [[zk-snarks|zk-SNARKs]] | Add floating-point arithmetic as source extension, not foundation replacement | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-floating-point-snarks | applies_to | nahida-knowledge-privacy-preserving-location-proofs | ZKLP §4-§5 | high | active_seed |
| nahida-knowledge-privacy-preserving-location-proofs | uses | nahida-knowledge-floating-point-snarks | ZKLP §3-§4 | high | active_seed |
| nahida-knowledge-floating-point-snarks | bridges_to | nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs | bridge note | high | active_seed |
| nahida-knowledge-privacy-preserving-location-proofs | bridges_to | nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs | bridge note | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| Location provenance source absorbed | Separate authenticity layer from arithmetic/application layer | `nahida-update` |
| Floating-point ZKP prior work absorbed | Calibrate novelty and method-family comparison | `nahida-research-search` or `nahida-update` |
| ZKML floating-point source absorbed | Decide whether to bridge floating-point SNARKs to verifiable inference | `nahida-update` |
| H3/DGGS primary source absorbed | Strengthen geospatial endpoint assumptions | `nahida-research-search` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zklp-floating-point-snarks | Created bridge from floating-point SNARKs to privacy-preserving location proofs using ZKLP as first source-backed transfer. | 1 source note | codex |
