---
id: "sha256-a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
title: "Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain"
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
  - "p2-p3 motivation, related work, security model"
  - "p4-p6 system overview, workload sensing, adaptive instance reconfiguration"
  - "p6-p8 failed instance recovery and practical considerations"
  - "p8-p9 complexity and threat analysis"
  - "p9-p12 correctness proofs and evaluation"
  - "p12-p13 conclusion and references"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown in extracted PDF"
year: "2023"
pdf_pages: 13
pdf_sha256: "a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
local_pdf: "~/Desktop/paper/v_srds2023.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/v_srds2023-a6106319a63e-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "consensus"
topic_ids:
  - "permissioned-blockchain-consensus"
  - "byzantine-fault-tolerance"
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "permissioned-blockchain-consensus"
primary_ontology_path: "blockchain-systems/consensus/permissioned-blockchain-consensus/sha256-a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/sha256-a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "consensus"
  topics:
    - "permissioned-blockchain-consensus"
    - "byzantine-fault-tolerance"
    - "multi-instance-bft"
    - "workload-adaptive-consensus"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "permissioned-blockchain-consensus"
  - "byzantine-fault-tolerance"
  - "HotStuff"
  - "leaderless consensus"
  - "multi-instance BFT"
  - "workload-adaptive consensus"
  - "failed instance recovery"
aliases:
  - "Stretch-BFT"
  - "Stretch-BFT: Workload-Adaptive and Stretchable BFT Consensus"
  - "Stretchable BFT consensus for permissioned blockchain"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "consensus"
  - "permissioned-blockchain"
  - "byzantine-fault-tolerance"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "consensus"
  problem:
    - "BFT consensus scalability for permissioned blockchains"
    - "leader/proposer bottleneck under block-format proposals"
    - "leaderless BFT latency under light workload or sluggish proposers"
    - "workload fluctuation in permissioned blockchain deployments"
  method_family:
    - "HotStuff-based BFT"
    - "multi-instance consensus"
    - "workload sensing"
    - "adaptive instance reconfiguration"
    - "failed instance recovery"
  system_layer:
    - "consensus instance scheduling"
    - "proposer selection"
    - "workload estimation"
    - "recovery path"
  evaluation_context:
    - "LAN prototype benchmark"
    - "bandwidth-limited consensus experiments"
    - "BFT-SMaRt, HotStuff, RCC comparison"
  application:
    - "permissioned blockchain"
  bridge:
    - "BFT consensus to permissioned blockchains"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-stretch-bft"
source_refs:
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
  - "pdf:~/Desktop/paper/v_srds2023.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> consensus"
secondary_directions:
  - "distributed-systems -> consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "PDF title and abstract explicitly target workload-adaptive consensus for permissioned blockchain"
  - "Sections 3-5 define HotStuff-based multi-instance BFT with workload sensing, reconfiguration, and recovery"
  - "security model uses N >= 3f + 1, partial synchrony, PKI, and Byzantine nodes"
  - "evaluation compares against BFT-SMaRt, HotStuff, RCC(f+1), and RCC(N)"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0022"
queue_status: "absorbed"
---

# Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain

## 论文身份

- 标题: Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain
- Queue title/alias: Stretch-BFT: Workload-Adaptive and Stretchable BFT Consensus
- 作者: extracted PDF 未显示作者列表
- 年份: 2023 from queue/PDF metadata
- Venue/DOI/arXiv: extracted PDF 未给出
- 本地 PDF: `~/Desktop/paper/v_srds2023.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/v_srds2023-a6106319a63e-pages.txt`
- SHA-256: `a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 13
- 已覆盖章节/页码: Abstract, Introduction, Motivation, Related Work, Security Model, Stretch-BFT Protocol, Workload Sensing, Adaptive Reconfiguration, Failed Instance Recovery, Practical Considerations, Complexity, Threat Analysis, Correctness, Evaluation, Conclusion, References
- Extraction gaps: PDF metadata 未提供作者、venue、DOI/arXiv。抽取文本保留公式和核心实验数字，但部分图表只可读出正文解释。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题和贡献 | Permissioned blockchain 中 proposer/leader 可能成为 bottleneck；leaderless BFT 能并行但在 light workload 和 sluggish proposer 下增加 latency；Stretch-BFT 自适应实例数 | high |
| §2 / p2-p3 | 动机与相邻工作 | 对比 leader-based PBFT/HotStuff/SBFT/BFT-SMaRt 和 leaderless Mir-BFT/RCC 等；解释 workload fluctuation | high |
| §3 / p3-p4 | 安全模型与总览 | Partial synchrony, `N >= 3f + 1`, PKI；epoch/era/instance 架构；以 HotStuff 为 master protocol | high |
| §4 / p4-p6 | BFT workload sensing | Consistent hashing 分配 transaction；收集 `2f+1` workload reports；排序后去掉最高/最低各 `f` 个，估计系统 workload | high |
| §5 / p6 | Adaptive instances reconfiguration | 每个 Era 末根据 workload 和 throughput 的偏差率 `DR` 决定下个 Era instance count，并确定 proposer 集合 | high |
| §6 / p6-p8 | Failed instance recovery | Heavy workload 下 piggyback recovery；light workload 下 proposer replacement；跨 Era recovery 和 workload report handling | high |
| §7 / p8 | 实践问题 | 硬件异构、transaction eventual commit、持续慢实例的额外触发规则 | medium-high |
| §8-10 / p8-p10 | 复杂度、威胁分析、正确性 | 单实例与多实例复杂度，Byzantine workload report/client skew 分析，安全和活性证明 | high |
| §11 / p10-p12 | 实验 | Instance count、workload sensing、对比 BFT-SMaRt/HotStuff/RCC、proposer failure、scalability | high |
| §12 / p12-p13 | 结论与引用 | 总结 Stretch-BFT 的 workload-adaptive/stretachable BFT route | medium |

## 一句话贡献

Stretch-BFT 是面向 permissioned blockchain 的 HotStuff-based BFT 扩展：它把一个固定 leader/proposer 的共识过程伸缩为按 Era 调整实例数的多实例 BFT，在高负载时增加并行 proposers 提升吞吐，在低负载或存在 sluggish proposer 时减少实例数以控制 latency，并提供 BFT workload sensing、instance reconfiguration 和 failed instance recovery。

## 核心精读笔记

### 问题设定

论文认为 permissioned blockchain 的交易通常以 block 形式提议，因此 leader/proposer 不只是排序少量 metadata，还要广播 block proposal；当节点数、block size 或 workload 上升时，单 proposer 成为 upload bottleneck。Leaderless BFT 通过多个 proposer/multiple consensus instances 分摊 proposal 负载，但固定地启用许多 instances 并不总是好: light workload 下吞吐不是主目标，多个 proposer 反而让每个 block 的完成时间受 slowest/sluggish/Byzantine proposer 影响。

Stretch-BFT 的核心问题不是“永远最大化 throughput”，而是在 workload 波动时选择合适的实例数: heavy workload 时伸展到更多 instances；light workload 时收缩到少量 instances，减少资源浪费和尾部 latency。

### 安全模型与架构边界

Stretch-BFT 使用 partial synchrony: 存在 GST，GST 后消息延迟有已知上界。系统有 `N` 个 nodes，最多 `f` 个 Byzantine nodes，要求 `N >= 3f + 1`。节点间使用 PKI 身份认证。论文以 HotStuff 作为 foundation/master protocol，因此 safety、QC、SAFENODE 等概念继承自 HotStuff-style BFT。

协议单位分为:

- Epoch: 每个 epoch 中多个 instances 并行运行；每个 instance 对一个 sub-block 达成共识。
- Era: workload sensing 和 reconfiguration 周期；一个 Era 内 instance configuration 固定，Era 末计算下一个 Era 的 instance count 和 proposer set。
- Block construction: 同一 epoch 的多个 sub-block 以确定性顺序合并为完整 block。

### BFT workload sensing

论文把 workload sensing 的困难拆为三类: Byzantine nodes 可能谎报 workload；同一 transaction 不能被多个节点重复计入；所有 correct nodes 必须得到一致 workload estimate。Stretch-BFT 使用 consistent hashing 把 transaction 映射到节点，减少重复计数和 uneven assignment。Permissioned blockchain 中 client 有身份，恶意 client 若把大量交易偏置到少数节点，理论上可被检测、限制或惩罚。

每个 proposer 在 sub-block 中携带收集到的 local workload reports。报告一旦通过共识进入链，所有 correct nodes 都能用同一组 reports 做确定性计算。每个节点收集至少 `2f + 1` reports 后，将 reports 排序，去掉最高 `f` 个和最低 `f` 个，平均剩余值为 `WLaver`，再估计系统 workload:

```text
SysWL = WLaver * (3f + 1)
```

这个 trimmed-average 结构让最多 `f` 个 Byzantine report 很难单方面把估计拉到极端；代价是 sensing reports 也会增加通信量。论文说明 proposer 收集 `2f+1` reports 并广播带 report 的 sub-block 约为 `O(N^2)`，若每个 Era 含 `K` 个 epochs，可把 report 分摊到 `O(N^2 / K)`，但 `K` 越大 sensing 越不敏感。

### Adaptive instances reconfiguration

Stretch-BFT 在 Era `n` 中收集 Era `n-1` 的 workload reports，并在 Era 末统计 Era `n-1` 的 throughput `T`。如果 workload 与 throughput 偏差超过阈值 `DR`，协议按比例调整下个 Era 的 instance count:

```text
|I_{n+1}| = ceil(W_{n-1} / T_{n-1} * |I_{n-1}|)
```

如果 workload 与 throughput 接近、实例数稳定，但 throughput 下降，则按 throughput 变化比例减少 instances:

```text
|I_{n+1}| = ceil(T_{n-1} / T_{n-2} * |I_{n-1}|)
```

`DR` 用于避免实例数在边界附近频繁震荡。论文的目标可概括为: 在满足 workload demand 的同时，使用尽可能少的 instances，从而避免 light workload 下 leaderless design 的慢 proposer latency 暴露。

Proposer selection 使用 deterministic random: 对候选节点号和 Era number 做 hash，hash 较小者入选。Era switch 使用 `NEW-Era` signed messages；下个 Era 的 proposers 聚合 `f+1` 个 `NEW-Era` 消息并附到 sub-block 中。`f+1` 至少包含一个 honest node，因此可代表 honest deterministic result。

### Failed instance recovery

Stretch-BFT 的 recovery 按 workload 状态分两条路径:

- Heavy workload: 所有节点都可能是 proposers，没有 spare proposer。节点广播 `FAILURE(n, i, e, prepareQC)`，收集 `2f+1` 个 FAILURE 后选择最高 epoch 的 `prepareQC` 作为 `highQC`，并把 recovery 结果 piggyback 到其他仍在运行的 instances 的 sub-block 中。若多个 instances 同时恢复同一失败 instance，论文用更低 epoch number、再更低 instance number 做确定性优先级。
- Light workload: instance 数少于节点数，存在 spare nodes。候选 proposer 收集 `2f+1` FAILURE messages 后选择 highQC，重新发起三轮投票恢复 failed instance。若 candidate 自身失败或 timeout，再恢复 candidate 或退回 piggyback path。

跨 Era 时，如果失败的是 Era 最后一个 epoch 的 instance，后续没有 running instances 可 piggyback；协议先运行 recovery 而不产生新 sub-block，再进入新 Era。Workload reports 在 recovery 中也要避免重复广播: replacement proposer 或 piggyback proposer 只继续广播剩余 reports。

### 复杂度和系统边界

单 HotStuff-style instance 中，threshold signature 可让 follower communication 为 `O(1)`，leader communication 为 `O(N)`。多个 instances 后，每个节点在 `S` 个 instances 中作为 follower，且最多作为一个 instance leader；单节点最大通信负载近似 `O(S + N)`，全网负载为 `O(N*S)`。这说明多实例可以分散 proposer 上传瓶颈，但不会无限提升吞吐，因为每个节点最终仍要接收/验证每笔交易。论文把 worst-resourced node 的 receive rate 和 verify rate 作为 Maximum Stable Throughput 的上限。

Stretch-BFT 也显式依赖 permissioned setting: client 身份、节点资源配置、硬件异构权重、恶意 client 限制等都不是 permissionless public chain 可直接假设的能力。

### 正确性和威胁分析

论文的 safety 证明继承 HotStuff。Instance safety 由 HotStuff 的 QC/SAFENODE 保证；failed recovery 使用 highQC 和确定性优先级，保持恢复结果一致；Era reconfiguration 因为所有 correct nodes 从已共识 reports 和 blocks 计算 workload/throughput，故能得到相同下个 Era 配置。最终 theorem 说明每个 epoch 中 correct nodes 构造相同 block。

Liveness 方面，failed instance eventually recovered，且每个节点最终得到至少 `2f+1` workload reports；如果前一个 Era 完成，Stretch-BFT 可进入下一个 Era。

Threat analysis 的重点是 workload manipulation。最多 `f` 个 Byzantine nodes 可统一高报或低报，但排序去极值后，最终估计由 honest reports 主导。恶意 clients 若集中提交映射到少量节点的交易，会影响短期性能；论文依赖 permissioned chain 的 client identity 来限制或惩罚这类行为，而不把它视为核心 safety break。

### 实验与结果

实验在 LAN 环境中进行，机器为 `4 * 3.2GHz CPU`、`16GB RAM`、Ubuntu 16.04；client request 和 P2P 使用不同 NIC；transaction payload 为 100 bytes；不计 transaction execution time，存储为异步持久化。

Instance count 实验区分 heavy workload 和 light workload，并测试不同 batch sizes。结论是 upload bottleneck 下增加 instances 可近似线性提升 throughput 且不显著增加 latency；但当 download bandwidth 成为瓶颈时，更多 instances 或更大 batch 只会增加 receiving latency，throughput 在若干 instances 后趋于稳定。Light workload 下单 instance 与多 instance 的性能接近，因此固定使用多实例不划算。

Workload sensing 实验显示，sample 太小时估计误差较大；workload 到 `10K/s` 时 Byzantine nodes 统一高报/低报下 deviation 小于约 `6%`，到 `100K/s` 时小于约 `3%`。

与 BFT-SMaRt、HotStuff、RCC(f+1)、RCC(N) 的比较中，Stretch-BFT 在 workload 增加时通过增加 instances 提升吞吐；heavy workload 下 Stretch-BFT/RCC 相比 HotStuff/BFT-SMaRt 有显著 throughput advantage。Light workload 时各协议性能更接近，但 Stretch-BFT 使用更少 instances，并在 proposer rotation 下比固定 leaderless instances 更能避免 sluggish proposer 的尾部影响。

Proposer failure 实验说明: heavy workload 下所有节点都是 proposers，一个 proposer 失败后没有 spare proposer，throughput 会下降且不完全回升；medium/light workload 下 replacement proposer 可让 TPS 在恢复后反弹。Scalability 实验在 bandwidth-limited setting 下增加节点数，Stretch-BFT 通过增加 instances 抵消 proposer 负载增长，throughput 没有明显下降，但 latency 会随节点数增加而升高。

## 可复用知识与来源内边界

### 可上升为 knowledge/source-extension 的内容

- Permissioned blockchain 中，BFT leader/proposer bottleneck 与 CFT/Raft leader bottleneck相似，但 fault model 和 recovery 边界更强: 需要处理 Byzantine proposer、伪造 workload report、failed instance recovery。
- 多实例/leaderless BFT 不是单向“越多越好”；它在 heavy workload 下扩展吞吐，在 light workload 下可能因 slowest/sluggish proposer 增加 latency。
- Workload-adaptive consensus 可把 sensing、deterministic reconfiguration、proposer selection 和 recovery 纳入一个 Era-level control loop。
- Permissioned environment 的 client identity 和节点资源配置能支持 workload sensing 与 client abuse handling，但这不是开放链可直接迁移的假设。

### 不应上升为基础概念的内容

- `Stretch-BFT` 是 source/protocol instance，不应单独成为 foundation concept。
- `BFT Workload Sensing`、`Adaptive Instances Reconfiguration`、`Piggyback Recovery` 是本文机制，除非后续多来源反复出现同类设计，否则保留在 source note 和 source extension 中。
- LAN benchmark 和具体倍率是本文实验上下文，不能直接推广为所有 HotStuff/RCC/BFT-SMaRt 实现的性能排序。

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 knowledge/bridge 以 source-extension 形式引用。上层节点应引用本元笔记，而不是复制整篇机制细节。

| Evidence point | Source anchor | Handling |
| --- | --- | --- |
| Permissioned blockchain 的 BFT proposer 需要广播 block proposal，节点数和 workload 增加会放大 proposer bottleneck。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p1-p3` | source_extension |
| Leaderless/multi-instance BFT 在 heavy workload 下可分摊 proposal 负载，但 light workload 下会暴露 slowest/sluggish proposer latency。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p1-p3` | source_extension |
| Stretch-BFT 以 HotStuff 为 master protocol，运行在 partial synchrony、`N >= 3f + 1`、PKI 的 BFT 模型中。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p3-p4` | boundary |
| Protocol architecture 使用 Epoch/Era/Instance: Era 内配置固定，Era 末用 workload sensing 和 throughput 调整下个 Era instance count。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p4-p6` | source_extension |
| Workload sensing 使用 consistent hashing、`2f+1` reports、去掉最高/最低各 `f` 个并平均剩余值估计 system workload。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p4-p5` | source_detail |
| Failed instance recovery 区分 heavy workload piggyback recovery 与 light workload proposer replacement，并用 highQC/SAFENODE/priority 保持一致性。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p6-p8` | source_extension |
| Complexity analysis 指出多实例分散 proposer 负载，但全网仍为 `O(N*S)`，worst-resourced node 的接收/验证能力限制最大稳定吞吐。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p8-p9` | boundary |
| Correctness proofs 通过 HotStuff instance safety、recovery consistency 和 deterministic Era reconfiguration 推出 epoch block 一致。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p9-p10` | proof_summary |
| Evaluation 显示 heavy workload 下增加 instances 可提升 throughput；download bottleneck 或 light workload 下盲目增加 instances 会拉高 latency 或浪费资源。 | `sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122#p10-p12` | evaluation |

## 概念与地图落点

| 层级 | 落点 | 说明 |
| --- | --- | --- |
| Primary topic | [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | 许可链中 BFT consensus 的 proposer bottleneck、workload fluctuation 和多实例伸缩路线 |
| Secondary topic | [[byzantine-fault-tolerance|Byzantine fault tolerance]] | Stretch-BFT 的 fault model、HotStuff foundation 和 BFT recovery 机制 |
| Parent direction | [[blockchain-consensus|Blockchain consensus]] | 区块链共识方向下的 permissioned BFT consensus evidence |
| Parent direction | [[consensus|Consensus]] | 共识方向下的 BFT/multi-instance source extension |
| Bridge | [[bft-consensus-to-permissioned-blockchains|BFT consensus -> permissioned blockchains]] | BFT SMR/HotStuff-style quorum logic 到 permissioned blockchain workload control 的 application/translation |

## 适用边界

- 适用于 permissioned blockchain / BFT / known membership 场景。
- 不直接适用于 permissionless open membership、stake economics、validator churn 或 public-chain client anonymity。
- Workload sensing 假设 client identity、transaction-to-node assignment 和节点资源信息可被系统利用。
- 评估是 LAN prototype；不计 transaction execution time 和同步持久化，不能单独代表真实生产部署性能。
- Stretch-BFT 依赖 HotStuff-style safety foundation；本文不是 HotStuff 本身的基础定义来源。

## Path Materialization

| Path role | Ontology path | Action |
| --- | --- | --- |
| Primary | `blockchain-systems/consensus/permissioned-blockchain-consensus/sha256-a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122` | source note written and attached as source extension |
| Secondary | `distributed-systems/consensus/byzantine-fault-tolerance/sha256-a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122` | BFT source evidence added |
| Bridge | `distributed-systems/consensus/byzantine-fault-tolerance -> blockchain-systems/consensus/permissioned-blockchain-consensus` | bridge evidence created |

## Path Propagation

| Target note | Planned update | Materiality |
| --- | --- | --- |
| [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | add Stretch-BFT as BFT/multi-instance source extension; refine BFT vs CFT solution routes | material |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | add HotStuff-based multi-instance/adaptive BFT source extension | material |
| [[blockchain-consensus|Blockchain consensus]] | add representative source ref and route to permissioned BFT branch | light |
| [[consensus|Consensus]] | add representative source ref under BFT/multi-instance route | light |
| [[bft-consensus-to-permissioned-blockchains|BFT consensus -> permissioned blockchains]] | create bridge with source-backed transfer boundary | material |

## 吸收结果

- Source note: written as complete meta/source note.
- Knowledge handoff: ready for `nahida-knowledge-get`.
- Promotion decision: no new foundation knowledge node for Stretch-BFT; attach as source extension under BFT and permissioned blockchain consensus.
