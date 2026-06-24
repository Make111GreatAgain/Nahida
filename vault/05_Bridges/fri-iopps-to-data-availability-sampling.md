---
id: "nahida-bridge-fri-iopps-to-data-availability-sampling"
title: "FRI IOPPs -> data availability sampling"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "fri-iopps"
  - "data-availability-sampling"
  - "erasure-code-commitments"
endpoint_knowledge_refs:
  - "nahida-knowledge-fri-iopps"
  - "nahida-knowledge-data-availability-sampling"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/fri-iopps"
  - "blockchain-systems/data-availability-and-light-clients/data-availability-sampling"
relation_types:
  - "method_transfer"
  - "application"
  - "dependency"
  - "transparent_commitment_route"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
representative_source_refs:
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
query_keys:
  - "FRI data availability"
  - "FRIDA"
  - "FRI IOPPs to DAS"
  - "transparent data availability commitments"
  - "erasure code commitments from IOPP"
aliases:
  - "FRIDA bridge"
  - "FRI-based DAS"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
  - "verifiable-computation"
topics:
  - "fri-iopps"
  - "data-availability-sampling"
  - "erasure-code-commitments"
  - "opening-consistency"
tags:
  - "nahida/bridge"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-frida-data-availability-from-fri"
source_refs:
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
confidence: "high"
trust_tier: "primary"
---

# FRI IOPPs -> data availability sampling

## 关系命题

FRI IOPPs can transfer into data availability sampling when the proof-system layer is strengthened from ordinary proximity soundness to opening-consistency. [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] shows this transfer concretely: an opening-consistent, non-adaptive, query-selectable IOPP can be compiled into an erasure-code commitment; the HASW23 transformation then turns that commitment into a DAS scheme for light clients.

This bridge does not mean FRI proves blockchain state validity. It means FRI's Reed-Solomon proximity, folding, random-query and Merkle-authenticated oracle machinery can serve the commitment/opening layer needed by DAS.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[fri-iopps|FRI IOPPs]] | `zero-knowledge-proofs/proof-systems/fri-iopps` | proof-system method family: RS proximity, recursive folding, query consistency, opening-consistency | transparent IOPP / proximity proof |
| [[data-availability-sampling|Data availability sampling]] | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | light-client availability problem: sample encoded data and verify openings without downloading all data | blockchain light-client problem |

## Transfer Matrix

| From FRI/IOPP | Transfers to DAS? | How | Boundary |
| --- | --- | --- | --- |
| Reed-Solomon proximity | yes | DAS encodes data as an erasure-coded word; proximity proof supports consistency with a codeword | proximity alone is insufficient for opened-position consistency |
| Merkle-authenticated oracle access | yes | encoded symbols and proof oracles can be committed/opened with Merkle paths | random-oracle/Merkle extraction assumptions remain |
| Recursive folding | yes | reduces proof/opening size through FRI layers | parameter choices affect encoding size and query overhead |
| Query-selectable verifier | yes | `QSelect` lets an opening force the final verifier query to include the target base position | not every IOPP is query-selectable without adaptation |
| Opening-consistency | yes, essential | ensures queried base symbols match the unique closest codeword, giving code-binding | ordinary IOPP soundness does not imply this |
| Batched FRI | yes | interleaved RS + random linear combination reduces encoding/opening size | adds batch collision/distortion analysis and parameter trade-offs |

## Non-Transfer Boundary

- DAS availability is not transaction validity, execution correctness, fraud proof or validity proof.
- FRI as used by FRIDA is not automatically a full polynomial commitment API over arbitrary field points.
- FRIDA improves commitment/per-query size but can make network encoding/storage much larger.
- The bridge does not replace KZG/Tensor/Hash DAS comparisons; it records a transparent/no-trusted-setup route.
- The original FRI/STARK foundation still needs primary sources beyond FRIDA.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] §3 | opening-consistent IOPP -> erasure-code commitment compiler | relies on random oracle and Merkle extraction |
| FRIDA §4 | FRI satisfies opening-consistency | not original FRI foundation source |
| FRIDA Appendix C | batched FRI satisfies opening-consistency | current vault has one source only |
| FRIDA §5 | light-client commitment/query improvements and encoding-size trade-off | network storage can be much larger |
| FRIDA Appendix A | erasure-code commitment -> DAS transformation background | formal transformation belongs to HASW23 |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[fri-iopps|FRI IOPPs]] | Create method-family seed with opening-consistency and batched FRI route | done |
| [[data-availability-sampling|Data availability sampling]] | Add FRIDA source extension and transparent FRI/erasure-code-commitment method route | done |
| [[polynomial-commitments|Polynomial commitments]] | Add boundary note: FRIDA uses erasure-code commitment route, not full PCS semantics | done |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| opening-consistent IOPP | `zero-knowledge-proofs/proof-systems/fri-iopps` | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | method_transfer via erasure-code commitments | FRIDA §3-§4 | treating proximity soundness as code-binding without opening-consistency |
| Merkle/FRI transparent commitment route | `zero-knowledge-proofs/proof-systems/fri-iopps` | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | application route | FRIDA §5 | ignoring larger encoding/network storage |
| batched FRI | `zero-knowledge-proofs/proof-systems/fri-iopps` | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | parameterized optimization | FRIDA §4.3, Appendix C | one-source seed; implementation evidence missing |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[fri-iopps|FRI IOPPs]] | definition, methods, bridge links | new method-family seed | active_seed |
| [[data-availability-sampling|Data availability sampling]] | methods, representatives, bridge links | FRIDA adds transparent DAS route | active_seed |
| [[data-availability-and-light-clients|Data availability and light clients]] | methods and current synthesis | light-client data availability trade-off updated | active_seed |
| [[polynomial-commitments|Polynomial commitments]] | source extension/boundary | FRIDA contrasts FRI erasure-code commitment with FRI PCS use | active_seed |

## 查询入口

- FRIDA 解决了 DAS 的什么问题?
- FRI 为什么可以用于 data availability sampling?
- opening-consistency 和普通 IOPP soundness 有什么区别?
- FRI-based DAS 和 KZG/Tensor/Hash-based DAS 的取舍是什么?
- FRI 是 polynomial commitment 吗，还是 erasure-code commitment?

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-frida-data-availability-from-fri | Created bridge from FRI IOPPs to data availability sampling using FRIDA. | 1 source note | codex |
