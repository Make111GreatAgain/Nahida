---
id: "nahida-bridge-kzg-commitments-to-fair-data-exchange"
title: "KZG commitments -> fair data exchange"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "polynomial-commitments"
topic_ids:
  - "kzg-commitments"
  - "fair-data-exchange"
  - "verifiable-encryption-under-committed-key"
endpoint_knowledge_refs:
  - "nahida-knowledge-kzg-commitments"
  - "nahida-knowledge-fair-data-exchange"
endpoint_paths:
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
  - "blockchain-systems/data-availability-and-light-clients/fair-data-exchange"
relation_types:
  - "dependency"
  - "application"
  - "cryptographic_enabler"
  - "selective_opening_route"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
representative_source_refs:
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
query_keys:
  - "KZG FDE"
  - "KZG fair data exchange"
  - "VECK KZG"
  - "committed data exchange"
  - "selective opening fair exchange"
aliases:
  - "KZG-to-FDE"
  - "VECK for KZG commitments"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "kzg-commitments"
  - "fair-data-exchange"
  - "data-availability-service-incentives"
tags:
  - "nahida/bridge"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-atomic-fair-data-exchange"
source_refs:
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
confidence: "high"
trust_tier: "primary"
---

# KZG commitments -> fair data exchange

## 关系命题

KZG commitments enable fair data exchange when the exchange problem is “pay for data under a known commitment.” [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] uses KZG commitments as the cryptographic anchor for VECK: the server proves off-chain that ciphertexts encrypt evaluations of the committed polynomial, while the blockchain only enforces payment for the corresponding decryption key.

This bridge does not mean KZG alone gives fairness. KZG supplies succinct commitment/opening structure; VECK supplies verifiable encryption; the blockchain payment environment supplies atomic payment/key release.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[kzg-commitments|KZG commitments]] | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | polynomial commitment backend for committed data, batch openings and subset openings | pairing-based PCS with succinct opening proofs |
| [[fair-data-exchange|Fair data exchange for committed data]] | `blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | blockchain-mediated exchange of payment for correct data under a commitment | committed-data service/retrieval problem |

## Transfer Matrix

| From KZG / PCS | Transfers to FDE? | How | Boundary |
| --- | --- | --- | --- |
| Constant-size commitment | yes | client can hold a short commitment to large data and use it as the exchange anchor | does not prove server will serve data |
| Evaluation/opening semantics | yes | ciphertext correctness is stated as “encryptions match evaluations of the committed polynomial” | requires VECK proof, not plain KZG verification alone |
| Batch/subset openings | yes | a client can request only selected data evaluations/fragments | subset handling adds protocol machinery and proof costs |
| Pairing/SRS assumptions | yes, as dependency | security inherits KZG setup/pairing assumptions | deployments with FRI/IPA commitments need different VECK constructions |
| Ethereum blob commitments | yes, as application route | EIP-4844/Danksharding retain KZG commitments after blob expiry | blob retention, archival-node economics and DA sampling remain blockchain-specific |

## Non-Transfer Boundary

- KZG does not enforce payment fairness, timeout, or key release; that is the blockchain/adaptor-signature layer.
- KZG does not hide data; hiding before payment comes from VECK zero-knowledge/encryption.
- FDE is not a data availability sampling protocol. It pays for serving already committed data or fragments.
- The bridge is currently KZG-specific because the paper instantiates VECK for KZG; other commitments such as FRI/IPA require separate source evidence.
- The paper's VECK constructions are source-local seeds, not yet a full Nahida foundation for all verifiable encryption.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] §1 | KZG chosen for constant-size commitments, batchable openings and Danksharding fit | one source |
| Same source §3 | VECK formalizes encryption under committed key | VECK is newly defined by this paper |
| Same source §5.1-§5.3 | ElGamal/Paillier VECK constructions for KZG evaluations | implementation overhead remains high |
| Same source §5.2 | subset openings for KZG-committed data | proof machinery more complex |
| Same source §8 and Appendix A.3 | Danksharding/EIP-4844 data retrieval application | DA foundation not complete in this source alone |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[kzg-commitments|KZG commitments]] | Add FDE/VECK usage extension and bridge link | done |
| [[fair-data-exchange|Fair data exchange for committed data]] | Create topic seed with VECK and KZG dependency | done |
| [[data-availability-and-light-clients|Data availability and light clients]] | Add expired blob / committed-data retrieval incentive route | done |
| [[data-availability-sampling|Data availability sampling]] | Add boundary note: FDE serves DA retrieval but is not DAS | done |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| KZG commitment/opening | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | `blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | cryptographic dependency | 2024/418 §1, §5 | confusing commitment correctness with payment fairness |
| subset opening | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | `fair-data-exchange` | selective download route | 2024/418 §5.2 | assuming all commitment schemes support the same route |
| Ethereum blob KZG commitments | `kzg-commitments` | `data-availability/light-clients/fair-data-exchange` | application route | 2024/418 §1, §8 | EIP-4844 foundation still thin |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[fair-data-exchange|Fair data exchange for committed data]] | new problem node | source passes split gate as reusable problem and future queued sources will revisit it | active_seed |
| [[kzg-commitments|KZG commitments]] | source extension and bridge link | KZG receives a committed-data-exchange usage extension | active_seed |
| [[data-availability-and-light-clients|Data availability and light clients]] | method and representative source | FDE adds a service-incentive/retrieval route | active_seed |
| [[data-availability-sampling|Data availability sampling]] | source extension boundary | FDE applies to DA retrieval but is not a DAS construction | active_seed |

## 查询入口

- KZG 在 Fair Data Exchange 中起什么作用?
- VECK 为什么需要 commitment?
- FDE 和 data availability sampling 是什么关系?
- EIP-4844 的 KZG blob commitment 如何支持过期数据付费检索?
- KZG 能否直接替代区块链支付公平性?

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-atomic-fair-data-exchange | Created KZG-to-FDE bridge from 2024/418. | 1 source note | codex |

