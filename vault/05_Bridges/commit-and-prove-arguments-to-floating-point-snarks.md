---
id: "nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks"
title: "Commit-and-prove arguments -> Floating-point SNARKs"
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
  - "floating-point-snarks"
endpoint_knowledge_refs:
  - "nahida-knowledge-commit-and-prove-arguments"
  - "nahida-knowledge-floating-point-snarks"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
  - "zero-knowledge-proofs/proof-systems/floating-point-snarks"
relation_types:
  - "dependency"
  - "compiler_backend"
  - "method_transfer"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
representative_source_refs:
  - "doi:10.1145/3548606.3560653"
query_keys:
  - "commit-and-prove floating-point SNARKs"
  - "relative-error floating-point proofs"
  - "floating point commit-and-prove compiler"
  - "approximate floating-point ZK proofs"
aliases:
  - "CP compiler for floating-point SNARKs"
  - "Commit-and-prove backend for approximate floating-point ZK"
domains:
  - "zero-knowledge-proofs"
topics:
  - "commit-and-prove-arguments"
  - "floating-point-snarks"
  - "relative-error-model"
tags:
  - "nahida/bridge"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-succinct-zk-floating-point"
source_refs:
  - "doi:10.1145/3548606.3560653"
confidence: "high"
trust_tier: "primary"
---

# Commit-and-prove arguments -> Floating-point SNARKs

## 关系命题

Commit-and-prove arguments can serve as the proof backend for a compiler from approximate floating-point constraints to succinct zero-knowledge proofs. Garg, Jain, Jin and Zhang compile floating/fixed point computations with per-gate relative-error constraints into R1CS plus range/format checks, then rely on a public-coin commit-and-prove zero-knowledge proof of knowledge to prove the resulting relation succinctly.

这条 bridge 不表示 commit-and-prove 本身定义了浮点语义。语义层来自 floating-point compiler and relative-error model；CP backend 只提供 committed witness consistency、succinct proof interface、zero-knowledge hiding and Fiat-Shamir route.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments` | public-coin CP proof of knowledge over committed R1CS witnesses, with optional Fiat-Shamir transformation | proof-system method family |
| [[floating-point-snarks|Floating-point SNARKs]] | `zero-knowledge-proofs/proof-systems/floating-point-snarks` | SNARK/argument routes for floating-point arithmetic, including exact IEEE 754 circuits and approximate relative-error semantics | numeric proof-system method family |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `dependency` | The floating-point compiler uses a CP proof of knowledge as its succinct ZK backend. | Garg et al. §2, §5-§6 | active_seed |
| `compiler_backend` | CP is not the front-end numeric model; it is the backend proving interface after constraints are generated. | Garg et al. §3, §6 | active_seed |
| `method_transfer` | Commitments, public-coin challenges, R1CS relation proving and Fiat-Shamir can transfer to the floating-point proof route. | Garg et al. §2.1, §5.2 | active_seed |

## Transfer Matrix

| From commit-and-prove arguments | Transfers to floating-point SNARKs? | How | Boundary |
| --- | --- | --- | --- |
| Commitment to witness values | yes | prover commits to witness/auxiliary values before proving R1CS-style constraints | commitment hiding/binding is backend-specific |
| Public-coin challenge flow | yes | linear-combination checks and CP proof can be made public-coin | only after compiler constraints are fixed |
| R1CS proof backend | yes | floating/fixed point constraints are compiled to an R1CS relation with range/format checks | R1CS size depends on numeric compiler, not CP alone |
| Zero-knowledge hiding | yes | ZK CP plus hidden auxiliary values supports ZK for the compiled relation | requires the paper's extra hiding/range-check modifications |
| Fiat-Shamir non-interactivity | partially | public-coin CP can be Fiat-Shamir transformed into a non-interactive argument | heuristic/model assumptions follow the selected backend |
| Succinct verification | partially | inherited from the underlying succinct CP proof with additional compiler overhead | proof size and verifier time are not universal constants |

## Non-Transfer Boundary

- Commit-and-prove does not choose the floating-point semantic model. Garg et al. choose relative-error approximate correctness; ZKLP chooses exact IEEE 754 circuit semantics.
- Relative-error soundness does not imply exact IEEE rounding or compliance with a software floating-point library.
- Numerical stability and end-application accuracy do not transfer from CP. They require application-specific error analysis.
- The batch range proof and three-square positivity route are part of Garg et al.'s compiler, not generic CP machinery.
- The local ACM CCS PDF defers several proofs and concrete instantiations to the full version, so this bridge should stay `active_seed` until comparison sources are absorbed.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct Zero Knowledge for Floating Point Computations]] Abstract/§1 | need for succinct ZK for floating-point computations and high cost of exact binary-circuit routes | source-authored framing |
| Garg et al. §2.1 | generic transformation from public-coin CP proof for R1CS to floating-point computation proofs | depends on underlying CP properties |
| Garg et al. §3 | technical overview of approximate correctness, batch range proof and wrap-around soundness issues | proof details partly deferred |
| Garg et al. §5-§6 | definitions, CP protocol and zero-knowledge adaptation | local PDF contains conference-length presentation |
| Garg et al. Tables 1-3 | R1CS/prover-efficiency comparison against bit-decomposition and exact IEEE routes | benchmark and group-size assumptions are source-local |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | Add CP compiler backend use case for relative-error floating-point proofs | done |
| [[floating-point-snarks|Floating-point SNARKs]] | Add approximate relative-error route beside exact IEEE 754 route | done |
| [[proof-systems|Proof systems]] | Add source extension and bridge link | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-commit-and-prove-arguments | applies_to | nahida-knowledge-floating-point-snarks | Garg et al. §2.1, §5-§6 | high | active_seed |
| nahida-knowledge-floating-point-snarks | depends_on | nahida-knowledge-commit-and-prove-arguments | Garg et al. §2.1 | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | bridges_to | nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks | bridge note | high | active_seed |
| nahida-knowledge-floating-point-snarks | bridges_to | nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks | bridge note | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| CP canonical source absorbed | Strengthen the backend taxonomy beyond source-local compiler use | `nahida-research-search` or `nahida-update` |
| Floating-point ZK comparison source absorbed | Compare exact IEEE route and relative-error route | `nahida-update` |
| Numerical-analysis source absorbed | Calibrate when relative-error gates imply useful application-level accuracy | `nahida-research-search` |
| Full version of Garg et al. absorbed | Replace deferred-proof caveats with concrete proof/instantiation evidence | `nahida-update` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-succinct-zk-floating-point | Created bridge from commit-and-prove arguments to approximate floating-point SNARKs using Garg et al. as first source-backed transfer. | 1 source note | codex |
