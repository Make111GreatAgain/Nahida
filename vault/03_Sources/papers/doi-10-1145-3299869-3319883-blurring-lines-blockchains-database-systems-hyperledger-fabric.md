---
id: "doi:10.1145/3299869.3319883"
title: "Blurring the Lines between Blockchains and Database Systems: the Case of Hyperledger Fabric"
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
  - "p1 abstract, keywords, introduction"
  - "p2-p4 blockchain order-execute model, Hyperledger Fabric architecture, simulate-order-validate workflow"
  - "p4-p6 related database concurrency-control work and Fabric-specific transfer boundaries"
  - "p6-p9 Fabric++ transaction reordering, conflict graph, cycle handling, batch cutting, early abort"
  - "p9-p14 experimental setup, Smallbank/custom workload evaluation, scalability, Caliper comparison"
  - "p14-p18 conclusion, references, Fabric running example, reordering microbenchmarks"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1145/3299869.3319883"
doi: "10.1145/3299869.3319883"
arxiv_id: ""
venue: "SIGMOD '19"
year: "2019"
pdf_pages: 18
pdf_sha256: "49b11d97793aa32306b2e4221ddd9262c807251599ecac1a0339d666e351c0ff"
local_pdf: "~/Desktop/paper/3299869.3319883.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/blurring-the-lines-between-blockchains-and-database-systems-the-case-of-hyperledger-fabric-49b11d97793a-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
topic_ids:
  - "transaction-processing"
  - "execute-order-validate"
  - "database-inspired-blockchain-transaction-processing"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing/doi-10-1145-3299869-3319883"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing/doi-10-1145-3299869-3319883"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "execution-and-transactions"
    - "transaction-processing"
  topics:
    - "Hyperledger Fabric transaction processing"
    - "execute-order-validate"
    - "transaction reordering"
    - "optimistic concurrency control"
    - "early abort"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "Hyperledger Fabric"
  - "Fabric++"
  - "execute-order-validate"
  - "transaction reordering"
  - "early transaction abort"
  - "optimistic concurrency control"
  - "serializability"
  - "Smallbank"
aliases:
  - "Fabric++"
  - "Blurring the Lines between Blockchains and Databases"
  - "Hyperledger Fabric transaction reordering"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
  - "distributed-systems"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "execution-and-transactions"
    - "transaction-processing"
  problem:
    - "Hyperledger Fabric's simulate-order-validate pipeline aborts many transactions after ordering because arrival order ignores read/write conflicts"
    - "vanilla Fabric discovers doomed transactions late, after simulation, ordering, block distribution, and validation work"
    - "database concurrency-control ideas must be adapted to Fabric's block granularity, replicated trust model, endorsement, signatures, and ordering service"
  method_family:
    - "block-local transaction reordering using read/write-set conflict graph"
    - "greedy cycle-breaking abort before block dissemination"
    - "simulation-phase early abort for stale reads"
    - "ordering-phase early abort for same-block version mismatch"
    - "unique-key-aware batch cutting"
  system_layer:
    - "Hyperledger Fabric endorsers"
    - "ordering service"
    - "validation phase"
    - "ledger commit"
    - "LevelDB state database"
  evaluation_context:
    - "Hyperledger Fabric prototype"
    - "Smallbank workload"
    - "custom hot-key workload"
    - "Caliper comparison"
    - "6-server LAN deployment"
  bridge:
    - "database transaction processing to blockchain execution"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-fabric-plus-plus-transaction-processing"
source_refs:
  - "doi:10.1145/3299869.3319883"
  - "pdf:~/Desktop/paper/3299869.3319883.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> execution-and-transactions"
secondary_directions:
  - "distributed-systems -> transaction-processing"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "abstract explicitly analyzes Hyperledger Fabric transaction processing from a database perspective"
  - "Sections 3-4 describe Fabric's simulate-order-validate pipeline, transaction reordering, and early abort"
  - "evaluation measures successful transaction throughput and latency under Smallbank/custom workloads"
  - "queue path corrected from blockchain-systems/consensus/consensus-foundations to blockchain-systems/execution-and-transactions/transaction-processing"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0061"
queue_status: "absorbed"
---

# Blurring the Lines between Blockchains and Database Systems: the Case of Hyperledger Fabric

## 论文身份

- 标题: Blurring the Lines between Blockchains and Database Systems: the Case of Hyperledger Fabric
- 作者: Ankur Sharma, Felix Martin Schuhknecht, Divya Agrawal, Jens Dittrich
- 机构: Big Data Analytics Group, Saarland University
- 会议: SIGMOD '19
- 年份: 2019
- DOI: `10.1145/3299869.3319883`
- 本地 PDF: `~/Desktop/paper/3299869.3319883.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/blurring-the-lines-between-blockchains-and-database-systems-the-case-of-hyperledger-fabric-49b11d97793a-pages.txt`
- SHA-256: `49b11d97793aa32306b2e4221ddd9262c807251599ecac1a0339d666e351c0ff`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 18
- 已覆盖章节/页码: Abstract, Introduction, Blockchain transaction management, Hyperledger Fabric architecture, database related work, Fabric++ reordering, early abort, evaluation, conclusion, references, Appendix A/B。
- Extraction gaps: 图 7-17 的曲线细粒度逐点值未 OCR；本文只记录正文报告的关键数值、趋势和表格数据。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p3 | 问题与贡献 | 将 Fabric 交易处理与数据库 OCC 类比；提出 transaction reordering 和 early abort；报告最高 12x successful throughput、平均 latency 近半 | high |
| §2.1 / p3 | Order-execute 背景 | Bitcoin/Ethereum 类系统先排序再顺序执行，不能利用多核和 peer 扩展 | medium |
| §2.2 / p3-p5 | Fabric 架构 | Endorsement/simulation、ordering、validation、commit；readset/writeset、endorsement policy、serialization conflict | high |
| §2.3 / p5-p6 | 相关数据库工作 | 区分提高 raw throughput 与减少 abort 两类方法；说明 Fabric 的瓶颈和传统数据库不同 | high |
| §3 / p6-p9 | Fabric++ 方法 | conflict graph reordering、cycle detection/greedy abort、unique-key batch cutting、simulation/order early abort | high |
| §4 / p9-p14 | 实验 | 6-server Fabric prototype；Smallbank/custom workload；blocksize、skew、hot records、channels、clients、Caliper | high |
| §5 / p14 | 结论 | 数据库社区的事务管理思想可改善 Fabric，但必须适配区块链架构 | medium |
| Appendix A / p15-p17 | Fabric 示例 | 用完整 running example 展示 arrival order 如何导致 valid/invalid 差异 | high |
| Appendix B / p17-p18 | Reordering 微基准 | 大 block 下 reordering 约毫秒级；cycle 长度影响 runtime 和 valid count | medium |

## 一句话贡献

这篇论文把 Hyperledger Fabric 的 simulate-order-validate 管线解释为一种区块链化的乐观并发控制，并提出 Fabric++: 在 ordering/validation 前利用 read/write set 重排区块内交易、提前中止不可避免冲突交易，从而提升有效吞吐并降低无效交易带来的延迟。

## 核心问题设定

Fabric 的 raw throughput 不等于 successful transaction throughput。Vanilla Fabric 的 ordering service 默认按交易到达顺序组块，不理解交易语义；peer 在 validation 阶段才检查 endorsement policy 和 readset version。如果 block 中早到的交易写了后到交易读过的 key，后到交易会被标记 invalid，即使存在另一种 block 内顺序可以让更多交易有效。

论文把这个问题连接到数据库事务管理:

- Simulation 类似乐观执行: endorser 在当前 state 上执行 chaincode，返回 readset/writeset。
- Ordering 类似给事务选择 serialization order: orderer 生成 block 内顺序。
- Validation 类似 OCC validation: peer 检查读版本是否仍匹配。
- Commit 把 valid transaction 的 writeset 应用到 state，同时把 valid/invalid 交易都写入 ledger。

这不是 consensus 安全问题。排序服务仍负责全局交易顺序/区块广播，论文优化的是执行层如何在给定候选交易集合中减少因并发冲突导致的无效交易。

## Fabric 工作流

论文将 Fabric 交易流拆成四段:

1. Simulation: 客户端向 endorsement policy 要求的 endorsers 发送 proposal；endorsers 并行执行 chaincode，返回 readset/writeset 和签名。
2. Ordering: 客户端收集足够 endorsement 后把交易交给 ordering service；orderer 给交易排序并切成 blocks，但不检查交易语义。
3. Validation: 每个 peer 检查 endorsement policy、签名，以及 readset 中每个 key 的版本是否仍等于模拟时看到的版本。
4. Commit: 整个 block 追加到 ledger；只有 valid 交易的 writeset 更新 state；invalid 交易也留在 ledger 中作为历史。

论文强调 Fabric 与传统并行数据库不同:

- Fabric 以 block 为 commit 单位，而不是单事务即时提交。
- 每个 peer 都有完整复制状态，传统数据库通常关注 partition/locality。
- Simulation 在多个互不完全信任的 endorsers 上发生，节点 state 可能不同。
- 性能瓶颈更多来自签名、网络、endorsement/validation，而不是纯并发控制 primitive。

因此，直接套用“提高数据库事务执行吞吐”的方法并不合适；更重要的是减少无效交易，让有限 block/validation 带宽承载更多 successful transactions。

## Fabric++ 方法

### Transaction reordering

Fabric++ 把 block 内交易集合视为可重排对象。若交易 `Ti` 写某个 key，而交易 `Tj` 在 simulation 时读了旧版本 key，则为了让 `Tj` 保持 valid，`Tj` 应该排在 `Ti` 前面。论文据此定义冲突边 `Ti -> Tj`，表示 reordering 时需要让 `Tj` 先于 `Ti`。

算法流程:

- 从每笔交易的 readset/writeset 构建 conflict graph。
- 用 read/write bit-vectors 做 pairwise conflict 检测，复杂度约 `O(n^2)`；block size 有限时可接受。
- 用 Tarjan 算法找 strongly connected components，再用 Johnson 算法枚举 cycles。
- 若 conflict graph 有 cycle，则不可能保留所有交易；Fabric++ 贪心删除出现在最多 cycles 中的交易，直到 graph 无环。
- tie-break 采用 deterministic rule，保证所有节点重排结果一致。
- 对剩余 DAG 得到一个 serializable schedule，再反转为 block 内提交顺序。

这个 cycle-breaking 不是最优最少 abort；论文承认找到最小交易删除集是 NP-hard，因此选择轻量启发式。

### Batch cutting

Vanilla Fabric 按交易数、block byte size 或时间切 block。Fabric++ 增加 “unique accessed keys per block” 条件: 如果 block 访问的 unique key 数量达到阈值，就提前切 block。这样可以限制 conflict graph 的规模，避免 reordering runtime 随热点/大 block 不可控增长。

### Early abort

论文把 early abort 分成 simulation phase 和 ordering phase。

Simulation-phase early abort:

- Fabric 原本可用全局 read-write lock 保证 simulation 和 validation 不交错，但锁会限制并发。
- Fabric++ 改成更细粒度/近似 lock-free 的方式，利用 Fabric 已有 version number。
- 交易开始 simulation 时记录 `last-block-ID`。
- 如果交易读到的某个 value version 来自比 `last-block-ID` 更晚的 block，说明 simulation 与验证并发交错导致快照不一致，可以立即 abort 并通知客户端重试。
- Version updates 需要原子化，避免读取中间状态。

Ordering-phase early abort:

- 如果同一 block 内两笔交易读同一个 key 但读到不同版本，读旧版本的交易在 block 顺序下必然无效，可以在 block 分发前 abort。
- Reordering 本身也会删除 cycle 中的部分交易，因此这些交易不再进入后续 validation/commit 路径。

## 实验与证据

| 维度 | 设置/结果 | 证据锚点 | Caveat |
| --- | --- | --- | --- |
| 实验环境 | 6 台同 rack 服务器，gigabit network；4 peers、1 ordering service、1 client；双 quad-core Xeon E5-2407 2.2GHz，Arch Linux 4.17，Fabric + LevelDB | §4.1 | 许可链 LAN 设置，不代表开放网络 |
| Workloads | Smallbank 100k users，write probability `Pw=95/50/5`，Zipf skew `s=0..2.0`；custom workload 10k accounts，RW=4/8，HR=10/20/40%，HW=5/10%，HSS=1/2/4% | §4.1 | 以账户型读写冲突为主 |
| Block size | block size 16 到 2048 增大时，两者 successful throughput 都提高；Fabric++ 在大 block 下收益更明显；默认选择 1024 | §4.2 | 大 block 也增加 reordering 搜索空间 |
| Smallbank throughput | 低/无 skew 时 Fabric++ 约 1000 successful tx/s，Fabric 约 900；高 skew `s=2.0` 时提升 2.68x 到 12.61x；写密集高 skew 下 Fabric 约 30 tx/s，Fabric++ 约 370 tx/s | §4.2 | 数值来自作者图表/正文描述 |
| Custom workload | 36 个配置下 Fabric++ 均提升；BS=1024、RW=8、HR=40%、HW=10%、HSS=1% 时最高约 3x | §4.2 | 热点和读写比例决定收益 |
| 优化拆分 | 在 BS=1024、RW=8、HR=40%、HW=10%、HSS=1% 下，Fabric 约 100 tx/s；仅 reordering 或仅 early abort 约 150；两者组合约 220 | §4.2 | 两种优化有协同，不宜只看单项 |
| Channels | 1 到 4 个 channels 提升两者吞吐；8 channels 因资源竞争下降，failed txs 增加 | §4.2 | 并行 channel 会带来资源争用 |
| Clients/channel | Fabric 从 1 到 8 clients 缓慢升至约 105；Fabric++ 在 2 clients 左右约 205，8 clients 时约减半 | §4.2 | client 并发升高会增加冲突和失败交易 |
| Caliper | 150 tx/s/client，总 600 tx/s，block size 512；Fabric++ 平均 latency 0.28s vs Fabric 0.47s，successful TPS 299 vs 188 | §4.3, Table 1 | 与作者自研框架不同，rate 较低 |
| Reordering 微基准 | 对 1024 tx 的 interleaved read/write workload，reordering 可让所有交易 valid，runtime 约 1-2 ms；cycle 长度越大 runtime 越高 | Appendix B | MacBook Pro i7 microbenchmark，不是完整 Fabric 跑分 |

## 相关工作边界

- Vanilla Fabric: 论文优化的是 Fabric 的 transaction pipeline，不改 consensus safety 或 endorsement model。
- Fabric++ 与后续 FabricSharp/FastFabricSharp: 本文是 Fabric++ 原始路线之一，主要做 block-local reordering 和 early abort；后续 [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]] 批评 Fabric++ 只处理 block-scope reordering，进一步引入跨 block pending transactions 的 OCC/serializability dependency analysis。
- Blockchain Meets Database: [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] 把 PostgreSQL/SSI/MVCC 作为执行 substrate；本文不替换 Fabric state/execution substrate，而是在 Fabric 管线中迁移数据库事务管理思想。
- 经典数据库并发控制: 提供 OCC、transaction reordering、early abort 的思想来源，但 Fabric 的签名、endorsement、block commit、全复制和互不信任 peer 模型使其不能直接照搬。

## 限制与边界

- 适用对象是 permissioned Hyperledger Fabric 风格系统；不讨论 permissionless incentives、Sybil resistance 或开放网络治理。
- Reordering 只在当前 block 范围内工作；跨 block concurrent transactions 的依赖可能仍被漏掉。
- Cycle-breaking 是贪心启发式，不保证最少 abort。
- 算法依赖 readset/writeset 可见；隐私 channel、private data、或不愿向 orderer 暴露访问集合的场景需要额外设计。
- 性能结论基于 Fabric 当时实现和作者环境；现代 Fabric、不同数据库后端、不同 endorsement policy 可能改变瓶颈。
- 论文优化 successful throughput，但不替代共识层的 ordering availability、Byzantine orderer 安全或 endorsement policy 正确性。

## Knowledge Handoff

| Candidate | Generality class | Target handling | Reason |
| --- | --- | --- | --- |
| Fabric++ | source instance / method route | keep source-specific details here; add method/source-extension rows in transaction-processing nodes | 单篇论文系统名，不应升成基础概念节点 |
| Execute-order-validate transaction processing | method/architecture route | strengthen [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | 多篇 Fabric/EOV source 已形成可复用交易处理路线 |
| Transaction reordering over read/write conflict graph | method route | update transaction-processing and bridge pattern | 可迁移思想来自数据库并发控制，但需适配 block/orderer determinism |
| Early abort in Fabric pipeline | method route | update bridge and source-extension rows | 减少 doomed transaction 在区块链 pipeline 中浪费网络/验证资源 |
| Unique-key-aware batch cutting | implementation detail / tuning route | keep in source note, mention only as boundary if needed | 目前是 Fabric++ tuning，不足以单独成节点 |

## Cold-Start Hierarchy Discovery

| Facet | Value | Durable handling |
| --- | --- | --- |
| Research field/domain | Blockchain systems; distributed transaction processing | `blockchain-systems` primary, `distributed-systems` secondary |
| Research background | Fabric supports parallel simulation but validation abort wastes effective throughput | background/update in transaction-processing |
| Research problem | Reduce serialization-conflict invalid transactions and late abort in Fabric EOV pipeline | source extension under transaction-processing |
| Foundation concepts | optimistic concurrency control, conflict graph, serializability, early abort | `distributed-systems/transaction-processing` bridge evidence; direct foundation still queued |
| Method family | block-local transaction reordering and early abort | method route |
| Application/evaluation context | Hyperledger Fabric, Smallbank, custom hot-key workloads | source detail |
| Source instance | Fabric++ | source-only/system instance |

## Retrieval Optimization

- 未来问“Fabric++ 解决什么问题”时，直接读本 note 的核心问题、方法与实验。
- 未来问“Fabric++ 和 FabricSharp/FastFabricSharp 区别”时，先读本 note，再读 [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]]。
- 未来问“数据库事务思想如何迁移到区块链执行层”时，优先进入 [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]]，本 note 提供 Fabric pipeline 证据。
- 仍保留 source-only 的内容: Tarjan/Johnson 组合、cycle participation tie-break、Smallbank/custom workload 的具体参数、Caliper 表格和 reordering microbenchmark。

## Relation Extraction

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| `doi:10.1145/3299869.3319883` | instance_of | `blockchain-systems/execution-and-transactions/transaction-processing` | abstract, §2-§4 | high | active_seed |
| `doi:10.1145/3299869.3319883` | bridges | `distributed-systems/transaction-processing -> blockchain-systems/execution-and-transactions/transaction-processing` | §2.3, §3 | high | active_seed |
| `Fabric++ transaction reordering` | solves | invalid transaction reduction in Fabric EOV pipeline | §3, §4 | high | source_extension |
| `Fabric++ early abort` | mitigates | late abort and wasted validation/network work | §3.3, §4 | high | source_extension |
| `unique-key batch cutting` | bounds | reordering runtime under large blocks | §3.2 | medium | source_only |

## 吸收决策

- Queue 原分类 `blockchain-systems/consensus/consensus-foundations` 精读后修正为 `blockchain-systems/execution-and-transactions/transaction-processing`。
- Primary path 放入 `blockchain-systems/execution-and-transactions/transaction-processing`，因为 durable problem 是 Fabric 交易执行、冲突检测、reordering 和 abort。
- Secondary path 传播到 `distributed-systems/transaction-processing`，因为论文直接以数据库 transaction management/OCC 解释并改造 Fabric。
- 不新建 `Fabric++` 知识节点；它是 source instance。EOV 目前保持为方法路线/候选 child，等 Fabric++、FabricSharp、Nezha、parallel EVM 等更多来源继续进入后再复核 split gate。

## Review Items

| Item | Reason | Status |
| --- | --- | --- |
| 经典 OCC/serializability/transaction reordering foundation source 仍缺 | 本文是强迁移证据，但不是数据库事务基础教材 | queued |
| EOV 是否拆成 child method node | Fabric++ 与 FabricSharp 已形成强信号，但仍需更多 EOV/parallel blockchain execution sources 对齐 | review |
| Fabric++ 与 modern Fabric 版本差异 | 论文基于当时 Fabric 实现，现代实现可能改变瓶颈 | optional_future_source |
