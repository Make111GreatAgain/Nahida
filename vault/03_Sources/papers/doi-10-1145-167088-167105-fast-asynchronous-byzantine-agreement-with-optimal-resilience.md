---
id: "doi-10.1145-167088.167105"
title: "Fast Asynchronous Byzantine Agreement with Optimal Resilience"
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
canonical_url: "https://doi.org/10.1145/167088.167105"
doi: "10.1145/167088.167105"
arxiv_id: ""
venue: "STOC 1993"
year: "1993"
pdf_pages: 10
pdf_sha256: "140bbc9f1dff98514c41a02e9ad680c65e4c0640c1f8c2aee14563c07a099437"
local_pdf: "~/Desktop/paper/167088.167105.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/167088.167105-140bbc9f1dff-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-bft-consensus"
  - "byzantine-fault-tolerance"
  - "asynchronous-verifiable-secret-sharing"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-verifiable-secret-sharing"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/doi-10.1145-167088.167105"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/doi-10.1145-167088.167105"
path_update_status: "propagated"
domains:
  - "distributed-systems"
topics:
  - "asynchronous-bft-consensus"
  - "byzantine-fault-tolerance"
  - "asynchronous-verifiable-secret-sharing"
  - "global-coin"
aliases:
  - "Canetti Rabin optimal asynchronous Byzantine agreement"
  - "Optimal Asynchronous Byzantine Agreement"
  - "AVSS-backed global coin"
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
    - "asynchronous Byzantine agreement"
    - "asynchronous BFT consensus"
    - "Byzantine agreement with optimal resilience"
  method_family:
    - "asynchronous verifiable secret sharing"
    - "global coin from AVSS"
    - "randomized Byzantine agreement"
    - "information checking protocol"
    - "asynchronous broadcast"
  system_layer:
    - "agreement"
    - "distributed cryptographic primitive"
  evaluation_context:
    - "formal protocol and proof sketch"
    - "resilience threshold"
    - "expected time"
  application:
    - "fault-tolerant distributed computing"
    - "asynchronous BFT foundations"
  bridge:
    - "distributed BFT -> asynchronous blockchain consensus"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "PDF title page, abstract, model, AVSS sections, global-coin section, and BA section identify asynchronous Byzantine agreement as the primary problem"
  - "queue title was OCR noise from author/affiliation line and queue ontology was too blockchain-specific"
taxonomy_version: "1.0"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-canetti-rabin-optimal-async-ba"
source_refs:
  - "doi:10.1145/167088.167105"
  - "sha256:140bbc9f1dff98514c41a02e9ad680c65e4c0640c1f8c2aee14563c07a099437"
  - "pdf:~/Desktop/paper/167088.167105.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "distributed-systems -> consensus"
secondary_directions: []
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0078"
queue_status: "absorbed"
---

# Fast Asynchronous Byzantine Agreement with Optimal Resilience

## 论文身份

- 标题: Fast Asynchronous Byzantine Agreement with Optimal Resilience (Extended Abstract)
- 作者: Ran Canetti, Tal Rabin
- 机构: Technion; Hebrew University
- 会议/年份: 25th ACM Symposium on Theory of Computing (STOC 1993)
- DOI: 10.1145/167088.167105
- 链接: https://doi.org/10.1145/167088.167105
- 本地 PDF: `~/Desktop/paper/167088.167105.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/167088.167105-140bbc9f1dff-pages.txt`
- SHA-256: `140bbc9f1dff98514c41a02e9ad680c65e4c0640c1f8c2aee14563c07a099437`
- 关键词: `asynchronous Byzantine agreement`, `AVSS`, `global coin`, `information checking protocol`, `A-cast`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 10
- 已覆盖章节/页码: Abstract, §1 introduction, §2 definitions, §3 protocol overview, §4 tools, §5 A-RS, §6 AWSS, §7 AVSS, §8 global coin, §9 Byzantine agreement, references。
- 已检查附录: 本地 PDF 无 appendix；若要完整证明细节，需后续导入 technical report `Optimal Asynchronous Byzantine Agreement`。
- 未覆盖章节/页码: none material。
- Extraction gaps: OCR 把阈值括号和若干数学符号抽取得很粗糙；本 note 用正文语义统一为标准 `n >= 3t + 1` / `t < n/3` 表述。
- 精读说明: 队列标题来自作者/机构行的 OCR 噪声；真实标题和分类已更正。本 note 保留协议层细节，知识层只吸收 AVSS、global coin 与 async BA 的可复用结构。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §1 / pp. 42-43 | 问题与贡献 | 异步 Byzantine agreement 的最优 resilience 与快速终止问题；给出 `n >= 3t+1` 下常数期望时间的随机化 BA | high | 明确不是 blockchain paper。 |
| §2 / pp. 43-44 | 模型与定义 | 完全异步网络、可靠私有信道、dynamic Byzantine adversary、unbounded faulty players、BA 与 AVSS 定义 | high | 支撑假设边界。 |
| §3 / pp. 44-45 | 协议总览 | BA uses Vote + Global-Coin；Global-Coin uses AVSS；AVSS 由 A-RS -> AWSS -> AVSS 三层构造 | high | 核心层级结构。 |
| §4 / pp. 45-46 | 工具 | Information Checking Protocol (ICP) 与 Bracha A-cast | high | AVSS 的底层工具。 |
| §5 / pp. 46-48 | A-RS | Asynchronous Recoverable Sharing，用 ICP 和 A-cast 解决 reconstruction 时可用 share 集合不足的问题 | high | 解释为什么直接 VSS 不够。 |
| §6 / p. 48 | AWSS | Asynchronous Weak Secret Sharing，把 A-RS 提升为 dealer faulty 时输出固定值或 null | medium-high | 完整证明转 technical report。 |
| §7 / pp. 48-49 | AVSS | Two&Sum-AWSS 与 cut-and-choose 形成可验证、唯一 reconstructable 的 secret | high | 新 knowledge node 的主要证据。 |
| §8 / pp. 49-50 | Global coin | 用 AVSS shares 生成 common/global coin；每个 bit 对所有 honest players 有共同输出概率下界 | high | 连接 AVSS 与 randomized BA。 |
| §9 / pp. 50-51 | BA protocol | Vote 先做确定性多数过滤；无法确定时使用 global coin；常数期望轮数终止 | high | async BFT parent 的方法行。 |

## 一句话贡献

本文用 Asynchronous Verifiable Secret Sharing 构造 global coin，再把 global coin 接入 Vote-based 随机化 Byzantine agreement，在完全异步、私有信道、动态 Byzantine adversary 且 `n >= 3t+1` 的模型下，给出以 overwhelming probability 终止、条件于终止为常数期望时间的最优 resilience 异步 BA。

## 核心精读笔记

### 背景、问题与开放点

Byzantine Agreement 要求非故障参与者在 Byzantine faults 存在时决定同一值，并在所有 honest inputs 相同时保留该值。异步模型下，FLP 不可能性排除了确定性总终止；因此要用随机化来获得概率终止。论文聚焦的开放点是: 在完全异步网络里，能否同时达到最优 Byzantine resilience `t < n/3` 与快速终止，而不是退回指数期望时间或较低 resilience。

论文的贡献路径不是直接优化单个投票 round，而是补齐一个随机化异步 BA 需要的公共随机性层: 先构造 `t`-resilient AVSS，再由 AVSS 生成 global coin，最后把 global coin 用于 BA 的迭代式 Vote 协议。

### 模型与威胁假设

系统是 `n` 个 players 的完全异步网络，任意两点之间有可靠且私有的通信信道；消息延迟任意但有限，信道不要求保序。执行被看作 atomic steps 序列，scheduler 控制消息递送顺序；为了保持私有信道语义，scheduler 是 oblivious 的，只知道消息起点和终点。

fault model 是 dynamic Byzantine adversary，最多腐化 `t` 个 players，可在每个 atomic step 前选择额外腐化者；一旦腐化，内部状态交给 adversary，之后按 adversary 指令行动。faulty players 被允许有无限计算能力，因此协议不能依赖签名或 computational hardness 来约束 Byzantine 行为。

### AVSS 为什么是关键层

普通异步 secret sharing 的难点来自两个不同等待集合的交集。一个 honest player 在 sharing phase 和 reconstruction phase 各自最多只能等待 `n-t` 个响应。若 `n=3t+1`，两个集合的交集可能只有 `t+1` 个，其中 honest share 可能太少，直接用同步 VSS 或简单 Shamir sharing 不能保证所有 honest players 后续重构同一个 secret。

论文的解决路线是三层升级:

| 层 | 作用 | dealer faulty 时的保证 | 代表机制 |
| --- | --- | --- | --- |
| A-RS | Asynchronous Recoverable Sharing | reconstruction 后输出某个大小 `2t+1` 集合中的值或 null | ICP + A-cast 让必要 shares 在 reconstruction 时可用 |
| AWSS | Asynchronous Weak Secret Sharing | sharing 完成后固定一个值，reconstruction 输出该值或 null | 每个 player 用 A-RS 转分享 ICP 相关数据，并维护 ACC/ELG/FINAL 集 |
| AVSS | Asynchronous Verifiable Secret Sharing | sharing 完成后固定唯一 secret，reconstruction 输出该 secret | Two&Sum-AWSS + cut-and-choose 验证 shares define a unique secret |

AVSS 的知识价值在于它不是 Canetti-Rabin 论文的局部技巧，而是异步 BFT 和异步安全计算里“先安全地产生/固定一个 secret，再让所有 honest parties 后续可一致恢复”的基础原语。

### 工具: ICP 与 A-cast

Information Checking Protocol 在 unbounded adversary 下提供类似认证的保证: dealer 把 secret 交给 intermediary，receiver 之后可以在认证阶段接受或拒绝该 secret；若相关 parties honest，则接受值来自 dealer，且在认证前保持秘密性。它让 AVSS 不依赖数字签名或计算假设。

Bracha A-cast 是异步广播 primitive。它的 termination 比 BA 弱: sender honest 且 honest players 参与时会完成；若任一 honest player 完成，则所有 honest players 最终完成。论文用 A-cast 传播 `OK`、authenticated shares、suggested secrets、terminate 值等事件，从而把局部可见事实变成全体可见事实。

### 从 AVSS 到 global coin

Global-Coin 的目标是: 每个 player 有随机输入并输出 bit，对 `0/1` 中任一值，都至少以常数概率让所有 honest players 输出同一个值。这个性质足以让 BA 的 modified inputs 以常数概率聚合，从而得到常数期望轮数。

论文沿用 Feldman/Feldman-Micali 的思路: 每个 player 用 AVSS 分享多个随机 secrets；当足够多分配给某个 player 的 secrets 完成分享后，相关 identities 被 A-cast；随后 honest players 重构这些 secrets，并基于某个共同 core set 计算 coin 输出。AVSS 的作用是让 Byzantine dealer 或异步调度不能在 reconstruction 时让 honest players 看到互相不一致的随机性。

### Byzantine Agreement 协议骨架

BA 每轮有两个步骤:

1. `Vote`: players 用 A-cast 进行三轮输入/投票/re-vote 传播，试图识别 overwhelming majority、distinct majority 或 no distinct majority。若所有 honest players 输入相同值，则会识别 overwhelming majority；任意两个 honest players 不会识别两个不同值的 distinct majority。
2. `Global-Coin`: 若 Vote 没有给出 distinct majority，则把下一轮 modified input 设为 global coin 输出。若识别 overwhelming majority，则 A-cast terminate 值；收到 `t+1` 个 terminate A-casts 后输出并终止。

证明结构依赖三个里程碑: 每轮中 Global-Coin 完成则该轮常数时间结束；每轮以高概率完成；完成某轮后，所有 honest players 在下一轮拥有相同 modified input 的概率至少为常数。因此整体以常数期望轮数收敛。

### 成本、限制与迁移边界

Theorem 1/2 给出的结论是: 对任意误差参数 `epsilon > 0`，当 `n >= 3t+1` 时存在 `t`-resilient AVSS 和异步 BA；条件于 honest players 终止，运行时间为常数期望；每个 player 的计算资源为 `poly(n, log(1/epsilon))`。

限制也很明确: 这是 extended abstract，AWSS/AVSS/Global-Coin/BA 的若干完整证明转到 technical report；网络假设包含 private reliable channels；adversary 是 dynamic 且 unbounded；论文不讨论实现、WAN 性能、mempool、transaction dissemination 或区块链 validator economics。进入 blockchain 语境时，它只作为 async BFT/common-coin/AVSS foundation，通过 bridge 间接支持上层系统。

## 层级分类

| 层级 | 候选 | 证据 | 状态 |
| --- | --- | --- | --- |
| L1 domain | `distributed-systems` | Byzantine agreement, asynchronous distributed computing | accepted |
| L2 direction | `consensus` | BA/termination/correctness/resilience definitions | accepted |
| L3 topic | `asynchronous-bft-consensus` | asynchronous BA under Byzantine faults and `n >= 3t+1` | accepted |
| L4 method/concept | `asynchronous-verifiable-secret-sharing` | AVSS is the new reusable primitive used to build global coin | accepted as new knowledge node |
| Secondary bridge | `distributed-bft-to-asynchronous-blockchain-consensus` | async BFT foundations later support blockchain consensus, but paper itself is not blockchain-specific | bridge only |

## 与现有 Nahida 笔记的关系

| Existing note | Relation | Update needed | Reason |
| --- | --- | --- | --- |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | parent problem | add source extension and child concept | This paper supplies the AVSS-backed global coin route for fast optimal-resilience async BA |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | new method/concept | create | Needed to keep AVSS as reusable primitive instead of burying it inside a paper summary |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | ancestor problem | add source extension | It strengthens the BFT foundation with unbounded-adversary async BA at `t < n/3` |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | bridge | add transfer boundary | AVSS/global coin transfers as a liveness primitive; deployment, mempool and validator economics do not transfer |

## Knowledge Handoff

| Target knowledge node | Absorption instruction | Evidence | Status |
| --- | --- | --- | --- |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | Define AVSS as the reusable async secret-sharing primitive that gives agreement on a unique reconstructable secret and enables global coin construction | §2.3, §5-§7 | done |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | Add AVSS-backed global coin as a method route for optimal-resilience randomized async BA | Abstract, §3, §8-§9 | done |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | Add as historical/source-backed route showing randomized async BA can reach optimal resilience without computational assumptions under private channels | §1-§3, Theorem 2 | done |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | Add bridge evidence that common-coin/AVSS liveness machinery can transfer conceptually, but implementation and system assumptions remain application-specific | §8-§9 | done |

## Foundation candidate

- 是否为基础概念来源: yes。
- 适合提取的基础概念: `asynchronous-verifiable-secret-sharing`, `global coin`, `randomized asynchronous Byzantine agreement`, `information checking protocol`, `A-cast`。
- 本次新建节点: [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]]。
- 本次不新建节点: `global coin`, `A-cast`, `ICP` 暂作为 async BFT/AVSS 方法行；等后续 Bracha/Rabin/common-coin/VSS sources 补齐后再拆。

## Review Items

| Item | Reason | Status |
| --- | --- | --- |
| Queue title was OCR noise | Queue used `Ran Canetti Dept. of Computer Science` from affiliation line | fixed in queue metadata |
| Queue path was too blockchain-specific | Paper is a distributed algorithms foundation source, not a blockchain system paper | corrected to `distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing` |
| Need full technical report if proof-level audit is required | Extended abstract delegates details of AWSS/AVSS/Global-Coin proofs | queued as optional future source |

