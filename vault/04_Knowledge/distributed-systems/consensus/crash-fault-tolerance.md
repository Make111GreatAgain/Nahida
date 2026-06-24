---
id: "nahida-knowledge-crash-fault-tolerance"
title: "Crash-fault tolerance"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "crash-fault-tolerance"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-consensus"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "crash-fault-tolerance"
primary_ontology_path: "distributed-systems/consensus/crash-fault-tolerance"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-crash-fault-tolerance"
    relation: "is_a"
    to: "nahida-knowledge-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/crash-fault-tolerance.md"
      - "vault/04_Knowledge/distributed-systems/consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-crash-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-crash-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-crash-fault-tolerance"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-crash-fault-tolerance"
    relation: "bridges_to"
    to: "nahida-bridge-crash-fault-consensus-to-permissioned-blockchains"
    evidence_refs:
      - "vault/05_Bridges/crash-fault-consensus-to-permissioned-blockchains.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-crash-fault-consensus-to-permissioned-blockchains"
source_note_refs:
  - "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
  - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
representative_source_refs:
  - "sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
query_keys:
  - "Crash-fault tolerance"
  - "crash-fault-tolerance"
  - "CFT"
  - "Crash fault tolerant consensus"
  - "Raft-style CFT for permissioned blockchain"
aliases:
  - "CFT"
  - "Crash fault tolerant consensus"
domains:
  - "distributed-systems"
topics:
  - "crash-fault-tolerance"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-20"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-sraft-scalable-cft"
source_refs:
  - "sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
confidence: "medium"
trust_tier: "primary"
---

# Crash-fault tolerance

## 定义与范围

- 定义: Crash-fault tolerance (CFT) 处理节点停止、重启、丢包或延迟但不恶意伪造/分叉消息的故障模型。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `crash-fault-tolerance`
- Aliases/query keys: CFT, Crash fault tolerant consensus
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `crash-fault-tolerance`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

Raft 是当前代表 source；SRaft 是 CFT/Raft 进入 permissioned blockchain workload 的 source extension。16 页 SRaft 版本明确给出 crash-fault 模型: `2f + 1` peers 容忍 `f` crashed peers、partial synchrony、PKI 身份认证，并把 Raft-style CFT 在许可链中的主要压力点定位为 full-block replication 的 leader/initiator 带宽瓶颈。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[consensus|consensus]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在 crash/recovery/network delay 下维持 replicated log 或状态机顺序安全。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[consensus|consensus]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Leader election and terms | 通过 leader/term 管理 replicated log 或 ordering authority。 | 已知成员、crash/recovery、majority quorum。 | leader 可成为吞吐或可用性瓶颈；需要 leader change。 | [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|Raft]] |
| Majority quorum and replicated log/order | 以多数复制/确认保证已经提交的 log/order 不被后续 leader 覆盖。 | `2f + 1` 容忍 `f` crash faults。 | 不覆盖 Byzantine equivocation 或恶意分叉。 | [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|Raft]] |
| Data dissemination offload | 在应用层把大 payload 复制从 ordering leader 移走，只让 leader 处理 order/hash。 | payload 大、peer 数多、CFT setting。 | 需要额外处理 payload 可获得性、relay failure 和 workload reports。 | [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft scalable CFT]] |
| Workload-adaptive replication | 高负载 initiator 用 relay/tree route 分摊上传压力。 | workload skew，且 crash-only 假设允许信任 peer 身份和确认。 | CFT 边界内有效；不能直接推广到 Byzantine relay。 | [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft scalable CFT]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|In Search of an Understandable Consensus Algorithm]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain]] | paper | 展示 CFT/Raft 在 permissioned blockchain 中可通过 block replication/order split 与 workload-adaptive relay 扩展 | CFT-only；不覆盖 Byzantine relay 或 permissionless membership | `p1-p16` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-20`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: CFT 是 consensus 下的基础故障模型，不应被 Raft 或 SRaft 替代。新 SRaft 来源增强了一个下游问题: 当 CFT replicated-log 思路应用到区块链 block ordering 时，数据路径和 workload skew 可能比 consensus metadata 更先触顶，因此 CFT 知识节点需要把 "order agreement" 与 "payload dissemination" 分开解释。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|In Search of an Understandable Consensus Algorithm]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain]] | 将 CFT/Raft 的 majority-ordering 思路放入 permissioned blockchain，并明确把大 payload 复制从 hash ordering 中分离；BRT/workload-adaptive route 是 source-specific mechanism | 背景; 方法族与解决路线; 当前综合; Bridge Links | no | 后续和 CRaft、PigPaxos、Stretch-BFT 比较 leader bottleneck mitigation |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[crash-fault-consensus-to-permissioned-blockchains|Crash-fault consensus -> permissioned blockchains]] | `distributed-systems/consensus/crash-fault-tolerance; blockchain-systems/consensus/permissioned-blockchain-consensus` | application, translation, implementation_reuse | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-crash-fault-tolerance | is_a | nahida-knowledge-consensus | vault/04_Knowledge/distributed-systems/consensus/crash-fault-tolerance.md; vault/04_Knowledge/distributed-systems/consensus.md | medium | active_seed |
| nahida-knowledge-crash-fault-tolerance | evidenced_by | vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md | vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md | medium | active_seed |
| nahida-knowledge-crash-fault-tolerance | evidenced_by | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | medium | active_seed |
| nahida-knowledge-crash-fault-tolerance | evidenced_by | vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md | high | active_seed |
| nahida-knowledge-crash-fault-tolerance | bridges_to | nahida-bridge-crash-fault-consensus-to-permissioned-blockchains | vault/05_Bridges/crash-fault-consensus-to-permissioned-blockchains.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Paxos/Multi-Paxos/Viewstamped Replication 缺 source。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-sraft-scalable-cft | Added SRaft full paper as CFT source extension; clarified payload dissemination vs ordering distinction under permissioned blockchain workload. | 1 source note | codex |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 2 source notes; 3 legacy notes | codex |
