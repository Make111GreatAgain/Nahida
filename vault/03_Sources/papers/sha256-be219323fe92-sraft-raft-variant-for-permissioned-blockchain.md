---
id: "sha256-be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
title: "A Raft Variant for Permissioned Blockchain"
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
  - "p1 title, authors, abstract, introduction"
  - "p2 SRaft overview and Replicating phase"
  - "p3 Ordering phase and demonstration overview"
  - "p4-p5 demonstration panels, block status transition, acknowledgements, references"
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown in extracted PDF"
year: "2023"
local_pdf: "~/Desktop/paper/paper_972.pdf"
sha256: "be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
pages: 5
pdf_extractor: "codex-bundled-python:pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/paper-972-be219323fe92-pages.txt"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "crash-fault-tolerance"
  - "permissioned-blockchain-consensus"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "crash-fault-tolerance"
primary_ontology_path: "distributed-systems/consensus/crash-fault-tolerance/sha256-be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
secondary_ontology_paths:
  - "blockchain-systems/consensus/permissioned-blockchain-consensus/sha256-be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
    - "blockchain-systems"
  directions:
    - "consensus"
  topics:
    - "crash-fault-tolerance"
    - "permissioned-blockchain-consensus"
    - "leader-bottleneck-mitigation"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "sraft"
  - "raft"
  - "crash-fault-tolerance"
  - "permissioned-blockchain-consensus"
aliases:
  - "SRaft"
  - "Scalable Raft"
tags:
  - "nahida/source"
  - "paper"
  - "distributed-systems"
  - "consensus"
  - "crash-fault-tolerance"
  - "permissioned-blockchain"
direction_facets:
  parent_domain:
    - "distributed-systems"
    - "blockchain-systems"
  subdomain:
    - "consensus"
  problem:
    - "leader bottleneck in Raft-style blockchain ordering"
    - "CFT consensus for permissioned blockchains"
  method_family:
    - "Raft variant"
    - "leaderless block replication"
    - "hash ordering"
    - "workload-adaptive forwarding route"
  system_layer:
    - "replication"
    - "ordering"
    - "commit pipeline"
  evaluation_context:
    - "interactive demonstration"
  application:
    - "permissioned blockchain"
  bridge:
    - "crash-fault consensus to permissioned blockchains"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-sraft"
safe_for_absorption: true
source_refs:
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "pdf:~/Desktop/paper/paper_972.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "distributed-systems/consensus"
secondary_directions:
  - "blockchain-systems/consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title and abstract explicitly present a Raft variant for permissioned blockchain"
  - "abstract and Sections 2.1-2.2 split SRaft into Replicating and Ordering phases"
  - "paper targets CFT/Raft-style consensus rather than Byzantine consensus"
taxonomy_version: "1.0"
---

# A Raft Variant for Permissioned Blockchain

## 论文身份

- 标题: A Raft Variant for Permissioned Blockchain
- 作者: Zheming Ye, Xing Tong, Wei Fan, Zhao Zhang, Cheqing Jin
- 机构: East China Normal University; Engineering Research Center of Blockchain Data Management, Ministry of Education
- 年份: 2023, based on local queue/PDF metadata; venue not present in extracted PDF
- 本地 PDF: `~/Desktop/paper/paper_972.pdf`
- SHA-256: `be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 5
- 已覆盖章节/页码: Abstract, Introduction, SRaft overview, Replicating phase, Ordering phase, Demonstration, references
- Extraction gaps: PDF 没有显式 venue/DOI/arXiv；年份来自本地 queue 与 PDF metadata creation date。论文以 demo/design note 为主，没有完整性能实验、形式化安全证明或实现 artifact 描述。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1 | 问题与贡献 | permissioned blockchain 中 Raft 节点数更多，leader 网络瓶颈更突出；提出 SRaft | high |
| §2 / p2 | 总览 | SRaft 将共识拆成 Replicating 和 Ordering 两阶段 | high |
| §2.1 / p2 | Replicating phase | 任意 peer 可打包并复制 block；根据 peers 可用带宽选择 one-to-all 或 tree route；多数确认后发送 hash 给 ordering leader | high |
| §2.2 / p3 | Ordering phase | leader 排序 block hash 而不是完整 block；沿用 Raft 的广播、确认、commit 流程 | high |
| §2.2 / p3 | Sending-Receiving | 利用 blockchain chain structure 将当前 ordering result 广播与新 hash 接收流水化 | high |
| §3 / p3-p5 | Demonstration | 前端演示 peer 状态、通信、带宽/工作负载、overload ratio、block status、forwarding route 和 commit transition | medium-high |
| References / p5 | 相邻工作 | CAICT blockchain white paper, Raft, CRaft | medium |

## 一句话贡献

SRaft 是面向 permissioned blockchain 的 Raft 变体：它把 full block dissemination 从单 leader 转移到所有 peers 参与的 workload-adaptive replication，再由 leader 只排序已复制 block 的 hash，从而减轻 Raft leader 在大节点数 blockchain 场景下的网络压力。

## 核心精读笔记

### 背景与问题

论文观察到 permissioned blockchains 常采用 crash-fault-tolerant consensus，并且许多系统支持 Raft。但 blockchain deployment 往往比传统 Raft replicated service 有更多 peers，所有 block 都经由 leader 复制会放大 leader bandwidth bottleneck。

作者把 SRaft 定位为 CFT/Raft-family design，而不是 Byzantine consensus。文中没有讨论恶意节点任意作恶、slashing、validator incentives、accountable safety 或开放网络治理。

### SRaft 的两阶段拆分

SRaft 把 consensus 解耦为两个阶段:

- Replicating phase: peers 复制 block 内容，使多数 peers 持有 block。
- Ordering phase: ordering leader 对已经成功复制的 block hash 排序并提交。

这个拆分让 bandwidth-heavy block transfer 不再集中在 ordering leader。leader 仍承担 ordering/commit coordination，但其网络负载主要是 hash-level metadata，而不是完整 block。

### Replicating phase

每个 peer 都可以接收 client transactions、打包 block，并发起复制。发起 peer 会收集其他 peers 的可用带宽，再为当前 block 构造复制路线:

- 如果发起 peer 带宽足够，采用 one-to-all replication。
- 如果发起 peer 过载，采用 tree-pattern replication，让空闲 peers 作为 branch nodes 转发 block。

route 会发送给相关 peers。发起 peer 收到多数 confirm messages 后，认为 block 已成功复制，并把 block hash 发送给 Ordering leader。

### Ordering phase

Ordering leader 收到 Replicating phase 的 hash values 后，按 Raft-like flow 处理: 广播 ordering result，等待多数确认，再广播 commit message。与常规 Raft 相比，ordering result 只包含 hash values，目的是降低 leader 网络压力。

论文还用 blockchain chain structure 做流水线化: leader 广播当前 ordering result 时，同时接收新复制完成的 block hashes；下一轮 leader 对新 hashes 排序，并提交上一轮的 ordering result。演示中的 block status transition 展示了这一点: 前一轮达到 consensus 的 blocks 在下一轮 commit，新一轮 blocks 同时进入 consensus 状态。

### Demonstration 性质

这篇 paper 的实验部分是演示系统而非 benchmark。展示面板包括 peer status/communication、bandwidth/workload、overload ratio、latest block、forwarding route 和 local block status。它能说明 SRaft 的机制和状态流转，但不能独立证明吞吐/延迟改进幅度，也不能替代 safety/liveness 证明。

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| SRaft adapts Raft-style consensus for permissioned blockchains by decoupling full-block dissemination into a Replicating phase and hash ordering into an Ordering phase. | `sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e#p1-p2` | folded_into_meta_note |
| The SRaft paper's evaluation surface is an interactive demonstration that visualizes peer communication, bandwidth/workload, overload ratio, forwarding routes, and block status transitions rather than a full benchmark study. | `sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e#p3-p5` | folded_into_meta_note |
| In SRaft's Replicating phase, any peer can package and replicate a block, selecting one-to-all or tree forwarding routes according to peer bandwidth and treating majority confirmations as successful replication. | `sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e#p2` | folded_into_meta_note |
| SRaft's Ordering phase orders hashes of successfully replicated blocks rather than full blocks, preserving a Raft-like majority-confirm/commit flow while reducing leader network pressure. | `sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e#p3` | folded_into_meta_note |
| SRaft targets crash-fault-tolerant permissioned blockchain settings and should not be treated as Byzantine-fault or permissionless consensus evidence without additional sources. | `sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e#p1-p5` | folded_into_meta_note |
| SRaft uses the blockchain chain structure to pipeline ordering and commit: while broadcasting one ordering result, the leader receives newly replicated block hashes, then orders those hashes and commits the previous result in the next round. | `sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e#p3-p5` | folded_into_meta_note |

## 概念与地图落点

| 层级 | 落点 | 说明 |
| --- | --- | --- |
| Primary topic | [[crash-fault-tolerance|Crash-fault tolerance]] | Raft-family CFT consensus variant |
| Concept | [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|SRaft]] | 论文提出的 two-phase Raft variant |
| Concept | [[permissioned-blockchain-consensus|Raft for permissioned blockchains]] | Raft/CFT 在 blockchain deployment 中的 leader-bottleneck adaptation |
| Bridge | [[crash-fault-consensus-to-permissioned-blockchains|Crash-fault consensus -> permissioned blockchains]] | 将 distributed-systems CFT 与 blockchain-systems consensus 连接 |

## 适用边界

- 适用于 permissioned blockchain / CFT consensus 场景。
- 不应把 SRaft 直接当作 BFT/permissionless consensus。
- 本 paper 是 5 页 demo/design paper；性能和安全性需要后续吸收 SRaft 完整版、CRaft、production permissioned blockchain sources 后再强归纳。

## 吸收结果

- Source note: absorbed
- Evidence records: 6 source-local records retained in this meta note for upper-layer source-extension use
- Concepts: 2 created, 2 existing CFT/Raft concepts refreshed
- Maps: distributed consensus, crash-fault tolerance, blockchain consensus, blockchain systems refreshed
- Bridge: crash-fault consensus to permissioned blockchains created
