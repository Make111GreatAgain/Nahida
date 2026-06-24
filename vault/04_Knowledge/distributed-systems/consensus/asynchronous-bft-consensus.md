---
id: "nahida-knowledge-asynchronous-bft-consensus"
title: "Asynchronous BFT consensus"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "asynchronous-bft-consensus"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-byzantine-fault-tolerance"
child_knowledge_refs:
  - "nahida-knowledge-validated-asynchronous-byzantine-agreement"
  - "nahida-knowledge-asynchronous-verifiable-secret-sharing"
  - "nahida-knowledge-asynchronous-distributed-key-generation"
  - "nahida-knowledge-asynchronous-data-dissemination"
  - "nahida-knowledge-asynchronous-reliable-broadcast"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "is_a"
    to: "nahida-knowledge-byzantine-fault-tolerance"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "has_child"
    to: "nahida-knowledge-validated-asynchronous-byzantine-agreement"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "has_child"
    to: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "has_child"
    to: "nahida-knowledge-asynchronous-distributed-key-generation"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "has_child"
    to: "nahida-knowledge-asynchronous-data-dissemination"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "has_child"
    to: "nahida-knowledge-asynchronous-reliable-broadcast"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-bft-consensus"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
source_note_refs:
  - "vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md"
  - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
  - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
  - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
  - "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
  - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
  - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
  - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
  - "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
representative_source_refs:
  - "hal:hal-00944019v2"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "doi:10.1145/3293611.3331612"
  - "doi:10.1145/167088.167105"
  - "iacr:2019/1015"
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "usenix:security23/das"
query_keys:
  - "Asynchronous BFT consensus"
  - "asynchronous-bft-consensus"
  - "async BFT"
  - "ACS-based BFT"
  - "BV-broadcast"
  - "common coin"
  - "signature-free asynchronous Byzantine consensus"
  - "validated asynchronous Byzantine agreement"
  - "VABA"
  - "asynchronous verifiable secret sharing"
  - "AVSS"
  - "global coin from AVSS"
  - "asynchronous distributed key generation"
  - "ADKG"
  - "asynchronous data dissemination"
  - "ADD"
  - "asynchronous reliable broadcast"
  - "RBC"
  - "long-message RBC"
  - "high-threshold AVSS"
  - "eventually perfect common coin"
  - "trusted-dealer-free threshold setup"
  - "dual-threshold AVSS"
  - "publicly verifiable VSS"
  - "ACK transcript VSS"
  - "high-threshold ADKG"
  - "distributed polynomial sampling"
aliases:
  - "async BFT"
  - "ACS-based BFT"
  - "VABA"
  - "AVSS-backed async BA"
  - "ADKG-backed async BFT"
  - "ADD-backed async BFT"
domains:
  - "distributed-systems"
topics:
  - "asynchronous-bft-consensus"
  - "validated-asynchronous-byzantine-agreement"
  - "asynchronous-verifiable-secret-sharing"
  - "asynchronous-distributed-key-generation"
  - "asynchronous-data-dissemination"
  - "asynchronous-reliable-broadcast"
  - "dual-threshold-avss"
  - "high-threshold-adkg"
  - "distributed-polynomial-sampling"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
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
  - "nahida-paper-intake-20260620-item-0034"
  - "nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement"
  - "nahida-knowledge-20260623-canetti-rabin-optimal-async-ba"
  - "nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft"
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
  - "nahida-knowledge-20260623-verifiable-secret-sharing-simplified"
  - "nahida-knowledge-20260623-high-threshold-adkg-polynomial-sampling"
source_refs:
  - "hal:hal-00944019v2"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "doi:10.1145/3293611.3331612"
  - "doi:10.1145/167088.167105"
  - "iacr:2019/1015"
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "usenix:security23/das"
confidence: "medium"
trust_tier: "primary"
---

# Asynchronous BFT consensus

## 定义与范围

- 定义: Asynchronous BFT consensus 研究在不依赖固定 timing assumption 的网络中如何让 Byzantine 容错协议保持 progress。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `asynchronous-bft-consensus`
- Aliases/query keys: async BFT, ACS-based BFT
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `asynchronous-bft-consensus`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source seed 来自 Canetti-Rabin 1993、Mostefaoui-Moumen-Raynal 2014、VABA 2019、ADKG 2019/1015、ADD 2021/777、VSS Simplified 2023/1196、Das et al. 2023 high-threshold ADKG、MyTumbler/SuperMA 与 EPIC；它们分别覆盖 AVSS-backed global coin、common-coin/BV-broadcast binary foundation、externally valid multi-valued agreement、trusted-dealer-free threshold setup、long-message data dissemination/RBC、publicly verifiable / dual-threshold AVSS、practical high-threshold DKG via distributed polynomial sampling、flexible advancement/common-coin bypass 和 adaptive-security ACS。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[byzantine-fault-tolerance|byzantine-fault-tolerance]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

解决 binary agreement 到 externally-valid multi-valued agreement 的提升、fixed-slot asynchronous frameworks 的资源浪费、far-away proposer abort、common-coin critical path 和 adaptive corruption 开销。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[byzantine-fault-tolerance|byzantine-fault-tolerance]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[validated-asynchronous-byzantine-agreement|validated-asynchronous-byzantine-agreement]] | child/problem | VABA 是 externally valid multi-valued async BA，不应埋在单篇论文 source note 中 | [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|VABA 2019]] | active_seed |
| [[asynchronous-verifiable-secret-sharing|asynchronous-verifiable-secret-sharing]] | child/method | AVSS 是 async BA/global coin 的可复用分布式加密原语，不应埋在单篇论文 source note 中 | [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Canetti-Rabin 1993]] | active_seed |
| [[asynchronous-distributed-key-generation|asynchronous-distributed-key-generation]] | child/method | ADKG 是移除 trusted dealer 的 threshold-crypto setup primitive，连接 HA-VSS、common coin、VABA 和 threshold signatures | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] | active_seed |
| [[asynchronous-data-dissemination|asynchronous-data-dissemination]] | child/method | ADD 是长消息传播 primitive，解释 RBC/AVSS/ACSS/ADKG 中大 payload 如何避免 `O(n^2 |M|)` 全量广播 | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] | active_seed |
| [[asynchronous-reliable-broadcast|asynchronous-reliable-broadcast]] | child/method | RBC 是 ACS、AVSS、atomic broadcast 和 blockchain-oriented async BFT 的可靠传播层；已有多篇 source 引用，应从缺口提升为 thin node | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]]; [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC]] | active_seed |
| [[dual-threshold-asynchronous-vss|dual-threshold-asynchronous-vss]] | nested child/method | 双阈值 AVSS 分离 `t` 和 `ell`，是 AVSS/ADKG/common-coin setup 的可复用子问题 | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]]; [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| flexible advancement / pass quorum | flexible advancement / pass quorum | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| SuperMA/FastBA promise path | SuperMA/FastBA promise path | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| ACS with RBC + ABA | ACS with RBC + ABA | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| ADD-backed payload dissemination | 用 Reed-Solomon coded symbols 和 online error correction 让大消息从至少 `t+1` 个 honest holders 传播到所有 honest nodes | asynchronous network, `t<n/3`, long messages | `O(n|M|+n^2)` communication；coding/decoding computation 较重；不是 consensus 决定协议 | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| ADD-backed long-message RBC | 先用 RBC 广播 hash，再用 ADD 传播 payload，使 long-message RBC 成本降到 `O(n|M|+kappa n^2)` | collision-resistant hash, async BFT | Bracha/AVID direct sources 仍需补；RBC 应用和纯 ADD 假设不同 | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| adaptive threshold PRF and DKG setup | adaptive threshold PRF and DKG setup | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| AVSS-backed global coin | 用异步可验证秘密分享先固定可重构随机 secret，再生成所有 honest players 以常数概率一致的 global coin | 完全异步私有信道，dynamic/unbounded Byzantine adversary，`n >= 3t+1` | extended abstract 省略部分完整证明；不等同现代 threshold-coin implementation | [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Canetti-Rabin 1993]] |
| Publicly verifiable / dual-threshold AVSS | 用 ACK transcript、degree-`2t` sharing 和 selective verifiable encryption，使异步分享具备公开可验证、异步终止和 `t`/`ell` 分离能力 | async VSS setup, `n>=3t+1`, PKI/private channels, RBC, polynomial commitments and VE | 仍是 setup/randomness/threshold primitive，不处理 ordering/execution；batching/adaptive security 需后续 source | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] |
| BV-broadcast + common coin binary consensus | 用 value-oriented BV-broadcast 过滤 Byzantine-only values，再用 common coin 让 estimates 以常数概率聚合 | binary asynchronous Byzantine consensus, `n > 3t` | common coin 作为外部抽象，未覆盖实现成本；只处理 binary consensus | [[hal-00944019v2-signature-free-asynchronous-byzantine-consensus|Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages]] |
| Validated multi-valued asynchronous BA | 用 external validity predicate、proposal-promotion 和 threshold-coin leader election 把 async BA 提升为可用于 Atomic Broadcast/SMR 的多值 agreement | authenticated async BFT, adaptive adversary, `f < n/3`, threshold signatures/coin setup | 依赖加密 setup；会议版证明压缩；不处理 transaction dissemination 或 mempool | [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|VABA 2019]] |
| Trusted-dealer-free threshold setup | 用 HA-VSS、wDKG、EPCC 和 ACS-like ADKG 在异步环境中生成 threshold keys/common coin setup | authenticated asynchronous network, PKI, computational adversary, `f < n/3` | initial expected `O(n^4)` words and `O(f)` time；不是生产 key-rotation 方案 | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] |
| Practical high-threshold ADKG setup | 用 low-threshold ACSS、MVBA 和 distributed polynomial sampling 支持 `ell in [t,n-t-1]` 的高阈值 threshold setup | static Byzantine adversary, asynchronous private authenticated channels, PKI, DL hardness | 仍是 setup primitive；不处理 ordering、mempool 或 production key rotation；UC proof 未正式完成 | [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Das et al. 2023 high-threshold ADKG]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Fast Asynchronous Byzantine Agreement with Optimal Resilience]] | paper | 补入 AVSS-backed global coin foundation：A-RS -> AWSS -> AVSS -> Global-Coin -> BA，在 `n>=3t+1` 下实现快速最优 resilience async BA | 完全异步私有信道；dynamic/unbounded adversary；extended abstract，部分证明转 technical report | Definition 2, Theorem 1-2, §5-§9 |
| [[hal-00944019v2-signature-free-asynchronous-byzantine-consensus|Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages]] | paper | 为 async BFT 补入 signature-free common-coin/BV-broadcast foundation：`t<n/3`、每轮 `O(n^2)` messages、期望 4 轮决定 | 抽象掉 common coin 实现，只处理 binary consensus | Abstract, §3-§4 |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|Asymptotically Optimal Validated Asynchronous Byzantine Agreement]] | paper | 补入 externally-valid multi-valued async BA/VABA foundation：`f<n/3`、adaptive adversary、expected `O(1)` time、expected `O(n^2)` word communication | authenticated setting；trusted dealer/random oracle/threshold signatures/threshold coin；不含系统实现 | Definition 4, Theorem 1, §3.1-§3.6 |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | paper | 补入 ADKG setup foundation：HA-VSS -> wDKG -> EPCC -> EEABA/ADKG，移除 common coin、VABA 和 threshold signatures 的 trusted dealer 假设 | PKI/authenticated links/computational adversary；无实现评测；initial setup `O(n^4)` | Theorem 1.1, §3-§6 |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | paper | 补入 ADD/RBC payload dissemination layer：ADD `O(n|M|+n^2)`，long-message RBC `O(n|M|+kappa n^2)`，并影响 AVSS/ACSS/ADKG communication | main ADD is information-theoretic for `t<n/3`; RBC/high-threshold variants use collision-resistant hash; no implementation benchmark | Definition 3.1, Theorem 3.5, §4-§6 |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | paper | 补入 publicly verifiable and dual-threshold AVSS route：ACK transcript, degree-`2t` async sharing, selective VE and WAN evaluation | PKI/private channels/RBC; static adversary; batching/adaptive security remain future work | Definitions 1-3, Algorithms 1-3, Theorems 1-3, §8 |
| [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling]] | paper | 补入 practical high-threshold threshold-crypto setup：distributed polynomial sampling 避开 high-threshold ACSS，64 节点 curve25519 WAN 实验为 12.48s / 3.32MB per node。 | 不是 consensus/ordering protocol；static adversary；stand-alone proof；production key management 未覆盖 | Abstract, Algorithm 1, Theorem 2, Table 3 |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前可作为 async BFT seed；Canetti-Rabin 1993 补上了 AVSS -> global coin -> optimal-resilience async BA 的早期 foundation，Mostefaoui-Moumen-Raynal 2014 补上了 signature-free common-coin binary consensus baseline，VABA 2019 补上了 externally valid multi-valued agreement foundation，ADKG 2019/1015 把 trusted-dealer threshold setup 下降为可协议化的异步 DKG 层，ADD 2021/777 又补上 long-message dissemination/RBC 这一 payload movement 层。VSS Simplified 2023/1196 进一步让 AVSS 层具备公开可验证 transcript、异步终止和双阈值 secrecy/reconstruction 分离。Das et al. 2023 则表明 high-threshold ADKG 可以通过 distributed polynomial sampling 获得 practical prototype evidence，使 `2t+1` threshold signatures/common-coin setup 的工程成本显著下降。整体上，async BFT 从 binary BA 到 Atomic Broadcast/SMR primitive 需要随机性层、broadcast/secret-sharing primitives、long-message data dissemination、external validity、quality property、proposal promotion、threshold-coin leader election 和 threshold-crypto setup 等多个可拆层。仍缺 HoneyBadger/BEAT/Bracha RBC/common coin lineage、production DKG/key refresh、AVID/Merkle RBC、adaptive/batched VSS 等更完整 foundation。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse; VSS Simplified adds a Rust/WAN evaluation source but not production deployment evidence.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Fast Asynchronous Byzantine Agreement with Optimal Resilience]] | 新建 AVSS child/method 节点；补入 AVSS-backed global coin route 和 optimal-resilience async BA foundation | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; bridge | yes, created child | 后续补 Canetti-Rabin technical report、Bracha A-cast/RBC、modern AVSS/common-coin sources |
| [[hal-00944019v2-signature-free-asynchronous-byzantine-consensus|Signature-Free Asynchronous Byzantine Consensus with t < n/3 and O(n^2) Messages]] | 增加 common-coin/BV-broadcast foundation source；纠正队列的 blockchain-primary path | 背景; 方法族; 代表 Sources; 当前综合; 缺口与队列 | no | 后续补 common coin/Bracha/HoneyBadger sources |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|Asymptotically Optimal Validated Asynchronous Byzantine Agreement]] | 新增 VABA 子问题和 source extension；补入 externally valid multi-valued async BA 的 optimal `O(n^2)` route | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; bridge | yes, created child | 后续补 Cachin 2001、atomic broadcast、HoneyBadger/BEAT sources |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | 新增 ADKG method 节点；补入 trusted-dealer-free threshold setup 路线 | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; bridge | yes, created child | 后续补 DKG lineage、modern common coin、production key refresh sources |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | 新增 ADD 和 RBC child/method 节点；补入 long-message dissemination and ADD-backed RBC route | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; bridge | yes, created children | 后续补 Bracha RBC、AVID/HoneyBadger 和 modern data dissemination sources |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | 新增 dual-threshold AVSS nested method node；补入 publicly verifiable/terminating AVSS route | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; bridge | yes, child under AVSS | 后续补 PVSS、batching/adaptive VSS 和 production threshold setup sources |
| [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling]] | 补入 practical high-threshold ADKG setup route；保持为 ADKG 子节点的代表来源，不提升为共识协议。 | 背景; 方法族; 代表 Sources; 当前综合 | no, parent index only | 后续判断 distributed polynomial sampling 是否拆节点 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | `distributed-systems/consensus/byzantine-fault-tolerance; distributed-systems/consensus/asynchronous-bft-consensus` | application, translation, dependency | The BFT fault threshold, quorum-intersection intuition, reliable broadcast, AVSS/global-coin and dual-threshold setup ideas transfer; fixed-slot overhead, pass/skip advancement, timestamp efficiency, adaptive corruption, production key rotation, transaction selection, execution and WAN workload behavior remain asynchronous blockchain-system-specific. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-asynchronous-bft-consensus | is_a | nahida-knowledge-byzantine-fault-tolerance | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md; vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md | medium | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md | vault/03_Sources/papers/hal-00944019v2-signature-free-asynchronous-byzantine-consensus.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | medium | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | medium | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | has_child | nahida-knowledge-validated-asynchronous-byzantine-agreement | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | has_child | nahida-knowledge-asynchronous-verifiable-secret-sharing | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | has_child | nahida-knowledge-asynchronous-distributed-key-generation | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | has_child | nahida-knowledge-asynchronous-data-dissemination | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | has_child | nahida-knowledge-asynchronous-reliable-broadcast | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md | vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | high | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | evidenced_by | vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md | vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md | medium | active_seed |
| nahida-knowledge-asynchronous-bft-consensus | bridges_to | nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus | vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Bracha RBC、AVID、Rabin/common-coin lineage、HoneyBadgerBFT、BEAT direct source 缺失或仍薄。 | ADD 2021/777 补了 long-message RBC route，但 classic RBC/ACS lineage 仍需直接 source | nahida-research-search or nahida-update | high | queued |
| Common coin implementation 与 AVSS/BV-broadcast/RBC 关系仍需拆解。 | Canetti-Rabin 给出 AVSS-backed global coin；Mostefaoui 使用 common coin 抽象；还需要更多 sources 决定是否拆独立 common-coin 节点 | nahida-research-search or future papers | medium | queued |
| ADD/RBC 与 shared mempool、data availability sampling 的边界需要后续校准。 | 它们都处理 payload availability，但安全目标和系统层级不同 | nahida-update | medium | queued |
| Cachin et al. 2001 VABA source 尚缺。 | VABA 2019 的 `O(n^3)` baseline 和 open problem 目前只由该 source 转述 | nahida-research-search or nahida-update | high | queued |
| Production DKG/key-refresh/reconfiguration sources 尚缺。 | ADKG 2019/1015 移除 trusted dealer，但没有覆盖长期运行系统的 key rotation、membership change 和 implementation engineering | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 2 source notes; 4 legacy notes | codex |
| 2026-06-20 | nahida-paper-intake-20260620-item-0034 | Added signature-free common-coin/BV-broadcast asynchronous BFT foundation source. | hal:hal-00944019v2 | codex |
| 2026-06-20 | nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement | Added VABA child node and source extension for externally-valid multi-valued async BA. | doi:10.1145/3293611.3331612 | codex |
| 2026-06-23 | nahida-knowledge-20260623-canetti-rabin-optimal-async-ba | Added Canetti-Rabin AVSS-backed global coin route and created AVSS child/method node. | doi:10.1145/167088.167105 | codex |
| 2026-06-23 | nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft | Added ADKG child/method node and trusted-dealer-free threshold setup route. | iacr:2019/1015 | codex |
| 2026-06-23 | nahida-knowledge-20260623-asynchronous-data-dissemination | Added ADD and asynchronous reliable broadcast child nodes as the long-message dissemination layer under async BFT. | iacr:2021/777 | codex |
| 2026-06-23 | nahida-knowledge-20260623-high-threshold-adkg-polynomial-sampling | Added practical high-threshold ADKG as threshold-setup evidence under async BFT without reclassifying it as consensus. | usenix:security23/das | codex |
