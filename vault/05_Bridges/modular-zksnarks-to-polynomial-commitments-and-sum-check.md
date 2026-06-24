---
id: "nahida-bridge-modular-zksnarks-to-polynomial-commitments-and-sum-check"
title: "Modular zkSNARKs -> polynomial commitments and sum-check"
original_title: "Modular zkSNARKs -> polynomial commitments and sum-check"
file_slug: "modular-zksnarks-to-polynomial-commitments-and-sum-check"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "dependency"
bridge_status: "active_seed"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/modular-zksnarks"
  - "zero-knowledge-proofs/polynomial-commitments"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
endpoint_knowledge_refs:
  - "nahida-knowledge-modular-zksnarks"
  - "nahida-knowledge-polynomial-commitments"
  - "nahida-knowledge-sum-check-protocol"
from_domain: "zero-knowledge-proofs"
to_domain: "zero-knowledge-proofs"
from_direction: "proof-systems"
to_direction: "polynomial-commitments"
from_topic: "modular-zksnarks"
to_topic: ""
relation_types:
  - "dependency"
  - "shared_pattern"
  - "implementation_reuse"
directionality: "uncertain"
relationship_thesis: "LegoSNARK uses polynomial commitments and sum-check not just as standalone verifiable-computation tools, but as reusable CP-SNARK gadgets inside a modular zkSNARK framework. This creates a dependency bridge from proof-system composition to polynomial-commitment and interactive-proof machinery."
transferability: "medium"
non_transfer_boundary: "需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-22"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "modular-zksnarks"
  - "polynomial-commitments"
  - "sum-check-protocol"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
  - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
knowledge_refs:
  - "nahida-knowledge-modular-zksnarks"
  - "nahida-knowledge-polynomial-commitments"
  - "nahida-knowledge-sum-check-protocol"
query_keys:
  - "Modular zkSNARKs -> polynomial commitments and sum-check"
  - "zk-vSQL PolyCom"
  - "zk-VPD modular zkSNARKs"
  - "sum-check over committed polynomials"
created: "2026-06-11"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260622-vsql-zk"
source_refs:
  - "iacr:2019/142#p20-p35"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44#sections-3-6"
confidence: "medium"
trust_tier: "primary"
---

# Modular zkSNARKs -> polynomial commitments and sum-check

## 命名与路径

- Original title: Modular zkSNARKs -> polynomial commitments and sum-check
- File slug: `modular-zksnarks-to-polynomial-commitments-and-sum-check`
- Path safety check: migrated to `05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md` 迁移而来。端点 knowledge refs 为: review。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: Modular zkSNARKs -> polynomial commitments and sum-check

## Bridge Thesis

LegoSNARK uses polynomial commitments and sum-check not just as standalone verifiable-computation tools, but as reusable CP-SNARK gadgets inside a modular zkSNARK framework. zk-vSQL supplies upstream primary evidence for the VPD/committed-evaluation and committed sum-check/CMT side of that bridge. This creates a dependency bridge from proof-system composition to polynomial-commitment and interactive-proof machinery.

## Endpoints

| Endpoint | Role |
| --- | --- |
| [[modular-zksnarks|Modular zkSNARKs]] | target proof-system design pattern |
| [[polynomial-commitments|Polynomial commitments]] | commitment backend for PolyCom, CPpoly, and committed polynomial factors |
| [[sum-check-protocol|Sum-check protocol]] | algebraic protocol adapted into CP gadgets such as `CPsc`, `CPhad`, and `CPmm` |

## Evidence

| Source | Evidence | Confidence |
| --- | --- | --- |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]] | Sections 5.1-5.6 construct PolyCom/CPpoly and sum-check-based CP gadgets; Section 6 composes them into LegoAC, LegoUAC, and matrix/parallel applications. | high |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | Sections 3-6 construct zk-VPD, sum-check over homomorphic commitments, CMT over homomorphic commitments, and a function-independent-preprocessing zero-knowledge argument. | high |

## Bridge Notes

- Polynomial commitments provide the committed object language for many gadgets.
- Sum-check provides the verifier-efficient algebraic reduction for products, matrix multiplication, and multilinear-extension identities.
- The proof-system layer decides how those gadgets are composed, linked, and benchmarked.
- zk-vSQL is an upstream component source rather than a modular zkSNARK framework: it proves that committed polynomial evaluation and committed sum-check/CMT can carry zero-knowledge, while LegoSNARK later uses related PolyCom/CP gadget machinery inside a modular composition framework.

## Review Needs

- zk-vSQL/PolyCom primary source absorbed on 2026-06-22; remaining comparison claims still need vSQL original and modern PCS/IOP sources.
- Absorb Thaler/CMT/GKR foundations for internal product and sum-check variants.
- Absorb modern PCS/IOP sources to compare whether the same modular design survives outside pairing-based trusted setup.

## 连接命题

- From: `zero-knowledge-proofs/proof-systems/modular-zksnarks`
- To: `zero-knowledge-proofs/polynomial-commitments`
- Relation types: dependency, shared_pattern, implementation_reuse
- Directionality: `uncertain`
- Relationship thesis: LegoSNARK uses polynomial commitments and sum-check not just as standalone verifiable-computation tools, but as reusable CP-SNARK gadgets inside a modular zkSNARK framework. This creates a dependency bridge from proof-system composition to polynomial-commitment and interactive-proof machinery.


## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| nahida-knowledge-modular-zksnarks | `zero-knowledge-proofs/proof-systems/modular-zksnarks` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-polynomial-commitments | `zero-knowledge-proofs/polynomial-commitments` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-sum-check-protocol | `verifiable-computation/interactive-proofs/sum-check-protocol` | bridge endpoint | endpoint knowledge + source notes | active_seed |


## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `dependency, shared_pattern, implementation_reuse` | endpoint paths above | source notes and legacy bridge detail | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 |


## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| bridge relation | `zero-knowledge-proofs/proof-systems/modular-zksnarks` | `zero-knowledge-proofs/polynomial-commitments` | dependency, shared_pattern, implementation_reuse | source notes / legacy detail | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 |


## 类比、依赖或关系边界

需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs]] | source_note_refs | active_seed |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | source_note_refs / upstream PolyCom and committed sum-check calibration | active_seed |


## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/modular-zksnarks` | update Bridge Links and relation_edges | active_seed |
| `zero-knowledge-proofs/polynomial-commitments` | update Bridge Links and relation_edges | active_seed |
| `verifiable-computation/interactive-proofs/sum-check-protocol` | update Bridge Links and relation_edges | active_seed |


## 查询入口

- Modular zkSNARKs -> polynomial commitments and sum-check


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | Evidence / Review Needs / transfer boundary | closes the zk-vSQL primary-source gap for PolyCom-style committed polynomial evaluation and committed sum-check/CMT evidence | active_seed |

## 刷新规则

- Last checked: `2026-06-22`
- Valid until: `2026-07-22`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-vsql-zk | Added zk-vSQL as upstream source evidence for zk-VPD, committed sum-check and CMT-over-commitments; closed primary-source review need. | 1 source note | codex |
