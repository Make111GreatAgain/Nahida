---
id: "nahida-knowledge-recursion-and-folding"
title: "Recursion and folding"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "recursion-and-folding"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
parent_knowledge_refs:
  - "nahida-knowledge-zero-knowledge-proofs"
child_knowledge_refs:
  - "nahida-knowledge-folding-schemes"
  - "nahida-knowledge-snark-proof-aggregation"
  - "nahida-knowledge-recursive-proof-composition"
  - "nahida-knowledge-accumulation-schemes"
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "is_a"
    to: "nahida-knowledge-zero-knowledge-proofs"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md"
      - "vault/04_Knowledge/zero-knowledge-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "has_child"
    to: "nahida-knowledge-folding-schemes"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "has_child"
    to: "nahida-knowledge-snark-proof-aggregation"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation.md"
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "has_child"
    to: "nahida-knowledge-recursive-proof-composition"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition.md"
      - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "bridges_to"
    to: "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
    evidence_refs:
      - "vault/05_Bridges/folding-schemes-to-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "bridges_to"
    to: "nahida-bridge-folding-schemes-to-memory-efficient-snarks"
    evidence_refs:
      - "vault/05_Bridges/folding-schemes-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "bridges_to"
    to: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
    evidence_refs:
      - "vault/05_Bridges/split-prover-zksnarks-to-recursion-and-folding.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "bridges_to"
    to: "nahida-bridge-polynomial-commitments-to-recursive-proof-composition"
    evidence_refs:
      - "vault/05_Bridges/polynomial-commitments-to-recursive-proof-composition.md"
      - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "bridges_to"
    to: "nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition"
    evidence_refs:
      - "vault/05_Bridges/public-coin-interactive-proofs-to-recursive-proof-composition.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "has_child"
    to: "nahida-knowledge-accumulation-schemes"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/accumulation-schemes.md"
      - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-recursion-and-folding"
    relation: "bridges_to"
    to: "nahida-bridge-fri-iopps-to-accumulation-schemes"
    evidence_refs:
      - "vault/05_Bridges/fri-iopps-to-accumulation-schemes.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-folding-schemes-to-snark-proof-aggregation"
  - "nahida-bridge-folding-schemes-to-memory-efficient-snarks"
  - "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
  - "nahida-bridge-polynomial-commitments-to-recursive-proof-composition"
  - "nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition"
  - "nahida-bridge-fri-iopps-to-accumulation-schemes"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md"
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
  - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
  - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
  - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
  - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
  - "vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md"
  - "vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md"
representative_source_refs:
  - "iacr:2021/370"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
  - "iacr:2019/1021"
  - "iacr:2022/1072"
  - "sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
query_keys:
  - "Recursion and folding"
  - "recursion-and-folding"
  - "recursive proofs"
  - "folding schemes"
  - "recursive proof compression"
  - "SNARK proof aggregation"
  - "split IVC"
  - "commit-and-fold"
  - "folding-based SNARKs"
  - "memory-efficient SNARKs"
  - "split prover zkSNARKs"
  - "split prover vs IVC"
  - "recursive proof composition"
  - "Halo"
  - "nested amortization"
  - "public-coin proof recursion"
  - "GKR inside SNARK"
  - "recursive hash verification"
  - "accumulation schemes"
  - "hash-based accumulation"
  - "Reed-Solomon proximity accumulation"
  - "ARC"
  - "proof-carrying data accumulation"
aliases:
  - "recursive proofs"
  - "folding schemes"
  - "recursive proof compression"
  - "SNARK proof aggregation"
  - "split IVC"
  - "folding-based SNARKs"
  - "recursive proof composition"
  - "nested amortization"
  - "accumulation schemes"
  - "hash-based accumulation"
  - "RS proximity accumulation"
domains:
  - "zero-knowledge-proofs"
topics:
  - "recursion-and-folding"
  - "recursive-proof-compression"
  - "snark-proof-aggregation"
  - "memory-efficient-snarks"
  - "split-prover-zksnarks"
  - "recursive-proof-composition"
  - "nested-amortization"
  - "public-coin-proof-recursion"
  - "hash-verification"
  - "accumulation-schemes"
  - "reed-solomon-proximity-accumulation"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-22"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-zkbridge"
  - "nahida-knowledge-20260620-snarkfold"
  - "nahida-knowledge-20260620-mangrove"
  - "nahida-knowledge-20260621-split-prover-zksnarks"
  - "nahida-knowledge-20260622-halo-recursive-proof-composition"
  - "nahida-knowledge-20260622-public-coin-proof-recursion"
  - "nahida-knowledge-20260623-arc-accumulation-reed-solomon"
source_refs:
  - "iacr:2021/370"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
  - "iacr:2019/1021"
  - "sha256:6814cb0cb866cdfe3af135c0edf4626a266b92e916edef9132c3912f7decbe0e"
  - "iacr:2022/1072"
  - "sha256:59a20b778b53499f5ea71aa494290794a84d780158d6a50fcb9745a4a981ab2a"
  - "sha256:12ffa8e928a85373ebcaa233ac0db0180ce98a58408f70fb918b64ddba08847c"
confidence: "medium"
trust_tier: "primary"
---

# Recursion and folding

## 定义与范围

- 定义: Recursion and folding 研究如何把多步证明/计算状态压缩为可递归验证或增量验证的结构。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `recursion-and-folding`
- Aliases/query keys: recursive proofs, folding schemes
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `recursion-and-folding`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source-backed seed 来自 Nova folding schemes，包括 relaxed R1CS 与 incrementally verifiable computation；zkBridge 提供一个应用型 seed: 用 Groth16 递归证明 deVirgo/Virgo verification circuit，把大 proof 压缩为链上友好的短 proof；SnarkFold 进一步提供 proof aggregation seed: 用 split IVC 将多个 SNARK proofs 聚合为常数大小/常数验证成本的 aggregation proof；Mangrove 提供 low-memory SNARK seed: 用 PCD/folding/commit-and-fold 把 Plonkish chunks 压缩为 succinct proof。Halo 补上 recursive proof composition seed: 通过 nested amortization 将 IPA-style polynomial commitment 的线性验证成本递延到最终 verifier，从而实现无 trusted setup 的 practical recursion。Split Prover 只作为 contrast-only source extension：它和 recursion/folding 都有 phase decomposition 直觉，但 split prover 保持原 verifier 并定义 aux privacy，因此不应归入 folding schemes。
Public-coin recursion source 进一步扩展 recursive proof composition：GKR/sum-check 负责批量哈希计算，外层 SNARK 只递归验证 public-coin verifier，并通过短 statement-binding 值控制 Fiat-Shamir 成本。
Arc 增加 accumulation schemes 子路线：它把 Reed-Solomon proximity / IOPP 工具迁移到 accumulation，构造 hash-based、distance-preserving、unbounded-depth 的 PCD/IVC accumulation route；因此应独立于 folding schemes，而不是把 ARC 当作 folding paper。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[zero-knowledge-proofs|zero-knowledge-proofs]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

降低递归证明中每步证明生成和验证的成本，把长期计算链折叠进小证明或可持续验证状态。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zero-knowledge-proofs|zero-knowledge-proofs]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[folding-schemes|folding-schemes]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[snark-proof-aggregation|SNARK proof aggregation]] | child | 可复用问题层：多个 SNARK proofs 的聚合与 verifier-cost 压缩；将承接 SnarkFold/SnarkPack/Hekaton 等后续 sources | [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] | active_seed |
| [[recursive-proof-composition|Recursive proof composition]] | child | 可复用问题层：proofs verifying proofs / IVC；承接 Halo-style nested amortization、folding-based IVC 和未来 accumulation/PCD sources | [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Halo]] | active_seed |
| [[accumulation-schemes|Accumulation schemes]] | child | 可复用方法族：把多条 proof/claim/accumulator obligation 压成一个 running accumulator；Arc 提供 hash-based RS proximity route | [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| folding scheme | folding scheme | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| relaxed R1CS | relaxed R1CS | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| IVC | IVC | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| recursive proof compression | 用链上友好 SNARK 证明另一种大 proof 的 verification circuit，从而压缩 proof size 和 verifier cost。 | 大 proof 直接在 verifier/on-chain 环境验证不可行，但 verification circuit 可被另一个 SNARK 高效证明。 | 增加 second-layer proving time；安全和成本依赖外层 proof system、curve/precompile 和随机预言机/哈希假设。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |
| split IVC for proof aggregation | 同时维护 F-friendly 与 Fold-friendly running instances，把 pairing-heavy SNARK verification 留在 algebraic-friendly relation，递归电路只证明 folding/hash claim。 | 多个 SNARK proofs 需要聚合，且直接把 verification relation 转成电路太贵。 | 需要具体 SNARK 的可折叠 relation；SnarkFold 只给 Groth16 detailed instantiation 与 operation-count comparison。 | [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] |
| folding-based low-memory SNARK construction | 把大 Plonkish relation 编译为 uniform chunks，用 PCD tree/folding 合并 chunk obligations，并通过 commit-and-fold 避免 opening constraints 膨胀。 | 单个大 proof 的 prover memory/pass complexity 是瓶颈，且 workload 可被 chunked/folded。 | 不等于 proof aggregation；Mangrove 性能是估计，PCD/folding assumptions 需 source 校准。 | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] |
| split-prover contrast route | 把 partial-witness proving 与 IVC/recursive SNARKs 做边界比较：两者都分阶段，但 verifier/aux privacy/assumption model 不同。 | 需要判断“用 IVC 替代 split prover”是否合理。 | 这不是 recursion/folding 方法本身；Split Prover 的 Groth16 lower bound 不迁移到 folding schemes。 | [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] |
| nested amortization for recursive proof composition | 递归电路只做 logarithmic marginal verification，把线性 PCS opening check 作为 public verifier state 递延并跨层摊销，最终 verifier 做一次线性检查。 | expensive verifier operation 可被承诺/摊销为可验证状态，且存在适合的 curve cycle 与 Fiat-Shamir transcript。 | final verifier 仍线性；不等价于 fully succinct SNARK，也不等价于 folding scheme。 | [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Halo]] |
| public-coin verifier recursion | 用 GKR 等 public-coin argument 证明 bulk computation，在外层 SNARK 里验证其 verifier，并用 SNARK verifier computation 绑定短 Fiat-Shamir 输入。 | 批量计算适合 public-coin/GKR，且外层 SNARK verifier 可拆分公共输入计算。 | 具体 GKR one-round instantiation 是 heuristic；不等于 accumulation/folding，也不等于通用 IP recursion。 | [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Public-coin recursion for hash verification]] |
| hash-based RS proximity accumulation | 用 Merkle-committed Reed-Solomon codewords、quotienting、out-of-domain samples 和 IOR formalism，把多个 proximity/NP accumulator claims 归约为一个 distance-preserving accumulator。 | statement 可路由为 RS proximity/R1CS accumulator relation，且满足 field/rate/list-decoding 参数。 | 当前由 Arc 单一 source 支撑；ROM/Merkle/list-decoding/proximity assumptions 不能自动泛化到任意 code 或 PCS。 | [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova: Recursive Zero-Knowledge Arguments from Folding Schemes]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | paper | 作为 recursive proof compression source extension：deVirgo proof -> Groth16 proof for on-chain verification | 应用型 source；不替代 Nova/folding foundation | `p10-p13` |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | paper | 作为 SNARK proof aggregation source extension：split IVC + augmented relaxed Groth16 folding | 单一 source；operation-count comparison 不是生产 benchmark；DOI/Venue unknown | `p1-p19`, `p22-p29` |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | paper | 作为 memory-efficient SNARK source extension：PCD/folding + commit-and-fold route | 单一 source；不是 proof aggregation source；canonical URL unknown | `p1-p69` |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | paper | 作为 contrast-only source extension：比较 split prover 与 IVC/recursive SNARKs 的 phase-decomposition 相似性和 verifier/assumption/Fiat-Shamir 边界 | 不是 recursion/folding foundation evidence；Groth16-specific construction 留在 split-prover node/source note | `p6-p7` |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Recursive Proof Composition without a Trusted Setup]] | paper | 作为 recursive proof composition source extension：nested amortization + IPA-style PCS enables practical recursion without trusted setup | final verifier 仍 linear；Tweedledum/Tweedledee/benchmark details 留在 source note | `§3`, `§4`, `§6`, `§7` |
| [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification]] | paper | 作为 recursive proof composition source extension：public-coin/GKR verifier recursion with short Fiat-Shamir inputs for faster hash verification | concrete GKR instantiation heuristic; not a GKR foundation source | `Abstract`, `§4-§6`, `Appendix H-I` |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]] | paper | 作为 accumulation schemes source extension：hash-based RS proximity accumulation removes bounded-depth restriction and avoids homomorphic vector commitments | no implementation benchmark; ePrint URL unverified; list-decoding/ROM assumptions remain source-bound | `Abstract`, `§1-§2`, `§6-§7`, `Appendix A-B` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-22`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: 当前是 Nova seed、Halo recursive-composition seed、zkBridge 应用型 seed、SnarkFold proof-aggregation seed、Mangrove low-memory SNARK seed、Split Prover 的 contrast-only bridge，以及 Arc accumulation seed。Nova 覆盖 folding/IVC 基础路线；Halo 覆盖 nested amortization route，即把 IPA-style polynomial commitment 的线性 verifier work 递延为 public verifier state 并在最终 verifier 处一次性检查；zkBridge 覆盖 proof compression for on-chain verification；SnarkFold 覆盖 split IVC for SNARK proof aggregation，即用多类型 running instances 避免 pairing-heavy verification relation 进入递归电路；Mangrove 覆盖 folding/PCD for memory-efficient SNARK construction，即用 uniform chunks、decoupled PCD 和 commit-and-fold 降低 prover memory/pass pressure。Split Prover 说明 phase decomposition 并不自动意味着 recursion/folding：当目标是 aux privacy、授权边界和保持原 verifier 时，应走 [[split-prover-zksnarks|Split prover zkSNARKs]] 而不是把问题折叠到 IVC。Public-coin recursion source 说明另一种非-folding route：把 GKR verifier 递归进外层 SNARK，通过 short Fiat-Shamir input 降低 hash-verification prover time。Arc 则补上 accumulation-specific route：用 RS proximity/list-decoding/IOR machinery 构造 hash-based unbounded accumulation，纠正了把这类 source 全部塞进 folding schemes 的粗粒度分类。

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
| [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova: Recursive Zero-Knowledge Arguments from Folding Schemes]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | source extension | recursive proof compression for on-chain verification | 方法族与解决路线; 代表 Sources; 当前综合 | no | keep as application evidence |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | source extension + child problem | split IVC and SNARK proof aggregation route | 下级结构; 方法族与解决路线; 当前综合; Bridge Links | yes | absorb SnarkPack/TIPP/Hekaton for comparison; Pianist routes to [[distributed-proof-generation|Distributed proof generation]], Mangrove routes to [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | source extension + bridge | folding/PCD route for memory-efficient SNARK construction | 方法族与解决路线; 当前综合; Bridge Links | yes | route details through [[memory-efficient-snarks|Memory-efficient SNARKs]]; do not treat as proof aggregation |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | contrast-only source extension + bridge | distinguishes partial-witness split proving from IVC/recursive SNARKs; records verifier/assumption/Fiat-Shamir non-transfer boundary | 方法族与解决路线; 当前综合; Bridge Links | yes | route details through [[split-prover-zksnarks|Split prover zkSNARKs]] |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Recursive Proof Composition without a Trusted Setup]] | source extension + child problem + bridge | creates [[recursive-proof-composition|Recursive proof composition]] and adds nested amortization route; links PCS verifier-state deferral to recursion | 下级结构; 方法族与解决路线; 当前综合; Bridge Links | yes | compare future accumulation/Halo2/public-coin recursion sources before generalizing |
| [[eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification|Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification]] | source extension + bridge | adds public-coin verifier recursion route and interactive-proofs bridge; keeps GKR/sum-check as dependencies | 方法族与解决路线; 当前综合; Bridge Links | yes | compare with Arc/accumulation sources next |
| [[sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes|Arc: Accumulation for Reed-Solomon Codes]] | source extension + child method-family + bridge | creates [[accumulation-schemes|Accumulation schemes]]; adds hash-based RS proximity accumulation and FRI IOPP bridge | 下级结构; 方法族与解决路线; 当前综合; Bridge Links | yes | absorb BMNW24/Protostar/ProtoGalaxy/FRI sources to refine taxonomy |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, succinct_verification, soundness, performance_compression | Recursive compression transfers proof-system efficiency into bridge verification; liveness and chain semantics do not transfer. | active_seed |
| [[folding-schemes-to-snark-proof-aggregation|Folding schemes -> SNARK proof aggregation]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation` | applies_to, method_transfer, performance_compression | Folding/IVC transfers as aggregation route; specific SNARK relation, curve, setup, and final verifier duties do not transfer automatically. | active_seed |
| [[folding-schemes-to-memory-efficient-snarks|Folding schemes -> memory-efficient SNARKs]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | application, method_transfer, performance_compression, dependency | Folding/PCD transfers as low-memory SNARK construction route; specific Plonkish compiler, commitment map and performance estimates do not transfer automatically. | active_seed |
| [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks; zero-knowledge-proofs/recursion-and-folding` | contrast, design_boundary, phase_decomposition | Phase decomposition is shared intuition; verifier preservation, aux privacy, authorization boundary and Groth16 lower bound do not transfer to IVC/folding automatically. | active_seed |
| [[polynomial-commitments-to-recursive-proof-composition|Polynomial commitments -> recursive proof composition]] | `zero-knowledge-proofs/polynomial-commitments; zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | dependency, method_transfer, verification_deferral, performance_compression | Halo transfers amortized PCS verifier work into recursive verifier-state design; arbitrary PCS/curve/setup compatibility does not transfer. | active_seed |
| [[public-coin-interactive-proofs-to-recursive-proof-composition|Public-coin interactive proofs -> recursive proof composition]] | `verifiable-computation/interactive-proofs; zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | method_transfer, dependency, verification_embedding, fiat_shamir_boundary | Public-coin verifier recursion transfers as a route; the GKR one-round heuristic and SNARK verifier split requirements do not transfer automatically. | active_seed |
| [[fri-iopps-to-accumulation-schemes|FRI IOPPs -> accumulation schemes]] | `zero-knowledge-proofs/proof-systems/fri-iopps; zero-knowledge-proofs/recursion-and-folding/accumulation-schemes` | method_transfer, dependency, shared_pattern, formalization_bridge | RS proximity/list-decoding/quotienting transfers into Arc-style accumulation; ordinary FRI, DAS commitments and full PCS semantics do not transfer automatically. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-recursion-and-folding | is_a | nahida-knowledge-zero-knowledge-proofs | vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md; vault/04_Knowledge/zero-knowledge-proofs.md | medium | active_seed |
| nahida-knowledge-recursion-and-folding | has_child | nahida-knowledge-folding-schemes | vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding.md; vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/folding-schemes.md | medium | active_seed |
| nahida-knowledge-recursion-and-folding | evidenced_by | vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md | vault/03_Sources/papers/eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes.md | medium | active_seed |
| nahida-knowledge-recursion-and-folding | evidenced_by | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | medium | active_seed |
| nahida-knowledge-recursion-and-folding | has_child | nahida-knowledge-snark-proof-aggregation | vault/04_Knowledge/zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation.md; vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-recursion-and-folding | evidenced_by | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-recursion-and-folding | bridges_to | nahida-bridge-folding-schemes-to-snark-proof-aggregation | vault/05_Bridges/folding-schemes-to-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-recursion-and-folding | bridges_to | nahida-bridge-folding-schemes-to-memory-efficient-snarks | vault/05_Bridges/folding-schemes-to-memory-efficient-snarks.md | high | active_seed |
| nahida-knowledge-recursion-and-folding | evidenced_by | vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md | Mangrove source note | high | active_seed |
| nahida-knowledge-recursion-and-folding | bridges_to | nahida-bridge-split-prover-zksnarks-to-recursion-and-folding | bridge note; Split Prover p6-p7 | medium | active_seed |
| nahida-knowledge-recursion-and-folding | has_child | nahida-knowledge-recursive-proof-composition | Halo source note; recursive-proof-composition node | high | active_seed |
| nahida-knowledge-recursion-and-folding | evidenced_by | vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md | Halo §3-§7 | high | active_seed |
| nahida-knowledge-recursion-and-folding | bridges_to | nahida-bridge-polynomial-commitments-to-recursive-proof-composition | bridge note; Halo §3-§4 | high | active_seed |
| nahida-knowledge-recursion-and-folding | evidenced_by | vault/03_Sources/papers/eprint-2022-1072-recursion-over-public-coin-interactive-proof-systems-faster-hash-verification.md | public-coin recursion source note | high | active_seed |
| nahida-knowledge-recursion-and-folding | bridges_to | nahida-bridge-public-coin-interactive-proofs-to-recursive-proof-composition | bridge note | high | active_seed |
| nahida-knowledge-recursion-and-folding | has_child | nahida-knowledge-accumulation-schemes | Arc source note; accumulation-schemes node | high | active_seed |
| nahida-knowledge-recursion-and-folding | evidenced_by | vault/03_Sources/papers/sha256-12ffa8e928a8-arc-accumulation-for-reed-solomon-codes.md | Arc source note | high | active_seed |
| nahida-knowledge-recursion-and-folding | bridges_to | nahida-bridge-fri-iopps-to-accumulation-schemes | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| SuperNova/HyperNova、Halo 2、recursive SNARK compression 等缺 source。 | Halo/Public-coin recursion/Arc 已补三条 route；仍需后续 sources 校准 modern accumulation/folding/PCD 路线。 | nahida-research-search or nahida-update | medium | queued |
| Additional accumulation sources 缺。 | Arc 已创建 accumulation-schemes seed，但 BCLMS/BCMS/BMNW24/Protostar/ProtoGalaxy 等仍未深读。 | nahida-update / nahida-research-search | high | queued |
| SnarkPack/TIPP/Hekaton 等 proof aggregation sources 缺；Pianist 已归入 distributed proof generation，Mangrove 已归入 memory-efficient SNARKs。 | 影响 SNARK proof aggregation 节点的比较完整性，并避免把 prover-side distributed proving 或 low-memory SNARK construction 混入 aggregation。 | nahida-update | high | pending_queue |
| PCD / ProtoGalaxy / Gemini / streaming SNARK sources 缺。 | Mangrove 打开 folding-to-low-memory-SNARK route，需要更多 primary sources 校准。 | nahida-update or nahida-research-search | high | queued |
| Split prover / IVC 可替代性 sources 缺。 | Split Prover 指出 IVC/recursive SNARKs 相邻但不等价；需要后续来源判断 partial-witness proving 是否可由 recursive route 解决。 | nahida-research-search / nahida-daily-fetch | medium | watch |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 1 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkbridge | Added recursive proof compression source extension from zkBridge. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-snarkfold | Added SNARK proof aggregation child node and split IVC source extension. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-mangrove | Added folding/PCD route for memory-efficient SNARK construction and kept Mangrove out of proof aggregation. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-split-prover-zksnarks | Added contrast-only bridge from split prover zkSNARKs to recursion/folding to prevent misrouting phase-aware proving as IVC/folding. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-halo-recursive-proof-composition | Added recursive proof composition child node, nested amortization method route and PCS bridge from Halo. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-public-coin-proof-recursion | Added public-coin verifier recursion route and bridge to recursive proof composition. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-arc-accumulation-reed-solomon | Added accumulation-schemes child node, RS proximity/hash-based accumulation route and FRI bridge from Arc. | 1 source note | codex |
