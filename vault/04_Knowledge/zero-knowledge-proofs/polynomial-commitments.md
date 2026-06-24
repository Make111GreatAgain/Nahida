---
id: "nahida-knowledge-polynomial-commitments"
title: "Polynomial commitments"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "polynomial-commitments"
domain_id: "zero-knowledge-proofs"
direction_id: "polynomial-commitments"
parent_knowledge_refs:
  - "nahida-knowledge-zero-knowledge-proofs"
child_knowledge_refs:
  - "nahida-knowledge-kzg-commitments"
ontology_path:
  - "zero-knowledge-proofs"
  - "polynomial-commitments"
primary_ontology_path: "zero-knowledge-proofs/polynomial-commitments"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "is_a"
    to: "nahida-knowledge-zero-knowledge-proofs"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments.md"
      - "vault/04_Knowledge/zero-knowledge-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "has_child"
    to: "nahida-knowledge-kzg-commitments"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments/kzg-commitments.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments/kzg-commitments.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "related_to"
    to: "nahida-knowledge-fri-iopps"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "bridges_to"
    to: "nahida-bridge-folding-schemes-to-sum-check-and-polynomial-commitments"
    evidence_refs:
      - "vault/05_Bridges/folding-schemes-to-sum-check-and-polynomial-commitments.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "bridges_to"
    to: "nahida-bridge-modular-zksnarks-to-polynomial-commitments-and-sum-check"
    evidence_refs:
      - "vault/05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
      - "vault/05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "bridges_to"
    to: "nahida-bridge-polynomial-commitments-to-recursive-proof-composition"
    evidence_refs:
      - "vault/05_Bridges/polynomial-commitments-to-recursive-proof-composition.md"
      - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-polynomial-commitments"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-transparent-polynomial-commitments"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-transparent-polynomial-commitments.md"
      - "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-folding-schemes-to-sum-check-and-polynomial-commitments"
  - "nahida-bridge-modular-zksnarks-to-polynomial-commitments-and-sum-check"
  - "nahida-bridge-polynomial-commitments-to-recursive-proof-composition"
  - "nahida-bridge-memory-efficient-snarks-to-transparent-polynomial-commitments"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md"
  - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
  - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
  - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
  - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
  - "vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md"
  - "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
representative_source_refs:
  - "doi:10.1007/978-3-642-17373-8_11"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
  - "iacr:2019/1021"
  - "sha256:51c6a37d5caa894a133dae1ede4631ad35dc729675c6ac9a4caf00be5ecfc6ff"
query_keys:
  - "Polynomial commitments"
  - "polynomial-commitments"
  - "PCS"
  - "多项式承诺"
  - "DKZG"
  - "FRI commitments"
  - "FRI"
  - "erasure-code commitments"
  - "KZG fair data exchange"
  - "VECK for KZG"
  - "elastic KZG"
  - "streaming polynomial commitment"
  - "zero-knowledge verifiable polynomial delegation"
  - "zk-VPD"
  - "committed polynomial evaluation"
  - "inner-product argument polynomial commitments"
  - "IPA polynomial commitments"
  - "amortized polynomial openings"
  - "nested amortization"
  - "transparent polynomial commitments for low-memory SNARKs"
  - "HOBBIT PCS"
  - "post-quantum polynomial commitment SNARK"
aliases:
  - "PCS"
  - "多项式承诺"
  - "FRI commitments"
  - "verifiable polynomial delegation"
  - "IPA polynomial commitments"
domains:
  - "zero-knowledge-proofs"
topics:
  - "polynomial-commitments"
  - "bivariate-kzg"
  - "fri-iopps"
  - "erasure-code-commitments"
  - "fair-data-exchange"
  - "elastic-snarks"
  - "zk-vpd"
  - "verifiable-polynomial-delegation"
  - "inner-product-argument-pcs"
  - "amortized-openings"
  - "transparent-polynomial-commitments"
  - "post-quantum-zksnarks"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-22"
created: "2026-06-20"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-pianist"
  - "nahida-knowledge-20260620-frida-data-availability-from-fri"
  - "nahida-knowledge-20260620-atomic-fair-data-exchange"
  - "nahida-knowledge-20260622-gemini-elastic-snarks"
  - "nahida-knowledge-20260622-vsql-zk"
  - "nahida-knowledge-20260622-halo-recursive-proof-composition"
  - "nahida-knowledge-20260623-hobbit-space-efficient-zksnark"
source_refs:
  - "doi:10.1007/978-3-642-17373-8_11"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
  - "iacr:2019/1021"
  - "sha256:6814cb0cb866cdfe3af135c0edf4626a266b92e916edef9132c3912f7decbe0e"
  - "sha256:51c6a37d5caa894a133dae1ede4631ad35dc729675c6ac9a4caf00be5ecfc6ff"
confidence: "medium"
trust_tier: "primary"
---

# Polynomial commitments

## 定义与范围

- 定义: Polynomial commitments 让 prover 承诺一个多项式，并后续证明某点评估值或批量关系，而 verifier 不需要读取整个多项式。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `polynomial-commitments`
- Aliases/query keys: PCS, 多项式承诺
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `polynomial-commitments`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source-backed seed 来自 KZG paper；Pianist 提供了 KZG 在 distributed bivariate proof generation 中的 usage extension；FRIDA 提供了 FRI/IOPP 与 commitment landscape 的相邻证据，但它选择的是 erasure-code commitments for DAS，而不是把 FRI 当作 full polynomial commitment API；Atomic/Fair Data Exchange 提供 KZG committed evaluations 在 fair data exchange 中的 usage signal；Gemini 提供 KZG 在 elastic SNARK 中作为 streaming commit/open layer 的 usage signal；zk-vSQL 提供 zero-knowledge verifiable polynomial delegation source extension，用 committed evaluation 替代明文 evaluation 来支撑零知识 VC argument；Halo 提供 IPA-style PCS source extension：用内积证明做 polynomial opening，并通过 amortized opening verification 把线性 verifier work 转化为递归 proof composition 可递延的 verifier state。HOBBIT 提供 transparent plausibly post-quantum multilinear PCS source extension：用 Brakedown-style PCS + tensor-code proof composition + WHIR 组合出可 streaming 的低内存 SNARK commitment/opening layer。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[zero-knowledge-proofs|zero-knowledge-proofs]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

为 SNARK、verifiable secret sharing、data availability 和 polynomial IOP 提供 succinct commitment/opening primitive。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zero-knowledge-proofs|zero-knowledge-proofs]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[kzg-commitments|kzg-commitments]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| KZG/pairing-based quotient witness | KZG/pairing-based quotient witness | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| batch opening and evaluation proof | batch opening and evaluation proof | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| trusted setup boundary | trusted setup boundary | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| bivariate/distributed KZG usage | 在 `Y` 维 machine index 和 `X` 维 local circuit index 上承诺 bivariate polynomial，并聚合各 machine 的 commitments/openings。 | Plonk/KZG-compatible distributed proving，需要常数 proof/opening 结构。 | 不是 KZG foundation replacement；依赖 pairing/SRS，且 protocol-specific。 | [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] |
| FRI/IOPP-derived erasure-code commitments | 用 [[fri-iopps|FRI IOPPs]] 的 proximity/folding/opening-consistency machinery 生成 DAS 所需的 erasure-code commitments。 | 目标是 evaluation-domain codeword openings and data availability sampling，而非任意点 polynomial evaluation API。 | FRIDA 明确指出直接用 FRI as polynomial commitment 会有额外 opening overhead；因此这里是 adjacent/source extension，不拆为 PCS child。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| KZG-backed committed-data exchange | 用 KZG commitment 锚定 polynomial evaluations，再用 VECK 证明 ciphertext 与 committed evaluations 一致，支持全量或 subset data exchange。 | 客户端已有 KZG commitment，服务器持有数据/片段并需要公平收款。 | PCS 只提供 correctness anchor；fairness、privacy-before-payment 和 key release 由 FDE/VECK/chain 层提供。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| KZG as elastic SNARK PCS layer | 让 KZG commitment/opening 以 coefficient/SRS streams 与 quotient recurrence 小状态运行，支撑低内存 SNARK prover。 | SNARK compiler 需要 polynomial commitment layer 可 streaming commit/open。 | 这是 KZG child usage extension；不代表所有 PCS 都有相同 streaming properties。 | [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] |
| zero-knowledge verifiable polynomial delegation | 将多项式点评估值替换为 hiding commitment，并证明该 commitment 确实承诺了 `f(t)`。 | VC/proof-system 需要验证 polynomial evaluation，但不能泄露 evaluation/witness-dependent value。 | 依赖 pairing、q-SDH 和 knowledge-of-exponent 型假设；这是 VPD/zk-vSQL route，不是 KZG child，也不是完整 PCS landscape。 | [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] |
| IPA-style PCS with amortized openings | 用 Pedersen-vector/inner-product argument 承诺多项式系数并证明点评估；把 opening verification 中的线性 multiscalar multiplication 跨 proofs 摊销。 | 需要 trusted-setup-free PCS、可利用 challenge-vector smooth structure，并能用 helper/random linear combination 批量证明 claimed verifier outputs。 | 不是 KZG；final verifier 仍可能 linear；Halo 的 recursion route 依赖 nested amortization 和 curve cycle。 | [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Halo]] |
| Transparent/PQ multilinear PCS for streaming SNARKs | 用 Brakedown-style row/column commitment、tensor code 和 proof composition 降低 Spielman-code 证明成本；streaming variant 以 `O(B)` buffer 生成 commitment/evaluation proof。 | 低内存 SNARK 需要避免 KZG SRS/pairing assumptions，且能接受更大 proof size。 | HOBBIT source-specific route；WHIR/Brakedown/BrakingBase/Orion foundation 仍需补齐；plausibly post-quantum 不等于标准化 PQ guarantee。 | [[sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time|HOBBIT]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials|Constant-Size Commitments to Polynomials and Their Applications]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | paper | 作为 modern usage source extension：DKZG/bivariate KZG supports distributed Plonk proving | 应用/协议 source；不替代 PCS/KZG foundation | `§4.2`, `p9-p11` |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | paper | 作为 FRI/commitment-adjacent source extension：说明 FRI IOPPs 可用于 erasure-code commitments and DAS，并给出与 FRI-as-polynomial-commitment route 的效率边界 | 不是 PCS foundation source；details route through [[fri-iopps|FRI IOPPs]] and DAS bridge | `§1.3`, `§3-§5` |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | paper | 作为 KZG usage source extension：KZG commitments support VECK-backed committed-data fair exchange and selective retrieval | 不是 PCS foundation source；details route through [[kzg-commitments|KZG commitments]] and [[fair-data-exchange|Fair data exchange for committed data]] | `§1`, `§5.1-§5.3` |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | paper | 作为 KZG/PCS usage source extension：KZG commitments/openings can be streaming realized for elastic SNARKs | 不是 PCS foundation source；details route through [[kzg-commitments|KZG commitments]] and [[memory-efficient-snarks|Memory-efficient SNARKs]] | `§2.3`, `§9`, `§10` |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | paper | 作为 VPD/committed-evaluation source extension：zk-VPD 证明 committed polynomial evaluation correctness | 不是 KZG foundation source；details route through source note and modular-zksnarks bridge | `§3`, `Theorem 1` |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Recursive Proof Composition without a Trusted Setup]] | paper | 作为 IPA-style PCS source extension：inner-product polynomial openings and amortized verifier work support nested amortization | 不是 KZG；不是完整 PCS taxonomy；Halo-specific recursion details stay in source note and bridge | `§3`, `§4` |
| [[sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time|Hobbit: Space-Efficient zkSNARK with Optimal Prover Time]] | paper | 作为 transparent/PQ PCS source extension：给出 linear-time multilinear PCS 和 streaming variant，用于 HOBBIT low-memory zkSNARK。 | 不是 KZG；proof size 较大；PCS primary comparisons 仍需 WHIR/Brakedown/BrakingBase/Orion sources 校准。 | `§4`, Table 2 |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: 当前 direction 主要由 KZG seed 支撑，不能代表完整 PCS landscape。Pianist 增加一个现代 usage signal: KZG-style commitments/openings 可以被扩展为 distributed bivariate KZG，用于多机 Plonk proving；FRIDA 增加一个边界 signal: FRI/IOPP machinery 可以服务 erasure-code commitments and DAS，但这不同于 full polynomial commitments；Atomic/Fair Data Exchange 增加另一个 usage signal: KZG 的 succinct commitment/opening 可作为 committed-data exchange 的 correctness anchor；Gemini 增加 elastic SNARK usage signal: KZG commitment/opening 可作为 streaming PCS layer 支撑低内存 prover；zk-vSQL 增加 VPD/committed-evaluation signal: polynomial evaluation 可以被隐藏在承诺中并保持可验证；Halo 增加 IPA-style PCS/amortized-opening signal；HOBBIT 增加 transparent/PQ multilinear PCS signal，说明低内存 SNARK 的 PCS 层不必只走 KZG，但要接受更大 proof size 和更多 proof-composition machinery。当前节点应区分 foundation 与 usage extension，不把 FDE/FRIDA/Pianist/Gemini/vSQL/Halo/HOBBIT 的协议细节并入 PCS 基础定义。

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
| [[doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials|Constant-Size Commitments to Polynomials and Their Applications]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | usage source extension | DKZG/bivariate KZG for distributed proving | 方法族与解决路线; 代表 Sources; 当前综合 | no | route protocol details through [[distributed-proof-generation|Distributed proof generation]] and source note |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | adjacent source extension | FRI IOPPs can be compiled to erasure-code commitments for DAS; direct FRI-as-PCS route would be less efficient for this use case | 方法族与解决路线; 代表 Sources; 当前综合; 缺口与队列 | no | route foundation through [[fri-iopps|FRI IOPPs]]; keep PCS comparison queued |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | usage source extension | KZG committed evaluations and subset openings as VECK/FDE correctness anchor | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route bridge through [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | usage source extension | KZG commitment/opening as streaming PCS layer for elastic SNARKs | 方法族与解决路线; 代表 Sources; 当前综合 | no | route bridge through [[memory-efficient-snarks-to-kzg-commitments|Memory-efficient SNARKs -> KZG commitments]] |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | VPD source extension | committed polynomial evaluation / zk-VPD for function-independent zero-knowledge arguments | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route bridge through [[modular-zksnarks-to-polynomial-commitments-and-sum-check|Modular zkSNARKs -> polynomial commitments and sum-check]] |
| [[eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup|Recursive Proof Composition without a Trusted Setup]] | IPA/transparent PCS source extension | inner-product-style PCS and amortized opening verification as dependency for recursive proof composition | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route recursion through [[recursive-proof-composition|Recursive proof composition]]; keep Halo-specific equations in source note |
| [[sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time|Hobbit: Space-Efficient zkSNARK with Optimal Prover Time]] | transparent/PQ multilinear PCS source extension | tensor-code proof-composition PCS and streaming variant for low-memory SNARKs | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route low-memory implications through [[memory-efficient-snarks-to-transparent-polynomial-commitments|Memory-efficient SNARKs -> transparent polynomial commitments]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[folding-schemes-to-sum-check-and-polynomial-commitments|Folding schemes -> sum-check and polynomial commitments]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/polynomial-commitments` | dependency, shared_pattern | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 | active_seed |
| [[modular-zksnarks-to-polynomial-commitments-and-sum-check|Modular zkSNARKs -> polynomial commitments and sum-check]] | `zero-knowledge-proofs/proof-systems/modular-zksnarks; zero-knowledge-proofs/polynomial-commitments; verifiable-computation/interactive-proofs/sum-check-protocol` | dependency, shared_pattern, implementation_reuse | 需要保留端点领域边界；可迁移的是模式/依赖/应用关系，不是把两个 knowledge node 合并。 | active_seed |
| [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments; blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | dependency, application, cryptographic_enabler | KZG transfer is through the child node [[kzg-commitments|KZG commitments]]; FDE fairness is not a PCS property. | active_seed |
| [[polynomial-commitments-to-recursive-proof-composition|Polynomial commitments -> recursive proof composition]] | `zero-knowledge-proofs/polynomial-commitments; zero-knowledge-proofs/recursion-and-folding/recursive-proof-composition` | dependency, method_transfer, verification_deferral, performance_compression | Halo transfers an amortized IPA-style opening-verification pattern; arbitrary PCS compatibility and Halo implementation parameters do not transfer. | active_seed |
| [[memory-efficient-snarks-to-transparent-polynomial-commitments|Memory-efficient SNARKs -> transparent polynomial commitments]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/polynomial-commitments` | dependency, method_transfer, transparent_commitment_route, post_quantum_candidate | HOBBIT transfers transparent/PQ PCS machinery into low-memory SNARK construction; it does not transfer all HOBBIT PIOP or lookup machinery. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-polynomial-commitments | is_a | nahida-knowledge-zero-knowledge-proofs | vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments.md; vault/04_Knowledge/zero-knowledge-proofs.md | medium | active_seed |
| nahida-knowledge-polynomial-commitments | has_child | nahida-knowledge-kzg-commitments | vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments.md; vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments/kzg-commitments.md | medium | active_seed |
| nahida-knowledge-polynomial-commitments | evidenced_by | vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md | vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md | medium | active_seed |
| nahida-knowledge-polynomial-commitments | evidenced_by | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | medium | active_seed |
| nahida-knowledge-polynomial-commitments | evidenced_by | vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md | FRIDA source note | medium | active_seed |
| nahida-knowledge-polynomial-commitments | evidenced_by | vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md | FDE source note | medium | active_seed |
| nahida-knowledge-polynomial-commitments | evidenced_by | vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md | Gemini source note | medium | active_seed |
| nahida-knowledge-polynomial-commitments | related_to | nahida-knowledge-fri-iopps | FRIDA source note | medium | active_seed |
| nahida-knowledge-polynomial-commitments | bridges_to | nahida-bridge-folding-schemes-to-sum-check-and-polynomial-commitments | vault/05_Bridges/folding-schemes-to-sum-check-and-polynomial-commitments.md | medium | active_seed |
| nahida-knowledge-polynomial-commitments | bridges_to | nahida-bridge-modular-zksnarks-to-polynomial-commitments-and-sum-check | vault/05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md | medium | active_seed |
| nahida-knowledge-polynomial-commitments | evidenced_by | vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md | zk-vSQL §3/Theorem 1 | medium | active_seed |
| nahida-knowledge-polynomial-commitments | evidenced_by | vault/03_Sources/papers/eprint-2019-1021-halo-recursive-proof-composition-without-trusted-setup.md | Halo §3-§4 | high | active_seed |
| nahida-knowledge-polynomial-commitments | bridges_to | nahida-bridge-polynomial-commitments-to-recursive-proof-composition | bridge note; Halo §3-§4 | high | active_seed |
| nahida-knowledge-polynomial-commitments | evidenced_by | vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md | HOBBIT §4/Table 2 | high | active_seed |
| nahida-knowledge-polynomial-commitments | bridges_to | nahida-bridge-memory-efficient-snarks-to-transparent-polynomial-commitments | bridge note; HOBBIT §4-§5 | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| FRI-as-PCS、vector commitments、PCS in PLONK/Marlin、IPA comparison sources 缺。 | Halo 已提供 IPA-style PCS usage seed，但仍不能替代完整 PCS/IPA/FRI foundation。 | nahida-research-search or nahida-update | medium | queued |
| DKZG/bivariate KZG primary treatment beyond Pianist 缺。 | 影响 distributed PCS usage comparison，但不阻塞当前 source extension。 | nahida-update / nahida-research-search | medium | queued |
| KZG-backed fair exchange 目前只有 FDE source。 | SAVER 已补足 generic verifiable-encryption seed；仍需 ZKCPlus/VECK/KZG-specific fair-exchange sources 决定是否拆出更广 fair-exchange 方法族。 | nahida-update | medium | queued |
| Streaming/elastic PCS comparison sources 缺。 | Gemini 给出 KZG route，但仍需 IPA/FRI/DARK/transparent PCS 对照，避免把 KZG-specific 方法泛化。 | nahida-update / nahida-research-search | medium | review |
| Transparent/PQ multilinear PCS foundation 缺。 | HOBBIT 给出实用 route，但 WHIR、Brakedown、BrakingBase、Orion 和 code-based PCS foundation 仍未系统吸收。 | nahida-update / nahida-research-search | high | queued |
| VPD / PolyCom comparison sources 缺。 | zk-vSQL 补了 VPD/committed-evaluation route，但仍需 vSQL original、PolyCom/LegoSNARK 对照和 modern PCS comparison，避免把 VPD 直接等同于 KZG/PCS 通用 API。 | nahida-update / nahida-research-search | medium | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 2 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Added DKZG/bivariate KZG as usage extension from Pianist. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-frida-data-availability-from-fri | Added FRI/IOPP-derived erasure-code commitments as adjacent DAS route and preserved PCS boundary. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-atomic-fair-data-exchange | Added KZG-backed committed-data exchange as a usage extension. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-gemini-elastic-snarks | Added KZG as streaming PCS layer usage extension from Gemini. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-vsql-zk | Added zk-VPD / committed polynomial evaluation as a VPD source extension and bridge evidence. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-halo-recursive-proof-composition | Added IPA-style polynomial commitments with amortized openings as a recursive-proof-composition dependency. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-hobbit-space-efficient-zksnark | Added HOBBIT transparent/PQ multilinear PCS usage route for memory-efficient SNARKs. | 1 source note | codex |
