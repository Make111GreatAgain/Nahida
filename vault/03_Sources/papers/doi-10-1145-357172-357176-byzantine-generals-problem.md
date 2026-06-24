---
id: "doi-10-1145-357172-357176"
title: "The Byzantine Generals Problem"
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
  - "p2-p6 interactive consistency and impossibility"
  - "p7-p9 oral-message algorithm OM(m)"
  - "p9-p12 signed-message algorithm SM(m)"
  - "p12-p16 missing communication paths"
  - "p16-p20 reliable systems and conclusion"
safe_for_absorption: true
canonical_url: "https://dl.acm.org/doi/10.1145/357172.357176"
doi: "10.1145/357172.357176"
arxiv_id: ""
venue: "ACM Transactions on Programming Languages and Systems"
year: "1982"
pdf_pages: 20
pdf_sha256: "800283221362ba1789ae997b4d719355be859a2861a6359573b46fd4fdcc839d"
local_pdf: "~/Desktop/paper/357172.357176.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/the-byzantine-generals-problem-800283221362-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "byzantine-fault-tolerance"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "byzantine-fault-tolerance"
primary_ontology_path: "distributed-systems/consensus/byzantine-fault-tolerance/doi-10-1145-357172-357176"
secondary_ontology_paths:
  - "distributed-systems/fault-tolerance/interactive-consistency/doi-10-1145-357172-357176"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
  directions:
    - "consensus"
  topics:
    - "byzantine-fault-tolerance"
    - "interactive-consistency"
domains:
  - "distributed-systems"
topics:
  - "byzantine-fault-tolerance"
  - "interactive-consistency"
aliases:
  - "Byzantine Generals"
  - "interactive consistency"
tags:
  - "nahida/source"
  - "paper"
  - "distributed-systems"
  - "consensus"
  - "byzantine-fault-tolerance"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "consensus"
  problem:
    - "byzantine-fault-tolerance"
    - "interactive-consistency"
  method_family:
    - "oral-message consensus"
    - "signed-message consensus"
  system_layer:
    - "fault-tolerant distributed systems"
  evaluation_context:
    - "theoretical impossibility and constructive algorithms"
  application:
    - "reliable replicated processors"
  bridge:
    - "distributed-systems/consensus -> reliable-computing"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-byzantine-generals-problem"
source_refs:
  - "doi:10.1145/357172.357176"
  - "pdf:~/Desktop/paper/357172.357176.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "distributed-systems -> consensus"
secondary_directions:
  - "distributed-systems -> fault-tolerance"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title"
  - "known DOI"
  - "abstract"
  - "full PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0001"
queue_status: "absorbed"
---

# The Byzantine Generals Problem

## 论文身份

- 标题: The Byzantine Generals Problem
- 作者: Leslie Lamport, Robert Shostak, Marshall Pease
- 机构: SRI International
- 会议/期刊: ACM Transactions on Programming Languages and Systems, Vol. 4, No. 3
- 年份: 1982
- DOI: `10.1145/357172.357176`
- 链接: https://dl.acm.org/doi/10.1145/357172.357176
- 本地 PDF: `~/Desktop/paper/357172.357176.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/the-byzantine-generals-problem-800283221362-pages.txt`
- 代码/数据: unknown
- License: PDF 内为 ACM permission/copyright 声明，未发现开放数据或代码。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 20
- 已覆盖章节/页码: p1 abstract/introduction, p2-p6 impossibility, p7-p9 OM(m), p9-p12 SM(m), p12-p16 missing paths, p16-p20 reliable systems/conclusion
- 已检查附录: 无附录
- 未覆盖章节/页码: references 只用于定位相关 foundational work，未逐条外部读取
- Extraction gaps: p8 图形页正文抽取弱，但上下文由 p7/p9 文本覆盖；其余核心正文可读
- 精读说明: 本文是分布式系统中 Byzantine fault tolerance 的经典基础论文，既给出 oral messages 下的下界和算法，也给出 signed messages 下的算法，并把问题解释为可靠计算系统中的 interactive consistency。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1 | 摘要与引入 | 把“组件向不同处理器给出冲突信息”的故障抽象成 Byzantine Generals Problem | 定义领域问题和应用背景 | 可作为 topic foundation |
| p2-p3 | Interactive consistency | 将全体将军一致行动拆成 IC1/IC2，并把原问题化约成 commander 向 lieutenants 发送一个值 | 定义 BFT 的一致性条件 | 也是可靠系统映射的接口 |
| p3-p6 | Impossibility results | oral messages 下 3 个将军无法容忍 1 个 traitor；一般化为少于 `3m + 1` 无法容忍 `m` 个 traitors | 核心下界 | 近似一致同样困难 |
| p6-p9 | Algorithm OM(m) | 在 A1-A3 假设下，递归转发 commander value，并用 majority 聚合 | 构造性算法和充分条件 | Theorem 1 |
| p9-p12 | Algorithm SM(m) | 引入 A4 signatures，将收到的 signed order 集合传播并用 choice 选值 | 说明签名如何改变容错边界 | Theorem 2 |
| p12-p16 | Missing communication paths | 将通信能力抽象为图，给出 OM 的 `3m`-regular 条件和 SM 在 loyal subgraph connectivity 下的结果 | 网络连通性视角 | Theorem 3/4 |
| p16-p19 | Reliable systems | 将 IC1/IC2 映射到冗余处理器对输入值的一致使用，讨论 A1-A4 在真实系统中的实现成本 | 将理论问题连接到系统设计 | 解释 timeout、clock sync、signature |
| p19-p20 | Conclusion | 算法时间路径长度和消息数昂贵，可靠性面对任意故障时本质上成本高 | 限制与工程边界 | 后续系统论文的重要背景 |

## 核心精读笔记

### 背景、动机与问题边界

本文的问题不是普通 crash failure，而是一个组件可能向不同接收方给出互相矛盾的信息。作者用 Byzantine army 的叙事把它抽象成一个 commander 向多个 lieutenants 传递命令的问题，并要求 loyal participants 在 traitors 任意行为下仍满足 interactive consistency。

问题的两个核心条件是 IC1 和 IC2。IC1 要求所有 loyal lieutenants 遵从同一个命令；IC2 要求如果 commander 是 loyal，那么所有 loyal lieutenants 都遵从 commander 发送的命令。对原始“每个将军都有一个观察值”的问题，作者把每个 general 轮流当 commander，发送“把我的观察值作为 `v(i)` 使用”的命令。这样，所有 loyal generals 最终对向量 `v(1)...v(n)` 使用相同的聚合方法。

本文不解决恶意输入值本身是否“正确”的问题。它只能保证 nonfaulty/loyal processors 对同一个输入值达成一致；如果输入设备本身故障，仍需要冗余输入源和更高层的容错设计。证据锚点: p1-p3, p16-p17。

### 模型、假设与定义

oral messages 模型下，作者显式提出 A1-A3: sent messages are delivered correctly, receiver knows sender identity, absence of a message can be detected。这些假设让 traitor 不能伪造其他人的发送身份，也不能隐形地删除两个 loyal parties 之间的消息，但 traitor 可以任意选择自己发出的消息内容。

signed messages 模型加入 A4: loyal general 的签名不能被伪造，消息内容修改可检测，且任何人都能验证签名。作者不假设 traitorous general 的签名不可被其他 traitors 伪造，因此模型允许 traitors 之间合谋。

真实系统中的 A3 依赖 timeout，而 timeout 又依赖最大消息生成/传输时间和处理器时钟同步误差上界。作者强调 clock synchronization 本身与 Byzantine Generals Problem 一样困难。证据锚点: p6, p9-p10, p17-p19。

### 方法、协议或系统机制

oral-message 算法 `OM(m)` 是递归式的。`OM(0)` 中 commander 直接向每个 lieutenant 发送值，未收到值则使用默认值 `RETREAT`。`OM(m)` 中 commander 先发值；每个 lieutenant 再作为 commander 运行 `OM(m-1)`，把自己从 commander 收到的值转发给其他 lieutenants；最后每个 lieutenant 对收到的值集合运行 `majority`。Theorem 1 证明当 generals 数量大于 `3m` 且 traitors 至多 `m` 时，`OM(m)` 满足 IC1/IC2。

signed-message 算法 `SM(m)` 维护每个 lieutenant 已收到的 properly signed orders 集合 `V_i`。commander 发送签名命令后，lieutenants 将收到的新 order 加上自己的签名继续传播，直到签名链长度达到 `m` 或没有新消息；最后对集合 `V_i` 使用 `choice` 函数。若 commander loyal，则 A4 防止其他 signed commander order 出现；若 commander traitor，则所有 loyal lieutenants 最终看到相同的 order 集合。Theorem 2 说明只要 traitors 至多 `m`，`SM(m)` 可解 Byzantine Generals Problem。

在通信图不完全连通时，oral-message 版本需要更强的图正则/多路径条件。`OM(m, p)` 在 `p >= 3m` 且图满足 p-regular 的条件下工作。signed-message 版本可弱化到 loyal generals 子图连通；Theorem 4 用 diameter `d` 表示 loyal 子图路径长度，证明 `SM(m+d-1)` 可以解决相应问题。证据锚点: p7-p16。

### 理论、证明或正确性论证

本文的下界证明核心是 indistinguishability。3 个 generals 中若只能容忍 1 个 traitor，Lieutenant 1 无法区分“commander loyal, Lieutenant 2 traitor”与“commander traitor, 向两个 lieutenants 发不同命令”的局部视图；同理 Lieutenant 2 会作出相反决定，违反 IC1。作者再用 simulation argument 把三将军不可能性推广到少于 `3m + 1` generals 无法容忍 `m` traitors。

`OM(m)` 的正确性使用 induction。Lemma 1 表明 loyal commander 时，只要有足够多 loyal lieutenants，majority 会恢复 commander value；Theorem 1 再处理 commander traitor 情况，由递归子调用保证每个 loyal lieutenant 对每个 `v_j` 得到相同值，所以最终 majority 相同。

`SM(m)` 的正确性依赖签名链传播。若 commander loyal，则 A4 阻止伪造第二个 commander-signed order。若 commander traitor，任一 loyal lieutenant 收到的 order 都会被直接或经由 loyal signer 传播给其他 loyal lieutenants，因此所有 loyal lieutenants 的 `V_i` 相同。证据锚点: p3-p6, p9-p12。

### 实验、评估或案例

本文是理论与系统设计论文，没有 empirical benchmark。系统应用部分用冗余 processor/majority voting 说明 interactive consistency 对可靠系统的必要性: nonfaulty processors 必须使用同一 input value，否则多数投票无法保证输出一致；如果 input unit nonfaulty，还要使用它提供的真实值。作者还讨论了通信线故障、身份识别、timeout、clock synchronization 和签名实现的工程代价。

评估 caveat 是成本很高。结论指出 `OM(m)` 和 `SM(m)` 都需要长度到 `m + 1` 的消息路径，消息数量可达到 `(n-1)(n-2)...(n-m-1)` 级别；在不完全连通图中路径长度可达 `m+d`。作者认为面对 arbitrary malfunctioning，高可靠性的代价难以避免。证据锚点: p16-p20。

### 作者结论与我的判断

作者明确给出三层结论: oral messages 下 `3m + 1` 是容忍 `m` Byzantine traitors 的基本边界；签名消息把问题从“多数无法区分”转化为“带证据的传播”，从而允许更少的 generals；真实系统要实现这些算法，需要满足通信、身份、timeout、时钟同步、签名等强假设。

我的判断: 这篇论文是 Nahida 中 `distributed-systems/consensus/byzantine-fault-tolerance` 的 foundation source。它适合作为 PBFT、Tendermint、HotStuff、DAG-BFT、区块链最终性和可靠 replicated processor 方向的父层概念入口，但它本身不是现代 BFT 性能或部分同步模型的完整说明。后续 PBFT、Paxos/Raft、DLS partial synchrony、FLP、HotStuff 等需要单独作为 source extensions 加入。

## 层级候选分类

- L1 Domain candidate: `distributed-systems`
- L2 Direction candidate: `consensus`
- L3 Topic/content cluster candidates: `byzantine-fault-tolerance`, `interactive-consistency`
- Ontology path: `distributed-systems/consensus/byzantine-fault-tolerance/doi-10-1145-357172-357176`
- 备选归属: `distributed-systems/fault-tolerance/interactive-consistency`
- 父级领域: distributed systems
- 学术子领域: fault-tolerant distributed algorithms, consensus
- 任务/问题: arbitrary/Byzantine faulty participants under agreement requirements
- 方法族: oral-message recursive majority, signed-message order propagation
- 模型/协议/算法族: `OM(m)`, `SM(m)`, interactive consistency
- 评测场景: theoretical lower bounds and constructive algorithms
- Benchmark/应用: reliable replicated processors, majority-voting reliable systems
- 别名: Byzantine Generals Problem, interactive consistency, Byzantine agreement seed
- 相邻方向: crash-fault consensus, state machine replication, reliable broadcast, clock synchronization
- 置信度: high
- 分类理由: 标题、摘要、定理、系统应用部分都明确指向分布式系统中的 Byzantine fault tolerance foundation。
- 分类状态: accepted
- 分类证据: p1-p3 definitions, p3-p6 impossibility, p7-p12 algorithms, p16-p20 reliable systems
- Taxonomy version: 1.0

## 一句话贡献

本文形式化了 Byzantine Generals Problem 和 interactive consistency，证明 oral messages 下容忍 `m` 个 traitors 需要至少 `3m + 1` 个 generals，并给出 oral-message 与 signed-message 两类构造性算法及其在可靠系统中的解释。

## 问题设定

系统中某些组件可能故障，并向不同接收者发送冲突信息。目标是在 traitors 任意行为下，让所有 loyal participants 对行动或输入值保持一致，并在 commander/input unit nonfaulty 时使用其真实值。问题不假设故障节点只停止响应，而允许 arbitrary behavior。

## 方法概览

### 组成部分

- `IC1`: all loyal lieutenants obey the same order。
- `IC2`: if commander is loyal, every loyal lieutenant obeys commander order。
- `OM(m)`: oral-message recursive relay plus majority。
- `SM(m)`: signed order dissemination plus choice over received orders。
- 通信图扩展: 完全图以外，用 p-regular graph 或 loyal subgraph connectivity 表达通信路径条件。

### 流程或协议

`OM(m)` 让 commander 的值逐层通过 lieutenants 递归传播，最终每个 lieutenant 对同一组 sender-indexed values 取 majority。`SM(m)` 让命令带 commander signature 和 lieutenant signature chain 传播，loyal participants 对完整可验证 order 集合取 choice。

### 关键定义、公式、算法或定理

- Oral messages 下 3 generals 不能容忍 1 traitor。
- 少于 `3m + 1` generals 不能容忍 `m` traitors。
- Theorem 1: `OM(m)` 在 generals 数量大于 `3m` 且 traitors 至多 `m` 时满足 IC1/IC2。
- Theorem 2: `SM(m)` 在 traitors 至多 `m` 时解决问题。
- Theorem 4: 若 loyal generals 子图 diameter 为 `d`，则修改后的 `SM(m+d-1)` 可解决问题。

### 假设条件

`OM(m)` 依赖 A1-A3，包括可靠投递、可识别发送者和可检测缺失消息。`SM(m)` 还依赖 A4，即 loyal 签名不可伪造且可验证。工程实现上 A3 需要时间上界和时钟同步，A4 需要随机/密码学签名机制。

## 创新点

- 新思想: 将冲突信息故障抽象为 interactive consistency，并给出严格不可能性边界。
- 对已有工作的扩展: 在 oral messages 与 signed messages 两类模型中分别给出可证明算法。
- 工程或实证贡献: 把问题映射到冗余处理器可靠系统，解释为什么多数投票前必须先达成输入一致。
- 依赖的 prior work: Pease, Shostak, Lamport 的 fault agreement 结果；Diffie-Hellman/RSA 等签名基础作为 A4 工程实现背景。

## 实验与结果

### 实验设置

无实验。本文用数学证明和系统假设分析作为主要证据。

### Baseline

隐含对比是 naive direct send/majority 和仅靠硬件共享输入线的方案。作者说明这些做法在 arbitrary faulty input 下不能保证 nonfaulty processors 看到同一值。

### 指标

理论指标包括可容忍 traitors 数量、最少 generals 数、消息路径长度、通信图 connectivity、消息数量级。

### 主要结果

- oral messages: 容忍 `m` traitors 需要至少 `3m + 1` generals，`OM(m)` 达到该条件。
- signed messages: A4 signatures 允许任意数量 generals 下容忍至多 `m` traitors，前提是签名传播能覆盖 loyal participants。
- incomplete graph: oral messages 需要较强的 regularity；signed messages 可依赖 loyal subgraph connectivity。

### 效率、成本或安全性

消息路径长度最高到 `m + 1`，不完全图中最高到 `m + d`。消息数量可达 descending product 量级。签名安全只可概率性保证或依赖密码学假设。

### 结果 caveat

本文没有现代 partial synchrony、asynchronous randomized consensus、state machine replication performance、网络攻击面或区块链经济安全模型。不能直接把 `SM(m)` 当作现代 BFT 协议的完整工程方案。

## 局限性

### 作者明确说明

- 算法消息和时间成本昂贵。
- timeout 需要最大延迟和时钟同步假设。
- 签名不可伪造在工程上只能通过概率或密码学难题近似实现。
- 仅保证 loyal processors 使用同一值，不保证 faulty input value 本身有意义。

### 基于证据的推断

本文的 foundation value 很高，但作为上层 synthesis 时需要与后续 PBFT、FLP、partial synchrony、HotStuff/Tendermint 等来源共同使用，否则会把早期模型误当作现代 BFT 协议全貌。

## 可复用思路

- 用 IC1/IC2 检查任意 BFT 协议的安全目标。
- 把不同 fault model 拆成 oral-message arbitrary behavior、signed evidence propagation、crash-fault timeout 等模型。
- 分析协议成本时分别记录 participant threshold、message path length、message count、connectivity 和 synchrony assumptions。
- 在区块链共识论文中，把“签名证据传播”与现代 quorum certificates / votes / commit certificates 建立桥接，但保留 partial synchrony 与 SM(m) 模型差异。

## 术语表

| Term | 说明 |
| --- | --- |
| Byzantine fault | 节点可任意错误，包括向不同对象发送冲突信息。 |
| Interactive consistency | loyal participants 对一个 sender value 使用同一值，并在 sender loyal 时使用真实 sender value。 |
| Oral messages | 消息内容完全由 sender 控制，traitor 可任意撒谎，但不能伪造身份。 |
| Signed messages | 消息带不可伪造、可验证签名，冲突命令可被传播为证据。 |
| `OM(m)` | oral-message recursive majority algorithm。 |
| `SM(m)` | signed-message order propagation algorithm。 |
| `RETREAT` | 未收到 commander value 时使用的默认值。 |

## Connections

- Extends/Seeds: [[byzantine-fault-tolerance|Byzantine fault tolerance]], [[byzantine-fault-tolerance|Interactive consistency]]
- Source extensions to read next: [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|Practical Byzantine Fault Tolerance]] is the next queue item.
- Adjacent directions: crash-fault consensus, state machine replication, reliable broadcast, clock synchronization, blockchain BFT finality.
- Bridge candidates: `distributed-systems/consensus/byzantine-fault-tolerance` -> `blockchain-systems/consensus/byzantine-fault-tolerance` as application/dependency.

## Evidence Table

| Claim | Evidence anchor | Claim type | Confidence |
| --- | --- | --- | --- |
| Byzantine fault captures conflicting information sent to different system parts. | p1 abstract/introduction | definition | high |
| IC1/IC2 define the lieutenant agreement and loyal commander validity requirements. | p2-p3 | definition | high |
| Oral messages cannot solve 3 generals with 1 traitor and generally need at least `3m + 1` generals for `m` traitors. | p3-p6 | theorem/lower bound | high |
| `OM(m)` solves under A1-A3 when there are more than `3m` generals and at most `m` traitors. | p6-p9, Theorem 1 | theorem/mechanism | high |
| Signed messages add A4 and make `SM(m)` solve the problem for at most `m` traitors. | p9-p12, Theorem 2 | theorem/mechanism | high |
| In incomplete communication graphs, signed-message algorithms can work under loyal-subgraph connectivity with diameter-dependent path length. | p12-p16, Theorem 4 | theorem/mechanism | high |
| Reliable replicated systems need interactive consistency before majority voting over outputs is meaningful. | p16-p17 | design principle | high |
| Timeouts for detecting absent messages require bounded delay and bounded clock skew. | p17-p18 | assumption/limitation | high |
| Byzantine solutions are inherently expensive in message path length and message count under arbitrary failures. | p19-p20 | limitation | high |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| 在 oral messages 模型下，容忍 m 个 Byzantine traitors 的 Byzantine Generals Problem 需要至少 3m+1 个 generals；Lamport-Shostak-Pease 的 OM(m) 在 A1-A3 假设下给出匹配的充分算法。 | `doi:10.1145/357172.357176#p3-p9` | folded_into_meta_note |
| 在 Lamport-Shostak-Pease 的模型中，不可伪造签名把 commander equivocation 变成可传播证据，使 SM(m) 能在 A4 假设下容忍至多 m 个 traitors，而不再受 oral-message 的 3m+1 下界约束。 | `doi:10.1145/357172.357176#p9-p12` | folded_into_meta_note |
| Lamport-Shostak-Pease 将 Byzantine Generals Problem 映射到可靠计算系统时指出，多数投票前必须先让所有 nonfaulty processors 使用同一 input value，并在 input unit nonfaulty 时使用其真实值，这正对应 IC1/IC2。 | `doi:10.1145/357172.357176#p16-p17` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `byzantine-oral-messages-three-m-plus-one`: oral messages require `3m + 1` participants to tolerate `m` Byzantine traitors, and `OM(m)` matches the sufficient side under A1-A3.
- `byzantine-signed-messages-removes-three-m-plus-one-bound`: signed messages change the problem by making equivocation transferable as evidence, allowing `SM(m)` under A4.
- `interactive-consistency-connects-bft-to-reliable-systems`: reliable replicated processors need IC1/IC2 on inputs before majority voting on outputs can work.

### Concepts to update

- `byzantine-fault-tolerance`: create `source_backed_seed` concept, foundation status `foundation_thin`.
- `interactive-consistency`: create seed concept because the paper makes it the formal bridge from Byzantine Generals to reliable systems.

### Missing foundations

- `distributed-systems` Domain Pack is seed-only.
- `consensus` Direction Pack is seed-only.
- Topic Pack `byzantine-fault-tolerance` has first primary paper but still needs PBFT, FLP/partial synchrony context, state machine replication, quorum certificates, and blockchain BFT sources.

### Review queue items

- Compare `Byzantine agreement`, `Byzantine fault tolerance`, `interactive consistency`, and `state machine replication` before merging aliases.
- Create bridge to `blockchain-systems/consensus` after at least one blockchain BFT source is deep-read.

## Synthesis Handoff

- Create topic synthesis: `09_Syntheses/Topics/byzantine-fault-tolerance-state-2026-06-11.md`.
- Refresh later after PBFT and Tendermint/Casper are absorbed.
- Domain/direction synthesis can remain `foundation_thin` after this first paper; do not overgeneralize from one 1982 source.
