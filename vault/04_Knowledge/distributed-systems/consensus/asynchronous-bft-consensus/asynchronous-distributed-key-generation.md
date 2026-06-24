---
id: "nahida-knowledge-asynchronous-distributed-key-generation"
title: "Asynchronous distributed key generation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "method"
hierarchy_level: "method"
file_slug: "asynchronous-distributed-key-generation"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-asynchronous-bft-consensus"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-distributed-key-generation"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation"
secondary_ontology_paths:
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing"
  - "distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement"
relation_edges:
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "is_a_method_for"
    to: "nahida-knowledge-asynchronous-bft-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "depends_on"
    to: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md"
      - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "supports"
    to: "nahida-knowledge-validated-asynchronous-byzantine-agreement"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement.md"
      - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "supported_by"
    to: "nahida-knowledge-asynchronous-reliable-broadcast"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md"
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "supported_by"
    to: "nahida-knowledge-dual-threshold-asynchronous-vss"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss.md"
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-distributed-key-generation"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md"
      - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
  - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
  - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
  - "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
representative_source_refs:
  - "iacr:2019/1015"
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "usenix:security23/das"
query_keys:
  - "Asynchronous distributed key generation"
  - "asynchronous-distributed-key-generation"
  - "ADKG"
  - "trusted-dealer-free threshold setup"
  - "high-threshold AVSS"
  - "HA-VSS"
  - "weak DKG"
  - "wDKG"
  - "eventually perfect common coin"
  - "EPCC"
  - "threshold signatures without trusted dealer"
  - "trusted-dealer-free VABA"
  - "ADKG communication complexity"
  - "long-message RBC for ADKG"
  - "ADD-backed reliable broadcast"
  - "dual-threshold AVSS for ADKG"
  - "publicly verifiable VSS setup"
  - "high-threshold ADKG"
  - "distributed polynomial sampling"
  - "practical asynchronous high-threshold DKG"
  - "low-threshold ACSS high-threshold ADKG"
aliases:
  - "ADKG"
  - "asynchronous DKG"
  - "trusted-dealer-free threshold setup"
  - "High-threshold ADKG"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "asynchronous-bft-consensus"
  - "distributed-key-generation"
  - "threshold-cryptographic-setup"
  - "asynchronous-verifiable-secret-sharing"
  - "asynchronous-reliable-broadcast"
  - "dual-threshold-avss"
  - "high-threshold-adkg"
  - "distributed-polynomial-sampling"
tags:
  - "nahida/knowledge"
  - "nahida/method"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft"
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
  - "nahida-knowledge-20260623-verifiable-secret-sharing-simplified"
  - "nahida-knowledge-20260623-high-threshold-adkg-polynomial-sampling"
source_refs:
  - "iacr:2019/1015"
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "usenix:security23/das"
  - "sha256:0cded3a5e3529e9d1e544d84587031cab1588b79f8f5d45d319dbe68c4ef4c8a"
confidence: "high"
trust_tier: "primary"
---

# Asynchronous distributed key generation

## 定义与范围

- 定义: Asynchronous distributed key generation (ADKG) 是在完全异步、Byzantine 容错网络中，由参与方共同生成 threshold cryptography 所需 key shares 和公共承诺，而不依赖 trusted dealer 的 setup 方法族。
- 不包含: 单篇 ADKG 论文全文、某个具体 threshold-signature library、同步/部分同步 DKG 的工程部署、区块链 validator governance；这些留在 source notes 或更具体的实现/协议节点。
- Canonical terms: `asynchronous-distributed-key-generation`, `ADKG`
- Aliases/query keys: asynchronous DKG, trusted-dealer-free threshold setup, HA-VSS, wDKG, EPCC
- Standalone completeness check: 本节点给出本地定义、问题、方法路线、代表 source、迁移边界和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询异步 DKG、trusted dealer removal、VABA/common coin setup 或 threshold signatures without dealer 时先到本节点。
- Update scope: 新 source 若改变 fault threshold、threshold level、termination model、coin construction、threshold signature setup 或 ADKG/AVSS/VABA 关系，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

许多高效 asynchronous BFT、VABA、SMR 和 threshold-signature 协议默认有一个 trusted dealer 预先生成 threshold keys 或 common coin。这个假设在论文中方便，但在开放或长期运行系统中会变成安全和部署瓶颈。

ADKG 解决的是 setup 层问题: 在没有同步 timing assumption 的情况下，honest parties 仍能对一组可用 key shares 达成足够一致的视图，并把它用于 common coin、VABA 或 threshold signatures。

ADD 2021/777 不改变 ADKG 的 setup 逻辑，但改进了 ADKG 常用的 long-message reliable broadcast 子层。若 ADKG 需要 `O(n)` 个 RBC instances 广播 `O(kappa n)` 大小的消息，ADD-backed RBC 可把这部分通信从 `O(kappa n^3 log n)` 降到 `O(kappa n^3)`。

VSS Simplified 2023/1196 同样不替代 ADKG 协议本体，但它补强了 ADKG 可复用的 VSS 子层: publicly verifiable transcript 让分享结果可被外部验证，dual-threshold AVSS 让 setup 可以分离容错阈值 `t` 与 secrecy/reconstruction 阈值 `ell`。

Das-Xiang-Kokoris-Kogias-Ren 2023/USENIX Security 则把高阈值 ADKG 推向实际可运行路径: 不再用昂贵的 high-threshold ACSS 直接分享高阶多项式，而是用 low-threshold ACSS 分享随机输入、用 MVBA 选定 `n-t` 个完成实例，再用 hyperinvertible matrix 提取 `ell+1` 个随机系数，得到随机 degree-`ell` polynomial。这个 source 说明 ADKG 的高阈值瓶颈可以转化为 distributed polynomial sampling，而不是必须依赖高阈值分享子层。

## 基础概念判断

- 是否是基础概念/方向/问题: `method` / `method`。
- 为什么足够通用: ADKG 是一类可复用 setup primitive，连接 AVSS、common coin、threshold signatures、VABA 和 asynchronous BFT；它不等同于 `2019/1015` 这篇 source。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 该 source 当前是代表证据；未来同步 DKG、Hybrid-DKG、BLS threshold setup、proactive refresh 或 production DKG source 可继续扩展本节点。
- 需要引用的更基础 Knowledge: [[asynchronous-bft-consensus|asynchronous-bft-consensus]], [[asynchronous-verifiable-secret-sharing|asynchronous-verifiable-secret-sharing]]。
- 不应拆出的实例/协议/来源: HA-VSS、wDKG、EPCC 当前作为方法路线；如果后续多个 sources 独立复用，再拆子节点。

## 解决的问题

ADKG 解决的是: 在 `f<n/3` Byzantine、异步网络和 adaptive adversary 下，如何让参与方不依赖 trusted dealer，也能得到 threshold signatures/common coin/VABA 所需的 key shares 和公共承诺。

它尤其处理两个异步难点:

- 不能等待所有 parties，因此 key-share set 必须能在不同 honest parties 间最终收敛。
- 如果 reconstruction threshold 需要 `2f+1`，传统 AVSS 在 `n=3f+1` 下的等待集合交集不足，需要 high-threshold AVSS。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | method_for | ADKG removes trusted-dealer setup behind common coins, threshold signatures and VABA. | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| high-threshold AVSS | method candidate | `2f+1` reconstruction threshold in `n=3f+1` async systems is a reusable subproblem. | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] | hold |
| [[dual-threshold-asynchronous-vss|dual-threshold asynchronous VSS]] | dependency method | publicly verifiable and dual-threshold sharing can support threshold setup, randomness beacons and later DKG variants | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] | active_seed |
| eventually perfect common coin | method candidate | Common coin setup spans ABA, VABA and ACS-style protocols. | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] | queued |
| reliable broadcast for ADKG payloads | dependency candidate | ADKG/VSS setup protocols often broadcast commitment/share vectors; long-message RBC affects total setup cost. | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] | active_seed |
| distributed polynomial sampling | method candidate | high-threshold ADKG、random double sharing 和 proactive refresh 都可被看成随机高阶多项式采样问题。 | [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Das et al. 2023 high-threshold ADKG]] | hold |
| production threshold-key refresh | engineering candidate | Long-lived systems need rotation/reconfiguration beyond one initial setup. | no direct source yet | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| High-threshold AVSS | 用 asymmetric bivariate polynomial 把 recovery threshold 与 reconstruction threshold 分离，支持 `k <= n-f`。 | asynchronous authenticated network, `f<n/3`, computational security | 协议复杂；当前 evidence 主要来自一篇 source | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] |
| Weak DKG predictions | 运行多个 HA-VSS，并输出单调增长的 prediction set，使 honest parties 最终拥有相同末态视图。 | 不能强行要求 deterministic async termination | 可能输出最多 `f+1` 个 predictions；需要上层处理早期不一致 | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] |
| Eventually perfect common coin | 用 wDKG prediction 生成 coin；前 `f` 个序号可能不一致，之后行为接近 perfect coin。 | sequential coin invocations, threshold shares available | 早期 bad coin prefix 需要 ABA/VABA 容忍 | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] |
| ACS-style ADKG | 在 HA-VSS shares 上运行 ABA/ACS-like decision，得到所有 honest parties 同意的 key-share set。 | threshold crypto setup for async BFT/VABA/signatures | 初始 expected `O(n^4)` words and `O(f)` time | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] |
| Long-message RBC optimization | 用 ADD-backed RBC 降低 ADKG 中大消息 RBC instances 的通信成本。 | ADKG protocols using `O(n)` RBC instances of `O(kappa n)` messages | 这是通信子层优化，不是新的 DKG agreement/set-selection protocol | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| Publicly verifiable / dual-threshold VSS setup | 用 ACK transcript、degree-`2t` sharing 和 selective VE 提供公开可验且可分离 `t`/`ell` 的分享子层。 | ADKG/randomness/threshold setup protocols that need AVSS/PVSS-style sharing | 这是 VSS 子层，不给出 DKG set agreement、key aggregation 或 production key rotation | [[dual-threshold-asynchronous-vss|Dual-threshold asynchronous VSS]]; [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] |
| Distributed polynomial sampling for high-threshold ADKG | 用 low-threshold ACSS + MVBA + hyperinvertible-matrix extraction 生成随机 degree-`ell` polynomial，并让每个节点只获得一个 evaluation point。 | static Byzantine adversary, asynchronous authenticated private channels, `n>=3t+1`, `ell in [t,n-t-1]`, DL hardness | 目前由一个 direct source 支撑；UC proof 和 production key rotation 仍是后续缺口 | [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Das et al. 2023 high-threshold ADKG]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | paper | 首个 asynchronous DKG source seed；补入 HA-VSS、wDKG、EPCC、EEABA 和 ADKG，并把 trusted-dealer-free setup 连接到 VABA 和 threshold signatures。 | PKI/authenticated links/computational adversary；无实现评测；initial setup `O(n^4)`；ePrint identity from local filename/PDF. | Theorem 1.1, §3-§6 |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | paper | 给出 long-message RBC 子层优化，使 ADKG-style protocols 的 RBC cost 从 `O(kappa n^3 log n)` 降到 `O(kappa n^3)` | 不替代 ADKG 协议本体；只是 inherited communication improvement | §4.2 |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | paper | 给出 publicly verifiable and dual-threshold AVSS 子层，可作为 future ADKG/randomness/threshold setup 的分享基础 | 不替代 ADKG 协议本体；只补强 VSS/PVSS primitive | Definitions 1-3, Algorithms 2-3, §8 |
| [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling]] | paper | 给出 practical high-threshold ADKG 路线：用 distributed polynomial sampling 避开 high-threshold ACSS，支持 `ell in [t,n-t-1]`，并提供 128 节点 WAN prototype/evaluation。 | static adversary; PKI/private authenticated channels; stand-alone proof; distributed polynomial sampling 尚未拆成独立 node | Abstract, Figure 1, Algorithm 1, Theorem 2, Table 3 |

## 正反例约束

- 正确: 把 ADKG 作为 async BFT threshold setup primitive。
- 正确: 把 HA-VSS 作为 AVSS 的 high-threshold route，把 VABA 作为被 setup 支持的上层问题。
- 错误: 把 ADKG 直接写成区块链共识协议。
- 错误: 把 trusted-dealer-free 等同于无需任何 PKI、认证信道或密码假设。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: ADKG 是 async BFT 栈中的 setup 层: HA-VSS 提供高阈值可验证分享，wDKG 让 key-set view 在异步系统中最终收敛，EPCC 将这个收敛过程转为 eventually perfect common coin，EEABA/ADKG 再把它用于无 trusted dealer 的 threshold signatures、VABA 和随机化异步共识。它把原本“论文假设已有 trusted dealer”的边界推回到可协议化的 distributed setup；ADD 2021/777 进一步说明，若 ADKG 依赖大量 long-message RBC，可靠广播子层可以从 Merkle/AVID-style `log n` 因子中受益并降到 `O(kappa n^3)`；VSS Simplified 2023/1196 则补强了可复用 VSS 子层，使公开可验 transcript 和双阈值 secrecy/reconstruction 成为后续 ADKG/threshold setup 可以引用的基础。Das et al. 2023 进一步把 practical high-threshold ADKG 的瓶颈从 high-threshold ACSS 转为 distributed polynomial sampling：low-threshold ACSS 提供随机输入，MVBA 选定 `n-t` 完成实例，hyperinvertible matrix 提取 `ell+1` 随机系数，最终在 64 节点 curve25519 WAN 实验中把 prior high-threshold ADKG 从 152.56s/18.97MB per node 降到 12.48s/3.32MB per node。以上都不消除 ADKG 本体的复杂 setup 假设、PKI、membership、UC proof 和 production key rotation 问题。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: VSS Simplified includes a Rust/WAN evaluation of VSS primitives, but no production ADKG deployment evidence.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new DKG, AVSS, common coin, threshold signatures, VABA or production key-management source.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | 新建 ADKG method 节点；补入 trusted-dealer-free threshold setup 路线。 | 定义; 背景; 方法族; 代表 Sources; bridge | yes, child/method under async BFT | 后续补 DKG lineage、modern threshold-signature setup、production key refresh sources |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | 补入 ADD-backed RBC 对 ADKG communication complexity 的 inherited improvement。 | 背景; 下级结构; 方法族; 代表 Sources; 当前综合 | no, ADKG node remains setup layer | 后续补 ADKG variants 和 AVID/HoneyBadger source 校准成本 |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | 补入 publicly verifiable / dual-threshold VSS as ADKG setup dependency. | 背景; 下级结构; 方法族; 代表 Sources; 当前综合 | no, ADKG node remains setup layer | 后续补 DKG variants using PVSS/dual-threshold VSS |
| [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling]] | 补入 practical high-threshold ADKG route：用 distributed polynomial sampling 避免 high-threshold ACSS，并加入实现/评测证据。 | 背景; 方法族; 代表 Sources; 当前综合; query keys | no, keep distributed polynomial sampling as method route until more sources | 后续判断 distributed polynomial sampling 是否拆成 child method node |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | `distributed-systems/consensus/asynchronous-bft-consensus` | dependency, setup_transfer | ADKG transfers as a threshold-crypto setup primitive for common coins/signatures; it does not transfer transaction dissemination, validator governance, economic incentives or production key-rotation policy. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-asynchronous-distributed-key-generation | is_a_method_for | nahida-knowledge-asynchronous-bft-consensus | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md | high | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | depends_on | nahida-knowledge-asynchronous-verifiable-secret-sharing | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md; vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | high | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | supports | nahida-knowledge-validated-asynchronous-byzantine-agreement | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement.md; vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | high | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | evidenced_by | vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | high | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | supported_by | nahida-knowledge-asynchronous-reliable-broadcast | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md; vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | medium | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | evidenced_by | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | medium | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | supported_by | nahida-knowledge-dual-threshold-asynchronous-vss | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss.md; vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | medium | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | evidenced_by | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | medium | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | evidenced_by | vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md | vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md | high | active_seed |
| nahida-knowledge-asynchronous-distributed-key-generation | bridges_to | nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus | vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md; vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| DKG lineage direct sources 尚缺。 | 需要区分 synchronous/partially synchronous/asynchronous DKG，以及 trusted-dealer-free setup 的历史边界。 | nahida-research-search or nahida-update | medium | queued |
| Common coin 节点尚未独立。 | Canetti-Rabin、MMR、VABA、ADKG 都触及 common coin，但当前还缺足够综合 source 来拆出完整节点。 | nahida-consolidate after more sources | high | queued |
| ADKG 的 reliable-broadcast 子层仍缺 AVID/HoneyBadger direct source。 | ADD 2021/777 给出优化结论，但比较对象和系统用法需要更多 direct source。 | nahida-update | medium | queued |
| Production key rotation/reconfiguration source 尚缺。 | 长期运行 blockchain/BFT 系统需要 key refresh、membership change 和 operational setup。 | nahida-research-search | medium | queued |
| Distributed polynomial sampling 是否应拆独立节点。 | Das et al. 2023 显示它可用于 high-threshold ADKG、random double sharing 和 proactive secret sharing，但当前 direct source 仍少。 | nahida-consolidate after more sources | medium | hold |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft | Created ADKG method node and linked it to async BFT, AVSS, VABA and the distributed-BFT bridge. | iacr:2019/1015 | codex |
| 2026-06-23 | nahida-knowledge-20260623-asynchronous-data-dissemination | Added ADD-backed long-message RBC as an ADKG communication sublayer improvement. | iacr:2021/777 | codex |
| 2026-06-23 | nahida-knowledge-20260623-verifiable-secret-sharing-simplified | Added publicly verifiable / dual-threshold AVSS as an ADKG setup dependency, without changing the ADKG protocol layer. | iacr:2023/1196 | codex |
| 2026-06-23 | nahida-knowledge-20260623-high-threshold-adkg-polynomial-sampling | Added practical high-threshold ADKG via distributed polynomial sampling and implementation/evaluation evidence. | usenix:security23/das | codex |
