---
id: "nahida-bridge-distributed-bft-to-blockchain-finality"
title: "Distributed BFT -> blockchain finality"
original_title: "Distributed BFT -> blockchain finality"
file_slug: "distributed-bft-to-blockchain-finality"
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
  - "blockchain-systems/consensus/proof-of-stake-finality"
endpoint_knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-proof-of-stake-finality"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "consensus"
to_direction: "consensus"
from_topic: "byzantine-fault-tolerance"
to_topic: "proof-of-stake-finality"
relation_types:
  - "application"
  - "dependency"
  - "translation"
directionality: "one_way"
relationship_thesis: "Blockchain proof-of-stake finality applies Byzantine fault-tolerant consensus ideas to stake-weighted validators, adding economic accountability and long-range attack assumptions."
transferability: "medium"
non_transfer_boundary: "Classical BFT quorum and safety arguments transfer; token economics, validator churn, unbonding periods, light-client trust, and long-range attacks require blockchain-specific assumptions."
evidence_window_start: "1982"
evidence_window_end: "2014"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "byzantine-fault-tolerance"
  - "proof-of-stake-finality"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
  - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
  - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
  - "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-proof-of-stake-finality"
query_keys:
  - "BFT to PoS finality"
  - "Tendermint Byzantine consensus bridge"
created: "2026-06-11"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
source_refs:
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1710.09437v4"
confidence: "medium"
trust_tier: "primary"
---

# Distributed BFT -> blockchain finality

## 命名与路径

- Original title: Distributed BFT -> blockchain finality
- File slug: `distributed-bft-to-blockchain-finality`
- Path safety check: migrated to `05_Bridges/distributed-bft-to-blockchain-finality.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/distributed-bft-to-blockchain-finality.md` 迁移而来。端点 knowledge refs 为: nahida-knowledge-byzantine-fault-tolerance, nahida-knowledge-proof-of-stake-finality。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: Distributed BFT -> blockchain finality

## 连接命题

- From: `distributed-systems/consensus/byzantine-fault-tolerance`
- To: `blockchain-systems/consensus/proof-of-stake-finality`
- Relation types: application, dependency, translation
- Directionality: one_way
- Relationship thesis: Blockchain proof-of-stake finality applies Byzantine fault-tolerant consensus ideas to stake-weighted validators, adding economic accountability and long-range attack assumptions.

## 端点范围

| Endpoint | Path | Scope in bridge | Evidence | Notes |
| --- | --- | --- | --- | --- |
| Distributed BFT | `distributed-systems/consensus/byzantine-fault-tolerance` | arbitrary faulty participants, quorum/intersection, state-machine replication foundations | Byzantine Generals, PBFT | source-backed seed |
| Blockchain finality | `blockchain-systems/consensus/proof-of-stake-finality` | stake-weighted validators, 2/3 commits, slashing evidence, unbonding window, finality overlay, inactivity leak | Tendermint p1-p10; Casper p1-p10 | source-backed seed |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Byzantine fault threshold | BFT topic | PoS finality | <1/3 Byzantine voting power maps to stake-weighted validator voting | Tendermint p5, p8 | Voting power is economic stake, not one-process-one-vote |
| Quorum intersection | BFT/PBFT | PoS finality | 2/3 commit sets imply overlap/accountability | Tendermint p3-p4 | Accountability depends on evidence and unbonding |
| Partial synchrony | DLS/PBFT background | Tendermint liveness | liveness assumes unknown finite delay and increasing timeouts | Tendermint p4-p5 | DLS source still missing |
| Accountable safety | BFT safety | Casper FFG | conflicting finality implies slashable >=1/3 deposits | Casper p4-p5 | Evidence enforcement and client rules matter |
| Finality overlay | Leader/finality separation | Casper FFG | proposal mechanism is separated from finality gadget | Casper p1-p2 | Liveness still depends on proposal mechanism |

## 不可迁移边界

- Classical BFT does not directly cover proof-of-stake economics.
- Slashing only helps if evidence is available before funds are spendable.
- Long-range attacks are blockchain-specific and need client sync/trust assumptions.
- Modern production concerns such as validator set updates and light clients require later sources.
- Casper adds dynamic validator set stitching and inactivity leak, but still leaves modern spec/incentive analysis as future work.

## 路径传播

| Endpoint path | Pack update | Relation/index update | Synthesis action | Status |
| --- | --- | --- | --- | --- |
| `distributed-systems/consensus/byzantine-fault-tolerance` | Add Tendermint as blockchain application bridge | bridge row indexed | existing BFT synthesis remains seed | active_seed |
| `blockchain-systems/consensus/proof-of-stake-finality` | Create topic map/synthesis | bridge row indexed | create PoS finality topic synthesis | active_seed |

## 查询入口

- BFT 如何迁移到 PoS finality?
- Tendermint 与 PBFT/DLS 有什么关系?
- 为什么 PoS finality 需要 unbonding period?

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `application, dependency, translation` | endpoint paths above | source notes and legacy bridge detail | Classical BFT quorum and safety arguments transfer; token economics, validator churn, unbonding periods, light-client trust, and long-range attacks require blockchain-specific assumptions. |


## 类比、依赖或关系边界

Classical BFT quorum and safety arguments transfer; token economics, validator churn, unbonding periods, light-client trust, and long-range attacks require blockchain-specific assumptions.


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[doi-10-1145-357172-357176-byzantine-generals-problem|doi-10-1145-357172-357176-byzantine-generals-problem]] | source_note_refs | active_seed |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|doi-10-5555-296806-296824-practical-byzantine-fault-tolerance]] | source_note_refs | active_seed |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|sha256-9fd9aff80709-tendermint-consensus-without-mining]] | source_note_refs | active_seed |
| [[arxiv-1710-09437v4-casper-friendly-finality-gadget|arxiv-1710-09437v4-casper-friendly-finality-gadget]] | source_note_refs | active_seed |


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
