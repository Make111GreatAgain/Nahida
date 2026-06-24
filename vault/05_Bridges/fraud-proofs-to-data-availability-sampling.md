---
id: "nahida-bridge-fraud-proofs-to-data-availability-sampling"
title: "Fraud proofs -> data availability sampling"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
topic_ids:
  - "fraud-proofs"
  - "data-availability-sampling"
  - "light-client-security"
endpoint_knowledge_refs:
  - "nahida-knowledge-fraud-proofs"
  - "nahida-knowledge-data-availability-sampling"
endpoint_paths:
  - "blockchain-systems/data-availability-and-light-clients/fraud-proofs"
  - "blockchain-systems/data-availability-and-light-clients/data-availability-sampling"
relation_types:
  - "dependency"
  - "complementarity"
  - "validation_boundary"
  - "light_client_security"
directionality: "bidirectional"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
representative_source_refs:
  - "arxiv:1809.09044v1"
query_keys:
  - "fraud proofs data availability"
  - "fraud proofs need data availability"
  - "data availability proofs vs fraud proofs"
  - "codec fraud proofs"
  - "2D Reed-Solomon DAS fraud proof"
aliases:
  - "Fraud proofs and DAS"
  - "fraud proof data availability bridge"
domains:
  - "blockchain-systems"
topics:
  - "fraud-proofs"
  - "data-availability-sampling"
  - "light-client-security"
  - "erasure-coded-blocks"
tags:
  - "nahida/bridge"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-fraud-proofs-data-availability"
source_refs:
  - "arxiv:1809.09044v1"
  - "doi:10.48550/arxiv.1809.09044"
confidence: "high"
trust_tier: "primary"
---

# Fraud proofs -> data availability sampling

## 关系命题

Fraud proofs and data availability sampling are complementary light-client security mechanisms. [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] shows the dependency in both directions: fraud proofs let light clients reject invalid state transitions or malformed erasure coding, but honest full nodes can only generate those fraud proofs if the relevant block data is available; DAS gives light clients probabilistic evidence that enough encoded data was published, but DAS alone does not prove transaction execution validity.

This bridge therefore records a validation boundary, not a merge of the two concepts. Fraud proofs answer “can someone show this object violates the rules?” DAS answers “is enough data available for someone honest to reconstruct and challenge the object?”

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[fraud-proofs|Fraud proofs]] | `blockchain-systems/data-availability-and-light-clients/fraud-proofs` | refutation mechanism for invalid transitions, malformed coding, or optimistic candidates | short proof of rule violation |
| [[data-availability-sampling|Data availability sampling]] | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | light-client mechanism for checking that encoded block data is recoverable without downloading all data | random sampling over encoded data |

## Transfer Matrix

| Mechanism | Transfers across endpoint? | How | Boundary |
| --- | --- | --- | --- |
| State transition fraud proof | yes, depends on DAS | full nodes need block data, transactions and witnesses to produce the invalid-transition proof | proof format remains execution-model-specific |
| Data availability sampling | yes, enables fraud proofs | random samples and gossip/reconstruction make hidden data detectable and recoverable | sampling does not prove state validity |
| Codec fraud proof | yes, sits between both endpoints | a row/column proof refutes malformed 2D Reed-Solomon extended data used by DAS | proof size grows with axis length unless replaced by succinct proof |
| 2D Reed-Solomon roots | yes | row/column roots under `dataRoot` let light clients authenticate sampled shares and codec proofs | assumes the encoded data structure is included in the block commitment |
| Succinct validity proofs | partial alternative | can replace some state-transition or codec fraud proofs | cannot replace data availability; unavailable data still blocks verification/reconstruction |
| Selective disclosure countermeasures | yes, network boundary | unlinkable/randomized sample requests reduce adversary's ability to serve only sampled shares | depends on network model, gossip and anti-eclipse assumptions |

## Non-Transfer Boundary

- Fraud proofs are not data availability proofs. A valid fraud proof can reject an invalid block, but the absence of a fraud proof is meaningful only if data was available to challengers.
- DAS is not execution validity. A block can be data-available and still contain an invalid state transition.
- A codec fraud proof protects the erasure-coded availability layer; it does not validate application transactions.
- Validity proofs can remove some fraud-proof duties, but they do not remove the need to publish data needed by clients and applications.
- Sharded ledgers can reuse this pattern for shard-local invalidity detection, but shard assignment, cross-shard atomicity and execution semantics remain separate problems.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] Abstract and §1 | light-client security goal under dishonest-majority producers | one central seed source |
| Same source §3 | assumptions: at least one honest full node, honest light-client sampling mass, bounded delay, anti-eclipse | strong network assumptions remain |
| Same source §4 | state transition fraud proof with execution traces and sparse Merkle witnesses | requires fraud-proof-friendly block structure |
| Same source §5.1-§5.5 | 2D Reed-Solomon DAS and codec fraud proofs | proof size is not constant |
| Same source §5.6-§5.7 | probability/security analysis for missing shares and detection | selective disclosure requires enhanced model |
| Same source §7.1 | succinct proofs can replace some fraud proofs but not availability proofs | ZK/validity-proof bridge still needs more sources |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[fraud-proofs|Fraud proofs]] | Create method-family seed and record DAS dependency | done |
| [[data-availability-sampling|Data availability sampling]] | Add 2D Reed-Solomon DAS, codec fraud proof and data-available-before-challenge boundary | done |
| [[data-availability-and-light-clients|Data availability and light clients]] | Add fraud proofs as a child mechanism and update open gaps | done |
| [[data-availability-to-sharded-ledgers|Data availability -> sharded ledgers]] | Record shard/light-client invalidity detection as a transfer pattern | done |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| data-available-before-fraud-proof principle | `fraud-proofs` | `data-availability-sampling` | dependency | Fraud Proofs §5 | treating absence of challenge as validity without availability |
| codec fraud proof | `fraud-proofs` | `data-availability-sampling` | validation_boundary | Fraud Proofs §5.5 | confusing coding correctness with transaction validity |
| 2D Reed-Solomon sampling | `data-availability-sampling` | `fraud-proofs` | enabling condition | Fraud Proofs §5.2-§5.7 | assuming network sampling is robust without anti-eclipse/selective-disclosure defenses |
| validity-proof alternative | `fraud-proofs` | `data-availability-sampling` | partial substitution | Fraud Proofs §7.1 | forgetting that validity proofs do not publish data |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[fraud-proofs|Fraud proofs]] | definition, methods, bridge links | source passes split gate as reusable method family | active_seed |
| [[data-availability-sampling|Data availability sampling]] | methods, representatives, bridge links | Fraud Proofs adds 2D RS DAS and codec fraud proofs | active_seed |
| [[data-availability-and-light-clients|Data availability and light clients]] | child structure and current synthesis | fraud proofs become a child mechanism under light-client security | active_seed |
| [[data-availability-to-sharded-ledgers|Data availability -> sharded ledgers]] | transfer boundary | sharded systems use DA/fraud-proof pattern when no single node validates all shards | active_seed |

## 查询入口

- fraud proofs 为什么需要 data availability?
- data availability sampling 能不能证明交易有效?
- codec fraud proof 和 state transition fraud proof 有什么区别?
- validity proof 能否替代 fraud proof 和 DAS?
- sharding 中为什么需要 fraud/DA proof 组合?

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-fraud-proofs-data-availability | Created bridge between fraud proofs and data availability sampling from Fraud Proofs. | 1 source note | codex |
