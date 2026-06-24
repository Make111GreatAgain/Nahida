---
id: "nahida-knowledge-replicated-database-concurrency-control"
title: "Replicated database concurrency control"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "replicated-database-concurrency-control"
domain_id: "distributed-systems"
direction_id: "transaction-processing"
topic_ids:
  - "replicated-database-concurrency-control"
  - "primary-backup-replication"
  - "cloned-concurrency-control"
parent_knowledge_refs:
  - "nahida-knowledge-transaction-processing"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "transaction-processing"
  - "replicated-database-concurrency-control"
primary_ontology_path: "distributed-systems/transaction-processing/replicated-database-concurrency-control"
secondary_ontology_paths:
  - "distributed-systems/data-management-and-storage/storage-engines"
relation_edges:
  - from: "nahida-knowledge-replicated-database-concurrency-control"
    relation: "part_of"
    to: "nahida-knowledge-transaction-processing"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/transaction-processing.md"
      - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-replicated-database-concurrency-control"
    relation: "depends_on"
    to: "nahida-knowledge-storage-engines"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
      - "vault/05_Bridges/replicated-database-concurrency-control-to-storage-engines.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-replicated-database-concurrency-control"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-replicated-database-concurrency-control"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-replicated-database-concurrency-control-to-storage-engines"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md"
  - "vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md"
representative_source_refs:
  - "arxiv:2207.02746"
  - "doi:10.14778/3561261.3561268"
query_keys:
  - "replicated database concurrency control"
  - "primary-backup replication concurrency control"
  - "backup read-only transactions"
  - "cloned concurrency control"
  - "monotonic prefix consistency"
  - "bounded replication lag"
  - "C5"
  - "C5 MyRocks"
  - "C5 Cicada"
  - "Starry"
  - "multi-master replicated transaction commit"
  - "semi-leader commit protocol"
  - "storage-layer transaction commit"
aliases:
  - "Primary-backup concurrency control"
  - "Cloned concurrency control"
  - "备库并发控制"
domains:
  - "distributed-systems"
topics:
  - "replicated database concurrency control"
  - "primary-backup replication"
  - "bounded replication lag"
  - "backup read-only transactions"
  - "multi-master replicated transaction commit"
  - "semi-leader commit protocol"
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
  - "nahida-knowledge-20260623-c5-cloned-concurrency-control"
  - "nahida-knowledge-20260623-starry-multi-master-transaction-processing"
source_refs:
  - "arxiv:2207.02746"
  - "doi:10.14778/3561261.3561268"
confidence: "medium"
trust_tier: "primary"
---

# Replicated database concurrency control

## 定义与范围

- 定义: Replicated database concurrency control 关注复制数据库中，副本如何在接收/产生事务日志、应用写入、服务读请求、推进可见状态和达成 commit decision 之间保持一致性、新鲜度和可恢复性。
- 当前 vault 范围: C5 补入 primary-backup cloned concurrency control seed，重点是异步复制备库如何同时保持 monotonic prefix consistency 和 bounded replication lag；Starry 补入 multi-master storage-layer transaction commit seed，重点是无冲突事务 fast commit 与冲突事务 sequencer reordering 如何共同保证 serializability 与 replica agreement。
- 不包含: 跨多条独立区块链的 atomic commit、Byzantine 共识安全、开放网络治理或完整 storage-engine 设计。
- Retrieval role: 防止 C5 这类 primary-backup database replication source 被误归为 `distributed-transactions`；查询备库复制滞后、read-only backups、cloned concurrency control 时从这里进入。

## 背景

Primary-backup databases 常用异步复制: primary 承担写事务并输出 log，backups 应用 log，并可承担读-only transactions。这个结构把并发控制问题拆成两层: primary 的并发控制已经决定了 committed log order；backup 的 cloned concurrency control 必须在不重新定义事务语义的情况下，尽量并行应用 log writes，同时只向 reads 暴露 primary 曾经存在过的前缀状态。

C5 是当前 vault 的第一条直接 source。它说明，备库并发控制不能只问“是否一致”，还必须问“是否总能追上 primary”。Coarse-grained protocols 可以保持一致性，但如果它们在 backup 上施加比 primary 更多的串行化约束，就会在某些 workload 中产生 unbounded replication lag。

Starry 扩展了本节点的范围边界: 它不是 primary-backup backup-side cloned CC，而是 multi-master storage replicas 的 transaction commit protocol。它说明，在所有副本都可提议事务的数据库中，并发控制必须同时处理 timestamp order、read/write conflict、replica quorum、failure recovery 和 conflict reordering。也就是说，复制数据库并发控制不仅可能发生在“备库如何读”这一层，也可能发生在“多个副本如何共同决定事务提交顺序”这一层。

## 解决的问题

| 问题 | 说明 | C5 中的证据 |
| --- | --- | --- |
| Backup reads 应该看到什么状态? | read-only transactions 需要看到 primary history 的连续前缀，而不是部分事务或跨 row 拼接出的不可能状态。 | monotonic prefix consistency |
| Backup 如何不永久落后? | 复制协议需要 bounded replication lag，而不只是 eventually catch up under light load。 | Theorem 1 and evaluation |
| Backup 如何保留 primary 并行度? | 备库调度粒度不能粗于 primary 必要冲突，否则 parallel writes 会被无谓串行化。 | transaction/page granularity lower bound |
| Storage-engine API 如何影响实现? | snapshot、timestamp、row logging 和 commit interface 会决定 ideal C5 能否直接落地。 | C5-MyRocks vs C5-Cicada |
| Multi-master replicas 如何避免 leader bottleneck 与 leaderless abort? | 无冲突事务走 decentralized fast path，冲突事务由 sequencer 精确重排。 | Starry semi-leader commit |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | `part_of` | C5 source note | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| cloned concurrency control | method family | 备库复制 primary 并发控制效果的协议族；C5、KuaFu、Query Fresh 等可在这里比较 | C5 | review |
| monotonic prefix consistency | concept/problem | 备库读一致性的核心目标，可能也适用于其他 replicated storage/serving systems | C5 | review |
| bounded replication lag | objective/problem | 备库追赶能力的性能正确性目标，和 freshness/failover/data-loss risk 相关 | C5 | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Transaction-granularity cloned CC | 把整个事务作为 backup scheduling unit；同一事务内 writes 由一个执行单元处理。 | 实现简单、log 格式或系统接口限制较强 | 会把 primary 可并行的 row writes 串行化；C5 证明可能无界 lag | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] |
| Page-granularity cloned CC | 按 page 作为冲突单位，比 transaction 粒度细但仍粗于 row。 | page-based storage/recovery interface | 同 page 不同行更新会被无谓串行化 | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] |
| Row-granularity cloned CC | 每个 row 维护 primary-log-ordered FIFO，只对同一 row writes 施加必要顺序。 | primary log 能定位 rows，backup 可并行应用 safe writes | 仍需 snapshotter 确保全局 MPC；实现受 storage-engine API 限制 | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] |
| Prefix snapshot exposure | 用 current/next/future snapshots 把 per-row completion 转化为事务边界上的全局 prefix。 | 备库必须同时服务 read-only transactions | snapshot creation/merge 的代价由 storage-engine API 决定 | [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] |
| Semi-leader replicated commit | 任意副本可作为 proposer，non-conflict transactions 通过 super quorum fast commit；conflicting transactions 由 sequencer 运行 conflict graph reordering 并写回 decision。 | multi-master cloud database storage layer；`2F+1` crash-fault replicas；read/write sets 可用于 OCC-style check | 不是 Byzantine；高竞争下 sequencer/tail latency 成为限制；与 C5 的 backup read visibility 问题不同 | [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5: Cloned Concurrency Control That Always Keeps Up]] | paper | 建立 primary-backup cloned CC 的 consistency + bounded lag 问题框架，并给出 row-granularity C5 route | formal model 假设 prompt log delivery；MyRocks/Cicada 实现各有限制 | §2-§7 |
| [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry: Multi-master Transaction Processing on Semi-leader Architecture]] | paper | 补入 multi-master replicated storage-layer commit 路线：semi-leader fast path + sequencer conflict reordering + failure recovery | crash-fault model only；与 primary-backup cloned CC 是相邻而非同一问题 | §2-§5 |

## 当前综合

- Evidence window: `2026-06-23`
- Freshness: `fresh_current_vault`; 只代表当前已读 C5，不是外部最新综述。
- 综合: C5 让 vault 中的 `transaction-processing` 不再只由 blockchain adaptation sources 支撑，而是补入一个真实数据库复制问题: backup-side concurrency control。核心判断是，复制数据库的备库协议必须同时满足一致性和追赶能力；transaction/page granularity 虽然可保证一致性，却可能因施加额外串行约束导致 unbounded lag。C5 的 row-granularity route 把必要冲突降到同一 row 的 log order，再通过 snapshotter 暴露事务前缀。Starry 进一步补入相邻的 multi-master replicated commit 问题: 当所有 storage replicas 都可提议事务时，系统需要把 quorum evidence、timestamp order、OCC conflict detection、sequencer recovery 和 conflict graph reordering 合在一起，才能同时避免 leader bottleneck 和 leaderless conflict abort。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up|C5]] | 新增 replicated database concurrency-control problem node；纠正队列中 distributed-transactions 误分类。 | 定义、方法族、代表 Sources、Bridge Links | yes | 后续补 KuaFu、Query Fresh、database replication/recovery/parallel replication foundations |
| [[doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing|Starry]] | 增加 multi-master replicated storage-layer commit 证据；明确它和 C5 同属复制数据库并发控制邻域，但问题不同。 | 定义、背景、解决的问题、方法族、代表 Sources、关系图谱 | no | 后续补 TAPIR、MDCC、Janus、Rococo、Paxos Commit 等对照源 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[05_Bridges/replicated-database-concurrency-control-to-storage-engines|Replicated database concurrency control -> storage engines]] | `distributed-systems/transaction-processing/replicated-database-concurrency-control` -> `distributed-systems/data-management-and-storage/storage-engines` | dependency, implementation_boundary | snapshot/log/timestamp API constrains whether ideal cloned CC can be implemented directly; storage engine mechanisms do not by themselves provide MPC or bounded lag | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-replicated-database-concurrency-control | part_of | nahida-knowledge-transaction-processing | C5 source note | high | active_seed |
| nahida-knowledge-replicated-database-concurrency-control | depends_on | nahida-knowledge-storage-engines | C5 MyRocks/Cicada implementation contrast | medium | active_seed |
| nahida-knowledge-replicated-database-concurrency-control | evidenced_by | vault/03_Sources/papers/arxiv-2207-02746-c5-cloned-concurrency-control-that-always-keeps-up.md | C5 source note | high | active_seed |
| nahida-knowledge-replicated-database-concurrency-control | evidenced_by | vault/03_Sources/papers/doi-10-14778-3561261-3561268-starry-multi-master-transaction-processing.md | Starry source note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| KuaFu / Query Fresh / MySQL parallel replication 直接 sources 缺失 | C5 使用它们作为对照，当前 vault 只能记录 C5 的论文描述 | `nahida-research-search` or future paper intake | medium | queued |
| 数据库 recovery / replication textbook source 缺失 | 需要把 cloned CC 放入更完整 primary-backup replication 谱系 | `nahida-research-search` foundation_pack | medium | queued |
| Optimistic concurrency control 下的 cloned CC generalization | C5 将其列为 future work；后续 source 可能改变方法树 | future paper intake | low | watch |
| multi-master replicated commit protocol 对照源缺失 | Starry 拓宽了本节点，但还需要 TAPIR、MDCC、Janus、Rococo 等对照源来判断是否应拆出独立方法节点 | `nahida-research-search` foundation_pack 或继续 paper intake | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-c5-cloned-concurrency-control | Created problem node from C5 and placed it under transaction processing, with storage-engine bridge. | arxiv:2207.02746 | codex |
| 2026-06-23 | nahida-knowledge-20260623-starry-multi-master-transaction-processing | Added Starry as adjacent evidence for multi-master replicated storage-layer transaction commit and semi-leader conflict reordering. | doi:10.14778/3561261.3561268 | codex |
