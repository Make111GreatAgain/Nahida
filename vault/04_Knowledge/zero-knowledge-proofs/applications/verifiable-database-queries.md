---
id: "nahida-knowledge-verifiable-database-queries"
title: "Verifiable database queries"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "verifiable-database-queries"
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
parent_knowledge_refs:
  - "nahida-knowledge-zkp-applications"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "applications"
  - "verifiable-database-queries"
primary_ontology_path: "zero-knowledge-proofs/applications/verifiable-database-queries"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases"
  - "verifiable-computation/verifiable-computation-systems"
relation_edges:
  - from: "nahida-knowledge-verifiable-database-queries"
    relation: "is_a"
    to: "nahida-knowledge-zkp-applications"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/verifiable-database-queries.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-database-queries"
    relation: "depends_on"
    to: "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
      - "vault/05_Bridges/zero-knowledge-sets-to-verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-database-queries"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-database-queries"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-database-queries"
    relation: "bridges_to"
    to: "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
    evidence_refs:
      - "vault/05_Bridges/zero-knowledge-sets-to-verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-database-queries"
    relation: "bridges_to"
    to: "nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries"
    evidence_refs:
      - "vault/05_Bridges/privacy-preserving-database-queries-to-verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
  - "nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
  - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
representative_source_refs:
  - "iacr:2023/156"
  - "doi:10.14778/3594512.3594513"
query_keys:
  - "Verifiable database queries"
  - "verifiable database"
  - "zero-knowledge database queries"
  - "private database queries"
  - "ZK-FEDB"
  - "ZK-EDB"
  - "ZKSQL"
  - "zero-knowledge SQL"
  - "authenticated SQL queries"
  - "operator-at-a-time proofs"
  - "private aggregate queries"
  - "functional queries over committed databases"
aliases:
  - "zero-knowledge database queries"
  - "private verifiable database queries"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "verifiable-database-queries"
  - "zero-knowledge-elementary-databases"
  - "functional-database-queries"
  - "private-query-processing"
  - "zero-knowledge-sql"
  - "authenticated-query-evaluation"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-zk-functional-elementary-databases"
  - "nahida-knowledge-20260623-private-aggregate-queries"
  - "nahida-knowledge-20260623-zksql"
source_refs:
  - "iacr:2023/156"
  - "doi:10.14778/3594512.3594513"
confidence: "medium"
trust_tier: "primary"
---

# Verifiable database queries

## 定义与范围

- 定义: Verifiable database queries 研究如何让 prover/server 对已承诺、外包或私有数据库回答查询，并让 verifier/client 确信返回结果正确、完整，同时在需要时隐藏未返回记录、数据库大小或 witness 信息。
- 不包含: 普通数据库事务、并发控制、存储引擎、SQL optimizer、区块链关系数据库执行层；这些属于 database systems 或 blockchain execution。这里关注的是 query answer 的 cryptographic correctness/privacy。
- Canonical terms: `verifiable database queries`, `zero-knowledge database queries`, `private verifiable database queries`
- Standalone completeness check: 本节点给出本地定义、问题、方法族、代表 source、桥接和边界；链接用于深入，不作为唯一解释。
- Retrieval role: 以后查询 ZK-FEDB、ZKSQL、private aggregate queries、committed database query proof 时，从本节点理解问题层，再进入具体 source。
- Update scope: 新 source 若改变 query model、privacy boundary、proof-system dependency、application route 或 SQL/aggregate coverage，应刷新本节点。

## 背景

数据库查询的可验证性不只要求“返回的 rows 满足谓词”，还要求“没有漏掉满足谓词的 rows”。在零知识或私有查询场景中，还要隐藏未返回 rows、数据库大小、witness/intermediate state，甚至只暴露查询结果本身。

当前 source-backed seed 是 [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]]。它从 ZK-EDB 的点查询出发，指出 range-query ZK-EEDB 仍不能支持一般 predicate，于是定义 ZK-FEDB: 对任意布尔电路 `f(x,v)` 返回所有满足记录，并证明完整性与零知识。[[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] 新增 SQL/operator-at-a-time route: 对私有关系数据库先 commitment，再按 SQL query plan 的 Project、Filter、Sort、Join、Aggregate 等 operator 证明 answer 正确完整，同时隐藏输入记录和中间结果；但 schema、table cardinalities、query、query DAG 和最终 answer 是公开的。[[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] 是相邻但不同的问题: 它隐藏用户查询和参与聚合的记录集合，不证明数据库回答正确完整；因此通过 bridge 连接，而不是作为本节点的直接 evidence。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它可以承接 ZK-FEDB、ZKSQL、key transparency queries、authenticated/zero-knowledge database commitments 等多类 source；private aggregate queries 作为 query privacy 邻域通过 bridge 连接。
- 为什么不是单篇论文/单个协议: ZK-FEDB 是当前代表路线；本节点组织的是“私有/可验证数据库查询”问题域。
- 需要引用的更基础 Knowledge: [[applications|ZKP applications]], [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]], [[proof-systems|Proof systems]]。
- 不应拆出的实例/协议/来源: ZK-FEDB、ZKSQL、zk-vSQL、single SQL benchmark 默认作为 source/system instances，除非多来源证明需要独立问题节点。

## 解决的问题

| Problem | Why it matters | Example route |
| --- | --- | --- |
| Query correctness | 返回记录必须满足查询谓词。 | 对每个 returned `(x,v)` 证明 `D(x)=v` 且 bit-subset consistency。 |
| Query completeness | 不能漏掉满足谓词的 records。 | 把 Boolean predicate 转换为 support set operation，并证明 output support 正确。 |
| Database-size hiding | 不能通过 witness length 或 proof size 泄露数据库大小。 | ZK-FEDB 避免 naive SNARK 全库 witness route，证明大小与 `|D|` 无关。 |
| Query expressiveness | 点查询和范围查询不足以表达通用应用需求。 | 用 Boolean circuit `f(x,v)` 表达 arbitrary functional query。 |
| SQL query answer integrity | Ad-hoc SQL 需要证明 plan/operator pipeline 的输出正确完整，而不是只证明每条返回 row 满足谓词。 | ZKSQL 用 commit-and-prove、circuit-based Project/Filter/Aggregate 与 set-based Sort/Join 组合。 |
| Application fit | 查询模型需要匹配 key transparency、SQL、aggregate 或 audit 场景。 | 当前直接 source 覆盖 elementary database functional queries 与 SQL operator pipeline；aggregate/query-privacy 仍通过 bridge 区分。 |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[applications|ZKP applications]] | child_of | ZK-FEDB is a concrete ZKP application problem over committed databases | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Point-query ZK-EDB | 证明 key 的 value 或不存在性。 | key-value lookup。 | 表达力弱，不能回答 general predicate。 | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| Range/expressive EDB | 支持 key/value range 和简单组合。 | 查询能表示为 range conditions。 | 对一般 Boolean predicate 不够。 | mentioned in [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| Functional EDB via set operations | 将 `f(x,v)` 转换成 bit-position sets 上的 union/intersection/difference circuit。 | fixed-length records, Boolean-circuit predicates, committed support sets。 | Prover work 与 `|D|` 和 `|f|` 相关；依赖 ZKS set-operation machinery。 | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| Operator-at-a-time ZKSQL | 把 SQL query plan 拆成 operator pipeline；对 Project/Filter/Aggregate 用 circuit route，对 Sort/Join 用 polynomial set-operation route 证明 multiset equality、order、membership 和 join completeness。 | schema、cardinality、query/DAG 和 answer 可公开；需要验证私有输入记录与中间结果不泄露。 | 不隐藏 query/access pattern；实现只覆盖 two-way equi-join，浮点和 string pattern matching 有实验限制；padding 会带来高开销。 | [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] |
| SNARK/lookup baseline | 用通用 ZK proof 证明 returned rows satisfy query and membership。 | 可以接受 witness size leakage 或另有 size-hiding/completeness design。 | Naive route 需要证明剩余数据库不满足 predicate，容易泄露 database size。 | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| Key transparency query extension | 把 append-only ZK-FEDB 用于 richer public-key directory search。 | 目录服务需要可审计且隐私友好的灵活查询。 | 当前只作为应用示例，缺生产系统 source。 | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] |
| Query-privacy complement | 将 PIR/private aggregate query 的 access privacy 与 verifiable query 的 answer integrity 分开建模。 | 系统需要同时隐藏查询意图并验证回答时。 | PIR 隐私不自动提供 correctness/completeness；ZK correctness 不自动隐藏 access pattern。 | [[privacy-preserving-database-queries-to-verifiable-database-queries|Privacy-preserving database queries -> verifiable database queries]] |

## 当前综合

- Evidence window: `2026-06-23`，仅覆盖当前已吸收 source。
- Freshness: `fresh` for current-vault synthesis; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前节点是 `foundation_thin`。ZK-FEDB 提供一个清晰的 source-backed seed: verifiable database query 的核心难点是 correctness + completeness + size hiding 的组合，而不是单纯的 predicate satisfaction。ZKSQL 把同一问题推进到 ad-hoc SQL query evaluation: 它不是证明一个 monolithic DBMS trace，而是沿 SQL operator pipeline 维护 authenticated intermediate results，并用 set-based polynomial protocols 降低 sort/join 证明成本。与 zk-vSQL 这类“把计算验证协议零知识化”的路线不同，ZK-FEDB 和 ZKSQL 都直接把数据库查询语义作为对象；与 Private Aggregate Queries 相比，ZKSQL 增强 answer correctness/completeness，但仍不提供 query privacy 或 access-pattern privacy。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]] | 创建 verifiable database queries 问题节点；新增 arbitrary Boolean-circuit functional query route；纠正队列的 distributed-transactions 分类 | 定义与范围; 解决的问题; 方法族; 当前综合; Bridge Links | yes | 后续吸收 ZKSQL 和 private aggregate query papers 后校准 SQL/aggregate 分支 |
| [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] | 作为相邻 query-privacy source 创建 bridge，明确 PIR aggregate privacy 不等于 verifiable query correctness/completeness。 | 背景; 方法族; 当前综合; Bridge Links; 缺口与队列 | no for this node | 后续若出现同时支持 privacy + verifiability 的系统，再评估是否拆 hybrid node |
| [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] | 新增 SQL/operator-at-a-time verifiable query route，并纠正队列的 distributed-transactions 分类。 | 背景; 解决的问题; 方法族; 当前综合; Bridge Links; 缺口与队列 | no | 后续补 zk-vSQL/vSQL/SQL proof foundations 与 query privacy + verifiability hybrid systems |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zero-knowledge-sets-to-verifiable-database-queries|Zero-knowledge sets -> verifiable database queries]] | `zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases; zero-knowledge-proofs/applications/verifiable-database-queries` | dependency, method_transfer, application | ZKS set-operation proofs provide query support completeness; SQL planning, transaction isolation and storage execution do not transfer. | active_seed |
| [[privacy-preserving-database-queries-to-verifiable-database-queries|Privacy-preserving database queries -> verifiable database queries]] | `distributed-systems/data-management-and-storage/privacy-preserving-database-queries; zero-knowledge-proofs/applications/verifiable-database-queries` | complement, boundary, privacy_vs_integrity | PIR hides what is queried; verifiable queries prove answer correctness/completeness. ZKSQL strengthens the correctness side for SQL but still leaves query/access privacy outside scope. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-verifiable-database-queries | is_a | nahida-knowledge-zkp-applications | this note | high | active_seed |
| nahida-knowledge-verifiable-database-queries | depends_on | nahida-knowledge-zero-knowledge-sets-and-elementary-databases | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB paper]] | high | active_seed |
| nahida-knowledge-verifiable-database-queries | evidenced_by | vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md | source note | high | active_seed |
| nahida-knowledge-verifiable-database-queries | evidenced_by | vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md | [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL source note]] | high | active_seed |
| nahida-knowledge-verifiable-database-queries | bridges_to | nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries | [[privacy-preserving-database-queries-to-verifiable-database-queries|bridge note]] | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| SQL route now has only one direct ZKSQL seed | Need compare ZKSQL with vSQL/zk-vSQL, authenticated SQL databases, richer joins/floats/string predicates and query optimizer foundations | nahida-update | high | partially_closed |
| Hybrid private-and-verifiable aggregate query sources pending | Need systems that combine query/access privacy with correctness/completeness proofs | nahida-update | high | queued |
| Foundational ZKS/ZK-EEDB sources not directly absorbed | Current history and range-query baseline are mediated by ZK-FEDB paper | nahida-research-search / nahida-update | medium | queued |
| Real database-system boundary thin | Need source-backed distinction between cryptographic query proof and database execution/storage systems | nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-zk-functional-elementary-databases | Created problem node from ZK-FEDB source; corrected classification from distributed transactions to ZKP application. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-private-aggregate-queries | Added bridge boundary to privacy-preserving database queries; private aggregate query source is adjacent, not direct evidence for verifiable query correctness. | 1 source note + bridge | codex |
| 2026-06-23 | nahida-knowledge-20260623-zksql | Added ZKSQL as SQL/operator-at-a-time verifiable database query route; corrected queue classification away from distributed transactions. | doi:10.14778/3594512.3594513 | codex |
