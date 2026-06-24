---
id: "nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries"
title: "Privacy-preserving database queries -> verifiable database queries"
original_title: "Privacy-preserving database queries -> verifiable database queries"
file_slug: "privacy-preserving-database-queries-to-verifiable-database-queries"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "complement"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/data-management-and-storage/privacy-preserving-database-queries"
  - "zero-knowledge-proofs/applications/verifiable-database-queries"
endpoint_knowledge_refs:
  - "nahida-knowledge-privacy-preserving-database-queries"
  - "nahida-knowledge-verifiable-database-queries"
from_domain: "distributed-systems"
to_domain: "zero-knowledge-proofs"
from_direction: "data-management-and-storage"
to_direction: "applications"
from_topic: "privacy-preserving-database-queries"
to_topic: "verifiable-database-queries"
relation_types:
  - "complement"
  - "boundary"
  - "privacy_vs_integrity"
directionality: "bidirectional_boundary"
relationship_thesis: "Privacy-preserving database query systems such as PIR hide what the user asks and which records participate in an answer, while verifiable database query systems prove that the returned answer is correct and complete. These properties are complementary: query privacy does not imply answer integrity, and answer verifiability does not imply access-pattern privacy."
transferability: "medium"
non_transfer_boundary: "PIR/IAQ techniques transfer query-hiding and access-pattern privacy intuitions, not proof of database state, completeness, freshness, SQL semantics, transaction isolation or authenticated storage. ZK/ADS database-query proofs transfer correctness/completeness machinery, not the non-colluding multi-server IT-PIR access-privacy guarantee."
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
domains:
  - "distributed-systems"
  - "zero-knowledge-proofs"
topics:
  - "privacy-preserving-database-queries"
  - "verifiable-database-queries"
  - "private-aggregate-queries"
  - "query-correctness"
  - "query-privacy"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
  - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
  - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
knowledge_refs:
  - "nahida-knowledge-privacy-preserving-database-queries"
  - "nahida-knowledge-verifiable-database-queries"
query_keys:
  - "PIR versus verifiable database queries"
  - "private aggregate queries and ZK database queries"
  - "query privacy versus query correctness"
  - "access privacy and verifiable query completeness"
  - "ZKSQL query privacy boundary"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-private-aggregate-queries"
  - "nahida-knowledge-20260623-zksql"
source_refs:
  - "doi:10.5281/zenodo.10225325"
  - "arxiv:2403.13296v1"
  - "iacr:2023/156"
  - "doi:10.14778/3594512.3594513"
confidence: "high"
trust_tier: "primary"
---

# Privacy-preserving database queries -> verifiable database queries

## Bridge Thesis

[[privacy-preserving-database-queries|Privacy-preserving database queries]] and [[verifiable-database-queries|Verifiable database queries]] address adjacent but different trust failures.

Private aggregate query / PIR systems hide the user's query and access pattern from an untrusted database host. Verifiable database query systems prove that a server's answer is correct and complete with respect to a committed or authenticated database. ZKSQL is direct evidence for the latter in SQL settings: it proves SQL operator-pipeline answer integrity while leaving query text, query DAG, table cardinalities and final answer public. A system may need both, but neither property automatically implies the other.

## Endpoints

| Endpoint | Role |
| --- | --- |
| [[privacy-preserving-database-queries|Privacy-preserving database queries]] | Source problem: hide query condition, selected records and access pattern from untrusted database/PIR servers. |
| [[verifiable-database-queries|Verifiable database queries]] | Target/adjacent problem: prove returned records, aggregates or functional query outputs are correct and complete. |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Query/access privacy lens | Verifiable query systems should ask what the server learns from query text, access pattern and witness shape. | [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] | Does not prove the answer is computed from an authentic database. |
| Aggregate-query semantics | Verifiable database notes should distinguish aggregate result privacy from per-record selection correctness. | [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] | IAQ supports SUM/COUNT/MEAN/histogram; JOIN remains future work. |
| Correctness/completeness lens | PIR/private query systems should ask whether the server can return wrong or incomplete aggregates. | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] | ZK-FEDB proves functional selection over committed databases, not IT-PIR access privacy. |
| SQL answer-integrity route | Query-privacy systems that expose SQL-like analytics still need a separate proof that Project/Filter/Sort/Join/Aggregate results are correct and complete. | [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] | ZKSQL hides prover input records/intermediate results, not verifier query intent or access pattern. |
| Hiding boundary vocabulary | Separate query privacy, access-pattern privacy, result privacy, database-size hiding, answer correctness and answer completeness. | both source notes | These terms are not interchangeable. |

## 不可迁移边界

- IT-PIR `t`-privacy does not certify database freshness, provenance, answer completeness or absence of tampering.
- ZK/ADS query verification does not hide which query the user issued unless the query model specifically includes that privacy property.
- ZKSQL's zero-knowledge property protects input rows and intermediate results under public query/cardinality/answer assumptions; it is not a private SQL query or PIR protocol.
- Aggregate query privacy is not the same as zero-knowledge proof privacy: PIR hides user interest from database hosts; ZK hides witness/intermediate data while proving a statement.
- Neither endpoint automatically covers SQL optimizer behavior, transaction isolation, replicated database consistency or write-pattern privacy.

## Evidence

| Source | Evidence | Confidence |
| --- | --- | --- |
| [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries to Untrusted Databases]] | Defines IT-PIR aggregate queries over untrusted databases, hiding query conditions and contributing records while returning SUM/COUNT/MEAN/histogram/MIN/MAX results. | high |
| [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]] | Defines verifiable functional queries over committed elementary databases, emphasizing correctness, completeness and database-size hiding. | high |
| [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs]] | Defines verifiable SQL operator-pipeline proofs over private relational data, emphasizing answer correctness/completeness and input/intermediate zero-knowledge under public query/cardinality assumptions. | high |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[privacy-preserving-database-queries|Privacy-preserving database queries]] | Bridge Links / 当前综合 | Marks PIR aggregate queries as query/access privacy rather than result-verification machinery. | active_seed |
| [[verifiable-database-queries|Verifiable database queries]] | Bridge Links / 缺口与队列 | Replaces "private aggregate query pending" with an active boundary bridge. | active_seed |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | 下级结构 / 方法族 | Adds privacy-preserving query processing as a data-management child route. | active_seed |
| [[verifiable-database-queries|Verifiable database queries]] | 方法族 / 当前综合 | Adds ZKSQL as the SQL answer-integrity side of this bridge, without importing query privacy. | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/data-management-and-storage/privacy-preserving-database-queries` | update Data Management and Storage child list and source extensions | active_seed |
| `zero-knowledge-proofs/applications/verifiable-database-queries` | update Bridge Links and clarify complement boundary | active_seed |

## 查询入口

- private aggregate queries
- PIR versus ZK database queries
- query privacy versus answer correctness
- access-pattern privacy for aggregate SQL
- verifiable private database query boundary

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: private SQL/PIR source, authenticated aggregate query source, ORAM/SSE source, or any system combining query privacy with verifiable results.

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-private-aggregate-queries | Created bridge to distinguish/combine query privacy and verifiable database query correctness/completeness. | 2 source notes | codex |
| 2026-06-23 | nahida-knowledge-20260623-zksql | Added ZKSQL as SQL answer-integrity evidence and clarified that it does not provide query/access privacy. | doi:10.14778/3594512.3594513 | codex |
