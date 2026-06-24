---
id: "arxiv-2310-10065-bridging-brc20-to-ethereum"
title: "Bridging BRC-20 to Ethereum"
original_title: "Bridging BRC-20 to Ethereum"
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
  - "p1-p10 full extracted text"
  - "Abstract, Sections I-VII, Algorithm 1, references"
canonical_url: "https://arxiv.org/abs/2310.10065"
doi: ""
arxiv_id: "2310.10065"
venue: "arXiv preprint"
year: "2023"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "interoperability"
topic_ids:
  - "cross-chain-protocols"
  - "bitcoin-ethereum-bridge"
  - "brc20-bridge"
  - "inscription-based-message-relaying"
  - "cross-chain-smart-contract-invocation"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols"
secondary_ontology_paths:
  - "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-message-relaying"
  - "blockchain-systems/interoperability/cross-chain-protocols/cross-chain-smart-contract-invocation"
path_update_status: "corrected_from_queue"
classification_corrected_from: "blockchain-systems/execution-and-transactions/transaction-processing"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
  directions:
    - "interoperability"
  topics:
    - "cross-chain-protocols"
    - "cross-chain-message-relaying"
    - "cross-chain-smart-contract-invocation"
    - "bitcoin-ethereum-bridge"
domains:
  - "blockchain-systems"
topics:
  - "cross-chain-protocols"
  - "bitcoin-ethereum-bridge"
  - "brc-20"
  - "bitcoin-inscriptions"
  - "cross-chain-message-relaying"
  - "cross-chain-smart-contract-invocation"
  - "validator-committee-bridge"
aliases:
  - "MIDAS TOUCH"
  - "BRC-20 to Ethereum bridge"
  - "Bitcoin inscriptions to Ethereum smart contracts"
  - "inscription-triggered smart contract invocation"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "blockchain-systems/interoperability"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "interoperability"
  problem:
    - "connecting Bitcoin's UTXO and inscription model to Ethereum's account-based smart contracts"
    - "allowing Bitcoin users to trigger Ethereum contract operations without holding Ethereum addresses"
    - "transporting inscription requests and receipts across heterogeneous blockchains"
  method_family:
    - "middleware bridge"
    - "validator committee relaying"
    - "multi-signature validation"
    - "BRC-20 inscription parsing"
    - "receipt inscription publication"
  system_layer:
    - "cross-chain protocols"
    - "cross-chain message relaying"
    - "cross-chain smart contract invocation"
  evaluation_context:
    - "Ethereum testnet smart contract operations"
    - "committee-size scalability analysis"
    - "gas consumption by contract functionality"
    - "epsilon block-interval checking tradeoff"
  application:
    - "Bitcoin BRC-20 assets"
    - "Ethereum smart contracts"
    - "DeFi contract interactions"
authors:
  - "Guangsheng Yu"
  - "Qin Wang"
knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
  - "nahida-knowledge-blockchain-interoperability"
  - "nahida-knowledge-cross-chain-protocols"
  - "nahida-knowledge-cross-chain-message-relaying"
  - "nahida-knowledge-cross-chain-smart-contract-invocation"
bridge_refs:
  - "nahida-bridge-cross-chain-message-relaying-to-cross-chain-smart-contract-invocation"
source_refs:
  - "arxiv:2310.10065"
source_identity_key: "arxiv:2310.10065"
local_pdf_path: "~/Desktop/paper/2310.10065.pdf"
raw_text_path: "vault/02_Raw/pdf/extracted/2310.10065-351731b705f9-pages.txt"
pdf_sha256: "351731b705f9045495edec7caf969d86236bf66461d89f6d45ec6f9bf47b3278"
pages: 10
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_id: "nahida-knowledge-20260623-brc20-to-ethereum"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0091"
confidence: "high"
trust_tier: "primary"
---

# Bridging BRC-20 to Ethereum

## Paper Identity

- Source: Guangsheng Yu and Qin Wang, "Bridging BRC-20 to Ethereum", arXiv preprint, 2023.
- arXiv: `2310.10065`.
- Local PDF: `~/Desktop/paper/2310.10065.pdf`.
- Extraction: `vault/02_Raw/pdf/extracted/2310.10065-351731b705f9-pages.txt`.
- Read scope: full extracted text, pages 1-10.

## One-Sentence Summary

本文提出 `MIDAS TOUCH`，一个轻量级单向 middleware bridge：用户在 Bitcoin 侧用 BRC-20/inscription 写入 Ethereum contract address、operation 和参数，validator committee 扫描并聚合 inscriptions，通过 multi-signature validation 调用 Ethereum smart contracts，最后把 Ethereum events 作为 receipt inscriptions 写回 Bitcoin。

## Absorption Decision

队列原路径 `blockchain-systems/execution-and-transactions/transaction-processing` 需要修正。本文确实讨论 state update、gas 和 validator processing，但核心问题不是区块链内部 transaction execution/concurrency control，而是 Bitcoin 和 Ethereum 两个异构生态之间的 interoperability。

稳定吸收路径为:

```text
blockchain-systems / interoperability / cross-chain-protocols
```

它还作为两个已有子问题的桥接证据:

- [[cross-chain-message-relaying|Cross-chain message relaying]]: validator committee 扫描 Bitcoin inscriptions、构造 bundle、排序、共识并广播 receipts。
- [[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]]: Bitcoin 侧 inscription 触发 Ethereum smart contract function/state update，但它不是 ShuttleCross 那种 origin-chain contract workflow。

`MIDAS TOUCH` 和 `BRC-20 bridge` 不应单独升级成知识节点；它们是 source instance / source extension。

## Structured Summary

### Problem

Bitcoin 采用 UTXO 模型，Ethereum 采用 account/state + smart contract 模型。BRC-20/Ordinals 让 Bitcoin 上的 satoshi 可以携带 inscription metadata，但 BRC-20 token 不能直接使用 Ethereum 的 EVM、ERC-20/DeFi 和智能合约生态。本文要解决的是: 如何在不重建 Polkadot/Cosmos 式生态、不使用复杂 ZK/TEE/HTLC 路线的情况下，让 Bitcoin 用户通过 inscriptions 触发 Ethereum 合约动作。

### Core Idea

MIDAS TOUCH 利用 BRC-20 inscription 的可编辑字段作为跨链请求载体。用户在 Bitcoin transaction output 中嵌入 operation、target Ethereum contract address、参数和 deposit/gas 信息；middleware validators 周期性扫描 Bitcoin blocks，把有效 inscriptions 组成 bundle，在 committee 内达成共识，然后对 Ethereum 上的目标合约做 multi-signature invocation。Ethereum 合约执行后发出 events，validators 再把这些 events 作为 receipt inscriptions 发布回 Bitcoin，形成一个 U-shaped workflow。

### Claimed Contributions

| Contribution | Paper evidence | Nahida handling |
| --- | --- | --- |
| Lightweight Bitcoin-Ethereum middleware | p1, §III | source extension under [[cross-chain-protocols|Cross-chain protocols]] |
| BRC-20 inscriptions as cross-chain request format | p2-p5 | source detail; query key for future BRC-20 sources |
| Validator committee with deposits and multi-signature validation | p4-p7 | message-relaying / bridge evidence |
| Prototype and partial evaluation | p7-p9 | source evidence only; not production proof |
| Security discussion around settlement/liveness/fairness | p8-p9 | assumptions and boundaries in source note |

## Detailed Outline

| Section | Pages | Role |
| --- | --- | --- |
| Abstract + I Introduction | p1-p2 | Motivation: Bitcoin and Ethereum are isolated; contributions and U-shaped workflow. |
| II Before Construction | p2-p3 | BRC-20, smart contracts, Ethereum token standards, existing interoperability routes, assumptions. |
| III Middleware Construction | p3-p5 | Technical challenges, roles, system overview and detailed construction. |
| IV Implementation | p5-p7 | Registration, deploy and receipt operations; Algorithm 1. |
| V Evaluation and Analysis | p7-p9 | Scalability, gas consumption, checking frequency, security analysis. |
| VI Limitation Discussion | p9 | One-way utility, one-side evaluation, non-comparison, validator faithfulness. |
| VII Conclusion | p9-p10 | Summary and claim of first attempt to expand BRC-20 capabilities. |

## Technical Content

### BRC-20 and Inscription Model

The paper treats BRC-20 as a Bitcoin-native token standard parallel to ERC-20, enabled by Ordinals and inscriptions. BRC-20 supports:

| Operation | Meaning |
| --- | --- |
| `deploy` | Create a new token type with fields such as `tick`, `max` and `lim`. |
| `mint` | Increase supply subject to token limits. |
| `transfer` | Move token balance between Bitcoin addresses. |

The paper's key move is to add middleware-specific fields such as an operation signature and Ethereum `caddr` so that a Bitcoin inscription can name a target Ethereum contract and a function-like operation.

### Roles

| Role | Chain/layer | Function |
| --- | --- | --- |
| Transaction originator | Bitcoin | Creates inscription requests containing contract address and operation data. |
| Contract owner | Ethereum | Defines smart contract interfaces that inscriptions may invoke. |
| Validator | Middleware | Registers with deposit, scans Bitcoin, validates inscriptions, updates Ethereum state and publishes receipts. |
| Operator | Middleware | Configures committee size, block intervals, multi-signature rules, security parameters and upgrades. |

The paper notes that validators, operators and Ethereum contract owners may be the same group in a typical deployment.

### U-Shaped Workflow

1. A Bitcoin user publishes an inscription that includes an operation, Ethereum smart contract address and values.
2. Validators monitor Bitcoin blocks, parse outputs, identify inscriptions and add valid inscriptions to bundle `B`.
3. Every `epsilon` Bitcoin block heights, validators sort the bundle by timestamp and run a committee consensus process.
4. Validators fetch Ethereum contract state `S` and Bitcoin-address balance mapping `Psi`.
5. The requested contract operation is invoked on Ethereum with multi-signature validation.
6. Gas fee is deducted from inscription value and distributed to validators.
7. Ethereum contract events are cached as receipt set `Lambda`.
8. Validators publish receipt inscriptions back to Bitcoin.

This receipt step is central to settlement: only inscription requests included in a receipt are considered successfully committed.

### Algorithm 1

Algorithm 1 contains three procedures:

| Procedure | Role |
| --- | --- |
| `MainFunc()` | Iterates Bitcoin blocks, parses transaction outputs, builds bundles, periodically updates EVM state and publishes receipts. |
| `CommitteeRegistration()` | Waits for validators that bind Bitcoin and Ethereum addresses and deposit enough ETH. |
| `UpdateEVMState(B, S, Psi, g)` | Deducts gas, distributes validator rewards, checks contract interfaces and invokes operations with multi-sig validation. |
| `HandleInscription(ins)` | Extracts operation, contract address and values from inscriptions. |

The algorithm is intentionally high-level. It does not specify a full consensus protocol beyond using committee consensus and examples such as PBFT in evaluation.

## Assumptions and Threat Model

| Assumption | Scope | Consequence |
| --- | --- | --- |
| Bitcoin and Ethereum consensus robustness | Both chains | Fewer adversarial nodes than each chain's security threshold; consistency and liveness hold. |
| Smart contract abstraction | Ethereum | Contracts can be deployed, update state, reach state consensus and answer state queries. |
| Cryptographic primitives | Middleware | Signatures, multisignatures and hash functions are unforgeable/collision-resistant in the conventional sense. |
| Majority honesty | Blockchain nodes and middleware committee | The majority of validators faithfully execute scanning, validation, invocation and receipt publication. |

The middleware inherits chain safety/liveness only under these assumptions. Validator compromise is explicitly a concern, addressed only by deposits/slashing and possibly larger/dynamic committees.

## Evaluation

### Scalability

The paper evaluates committee size from 1 to 20 and treats committee sizes below 4 as centralized because no consensus process is performed. It uses PBFT as the committee consensus example. The conclusion is qualitative but important: after committee size reaches 4, speed decreases non-linearly because PBFT has `O(n^2)` message complexity, so committee size is a decentralization/performance tradeoff.

### Gas Consumption

The paper compares additional gas/value needed for different Ethereum contract functionality categories:

| Contract type | Qualitative result |
| --- | --- |
| FT | Lowest additional value because token transfer is simple. |
| NFT | Higher because metadata, uniqueness and royalties may be involved. |
| Stablecoin | Generally simple, but peg mechanics can add complexity. |
| Insurance / Loan / Auction | More complex due to policy terms, interest/risk/recovery or bid management. |
| DAO | Highest complexity due to governance, voting and fund management. |

The takeaway is not a universal gas benchmark; it is that the bridge's extra value/gas model depends heavily on the target smart contract type.

### Frequency of Checking

The parameter `epsilon` controls how often validators invoke `UpdateEVMState` by Bitcoin block heights:

- `epsilon = 1` means every Bitcoin block is checked and pushed through to Ethereum.
- Larger `epsilon` accumulates more inscriptions before an EVM update.
- Larger `epsilon` reduces time-related overhead but increases resource-related overhead due to storage and sorting of larger bundles.

This makes `epsilon` a batching/latency/resource tradeoff.

## Security Discussion

| Property | Paper's argument | Boundary |
| --- | --- | --- |
| Safety / settlement | A request lifecycle is marked by a Bitcoin inscription request and a later Bitcoin receipt inscription. Ethereum execution requires majority validator multi-signature endorsement. | Safety depends on honest-majority validators, correct receipt publication and Ethereum contract correctness. |
| Liveness | Valid Bitcoin-side actions eventually reflect in Ethereum if chains and majority validators function correctly. | No liveness guarantee if committee stalls or validator majority is unavailable/malicious. |
| Fairness | Valid transactions that conform to rules and pay gas should be reflected without discrimination. | The paper does not fully formalize ordering fairness, fee priority or MEV-style validator behavior. |

## Limitations

The paper's own limitations are important:

- **One-direction**: The bridge is Bitcoin -> Ethereum. It does not support Ethereum -> Bitcoin or a general bidirectional bridge.
- **One-side evaluation**: The evaluation focuses on Ethereum testnet smart contract behavior. The Bitcoin side is not fully evaluated because batch Bitcoin transactions were costly.
- **Not a general comparison**: The paper emphasizes enhancing BRC-20 with Ethereum tooling, not fully competing with all cross-chain bridge designs.
- **Validator faithfulness**: The middleware remains sensitive to validator trust. Deposits such as `32 ETH`, larger committees and dynamic formation are mitigations, not a complete trustless solution.

## Knowledge Handoff

| Target | Update |
| --- | --- |
| [[interoperability|Blockchain interoperability]] | Add Bitcoin/Ethereum heterogeneity and inscription-based bridge as a source-backed application route. |
| [[cross-chain-protocols|Cross-chain protocols]] | Add BRC-20-to-Ethereum one-way middleware bridge route; correct queue classification away from transaction-processing. |
| [[cross-chain-message-relaying|Cross-chain message relaying]] | Add validator committee inscription scanning, bundling, sorting, consensus and receipt publication as a source extension. |
| [[cross-chain-smart-contract-invocation|Cross-chain smart contract invocation]] | Add inscription-triggered Ethereum contract invocation as an adjacent source extension, with boundary that origin is not a smart contract. |
| [[cross-chain-message-relaying-to-cross-chain-smart-contract-invocation|Cross-chain message relaying -> cross-chain smart contract invocation]] | New bridge: relaying layer transports inscription requests/receipts; invocation layer executes target smart contract state updates. |

## Cold-Start Hierarchy Discovery

| Facet | Candidate | Evidence | Handling |
| --- | --- | --- | --- |
| Domain | `blockchain-systems` | Bitcoin/Ethereum interoperability, validators, smart contracts | active |
| Direction | `interoperability` | paper frames Bitcoin/Ethereum isolation and bridge middleware | active |
| Problem | `cross-chain-protocols` | middleware bridge, validator committee, receipt settlement | active |
| Subproblem | `cross-chain-message-relaying` | scanning inscriptions, bundling, publishing receipts | source extension |
| Subproblem | `cross-chain-smart-contract-invocation` | Bitcoin-side inscriptions trigger Ethereum contract functions | source extension / bridge endpoint |
| Foundation concepts | BRC-20, Bitcoin inscriptions, smart contract token standards | used but not enough to create standalone foundation nodes | queued/watch |
| Source instance | MIDAS TOUCH | named system and algorithm | source-only |

## Retrieval Optimization

This note should help future queries about:

- BRC-20 to Ethereum bridge design.
- Bitcoin inscription-based interoperability.
- One-way cross-chain middleware.
- Relation between relayer/message transport and smart contract invocation.
- Validator-committee trust boundary in lightweight bridge designs.

Future agents should answer most MIDAS TOUCH questions from this source note and most taxonomy questions from [[cross-chain-protocols|Cross-chain protocols]] plus the new bridge.

## Domain Dynamics Impact

Affected L1 domain: `blockchain-systems`.

Decision: `unchanged`. The paper adds a narrow source extension inside interoperability. It does not by itself refresh the domain-level `research-dynamics.md`, though BRC-20/inscription bridges become a watch term for future interoperability dynamics.

## Review Items

| Item | Reason | Status |
| --- | --- | --- |
| Queue path corrected | Original queue path pointed to transaction-processing; deep read shows interoperability is primary. | resolved |
| BRC-20 foundation node | Paper uses BRC-20 and Ordinals but does not provide a stable enough foundation pack. | queued |
| Production security evidence | Prototype/partial evaluation is not production bridge evidence. | queued |

## Update Log

| Date | Run ID | Change |
| --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-brc20-to-ethereum | Deep-read source note created and handed off to Source + Knowledge + Bridge absorption. |
