---
id: "nahida-bridge-qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove"
title: "QAP-based VC systems -> modular zkSNARKs and commit-and-prove"
original_title: "QAP-based VC systems -> modular zkSNARKs and commit-and-prove"
file_slug: "qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "shared_pattern"
bridge_status: "active_seed"
endpoint_paths:
  - "verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems"
  - "zero-knowledge-proofs/proof-systems/modular-zksnarks"
endpoint_knowledge_refs:
  - "nahida-knowledge-qap-based-verifiable-computation-systems"
  - "nahida-knowledge-modular-zksnarks"
from_domain: "verifiable-computation"
to_domain: "zero-knowledge-proofs"
from_direction: "verifiable-computation-systems"
to_direction: "proof-systems"
from_topic: "qap-based-verifiable-computation-systems"
to_topic: "modular-zksnarks"
relation_types:
  - "shared_pattern"
  - "dependency"
  - "translation"
directionality: "uncertain"
relationship_thesis: "QAP-based VC systems and modular zkSNARKs share a commit-and-prove pattern: hidden state is represented by succinct commitments/digests that can be reused across proof components. Geppetto provides the current VC-system source extension for scheduled MultiQAP state sharing, while LegoSNARK provides the current proof-system source extension for modular CP-SNARK composition and commitment-linking."
transferability: "medium"
non_transfer_boundary: "Geppetto's MultiQAPs are tied to QAP/Pinocchio-style compiled VC and programmer-guided C libraries. LegoSNARK is a broader framework for composing CP-SNARK gadgets and lifting cc-SNARKs; it does not inherit Geppetto's compiler/runtime model wholesale."
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-20"
domains:
  - "verifiable-computation"
  - "zero-knowledge-proofs"
topics:
  - "qap-based-vc-systems"
  - "modular-zksnarks"
  - "commit-and-prove-snarks"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
  - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
knowledge_refs:
  - "nahida-knowledge-qap-based-verifiable-computation-systems"
  - "nahida-knowledge-modular-zksnarks"
query_keys:
  - "QAP-based VC systems -> modular zkSNARKs and commit-and-prove"
created: "2026-06-19"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
source_refs:
  - "doi:10.1109/SP.2015.23"
  - "iacr:2019/142"
confidence: "medium"
trust_tier: "primary"
---

# QAP-based VC systems -> modular zkSNARKs and commit-and-prove

## 命名与路径

- Original title: QAP-based VC systems -> modular zkSNARKs and commit-and-prove
- File slug: `qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove`
- Path safety check: migrated to `05_Bridges/qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove.md` 迁移而来。端点 knowledge refs 为: review。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: QAP-based VC systems -> modular zkSNARKs and commit-and-prove

## Bridge Thesis

QAP-based VC systems and modular zkSNARKs share a commit-and-prove pattern: hidden state is represented by succinct commitments/digests that can be reused across proof components. Geppetto provides the current VC-system source extension for scheduled MultiQAP state sharing, while LegoSNARK provides the current proof-system source extension for modular CP-SNARK composition and commitment-linking.

## Endpoints

| Endpoint | Role |
| --- | --- |
| [[qap-based-verifiable-computation-systems|QAP-based VC systems]] | systems-oriented VC topic covering MultiQAP banks/buses, scheduled CP proofs, compiler/runtime constraints, and proof aggregation |
| [[modular-zksnarks|Commit-and-prove SNARKs]] | proof-system interface for proving relations over committed witness slots |
| [[modular-zksnarks|Modular zkSNARKs]] | higher-level modular proof-system design pattern |

## Transfer Matrix

| Transfer | VC-system side | Modular zkSNARK side |
| --- | --- | --- |
| Shared state interface | bus digests connect sub-QAPs | committed slots connect proof gadgets |
| Consistency condition | binding bus digests | binding commitment scheme or CPlink |
| Composition unit | proof schedule over outsourced functions | conjunction/sequential composition of CP gadgets |
| System pressure | prover/compiler practicality | proof-system interoperability and specialization |

## Non-Transfer Boundary

Geppetto's MultiQAPs are tied to QAP/Pinocchio-style compiled VC and programmer-guided C libraries. LegoSNARK is a broader framework for composing CP-SNARK gadgets and lifting cc-SNARKs; it does not inherit Geppetto's compiler/runtime model wholesale.

## Evidence

| Source | Evidence | Confidence |
| --- | --- | --- |
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto]] | Defines CP schemes, scheduled soundness, banks/buses, and MultiQAP state-sharing. | high |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]] | Discusses existing CP/cc-SNARKs including Geppetto and builds a CP-SNARK composition/lifting framework. | high |

## Review Needs

- Absorb Pinocchio and Groth16 to clarify the exact proof-system lineage.
- Absorb Geppetto full ePrint 2014/976 if proof details become important.
- Avoid claiming direct influence beyond the papers' explicit related-work/definition overlap unless supported by sources.

## 连接命题

- From: `verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems`
- To: `zero-knowledge-proofs/proof-systems/modular-zksnarks`
- Relation types: shared_pattern, dependency, translation
- Directionality: `uncertain`
- Relationship thesis: QAP-based VC systems and modular zkSNARKs share a commit-and-prove pattern: hidden state is represented by succinct commitments/digests that can be reused across proof components. Geppetto provides the current VC-system source extension for scheduled MultiQAP state sharing, while LegoSNARK provides the current proof-system source extension for modular CP-SNARK composition and commitment-linking.


## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| nahida-knowledge-qap-based-verifiable-computation-systems | `verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-modular-zksnarks | `zero-knowledge-proofs/proof-systems/modular-zksnarks` | bridge endpoint | endpoint knowledge + source notes | active_seed |


## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `shared_pattern, dependency, translation` | endpoint paths above | source notes and legacy bridge detail | Geppetto's MultiQAPs are tied to QAP/Pinocchio-style compiled VC and programmer-guided C libraries. LegoSNARK is a broader framework for composing CP-SNARK gadgets and lifting cc-SNARKs; it does not inherit Geppetto's compiler/runtime model wholesale. |


## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| bridge relation | `verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems` | `zero-knowledge-proofs/proof-systems/modular-zksnarks` | shared_pattern, dependency, translation | source notes / legacy detail | Geppetto's MultiQAPs are tied to QAP/Pinocchio-style compiled VC and programmer-guided C libraries. LegoSNARK is a broader framework for composing CP-SNARK gadgets and lifting cc-SNARKs; it does not inherit Geppetto's compiler/runtime model wholesale. |


## 类比、依赖或关系边界

Geppetto's MultiQAPs are tied to QAP/Pinocchio-style compiled VC and programmer-guided C libraries. LegoSNARK is a broader framework for composing CP-SNARK gadgets and lifting cc-SNARKs; it does not inherit Geppetto's compiler/runtime model wholesale.


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation]] | source_note_refs | active_seed |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs]] | source_note_refs | active_seed |


## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems` | update Bridge Links and relation_edges | active_seed |
| `zero-knowledge-proofs/proof-systems/modular-zksnarks` | update Bridge Links and relation_edges | active_seed |


## 查询入口

- QAP-based VC systems -> modular zkSNARKs and commit-and-prove


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
