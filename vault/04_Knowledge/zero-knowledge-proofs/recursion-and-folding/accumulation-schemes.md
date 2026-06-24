---
id: "nahida-knowledge-accumulation-schemes"
title: "Accumulation schemes"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "accumulation-schemes"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
parent_knowledge_refs:
  - "nahida-knowledge-recursion-and-folding"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "accumulation-schemes"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/accumulation-schemes"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/fri-iopps"
  - "zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition"
relation_edges:
  - from: "nahida-knowledge-accumulation-schemes"
    relation: "is_a"
    to: "nahida-knowledge-recursion-and-folding"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/accumulation-schemes.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-accumulation-schemes"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-accumulation-schemes"
    relation: "depends_on"
    to: "nahida-knowledge-fri-iopps"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
      - "vault/05_Bridges/fri-iopps-to-accumulation-schemes.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-accumulation-schemes"
    relation: "applies_to"
    to: "nahida-knowledge-recursive-proof-composition"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-accumulation-schemes"
    relation: "bridges_to"
    to: "nahida-bridge-fri-iopps-to-accumulation-schemes"
    evidence_refs:
      - "vault/05_Bridges/fri-iopps-to-accumulation-schemes.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-fri-iopps-to-accumulation-schemes"
source_note_refs:
  - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
representative_source_refs:
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
query_keys:
  - "Accumulation schemes"
  - "accumulation-schemes"
  - "hash-based accumulation"
  - "Reed-Solomon proximity accumulation"
  - "ARC"
  - "proof-carrying data accumulation"
  - "PCD accumulation"
  - "IVC accumulation"
  - "accumulation without homomorphic vector commitments"
aliases:
  - "accumulation schemes"
  - "hash-based accumulation"
  - "RS proximity accumulation"
  - "PCD accumulation"
  - "IVC accumulation"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "accumulation-schemes"
  - "proof-carrying-data"
  - "incrementally-verifiable-computation"
  - "reed-solomon-proximity"
  - "fri-iopps"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-arc-accumulation-reed-solomon"
source_refs:
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
confidence: "high"
trust_tier: "primary"
---

# Accumulation schemes

## 定义与范围

- 定义: Accumulation schemes 把多个证明/声明/累加器实例压缩成一个新的累加器实例，使最终 decider 可以检查一个短状态，而不随历史步骤数线性增长。
- 不包含: 单个系统名、单篇论文、单次 benchmark 或某个 proof-system 的具体参数；这些属于 source note 或更窄的 source extension。
- Canonical terms: `accumulation schemes`, `accumulator`, `proof-carrying data`, `IVC`
- Aliases/query keys: hash-based accumulation, RS proximity accumulation, PCD accumulation, accumulation without homomorphic vector commitments.
- Standalone completeness check: 本节点本地说明 accumulation schemes 的问题、路线、边界、代表 sources、桥接和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 "Arc 是什么层级"、"accumulation 和 folding 有什么区别"、"hash-based PCD/IVC accumulation 怎么做" 时先读本节点。
- Update scope: 新 source 若改变 accumulation/folding/PCD 路线、承诺后端、安全模型、距离保持或 query complexity，应刷新本节点。

## 背景

在 PCD/IVC 中，系统需要不断把新的 computation/proof obligation 接到历史状态上。如果每一步都重新验证所有历史证明，verifier/circuit 会随时间增长。Accumulation schemes 的目标是把这些历史 obligation 变成一个可持续维护的 accumulator，再由最终 decider 检查。

[[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] 提供当前 vault 的主 seed。它把 prior accumulation 路线分成两类: 多数方案依赖 homomorphic vector commitments，成本较高且通常依赖 number-theoretic assumptions；BMNW24 的 hash-based 路线避免这些承诺，但只能支持 bounded consecutive accumulation depth。Arc 的贡献是把 RS proximity claim 做成 distance-preserving accumulation，从而支持 unbounded accumulation depth。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family`。
- 为什么足够通用: Accumulation schemes 是 PCD、IVC、recursive proof composition 和 folding-adjacent proof systems 反复使用的中层方法族。
- 为什么不是单篇论文/单个协议的局部概念: ARC 是代表 source；`accumulation schemes` 本身组织多条实现路线和后续 sources。
- 需要引用的更基础 Knowledge: [[recursion-and-folding|Recursion and folding]], [[recursive-proof-composition|Recursive proof composition]], [[fri-iopps|FRI IOPPs]]。
- 不应拆出的实例/协议/来源: ARC、BMNW24、Protostar/ProtoGalaxy、具体 Merkle opening counts 和 delayed-FFT 参数默认作为 source extension，除非多来源支持独立 child。

## 解决的问题

Accumulation schemes 解决的是递归/增量证明中的历史验证成本问题:

- 如何把多个 proofs/claims/accumulators 合并成一个短的 running state；
- 如何让最终 verifier 不随累计步骤数线性增长；
- 如何避免把完整 verifier 或所有历史 witness 反复放入递归电路；
- 如何在不同承诺后端和安全假设下保持 soundness/knowledge soundness。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[recursion-and-folding|Recursion and folding]] | child_of / method_family | Arc introduction and reductions-to-PCD route | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Reed-Solomon proximity accumulation | method route | 当前由 Arc 单一 source 支撑；先作为路线，不拆独立 node | [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] | keep_as_section |
| Homomorphic-VC accumulation | contrast route | 需要 primary sources for BCLMS/Protostar/ProtoGalaxy 等；Arc 只作为 related-work contrast | Arc related work | queued |
| IOR-based accumulation formalism | formal route | 当前是 Arc 的形式化工具，先不独立拆 node | Arc §5 and Appendix B | keep_as_section |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| homomorphic vector commitment accumulation | 用 homomorphic VC 支持线性合并/累加证明 obligation。 | 承诺后端支持所需 homomorphism，且系统可接受 number-theoretic assumptions。 | 可能需要大域/群操作；post-quantum 边界和 concrete cost 需具体 source 校准。 | Arc related-work contrast; dedicated sources queued |
| bounded-depth hash-based accumulation | 用 hash/Merkle 路线避免 homomorphic VC，但牺牲连续 accumulation depth。 | 深度可预先界定，且参数可随 depth 设定。 | depth bound 影响效率和安全边界。 | Arc contrast to BMNW24 |
| Reed-Solomon proximity accumulation | 将多个 RS proximity claims 通过随机组合、out-of-domain binding、quotient 和 Merkle/oracle access 归约成一个 distance-preserving proximity claim。 | statement 可路由为 RS code proximity；field/rate/list-decoding 参数满足 source 条件。 | 当前由 Arc 单一 source 支撑；依赖 ROM/Merkle commitments/proximity-gap assumptions。 | [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] |
| NP/R1CS accumulation via RS proximity | 把 R1CS witness 编码为 RS word，并用 accumulator relation 维护 proximity and algebraic constraints。 | NP/R1CS 或可表达为相应 polynomial relation。 | 形式复杂；具体系统还需 outer argument/PCD integration。 | [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] |
| IOR-to-noninteractive reduction route | 用 interactive oracle reductions 表达 oracle-message reductions，再通过 Merkle commitments 和 Fiat-Shamir 编译为 non-interactive reductions。 | 需要 ROM、Merkle multi-extractability、monotone committed relations 等条件。 | 不是所有 IOP/IP 自动满足；具体 soundness 依赖 protocol state function。 | [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]] | paper | 创建本节点的主 seed；提供 hash-based, RS-proximity, unbounded-depth accumulation route and IOR formalism | ROM; RS/list-decoding/proximity assumptions; no implementation benchmark; ePrint URL unverified | `Abstract`, `§1-§2`, `§6-§7`, `Appendix A-B` |

## 正反例约束

- 正确: 把 ARC 当作 accumulation schemes 的代表 source extension。
- 正确: 把 RS proximity/list-decoding/Merkle/IOR 作为 method route，而不是把它们全部拆成 paper-shaped concepts。
- 正确: 与 [[folding-schemes|Folding schemes]] 并列/相邻；两者都服务 PCD/IVC/recursive proof systems，但机制不同。
- 错误: 把 ARC 归为 `folding-schemes` 本身；论文把 folding 作为相邻 prior route。
- 错误: 把 Merkle-committed RS codewords 当成 full polynomial commitments API。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`，主 evidence 为 Arc source note。
- Freshness: `fresh` for local vault absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: Accumulation schemes 是 `recursion-and-folding` 方向下独立于但相邻于 folding schemes 的方法族。Arc 显示一条重要路线: 把 RS proximity 的 IOPP/list-decoding/quotient tools 迁移到 accumulation，使 hash-based accumulation 不再需要预设 bounded depth。它把 recursive proof/PCD 的难点从 homomorphic vector commitments 转为 RS proximity、Merkle commitments、out-of-domain binding 和 IOR soundness。

## 领域态势

- Research dynamics note: not_applicable
- Academic focus summary: current-vault-only; Arc shows active movement toward transparent/hash-based accumulation but cannot alone define the whole field.
- Industrial focus summary: no implementation/repo evidence in this source.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: Protostar/ProtoGalaxy/BCLMS/BMNW24/HyperNova/Halo2 sources or implementations.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]] | creates accumulation-schemes node; adds hash-based RS proximity route; corrects queue placement from folding-schemes to accumulation-schemes | 定义; 方法族; 当前综合; Bridge Links | yes | absorb related accumulation/folding sources for taxonomy calibration |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[fri-iopps-to-accumulation-schemes|FRI IOPPs -> accumulation schemes]] | `zero-knowledge-proofs/proof-systems/fri-iopps; zero-knowledge-proofs/recursion-and-folding/accumulation-schemes` | method_transfer, dependency, shared_pattern, formalization_bridge | RS proximity/list-decoding/quotient tools transfer to accumulation; full FRI/STARK proof-system semantics and DAS commitments do not automatically transfer. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-accumulation-schemes | is_a | nahida-knowledge-recursion-and-folding | this node and parent direction | high | active_seed |
| nahida-knowledge-accumulation-schemes | evidenced_by | vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md | Arc source note | high | active_seed |
| nahida-knowledge-accumulation-schemes | depends_on | nahida-knowledge-fri-iopps | Arc RS proximity/list-decoding route; bridge note | high | active_seed |
| nahida-knowledge-accumulation-schemes | applies_to | nahida-knowledge-recursive-proof-composition | Arc PCD/IVC route | high | active_seed |
| nahida-knowledge-accumulation-schemes | bridges_to | nahida-bridge-fri-iopps-to-accumulation-schemes | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| BCLMS/BCMS PCD-from-accumulation primary sources not yet absorbed. | Needed to ground accumulation schemes beyond Arc's related-work summary. | nahida-update / nahida-research-search | high | queued |
| BMNW24 Accumulation without Homomorphism not absorbed. | Direct predecessor for bounded-depth hash-based accumulation. | nahida-update | high | queued |
| Protostar/ProtoGalaxy/HyperNova/Halo2 related sources missing. | Needed to calibrate accumulation vs folding taxonomy and practical routes. | nahida-update | medium | queued |
| Original FRI/STIR/DEEP-FRI sources still thin. | Arc depends on RS proximity tools; FRI node should not rely only on Arc/FRIDA. | nahida-update / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-arc-accumulation-reed-solomon | Created accumulation-schemes method-family node from Arc; added RS proximity/hash-based accumulation route and FRI bridge. | 1 source note | codex |
