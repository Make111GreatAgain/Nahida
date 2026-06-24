---
id: "sha256-e1d0bc04b53e"
title: "Calvin: Fast Distributed Transactions for Partitioned Database Systems"
type: "source"
source_kind: "paper"
schema_version: "1.0"
status: "absorbed"
created: "2026-06-23"
updated: "2026-06-23"
authors:
  - "Alexander Thomson"
  - "Thaddeus Diamond"
  - "Shu-Chun Weng"
  - "Kun Ren"
  - "Philip Shao"
  - "Daniel J. Abadi"
year: 2012
venue: "SIGMOD 2012"
publisher: "ACM"
source_refs:
  - "sha256:e1d0bc04b53e5702d2f0d52b5bb1e561ff25fdf3490402c98abdb94c81281818"
  - "acm-proceedings-isbn:978-1-4503-1247-9/12/05"
canonical_url: ""
local_pdf_path: "~/Desktop/paper/calvin.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/home-accts-agt5-papers-preproc-contention.eps-e1d0bc04b53e-pages.txt"
pages: 12
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
primary_domain: "distributed-systems"
primary_direction: "transaction-processing"
primary_ontology_path: "distributed-systems/transaction-processing/distributed-transactions"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing"
  - "distributed-systems/data-management-and-storage/storage-engines"
  - "blockchain-systems/execution-and-transactions/transaction-processing"
topic_ids:
  - "distributed-transactions"
  - "deterministic-database-systems"
  - "deterministic-transaction-scheduling"
  - "transaction-input-replication"
  - "distributed-database-systems"
  - "disk-backed-transaction-processing"
knowledge_node_refs:
  - "[[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]]"
  - "[[04_Knowledge/distributed-systems/transaction-processing/distributed-transactions|Distributed transactions]]"
bridge_refs:
  - "[[database-transaction-processing-to-blockchain-execution]]"
queue_id: "nahida-paper-domain-serial-queue-20260611-v2"
queue_item_id: "item0101"
run_id: "nahida-paper-intake-20260623-calvin"
---

# Calvin: Fast Distributed Transactions for Partitioned Database Systems

## Source Identity

| 字段 | 内容 |
| --- | --- |
| 论文 | Calvin: Fast Distributed Transactions for Partitioned Database Systems |
| 作者 | Alexander Thomson; Thaddeus Diamond; Shu-Chun Weng; Kun Ren; Philip Shao; Daniel J. Abadi |
| 会议 | SIGMOD 2012 |
| 页数 | 12 |
| 本地文件 | `~/Desktop/paper/calvin.pdf` |
| 摘要定位 | 分布式数据库系统、确定性调度、分布式事务、复制、事务处理 |

## One-Sentence Takeaway

Calvin 把分布式事务的全局顺序和复制协议前移到事务执行之前，再用确定性锁管理让所有副本按同一输入序列执行，从而把传统 2PC 在锁持有期间造成的高竞争成本从事务临界区中移出去。

## Cold-Start Position

| 层级 | 定位 |
| --- | --- |
| 领域 | 分布式系统 |
| 方向 | 事务处理 |
| 问题域 | 分区数据库中的分布式 ACID 事务 |
| 方法族 | 确定性数据库系统、确定性事务调度、事务输入复制 |
| 具体系统 | Calvin |
| 可迁移关系 | 数据库事务处理中的“先排序再执行”可以映射到区块链执行层中的全局排序、确定性执行与并行调度问题，但 Byzantine 环境、智能合约非确定性和读写集声明约束需要额外处理。 |

## Problem

分区和复制能让存储系统横向扩展，但多分区 ACID 事务常被认为会破坏可扩展性。论文将主要瓶颈归结为传统分布式事务的提交时协调：事务在执行过程中获得锁，随后还要在锁持有期间完成 2PC 之类的提交协议；在高竞争负载下，这会显著扩大每个事务占用冲突资源的时间窗口。

论文把这个窗口称为竞争足迹：事务持有锁的总时长，不只包括业务逻辑执行，也包括网络消息、提交决策和协调协议。竞争越高，额外几毫秒的协调时间越容易转化成吞吐下降、排队和潜在级联阻塞。

## Main Idea

Calvin 的核心不是让分布式事务“不需要共识”，而是把必须达成一致的内容从“事务执行后的提交结果”换成“事务执行前的输入顺序”。系统先让 sequencer 层对事务输入达成全局顺序并复制输入日志，然后 scheduler 层按该顺序请求锁并执行事务。只要每个副本看到相同输入序列，并且并发控制保证等价于这个序列化顺序，副本就能独立执行出相同结果。

这样，节点故障不再需要让正在执行的事务以非确定性方式 abort；系统可以依赖其他副本和输入日志重放来恢复。确定性调度也让多分区事务不需要在事务末尾运行传统分布式提交协议来决定提交或回滚，因此锁持有时间不再包含提交时协调。

## Architecture

Calvin 被设计为位于普通 CRUD 存储层之上的事务调度和复制层。它不要求底层存储引擎本身具备分布式事务能力，而是把事务、并发控制和复制从物理存储中拆出来。

| 层 | 作用 |
| --- | --- |
| Sequencing layer | 接收事务输入，形成全局输入序列，负责输入日志复制和跨副本一致排序。 |
| Scheduling layer | 按确定性顺序获取锁，执行事务逻辑，保证并发执行结果等价于 sequencer 给出的串行顺序。 |
| Storage layer | 提供 CRUD 接口和物理数据布局；可以是内存或磁盘存储，也可以由已有存储系统承载。 |

这种拆分的代价是 Calvin 只能直接看到逻辑记录，不能自然复用传统数据库里的 ARIES/physiological logging、next-key locking 等和物理存储结构紧耦合的机制。论文把范围锁和 phantom 问题留给未来的 virtual resources 机制。

## Sequencing And Replication

Calvin 把时间划成 10ms epoch。每个 sequencer 在一个 epoch 内收集客户端请求，形成本地 batch。batch 被复制后，sequencer 将包含节点 ID、epoch 编号和相关事务输入的消息发送给 scheduler。每个 scheduler 用确定性的 round-robin 规则把不同 sequencer 的 batch 交织起来，得到相同的全局事务顺序。

复制有两种模式：

| 模式 | 机制 | 含义 |
| --- | --- | --- |
| 异步复制 | master replica 接收请求并把 batch 发送给 slave sequencer | 延迟低，但故障切换复杂。 |
| Paxos 同步复制 | 同一 replication group 内的 sequencer 对每个 epoch 的 batch 达成一致 | 可以跨数据中心提供强一致输入复制；论文实现中用 ZooKeeper。 |

论文强调，同步复制增加事务延迟，但因为它发生在锁获取和事务执行之前，不会扩大事务竞争足迹，所以在实验中不降低事务吞吐。这个结论依赖 Calvin 的架构边界：复制的是事务输入，而不是执行后的写效果。

## Deterministic Locking

Calvin 的 scheduler 使用类似 strict 2PL 的锁，但加了确定性约束：

1. 如果两个事务都要在本节点对同一记录申请排他锁，并且事务 A 在全局序列中排在事务 B 前面，那么 A 必须先申请锁。
2. 锁管理器必须严格按请求顺序授予锁。

实现上，单线程按全局事务序列扫描，每个事务在执行前声明完整读写集，然后一次性发出本地锁请求。这个设计让并发执行可以存在，但并发结果必须等价于 sequencer 给出的串行顺序。

这个约束也是 Calvin 的主要适用性边界：事务必须能在执行前声明完整读写集。对于读写集依赖读取结果的事务，Calvin 不能直接处理。

## Distributed Transaction Execution

事务获得所需锁后，worker 按五个阶段执行：

| 阶段 | 内容 |
| --- | --- |
| 1 | 分析读写集，识别本地读写、active participant 和 passive participant。 |
| 2 | 执行本地读取。 |
| 3 | 为 active participant 提供远程读取结果；只读参与者在这里完成。 |
| 4 | active participant 收集远程读取结果。 |
| 5 | 执行业务逻辑并应用本地写入；非本地写入由对应分区执行。 |

因为参与节点在同一确定性序列下开始同一事务，远程读取和结果传递可以并行发生。相比传统执行中事务临时请求远程数据并在最后 2PC，Calvin 试图让事务开始时已经知道参与者、读写集和顺序。

## Dependent Transactions And OLLP

对于需要先读取数据才能确定读写集的 dependent transactions，Calvin 提供 Optimistic Lock Location Prediction。OLLP 先用低隔离、未复制的 reconnaissance query 预测真实事务的读写集，再把真实事务放入全局序列。真实事务执行时重新检查 reconnaissance 读取的条件；如果预测失效，就用确定性方式重启。

OLLP 适合二级索引查找这类读写集依赖但索引本身相对稳定的场景。论文用 TPC-C Payment 的 warehouse name 到 warehouse ID 查找作为例子：如果二级索引不被修改，OLLP 不会出现重启。

## Disk-Resident Data

早期确定性数据库常假设内存数据。Calvin 讨论了确定性调度遇到磁盘 I/O 时的风险：如果事务 A 按序排在 B、C 前面，但 A 的记录在磁盘上，B、C 可能因为 A 持锁或等待而被放大阻塞。

Calvin 的解决路线是把磁盘 I/O 前移到锁获取之前。sequencer 在把事务交给 scheduler 前，向存储层发送 warm-up 或 prefetch 请求，并延迟事务进入调度层。只要延迟覆盖磁盘读取时间，事务进入执行阶段时需要的数据已经在内存里，磁盘等待就不会落入锁持有窗口。

这个策略有两个工程难点：

| 难点 | 说明 |
| --- | --- |
| 延迟预测 | 预测过长会增加事务延迟和内存压力；预测过短会让事务在持锁期间等待磁盘，损害吞吐。 |
| 热数据追踪 | sequencer 需要知道哪些 key 已在对应存储节点内存中；全局追踪不易扩展。 |

论文的实验显示，在简单磁盘存储实现中，只要磁盘访问比例不超过约 0.9%，单机 10k tx/sec 的吞吐不受影响；模拟冷数据延迟时，如果 prefetch 延迟设置得当，高竞争下也能保持吞吐。

## Checkpointing And Recovery

Calvin 用输入日志和确定性重放替代物理 REDO 日志。系统只需要保存事务输入序列和周期性 checkpoint；故障后可以从 checkpoint 开始重放输入。

论文讨论了三类 checkpoint：

| 方式 | 特点 |
| --- | --- |
| 同步 checkpoint | 暂停一个副本产生完整快照；其他副本继续服务，所以客户端不一定感知，但该副本会落后。 |
| 修改版 Zig-Zag checkpoint | 在全局序列中选一个虚拟一致点，围绕该点保留 before/after 版本；等一致点前事务完成后异步写出 before 版本。 |
| 多版本存储 checkpoint | 如果底层存储天然支持多版本快照，可用快照查询生成 checkpoint。 |

这再次体现 Calvin 的核心路线：用确定性输入顺序降低恢复和复制对物理日志的依赖。

## Evaluation

实验平台是 Amazon EC2 High-CPU Extra-Large 机器。论文使用 TPC-C New Order 子集和自定义 microbenchmark。

### TPC-C New Order

Calvin 在每个分区存储 10 个 TPC-C warehouse，并让约 10% New Order 事务访问第二个 warehouse，且第二个 warehouse 位于不同机器。论文报告，当集群超过 10 个节点后，每节点吞吐约 5000 tx/sec，并在 100 节点达到约 50 万 New Order tx/sec。作者将其与当时 Oracle TPC-C 世界纪录的 New Order 吞吐进行对比，强调 Calvin 在普通云硬件上接近该数量级。

这个结果不能解释为完整 TPC-C 全负载已被同等验证；论文明确聚焦 New Order 子集，并表示预计完整 TPC-C 也有类似扩展性。

### Microbenchmark

microbenchmark 中每个事务读取 10 条记录，检查约束后更新每条记录的计数器。其中一个记录来自小 hot set；如果事务跨机器，就在每台机器选择一个 hot record。论文定义 contention index 表示 hot set 中某条记录被访问的比例。

低竞争下 Calvin 从单机扩展到多机后先因远程读序列化、上下文切换和分布式执行开销出现每节点吞吐下降，随后在较大节点数保持近线性增长。高竞争时，多机执行中的进度偏斜会导致等待：如果节点 A 等待节点 B 的远程读，而 B 已经落后，A 会短暂停滞。节点越多、竞争越高，这种偏斜越明显。

### High-Contention Distributed Transactions

论文用 100% 多分区高竞争事务比较 Calvin 和传统 System R* 风格 2PC 的理论下界模型。模型假设 2PC 用约 8ms，且锁在 2PC 期间被持有。结果表明，低竞争时 Calvin 的主要损失来自分布式执行开销；高竞争时，2PC 模型因锁持有期扩大而吞吐显著下降，Calvin 的相对优势更明显。

## What The Paper Contributes

| 贡献 | 说明 |
| --- | --- |
| 确定性分布式事务层 | 把事务顺序和复制从存储引擎中拆出，作为可水平扩展层。 |
| 提前一致的输入序列 | 复制事务输入而非事务效果，支持异步复制和 Paxos 同步复制。 |
| 确定性锁管理 | 用全局顺序驱动锁请求，避免事务尾部 2PC 决策进入锁持有窗口。 |
| 磁盘数据支持路线 | 用 prefetch 和调度延迟把磁盘 I/O 移到锁获取前。 |
| 确定性恢复 | 用输入日志和 checkpoint 替代传统物理 REDO 日志。 |

## Limitations

| 限制 | 影响 |
| --- | --- |
| 必须提前声明读写集 | 复杂事务、二级索引、条件访问和动态查询需要 OLLP 或额外机制。 |
| 范围查询和 phantom 未完整解决 | 论文提到 virtual resources，但不是已实现核心能力。 |
| 磁盘预取依赖预测 | 延迟预测和热数据追踪是系统级难点。 |
| Paxos 实现依赖 ZooKeeper | 论文说明 ZooKeeper 不是高数据量复制的理想实现，实验更多证明吞吐不受锁竞争影响，而不是证明最佳延迟。 |
| 故障恢复仍可能产生 hiccup | 失败分区恢复期间，其他分区的远程读取可能受影响；论文将无停顿故障切换列为未来工作。 |

## Knowledge Extraction

### For `distributed-systems/transaction-processing`

Calvin 是事务处理方向的直接数据库系统证据：它表明高吞吐分布式 ACID 事务的一条路线是先建立确定性输入序列，再用确定性锁管理和输入日志把提交时协调移出事务临界区。它补足了知识库中此前主要来自区块链/跨链论文的“事务处理”证据，使该方向不再只依赖区块链适配视角。

### For `distributed-systems/transaction-processing/distributed-transactions`

Calvin 给出了分布式事务问题的关键拆解：多分区事务的困难不只是远程访问，而是远程访问、锁持有、提交协议和故障决策耦合在一起后造成的竞争足迹扩大。它的解决方法是把全局顺序和复制协议前移，让执行阶段不需要传统 2PC。

### For `database-transaction-processing-to-blockchain-execution`

Calvin 的 sequencer/scheduler 分层可以作为数据库侧“order-then-execute”的强证据。迁移到区块链时，consensus/orderer 类似 sequencer，但区块链还必须处理 Byzantine fault、智能合约非确定性、公开可验证性和状态访问不可提前知道等问题，因此只能作为结构类比和方法候选，不能直接等同。

## Relation Hints

| 关系 | 目标 | 说明 |
| --- | --- | --- |
| evidenced_by | [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | 直接提供确定性事务处理系统证据。 |
| evidenced_by | [[04_Knowledge/distributed-systems/transaction-processing/distributed-transactions|Distributed transactions]] | 直接提供分区数据库分布式事务解决路线。 |
| strengthens_bridge | [[database-transaction-processing-to-blockchain-execution]] | 强化“先排序再执行”和确定性执行对区块链执行层的迁移关系。 |
| touches | [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage engines]] | 通过 CRUD storage layer、prefetch 和 checkpoint 触及存储引擎接口，但不是主要贡献。 |

## Review Notes

- 该 PDF 元数据标题被错误写成 gnuplot 输出路径，队列应以论文首页标题为准。
- 作者应以首页列出的 Yale 作者为准，而不是 PDF metadata 中的 `agt5`。
- 这篇论文不应被归入通用 data-management-and-storage 作为主方向；主方向应是 `distributed-systems/transaction-processing/distributed-transactions`。
