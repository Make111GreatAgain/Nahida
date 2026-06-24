---
id: "nahida-bridge-crash-fault-consensus-to-permissioned-blockchains"
title: "Crash-fault consensus -> permissioned blockchains"
original_title: "Crash-fault consensus -> permissioned blockchains"
file_slug: "crash-fault-consensus-to-permissioned-blockchains"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_domain_method_transfer"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/consensus/crash-fault-tolerance"
  - "blockchain-systems/consensus/permissioned-blockchain-consensus"
endpoint_knowledge_refs:
  - "nahida-knowledge-crash-fault-tolerance"
  - "nahida-knowledge-permissioned-blockchain-consensus"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "consensus"
to_direction: "consensus"
from_topic: "crash-fault-tolerance"
to_topic: "permissioned-blockchain-consensus"
relation_types:
  - "application"
  - "translation"
  - "implementation_reuse"
directionality: "uncertain"
relationship_thesis: "Raft-style crash-fault consensus can be reused in permissioned blockchain ordering, but blockchain workloads expose a different bottleneck profile: more peers, larger blocks, geo-distributed clients, and skewed workload make leader-centric block replication expensive. SRaft-style designs translate CFT ordering by separating full-block dissemination from hash ordering and by making replication workload-adaptive."
transferability: "medium"
non_transfer_boundary: "需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-20"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "raft"
  - "sraft"
  - "permissioned-blockchain-consensus"
source_note_refs:
  - "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
  - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
knowledge_refs:
  - "nahida-knowledge-crash-fault-tolerance"
  - "nahida-knowledge-permissioned-blockchain-consensus"
query_keys:
  - "Crash-fault consensus -> permissioned blockchains"
  - "Raft to permissioned blockchain"
  - "SRaft workload-adaptive CFT"
created: "2026-06-11"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-sraft-scalable-cft"
source_refs:
  - "sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
confidence: "medium-high"
trust_tier: "primary"
---

# Crash-fault consensus -> permissioned blockchains

## 命名与路径

- Original title: Crash-fault consensus -> permissioned blockchains
- File slug: `crash-fault-consensus-to-permissioned-blockchains`
- Path safety check: migrated to `05_Bridges/crash-fault-consensus-to-permissioned-blockchains.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/crash-fault-consensus-to-permissioned-blockchains.md` 迁移而来。端点 knowledge refs 为: review。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: Crash-fault consensus -> permissioned blockchains

## Bridge Thesis

Raft-style crash-fault consensus can be reused in permissioned blockchain ordering, but blockchain workloads expose a different bottleneck profile: more peers, larger blocks, geo-distributed clients, and skewed workload make leader-centric block replication expensive. SRaft-style designs translate CFT ordering by separating full-block dissemination from hash ordering and by making replication workload-adaptive.

## Endpoint Paths

| Endpoint | Role | Current evidence |
| --- | --- | --- |
| `distributed-systems/consensus/crash-fault-tolerance` | Source protocol family | [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|Raft]] establishes leader-based replicated-log CFT consensus |
| `blockchain-systems/consensus/permissioned-blockchain-consensus` | Application/adaptation setting | [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|SRaft demo/design note]] and [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft full paper]] adapt Raft to permissioned blockchain by splitting replication and ordering |

## Relation Rows

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| Raft | provides | CFT ordering foundation | Raft p1-p8 | high | active_seed |
| Permissioned blockchain ordering | reuses | Raft-style CFT consensus | SRaft p1 | high | active_seed |
| Blockchain peer count and block transfer | stress | Raft leader bandwidth | SRaft p1 | medium-high | active_seed |
| SRaft | adapts | Raft via replication/ordering decoupling | SRaft p1-p3 | high | active_seed |
| SRaft | remains_within | crash-fault fault model | SRaft p1-p5 | medium-high | active_seed |
| SRaft full paper | strengthens | workload-adaptive CFT transfer evidence | SRaft full paper p1-p16 | high | active_seed |
| Block Replicating Tree | mitigates | overloaded initiator upload bottleneck | SRaft full paper p7-p10 | high | active_seed |
| Hash-only ordering | translates | Raft-style ordering to blockchain block order | SRaft full paper p11-p12 | high | active_seed |

## Open Gaps

- Direct Hyperledger Fabric / orderer documentation or paper source.
- CRaft source and broader production permissioned-chain sources.
- BFT permissioned blockchain comparison source before making protocol-selection recommendations.


## 连接命题

- From: `distributed-systems/consensus/crash-fault-tolerance`
- To: `blockchain-systems/consensus/permissioned-blockchain-consensus`
- Relation types: application, translation, implementation_reuse
- Directionality: `uncertain`
- Relationship thesis: Raft-style crash-fault consensus can be reused in permissioned blockchain ordering, but blockchain workloads expose a different bottleneck profile: more peers, larger blocks, geo-distributed clients, and skewed workload make leader-centric block replication expensive. SRaft-style designs translate CFT ordering by separating full-block dissemination from hash ordering and by making replication workload-adaptive.


## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| nahida-knowledge-crash-fault-tolerance | `distributed-systems/consensus/crash-fault-tolerance` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | `blockchain-systems/consensus/permissioned-blockchain-consensus` | bridge endpoint | endpoint knowledge + source notes | active_seed |


## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `application, translation, implementation_reuse` | endpoint paths above | source notes and legacy bridge detail | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 |
| `payload dissemination / ordering split` | permissioned blockchain consensus | [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft full paper]] p4-p12 | 可迁移的是拆分思路；BRT 细节仍是 SRaft source-specific mechanism。 |
| `workload-adaptive relay` | high-skew permissioned deployments | [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft full paper]] p7-p16 | 只在 crash-fault/trusted-membership 边界内作为 evidence；不能直接推广到 Byzantine relay。 |


## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| bridge relation | `distributed-systems/consensus/crash-fault-tolerance` | `blockchain-systems/consensus/permissioned-blockchain-consensus` | application, translation, implementation_reuse | source notes / legacy detail | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 |
| replication/order split | `distributed-systems/consensus/crash-fault-tolerance` | `blockchain-systems/consensus/permissioned-blockchain-consensus` | translate CFT ordering while moving full-block dissemination off the leader | [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft full paper]] | 依赖 CFT/known-membership; 不处理 Byzantine data withholding。 |


## 类比、依赖或关系边界

需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|sha256-0f53a6508592-raft-understandable-consensus-algorithm]] | source_note_refs | active_seed |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain]] | source_note_refs | active_seed |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain]] | source_note_refs; stronger mechanism/evaluation evidence | active_seed |


## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/consensus/crash-fault-tolerance` | update Bridge Links and relation_edges | active_seed |
| `blockchain-systems/consensus/permissioned-blockchain-consensus` | update Bridge Links and relation_edges | active_seed |


## 查询入口

- Crash-fault consensus -> permissioned blockchains
- Raft to permissioned blockchain
- SRaft workload-adaptive CFT


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |
| nahida-knowledge-crash-fault-tolerance | Source Extensions / relation_edges | SRaft full paper clarifies CFT payload dissemination limits | active_seed |
| nahida-knowledge-permissioned-blockchain-consensus | Source Extensions / 方法族 | SRaft full paper strengthens workload-adaptive route | active_seed |

## 刷新规则

- Last checked: `2026-06-20`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
