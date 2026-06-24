---
id: "nahida-knowledge-proof-system-benchmarking"
title: "Proof-system benchmarking"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "evaluation_axis"
hierarchy_level: "problem"
file_slug: "proof-system-benchmarking"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "proof-system-benchmarking"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/proof-systems/hardware-accelerated-proving"
relation_edges:
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/proof-system-benchmarking.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "applies_to"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "evaluates"
    to: "nahida-knowledge-hardware-accelerated-proving"
    evidence_refs:
      - "vault/05_Bridges/hardware-accelerated-proving-to-proof-system-benchmarking.md"
      - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
      - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-system-benchmarking"
    relation: "bridges_to"
    to: "nahida-bridge-hardware-accelerated-proving-to-proof-system-benchmarking"
    evidence_refs:
      - "vault/05_Bridges/hardware-accelerated-proving-to-proof-system-benchmarking.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-hardware-accelerated-proving-to-proof-system-benchmarking"
source_note_refs:
  - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
  - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
  - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
  - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
  - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
representative_source_refs:
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
  - "doi:10.1145/3575693.3575711"
  - "doi:10.1109/isca52012.2021.00040"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "doi:10.1109/TC.2023.3235975"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
query_keys:
  - "Proof-system benchmarking"
  - "proof-system benchmarks"
  - "SNARK benchmarking"
  - "zk-Bench"
  - "ZKP tool benchmarking"
  - "ZKP performance evaluation"
  - "proof-system runtime estimation"
  - "ZKP benchmark test vectors"
  - "Hekaton benchmark"
  - "distributed zkSNARK benchmark"
  - "GZKP benchmark"
  - "GPU prover benchmarking"
  - "hardware accelerated ZKP benchmark"
  - "PipeZK benchmark"
  - "ASIC zkSNARK prover benchmark"
  - "DIZK benchmark"
  - "Spark zkSNARK benchmark"
  - "Split benchmark"
  - "Good Split benchmark"
  - "SNARK prover memory benchmark"
  - "Yoimiya benchmark"
  - "proof generation pipeline benchmark"
  - "serializable ZK-SNARK benchmark"
aliases:
  - "SNARK benchmarking"
  - "ZKP benchmarking"
  - "proof-system performance evaluation"
domains:
  - "zero-knowledge-proofs"
topics:
  - "proof-system-benchmarking"
  - "zk-snarks"
  - "runtime-estimation"
  - "evaluation-axis"
  - "proof-system-tooling"
  - "distributed-proof-generation"
  - "hardware-accelerated-proving"
  - "gpu-proving"
  - "asic-proving"
  - "cluster-distributed-proving"
  - "memory-efficient-snarks"
  - "prover-memory-benchmarking"
  - "scalable-proof-generation"
  - "proof-generation-pipeline"
tags:
  - "nahida/knowledge"
  - "nahida/evaluation-axis"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-21"
evidence_window_end: "2026-06-22"
created: "2026-06-21"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zk-bench-proof-system-benchmarking"
  - "nahida-knowledge-20260621-hekaton-proof-aggregation"
  - "nahida-knowledge-20260621-gzkp-hardware-accelerated-proving"
  - "nahida-knowledge-20260622-pipezk-pipelined-architecture"
  - "nahida-knowledge-20260622-dizk-distributed-zkp"
  - "nahida-knowledge-20260622-split-hash-memory-optimization"
  - "nahida-knowledge-20260623-scalable-zkp-generation"
source_refs:
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
  - "doi:10.1145/3575693.3575711"
  - "doi:10.1109/isca52012.2021.00040"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "doi:10.1109/TC.2023.3235975"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
confidence: "medium"
trust_tier: "primary"
---

# Proof-system benchmarking

## 定义与范围

- 定义: Proof-system benchmarking 是 ZKP/proof-system engineering 中的评测轴，关注如何在可复现、可比较的条件下测量 proof systems、ZKP development tools、arithmetic libraries 和硬件配置的 execution time、memory consumption、proof size 与 runtime-estimation behavior。
- 不包含: 单个 benchmark 数值、某个版本的性能排行、某个库的实现细节、某篇论文的实验表格或生产部署结论。这些保留在 source notes 或 repo notes。
- Canonical terms: `proof-system benchmarking`, `SNARK benchmarking`, `ZKP performance evaluation`
- Aliases/query keys: zk-Bench, ZKP tool benchmarking, proof-system runtime estimation
- Standalone completeness check: 本节点解释为什么 proof-system benchmarking 是独立评测轴、该评测轴如何组织指标/方法/限制，以及当前 vault 的代表 source 和缺口。
- Retrieval role: 查询“哪个 SNARK 工具快”“benchmark 能否说明生产性能”“某篇 proof-system paper 的实验怎么比较”时先读本节点，再打开具体 source。
- Update scope: 新 source 若提供 benchmark framework、standardized test vectors、ZKP tool comparison、prover hardware comparison、proof-system runtime estimator 或 production benchmark，应刷新本节点。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

Proof systems 的理论指标和工程表现之间有明显落差。一个方案可能在 asymptotic complexity、proof size 或 verifier time 上优秀，但实际 prover time、memory footprint、serialization cost、DSL/circuit implementation、arithmetic backend 和硬件配置都会改变结果。

在当前 vault 中，许多论文都有自己的 benchmark 或 operation-count comparison，例如 SnarkFold、Pianist、Mangrove、Sparrow、ZKLP、SAVER、Hekaton、GZKP、PipeZK、DIZK 和 SPLITA。但这些实验通常服务于各自 source 的论证，不能直接构成跨工具、跨硬件、跨电路的统一结论。zk-Bench 给这个缺口提供了一个独立 source-backed seed；DIZK 和 Hekaton 提供 distributed zkSNARK 的 source-local end-to-end benchmark evidence；GZKP/PipeZK 提供 accelerator-aware prover benchmark evidence；SPLITA 提供 single-machine prover-memory tradeoff benchmark evidence。

## 基础概念判断

- 是否是基础概念/方向/问题: `evaluation_axis`
- 为什么足够通用: 它能组织多个 proof-system paper/repo 的评测证据，降低未来查询“性能/工具选择/生产可用性”时扫描所有 source notes 的成本。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zk-Bench 是当前代表 source；本节点表达的是可复用评测问题，而不是 zk-Bench 项目本身。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[zk-snarks|zk-SNARKs]]。
- 不应拆出的实例/协议/来源: zk-Bench、Zkalc、zk-Harness、criterion.rs、tinybench、单个 AWS instance、单个 chart/table 默认留在 source note 或未来 repo note。

## 解决的问题

Proof-system benchmarking 解决的是 selection and comparability problem:

- 开发者需要在 Groth16、Plonk/Halo2、STARK-like systems、DSL/library combinations、curves and hardware 之间选择。
- 单篇论文的实验往往只覆盖一组实现和硬件，缺乏横向比较。
- 低层 arithmetic operations 会强烈影响高层 proving performance，但两层经常被分开报告。
- circuit implementation quality can falsify apparent backend performance: 一个优化良好的 SHA-256 circuit 可能让工具看起来更快，未优化 circuit 则可能反过来。
- 生产决策需要将 runtime、memory、proof size、setup、verifier time、hardware price/performance 和 maintainability 一起看。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of / evaluation_axis_of | zk-Bench source absorption | active_seed |
| [[zk-snarks|zk-SNARKs]] | applies_to | zk-Bench focuses on SNARK tooling and public-key cryptography operations | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么暂不拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| arithmetic-library benchmarking | section | 目前只有 zk-Bench 一个统一 source；具体 library/version 数值留在 source note。 | zk-Bench §3-§5 | active_seed |
| circuit-level ZKP benchmarking | section | 与 proof-system benchmarking 强相关，但尚无多 source 支撑独立节点。 | zk-Bench §5.3 | active_seed |
| runtime-estimation for cryptographic protocols | section/candidate | 有 zk-Bench 方法 seed，但还需要更多 estimator/profiling sources。 | zk-Bench §6 | review |
| standardized ZKP test vectors | gap/candidate | zk-Bench recommends community convergence,但不是规范本身。 | zk-Bench §7.2 | queued |
| proof-system benchmarking repositories | repo-followup | 需要单独分析 zk-Bench/zk-Harness/Zkalc repo 后再决定是否拆 implementation-practice node。 | source note only | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Layered metric collection | 同时测 low-level arithmetic、setup/prove/verify、memory 和 proof size。 | 需要比较 proof-system stack 而非单个算法。 | 指标定义必须清楚；不同工具 API 会影响 measurement boundary。 | [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench]] |
| Comparable circuit test vectors | 用同一功能的 circuit across tools 评测 proof systems。 | 工具能表达相同 computation。 | circuit optimization 差异会影响公平性；SHA-256 这类真实 circuit 更难完全一致。 | zk-Bench p13-p16 |
| Arithmetic-to-protocol estimation | 用 low-level benchmark data、interpolation/extrapolation 和 operation enumeration 估计高层 protocol runtime。 | 目标 protocol 的 operation mix 可被估计。 | 估算不是 production benchmark；source currently validates only selected gnark Plonk examples。 | zk-Bench §6 |
| Hardware-aware benchmarking | 把 CPU/RAM/architecture 纳入 proof-system evaluation。 | Prover performance受硬件和并行度影响明显。 | cloud on-demand variability and missing GPU/FPGA/mobile coverage must be recorded。 | zk-Bench §5.1, §5.3 |
| Benchmark-data validation | 记录 variance/CV 等统计指标，避免只看单次均值。 | benchmark samples may vary by machine/library/operation。 | 需要原始数据或 repo artifact 才能复现；PDF extraction 只给概要。 | zk-Bench Appendix B |
| Source-local distributed prover benchmarking | 对一个 distributed zkSNARK implementation 报告 supported instance size、setup/prover time、component runtime、scaling behavior、communication/coordination cost、proof size 和 verification time。 | 需要理解某个 distributed prover paper 的实验主张。 | 不是跨工具 benchmark 方法；Spark/OpenMPI/SLURM、硬件、曲线、partitioning、trusted setup 和实现细节都会影响结论。 | [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]]; [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton]] |
| Accelerator-aware prover benchmarking | 把 GPU/ASIC/accelerator 型号、curve/field bit width、NTT/MSM phase、workload sparsity、memory budget、baseline boundary、module-vs-end-to-end boundary 和 CPU residual work 显式写入评测。 | 需要理解 hardware-accelerated prover paper 的性能主张或迁移性。 | exact speedups 依赖 hardware generation、kernel/library、process node、workload、G2/witness/data-movement coverage；不是当前工具排行。 | [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP]]; [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] |
| Source-local prover-memory tradeoff benchmarking | 对一个 memory-efficient SNARK route 同时报告 constraints/QAP degree、prove time、prove memory、setup/proof/verify cost 和 workload boundary。 | 需要理解某个低内存 prover 方法是否真的降低 peak memory。 | 不是跨工具 benchmark 方法；SPLITA 的 loop/xJsnark/libsnark/SHA256-overhead 不能直接外推到 arbitrary circuits 或其他 backend。 | [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] |
| Source-local scalable proof-generation benchmarking | 同时记录 partition count、max subcircuit load、setup/SRS behavior、prove memory、total memory、loading time、CPU utilization、witness/proof thread allocation 和 batch throughput。 | 需要理解 partition/pipeline proof-generation system 是否真的改善端到端资源利用。 | 不是通用工具排行；Ye 2026 的 exact values 依赖 Gnark、BN254、Groth16/Plonk、CPU hardware、matrix/Merkle/linear-recurrence workloads 和配置。 | [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|Ye 2026]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs]] | paper | 创建 proof-system benchmarking 评测轴；提出 arithmetic/circuit backends、Zkalc/zk-Harness、13 curves/9 libraries/5 tools 的 benchmark 和 Plonk runtime estimator | 2023 tool versions；commodity CPU hardware only；limited circuits；repo not analyzed in this run | `p1-p21`, `Appendix A-B` |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | paper | 提供 Spark-distributed Groth zkSNARK source-local benchmark evidence：最大可支持实例、setup/prover scaling、FFT/Lag/MSM components、application constraint/witness generation。 | 不是通用 benchmark methodology；exact values 依赖 2018 EC2/Spark/Groth/R1CS/QAP/curve choices and implementation. | `p1-p19` |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | paper | 提供 distributed zkSNARK source-local benchmark evidence：HPC/OpenMPI setup、latency/throughput scaling、communication costs、proof/verifier behavior、VKD/RAM applications | 不是通用 benchmark methodology；exact values 依赖 Hekaton implementation、cluster and partitioning | `p29-p35`, Appendix A |
| [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP: A GPU Accelerated Zero-Knowledge Proof System]] | paper | 提供 GPU prover source-local benchmark evidence：V100/GTX1080Ti、MNT4753/BLS12-381/ALT-BN128、NTT/MSM breakdown、Zcash/xJsnark workload | 不是通用 benchmark framework；exact speedups depend on hardware, curves, libraries and workload sparsity | `p9-p12` |
| [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK: Accelerating Zero-Knowledge Proof with a Pipelined Architecture]] | paper | 提供 custom ASIC prover source-local benchmark evidence：28 nm synthesis、NTT/MSM module breakdown、BN-128/BLS12-381/MNT4753、Zcash workloads、G2/witness residual bottlenecks | 不是通用 benchmark framework；exact speedups depend on process node, baseline, curve, workload, and what CPU-side work remains | `p10-p13` |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split: A Hash-Based Memory Optimization Method for zk-SNARK]] | paper | 提供 memory-efficient SNARK source-local benchmark evidence：2-Split/5-Split constraints、QAP degree、prove time 与 peak memory tradeoff。 | 不是通用 benchmark framework；exact memory reduction depends on Good Split structure, hash circuit overhead, xJsnark/libsnark backend and loop workload. | `Table II`, `Table III` |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|面向大规模计算的可扩展零知识证明生成方法]] | thesis | 提供 scalable proof-generation source-local benchmark evidence：partition/load reduction、Groth16/Plonk setup and proof memory/time、async loading、CPU utilization and pipeline throughput. | Not a general benchmark framework; exact values are tied to Gnark/BN254/workloads/hardware/configuration. | Ch.3-Ch.5 |

## 正反例约束

- 正确: 用本节点判断某个 source 的 benchmark 是否可跨版本/跨硬件/跨电路迁移。
- 正确: 把 exact benchmark numbers 留在 source note，把 reusable methodology 放在本节点。
- 正确: 把 zk-Bench 作为 representative source，而不是把它写成 foundation concept。
- 错误: 看到一篇论文的 benchmark 就得出所有 SNARK tools 的永久性能排序。
- 错误: 把 operation-count comparison 当作 wall-clock benchmark 或 production deployment evidence。

## 当前综合

- Evidence window: `2026-06-21` to `2026-06-22`，覆盖当前 vault 已深读 zk-Bench、DIZK、Hekaton、GZKP 和 PipeZK 的 benchmark evidence。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-22`。
- 综合: 当前节点是 foundation_thin seed。zk-Bench 显示 proof-system performance 必须分层评估: arithmetic backend、circuit/backend phase、memory/proof size、hardware and runtime estimation 都会改变选择结论。DIZK 补充 Spark-distributed Groth prover evaluation，强调最大 instance size、setup/prover scalability、FFT/Lag/MSM components 和 dense row/column handling 必须与 Spark/EC2/curve/trusted-setup 边界一起记录。Hekaton 补充 divide-and-aggregate distributed prover source-local evaluation；GZKP 补充 GPU hardware-accelerated prover evaluation；PipeZK 补充 custom ASIC / pipelined architecture evaluation；SPLITA 补充 single-machine memory-efficient prover source-local evaluation，强调 memory reduction 必须和 constraint/hash overhead、QAP degree、prove time、split count 与 workload boundary 一起记录。GZKP 与 PipeZK 共同强调 accelerator benchmark 要区分 NTT/MSM module speedup、end-to-end proof time、G2/witness/data-movement residual bottlenecks、curve/field bit width、hardware generation/process node 和 workload sparsity。它们都不能替代跨工具、跨硬件、跨版本的 benchmark methodology。这个节点为后续 proof aggregation、distributed proving、hardware-accelerated proving、memory-efficient SNARKs、zkML proof systems 和 repo/practice evidence 提供统一评测语境。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs]] | 创建 proof-system benchmarking evaluation-axis node；把 proof-system performance 从单篇 benchmark 数值提升为检索/评估结构 | 定义; 方法族与解决路线; 代表 Sources; 当前综合; 缺口与队列 | yes | 若需要当前工具选择，分析 zk-Bench repo/最新 benchmark sources；吸收 Hekaton 等后复核 proof aggregation benchmark 维度 |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | 添加 Spark-distributed Groth zkSNARK source-local benchmark evidence；明确其 100x/10 microseconds per gate 等数值不可脱离 2018-era setup/prover/cluster 边界使用 | 方法族与解决路线; 代表 Sources; 当前综合 | no | repo/current benchmark refresh before engineering decisions |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | 添加 distributed zkSNARK source-local benchmark evidence；明确其数值不应提升为通用工具排行 | 方法族与解决路线; 代表 Sources; 当前综合 | no | repo/current benchmark refresh before engineering decisions |
| [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP: A GPU Accelerated Zero-Knowledge Proof System]] | 添加 GPU prover / accelerator-aware source-local benchmark evidence；连接 hardware-accelerated proving | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | analyze GZKP/current GPU prover repos before engineering decisions |
| [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK: Accelerating Zero-Knowledge Proof with a Pipelined Architecture]] | 添加 custom ASIC / pipelined prover source-local benchmark evidence；补充 module-vs-end-to-end and CPU residual boundary | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | compare with DIZK/distributed sources after next intake |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split: A Hash-Based Memory Optimization Method for zk-SNARK]] | 添加 memory-efficient SNARK source-local benchmark evidence；记录 hash-bound split route 的 constraints/prove time/peak-memory tradeoff and workload boundary | 方法族与解决路线; 代表 Sources; 当前综合 | no | compare with future low-memory SNARK benchmarks after more sources |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|面向大规模计算的可扩展零知识证明生成方法]] | 添加 scalable proof-generation source-local benchmark evidence；记录 partition count/load、setup/SRS、prove memory/time、resource loading、CPU utilization and pipeline throughput boundaries | 方法族与解决路线; 代表 Sources; 当前综合 | no | analyze Yoimiya repo/current benchmark only before engineering decisions |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[hardware-accelerated-proving-to-proof-system-benchmarking|Hardware-accelerated proving -> Proof-system benchmarking]] | `zero-knowledge-proofs/proof-systems/hardware-accelerated-proving; zero-knowledge-proofs/proof-systems/proof-system-benchmarking` | evaluation_axis, benchmark_dependency, hardware_sensitivity, implementation_reuse | Benchmark discipline transfers to accelerated provers; exact speedups, kernel designs, memory budgets and hardware availability remain source-specific. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-proof-system-benchmarking | is_a | nahida-knowledge-proof-systems | this node; parent proof-systems node | high | active_seed |
| nahida-knowledge-proof-system-benchmarking | applies_to | nahida-knowledge-zk-snarks | zk-Bench source note; zk-SNARK tooling focus | high | active_seed |
| nahida-knowledge-proof-system-benchmarking | evidenced_by | vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md | full source note | high | active_seed |
| nahida-knowledge-proof-system-benchmarking | evidenced_by | vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md | DIZK source-local cluster benchmark evidence | medium | active_seed |
| nahida-knowledge-proof-system-benchmarking | evidenced_by | vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md | Hekaton source-local benchmark evidence | medium | active_seed |
| nahida-knowledge-proof-system-benchmarking | evaluates | nahida-knowledge-hardware-accelerated-proving | [[hardware-accelerated-proving-to-proof-system-benchmarking|bridge]]; GZKP §5; PipeZK §6 | high | active_seed |
| nahida-knowledge-proof-system-benchmarking | evidenced_by | vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md | GZKP source-local accelerator benchmark evidence | high | active_seed |
| nahida-knowledge-proof-system-benchmarking | evidenced_by | vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md | PipeZK source-local ASIC accelerator benchmark evidence | high | active_seed |
| nahida-knowledge-proof-system-benchmarking | evidenced_by | vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md | SPLITA source-local prover-memory benchmark evidence | medium | active_seed |
| nahida-knowledge-proof-system-benchmarking | evidenced_by | vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md | Ye 2026 scalable proof-generation benchmark evidence | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| zk-Bench / zk-Harness / Zkalc repository not analyzed. | 论文声称 open-source framework，但 source note does not capture repo architecture, current maintenance, data formats or reproducibility scripts. | nahida-github-repo-analyze | high | queued |
| Current benchmark freshness missing. | 2023 library versions may be outdated; do not use numeric rankings for current engineering decisions without refresh. | nahida-daily-fetch / nahida-research-search | high | queued |
| Hekaton implementation/reproducibility evidence missing. | Hekaton reports strong distributed-prover results, but the PDF source note does not verify the repository, scripts or current maintenance. | nahida-github-repo-analyze | medium | queued_if_repo_known |
| DIZK implementation/reproducibility evidence missing. | DIZK reports Spark-distributed proving and intended code release, but this run did not verify repository, scripts or current maintenance. | nahida-github-repo-analyze | medium | queued_if_repo_known |
| PipeZK RTL/reproducibility evidence missing. | PDF reports 28 nm RTL synthesis and system evaluation, but no local implementation artifact was analyzed. | nahida-github-repo-analyze / nahida-research-search | medium | queued_if_repo_known |
| Standardized ZKP test vectors remain unsettled. | Cross-tool comparison needs community-agreed circuits/functions. | nahida-research-search | medium | queued |
| Interoperable IR / compiler benchmark sources missing. | ZKP tool comparison is affected by frontend/intermediate representation choices. | nahida-research-search | medium | queued |
| GPU/FPGA/mobile benchmark evidence missing. | Prover deployment often uses accelerators; zk-Bench paper excludes them. | nahida-research-search or nahida-github-repo-analyze | medium | queued |
| Current GPU prover benchmark/repo evidence still thin. | GZKP adds one ASPLOS 2023 GPU source, but production/current hardware decisions still need repo and newer benchmark evidence. | nahida-github-repo-analyze / nahida-daily-fetch | high | queued |
| Memory-efficient SNARK benchmark comparison thin. | SPLITA adds a source-local loop benchmark, but current vault still lacks cross-source low-memory benchmark normalization across Mangrove/Sparrow/Gemini/Split-style methods. | nahida-research-search / nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-zk-bench-proof-system-benchmarking | Created evaluation-axis node from zk-Bench source absorption. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-hekaton-proof-aggregation | Added Hekaton as distributed zkSNARK source-local benchmark evidence without changing the evaluation-axis structure. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-gzkp-hardware-accelerated-proving | Added GZKP accelerator-aware prover benchmark evidence and bridge to hardware-accelerated proving. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-pipezk-pipelined-architecture | Added PipeZK as custom ASIC accelerator benchmark evidence and module-vs-end-to-end boundary. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-dizk-distributed-zkp | Added DIZK as Spark-distributed Groth zkSNARK source-local benchmark evidence. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-split-hash-memory-optimization | Added SPLITA as source-local prover-memory tradeoff benchmark evidence. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-scalable-zkp-generation | Added Ye 2026 as source-local scalable proof-generation benchmark evidence. | 1 source note | codex |
