---
id: "nahida-knowledge-privacy-preserving-database-queries"
title: "Privacy-preserving database queries"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "privacy-preserving-database-queries"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
parent_knowledge_refs:
  - "nahida-knowledge-data-management-and-storage"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "privacy-preserving-database-queries"
primary_ontology_path: "distributed-systems/data-management-and-storage/privacy-preserving-database-queries"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/verifiable-database-queries"
relation_edges:
  - from: "nahida-knowledge-privacy-preserving-database-queries"
    relation: "part_of"
    to: "nahida-knowledge-data-management-and-storage"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-preserving-database-queries"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-preserving-database-queries"
    relation: "bridges_to"
    to: "nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries"
    evidence_refs:
      - "vault/05_Bridges/privacy-preserving-database-queries-to-verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md"
representative_source_refs:
  - "doi:10.5281/zenodo.10225325"
  - "arxiv:2403.13296v1"
query_keys:
  - "Privacy-preserving database queries"
  - "private database queries"
  - "private aggregate queries"
  - "information-theoretic PIR"
  - "private information retrieval"
  - "indexes of aggregate queries"
  - "query access privacy"
  - "untrusted databases"
aliases:
  - "Private database queries"
  - "Private aggregate queries"
domains:
  - "distributed-systems"
topics:
  - "privacy-preserving-database-queries"
  - "private-information-retrieval"
  - "private-aggregate-queries"
  - "database-query-privacy"
  - "aggregate-query-indexes"
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
  - "nahida-knowledge-20260623-private-aggregate-queries"
source_refs:
  - "doi:10.5281/zenodo.10225325"
  - "arxiv:2403.13296v1"
confidence: "medium"
trust_tier: "primary"
---

# Privacy-preserving database queries

## 定义与范围

- 定义: Privacy-preserving database queries 研究用户如何向不可信数据库或查询服务请求数据、统计量或聚合结果，同时隐藏查询条件、访问模式、目标记录集合或其他会泄露用户意图的信息。
- 不包含: 普通 SQL optimizer、事务隔离、复制并发控制、存储引擎内部 layout；这些属于 database systems / transaction processing / storage engines。也不等同于 verifiable database queries，后者关注结果正确性和完整性证明。
- Canonical terms: `private database queries`, `private information retrieval`, `private aggregate queries`, `query access privacy`
- Standalone completeness check: 本节点给出问题定义、威胁模型、方法族、代表 source 和跨域边界；具体协议实例留在 source note。
- Retrieval role: 当查询 PIR、private aggregate SQL、untrusted database query privacy、IAQ、Splinter/SSE/ORAM 对比时，先进入本节点，再打开代表 source。
- Update scope: 新 source 若改变查询模型、隐私假设、聚合覆盖、server trust model、系统评估或和 verifiable query 的边界，应刷新本节点。

## 背景

数据库查询本身会泄露用户关注的对象。即使数据库记录是公开的，数据库主机仍可能通过用户搜索的关键词、过滤条件、访问记录、聚合对象和查询频率推断敏感信息。传统 PIR 解决“隐藏访问哪条记录”的问题，但很多实际分析任务不是按物理行号读取单条记录，而是按语义条件执行聚合查询。

当前 source-backed seed 是 [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries to Untrusted Databases]]。它把多服务器 IT-PIR 的 one-hot positional query 推广到 standard aggregate vectors 和 indexes of aggregate queries，使用户在单轮中获得 SUM、COUNT、MEAN、histogram、MIN/MAX 等聚合结果，同时隐藏查询条件和参与聚合的记录集合。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它可以容纳 PIR、function secret sharing private queries、private aggregate SQL、SSE/ORAM adjacent systems、oblivious datastores 和未来数据库查询隐私 source。
- 为什么不是单篇论文/单个协议: IAQ-based IT-PIR 是当前代表方案；本节点组织的是“查询隐私”问题域。
- 需要引用的更基础 Knowledge: [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]；跨域参照 [[verifiable-database-queries|Verifiable database queries]]。
- 不应拆出的实例/协议/来源: IAQ、Splinter、COEUS、具体 Yelp/Twitter/MIMIC case study 默认作为 source/system instances，除非后续多来源证明需要独立方法节点。

## 解决的问题

| Problem | Why it matters | Example route |
| --- | --- | --- |
| Access/query privacy | 数据库主机不应知道用户想查哪些记录或条件。 | Multi-server IT-PIR hides query vector shares from any `t` colluding servers. |
| Semantic query privacy | 用户不一定知道物理行号，只知道关键词、条件或聚合桶。 | Index of queries / index of aggregate queries maps semantic values to record sets. |
| Aggregate result retrieval | 分析型查询需要 SUM、COUNT、MEAN、histogram 等结果，而非单条 record。 | Standard aggregate vectors compute linear aggregation over selected records. |
| Index-selection leakage | 如果服务器能观察用户选了哪个 index，也会泄露查询类别。 | Polynomial batch coding puts multiple IAQs behind a shared batched index route. |
| Deployment assumptions | 隐私保证依赖多服务器非串通、阈值和数据库/index 更新模型。 | `t`-privacy and `t+u` reconstruction boundary. |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | child_of | Query privacy is a data-management problem over untrusted hosted databases, not a transaction-processing problem. | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Positional PIR | 用户隐藏要访问的物理记录位置。 | 用户知道 row/block index，查询目标简单。 | 难以表达语义过滤和复杂聚合。 | [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] background |
| Index of queries | 用预处理索引把关键词/条件映射到数据库行集合。 | 语义查询可提前索引，服务器可存储辅助结构。 | index 选择可能泄露查询类别；更新需要维护索引。 | Hafiz-Henry route as used in [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] |
| Standard aggregate vectors | 查询向量包含多个 1，线性聚合多条记录。 | 聚合可表示为逐列线性组合或后处理。 | 复杂 JOIN 仍是 future work；字段编码影响支持范围。 | [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] |
| Indexes of aggregate queries | 每一行代表一个聚合条件/桶，用户私下选择行并得到聚合结果。 | SUM、COUNT、MEAN、histogram、MIN/MAX 等分析查询。 | 需要离线扫描构造 IAQ；新查询类型可能要新 index。 | [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] |
| Polynomial-batched indexes | 把多个 index 编码为同一 batch index，隐藏 index selection 并降低成本。 | 多个同维度 IAQ 可批处理，多服务器 IT-PIR。 | 需要至少 `t+u` 个正确服务器响应；batching 有离线成本。 | [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] |
| Function secret sharing private queries | 把查询函数拆成多份给不同 provider。 | 多 provider 非串通，public/replicated data。 | 非串通假设严格；某些复杂 query 需要多轮。 | Splinter as related work in [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] |
| SSE/ORAM/oblivious datastore adjacent routes | 隐藏搜索或访问模式的不同系统路线。 | encrypted documents, access-pattern hiding, storage systems。 | SSE 有泄露 profile；ORAM 成本/客户端状态不同；不一定支持 aggregate SQL。 | Related work in [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries to Untrusted Databases]] | paper + artifact | 建立 private aggregate query seed；给出 standard aggregate vector、IAQ、batched IAQ 和 MIMIC/Twitter/Yelp 评估。 | 多服务器非串通/阈值假设；隐藏 query/access，不证明结果正确性；JOIN 是 future work。 | Abstract, §II-§VII, Appendix B-C |

## 当前综合

- Evidence window: `2026-06-23`，仅覆盖当前已吸收 source。
- Freshness: `fresh` for current-vault synthesis; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前节点是 `foundation_thin`。Private Aggregate Queries 提供一个强 seed: 数据库查询隐私不仅是“取哪一行”的 PIR，也包括“按什么语义条件聚合哪些记录”的隐私。IAQ 路线把查询语义提前编译成稀疏矩阵，使 online query length 主要取决于搜索项数量 `p`，而不是数据库行数 `r`。但是它的保证和 [[verifiable-database-queries|Verifiable database queries]] 互补: PIR 隐藏用户查询，ZK/ADS 路线证明服务器回答正确完整。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases|Private Aggregate Queries to Untrusted Databases]] | 创建 privacy-preserving database queries 问题节点；纠正队列的 distributed-transactions 分类；建立 query privacy vs verifiability bridge。 | 定义与范围; 解决的问题; 方法族; 当前综合; Bridge Links | yes | 后续吸收 ZKSQL/private SQL/PIR/SSE/ORAM source 后校准方法族 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[privacy-preserving-database-queries-to-verifiable-database-queries|Privacy-preserving database queries -> verifiable database queries]] | `distributed-systems/data-management-and-storage/privacy-preserving-database-queries; zero-knowledge-proofs/applications/verifiable-database-queries` | complement, boundary, privacy_vs_integrity | PIR query privacy hides what the user asks and which records aggregate; ZK/ADS verifiable queries prove answer correctness/completeness. Neither property automatically implies the other. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-privacy-preserving-database-queries | part_of | nahida-knowledge-data-management-and-storage | this note; source note | high | active_seed |
| nahida-knowledge-privacy-preserving-database-queries | evidenced_by | vault/03_Sources/papers/doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases.md | source note | high | active_seed |
| nahida-knowledge-privacy-preserving-database-queries | bridges_to | nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| PIR foundations not directly absorbed | 当前对 Chor/Goldberg/Hafiz-Henry 依赖通过本论文间接进入。 | `nahida-research-search` / future papers | medium | queued |
| SQL/JOIN privacy thin | 当前 source 支持多种 aggregate queries，但 JOIN 是 future work。 | `nahida-update` | high | pending_future_source |
| Result correctness/completeness missing | PIR 隐藏查询，但无法单独保证数据库回答正确完整。 | bridge to `verifiable-database-queries` | high | active_bridge |
| Deployment trust model needs more sources | 多服务器非串通、collusion mitigation、Byzantine robustness 的实践证据仍少。 | `nahida-research-search` | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-private-aggregate-queries | Created problem node from Private Aggregate Queries source; corrected classification from distributed transactions to privacy-preserving database queries. | 1 source note | codex |
