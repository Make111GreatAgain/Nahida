---
id: "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
title: "TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus"
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
  - "p2-p3 motivation, related work, consensus/execution taxonomy"
  - "p4-p8 overview, State Hash Table, intra-block and intra-instance execution"
  - "p8-p10 inter-instance merging and Dynamic Commitment Epoch"
  - "p10-p13 experiments"
  - "p13-p14 conclusion and references"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown in extracted PDF"
year: "2024"
pdf_pages: 14
pdf_sha256: "69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
local_pdf: "~/Desktop/paper/v_icde2024r2_execution_camera_ready.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/v_icde2024r2_execution_camera_ready-69daae93b34a-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
topic_ids:
  - "transaction-processing"
  - "leaderless-consensus-execution"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
  - "leaderless-consensus-execution"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution/sha256-69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
secondary_ontology_paths:
  - "blockchain-systems/consensus/permissioned-blockchain-consensus/sha256-69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "distributed-systems/transaction-processing/sha256-69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "execution-and-transactions"
    - "consensus"
    - "transaction-processing"
  topics:
    - "transaction-processing"
    - "leaderless-consensus-execution"
    - "permissioned-blockchain-consensus"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "permissioned blockchain"
  - "transaction execution"
  - "leaderless consensus"
  - "multi-leader consensus"
  - "parallel execution"
  - "optimistic deterministic concurrency control"
  - "State Hash Table"
  - "Dynamic Commitment Epoch"
aliases:
  - "TELL"
  - "Efficient transaction execution towards leaderless consensus"
  - "State Hash Table"
  - "Dynamic Commitment Epoch"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
  - "leaderless-consensus"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "execution-and-transactions"
  problem:
    - "transaction execution under leaderless consensus"
    - "commit latency from slow consensus instances"
    - "deterministic execution of out-of-order blocks"
    - "conflict detection and serialization for parallel blockchain execution"
  method_family:
    - "optimistic deterministic concurrency control"
    - "speculative block execution"
    - "inter-instance execution-result merging"
    - "dynamic commitment epochs"
  system_layer:
    - "transaction execution module"
    - "consensus-execution boundary"
    - "state database"
  evaluation_context:
    - "RCC consensus instantiated with PBFT"
    - "SmallBank workload"
    - "LevelDB state database"
    - "single data-center controlled experiments"
  application:
    - "permissioned blockchain"
  bridge:
    - "permissioned consensus to transaction execution"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-tell-leaderless-consensus-execution"
source_refs:
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "pdf:~/Desktop/paper/v_icde2024r2_execution_camera_ready.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> execution-and-transactions"
secondary_directions:
  - "blockchain-systems -> consensus"
  - "distributed-systems -> transaction-processing"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title, abstract, and introduction explicitly target permissioned blockchain transaction execution towards leaderless consensus"
  - "Sections II-IV define consensus-execution taxonomy, TELL design, SHT, speculative execution, merging, and DCE"
  - "evaluation instantiates RCC with PBFT and measures transaction execution latency/throughput"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0035"
queue_status: "absorbed"
---

# TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus

## 论文身份

- 标题: TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus
- 作者: Xing Tong, Zheming Ye, Zhao Zhang, Cheqing Jin, Aoying Zhou
- 机构: School of Data Science and Engineering, East China Normal University
- 年份: 2024 from queue/filename
- Venue/DOI/arXiv: extracted PDF 未给出；文件名显示 `icde2024r2_execution_camera_ready`，因此只作为弱 venue hint 记录，不写成强 canonical metadata。
- 本地 PDF: `~/Desktop/paper/v_icde2024r2_execution_camera_ready.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/v_icde2024r2_execution_camera_ready-69daae93b34a-pages.txt`
- SHA-256: `69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 14
- 已覆盖章节/页码: Abstract, Introduction, Background and Related Work, TELL overview, State Hash Table, intra-instance execution, inter-instance merging, Dynamic Commitment Epoch, experiments, conclusion。
- Extraction gaps: PDF 元数据未给出 DOI/arXiv/venue；部分图表需要依赖正文解释而不是完整图像数值。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | permissioned blockchain 性能同时受 consensus 和 transaction execution 影响；TELL 面向 leaderless consensus 做协同优化 | high |
| §2 / p2-p4 | 背景和相关工作 | leader-based vs leaderless consensus；transaction execution；Ordering-Execution 范式下 sequential、sequential-parallel、parallel、integrated parallel 分类 | high |
| §3 / p4-p5 | 系统总览 | 节点本地 `stateDB`、consensus module 与 transaction execution module 松耦合；每个 consensus instance 独立执行，周期性合并结果 | high |
| §4.A-B / p5-p6 | State Hash Table | SHT 用状态桶记录读写集合和依赖，避免完整 pairwise conflict detection | high |
| §4.C-D / p6-p8 | Intra-instance execution | block 内并行执行、BDS-style conflict serialization、abort 后重执行；同一 instance 的 blocks 按 height 顺序，out-of-order 时做 speculative execution | high |
| §4.E / p8-p9 | Inter-instances merging | 各 instance 独立执行后按 SHT bucket 交集检测冲突；选择 m-instance 使 abort 数更小 | high |
| §4.F / p9-p10 | Dynamic Commitment Epoch | 按各 instance block-producing interval 动态决定每个 DCE 包含多少 blocks，减少快速 instance 等待慢 instance | high |
| §5 / p10-p13 | 实验 | SmallBank, LevelDB, RCC+PBFT；比较 CGB、accumulated execution、static ordering 和 SharPer+SE | high |
| §6 / p13 | 结论 | TELL 是面向 leaderless consensus 的交易执行协议，核心机制为 SHT、speculative execution、merging、DCE | medium |

## 一句话贡献

TELL 将 permissioned blockchain 的交易执行协议改造成 leaderless/multi-leader consensus 的配套层：每个 consensus instance 先独立并行执行，再周期性、确定性地合并结果，并用 State Hash Table 和 Dynamic Commitment Epoch 降低冲突序列化与慢实例等待带来的执行/提交延迟。

## 核心问题设定

论文的核心观察是: 许可链性能不只由 consensus protocol 或 transaction execution protocol 单独决定，二者的边界也会产生瓶颈。Leaderless consensus 本质上是多个 leader-based consensus instances 并行运行。若 execution layer 仍用固定 epoch 等待所有 instances 的 blocks，快速 instance 的 blocks 会被慢 instance 拖住，形成 accumulated blocks 和持续增长的 waiting latency。Figure 1 和 Figure 2 用 4 个 instances 展示了这个问题: 慢 instance 让 ordering/commitment 无法及时完成，快速 instance 的 block 越积越多。

TELL 要解决的两个问题是:

- 同一 instance 顺序产块，但节点可能乱序收到 blocks；执行层如何确定性、高效地处理 out-of-order blocks。
- 不同 instances 并行产块且运行速度不同；执行层如何避免慢 instance 阻塞快 instance，并把多实例结果合并成一个确定状态。

## 方法与机制

### 系统边界

TELL 位于 transaction execution module，与 consensus module 松耦合。Consensus 负责产生 blocks；每个节点本地持有 `stateDB`，在本地执行 blocks，不需要在执行阶段再做节点间交互。Leader-based consensus 可视为只有一个 instance 的特例，因此 TELL 的结构也可退化到 leader-based 场景。

### State Hash Table

State Hash Table (SHT) 是 TELL 的 conflict metadata 结构。每个 bucket 对应一个状态或哈希桶，transaction node 记录该交易的 read set、write set 和执行依赖。属于同一个 bucket 的 transactions 被视为可能冲突，因此执行层不必对所有交易做完整两两冲突检测。论文把这描述为以空间换时间: conflict detection 从近似 `O(n^2)` 的 pairwise comparison 转向基于访问状态的 bucket 记录。

SHT 还记录 Execution Cascading (EC) 依赖。若 `Tj` 写入状态 `s`，而 `Ti` 读取了 `Tj` 写入的 `s`，则存在 `Ti -> Tj` 的依赖；当 `Tj` abort 时，`Ti` 也要 abort，反过来不一定成立。论文进一步区分 WTS/RTS 以及 WTSW/RTSW，用权重估计某个状态上 abort 不同交易集合的代价。

### Block 内并行执行与冲突序列化

在同一 block 内，transactions 先并行执行并填入 SHT。随后 TELL 使用 backward dangerous structure 思路做 conflict serialization: 检测 `Ti -rw-> Tj -rw-> Tk` 且满足序关系的结构时 abort 中间交易。作者没有追求 conflict graph 的最小 abort ratio，因为 Ordering-Execution 范式下 abort 后的交易会在本地确定性重执行，不需要额外网络轮次；因此 TELL 选择更容易并行、开销更低的序列化策略。

Abort 后的交易不重新从零检测冲突。由于 SHT 已记录访问状态和冲突依赖，冲突交易按确定顺序重执行，非冲突交易仍可并行执行。

### 同一 instance 的顺序与 speculative execution

同一 consensus instance 的 blocks 应按 block height 顺序生效。但网络或 Byzantine 行为可能让节点先收到较高 height 的 block。悲观策略会等待缺失 block；TELL 选择 optimistic speculative execution，先执行较高 block，等缺失 block 到达后再检测异常。

异常分为两类:

- Write-after-Read: 缺失 block 的交易写了 speculative block 已读取的状态，说明 speculative block 读到了旧值，需要 abort/re-execute。
- Write-after-Write: TELL 使用确定性 multi-version concurrency control。写入生成新版本，commit 顺序按 block number，读取选择对该 block 可见的最大版本，从而避免 update lost。

### 多 instances 合并

不同 instances 的执行结果周期性合并。若多个 instances 的 SHT bucket 没有交集，可直接 commit；若存在交集，则按确定性 instance 顺序做冲突序列化和重执行。论文为每个冲突 bucket 选择一个 `m-instance`: 在它之前的 instances commit RTS/abort WTS，在它之后的 instances abort RTS/commit WTS，并用 WTSW/RTSW 权重选择 abort 数更小的方案。

这个合并设计让 TELL 能在 consensus instances 并行运行时保持确定性状态更新，但它也意味着 conflict skew 和实例数增加会推高 abort/re-execution 成本。

### Dynamic Commitment Epoch

固定 epoch 会让快 instance 等慢 instance。Dynamic Commitment Epoch (DCE) 是 TELL 的 ordering/merging unit，它根据每个 instance 的 block-producing interval 动态决定一个 DCE 中包含哪些 blocks。

若预设 interval 为 `t`，某 instance 的 block interval 为 `ti`:

- `ti < t` 时，一个 DCE 可包含该 instance 的 `floor(t / ti)` 个 blocks。
- `ti > t` 时，该 instance 不是每个 DCE 都出现，而是每 `floor(ti / t)` 个 DCE 包含一个 block。
- 如果所有 instances 都慢于 `t`，则以最快 instance 为基准，其他 instances 按相对 interval 周期性加入。

为保证节点视图一致，leaders 为 block 构造 timestamp，timestamp 在 consensus 中被检查/确认；节点基于已确认 timestamp 计算 intervals，并拒绝超过合理阈值的 timestamp。

## 实验与证据

| 维度 | 设置/结果 | 证据锚点 | Caveat |
| --- | --- | --- | --- |
| 实验平台 | Same data center；RCC 作为 leaderless consensus，每个 instance 用 PBFT；LevelDB 作为 `stateDB` | §5.A, Fig. 11 | 控制环境，不是 WAN/开放网络 |
| Workload | SmallBank，100 万账户，Zipf skewness 控制冲突 | §5.A | 与真实合约/workload 的差异未系统覆盖 |
| Intra-block conflict serialization | TELL 的 abort ratio 接近 conflict graph-based baseline，但 latency 明显更低；高 skew 下 TPS 可显著超过 CGB | §5.B, Fig. 12 | TELL 通过更多 abort 换更低检测开销 |
| Speculative execution | out-of-order degree 增加时，TELL 比 accumulated execution 有更低 latency；高 skew 下仍有收益 | §5.C, Fig. 13-14 | skew 越高，hit ratio 和 accumulated aborts 增加 |
| Inter-instance merging | 吞吐随 instances 近似线性增长；高 skew 和多 instances 会导致 abort rate/merge latency 上升 | §5.D, Fig. 15-16 | throughput 指标排除了 consensus latency |
| DCE | 4 个 instances 手动设为 40ms/30ms/20ms/10ms，DCE 相比 static ordering 将 execution waiting latency 降低超过 90% | §5.E, Fig. 17 | 手动控制 interval；依赖 timestamp 确认机制 |
| Sharding/intra-shard | 将 TELL 用作 SharPer intra-shard execution，重负载下比 SharPer+sequential execution 最高约 8x TPS | §5.F, Fig. 18 | 这是 intra-shard execution 证据，不等同完整 sharding 协议 |

## 限制与边界

- 论文主要评估 execution module，throughput 不包含 consensus latency。
- 实验部署在 same data center，并通过控制实例速度来观察 DCE；对 WAN、真实 Byzantine 网络扰动和生产 workload 的覆盖有限。
- TELL 的核心是 protocol-level heuristic，不是形式化安全证明论文。
- SHT 通过 bucket 降低检测成本，但会引入空间开销；哈希/bucket 冲突可通过 separate chaining 保持正确性，但高冲突 workload 仍会增加 abort/re-execution。
- DCE 依赖共识确认 timestamp 与阈值检查；如果 timestamp 选择、时钟假设或 leader 行为约束不足，需要额外协议论证。
- TELL 面向 leaderless/multi-leader consensus 的 transaction execution，不应被误读为新的 consensus protocol。

## Knowledge Handoff

| Candidate | Generality class | Target handling | Reason |
| --- | --- | --- | --- |
| TELL | source instance | source extension under [[leaderless-consensus-execution]] | 具体论文系统/协议，不是基础概念 |
| State Hash Table | source-specific mechanism | source note detail; optional future method section | 当前只有 TELL source，暂不独立成 node |
| Dynamic Commitment Epoch | source-specific mechanism | source note detail; optional method section under leaderless execution | 当前由 TELL 提出，先作为代表方法 |
| transaction execution under leaderless consensus | reusable problem/method family | create [[leaderless-consensus-execution]] | 可服务未来 RCC/MIR-BFT/DAG/parallel consensus execution sources |
| blockchain execution-and-transactions | L2 direction | create [[execution-and-transactions]] | vault 已有 consensus/mempool/sharding，但缺执行层方向 |
| permissioned consensus to transaction execution | bridge | create [[permissioned-consensus-to-transaction-execution]] | TELL 明确把 consensus characteristics 作为 execution design input |

## Cold-Start Hierarchy Discovery

| Facet | Result | Evidence | Confidence |
| --- | --- | --- | --- |
| Research field/domain | `blockchain-systems` | paper scope: permissioned blockchain | high |
| Research background | consensus protocol and transaction execution jointly determine performance | abstract, §1 | high |
| Reusable research problem | transaction execution/commitment under leaderless consensus instances with different speeds | §1, Fig. 1-2 | high |
| Foundation concepts | consensus, leaderless consensus, transaction processing, concurrency control, deterministic execution | §2-§4 | medium-high |
| Method family | optimistic deterministic concurrency control plus execution-result merging | Table I, §4 | high |
| Application/evaluation context | permissioned blockchain, RCC+PBFT, SmallBank, LevelDB | §5 | high |
| Source instance | TELL, SHT, DCE | §3-§4 | high |

## Retrieval Optimization

- 未来问“leaderless consensus 下为什么交易执行会被慢实例拖住”时，优先读 [[leaderless-consensus-execution]]，只在需要 TELL 算法细节时打开本 source note。
- 未来问“区块链执行层有哪些方向”时，优先读 [[execution-and-transactions]] 和 [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]]，而不是扫描所有 blockchain papers。
- 未来问“consensus 和 execution 怎么协同设计”时，优先读 [[permissioned-consensus-to-transaction-execution]]。
- Source-only 内容: SHT bucket 结构、RTSW/WTSW 计算细节、Algorithm 1-3、具体实验曲线和参数。

## Domain Dynamics Impact

- Affected L1 domain: `blockchain-systems`
- Impact: 结构性新增一个执行/交易方向，并给出 consensus-execution co-design 的桥接证据；不是外部最新趋势证据。
- Dynamics action: refresh domain dynamics as existing-vault evidence, keep freshness as stale/queued for daily-fetch because no web/latest sources were fetched.

## Foundation Candidate Judgment

- `leaderless consensus`: foundation/method-family candidate; vault 已有 consensus sources，可由 consensus 节点承接，不由 TELL 定义。
- `transaction processing`: foundation_thin candidate; distributed systems 已有薄节点，blockchain-specific execution 需要本次新增方向。
- `TELL`, `SHT`, `DCE`: source instance/source-specific mechanisms；不单独晋升为基础概念。

## Review Items

| Item | Reason | Suggested action |
| --- | --- | --- |
| Venue metadata | PDF extraction did not expose DOI/venue; filename suggests ICDE 2024 camera-ready | later metadata verification if user wants canonical citation |
| Foundation gap | blockchain execution/concurrency control lacks survey or canonical foundation note | queue `foundation_pack` research/search |
| Generalization boundary | TELL uses RCC+PBFT and controlled datacenter experiments | compare with future MIR-BFT, Narwhal/Bullshark, Fabric/FISCO execution sources |
