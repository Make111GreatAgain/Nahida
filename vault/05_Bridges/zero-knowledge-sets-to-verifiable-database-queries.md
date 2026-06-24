---
id: "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
title: "Zero-knowledge sets -> verifiable database queries"
original_title: "Zero-knowledge sets -> verifiable database queries"
file_slug: "zero-knowledge-sets-to-verifiable-database-queries"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "dependency"
bridge_status: "active_seed"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases"
  - "zero-knowledge-proofs/applications/verifiable-database-queries"
endpoint_knowledge_refs:
  - "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
  - "nahida-knowledge-verifiable-database-queries"
from_domain: "zero-knowledge-proofs"
to_domain: "zero-knowledge-proofs"
from_direction: "proof-systems"
to_direction: "applications"
from_topic: "zero-knowledge-sets-and-elementary-databases"
to_topic: "verifiable-database-queries"
relation_types:
  - "dependency"
  - "method_transfer"
  - "application"
directionality: "source_to_target"
relationship_thesis: "Zero-knowledge set and elementary-database commitments provide the object language and query-proof machinery for private verifiable database queries; ZK-FEDB transfers set-operation proofs into arbitrary Boolean-circuit database selection while keeping proof size independent of input database size."
transferability: "high"
non_transfer_boundary: "The transferable object is cryptographic membership/non-membership and set-operation binding. It does not transfer SQL optimization, storage layout, transaction isolation, concurrency control, database replication, or key-transparency production operations."
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "zero-knowledge-sets"
  - "zero-knowledge-elementary-databases"
  - "verifiable-database-queries"
  - "functional-database-queries"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
knowledge_refs:
  - "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
  - "nahida-knowledge-verifiable-database-queries"
query_keys:
  - "Zero-knowledge sets -> verifiable database queries"
  - "ZKS to ZK-FEDB"
  - "set-operation ZKS database queries"
  - "functional elementary database bridge"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-zk-functional-elementary-databases"
source_refs:
  - "iacr:2023/156"
confidence: "high"
trust_tier: "primary"
---

# Zero-knowledge sets -> verifiable database queries

## Bridge Thesis

[[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] provide the committed-object primitive for [[verifiable-database-queries|Verifiable database queries]]. In the ZK-FEDB source, the transfer is not “use a generic SNARK for a database circuit”; it is “turn a database predicate into set operations over committed support subsets, then prove those set operations in zero knowledge”.

## Endpoints

| Endpoint | Role |
| --- | --- |
| [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] | Source primitive: membership, non-membership, key-value binding, set-operation queries |
| [[verifiable-database-queries|Verifiable database queries]] | Target problem: prove query answer correctness and completeness while hiding non-output data and database size |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Membership/non-membership proofs | Point lookup and support checks | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] Section 2 | Does not provide SQL semantics by itself. |
| Set-operation proofs | Completeness of selected output support | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] Section 4 | Requires relation-specific ZKS machinery; not ordinary ADS. |
| Boolean circuit to set-operation transform | Arbitrary functional query over fixed-length records | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] Section 5.2 | Works for circuit predicates over encoded records; query language usability remains separate. |
| Size-hiding proof route | Proof size independent of input database size | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] performance section | Prover time still depends on database size. |

## 不可迁移边界

- ZKS/EDB machinery does not imply transaction isolation, serializability, concurrency control or replicated database consistency.
- ZK-FEDB's functional query model does not automatically become SQL; SQL parsing, joins, aggregates, indexes and optimizer cost models need separate sources.
- Key transparency is an application sketch in the source, not a full production system guarantee.
- Generic zk-SNARK knowledge transfers only carefully: the source explicitly warns that naive SNARK witnesses can leak database size.

## Evidence

| Source | Evidence | Confidence |
| --- | --- | --- |
| [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]] | Defines ZK-FEDB, constructs set-operation ZKS, transforms Boolean circuit queries into set-operation queries and proves proof size independent of `|D|`. | high |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] | Bridge Links / 当前综合 | Exposes ZKS/EDB as reusable proof primitive for database queries. | active_seed |
| [[verifiable-database-queries|Verifiable database queries]] | Bridge Links / 方法族 | Connects functional query completeness to set-operation proof machinery. | active_seed |
| [[applications|ZKP applications]] | 下级结构 / 方法族 | Adds verifiable database queries as a reusable application problem. | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases` | update Proof systems child list and bridge refs | active_seed |
| `zero-knowledge-proofs/applications/verifiable-database-queries` | update ZKP applications child list and bridge refs | active_seed |

## 查询入口

- ZK-FEDB
- zero-knowledge database queries
- set-operation ZKS
- database-size hiding query proofs
- functional elementary databases

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: ZKSQL, private aggregate query, ADS/ZKS foundation sources, or implementation sources that change query expressiveness, privacy leakage, prover/verifier cost, or endpoint taxonomy.

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-zk-functional-elementary-databases | Created bridge from ZKS/EDB primitive layer to verifiable database query problem. | 1 source note | codex |
