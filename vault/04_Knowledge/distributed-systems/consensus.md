---
id: "nahida-knowledge-consensus"
title: "Consensus"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "consensus"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-distributed-systems"
child_knowledge_refs:
  - "nahida-knowledge-asynchronous-bft-consensus"
  - "nahida-knowledge-byzantine-fault-tolerance"
  - "nahida-knowledge-crash-fault-tolerance"
ontology_path:
  - "distributed-systems"
  - "consensus"
primary_ontology_path: "distributed-systems/consensus"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-consensus"
    relation: "is_a"
    to: "nahida-knowledge-distributed-systems"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus.md"
      - "vault/04_Knowledge/distributed-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "has_child"
    to: "nahida-knowledge-asynchronous-bft-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "has_child"
    to: "nahida-knowledge-byzantine-fault-tolerance"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "has_child"
    to: "nahida-knowledge-crash-fault-tolerance"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/crash-fault-tolerance.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "high"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
  - "vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md"
  - "vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md"
  - "vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md"
  - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
  - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
  - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
  - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
  - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
  - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
  - "vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md"
  - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
  - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
representative_source_refs:
  - "hal:hal-00944019v2"
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1802.07240"
  - "arxiv:2203.05158"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "doi:10.1145/3293611.3331612"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
  - "iacr:2019/1015"
  - "iacr:2021/777"
query_keys:
  - "Consensus"
  - "consensus"
  - "共识"
  - "Consensus algorithms"
  - "Consensus protocols"
  - "multi-instance BFT"
  - "workload-adaptive consensus"
  - "validated asynchronous Byzantine agreement"
  - "VABA"
  - "asynchronous distributed key generation"
  - "ADKG"
  - "trusted-dealer-free threshold setup"
  - "asynchronous data dissemination"
  - "asynchronous reliable broadcast"
  - "long-message RBC"
aliases:
  - "共识"
  - "Consensus algorithms"
  - "Consensus protocols"
domains:
  - "distributed-systems"
topics:
  - "consensus"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-sraft-scalable-cft"
  - "nahida-knowledge-20260620-stretch-bft"
  - "nahida-paper-intake-20260620-item-0034"
  - "nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement"
  - "nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft"
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
source_refs:
  - "hal:hal-00944019v2"
  - "doi:10.1145/357172.357176"
  - "doi:10.5555/296806.296824"
  - "sha256:0f53a6508592f35812e142b277958af6717bd8b1993532b155d518172f2a66c2"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "sha256:ae33e526eb0f132f8aeddde75be901b4b0024b4b786e68b77adbdbdff69634bf"
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1802.07240"
  - "arxiv:2203.05158"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "doi:10.1145/3293611.3331612"
  - "sha256:a6106319a63e474b5f95328d72e63bfd813aa589a32e7cdcc1295e4ff730d122"
  - "iacr:2019/1015"
  - "iacr:2021/777"
confidence: "medium"
trust_tier: "primary"
---

# Consensus

## 定义与范围

- 定义: Consensus 是分布式节点在故障、延迟或恶意行为下对值、日志顺序、请求序列、区块或检查点形成一致决定的问题和方法族。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `consensus`
- Aliases/query keys: 共识, Consensus algorithms, Consensus protocols
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `consensus`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

该方向由故障模型、时序假设、成员模型、决定对象和数据路径共同决定。Raft/PBFT/Tendermint/VABA 等是代表实例或子问题来源，不是 consensus 本身。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[distributed-systems|distributed-systems]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

为 replicated services、blockchain finality、governance、mempool/order split 和 asynchronous BFT 提供父问题结构。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[distributed-systems|distributed-systems]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[crash-fault-tolerance|crash-fault-tolerance]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[byzantine-fault-tolerance|byzantine-fault-tolerance]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[asynchronous-bft-consensus|asynchronous-bft-consensus]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| CFT replicated log | CFT replicated log: Raft/SRaft | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| BFT SMR | BFT SMR: Byzantine Generals/PBFT | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Externally-valid multi-valued agreement | 让共识决定对象不只是 bit，而是满足应用外部有效性谓词的 value/batch/command。 | atomic broadcast、SMR、异步 BFT 协议需要避免默认 valid value 的空决定。 | 需要 external validity predicate、quality property 和加密/随机化 setup；不覆盖应用层数据传播。 | [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|VABA 2019]] |
| Workload-adaptive BFT | 在 BFT fault model 下用多实例/proposer 并行和 workload feedback 控制吞吐与 latency。 | permissioned/known-membership 或可可靠感知 workload 的系统。 | 需要 recovery、report filtering 和资源边界；不替代 BFT foundation。 | [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT]] |
| Asynchronous BFT | Asynchronous BFT: MyTumbler/SuperMA/EPIC | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Trusted-dealer-free threshold setup | 在 consensus 协议使用 common coin 或 threshold signatures 前，用 ADKG 等分布式 setup 移除 trusted dealer 假设。 | asynchronous BFT/VABA/threshold-signature-based consensus | setup initial cost high；不解决 consensus 决定对象和数据传播问题 | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] |
| Long-message broadcast/dissemination | 在共识进入 agreement 前，用 RBC/ADD 等 primitive 让大 payload、commitment vectors 或 shares 被 honest nodes 获得。 | asynchronous BFT, ACS, AVSS/ACSS, ADKG | 传播层不等于 agreement；不处理 mempool policy 或 data availability sampling | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| Application translation | Application translation: Tendermint/Casper/Cobalt/Stratus | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-357172-357176-byzantine-generals-problem|The Byzantine Generals Problem]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|Practical Byzantine Fault Tolerance]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|In Search of an Understandable Consensus Algorithm]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain]] | paper | 为 CFT replicated log/order 路线增加 permissioned blockchain payload-dissemination 扩展证据 | CFT-only；不是 BFT/permissionless consensus foundation | `p1-p16` |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|Asymptotically Optimal Validated Asynchronous Byzantine Agreement]] | paper | 为 consensus 顶层补入 externally-valid multi-valued agreement 这个决定对象维度，具体吸收在 VABA 子节点 | authenticated async BFT；threshold signatures/coin；不含系统实现 | Definition 4, Theorem 1, §3.1-§3.6 |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | paper | 为 BFT/multi-instance route 增加 permissioned workload-adaptive consensus evidence | permissioned/known-membership；不代表 generic consensus foundation | `p1-p13` |
| [[hal-00944019v2-signature-free-asynchronous-byzantine-consensus|Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages]] | paper | 为 asynchronous BFT consensus 补入 common-coin/BV-broadcast 二值共识 foundation | 依赖 common coin 抽象；不含 blockchain application | Abstract, §3-§4 |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | paper | 为 consensus 顶层补入 threshold-crypto setup 维度：ADKG 可移除 common coin、VABA 和 threshold signatures 的 trusted dealer 假设 | PKI/authenticated links/computational adversary；initial setup `O(n^4)`；不是完整 consensus protocol | Theorem 1.1, §3-§6 |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | paper | 为 consensus 顶层补入 long-message broadcast/dissemination 维度：ADD/RBC 解决 payload movement，支撑 async atomic broadcast、AVSS/ACSS 和 ADKG | `t<n/3` main ADD; hash assumptions for RBC; not itself consensus | Definition 3.1, §4-§6 |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前共识方向已从论文列表合并成 fault-model/problem-axis 入口；Mostefaoui-Moumen-Raynal 2014 source 补强 asynchronous BFT 的 common-coin/BV-broadcast foundation；VABA 2019 补入 externally-valid multi-valued agreement 这一决定对象维度；ADKG 2019/1015 补入 threshold-crypto setup 维度；ADD 2021/777 补入 long-message broadcast/dissemination 维度，说明 consensus 协议的成本还由 payload movement 和 reliable broadcast 子层决定；Stretch-BFT 作为 source extension 补充了 BFT consensus 在 permissioned blockchain workload-control 场景下的 multi-instance route。仍缺 Paxos/FLP/DLS/HotStuff/HoneyBadger/Narwhal 等直接 source。

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
| [[doi-10-1145-357172-357176-byzantine-generals-problem|The Byzantine Generals Problem]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-5555-296806-296824-practical-byzantine-fault-tolerance|Practical Byzantine Fault Tolerance]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-0f53a6508592-raft-understandable-consensus-algorithm|In Search of an Understandable Consensus Algorithm]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain|SRaft: A Scalable CFT Consensus Protocol for Permissioned Blockchain]] | source extension under CFT: distinguishes payload dissemination bottleneck from ordering agreement | 代表 Sources; Source Extensions; relation graph | no | keep linked |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|Asymptotically Optimal Validated Asynchronous Byzantine Agreement]] | source extension under async BFT/VABA: adds externally-valid multi-valued agreement as a consensus decision-object axis | 方法族与解决路线; 代表 Sources; 当前综合; relation graph | no | keep linked under VABA child |
| [[sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain|Stretch-BFT: Workload-Adaptive and Stretchable Consensus Protocol for Permissioned Blockchain]] | source extension under BFT: adds workload-adaptive multi-instance consensus and proposer recovery route | 方法族与解决路线; 代表 Sources; relation graph | no | keep linked |
| [[hal-00944019v2-signature-free-asynchronous-byzantine-consensus|Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages]] | source extension under async BFT: adds signature-free common-coin binary consensus with BV-broadcast | 代表 Sources; 当前综合; relation graph | no | keep linked under async BFT |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | source extension under async BFT/ADKG: adds trusted-dealer-free threshold setup as a consensus setup axis | 方法族与解决路线; 代表 Sources; 当前综合; relation graph | no, child method handles details | keep linked under ADKG child |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | source extension under async BFT/ADD/RBC: adds long-message broadcast/dissemination as a consensus support axis | 方法族与解决路线; 代表 Sources; 当前综合; relation graph | no, child methods handle details | keep linked under ADD/RBC children |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| none | not_applicable | not_applicable | no bridge currently targets this node | review |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-consensus | is_a | nahida-knowledge-distributed-systems | vault/04_Knowledge/distributed-systems/consensus.md; vault/04_Knowledge/distributed-systems.md | medium | active_seed |
| nahida-knowledge-consensus | has_child | nahida-knowledge-asynchronous-bft-consensus | vault/04_Knowledge/distributed-systems/consensus.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md | medium | active_seed |
| nahida-knowledge-consensus | has_child | nahida-knowledge-byzantine-fault-tolerance | vault/04_Knowledge/distributed-systems/consensus.md; vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md | medium | active_seed |
| nahida-knowledge-consensus | has_child | nahida-knowledge-crash-fault-tolerance | vault/04_Knowledge/distributed-systems/consensus.md; vault/04_Knowledge/distributed-systems/consensus/crash-fault-tolerance.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md | vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md | high | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md | vault/03_Sources/papers/doi-10-1145-357172-357176-byzantine-generals-problem.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md | vault/03_Sources/papers/doi-10-5555-296806-296824-practical-byzantine-fault-tolerance.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md | vault/03_Sources/papers/sha256-0f53a6508592-raft-understandable-consensus-algorithm.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-ae33e526eb0f-sraft-scalable-cft-consensus-protocol-for-permissioned-blockchain.md | high | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | medium | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | high | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md | vault/03_Sources/papers/sha256-a6106319a63e-stretch-bft-workload-adaptive-stretchable-consensus-protocol-permissioned-blockchain.md | high | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | high | active_seed |
| nahida-knowledge-consensus | evidenced_by | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 补齐 CFT foundation 和 asynchronous/BFT classic foundations。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |
| Common coin、Bracha RBC、HoneyBadger/ACS 等 asynchronous consensus foundations 仍不完整。 | 新 source 补了一个 signature-free common-coin baseline，但不是完整 async BFT foundation pack | nahida-research-search or future papers | medium | queued |
| Threshold setup/DKG foundation 尚薄。 | ADKG 2019/1015 补入 trusted-dealer-free route，但同步/部分同步 DKG、production setup 和 key refresh source 尚缺。 | nahida-research-search or future papers | medium | queued |
| Reliable broadcast / payload dissemination foundation 尚薄。 | ADD 2021/777 补了 long-message route，但 Bracha RBC、AVID、HoneyBadger direct source 仍需补。 | nahida-update | high | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-sraft-scalable-cft | Added SRaft full paper as CFT source extension under the consensus direction. | 1 source note | codex |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 9 source notes; 2 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-stretch-bft | Added Stretch-BFT as BFT/workload-adaptive source extension under the consensus direction. | 1 source note | codex |
| 2026-06-20 | nahida-paper-intake-20260620-item-0034 | Added signature-free asynchronous Byzantine consensus source under async BFT. | hal:hal-00944019v2 | codex |
| 2026-06-20 | nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement | Added VABA as externally-valid multi-valued consensus decision-object route under async BFT. | doi:10.1145/3293611.3331612 | codex |
| 2026-06-23 | nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft | Added ADKG as trusted-dealer-free threshold setup route under async BFT consensus. | iacr:2019/1015 | codex |
| 2026-06-23 | nahida-knowledge-20260623-asynchronous-data-dissemination | Added ADD/RBC as long-message broadcast and data-dissemination support layer under async BFT consensus. | iacr:2021/777 | codex |
