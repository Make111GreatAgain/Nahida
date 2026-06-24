---
id: "nahida-knowledge-floating-point-snarks"
title: "Floating-point SNARKs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "method_family"
hierarchy_level: "problem"
file_slug: "floating-point-snarks"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "floating-point-snarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/floating-point-snarks"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/privacy-preserving-location-proofs"
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
relation_edges:
  - from: "nahida-knowledge-floating-point-snarks"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/floating-point-snarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-floating-point-snarks"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-floating-point-snarks"
    relation: "applies_to"
    to: "nahida-knowledge-privacy-preserving-location-proofs"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
      - "vault/05_Bridges/floating-point-snarks-to-privacy-preserving-location-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-floating-point-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-floating-point-snarks"
    relation: "depends_on"
    to: "nahida-knowledge-commit-and-prove-arguments"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/commit-and-prove-arguments.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-floating-point-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-floating-point-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs"
    evidence_refs:
      - "vault/05_Bridges/floating-point-snarks-to-privacy-preserving-location-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-floating-point-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks"
    evidence_refs:
      - "vault/05_Bridges/commit-and-prove-arguments-to-floating-point-snarks.md"
      - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs"
  - "nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
  - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
representative_source_refs:
  - "arxiv:2404.14983v2"
  - "doi:10.1145/3548606.3560653"
query_keys:
  - "Floating-point SNARKs"
  - "IEEE 754 SNARK circuits"
  - "floating-point ZKP"
  - "accurate floating-point proofs"
  - "SNARK floating-point arithmetic"
  - "TestFloat ZKP"
  - "relative-error floating-point ZK"
  - "succinct ZK for floating point"
  - "floating-point commit-and-prove compiler"
aliases:
  - "IEEE 754 SNARK circuits"
  - "floating-point ZK circuits"
  - "accurate floating-point SNARKs"
  - "relative-error floating-point proofs"
domains:
  - "zero-knowledge-proofs"
topics:
  - "floating-point-snarks"
  - "proof-systems"
  - "ieee-754"
  - "relative-error-model"
  - "commit-and-prove"
  - "lookup-arguments"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zklp-floating-point-snarks"
  - "nahida-knowledge-20260623-succinct-zk-floating-point"
source_refs:
  - "arxiv:2404.14983v2"
  - "doi:10.1145/3548606.3560653"
confidence: "medium"
trust_tier: "primary"
---

# Floating-point SNARKs

## 定义与范围

- 定义: Floating-point SNARKs 研究如何在 SNARK/ZKP 中准确或近似地表示、验证 floating-point arithmetic。当前 vault 记录两条路线: 一条追求 IEEE 754 语义、rounding、subnormal、NaN、infinity 和 signed zero 等边界的 exact/compliance route；另一条用 numerical analysis 启发的 relative-error model 证明每个浮点 gate 的近似正确性，以降低 prover overhead。
- 不包含: 单个应用电路、某次 benchmark、某个 proof backend、某个地理库或 ML 模型本身。ZKLP 是代表 source；本节点关注可迁移的数值电路方法族。
- Canonical terms: `floating-point-snarks`, `IEEE 754 SNARK circuits`
- Aliases/query keys: floating-point ZKP, accurate floating-point proofs, SNARK floating-point arithmetic
- Standalone completeness check: 本节点本地解释问题、方法路线、适用条件、代表 source、bridge 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“SNARK 怎么支持浮点数”“为什么 fixed-point 不够”“IEEE 754 ZKP circuit 怎么做”“relative-error floating-point ZK 是什么”时先读本节点。
- Update scope: 新 source 若提出 floating-point ZKP/MPC/SNARK circuits、IEEE 754 compliant proof systems、numeric soundness for ZKML/geospatial/scientific computing，应刷新本节点。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

多数 SNARK 约束系统原生处理 finite field arithmetic，但真实软件常使用 floating-point。把 floating-point 程序简单替换成 fixed-point 会引入范围、精度、rounding 和 compatibility 问题。对于地理、ML、科学计算等应用，微小的舍入差异可能造成不同输出，进而影响 proof completeness，甚至让 adversary 利用不一致构造错误 statement。

当前 vault 有两类 primary source: ZKLP 给出 IEEE 754 compliant FP32/FP64 primitive operation circuits，并用 location proof 展示 exact semantics 的必要性；Garg et al. CCS 2022 则提出 relative-error model，不证明每一步 exact IEEE rounding，而证明每个 gate 的相对误差上界，并通过 commit-and-prove compiler 和 batch range proof 降低 prover cost。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family`
- 为什么足够通用: 它不等于 ZKLP 或 Garg et al.。它组织 IEEE 754 representation、rounding、subnormal/NaN/infinity handling、relative-error verification、lookup/range checks、commit-and-prove compiler、floating-point primitive operations 和应用迁移。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: ZKLP 是当前代表 source；本节点表达“浮点数值语义如何进入 SNARK”这一类可复用 proof-system engineering 问题。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[zk-snarks|zk-SNARKs]], [[commit-and-prove-arguments|Commit-and-prove arguments]]。
- 不应拆出的实例/协议/来源: `CFpInit`, `CFpRound`, Berkeley TestFloat, gnark implementation 默认保留在 source note；除非多来源证明需要独立 primitive node。

## 解决的问题

Floating-point SNARKs 解决的是 numeric semantics gap:

- finite-field circuits 不天然支持 IEEE 754 exponent/mantissa/sign 结构。
- comparison、shift、range check、rounding、division、sqrt、NaN/subnormal 等操作 circuit-unfriendly。
- fixed-point 可能不能同时表达大/小数值范围，或与现有软件库输出不一致。
- 应用需要证明“和真实软件相同的 floating-point 结果”，而不是仅证明某个近似算术关系。
- 另一类应用只需要数值分析意义上的 bounded relative error，而不需要 exact IEEE rounding；此时 exact binary-circuit route 可能造成过高 prover overhead。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of / method_family | ZKLP source absorption | active_seed |
| [[zk-snarks|zk-SNARKs]] | depends_on | ZKLP instantiates Groth16/Plonk and floating-point circuits | active_seed |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | depends_on / compiler_backend | Garg et al. compile public-coin CP systems for R1CS into floating-point ZK proofs | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| IEEE 754 primitive circuits | route section | ZKLP source covers init/round/add/mul/div/sqrt/compare | ZKLP §3 | active_seed |
| Relative-error floating-point proofs | route section | Garg et al. source covers approximate correctness, CP compiler, and batch range proofs | Garg et al. §2-§6 | active_seed |
| Batch range proofs without bit decomposition | candidate method family | Garg et al. gives one strong source, but more independent uses are needed before splitting | Garg et al. §2.2/§3 | watching |
| numeric soundness for application circuits | candidate problem | precision mismatch affects location proof and future ML proofs | ZKLP §1/§5/§7 | review |
| floating-point ZKML | candidate application | 论文提到 future adaptation, but no primary source yet | ZKLP discussion only | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Circuit-efficient FP representation | 把 IEEE 754 `(sign, exponent, mantissa)` 转成 `(s,e,m,a)`，显式 leading bit、归一化 subnormal，并标记 abnormal。 | 需要在 finite field 中模拟 FP32/FP64。 | 必须完整处理 NaN、infinity、signed zero 和 subnormal。 | [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]] |
| Correct rounding | 实现 round half to even，并处理 subnormal 的有效 precision。 | 应用需要与 IEEE 754 software/hardware 对齐。 | Rounding 是主要复杂度来源之一。 | ZKLP §3.2 |
| Relative-error approximate correctness | 对每个 addition/subtraction/multiplication gate 证明 `|c-f(a,b)| < delta |f(a,b)|`，用数值分析中的 relative error bound 替代 exact rounding proof。 | ML/scientific computing 等可用 numerical analysis 解释 output accuracy，且不要求 exact IEEE per-step rounding。 | 不适合 finance/accounting 等 precise rounding critical 场景；completeness/soundness 有 real-vs-floating 表示 gap。 | [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Garg et al. 2022]] |
| Commit-and-prove compiler route | 从 public-coin commit-and-prove ZKPoK for R1CS 编译出 floating-point ZK proof；R1CS size 约 `O(log w + k) * |C|`。 | 底层 proof system 可抽象为 CP system，relation 可编译到 R1CS。 | 依赖底层 CP 系统；正文把若干安全证明和 instantiation 推迟到 full version；ZK 版本约 2x proof size。 | Garg et al. §2.2, §6 |
| Batch range proof without bit decomposition | 把 relative-error inequality 转为 positivity/range proof，使用 Legendre three-square theorem 与 small random linear combinations，在 prime known-order groups 中避免逐位分解。 | 需要证明 batch range constraints 且希望降低 bit-decomposition overhead。 | soundness argument 技术复杂；sublinear verification route 会增加 prover cost。 | Garg et al. §3, §6.1, §6.7 |
| Lookup-assisted integer operations | 用 lookup tables 做 range checks、powers of two 和 shifts，降低 bit decomposition 成本。 | SNARK backend 支持或可组合 lookup argument。 | lookup identity 可能仍在 circuit 中带来 amortized overhead。 | ZKLP §2.5, Appendix A |
| Nondeterministic hints | division, sqrt, MSB/LSB/trig-derived values 等由 prover 提供，circuit 验证 predicate。 | 计算难但验证便宜。 | predicate 必须足够强；hint 不可被直接信任。 | ZKLP §2.5, §3.5 |
| Application-specific trig elimination | 用恒等式和可验证 hints 避免直接逼近 sin/cos/tan。 | geospatial 或其他函数可代数改写。 | 不是通用三角函数 SNARK；只对特定 transform 有效。 | ZKLP §4 |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | paper | 创建本方法节点；提出 IEEE 754 compliant floating-point SNARK primitive circuits，并用 TestFloat/BN254/Groth16/Plonk 评估 | "first" novelty claim 按论文自述；implementation URL 未联网验证；benchmark 是 gnark-specific | `p1-p19` |
| [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct Zero Knowledge for Floating Point Computations]] | paper | 补充 relative-error floating-point proof route；提出从 CP/R1CS systems 到 floating-point ZK 的 generic compiler 和无 bit decomposition 的 batch range proof | 不证明 exact IEEE rounding；ZK 版本 proof size 约 2x；full security proofs/instantiations 在 full version；不是 zkML inference source | `p1-p14` |

## 正反例约束

- 正确: 把 floating-point SNARKs 作为 proof-system engineering method family。
- 正确: 把 ZKLP 的位置隐私应用通过 bridge 连接到本方法。
- 正确: 区分 IEEE 754 exact/compliance route 与 relative-error approximate route。
- 正确: 把 fixed-point vs floating-point 视为 numeric soundness/completeness 问题。
- 错误: 把 floating-point SNARKs 当作 zk-SNARK foundation 本身；它是 circuit arithmetic layer。
- 错误: 仅因为论文提到 ML/scientific computing motivation 就把该 source 主分类为 zkML/verifiable inference。
- 错误: 把 relative-error route 说成完全替代 IEEE 754 exact route；finance/accounting 等场景可能仍需要 precise rounding。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，覆盖当前 vault 已深读 ZKLP 与 Garg et al. CCS 2022。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: 当前节点是 foundation_thin seed，但 taxonomy 已从单一 IEEE-compliant circuit route 扩展为两条路线。ZKLP 显示 floating-point 在 SNARK 中不是简单 bit packing 问题，而是 IEEE 754 semantics preservation 问题；lookup arguments 和 nondeterministic predicates 能把 range checks、rounding、division、sqrt 等 circuit-unfriendly operations 降到可用规模。Garg et al. 显示另一种 proof-system 取舍: 放弃 exact per-step IEEE rounding，转而证明 numerical-analysis 风格的 relative error bound，并通过 CP compiler 和 batch range proof 把 prover overhead 大幅降下来。两条路线服务不同需求，不能互相覆盖。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | 创建 floating-point SNARKs 方法节点；补充 IEEE 754 circuits、lookup/hints、TestFloat/evaluation evidence | 定义; 方法族与解决路线; 代表 Sources; Bridge Links | yes | 吸收 Succinct ZK for floating point / Mystique / ZKML floating-point sources 后校准 |
| [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct Zero Knowledge for Floating Point Computations]] | 补充 relative-error approximate correctness route；把 CP compiler 和 batch range proof 纳入 floating-point SNARK taxonomy；纠正其不属于 zkML inference primary path | 定义; 背景; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 exact IEEE prior / ZKML floating-point primary sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[floating-point-snarks-to-privacy-preserving-location-proofs|Floating-point SNARKs -> privacy-preserving location proofs]] | `zero-knowledge-proofs/proof-systems/floating-point-snarks; zero-knowledge-proofs/applications/privacy-preserving-location-proofs` | application, method_transfer, numerical_soundness, dependency | IEEE 754 arithmetic transfers to geospatial proof accuracy; location provenance and application policy do not. | active_seed |
| [[commit-and-prove-arguments-to-floating-point-snarks|Commit-and-prove arguments -> Floating-point SNARKs]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; zero-knowledge-proofs/proof-systems/floating-point-snarks` | dependency, compiler_backend, method_transfer | CP/R1CS backend abstraction transfers to relative-error floating-point proofs; exact IEEE semantics, application-level accuracy and backend-specific efficiency do not. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-floating-point-snarks | is_a | nahida-knowledge-proof-systems | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/floating-point-snarks.md | high | active_seed |
| nahida-knowledge-floating-point-snarks | depends_on | nahida-knowledge-zk-snarks | ZKLP uses Groth16/Plonk SNARK backends | medium | active_seed |
| nahida-knowledge-floating-point-snarks | applies_to | nahida-knowledge-privacy-preserving-location-proofs | ZKLP §4-§5 | high | active_seed |
| nahida-knowledge-floating-point-snarks | evidenced_by | vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md | full source note | high | active_seed |
| nahida-knowledge-floating-point-snarks | bridges_to | nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs | bridge note | high | active_seed |
| nahida-knowledge-floating-point-snarks | depends_on | nahida-knowledge-commit-and-prove-arguments | Garg et al. §2.2/§6 | high | active_seed |
| nahida-knowledge-floating-point-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md | full source note | high | active_seed |
| nahida-knowledge-floating-point-snarks | bridges_to | nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Floating-point ZKP prior sources 未吸收。 | 需要校准 novelty 和与 Garg et al./Mystique/secure MPC 的边界。 | nahida-research-search or nahida-update | high | queued |
| ZKML floating-point primary sources 缺。 | 不能仅凭 ZKLP discussion 声称 ML 适用性。 | nahida-update | medium | queued |
| Backend-agnostic lookup/capability comparison 缺。 | gnark/LogUp 实验不能直接推广到所有 proof systems。 | nahida-research-search | medium | queued |
| Exact rounding vs approximate correctness taxonomy 仍薄。 | ZKLP 和 Garg et al. 提供两端 seed，但需要更多 exact IEEE / relative-error / MPC floating-point sources 稳定边界。 | nahida-update / nahida-research-search | high | active_seed_gap |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zklp-floating-point-snarks | Created floating-point SNARKs method-family node from ZKLP source absorption. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-succinct-zk-floating-point | Added relative-error floating-point proof route and CP compiler bridge from Garg et al. CCS 2022. | 1 source note | codex |
