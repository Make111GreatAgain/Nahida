---
id: "sha256-0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
title: "In Search of an Understandable Consensus Algorithm"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1-p3 abstract, replicated state machines, Paxos critique, understandability design goals"
  - "p3-p10 Raft basics, leader election, log replication, safety argument, timing and availability"
  - "p10-p13 cluster membership changes, log compaction, client interaction"
  - "p13-p16 implementation, user study, correctness, performance, related work"
  - "p16-p18 conclusion and references"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "USENIX ATC 2014 extended version"
year: "2014"
pdf_pages: 18
pdf_sha256: "0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
local_pdf: "~/Desktop/paper/raft.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/in-search-of-an-understandable-consensus-algorithm-0f53a6508592-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "crash-fault-tolerance"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "crash-fault-tolerance"
primary_ontology_path: "distributed-systems/consensus/crash-fault-tolerance/sha256-0f53a6508592"
secondary_ontology_paths:
  - "distributed-systems/replication/state-machine-replication/sha256-0f53a6508592"
path_update_status: "propagated"
domains:
  - "distributed-systems"
topics:
  - "crash-fault-tolerance"
  - "raft"
  - "state-machine-replication"
aliases:
  - "Raft"
  - "Raft consensus algorithm"
tags:
  - "nahida/source"
  - "paper"
  - "distributed-systems"
  - "consensus"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "consensus"
  problem:
    - "crash-fault tolerant consensus"
    - "replicated log"
    - "state machine replication"
  method_family:
    - "leader-based consensus"
    - "randomized leader election"
    - "replicated log"
    - "joint consensus reconfiguration"
  system_layer:
    - "replication protocol"
    - "coordination service foundation"
  evaluation_context:
    - "understandability user study"
    - "TLA+ safety proof"
    - "leader election downtime"
  application:
    - "replicated state machines"
    - "configuration services"
    - "fault-tolerant storage systems"
  bridge:
    - "crash-fault consensus -> replicated state machines"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-raft-consensus"
source_refs:
  - "sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
  - "pdf:~/Desktop/paper/raft.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "distributed-systems -> consensus"
secondary_directions:
  - "distributed-systems -> replication"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title"
  - "abstract"
  - "full PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0006"
queue_status: "absorbed"
---

# In Search of an Understandable Consensus Algorithm

## 论文身份

- 标题: In Search of an Understandable Consensus Algorithm
- 版本: Extended Version
- 作者: Diego Ongaro, John Ousterhout
- 机构: Stanford University
- 会议/期刊: USENIX ATC 2014 extended version
- 年份: 2014
- DOI: unknown
- arXiv: unknown
- 本地 PDF: `~/Desktop/paper/raft.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/in-search-of-an-understandable-consensus-algorithm-0f53a6508592-pages.txt`
- 代码/数据: 论文引用 LogCabin source code 和 Raft website，但本次未外部验证

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 18
- 已覆盖章节/页码: p1-p18 full text
- 已检查附录: 本 PDF 无附录
- 未覆盖章节/页码: 无
- Extraction gaps: 图表文字和参考文献有少量换行/大小写噪声；算法规则、性质和评估数据可读
- 精读说明: 该 extended version 覆盖算法机制、reconfiguration、snapshotting、client interaction、TLA+ safety proof 状态和 user study；适合 durable absorption。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1 | Abstract/Introduction | Raft 与 multi-Paxos 等价目标、强调 understandability；三项新特征 | 贡献定位 | strong leader, randomized election, joint consensus |
| p1-p2 | Replicated state machines | replicated log、deterministic state machine、CFT 系统属性 | 问题模型 | non-Byzantine failures |
| p2-p3 | What's wrong with Paxos | Paxos 难理解、single-decree decomposition 不适合实践 | 背景/动机 | 与 Paxos 对比 |
| p3 | Designing for understandability | decomposition 和 state-space reduction | 设计原则 | 分解 leader election/log replication/safety |
| p3-p5 | Raft overview/basics | states、terms、RequestVote/AppendEntries、核心性质 | 协议框架 | Figure 2/3 |
| p5-p6 | Leader election | randomized election timeout, majority vote, split vote handling | 机制 | Election Safety |
| p6-p8 | Log replication | leader append, commit, Log Matching Property, nextIndex repair | 机制 | leader append-only |
| p8-p10 | Safety | election restriction, committing current-term entries, proof sketch | 正确性 | Leader Completeness -> State Machine Safety |
| p10 | Timing and availability | safety 不依赖 timing；availability 依赖 `broadcastTime << electionTimeout << MTBF` | 边界 | timing affects progress |
| p10-p11 | Cluster membership changes | joint consensus, overlapping majorities, non-voting catch-up | reconfiguration | avoids split majorities |
| p11-p13 | Log compaction/client interaction | snapshots, InstallSnapshot, linearizable reads/writes | 实践机制 | duplicate suppression, no-op entry |
| p13-p15 | Evaluation | 约 2000 lines C++, user study, TLA+ spec/proof, election performance | 证据 | 43 participants, 150-300ms recommendation |
| p15-p16 | Related work | Paxos, VR, ZooKeeper, EPaxos, membership changes | 对比 | strong leadership tradeoff |
| p16 | Conclusion | understandability as primary design goal | 结论 | implementation intuition |

## 核心精读笔记

### 背景、动机与问题边界

Raft 的目标是管理 replicated log，使一组 deterministic state machines 以同样顺序执行同样命令，从而在非拜占庭故障、网络延迟、分区、丢包、重复和重排下保持 safety。论文明确是 crash-fault/non-Byzantine consensus，不处理任意恶意节点。

作者认为 Paxos 虽正确且高效，但 single-decree Paxos 的基础分解让 multi-Paxos 和实际实现难以理解、难以扩展。Raft 的目标不是提出更强的 fault model，而是在等价于 multi-Paxos 的目标下，把协议结构改造成更容易学习、实现和推理的形式。证据锚点: p1-p3。

### 模型、假设与定义

Raft cluster 通常由奇数个 servers 组成，五节点可容忍两个 crash failures。每个 server 处于 follower、candidate、leader 三种状态之一。时间被分成单调递增的 terms，每个 term 至多一个 leader。RPC 只有核心两类: `RequestVote` 用于选举，`AppendEntries` 用于日志复制和 heartbeat；snapshotting 引入 `InstallSnapshot`。

系统 safety 不依赖时间；timing 只影响 availability。Raft 可用性需要 `broadcastTime << electionTimeout << MTBF`，使 leader 能发送 heartbeat，election timeout 又足够小以快速恢复。证据锚点: p4-p5, p10。

### 方法、协议或系统机制

Raft 的核心设计是 strong leader。所有客户端写请求由 leader 接收，leader append 到本地 log，再通过 `AppendEntries` 并行复制到 followers。日志条目包含 command、term 和 index；一旦当前 leader 创建的 entry 被多数节点存储，就可认为该 entry committed，并间接提交之前的 entries。

Leader election 使用 randomized election timeout 来降低 split vote 概率。Follower 在 election timeout 内没有收到有效 RPC 就转为 candidate，递增 term、投自己票，并向其他节点发 `RequestVote`。Candidate 获得多数票即成为 leader；若收到更高或相同 term 的合法 leader `AppendEntries`，则回到 follower。

Log replication 通过 `prevLogIndex` 和 `prevLogTerm` 做一致性检查。如果 follower 找不到匹配的前驱 entry，就拒绝；leader 递减该 follower 的 `nextIndex` 并重试，直到找到共同前缀，再删除 follower 冲突后缀并追加 leader entries。该机制维持 Log Matching Property，并让日志以 leader 为准收敛。证据锚点: p5-p8。

### 理论、证明或正确性论证

Raft 的核心 safety properties 包括 Election Safety、Leader Append-Only、Log Matching、Leader Completeness、State Machine Safety。最关键的补丁是 election restriction: voter 只有在 candidate log 至少和自己一样 up-to-date 时才投票。Up-to-date 先比较 last log term，再比较 log length。

Commit rule 还有一个 subtle point: leader 不能仅因为“旧 term entry 被复制到多数”就把旧 term entry 判定为 committed；只能对当前 term 的 entry 按多数提交。一旦当前 term entry committed，之前 entries 通过 Log Matching Property 间接 committed。这个保守规则避免 Figure 8 中旧 leader entry 已在多数但仍可能被未来 leader 覆盖的问题。

Safety proof sketch 通过多数交集论证 Leader Completeness: 如果 term T 的 leader committed 一个当前 term entry，而未来最小 term U 的 leader 缺失该 entry，则 term T 复制多数与 term U 投票多数必有交集 voter。该 voter 在投票时仍持有 entry，且只会投给至少一样 up-to-date 的 candidate，于是推出 leader U 必须也含有该 committed entry，矛盾。Leader Completeness 再推出 State Machine Safety。证据锚点: p8-p10。

### 实践机制与评估

Reconfiguration 用 joint consensus，过渡配置 `Cold,new` 要求 old 和 new configurations 分别多数同意。这样即使 servers 在不同时间切换配置，也不会出现 old/new 各自形成独立多数并选出两个 leader 的窗口。新增节点先作为 non-voting members catch up；被移除节点可能用更高 term 干扰集群，因此当前 leader 存在时 servers 会忽略最小 election timeout 内收到的 RequestVote。

Log compaction 使用 snapshotting。各 server 独立为 committed prefix 生成 snapshot，保存 last included index/term 和配置；leader 在 follower 落后到缺失日志时用 `InstallSnapshot` 发送 snapshot。Client interaction 通过 client serial numbers 防止 retry 导致 command 重复执行；read-only requests 需要 leader 先知道当前 committed entries，并在响应前与多数 heartbeat 确认自己未被取代，以维持 linearizability。

评估方面，论文报告 Raft implementation 约 2000 行 C++；understandability user study 中 43 名学生的 Raft quiz 平均 25.7 分、Paxos quiz 平均 20.8 分，33/43 个点在 Raft 更高一侧；paired t-test 给出 95% confidence 下 Raft score mean 至少高 2.5 分。Performance 部分显示少量 randomized timeout 足以避免 split votes；推荐 conservative election timeout 150-300ms。证据锚点: p10-p15。

### 作者结论与我的判断

Raft 是 crash-fault consensus/SMR 的 foundation source，尤其适合作为 Nahida 中 `distributed-systems/consensus/crash-fault-tolerance` 的代表材料。它的价值不仅是算法本身，还包括“understandability as design goal”的方法论: decomposition、strong leadership、state-space reduction。需要注意，它不处理 Byzantine faults；与 PBFT 属于不同 fault model。后续还需要 Paxos、Viewstamped Replication、FLP、partial synchrony 等来源补齐 consensus 方向。

## 层级候选分类

- L1 Domain candidate: `distributed-systems`
- L2 Direction candidate: `consensus`
- L3 Topic/content cluster candidates: `crash-fault-tolerance`, `raft`
- Ontology path: `distributed-systems/consensus/crash-fault-tolerance/sha256-0f53a6508592`
- 备选归属: `distributed-systems/replication/state-machine-replication`
- 父级领域: distributed systems
- 学术子领域: consensus algorithms, replicated state machines
- 任务/问题: crash-fault tolerant replicated log and state-machine replication
- 方法族: leader-based consensus, randomized leader election, log replication, joint consensus
- 模型/协议/算法族: Raft
- 评测场景: understandability study, TLA+ safety proof, leader election downtime
- Benchmark/应用: RAMCloud configuration, LogCabin, coordination services
- 别名: Raft consensus algorithm
- 相邻方向: Paxos, Viewstamped Replication, ZooKeeper/Zab, PBFT
- 置信度: high
- 分类理由: title/abstract/sections all identify Raft as consensus algorithm for replicated log under crash faults
- 分类状态: accepted
- 分类证据: title, abstract, full PDF deep read

## 一句话贡献

本文提出 Raft，一个以 understandability 为首要设计目标的 leader-based crash-fault consensus algorithm，通过 leader election、log replication、安全限制和 joint consensus 管理 replicated log，并用用户研究、TLA+ 规格/证明和实现评估支持其实践可用性。

## 问题设定

分布式服务需要多个 replicas 在 crash failures 和网络异常下保持一致状态。共识算法需要保证 non-faulty replicas 以同一顺序执行同一命令，同时在多数节点可通信时保持可用。Paxos 是主流基础，但难以理解和实现；Raft 试图给出更适合教学和工程的结构。

## 方法概览

### 组成部分

- Server states: follower, candidate, leader。
- Terms: logical clock and leader epoch。
- RPCs: `RequestVote`, `AppendEntries`, `InstallSnapshot`。
- Persistent state: `currentTerm`, `votedFor`, `log[]`。
- Volatile state: `commitIndex`, `lastApplied`, leader-side `nextIndex[]`, `matchIndex[]`。
- Safety properties: Election Safety, Leader Append-Only, Log Matching, Leader Completeness, State Machine Safety。

### 流程或协议

1. Follower 超时后成为 candidate，递增 term 并请求投票。
2. 获得多数票的 candidate 成为 leader，并发送 heartbeats。
3. Leader 接收 client command，append 到 log，通过 `AppendEntries` 复制。
4. 当前 term entry 复制到多数后 commit，并通知 followers apply。
5. Follower 与 leader log 不一致时，leader 通过 `nextIndex` 回退找到共同前缀并覆盖冲突后缀。
6. Reconfiguration 通过 joint consensus 从 old config 过渡到 new config。

### 关键定义、公式、算法或定理

- `broadcastTime << electionTimeout << MTBF`: availability timing condition。
- Up-to-date log: compare last log term first, then last log index。
- Commit current-term-only rule: 只有 current term entries 可通过多数计数直接提交。
- Joint consensus: old and new configs both need majorities。

### 假设条件

- Non-Byzantine/crash-stop or crash-recover faults with stable storage。
- Majority quorum 可通信。
- State machines deterministic。
- Safety 不依赖 timing；availability 依赖合理 timeout。

## 创新点

- 新思想: 将 understandability 作为 primary design goal，并用 decomposition/state-space reduction 约束协议形态。
- 对已有工作的扩展: 相比 Paxos，Raft 强化 leader，使 log entries 单向从 leader 流向 followers，减少机制复杂度。
- 工程贡献: 给出完整实现所需的 leader election、log replication、membership change、snapshotting、client semantics。
- 实证贡献: user study 支持 Raft 更易学习；TLA+ spec/proof 和 performance experiment 支持正确性/可用性。

## 实验与结果

- Understandability: 43 名学生，Raft quiz 平均 25.7，Paxos quiz 平均 20.8；33 名学生 Raft 得分更高。
- Correctness: 约 400 行 TLA+ specification；mechanically proven Log Completeness Property；informal proof of State Machine Safety。
- Performance: normal log replication 使用 leader 到多数的一轮 RPC；leader election 实验显示 timeout randomization 对避免 split votes 很关键。
- Recommended timeout: 150-300ms conservative election timeout。

## 局限性

### 作者明确说明

- Raft 是 non-Byzantine consensus，不处理 Byzantine behavior。
- Safety 不依赖 timing，但 availability 必然依赖 timing。
- Strong leadership 简化协议，但排除一些 leaderless/EPaxos 风格优化。
- TLA+ mechanical proof 仍依赖未机械检查的 invariants。

### 基于证据的推断

- Raft 更容易理解的证据来自学生 user study，虽有偏差控制，但不是工业实现正确性的充分证明。
- 与 Paxos/VR/Zab 的完整性能和复杂度比较还需要独立来源。

## 可复用思路

- 把工程协议拆成相对独立的机制: election、replication、safety、reconfiguration。
- 使用 majority intersection 设计 election 和 commit 规则。
- 用 current-term-only commit 避免旧 term 条目被错误提交。
- Reconfiguration 必须避免 old/new configs 同时形成独立多数。
- Client retry 必须有 serial number 去重；read-only optimization 也要维护 linearizability。

## 术语表

| Term | 解释 | 备注 |
| --- | --- | --- |
| Raft | leader-based crash-fault consensus algorithm | 本文提出 |
| Term | Raft 的 logical clock/epoch | 每个 term 至多一个 leader |
| Log Matching Property | 相同 index/term 的 entries 意味着此前日志前缀也相同 | safety foundation |
| Leader Completeness | committed entries appear in future leaders | election restriction 保证 |
| Joint consensus | old/new configurations overlapping majorities during reconfiguration | membership change safety |
| State Machine Safety | 同一 log index 不会被不同 servers apply 不同 commands | core safety property |

## Connections

- Extends: [[consensus|State machine replication]]
- New concepts: [[crash-fault-tolerance|Crash-fault tolerance]], [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|Raft]]
- Contrasts with: [[byzantine-fault-tolerance|Byzantine fault tolerance]], Paxos, Viewstamped Replication
- Related maps: [[consensus|Consensus]], [[crash-fault-tolerance|Crash-fault tolerance]]

## Evidence Table

| Claim | Evidence anchor | Claim type | Confidence |
| --- | --- | --- | --- |
| Raft manages a replicated log and is equivalent in result to multi-Paxos while using a different, more understandable structure. | p1 abstract/introduction | contribution | high |
| Raft decomposes consensus into leader election, log replication, safety, and membership changes to improve understandability. | p1, p3-p4 | design principle | high |
| RequestVote denies candidates whose logs are less up-to-date, ensuring future leaders contain committed entries. | p8-p9 §5.4.1 and proof sketch | mechanism/theorem | high |
| Raft only directly commits entries from the leader's current term by counting replicas; prior entries commit indirectly. | p8-p9 §5.4.2 | safety rule | high |
| Joint consensus requires majorities from old and new configurations to avoid split-brain reconfiguration. | p10-p11 §6 | mechanism | high |
| Safety does not depend on timing, but availability depends on `broadcastTime << electionTimeout << MTBF`. | p10 §5.6 | model boundary | high |
| User study found higher quiz scores for Raft than Paxos among 43 students. | p13-p14 §9.1 | empirical result | medium-high |
| Raft has a TLA+ specification and safety proof artifacts, with some proof limitations. | p14-p15 §9.2 | correctness evidence | high |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| Raft leaders only directly commit entries from their current term by majority replication; older entries become committed indirectly through Log Matching once a current-term entry commits. | `sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2#p8-p9` | folded_into_meta_note |
| Raft's RequestVote log up-to-date restriction prevents candidates missing committed entries from becoming leader, supporting the Leader Completeness Property. | `sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2#p8-p10` | folded_into_meta_note |
| Raft changes cluster membership through joint consensus, where decisions require separate majorities from old and new configurations so both configurations cannot decide independently. | `sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2#p10-p11` | folded_into_meta_note |
| Raft improves understandability by using strong leadership and decomposing consensus into leader election, log replication, safety, and membership changes. | `sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2#p1`<br>`sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2#p3-p4` | folded_into_meta_note |
| Raft safety does not depend on timing, but availability requires broadcast time to be much smaller than election timeout and election timeout to be much smaller than MTBF. | `sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2#p10` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `raft-strong-leader-decomposition-understandability`: Raft makes understandability a design goal through strong leadership and problem decomposition.
- `raft-election-restriction-leader-completeness`: RequestVote log up-to-date restriction enforces Leader Completeness.
- `raft-current-term-commit-rule-safety`: Raft only commits current-term entries directly by majority to avoid unsafe old-term commitment.
- `raft-joint-consensus-overlapping-majorities`: Joint consensus requires overlapping majorities from old and new configurations for safe membership changes.
- `raft-timing-affects-availability-not-safety`: timing affects availability, not safety.

### Concepts to update

- `crash-fault-tolerance`: create foundation concept seed.
- `raft`: create protocol concept seed.
- `state-machine-replication`: update with Raft as CFT source extension.

### Missing foundations

- Paxos and Viewstamped Replication as comparison sources.
- FLP impossibility and partial synchrony.
- ZooKeeper/Zab and production consensus implementations.

## Synthesis Handoff

- Create `vault/04_Knowledge/distributed-systems/consensus/crash-fault-tolerance.md`.
- Refresh `vault/04_Knowledge/distributed-systems.md` and `vault/04_Knowledge/distributed-systems/consensus.md`.
- Create `vault/04_Knowledge/distributed-systems/consensus/crash-fault-tolerance.md`.
- Keep consensus direction `foundation_thin` until Paxos/FLP/partial synchrony are absorbed.
