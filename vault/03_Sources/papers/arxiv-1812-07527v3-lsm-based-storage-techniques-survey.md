---
id: "arxiv-1812-07527v3-lsm-based-storage-techniques-survey"
title: "LSM-based Storage Techniques: A Survey"
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
canonical_url: "https://arxiv.org/abs/1812.07527"
doi: ""
arxiv_id: "1812.07527v3"
venue: "arXiv preprint"
year: "2019"
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
  - "compaction"
  - "NoSQL"
aliases:
  - "LSM-based Storage Techniques"
  - "LSM-tree survey"
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
    - "write-optimized persistent storage"
    - "read/write/space amplification tradeoffs"
  method_family:
    - "Log-Structured Merge-tree"
    - "leveling"
    - "tiering"
    - "partitioned compaction"
  system_layer:
    - "storage engine"
    - "NoSQL database storage layer"
  evaluation_context:
    - "write amplification"
    - "read amplification"
    - "space amplification"
    - "merge cost"
  application:
    - "key-value stores"
    - "NoSQL databases"
  bridge: []
classification_status: "refined_from_queue"
classification_confidence: "high"
classification_evidence:
  - "title, abstract, keywords, and Sections 2-4 all center on LSM-tree storage engines and NoSQL/data system storage layers"
taxonomy_version: "1.0"
local_pdf: "~/Desktop/paper/1812.07527.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/1812.07527-06efb3176be8-pages.txt"
pdf_sha256: "06efb3176be877bf074ad869683e91c11065b98ddf0411d5d6241acbde4be92a"
page_count: 25
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260620-item-0033"
source_refs:
  - "arxiv:1812.07527v3"
  - "sha256:06efb3176be877bf074ad869683e91c11065b98ddf0411d5d6241acbde4be92a"
confidence: "high"
trust_tier: "primary"
---

# LSM-based Storage Techniques: A Survey

## 论文身份

- 标题: `LSM-based Storage Techniques: A Survey`
- 作者: Chen Luo, Michael J. Carey
- 机构: University of California, Irvine
- 会议/期刊: arXiv preprint; PDF 页眉显示 `Noname manuscript No. (will be inserted by the editor)`，未从本地 PDF 证据中确认正式期刊/会议。
- 年份: 2019
- DOI: unknown
- arXiv: `1812.07527v3 [cs.DB]`, 19 Jul 2019
- 链接: https://arxiv.org/abs/1812.07527
- 本地 PDF: `~/Desktop/paper/1812.07527.pdf`
- Extracted text: `vault/02_Raw/pdf/extracted/1812.07527-06efb3176be8-pages.txt`
- SHA-256: `06efb3176be877bf074ad869683e91c11065b98ddf0411d5d6241acbde4be92a`
- 关键词: `LSM-tree`, `NoSQL`, `Storage Management`, `Indexing`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: existing managed text extraction
- 页数: 25
- 已覆盖章节/页码: Abstract, §1-§6, Tables 1-3, representative systems, future directions, references overview
- 已检查附录: 本地文本中未见独立 appendix
- 未覆盖章节/页码: none material
- Extraction gaps: 少量连字符、排版页眉和表格符号需要人工解释；不影响主要论证。
- 精读说明: 本 note 按章节重建 survey 的 taxonomy、cost model、trade-off 表、代表系统和未来方向；普通查询不需要重新打开 PDF。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / §1 | 问题与贡献 | LSM-tree 在 BigTable、Dynamo、HBase、Cassandra、LevelDB、RocksDB、AsterixDB 等系统中的采用；本文给出近期研究 taxonomy、trade-off 和代表系统综述。 | high | 队列原标题来自页眉噪声，已更正。 |
| §2 | 基础机制 | 对比 in-place update 与 out-of-place update；解释原始 LSM-tree、现代 SSTable 组件、leveling/tiering、Bloom filters、partitioning、并发与恢复、成本分析。 | high | 这是上层 `lsm-tree-storage-engines` 节点的基础证据。 |
| §3.1-§3.8 | 改进 taxonomy | 六类改进: 降低 write amplification、merge operations、hardware、special workloads、auto-tuning、secondary indexing；Table 2/3 给出文献分类与 trade-off。 | high | 细节很多，适合作为 source note；上层只抽路线和边界。 |
| §4 | 代表系统 | LevelDB、RocksDB、HBase、Cassandra、AsterixDB 的 LSM 设计与工程策略。 | high | 这些系统目前是代表实例，不单独建 foundation node。 |
| §5 | 未来方向 | 要求与 tuned baseline 比较、系统评估 partitioned tiering、hybrid policies、降低性能方差、走向 database storage engine。 | high | 更新 domain dynamics 和 gap/watchlist。 |
| §6 | 总结 | LSM-tree 因写性能、空间利用率、不可变组件和 tunability 而流行，但 trade-off 必须显式管理。 | medium | 支撑综合判断。 |

## 核心精读笔记

### 背景、动机与问题边界

- 背景脉络: 数据系统长期在 read/update/storage 之间权衡。B+-tree 等 in-place update 结构适合点查和范围查，但更新会造成随机 I/O 和碎片；out-of-place update 结构把新版本写到新位置，用顺序 I/O 换取更复杂的读取和后台重组。
- 现有方法不足: LSM-tree 写入友好，但读请求可能要查多个组件，删除/更新会留下旧版本，后台 merge/compaction 会制造写放大、空间放大和延迟方差。许多论文只和默认 LevelDB/RocksDB 配置比较，忽视 LSM 参数可调性。
- 本文问题定义: 综述近期 LSM-based storage techniques，建立分类、解释每类优化改善什么、牺牲什么，并把研究技术和生产系统连接起来。
- 明确不解决的问题: 本文不是单一新算法论文，不给出新的实验系统；它也不声称覆盖所有数据库索引结构，只聚焦 LSM-tree 及其 storage-engine 技术。
- 证据锚点: Abstract, §1 Introduction, §2 Basics, §3 Overall trade-offs, §5 Future Directions。

### 模型、假设与定义

- LSM-tree 基本模型: 内存组件吸收写入；组件满后 flush 到磁盘；磁盘组件通常是 B+-tree 或 SSTable；查询从新到旧查多个组件并按 timestamp/reconciliation 处理多版本。
- 原始 LSM-tree: 有内存 `C0` 和磁盘 `C1..Ck`，通过 rolling merge 把较小层组件合并到较大层；稳定工作负载下相邻层大小比例相等时成本较优。
- 现代组件: SSTable 通常由不可变 sorted run 组成，配合 Bloom filters、range metadata、timestamp/sequence number 和后台 compaction。
- Leveling: 每层通常只有一个逻辑组件，下一层约为上一层 `T` 倍；优点是读和空间较好，代价是 write amplification 较高。
- Tiering: 每层允许最多 `T` 个组件，满后一起向下一层 merge；优点是写入更友好，代价是读放大和空间放大更高。
- Bloom filters: 点查优化，没有 false negative，有 false positive；公式为 `(1 - e^{-kn/m})^k`，最优 `k = m/n ln 2`，常见 10 bits/key 约 1% false positive。
- 分区: 把磁盘组件拆为 SSTable/range partition，限制单次 merge 处理量和临时空间；LevelDB 是 partitioned leveling 的代表。
- 证据锚点: §2.1-§2.5。

### 方法、协议或系统机制

- 写路径: 写入先进入 mutable memory component 和 WAL；内存满后 flush 成 immutable disk component；后台按 merge policy 重组。
- 读路径: 点查用 memory component、Bloom filters 和磁盘组件元数据减少 I/O；范围查必须合并多个 sorted runs，因此 tiering 对短/长 range query 的代价更明显。
- 并发与恢复: 读写和 merge 可通过 locking 或 multi-version schemes 协调；组件元数据需要同步；WAL 记录内存写入，no-steal buffer policy 简化恢复；LevelDB/RocksDB 可用 metadata log 恢复组件状态。
- 成本模型: 若 size ratio 为 `T`、层数为 `L`、page size 为 `B`、memory component pages 为 `P`、总记录数为 `N`，则层数近似为 `log_T(N/(B·P) * T/(T+1))`。Leveling write amplification 约 `O(T·L/B)`，tiering 约 `O(L/B)`；无 Bloom 点查 leveling `O(L)`、tiering `O(T·L)`；range query leveling 比 tiering 更好；space amplification leveling 约 `O((T+1)/T)`，tiering 约 `O(T)`。
- RUM conjecture: 论文把 LSM 设计放在 read/update/memory-storage trade-off 中，任何优化通常改善一个维度并牺牲另一个维度。
- 证据锚点: §2.4-§2.6, Table 1。

### LSM 改进 taxonomy

| 类别 | 代表路线 | 改善什么 | 牺牲/限制 | 证据锚点 |
| --- | --- | --- | --- | --- |
| 降低 write amplification | WB-tree、LWC-tree、PebblesDB、dCompaction、SifrDB、skip-tree、TRIAD | 减少真实 merge 或利用热点/分区降低写成本 | 通常增加 read/space amplification、复杂度或范围查询成本 | §3.2 |
| Merge operations | VT-tree stitching、pipelined merge、remote merge、LSbM-tree、bLSM | 降低 merge copy、缓存扰动或 write stalls | 可能破坏 Bloom filter 兼容、增加碎片或只解决吞吐不解决尾延迟 | §3.3 |
| 硬件适配 | FloDB、Accordion、cLSM、FD-tree/FD+tree、WiscKey、HashKV、Kreon、NoveLSM、LOCS、NoFTL-KV | 利用大内存、多核、SSD/NVM/native flash | 需要特殊硬件或引入 GC、range query 退化、系统复杂度 | §3.4 |
| 特殊工作负载 | LHAM、LSM-trie、SlimDB、append-mostly policies | 针对时间、超大 KV、小对象、半排序 key、append-mostly | 常牺牲通用查询能力或范围查询 | §3.5 |
| Auto-tuning | Lim et al. model、Monkey、Dostoevsky、ElasticBF、Mutant | 参数、Bloom filter memory、merge policy 和 cloud storage placement 自动优化 | 依赖 workload 模型；部分收益只在低 Bloom memory 或特定 workload 下明显 | §3.6 |
| Secondary indexing | LSII、LSM R-tree/spatial indexes、component filters、Diff-Index、DELI、bulk loading/global-local indexes | 把 LSM 用于二级索引、空间/倒排索引、索引维护和分布式索引 | 更新清理、验证、index-only query、选择性和分区通信成本复杂 | §3.7 |

### 实验、评估或案例

- 本文不是统一 benchmark 论文，而是 survey；它用 Table 2 分类文献、Table 3 总结各技术对 write/read/space amplification 和复杂度的影响。
- 作者明确批评许多工作只对比默认 LevelDB/RocksDB，尤其默认 leveling `T=10`，没有和经过调参的 LSM baseline 比较，也常忽略 space amplification。
- 代表系统:
  - LevelDB: Google 2011 embedded key-value store，代表 partitioned leveling。
  - RocksDB: Facebook fork，增加 L0 tiering、dynamic level sizes、compaction filter、tiering/FIFO policies、rate limiting、merge operator 等。
  - HBase: Bigtable-like Hadoop storage，region 内部使用 LSM，支持 tiering、date-tiered merge policy、stripping 和 coprocessor-based secondary index。
  - Cassandra: Dynamo/BigTable-like decentralized store，每个 partition 用 LSM engine，支持 tiering、partitioned leveling、date-tiered merge，以及 lazily maintained local secondary indexes。
  - AsterixDB: shared-nothing BDMS，每个 partition 有 primary index、primary-key index、local secondary indexes，提供 generic LSM-ification、record-level transactions 和 correlated merge policy。
- 证据锚点: §3.8, §4。

### 作者结论与我的判断

- 作者明确声称: LSM-tree 在现代数据系统中流行，是因为它把随机更新转成顺序写，能获得写性能和空间利用率，同时通过 merge policies、Bloom filters 和 partitioning 提供可调性。
- 由证据支持的判断: LSM-tree 不是“更快的 B-tree”，而是一组围绕 write/read/space amplification、merge scheduling 和 workload/hardware 特化的设计空间；大多数改进都不是免费午餐。
- 仍需谨慎的推断: 由于本文是 2019 survey，不能代表 2026 最新工业实践或最新 LSM 研究；后续 query 若问最新进展，需要 daily-fetch 或新的 source。
- 证据锚点: §3.8 Overall Trade-offs, §5 Future Directions, §6 Conclusion。

## 层级候选分类

- L1 Domain candidate: `distributed-systems`
- L2 Direction candidate: `data-management-and-storage`
- L3 Topic/content cluster candidates: `storage-engines`, `lsm-tree-storage-engines`
- Ontology path: `distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines`
- 备选归属: 可与 `database-systems/storage-engines` 相邻，但当前 vault 没有独立 database-systems 域；为保持队列和已有 domain 结构，先放入 distributed-systems 下的数据管理与存储方向。
- 父级领域: distributed systems / data systems
- 学术子领域: storage management, indexing, NoSQL storage engines
- 任务/问题: 写优化持久化存储、读写空间放大权衡、后台 compaction/merge 调度、二级索引维护。
- 方法族: Log-Structured Merge-tree, leveling, tiering, partitioned compaction, Bloom-filter-assisted lookup。
- 模型/协议/算法族: storage engine design family，不是共识协议或单个系统实例。
- 评测场景: write amplification、read amplification、space amplification、range query、merge overhead、latency variance、secondary index maintenance。
- Benchmark/应用: LevelDB、RocksDB、HBase、Cassandra、AsterixDB。
- 别名: LSM-tree, LSM-based storage, log-structured merge-tree。
- 相邻方向: transaction processing, distributed databases, cloud storage, secondary indexing。
- 置信度: high
- 分类理由: 论文标题、关键词、§2 基础、§3 taxonomy、§4 代表系统都明确围绕 LSM-tree storage engine。
- 分类状态: refined_from_queue
- 分类证据: queue title 为 PDF 页眉误抽；正文标题、摘要和 arXiv ID 支持正确标题。

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `distributed-systems` / data systems | NoSQL systems and distributed storage systems in §1/§4 | high | update domain parent |
| Research background | out-of-place update, log-structured storage, LSM history from differential files/LFS/original LSM | §2 Basics | high | background in storage-engine nodes |
| Research problem | storage engines that reduce random-write cost while controlling read/space/merge amplification | Abstract, §2.6, §3.8 | high | create topic node |
| Foundation concepts | storage engine, LSM-tree, leveling, tiering, Bloom filter, compaction, RUM trade-off | §2 | high | foundation_thin knowledge nodes/sections |
| Method family | LSM-tree storage engines and compaction policy families | §2-§3 | high | create `lsm-tree-storage-engines` node |
| Application/evaluation context | NoSQL key-value/database storage systems; LevelDB/RocksDB/HBase/Cassandra/AsterixDB | §4 | high | representative systems in knowledge |
| Artifact/source instance | this survey paper | full PDF | high | source extension / representative source |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines`
- 它能帮助未来哪些问题少读 source notes: “LSM-tree 是什么”、“leveling vs tiering 怎么取舍”、“LSM-tree 为什么有 write/read/space amplification”、“哪些系统使用 LSM”、“LSM 研究有哪些路线”。
- 哪些内容应留在 source note: Table 2/3 的细粒度文献清单、每个具体改进论文的机制细节、各系统的实现细节。
- 哪些上层节点过薄、缺失或需要 foundation_pack: `data-management-and-storage`、`storage-engines` 是新 seed；未来可补数据库系统/分布式存储 foundations。
- 哪些候选只是别名/query key/watch term: LevelDB、RocksDB、HBase、Cassandra、AsterixDB、WiscKey、Monkey、Dostoevsky 等暂作代表系统/路线，不建独立 foundation node。

## 一句话贡献

这是一篇 LSM-tree storage engine survey：它把 LSM-tree 的基础成本模型、改进路线、工程系统和未来问题组织成一套读写空间权衡的 taxonomy。

## 问题设定

现代数据系统需要高吞吐写入、低读延迟、较低空间开销和可控后台维护成本。LSM-tree 用 out-of-place sequential writes 缓解随机写，但带来多组件查找、后台 merge、空间放大和延迟方差。本文的问题不是提出单一算法，而是回答这个设计空间里有哪些路线、各自解决什么、牺牲什么。

## 方法概览

### 组成部分

- Memory component: mutable write buffer，配合 WAL。
- Disk components: immutable sorted runs/SSTables/B+-tree-like components。
- Merge/compaction policy: leveling、tiering、hybrid/partitioned variants。
- Lookup optimizations: Bloom filters、component metadata、partition boundaries。
- Recovery/concurrency: WAL、component metadata log、snapshot/reference counting、multi-version read。

### 流程或协议

1. 写入进入 memory component 和 WAL。
2. 内存满后 flush 为磁盘 component。
3. 后台根据 policy 选择 components 合并到下一层或同层。
4. 读请求从新到旧查 memory/disk components，并用 Bloom filters/metadata 减少无效 I/O。
5. 范围查询合并多个 sorted streams，tiering 下需要处理更多组件。

### 关键定义、公式、算法或定理

- Bloom filter false positive: `(1 - e^{-kn/m})^k`，最优 `k = m/n ln 2`。
- Leveling write amplification: `O(T·L/B)`。
- Tiering write amplification: `O(L/B)`。
- 无 Bloom 点查: leveling `O(L)`，tiering `O(T·L)`。
- Space amplification: leveling `O((T+1)/T)`，tiering `O(T)`。
- RUM conjecture: 读、更新、内存/存储之间存在不可同时最优的 trade-off。

### 假设条件

- 讨论以排序 key-value/data records 为主。
- 成本模型依赖稳定 workload、size ratio、component organization、Bloom filter memory 和 page size 等参数。
- Survey 主要解释论文和系统层面的设计，不直接给出统一复现实验。

## 创新点

- 新思想: 不是提出新算法，而是把 LSM 研究按可复用的优化目标和 trade-off 建模。
- 对已有工作的扩展: 把原始 LSM、stepped-merge/tiering、LevelDB/RocksDB 工程实践和多篇研究论文放入同一设计空间。
- 工程或实证贡献: 对 LevelDB、RocksDB、HBase、Cassandra、AsterixDB 的 LSM 使用进行系统总结。
- 依赖的 prior work: 原始 LSM-tree、LFS、differential files、NoSQL systems、Bloom filters、B+-tree、RUM conjecture。

## 实验与结果

### 实验设置

本文是 survey，无统一实验设置；证据来自文献分类、成本模型和代表系统分析。

### 数据集或 Benchmark

无统一 benchmark。作者强调未来工作应更重视和 well-tuned baselines 比较，而不是只对默认 LevelDB/RocksDB。

### Baseline

许多被 survey 的论文使用 LevelDB/RocksDB 默认配置作为 baseline；作者认为这常常不够，因为 LSM-tree 本身可通过 size ratio、merge policy、Bloom filter memory 等参数调优。

### 指标

- write amplification
- point lookup cost
- range query cost
- space amplification
- merge overhead
- cache misses
- write stalls / latency variance
- implementation complexity

### 主要结果

主要结论是 qualitative taxonomy: 降低写放大的方法通常增加读放大、空间放大或系统复杂度；tiering 对点查可被 Bloom filters 缓解，但对范围查影响更大；key-value separation 能显著改善写入但会损害范围查询并引入 value log GC；auto-tuning 是必要方向。

### 消融实验

无统一消融实验；Table 3 可视作跨方法 trade-off summary。

### 效率、成本或安全性

效率核心是 I/O 模式和放大因子；安全性不是本文主题。成本还包括后台 compaction 对 foreground workload 的干扰和性能方差。

### 结果 caveat

由于本文汇总不同论文，实验环境不可比；作者尤其提醒不要把默认 LevelDB/RocksDB 当作强 baseline。

## 局限性

### 作者明确说明

- LSM 改进常有 trade-off，不存在单一最优方案。
- 研究评估应更重视 well-tuned baseline、space utilization 和性能方差。
- LSM 应从 key-value store 走向完整 database storage engine，需要考虑辅助结构维护、query optimization 和维护任务与查询执行的共同规划。

### 基于证据的推断

- 本文时间点为 2019，不覆盖后续 RocksDB/SQLite/PostgreSQL/云厂商 storage engine 的最新实践。
- 对新硬件的讨论反映当时 SSD/NVM/open-channel SSD 研究；当前硬件生态可能已经变化，需要后续 source 更新。

## 可复用思路

- 把 storage engine 设计理解为 RUM trade-off，而不是单项指标优化。
- 对任何“降低写放大”的方案，追问它把成本转移到了读、空间、GC、范围查询、复杂度还是尾延迟。
- 对系统论文评估，检查 baseline 是否调参、是否报告 space amplification、是否覆盖点查和范围查。
- LSM 上层知识节点应把 `leveling/tiering/hybrid/partitioned` 作为方法族，而不是把每个论文系统名都建为概念。

## 术语表

| Term | 中文说明 | 本文用途 |
| --- | --- | --- |
| LSM-tree | 日志结构合并树 | 写优化的存储引擎结构，通过内存缓冲和磁盘层级 merge 管理数据。 |
| SSTable | Sorted String Table | 现代 LSM 磁盘组件常用不可变 sorted run。 |
| Leveling | 分层合并策略 | 每层一个主要组件，读/空间好，写放大高。 |
| Tiering | 多组件分层策略 | 每层保留多个组件，写好，读/空间差。 |
| Compaction / merge | 后台合并 | 把多个组件重组，清理旧版本和删除标记，但制造 I/O。 |
| Bloom filter | 布隆过滤器 | 点查时判断 key 是否不在组件中，降低无效 I/O。 |
| Write amplification | 写放大 | 用户写入被后台 merge 反复写出的额外 I/O。 |
| Read amplification | 读放大 | 一次查询需要检查多个组件或页面。 |
| Space amplification | 空间放大 | 旧版本、重复组件或延迟清理导致占用超过逻辑数据量。 |
| RUM conjecture | RUM 权衡 | Read、Update、Memory/storage 不能同时最优的系统设计直觉。 |

## 连接

- 相关论文: 原始 LSM-tree paper 被本文作为 foundational prior work 引用，但本次队列下一项不是它，不在此 source note 深读。
- 相关仓库: LevelDB、RocksDB、HBase、Cassandra、AsterixDB 作为代表系统出现；未读取仓库源码。
- 相关 Knowledge nodes:
  - [[04_Knowledge/distributed-systems|Distributed systems]]
  - [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]
  - [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]]
  - [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines|LSM-tree Storage Engines]]
- 相关 Bridges: none
- Bridge 候选: 未来可在 `transaction-processing` 与 `storage-engines` 之间建立 database-engine bridge，但当前 source 证据主要在存储引擎内部，先不建 bridge。

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |
| `data-management-and-storage` | direction knowledge node | §1/§4 将 LSM 放在 NoSQL/data systems storage management 中 | active_seed | create parent node |
| `storage-engines` | problem/topic knowledge node | §2-§4 围绕 storage engine design | active_seed | create parent node |
| `lsm-tree-storage-engines` | method-family/topic knowledge node | 全文核心 | active | create detailed topic node |
| LevelDB/RocksDB/HBase/Cassandra/AsterixDB | representative instances | §4 | source_extension | 不建 foundation node |
| WiscKey/Monkey/Dostoevsky/PebblesDB 等 | route examples | §3 | source_only/source_extension | 先留在 source note 或路线表 |

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| LSM-tree 用 out-of-place sequential writes 改善写入但引入读/空间/merge 成本 | source claim | §2 | in-place vs out-of-place discussion and cost analysis | high | 上层节点基础定义 |
| Leveling 与 tiering 是核心 merge policy 家族 | source claim | §2.2 | Figure/description of merge policies and cost table | high | 上层方法族 |
| Bloom filters 主要缓解点查，不解决范围查询成本 | source claim | §2.3, §2.6, §3.8 | Bloom filter formula and range query discussion | high | 重要 trade-off |
| 多数降低写放大的技术会牺牲读、空间或复杂度 | synthesis from source | §3.8/Table 3 | author trade-off summary | high | 作为 `当前综合` |
| 未来评估需要 well-tuned baseline | author future direction | §5 | future directions | high | review/watchlist |
| LSM 应走向 database storage engine 级别的维护和查询协同 | author future direction | §5 | database storage engine discussion | medium | 可触发未来 parent expansion |

## 知识交接

- 留在本文元笔记的证据: 具体论文系统名、每篇被 survey 文献的细节、Table 2/3 的完整分类、LevelDB/RocksDB/HBase/Cassandra/AsterixDB 的系统摘录。
- 待更新 Knowledge node:
  - `distributed-systems`
  - `distributed-systems/data-management-and-storage`
  - `distributed-systems/data-management-and-storage/storage-engines`
  - `distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines`
  - `distributed-systems/research-dynamics`
- 作为哪些 Knowledge node 的 source extension: 主要是 `lsm-tree-storage-engines`；父级节点只记录代表 source 和新增下级结构。
- 需要补的 foundation knowledge/source: 原始 LSM-tree paper、B+-tree/storage engine foundation、RUM conjecture、RocksDB/LevelDB implementation sources。
- 待新增或复核 domain/direction/problem: 未来可考虑是否需要独立 `database-systems` 域；当前保持 `distributed-systems/data-management-and-storage`。
- Bridge 候选: storage engines 与 transaction processing / distributed databases 的 bridge，待更多 source。
- Watchlist 词条: LSM-tree, compaction, write amplification, RocksDB, Monkey, Dostoevsky, WiscKey, secondary indexing。
- 后续论文: 原始 LSM-tree、Monkey、Dostoevsky、WiscKey、RocksDB CIDR。
- 后续仓库: RocksDB, LevelDB。
- Review queue: 队列 metadata title 已更正；DOI/正式 venue 未核验。

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Storage engine | foundation_knowledge_candidate | 建/更新 `storage-engines` 节点，解释持久化、索引、更新、恢复、查询代价 | 只把它当作 LSM 论文里的词 | §1-§4 |
| LSM-tree | foundation/method_family_knowledge_candidate | 建 `lsm-tree-storage-engines` 节点，解释方法族、边界和 trade-off | 把每个 LSM 变体都建成基础概念 | §2-§3 |
| Leveling / tiering | method_family_section | 作为 LSM 节点内的主要路线，后续多 source 再拆 | 直接为每个 policy 建节点但缺 source coverage | §2.2 |
| LevelDB/RocksDB/HBase/Cassandra/AsterixDB | representative_instance_or_source_extension | 放入代表系统，不作为基础概念 | 把系统名当成领域/方向 | §4 |
| WiscKey/Monkey/Dostoevsky/PebblesDB | route examples/source-specific systems | 留在 source note 或路线表；多 source 后再判断 | 单篇 survey 提到就建节点 | §3 |

## Knowledge 综合交接

- 应创建 Knowledge node:
  - `vault/04_Knowledge/distributed-systems/data-management-and-storage.md`
  - `vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md`
  - `vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines.md`
- 应刷新 Knowledge synthesis section: `distributed-systems.md` 的下级结构、Source Extensions、当前综合；`distributed-systems/research-dynamics.md` 的学术关注和 open problems。
- 应标记过期: domain dynamics 仍不是最新趋势综述，保持 `stale` 或 `queued_refresh`。
- 无需更新的理由: 不创建 bridge，因为当前证据未形成跨节点 typed relationship；不创建代表系统独立节点，因为 split gate 未过。
- 建议 node kind: `direction`, `problem`, `method_family`。

## 处理日志

| Date | Run ID | Action | Result |
| --- | --- | --- | --- |
| 2026-06-20 | nahida-paper-intake-20260620-item-0033 | deep-read `1812.07527.pdf` and normalize metadata | source note ready for absorption |
