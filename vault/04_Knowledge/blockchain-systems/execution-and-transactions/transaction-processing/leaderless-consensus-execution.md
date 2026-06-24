---
id: "nahida-knowledge-leaderless-consensus-execution"
title: "Leaderless consensus execution"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "method_family"
hierarchy_level: "subproblem"
file_slug: "leaderless-consensus-execution"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-transaction-processing"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "transaction-processing"
  - "leaderless-consensus-execution"
primary_ontology_path: "blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution"
secondary_ontology_paths:
  - "blockchain-systems/consensus/permissioned-blockchain-consensus"
relation_edges:
  - from: "nahida-knowledge-leaderless-consensus-execution"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-transaction-processing"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-leaderless-consensus-execution"
    relation: "depends_on"
    to: "nahida-knowledge-permissioned-blockchain-consensus"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
      - "vault/05_Bridges/permissioned-consensus-to-transaction-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-leaderless-consensus-execution"
    relation: "bridges_to"
    to: "nahida-bridge-permissioned-consensus-to-transaction-execution"
    evidence_refs:
      - "vault/05_Bridges/permissioned-consensus-to-transaction-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-leaderless-consensus-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-permissioned-consensus-to-transaction-execution"
source_note_refs:
  - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
representative_source_refs:
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
query_keys:
  - "leaderless consensus execution"
  - "multi-leader consensus transaction execution"
  - "consensus-aware transaction execution"
  - "TELL"
  - "Dynamic Commitment Epoch"
aliases:
  - "Leaderless consensus-aware execution"
  - "Multi-leader consensus execution"
domains:
  - "blockchain-systems"
topics:
  - "leaderless-consensus-execution"
  - "transaction-processing"
  - "permissioned-blockchain-consensus"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-tell-leaderless-consensus-execution"
source_refs:
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
confidence: "high"
trust_tier: "primary"
---

# Leaderless consensus execution

## 定义与范围

- 定义: Leaderless consensus execution 是区块链交易执行的一个方法/问题族，关注当 consensus 由多个 leader-based instances 并行运行时，execution layer 如何按 instance 局部执行、跨 instance 合并结果，并避免慢 instance 阻塞快 instance 的 commit。
- 不包含: leaderless consensus 本身的 safety/liveness 证明；那属于 [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] 或更基础的 BFT/CFT consensus 节点。
- Canonical terms: `leaderless consensus execution`, `multi-leader consensus execution`, `consensus-aware transaction execution`.
- Retrieval role: 回答 TELL、RCC/MIR-BFT 上的执行调度、multi-instance block execution、DCE 等问题时的首选入口。

## 背景

Leaderless/multi-leader consensus 通过多个 proposers 或 consensus instances 并行产块来绕开单 leader bottleneck。对 consensus 来说，这是一种扩展 ordering 吞吐的方式；对 execution 来说，它引入了新的结构: 每个 instance 内有自己的 block height 顺序，instances 之间同时推进且速度可能不同。如果 execution 仍按固定 epoch 等待所有 instances 的 blocks，快速 instance 会被慢 instance 拖住。

因此，本节点的关键不是定义 leaderless consensus，而是说明 execution layer 如何利用 leaderless consensus 的结构信息。

## 解决的问题

| Problem | 说明 | Why it matters |
| --- | --- | --- |
| Fast/slow instance skew | 不同 consensus instances 产块速度不同 | 固定 ordering unit 会让快速 instance 的 blocks 等待慢 instance |
| Out-of-order blocks | 同一 instance 的 blocks 可能乱序到达节点 | 悲观等待会降低吞吐，乐观执行需要确定性修正 |
| Cross-instance conflicts | 多 instances 独立执行后可能写/读相同状态 | 合并时需要确定性 abort/re-execution |
| Commit unit selection | ordering/merge unit 过大或固定会放大等待 | 动态 commit unit 可适配 instance 运行状态 |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | child_of | TELL split gate: reusable subproblem beyond one algorithm detail | active_seed |
| [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | depends_on / bridge endpoint | TELL targets leaderless consensus in permissioned blockchain | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Per-instance independent execution | 每个 consensus instance 的 blocks/transactions 先局部执行 | 多 instances 可并行且本地 stateDB 可执行 | 后续仍需跨 instance merge | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| SHT-style conflict metadata | 记录交易访问状态和 read/write dependency，降低冲突检测成本 | 状态访问集合可被捕获 | 高冲突/哈希碰撞下仍有 abort/re-execution 成本 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| Speculative execution for out-of-order blocks | 先执行较高 height block，缺失低 height block 到达后检测 WAR/WAW 并修正 | 网络乱序或慢 block 不应阻塞全部执行 | 需要 deterministic MVCC/visibility 规则 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| Deterministic inter-instance merge | 周期性用 SHT bucket 交集检测冲突，选择 abort 更少的 m-instance plan | 多 instances 独立执行产生可合并结果 | skew/instances 增加时 abort rate 和 merge latency 上升 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| Dynamic Commitment Epoch | 根据实例 block-producing interval 动态决定一个 DCE 包含哪些 blocks | instances 速度差异大，timestamp 可被共识确认 | 不是 consensus safety 证明；timestamp/threshold 需协议约束 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus]] | paper | 首个 source-backed instance: 提出 SHT、intra-instance speculative execution、inter-instance merging、DCE，并在 RCC+PBFT/SmallBank/LevelDB 下评估 | evaluation excludes consensus latency; single data-center; source-specific mechanisms 不等同 foundation | p1-p13 |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-20`。
- Freshness: `fresh` for current-vault evidence, not a latest-news claim。
- 综合: Leaderless consensus execution 是值得拆出的 child node，因为它把多个来源可能重复出现的执行层问题集中起来: consensus instance 的并行性会改变 execution 的等待、冲突和合并策略。TELL 目前是唯一完整 source，因此本节点为 `active_seed`，不是 evergreen survey。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | 创建本方法族；SHT/DCE/speculative execution/merge 作为 source-specific representative mechanisms | 定义; 方法族; 当前综合; Bridge Links | yes | 后续对比 Nezha、SChain、MIR-BFT/RCC execution papers |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[permissioned-consensus-to-transaction-execution|Permissioned consensus -> transaction execution]] | `blockchain-systems/consensus/permissioned-blockchain-consensus; blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution` | dependency, co_evolution, implementation_reuse, tension | consensus instance status transfers as scheduling/commit information; execution optimizations do not establish consensus safety. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-leaderless-consensus-execution | is_a | nahida-knowledge-blockchain-transaction-processing | vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution.md | high | active_seed |
| nahida-knowledge-leaderless-consensus-execution | depends_on | nahida-knowledge-permissioned-blockchain-consensus | TELL source note; bridge note | high | active_seed |
| nahida-knowledge-leaderless-consensus-execution | bridges_to | nahida-bridge-permissioned-consensus-to-transaction-execution | vault/05_Bridges/permissioned-consensus-to-transaction-execution.md | high | active_seed |
| nahida-knowledge-leaderless-consensus-execution | evidenced_by | vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md | TELL source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 缺少 Nezha/SChain/DAG/parallel consensus execution source。 | 判断本节点是否应拆分为 DAG execution、RCC execution、sharded execution 等子路线。 | continue paper intake | high | queued |
| 缺少 consensus-side foundation for RCC/MIR-BFT in this exact bridge. | TELL 以 RCC+PBFT 实验，但 endpoint consensus node 还缺 RCC/MIR-BFT 细化。 | `nahida-update` for queued consensus papers or `nahida-research-search` foundation_pack | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-tell-leaderless-consensus-execution | Created method-family seed from TELL and linked it to permissioned consensus bridge. | 1 source note | codex |
