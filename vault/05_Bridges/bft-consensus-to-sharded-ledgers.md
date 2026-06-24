---
id: "nahida-bridge-bft-consensus-to-sharded-ledgers"
title: "BFT consensus -> sharded ledgers"
original_title: "BFT consensus -> sharded ledgers"
file_slug: "bft-consensus-to-sharded-ledgers"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active"
hierarchy_level: "bridge"
bridge_kind: "cross_path"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance"
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers"
endpoint_knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-sharded-ledgers"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "consensus"
to_direction: "scaling-and-sharding"
from_topic: "byzantine-fault-tolerance"
to_topic: "sharded-ledgers"
relation_types:
  - "application"
  - "dependency"
  - "translation"
directionality: "one_way"
relationship_thesis: "Sharded ledgers reuse Byzantine fault-tolerant consensus inside each shard, but add global validator assignment, cross-shard atomic commit, transaction isolation, state checkpointing, workload-locality constraints, and sometimes trusted-hardware assumptions to make committee sizing practical."
transferability: "medium"
non_transfer_boundary: "BFT quorum and shard-level consensus transfer; secure random validator assignment, cross-shard atomicity, transaction isolation, proof storage, workload locality, trusted-hardware assumptions, and economic incentives are sharded-ledger-specific."
evidence_window_start: "1982"
evidence_window_end: "2022"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "byzantine-fault-tolerance"
  - "sharded-ledgers"
  - "TEE-assisted BFT"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
  - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
  - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-sharded-ledgers"
query_keys:
  - "BFT consensus for sharded ledgers"
  - "OmniLedger ByzCoinX Atomix bridge"
  - "RingBFT cross-shard consensus topology"
  - "AHL+ TEE-assisted BFT sharding"
created: "2026-06-11"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260621-ahl-sharding"
source_refs:
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "doi:10.14778/3476249.3476275"
  - "arxiv:2107.13047v2"
  - "arxiv:1804.00399v4"
confidence: "medium"
trust_tier: "primary"
---

# BFT consensus -> sharded ledgers

## 命名与路径

- Original title: BFT consensus -> sharded ledgers
- File slug: `bft-consensus-to-sharded-ledgers`
- Path safety check: migrated to `05_Bridges/bft-consensus-to-sharded-ledgers.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/bft-consensus-to-sharded-ledgers.md` 迁移而来。端点 knowledge refs 为: nahida-knowledge-byzantine-fault-tolerance, nahida-knowledge-sharded-ledgers。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: BFT consensus -> sharded ledgers

## 连接命题

- From: `distributed-systems/consensus/byzantine-fault-tolerance`
- To: `blockchain-systems/scaling-and-sharding/sharded-ledgers`
- Relation types: dependency, implementation_reuse, translation
- Directionality: one_way
- Relationship thesis: Sharded ledgers reuse Byzantine fault-tolerant consensus inside each shard, but add global validator assignment, cross-shard atomic commit, transaction isolation, cross-shard consensus topology, state checkpointing, workload-locality constraints, and sometimes trusted-hardware assumptions to make committee sizing practical.

## 端点范围

| Endpoint | Path | Scope in bridge | Evidence | Notes |
| --- | --- | --- | --- | --- |
| Distributed BFT | `distributed-systems/consensus/byzantine-fault-tolerance` | arbitrary Byzantine faults, quorum/intersection, practical BFT SMR | Byzantine Generals, PBFT | existing seed |
| Sharded ledgers | `blockchain-systems/scaling-and-sharding/sharded-ledgers` | multiple BFT shards plus cross-shard transaction processing, isolation, secure validator assignment, and sometimes TEE-assisted committee sizing | OmniLedger; ByShard; AHL | active_seed |
| Sharded ring consensus | `blockchain-systems/scaling-and-sharding/sharded-ledgers` | ring-topology cross-shard BFT consensus and linear shard-to-shard communication | RingBFT | active_seed |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Byzantine fault threshold | BFT topic | Shard-level consensus | each shard requires less than one-third Byzantine validators for ByzCoinX consensus | OmniLedger p3-p4,p9-p10 | global security depends on random assignment |
| State-machine replication | PBFT/SMR | shard ledger | each shard maintains ordered UTXO state | OmniLedger p2,p7-p8 | cross-shard transactions are outside single SMR |
| View change/timeouts | PBFT | ByzCoinX | shard leader failure uses PBFT-like view change and increasing timeouts | OmniLedger p7,p10 | group topology changes performance/failure behavior |
| Checkpointing | PBFT stable checkpoints | State blocks | state blocks summarize shard UTXO state | OmniLedger p8 | clients must store proofs |
| Atomic commit | distributed systems | Atomix | lock/unlock protocol adapts atomic commit to Byzantine shards | OmniLedger p5-p7 | client-driven liveness responsibility |
| Shard-step ordering | PBFT/SMR | ByShard OEM | each shard uses consensus to order Vote/Commit/Abort shard-steps | ByShard §3.2 | cross-shard order still needs orchestration |
| Consensus-wrapped 2PC | BFT topic | ByShard orchestration | linear/centralized/distributed orchestration adapt 2PC under Byzantine shards | ByShard §4 | latency/message trade-offs differ by topology |
| Deterministic locks | SMR determinism | ByShard 2PL execution | deterministic wait queues allow lock waits/wakeups without extra consensus | ByShard §5.2 | contention remains an application workload issue |
| Ring-topology forwarding | BFT shard consensus | RingBFT cross-shard consensus | each shard locally orders and locks, then forwards signed commit proof to the next involved shard | RingBFT §4 | assumes known read/write sets and deterministic transactions |
| Remote view-change | BFT view-change | cross-shard recovery | next shard can trigger previous shard view-change after partial communication failure | RingBFT §5.1.2 | liveness still depends on periods of synchrony |
| Non-equivocating BFT threshold | BFT fault model | shard committee sizing | AHL+ uses TEE append-only logs to prevent equivocation, allowing `N=2f+1` non-equivocating Byzantine tolerance and smaller committees | AHL §4.1, §5.2 | depends on TEE integrity, signing keys and rollback defenses |
| Consensus communication tuning | PBFT implementation | shard throughput | AHL+ separates consensus/request queues and removes redundant request broadcast to avoid dropped consensus messages | AHL §4.1, §7.1 | still PBFT-like and sensitive to WAN/view-change behavior |
| TEE randomness for validator assignment | BFT/sharding safety | shard formation | RandomnessBeacon gives efficient random committee assignment, then BFT committee thresholds determine shard failure probability | AHL §5.1-§5.2 | synchronous `Delta` and TEE restart/rollback assumptions remain |

## 不可迁移边界

- Classical BFT does not solve validator sampling or Sybil-resistant identities.
- Shard compromise probability is a global random-sampling problem, not only a local BFT threshold.
- Cross-shard transactions need additional atomic commit logic.
- Cross-shard transactions may also need isolation/concurrency-control logic and topology/recovery choices, not only atomic commit.
- Ledger pruning changes proof responsibility and historical availability.
- TEE-assisted BFT changes the fault model by removing equivocation; it does not remove the need to trust hardware integrity, attestation, signing keys and rollback defenses.
- Economic incentives and anti-censorship require blockchain-specific mechanisms.

## 路径传播

| Endpoint path | Pack update | Relation/index update | Synthesis action | Status |
| --- | --- | --- | --- | --- |
| `distributed-systems/consensus/byzantine-fault-tolerance` | bridge refreshed through ByShard, RingBFT and AHL | relation rows indexed | existing BFT synthesis receives AHL source extension only | active_seed |
| `blockchain-systems/scaling-and-sharding/sharded-ledgers` | direction/topic pack refreshed through ByShard, RingBFT and AHL | relation rows indexed | sharded-ledgers synthesis refreshed | active_seed |

## 查询入口

- BFT consensus 如何迁移到 sharded ledger?
- OmniLedger 为什么还需要 Atomix?
- ByShard 为什么还需要 OEM/2PC/2PL?
- RingBFT 为什么选择 ring order 和 linear communication?
- AHL+ 为什么通过 TEE non-equivocation 改变 shard committee sizing?
- Sharded ledger 的安全问题和普通 BFT group 有什么区别?

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `application, dependency, translation` | endpoint paths above | source notes and bridge detail | BFT quorum and shard-level consensus transfer; secure random validator assignment, cross-shard atomicity, transaction isolation, proof storage, workload locality, trusted hardware, and economic incentives are sharded-ledger-specific. |


## 类比、依赖或关系边界

BFT quorum and shard-level consensus transfer; secure random validator assignment, cross-shard atomicity, transaction isolation, proof storage, workload locality, trusted hardware, and economic incentives are sharded-ledger-specific.


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[doi-10-1145-357172-357176-byzantine-generals-problem|doi-10-1145-357172-357176-byzantine-generals-problem]] | source_note_refs | active_seed |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|doi-10-5555-296806-296824-practical-byzantine-fault-tolerance]] | source_note_refs | active_seed |
| [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding]] | source_note_refs | active_seed |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment]] | source_note_refs | active_seed |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology]] | source_note_refs | active_seed |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding]] | source_note_refs | active_seed |


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |

## 刷新规则

- Last checked: `2026-06-21`
- Valid until: `2026-07-21`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
