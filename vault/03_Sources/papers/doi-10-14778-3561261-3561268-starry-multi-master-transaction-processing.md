---
id: "doi-10-14778-3561261-3561268"
title: "Starry: Multi-master Transaction Processing on Semi-leader Architecture"
type: "source"
source_kind: "paper"
schema_version: "1.0"
status: "absorbed"
created: "2026-06-23"
updated: "2026-06-23"
authors:
  - "Zihao Zhang"
  - "Huiqi Hu"
  - "Xuan Zhou"
  - "Jiang Wang"
year: 2022
venue: "PVLDB 16(1):77-89"
publisher: "VLDB Endowment"
doi: "10.14778/3561261.3561268"
arxiv_id: ""
source_refs:
  - "doi:10.14778/3561261.3561268"
  - "sha256:ce8e3791525a2824f65114083a6510873f8cae57b15050bf7cfc02c688fd85d7"
canonical_url: "https://doi.org/10.14778/3561261.3561268"
local_pdf_path: "~/Desktop/paper/p77-hu.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/p77-hu-starry-multi-master-transaction-processing-pages.txt"
pages: 13
pdf_sha256: "ce8e3791525a2824f65114083a6510873f8cae57b15050bf7cfc02c688fd85d7"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
primary_domain: "distributed-systems"
primary_direction: "transaction-processing"
primary_ontology_path: "distributed-systems/transaction-processing/distributed-transactions"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing/replicated-database-concurrency-control"
  - "distributed-systems/data-management-and-storage"
topic_ids:
  - "distributed-transactions"
  - "multi-master-transaction-processing"
  - "semi-leader-commit-protocol"
  - "replicated-database-concurrency-control"
  - "transaction-reordering"
  - "cloud-database-transaction-processing"
knowledge_node_refs:
  - "[[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]]"
  - "[[04_Knowledge/distributed-systems/transaction-processing/distributed-transactions|Distributed transactions]]"
  - "[[04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control|Replicated database concurrency control]]"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0111"
queue_status: "absorbed"
run_id: "nahida-knowledge-20260623-starry-multi-master-transaction-processing"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p13"
  - "abstract states the target is multi-master transaction processing and transaction commit at the storage layer"
  - "Sections 3-4 define semi-leader commit, conflict reordering, distributed transactions, and read-only transactions"
  - "classification corrected from data-management-and-storage/distributed-transactions to transaction-processing/distributed-transactions"
trust_tier: "primary"
---

# Starry: Multi-master Transaction Processing on Semi-leader Architecture

## 论文身份

- 标题: Starry: Multi-master Transaction Processing on Semi-leader Architecture
- 作者: Zihao Zhang; Huiqi Hu; Xuan Zhou; Jiang Wang
- 发表: PVLDB 16(1):77-89, 2022
- DOI: `10.14778/3561261.3561268`
- 本地 PDF: `~/Desktop/paper/p77-hu.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/p77-hu-starry-multi-master-transaction-processing-pages.txt`
- SHA-256: `ce8e3791525a2824f65114083a6510873f8cae57b15050bf7cfc02c688fd85d7`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- 已覆盖: abstract/introduction、cloud database 背景、leader-based/leaderless commit 对比、Starry semi-leader 协议、conflict graph reordering、故障恢复、正确性证明、distributed transactions 扩展、read-only transactions 扩展、Retwis/YCSB 实验与限制。
- Extraction gaps: 图中曲线的逐点数值未完整 OCR；source note 只记录正文与表格能确认的关键数值和趋势。

## 一句话贡献

Starry 为云数据库的 multi-master transaction processing 提出 semi-leader transaction commit protocol: 无冲突事务走去中心化 fast path，一次 wide-area RTT 即可提交；冲突事务交给 sequencer 做精确冲突图重排，以降低 leaderless 协议在高竞争下的无谓 abort，同时避免 leader-based 协议的单点瓶颈。

## 分类判断

这篇论文的主路径应是:

```text
distributed-systems / transaction-processing / distributed-transactions
```

队列原始分类为 `distributed-systems/data-management-and-storage/distributed-transactions`。这需要纠正: Starry 虽然运行在 disaggregated cloud database 的 storage layer，并依赖多副本日志、时间戳和存储层高可用，但论文的核心问题不是存储引擎、索引或物理数据布局，而是多主事务提交、并发控制、复制一致性和分布式事务扩展。

Secondary path 可以连接到 `replicated-database-concurrency-control`，因为 Starry 把事务提交、OCC 风格冲突检测、timestamp order、replicated log 和 sequencer recovery 组合在同一个 storage-layer commit protocol 中。它不同于 C5 的 primary-backup backup-side cloned CC，但同属“复制数据库中事务/并发控制如何与副本一致性耦合”的问题族。

## 论文要解决的问题

云原生数据库常把计算层和存储层分离，以便独立扩缩容。为了让多个计算节点并发执行事务，存储层必须提供一个 commit protocol，同时保证 ACID、replica consensus 和 serializability。

已有两类路线各有短板:

| 路线 | 优点 | 主要短板 |
| --- | --- | --- |
| Leader-based protocol | 实现直观，冲突处理集中 | leader 成为单节点瓶颈；跨地域部署中，非 leader 附近的事务需要额外 wide-area latency |
| Leaderless protocol | 所有副本可并行提议，低冲突时扩展性好 | 冲突事务缺少精确协调，容易 abort 或反复协调，高竞争下吞吐下降 |

Starry 的问题表述是: 能否让无冲突事务像 leaderless 协议一样就近快速提交，同时让真正冲突的事务获得 leader-like 的精确冲突决策，而不把所有事务都送到中心节点。

## 系统模型

Starry 面向 disaggregated cloud database。计算层负责执行事务逻辑，存储层保存数据、多副本日志和 commit protocol 状态。每个 shard 有 `2F+1` 个副本，可容忍最多 `F` 个非 Byzantine failure。

关键角色:

| 角色 | 作用 |
| --- | --- |
| Computing node | 执行业务事务，读取最近副本，缓存 read/write set；提交时向最近副本发起 commit。 |
| Proposer | 存储层副本之一，给事务分配 Lamport timestamp 并尝试复制提交。所有副本都可充当 proposer。 |
| Normal replica | 参与复制、冲突检测、回复 pre-commit/conflict/abort/re-commit。 |
| Sequencer | 只处理冲突路径，维护 conflict graph，决定 commit/abort/re-commit 顺序，并参与故障恢复。 |

时间戳使用 Lamport logical timestamp，形如 `<counter, replica_id>`。timestamp 既编码 happens-before，也通过 replica id 打破平局形成唯一全序。

## Semi-leader Commit Protocol

Semi-leader 的核心是把 commit 分成两条路径:

| 路径 | 触发条件 | 机制 | 延迟/代价 |
| --- | --- | --- | --- |
| Non-conflict fast path | 副本没有发现 stale read 或 rw-conflict | proposer 收集 super quorum pre-commit 后直接提交 | 约 1 wide-area RTT |
| Conflict path | 任一副本发现与 active transactions 的 rw-conflict | sequencer 合并依赖并运行冲突图重排 | 约 2.5 wide-area RTT，tail latency 更高 |

一个事务提交时，computing node 把 read/write set 交给最近副本。proposer 分配 timestamp，写入本地 log，并发送 `RepTxn`。副本运行 `OCC_Check`:

| 检查结果 | 含义 | 后续动作 |
| --- | --- | --- |
| abort | 读到了已被更高版本写覆盖的 stale data | proposer 收到任意 abort 即中止事务 |
| re-commit | 事务可以用更大的 timestamp 重新排序 | proposer 或 sequencer 触发重新提交 |
| conflict | 与 active transaction 存在 rw-conflict | 进入 sequencer conflict path |
| pre-commit | 没有发现冲突或 stale read | proposer 收集 quorum 后 fast commit |

Starry 忽略 ww-conflict，使用 Thomas write rule 和 `write_ts` 处理写写覆盖；真正影响 serializability 的是 rw-conflict。

## Quorum 与日志结构

每个副本维护:

| 状态 | 作用 |
| --- | --- |
| `counter` | Lamport timestamp counter |
| `active list` | 尚未最终 commit/abort 的事务 |
| `Log[][]` | 二维日志数组，每个 proposer 有独占行，避免不同 proposer 竞争同一 log slot |

Starry 使用 `ceil(3F/2)+1` 的 super quorum 支撑 non-conflict fast path。直觉是: 如果事务已经在 super quorum 上 pre-commit，那么在最多 `F` 个副本失败后，恢复流程仍能从足够 surviving replicas 看到它的 pre-commit 证据，不会把已提交事务误判为未提交。

对于 sequencer，若收到至少 `floor(F/2)+1` 个 `NotConf`，它可以确定该事务无法已经通过 non-conflict path 提交，于是安全地把它加入 conflict graph。

## Conflict Graph Reordering

Sequencer 维护 `txn_graph`。图中节点是冲突事务，边代表 rw-dependency。目标是保留尽可能多的 conflicting transactions，并给剩余事务安排一个 serializable order。

处理流程:

| 步骤 | 说明 |
| --- | --- |
| 合并依赖 | sequencer 从 `NotConf` 和 `ReqDec` 中合并 proposer/replica 观察到的冲突依赖。 |
| Tarjan SCC | 在强连通分量中找 dependency cycle。 |
| Break cycles | 对 size > 1 的 SCC，启发式 abort `in_degree * out_degree` 最大的 entry 来打破循环。 |
| Topological sort | 对剩余节点拓扑排序。 |
| Commit/re-commit | 无入依赖的事务可按原 timestamp commit；有依赖的事务用更大 timestamp re-commit。 |

论文把目标描述为最小化 abort set，但实际算法是启发式 cycle breaking，不应理解为全局最优求解。它的意义是比 leaderless 的粗糙冲突处理更精确: 冲突不等于必须 abort，只要能重排成可串行顺序，就可以保留。

## Failure Recovery

Starry 分 normal replica failure 和 sequencer failure。

### Normal Replica Failure

sequencer 接管恢复，向其他副本发送 recovery 请求并等待 `F+1` 个 status:

| 观察到的状态 | 决策 |
| --- | --- |
| 已有 final result | 同步 final decision |
| 无 final，且 pre-commit 少于 `floor(F/2)+1` | abort |
| 无 final，且 pre-commit 至少 `floor(F/2)+1` | commit，并 abort 与其冲突的事务 |

该规则与 super quorum 互补: 已经 fast-commit 的 non-conflict transaction 不会因为最多 `F` 个副本故障而失去可恢复证据。

### Sequencer Failure

Starry 用类似 Raft term 的方式选出新 sequencer。候选 sequencer 从超过 `F` 个副本收集 vote；vote 中会携带未决冲突信息。新 sequencer 重建 `txn_graph`，向多数副本查询状态，并保留先前已经形成的决定。

## Correctness 边界

论文证明 Starry 满足:

| 性质 | 证明直觉 |
| --- | --- |
| Non-triviality | committed transaction 必须来自 client proposal。 |
| Linearizability | 每个 proposer 使用独占 log row；timestamp 全序和 OCC cases 保证 real-time order。 |
| Fault tolerance | fast path 有 super quorum 证据，conflict path 决策写到 `F+1` 副本，最多 `F` 个故障后仍可恢复。 |
| Serializability | 并发冲突事务不能以违背 timestamp/依赖的方式同时提交；conflict path 通过 abort/re-commit/reorder 打破 cycle。 |

注意: failure model 是 crash/normal failure，不是 Byzantine fault tolerance；这点不能迁移到开放链或 BFT shard 场景。

## Distributed Transactions 扩展

Starry 支持跨 shard distributed transactions。计算节点充当 coordinator:

1. 在提交前向参与 shards 获取当前 timestamp。
2. 选择最大 timestamp 作为事务 timestamp。
3. 每个参与 shard 独立运行 Starry phase。
4. 如果所有参与 shards pre-commit，则全局 commit。
5. 如果任一 shard abort，则全局 abort。
6. 如果收到 re-commit，则选择更大的新 timestamp 并重新提交。

论文强调，Starry 不让 coordinator 在所有 participants 已经决定 commit 后单方面 abort。依赖 storage-layer 高可用和 termination protocol，它试图避免传统 2PC 中 coordinator failure 带来的 blocking/unsafe abort 问题。

## Read-only Transactions 扩展

Starry 支持两种 read-only consistency:

| 模式 | 机制 | 适用 |
| --- | --- | --- |
| Strict serializable RO | 像 read-write transaction 一样进入复制和冲突检测 | 需要最强语义，延迟较高 |
| Process-ordered serializability (POS) RO | 读取本地或较旧副本状态；跨 shard 时先获取各 read key 的最新 `write_ts`，选最大 read timestamp | 可接受 weaker RO consistency、追求低延迟/高吞吐 |

实验中 POS RO 的平均 latency 为 12-19ms，吞吐约为 strict serializable RO 的 10x，因为后者需要复制和冲突检测。

## 实验设置

Starry 基于 TAPIR 开源实现改造: 用 semi-leader commit protocol 替换 TAPIR 的 inconsistent replication protocol。对照包括 TAPIR leaderless 和 Raft-based leader protocol。

| 场景 | 设置 |
| --- | --- |
| Local cluster | Intel Xeon Silver 4110，32 cores，196GB RAM；Retwis/YCSB+T；3-9 replicas；5 shards 测试 |
| Cross-region | Alibaba ECS, Shanghai / San Francisco / Frankfurt；3 shards，每 shard 3 replicas，每个数据中心一个 replica；2 vCPU, 8GB RAM |
| Workloads | Retwis Twitter-like workload；YCSB A/B 变体；Zipf skew 控制 contention |

Retwis 操作比例: Add User 5%，Follow/Unfollow 15%，Post Tweet 30%，Load Timeline 50%。事务平均访问 4-10 items，并跨 2-3 shards。

## 实验结论

| 结论 | 证据 |
| --- | --- |
| Local Retwis 下 Starry 比 TAPIR/Raft-based 更高吞吐 | 单 shard peak 8258 tps，约 1.4x TAPIR、3.42x Raft-based；5 shards 时约 1.33x TAPIR、4.21x Raft-based |
| Starry 降低 abort rate | Retwis 中 abort rate 降低超过 60%；Zipf 0.8/0.9 时吞吐约为 TAPIR 的 1.43x/1.5x |
| 高竞争下 sequencer 会成为潜在瓶颈 | Zipf 超过 0.9 后 reordering 效果变弱，abort rate 快速上升；作者建议通过 shard-level sequencer 分担 |
| Cross-region low load 下 latency 接近 TAPIR 且优于 Raft | Starry/TAPIR conflict-free path 约 1 RTT；Raft 非 leader 本地事务需额外跨地域跳转 |
| Cross-region 高竞争下 Starry throughput/abort 优势明显，但 tail latency 可能更高 | conflict path 约 2.5 RTT，TAPIR conflict path 约 2 RTT |
| POS read-only 路线显著提升读多负载 | YCSB-B 中 POS RO 平均 latency 12-19ms，吞吐约 strict serializable RO 的 10x |

## What The Paper Contributes

| 贡献 | 说明 |
| --- | --- |
| Semi-leader commit protocol | 把 non-conflict fast path 和 conflict sequencer path 分离。 |
| Precise conflict resolution | 使用 conflict graph、Tarjan SCC 和 re-commit/abort 决策减少不必要 abort。 |
| Multi-master cloud DB architecture | 所有 storage replicas 可提议事务，支持计算层多主并发提交。 |
| Failure recovery protocol | 用 super quorum、sequencer takeover 和 term/vote 恢复保护已提交/未决事务。 |
| Distributed transaction extension | 将 semi-leader protocol 扩展到跨 shard transaction，处理 coordinator failure 边界。 |
| Read-only transaction optimization | 对 read-heavy workload 提供 POS 读路径。 |

## Limitations

| 限制 | 影响 |
| --- | --- |
| 非 Byzantine failure model | 不能直接迁移到 BFT/open blockchain；恶意副本、equivocation 和 Sybil 不在模型内。 |
| Sequencer conflict path 仍可能成为热点 | 高 Zipf skew 下冲突图批处理和 reordering 开销上升，tail latency 增大。 |
| Reordering 是启发式 | SCC 中 abort `in_degree * out_degree` 最大节点不等价于最小 abort 的全局最优求解。 |
| POS read-only 弱于 strict serializability | POS 适合读多/低延迟，但不是严格串行化读。 |
| 实验基于 TAPIR 代码改造 | 证明协议方向，但不是生产云数据库完整落地；作者也将真实云数据库部署、计算层 caching/sharding 列为未来工作。 |

## Knowledge Extraction

### For `distributed-systems/transaction-processing`

Starry 补入一条直接数据库系统证据: 事务处理中的瓶颈不只是 2PC 或锁本身，而是 commit protocol、replica consensus、OCC conflict detection 和跨地域 topology 的组合。Semi-leader 路线说明，可以把“是否需要中心化处理”延迟到冲突出现时再决定；无冲突事务保留 leaderless 并行性，冲突事务才支付 sequencer reordering 成本。

### For `distributed-systems/transaction-processing/distributed-transactions`

Starry 的 distributed transaction 扩展让本节点不再只有 Calvin 的 deterministic input-order route 和区块链/跨链 adaptation route。它提供了另一条多 shard ACID 路线: 在每个 shard 内用 semi-leader commit 得到 pre-commit/final decision，再由 computing-node coordinator 聚合；同时借 storage-layer HA 和 termination protocol 减少 coordinator failure 带来的 blocking/unsafe abort。

### For `distributed-systems/transaction-processing/replicated-database-concurrency-control`

Starry 与 C5 不同: C5 关注 primary-backup backup read visibility 和 replication lag；Starry 关注 multi-master storage replicas 的事务提交与冲突处理。但 Starry 仍强烈连接复制数据库并发控制，因为它把 timestamp、active transactions、read/write sets、per-proposer logs、quorum evidence 和 sequencer recovery 放在同一个 replicated transaction commit protocol 内。

### For `distributed-systems/data-management-and-storage`

Starry 只应作为 secondary evidence。它说明 disaggregated storage layer 可以承载事务提交与副本一致性协议，但不提供 storage engine、index、LSM、snapshot API 或物理布局的主要贡献。

## Relation Hints

| 关系 | 目标 | 说明 |
| --- | --- | --- |
| evidenced_by | [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | 直接提供 cloud database multi-master transaction commit 证据。 |
| evidenced_by | [[04_Knowledge/distributed-systems/transaction-processing/distributed-transactions|Distributed transactions]] | 提供 semi-leader commit + multi-shard extension 路线。 |
| evidenced_by | [[04_Knowledge/distributed-systems/transaction-processing/replicated-database-concurrency-control|Replicated database concurrency control]] | 作为 multi-master replicated storage-layer commit/concurrency-control evidence。 |
| touches | [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | disaggregated storage layer 是系统上下文，但不是主知识路径。 |

## Review Notes

- 队列中的 `arxiv_id: 1261.35612` 是 DOI 被正则误识别，应清空。
- 主分类从 `data-management-and-storage/distributed-transactions` 改为 `transaction-processing/distributed-transactions`。
- 这篇不应新建 `Starry` 作为知识节点；Starry 是 source/system 实例，真正可复用的通用概念是 semi-leader commit、conflict-path reordering、multi-master transaction processing 和 replicated database transaction commit。
