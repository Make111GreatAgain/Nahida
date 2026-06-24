---
id: "sha256-662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
title: "OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding"
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
  - "p1-p2 abstract, introduction, contributions, background"
  - "p3-p4 system/network/threat model and design roadmap"
  - "p4-p7 security design: randomness, shard transition, Atomix"
  - "p7-p9 performance design: ByzCoinX, state blocks, trust-but-verify"
  - "p9-p12 security analysis, implementation, evaluation"
  - "p12-p16 related work, limitations, conclusion, appendices"
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown"
year: "2017"
local_pdf: "~/Desktop/paper/OmniLedger.pdf"
sha256: "662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
pages: 16
pdf_extractor: "pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "scaling-and-sharding"
topic_ids:
  - "sharded-ledgers"
  - "cross-shard-transactions"
  - "byzantine-fault-tolerance"
ontology_path:
  - "blockchain-systems"
  - "scaling-and-sharding"
  - "sharded-ledgers"
primary_ontology_path: "blockchain-systems/scaling-and-sharding/sharded-ledgers/sha256-662f70f3c28a"
secondary_ontology_paths:
  - "blockchain-systems/consensus/byzantine-fault-tolerance/sha256-662f70f3c28a"
  - "distributed-systems/consensus/byzantine-fault-tolerance/sha256-662f70f3c28a"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
  directions:
    - "scaling-and-sharding"
    - "consensus"
  topics:
    - "sharded-ledgers"
    - "cross-shard-transactions"
    - "byzantine-fault-tolerance"
domains:
  - "blockchain-systems"
topics:
  - "sharded-ledgers"
  - "omniledger"
  - "atomix"
  - "byzcoinx"
aliases:
  - "OmniLedger"
  - "Secure scale-out ledger via sharding"
  - "Atomix"
  - "ByzCoinX"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "sharding"
  - "distributed-ledger"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "scaling"
    - "sharding"
  problem:
    - "scale-out distributed ledger"
    - "cross-shard atomic commit"
    - "secure validator assignment"
  method_family:
    - "sharded ledger"
    - "BFT shard consensus"
    - "client-driven atomic commit"
    - "distributed randomness"
  system_layer:
    - "validator assignment"
    - "transaction execution"
    - "intra-shard consensus"
    - "state checkpointing"
  evaluation_context:
    - "DeterLab prototype"
    - "Bitcoin UTXO trace"
  application:
    - "permissionless payment ledger"
  bridge:
    - "distributed BFT to sharded ledgers"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-omniledger"
safe_for_absorption: true
source_refs:
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "pdf:~/Desktop/paper/OmniLedger.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "scaling-and-sharding"
secondary_directions:
  - "consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract identify scale-out distributed ledger via sharding"
  - "Sections IV-V focus on shard assignment, cross-shard transactions, ByzCoinX, state blocks"
  - "Evaluation measures throughput scaling by shard count"
taxonomy_version: "1.0"
---

# OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding

## 论文身份

- 标题: OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding
- 作者: Eleftherios Kokoris-Kogias, Philipp Jovanovic, Linus Gasser, Nicolas Gailly, Ewa Syta, Bryan Ford
- 机构: EPFL, Trinity College
- 会议/期刊: unknown in local PDF extraction
- 年份: 2017, based on local queue/PDF timestamp; venue year needs external bibliographic verification
- DOI: unknown
- arXiv: unknown
- 链接: unknown
- 本地 PDF: `~/Desktop/paper/OmniLedger.pdf`
- SHA-256: `662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb`
- 代码: paper states the Go implementation combines RandHound/ByzCoin code available on GitHub, but this PDF extraction does not provide repository URLs.
- 数据: evaluation uses the first 10,000 Bitcoin blocks and DeterLab; exact dataset artifact URL unknown.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 16
- 已覆盖章节/页码: Abstract, I-XI, Appendix A-D, references scanned for relation context
- 已检查附录: A anti-censorship sketch, B network-model fallback, C cross-shard probability, D Atomix for stateful objects
- 未覆盖章节/页码: none
- Extraction gaps: venue/DOI/arXiv/code URL not present in extracted metadata; figure images are read through captions and surrounding text, not visual inspection.
- 精读说明: 这是 protocol/systems paper，重点读取了威胁模型、协议流程、安全论证、实现和评估结果；数值 claim 只采用正文/表格可见数字。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, I / p1-p2 | 问题与贡献 | 目标是 permissionless decentralized ledger 的 scale-out；提出 representative shards、Atomix、ByzCoinX、state blocks、trust-but-verify | high | 摘要包含核心 claim 与评估摘要 |
| II / p2-p3 | 背景 | ByzCoin/CoSi、UTXO、RandHound、VRF sortition、Sybil-resistant identities、Elastico 缺口 | high | 解释 OmniLedger 的依赖 |
| III / p3-p4 | 模型与路线图 | n validators、m shards、epochs、synchronous/partially synchronous split、f <= n/4、mildly adaptive adversary、设计目标 | high | 决定适用边界 |
| IV-A / p4-p5 | Secure sharding | RandHound + VRF leader election 产生 bias-resistant randomness，再把 validators 分配到 shards | high | 核心安全机制 |
| IV-B / p5 | Epoch transition | 每个 epoch 只逐批替换 shard 中 validators，保持服务可用 | medium-high | liveness 风险与 churn 处理 |
| IV-C / p5-p7 | Atomix | client-driven lock/unlock cross-shard atomic commit；proof-of-acceptance/rejection；无直接 shard-to-shard 通信 | high | 可复用 protocol claim |
| V-A/V-B / p7-p8 | ByzCoinX and blockDAG | group-based communication 提高 fault tolerance；UTXO dependency analysis 支持 parallel block commitments | high | intra-shard performance layer |
| V-C / p8 | State blocks | per-shard ordered Merkle UTXO state block，降低 bootstrap/storage；clients 保存 proof-of-existence | high | 存储与同步机制 |
| V-D / p8-p9 | Trust-but-verify | optimistic validators 快速给低价值交易 provisional confirmation，core validators 后续 re-validation | high | 明确 trade-off |
| VI / p9-p10 | Security analysis | randomness leader bias bound、shard-size binomial model、epoch union bound、group communication probability | high | mostly informal/pragmatic |
| VII-VIII / p10-p12 | Implementation and evaluation | Go prototype；DeterLab；1800 hosts；throughput/latency/epoch transition/Atomix/ByzCoinX/state block experiments | high | 实证 claim 来源 |
| IX-XI / p12-p13 | Related, limitations, conclusion | 与 RSCoin/Elastico/ByzCoin/Bitcoin-NG/Chainspace 比较；proof-of-concept、incentives/adaptivity/locality limitations | high | 边界和后续任务 |
| Appendix A-D / p14-p16 | 补充协议和概率 | anti-censorship sketch、fallback randomness、cross-shard probability、stateful Atomix | medium | 多数为 sketch/future-work level |

## 一句话贡献

OmniLedger 将 permissionless ledger 的 sharding 问题拆成 secure validator assignment、cross-shard atomic commit、robust intra-shard BFT、state checkpointing 和 optimistic validation，试图在不放弃去中心化与长期安全的前提下实现吞吐随 validator/shard 数量增长。

## 核心精读笔记

### 背景、动机与问题边界

论文认为多数 distributed ledgers 不能真正 scale-out：即使把 Nakamoto consensus 替换为 PBFT 类协议，所有 validators 仍然重复验证和处理所有交易，因此总处理容量不会随着参与者增加而增加。数据库领域的 sharding 可以把状态分区给不同参与者并行处理，但开放式 distributed ledger 的 sharding 同时引入三个难题: 如何安全随机地把 validators 分配到 shards，如何让任何一个 shard 在长期运行中被攻破的概率可忽略，以及如何让跨 shard 交易保持原子性。

OmniLedger 的目标不是仅提高单个共识组吞吐，而是实现 `scale-out`：系统总吞吐随着活跃 validators/shards 增加而近似线性增长。它明确把安全、去中心化和扩展性放在同一个三角中，与 RSCoin、Elastico、ByzCoin 等系统比较，声称 prior systems 通常只能取其中两项。

### 模型、假设与定义

系统有 `n` 个 validators，均匀分布在 `m` 个 shards 中；一个 epoch 是两次全局 reconfiguration 之间的固定时间，例如一天。Shard 内部处理客户端交易并维护该 shard 的 ledger/state。Validators 可以通过 PoW、PoS、PoB、proof-of-personhood 等 Sybil-resistant mechanism 创建身份并写入 identity blockchain。

网络模型分两层: shard assignment 这类慢操作使用 honest validators 之间同步且有已知最大延迟 `Delta` 的假设；epoch 内部的共识因为目标是秒级延迟，使用 PBFT 类 partially synchronous model 和 optimistic/increasing timeouts。威胁模型假设最多 25% validators Byzantine，即 `n = 4f`；也提到系统在接近 1/3 Byzantine 时性能降级。对手是 epoch 粒度的 mildly adaptive adversary，不能瞬时腐化 validators；加密原语安全且 CDH hard。

这些假设非常关键：OmniLedger 的安全结论不应外推到高度 adaptive adversary、无限制网络分区、或没有 Sybil-resistant identity 的场景。

### 安全分片: RandHound + VRF leader election

OmniLedger 不依赖 trusted randomness beacon，也不把随机性绑定到 PoW hash 低位。它要求 randomness generation 具备 unbiasability、unpredictability、third-party verifiability 和 scalability。论文使用 RandHound 产生分片随机数，但 RandHound 需要 leader，因此用 VRF-based leader election 解决 leader 选择。

每个 epoch 开始时，validator `i` 计算 `ticket_i,e,v = VRF_sk_i("leader" || config_e || v)`，validators gossip tickets，在 `Delta` 后锁定最小有效 ticket 对应的 leader。如果 leader 在另一个 `Delta` 内不启动 RandHound，就在本 epoch 排除该 validator 并增加 view 重新抽签。RandHound 成功后，leader 广播 `rnd_e` 和 proof，validators 验证后用它生成全体 validators 的 permutation，并分入约等大小的 shards。

安全直觉是: 每个 validator 每 view 只能生成一个有效 ticket；honest private keys 未知使 honest tickets 不可预测；adversary 若赢得 leader lottery 只能接受当前随机数或拒绝并冒险重抽。连续控制 `a` 个 leaders 的概率以 `(f/n)^a` 下降。论文后续用 `1/4^n` 给出 25% adversary 下连续控制 leader 的上界。

### Epoch transition 与 validator churn

若每个 epoch 都把所有 validators 重新分配，系统会在 bootstrapping 期间停顿。OmniLedger 因此只逐批替换每个 shard 的 validators，固定 `k < 1/3 * n/m`，论文选择 `k = log(n/m)`。每个 shard 用 `H(j || rnd_e)` 决定既有 validators 的 batch permutation，用 `H(0 || rnd_e)` 打散新加入 validators，并按批次间隔 `Delta` 逐步替换。

这个设计试图保持 shard 内至少 `2/3` honest/up-to-date validators 可以继续服务。其代价是 epoch transition 安全依赖 mildly adaptive adversary 和 bootstrapping 时间；论文在 limitations 中承认 day-long epochs 与高度 adaptive adversary 不匹配。

### Atomix: cross-shard atomic commit

Atomix 面向 UTXO 模型，是 client-driven 的 Byzantine shard atomic commit。协议分三步:

1. Initialize: client 创建 cross-shard transaction，inputs 位于若干 input shards，outputs 位于若干 output shards，并 gossip 给 input shards。
2. Lock: 每个 input shard 验证该交易。若有效，则把 input UTXO 标为 spent/locked、把交易写入 shard ledger，并给出 proof-of-acceptance；若拒绝，则给出 proof-of-rejection。Proof 是相对包含该交易 block 的 signed Merkle proof。
3. Unlock: 若所有 input shards 都接受，client 或任何其他实体 gossip unlock-to-commit transaction 到 output shards；若至少一个 input shard 拒绝，则 client 或其他实体 gossip unlock-to-abort transaction 给 input shards，让已锁资金恢复 spendable。

论文强调 Atomix 不需要 shard-to-shard communication，把协调责任放到 client 或替代实体上，换来 shard 逻辑简单。安全性来自 shards 本身通过 BFT consensus collectively honest，且每个 input shard 对一个 input UTXO 只给出 acceptance/rejection 中的一种。若 client 崩溃，资金可能保持锁定，除非其他实体基于 gossip 信息代为提交 unlock；论文建议可让最小 input UTXO 的 shard 作为 coordinator，并由 `f+1` validators 发送 unlock transaction。

Atomix 的证明大小依赖 ByzCoinX collective signatures。如果没有 collective signatures，100 validators shard 的 regular signatures 约 9 KB，而 collective signature 只有 77 bytes，unlock transaction 会更接近 practical。

### ByzCoinX 与并行 block commitments

ByzCoin 用 tree communication 获得可扩展性，但故障时回退到 flat/all-to-all 模式，性能会被 Byzantine DoS 利用。ByzCoinX 在每个 shard 内把 validators 随机分成若干 groups，leader 对每组随机选择 group leader；若 group leader 超时则重选。Shard leader 收到超过 `2/3` validators acceptances 后推进下一阶段；若 shard leader 失败，validators 走 PBFT-like view change。

ByzCoinX 还利用 UTXO 模型并行化 block commitments。两个交易只有在花费同一 UTXO，或一个交易消费另一个交易新建 UTXO 时需要排序；其他交易可以放入不同 blocks 并并行 commit。论文采用 blockDAG，每个 block 可有多个 parent/backpointer，用 transitive dependencies 降低直接 backpointer 数量。

### State blocks 与 ledger pruning

高吞吐 ledger 的历史增长很快，Visa 级别系统按 4000 tx/s、500 B/tx 估算可达每日 150 GB。OmniLedger 因此引入 state blocks，类似 PBFT stable checkpoints。每个 epoch 结束时，shard leader 把当前 UTXOs 存入 ordered Merkle tree，把 root hash 放到 state block header，validators 对 header 达成共识。State block 成为下一个 epoch 的 genesis/reference point，旧 state block body 可丢弃，常规 blocks 至少保留到下一 epoch 结束以支持 transaction proofs。

由于只保存 state block headers，过去交易存在性的证明由 clients 负责保存。Proof 包含交易所在 regular block 的 Merkle proof，以及从 state block 到 regular block 的 header sequence；state blocks 可用 skipchain-like multi-hop backpointers 缩短证明。

### Trust-but-verify validation

在强 adversary 假设下，shards 要大，低延迟交易会变慢。OmniLedger 增加 optional trust-but-verify: optimistic validators 先以较小 group 低延迟处理低价值交易，提供 provisional commitment；core validators 随后重新验证 optimistic blocks，发现不一致时排除坏交易并追责签名 validators。

这个机制不是免费安全升级，而是显式 trade-off。低价值交易可接受 optimistic assurance；高价值交易应等待 core validation/finality。论文指出惩罚机制和激励设计细节超出范围，因此不能把 trust-but-verify 视作已形式化的 economic security。

### 安全分析

论文把贡献称为 pragmatic rather than theoretical。Randomness 部分说明 dishonest RandHound leader 不能偏置输出，但可选择 withholding 并重启；VRF lottery 将连续控制 leader 的概率限制为 `1/4^n`。Shard-size 部分把 shard compromise 视为从总体中随机抽取 malicious validators 的 binomial distribution；epoch security 用 union bound 近似多个 shards 的总失败概率。文中给出例子: 12.5% adversary、16 shards 时 one-day epochs 的 failure probability 为 `4 * 10^-5`，约 68.5 年一次。

Group communication 部分计算 `N=600`、`sqrt(N)=25` groups 时 leader 找到 honest group leaders 的概率，强调失败不是安全破坏，而是当前 shard leader 协调失败，需要 elect new shard leader。

### 实现与评估

OmniLedger 原型使用 Go 实现，组合 RandHound code、VRF leader election、ByzCoin extension、Atomix client。实验在 DeterLab 上运行，60 台物理机，每台 Intel E5-2420 v2、24 GB RAM、10 Gbps link；所有连接限制到 20 Mbps，延迟设为 100 ms；交易数据基于 Bitcoin 前 10,000 blocks。

主要结果:

- 1800 hosts 下，trust-but-verify throughput 比 regular validation 近一个数量级高；低风险交易可在几秒得到 optimistic confirmation，高风险交易等待两级验证仍小于一分钟。
- `f/n=12.5%`、shard size 70 时，shards 从 1 到 16，吞吐约 `439, 869, 1674, 3240, 5850` tps，近似线性增长。
- 1800 hosts、25 shards、12.5% adversary 时测得约 13,000 tps；若要在 25% adversary 下达到 Visa 平均 4000 tps，论文估计需要约 4200 hosts 和 7 shards，但实验平台未实测该配置。
- Epoch transition cost 主要来自 RandHound，1800 hosts 最坏情况下 10 次 RandHound 约 3 小时；如果 epoch 是一天，论文认为可接受。
- Atomix cross-shard transaction 的 end-to-end latency 约为 consensus latency 的近两倍，但随着参与 shards 增加只略增。
- ByzCoinX 从 1 个大 block 到 4 个并发小 blocks 时吞吐增加约 20%，per-block latency 降低约 35%；继续增加并发则加密操作开销抵消收益。
- State blocks 对 Bitcoin 前 100 天模拟中，离线超过 19 天后比全量重放省带宽；在 OmniLedger 高吞吐/day-long epoch 下收益更明显。

### 限制与未来工作

论文明确承认 OmniLedger 是 proof of concept。主要限制包括:

- Epoch bootstrap 成本按分钟甚至小时计，虽然不在普通交易 critical path，但对高度 adaptive adversary 不友好。
- 实际 throughput 依赖 workload locality；如果所有交易都触达所有 shards，一个 shard 反而更好。
- Anti-censorship 只有 protocol sketch，没有实现和完整保证。
- 没有形式化参与者 incentives，而开放匿名 cryptocurrency 中 honest/malicious 二分可能不现实。
- 不适合 highly adaptive adversaries，因为 epoch bootstrap 时间长且只能 day-long epochs。

## 可复用想法

- Sharded ledger 不是简单把状态分片；需要把 validator assignment、cross-shard commit、intra-shard consensus、state synchronization 和 client proof responsibility 一起设计。
- Cross-shard atomicity 可通过 client-driven proofs 规避 shard-to-shard coordination，但会把 liveness/recovery 责任转移给 client 或第三方 relayer。
- Scale-out claim 必须同时报告 workload assumptions；UTXO 随机分配下 cross-shard transaction 比例会压低理论 speed-up。
- State checkpointing 在高吞吐 ledger 中不仅是存储优化，也决定 validator churn 和 shard reassignment 是否可持续。
- Trust-but-verify 是 latency/security/economic-incentive trade-off，不应写成无条件 finality。

## 术语

| Term | 含义 | 来源 |
| --- | --- | --- |
| scale-out distributed ledger | 总处理能力随 validators/shards 增加而增长的 ledger | p1-p2 |
| shard | 由 validator subset 维护的一部分 ledger/state | p3-p4 |
| epoch | 两次 global reconfiguration 之间的时间窗口 | p3 |
| RandHound | scalable bias-resistant distributed randomness protocol | p2, p4-p5 |
| Atomix | OmniLedger 的 client-driven cross-shard atomic commit protocol | p5-p7 |
| ByzCoinX | OmniLedger 的 ByzCoin variant，用 group communication 和并行 block commitment 提高鲁棒性/吞吐 | p7-p8 |
| state block | shard state 的 Merkle checkpoint，用于 pruning/bootstrap | p8 |
| trust-but-verify validation | optimistic validators 先确认，core validators 后验证的低延迟机制 | p8-p9 |

## 连接

- 依赖/桥接: [[byzantine-fault-tolerance|Byzantine fault tolerance]], [[consensus|State machine replication]]
- 新概念: [[sharded-ledgers|Sharded ledgers]], [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger]], [[sharded-ledgers|Atomix]], [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|ByzCoinX]], [[sharded-ledgers|State blocks]]
- 新地图: [[scaling-and-sharding|Scaling and sharding]], [[sharded-ledgers|Sharded ledgers]]
- 新桥: [[bft-consensus-to-sharded-ledgers|BFT consensus -> sharded ledgers]]
- 相邻待补: Elastico, RSCoin, Chainspace, data availability sampling, modern Ethereum sharding/danksharding

## Evidence Table

| Claim | 位置 | 类型 | 证据强度 | 备注 |
| --- | --- | --- | --- | --- |
| OmniLedger aims to provide scale-out throughput without abandoning security/decentralization | Abstract, p1-p2 | design claim | high | dependent on assumptions and prototype evaluation |
| Shard assignment uses bias-resistant randomness from RandHound plus VRF leader election | IV-A, p4-p5 | mechanism/security | high | informal security argument |
| Gradual validator swapping avoids stopping transaction processing at epoch boundaries | IV-B, p5 | mechanism | medium-high | depends on honest/up-to-date quorum |
| Atomix provides cross-shard atomic commit with lock/unlock proofs | IV-C, p5-p7 | protocol | high | UTXO model focus |
| ByzCoinX group communication improves robustness over ByzCoin fallback behavior | V-A, p7 | mechanism | high | evaluated later |
| UTXO dependency analysis permits parallel block commitments through blockDAG | V-B, p7-p8 | mechanism | high | specific to UTXO dependencies |
| State blocks reduce storage/bootstrap costs through shard state checkpoints | V-C, p8 | mechanism | high | clients must keep proof-of-existence |
| Trust-but-verify lowers latency for low-risk transactions while core validators later verify | V-D, p8-p9 | trade-off | high | economic punishment not formalized |
| Throughput scales near-linearly with shard count in evaluation | Table II, p10-p11 | empirical result | high | 12.5% adversary, shard size 70 |
| OmniLedger is proof-of-concept and not suitable for highly adaptive adversaries | X, p13 | limitation | high | author-stated |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| Atomix makes cross-shard UTXO transactions commit or abort atomically by locking input shards and using proof-of-acceptance or proof-of-rejection unlock transactions, without direct shard-to-shard communication. | `sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb#p5-p7` | folded_into_meta_note |
| ByzCoinX modifies ByzCoin with group-based communication and UTXO dependency-aware blockDAG commitments to improve robustness under failures and enable parallel block processing within a shard. | `sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb#p7-p8` | folded_into_meta_note |
| OmniLedger's safety and scale-out claims are bounded by assumptions including at most about 25% Byzantine validators, mildly adaptive corruption at epoch granularity, Sybil-resistant identities, and workloads that do not force every transaction to touch all shards. | `sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb#p3-p4,p13,p15` | folded_into_meta_note |
| OmniLedger targets scale-out distributed-ledger throughput by assigning validators to statistically representative shards using bias-resistant distributed randomness and a VRF-based leader election process. | `sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb#p1-p5` | folded_into_meta_note |
| OmniLedger state blocks summarize each shard's UTXO state as a collectively agreed Merkle checkpoint, allowing old state bodies to be pruned and new validators to bootstrap without replaying the full ledger history. | `sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb#p8,p12` | folded_into_meta_note |
| In the OmniLedger prototype evaluation with 12.5% adversarial power and shard size 70, throughput grows from 439 tps at one shard to 5850 tps at sixteen shards, supporting the paper's scale-out claim under that workload and setup. | `sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb#p10-p11` | folded_into_meta_note |
| OmniLedger's trust-but-verify mode gives low-value transactions fast optimistic confirmations from small validator groups, while core validators later re-validate them for finality and accountability. | `sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb#p8-p11` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `[[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger combines sharding with bias-resistant randomness to target secure scale-out]]`
- `[[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|Atomix provides client-driven cross-shard atomic commit for UTXO ledgers]]`
- `[[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|ByzCoinX improves shard consensus robustness and parallelism]]`
- `[[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|State blocks prune shard ledgers and reduce validator bootstrapping]]`
- `[[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|Trust-but-verify trades low latency for delayed final validation]]`
- `[[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger prototype throughput scales nearly linearly with shard count]]`
- `[[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger security claims are bounded by mild adaptivity and workload assumptions]]`

### Concepts to create or update

- Create [[sharded-ledgers|Sharded ledgers]] as `foundation_thin` topic concept.
- Create [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger]] as protocol/system concept.
- Create [[sharded-ledgers|Atomix]] as cross-shard atomic commit concept.
- Create [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|ByzCoinX]] as shard-level BFT consensus variant concept.
- Create [[sharded-ledgers|State blocks]] as ledger pruning/checkpointing concept.
- Update [[byzantine-fault-tolerance|Byzantine fault tolerance]] and [[consensus|State machine replication]] later if broader sharded-ledger bridge needs more classical foundation.

### Maps and synthesis

- Create `vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md`.
- Create `vault/04_Knowledge/blockchain-systems/scaling-and-sharding/sharded-ledgers.md`.
- Update `vault/04_Knowledge/blockchain-systems.md`.
- Create `vault/04_Knowledge/blockchain-systems/scaling-and-sharding/sharded-ledgers.md`.
- Create bridge `vault/05_Bridges/bft-consensus-to-sharded-ledgers.md`.

### Review queue items

- Bibliographic metadata should be externally verified for venue/DOI.
- Elastico, RSCoin, Chainspace should be read directly before strong comparative synthesis.
- Modern sharding/data availability work should not be inferred from OmniLedger alone.

## Synthesis Handoff

OmniLedger is the first source for `blockchain-systems/scaling-and-sharding/sharded-ledgers`; it should initialize a topic synthesis rather than simply extend the existing consensus/finality synthesis. Parent `blockchain-systems` domain remains `foundation_thin` because only consensus/finality and sharding seeds are covered.
