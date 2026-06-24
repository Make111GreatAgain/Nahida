---
id: "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
title: "Commit-and-prove arguments -> blockchain fair exchange protocols"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "commit-and-prove-arguments"
  - "fair-exchange-protocols"
endpoint_knowledge_refs:
  - "nahida-knowledge-commit-and-prove-arguments"
  - "nahida-knowledge-blockchain-fair-exchange-protocols"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
  - "blockchain-systems/execution-and-transactions/fair-exchange-protocols"
relation_types:
  - "dependency"
  - "application"
  - "proof_protocol_enabler"
  - "shared_pattern"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
  - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
representative_source_refs:
  - "doi:10.1145/3460120.3484558"
  - "iacr:2019/142"
query_keys:
  - "commit-and-prove fair exchange"
  - "CP-NIZK ZKCPlus"
  - "proof of delivery"
  - "ZKCP commit-and-prove"
aliases:
  - "CP-NIZK to fair exchange"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "commit-and-prove-arguments"
  - "fair-exchange-protocols"
tags:
  - "nahida/bridge"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcplus-fair-exchange"
source_refs:
  - "doi:10.1145/3460120.3484558"
  - "iacr:2019/142"
confidence: "high"
trust_tier: "primary"
---

# Commit-and-prove arguments -> blockchain fair exchange protocols

## 关系命题

Commit-and-prove arguments enable a strong proof-before-payment route for blockchain fair exchange: the seller can commit to a hidden good, prove that the committed good satisfies buyer predicates, and separately prove that the delivered ciphertext encrypts the same committed good. ZKCPlus is the current source-backed instance of this bridge.

The bridge is one-way. CP arguments provide relation proof and commitment consistency; they do not by themselves provide payment finality, refund liveness, timeout policy, censorship resistance, dispute economics, or post-decryption redistribution control.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments` | proof over committed witness slots and proof composition | bind hidden values to commitments, then prove relations about them |
| [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] | `blockchain-systems/execution-and-transactions/fair-exchange-protocols` | exchange payment for digital goods/services without centralized arbiter | transaction locks/contracts plus proof/encryption layers |

## Transfer Matrix

| From CP arguments | Transfers to fair exchange? | How | Boundary |
| --- | --- | --- | --- |
| Committed witness binding | yes | buyer can verify all proofs refer to the same hidden good `x` via `c_x` | binding comes from commitment; application still decides what `x` is worth |
| Predicate proof composition | yes | validate phase can run multiple predicate proofs over shared commitment | predicate selection/testing policy is application-specific |
| Proof of encrypted delivery | yes | deliver phase proves ciphertext encrypts the committed good and key/lock is consistent | decryption/payment ordering needs blockchain lock/reveal |
| Commitment lock | yes | smart contract can verify opening instead of hash preimage when chain supports it | on-chain feasibility depends on curve/commitment support |
| Zero-knowledge hiding | partly | buyer learns validity evidence before payment without seeing the good | metadata, ciphertext size, repeated tests and final decryption can still leak/application constraints |

## Non-Transfer Boundary

- CP-NIZK soundness does not mean the seller will reveal the key; reveal/refund incentives are protocol-layer responsibilities.
- CP zero-knowledge does not define market fairness or price fairness.
- ZKCPlus's data-parallel construction does not automatically cover arbitrary non-data-parallel predicates; the protocol needs other CP-compatible arguments for those parts.
- Commitment lock security relies on commitment binding/hiding; hash-lock variants rely on hash assumptions.
- Fair exchange does not prevent buyers from redistributing data after successful decryption.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] §2.4 | CP-NIZK proves relations over committed message parts and auxiliary witness | adopts LegoSNARK notion |
| ZKCPlus §3 | data-parallel CP-NIZK and proof composition | construction details are source-specific |
| ZKCPlus §4.2 | commit/validate/deliver protocol and proof of delivery | payment lock remains blockchain-specific |
| ZKCPlus Appendix E | security proof combines CP-NIZK, commitment, hash/lock and blockchain finalization | no claim that CP alone implies fairness |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]] | broader CP-SNARK composition vocabulary | not a fair-exchange protocol |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | Add ZKCPlus as data-parallel CP-NIZK/fair-exchange application source extension. | done |
| [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] | Add CP-NIZK route as proof-before-payment method and separate it from payment finality. | done |
| [[fair-data-exchange|Fair data exchange for committed data]] | Mark ZKCPlus as broader comparison source, not a KZG/DA-specific FDE construction. | done |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| committed witness consistency | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments` | `blockchain-systems/execution-and-transactions/fair-exchange-protocols` | proof_protocol_enabler | ZKCPlus §4.2 | mistaking proof consistency for payment fairness |
| predicate composition | CP arguments | fair exchange validation | application | ZKCPlus §4.3.1 | application predicates may be weak or gameable |
| proof of delivery | CP arguments + encryption | fair exchange delivery | dependency | ZKCPlus §4.2.2 | encryption/lock assumptions remain separate |

## 查询入口

- ZKCPlus 为什么比 ZKCP 更适合大规模数据?
- Commit-and-prove 在 fair exchange 里到底解决什么?
- CP-NIZK 是否能直接保证买卖公平?
- Proof of delivery、hash lock、commitment lock 怎么分层?

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-zkcplus-fair-exchange | Created bridge from ZKCPlus absorption. | 2 source notes | codex |
