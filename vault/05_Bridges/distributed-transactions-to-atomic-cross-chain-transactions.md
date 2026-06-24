---
id: "nahida-bridge-distributed-transactions-to-atomic-cross-chain-transactions"
title: "Distributed transactions -> atomic cross-chain transactions"
original_title: "Distributed transactions -> atomic cross-chain transactions"
file_slug: "distributed-transactions-to-atomic-cross-chain-transactions"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_domain_method_translation"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/transaction-processing/distributed-transactions"
  - "blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions"
endpoint_knowledge_refs:
  - "nahida-knowledge-distributed-transactions"
  - "nahida-knowledge-atomic-cross-chain-transactions"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "transaction-processing"
to_direction: "interoperability"
from_topic: "distributed-transactions"
to_topic: "atomic-cross-chain-transactions"
relation_types:
  - "translation"
  - "trust_model_shift"
  - "coordination"
  - "dependency"
directionality: "one_way_with_feedback"
relationship_thesis: "Atomic commit and two-phase-commit style coordination structure can be translated from distributed transactions into cross-chain asset movement, but independent adversarial ledgers cannot assume a trusted coordinator, shared recovery log, uniform failure model, or globally enforceable all-or-nothing correctness. Atomic cross-chain protocols must externalize decisions into mutually verifiable evidence and, for adversarial commerce, express safety as compliant parties receiving acceptable payoffs while escrowed assets remain live."
transferability: "medium"
non_transfer_boundary: "The reusable part is the coordination skeleton: escrow/lock-like resource control, validation, and some form of commit/abort/redeem/refund decision. Traditional 2PC trust, blocking, coordinator recovery, crash-only failures, local log assumptions, serializability-style isolation, and global all-or-nothing correctness do not transfer unchanged. Cross-chain settings add adversarial participants, independent ledgers, acceptable-payoff safety, smart-contract fees, finality/fork probabilities, relayer/evidence transport, and per-chain validation constraints."
evidence_window_start: "2019"
evidence_window_end: "2019"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "distributed-transactions"
  - "atomic-cross-chain-transactions"
  - "atomic-commit"
  - "cross-chain-protocols"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
  - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
knowledge_refs:
  - "nahida-knowledge-distributed-transactions"
  - "nahida-knowledge-atomic-cross-chain-transactions"
query_keys:
  - "distributed transactions atomic cross-chain transactions"
  - "atomic commit across blockchains"
  - "two-phase commit cross-chain"
  - "witness network atomic commitment"
  - "AC3WN"
  - "cross-chain deals"
  - "adversarial commerce"
  - "acceptable payoff safety"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-atomic-cross-chain-transactions"
  - "nahida-knowledge-20260622-cross-chain-deals"
source_refs:
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
confidence: "high"
trust_tier: "primary"
---

# Distributed transactions -> atomic cross-chain transactions

## 命名与路径

- Original title: Distributed transactions -> atomic cross-chain transactions
- File slug: `distributed-transactions-to-atomic-cross-chain-transactions`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

[[distributed-transactions|Distributed transactions]] 关注一个 logical transaction 跨多个参与方或分区时，如何保持共同的 commit/abort 结果。[[atomic-cross-chain-transactions|Atomic cross-chain transactions]] 关注多条独立区块链之间的资产转移或交换如何满足 all-or-nothing 语义。

这条 bridge 记录的不是“2PC 直接可以放到区块链上”。它记录的是更窄的迁移命题：atomic commit / transaction coordination 的结构可以迁移，但传统 trusted coordinator、crash-only failure、blocking/recovery log 和全局 all-or-nothing correctness 必须替换为链上可验证、互斥且跨链可携带的 commit/refund/abort evidence，或替换为 compliant-party acceptable payoff 这类 adversarial-commerce safety 语义。

## 连接命题

- From: `distributed-systems/transaction-processing/distributed-transactions`
- To: `blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions`
- Relation types: translation, trust_model_shift, coordination, dependency
- Directionality: `one_way_with_feedback`
- Relationship thesis: Atomic commit and two-phase-commit style coordination structure can be translated from distributed transactions into cross-chain asset movement, but independent adversarial ledgers cannot assume a trusted coordinator, shared recovery log, uniform failure model, or globally enforceable all-or-nothing correctness. Atomic cross-chain protocols must externalize decisions into mutually verifiable evidence and, for adversarial commerce, express safety as compliant parties receiving acceptable payoffs while escrowed assets remain live.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[distributed-transactions|Distributed transactions]] | `distributed-systems/transaction-processing/distributed-transactions` | atomic commit, commit/abort decision, sub-transaction coordination | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] uses 2PC/AC3 framing | active_seed |
| [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] | `blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | cross-chain asset movement/deals, witness/CBC authorization, evidence validation, compliant-party safety | [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]]; [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals]] | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Global commit/abort decision | cross-chain redeem/refund authorization | Atomic Commitment §3-§4 | Decision must be represented as chain-verifiable evidence, not a private coordinator message. |
| Transaction correctness vocabulary | compliant-party acceptable payoff and escrow liveness | Cross-chain Deals §1-§2 | Global all-or-nothing is not enforceable when arbitrary parties may deviate. |
| Participant yes vote / contract publication | each asset chain smart contract is published and locks assets | Atomic Commitment §3-§4 | Publishing on different chains has heterogeneous latency/finality and fee dynamics. |
| Coordinator/witness role | trusted witness baseline or permissionless witness network | Atomic Commitment §4.1-§4.2 | Trusted witness is a centralization baseline; witness network adds fork/finality assumptions. |
| Shared decision log | certified blockchain commit/abort proof | Cross-chain Deals §6 | Semi-synchronous liveness requires a shared ledger/CBC, so full decentralization does not transfer. |
| Mutual exclusion | `RDauth` and `RFauth` cannot both become stable authorization states | Atomic Commitment §4.2, §5.1 | Fork depth and evidence acceptance policy determine practical safety. |
| Recovery/abort path | refund all contracts when not all contracts are published | Atomic Commitment §4.2 | Liveness depends on asset chains accepting refund evidence and participants/relayers submitting it. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Atomic commit | `distributed-systems/transaction-processing/distributed-transactions` | `blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | AC2T graph sub-transactions share a single redeem/refund decision | Atomic Commitment §3 | Cross-chain participants may be adversarial; chains cannot assume common coordinator trust. |
| Coordinator decision | distributed transaction coordinator | witness smart contract state | `SCw` transitions from `P` to either `RDauth` or `RFauth` | Atomic Commitment §4.2 | Witness chain forks can create conflicting evidence unless depth `d` is enforced. |
| All-or-nothing correctness | classical atomicity | compliant-party acceptable payoff | each compliant party must get an acceptable payoff even if deviating parties behave arbitrarily | Cross-chain Deals §2.2 | Some non-all-or-nothing outcomes are acceptable; correctness is local to compliant parties. |
| Contract votes | participant yes votes | asset-chain smart-contract publication | all contracts published and correct before redeem authorization | Atomic Commitment §4.2 | Cross-chain evidence validation is expensive and chain-specific. |
| Isolation / non-interference | serializability-like isolation | anti-double-spending escrow | escrow contract owns assets while deal is active, preventing concurrent sale of the same asset | Cross-chain Deals §1, §4 | Full serializability/snapshot isolation is not the right cross-chain deal abstraction. |
| Abort/refund | transaction abort | global `RFauth` evidence accepted by all asset contracts | any participant can request refund authorization while `SCw` remains `P` | Atomic Commitment §4.2 | Refund liveness still depends on submitting evidence to every involved chain. |
| Commit latency analysis | sequential 2PC-style coordination concern | parallel publication/redeem with witness decision | AC3WN latency modeled as `4 * Delta` vs Herlihy `2 * Delta * Diam(D)` | Atomic Commitment §6.1 | Analytical model abstracts real fee markets, heterogeneous finality and relayer behavior. |

## 类比、依赖或关系边界

The bridge is medium-transferability. Distributed transaction concepts provide the vocabulary for atomicity, commitment, sub-transactions, escrow/locking, validation and commit/abort, but blockchains change the failure, trust and correctness models. A cross-chain coordinator cannot simply be a database coordinator unless all participants trust it. AC3TW shows the centralized baseline; AC3WN shows one decentralization route by making a permissionless witness network publish the mutually exclusive decision. Cross-chain Deals shows the complementary semantic boundary: in adversarial commerce, a protocol may not be able to enforce global all-or-nothing, so the realizable target is that compliant parties end with acceptable payoff and their escrowed assets remain live. These routes do not remove all assumptions: they shift them to witness/CBC finality, timeout choice, censorship/DoS, cross-chain evidence verification and application-specific payoff validation.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | direct evidence for translating atomic commit into witness-network coordinated cross-chain asset movement | active_seed |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | direct evidence for replacing classical all-or-nothing correctness with compliant-party acceptable payoff and for timelock/CBC deal protocols | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/transaction-processing/distributed-transactions` | add bridge link, witness-network atomic-commit method row and source extension | active_seed |
| `blockchain-systems/interoperability/cross-chain-protocols/atomic-cross-chain-transactions` | add deal-safety vocabulary, timelock/CBC method rows and bridge link | active_seed |
| `blockchain-systems/interoperability/cross-chain-protocols` | add cross-chain deal route, source extension and bridge link | active_seed |

## 查询入口

- distributed transactions 和 atomic cross-chain transactions 有什么关系?
- 2PC 为什么不能直接用于开放区块链跨链交易?
- AC3WN 如何把 commit/abort 决策变成链上证据?
- witness network atomic commitment 的安全边界是什么?
- cross-chain deals 为什么不能只按经典 all-or-nothing atomic transactions 理解?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: universal atomic swaps、classic 2PC/atomic commit foundation、production bridge/finality source 改变任一端点、relation type、transfer boundary 或 bridge maturity。

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[distributed-transactions|Distributed transactions]] | Methods, representative sources, bridge links | Atomic Commitment shows atomic commit translated to adversarial independent ledgers | active_seed |
| [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] | Refreshed node | Atomicity is a reusable cross-chain problem; Cross-chain Deals adds adversarial-commerce safety/liveness semantics | active_seed |
| [[cross-chain-protocols|Cross-chain protocols]] | Child structure, methods, bridge links | Adds atomicity route under cross-chain protocols | active_seed |

## 刷新规则

- Last checked: `2026-06-22`
- Valid until: `2026-07-22`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity；尤其 universal atomic swaps、witness/global-ledger protocols、CBC/finality/evidence-validation sources。
