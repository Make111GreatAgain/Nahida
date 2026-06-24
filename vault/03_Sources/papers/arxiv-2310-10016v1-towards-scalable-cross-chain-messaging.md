---
id: "arxiv:2310.10016v1"
title: "Towards Scalable Cross-Chain Messaging"
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
  - "p1 abstract, introduction, cross-chain communication problem split"
  - "p2-p3 permissionless relayer model, race conditions, scalability bottlenecks, reordering/censorship risk"
  - "p3 system model, threat model, cryptographic assumptions"
  - "p3-p4 design goals: scalability, accountability, fair allocation"
  - "p4-p6 Coordinator protocol: membership, task allocation, message delivery, incentives"
  - "p6-p7 discussion: performance/reliability trade-off, efficient allocation, incentive/QoS"
  - "p7-p8 related work, conclusion, references"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2310.10016"
doi: ""
arxiv_id: "2310.10016v1"
venue: "arXiv preprint"
year: "2023"
pdf_pages: 8
pdf_sha256: "f2de7330ad81febc67f8adb2060ce5c57724598d761c3a4482ac1ad8ae4065b2"
local_pdf: "~/Desktop/paper/2310.10016.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2310.10016-f2de7330ad81-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "interoperability"
topic_ids:
  - "cross-chain-protocols"
  - "cross-chain-message-relaying"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
  - "cross-chain-message-relaying"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying/arxiv-2310-10016v1"
secondary_ontology_paths: []
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
  directions:
    - "interoperability"
  topics:
    - "cross-chain-protocols"
    - "cross-chain-message-relaying"
    - "permissionless-relayer-coordination"
domains:
  - "blockchain-systems"
topics:
  - "cross-chain messaging"
  - "cross-chain relaying"
  - "permissionless relayers"
  - "relayer coordination"
  - "cross-chain protocol scalability"
aliases:
  - "Scalable Cross-Chain Messaging"
  - "permissionless cross-chain relaying"
  - "relayer coordination protocol"
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
    - "permissionless relayers redundantly deliver the same cross-chain messages and waste gas in winner-takes-all races"
    - "adding relayers does not necessarily increase cross-chain messaging throughput when all relayers compete for the same tasks"
    - "faster or better funded relayers can monopolize delivery and create reordering or censorship risk"
    - "cross-chain data transport needs coordination distinct from authenticity verification"
  method_family:
    - "on-chain Coordinator contract/module"
    - "relayer membership with collateral and unbonding"
    - "modular-hash task allocation over registered relayer set"
    - "three-transaction source request, destination delivery, source acknowledgement flow"
    - "assigned-relayer delivery fee, timeout proof reward, collateral slashing"
  system_layer:
    - "cross-chain message transport"
    - "relayer network"
    - "source and destination chain coordination contracts"
    - "light-client-assisted cross-chain channel"
  evaluation_context:
    - "conceptual protocol and research-challenge discussion"
    - "no empirical benchmark"
    - "synchronous-network model"
  bridge:
    - "candidate: task-allocation-and-load-balancing-to-cross-chain-relayer-coordination"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-scalable-cross-chain-messaging"
source_refs:
  - "arxiv:2310.10016"
  - "arxiv:2310.10016v1"
  - "pdf:~/Desktop/paper/2310.10016.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> interoperability -> cross-chain-protocols"
secondary_directions: []
classification_status: "refined_from_queue"
classification_confidence: "high"
classification_evidence:
  - "abstract frames relayers as cross-chain data transport applications"
  - "Sections II and V analyze permissionless relaying and propose relayer coordination"
  - "paper explicitly excludes authenticity verification as the focus and targets message transport performance/scalability/security"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0060"
queue_status: "absorbed"
---

# Towards Scalable Cross-Chain Messaging

## 论文身份

- 标题: Towards Scalable Cross-Chain Messaging
- 作者: Joao Otavio Chervinski, Diego Kreutz, Jiangshan Yu
- 机构: Monash University; Federal University of Pampa
- 年份: 2023
- arXiv: `2310.10016v1`
- 本地 PDF: `~/Desktop/paper/2310.10016.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/2310.10016-f2de7330ad81-pages.txt`
- SHA-256: `f2de7330ad81febc67f8adb2060ce5c57724598d761c3a4482ac1ad8ae4065b2`
- 备注: 本 note 只基于本地 PDF 精读；没有重新搜索网页或项目实现。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 8
- 已覆盖章节: Abstract, Introduction, Cross-chain Message Relaying, System Model, Design Goals, Protocol for Relayer Coordination, Discussion and Research Challenges, Related Work, Conclusion。
- Extraction gaps: 作者姓名在 PDF 抽取文本中有重音字符错位；本 note 使用规范化 ASCII 名称。论文没有实验评测，故没有 benchmark 数字可抽取。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §I / p1 | 问题与贡献 | 区块链缺直接外部通信；relayers 负责跨链数据运输；permissionless redundancy 带来 race/scalability/security 问题 | high |
| §II / p2-p3 | 现有 relaying 模型的问题 | winner-takes-all race、gas 浪费、加入更多 relayer 不提升 throughput、强 relayer 可重排/审查 | high |
| §III / p3 | 系统与威胁模型 | 两条 append-only blockchain、deterministic contracts、同步网络、profit-maximizing relayers、签名和哈希假设 | high |
| §IV / p3-p4 | 设计目标 | scalability、accountability、fair allocation | high |
| §V / p4-p6 | 协议设计 | Coordinator、membership/collateral/unbonding、hash-based task allocation、delivery/ack/timeout、fee/slashing incentives | high |
| §VI / p6-p7 | 研究挑战 | 分配任务提升性能但降低 redundancy；异构 relayer 负载均衡、QoS 与 fee priority 仍难 | high |
| §VII-§VIII / p7-p8 | 相关工作与结论 | 声称该问题在 cross-chain communication 中少被研究；提出后续方向 | medium |

## 一句话贡献

这篇论文把跨链协议中的 relayer transport 从“默认可用的链下转发组件”提升成独立问题：permissionless relayers 的冗余竞争会造成 race conditions、吞吐不可扩展和重排/审查风险，因此需要可激励、可追责、可公平分配任务的 relayer coordination 层。

## 核心问题设定

跨链通信可以拆成两个问题：一是如何把数据从 source chain 运输到 destination chain，二是 destination chain 如何验证输入数据的真实性。论文明确聚焦第一个问题，即 data/message transport；light client、NIPoPoW、ZKP、Merkle proof 等真实性验证机制不是本篇要解决的核心。

现有 permissionless relaying 的好处是 redundancy：多个独立 relayers 同时尝试运输同一批消息，只要有一个成功，跨链消息就能前进。但当每个 relayer 都为相同任务付出 gas 和网络/节点访问成本时，系统变成 winner-takes-all。输掉的 relayers 可能交易失败并承担 gas，强 relayer 可以通过更高 fee 或更快链上提交抢走收益，最终弱 relayer 退出，permissionless relay set 反而集中化。

因此，本 source 的持久知识不应落成某个具体协议名，而应落在 [[cross-chain-message-relaying|cross-chain message relaying]]：跨链消息运输层如何在 reliability、throughput、incentives、公平性和 censorship resistance 之间做设计。

## 论文识别出的三个问题

| 问题 | 机制 | 影响 | 本文证据 |
| --- | --- | --- | --- |
| Race conditions | 多个 relayers 同时交付相同 pending transactions；链上只接受第一个成功交付，其他交付失败或 revert。 | 重复 gas 支出、fee race、relayer 预期收益下降。 | §II-A |
| Hindered scalability | 添加 relayer 不等于提高吞吐，因为大家仍争抢同一任务；full-node/RPC 数据获取和 surge load 也可成为 bottleneck。 | 系统容量不随 relayer 数量线性增长，高峰期 relayers 可能崩溃。 | §II-B |
| Reordering and censorship | 更快/更有钱的 relayer 可能持续垄断消息提交顺序。 | 可进行 transaction censorship、frontrunning、sandwich-style reordering，permissionless 性质被削弱。 | §II-C |

## 系统模型和边界

- 两条链 `Chain A` 和 `Chain B` 都是 independent tamper-proof append-only blockchains，并满足 persistence 与 liveness。
- Smart contracts 是 public deterministic programs，不能主动访问外部信息，只能接收外部输入。
- 网络模型是 synchronous network with known upper delay，message delivery reliable。
- Relayers 维护跨链 channel，并在 source/destination 链之间运输消息和证明材料。
- 威胁模型关注 profit-maximizing relayers；不讨论底层区块链、合约代码或真实性验证协议本身被攻击。
- 密码假设包括用户公私钥、签名不可伪造，以及 collision-resistant hash。

这意味着论文提出的是 transport coordination 层，而不是完整 bridge 安全证明。若 source chain finality、light-client verifier 或 destination contract 有问题，本协议不会自动修复。

## 设计目标

| 目标 | 含义 | 关键边界 |
| --- | --- | --- |
| Scalability | 从 `n` 到 `n+1` 个 relayers 时，collective throughput 应提高。 | 不要求严格线性，因为 relayer 资源异构。 |
| Accountability | 被分配任务的 relayer 若超时未完成，应可被惩罚。 | 需要 timeout proof 和 collateral/slashing。 |
| Fair allocation | 工作量应在维护 channel 的 relayers 间均匀分配，让每个 relayer 有获利机会。 | 复杂动态 load balancing 很难直接在链上实现。 |

## 协议机制

### Coordinator

论文提出一个链上 `COORDINATOR`，由 source chain 和 destination chain 各自实现为 contract 或 runtime module。Coordinator 不直接增加可信第三方，因为代码公开、执行确定；但两边 Coordinator 仍需要通过跨链协议维护 counterparty state，例如 light client 和 relayers 携带的 block headers。

Coordinator 承担四个职能:

- membership management
- task allocation
- message delivery
- incentivization

### Membership and collateral

Relayer 调用 `register(pubkey, collateral)` 加入 active set `R`。Coordinator 保存公钥、relayer id、collateral。退出时调用 `withdraw(pubkey)` 进入 unbonding period，期间从 active set 移除，不再分配新任务，但仍需完成既有 pending tasks。Unbonding 期长于最长 timeout，避免 relayer 接任务后立刻退出取回抵押。

如果 relayer 未完成任务，其 collateral 可被 slashed；抵押低于最低值时也可自动进入 unbonding。

### Hash-based task allocation

任务分配的核心是简单、可链上验证的 uniform allocation。论文给出两种 route:

| Route | 做法 | 适用条件 | 代价 |
| --- | --- | --- | --- |
| Contract-side allocation | 用户通过 `COORDINATOR` 提交跨链请求；contract 获取当前 transaction hash，计算 `H(txHash) mod m`，其中 `m = |R|`，把任务分给对应 relayer。 | Contract/runtime 可访问 invoking transaction hash。 | 对链功能有要求；分配随当前 registered set 改变。 |
| User/relayer-side allocation | 用户或 relayer 在交易上链后计算分配结果，再调用 `assignTasks()` 提交 tx hash 与 relayer id；contract 验证交易存在、未被分配、分配正确。 | Contract 无法访问当前 tx hash，但能按 hash 检索交易或依赖 oracle。 | 至少多一个 block interval 延迟；提交者激励需要设计。 |

这一步的知识价值在于：跨链 relaying 的可扩展性可以通过 task partitioning 而不是 pure redundancy 来获得，但它把问题从“谁先送达”改成“谁被分配并可被追责”。

### Message delivery and acknowledgement

一次跨链操作被拆成三笔交易:

1. Source chain 上的 request transaction。
2. Destination chain 上的 delivery / processed-operation transaction。
3. Source chain 上证明 destination 已处理的 acknowledgement transaction。

被分配的 relayer 读取 source transaction，调用 destination 的 `deliverTx()`，携带格式化数据和 light-client/state evidence；随后读取 destination receipt，再调用 source 的 `proveDelivery()`。以 token transfer 为例，source coordinator 先 escrow tokens，destination mint 或发送 tokens，source 在看到 receipt 后销毁 escrowed tokens。

### Timeout and proof-of-absence

如果 destination chain 在指定 block range 内没有包含对应 cross-chain transaction，其他 relayers 可提交 `submitTimeout()`。Coordinator 需要能验证 proof-of-absence，确认任务未按时完成。论文不展开 proof-of-absence 实现，只把它作为 timeout/slashing 的必要机制。

### Incentives

用户支付 delivery fee，由 source Coordinator 持有。关键设计是 reward 总是发给最初被分配的 relayer，而不是实际抢先提交者。这样，其他 relayers 即使抢送成功也拿不到 reward，只会付出 gas，从而削弱任务偷抢动机。

当任务超时，assigned relayer 的 collateral 被 slashed。由于 assigned relayer 没有动力举报自己失败，协议允许其他 relayers 提交 timeout proof，并从被 slashed collateral 中获得奖励；用户也可得到一部分补偿。

## 主要权衡

| 权衡 | 论文观点 | 对知识库的意义 |
| --- | --- | --- |
| Performance vs reliability | 任务分配能减少冗余竞争，提高扩展性；但单 relayer 分配会降低 redundancy，一旦 assigned relayer 失败会影响 liveness。 | cross-chain relaying 不能简单追求吞吐，必须记录 redundancy parameter 或 near-timeout rescue 机制。 |
| Efficient allocation | 统一 hash 分配简单可验证，但不考虑 relayer 资源异构；复杂 load balancing 需要链上观察性能、硬件或队列状态，成本高。 | 这是分布式系统 task allocation 与链上可验证状态之间的 bridge candidate。 |
| Incentives and QoS | 消除竞争会减少 gas waste，但也可能削弱 relayer 为更高 service quality 投资的动机；fee priority 的作用被改变。 | relayer coordination 是经济激励问题，不只是调度算法。 |

## 与现有知识库的关系

| Knowledge target | 关系 | 处理方式 |
| --- | --- | --- |
| [[cross-chain-protocols|Cross-chain protocols]] | 本文补上 cross-chain messaging transport / relayer coordination 路线。 | 更新父节点的方法族、source extension 和缺口。 |
| [[interoperability|Blockchain interoperability]] | 本文说明互操作不只验证跨链状态，也要运输消息并协调 relayers。 | 更新方向节点的综合和 source list。 |
| distributed task allocation / load balancing | 本文使用任务分配和负载均衡思想，但没有给出通用分布式系统基础。 | 暂不新建 bridge；记录为 candidate/foundation gap。 |

## Source-only 细节

以下内容保留在 source note，不上升为知识节点:

- `COORDINATOR` 的函数名、`register(pubkey, collateral)`、`withdraw(pubkey)`、`deliverTx()`、`proveDelivery()`、`assignTasks()`、`submitTimeout()`。
- token transfer 示例中的 escrow/mint/destroy 细节。
- 论文列举的 IBC、Nomad、Gelato、Keep3r、Darwinia、LayerZero 作为 relayer-using systems 的例子；未精读这些系统，不把它们当成本库证据。
- Tendermint RPC sequential processing 作为性能瓶颈例子；没有因此改写 Tendermint/CometBFT 节点。

## 知识增量

| Delta | Reusable placement | Notes |
| --- | --- | --- |
| Cross-chain communication 应拆分为 data transport 与 authenticity verification。 | Cross-chain message relaying; cross-chain protocols | 本文只解决 transport。 |
| Permissionless redundancy improves liveness but causes race/gas-waste/scalability issues. | Cross-chain message relaying | 问题 framing。 |
| Hash-based task allocation can convert relayer competition into assigned accountability. | Cross-chain message relaying | 方法 route。 |
| Rewards to assigned relayer reduce task stealing but change QoS/fee-priority incentives. | Cross-chain message relaying | 激励边界。 |
| Relayer coordination needs timeout proof and collateral slashing to preserve accountability. | Cross-chain message relaying | 机制依赖。 |

## 不足与后续

- 没有实验评测，不能用来判断真实吞吐提升幅度。
- 没有形式化安全证明，主要是 protocol proposal 和 trade-off analysis。
- 没有深读具体 relayer implementations，例如 IBC relayer、LayerZero endpoint、Gelato/Keep3r 等。
- Proof-of-absence 和 light-client verification 只是依赖项，不是本文贡献。
- 需要后续 source 建立 distributed task allocation / load balancing 基础，再决定是否创建 bridge 到 cross-chain relayer coordination。

## 提取关系

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| `arxiv:2310.10016v1` | instance_of | `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying` | source note; §II-§VI | high | active_seed |
| `permissionless relayer redundancy` | creates | `race conditions and gas waste` | §II-A | high | source_extension |
| `relayer task allocation` | mitigates | `winner-takes-all relayer competition` | §V-B | high | source_extension |
| `assigned-relayer rewards` | discourages | `task stealing by non-assigned relayers` | §V-D | high | source_extension |
| `timeout proof and collateral slashing` | supports | `relayer accountability` | §V-D | high | source_extension |

