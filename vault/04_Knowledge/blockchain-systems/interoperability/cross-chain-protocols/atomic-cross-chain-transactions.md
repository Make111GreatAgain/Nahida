---
id: "nahida-knowledge-atomic-cross-chain-transactions"
title: "Atomic cross-chain transactions"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "atomic-cross-chain-transactions"
domain_id: "blockchain-systems"
direction_id: "interoperability"
parent_knowledge_refs:
  - "nahida-knowledge-cross-chain-protocols"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
  - "atomic-cross-chain-transactions"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions"
secondary_ontology_paths:
  - "distributed-systems/transaction-processing/distributed-transactions"
relation_edges:
  - from: "nahida-knowledge-atomic-cross-chain-transactions"
    relation: "is_a"
    to: "nahida-knowledge-cross-chain-protocols"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-atomic-cross-chain-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-atomic-cross-chain-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-atomic-cross-chain-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    confidence: "medium"
    status: "supporting_seed"
  - from: "nahida-knowledge-atomic-cross-chain-transactions"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-atomic-cross-chain-transactions.md"
      - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
  - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
  - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
representative_source_refs:
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
query_keys:
  - "atomic cross-chain transactions"
  - "atomic cross-chain commitment"
  - "cross-chain atomic swap"
  - "cross-chain transaction atomicity"
  - "AC3"
  - "AC3WN"
  - "witness network atomic commitment"
  - "HTLC timelock crash failure"
  - "cross-chain deals"
  - "adversarial commerce"
  - "certified blockchain protocol"
  - "CBC protocol"
aliases:
  - "atomic cross-chain commitment"
  - "Atomic Cross-Chain Transaction"
  - "Atomic Cross-Chain Commitment"
  - "cross-chain deals"
  - "adversarial commerce"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "atomic-cross-chain-transactions"
  - "cross-chain-protocols"
  - "atomic-commit"
  - "distributed-transactions"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2019"
evidence_window_end: "2026-06-22"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-atomic-cross-chain-transactions"
  - "nahida-knowledge-20260622-cross-chain-deals"
source_refs:
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
confidence: "medium"
trust_tier: "primary"
---

# Atomic cross-chain transactions

## 定义与范围

- 定义: Atomic cross-chain transactions 研究多条独立区块链之间的资产转移、交换或复合交易如何共享可验证的 commit/refund/abort 结果，并让遵循协议的参与者得到可接受 payoff；在简单交换中它接近 all-or-nothing，在 adversarial commerce 中还必须处理 cross-chain deals 的局部安全性和 liveness。
- 不包含: `AC3WN`、`AC2T`、某个 hashlock 脚本、某个 witness contract 伪代码或某篇论文的图例；这些保留在 source note。
- Canonical terms: `atomic cross-chain transactions`, `atomic cross-chain commitment`.
- Retrieval role: 让查询能从 cross-chain protocols 进入跨链原子性问题，再按需打开 Atomic Commitment Across Blockchains、Cross-chain Deals 或 zkCross。
- Update scope: 新 source 涉及 atomic swaps、cross-chain deals、universal atomic swaps、witness ledgers、global ledgers、HTLC limitations 或 cross-chain transaction liveness/safety 时刷新。

## 背景

跨链交易的基础张力是：各条链独立排序、独立确认、独立处理合约状态，但用户想把多条链上的资产移动看成一个 logical transaction。传统 distributed transaction 的 atomic commit 提供了 commit/abort 问题结构，但 open blockchains 中参与者可恶意、链之间没有共同日志，传统 coordinator 或 2PC 信任模型不能直接迁移。

当前 vault 的直接证据来自 [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] 和 [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]]。前者把 AC2T 建模为跨链有向图，并用 witness network 的 `RDauth/RFauth` 互斥状态来协调所有链上的 redeem/refund；后者把跨链资产交换扩展成 adversarial commerce 下的 deal abstraction，要求 compliant party 得到 acceptable payoff、资产不被永久 escrow，并对比 synchronous timelock 与 semi-synchronous certified-blockchain route。[[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] 作为 supporting seed，说明 HTLC 可以支持 cross-chain exchange atomicity，但同一 preimage 会带来 linkability，且 HTLC 的 crash/timelock 边界需要更细的原子性节点承接。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它组织 HTLC atomic swaps、witness-network atomic commitment、cross-chain deals、global-ledger or witness-ledger protocols 等多类 future sources。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: `AC3WN` 是 source-specific route；本节点沉淀的是跨链原子性问题和方法族。
- 需要引用的更基础 Knowledge: [[cross-chain-protocols|Cross-chain protocols]]；相邻基础为 [[distributed-transactions|Distributed transactions]]。

## 解决的问题

在多条互不信任的区块链之间，如何让一个跨链交易的所有资产锁定、赎回和退款动作共享同一个 commit/abort 决策，并避免一部分链上成功、一部分链上失败的 split outcome。

关键子问题:

- crash 或 network delay 下，诚实参与者是否会错过 redeem/refund 窗口。
- 多条链如何验证对方链上的 contract publication、contract state 或 witness decision。
- 全局 commit/abort 决策由谁做，以及它的 trust、fork/finality、liveness 和成本边界是什么。
- 交易图是否可以是 cyclic、disconnected 或多方复杂图，而不是两方单交换。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[cross-chain-protocols|Cross-chain protocols]] | child_of | Atomic Commitment Across Blockchains creates reusable atomicity problem under cross-chain protocols | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| HTLC atomic swaps | method candidate | hashlock/timelock 是 atomic exchange 常见路线，但 privacy、timeout 和 crash 边界需要更多 source 对照 | zkCross; Atomic Commitment discussion of Nolan/Herlihy | review |
| witness-network atomic commitment | method candidate | 用 witness ledger/contract 作全局 commit/abort 授权源，是当前最强 source-backed route | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | source_extension |
| cross-chain deals | method/application section | deal abstraction 已补入本节点，当前作为 atomic cross-chain transactions 的 source extension 处理；若后续多篇来源围绕 adversarial commerce、auctions、brokerage 和 incentive design 展开，再考虑拆 child。 | [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals]] | source_extension |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| HTLC-based atomic exchange | 用 hash preimage 解锁两条链上的资产，并用 timelock 提供退款路径。 | 两方或较简单的跨链 exchange；链支持 hash/time locks。 | crash/network delay 会让诚实方错过窗口；同一 preimage 可能暴露 linkability；复杂交易图支持弱。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]]; [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment]] |
| Trusted witness atomic commitment | 一个可信见证人对同一 transaction graph 只签署 redeem 或 refund 中一种结果。 | 可以接受中心化 coordinator 或联盟式中介时。 | 重新引入 trusted intermediary；见证人可成为审查、故障或信任瓶颈。 | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment]] |
| Witness-network atomic commitment | 在 permissionless witness chain 上部署协调合约，用 `P -> RDauth/RFauth` 互斥状态作为所有 asset contracts 的统一授权。 | 参与链能验证 witness-chain evidence，witness chain finality/fork risk 可接受。 | 增加 witness contract 部署和状态调用成本；需设置 confirmation depth `d`；跨链证据大小和验证方式影响可行性。 | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment]] |
| Contract-embedded cross-chain evidence validation | 在 validator chain 的合约中验证 validated chain 的 headers、PoW 和交易 inclusion evidence。 | 不希望 miners 运行其他链 full nodes/light nodes。 | 验证逻辑复杂且可能昂贵；不同链 finality/证明格式差异大。 | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment]] |
| Timelock cross-chain deals | 用 escrow contracts、commit votes、path signatures 和路径长度相关 timeouts，让 strongly connected deal graph 中的 votes 按 incentive 路径传播。 | 同步网络模型，已知链状态传播上界 `Delta`；希望不引入全局共享 ledger。 | 对 `Delta`/watchtower/DoS countermeasure 敏感；最坏 commit 成本 `O(mn^2)` signature verifications；复杂 deal 必须检查 acceptable payoff。 | [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals]] |
| Certified-blockchain cross-chain deals | 用 CBC/global ledger 记录 commit/abort votes，并向各资产链合约提供 commit/abort proof。 | 半同步模型或需要避免 explicit timelock 的 deal。 | 失去完全去中心化；CBC 可能被 DoS/censor；PoW CBC proof 受 finality/fork 风险影响，BFT certificate 更适合。 | [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | paper | 建立 AC2T graph model、trusted witness baseline、permissionless witness-network atomic commitment、cross-chain evidence validation route | arXiv preprint; analytical evaluation; witness-chain finality/fork/evidence assumptions | p1-p19 |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | paper | 建立 cross-chain deal abstraction；用 compliant-party acceptable payoff 替代不可实现的全局 all-or-nothing，并给出 timelock 与 CBC 两条协议路线 | PVLDB paper; theory/protocol/cost model; no production evaluation | p1-p12 |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | paper | supporting seed: 说明 HTLC exchange atomicity 与 preimage linkability 的问题交叠 | 主要贡献是 privacy/auditing，不是 atomicity foundation | p8-p9 |

## 当前综合

- Evidence window: `2019` to `2026-06-22`，仅覆盖当前 vault 已有 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: Atomic cross-chain transactions 是 cross-chain protocols 下的 problem node。Atomic Commitment Across Blockchains 提供的核心结构是把 distributed transaction 的 atomic commit/abort 决策搬到独立 witness network，并让各 asset chains 只接受同一个稳定 witness decision。Cross-chain Deals 修正了本节点的正确性语义：在 adversarial commerce 中，经典 all-or-nothing 不能作为普遍可实现目标，安全性应表达为每个 compliant party 得到 acceptable payoff，且 compliant party 的资产不能永久 escrow。它还把方法族补成两条 timing/decentralization 路线：synchronous timelock route 保持 fully decentralized，但依赖 `Delta` 和 watchtower/DoS 边界；semi-synchronous CBC route 通过 shared ledger 获得 commit/abort proof，但引入全局 ledger 的 DoS/censorship/finality 边界。zkCross 则作为 supporting seed 表明，HTLC exchange 仍是 atomic cross-chain transactions 的重要方法族，但其 privacy 和 timeout 边界需要与 witness/global-ledger/deal routes 分开记录。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | 新建 atomic cross-chain transactions problem；增加 witness-network atomic commitment、cross-chain evidence validation、witness-network choice/fork-depth 边界。 | 定义与范围; 方法族; 代表 Sources; Bridge Links; 当前综合 | yes | 下一篇 Cross-chain Deals 吸收后复核 method split 和 safety/liveness vocabulary |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | 增加 adversarial-commerce correctness vocabulary、timelock deal protocol、CBC/global-ledger deal protocol，并将 `cross-chain deals` 保持为 source extension 而非独立节点。 | 定义与范围; 背景; 方法族; 代表 Sources; 当前综合; Bridge Links | no new node | 继续吸收 universal atomic swaps、production bridge/finality sources |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | translation, trust_model_shift, coordination, dependency | Atomic commit/commit-abort structure transfers; trusted coordinator, common failure model, blocking assumptions, recovery logs and global all-or-nothing correctness do not transfer unchanged to adversarial independent ledgers. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-atomic-cross-chain-transactions | is_a | nahida-knowledge-cross-chain-protocols | vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md | high | active_seed |
| nahida-knowledge-atomic-cross-chain-transactions | evidenced_by | vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md | Atomic Commitment source note | high | active_seed |
| nahida-knowledge-atomic-cross-chain-transactions | evidenced_by | vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md | Cross-chain Deals source note | high | active_seed |
| nahida-knowledge-atomic-cross-chain-transactions | evidenced_by | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | zkCross source note | medium | supporting_seed |
| nahida-knowledge-atomic-cross-chain-transactions | bridges_to | nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions | vault/05_Bridges/distributed-transactions-to-atomic-cross-chain-transactions.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Universal atomic swap / HTLC graph sources 尚未吸收。 | Cross-chain Deals 已补 deal-based safety/liveness；还需要 Herlihy atomic swaps、XCLAIM 或 production swap/bridge sources 对比 HTLC graph route。 | nahida-update serial intake | high | queued |
| Production bridge/finality/evidence validation source 仍缺。 | 真实链上的 finality、proof size、gas、relay incentives 会决定 witness/evidence route 是否可部署。 | nahida-research-search or paper intake | high | queued |
| 经典 atomic commit / 2PC foundation source 仍缺。 | 当前 bridge 用 blockchain adaptation evidence 支撑，仍不能替代分布式事务教材。 | nahida-research-search foundation_pack | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-atomic-cross-chain-transactions | Created atomic cross-chain transactions problem node from Atomic Commitment Across Blockchains; added witness-network atomic commitment route and bridge to distributed transactions. | arxiv:1905.02847v2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-cross-chain-deals | Added Cross-chain Deals as a source extension; refreshed safety/liveness vocabulary and timelock/CBC method routes without creating a source-named knowledge node. | doi:10.14778/3364324.3364326 | codex |
