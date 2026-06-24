---
id: "arxiv-1905.09274v4"
title: "LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts"
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
  - "p1-p2 abstract, introduction, contribution, outline"
  - "p2-p4 blockchain and sampling-based data availability background"
  - "p4-p5 threat model, node types, block model, goals"
  - "p5-p6 block validity rules and data availability definitions"
  - "p6-p10 application-layer model, cross-application calls, namespaced Merkle tree, DoS"
  - "p10-p13 implementation and evaluation"
  - "p13-p15 discussion, related work, conclusion, references"
canonical_url: "https://arxiv.org/abs/1905.09274v4"
doi: ""
arxiv_id: "1905.09274v4"
venue: "arXiv draft"
year: "2019"
local_pdf: "~/Desktop/paper/1905.09274v4.pdf"
sha256: "30fbf42d30c4db2eeea98843f9dc08e11078b78b2a837dfe03f3c0f6f6d1f879"
pages: 15
pdf_extractor: "pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
topic_ids:
  - "data-availability-sampling"
  - "client-side-smart-contracts"
  - "modular-blockchains"
ontology_path:
  - "blockchain-systems"
  - "data-availability-and-light-clients"
  - "data-availability-sampling"
primary_ontology_path: "blockchain-systems/data-availability-and-light-clients/data-availability-sampling/arxiv-1905.09274v4"
secondary_ontology_paths:
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers/arxiv-1905.09274v4"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
  directions:
    - "data-availability-and-light-clients"
    - "scaling-and-sharding"
  topics:
    - "data-availability-sampling"
    - "client-side-smart-contracts"
    - "modular-blockchains"
domains:
  - "blockchain-systems"
topics:
  - "data-availability-sampling"
  - "lazyledger"
  - "client-side-smart-contracts"
  - "namespaced-merkle-tree"
aliases:
  - "LazyLedger"
  - "data availability ledger"
  - "client-side smart contracts"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "data-availability"
  - "light-clients"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "data availability"
    - "light clients"
    - "modular blockchain"
  problem:
    - "decouple consensus from execution"
    - "probabilistic data availability verification"
    - "application-specific message retrieval"
  method_family:
    - "erasure-coded data availability sampling"
    - "namespaced Merkle tree"
    - "client-side execution"
  system_layer:
    - "ordering layer"
    - "data availability layer"
    - "application/client execution layer"
  evaluation_context:
    - "Golang prototype"
    - "currency/name registrar/petitions examples"
  application:
    - "base layer for client-side applications"
  bridge:
    - "data availability to sharded ledgers"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-lazyledger"
safe_for_absorption: true
source_refs:
  - "arxiv:1905.09274v4"
  - "sha256:30fbf42d30c4db2eeea98843f9dc08e11078b78b2a837dfe03f3c0f6f6d1f879"
  - "pdf:~/Desktop/paper/1905.09274v4.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "data-availability-and-light-clients"
secondary_directions:
  - "scaling-and-sharding"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract identify distributed data availability ledger"
  - "Section 4 reduces block validity to data availability"
  - "Section 5 builds client-side application model with namespaced Merkle trees"
taxonomy_version: "1.0"
---

# LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts

## 论文身份

- 标题: LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts
- 作者: Mustafa Al-Bassam
- 机构: University College London
- 会议/期刊: arXiv draft; local PDF says "This document is a draft; feedback is welcome."
- 年份: 2019
- DOI: unknown
- arXiv: `1905.09274v4`
- 链接: https://arxiv.org/abs/1905.09274v4
- 本地 PDF: `~/Desktop/paper/1905.09274v4.pdf`
- SHA-256: `30fbf42d30c4db2eeea98843f9dc08e11078b78b2a837dfe03f3c0f6f6d1f879`
- 代码: `https://github.com/musalbas/lazyledger-prototype` appears in p10 footnote.
- 数据/应用: prototype includes currency, name registrar, petitions/dummy-style examples; exact benchmark scripts not inspected.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 15
- 已覆盖章节/页码: Abstract, Sections 1-9, references
- 已检查附录: 本地 PDF 无附录
- 未覆盖章节/页码: none
- Extraction gaps: figures are understood from captions and nearby prose; DOI/venue not present; code repository URL recorded from footnote but repo content not inspected.
- 精读说明: 这是 modular blockchain / data availability design paper，重点读取了 threat model、block validity definitions, sampling cost model, namespaced Merkle tree, application semantics, evaluation graphs, limitations。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | LazyLedger 只排序并保证 transaction/message data availability，把执行/验证移到 interested clients | high | 核心范式转移 |
| §2 / p2-p4 | 背景 | full node/light client, data availability problem, erasure coding, random sampling, 2D coding/fraud proofs | high | DA sampling 前置 |
| §3 / p4-p5 | 模型 | consensus/storage/client nodes, honest storage node, bounded delay, block header/message model, four goals | high | 决定适用边界 |
| §4 / p5-p6 | Block validity | availability-only validity, soundness/agreement, simplistic O(n) rule, probabilistic O(sqrt(n)+log(sqrt(n))) rule | high | 主要理论/设计 claim |
| §5.1 / p6-p8 | Application model | namespace IDs, client-side execution, transition function cannot error, cross-application pre/post conditions | high | client-side smart contracts |
| §5.2 / p8-p10 | Namespaced Merkle tree | ordered Merkle tree with min/max namespace ranges; complete namespace proof; Theorem 3 | high | 核心数据结构 |
| §5.3 / p9-p10 | DoS and fees | invalid-message DoS, fee transactions as child-message dependency, max block size through nsHash rule | medium | sketch-level |
| §6 / p10-p13 | Implementation/evaluation | 2,865 LoC Go prototype, currency/name registrar/dummy apps, figures 3-7 | high | empirical workload-isolation evidence |
| §7 / p13 | Discussion | application light clients unclear; hard-fork consequences | high | limitation and governance implication |
| §8-§9 / p13-p14 | Related/conclusion | Mastercoin, sidechains, Chainspace, Fraud Proofs, DA base layer conclusion | medium-high | comparison needs direct sources later |

## 一句话贡献

LazyLedger 将区块链 base layer 重新定义为只负责 ordering and data availability 的消息层，把交易执行与状态验证移到应用客户端，并用 data availability sampling 与 namespaced Merkle trees 支撑轻量验证和按应用 namespace 检索。

## 核心精读笔记

### 背景、动机与问题边界

传统 blockchain/full node 模型要求验证节点下载、处理和验证每一笔交易，以判断区块是否符合 transaction validity rules。LazyLedger 认为这个模型是扩展性瓶颈之一：共识节点并不一定需要理解所有应用交易内容，核心共识功能只是给消息排序并保证消息数据可获得。

与 sharding 的“把状态分给不同共识组并行执行”不同，LazyLedger 更接近后来的 modular blockchain 思路：base layer 不执行应用状态机，只提供 ordered available data；应用用户只下载和执行自己关心 namespace 的消息。这让应用逻辑可用任意语言/环境实现，修改应用逻辑不需要 base chain hard fork。

### 模型、节点与目标

LazyLedger 区分三类节点:

- Consensus nodes: 决定哪些 blocks 加入链。
- Storage nodes: 存储链和 blocks 的完整数据。
- Client nodes: 应用用户，从 storage nodes 获取与自己应用相关的数据并执行应用状态。

网络假设包括 honest nodes 不被 eclipse attack 且至少连到一个 honest node；网络未分裂，任意两个 honest nodes 之间存在路径；至少有一个 honest storage node；并存在最大网络延迟 `delta`。Block model 中 header 包含 namespaced Merkle tree root `mRoot_i`，`blockValid(h)` 只检查 block data availability，而 `inChain` 的具体 PoW/PoS/longest-chain 规则不属于 LazyLedger 设计范围。

论文列出四个目标: availability-only block validity、application message retrieval partitioning、application message retrieval completeness、application state sovereignty。

### Block validity: 从交易正确性降到数据可用性

LazyLedger 的关键设计是让 `blockValid(h_i)` 只取决于构造 `mRoot_i` 所需数据是否可被网络获得，而不取决于消息是否满足某个应用状态机。这样 `inChain` 选择链时不再依赖交易内容执行。

论文给出两个 data availability 性质:

- Data Availability Soundness: 若 honest node 接受某 block available，则至少一个 honest storage node 已经或将在 `k * delta` 内获得 full block data。
- Data Availability Agreement: 若 honest node 接受某 block available，则所有 honest nodes 将在 `k * delta` 内接受该 block available。

它提供两种 validity rule:

1. Simplistic Validity Rule: 节点下载完整 `M_i`，验证 `root(M_i) = mRoot_i`，然后传播数据。带宽成本 `O(n)`，以 100% 概率满足 soundness/agreement。
2. Probabilistic Validity Rule: 使用 Al-Bassam et al. 的 erasure-coded random sampling。节点下载 row/column roots、固定数量 samples 和 Merkle proofs，在高概率下判断数据可用。论文写出带宽成本约 `O(sqrt(n) + log(sqrt(n)))`，并给例子: 4096 shares、2D Reed-Solomon 1/4 code rate 时，15 samples 约 0.4% block data 可给 99% availability guarantee。

这个设计产生一个重要扩展性直觉：传统 full node 增多不提升 on-chain throughput；LazyLedger 中若更多节点参与采样和传播，网络可安全支持更大的 blocks，更像 P2P file-sharing storage capacity 随节点数增加。

### Application model: client-side smart contracts

LazyLedger 的应用类似 smart contracts，但不是由 consensus participants 执行，而是由 end-user clients 执行。每条消息有 application namespace `ns(m)`；使用应用 `nid` 的客户端只关心所有 `ns(m) = nid` 的消息。

因为 base chain 允许任意消息，应用状态转移函数 `transition_nid(state, tx) = state'` 不能通过抛错让全局状态坏掉。若 `tx` 对该应用无效，transition 应返回旧状态。应用用户必须就 `transition_nid` 的逻辑达成一致；如果某用户采用不同逻辑，相当于本地进入另一个应用状态分支，不影响其他应用。

Application state sovereignty 是核心原则：应用 A 不能被第三方应用强迫下载/执行无关状态。跨应用调用只能通过显式 dependencies 表示。Pre-condition 需要依赖应用状态；post-condition 只有在被修改应用显式把调用应用设为 dependency 时才可直接成立，否则会迫使其用户下载不想要的应用状态。

### Namespaced Merkle tree: 按 namespace 完整检索

为了让 client 从 storage node 获取某 namespace 的完整消息集合，而不下载整个 block，LazyLedger 使用 namespaced Merkle tree。它是按 namespace 排序的 Merkle tree，每个非叶节点 hash 前缀包含其所有后代叶子的 minimum namespace 和 maximum namespace。

哈希格式为 `minNs || maxNs || hash(x)`。叶节点有 `minNs = maxNs = ns(x)`；内部节点从左右子树的 namespace range 合成。若左右子树排序错误，例如 `leftMaxNs >= rightMinNs`，则 hash 无效，导致无法构造有效 Merkle root。

Storage node 对 `query(hash(h_i), nid)` 返回该 namespace 的 Merkle proofs 和起始 index。Client 不仅验证每条 inclusion proof，还验证 proof set 左侧 siblings 的 max namespace 小于 `nid`、右侧 siblings 的 min namespace 大于 `nid`，从而检测是否有 namespace 内消息被遗漏。Theorem 3 证明在 Merkle tree 正确构造时，不完整 proof set 总能被检测到。

### DoS、费用和 block size

由于 consensus nodes 不验证应用交易，恶意客户端可向某 namespace 提交大量无效交易，迫使该应用客户端下载并过滤。论文讨论用 transaction fees 做优先级和 DoS 抑制，但强调 fee system 不应强迫原应用客户端也验证 fee currency application。方案是提交消息时附带 currency application 的 fee transaction，并把 child message hash 绑定到 fee；currency application clients/consensus nodes 验证 fee，原应用客户端不需要验证 fee 状态。

Maximum block size 可通过每条 message 最大大小和 `nsHash` 规则实现，避免节点下载整个 block 才知道是否超大。

### 实现与评估

论文实现了 2,865 行 Go prototype，并释放为开源项目。示例应用包括:

- Currency application: public keys 作为账户，签名交易更新余额。
- Name registration application: 依赖 currency app 充值，注册名称到 public key。
- Dummy application: 写入任意大小 key-value pairs 用于测试。

评估重点不是传统 TPS，而是客户端验证/检索成本:

- Figure 3: Simple Validity Rule 下载量随 block size 线性增长；Probabilistic Validity Rule 下载量次线性且接近 flat，因为 sample 数固定、Merkle proof size logarithmic、row/column roots 为 `2 sqrt(n)`。
- Figure 4: 查询 currency namespace 的 application proofs 时，无关 dummy transactions 总大小增加，proof size 只 logarithmic 增加。
- Figure 5: 当其他应用 state size 增加时，currency app 用户本地需存储的 state size 保持静态。
- Figure 6: 当 name registrar app 依赖 currency app，且其他 registrar 的 top-up transactions 增加时，相关用户必须下载 currency app proofs，因此 proof size 线性增加；这是 dependency 破坏隔离的极端情况。
- Figure 7: 当其他 registrar 增加的是 registration transactions 而非 dependency top-ups，相关用户 proof size 不线性增加。

### 限制与未来工作

作者明确指出 application light clients 不是显然可构建的：因为应用消息不由 consensus nodes 验证，客户端不能简单假设 honest majority 已验证应用状态。Hard fork 方面，LazyLedger 的 base layer 无 transaction-specific rules，因此应用升级/状态解释变化可以在应用客户端侧发生，而不需要 base chain hard fork；不升级的用户会本地解释出不同应用状态。

## 可复用想法

- Data availability 是 modular blockchain 中可从 execution validity 中剥离出来的底层职责。
- Namespace-aware authenticated data structures 可以把“完整检索某应用数据”变成可验证接口。
- 应用状态主权是扩展性与组合性之间的约束：dependency 会把另一个应用的负载带进来。
- Probabilistic DA sampling 的安全性依赖足够多节点采样并 gossip shares；这不是单客户端独立保证。
- Client-side smart contracts 降低 base layer 复杂度，但把应用 light client 和状态验证问题推到上层。

## 术语

| Term | 含义 | 来源 |
| --- | --- | --- |
| data availability problem | 只下载 header 的客户端如何确认 block data 未被 withheld | p3 |
| availability-only block validity | block validity 只关心 data availability，不执行交易状态机 | p5 |
| Probabilistic Validity Rule | erasure-coded random sampling 的 DA block validity rule | p6 |
| namespaced Merkle tree | 每个节点记录 namespace range 的 ordered Merkle tree | p8-p10 |
| application state sovereignty | 应用用户只执行自己应用及显式依赖应用的消息 | p5,p7-p8 |
| client-side smart contracts | 由 end-user clients 执行的应用逻辑，而非 consensus participants | p6-p7 |

## 连接

- 新方向: [[data-availability-and-light-clients|Data availability and light clients]]
- 新 topic: [[data-availability-sampling|Data availability sampling]]
- 概念: [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger]], [[data-availability-sampling|Namespaced Merkle trees]], [[data-availability-sampling|Application state sovereignty]]
- 桥: [[data-availability-to-sharded-ledgers|Data availability -> sharded ledgers]]
- 相邻已有: [[sharded-ledgers|Sharded ledgers]], [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger]]

## Evidence Table

| Claim | 位置 | 类型 | 证据强度 | 备注 |
| --- | --- | --- | --- | --- |
| LazyLedger decouples consensus ordering/data availability from application transaction execution | Abstract, p1-p2, p5 | design claim | high | core thesis |
| Block validity can be reduced to availability-only rules | §4, p5-p6 | mechanism/definition | high | includes soundness/agreement definitions |
| Probabilistic Validity Rule gives sub-linear block verification via DA sampling | §4.2, p6, Fig. 3 | mechanism/empirical | high | depends on enough network sampling |
| Namespaced Merkle tree supports complete namespace retrieval proofs | §5.2, p8-p10, Theorem 3 | data structure/theorem | high | assumes correct tree construction |
| Application state sovereignty prevents unrelated applications from imposing execution workload | §3.3, §5.1.1 p5,p7-p8 | design principle | high | dependency model |
| Prototype examples show unrelated application workload often does not significantly increase client workload | §6, Fig. 4-7 p11-p13 | empirical result | medium-high | dependency top-up case is negative result |
| Application light clients remain an open problem | §7 p13 | limitation | high | author-stated |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| LazyLedger leaves application light clients as an open problem because consensus nodes do not validate application messages, so clients cannot inherit application-state validity from consensus. | `arxiv:1905.09274v4#p13` | folded_into_meta_note |
| LazyLedger's application state sovereignty means clients execute only their application's messages and explicitly declared dependency applications, preventing unrelated applications from forcing extra state execution. | `arxiv:1905.09274v4#p5,p7-p8` | folded_into_meta_note |
| LazyLedger defines block validity so that a block is valid if the data behind its Merkle root is available, not if its messages satisfy an application state machine. | `arxiv:1905.09274v4#p5-p6` | folded_into_meta_note |
| LazyLedger makes the base blockchain responsible only for ordering and guaranteeing availability of transaction data, shifting transaction execution and validation to application clients. | `arxiv:1905.09274v4#p1-p2` | folded_into_meta_note |
| LazyLedger's probabilistic validity rule uses erasure-coded data availability sampling so nodes can gain high-probability block availability guarantees without downloading the whole block. | `arxiv:1905.09274v4#p3-p6,p11-p12` | folded_into_meta_note |
| LazyLedger's prototype evaluation shows that unrelated application data does not significantly increase a client's queried application state/proof workload, except when dependency applications carry shared workload such as registrar top-ups through a currency app. | `arxiv:1905.09274v4#p10-p13` | folded_into_meta_note |
| LazyLedger's namespaced Merkle tree lets clients verify that a storage node returned the complete set of messages for a namespace in a block. | `arxiv:1905.09274v4#p8-p10` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `[[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger decouples consensus from transaction execution]]`
- `[[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger block validity depends only on data availability]]`
- `[[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger probabilistic validity verifies availability with sub-linear sampling]]`
- `[[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|Namespaced Merkle trees prove complete namespace retrieval]]`
- `[[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger application state sovereignty limits cross-application workload]]`
- `[[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger prototype shows namespace workload isolation with dependency caveats]]`
- `[[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|Application light clients are an open problem for LazyLedger]]`

### Concepts to create or update

- Create [[data-availability-sampling|Data availability sampling]].
- Create [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger]].
- Create [[data-availability-sampling|Namespaced Merkle trees]].
- Create [[data-availability-sampling|Application state sovereignty]].
- Update domain map and bridge to [[sharded-ledgers|Sharded ledgers]].

### Maps and synthesis

- Create `vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md`.
- Create `vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/data-availability-sampling.md`.
- Create `vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/data-availability-sampling.md`.
- Create `vault/05_Bridges/data-availability-to-sharded-ledgers.md`.

### Review queue items

- Directly read Fraud Proofs / DA sampling source `[9]`; LazyLedger depends heavily on it.
- Inspect `musalbas/lazyledger-prototype` if implementation details become important.
- Modern Celestia/DA layer terminology should be calibrated by later sources, not inferred solely from this 2019 draft.

## Synthesis Handoff

LazyLedger should initialize `blockchain-systems/data-availability-and-light-clients/data-availability-sampling`. It is also a conceptual bridge from `sharded-ledgers` to modular DA: both seek scaling by avoiding global execution, but LazyLedger avoids execution in consensus rather than assigning execution to shards.
