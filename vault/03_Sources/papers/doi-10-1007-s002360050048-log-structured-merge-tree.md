---
id: "doi-10-1007-s002360050048-log-structured-merge-tree"
title: "The Log-Structured Merge-Tree (LSM-Tree)"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1007/s002360050048"
doi: "10.1007/s002360050048"
arxiv_id: ""
venue: "Acta Informatica 33(4):351-385"
year: "1996"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "storage-engines"
  - "lsm-tree-storage-engines"
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "storage-engines"
  - "lsm-tree-storage-engines"
primary_ontology_path: "distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines"
secondary_ontology_paths: []
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
  directions:
    - "data-management-and-storage"
  topics:
    - "storage-engines"
    - "lsm-tree-storage-engines"
domains:
  - "distributed-systems"
topics:
  - "LSM-tree"
  - "storage engines"
  - "deferred index maintenance"
  - "rolling merge"
  - "history table indexing"
aliases:
  - "The log-structured merge-tree (LSM-tree)"
  - "Log-Structured Merge-tree"
  - "LSM original paper"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "distributed-systems/data-management-and-storage"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "data-management-and-storage"
  problem:
    - "high-insert-rate index maintenance"
    - "history and log indexing"
    - "write-optimized persistent storage"
  method_family:
    - "Log-Structured Merge-tree"
    - "rolling merge"
    - "deferred index maintenance"
    - "multi-component storage engine"
  system_layer:
    - "storage engine"
    - "database access method"
    - "transaction log/history index"
  evaluation_context:
    - "B-tree insert I/O cost"
    - "multi-page block I/O"
    - "memory versus disk-arm cost"
    - "find versus insert workload balance"
  application:
    - "high-performance transaction systems"
    - "history tables"
    - "transaction logs"
  bridge: []
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF first page gives title, authors, Acta Informatica target, abstract, and transaction-history/log indexing motivation"
  - "sections 2-4 define two-component and multi-component LSM-tree algorithms plus concurrency/recovery"
  - "Crossref/DBLP metadata correct publication year from PDF creation-date 2003 to Acta Informatica 1996, DOI 10.1007/s002360050048"
taxonomy_version: "1.0"
local_pdf: "~/Desktop/paper/lsmtree.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/lsmtree.acta.inf.pat-8fe1d3206fe8-pages.txt"
pdf_sha256: "8fe1d3206fe8eb151e9d8c54e0772a46786e2ec40e4c2b7782995067d6b938c6"
page_count: 32
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260623-lsm-tree"
source_refs:
  - "doi:10.1007/s002360050048"
  - "sha256:8fe1d3206fe8eb151e9d8c54e0772a46786e2ec40e4c2b7782995067d6b938c6"
confidence: "high"
trust_tier: "primary"
---

# The Log-Structured Merge-Tree (LSM-Tree)

## 论文身份

- 标题: `The Log-Structured Merge-Tree (LSM-Tree)`
- 作者: Patrick O'Neil, Edward Cheng, Dieter Gawlick, Elizabeth O'Neil
- PDF 内部出版线索: 首页写有 `To be published: Acta Informatica`；PDF metadata title 为 `LSMtree.Acta.Inf.Pat`，CreationDate 是 2003，这只是 PDF 生成时间，不应作为论文年份。
- 正式出版元数据: Crossref 与 DBLP 均给出 Acta Informatica, volume 33, issue 4, pages 351-385, 1996, DOI `10.1007/s002360050048`。
- 链接: https://doi.org/10.1007/s002360050048
- 本地 PDF: `~/Desktop/paper/lsmtree.pdf`
- Extracted text: `vault/02_Raw/pdf/extracted/lsmtree.acta.inf.pat-8fe1d3206fe8-pages.txt`
- SHA-256: `8fe1d3206fe8eb151e9d8c54e0772a46786e2ec40e4c2b7782995067d6b938c6`
- 元数据修正: queue 中 `year: 2003` 来自 Acrobat Distiller metadata；本 note 修正为正式出版年 `1996`，并保留 PDF evidence 与外部 metadata evidence 的区别。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: managed pypdf extraction
- 页数: 32
- 已覆盖章节/页码: Abstract, §1-§6, references
- 未覆盖章节/页码: none material
- Extraction gaps: 公式排版与上下标有少量断裂；主要定义、算法、成本公式、例子和结论可读。
- 精读说明: 本 note 重建原始 LSM-tree 的问题设定、两组件/多组件算法、成本模型、并发恢复设计、竞争 access method 比较和吸收路径；未来普通查询不需要重新打开 PDF。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 高吞吐 transaction system 会产生 history table rows 和 recovery logs；B-tree 实时维护随机 secondary index 成本高；LSM-tree 用 defer-and-batch index changes 降低 disk arm movements。 | high | 核心问题不是“通用排序结构”，而是写密集索引维护。 |
| §1 p1-p3 | 动机与 TPC-A 例子 | Account-ID||Timestamp history index 若用 B-tree，会在 1000 TPS 例子中把 index insert 变成大量随机 I/O，几乎翻倍磁盘臂需求。 | high | 给出历史表/日志索引工作负载。 |
| §2 p4-p8 | Two-component LSM-tree | `C0` 内存组件、`C1` 磁盘组件、rolling merge、multi-page blocks、exact/range find、delete node、predicate deletion、long-latency find。 | high | 上层 LSM 节点的原始机制证据。 |
| §3 p8-p21 | 成本模型与多组件 LSM | 用 `COSTπ/COSTP` 和 batch-merge 参数 `M` 分析 LSM 相对 B-tree 的 insert cost；多组件通过几何级数的组件比例降低内存成本。 | high | 提供原始 cost-performance 公式与 workload boundary。 |
| §4 p21-p25 | 并发与恢复 | 节点锁、merge cursor、cursor passing、checkpoint、root/cursor/block allocation logging、从 transaction logs 重建 `C0`。 | high | 说明 LSM 不是只靠“先写内存”，还要能在线查找与崩溃恢复。 |
| §5 p25-p29 | 与其他 access methods 比较 | 定义 Continuum Structure；说明 B-tree/hash/SB-tree/Bounded Disorder 立即定位导致随机 I/O；TSB-tree、MD/OD R-tree、Differential File、text deferred updates 不保证 authoritative memory component。 | high | 明确 LSM 的差异边界。 |
| §6 p29-p31 | 结论与扩展 | LSM 把逻辑 hot insert workload 变成物理更冷的 disk workload；讨论 clustered records、Escrow logs、recent-entry retention、CPU offload。 | high | 给出后续 LHAM/modern LSM 路线的根部。 |
| References p31-p32 | 相关工作 | LFS、SB-tree、Differential File、TSB-tree、B-tree concurrency/recovery、Five Minute Rule、transaction processing。 | medium | 支撑相邻 foundation gaps。 |

## 核心精读笔记

### 背景、动机与问题边界

- 论文的直接背景是高性能事务处理系统。系统一方面写 recovery logs，另一方面可能写 history table 作为 activity trace；如果需要按账号或事务维度查询历史，必须维护索引。
- 作者用 modified TPC-A 展示问题: 每秒 1000 笔交易产生随机 `Acct-ID||Timestamp` index entries。传统 B-tree 需要把 leaf page 随机读入、修改、写回；由于 leaf pages 远大于可经济缓存范围，新增 secondary index 会显著增加 disk arm 成本。
- LSM-tree 解决的是“高插入率文件上的低成本实时索引”，尤其适合 insert/delete/update/long-latency find 这类可 mergeable 的操作。它不适合把 immediate find 作为主要负载的场景，因为查询可能需要检查多个组件。
- 证据锚点: Abstract, §1 Example 1.1/1.2, §3, §6。

### 模型、假设与定义

- LSM-tree 由两个或更多 tree-like components 组成。`C0` 是内存组件，`C1..CK` 是磁盘组件；组件越往后越大。
- 插入路径: 新 record 的 recovery log 正常写入 sequential log；index entry 先插入 `C0`，不产生随机磁盘 I/O；之后 rolling merge 将 `C0` 的连续 key range 批量合并到 `C1`。
- 磁盘组件结构类似 B-tree directory，但 leaf/directory nodes 会按 key sequence 打包在 multi-page disk blocks 中。rolling merge 用大块顺序 I/O；exact find 仍可通过单页节点查找来减少 buffer 需求。
- rolling merge 有 conceptual cursor。它在 key order 上循环，读取 `C1` 的 emptying block，和 `C0` 的对应 entries 合并，生成 filling block 写到新磁盘位置。旧块在新写成功后 invalidated，便于 crash recovery。
- Delete/update/future find 也可延迟: delete node 随 merge 向外迁移并在遇到目标 entry 时 annihilate；predicate deletion 可批量删旧 timestamp；long-latency find 可作为 note entry 迁移并逐步收集结果。
- 证据锚点: §2.1-§2.3。

### 成本模型与关键公式

- 论文把 I/O 成本拆成随机 page I/O cost `COSTP` 与 multi-page block I/O per-page cost `COSTπ`。1995 workstation cost model 中，multi-page block I/O 的每页磁盘臂成本约为随机 I/O 的十分之一。
- B-tree insert cost 近似为 `COSTP * (De + 1)`：搜索到 leaf 的未缓存 I/O 加上 leaf write-back。
- LSM insert cost 近似为 `2 * COSTπ / M`。其中 `M` 是每次 rolling merge 到一个 `C1` leaf page 时，从 `C0` 批量合入的平均 entries 数。
- 因此 LSM/B-tree insert cost ratio 由两个 batching effects 决定: multi-page block I/O 优势 `COSTπ/COSTP`，以及 batch-merge 参数 `1/M`。当 index 对 B-tree 来说是 warm/high-temperature data 时，这两者可以带来数量级级别的 insert cost 改善。
- 多组件 LSM 的动机: 如果 `C0` 相对最终磁盘组件太小，rolling merge 需要快速扫过大组件，I/O 又会上升；如果 `C0` 太大，内存成本高。加入中间磁盘组件可以用几何级数的组件大小在内存和磁盘臂成本之间取平衡。
- Theorem 3.1 给出固定最大组件、固定 `C0`、固定插入率时的最优 intuition: 相邻组件大小比例相等。工程含义是多组件 LSM 可以用更小的内存组件承受更高写入率，但组件数增加也会增加 immediate find I/O 和 merge CPU/buffer 开销。
- 证据锚点: §3.1-§3.4, Examples 3.1-3.4。

### 并发与恢复机制

- 并发问题有三类: find 不能和 rolling merge 同时改同一磁盘节点；find/insert 不能和 `C0 -> C1` merge 同时改同一内存范围；较快的小组件 cursor 必须能越过较慢的大组件 cursor。
- 论文建议以节点作为物理锁粒度。rolling merge 修改节点时持 write lock，find 持 read lock；节点级锁在每个 merge step 后释放，使长 range find 或较快 cursor 有机会通过。
- 对 `C0`，锁策略取决于具体内存树结构，例如可对 `(2-3)-tree` 的相关 subtree/range 加写锁，并在 merge 后批量 rebalance。
- Recovery 依赖 checkpoint。checkpoint 记录 last indexed row 的 LSN、所有组件 root 地址、merge cursor 位置和 dynamic block allocation 信息，并把 `C0` 与 dirty buffered nodes 刷盘。
- crash recovery 从 checkpoint 恢复组件和 cursor，然后从 `LSN0` 后的 transaction insert logs 重放 index entries 到 `C0`。由于 merge 写入新块而不覆盖旧块，checkpoint 后写出的块可以在恢复时被重新生成。
- 证据锚点: §4.1-§4.2。

### 与其他 access methods 的边界

- 作者定义 `Continuum Structure`: 新 index entry 必须立即放到最终 key collation order 的位置。B-tree、hash variants、SB-tree、Bounded Disorder File 等大多属于这一类，所以在随机 key 高插入率下会遇到不可经济缓存的大 leaf set。
- LSM 胜出的两个必要条件是: 新 entry 首先进入确定内存常驻的 authoritative component；随后通过 carefully deferred placement 批量进入更大组件。如果新写入组件本身会变成磁盘常驻，则 insert I/O 会退化。
- TSB-tree、MD/OD R-tree、Differential File 等也有迁移/归档/差分思想，但原论文批评它们没有把初始动态组件设计为始终内存常驻、权威参与查询的组件，因此不直接提供同等 insert-performance guarantee。
- Text deferred index updates 会缓存更新并批量写回，但 memory cache 不是 authoritative index；查询冲突可能迫使更新刷到磁盘，所以仍像 Continuum Structure。
- 证据锚点: §5。

### 结论、扩展与后续路线

- LSM-tree 的核心不是单纯“日志式写入”，而是把内存组件、multi-page block I/O、rolling merge 和延迟最终定位结合起来，使逻辑热插入负载在物理磁盘层接近冷/温数据成本。
- 论文已经预见了多个现代 LSM 方向: entries 可以直接包含 records 以支持 clustering；可以保留 recent entries 改善新近查询；可以把维护工作 offload 到其他 CPU；可以为 Escrow/long-lived transactions 的日志按 TID/FID 做不同聚簇。
- 需要保留的限制: immediate find 和 range query 不是免费；组件越多，查询可能越慢；checkpoint 可能带来暂停；并发/恢复算法在论文中是 sketch，需要实现经验和 formal correctness 补足。
- 证据锚点: §6.1。

## 层级候选分类

- L1 Domain: `distributed-systems`
- L2 Direction: `data-management-and-storage`
- L3 Topic: `storage-engines`, `lsm-tree-storage-engines`
- Primary ontology path: `distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines`
- Secondary path: none promoted. 虽然论文动机来自 transaction processing 的 history/log indexing，但 durable 方法族是 storage engine / access method；事务处理只作为 workload context 写入 source note 和上层 source extension。
- 分类置信度: high
- 分类理由: 标题、摘要、§2-§4 都在定义一种磁盘 access method / storage-engine method family；§1 的 transaction workload 是动机和应用边界，不是本论文的上层协议主题。

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `distributed-systems` / data systems | high-performance transaction systems, disk access methods, recovery/concurrency | high | attach to existing domain |
| Research background | B-tree random I/O, Five Minute Rule, log-structured storage, transaction logs/history tables | §1, §3, references | high | refresh storage-engine background |
| Research problem | high-insert-rate real-time index maintenance | Abstract, Examples 1.1/1.2 | high | source extension under LSM-tree storage engines |
| Foundation concepts | storage engine, access method, LSM-tree, rolling merge, deferred index maintenance | §2-§5 | high | refresh existing knowledge node |
| Method family | Log-Structured Merge-tree | full paper | high | representative/foundational source, no source-named upper page |
| Application/evaluation context | history table index, transaction logs, Escrow logs | §1, §6.1 | high | record as workload boundary |
| Artifact/source instance | original LSM paper | local PDF + DOI metadata | high | detailed source note |

## 检索优化判断

- 应更新的 Knowledge path: `distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines`
- 它减少未来阅读成本的问题: “原始 LSM-tree 到底解决什么问题”、“为什么 LSM 比 B-tree 插入便宜”、“rolling merge 和多组件尺寸怎么解释”、“LSM 并发恢复靠什么”。
- 应留在 source note 的内容: TPC-A 数值例子、详细公式推导、cursor locking sketch、竞争 access method 逐项比较、Escrow log extensions。
- 应进入知识节点的 delta: 原始 LSM 的 defer-and-batch index maintenance 机制、`C0/C1..CK` rolling merge model、immediate find 的边界、history/log indexing workload。
- 新 bridge 判断: 不创建新 bridge。论文的 transaction workload 与 storage engine 的关系目前可作为 `Storage Engines` source extension；现有 `replicated-database-concurrency-control -> storage engines` bridge 关注备库 CC 接口，不应被这篇原始 LSM 论文强行扩展。

## 一句话贡献

这篇原始 LSM-tree 论文提出了用内存常驻组件加 rolling merge 的磁盘 access method，把写密集历史表/日志索引的随机 B-tree 更新转化为批量顺序化的多页块合并，从而大幅降低插入路径的磁盘臂成本。

## 问题设定

高性能事务系统会持续生成历史记录和日志。如果这些记录需要按非时间主键查询，例如按账号查询最近活动，系统必须实时维护 secondary index。B-tree 这类传统结构把新 index entry 立即插入最终位置，在随机 key 分布下会导致每次写入至少一次随机 leaf read 和一次 leaf write。LSM-tree 的问题定义是: 在保证索引持续可查的同时，如何延迟并批量处理这些 index changes。

## 方法概览

### 组成部分

- `C0`: 内存常驻组件，承接新 index entries。
- `C1..CK`: 磁盘组件，按大小递增，结构类似 B-tree directory 加 packed multi-page blocks。
- Rolling merge cursor: 在相邻组件间循环推进，把小组件的连续 key range 合并到大组件。
- Checkpoint/recovery metadata: 记录 LSN、component roots、merge cursors 和 block allocation。
- Query path: immediate find 必须先查 `C0`，再查磁盘组件；可用 uniqueness/recent timestamp 等条件剪枝。

### 核心机制

1. 新写入先进入 `C0`，避免随机磁盘 I/O。
2. `C0` 到达阈值后，rolling merge 取一个连续 key segment，与 `C1` 的 leaf block 合并。
3. 新生成的 `C1` blocks 写到新磁盘位置，旧 blocks invalidated 而不覆盖。
4. 多组件版本把这个过程推广到 `C0 -> C1 -> ... -> CK`，用中间组件降低内存和磁盘臂成本。
5. Deletes、updates 和 long-latency finds 也可作为可迁移条目，在 rolling merge 中延迟生效。

## 证据与限制

| 论点 | Evidence anchors | 置信度 | 限制 |
| --- | --- | --- | --- |
| B-tree 实时维护随机 history index 会显著增加磁盘 I/O | Abstract, §1 Example 1.2 | high | 数值基于 1990s disk/memory cost model；现代硬件需重新评估。 |
| LSM insert 成本来自 multi-page block I/O 与 batch merge 两个 batching effects | §3.2 equations 3.1-3.4 | high | 公式是模型分析，未给现代实现 benchmark。 |
| 多组件 LSM 可降低 `C0` 内存需求 | §3.3-§3.4, Theorem 3.1, Examples 3.3-3.4 | high | 组件数增加会损害 immediate find。 |
| Recovery 可从 checkpoint 和 transaction logs 重建 | §4.2 | medium-high | 作者说明 correctness formal proof 留给后续工作。 |
| LSM 区别于其他 deferred/differential access methods | §5 | high | 比较针对当时文献，不覆盖现代 RocksDB/LevelDB/SSTable 实践。 |

## 与现有知识库的关系

| Target | Update | Reason |
| --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines|LSM-tree Storage Engines]] | 新增原始论文 source extension；补强 rolling merge、成本模型和并发恢复来源。 | 原始 source 是当前 LSM 节点缺口。 |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | 新增 high-insert-rate index maintenance as storage-engine problem axis。 | 论文从 access method 角度说明 storage engine 如何服务事务历史/日志负载。 |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | 补入 LSM 原论文作为存储引擎方向代表 source。 | 强化 data-management-and-storage 不只是 survey 派生。 |

## 后续队列

| Candidate | Why | Handling |
| --- | --- | --- |
| B-tree / buffer manager / WAL recovery foundation | LSM 论文反复用 B-tree、buffer、recovery 作对照，当前知识库仍偏薄。 | 保持 queued foundation gap。 |
| RocksDB / LevelDB implementation source | 原始 LSM 与现代 SSTable/compaction engine 之间有工程差异。 | future GitHub/source analysis。 |
| LHAM / log-structured history access method | 论文 §6.1 和 references 指向历史数据访问扩展。 | candidate/watch, 不立即建节点。 |

## 参考来源

- 本地 PDF: `~/Desktop/paper/lsmtree.pdf`
- Crossref metadata: https://api.crossref.org/works?query.title=The%20Log-Structured%20Merge-Tree%20LSM-Tree&rows=3
- DBLP metadata: https://dblp.org/rec/journals/acta/ONeilCGO96
