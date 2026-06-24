---
id: "nahida-bridge-database-transactions-to-byzantine-sharded-ledgers"
title: "Database transaction protocols -> Byzantine sharded ledgers"
original_title: "Database transaction protocols -> Byzantine sharded ledgers"
file_slug: "database-transactions-to-byzantine-sharded-ledgers"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_path"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/transaction-processing/distributed-transactions"
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers"
endpoint_knowledge_refs:
  - "nahida-knowledge-distributed-transactions"
  - "nahida-knowledge-sharded-ledgers"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "transaction-processing"
to_direction: "scaling-and-sharding"
from_topic: "distributed-transactions"
to_topic: "sharded-ledgers"
relation_types:
  - "translation"
  - "implementation_reuse"
  - "dependency"
directionality: "one_way"
relationship_thesis: "ByShard and AHL translate database transaction protocols such as two-phase commit and two-phase locking into Byzantine sharded ledgers: ByShard wraps shard-steps in consensus and cluster-sending, while AHL runs the coordinator logic inside a BFT reference committee. LightCross provides a contrast route for arbitrary smart contracts: avoid exposing all contract logic as 2PC/2PL fragments by offloading CSTx execution to TEE executors and validating results through an R-shard/S-shard bitmap protocol."
transferability: "medium"
non_transfer_boundary: "2PC/2PL structure transfers; Byzantine voting, shard consensus, cluster-sending or reference committees, faulty clients, validator assignment, trusted hardware, permissionless incentives, and data availability remain sharded-ledger-specific concerns."
evidence_window_start: "1978"
evidence_window_end: "2024"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "distributed-transactions"
  - "sharded-ledgers"
  - "byshard"
  - "AHL"
  - "LightCross"
  - "cross-shard smart contract execution"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
knowledge_refs:
  - "nahida-knowledge-distributed-transactions"
  - "nahida-knowledge-sharded-ledgers"
query_keys:
  - "ByShard database transactions Byzantine sharding"
  - "two-phase commit in Byzantine shards"
  - "two-phase locking in sharded ledgers"
  - "AHL reference committee 2PC 2PL"
  - "LightCross TEE executor cross-shard smart contracts"
created: "2026-06-11"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260621-ahl-sharding"
  - "nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts"
source_refs:
  - "doi:10.14778/3476249.3476275"
  - "arxiv:1804.00399v4"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
confidence: "medium"
trust_tier: "primary"
---

# Database transaction protocols -> Byzantine sharded ledgers

## 命名与路径

- Original title: Database transaction protocols -> Byzantine sharded ledgers
- File slug: `database-transactions-to-byzantine-sharded-ledgers`
- Path safety check: migrated to `05_Bridges/database-transactions-to-byzantine-sharded-ledgers.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/database-transactions-to-byzantine-sharded-ledgers.md` 迁移而来。端点 knowledge refs 为: nahida-knowledge-distributed-transactions, nahida-knowledge-sharded-ledgers。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: Database transaction protocols -> Byzantine sharded ledgers

## 连接命题

- From: `distributed-systems/transaction-processing/distributed-transactions`
- To: `blockchain-systems/scaling-and-sharding/sharded-ledgers`
- Relation types: translation, implementation_reuse, dependency
- Directionality: one_way
- Relationship thesis: ByShard and AHL translate database transaction protocols such as two-phase commit and two-phase locking into Byzantine sharded ledgers. ByShard wraps shard-steps in consensus and cluster-sending; AHL runs 2PC coordinator logic inside a BFT reference committee. LightCross is a contrast route: for arbitrary smart contracts, it avoids exposing every contract call as shard-local 2PC/2PL fragments by executing the CSTx inside a TEE executor and validating the certified result through R-shard/S-shard bitmap coordination.

## 端点范围

| Endpoint | Path | Scope in bridge | Evidence | Notes |
| --- | --- | --- | --- | --- |
| Distributed transactions | `distributed-systems/transaction-processing/distributed-transactions` | 2PC, 2PL, ACID isolation, distributed database transaction processing | ByShard and AHL cite/adapt database mechanisms | foundation_missing in vault |
| Byzantine sharded ledgers | `blockchain-systems/scaling-and-sharding/sharded-ledgers` | multiple resilient shards executing multi-shard transactions | ByShard + OmniLedger + AHL | foundation_thin |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Two-phase commit | Distributed transactions | Byzantine shards | linear, centralized, distributed orchestration variants | ByShard §4 | Byzantine votes require shard consensus and cluster-sending |
| Vote collection | 2PC coordinator logic | root/distributed shards | process unordered vote set with one consensus step | ByShard Lemma 4.2 | cluster-sending assumptions must hold |
| Two-phase locking | Distributed DB isolation | Byzantine shards | locks acquired in deterministic order during vote-steps | ByShard §5.2 | high contention can raise latency or abort rate |
| Isolation levels | DB isolation degrees | sharded resilient systems | read uncommitted/read committed/serializable variants | ByShard §5.2 | lower isolation may be unacceptable for some apps |
| Performance trade-off analysis | DB systems benchmarking | sharded ledger design | throughput/committed throughput/duration/abort/per-shard work | ByShard §6 | simulated consensus model |
| BFT reference committee coordinator | 2PC coordinator state machine | Byzantine shards for general workloads | coordinator logic runs as BFT SMR in reference committee `R`; tx-committees wait for quorums of `PrepareTx`, `CommitTx`, or `AbortTx` | AHL §6.2 | reference committee can bottleneck and needs scaling; liveness assumes partial synchrony |
| Chaincode-level 2PL adaptation | database locking | Hyperledger-style sharded chaincode | split `sendPayment` into prepare/commit/abort and store `L_acc` lock state | AHL §6.3 | requires manual refactoring or future language/runtime support |
| TEE-executor contrast route | arbitrary smart-contract execution | smart-contract sharded ledgers | execute CSTx once in a TEE executor, then validate read freshness and commit write sets through R-shard/S-shard batch protocol | LightCross §III | TEE and R-shard/executor availability replace some 2PC/2PL refactoring costs; stale reads can still abort |

## 不可迁移边界

- Traditional 2PC/2PL does not solve Byzantine equivocation; ByShard needs consensus and cluster-sending around each shard-step.
- Traditional distributed databases do not solve permissionless validator assignment or Sybil resistance.
- Interactive transactions are not a good fit for high-cost consensus rounds according to ByShard §7.
- AHL's reference committee protects liveness against malicious coordinators, but it does not remove contention, reference-committee bottlenecks, or the need to refactor application logic.
- LightCross reduces the need to express arbitrary smart-contract logic as explicit 2PC/2PL fragments, but it does not remove the need for shard-level BFT, serializable validation, state authentication, or trusted execution assumptions.
- Database transaction foundations are not yet directly present in the vault; this bridge must stay `foundation_thin`.

## 路径传播

| Endpoint path | Pack update | Relation/index update | Synthesis action | Status |
| --- | --- | --- | --- | --- |
| `distributed-systems/transaction-processing/distributed-transactions` | queued foundation pack | review relation rows added | no synthesis yet | foundation_missing |
| `blockchain-systems/scaling-and-sharding/sharded-ledgers` | topic refreshed with ByShard and AHL | active_seed relation rows indexed | sharded-ledgers synthesis refreshed | active_seed |

## 查询入口

- ByShard 如何把 two-phase commit 放进 Byzantine shards?
- two-phase locking 在 BFT 分片里为什么不需要额外 consensus?
- AHL reference committee 和 ByShard decentralized orchestration 有什么 trade-off?
- LightCross 为什么不是简单的 2PC/2PL 迁移，而是 TEE executor + R-shard validation 的对照路线?

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `translation, implementation_reuse, dependency` | endpoint paths above | source notes and bridge detail | 2PC/2PL structure transfers; Byzantine voting, shard consensus, cluster-sending or reference committees, faulty clients, validator assignment, trusted hardware, permissionless incentives, and data availability remain sharded-ledger-specific concerns. |


## 类比、依赖或关系边界

2PC/2PL structure transfers; Byzantine voting, shard consensus, cluster-sending or reference committees, faulty clients, validator assignment, trusted hardware, permissionless incentives, and data availability remain sharded-ledger-specific concerns.


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment]] | source_note_refs | active_seed |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding]] | source_note_refs | active_seed |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] | source_note_refs / contrast route | active_seed |


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |
| [[cross-shard-transaction-execution|Cross-shard transaction execution]] | Bridge Links / method contrast | LightCross shows a TEE-backed alternative to direct 2PC/2PL fragmentation for arbitrary smart contracts. | active_seed |

## 刷新规则

- Last checked: `2026-06-22`
- Valid until: `2026-07-21`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
