---
id: "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
title: "Cross-chain message relaying -> cross-chain smart contract invocation"
original_title: "Cross-chain message relaying -> cross-chain smart contract invocation"
file_slug: "cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "intra_domain_problem_composition"
bridge_status: "active_seed"
endpoint_paths:
  - "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying"
  - "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation"
endpoint_knowledge_refs:
  - "nahida-knowledge-cross-chain-message-relaying"
  - "nahida-knowledge-cross-chain-smart-contract-invocation"
from_domain: "blockchain-systems"
to_domain: "blockchain-systems"
from_direction: "interoperability"
to_direction: "interoperability"
from_topic: "cross-chain-message-relaying"
to_topic: "cross-chain-smart-contract-invocation"
relation_types:
  - "dependency"
  - "transport_to_execution"
  - "receipt_flow"
  - "trust_boundary"
directionality: "one_way_with_feedback"
relationship_thesis: "Cross-chain message relaying can serve as the transport layer for cross-chain smart contract invocation: source-chain requests are detected, ordered and delivered to a target-chain execution layer, while target-chain receipts are relayed back to the source side. The transfer is not automatic: invocation correctness still depends on target-chain execution semantics, validator/relayer trust, fee accounting and receipt finality."
transferability: "medium_high"
non_transfer_boundary: "Message transport patterns transfer, but they do not by themselves provide cross-chain transaction atomicity, serializability, target-contract correctness, permissionless relayer allocation or bidirectional interoperability. MIDAS TOUCH currently covers one-way Bitcoin inscription requests triggering Ethereum smart contracts through a validator committee, not general CCSCI concurrency control."
evidence_window_start: "2023"
evidence_window_end: "2026-06-23"
domains:
  - "blockchain-systems"
topics:
  - "cross-chain-message-relaying"
  - "cross-chain-smart-contract-invocation"
  - "bitcoin-ethereum-bridge"
  - "brc-20"
  - "receipt-relaying"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
  - "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
  - "vault/03_Sources/papers/sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation.md"
knowledge_refs:
  - "nahida-knowledge-cross-chain-message-relaying"
  - "nahida-knowledge-cross-chain-smart-contract-invocation"
relation_edges:
  - from: "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
    relation: "connects"
    to: "nahida-knowledge-cross-chain-message-relaying"
    evidence_refs:
      - "vault/05_Bridges/cross-chain-message-relaying-to-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
    relation: "connects"
    to: "nahida-knowledge-cross-chain-smart-contract-invocation"
    evidence_refs:
      - "vault/05_Bridges/cross-chain-message-relaying-to-cross-chain-smart-contract-invocation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2310-10065-bridging-brc20-to-ethereum.md"
    confidence: "high"
    status: "active_seed"
query_keys:
  - "cross-chain message relaying to smart contract invocation"
  - "inscription-triggered smart contract invocation"
  - "Bitcoin inscriptions Ethereum contract calls"
  - "MIDAS TOUCH BRC-20 bridge"
  - "receipt relaying cross-chain invocation"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-brc20-to-ethereum"
source_refs:
  - "arxiv:2310.10065"
  - "arxiv:2310.10016v1"
  - "sha256:46e621e4288cb2804673fde0e4ebd0d8b40be196596dac8071ee38c5ff13be72"
confidence: "high"
trust_tier: "primary"
---

# Cross-chain message relaying -> cross-chain smart contract invocation

## 命名与路径

- Original title: Cross-chain message relaying -> cross-chain smart contract invocation
- File slug: `cross-chain-message-relaying-to-cross-chain-smart-contract-invocation`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

[[cross-chain-message-relaying|Cross-chain message relaying]] 关注 source chain 事件、交易收据、区块头或应用消息如何被 relayer/validator/transport layer 发现、排序、提交、确认和回执。[[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]] 关注跨链消息抵达后，目标链 smart contract function 如何被执行，并如何处理 atomicity、serializability、liveness 和执行状态边界。

这条 bridge 记录的是更窄的组合关系: message relaying 可以成为 smart contract invocation 的前置运输层，负责把 source-chain intent 搬到 target-chain execution layer；target-chain invocation 完成后，再把 receipt 或 acknowledgement 搬回 source side。

## 连接命题

- From: `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying`
- To: `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation`
- Relation types: dependency, transport_to_execution, receipt_flow, trust_boundary
- Directionality: `one_way_with_feedback`
- Relationship thesis: Cross-chain message relaying can serve as the transport layer for cross-chain smart contract invocation: source-chain requests are detected, ordered and delivered to a target-chain execution layer, while target-chain receipts are relayed back to the source side. The transfer is not automatic: invocation correctness still depends on target-chain execution semantics, validator/relayer trust, fee accounting and receipt finality.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[cross-chain-message-relaying|Cross-chain message relaying]] | `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying` | source-chain request discovery, batching, ordering, delivery, acknowledgement/receipt transport | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]]; [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | active_seed |
| [[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]] | `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | target-chain contract function execution triggered by cross-chain intent | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]]; [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Source request scanning | Detecting target-chain invocation intent from source-chain records | MIDAS TOUCH scans Bitcoin transactions and parses BRC-20 inscriptions | Scanning does not verify arbitrary source-chain consensus beyond the assumed Bitcoin security model. |
| Batch ordering | Ordered delivery into target-chain execution | Validators bundle inscriptions every `epsilon` block heights and sort by timestamp before consensus | Ordering policy is middleware-defined; it is not target-chain serializability. |
| Committee agreement | Relayer/validator agreement before target invocation | MIDAS TOUCH uses a validator committee and PBFT-style consensus example | Trust shifts to honest-majority validators; this is weaker than trustless light-client verification. |
| Target contract invocation | Cross-chain message becomes Ethereum contract call | Inscription fields include target contract address, operation and parameters | This is one-way Bitcoin to Ethereum invocation, not a general multi-chain CTX model. |
| Receipt relaying | Target-chain result is acknowledged back to source side | Ethereum events are cached and published back to Bitcoin as receipt inscriptions | Receipt finality and user interpretation remain protocol/application responsibilities. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Source-chain intent | `cross-chain-message-relaying` | `cross-chain-smart-contract-invocation` | inscription/request payload carries target contract address, operation and parameters | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | Payload parsing errors, inscription standards drift and unsupported target contracts can break execution. |
| Relayer ordering | `cross-chain-message-relaying` | `cross-chain-smart-contract-invocation` | validator committee batches and orders requests before Ethereum execution | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | Middleware ordering is not equivalent to target-chain transaction serializability. |
| Acknowledgement flow | `cross-chain-message-relaying` | `cross-chain-smart-contract-invocation` | Ethereum events are cached as receipts and later posted back to Bitcoin | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | Receipt visibility depends on validators and Bitcoin inclusion latency. |
| Relayer incentive/accountability | `cross-chain-message-relaying` | `cross-chain-smart-contract-invocation` | gas fees are deducted from inscription value and distributed to validators | [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | Fee distribution helps liveness but does not remove validator-faithfulness assumptions. |

## 类比、依赖或关系边界

MIDAS TOUCH shows a practical composition: Bitcoin users express Ethereum contract calls in BRC-20 inscriptions, a validator committee reads and orders those inscriptions, and Ethereum contract execution produces receipts that can be written back to Bitcoin. This makes message relaying a concrete precursor to invocation.

The boundary is equally important. The system does not provide ShuttleCross-style multi-invocation atomicity, HCC serializability, bidirectional invocation, permissionless relayer task allocation, or trustless light-client correctness. It is best recorded as an inscription-based source extension that connects transport and invocation, not as a replacement for either endpoint.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[arxiv-2310-10065-bridging-brc20-to-ethereum|Bridging BRC-20 to Ethereum]] | direct evidence that source-chain inscription relaying can trigger target-chain smart contract invocation and return receipts | active_seed |
| [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | endpoint foundation for relayer coordination and transport-layer risks | supporting |
| [[sha256-46e621e4288c-shuttlecross-cross-chain-smart-contract-invocation|ShuttleCross]] | endpoint foundation for the broader CCSCI problem and its stronger atomicity/serializability goals | supporting |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying` | add source extension for inscription scanning, committee batching and receipt relaying | active_seed |
| `blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation` | add adjacent source extension for inscription-triggered Ethereum contract calls | active_seed |
| `blockchain-systems/interoperability/cross-chain-protocols` | add route row for inscription-based Bitcoin-to-Ethereum middleware bridge | active_seed |

## 查询入口

- Bitcoin inscription 如何触发 Ethereum smart contract?
- BRC-20 bridge 属于 relaying 还是 smart contract invocation?
- receipt inscription 在跨链调用里解决什么问题?
- MIDAS TOUCH 与 ShuttleCross 的边界有什么不同?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: 以后出现 BRC-20 bridge production implementation、trustless Bitcoin light-client bridge、bidirectional Bitcoin/EVM invocation、permissionless relayer allocation 或 inscription standard change 时，复核 relation type、trust boundary 和 endpoint maturity。

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[cross-chain-message-relaying|Cross-chain message relaying]] | Source extension, method row, bridge link | MIDAS TOUCH uses validators to scan Bitcoin inscriptions, batch/order requests and publish receipts. | active_seed |
| [[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]] | Source extension, bridge link | MIDAS TOUCH lets Bitcoin-side inscriptions trigger Ethereum smart contract operations. | active_seed |
| [[cross-chain-protocols|Cross-chain protocols]] | Method route and representative source | The paper adds an inscription-based one-way Bitcoin-to-Ethereum middleware bridge. | active_seed |

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、trust boundary 或 bridge maturity；尤其 Bitcoin light-client verification、BRC-20 standards evolution、Ethereum receipt proof semantics、permissionless validators 或 bidirectional invocation sources。
