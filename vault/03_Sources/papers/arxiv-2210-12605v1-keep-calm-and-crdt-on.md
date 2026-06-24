---
id: "arxiv:2210.12605v1"
title: "Keep CALM and CRDT On"
type: "source"
source_kind: "paper"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
hierarchy_level: "source"
created: "2026-06-24"
updated: "2026-06-24"
authors:
  - "Shadaj Laddad"
  - "Conor Power"
  - "Mae Milano"
  - "Alvin Cheung"
  - "Natacha Crooks"
  - "Joseph M. Hellerstein"
year: 2022
venue: "arXiv preprint"
publisher: "arXiv"
source_refs:
  - "arxiv:2210.12605v1"
canonical_url: "https://arxiv.org/abs/2210.12605v1"
doi: ""
arxiv_id: "2210.12605v1"
local_pdf_path: "~/Desktop/paper/vldb23_calm_and_crdt.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/keep-calm-and-crdt-on-36a95743b0e0-pages.txt"
inventory_path: "vault/02_Raw/pdf/extracted/keep-calm-and-crdt-on-36a95743b0e0-inventory.json"
pages: 8
pdf_sha256: "36a95743b0e0854454da8960cecf1bbe78d30e8b5c2e769e021a51e3b50ab726"
pdf_extractor: "codex-bundled-python:pypdf"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "title, authors, abstract and introduction"
  - "Section 2 CRDT overview, state-based CRDTs, op-based CRDTs and practice snapshot"
  - "Section 3 query model, safe examples, monotonicity and non-monotone coordination boundary"
  - "Section 4 query languages, CRDT data stores, optimization opportunities and weak consistency tradeoffs"
  - "Sections 5-6 related work, research agenda and conclusion"
  - "references for CALM, BloomL, Lasp, Datafun, CRDT foundations and CRDT production systems"
safe_for_absorption: true
primary_domain: "distributed-systems"
primary_direction: "data-management-and-storage"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
primary_ontology_path: "distributed-systems/data-management-and-storage/conflict-free-replicated-data-types"
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "conflict-free-replicated-data-types"
secondary_ontology_paths:
  - "distributed-systems/data-management-and-storage"
topic_ids:
  - "conflict-free-replicated-data-types"
  - "crdt-query-models"
  - "calm-theorem"
  - "monotone-queries"
  - "coordination-free-replication"
  - "crdt-data-stores"
domains:
  - "distributed-systems"
topics:
  - "CRDTs"
  - "CALM theorem"
  - "monotone queries"
  - "coordination-free replication"
  - "CRDT data stores"
aliases:
  - "Keep CALM and CRDT On"
  - "CALM-based CRDT query model"
  - "CRDT monotone query model"
tags:
  - "nahida/source"
  - "paper"
  - "crdts"
  - "distributed-systems"
classification_status: "corrected_absorbed"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p8"
  - "metadata and first page confirm title, authors, arXiv id and 2022 date"
  - "abstract and Section 3 identify the primary contribution as a CALM-based query model for CRDT observations"
  - "Section 4 frames a CRDT data-store agenda with query language, optimizer, storage representation, GC and non-monotone tradeoffs"
  - "queue path crdts was normalized to conflict-free-replicated-data-types"
knowledge_node_refs:
  - "[[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]"
  - "[[conflict-free-replicated-data-types|Conflict-free replicated data types]]"
bridge_refs: []
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "item0118"
run_id: "nahida-knowledge-20260624-keep-calm-crdt-query-model"
managed_by: "nahida"
confidence: "high"
trust_tier: "primary"
---

# Keep CALM and CRDT On

## Paper Identity

| 字段 | 内容 |
| --- | --- |
| 论文 | Keep CALM and CRDT On |
| 作者 | Shadaj Laddad; Conor Power; Mae Milano; Alvin Cheung; Natacha Crooks; Joseph M. Hellerstein |
| 机构 | University of California, Berkeley |
| 年份 | 2022 |
| 版本 | arXiv `2210.12605v1` |
| 本地 PDF | `~/Desktop/paper/vldb23_calm_and_crdt.pdf` |
| 抽取文本 | `vault/02_Raw/pdf/extracted/keep-calm-and-crdt-on-36a95743b0e0-pages.txt` |
| SHA-256 | `36a95743b0e0854454da8960cecf1bbe78d30e8b5c2e769e021a51e3b50ab726` |

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- 已覆盖: title/abstract/introduction、CRDT overview、CvRDT/CmRDT、practice snapshot、query examples、CALM/monotonicity criterion、non-monotone query coordination boundary、query language and datastore agenda、optimization opportunities、weak consistency tradeoff、related work、conclusion and references.
- Metadata correction: PDF metadata and first page agree on title. File name suggests a VLDB-related local label, but the PDF itself identifies the paper as arXiv `2210.12605v1`; no DOI or formal venue is present in the local PDF. Queue topic `crdts` was normalized to the existing durable knowledge path `conflict-free-replicated-data-types`.
- Extraction gaps: figures and reference formatting are lossy, but the main text and section structure are complete enough for absorption.

## 一句话贡献

论文把 CRDT 的问题从“updates 能否无协调收敛”推进到“queries/observations 能否无协调且安全地读取”，并主张用 CALM theorem 的 monotonicity criterion 判断哪些 CRDT 查询可以本地执行，哪些非单调查询需要协调、预协调或显式接受 stale/weak consistency。

## 要解决的问题

传统 CRDT API 给开发者一个相对简单的 object-oriented replicated datatype: replicas 可以本地更新，然后通过 merge/eventual delivery 收敛。论文指出这个保证只覆盖 updates。只要应用开始观察 CRDT state，查询结果就可能不安全。

最典型例子是 two-phase set 的 `A - R` 查询。`add` 和 `remove` 各自都是 grow-only set，merge 也能收敛；但某个 replica 在还没收到 remote remove 时读取 `A - R`，可能读到一个后来必须消失的元素。换句话说，CRDT 的收敛保证不会自动变成任意 query 的一致读保证。

论文提出的研究问题是:

| 问题 | 为什么重要 | 论文给出的方向 |
| --- | --- | --- |
| 哪些 CRDT 查询可以在 local replica 上安全执行? | 开发者需要知道什么时候不需要 consensus/transactions。 | 用 CALM theorem 的 monotonicity 判断。 |
| 非单调查询怎么办? | set difference、checkout、absence/threshold-below 等查询不能靠最终收敛自动安全。 | 需要协调、预协调、读所有副本、majority/read-write quorum，或声明弱一致。 |
| CRDT 系统应如何从 library 走向 datastore? | 只暴露对象 API 会让 query safety 和 optimization 都落到应用层。 | 提供 query language、optimizer、storage manager、GC 和 propagation policies。 |

## CRDT 背景提取

论文把 CRDT 分成两条常用路线:

| 路线 | 论文中的抽象 | 查询风险 |
| --- | --- | --- |
| State-based CRDTs / CvRDTs | state domain 是 join semilattice；merge 是 associative、commutative、idempotent 的 join；updates 对 lattice order 单调。 | query function 没有被 CRDT 定义约束，可能对 partial state 给出不安全 observation。 |
| Operation-based CRDTs / CmRDTs | replicas gossip operation logs，按 causal delivery 应用；paper 认为其 log/happens-before partial order 可看成某种 state-based encoding。 | 即使 operation delivery 最终收敛，观察当前 log 的 query 仍需要判断是否对未来 operation 单调。 |

论文的关键界限是: CRDT 类型定义保证 merge/update 安全，不保证所有 read/query 安全。仅暴露 internal state 不等于给出一个可用的一致 query model。

## CALM 与单调查询模型

论文把 query safety 归约到 monotonicity。对于 CRDT 的 join semilattice `S = (D, join)`，如果 `i <= j` 时总有 `Q(i) => Q(j)`，则 query `Q` 对这个 CRDT state order 是单调的。直觉上，local replica 当前看到的是 future global state 的一个 under-approximation；如果一个查询结果一旦为真就不会被后续 state 扩展推翻，它就可以本地返回。

| Query pattern | 结果 | 原因 | 示例 |
| --- | --- | --- | --- |
| Grow-only threshold | safe/local | state 只增长，超过阈值后不会回到 false。 | gift-card purchase G-Set size `> 50`。 |
| 2P-set membership via `A - R` | unsafe/local | 未来 remove set 增长可能推翻当前 membership。 | shopping cart checkout 可能读到已被删除的商品。 |
| `|A| + |R| > 100` over 2P-set internals | safe/local | add/remove internal sets 都只增长，threshold 为真后不被推翻。 | 内部活动规模告警。 |
| Set difference / absence queries | non-monotone | 新信息可能撤销当前答案。 | “没有删除”“这个元素仍存在”。 |

论文引用 CALM theorem 的核心含义: 在分布式环境中，不需要协调即可一致收敛的 computation 正是 monotone computation。迁移到 CRDT query context 后，monotone queries 是那些只靠 local view 就能安全返回的 queries；non-monotone queries 需要某种 coordination 或明确降级成弱一致读。

## 非单调查询的协调边界

论文没有把所有非单调查询都排除，而是把它们放在一个协调谱系里:

| 策略 | 适合情况 | 代价/边界 |
| --- | --- | --- |
| Write-one read-all | 写入轻、读时可接受多副本同步 | 读延迟高，对副本可用性敏感。 |
| Write-majority read-majority | 需要 quorum 交叠 | 读写都要协调，牺牲部分 availability。 |
| Write-all read-one | 读路径快，写路径强同步 | 写延迟和可用性成本最高。 |
| Pre-coordinate before expected non-monotone query | 查询模式可预测，数据 store 能提前同步相关状态 | 需要 workload model 或 metrics；预测错误会浪费协调。 |
| Explicit stale/recent API | 应用愿意接受弱一致结果并自行补偿 | 需要 lineage、apologies 或 compensating actions。 |

论文强调，CRDT 仍然有价值: 即使某些 queries 需要协调，updates 之间仍可保持 commutative/coordination-free；系统只需要围绕 non-monotone observations 引入 ordering/coordination。

## CRDT Data Store 研究议程

论文主张把 CRDT 从 library/API 推向 data-management system:

| 子问题 | 论文建议 | 对 Knowledge 的影响 |
| --- | --- | --- |
| Query language | 用 SQL-like language、relational algebra、Datalog 或 lattice-aware DSL 表达 CRDT queries，并让语法/类型系统识别 monotonicity。 | 将 CRDTs 与 query processing/programming languages 建立候选连接，但当前 vault 还没有独立 query-processing knowledge node。 |
| Optimizer | 利用 monotone/non-monotone 分析，把 safe local stages 和需要 barrier/coordination 的 stages 分开。 | CRDT 查询安全不仅是理论判断，也会影响执行计划。 |
| Storage representation | data store 可以隐藏 logical CRDT 与 physical layout 的差异，选择 columnar/compressed/derived representations。 | 与 Canteen 的 metadata/GC 问题互补。 |
| Garbage collection | store 知道 replicas 和 query/update lifecycle 后，可安全回收不可达 state 或历史 metadata。 | 强化 CRDT node 里 metadata GC 的重要性。 |
| Propagation policy | 选择 full state、delta、batching、topology 和 gossip frequency。 | 让 CRDT data store 成为优化对象，而不是一组裸数据类型。 |
| Custom CRDT extension | 类似 Postgres extensions，开发者可通过 FFI 注册 CRDT logic 并证明/声明 monotonicity/convergence。 | 保留为未来 repo/system source 的 watch item。 |

## 与 Canteen 的互补关系

[[sha256-ac567f8d9ef6-canteen-partially-ordered-log-crdt-datastore|Canteen]] 关注 CRDT data store 的 operation log、causality metadata、COG compaction、non-commutative operations 和 equivocation tolerance。Keep CALM and CRDT On 关注 CRDT observations 的 query-safety 边界。二者共同把 CRDT 从“可收敛的数据类型”扩展为“需要 data-store/query/runtime 支持的 replicated data management problem”。

## Source-level Claims

| Claim | Evidence | Confidence |
| --- | --- | --- |
| CRDT guarantees cover updates/merge convergence, not arbitrary observations over current local state. | Abstract, §1, 2P-set example | high |
| Monotone queries over CRDT semilattice state are exactly the queries that can be answered locally without coordination under the CALM framing. | §3.2 | high |
| Non-monotone queries require coordination, pre-coordination, or explicit weak/stale semantics if applications need consistency. | §3.3, §4.4 | high |
| A CRDT data store should expose a query language and optimizer that separates monotone local execution from non-monotone coordination boundaries. | §4.1-§4.2 | medium-high |
| CRDT system performance work includes logical/physical separation, compression, garbage collection, delta propagation and workload-aware coordination. | §4.3-§4.4 | medium-high |

## Limitations and Caveats

- This is primarily a research agenda/position paper, not an implemented system evaluation.
- The paper relies on CALM/monotonicity as a conceptual criterion; it does not provide a full production SQL dialect, optimizer implementation or type checker.
- The paper's CRDT foundation discussion is useful but should not replace direct Shapiro/Preguiça/Delta-CRDT foundation sources.
- It does not create a BFT bridge. Its coordination boundary is about monotonicity and query safety, not adversarial equivocation.

## Absorption Routing

| 目标 | 动作 | 理由 |
| --- | --- | --- |
| [[conflict-free-replicated-data-types|Conflict-free replicated data types]] | update | 新增 CALM-based monotone query model 作为方法族/source extension。 |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | update | 数据管理方向新增 CRDT query/observation safety 问题。 |
| [[04_Knowledge/distributed-systems|Distributed systems]] | update | 分布式系统父域补充 coordination-free replication 的 safe observation 边界。 |
| [[04_Knowledge/distributed-systems/research-dynamics|Distributed systems Research Dynamics]] | update | 当前 vault 动态里新增 CRDT query model/data-store agenda。 |
| bridge | no-op | 暂不新建 bridge；缺少独立 query-processing/programming-languages 端点，先作为 CRDT source extension 和 future bridge candidate。 |

## Future Retrieval Hints

- 用户问“CRDT 查询什么时候安全?”应优先打开 [[conflict-free-replicated-data-types|CRDTs]] 的 CALM/monotone query model 小节，再打开本 source note。
- 用户问“为什么 CRDT 不等于所有读都一致?”应看 two-phase set / `A - R` example 和 non-monotone query boundary。
- 用户问“CRDT data store 可以怎么做?”应看本 note 的 data-store agenda，以及 Canteen 的 operation-log/GC 机制。

## 更新记录

| Date | Run ID | Change |
| --- | --- | --- |
| 2026-06-24 | nahida-knowledge-20260624-keep-calm-crdt-query-model | Deep-read PDF, corrected queue taxonomy from `crdts` to `conflict-free-replicated-data-types`, and absorbed as CRDT query-safety/data-store agenda evidence. |
