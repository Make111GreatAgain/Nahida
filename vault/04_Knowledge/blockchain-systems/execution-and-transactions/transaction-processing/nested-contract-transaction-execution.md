---
id: "nahida-knowledge-nested-contract-transaction-execution"
title: "Nested contract transaction execution"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "nested-contract-transaction-execution"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
topic_ids:
  - "nested-contract-transaction-execution"
  - "smart-contract-concurrency-control"
  - "deterministic-concurrency-control"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-transaction-processing"
  - "nahida-knowledge-smart-contract-execution"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
  - "nested-contract-transaction-execution"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing/nested-contract-transaction-execution"
secondary_ontology_paths:
  - "blockchain-systems/execution-and-transactions/smart-contract-execution"
  - "distributed-systems/transaction-processing"
relation_edges:
  - from: "nahida-knowledge-nested-contract-transaction-execution"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-transaction-processing"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/nested-contract-transaction-execution.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-nested-contract-transaction-execution"
    relation: "depends_on"
    to: "nahida-knowledge-smart-contract-execution"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/smart-contract-execution.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-nested-contract-transaction-execution"
    relation: "bridges_to"
    to: "nahida-bridge-smart-contract-execution-to-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/smart-contract-execution-to-transaction-processing.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-nested-contract-transaction-execution"
    relation: "bridges_to"
    to: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    evidence_refs:
      - "vault/05_Bridges/database-transaction-processing-to-blockchain-execution.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-nested-contract-transaction-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-smart-contract-execution-to-transaction-processing"
  - "nahida-bridge-database-transaction-processing-to-blockchain-execution"
source_note_refs:
  - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
representative_source_refs:
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
query_keys:
  - "nested contract transaction execution"
  - "nested smart contract transaction"
  - "deterministic nested contract transactions"
  - "subtransaction-level rollback"
  - "smart contract concurrency control"
  - "parallel smart contract execution nested calls"
  - "Loom nested contract transactions"
  - "hyper-dependency graph"
  - "fine-grained re-execution"
  - "two-phase deterministic rollback"
aliases:
  - "Nested smart-contract transaction execution"
  - "嵌套合约交易执行"
  - "嵌套智能合约交易执行"
domains:
  - "blockchain-systems"
topics:
  - "nested contract transactions"
  - "blockchain transaction processing"
  - "smart contract execution"
  - "deterministic concurrency control"
  - "partial rollback"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh_current_vault"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260623-loom-nested-contract-transactions"
source_refs:
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
confidence: "medium"
trust_tier: "primary"
---

# Nested contract transaction execution

## 定义与范围

- 定义: Nested contract transaction execution 关注区块链中一笔交易触发多层跨合约调用时，节点如何在确定性顺序、读写冲突、部分回滚、重执行和多核并发之间取得一致且高吞吐的执行结果。
- 核心对象: nested contract call tree, subtransaction, weak/strong intra-transaction dependency, inter-transaction conflict, deterministic serializability, rollback list, re-execution schedule, block-level snapshot。
- 不包含: 单个 Loom 系统名、某个 smart-contract VM/runtime、共识排序、mempool、gas/trap 语义、跨链调用协议或普通数据库 nested transaction 理论本身。
- Canonical terms: `nested contract transactions`, `subtransaction-level rollback`, `deterministic concurrent smart contract execution`, `smart contract concurrency control`.
- Retrieval role: 查询“嵌套合约调用如何并行执行/回滚/重调度”“Loom 解决什么问题”“parallel smart contract execution 如何处理 nested calls”时进入本节点，而不是直接进入 Loom source。
- Update scope: 新资料涉及 parallel EVM、Block-STM、SChain、EOR、nested transactions in smart contracts、subtransaction scheduling、call-tree conflict analysis 或 deterministic smart-contract concurrency control 时刷新。

## 背景

普通区块链交易处理常把一笔交易视为一个 flat transaction: 交易并行执行，冲突后整笔 abort/re-execute，最后按区块顺序提交。这个模型在简单转账或浅层合约调用中可用，但在复杂智能合约生态里会丢失大量结构信息。

嵌套合约交易的关键差异是: 一笔外层交易可能调用多个合约，某些子调用决定父调用是否能继续，另一些子调用可以独立成功或失败。于是执行层不只面对“交易 A 与交易 B 是否读写冲突”，还要判断“交易 A 的哪个子调用与交易 B 的哪个子调用冲突，冲突子调用是否会迫使父调用回滚，以及哪些子调用能被并行移动”。

当前 vault 的直接证据来自 [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]]。Loom 说明该问题足够从 generic [[transaction-processing|Blockchain transaction processing]] 中拆出: 它需要智能合约调用结构作为输入，同时仍受区块链确定性交易处理约束。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它覆盖 nested smart-contract calls、subtransaction dependency、partial rollback、deterministic rescheduling、parallel execution 和 database nested-transaction adaptation，未来可承接 Loom、EOR、Block-STM/parallel EVM、SChain/PEEP 类执行源。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Loom 是一个代表系统；HDG、SAT、GWG、two-phase rollback 是 Loom 的具体 route。节点保留问题边界和方法族，不把 Loom 名称上提。
- 需要引用的更基础 Knowledge: [[transaction-processing|Blockchain transaction processing]] 和 [[smart-contract-execution|Smart contract execution]]。
- 不应拆出的实例/来源: Loom、单次 TPC-C-like benchmark、具体 Fig. 4/5/6 示例暂不建知识节点。

## 解决的问题

本节点回答: 当一笔智能合约交易内部存在多层合约调用和子交易依赖时，区块链节点如何利用调用树结构提升并发，同时保证所有节点选择相同的回滚、重执行和提交结果。

典型子问题包括:

- 如何把合约调用树转化为可调度的 subtransactions。
- 如何区分 parent-critical 子调用和可独立执行/回滚的子调用。
- 如何在确定性 commit order 约束下做并发执行，而不是像普通数据库一样自由选择提交顺序。
- 如何避免高冲突 nested workloads 下整笔交易反复回滚。
- 如何让 re-execution 不因长强依赖链而阻塞其他可执行子调用。
- 如何在跨区块 pipeline 中追踪 snapshot provenance 和 read-write dependency。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[transaction-processing|Blockchain transaction processing]] | child_of | Loom indexes itself as transaction processing/concurrency control and optimizes deterministic block execution | active_seed |
| [[smart-contract-execution|Smart contract execution]] | depends_on / adjacent_problem | nested calls are smart-contract invocation structure, not ordinary key-value transactions | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| subtransaction-level rollback | method candidate | Loom shows partial rollback is the central performance lever, but one source is not enough for a full method node. | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | review |
| deterministic smart-contract concurrency control | method/problem candidate | This may become a broader route covering Loom, Block-STM and parallel EVM. | Loom only in current vault | review |
| parallel EVM execution | method family candidate | Likely related but not source-backed in current vault. | gap | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Flat transaction parallel execution | 把整笔交易作为原子单元并行执行，冲突后整笔 rollback/re-execute。 | 调用浅、冲突低或读写集合明确。 | 长 nested call chain 会放大 rollback 成本；无法利用 intra-transaction parallelism。 | Loom related work |
| Database nested-transaction adaptation | 借用 nested transaction 的 parent/child、partial rollback 和 parallel nesting 思想。 | 合约调用树能被识别并映射为子交易。 | 普通数据库可自由调度 commit order；区块链需要 deterministic serializability。 | [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] |
| Dependency-aware subtransaction rollback | 用 strong/weak dependency、HDG/SAT/GWG 捕获子交易冲突与回滚成本，选择部分 rollback 而不是整笔 rollback。 | 预执行能捕获调用结构、读写集和执行代价。 | 图构建和启发式选择有开销；高动态读写集仍需 retry。 | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] |
| Fine-grained deterministic re-execution | 在保留 serialization order 的前提下，把 non-conflicting subtransactions 提前填入 idle slots。 | rollback subtransactions 和依赖关系已知。 | 重调度策略必须 deterministic；mutable read/write sets 会触发额外 rollback。 | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] |
| Snapshot-based multi-phase parallelism | 用 provisional/finalized snapshots 让下一 block 的 pre-execution/rollback 与当前 block 的 re-execution overlap。 | permissioned execution pipeline 有 idle threads，且能检测跨 block read-write dependency。 | 复杂化 snapshot provenance；错误依赖必须 rollback/retry。 | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom: A Deterministic Execution Framework Towards Nested Contract Transactions]] | paper | 创建本问题节点；提出 snapshot-based pre-execution、strong/weak dependency、HDG/SAT/GWG two-phase rollback、fine-grained rescheduling 和 multi-phase parallelism。 | Permissioned blockchain prototype; TPC-C-like smart contracts; assumes deterministic ordering service; not VM-runtime or consensus paper. | p1-p14 |

## 当前综合

- Evidence window: `2026-06-23`。
- Freshness: `fresh_current_vault`; 只代表当前已读 Loom，不是外部最新综述。
- 综合: Loom 把 smart-contract execution 和 blockchain transaction processing 之间的交界具体化: 合约调用树不是 VM 内部细节，也不是单纯业务逻辑；它会改变交易处理的冲突粒度、回滚粒度和重执行调度空间。当前节点因此作为 active seed 存在，但仍保持 `foundation_thin` 风格: 细节来自 Loom，后续需要 parallel EVM / Block-STM / EOR / database nested transaction direct sources 验证方法谱系。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | 创建 nested-contract-transaction-execution 问题节点，并把 Loom 留作 source instance；补入 subtransaction-level rollback/reschedule route。 | 全节点 | yes | 后续吸收 EOR/Block-STM/parallel EVM 后复核 child split |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[smart-contract-execution-to-transaction-processing|Smart contract execution -> blockchain transaction processing]] | `blockchain-systems/execution-and-transactions/smart-contract-execution; blockchain-systems/execution-and-transactions/transaction-processing` | dependency, granularity_shift, conflict_modeling | Smart-contract call structure transfers to transaction-processing granularity; VM gas/trap correctness and consensus ordering remain separate. | active_seed |
| [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] | `distributed-systems/transaction-processing; blockchain-systems/execution-and-transactions/transaction-processing` | translation, implementation_reuse, trust_model_shift | Nested-transaction partial rollback transfers as an execution idea only after deterministic serializability and replica consistency constraints are added. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-nested-contract-transaction-execution | is_a | nahida-knowledge-blockchain-transaction-processing | Loom source note | high | active_seed |
| nahida-knowledge-nested-contract-transaction-execution | depends_on | nahida-knowledge-smart-contract-execution | Loom nested call model | high | active_seed |
| nahida-knowledge-nested-contract-transaction-execution | bridges_to | nahida-bridge-smart-contract-execution-to-transaction-processing | bridge note | high | active_seed |
| nahida-knowledge-nested-contract-transaction-execution | bridges_to | nahida-bridge-database-transaction-processing-to-blockchain-execution | bridge note | medium | active_seed |
| nahida-knowledge-nested-contract-transaction-execution | evidenced_by | vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md | Loom p1-p14 | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 缺少 EOR / Block-STM / parallel EVM / SChain 等对照 sources。 | Loom 只能建立 active seed；要拆更细方法族需要更多执行框架。 | continue paper intake or `nahida-research-search` | high | queued |
| 缺少直接 database nested transaction foundation source。 | Loom 引用 nested transaction lineage，但 vault 还没有 Moss/open nesting/parallel nesting 的 source note。 | `nahida-research-search` foundation_pack | medium | queued |
| 合约运行时 gas/trap 与 nested scheduling 的交互还薄。 | DTVM 和 Loom 分别覆盖 runtime determinism 与 nested execution，但尚未有 source 同时处理两者。 | continue paper intake | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-paper-intake-20260623-loom-nested-contract-transactions | Created nested-contract-transaction-execution as an active seed problem node and connected it to transaction processing, smart-contract execution and database transaction-processing bridge. | sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd | codex |
