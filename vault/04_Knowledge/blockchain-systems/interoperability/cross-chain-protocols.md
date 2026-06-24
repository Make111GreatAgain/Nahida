---
id: "nahida-knowledge-cross-chain-protocols"
title: "Cross-chain protocols"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "cross-chain-protocols"
domain_id: "blockchain-systems"
direction_id: "interoperability"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-interoperability"
child_knowledge_refs:
  - "nahida-knowledge-cross-chain-message-relaying"
  - "nahida-knowledge-atomic-cross-chain-transactions"
  - "nahida-knowledge-cross-chain-smart-contract-invocation"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/blockchain-applications"
  - "blockchain-systems/consensus/proof-of-stake-finality"
relation_edges:
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-interoperability"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "has_child"
    to: "nahida-knowledge-cross-chain-message-relaying"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "has_child"
    to: "nahida-knowledge-atomic-cross-chain-transactions"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "has_child"
    to: "nahida-knowledge-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2302-01600-metaopera-cross-metaverse-interoperability.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2302-01600-metaopera-cross-metaverse-interoperability.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-cross-chain-privacy-preserving-auditing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-trustless-cross-chain-bridges.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "bridges_to"
    to: "nahida-bridge-permissioned-consensus-to-cross-chain-bridges"
    evidence_refs:
      - "vault/05_Bridges/permissioned-consensus-to-cross-chain-bridges.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-atomic-cross-chain-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "bridges_to"
    to: "nahida-bridge-proof-of-stake-finality-to-cross-chain-protocols"
    evidence_refs:
      - "vault/05_Bridges/proof-of-stake-finality-to-cross-chain-protocols.md"
      - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/05_Bridges/distributed-transactions-to-cross-chain-smart-contract-invocation.md"
      - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-cross-chain-protocols"
    relation: "bridges_to"
    to: "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/05_Bridges/cross-chain-message-relaying-to-cross-chain-smart-contract-invocation.md"
      - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing"
  - "nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges"
  - "nahida-bridge-permissioned-consensus-to-cross-chain-bridges"
  - "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
  - "nahida-bridge-proof-of-stake-finality-to-cross-chain-protocols"
  - "nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation"
  - "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
source_note_refs:
  - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
  - "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
  - "vault/03_Sources/papers/doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency.md"
  - "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
  - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
  - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
  - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
  - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
  - "vault/03_Sources/papers/arxiv-2302-01600-metaopera-cross-metaverse-interoperability.md"
  - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
representative_source_refs:
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
  - "doi:10.1016/j.jksuci.2023.101897"
  - "arxiv:2310.10016v1"
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
  - "arxiv:2302.01600"
  - "arxiv:2310.10065"
query_keys:
  - "Cross-chain protocols"
  - "cross-chain-protocols"
  - "cross-chain transfer"
  - "cross-chain exchange"
  - "cross-chain privacy-preserving auditing"
  - "trustless cross-chain bridge"
  - "ZK light-client bridge"
  - "CLE IPA FAI"
  - "sigBridge"
  - "signature bridge"
  - "permissioned cross-chain bridge"
  - "DCCV"
  - "dynamic cross-chain data consistency verification"
  - "cross-chain data updating consistency"
  - "cross-chain messaging"
  - "cross-chain message relaying"
  - "permissionless relayers"
  - "relayer coordination"
  - "relayer task allocation"
  - "atomic cross-chain transactions"
  - "atomic cross-chain commitment"
  - "witness network atomic commitment"
  - "AC3WN"
  - "cross-chain deals"
  - "adversarial commerce"
  - "certified blockchain protocol"
  - "CBC protocol"
  - "FedChain"
  - "federated-blockchain systems"
  - "PoS-secured cross-chain transfer"
  - "Stackelberg cross-chain incentives"
  - "weakest chain security"
  - "cross-chain smart contract invocation"
  - "cross-chain contract calls"
  - "CCSCI"
  - "ShuttleCross"
  - "cross-chain hybrid concurrency control"
  - "MetaOpera"
  - "cross-metaverse interoperability"
  - "relay metaverse"
  - "metaverse object transfer"
  - "NFT wrapped metaverse assets"
  - "oracle-based metaverse interoperability"
  - "BRC-20 to Ethereum bridge"
  - "MIDAS TOUCH"
  - "Bitcoin inscriptions Ethereum smart contracts"
  - "inscription-triggered smart contract invocation"
aliases:
  - "cross-chain transfer"
  - "cross-chain exchange"
  - "cross-chain privacy-preserving auditing"
  - "trustless cross-chain bridge"
  - "sigBridge"
  - "signature bridge"
  - "DCCV"
  - "dynamic cross-chain data consistency verification"
  - "cross-chain message relaying"
  - "permissionless relayer coordination"
  - "atomic cross-chain transactions"
  - "atomic cross-chain commitment"
  - "cross-chain deals"
  - "adversarial commerce"
  - "cross-chain smart contract invocation"
  - "CCSCI"
  - "cross-metaverse interoperability"
  - "MetaOpera"
  - "relay metaverse"
  - "BRC-20 bridge"
  - "MIDAS TOUCH"
domains:
  - "blockchain-systems"
  - "zero-knowledge-proofs"
topics:
  - "cross-chain-protocols"
  - "privacy-preserving-auditing"
  - "trustless bridges"
  - "light clients"
  - "permissioned cross-chain bridges"
  - "signature-of-consensus bridge"
  - "dynamic-data-consistency-verification"
  - "audit chain"
  - "cross-chain-message-relaying"
  - "relayer-coordination"
  - "atomic-cross-chain-transactions"
  - "atomic-cross-chain-commitment"
  - "cross-chain-deals"
  - "adversarial-commerce"
  - "cross-chain-incentives"
  - "cross-chain-smart-contract-invocation"
  - "hybrid-concurrency-control"
  - "cross-metaverse-interoperability"
  - "nft-wrapped-assets"
  - "oracle-based-interoperability"
  - "bitcoin-ethereum-bridge"
  - "brc-20"
  - "inscription-based-message-relaying"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkcross"
  - "nahida-knowledge-20260620-zkbridge"
  - "nahida-knowledge-20260622-sigbridge"
  - "nahida-knowledge-20260622-dccv-dynamic-cross-chain-data-consistency"
  - "nahida-knowledge-20260622-scalable-cross-chain-messaging"
  - "nahida-knowledge-20260622-atomic-cross-chain-transactions"
  - "nahida-knowledge-20260622-cross-chain-deals"
  - "nahida-knowledge-20260622-fedchain"
  - "nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation"
  - "nahida-knowledge-20260623-metaopera-cross-metaverse-interoperability"
  - "nahida-knowledge-20260623-brc20-to-ethereum"
source_refs:
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
  - "doi:10.1016/j.jksuci.2023.101897"
  - "arxiv:2310.10016v1"
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "doi:10.1109/tsc.2023.3240235"
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
  - "arxiv:2302.01600"
  - "arxiv:2310.10065"
confidence: "medium"
trust_tier: "primary"
---

# Cross-chain protocols

## 定义与范围

- 定义: Cross-chain protocols 研究不同区块链之间如何安全地转移资产、交换资产、验证状态或执行审计，并处理原子性、隐私、可验证性和跨链信息不对称。
- 不包含: 单个系统名、某个 smart contract 实现、一次 benchmark 或某篇论文的协议符号；这些留在 `03_Sources` source note。
- Canonical terms: `cross-chain-protocols`
- Aliases/query keys: cross-chain transfer, cross-chain exchange, cross-chain privacy-preserving auditing
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解跨链协议问题，再按需打开 zkCross 或未来 zkBridge/atomic-swap sources。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

跨链协议可以是 chain-based，也可以是 bridge-based。Chain-based 方案依赖链自身机制，如 sidechains、HTLC、SPV/Merkle proofs；bridge-based 方案引入 notary、relay chain 或 audit/supervision chain。zkCross 表明，当跨链协议同时要求 privacy 和 auditing 时，不能只关注资产能否转移，还要处理三类问题: linkability exposure、privacy/auditability conflict、full auditing scalability。zkBridge 补上另一条关键路线: 跨链桥的 correctness 不应依赖小委员会签名，而可以通过 sender-chain light-client transition proof 和 receiver-chain updater contract 来实现。sigBridge 则补上 permissioned blockchain 的替代路线: 当源链 consensus nodes/public keys/signature rules 可被目标链 updater contract 使用时，bridge 可以验证 consensus signatures 或其抽样子集，而不一定生成 ZK proof。DCCV 进一步把跨链协议的对象从资产/header/audit proof 推到 dynamic data：source chain 更新数据后，target chain 是否完整、正确地同步更新，需要 audit chain、dynamic Merkle hash tree 和 decentralized chameleon hash 一起验证。Towards Scalable Cross-Chain Messaging 又补上 transport-layer 问题：即使目标链有验证机制，permissionless relayers 如何运输消息、分配任务、避免 gas-wasting races 和审查/重排，仍是跨链协议本身的设计面。Atomic Commitment Across Blockchains 则把跨链 exchange/transfer 的 all-or-nothing 语义单独拆成 [[atomic-cross-chain-transactions|atomic cross-chain transactions]]：HTLC/timelock 不是完整答案，crash、network delay、复杂交易图和跨链证据验证都需要独立记录。Cross-chain Deals 进一步把复杂交易从 swap 扩展到 broker、auction、arbitrage 等 adversarial commerce，并说明跨链原子性在恶意参与者下应以 compliant-party acceptable payoff 和 escrow liveness 表达。

FedChain 新增一条 PoS-secured federated-chain transfer 路线：destination chain 上的合约接受 source-chain SPV proof，但这个 proof 的可信度不强于 source chain 的 PoS consensus/finality。论文进一步指出 federated-blockchain 的安全受最弱链约束，所以跨链协议还要考虑 stake/reward 分布，避免某条链因 stake 稀薄而成为攻击入口。

ShuttleCross 把跨链协议从资产/消息/证明运输推进到 [[cross-chain-smart-contract-invocation|cross-chain smart contract invocation]]：origin-chain smart contract 可以触发多条 target chains 上的 contract functions，并把这些 invocations 组织成一个需要 atomicity、serializability、liveness 和低延迟的 `CTX`。这不是单纯 relayer transport，也不是资产 swap，而是跨链 execution workflow。

MetaOpera 把跨链协议的对象从 token/header/message 进一步扩展到 metaverse users and objects：它用 MetaOpera blockchain 作为 relay metaverse，把 origin metaverse 中被锁定的 avatar/asset/object 包装成 NFT，再通过 staking、committee proof 和 customizer 格式转换在目标 metaverse 中重铸。对于 decentralized metaverse，它复用 cross-chain/notary 思路；对于 centralized metaverse，它改用 multi-signature oracle 观察服务器状态，因此其持久价值是 cross-chain protocols 与 oracle-based on-chain/off-chain interoperability 的组合路线。

Bridging BRC-20 to Ethereum 新增一条 inscription-based middleware bridge：Bitcoin 用户把 operation、目标 Ethereum contract address 和参数写入 BRC-20 inscription，validator committee 扫描 Bitcoin block/transaction output、打包排序请求、运行 consensus，然后调用 Ethereum smart contract 并把 event receipt 再写回 Bitcoin。它应归入 interoperability/cross-chain-protocols，尤其连接 [[cross-chain-message-relaying|cross-chain message relaying]] 和 [[cross-chain-smart-contract-invocation|cross-chain smart contract invocation]]；原 queue 中的 transaction-processing 分类已纠正。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它能组织 transfer、exchange、bridge、relay、notary、auditing、privacy-preserving protocols 等多类 future sources。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: `zkCross`、`Θ`、`Φ`、`Ψ` 留在 source note；本节点只沉淀问题结构和方法族。
- 需要引用的更基础 Knowledge: [[interoperability|blockchain interoperability]]。
- 不应拆出的实例/协议/来源: zkCross、zkBridge、XCLAIM、MAD-HTLC、specific relay chains 默认作为 source/protocol instances。

## 解决的问题

在多链系统中让跨链 transfer/exchange/audit 同时满足原子性、unlinkability、auditability 和效率。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[interoperability|Blockchain interoperability]] | child_of | zkCross source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| cross-chain privacy-preserving auditing | section | 当前只有 zkCross 一个 source，先作为本节点章节和方法族，不单独拆 node。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] | source_extension |
| trustless cross-chain bridges | section | zkBridge 是单 source，但问题足够通用；先作为方法族章节，不拆 node。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] | source_extension |
| dynamic cross-chain data consistency verification | section | DCCV 暴露 source/target/audit chain 下的动态数据更新一致性问题；当前只有一篇 source，先作为方法族章节和 query key，不拆 node。 | [[doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency|DCCV]] | source_extension |
| [[cross-chain-message-relaying|cross-chain message relaying]] | child | relayer transport 已从验证/桥 correctness 中分离成可复用问题：任务分配、激励、timeout、censorship resistance 都不是单篇实现细节。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | active_seed |
| [[atomic-cross-chain-transactions|atomic cross-chain transactions]] | child | cross-chain exchange/asset movement 的 all-or-nothing 语义已从 privacy、bridge correctness 和 relayer transport 中分离成独立问题：commit/refund decision、timeout/crash、witness/global ledger 和 evidence validation 都是可复用设计面。 | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | active_seed |
| [[cross-chain-smart-contract-invocation|cross-chain smart contract invocation]] | child | smart-contract workflow 跨多条链调用 functions 时，问题从 transfer/message 扩展到 atomic multi-invocation execution、serializability、concurrency control 和 read-only invocation latency。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | active_seed |
| cross-metaverse object interoperability | section | MetaOpera 说明跨链/Oracle 技术可以承载 metaverse avatar/object portability，但当前只有一篇 source 且 vault 尚无稳定 metaverse 知识端点，先作为方法族和 query key。 | [[arxiv-2302-01600-metaopera-cross-metaverse-interoperability|MetaOpera]] | source_extension |
| Bitcoin-to-Ethereum inscription bridge | section | BRC-20 inscription bridge 是 relaying + invocation 的组合实例；当前只有一篇 source，先作为方法族和 bridge evidence，不拆单独知识节点。 | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | source_extension |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| HTLC-based exchange | 用 hash lock + time lock 保证双方要么都拿到资产，要么都退款。 | 跨链资产交换，双方能在两链上锁定资产。 | 同一 preimage 会暴露 linkability；不同链脚本/合约能力不同；crash/network delay 下的 timelock 窗口会造成诚实方错过 redeem。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]]; [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment]] |
| Witness-network atomic commitment | 在 permissionless witness chain 上部署协调合约，用互斥的 redeem/refund authorization state 作为所有 asset-chain contracts 的统一 commit/abort evidence。 | 多条独立链需要 all-or-nothing asset movement，且不想使用中心交易所或可信 witness。 | 需要跨链 evidence validation、confirmation depth `d`、witness-chain fork/51% attack 风险分析，以及额外 witness contract 成本。 | [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] |
| Cross-chain deal protocols | 用 escrow、tentative transfers、validation 和 commit phase 支撑 broker/auction/arbitrage 等复杂资产交易；安全目标是 compliant party 得到 acceptable payoff。 | 需要表达比 atomic swap 更复杂的业务逻辑，且参与者可偏离协议。 | Timelock route 依赖同步 timeout 和 watchtower/DoS 边界；CBC route 需要共享 certified blockchain 并承担 censorship/finality 风险。 | [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals]] |
| SPV/Merkle-proof transfer | 用源链交易 inclusion proof 支撑目标链 mint/claim。 | 链可提供区块头和 Merkle proof。 | 隐私隐藏 receiver/amount 后可能破坏直接 SPV 验证。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| ZK privacy-preserving transfer/exchange | 用 zk-SNARK 隐藏 receiver/preimage 等 linkability sources，同时让合约验证正确性。 | 跨链活动要求 unlinkability 且不想引入 trusted third party。 | 需要 proving/setup、gas、匿名集合和 denomination 设计。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| ZK audit aggregation | 把审计函数、签名验证、状态转移和 state-root 验证压缩进证明，audit chain 验证 proof。 | 多链 full auditing 需要避免逐交易检查。 | Proving 成本转移到 committer；需要至少一个 honest committer 和链共识安全阈值。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| Trustless light-client bridge | Relayer 生成 sender chain block-header/light-client transition 的 succinct proof，receiver chain updater contract 验证 proof 并维护 headers。 | 想减少 committee correctness trust，同时 receiver chain 上直接验证共识/签名过贵。 | 仍依赖 sender chain light-client verifier 正确性、proof soundness、至少一个 honest relayer 保活、应用层 Merkle/state proofs 和 gas/prover 成本。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |
| Batched header relay | 一批连续 block headers 生成统一 proof，链上只存 batch Merkle root。 | 区块头连续更新频繁，单块更新 gas/storage 成本过高。 | 增加确认等待时间；batch size 是用户体验和系统成本之间的参数。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |
| Signature-of-consensus bridge | 在 permissioned chain 中直接把源链 consensus signatures 作为 header correctness evidence；relayer 可选择满足 consensus threshold 的签名子集，updater contract 随机验证 `t` 个 signatures。 | 源链 membership/public keys/consensus rules 已知，目标链可执行签名验证且希望避免 ZK proof generation infrastructure。 | 需要 trusted initialization、relayer certificates、至少一个 honest relayer；verification cost/data size 随 signature count 增长；抽样验证存在 `epsilon = C(n-alpha,t)/C(n,t)` 错误接受概率。 | [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge]] |
| Audit-chain-based dynamic data consistency verification | source chain、target chain 和 audit chain 分别部署协作 smart contracts；source 更新动态数据后，audit chain 通过 Merkle proof 与 decentralized chameleon hash randomness 验证传输一致性和更新一致性。 | 联盟链/监管链场景中，跨链交互对象是可更新数据而不只是资产或 block headers。 | 依赖 honest audit chain/data owner、正确实现的 threshold decentralized chameleon hash、CoSi/multi-signcryption 和合约部署流程；Fabric synthetic evaluation 不等于 permissionless production bridge。 | [[doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency|DCCV]] |
| Coordinator-based relayer task allocation | 链上 Coordinator 维护 relayer set/collateral，用 hash-based allocation 把跨链消息任务分配给具体 relayer，并通过 fee、acknowledgement、timeout proof 和 slashing 建立 accountability。 | Permissionless relayers 同时竞争同一消息导致 gas waste、吞吐不可扩展或强 relayer 垄断时。 | 牺牲纯冗余；依赖 timeout/proof-of-absence、collateral 参数和链上可验证分配；复杂异构 load balancing 仍难。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] |
| 2PC-based cross-chain smart contract invocation | origin chain 作为 coordinator，target chains 暂存 dirty states，所有 invocations 成功后统一 commit，否则统一 abort。 | 跨链 workflow 由多个 contract-function invocations 组成，且需要 all-or-abort 语义。 | origin-chain decision、target-chain timeout/status polling、committee signature verification 和 inter-chain delay 是协议边界。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] |
| Hybrid cross-chain invocation concurrency control | 按 state contention 在 OCC `opList` 与 S2PL `lockList` 间动态切换，并通过 wait-for graph deadlock detection 降低高争用 abort/等待成本。 | 多个 cross-chain transactions 并发读写 target-chain state。 | 阈值 `lambda` 与 workload 相关；off-chain read fast path 仍需链上正式版本匹配。 | [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] |
| Cross-metaverse object wrapping | Origin metaverse 先锁定 object，MetaOpera relay metaverse 铸造对应 NFT；目标 metaverse 根据 staking proof 和 customizer 格式转换铸造目标 object 或 NFT-derivative。 | 需要在 decentralized metaverses 和 centralized metaverses 之间迁移 avatar、NFT、virtual assets 或对象语义。 | 安全性依赖 notary/oracle committee、lock/mint 接口、object format compatibility 和 customizer trust；不自动解决 universal data structure、policy 或 physical/virtual semantics。 | [[arxiv-2302-01600-metaopera-cross-metaverse-interoperability|MetaOpera]] |
| Inscription-based Bitcoin-to-Ethereum middleware bridge | Bitcoin inscription 携带 Ethereum 调用请求；validator committee 周期扫描、排序、共识、调用目标合约，并把 Ethereum event receipt 写回 Bitcoin inscription。 | Bitcoin-side 用户希望触发 Ethereum smart contract，但源链执行模型不是 EVM/account-based smart contract。 | One-way route；依赖 honest-majority validators、gas fee deduction、committee size/`epsilon` 参数和 receipt publication；不提供 ShuttleCross-style serializability。 | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | paper | 定义 CLE/IPA/FAI 并给出 transfer/exchange/auditing 三协议 source extension | 单 source；修改 geth/Solidity；匿名集合和 denomination 是隐私边界 | `p1-p17` |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | paper | 给出 trustless light-client bridge 路线，用 deVirgo + Groth16 让 Cosmos->Ethereum header verification 可用 | 单 source；liveness 仍需 honest relayer；性能数字依赖 2022 实验环境和 gas 假设 | `p1-p15` |
| [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control]] | paper | 给出 permissioned cross-chain bridge 路线：用 consensus signatures 和概率抽样验证替代 ZK proof，并用跨链 ABAC resource sharing 演示应用 | 单 source；依赖 trusted setup/relayer certificates/known consensus rules；signature count 增大时成本上升 | `p1-p10` |
| [[doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency|A secure dynamic cross-chain decentralized data consistency verification model]] | paper | 给出 dynamic cross-chain data consistency verification 路线：audit chain + dynamic Merkle hash tree + decentralized chameleon hash，覆盖传输完整性和更新同步一致性 | 单 source；audit chain/data owner honest assumption；Hyperledger Fabric v1.4 synthetic evaluation；不是 trustless bridge | `p1-p13` |
| [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | paper | 给出 cross-chain message relaying seed：识别 permissionless relayer race/scalability/censorship 问题，并提出 Coordinator-based task allocation 与 incentive/slashing route | 单 source；无实验评测；同步网络模型；不解决 authenticity verification 或 proof-of-absence 实现 | `p1-p8` |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | paper | 给出 atomic cross-chain transactions seed：AC2T graph、trusted witness baseline、permissionless witness-network atomic commitment、cross-chain evidence validation | arXiv preprint；分析性评估；witness-chain finality/fork/evidence validation 是关键假设 | `p1-p19` |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | paper | 给出 cross-chain deal abstraction 和 adversarial-commerce correctness vocabulary，补充 timelock 与 certified-blockchain 两条协议路线 | 理论/协议/成本模型；未做生产系统实测；CBC/timelock 的安全性依赖底层链模型 | `p1-p12` |
| [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] | paper | 新增 federated-blockchain transfer 路线：SPV proof + PoS finality + Stackelberg stake/reward distribution，共同处理跨链系统的 weakest-chain security。 | 单 source；simulation/analysis；不覆盖 arbitrary messaging/privacy/deals；真实 staking market 不一定满足模型。 | `p1-p13` |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | paper | 新增 cross-chain smart contract invocation 子问题：origin-chain 2PC、HCC、deadlock detection、dual-processing read-write separation 和 ChainMaker/TBFT evaluation。 | Manuscript proof；ChainMaker/TBFT prototype；依赖 BFT-secure chains、PKI/committee signatures、partial synchrony 和 `2f + 1` matching off-chain read results。 | `p1-p12` |
| [[arxiv-2302-01600-metaopera-cross-metaverse-interoperability|MetaOpera]] | paper | 新增 cross-metaverse object interoperability 路线：relay metaverse + NFT wrapping/staking/reminting + notary/oracle committee + customizer format conversion。 | arXiv preprint；PoC/simulation；security depends on committee/oracle observation, platform lock/mint APIs and object-format/policy compatibility。 | `p1-p10` |
| [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | paper | 新增 inscription-triggered invocation route：MIDAS TOUCH 用 validator middleware 将 Bitcoin BRC-20 inscriptions 转换为 Ethereum smart contract calls，并把 receipts 写回 Bitcoin。 | arXiv preprint；one-way Bitcoin -> Ethereum；validator-faithfulness 是 trust boundary；Bitcoin-side evaluation 有成本限制。 | `p1-p10` |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，仅覆盖当前 vault 已有 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前 cross-chain protocols 节点有七条 source-backed 路线。zkCross 说明跨链协议需要同时处理 asset movement/exchange atomicity、receiver/preimage/amount linkability 和 full auditing scalability。zkBridge 说明跨链桥的 correctness 可以从 committee signatures 转移到 light-client transition proof verification，但 liveness、finality/orphan policy、application state proofs 和 fee incentives 仍属于区块链系统层。sigBridge 说明在 permissioned setting 中，known membership 和 consensus signatures 可以成为另一种 verification material：它省掉 ZK proof generation，但把成本/风险转成 signature verification gas、签名数量扩展、trusted initialization 和抽样验证概率边界。DCCV 说明还有一类互操作问题是动态数据更新后的跨链一致性：源链允许授权改写/更新时，目标链的副本必须被可审计地同步更新。Scalable Cross-Chain Messaging 进一步说明，即使 verification 正确，消息运输层仍会因 permissionless relayer redundancy 产生 race、gas waste、non-scaling throughput 和 reordering/censorship 风险。Atomic Commitment Across Blockchains 新增的父级信号是跨链原子性：多链资产交易需要一个共同的 redeem/refund decision，而这个 decision 的 trust、fork/finality 和 evidence-validation 边界应由 [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] 承接。Cross-chain Deals 修正了这一子问题的业务边界：跨链协议还要表达 broker/auction/arbitrage 等多步 deal，并在 adversarial participants 下保护 compliant parties，而不是只追求简单 atomic swap。

- FedChain delta: FedChain 把 cross-chain protocols 的安全边界从“能否验证 inclusion proof”推进到“source chain finality 是否足够可信、stake 是否在多条链上均衡分布”。这不改变 atomic/message/privacy 子结构，但新增一条 PoS finality -> cross-chain protocols bridge。
- ShuttleCross delta: ShuttleCross 把 cross-chain protocols 的对象从 asset/message/proof 推进到 smart-contract workflow execution。它新增 [[cross-chain-smart-contract-invocation|cross-chain smart contract invocation]] 子节点，并通过 distributed-transactions bridge 记录 2PC/OCC/S2PL/serializability 如何迁移到独立 BFT chains 的 invocation setting。
- MetaOpera delta: MetaOpera 把 cross-chain protocols 的对象从 blockchain-native assets/messages 推到 metaverse objects。它没有改变现有 child 结构，但新增一条 source-backed route：当目标对象是 avatar/NFT/virtual item 时，互操作协议需要同时处理 lock/mint exclusivity、NFT representation、off-chain oracle observation、customizer-mediated format conversion 和 platform policy compatibility。
- BRC-20 bridge delta: Bridging BRC-20 to Ethereum 把 cross-chain protocols 的对象从 generic message/contract workflow 具体化为 Bitcoin inscription -> Ethereum contract call。它新增的不是 source-named child，而是一条 bridge-backed composition: source-chain inscription relaying 负责 intent transport，target-chain smart contract invocation 负责执行，receipt inscriptions 负责反馈。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | 新增 CLE/IPA/FAI、ZK transfer/exchange、ZK audit aggregation 路线 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 吸收 zkBridge、atomic cross-chain swaps、universal atomic swaps 后复核 child split |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | 新增 trustless light-client bridge、batched header relay、committee-trust boundary 路线 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 吸收 IBC/light-client bridge/optimistic bridge sources 后复核 child split |
| [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control]] | 新增 permissioned signature-of-consensus bridge 路线：用源链 consensus signatures 和 updater contract 抽样验证替代 ZK proof；同时给出 cross-chain ABAC resource-sharing 应用 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no new node | 后续吸收 IBC/PoA/permissioned-bridge sources 后复核是否拆 `permissioned cross-chain bridges` child |
| [[doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency|A secure dynamic cross-chain decentralized data consistency verification model]] | 新增 dynamic cross-chain data consistency verification 路线：audit chain 周期检查传输完整性，并在 source-chain 动态更新后检查 target-chain 是否同步更新 | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合 | no new node | 吸收 BeDCV/DCIV/dynamic data auditing sources 后复核是否拆 `dynamic cross-chain data consistency verification` child 或建立 DA/storage bridge |
| [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | 新增 cross-chain message relaying 子问题：permissionless relayers 的 race/scalability/censorship risk，以及 Coordinator + hash allocation + incentive/slashing route | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; 缺口与队列 | yes | 吸收 IBC relayer、cross-chain smart-contract invocation、relayer MEV/QoS sources 后复核子结构 |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | 新增 atomic cross-chain transactions 子问题：AC2T graph、witness-network atomic commitment、cross-chain evidence validation 和 witness-chain fork-depth/attack-economics 边界。 | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 下一篇 Cross-chain Deals 吸收后复核 atomic cross-chain transactions 的 safety/liveness vocabulary |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | 新增 cross-chain deal route：复杂资产交易、acceptable payoff safety、timelock path signatures、CBC/global-ledger proof 和半同步去中心化边界。 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; 缺口与队列 | no new node | 继续补 universal atomic swaps、IBC/production relayers 和 bridge finality sources |
| [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] | 新增 PoS-secured federated-chain transfer route：SPV transfer 的 correctness 依赖各链 PoS consensus，Stackelberg dynamic rewards 用于降低 weakest-chain/stake-centralization 风险。 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no new child | 后续吸收 PoS sidechains/IBC/interchain staking/bridge finality sources 后复核 `federated-blockchain systems` 是否拆 node |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | 新增 CCSCI 子问题：跨链 smart-contract workflow 需要 atomicity、serializability、liveness 和低延迟；用 2PC、HCC、deadlock detection 和 read-write separation 作为 seed route。 | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 GPACT/2PC4BC/EOVPC/Avalon/IBC callback sources 后复核 child split |
| [[arxiv-2302-01600-metaopera-cross-metaverse-interoperability|MetaOpera]] | 新增 cross-metaverse object interoperability route：跨链/Oracle 思路被用于 DM/CM metaverse 之间的 avatar/object portability，协议组合为 relay metaverse、NFT wrapping、staking/reminting 和 customizer format conversion。 | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; 缺口与队列 | no new child | 等待更多 metaverse interoperability / virtual object standard / oracle integration sources 后复核是否拆 `cross-metaverse interoperability` child 或新 domain |
| [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | 新增 inscription-based Bitcoin-to-Ethereum middleware bridge，并创建 relaying -> invocation bridge；纠正 queue path 从 transaction-processing 到 cross-chain-protocols。 | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no new child | 吸收 Bitcoin light-client bridge、BRC-20 production bridge 或 bidirectional invocation source 后复核是否拆 `Bitcoin/EVM interoperability` child |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-cross-chain-privacy-preserving-auditing|zk-SNARKs -> cross-chain privacy-preserving auditing]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, privacy, auditability, implementation_reuse | ZK succinctness/zero-knowledge transfers; cross-chain atomicity, SPV/HTLC semantics, denomination policy and audit-chain incentives are blockchain-specific. | active_seed |
| [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, succinct_verification, soundness, performance_compression | Proof soundness/succinctness transfers; bridge liveness, sender-chain finality, application state semantics and relayer incentives remain blockchain-specific. | active_seed |
| [[permissioned-consensus-to-cross-chain-bridges|Permissioned consensus -> cross-chain bridges]] | `blockchain-systems/consensus/permissioned-blockchain-consensus; blockchain-systems/interoperability/cross-chain-protocols` | dependency, application, verification_material | Consensus signatures/known validators transfer as bridge verification material; they do not by themselves solve relayer liveness, trusted setup, Merkle transaction proof validity, or heterogeneous consensus abstraction. | active_seed |
| [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | translation, trust_model_shift, coordination, dependency | Atomic commit structure transfers; trusted coordinator, shared recovery log and crash-only failure assumptions do not transfer unchanged to adversarial independent ledgers. | active_seed |
| [[distributed-transactions-to-cross-chain-smart-contract-invocation|Distributed transactions -> cross-chain smart contract invocation]] | `distributed-systems/transaction-processing/distributed-transactions; blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | translation, coordination, concurrency_control, trust_model_shift | 2PC/OCC/S2PL vocabulary transfers; independent BFT ledgers, origin-chain coordination, timeout polling and on-chain visibility change the correctness boundary. | active_seed |
| [[cross-chain-message-relaying-to-cross-chain-smart-contract-invocation|Cross-chain message relaying -> cross-chain smart contract invocation]] | `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying; blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | dependency, transport_to_execution, receipt_flow, trust_boundary | Relaying can carry source-chain intent and target-chain receipts; it does not automatically solve target invocation atomicity, serializability, permissionless allocation or bidirectionality. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-cross-chain-protocols | is_a | nahida-knowledge-blockchain-interoperability | vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md | medium | active_seed |
| nahida-knowledge-cross-chain-protocols | has_child | nahida-knowledge-cross-chain-message-relaying | vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | has_child | nahida-knowledge-atomic-cross-chain-transactions | vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | bridges_to | nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing | vault/05_Bridges/zk-snarks-to-cross-chain-privacy-preserving-auditing.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | bridges_to | nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges | vault/05_Bridges/zk-snarks-to-trustless-cross-chain-bridges.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md | sigBridge source note | high | active_seed |
| nahida-knowledge-cross-chain-protocols | bridges_to | nahida-bridge-permissioned-consensus-to-cross-chain-bridges | vault/05_Bridges/permissioned-consensus-to-cross-chain-bridges.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency.md | DCCV source note | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md | Scalable Cross-Chain Messaging source note | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md | Atomic Commitment source note | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md | Cross-chain Deals source note | high | active_seed |
| nahida-knowledge-cross-chain-protocols | bridges_to | nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions | vault/05_Bridges/distributed-transactions-to-atomic-cross-chain-transactions.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | has_child | nahida-knowledge-cross-chain-smart-contract-invocation | vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md | ShuttleCross source note | high | active_seed |
| nahida-knowledge-cross-chain-protocols | bridges_to | nahida-bridge-distributed-transactions-to-cross-chain-smart-contract-invocation | vault/05_Bridges/distributed-transactions-to-cross-chain-smart-contract-invocation.md | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/arxiv-2302-01600-metaopera-cross-metaverse-interoperability.md | MetaOpera source note | high | active_seed |
| nahida-knowledge-cross-chain-protocols | evidenced_by | vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md | BRC-20 to Ethereum source note | high | active_seed |
| nahida-knowledge-cross-chain-protocols | bridges_to | nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation | vault/05_Bridges/cross-chain-message-relaying-to-cross-chain-smart-contract-invocation.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Universal atomic swaps、XCLAIM、production IBC/relay-chain source 缺。 | Cross-chain Deals 已补 deal-based safety/liveness，但仍缺 HTLC graph route、production finality 和真实 relayer 生态对照。 | nahida-update | high | queued |
| permissioned cross-chain bridge foundations 仍薄。 | sigBridge 是单 source seed，尚不能代表 Fabric/Quorum/PoA/Consortium-chain bridge 设计全貌。 | nahida-update or nahida-research-search | medium | queued |
| decentralized access control / ABAC application foundation 缺。 | sigBridge 的 ABAC resource-sharing 是应用证据，不足以建立完整 access-control 知识节点。 | nahida-research-search | medium | queued |
| dynamic cross-chain data consistency verification 仍是单 source seed。 | DCCV 引入 audit-chain + dynamic-MHT + decentralized-chameleon-hash 路线，但还缺 BeDCV/DCIV、动态 PDP/POR 和实际跨链数据更新部署对照。 | nahida-update or nahida-research-search | medium | queued |
| PoS sidechain/interchain staking/bridge finality sources 缺。 | FedChain 是单 source seed，说明 PoS finality 和 stake distribution 会影响跨链 transfer，但还不足以代表全部 PoS bridge/federated-chain design。 | nahida-update / nahida-research-search | medium | queued |
| CCSCI direct sources 缺。 | ShuttleCross 已建立 cross-chain smart contract invocation 子问题，但 GPACT/2PC4BC/EOVPC/Avalon/IBC callback 等 direct sources 尚未进入 vault。 | nahida-update / nahida-research-search | high | queued |
| Cross-metaverse interoperability 仍是单 source seed。 | MetaOpera 证明 metaverse object/avatar portability 可以映射到 cross-chain/oracle protocol 问题，但还缺 metaverse data standards、identity standards、production platform bridges 和 policy/security sources。 | nahida-update / nahida-research-search | medium | queued |
| Bitcoin/EVM inscription bridge 仍是单 source seed。 | MIDAS TOUCH 证明 inscription-triggered invocation route 可行，但还缺 production BRC-20 bridge、trustless Bitcoin verification、bidirectional invocation 和 validator incentive/slashing 对照。 | nahida-update / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkcross | Created cross-chain protocols problem node and added zkCross source extension. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkbridge | Added trustless light-client bridge route and zkBridge source extension. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-sigbridge | Added sigBridge as permissioned signature-of-consensus bridge source extension and linked it to permissioned blockchain consensus. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-dccv-dynamic-cross-chain-data-consistency | Added DCCV as dynamic cross-chain data consistency verification source extension and corrected queue path from transaction-processing to interoperability/cross-chain-protocols. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-scalable-cross-chain-messaging | Added cross-chain message relaying child node and relayer coordination route from Scalable Cross-Chain Messaging. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-atomic-cross-chain-transactions | Added atomic cross-chain transactions child node and witness-network atomic commitment route from Atomic Commitment Across Blockchains. | arxiv:1905.02847v2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-cross-chain-deals | Added cross-chain deal protocol route and adversarial-commerce correctness vocabulary, routed through atomic cross-chain transactions without creating a source-named child. | doi:10.14778/3364324.3364326 | codex |
| 2026-06-22 | nahida-knowledge-20260622-shuttlecross-cross-chain-smart-contract-invocation | Added cross-chain smart contract invocation child node and linked ShuttleCross through distributed transaction/concurrency-control bridge. | sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72 | codex |
| 2026-06-23 | nahida-knowledge-20260623-metaopera-cross-metaverse-interoperability | Added cross-metaverse object interoperability as a source extension without creating a single-paper child node. | arxiv:2302.01600 | codex |
| 2026-06-23 | nahida-knowledge-20260623-brc20-to-ethereum | Added inscription-based Bitcoin-to-Ethereum bridge route, connected relaying to invocation, and corrected queue classification from transaction-processing. | arxiv:2310.10065 | codex |
