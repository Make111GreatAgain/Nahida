---
id: "nahida-knowledge-modular-zksnarks"
title: "Modular zkSNARKs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "modular-zksnarks"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-zk-snarks"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "modular-zksnarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/modular-zksnarks"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-modular-zksnarks"
    relation: "depends_on"
    to: "nahida-knowledge-commit-and-prove-arguments"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/commit-and-prove-arguments.md"
      - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-modular-zksnarks"
    relation: "is_a"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-modular-zksnarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-modular-zksnarks"
    relation: "bridges_to"
    to: "nahida-bridge-modular-zksnarks-to-polynomial-commitments-and-sum-check"
    evidence_refs:
      - "vault/05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-modular-zksnarks"
    relation: "bridges_to"
    to: "nahida-bridge-qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove"
    evidence_refs:
      - "vault/05_Bridges/qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-modular-zksnarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-modular-zksnarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
      - "vault/05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
  - "nahida-bridge-modular-zksnarks-to-polynomial-commitments-and-sum-check"
  - "nahida-bridge-qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
  - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
  - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
representative_source_refs:
  - "iacr:2019/142"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
query_keys:
  - "Modular zkSNARKs"
  - "modular-zksnarks"
  - "LegoSNARK"
  - "commit-and-prove arguments"
  - "commit-and-prove SNARKs"
  - "commit-carrying SNARKs"
  - "commit-and-fold"
  - "Mangrove commit-and-prove"
  - "zk-vSQL"
  - "PolyCom"
  - "zero-knowledge verifiable polynomial delegation"
aliases:
  - "LegoSNARK"
  - "commit-and-prove SNARKs"
  - "commit-carrying SNARKs"
  - "zk-vSQL"
domains:
  - "zero-knowledge-proofs"
topics:
  - "modular-zksnarks"
  - "zk-vpd"
  - "function-independent-preprocessing"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-22"
created: "2026-06-20"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-mangrove"
  - "nahida-knowledge-20260621-zkcplus-fair-exchange"
  - "nahida-knowledge-20260622-vsql-zk"
source_refs:
  - "iacr:2019/142"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
confidence: "medium"
trust_tier: "primary"
---

# Modular zkSNARKs

## 定义与范围

- 定义: Modular zkSNARKs 关注把 SNARK 组件模块化组合，使不同关系、承诺和子证明能以可组合方式连接。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `modular-zksnarks`
- Aliases/query keys: LegoSNARK, commit-and-prove SNARKs, commit-carrying SNARKs
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `modular-zksnarks`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source seed 是 LegoSNARK；[[commit-and-prove-arguments|Commit-and-prove arguments]] 已经由 ZKCPlus、LegoSNARK、Geppetto、SAVER 和 Mangrove 的多来源 evidence 拆成独立 foundation-thin 方法族。本节点只保留 SNARK-specific modular composition 问题: 如何把 proof gadgets、commitment-linked components 和 specialized relations 组合为 zkSNARK framework。Mangrove 提供一个 source extension: 它的 witness chunk commitments 可被拉出为 statement commitments，从而支持 commit-and-prove 式 witness reuse，但该扩展仍服务 low-memory SNARK construction，不替代 LegoSNARK 的 modular SNARK framework。vSQL zero-knowledge source 补的是上游构件证据: zk-VPD、承诺上的 sum-check/CMT 后续可被 LegoSNARK/PolyCom-style gadgets 复用，但 vSQL 本身不升级为 modular zkSNARK 节点。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[zk-snarks|zk-snarks]], [[commit-and-prove-arguments|Commit-and-prove arguments]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

解决 monolithic SNARK 难以复用、组合和跨组件传递 witness/commitment 的问题。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zk-snarks|zk-snarks]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| commit-and-prove interface | commit-and-prove interface | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| commit-carrying composition | commit-carrying composition | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| modular proof components | modular proof components | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| committed witness reuse in low-memory SNARKs | 将 prover witness chunk commitments 从 proving protocol 拉入 statement，使不同 proofs 可连接或复用部分 witness commitments。 | committed witness subdomains 能与 PCD tree chunks/subtrees 对齐。 | 当前只来自 Mangrove §7.2；不等同 LegoSNARK 全框架，也不解决不均匀 witness sizes 下的 tree imbalance。 | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] |
| zk-VPD / committed polynomial-evaluation gadgets | 用 zero-knowledge verifiable polynomial delegation 证明 committed polynomial evaluation 的正确性，并用同态承诺隐藏 sum-check/CMT 中的中间值。 | 需要把 polynomial commitment / sum-check machinery 作为 proof gadget 复用，而不是把所有 relation 编译进单一通用电路。 | 这是 vSQL/zk-vSQL 上游构件证据；不是 LegoSNARK 的完整 CP-SNARK framework，也不说明所有 PCS 都可直接替代。 | [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]]; [[modular-zksnarks-to-polynomial-commitments-and-sum-check|bridge]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | paper | commit-and-prove source extension：witness chunk commitments 可作为 statement 复用 | 这是 Mangrove §7.2 扩展；主问题仍是 memory-efficient SNARKs | `p48-p49` |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | paper | 上游构件 source extension：zk-VPD、承诺上的 sum-check/CMT 给 PolyCom/CP-style gadgets 提供 primary calibration | 不是 modular zkSNARK framework；具体 protocol details 留在 source note 和 [[polynomial-commitments|Polynomial commitments]] / [[sum-check-protocol|Sum-check protocol]] | `§3-§6` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-22`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: Modular zkSNARKs 是 zk-SNARKs 下的 problem/method node；LegoSNARK 是 representative source。Mangrove 新增一个 narrow source extension: low-memory SNARK 构造中的 chunk commitments 也可被改造成 commit-and-prove interface，但它没有替代 LegoSNARK 的完整 modular/CP-SNARK framework。vSQL zero-knowledge source 补齐了 bridge 里等待的 PolyCom/zk-VPD primary calibration: 它说明 committed polynomial evaluation、承诺上的 sum-check 和 CMT 可作为可复用 proof machinery，但 vSQL 自身仍应保留为 source/protocol instance。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | source extension | committed witness reuse / CP-SNARK compatibility in a low-memory SNARK | 方法族与解决路线; 代表 Sources; 当前综合 | no | keep detailed protocol in source note and [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | boundary/source-extension trigger | CP-NIZK is now routed through [[commit-and-prove-arguments|Commit-and-prove arguments]], not folded into modular-zksnarks. | 定义与范围; 背景; Bridge Links | yes | keep ZKCPlus protocol details in source note and fair-exchange bridge |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | upstream gadget source extension | zk-VPD and commitment-wrapped sum-check/CMT calibrate the PolyCom dependency side of the modular-zksnarks bridge. | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | keep vSQL as source note; refresh bridge evidence |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[modular-zksnarks-to-polynomial-commitments-and-sum-check|Modular zkSNARKs -> polynomial commitments and sum-check]] | `zero-knowledge-proofs/proof-systems/modular-zksnarks; zero-knowledge-proofs/polynomial-commitments; verifiable-computation/interactive-proofs/sum-check-protocol` | dependency, shared_pattern, implementation_reuse | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 | active_seed |
| [[qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove|QAP-based VC systems -> modular zkSNARKs and commit-and-prove]] | `verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems; zero-knowledge-proofs/proof-systems/modular-zksnarks` | shared_pattern, dependency, translation | Geppetto's MultiQAPs are tied to QAP/Pinocchio-style compiled VC and programmer-guided C libraries. LegoSNARK is a broader framework for composing CP-SNARK gadgets and lifting cc-SNARKs; it does not inherit Geppetto's compiler/runtime model wholesale. | active_seed |
| [[commit-and-prove-arguments-to-fair-exchange-protocols|Commit-and-prove arguments -> blockchain fair exchange protocols]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; blockchain-systems/execution-and-transactions/fair-exchange-protocols` | application, dependency | This bridge is CP-wide rather than modular-zkSNARK-specific; it is linked here only to preserve the CP boundary. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-modular-zksnarks | is_a | nahida-knowledge-zk-snarks | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md; vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md | medium | active_seed |
| nahida-knowledge-modular-zksnarks | depends_on | nahida-knowledge-commit-and-prove-arguments | commit-and-prove arguments node; LegoSNARK source note | high | active_seed |
| nahida-knowledge-modular-zksnarks | evidenced_by | vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md | vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md | medium | active_seed |
| nahida-knowledge-modular-zksnarks | bridges_to | nahida-bridge-modular-zksnarks-to-polynomial-commitments-and-sum-check | vault/05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md | medium | active_seed |
| nahida-knowledge-modular-zksnarks | bridges_to | nahida-bridge-qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove | vault/05_Bridges/qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove.md | medium | active_seed |
| nahida-knowledge-modular-zksnarks | evidenced_by | vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md | Mangrove §7.2 | medium | active_seed |
| nahida-knowledge-modular-zksnarks | evidenced_by | vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md | zk-vSQL §3-§6; bridge calibration | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 其他 modular SNARK frameworks 和 universal SNARK sources 缺。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 3 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-mangrove | Added narrow commit-and-prove witness-reuse source extension from Mangrove §7.2. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcplus-fair-exchange | Split CP into [[commit-and-prove-arguments|Commit-and-prove arguments]] and kept this node scoped to modular zkSNARK composition. | doi:10.1145/3460120.3484558 | codex |
| 2026-06-22 | nahida-knowledge-20260622-vsql-zk | Added zk-vSQL as upstream PolyCom/zk-VPD source evidence for the polynomial-commitment and sum-check bridge. | sha256:17844a65dcd5 | codex |
