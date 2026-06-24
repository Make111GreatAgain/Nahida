---
id: "doi-10-5555-296806-296824"
title: "Practical Byzantine Fault Tolerance"
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
  - "p1-p3 abstract, introduction, system model, service properties"
  - "p3-p7 algorithm, normal case, checkpoint, view change, correctness"
  - "p7-p10 optimizations and implementation"
  - "p10-p13 performance evaluation and related work"
  - "p13-p14 conclusion and limitations"
safe_for_absorption: true
canonical_url: "https://dl.acm.org/doi/10.5555/296806.296824"
doi: "10.5555/296806.296824"
arxiv_id: ""
venue: "OSDI 1999"
year: "1999"
pdf_pages: 14
pdf_sha256: "5fa9f9b0f91c1df6b7d86b84682774c00aeec70274d5260f868d0be71946e10e"
local_pdf: "~/Desktop/paper/PBFT1.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/pbft1-5fa9f9b0f91c-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "byzantine-fault-tolerance"
  - "state-machine-replication"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "byzantine-fault-tolerance"
primary_ontology_path: "distributed-systems/consensus/byzantine-fault-tolerance/doi-10-5555-296806-296824"
secondary_ontology_paths:
  - "distributed-systems/replication/state-machine-replication/doi-10-5555-296806-296824"
path_update_status: "propagated"
domains:
  - "distributed-systems"
topics:
  - "byzantine-fault-tolerance"
  - "state-machine-replication"
aliases:
  - "PBFT"
tags:
  - "nahida/source"
  - "paper"
  - "distributed-systems"
  - "consensus"
  - "byzantine-fault-tolerance"
  - "state-machine-replication"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "consensus"
  problem:
    - "byzantine-fault-tolerance"
    - "state-machine-replication"
  method_family:
    - "primary-backup replication"
    - "three-phase atomic multicast"
    - "view change"
  system_layer:
    - "replicated services"
  evaluation_context:
    - "NFS implementation"
    - "Andrew benchmark"
  application:
    - "Byzantine-fault-tolerant file system"
  bridge:
    - "BFT theory -> practical replicated services"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-practical-byzantine-fault-tolerance"
source_refs:
  - "doi:10.5555/296806.296824"
  - "pdf:~/Desktop/paper/PBFT1.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "distributed-systems -> consensus"
secondary_directions:
  - "distributed-systems -> replication"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title"
  - "known DOI"
  - "abstract"
  - "full PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0002"
queue_status: "absorbed"
---

# Practical Byzantine Fault Tolerance

## 论文身份

- 标题: Practical Byzantine Fault Tolerance
- 作者: Miguel Castro, Barbara Liskov
- 机构: MIT Laboratory for Computer Science
- 会议/期刊: OSDI 1999
- 年份: 1999
- DOI: `10.5555/296806.296824`
- 链接: https://dl.acm.org/doi/10.5555/296806.296824
- 本地 PDF: `~/Desktop/paper/PBFT1.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/pbft1-5fa9f9b0f91c-pages.txt`
- 代码/数据: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 14
- 已覆盖章节/页码: p1-p14 full text, including system model, algorithm, view change, optimizations, implementation, evaluation, related work, conclusion
- 已检查附录: 无附录
- 未覆盖章节/页码: references 未逐条外部读取
- Extraction gaps: 数学符号如 `3f+1`, `2f+1`, `f+1` 在抽取中有断行，但上下文可恢复；核心正文可读

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1-p2 | 引言与贡献 | 第一个 practical state-machine replication protocol，安全性不依赖 synchrony，并实现 BFS/NFS | 定位贡献 | 给性能目标和系统背景 |
| p2-p3 | System model / Service properties | asynchronous network, Byzantine failure, cryptographic authentication, safety/liveness assumptions, `3f+1` optimality | 模型与正确性边界 | 安全/活性条件分离 |
| p3-p5 | Normal-case operation | primary/backups, client request, pre-prepare/prepare/commit, prepared/committed predicates | 核心协议机制 | state machine total order |
| p5-p6 | Checkpoint / garbage collection | stable checkpoint with `2f+1` matching checkpoint messages, water marks | 日志截断与状态证明 | 保证 view change 可恢复 |
| p6-p7 | View changes / correctness | timeout triggered view change, `2f+1` view-change messages, new-view construction, safety/liveness sketch | primary fault handling | 与 Paxos/Viewstamped 类比 |
| p7-p8 | Non-determinism / optimizations | deterministic non-deterministic values, tentative execution, read-only fast path | 实用优化 | 性能关键 |
| p8-p10 | Cryptography / implementation | normal case uses MAC authenticators, signatures only for view-change/new-view; replication library + BFS | 工程实现 | 降低 public-key bottleneck |
| p10-p13 | Performance evaluation | 4 replicas tolerate 1 Byzantine fault; microbenchmark, Andrew benchmark, BFS vs NFS | 实证证据 | BFS strict total only 3% slower than NFS-std |
| p13-p14 | Related work / conclusion | 相比 Rampart/SecureRing，不依赖 failure detector exclusion for safety；未来方向 | 边界和贡献总结 | practical BFT milestone |

## 核心精读笔记

### 背景、动机与问题边界

PBFT 的核心动机是把 Byzantine fault tolerance 从早期理论可行性推进到可运行服务。作者指出之前许多 Byzantine agreement/replication 方法要么主要证明可行但太慢，要么依赖 synchrony/failure detectors；在攻击者可延迟消息或节点的情况下，错误地把 non-faulty replica 排除出 group 会破坏安全性。

本文解决的是 deterministic replicated service 的 state machine replication。服务有状态和操作，clients 发起请求并等待响应。PBFT 保证 safety 为 linearizability，并说明 safety 不依赖 synchrony；liveness 需要弱同步假设，也就是网络故障最终修复、消息延迟不无限增长。本文不解决 fault-tolerant privacy，因为 replicas 需要明文状态和请求来执行任意服务操作。证据锚点: p1-p3。

### 模型、假设与定义

系统模型是 asynchronous distributed system，网络可能丢失、延迟、重复或乱序消息。故障模型是 Byzantine: faulty nodes 可任意行为，但假设 node failures 独立；为抵抗恶意攻击，作者建议不同实现、不同 OS、不同管理员等多样化措施。加密假设包括 public-key signatures、MACs、collision-resistant hashes，攻击者 computationally bounded，不能伪造 non-faulty node 的签名或破坏 digest。

服务属性方面，PBFT 需要 `n = 3f + 1` replicas 才能容忍 `f` Byzantine replicas。client 接受结果时等待 `f+1` matching replies，因为至少一个来自 non-faulty replica。normal-case commit 使用 `2f+1` prepare/commit 类阈值，保证交集包含 non-faulty replica。证据锚点: p2-p5。

### 方法、协议或系统机制

PBFT 是 primary-backup 风格的 state machine replication。replicas 处在连续编号的 views 中，每个 view 有一个 primary，其他为 backups；primary 由 view number mod replica count 决定。client 向 primary 发送请求，primary 给请求分配 sequence number，并启动三阶段 atomic multicast: pre-prepare, prepare, commit。

pre-prepare 阶段中 primary 发送 view、sequence number 和 request digest。backup 接受 pre-prepare 前要检查签名、view、是否已有冲突 pre-prepare，以及 sequence number 是否在 low/high water mark 之间。prepare 阶段 backups 广播 prepare；当 replica 拥有 request、matching pre-prepare、以及 `2f` matching prepares 时，`prepared(m, v, n, i)` 为真。commit 阶段 replica 在 prepared 后广播 commit；当 prepared 且收到 `2f+1` matching commits 时，`committed-local` 为真，replica 按 sequence order 执行请求并回复 client。

checkpoint 机制用于日志截断和 view change 证明。replicas 周期性生成 checkpoint digest；当某个 sequence number 的 checkpoint 收到 `2f+1` matching checkpoint messages 时成为 stable checkpoint，replica 可以丢弃更早的协议消息。view change 在 backup 等待请求超时后触发，新的 primary 收集 `2f+1` valid view-change messages，选择最新 stable checkpoint 和需要保留的 prepared requests，为新 view 构造 pre-prepare 集合，填补 null requests，保证跨 view 的已提交请求不会被不同请求替换。证据锚点: p3-p7。

### 理论、证明或正确性论证

Safety 依赖两个交集不变量。第一，同一 view 中，如果某个 non-faulty replica prepared 了 digest `d`，另一个 non-faulty replica 不可能为同一 view/sequence prepared 不同 digest，因为 `3f+1` 和 `2f+1`/`2f` 的交集至少含一个 non-faulty replica，而 non-faulty replica 不会发冲突 prepare。第二，view-change protocol 把先前 view 中已经 prepared/committed 的 request 携带到后续 view，或者通过 stable checkpoint 排除旧 sequence numbers。

Liveness 不能在纯异步中无条件保证，因为那会违反 FLP。PBFT 通过 view change、指数退避 timer、以及收到 `f+1` higher-view messages 后跟进 view change，保证在消息延迟不无限增长时 eventually progress。faulty primary 最多连续 `f` 个 views，因为 primary 按 view number 轮转。证据锚点: p6-p7。

### 实验、评估或案例

作者实现了 replication library，并构建 BFS: Byzantine-fault-tolerant NFS。实验设置中 4 replicas 容忍 1 Byzantine fault，运行在 DEC 3000/400 Alpha workstations、10Mbit/s switched Ethernet、Digital Unix 4.0，checkpoint interval 为 128 requests。

Microbenchmark 中 null operation read-write 0/0 为 3.35 ms，无复制 UDP 为 0.82 ms；read-only 0/0 为 1.62 ms。作者解释 read-only overhead 较低，因为优化把通信轮次降为单 round-trip。Andrew benchmark 中 BFS strict 总耗时 64.48s，BFS-nr 51.07s，overhead 26%；与 Digital Unix NFS-std 的 62.52s 对比，BFS strict 只慢 3%，开启 read-only lookup 后总耗时 61.07s，甚至比 NFS-std 快 2%。证据锚点: p10-p13。

### 作者结论与我的判断

作者的核心结论是 PBFT 将 Byzantine state-machine replication 做到 practical: safety 不依赖 synchrony，性能比 Rampart/SecureRing 高一个数量级以上，并用 BFS/NFS 证明真实服务的 overhead 可接受。

我的判断: PBFT 是 `distributed-systems/consensus/byzantine-fault-tolerance` 从理论模型走向 practical state-machine replication 的关键 source extension。它应当和 1982 Byzantine Generals 分开记录: 前者定义 fault model/threshold foundation，PBFT 贡献 primary-backup view、three-phase atomic multicast、checkpoint/view change、MAC-based authentication 和 NFS 实证。后续 Tendermint/HotStuff/区块链 BFT 可把 PBFT 的 prepare/commit quorum、view change 和 cryptographic authentication 当作历史锚点，但不能忽略链上网络、leader rotation、block proposal、经济安全等额外维度。

## 层级候选分类

- L1 Domain candidate: `distributed-systems`
- L2 Direction candidate: `consensus`
- L3 Topic/content cluster candidates: `byzantine-fault-tolerance`, `state-machine-replication`
- Ontology path: `distributed-systems/consensus/byzantine-fault-tolerance/doi-10-5555-296806-296824`
- 备选归属: `distributed-systems/replication/state-machine-replication`
- 父级领域: distributed systems
- 学术子领域: fault-tolerant replication, Byzantine consensus
- 任务/问题: practical replicated service with Byzantine replicas
- 方法族: primary-backup, three-phase atomic multicast, view change, checkpointing
- 模型/协议/算法族: PBFT, state machine replication
- 评测场景: microbenchmark, Andrew benchmark, NFS V2
- Benchmark/应用: BFS, Byzantine-fault-tolerant NFS
- 别名: PBFT, Practical BFT
- 相邻方向: Paxos/Viewstamped Replication, crash-fault state machine replication, blockchain BFT
- 置信度: high
- 分类理由: 全文围绕 Byzantine-fault-tolerant state machine replication，并以真实服务实现和 benchmark 为证。
- 分类状态: accepted
- 分类证据: p1 contribution, p2-p3 model, p3-p7 algorithm, p10-p13 evaluation

## 一句话贡献

PBFT 提出并实现了一个 practical Byzantine state-machine replication protocol，在 `3f+1` replicas、弱同步 liveness 假设和 cryptographic authentication 下，用 pre-prepare/prepare/commit、checkpoint、view change 和 MAC 优化实现安全且高效的复制服务。

## 问题设定

给定一个 deterministic replicated service，replicas 可能 Byzantine faulty，网络异步且可能丢失/乱序/延迟消息。系统要提供 linearizability safety，并在最多 `f` faulty replicas 和最终有界延迟下提供 liveness。faulty clients 不能破坏 non-faulty clients 对服务状态的 consistent observation，但服务本身仍需 access control 限制恶意 client 的业务层破坏。

## 方法概览

### 组成部分

- Primary/backups and views.
- Three-phase normal case: pre-prepare, prepare, commit.
- Client waits for `f+1` matching replies.
- Prepared predicate requires pre-prepare plus `2f` matching prepares.
- Committed-local requires prepared plus `2f+1` matching commits.
- Stable checkpoints require `2f+1` matching checkpoint messages.
- View change requires `2f+1` view-change messages and new-view construction.
- MAC authenticators replace normal-case public-key signatures.

### 假设条件

- `n = 3f + 1` replicas.
- deterministic state machine and same initial state.
- cryptographic assumptions for signatures, MACs, digests.
- independent node failures for malicious-fault resilience.
- safety independent of synchrony; liveness needs delay not grow faster than timeout indefinitely.

## 创新点

- 新思想: 将 Byzantine state-machine replication 做成 practical primary-backup protocol。
- 对已有工作的扩展: 相比早期理论算法和 Rampart/SecureRing，避免依赖 synchrony/failure detector exclusion 来保证 safety。
- 工程贡献: MAC authenticators、read-only fast path、tentative execution、checkpoint optimization、incremental digest。
- 实证贡献: BFS/NFS 实现和 Andrew benchmark 证明 normal-case overhead 接近商用 NFS。

## 实验与结果

| 实验 | 设置 | 主要结果 | Caveat |
| --- | --- | --- | --- |
| Microbenchmark | 4 replicas, null operations | read-write 0/0 3.35 ms, read-only 0/0 1.62 ms, unreplicated 0.82 ms | worst-case overhead because operation does no useful work |
| Andrew BFS vs BFS-nr | BFS strict vs no replication | total 64.48s vs 51.07s, overhead 26% | normal-case, no view changes |
| Andrew BFS vs NFS-std | BFS strict vs Digital Unix NFS | total 64.48s vs 62.52s, only 3% slower | specific hardware/network, NFS V2 workload |
| Read-only lookup optimization | BFS r/o lookup | total 61.07s, 2% faster than NFS-std | modifies strict Unix atime semantics |

## 局限性

### 作者明确说明

- 不提供一般 fault-tolerant privacy。
- 当前 replication library 未实现 view changes/retransmissions，但完整算法已 formalized/proved in separate technical memo。
- 不能 mask 所有 replicas 上共同出现的软件错误。
- 未来仍需降低资源消耗，如 witnesses 和减少 state copies。

### 基于证据的推断

PBFT 是 practical milestone，但它不是现代区块链 BFT 的完整模板。区块链场景需要额外处理开放网络、validator set change、leader schedule、block propagation、economic incentives 和 DoS 模型。

## 可复用思路

- 用 pre-prepare/prepare/commit 区分 same-view total order 与 cross-view safety。
- 用 checkpoint certificates 作为日志截断和 state transfer 的可验证边界。
- 把 public-key cryptography 从 normal path 移到 view-change path，用 MACs 降低延迟。
- 对 deterministic requirement 下的 nondeterminism 单独协议化，避免 replicas state divergence。

## 术语表

| Term | 说明 |
| --- | --- |
| PBFT | Practical Byzantine Fault Tolerance protocol。 |
| State machine replication | 复制 deterministic state machine，并让 replicas 执行同一请求顺序。 |
| View | primary/backups 的配置编号。 |
| Pre-prepare | primary 为请求分配 sequence number 的阶段。 |
| Prepare | backups 传播对 pre-prepare 的接受，建立 same-view ordering。 |
| Commit | 确保跨 view committed request 的 ordering。 |
| Stable checkpoint | 有 `2f+1` matching checkpoint messages 的状态摘要。 |
| MAC authenticator | normal-case 用于替代 signatures 的 per-replica MAC vector。 |

## Connections

- Extends: [[byzantine-fault-tolerance|Byzantine fault tolerance]]
- Creates/extends: [[consensus|State machine replication]]
- Builds on: [[doi-10-1145-357172-357176-byzantine-generals-problem|The Byzantine Generals Problem]]
- Adjacent: Paxos, Viewstamped Replication, Rampart, SecureRing, HotStuff, Tendermint.

## Evidence Table

| Claim | Evidence anchor | Claim type | Confidence |
| --- | --- | --- | --- |
| PBFT provides Byzantine state-machine replication with `3f+1` replicas and safety independent of synchrony. | p1-p3 | mechanism/design | high |
| PBFT normal case uses pre-prepare, prepare, commit to establish total order and cross-view safety. | p3-p5 | mechanism | high |
| View changes preserve prepared/committed requests across views using `2f+1` view-change messages and new-view construction. | p6-p7 | mechanism | high |
| Normal-case performance depends on MAC authenticators and limiting public-key signatures to rare view-change/new-view messages. | p8 | implementation pattern | high |
| BFS strict is only 3% slower than Digital Unix NFS-std on the Andrew benchmark. | p12 table 3 | empirical_result | high |
| PBFT does not provide general fault-tolerant privacy and cannot mask common-mode bugs across all replicas. | p3, p13-p14 | limitation | high |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| PBFT 的 normal-case 性能很大程度来自用 MAC authenticators 替代 public-key signatures，并把 signatures 限制在较少发生的 view-change/new-view messages 上。 | `doi:10.5555/296806.296824#p8` | folded_into_meta_note |
| PBFT 的 safety 不依赖 synchrony，但 liveness 需要消息延迟不会无限快地超过 timeout 增长；这使 PBFT 避免了通过不可靠 failure detector 排除 replicas 来维持 safety。 | `doi:10.5555/296806.296824#p2-p3`<br>`doi:10.5555/296806.296824#p13` | folded_into_meta_note |
| PBFT 将 Byzantine state-machine replication 的 normal case 组织为 pre-prepare、prepare、commit 三阶段: pre-prepare/prepare 保证同一 view 内请求排序一致，prepare/commit 与 view-change protocol 一起保证跨 view 的 committed request 不被替换。 | `doi:10.5555/296806.296824#p3-p7` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `pbft-three-phase-state-machine-replication`: PBFT uses pre-prepare/prepare/commit to order requests safely across Byzantine replicas.
- `pbft-safety-liveness-assumption-split`: PBFT safety does not rely on synchrony, while liveness needs eventual timing progress.
- `pbft-mac-normal-path-practicality`: PBFT's normal-case practicality comes largely from replacing public-key signatures with MAC authenticators and using signatures rarely.

### Concepts to update

- `byzantine-fault-tolerance`: add practical state-machine replication source extension.
- `state-machine-replication`: create source-backed seed.

### Missing foundations

- Paxos/Viewstamped Replication as benign-fault ancestors.
- FLP/partial synchrony as liveness context.
- Modern BFT protocols and blockchain consensus as later extensions.

## Synthesis Handoff

- Refresh `byzantine-fault-tolerance-state-2026-06-11` to include practical BFT replication.
- Keep overall foundation status `foundation_thin` until FLP/partial synchrony and at least one modern protocol are absorbed.
