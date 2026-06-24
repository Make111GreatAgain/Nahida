---
id: "nahida-knowledge-dual-threshold-asynchronous-vss"
title: "Dual-threshold asynchronous VSS"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "method"
hierarchy_level: "method"
file_slug: "dual-threshold-asynchronous-vss"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-asynchronous-verifiable-secret-sharing"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-verifiable-secret-sharing"
  - "dual-threshold-asynchronous-vss"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss"
secondary_ontology_paths:
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation"
relation_edges:
  - from: "nahida-knowledge-dual-threshold-asynchronous-vss"
    relation: "is_a_method_for"
    to: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-dual-threshold-asynchronous-vss"
    relation: "depends_on"
    to: "nahida-knowledge-asynchronous-reliable-broadcast"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-dual-threshold-asynchronous-vss"
    relation: "supports"
    to: "nahida-knowledge-asynchronous-distributed-key-generation"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-dual-threshold-asynchronous-vss"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-dual-threshold-asynchronous-vss"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
    confidence: "high"
    status: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
  - "vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md"
representative_source_refs:
  - "iacr:2021/777"
  - "iacr:2023/1196"
query_keys:
  - "Dual-threshold asynchronous VSS"
  - "dual-threshold-asynchronous-vss"
  - "dual-threshold AVSS"
  - "dual-threshold ACSS"
  - "PVSS dual threshold"
  - "secrecy threshold ell"
  - "degree 2t AVSS"
  - "selective verifiable encryption"
  - "publicly verifiable AVSS"
aliases:
  - "dual-threshold AVSS"
  - "DtAVSS"
  - "dual-threshold ACSS"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "asynchronous-verifiable-secret-sharing"
  - "dual-threshold-avss"
  - "publicly-verifiable-secret-sharing"
  - "asynchronous-distributed-key-generation"
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
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
  - "nahida-knowledge-20260623-verifiable-secret-sharing-simplified"
source_refs:
  - "iacr:2021/777"
  - "iacr:2023/1196"
confidence: "high"
trust_tier: "primary"
---

# Dual-threshold asynchronous VSS

## 定义与范围

- 定义: Dual-threshold asynchronous VSS 是异步 Byzantine secret-sharing 方法族，它把容错阈值 `t` 与 secrecy/reconstruction 阈值 `ell` 分开，使协议在 `t` 个 Byzantine 节点下仍能完成分享，同时对最多 `ell` 个观察/合谋方保持 secret 隐藏。
- 不包含: 某篇 VSS 论文、完整 ADKG、完整 common coin、threshold signature 实现或区块链 validator key-management policy；这些分别留在 source notes 或上层系统节点。
- Canonical terms: `dual-threshold-asynchronous-vss`, `dual-threshold AVSS`
- Aliases/query keys: dual-threshold ACSS, PVSS dual threshold, secrecy threshold `ell`, degree-`2t` AVSS, selective verifiable encryption.
- Standalone completeness check: 本节点给出定义、问题、方法路线、代表 source、边界和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询双阈值 AVSS/ACSS、PVSS with `ell`、high secrecy threshold asynchronous sharing 时先到本节点。
- Update scope: 新 source 若改变 `ell` range、public verifiability、completeness/termination model、VE assumptions、ACSS/AVSS boundary 或 ADKG application，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

普通 AVSS 往往把容错阈值和 secrecy/reconstruction 阈值绑在一起。对 async BFT setup、DKG、threshold cryptography 和 randomness beacon 来说，这不总够用: 系统可能只希望容忍 `t` 个 Byzantine 节点破坏协议执行，却希望 secret 在更高的重构阈值 `ell` 之前保持隐藏。

异步网络的难点是等待集合不稳定。一个 dealer 可以先拿到 `n-t` 个 ACK，又被迫公开缺失节点的 share material；如果仍用低度数多项式，公开信息和腐化方持有信息合起来可能超过 secrecy limit。Dual-threshold AVSS/ACSS 的核心，就是在保证完成性的同时限制可见 share 数量。

## 基础概念判断

- 是否是基础概念/方向/问题: `method` / `method`。
- 为什么足够通用: 该问题同时出现在 ADD 2021/777 的 dual-threshold ACSS 和 VSS Simplified 2023/1196 的 dual-threshold AVSS 中，且上接 ADKG、threshold setup 和 async BFT common-coin layer。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 两个独立 source 都围绕 `t` 与 `ell` 分离给出路线；具体 PVSS/NIZK/VE 实现留在 source note。
- 需要引用的更基础 Knowledge: [[asynchronous-verifiable-secret-sharing|asynchronous-verifiable-secret-sharing]], [[asynchronous-reliable-broadcast|asynchronous-reliable-broadcast]]。
- 不应拆出的实例/协议/来源: VSS Simplified Algorithm 3、ADD dual-threshold ACSS 具体 construction、Groth VE/Pedersen VE 修改留在 source notes；若后续 VE 多源复用，再拆 `verifiable-encryption` 知识节点。

## 解决的问题

Dual-threshold asynchronous VSS 解决的是: 在 `n >= 3t+1` 的异步 Byzantine 网络中，如何让分享协议容忍 `t` 个 Byzantine 节点，同时让 adversary 或观察者即使看到协议中的公开修复信息，也无法在达到更高阈值 `ell` 之前恢复 secret。

它不是单纯“把阈值调高”。异步场景会公开缺失 share 或加密 share 以保证完成性，因此协议必须精确控制公开 opening、recipient-specific recovery 和 transcript verifiability 的组合。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | method_for | Dual-threshold AVSS/ACSS is a specialized AVSS route for separating `t` and `ell`. | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| publicly verifiable VSS transcripts | method candidate | ACK/PVSS transcripts allow third parties to validate dealer success without rerunning sharing. | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] | hold |
| verifiable encryption for committed shares | primitive candidate | VE is the recovery mechanism that keeps hidden missing shares recipient-decryptable and publicly checkable. | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]]; [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| PVSS-based dual-threshold ACSS | 用 publicly verifiable encrypted shares 和 NIZK proofs 支持 completeness 与更高 secrecy threshold `ell`。 | asynchronous complete secret sharing, `ell < n-t`, cryptographic assumptions for PVSS/NIZK | Arbitrary secret may need extra transform; construction details live in source note. | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| Degree-`2t` AVSS plus selective VE | 使用 degree-`2t` sharing；对缺失 ACK 的节点只公开 `2t-ell` 份 share，并把 `ell-t` 份 verifiably encrypt 给目标 recipient。 | asynchronous network, `n >= 3t+1`, `ell in [t,n-t)`, PKI, signatures, RBC, polynomial commitments and VE | More interactive than non-interactive VE schemes; reconstruction cost higher than degree-`t` AVSS. | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] |
| Common-case ACK waiting | Dealer waits briefly for extra ACKs so fewer missing shares need VE; if enough ACKs arrive, dual-threshold support is nearly free. | Practical WAN settings with bounded observed delay parameter for optimization only | Optimization cannot replace worst-case async correctness; needs timeout/tuning. | [[eprint-2023-1196-verifiable-secret-sharing-simplified|VSS Simplified 2023/1196]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | paper | 把 ADD/RBC-backed AVSS 扩展到 ACSS 和 dual-threshold ACSS，并显示通信可达 `O(kappa n^2)`。 | Focus is communication complexity; no implementation benchmark for the dual-threshold route. | §5, Table 1 |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | paper | 给出 ACK-transcript PVSS、terminating degree-`2t` AVSS 和 selective-VE dual-threshold AVSS，并提供 Rust/WAN evaluation。 | Static adversary, PKI/private channels/RBC; batching and adaptive security remain future work. | Definitions 1-3, Algorithms 2-3, Theorem 3, §8 |

## 正反例约束

- 正确: 把 dual-threshold AVSS 作为 AVSS/ACSS 中处理 `t` vs `ell` 分离的 reusable method。
- 正确: 在 source note 中保留具体 ACK transcript、PVSS/NIZK/VE 和 Pedersen commitment details。
- 错误: 把 dual-threshold AVSS 等同于 ADKG。ADKG 可以使用它，但 ADKG 还需要 dealer selection、key-share agreement 和 common-coin/signature setup 逻辑。
- 错误: 忽略 RBC/termination 条件。没有 reliable broadcast totality，异步 sharing transcript 不能保证所有 honest nodes eventually finish。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: Dual-threshold asynchronous VSS 是 AVSS 栈中应独立检索的方法层。ADD 2021/777 先显示 dual-threshold ACSS 可以通过 PVSS/NIZK 和改进传播层达到二次通信复杂度；VSS Simplified 2023/1196 进一步说明，可以用 ACK transcript、degree-`2t` sharing 和 selective verifiable encryption 同时获得公开可验证、异步终止和双阈值 secrecy，并在 256 节点 WAN 实验中显著降低 VE-only baseline 的带宽与延迟。这个节点向上支撑 ADKG、common coin、threshold signatures 和 async BFT setup，但不替代这些上层协议。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: current implementation evidence comes only from VSS Simplified 2023/1196.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new VSS/PVSS/ACSS, DKG, randomness beacon or threshold-signature setup source.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | 从 AVSS 父节点的 `hold` candidate 提升为 dual-threshold AVSS/ACSS 方法节点的第一证据。 | 背景; 方法族; 代表 Sources | yes, child/method under AVSS | 后续补 ACSS/PVSS direct sources |
| [[eprint-2023-1196-verifiable-secret-sharing-simplified|Verifiable Secret Sharing Simplified]] | 补入 ACK-transcript, degree-`2t`, selective-VE and implementation evidence。 | 定义; 方法族; 当前综合; Bridge Links | yes, confirms split gate | 后续补 batching/adaptive-security VSS sources |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | `distributed-systems/consensus/asynchronous-bft-consensus` | dependency, setup_transfer | Dual-threshold AVSS transfers as publicly verifiable threshold setup/common-randomness machinery; it does not transfer validator membership, key-rotation operations, mempool policy, execution or data availability. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-dual-threshold-asynchronous-vss | is_a_method_for | nahida-knowledge-asynchronous-verifiable-secret-sharing | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss.md | high | active_seed |
| nahida-knowledge-dual-threshold-asynchronous-vss | depends_on | nahida-knowledge-asynchronous-reliable-broadcast | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | high | active_seed |
| nahida-knowledge-dual-threshold-asynchronous-vss | supports | nahida-knowledge-asynchronous-distributed-key-generation | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | medium | active_seed |
| nahida-knowledge-dual-threshold-asynchronous-vss | evidenced_by | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | high | active_seed |
| nahida-knowledge-dual-threshold-asynchronous-vss | evidenced_by | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | vault/03_Sources/papers/eprint-2023-1196-verifiable-secret-sharing-simplified.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Direct PVSS/class-group VSS sources 尚缺。 | 当前 dual-threshold 节点有 ADD/VSS Simplified 两条路线，但 PVSS lineage 还薄。 | nahida-research-search or nahida-update | medium | queued |
| Adaptive/batched dual-threshold AVSS 尚缺。 | VSS Simplified 把 batching and adaptive security 列为未来方向。 | nahida-update | medium | queued |
| Verifiable encryption 是否拆独立节点待定。 | VE 同时出现在 VSS Simplified 和 SAVER 等 source 中；需要跨 ZK/VSS 领域统一边界。 | nahida-consolidate after more VE sources | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-verifiable-secret-sharing-simplified | Created dual-threshold asynchronous VSS method node from ADD 2021/777 and VSS Simplified 2023/1196. | iacr:2021/777; iacr:2023/1196 | codex |
