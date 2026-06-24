---
id: "doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system"
title: "GZKP: A GPU Accelerated Zero-Knowledge Proof System"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1-p14 full extracted text"
  - "Sections 1-8, evaluation, related work, discussion, and references"
canonical_url: "https://doi.org/10.1145/3575693.3575711"
doi: "10.1145/3575693.3575711"
arxiv_id: ""
venue: "ASPLOS 2023"
year: "2023"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "hardware-accelerated-proving"
  - "gpu-proving"
  - "prover-acceleration"
  - "ntt-msm-acceleration"
  - "zk-snarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "hardware-accelerated-proving"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/hardware-accelerated-proving"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
  directions:
    - "proof-systems"
  topics:
    - "hardware-accelerated-proving"
    - "proof-system-benchmarking"
    - "zk-snarks"
domains:
  - "zero-knowledge-proofs"
topics:
  - "hardware-accelerated-proving"
  - "gpu-proving"
  - "prover-acceleration"
  - "ntt"
  - "msm"
  - "finite-field-arithmetic"
  - "zk-snarks"
aliases:
  - "GZKP"
  - "GPU accelerated ZKP"
  - "GPU accelerated zkSNARK prover"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "proof-systems"
  problem:
    - "zkSNARK proof-generation latency"
    - "large finite-field prover bottlenecks"
    - "GPU utilization for NTT and MSM"
    - "load imbalance in sparse scalar MSM"
  method_family:
    - "GPU NTT acceleration"
    - "GPU MSM acceleration"
    - "cache-aware memory scheduling"
    - "bucket-based MSM task mapping"
    - "large-integer finite-field arithmetic"
  system_layer:
    - "prover backend"
    - "hardware acceleration"
    - "finite-field library"
    - "multi-GPU proving"
  evaluation_context:
    - "NVIDIA V100"
    - "NVIDIA GTX1080Ti"
    - "MNT4753"
    - "BLS12-381"
    - "ALT-BN128"
    - "Zcash"
    - "xJsnark"
  bridge:
    - "hardware-accelerated-proving-to-proof-system-benchmarking"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-gzkp-hardware-accelerated-proving"
source_refs:
  - "doi:10.1145/3575693.3575711"
  - "sha256:6eae4f3b9741af60ce09ad0fb35a943d8990f86478befe8832967411369efd89"
confidence: "high"
trust_tier: "primary"
primary_direction: "proof-systems"
secondary_directions:
  - "proof-system-benchmarking"
  - "zk-snarks"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The paper's main contribution is a GPU prover backend for zkSNARK proof generation, not a new ZKP protocol."
  - "The reusable problem is prover-side hardware acceleration for NTT, MSM and finite-field arithmetic."
  - "Evaluation evidence belongs under proof-system benchmarking as hardware-specific benchmark data."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0049"
local_pdf: "~/Desktop/paper/3575693.3575711.pdf"
pdf_sha256: "6eae4f3b9741af60ce09ad0fb35a943d8990f86478befe8832967411369efd89"
extracted_text_path: "vault/02_Raw/pdf/extracted/gzkp-a-gpu-accelerated-zero-knowledge-proof-system-6eae4f3b9741-pages.txt"
---

# GZKP: A GPU Accelerated Zero-Knowledge Proof System

## 论文身份

- 标题: GZKP: A GPU Accelerated Zero-Knowledge Proof System
- 作者: Weiliang Ma, Qian Xiong, Xuanhua Shi, Xiaosong Ma, Hai Jin, Haozhao Kuang, Mingyu Gao, Ye Zhang, Haichen Shen, Weifang Hu
- 会议/期刊: ASPLOS '23, Proceedings of the 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2
- 年份: 2023
- DOI: 10.1145/3575693.3575711
- arXiv: unknown in local PDF
- 链接: https://doi.org/10.1145/3575693.3575711
- 本地 PDF: `~/Desktop/paper/3575693.3575711.pdf`
- 代码/数据: 本地 PDF 未给出 GZKP 仓库 URL；引用了 MINA GPU Groth16 prover、bellperson、bellman、libsnark 和 Zcash tooling。
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 14
- 已覆盖章节/页码: p1-p14, including abstract, introduction, background, POLY/NTT design, MSM design, finite-field library, evaluation, related work, discussion, conclusion and references.
- 未覆盖章节/页码: none in the local ASPLOS PDF.
- Extraction gaps: figures and equations are partially noisy in text extraction, but section prose, tables and key results are recoverable.
- 精读说明: 队列元数据把该论文暂放在 `proof-system-foundations`；深读后主路径纠正为 `zero-knowledge-proofs/proof-systems/hardware-accelerated-proving`。GZKP 是 source instance；可上升为知识层的是“硬件感知 prover 加速”问题域，以及 NTT/MSM/finite-field arithmetic 三类加速路线。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和结果 | ZKP proof generation 开销阻碍在线应用；GZKP 用 GPU 加速 NTT、MSM 和大整数有限域运算 | high | 主分类依据 |
| §1 / p2-p3 | 动机和贡献 | zkSNARK prover bottleneck；现有 GPU 方案受 global-memory shuffle、冗余计算、load imbalance 和 arithmetic library 限制 | high | 硬件加速问题定义 |
| §2 / p3-p5 | Background | zkSNARK workflow、POLY/NTT、MSM/Pippenger、large finite field and elliptic-curve operations | high | 方法依赖 |
| §3 / p5-p6 | POLY/NTT design | 保持 global memory 布局不变，内部 shuffle 到 shared memory，提升 cache/L2 utilization | high | NTT 加速路线 |
| §4.1 / p6-p7 | MSM computation consolidation | 用 cross-window / bucket-based point merging 和 checkpoint preprocessing 减少 PMUL/window reduction | high | MSM 加速路线 |
| §4.2 / p8 | Workload management | 按 bucket load 分组并用 fine-grained warp/CG mapping 处理 sparse scalar imbalance | high | 负载均衡路线 |
| §4.3 / p8-p9 | Optimized finite-field library | 支持 256-753 bit 大整数，warp cooperation，借用 floating-point units 加速 modular multiplication | high | arithmetic backend |
| §5.1-§5.2 / p9-p10 | Evaluation methodology / overall | V100/GTX1080Ti，MNT4753/BLS12-381/ALT-BN128，xJsnark/Zcash workload，对比 libsnark/MINA/bellman/bellperson | high | benchmarking evidence |
| §5.3 / p10-p12 | Breakdown | NTT/MSM 单模块性能、memory usage、ablation of library/no-shuffle/load-balance | high | 判断机制贡献 |
| §6 / p12 | Related work | zkSNARK implementations、FPGA/GPU acceleration、GPU NTT/MSM/ECC acceleration | medium | 领域边界 |
| §7 / p12 | Discussion | 可迁移到 HE/NTT throughput；不改变 ZKP protocol security；implementation bugs 可考虑 formal verification | high | transfer boundary |
| §8 / p12-p13 | Conclusion | GZKP 展示 ZKP proof generation 仍有大量并行执行效率优化空间 | medium | 总结 |
| References / p13-p14 | Prior work | Marlin/Plonk/Sonic、Groth16、libsnark、bellperson、MINA、GPU/FPGA arithmetic references | medium | follow-up seeds |

## 核心精读笔记

> 这篇论文的主线是: 不修改 ZKP protocol，而是在 zkSNARK prover 的 NTT、MSM 和大整数有限域运算层面重做 GPU 后端，让 proof generation latency 更接近在线应用可用范围。

### 问题、动机与边界

- ZKP 已能给 verifier 提供短 proof 和快速验证，但 prover 端仍要执行大量有限域乘加、NTT 和椭圆曲线 MSM。
- 论文特别关注 zkSNARK-style prover:
  - POLY stage 主要由 NTT/INTT 和 polynomial multiplication 组成；
  - MSM stage 对大规模 scalar/point vectors 做多标量乘法，通常是 proof generation 中最重的部分；
  - 使用的 field/curve integer bit width 可到 256-753 bit，普通 GPU/CPU 原生类型不能直接承载。
- 现有 GPU 路线的瓶颈不是“没有并行化”，而是并行化没有贴合 ZKP workload:
  - NTT 为保证 contiguous access 做昂贵 global-memory shuffle；
  - MSM 的 Pippenger/sub-MSM 分解没有跨窗口/跨子任务合并足够多的 point operations；
  - Zcash 等真实 workload 中 scalar vector 稀疏，导致 bucket/warp load imbalance；
  - arithmetic library 没有充分利用 GPU warp cooperation 和 floating-point units。
- GZKP 是高性能 prover backend，不是新的 proof system，也不改变 Groth16/Plonk/Marlin/Sonic 这类上层协议的安全定义。

### 论文贡献

- NTT/POLY stage:
  - 保持 global memory 中 vector 原始顺序，避免每个 batch 前昂贵的 global-memory shuffle。
  - 把多个较小 independent groups 同时映射到一个 GPU block，使线程从 global memory 读取连续 chunk，再在 shared memory 内部重排为 NTT 需要的 strided pattern。
  - 目标是在 global memory 侧提高 L2/cache-line utilization，同时在 shared memory 侧减少 bank conflict。
- MSM stage:
  - 不再只把 MSM 水平切成 sub-MSM 后分别跑 window-based Pippenger，而是把同一 scalar component 的点跨窗口合并到 bucket。
  - 通过 checkpoint preprocessing 预计算部分 weighted points，在性能和 GPU memory footprint 之间调参。
  - 用 bucket load grouping、heavy-first scheduling、warp/cooperative-group mapping 处理 sparse scalar distribution 带来的不均衡。
- Finite-field arithmetic:
  - 支持 256-753 bit 大整数有限域运算。
  - 用 warp-level primitives 协作处理 carry and multi-word arithmetic。
  - 用 double-precision floating-point units 和 Dekker-style multiplication 辅助 modular multiplication，让 GPU 原本闲置的 FP 单元参与大整数运算。
- Evaluation:
  - 对比 CPU-based libsnark/bellman 和 GPU-based MINA/bellperson。
  - 覆盖 MNT4753、BLS12-381、ALT-BN128，多种 synthetic 和真实 workload，包括 Zcash。

### zkSNARK prover workflow 抽象

论文把 zkSNARK prover 归纳为两大阶段:

- POLY stage:
  - 输入 witness-derived vectors `a,b,c`。
  - 通过一系列 NTT/INTT/PMUL 计算 polynomial `H(x)`。
  - 瓶颈是 large finite field 上的 NTT memory access 和 modular arithmetic。
- MSM stage:
  - 输入 POLY 输出、scalar vector、proving key point vectors。
  - 执行 `sum_i s_i * P_i` 类型的多标量乘法。
  - 瓶颈是大量 PADD/PMUL、Pippenger buckets、window reductions 和 sparse scalar load imbalance。

这组抽象对上层知识库很有用: GZKP 不要求把每个 protocol 细节都升层，而是把 prover backend 的 reusable bottlenecks 锚定在 `NTT`, `MSM`, `finite-field arithmetic`, `memory layout`, `load balance`。

### NTT/POLY stage 设计

传统 GPU NTT 在每个 batch 前通过 shuffle 让后续 butterfly operations 获得 contiguous memory access。GZKP 的观察是: 对 ZKP 的大 bit-width field elements，shuffle 自身会吃掉大量 batch time。

GZKP 的替代路线:

- 保持 global memory layout 稳定，避免全局重排。
- 每个 GPU block 不只处理一个大 independent group，而是处理多个小 groups。
- 线程从 global memory 读取一组连续 chunk，保证 L2/cache line 利用。
- 写入 shared memory 时做内部重排，让 NTT butterfly 在 shared memory 中看到自己需要的 strided/interleaved layout。
- batch 完成后反向过程写回 global memory。

知识层可迁移点:

- 对 ZKP 的 NTT 加速，contiguous memory access 和避免全局 shuffle 之间存在 trade-off。
- GPU shared memory 可以作为“局部重排层”，把 global-memory coalescing 与算法所需访问模式解耦。
- 该路线偏 latency-oriented single large NTT；HE 中的 NTT batching 更偏 throughput-oriented，不能直接把结论互换。

### MSM stage 设计

GZKP 的 MSM 仍基于 Pippenger-like 思路，但改变并行化单位:

- 旧路线: 水平切成多个 sub-MSM，每个 sub-MSM 内部做 window/bucket/reduction。
- GZKP: 跨 sub-MSM 和跨窗口合并相同 scalar component 的点，把更多 point additions 合并在同一个 bucket。
- 通过预计算 weighted points，把不同 window 的权重提前转化为 point representation，从而消除或压缩 window-reduction step。

关键代价:

- 完整预计算可能占用大量 GPU global memory，论文给出的 381-bit / MSM scale `2^21` 场景已超过数 GB。
- 因此 GZKP 引入 checkpoint interval `M`，只预计算一部分 weighted points，需要时从最近 checkpoint 通过若干 PADD 补到目标点。

负载均衡:

- Sparse scalar vector 会让某些 bucket 很重、某些 bucket 几乎为空。
- GZKP 按 bucket workload 分组，从重任务开始调度，并根据 group 的平均 load 分配 warp 数。
- Cooperative groups 进一步把一个 PADD 的大整数运算分给多个线程。

知识层可迁移点:

- MSM 加速不只是“并行更多窗口”，还要问并行粒度是否阻碍跨窗口/跨子任务的合并。
- 预计算可以换减少 PMUL/window work，但必须显式记录 memory budget。
- 稀疏 scalar distribution 是真实 ZKP workload 的一等问题，不应只用 dense synthetic benchmark 判断。

### Finite-field arithmetic library

GZKP 的底层库负责把大整数 field arithmetic 映射到 GPU:

- 对 256-753 bit integers 分拆为多个 machine-word components。
- 用 warp-level communication 处理 carry propagation 和多字结果合并。
- 对 753-bit 场景使用 52-bit chunks，转成 double-precision floating point 后利用 Dekker-style method 避免 rounding 问题。
- NTT butterfly 和 MSM PADD 都构建在该库上。

这里的通用意义是: proof-system performance 不只由 protocol asymptotics 决定，有限域库、curve bit width、GPU warp/SM/shared-memory 参数都会改变 prover latency。

### 实验与结果

实验环境:

- Dual Intel Xeon Gold 5117, 256GB DRAM, Ubuntu 18.04.2, CUDA 11.4。
- Four NVIDIA Tesla V100 GPUs, each 32GB memory；one NVIDIA GTX1080Ti GPU, 11GB memory。
- Baselines:
  - CPU: libsnark, bellman。
  - GPU: MINA GPU Groth16 prover, bellperson。
- Curves:
  - MNT4753 / 753-bit；
  - BLS12-381 / 381-bit curve with 256-bit NTT field operations in the paper's breakdown;
  - ALT-BN128 / 256-bit。

End-to-end:

- xJsnark workloads on one V100 / MNT4753:
  - GZKP reports average 48.1x speedup over libsnark and 33.6x over MINA。
  - Workloads include AES, SHA-256, RSAEnc, RSASigVer, Merkle-Tree, Auction。
- Zcash workload on one V100 / BLS12-381:
  - Average 24.7x over bellman and 8.7x over bellperson。
  - For a shielded transaction combination, paper reports 37.1x over bellman and 9.2x over bellperson。
- Four V100 GPUs / Zcash:
  - GZKP further reduces time by average 2.1x compared with one GPU, and reports average 13.2x over bellperson multi-GPU baseline。

Breakdown:

- NTT:
  - On V100, single NTT average speedups include 343.0x over CPU libsnark for MNT4753 and 5.8x over bellperson for BLS12-381。
  - GZKP ablation shows finite-field library and no-global-memory-shuffle / flexible block assignment both matter。
- MSM:
  - On V100, GZKP reports average 12.4x over MINA for MNT4753 and 7.0x over bellperson for BLS12-381。
  - For ALT-BN128, it reports average 26.6x over CPU libsnark。
  - Memory: GZKP's BLS12-381 MSM uses more GPU memory than bellperson but stays within V100 memory and gains speed; MNT4753 memory grows more slowly than MINA, which fails beyond a reported scale due to memory.
- Ablation:
  - Bucket-based computation consolidation is the largest MSM gain.
  - Finite-field library adds further speed.
  - Load balancing matters especially for sparse scalar vectors.

### 安全性与正确性边界

- GZKP 不修改 ZKP protocol，本身不改变 protocol soundness/zero-knowledge assumptions。
- 它优化的是 prover backend；Verifier/proof semantics 仍由原 protocol 决定。
- Implementation bugs 可能生成错误 proofs。论文把 formal verification of GZKP 留作 future work。
- Benchmark 数字是 hardware/backend/source-version specific，不应迁移为“GPU prover 永远快多少倍”的通用结论。

### 与相关方向的关系

- 与 [[distributed-proof-generation|Distributed proof generation]] 相邻但不同:
  - GZKP 主要是单机/多 GPU hardware backend 优化；
  - distributed proof generation 关注多机器/多参与者分摊 proving work、通信和 proof aggregation。
- 与 [[memory-efficient-snarks|Memory-efficient SNARKs]] 相邻但不同:
  - GZKP 使用更多 GPU memory 换性能，并非以降低 peak memory 为主目标；
  - low-memory SNARKs 关注 streaming/chunking/folding/pass complexity。
- 与 [[proof-system-benchmarking|Proof-system benchmarking]] 强相关:
  - GZKP 的贡献必须在 hardware、curve、workload、field library、sparse/dense scalar 和 memory budget 条件下解释。
  - 它补充了 zk-Bench 缺失的 GPU/accelerator benchmark 维度，但不是一个通用 benchmark framework。

## 对 Nahida 分层知识库的吸收判断

### 应进入的上层节点

- [[hardware-accelerated-proving|Hardware-accelerated proving]]: GZKP 是创建该问题节点的主 source seed，定义 prover-side hardware acceleration 的 NTT/MSM/finite-field arithmetic 路线。
- [[proof-systems|Proof systems]]: 作为 proof-system engineering 的 source extension，补足 prover backend/hardware acceleration 轴。
- [[zk-snarks|zk-SNARKs]]: 作为 zkSNARK prover acceleration source extension，而不是 zk-SNARK foundation。
- [[proof-system-benchmarking|Proof-system benchmarking]]: 作为 GPU/hardware-specific source-local benchmark evidence，用于提醒 benchmark 必须显式记录硬件、curve、field library、workload sparsity 和 memory budget。

### 不应升级为独立知识节点的内容

- `GZKP`: 单篇系统/论文名，保留为 source note。
- `GZKP-no-LB`, `GZKP-no-GM-shuffle`, `BG w. lib`: ablation variants，保留为 source-specific evidence。
- 某个表格中的 exact speedup 数字: 保留在 source note，用于回答 GZKP-specific question；上层只保留路线和边界。
- MINA/bellperson/libsnark 的 2022 版本性能: 不作为当前工具排名。

### 新增桥接需求

- 新建 [[hardware-accelerated-proving-to-proof-system-benchmarking|Hardware-accelerated proving -> Proof-system benchmarking]]，说明 GPU prover 加速结论必须通过硬件感知 benchmark 解释。
- 不新建 `GZKP -> blockchain` bridge: Zcash/Mina 是 evaluation/application examples，论文没有提出新的 blockchain protocol route。

## 边界与残留问题

- Protocol coverage: 论文以 zkSNARK prover workflow 为中心；虽然提到 Marlin/Plonk/Sonic 可受益，具体 integration 仍需 source/repo evidence。
- Hardware coverage: 主实验为 V100 和 GTX1080Ti；不能推断 A100/H100/consumer GPU/FPGA/ASIC 的表现。
- Implementation evidence: 本地 PDF 未给出 GZKP 代码仓库；可复现性需要 repo/source artifact。
- Security engineering: GZKP 不改 protocol security，但实现正确性、side channels、GPU memory isolation、constant-time behavior 未形成完整分析。
- Workload transfer: Dense synthetic data 和 sparse real workload 都有结果；新 workload 仍需单独测 NTT/MSM ratio、scalar distribution、curve bit width 和 memory budget。
- HE transfer: NTT 技术可能迁移到 homomorphic encryption，但 HE 更常追求 batched throughput，GZKP 只给 future-work 边界。

## 可查询关键词

- GZKP
- GPU accelerated zero-knowledge proof
- GPU zkSNARK prover
- hardware-accelerated proving
- NTT acceleration
- MSM acceleration
- sparse scalar MSM
- finite-field arithmetic GPU
- bellperson GPU baseline
- MINA GPU Groth16 prover
- Zcash proof generation GPU

## 更新记录

| 日期 | run_id | 变更 | 证据 | 操作者 |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-gzkp-hardware-accelerated-proving | Deep-read source note created and classified into hardware-accelerated proof-system engineering, with benchmarking and zk-SNARK secondary paths. | 14-page local PDF, DOI 10.1145/3575693.3575711, sha256:6eae4f3b9741af60ce09ad0fb35a943d8990f86478befe8832967411369efd89 | codex |
