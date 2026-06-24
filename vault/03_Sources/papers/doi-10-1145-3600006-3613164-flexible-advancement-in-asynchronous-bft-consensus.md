---
id: "doi-10.1145-3600006.3613164"
title: "Flexible Advancement in Asynchronous BFT Consensus"
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
  - "p1-p2 abstract, introduction, WAN/blockchain motivation, fixed-slot asynchronous protocol limitations, MyTumbler and SuperMA contribution overview"
  - "p2-p3 system model, n and f assumptions, asynchronous reliable channels, loosely synchronized physical clocks"
  - "p3-p4 production workload motivation, BKR/HBBFT-style fixed-slot asynchronous flow, comparison table"
  - "p4-p7 flexible-advancement paradigm, ARBC abstraction, MyTumbler timestamp ordering, pass/skip mechanism, Algorithm 1, liveness lemmas"
  - "p7-p10 SuperMA, fast negotiation, FastBA, Algorithm 2, correctness theorems for BA and ARBC"
  - "p10-p13 Go implementation, WAN experimental setup, fault-free/faulty performance, light/far-away/unbalanced workload results"
  - "p13-p14 related work, ordering and agreement taxonomy, limitations, conclusion"
  - "p15-p17 references"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1145/3600006.3613164"
doi: "10.1145/3600006.3613164"
arxiv_id: ""
venue: "SOSP 2023"
year: "2023"
pdf_pages: 17
pdf_sha256: "d9b5267f06a1fa2dc540e0192ec3d1b0a611cf172ce89acc9c4b9bf94cd74598"
local_pdf: "~/Desktop/paper/3600006.3613164.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/flexible-advancement-in-asynchronous-bft-consensus-d9b5267f06a1-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-bft-consensus"
  - "byzantine-fault-tolerance"
  - "leaderless-consensus"
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
primary_ontology_path: "blockchain-systems/consensus/asynchronous-bft-consensus/doi-10.1145-3600006.3613164"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/doi-10.1145-3600006.3613164"
  - "blockchain-systems/consensus/leaderless-consensus/doi-10.1145-3600006.3613164"
path_update_status: "propagated"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "asynchronous-bft-consensus"
  - "byzantine-fault-tolerance"
  - "flexible-advancement"
  - "MyTumbler"
  - "SuperMA"
  - "FastBA"
  - "ARBC"
aliases:
  - "MyTumbler"
  - "SuperMA"
  - "FastBA"
  - "Flexible advancement"
  - "Abortable Reliable Broadcast"
  - "ARBC"
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
    - "fixed-slot overhead in asynchronous BFT"
    - "leader bottleneck and timeout tuning in WAN blockchains"
    - "light and unbalanced workload latency"
    - "far-away proposer suppression"
    - "randomization on asynchronous agreement critical path"
  method_family:
    - "flexible advancement"
    - "timestamp-based state machine replication"
    - "abortable reliable broadcast"
    - "promise-based fast path"
    - "randomized binary agreement"
  system_layer:
    - "ordering"
    - "agreement"
    - "state machine replication"
    - "blockchain consensus"
  evaluation_context:
    - "Go implementation"
    - "public cloud WAN clusters"
    - "4 to 100 nodes"
    - "fault-free, crash-fault, Byzantine-fault, light, skewed, and unbalanced workloads"
  application:
    - "permissioned blockchains"
    - "WAN state machine replication"
  bridge:
    - "distributed BFT -> asynchronous blockchain consensus"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-flexible-advancement-asynchronous-bft"
source_refs:
  - "doi:10.1145/3600006.3613164"
  - "sha256:d9b5267f06a1fa2dc540e0192ec3d1b0a611cf172ce89acc9c4b9bf94cd74598"
  - "pdf:~/Desktop/paper/3600006.3613164.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> consensus"
secondary_directions:
  - "distributed-systems -> consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "PDF title page and ACM reference"
  - "Abstract and Sections 1-8"
  - "Algorithm 1, Algorithm 2, Lemmas 1-7, Theorems 1-4"
  - "local PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0019"
queue_status: "absorbed"
---

# Flexible Advancement in Asynchronous BFT Consensus

## 论文身份

- 标题: Flexible Advancement in Asynchronous BFT Consensus
- 作者: Shengyun Liu, Wenbo Xu, Chen Shan, Xiaofeng Yan, Tianjing Xu, Bo Wang, Lei Fan, Fuxi Deng, Ying Yan, Hui Zhang
- 机构: Shanghai Jiao Tong University; Blockchain Platform Div., Ant Group
- 会议/年份: SOSP '23, October 23-26, 2023, Koblenz, Germany
- DOI: 10.1145/3600006.3613164
- 链接: https://doi.org/10.1145/3600006.3613164
- 本地 PDF: `~/Desktop/paper/3600006.3613164.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/flexible-advancement-in-asynchronous-bft-consensus-d9b5267f06a1-pages.txt`
- 代码: unknown in PDF
- License: ACM copyright/license notice on p1

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 17
- 已覆盖章节/页码: p1-p17 full text
- 已检查附录: 无独立 appendix；p15-p17 references 已检查。
- 未覆盖章节/页码: 无
- Extraction gaps: 图表曲线坐标有抽取噪声，吸收时只使用正文明确描述的比较结论、图号和量级表述；算法伪码、定理、实验设置和 limitations 可读。
- 精读说明: 这篇是异步 BFT/区块链共识的 source-backed seed，重点贡献在 ordering/agreement 连接范式和 agreement fast path；不要把评测结论泛化到所有 permissionless 或完全开放网络，论文场景主要是 permissioned/WAN blockchain applications。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 动机与贡献 | WAN 区块链中 partial synchrony/leader-based BFT 的 leader 和 timeout 问题；现有异步协议 fixed-slot/coin critical path 问题；提出 flexible advancement, SuperMA, MyTumbler | 贡献定位 | 明确声称 MyTumbler 适合 light/unbalanced workloads |
| §2 / p2-p3 | 系统模型 | `n` nodes, at most `f < n/3` Byzantine, reliable asynchronous channels, signatures/hash/threshold signatures, loosely synchronized physical clocks | 模型边界 | physical clock 影响效率，不影响 safety/liveness |
| §3 / p3-p4 | 背景和动机 | permissioned blockchain 的 heterogeneous workload/latency；BKR/HBBFT fixed-slot asynchronous flow；Table 1 比较 compulsory/dedicated proposer roles | 问题设定 | Figure 1 展示慢节点 proposal 被快节点 abort |
| §4.1 / p4-p5 | Flexible advancement | committed proposal 不能立刻执行，需要知道更早位置不会再 commit；用 pass 表示不再 endorse 更早位置；Lemma 1 给 quorum intersection 安全直觉 | 核心机制 | 将推进 pace 从固定 slot 中抽离 |
| §4.1 / p5 | ARBC abstraction | `ENDORSE`/`ABORT` 输入，输出 message 或 bottom；Agreement, Strong Validity, Conditional Termination, Totality | 抽象接口 | SuperMA 是 ARBC 实例化 |
| §4.2-4.3 / p5-p7 | MyTumbler | timestamp ordering, pass messages, endorsed set, `exec_ts`, skip mechanism, Algorithm 1 | 协议机制 | pass 通过 FIFO channel 传递并携带 recently endorsed MAs |
| §4.4 / p7 | MyTumbler correctness | Lemma 2-5 证明 pass propagation, proposal liveness, committed MA executability, request execution | 正确性证据 | 证明依赖 ARBC properties 和 pass ordered delivery |
| §5.1 / p7-p8 | SuperMA fast negotiation | propose/endorse/prom 三阶段；若收到 `n-f` prom 可直接决定，避免进入 BA | agreement fast path | 类 PBFT normal case，但在异步 ARBC 下使用 promise |
| §5.2-5.3 / p8-p10 | FastBA | promise-based BA fast path；normal path 使用 common coin；Lemma 6-7, Theorem 1-4 | 正确性和复杂度 | 期望 `O(lambda n^3)` communication complexity, `O(n^2)` messages |
| §6.1-6.2 / p10-p11 | 实现和实验设置 | Go implementation, SHA256, Ed25519, BLS threshold signature common coin, public cloud 5 regions, 1000-byte requests | 实证设置 | 与 HotStuff, Tusk, BKR, BKR-SuperMA 比较 |
| §6.3 / p11-p12 | Fault-free performance | BKR-SuperMA latency 最低；MyTumbler throughput 更高；SuperMA 降低 BKR latency；Tusk small n peak high但 coin 在执行路径 | 性能证据 | 文中报告 BKR-SuperMA up to order-of-magnitude latency reduction |
| §6.4 / p12-p13 | Faults | crash faults 下 MyTumbler 无 timeout fail-over；Byzantine nodes 可破坏 fast negotiation 但通常仍能 FastBA 首轮 abort | 鲁棒性证据 | HotStuff 在某些设置因 timeout/leader crash 表现差 |
| §6.5 / p13 | 真实 workload | far-away node, light workload, unbalanced workload；MyTumbler 通过 timestamps/skip 避免慢节点 proposal 被 abort、降低 idle-slot 开销 | 应用证据 | 对 Ant Group production-like 场景特别重要 |
| §7-8 / p13-p14 | Related work and limitations | ordering 分类: sequence, chain, DAG, timestamp；agreement 分类: asynchronous/partial synchrony/synchrony；limitations: common coin/DKG, `O(n^3)` communication | 边界 | flexible advancement 不能直接套 chain ordering |

## 一句话贡献

本文把异步 BFT SMR 中 ordering 与 agreement 的连接方式改成 flexible advancement: 节点用 pass/skip/timestamp 自适应推进可执行边界，并用 SuperMA/FastBA 在 common case 绕过随机化，从而让 leaderless asynchronous BFT 更适合 WAN permissioned blockchain 的轻载、偏载和远距离 proposer 场景。

## 核心精读笔记

### 背景、动机与问题边界

论文针对的是区块链/SMR 中的 BFT ordering。作者认为 WAN permissioned blockchain 和传统 SMR 不同: 节点代表不同机构，工作负载和跨区域延迟可能高度不均衡。leader-based partially synchronous BFT 在这种场景有两个直接问题: 需要调 timeout/maximum network delay，且单 leader 容易成为 proposal bottleneck。即使轮换 leader，faulty 或远距离 leader 也会让 timeout/failover 成本进入用户可见路径。证据锚点: §1 p1-p2, §3 p3。

异步 BFT 不依赖 timing assumption，并且每个节点可以平等提案，但 BKR/HBBFT/Tusk 这类 fixed-slot 结构仍有两个问题。第一，每个节点每轮都有预分配 slot，即使无请求也要提案或空提案；第二，快的 `n-f` 节点可能先推进，导致慢节点的真实请求被 abort。Figure 1 中 `n=4,f=1` 时，node 0 的请求因网络慢被其他节点在其 slot 输入 0 而 abort。证据锚点: §3 p3-p4。

论文目标不是替代所有 BFT 基础，而是在 `f < n/3` 和可靠异步信道下，为 permissioned blockchain 的 heterogeneous workload 提供一种更 flexible 的 asynchronous SMR 结构。它仍依赖 signatures、hash functions 和用于 coin-flipping 的 threshold signatures；MyTumbler 还使用 loosely synchronized physical clocks 作为 timestamp source，但作者明确说 clock synchronization 影响效率，不影响 safety/liveness。证据锚点: §2 p2-p3。

### Flexible advancement: 从填满 slot 改成证明更早位置不会再 commit

固定槽协议回答“能否执行位置 `phi(B)` 的 proposal”的方式是填满所有更早 slot: 每个 slot 必须有 proposal 或 abort decision。Flexible advancement 换了问题: correct nodes 只需要知道更早位置不可能再出现可 commit proposal，而不是强制每个位置都有内容。证据锚点: §4.1 p4。

具体做法是 pass。一个节点 pass 某个位置，含义是承诺不再 endorse 更早位置的 proposal。若 `n-f` 个节点都 pass 某位置，而 agreement component 要求 commit proposal 必须有 `n-f` endorse quorum，则两个 quorum 至少交于一个 correct node。因此，一个已经被 `n-f` pass 排除的 proposal 不可能再获得 commit quorum。Lemma 1 将此形式化为: 若 `n-f` 节点声明未 endorse 某 proposal 且承诺未来也不 endorse，该 proposal 不能被 commit。证据锚点: §4.1 p4-p5。

这个抽象改变了系统 pace: 当只有少数节点有请求时，其他节点可以 skip/pass，系统快速推进；当多数节点都在提案时，系统可以放慢并容纳更多 proposal。这里的“flexible”不是参数调优，而是 ordering/executability 层允许 workload 影响推进速度。证据锚点: §4.1 p5。

### ARBC: agreement 组件的接口

论文将单提案 agreement 抽象为 Abortable Reliable Broadcast (ARBC)。proposer broadcast message `m`，节点可输入 `ENDORSE` 或 `ABORT`，输出 `m` 或 `bottom`。ARBC 要满足 Agreement、Strong Validity、Conditional Termination、Totality。Strong Validity 很关键: 非 bottom 决定必须被 `n-f` 节点 endorse；若 proposer correct 且没有 correct node 输入 abort，则所有 correct nodes 决定 proposer 的 message。Conditional Termination 则保证当所有 correct nodes 都输入 abort 后实例会终止。证据锚点: §4.1 p5。

Flexible advancement 借 ARBC 处理“有人已经 endorse，但别人已经 pass”的歧义。节点收到 `phi(B)` proposal 时，如果自己尚未 pass 该位置就 endorse；如果后来 `n-f` 节点已 pass 该位置但 proposal 未 commit，就对相关 ARBC 输入 abort。证据锚点: §4.1 p5。

### MyTumbler: timestamp, pass, skip 和 exec_ts

MyTumbler 使用 physical timestamp 作为 ordering indicator，而不是 sequence number。timestamp ordering 让不同 proposer 可以把 proposal 放在更精细的位置，减少多个 proposal 争同一个 sequence slot 的竞争。问题是: 节点看到 timestamp `ts` 的 ARBC commit 后不能立刻执行，因为异步网络中可能还有未见的更早 timestamp proposal；同时节点也不能无限等待更早 proposal。证据锚点: §4.2 p5。

MyTumbler 的规则是: 节点只有在 `n-f` nodes 已 pass `ts` 后，才把 `exec_ts` 推到 `ts` 并执行 `ts` 以前所有已 committed 且更早 pending ARBC 已终止的 blocks。一个节点在看到来自 distinct proposers 的 `n-f` 个 ARBC instances 在 `ts` 之后 commit 后，可以 pass `ts`；pass message 还携带自己最近 endorse 的 proposals，帮助其他节点发现可能尚未看到但可 commit 的实例。证据锚点: Algorithm 1 p6-p7。

pass messages 需要 peer-to-peer FIFO ordered delivery，否则后收到的旧 pass 可能破坏 promise 的时间顺序。论文说可以用 sequence numbers 实现 FIFO，并指出 chain/DAG ordering 也隐含类似 ordering restriction。证据锚点: §4.3 p7。

skip mechanism 处理轻载: 若节点没有 pending requests，可以广播 signed skip。skip 不经过 ARBC，也不用放入 pass messages；它等价于一个不含 payload、只帮助推进 `passed_ts` 的证据。修改后的 pass rule 是: 节点看到 `n-f` 个 distinct nodes 中每个都在 `ts` 之后有 committed MA 或 skip `ts' >= ts`，且 `ts` 处至少有一个 committed MA，就可以 pass `ts`。证据锚点: §4.3 p7。

### MyTumbler 正确性边界

Safety 依赖 ARBC Agreement/Strong Validity、Lemma 1 和 pass message ordered delivery。直觉是: correct node 不会漏掉任何可能 commit 的 ARBC instance；如果某 earlier proposal 没出现在 `n-f` pass messages 中，就不可能再获得 commit quorum。证据锚点: §4.4 p7。

Liveness 由 Lemma 2-5 分层证明。Lemma 2: 一个 correct node pass `ts` 后，其他 correct nodes 最终也能 pass `ts`，因为 skip 会可靠传播，ARBC 有 totality/agreement。Lemma 3: correct node 在 `ts` 提案后，所有 correct nodes 最终能 pass `ts`。Lemma 4: every committed MA becomes executable，因为更早 pending instances 要么被某 correct node endorse 并进入 pass message，要么无人 endorse 并可按 Line 25-26 决定 bottom。Lemma 5: 若 every correct node 的 proposal 包含 request `req`，则 `req` 会在某 ARBC commit 并最终执行。证据锚点: §4.4 p7。

### SuperMA and FastBA: common case 绕过随机化

SuperMA 是 ARBC 实例化。第一层 fast negotiation 有 propose, endorse, prom 三阶段。节点收到 `n-f` 个相同 hash 的 endorse 后，输入 1 给 BA 并传播 endorse 证据；如果自己没有为 bottom endorse，就广播 `prom(hash)`。当节点收到 `n-f` 个 `prom(hash)` 时，可以直接决定 message，因为此时没有 correct node 会输入 0 给 BA。对 bottom 的情况对称。证据锚点: §5.1 p8。

Fast negotiation 不是完整 agreement；如果 correct nodes 对 proposal 意见分裂，可能有人输入 1、有人输入 0，这时进入 FastBA。FastBA 扩展 Mostefaoui-style BA，引入 promise fast path: 当 `n-f` 节点对同一 binary value `b` 投票并承诺不投 `1-b`，`b` 就是唯一可能 valid value，节点可在两阶段后决定，无需 common coin。若 votes 分裂，则走 normal path，经 aux/con/common coin 收敛。证据锚点: Algorithm 2 p9, §5.2 p8-p9。

论文给出 Lemma 6-7 和 Theorem 1-2 证明 FastBA Agreement/Termination，再用 Theorem 3-4 证明 SuperMA ARBC Agreement/Conditional-Termination。复杂度上，FastBA/SuperMA 期望 `O(lambda n^3)` communication complexity 和 `O(n^2)` message complexity；作者认为签名传播的渐进代价在实践中相对大 payload dissemination 较小。证据锚点: §5.2-5.3 p9-p10。

### 实验与性能解释

实现是 Go，使用 SHA256、Ed25519 和 BLS threshold signature 构造 common coin；pass message 用 sequence number 实现 FIFO。实验部署在 5 个 public cloud regions，节点从 4 到 100，比较 HotStuff、Tusk、BKR、BKR-SuperMA 和 MyTumbler，并用 1000-byte requests 模拟较大交易。证据锚点: §6.1-6.2 p10-p11。

Fault-free 下，BKR-SuperMA 在所有配置中平均延迟最低，因为每个 fixed slot proposal 可通过 fast negotiation 三阶段结束，且 `n` 个 SuperMA instances 并行。MyTumbler 延迟略高，因为要付 pass mechanism 的 executable cost；但它的 peak throughput 比 BKR-SuperMA 更高，原因是 timestamp ordering 减少 proposal abort，且 pass 规则让 proposal 更可能被容纳。正文给出例子: `n=4` 下 BKR-SuperMA saturated 时 19.7% SuperMA instances aborted，而 MyTumbler 在相似 throughput 处没有 instance aborted，饱和时也只有 0.8% aborted。证据锚点: §6.3 p11-p12。

Crash faults 下，MyTumbler 在 `n=4` 和 `n=10` 平均延迟最低。BKR-SuperMA 要为 faulty nodes 的 slots deliver bottom；Tusk 可能 coin 选中 crashed node 的 null block；HotStuff 在轮换到 crashed leader 时受 timeout 影响。MyTumbler 只要 `n-f` nodes correct，就能持续推进 passed/executable timestamp，没有 timeout fail-over。证据锚点: §6.4 p12。

Byzantine faults 下，作者构造 Byzantine nodes 只给部分 correct nodes 传播 proposals 并不参与消息交换，从而破坏 fast negotiation。这会让 problematic proposals 被少数 correct nodes endorse 后最终 abort，但通常仍能在 FastBA 第一轮输出 0；作者认为需要 adversary 精准控制 message scheduling 才会频繁触发 coin-flipping。这个结论是实验场景内的性能判断，不等于对强自适应 adversary 的普遍性能保证。证据锚点: §6.4 p12-p13。

更真实 workload 中，MyTumbler 的定位最清楚。far-away node 场景中，Frankfurt 节点在 Tusk 和 BKR-SuperMA 中没有 block commit，因为近端三节点看到其 proposal 时已经进入新 round 或对该 slot 决定 0；MyTumbler 虽然 Frankfurt latency 增大，但仍能 commit。light workload 下，MyTumbler 因 skip 和 SuperMA promise 绕过 randomization 得到最低 latency。unbalanced workload 下，其他异步协议仍需 idle nodes 构造和 commit empty blocks，而 MyTumbler 让 idle nodes skip timestamps。证据锚点: §6.5 p13。

### 局限与迁移边界

MyTumbler/SuperMA 仍需要 common coin fallback；若无 trusted party，threshold signature common coin 需要 DKG。SuperMA 用通信复杂度换快速终止，单实例 `O(n^3)` communication 在很大 `n` 时需要 threshold signatures 或 gossip 进一步优化。证据锚点: §7.3 p14。

Flexible advancement 可接入 sequence、DAG、timestamp 等 ordering 方法，但不容易直接接入 chain-based ordering，因为 chain structure 不自然支持不同节点 concurrent proposing。MyTumbler 本文只实现 timestamp ordering；论文结论不能直接证明 DAG/sequence 版本的性能。证据锚点: §7.1, §8 p13-p14。

## 层级分类

| 层级 | 候选 | 证据 | 状态 |
| --- | --- | --- | --- |
| L1 domain | `blockchain-systems` | title/abstract 明确 blockchains；motivation 来自 permissioned blockchain production scenarios；评测面向 blockchain SMR | accepted |
| L2 direction | `consensus` | BFT consensus, SMR, ordering/agreement, HotStuff/Tusk/BKR baselines | accepted |
| L3 topic | `asynchronous-bft-consensus` | asynchronous protocols, no timing assumptions, SuperMA/FastBA/common coin, MyTumbler | accepted |
| Secondary topic | `byzantine-fault-tolerance` | `f < n/3`, Byzantine adversary, BFT SMR, ARBC/BA correctness | accepted as foundation extension |
| Secondary topic | `leaderless-consensus` | each node can propose when it has requests; no dedicated proposer role at SMR layer | accepted as retrieval facet |

## 与现有 Nahida 笔记的关系

- 扩展 [[byzantine-fault-tolerance|Byzantine fault tolerance]]: 增加 asynchronous BFT 的 randomized agreement/common-coin 路线，以及 fixed-slot vs flexible advancement 的性能边界。
- 扩展 [[blockchain-consensus|Blockchain consensus]]: 新建 [[asynchronous-bft-consensus|Asynchronous BFT consensus]] topic，补上 permissioned WAN blockchain 的 leaderless/asynchronous branch。
- 连接 [[shared-mempool|Shared mempool]]: Stratus 处理 leader-based BFT 的数据传播瓶颈；MyTumbler 处理异步 BFT 中 fixed-slot/slow-proposer/coin-path 瓶颈。二者都提醒 consensus 性能不只由 safety proof 决定。
- 与 Cobalt 互补: Cobalt 关注 open-network governance 和 non-uniform trust；MyTumbler 仍假设 symmetric `n-f` quorum 和 known public keys。

## 可复用思路

- 将“commit 已达成”和“safe to execute”分层: 在异步 SMR 中，committed proposal 仍可能被更早位置阻塞，pass/exec_ts 可作为独立推进层。
- 将 idle participant 明确建模为 skip，而不是强制其提交空 block。
- 用 promise 证明“另一边不可能成为 valid input”，从而在 BA/ARBC common case 绕过 common coin。
- 评测异步 BFT 时必须包含 light/unbalanced/far-away proposer workloads；只看 saturated uniform throughput 会掩盖 fixed-slot 缺陷。

## 术语表

| Term | 解释 | 来源 |
| --- | --- | --- |
| Flexible advancement | 用 pass promise 推进可执行边界，而不是强制填满每个 slot | §4.1 |
| ARBC | Abortable Reliable Broadcast，输出 message 或 bottom 的 multi-valued agreement abstraction | §4.1 |
| MyTumbler | timestamp-based asynchronous BFT SMR protocol using flexible advancement and SuperMA | §4 |
| SuperMA | efficient ARBC instantiation with fast negotiation plus FastBA fallback | §5 |
| FastBA | promise-enhanced randomized binary agreement, common case without common coin | §5.2 |
| pass | 节点承诺不再 endorse 某 timestamp/position 之前的 proposal，并携带 recently endorsed proposals | §4.1-4.3 |
| skip | idle node 用 signed skip 帮助推进 timestamp，不经过 ARBC | §4.3 |
| `exec_ts` | MyTumbler 中只有其之前的 committed proposals 可安全执行的 watermark | Algorithm 1 |

## Evidence Table

| Claim | Source location | Evidence note | Claim type | Confidence |
| --- | --- | --- | --- | --- |
| Existing asynchronous protocols waste resources under light/unbalanced workloads and can abort slow proposers | §3 p3-p4, Figure 1, Table 1 | BKR/HBBFT fixed slots require every node proposal or empty proposal; `n-f` fast nodes can suppress slow node request | problem | high |
| Flexible advancement uses pass quorum intersection to prove older proposals cannot commit | §4.1 p4-p5, Lemma 1 | `n-f` pass quorum intersects `n-f` endorse quorum at a correct node under `f < n/3` | mechanism/theorem | high |
| MyTumbler uses timestamp ordering plus pass/skip to make proposals executable without filling all slots | §4.2-4.3 p5-p7, Algorithm 1 | pass messages update `passed_ts`; `exec_ts` is `(n-f)`th highest pass; skip handles idle nodes | mechanism | high |
| SuperMA can decide through fast negotiation in three message phases when nodes agree | §5.1 p7-p8, Figure 4 | propose/endorse/prom; `n-f` prom proves the opposite BA input cannot come from correct nodes | mechanism | high |
| FastBA bypasses common coin when `n-f` promises align | §5.2 p8-p9, Algorithm 2 | `n-f` prom for `b` means `1-b` cannot become valid; normal path still uses common coin | mechanism/theorem | high |
| MyTumbler improves workload adaptability in the paper's WAN experiments | §6.3-6.5 p11-p13, Figures 6-16 | throughput/latency comparisons under fault-free, crash, Byzantine, far-away, light, unbalanced workloads | empirical_result | medium-high |
| MyTumbler/SuperMA remain bounded by common coin and communication-complexity trade-offs | §5.2, §7.3 p9,p14 | common coin fallback requires threshold signatures/DKG; communication complexity `O(lambda n^3)` per SuperMA instance | limitation | high |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| FastBA avoids common-coin latency in the aligned-vote case by deciding b after n-f nodes promise not to vote for 1-b in the same round. | `doi:10.1145/3600006.3613164#p8-p10` | folded_into_meta_note |
| MyTumbler and SuperMA reduce common-case latency but remain bounded by common-coin setup and O(lambda n^3) communication per SuperMA instance. | `doi:10.1145/3600006.3613164#p9-p14` | folded_into_meta_note |
| Flexible advancement lets asynchronous BFT SMR advance by proving earlier positions cannot still commit, rather than forcing every node to fill a preassigned slot with a real or empty proposal. | `doi:10.1145/3600006.3613164#p3-p5` | folded_into_meta_note |
| MyTumbler advances executable time by collecting pass quorums: once n-f nodes promise not to endorse earlier timestamps, quorum intersection prevents unseen earlier proposals from later committing. | `doi:10.1145/3600006.3613164#p4-p7` | folded_into_meta_note |
| In the paper's far-away-node WAN experiment, MyTumbler commits blocks from the remote Frankfurt node while Tusk and BKR-SuperMA commit no Frankfurt blocks under the reported setting. | `doi:10.1145/3600006.3613164#p13` | folded_into_meta_note |
| MyTumbler uses signed skip messages from idle nodes so light or unbalanced workloads can pass timestamps without forcing agreement on empty blocks. | `doi:10.1145/3600006.3613164#p5-p7`<br>`doi:10.1145/3600006.3613164#p13` | folded_into_meta_note |
| SuperMA can decide an ARBC instance through propose, endorse, and prom phases without invoking binary agreement when n-f promises show the opposite BA input cannot come from correct nodes. | `doi:10.1145/3600006.3613164#p7-p8` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `[[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|MyTumbler flexible advancement removes fixed-slot compulsion]]`
- `[[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|MyTumbler pass quorums make earlier timestamps safe]]`
- `[[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|MyTumbler skip mechanism lowers light workload latency]]`
- `[[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|SuperMA fast negotiation bypasses randomization]]`
- `[[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|FastBA promise path avoids common coin when votes align]]`
- `[[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|MyTumbler preserves far-away proposer progress]]`
- `[[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|MyTumbler remains bounded by common coin and O(n^3) communication]]`

### Concepts to create or update

- Create [[asynchronous-bft-consensus|Asynchronous BFT consensus]] as source-backed topic seed.
- Create [[asynchronous-bft-consensus|Flexible advancement]] as the reusable ordering/agreement connection concept.
- Create [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|MyTumbler]] as protocol concept.
- Create [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|SuperMA]] with FastBA as submechanism concept.
- Update [[byzantine-fault-tolerance|Byzantine fault tolerance]] with asynchronous/common-coin/fixed-slot branch.

### Synthesis handoff

- Create/update [[asynchronous-bft-consensus|Asynchronous BFT consensus state 2026-06-19]] as topic synthesis.
- Refresh [[byzantine-fault-tolerance|Byzantine fault tolerance state 2026-06-11]] to include asynchronous BFT branch and keep FLP/Bracha/Mostefaoui/common coin as direct-source gaps.
- Create/update bridge [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]].

## 局限性

- 论文未给出公开代码链接；实现细节以正文描述为准。
- 图表逐点数值抽取不完整，吸收只使用正文明确数字和相对结论。
- `loose clock synchronization` 被作者说不影响 safety/liveness，但 timestamp choice 影响效率；这不等于完全摆脱时钟质量的性能问题。
- SuperMA 的 common coin fallback 仍需要 threshold signature/DKG 或 trusted setup；这对 production deployment 是实际系统成本。
- 论文使用 symmetric trust/quorum，未覆盖 Cobalt 一类 non-uniform trust/open-network governance。
