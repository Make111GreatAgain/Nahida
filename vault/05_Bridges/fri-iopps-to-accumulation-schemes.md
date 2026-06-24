---
id: "nahida-bridge-fri-iopps-to-accumulation-schemes"
title: "FRI IOPPs -> accumulation schemes"
original_title: "FRI IOPPs -> accumulation schemes"
file_slug: "fri-iopps-to-accumulation-schemes"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "method_transfer"
bridge_status: "active_seed"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/fri-iopps"
  - "zero-knowledge-proofs/recursion-and-folding/accumulation-schemes"
endpoint_knowledge_refs:
  - "nahida-knowledge-fri-iopps"
  - "nahida-knowledge-accumulation-schemes"
from_domain: "zero-knowledge-proofs"
to_domain: "zero-knowledge-proofs"
from_direction: "proof-systems"
to_direction: "recursion-and-folding"
from_topic: "fri-iopps"
to_topic: "accumulation-schemes"
relation_types:
  - "method_transfer"
  - "dependency"
  - "shared_pattern"
  - "formalization_bridge"
  - "transparent_hash_route"
directionality: "from_to"
relationship_thesis: "Reed-Solomon proximity, quotienting, list-decoding and oracle-query machinery from the FRI/IOPP family can be reused to build hash-based accumulation schemes when it is wrapped in an IOR/noninteractive-reduction framework that preserves distance across accumulation steps."
transferability: "medium"
non_transfer_boundary: "This bridge transfers RS proximity and oracle-reduction patterns, not a claim that ordinary FRI is itself an accumulator, a full polynomial commitment scheme, or a complete PCD construction. Arc needs additional machinery: out-of-domain binding, quotient-based distance preservation, Merkle commitments, IOR soundness, and NP/R1CS lifting."
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
domains:
  - "zero-knowledge-proofs"
topics:
  - "fri-iopps"
  - "accumulation-schemes"
  - "reed-solomon-proximity"
  - "interactive-oracle-reductions"
source_note_refs:
  - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
knowledge_refs:
  - "nahida-knowledge-fri-iopps"
  - "nahida-knowledge-accumulation-schemes"
  - "nahida-knowledge-recursive-proof-composition"
query_keys:
  - "FRI IOPPs -> accumulation schemes"
  - "FRI to accumulation"
  - "Reed-Solomon proximity accumulation"
  - "Arc RS proximity"
  - "hash-based accumulation via IOPP"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-arc-accumulation-reed-solomon"
source_refs:
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
confidence: "high"
trust_tier: "primary"
---

# FRI IOPPs -> accumulation schemes

## 命名与路径

- Original title: FRI IOPPs -> accumulation schemes
- File slug: `fri-iopps-to-accumulation-schemes`
- Path safety check: current bridge lives under `05_Bridges`.

## 端点基础说明

This bridge connects [[fri-iopps|FRI IOPPs]] and [[accumulation-schemes|Accumulation schemes]]. The direct source evidence is [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]].

FRI IOPPs are proof-system/proximity-testing machinery around Reed-Solomon codewords, folding, oracle queries and Merkle-authenticated openings. Accumulation schemes are a recursion/PCD method family that compresses many proof obligations into a running accumulator. Arc shows a narrow but important method transfer: RS proximity machinery can be repurposed so the accumulator relation preserves distance rather than degrading with each step.

## Relationship Thesis

Reed-Solomon proximity tools developed for IOPP/FRI-style proof systems can become the core of hash-based accumulation when the protocol is redesigned as a many-to-one reduction. Arc does this by combining input codeword claims, binding nearby codewords with out-of-domain samples, quotienting by sampled points, and compiling the resulting IORs into non-interactive reductions with Merkle commitments.

The result is not "FRI equals accumulation." It is "FRI-family RS proximity/list-decoding ideas can serve the accumulation layer if the construction preserves distance and is wrapped in a reduction/PCD framework."

## Endpoints

| Endpoint | Role | Evidence |
| --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/fri-iopps` | supplies RS proximity, quotienting, list-decoding and oracle-query patterns | Arc §2.1, §3.2, §6; existing [[fri-iopps|FRI IOPPs]] node |
| `zero-knowledge-proofs/recursion-and-folding/accumulation-schemes` | uses those patterns to create unbounded hash-based accumulation | Arc Abstract, §1, §6, §7 |
| `zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | downstream beneficiary through PCD/IVC from accumulation | Arc §2.3, §4, Appendix A |

## Transfer Matrix

| From FRI/IOPP side | Transfers to accumulation? | How | Boundary |
| --- | --- | --- | --- |
| Reed-Solomon proximity claims | yes | accumulator relation can track closeness to RS codewords | proximity alone is not an accumulator |
| quotienting over sampled points | yes | turns checked evaluations into a new lower-degree proximity claim | must preserve distance to support unbounded depth |
| list-decoding/out-of-domain samples | yes | binds prover to a unique nearby codeword in larger radius regimes | parameter and conjecture assumptions matter |
| Merkle-authenticated oracle access | yes | supports non-homomorphic, hash-based commitments to codewords | does not provide homomorphic VC semantics |
| FRI/STIR-style proximity literature | partial | provides RS proximity tools and intuition | original FRI/STARK security and DAS opening-consistency do not automatically transfer |
| IOR/Fiat-Shamir formalization | required by Arc | compiles oracle reductions into non-interactive reductions | this is Arc-specific extra machinery, not part of plain FRI |

## Non-Transfer Boundary

- Do not treat ordinary FRI as a complete accumulation scheme.
- Do not infer that FRI-style erasure-code commitments, DAS commitments, or full polynomial commitments are interchangeable.
- Do not transfer FRIDA's data-availability semantics into accumulation schemes.
- Do not transfer Arc's RS proximity route to arbitrary error-correcting codes without a source; BMNW24 supports any constant-distance linear code but only bounded depth, while Arc's unbounded route is RS-specific.
- Do not present list-decoding-radius efficiency as unconditional; Arc distinguishes proved Johnson-bound ranges from commonly used conjectural ranges.

## Evidence

| Source | Evidence | Confidence |
| --- | --- | --- |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] `Abstract`, `§1.1` | states the new tool is accumulation for proximity of claimed codewords to RS code and that it removes bounded accumulation depth. | high |
| Arc `§2.1`, `§6` | explains quotient-based, distance-preserving many-to-one reduction for RS proximity claims. | high |
| Arc `§2.2`, `§7` | lifts RS proximity accumulation to NP/R1CS accumulation. | high |
| Arc `§5`, Appendix B | formalizes IORs and compiles them with Merkle commitments and Fiat-Shamir into non-interactive reductions. | high |

## Propagation Targets

- [[fri-iopps|FRI IOPPs]]
- [[accumulation-schemes|Accumulation schemes]]
- [[recursive-proof-composition|Recursive proof composition]]
- [[recursion-and-folding|Recursion and folding]]

## 连接命题

- From: `zero-knowledge-proofs/proof-systems/fri-iopps`
- To: `zero-knowledge-proofs/recursion-and-folding/accumulation-schemes`
- Relation types: method_transfer, dependency, shared_pattern, formalization_bridge, transparent_hash_route
- Directionality: `from_to`
- Relationship thesis: RS proximity/list-decoding/quotienting patterns from FRI-family IOPPs can support unbounded hash-based accumulation when Arc's distance-preserving reduction and IOR wrapper are added.

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| RS proximity and low-degree codeword reasoning | accumulator relation | Arc §2.1, §6 | needs distance preservation |
| out-of-domain sampling | list-decoding-radius binding | Arc §2.1, §6.3, §7.15 | parameter/conjecture dependent |
| quotient-based claim update | many-to-one reduction | Arc §2.1, §6 | quotient degree and sampled points affect constraints |
| Merkle oracle commitments | hash-based accumulator commitments | Arc §3.3, §5.3, Appendix B | no homomorphic operations |

## 查询入口

- FRI IOPPs -> accumulation schemes
- FRI to accumulation
- Reed-Solomon proximity accumulation
- Arc RS proximity
- hash-based accumulation via IOPP

## 复核笔记

- Maturity: `active_seed`.
- Keep this bridge separate from [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]]: FRIDA transfers FRI opening-consistency into DAS commitments; Arc transfers RS proximity/list-decoding machinery into accumulation schemes.

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: original FRI/STIR/DEEP-FRI sources, BMNW24/Protostar/ProtoGalaxy/HyperNova sources, or any implementation source that changes Arc's practical assumptions.
