---
id: "nahida-bridge-polynomial-commitments-to-recursive-proof-composition"
title: "Polynomial commitments -> recursive proof composition"
original_title: "Polynomial commitments -> recursive proof composition"
file_slug: "polynomial-commitments-to-recursive-proof-composition"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "dependency"
bridge_status: "active_seed"
endpoint_paths:
  - "zero-knowledge-proofs/polynomial-commitments"
  - "zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition"
endpoint_knowledge_refs:
  - "nahida-knowledge-polynomial-commitments"
  - "nahida-knowledge-recursive-proof-composition"
from_domain: "zero-knowledge-proofs"
to_domain: "zero-knowledge-proofs"
from_direction: "polynomial-commitments"
to_direction: "recursion-and-folding"
from_topic: "polynomial-commitments"
to_topic: "recursive-proof-composition"
relation_types:
  - "dependency"
  - "method_transfer"
  - "verification_deferral"
  - "performance_compression"
directionality: "from_to"
relationship_thesis: "Halo shows that an inner-product-style polynomial commitment with amortized opening verification can support recursive proof composition: the recursive circuit carries the input/output of the expensive linear commitment-opening check as public verifier state, while nested amortization collapses many deferred checks into one final outside check."
transferability: "medium"
non_transfer_boundary: "This bridge transfers the amortized-verification pattern, not arbitrary PCS compatibility. Halo relies on the smooth inner-product challenge structure, a sound amortization argument, Fiat-Shamir/random oracle, a suitable curve cycle and a final linear verifier check outside the recursive circuit."
evidence_window_start: "2026-06-22"
evidence_window_end: "2026-06-22"
domains:
  - "zero-knowledge-proofs"
topics:
  - "polynomial-commitments"
  - "recursive-proof-composition"
  - "nested-amortization"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
knowledge_refs:
  - "nahida-knowledge-polynomial-commitments"
  - "nahida-knowledge-recursive-proof-composition"
query_keys:
  - "Polynomial commitments -> recursive proof composition"
  - "IPA polynomial commitments recursive proofs"
  - "nested amortization polynomial commitments"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-halo-recursive-proof-composition"
source_refs:
  - "iacr:2019/1021#section-3"
  - "iacr:2019/1021#section-4"
confidence: "high"
trust_tier: "primary"
---

# Polynomial commitments -> recursive proof composition

## 命名与路径

- Original title: Polynomial commitments -> recursive proof composition
- File slug: `polynomial-commitments-to-recursive-proof-composition`
- Path safety check: current bridge lives under `05_Bridges`.

## 端点基础说明

This bridge connects the reusable primitive [[polynomial-commitments|Polynomial commitments]] to the recursive-proof problem node [[recursive-proof-composition|Recursive proof composition]]. The source evidence is Halo: [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Recursive Proof Composition without a Trusted Setup]].

## Relationship Thesis

Halo's inner-product-style polynomial commitment has logarithmic proof size but a linear verifier operation. The bridge contribution is not simply “use a PCS inside a proof system”; it is the stronger pattern that commitment-opening verification can be amortized, converted into verifier state, and checked once outside a recursive proof chain.

In this pattern:

- the recursive circuit performs only logarithmic marginal verification work;
- the circuit treats the expensive operation's input and claimed output as public inputs;
- nested amortization merges old and new deferred obligations;
- the ultimate verifier performs one final linear operation to validate the accumulated state.

## Endpoints

| Endpoint | Role | Evidence |
| --- | --- | --- |
| `zero-knowledge-proofs/polynomial-commitments` | supplies the commitment/opening structure and amortized verifier obligation | Halo §3 |
| `zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | uses the deferred verifier state to make arbitrary-depth recursion practical | Halo §4 and §6 |

## Transfer Matrix

| From | To | Transfer | Boundary |
| --- | --- | --- | --- |
| IPA-style PCS | recursive proof composition | logarithmic opening proof plus amortizable linear verifier operation | does not imply KZG/FRI/other PCS have the same nested-amortization route |
| amortized opening verification | verifier circuit design | move expensive operation outside the recursive circuit while carrying its claimed output as public state | requires sound helper/amortization proof and final linear check |
| elliptic-curve cycle implementation | recursive verifier arithmetic | each curve verifies proofs over the other curve's native field | Tweedledum/Tweedledee details are source-specific, not a general PCS property |

## Non-Transfer Boundary

- Do not infer that a polynomial commitment alone gives recursive proof composition.
- Do not infer that Halo is fully succinct; the final verifier still performs linear work.
- Do not transfer Halo's curve parameters, 3.5 KiB proof size or `2^17` threshold to later recursive systems without a dedicated source.
- Do not merge this bridge into the existing folding-schemes bridge: Halo's route is nested amortization, not relaxed-R1CS folding.

## Evidence

| Source | Evidence | Confidence |
| --- | --- | --- |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Halo]] §3 | Introduces a Pedersen-vector/inner-product-style polynomial commitment and amortizes the linear verifier operation across many openings. | high |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Halo]] §4 | Defines nested amortization: recursive circuits carry deferred operation state and collapse obligations instead of performing full linear verification at each depth. | high |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Halo]] §6 | Implements the route over a normal elliptic-curve 2-cycle and reports practical recursive composition. | high |

## Propagation Targets

- [[polynomial-commitments|Polynomial commitments]]
- [[recursive-proof-composition|Recursive proof composition]]
- [[recursion-and-folding|Recursion and folding]]

## 连接命题

- From: `zero-knowledge-proofs/polynomial-commitments`
- To: `zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition`
- Relation types: dependency, method_transfer, verification_deferral, performance_compression
- Directionality: `from_to`
- Relationship thesis: Halo turns an amortizable PCS verifier obligation into recursive verifier state, enabling recursive proof composition without embedding the expensive linear check into every recursive circuit.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| nahida-knowledge-polynomial-commitments | `zero-knowledge-proofs/polynomial-commitments` | commitment/opening primitive and amortized verifier obligation | Halo §3 | active_seed |
| nahida-knowledge-recursive-proof-composition | `zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | recursive proof-chain problem and nested amortization usage | Halo §4/§6 | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| amortized verification of commitment openings | recursive verifier-state design | Halo §3-§4 | only where deferred obligations can be soundly batched and finalized |
| public-input verifier state | recursive circuit sizing | Halo §4 | public state must be checked by final verifier; it is not free trust |
| curve-cycle native-field recursion | implementation design | Halo §6.1 | ordinary curve cycles are easier than pairing-friendly cycles but still require security and circuit checks |

## 查询入口

- Polynomial commitments -> recursive proof composition
- IPA polynomial commitments recursive proofs
- nested amortization polynomial commitments

## 复核笔记

- Maturity: `active_seed`.
- Repair pass: ensure reciprocal references exist in both endpoint nodes after index rebuild.

## 刷新规则

- Last checked: `2026-06-22`
- Valid until: `2026-07-22`
- Refresh triggers: new source changes PCS compatibility, accumulation/nested-amortization boundary, final verifier cost, setup assumptions or recursive curve-cycle requirements.
