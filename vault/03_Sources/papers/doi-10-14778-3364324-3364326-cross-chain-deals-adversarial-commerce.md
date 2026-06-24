---
id: "doi:10.14778/3364324.3364326"
title: "Cross-chain Deals and Adversarial Commerce"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
source_kind: "paper"
source_subtype: "academic_paper"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage: "full_text_pdf_extraction"
safe_for_absorption: true
identity_key: "doi:10.14778/3364324.3364326"
doi: "10.14778/3364324.3364326"
arxiv_id: "1905.09743v5"
canonical_url: "https://doi.org/10.14778/3364324.3364326"
local_pdf: "~/Desktop/paper/Cross-chain Deals and Adversarial Commerce.pdf"
pdf_sha256: "5cd2b932bcda88cf16afc46015957477cfb8f9b46cd4c3a187c9da80a313e9c0"
extracted_text_path: "vault/02_Raw/pdf/extracted/cross-chain-deals-and-adversarial-commerce-5cd2b932bcda-pages.txt"
pdf_pages: 14
authors:
  - "Maurice Herlihy"
  - "Barbara Liskov"
  - "Liuba Shrira"
venue: "Proceedings of the VLDB Endowment"
year: 2019
publication: "PVLDB 13(2):100-113"
domain_id: "blockchain-systems"
direction_id: "interoperability"
topic_ids:
  - "cross-chain-protocols"
  - "atomic-cross-chain-transactions"
  - "cross-chain-deals"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing/distributed-transactions"
classification_status: "refined_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Abstract and Section 1 define cross-chain deals as complex asset exchanges under adversarial commerce"
  - "Sections 2-4 replace classical atomicity with compliant-party acceptable payoff plus escrow/commit semantics"
  - "Sections 5-6 give timelock and certified-blockchain protocols for independent ledgers"
  - "Section 8 contrasts cross-chain swaps, atomic commitment across blockchains, sharded transactions and federated databases"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0063"
hierarchy_level: "source"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
  - "atomic-cross-chain-transactions"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "cross-chain-protocols"
  - "atomic-cross-chain-transactions"
  - "cross-chain-deals"
  - "adversarial-commerce"
  - "distributed-transactions"
aliases:
  - "Cross-chain Deals"
  - "Adversarial Commerce"
  - "CBC protocol"
  - "certified blockchain protocol"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "blockchain-systems/interoperability"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-cross-chain-deals"
source_refs:
  - "doi:10.14778/3364324.3364326"
confidence: "high"
trust_tier: "primary"
---

# Cross-chain Deals and Adversarial Commerce

## 论文身份

| Field | Value |
| --- | --- |
| Title | Cross-chain Deals and Adversarial Commerce |
| Authors | Maurice Herlihy; Barbara Liskov; Liuba Shrira |
| Venue | PVLDB 13(2):100-113, 2019 |
| DOI | `10.14778/3364324.3364326` |
| arXiv | `1905.09743v5` |
| Local PDF | `~/Desktop/paper/Cross-chain Deals and Adversarial Commerce.pdf` |
| SHA-256 | `5cd2b932bcda88cf16afc46015957477cfb8f9b46cd4c3a187c9da80a313e9c0` |

## 精读状态

- Reading depth: `deep_read_complete`.
- 覆盖范围: 全文 14 页，包含 problem framing、deal model、timelock protocol、CBC protocol、cross-chain proofs、gas/time cost analysis、related work 和 conclusion。
- 抽取质量: 文本抽取可用，页面边界完整。公式和伪代码有少量排版噪声，但不影响机制重建。
- Absorption decision: 作为 [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] 的 source extension 吸收；不新建同名 `Cross-chain Deals` 知识节点，因为当前只有一篇直接 source，且 reusable 层是跨链原子交易/对抗性商务下的安全与活性语义。

## 章节地图

| Section/Page | 内容 | 记忆锚点 |
| --- | --- | --- |
| p1-p2, Section 1 | 引入 adversarial commerce；说明经典 ACID 原子性、隔离性和 crash-only 假设不适合互不信任的自治参与者；列出贡献。 | correctness replacement; deal abstraction |
| p2-p3, Sections 1.1-1.4 | 系统模型、其他方案和 Alice/Bob/Carol ticket broker 示例；指出 cross-chain swaps 不能表达 broker、auction、arbitrage 等多步业务逻辑。 | expressive power |
| p3-p4, Section 2 | 定义 payoff matrix、compliant/deviating parties、acceptable payoff、安全性和两级 liveness。 | Properties 1-3 |
| p4-p5, Sections 3-4 | 定义多条独立区块链、被动合约、主动参与者、escrow、tentative transfer、clearing/escrow/transfer/validation/commit 五阶段。 | escrow as concurrency control |
| p5-p7, Section 5 | Timelock protocol：用 path signatures 和路径长度相关 timeout 传播 commit votes；强连通 deal graph 支撑去中心化转发。 | synchronous decentralized route |
| p7-p9, Section 6 | CBC protocol：用 certified blockchain 作为共享日志，记录 commit/abort votes，并向各资产链合约提供 commit/abort proof；半同步下去中心化不可得。 | semi-synchronous global-ledger route |
| p9-p12, Section 7 | 成本分析：timelock commit 约 `O(mn^2)` signature verification；CBC/BFT route 约 `O(m(f+1))` signature verification；时间成本随同步模型不同。 | cost tradeoff |
| p11-p12, Sections 8-10 | 对比 cross-chain swaps、Atomic Commitment Across Blockchains、state channels、sharded blockchains、BAR、oracles、federated databases；总结 adversarial commerce。 | related work boundary |

## 一句话贡献

这篇论文把跨链资产交换从“简单 atomic swap”提升为“cross-chain deal”抽象：允许经纪、拍卖、套利等多步业务逻辑，并在参与者可任意偏离协议的 adversarial commerce 模型下，用 compliant-party acceptable payoff、escrow liveness 和两类 commit protocol 替代经典 atomic transaction 的 all-or-nothing 语义。

## 核心问题设定

论文的问题不是“如何更快交换两条链上的两个 token”，而是：

- 多个自治且互不信任的参与者，如何通过多条独立链上的合约完成复杂资产流转。
- 某些参与者可能任意偏离协议，不能假设 rational、altruistic、crash-only 或 Byzantine 数量上界。
- 合约是被动、公开、确定性且可信的；参与者是主动、自治且可能不诚实的。
- 合约不能直接读取其他链状态，跨链状态必须通过某种 proof 或共享 ledger 传入。
- 正确性要保证 compliant parties 不被坑，而不是保证所有全局结果都满足经典事务的 all-or-nothing。

## Deal 抽象

### Payoff matrix

一笔 deal 的最终资产流转用 matrix/table 表示：row 是某 party 交出的资产，column 是该 party 期望收到的资产。Alice/Bob/Carol 示例中：

- Bob 把 tickets 转给 Alice，期望从 Alice 收到 100 coins。
- Carol 把 101 coins 转给 Alice，期望从 Alice 收到 tickets。
- Alice 作为 broker，把 Carol 的 101 coins 中的 100 coins 给 Bob，并把 Bob 的 tickets 给 Carol，留下 1 coin commission。

这个例子不能用传统 cross-chain swap 表达，因为 Alice 在 deal 开始时并不拥有要转出的 tickets 或 100 coins。她的价值来自中介撮合和多步 relaying，而不是一开始就能承诺无条件转账。

### Acceptable payoff

论文不要求每个 compliant party 都得到精确的 `All` 或 `Nothing`。每个 party 至少接受：

- `All`: 所有约定 transfer 都发生。
- `Nothing`: 没有 transfer 发生。

但应用可以允许其他可接受 partial payoff。并且如果一个 payoff 已可接受，那么“收到更多 incoming assets”或“交出更少 outgoing assets”的 payoff 也应可接受。

### Compliant vs deviating

论文避免使用 classical faulty/non-faulty，而是使用：

- `compliant parties`: 选择遵循协议的参与者。
- `deviating parties`: 不遵循协议的参与者，无论其动机是否理性。

关键点是：不假设 deviating party 数量上界。这个设定比 BAR/BFT 类型模型更强地反映 adversarial commerce。

## 正确性语义

| Property | 论文含义 | 替代/修正的经典概念 |
| --- | --- | --- |
| Safety | 每次协议执行中，每个 compliant party 都得到自己可接受的 payoff。 | 替代 atomic transaction 的全局 all-or-nothing。 |
| Weak liveness | compliant party 的资产不会永远被 escrow。 | 避免恶意对手永久锁资产。 |
| Strong liveness | 如果所有 party 都 compliant 且愿意接受 proposed payoff，则所有 transfers 都发生。 | 仅在同步期可实现，受 FLP/异步不可决定性边界影响。 |

这组语义是本论文对知识库最重要的增量：跨链原子性不能只写成“所有链一起 commit 或 abort”，因为恶意参与者无法被强制遵守全局事务协议。可实现的安全目标应是保护遵循协议者的局部利益。

## Escrow 与状态机

论文把 deal 建模为资产 ownership 状态机：

- 每个资产一次只有一个 owner。
- Escrow 将资产所有权临时转给 deal/contract，同时记录 commit outcome owner `C(a)` 和 abort outcome owner `A(a)`。
- Tentative transfer 只改变 commit outcome map，不立即改变真实 ownership。
- Deal commit 时，`C` 中的 owner 成为真实 owner；deal abort 时，`A` 中的 owner 成为真实 owner。

Escrow 在这里承担类似 concurrency control 的角色：防止同一资产同时卖给多个 counterparties。与数据库 lock 的差别是，escrow 还必须与 adversarial commit protocol 结合，保证 compliant party 的资产不会被永久锁住或被错误释放。

## 五个执行阶段

| Phase | 作用 | 信任边界 |
| --- | --- | --- |
| Clearing | market-clearing service 广播参与者、拟议 transfers 和 deal 信息。 | 服务可中心化但不可信；每个 party 之后自行验证。 |
| Escrow | party 把 outgoing assets 放入 escrow contract。 | 合约必须确认 sender 是 owner 且属于 deal。 |
| Transfer | parties 执行 tentative ownership transfers。 | 只更新 commit outcome，不立即交割资产。 |
| Validation | 每个 party 检查 deal、incoming assets escrow 状态和 payoff 是否可接受。 | 应用语义判断留给各 party。 |
| Commit | party 投票 commit 或 abort，最终 release/refund escrowed assets。 | 核心难点是 adversarial commit protocol。 |

## Timelock Protocol

Timelock protocol 是 fully decentralized route，但依赖 synchronous model，即链状态传播时间有已知上界 `Delta`。

### 机制

- Clearing phase 设定 deal identifier `D`、party list `plist`、commit phase start time `t0` 和 timeout delay `Delta`。
- 每个 party 将 outgoing assets escrow 到对应链上。
- party 对 incoming assets 有经济动机发布 commit vote，对 outgoing assets 没有同等动机。
- 因此 vote 可以由其他有动机 party forward。
- 合约接受 `commit(D, v, p)`，其中 `v` 是 voter，`p` 是 path signature。
- 若 path signature 长度为 `|p|`，vote 必须在 `t0 + |p| * Delta` 前到达。
- 若到 `t0 + N * Delta` 未收到所有 parties 的 vote，escrow refund 给原 owner。

### 为什么需要 path-dependent timeout

固定每个 party 每条链的 timeout 会出现矛盾：Alice 可先在 coin chain 临近 timeout 投票，Carol 需要额外 `Delta` 才能把该 vote 转发到 ticket chain；反过来又要求 coin chain timeout 至少比 ticket chain 大 `Delta`。两个方向同时成立不可能。因此 timeout 必须依赖 vote 被转发的路径长度。

### Deal graph

论文把 deal 表示为 directed graph，顶点是 party，边是 transfer。若 graph 不是 strongly connected，就会有 free riders，其他参与者没有 incentive 执行 deal。强连通性也支持 vote 沿 transfer incentive 路径传播到所有 escrow contracts。

### 正确性与限制

- Safety: 如果 compliant party 的 outgoing asset 已释放，但 incoming asset 因某 vote 缺失而 timeout，将与该 party 会转发已见 vote 的行为矛盾。
- Weak liveness: compliant party 创建的 escrow 都有 finite timeout。
- Strong liveness: 在所有 party compliant 且 graph strongly connected 时，所有 commit votes 可按时传播到所有 contracts。
- 风险: `Delta` 过小会让 DoS 攻击使 compliant party 错过 claim window；需要 watchtowers 或足够保守的 timeout。
- 成本: commit phase 最坏 `O(mn^2)` signature verifications，加 `O(m)` writes；同步通信下 commit/abort 延迟 `O(n)Delta`。

## CBC Protocol

CBC protocol 是 semi-synchronous route。它放弃 fully decentralized，使用 certified blockchain (CBC) 作为所有 parties 共享的 commit/abort 日志。

### 机制

- 某个 party 在 CBC 上发布 `startDeal(D, plist)`；若有多个 start record，最早者有效。
- asset-chain escrow contract 记录 CBC start entry hash `h`。
- 每个 party 在 CBC 上发布 `commit(D, h, X)` 或 `abort(D, h, X)`。
- Proof of commit: 所有 party 的 commit vote 都在任何 abort vote 之前记录。
- Proof of abort: 某个 abort vote 在所有 commit vote 之前记录。
- party 将 CBC proof 提交给各资产链上的 escrow contract，由合约检查 proof 后 release/refund。

### 为什么半同步需要共享 ledger

论文给出 FLP 风格论证：如果所有 party compliant，且某资产链 commit/abort 会迫使所有链同结果，那么系统从 bivalent 进入 univalent 的 decisive step 必须有全局先后顺序。若 decisive commit step 和 decisive abort step 可发生在不同链上，就无法确定哪个先发生。因此 tolerates periods of asynchrony 的协议必须让所有 parties 在关键状态访问同一个 contract/ledger。

### Cross-chain proofs

CBC proof 的难点是资产链合约不能直接观察 CBC：

- 如果 CBC 基于 BFT consensus，blocks 可由 validators certificate 支撑。合约知道初始 validators 后，可检查 block/certificate sequence；优化方式是让 CBC validators 直接签发 deal state certificate。
- 如果 CBC 基于 PoW/Nakamoto consensus，缺少 finality。攻击者可能私下挖含 abort vote 的分叉，再公开合法 commit proof 获取 incoming assets，同时用私有 abort proof 阻止 outgoing assets。需要 confirmation blocks 和 value-dependent difficulty/confirmation policy 才能降低风险。

### 正确性与限制

- Safety: compliant parties 对 deal commit/abort 结果达成一致，不会出现诚实方被分裂执行坑害。
- Weak liveness: 被锁太久的 compliant party 可在 CBC 上 vote abort。
- Strong liveness: 同步期内所有 compliant party 先 commit，晚于足够等待时间才 abort。
- 成本: BFT CBC route 约 `O(m(f+1))` signature verifications 加 `O(m)` writes；commit delay 在同步网络下约 `O(1)Delta`，abort 依赖 per-party timeout。
- 风险: CBC 是共享白板，可能成为 DoS 或 censorship 目标；BFT finality 较适合 proof，PoW proof 慢且复杂。

## 与 cross-chain swaps 的边界

Cross-chain swaps 是 deals 的特殊情形，但表达能力弱得多。论文列举无法表达的常见商业模式：

- broker: Alice 在 deal 开始时不拥有 Bob 的 tickets 或 Carol 的 coins，不能提前无条件转账。
- currency conversion as subdeal: Carol 不想在主 deal 失败后持有额外 coins。
- auction: outcome 取决于 bids 与 reserve price，不能在开始时静态写死 unconditional transfers。
- arbitrage: Alice 先低价买入再高价卖出，资产取得和转出之间有顺序依赖。

这意味着知识库里应把 `cross-chain deals` 作为 atomic cross-chain transactions 的方法/应用扩展，而不是把所有跨链原子性都压成 HTLC atomic swaps。

## 与经典分布式事务的关系

论文明确说 deals 受 classical atomic transactions 启发，但不是 atomic transactions：

- transactions 解决复杂分布式 state changes，deals 解决自治参与者之间的资产 exchange。
- transactions 的 correctness 通常要求 global all-or-nothing；deals 的 correctness 是每个 compliant party 得到 acceptable payoff。
- transactions 常假设 crash failures 或可信参与者；deals 必须容忍任意数量 parties 偏离协议。
- transactions 的 isolation 可用 serializability/snapshot consistency；deals 的 non-interference 更接近 double-spending prevention。

因此它强化了 [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] bridge：可迁移的是 commit/abort、escrow/lock、proof/log 的结构；不可迁移的是 trusted coordinator、crash-only fault model 和全局事务语义。

## 与 Atomic Commitment Across Blockchains 的关系

Atomic Commitment Across Blockchains 关注把 AC2T/AC3 的 all-or-nothing redeem/refund decision 交给 witness network。本文则从 adversarial commerce 的 problem semantics 出发，指出全局 all-or-nothing 在恶意 party 存在时并非可实现正确性目标，必须以 compliant-party acceptable payoff 替代。

两篇论文互补：

- Atomic Commitment 提供 witness-network atomic commitment/evidence-validation route。
- Cross-chain Deals 提供 deal abstraction、安全/活性语义、timelock 与 CBC 的 timing/decentralization tradeoff。
- 两者共同说明跨链原子性不能只由 HTLC preimage 或 bridge verification 处理，而需要单独的 [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] 节点。

## 成本与取舍

| 维度 | Timelock protocol | CBC protocol |
| --- | --- | --- |
| Communication model | synchronous | semi-synchronous |
| Decentralization | fully decentralized, no single chain accessed by all compliant parties | requires globally shared certified blockchain |
| Commit evidence | path signatures propagated across escrow contracts | CBC commit/abort proof or status certificate |
| Signature verification cost | worst-case `O(mn^2)` | BFT CBC `O(m(f+1))`, plus reconfiguration proof if needed |
| Time cost | commit/abort `O(n)Delta` | commit `O(1)Delta`; abort per-party timeout |
| Main risk | timeout/DoS/watchtower sensitivity | CBC DoS/censorship; PoW finality/proof ambiguity |

## 复用价值

这篇 source 向知识库贡献三类可复用结构：

- Correctness vocabulary: compliant/deviating、acceptable payoff、safety、weak liveness、strong liveness。
- Protocol family: synchronous timelock path-signature route 和 semi-synchronous CBC/global-ledger proof route。
- Bridge boundary: distributed transactions 只迁移 coordination skeleton，不迁移 crash-only all-or-nothing semantics。

## 局限

- 论文给的是理论/协议和 gas/time 成本模型，没有生产系统实测。
- 合约伪代码是说明性草图，不是完整实现。
- CBC route 的安全性强依赖底层 CBC finality、validator set/reconfiguration proof 和 censorship resistance。
- Timelock route 的安全性强依赖 `Delta` 设置、观察/转发能力和 DoS countermeasures。
- 经济激励只在 discussion 中简要提到，deposit/slashing/mechanism design 不是本文主体。

## 知识库吸收

| Target | Action | Reason |
| --- | --- | --- |
| [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] | refresh | 增加 deal safety/liveness 语义、timelock route、CBC route 和 cross-chain swaps 表达能力边界。 |
| [[cross-chain-protocols|Cross-chain protocols]] | refresh | 把 cross-chain deals 作为跨链协议中的复杂资产交换 route。 |
| [[interoperability|Blockchain interoperability]] | refresh | 标记互操作方向已补 deal-based safety/liveness source。 |
| [[distributed-transactions|Distributed transactions]] | refresh | 增加 adversarial-commerce adaptation，说明 all-or-nothing 不可直接迁移。 |
| [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] | strengthen | 明确迁移边界：commit skeleton 可迁移，correctness/failure model 需要重写。 |

## 关系抽取

| From | Relation | To | Evidence | Status |
| --- | --- | --- | --- | --- |
| `doi:10.14778/3364324.3364326` | evidenced_by | [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] | Sections 1-7 | active_seed |
| `cross-chain deals` | is_a | `atomic-cross-chain-transactions` | Sections 1-2 define deals as adversarial asset-exchange abstraction | source_extension |
| `timelock cross-chain deal protocol` | method_for | `atomic-cross-chain-transactions` | Section 5 | active_seed |
| `certified blockchain protocol` | method_for | `atomic-cross-chain-transactions` | Section 6 | active_seed |
| `distributed transactions` | bridges_to | `atomic-cross-chain-transactions` | Sections 1, 2, 4, 8 | active_seed |

## 后续队列

- Universal atomic swap / Herlihy PODC 2018 可作为 HTLC graph route 的直接 source。
- Production IBC/relayer/bridge sources 仍需补充，以验证 deal/CBC/witness routes 在真实 finality、relayer incentive 和 heterogeneous chain proof 下的边界。
- 经典 atomic commit/2PC foundation source 仍应补，以让 distributed-transactions 节点不只依赖 blockchain adaptation evidence。
