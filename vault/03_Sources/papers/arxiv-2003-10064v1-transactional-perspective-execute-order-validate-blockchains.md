---
id: "arxiv:2003.10064v1"
title: "A Transactional Perspective on Execute-Order-Validate Blockchains"
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
  - "p2-p4 EOV architecture in Fabric/Fabric++ and OCC background"
  - "p5-p9 theoretical analysis: blockchain snapshots, timestamp mapping, serializability, reorderability"
  - "p9-p13 algorithms, security analysis, implementation design, dependency graph, pruning"
  - "p13-p17 FabricSharp/FastFabricSharp evaluation"
  - "p17-p19 related work, conclusion, acknowledgements, references"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2003.10064"
doi: ""
arxiv_id: "2003.10064v1"
venue: "arXiv preprint"
year: "2020"
pdf_pages: 19
pdf_sha256: "c482c7c18ab4400f261ada6a1080b8d654a79550e458d273b63b48fe77333ac4"
local_pdf: "~/Desktop/paper/2003.10064.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2003.10064-c482c7c18ab4-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
topic_ids:
  - "transaction-processing"
  - "execute-order-validate"
  - "optimistic-concurrency-control"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing/arxiv-2003-10064v1"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing/arxiv-2003-10064v1"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "execution-and-transactions"
    - "transaction-processing"
  topics:
    - "blockchain transaction processing"
    - "execute-order-validate blockchains"
    - "optimistic concurrency control"
    - "serializability"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "execute-order-validate"
  - "Hyperledger Fabric"
  - "FabricSharp"
  - "FastFabricSharp"
  - "optimistic concurrency control"
  - "serializability"
  - "transaction dependency graph"
aliases:
  - "Transactional Perspective on EOV Blockchains"
  - "FabricSharp"
  - "Fabric#"
  - "FastFabricSharp"
  - "FastFabric#"
  - "EOV blockchains"
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
    - "EOV blockchains abort too many serializable transactions during validation"
    - "block formation rate is limited by cryptography and consensus, so invalid in-ledger transactions waste scarce throughput"
    - "database OCC analysis must be adapted to blockchain immutability and block ordering"
  method_family:
    - "OCC-inspired dependency analysis for EOV blockchains"
    - "fine-grained pre-ordering abort"
    - "topological reordering of pending transactions"
    - "snapshot-consistent contract simulation"
  system_layer:
    - "Hyperledger Fabric ordering service"
    - "FastFabric ordering service"
    - "endorsement simulation"
    - "validation and serializability"
  evaluation_context:
    - "Fabric 1.3 prototype"
    - "FastFabric prototype"
    - "Smallbank-style workload"
    - "Fabric/Fabric++/Focc-s/Focc-l baselines"
  bridge:
    - "database transaction processing to blockchain execution"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-transactional-perspective-eov"
source_refs:
  - "arxiv:2003.10064"
  - "arxiv:2003.10064v1"
  - "pdf:~/Desktop/paper/2003.10064.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> execution-and-transactions"
secondary_directions:
  - "distributed-systems -> transaction-processing"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "abstract explicitly targets execute-order-validate blockchains and invalid transaction reduction"
  - "Sections 3-4 define OCC-style serializability analysis, dependency graph algorithms, and Fabric/FastFabric integration"
  - "evaluation compares FabricSharp/FastFabricSharp against Fabric, Fabric++, and database OCC-inspired baselines"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0058"
queue_status: "absorbed"
---

# A Transactional Perspective on Execute-Order-Validate Blockchains

## 论文身份

- 标题: A Transactional Perspective on Execute-Order-Validate Blockchains
- 作者: Pingcheng Ruan, Dumitrel Loghin, Quang-Trung Ta, Meihui Zhang, Gang Chen, Beng Chin Ooi
- 机构: National University of Singapore; Beijing Institute of Technology; Zhejiang University
- 年份: 2020
- arXiv: `2003.10064v1`
- 本地 PDF: `~/Desktop/paper/2003.10064.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/2003.10064-c482c7c18ab4-pages.txt`
- SHA-256: `c482c7c18ab4400f261ada6a1080b8d654a79550e458d273b63b48fe77333ac4`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 19
- 已覆盖章节/页码: Abstract, Introduction, EOV/Fabric/Fabric++ background, OCC background, theoretical analysis, reordering theorem, algorithms, security analysis, implementation, FabricSharp/FastFabricSharp experiments, related work, conclusion, references。
- Extraction gaps: 图 10-15 的曲线细粒度数值按正文报告记录；图中未逐点 OCR 的数值不做额外推断。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p3 | 问题与贡献 | EOV 架构支持并行交易但 validation 会丢弃大量无效交易；作者提出 OCC-inspired 方法，在 ordering 前丢弃不可串行化交易，剩余交易经重排保证 serializable | high |
| §2.1 / p3-p4 | EOV/Fabric 背景 | 解释 execution、ordering、validation 三阶段，Fabric++ 在 consensus 后、block formation 前重排交易 | high |
| §2.2 / p4-p5 | OCC 背景 | 回顾 optimistic concurrency control、snapshot isolation、serializable isolation 的数据库语境 | medium |
| §3.1 / p5-p6 | EOV 与 OCC 的相似性 | 定义 blockchain snapshot、snapshot consistency、start/end timestamp；说明跨 block 读取不必然不一致 | high |
| §3.2 / p6-p7 | Serializability 分析 | 用 dependency graph 分析 Fabric/Fabric++，指出它们实际上满足 Strong Serializability，比 Fabric 协议要求的 Serializability 更严格 | high |
| §3.3 / p7-p8 | Reorderability 分析 | 证明只有 concurrent pending transactions 可以被重排；c-rw/anti-rw 交换顺序不改变依赖方向，c-ww 可翻转依赖方向 | high |
| §3.4 / p8-p9 | Fine-grained concurrency control | Theorem 2 支撑算法: 若 cycle 中没有 pending c-ww，则不可通过重排串行化；用 arrival-time cycle check、block-formation topological sort 和 c-ww restoration 处理 | high |
| §3.5 / p9-p10 | 安全分析 | 讨论 reordering 作为 ordering service 的确定性步骤如何保持 safety；也说明可能牺牲 Fabric liveness/validity，并提出 transaction hash 先排序后披露细节的缓解 | high |
| §4 / p10-p13 | 实现 | 在 Fabric/FastFabric 上实现 FabricSharp/FastFabricSharp；用 snapshot read、CommittedWriteTxns/CommittedReadTxns、PendingWriteTxns/PendingReadTxns、Bloom filter reachability、ww restoration、max span pruning | high |
| §5 / p13-p17 | 实验 | FabricSharp 与 Fabric、Fabric++、Focc-s、Focc-l 比较；FastFabricSharp 与 FastFabric 比较；报告有效吞吐、reordering latency、transaction process latency、abort rate | high |
| §6-§7 / p17 | 相关工作与结论 | 将贡献定位为 database transactional analysis 到 EOV blockchain 的迁移，区别于 Fabric++、FastFabric 和 database-backed blockchain | medium |

## 一句话贡献

这篇论文把 Hyperledger Fabric 类 execute-order-validate 区块链的无效交易问题形式化为 OCC/快照事务的 serializability 问题，并提出 FabricSharp/FastFabricSharp：在 ordering 阶段维护依赖图，提前丢弃不可重排的交易，再用拓扑重排提交剩余交易，从而减少 validation 阶段的 abort。

## 核心问题设定

EOV 架构把交易生命周期拆成 execution、ordering、validation。Execution/endorsement 可并行产生 readset/writeset；ordering 通过共识给交易排序并组成 blocks；validation 再检查 endorsement policy 和 serializability。问题在于: 共识与密码学已经限制了 block formation 速度，如果大量交易进入 ledger 后才在 validation 中因读写冲突被标记 invalid，raw throughput 看似稳定，effective throughput 会随冲突 skew 快速下降。

论文把这个问题放在数据库事务处理的视角下分析: Fabric/Fabric++ 当前做法类似“保守地禁止会产生 anti-rw 的调度”，因此实际达到的是 Strong Serializability；但 Fabric 协议只需要 One-Copy Serializability。这个差距意味着一些被 Fabric/Fabric++ 丢弃的交易其实可以通过重排变成 serializable。

## 方法与机制

### EOV 与 OCC 的对应

论文定义 `blockchain snapshot` 为某个 block commit 后的状态，定义 `snapshot consistency` 为交易所有读取都可归属于某个区块快照。Fabric 使用 read lock 确保 simulation 对最新状态执行；Fabric++ 去掉锁但会早停跨 block 读取交易。论文指出跨 block read 不一定不一致: 如果后续 block 没有改变先前读过的 key，交易仍可归属于后来的 snapshot。

据此，论文把区块链 sequence number 映射为 OCC 风格 timestamp:

- `StartTs(Txn)`: 交易读取的区块 snapshot sequence number。
- `EndTs(Txn)`: 共识决定的交易在 block 中的位置。
- 同 block 内任意两笔交易都 concurrent，但 concurrent 交易不一定在同一 block；Fabric++ 只在 block scope 内重排，因此会漏掉跨 block concurrent 依赖。

### Serializability 与 reorderability

论文采用 snapshot transactions 的六类 canonical dependencies: `n-ww`, `n-wr`, `n-rw`, `c-ww`, `c-rw`, `anti-rw`。关键结论是:

- 没有 `anti-rw` 的调度满足 Strong Serializability。
- Fabric/Fabric++ 会拒绝产生 `anti-rw` 的交易，因此比 Fabric protocol 所需的 Serializability 更严格。
- 区块链 immutability 限制重排只能发生在 pending concurrent transactions 之间，不能改变已经 committed block 的相对顺序。
- `c-rw` 与 `anti-rw` 在交换 commit order 后仍保持同一依赖方向；`c-ww` 交换 commit order 会翻转依赖方向。
- Theorem 2: 若某个 cycle 中没有涉及 pending transactions 的 `c-ww`，该调度无法通过重排变成 serializable；若 cycle 含 pending `c-ww`，则可能通过翻转依赖方向解除 cycle。

这也是论文相对 Fabric++ 的核心理论细化: 不是所有冲突都该预防性 abort，只有不可能靠 pending `c-ww` 重排修复的 cycle 才应在 ordering 前丢弃。

### Fine-grained concurrency control

算法分三步:

1. Contract simulation: endorser 在模拟开始时读取最新 block number，并在该 snapshot 上执行合约，输出 readset/writeset 与 snapshot block number。
2. Transaction arrival: orderer 在共识决定交易相对顺序后，基于 pending set 和已提交交易计算除 pending `c-ww` 外的依赖；若加入新交易会形成不可重排 cycle，则直接丢弃，否则把它加入 pending graph。
3. Block formation: 对 pending transactions 按依赖可达性做 topological sort，形成 commit order；随后按该顺序恢复 pending `c-ww` 依赖并清空 pending set。

论文强调这个方法比 Fabric++ 更细粒度: 不再局限 block 内重排；不可串行化交易在 ordering 中提前 abort；剩余交易不再需要 validation 阶段的并发有效性检查。

### 实现细节

FabricSharp/FastFabricSharp 的大部分实现位于 orderers，Algorithm 1 在 peers/endorsers 侧支持 snapshot-consistent simulation。Orderer 侧维护:

- `CommittedWriteTxns (CW)`: LevelDB 中按 record key + commit sequence 记录已提交写事务。
- `CommittedReadTxns (CR)`: LevelDB 中按 record key + commit sequence 记录已提交读事务。
- `PendingWriteTxns (PW)` 与 `PendingReadTxns (PR)`: 内存索引，记录 pending transactions 的读写 key。
- Dependency graph `G`: 保存 transaction immediate successors，并用 Bloom filter 表示能到达某 transaction 的前驱集合。

Cycle detection 通过测试 predecessor/successor 是否已有 reachability 来完成。Bloom filter 有 false positive，因此可能预防性 abort 某些可串行化交易；论文用 relay 的两个 Bloom filters 控制 false positive 率。Graph pruning 用 `max_span` 限制交易跨越区块数，并用 transaction `age` 删除不再可能影响 pending transactions 的旧节点。

### 安全与活性边界

Safety 方面，论文认为算法作为 ordering process 的确定性步骤复制到所有 honest orderers 上后，不改变 hash chain integrity、no skipping、no creation，并且在相同 transaction stream 上 deterministic reordering 可保持 agreement。

Liveness 方面，算法可能破坏 Fabric 的 validity 属性，因为被算法 abort 的交易不会进入 ledger。论文指出 malicious leader 如果提前看到交易读写集，可能构造并排列一个代理交易以 defer 目标交易。缓解方式是先让客户端只向 orderers 发送 transaction hash；排序确定后再披露交易细节，既隐藏 accessed records，也防止客户端在排序后篡改交易内容。

## 实验与证据

| 维度 | 设置/结果 | 证据锚点 | Caveat |
| --- | --- | --- | --- |
| Fabric raw vs effective throughput | No-op/raw throughput 约 677 tps；update workload 中 skew 越高，因 serializability abort 导致 effective throughput 越低 | Fig. 1, §1 | 这是作者的 Fabric 1.3 环境，不代表所有 Fabric 版本 |
| Block size | FabricSharp 在 block size 100 达到 542 tps；Fabric/Fabric++/Focc-s/Focc-l peak 分别为 411/437/327/415 tps；相对 Fabric++ 提升约 25% | §5.3, Fig. 10 | 以 effective throughput 计；block size 改变也影响 latency 和 contention |
| Write hot ratio | FabricSharp 在不同写热点比例下保持最高吞吐；Focc-s 因预防性禁止 `c-ww` 明显下降 | §5.3, Fig. 11 | FabricSharp 的 ww restoration 占 reordering delay 较大比例，且随写热点增加 |
| Read hot ratio | 读热点增加会让大多数系统吞吐下降；FabricSharp 的 transaction processing latency 主要来自 reachability update | §5.3, Fig. 12 | 读写冲突多时 Algorithm 2 traversal 开销增大 |
| Client delay | 客户端延迟增加导致 block span 和依赖更多，吞吐下降；FabricSharp 仍优于 baselines | §5.3, Fig. 13 | 较长端到端延迟会增加 graph traversal hops |
| Read interval | 长执行交易更容易跨 block read；Fabric++ 早停跨 block 交易，Fabric 因 read-write lock 退化明显 | §5.3, Fig. 14 | Focc-s/Fabric++/FabricSharp 的 abort 类型不同 |
| FastFabricSharp | Create Account workload 下 FastFabric raw 3114 tps，FastFabricSharp effective 2960 tps，重排 overhead <5%；mixed workload θ=1 时 FastFabricSharp 2370 tps，FastFabric 1424 tps，提升 66% | §5.4, Fig. 15 | FastFabricSharp 收益主要来自 anti-rw 交易被序列化而不是被 FastFabric abort |

## 相关工作边界

- Fabric++: 同样减少 EOV invalid transactions，但主要在 consensus 后、block formation 前做重排；本文认为它忽略跨 block concurrent dependencies，并且比 Serializability 更保守。
- FastFabric: 通过拆分节点功能提高 Fabric implementation throughput；与本文方法正交，本文在 FastFabric 上叠加为 FastFabricSharp。
- Blockchain Meets Database: 更像把 PostgreSQL/SSI/MVCC 作为区块链执行 substrate；本文则保留 Fabric/FastFabric EOV 架构，把数据库 OCC 的分析方法迁移到 orderer-side transaction scheduling。
- 数据库 OCC 文献: 提供 snapshot isolation、serializability、dangerous pattern、operation reordering 的理论和算法来源，但不能直接搬到区块链，因为 committed blocks 不可重排，且 ordering service 与共识安全是额外边界。

## 限制与边界

- 适用对象主要是 permissioned EOV blockchains，尤其 Fabric/FastFabric 家族；不直接处理 permissionless consensus、Sybil resistance 或 incentive compatibility。
- 算法可能为了 liveness/safety 边界而排除交易，因此“剩余交易 serializable”不等于“所有 broadcast 交易都进入 ledger”。
- Bloom filter false positives、`max_span` stale snapshot pruning、complex transaction fallback 都可能导致额外 abort。
- 安全讨论依赖 ordering service 的原有 consensus safety/liveness 模型；本文不证明新的 consensus 协议。
- 评估 workload 主要是 Smallbank-style 和 FastFabric 的两个 workload；复杂智能合约、跨链/跨片交易和开放网络延迟未覆盖。

## Knowledge Handoff

| Candidate | Generality class | Target handling | Reason |
| --- | --- | --- | --- |
| Execute-order-validate transaction processing | method route | add source extension under [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | EOV 是可复用架构模式，但当前 vault 更适合先作为方法路线而非独立 node |
| OCC-inspired dependency analysis for EOV | method route / bridge pattern | update [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] and [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | 论文直接将 OCC/serializability 分析迁移到区块链 orderer |
| FabricSharp/FastFabricSharp | source instance | keep inside source note and representative source rows | 系统名是本文实现，不应提升为基础概念 |
| Strong Serializability vs Serializability in EOV | source-backed insight | add to source extension and bridge transfer boundary | 有助于解释为什么数据库式分析可以减少 over-abort |
| Bloom-filter reachability dependency graph | implementation detail | keep in source note | 是本文算法实现，不是当前上层知识节点 |

## Cold-Start Hierarchy Discovery

| Facet | Value | Durable handling |
| --- | --- | --- |
| Research field/domain | Blockchain systems; distributed transaction processing | `blockchain-systems` primary, `distributed-systems` secondary |
| Research background | EOV chains improve concurrency but validation abort wastes limited block throughput | background/update in blockchain transaction processing |
| Research problem | Reducing invalid transactions while preserving serializability in EOV blockchains | source extension under transaction-processing |
| Foundation concepts | optimistic concurrency control, snapshot isolation, serializability, dependency graph | `distributed-systems/transaction-processing` remains foundation_thin; direct foundation source still queued |
| Method family | OCC-inspired fine-grained dependency analysis and reordering | method row, bridge pattern |
| Application/evaluation context | Hyperledger Fabric, FastFabric, Smallbank-like workloads | source detail |
| Source instance | FabricSharp, FastFabricSharp | source-only/system instance |

## Retrieval Optimization

- 未来问“FabricSharp 是什么、解决什么问题、和 Fabric++ 区别是什么”时，本 source note 可直接回答，不需要重新打开 PDF。
- 未来问“数据库 OCC 如何迁移到区块链执行层”时，优先读 bridge，再到本 note 和 Blockchain Meets Database。
- 未来问“EOV 为什么会 abort 交易、如何降低 invalid transaction rate”时，优先进入 blockchain transaction processing 节点，再打开本 note。
- 仍保留 source-only 的内容: Bloom filter relay 细节、CW/CR/PW/PR 数据结构、实验曲线逐点值。

## Relation Extraction

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| `arxiv:2003.10064v1` | instance_of | `blockchain-systems/execution-and-transactions/transaction-processing` | abstract, §2-§5 | high | active_seed |
| `arxiv:2003.10064v1` | bridges | `distributed-systems/transaction-processing -> blockchain-systems/execution-and-transactions/transaction-processing` | §3-§4 | high | active_seed |
| `OCC-inspired EOV reordering` | solves | invalid transaction reduction in EOV blockchains | §3.4, §5 | high | source_extension |
| `FabricSharp` | implements | OCC-inspired EOV reordering on Fabric 1.3 | §4-§5 | high | source_only |
| `FastFabricSharp` | implements | OCC-inspired EOV reordering on FastFabric | §4, §5.4 | high | source_only |
| `transaction hash before detail disclosure` | mitigates | leader manipulation of accessed-record visibility | §3.5 | medium | source_extension |

## 吸收决策

- Queue 原分类 `blockchain-systems/execution-and-transactions/transaction-processing` 精读后确认正确。
- Primary path 保持 `blockchain-systems/execution-and-transactions/transaction-processing`，因为 durable problem 是 EOV 区块链交易执行与 serializability。
- Secondary path 传播到 `distributed-systems/transaction-processing`，因为论文直接复用 OCC、snapshot isolation、dependency graph 和 serializability 理论。
- 不新建 `FabricSharp` 或 `execute-order-validate` 知识节点；当前作为 source extension/method route 足够，等 Fabric++、Nezha、parallel EVM 等来源继续进入后再复核 split gate。

## Review Items

| Item | Reason | Status |
| --- | --- | --- |
| 经典 OCC/SSI/serializability foundation source 仍缺 | 本文是强迁移证据，但不是数据库事务基础教材 | queued |
| EOV 是否应拆成 child method node | 目前只有 Fabric/Fabric++/FabricSharp 线索，等 Fabric++ 原论文和后续 EOV source 进入后再判断 | review |
| FabricSharp GitHub 实现 | 论文参考列出 GitHub，但本次按 PDF 吸收，未读取仓库 | optional_future_source |
