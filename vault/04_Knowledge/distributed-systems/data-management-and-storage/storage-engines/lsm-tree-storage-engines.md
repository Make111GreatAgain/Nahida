---
id: "nahida-knowledge-lsm-tree-storage-engines"
title: "LSM-tree Storage Engines"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "lsm-tree-storage-engines"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "storage-engines"
  - "lsm-tree-storage-engines"
parent_knowledge_refs:
  - "nahida-knowledge-storage-engines"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "storage-engines"
  - "lsm-tree-storage-engines"
primary_ontology_path: "distributed-systems/data-management-and-storage/storage-engines/lsm-tree-storage-engines"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-lsm-tree-storage-engines"
    relation: "part_of"
    to: "nahida-knowledge-storage-engines"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md"
      - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-lsm-tree-storage-engines"
    relation: "depends_on"
    to: "nahida-knowledge-storage-engines"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-lsm-tree-storage-engines"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-lsm-tree-storage-engines"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
    confidence: "high"
    status: "active"
  - from: "nahida-knowledge-lsm-tree-storage-engines"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "vault/05_Bridges/storage-engines-to-blockchain-state-storage.md"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md"
  - "vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md"
  - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
representative_source_refs:
  - "doi:10.1007/s002360050048"
  - "arxiv:1812.07527v3"
  - "arxiv:2306.10739v1"
query_keys:
  - "LSM-tree"
  - "log-structured merge tree"
  - "rolling merge"
  - "C0 component"
  - "C1 component"
  - "deferred index maintenance"
  - "history table index"
  - "LSM storage engine"
  - "leveling vs tiering"
  - "write amplification"
  - "read amplification"
  - "space amplification"
  - "compaction"
  - "checkpointed async merge"
  - "blockchain LSM storage"
aliases:
  - "Log-Structured Merge-tree"
  - "LSM based storage"
  - "LSM storage engines"
domains:
  - "distributed-systems"
topics:
  - "LSM-tree"
  - "storage engines"
  - "compaction"
  - "rolling merge"
  - "deferred index maintenance"
  - "RUM tradeoff"
  - "checkpointed merge"
  - "blockchain state storage"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "1996"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260620-item-0033"
  - "nahida-knowledge-20260622-cole-blockchain-storage"
  - "nahida-paper-intake-20260623-lsm-tree"
source_refs:
  - "doi:10.1007/s002360050048"
  - "sha256:8fe1d3206fe8eb151e9d8c54e0772a46786e2ec40e4c2b7782995067d6b938c6"
  - "arxiv:1812.07527v3"
  - "arxiv:2306.10739v1"
confidence: "high"
trust_tier: "primary"
---

# LSM-tree Storage Engines

## 定义与范围

- 定义: LSM-tree storage engine 是一种写优化存储引擎方法族。它把写入先缓存在内存组件中，再 flush 成不可变磁盘组件，并通过后台 merge/compaction 在多个有序组件之间整理数据。它的核心收益是把随机更新转化为顺序写；核心代价是 read amplification、space amplification、write amplification 和后台维护的延迟方差。
- 不包含: 某个具体系统如 LevelDB/RocksDB/HBase/Cassandra/AsterixDB 的完整架构；这些是代表实例。也不把 WiscKey、Monkey、Dostoevsky、PebblesDB 等单篇论文系统名直接提升为基础概念。
- Canonical terms: `LSM-tree`, `Log-Structured Merge-tree`, `SSTable`, `compaction`, `leveling`, `tiering`
- Standalone completeness check: 本节点本地解释 LSM-tree 的基本结构、成本模型、方法族、代表系统和 open problems；source note 保存每个 survey 细节。
- Retrieval role: 回答“LSM-tree 是什么/怎么权衡/有哪些路线/代表系统是什么”时，先读此节点即可定位少量 source。
- Update scope: 新的 LSM paper、RocksDB/LevelDB source、compaction policy、key-value separation、secondary indexing、auto-tuning 或硬件适配材料应以 source extension 更新本节点。

## 背景

source_backed_background: 原始 [[doi-10-1007-s002360050048-log-structured-merge-tree|LSM-tree paper]] 从高性能事务系统的 history table / recovery log 索引需求出发，指出随机 key 的 B-tree secondary index 会把每次 history insert 变成昂贵的随机 leaf read/write。它提出的关键结构是内存常驻 `C0` 组件、一个或多个磁盘组件 `C1..CK`、以及在相邻组件间循环推进的 rolling merge。`LSM-based Storage Techniques: A Survey` 则把这个原始结构放进现代 NoSQL / storage-engine 设计空间，扩展出 leveling、tiering、Bloom filters、partitioning、hardware adaptation 和 auto-tuning 等路线。COLE 作为 source extension 展示了 LSM-like runs/merge 在区块链状态存储中的专门化: 后台 merge 不能自由改变结构，必须经过 checkpointed root-hash update。

## 解决的问题

- 写密集 workload 中，如何避免每次更新都触发随机磁盘写。
- 如何在多个不可变组件中支持点查、范围查、更新和删除。
- 如何通过 merge policy 和过滤器在 write/read/space amplification 之间调参。
- 如何把后台 compaction 对前台请求的影响控制在可接受范围内。
- 如何让存储引擎适配不同 workload、硬件和二级索引需求。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | `part_of` | LSM survey §1-§2 | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Leveling and tiering policies | method section | 当前可在本节点解释，不需单独节点；后续多 source 再拆 | LSM survey §2.2 | section |
| LSM auto-tuning | candidate method child | Monkey/Dostoevsky 等路线可能形成多 source 子问题 | LSM survey §3.6 | review |
| LSM secondary indexing | candidate application/problem child | §3.7 材料丰富，但当前一篇 survey 不够稳 | LSM survey §3.7 | review |
| Key-value separation | candidate method child | WiscKey/HashKV/Kreon 形成可复用路线，但需原论文/source | LSM survey §3.4 | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Original rolling merge LSM-tree | 新写入先进入内存 `C0`，再通过 rolling merge 批量进入 `C1..CK`；磁盘组件使用 multi-page block I/O | 高插入率、随机 key、history/log index 等写多查少负载 | immediate find 可能要查多个组件；并发/恢复需要 checkpoint、cursor 和节点锁设计 | [[doi-10-1007-s002360050048-log-structured-merge-tree|Original LSM-tree paper]] §2-§4 |
| Leveling | 每层通常只有一个主要组件，下一层约为上一层 `T` 倍；merge 后保持层级紧凑 | 读和空间更敏感的 workload | write amplification 较高，merge 成本更重 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §2.2 |
| Tiering | 每层允许多个组件，满后批量 merge 到下一层 | 写吞吐更敏感的 workload | read amplification 与 space amplification 更高，range query 更受影响 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §2.2 |
| Partitioned compaction | 将磁盘组件拆成 SSTables/ranges，限制单次 merge 处理范围 | 大规模数据、顺序或 skewed key workload | 分区策略和 range grouping 变复杂 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §2.3 |
| Bloom-filter-assisted lookup | 用 Bloom filters 排除不含 key 的组件，降低点查 I/O | point lookup workload | 无法同样解决 range query；需要内存并有 false positives | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §2.3 |
| Write-amplification reduction | tiering variants、merge skipping、hot/cold separation、virtual merges | 写密集系统 | 多数会转移成本到读、空间、范围查或复杂度 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §3.2 |
| Merge scheduling/operation optimization | stitching、pipelining、remote merge、cache-aware merge、write-stall scheduling | compaction 成为瓶颈时 | 可能增加碎片、系统复杂度或只改善部分延迟指标 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §3.3 |
| Hardware-aware LSM | 大内存、多核、SSD/NVM/native flash 优化 | 特定硬件/部署环境 | 可移植性和工程复杂度高，可能引入 GC 或 range query 退化 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §3.4 |
| Auto-tuning | 根据 workload、Bloom memory、merge policy 和 storage placement 自动选择参数 | workload 变化或云存储差异明显 | 依赖模型和观测质量；需要强 tuned baseline | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §3.6 |
| Secondary indexing on LSM | 维护二级索引、空间/倒排索引、component filters 或分布式索引 | 数据库系统需要多维查询 | cleanup、validation、index-only query 和分布式通信成本复杂 | [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM survey]] §3.7 |
| Checkpointed merge for authenticated state | 将 LSM-like runs 的后台 merge 放入 start/commit checkpoint，并同步更新 root_hash_list | 区块链状态存储需要降低 write tail latency 且所有节点保持同一 state digest | 普通 async merge 不可直接迁移；fork/rewind 仍未解决 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] §5 |

## 成本模型与权衡

原始论文给出 LSM 相对 B-tree 的 root cost intuition: B-tree 插入在随机 key 下需要走到 leaf 并写回随机页；LSM 插入先落到内存 `C0`，随后用 multi-page block I/O 和 batch merge 摊销到磁盘组件。其 insert cost ratio 可以理解为两个因子的乘积: multi-page block I/O 相对 random page I/O 的成本优势 `COSTπ/COSTP`，以及每次 merge 合入多个 entries 的批量优势 `1/M`。多组件 LSM 的意义是让相邻组件按近似几何级数增长，在 `C0` 内存成本、磁盘臂成本和 immediate find 成本之间取平衡。

| 维度 | Leveling | Tiering | 解释 |
| --- | --- | --- | --- |
| Write amplification | `O(T·L/B)` | `O(L/B)` | Leveling 反复把数据推入更大层，写成本高；tiering 批量 merge 写成本低。 |
| Point lookup without Bloom | `O(L)` | `O(T·L)` | Tiering 每层多个组件，需要查更多 run。 |
| Point lookup with Bloom | 可大幅降低无效查找 | 可缓解但组件更多 | Bloom filters 对 zero-result point lookup 特别重要。 |
| Range query | 较好 | 较差 | Bloom filters 对范围查帮助有限，tiering 需要合并更多组件。 |
| Space amplification | `O((T+1)/T)` | `O(T)` | Tiering 延迟清理旧版本，空间放大更高。 |

当前综合判断: LSM-tree 的工程设计不能只优化写吞吐。任何降低写放大的方法都应同时检查 point lookup、range query、space utilization、merge interference、tail latency 和实现复杂度。

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-s002360050048-log-structured-merge-tree|The Log-Structured Merge-Tree (LSM-Tree)]] | paper | 提出 `C0/C1..CK` 组件、rolling merge、deferred index maintenance、insert cost model、concurrency/recovery sketch | 成本数值基于 1990s disk/memory model；现代 SSTable/compaction 系统需另读工程 sources | Abstract, §1-§6 |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | paper survey | 提供 LSM-tree 基础机制、成本模型、研究 taxonomy、代表系统和未来方向 | 2019 survey；不是最新工业实践或所有原论文的一手评估 | §2-§5 |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE: A Column-based Learned Storage for Blockchain Systems]] | paper | 展示 LSM-like runs、Bloom filters 和 async merge 如何适配 authenticated blockchain state storage | 主路径不是通用 LSM；checkpoint 约束来自区块链 state root determinism | §3-§5 |

## 代表系统与实例

| 系统/实例 | 本节点中的地位 | 关键点 | 是否建独立节点 |
| --- | --- | --- | --- |
| LevelDB | representative instance | partitioned leveling, embedded key-value store | no |
| RocksDB | representative instance | LevelDB fork; L0 tiering、dynamic level sizes、compaction filters、rate limiting、merge operator | no |
| HBase | representative distributed storage system | Bigtable-like regions, tiering/date-tiered policies, coprocessor secondary indexes | no |
| Cassandra | representative distributed storage system | decentralized store; tiering/partitioned leveling/date-tiered; local secondary indexes | no |
| AsterixDB | representative database system | primary/secondary LSM indexes, correlated merge policy, record-level transactions | no |
| WiscKey / HashKV / Kreon | route examples | key-value separation / value log routes | queued for source-backed split |
| Monkey / Dostoevsky | route examples | auto-tuning and hybrid merge policy | queued for source-backed split |

## 当前综合

- Evidence window: `1996` to `2026-06-23`
- Freshness: `fresh` for source-backed hierarchy and foundation; not a latest-progress claim.
- Valid until: `2026-07-23`
- 综合: LSM-tree 是 storage-engine 方法族而不是一个单一系统名。原始论文给出这个方法族的核心不变量: authoritative memory component、deferred final placement、rolling merge、multi-page block I/O、checkpointed recovery。2019 survey 把这些不变量扩展成现代 `leveling/tiering/hybrid`、Bloom filters、partitioning、hardware adaptation 和 auto-tuning 设计空间。COLE 再增加一个专门化边界: 当 LSM-like merge 进入 blockchain state storage，merge scheduling 还会影响 state root determinism，因此需要 checkpointed async merge。当前最重要的 retrieval axis 是 RUM trade-off: read amplification、write/update amplification、space/memory cost 不能同时最优。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-s002360050048-log-structured-merge-tree|The Log-Structured Merge-Tree (LSM-Tree)]] | 补入原始 `C0/C1..CK` rolling merge、deferred index maintenance、B-tree cost comparison、concurrency/recovery sketch；将“原始 LSM paper 未吸收”缺口关闭 | 背景、方法族、成本模型、代表 Sources、当前综合、缺口 | no | 后续补 RocksDB/LevelDB 和 B-tree/recovery foundations |
| [[arxiv-1812-07527v3-lsm-based-storage-techniques-survey|LSM-based Storage Techniques: A Survey]] | 首次建立 LSM-tree storage engine 节点，补入基础定义、成本模型、taxonomy、代表系统和 future directions | 全文 | yes | 后续吸收 Monkey、Dostoevsky、WiscKey、RocksDB source |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] | 增加 LSM-like runs/merge 在区块链 authenticated state storage 中的 source extension | 方法族、代表 Sources、当前综合、Bridge Links | no | 保持 COLE 细节在 blockchain-state-storage 和 bridge |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[05_Bridges/storage-engines-to-blockchain-state-storage|Storage engines -> blockchain state storage]] | `distributed-systems/data-management-and-storage/storage-engines` -> `blockchain-systems/data-management-and-storage/blockchain-state-storage` | method_translation | LSM-like runs/merge transfer as write-path/storage-layout patterns; blockchain state-root determinism and proof completeness require extra machinery | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-lsm-tree-storage-engines | part_of | nahida-knowledge-storage-engines | vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md; vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | high | active_seed |
| nahida-knowledge-lsm-tree-storage-engines | depends_on | nahida-knowledge-storage-engines | vault/04_Knowledge/distributed-systems/data-management-and-storage/storage-engines.md | medium | active_seed |
| nahida-knowledge-lsm-tree-storage-engines | evidenced_by | vault/03_Sources/papers/doi-10-1007-s002360050048-log-structured-merge-tree.md | original LSM-tree source note | high | active |
| nahida-knowledge-lsm-tree-storage-engines | evidenced_by | vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | vault/03_Sources/papers/arxiv-1812-07527v3-lsm-based-storage-techniques-survey.md | high | active_seed |
| nahida-knowledge-lsm-tree-storage-engines | evidenced_by | vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md | COLE source note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| RocksDB/LevelDB 工程 source 缺失 | 工业实践不能只靠 survey 描述 | `nahida-github-repo-analyze` or web/source research | medium | queued |
| Monkey/Dostoevsky/WiscKey 等路线未读原论文 | 不宜仅凭 survey 建独立节点 | future paper intake | medium | queued |
| 2019 后 LSM 研究/工业演进未更新 | 用户若问最新趋势会 stale | `nahida-daily-fetch` / `nahida-research-search` | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-paper-intake-20260620-item-0033 | Created LSM-tree storage engine method-family node from deep-read survey. | arxiv:1812.07527v3 | codex |
| 2026-06-22 | nahida-knowledge-20260622-cole-blockchain-storage | Added checkpointed LSM-like merge for authenticated blockchain state storage as a source extension. | arxiv:2306.10739v1 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-lsm-tree | Absorbed the original LSM-tree paper, corrected PDF metadata year to 1996, and closed the original-paper foundation gap. | doi:10.1007/s002360050048 | codex |
