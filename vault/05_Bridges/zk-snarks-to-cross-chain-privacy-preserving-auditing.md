---
id: "nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing"
title: "zk-SNARKs -> cross-chain privacy-preserving auditing"
original_title: "zk-SNARKs -> cross-chain privacy-preserving auditing"
file_slug: "zk-snarks-to-cross-chain-privacy-preserving-auditing"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_domain_method_transfer"
bridge_status: "active_seed"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "blockchain-systems/interoperability/cross-chain-protocols"
endpoint_knowledge_refs:
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-cross-chain-protocols"
from_domain: "zero-knowledge-proofs"
to_domain: "blockchain-systems"
from_direction: "proof-systems"
to_direction: "interoperability"
from_topic: "zk-snarks"
to_topic: "cross-chain-protocols"
relation_types:
  - "application"
  - "privacy"
  - "auditability"
  - "implementation_reuse"
directionality: "from_zk_snarks_to_cross_chain_protocols"
relationship_thesis: "zk-SNARK zero-knowledge can hide cross-chain linkability sources such as receiver addresses and HTLC preimage relations, while succinct verification can compress full auditing into proof verification. The cross-chain part still requires blockchain-specific mechanisms: SPV/Merkle proofs, HTLC atomicity, denominations, state roots, audit-chain incentives, committer assumptions, and gas/proving tradeoffs."
transferability: "medium-high"
non_transfer_boundary: "ZK proof properties transfer as privacy/verifiability tools; they do not by themselves provide cross-chain atomicity, state availability, honest committer guarantees, anonymity set size, denomination design, or audit-chain consensus/security."
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "zk-snarks"
  - "cross-chain-protocols"
  - "privacy-preserving-auditing"
source_note_refs:
  - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
knowledge_refs:
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-cross-chain-protocols"
query_keys:
  - "zk-SNARKs -> cross-chain privacy-preserving auditing"
  - "zk-SNARK cross-chain auditing"
  - "ZK cross-chain privacy"
  - "zkCross bridge"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkcross"
source_refs:
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
confidence: "high"
trust_tier: "primary"
---

# zk-SNARKs -> cross-chain privacy-preserving auditing

## 命名与路径

- Original title: zk-SNARKs -> cross-chain privacy-preserving auditing
- File slug: `zk-snarks-to-cross-chain-privacy-preserving-auditing`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

[[zk-snarks|zk-SNARKs]] 是证明系统族，提供 zero-knowledge、succinct proof 和低成本 verification 等能力。[[cross-chain-protocols|Cross-chain protocols]] 是 blockchain interoperability 的问题族，关注不同链之间的 transfer、exchange、state verification 和 auditing。

这个 bridge 的重点是区分“ZK 能力”和“跨链语义”。zk-SNARK 能隐藏 receiver/preimage/witness 并压缩验证；但资产原子性、交易 inclusion、state root、审计链激励、committer 诚实性、gas 成本和匿名集合不是 zk-SNARK 自动提供的，需要 cross-chain protocol 设计。

## 连接命题

- From: `zero-knowledge-proofs/proof-systems/zk-snarks`
- To: `blockchain-systems/interoperability/cross-chain-protocols`
- Relation types: application, privacy, auditability, implementation_reuse
- Directionality: `from_zk_snarks_to_cross_chain_protocols`
- Relationship thesis: zk-SNARK zero-knowledge can hide cross-chain linkability sources such as receiver addresses and HTLC preimage relations, while succinct verification can compress full auditing into proof verification. The cross-chain part still requires blockchain-specific mechanisms: SPV/Merkle proofs, HTLC atomicity, denominations, state roots, audit-chain incentives, committer assumptions, and gas/proving tradeoffs.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks|zk-SNARKs]] | `zero-knowledge-proofs/proof-systems/zk-snarks` | proof-system capability provider | zkCross uses zk-SNARK/Groth16, but not as foundation definition | active_seed |
| [[cross-chain-protocols|Cross-chain protocols]] | `blockchain-systems/interoperability/cross-chain-protocols` | application/problem endpoint | zkCross transfer/exchange/audit protocols | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Zero-knowledge hiding of witness | cross-chain transfer/exchange unlinkability | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] p7-p12 | Metadata, amount uniqueness, and anonymity set are outside the proof system. |
| Succinct verification | audit-chain full auditing | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] p9-p14 | Proving cost and circuit construction move to committers; verification gas remains an engineering boundary. |
| Circuitized state transition/audit function | privacy-preserving auditing | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] p9-p11 | Correctness depends on state roots, signatures, chain consensus and committer data availability. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| zk-SNARK zero-knowledge | `zero-knowledge-proofs/proof-systems/zk-snarks` | `blockchain-systems/interoperability/cross-chain-protocols` | Hide receiver address, sender address, HTLC preimage relationship, and transaction details as private inputs. | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] | Does not hide unique amounts or small anonymity sets by itself. |
| zk-SNARK succinctness | `zero-knowledge-proofs/proof-systems/zk-snarks` | `blockchain-systems/interoperability/cross-chain-protocols` | Replace per-transaction audit with proof verification over aggregated state transitions. | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] | Setup/prove costs and on-chain verification gas still matter. |

## 类比、依赖或关系边界

The proof system is the privacy and compression mechanism; the cross-chain protocol is the system contract. A good query answer should not say “zk-SNARKs solve cross-chain auditing” without naming the required blockchain pieces: SPV/Merkle proofs, HTLC, state roots, audit chain, committers, denominations and consensus thresholds.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | source-backed application and transfer boundary | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/zk-snarks` | update Bridge Links and relation_edges; no foundation upgrade | active_seed |
| `blockchain-systems/interoperability/cross-chain-protocols` | update Bridge Links and relation_edges | active_seed |

## 查询入口

- zk-SNARKs -> cross-chain privacy-preserving auditing
- zk-SNARK cross-chain auditing
- ZK cross-chain privacy
- zkCross bridge

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: zkBridge, private atomic swaps, rollup bridge auditing, production proof verification gas, or new source changing the privacy/auditability boundary.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[zk-snarks|zk-SNARKs]] | Bridge Links only | zkCross uses zk-SNARKs but does not define the proof-system foundation | active_seed |
| [[cross-chain-protocols|Cross-chain protocols]] | Methods, Source Extensions, Bridge Links | zkCross is primary cross-chain privacy/auditing source | active_seed |
| [[blockchain-applications|ZKP blockchain applications]] | Methods, Source Extensions, Bridge Links | Source is ZKP blockchain application evidence | active_seed |

## 刷新规则

- Last checked: `2026-06-20`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
