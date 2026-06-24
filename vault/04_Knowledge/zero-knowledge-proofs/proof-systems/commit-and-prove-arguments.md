---
id: "nahida-knowledge-commit-and-prove-arguments"
title: "Commit-and-prove arguments"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "commit-and-prove-arguments"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "commit-and-prove-arguments"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/modular-zksnarks"
  - "zero-knowledge-proofs/proof-systems/floating-point-snarks"
  - "blockchain-systems/execution-and-transactions/fair-exchange-protocols"
relation_edges:
  - from: "nahida-knowledge-commit-and-prove-arguments"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/commit-and-prove-arguments.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-commit-and-prove-arguments"
    relation: "used_in"
    to: "nahida-knowledge-modular-zksnarks"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-commit-and-prove-arguments"
    relation: "applies_to"
    to: "nahida-knowledge-blockchain-fair-exchange-protocols"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
      - "vault/05_Bridges/commit-and-prove-arguments-to-fair-exchange-protocols.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-commit-and-prove-arguments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-commit-and-prove-arguments"
    relation: "applies_to"
    to: "nahida-knowledge-floating-point-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
      - "vault/05_Bridges/commit-and-prove-arguments-to-floating-point-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-commit-and-prove-arguments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-commit-and-prove-arguments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-commit-and-prove-arguments"
    relation: "bridges_to"
    to: "nahida-bridge-commit-and-prove-arguments-to-distributed-proof-generation"
    evidence_refs:
      - "vault/05_Bridges/commit-and-prove-arguments-to-distributed-proof-generation.md"
      - "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
  - "nahida-bridge-qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove"
  - "nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks"
  - "nahida-bridge-commit-and-prove-arguments-to-distributed-proof-generation"
  - "nahida-bridge-commit-and-prove-arguments-to-scalable-proof-generation"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
  - "vault/03_Sources/papers/doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation.md"
  - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
  - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
  - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
  - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
  - "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
  - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
representative_source_refs:
  - "iacr:2019/142"
  - "doi:10.1109/SP.2015.23"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "doi:10.1145/3460120.3484558"
  - "doi:10.1145/3548606.3560653"
  - "doi:10.1145/3576915.3616621"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
query_keys:
  - "commit-and-prove"
  - "CP-NIZK"
  - "commit-and-prove arguments"
  - "commit-and-prove SNARKs"
  - "commit-carrying SNARKs"
  - "proof over committed witness"
  - "CPlink"
  - "floating-point commit-and-prove compiler"
  - "CP compiler for R1CS"
  - "commit-and-prove for distributed proof generation"
  - "commit-and-prove statement partitioning"
  - "Ou"
  - "Lian"
  - "polynomial binding shared variables"
  - "serializable ZK-SNARK consistency"
aliases:
  - "CP-NIZK"
  - "commit-and-prove NIZK"
  - "CP arguments"
  - "committed-value consistency interface"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
  - "blockchain-systems"
topics:
  - "commit-and-prove-arguments"
  - "modular-zksnarks"
  - "floating-point-snarks"
  - "fair-exchange-protocols"
  - "distributed-proof-generation"
  - "compiler-assisted-zkp-parallelization"
  - "scalable-proof-generation"
  - "consistency-binding"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-21"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcplus-fair-exchange"
  - "nahida-knowledge-20260623-succinct-zk-floating-point"
  - "nahida-knowledge-20260623-ou-zkp-parallelization"
  - "nahida-knowledge-20260623-scalable-zkp-generation"
source_refs:
  - "iacr:2019/142"
  - "doi:10.1109/SP.2015.23"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "doi:10.1145/3460120.3484558"
  - "doi:10.1145/3548606.3560653"
  - "doi:10.1145/3576915.3616621"
  - "sha256:dd9b5b3e54f932d9bc55148ccf408969c23c081980e9ffe5358fe052ffefab5a"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
confidence: "medium"
trust_tier: "primary"
---

# Commit-and-prove arguments

## 定义与范围

- 定义: Commit-and-prove arguments 是一类证明接口，证明者先对 witness 的一部分做 commitment，随后证明这些已承诺值和辅助 witness 一起满足某个关系；验证者检查 proof 时只看到 statement、commitment 和 proof。
- 不包含: 普通 commitment scheme、任意 NIZK、单篇 LegoSNARK/ZKCPlus/Geppetto 机制、某个 C++ implementation；这些留在更具体 source notes 或 source-extension 行。
- Canonical terms: `commit-and-prove`, `CP-NIZK`, `commit-and-prove SNARKs`, `commit-carrying`.
- Standalone completeness check: 本节点给出 CP 的定义、问题、方法路线、代表 sources、边界和 bridge；读者不需要先打开 LegoSNARK 或 ZKCPlus 才知道 CP 的基本作用。
- Retrieval role: 查询“证明承诺里的 witness 满足关系”“CPlink/commit-carrying/CP-NIZK 是什么”“ZKCPlus 为什么能组合 predicate”时优先读本节点。
- Update scope: 新 source 涉及 CP-SNARK、commit-carrying encryption、proof over committed witness、shared committed input、commitment-linking 或把 CP/R1CS 当作 compiler backend，应刷新本节点。

## 背景

许多 ZK 应用不是只证明一个封闭 circuit，而是需要把多个证明组件连接到同一份隐藏数据: 例如一个模块证明数据满足 predicate，另一个模块证明密文确实加密同一份数据，第三个模块证明两个子计算共享中间状态。直接把所有逻辑塞进一个大 circuit 会造成 CRS、proving time、工程复用和模块化问题。

Commit-and-prove 的抽象是把“隐藏值是什么”先绑定到 commitment，再让不同 proof 或 compiler-generated constraints 共同引用这些 commitment。这样，组合的安全性来自 proof soundness 加 commitment binding，而隐私来自 zero-knowledge 加 commitment hiding。Garg et al. 2022 进一步说明，CP 还可以作为 proof-system compiler 的后端接口: 先把 floating/fixed point approximate correctness 编译成 R1CS，再用 public-coin CP system 证明 committed witness 满足这些 constraints。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family`。
- 为什么足够通用: 它已跨 LegoSNARK、Geppetto、SAVER、Mangrove、ZKCPlus 和 Garg et al. 多个已吸收 source，用于模块化 SNARK、VC state sharing、verifiable encryption compatibility、low-memory witness reuse、fair exchange 和 floating-point proof compiler。
- 为什么不是单篇论文/单个协议的局部概念: LegoSNARK 是 CP-SNARK framework，ZKCPlus 是 CP-NIZK fair-exchange application，Geppetto 是 QAP/VC route，SAVER 是 encryption composition route；都不是 CP 的唯一含义。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[zk-snarks|zk-SNARKs]], Pedersen commitments/source-local definitions。
- 不应拆出的实例/协议/来源: CPlink、LegoAC1、ZKCPlus proof-of-delivery、Mangrove commit-and-prove extension 默认作为 method/source-extension，不单独成 foundation。

## 解决的问题

Commit-and-prove 解决的是 proof components 如何共享隐藏输入并保持一致:

- 同一个 hidden value 被多个关系引用时，验证者需要知道它们指向同一对象。
- 证明系统需要把外部 commitment 和内部 witness 绑定起来。
- 应用想把 predicate validation、delivery correctness、encryption consistency 或 state transition 分开证明。
- 需要在不公开 witness 的情况下组合不同 proof gadgets 或 different proof systems。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of | CP is a proof-system interface/method family | active_seed |
| [[zk-snarks|zk-SNARKs]] | adjacent method | many current sources use CP-SNARK or SNARK-compatible CP routes | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| `CP-SNARK / modular zkSNARK composition` | method section / sibling route | SNARK-specific modular composition is already organized by [[modular-zksnarks|Modular zkSNARKs]]. | LegoSNARK, Mangrove | keep_section |
| `data-parallel CP-NIZK` | method section | ZKCPlus provides one strong construction/application, but not enough independent sources for a child node. | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | keep_section |
| `commit-carrying encryption` | method section | SAVER exposes encryption/proof compatibility through commitment handles. | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] | keep_section |
| `proof-linking adapters` | method candidate | CPlink/interlinking functions recur across sources; may deserve a node after more direct sources. | LegoSNARK; ZKCPlus | watching |
| `distributed statement partitioning backend` | method section | Ou/Lian shows CP can be used as the consistency interface for compiler-generated substatements in distributed proving, but one source is not enough for a separate child node. | Ou §1.2, §2, §5-§6 | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| CP relation over committed witness | Witness splits into committed message and auxiliary witness; verifier checks commitment opening relation inside the proof. | Hidden values must be reused or externally committed. | Requires a binding/hiding commitment scheme compatible with proof assumptions. | [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]] |
| Commitment-linking / CPlink | Prove two commitments or two proof components refer to related hidden values. | Modular proof gadgets need shared witness or state consistency. | Linking relation can become the real bottleneck if not specialized. | [[modular-zksnarks|Modular zkSNARKs]] |
| QAP/VC state-sharing route | Use commitments/digests to connect sub-QAPs or scheduled proofs. | Verifiable computation systems with shared state/bus values. | Coupled to compiler/runtime and QAP-style representation. | [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto]] |
| Commit-carrying encryption | Ciphertext exposes a commitment-compatible handle so a proof can bind encrypted plaintext to a relation. | Encrypted witness or verifiable encryption applications. | Generic encryption does not automatically satisfy this interface. | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] |
| Data-parallel CP-NIZK | Commit row vectors for many identical sub-circuits and reduce constraints via inner-product arguments. | CTR encryption, CNN layers, SQL row predicates and other data-parallel workloads. | Public setup and prover efficiency improve, but proof size/verifier are not constant like Groth16. | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] |
| Committed witness reuse | Pull witness chunk commitments into the statement so proofs can be linked/reused. | Low-memory or folding-based SNARKs where witness chunks are natural boundaries. | Current evidence is source-local to Mangrove's extension. | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] |
| CP compiler backend | 把应用/算术语义先编译成 R1CS 和 committed witness relation，再调用 public-coin CP proof of knowledge；compiler 继承底层 CP 的 succinctness/ZK，并可经 Fiat-Shamir 非交互化。 | 目标计算可被 R1CSCompiler 表达，底层 proof system 支持 CP interface。 | 编译器语义和安全 gap 仍由前端模型承担；floating-point route 不自动变成 exact IEEE proof。 | [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Garg et al. 2022]] |
| Distributed statement partitioning interface | 把同一 committed/private input 绑定到多个 compiler-generated substatements；跨 chunk intermediate values 作为 extended witnesses，并用 consistency check 防止 prover 在不同分片中给出不同值。 | 目标 ZK backend 支持 commit-and-prove-style multiple statements over the same witness/commitments；前端编译器能识别 dependency/cut costs。 | CP 只提供一致性绑定接口；不负责 optimal partition、type-system non-interference、runtime scheduling 或应用正确性。 | [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou/Lian]] |
| Partitioned-proof consistency binding | 将 serial subcircuits 或 partitioned proofs 的 shared private variables 绑定到 public handles/evaluations，防止局部 subproof 使用不同中间值。 | 电路或 statement 已被切分，且 shared values 不能公开。 | Ye 2026 的 polynomial binding 是 CP-like consistency route，不应泛化为完整 CP-SNARK taxonomy；challenge generation and singleton shared-variable cases are source-specific. | [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|Ye 2026]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]] | paper | CP-SNARK/modular proof composition seed; supplies key vocabulary and framework route. | SNARK-specific; details stay in source note and [[modular-zksnarks|Modular zkSNARKs]]. | p1-p7, p12-p19 |
| [[doi-10-1109-sp-2015-23-geppetto-versatile-verifiable-computation|Geppetto]] | paper | Earlier QAP/VC commit-and-prove pattern around banks/buses and scheduled proofs. | VC/compiler-specific; not generic CP foundation alone. | p6-p9 |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] | paper | Shows commit-carrying encryption as proof/encryption composition route. | Pairing/Groth16-like route; not fair exchange by itself. | p12-p20 |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]] | paper | Adds committed witness reuse in low-memory/folding-based SNARK extension. | Narrow extension, not a CP framework source. | p48-p49 |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | paper | Adds public-setup data-parallel CP-NIZK and uses CP composition to split fair exchange validation/delivery. | Application-driven; exact algebra/prototype details stay in source note. | p3-p10 |
| [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct Zero Knowledge for Floating Point Computations]] | paper | Uses public-coin commit-and-prove systems for R1CS as a generic backend to prove relative-error floating/fixed point computations. | CP role is compiler backend; exact floating-point constraints and performance details stay in the source note. | p3-p13 |
| [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou: Automating the Parallelization of Zero-Knowledge Protocols]] | paper | Uses commit-and-prove as the consistency-binding interface for arbitrary compiler-generated ZK substatements in a distributed proving pipeline. | CP dependency is necessary but not sufficient; Ou/Lian still supplies staged semantics, type system, partition optimization and deep simulation. | p2-p12 |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|面向大规模计算的可扩展零知识证明生成方法]] | thesis | Adds polynomial-binding consistency for serializable subcircuits; useful as CP-adjacent hidden-value binding evidence for scalable proof generation. | Not a generic CP-SNARK construction; exact protocol details stay in source note and bridge. | Ch.4 |

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，覆盖当前 vault 已有 source notes。
- Freshness: `fresh` for current-vault synthesis; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: Commit-and-prove should now be a standalone method-family note rather than a row hidden inside Modular zkSNARKs. LegoSNARK establishes the SNARK modular-composition route; Geppetto and Mangrove show adjacent VC/folding uses; SAVER connects CP with encrypted plaintext consistency; ZKCPlus shows CP-NIZK as the enabling proof interface for fair exchange over committed data；Garg et al. adds a compiler-backend route where CP abstracts the proof layer for relative-error floating-point computation。Ou/Lian adds a distributed-proving compiler route: CP is the consistency interface that lets multiple compiler-generated substatements share committed/private inputs and extended witnesses without letting the prover change values across chunks. The common pattern is stable, but the foundation remains thin because exact security notions and construction taxonomy are still source-fragmented.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | 新增 data-parallel CP-NIZK route and fair-exchange application, enough to split CP from modular-zksnarks-only handling. | 定义与范围; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | Keep exact protocol in source note and bridge to fair exchange. |
| [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct Zero Knowledge for Floating Point Computations]] | 新增 CP compiler backend route；说明 public-coin CP/R1CS systems 可被编译成 floating-point ZK proof backend。 | 背景; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | Keep relative-error/floating-point constraints in source note and bridge to floating-point SNARKs. |
| [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou: Automating the Parallelization of Zero-Knowledge Protocols]] | 新增 distributed statement partitioning route；说明 CP 可作为 compiler-generated substatements 的 committed-value consistency interface。 | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | Keep Ou/Lian compiler details in source note and distributed proving node. |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|面向大规模计算的可扩展零知识证明生成方法]] | 新增 partitioned-proof consistency-binding evidence；polynomial binding plays a CP-like role for shared variables in serial subproofs, but stays source-specific. | 方法族与解决路线; 代表 Sources; Bridge Links | yes | Use [[commit-and-prove-arguments-to-scalable-proof-generation|CP -> scalable proof generation]] for the transfer boundary. |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[commit-and-prove-arguments-to-fair-exchange-protocols|Commit-and-prove arguments -> blockchain fair exchange protocols]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; blockchain-systems/execution-and-transactions/fair-exchange-protocols` | dependency, application, proof_protocol_enabler | CP proves committed data/ciphertext/predicate consistency; transaction lock, timeout/refund and commerce semantics remain fair-exchange-specific. | active_seed |
| [[qap-based-vc-systems-to-modular-zksnarks-and-commit-and-prove|QAP-based VC systems -> modular zkSNARKs and commit-and-prove]] | `verifiable-computation/verifiable-computation-systems/qap-based-verifiable-computation-systems; zero-knowledge-proofs/proof-systems/modular-zksnarks` | shared_pattern, dependency, translation | QAP/VC compiler constraints do not transfer wholesale to CP-NIZK or blockchain exchange. | active_seed |
| [[commit-and-prove-arguments-to-floating-point-snarks|Commit-and-prove arguments -> Floating-point SNARKs]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; zero-knowledge-proofs/proof-systems/floating-point-snarks` | dependency, compiler_backend, method_transfer | CP succinctness/ZK properties can transfer through the compiler; exact IEEE rounding, numerical stability and application semantics do not. | active_seed |
| [[commit-and-prove-arguments-to-distributed-proof-generation|Commit-and-prove arguments -> Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; zero-knowledge-proofs/proof-systems/distributed-proof-generation` | dependency, consistency_binding, compiler_backend, method_transfer | CP consistency transfers as a committed-value interface; partition search, staged semantics, worker scheduling and application correctness remain outside CP. | active_seed |
| [[commit-and-prove-arguments-to-scalable-proof-generation|Commit-and-prove arguments -> scalable proof generation]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; zero-knowledge-proofs/proof-systems/scalable-proof-generation` | dependency, consistency_binding, method_transfer | CP-style hidden-value consistency transfers to partitioned proving; exact partition search, polynomial binding formula, scheduler and backend loading remain source-specific. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-commit-and-prove-arguments | is_a | nahida-knowledge-proof-systems | this node and proof-systems parent | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | used_in | nahida-knowledge-modular-zksnarks | LegoSNARK source note and modular-zksnarks node | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | applies_to | nahida-knowledge-blockchain-fair-exchange-protocols | ZKCPlus source note and bridge | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md | ZKCPlus source note | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | applies_to | nahida-knowledge-floating-point-snarks | Garg et al. §2.2/§6 | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | evidenced_by | vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md | source note | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | evidenced_by | vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md | Ou/Lian source note | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | bridges_to | nahida-bridge-commit-and-prove-arguments-to-distributed-proof-generation | bridge note; Ou/Lian source note | high | active_seed |
| nahida-knowledge-commit-and-prove-arguments | bridges_to | nahida-bridge-commit-and-prove-arguments-to-scalable-proof-generation | bridge note; Ye 2026 source note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| CP-NIZK/CP-SNARK canonical definitions and survey sources are incomplete. | Current foundation is source-backed but assembled from several application/framework papers. | nahida-research-search or future paper intake | high | queued |
| PLONK/STARK/transparent commit-and-prove routes missing. | Current evidence leans pairing/DL/folding examples and may not transfer to all proof systems. | nahida-update / nahida-research-search | medium | watching |
| CPlink/proof-linking adapters not split. | Multiple sources mention linking, but deeper comparison is missing. | future source absorption | medium | watching |
| CP compiler use cases beyond fair exchange/floating-point still sparse. | Garg et al. shows compiler-backend use, but general taxonomy across front-end compilers is still thin. | nahida-update / nahida-research-search | medium | active_seed_gap |
| CP as distributed-proving consistency interface has one strong source. | Ou/Lian is clear evidence, but more compiler/protocol sources are needed before splitting a separate CP-distributed child node. | future paper/repo intake | medium | watching |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-zkcplus-fair-exchange | Split commit-and-prove into a standalone foundation-thin method-family node and added ZKCPlus data-parallel CP-NIZK source extension. | 5 source notes | codex |
| 2026-06-23 | nahida-knowledge-20260623-succinct-zk-floating-point | Added CP compiler-backend route for relative-error floating-point ZK proofs. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-ou-zkp-parallelization | Added distributed statement partitioning route and bridge to distributed proof generation from Ou/Lian. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-scalable-zkp-generation | Added partitioned-proof consistency-binding route from Ye 2026 and created bridge to scalable proof generation. | 1 source note | codex |
