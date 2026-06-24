---
id: "nahida-knowledge-fri-iopps"
title: "FRI IOPPs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "fri-iopps"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "fri-iopps"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/fri-iopps"
secondary_ontology_paths:
  - "blockchain-systems/data-availability-and-light-clients/data-availability-sampling"
relation_edges:
  - from: "nahida-knowledge-fri-iopps"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/fri-iopps.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fri-iopps"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fri-iopps"
    relation: "bridges_to"
    to: "nahida-bridge-fri-iopps-to-data-availability-sampling"
    evidence_refs:
      - "vault/05_Bridges/fri-iopps-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fri-iopps"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fri-iopps"
    relation: "bridges_to"
    to: "nahida-bridge-fri-iopps-to-accumulation-schemes"
    evidence_refs:
      - "vault/05_Bridges/fri-iopps-to-accumulation-schemes.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-fri-iopps-to-data-availability-sampling"
  - "nahida-bridge-fri-iopps-to-accumulation-schemes"
source_note_refs:
  - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
  - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
representative_source_refs:
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
query_keys:
  - "FRI IOPPs"
  - "FRI"
  - "Fast Reed-Solomon IOPP"
  - "interactive oracle proofs of proximity"
  - "FRI commitments"
  - "FRI data availability"
  - "opening-consistency"
  - "Reed-Solomon proximity accumulation"
  - "FRI to accumulation"
  - "ARC"
aliases:
  - "FRI"
  - "FRI proximity proofs"
  - "FRI interactive oracle proofs of proximity"
  - "RS proximity"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "fri-iopps"
  - "interactive-oracle-proofs-of-proximity"
  - "reed-solomon-codes"
  - "opening-consistency"
  - "data-availability-sampling"
  - "reed-solomon-proximity-accumulation"
  - "accumulation-schemes"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-frida-data-availability-from-fri"
  - "nahida-knowledge-20260623-arc-accumulation-reed-solomon"
source_refs:
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
confidence: "medium"
trust_tier: "primary"
---

# FRI IOPPs

## 定义与范围

- 定义: FRI IOPPs 是以 Reed-Solomon code proximity 为核心的 interactive oracle proof of proximity 方法族，通过递归 folding、随机查询和 Merkle-authenticated oracle access，让 verifier 以少量查询检查一个 evaluation vector 是否接近低度多项式 codeword。
- 不包含: FRIDA 论文的 DAS construction 细节、具体参数脚本、单次效率表、或某个 STARK/FRI 实现仓库；这些属于 source note 或相邻节点的 source extension。
- Canonical terms: `FRI`, `FRI IOPP`, `Fast Reed-Solomon IOPP`
- Aliases/query keys: FRI proximity proofs, interactive oracle proofs of proximity, opening-consistency, FRI commitments
- Standalone completeness check: 本节点本地说明 FRI IOPPs 的问题、机制、边界、代表 source、桥接和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 “FRI 是什么层级”“FRI 如何用于 DAS”“FRI 和 polynomial commitments/data availability 的关系”时先读本节点。
- Update scope: 新 source 若提供 FRI/DEEP-FRI/STARK/transparent commitment primary evidence，或改变 FRI 与 DAS/PCS 的关系，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

FRI 属于 proof-system / IOPP 方向，而不是单篇应用系统。FRIDA 使用 FRI 的 folding 和 query consistency 来构造 erasure-code commitments，再服务 data availability sampling。Arc 使用 Reed-Solomon proximity、quotienting、out-of-domain samples 和 list-decoding/proximity-gap machinery 来构造 accumulation schemes，这说明 FRI/IOPP 侧的 RS proximity 工具还能迁移到 recursion/folding 的 accumulation 层。当前 vault 还没有原始 FRI、DEEP-FRI、STARK foundation source；因此本节点仍是 `foundation_thin`。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family`
- 为什么足够通用: FRI 是 STARK/transparent proof systems、proximity testing、FRI-style commitments 和 FRIDA-like DAS constructions 会反复引用的方法族，不等于 FRIDA 这篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: FRIDA 只是当前代表 source；本节点保存的是 Reed-Solomon proximity/folding/query-check 这类可迁移方法。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[polynomial-commitments|Polynomial commitments]]。
- 不应拆出的实例/协议/来源: FRIDA、具体 fan-in/batch-size 参数、某次 table 结果和 Appendix D scripts 留在 source note。

## 解决的问题

FRI IOPPs 解决的是如何让 verifier 低成本检查一个被 Merkle/Oracle 承诺的 evaluation vector 是否接近 Reed-Solomon code，即是否可解释为低度多项式在某个 domain 上的取值。

这个问题在 ZKP/VC 中常作为透明 proof-system primitive；在 FRIDA 中，它被进一步要求满足 opening-consistency，才能安全地作为 data availability sampling 的 erasure-code-commitment backend。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of / method_family | FRIDA §4 uses FRI as an IOPP and proves a reusable consistency property | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| DEEP-FRI | method variant | 原始/DEEP-FRI sources 尚未吸收，当前不拆 | FRIDA references only | queued |
| FRI commitments | adjacent route | 需要 PCS/transparent commitment primary sources；FRIDA 明确区分 erasure-code commitments 与 full polynomial commitments | FRIDA §1.3 | review |
| Batched FRI | route section | FRIDA 附录给出 opening-consistency 扩展，但目前单 source | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] | keep_as_section |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Reed-Solomon proximity testing | 检查 oracle vector 是否接近某个 RS codeword，而不读取全部 vector。 | statement 可编码为低度多项式/evaluation vector。 | proximity 不等于某个位置 opening 与 unique closest codeword 一致。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| Recursive FRI folding | 每轮用随机 challenge 对 preimage block 做 algebraic folding，逐步降低 degree bound 和 domain size。 | domain 支持 smooth multiplicative subgroup / folding map，通常配合 Merkle oracle。 | 需要 soundness analysis；参数影响 proof/opening size。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| Query consistency checks | verifier 随机抽样 base position，并沿 folding chain 检查各层 oracle 一致性。 | IOPP non-adaptive and query-selectable when要编译为 commitment/opening protocol。 | 普通 soundness 不足以给 DAS code-binding。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| Opening-consistent FRI | 用 Lucky/Bad/suitable transcript analysis 证明: 若查询到与 unique closest codeword 不一致的 base symbol，verifier rejects。 | erasure-code commitment 或 DAS 需要 opened symbols code-binding。 | 是 FRIDA 对 FRI 的额外性质证明；不是所有 IOPP 自动满足。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| Batched FRI / interleaved RS | 将多条 RS codeword 随机线性组合后跑 FRI，查询时检查 batch consistency。 | 需要降低 encoding/opening overhead，且能承受 batch soundness 参数。 | analysis 多一个 batching lucky/bad layer；当前只有 FRIDA source。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| RS proximity accumulation transfer | 用 RS proximity/list-decoding/quotienting patterns 构造 distance-preserving many-to-one reductions for accumulation。 | 目标是 PCD/IVC accumulation，而不是单次 proximity testing。 | 需要 Arc 的 IOR/noninteractive-reduction/Merkle wrapper；不是普通 FRI 自动具备的性质。 | [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | paper | 作为 FRI IOPP source extension，给出 FRI/batched FRI construction overview，并证明 opening-consistency 可支撑 DAS erasure-code commitments | 不是 FRI 原始论文；foundation 仍需 BBHR18/DEEP-FRI/STARK sources | `§4`, `Appendix C` |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]] | paper | 作为 adjacent source extension：将 RS proximity/list-decoding/quotient tools 迁移到 hash-based accumulation schemes | 不是 FRI 原始论文；不是 DAS/PCS source；Arc-specific IOR machinery stays in source note | `§2.1`, `§3.2`, `§6`, `§7` |

## 正反例约束

- 正确: 把 FRIDA 作为 “FRI IOPPs 可服务 DAS” 的 bridge evidence。
- 正确: 将 FRI 的 folding/query/Merkle pattern 与 DAS 的 light-client/network/extraction assumptions 分开。
- 正确: 若问 “FRIDA 具体参数/效率表”，转到 source note。
- 错误: 把 FRI IOPPs 直接等同于 polynomial commitments；FRIDA 明确说直接用 FRI as polynomial commitment 会有额外 opening overhead。
- 错误: 用 FRIDA 替代原始 FRI/STARK foundation。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-20`，仅覆盖当前 vault 已深读 FRIDA。
- Freshness: `fresh` for current-vault seed; not an external latest claim.
- Valid until: `2026-07-20`。
- 综合: 当前节点由 FRIDA 和 Arc 两个相邻 source seed 支撑。FRIDA 说明 FRI 的核心可迁移价值不只是 “transparent proximity proof”，还包括在额外 opening-consistency 条件下为 erasure-code commitments 提供 code-binding。Arc 则说明 RS proximity/list-decoding/quotienting 不只服务 proof-system proximity testing，也可以成为 hash-based accumulation 的核心 primitive。对 Nahida 来说，FRI IOPPs 现在应作为 [[proof-systems|Proof systems]] 下的 method-family seed，并通过两个桥分别连接到 DAS 与 accumulation。

## 领域态势

- Research dynamics note: not_applicable
- Academic focus summary: current-vault-only; 原始 FRI、DEEP-FRI、STARK 和 transparent PCS sources 缺失。
- Industrial focus summary: implementation/repo/standard evidence 未吸收。
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: original FRI/DEEP-FRI/STARK/PCS source absorption, or source that compares FRI/KZG/IPA in DA systems.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | 创建 FRI IOPPs method-family seed；补充 opening-consistency、batched FRI 和 DAS bridge | 定义; 方法族与解决路线; 当前综合; Bridge Links | yes | 吸收原始 FRI/DEEP-FRI/STARK/transparent PCS sources 后校准 |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]] | 新增 FRI/IOPP-to-accumulation adjacent bridge；补充 RS proximity accumulation transfer | 背景; 方法族与解决路线; 当前综合; Bridge Links | yes | 吸收 FRI/STIR/BMNW24/Protostar sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] | `zero-knowledge-proofs/proof-systems/fri-iopps; blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | method_transfer, application, dependency, transparent_commitment_route | FRI 的 proximity/opening-consistency machinery 可迁移到 DAS commitment/opening layer；blockchain data availability 的 network sampling、data recovery 和 validity boundary 不自动迁移。 | active_seed |
| [[fri-iopps-to-accumulation-schemes|FRI IOPPs -> accumulation schemes]] | `zero-knowledge-proofs/proof-systems/fri-iopps; zero-knowledge-proofs/recursion-and-folding/accumulation-schemes` | method_transfer, dependency, shared_pattern, formalization_bridge | RS proximity/list-decoding/quotienting 可迁移到 Arc-style accumulation；普通 FRI/DAS/PCS 语义不自动迁移。 | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-fri-iopps | is_a | nahida-knowledge-proof-systems | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/fri-iopps.md; vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md | high | active_seed |
| nahida-knowledge-fri-iopps | evidenced_by | vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md | FRIDA source note | high | active_seed |
| nahida-knowledge-fri-iopps | bridges_to | nahida-bridge-fri-iopps-to-data-availability-sampling | bridge note | high | active_seed |
| nahida-knowledge-fri-iopps | evidenced_by | vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md | Arc source note | high | active_seed |
| nahida-knowledge-fri-iopps | bridges_to | nahida-bridge-fri-iopps-to-accumulation-schemes | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Original FRI paper (BBHR18) 未吸收。 | 当前 FRI foundation 只来自 FRIDA/Arc 的 recall/extension。 | nahida-update or nahida-research-search | high | queued |
| DEEP-FRI / STARK / transparent SNARK sources 未吸收。 | 影响 FRI IOPPs 在 ZKP 方向的完整定位。 | nahida-update | medium | queued |
| FRI vs KZG vs IPA commitment comparison 缺 primary source。 | 影响 polynomial commitments 与 DA route 比较。 | nahida-research-search | medium | queued |
| Implementation/repo evidence 缺。 | 影响工程可用性判断。 | nahida-github-repo-analyze | low | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-frida-data-availability-from-fri | Created FRI IOPPs method-family seed from FRIDA deep read and linked it to DAS through a bridge. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-arc-accumulation-reed-solomon | Added RS proximity accumulation transfer and bridge from FRI IOPPs to accumulation schemes. | 1 source note | codex |
