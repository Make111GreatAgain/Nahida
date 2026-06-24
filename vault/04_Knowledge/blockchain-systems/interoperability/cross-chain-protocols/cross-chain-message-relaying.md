---
id: "nahida-knowledge-cross-chain-message-relaying"
title: "Cross-chain message relaying"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "subproblem"
file_slug: "cross-chain-message-relaying"
domain_id: "blockchain-systems"
direction_id: "interoperability"
parent_knowledge_refs:
  - "nahida-knowledge-cross-chain-protocols"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
  - "cross-chain-message-relaying"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-cross-chain-message-relaying"
    relation: "is_a"
    to: "nahida-knowledge-cross-chain-protocols"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-message-relaying"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-message-relaying"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-message-relaying"
    relation: "bridges_to"
    to: "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/05_Bridges/cross-chain-message-relaying-to-cross-chain-smart-contract-invocation.md"
      - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
  - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
representative_source_refs:
  - "arxiv:2310.10016v1"
  - "arxiv:2310.10065"
query_keys:
  - "Cross-chain message relaying"
  - "cross-chain messaging"
  - "cross-chain relaying"
  - "permissionless relayers"
  - "relayer coordination"
  - "relayer task allocation"
  - "relayer censorship"
  - "cross-chain message transport"
  - "inscription-based message relaying"
  - "Bitcoin inscription relay"
  - "BRC-20 receipt relaying"
aliases:
  - "cross-chain relaying"
  - "permissionless relayer coordination"
  - "cross-chain message transport"
  - "inscription-based relaying"
domains:
  - "blockchain-systems"
topics:
  - "cross-chain-message-relaying"
  - "permissionless relayers"
  - "relayer coordination"
  - "cross-chain protocol scalability"
  - "inscription-based-message-relaying"
  - "receipt-relaying"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-22"
evidence_window_end: "2026-06-23"
created: "2026-06-22"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-scalable-cross-chain-messaging"
  - "nahida-knowledge-20260623-brc20-to-ethereum"
source_refs:
  - "arxiv:2310.10016v1"
  - "arxiv:2310.10065"
confidence: "medium"
trust_tier: "primary"
---

# Cross-chain message relaying

## 定义与范围

- 定义: Cross-chain message relaying 研究在不同区块链之间运输消息、交易收据、区块头或应用数据的 relayer layer 如何组织，使跨链消息能及时、可追责、抗审查地从 source chain 到达 destination chain。
- 不包含: 具体桥合约实现、单个 relayer 服务、某个 token-transfer 示例函数、light-client verifier 或 ZK proof 的内部证明系统；这些保留在 source note 或更专门的知识节点。
- Canonical terms: `cross-chain message relaying`, `cross-chain relaying`
- Aliases/query keys: permissionless relayers, relayer coordination, relayer task allocation, cross-chain message transport
- Standalone completeness check: 本节点解释 relayer transport 的问题边界、设计目标、方法族、代表 source、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 当用户问跨链消息、IBC relayers、bridge relayers、relayer incentives、跨链消息吞吐或 relayer censorship 时，优先返回本节点，再按需打开 source note。
- Update scope: 新 source 若改变 relayer coordination、task allocation、incentive、liveness/reliability 或 censorship resistance 的判断，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

跨链协议通常把重点放在 destination chain 如何验证 source chain 状态，例如 light-client verification、Merkle proof、ZK proof 或 consensus signatures。但真正让消息跨链移动的往往是链下 relayers。[[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] 把这个运输层单独抽出：permissionless relayers 的冗余交付提高可靠性，却会让多个 relayers 为同一消息竞争链上提交，形成 gas waste、吞吐不可扩展和重排/审查风险。

因此，本节点位于 [[cross-chain-protocols|Cross-chain protocols]] 下方，而不是放进 generic consensus 或 storage。它关注的不是“跨链证明是否正确”，而是“谁负责把消息送过去、如何分配任务、失败如何追责、经济激励是否让 relayer set 保持开放”。

[[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] 补充了另一种 relaying evidence：消息不是来自通用 bridge contract event，而是来自 Bitcoin BRC-20 inscription。MIDAS TOUCH 的 validator committee 负责扫描 Bitcoin blocks/transaction outputs、解析 inscriptions、每隔 `epsilon` block heights 打包排序请求、运行 consensus，并在 Ethereum 调用完成后把 receipts 写回 Bitcoin。它扩展了本节点的 transport scope，但没有替代 permissionless relayer coordination 问题。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `subproblem`。
- 为什么足够通用: IBC、bridges、oracle-like cross-chain channels、cross-chain smart-contract invocation 等系统都可能依赖 relayers 或等价 transport workers。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: `COORDINATOR`、`assignTasks()`、token escrow/mint 示例留在 source note；本节点抽取 relayer transport 的通用问题和方法。
- 需要引用的更基础 Knowledge: [[cross-chain-protocols|Cross-chain protocols]]、[[interoperability|Blockchain interoperability]]。
- 不应拆出的实例/协议/来源: IBC relayer、LayerZero、Gelato、Keep3r、Darwinia、Nomad 等未精读前只作为待补 source，不作为本库证据。

## 解决的问题

在 permissionless 或多 relayer 的跨链系统中，如何让 relayers 既不重复浪费资源，也不因为强者垄断而削弱 throughput、公平性和 censorship resistance。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[cross-chain-protocols|Cross-chain protocols]] | child_of | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| relayer task allocation | section | 任务分配是 relayer scalability 的核心方法，但当前只有一篇 source，不单独拆 node。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] | source_extension |
| relayer incentives and slashing | section | fee、collateral、timeout proof 决定 accountability 和抗 task stealing；当前 evidence 仍薄。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] | source_extension |
| relayer censorship and ordering | section | relayer 速度/资金优势可造成跨链消息重排与审查；需要更多 MEV/bridge relayer source。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] | queued |
| inscription scanning and receipt relaying | section | Bitcoin inscription 可作为 source-chain intent carrier；validator middleware 需要解析、排序、执行并回写 receipt。 | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | source_extension |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Permissionless redundant relaying | 多个 relayers 同时尝试交付同一消息，依靠冗余提高 liveness。 | 只要任一 relayer 可用就希望消息送达。 | winner-takes-all race、gas waste、fee race、吞吐不随 relayer 数增长。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] |
| Coordinator-based relayer membership | 链上 Coordinator 管理 relayer registration、collateral、withdraw/unbonding。 | 系统希望把 relayer set 和 accountability 显式放到链上状态。 | 需要合约/module 支持；unbonding 期和 collateral 规模需要参数化。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] |
| Hash-based task allocation | 用 `H(txHash) mod |R|` 或等价机制把 cross-chain tasks 分给具体 relayer。 | 任务可被链上验证地映射到 relayer set，且公平性比复杂最优调度更重要。 | 不考虑 relayer 资源异构；链上动态负载均衡困难。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] |
| Source-destination-ack delivery flow | 将跨链操作分成 source request、destination delivery、source acknowledgement。 | 需要 source chain 最终知道 destination 是否处理成功，以便释放 reward 或清理 escrow。 | 依赖 receipt/proof transport 和 light-client/state evidence；增加一次回执路径。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] |
| Assigned-relayer fee and timeout slashing | reward 发给 assigned relayer，失败则 collateral slashed；其他 relayers 可提交 timeout proof 得奖励。 | 希望减少 task stealing，并对未履约 relayer 建立 accountability。 | 需要 proof-of-absence/timeout proof；降低竞争后可能影响 QoS 和 fee-priority。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] |
| Inscription scanning and receipt relaying | Validator committee 扫描 Bitcoin inscriptions，把 operation/contract address/params 作为跨链请求，执行后把 Ethereum receipt 重新发布为 Bitcoin inscription。 | 源链不提供 EVM-style contract calls，但可承载可解析 metadata/inscriptions。 | 依赖 validator committee、inscription parsing、`epsilon` batching 和 receipt inclusion；不是 permissionless task allocation。 | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | paper | 建立 cross-chain message relaying seed：识别 permissionless relayer race、non-scaling throughput、ordering/censorship risk，并提出 Coordinator + task allocation + incentive/slashing 路线 | 单一 source；无实验评测；同步网络模型；不解决 authenticity verification、light-client correctness 或 proof-of-absence 实现 | `p1-p8` |
| [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | paper | 新增 inscription-based relaying evidence：Bitcoin inscriptions 作为 source-chain intent，validator committee 负责 scanning/batching/ordering/receipt relaying。 | One-way Bitcoin -> Ethereum；validator-faithfulness trust boundary；evaluation 主要在 Ethereum testnet。 | `p1-p10` |

## 当前综合

- Evidence window: `2026-06-22` to `2026-06-22`，仅覆盖当前 vault 已有 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: 当前证据显示，cross-chain protocols 至少应把 transport layer 从 verification layer 中分离出来。Relayer redundancy 提供 liveness，但若没有协调，会让所有 relayers 对同一消息重复提交，造成 race/gas waste；更强 relayer 可通过速度或 fee 优势持续抢占任务，进一步带来消息重排和审查风险。Coordinator-based task allocation 是一个 source-backed 路线：它牺牲一部分冗余，通过链上 membership、collateral、hash allocation、delivery acknowledgement 和 timeout slashing 换取可扩展性与可追责性。Bridging BRC-20 to Ethereum 增加了 inscription-based route：source-chain request 可以嵌在 Bitcoin inscription 中，由 validator committee 扫描、排序、执行并回写 receipt。尚未解决的是生产 relayer 系统、异构负载均衡、proof-of-absence 实现、validator trust reduction 和 relayer MEV/QoS 的实证边界。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | 新增 cross-chain message relaying 子问题；把 relayer transport、permissionless race、task allocation、timeout slashing 和 censorship risk 从 generic cross-chain protocols 中拆出 | 定义与范围; 方法族与解决路线; 代表 Sources; 当前综合; 缺口与队列 | yes | 吸收 IBC relayer、cross-chain smart-contract invocation、bridge relayer MEV 或 production relayer sources 后复核是否拆子节点/bridge |
| [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | 新增 inscription scanning、validator batching/ordering 和 receipt relaying source extension，并连接到 cross-chain smart contract invocation。 | 背景; 下级结构; 方法族与解决路线; 代表 Sources; Bridge Links; 当前综合 | no new child | 通过 [[cross-chain-message-relaying-to-cross-chain-smart-contract-invocation|Cross-chain message relaying -> cross-chain smart contract invocation]] 维护 bridge 边界 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| task allocation/load balancing -> cross-chain relayer coordination | `distributed-systems/task-allocation-and-load-balancing; blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying` | candidate, scheduling, incentive_boundary | 通用任务分配思想可迁移；但链上可验证、公平分配、collateral/slashing、跨链 finality 和 relayer incentives 是区块链特有边界。 | review |
| [[cross-chain-message-relaying-to-cross-chain-smart-contract-invocation|Cross-chain message relaying -> cross-chain smart contract invocation]] | `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying; blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | dependency, transport_to_execution, receipt_flow, trust_boundary | Inscription/request transport can trigger target-chain contract execution, but does not itself provide target invocation atomicity or serializability. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-cross-chain-message-relaying | is_a | nahida-knowledge-cross-chain-protocols | vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying.md | high | active_seed |
| nahida-knowledge-cross-chain-message-relaying | evidenced_by | vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md | source note | high | active_seed |
| nahida-knowledge-cross-chain-message-relaying | evidenced_by | vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md | BRC-20 to Ethereum source note | high | active_seed |
| nahida-knowledge-cross-chain-message-relaying | bridges_to | nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation | vault/05_Bridges/cross-chain-message-relaying-to-cross-chain-smart-contract-invocation.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| IBC relayer / production relayer implementations 未深读。 | 需要验证 Coordinator-style allocation 与真实 relayer ecosystem 的差距。 | nahida-github-repo-analyze / nahida-research-search | high | queued |
| Proof-of-absence / timeout proof foundation 缺。 | Slashing/accountability 依赖能够证明 destination chain 在窗口内未包含消息。 | nahida-research-search | medium | queued |
| Relayer MEV、ordering 和 censorship 的独立 source 缺。 | 当前只有本文的风险讨论，无法形成稳定子节点。 | nahida-update / nahida-research-search | medium | queued |
| 通用 task allocation/load balancing foundation 缺。 | 本文使用任务分配思想，但尚未建立跨域 bridge 所需的通用基础概念。 | nahida-research-search | low | queued |
| Inscription-based relaying 仍是单 source seed。 | MIDAS TOUCH 说明 Bitcoin inscription 可作为跨链请求载体，但还缺 production BRC-20 bridge、receipt proof、validator rotation/slashing 和 trustless Bitcoin verification source。 | nahida-update / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-scalable-cross-chain-messaging | Created cross-chain message relaying problem node from Scalable Cross-Chain Messaging and connected it under cross-chain protocols. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-brc20-to-ethereum | Added inscription-based request scanning and receipt relaying route from Bridging BRC-20 to Ethereum. | arxiv:2310.10065 | codex |
