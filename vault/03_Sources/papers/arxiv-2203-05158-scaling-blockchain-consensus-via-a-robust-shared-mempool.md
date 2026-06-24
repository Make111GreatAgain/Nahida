---
id: "arxiv-2203.05158"
title: "Scaling Blockchain Consensus via a Robust Shared Mempool"
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
  - "p1-p2 abstract, introduction, leader bottleneck motivation, SMP contribution, Stratus overview"
  - "p2-p3 related work and comparison with Tendermint, Kauri, Leopard, Narwhal, MirBFT"
  - "p3-p5 shared mempool abstraction, system model, primitives, microblock/proposal/block data structures, missing-transaction and load-imbalance problems"
  - "p5-p7 PAB push/recovery phases, availability proof construction, Stratus MakeProposal/FillProposal integration, correctness theorems"
  - "p7-p9 distributed load balancing, Power-of-d choices, proxy forwarding, banList, stable-time workload estimation"
  - "p9-p10 Go/Bamboo implementation, HotStuff/PBFT/Streamlet integrations, evaluated protocol variants and benchmark setup"
  - "p11-p13 scalability experiments, bandwidth measurements, missing-transaction experiments, Byzantine-sender experiments, load-imbalance experiments"
  - "p13-p14 discussion, attacks on PAB/load balancing, reconfiguration, garbage collection, conclusion"
  - "p14-p15 references"
  - "p16-p17 appendix throughput analysis for LBFT and shared mempool"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2203.05158"
doi: ""
arxiv_id: "2203.05158v3"
venue: "arXiv"
year: "2022"
pdf_pages: 17
pdf_sha256: "642a8f376313099cef8cb209193377c67b86ab226f5c859227e5bc5556c47a8b"
local_pdf: "~/Desktop/paper/2203.05158.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2203.05158-642a8f376313-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "mempool-and-networking"
topic_ids:
  - "shared-mempool"
  - "leader-based-bft-scaling"
  - "provable-availability"
ontology_path:
  - "blockchain-systems"
  - "mempool-and-networking"
  - "shared-mempool"
primary_ontology_path: "blockchain-systems/mempool-and-networking/shared-mempool/arxiv-2203.05158"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/arxiv-2203.05158"
  - "blockchain-systems/consensus/leader-based-bft-scaling/arxiv-2203.05158"
path_update_status: "propagated"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "stratus"
  - "shared-mempool"
  - "provably-available-broadcast"
  - "leader-based-bft"
  - "load-balancing"
  - "hotstuff"
aliases:
  - "Stratus"
  - "Robust Shared Mempool"
  - "SMP"
  - "PAB"
  - "Provably Available Broadcast"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "mempool-and-networking"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "mempool-and-networking"
    - "consensus"
  problem:
    - "leader bottleneck in leader-based BFT"
    - "proposal data dissemination pressure"
    - "missing transactions in shared mempools"
    - "skewed client load across replicas"
  method_family:
    - "shared mempool"
    - "provably available broadcast"
    - "distributed load balancing"
    - "power-of-d choices"
    - "stable-time workload estimation"
  system_layer:
    - "transaction dissemination"
    - "mempool"
    - "leader-based BFT integration"
  evaluation_context:
    - "Bamboo prototype"
    - "HotStuff/PBFT/Streamlet integrations"
    - "Alibaba Cloud LAN/WAN experiments"
  application:
    - "permissioned blockchains"
    - "BFT-based proof-of-stake blockchains"
  bridge:
    - "BFT consensus -> shared mempool scaling"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-stratus-shared-mempool"
source_refs:
  - "arxiv:2203.05158"
  - "arxiv:2203.05158v3"
  - "sha256:642a8f376313099cef8cb209193377c67b86ab226f5c859227e5bc5556c47a8b"
  - "pdf:~/Desktop/paper/2203.05158.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> mempool-and-networking"
secondary_directions:
  - "distributed-systems -> consensus"
  - "blockchain-systems -> consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "PDF header and arXiv line"
  - "Abstract and Sections I-VII"
  - "Appendix throughput analysis"
  - "local PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0018"
queue_status: "absorbed"
original_queue_title: "Narwhal and Tusk: A DAG-based Mempool and Efficient BFT Consensus"
metadata_notes:
  - "Queue title was stale/mismatched: the local PDF header and arXiv line identify this file as Scaling Blockchain Consensus via a Robust Shared Mempool, not Narwhal and Tusk."
---

# Scaling Blockchain Consensus via a Robust Shared Mempool

## 论文身份

- 标题: Scaling Blockchain Consensus via a Robust Shared Mempool
- 作者: Fangyu Gai, Jianyu Niu, Ivan Beschastnikh, Chen Feng, Sheng Wang
- 机构: University of British Columbia; Southern University of Science and Technology; Alibaba Group
- 年份/版本: 2022, arXiv:2203.05158v3
- DOI: unknown
- 链接: https://arxiv.org/abs/2203.05158
- 本地 PDF: `~/Desktop/paper/2203.05158.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/2203.05158-642a8f376313-pages.txt`
- 代码: https://github.com/gitferry/bamboo-stratus and https://github.com/gitferry/bamboo, both listed in the PDF
- License: unknown in PDF
- Metadata review: intake queue 的题名曾写成 `Narwhal and Tusk: A DAG-based Mempool and Efficient BFT Consensus`；本地 PDF 的标题页和 arXiv header 明确对应 Stratus/shared mempool 论文。Narwhal 在此文中是 related work/baseline，不是这份 PDF 的标题。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 17
- 已覆盖章节/页码: p1-p17 full text including Appendix
- 未覆盖章节/页码: 无
- Extraction gaps: 公式和图表坐标有换行噪声；主要算法、表格和实验结论可读。Figure 7/9/11 的曲线数值没有全部逐点抽出，吸收时只使用论文正文明确描述的量级和结论。
- 精读说明: 这是一篇系统/协议性能论文，应作为 `shared mempool` 和 leader-based BFT scaling 的 source-backed seed。不要把它等同于 Narwhal/Tusk；文中对 Narwhal 的比较是在“每个 primary 一个 worker 且同 VM”的公平性设置下进行，不能替代直接吸收 Narwhal/Tusk 原文。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §I / p1-p2 | 动机与贡献 | leader-based BFT 的 proposal phase 把大批交易数据压在 leader 上；SMP 让 replicas 分布式传播交易，leader 只排序 ids | 贡献定位 | 声称 LAN/WAN 中比 native protocol 高 5x-20x |
| §II / p2-p3 | Related work | sharding, PigPaxos, Algorand, HoneyBadger/Dumbo, multi-leader BFT, Tendermint/Kauri/Leopard/Narwhal/MirBFT 对比 | 边界定位 | Table I 说明 Stratus 目标是 SMP + availability + load balance + O(n) |
| §III / p3-p5 | SMP abstraction | `ReceiveTx`, `ShareTx`, `MakeProposal`, `FillProposal`; microblock/proposal/block; SMP-Inclusion and SMP-Stability | 抽象定义 | 明确 shared mempool 不改变 committed order，因此不破坏 consensus safety |
| §III-E / p4-p5 | Challenges | best-effort SMP 会有 missing transactions；client load 可能严重 skew | 问题设定 | missing tx 会触发 view changes 或把 fetch 压力转回 leader |
| §IV / p5-p7 | PAB | push phase 收集 `q` 个 ack 生成 proof；recovery phase 从 proof signers 拉取 microblock；`q` 在 `f+1` 到 `2f+1` 间可调 | 核心机制 | Lemma 1, Theorem 1/2 |
| §IV-B / p6-p7 | Stratus integration | leader proposal 包含 microblock ids 和 proofs；replica 验 proof 后进入 commit，并在后台 `FillProposal` 补齐 microblocks | 系统集成 | PAB 让缺失交易不阻塞 consensus critical path |
| §V / p7-p9 | Load balancing | busy replica 用 Power-of-d choices 采样 proxy；proxy 代表 sender 跑 PAB push phase；banList 规避不响应 proxy | 核心机制 | 工作负载估计基于 stable time |
| §VI / p9-p10 | Implementation | Go + Bamboo; 替换 Bamboo mempool；集成 HotStuff/PBFT/Streamlet；新增约 1,300 行 Go | 实现证据 | PAB proof 实现用 concatenated ECDSA signatures |
| §VII-A/B / p10-p12 | Setup and scalability | Alibaba Cloud; LAN/WAN; 128-byte transactions; batch-size sweep; 16-400 replicas; bandwidth table | 实证证据 | `N=128` 时 S-HS/SMP-HS 对 N-HS 约 5x |
| §VII-C / p12-p13 | Missing transactions | WAN fluctuation 下 SMP-HS throughput drops to zero；Byzantine senders 让 SMP-HS 随 Byzantine 数增加而急剧退化 | 鲁棒性证据 | S-HS 的 latency 基本平坦，因为缺失 microblocks 在后台恢复 |
| §VII-D / p13 | Unbalanced workload | Zipf skew 下 S-HS-dX 比 SMP-HS 高 5x 到 10x；`d=3` 最好但不同 d 差异不大 | load-balancing 证据 | 高 skew 时前 10% replicas 可收到 85%+ load |
| §VIII-IX / p13-p14 | Discussion/conclusion | Byzantine PAB/load balancing attacks, reconfiguration, garbage collection, multi-leader future work | 限制和扩展 | duplicate client attack 在 §III-A 中也列为 out of scope |
| Appendix / p16-p17 | Throughput model | LBFT leader proposal dissemination gives `C/(B(n-1))` upper bound; ideal shared mempool approaches `C/(2B)` for large `n` | 理论解释 | 模型是 idealized honest/synchronous capacity analysis |

## 一句话贡献

Stratus 把 leader-based BFT 的交易传播从 consensus ordering 中拆出来，用 shared mempool、provably available broadcast 和分布式负载均衡，让 leader 只排序 microblock ids，同时保证被 proposal 引用的数据最终可取回。

## 核心精读笔记

### 背景、动机与问题边界

论文针对的是 leader-based BFT consensus 在区块链中的 proposal-phase bottleneck。PBFT/HotStuff/Streamlet 这类协议为了避免冲突，通常由 leader 决定 proposal。问题在于 proposal 往往包含大批交易数据，而 commit phase 只传播签名、hash 等小消息。论文指出，优化 commit-phase message complexity 不能解决由 leader 发送大 proposal 造成的吞吐下降；Appendix A 用 workload model 说明，在 LBFT 中 leader 为确认一笔交易要向 `n-1` 个 replicas 发送交易数据，理想吞吐随 replica 数增加按比例下降。证据锚点: p1, p16。

Stratus 的路线不是 sharding、树状 relay 或 multi-leader，而是 shared mempool (SMP): 交易数据先由 replicas 分布式传播，leader proposal 只包含 transaction/microblock ids 和必要元数据。这样 leader 从“大数据广播者”变成“id ordering coordinator”。该做法保留 off-the-shelf leader-based consensus core，适合在已有 HotStuff/PBFT/Streamlet 风格系统中替换 mempool。证据锚点: p1-p4。

### Shared mempool 抽象

SMP 修改传统 mempool 的两个 primitive: `ReceiveTx(tx)` 接收交易，`MakeProposal()` 产生 proposal；并增加 `ShareTx(tx)` 传播交易、`FillProposal(p)` 由 proposal ids 填回交易数据。数据结构上，client 交易被 batch 成 microblocks，每个 microblock 的 id 由其中交易 ids 计算；leader 的 proposal 是 microblock id list 加 metadata；若本地 mempool 拥有所有 referenced microblocks，则 proposal 可以被填成 full block，否则是 partial block。证据锚点: §III-C/D p3-p4。

SMP 需要两个 liveness 属性: `SMP-Inclusion` 要求正确 replica 收到并验证的交易最终进入 proposal；`SMP-Stability` 要求正确 leader proposal 中包含的交易最终被所有正确 replicas 收到。论文强调，SMP 不改变 consensus 已提交交易的顺序，因此安全性仍由原 consensus protocol 负责；SMP 的难点是让 proposal 引用的数据最终可获得。证据锚点: §III-B p3。

### Missing transactions 为什么会成为 bottleneck

如果 `ShareTx` 只用 best-effort broadcast，Byzantine sender 可以只把某个 microblock 发给 leader，不发给其他 replicas。leader 将其 id 放入 proposal 后，non-leader replicas 会发现 referenced transaction 缺失。若为了 proposal integrity 阻塞 consensus，则可能触发频繁 view-change；若从 leader 主动 fetch 缺失数据，又把数据传播压力重新集中到 leader。论文在 §VII-C 的实验中展示，网络 fluctuation 下 basic SMP-HS 的 throughput 会降到 0，恢复也很慢。证据锚点: p4-p5, p12。

### PAB: availability proof 而不是 full reliable broadcast

Provably available broadcast (PAB) 的目标不是让每个 replica 在 proposal 前都已经有完整 microblock，而是让 proposal 中每个 id 都带有一个可验证的 availability proof。sender 广播 microblock `m`，收到至少 `q` 个 distinct acknowledgements 后，用 threshold signature 或实现中的签名拼接形成 proof `sigma`。因为 `q >= f+1`，valid proof 表明至少一个正确 replica 持有 `m`。收到 proof 但没有 `m` 的 replica 可以从 proof signers 中随机 fetch，最终拿到内容。证据锚点: §IV-A p5-p6, Lemma 1 p7。

`q` 是 `f+1` 到 `2f+1` 之间的可调参数。较大的 `q` 让 recovery phase 更容易从正确 replica 拉到数据，减少缺失 microblock；代价是 push phase 需要等待更多 acks，增加 latency。§VII-C 的 Byzantine-sender 实验显示 `S-HS-2f` 在 Byzantine replicas 增加时 throughput 更好，但 latency 更高。证据锚点: p6, p12-p13。

### Stratus 如何接入 leader-based BFT

Stratus 在 `MakeProposal(v)` 中从 `avaQue` 拉取已经有 availability proof 的 microblock ids，并把 proofs 一起 piggyback 到 proposal。收到 proposal 的 replica 先验证每个 proof；验证失败触发 view change，验证成功则进入 consensus commit phase，并独立启动 `FillProposal(p)` 在后台拉取缺失 microblocks。关键点是: 等待缺失 microblock 的线程不阻塞 consensus 事件线程；真正执行时仍要求之前 microblocks 已收到并执行，因此 ledger consistency 不被破坏。证据锚点: Algorithm 3 p6-p7。

Theorem 1 证明 Stratus satisfies SMP-Inclusion: 正确 replica 接收并验证的交易会 batch 成 microblock，经 PAB 产生 proof，最终被某个正确 leader 从 `avaQue` 提出。Theorem 2 证明 Stratus satisfies SMP-Stability: 正确 leader proposal 中的交易都有 valid proof，PAB-Provable Availability 保证每个正确 replica 最终收到交易。证据锚点: p7。

### 分布式负载均衡

Shared mempool 会把传播任务分散给所有 replicas，但现实中 client 可能集中把交易发给少数热门节点。Stratus 使用 distributed load balancing (DLB): busy replica 对每个新 microblock 用 Power-of-d choices 随机采样 `d` 个 replicas 的 load status，选择最不忙者作为 proxy。proxy 代替原 sender 运行 PAB push phase，产生 proof 后交回原 sender，由原 sender 接管 recovery phase。若 proxy 超时不返回 proof，sender 将其加入 banList 并重新选择 proxy。证据锚点: §V-A p7-p9。

Load status 的估计使用 stable time (ST): 从 sender 广播 microblock 到收到 `f+1` acks 的时间。replica 在最近稳定 microblocks 的窗口上取第 n 百分位作为 ST；ST 变大表示 replica 可能过载，ST 越小表示更适合帮忙传播。这个设计依赖论文对 private inter-datacenter network 的观测: 正常延迟在短窗口内相对稳定，过载时延迟会明显上升。证据锚点: §V-B p9。

### 实现与实验设置

实现基于 Go 和 Bamboo，替换 Bamboo 的 mempool，并集成 HotStuff、PBFT、Streamlet；论文称因接口设计，consensus core 只需最小修改。实现中 PAB proof 没有用 Boldyreva threshold signature，而是拼接 `f+1` 个 ECDSA signatures，理由是计算效率更好。Stratus-specific 优化包括 prioritizing consensus messages 和 token-based limiter 限制 microblock data messages，避免 data traffic 抢占 consensus resources。证据锚点: §VI p9-p10。

实验在 Alibaba Cloud ECS 上进行，LAN 模拟 national deployment，WAN 通过 NetEm 加 100ms inter-replica RTT 和 100Mb/s replica bandwidth。workload 是 Bamboo 的 in-memory key-value set 操作；latency 在 server side 从 replica 首次收到交易到 block commit 计算，不包括 client-replica 网络延迟；默认 workload 均匀分布，最后一组才使用 Zipf skew。证据锚点: §VII-A p10。

### 性能结果与解释

Batch-size 实验显示，microblock batch 越大越能 amortize PAB ack overhead，但 latency 也会增加；论文后续用小网络 `N <= 128` 的 128KB batch 和大网络 `N >= 256` 的 256KB batch 作为设置，并用 128-byte transaction payload。证据锚点: Figure 6 p11。

在 16 到 400 replicas 的 LAN/WAN 实验中，使用 shared mempool 的 SMP-HS、S-HS、S-PBFT、Narwhal 和 multi-leader MirBFT 都比 native HotStuff/PBFT 有更高 throughput。S-HS/SMP-HS 在 `N=128` 时相对 N-HS 约 5x，且随着网络规模增大差距扩大。S-HS 与 SMP-HS 在均匀/无攻击环境下接近，说明 PAB overhead 在大 batch 下可被摊薄。证据锚点: Figure 7 p11-p12。

Table III 说明 bandwidth bottleneck 的转移: 在 `N=64`、每 replica 100Mb/s 限速时，N-HS 的 leader outbound 约 75.4Mb/s，而 non-leader 只有 0.5Mb/s；S-HS 中 leader 约 60.1Mb/s，non-leader 约 57.4Mb/s，负载更均衡。S-HS 比 SMP-HS 多约 10% outbound overhead，换来 availability insurance。证据锚点: Table III p12。

Missing-transaction 实验显示，在 WAN fluctuation 的 10 秒窗口里，SMP-HS throughput drops to zero，因为缺失交易从 leader fetch 造成拥塞并触发 view changes；S-HS 仍按网络速度推进，原因是 proposal proofs 允许 consensus 不在 critical path 等待 microblock 内容。Byzantine-sender 实验中，随着 Byzantine replicas 增加，SMP-HS 的吞吐/延迟急剧恶化；S-HS latency 基本平坦，`S-HS-2f` 在高 Byzantine 数下 throughput 更好但 latency 更高。证据锚点: Figure 8/9 p12-p13。

Skewed-load 实验用 Zipf1/Zipf10 模拟热门节点，论文指出在 100 replicas 且 `s=1.01` 时，10% replicas 收到超过 85% load。S-HS-dX 在全部实验中超过 SMP-HS 和 gossip-based SMP-HS-G；高 skew (`Zipf1`) 下，S-HS-dX 相比 SMP-HS 获得 5x (`N=100`) 到 10x (`N=400`) throughput。`d=3` 最好，但 `d=1/2/3` 的差距不大。证据锚点: Figure 10/11 p13。

### 攻击、限制和未来工作

PAB 防止的是 proposal 引用不可用数据导致 consensus 阻塞。若 Byzantine leader 把没有 proof 的 microblock 放入 proposal，replicas 会触发 view change，某些 PoS 链还可 slashing。若 Byzantine replicas 生成 proofs 但只发给少数节点，correct replicas 仍能通过 proof recovery 拉取数据。证据锚点: §VIII p13。

Load balancing 仍有攻击面: Byzantine sender 可向多个 proxies 发送同一 microblock 造成网络拥塞；论文建议 proxy broadcast 时带上 sender 对 `(mb.id, proxy identity)` 的签名，其他 replicas 可检测一个 sender 用多个 proxies 传播同一 microblock。恶意 replica 也可伪装 busy 把负载转嫁给别人，论文建议 availability proof 生产者奖励作为 incentive。证据锚点: §VIII p13-p14。

论文边界包括: 系统模型继承 BFT 的 `N >= 3f + 1` 和 partial synchrony；client duplicate attack 被列为 out of scope；实验没有纳入 application-specific verification/signature checks、execution 和 disk I/O；Stratus 当前针对 leader-based BFT，multi-leader extension 是 future work。证据锚点: §III-A p3, §VII-A p10, §IX p14。

## 层级分类

| 层级 | 候选 | 证据 | 状态 |
| --- | --- | --- | --- |
| L1 domain | `blockchain-systems` | blockchain consensus, permissioned blockchains, BFT-based PoS deployments | accepted |
| L2 direction | `mempool-and-networking` | transaction dissemination, shared mempool, client load, microblock broadcast | accepted |
| L3 topic | `shared-mempool` | SMP abstraction, PAB, DLB, Stratus | accepted |
| Secondary path | `distributed-systems/consensus/byzantine-fault-tolerance` | PBFT/HotStuff model, `N >= 3f+1`, Byzantine replicas, view change | accepted as bridge |
| Secondary path | `blockchain-systems/consensus/leader-based-bft-scaling` | leader-based BFT ordering core and consensus/mempool split | accepted as cross-direction bridge |

## 与现有 Nahida 笔记的关系

- 扩展 [[byzantine-fault-tolerance|Byzantine fault tolerance]]: Stratus 不改 BFT safety core，而是把 transaction dissemination 从 leader-based ordering core 外移。
- 扩展 [[blockchain-consensus|Blockchain consensus]]: 对 HotStuff/PBFT 类 leader-based BFT 增加 mempool/consensus split 视角。
- 新建 [[shared-mempool|Shared mempool]] 和 [[shared-mempool|Provably available broadcast]]: 用作后续 Narwhal/Tusk、Leopard、DAG mempool、Block-STM/parallel execution 前置概念。
- 与 [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt]] 的架构呼应: Cobalt 把治理和交易排序拆开；Stratus 把交易传播和排序拆开。二者都说明区块链系统的性能/治理问题不一定要塞进同一个 consensus primitive。

## Evidence Table

| Claim / observation | Source location | Claim type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Shared mempool decouples transaction dissemination from leader-based BFT ordering | Abstract, §I, §III p1-p4 | architecture | high | explicit |
| SMP requires SMP-Inclusion and SMP-Stability | §III-B p3 | definition | high | exact properties |
| Best-effort SMP can stall on missing transactions or overload leader fetch path | §III-E p4-p5, §VII-C p12 | mechanism/risk | high | supported by experiment |
| PAB proof means at least one correct replica holds the microblock | §IV-A p5-p6, Lemma 1 p7 | protocol theorem | high | depends on `q >= f+1` |
| Stratus lets consensus enter commit before missing microblocks are fetched | §IV-B p6-p7 | mechanism | high | background recovery thread |
| DLB uses Power-of-d choices, proxy forwarding, banList, and stable-time estimation | §V p7-p9 | mechanism | high | Algorithm 4 and Figure 4 |
| S-HS/SMP-HS achieve about 5x N-HS throughput at `N=128` | §VII-B p11-p12 | empirical_result | high | Figure 7 text |
| S-HS avoids the SMP-HS zero-throughput collapse during 10s WAN fluctuation | §VII-C p12 | empirical_result | high | Figure 8 text |
| S-HS-dX improves skewed-workload throughput 5x to 10x over SMP-HS under Zipf1 | §VII-D p13 | empirical_result | high | Figure 11 text |
| Stratus does not evaluate app-specific verification, execution, disk I/O, or client duplicate attacks | §III-A p3, §VII-A p10 | limitation | high | explicit exclusions |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| Stratus is designed as a mempool replacement that can be integrated with existing leader-based BFT cores such as HotStuff, Streamlet, and PBFT without redesigning the consensus protocol. | `arxiv:2203.05158#p2`<br>`arxiv:2203.05158#p9-p10` | folded_into_meta_note |
| Under the paper's Zipf-skew workload experiments, Stratus' distributed load balancing improves throughput by about 5x at 100 replicas and 10x at 400 replicas over basic SMP-HS for the highly skewed Zipf1 setting. | `arxiv:2203.05158#p13` | folded_into_meta_note |
| Stratus balances skewed client load by having busy replicas use Power-of-d choices over sampled stable-time estimates, forward excess microblocks to proxies, and retry through a banList when proxies fail to return proofs. | `arxiv:2203.05158#p7-p9` | folded_into_meta_note |
| In the paper's network-fluctuation and Byzantine-sender experiments, Stratus keeps consensus progressing despite missing microblocks because proposal references carry availability proofs and recovery runs off the critical path. | `arxiv:2203.05158#p12-p13` | folded_into_meta_note |
| Stratus' provably available broadcast attaches availability proofs to proposed microblock IDs, guaranteeing that a valid reference can eventually be recovered from at least one correct replica. | `arxiv:2203.05158#p5-p7` | folded_into_meta_note |
| PAB's quorum parameter can vary between `f+1` and `2f+1`, trading faster proof generation against fewer recovery fetches and better throughput under Byzantine senders. | `arxiv:2203.05158#p6`<br>`arxiv:2203.05158#p12-p13` | folded_into_meta_note |
| Stratus is scoped to leader-based BFT protocols under the standard `N >= 3f + 1` partially synchronous model, and the paper excludes client duplicate attacks plus application-specific verification, execution, disk I/O, and multi-leader extension. | `arxiv:2203.05158#p3`<br>`arxiv:2203.05158#p10`<br>`arxiv:2203.05158#p14` | folded_into_meta_note |
| Stratus uses a shared mempool abstraction to decouple transaction-data dissemination from leader-based BFT ordering, so the leader proposes microblock IDs rather than broadcasting full transaction payloads. | `arxiv:2203.05158#p1-p4` | folded_into_meta_note |
| In the paper's 64-replica bandwidth experiment, Stratus shifts outbound bandwidth from a leader-dominated pattern to a more balanced leader/non-leader pattern, with about 10% overhead over basic SMP for PAB acknowledgements. | `arxiv:2203.05158#p12` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `stratus-shared-mempool-decouples-dissemination-from-ordering`
- `stratus-pab-provides-provable-availability-for-proposal-references`
- `stratus-pab-quorum-parameter-trades-latency-for-recovery`
- `stratus-load-balancing-uses-stable-time-and-power-of-d-choices`
- `stratus-integrates-with-leader-based-bft-with-minimal-core-changes`
- `stratus-smp-rebalances-leader-and-non-leader-bandwidth`
- `stratus-pab-prevents-missing-transactions-from-blocking-consensus`
- `stratus-load-balancing-improves-skewed-workload-throughput`
- `stratus-scope-is-leader-based-partially-synchronous-bft`

### Concepts and maps to create/update

- Create [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Stratus]] concept as source-backed protocol seed.
- Create/update [[shared-mempool|Shared mempool]] concept and topic map.
- Create [[shared-mempool|Provably available broadcast]] concept.
- Create [[shared-mempool|Distributed load balancing for shared mempools]] concept.
- Create [[mempool-and-networking|Mempool and networking]] direction map under `blockchain-systems`.
- Refresh [[blockchain-systems|Blockchain systems]], [[blockchain-consensus|Blockchain consensus]], [[byzantine-fault-tolerance|Byzantine fault tolerance]].

### Synthesis handoff

- Create [[shared-mempool|Shared mempool state 2026-06-11]] as topic-state seed.
- Create [[bft-consensus-to-shared-mempool-scaling|BFT consensus -> shared mempool scaling]] bridge.
- Queue direct absorption of Narwhal/Tusk, Leopard, MirBFT, Kauri, HotStuff, and a stable BFT/partial-synchrony source before making the direction `foundation_ready`.

## Limitations and Review Items

- `metadata_review`: queue hint title mismatched the local PDF; durable note uses the PDF header title and keeps the mismatch as provenance.
- `direct_source_needed`: Narwhal/Tusk should be processed as its own paper before comparing DAG mempool designs as settled knowledge.
- `scope_boundary`: Stratus targets leader-based partially synchronous BFT; it is not a general asynchronous consensus protocol and not a multi-leader protocol.
- `evaluation_scope`: benchmark excludes app-specific signature verification, transaction execution, disk I/O, and client network latency.
- `security_scope`: duplicate client attack and richer proxy reputation/incentive mechanisms are left to future work.
