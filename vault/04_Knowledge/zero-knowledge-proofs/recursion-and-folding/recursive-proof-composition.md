---
id: "nahida-knowledge-recursive-proof-composition"
title: "Recursive proof composition"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "recursive-proof-composition"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
parent_knowledge_refs:
  - "nahida-knowledge-recursion-and-folding"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "recursive-proof-composition"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition"
secondary_ontology_paths:
  - "verifiable-computation/incrementally-verifiable-computation"
  - "verifiable-computation/interactive-proofs"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/recursion-and-folding/accumulation-schemes"
relation_edges:
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "is_a"
    to: "nahida-knowledge-recursion-and-folding"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "depends_on"
    to: "nahida-knowledge-polynomial-commitments"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
      - "vault/05_Bridges/polynomial-commitments-to-recursive-proof-composition.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "bridges_to"
    to: "nahida-bridge-polynomial-commitments-to-recursive-proof-composition"
    evidence_refs:
      - "vault/05_Bridges/polynomial-commitments-to-recursive-proof-composition.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "depends_on"
    to: "nahida-knowledge-interactive-proofs"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
      - "vault/05_Bridges/public-coin-interactive-proofs-to-recursive-proof-composition.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "bridges_to"
    to: "nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition"
    evidence_refs:
      - "vault/05_Bridges/public-coin-interactive-proofs-to-recursive-proof-composition.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "depends_on"
    to: "nahida-knowledge-accumulation-schemes"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/accumulation-schemes.md"
      - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursive-proof-composition"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-polynomial-commitments-to-recursive-proof-composition"
  - "nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
  - "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
  - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
representative_source_refs:
  - "iacr:2019/1021"
  - "sha256:6814cb0cb866cdfe3af135c0edf4626a266b92e916edef9132c3912f7decbe0e"
  - "iacr:2022/1072"
  - "sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
query_keys:
  - "Recursive proof composition"
  - "recursive-proof-composition"
  - "recursive proofs"
  - "proofs that verify proofs"
  - "incrementally verifiable computation"
  - "IVC"
  - "Halo"
  - "nested amortization"
  - "public-coin proof recursion"
  - "GKR inside SNARK"
  - "recursive hash verification"
  - "short Fiat-Shamir input"
  - "accumulation schemes"
  - "proof-carrying data accumulation"
  - "hash-based accumulation"
  - "ARC"
aliases:
  - "recursive proofs"
  - "proofs that verify proofs"
  - "proof-carrying data"
  - "incrementally verifiable computation"
  - "IVC"
  - "PCD accumulation"
  - "accumulation schemes"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "recursive-proof-composition"
  - "incrementally-verifiable-computation"
  - "nested-amortization"
  - "public-coin-proof-recursion"
  - "hash-verification"
  - "GKR"
  - "accumulation-schemes"
  - "proof-carrying-data"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-22"
evidence_window_end: "2026-06-22"
created: "2026-06-22"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-halo-recursive-proof-composition"
  - "nahida-knowledge-20260622-public-coin-proof-recursion"
  - "nahida-knowledge-20260623-arc-accumulation-reed-solomon"
source_refs:
  - "iacr:2019/1021"
  - "sha256:6814cb0cb866cdfe3af135c0edf4626a266b92e916edef9132c3912f7decbe0e"
  - "iacr:2022/1072"
  - "sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
confidence: "high"
trust_tier: "primary"
---

# Recursive proof composition

## 定义与范围

- 定义: Recursive proof composition 研究让一个 proof 可行地证明另一个同类 proof 的正确性，从而把长计算链、状态转移链或 proof tree 压缩成可递归扩展的证明状态。
- 不包含: 单篇论文、某个曲线 cycle、某个 protocol instance 或某次 benchmark；这些留在 `03_Sources` source note。
- Canonical terms: `recursive-proof-composition`
- Aliases/query keys: recursive proofs, proofs that verify proofs, IVC, proof-carrying data
- Standalone completeness check: 本节点给出本地定义、问题、方法族、source extension、bridge 和边界；链接用于深入，不作为唯一解释。
- Retrieval role: 当查询“递归证明、Halo、IVC、证明验证证明”时，先从这里理解问题层，再进入 source note。
- Update scope: 新 source 若改变递归验证成本、可信设置边界、累积/折叠路线、curve/setup assumptions 或应用场景，应刷新本节点。

## 背景

递归证明组合的直接动机是 incrementally verifiable computation: verifier 不希望重新执行所有历史计算，也不希望逐个验证所有历史 proofs。递归组合让最新 proof 递归证明前一个 proof 与当前 step 的正确性，因此最终 verifier 只检查当前 proof 和少量状态。

Halo 当前提供本节点的主 seed: 传统路线需要 fully succinct proof system 和 pairing-friendly curve cycles；Halo 改为把内积型多项式承诺的线性验证操作作为 deferred verifier state，通过 nested amortization 折叠到最终 verifier 的一次线性检查中，从而避开 trusted setup 和 pairing-friendly cycle 约束。
这篇 public-coin recursion source 补上另一条路线: 不再只递归同类 proof 或摊销 PCS verifier work，而是让 GKR 这样的 public-coin argument 证明批量哈希计算，再把 GKR verifier 嵌入外层 SNARK。关键难点是 Fiat-Shamir transcript 不能在电路里变成巨大哈希，因此它利用外层 SNARK verifier 的 public-input computation 生成短绑定值。
Arc 补上 accumulation-based PCD/IVC 路线: 它不从 PCS verifier-state deferral 或 public-coin verifier embedding 入手，而是构造 hash-based、RS proximity、distance-preserving 的 accumulator relation，让 PCD/IVC 可以在不依赖 homomorphic vector commitments 的情况下维护无界历史。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它组织多种递归证明路线，包括 nested amortization、folding schemes、recursive proof compression 和未来 PCD/accumulation sources，而不是复述 Halo。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Halo 只是代表 source；Tweedledum/Tweedledee、Rescue、具体 proof size 留在 source note。
- 需要引用的更基础 Knowledge: [[recursion-and-folding|Recursion and folding]]、[[polynomial-commitments|Polynomial commitments]]。
- 不应拆出的实例/协议/来源: Halo、Nova、zkBridge、SnarkFold 默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

递归组合要解决的是“proof verifier 能否被另一个 proof 的电路/关系高效表达”。主要瓶颈包括:

- verifier circuit 比被验证计算还大，导致递归无法收敛；
- proof system 需要 trusted setup 或 pairing-friendly curve cycle；
- verifier 仍有线性时间操作，不能直接嵌入每一层递归；
- 每步递归产生的 verifier obligations 会累积失控。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[recursion-and-folding|Recursion and folding]] | child_of | Halo source note and existing direction node | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前只有 Halo primary seed；等 Halo 2/Nova-family/accumulation/PCD sources 增多后再拆子节点 | existing vault evidence | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| fully succinct recursive verifier | 构造一个 verifier circuit 小于被验证计算的 proof system，让 proof 直接验证前一层 proof。 | proof system 的 verifier 足够小，且底层 field/curve 可互相高效表达。 | pairing-friendly cycles 稀缺；传统 pairing SNARK 还有 trusted setup。 | Halo intro as prior-work contrast |
| nested amortization | 递归电路只检查 logarithmic marginal verifier work，把线性 commitment-opening check 作为 public verifier state 递延；多层递归通过 amortization 折叠，最终 verifier 只做一次线性检查。 | expensive verifier operation 可表示为可递延状态，且有 sound amortization argument 可批量检查。 | final verifier 仍是线性时间；依赖 random oracle、DLOG、曲线 cycle 和具体 PCS 结构。 | [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Halo]] |
| public-coin argument verifier recursion | 用 GKR 等 public-coin argument 证明 bulk computation，再在外层 SNARK 电路里验证 public-coin verifier；Fiat-Shamir challenge 绑定到 SNARK verifier computation 的短值。 | bulk computation 适合 public-coin argument，且外层 SNARK verifier 可拆成 statement-binding computation step。 | 具体 GKR+SNARK instantiation 仍是 heuristic；不适用于任意 IP/SNARK；需要防止 statement mix-and-match。 | [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Public-coin recursion for hash verification]] |
| folding-based IVC | 把多个约束实例折叠成一个同型 running instance，避免每步递归验证完整 SNARK。 | computation 可表示为可折叠 relation，例如 relaxed R1CS。 | folding 本身不等于 final succinct ZK proof；通常还需要 compression proof 或 commitment backend。 | [[folding-schemes|Folding schemes]]; [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova]] |
| accumulation-based PCD/IVC | 把多个 claims/proofs/accumulators 合成一个 running accumulator，再让最终 decider 检查 accumulated state。 | 存在 sound many-to-one reduction 和 succinct accumulator verifier/decider。 | 具体路线受承诺后端、随机预言机、code/list-decoding assumptions 约束；Arc 是 RS-specific hash route。 | [[accumulation-schemes|Accumulation schemes]]; [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] |
| application-level recursive proof compression | 用一个链上/外部 verifier 友好的 proof 证明另一个更大 proof 的 verification circuit。 | 大 proof 直接验证成本过高，但 verification circuit 可被外层 proof system 承载。 | 增加外层 prover cost；应用语义、链上 liveness 和 state assumptions 不由 proof recursion 自动解决。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Recursive Proof Composition without a Trusted Setup]] | paper | 主 seed: nested amortization + IPA-style polynomial commitment enables practical recursive proof composition without trusted setup | final verifier remains linear; Fiat-Shamir/random oracle; DLOG over normal elliptic-curve cycles; Tweedledum/Tweedledee implementation-specific | `Abstract`, `§3`, `§4`, `§6`, `§7` |
| [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification]] | paper | 新增 route: public-coin verifier recursion for faster SNARK-friendly hash verification; embeds GKR verifier in outer SNARK with short Fiat-Shamir inputs | general compiler is ROM-secure under assumptions; concrete GKR instantiation is heuristic after one-round conversion | `Abstract`, `§4-§6`, `Appendix H-I` |
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova: Recursive Zero-Knowledge Arguments from Folding Schemes]] | paper | 相邻 route: folding schemes for IVC reduce per-step recursive proof overhead | folding route, not Halo-style nested amortization | existing source note |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | paper | application signal: recursive proof compression can make large verification chains on-chain friendly | application source, not foundation for recursive proof composition | existing source note |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]] | paper | accumulation route: hash-based RS proximity accumulation supports unbounded PCD/IVC without homomorphic vector commitments | ROM/Merkle/list-decoding assumptions; no implementation benchmark; Arc details stay in source note | `Abstract`, `§1-§2`, `§6-§7`, `Appendix A-B` |

## 正反例约束

- 正确: “Halo 用 nested amortization 把线性 verification obligation 推迟到最终 verifier”，这是本节点可吸收的通用路线。
- 正确: “Nova 用 folding schemes 做 IVC”，是同一上层方向里的不同路线。
- 错误: “Halo 是 folding scheme”，除非有后续 source 直接建立这个等价。
- 错误: “递归证明组合一定需要 fully succinct verifier”，Halo 的贡献正是绕开这个常规要求。
- 错误: “避免 trusted setup 是所有 zk-SNARK 的性质”，该性质只随具体 proof/commitment construction 成立。

## 当前综合

- Evidence window: `2026-06-22` to `2026-06-22`，主 evidence 为 Halo source note，并利用 vault 既有 Nova/zkBridge notes 作相邻路线定位。
- Freshness: `fresh` for local vault absorption; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: Recursive proof composition 是 `recursion-and-folding` 下比 `folding-schemes` 更上层/相邻的问题节点。Halo 说明递归证明不必只通过 fully succinct pairing SNARK 或 Nova-style folding 来实现；当 verifier 的昂贵线性工作能被承诺/摊销为 deferred state 时，nested amortization 可以让递归电路保持小，而最终 verifier 只在链尾检查一次累计状态。Public-coin recursion source 补上另一类路线：让 GKR 等 public-coin argument 承担 bulk computation，并把其 verifier 嵌入外层 SNARK；递归难点从 PCS 线性检查转为 statement binding 与 short-input Fiat-Shamir。Arc 再补上 accumulation-based PCD/IVC route：递归难点转为如何保持 accumulator distance/soundness 不随步骤退化，核心依赖 RS proximity、Merkle commitments、IOR formalism 和 list-decoding/out-of-domain binding。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Recursive Proof Composition without a Trusted Setup]] | primary seed | 新建本 problem node；新增 nested amortization route；新增 PCS bridge | yes | 后续吸收 Halo 2 / accumulation / public-coin recursion sources 时比较路线边界 |
| [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification]] | source extension + bridge | 新增 public-coin verifier recursion route；用 GKR proof 承载批量哈希计算，并通过外层 SNARK verifier computation 缩短 Fiat-Shamir 输入 | yes | 后续与 Arc/accumulation/Halo2 比较 transcript binding 与安全模型 |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]] | source extension + child dependency | 新增 accumulation-based PCD/IVC route；用 hash-based RS proximity accumulation 支撑 unbounded recursive/PCD history | yes | 后续与 BMNW24/Protostar/ProtoGalaxy/FRI sources 比较 depth、commitment backend 与安全模型 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[polynomial-commitments-to-recursive-proof-composition|Polynomial commitments -> recursive proof composition]] | `zero-knowledge-proofs/polynomial-commitments; zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | dependency, method_transfer, verification_deferral, performance_compression | 可迁移的是“amortized commitment opening can defer verifier work”的模式；不能推出任意 PCS 或任意 curve 都支持 Halo recursion。 | active_seed |
| [[public-coin-interactive-proofs-to-recursive-proof-composition|Public-coin interactive proofs -> recursive proof composition]] | `verifiable-computation/interactive-proofs; zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | method_transfer, dependency, verification_embedding, fiat_shamir_boundary, performance_compression | 可迁移的是 public-coin verifier embedding + short-input Fiat-Shamir pattern；不能推出任意 interactive proof 或任意 SNARK 都可低成本递归。 | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-recursive-proof-composition | is_a | nahida-knowledge-recursion-and-folding | this node and parent direction | high | active_seed |
| nahida-knowledge-recursive-proof-composition | evidenced_by | vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md | Halo source note | high | active_seed |
| nahida-knowledge-recursive-proof-composition | depends_on | nahida-knowledge-polynomial-commitments | Halo §3-§4; bridge note | high | active_seed |
| nahida-knowledge-recursive-proof-composition | bridges_to | nahida-bridge-polynomial-commitments-to-recursive-proof-composition | bridge note | high | active_seed |
| nahida-knowledge-recursive-proof-composition | evidenced_by | vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md | public-coin recursion source note | high | active_seed |
| nahida-knowledge-recursive-proof-composition | depends_on | nahida-knowledge-interactive-proofs | source `§3-§6`; bridge note | high | active_seed |
| nahida-knowledge-recursive-proof-composition | bridges_to | nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition | bridge note | high | active_seed |
| nahida-knowledge-recursive-proof-composition | depends_on | nahida-knowledge-accumulation-schemes | accumulation-schemes node; Arc source note | high | active_seed |
| nahida-knowledge-recursive-proof-composition | evidenced_by | vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md | Arc source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Additional Halo 2 / accumulation / public-coin recursion comparison sources still thin. | Needed to compare nested amortization, public-coin verifier embedding, Arc-style accumulation and later practical recursive proof systems without overgeneralizing current sources. | nahida-update / nahida-research-search | high | queued |
| PCD and proof-carrying data foundation sources absent. | Recursive proof composition is closely related to proof-carrying data, but current vault only has source-note mentions. | nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-halo-recursive-proof-composition | Created problem node from Halo source; added nested amortization route and PCS bridge. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-public-coin-proof-recursion | Added public-coin argument verifier recursion route and bridge from interactive proofs/GKR to recursive proof composition. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-arc-accumulation-reed-solomon | Added accumulation-based PCD/IVC route from Arc and linked recursive composition to accumulation schemes. | 1 source note | codex |
