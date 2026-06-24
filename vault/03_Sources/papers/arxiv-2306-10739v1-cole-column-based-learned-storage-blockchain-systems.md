---
id: "arxiv:2306.10739v1"
title: "COLE: A Column-based Learned Storage for Blockchain Systems"
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
  - "p1-p2 abstract, introduction, storage bottleneck, contribution summary"
  - "p2-p3 blockchain storage model, MPT background, integrity and provenance functions"
  - "p3-p4 COLE overview and root-hash state digest"
  - "p4-p6 write path, Bloom filters, disk-optimized learned indexes, Merkle files"
  - "p7-p9 checkpoint-based asynchronous merge, Get, provenance query, verification"
  - "p9-p10 complexity analysis"
  - "p10-p12 implementation, workloads, baselines, storage/throughput/tail-latency/provenance experiments"
  - "p12-p14 related work, future work, conclusion, references"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2306.10739"
doi: ""
arxiv_id: "2306.10739v1"
venue: "PVLDB reference format / arXiv preprint"
year: "2023"
pdf_pages: 14
pdf_sha256: "d04a9d58d5740f4db6df6eb089e4cdeac1fc04b42cb208815ff0ad84160e0121"
local_pdf: "~/Desktop/paper/2306.10739.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/cole-a-column-based-learned-storage-for-blockchain-systems-d04a9d58d574-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "blockchain-state-storage"
  - "authenticated-state-indexing"
  - "provenance-queries"
ontology_path:
  - "blockchain-systems"
  - "data-management-and-storage"
  - "blockchain-state-storage"
primary_ontology_path: "blockchain-systems/data-management-and-storage/blockchain-state-storage/arxiv-2306-10739v1"
secondary_ontology_paths:
  - "distributed-systems/data-management-and-storage/storage-engines/arxiv-2306-10739v1"
  - "distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines/arxiv-2306-10739v1"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "data-management-and-storage"
    - "storage-engines"
  topics:
    - "blockchain-state-storage"
    - "authenticated-state-indexing"
    - "learned-indexes"
    - "lsm-tree-storage"
    - "provenance-queries"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "blockchain state storage"
  - "authenticated state indexing"
  - "learned index"
  - "LSM-tree maintenance"
  - "Merkle tree"
  - "provenance query"
aliases:
  - "COLE"
  - "Column-based Learned Storage"
  - "column-based learned storage for blockchains"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "data-management-and-storage"
  - "blockchain-state-storage"
  - "distributed-systems"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "data-management-and-storage"
    - "storage-engines"
  problem:
    - "full nodes store large historical state indexes and cannot drop old authenticated state without losing provenance"
    - "MPT-style authenticated state indexes duplicate update paths and make index storage dominate blockchain archival storage"
    - "learned indexes must be combined with integrity, provenance, disk writes, and deterministic block-level state digests"
    - "LSM-style background merge can improve write path but creates blockchain-specific root-digest synchronization problems"
  method_family:
    - "column-based state history layout over compound key <address, block>"
    - "disk-optimized learned index inspired by PGM-index"
    - "LSM-tree run maintenance with in-memory MB-tree and on-disk learned index files"
    - "Merkle files for value-file integrity"
    - "checkpoint-based asynchronous merge"
  system_layer:
    - "blockchain full-node storage"
    - "state index"
    - "historical state provenance query"
    - "integrity verification"
    - "write path and merge scheduler"
  evaluation_context:
    - "Rust prototype with Rust EVM"
    - "SmallBank and KVStore workloads"
    - "MPT, LIPP, and CMI baselines"
    - "100 transactions per block"
    - "T=4, m=4 default configuration"
  bridge:
    - "storage engines to blockchain state storage"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-cole-blockchain-storage"
source_refs:
  - "arxiv:2306.10739"
  - "arxiv:2306.10739v1"
  - "pdf:~/Desktop/paper/2306.10739.pdf"
  - "github:https://github.com/cezhang52111/cole-public"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> data-management-and-storage"
secondary_directions:
  - "distributed-systems -> data-management-and-storage -> storage-engines"
classification_status: "corrected"
classification_confidence: "high"
classification_evidence:
  - "abstract and introduction target blockchain storage overhead rather than consensus"
  - "Sections 3-6 define state storage layout, learned indexes, Merkle files, and merge scheduling"
  - "evaluation studies storage footprint, throughput, tail latency, and provenance queries against MPT/LIPP/CMI"
  - "queue path corrected from blockchain-systems/consensus/consensus-foundations to blockchain-systems/data-management-and-storage/blockchain-state-storage"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0059"
queue_status: "absorbed"
---

# COLE: A Column-based Learned Storage for Blockchain Systems

## 论文身份

- 标题: COLE: A Column-based Learned Storage for Blockchain Systems
- 作者: Ce Zhang, Cheng Xu, Haibo Hu, Jianliang Xu
- 机构: Hong Kong Baptist University; Hong Kong Polytechnic University
- 年份: 2023
- arXiv: `2306.10739v1`
- 论文声明 artifact: `https://github.com/cezhang52111/cole-public`
- 本地 PDF: `~/Desktop/paper/2306.10739.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/cole-a-column-based-learned-storage-for-blockchain-systems-d04a9d58d574-pages.txt`
- SHA-256: `d04a9d58d5740f4db6df6eb089e4cdeac1fc04b42cb208815ff0ad84160e0121`
- 备注: PDF 的 PVLDB reference format 行带有占位式卷期/页码信息；本 note 以 arXiv v1 日期和队列年份作为年份依据。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 14
- 已覆盖章节/页码: Abstract, Introduction, Preliminaries, COLE overview, Write, Asynchronous Merge, Get, Provenance Query, VerifyProv, Complexity, Evaluation, Related Work, Conclusion。
- Extraction gaps: 图中曲线精确数值只记录正文明确给出的结果；artifact repository 未重新读取。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | 全节点 storage bottleneck 主要来自 MPT index；COLE 以 column-based learned storage 缩小状态存储并保持 integrity/provenance | high |
| §2 / p2-p3 | 背景模型 | 定义 `Put`, `Get`, `ProvQuery`, `VerifyProv`；回顾区块头、state root、MPT 证明路径 | high |
| §3 / p3-p4 | 总体架构 | L0 in-memory MB-tree、多层 on-disk runs、value/index/Merkle files、root_hash_list 到 state digest | high |
| §4 / p4-p6 | 写路径和文件结构 | compound key `<addr, blk>`、Bloom filters、PGM-like learned index、Merkle file streaming construction | high |
| §5 / p7 | 异步 merge | start/commit checkpoints 与 writing/merging group 分离，避免不同节点因 merge 速度不同导致 state digest 不一致 | high |
| §6 / p7-p9 | 查询与证明 | Get 在 MB-tree/runs 中按 freshness 查找；ProvQuery 用边界 key 和 Merkle paths 证明区间完整性 | high |
| §7 / p9-p10 | 复杂度 | COLE storage `O(n)`，MPT storage `O(n*d_MPT)`；async merge 让 write tail latency 回到 `O(1)` | medium |
| §8 / p10-p12 | 评估 | Rust/EVM prototype；SmallBank/KVStore；MPT/LIPP/CMI baselines；storage、throughput、tail latency、provenance query | high |
| §9-§10 / p12-p14 | 相关工作与结论 | 学习索引、区块链存储管理、查询系统；未来支持 fork/rewind 和相邻状态压缩 | medium |

## 一句话贡献

COLE 把区块链全节点的 authenticated state storage 从“按每次更新持久化整条 Merkle 路径”转成“按账户/状态列组织历史值，再用 LSM-like runs、disk learned indexes 和 Merkle files 组合验证”，从而在不放弃 state root、point lookup 和 provenance proof 的前提下降低索引存储和写路径代价。

## 核心问题设定

全节点为了验证和重放需要长期保存状态历史。Ethereum-style MPT 会在每次更新时持久化从根到叶子的路径节点，使 index overhead 随区块高度快速膨胀。论文的预实验指出，在 1000 万次更新中 underlying data 只占存储的 4.2%，主要空间来自历史 MPT index nodes。直接把 learned index 接到 blockchain storage 上也不够，因为 naive learned index + persistent nodes + Merkle integrity 可能比 MPT 更大，论文报告在早期规模上就达到 MPT 的 5x 到 31x。

因此，这篇论文的持久知识不属于 consensus，而属于 [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain state storage]]：如何为全节点的状态索引同时满足小空间、可验证查询、历史 provenance、可落盘写入和可确定的 state digest。

## 方法与机制

### Column-based historical state layout

COLE 把同一个状态 key 的不同历史版本放在相邻位置。每条 value 用 compound key `<addr, blk>` 排序，其中 `addr` 是状态地址，`blk` 是区块高度。查询最新值时使用 `<addr, max_int>` 查找小于等于该 key 的最新记录；查询历史 provenance 时使用 `<addr, blk_l-1>` 和 `<addr, blk_u+1>` 作为边界，找到区间内的版本记录并证明没有缺失。

这一步是 COLE 和普通 MPT 之间最重要的形态差异: MPT 按当前 key 路径维护 authenticated trie，历史版本由路径节点持久化隐式保留；COLE 直接把历史版本变成可排序的数据列，让 provenance query 可以沿连续 key range 执行。

### LSM-like runs and root-hash state digest

系统维护一个 L0 in-memory MB-tree 和多层 on-disk runs。每个 on-disk run 包含:

- value file: 排序后的 compound key-value pairs。
- index file: disk-optimized learned index。
- Merkle file: 对 value file 生成的 Merkle tree。

当 L0 满时，COLE flush 成一个 L1 run。某层 run 数达到阈值 `T` 时 merge 到下一层。所有 MB-tree 和 Merkle file root hash 组成 `root_hash_list`，再被哈希成区块头里的 state root digest。这样，完整状态 digest 不依赖某一个 monolithic trie，而依赖当前所有有效 runs/trees 的 root hash 集合。

### Disk-optimized learned index

COLE 的 learned index 借鉴 PGM-index 的 piecewise linear model。每个 model 近似一段 key 到 position 的映射，包含 slope、intercept、range key 和最大 position 等元数据。模型保证预测误差在 `epsilon` 内；论文设置 `epsilon` 为半个 disk page 可容纳的 model 数，使一次预测最多需要读取两个相邻页。`BuildModel` 用 streaming convex-hull/minimal-parallelogram 方法构建误差有界模型，`ConstructIndexFile` 递归构建多层 index file，直到 top layer 可放进一个 disk page。

这里的关键边界是: learned model 本身不作为安全对象认证。模型损坏会让查询性能退化或失败，但数据完整性由 value file 的 Merkle file 证明。COLE 把“索引用于定位”和“Merkle 用于验证”明确分离。

### Merkle files

每个 value file 对应一个 m-ary complete MHT。底层叶子为 `hash(K || value)`，上层节点 hash 子节点串联。论文给出 streaming construction: 各层维护 buffer，value record 到达时生成 bottom hash，buffer 满 `m` 个就向上一层推进。这样构建 Merkle file 不需要把整棵树一次性放入内存。

### Checkpoint-based asynchronous merge

普通 LSM merge 会造成 write stalls；但区块链里直接采用通用异步 merge 会带来新问题: 不同节点 merge 速度不同，同一高度的 storage structure/root digest 会不一致。COLE 的做法是对每层维护 writing group 和 merging group，并在 start checkpoint 与 commit checkpoint 之间隔离 merge 线程。

流程是:

- writing group 满时，如果前一次 merge 未完成则等待。
- commit checkpoint 同步更新 `root_hash_list`，移除旧 run hash，加入 merge 后 run hash。
- 删除旧 runs，交换 writing/merging group 角色。
- 后台线程开始处理新的 merging group。

论文的 soundness 论证依赖一个边界: `H_state` 只在同步 checkpoint 修改，后台线程不直接改状态摘要。因此异步 merge 可以减少 tail latency，同时保持所有节点的 state digest 更新顺序一致。

## 查询与证明

### Get

`Get(addr)` 先查 L0 writing/merging MB-tree，再查各层 runs。对 runs 的搜索按 freshness 顺序执行，并跳过尚未 commit 的 writing group runs。`SearchRun` 先用 Bloom filter 检查地址，再在 index top layer 做 binary search，逐层用 learned model 预测位置，最后在预测页或邻页中二分查找。

### ProvQuery

`ProvQuery(addr, [blk_l, blk_u])` 查找同一地址在区块区间内的所有历史版本。为了证明完整性，它还查询 `<addr, blk_l-1>` 和 `<addr, blk_u+1>` 两个边界。证明内容包括:

- 查询到的 key-value records。
- MB-tree proofs 或 Merkle paths。
- 未搜索 runs 的 root hashes。
- 边界 keys 的存在/不存在证明。

验证者重建相关 MB-tree/run roots，再与未搜索 root hashes 组合出 `H_state`。如果边界结果和区间结果一致，验证者可以确认区间内没有被遗漏的版本。

## 复杂度与系统边界

论文对比认为 MPT storage 为 `O(n*d_MPT)`，COLE 为 `O(n)`。COLE 写入 I/O 与层数相关，async merge 将 write tail latency 从可能随 merge size 增长的 `O(n)` 降为前台路径上的 `O(1)`。Get 需要在层级和 runs 中使用 Bloom filters/learned index 查询，Provenance proof size 与 Merkle fanout、层数和区间结果相关。

边界条件:

- 论文聚焦 non-forking blockchain systems，明确不支持 rewind。
- COLE 优化 full-node state storage，不解决 consensus safety、data availability、light-client networking 或 transaction validity。
- Learned index 只用于定位；安全性仍依赖 Merkle files 和 state digest。
- Async merge 的正确性依赖 checkpoint discipline 和 deterministic root hash updates。

## 实验设置与结果

实现使用 Rust，接入 Rust EVM 执行交易。每个 block 含 100 笔交易，初始有 10 个 smart contracts。默认配置为 page size 4KB、`epsilon=23`、size ratio `T=4`、MHT fanout `m=4`。机器为 Intel i7-10710U、16GB 内存、Samsung SSD、Ubuntu 20.04。

Baselines:

- MPT: Ethereum-style persistent Merkle Patricia Trie。
- LIPP: updatable learned index with persistence，但无 COLE 的 column-based design。
- CMI: column-based Merkle Index，用传统 Merkle/MB-tree 和 RocksDB 实现两层结构。

Workloads:

- SmallBank。
- KVStore，覆盖 read-only、read-write、write-only 场景。
- Provenance query: 固定基础状态后连续写入，对随机 key 查询不同 block-height range。

主要结果:

- Storage: 在 block height `10^5`，COLE 相比 MPT 在 SmallBank 减少 94% storage，在 KVStore 减少 93%。
- Throughput: COLE 相比 MPT 提升约 1.4x 到 5.4x。
- Tail latency: COLE* 的 checkpoint async merge 在 `10^4`/`10^5` 高度将 long-tail latency 降低 1 到 2 个数量级，但 median latency 略高于同步 COLE。
- Learned-index baseline: LIPP 在早期规模已经达到 MPT 的 5x/31x storage，并无法在 24 小时内完成更大规模实验。
- CMI: 没有明显 storage 改善，且在 `10^4` 高度吞吐比 MPT 慢 7x/22x，难以扩展到更大高度。
- Provenance query: MPT 的 CPU/proof size 随查询区间近似线性增长；COLE/COLE* 呈 sublinear 变化，但小区间 proof size 可能更大，因为 Merkle path sharing 有限。

## 与现有知识库的关系

| 位置 | 关系 | 为什么放这里 |
| --- | --- | --- |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain state storage]] | primary topic | COLE 的核心问题是 full-node state/index storage，而不是 consensus |
| [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain data management and storage]] | parent direction | 把 blockchain storage、state history、authenticated query 和 provenance 统一收纳 |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | secondary direction | COLE 复用 learned indexes、LSM-like runs、Bloom filters 和 merge scheduling |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines|LSM-tree Storage Engines]] | source extension | COLE 的 run/merge/checkpoint 问题是 LSM 思想在区块链 state root 下的专门化 |
| [[05_Bridges/storage-engines-to-blockchain-state-storage|Storage engines -> blockchain state storage]] | bridge | 记录存储引擎机制如何迁移到 blockchain authenticated state storage，以及哪些边界不能迁移 |

## 可吸收的知识增量

| Delta | Reusable placement | Notes |
| --- | --- | --- |
| Blockchain full-node storage bottleneck can be dominated by authenticated index history rather than raw state values. | Blockchain state storage | source-backed problem framing |
| Column-based layout over `<address, block>` turns state history into a range-queryable storage problem. | Blockchain state storage | method route |
| Learned indexes can serve blockchain storage only when separated from integrity verification. | Bridge: storage engines -> blockchain state storage | transfer boundary |
| LSM-style async merge needs checkpointed root-hash updates in blockchain systems. | Blockchain state storage; LSM source extension | trust/determinism boundary |
| Provenance queries need both interval results and boundary proofs to prove completeness. | Blockchain state storage | method route |

## 不应直接提升为基础概念的内容

- `COLE` 不应变成基础概念；它是 source/system instance。
- `COLE*` 不应单独建节点；它是 COLE 的 async-merge variant。
- `LIPP`、`CMI` 在本库当前只作为 baseline，不单独建 source-backed knowledge node。
- 论文里的 Rust prototype 细节留在 source note；除非后续读取 artifact 仓库，否则不建 repo/source note。

## 后续缺口

| Gap | Why it matters | Suggested action |
| --- | --- | --- |
| Learned index 基础概念未在 vault 中独立建立 | COLE 用 PGM-like learned index，但当前只可作为 storage engine 方法引用 | 后续用 `nahida-research-search` 或读取 PGM/ALEX/LIPP 论文 |
| Blockchain state storage 目前主要由 COLE 支撑 | 需要 MPT/ForkBase/stateless clients/state expiry 等 source 扩展 | 后续吸收相关论文/仓库 |
| COLE 不支持 fork/rewind | 区块链实际系统常需要重组、回滚或 state pruning | 后续遇到 forkable authenticated storage 再扩展 |

## Knowledge Handoff

| Target | Update |
| --- | --- |
| `blockchain-systems/data-management-and-storage` | 新建方向节点，承接 blockchain storage 与 state/history/provenance 的数据管理问题 |
| `blockchain-systems/data-management-and-storage/blockchain-state-storage` | 新建 problem node，吸收 COLE 的 reusable problem/method routes |
| `distributed-systems/data-management-and-storage/storage-engines` | 增加 COLE 作为 storage-engine mechanisms 在 blockchain trust/digest 边界下的 source extension |
| `distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines` | 增加 LSM-like run/merge/checkpoint 的 cross-domain specialization |
| `05_Bridges/storage-engines-to-blockchain-state-storage` | 新建 bridge，明确 learned index、LSM、Bloom filter、Merkle proof 的迁移边界 |

