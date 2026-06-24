---
id: "nahida-bridge-zk-snarks-to-verifiable-encryption"
title: "zk-SNARKs -> verifiable encryption"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "zk-snarks"
  - "verifiable-encryption"
  - "proof-encryption-composition"
endpoint_knowledge_refs:
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-verifiable-encryption"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/proof-systems/verifiable-encryption"
relation_types:
  - "dependency"
  - "application"
  - "method_transfer"
  - "proof_encryption_composition"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
  - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
representative_source_refs:
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "iacr:2019/142"
query_keys:
  - "zk-SNARK verifiable encryption"
  - "SAVER"
  - "SNARK-friendly encryption"
  - "commit-carrying encryption"
  - "prove encrypted witness"
aliases:
  - "SNARK-friendly verifiable encryption"
domains:
  - "zero-knowledge-proofs"
topics:
  - "zk-snarks"
  - "verifiable-encryption"
tags:
  - "nahida/bridge"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-saver-verifiable-encryption"
source_refs:
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "iacr:2019/142"
confidence: "high"
trust_tier: "primary"
---

# zk-SNARKs -> verifiable encryption

## 关系命题

zk-SNARKs enable verifiable encryption when the proof system can bind an encrypted plaintext to the witness used in a relation proof. [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] gives a concrete pairing-based route: instead of encoding the encryption algorithm inside the SNARK circuit, ciphertext components are connected to a Groth16-like verification equation through commitment-compatible structure.

This bridge does not mean any zk-SNARK automatically gives encryption security. zk-SNARKs supply succinct relation proof, soundness and zero-knowledge machinery; the encryption scheme must separately provide privacy, ciphertext/plaintext binding, homomorphism, verifiable decryption or rerandomization where needed.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[zk-snarks|zk-SNARKs]] | `zero-knowledge-proofs/proof-systems/zk-snarks` | succinct non-interactive relation proof machinery, especially pairing-based/Groth16-like verification in SAVER | short proof/verifier for arithmetic relations with soundness/zero-knowledge assumptions |
| [[verifiable-encryption|Verifiable encryption]] | `zero-knowledge-proofs/proof-systems/verifiable-encryption` | encrypted-message relation proof, ciphertext/plaintext consistency, optional verifiable decryption/rerandomization | encryption plus proof that encrypted plaintext satisfies a relation |

## Transfer Matrix

| From zk-SNARKs | Transfers to verifiable encryption? | How | Boundary |
| --- | --- | --- | --- |
| Succinct relation proof | yes | verifier checks the relation proof without reading plaintext | relation proof alone does not encrypt data |
| Knowledge soundness | yes | valid proof should imply a witness/plaintext satisfying the relation | must be connected to ciphertext; otherwise prover can prove `m` and encrypt `m'` |
| Zero-knowledge | yes | hides witness details beyond public statement | encryption privacy remains a separate IND-CPA-style property |
| Pairing verification equation | yes in SAVER | ciphertext terms can be wired into Groth16-like verification with cancellation terms | specific to pairing/Groth16-like construction, not all SNARKs |
| Commit-and-prove compatibility | yes as design pattern | commit-carrying encryption can expose a commitment to encrypted plaintext | ordinary encryption is not automatically commit-carrying |

## Non-Transfer Boundary

- zk-SNARK soundness does not imply IND-CPA encryption security.
- zk-SNARK zero-knowledge does not imply ciphertext rerandomizability or unlinkability.
- SAVER's construction is pairing/Groth16-like; transparent/STARK/PLONK-style adaptations require separate evidence.
- Verifiable encryption does not provide fair exchange, payment atomicity, or data-market economics by itself.
- Vote-SAVER's election security also depends on Merkle membership, serial numbers, blockchain-board assumptions and decryption-key governance, not only this bridge.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] abstract and introduction | Need to combine zk-SNARK proof with encryption while avoiding encryption-in-circuit overhead | single primary construction source |
| SAVER Section 3.7 | commit-carrying encryption abstraction | definition is from this paper; generic foundation still thin |
| SAVER Section 4 / Algorithm 2 | concrete Setup/KeyGen/Enc/Verify/Rerandomize/Dec/Verify Dec route | pairing/Groth16-specific details |
| SAVER Section 5 | privacy/soundness/rerandomization/decryption-soundness arguments | assumptions need future comparison |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]] source note | commit-and-prove / commit-carrying SNARK background | not a verifiable-encryption source by itself |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[verifiable-encryption|Verifiable encryption]] | create method-family node and record SAVER/FDE source extensions | done |
| [[zk-snarks|zk-SNARKs]] | add SAVER as application/composition source extension without upgrading foundation | done |
| [[proof-systems|Proof systems]] | add verifiable-encryption child and bridge link | done |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Relation proof and knowledge soundness | `zero-knowledge-proofs/proof-systems/zk-snarks` | `zero-knowledge-proofs/proof-systems/verifiable-encryption` | dependency/method_transfer | SAVER §3-§5 | assuming proof soundness also proves encryption privacy |
| Commit-and-prove pattern | `zero-knowledge-proofs/proof-systems/modular-zksnarks` | `verifiable-encryption` | shared_pattern | SAVER §3.7; LegoSNARK source note | treating SAVER as a full modular SNARK framework |
| Groth16-like verification equation | `zk-snarks` | `verifiable-encryption` | construction technique | SAVER §4 | overgeneralizing to all proof systems |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[verifiable-encryption|Verifiable encryption]] | new node | reusable method-family layer split from SAVER/FDE evidence | active_seed |
| [[zk-snarks|zk-SNARKs]] | source extension and bridge link | SAVER is a SNARK application/composition route | active_seed |
| [[proof-systems|Proof systems]] | child/route list | VE is a proof-system composition method family | active_seed |

## 查询入口

- zk-SNARK 如何证明密文里的明文满足关系?
- SAVER 为什么不用把 encryption 放进 SNARK circuit?
- commit-carrying encryption 和 commit-and-prove 有什么关系?
- SAVER 能否直接迁移到 PLONK/STARK?
- zk-SNARK soundness 和 encryption privacy 是不是一回事?

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-saver-verifiable-encryption | Created bridge from SAVER deep read. | 2 source notes | codex |
