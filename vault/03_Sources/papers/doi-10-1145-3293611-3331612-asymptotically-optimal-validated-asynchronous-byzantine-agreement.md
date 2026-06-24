---
id: "doi-10.1145-3293611.3331612"
title: "Asymptotically Optimal Validated Asynchronous Byzantine Agreement"
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
  - "p1 abstract, introduction, VABA motivation, prior Cachin et al. bound and theorem statement"
  - "p2-p3 model, cryptographic setup, threshold signatures, threshold coin-tossing, VABA definition"
  - "p3-p4 provable-broadcast abstraction and proposal-promotion structure"
  - "p4-p6 leader-election, view phases, key/lock/commit rules, safety intuition"
  - "p6-p7 progress and complexity analysis"
  - "p7-p10 discussion, appendix properties, references"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1145/3293611.3331612"
doi: "10.1145/3293611.3331612"
arxiv_id: ""
venue: "PODC 2019"
year: "2019"
pdf_pages: 10
pdf_sha256: "c3b1a5d44fc7f2d5be55c05e57d4d9fc79e3d574b7a3b580a3b29e9729bbd991"
local_pdf: "~/Desktop/paper/VABA-PODC2019.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/asymptotically-optimal-validated-asynchronous-byzantine-agreement-c3b1a5d44fc7-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-bft-consensus"
  - "validated-asynchronous-byzantine-agreement"
  - "byzantine-fault-tolerance"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "validated-asynchronous-byzantine-agreement"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement/doi-10.1145-3293611.3331612"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/doi-10.1145-3293611.3331612"
  - "blockchain-systems/consensus/doi-10.1145-3293611.3331612"
path_update_status: "propagated"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "asynchronous-bft-consensus"
  - "validated-asynchronous-byzantine-agreement"
  - "byzantine-fault-tolerance"
  - "atomic-broadcast"
  - "state-machine-replication"
aliases:
  - "VABA"
  - "validated asynchronous Byzantine agreement"
  - "multi-valued asynchronous Byzantine agreement"
  - "external validity"
tags:
  - "nahida/source"
  - "paper"
  - "distributed-systems"
  - "consensus"
direction_facets:
  parent_domain:
    - "distributed-systems"
    - "blockchain-systems"
  subdomain:
    - "consensus"
  problem:
    - "validated asynchronous Byzantine agreement"
    - "externally valid multi-valued asynchronous agreement"
    - "atomic broadcast and state machine replication primitive"
    - "adaptive asynchronous Byzantine adversary"
  method_family:
    - "provable broadcast"
    - "proposal promotion"
    - "threshold-signature common coin"
    - "leader election after proposal completion"
    - "key-lock-commit view change"
  system_layer:
    - "agreement"
    - "atomic broadcast"
    - "state machine replication"
  evaluation_context:
    - "formal protocol and complexity proof"
    - "authenticated asynchronous model"
  application:
    - "fault-tolerant state machine replication"
    - "asynchronous atomic broadcast"
    - "blockchain consensus foundations"
  bridge:
    - "distributed BFT -> asynchronous blockchain consensus"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement"
source_refs:
  - "doi:10.1145/3293611.3331612"
  - "sha256:c3b1a5d44fc7f2d5be55c05e57d4d9fc79e3d574b7a3b580a3b29e9729bbd991"
  - "pdf:~/Desktop/paper/VABA-PODC2019.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "distributed-systems -> consensus"
secondary_directions:
  - "blockchain-systems -> consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "PDF title page, DOI, abstract, theorem statement"
  - "Model, Definitions 1-4, protocol overview, complexity analysis"
  - "local PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0036"
queue_status: "absorbed"
---

# Asymptotically Optimal Validated Asynchronous Byzantine Agreement

## 论文身份

- 标题: Asymptotically Optimal Validated Asynchronous Byzantine Agreement
- 作者: Ittai Abraham, Dahlia Malkhi, Alexander Spiegelman
- 机构: VMware Research
- 会议/年份: PODC '19, July 29-August 2, 2019, Toronto, Canada
- DOI: 10.1145/3293611.3331612
- 链接: https://doi.org/10.1145/3293611.3331612
- 本地 PDF: `~/Desktop/paper/VABA-PODC2019.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/asymptotically-optimal-validated-asynchronous-byzantine-agreement-c3b1a5d44fc7-pages.txt`
- 代码: unknown in PDF
- License: ACM copyright/license notice on p1

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 10
- 已覆盖章节/页码: p1-p10 full text
- 已检查附录: Appendix A 的 provable-broadcast properties 已检查；references 已检查。
- 未覆盖章节/页码: 无
- Extraction gaps: PDF 是 10 页会议版，部分证明被压缩；算法伪码和性质表述可读，但完整证明细节需要后续若有 extended/full version 再补。
- 精读说明: 这篇应作为 `validated asynchronous Byzantine agreement` 问题节点的代表 source，而不是直接作为 blockchain consensus 节点。它提供的是异步 BFT/atomic broadcast/SMR 的基础原语和复杂度边界。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 动机与贡献 | VABA 是 Atomic Broadcast 和 fault-tolerant SMR 的基础；Cachin et al. 2001 以来的 open problem 是 authenticated adaptive setting 下同时达到 optimal resilience、expected constant time、expected quadratic communication | 贡献定位 | 明确声称 expected `O(n^2)` word communication 和 expected `O(1)` running time |
| §2 / p2-p3 | 模型和加密原语 | 异步消息传递，adaptive adversary corrupts up to `f < n/3`，trusted dealer setup，random oracle，threshold signatures，threshold coin-tossing | 模型边界 | 对 honest state privacy 和 adversary polynomial computation 有 crypto-model 假设 |
| §2 / p3 | VABA 定义 | Validity, Quality, Agreement, Termination, Efficiency | 问题定义 | Quality 至少 `1/2` 选择 honest party 提案，避免总是选择默认 externally-valid 值 |
| §3.1 / p3-p4 | Provable-Broadcast | sender 通过 externally valid value/proof 收集 `n-f` signature shares 形成 broadcast proof | 子协议 | proof implies `f+1` honest parties delivered；不能为两个不同值都证明 |
| §3.2 / p4-p5 | Proposal-Promotion | 每个 view 有 n 个 leader-specific instances；四步 Provable-Broadcast 推动 key/lock/commit | 核心结构 | completion proof 来自第 4 次 PB threshold signature |
| §3.3 / p5 | Leader-Election | threshold coin 让所有 honest parties 得到唯一随机 leader | 进展机制 | coin 在 proposal promotion 完成后使用 |
| §3.4 / p5-p6 | VABA view phases | leader-nomination, leader-election, view-change；commit 则 decide，否则更新 LOCK/KEY 进入下一 view | 协议骨架 | 先收集 `n-f` completed promotions，再随机选 leader |
| §3.5 / p6 | Correctness intuition | Lock Safety, Key Safety, Key Progress；KEY/LOCK 保证跨 view 安全和解锁 | 安全直觉 | 会议版给直觉，完整证明可能在 extended version |
| §3.6 / p6-p7 | Progress and complexity | completed leader 被选中概率大于 `2/3`；expected views 小于 `3/2`；单 view `O(n^2)` word communication | 性能证据 | 结合下界称 asymptotically optimal |
| §4, Appendix A, refs / p7-p10 | 讨论、PB properties、相关工作 | 回答 Cachin et al. open problem；weak termination 下 lower bound/protocol 仍 open | 边界和队列 | 相关工作含 PBFT、HoneyBadger、BEAT、HotStuff 等 |

## 一句话贡献

本文给出 authenticated asynchronous adaptive Byzantine setting 下的 VABA 协议，通过 provable broadcast、proposal promotion、threshold-coin leader election 和 key/lock/commit view-change，在 `f < n/3` 下达到 expected `O(1)` time 与 expected `O(n^2)` word communication，并把 Cachin et al. 2001 的 `O(n^3)` open problem 降到渐进最优。

## 核心精读笔记

### 背景、问题和为什么不是普通 ABA

论文研究的是 validated multi-valued asynchronous Byzantine agreement。Binary asynchronous BA 已有能做到 optimal resilience 和 expected constant time 的协议；但 Atomic Broadcast 和 fault-tolerant state machine replication 需要决定的不只是 bit，而是应用值、交易批次或命令，并且决定值必须满足外部有效性谓词。弱有效性不够，因为 adversary 可以让协议决定一个对应用无意义的值，或者用默认值绕开真实请求。证据锚点: §1 p1-p2, Definition 4 p3。

VABA 的外部有效性由 `EX-VABA-VAL(v)` 表示。协议的 Validity 要求 honest party 决定的值必须 externally valid；Quality 要求当 honest parties 以 valid values 启动时，至少以 `1/2` 概率选择 honest party proposed value。这一条让协议不能靠固定输出某个 valid default value 伪装成 validated agreement。证据锚点: Definition 4 p3。

### 模型和终止定义的微妙处

系统是 asynchronous message passing，`n` parties，adaptive adversary 可在执行中 corrupt 最多 `f < n/3` 个 parties。论文在 authenticated setting 中使用 trusted dealer setup、random oracle model、threshold signatures 和 threshold coin-tossing。adversary 控制网络调度，但为了保持加密 setting 的 meaningfulness，在 honest parties 间消息传输期间 adversary 计算步数被限制为 polynomially bounded；同时 adversary 不能在执行期间读取 honest party 的内部状态。证据锚点: §2 p2。

论文区分 cryptographic asynchronous model 下的 liveness 表述。它采用 Cachin et al. 的 termination 和 efficiency 风格: honest messages 数量需要 probabilistically uniformly bounded；若 honest parties 之间所有消息都被 delivered，则 all honest parties terminate。作者也提到更弱的 termination notion，并把 adaptive setting 下 weak termination 的 lower bound/protocol 留作 open question。证据锚点: §2 p2-p3, §4 p7。

### 加密抽象: threshold signature 和 threshold coin

Threshold signature interface 包括 `share-sign_i`、`share-validate`、`threshold-sign`、`threshold-validate`。只要收集 `n-f` 个 valid signature shares，就能生成 threshold signature。这里的 `n-f` threshold 与 `f < n/3` 一起提供 quorum intersection，确保 proof 里包含足够 honest participation。证据锚点: Definition 1 p2。

Threshold coin-tossing interface 包括 `coin-share_i`、`coin-share-validate`、`coin-toss`。任意 `f+1` 个 valid coin shares 可以得到唯一伪随机数，输出范围为 `[1,n]`。Leader-Election 用这个 coin 选出共同 leader，并依赖 unpredictability 让 adversary 不能提前只针对会被选中的 leader 阻断进展。证据锚点: Definition 2 p2-p3, §3.3 p5。

### Provable-Broadcast: 让 broadcast 变成可携带的证明

Provable-Broadcast 是两轮 broadcast。sender 先发送 value/proof；receivers 检查外部有效性后 deliver，并把 threshold signature share 发回 sender；sender 等待 `n-f` signed shares 后合成为 proof。Appendix A 给出的关键性质包括 integrity、validity、abandon-ability、provability 和 termination: 如果 sender 能形成 proof，则至少 `f+1` honest parties delivered；sender 无法为两个不同 values 都形成 proof。证据锚点: §3.1 p3-p4, Appendix A p8。

这个抽象的重要性在于，协议后续不需要让所有人重新相信原始广播路径，只要携带 threshold-signature proof，就能把“某个值已经被足够多 honest parties 见过”的事实传到下一阶段。它是 VABA 把通信量压到 `O(n^2)` 的基础之一。证据锚点: §3.1 p3-p4。

### Proposal-Promotion: 在每个 view 中为每个候选 leader 提前铺路

每个 view 同时运行 n 个 Proposal-Promotion instances，每个 instance 以一个 party 作为 leader。Proposal-Promotion 由四个顺序 Provable-Broadcast steps 组成。第 1 步广播 value 和 key proof；后续步骤使用前一步 threshold signature proof 作为外部有效性证据。节点本地维护 key、lock、commit 三类 delivered messages，completion proof 来自第 4 步 PB。证据锚点: §3.2 p4-p5。

这种设计的核心不是“先选 leader 再看它能不能提案”，而是先让足够多 leader candidates 完成可证明推进，然后再用随机 leader election 从已推进集合中抽一个。由于每个 view 至少等到 `n-f` proposal promotions 完成，被 coin 选中的 leader 已经完成的概率大于 `2/3`。adaptive adversary 在 coin 之后才知道 leader 时，无法回头阻止已经完成的 promotion。证据锚点: §3.4-§3.6 p5-p7。

### KEY/LOCK/COMMIT: 异步 view-change 的安全骨架

LOCK 存储 party 在 elected leader 的 Proposal-Promotion 中收到 lock 的最高 view；KEY 存储最高 view 的 key tuple/value/proof。下一 view 的第 1 步 external validity 检查要求 proposed value externally valid，并且 key view 不低于本地 LOCK。这让被锁定的值不会被不同值的 key 越过。证据锚点: §3.4-§3.5 p5-p6。

安全直觉分三层。Lock Safety: 若 view R 中存在 commit proof，则至少 `f+1` honest parties 在 R 中 delivered lock。Key Safety: 对某个 value 的 commit proof 会阻止更高或相同 view 中为不同 value 形成 valid key。Key Progress: 如果某 party 在 R 中被 lock，honest parties 会在下一 view 获得 view 不低于 R 的 KEY，从而可以推进或解锁。证据锚点: §3.5 p6。

### 进展和复杂度

每个 view 中，leader-nomination 等到 `n-f` Proposal-Promotion instances completed 后发送 skip-share，并合成 threshold skip signature 进入 election。由于 completed set 大小至少 `n-f`，threshold coin 在 `[1,n]` 上均匀选 leader 时，选中 completed leader 的概率至少 `(n-f)/n > 2/3`。因此 expected number of views 小于 `3/2`，expected running time 为常数。证据锚点: §3.4-§3.6 p5-p7。

通信上，单个 Provable-Broadcast 是 `O(n)` words，单个 Proposal-Promotion 是四个 PB，仍为 `O(n)` words；每 view 有 n 个 Proposal-Promotion，leader-election 和 view-change 各是 all-to-all `O(n^2)` one-word messages。因此每 view `O(n^2)`，再乘 expected constant views，得到 expected `O(n^2)` word communication。证据锚点: §3.6 p6-p7。

论文还引用近期 lower bound: adaptive adversary 下任何没有 constant error probability 的 ABA protocol 都要求 honest parties 发送 expected `Omega(n^2)` messages。因此本文的 `O(n^2)` message/word order 是 asymptotically optimal。证据锚点: §1 p1-p2, Theorem 1 p1。

### 限制和迁移边界

这篇是 formal protocol paper，没有实现或实验。它的结论依赖 authenticated setting、trusted dealer 或相当的 setup、threshold signatures、threshold coin 和 random oracle model。把 VABA 迁移到实际 blockchain 或 SMR 系统时，还需要处理 transaction dissemination、mempool、batch validity、client semantics、committee membership、key generation/setup、网络实现以及应用层 external validity predicate。证据锚点: §2 p2-p3, §4 p7。

它解决的是 VABA 的 asymptotic communication/time open problem，不直接替代 HoneyBadger/BEAT/Narwhal/Tusk 等系统层协议。它应当连接到 async BFT foundations、atomic broadcast/SMR、common coin、reliable/provable broadcast 和 external validity，而不是被归为某一个具体区块链协议实例。证据锚点: §1 p1-p2, refs p8-p10。

## 层级分类

| 层级 | 候选 | 证据 | 状态 |
| --- | --- | --- | --- |
| L1 domain | `distributed-systems` | VABA, asynchronous Byzantine agreement, Atomic Broadcast, SMR | accepted |
| L2 direction | `consensus` | agreement, termination, validity, BFT fault threshold | accepted |
| L3 topic | `asynchronous-bft-consensus` | asynchronous model, common coin, adaptive adversary, `f < n/3` | accepted |
| L4 problem | `validated-asynchronous-byzantine-agreement` | externally valid multi-valued asynchronous Byzantine agreement is the paper's explicit object | accepted as new knowledge node |
| Secondary domain | `blockchain-systems/consensus` | refs and motivation include blockchain/SMR use, but paper itself is foundation rather than blockchain protocol | accepted as bridge facet |

## 与现有 Nahida 笔记的关系

| Existing note | Relation | Update needed | Reason |
| --- | --- | --- | --- |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | parent problem | add child/source extension | VABA is a reusable async BFT subproblem with external validity and optimal complexity |
| [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]] | new child problem | create | Needed to avoid burying VABA under a single paper source |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | ancestor problem | source extension | Fault model and `f < n/3` threshold extend BFT foundations |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | bridge | add transfer/evidence row | VABA clarifies how async BFT foundations serve atomic broadcast/SMR before blockchain-specific workload layers |
| [[blockchain-consensus|Blockchain consensus]] | secondary application direction | optional evidence only | Use as bridge/application facet; do not make blockchain the primary path |

## Knowledge Handoff

| Target knowledge node | Absorption instruction | Evidence | Status |
| --- | --- | --- | --- |
| [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]] | Define VABA as externally valid multi-valued async Byzantine agreement; list Cachin-style `O(n^3)` baseline, this paper's `O(n^2)` route, and open weak-termination question | Definition 4, Theorem 1, §3.1-§3.6, §4 | done |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | Add VABA as child subproblem and representative source; connect provable broadcast, proposal promotion and threshold coin to async BFT methods | §1-§3.6 | done |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | Add as source extension under asynchronous/randomized BFT, not as standalone protocol branch | §2, Definition 4 | done |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | Add bridge evidence that external validity is the adapter from generic BA to atomic broadcast/SMR/blockchain ordering | §1, §4 | done |

## Foundation candidate

- 是否为基础概念来源: yes。
- 适合提取的基础概念: `validated-asynchronous-byzantine-agreement`, `external validity`, `provable broadcast`, `threshold coin`, `adaptive asynchronous Byzantine adversary`。
- 本次新建节点: [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]]。
- 本次不新建节点: `provable broadcast` 和 `threshold coin` 暂作为 VABA/async BFT 方法行，等后续多来源覆盖后再拆。

## Review Items

| Item | Why | Status |
| --- | --- | --- |
| 检查是否有 VABA full/extended version | PODC 10 页版压缩了部分证明 | queued |
| 后续补 Cachin et al. 2001 VABA source | 本文主要与其 `O(n^3)` baseline 对比 | queued |
| 后续补 HoneyBadger/BEAT/Bracha RBC/common coin source | VABA 与 async atomic broadcast/SMR 系统的连接仍薄 | queued |

## Cold-start retrieval

- 查询 `VABA` 时先打开本 source，再打开 [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]]。
- 查询 `async BFT external validity` 时优先打开 [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]]，再回到本 source 的 Definition 4 和 §3。
- 查询 `asynchronous BFT O(n^2) communication` 时注意区分 binary BA 的 Mostefaoui-Moumen-Raynal 路线与本文 multi-valued externally-valid VABA 路线。
