---
id: "nahida-knowledge-cross-chain-smart-contract-invocation"
title: "Cross-chain smart contract invocation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "cross-chain-smart-contract-invocation"
domain_id: "blockchain-systems"
direction_id: "interoperability"
parent_knowledge_refs:
  - "nahida-knowledge-cross-chain-protocols"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
  - "cross-chain-smart-contract-invocation"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation"
secondary_ontology_paths:
  - "blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions"
  - "blockchain-systems/execution-and-transactions/transaction-processing"
  - "distributed-systems/transaction-processing/distributed-transactions"
relation_edges:
  - from: "nahida-knowledge-cross-chain-smart-contract-invocation"
    relation: "is_a"
    to: "nahida-knowledge-cross-chain-protocols"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-smart-contract-invocation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-smart-contract-invocation"
    relation: "depends_on"
    to: "nahida-knowledge-atomic-cross-chain-transactions"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-smart-contract-invocation"
    relation: "adjacent_to"
    to: "nahida-knowledge-blockchain-transaction-processing"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-smart-contract-invocation"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-smart-contract-invocation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-smart-contract-invocation"
    relation: "bridges_to"
    to: "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/05_Bridges/cross-chain-message-relaying-to-cross-chain-smart-contract-invocation.md"
      - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
  - "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
source_note_refs:
  - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
  - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
representative_source_refs:
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
  - "arxiv:2310.10065"
query_keys:
  - "cross-chain smart contract invocation"
  - "cross-chain contract calls"
  - "CCSCI"
  - "cross-chain transaction serializability"
  - "cross-chain transaction atomicity"
  - "cross-chain hybrid concurrency control"
  - "read-write separation cross-chain invocation"
  - "ShuttleCross"
  - "inscription-triggered smart contract invocation"
  - "Bitcoin inscriptions Ethereum contract calls"
  - "BRC-20 to Ethereum smart contract invocation"
aliases:
  - "cross-chain smart contract calls"
  - "cross-chain contract invocation"
  - "CCSCI"
  - "inscription-triggered contract invocation"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "cross-chain-smart-contract-invocation"
  - "cross-chain-protocols"
  - "atomicity"
  - "serializability"
  - "hybrid-concurrency-control"
  - "two-phase-commit"
  - "inscription-triggered-invocation"
  - "bitcoin-ethereum-bridge"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-22"
evidence_window_start: "2025"
evidence_window_end: "2026-06-23"
created: "2026-06-22"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation"
  - "nahida-knowledge-20260623-brc20-to-ethereum"
source_refs:
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
  - "arxiv:2310.10065"
confidence: "medium"
trust_tier: "primary"
---

# Cross-chain smart contract invocation

## 定义与范围

- 定义: Cross-chain smart contract invocation 研究一条链上的 smart contract 如何调用另一条或多条链上的 contract functions，并把这些跨链调用组织成具有 atomicity、serializability、liveness 和可接受性能的 cross-chain transaction。
- 不包含: 某个系统名、某个 callback API、某个 `opList`/`lockList` 实现细节或一次 benchmark 数字；这些保留在 source note。
- Canonical terms: `cross-chain smart contract invocation`, `CCSCI`.
- Retrieval role: 回答“跨链智能合约调用如何保证原子性/串行化/低延迟”时先进入本节点，再按需要打开 ShuttleCross、atomic cross-chain transactions、message relaying 或 transaction-processing 节点。
- Update scope: 新 source 涉及 cross-chain contract calls、callback invocation、2PC/GPACT-style invocation、read-only off-chain invocation、cross-chain serializability/concurrency control 时刷新。

## 背景

跨链协议早期常围绕 token transfer、atomic swap、bridge header verification 或 relayer transport 展开。但 smart contracts 让跨链交互变成多步服务逻辑：一个 origin-chain contract 可以调用 target-chain functions、等待返回值、再触发后续调用。典型场景不是“把资产从 A 链换到 B 链”，而是贷款审批、供应链验证、抵押、权限检查等跨链 workflow。

[[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] 是本节点的 seed source。它把问题明确成 cross-chain transaction 的调用执行: `CTX` 包含多个 `invoke_i`，每个 invocation 在 target chain 上读写状态；只有所有 invocations 都成功并提交，整个 `CTX` 才成功。

[[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] 提供相邻但较窄的 source extension：Bitcoin 用户不能直接运行 Ethereum-style contract workflow，但可以把 Ethereum contract address、operation 和参数写入 BRC-20 inscription；MIDAS TOUCH middleware 读取后代表用户调用 Ethereum contract。它证明 source-chain message relaying 可以触发 target-chain smart contract invocation，但不提供 ShuttleCross 所要求的 multi-invocation atomicity、serializability 或 HCC。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它能组织 RPC-like invocation、2PC-based invocation、smart contract portability、cross-chain serializability、read-only cross-chain invocation 和 future production CCSCI sources。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: ShuttleCross 是当前代表 source；本节点沉淀的是“跨链合约调用”的问题边界和方法族。
- 需要引用的更基础 Knowledge: [[cross-chain-protocols|Cross-chain protocols]]。
- 相邻基础: [[atomic-cross-chain-transactions|Atomic cross-chain transactions]]、[[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]]、[[distributed-transactions|Distributed transactions]]。

## 解决的问题

当一个 smart-contract workflow 跨多条链执行时，系统要同时解决:

- **Atomicity**: 同一 cross-chain transaction 内所有 invocations 要么全部提交，要么全部中止。
- **Serializability**: 并发 cross-chain transactions 读写同一 state 时，结果要等价于某个串行顺序。
- **Liveness**: origin/target chain 或 inter-chain messages 出现延迟/丢失时，目标链不能无限等待。
- **Performance**: 多次跨链调用不应因为 target-chain tx pool/consensus 等待、锁竞争或乐观冲突而产生过高 latency/abort rate。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[cross-chain-protocols|Cross-chain protocols]] | child_of | CCSCI 是跨链协议中从 asset/message transfer 推进到 contract-function execution 的问题族 | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| RPC-like cross-chain invocation | method candidate | callback/API route 是常见 invocation family，但当前只有 related-work evidence。 | ShuttleCross related work | review |
| 2PC-based cross-chain invocation | method candidate | 2PC/GPACT/2PC4BC/ShuttleCross 共同围绕 commit/abort coordination；需要更多 direct sources 决定是否拆 child。 | ShuttleCross; existing atomic cross-chain sources | review |
| cross-chain invocation concurrency control | method/problem candidate | serializability、OCC、S2PL、HCC、deadlock detection 对性能与正确性都关键；当前 ShuttleCross 是强 seed。 | ShuttleCross | review |
| read-only cross-chain invocation acceleration | method candidate | 读写分离/dual-processing 是 latency route；需要更多 production 或理论 source 才能拆独立节点。 | ShuttleCross | source_extension |
| inscription-triggered target-chain invocation | method candidate | 源链 metadata/inscription 触发目标链合约调用，是 relay-to-invocation 的一条 route；当前只有 MIDAS TOUCH source。 | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | source_extension |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| RPC-like invocation | Origin-chain contract 异步调用 target-chain contract，并通过 callback 接收返回值。 | 简单跨链查询或无需复杂 all-or-nothing 的调用。 | 不自然保证复杂跨链交易 atomicity。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] related work |
| 2PC-based invocation | 一个 client 或 origin chain 作为 2PC manager，协调 target chains 执行 invocations，并统一 commit/abort。 | 复杂跨链 workflow 需要 atomicity。 | coordinator/finality/evidence/liveness assumptions 必须显式处理；单一 S2PL/OCC 会影响性能。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] |
| Smart contract portability | 把涉及的 contracts/states 迁移到同一条链，利用单链交易 atomicity 执行后再写回。 | 参与链兼容、contract 可迁移且状态迁移成本可接受。 | 对异构链支持弱；频繁迁移增加 inter-chain overhead。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] related work |
| Hybrid cross-chain concurrency control | 按 state contention 动态选择 OCC 或 S2PL：低争用 state 用 `opList` 乐观执行，高争用 state 用 `lockList` 排队锁定。 | 多个 CTX 会并发访问同一 target-chain state，且 workload contention 变化。 | 需要状态分类、deadlock detection、timeout 和阈值调参；OCC 冲突与 S2PL 等待都没有消失。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] |
| Dual-processing read-write separation | read-only invocation 先由 target-chain nodes off-chain 执行并返回 `2f + 1` 一致结果，同时仍进入 tx pool 形成官方版本；版本匹配才允许 commit。 | read-only invocation 比例较高，目标状态是 `occState`，且 target chain 能提供足够一致的节点返回。 | off-chain result 必须后来在链上可见；版本不匹配要 abort；无法加速写调用或高争用 lockState 写路径。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] |
| Inscription-triggered target-chain invocation | 源链 inscription 携带 target contract address、operation 和参数；middleware validators 解析后调用 Ethereum smart contract。 | 源链可承载可解析 metadata，但不支持目标链合约直接执行。 | 当前是 one-way Bitcoin -> Ethereum；依赖 validator committee 和 receipt relay；不保证跨多个目标合约的 atomicity/serializability。 | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross: An Efficient Cross-Chain Smart Contract Invocation Framework]] | paper | 新建 CCSCI problem node；给出 origin-chain 2PC、HCC、deadlock detection、dual-processing read-write separation 和 ChainMaker evaluation。 | Manuscript proof; ChainMaker/TBFT prototype; assumes BFT-secure chains, PKI/committee signatures, partial synchrony, `2f + 1` matching off-chain read results. | p1-p12 |
| [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | paper | 新增 inscription-triggered invocation source extension：Bitcoin inscriptions 经过 validator middleware 触发 Ethereum contract calls，并把 receipts 写回 Bitcoin。 | One-way bridge; validator honest-majority assumption; not a general CTX atomicity/serializability framework. | p1-p10 |

## 当前综合

- Evidence window: `2025` to `2026-06-23`，仅覆盖当前 vault source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- 综合: Cross-chain smart contract invocation 是 cross-chain protocols 下独立于 atomic swaps 和 relayer transport 的问题。它的核心对象是由多个 contract-function invocations 构成的 `CTX`，其正确性目标包含 atomicity、serializability 和 liveness。ShuttleCross 提供当前最强 seed: origin chain 用 2PC 统一 commit/abort；target chains 通过 cached dirty states 暂存写入；HCC 根据 state contention 在 OCC `opList` 和 S2PL `lockList` 之间切换；read-only invocations 通过 off-chain fast path 加速，但仍必须进入链上正式执行来建立 serializability visibility。Bridging BRC-20 to Ethereum 提供较窄的 relay-to-invocation route：Bitcoin inscription 表达调用意图，middleware 在 Ethereum 上执行目标 contract call，再把 receipt 写回 Bitcoin。该 route 扩展 invocation 入口，但不改变 CCSCI 的核心 correctness goals。该问题向上属于 [[cross-chain-protocols|cross-chain protocols]]，向侧面依赖 [[atomic-cross-chain-transactions|atomic cross-chain transactions]] 和 [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|blockchain transaction processing]]。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | 新建 CCSCI problem node；新增 2PC-based invocation、hybrid cross-chain concurrency control、dual-processing read-write separation 和 source-backed bridge to distributed transactions。 | 定义与范围; 方法族; 代表 Sources; Bridge Links; 当前综合 | yes | 后续吸收 GPACT/2PC4BC/EOVPC/Avalon/IBC callback/production CCSCI sources 后复核 child split。 |
| [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | 新增 inscription-triggered target-chain invocation route，并通过 bridge 连接 message relaying；不改变 ShuttleCross seed 的 CTX correctness boundary。 | 背景; 下级结构; 方法族; 代表 Sources; Bridge Links; 当前综合 | no new child | 后续吸收 bidirectional Bitcoin/EVM invocation、BRC-20 bridge production 或 trustless verification source 后复核。 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-transactions-to-cross-chain-smart-contract-invocation|Distributed transactions -> cross-chain smart contract invocation]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | translation, coordination, concurrency_control, trust_model_shift | 2PC/OCC/S2PL vocabulary transfers; independent BFT ledgers, origin-chain coordination, committee signatures, timeout polling and on-chain visibility change the correctness boundary. | active_seed |
| [[cross-chain-message-relaying-to-cross-chain-smart-contract-invocation|Cross-chain message relaying -> cross-chain smart contract invocation]] | `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying; blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | dependency, transport_to_execution, receipt_flow, trust_boundary | Message/inscription transport can trigger target-chain contract execution; target contract atomicity, serializability and bidirectional workflow semantics remain outside relaying alone. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-cross-chain-smart-contract-invocation | is_a | nahida-knowledge-cross-chain-protocols | vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md | high | active_seed |
| nahida-knowledge-cross-chain-smart-contract-invocation | evidenced_by | vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md | ShuttleCross source note | high | active_seed |
| nahida-knowledge-cross-chain-smart-contract-invocation | depends_on | nahida-knowledge-atomic-cross-chain-transactions | ShuttleCross 2PC atomicity | high | active_seed |
| nahida-knowledge-cross-chain-smart-contract-invocation | adjacent_to | nahida-knowledge-blockchain-transaction-processing | ShuttleCross HCC/serializability | high | active_seed |
| nahida-knowledge-cross-chain-smart-contract-invocation | bridges_to | nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation | vault/05_Bridges/distributed-transactions-to-cross-chain-smart-contract-invocation.md | high | active_seed |
| nahida-knowledge-cross-chain-smart-contract-invocation | evidenced_by | vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md | BRC-20 to Ethereum source note | high | active_seed |
| nahida-knowledge-cross-chain-smart-contract-invocation | bridges_to | nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation | vault/05_Bridges/cross-chain-message-relaying-to-cross-chain-smart-contract-invocation.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| GPACT、2PC4BC、EOVPC、Avalon 等 CCSCI direct sources 尚未吸收。 | 需要判断 2PC-based invocation、OCC/S2PL/HCC 是否应拆成独立 child nodes。 | nahida-update / nahida-research-search | high | queued |
| IBC/XCMP/callback production invocation source 缺。 | RPC-like invocation 目前来自 related-work evidence，不足以成为成熟路线。 | nahida-research-search | medium | queued |
| Heterogeneous-chain finality、fee、relayer、contract-language compatibility 边界缺生产 source。 | ShuttleCross evaluation 在 ChainMaker/TBFT 环境，不能直接代表开放异构链部署。 | nahida-research-search | medium | queued |
| Inscription-triggered invocation source 仍薄。 | MIDAS TOUCH 给出 Bitcoin -> Ethereum one-way route，但还缺 bidirectional workflow、trustless receipt proof、BRC-20 production bridge 和 validator incentive/slashing source。 | nahida-update / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation | Created cross-chain smart contract invocation problem node from ShuttleCross and linked it to distributed transaction and blockchain transaction-processing foundations. | sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72 | codex |
| 2026-06-23 | nahida-knowledge-20260623-brc20-to-ethereum | Added inscription-triggered Ethereum invocation route from Bridging BRC-20 to Ethereum and linked it to message relaying. | arxiv:2310.10065 | codex |
