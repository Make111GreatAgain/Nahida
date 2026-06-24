---
id: "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
title: "Memory-efficient SNARKs -> KZG commitments"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "memory-efficient-snarks"
  - "kzg-commitments"
  - "elastic-snarks"
  - "streaming-r1cs"
  - "plonkish-snarks"
  - "multilinear-kzg"
endpoint_knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-kzg-commitments"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
relation_types:
  - "dependency"
  - "method_transfer"
  - "implementation_reuse"
  - "prover_space_reduction"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
  - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
representative_source_refs:
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
query_keys:
  - "elastic KZG"
  - "streaming KZG"
  - "Gemini KZG"
  - "Epistle multilinear KZG"
  - "elastic multilinear KZG"
  - "memory-efficient SNARK KZG"
  - "elastic SNARK polynomial commitment"
aliases:
  - "Elastic SNARKs to KZG"
domains:
  - "zero-knowledge-proofs"
topics:
  - "memory-efficient-snarks"
  - "kzg-commitments"
  - "elastic-snarks"
  - "polynomial-commitments"
  - "multilinear-kzg"
tags:
  - "nahida/bridge"
created: "2026-06-22"
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

# Memory-efficient SNARKs -> KZG commitments

## 关系命题

Gemini shows that low-memory SNARK construction needs more than a streaming-friendly constraint-system prover. The polynomial commitment layer must also admit streaming commitment and opening algorithms. In Gemini, KZG commitments fill that role for an R1CS elastic SNARK: commitment can be computed by streaming coefficient/SRS pairs into a running group sum, and opening can be computed by streaming quotient-witness coefficients via Ruffini-style recurrence.

Epistle extends the same bridge to the Plonkish/HyperPlonk route: multilinear KZG can also be realized elastically, with streaming commitment and a stack-based streaming opening algorithm over multilinear decomposition witnesses. This bridge therefore records a dependency from [[memory-efficient-snarks|Memory-efficient SNARKs]] to [[kzg-commitments|KZG commitments]]: KZG-family polynomial commitments can be reused as a streaming PCS layer inside source-backed elastic SNARK compilers, while KZG trust/setup assumptions remain intact.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | prover memory, pass complexity, streaming/elastic proof-system design | ZKP proof-system problem |
| [[kzg-commitments|KZG commitments]] | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | succinct polynomial commitment/opening layer with streaming realizations in Gemini and Epistle | PCS problem |

## Transfer Matrix

| From KZG commitments | Transfers to memory-efficient SNARKs? | How | Boundary |
| --- | --- | --- | --- |
| Constant-size commitments/openings | yes | preserves succinct commitment/opening interface for compiled elastic argument | does not remove KZG trusted setup or pairing assumptions |
| Coefficient/SRS linearity | yes | commitment can be streamed as a running group sum over coefficient-key pairs | requires ordered stream access to coefficients and commitment key |
| Quotient witness opening | yes | opening witness can be generated with small state using a recurrence over high-to-low coefficients | exact opening/batching protocol remains Gemini-specific |
| Multilinear decomposition witnesses | yes | Epistle's multilinear KZG opening generates `O(log N)` witness group elements with a small stack over input/SRS streams | exact algorithm is tied to multilinear KZG and Plonkish/HyperPlonk context |
| Batched openings | yes | reduces many PIOP oracle openings into a compact KZG opening layer | batching details do not transfer to all PCS or all SNARKs |
| PCS security assumptions | no | Gemini inherits KZG-style assumptions | KZG is an enabling layer, not a general low-memory SNARK theorem |

## Non-Transfer Boundary

- KZG does not make every SNARK memory-efficient; the PIOP and constraint-system layer must also be streaming-compatible.
- Gemini/Epistle elastic realizations do not eliminate trusted setup, pairing assumptions or universal SRS concerns.
- KZG is not the only possible PCS route for low-memory SNARKs; DARK/FRI/IPA-style comparisons still require separate primary sources.
- The arkworks/hyperplonk implementation evidence belongs to source notes and should not be generalized to all KZG deployments.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] §2.2 | elastic PIOP + elastic polynomial commitment compiles to an elastic argument | compiler assumes compatible message/commitment streams |
| Gemini §2.3, §9 | KZG commitment/opening can be realized with small streaming state | KZG setup/trust assumptions remain |
| Gemini §10 | final elastic argument system uses the elastic PC layer | proof-system result is R1CS-focused |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] §6 | multilinear KZG commitment/opening can be realized elastically with streaming commit/open | KZG setup/trust assumptions remain |
| Epistle §5-§7 | final Plonkish elastic argument uses the elastic multilinear KZG layer and reports implementation evidence | lookup and benchmark boundaries remain source-specific |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | Add elastic SNARK / streaming R1CS and Plonkish routes and this bridge | done |
| [[elastic-snarks|Elastic SNARKs]] | Track R1CS vs Plonkish elastic SNARK routes | done |
| [[kzg-commitments|KZG commitments]] | Add elastic KZG and elastic multilinear KZG source extensions and this bridge | done |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-gemini-elastic-snarks | Created bridge from memory-efficient SNARKs to KZG commitments using Gemini. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-epistle-elastic-snarks | Added Epistle evidence that multilinear KZG can serve as the streaming PCS layer for Plonkish elastic SNARKs. | 1 source note | codex |
