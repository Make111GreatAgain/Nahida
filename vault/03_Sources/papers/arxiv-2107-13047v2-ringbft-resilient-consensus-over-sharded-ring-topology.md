---
id: "arxiv-2107.13047v2"
title: "RingBFT: Resilient Consensus over Sharded Ring Topology"
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
  - "p1-p2 abstract, introduction, BFT/sharding landscape, contributions"
  - "p2-p3 cross-shard dilemma and system model"
  - "p3-p6 RingBFT goals, single-shard consensus, cross-shard flow, algorithm"
  - "p7-p9 Byzantine attacks, retransmission, remote view-change, timers"
  - "p9-p10 no-deadlock, safety, and liveness guarantees"
  - "p10-p14 ResilientDB implementation and evaluation"
  - "p14-p16 related work and references scanned"
canonical_url: "https://arxiv.org/abs/2107.13047v2"
doi: ""
arxiv_id: "2107.13047v2"
venue: "arXiv"
year: "2022"
local_pdf: "~/Desktop/paper/RingBFT.pdf"
sha256: "ac7027175600fdaf83feb91b803276111c1ae64eb379feec972dfe60a06d1690"
pages: 16
pdf_extractor: "codex-bundled-python:pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/ringbft-ac7027175600-pages.txt"
code_url: "https://github.com/resilientdb/resilientdb"
project_url: "https://resilientdb.com/"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "scaling-and-sharding"
topic_ids:
  - "sharded-ledgers"
  - "byzantine-sharded-transactions"
ontology_path:
  - "blockchain-systems"
  - "scaling-and-sharding"
  - "sharded-ledgers"
primary_ontology_path: "blockchain-systems/scaling-and-sharding/sharded-ledgers/arxiv-2107.13047v2"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/arxiv-2107.13047v2"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "distributed-systems"
  directions:
    - "scaling-and-sharding"
    - "consensus"
  topics:
    - "sharded-ledgers"
    - "byzantine-sharded-transactions"
    - "cross-shard-consensus"
    - "byzantine-fault-tolerance"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "ringbft"
  - "sharded-ledgers"
  - "byzantine-sharded-transactions"
  - "cross-shard-consensus"
  - "permissioned-blockchain"
aliases:
  - "RingBFT"
  - "sharded ring topology consensus"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "sharding"
  - "byzantine-fault-tolerance"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "scaling-and-sharding"
    - "consensus"
  problem:
    - "cross-shard BFT consensus"
    - "cross-shard transactions in permissioned sharded blockchains"
    - "geographically distributed sharded consensus"
  method_family:
    - "meta-BFT protocol"
    - "ring topology"
    - "linear cross-shard communication"
    - "remote view-change"
  system_layer:
    - "shard-level consensus"
    - "cross-shard transaction ordering"
    - "blockchain fabric implementation"
  evaluation_context:
    - "ResilientDB"
    - "Google Cloud Platform 15 regions"
    - "YCSB workload"
    - "AHL and Sharper baselines"
  application:
    - "permissioned blockchain"
    - "federated data management"
  bridge:
    - "BFT consensus to sharded ledgers"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-ringbft"
safe_for_absorption: true
source_refs:
  - "arxiv:2107.13047v2"
  - "sha256:ac7027175600fdaf83feb91b803276111c1ae64eb379feec972dfe60a06d1690"
  - "pdf:~/Desktop/paper/RingBFT.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems/scaling-and-sharding"
secondary_directions:
  - "distributed-systems/consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract explicitly frame RingBFT as sharded ring-topology consensus"
  - "Sections 2-4 define cross-shard dilemma, system model, and RingBFT protocol"
  - "Sections 6-8 give guarantees and ResilientDB evaluation"
taxonomy_version: "1.0"
---

# RingBFT: Resilient Consensus over Sharded Ring Topology

## 论文身份

- 标题: RingBFT: Resilient Consensus over Sharded Ring Topology
- 作者: Sajjad Rahnama, Suyash Gupta, Rohan Sogani, Dhruv Krishnan, Mohammad Sadoghi
- 机构: Exploratory Systems Lab, University of California Davis
- 年份/版本: arXiv:2107.13047v2, 23 Mar 2022
- 链接: `https://arxiv.org/abs/2107.13047v2`
- 本地 PDF: `~/Desktop/paper/RingBFT.pdf`
- SHA-256: `ac7027175600fdaf83feb91b803276111c1ae64eb379feec972dfe60a06d1690`
- 代码/系统: `https://github.com/resilientdb/resilientdb`; `https://resilientdb.com/`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 16
- 已覆盖章节/页码: Abstract, Sections 1-10, references
- Extraction gaps: Figure 8/10 曲线的精确点值未从图中结构化提取；本笔记只记录正文明确给出的数值和趋势。论文是 arXiv PDF，未发现 DOI/会议元数据。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | permissioned blockchain + sharded replicated setting 中，cross-shard transactions 使 AHL/Sharper 等方案性能下降；RingBFT 以 ring order 和 process/forward/re-transmit 降低跨 shard 通信 | high |
| §2 / p2-p3 | Cross-shard dilemma | AHL reference committee 与 Sharper initiator shard 的通信瓶颈 | high |
| §3 / p3 | System model | 每个 shard 至少 `n >= 3f + 1`; deterministic transactions; known read/write sets; authenticated communication | high |
| §4.1 / p4 | Single-shard consensus | 单 shard 交易复用 PBFT 等 intra-shard BFT | high |
| §4.2-§4.3 / p4-p7 | RingBFT algorithm | initiator shard, ring order, locking, Forward/Execute messages, linear cross-shard primitive | high |
| §5 / p7-p9 | Uncivil executions | local timer, transmit timer, remote timer, retransmission, remote view-change | high |
| §6 / p9-p10 | Guarantees | Proposition 6.1, Theorems 6.2-6.4: no-deadlock, safety, liveness | high |
| §7 / p10 | Implementation | ResilientDB, parallel-pipelined architecture, partial-blockchain ledger layout | medium-high |
| §8 / p10-p14 | Evaluation | GCP 15 regions, YCSB, AHL/Sharper baselines, scale/batch/client/failure/dependency studies | high |
| §9-§10 / p14-p16 | Related work/conclusion | RingBFT relative to traditional BFT, permissionless sharding, ByShard and related ResilientDB work | medium |

## 一句话贡献

RingBFT 是面向 permissioned sharded blockchains 的 meta-BFT protocol：它让每个 shard 内部复用 PBFT 等 single-primary BFT，并让 cross-shard transactions 按 ring order 做 process, forward, and re-transmit，以线性跨 shard 通信取代 reference committee 或 all-to-all 交互。

## 核心精读笔记

### 问题背景

论文将问题放在 federated data management 和 permissioned blockchain 的交叉处。复制可以提高容错，但所有 replicas 都处理所有交易会限制吞吐；sharding 可以并行处理单 shard transactions，但 cross-shard transactions 需要多个 shards 对同一交易的顺序、锁和执行结果达成一致。

AHL 使用 reference committee 全局排序 cross-shard transactions，再通过 2PC 与 involved shards 交互；Sharper 使用 initiator shard primary 协调 involved shards，但需要 involved shards 的 replicas 做 all-to-all communication。RingBFT 试图避免这两种中心化或二次通信开销。

### 模型与假设

系统有 shard 集合 `S`，每个 shard 管理独立数据分区并由 replica set 复制。每个 shard 内最多有 `f` 个 Byzantine replicas，要求每个 shard 满足 `n >= 3f + 1`。这个阈值是 shard-local 的，不要求全系统 Byzantine replicas 少于总 replicas 的三分之一。

RingBFT 假设交易是 deterministic transactions：交易开始共识前，读/写数据项和 involved shards 已知。每个 cross-shard transaction 可能是 simple，也可能是 complex。simple cst 中各 shard 可独立执行 fragment；complex cst 有跨 shard 数据依赖，需要跨 shard 传递 read/write sets。

通信使用 authenticated messages。intra-shard communication 使用 MAC；cross-shard communication 使用 digital signatures，以获得 non-repudiation。RingBFT 使用 collision-resistant hash `H(.)` 检查 message digest。

### Ring order 与 transaction flow

RingBFT 将 shards 逻辑排列为 ring，每个 shard 有 identifier。对一个 cst，involved shards 中 ring order 第一个 shard 是 initiator shard。client 将 transaction 发送给 initiator shard primary；该 shard 先本地运行 PBFT 式 consensus，成功后锁定本地 read/write set，再将 Forward message 发送给 ring order 中下一个 involved shard。

每个后续 shard 重复本地 consensus、锁定数据并 forward。simple cst 在一轮 ring traversal 后即可执行；complex cst 在第一轮锁住数据后，第二轮通过 Execute messages 传播 updated write sets，解决跨 shard 依赖并完成执行。论文声称 deterministic cst 最多需要两轮 ring rotations。

### 线性跨 shard 通信

RingBFT 的关键通信 primitive 是: shard `S` 的每个 replica 只向下一个 shard `U` 中相同 identifier 的 replica 发送 message。因此 shard 间只交换 `n` 条消息，而不是 AHL/Sharper 式二次通信。为了证明前一 shard 已完成本地 consensus，Forward message 携带来自 `nf` 个 distinct replicas 的 signed Commit messages。

收到 Forward 的 replica 会在本 shard 内 locally share 该 message。若一个 replica 收到来自前一 shard 至少 `f + 1` 个 distinct replicas 的 valid Forward messages，且其中包含 `nf` 个 commit signatures 的证明，就可以让本 shard primary 启动本地 consensus。

### 并发、锁和 deadlock

RingBFT 允许 replicas out-of-order 处理 Prepare/Commit messages，但要求按 transactional sequence order 获取锁。每个 replica 维护 `kmax` 和 pending list `pi`：当序号大于 `kmax + 1` 时，transaction 先进入 pending；只有前序交易已锁定/释放且不存在 lock conflict，后续交易才能继续。

deadlock 避免依赖统一 ring order。若两个冲突 transactions 都访问 shards `S` 和 `U`，且 `id(S) < id(U)`，它们都会先在 `S` 处被 initiator ordering 排出不同 sequence numbers。较大 sequence transaction 在 `S` 的 pending/lock 规则中等待，因此不能在 `U` 形成反向锁等待。

### 异常与恢复

RingBFT 区分本地 BFT 故障和 cross-shard attacks。local timer 检测 shard 内 primary 未能成功复制交易并触发 PBFT view-change；transmit timer 让前一 shard 在 no communication attack 下重新发送 Forward；remote timer 让后一 shard 在 partial communication attack 下发送 RemoteView message 给前一 shard。如果前一 shard 收到来自后一 shard `f + 1` 个 RemoteView messages，就启动本地 view-change。

论文强调 safety 在 asynchronous setting 下成立，但 liveness 需要 periods of synchrony。timer 顺序为 local 最短、remote 次之、transmit 最长，以避免 recovery 机制相互干扰。

### 实现与实验

RingBFT 实现在 ResilientDB 上。ResilientDB 使用多 input/output threads、按消息类型拆分 work queues、batching/certify/worker/checkpoint/execute threads 来流水线处理共识任务。sharded ledger 中每个 shard 维护自己的 partial-blockchain；cross-shard block 会出现在所有 involved shards 的 ledger 中。若两个 blocks 含有冲突交易且访问相交 shard set，则各 ledger 中的相对顺序保持一致。

实验使用 GCP 15 个区域，16-core N1 replicas，YCSB workload，AHL 与 Sharper 为 baseline。默认设置为 30% cross-shard transactions、15 shards、每 shard 28 replicas，总计 420 globally distributed replicas；最多 50K clients；batch size 100。

正文报告的关键结果包括:

- 15 shard 设置下，RingBFT 的 throughput 比 AHL 高 16x，比 Sharper 高 4x；从 3 到 15 shards，latency 从 1.17s 增到 6.82s，但 throughput nearly constant。
- 在每 shard replicas 从 10 增到 28 时，RingBFT 仍有最高吞吐，但由于 intra-shard PBFT 的二次通信和 Forward proof 变大，throughput 下降。
- 0% cross-shard workload 时，三种协议都退化为 PBFT single-shard flow，可在约 500 nodes 达到 1.2M txn/s；100% cross-shard workload 下，RingBFT 相比 Sharper/AHL 分别有 4x/18x 更高 throughput 和 3.3x/7.8x 更低 latency。
- batch size 增大可减少 consensus instances；RingBFT throughput 从 batch 10 到约 1.5K batch 提升最高 27x，但延迟随 ring processing time 增加。
- primary failure 实验中，三个 shards primary 在 10s 失败，20s timeout，30s 新 view，35s throughput 开始恢复，约 55s 回到正常；期间 throughput 下降约 15%。
- complex cst 实验中，64 个 remote operations 分布在 15 shards 时，RingBFT 仍有至少 45K txn/s；论文未将 Sharper/AHL 纳入该图，因为它们对 complex cst 的支持不在对应论文覆盖范围内。

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| RingBFT assumes each cross-shard transaction's involved shards and read/write sets are known before consensus, so its protocol does not directly cover dynamic access-set discovery or unrestricted smart-contract execution. | `arxiv:2107.13047v2#p2-p4,p11` | folded_into_meta_note |
| In the RingBFT paper's ResilientDB evaluation, RingBFT scales to hundreds of globally distributed replicas and outperforms AHL and Sharper on cross-shard workloads, including reported gains up to 18x over AHL and 4x over Sharper. | `arxiv:2107.13047v2#p1-p2,p10-p14` | folded_into_meta_note |
| RingBFT reduces cross-shard communication to a linear neighbor-to-neighbor pattern by having each replica in one shard send a Forward or Execute message only to the matching-identifier replica in the next shard. | `arxiv:2107.13047v2#p5-p6` | folded_into_meta_note |
| RingBFT is a meta-BFT protocol for permissioned sharded blockchains: each shard may use an existing single-primary BFT protocol internally, while cross-shard transactions progress through involved shards in a prescribed ring order. | `arxiv:2107.13047v2#p2-p5` | folded_into_meta_note |
| RingBFT handles Byzantine primaries and cross-shard communication failures with local view-change, periodic checkpoints, transmit-timer retransmission, and remote view-change requests from the next shard. | `arxiv:2107.13047v2#p7-p9` | folded_into_meta_note |
| RingBFT avoids cross-shard deadlock by forcing conflicting cross-shard transactions to acquire shard locks in the same ring order and by delaying larger sequence-number transactions in each shard's pending list. | `arxiv:2107.13047v2#p5,p9` | folded_into_meta_note |
| RingBFT assumes each shard has fewer than one-third Byzantine replicas, gives safety under asynchronous communication, and gives liveness during periods of synchrony. | `arxiv:2107.13047v2#p3-p4,p9-p10` | folded_into_meta_note |
| RingBFT claims that deterministic cross-shard transactions can reach consensus in at most two rotations around the ring, with simple transactions completing after one rotation and complex transactions using a second Execute rotation to pass dependencies. | `arxiv:2107.13047v2#p4-p7` | folded_into_meta_note |

## 概念与地图落点

| 层级 | 落点 | 说明 |
| --- | --- | --- |
| Primary topic | [[sharded-ledgers|Sharded ledgers]] | permissioned sharded blockchain 的 cross-shard consensus source extension |
| Concept | [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT]] | paper-specific meta-BFT protocol |
| Concept | [[sharded-ledgers|Ring-ordered cross-shard consensus]] | reusable topology/ordering pattern |
| Existing concept | [[sharded-ledgers|Byzantine sharded transactions]] | 增补 ring topology 和 complex cst 支持 |
| Bridge | [[bft-consensus-to-sharded-ledgers|BFT consensus -> sharded ledgers]] | 增补跨 shard BFT consensus topology 证据 |

## 适用边界

- RingBFT 是 permissioned sharded blockchain protocol，不处理 permissionless shard assignment 或 Sybil resistance。
- 需要 deterministic transactions 和已知 read/write sets；动态 smart-contract execution 或未知访问集需要额外机制。
- intra-shard BFT 成本仍存在；每 shard replicas 增加时 PBFT 二次通信会降低 RingBFT throughput。
- 论文的 AHL/Sharper 比较可作为 RingBFT paper 内的 baseline evidence，但不能替代 AHL/Sharper 直接精读。

## 吸收结果

- Source note: absorbed
- Evidence records: 8 source-local records retained in this meta note for upper-layer source-extension use
- Concepts: 2 created, sharded-ledgers / Byzantine sharded transactions / cluster-sending / BFT concept refreshed
- Maps/syntheses: scaling-and-sharding, sharded-ledgers, blockchain-systems, BFT topic, sharded-ledgers synthesis refreshed
- Bridge: BFT consensus -> sharded ledgers refreshed

