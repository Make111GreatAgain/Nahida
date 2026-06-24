---
id: "nahida-knowledge-elastic-snarks"
title: "Elastic SNARKs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "elastic-snarks"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "memory-efficient-snarks"
  - "elastic-snarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/memory-efficient-snarks/elastic-snarks"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
relation_edges:
  - from: "nahida-knowledge-elastic-snarks"
    relation: "is_a"
    to: "nahida-knowledge-memory-efficient-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks/elastic-snarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-elastic-snarks"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-elastic-snarks"
    relation: "uses"
    to: "nahida-knowledge-kzg-commitments"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-elastic-snarks"
    relation: "uses"
    to: "nahida-knowledge-sum-check-protocol"
    evidence_refs:
      - "vault/05_Bridges/sum-check-protocol-to-memory-efficient-snarks.md"
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-elastic-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-elastic-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
  - "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
source_note_refs:
  - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
  - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
representative_source_refs:
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
query_keys:
  - "Elastic SNARKs"
  - "elastic-snarks"
  - "elastic prover"
  - "space-efficient SNARK prover"
  - "streaming SNARK"
  - "Gemini elastic SNARK"
  - "Epistle elastic SNARK"
  - "elastic Plonk"
  - "streaming R1CS"
aliases:
  - "elastic prover SNARKs"
  - "streaming SNARKs"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "elastic-snarks"
  - "memory-efficient-snarks"
  - "zk-snarks"
  - "streaming-r1cs"
  - "plonkish-snarks"
  - "kzg-commitments"
  - "sum-check-protocol"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-22"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-gemini-elastic-snarks"
  - "nahida-knowledge-20260623-epistle-elastic-snarks"
source_refs:
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
confidence: "high"
trust_tier: "primary"
---

# Elastic SNARKs

## 定义与范围

- 定义: Elastic SNARKs 是一类低内存 SNARK 方法族，目标是在同一个 statement、proof 格式和 verifier 接口下，允许 prover 按资源环境选择 time-efficient 或 space-efficient 配置，并且可在执行中从低内存状态切换到快速状态。
- 不包含: Gemini 或 Epistle 的论文全部细节、某个 Rust implementation、某一次 benchmark、KZG foundation、PLONK/HyperPlonk foundation。
- Canonical terms: `elastic-snarks`, `elastic prover`, `streaming SNARKs`
- Standalone completeness check: 本节点本地解释 elastic SNARK 的问题、约束、两条 source-backed route、依赖与边界；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“同一个 SNARK proof 怎么支持低内存和高性能 prover”“Gemini 和 Epistle 属于什么层”“elastic SNARK 与 KZG/sumcheck 的关系”时先读本节点。
- Update scope: 新 source 若提出新的 constraint-system route、非 KZG elastic PCS、lookup-friendly streaming Plonkish prover、或改变 time/memory/pass tradeoff，应刷新本节点。

## 背景

很多 SNARK 的 verifier 端很短，但 prover 端需要持有完整 witness、constraint matrices、execution trace、polynomial buffers 或 commitment state。Elastic SNARKs 关心的不是重新定义 SNARK，而是在保持 proof/verifier interface 不变的情况下，让 prover 有多种资源配置:

- memory-rich environment: 用线性内存换更低 prover time。
- memory-poor environment: 通过 streaming、多次扫描和小状态生成相同类型 proof。
- hybrid environment: space-efficient prover 在状态缩小后暂停保存，再由 time-efficient prover 恢复完成。

这使 elastic SNARKs 成为 [[memory-efficient-snarks|Memory-efficient SNARKs]] 下的一个方法族，而不是某篇论文或某个协议名。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family`
- 为什么足够通用: Gemini 和 Epistle 已经分别覆盖 R1CS 与 Plonkish/HyperPlonk 路线，说明“elastic prover under stable proof interface”是跨 source、跨 constraint-system 的可复用方法族。
- 为什么不是单篇论文/单个协议/单个仓库: Gemini、Epistle 和 ark-gemini/arkworks/hyperplonk 只是代表 evidence；本节点组织的是 time/memory elasticity 的通用问题与边界。
- 需要引用的更基础 Knowledge: [[memory-efficient-snarks|Memory-efficient SNARKs]], [[zk-snarks|zk-SNARKs]], [[kzg-commitments|KZG commitments]], [[sum-check-protocol|Sum-check protocol]]。
- 不应拆出的实例/协议/来源: Gemini 与 Epistle 默认保留为 source notes；只有未来多 source 形成稳定子问题时才拆出 `streaming R1CS SNARKs` 或 `elastic Plonkish SNARKs`。

## 解决的问题

Elastic SNARKs 解决 prover-side resource elasticity:

- 同一应用不希望为低内存机器和高性能机器部署不同 proof/verifier contract。
- 低内存 prover 不能随机访问或持有完整向量，但仍要生成与常规 prover 兼容的 oracle messages、commitments 和 openings。
- 单独优化 PIOP 或 PCS 不够；整个 proof pipeline 里的 constraint-system streams、PIOP messages、polynomial commitments 和 openings 都必须支持 streaming realization。
- Space-efficient prover 的额外 pass/time 开销必须可表达、可比较，避免把低内存实现伪装成“免费”优化。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | child_of / method_family_of | Gemini + Epistle source-backed routes | active_seed |
| [[zk-snarks|zk-SNARKs]] | depends_on | Elastic SNARKs preserve SNARK proof/verifier semantics while changing prover realization | active_seed |

## 方法族与解决路线

| Route | Core idea | Applies when | Cost / boundary | Representative source |
| --- | --- | --- | --- | --- |
| Streaming R1CS elastic SNARK | Treat R1CS matrices, witness and trace as streams; use elastic PIOP plus streaming KZG commitment/opening to offer time-efficient and space-efficient prover configurations under one proof interface. | R1CS inputs and traces can be generated/replayed as streams; application accepts extra passes and quasi-linear prover time. | Space-efficient route pays `log` factors and depends on KZG setup/pairing assumptions; trace generation may still be memory-heavy outside prover core. | [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] |
| Plonkish / HyperPlonk elastic SNARK | Make HyperPlonk's multivariate PIOP toolbox streaming-friendly, then compile Plonk constraint-system gate and wiring checks with elastic multilinear KZG. | Plonkish circuit has streamable selector/trace/permutation data; custom gate degree is bounded; lookup is not required or handled separately. | General lookup streaming remains open; still inherits KZG setup/pairing assumptions; current benchmark uses mock Plonk gates. | [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] |
| Hybrid prover switching | Space-efficient prover stores a compact current state; if later rounds fit memory threshold, time-efficient prover resumes from that state. | Protocol messages are identical across configurations and state can be faithfully serialized. | Implementation-specific thresholds affect memory/time; does not change proof semantics. | Gemini; Epistle |
| Elastic PCS layer | Polynomial commitment commit/open must be streamable, not just the IOP prover. | PCS has algebraic structure enabling small-state commit/open over ordered coefficient/SRS streams. | KZG-specific realizations do not generalize to all PCS; transparent/IPA/FRI/DARK routes need separate evidence. | Gemini KZG; Epistle multilinear KZG |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | paper | Introduces elastic SNARKs and gives R1CS route with streaming R1CS, elastic PIOP and elastic KZG. | R1CS-focused; space-efficient prover trades memory for higher time/passes; KZG assumptions remain. | Abstract; §2.1-§2.8; §4-§10 |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle: Elastic Succinct Arguments for Plonk Constraint System]] | paper | Extends elastic SNARKs to Plonk constraint systems by streaming HyperPlonk-style multivariate PIOP and elastic multilinear KZG; improves Gemini-style space-efficient asymptotic time from `O(N log^2 N)`-like R1CS route to `O(N log N)` for Plonkish setting. | Lookup protocol not generally streaming; custom gate degree constant; benchmark is one implementation/hardware setup. | Abstract; §2; §4-§7 |

## 当前综合

- Evidence window: `2026-06-22` to `2026-06-23`，覆盖当前 vault 已深读 Gemini 与 Epistle。
- Freshness: `fresh` for current-vault synthesis; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: Elastic SNARKs 已从 Gemini 单 source route 升级为独立方法族。Gemini 证明 R1CS 可以在同一 proof/verifier interface 下提供 time-efficient 与 space-efficient prover；Epistle 证明同一思想可以迁移到 Plonk constraint system，但不是简单套用 R1CS，而是要把 HyperPlonk 的 SumCheck、ZeroCheck、product/permutation checks 和 multilinear KZG 都重写为 streaming model。二者共同说明: 低内存 SNARK 的关键不是“把 prover 循环改成 iterator”，而是 constraint system、PIOP toolbox 和 PCS/opening layer 的端到端弹性。

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[sum-check-protocol-to-memory-efficient-snarks|Sum-check protocol -> memory-efficient SNARKs]] | `verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | dependency, method_transfer, prover_space_reduction | Sumcheck-style round reductions help streaming prover construction, but non-interactivity, commitments, zero knowledge and constraint-system specifics remain separate. | active_seed |
| [[memory-efficient-snarks-to-kzg-commitments|Memory-efficient SNARKs -> KZG commitments]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | dependency, implementation_reuse, prover_space_reduction | KZG can be made streaming in Gemini/Epistle, but KZG trust/setup/pairing assumptions and exact batching/opening algorithms do not transfer to every low-memory SNARK. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-elastic-snarks | is_a | nahida-knowledge-memory-efficient-snarks | this note; parent note | high | active_seed |
| nahida-knowledge-elastic-snarks | depends_on | nahida-knowledge-zk-snarks | Gemini; Epistle | high | active_seed |
| nahida-knowledge-elastic-snarks | uses | nahida-knowledge-sum-check-protocol | Gemini scalar/tensor protocols; Epistle streaming SumCheck/ZeroCheck/Product/Permutation | high | active_seed |
| nahida-knowledge-elastic-snarks | uses | nahida-knowledge-kzg-commitments | Gemini KZG; Epistle multilinear KZG | high | active_seed |
| nahida-knowledge-elastic-snarks | evidenced_by | vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md | source note | high | active_seed |
| nahida-knowledge-elastic-snarks | evidenced_by | vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md | source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| PLONK/HyperPlonk foundation notes 缺。 | Epistle depends on Plonkish/HyperPlonk machinery, but Epistle source note should not become foundation definition. | nahida-update / nahida-research-search | high | queued |
| Streaming lookup protocol for Plonkish elastic SNARKs 缺。 | Epistle explicitly leaves lookup under limited space open; this limits Plonkish route completeness. | nahida-research-search | high | open_problem |
| Non-KZG elastic PCS comparisons 缺。 | Gemini/Epistle are KZG-heavy; transparent/IPA/FRI/DARK routes need primary evidence. | nahida-research-search / nahida-update | medium | queued |
| End-to-end stream generation evidence sparse. | Prover-core streaming assumptions may hide trace/index generation memory in applications. | nahida-github-repo-analyze / nahida-update | medium | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-epistle-elastic-snarks | Created elastic SNARKs method-family node from Gemini + Epistle, with R1CS and Plonkish route split. | 2 source notes | codex |
