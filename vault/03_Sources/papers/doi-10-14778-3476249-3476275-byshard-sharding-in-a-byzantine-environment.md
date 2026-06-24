---
id: "doi-10-14778-3476249-3476275"
title: "ByShard: Sharding in a Byzantine Environment"
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
  - "p1-p2 abstract, introduction, contributions"
  - "p2-p4 resilient-system background and sharded-system model"
  - "p4-p5 ByShard framework and orchestrate-execute model"
  - "p5-p7 linear, centralized, and distributed orchestration"
  - "p7-p9 isolation-free and lock-based execution"
  - "p9-p12 implementation, experiments, results, discussion, conclusion"
  - "p13-p14 references scanned for adjacent work"
canonical_url: "https://doi.org/10.14778/3476249.3476275"
doi: "10.14778/3476249.3476275"
arxiv_id: ""
venue: "Proceedings of the VLDB Endowment, 14(11): 2230-2243"
year: "2021"
local_pdf: "~/Desktop/paper/ByShard.pdf"
sha256: "54199721c87b897a1ec9bff6a6f364441eee3406e940f5e00d0a97efe47092c2"
pages: 14
pdf_extractor: "codex-bundled-python:pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/byshard-54199721c87b-pages.txt"
artifact_url: "https://www.jhellings.nl/projects/byshard/"
license: "CC BY-NC-ND 4.0"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "scaling-and-sharding"
topic_ids:
  - "sharded-ledgers"
  - "multi-shard-transactions"
  - "byzantine-fault-tolerance"
ontology_path:
  - "blockchain-systems"
  - "scaling-and-sharding"
  - "sharded-ledgers"
primary_ontology_path: "blockchain-systems/scaling-and-sharding/sharded-ledgers/doi-10-14778-3476249-3476275"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/doi-10-14778-3476249-3476275"
  - "distributed-systems/transaction-processing/distributed-transactions/doi-10-14778-3476249-3476275"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "scaling-and-sharding"
    - "consensus"
    - "transaction-processing"
  topics:
    - "sharded-ledgers"
    - "multi-shard-transactions"
    - "byzantine-fault-tolerance"
    - "two-phase-commit"
    - "two-phase-locking"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "byshard"
  - "sharded-ledgers"
  - "multi-shard-transactions"
  - "orchestrate-execute-model"
  - "two-phase-commit"
  - "two-phase-locking"
aliases:
  - "ByShard"
  - "Sharding in a Byzantine Environment"
  - "orchestrate-execute model"
  - "OEM"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "sharding"
  - "distributed-transactions"
  - "byzantine-fault-tolerance"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "scaling-and-sharding"
    - "distributed transaction processing"
  problem:
    - "general-purpose multi-shard transaction processing"
    - "ACID-compliant sharded resilient systems"
    - "cross-shard atomicity and isolation"
  method_family:
    - "orchestrate-execute model"
    - "Byzantine two-phase commit"
    - "Byzantine two-phase locking"
    - "cluster-sending"
  system_layer:
    - "multi-shard orchestration"
    - "transaction execution"
    - "concurrency control"
    - "shard-level consensus"
  evaluation_context:
    - "simulated sharded resilient system"
    - "5000 account-transfer transactions"
    - "64 shards baseline"
  application:
    - "permissioned blockchain data management"
    - "resilient sharded databases"
  bridge:
    - "database transaction protocols to Byzantine sharded ledgers"
    - "BFT consensus to sharded ledgers"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-byshard"
safe_for_absorption: true
source_refs:
  - "doi:10.14778/3476249.3476275"
  - "sha256:54199721c87b897a1ec9bff6a6f364441eee3406e940f5e00d0a97efe47092c2"
  - "pdf:~/Desktop/paper/ByShard.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "scaling-and-sharding"
secondary_directions:
  - "distributed-systems/consensus"
  - "distributed-systems/transaction-processing"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract explicitly frame sharding in a Byzantine environment"
  - "Sections 3-5 define ByShard, OEM, Byzantine two-phase commit, and Byzantine two-phase locking"
  - "Section 6 evaluates scalability and contention trade-offs across eighteen multi-shard protocols"
taxonomy_version: "1.0"
---

# ByShard: Sharding in a Byzantine Environment

## 论文身份

- 标题: ByShard: Sharding in a Byzantine Environment
- 作者: Jelle Hellings, Mohammad Sadoghi
- 机构: Exploratory Systems Lab, Department of Computer Science, University of California, Davis
- 会议/期刊: Proceedings of the VLDB Endowment, Vol. 14, No. 11, pp. 2230-2243
- 年份: 2021
- DOI: `10.14778/3476249.3476275`
- 链接: `https://doi.org/10.14778/3476249.3476275`
- 本地 PDF: `~/Desktop/paper/ByShard.pdf`
- SHA-256: `54199721c87b897a1ec9bff6a6f364441eee3406e940f5e00d0a97efe47092c2`
- Artifact: `https://www.jhellings.nl/projects/byshard/`
- License: CC BY-NC-ND 4.0

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 14
- 已覆盖章节/页码: Abstract, Sections 1-8, references
- 已检查附录: 本 PDF 无正文附录；references 扫描用于识别 AHL, Chainspace, Caper, Cerberus, SharPer 等相邻系统。
- 未覆盖章节/页码: none
- Extraction gaps: 图 6.1 的曲线由正文解释和图注读取，未从图中提取精确数值；队列中自动抽到的 `arxiv_id: 6249.34762` 是 DOI 片段误识别，本笔记将 arXiv 记为 unknown/empty。
- 精读说明: 这是 protocol/systems paper。精读重点放在 ByShard framework、OEM、三类 orchestration、两类 execution/concurrency control、定理中的 step cost、以及实验对 latency/throughput/contention/abort-rate trade-off 的解释。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | 当前 sharded resilient systems 多是系统专用方案；ByShard 提出统一框架，把 2PC/2PL 迁移到 Byzantine 环境并给出 18 个协议 | high | 贡献清单非常具体 |
| §2 / p2-p3 | 背景 | 非分片 Byzantine resilient system 通过 consensus 把 replication 和 ordering 合并；PBFT 例子说明 consensus 成本高 | high | 后续 cost model 的前提 |
| §3 / p3-p5 | ByShard 与 OEM | 定义 shards, multi-shard transaction, cluster-sending；提出 vote/commit/abort shard-steps | high | 核心抽象 |
| §4.1 / p5 | Linear orchestration | 类 Linear-2PC，顺序 vote，fast-abort，Theorem 4.1 给 consensus/cluster-sending step cost | high | 延迟/工作量 trade-off |
| §4.2 / p5-p6 | Centralized orchestration | root shard 并行发起 votes；Lemma 4.2 用一个 consensus step 聚合所有 votes；Theorem 4.3 给 4 consecutive consensus steps | high | 关键 Byzantine vote 聚合技巧 |
| §4.3 / p6-p7 | Distributed orchestration | votes 广播给 commit/abort shards；Theorem 4.4 给 3 consecutive consensus steps 和更高 cluster-sending cost | high | 低延迟但消息更多 |
| §5.1 / p7-p8 | Isolation-free execution | unsafe/safe isolation-free execution；safe modifications 放在 vote-step，unsafe modifications 放在 commit-step | high | degree-0 baseline 和 domain-specific safety |
| §5.2 / p8-p9 | Lock-based execution | Byzantine two-phase locking；deterministic wait queues；Theorem 5.3 给 `2n-1` consensus 和 `2n-2` cluster-sending | high | isolation semantics 核心 |
| §6 / p9-p12 | 实现与评估 | 18 个协议；AHL/Chainspace 对照；5000 transaction workload；scalability/contention/factor-scalability experiments | high | empirical evidence |
| §7-§8 / p12 | 讨论与结论 | 适用于 one-shot transactions；与 AHL, Chainspace, Caper, SharPer, permissionless cross-chain 技术比较 | medium-high | 边界和相邻方向 |
| References / p13-p14 | 关联工作 | AHL, Caper, Chainspace, Cerberus, SharPer, PBFT, HotStuff, distributed DB references | medium | 作为后续队列/桥接线索，不直接作 claim |

## 一句话贡献

ByShard 把传统分布式数据库中的 two-phase commit 与 two-phase locking 系统化地改写到 Byzantine sharded resilient systems 中，用 orchestrate-execute model 组合出 18 个多 shard 事务协议，并展示它们在吞吐、隔离级别、延迟和 abort rate 之间的可调 trade-off。

## 核心精读笔记

### 背景、动机与问题边界

论文的起点是 blockchain-inspired resilient systems 的 fully replicated design 无法满足大规模数据应用。把数据按 geography 或 key range 分给多个 resilient clusters 可以带来 storage scalability 和 processing scalability，但一旦交易同时影响多个 shards，系统不再能只依赖每个 shard 内部的本地 consensus order。

作者批评当时的 sharded resilient systems 往往是系统专用方案: 有的主要优化 single-shard transactions，有的假设低 contention，有的强绑定 UTXO data model。ByShard 的目标不是提出一个具体区块链代币协议，而是为 Byzantine 环境下的 general-purpose, ACID-compliant sharded data management 提供可调框架。

该边界很重要: ByShard 主要讨论 permissioned/resilient data management setting，依赖每个 shard 内已有 BFT consensus 和 cluster-sending primitives。它不是 permissionless shard assignment 方案，也不处理 PoS incentives、anti-censorship、data availability sampling 等现代 blockchain scaling 问题。

### 模型、假设与定义

ByShard 将所有 replicas `R` 分区为 shards `S1...Sz`。一个 transaction `tau` 影响的 shard 集合记为 `shards(tau)`；若集合大小大于 1，就是 multi-shard transaction。每个 shard 内可使用任意 consensus protocol，比如 PBFT、Paxos、HotStuff。论文要求 shard 内 Byzantine 容错满足常见条件 `n_S > 3 f_S`，即每个 shard 中总 replicas 数量大于三倍 Byzantine faulty replicas 数。

跨 shard 通信使用 cluster-sending protocol。Definition 3.2 要求: 发送方 cluster 只有在非故障 replicas 对发送值达成一致时才能发送；接收方 cluster 的所有非故障 replicas 都会收到该值；发送方非故障 replicas 会得到 receipt confirmation。ByShard 中 cluster-sending steps 总是跟在 consensus decision 后，因此发送值已经由 shard 内 consensus 确认，不再需要额外 consensus。

非分片系统中，ordered replication via consensus 同时解决复制和执行顺序。在分片系统中，每个 shard 的本地 order 不能自动给出跨 shard 的 conflict-free execution order；此外，单个 shard 不持有交易需要的全部状态，执行时必须跨 shard 交换状态和协调。

### 方法、协议或系统机制

#### Orchestrate-execute model (OEM)

OEM 的核心目标是把 multi-shard transaction 的 commit、locking 和 execution operations 合并进每个 involved shard 最多两个 consensus steps。它把处理过程拆成三类 shard-steps:

- `Vote(S)`: 在 shard `S` 检查 constraints，决定本 shard 对交易是 commit vote 还是 abort vote，并可执行局部修改或获取 locks。论文为简化假设 abort vote 的 vote-step 无 side effects。
- `Commit(S)`: 当全局决定 commit 时，在 shard `S` 做最终修改、释放 locks 等。
- `Abort(S)`: 当全局决定 abort 时，在 shard `S` 回滚 vote-step 修改或释放 locks。

这个模型把数据库的 2PC/2PL 概念翻译成 Byzantine shard-steps: 2PC 负责 orchestration/atomicity，2PL 负责 execution/isolation，consensus 负责让每个 shard 内部所有非故障 replicas 对一个 shard-step 的顺序和结果达成一致。

#### Linear orchestration

Linear orchestration 类似传统 Linear-2PC。按一个顺序访问有 vote-steps 的 shards。若某个 vote abort，就 fast-abort，只向之前已经投过 commit vote 且需要 rollback/release 的 shards 发送 abort-steps；若所有 vote 都 commit，就向需要 commit-step 的 shards 并行发送 commit-steps。Theorem 4.1 给出 cost: commit 需要 `n_v + 1` consecutive consensus steps，总 consensus steps 为 `n_v + n_c`，cluster-sending steps 为 `n_v + n_c - 1`；abort 情况类似且最多 `n_v + 1` consecutive steps。

优点是简单、可以按失败概率或 abort cost 调整 vote 顺序，并能 fast-abort；缺点是 latency 随 vote shard 数量线性增长。

#### Centralized orchestration

Centralized orchestration 类似 Centralized-2PC。一个 root shard 先执行自己的 vote-step，然后把交易发给其他 vote shards 并行 vote；其他 shards 将 commit/abort vote 用 cluster-sending 发回 root；root 收齐 votes 后作 global commit/abort decision，再把结果发送给需要 commit/abort step 的 shards。

Lemma 4.2 是关键: root 不需要为每个 incoming vote 单独跑 consensus。因为 cluster-sending 保证每个非故障 root replica 最终收到同一个 vote set，vote set 的顺序不影响全局 commit/abort 结果；root 只需用一个 consensus step 决定在某个 round 处理这个全局结果。Theorem 4.3 给出 exactly four consecutive consensus steps；commit 总 consensus steps 为 `n_v + n_c + 1`，cluster-sending steps 为 `2(n_v - 1) + n_c`。

#### Distributed orchestration

Distributed orchestration 类似 Distributed-2PC。每个 voting shard 不只把 vote 发给 root，而是广播给所有有 commit-step 或 abort-step 的 shards。root 还负责发送 wait instructions，让这些 shards 知道要等哪些 votes。收到所有 commit votes 的 commit shard 可以执行 commit；收到任一 abort vote 的 abort shard 可以执行 abort。

Theorem 4.4 给出 exactly three consecutive consensus steps；commit 总 consensus steps 为 `n_v + n_c`，cluster-sending steps 为 `n_v(n_a + n_c) + (n_v - 1)`。这比 centralized latency 更低，但 vote 广播带来更多 cluster-sending cost。Remark 4.5 说明，如果依赖可靠 client 把交易直接发给所有 involved shards，可以类似 Chainspace/PCerberus 降到 two-step distributed orchestration，但需要处理 faulty client recovery。

#### Execution: isolation-free 与 lock-based

Isolation-free execution 是最低隔离 baseline。若一个 shard 有 constraints，就在 vote-step 检查 constraints，并乐观执行 modifications；若最终 abort，再用 abort-step rollback。若 shard 只有 modifications，就只需要 commit-step。它提供 atomicity，但只有 degree-0/write-uncommitted 级别隔离，可能出现 dirty reads 并破坏数据约束。

Safe isolation-free execution 区分 safe/unsafe modifications。论文用银行账户例子说明: rollback 一个扣款会增加余额，通常不会使余额变负，因此较安全；rollback 一个加款会降低余额，可能破坏约束，因此应放到 commit-step。这个变体是 domain-specific 的，不是通用 ACID 解。

Lock-based execution 用 two-phase locking 提供更高 isolation。每个 transaction 在固定 shard order 和 data item order 下获取 read/write locks，避免 deadlock。Vote-step 获取 locks 并检查 constraints；Commit-step 执行 modifications 并释放 locks；Abort-step 释放 locks。Theorem 5.3 证明，在 `n = |shards(tau)|` 时，用 2PL 处理交易需要 `n` 个 vote-steps，再接 `n-1` 个 commit/abort steps，总计 `2n-1` consensus steps 和 `2n-2` cluster-sending steps。

定理证明的关键是 deterministic wait queues: 若 lock 不可获取，所有非故障 replicas 都把同一 `(tau, Vote(S))` 放入本地 deterministic queue；当持锁交易的 commit/abort step 释放 lock 时，所有 replicas 以同样方式唤醒下一批等待者，因此不需要额外 consensus 来决定唤醒顺序。

ByShard 还支持 lower isolation levels: read uncommitted 不获取 read locks；read committed 读后立即释放 read locks；serializable 保持传统 2PL。Non-blocking locks 则在 lock 获取失败时直接 abort transaction，降低高 contention 下的 latency/resource use，但提高 abort rate。

### 实验、评估或案例

作者实现了 ByShard framework、OEM 和 18 个协议。协议来自三种 orchestration 族和多种 execution/isolation 组合: isolation-free unsafe/safe，read uncommitted/read committed/serializable，以及 blocking/non-blocking variants。论文还实现 AHL 作为对照，并说明 ByShard 的 distributed serializable non-blocking protocol `DSnb` 是 Chainspace 风格设计的 generalized version。

实验是 simulated sharded resilient system: consensus 与 cluster-sending 成本被抽象控制，但每个 shard 执行 replica-specific orchestration/execution operations。默认 workload 包含 5000 transactions；每个交易影响 16 个 accounts，其中 8 个 constraints、4 个扣款写、4 个加款写。默认 64 shards、8192 active accounts、每 shard 128 active accounts；message delay 10 ms，consensus decision 30 ms，每 shard 1000 decisions/s。指标包括 total runtime、cumulative duration、average throughput、average committed throughput、median shard-steps。

三个实验分别考察:

- Scalability: 固定 workload/dataset，增加 shard 数量，增加并行处理能力，同时也提高 multi-shard transaction 比例和平均触达 shards。
- Contention: 固定 64 shards，改变每 shard active accounts 数量；active accounts 越多，contention 越低。
- Factor-scalability: 同时增加 shards 与 active accounts，观察系统 scale factor。

正文结果给出定性结论: 18 个协议都表现出 scalability，增加 shards 会让每 shard median work 快速下降。低隔离协议 runtime/duration 最低、throughput 最高。Centralized 和 distributed orchestration 性能相近，并明显优于 linear orchestration。Blocking locks 在低 contention 时有较好 runtime、高 commit rate 和 scalable performance，但高 contention 会显著影响性能。Non-blocking locks runtime/duration 低，但高 contention 会带来更多 aborts。Distributed orchestration 的 committed throughput 通常最高，因为其高吞吐抵消了 contention 的负面影响。

AHL 的 reference committee 在 single-shard-heavy workloads 下有很好 scalability，且能减少 contention；但在 multi-shard-heavy workloads 中，reference committee 会成为瓶颈。这个对比支撑 ByShard 去中心化 root-shard/transaction-specific coordination 的动机。

### 作者结论与我的判断

作者明确声称 ByShard 是 flexible general-purpose ACID-compliant scalable resilient multi-shard data and transaction processing 的基础。这个结论由协议成本分析和模拟评估支撑，但仍应标记为 `source_backed_seed`: 实验抽象了 consensus/cluster-sending，交易模型是 one-shot account-transfer，且没有评估开放网络的 Sybil/incentive/data availability/validator assignment 问题。

我的判断是: ByShard 对 Nahida 的最大增量不是又一个 sharded ledger protocol，而是把 sharding 方向从 OmniLedger 的 UTXO/payment ledger 扩展到 general-purpose transaction processing。它提供了一组可复用轴: orchestration topology、isolation level、blocking vs non-blocking locks、central coordinator vs decentralized coordination、latency vs abort rate vs message cost。

## 层级候选分类

- L1 Domain candidate: `blockchain-systems`; secondary `distributed-systems`
- L2 Direction candidate: `scaling-and-sharding`; secondary `consensus`, `transaction-processing`
- L3 Topic/content cluster candidates: `sharded-ledgers`, `multi-shard-transactions`, `byzantine-fault-tolerance`, `two-phase-commit`, `two-phase-locking`
- Ontology path: `blockchain-systems/scaling-and-sharding/sharded-ledgers/doi-10-14778-3476249-3476275`
- 备选归属: `distributed-systems/transaction-processing/distributed-transactions` 应作为 foundation_missing review path；当前 vault 尚未建立 transaction-processing direction pack。
- 父级领域: blockchain systems, distributed systems
- 学术子领域: resilient data management, sharded blockchain/database systems, Byzantine fault-tolerant transaction processing
- 任务/问题: multi-shard transaction processing with atomicity and isolation
- 方法族: orchestrate-execute model, Byzantine 2PC, Byzantine 2PL, cluster-sending
- 模型/协议/算法族: linear/centralized/distributed orchestration; isolation-free execution; lock-based execution; blocking/non-blocking locks
- 评测场景: simulated sharded resilient system, account-transfer workload, 5000 transactions
- Benchmark/应用: C++ implementation/raw measurements artifact URL in PDF
- 别名: ByShard, OEM, Byzantine sharded transactions
- 相邻方向: AHL, Chainspace, Cerberus, Caper, SharPer, PBFT/HotStuff, distributed database systems
- 置信度: high
- 分类理由: paper title/abstract, §§3-5 protocol design, §6 evaluation all explicitly target Byzantine sharded systems.
- 分类状态: accepted

## 创新点

- 新思想: 用 OEM 将 multi-shard transaction 的 commit、locking、execution 压缩进每个 shard 最多两个 consensus steps。
- 对已有工作的扩展: 将 traditional distributed database 的 2PC/2PL 迁移到 Byzantine shard setting，并与 cluster-sending/BFT consensus 组合。
- 工程或实证贡献: 实现 18 个协议，比较 scalability、contention、factor-scalability；与 AHL/Chainspace 风格协议对照。
- 依赖的 prior work: PBFT/HotStuff/Paxos 等 shard consensus，distributed DB 2PC/2PL，AHL/Chainspace/Cerberus/Caper/SharPer。

## 局限性

### 作者明确说明

- Workload model 限定为 one-shot transactions；作者认为 interactive transactions 因为每个 client-system round-trip 都要 consensus，成本高且不适合 resilient systems。
- 评估使用 simulated sharded resilient system，抽象 consensus 和 cluster-sending 成本；这便于数百 shards 实验，但不是完整 production deployment。
- Permissionless cross-chain/sidechain/relay/atomic-swap 技术被认为比 traditional resilient systems 的技术慢几个数量级，本文不将其作为高性能数据管理路径。

### 基于证据的推断

- Byzantine shard assignment/Sybil resistance 不在本文核心范围；如果用于 permissionless setting，必须额外结合 OmniLedger/Elastico 类 validator assignment 或 PoS committee sampling。
- 图 6.1 的结果主要是定性趋势；若后续需要精确 throughput 数字，应直接读取 artifact raw measurements。
- Transaction-processing direction 在 vault 中仍是 `foundation_missing`，不能仅凭 ByShard 把分布式数据库事务层提升为完整 foundation。

## 可复用思路

- 把跨 shard 协议拆成两个正交轴: orchestration 决定 commit/abort agreement，execution/concurrency control 决定 isolation。
- 在 Byzantine 环境中，若输入 vote set 无序但集合最终一致，可以用一个 consensus step 决定处理 round，而不是对每个 vote 逐个 consensus。
- Deterministic wait queues 是把 lock waiting 内化到 shard-step execution 的关键，使 2PL 不需要额外 consensus。
- Protocol comparison 应同时报告 throughput、committed throughput、latency/duration、abort rate 和 per-shard work；单看吞吐会掩盖 high abort 的协议。
- Reference committee 可以降低 contention，但在 multi-shard-heavy workload 下会形成中心瓶颈。

## 术语表

| Term | 解释 | Evidence |
| --- | --- | --- |
| ByShard | sharded resilient systems 的统一框架 | §3 |
| Orchestrate-execute model (OEM) | 将 commit、locking、execution 映射为 vote/commit/abort shard-steps 的模型 | §3.2 |
| Cluster-sending | resilient clusters 之间的 reliable communication primitive | Definition 3.2 |
| Linear orchestration | 顺序 vote、fast-abort 的 2PC-like orchestration | §4.1 |
| Centralized orchestration | root shard 收集 votes 并作 global decision | §4.2 |
| Distributed orchestration | voting shards 将 votes 广播给 commit/abort shards | §4.3 |
| Isolation-free execution | 低隔离 execution baseline，可能 dirty read | §5.1 |
| Lock-based execution | Byzantine 环境下的 two-phase locking | §5.2 |
| Non-blocking locks | lock 获取失败时直接 abort，控制 latency 但增加 abort rate | §5.2 |

## 证据表

| Claim | 位置 | 类型 | 置信度 | 备注 |
| --- | --- | --- | --- | --- |
| ByShard 将 multi-shard transaction 处理拆成 orchestration 与 execution，并以 vote/commit/abort shard-steps 表达 | §3.2, p4-p5 | mechanism | high | OEM |
| OEM 可把 commit、locking、execution 操作纳入每个 involved shard 至多两个 consensus steps | Abstract, §3.2, §8 | design claim | high | 具体协议见 §4-§5 |
| Linear orchestration commit 需要 `n_v + 1` consecutive consensus steps，支持 fast-abort | Theorem 4.1, p5 | theorem/cost | high | latency 随 vote shards 线性增长 |
| Centralized orchestration 可用一个 root consensus step 处理所有 incoming votes | Lemma 4.2, Theorem 4.3, p6 | theorem/cost | high | exactly four consecutive consensus steps |
| Distributed orchestration 将 consecutive consensus steps 降到 exactly three，但 cluster-sending 更多 | Theorem 4.4, p7 | theorem/cost | high | vote 广播给 commit/abort shards |
| Lock-based execution 用 deterministic wait queues 实现 2PL，`n` shards 需要 `2n-1` consensus steps | Theorem 5.3, p8-p9 | theorem/mechanism | high | serializable execution |
| 18 个协议在实验中都显示 per-shard work 随 shards 增加下降 | §6.2, Figure 6.1, p10-p12 | empirical_result | medium-high | 图中趋势 + 正文结论 |
| AHL reference committee 可降低 contention，但 multi-shard-heavy workloads 下成为瓶颈 | §6, §6.2, p10-p12 | comparison | high | 对照 AHL |
| ByShard 不覆盖 interactive transactions 的高效支持 | §7, p12 | limitation | high | one-shot transactions scope |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| ByShard shows that a shard receiving multiple commit or abort votes can derive the same global decision from the unordered vote set and needs only one consensus step to agree on the round that processes that decision. | `doi:10.14778/3476249.3476275#p6` | folded_into_meta_note |
| ByShard composes three orchestration styles with isolation-free, read-uncommitted, read-committed, and serializable execution variants to produce eighteen multi-shard transaction protocols with different throughput, isolation, latency, and abort-rate trade-offs. | `doi:10.14778/3476249.3476275#p7-p11` | folded_into_meta_note |
| In ByShard's simulated evaluation, increasing the number of shards lowers median work per shard across all eighteen protocols, while contention shifts the trade-off between blocking-lock latency, non-blocking-lock aborts, and committed throughput. | `doi:10.14778/3476249.3476275#p10-p12` | folded_into_meta_note |
| ByShard implements two-phase locking in Byzantine shards by acquiring locks in deterministic order during vote-steps and using deterministic wait queues, allowing lock waits and wakeups without extra consensus beyond the shard-steps. | `doi:10.14778/3476249.3476275#p8-p9` | folded_into_meta_note |
| ByShard's orchestrate-execute model represents commit, locking, and execution through vote, commit, and abort shard-steps so a multi-shard transaction can be processed with at most two consensus steps per involved shard. | `doi:10.14778/3476249.3476275#p4-p5` | folded_into_meta_note |
| ByShard adapts two-phase commit into three Byzantine shard orchestration patterns: linear orchestration minimizes total work and supports fast aborts, centralized orchestration reduces latency through a root shard, and distributed orchestration further reduces consecutive consensus steps by broadcasting votes. | `doi:10.14778/3476249.3476275#p5-p7` | folded_into_meta_note |
| ByShard's comparison with AHL finds that a dedicated reference committee can reduce contention and scale well for single-shard-heavy workloads, but becomes a bottleneck when many transactions are multi-shard. | `doi:10.14778/3476249.3476275#p10-p12` | folded_into_meta_note |
| ByShard targets one-shot transactions in sharded resilient data management systems and explicitly treats interactive transactions and slow permissionless cross-chain techniques as outside its high-performance transaction-processing scope. | `doi:10.14778/3476249.3476275#p12` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `[[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard OEM bounds multi-shard processing to at most two consensus steps per involved shard]]`
- `[[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard translates two-phase commit into Byzantine shard orchestration]]`
- `[[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard processes Byzantine shard votes with one consensus step when vote sets are deterministic]]`
- `[[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard implements Byzantine two-phase locking with deterministic wait queues]]`
- `[[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard composes eighteen protocols that expose isolation, latency, and abort-rate trade-offs]]`
- `[[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard evaluation shows per-shard work scales down while contention changes latency and abort trade-offs]]`
- `[[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard comparison finds reference committees can bottleneck multi-shard-heavy workloads]]`
- `[[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard scope is one-shot resilient transactions rather than interactive transactions or permissionless sharding]]`

### Concepts to create or update

- Create [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard]] as source-backed seed.
- Create [[sharded-ledgers|Orchestrate-execute model]].
- Create [[sharded-ledgers|Byzantine sharded transactions]].
- Create [[sharded-ledgers|Cluster-sending]] as source-backed seed.
- Update [[sharded-ledgers|Sharded ledgers]] with general-purpose ACID/OEM branch.
- Update [[byzantine-fault-tolerance|Byzantine fault tolerance]] with sharded transaction source extension.

### Maps, bridges, syntheses

- Refresh [[scaling-and-sharding|Scaling and sharding]] and [[sharded-ledgers|Sharded ledgers]].
- Refresh [[bft-consensus-to-sharded-ledgers|BFT consensus -> sharded ledgers]] with ByShard rows.
- Create [[database-transactions-to-byzantine-sharded-ledgers|Database transaction protocols -> Byzantine sharded ledgers]] as bridge seed with foundation gap for distributed transaction processing.
- Refresh [[sharded-ledgers|Sharded ledgers state 2026-06-11]] to cover OmniLedger + LazyLedger + ByShard relationship.

### Review queue items

- `foundation_missing`: distributed transaction processing / distributed database systems direction lacks direct foundation pack.
- `metadata_review`: queue had false arXiv extraction from DOI; no arXiv ID used in source note.
- `artifact_followup`: ByShard raw measurements/code URL available; use it if exact numeric benchmark extraction is needed.

## Synthesis Handoff

- Topic synthesis `sharded-ledgers-state-2026-06-11` should be refreshed because ByShard changes the local sharded-ledger state from UTXO/payment-centric seed to a broader resilient data management / ACID transaction-processing seed.
- Domain synthesis for `blockchain-systems` remains `foundation_thin`; no full domain rewrite needed.
- A future direction/topic pack for `distributed-systems/transaction-processing` should be queued before making database-side bridge conclusions evergreen.
