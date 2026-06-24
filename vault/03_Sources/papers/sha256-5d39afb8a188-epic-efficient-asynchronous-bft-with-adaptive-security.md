---
id: "sha256-5d39afb8a188"
title: "EPIC: Efficient Asynchronous BFT with Adaptive Security"
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
  - "p1-p3 abstract, introduction, contribution list, related work, static vs adaptive corruption motivation"
  - "p3-p5 system/threat model, asynchronous timing model, threshold PRF, RBC, ABA definitions"
  - "p5-p6 ACS workflow, HoneyBadgerBFT/BEAT transaction selection and threshold-cryptography bottlenecks"
  - "p6-p8 adaptive-security design: LM-LJY threshold PRF, HYB transaction selection, Cobalt ABA, DKG"
  - "p8-p9 DKG sketch, LM-LJY threshold PRF and common coin protocol"
  - "p9-p12 implementation and evaluation: protocol variants, LAN/WAN setup, ABA/crypto/transaction-selection/scalability results, DKG cost"
  - "p12-p15 conclusion and references"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown"
year: "2020"
pdf_pages: 15
pdf_sha256: "5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
local_pdf: "~/Desktop/paper/EPIC.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/epic-5d39afb8a188-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-bft-consensus"
  - "byzantine-fault-tolerance"
  - "adaptive-bft-security"
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
primary_ontology_path: "blockchain-systems/consensus/asynchronous-bft-consensus/sha256-5d39afb8a188"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/sha256-5d39afb8a188"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "consensus"
  topics:
    - "asynchronous-bft-consensus"
    - "byzantine-fault-tolerance"
    - "adaptive-bft-security"
    - "asynchronous-common-subset"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "asynchronous-bft-consensus"
  - "adaptive-security"
  - "asynchronous-common-subset"
  - "Cobalt ABA"
  - "LM-LJY threshold PRF"
  - "hybrid transaction selection"
  - "distributed key generation"
aliases:
  - "EPIC"
  - "Efficient Asynchronous BFT with Adaptive Security"
  - "HYB transaction selection"
  - "adaptive asynchronous BFT"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "consensus"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "consensus"
  problem:
    - "adaptive corruption in asynchronous BFT"
    - "MHR ABA liveness issue under cryptographic common coin"
    - "trusted-dealer setup in HoneyBadgerBFT and BEAT"
    - "threshold encryption cost and censorship prevention"
  method_family:
    - "asynchronous common subset"
    - "Cobalt ABA"
    - "adaptively secure threshold PRF"
    - "distributed key generation"
    - "hybrid random/FIFO transaction selection"
  system_layer:
    - "RBC"
    - "ABA"
    - "common coin"
    - "transaction selection"
    - "key setup"
    - "state machine replication"
  evaluation_context:
    - "Python implementation"
    - "Amazon EC2 LAN and WAN"
    - "five continents"
    - "n = 3f + 1 replicas"
    - "250-byte transactions"
    - "20-epoch and 100-epoch experiments"
  application:
    - "permissioned blockchains"
    - "hybrid blockchains"
    - "asynchronous BFT SMR"
  bridge:
    - "distributed BFT -> asynchronous blockchain consensus"
created: "2026-06-19"
updated: "2026-06-19"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260619-epic-adaptive-asynchronous-bft"
source_refs:
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "pdf:~/Desktop/paper/EPIC.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> consensus"
secondary_directions:
  - "distributed-systems -> consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "PDF title page and abstract"
  - "Sections I-IX"
  - "Figures 1-14 and Tables I-II"
  - "local PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0020"
queue_status: "absorbed"
---

# EPIC: Efficient Asynchronous BFT with Adaptive Security

## 论文身份

- 标题: EPIC: Efficient Asynchronous BFT with Adaptive Security
- 作者: Chao Liu, Sisi Duan, Haibin Zhang
- 机构: UMBC
- 会议/期刊: unknown in PDF
- 年份: 2020 from PDF metadata / queue inventory
- DOI: unknown
- arXiv: unknown
- 链接: unknown
- 本地 PDF: `~/Desktop/paper/EPIC.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/epic-5d39afb8a188-pages.txt`
- 代码: unknown in PDF
- 数据: unknown in PDF
- License: unknown in PDF

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 15
- 已覆盖章节/页码: p1-p15 full text
- 已检查附录: 无独立 appendix；p13-p15 references 已检查。
- 未覆盖章节/页码: 无
- Extraction gaps: 抽取文本存在 ligature、断词和图表坐标噪声；协议框图、表格、主要评测数字和正文结论可读。Venue/DOI 不在 PDF metadata 或 title page 中，保持 unknown。
- 精读说明: 这篇是 ACS/HoneyBadgerBFT/BEAT 系列的 adaptive-security source extension。吸收时不要把它误读成 MyTumbler 一类 ordering redesign；EPIC 保持 ACS 两阶段框架，主要替换 ABA/common coin/key setup/transaction selection。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §I / p1-p3 | 动机与贡献 | HoneyBadgerBFT/BEAT 是 static security；EPIC 追求 adaptive security、DKG、去 threshold encryption，并评估 ABA/crypto bottlenecks | 贡献定位 | 摘要给出 8,000-12,500 tx/sec、4,000-6,300 tx/sec 等量级 |
| §II / p3 | 相关工作 | partial synchrony BFT、ABA、ACS/HoneyBadger/BEAT、local-coin protocols、hybrid async BFT、asynchronous MPC | 背景边界 | 说明 EPIC 位于 common-coin ACS 分支 |
| §III / p3-p4 | 系统与威胁模型 | `f <= floor((n-1)/3)` Byzantine；computationally bounded adaptive adversary；pure async during protocol；DKG setup assumes synchrony | 模型边界 | Liveness probabilistic due to FLP |
| §IV / p4-p5 | primitives | Threshold PRF with FGen/Eva/Vrf/FCom；RBC properties；ABA properties；common coin in ABA rounds | 组件定义 | EPIC compatible with any RBC, implements AVID |
| §V.A / p5 | ACS workflow | Epoch = RBC phase + n parallel ABA instances；deliver union of proposals with ABA value 1; abstain from 0 until `n-f` delivered | 协议骨架 | 与 HoneyBadgerBFT/BEAT shared framework |
| §V.B / p5-p6 | corruption model taxonomy | Common-coin asynchronous BFT systems use statically secure threshold crypto; local-coin alternatives are adaptive but less scalable | 分类贡献 | Table-like conceptual taxonomy |
| §V.C / p6 | adaptive-security approach | LM-LJY threshold PRF, HYB random/FIFO selection, Cobalt ABA, DKG for PRF | 核心设计 | 避免 adaptive threshold encryption |
| §VI / p6-p9 | EPIC design | Figure 2 EPIC algorithm; HYB parameters `mu`/`delta`; Figure 3 Cobalt ABA; Figure 4 DKG; Figures 5-6 common coin | 机制细节 | EPIC waits for all n ABA instances; expected `O(log N)` runtime |
| §VII / p8-p9 | implementation | 13,000 lines Python; four variants; BN256; modified Charm + relic C++ | 实现证据 | 表 I 定义 BEAT/BEAT-Cobalt/EPIC-MHR/EPIC |
| §VIII / p9-p12 | evaluation | EC2 LAN/WAN, five continents, t2.medium, `n=3f+1`, 250-byte tx; latency/throughput/scalability/DKG | 实证证据 | Figures 7-14, Tables I-II |
| §IX / p12 | conclusion | EPIC achieves adaptive security and decentralized key distribution with moderate overhead, but bottlenecks vary with scale | 总结 | 不声称大规模下接近 static-security protocols |
| References / p12-p15 | 依赖来源 | HoneyBadgerBFT, BEAT, Cobalt, LM-LJY, CKS, MHR, AVID, FLP/DLS 等 | 后续补源 | 多个 foundation refs 未直接吸收 |

## 一句话贡献

EPIC 在 HoneyBadgerBFT/BEAT 的 ACS 框架内，用 Cobalt ABA + LM-LJY adaptively secure threshold PRF + synchronous DKG + random/FIFO hybrid transaction selection，把高性能 asynchronous BFT 从 static-security threshold-crypto setup 推进到 adaptive-security 版本，同时用四个实现变体定位 Cobalt ABA、adaptive PRF 和 HYB selection 的性能代价。

## 核心精读笔记

### 背景、动机与问题边界

论文的基本观察是: asynchronous BFT 对 timing/performance/DoS 攻击天然更鲁棒，因为 safety 和 liveness 不依赖同步网络窗口；但现代高性能异步协议 HoneyBadgerBFT 和 BEAT 主要是 static security。static corruption 要求 adversary 在协议开始前固定腐化集合；adaptive corruption 则允许 adversary 根据已看到的消息和已腐化状态随时选择新节点。论文引用经典分离结果指出 static secure protocol 不必然 adaptive secure。证据锚点: Abstract, §I p1-p2。

HoneyBadgerBFT/BEAT 的 static-security 根因在 threshold cryptography: 它们使用 threshold PRF/common coin 和 threshold encryption，且 key generation 依赖 trusted dealer。EPIC 不试图重做整个异步 BFT 架构，而是保留 ACS framework，替换会影响 adaptive security 的组件: common coin、ABA、transaction selection 和 key generation。证据锚点: §I p1-p3, §V.C p6。

这篇的边界也很清楚: 正常协议执行是 purely asynchronous；但 distributed key setup 是 one-time synchronous phase。作者认为 setup 阶段可以使用足够大的 timeout 且 DKG 可容忍最多 `n/2` Byzantine faulty replicas；不过这意味着 EPIC 的“全异步”不包含密钥生成阶段。证据锚点: §III p4, §VI p8。

### 系统模型和基础组件

EPIC 的 BFT/SMR 模型允许 `f <= floor((n-1)/3)` Byzantine replicas，由 computationally bounded adaptive adversary 协调。Correctness 包括 Agreement、Total order 和 Liveness: 若 operation 提交给 `n-f` correct replicas，所有 correct replicas eventually deliver。由于 FLP，异步 BFT 必须依赖 randomization，因此 liveness 是 probabilistic。证据锚点: §III p3-p4。

构件层包括 threshold PRF、RBC 和 ABA。Threshold PRF 提供 `FGen`、`Eva`、`Vrf`、`FCom`，要求 `t-1` corrupt servers 下 PRF value unpredictable，并依赖 uniqueness property。RBC 采用 Agreement/Totality/Validity/Integrity；EPIC 可兼容任何 RBC，实现里用 AVID broadcast，和 HoneyBadgerBFT/BEAT 一致。ABA 是每个实例就 bit 达成 agreement，轮内使用 common coin。证据锚点: §IV p4-p5。

### ACS workflow: EPIC 保留 HoneyBadgerBFT/BEAT 的骨架

ACS 中每个 epoch 有 RBC phase 和 ABA phase。每个 replica 从 transaction buffer 选择一批交易，通过自己的 RBC instance 广播；随后运行 `n` 个并行 ABA instances，第 `i` 个 ABA 决定 replica `p_i` 的 RBC-delivered proposal 是否进入本 epoch 输出。节点在本地 RBC-deliver 某 proposal 后给对应 ABA 输入 1；直到本地已有 `n-f` 个 ABA delivered 1，才给剩余还未输入的 ABA instances 输入 0。最终 deliver 所有 ABA 输出 1 的 proposals 的 union。证据锚点: §V.A p5, Figure 1, §VI p6-p7, Figure 2。

这个框架解释了 EPIC 和 MyTumbler 的差异。MyTumbler 改的是 ordering/agreement 连接范式，避免 fixed-slot 强制推进；EPIC 则仍在 epoch/ACS 框架中，每轮要等所有 `n` 个 ABA instances 终止。论文说每个 ABA round 以 `1/2` 概率终止，EPIC 等所有 ABA instances，因此运行时间期望为 `O(log N)`。证据锚点: §VI p7。

### Adaptive security strategy: 三个替换而不是一个银弹

EPIC 的 adaptive-security 设计有三根支柱。

第一，用 Loss-Moran / Libert-Joye-Yung (LM-LJY) adaptively secure threshold PRF 做 common coin。LM-LJY threshold PRF 的 signature verification 需要 4 次 pairing，比 HoneyBadgerBFT 的 threshold PRF 多一倍，也明显贵于 BEAT 的 pairing-free PRF。EPIC 的评测因此专门比较 EPIC 和 BEAT-Cobalt，隔离 adaptive PRF 的代价。证据锚点: §V.C p6, §VI p8-p9, Figure 5-6。

第二，不使用 adaptively secure threshold encryption。作者认为最有效率的 adaptive threshold encryption 依赖 composite-order bilinear group，代价太高。EPIC 改用 HYB transaction selection: 大多数 epochs 选 random plaintext transactions，周期性切到 FIFO selection。Random selection 保持高吞吐，FIFO fraction 保证某笔交易不会被长期 censorship，从而避免 threshold encryption 的 encrypt-then-decrypt 路径。证据锚点: §V.C p6, §VI p7。

第三，用 Cobalt ABA 替换 MHR ABA。MHR ABA 在 HoneyBadgerBFT/BEAT 中高效，但在现有 cryptographic common coin 实例化下存在 liveness issue: adversary/network scheduler 可以学习 coin 并安排消息顺序让 correct nodes 带着不一致值进入下一轮。Cobalt ABA 增加一轮 `conf` 广播，让节点在 query coin 前确认 aux values，从而修复此问题；代价是每个 round 多一步，WAN 延迟更明显。证据锚点: §I p2, §VI p7-p8, Figure 3。

### Transaction selection: HYB 的吞吐/延迟/审查权衡

FIFO selection 容易保证 liveness/censorship-resilience，但多个 replicas 往往选到重叠交易，系统吞吐下降。HoneyBadgerBFT/BEAT 用 random selection 提高 proposals 之间的 disjointness，再用 threshold encryption 避免 adversary 根据明文交易审查某笔交易。EPIC 的 HYB 选择不加密: `mu` 个 epochs 做 random selection，再 `delta` 个 epochs 做 FIFO selection，切换策略对所有 replicas deterministic。证据锚点: §VI p7。

HYB 的 trade-off 是显式参数化的。`mu` 远大于 `delta` 时偏吞吐；`mu` 较小时偏延迟/更频繁 FIFO fairness。评测固定 `delta=1`，Table II 在 `f=1,b=1000` 下显示 `mu` 从 2 增到 100 时 LAN/WAN throughput 都提高，例如 WAN 从约 1147 tx/sec 增到约 1708 tx/sec。这个结果说明 FIFO fraction 确实有吞吐成本，但也提供了不依赖 threshold encryption 的 censorship bound。证据锚点: §VIII p11, Table II。

### DKG 和 common coin

EPIC 只使用一个 threshold cryptographic primitive: LM-LJY threshold PRF。只要 threshold PRF 的 key generation 是 decentralized，EPIC 就不需要 HoneyBadgerBFT/BEAT 那样的 trusted dealer。论文使用 Libert-Joye-Yung 的 DKG 方案，并用 Bracha broadcast 实例化其中假设的 broadcast channel。Figure 4 给出 `(f+1,n)` threshold PRF 的 FGen: 节点广播 polynomial commitments，互发 shares，投诉无效或缺失 shares，排除 disqualified replicas，再本地计算 `pk/vk/sk_i`。证据锚点: §VI p8, Figure 4。

这个 DKG 是 synchronous one-time event，而不是异步协议的一部分。作者选择 synchronous DKG 的理由是实现简单且 setup 可设大 timeout；同时他们指出该 DKG 可容忍 `n/2` Byzantine faults，而 asynchronous key generation 只能容忍 `n/3`。评测 Figure 14 显示 DKG 相比 centralized key generation 成本高很多；例如 `(10,19)` LAN 下 failure-free 约 12.21 秒，有一个 malicious replica 时约 13.75 秒，而 centralized 约 1.54 秒。证据锚点: §VI p8, §VIII p12, Figure 14。

Common coin 协议用 session id `sid = (epoch, round, ABA instance)` 作为 PRF input；各 replica 广播 PRF share，收集 `f+1` valid shares 后用 `FCom` 合成 coin。LM-LJY 的 adaptive security 依赖 SXDH assumption。证据锚点: §VI p8-p9, Figure 5-6。

### 四个实现变体和瓶颈定位

论文实现 4 个协议变体，而不仅是 EPIC 单点对比:

| 变体 | ABA | Common coin | Transaction selection | Liveness | Adaptive security |
| --- | --- | --- | --- | --- | --- |
| BEAT | MHR | CKS | ETD | No | No |
| BEAT-Cobalt | Cobalt | CKS | ETD | Yes | No |
| EPIC-MHR | MHR | LM-LJY | HYB | No | Yes |
| EPIC | Cobalt | LM-LJY | HYB | Yes | Yes |

这个设计使论文能分别看 Cobalt ABA extra step、adaptive threshold PRF、HYB transaction selection 和 scale 的影响。实现是 13,000 行 Python，其中 DKG 900 行、evaluation 1,200 行；使用 BN256 curve、修改 Charm 包装 relic C++。证据锚点: §VII p8-p9, Table I。

### 评测设置和主要结果

评测在 Amazon EC2 上进行，最多 91 台 t2.medium VMs，分 LAN 和五大洲 WAN，`n=3f+1`，交易大小 250 bytes。Latency-only 实验让每个 replica 提案单交易；throughput 实验调整每 replica batch size `b` 直到 peak/stable。作者强调 throughput 按实际 delivered transactions 计算，重叠交易只计一次，以便真实观察 transaction selection 的影响。证据锚点: §VIII p9-p10。

MHR vs Cobalt: 所有实验中 MHR 变体都快于 Cobalt 变体。LAN 中 extra step 代价小但可见；WAN 中更明显。Figure 8/9 报告 `f=1` 时 LAN 下 BEAT-Cobalt throughput 仅比 BEAT 低 0.02%，EPIC 比 EPIC-MHR 低 1%；WAN 下对应低 2% 和 8%。Figure 7 报告 latency 上 BEAT-Cobalt 比 BEAT 高 16%-34%，EPIC 比 EPIC-MHR 高 18%-31%。证据锚点: §VIII p10。

Adaptive vs static: EPIC 相对 BEAT-Cobalt 的吞吐更低、延迟更高，主要来自 LM-LJY 的更重 pairing cryptography。`f=1` WAN 下 EPIC latency 高 13%、throughput 低 5%；LAN 下 EPIC peak throughput 比 BEAT-Cobalt 低 29%。这意味着 adaptive security 的代价在网络延迟占主导的 WAN 小规模场景较温和，在计算更显著的 LAN 或大规模场景更重。证据锚点: §VIII p10-p11, Figure 10。

Scalability: 作者区分 total throughput 和 average throughput per replica。随着 `f` 增大，average throughput per replica 下降；total throughput 会先增后降，因为并发 proposer 数增加但单 replica 吞吐下降。WAN 下 `b=5000`，EPIC 相对 BEAT-Cobalt 的 average throughput per replica 在 `f=1,2,5` 时分别低约 2%、5%、21%；`f=30` 时 peak throughput 低 68%。EPIC total throughput 在 `f=5` 达 peak，而 BEAT-Cobalt 在 `f=15` peak。证据锚点: §VIII p11-p12, Figure 11-13。

摘要还给出高层结果: 当 replicas 少于 46 时，EPIC throughput stable，peak throughput 8,000-12,500 tx/sec；规模更大时，throughput 约 4,000-6,300 tx/sec。正文另说即使 31 replicas，EPIC 对 250-byte transactions 仍可达 10,000 tx/sec。证据锚点: Abstract p1, §I p3。

### 作者结论与我的判断

作者结论是 EPIC 证明 adaptively secure asynchronous BFT 可以 practical，但不是免费午餐。它修复了 MHR/common-coin liveness issue，消除了 trusted dealer 和 threshold encryption，但引入 Cobalt ABA extra step、LM-LJY pairing overhead、HYB selection 参数权衡，以及 one-time synchronous DKG。证据锚点: §IX p12。

我的吸收判断: EPIC 对 Nahida 的最大价值不是“最快异步 BFT”，而是把 async BFT 的基础坐标补齐为四维比较: timing assumption、corruption model、cryptographic setup、transaction-selection/censorship strategy。它应放在 [[asynchronous-bft-consensus|Asynchronous BFT consensus]] 的 `adaptive-security / ACS` 分支，并和 [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|MyTumbler]] 形成互补: MyTumbler 优化 fixed-slot/workload behavior，EPIC 优化 adaptive-security and setup assumptions。

## 层级候选分类

| 层级 | 候选 | 证据 | 状态 |
| --- | --- | --- | --- |
| L1 domain | `blockchain-systems` | abstract/introduction 明确 permissioned/hybrid blockchain applications；评测面向 BFT SMR | accepted |
| L2 direction | `consensus` | BFT, atomic broadcast, ACS, RBC, ABA, total order, SMR | accepted |
| L3 topic | `asynchronous-bft-consensus` | fully asynchronous protocol, ACS, common coin, Cobalt ABA | accepted |
| Secondary topic | `byzantine-fault-tolerance` | `f <= floor((n-1)/3)`, Byzantine failures, SMR correctness | accepted as foundation extension |
| Candidate topic | `adaptive-bft-security` | adaptive corruption, LM-LJY PRF, DKG, static/adaptive taxonomy | accepted as source-backed seed; needs more sources |
| Candidate topic | `asynchronous-common-subset` | RBC + n ABA instances workflow, transaction union, HoneyBadger/BEAT lineage | source-backed seed |

## 与现有 Nahida 笔记的关系

- 扩展 [[asynchronous-bft-consensus|Asynchronous BFT consensus]]: 从 MyTumbler 的 flexible advancement branch 补到 ACS/common coin/adaptive-security branch。
- 扩展 [[byzantine-fault-tolerance|Byzantine fault tolerance]]: 增加 adaptive corruption/security-model 维度，区别于 classical PBFT practical source 和 Cobalt open-network governance source。
- 与 [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt]] 相连: EPIC 使用 Cobalt ABA 来修复 MHR/common-coin liveness issue，但 EPIC 不是 Cobalt 的 open-network UNL governance model。
- 与 [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] 互补: MyTumbler 处理 fixed-slot/workload/adaptive advancement，EPIC 处理 adaptive security/trusted setup/threshold encryption。

## Evidence Table

| Claim / observation | Source location | Claim type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| HoneyBadgerBFT/BEAT achieve static, not adaptive, security because their threshold crypto is statically secure and dealer-based | §I p1-p2, §V.B p5-p6 | motivation/security taxonomy | high | explicit |
| EPIC combines LM-LJY threshold PRF, Cobalt ABA, HYB transaction selection, and DKG to obtain adaptive security | §V.C p6, §VI p6-p9 | protocol construction | high | main contribution |
| HYB avoids threshold encryption by mixing random plaintext selection with periodic FIFO selection | §V.C p6, §VI p7 | mechanism | high | random/FIFO parameters `mu/delta` |
| Cobalt ABA fixes MHR/common-coin liveness issue at one extra step per ABA round | §I p2, §VI p7-p8, Figure 3 | protocol component | high | liveness issue from cryptographic coin scheduling |
| EPIC's DKG removes trusted dealer but is a synchronous one-time setup and costs much more than centralized key generation | §III p4, §VI p8, §VIII p12, Figure 14 | setup/limitation | high | DKG tolerates up to `n/2` Byzantine in setup |
| EPIC has modest overhead vs BEAT-Cobalt at small WAN scale but overhead grows with `f` | §VIII p10-p12, Figures 10-13 | empirical result | high | 5% lower throughput at `f=1` WAN, 68% lower peak throughput at `f=30` |
| HYB `mu` controls latency/throughput trade-off; larger `mu` improves throughput when `delta=1` | §VIII p11, Table II | empirical result | high | LAN/WAN throughput rises as `mu` grows |
| EPIC is still an ACS epoch protocol and waits for all ABA instances | §VI p6-p7, Figure 2 | protocol boundary | high | not a flexible-advancement/timestamp-ordering redesign |

## 创新点

- 新思想: 将 adaptively secure threshold PRF + Cobalt ABA + HYB transaction selection 组合成 practical adaptive asynchronous BFT，而不是直接使用昂贵 adaptive threshold encryption。
- 对已有工作的扩展: 沿用 HoneyBadgerBFT/BEAT 的 ACS/RBC/ABA structure，但修正 MHR liveness issue 和 trusted-dealer/static-security boundary。
- 工程或实证贡献: 实现四个可比变体，隔离 ABA、common coin、transaction selection、scale 和 DKG 的实际开销。
- 依赖的 prior work: Ben-Or et al. ACS, AVID RBC, MHR ABA, Cobalt ABA, CKS/LM-LJY threshold PRF, HoneyBadgerBFT, BEAT。

## 局限性

### 作者明确说明

- DKG setup 阶段是 synchronous one-time event，不是 fully asynchronous setup。
- LM-LJY threshold PRF 明显比 BEAT 的 pairing-free PRF 更贵。
- Cobalt ABA 每轮多一步，WAN 中延迟影响更明显。
- HYB 的 FIFO fraction 降低吞吐，`mu/delta` 是需要调的 trade-off。
- 大规模时 EPIC 相对 BEAT-Cobalt 的 throughput penalty 明显变大。

### 基于证据的推断

- EPIC 的 adaptive security 结论依赖 LM-LJY PRF 和 DKG 安全模型；论文没有给出完整形式化系统 proof，只给出组件组合和评测。
- 论文没有给出生产部署中的 parameter tuning、client behavior、mempool DoS、reconfiguration 或 key-rotation 机制。
- Venue/DOI 不在本地 PDF 中，引用时应使用 sha256 identity 或用户后续补充的 bibliographic metadata。

## 可复用思路

- 把 BFT 协议比较拆成四个轴: timing model、corruption model、setup model、transaction-selection/censorship model。
- 若 threshold encryption 的 adaptive-secure 版本过贵，可用 deterministic periodic FIFO path 作为 liveness/censorship fallback。
- 对异步协议评测要同时报告 total throughput 和 average throughput per replica，否则大规模并发 proposer 会掩盖单节点性能下降。
- 对 common-coin ABA 不只看 expected rounds，还要检查 cryptographic coin 与 scheduler 的交互是否满足协议假设。

## 术语表

| Term | 解释 | Source |
| --- | --- | --- |
| Adaptive corruption | adversary 可根据执行中看到的信息随时选择腐化节点 | §I, §III |
| ACS | Asynchronous Common Subset，由 RBC + n ABA instances 组成，输出至少 `n-f` proposals 的 union | §V.A |
| ETD | encrypt-then-decrypt transaction selection, HoneyBadgerBFT/BEAT 用 threshold encryption 防 censorship | §VI |
| HYB | EPIC 的 hybrid transaction selection: 多数 epochs random plaintext，周期性 FIFO | §VI |
| LM-LJY threshold PRF | Loss-Moran / Libert-Joye-Yung adaptively secure threshold PRF，用于 common coin | §V.C, §VI |
| Cobalt ABA | 通过额外 conf step 修复 MHR + cryptographic common coin liveness issue 的 ABA | §VI |
| DKG | Distributed key generation；EPIC 用 Bracha broadcast 实例化 PRF key setup | §VI |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| EPIC's adaptive-security overhead is modest at small WAN scale but grows with network size; compared with BEAT-Cobalt, EPIC has about 2%, 5%, and 21% lower per-replica throughput at f=1,2,5 and about 68% lower peak throughput at f=30. | `sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e#p10-p12` | folded_into_meta_note |
| EPIC uses Cobalt ABA instead of MHR ABA because MHR is not live with existing cryptographic common coins; Cobalt adds a confirmation step that restores liveness but increases latency, especially in WAN settings. | `sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e#p2,p7-p8,p10` | folded_into_meta_note |
| EPIC obtains adaptively secure asynchronous BFT by combining Cobalt ABA, the LM-LJY adaptively secure threshold PRF for common coins, HYB transaction selection, and distributed key generation within the ACS framework. | `sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e#p6-p9` | folded_into_meta_note |
| EPIC removes the trusted dealer for its threshold PRF by instantiating distributed key generation with Bracha broadcast, but the key setup is a synchronous one-time phase and is much slower than centralized key generation. | `sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e#p4,p8,p12` | folded_into_meta_note |
| EPIC's four-variant evaluation separates the performance impact of ABA choice, common-coin cryptography, transaction selection, and network size by comparing BEAT, BEAT-Cobalt, EPIC-MHR, and EPIC. | `sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e#p8-p12` | folded_into_meta_note |
| EPIC replaces threshold-encrypted random transaction selection with a deterministic hybrid of random plaintext epochs and periodic FIFO epochs, trading some throughput for censorship-resilience without threshold encryption. | `sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e#p6-p7` | folded_into_meta_note |

## Knowledge Handoff

- 可吸收的来源内判断:
  - `epic-combines-cobalt-aba-and-lm-ljy-prf-for-adaptive-async-bft`
  - `epic-hyb-selection-avoids-threshold-encryption-with-censorship-tradeoff`
  - `epic-cobalt-aba-fixes-mhr-common-coin-liveness-at-extra-step-cost`
  - `epic-dkg-removes-trusted-dealer-but-keeps-synchronous-setup`
  - `epic-adaptive-security-overhead-grows-with-network-size`
  - `epic-evaluation-separates-aba-crypto-selection-and-scale-bottlenecks`
- Concepts to create/update:
  - Update [[asynchronous-bft-consensus|Asynchronous BFT consensus]]
  - Create [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC]]
  - Create [[asynchronous-bft-consensus|Asynchronous common subset]]
  - Create [[asynchronous-bft-consensus|Adaptive security in BFT]]
  - Create [[asynchronous-bft-consensus|Hybrid transaction selection]]
- Maps/syntheses:
  - Update [[asynchronous-bft-consensus|Asynchronous BFT consensus]] topic map with EPIC as second direct source.
  - Refresh topic synthesis for `asynchronous-bft-consensus` on 2026-06-19.
  - Update BFT topic/map and distributed-BFT-to-asynchronous-blockchain-consensus bridge with adaptive-security dimension.

## Synthesis Handoff

- Create or refresh `vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md`.
- Existing `byzantine-fault-tolerance` synthesis can be lightly amended: EPIC adds adaptive corruption/static-vs-adaptive dimension but does not replace missing FLP/Bracha/MHR/HoneyBadger direct sources.
- Keep foundation status `foundation_thin`: HoneyBadgerBFT, BEAT, MHR ABA, Bracha RBC, FLP, DKG/common coin sources still need direct absorption.
