---
id: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
title: "Private delegated proving -> KZG commitments"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
bridge_kind: "cross_direction_dependency"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "private-delegated-proving"
  - "kzg-commitments"
endpoint_knowledge_refs:
  - "nahida-knowledge-private-delegated-proving"
  - "nahida-knowledge-kzg-commitments"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
relation_types:
  - "dependency"
  - "verification_enabler"
  - "implementation_reuse"
  - "privacy_preserving_delegation"
relation_edges:
  - from: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    relation: "connects"
    to: "nahida-knowledge-private-delegated-proving"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving.md"
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    relation: "connects"
    to: "nahida-knowledge-kzg-commitments"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments/kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
  - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
representative_source_refs:
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
query_keys:
  - "private delegated proving KZG"
  - "KZG consistency checker"
  - "witness consistency checker KZG"
  - "PIOP consistency checker KZG"
  - "Siniel KZG commitments"
  - "EOS KZG commitments"
  - "EOS PIOP consistency checker"
  - "KZG in delegated SNARKs"
aliases:
  - "KZG for private delegated proving"
domains:
  - "zero-knowledge-proofs"
topics:
  - "private-delegated-proving"
  - "kzg-commitments"
  - "consistency-checker"
tags:
  - "nahida/bridge"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-21"
evidence_window_end: "2026-06-23"
created: "2026-06-21"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-siniel-private-delegated-proving"
  - "nahida-knowledge-20260623-eos-private-delegated-proving"
source_refs:
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
confidence: "high"
trust_tier: "primary"
---

# Private delegated proving -> KZG commitments

## 关系摘要

- From: [[private-delegated-proving|Private delegated proving]]
- To: [[kzg-commitments|KZG commitments]]
- Relation types: `dependency`, `verification_enabler`, `implementation_reuse`, `privacy_preserving_delegation`
- Relationship thesis: Private delegated proving needs a binding/evaluation layer so secret-shared witness inputs, PIOP computations and polynomial commitments remain consistent even when workers are untrusted. In EOS, PC/KZG-oriented prover-operation circuits and PIOP consistency checks make delegated PIOP proving checkable by the delegator; in Siniel, KZG commitments and opening proofs supply worker-side witness/PIOP consistency checks without delegator online participation.
- Evidence scope: currently source-backed by [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS]] and [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]]; zkSaaS, OB22 collaborative zkSNARKs and non-KZG PCS routes remain queued.

## Endpoint 背景

| Endpoint | Path | Local meaning | Status |
| --- | --- | --- | --- |
| [[private-delegated-proving|Private delegated proving]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving` | 把 prover work 外包给多个 worker，同时隐藏 witness、降低 delegator 在线负担，并检测恶意 worker。 | foundation_thin |
| [[kzg-commitments|KZG commitments]] | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | pairing-based polynomial commitment scheme，提供 commitment、evaluation opening proof 和 verifier check。 | foundation_thin |

## Transfer Matrix

| 从 KZG commitments 迁移的东西 | 到 Private delegated proving 的作用 | Evidence | 不迁移/需重做的边界 |
| --- | --- | --- | --- |
| Commitment binding | 绑定 worker 对 witness/prover polynomial share 的承诺，防止后续随意替换 polynomial。 | Siniel p10-p18 | KZG 不提供 witness secret sharing 或 MPC privacy。 |
| Evaluation opening proof | 让 worker 在随机点验证 polynomial/evaluation/commitment 一致性。 | Siniel Fig. 8, Fig. 9 | 随机挑战、authentication tags 和 worker voting 是 Siniel 协议层设计。 |
| Succinct verification of polynomial openings | 使 consistency checker 不需要读取完整 polynomial。 | Siniel p8-p9, p14-p18 | Proof-system-specific，换成 IPA/FRI/other PCS 需要重做 checker 成本和安全证明。 |
| KZG knowledge soundness/extractor assumption | Appendix proof 用 KZG extractor 论证 consistency checker 安全性。 | Siniel Theorem 1-3, Appendix D-F | AGM/trusted setup/pairing assumptions 不自动适用于 transparent PCS。 |
| PIOP+PCS prover-operation circuits | EOS 把 PIOP polynomial arithmetic 与 KZG-style commit/open operations 设计成低深度 secret-shared circuits，使 delegated prover 不必走 naive generic MPC。 | EOS §4, §6 | 这是 EOS/MARLIN-style implementation evidence；不代表所有 PCS 或 SNARK backend 自动低成本。 |
| Delegator-side PIOP consistency check | EOS 用 random-point witness LDE check 与 PC openings 约束 worker 提交的 PIOP oracle state，避免最终 proof accept/reject 变成 witness leakage channel。 | EOS §5, Appendix B | 与 Siniel 的 worker-side WCC/PCC 不同；delegator 仍在线参与 checker rounds。 |

## Non-Transfer Boundary

- KZG commitments 是 enabling primitive，不是 private delegated proving 协议本身。Witness privacy 依赖协议层的 secret sharing/MPC execution、worker-collusion threshold、consistency-check policy 和具体 adversary model；Siniel 使用 Shamir sharing/authentication tags/Beaver triples，EOS 使用 additive shares 和 isolated/collaborative delegated SNARK execution.
- EOS 中的 KZG/PCS role 是 consistency-binding 和 efficient prover-operation substrate，不是 witness privacy 本身；witness privacy 来自 additive secret sharing、worker-collusion assumption 和 delegated SNARK protocol.
- KZG 不能消除 delegator offline communication；Siniel 的 offline phase 仍需发送 witness shares、tags、keys 和 Beaver triples。
- KZG 不决定 adversary threshold。Siniel 选择 honest majority，EOS/zkSaaS/FHE routes 的 threshold/security model 需要各自来源校准。
- KZG-based checker 不自动迁移到 FRI/IPA/transparent commitments；需要新的 opening/checker relation 和证明。

## Evidence

| Source/Note | 支撑内容 | Confidence | Limitation |
| --- | --- | --- | --- |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS]] p5-p10, p17-p18 | PIOP+PCS delegated proving uses efficient circuits for KZG-style PC operations and a PIOP consistency checker to bind worker-produced polynomial oracles to the delegated witness. | high | Delegator remains online; evaluation is MARLIN/arkworks/source-local. |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]] p8-p18 | Witness consistency checker and PIOP consistency checker use KZG.Open/KZG.Verify to bind shares, evaluations and commitments. | high | Single source and KZG-specific instantiation. |
| [[kzg-commitments|KZG commitments]] | Provides local definition of KZG commitment/opening semantics. | medium | Foundation remains thin; modern KZG usage sources still incomplete. |
| [[private-delegated-proving|Private delegated proving]] | Organizes the privacy-preserving delegated-prover problem and keeps EOS/Siniel source-specific details below. | high | zkSaaS/OB22/non-KZG routes remain unabsorbed. |

## Path Propagation

| Endpoint path | Knowledge update | Relation/index update | Bridge/refresh action | Status |
| --- | --- | --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving` | Created child node and added bridge link. | `depends_on` KZG and `bridges_to` bridge. | Created this bridge. | done |
| `zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | Added Siniel usage extension and bridge link. | `bridges_to` bridge and source evidence row. | Created this bridge. | done |
| `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving` | Added EOS primary-source evidence for online PIOP consistency checking. | Added source evidence to bridge and delegated-proving node. | Refreshed bridge scope from Siniel-only to EOS+Siniel. | done |

## Query Keys

- KZG 在 Siniel 里做什么?
- private delegated proving 怎么检查 worker 有没有篡改 share?
- witness consistency checker 和 polynomial commitments 有什么关系?
- PIOP consistency checker 为什么需要 KZG opening proof?
- EOS 和 Siniel 对 KZG/PCS 的使用有什么区别?

## Refresh Rules

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: zkSaaS/OB22 collaborative zkSNARK primary source absorption; non-KZG PCS delegated proving source; EOS/Siniel repository analysis; KZG/PCS foundation refresh.
