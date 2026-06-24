---
id: "nahida-knowledge-memory-efficient-snarks"
title: "Memory-efficient SNARKs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "memory-efficient-snarks"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs:
  - "nahida-knowledge-elastic-snarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "memory-efficient-snarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
secondary_ontology_paths:
  - "zero-knowledge-proofs/recursion-and-folding/folding-schemes"
relation_edges:
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "has_child"
    to: "nahida-knowledge-elastic-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks/elastic-snarks.md"
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "uses"
    to: "nahida-knowledge-folding-schemes"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
      - "vault/05_Bridges/folding-schemes-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "uses"
    to: "nahida-knowledge-sum-check-protocol"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
      - "vault/05_Bridges/sum-check-protocol-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "uses"
    to: "nahida-knowledge-kzg-commitments"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
      - "vault/05_Bridges/memory-efficient-snarks-to-kzg-commitments.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-folding-schemes-to-memory-efficient-snarks"
    evidence_refs:
      - "vault/05_Bridges/folding-schemes-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
    evidence_refs:
      - "vault/05_Bridges/sum-check-protocol-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-verifiable-ml-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-distributed-proof-generation.md"
      - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
      - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-memory-efficient-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-transparent-polynomial-commitments"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-transparent-polynomial-commitments.md"
      - "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-folding-schemes-to-memory-efficient-snarks"
  - "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
  - "nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training"
  - "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
  - "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
  - "nahida-bridge-memory-efficient-snarks-to-transparent-polynomial-commitments"
source_note_refs:
  - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
  - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
  - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
  - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
  - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
  - "vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md"
representative_source_refs:
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "doi:10.1145/3658644.3690318"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "doi:10.1109/TC.2023.3235975"
  - "iacr:2024/872"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
  - "sha256:51c6a37d5caa894a133dae1ede4631ad35dc729675c6ac9a4caf00be5ecfc6ff"
query_keys:
  - "Memory-efficient SNARKs"
  - "memory-efficient-snarks"
  - "streaming SNARKs"
  - "low-memory SNARK prover"
  - "folding-based SNARKs"
  - "Mangrove"
  - "two-pass SNARK prover"
  - "Sparrow"
  - "space-efficient zkSNARKs"
  - "space-efficient sumcheck"
  - "data-parallel circuits"
  - "Gemini"
  - "elastic SNARKs"
  - "streaming R1CS"
  - "elastic prover"
  - "ark-gemini"
  - "Split"
  - "n-Split"
  - "Good Split"
  - "R1CS circuit partitioning"
  - "hash-bound subcircuits"
  - "Epistle"
  - "elastic Plonk"
  - "HyperPlonk elastic prover"
  - "streaming multivariate PIOP"
  - "elastic multilinear KZG"
  - "Yoimiya"
  - "serializable ZK-SNARK"
  - "CDG circuit partitioning"
  - "HOBBIT"
  - "transparent space-efficient zkSNARK"
  - "post-quantum space-efficient zkSNARK"
  - "optimal-time space-efficient zkSNARK"
aliases:
  - "streaming SNARKs"
  - "low-memory SNARKs"
  - "folding-based SNARKs"
  - "prover-memory-efficient SNARKs"
  - "elastic SNARKs"
domains:
  - "zero-knowledge-proofs"
topics:
  - "memory-efficient-snarks"
  - "folding-schemes"
  - "proof-carrying-data"
  - "sum-check-protocol"
  - "data-parallel-circuits"
  - "verifiable-ml-training"
  - "elastic-snarks"
  - "streaming-r1cs"
  - "kzg-commitments"
  - "front-end-circuit-partitioning"
  - "hash-bound-subcircuits"
  - "plonkish-snarks"
  - "hyperplonk"
  - "multivariate-piop"
  - "multilinear-kzg"
  - "scalable-proof-generation"
  - "serializable-zksnarks"
  - "transparent-polynomial-commitments"
  - "post-quantum-zksnarks"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-mangrove"
  - "nahida-knowledge-20260620-sparrow-space-efficient-snarks"
  - "nahida-knowledge-20260622-gemini-elastic-snarks"
  - "nahida-knowledge-20260622-split-hash-memory-optimization"
  - "nahida-knowledge-20260623-epistle-elastic-snarks"
  - "nahida-knowledge-20260623-scalable-zkp-generation"
  - "nahida-knowledge-20260623-hobbit-space-efficient-zksnark"
source_refs:
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "doi:10.1145/3658644.3690318"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "doi:10.1109/TC.2023.3235975"
  - "iacr:2024/872"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
  - "sha256:51c6a37d5caa894a133dae1ede4631ad35dc729675c6ac9a4caf00be5ecfc6ff"
confidence: "high"
trust_tier: "primary"
---

# Memory-efficient SNARKs

## 定义与范围

- 定义: Memory-efficient SNARKs 研究如何在保持 succinct verification 的同时降低 SNARK prover 的 peak memory、全局数据持有需求、pass 数或单机资源门槛。
- 不包含: 单篇系统名、单个性能数字、proof aggregation 的全部问题、distributed prover network economics 或某个实现的 worker scheduler。Mangrove、Gemini、DARK、Nova-UC 等应作为代表来源或方法路线，而不是本节点本体。
- Canonical terms: `memory-efficient-snarks`, `streaming SNARKs`, `low-memory SNARKs`, `elastic SNARKs`
- Aliases/query keys: Mangrove, folding-based SNARKs, two-pass SNARK prover, Gemini, elastic SNARKs, streaming R1CS, prover memory
- Standalone completeness check: 本节点本地解释低内存 SNARK 的问题、边界、方法路线、代表 source、桥接和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“SNARK prover 太占内存怎么办”“Mangrove 属于什么问题层”“folding 如何构造低内存 SNARK”时先读本节点。
- Update scope: 新 source 若提出 streaming/low-memory SNARK、改变 pass/memory/prover-time tradeoff、补充 Gemini/DARK/Spartan/Nova-UC/Mangrove comparisons 或生产实现证据，应刷新本节点。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

zk-SNARK 的 verifier 端短 proof/低验证成本并不自动意味着 prover 端便宜。monolithic SNARK 往往需要持有完整 witness/trace，并执行全局多项式、FFT/MSM 或 proximity-proof 类操作；当电路扩大到数千万或数十亿 gates，peak memory 和数据遍历成为瓶颈。低内存 SNARK 路线试图把 prover 工作变成 streaming、chunked、piecewise 或 foldable 的结构。

model_prior_background: 这个问题与 [[distributed-proof-generation|Distributed proof generation]] 相邻但不同。低内存 SNARK 可以在单机上通过 streaming/chunking/folding/sumcheck-GKR specialization 降低 peak memory；distributed proof generation 则把工作分给多机。它也不同于 [[snark-proof-aggregation|SNARK proof aggregation]]，后者关注多个已有 proofs 的 verifier-cost/proof-size 压缩。

Gemini 新增的约束是“弹性”: 同一个 proof/verifier interface 下，prover 可以选择线性时间/线性内存配置，或用更多 passes 与准线性时间换取对数 working memory。这个路线要求 PIOP、R1CS 输入模型和 polynomial commitment/opening 层都支持 streaming，而不只是把某个 prover loop 改成 iterator。

Epistle 新增的约束是“Plonkish 弹性”: Gemini 证明了 R1CS route，Epistle 则把 HyperPlonk 的 multivariate PIOP toolbox 逐个重写到 streaming model，并配套 elastic multilinear KZG，使 Plonk constraint system 也能在同一 proof/verifier interface 下提供 time-efficient 与 space-efficient prover。它说明 elastic SNARKs 已经不只是单篇 Gemini 的 R1CS 技巧，而是可迁移的方法族。

Split 新增的约束更靠近 zk-SNARK front-end: R1CS/arithmetic-circuit 会保留 loop unrolling 产生的所有中间变量，因此可以在电路层把 obsolete variables 所在区间切开，用 hash digest 绑定跨切分 state，让 prover 顺序证明多个子电路而不是一次持有完整电路 witness。它是单机 memory reduction route，不是 cluster/distributed proving route。

HOBBIT 新增的约束是“通用算术电路上的透明/PQ 低内存路线”: 它不沿 Gemini/Epistle 的 KZG elastic route，而是同时重做 product-form streaming sumcheck、transparent plausibly post-quantum multilinear PCS、execution-trace streaming access 和 memory-checking wiring consistency，使通用 arithmetic circuit route 也能达到 `O(|C|)` prover time 与 `O(B+S_eval)` total space。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它不等于 Mangrove。它组织 prover memory、pass complexity、streaming commitments、PCD/folding、universal-circuit IVC、proof compression 等路线，未来可承接 Gemini、DARK、Spartan、Nova-UC、Mangrove 和生产 prover sources。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Mangrove 是当前代表 source；本节点组织的是“证明系统如何降低 prover memory”这一类可复用问题。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[zk-snarks|zk-SNARKs]], [[folding-schemes|Folding schemes]], [[polynomial-commitments|Polynomial commitments]]。
- 不应拆出的实例/协议/来源: Mangrove、Mangrove-Basic、Mangrove-Tree、Nova-UC、Gemini 等默认是 route/source instance；只有积累多来源和重复查询后才考虑更细 child node。

## 解决的问题

Memory-efficient SNARKs 解决的是 prover-side resource bottleneck:

- 大电路 proof 需要完整 computation trace，单机内存不足。
- 全局 FFT/MSM/commitment/opening 需要多次读取或保留大数组。
- streaming/chunking 降低内存后可能增加 pass 数或 prover time。
- piecewise/recursive/IVC 路线降低内存，但可能引入 universal circuit overhead、递归关系开销或安全模型限制。
- 低内存同时还要保持 proof size、verifier work 和 CRS/setup 在可接受范围内。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of / problem_of | Mangrove source absorption and proof-system resource axis | active_seed |
| [[zk-snarks|zk-SNARKs]] | depends_on | Memory-efficient SNARKs optimize the SNARK prover side while preserving succinct verification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| streaming polynomial-commitment SNARKs | route section | Sparrow deep read adds data-parallel streaming/GKR evidence; Gemini adds R1CS elastic PIOP + elastic KZG evidence, but DARK/Spartan primary comparisons still need absorption before splitting further | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]]; [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] | active_seed |
| transparent/PQ streaming SNARKs for general arithmetic circuits | route section | HOBBIT adds a non-KZG transparent and plausibly post-quantum route with optimal prover time for arbitrary arithmetic circuits; keep as route section until more transparent/PQ low-memory sources are absorbed. | [[sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time|HOBBIT]] | active_seed |
| [[elastic-snarks|Elastic SNARKs]] | method_family | Gemini + Epistle now provide two source-backed routes, R1CS and Plonkish/HyperPlonk, under the same proof/verifier-interface elasticity idea. This is stable enough to split below the parent problem node. | [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]]; [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] | active_seed |
| front-end circuit partitioning with hash binding | route section | SPLITA adds a R1CS/front-end route: split a large circuit into sequential subcircuits and bind intermediate state with hash circuits. It is useful as a route row, while `Split` itself remains a source instance. | [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] | active_seed |
| folding-based low-memory SNARKs | route section | Mangrove 已提供深读 source，但目前单 source，不拆 child | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] | active_seed |
| universal-circuit IVC SNARKs | candidate route | Nova-UC 等需要 source 校准 | Mangrove related work only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Chunked/streaming polynomial commitments | 将全局多项式承诺或 opening 工作拆成多次读取/小内存状态。 | prover memory 是瓶颈，允许更多 passes 或额外 prover time。 | Gemini 已补 KZG streaming route；DARK/Spartan 等 non-KZG primary sources 仍缺，不能只凭 related work 定论。 | [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] |
| Elastic SNARKs / streaming R1CS and Plonkish PIOP | 在同一 proof/verifier interface 下提供 time-efficient 与 space-efficient prover 配置；Gemini 给出 R1CS route，Epistle 给出 Plonk/HyperPlonk route。 | R1CS 或 Plonkish trace/index/witness 能以 stream 形式产生或重放；PIOP 与 PCS layer 都支持 streaming commit/open/message generation。 | space-efficient prover 用 `O(log N)` working memory 但增加 passes/time；KZG trusted setup/pairing assumptions 保留；Epistle 暂未解决一般 lookup streaming；应用端 trace generation 可能仍耗内存。 | [[elastic-snarks|Elastic SNARKs]]; [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]]; [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] |
| Universal-circuit / CPU-style IVC | 把计算分成多步机器执行，用 IVC 避免一次持有完整 trace。 | 计算能表达成统一 step function。 | universal circuit overhead；Mangrove 指出 Nova-UC 只适合 constant-length security model。 | Mangrove related-work discussion |
| Uniform compiler + folding PCD | 利用 Plonkish trace 的规则结构，把 NP statement 编译成 uniform chunks；PCD tree 合并 chunks；folding 维护 leaf relation。 | 目标 computation 可被 Plonkish/chunked 表达；可接受 folding/PCD assumptions。 | recursive control overhead 需要 decoupling；commitment opening constraints 需要 commit-and-fold 避免膨胀。 | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] |
| Commit-and-fold | 在 committed values 上折叠 polynomial relation，避免把 commitment openings 编进递归电路。 | commitment map 是 binding/linear，leaf relation 可表示为 polynomial map。 | 依赖 specific commitment/folding scheme；standard-model folding for PCD 有 heuristic step。 | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] |
| Proof wrapping/compression | 先得到较大的 low-memory proof，再用另一个 SNARK 压缩 proof size。 | raw proof size 可接受但最终 verifier/proof size 需要更小。 | 增加 compression prover step；不改变原 prover low-memory construction 本身。 | Mangrove with Spartan compression |
| Data-parallel streaming GKR/SNARKs | 针对 layered data-parallel circuits，用 space-efficient sumcheck、streaming oracles、depth reduction 和 sublinear-parameter PC 降低 prover memory。 | computation can be represented as layered data-parallel arithmetic circuits. | 不支持任意/non-layered circuits；padding 可能增大电路；prover time can still be large. | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]] |
| Transparent/PQ optimal-time streaming SNARKs | 对通用 arithmetic circuit，从 evaluation trace 显式生成 proving-data stream；用 product-form optimal-time streaming sumcheck、transparent PQ multilinear PCS、memory-checking wiring consistency 和 lookup argument 组合成低内存 zkSNARK。 | 需要电路 evaluation algorithm 可在线重放，且应用接受 MB-level proof size 和较慢但实用的 verifier。 | proof size 明显大于 curve/KZG systems；formal proofs 在 full version；benchmark 单线程 CPU；transparent/PQ PCS route 尚需更多来源校准。 | [[sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time|HOBBIT]] |
| Front-end circuit partitioning / hash-bound sequential subcircuits | 在 R1CS/arithmetic-circuit 前端把大电路切成 `F1, F2, ... Fn`，只把跨切分中间变量 `m_i` 传递到下一段，并用 public hash `h_i=H(m_i)` 绑定 state，避免 obsolete variables 跨全程占用内存。 | 电路存在 Good Split: cross-cut state 很小，最大子电路明显小于原电路；loop/unrolled circuits 尤其适合。 | hash circuit 增加 constraints；proof/setup/verify steps 随 split number 增加；Good Split 搜索困难；实验主要是 loop proof-of-concept。 | [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] |
| Distributed proof generation | 多机分摊 prover work。 | 有多机资源和可分区 workload。 | 相邻问题，不等于低内存单机 SNARK；communication/worker trust 是主要边界。 | [[distributed-proof-generation|Distributed proof generation]] |

## 代表 Sources

| Source                                                                               | Source kind                                                                                                     | 贡献 delta | 假设/限制                                                                                                                                                    | Evidence anchors                                                                                                                                                           |                                                                                                                                                       |                                                                                                                                          |                            |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks               | Mangrove: A Scalable Framework for Folding-based SNARKs]]                                                       | paper    | 创建本问题节点；提出 uniform compiler、decoupled PCD、commit-and-fold，并估计 two-pass low-memory proving                                                                | 性能是估计/modified Nova benchmark；zero-knowledge 和 production implementation 边界未完整展开；canonical URL unknown                                                                     | `p1-p69`                                                                                                                                              |                                                                                                                                          |                            |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits | Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | paper    | 增加 data-parallel streaming/GKR route；提出 space-efficient sumcheck and Sparrow zkSNARK，并用 zkFTP 展示 ML training application                                 | limited to layered data-parallel circuits; single-thread benchmark; formal proofs in full version                                                                          | `p1-p15`                                                                                                                                              |                                                                                                                                          |                            |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments                 | Gemini: Elastic SNARKs for Diverse Environments]]                                                               | paper    | 增加 elastic SNARK / streaming R1CS route；说明 R1CS SNARK 可在同一 proof interface 下支持线性内存或对数内存 prover；补足 elastic KZG 与 arkworks implementation evidence         | space-efficient route trades memory for quasi-linear time and multiple passes; streaming trace generation is an input-model assumption; KZG setup/trust assumptions remain | `Abstract`, `§2.1-§2.8`, `§4-§10`                                                                                                                     |                                                                                                                                          |                            |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark           | Split: A Hash-Based Memory Optimization Method for zk-SNARK]]                                                   | paper    | 增加 front-end circuit partitioning route；定义 Split/Good Split/n-Split，用 hash-bound intermediate variables 降低单机 prover peak memory                          | only works well for circuits with Good Split; SHA256 hash circuit overhead; proof/verify/setup scale with component count; proof-of-concept loop workload                  | `p1-p12`, Table II/III                                                                                                                                |                                                                                                                                          |                            |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system         | Epistle: Elastic Succinct Arguments for Plonk Constraint System]]                                               | paper    | 增加 elastic Plonkish / HyperPlonk route；把 SumCheck、ZeroCheck、product/permutation checks 与 multilinear KZG 都改造成 streaming prover，并把 elastic SNARKs 拆为独立方法族 | lookup protocol not generally streaming; fixed custom-gate degree; benchmark uses mock Plonk gates and one Rust/hardware setup                                             | `Abstract`, `§2`, `§4-§7`                                                                                                                             |                                                                                                                                          |                            |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing                  | 面向大规模计算的可扩展零知识证明生成方法]]                                                                                          | thesis   | 增加 CDG automatic circuit partitioning + polynomial-binding serial subproof route；将低内存路线放入更上层 [[scalable-proof-generation                                 | Scalable proof generation]] 问题节点。                                                                                                                                          | partition heuristic not globally optimal; serial proof verification overhead remains; implementation/evaluation are Gnark/Groth16/Plonk source-local. | Ch.3-Ch.5                                                                                                                                |                            |
| [[sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time             | Hobbit: Space-Efficient zkSNARK with Optimal Prover Time]]                                                      | paper    | 增加 transparent/PQ optimal-time route：通用 arithmetic circuit 上 `O(                                                                                         | C                                                                                                                                                                          | )` prover、`O(B+S_eval)` total space，并通过 lookup support 改善 AES/SQL/MLP workloads。                                                                      | proof size MB-level; verifier slower than curve/KZG routes but practical; full proofs in full version; single-thread benchmark evidence. | `Abstract`, Table 1, §3-§6 |

## 正反例约束

- 正确: 把 Mangrove 作为 low-memory/folding-based SNARK route 的代表 source。
- 正确: 把 `folding schemes -> memory-efficient SNARKs` 写成 bridge，而不是把两个方向合并。
- 正确: 与 [[distributed-proof-generation|Distributed proof generation]] 区分: 前者降低/组织单个 prover 的内存/pass，后者多机分摊 proving。
- 错误: 把 Mangrove 当作 proof aggregation source。它构造一个 SNARK for Plonkish NP statements，不是聚合多个已有 SNARK proofs。
- 错误: 用 Mangrove 的 related work 替代 Gemini/Spartan/DARK primary sources。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，覆盖当前 vault 已深读 Mangrove、Sparrow、Gemini、Split、Epistle、Ye 2026 和 HOBBIT。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: 当前节点已形成六条主要路线的低内存 SNARK 地图。Mangrove 说明 folding/PCD 可被重新定位为 low-memory SNARK construction mechanism。Sparrow 增加 data-parallel route: 对 layered data-parallel circuits，用 space-efficient sumcheck、space-efficient GKR、streaming oracles、depth reduction 和 sublinear-parameter PC，把 prover space 降到接近 `sqrt(|C|)+input/streaming space`。Gemini 与 Epistle 共同把 [[elastic-snarks|Elastic SNARKs]] 升级为独立方法族: Gemini 是 R1CS route，Epistle 是 Plonkish/HyperPlonk route；二者共同说明低内存 SNARK 需要 constraint-system streams、PIOP toolbox 和 PCS/opening layer 端到端支持 streaming，而不是只优化某个 prover loop。Split/Yoimiya 增加 front-end / serial partition routes。HOBBIT 则给出一个 sibling transparent/PQ route: 它不依赖 KZG SRS，而是重做 sumcheck、PCS 和 execution-trace streaming access，使 arbitrary arithmetic circuits 也能达到 `O(|C|)` prover time；代价是 MB-level proof size 和仍需更多 transparent/PQ PCS comparison evidence。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Academic focus summary: vault 当前有 Mangrove、Sparrow、Gemini、Split、Epistle deep-read sources，仍不能声称该问题的最新外部趋势。
- Industrial focus summary: Gemini 提供 arkworks/Rust implementation 与单机大规模 R1CS benchmark evidence，但 production deployment / current repository state 未联网复核。
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: Gemini/DARK/Spartan/Nova-UC/Mangrove implementation or production prover source.

## Source Extensions

| Source                                                                               | 新增/修正内容                                                                                                         | 影响的章节                                                                                                                                                                                                         | 是否改变上层结构                                                                                | Next action                                               |                                                                                                     |                                                                  |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks               | Mangrove: A Scalable Framework for Folding-based SNARKs]]                                                       | 创建 memory-efficient SNARKs 问题节点；补充 uniform compiler、decoupled PCD、commit-and-fold、performance estimates                                                                                                       | 定义; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links                                            | yes                                                       | 吸收 Spartan/DARK/PCD primary sources 后校准                                                             |                                                                  |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits | Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | 增加 data-parallel streaming/GKR route；补充 space-efficient sumcheck、Kopis PC、zkFTP application evidence                                                                                                          | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links                                                | yes                                                       | 吸收 Ligetron/GKR primary sources 后校准                                                                 |                                                                  |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments                 | Gemini: Elastic SNARKs for Diverse Environments]]                                                               | 增加 elastic SNARK / streaming R1CS route；补充 elastic KZG、tensor/scalar-product protocols、arkworks implementation 和单机大规模 R1CS evaluation evidence                                                                | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links; 缺口与队列                                     | yes                                                       | 吸收 DARK/Spartan/Ligetron 和 PCS comparison sources 后校准                                               |                                                                  |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark           | Split: A Hash-Based Memory Optimization Method for zk-SNARK]]                                                   | 增加 front-end circuit partitioning / hash-bound sequential subcircuits route；补充 Good Split/n-Split、single-machine proof memory benchmark 和与 DIZK cluster route 的边界                                             | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links; 缺口与队列                               | yes                                                       | 吸收 R1CS/arithmetization foundation、SNARK-friendly hash 和 circuit partitioning follow-up sources 后校准 |                                                                  |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system         | Epistle: Elastic Succinct Arguments for Plonk Constraint System]]                                               | 增加 elastic Plonkish/HyperPlonk route；将 Gemini+Epistle 提升为 [[elastic-snarks                                                                                                                                    | Elastic SNARKs]] 子方法族；补充 streaming multivariate PIOP 与 elastic multilinear KZG evidence | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links; 缺口与队列 | yes                                                                                                 | 补 PLONK/HyperPlonk foundation 和 streaming lookup primary sources |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing                  | 面向大规模计算的可扩展零知识证明生成方法]]                                                                                          | 增加 automatic circuit partitioning / serializable zk-SNARK route；把 Split 的 hash-bound partitioning 与 Yoimiya 的 polynomial-binding partitioning 作为相邻低内存证明生成路线区分。                                                | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links                                          | yes                                                       | 后续分析 Yoimiya repo/arXiv 后复核工程边界                                                                     |                                                                  |
| [[sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time             | Hobbit: Space-Efficient zkSNARK with Optimal Prover Time]]                                                      | 增加 transparent/PQ optimal-time streaming route；补充 product-form sumcheck、transparent multilinear PCS、execution-trace streaming oracle、memory-checking wiring consistency 和 lookup-enabled evaluation evidence。 | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links; 缺口与队列                               | yes                                                       | 补 WHIR/Brakedown/Orion/Lasso/lookup foundation sources 后校准                                          |                                                                  |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[folding-schemes-to-memory-efficient-snarks|Folding schemes -> memory-efficient SNARKs]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | application, method_transfer, performance_compression, dependency | Folding/PCD 可迁移为 low-memory SNARK construction route；具体 arithmetization、commitment map、PCD overhead、heuristic standard-model assumptions 不自动迁移。 | active_seed |
| [[sum-check-protocol-to-memory-efficient-snarks|Sum-check protocol -> memory-efficient SNARKs]] | `verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | dependency, method_transfer, prover_space_reduction, implementation_reuse | Space-efficient sumcheck transfers to low-memory GKR/SNARK construction; it does not by itself provide non-interactivity or commitments. | active_seed |
| [[memory-efficient-snarks-to-verifiable-ml-training|Memory-efficient SNARKs -> verifiable ML training]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/zkml/verifiable-training` | application, scalability_enabler, privacy, implementation_reuse | Low-memory proving transfers to large-dataset training certification; ML fairness, data legality and model quality do not. | active_seed |
| [[memory-efficient-snarks-to-kzg-commitments|Memory-efficient SNARKs -> KZG commitments]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | dependency, method_transfer, implementation_reuse, prover_space_reduction | KZG commit/open can be realized as a streaming PCS layer for Gemini-style elastic SNARKs; KZG trusted setup/pairing assumptions and batch-opening details do not become general low-memory SNARK properties. | active_seed |
| [[memory-efficient-snarks-to-distributed-proof-generation|Memory-efficient SNARKs -> Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/proof-systems/distributed-proof-generation` | contrast, shared_bottleneck, scalability_alternative | Both address prover-side time/memory bottlenecks; Split/Sparrow/Gemini/Mangrove reduce single-prover peak memory or passes, while DIZK/Pianist/Hekaton distribute work across machines/participants. Worker trust, communication and cluster economics do not transfer to single-machine low-memory SNARKs. | active_seed |
| [[memory-efficient-snarks-to-transparent-polynomial-commitments|Memory-efficient SNARKs -> transparent polynomial commitments]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/polynomial-commitments` | dependency, method_transfer, transparent_commitment_route, post_quantum_candidate | HOBBIT shows a transparent/PQ PCS can support low-memory SNARK construction; PCS alone does not provide circuit streaming, lookup support or small proof size. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-memory-efficient-snarks | is_a | nahida-knowledge-proof-systems | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md; vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | depends_on | nahida-knowledge-zk-snarks | Mangrove SNARK construction | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | uses | nahida-knowledge-folding-schemes | Mangrove §4-§6; bridge | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | has_child | nahida-knowledge-elastic-snarks | Gemini + Epistle source notes | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | uses | nahida-knowledge-sum-check-protocol | Sparrow §3; Gemini scalar/tensor protocols; Epistle §4 | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | uses | nahida-knowledge-kzg-commitments | Gemini §2.3, §9; Epistle §6; bridge | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | evidenced_by | vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md | full source note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md | source note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | evidenced_by | vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md | source note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md | source note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | evidenced_by | vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md | source note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | evidenced_by | vault/03_Sources/papers/sha256-51c6a37d5caa-hobbit-space-efficient-zksnark-optimal-prover-time.md | source note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | bridges_to | nahida-bridge-folding-schemes-to-memory-efficient-snarks | bridge note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | bridges_to | nahida-bridge-sum-check-protocol-to-memory-efficient-snarks | bridge note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | bridges_to | nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training | bridge note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | bridges_to | nahida-bridge-memory-efficient-snarks-to-kzg-commitments | bridge note | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | bridges_to | nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation | bridge note; Split and DIZK source notes | high | active_seed |
| nahida-knowledge-memory-efficient-snarks | bridges_to | nahida-bridge-memory-efficient-snarks-to-transparent-polynomial-commitments | bridge note; HOBBIT source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| DARK/Spartan/Gemini-adjacent PCS primary comparisons 缺。 | Gemini 已补；仍需校准 transparent/streaming/monolithic route 与 PCS tradeoff。 | nahida-update or nahida-research-search | medium | queued |
| Spartan/DARK primary sources 缺。 | 需要校准 monolithic/transparent/streaming tradeoff。 | nahida-update or nahida-research-search | medium | queued |
| Proof-Carrying Data primary sources 缺。 | Mangrove PCD 优化依赖 PCD foundation。 | nahida-update or nahida-research-search | high | foundation_gap |
| Plonk/Plonkish arithmetization foundation 缺。 | Mangrove 的 uniform compiler 依赖 Plonkish structure。 | nahida-update or nahida-research-search | high | foundation_gap |
| Production implementation evidence 缺。 | Mangrove 性能是 estimate，不足以回答生产部署。 | nahida-github-repo-analyze or nahida-research-search | medium | queued |
| Ligetron/Sparrow/Gemini related routes 缺 cross-primary comparison。 | 需要比较 RAM、R1CS/arithmetic-circuit、data-parallel circuit 的 space model 差异；Gemini 原文已补但横向对照仍薄。 | nahida-update / nahida-research-search | high | queued |
| Streaming lookup for Plonkish elastic SNARKs 缺 primary source。 | Epistle 明确留下 lookup protocol 在 limited space 下的 open problem，影响 elastic Plonkish route 的完整性。 | nahida-research-search / nahida-update | high | open_problem |
| Good Split finding / circuit partitioning follow-up sources 缺。 | Split 说明找到 Good Split 很难；需要后续算法/工具/编译器 source 才能回答 arbitrary circuit 是否可自动低内存切分。 | nahida-research-search / nahida-update | medium | queued |
| SNARK-friendly hash choices for Split route 缺 primary comparison。 | Split 使用 SHA256 proof-of-concept，并建议 MiMC/Poseidon；需要 hash-circuit cost/source 才能判断 route 可迁移性。 | nahida-research-search / nahida-update | medium | queued |
| Streaming/elastic/transparent PCS comparison sources 缺。 | Gemini/Epistle 给出 KZG route，HOBBIT 给出 transparent/PQ route，但仍需 WHIR/Brakedown/Orion/FRI/IPA/DARK primary sources 校准边界。 | nahida-update / nahida-research-search | high | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-mangrove | Created memory-efficient SNARKs problem node from Mangrove and connected it to folding schemes through a bridge. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-sparrow-space-efficient-snarks | Added data-parallel streaming/GKR route from Sparrow and connected memory-efficient SNARKs to sum-check and verifiable ML training. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-gemini-elastic-snarks | Added Gemini elastic SNARK / streaming R1CS route and bridged low-memory SNARKs to KZG commitments. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-split-hash-memory-optimization | Added Split front-end circuit partitioning route and bridged low-memory SNARKs to distributed proof generation as an alternative prover-scalability path. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-epistle-elastic-snarks | Added Epistle Plonkish/HyperPlonk elastic route and split [[elastic-snarks|Elastic SNARKs]] into a child method-family node. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-scalable-zkp-generation | Added Ye 2026 as automatic partitioning / polynomial-binding serial proof route and connected it to [[scalable-proof-generation|Scalable proof generation]]. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-hobbit-space-efficient-zksnark | Added HOBBIT transparent/PQ optimal-time low-memory zkSNARK route and bridge to polynomial commitments. | 1 source note | codex |
