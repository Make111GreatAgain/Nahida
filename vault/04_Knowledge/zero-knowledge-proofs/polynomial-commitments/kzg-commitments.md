---
id: "nahida-knowledge-kzg-commitments"
title: "KZG commitments"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "kzg-commitments"
domain_id: "zero-knowledge-proofs"
direction_id: "polynomial-commitments"
parent_knowledge_refs:
  - "nahida-knowledge-polynomial-commitments"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "polynomial-commitments"
  - "kzg-commitments"
primary_ontology_path: "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-kzg-commitments"
    relation: "is_a"
    to: "nahida-knowledge-polynomial-commitments"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments/kzg-commitments.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "bridges_to"
    to: "nahida-bridge-kzg-commitments-to-fair-data-exchange"
    evidence_refs:
      - "vault/05_Bridges/kzg-commitments-to-fair-data-exchange.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "bridges_to"
    to: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    evidence_refs:
      - "vault/05_Bridges/private-delegated-proving-to-kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-kzg-commitments"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-kzg-commitments-to-fair-data-exchange"
  - "nahida-bridge-private-delegated-proving-to-kzg-commitments"
  - "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md"
  - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
  - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
  - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
  - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
  - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
  - "vault/03_Sources/github/consensys-gnark-master.md"
representative_source_refs:
  - "doi:10.1007/978-3-642-17373-8_11"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
  - "github:Consensys/gnark@cb367d86b8ad0cc1ee1a29b89658f2f92a461721"
query_keys:
  - "KZG commitments"
  - "kzg-commitments"
  - "Kate commitments"
  - "KZG"
  - "DKZG"
  - "VECK for KZG"
  - "KZG fair data exchange"
  - "KZG consistency checker"
  - "Siniel WCC"
  - "Siniel PCC"
  - "EOS PIOP consistency checker"
  - "EOS KZG commitments"
  - "elastic KZG"
  - "streaming KZG"
  - "Gemini KZG"
  - "elastic multilinear KZG"
  - "Epistle multilinear KZG"
  - "gnark PLONK KZG"
  - "gnark KZG SRS"
aliases:
  - "Kate commitments"
  - "KZG"
domains:
  - "zero-knowledge-proofs"
topics:
  - "kzg-commitments"
  - "bivariate-kzg"
  - "fair-data-exchange"
  - "verifiable-encryption"
  - "private-delegated-proving"
  - "consistency-checking"
  - "piop-consistency-checker"
  - "elastic-snarks"
  - "streaming-kzg"
  - "multilinear-kzg"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-24"
valid_until: "2026-07-24"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-24"
created: "2026-06-20"
updated: "2026-06-24"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-pianist"
  - "nahida-knowledge-20260620-atomic-fair-data-exchange"
  - "nahida-knowledge-20260621-siniel-private-delegated-proving"
  - "nahida-knowledge-20260623-eos-private-delegated-proving"
  - "nahida-knowledge-20260622-gemini-elastic-snarks"
  - "nahida-knowledge-20260623-epistle-elastic-snarks"
  - "nahida-knowledge-20260624-consensys-gnark"
source_refs:
  - "doi:10.1007/978-3-642-17373-8_11"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
  - "github:Consensys/gnark@cb367d86b8ad0cc1ee1a29b89658f2f92a461721"
confidence: "medium"
trust_tier: "primary"
---

# KZG commitments

## 定义与范围

- 定义: KZG commitments 是 pairing-based polynomial commitment scheme，提供常数大小 commitment/opening proof，并通过 quotient polynomial witness 证明 evaluation。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `kzg-commitments`
- Aliases/query keys: Kate commitments, KZG
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `kzg-commitments`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 source seed 是 Kate-Zaverucha-Goldberg 2010 paper。该节点应解释 KZG 的 reusable role，而不是只复制论文摘要。Pianist 提供一个 DKZG/bivariate KZG usage extension，用于 distributed Plonk proving；Atomic and Fair Data Exchange via Blockchain 提供另一个 usage extension：把 KZG 的 committed evaluations 和 subset openings 用作 fair data exchange 的 correctness anchor；EOS 和 Siniel 则从两个不同 delegated-proving 设计说明 KZG/PCS commitments/openings 可作为 private delegated proving 中 PIOP/witness consistency checking 的绑定机制；Gemini 则新增 elastic KZG usage extension，说明 KZG commitment/opening 可以被按 coefficient/SRS streams 低内存实现，服务 elastic SNARK compiler。Epistle 进一步说明 multilinear KZG 也可被 elastic realized，用于 Plonkish/HyperPlonk-style SNARK 的 streaming prover。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[polynomial-commitments|polynomial-commitments]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

为 polynomial evaluation proof 提供 succinct opening，服务 SNARK、VSS、DA 等上层系统。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[polynomial-commitments|polynomial-commitments]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| SRS/trusted setup | SRS/trusted setup | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| quotient polynomial witness | quotient polynomial witness | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| pairing verification equation | pairing verification equation | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| batch opening | batch opening | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| DKZG / bivariate KZG | 每个 machine 对自己的 bivariate polynomial slice 做 commitment/opening，master 聚合为全局 commitment/proof；verification 保持 pairing-based succinct opening intuition。 | distributed Plonk proving，需要按 machine/circuit 两个维度组织多项式。 | 这是 KZG 的应用扩展，不替代 KZG foundation；依赖 SRS/pairing assumptions 和 Pianist 协议上下文。 | [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] |
| VECK-backed committed-data exchange | 用 KZG commitment 锚定数据 polynomial，再用 VECK 证明 ciphertext 加密的是承诺下的 evaluations 或 subset evaluations。 | 客户端持有 KZG commitment，服务器持有数据/片段，需要公平付费检索。 | KZG 只提供承诺/打开语义；公平性来自 VECK 与区块链 payment/key-release。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| KZG-backed consistency checking | 让服务器把 secret-shared/authenticated witness 或 PIOP polynomial state 承诺到 KZG commitments，再通过 opening/linear checks 证明各服务器输出与同一底层 witness/share set 一致。 | private delegated proving、MPC-style zkSNARK prover outsourcing，需要非交互一致性检查。 | 这是 Siniel 的 usage extension；privacy 和 robustness 还依赖 secret sharing、authentication tags、Beaver triples 和具体 adversary threshold。 | [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]] |
| EOS PIOP/PCS consistency checking | 用 KZG-style PC commit/open circuits 和 random-point PIOP consistency checks 约束 worker 生成的 polynomial oracles，避免最终 proof validity 变成 witness leakage channel。 | delegator 可在线参与 consistency-check rounds，且目标是 PIOP+PCS universal-setup zkSNARK delegation。 | 这是 EOS/MARLIN-style usage extension；KZG 不提供 witness privacy 本身，delegated SNARK protocol 和 secret sharing 才决定安全边界。 | [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS]] |
| Elastic KZG commitment/opening | commitment 通过 coefficient/SRS streams 维护 running group-sum；opening 用高次到低次的 quotient-witness recurrence 小状态生成 opening witness。 | elastic SNARK / streaming R1CS compiler 需要 PCS layer 也能 streaming commit/open。 | 不改变 KZG trusted setup、pairing assumptions 或安全边界；batch opening 和 stream order 是 Gemini-specific engineering/protocol details。 | [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] |
| Elastic multilinear KZG commitment/opening | 对 multilinear polynomial commitment，commitment 顺序扫描 vector/SRS streams；opening 用 multilinear decomposition 和 stack 合并相邻元素，小状态生成 `O(log N)` 个 witness group elements。 | Plonkish/HyperPlonk-style elastic SNARK 需要 multilinear PCS 也支持 streaming open/check。 | 保留 KZG trusted setup/pairing assumptions；需要有序 SRS/key streams；不自动解决 Plonkish lookup streaming。 | [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] |
| KZG-backed PLONK implementation | SparseR1CS trace、selector/permutation polynomials、quotient/linearized polynomial 和 batch opening 都通过 KZG SRS/commit/open/check 组织；setup 需要 canonical 与 Lagrange SRS。 | PLONK backend implementation needs trusted/setup SRS provenance and efficient polynomial commitments. | 这是 gnark 的 implementation usage extension；不替代 KZG foundation，也不说明所有 PLONK implementations 都有相同 API/serialization/security boundary。 | [[consensys-gnark-master|Consensys/gnark]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials|Constant-Size Commitments to Polynomials and Their Applications]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | paper | 作为 usage source extension：把 KZG 扩展到 distributed bivariate commitment/opening for Pianist | 不替代 KZG foundation；具体 DKZG 留在 source note | `§4.2`, `p9-p11` |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | paper | 作为 usage source extension：KZG commitments 支撑 committed-data FDE 和 subset retrieval | 不替代 KZG foundation；VECK/FDE 细节留在 source note 与 fair-data-exchange 节点 | `§1`, `§5.1-§5.3` |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel: Distributed Privacy-Preserving zkSNARK]] | paper | 作为 usage source extension：KZG commitments/openings 支撑 WCC/PCC，让私有委托证明服务器输出保持一致 | 不替代 KZG foundation；一致性检查语义依赖 Siniel protocol | `§4.3-§4.6`, `§5` |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS: Efficient Private Delegation of zkSNARK Provers]] | paper | 作为 usage source extension：KZG-style PC operations and openings support efficient delegated PIOP prover circuits and consistency checking | 不替代 KZG foundation；delegator 在线检查和 MARLIN/arkworks 实现细节留在 source note | `§4-§6`, Appendix B |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | paper | 作为 usage source extension：KZG commitments/openings 可被 streaming realized，成为 elastic SNARK compiler 的 PCS 层 | 不替代 KZG foundation；低内存 SNARK 还依赖 elastic PIOP/streaming R1CS | `§2.3`, `§9`, `§10` |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle: Elastic Succinct Arguments for Plonk Constraint System]] | paper | 作为 usage source extension：multilinear KZG 可以被 streaming commit/open，成为 elastic Plonkish SNARK 的 PCS 层 | 不替代 KZG foundation；低内存 Plonkish SNARK 还依赖 streaming HyperPlonk PIOP toolbox | `§2`, `§6`, `§7` |
| [[consensys-gnark-master|Consensys/gnark]] | GitHub repository | 作为 usage source extension：PLONK backend 使用 KZG SRS、trace commitments、quotient/linearized polynomial 和 batch openings | 不替代 KZG foundation；production SRS provenance、serialization compatibility 和 backend-specific details 留在 source note | `backend/plonk/plonk.go`; `backend/plonk/bn254/setup.go`; `backend/plonk/bn254/prove.go`; `backend/plonk/bn254/verify.go` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-24`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-24`。
- 综合: KZG 是 PCS 的代表实例，效率好但带来 setup/trust/pairing 假设边界。Pianist 说明 KZG 的 quotient/opening intuition 可被扩展到 distributed bivariate setting，支持多机 Plonk proving；Atomic/Fair Data Exchange 说明 KZG 的 succinct commitment、batch opening 和 subset opening 可作为 committed-data exchange 的 correctness anchor；EOS 与 Siniel 说明 KZG/PCS commitments/openings 还可作为 private delegated proving 的 consistency-binding layer，约束 secret-shared witness 与 PIOP oracle state；Gemini 说明 KZG commitment/opening 能被 streaming realized，作为 R1CS elastic SNARK 的 PCS layer；Epistle 说明 multilinear KZG 也能被 streaming realized，作为 Plonkish/HyperPlonk elastic SNARK 的 PCS layer。这些都是 usage extensions: DKZG/FDE/EOS-Siniel delegated checks/elastic KZG/elastic multilinear KZG 不替代 KZG foundation，也不把 KZG 变成完整 proof-system、fairness mechanism、delegated-proving protocol 或通用低内存 SNARK 定理。
- Repository implementation update: [[consensys-gnark-master|Consensys/gnark]] 补充 KZG-backed PLONK implementation evidence：PLONK setup 需要 canonical/Lagrange SRS，setup/prove/verify 围绕 trace commitments、quotient/linearized polynomial 和 batch openings；这是 KZG usage extension，不替代 KZG foundation。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository evidence now includes gnark's KZG-backed PLONK implementation, but cross-implementation KZG trends still need broader repo/standard refresh.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials|Constant-Size Commitments to Polynomials and Their Applications]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | usage source extension | DKZG/bivariate KZG for distributed proof generation | 方法族与解决路线; 代表 Sources; 当前综合 | no | do not split DKZG until more sources require it |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | usage source extension + bridge trigger | KZG commitments as committed-data correctness anchor for VECK/FDE and selective retrieval | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route protocol details through [[fair-data-exchange|Fair data exchange for committed data]] |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel: Distributed Privacy-Preserving zkSNARK]] | usage source extension + bridge trigger | KZG commitments/openings as witness/PIOP consistency checker substrate for private delegated proving | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route delegated-proving details through [[private-delegated-proving|Private delegated proving]] |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS: Efficient Private Delegation of zkSNARK Provers]] | usage source extension + bridge trigger | KZG-style PC circuits and openings as PIOP consistency-check substrate for delegated SNARK proving | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route delegated-proving details through [[private-delegated-proving|Private delegated proving]] |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | usage source extension + bridge trigger | KZG commitment/opening as streaming PCS layer for elastic SNARKs | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route low-memory proof-system details through [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle: Elastic Succinct Arguments for Plonk Constraint System]] | usage source extension + bridge trigger | multilinear KZG commitment/opening as streaming PCS layer for elastic Plonkish SNARKs | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route low-memory proof-system details through [[elastic-snarks|Elastic SNARKs]] |
| [[consensys-gnark-master|Consensys/gnark]] | usage source extension | KZG SRS, trace commitments and batch openings in a production PLONK backend implementation | 方法族与解决路线; 代表 Sources; 当前综合 | no | route implementation details through source note; compare with other PLONK/KZG implementations before splitting a child node |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-proof-generation-to-zkrollups|Distributed proof generation -> zkRollup prover scaling]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation; zero-knowledge-proofs/applications/blockchain-applications` | implementation_reuse | DKZG is a mechanism in the distributed-proving endpoint, not the whole bridge. | active_seed |
| [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments; blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | dependency, application, cryptographic_enabler | KZG supplies commitment/opening semantics; VECK and blockchain payment/key-release supply data privacy before payment and fairness. | active_seed |
| [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving; zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | dependency, verification_enabler, implementation_reuse, privacy_preserving_delegation | KZG supplies binding/opening checks for consistency; witness privacy, share authentication and server execution model remain delegated-proving protocol details. | active_seed |
| [[memory-efficient-snarks-to-kzg-commitments|Memory-efficient SNARKs -> KZG commitments]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | dependency, method_transfer, implementation_reuse, prover_space_reduction | KZG supplies a streaming commitment/opening layer for Gemini-style R1CS elastic SNARKs and Epistle-style Plonkish elastic SNARKs; low-memory proving still depends on elastic PIOP and streamable constraint-system data. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-kzg-commitments | is_a | nahida-knowledge-polynomial-commitments | vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments/kzg-commitments.md; vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments.md | medium | active_seed |
| nahida-knowledge-kzg-commitments | evidenced_by | vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md | vault/03_Sources/papers/doi-10-1007-978-3-642-17373-8-11-constant-size-commitments-to-polynomials.md | medium | active_seed |
| nahida-knowledge-kzg-commitments | evidenced_by | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | medium | active_seed |
| nahida-knowledge-kzg-commitments | evidenced_by | vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md | FDE source note | high | active_seed |
| nahida-knowledge-kzg-commitments | bridges_to | nahida-bridge-kzg-commitments-to-fair-data-exchange | bridge note | high | active_seed |
| nahida-knowledge-kzg-commitments | evidenced_by | vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md | Siniel source note | high | active_seed |
| nahida-knowledge-kzg-commitments | evidenced_by | vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md | EOS source note | medium | active_seed |
| nahida-knowledge-kzg-commitments | bridges_to | nahida-bridge-private-delegated-proving-to-kzg-commitments | bridge note | high | active_seed |
| nahida-knowledge-kzg-commitments | evidenced_by | vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md | Gemini source note | high | active_seed |
| nahida-knowledge-kzg-commitments | bridges_to | nahida-bridge-memory-efficient-snarks-to-kzg-commitments | bridge note | high | active_seed |
| nahida-knowledge-kzg-commitments | evidenced_by | vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md | Epistle source note; elastic multilinear KZG route | high | active_seed |
| nahida-knowledge-kzg-commitments | evidenced_by | vault/03_Sources/github/consensys-gnark-master.md | gnark PLONK KZG SRS/commit/open implementation route | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| KZG 在 PLONK/DA 中的现代使用、trusted setup ceremonies、IPA/FRI 对照仍薄。 | gnark 已补 PLONK/KZG implementation evidence；foundation 和 cross-implementation comparison 仍需更多 sources。 | nahida-research-search or nahida-update | medium | queued |
| DKZG/bivariate KZG 目前只有 Pianist usage source。 | 需要更多来源才能判断是否拆成独立子节点。 | nahida-update / nahida-research-search | medium | review |
| KZG-backed fair exchange 目前只有 FDE seed。 | SAVER 已补足 generic verifiable-encryption seed；仍需 ZKCPlus/VECK/KZG-specific sources 校准 KZG-backed fair exchange 的方法族边界。 | nahida-update | medium | queued |
| KZG-backed delegated-proving consistency checking 目前只有 EOS + Siniel seeds。 | 需要 zkSaaS/collaborative zkSNARKs 或 non-KZG delegated-proving sources 作为对照，避免把 EOS/Siniel 的 checker 设计误当成领域通用定理。 | nahida-update / nahida-research-search | medium | queued |
| Elastic KZG 目前只有 Gemini + Epistle KZG-family seeds。 | 需要 DARK/IPA/FRI 或其他 PCS low-memory route 对照，避免把 KZG-specific streaming 方法误当成所有 PCS 的结论。 | nahida-update / nahida-research-search | medium | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 3 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Added DKZG/bivariate KZG usage extension from Pianist. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-atomic-fair-data-exchange | Added KZG-backed committed-data FDE usage extension and bridge. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-siniel-private-delegated-proving | Added KZG-backed consistency-check usage extension and bridge to private delegated proving. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-eos-private-delegated-proving | Added EOS KZG/PCS consistency-check usage extension to private delegated proving bridge. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-gemini-elastic-snarks | Added elastic KZG usage extension and bridge to memory-efficient SNARKs. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-epistle-elastic-snarks | Added elastic multilinear KZG usage extension from Epistle for Plonkish elastic SNARKs. | 1 source note | codex |
| 2026-06-24 | nahida-knowledge-20260624-consensys-gnark | Added gnark PLONK/KZG implementation usage extension. | 1 source note | codex |
