---
id: "nahida-knowledge-distributed-proof-generation"
title: "Distributed proof generation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "distributed-proof-generation"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs:
  - "nahida-knowledge-private-delegated-proving"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "distributed-proof-generation"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/blockchain-applications"
relation_edges:
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "has_child"
    to: "nahida-knowledge-private-delegated-proving"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving.md"
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-distributed-proof-generation.md"
      - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
      - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "applies_to"
    to: "nahida-knowledge-zkp-blockchain-applications"
    evidence_refs:
      - "vault/05_Bridges/distributed-proof-generation-to-zkrollups.md"
      - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
    evidence_refs:
      - "vault/05_Bridges/distributed-proof-generation-to-snark-proof-aggregation.md"
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "bridges_to"
    to: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    evidence_refs:
      - "vault/05_Bridges/private-delegated-proving-to-kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-distributed-proof-generation"
    relation: "bridges_to"
    to: "nahida-bridge-commit-and-prove-arguments-to-distributed-proof-generation"
    evidence_refs:
      - "vault/05_Bridges/commit-and-prove-arguments-to-distributed-proof-generation.md"
      - "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-proof-generation-to-zkrollups"
  - "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
  - "nahida-bridge-private-delegated-proving-to-kzg-commitments"
  - "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
  - "nahida-bridge-commit-and-prove-arguments-to-distributed-proof-generation"
source_note_refs:
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
  - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
  - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
  - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
  - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
  - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
  - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
  - "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
  - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
representative_source_refs:
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "doi:10.1145/3576915.3616621"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
query_keys:
  - "Distributed proof generation"
  - "distributed ZKP"
  - "distributed prover"
  - "data-parallel ZKP"
  - "fully distributed ZKPs"
  - "deVirgo"
  - "Pianist"
  - "DIZK"
  - "Spark zkSNARK"
  - "Split vs DIZK"
  - "single-machine SNARK memory vs distributed proving"
  - "distributed Groth16"
  - "Ou"
  - "Lian"
  - "compiler-assisted distributed proof generation"
  - "ZKP statement partitioning"
  - "shallow simulation"
  - "deep simulation"
  - "extended witnesses"
  - "PBO ILP ZKP partitioning"
  - "Yoimiya"
  - "proof generation pipeline"
  - "serializable ZK-SNARKs"
  - "aPlonk"
  - "zkRollup prover scaling"
  - "Hekaton"
  - "divide-and-aggregate zkSNARK"
  - "DNA zkSNARK"
  - "private delegated proving"
  - "privacy-preserving prover delegation"
  - "Siniel"
  - "EOS"
  - "Efficient Outsourcing of SNARKs"
  - "private delegation of zkSNARK provers"
  - "universal-setup zkSNARK delegation"
  - "zkSaaS"
  - "split prover zkSNARKs"
  - "partial witness zkSNARK delegation"
aliases:
  - "distributed ZKP"
  - "distributed prover"
  - "fully distributed ZKPs"
  - "data-parallel proof generation"
  - "privacy-preserving prover delegation"
  - "partial-witness delegated proving"
  - "compiler-assisted ZKP parallelization"
  - "ZKP statement partitioning"
domains:
  - "zero-knowledge-proofs"
topics:
  - "distributed-proof-generation"
  - "prover-scalability"
  - "data-parallel-circuits"
  - "zkrollup-prover-scaling"
  - "divide-and-aggregate"
  - "proof-aggregation"
  - "private-delegated-proving"
  - "piop-based-zksnark-delegation"
  - "split-prover-zksnarks"
  - "cluster-proving"
  - "distributed-fft"
  - "distributed-msm"
  - "memory-efficient-snarks"
  - "single-machine-prover-memory"
  - "compiler-assisted-zkp-parallelization"
  - "zkp-programming-languages"
  - "statement-partitioning"
  - "scalable-proof-generation"
  - "pipeline-proof-generation"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkbridge"
  - "nahida-knowledge-20260620-pianist"
  - "nahida-knowledge-20260621-hekaton-proof-aggregation"
  - "nahida-knowledge-20260621-siniel-private-delegated-proving"
  - "nahida-knowledge-20260623-eos-private-delegated-proving"
  - "nahida-knowledge-20260621-split-prover-zksnarks"
  - "nahida-knowledge-20260622-dizk-distributed-zkp"
  - "nahida-knowledge-20260622-split-hash-memory-optimization"
  - "nahida-knowledge-20260623-ou-zkp-parallelization"
  - "nahida-knowledge-20260623-scalable-zkp-generation"
source_refs:
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "doi:10.1109/TC.2023.3235975"
  - "doi:10.1145/3576915.3616621"
  - "sha256:dd9b5b3e54f932d9bc55148ccf408969c23c081980e9ffe5358fe052ffefab5a"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
confidence: "medium"
trust_tier: "primary"
---

# Distributed proof generation

## 定义与范围

- 定义: Distributed proof generation 是 ZKP proof-system engineering 中的一个方法族，目标是把一个大 proving task 分摊到多台机器或多个参与者，同时尽量保持 proof size、verifier time 和通信成本可控。
- 不包含: 单篇系统名、单个实验数字、某个 prover worker scheduler、rollup economics 或 proof aggregation 的全部问题；这些分别留在 source note、实现/系统节点或 [[snark-proof-aggregation|SNARK proof aggregation]] 中。
- Canonical terms: `distributed proof generation`, `distributed ZKP`, `distributed prover`
- Aliases/query keys: deVirgo, Pianist, DIZK, aPlonk, fully distributed ZKPs, data-parallel ZKP
- Standalone completeness check: 本节点解释 distributed proving 的问题、方法族、边界、代表 sources、桥接关系和缺口；source-specific protocol 和 benchmark 留在 source notes。
- Retrieval role: 查询“ZKP 怎么多机生成 proof”“zkRollup prover 如何横向扩展”“Pianist/deVirgo/DIZK 区别”时优先读本节点。
- Update scope: 新 distributed proving paper/repo、production rollup prover benchmark、DIZK/aPlonk/deVirgo primary source、或者 proof aggregation/distributed proving 边界变化。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

ZKP 的 verifier 端通常追求短 proof 和低验证成本，但 prover 端可能面对数百万到数十亿约束、巨大 witness、FFT/MSM/commitment 开销和内存瓶颈。区块链中的 zkRollups、zkEVM、trustless bridge/light-client verification 等应用尤其明显: verifier 在链上或轻节点侧很贵，prover 可以离线或多机承担成本。

model_prior_background: 分布式 proving 的自然目标是把 prover work 横向扩展，但 naive 做法常会让 communication、proof size、verifier work、aggregation complexity 或 witness privacy 变成新瓶颈。当前 vault 的 source-backed evidence 来自 zkBridge/deVirgo、Pianist、Hekaton、EOS、Siniel、Split Prover 和 DIZK；其中 DIZK 属于 cluster/Spark-distributed Groth zkSNARK route，EOS/Siniel 属于 full-witness private delegation route，Split Prover 属于 phase-aware private delegation，不属于 data-parallel cluster proving。SPLITA/`Split` 这篇 hash-bound circuit partitioning source 只作为对照桥接: 它解决同一个 prover-side memory bottleneck，但路线是单机低内存证明，不属于 distributed proof generation。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family`
- 为什么足够通用: 它已经承接 zkBridge/deVirgo、Pianist 与 Hekaton 三条不同路线，后续 DIZK、aPlonk、distributed Plonk/FRI/STARK prover、rollup prover networks 都可进入同一比较框架。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: deVirgo、Pianist 和 Hekaton 是代表来源；本节点组织的是“如何多机生成一个可验证 proof”的问题族。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[zk-snarks|zk-SNARKs]], [[polynomial-commitments|Polynomial commitments]]。
- 不应拆出的实例/协议/来源: Pianist、deVirgo、DIZK、aPlonk 默认作为 protocol/source instances，除非多来源和重复查询证明需要 protocol-instance child。

## 解决的问题

Distributed proof generation 解决的是 prover-side scalability:

- 单机时间太长: 一个大电路或大 batch proof 需要在固定时间窗口内生成。
- 单机内存太高: witness、polynomial evaluations、FFT/MSM 和 commitments 无法轻松放入普通机器。
- 应用需要更大 batch: zkRollups 希望更多交易进入一个 proof；跨链 light-client proof 希望验证更多 signatures/headers。
- Verifier/proof 不应同步膨胀: 多机证明不能只是生成 `M` 个 proofs 再让 verifier 验 `M` 次。
- 参与者可能不可信: 多机/多参与者 proving 需要定位错误 worker 或恶意 sub-prover 的机制。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of / method_family_of | zkBridge/deVirgo and Pianist source absorption | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| cluster-distributed Groth zkSNARKs | section | DIZK 给出早期通用 R1CS/QAP/Groth setup/prover 的 Spark-distributed route，适合作为 cluster proving baseline。 | DIZK §3-§6 | active_seed |
| data-parallel distributed proving | section | 多个相同子电路是最清晰的分布式 proving 场景 | zkBridge/deVirgo; Pianist | active_seed |
| general-circuit distributed proving | section | 支持 arbitrary connections 是 Pianist 相对 data-parallel-only 路线的一个重要扩展；Hekaton 也以 arbitrary circuits 为目标，但通过 partition-friendly memory checking 处理 shared wires。 | Pianist §4/§6.2; Hekaton §2/§4 | active_seed |
| robust collaborative proving | section | 多参与者/worker 可能恶意，需要 partial proof verification 和排除机制 | Pianist §5 | source_extension |
| divide-and-aggregate distributed SNARKs | section | Hekaton 提供把分布式 chunk proving 与 proof aggregation 组合起来的 route，但目前仍是单 source-backed seed，不单独拆节点。 | Hekaton §1-§8 | active_seed |
| compiler-assisted statement partitioning | section | Ou/Lian 提供语言+编译器 route：用 staged semantics、live-variable analysis 和 PBO/ILP cut search 自动切分 ZK statements，减少开发者手动 partition。 | Ou §1-§7 | active_seed |
| [[private-delegated-proving|Private delegated proving]] | subproblem | 委托方希望把 proving 外包或分阶段交给其他参与者，同时隐藏 witness/aux-sensitive data 并减少在线开销；这与普通多机 prover scaling 的信任/隐私边界不同。 | EOS §1-§6; Siniel §1-§6; Split Prover §1-§5 | active_seed |
| distributed prover networks / markets | watchlist | Pianist 用 mining-pool analogy，但未给完整经济机制 | Pianist §1/§7 | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| DIZK/Spark-distributed Groth proving | 把 Groth zkSNARK setup/prover 中的 R1CS/QAP、FFT/Lag、fixed/variable-base MSM 和 dense row/column handling 分配到 Spark cluster。 | 目标 statement 能表达为大 R1CS，且系统可接受 cluster setup/prover 和 trusted setup 运营成本。 | proof/verifier interface 保持 Groth；Spark shuffle、dense row/column skew、trusted setup security 和 2018-era benchmark 边界必须记录。 | [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]] |
| deVirgo/data-parallel distributed proof generation | 对大量相同子电路的 proof work 做分布式 sumcheck/polynomial-commitment aggregation。 | 工作负载高度 data-parallel，例如多个 signature verification。 | zkBridge source 指出它适合跨链 light-client 大电路，但 proof/verifier/on-chain 成本仍需递归压缩。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |
| Pianist/bivariate distributed Plonk | 用 `Y` 维分机器、`X` 维分局部电路，并用 DKZG 聚合 commitments/openings，使 proof size/verifier time 近似常数。 | Plonk/KZG-compatible setting；data-parallel 或已分布 witness 的 general circuits。 | trusted setup/pairing assumptions；custom-gate production workload 未验证；robustness主要见 data-parallel RCPS。 | [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] |
| Hekaton/divide-and-aggregate via proof aggregation | 把大电路分成 subcircuits，worker 并行生成 commit-carrying inner proofs，coordinator 聚合 commitments/proofs 得到最终 proof；shared wires 通过 partition-friendly memory checking 处理。 | 大计算可被分区，且 inner SNARK/aggregation scheme 支持 Hekaton 的 commit-carrying/Mirage 路线。 | final proof size/verifier time 为 logarithmic；aggregation 当前单机；性能依赖 partitioning、OpenMPI/cluster 和 Mirage 实现。 | [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton]] |
| Ou/Lian compiler-assisted statement partitioning | 用 Ou 语言标注 security/knowledge levels，Lian 通过 shallow simulation、live-variable dependency graph、PBO/ILP cut search 和 deep simulation 自动生成可并行验证的 substatements。 | 目标 ZK backend 支持 commit-and-prove-style consistency；程序本身已经对应用安全且适合目标 protocol。 | 不证明程序功能正确性/data-obliviousness；proof details 部分在 online full version；partition quality 受 atomic annotation、solver budget 和 backend setup time 影响。 | [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou/Lian]] |
| Private delegated proving | delegator 把 proving 工作交给其他参与者，同时通过 secret sharing/consistency checks 或 split aux privacy 保持 witness/授权边界。 | witness 需要保密，或 witness 分阶段到达且 delegator 希望提前预计算。 | EOS 是 full-witness 强隐私/online-checking route；Siniel 是 full-witness worker-side checking/offline-delegator route；Split Prover 是 partial-witness two-phase completion；zkSaaS/FHE/collaborative primary sources 仍缺。 | [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS]]; [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]]; [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| Recursive compression after distributed proving | 用链上友好 SNARK 证明 distributed proof 的 verification，降低 on-chain verification。 | 大 proof 直接链上验证不可行，且目标链低成本支持 Groth16/类似 verifier。 | 增加 recursive proving time；不是 distributed generation 本身。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |
| Proof aggregation of already-generated SNARK proofs | 把多个 proof 合并降低 verifier work。 | 系统已有多个独立 proofs，瓶颈在批量验证。 | 与 distributed generation 不同: 它不一定减少生成单个大 proof 的 prover memory/time。 | [[snark-proof-aggregation|SNARK proof aggregation]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | paper | 提供 deVirgo/data-parallel distributed proof generation seed，用于跨链 light-client signatures/header verification | 单一应用 source；deVirgo primary comparison 仍需更多来源；链上成本依赖 Groth16 recursive compression | `p8-p13` |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | paper | 提供 Plonk/bivariate KZG fully distributed ZKP 路线，覆盖 data-parallel 与 general circuits，并评估 zkRollup prover scaling | BN254/Gnark/R1CS-to-Plonk conversion；witness distribution 假设；经济模型未实现 | `p1-p15` |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | paper | 提供 divide-and-aggregate distributed zkSNARK 路线：partitioned chunk proving + commit-carrying proof/commitment aggregation + partition-friendly memory checking | Rust/arkworks/OpenMPI/HPC implementation source-local；aggregation 当前未并行；repository 未分析 | `p1-p35`, Appendix `p36-p44` |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel: Distributed Privacy-Preserving zkSNARK]] | paper | 提供 private delegated proving 路线：delegate-friendly preprocessing + secret-shared witness + noninteractive witness/PIOP consistency checkers | 只覆盖 Groth16/KZG-oriented construction 和 honest-majority secure-with-abort assumptions；zkSaaS/OB22 等对照仍需 source-level 吸收 | `p1-p30` |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS: Efficient Private Delegation of zkSNARK Provers]] | paper | 提供 full-witness private delegated proving primary source：isolated/collaborative protocols, PIOP consistency checker, PIOP/KZG prover operation circuits, mobile/cloud delegation evaluation | Delegator remains online for checks; source-local MARLIN/arkworks implementation; repository not analyzed | `p1-p18` |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | paper | 提供 phase-aware private delegated proving 路线：early witness precomputation + aux split zero-knowledge + late Groth16 proof completion | Groth16-specific；不是 generic data-parallel distributed proving；implementation evidence 缺 | `p1-p23` |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | paper | 提供 cluster-distributed Groth zkSNARK 路线：Spark RDDs、distributed FFT/Lag/MSM、dense row/column aware QAP instance/witness reduction。 | 2018 Spark/EC2/source-local benchmark；trusted setup 仍随 circuit size 增长；code repository 未分析。 | `p1-p19` |
| [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou: Automating the Parallelization of Zero-Knowledge Protocols]] | paper | 提供 compiler-assisted statement partitioning 路线：Ou front-end、Lian compiler、shallow/deep simulation、live-variable/PBO-ILP cut search 和 consistency sync。 | 依赖 commit-and-prove-compatible backend；不证明应用 functional correctness/data-obliviousness；exact speedups 是 source-local。 | `p1-p15` |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|面向大规模计算的可扩展零知识证明生成方法]] | thesis | contrast/adjacent route: Yoimiya uses partitioning and pipeline scheduling to improve proof-generation throughput/resource utilization, but it is not a cluster-distributed prover. | Single-machine/multi-task pipeline route; exact CPU utilization and memory numbers are source-local. | Ch.5 |

## 正反例约束

- 正确: 把 Pianist、deVirgo、DIZK、aPlonk 放在同一方法族下比较通信、proof size、verifier time、worker trust 和适用电路。
- 正确: 把 zkRollup/zkEVM 作为应用场景，通过 bridge 连接到 blockchain applications。
- 错误: 把 Pianist 当作 foundation concept；它是 source instance。
- 错误: 把 distributed proof generation 和 SNARK proof aggregation 混为一谈；前者优化 prover-side generation，后者优化 verifying many existing proofs。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，只代表当前 vault 已吸收 sources。
- Freshness: `fresh` for source absorption; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: DIZK 补上 early cluster-distributed Groth zkSNARK baseline: 它把 setup/prover 的 R1CS/QAP、FFT/Lag、MSM 和 sparse-matrix skew handling 映射到 Spark cluster，并保持 Groth verifier/proof interface 不变。zkBridge/deVirgo 说明 data-parallel distributed proving 可服务跨链 light-client verification，但直接链上验证仍重，需要 recursive compression。Pianist 把分布式 proving 作为 Plonk/KZG-compatible 方法族展开，用 bivariate constraints 和 DKZG 保持 proof/verifier/communication 常数级，并在 zkRollup workload 上给出扩展性证据。Hekaton 给出 divide-and-aggregate route: 用 proof aggregation 做 fan-in，通过 partition-friendly memory checking 处理 arbitrary circuits 的 shared wires，并用 Mirage/TIPP-style aggregation 把 worker 产生的 chunk proofs 压成一个 proof。EOS、Siniel 和 Split Prover 补上正交隐私/授权轴线: EOS 处理完整 witness 的强隐私委托证明但要求 delegator 在线检查，Siniel 处理完整 witness 的 worker-side checking/offline-delegator route，Split Prover 处理早到 witness 的预计算和晚到 witness 的安全补全。SPLITA/`Split` 新增的是对照边界: 它同样针对 prover memory bottleneck，但通过单机 hash-bound circuit partitioning 解决，不增加 distributed worker model。Ou/Lian 新增的是编译器路线: 不从底层 protocol 或硬件入手，而是让前端语言和编译器自动把 ZK statement 切成可并行证明/验证的 substatements，并用 commit-and-prove consistency 维护跨分片 extended witnesses。当前节点因此区分七类路线: cluster/Spark-distributed Groth proving、data-parallel distributed proving、bivariate Plonk distributed proving、divide-and-aggregate via proof aggregation、compiler-assisted statement partitioning、full-witness private delegated proving、partial-witness split proving。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | deVirgo: data-parallel distributed proof generation for cross-chain light-client workload | 方法族与解决路线; 代表 Sources | yes | 吸收 deVirgo/DIZK primary source 后复核 |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | Plonk/bivariate-KZG fully distributed ZKPs; zkRollup and general-circuit evaluation; RCPS robustness | 定义; 方法族; 当前综合; Bridge Links | yes | 继续吸收 DIZK/aPlonk/Hekaton 时分清 distributed generation vs aggregation；Mangrove 已路由到 [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | divide-and-aggregate route; partition-friendly memory checking; proof aggregation as distributed prover fan-in; VKD/RAM applications and source-local scaling benchmark | 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 分析 Hekaton repo/吸收 DIZK、aPlonk、SnarkPack/TIPP 后校准 |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel: Distributed Privacy-Preserving zkSNARK]] | private delegated proving route; delegator-offline preprocessing; secret-shared/authenticated witness; WCC/PCC consistency checkers | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 吸收 zkSaaS、collaborative zkSNARKs 后复核 private delegated proving taxonomy |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS: Efficient Private Delegation of zkSNARK Provers]] | private delegated proving primary source; isolated/collaborative delegated SNARK protocols; PIOP consistency checker and efficient PIOP/KZG prover circuits | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | Analyze EOS repo if available; absorb zkSaaS/OB22 primary sources for comparison |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | phase-aware private delegation route; partial witness precomputation; unchanged Groth16 verifier; bridge to recursion/folding boundary | 下级结构; 方法族; 代表 Sources; 当前综合 | yes | Track non-Groth16 split prover sources and implementation evidence |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | cluster/Spark-distributed Groth zkSNARK route; distributed FFT/Lag/MSM; dense row/column aware QAP reduction; source-local 2018 scaling benchmark | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | Analyze DIZK repo/artifact if needed; compare with aPlonk/deVirgo primary sources later |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split: A Hash-Based Memory Optimization Method for zk-SNARK]] | contrast-only source extension: hash-bound circuit partitioning reduces single-machine prover memory, but does not introduce worker scheduling, communication, or distributed trust assumptions | Bridge Links; 当前综合; 关系图谱 | no | Keep routed through [[memory-efficient-snarks|Memory-efficient SNARKs]]; compare against DIZK only as alternative prover-scalability route |
| [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou: Automating the Parallelization of Zero-Knowledge Protocols]] | compiler-assisted statement partitioning route; shallow/deep simulation; live-variable/PBO-ILP cut search; extended-witness consistency via commit-and-prove backend | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | Keep Ou/Lian as source instance; split `ZKP programming languages and compilers` only after more sources justify it |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|面向大规模计算的可扩展零知识证明生成方法]] | adjacent pipeline/partition route: subcircuit-level scheduling and multi-task witness/proof pipeline improve resource utilization without introducing a distributed worker trust/communication model | 当前综合; 代表 Sources; Bridge Links | no | Route primarily through [[scalable-proof-generation|Scalable proof generation]] and [[memory-efficient-snarks|Memory-efficient SNARKs]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-proof-generation-to-zkrollups|Distributed proof generation -> zkRollup prover scaling]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation; zero-knowledge-proofs/applications/blockchain-applications` | applies_to, scalability_enabler, implementation_reuse | Prover parallelization transfers to rollup proving; rollup security, data availability, sequencer economics and finality do not transfer. | active_seed |
| [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation; zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation` | method_transfer, scalability_enabler, performance_compression, implementation_reuse | Proof aggregation can fan in distributed chunk proofs; circuit partitioning, witness distribution, worker scheduling and exact aggregation scheme remain source-specific. | active_seed |
| [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving; zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | dependency, verification_enabler, implementation_reuse, privacy_preserving_delegation | KZG commitment/opening machinery transfers as a consistency-binding mechanism; witness-sharing protocol, authentication tags, trusted setup and concrete zkSNARK backend remain protocol-specific. | active_seed |
| [[memory-efficient-snarks-to-distributed-proof-generation|Memory-efficient SNARKs -> Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/proof-systems/distributed-proof-generation` | contrast, shared_bottleneck, scalability_alternative | Both address prover-side time/memory bottlenecks; single-machine low-memory routes such as SPLITA do not inherit distributed worker trust, communication, scheduling, or cluster economics. | active_seed |
| [[commit-and-prove-arguments-to-distributed-proof-generation|Commit-and-prove arguments -> Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; zero-knowledge-proofs/proof-systems/distributed-proof-generation` | dependency, consistency_binding, compiler_backend, method_transfer | Commit-and-prove transfers the committed-value consistency interface needed for arbitrary statement partitioning; it does not provide partition search, staged semantics, worker scheduling, or application functional correctness. | active_seed |
| [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, succinct_verification, performance_compression | deVirgo/Groth16 route is a cross-chain application, not a general rollup-prover claim. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-distributed-proof-generation | is_a | nahida-knowledge-proof-systems | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md | high | active_seed |
| nahida-knowledge-distributed-proof-generation | evidenced_by | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | zkBridge/deVirgo source note | medium | active_seed |
| nahida-knowledge-distributed-proof-generation | evidenced_by | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | Pianist source note | high | active_seed |
| nahida-knowledge-distributed-proof-generation | applies_to | nahida-knowledge-zkp-blockchain-applications | [[distributed-proof-generation-to-zkrollups|bridge]]; Pianist §6.1 | high | active_seed |
| nahida-knowledge-distributed-proof-generation | evidenced_by | vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md | Hekaton source note | high | active_seed |
| nahida-knowledge-distributed-proof-generation | bridges_to | nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation | [[distributed-proof-generation-to-snark-proof-aggregation|bridge]]; Hekaton §1-§8 | high | active_seed |
| nahida-knowledge-distributed-proof-generation | has_child | nahida-knowledge-private-delegated-proving | [[private-delegated-proving|Private delegated proving]]; Siniel source note | high | active_seed |
| nahida-knowledge-distributed-proof-generation | evidenced_by | vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md | Siniel source note | high | active_seed |
| nahida-knowledge-distributed-proof-generation | evidenced_by | vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md | EOS source note | high | active_seed |
| nahida-knowledge-distributed-proof-generation | bridges_to | nahida-bridge-private-delegated-proving-to-kzg-commitments | [[private-delegated-proving-to-kzg-commitments|bridge]]; Siniel WCC/PCC | high | active_seed |
| nahida-knowledge-distributed-proof-generation | evidenced_by | vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md | Split Prover source note | medium | active_seed |
| nahida-knowledge-distributed-proof-generation | evidenced_by | vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md | DIZK source note | high | active_seed |
| nahida-knowledge-distributed-proof-generation | bridges_to | nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation | bridge note; Split/SPLITA and DIZK source notes | high | active_seed |
| nahida-knowledge-distributed-proof-generation | evidenced_by | vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md | Ou/Lian source note | high | active_seed |
| nahida-knowledge-distributed-proof-generation | bridges_to | nahida-bridge-commit-and-prove-arguments-to-distributed-proof-generation | bridge note; Ou/Lian source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| DIZK repository/artifact 未分析。 | PDF 已吸收，但 source code、current maintenance、Spark job layout 和 reproducibility scripts 未验证。 | nahida-github-repo-analyze | medium | queued_if_repo_known |
| aPlonk primary source 未吸收。 | Pianist 直接比较 aPlonk；需要源级细节判断边界。 | nahida-update | medium | queued_or_search |
| Hekaton repository 未分析。 | PDF 只说明实现和会开源；当前代码架构、维护状态和可复现脚本不在 vault 中。 | nahida-github-repo-analyze | medium | queued_if_repo_known |
| Production zkRollup prover pipeline/repo evidence 缺。 | Pianist 的实验不能代表完整生产 prover economics/scheduling/reliability。 | nahida-github-repo-analyze / nahida-research-search | high | queued |
| Plonk foundation node/source 缺。 | Pianist 依赖 Plonk，但 vault 还没有完整 Plonk foundation。 | nahida-research-search / nahida-update | high | foundation_gap |
| zkSaaS/collaborative zkSNARKs primary sources 未吸收。 | EOS/Siniel 把它们作为 private delegated proving 的直接对照；需要源级吸收才能判断 preprocessing、online cost、privacy 和 consistency-check taxonomy。 | nahida-update / nahida-research-search | high | queued |
| Split prover follow-up / implementation evidence 缺。 | Split Prover 给出 Groth16 theory route；需要确认真实 workload 中 aux size、setup material 和 online completion gains。 | nahida-research-search / nahida-github-repo-analyze | medium | queued_if_repo_known |
| ZKP programming languages and compilers 还未成独立节点。 | Ou/Lian 暴露一个 compiler tooling 轴，但单 source 不足以把 `ZKP programming languages and compilers` 拆成 durable child。 | future paper/repo intake | medium | watching |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Created method-family node from zkBridge/deVirgo seed plus Pianist source; corrected Pianist away from folding-schemes queue classification. | 2 source notes | codex |
| 2026-06-21 | nahida-knowledge-20260621-hekaton-proof-aggregation | Added Hekaton divide-and-aggregate route and bridge to SNARK proof aggregation. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-siniel-private-delegated-proving | Added private delegated proving child problem and KZG consistency-check bridge from Siniel. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-eos-private-delegated-proving | Added EOS as primary full-witness private delegation evidence and closed the EOS missing-source gap. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-split-prover-zksnarks | Added split prover zkSNARKs as phase-aware delegated proving evidence and child route. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-dizk-distributed-zkp | Added DIZK as cluster/Spark-distributed Groth zkSNARK baseline and closed the missing-primary-source gap. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-split-hash-memory-optimization | Added SPLITA as contrast-only evidence through the memory-efficient SNARKs bridge; kept it out of distributed-proving route rows. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-ou-zkp-parallelization | Added Ou/Lian as compiler-assisted statement partitioning route and bridge to commit-and-prove consistency binding. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-scalable-zkp-generation | Added Ye 2026 as adjacent pipeline/partition source under the broader scalable proof generation problem; not classified as cluster-distributed proving. | 1 source note | codex |
