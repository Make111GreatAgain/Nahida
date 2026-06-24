---
id: "arxiv:1905.02847v2"
title: "Atomic Commitment Across Blockchains"
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
  - "p1 abstract, problem statement, hashlock/timelock failure motivation"
  - "p1-p4 open blockchain model, data model, transaction model"
  - "p4-p6 Atomic Cross-Chain Transaction model and atomicity/commitment definitions"
  - "p6-p12 AC3 protocol design: smart contracts, trusted witness, witness-network variant"
  - "p12-p14 cross-chain evidence validation techniques"
  - "p14-p15 AC3WN atomicity proof, fork-probability argument, scalability argument"
  - "p15-p19 complex graph support, latency/cost/witness-network choice/throughput analysis"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/1905.02847v2"
doi: ""
arxiv_id: "1905.02847v2"
venue: "arXiv preprint"
year: "2019"
pdf_pages: 20
pdf_sha256: "7522c3321528931e1a7d465fc01914c17c9dbab30148e771dc1ec20d759ca981"
local_pdf: "~/Desktop/paper/atomic commitment.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/atomic-commitment-7522c3321528-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "interoperability"
topic_ids:
  - "cross-chain-protocols"
  - "atomic-cross-chain-transactions"
  - "atomic-cross-chain-commitment"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
  - "atomic-cross-chain-transactions"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions/arxiv-1905-02847v2"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing/distributed-transactions"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "interoperability"
    - "transaction-processing"
  topics:
    - "cross-chain-protocols"
    - "atomic-cross-chain-transactions"
    - "distributed-transactions"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "atomic cross-chain transactions"
  - "atomic cross-chain commitment"
  - "cross-chain protocols"
  - "distributed transactions"
  - "witness network"
aliases:
  - "AC3"
  - "AC3WN"
  - "Atomic Cross-Chain Commitment"
  - "Atomic Cross-Chain Transaction"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "interoperability"
  problem:
    - "hashlock/timelock atomic swaps can violate all-or-nothing semantics when an honest participant crashes or the network is delayed before a timelock expires"
    - "centralized exchanges or centralized trusted witnesses reintroduce a trusted intermediary into cross-chain asset exchange"
    - "a cross-chain transaction graph may be cyclic or disconnected, making leader-based atomic swap protocols hard to apply"
    - "independent blockchains need a way to validate evidence about smart-contract publication and witness-network state without all miners fully replicating every chain"
  method_family:
    - "Atomic Cross-Chain Transaction graph model"
    - "smart-contract locks with mutually exclusive redeem/refund authorization"
    - "trusted-witness atomic commitment baseline"
    - "permissionless witness-network atomic commitment"
    - "cross-chain evidence validation through light clients or smart-contract header proofs"
  system_layer:
    - "source asset blockchains"
    - "witness blockchain or witness network"
    - "smart contracts controlling asset locks"
    - "miners/witnesses verifying publication and authorization evidence"
  evaluation_context:
    - "analytical comparison with Herlihy atomic swap protocol"
    - "latency changes from 2 * Delta * Diam(D) to 4 * Delta under the paper model"
    - "cost overhead is one additional witness smart contract deployment and one witness-state function call"
  bridge:
    - "distributed transactions -> atomic cross-chain transactions"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-atomic-cross-chain-transactions"
source_refs:
  - "arxiv:1905.02847"
  - "arxiv:1905.02847v2"
  - "pdf:~/Desktop/paper/atomic commitment.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> interoperability -> cross-chain-protocols -> atomic-cross-chain-transactions"
secondary_directions:
  - "distributed-systems -> transaction-processing -> distributed-transactions"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Abstract and Section 1 target cross-chain asset exchange and atomic all-or-nothing semantics"
  - "Sections 3-4 define Atomic Cross-Chain Transactions and AC3 witness protocols over multiple independent blockchains"
  - "Section 4.3 and Section 6 focus on cross-chain evidence validation, witness-network choice, latency and throughput"
  - "classification corrected from blockchain-systems/execution-and-transactions/transaction-processing to blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions; distributed transactions kept as secondary path"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0062"
queue_status: "absorbed"
---

# Atomic Commitment Across Blockchains

## 论文身份

- 标题: Atomic Commitment Across Blockchains
- 作者: Victor Zakhary, Divyakant Agrawal, Amr El Abbadi
- 机构: Department of Computer Science, University of California Santa Barbara
- 年份: 2019
- arXiv: `1905.02847v2`
- 本地 PDF: `~/Desktop/paper/atomic commitment.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/atomic-commitment-7522c3321528-pages.txt`
- SHA-256: `7522c3321528931e1a7d465fc01914c17c9dbab30148e771dc1ec20d759ca981`
- 备注: 本 note 只基于本地 PDF 精读；没有重新搜索网页或项目实现。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 20
- 已覆盖章节: Abstract, Introduction, Open Blockchain Models, Atomic Cross-Chain Transaction Model, AC3, AC3WN Analysis, Evaluation, Conclusion。
- Extraction gaps: PDF 元数据 title/author 为空；作者、日期和 arXiv 版本从第一页正文提取。抽取文本中公式和上标有少量空格错位，但不影响协议结构判断。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | HTLC/timelock 在 crash 或 network delay 下可能违反 all-or-nothing；目标是 decentralized AC3WN | high |
| §2 / p2-p4 | 开放区块链模型 | storage layer、end users、UTXO-like asset ownership、smart contract state/function model | medium |
| §3 / p4-p6 | 事务模型 | AC2T graph、sub-transactions、atomicity 与 commitment 定义 | high |
| §4.1 / p6-p8 | Trusted witness baseline | 用一个可信 Trent 对 `ms(D)` 只签 RD 或 RF，形成中心化 AC3TW | high |
| §4.2 / p8-p12 | Witness-network protocol | 用 witness smart contract `SCw` 的 `P -> RDauth/RFauth` 状态作为全局 commit/abort 授权 | high |
| §4.3 / p12-p14 | 跨链证据验证 | full replication/light node/contract-embedded header proof 三种验证方式 | high |
| §5 / p14-p15 | 正确性与扩展性 | 无 fork 时 atomic；有 negligible fork probability 时以 `1-epsilon` atomic；witness coordination 可并行化 | high |
| §6 / p15-p19 | 评估 | 与 Herlihy 比较 latency、成本、witness-network choice、throughput | high |

## 一句话贡献

这篇论文把传统 distributed transaction 的 atomic commit 问题翻译到多条独立区块链之间：用一个 permissionless witness network 的 smart contract 状态来决定所有链上锁定资产是统一 redeem 还是统一 refund，从而避免 HTLC/timelock 在 crash 或 delay 下的一边成交、一边退款风险。

## 核心问题设定

Atomic Cross-Chain Transaction，论文记为 AC2T，是一个跨多条区块链的分布式事务。它由一个有向图 `D = (V, E)` 描述：顶点是参与者，边是某条链上的资产转移 sub-transaction。每条边会部署一个智能合约锁住资产；全局目标是所有边都 redeemed，或所有边都 refunded。

论文指出，hashlock/timelock atomic swap 的核心弱点不只是“需要等待 timeout”。如果某个诚实参与者崩溃，或网络延迟使其在 timelock 到期前没有提交 redeem，那么已公开的 preimage 可能被另一方利用，而崩溃方只能错过 redeem 窗口，导致 all-or-nothing 被破坏。这个问题不能仅靠把 timeout 设长消除，因为更长 timeout 会直接增加延迟和资本锁定时间。

因此，本 source 的持久知识不应落成 `AC3WN` 这个协议名，而应落在 [[atomic-cross-chain-transactions|Atomic cross-chain transactions]]：多条互不信任区块链之间，怎样在无中心交易所、无可信 coordinator 的情况下实现 all-or-nothing asset movement。

## 模型与定义

### Open blockchain model

论文把开放区块链分成两层：

- Storage layer: permissionless miners 维护账本、验证交易、收取手续费。
- Application layer: end users 生成交易、部署或调用智能合约。

数据模型是 ownership-oriented：资产由公钥拥有，交易可以合并输入资产并拆分输出资产。智能合约被视为有状态对象，拥有 state attributes 和 functions；函数调用可以改变合约状态并转移资产。

### AC2T graph

AC2T 图中的每条边 `e = (u, v)` 包含资产 `e.a` 和目标链 `e.BC`，表示参与者 `u` 在链 `e.BC` 上向 `v` 转移资产。论文给出两个语义条件：

| 条件 | 含义 | 本文实现方式 |
| --- | --- | --- |
| Atomicity | AC2T 中不存在某些合约 redeemed、另一些合约 refunded 的最终状态。 | 全局 `RDauth` 与 `RFauth` 互斥。 |
| Commitment | 如果所有需要的 smart contracts 都正确发布，协议应允许全局 commit；否则应允许 abort/refund。 | witness network 验证所有 contracts 后授权 redeem；任一方拒绝发布时允许 refund。 |

### Smart contract template

每个资产锁定合约有三种状态：

- `P`: published，资产已锁定。
- `RD`: redeemed，资产转给 recipient。
- `RF`: refunded，资产退回 sender。

合约同时带有 redemption commitment scheme 和 refund commitment scheme。设计目标是让系统只能公开一种授权：一旦 redeem 被授权，就不能再 refund；一旦 refund 被授权，就不能再 redeem。

## 协议路线

### AC3TW: centralized trusted witness baseline

AC3TW 使用一个受信任见证人 Trent。参与者先对交易图 `D` 和 timestamp `t` 多签，得到 `ms(D)`。每个链上合约把 redeem/refund 条件绑定到 `ms(D)` 和 Trent 的公钥。Trent 对同一个 `ms(D)` 最多签署一种结果：

- `(ms(D), RD)`: 所有合约正确发布后，授权全局 redeem。
- `(ms(D), RF)`: 出现未发布/拒绝发布时，授权全局 refund。

这条路线说明 atomic commit 的结构可以跨链迁移，但也暴露了问题：可信见证人只是传统 coordinator 的中心化版本，违背 open blockchain 想避免 trusted intermediary 的目标。

### AC3WN: permissionless witness-network atomic commitment

AC3WN 用一条 permissionless witness blockchain 替代 Trent。参与者部署 witness smart contract `SCw`，它记录某个 `ms(D)` 对应 AC2T 的全局状态：

- `P`: pending。
- `RDauth`: redeem authorized。
- `RFauth`: refund authorized。

资产链上的每个锁定合约不直接接受 hash preimage，而是接受关于 `SCw` 状态的跨链证据：

- 如果能证明 `SCw` 已稳定进入 `RDauth`，该资产合约可以 redeem。
- 如果能证明 `SCw` 已稳定进入 `RFauth`，该资产合约可以 refund。

`SCw` 只允许从 `P` 转移到 `RDauth` 或 `RFauth`，不允许二次切换。fork 的风险通过等待 witness block buried under `d` blocks 来降低；论文用 Bitcoin 的 6-block confirmation 作为稳定区块例子，但 witness-network 的 `d` 需要根据攻击成本与资产价值设置。

## AC3WN 执行流程

| 步骤 | 操作 | 安全目的 |
| --- | --- | --- |
| 1 | 参与者构造 AC2T 图 `D`，多签 `(D, t)` 得到 `ms(D)`。 | 固定所有 sub-transactions 的 sender/recipient/asset/chain。 |
| 2 | 在 witness network 上部署并注册 `SCw`，状态为 `P`。 | 建立全局 commit/abort 决策点。 |
| 3 | 每个参与者在各自 asset blockchain 上并发发布锁定合约。 | 避免 Herlihy single-leader protocol 的顺序发布延迟。 |
| 4 | 若所有合约已正确发布，任一参与者向 witness network 请求 `P -> RDauth`，并附上所有发布证据。 | miners/witnesses 验证所有合约后授权 commit。 |
| 5 | 若有参与者拒绝发布，任一参与者请求 `P -> RFauth`。 | 只检查 `SCw` 当前仍为 `P`，然后授权 abort/refund。 |
| 6 | 参与者把稳定 witness block 作为证据提交到各 asset blockchains，统一 redeem 或统一 refund。 | 所有 asset contracts 读取同一全局授权结果。 |

## 跨链证据验证

论文讨论了三类让一条链验证另一条链状态的方式：

| 方式 | 核心思想 | 成本/边界 |
| --- | --- | --- |
| Full replication | 每条链的 miners 都维护其他链的完整副本。 | 最直接但不可扩展，处理、存储和网络成本过高。 |
| Light nodes | validators 维护其他链 block headers 和相关 Merkle branches。 | 比 full node 轻，但链数量增长后仍难扩展，且要求矿工基础设施改变。 |
| Smart-contract header proof | validator chain 上的合约保存 validated chain 的稳定区块头；参与者提交后续 header chain、PoW 验证和交易 inclusion evidence。 | 不要求 miners 运行其他链节点；验证逻辑和 gas/计算成本转移给合约开发者和调用者。 |

AC3WN 同时需要两类验证：witness network 验证各 asset-chain contracts 已发布且状态正确；asset blockchains 验证 `SCw` 已授权 `RDauth` 或 `RFauth`。

## 正确性与扩展性

论文的 atomicity 论证依赖 `SCw` 的互斥状态转移。

- 若 witness network 无 fork，则 `RDauth` 和 `RFauth` 不可能在同一线性历史中都成为有效状态。任何“一个合约 redeemed、另一个合约 refunded”的情况都意味着 `SCw` 同时或先后进入两个互斥状态，与合约状态机矛盾。
- 若 witness network 的深度 `d` fork 概率为 `epsilon`，则 AC3WN 以至少 `1 - epsilon` 的概率保持 atomicity。atomicity violation 只能来自 witness chain fork 中两个冲突状态都被不同 asset chains 接受。

扩展性论点是：不同 AC2Ts 的全局 atomicity 决策彼此独立，可以使用不同 witness networks 并行协调。若两个 AC2Ts 在某条 asset chain 的 sub-transaction 层冲突，该冲突由该 asset chain 的 miners 解决，而不是由 witness network 全局串行化。

## 评估与成本

| 维度 | AC3WN 结论 | 对比对象/边界 |
| --- | --- | --- |
| Latency | `4 * Delta`，包括 witness contract deployment、asset contracts 并发发布、witness state change、asset contracts 并发 redeem/refund。 | Herlihy single-leader atomic swap 为 `2 * Delta * Diam(D)`。 |
| Cost overhead | 比 Herlihy 多一个 witness smart contract deployment 和一次 witness state-change function call；若每个合约部署/调用费用相同，总费用从 `N * (fd + ffc)` 到 `(N + 1) * (fd + ffc)`。 | overhead 约为 Herlihy 费用的 `1/N`。论文用 Ethereum 当时价格估算类似 `SCw` 的部署约 $2；这是 2019 费率假设，不是当前价格。 |
| Witness-network choice | `d` 应满足攻击 `d` blocks 的 51% 成本高于可盗资产价值。论文给出 `d > Va * dh / Ch`。 | 示例: `Va = $1M`，Bitcoin `Ch = $300K/hour`，`dh = 6 blocks/hour`，需 `d > 20`。 |
| Throughput | 若固定 witness chain，吞吐受 involved chains 和 witness chain 中最慢者限制；若 witness 从参与链中选择，可避免额外 witness bottleneck。 | 表 1 给出当时 Bitcoin 7 tps、Ethereum 25 tps、Litecoin 56 tps、Bitcoin Cash 61 tps。 |
| Graph support | 支持 cyclic 和 disconnected AC2T graphs。 | Nolan/Herlihy leader-based protocols 对图结构有额外约束或需要多 leader 扩展。 |

## 与现有知识库的关系

| Knowledge target | 关系 | 处理方式 |
| --- | --- | --- |
| [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] | 本文建立 cross-chain atomicity problem 的强 source seed。 | 新建 child node，吸收 witness-network atomic commitment 路线。 |
| [[cross-chain-protocols|Cross-chain protocols]] | 本文把跨链协议中的 exchange/transfer atomicity 具体化为 AC2T/AC3。 | 更新父节点的方法族、source extension、bridge link。 |
| [[distributed-transactions|Distributed transactions]] | 本文直接复用 atomic commit 和 2PC 的问题结构，但改写了 trust model。 | 更新为 secondary evidence，并建立 bridge。 |
| [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] | 记录 atomic commit 结构如何跨到 adversarial independent ledgers。 | 新建 bridge，边界写清 witness network/finality/evidence validation。 |

## Source-only 细节

以下内容保留在 source note，不上升为知识节点：

- `AC2T`、`AC3`、`AC3TW`、`AC3WN` 这些论文命名。
- Algorithm 1/3/4 的具体函数名、状态变量名和伪代码结构。
- `ms(D)` 的多签细节、`SCw` 构造参数、`RDauth/RFauth` 的源内命名。
- 图 4、图 7 的 Alice/Bob、Bitcoin/Ethereum 示例。
- 2019 年具体 gas/美元估计和 top-4 cryptocurrency tps 表格，除非用于解释论文当时的评估边界。

## 知识增量

| Delta | Reusable placement | Notes |
| --- | --- | --- |
| Cross-chain atomicity 不能只依赖 timelock；crash/delay 会让诚实方错过 redeem 窗口。 | Atomic cross-chain transactions | 修正 HTLC-only 路线的风险边界。 |
| Atomic commit 的 commit/abort 结构可以迁移到跨链，但可信 coordinator 必须替换或去信任化。 | Distributed transactions -> atomic cross-chain transactions | AC3TW 是 baseline，AC3WN 是去中心化 route。 |
| Witness smart contract 的互斥状态可以作为所有 asset contracts 的统一授权源。 | Atomic cross-chain transactions | 可复用模式，不等于 AC3WN 专名节点。 |
| Cross-chain evidence validation 是跨链 atomicity 的系统依赖。 | Cross-chain protocols | 涉及 full replication、light nodes、contract header proofs。 |
| Witness-network safety depends on finality/fork depth and attack economics. | Atomic cross-chain transactions | `d` 不是固定常数，应随资产价值和 51% 攻击成本变化。 |

## 不足与后续

- 论文是 analytical/preprint 评估，没有真实多链部署实验。
- Witness-network 仍引入额外链和合约，具体 liveness、fee market、DoS 和 evidence-size 成本需要更多 source。
- 2019 年 gas 和 throughput 数字只可作为历史评估上下文。
- 需要与 Herlihy/Liskov/Shrira 的 cross-chain deals、universal atomic swaps、IBC/production bridge/finality 资料对照，判断 atomic cross-chain transactions 是否继续拆 child method families。

## 提取关系

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| `arxiv:1905.02847v2` | instance_of | `blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | source note; §3-§6 | high | active_seed |
| `Atomic Cross-Chain Commitment` | translates | `distributed transaction atomic commit` | §1, §3-§4 | high | source_extension |
| `witness-network smart contract state` | authorizes | `global redeem or refund decision` | §4.2 | high | source_extension |
| `RDauth/RFauth mutual exclusion` | enforces | `all-or-nothing cross-chain transaction outcome` | §4.2, §5.1 | high | source_extension |
| `cross-chain evidence validation` | depends_on | `validated-chain headers, inclusion proofs, or light-client/full-node state` | §4.3 | high | source_extension |

## 吸收决策

| Target | Decision | Reason |
| --- | --- | --- |
| Source note | create standalone paper source note | 论文自身贡献、协议、模型、评估足够完整。 |
| Knowledge node | create [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] | 这是跨链协议中可复用问题，已有 zkCross HTLC exchange seed，且后续队列还有 Cross-chain Deals。 |
| Bridge | create [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] | 论文显式把 2PC/atomic commitment 思路迁移到 independent blockchains。 |
| Queue path | correct from `blockchain-systems/execution-and-transactions/transaction-processing` to `blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | durable problem is cross-chain atomicity, not local blockchain execution pipeline. |
