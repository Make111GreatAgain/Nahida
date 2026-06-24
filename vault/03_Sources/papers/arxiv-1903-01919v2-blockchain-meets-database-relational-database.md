---
id: "arxiv:1903.01919v2"
title: "Blockchain Meets Database: Design and Implementation of a Blockchain Relational Database"
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
  - "p2-p3 blockchain/database feature comparison and design motivation"
  - "p3-p5 key components and Serializable Snapshot Isolation background"
  - "p5-p8 order-then-execute and execute-order-in-parallel transaction flows"
  - "p8-p10 security, recovery, bootstrapping, and PostgreSQL implementation overview"
  - "p10-p12 PostgreSQL components, block-height SSI, ordering service, and transaction flow"
  - "p12-p14 performance evaluation"
  - "p14-p17 related work, future work, conclusion, references, and appendix"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/1903.01919"
doi: ""
arxiv_id: "1903.01919v2"
venue: "arXiv preprint"
year: "2019"
pdf_pages: 17
pdf_sha256: "ad2a281e79dbed6c104a89dd1ec7d270b2852fe8c5aaf8936734e6e514a950e8"
local_pdf: "~/Desktop/paper/1903.01919.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/1903.01919-ad2a281e79db-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
topic_ids:
  - "transaction-processing"
  - "blockchain-relational-databases"
  - "serializable-snapshot-isolation"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing/arxiv-1903-01919v2"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing/arxiv-1903-01919v2"
  - "distributed-systems/data-management-and-storage/arxiv-1903-01919v2"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "execution-and-transactions"
    - "transaction-processing"
    - "data-management-and-storage"
  topics:
    - "transaction-processing"
    - "blockchain-relational-databases"
    - "serializable-snapshot-isolation"
    - "provenance-queries"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "blockchain relational database"
  - "permissioned blockchain"
  - "transaction processing"
  - "serializable snapshot isolation"
  - "block height snapshot isolation"
  - "PostgreSQL"
  - "provenance queries"
aliases:
  - "Blockchain relational database"
  - "Blockchain Meets Database"
  - "block-height SSI"
  - "execute-order-in-parallel"
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
    - "data-management-and-storage"
  problem:
    - "decentralized replicated relational database among mutually distrustful organizations"
    - "same serializable commit order across untrusted database replicas"
    - "parallel transaction execution respecting consensus block order"
    - "rich SQL smart contracts and provenance queries in permissioned blockchains"
  method_family:
    - "order-then-execute with SSI"
    - "execute-and-order-in-parallel"
    - "SSI based on block height"
    - "block-aware abort during commit"
    - "PostgreSQL-backed blockchain execution"
  system_layer:
    - "database peer node"
    - "ordering service"
    - "communication middleware"
    - "block processor"
    - "ledger table"
    - "serializable snapshot isolation"
  evaluation_context:
    - "PostgreSQL prototype"
    - "Kafka/ZooKeeper CFT ordering"
    - "BFT-SMaRt ordering"
    - "LAN and WAN deployment"
    - "simple inserts, joins, aggregates, group-by smart contracts"
  application:
    - "enterprise permissioned blockchain"
    - "financial compliance"
    - "supply-chain provenance"
  bridge:
    - "database transaction processing to blockchain execution"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-blockchain-meets-database"
source_refs:
  - "arxiv:1903.01919"
  - "arxiv:1903.01919v2"
  - "pdf:~/Desktop/paper/1903.01919.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> execution-and-transactions"
secondary_directions:
  - "distributed-systems -> transaction-processing"
  - "distributed-systems -> data-management-and-storage"
classification_status: "corrected"
classification_confidence: "high"
classification_evidence:
  - "abstract explicitly targets decentralized replicated relational database with blockchain properties"
  - "Sections 3-4 define transaction execution/commit protocols and PostgreSQL SSI modifications"
  - "evaluation studies transaction throughput/latency for SQL smart contracts"
  - "queue path corrected from blockchain-systems/consensus/consensus-foundations to blockchain-systems/execution-and-transactions/transaction-processing"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0057"
queue_status: "absorbed"
---

# Blockchain Meets Database: Design and Implementation of a Blockchain Relational Database

## 论文身份

- 标题: Blockchain Meets Database: Design and Implementation of a Blockchain Relational Database
- 作者: Senthil Nathan, Chander Govindarajan, Adarsh Saraf, Manish Sethi, Praveen Jayachandran
- 机构: IBM Research India; IBM Industry Platforms USA
- 年份: 2019
- arXiv: `1903.01919v2`
- 本地 PDF: `~/Desktop/paper/1903.01919.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/1903.01919-ad2a281e79db-pages.txt`
- SHA-256: `ad2a281e79dbed6c104a89dd1ec7d270b2852fe8c5aaf8936734e6e514a950e8`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 17
- 已覆盖章节/页码: Abstract, Introduction, Motivation, Design, SSI background, order-then-execute, execute-and-order-in-parallel, security discussion, recovery, bootstrapping, PostgreSQL implementation, evaluation, related work, future work, conclusion, appendix。
- Extraction gaps: 图表中的曲线数值只按正文和表格记录；附录图 9-11 的 SQL 图片未被完整文本化，但正文已解释 workload 类型。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | 提出 blockchain relational database；目标是让互不信任组织各自运行数据库副本，并通过共识决定交易提交顺序 | high |
| §2 / p2-p3 | 动机 | 将 smart contract、签名、ACL、不可变日志、复制、serializability、异步交易、provenance 与数据库特性逐项对齐 | high |
| §3.1-§3.2 / p3-p5 | 系统组件和 SSI 背景 | 客户端、数据库 peer、ordering service；回顾 SSI、rw/wr/ww 依赖和 abort during commit | high |
| §3.3 / p5-p6 | Order then Execute | 先共识排序 block，再在各数据库节点并行执行 block 内交易，最后按 block 内顺序串行 commit/abort | high |
| §3.4 / p6-p8 | Execute and Order in Parallel | 交易先在数据库节点按 snapshot-height 执行，同时 ordering service 排序；提出基于 block height 的 SSI 和 block-aware abort rule | high |
| §3.5-§3.7 / p8-p10 | 安全、恢复、网络启动 | 处理 invalid transaction、obscuration、withholding、Byzantine orderers、tampering、failure recovery、smart-contract deployment | medium |
| §4 / p9-p12 | PostgreSQL 实现 | 新增 middleware、block processor、TxMetadata、BlockProcessorMetadata、TxWriteSet、TxOrder、pgLedger、pgCerts、block-height row fields | high |
| §5 / p12-p14 | 评估 | simple/complex SQL smart contracts；execute-and-order-in-parallel 在 simple contract 中达到约 2700 tps；复杂 SQL 场景下收益更明显 | high |
| §6-§8 / p14-p15 | 相关工作与结论 | 对比 Bitcoin/Ethereum、Fabric、Composer、Corda、Veritas、BigchainDB；强调 rich relational features 与 decentralized trust 的组合 | medium |

## 一句话贡献

这篇论文把关系数据库从“区块链状态存储后端”提升为区块链执行 substrate：用 PostgreSQL 的 MVCC/SSI、存储过程、访问控制、历史版本和 SQL 查询能力，配合外部 ordering service，让互不信任的组织各自独立执行交易并提交出同一 serializable 顺序。

## 核心问题设定

传统数据库复制通常假设某个 master 或协调者可信，或者只处理 crash fault；许可链场景中的组织彼此已知但互不信任，不能让一个节点执行交易后把结果复制给其他节点。每个数据库副本都必须独立执行交易、独立验证提交结果，又必须得到相同的串行化顺序和相同的 ledger state。

论文将这个问题拆成两层:

- ordering layer: 共识只负责给 blocks of transactions 一个全局顺序，而不负责数据库内部的每个并发冲突。
- database execution layer: 每个节点用可确定重放的并发控制机制执行交易，保证提交结果尊重 consensus block order。

因此它不是一篇新的 consensus paper。它的持久贡献属于 [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]]，并与 [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] 形成 bridge。

## 方法与机制

### Blockchain relational database

论文定义的 blockchain relational database 是一个许可链式、去中心化复制的关系数据库。每个组织运行自己的 database peer node；peer 之间互不信任，但都维护同一份 ledger replica。Smart contract 对应受约束的 PL/SQL stored procedure，交易是 procedure invocation，客户端用证书签名交易以支持 authenticity 和 non-repudiation。

关系数据库提供的能力包括:

- roles/groups/ACL 作为链上访问控制基础。
- PL/SQL procedures 作为 smart contracts，但需要禁止 random、timestamp、sequence、system information 等非确定性能力。
- MVCC 历史版本和 ledger table 共同支持 provenance queries。
- SQL joins、aggregates、constraints、triggers、schema、complex data types 支持比常见 key-value state database 更强的应用表达力。

### Order then Execute

Order-then-execute 的交易流为: 客户端先把交易交给 ordering service，ordering service 周期性共识出 block 并原子广播给所有数据库节点。每个节点验证 block 后，将 block 追加到 block store，然后为 block 内每个合法交易分配执行线程。

关键点不是“按 block 顺序逐笔执行”，而是:

- block 内交易先并行执行。
- 每个线程执行完后先等待，不立即提交。
- block 内所有交易执行完后，block processor 按交易在 block 中出现的顺序逐个触发 commit/abort。
- SSI 使用 `abort during commit` 变体保证每个节点对冲突结构做同样判断。

这样做比 Ethereum 式顺序执行更并行，但仍保留共识顺序作为确定性边界。论文还处理 ww-dependency: 因 PostgreSQL 更新不是 in-place，可以让竞争写入先写不同版本，最后按共识顺序只保留先提交者，避免锁等待导致不同节点执行时序不一致。

### Execute and Order in Parallel

Execute-and-order-in-parallel 进一步把执行与排序重叠。客户端把交易提交给数据库节点，交易携带 `snapshot-height`；数据库节点认证后转发给其他 peers 和 ordering service，同时开始执行。Ordering service 并行形成 block；block 到达后，节点等待 block 内交易都执行完，缺失的交易由 middleware 补执行，然后进入 commit phase。

这个设计的核心难点是: 不同节点当前处理到的 block height 可能不同，同一交易在不同节点如果看到不同 committed state，就会破坏一致性。论文为此提出基于 block height 的 SSI。

### SSI based on block height

Block-height SSI 给每一行增加 `creator block number` 和 `deleter block number`。交易按自己声明的 `snapshot-height` 判断行可见性:

- 行的 creator 不大于 snapshot-height。
- 行没有 deleter，或 deleter 大于 snapshot-height。
- update/delete 通过保留旧版本、插入新版本或标记 deleter 来维护历史版本。

如果节点当前 block 已高于交易 snapshot-height，交易还必须检测 phantom/stale read:

- 若存在 creator 大于 snapshot-height 且当前可见的行满足谓词，说明出现 phantom read，交易 abort。
- 若 snapshot-height 之前可见的行后来被删除或更新，且仍满足相关谓词，说明 stale read，交易 abort。

为了降低 false positives，论文要求 predicate reads 通过索引访问；若没有可用索引，交易 abort。`SELECT * FROM table_name` 在 PL/SQL smart contract 中也不允许，因为它会遍历全表并扩大 phantom/stale 检测问题。

### Block-aware abort during commit

默认 SSI 的 abort during commit 只关心 nearConflict 和 farConflict。论文的 block-aware 变体还关心冲突交易是否在同一 block，以及它们在 block 中的先后顺序。

规则的直觉是:

- 若 nearConflict/farConflict 与当前交易在同一 block，则按 block 内共识顺序保留靠前交易、abort 靠后交易。
- 若 nearConflict 不在同一 block，则即使没有 farConflict，也要 abort nearConflict；否则某些节点可能把它看成 stale read，而另一些节点只看到 rw-dependency，导致提交集合不一致。

这使得 execute-and-order-in-parallel 能在本地执行时序不同的节点之间保持同样的 commit/abort 决策。

### PostgreSQL prototype

实现基于 PostgreSQL 10，新增约 4000 行 C 代码。新增或修改的核心组件:

- communication middleware: 在节点和 ordering service 之间转发交易/blocks，接收的 block 存入 `pgBlockstore`。
- block processor: 按 block 顺序执行 commit phase。
- `TxMetadata`: 记录交易全局 ID、本地 txid、backend pid、等待信号、最终状态。
- `BlockProcessorMetadata`: 保存 last committed block、current block，并用于后台 worker/backend 信号同步。
- `TxWriteSet`: 记录交易写集，用于写入 creator/deleter block number 和计算 block write-set hash。
- `TxOrder`: 支持 block-aware SSI 判断 near/far conflicts 是否在同一 block 以及相对顺序。
- `pgLedger`: 记录交易全局 ID、本地 txid、SQL/调用、客户端、block number、commit/abort status，用于 recovery 和 provenance。
- `pgCerts`: 保存链上用户证书。

Ordering service 可替换；论文实现了 Kafka/ZooKeeper 的 CFT ordering 和 BFT-SMaRt 的 BFT ordering。

## 实验与证据

| 维度 | 设置/结果 | 证据锚点 | Caveat |
| --- | --- | --- | --- |
| Simple contract | 单表插入；order-then-execute peak 约 1800 tps；execute-and-order-in-parallel peak 约 2700 tps | §5.1, Fig. 5 | checkpoint flow 尚未实现；高活跃 backend 造成共享内存争用 |
| Ethereum-style sequential baseline | 模拟 block 形成后逐笔执行，peak 约 800 tps | §5.1 | baseline 是作者系统内的顺序模式，不是完整 Ethereum 节点 |
| Complex join contract | execute-and-order-in-parallel 相比 order-then-execute 约 2x peak throughput；CPU 可打满 | §5.2, Fig. 6 | 合约 workload 是作者构造的 SQL smart contracts |
| Complex group contract | group-by/order-by/limit/aggregate 也能作为 smart contract 被执行 | §5.2, Fig. 7 | 附录 SQL 图未完整文本抽取 |
| WAN/multi-cloud | 跨四大洲部署时吞吐基本保持，平均 latency 增加约 100ms；因为单交易/单 block 数据量小 | §5.3, Fig. 8(a) | 大交易、大 block 或 gossip 优化未充分覆盖 |
| Ordering service scale | Kafka ordering 随 orderer nodes 增加影响小；BFT ordering 随节点数增加吞吐下降 | §5.3, Fig. 8(b) | 说明 ordering service 仍可成为瓶颈 |

## 相关工作边界

- Bitcoin/Ethereum: order-execute，但 block 内顺序执行，状态模型相对简单。
- Hyperledger Fabric: execute-then-order-validate；支持 parallel endorsement，但状态数据库通常是 LevelDB/CouchDB，SQL 智能合约能力有限。
- Corda: 更像 decentralized database，但交易不由所有节点并行独立执行，也没有传统意义上的 blockchain log。
- Veritas: 共享可验证表，但依赖中心化 trusted timestamp server，且节点被信任会正确执行和分享结果。
- BigchainDB: Tendermint + MongoDB，更接近区块链数据库目标，但主要支持资产/token，缺少智能合约和 SQL rich query。

## 限制与边界

- 本文目标是 permissioned blockchain，不处理开放网络的 Sybil resistance、permissionless incentives 或 validator assignment。
- Checkpoint flow 在实现中尚未完成；评估主要覆盖 transaction execution/commit path。
- Execute-and-order-in-parallel 不支持 blind updates，且 predicate reads 依赖索引，否则会 abort。
- 论文没有完整形式化证明 block-height SSI；安全讨论偏系统设计分析。
- 隐私/通道/channel、历史数据 pruning、gossip batching、atomic block commit 是 future work。
- 这篇论文不能当作经典数据库事务教材；它是 database transaction processing 在 blockchain trust model 下的强 source extension。

## Knowledge Handoff

| Candidate | Generality class | Target handling | Reason |
| --- | --- | --- | --- |
| Blockchain relational database | method_family / system pattern | source extension under [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]]; candidate child only after more sources | 当前主要由本文定义，先不单独建知识节点 |
| Order-then-execute with SSI | method route | add to blockchain transaction processing methods | 可复用到其他 permissioned blockchain execution systems |
| Execute-and-order-in-parallel | method route | add to blockchain transaction processing methods | 可复用为 execution/order overlap pattern |
| SSI based on block height | method detail | source note detail + method row; future bridge to concurrency control | 当前 source 强，但 vault 缺经典 SSI foundation |
| PostgreSQL-backed blockchain execution | implementation pattern | source note detail; data-management secondary path | 是实现 substrate，不单独变成上层概念 |
| Database transaction processing -> blockchain execution | bridge | create [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] | 本文直接把数据库事务/SSI/SQL 能力翻译到区块链执行层 |

## Relation Extraction

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| `arxiv:1903.01919v2` | instance_of | `blockchain-systems/execution-and-transactions/transaction-processing` | abstract, §3-§4 | high | active_seed |
| `arxiv:1903.01919v2` | bridges | `distributed-systems/transaction-processing -> blockchain-systems/execution-and-transactions/transaction-processing` | §2-§4 | high | active_seed |
| `order-then-execute with SSI` | solves | same serializable commit order after consensus block ordering | §3.3 | high | source_extension |
| `execute-and-order-in-parallel` | solves | overlapping transaction execution with decentralized block ordering | §3.4 | high | source_extension |
| `SSI based on block height` | specializes | Serializable Snapshot Isolation for blockchain block-height snapshots | §3.4.1, §4.3 | high | source_extension |
| `pgLedger provenance queries` | enables | relational audit queries over blockchain history | §4.2, Table 3 | medium | source_extension |

## 吸收决策

- Queue 原分类为 `blockchain-systems/consensus/consensus-foundations`，精读后修正为 `blockchain-systems/execution-and-transactions/transaction-processing`。
- 作为 secondary path 传播到 `distributed-systems/transaction-processing`，因为论文的核心迁移对象是 SSI/MVCC/PLSQL/transaction processing。
- 作为 weak secondary context 传播到 `distributed-systems/data-management-and-storage`，因为它展示关系数据库能力、历史版本和 provenance queries 如何服务区块链，但不是 storage-engine 论文。
- 新增 bridge: [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]]。
