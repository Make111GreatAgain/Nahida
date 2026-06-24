---
id: "nahida-bridge-folding-schemes-to-sum-check-and-polynomial-commitments"
title: "Folding schemes -> sum-check and polynomial commitments"
original_title: "Folding schemes -> sum-check and polynomial commitments"
file_slug: "folding-schemes-to-sum-check-and-polynomial-commitments"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "dependency"
bridge_status: "active_seed"
endpoint_paths:
  - "zero-knowledge-proofs/recursion-and-folding/folding-schemes"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
  - "zero-knowledge-proofs/polynomial-commitments"
endpoint_knowledge_refs:
  - "nahida-knowledge-folding-schemes"
  - "nahida-knowledge-sum-check-protocol"
  - "nahida-knowledge-polynomial-commitments"
from_domain: "zero-knowledge-proofs"
to_domain: "verifiable-computation"
from_direction: "recursion-and-folding"
to_direction: "interactive-proofs"
from_topic: "folding-schemes"
to_topic: "sum-check-protocol"
relation_types:
  - "dependency"
  - "shared_pattern"
directionality: "uncertain"
relationship_thesis: "Nova separates recursion from final succinct proof compression. The folding layer maintains a running committed relaxed R1CS instance, while the compression layer uses a Spartan-style polynomial IOP, sum-check, and polynomial commitments to prove knowledge of a valid folded witness succinctly and in zero-knowledge."
transferability: "medium"
non_transfer_boundary: "需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-20"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "folding-schemes"
  - "sum-check-protocol"
  - "polynomial-commitments"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md"
knowledge_refs:
  - "nahida-knowledge-folding-schemes"
  - "nahida-knowledge-sum-check-protocol"
  - "nahida-knowledge-polynomial-commitments"
query_keys:
  - "Folding schemes -> sum-check and polynomial commitments"
created: "2026-06-11"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
source_refs:
  - "iacr:2021/370#p22-p27"
confidence: "medium"
trust_tier: "primary"
---

# Folding schemes -> sum-check and polynomial commitments

## 命名与路径

- Original title: Folding schemes -> sum-check and polynomial commitments
- File slug: `folding-schemes-to-sum-check-and-polynomial-commitments`
- Path safety check: migrated to `05_Bridges/folding-schemes-to-sum-check-and-polynomial-commitments.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/folding-schemes-to-sum-check-and-polynomial-commitments.md` 迁移而来。端点 knowledge refs 为: nahida-knowledge-folding-schemes, nahida-knowledge-sum-check-protocol, nahida-knowledge-polynomial-commitments。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: Folding schemes -> sum-check and polynomial commitments

## Relationship Thesis

Nova separates recursion from final succinct proof compression. The folding layer maintains a running committed relaxed R1CS instance, while the compression layer uses a Spartan-style polynomial IOP, sum-check, and polynomial commitments to prove knowledge of a valid folded witness succinctly and in zero-knowledge.

## Endpoints

| Endpoint | Role | Evidence |
| --- | --- | --- |
| `zero-knowledge-proofs/recursion-and-folding/folding-schemes` | primary recursion primitive | Nova §3-§5 |
| `verifiable-computation/interactive-proofs/sum-check-protocol` | polynomial IOP reduction inside compression SNARK | Nova §6.2 |
| `zero-knowledge-proofs/polynomial-commitments` | compiles polynomial IOP queries into zkSNARK commitments/proofs | Nova §6.3 |

## Transfer Matrix

| From | To | Transfer | Boundary |
| --- | --- | --- | --- |
| Sum-check | Nova compression | Reduces relaxed R1CS identity to random polynomial evaluation checks | Not used as the core per-step folding operation |
| Polynomial commitments | Nova compression | Commit/open MLEs and sparse polynomials for the Spartan-style zkSNARK | Nova uses PCBP/PCDory-style commitments, not KZG in this paper |
| Folding schemes | IVC | Maintains a running proof obligation without verifying a SNARK at each step | Folding alone does not provide succinct ZK proof |

## Non-Transfer Boundary

- Do not infer that all folding schemes require sum-check; Nova's committed relaxed R1CS folding does not.
- Do not infer that KZG is Nova's commitment backend; the paper discusses PCBP and PCDory paths.
- Do not infer that a sum-check protocol alone gives Nova-style recursion.

## Evidence

| Source | Evidence | Confidence |
| --- | --- | --- |
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova]] §5.2-§6 | Compression proof first folds the raw IVC proof, then uses a zkSNARK for committed relaxed R1CS built via polynomial IOP, sum-check, and commitments. | high |

## Propagation Targets

- [[folding-schemes|Folding schemes]]
- [[sum-check-protocol|Sum-check protocol]]
- [[polynomial-commitments|Polynomial commitments]]
- [[recursion-and-folding|Recursion and folding]]

## 连接命题

- From: `zero-knowledge-proofs/recursion-and-folding/folding-schemes`
- To: `verifiable-computation/interactive-proofs/sum-check-protocol`
- Relation types: dependency, shared_pattern
- Directionality: `uncertain`
- Relationship thesis: Nova separates recursion from final succinct proof compression. The folding layer maintains a running committed relaxed R1CS instance, while the compression layer uses a Spartan-style polynomial IOP, sum-check, and polynomial commitments to prove knowledge of a valid folded witness succinctly and in zero-knowledge.


## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| nahida-knowledge-folding-schemes | `zero-knowledge-proofs/recursion-and-folding/folding-schemes` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-sum-check-protocol | `verifiable-computation/interactive-proofs/sum-check-protocol` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-polynomial-commitments | `zero-knowledge-proofs/polynomial-commitments` | bridge endpoint | endpoint knowledge + source notes | active_seed |


## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `dependency, shared_pattern` | endpoint paths above | source notes and legacy bridge detail | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 |


## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| bridge relation | `zero-knowledge-proofs/recursion-and-folding/folding-schemes` | `verifiable-computation/interactive-proofs/sum-check-protocol` | dependency, shared_pattern | source notes / legacy detail | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 |


## 类比、依赖或关系边界

需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes]] | source_note_refs | active_seed |


## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `zero-knowledge-proofs/recursion-and-folding/folding-schemes` | update Bridge Links and relation_edges | active_seed |
| `verifiable-computation/interactive-proofs/sum-check-protocol` | update Bridge Links and relation_edges | active_seed |
| `zero-knowledge-proofs/polynomial-commitments` | update Bridge Links and relation_edges | active_seed |


## 查询入口

- Folding schemes -> sum-check and polynomial commitments


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |

## 刷新规则

- Last checked: `2026-06-20`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
