---
id: "eprint-2023-156-zero-knowledge-functional-elementary-databases"
title: "Zero-Knowledge Functional Elementary Databases"
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
  type: "pdf"
  key: "sha256:a61ca27d267c30a56ed577c491b4340201dead6bc9c68d9dd3e235ef5cd68b48"
source_refs:
  - "sha256:a61ca27d267c30a56ed577c491b4340201dead6bc9c68d9dd3e235ef5cd68b48"
  - "iacr:2023/156"
  - "filename:2023-156.pdf"
representative_source_refs:
  - "iacr:2023/156"
authors:
  - "Xinxuan Zhang"
  - "Yi Deng"
year: "2023"
doi: ""
arxiv_id: ""
canonical_url: "https://eprint.iacr.org/2023/156"
venue: "Cryptology ePrint Archive / local PDF"
local_pdf: "~/Desktop/paper/2023-156.pdf"
pdf_sha256: "a61ca27d267c30a56ed577c491b4340201dead6bc9c68d9dd3e235ef5cd68b48"
extracted_text_path: "vault/02_Raw/pdf/extracted/2023-156-a61ca27d267c-pages.txt"
pages: 43
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
primary_ontology_path: "zero-knowledge-proofs/applications/verifiable-database-queries"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases"
  - "zero-knowledge-proofs/proof-systems"
  - "verifiable-computation/verifiable-computation-systems"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "verifiable-database-queries"
  - "zero-knowledge-sets"
  - "zero-knowledge-elementary-databases"
  - "zero-knowledge-functional-elementary-databases"
  - "set-operation-queries"
  - "groups-of-unknown-order"
  - "key-transparency"
topic_ids:
  - "verifiable-database-queries"
  - "zero-knowledge-sets"
  - "zero-knowledge-elementary-databases"
  - "zk-functional-elementary-databases"
query_keys:
  - "Zero-Knowledge Functional Elementary Databases"
  - "ZK-FEDB"
  - "zero-knowledge functional elementary database"
  - "zero-knowledge elementary databases"
  - "ZK-EDB"
  - "zero-knowledge sets with set-operation queries"
  - "functional queries over committed databases"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The abstract and Section 1 define ZK-FEDBs for Boolean-circuit functional queries over committed key-value databases."
  - "Sections 4-5 construct ZKS with set-operation queries and use them to answer functional database queries."
  - "The performance claim targets proof size independent of input database size, not distributed transaction processing."
  - "The queued distributed-transactions path was too broad; database here means cryptographic elementary database, not concurrency control."
parent_knowledge_refs:
  - "nahida-knowledge-verifiable-database-queries"
  - "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
  - "nahida-knowledge-zkp-applications"
  - "nahida-knowledge-proof-systems"
bridge_refs:
  - "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
related_paths:
  - "vault/04_Knowledge/zero-knowledge-proofs/applications/verifiable-database-queries.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
  - "vault/05_Bridges/zero-knowledge-sets-to-verifiable-database-queries.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0084"
queue_rank: 84
run_ids:
  - "nahida-knowledge-20260623-zk-functional-elementary-databases"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# Zero-Knowledge Functional Elementary Databases

## Paper Identity

| Field | Value |
| --- | --- |
| Title | Zero-Knowledge Functional Elementary Databases |
| Authors | Xinxuan Zhang; Yi Deng |
| Year | 2023 |
| Local PDF | `~/Desktop/paper/2023-156.pdf` |
| Source key | `sha256:a61ca27d267c30a56ed577c491b4340201dead6bc9c68d9dd3e235ef5cd68b48` |
| ePrint identity | `iacr:2023/156` inferred from local filename and reference entry `[ZD23]` in the PDF |
| Pages | 43 |
| Extracted text | `vault/02_Raw/pdf/extracted/2023-156-a61ca27d267c-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Absorption run: `nahida-knowledge-20260623-zk-functional-elementary-databases`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0084`
- Queue title: `Zero-Knowledge Functional Elementary Databases`
- Classification correction: 队列把它暂放在 `distributed-systems/data-management-and-storage/distributed-transactions`。精读后修正为 [[verifiable-database-queries|Verifiable database queries]]，因为这里的 database 是 cryptographic elementary database，不是分布式事务或并发控制系统。
- External fetch: not performed. ePrint identity and URL are recorded from the local filename plus PDF reference list.

## 一句话贡献

这篇论文把零知识 elementary database 从点查询和范围查询扩展到任意布尔电路函数查询: prover 承诺 key-value database 后，可以证明并返回所有满足 `f(x, v) = 1` 的记录，同时不泄露额外信息，包括数据库大小，并且证明大小不依赖输入数据库大小。

## 章节地图

| Section | 内容 | 对知识库的作用 |
| --- | --- | --- |
| Abstract, 1 | 说明 ZK-EDB 只能支持点查询，既有 ZK-EEDB 主要支持 key/value 范围查询；本文定义 ZK-FEDB。 | 建立 [[verifiable-database-queries|Verifiable database queries]] 的问题增量。 |
| 1.2 | 技术概览: SNARK baseline 会泄露 witness length/database size；改用 randomized unknown-order-group ZKS 与 set-operation proofs。 | 记录为什么不是普通 zk-SNARK application。 |
| 2 | 定义 ZK-EDB、groups of unknown order、strong RSA、generic group model、PoKE 等基础。 | 支撑 [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]]。 |
| 3 | 构造 multidimensional DL variant、standard ZKS、pseudo-coprime 和 pseudo-DDH NIZK。 | 记录 set-operation ZKS 的证明组件。 |
| 4 | 定义并构造支持 set-operation queries 的 ZKS，覆盖 intersection、union、difference 和 combined operations。 | 把 ZKS 从 membership 扩展到 set algebra queries。 |
| 5.1 | 定义 ZK-FEDB: 对任意 Boolean circuit `f` 证明 `Doutput = D(f)`。 | 建立 functional database query 语义。 |
| 5.2 | 把 Boolean circuit query 转换为 union/intersection/difference 的 set-operation circuit。 | 核心转换方法。 |
| 5.3 | 用 ZK-EDB + set-operation ZKS 构造 ZK-FEDB，给出 function binding 和 zero-knowledge 证明。 | 连接 source 到知识节点和 bridge。 |
| Performance, Applications | 证明大小约随记录长度 `l` 和 circuit size `|f|` 线性；应用到 key transparency。 | 记录性能边界和应用边界。 |
| Appendix | 补充 security proofs 与 constant-size batched ZK-EDB。 | 保留证明依据，不展开成独立知识节点。 |

## 解决的问题

ZK-EDB 允许 prover 承诺一个 key-value elementary database，并证明某个 key 的 value 或 key 不存在，但表达力很有限。Libert et al. 的 ZK-EEDB 支持 richer queries，如 key/value range query 和组合范围查询，但还不能表达一般 predicate，例如“返回 value 最后一位为 0 的所有记录”。

本论文要解决的问题是: 在不泄露数据库大小和非返回记录信息的前提下，让 verifier 接受任意布尔电路谓词 `f(x, v)` 对 committed database 的完整查询结果。

直接用 zk-SNARK 的想法会遇到一个重要障碍: 为了证明查询结果完整，witness 需要覆盖全库或剩余数据库，而常见通用证明会暴露 witness length，从而泄露数据库大小。论文因此走 ZKS/accumulator 路线，而不是把整库关系塞进通用 SNARK。

## 核心方法

### Set-operation ZKS

论文从 statistically hiding ZKS / RSA accumulator 风格出发，把 set commitment 写成 unknown-order group 中的随机化指数形式。随机化提供 hiding，但也会破坏普通 accumulator 中 set algebra 到 coprime/DDH relation 的直接化约。

为恢复可证明的 set operations，作者把随机数限制在小范围，定义并证明两个 pseudo relation:

- `pseudo-coprime exponent relation`: 用于表达两个承诺集合近似 disjoint。
- `pseudo-DDH relation`: 用于表达 union/disjoint-union 风格的指数关系。

随后给出 intersection、union、difference 三种 NIZK，并把它们组合成任意 set-operation circuit 的证明。function binding 证明使用特殊 extractor: 如果 adversary 对 membership/non-membership 或 set-operation 给出互相矛盾的有效证明，就可以导向 strong RSA contradiction。

### Boolean circuit to set operations

对数据库 `D` 和布尔电路 `f(x, v)`，论文为每个输入位 `i` 和 bit `b` 构造集合:

`S_i^b = {x in Sup(D) | x||v 的第 i 位为 b}`。

然后逐门把 Boolean circuit 转换为 set-operation circuit:

- AND: 输出为 1 的集合来自两个输入为 1 的交集，输出为 0 的集合来自两个输入为 0 的并集。
- OR: 输出为 1 的集合来自两个输入为 1 的并集，输出为 0 的集合来自两个输入为 0 的交集。
- NOT: 交换 0/1 两个集合。

最终输出 wire 的 `1` 集合等于满足 `f(x, v)=1` 的 key support。这样，函数查询被转成对一组 bit-position subsets 的 set-operation query。

### ZK-FEDB construction

最终构造由两层承诺组成:

- 标准 ZK-EDB 承诺原始 key-value database，用于证明每个输出 key 的 value 正确。
- set-operation ZKS 承诺每个 `S_i^b`，用于证明输出 support 正好是 `f` 的满足集合。

Prover 对 `Sup(D(f))` 给出 set-operation proof，并对每个返回记录给出 ZK-EDB proof 和 bit-subset membership/non-membership proofs。Verifier 检查 set-operation output support、记录值正确性和 bit-subset consistency。

## 贡献与边界

| 贡献 | 说明 | 知识库吸收位置 |
| --- | --- | --- |
| ZK-FEDB definition | 首次把 ZK elementary database 查询定义到任意 Boolean circuit predicate。 | [[verifiable-database-queries|Verifiable database queries]] |
| ZKS with set-operation queries | 支持 membership 与 combined set operations 的 ZKS 变体。 | [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] |
| Circuit-to-set-operation transform | 将 Boolean predicate over records 转为 support subsets 上的 union/intersection/difference circuit。 | [[zero-knowledge-sets-to-verifiable-database-queries|Zero-knowledge sets -> verifiable database queries]] |
| Size-hiding route | 证明大小与 `l` 和 `|f|` 线性，与输入 database size 无关。 | [[verifiable-database-queries|Verifiable database queries]] |
| Key transparency application | append-only ZK-FEDB 可增强 key transparency 系统的灵活查询。 | [[applications|ZKP applications]] |

重要边界:

- 论文没有给出真实数据库系统实现、SQL engine 或分布式事务协议。
- 安全性在 random oracle model 和 generic group model 下证明，并依赖 groups of unknown order / strong RSA 风格假设。
- Prover work 仍与 `|D|` 和 `|D||f|` 相关；“与数据库大小无关”的是 proof size，不是 prover time。
- 它不是普通 zk-SNARK route；论文明确指出 naive SNARK/lookup route 的 completeness 或 database-size hiding 难点。
- 应用到 key transparency 是设计指向，不等于完整生产 KT 系统评估。

## 性能记录

论文的性能表给出:

| Phase | Prover work | Verifier work | Communication |
| --- | --- | --- | --- |
| Commit | `O(l|D|)` exponentiations plus hashing | N/A | `O(l)` group elements |
| Query | `O(l|D| + |D||f|)` exponentiations plus hashing | `O(l + |f|)` exponentiations plus output hashing | `O(l + |f|)` group elements |

进一步用 PoE 降低 verifier computation 后，proof size 近似为 `(28l + 122|f|)G`，verify cost 近似为 `(24l + 131|f|)EXT + (3l + 43|f| + |Doutput|)h`。

## 层级候选分类

| Candidate | Decision | Reason |
| --- | --- | --- |
| [[verifiable-database-queries|Verifiable database queries]] | primary | 论文核心目标是对 committed database 的 private/verifiable functional query。 |
| [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] | secondary / proof-system primitive | ZKS/ZK-EDB 是构造基础，不是应用目标。 |
| [[proof-systems|Proof systems]] | secondary | 新 NIZK 组件和 unknown-order groups 属于 proof-system machinery。 |
| `distributed-transactions` | reject | 没有并发控制、commit protocol、replication ordering 或 transaction isolation 内容。 |
| `ZK-FEDB` standalone node | reject for now | 是本文定义的 protocol/notion；先作为 verifiable database query 的方法路线，等有多来源再拆。 |

## 知识交接

### 应更新的 Knowledge

- 新建 [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]]，记录 ZKS、ZK-EDB、set-operation ZKS 和 ZK-FEDB 的 primitive 层边界。
- 新建 [[verifiable-database-queries|Verifiable database queries]]，承接 ZK-FEDB、未来 ZKSQL、private aggregate queries、authenticated/zero-knowledge database 查询等 source。
- 刷新 [[applications|ZKP applications]]，新增 `verifiable database queries` 子问题。
- 刷新 [[proof-systems|Proof systems]]，新增 ZKS/EDB method-family seed。

### 应刷新 Bridge

- 新建 [[zero-knowledge-sets-to-verifiable-database-queries|Zero-knowledge sets -> verifiable database queries]]，明确 proof primitive 到 database-query problem 的迁移边界。

### 不应新建的 Knowledge

- 不新建 paper-specific `ZK-FEDB` 知识页。
- 不把 key transparency 单独拆成 ZKP 应用子节点，当前只是本文的应用示例。
- 不把这篇归入 distributed transactions 或 blockchain database execution。

## Evidence Notes

| Evidence anchor | Observation | Absorption target |
| --- | --- | --- |
| Abstract / p1 | 定义 ZK-FEDB，支持任意 Boolean circuit functional queries，proof size 不依赖 input database size。 | [[verifiable-database-queries|Verifiable database queries]] |
| Introduction / p2 | 既有 ZK-EEDB 只支持 key/value range queries，无法处理简单 bit predicate。 | [[verifiable-database-queries|Verifiable database queries]] |
| Technique overview / p3-p5 | Naive SNARK route 会泄露 database size；作者转向 set-operation ZKS。 | [[zero-knowledge-sets-to-verifiable-database-queries|bridge]] |
| Section 3 / p11-p18 | 构造 ZK multiDL、pseudo-coprime、pseudo-DDH 等 NIZK building blocks。 | [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] |
| Section 4 / p18-p27 | 定义并构造支持 set-operation queries 的 ZKS。 | [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] |
| Section 5 / p27-p31 | 定义 ZK-FEDB、转换电路、构造和性能。 | [[verifiable-database-queries|Verifiable database queries]] |
| Applications / p31 | append-only ZK-FEDB 可增强 key transparency 查询。 | [[applications|ZKP applications]] |

## 处理日志

| Date | Run ID | Action | Reviewer |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-zk-functional-elementary-databases | Deep-read `2023-156.pdf`; created source note; corrected ontology; queued absorption into Source + Knowledge + Bridge architecture. | codex |
