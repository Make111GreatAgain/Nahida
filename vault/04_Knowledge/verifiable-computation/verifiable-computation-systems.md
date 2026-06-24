---
id: "nahida-knowledge-verifiable-computation-systems"
title: "Verifiable computation systems"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "verifiable-computation-systems"
domain_id: "verifiable-computation"
direction_id: "verifiable-computation-systems"
parent_knowledge_refs:
  - "nahida-knowledge-verifiable-computation"
child_knowledge_refs:
  - "nahida-knowledge-qap-based-verifiable-computation-systems"
ontology_path:
  - "verifiable-computation"
  - "verifiable-computation-systems"
primary_ontology_path: "verifiable-computation/verifiable-computation-systems"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-verifiable-computation-systems"
    relation: "is_a"
    to: "nahida-knowledge-verifiable-computation"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md"
      - "vault/04_Knowledge/verifiable-computation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation-systems"
    relation: "has_child"
    to: "nahida-knowledge-qap-based-verifiable-computation-systems"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md"
      - "vault/04_Knowledge/verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-computation-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-verifiable-computation-systems-to-contingent-service-payments"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
  - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
  - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
  - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
representative_source_refs:
  - "doi:10.1109/SP.2015.23"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
  - "arxiv:2208.00283v2"
  - "doi:10.14778/3594512.3594513"
query_keys:
  - "Verifiable computation systems"
  - "verifiable-computation-systems"
  - "VC systems"
  - "function-independent preprocessing"
  - "vSQL"
  - "zk-vSQL"
  - "verifiable service"
  - "VSID"
  - "contingent service payment"
  - "ZKSQL"
  - "operator-at-a-time proofs"
  - "verifiable SQL query evaluation"
aliases:
  - "VC systems"
  - "function-independent preprocessing VC"
domains:
  - "verifiable-computation"
topics:
  - "verifiable-computation-systems"
  - "function-independent-preprocessing"
  - "zk-vsql"
  - "verifiable-services"
  - "verifiable-service-with-identifiable-abort"
  - "operator-at-a-time-proofs"
  - "zero-knowledge-sql"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260622-vsql-zk"
  - "nahida-knowledge-20260623-recurring-contingent-service-payment"
  - "nahida-knowledge-20260623-zksql"
source_refs:
  - "doi:10.1109/SP.2015.23"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
  - "arxiv:2208.00283v2"
  - "doi:10.14778/3594512.3594513"
confidence: "medium"
trust_tier: "primary"
---

# Verifiable computation systems

## 定义与范围

- 定义: Verifiable computation systems 把交互式证明、承诺、SNARK/QAP 等构件组织成可实现的计算外包和验证系统。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `verifiable-computation-systems`
- Aliases/query keys: VC systems
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `verifiable-computation-systems`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source-backed seed 来自 Geppetto，并和 LegoSNARK 的 modular/commit-and-prove 路线形成 bridge。zk-vSQL 新增一条 vSQL-style route: preprocessing 只依赖输入/见证长度上界而不是具体电路，再通过 zk-VPD 与承诺上的 CMT/sum-check 取得 zero-knowledge。ZKSQL 新增 SQL-facing VC system route: 把 commit-and-prove、VOLE-based ZK 与 set-based polynomial checks 组织成 operator-at-a-time query proof，而不是把整个 DBMS execution trace 作为 monolithic circuit。RC-S-P 额外提供了一个 payment-facing abstraction: `Verifiable Service (VS)` 把 PoR、verifiable computation、searchable encryption 和 information retrieval 都视为可验证服务；`VSID` 再增加 identifiable abort，使服务证明能进入 fair-exchange/payment protocol。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[verifiable-computation|verifiable-computation]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在不同 computation/circuit boundaries 上复用证明状态、减少 prover/verifier 成本并支持多阶段/多组件计算。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[verifiable-computation|verifiable-computation]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[qap-based-verifiable-computation-systems|qap-based-verifiable-computation-systems]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| QAP-based VC | QAP-based VC | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| state sharing | state sharing | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| commit-and-prove bridge | commit-and-prove bridge | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| function-independent preprocessing with zero-knowledge | 预处理只对输入/见证长度上界生成参数，具体电路在 evaluation phase 给出；用 CMT-over-commitments 与 zk-VPD 隐藏 witness 和中间值。 | 需要在 computation unknown at setup time 的场景保留低 verifier cost，并避免 universal circuit 的 concrete overhead。 | 仍是 trusted preprocessing 和交互式 argument；依赖 zk-VPD、同态承诺、ZKeq/ZKprod 与知识假设。 | [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] |
| operator-at-a-time verifiable SQL | 把 SQL plan 拆成 Project/Filter/Sort/Join/Aggregate 等 operator；每个 operator 输出 authenticated tags，并用 circuit 或 set-operation protocol 证明语义正确。 | 应用需要证明 ad-hoc SQL answer correctness/completeness，且可公开 schema/cardinality/query/DAG/answer。 | 不是完整 DBMS verification；不证明 transaction isolation、optimizer correctness 或 query privacy；padding 和 join 仍是瓶颈。 | [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] |
| verifiable service with identifiable abort | 把服务 proof 的验证接口升级为可归责接口: 客户端 metadata/query 必须 well-formed，争议时 arbiter 能识别 client/server/false complaint。 | 可验证服务要进入 payment/fair-exchange 协议，且客户端也可能作恶。 | 目前主要由 RC-S-P source 定义；通用路线可能需要 NIZK、签名和 bulletin board，PoR 例子可用 Merkle shortcut。 | [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto: Versatile Verifiable Computation]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | paper | source extension：zero-knowledge function-independent preprocessing VC argument | 不是完整 VC systems survey；vSQL/zk-VPD details 留在 source note，PCS/sum-check details 留在对应 knowledge node | `§1`, `§3-§6` |
| [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs]] | paper | source extension: operator-at-a-time commit-and-prove system for SQL query evaluation | SQL query semantics 留在 verifiable-database-queries；不代表通用 DBMS verification | §2-§5 |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | paper | source extension: VS/VSID abstraction and verifiable-service payment boundary | 不是 VC systems survey；RC-S-P/RC-PoR-P payment protocol details 留在 fair-exchange child node | §7, Appendix E-F |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前是 Geppetto seed；缺 Pinocchio、Pepper、SNARK compiler、zkVM 等系统来源。zk-vSQL 额外补了一条 VC-system source extension: function-independent preprocessing 可以与 zero-knowledge 结合，但它依赖 trusted preprocessing、同态承诺和知识假设，不应替代通用 VC systems foundation。ZKSQL 补充了另一条系统组织路线: VC machinery 可以按 SQL operator pipeline 组合，并通过 set-based polynomial checks 避免 sort/join 全部电路化；但 SQL answer semantics 应主要落到 [[verifiable-database-queries|Verifiable database queries]]，本节点只保存其 VC system pattern。RC-S-P 提供的是另一个角度: 当 VC/PoR/searchable-encryption 作为可付费服务时，普通 soundness 不够，系统还需要 client-input well-formedness 和 identifiable abort，才能把 proof correctness 接入 fair-exchange payment layer。

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
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto: Versatile Verifiable Computation]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | source extension | function-independent preprocessing zero-knowledge argument route | 背景; 方法族与解决路线; 代表 Sources; 当前综合 | no | keep vSQL as source note; route components through PCS/sum-check |
| [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] | source extension | operator-at-a-time commit-and-prove SQL route with set-based sort/join proofs | 背景; 方法族与解决路线; 代表 Sources; 当前综合 | no | keep SQL semantics under [[verifiable-database-queries|Verifiable database queries]] |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | source extension | VS/VSID abstraction and payment-facing identifiable abort route | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes, creates bridge | keep RC-S-P protocol details under [[contingent-service-payments|Contingent service payments for verifiable services]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[verifiable-computation-systems-to-contingent-service-payments|Verifiable computation systems -> contingent service payments]] | `verifiable-computation/verifiable-computation-systems; blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | dependency, application, payment_finality_boundary | service proof validity can feed payment protocols; escrow, deposits, privacy window and final coin distribution remain fair-exchange responsibilities. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-verifiable-computation-systems | is_a | nahida-knowledge-verifiable-computation | vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md; vault/04_Knowledge/verifiable-computation.md | medium | active_seed |
| nahida-knowledge-verifiable-computation-systems | has_child | nahida-knowledge-qap-based-verifiable-computation-systems | vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md; vault/04_Knowledge/verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems.md | medium | active_seed |
| nahida-knowledge-verifiable-computation-systems | evidenced_by | vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md | vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md | medium | active_seed |
| nahida-knowledge-verifiable-computation-systems | evidenced_by | vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md | zk-vSQL §1/§6 | medium | active_seed |
| nahida-knowledge-verifiable-computation-systems | evidenced_by | vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md | VS/VSID definitions and RC-S-P bridge | medium | active_seed |
| nahida-knowledge-verifiable-computation-systems | evidenced_by | vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md | ZKSQL operator-at-a-time commit-and-prove route | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Pinocchio/Pepper/modern zkVM systems 缺 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |
| vSQL original and function-independent VC comparison sources 缺。 | zk-vSQL 描述并扩展 vSQL，但当前还缺 vSQL original、Pepper/Pinocchio/Geppetto 对比来校准 function-independent preprocessing 的系统边界。 | nahida-update / nahida-research-search | medium | queued |
| SQL-facing VC system comparison sources 缺。 | ZKSQL 给出 operator-at-a-time SQL route，但还需要 CorrectDB/VeriDB/IntegriDB/vSQL 等来源校准 database verification 系统边界。 | nahida-update / nahida-research-search | medium | queued |
| Dedicated verifiable-service / VSID sources 缺。 | RC-S-P 给出 VS/VSID 定义，但还不能把 VSID 作为完整 foundation node；需要更多服务付款或 VC-with-abort sources。 | nahida-update / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 1 legacy notes | codex |
| 2026-06-22 | nahida-knowledge-20260622-vsql-zk | Added function-independent preprocessing zero-knowledge VC argument route from zk-vSQL. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-recurring-contingent-service-payment | Added VS/VSID as payment-facing verifiable-service route and linked to contingent service payments. | arxiv:2208.00283v2 | codex |
| 2026-06-23 | nahida-knowledge-20260623-zksql | Added ZKSQL as operator-at-a-time verifiable SQL computation route. | doi:10.14778/3594512.3594513 | codex |
