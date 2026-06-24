---
id: "nahida-bridge-data-availability-to-sharded-ledgers"
title: "Data availability -> sharded ledgers"
original_title: "Data availability -> sharded ledgers"
file_slug: "data-availability-to-sharded-ledgers"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active"
hierarchy_level: "bridge"
bridge_kind: "cross_path"
bridge_status: "active_seed"
endpoint_paths:
  - "blockchain-systems/data-availability-and-light-clients/data-availability-sampling"
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers"
endpoint_knowledge_refs:
  - "nahida-knowledge-data-availability-sampling"
  - "nahida-knowledge-sharded-ledgers"
from_domain: "blockchain-systems"
to_domain: "blockchain-systems"
from_direction: "data-availability-and-light-clients"
to_direction: "scaling-and-sharding"
from_topic: "data-availability-sampling"
to_topic: "sharded-ledgers"
relation_types:
  - "dependency"
  - "shared_pattern"
directionality: "bidirectional"
relationship_thesis: "Sharded ledgers and data-availability ledgers are two scaling routes that reduce global execution burden: sharding distributes execution across validator subsets, while LazyLedger removes execution from consensus and keeps a shared data-availability/order layer. Fraud/DA proofs add the light-client safety pattern for systems where no single node verifies all data or shards."
transferability: "medium"
non_transfer_boundary: "Shard-level execution, cross-shard atomicity, and validator assignment from OmniLedger do not transfer directly to LazyLedger; LazyLedger's namespace/data-availability model and fraud/DA proofs do not by themselves validate application state, assign shard committees, or solve cross-shard execution."
evidence_window_start: "2017"
evidence_window_end: "2019"
domains:
  - "blockchain-systems"
topics:
  - "data-availability-sampling"
  - "sharded-ledgers"
  - "fraud-proofs"
source_note_refs:
  - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
  - "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
  - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
knowledge_refs:
  - "nahida-knowledge-data-availability-sampling"
  - "nahida-knowledge-sharded-ledgers"
query_keys:
  - "data availability vs sharding"
  - "LazyLedger OmniLedger scaling comparison"
  - "fraud proofs sharding"
  - "data availability proofs sharded ledgers"
created: "2026-06-11"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260621-fraud-proofs-data-availability"
source_refs:
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "arxiv:1905.09274v4"
  - "arxiv:1809.09044v1"
  - "doi:10.48550/arxiv.1809.09044"
confidence: "medium"
trust_tier: "primary"
---

# Data availability -> sharded ledgers

## 命名与路径

- Original title: Data availability -> sharded ledgers
- File slug: `data-availability-to-sharded-ledgers`
- Path safety check: migrated to `05_Bridges/data-availability-to-sharded-ledgers.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/data-availability-to-sharded-ledgers.md` 迁移而来。端点 knowledge refs 为: nahida-knowledge-data-availability-sampling, nahida-knowledge-sharded-ledgers。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: Data availability -> sharded ledgers

## 连接命题

- From: `blockchain-systems/data-availability-and-light-clients/data-availability-sampling`
- To: `blockchain-systems/scaling-and-sharding/sharded-ledgers`
- Relation types: tension, shared_pattern, co_evolution
- Directionality: bidirectional
- Relationship thesis: Sharded ledgers and data-availability ledgers are two scaling routes that reduce global execution burden: sharding distributes execution across validator subsets, while LazyLedger removes execution from consensus and keeps a shared data-availability/order layer. [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] adds the light-client safety pattern: when validators/full nodes do not all validate all data, fraud proofs need data availability before invalidity can be propagated to light clients.

## 对比矩阵

| 维度 | OmniLedger / sharded ledgers | LazyLedger / data availability ledger | 证据 |
| --- | --- | --- | --- |
| Scaling strategy | 多 shard 并行执行/验证交易 | base layer 不执行应用交易，只排序并保证数据可用 | OmniLedger p1-p8; LazyLedger p1-p6 |
| Cross-application/state | Atomix 处理 cross-shard UTXO atomicity | dependencies and application state sovereignty | OmniLedger p5-p7; LazyLedger p7-p8 |
| Client role | client 驱动 Atomix unlock，仍依赖 shard consensus 执行 | client 执行应用状态机并验证 namespace data | LazyLedger p6-p10 |
| Proof/data structure | shard state blocks and transaction proofs | namespaced Merkle trees and DA sampling | OmniLedger p8; LazyLedger p3-p10 |
| Light-client invalidity detection | shard-local invalidity must be exposed across partial validators/clients | fraud proofs require data availability before honest challengers can prove invalid state or malformed coding | Fraud Proofs §3-§7 |
| Limitation | workload locality/adaptive adversary | application light clients and dependency coupling | OmniLedger p13,p15; LazyLedger p13 |

## 不可迁移边界

- OmniLedger 的 shard validator assignment 不适用于 LazyLedger，因为 LazyLedger 不把执行分到 shards。
- LazyLedger 的 DA sampling 不自动保证 application transaction validity。
- Fraud proofs/data availability proofs 不自动解决 shard committee assignment、cross-shard atomicity 或 shard execution semantics。
- 两者都降低 global processing burden，但一个靠并行执行，一个靠延迟/转移执行职责。

## 路径传播

| Endpoint path | Pack update | Relation/index update | Synthesis action | Status |
| --- | --- | --- | --- | --- |
| `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | new topic pack created | bridge row indexed | data availability synthesis created | active_seed |
| `blockchain-systems/scaling-and-sharding/sharded-ledgers` | bridge added | bridge row indexed | sharded-ledgers synthesis remains seed | active_seed |

## 查询入口

- LazyLedger 和 OmniLedger 的 scaling 思路有什么区别?
- Data availability 能否替代 sharding?
- 为什么 DA layer 不等于 execution validity?

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| nahida-knowledge-data-availability-sampling | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-sharded-ledgers | `blockchain-systems/scaling-and-sharding/sharded-ledgers` | bridge endpoint | endpoint knowledge + source notes | active_seed |


## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `dependency, shared_pattern` | endpoint paths above | source notes and legacy bridge detail | Shard-level execution, cross-shard atomicity, and validator assignment from OmniLedger do not transfer directly to LazyLedger; LazyLedger's namespace/data-availability model and fraud/DA proofs do not by themselves validate application state or solve shard execution. |


## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| bridge relation | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | `blockchain-systems/scaling-and-sharding/sharded-ledgers` | dependency, shared_pattern | source notes / legacy detail | Shard-level execution, cross-shard atomicity, and validator assignment from OmniLedger do not transfer directly to LazyLedger; LazyLedger's namespace/data-availability model and fraud/DA proofs do not by themselves validate application state or solve shard execution. |
| fraud/DA proof pattern | `blockchain-systems/data-availability-and-light-clients/fraud-proofs` | `blockchain-systems/scaling-and-sharding/sharded-ledgers` | light-client invalidity detection | Fraud Proofs §3-§7 | assuming DA/fraud proof replaces shard execution or cross-shard transaction protocol |


## 类比、依赖或关系边界

Shard-level execution, cross-shard atomicity, and validator assignment from OmniLedger do not transfer directly to LazyLedger. LazyLedger's namespace/data-availability model and Fraud Proofs' fraud/DA proof pattern do not by themselves validate application state, assign shard committees, or solve cross-shard execution.


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding]] | source_note_refs | active_seed |
| [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts]] | source_note_refs | active_seed |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] | fraud/DA proof transfer boundary for light clients and sharding | active_seed |


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |
| [[fraud-proofs|Fraud proofs]] | transfer boundary | records why sharded systems may need data-available invalidity proofs without turning sharding into DA | active_seed |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-fraud-proofs-data-availability | Added fraud/DA proof light-client safety boundary to the data-availability/sharding bridge. | 1 source note | codex |

## 刷新规则

- Last checked: `2026-06-21`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
