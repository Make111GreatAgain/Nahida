---
id: "nahida-knowledge-gkr-protocols"
title: "GKR-style interactive proofs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "gkr-protocols"
domain_id: "verifiable-computation"
direction_id: "interactive-proofs"
parent_knowledge_refs:
  - "nahida-knowledge-interactive-proofs"
child_knowledge_refs: []
ontology_path:
  - "verifiable-computation"
  - "interactive-proofs"
  - "gkr-protocols"
primary_ontology_path: "verifiable-computation/interactive-proofs/gkr-protocols"
secondary_ontology_paths:
  - "verifiable-computation/interactive-proofs/delegated-computation"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
relation_edges:
  - from: "nahida-knowledge-gkr-protocols"
    relation: "is_a"
    to: "nahida-knowledge-interactive-proofs"
    evidence_refs:
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/gkr-protocols.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-gkr-protocols"
    relation: "applies_to"
    to: "nahida-knowledge-delegated-computation"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
      - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-gkr-protocols"
    relation: "depends_on"
    to: "nahida-knowledge-sum-check-protocol"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
      - "vault/04_Knowledge/verifiable-computation/interactive-proofs/sum-check-protocol.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-gkr-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-gkr-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
    confidence: "high"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md"
  - "vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md"
representative_source_refs:
  - "doi:10.1145/1374376.1374396"
  - "arxiv:1304.3812v4"
query_keys:
  - "GKR protocol"
  - "GKR-style interactive proofs"
  - "Goldwasser Kalai Rothblum protocol"
  - "time-optimal GKR"
  - "verifiable circuit evaluation"
  - "delegated circuit evaluation"
  - "layered arithmetic circuit verification"
  - "GKR prover optimization"
aliases:
  - "GKR protocol"
  - "Goldwasser-Kalai-Rothblum protocol"
  - "Time-optimal GKR"
domains:
  - "verifiable-computation"
topics:
  - "gkr-protocols"
  - "delegated-computation"
  - "sum-check-protocol"
  - "verifiable-circuit-evaluation"
  - "regular-circuit-verification"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-time-optimal-interactive-proofs"
source_refs:
  - "doi:10.1145/1374376.1374396"
  - "arxiv:1304.3812v4"
confidence: "medium"
trust_tier: "primary"
---

# GKR-style interactive proofs

## 定义与范围

- 定义: GKR-style interactive proofs 指以 Goldwasser-Kalai-Rothblum protocol 为核心的一类分层电路验证协议：prover 声称某个 layered arithmetic circuit 的输出，verifier 通过每层的 sum-check 归约，把输出层 claim 逐层降到输入层的 multilinear extension claim。
- 不包含: 任意交互式证明、任意 SNARK、单个实现优化或某篇论文的一次 benchmark。Time-optimal GKR、GPU 实现、matrix multiplication 专用协议和 data-parallel batching 都是 source extension，而不是本节点的全部定义。
- Canonical terms: `GKR protocol`, `GKR-style interactive proofs`, `Goldwasser-Kalai-Rothblum protocol`
- Retrieval role: 让关于 `GKR`, `verifiable circuit evaluation`, `delegated circuit evaluation`, `time-optimal prover`, `GKR inside SNARK` 的查询先进入一个方法族节点，而不是直接散到多篇 source note。
- Update scope: 新 source 若改变 GKR 的适用电路、prover/verifier 成本、sum-check 组织方式、SNARK/IOP 编译边界或应用场景，应刷新本节点。

## 背景

GKR 属于 [[interactive-proofs|Interactive proofs]] 方向，主要服务 [[delegated-computation|Delegated computation]]: 弱 verifier 把大计算交给强 prover 后，希望用少量通信、少量空间和远低于重算的时间检查结果。GKR 的基本对象是 layered arithmetic circuit，每一层 gate 的 wiring 被编码成低度多项式，协议用 [[sum-check-protocol|Sum-check protocol]] 验证上一层 multilinear extension claim 与下一层 gate values 的关系。

本节点的 source-backed seed 目前来自两类材料：原始 GKR/delegated-computation source seed 说明协议形态和 verifiable outsourcing 背景；Thaler 2017 的 time-optimal source 说明当电路 wiring 足够 regular 时，GKR prover 可以从 `O(S log S)` 降到 `O(S)`。

## 解决的问题

| 问题 | 为什么重要 | GKR 路线 | 限制 |
| --- | --- | --- | --- |
| 外包电路计算的低成本验证 | verifier 不想重算整个 circuit，但需要 soundness | 把输出 claim 逐层转化为输入层 claim | 电路要能表达为 layered arithmetic circuit |
| Prover overhead 过高 | 早期 GKR 实现虽然 verifier 便宜，但 prover `O(S log S)` 会阻碍实践 | 重写每层 sum-check polynomial 并复用工作，特定 regular circuits 可达 `O(S)` | 依赖 wiring regularity；不是任意 irregular circuit 的通用优化 |
| Data-parallel computation 验证 | 批量独立子计算常见于 counting queries、ML/数据处理和可验证外包 | 利用 batch copies 之间的规则结构，把 full super-circuit 的额外 overhead 拿掉 | 聚合逻辑要简单或另行验证 |
| 与现代 ZKP/SNARK 的关系边界 | 后续系统常说 "GKR inside SNARK" 或 "GKR-style sumcheck" | GKR/sum-check 可作为 public-coin/IOP/PIOP 组件 | Commitments、Fiat-Shamir、zero knowledge、non-interactivity 不由 GKR 本身提供 |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[interactive-proofs|Interactive proofs]] | is_a / method_family_under | GKR 是交互式证明中的分层电路验证方法族 | active_seed |
| [[delegated-computation|Delegated computation]] | applies_to | GKR 的主要问题背景是外包计算验证 | active_seed |
| [[sum-check-protocol|Sum-check protocol]] | depends_on | GKR 每层归约依赖 sum-check | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么暂不拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| time-optimal GKR refinement | source_extension | 主要是 Thaler 2017 对 regular circuits 的优化，不是独立 foundation | [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | source_extension |
| data-parallel verifiable computation | candidate problem | 已有 Theorem 2 seed，但需要更多来源再判断是否拆 L3/L4 节点 | Thaler 2017 p31-p36 | watching |
| matrix-multiplication verification | application/specialized primitive | Theorem 3 很重要，但目前仍是专用协议/应用 extension | Thaler 2017 p38-p41 | source_extension |
| GKR inside SNARK / recursive proof systems | bridge candidate | 已通过 Sparrow、public-coin recursion 等 sources 进入 bridge，但 endpoint 在 ZKP proof systems | existing bridge/source notes | keep_as_bridge |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Layer-by-layer GKR reduction | 对每层 circuit gate relation 运行 sum-check，把 `V_i` 的 claim 归约为 `V_{i+1}` 的 claim。 | layered arithmetic circuit；wiring predicates 可被低度扩展表达 | verifier 便宜，但 naive prover 会扫描大量 gate/wiring 多轮 | [[doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles|Delegating Computation: Interactive Proofs for Muggles]] |
| Time-optimal regular-circuit GKR | 用 lower-dimensional dense polynomial `g_z^(i)` 替换 sparse `f_z^(i)`，并用 `C^(j)` / `V^(j)` arrays 复用 sum-check rounds 的工作。 | regular wiring pattern；多数层 in-neighbor functions similar | Theorem 1 不覆盖 arbitrary irregular circuits；实现仍依赖电路结构识别 | [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] |
| Data-parallel GKR batching | 对 `B` 个互不交互的 sub-computations 构造 super-circuit，但 sum-check 只利用重复结构，避免额外 `log(BS)` overhead。 | 同一个 sub-circuit 的多批独立输入；聚合简单 | 子计算内部仍可 irregular；prover time 仍有 `B*S*log S` 级别 | [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] |
| Specialized algebraic primitive | 对 matrix multiplication 直接用 higher-degree extensions 和 sum-check，不走完整 circuit checking。 | matrix multiplication 或 repeated matrix multiplication as primitive | 专用路线，不能替代一般 GKR | [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles|Delegating Computation: Interactive Proofs for Muggles]] | paper | GKR/delegated computation seed source；支撑本节点的协议家族定位 | 当前笔记是已吸收 source，仍需更多 canonical/foundation comparisons 扩展 | `source note` |
| [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | paper | 将 GKR-style circuit evaluation 的 prover overhead 在 regular circuits 上降到 `O(S)`，并扩展到 data-parallel 和 matrix multiplication 场景 | 不是 SNARK/zero-knowledge paper；不解决任意 irregular circuits | `p1-p50`, `Theorem 1-3`, `Tables 1-5` |

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，只代表当前 vault 已吸收资料。
- Freshness: `fresh` for vault synthesis; not an external latest trend claim.
- Valid until: `2026-07-23`。
- 综合: GKR 是 verifiable computation 中连接 interactive proofs、delegated computation 和 sum-check 的关键方法族。Thaler 2017 让本节点不再只是“可验证外包的理论协议”，而能记录一个实践化问题: 如何让 prover overhead 接近直接计算。当前最稳的上层结论是，GKR 的 durable role 是“分层电路验证方法族”；time-optimal prover、data-parallel batching、matrix multiplication primitive 都应作为 source extensions，后续若有多篇来源再拆成独立 problem/application 节点。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation|Time-Optimal Interactive Proofs for Circuit Evaluation]] | 补充 time-optimal regular-circuit GKR、data-parallel GKR batching、matrix multiplication verification primitive | 方法族与解决路线; 当前综合; 缺口与队列 | yes | 后续可吸收更多 GKR/streaming IP/IOP source 来判断子节点拆分 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| none promoted in this run | not_applicable | not_applicable | 本次只创建方法族节点；GKR 到 SNARK/zkML/recursion 的跨域迁移继续由已有 bridges 承载。 | review |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-gkr-protocols | is_a | nahida-knowledge-interactive-proofs | vault/04_Knowledge/verifiable-computation/interactive-proofs/gkr-protocols.md; vault/04_Knowledge/verifiable-computation/interactive-proofs.md | high | active_seed |
| nahida-knowledge-gkr-protocols | applies_to | nahida-knowledge-delegated-computation | GKR/delegated computation source seed; Thaler 2017 p4-p7 | high | active_seed |
| nahida-knowledge-gkr-protocols | depends_on | nahida-knowledge-sum-check-protocol | Thaler 2017 p12-p24 | high | active_seed |
| nahida-knowledge-gkr-protocols | evidenced_by | vault/03_Sources/papers/doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles.md | source note | medium | active_seed |
| nahida-knowledge-gkr-protocols | evidenced_by | vault/03_Sources/papers/arxiv-1304-3812v4-time-optimal-interactive-proofs-for-circuit-evaluation.md | source note p1-p50 | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| GKR 原始论文/后续 streaming IP/IOP comparison 仍需更多来源校准。 | 当前节点已有 seed，但还不是完整 evergreen foundation。 | nahida-update / nahida-research-search | high | queued |
| Data-parallel verifiable computation 是否应独立成问题节点尚未定。 | Thaler 2017 给出强 seed，但还需要更多来源确认其可复用边界。 | nahida-update | medium | watching |
| GKR 到 SNARK/zkML/recursion 的迁移边界需要 bridge 级持续维护。 | GKR/sum-check 常被后续系统借用，但不应把 SNARK 组件混进 GKR 定义。 | nahida-knowledge-get / nahida-consolidate | medium | active_seed |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-time-optimal-interactive-proofs | Created method-family node for GKR-style interactive proofs and attached Thaler time-optimal GKR source extension. | 2 source notes | codex |
