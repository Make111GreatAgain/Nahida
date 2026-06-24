---
id: "sha256-ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
title: "SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain"
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
  - "p1 abstract and introduction"
  - "p2-p3 motivation, contributions, related work"
  - "p4-p6 system assumptions, overview, communication flow"
  - "p7-p10 block replication, workload-adaptive BRT construction, failure recovery"
  - "p11-p12 block ordering and Sending-Receiving framework"
  - "p12-p16 evaluation, industrial comparison, conclusion, references"
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown in extracted PDF"
year: "2022"
local_pdf: "~/Desktop/paper/sraft6.pdf"
sha256: "ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
pages: 16
pdf_extractor: "codex-bundled-python:pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/sraft6-ae33e526eb0f-pages.txt"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "consensus"
topic_ids:
  - "permissioned-blockchain-consensus"
  - "crash-fault-tolerance"
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "permissioned-blockchain-consensus"
primary_ontology_path: "blockchain-systems/consensus/permissioned-blockchain-consensus/sha256-ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
secondary_ontology_paths:
  - "distributed-systems/consensus/crash-fault-tolerance/sha256-ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "consensus"
  topics:
    - "permissioned-blockchain-consensus"
    - "crash-fault-tolerance"
    - "leader-bottleneck-mitigation"
    - "workload-adaptive-replication"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "sraft"
  - "raft"
  - "crash-fault-tolerance"
  - "permissioned-blockchain-consensus"
  - "leaderless-replication"
  - "workload-adaptive-replication"
aliases:
  - "SRaft"
  - "Scalable CFT Consensus Protocol"
  - "SRaft for Permissioned Blockchain"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "consensus"
  - "permissioned-blockchain"
  - "crash-fault-tolerance"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "consensus"
  problem:
    - "CFT consensus scalability for permissioned blockchains"
    - "Raft leader bandwidth bottleneck"
    - "skewed workload distribution in geo-distributed blockchain peers"
  method_family:
    - "Raft variant"
    - "leaderless block replication"
    - "workload-adaptive tree replication"
    - "hash-based block ordering"
    - "Sending-Receiving ordering pipeline"
  system_layer:
    - "block replication"
    - "block ordering"
    - "commit pipeline"
  evaluation_context:
    - "LAN prototype benchmark"
    - "FISCO BCOS Raft comparison"
  application:
    - "permissioned blockchain"
  bridge:
    - "crash-fault consensus to permissioned blockchains"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-sraft-scalable-cft"
safe_for_absorption: true
source_refs:
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
  - "pdf:~/Desktop/paper/sraft6.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems/consensus"
secondary_directions:
  - "distributed-systems/consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract explicitly target a scalable CFT consensus protocol for permissioned blockchain"
  - "Sections 3-5 define SRaft as a Raft-style split between block replication and block ordering"
  - "system assumptions tolerate crash faults in 2f+1 peers and do not model Byzantine behavior"
  - "evaluation compares SRaft with Raft variants and FISCO BCOS Raft under workload skew"
taxonomy_version: "1.0"
---

# SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain

## 论文身份

- 标题: SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain
- 作者: extracted PDF 显示为 `No Author Given`
- 年份: 2022, 来自本地 queue/PDF metadata
- Venue/DOI/arXiv: extracted PDF 未给出
- 本地 PDF: `~/Desktop/paper/sraft6.pdf`
- SHA-256: `ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 16
- 已覆盖章节/页码: Abstract, Introduction, Background and Related Work, SRaft overview, Block Replication, Block Ordering, Evaluation, Conclusion, References
- Extraction gaps: PDF 未给出作者、机构、venue、DOI/arXiv；第一页作者占位为 `No Author Given`。公式和图可从文本中抽取出核心变量与含义，但没有额外图像复核。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p3 | 问题与贡献 | Permissioned blockchains 可采用 CFT/Raft，但 Raft leader 在大节点数、geo-distributed、skewed workload 下成为带宽瓶颈；SRaft 拆成 Block Replicating 与 Block Ordering | high |
| §2 / p3-p4 | 背景与相邻工作 | Raft/Paxos，S-Paxos、EPaxos、PigPaxos、MultiPaxos leader 拆分、CRaft 等 CFT scalability 工作 | medium-high |
| §3.1 / p4 | 系统假设 | 2f+1 peers 容忍 f crashed peers；partial synchrony/GST；专用 P2P 网络；PKI 身份认证 | high |
| §3.2-3.3 / p4-p7 | SRaft 总览与通信流 | 多个 Block Replicating Instances 并行、一个 Block Ordering Instance 排序 hash；两个子任务异步通信 | high |
| §4.1-4.2 / p7-p10 | Block Replication | 每个 peer 可作为 initiator；根据 workload/bandwidth 选择 One-to-All 或 Tree-based；BRT 描述转发路径 | high |
| §4.3 / p10 | 失败恢复 | initiator failure 通过 FAIL 与最高复制轮次恢复；relay failure 触发 BRT 重构与重复制 | high |
| §5.1-5.2 / p11-p12 | Block Ordering | leader 只排序已复制 block 的 hash；利用链结构把上一轮 commit 与下一轮 ordering proposal 合并为 Sending-Receiving RPC 框架 | high |
| §6 / p12-p16 | 实验 | LAN prototype；SRaft/SRaft-OA/SRaft-T/Raft/Raft-T；workload skew、scaling、sluggish peers、FISCO BCOS Raft 比较 | high |
| §7 / p16 | 结论 | SRaft 使用 workload-aware BRT 和 hash ordering 提升 permissioned blockchain 中 Raft-style CFT 的扩展性 | medium |

## 一句话贡献

SRaft 是面向 permissioned blockchain 的 Raft/CFT 变体：它把 bandwidth-heavy 的完整区块复制从单 leader 拆给所有 peers 以 leaderless/workload-adaptive BRT 方式完成，再让 ordering leader 只对已复制 block 的 hash 排序，从而缓解 Raft 在大规模许可链中的 leader 带宽瓶颈。

## 核心精读笔记

### 问题设定

论文把目标场景限定在 permissioned blockchain。作者认为许可链有严格准入机制和一定信任假设，因此很多系统可以支持 CFT 协议，如 Raft，而不必总是采用 permissionless setting 中更强的 BFT 假设。

Raft 的传统使用场景通常是 3 或 5 个副本的 replicated service；permissioned blockchain 往往 peer 数更多，且 clients/workload 分布在多个地理位置。Raft leader 需要接收所有 workload 并把完整 log/block 复制给 followers，因此上传带宽需求会随 peers 数近似增长为 `W * (N - 1)`。在 workload skew 下，重负载 peer 或 leader 的上传/下载带宽都可能成为瓶颈。

### 系统假设

SRaft 沿用 Raft 的 crash fault safety assumption：`2f + 1` 个 peers 可容忍 `f` 个 crashed peers。网络模型是 partial synchrony，即存在未知 GST，GST 后网络进入同步状态。论文还假设 peer 间使用专用 P2P 网络，且存在 PKI 做身份认证。

这意味着 SRaft 不是 Byzantine consensus。它没有处理恶意节点伪造、equivocation、审计惩罚、open membership 或 permissionless validator churn。

### SRaft 的两子任务架构

SRaft 将区块链共识拆为两个异步子任务:

- Block Replicating sub-task: 复制完整 block 内容，使多数 peers 持有该 block。
- Block Ordering sub-task: 收集已复制 blocks 的 hash，形成 `Pending Blocks Order` 并让 peers 对顺序达成一致。

系统中可以有多个 Block Replicating Instances 并行运行，每个 instance 有一个 initiator；但只有一个 Block Ordering Instance，其 leader 负责收集 hash、排序并推动提交。两个子任务异步通信，避免完整 block 复制直接阻塞 ordering leader。

### Leaderless block replication

每个 peer 都可以接收 client transactions、打包 block，并作为 initiator 发起一个 Block Replicating Instance。一个 block 被复制到多数 peers 后，initiator 认为复制成功，并把该 block 的 hash 发送给 ordering leader。

所有 Block Replicating Instances 并行且相互独立；每个 initiator 负责自己 block 的复制成败。这一设计把 Raft 里集中在 leader 的 block dissemination 负载分散到所有接收 workload 的 peers。

### Workload-adaptive replication 与 BRT

SRaft 的复制模式由 initiator 当前 workload 和可用带宽决定:

- One-to-All pattern: initiator 上传带宽足够支撑当前 workload 时，直接把 block 发给所有其他 peers。
- Tree-based pattern: initiator 过载时，把一部分转发任务交给轻负载 peers 作为 relay peers。

论文引入 Block Replicating Tree (BRT) 描述转发路径。BRT 的每个节点对应一个 peer，branch nodes 是有可用带宽的 relay peers。initiator 复制 block 时同时发送 BRT；relay peers 收到 block 后按 BRT 转发给子节点，并收集子节点 confirm messages，最终返回给 initiator。

可用带宽估算为:

```text
ab = B - (w * Stx) * (|N| - 1)
```

其中 `B` 是 peer bandwidth，`w` 是每秒接收交易数，`Stx` 是平均交易大小，`|N|` 是 peers 数。`ab > 0` 表示 peer 有可用带宽，`ab < 0` 时 overload volume `ov = |ab|`。

轻负载 peer 会把可用带宽按各 overloaded peers 的 `ov` 比例分配，分配给 peer `n` 的带宽份额为:

```text
ab_n = ab * ov_n / sum(ov_i)
```

initiator 收到可用带宽分配后构造 BRT。BRT root 的 children 数由 initiator 自身 bandwidth、workload 与 relay peers 总可用带宽共同决定；branch node 的 children 数按其分配到的 available bandwidth 比例决定。这样 SRaft 试图在不 flood 的前提下，把过载 initiator 的上传任务转给空闲 peers。

### 失败恢复

Initiator failure 分三类: block 已安全复制且已 commit；block 已安全复制但未 commit；block 未安全复制。后两类中，每个 peer 为每个 initiator 维护 timer；超时后向 ordering leader 发送 `FAIL(initiator.id)`。leader 广播 pending order 时携带 failed initiator id，peers 返回该 initiator 的最高复制 round number；leader 选择至少 `N/2 + 1` peers 达到的最高 round `n`，再把小于等于 `n` 的 blocks 放入 `Pending Blocks Order` 推进共识。

Relay peer failure 主要影响 Tree-based pattern 的多数确认。initiator 如果在 timeout 前没有收到 `N/2 + 1` 个 confirms，会针对未响应 peers 重构 BRT 并重新复制 block；同时向已确认 peers 发送 heartbeat，避免它们误触发 initiator timeout。

### Block Ordering 与 Sending-Receiving

Block Ordering sub-task 沿用 Raft-like majority confirm/commit flow，但只广播已安全复制 blocks 的 hash，而不是完整 block。若某 peer 本地缺少 `Pending Blocks Order` 中的 block，它可从其他 peers 拉取；因为这些 blocks 已经安全复制，最终应能取到。

SRaft 利用 blockchain chain structure 做流水线化。leader 广播当前 `Pending Blocks Order` 时，followers 返回 confirm vote，同时携带新完成复制的 block hashes；下一轮 leader 对这些新 hashes 排序，并在同一轮中提交上一轮 ordering result。论文把这个过程抽象为基于 RPC 的 Sending-Receiving communication framework，目的是把 ordering proposal、hash collection 和 previous-round commit 合并成工程上更简单的一类通信。

### 实验与结果

实验在 LAN 中模拟不同网络状态；机器为 `4 * 3.2GHz CPU`、`16GB RAM`、Ubuntu 16.04。client request 接收网络接口与 peer-to-peer 网络接口分离，P2P 网络不受 client submit 影响；request payload 为 500 bytes；不计 transaction execution time。作者实现了 Go prototype，并比较:

- SRaft: adaptive One-to-All/Tree-based。
- SRaft-OA: 只用 One-to-All。
- SRaft-T: 只用 Tree-based binary tree。
- Raft: 原始 Raft。
- Raft-T: 带 Tree-based replication 的 Raft 变体。

在 replication pattern 带宽实验中，35 peers 被分成 7 组，每个 peer P2P upload/download bandwidth 为 8Mb/s，总 workload 为 1.5K tx/s。skew setup 中高负载 peers 与低负载 peers 比例为 1:6，workload ratio 为 5:1，高负载在 N4。Tree-based pattern 让各组 NIC traffic 接近 uniform control，而 One-to-All 使 N4 peers 上传接近上限并限制吞吐。

在 workload skew rate 实验中，uniform workload 下 SRaft、SRaft-T、SRaft-OA 明显高于 Raft-T 和 Raft；论文报告相对 Raft-T/Raft 的吞吐提升分别达到约 `2.84x` 与 `25.2x`。随着 skew rate 上升，SRaft-OA 因高负载 peers 成为瓶颈而吞吐下降；tree-based replication 在高 skew 下把重负载 peers block replicating latency 控制得更好，论文报告 SRaft-OA 与 Raft 比 tree-based pattern 慢约 `2.8x`。

在 scalability 实验中，peer 数从 7 增至 35。SRaft 及其两个变体吞吐只轻微下降，而原始 Raft 因 peers 数增加带来的 leader replication 负担而明显下降。skew workload 下，相比 uniform workload，SRaft 和 SRaft-T 吞吐分别下降约 `15%` 和 `9%`，SRaft-OA 下降约 `31%`。

在 peer failure/sluggishness 实验中，35 peers 中有 15 个 sluggish peers，被人为增加 2 秒响应延迟。Tree-based pattern 可能受到 sluggish relay peers 影响；SRaft 因轻负载 peers 仍可用 One-to-All、重负载 peers 才用 Tree-based，平衡了吞吐和延迟。论文报告 SRaft/SRaft-T 吞吐比 SRaft-OA 高约 `1.29x`，Raft-T 吞吐约为 Raft 的 `4.2x`，延迟约为 Raft 的 `44%`。

工业实现对比使用 FISCO BCOS 的 Raft consensus module，7 peers，每个 peer upload/download bandwidth 为 40Mb/s，并禁用 execution 等其他模块以只比较 consensus。不同 workload skew rate 下，SRaft 吞吐约为 FISCO BCOS Raft 的 `5x` 到 `6.1x`。

## 可复用知识与来源内边界

### 可上升为 knowledge/source-extension 的内容

- CFT/Raft 被迁移到 permissioned blockchain 后，完整 block dissemination 的 leader bandwidth bottleneck 会被 peer 数、block size 与 workload skew 放大。
- 一个可复用的解决路线是拆分数据复制和顺序共识: 完整 block 由多 initiators/relay peers 复制，ordering leader 只排序 hash。
- workload-adaptive routing 可以把复制任务从 overloaded peers 转给 lightly loaded peers，但需要处理 relay failure 和可用带宽估计。

### 不应上升为基础概念的内容

- `SRaft` 本身是 source/protocol instance，不是 `consensus` 或 `CFT` 的父概念。
- `Block Replicating Tree` 是 SRaft 论文内部机制；除非后续多来源反复出现同类树式共识复制路径，否则留在 source note 与 source-extension 行中。
- FISCO BCOS 对比是本文实验上下文，不能单独推广成所有 permissioned blockchain Raft 实现的性能结论。

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 knowledge/bridge 以 source-extension 形式引用。上层节点应引用本元笔记，而不是复制整篇机制细节。

| Evidence point | Source anchor | Handling |
| --- | --- | --- |
| Permissioned blockchain 场景下，Raft leader 的上传带宽需求随 peers 数扩张，且 geo-distributed workload 会让转发到 leader 的下载路径和高负载 peer 成为瓶颈。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p1-p3` | source_extension |
| SRaft 将 consensus 拆成 Block Replicating 和 Block Ordering，二者异步运行；多个 replicating instances 并行，一个 ordering instance 排序 hash。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p4-p7` | source_extension |
| SRaft 的 system assumptions 是 CFT: `2f + 1` peers 容忍 `f` crashed peers，partial synchrony，PKI 身份认证；不覆盖 Byzantine 行为。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p4` | boundary |
| Block Replication 允许每个 peer 作为 initiator，block 复制到多数 peers 后才把 hash 交给 ordering leader。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p6-p7` | source_extension |
| BRT 根据 peer workload、transaction size、bandwidth 和可用带宽分配构造，branch nodes 由轻负载 peers 承担 relay。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p7-p10` | source_detail |
| Initiator failure 由 timer、FAIL 消息和多数 peers 的最高复制轮次恢复；relay failure 由 timeout、BRT 重构和重复制恢复。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p10` | source_detail |
| Block Ordering 只广播 block hash，缺失 block 的 peer 可从其他 peers 拉取；Sending-Receiving pipeline 将当前 proposal 与上一轮 commit 合并。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p11-p12` | source_extension |
| LAN 实验显示 Tree-based pattern 在 skew workload 下能把 NIC traffic 拉近 uniform control，避免高负载组上传带宽触顶。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p12-p13` | evaluation |
| SRaft 在 peer 数扩张、workload skew 和 sluggish peers 下相对 Raft/SRaft-OA 维持更好吞吐/延迟，工业对比中吞吐约为 FISCO BCOS Raft 的 `5x` 到 `6.1x`。 | `sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf#p13-p16` | evaluation |

## 概念与地图落点

| 层级 | 落点 | 说明 |
| --- | --- | --- |
| Primary topic | [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | 许可链中 CFT/Raft 共识的扩展性问题与解决路线 |
| Secondary topic | [[crash-fault-tolerance|Crash-fault tolerance]] | SRaft 的 fault model 与 Raft-family 背景 |
| Parent direction | [[blockchain-consensus|Blockchain consensus]] | 区块链共识方向下的 permissioned consensus 分支 |
| Parent direction | [[consensus|Consensus]] | 共识方向下的 CFT source extension |
| Bridge | [[crash-fault-consensus-to-permissioned-blockchains|Crash-fault consensus -> permissioned blockchains]] | CFT/Raft 向 permissioned blockchain workload 的 translation/application |

## 适用边界

- 适用于 permissioned blockchain / crash-fault tolerance / Raft-style ordering 场景。
- 不适用于 permissionless BFT、open membership、malicious validators 或经济安全结论。
- 实验刻意排除了 transaction execution time；结果主要说明 consensus/replication data path。
- 实验是 LAN 模拟，不等同于真实 geo-distributed WAN 部署。
- 论文没有给出完整形式化 safety/liveness 证明；其安全直觉主要来自 Raft-style majority 与已安全复制 block hash ordering。

## Path Materialization

| Path role | Ontology path | Action |
| --- | --- | --- |
| Primary | `blockchain-systems/consensus/permissioned-blockchain-consensus/sha256-ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf` | source note written and attached as source extension |
| Secondary | `distributed-systems/consensus/crash-fault-tolerance/sha256-ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf` | CFT source evidence added |
| Bridge | `distributed-systems/consensus/crash-fault-tolerance -> blockchain-systems/consensus/permissioned-blockchain-consensus` | bridge evidence refreshed |

## Path Propagation

| Target note | Planned update | Materiality |
| --- | --- | --- |
| [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | add SRaft full paper as source extension, refine leader bottleneck/workload-adaptive route | material |
| [[crash-fault-tolerance|Crash-fault tolerance]] | add CFT/Raft source extension; clarify source remains CFT, not BFT | material |
| [[blockchain-consensus|Blockchain consensus]] | add representative source ref and route to permissioned CFT branch | light |
| [[consensus|Consensus]] | add representative source ref under CFT replicated log route | light |
| [[crash-fault-consensus-to-permissioned-blockchains|Crash-fault consensus -> permissioned blockchains]] | add stronger 16-page SRaft evidence and experiment boundary | material |

## 吸收结果

- Source note: written as complete meta/source note.
- Knowledge handoff: ready for `nahida-knowledge-get`.
- Promotion decision: no new foundation knowledge node for SRaft or BRT; attach as source extension under CFT and permissioned blockchain consensus.
