---
id: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
title: "Split prover zkSNARKs -> Recursion and folding"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
bridge_kind: "cross_direction_contrast"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "split-prover-zksnarks"
  - "recursion-and-folding"
  - "ivc"
endpoint_knowledge_refs:
  - "nahida-knowledge-split-prover-zksnarks"
  - "nahida-knowledge-recursion-and-folding"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks"
  - "zero-knowledge-proofs/recursion-and-folding"
relation_types:
  - "contrast"
  - "design_boundary"
  - "phase_decomposition"
  - "non_transfer_boundary"
relation_edges:
  - from: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
    relation: "connects"
    to: "nahida-knowledge-split-prover-zksnarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
    relation: "connects"
    to: "nahida-knowledge-recursion-and-folding"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
representative_source_refs:
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
query_keys:
  - "split prover vs recursive SNARK"
  - "split prover vs IVC"
  - "partial witness proving recursion"
  - "split prover Fiat-Shamir barrier"
  - "two-phase zkSNARK vs folding"
aliases:
  - "split prover versus IVC"
  - "split prover recursion boundary"
domains:
  - "zero-knowledge-proofs"
topics:
  - "split-prover-zksnarks"
  - "recursion-and-folding"
  - "ivc"
tags:
  - "nahida/bridge"
freshness_status: "fresh"
last_synthesized: "2026-06-21"
valid_until: "2026-07-21"
evidence_window_start: "2026-06-21"
evidence_window_end: "2026-06-21"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-split-prover-zksnarks"
source_refs:
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
confidence: "high"
trust_tier: "primary"
---

# Split prover zkSNARKs -> Recursion and folding

## 关系摘要

- From: [[split-prover-zksnarks|Split prover zkSNARKs]]
- To: [[recursion-and-folding|Recursion and folding]]
- Relation types: `contrast`, `design_boundary`, `phase_decomposition`, `non_transfer_boundary`
- Relationship thesis: Split prover zkSNARKs and recursion/folding both break proof work across stages, but they optimize different interfaces. Split prover keeps the final Groth16 verifier unchanged while protecting first-phase witness information in aux state; recursion/folding usually changes proof composition and verifier semantics to maintain an accumulated proof/state across many steps.
- Evidence scope: currently source-backed by [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] Section 1.3; recursion/folding details come from existing vault nodes, not from rereading those papers in this run.

## Endpoint 背景

| Endpoint | Path | Local meaning | Status |
| --- | --- | --- | --- |
| [[split-prover-zksnarks|Split prover zkSNARKs]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks` | 早到 witness 先生成隐私保护 aux，晚到 witness 出现后由第二 prover 完成标准 proof。 | active_seed |
| [[recursion-and-folding|Recursion and folding]] | `zero-knowledge-proofs/recursion-and-folding` | 把多步计算/证明状态递归压缩或折叠成可持续验证的小状态/证明。 | foundation_thin |

## Transfer Matrix

| 可迁移的直觉 | 到另一端的作用 | Evidence | 不迁移/需重做的边界 |
| --- | --- | --- | --- |
| Phase decomposition | 两边都把 proving/computation 拆成多个时间段，而不是等完整计算一次性完成。 | Split Prover p6-p7 | IVC 的多阶段状态不是 split-prover 的 aux privacy definition。 |
| Early work before final input | Split prover 提前处理 `wI`；IVC/folding 可逐步处理 prefix computation。 | Split Prover p3-p7 | Split prover 的目标是保持原 verifier；递归 proof 常引入新的 verifier relation。 |
| Incremental/composable proving workflow | 两者都服务“在线阶段更轻”的产品需求。 | Split Prover p4-p7 | Bob 的授权边界、`wI` 隐私、`CI(xI,wI)` 泄露边界需要 split-prover-specific 定义。 |
| Proof-system engineering tradeoff | 两者都在 prover time、setup、proof format、verifier cost 间权衡。 | Split Prover p6-p7 | Groth16 second-phase lower bound 不自动适用于 folding schemes、Nova 或 split IVC。 |

## Non-Transfer Boundary

- Split prover zkSNARKs 保留原始 Groth16 verification algorithm；recursion/folding 通常让 verifier 检查递归/累积 proof 或 folded instance。
- Split prover 的 split zero-knowledge 约束的是 `aux` 对第一阶段 witness 的泄露；IVC/folding 的 zero-knowledge/soundness 定义通常不自动覆盖“把 aux 交给 Bob 后 Bob 不能伪造 Alice 授权 proof”。
- 论文指出 random-oracle Fiat-Shamir SNARKs 的挑战依赖整段 transcript，因此在不知道后续 witness/transcript 时预计算 proof parts 有障碍。这个边界提示不能把任意 ROM-based recursive/SNARK system 直接当作 split prover solution。
- Groth16-specific lower bound 是关于 split Groth16 prover 的 second-phase group operations；它不是 folding schemes 或 proof aggregation 的一般 lower bound。

## Evidence

| Source/Note | 支撑内容 | Confidence | Limitation |
| --- | --- | --- | --- |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] p6-p7 | Explicitly compares split prover with IVC/recursive SNARKs and notes verifier/assumption/Fiat-Shamir differences. | high | Single source for this bridge; no external follow-up fetched. |
| [[split-prover-zksnarks|Split prover zkSNARKs]] | Defines local problem and privacy boundary. | high | Active seed from one paper. |
| [[recursion-and-folding|Recursion and folding]] | Provides existing vault endpoint for recursive proofs/folding/IVC. | medium | Foundation remains thin and should be refreshed with more primary sources. |

## Path Propagation

| Endpoint path | Knowledge update | Relation/index update | Bridge/refresh action | Status |
| --- | --- | --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks` | Created child node under private delegated proving. | `contrasts_with` recursion/folding and `bridges_to` this bridge. | Created this bridge. | done |
| `zero-knowledge-proofs/recursion-and-folding` | Added contrast-only source extension. | `bridges_to` this bridge. | Refresh when future IVC/recursive split proving sources arrive. | done |

## Query Keys

- split prover 和 recursive SNARK 有什么区别?
- witness 分阶段到达时，用 IVC 能不能替代 split prover?
- Split Prover 论文为什么说 random oracle Fiat-Shamir 有障碍?
- Groth16 split prover lower bound 能不能迁移到 folding schemes?

## Refresh Rules

- Last checked: `2026-06-21`
- Valid until: `2026-07-21`
- Refresh triggers: new split prover constructions for PLONK/STARK/transparent systems; new IVC source explicitly solving partial-witness aux privacy; Groth16/folding lower-bound follow-up; implementation evidence for delegatable payments.
