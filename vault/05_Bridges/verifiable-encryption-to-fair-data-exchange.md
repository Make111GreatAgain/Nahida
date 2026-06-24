---
id: "nahida-bridge-verifiable-encryption-to-fair-data-exchange"
title: "Verifiable encryption -> fair data exchange"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "verifiable-encryption"
  - "fair-data-exchange"
  - "payment-key-release"
endpoint_knowledge_refs:
  - "nahida-knowledge-verifiable-encryption"
  - "nahida-knowledge-fair-data-exchange"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/verifiable-encryption"
  - "blockchain-systems/data-availability-and-light-clients/fair-data-exchange"
relation_types:
  - "dependency"
  - "application"
  - "payment_protocol_enabler"
  - "cryptographic_enabler"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
  - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
representative_source_refs:
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
query_keys:
  - "verifiable encryption fair exchange"
  - "VECK"
  - "SAVER FDE"
  - "fair data exchange ciphertext proof"
  - "payment key release verifiable encryption"
aliases:
  - "VE-to-FDE"
  - "VECK boundary"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "verifiable-encryption"
  - "fair-data-exchange"
tags:
  - "nahida/bridge"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-saver-verifiable-encryption"
source_refs:
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
confidence: "medium"
trust_tier: "primary"
---

# Verifiable encryption -> fair data exchange

## 关系命题

Verifiable encryption is a cryptographic enabler for fair data exchange when the protocol needs the client to verify that a ciphertext hides data consistent with a known commitment before payment/key release. [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] uses the commitment-specific variant VECK for this purpose; [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] provides a broader SNARK-friendly verifiable-encryption seed that explains the generic proof/encryption composition problem.

This bridge does not collapse the two endpoints. Verifiable encryption supplies ciphertext correctness and sometimes verifiable decryption; fair data exchange additionally requires payment atomicity, timeout/key-release logic, commitment-specific constructions, and adversarial commerce assumptions.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[verifiable-encryption|Verifiable encryption]] | `zero-knowledge-proofs/proof-systems/verifiable-encryption` | prove encrypted plaintext satisfies relation or matches committed data | encryption plus proof/ciphertext consistency |
| [[fair-data-exchange|Fair data exchange for committed data]] | `blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | exchange payment for correct committed data or decryption key | protocol/economic problem mediated by blockchain or adaptor signatures |

## Transfer Matrix

| From verifiable encryption | Transfers to FDE? | How | Boundary |
| --- | --- | --- | --- |
| Ciphertext/plaintext consistency proof | yes | client can verify ciphertext corresponds to committed data before locking payment | commitment type and relation must be supported by a construction such as VECK |
| Verifiable decryption | yes | chain/public can verify key/plaintext release corresponds to ciphertext | does not ensure server releases key on time; protocol incentives needed |
| Zero-knowledge/privacy before payment | yes | server can hide data until key release while proving correctness | data may be redistributed after decryption; economics remain separate |
| Rerandomization | maybe | can support multi-client or unlinkability patterns | FDE's multi-client construction has its own preprocessing/key route; SAVER alone is not FDE |
| Homomorphism | maybe | useful for tallying or aggregating encrypted values | not a general requirement for committed-data exchange |

## Non-Transfer Boundary

- VE/VECK does not enforce payment. Payment fairness comes from blockchain contract logic or adaptor-signature mechanics.
- VE does not decide who stores data, how service is priced, or whether archival nodes have incentives.
- SAVER is not a fair-exchange protocol; it lacks client/server payment phases and commitment-specific key-release handling.
- FDE's KZG-specific VECK route should not be assumed to work for FRI/IPA/vector commitments without new evidence.
- Verifiable decryption does not prevent a client from redistributing decrypted data.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] §3 | VECK formalizes encryption under committed key for fair exchange | one FDE source |
| Same source §5 | KZG-backed VECK constructions and subset retrieval | KZG-specific |
| Same source Ethereum/Bitcoin protocols | payment/key-release layer beyond VE | protocol layer not implied by VE |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] §3-§4 | generic SNARK-friendly verifiable encryption seed | not fair exchange |
| SAVER Vote-SAVER sections | VE can support blockchain application with public board and rerandomization | voting application, not data exchange |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[verifiable-encryption|Verifiable encryption]] | record FDE/VECK as application/source extension | done |
| [[fair-data-exchange|Fair data exchange for committed data]] | promote `verifiable-encryption` from candidate to active adjacent method-family dependency | done |
| [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] | keep KZG-specific bridge separate; do not merge with generic VE bridge | no-op |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| ciphertext correctness proof | `zero-knowledge-proofs/proof-systems/verifiable-encryption` | `blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | cryptographic_enabler | FDE §3; SAVER §3-§4 | assuming correctness proof also gives payment fairness |
| verifiable decryption | `verifiable-encryption` | `fair-data-exchange` | key-release audit route | SAVER §4; FDE protocols | confusing public decryption proof with economic liveness |
| commitment-specific VECK | `fair-data-exchange` | `verifiable-encryption` | variant/source_extension | FDE §3/§5 | overgeneralizing KZG route |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[verifiable-encryption|Verifiable encryption]] | source extension and bridge link | FDE/VECK is an application of VE-style proof/encryption composition | active_seed |
| [[fair-data-exchange|Fair data exchange for committed data]] | child candidate promoted to bridge/dependency | SAVER supplies missing generic VE evidence, while FDE supplies application need | active_seed |

## 查询入口

- VECK 和 verifiable encryption 是什么关系?
- SAVER 能不能直接解决 Fair Data Exchange?
- Fair data exchange 中 ciphertext proof 负责什么，区块链负责什么?
- KZG commitments、VECK 和 payment/key release 怎么分层?

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-saver-verifiable-encryption | Created bridge to separate generic VE from FDE payment protocol semantics. | 2 source notes | codex |
