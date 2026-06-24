---
id: "nahida-bridge-bft-consensus-to-shared-mempool-scaling"
title: "BFT consensus -> shared mempool scaling"
original_title: "BFT consensus -> shared mempool scaling"
file_slug: "bft-consensus-to-shared-mempool-scaling"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_path"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
  - "blockchain-systems/mempool-and-networking/shared-mempool"
endpoint_knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-shared-mempool"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "consensus"
to_direction: "mempool-and-networking"
from_topic: "byzantine-fault-tolerance"
to_topic: "shared-mempool"
relation_types:
  - "application"
  - "dependency"
  - "implementation_reuse"
directionality: "uncertain"
relationship_thesis: "Leader-based BFT consensus 提供交易顺序和 safety；shared mempool scaling 把大交易数据传播从该 ordering core 外移。Stratus 的证据表明，很多区块链吞吐瓶颈不是 consensus vote 本身，而是 leader 传播 proposal payload 的数据路径。"
transferability: "medium"
non_transfer_boundary: "需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-20"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "byzantine-fault-tolerance"
  - "shared-mempool"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-shared-mempool"
query_keys:
  - "BFT consensus -> shared mempool scaling"
created: "2026-06-11"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
source_refs:
  - "arxiv:2203.05158"
confidence: "medium-high"
trust_tier: "primary"
---

# BFT consensus -> shared mempool scaling

## 命名与路径

- Original title: BFT consensus -> shared mempool scaling
- File slug: `bft-consensus-to-shared-mempool-scaling`
- Path safety check: migrated to `05_Bridges/bft-consensus-to-shared-mempool-scaling.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/bft-consensus-to-shared-mempool-scaling.md` 迁移而来。端点 knowledge refs 为: nahida-knowledge-byzantine-fault-tolerance, nahida-knowledge-shared-mempool。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: BFT consensus -> shared mempool scaling

## Relationship Thesis

Leader-based BFT consensus 提供交易顺序和 safety；shared mempool scaling 把大交易数据传播从该 ordering core 外移。Stratus 的证据表明，很多区块链吞吐瓶颈不是 consensus vote 本身，而是 leader 传播 proposal payload 的数据路径。

## Endpoint Scopes

| Endpoint | Scope | Evidence |
| --- | --- | --- |
| `distributed-systems/consensus/byzantine-fault-tolerance` | BFT fault model、leader/view、ordering safety、view change | PBFT seed; Stratus p3,p10 |
| `blockchain-systems/mempool-and-networking/shared-mempool` | transaction dissemination, microblock availability, load balancing | Stratus p1-p17 |

## Transfer Matrix

| Transfers | Does not transfer automatically |
| --- | --- |
| `N >= 3f+1`, signed/authenticated messages, view-change assumptions inform Stratus system model | Consensus safety proof does not solve data availability or skewed load |
| Leader-based ordering core can be reused while mempool changes | Stratus benchmark does not prove all BFT cores will get same improvement |
| View-change handles invalid proposals without availability proofs | Client duplicate attacks, proxy incentives, production DoS controls need separate mechanisms |

## Propagation Targets

- [[byzantine-fault-tolerance|Byzantine fault tolerance]]
- [[blockchain-consensus|Blockchain consensus]]
- [[mempool-and-networking|Mempool and networking]]
- [[shared-mempool|Shared mempool]]

## Evidence

| Source | Anchor | Note |
| --- | --- | --- |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | p1-p4,p5-p7,p11-p13,p16-p17 | Identifies leader bottleneck, defines SMP/PAB, evaluates Stratus, and models LBFT vs SMP throughput. |

## Limits

- Current bridge is active_seed because it rests on one direct source plus existing BFT/PBFT context.
- Narwhal/Tusk, HotStuff, and PBFT direct comparisons should refresh this bridge after absorption.

## 连接命题

- From: `distributed-systems/consensus/byzantine-fault-tolerance`
- To: `blockchain-systems/mempool-and-networking/shared-mempool`
- Relation types: application, dependency, implementation_reuse
- Directionality: `uncertain`
- Relationship thesis: Leader-based BFT consensus 提供交易顺序和 safety；shared mempool scaling 把大交易数据传播从该 ordering core 外移。Stratus 的证据表明，很多区块链吞吐瓶颈不是 consensus vote 本身，而是 leader 传播 proposal payload 的数据路径。


## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| nahida-knowledge-byzantine-fault-tolerance | `distributed-systems/consensus/byzantine-fault-tolerance` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-shared-mempool | `blockchain-systems/mempool-and-networking/shared-mempool` | bridge endpoint | endpoint knowledge + source notes | active_seed |


## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `application, dependency, implementation_reuse` | endpoint paths above | source notes and legacy bridge detail | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 |


## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| bridge relation | `distributed-systems/consensus/byzantine-fault-tolerance` | `blockchain-systems/mempool-and-networking/shared-mempool` | application, dependency, implementation_reuse | source notes / legacy detail | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 |


## 类比、依赖或关系边界

需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool]] | source_note_refs | active_seed |


## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/consensus/byzantine-fault-tolerance` | update Bridge Links and relation_edges | active_seed |
| `blockchain-systems/mempool-and-networking/shared-mempool` | update Bridge Links and relation_edges | active_seed |


## 查询入口

- BFT consensus -> shared mempool scaling


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |

## 刷新规则

- Last checked: `2026-06-20`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
