---
id: "nahida-knowledge-fraud-proofs"
title: "Fraud proofs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "fraud-proofs"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
parent_knowledge_refs:
  - "nahida-knowledge-data-availability-and-light-clients"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "data-availability-and-light-clients"
  - "fraud-proofs"
primary_ontology_path: "blockchain-systems/data-availability-and-light-clients/fraud-proofs"
secondary_ontology_paths:
  - "blockchain-systems/data-availability-and-light-clients/data-availability-sampling"
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers"
relation_edges:
  - from: "nahida-knowledge-fraud-proofs"
    relation: "is_a"
    to: "nahida-knowledge-data-availability-and-light-clients"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fraud-proofs.md"
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fraud-proofs"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fraud-proofs"
    relation: "depends_on"
    to: "nahida-knowledge-data-availability-sampling"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fraud-proofs"
    relation: "bridges_to"
    to: "nahida-bridge-fraud-proofs-to-data-availability-sampling"
    evidence_refs:
      - "vault/05_Bridges/fraud-proofs-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-fraud-proofs-to-data-availability-sampling"
  - "nahida-bridge-data-availability-to-sharded-ledgers"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
representative_source_refs:
  - "arxiv:1809.09044v1"
query_keys:
  - "Fraud proofs"
  - "fraud-proofs"
  - "fraud proofs and data availability"
  - "light client fraud proofs"
  - "state transition fraud proofs"
  - "codec fraud proofs"
aliases:
  - "fraud proofs"
  - "light-client fraud proofs"
domains:
  - "blockchain-systems"
topics:
  - "fraud-proofs"
  - "data-availability-sampling"
  - "light-client-security"
  - "state-transition-validation"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-21"
valid_until: "2026-07-21"
evidence_window_start: "2018"
evidence_window_end: "2026-06-21"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-fraud-proofs-data-availability"
source_refs:
  - "arxiv:1809.09044v1"
  - "doi:10.48550/arxiv.1809.09044"
confidence: "medium"
trust_tier: "primary"
---

# Fraud proofs

## 定义与范围

- 定义: Fraud proofs 是一种反驳式验证机制。系统先允许区块或状态承诺进入候选链，之后由 full nodes 或 challengers 提供短证明，说明某个区块、状态转换、编码数据或协议步骤违反规则；light clients 验证该证明后拒绝对应对象。
- 本节点范围: blockchain light clients、data availability、sharding 和 optimistic verification 场景中的 fraud proofs，尤其是状态转换 fraud proofs 与 data-availability/codec fraud proofs 的组合。
- 不包含: 完整 validity proof / SNARK / STARK 证明系统本身；单个 rollup/challenge game 的全部实现；任意“报错消息”或人工告警。
- Canonical terms: `fraud proofs`, `fraud-proofs`, `light-client fraud proofs`
- Retrieval role: 查询“fraud proofs 是什么”“为什么 fraud proofs 需要 data availability”“fraud proofs 和 validity proofs/DAS 有什么区别”时优先读本节点，再打开 source notes。
- Update scope: 新 source 若来自 optimistic rollups、Plasma、Celestia、Ethereum fraud proof specs、light-client protocols，应补入本节点或相关 bridge。

## 背景

Light clients 只下载 block headers 或少量证明，不执行完整交易列表，因此传统 SPV 模型通常假设 consensus majority honest。Fraud proofs 试图把“相信多数诚实”改成“至少有一个诚实观察者能在有数据时提出短反驳”。这让轻客户端可以在检测到无效状态转换或错误编码时拒绝区块，但前提是生成反驳所需的数据已经可获得。

当前 vault 中本节点由 [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities]] 作为 central seed 支撑；后续仍需要 optimistic rollup / Celestia / Ethereum DA and fraud-proof specs 来补足现代工程路径。

## 解决的问题

Fraud proofs 解决的是“低资源客户端如何发现候选对象违反规则”的问题。它适用于:

- light clients 不想下载/执行完整区块，但希望在 dishonest majority 下拒绝 invalid blocks。
- sharded blockchains 中没有单个节点验证所有 shards，需要跨 shard / shard-local invalidity 被传播。
- optimistic systems 先乐观接受结果，之后允许 challenger 提供反证。
- data availability systems 需要证明 erasure-coded extended data 构造错误，从而防止 producer 用 malformed coding 绕过 sampling。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[data-availability-and-light-clients|Data availability and light clients]] | child_of | light-client security route and source classification | active_seed |
| [[blockchain-systems|Blockchain systems]] | method_family_in | blockchain scaling and validation boundary | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| State transition fraud proofs | section | 证明某段 execution trace 从 pre-state root 到 post-state root 的转换不成立 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] §4 | source_extension |
| Codec / erasure-code fraud proofs | section | 证明 extended data 的某行/列无法对应 claimed row/column root | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] §5.5 | source_extension |
| Optimistic rollup challenge games | candidate | 现代 fraud-proof 工程路线，涉及 dispute periods、VM/state proofs、sequencer data availability | not yet in vault | queued |
| Validity proofs vs fraud proofs | bridge candidate | ZK validity proofs 可替代一部分执行反驳，但不能替代 data availability | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] §7.1 | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| State transition fraud proofs | 在 block data 中加入 intermediate state roots / traces；反证者给出相关 transactions、state witnesses 和 Merkle proofs，light client 重算该 period。 | 区块结构提前支持 execution trace；state 可用 sparse Merkle / authenticated map 表示。 | 需要 block data available；witness generation 依赖 full nodes；proof format 与执行模型强绑定。 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] |
| Data-availability-backed fraud proofs | 在接受 fraud proof 安全性之前，先用 DAS 确认 block data 可恢复，避免 producer 隐藏 invalid transaction data。 | 至少一个 honest full node，足够多 honest light clients 采样并 gossip。 | network/gossip/anti-eclipse 假设强；selective share disclosure 需匿名/随机化请求模型。 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] |
| Codec fraud proofs | 对 2D Reed-Solomon matrix 的某个 row/column 给出足够 shares 和 proofs，恢复后 root 不等于 claimed axis root 即反驳。 | DAS 使用 erasure-coded extended data，且 row/column roots 可由 dataRoot 认证。 | 证明大小约随 sqrt(block size) 增长；未来 succinct proofs 可替代这类 codec fraud proof。 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] |
| Succinct validity proof alternative | 用 SNARK/STARK 证明 erasure coding 或 state transition 正确，减少 fraud proof 需求。 | 证明系统可承受电路/编码成本，且 proof generation 有经济可行性。 | 不能替代 data availability proofs；数据不可用仍会阻止 witness/state recovery。 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] §7.1 |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities]] | paper | 建立 light-client fraud proofs + data availability proofs 的组合路线；给出 state transition fraud proof、2D RS DAS、codec fraud proof 和安全/实现分析 | 需要 honest full node、honest light-client sampling mass、bounded delay、anti-eclipse；selective disclosure 需要 enhanced request model | §3-§7 |

## 当前综合

- Evidence window: `2018` to `2026-06-21`，当前只有一篇 central source seed。
- Freshness: `fresh` for current-vault structure; not a latest-trend claim.
- Valid until: `2026-07-21`。
- 综合: Fraud proofs 是 light-client security 的反驳式验证路线。它把 trust model 从“多数 block producers 诚实”弱化为“至少一个诚实 full node 能看见数据并传播反证”。但 fraud proofs 本身依赖 data availability: 若 producer 隐藏 block data，honest full nodes 无法构造反证。因此在区块链扩容、sharding 和 optimistic verification 中，fraud proofs 必须与 DAS、数据传播、gossip、challenge period 和 anti-eclipse 假设一起分析。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] | 创建 fraud proofs seed node；补入 state transition fraud proofs、codec fraud proofs、DAS dependency 和 validity-proof boundary | 定义; 方法族; 当前综合; Bridge Links | yes | 后续吸收 optimistic rollup/Celestia/Ethereum fraud-proof sources 后升级 maturity |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[fraud-proofs-to-data-availability-sampling|Fraud proofs -> data availability sampling]] | `blockchain-systems/data-availability-and-light-clients/fraud-proofs; blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | dependency, complementarity, validation_boundary | Fraud proofs can reject invalid state transitions only when relevant data is available; DAS can show availability but not execution validity. | active_seed |
| [[data-availability-to-sharded-ledgers|Data availability -> sharded ledgers]] | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling; blockchain-systems/scaling-and-sharding/sharded-ledgers` | dependency, shared_pattern | Sharded systems need fraud/DA proofs when no single node validates all shards; DA does not solve shard execution by itself. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-fraud-proofs | is_a | nahida-knowledge-data-availability-and-light-clients | vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fraud-proofs.md | high | active_seed |
| nahida-knowledge-fraud-proofs | evidenced_by | vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md | Fraud Proofs source note | high | active_seed |
| nahida-knowledge-fraud-proofs | depends_on | nahida-knowledge-data-availability-sampling | Fraud Proofs §5 | high | active_seed |
| nahida-knowledge-fraud-proofs | bridges_to | nahida-bridge-fraud-proofs-to-data-availability-sampling | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Optimistic rollup fraud proofs / challenge games 缺 source。 | 现代工程中 fraud proofs 多通过 rollup/challenge protocol 落地。 | nahida-research-search or nahida-update | high | queued |
| Celestia / Ethereum DAS and light-client specs 缺 source。 | 可校准本文 2018 方案与现代 DAS/fraud-proof 实践的关系。 | nahida-research-search or nahida-update | high | queued |
| Validity proofs vs fraud proofs bridge 缺足够 source。 | ZK proof 可替代部分 execution fraud proof，但不能替代 DA。 | nahida-update | medium | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-fraud-proofs-data-availability | Created seed knowledge node for fraud proofs and linked it to DAS/light-client security. | 1 source note | codex |
