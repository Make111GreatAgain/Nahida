---
id: "hal-00944019v2-signature-free-asynchronous-byzantine-consensus"
title: "Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
canonical_url: "https://inria.hal.science/hal-00944019v2"
doi: ""
arxiv_id: ""
hal_id: "hal-00944019v2"
venue: "ACM PODC 2014 / IRISA internal report PI 2016"
year: "2014"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-bft-consensus"
  - "byzantine-fault-tolerance"
  - "randomized-consensus"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
  directions:
    - "consensus"
  topics:
    - "asynchronous-bft-consensus"
    - "byzantine-fault-tolerance"
domains:
  - "distributed-systems"
topics:
  - "asynchronous BFT"
  - "binary consensus"
  - "common coin"
  - "BV-broadcast"
aliases:
  - "Mostefaoui Moumen Raynal asynchronous Byzantine consensus"
  - "Signature-free asynchronous Byzantine consensus"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "distributed-systems/consensus"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "consensus"
  problem:
    - "asynchronous Byzantine consensus"
    - "binary Byzantine consensus"
  method_family:
    - "common-coin randomized consensus"
    - "binary-value broadcast"
  system_layer: []
  evaluation_context:
    - "message complexity"
    - "round complexity"
    - "resilience threshold"
  application:
    - "fault-tolerant distributed computing"
  bridge: []
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "title, abstract, and Sections 2-4 identify asynchronous Byzantine binary consensus as the primary problem"
  - "no blockchain-specific content in the paper; blockchain queue path is too narrow"
taxonomy_version: "1.0"
local_pdf: "~/Desktop/paper/RR-2016-Consensus-optimal-V5.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/signature-free-asynchronous-byzantine-consensus-with-t-n-3-and-o-n2-messages-a3f252ab38bf-pages.txt"
pdf_sha256: "a3f252ab38bf5bb73e8b51552c524f079de7a2b6f89d50af46f739fb46561130"
page_count: 13
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-paper-intake-20260620-item-0034"
source_refs:
  - "hal:hal-00944019v2"
  - "sha256:a3f252ab38bf5bb73e8b51552c524f079de7a2b6f89d50af46f739fb46561130"
confidence: "high"
trust_tier: "primary"
---

# Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages

## 论文身份

- 标题: `Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages`
- 作者: Achour Mostefaoui, Moumen Hamouna, Michel Raynal
- 机构: LINA Universite de Nantes; Universite de Bejaia; Institut Universitaire de France / IRISA
- 会议/期刊: citation page says ACM PODC, July 2014, Paris, pp. 2-9; PDF also carries IRISA internal report `PI 2016 - February 2014`
- 年份: 2014
- DOI: unknown
- HAL: `hal-00944019v2`
- 链接: https://inria.hal.science/hal-00944019v2
- 本地 PDF: `~/Desktop/paper/RR-2016-Consensus-optimal-V5.pdf`
- Extracted text: `vault/02_Raw/pdf/extracted/signature-free-asynchronous-byzantine-consensus-with-t-n-3-and-o-n2-messages-a3f252ab38bf-pages.txt`
- SHA-256: `a3f252ab38bf5bb73e8b51552c524f079de7a2b6f89d50af46f739fb46561130`
- 关键词: `asynchronous Byzantine consensus`, `common coin`, `BV-broadcast`, `signature-free`, `binary consensus`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 13
- 已覆盖章节/页码: HAL/citation page, Abstract, §1-§5, Table 1, Figures 1-2, Lemmas 1-5, Theorems 1-3, references overview
- 已检查附录: 本地文本中无 appendix
- 未覆盖章节/页码: none material
- Extraction gaps: 少量 ligature/空格噪声，`O(n2)` 在正文中表示 `O(n^2)`；不影响算法和证明重建。
- 精读说明: 本 note 保留算法阈值、抽象性质、证明结构和成本模型，后续查询不需要重新打开 PDF。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Page 1 | HAL/citation metadata | HAL ID、PODC 2014 citation、CC BY 4.0 | high | 队列 year `2023` 来自 PDF CreationDate，已更正为 2014。 |
| Page 2 / Abstract | 贡献摘要 | `t < n/3`、signature-free、expected 4 rounds、每轮 O(n^2) messages、每消息 round number + 1 bit、依赖 common coin 与 BV-broadcast | high | 核心身份与贡献。 |
| §1 | 背景与相关工作 | 异步 Byzantine consensus、FLP、不可能性、common coin、Table 1 对比 | high | 明确 primary path 是 async BFT foundation。 |
| §2 | 计算模型 | `BZ_AS_{n,t}`、可靠异步点对点网络、Byzantine process、`n > 3t`、common coin enriched model | high | 支撑假设边界。 |
| §3 | BV-broadcast | 四个性质、Figure 1 echo 算法、Theorem 1、成本 | high | paper 的核心抽象。 |
| §4 | 共识算法 | Figure 2 三阶段 round-based consensus、common coin、Lemma 1-5、Theorem 2-3、成本 | high | 核心算法与正确性。 |
| §5 | 结论 | 重申 optimal resilience、signature-free、O(n^2)、2/3 steps、expected 4 rounds、simplicity | medium | 贡献总结。 |

## 核心精读笔记

### 背景、动机与问题边界

- 背景脉络: 异步分布式系统中进程无法即时观测全局状态，asynchrony 与 failures 会让慢进程和故障进程难以区分。Consensus 是 fault-tolerant distributed computing 的核心 agreement abstraction。
- 现有方法不足: 异步 Byzantine consensus 不能在纯异步模型中确定性解决；需要随机化、message schedule assumptions、failure detectors、同步假设或输入限制。已有 common-coin binary Byzantine consensus 算法往往在 resilience、message complexity、签名依赖和通信步骤之间取舍。
- 本文问题定义: 在 `t < n/3` 的最优 Byzantine resilience 下，构造一个 signature-free、每轮 `O(n^2)` messages、每消息只携带 round number 和 1 bit、期望 4 轮决定的 asynchronous binary Byzantine consensus 算法。
- 明确不解决的问题: 不实现 common coin；不解决纯异步 deterministic consensus；不直接给 multi-valued consensus，只指出可基于 binary consensus 构造；不讨论区块链应用。
- 证据锚点: Abstract, §1 Related work, §2 model, §4.1 common coin。

### 模型、假设与定义

- 系统: 有 `n > 1` 个异步顺序进程 `Π = {p1, ..., pn}`。每个进程以未知速度运行。
- 网络: 异步可靠 point-to-point network；消息最终到达，不丢失、不重复、不修改、不伪造；每对进程有双向通道，接收方可识别发送者。
- Byzantine fault model: 最多 `t` 个进程任意偏离协议，可崩溃、发送不同消息给不同进程、串谋污染计算；但不能 impersonate another process。
- 基本模型: `BZ_AS_{n,t}[∅]`；限制模型 `BZ_AS_{n,t}[n > 3t]`；加入 common coin 后为 `BZ_AS_{n,t}[n > 3t, CC]`。
- Common coin: Rabin 风格 oracle，每次调用 `random()` 返回 bit；所有正确进程第 `r` 次调用得到相同随机 bit `b_r`。它必须由进程合作计算，以避免 Byzantine processes 提前知道随机序列并操纵 schedule。
- Consensus properties: BC-Validity、BC-Agreement、BC-One-shot、BC-Termination with probability 1。
- 证据锚点: §2, §4.1。

### BV-broadcast 抽象

BV-broadcast 是本文设计的 binary-value broadcast abstraction。它不是“某个 sender 广播了什么”，而是“哪些 binary values 可以被正确进程接受”。每个正确进程本地有只增集合 `bin_values_i`。

| 性质 | 含义 | 作用 |
| --- | --- | --- |
| BV-Obligation | 若至少 `t+1` 个正确进程 BV-broadcast 同一值 `v`，则每个正确进程最终把 `v` 加入 `bin_values_i` | 保证足够多正确支持的值传播到所有正确进程 |
| BV-Justification | 若正确进程的 `bin_values_i` 中出现 `v`，则 `v` 必须被某个正确进程 BV-broadcast 过 | 排除仅 Byzantine processes 伪造的值 |
| BV-Uniformity | 若某正确进程加入 `v`，最终所有正确进程都会加入 `v` | 形成正确进程间的 value-level convergence |
| BV-Termination | 每个正确进程最终 `bin_values_i` 非空 | 保证上层共识 round 不会卡在空集合 |

Figure 1 算法:

1. 进程 BV-broadcast `B_VAL(v)`。
2. 若从至少 `t+1` 个不同进程收到 `B_VAL(v)` 且自己未转发过，则向所有进程转发一次 `B_VAL(v)`。
3. 若从至少 `2t+1` 个不同进程收到 `B_VAL(v)`，则把 `v` 加入 `bin_values_i`。

关键直觉: `t+1` 阈值保证至少有一个正确进程支持该值；`2t+1` 阈值保证其中至少 `t+1` 个是正确进程，从而可通过可靠网络和 echo 传播到所有正确进程。

Theorem 1: Figure 1 在 `BZ_AS_{n,t}[t < n/3]` 中实现 BV-broadcast。成本是每个 BV-broadcast instance 1 或 2 communication steps；正确进程同值时发送 `c n` messages，否则 `2 c n` messages，其中 `c >= n-t`；消息内容除 tag 外只携带 1 bit。

### 随机化 Byzantine binary consensus 算法

Figure 2 的每轮共识有三阶段:

1. Phase 1: 进程把当前 estimate `est_i` 通过 `BV_broadcast EST[r_i](est_i)` 广播，并等待 `bin_values_i[r_i]` 非空。
2. Phase 2: 进程广播 `AUX[r_i](w)`，其中 `w` 来自自己的 `bin_values_i[r_i]`；随后等待来自 `n-t` 个不同进程的 AUX 消息，且这些 AUX value set `values_i` 是 `bin_values_i[r_i]` 的子集。这一步丢弃只由 Byzantine processes 产生的 value。
3. Phase 3: 调用 common coin 得到 `s`。若 `values_i = {v}`，且 `v = s`，则决定 `v`，并保持/更新 estimate 为 `v`；若 `values_i = {0,1}`，则把 estimate 更新为 common coin `s`。

算法运行 forever；`decide()` 不停止进程。这让已决定进程继续参与后续 round，便于证明所有正确进程最终保持同一 estimate。

### 正确性证明结构

| 结果 | 内容 | 证明直觉 | 证据锚点 |
| --- | --- | --- | --- |
| Lemma 1 | 若某轮开始所有正确进程 estimate 相同，则之后不会改变 | BV-Justification 确保 `bin_values` 只含该值，line 09 保持它 | §4.3 |
| Lemma 2 | 两个正确进程若在同一轮各自看到 singleton `values`，则 singleton 值相同 | `n-t` AUX quorum 与至少 `t+1` 正确发送者相交，正确进程不会发送不同 AUX | §4.3 |
| Lemma 3 | 决定值由正确进程提出 | 初始 round 经 BV-Justification 和 AUX subset 检查；后续 estimate 都继承正确提出值 | §4.3 |
| Lemma 4 | 两个正确进程不会决定不同值 | 首个决定轮若有人决定 `v`，其他 singleton 也只能是 `v`；非决定者若看到 `{0,1}` 会采用同一 common coin | §4.3 |
| Lemma 5 | 每个正确进程以概率 1 决定 | wait 不会永久阻塞；若不同进程走 line 09/10，common coin 以 1/2 概率让 estimates 聚合；最终概率趋 1 | §4.3 |
| Theorem 2 | Figure 2 解决 randomized binary consensus | Validity/Agreement/One-shot/Termination 分别由 Lemmas 3/4/line 08/5 得出 | §4.3 |
| Theorem 3 | expected decision time 为 4 rounds | 估计值聚合期望 2 轮；common coin 命中决定值期望 2 轮 | §4.3 |

### 成本与对比

- Table 1 对比 Rabin、Berman-Garay、Friedman-Mostefaoui-Raynal、Bracha、Srikanth-Toueg、Toueg、Canetti-Rabin、Cachin-Kursawe-Shoup 等 binary Byzantine consensus 算法。
- 本文组合了三点: `t < n/3` 最优 resilience、每轮 `O(n^2)` message complexity、无需 signatures。
- 每轮 communication steps: 若正确进程同 estimate，BV-broadcast 只需 1 step，加一次 AUX broadcast，共 2 steps；若不同，则 BV-broadcast 可需 2 steps，加 AUX，共 3 steps。
- 若正确进程初始提议同值，期望 2 轮决定，总消息约 `2 c n`。
- 若提议不同，期望 4 轮决定，每轮正确进程消息约 `4 c n`。
- 每个 EST/AUX/B_VAL 消息除 round number 外只携带 1 bit；期望 bit complexity 为 `O(n^2)`。
- 证据锚点: Table 1, §3.3 cost, §4.3 cost。

## 层级候选分类

- L1 Domain candidate: `distributed-systems`
- L2 Direction candidate: `consensus`
- L3 Topic/content cluster candidates: `asynchronous-bft-consensus`, `byzantine-fault-tolerance`, `randomized-consensus`, `broadcast-abstractions`
- Ontology path: `distributed-systems/consensus/asynchronous-bft-consensus`
- 备选归属: queue 给了 `blockchain-systems/consensus/consensus-foundations`，但本文没有 blockchain-specific content；可作为 blockchain BFT 的基础背景通过 bridge 间接引用，不作为 primary/secondary source path。
- 父级领域: distributed systems
- 学术子领域: fault-tolerant distributed computing, Byzantine consensus
- 任务/问题: asynchronous binary Byzantine consensus with optimal resilience and low message complexity。
- 方法族: common-coin randomized consensus, BV-broadcast, signature-free BFT。
- 评测场景: resilience threshold、message complexity、bit complexity、round/step complexity、signature dependence。
- 别名: Mostefaoui-Hamouna-Raynal 2014 async BFT, BV-broadcast consensus。
- 置信度: high
- 分类理由: title/abstract/§2-§4 全部是 distributed asynchronous Byzantine consensus。
- 分类状态: corrected_from_queue

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | distributed systems | §1 distributed computing and agreement abstractions | high | existing domain |
| Research background | asynchronous systems, FLP, Byzantine failures, common coin | §1-§2 | high | consensus/BFT background |
| Research problem | randomized asynchronous Byzantine binary consensus | Abstract, §4 | high | existing async BFT node |
| Foundation concepts | BFT, asynchronous consensus, common coin, broadcast abstraction, BV-broadcast | §2-§4 | high | sections/source extension; no new node yet |
| Method family | signature-free common-coin BFT with BV-broadcast | Figure 1/2 | high | source extension |
| Application/evaluation context | theoretical distributed algorithms | Table 1, cost sections | high | consensus foundation |
| Artifact/source instance | this PODC/HAL paper | local PDF | high | representative source |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `distributed-systems/consensus/asynchronous-bft-consensus`
- 它能帮助未来哪些问题少读 source notes: “什么是 common-coin async BFT”、“BV-broadcast 有什么用”、“为什么 t<n/3/O(n^2)/signature-free 可以同时成立”、“Mostefaoui async BFT 的证明路线是什么”。
- 哪些内容应留在 source note: Figure 1/2 的逐行机制、Lemma 1-5 证明细节、Table 1 全部对比。
- 哪些上层节点过薄、缺失或需要 foundation_pack: asynchronous BFT 的 common coin/Bracha RBC/HoneyBadger/BEAT 等 foundation 仍需更多 source。
- 哪些候选只是别名/query key/watch term: BV-broadcast、common coin、signature-free async BFT 先作为 query key/section，不单独建节点。

## 一句话贡献

本文给出一个基于 BV-broadcast 和 Rabin common coin 的 signature-free asynchronous binary Byzantine consensus 算法，在 `t < n/3` 下达到每轮 `O(n^2)` 消息、期望 4 轮决定且每消息只携带 1 bit。

## 问题设定

在异步 Byzantine message-passing 系统中，纯确定性 consensus 受 FLP 不可能性影响；若加入 common coin，目标是在最优 Byzantine fault threshold `t < n/3` 下实现随机化 binary consensus，同时避免 signatures 和 `O(n^3)` 级消息成本。

## 方法概览

### 组成部分

- `BV-broadcast`: value-oriented binary broadcast abstraction。
- `common coin`: 所有正确进程同一轮得到相同随机 bit。
- `EST` message: 通过 BV-broadcast 传播 estimate。
- `AUX` message: 广播从 `bin_values` 中取得的 value，并用 `n-t` quorum 过滤 Byzantine-only values。
- `values_i`: line 05 得到的候选值集合。

### 流程或协议

1. 每轮 BV-broadcast 当前 estimate。
2. 等待 `bin_values` 非空。
3. 广播一个来自 `bin_values` 的 AUX value。
4. 等待 `n-t` 个 AUX，且 AUX value set 是当前 `bin_values` 子集。
5. 调 common coin。
6. 若只剩一个 value 且与 coin 相同，则决定；若只剩一个 value 但 coin 不同，则保留该 value；若两个 value 都存在，则采用 coin。

### 关键定义、公式、算法或定理

- Byzantine threshold: `n > 3t`。
- BV-broadcast echo threshold: `t+1` 转发，`2t+1` 交付。
- AUX wait threshold: `n-t` distinct processes。
- Expected rounds: 4。
- Message complexity: `O(n^2)` per round。
- Bit complexity expectation: `O(n^2)`，正文写为 `O(n^2 r log r)` for `r` rounds and expected `O(n^2)`。

### 假设条件

- Reliable asynchronous point-to-point channels。
- Byzantine processes cannot impersonate other processes。
- Common coin abstraction exists and cannot be predicted/exploited by Byzantine scheduler before it is computed。
- Binary consensus only; multi-valued consensus requires reduction。

## 创新点

- 新思想: 用 value-oriented BV-broadcast 削弱 Byzantine processes 的影响，排除只由 Byzantine processes 提供的值。
- 对已有工作的扩展: 展示 `O(n^2)` messages、无需 signatures、`t<n/3` 最优 resilience 可以同时成立。
- 工程或实证贡献: 这是理论算法，不提供实现 benchmark；工程价值在于 message/bit/step complexity 与设计简洁性。
- 依赖的 prior work: Rabin common coin、FLP impossibility、Bracha/Toueg/Canetti-Rabin/Cachin-Kursawe-Shoup 等 Byzantine agreement work。

## 实验与结果

### 实验设置

无实验。本文是理论分布式算法论文。

### Baseline

Table 1 比较了已有 asynchronous Byzantine binary consensus 算法在 resilience、签名需求、messages/round、bits/message、steps/round 上的取舍。

### 指标

- resilience threshold `t < n/3`
- signature-free or signature-based
- messages per round
- bits per message
- communication steps per round
- expected rounds to decide

### 主要结果

- Optimal resilience: `t < n/3`。
- Signature-free。
- `O(n^2)` messages per round。
- 每消息除 round number 外只带 1 bit。
- 2 或 3 communication steps per round。
- expected 4 rounds to decide。

### 结果 caveat

Common coin 实现被抽象掉，实际部署成本取决于 common coin construction；论文没有工程 benchmark，也不讨论 adaptive adversary 或 cryptographic threshold setup。

## 局限性

### 作者明确说明

- 需要 common coin 作为额外计算能力。
- 只处理 binary consensus；multi-valued consensus 通过已知 reduction 实现。
- `decide()` 不停止进程，算法描述让进程继续执行 round。

### 基于证据的推断

- 该算法适合当作 async BFT 的 foundation source，而不是区块链协议实例。
- BV-broadcast 值得作为 async BFT node 的重要方法 section；是否拆为独立 knowledge node 需要更多 broadcast/ACS/HoneyBadger source。

## 可复用思路

- 在 Byzantine consensus 中，把 “value validity” 和 “sender identity” 分离，可以构造更轻的 broadcast abstraction。
- `t+1` 与 `2t+1` 阈值配合是 BFT 中过滤 Byzantine-only values 的核心模板。
- Common coin 的作用不是直接决定，而是在分歧 round 中让所有正确进程以常数概率聚合到同一 estimate。
- 评价 BFT 算法时要同时看 resilience、message complexity、bit complexity、签名/密码学依赖、steps per round 和 expected decision rounds。

## 术语表

| Term | 中文说明 | 本文用途 |
| --- | --- | --- |
| Asynchronous Byzantine consensus | 异步 Byzantine 共识 | 无消息延迟上界、进程可 Byzantine 的 consensus problem |
| Binary consensus | 二值共识 | 每个正确进程提出 0/1 并决定 0/1 |
| Common coin | 公共随机币 | 每轮所有正确进程得到相同随机 bit |
| BV-broadcast | Binary-value broadcast | 面向值而非 sender 的二值广播抽象 |
| Signature-free | 无签名 | 协议不依赖数字签名消息认证 |
| Optimal resilience | 最优容错阈值 | Byzantine consensus 中 `t < n/3` |

## 连接

- 相关论文: Rabin randomized Byzantine generals, Bracha asynchronous Byzantine agreement, Cachin-Kursawe-Shoup async BA, FLP impossibility。
- 相关仓库: none
- 相关 Knowledge nodes:
  - [[04_Knowledge/distributed-systems/consensus|Consensus]]
  - [[04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance|Byzantine Fault Tolerance]]
  - [[04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus|Asynchronous BFT Consensus]]
- 相关 Bridges: none
- Bridge 候选: 未来可把 async BFT foundation 与 blockchain asynchronous consensus bridge 更新；本 source 本身不含 blockchain 应用，不直接建桥。

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |
| Asynchronous BFT consensus | knowledge_node | 全文 | active | update existing node |
| Byzantine fault tolerance | parent problem | Byzantine model and `t<n/3` | active_seed | add representative source |
| BV-broadcast | method section | §3/Figure 1 | section | 不建独立节点，等待更多 broadcast sources |
| Common coin | foundation gap | §4.1 references Rabin/common coin implementation | queued | 后续 foundation source/search |
| Blockchain consensus foundation | alternative queue path | no blockchain content | rejected_primary | 不作为 primary path |

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 本文算法在 `t < n/3` 下最优 resilience | author claim/proof | Abstract, §4.2, Theorem 2 | high | BFT threshold |
| BV-broadcast 排除仅 Byzantine processes 广播的值 | theorem | §3.1-§3.3, Theorem 1 | high | 核心抽象 |
| 算法无需 signatures 且每轮 `O(n^2)` messages | author claim/cost | Abstract, Table 1, §4.3 cost | high | 对比 Table 1 |
| Expected decision time is 4 rounds | theorem | Theorem 3 | high | 依赖 common coin |
| Common coin 是额外模型能力，不由本文实现 | model boundary | §4.1 | high | 不可忽视的前提 |

## 知识交接

- 留在本文元笔记的证据: Figure 1/2 逐行算法、BV-broadcast 四性质、Lemma/Theorem 证明、Table 1 对比。
- 待更新 Knowledge node:
  - `distributed-systems/consensus/asynchronous-bft-consensus`
  - `distributed-systems/consensus/byzantine-fault-tolerance`
  - `distributed-systems/consensus`
- 作为哪些 Knowledge node 的 source extension: async BFT 主节点；BFT/consensus 父节点代表 source。
- 需要补的 foundation knowledge/source: Rabin common coin、Bracha reliable broadcast/asynchronous BA、HoneyBadger/ACS、BEAT。
- 待新增或复核 domain/direction/problem: no new durable node now。
- Bridge 候选: async BFT to blockchain asynchronous consensus, only after endpoint source needs refresh。
- Watchlist 词条: BV-broadcast, common coin, signature-free asynchronous Byzantine consensus, binary consensus。
- Review queue: queue year and blockchain path corrected; DOI unknown。

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Asynchronous BFT consensus | foundation/topic knowledge | 更新现有 async BFT node | 把本文算法名建成新领域 | 全文 |
| BV-broadcast | method_section_candidate | 放入 async BFT 方法族与 source note | 只凭一篇 paper 直接拆新 foundation node | §3 |
| Common coin | foundation_gap | 作为 async BFT 背景/缺口，后续补 source | 假装本文已完整实现 common coin | §4.1 |
| This paper's algorithm | representative_source_extension | 代表性 foundation source | 上升成单独方向 | Figure 2 |

## Knowledge 综合交接

- 应创建 Knowledge node: none
- 应刷新 Knowledge synthesis section: async BFT 的方法族、代表 sources、当前综合和 gaps；BFT/consensus 的 representative source rows。
- 应标记过期: none
- 无需更新的理由: 无 blockchain-specific bridge；BV-broadcast 暂不拆节点。
- 建议 node kind: source extension under existing problem node。

## 处理日志

| Date | Run ID | Action | Result |
| --- | --- | --- | --- |
| 2026-06-20 | nahida-paper-intake-20260620-item-0034 | deep-read `RR-2016-Consensus-optimal-V5.pdf` and corrected queue classification | source note ready for absorption |
