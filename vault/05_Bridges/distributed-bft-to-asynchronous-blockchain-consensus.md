---
id: "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
title: "Distributed BFT -> asynchronous blockchain consensus"
original_title: "Distributed BFT -> asynchronous blockchain consensus"
file_slug: "distributed-bft-to-asynchronous-blockchain-consensus"
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
  - "distributed-systems/consensus/asynchronous-bft-consensus"
endpoint_knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-asynchronous-bft-consensus"
from_domain: "distributed-systems"
to_domain: "distributed-systems"
from_direction: "consensus"
to_direction: "consensus"
from_topic: "byzantine-fault-tolerance"
to_topic: "asynchronous-bft-consensus"
relation_types:
  - "application"
  - "translation"
  - "dependency"
directionality: "uncertain"
relationship_thesis: "Asynchronous blockchain consensus applies Byzantine fault-tolerant agreement, AVSS/global-coin liveness primitives, publicly verifiable and dual-threshold VSS setup primitives, externally-valid agreement primitives, long-message reliable broadcast/data dissemination, and trusted-dealer-free threshold setup to WAN ledger ordering, but adds workload-adaptive proposal/execution mechanics, data availability policy, transaction policy, key-management operations, and common-coin engineering that classical BFT seeds do not cover."
transferability: "medium"
non_transfer_boundary: "The BFT fault threshold, quorum-intersection safety intuition, AVSS-backed common-randomness intuition, publicly verifiable and dual-threshold VSS setup idea, VABA external-validity framing, ADD/RBC long-message dissemination idea, and ADKG trusted-dealer-free setup idea transfer; fixed-slot overhead, pass/skip advancement, timestamp efficiency, adaptive corruption, production key refresh, validator membership, production common-coin liveness, data availability sampling, mempool policy, transaction selection, execution, and WAN workload behavior are asynchronous blockchain consensus-specific."
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "byzantine-fault-tolerance"
  - "asynchronous-bft-consensus"
  - "validated-asynchronous-byzantine-agreement"
  - "asynchronous-verifiable-secret-sharing"
  - "dual-threshold-avss"
  - "asynchronous-distributed-key-generation"
  - "asynchronous-data-dissemination"
  - "asynchronous-reliable-broadcast"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
  - "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
  - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
  - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
  - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
  - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
  - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
  - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
  - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
  - "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-asynchronous-bft-consensus"
  - "nahida-knowledge-validated-asynchronous-byzantine-agreement"
  - "nahida-knowledge-asynchronous-verifiable-secret-sharing"
  - "nahida-knowledge-dual-threshold-asynchronous-vss"
  - "nahida-knowledge-asynchronous-distributed-key-generation"
  - "nahida-knowledge-asynchronous-data-dissemination"
  - "nahida-knowledge-asynchronous-reliable-broadcast"
query_keys:
  - "Distributed BFT -> asynchronous blockchain consensus"
  - "VABA"
  - "external validity for asynchronous BFT"
  - "AVSS-backed global coin"
  - "asynchronous verifiable secret sharing"
  - "dual-threshold AVSS"
  - "publicly verifiable VSS"
  - "ADKG"
  - "trusted-dealer-free threshold setup"
  - "asynchronous distributed key generation"
  - "asynchronous data dissemination"
  - "asynchronous reliable broadcast"
  - "long-message RBC"
  - "high-threshold ADKG"
  - "distributed polynomial sampling"
created: "2026-06-12"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement"
  - "nahida-knowledge-20260623-canetti-rabin-optimal-async-ba"
  - "nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft"
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
  - "nahida-knowledge-20260623-verifiable-secret-sharing-simplified"
  - "nahida-knowledge-20260623-high-threshold-adkg-polynomial-sampling"
source_refs:
  - "doi:10.1145/357172.357176"
  - "doi:10.1145/167088.167105"
  - "doi:10.5555/296806.296824"
  - "doi:10.1145/3600006.3613164"
  - "doi:10.1145/3293611.3331612"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "iacr:2019/1015"
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "usenix:security23/das"
confidence: "medium"
trust_tier: "primary"
---

# Distributed BFT -> asynchronous blockchain consensus

## 命名与路径

- Original title: Distributed BFT -> asynchronous blockchain consensus
- File slug: `distributed-bft-to-asynchronous-blockchain-consensus`
- Path safety check: migrated to `05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md`.

## 端点基础说明

本 bridge 从 legacy `06_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md` 迁移而来。端点 knowledge refs 为: nahida-knowledge-byzantine-fault-tolerance, nahida-knowledge-asynchronous-bft-consensus。关系命题、迁移矩阵和不可迁移边界保留 legacy bridge 的 source-backed 内容，并改由当前 `04_Knowledge` 节点承接。



## Legacy Detail: Distributed BFT -> asynchronous blockchain consensus

## Thesis

Asynchronous blockchain consensus applies Byzantine fault-tolerant agreement, AVSS/global-coin liveness primitives, publicly verifiable and dual-threshold VSS setup primitives, externally-valid agreement primitives, long-message reliable broadcast/data dissemination, and trusted-dealer-free threshold setup to WAN ledger ordering, but adds workload-adaptive proposal/execution mechanics, adaptive-corruption security, production key-management, data availability policy, transaction-selection, and common-coin engineering that classical BFT seeds do not cover.

## Endpoints

| Endpoint | Scope | Current evidence | Status |
| --- | --- | --- | --- |
| `distributed-systems/consensus/byzantine-fault-tolerance` | arbitrary faults, quorum intersection, IC/SMR foundation | Byzantine Generals, PBFT | active_seed |
| `blockchain-systems/consensus/asynchronous-bft-consensus` | leaderless/asynchronous BFT SMR for WAN blockchain workloads plus VABA/ACS/adaptive-security branches | VABA; MyTumbler/SuperMA; EPIC | active_seed |

## Transfer Matrix

| Pattern | Transfers? | Evidence | Boundary |
| --- | --- | --- | --- |
| `f < n/3` quorum intersection | yes | MyTumbler §2, §4.1; PBFT/BFT seeds | assumes symmetric trust, unlike Cobalt |
| State-machine replication safety | yes | MyTumbler §2, PBFT | executability needs pass/timestamp handling |
| Leaderless proposal | partial | MyTumbler §1-§4 | classical BFT seeds do not settle workload/slot behavior |
| Common coin/randomization | partial | Canetti-Rabin §8-§9; MyTumbler §5, §7.3 | AVSS-backed global coin transfers as a foundation idea; production coin engineering, key setup, private-channel assumptions and blockchain workload integration remain system-specific |
| Asynchronous verifiable secret sharing | partial | Canetti-Rabin Definition 2, §5-§8 | helps explain how async BA can generate shared randomness under Byzantine faults; it is not a mempool, validator-set, transaction-validity or economic-finality mechanism |
| Publicly verifiable / dual-threshold VSS | partial | VSS Simplified Definitions 1-3, Algorithms 1-3, §8 | transfers as threshold setup/common-randomness primitive; it is not production key rotation, membership management, transaction policy, execution or data availability |
| Asynchronous distributed key generation | partial | ADKG 2019/1015 Theorem 1.1, §3-§6 | trusted-dealer-free threshold setup transfers as a primitive for coins/signatures; production key rotation, validator membership, DKG scheduling and implementation hardening remain system-specific |
| Long-message reliable broadcast/data dissemination | partial | ADD 2021/777 Definition 3.1, §4.2 | ADD/RBC explains how large proposals, shares or proof material can be moved efficiently; it is not data availability sampling, mempool policy, execution or validator-set governance |
| Externally valid multi-valued agreement | partial | VABA 2019 Definition 4, Theorem 1 | external validity transfers toward Atomic Broadcast/SMR, but the application predicate, transaction dissemination, mempool policy, and validator economics remain system-specific |
| Production WAN performance | no | MyTumbler §6 | empirical scope and cloud setup matter |
| Adaptive corruption model | partial | EPIC §I, §III, §V.C | classical BFT fault threshold transfers, but static-vs-adaptive cryptographic setup does not |
| Threshold-crypto setup | no | EPIC §VI, Figure 4, Figure 14 | trusted dealer, DKG, and synchronous setup are protocol-specific deployment assumptions |
| Transaction selection and censorship | no | EPIC §VI, Table II | FIFO/random/HYB choices affect throughput and censorship-resilience beyond BFT safety |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| Byzantine fault tolerance | provides | quorum-intersection safety basis | BFT/PBFT + MyTumbler §4.1 | high | active_seed |
| MyTumbler | translates | BFT SMR to asynchronous WAN blockchain workloads | MyTumbler §1-§6 | high | active_seed |
| SuperMA/FastBA promise fast-path route | evidenced_by | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | MyTumbler §5; extends asynchronous agreement with promise fast paths | high | active_seed |
| Common coin fallback for asynchronous liveness | evidenced_by | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | MyTumbler §5, §7.3 | high | active_seed |
| AVSS-backed global coin | provides | randomized liveness foundation for optimal-resilience asynchronous BA | Canetti-Rabin 1993 §5-§9 | high | active_seed |
| Publicly verifiable / dual-threshold VSS | provides | public transcript and higher-threshold setup primitive for async BFT threshold/rand beacon layers | VSS Simplified 2023/1196 Definitions 1-3, Algorithms 1-3, §8 | high | active_seed |
| ADKG | provides | trusted-dealer-free threshold setup for common coins, VABA and threshold signatures | ADKG 2019/1015 Theorem 1.1, §3-§6; Das et al. 2023 Algorithm 1, Theorem 2, Table 3 | high | active_seed |
| ADD/RBC | provides | efficient long-message dissemination for RBC, AVSS/ACSS and ADKG payloads | ADD 2021/777 Definition 3.1, §4-§5 | high | active_seed |
| VABA | translates | async BFT agreement into externally valid Atomic Broadcast/SMR primitive | VABA 2019 Definition 4, Theorem 1, §3 | high | active_seed |
| EPIC | translates | ACS asynchronous BFT into adaptive-security setting | EPIC §V.C-§VI | high | active_seed |
| EPIC | replaces | threshold encryption with HYB transaction selection | EPIC §VI | high | active_seed |
| EPIC DKG | changes | setup assumption from trusted dealer to synchronous distributed key generation | EPIC §VI, Figure 14 | high | active_seed |

## Limits

- 这个 bridge 不替代 FLP/Bracha/Mostefaoui/HBBFT/Narwhal/Tusk 或 Canetti-Rabin technical report 直接 source。
- Canetti-Rabin 的 AVSS/global coin 说明 async BA 的随机性层如何成立，但 private channels、secret-sharing proofs、global coin engineering 和 modern threshold setup 不能自动迁移为区块链生产实现。
- VSS Simplified 的 publicly verifiable / dual-threshold VSS 说明 threshold setup 可以获得公开可验 transcript、异步终止和更高 secrecy threshold，但不能自动给出 production key rotation、validator-set membership、DKG scheduling、common-coin engineering 或链上执行策略。
- ADKG 2019/1015 说明 threshold setup 可以在异步网络中去 trusted dealer，但不自动给出生产 key rotation、validator-set membership、reconfiguration、DKG scheduling 或实现安全。
- Das et al. 2023 说明 high-threshold ADKG 可以通过 distributed polynomial sampling 获得 practical WAN prototype evidence，但它仍不自动给出 production validator membership、key rotation、DKG scheduling、common-coin liveness engineering 或链上执行策略。
- ADD 2021/777 说明长消息 reliable broadcast 和 data dissemination 可降通信成本，但不自动给出 blockchain data availability sampling、mempool policy、transaction selection、execution scheduling 或 storage availability design。
- VABA 的 external validity 只说明 agreement 决定值要满足应用谓词；它不替代 mempool、transaction dissemination、data availability、validator membership 或 economic-finality 设计。
- Cobalt-style open-network non-uniform trust 和 MyTumbler symmetric trust 不能合并成同一个 quorum model。
- Stratus 的 shared-mempool split 与 MyTumbler 的 flexible advancement 是不同性能边界: 一个处理 transaction dissemination，一个处理 asynchronous fixed-slot/executability。
- EPIC 的 adaptive-security branch 与 MyTumbler 的 flexible-advancement branch 是互补关系: 前者处理 corruption/setup/selection，后者处理 ordering/executability/workload。

## 连接命题

- From: `distributed-systems/consensus/byzantine-fault-tolerance`
- To: `distributed-systems/consensus/asynchronous-bft-consensus`
- Relation types: application, translation, dependency
- Directionality: `uncertain`
- Relationship thesis: Asynchronous blockchain consensus applies Byzantine fault-tolerant agreement, AVSS/global-coin liveness primitives, publicly verifiable and dual-threshold VSS setup primitives, externally-valid agreement primitives, long-message reliable broadcast/data dissemination, and trusted-dealer-free threshold setup to WAN ledger ordering, but adds workload-adaptive proposal/execution mechanics, data availability policy, transaction policy, key-management operations, and common-coin engineering that classical BFT seeds do not cover.


## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| nahida-knowledge-byzantine-fault-tolerance | `distributed-systems/consensus/byzantine-fault-tolerance` | bridge endpoint | endpoint knowledge + source notes | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | `distributed-systems/consensus/asynchronous-bft-consensus` | bridge endpoint | endpoint knowledge + source notes | active_seed |


## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| `application, translation, dependency` | endpoint paths above | source notes and legacy bridge detail | The BFT fault threshold, quorum-intersection safety intuition, AVSS-backed common-randomness intuition, publicly verifiable / dual-threshold VSS setup idea, VABA external-validity framing, and ADKG trusted-dealer-free setup idea transfer; fixed-slot overhead, pass/skip advancement, timestamp efficiency, adaptive corruption, production key refresh, validator membership, production common-coin liveness, transaction dissemination, transaction selection, execution, and WAN workload behavior are asynchronous blockchain consensus-specific. |
| publicly verifiable / dual-threshold VSS | async BFT threshold setup / common-randomness layer | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] | transfers transcript/secrecy-threshold primitive, not production key management or ledger execution |
| ADD/RBC payload dissemination | async BFT ordering / proposal availability | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] | transfers communication primitive intuition, not DAS, mempool policy or execution semantics |


## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| ADKG setup primitive | `distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation` | `distributed-systems/consensus/asynchronous-bft-consensus` | dependency, setup_transfer | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] | transfers setup idea, not production membership/key-rotation operations |
| ADD/RBC dissemination primitive | `distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination` | `distributed-systems/consensus/asynchronous-bft-consensus` | dependency, payload_dissemination_transfer | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] | transfers long-message broadcast cost model, not data availability sampling or transaction policy |
| publicly verifiable / dual-threshold VSS | `distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss` | `distributed-systems/consensus/asynchronous-bft-consensus` | dependency, setup_transfer | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] | transfers setup/common-randomness primitive, not production key rotation, membership or execution |
| bridge relation | `distributed-systems/consensus/byzantine-fault-tolerance` | `distributed-systems/consensus/asynchronous-bft-consensus` | application, translation, dependency | source notes / legacy detail | The BFT fault threshold, quorum-intersection safety intuition, AVSS-backed common-randomness intuition, publicly verifiable / dual-threshold VSS setup idea, VABA external-validity framing, and ADKG trusted-dealer-free setup idea transfer; fixed-slot overhead, pass/skip advancement, timestamp efficiency, adaptive corruption, production key refresh, validator membership, production common-coin liveness, transaction dissemination, transaction selection, execution, and WAN workload behavior are asynchronous blockchain consensus-specific. |


## 类比、依赖或关系边界

The BFT fault threshold, quorum-intersection safety intuition, AVSS-backed common-randomness intuition, publicly verifiable / dual-threshold VSS setup idea, VABA external-validity framing, ADD/RBC long-message dissemination idea, and ADKG trusted-dealer-free setup idea transfer; fixed-slot overhead, pass/skip advancement, timestamp efficiency, adaptive corruption, production key refresh, validator membership, production common-coin liveness, data availability sampling, mempool policy, transaction selection, execution, and WAN workload behavior are asynchronous blockchain consensus-specific.


## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[doi-10-1145-357172-357176-byzantine-generals-problem|doi-10-1145-357172-357176-byzantine-generals-problem]] | source_note_refs | active_seed |
| [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Fast Asynchronous Byzantine Agreement with Optimal Resilience]] | AVSS-backed global coin and optimal-resilience async BA foundation | active_seed |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus]] | source_note_refs | active_seed |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|doi-10-5555-296806-296824-practical-byzantine-fault-tolerance]] | source_note_refs | active_seed |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement]] | VABA external-validity transfer evidence | active_seed |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security]] | source_note_refs | active_seed |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | trusted-dealer-free threshold setup transfer evidence | active_seed |
| [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling]] | practical high-threshold ADKG / distributed polynomial sampling setup evidence | active_seed |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | long-message reliable broadcast and data dissemination transfer evidence | active_seed |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | publicly verifiable / dual-threshold VSS setup transfer evidence | active_seed |


## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/consensus/byzantine-fault-tolerance` | update Bridge Links and relation_edges | active_seed |
| `distributed-systems/consensus/asynchronous-bft-consensus` | update Bridge Links and relation_edges | active_seed |


## 查询入口

- Distributed BFT -> asynchronous blockchain consensus


## 复核笔记

- Repair pass: endpoint refs, relation types, source note refs, reciprocal propagation and indexes should be checked by audit.
- Maturity: `active_seed`.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| endpoint knowledge refs | Bridge Links / 关系图谱 | legacy bridge migrated | active_seed |
| nahida-knowledge-validated-asynchronous-byzantine-agreement | Bridge Links / transfer boundary | VABA clarifies the externally-valid agreement layer between generic BFT and Atomic Broadcast/SMR applications | active_seed |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | Bridge Links / transfer boundary | AVSS clarifies the shared-randomness/global-coin layer beneath randomized asynchronous BA | active_seed |
| nahida-knowledge-dual-threshold-asynchronous-vss | Bridge Links / transfer boundary | dual-threshold AVSS clarifies which publicly verifiable threshold setup ideas can transfer without becoming production key management | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | Bridge Links / transfer boundary | ADKG clarifies which threshold-crypto setup assumptions can be protocolized before async BFT/VABA use them | active_seed |
| nahida-knowledge-asynchronous-data-dissemination | Bridge Links / transfer boundary | ADD clarifies which long-message dissemination costs can transfer to async ordering workloads without becoming mempool/DAS policy | active_seed |
| nahida-knowledge-asynchronous-reliable-broadcast | Bridge Links / transfer boundary | RBC clarifies reliable proposal/payload propagation below ACS and async atomic broadcast | active_seed |

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
