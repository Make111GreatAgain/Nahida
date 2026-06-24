---
id: "arxiv-1804.00399v4"
title: "Towards Scaling Blockchain Systems via Sharding"
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
  - "p1-p16 full extracted text"
  - "Abstract, Sections 1-9, appendices A-C, figures, tables and references"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/1804.00399v4"
doi: ""
arxiv_id: "1804.00399v4"
venue: "arXiv preprint"
year: "2019"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "scaling-and-sharding"
topic_ids:
  - "sharded-ledgers"
  - "cross-shard-transactions"
  - "byzantine-fault-tolerance"
ontology_path:
  - "blockchain-systems"
  - "scaling-and-sharding"
  - "sharded-ledgers"
primary_ontology_path: "blockchain-systems/scaling-and-sharding/sharded-ledgers"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
  - "distributed-systems/transaction-processing/distributed-transactions"
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
    - "cross-shard-transactions"
    - "byzantine-fault-tolerance"
    - "distributed-transactions"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "sharded-ledgers"
  - "permissioned-blockchain"
  - "AHL"
  - "AHL+"
  - "TEE-assisted BFT"
  - "SGX"
  - "shard-formation"
  - "cross-shard-transactions"
aliases:
  - "AHL"
  - "AHL+"
  - "Attested HyperLedger"
  - "Towards Scaling Blockchain Systems via Sharding"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/blockchain-systems"
  - "nahida/sharding"
  - "nahida/bft"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "scaling-and-sharding"
  problem:
    - "permissioned blockchain sharding for general workloads"
    - "fault-scalable shard-level BFT"
    - "secure shard formation"
    - "cross-shard distributed transactions"
  method_family:
    - "TEE-assisted non-equivocating BFT"
    - "AHL+"
    - "trusted randomness beacon"
    - "two-phase commit"
    - "two-phase locking"
    - "BFT reference committee"
  system_layer:
    - "intra-shard consensus"
    - "validator assignment"
    - "shard reconfiguration"
    - "transaction coordination"
    - "chaincode execution"
  evaluation_context:
    - "BLOCKBENCH KVStore"
    - "BLOCKBENCH Smallbank"
    - "local 100-server cluster"
    - "Google Cloud Platform 8-region deployment"
  bridge:
    - "bft-consensus-to-sharded-ledgers"
    - "database-transactions-to-byzantine-sharded-ledgers"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-ahl-sharding"
source_refs:
  - "arxiv:1804.00399v4"
  - "sha256:df3115daf1caee12dff1b156a2a4d18c182641b9ad267eba166a204bc18ded5f"
confidence: "high"
trust_tier: "primary"
primary_direction: "scaling-and-sharding"
secondary_directions:
  - "consensus"
  - "transaction-processing"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "The abstract and Section 3 frame the primary problem as sharding permissioned blockchain systems for general workloads."
  - "Sections 4-6 map the source to shard-level BFT, shard formation and cross-shard transaction coordination."
  - "Section 7 evaluates throughput scaling by committee size, shard count and network setting."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0040"
local_pdf: "~/Desktop/paper/AHL(1).pdf"
pdf_sha256: "df3115daf1caee12dff1b156a2a4d18c182641b9ad267eba166a204bc18ded5f"
extracted_text_path: "vault/02_Raw/pdf/extracted/towards-scaling-blockchain-systems-via-sharding-df3115daf1ca-pages.txt"
---

# Towards Scaling Blockchain Systems via Sharding

## 论文身份

- 标题: Towards Scaling Blockchain Systems via Sharding
- 作者: Hung Dang, Tien Tuan Anh Dinh, Dumitrel Loghin, Ee-Chien Chang, Qian Lin, Beng Chin Ooi
- 机构: National University of Singapore
- 会议/期刊: arXiv preprint in local metadata; venue not externally verified in this run
- 年份: 2019
- arXiv: 1804.00399v4
- DOI: unknown
- Canonical URL: https://arxiv.org/abs/1804.00399v4
- 本地 PDF: `~/Desktop/paper/AHL(1).pdf`
- PDF SHA-256: `df3115daf1caee12dff1b156a2a4d18c182641b9ad267eba166a204bc18ded5f`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf` via queue extraction.
- 页数: 16
- 已覆盖章节/页码: Abstract, 1 Introduction, 2 Preliminaries, 3 Overview, 4 Scaling Consensus Protocols, 5 Shard Formation, 6 Distributed Transactions, 7 Performance Evaluation, 8 Related Works, 9 Conclusions, Appendices A-C.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 图表坐标和公式有少量抽取噪声；正文、算法流程、表格数值和章节结构可读。SGX 实验使用 simulation mode 并注入实测 enclave 操作延迟，不能当作真实 SGX production benchmark。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 将数据库 sharding 方法迁移到 blockchain；用 TEE 加速 BFT、随机组片和跨片事务 | high | 主分类依据 |
| 1 Introduction / p1-p2 | 动机与挑战 | permissioned blockchain 要同时支持大规模节点、Visa 级吞吐和非 UTXO/general workload | high | 给出三类挑战 |
| 2 Preliminaries / p2-p3 | 背景 | 数据库 sharding、2PC/2PL、PBFT/Nakamoto consensus、TEE/SGX | high | 解释跨域 bridge |
| 3 Overview / p3-p4 | 系统与威胁模型 | N nodes, k committees, shard state partitions, partially synchronous network, adaptive but delayed corruption, TEE assumptions | high | 决定适用边界 |
| 4.1 / p5-p6 | AHL/AHL+/AHLR | 用 attested append-only memory 消除 equivocation；拆分消息队列、去掉 request broadcast、尝试 leader aggregation | high | BFT source extension |
| 4.2 / p6 | PoET+ | 用 SGX 随机采样减少竞争 leader 数量和 stale block rate，但性能/安全不如 AHL+ | medium | 非最终采用路线 |
| 5 / p6-p7 | Shard formation | TEE RandomnessBeacon、committee size 超几何概率、batch reconfiguration | high | sharded ledger 安全扩展 |
| 6 / p7-p10 | Distributed transactions | 分析 RapidChain/OmniLedger 局限；提出 BFT reference committee + 2PC/2PL | high | database transaction bridge |
| 7 / p10-p12 | Evaluation | BLOCKBENCH KVStore/Smallbank、本地 100 服务器、GCP 8 region；吞吐、组片、reconfiguration、sharding scaling | high | 性能边界 |
| 8-9 / p12-p13 | 相关工作与结论 | Chainspace、database storage/execution/off-chain scaling；总结超过 3,000 tps 的 GCP 结果 | medium | 领域定位 |
| Appendix A-C / p13-p16 | 补充 | rollback defenses、cross-shard transaction probability、PoET+/latency/view-change/cost breakdown | medium | 细节复核 |

## 结构化摘要

### 解决的问题

这篇论文处理的是 `permissioned blockchain sharding for general workloads`，不是只服务 UTXO cryptocurrency 的分片账本。作者认为数据库 sharding 的高吞吐思路不能直接搬到 blockchain，因为 blockchain 的 failure model 是 Byzantine，而传统分布式数据库通常是 crash failure。这个差异带来三个问题:

1. shard 内不能使用高性能 CFT consensus，必须让 BFT consensus 在较大 committee 中仍能保持吞吐。
2. validator/node 不能随意分到 shard，需要安全随机组片，避免某个 shard 被 Byzantine 节点控制。
3. 跨片事务不能依赖完全可信的 coordinator，需要在 coordinator 恶意或停摆时仍保持 atomicity、isolation 和 liveness。

论文的目标是面向 general blockchain applications，例如金融、供应链、医疗等，不局限于 UTXO payment ledger。

### 核心方法

论文把系统拆成三层:

1. `AHL+` shard-level consensus: 基于 Hyperledger Fabric PBFT，用 SGX 中的 attested append-only memory 防止 Byzantine nodes equivocate，使 `N = 2f + 1` 可容忍 `f` 个 non-equivocating Byzantine failures；再通过消息队列拆分和去掉 request broadcast 降低通信拥塞。
2. TEE shard formation: 每个节点的 `RandomnessBeacon` enclave 以 epoch 为输入，只能生成一次随机候选；节点在同步窗口后锁定最小随机值并据此做 node-to-committee assignment。更高 fault tolerance 使 25% adversarial power 下 committee size 可从 PBFT 约 600+ 降到约 80。
3. BFT reference committee for distributed transactions: 经典 2PC/2PL 负责 atomicity/isolation，但 coordinator 不是单点 client，而是一个运行 BFT SMR 的 reference committee `R`。`R` 执行 2PC coordinator state machine，tx-committees 执行 prepare/commit/abort。

### 创新点

- 将 `attested append-only memory` 引入 Hyperledger PBFT，形成 Attested HyperLedger/AHL，并进一步用工程和协议优化得到 AHL+。
- 把 TEE 随机性用于 shard formation，而不是使用更重的 distributed randomness protocol。
- 用 AHL+ 的 `f < n/2` non-equivocating Byzantine fault threshold 降低 shard committee size，从而提高每 shard 吞吐并增加同一网络规模下的 shard 数。
- 把数据库的 2PC/2PL 迁移到 Byzantine sharded ledger，但用 BFT reference committee 处理 malicious coordinator liveness 问题。
- 在 local cluster 和 GCP 8-region 设置下评估 sharded permissioned blockchain，而不是只在小规模或高 oversubscription 环境中展示。

### 主要限制

- 可信硬件假设很重: 每个节点都要有 TEE；TEE integrity、attestation、key generation、randomness、signature 被信任；confidentiality 采用 sealed-glass proof 风格，允许大部分 enclave 内存泄露但不泄露关键密码材料。
- SGX evaluation 不是在大规模真实 SGX 机器上运行，而是用 SGX SDK simulation mode 加上单机实测 operation latency 注入。
- 不考虑 denial-of-service attacks；adaptive corruption 需要时间生效。
- AHL+ 仍有 PBFT-like view change 和 `O(N^2)` 通信；AHLR 虽降到 leader aggregation，但 leader 容易成为瓶颈。
- 2PL concurrency control 可能无法充分利用 workload concurrency；作者明确把更高级 concurrency control 留作未来工作。
- 手动改 chaincode 支持 prepare/commit/abort，legacy application porting 成本仍高。
- Reference committee 可能成为跨片事务瓶颈，作者建议多实例扩展但未完整评估生产调度。

## 系统模型、威胁模型与目标

| 维度 | 内容 | Source anchor |
| --- | --- | --- |
| Network and shards | 全网 `N` nodes，被分成 `k` committees，每个 committee 有 `n << N` nodes 并维护 disjoint state partition | §3.3 / p4 |
| Network timing | 默认 partially synchronous；distributed randomness generation 使用同步窗口 `Delta` | §3.3, §5.1 |
| Byzantine fraction | 攻击者一次最多控制 `s` fraction of nodes，示例常用 25% | §3.3, §5.2 |
| Adaptive adversary | 可选择腐化 honest nodes，但腐化不是瞬时完成；不考虑 DoS | §3.3 |
| TEE model | 信任 enclave integrity、attestation、key generation、randomness 和 signature；大部分 confidentiality 不保证 | §3.3 |
| Workload goal | 支持 general workload，不只 UTXO cryptocurrency | §1, §3.1 |
| Performance goal | 网络规模接近 Bitcoin/Ethereum，吞吐接近 Visa average workloads | §1, §3.1 |

## AHL/AHL+ 细节

### AHL: non-equivocating Byzantine fault model

AHL 采用 Chun et al. 的 attested append-only memory 思路。每个 consensus message type 有独立 log，例如 pre-prepare、prepare、commit。节点发送消息前必须把 message digest append 到对应 TEE log，消息携带 enclave signature 作为 append proof；接收方只接受带有效 proof 的消息。

这个设计的关键不是把整个 consensus protocol 放进 enclave，而是只把小的 append-only log abstraction 放进去，从而降低 trusted code base。结果是 Byzantine node 不能对同一 log position 发出冲突消息，系统可以按 `N = 2f + 1` 的 non-equivocating Byzantine threshold 收集 `f + 1` prepare/commit messages。

### AHL+ 两个主要优化

| 优化 | 解决的问题 | 机制 | 边界 |
| --- | --- | --- | --- |
| Separate message queues | Hyperledger 把 consensus 和 request messages 放同一 queue，request flood 会导致 consensus messages dropped | 按 metadata 拆成 consensus channel 和 request channel | 工程优化，不改变 consensus message semantics |
| Remove request broadcast | PBFT spec 中 replica 收到 client request 后广播给所有节点，但 leader 后续还会 pre-prepare broadcast | 普通 replica 只把 request forward 给 leader | 协议级优化；依赖 leader 能收到 request |
| AHLR aggregation | 降低 normal-case communication from `O(N^2)` to `O(N)` | leader enclave 聚合 `f+1` signed messages 后发 quorum proof | 实验中 leader 成为 bottleneck，吞吐低于 AHL+ |

### Rollback 防御

Appendix A 讨论了 AHL+ enclave restart 后被喂 stale sealed log head 的 rollback attack。论文给出一种 recovery procedure: 重启 enclave 查询 peers 的 last checkpoint，估计一个上界 `HM`，在拿到 sequence number 不低于 `HM` 的 stable checkpoint 前不接受新的 append 操作。这个机制的目标是防止 enclave “忘记”已经处理过的 message sequence，从而恢复 equivocation 能力。

## PoET+ 为什么没有成为主路线

PoET+ 也是 TEE-assisted consensus，但属于 Nakamoto/leader election 路线。它先用 SGX 产生随机 `q`，只让 `q = 0` 的 wait certificate 有效，从而减少竞争出块的节点数和 stale block rate。论文在附录中报告 PoET+ 可将 stale block rate 从约 15% 降到约 3%，并有更高 throughput。

但 PoET+ 的安全仍受 network latency 影响，在 partially synchronous network 中 Byzantine threshold 可能低于 33%。相比之下，AHL+ 的 safety 不依赖网络同步假设，且论文实验显示 AHL+ 吞吐更高，因此最终 sharded blockchain 采用 AHL+。

## Shard Formation 与 Reconfiguration

### TEE RandomnessBeacon

每个 epoch 开始时，节点调用 `RandomnessBeacon(e)`。Enclave 用两次独立 `sgx_read_rand` 产生 `q` 和 `rnd`，只有 `q = 0` 时签发 `<e, rnd>` certificate。节点广播 certificate，等待 `Delta` 后锁定收到的最小 `rnd`，并用它计算 `[1:N]` 的随机排列，再切成 committees。

这个机制通过 “每 epoch 只能调用一次” 限制 selective abort/bias。Appendix A 进一步讨论了 restart attack: 对非 genesis epoch，enclave 初始化后需要等待 `Delta` 才能对输入 epoch 签发随机值，以缩小通过重启试探随机输出的窗口。

### Committee size

由于 committee assignment 相当于 without-replacement random sampling，论文用 hypergeometric distribution 计算一个 committee 中 Byzantine nodes 超过 fault threshold 的概率。关键结果:

| Consensus threshold | 25% adversarial power 下达到 `Pr <= 2^-20` 的 committee size | 影响 |
| --- | --- | --- |
| PBFT `f <= (n-1)/3` | 约 600+ nodes | committee 大，单 shard 吞吐低，shard 数少 |
| AHL+ `f <= (n-1)/2` | 约 80 nodes | committee 小，单 shard 吞吐高，同等 N 下可形成更多 shard |

### Batch reconfiguration

全量 swap 会导致每个 shard 同时停机、重新发现 peers 和同步 state。论文改为每个 committee 每次只让最多 `B` 个 nodes transition，`B` 常取 `log(n)`。安全上，new nodes swapped in 时可能短暂超过 Byzantine threshold，需要用 union bound 估计风险；liveness 上，如果 `B > f`，剩余节点可能无法形成 quorum。因此 `B` 是 safety/liveness/performance 的调参点。

## Distributed Transactions

### 为什么 RapidChain/OmniLedger 不够

RapidChain 的 UTXO split-transaction route 可以避开 distributed commit，但对 account-based/general transaction 会破坏 atomicity 和 isolation。例如一个交易要同时 debiting `acc1` 和 `acc3` 并 credit `acc2`，若其中一个 debit 子操作成功而另一个失败，就无法像 UTXO 那样自然回滚。

OmniLedger 的 client-driven lock/unlock protocol 对 UTXO payment ledger 有效，但如果 coordinator/client 恶意或永久假装 crash，其他人的资金或状态可能被无限期 locked。论文把这个问题明确归为 malicious coordinator 下的 liveness failure。

### Reference committee + 2PC/2PL

论文的解法是把传统数据库的 2PC/2PL 放到 Byzantine sharded ledger 中:

| 角色 | 传统 2PC | 本文协议 |
| --- | --- | --- |
| Coordinator | 一个 trusted/highly available coordinator | BFT reference committee `R` |
| Participants | 分布式数据库 partitions | tx-committees/shards |
| Phase 1 | prepare/vote | `R` 发送 `PrepareTx`，tx-committees 返回 `PrepareOK/PrepareNotOK` |
| Phase 2 | global commit/abort | `R` 进入 Committed/Aborted 后发送 `CommitTx/AbortTx` |
| Recovery logging | coordinator/participants logs | state already stored on blockchain |

Safety 来自 `R` 和 tx-committees 自身的 BFT safety，liveness 来自 `R` 在 partially synchronous network 下的 eventual availability。实现上，Smallbank 的 `sendPayment` 被拆成 `preparePayment`、`commitPayment`、`abortPayment`，并用 `L_acc` lock state 实现 2PL。

### 性能与工程边界

- Reference committee 参与时可能成为跨片吞吐 bottleneck；作者建议运行多个 `R` 实例。
- 当前 implementation 让 honest clients relay `R` 和 tx-committees 的消息以减少 normal-case cross-shard communication，但这不是安全前提。
- 需要手动 refactor chaincodes；未来应提供 sharding library、client library 或语言级自动 transformation。

## Evaluation

| 实验 | 设置 | 结果/观察 | 解释 |
| --- | --- | --- | --- |
| AHL+ vs HL/AHL/AHLR | KVStore, local cluster and GCP, varying N | HL/AHL 大规模下 livelock；AHL+ 和 AHLR 保持吞吐，AHL+ 通常高于 AHLR | 队列拆分和去 request broadcast 比 leader aggregation 更稳 |
| Byzantine behavior | Byzantine nodes 发 conflicting sequence numbers | 本地 cluster 上 AHL+ 仍优于其他协议；GCP 跨 zone 下所有协议受影响严重 | WAN latency + view change 放大 failure cost |
| Shard formation | 与 OmniLedger RandHound 比较，N from 32 to 512 | TEE beacon 在 local/GCP 上分别最高约 32x/21x faster | 通信复杂度从 RandHound 的更高开销降到 `O(N log N)` 配置 |
| Reconfiguration | two shards, n up to 33, swap all vs swap `log(n)` | naive swap 有明显吞吐掉零和恢复期；batch swap 接近 no-reshard baseline | 分批 transition 维持 quorum |
| Local sharding | Smallbank/KVStore, f=1, up to 36 nodes | 吞吐随 shard 数近似线性；reference committee 会成为 bottleneck | general workload sharding 成立但 coordinator 需扩展 |
| GCP sharding | 972 nodes, 432 clients, 8 regions, Smallbank without reference committee | 12.5% adversary 下 36 shards 超过 3,000 tps；25% adversary 下约 954 tps | 较小 committee size 带来更多 shard 和吞吐 |

## 与现有 Nahida 知识的关系

| 目标节点 | 关系 | Source delta | 是否新建节点 |
| --- | --- | --- | --- |
| [[sharded-ledgers|Sharded ledgers]] | primary source extension | 补入 permissioned/general-workload sharding route: TEE-assisted BFT + TEE shard formation + BFT reference committee transactions | no |
| [[scaling-and-sharding|Scaling and sharding]] | direction source extension | 说明 blockchain scaling 不只 UTXO/payment ledger，也包括 account/key-value general workload and chaincode refactoring | no |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | secondary source extension | AHL+ 展示 non-equivocating Byzantine model 如何提高 fault threshold 并服务 shard committee sizing | no |
| [[bft-consensus-to-sharded-ledgers|BFT consensus -> sharded ledgers]] | bridge evidence | 增加 TEE-assisted BFT、committee size 和 shard formation 的 transfer/boundary evidence | no |
| [[database-transactions-to-byzantine-sharded-ledgers|Database transaction protocols -> Byzantine sharded ledgers]] | bridge evidence | 增加 2PC/2PL + BFT reference committee route，区别于 ByShard/RingBFT 的 orchestration/topology route | no |

## Cold-Start Hierarchy Discovery

| Facet | Result | Evidence | Confidence | Durable handling |
| --- | --- | --- | --- | --- |
| Research field/domain | blockchain-systems; distributed-systems | title, abstract, Sections 1-3 | high | primary blockchain systems |
| Research background | database sharding, BFT consensus, TEE/SGX, distributed transactions | Sections 2-3 | high | update bridges rather than create source-named nodes |
| Research problem | scaling permissioned blockchain systems via sharding for general workloads | Abstract, §3 goals | high | source extension under [[sharded-ledgers]] |
| Foundation concepts | sharded ledgers, BFT, 2PC/2PL, TEE-assisted consensus | §2, §4-§6 | high | no new foundation node; existing nodes updated |
| Method family | AHL+, TEE randomness beacon, batch reconfiguration, BFT reference committee | §4-§6 | high | method rows/source extension |
| Application/evaluation context | Hyperledger Fabric, BLOCKBENCH KVStore/Smallbank, GCP multi-region | §6.3, §7 | high | source-local details |
| Source instance | AHL / AHL+ paper | §4.1 and title | high | paper source instance, not upper-layer concept |

## Evidence Table

| Claim/Relation | Evidence anchor | Confidence | Notes |
| --- | --- | --- | --- |
| 本文 primary problem 是 permissioned/general-workload blockchain sharding | Abstract, §1, §3.1 | high | 区别于 UTXO-only sharding |
| TEE-assisted append-only logs eliminate equivocation and allow `N=2f+1` threshold | §4.1 | high | depends on TEE keys/signature/integrity |
| AHL+ 的两个优化主要解决 message dropping and redundant broadcast | §4.1, Fig. 10 | high | AHLR aggregation not chosen |
| TEE RandomnessBeacon accelerates secure shard formation | §5.1, §7.2 | high | synchronous `Delta` window required |
| Smaller committees arise from AHL+ threshold and hypergeometric sizing | §5.2 | high | 25% adversary example: about 80 nodes vs 600+ |
| BFT reference committee adapts 2PC/2PL to malicious coordinator setting | §6.2, Fig. 5-7 | high | reference committee may bottleneck |
| General workload support requires chaincode refactoring | §6.3-§6.4 | high | not automatic in current implementation |
| Over 3,000 tps result is tied to 12.5% adversary, no reference committee, GCP 8-region setup | §7.3 | high | not a universal production claim |

## Knowledge Handoff

- Primary path: `blockchain-systems/scaling-and-sharding/sharded-ledgers`.
- Secondary paths:
  - `distributed-systems/consensus/byzantine-fault-tolerance`
  - `distributed-systems/transaction-processing/distributed-transactions`
- Bridge updates:
  - `bft-consensus-to-sharded-ledgers`
  - `database-transactions-to-byzantine-sharded-ledgers`
- Review/future:
  - Compare AHL with Chainspace and later smart-contract sharding systems.
  - Decide whether `TEE-assisted BFT` deserves a method-family child node after more sources such as Hybrids on Steroids, MinBFT/TrInc or Coco.
  - Add distributed transaction foundation sources if future queries need 2PC/2PL detail independent of blockchain papers.

## 查询入口

- AHL/AHL+ 是什么，为什么不等同于 PBFT?
- AHL 为什么可以把 BFT fault threshold 从 `1/3` 推到 non-equivocating `1/2`?
- Towards Scaling Blockchain Systems via Sharding 如何处理 general workload?
- AHL 的 shard formation 怎么用 SGX randomness?
- 这篇和 OmniLedger/ByShard/RingBFT 的区别是什么?
- 2PC/2PL 如何迁移到 Byzantine sharded ledger?
- Reference committee 为什么解决 malicious coordinator blocking?
- 论文 3,000 tps 的实验前提是什么?

## 局限与待复核

| Gap | 为什么重要 | 后续动作 |
| --- | --- | --- |
| TEE-assisted BFT foundation 仍薄 | AHL 依赖 attested append-only memory 和 SGX assumptions，vault 还缺 Hybrids on Steroids/TrInc/MinBFT 等直接 sources | future `nahida-update` or `nahida-research-search` |
| General smart-contract sharding 对比不足 | Chainspace 只在 related work 中被讨论，后续 systems may use different object/contract model | continue queue or targeted search |
| Distributed transaction foundation 缺 source | 2PC/2PL 目前主要由 AHL/ByShard source 转述，缺数据库经典 source note | foundation search when queried |
| Production SGX validity 不完整 | 论文用 simulation mode + latency injection，不能代表真实 SGX multi-region deployment | keep limitation visible |
| Reference committee scaling 未完整解决 | 多 `R` 实例是建议，不是完整调度/负载均衡设计 | compare with ByShard/RingBFT later |
