---
id: "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
title: "Memory-efficient SNARKs -> Distributed proof generation"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "memory-efficient-snarks"
  - "distributed-proof-generation"
  - "prover-scalability"
endpoint_knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-distributed-proof-generation"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
relation_types:
  - "contrast"
  - "shared_bottleneck"
  - "scalability_alternative"
  - "design_boundary"
directionality: "two_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
  - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-distributed-proof-generation"
representative_source_refs:
  - "doi:10.1109/TC.2023.3235975"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
query_keys:
  - "single-machine SNARK memory vs distributed proving"
  - "Split vs DIZK"
  - "low-memory SNARKs vs cluster proving"
  - "prover scalability alternatives"
  - "Yoimiya pipeline vs distributed proving"
aliases:
  - "Split vs DIZK"
domains:
  - "zero-knowledge-proofs"
topics:
  - "memory-efficient-snarks"
  - "distributed-proof-generation"
  - "zk-snarks"
tags:
  - "nahida/bridge"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-split-hash-memory-optimization"
  - "nahida-knowledge-20260623-scalable-zkp-generation"
source_refs:
  - "doi:10.1109/TC.2023.3235975"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
confidence: "high"
trust_tier: "primary"
---

# Memory-efficient SNARKs -> Distributed proof generation

## 连接命题

Memory-efficient SNARKs 和 Distributed proof generation 都在处理同一个上游瓶颈: zk-SNARK/ZKP verifier 可以很便宜，但 prover 端可能被大电路的 witness、R1CS/QAP、多项式、FFT/MSM、commitment/opening 和内存占用拖垮。二者的路线不同:

- [[memory-efficient-snarks|Memory-efficient SNARKs]] 试图让单个 prover 用更少 peak memory 完成 proving，例如 streaming/chunking/folding/elastic PIOP，或 SPLITA 这种 front-end circuit partitioning。
- [[distributed-proof-generation|Distributed proof generation]] 试图把 proving work 分摊到多台机器或多个参与者，例如 DIZK/Spark cluster、Pianist/bivariate Plonk、Hekaton divide-and-aggregate。

SPLITA 论文在 introduction 中明确把 DIZK/Wu et al. 的 cluster route 作为相邻但不适用于普通个人机器的方案，因此这个 bridge 记录的是 shared bottleneck 与 design boundary，而不是把低内存 SNARK 和分布式 proving 合并成一个方向。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | 单机或单个 proving pipeline 的 peak memory、pass complexity、front-end partitioning 和 streaming/folding routes | 证明系统资源优化问题 |
| [[distributed-proof-generation|Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation` | cluster/multi-worker/multi-party proving、worker scheduling、communication、proof aggregation/commitment aggregation | 证明生成横向扩展方法族 |

## 端点基础说明

[[memory-efficient-snarks|Memory-efficient SNARKs]] 关注的是 prover 端空间复杂度: 不一定减少总工作量，而是减少同时持有的 witness/trace/polynomial state。Split 属于这一端，因为它把 R1CS 电路切成多个 hash-bound subcircuits，让 obsolete variables 不跨全程驻留内存。

[[distributed-proof-generation|Distributed proof generation]] 关注的是把一个 proving task 拆给多台机器或多个参与者。DIZK 属于这一端，因为它把 Groth zkSNARK 的 setup/prover、QAP reductions、FFT/Lag/MSM 等映射到 Spark cluster，并保持 Groth proof/verifier interface。

## 迁移矩阵

| Concept / pattern | From | To | 可迁移部分 | 不可迁移部分 |
| --- | --- | --- | --- | --- |
| Prover-side bottleneck diagnosis | both | both | 两边都要量化 prover memory/time，而不是只看 proof size/verifier time | 单机 peak memory 与 cluster aggregate memory/communication 不是同一指标 |
| Circuit/task partitioning | memory-efficient SNARKs | distributed proving | Good Split 的 cut thinking 可以启发 worker partitioning 的 state-boundary analysis | Hash-bound sequential subcircuits 不自动给出 worker parallelism、fault isolation 或 communication protocol |
| Cluster decomposition | distributed proving | memory-efficient SNARKs | DIZK/Pianist/Hekaton 说明 FFT/MSM/QAP/proof chunks 可分治 | 多机 route 不能直接解决普通单机/手机 prover 的内存限制 |
| Proof/interface preservation | both | both | 两边都尽量保持 verifier/proof 接口可接受 | Split proof tuple、DIZK Groth proof、Pianist/Hekaton final proof 的接口和 assumptions 各自不同 |
| Benchmark discipline | both | both | 都需要同时报告 constraints/QAP degree/prove time/prove memory/verify time/communication | SPLITA 的 loop benchmark 不能替代 DIZK 的 cluster benchmark，反之亦然 |

## 非迁移边界

- Split/SPLITA 的 hash-bound subcircuit route 不提供分布式 worker 调度、worker trust、straggler handling 或 communication complexity。
- DIZK/Pianist/Hekaton 的 cluster route 不保证资源受限单机 prover 可运行；aggregate cluster memory 与单机 peak memory 是不同约束。
- proof aggregation 可能用于 distributed fan-in，但不等同于 memory-efficient SNARKs 本身。
- 单篇实验数字不能跨路线外推: SPLITA 使用 xJsnark/libsnark loop workload；DIZK 使用 Spark/EC2 与 2018-era Groth stack。

## 证据

| Source / note | 支撑内容 | 置信度 | 局限 |
| --- | --- | --- | --- |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] §I | 明确提出单机 resource-constrained prover 问题，并把 Wu et al. cluster route 作为不适用于普通机器的相邻方案 | high | 只覆盖 SPLITA 的 loop-oriented proof-of-concept |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] §III-V | 用 hash-bound circuit partitioning 降低 prover memory，2-Split/5-Split 实验给出 memory/time tradeoff | high | Good Split 搜索和 arbitrary circuits 后续仍缺 |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]] | Spark-distributed Groth zkSNARK route，服务 cluster-scale setup/prover | high | 2018 source-local benchmark；repository/current artifact 未分析 |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | 组织 Mangrove/Sparrow/Gemini/Split 等低内存 routes | high | foundation_thin，仍缺 R1CS/hash/front-end foundation packs |
| [[distributed-proof-generation|Distributed proof generation]] | 组织 DIZK/Pianist/Hekaton/Siniel/Split Prover 等 distributed/private delegated routes | high | production prover network evidence 仍薄 |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|Ye 2026 / Yoimiya]] | 增加中间路线：automatic circuit partitioning 降低单机 peak memory，同时用 proof-generation pipeline 提高 batch throughput/resource utilization；它连接两端的 bottleneck 语言，但不引入 cluster worker model。 | high | thesis/source-local; not a distributed prover and not a general benchmark framework |

## 路径传播

| Endpoint path | Knowledge update | Relation/index update | Bridge/refresh action | Status |
| --- | --- | --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | Add Split as front-end circuit partition route and add this bridge | add `bridges_to` edge | created bridge | done |
| `zero-knowledge-proofs/proof-systems/distributed-proof-generation` | Add single-machine contrast boundary from Split/DIZK comparison | add `bridges_to` edge | created bridge | done |
| `zero-knowledge-proofs/proof-systems/zk-snarks` | Add Split as prover-resource source extension only | `evidenced_by` source row | no standalone Split node | done |

## 查询入口

- “Split 和 DIZK 有什么区别?”
- “SNARK prover 内存不够时应该单机低内存优化还是分布式 proving?”
- “low-memory SNARK 和 distributed prover 是同一个方向吗?”
- “Good Split 的 circuit partitioning 能不能迁移到 cluster proving?”

## 刷新规则

- Last checked: 2026-06-22
- Valid until: 2026-07-22
- Refresh triggers:
  - DIZK/aPlonk/deVirgo repository or primary source analysis.
  - Follow-up work on automatic Good Split finding or compiler-level circuit partitioning.
  - New benchmarks comparing single-machine low-memory proving against cluster proving on the same workloads.

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-split-hash-memory-optimization | Created bridge to separate single-machine memory-efficient SNARK routes from distributed proving routes while preserving their shared prover-scalability bottleneck. | 2 source notes | codex |
| 2026-06-23 | nahida-knowledge-20260623-scalable-zkp-generation | Added Yoimiya/Ye 2026 as a partition-plus-pipeline midpoint: it reinforces the shared bottleneck while preserving the boundary between single-machine memory optimization and distributed proving. | 1 source note | codex |
