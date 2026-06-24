---
id: "doi:10.1109/icdcs54860.2022.00034"
title: "Nezha: Exploiting Concurrency for Transaction Processing in DAG-based Blockchains"
type: "source"
source_kind: "paper"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
identity_key: "doi:10.1109/icdcs54860.2022.00034"
doi: "10.1109/ICDCS54860.2022.00034"
arxiv_id: ""
canonical_url: "https://doi.org/10.1109/ICDCS54860.2022.00034"
local_pdf: "~/Desktop/paper/Nezha_Exploiting_Concurrency_for_Transaction_Processing_in_DAG-based_Blockchains.pdf"
sha256: "9a7ad95a00bf8cc4e32ffeddfc52642f7cb84e96e2de0f7d7ed59cea7e224f1e"
page_count: 11
venue: "2022 IEEE 42nd International Conference on Distributed Computing Systems (ICDCS)"
year: "2022"
authors:
  - "Jiang Xiao"
  - "Shijie Zhang"
  - "Zhiwei Zhang"
  - "Bo Li"
  - "Xiaohai Dai"
  - "Hai Jin"
extracted_text_path: "vault/02_Raw/pdf/extracted/nezha-exploiting-concurrency-for-transaction-processing-in-dag-based-blockchains-9a7ad95a00bf-pages.txt"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0065"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
topic_ids:
  - "transaction-processing"
  - "dag-based-blockchain-execution"
  - "concurrency-control"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing"
related_knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
  - "nahida-knowledge-blockchain-execution-and-transactions"
  - "nahida-knowledge-blockchain-transaction-processing"
  - "nahida-knowledge-transaction-processing"
bridge_refs:
  - "nahida-bridge-database-transaction-processing-to-blockchain-execution"
promotion_decisions:
  - candidate: "Nezha"
    handling: "source_extension"
    reason: "Nezha 是一篇论文提出的具体系统/方案；上层可复用层是 DAG-based blockchain transaction-processing concurrency control。"
  - candidate: "address-based conflict graph"
    handling: "method_row"
    reason: "ACG 是论文方法，可作为 transaction-processing 节点的方法路线；单篇 source 不足以拆独立知识节点。"
  - candidate: "hierarchical sorting"
    handling: "method_row"
    reason: "HS 是 ACG 上的排序算法，保留在 source note 和方法路线中。"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "transaction-processing"
  - "dag-based-blockchain"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-nezha-dag-transaction-processing"
source_refs:
  - "doi:10.1109/icdcs54860.2022.00034"
confidence: "high"
trust_tier: "primary"
---

# Nezha: Exploiting Concurrency for Transaction Processing in DAG-based Blockchains

## 身份与读取状态

| Field | Value |
| --- | --- |
| Title | Nezha: Exploiting Concurrency for Transaction Processing in DAG-based Blockchains |
| Authors | Jiang Xiao; Shijie Zhang; Zhiwei Zhang; Bo Li; Xiaohai Dai; Hai Jin |
| Venue | ICDCS 2022 |
| DOI | `10.1109/ICDCS54860.2022.00034` |
| Local PDF | `~/Desktop/paper/Nezha_Exploiting_Concurrency_for_Transaction_Processing_in_DAG-based_Blockchains.pdf` |
| SHA-256 | `9a7ad95a00bf8cc4e32ffeddfc52642f7cb84e96e2de0f7d7ed59cea7e224f1e` |
| Pages | 11 |
| Reading status | `deep_read_complete` |

> [!note]
> 队列元数据曾从 DOI 字符串误抽出 `4860.2022` 作为 arXiv-like ID；本文本身是 IEEE ICDCS 论文，当前 source note 将 `arxiv_id` 置空。

## 一句话摘要

Nezha 面向 main-chain/parallel-chain DAG-based blockchains 中“多个 blocks 并发产生但交易仍串行处理”的瓶颈，提出 address-based conflict graph（ACG）和 hierarchical sorting（HS），用地址依赖替代成对交易依赖来检测/排序冲突交易，从而在高冲突 workload 下比传统 conflict graph 路线显著降低并发控制延迟和 abort rate。

## 论文要解决的问题

DAG-based blockchains 通过并行生成 blocks 提高 consensus/block production throughput，但如果交易执行仍按串行方式处理，执行层会削弱 DAG 结构带来的吞吐优势。若直接并发执行多个 concurrent blocks 的交易，又会在 account-based data model 中放大读写同一地址的冲突。

论文把问题表述为: 对 epoch `e` 中 `N_e` 笔交易，若任意两笔交易发生冲突的概率是 `p`，潜在冲突数约为 `N_e(N_e-1)/2 * p`。当 block concurrency 增加时，冲突数量随交易对数量呈平方级增长。传统 conflict graph（CG）需要比较交易对、检测/删除 cycle、再拓扑排序，在 DAG-based blockchain 的高并发/高冲突场景中开销会失控。

## 背景与相关路线

论文区分三类 DAG-based blockchain: natural DAG（如 IOTA、SPECTRE）、main-chain-based DAG（如 Conflux、Prism）和 parallel-chain-based DAG（如 OHIE、Occam、Hashgraph、DAG-Rider）。Nezha 关注后两类，因为它们通过多个 consensus nodes / parallel chains 并发产块，且更适合支持 smart contracts。

传统 blockchain transaction processing 往往是 proposer 先模拟执行并把 scheduling information 放入 block，再共识，再由其他节点验证/提交。但论文指出这一框架不适合 DAG-based blockchains: 如果不同 consensus nodes 在出块前基于本地状态执行交易，会导致 execution results divergent；其他节点验证这些结果需要重放 concurrent blocks，开销很高。因此 Nezha 采用类似 Conflux deferred execution 的调整: consensus nodes 先广播 blocks，不在出块前执行交易；节点在收到一个 epoch 的 concurrent blocks 后，再并发执行这些交易并做 concurrency control。

论文比较的 concurrency-control 类别包括:

| 类别 | 代表 | 局限 |
| --- | --- | --- |
| Pessimistic concurrency control | PEEP | 锁开销会损害 DAG 高吞吐场景。 |
| Optimistic concurrency control | Fabric, SlimChain | 高 contention 下 abort rate 高，论文引用 Fabric 场景中无效交易超过 40% 的问题。 |
| OCC with conflict graph | Fabric++, FabricSharp, ParBlockchain, Jin et al., Dickerson et al., FastBlock | CG 需要捕获交易对依赖，cycle detection/removal 在高冲突下昂贵；STM/HTM 路线引入软件/硬件假设。 |

## 系统模型

Nezha 假设底层 DAG-based blockchain 采用 main-chain 或 parallel-chain 结构，允许多个 valid blocks 在同一 epoch 中并行生成；数据模型是 account-based，而不是 UTXO-based，因为论文关心的是读写同一 account address 引发的并发冲突。

论文用 `B = {B_e | e >= 0}` 表示 blockchain，每个 epoch `e` 有一组 concurrent valid blocks `B_e = {b^e_k | 0 <= k < omega_e}`，其中 `omega_e` 是 block concurrency。交易处理以 epoch 为单位: 节点收到 epoch `e` 的多个 blocks 后，基于上一个 epoch 的 state snapshot 并发执行这些 blocks 中第一次出现的交易。

## 交易处理流程

Nezha 的 DAG transaction-processing workflow 包含四个阶段:

| 阶段 | 作用 | 关键细节 |
| --- | --- | --- |
| Validation | 验证 concurrent blocks | 每个 block 包含 previous epoch state root；节点检查该 root 是否对应上一 epoch 状态。 |
| Concurrent execution | 并发/投机模拟交易执行 | 选择 verified blocks 中首次出现的交易，基于最新 state snapshot 模拟执行，记录每笔交易的 read/write addresses 和 values。 |
| Concurrency control | 发现冲突并生成调度信息 | 构造 ACG，基于 HS 给交易分配 total commit order。 |
| Commitment | 按 commit order 更新状态 | 交易写入 in-memory state，随后 flush 到底层数据库。相同 sequence number 的交易可并发提交。 |

## Strawman: transaction-dependency conflict graph

论文先定义 transaction dependency。给定 `T_u` 和 `T_v`，若 `T_u` 读/写的地址被 `T_v` 写，则存在依赖:

- `T_u ->rw T_v`: `RS(T_u) ∩ WS(T_v) != empty`。
- `T_u ->ww T_v`: `WS(T_u) ∩ WS(T_v) != empty`。

传统 CG 把 transactions 作为 vertices，把 transaction dependencies 作为 edges。并发控制包括 graph construction、cycle detection/removal 和 topological sorting。论文认为它在 DAG-based blockchain 中有三个核心瓶颈:

- 构图需要比较交易对，开销近似 `O((|V|^2-|V|)/2)`。
- cycle detection/removal 在大量冲突下昂贵；论文提到 Fabric++ 用 Johnson's algorithm，复杂度随 cycle 数显著上升。
- 拓扑排序得到的是 serial commit order，无法利用 non-conflicting transactions 的并发提交能力。

## Nezha 方法: address-based conflict graph

Nezha 的核心洞察是: 在 DAG 并发块场景中，冲突交易会集中到地址层面；与其捕获每一对 transaction dependency，不如按 address 收集读/写单元，并用 address dependency 表示地址之间的排序约束。

论文为每个 address `A_j` 维护 read/write set `RW_j`，并把交易的读写拆成更细粒度的 `T^R_v` 和 `T^W_v`。每个交易的 read/write units 被映射到对应地址的 `RW_j` 中；在同一地址上，read units 放在 write units 前面，以尊重 read-write dependency order。

地址依赖定义为: 对两个地址 `A_i` 和 `A_j`，如果存在交易 `T_v`，它的 write unit `T^W_v` 在 `RW_i` 中，read unit `T^R_v` 在 `RW_j` 中，则 `A_i` 依赖 `A_j`。直觉是: 某交易写 `A_i`、读 `A_j`，说明 `A_i` 上的写入排序会影响 `A_j` 上交易集的正确排序。

ACG（address-based conflict graph）将 vertices 设为 address read/write sets `RW_j`，edges 设为 address dependencies。这样构造成本从交易对比较降到按交易读写单元映射，论文给出复杂度 `O(u * N_e)`，其中 `u` 是每笔交易平均 read/write units 数量。

## Nezha 方法: hierarchical sorting

ACG 之后，Nezha 需要为交易生成 deterministic total commit order，同时尽量保留并发。论文借用 Lamport logical clock 的思路，为每个 read/write unit 分配 sequence number；同一交易的所有 read/write units 需要具有相同 sequence number。

同一地址上的基本排序规则:

- read unit 的 sequence number 小于其他交易的 write unit。
- 两个 write units 按交易 id/subscript 排序，保证 deterministic sorting。
- 两个 read units 不冲突，可以分配相同 sequence number。

地址之间如果有依赖，先排序哪个地址会影响结果。论文展示了 sorting anomaly: 若先给被依赖地址的 read units 分配相同 sequence number，后续在依赖地址上可能发现这些交易其实存在 read-write 或 write-write 冲突。解决思路是按 address dependency 决定 address sorting priority。

### Sorting rank division

论文把 address dependencies 形成一个 graph，对 addresses 做 topological sorting 来得到 sorting ranks。若图中有 cycles，Nezha 不直接做昂贵的 cycle removal，而是选择 in-degree 最小的地址；若多个地址 in-degree 相同，优先 out-degree 最大者；若仍相同，按 address subscript。这个启发式让高影响地址优先排序。

### Transaction sorting

每个地址内排序时，算法先处理 read units:

- 如果没有已分配 sequence 的 read units，则所有 read units 取得 initial sequence。
- 如果已有 read units，则用其中最小 sequence 给剩余 read units，记录 read units 最大 sequence。

随后处理 write units:

- 若某个 write unit 已有 sequence 且同一地址上也有该交易的 read unit，则把该交易 sequence 调整到大于 read units 最大 sequence。
- 若某个 write unit 的 sequence 小于 read units 最大 sequence，说明出现 unserializable transaction，默认 abort 该交易。
- 剩余 write units 取得未使用的递增 sequence。

相同 sequence number 的交易可并发提交；这也是 Nezha 相比普通 CG serial topological order 的一项收益。

## Reordering 增强

论文进一步利用 FabricSharp/Fabric++ 类工作中的 reorderability 直觉: 某些由 write-write dependencies 引起的 unserializable transactions 可以通过交换写入顺序变得 serializable。

当发现一个 write unit 因 sequence 异常将被 abort 时，Nezha 检查该交易是否在另一个地址上也有 write unit；若有，则将该交易 sequence 调整为相关地址上最大 sequence 之后的值。这样可以避免一部分 write-write anomaly 导致的 abort。论文的实验显示该增强在高 skew 下让 Nezha abort rate 低于 CG。

## 实现

论文实现了 Go 原型:

- 底层 DAG blockchain: OHIE，一个 parallel-chain DAG-based blockchain。
- Execution layer: 基于 EVM 支持 Solidity smart contracts。
- Read/write logger: 记录每笔交易读取和写入的 addresses/values。
- 并行执行/提交: 多 worker threads。
- Storage: LevelDB 存储 block/state data，Merkle Patricia Trie 组织 account state objects。

## 实验设置

实验在 Alibaba Cloud 上运行 14 个节点:

- 12 个 miner nodes 并行提出 blocks。
- 1 个 full node 同步全系统状态。
- 1 个 client 提交 transactions。
- miner/full node: Intel Xeon Ice Lake Platinum 8369B, 16 vCPUs, 64 GB RAM, Ubuntu 20.04。
- client: 4 vCPUs, 16 GB RAM。

底层 OHIE 最大 block concurrency 设为 12，block size 为 200 transactions。每个实验至少运行 4 次并取平均。论文测量 full node 侧的 transaction processing 和 system throughput。

对比方案:

| Scheme | 含义 |
| --- | --- |
| Serial | 当前 DAG-based blockchains 常见的串行交易处理；用 EVM 串行执行和提交。 |
| CG | Strawman conflict graph；使用 Fabric++/FabricSharp 类 graph construction and processing，Tarjan/Johnson 做 cycle detection/removal。 |

Workload 使用 SmallBank benchmark 的 Solidity contract，六类交易: `updateSavings`, `updateBalance`, `sendPayment`, `writeCheck`, `almagate`, `getBalance`。账户数 10k，访问 skew 服从 Zipfian distribution；`skew = 0` 表示 uniform distribution。

## 实验结果

### Transaction processing latency

在 uniform workload (`skew = 0`) 下，Serial latency 随 block concurrency 从 2 到 12 由 4.7s 增至 36.6s。Nezha 的 simulation execution latency 从 123.4ms 到 743.4ms，concurrency control + commit latency 从 22.1ms 到 87.1ms。论文总结 Nezha 相比 Serial 的 transaction-processing latency 最多可达到 40x speedup。

Nezha 与 CG 比较时，二者 simulation mechanism 相同，所以只比较 concurrency control + commit。论文在 `skew = 0.2, 0.4, 0.6, 0.8` 下测试:

- CG latency 随 block concurrency 增长更快。
- 在 `skew = 0.6` 且 block concurrency 为 12 时，CG latency 超过 10s。
- 在 `skew = 0.8` 且 block concurrency 超过 4 时，CG 因 out of memory 失败。
- Nezha 在高 contention 下 concurrency-control latency 仍低于 100ms。
- 论文总结 Nezha 相比 CG 的 concurrent transaction processing 最多可达到 10x speedup。

### Sub-phase latency

在 block concurrency 固定为 4、`skew = 0.5` 和 `0.6` 时，CG 的主要开销来自 graph construction 或 cycle detection/removal；`skew = 0.6` 时 Johnson's algorithm 的 cycle detection/removal 变成主要瓶颈。Nezha 因为 ACG 和 HS 不需要 transaction-pair dependency graph 和 cycle detection，graph construction overhead 几乎可以忽略，sorting latency 更稳定。

### Abort rate

论文在 block concurrency 为 1 时比较 Nezha 和 CG 的 abort rate:

| Zipfian skew | Nezha abort rate | CG abort rate |
| --- | --- | --- |
| 0.6 | 2% | 3% |
| 0.7 | 5.5% | 6% |
| 0.8 | 8.5% | 10.5% |
| 0.9 | 14% | 17% |
| 1.0 | 19.5% | 23% |

Nezha 在 skew 升高时优势更明显；论文将差异归因于 reordering enhanced design 能处理部分 write-write dependency 引起的 unserializable transactions。

### Effective throughput

论文将 effective throughput 定义为通过 transaction processing 并持久化状态的 valid transactions 数量，而不是单纯 consensus throughput。预期 block generation latency 为 1s。

Serial 即使在大 block concurrency 下也约在 60 tps 左右，说明串行 EVM 执行拖住了 DAG consensus 的吞吐。CG 在低 skew/低 concurrency 下能提升 throughput，但在高 concurrency 和高 skew 时受 concurrency-control latency 与 abort rate 影响，甚至在 `skew = 0.6`、block concurrency 为 12 时吞吐大幅下降。Nezha 的 throughput 随 block concurrency 近似线性增加，且 `skew = 0.6` 相比 `skew = 0.2` 不会明显下降。摘要给出的总体结论是: 在高 contention 下，Nezha 相比 conventional conflict graph scheme 可将 throughput 提高最多 8x。

## 贡献与局限

| 维度 | 内容 |
| --- | --- |
| 主要贡献 | 首次聚焦 DAG-based blockchain concurrent transaction processing 的冲突问题；提出 ACG 和 HS；用地址依赖降低冲突检测/排序开销；让 commit order 保留并发。 |
| 方法边界 | 适用于 account-based main-chain/parallel-chain DAG-based blockchains；论文不覆盖 UTXO natural DAG 的 irregular topology。 |
| 系统边界 | 底层原型是 OHIE + EVM + LevelDB/MPT；结果不直接等价于 Conflux、Prism、Hashgraph 或生产 EVM/parallel VM。 |
| 安全边界 | Nezha 是 execution/concurrency-control 机制，不提供 consensus safety、Byzantine ordering、mempool liveness 或开放网络激励安全。 |
| 实验边界 | Alibaba Cloud 同地域 14 节点；workload 是 SmallBank/Solidity，账户访问按 Zipfian skew；没有覆盖复杂 DeFi/stateful smart contract 生态。 |

## 知识层吸收决策

| Candidate | Generality | Handling | Reason |
| --- | --- | --- | --- |
| Nezha | source-specific system | source extension | 论文系统名不应成为上层概念；细节保留在本 source note。 |
| DAG-based blockchain concurrency control | reusable problem/method route | method row under [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | 它是 execution/transaction processing 的可复用问题。 |
| Address-based conflict graph | method | method row/source-contained details | 单篇直接来源，不拆独立 node；未来若出现多篇 address-level scheduling source 可复核。 |
| Hierarchical sorting | method | method row/source-contained details | 算法细节保留在 source note；上层只记录路线和适用边界。 |
| Database/distributed transaction processing bridge | bridge strengthening | update [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] | Nezha 将 conflict graph、serializability、reordering 从数据库/并发控制思想迁移到 DAG blockchain execution。 |

## Evidence anchors

| Anchor | Evidence | Confidence |
| --- | --- | --- |
| p1-p2 / Abstract and Introduction | DAG blockchains 并发块带来并发交易冲突；Nezha 提出 ACG/HS；摘要给出 up to 8x throughput and 10x latency over CG | high |
| p3-p4 / Background and System Overview | main/parallel-chain DAG 分类、deferred execution workflow、四阶段 transaction processing | high |
| p5-p6 / Strawman and ACG | transaction dependency、CG 瓶颈、address dependency、ACG 定义与 `O(u*N_e)` 构图 | high |
| p7-p8 / Hierarchical Sorting | sorting anomaly、address rank division、transaction sorting、unserializable transaction detection | high |
| p8 / Reordering | write-write dependency reorderability 用于减少 abort | medium-high |
| p8-p9 / Implementation | Go, OHIE, EVM, read/write logger, worker threads, LevelDB, MPT | high |
| p9-p11 / Evaluation | cluster setup, SmallBank workload, Serial/CG baselines, latency/abort/throughput results | high |

## 后续队列与复核

- 继续吸收后续 parallel execution / SlimChain / LightCross / SChain 类论文后，复核 `dag-based-blockchain-concurrency-control` 是否需要从 method row 拆成 child knowledge node。
- 若未来引入 Block-STM、parallel EVM、Aptos/Sui execution 等资料，应比较 optimistic parallel execution、static access declaration、deterministic scheduler 与 Nezha 的 address-dependency route。
- 若要补 foundation，建议用 `nahida-research-search` 或经典数据库 sources 建立 `concurrency control / serializability / conflict graph` 更完整的基础概念。
