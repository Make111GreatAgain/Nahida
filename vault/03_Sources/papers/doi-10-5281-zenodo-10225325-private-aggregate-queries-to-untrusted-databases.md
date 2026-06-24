---
id: "doi-10-5281-zenodo-10225325-private-aggregate-queries-to-untrusted-databases"
title: "Private Aggregate Queries to Untrusted Databases"
type: "source"
source_type: "paper"
source_kind: "pdf"
source_subtype: "paper_local"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
safe_for_absorption: true
trust_tier: "primary"
source_identity:
  type: "doi"
  key: "doi:10.5281/zenodo.10225325"
source_refs:
  - "doi:10.5281/zenodo.10225325"
  - "arxiv:2403.13296v1"
  - "sha256:2d5deae671ebb6742ce1d4f0c06b5575d546d16ee9de0d498b45eb932da87557"
  - "filename:2403.13296v1.pdf"
representative_source_refs:
  - "doi:10.5281/zenodo.10225325"
  - "arxiv:2403.13296v1"
authors:
  - "Syed Mahbub Hafiz"
  - "Chitrabhanu Gupta"
  - "Warren Wnuck"
  - "Brijesh Vora"
  - "Chen-Nee Chuah"
year: "2024"
doi: "10.5281/zenodo.10225325"
arxiv_id: "2403.13296v1"
canonical_url: "https://doi.org/10.5281/zenodo.10225325"
venue: "NDSS Symposium 2024 / arXiv preprint / Zenodo artifact"
local_pdf: "~/Desktop/paper/2403.13296v1.pdf"
pdf_sha256: "2d5deae671ebb6742ce1d4f0c06b5575d546d16ee9de0d498b45eb932da87557"
extracted_text_path: "vault/02_Raw/pdf/extracted/private-aggregate-queries-to-untrusted-databases-2d5deae671eb-pages.txt"
pages: 20
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
primary_ontology_path: "distributed-systems/data-management-and-storage/privacy-preserving-database-queries"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/verifiable-database-queries"
domains:
  - "distributed-systems"
  - "zero-knowledge-proofs"
topics:
  - "privacy-preserving-database-queries"
  - "private-information-retrieval"
  - "private-aggregate-queries"
  - "information-theoretic-pir"
  - "aggregate-query-indexes"
  - "database-query-privacy"
topic_ids:
  - "privacy-preserving-database-queries"
  - "private-information-retrieval"
  - "private-aggregate-queries"
  - "aggregate-query-indexes"
query_keys:
  - "Private Aggregate Queries to Untrusted Databases"
  - "private aggregate queries"
  - "information-theoretic PIR aggregate queries"
  - "indexes of aggregate queries"
  - "IAQ"
  - "query privacy for aggregate database queries"
  - "SUM COUNT MEAN histogram PIR"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Local PDF deep read pages 1-20."
  - "Abstract and Section IV define an IT-PIR framework for private aggregate queries, not transaction commit or concurrency control."
  - "The core construction uses standard aggregate vectors, indexes of aggregate queries, Shamir secret sharing and polynomial batch coding."
  - "Evaluation targets query throughput and server response generation for MIMIC3, Twitter and Yelp aggregate queries."
  - "The queued distributed-transactions path was too narrow and wrong; the paper belongs under privacy-preserving database queries."
parent_knowledge_refs:
  - "nahida-knowledge-privacy-preserving-database-queries"
  - "nahida-knowledge-data-management-and-storage"
bridge_refs:
  - "nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries"
related_paths:
  - "vault/04_Knowledge/distributed-systems/data-management-and-storage/privacy-preserving-database-queries.md"
  - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/applications/verifiable-database-queries.md"
  - "vault/05_Bridges/privacy-preserving-database-queries-to-verifiable-database-queries.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0093"
queue_rank: 93
run_ids:
  - "nahida-knowledge-20260623-private-aggregate-queries"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# Private Aggregate Queries to Untrusted Databases

## Paper Identity

| Field | Value |
| --- | --- |
| Title | Private Aggregate Queries to Untrusted Databases |
| Authors | Syed Mahbub Hafiz; Chitrabhanu Gupta; Warren Wnuck; Brijesh Vora; Chen-Nee Chuah |
| Year | 2024 |
| Venue/status | Accepted at NDSS Symposium 2024; arXiv preprint `2403.13296v1`; artifact DOI `10.5281/zenodo.10225325` |
| Local PDF | `~/Desktop/paper/2403.13296v1.pdf` |
| Source key | `sha256:2d5deae671ebb6742ce1d4f0c06b5575d546d16ee9de0d498b45eb932da87557` |
| Pages | 20 |
| Extracted text | `vault/02_Raw/pdf/extracted/private-aggregate-queries-to-untrusted-databases-2d5deae671eb-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Absorption run: `nahida-knowledge-20260623-private-aggregate-queries`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0093`
- Queue title: `Private Aggregate Queries to Untrusted Databases*`
- Classification correction: 队列把它放在 `distributed-systems/data-management-and-storage/distributed-transactions`。精读后修正为 [[privacy-preserving-database-queries|Privacy-preserving database queries]]，因为论文解决的是不可信数据库主机下的聚合查询隐私，而不是事务提交、隔离或并发控制。
- External fetch: not performed. DOI, arXiv id, GitHub artifact URL and artifact DOI are recorded from local PDF metadata/text.

## 一句话贡献

这篇论文把多服务器 information-theoretic PIR 从“按位置私取单条记录”扩展到“按语义条件私取聚合结果”: 用户可以在单轮交互中提交 SUM、COUNT、MEAN、histogram、MIN/MAX 等聚合查询，同时让不可信数据库服务器不知道查询条件和哪些记录参与聚合。

## 章节地图

| Section | 内容 | 对知识库的作用 |
| --- | --- | --- |
| Abstract, I | 聚合查询会泄露用户兴趣；传统 PIR 多要求已知行号且不适合复杂聚合；本文构造支持搜索/过滤/聚合的 IT-PIR 框架。 | 建立 [[privacy-preserving-database-queries|Privacy-preserving database queries]] 问题节点。 |
| II | 威胁模型: 数据库主机不可信、可观察查询/服务器计算/扫描行；假设最多 `t` 个 PIR 服务器串通。 | 记录 privacy guarantee 的适用边界。 |
| III | 背景: vector-matrix PIR、Shamir secret sharing、polynomial batch coding、index of queries。 | 解释为什么线性结构能支撑聚合。 |
| IV | 定义 standard aggregate vector、index of aggregate queries、batch index of aggregate queries，并说明 SUM/COUNT/histogram/MIN/MAX/MEAN。 | 核心方法。 |
| V | Benchmark 与 MIMIC3、Twitter、Yelp case studies；比较 Goldberg IT-PIR baseline 与 Splinter。 | 记录性能与适用场景。 |
| VI-VII | 数据库更新、最小配置、Byzantine robustness、大库与 CPU 实验。 | 记录工程边界和容错扩展。 |
| VIII | Related work: Splinter、secure aggregation、COEUS、SSE、ORAM、oblivious datastores。 | 支撑方法族位置。 |
| IX, Appendix | 结论、artifact 附录、安全证明。 | 记录可复现实验与 `t`-privacy 证明。 |

## 解决的问题

用户查询数据库的内容本身可能敏感。即使数据库内容是公开或可共享的，数据库主机也可能通过用户查询的关键词、过滤条件、访问模式和聚合对象推断政治偏好、健康状况、商业意图等信息。

传统 PIR 可以隐藏用户访问哪一条记录，但常见形式要求用户知道目标记录的物理位置，并且主要返回单个 block。现实的数据分析查询通常是语义查询: 例如按用户、地区、住院类型或政治账号过滤后求 SUM、COUNT、MEAN、histogram、MIN/MAX。这类查询不能简单地用单条 positional query 表达。

论文的问题陈述可以压缩为: 如何在不可信数据库主机和多服务器非串通假设下，让用户以单轮交互获得复杂聚合结果，同时隐藏敏感查询条件和参与聚合的记录集合。

## 核心方法

### Vector-matrix IT-PIR 基底

论文沿用 Goldberg IT-PIR 的 vector-matrix model。数据库 `D` 被视为 `r x s` 矩阵，普通 positional PIR 用标准基向量 `e_i` 取出第 `i` 条记录。隐私来自 Shamir `(t+1, l)` threshold secret sharing: 用户把查询向量按分量分享给多个服务器，少于等于 `t` 个服务器串通不能恢复查询。

这个基底的重要性质是线性: 查询向量与数据库矩阵相乘可以被秘密分享、服务器端矩阵乘法和客户端插值恢复组合起来。因此，如果查询向量不是 one-hot，而是多个位置为 1 的向量，就可以返回多条记录的逐列线性聚合。

### Standard aggregate vector

论文定义 standard aggregate vector `e_I`: 对索引集合 `I` 中的多个位置取 1，其余位置为 0。`e_I * D` 得到集合 `I` 中记录的逐列加和。

这一步把 PIR 从“取一条记录”扩展到“取一组记录的线性聚合”。如果再把数据库列设计成 count id、数值列或必要属性，就可以构造 SUM、COUNT、MEAN 和 histogram 的基础。

### Indexes of aggregate queries

仅有 aggregate vector 还不够，因为用户仍需要知道哪些行属于条件集合。论文引入 index of aggregate queries (IAQ): 每一行都是一个 standard aggregate vector，每一列对应数据库记录。IAQ 的每一行表示某个查询条件值或聚合桶对应的记录集合。

用户只需要构造一个维度为 `p` 的标准基向量，其中 `p` 是 IAQ 的行数，也就是搜索项/条件值数量。服务器把秘密分享的查询向量乘以 IAQ，再乘以数据库矩阵，返回可重构的聚合结果。这样，用户不需要知道数据库物理行号，只需要知道要查询的语义 keyword/类别。

### Polynomial batch coding

如果服务器直接存储许多 IAQ，攻击者可能通过观察选择了哪个 index 推断查询类别。论文使用 polynomial batch coding 把多个 IAQ 合并为 batch index of aggregate queries。每个服务器持有多项式在不同点的 evaluation bucket，用户把目标 query vector 编码到指定点，客户端重构时恢复目标聚合结果。

这个机制有两个效果:

- 降低多个索引的存储/通信/计算成本。
- 让查询都经过同一个 batch index，减少“选择了哪个索引”造成的信息泄露。

### 支持的查询类型

| Query type | 实现方式 | 额外处理 |
| --- | --- | --- |
| SUM | IAQ 行选择满足条件的记录集合，对目标数值列求和。 | 数据库需保留可加字段。 |
| COUNT | 对 categorical id 或辅助 count 字段求聚合，再做简单后处理。 | 非数值分类字段可能需要 master table / id preprocessing。 |
| Histogram | 批处理多个 COUNT query，每个桶一个 query vector。 | 用户把多个 count queries 合成一个请求。 |
| MIN/MAX | 使用按目标列排序/选择的 simple indexes of queries。 | 对 GROUP BY 场景可先取 histogram 再本地排序。 |
| MEAN | 批处理 SUM 和 COUNT 两个查询，客户端本地相除。 | 需要同时返回分子和分母。 |

## 威胁模型与安全边界

- 数据库主机/服务器可观察查询、服务器计算和扫描行为，是 honest-but-curious/passive adversary。
- 基本安全性依赖多服务器 IT-PIR 的非串通阈值假设: 最多 `t` 个服务器串通。
- 单个 IAQ 与 `u`-batch IAQ 都保持 `t`-privacy；批处理场景下用户需要至少 `t+u` 个服务器正确响应才能重构结果。
- 论文说明可继承 Devet-Goldberg-Heninger 风格的 vector-matrix IT-PIR Byzantine robustness，使协议在最多 `v` 个服务器 Byzantine failure/collusion 下仍可恢复正确输出。
- 它隐藏的是查询/访问模式和参与聚合的记录集合，不自动证明数据库主机返回的业务数据来自正确、最新或未篡改数据库状态；这一点需要和 [[verifiable-database-queries|Verifiable database queries]] 区分。
- 协议保护 read access patterns，不保护 write patterns。

## 实验与性能记录

| 实验/场景 | 设置 | 结果/结论 |
| --- | --- | --- |
| Benchmark over database rows | `r` 从 `2^14` 到 `2^24`，`p=2^16`，batch `u=6`。 | 数据库超过 1600 万行时，GPU 上仍能支持约 4000 queries/s。 |
| Benchmark over IAQ rows | `p` 从 `2^1` 到 `2^17`，`r=2^20`。 | `p` 增大到高位后 throughput 明显下降；query length 由搜索项数量决定。 |
| Aggregation width | 聚合记录数从 `2^1` 到 `2^11`。 | 聚合记录数增大降低 throughput，约 512 行聚合时仍约 4000 queries/s。 |
| MIMIC3 | Admissions/Prescription 表，urgent admission、ethnicity、dosage、stay duration 等。 | IAQ 生成通常秒级，较大 filtered MIMIC3 query server response 约 0.10-0.26s；Goldberg baseline 可到 7.37s。 |
| Twitter | 约 100 万政治相关 tweets；按用户聚合 likes/retweets/mean/histogram。 | 未过滤 Twitter query all attributes 约 1.13s，essential attributes 约 0.45s；过滤后可到 0.01s。 |
| Yelp / Splinter comparison | 重现 Splinter Yelp aggregate query 子集。 | 简单 restaurant type query Splinter 更快；复杂 highest rated query 本协议更快。 |
| 40/64 GiB augmented databases | Twitter filtered / MIMIC3 filtered，比较多种 modulus。 | GF(2^8) 下 Twitter 40 GiB 约 0.1s vs baseline 16.8s；MIMIC3 40 GiB 约 0.6s vs baseline 17.5s。 |
| CPU VspM | 基础 NTL CPU 实现，无并行/汇编优化。 | CPU throughput 下降明显，但 server response generation 不一定成为瓶颈。 |

## Artifact

论文附录记录 artifact:

- GitHub: `https://github.com/smhafiz/private_queries_it_pir/tree/v1.0.0`
- Artifact DOI: `https://doi.org/10.5281/zenodo.10225325`
- Manual: `AE_Doc_Revised.pdf`
- Dependencies: GMP, NTL, Socket++, Percy++, CUDA for GPU benchmarking.
- Raw datasets不完全包含在 artifact 中，但 case study 所需 IAQ indexes 以 CCS 格式提供。

## 贡献与边界

| 贡献 | 说明 | 知识库吸收位置 |
| --- | --- | --- |
| Private aggregate query problem | 把 PIR 从单条记录访问扩展到语义过滤后的聚合结果。 | [[privacy-preserving-database-queries|Privacy-preserving database queries]] |
| Standard aggregate vectors | 用多个 1 的查询向量线性聚合多条记录。 | [[privacy-preserving-database-queries|Privacy-preserving database queries]] |
| Indexes of aggregate queries | 把语义查询条件映射到参与聚合的记录集合。 | [[privacy-preserving-database-queries|Privacy-preserving database queries]] |
| Polynomial-batched IAQ | 同时降低多索引成本和索引选择泄露。 | [[privacy-preserving-database-queries|Privacy-preserving database queries]] |
| Privacy/verifiability boundary | PIR 隐藏查询和访问集合，但不等价于结果正确性/完整性证明。 | [[privacy-preserving-database-queries-to-verifiable-database-queries|Privacy-preserving database queries -> verifiable database queries]] |

重要边界:

- 非串通/阈值服务器假设是核心前提；单服务器数据库服务不能直接获得同等信息论隐私。
- IAQ 是离线构造的数据结构；新查询类型或数据库 schema 更新可能需要重新扫描/更新 index。
- 当前框架主要支持线性聚合和可由索引/批处理组合的查询；复杂 JOIN 是 future work。
- 性能结果依赖稀疏矩阵结构、字段选择、硬件和 modulus。
- 该论文不是 ZK-SQL 或 verifiable database paper；它不证明数据库回答的正确性/完整性，只隐藏用户查询和参与聚合记录。

## 层级候选分类

| Candidate | Decision | Reason |
| --- | --- | --- |
| `distributed-systems/data-management-and-storage/distributed-transactions` | reject | 没有 atomic commit、isolation、serializability、2PC/3PC 或 concurrency-control 内容。 |
| `distributed-systems/data-management-and-storage/privacy-preserving-database-queries` | accept primary | 论文主问题是数据库聚合查询的访问/条件隐私，系统对象是不可信数据库与多 PIR 服务器。 |
| `zero-knowledge-proofs/applications/verifiable-database-queries` | bridge only | 两者都处理数据库查询的 cryptographic boundary，但本论文是 PIR/access privacy，不是 ZK correctness/completeness proof。 |
| `cryptography/private-information-retrieval` | future possible parent | 当前 vault 还没有独立 cryptography/PIR domain；先放在数据管理方向下，并用 query keys 保留 PIR 入口。 |

## Knowledge Absorption Anchors

| Anchor | Target note | Update |
| --- | --- | --- |
| Aggregate query privacy | [[privacy-preserving-database-queries|Privacy-preserving database queries]] | Created problem node; added IAQ and IT-PIR method route. |
| Data management direction | [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | Added privacy-preserving query processing child. |
| Privacy vs verifiability | [[privacy-preserving-database-queries-to-verifiable-database-queries|Privacy-preserving database queries -> verifiable database queries]] | Created complement bridge. |
| Verifiable database queries | [[verifiable-database-queries|Verifiable database queries]] | Added bridge boundary: PIR query privacy is adjacent but not proof of answer correctness. |

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-private-aggregate-queries | Deep-read source note and absorbed into Source + Knowledge + Bridge architecture. | codex |
