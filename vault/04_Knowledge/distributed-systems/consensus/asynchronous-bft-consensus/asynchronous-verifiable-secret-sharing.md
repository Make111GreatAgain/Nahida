---
id: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
title: "Asynchronous verifiable secret sharing"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "concept"
hierarchy_level: "method"
file_slug: "asynchronous-verifiable-secret-sharing"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-asynchronous-bft-consensus"
child_knowledge_refs:
  - "nahida-knowledge-dual-threshold-asynchronous-vss"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-verifiable-secret-sharing"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/asynchronous-verifiable-secret-sharing"
relation_edges:
  - from: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    relation: "is_a_method_for"
    to: "nahida-knowledge-asynchronous-bft-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    relation: "depends_on"
    to: "nahida-knowledge-byzantine-fault-tolerance"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md"
      - "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    relation: "has_child"
    to: "nahida-knowledge-dual-threshold-asynchronous-vss"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss.md"
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
    confidence: "medium"
    status: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md"
  - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
  - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
  - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
  - "vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md"
representative_source_refs:
  - "doi:10.1145/167088.167105"
  - "iacr:2019/1015"
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "usenix:security23/das"
query_keys:
  - "Asynchronous verifiable secret sharing"
  - "asynchronous-verifiable-secret-sharing"
  - "AVSS"
  - "asynchronous VSS"
  - "global coin from AVSS"
  - "asynchronous recoverable sharing"
  - "asynchronous weak secret sharing"
  - "high-threshold AVSS"
  - "HA-VSS"
  - "asymmetric bivariate polynomial AVSS"
  - "AVSS reconstruction threshold"
  - "asynchronous complete secret sharing"
  - "ACSS"
  - "dual-threshold ACSS"
  - "dual-threshold AVSS"
  - "publicly verifiable VSS"
  - "ACK transcript VSS"
  - "degree 2t AVSS"
  - "selective verifiable encryption"
  - "AVSS communication complexity"
  - "ADD-backed AVSS"
  - "low-threshold ACSS"
  - "ACSS for high-threshold ADKG"
  - "distributed polynomial sampling"
aliases:
  - "AVSS"
  - "asynchronous VSS"
  - "HA-VSS"
domains:
  - "distributed-systems"
topics:
  - "asynchronous-bft-consensus"
  - "byzantine-fault-tolerance"
  - "secret-sharing"
  - "high-threshold-avss"
  - "asynchronous-complete-secret-sharing"
  - "dual-threshold-acss"
  - "publicly-verifiable-secret-sharing"
  - "dual-threshold-avss"
  - "low-threshold-acss"
  - "distributed-polynomial-sampling"
tags:
  - "nahida/knowledge"
  - "nahida/concept"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-canetti-rabin-optimal-async-ba"
  - "nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft"
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
  - "nahida-knowledge-20260623-verifiable-secret-sharing-simplified"
  - "nahida-knowledge-20260623-high-threshold-adkg-polynomial-sampling"
source_refs:
  - "doi:10.1145/167088.167105"
  - "iacr:2019/1015"
  - "iacr:2021/777"
  - "iacr:2023/1196"
  - "usenix:security23/das"
confidence: "high"
trust_tier: "primary"
---

# Asynchronous verifiable secret sharing

## 定义与范围

- 定义: Asynchronous verifiable secret sharing (AVSS) 是异步 Byzantine 环境中的 secret-sharing primitive；它要求一旦某个 honest player 完成 sharing phase，就存在一个唯一 secret，使得所有 honest players 在 reconstruction phase 中最终重构同一 secret，同时在 honest dealer 且 reconstruction 未开始前保持 secrecy。
- 不包含: 单篇 Canetti-Rabin 论文、Shamir secret sharing 的同步版、某个 global coin 协议实例或完整 Byzantine agreement 协议；这些分别留在 source note 或上层 async BFT 节点。
- Canonical terms: `asynchronous-verifiable-secret-sharing`, `AVSS`
- Aliases/query keys: asynchronous VSS, A-RS, AWSS, global coin from AVSS
- Standalone completeness check: 本节点给出本地定义、问题动机、方法路线、代表 source、边界和后续缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 AVSS、异步 VSS、AVSS-backed global coin、异步 BA 的随机性层时先到本节点，再打开 source note。
- Update scope: 新 source 若改变 AVSS 定义、fault threshold、secrecy model、private-channel assumption、global coin route 或与 async MPC 的关系，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

在异步 BFT 中，participants 不能等待所有消息；一个 honest player 在 sharing phase 和 reconstruction phase 各自最多等待 `n-t` 个响应。两个等待集合的交集在 `n=3t+1` 时可能只有 `t+1` 个，其中 honest share 可能太少，直接用同步 VSS 或简单 Shamir sharing 不能保证所有 honest players 后续重构同一个 secret。AVSS 解决的就是这个“异步等待集合不稳定 + Byzantine dealer/players”问题。

Canetti-Rabin 1993 把 AVSS 放在 async Byzantine agreement 的随机性层: AVSS 先保证 secret 被唯一、可验证地固定，global coin 再用这些 secrets 形成共同随机 bit，BA protocol 才能在 FLP 不可能性下以常数概率推进。ADKG 2019/1015 把 AVSS 扩展到 high-threshold setup；ADD 2021/777 则把长消息 RBC 和编码传播引入 AVSS/ACSS，使通信复杂度从 `O(kappa n^2 log n)` 路线降到 `O(kappa n^2)`。

VSS Simplified 2023/1196 进一步补齐了公开可验证和异步终止之间的缺口: 它用 signed ACK transcript 取代 complaint-response，普通异步版本用 degree-`2t` sharing 保护 secrecy，双阈值版本再用 selective verifiable encryption 分离 `t` 与 `ell`。这使 [[dual-threshold-asynchronous-vss|dual-threshold asynchronous VSS]] 从候选概念提升为可复用方法节点。

Das et al. 2023/USENIX Security 不是新的 AVSS 定义，而是展示 low-threshold ACSS 如何作为 high-threshold ADKG 的高效底层：各节点用 low-threshold ACSS 分享随机输入，之后用 MVBA 和 hyperinvertible-matrix extraction 在 ADKG 层生成高阶随机多项式。这一证据补充了 AVSS/ACSS 的“作为 threshold setup substrate”角色，也说明 high-threshold setup 不一定要直接依赖 high-threshold ACSS。

## 基础概念判断

- 是否是基础概念/方向/问题: `concept` / `method`。
- 为什么足够通用: AVSS 是可跨 source 复用的分布式加密原语，连接 secret sharing、common/global coin、randomized asynchronous BA 和 secure computation；它不是某篇论文的标题或某个实现模块。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Canetti-Rabin 1993 是当前代表 source；AVSS 本身定义为一类 primitive，后续 VSS/AVSS/common-coin/MPC sources 可继续扩展。
- 需要引用的更基础 Knowledge: [[asynchronous-bft-consensus|asynchronous-bft-consensus]], [[byzantine-fault-tolerance|byzantine-fault-tolerance]]。
- 不应拆出的实例/协议/来源: A-RS、AWSS、ICP、A-cast 暂作为方法路线和 source detail；等多个 sources 共同使用时再拆独立节点。

## 解决的问题

AVSS 解决的是: 在完全异步网络和 Byzantine faults 下，如何让 dealer 分享的 secret 在 sharing phase 完成后被唯一固定，并让后续 honest players 在 reconstruction 中恢复同一个值，而 adversary 不能利用不同等待集合、faulty dealer 或调度差异制造多个 secret。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | method_for | AVSS-backed global coin is used to build fast optimal-resilience async BA | active_seed |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | depends_on | Byzantine dealer/players and `n >= 3t+1` threshold define the problem boundary | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| global/common coin for asynchronous consensus | method candidate | AVSS is one construction route; other sources use threshold coin or abstract common coin | Canetti-Rabin 1993; MMR 2014; VABA 2019 | queued |
| asynchronous broadcast / A-cast | primitive candidate | A-cast/RBC is reusable across async BFT, AVSS and atomic broadcast | Canetti-Rabin 1993 references Bracha | queued |
| information checking protocol | primitive candidate | ICP gives unbounded-adversary authentication-like checks without digital signatures | Canetti-Rabin 1993 §4.1 | hold |
| asynchronous complete secret sharing | method candidate | ACSS strengthens AVSS completeness: if one honest node terminates sharing, all honest nodes eventually receive shares | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] | hold |
| [[dual-threshold-asynchronous-vss|Dual-threshold asynchronous VSS]] | child/method | separates sharing fault threshold from secrecy/reconstruction threshold and recurs in AVSS/ACSS and threshold-crypto setup contexts | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]]; [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| A-RS -> AWSS -> AVSS layering | 先保证 recoverable sharing，再保证 fixed value or null，最后保证 unique reconstructable secret | private channels, asynchronous network, `n >= 3t+1`, Byzantine adversary | Extended abstract 省略 AWSS/AVSS 完整证明；依赖 ICP 与 A-cast | [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Canetti-Rabin 1993]] |
| AVSS-backed global coin | 用多个 AVSS-shared random secrets 形成共同随机 bit，使 honest players 以常数概率得到相同 coin | randomized async BA, common/global coin route | 具体证明转 technical report；不等同现代 threshold-coin implementation | [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Canetti-Rabin 1993]] |
| High-threshold AVSS | 用 asymmetric bivariate polynomial 分离 recovery threshold 与 reconstruction threshold，使 AVSS 支持 `f+1 < k <= n-f`，特别是 `2f+1` threshold。 | authenticated async network, `f<n/3`, computational security | 当前 source 没有实现评测；作为 ADKG setup 的子路线，不等同完整 AVSS taxonomy | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] |
| ADD-backed AVSS | 用 improved RBC 广播承诺和 share material，并用 ADD/RBC 处理长消息传播 | asynchronous BFT, no trusted setup, `t<n/3` | 通信 `O(kappa n^2)`；编码/密码细节留在 source note | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| ACSS via encrypted-share recovery | 在 AVSS 上加入 completeness：若任一 honest node 完成 sharing，其他 honest nodes 最终也能获得一致 shares | asynchronous complete secret sharing, PKI/encryption context | 不是普通 AVSS；需要加密 share 传递和 recovery path | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| Dual-threshold ACSS via PVSS | 用 PVSS 和 NIZK proofs 支持 reconstruction secrecy threshold `l`，并让 encrypted shares publicly verifiable | `l < n-t`, DDH/random-oracle style assumptions in source route | 支持 group-secret/random-secret setting；arbitrary secret 需额外 one-time-pad transform | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| ACK-transcript publicly verifiable VSS | 用 recipient signatures 替代 complaint-response；transcript 中每个节点要么有 ACK，要么有公开可验 share opening | synchronous `n>=2t+1` or asynchronous `n>=3t+1`, PKI/private channels, broadcast/RBC | 需要 dealer-recipient interaction；public verifiability 依赖签名和 transcript validation | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] |
| Degree-`2t` terminating AVSS | 异步版本使用 degree-`2t` polynomial，避免公开缺失 shares 后泄露 degree-`t` secret；RBC totality 提供异步终止 | asynchronous `n>=3t+1`, polynomial commitments, signatures, RBC | reconstruction cost roughly doubles; low-threshold version itself不是 dual-threshold | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] |
| Dual-threshold AVSS via selective VE | 只公开 `2t-ell` 个缺失 shares，剩余 `ell-t` 个用 verifiable encryption 发给对应 recipient | `ell in [t,n-t)`, VE for committed shares, PKI/RBC | 比 low-threshold AVSS 更复杂；VE/batching/adaptive security 仍是后续校准点 | [[dual-threshold-asynchronous-vss|Dual-threshold asynchronous VSS]]; [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] |
| Low-threshold ACSS as high-threshold setup substrate | 不直接用 high-threshold ACSS 分享高阶多项式，而是用 low-threshold ACSS 分享随机输入，再由上层 extraction 生成 high-threshold polynomial。 | high-threshold ADKG, static adversary, `n>=3t+1`, PKI/private channels | 这是 ADKG 层方法，不是 AVSS 定义本身；distributed polynomial sampling 是否拆节点仍待更多 source | [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Das et al. 2023 high-threshold ADKG]] |
| Verifiable secret sharing for async MPC | 让 secret 在 Byzantine dealer 下可验证地固定，是异步 secure computation 的基础候选 | async MPC and BFT foundations | 当前 vault 只有 Canetti-Rabin source，需更多 direct source | queued |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Fast Asynchronous Byzantine Agreement with Optimal Resilience]] | paper | 给出 AVSS 的 A-RS/AWSS/AVSS 分层构造，并展示 AVSS 如何生成 global coin 以支持最优 resilience async BA | 完全异步私有信道；dynamic/unbounded adversary；10 页 extended abstract，完整证明转 technical report | Definition 2, Theorem 1, §5-§8 |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | paper | 给出 high-threshold AVSS route，用 asymmetric bivariate polynomial 支持 `k<=n-f` reconstruction，并作为 ADKG 的基础 primitive | PKI/authenticated links/computational adversary；无实现评测；细节服务于 ADKG setup | §3, Algorithms 1-2, Appendix B |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | paper | 给出 ADD/RBC-backed AVSS、ACSS 和 dual-threshold ACSS route，把相关通信复杂度降到 `O(kappa n^2)` | ACSS/dual-threshold constructions use additional crypto assumptions; no implementation benchmark | §5, Table 1 |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | paper | 给出 ACK-transcript PVSS、terminating degree-`2t` AVSS 和 selective-VE dual-threshold AVSS，并提供 Rust/WAN evaluation | PKI/private channels/RBC; static adversary; batching and adaptive security remain future work | Definitions 1-3, Algorithms 1-3, Theorems 1-3, §8 |
| [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling]] | paper | 作为 ACSS usage evidence：说明 low-threshold ACSS 可通过 distributed polynomial sampling 支撑 practical high-threshold ADKG，而不必直接使用昂贵 high-threshold ACSS。 | 不是 AVSS/ACSS 定义论文；安全模型是 static adversary；具体贡献主要归入 ADKG 节点 | §3.1, §4, Theorem 2, Table 3 |

## 正反例约束

- 正确: 把 AVSS 作为 async BFT/common-coin/randomized BA 的可复用 primitive。
- 正确: 在 source note 中保留 A-RS/AWSS/AVSS 的协议细节，在本节点中只抽象方法路线与适用边界。
- 错误: 把 Canetti-Rabin 1993 当作 `blockchain consensus` 的直接系统方案。
- 错误: 把 AVSS 直接等同于 Shamir secret sharing；AVSS 的核心是异步 Byzantine verifiability 和 reconstruction consistency。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: AVSS 是 async BFT 中把“局部随机 secret”提升为“全体 honest players 后续可一致使用的随机性或 key material”的基础层。Canetti-Rabin 1993 显示，在 `n >= 3t+1`、private channels 和 unbounded adversary 下，可通过 A-RS/AWSS/AVSS 分层构造 global coin；ADKG 2019/1015 补入 high-threshold AVSS，使 `n=3f+1` 异步 setting 可以支持 `2f+1` threshold setup；ADD 2021/777 又补入通信优化路线，用 ADD-backed RBC 和额外加密技巧把 AVSS、ACSS、dual-threshold ACSS 推到 `O(kappa n^2)`。VSS Simplified 2023/1196 说明 ACK transcript 可以同时提供公开可验证和异步终止，degree-`2t` sharing 修复异步公开缺失 shares 的 secrecy 问题，selective VE 进一步支撑 [[dual-threshold-asynchronous-vss|dual-threshold asynchronous VSS]]。Das et al. 2023 进一步说明，practical high-threshold ADKG 可以把 low-threshold ACSS 当作 substrate，再由上层 distributed polynomial sampling 生成高阶随机多项式，从而绕开昂贵 high-threshold ACSS。后续需要更多 VSS/AVSS/common-coin sources 来决定是否拆出独立的 `common coin`、`A-cast/RBC`、`ACSS`、`ICP`、`high-threshold AVSS` 和 `distributed polynomial sampling` 节点。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: VSS Simplified 2023/1196 includes a Rust implementation and WAN-style AWS evaluation, but no production deployment evidence.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new VSS/AVSS/common-coin/asynchronous secure computation source.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience|Fast Asynchronous Byzantine Agreement with Optimal Resilience]] | 新建 AVSS method/concept 节点；补入 AVSS -> global coin -> async BA 的 foundation path | 定义; 背景; 方法族; 代表 Sources; 当前综合 | yes, child/method under async BFT | 后续补 Bracha A-cast、Rabin common coin、modern AVSS/VSS sources |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | 补入 HA-VSS high-threshold route，并把 AVSS 从 common-coin foundation 扩展到 threshold setup foundation | 方法族; 代表 Sources; 当前综合; Bridge Links | no, keep as method under async BFT | 后续补 modern AVSS/high-threshold VSS sources |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | 补入 ADD/RBC-backed AVSS、ACSS 和 dual-threshold ACSS 通信优化路线 | 背景; 下级结构; 方法族; 代表 Sources; 当前综合 | yes, now supports dual-threshold child node with VSS Simplified | 后续补 ACSS/PVSS direct sources |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | 补入 ACK-transcript public verifiability, degree-`2t` terminating AVSS, selective-VE dual-threshold AVSS and implementation evidence | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes, promoted [[dual-threshold-asynchronous-vss|dual-threshold asynchronous VSS]] | 后续补 batching/adaptive-security VSS sources |
| [[sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling|Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling]] | 补入 low-threshold ACSS as high-threshold ADKG substrate 的 usage evidence | 背景; 方法族; 代表 Sources; 当前综合 | no, ADKG node carries main contribution | 后续判断 ACSS 和 distributed polynomial sampling 是否拆节点 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | `distributed-systems/consensus/byzantine-fault-tolerance; distributed-systems/consensus/asynchronous-bft-consensus` | dependency, translation | AVSS/global-coin and dual-threshold VSS machinery can inform asynchronous consensus and threshold setup foundations; transaction dissemination, validator economics, key rotation, private-channel assumptions and production common-coin engineering remain system-specific. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | is_a_method_for | nahida-knowledge-asynchronous-bft-consensus | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md | high | active_seed |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | depends_on | nahida-knowledge-byzantine-fault-tolerance | vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md; vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md | high | active_seed |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | evidenced_by | vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md | vault/03_Sources/papers/doi-10-1145-167088-167105-fast-asynchronous-byzantine-agreement-with-optimal-resilience.md | high | active_seed |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | evidenced_by | vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | high | active_seed |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | evidenced_by | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | high | active_seed |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | has_child | nahida-knowledge-dual-threshold-asynchronous-vss | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss.md; vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | high | active_seed |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | evidenced_by | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | high | active_seed |
| nahida-knowledge-asynchronous-verifiable-secret-sharing | evidenced_by | vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md | vault/03_Sources/papers/sha256-0cded3a5e352-practical-high-threshold-adkg-distributed-polynomial-sampling.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Canetti-Rabin technical report 尚未导入。 | Extended abstract 把 AWSS/AVSS/global-coin/BA 的完整证明转到 technical report | nahida-research-search or nahida-update | medium | queued |
| Bracha A-cast/RBC direct source 尚缺。 | AVSS 构造依赖 A-cast；async BFT 也常依赖 RBC/broadcast abstraction | nahida-research-search or nahida-update | high | queued |
| More VSS/AVSS sources 尚缺。 | 决定 AVSS 是否应继续拆出 VSS taxonomy、ICP、common coin 子节点 | nahida-update | medium | queued |
| ACSS 是否独立拆节点仍待更多 source。 | dual-threshold 已提升为子节点；ACSS completeness 本身仍需要更多 source 决定是否拆分。 | nahida-consolidate after more ACSS sources | medium | hold |
| Publicly verifiable VSS transcripts 是否独立拆节点待定。 | VSS Simplified 给出 ACK-transcript route；还需更多 PVSS/PVSS lineage source 判断是否从 dual-threshold 节点中拆出。 | nahida-update or nahida-research-search | medium | queued |
| High-threshold AVSS 是否应独立拆节点仍待更多 source。 | 当前 HA-VSS 主要由 ADKG 2019/1015 支撑；如果后续 DKG/common-coin sources 复用，应拆出子节点。 | nahida-consolidate after more sources | medium | hold |
| ACSS 是否应从 AVSS 下拆独立节点仍待更多 source。 | Das et al. 2023 强调 low-threshold ACSS 对 practical high-threshold ADKG 的作用，但当前仍更适合作为方法行。 | nahida-consolidate after more ACSS sources | medium | hold |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-canetti-rabin-optimal-async-ba | Created AVSS concept/method node from Canetti-Rabin 1993 and linked it under async BFT/BFT. | doi:10.1145/167088.167105 | codex |
| 2026-06-23 | nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft | Added HA-VSS high-threshold route from ADKG 2019/1015. | iacr:2019/1015 | codex |
| 2026-06-23 | nahida-knowledge-20260623-asynchronous-data-dissemination | Added ADD-backed AVSS, ACSS and dual-threshold ACSS communication route. | iacr:2021/777 | codex |
| 2026-06-23 | nahida-knowledge-20260623-verifiable-secret-sharing-simplified | Added ACK-transcript VSS, degree-`2t` terminating AVSS and promoted dual-threshold asynchronous VSS child node. | iacr:2023/1196 | codex |
| 2026-06-23 | nahida-knowledge-20260623-high-threshold-adkg-polynomial-sampling | Added low-threshold ACSS as high-threshold ADKG substrate evidence. | usenix:security23/das | codex |
