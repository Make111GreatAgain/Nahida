---
id: "arxiv:2207.02746"
title: "C5: Cloned Concurrency Control That Always Keeps Up"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1 abstract and introduction"
  - "p2-p4 monotonic prefix consistency, bounded replication lag, coarse cloned concurrency control lower bound"
  - "p5-p7 C5 scheduler, row-granularity safety, snapshotter design"
  - "p7-p10 C5-MyRocks implementation and evaluation"
  - "p10-p12 C5-Cicada implementation and evaluation"
  - "p12-p14 deployment experience, related work, conclusion, references"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2207.02746"
doi: ""
arxiv_id: "2207.02746v1"
venue: "arXiv preprint"
year: "2022"
pdf_pages: 14
pdf_sha256: "726ce7a52e6434c7aa8ab1ede41059d2468d2a9032f374548b2030aabb3520bd"
local_pdf: "~/Desktop/paper/2207.02746.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/c5-cloned-concurrency-control-that-always-keeps-up-726ce7a52e64-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "transaction-processing"
topic_ids:
  - "replicated-database-concurrency-control"
  - "primary-backup-replication"
  - "cloned-concurrency-control"
  - "bounded-replication-lag"
ontology_path:
  - "distributed-systems"
  - "transaction-processing"
  - "replicated-database-concurrency-control"
primary_ontology_path: "distributed-systems/transaction-processing/replicated-database-concurrency-control"
secondary_ontology_paths:
  - "distributed-systems/data-management-and-storage/storage-engines"
  - "distributed-systems/data-management-and-storage"
path_update_status: "corrected_from_queue"
related_knowledge_refs:
  - "nahida-knowledge-transaction-processing"
  - "nahida-knowledge-replicated-database-concurrency-control"
  - "nahida-knowledge-storage-engines"
  - "nahida-knowledge-data-management-and-storage"
bridge_refs:
  - "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
hierarchy_candidates:
  domains:
    - "distributed-systems"
  directions:
    - "transaction-processing"
    - "data-management-and-storage"
  topics:
    - "replicated-database-concurrency-control"
    - "primary-backup-replication"
    - "cloned-concurrency-control"
    - "bounded-replication-lag"
domains:
  - "distributed-systems"
topics:
  - "replicated database concurrency control"
  - "primary-backup replication"
  - "cloned concurrency control"
  - "monotonic prefix consistency"
  - "bounded replication lag"
  - "row-granularity scheduling"
  - "database backup read-only transactions"
aliases:
  - "C5"
  - "Cloned Concurrency Control"
  - "C5-MyRocks"
  - "C5-Cicada"
authors:
  - "Jeffrey Helt"
  - "Abhinav Sharma"
  - "Daniel J. Abadi"
  - "Wyatt Lloyd"
  - "Jose M. Faleiro"
tags:
  - "nahida/source"
  - "paper"
  - "distributed-systems"
  - "transaction-processing"
  - "replication"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "transaction-processing"
    - "data-management-and-storage"
  problem:
    - "asynchronous primary-backup databases need backups to serve read-only transactions while applying the primary log"
    - "coarse cloned concurrency control can preserve consistency but may fall permanently behind the primary"
    - "backup reads must see a monotonic prefix of primary states rather than partial or impossible states"
  method_family:
    - "row-granularity cloned concurrency control"
    - "per-row FIFO scheduling ordered by primary log sequence"
    - "snapshotter with current, next, and future snapshots"
  system_layer:
    - "database replication"
    - "backup concurrency control"
    - "storage-engine snapshot interface"
  evaluation_context:
    - "C5-MyRocks"
    - "C5-Cicada"
    - "TPC-C"
    - "insert-only workload"
    - "adversarial workload"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-c5-cloned-concurrency-control"
source_refs:
  - "arxiv:2207.02746"
confidence: "high"
trust_tier: "primary"
primary_direction: "distributed-systems -> transaction-processing"
secondary_directions:
  - "distributed-systems -> data-management-and-storage -> storage-engines"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p14"
  - "abstract and introduction target primary-backup database replication lag under asynchronous replication"
  - "Sections 2-4 define monotonic prefix consistency, bounded replication lag, and cloned concurrency control"
  - "Sections 5-7 implement/evaluate C5 in MyRocks and Cicada; storage-engine snapshot APIs are secondary evidence"
  - "classification corrected from distributed-systems/data-management-and-storage/distributed-transactions because the paper is not about multi-participant atomic commit"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0086"
queue_status: "absorbed"
---

# C5: Cloned Concurrency Control That Always Keeps Up

## 论文身份

- 标题: C5: Cloned Concurrency Control That Always Keeps Up
- 作者: Jeffrey Helt; Abhinav Sharma; Daniel J. Abadi; Wyatt Lloyd; Jose M. Faleiro
- 版本: arXiv `2207.02746v1`
- 年份: 2022
- 本地 PDF: `~/Desktop/paper/2207.02746.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/c5-cloned-concurrency-control-that-always-keeps-up-726ce7a52e64-pages.txt`
- SHA-256: `726ce7a52e6434c7aa8ab1ede41059d2468d2a9032f374548b2030aabb3520bd`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- 已覆盖: abstract/introduction、系统模型、一致性与复制滞后定义、transaction/page granularity 下界、C5 scheduler/snapshotter、MyRocks 与 Cicada 两个实现、TPC-C/insert-only/adversarial/read-only load 实验、Meta deployment、related work 与限制。
- Extraction gaps: 图表曲线的逐点数值未 OCR；source note 只记录正文给出的关键数值和趋势。

## 一句话贡献

C5 面向异步主备数据库的备库执行层，证明 transaction/page-granularity 的 cloned concurrency control 即使保持一致性也可能产生无界复制滞后，并提出 row-granularity scheduling + snapshotter，让备库一边应用 primary log、一边服务 read-only transactions，同时保持 monotonic prefix consistency 和 bounded replication lag。

## 论文要解决的问题

Primary-backup database replication 常用异步复制来提高可用性，并让 backups 承担读-only transactions。备库不能简单串行回放 primary log，因为它还要同时服务读请求；但如果备库在尚未应用完整事务或前缀状态时读出数据，就可能暴露 primary 从未存在过的状态。

论文把目标拆成两个条件:

| 条件 | 含义 | 为什么重要 |
| --- | --- | --- |
| Monotonic prefix consistency | 备库读事务只能看到 primary execution history 的某个连续前缀，并且这个前缀随时间单调前进。 | 保证 read-only backup 不暴露违反应用 invariant 的中间状态。 |
| Bounded replication lag | 存在有限常数 `L`，使任何事务在 backup 上可见的时间不会比在 primary 上可见时间晚超过 `L`。 | 避免备库长期落后导致灾难恢复数据丢失、跨地域读延迟或流量切换失败。 |

论文引用的工程动机包括 GitLab 的长期复制滞后导致 outage/data loss，以及 Meta 因 datacenter backup lag 被迫把流量切走的经验。

## 分类判断

本篇不属于 `distributed-systems/data-management-and-storage/distributed-transactions`。它没有研究跨多个参与者的 all-or-nothing commit、2PC、2PL 或 cross-chain atomicity；核心对象是同一个数据库的 primary-backup replication，问题在于备库并发控制如何追上 primary log 并服务 consistent reads。

正确主路径是:

```text
distributed-systems / transaction-processing / replicated-database-concurrency-control
```

Secondary path 是 `distributed-systems/data-management-and-storage/storage-engines`，因为 MyRocks/RocksDB 的 snapshot API 和 Cicada 的 timestamp/MVCC 接口直接影响 C5 snapshotter 的实现边界。

## 模型与定义

论文假设 primary 有多个 execution cores，备库通过 log 接收 primary 已提交事务。备库的 cloned concurrency control 不能改变 primary commit order；它只能决定如何并发应用 log 中的 writes，并怎样向 read-only transactions 暴露稳定 snapshot。

核心定义:

| 概念 | 定义/作用 |
| --- | --- |
| Write record | primary log 中一条已提交写入，带有 log sequence。 |
| Cloned concurrency control | 备库复制 primary 的并发控制效果，在不重新执行完整事务逻辑的情况下安排 log writes。 |
| MPC state | 对 primary log 的某个事务边界前缀完整可见。 |
| Inclusion time | 某事务在 primary/backup 状态中可见的时间。 |
| Replication lag | backup inclusion time 减去 primary inclusion time。 |

## 下界: coarse granularity 为什么追不上

论文证明 transaction-granularity cloned concurrency control 无法保证 bounded replication lag。证明构造的 workload 中，每个事务先写大量互不相交的 keys，最后写同一个 hot key `k0`。Primary 的 concurrency control 可以并行执行前面互不冲突的写，只在最后 hot key 上排序；但 transaction-granularity backup 会把整个事务视为冲突单元，从而串行处理全部写。只要 primary 的并行度和单次写耗时满足论文给出的条件，backup lag 就会随 workload 无限增长。

Page-granularity 协议也有类似问题: 如果同一 page 上的多个 rows 在 primary 上可并行更新，backup 仍会按 page 冲突串行化，暴露的并行度低于 primary。

这个下界的意义不是说 coarse-grained backup 一定不正确，而是说明它们可以正确但一直追不上。

## C5 设计

C5 包含三个组件:

| 组件 | 作用 | 关键机制 |
| --- | --- | --- |
| Scheduler | 接收 primary log，维护 row-level write order。 | 每个 row 一个 FIFO queue；write 只有在到达该 row 队头且前一个队头完成后才 safe。 |
| Workers | 并发应用 safe writes。 | 从 scheduler queue 取可执行 writes，尽快推进 per-row 队列。 |
| Snapshotter | 给 read-only transactions 暴露 MPC snapshot。 | 维护 current、next、future 三个 snapshot，将 completed prefix 推进到事务边界。 |

Row-granularity 是 C5 的核心。论文的 Theorem 2 表明，任何 valid primary concurrency control protocol 至少要对同一 row 的 writes 施加 primary log order；C5 施加的正是这类必要约束，而不额外把不同行或不同事务的 writes 绑在一起。

只保持 per-row monotonicity 仍不足以保证全局 MPC，因为不同 rows 的进度可能交错。C5 snapshotter 因此使用三个 snapshot:

- `current`: 已完成的 transaction-boundary prefix，服务 read-only transactions。
- `next`: 正在填充的下一段 prefix。
- `future`: 超过当前窗口的后续 writes。

当 `current..next` 范围内的 writes 全部完成，且边界落在 transaction boundary 上时，snapshotter 合并并推进 current。

## C5-MyRocks 实现

C5-MyRocks 是面向 Meta MyRocks/RocksDB 的 production/backward-compatible 实现，论文强调它不要求修改 primary 或 log format。实现只有约 630 行 C++，但受 MyRocks/RocksDB 接口限制:

- MyRocks row-based logging 假设同一事务的所有 writes 由同一个 backup worker 执行，因此 C5-MyRocks 采用 one-thread-per-transaction，并让 worker 按 commit order 选择事务。
- RocksDB snapshot 只能是当前数据库状态的只读视图，不能完全提供 C5 理想化的 Table 2 snapshot API。
- 因此 C5-MyRocks 以 RocksDB current snapshot + database-as-next 近似三快照设计；选定边界 `n` 后，需要暂时阻止 sequence `> n` 的 writes commit，直到新 snapshot 创建完成。
- Snapshot frequency parameter `I` 在 read freshness 和 write blocking 之间做权衡。

## C5-MyRocks 实验

实验环境: CloudLab Wisconsin，3 台服务器，低于 100us RTT；每台双 2.20GHz Intel Xeon 10-core CPUs with hyperthreading、192GB RAM、10Gb NIC、480GB SSD。每组实验 120 秒，去掉开头/结尾 15 秒，取 5 次 median。为隔离 cloned concurrency control，论文关闭备库 MyRocks 2PL，并确认 disk/memory/network 不是瓶颈。

对比基线是 KuaFu-style transaction-granularity protocol，论文称它类似 MySQL 8 write-set based parallel replication，并强于更早 MySQL/MariaDB parallel replication。

主要结果:

| Workload | 结果 |
| --- | --- |
| TPC-C NewOrder | 经过 deferred high-contention operation 优化后，primary 从约 2,527 tx/s 到 4,067 tx/s；KuaFu 和 C5 都能跟上。 |
| TPC-C Payment | primary 从约 1,249 tx/s 到 9,105 tx/s；KuaFu 最高约 6,889 tx/s，会持续积压；C5 能跟上。 |
| Insert-only | MyRocks primary 约 40,500 tx/s；C5 能跟上，scheduler offline 可达约 95,683 tx/s。 |
| Adversarial workload | 随每事务 inserts 增多，KuaFu 相对吞吐从约 70% 降到 38%；C5 仍能跟上 primary。 |
| Read-only load | snapshots every 10ms 时，median lag 从 87ms 增至 160ms，max 小于 300ms；16 个 read clients 下只读吞吐约 46,500 tx/s，同时 write throughput 匹配 primary。 |

## C5-Cicada 实现与实验

论文还在 in-memory multi-version database Cicada 上做了 C5-Cicada prototype。因为 Cicada 缺少 networking/logging/persistence，实验在单机上模拟 primary-backup replication。

实现要点:

- 每个 primary execution thread 输出 log segments；scheduler 用 row-id 到 last timestamp 的 map，为每个 write 填充 `prev_timestamp`，相当于把 per-row FIFO 链接嵌入 log。
- Workers round-robin 处理 log segments；如果某 write 的 `prev_timestamp` 等于当前 row version timestamp，就 safe，否则先 defer。
- Cicada timestamp model 让 current/next/future snapshots 可以逻辑化，不需要像 MyRocks 那样显式维护多个物理 snapshot。

主要结果:

| Workload | 结果 |
| --- | --- |
| Optimized 50/50 NewOrder-Payment | Primary 约 716,950 tx/s；KuaFu 约 596,310 tx/s，有约 17% lag；C5-Cicada 约 1,062,533 tx/s。 |
| District contention sweep | KuaFu 在中低 contention 下 lag，直到 primary 自身因高 contention 变慢；禁用 KuaFu 约束近乎翻倍吞吐，证明瓶颈来自 cloned CC 约束。 |
| Insert-only | Cicada primary 约 87M rows/s with 20 threads；KuaFu 约 96M rows/s with 12 workers；C5 约 99M rows/s with 10 workers。 |
| Adversarial | 128 inserts/transaction 时，KuaFu 仅约 40% primary throughput；C5 能跟上。 |

## 部署经验

C5-MyRocks 在 Meta 部署: 论文称相关版本自 2017 年中开始使用，2019 年初完成 full deployment。一个实际 shard 的日常复制滞后案例中，旧 single-threaded/table-granularity protocol lag 会超过 2 小时并需要约 2 小时恢复；C5 将 lag 控制在 3 秒以下。

论文还记录了几个工程收益:

- 降低 failover 时潜在数据丢失。
- 改善跨区域 read-your-writes。
- 消除多租户 MyRocks 中 noisy-neighbor 引起的复制滞后。
- 暴露备库下游系统瓶颈，因为 cloned CC 不再是主瓶颈。

## 边界与限制

| 边界 | 说明 |
| --- | --- |
| Prompt log delivery assumption | formal model 假设 log delivery 足够快；若网络、持久化或 log shipping 是瓶颈，C5 不能单独保证 lag。 |
| MyRocks snapshot API | C5-MyRocks 因现有 snapshot API 和 row logging 需要加额外约束，不是理想 C5 的完全实现。 |
| Cicada prototype | C5-Cicada 没有真实网络/logging/persistence，只证明 row-granularity/timestamp integration 的潜力。 |
| Optimistic CC generalization | 论文主要处理 pessimistic/2PL 和 Cicada timestamp ordering；更一般 optimistic CC 路线留作 future work。 |
| 不是 consensus/atomic commit | C5 不处理 Byzantine agreement、leader election、distributed atomic commit 或 cross-chain transactions。 |

## 与上层知识的连接

| Knowledge/Bridge | 关系 | 本文贡献 |
| --- | --- | --- |
| [[04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control|Replicated database concurrency control]] | primary knowledge node | 提供 primary-backup cloned CC 的问题定义、row-granularity route、bounded lag 证据。 |
| [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | parent direction | 将当前 vault 的 transaction-processing 从 blockchain adaptation 扩展回数据库复制/备库并发控制。 |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | secondary knowledge node | MyRocks/RocksDB snapshot API 和 Cicada timestamp/MVCC 表明 storage-engine interface 会约束上层 replication CC。 |
| [[05_Bridges/replicated-database-concurrency-control-to-storage-engines|Replicated database concurrency control -> storage engines]] | bridge | 记录 cloned CC 与 storage-engine snapshot/log/timestamp API 的实现依赖。 |

## Promotion Decisions

| Candidate | Handling | Reason |
| --- | --- | --- |
| C5 | source instance | 命名系统属于论文具体贡献，完整保留在 source note。 |
| Cloned concurrency control | method family row | 是可复用方法族，但当前 vault 只有 C5 一篇直接 source；先放在 knowledge node 的路线中。 |
| Replicated database concurrency control | new knowledge node | 问题足够通用，并且能防止 C5 误入 distributed transactions。 |
| Monotonic prefix consistency | concept row / candidate | 是 C5 的关键正确性目标，但当前只有一篇 source；等待更多 replication/freshness source 再拆。 |
| Bounded replication lag | concept row / candidate | 是备库复制的核心目标，可作为 future child candidate。 |

## Query Handoff

- C5 为什么能避免 replication lag?
- cloned concurrency control 和普通 concurrency control 的区别是什么?
- primary-backup database backup 如何同时服务只读事务?
- monotonic prefix consistency 是什么?
- MyRocks/RocksDB snapshot API 为什么影响 C5?
- C5 和 KuaFu/MySQL parallel replication 的差别是什么?
