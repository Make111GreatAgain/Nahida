---
id: "doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture"
title: "PipeZK: Accelerating Zero-Knowledge Proof with a Pipelined Architecture"
type: "source"
source_type: "paper"
source_kind: "pdf"
source_subtype: "paper_local"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
safe_for_absorption: true
trust_tier: "primary"
source_identity:
  type: "doi"
  key: "doi:10.1109/isca52012.2021.00040"
source_refs:
  - "doi:10.1109/isca52012.2021.00040"
  - "sha256:c0f14e8331711012ca6199369d563cfd2247810733ff7159d91ab0c3af8e3d3f"
  - "filename:PipeZK_Accelerating_Zero-Knowledge_Proof_with_a_Pipelined_Architecture.pdf"
representative_source_refs:
  - "doi:10.1109/isca52012.2021.00040"
authors:
  - "Ye Zhang"
  - "Shuo Wang"
  - "Xian Zhang"
  - "Jiangbin Dong"
  - "Xingzhong Mao"
  - "Fan Long"
  - "Cong Wang"
  - "Dong Zhou"
  - "Mingyu Gao"
  - "Guangyu Sun"
venue: "ISCA 2021"
year: "2021"
doi: "10.1109/isca52012.2021.00040"
arxiv_id: ""
canonical_url: "https://doi.org/10.1109/isca52012.2021.00040"
local_pdf: "~/Desktop/paper/PipeZK_Accelerating_Zero-Knowledge_Proof_with_a_Pipelined_Architecture.pdf"
pdf_sha256: "c0f14e8331711012ca6199369d563cfd2247810733ff7159d91ab0c3af8e3d3f"
extracted_text_path: "vault/02_Raw/pdf/extracted/pipezk-accelerating-zero-knowledge-proof-with-a-pipelined-architecture-c0f14e833171-pages.txt"
pages: 13
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/hardware-accelerated-proving"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
domains:
  - "zero-knowledge-proofs"
topics:
  - "hardware-accelerated-proving"
  - "asic-proving"
  - "pipelined-accelerator"
  - "prover-acceleration"
  - "ntt"
  - "msm"
  - "finite-field-arithmetic"
  - "zk-snarks"
topic_ids:
  - "hardware-accelerated-proving"
  - "proof-system-benchmarking"
  - "zk-snarks"
query_keys:
  - "PipeZK"
  - "pipelined ZKP accelerator"
  - "ASIC zkSNARK prover"
  - "NTT accelerator"
  - "MSM accelerator"
  - "Zcash prover acceleration"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Abstract and introduction identify proof generation latency, POLY/NTT, and MSM as the target."
  - "Sections 3 and 4 design accelerator subsystems for polynomial computation and multi-scalar multiplication."
  - "Section 6 evaluates a 28 nm ASIC-like implementation and source-local Zcash benchmarks."
  - "The paper does not introduce a new proof-system foundation; it accelerates zkSNARK prover execution."
parent_knowledge_refs:
  - "nahida-knowledge-hardware-accelerated-proving"
  - "nahida-knowledge-proof-system-benchmarking"
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-proof-systems"
bridge_refs:
  - "nahida-bridge-hardware-accelerated-proving-to-proof-system-benchmarking"
related_paths:
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/hardware-accelerated-proving.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/proof-system-benchmarking.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
  - "vault/05_Bridges/hardware-accelerated-proving-to-proof-system-benchmarking.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0051"
queue_rank: 51
run_ids:
  - "nahida-knowledge-20260622-pipezk-pipelined-architecture"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# PipeZK: Accelerating Zero-Knowledge Proof with a Pipelined Architecture

## Paper Identity

| Field | Value |
| --- | --- |
| Title | PipeZK: Accelerating Zero-Knowledge Proof with a Pipelined Architecture |
| Authors | Ye Zhang; Shuo Wang; Xian Zhang; Jiangbin Dong; Xingzhong Mao; Fan Long; Cong Wang; Dong Zhou; Mingyu Gao; Guangyu Sun |
| Venue | ISCA 2021, 2021 ACM/IEEE 48th Annual International Symposium on Computer Architecture |
| Year | 2021 |
| DOI | 10.1109/isca52012.2021.00040 |
| Local PDF | `~/Desktop/paper/PipeZK_Accelerating_Zero-Knowledge_Proof_with_a_Pipelined_Architecture.pdf` |
| Source key | `doi:10.1109/isca52012.2021.00040`; `sha256:c0f14e8331711012ca6199369d563cfd2247810733ff7159d91ab0c3af8e3d3f` |
| Pages | 13 |
| Extracted text | `vault/02_Raw/pdf/extracted/pipezk-accelerating-zero-knowledge-proof-with-a-pipelined-architecture-c0f14e833171-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Absorption run: `nahida-knowledge-20260622-pipezk-pipelined-architecture`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0051`
- Primary classification correction: queue 中的 `proof-system-foundations` 过宽；本论文主要进入 [[hardware-accelerated-proving|Hardware-accelerated proving]]，并作为 [[proof-system-benchmarking|Proof-system benchmarking]] 和 [[zk-snarks|zk-SNARKs]] 的 source extension。
- arXiv note: queue 元数据中的 `2012.2021` 是 DOI 派生误判；本地 PDF 未显示 arXiv ID。

## 一句话贡献

PipeZK 将 zkSNARK prover 的重计算拆成 POLY/NTT 与 MSM 两个硬件子系统，用递归 NTT 分解、带宽友好的流水 NTT 模块、on-chip transpose、Pippenger-style MSM bucket dispatch 和 28 nm ASIC 评估，证明 ZKP proof generation 的主要瓶颈可以在不改变 proof-system security/interface 的情况下通过定制硬件后端显著降低。

## 章节地图

| Section | 内容 | 对知识库的作用 |
| --- | --- | --- |
| Abstract, I | 定义目标: ZKP proof generation 太慢；PipeZK 面向 polynomial computation 和 elliptic-curve MSM。 | 支撑硬件加速 proving 的问题设定。 |
| II.A-II.B | ZKP/zkSNARK 应用和 prover workflow；R1CS、POLY、MSM、proof verification。 | 说明加速对象是 prover backend，不是 proof-system foundation。 |
| II.C-II.D | 硬件加速机会与 prior work；Zcash/Filecoin examples；CPU/GPU 局限；DIZK 作为互补分布式路线。 | 界定 hardware route 与 distributed route 的边界。 |
| III.A-III.C | NTT 计算、挑战与递归 NTT 分解。 | 给出 POLY 子系统的算法路线。 |
| III.D-III.E | 带宽友好 NTT pipeline、FIFO stride realization、INTT 支持、tiling 与 on-chip transpose。 | 给出 custom accelerator route 的可复用设计轴。 |
| IV.A-IV.C | MSM 定义、挑战、Pippenger algorithm 与 PADD-heavy 转换。 | 说明 MSM 不是简单复制 PMULT 单元。 |
| IV.D-IV.E | Dynamic work dispatch、shared PADD pipeline、FIFO/bucket buffering、多 PE 并行和负载均衡。 | 支撑 hardware-accelerated MSM 的 route。 |
| V | 总体系统: CPU witness/G2，accelerator 执行 POLY 与 G1 MSM。 | 说明异构系统边界。 |
| VI | Verilog/28 nm/DDR4/Ramulator/libsnark setup；NTT/MSM microbenchmarks；Zcash end-to-end workloads。 | 进入 proof-system benchmarking 的 source-local evidence。 |
| VII | 结论。 | 概括 PipeZK 是 architectural effort。 |
| References | libsnark、bellman、bellperson、DIZK、Zcash、Groth16、HEAX、Pippenger 等。 | follow-up seeds，不在本轮展开。 |

## 解决的问题

PipeZK 解决的是 zkSNARK prover-side latency problem:

- verifier 端 proof 很短、验证很快，但 prover 端要执行多轮大规模 finite-field NTT/INTT 和 elliptic-curve MSM。
- Zcash 等应用中 single proof generation 可能达到秒级到几十秒级；Filecoin-style large circuits 会更重。
- POLY/NTT 受到 large vector size、wide field elements、strided access 和 off-chip bandwidth 限制。
- MSM 受到大量 elliptic-curve point operations、scalar sparsity、bucket load imbalance 和 PADD/PMULT 资源利用率限制。
- 通用 CPU/GPU 不一定适合 wide integer finite-field arithmetic 和 irregular memory access；定制硬件可以把数据流、内存访问和算术单元一起设计。

边界: PipeZK 不提出新的 zkSNARK 协议，不改变 witness statement、trusted setup、zero-knowledge/security assumptions 或 verifier interface。它是 proof-system implementation/backend layer 的 source。

## 核心方法

### Prover workflow 抽象

论文把目标 prover computation 归纳为两块:

- POLY: 由 `A`, `B`, `C` 等 scalar vectors 经过 NTT/INTT、polynomial multiplication/addition 生成 `H`，主开销是大规模 NTT。
- MSM: 对 scalar vectors 与 elliptic-curve point vectors 做多标量乘法，主开销是 point additions/doublings/multiplications 以及 bucket reductions。

这组抽象是知识层可复用的: 未来 GPU、FPGA、ASIC 或 distributed backend 都可以用 POLY/NTT 与 MSM 作为比较轴。

### POLY/NTT 子系统

PipeZK 的 NTT 设计不是把百万级 NTT 整个放进片上，而是先递归分解:

- 将大 NTT 视作 `I x J` 矩阵，拆成多个较小的 column NTT、twiddle multiplication、row NTT。
- 小 NTT kernel 可映射到固定规模硬件模块，避免片上资源和 off-chip bandwidth 同时爆炸。
- NTT/INTT 使用类似 FFT 的 butterfly structure，但元素是大 bit-width finite-field scalars。

硬件模块层面:

- NTT pipeline 每个 cycle 顺序读一个元素、写一个元素。
- 每个 stage 使用不同深度的 FIFO 表示 stride，而不是用大规模 multiplexer 选择 butterfly inputs。
- 这种方式把复杂 strided access 转成可流水的 local buffering，使 off-chip bandwidth 需求从“不现实的大量并行元素访问”降为顺序读写。
- INTT 共享主要乘法资源，通过控制逻辑、反向 stage order 和 inverse twiddle factors 支持。
- 对不同 kernel size，可通过 bypass 早期 stage 支持较小 NTT。

整体数据流层面:

- 递归 NTT 的 column/row 访问天然会在 off-chip memory 上产生大 stride。
- PipeZK 用 tiling 和 on-chip transpose buffer，在片内把 `t x t` 小块转置，保证回写/读取具有较好顺序访问粒度。
- 多个 NTT module 并行时，每次从 row-major memory 中取连续的 `t` 个元素，减少 effective bandwidth loss。

知识层迁移点:

- NTT 加速的关键不是只堆更多 butterfly units，而是同时解决 off-chip memory layout、on-chip buffering、field bit width 和 kernel decomposition。
- FIFO-based stride realization 是 custom accelerator route，与 GZKP 的 GPU shared-memory local reorder route 互补。

### MSM 子系统

PipeZK 的 MSM 子系统避免“复制很多 PMULT 单元”:

- PMULT 的 bit-serial PADD/PDBL 依赖 scalar bit pattern，直接复制会造成 sparse scalars 下的低利用率和 load imbalance。
- 论文采用 Pippenger algorithm，把 scalar 切成窗口，把 point 按窗口值放进 buckets。
- 当 vector length 远大于 bucket count 时，大量昂贵 PMULT 可转为 bucket 内 PADD 与少量 weighted accumulation。

硬件架构:

- 将大 MSM 拆成能放进片上 buffer 的 segments。
- 每个 cycle 从 on-chip buffer 读取 scalar/point pairs，根据当前 window bits 放入对应 bucket。
- bucket depth 很小，发生冲突时把待加的两个点与 bucket label 放入 centralized FIFO。
- 一个共享且深流水的 PADD module 从多个 FIFO 取任务，结果再按 label 写回 bucket 或继续进入结果 FIFO。
- 这样避免对 bucket 做物理排序，用轻量 buffer/FIFO 实现 group-by and accumulation。

并行和负载均衡:

- PipeZK 复制整个 PE，而不是让多个 PADD modules 抢同一组 FIFO。
- 每个 PE 处理 scalar 的不同 4-bit chunk，控制逻辑简单，PE 间依赖较少。
- 论文指出 worst-case bucket skew 与较均匀分布在 PADD 总数上差距有限；共享 PADD module 能降低 straggler 风险。
- 对 witness-derived sparse scalar `S`，0/1 cases 可在 fetch/filter 阶段单独处理；POLY output `H` 更接近 dense/uniform。

知识层迁移点:

- MSM 加速要同时考虑 algorithmic transform、bucket scheduling、scalar distribution 和 PADD resource sharing。
- 这与 GZKP 的 GPU MSM consolidation/load balancing 是同一问题域的不同硬件实现路线。

### 总体异构系统

PipeZK 不是全系统完全上芯:

- CPU 负责 witness expansion，并把数据传到 accelerator DDR。
- Accelerator 执行 POLY 阶段的 NTT/INTT 和 G1 MSM。
- G2 MSM 因资源代价高且占比相对低，被放在 host CPU。
- G1 accelerator work 与 CPU-side G2 work 可以并行。
- Accelerator 输出部分 bucket sums，剩余很小比例的 additions 由 CPU 完成。

这个边界非常重要: end-to-end speedup 不等于 POLY 或 MSM module 的最大 speedup。未加速的 witness generation、G2 MSM、PCIe/data loading 和 CPU residual work 会在模块加速后成为新瓶颈。

## 主要评估结论

评估设置:

- RTL/Verilog implementation，Synopsys Design Compiler，UMC 28 nm library。
- DDR4 2400 MHz memory model through Ramulator。
- 与 libsnark/bellman CPU、单 GPU/八 GPU baseline 比较；curve 包括 BN-128、BLS12-381、MNT4753。
- end-to-end prototype 与 libsnark 中的 trusted setup / witness generation 等 CPU module 结合。

结论要点:

- NTT module 在不同 size/bit-width 上相对 CPU 表现出最高约百倍级模块加速；MSM module 相对 CPU/GPU baseline 也有显著模块加速。
- ASIC 资源主要被 MSM 与 modular multiplication 消耗；bit width 越大，资源与功耗压力越明显。
- 标准 cryptographic workloads 上，论文报告 end-to-end 约 10x 量级 speedup；Zcash workloads 上约 3.5x-5.8x proof speedup，具体取决于 sprout/sapling workload。
- 未加速 G2 MSM 与 witness generation 在后期成为主要剩余瓶颈；论文把 G2 accelerator 和 witness generation optimization 留作 future work。

知识库使用边界:

- exact speedups 只能作为 PipeZK source-local benchmark，不应提升为永久的 SNARK accelerator 排名。
- 需要同时记录 process node、memory channels、baseline library/hardware、curve、field bit width、workload size、是否包含 G2/witness/data movement。
- PipeZK 是 ASIC/custom hardware 证据；GZKP 是 GPU 证据；二者应共同刷新 [[hardware-accelerated-proving|Hardware-accelerated proving]]，而不是互相替代。

## 与现有知识库的关系

| Knowledge node | 关系 | PipeZK 增量 | 边界 |
| --- | --- | --- | --- |
| [[hardware-accelerated-proving|Hardware-accelerated proving]] | primary | 新增 custom ASIC / pipelined architecture route: NTT FIFO pipeline、on-chip transpose、Pippenger MSM dispatch。 | 不上升为独立 PipeZK 概念节点。 |
| [[proof-system-benchmarking|Proof-system benchmarking]] | secondary | 增加 accelerator-aware benchmark evidence，特别是 module vs end-to-end speedup boundary。 | exact numbers 留在 source note。 |
| [[zk-snarks|zk-SNARKs]] | secondary | 证明 zkSNARK prover implementation 可通过 hardware backend 优化。 | 不改变 zk-SNARK 基础定义。 |
| [[proof-systems|Proof systems]] | parent | 强化 proof-system engineering 中 prover backend route。 | 不新增 proof-system foundation。 |
| [[hardware-accelerated-proving-to-proof-system-benchmarking|Hardware-accelerated proving -> Proof-system benchmarking]] | bridge | 补充 custom hardware / ASIC benchmark transfer boundary。 | benchmark discipline transfers; architecture details remain source-specific。 |

## 正反例约束

- 正确: 查询“ZKP prover 为什么慢”时，用 PipeZK 支撑 POLY/NTT 与 MSM 两大瓶颈。
- 正确: 查询“ASIC/FPGA/custom accelerator 怎么加速 SNARK prover”时，把 PipeZK 作为代表 source。
- 正确: 查询“PipeZK 和 GZKP 的区别”时，解释为 custom pipelined accelerator route 与 GPU backend route 的差异。
- 错误: 把 PipeZK 写成新的 zkSNARK protocol 或新的 proof-system foundation。
- 错误: 把论文的 28 nm / Zcash speedup 直接外推到当前生产 rollup prover 或任意 GPU/FPGA。
- 错误: 忽略 CPU-side G2 MSM / witness generation，直接用 module speedup 代表 end-to-end application speedup。

## 吸收交接

- Primary node to refresh: [[hardware-accelerated-proving|Hardware-accelerated proving]]
- Secondary nodes to refresh: [[proof-system-benchmarking|Proof-system benchmarking]], [[zk-snarks|zk-SNARKs]], [[proof-systems|Proof systems]]
- Bridge to refresh: [[hardware-accelerated-proving-to-proof-system-benchmarking|Hardware-accelerated proving -> Proof-system benchmarking]]
- Do not create: `PipeZK` standalone knowledge node, `proof-system-foundations` update, or legacy claim files.
- Follow-up queue: DIZK should later refresh [[distributed-proof-generation|Distributed proof generation]] and help contrast distributed scaling with PipeZK's per-machine hardware acceleration.

## Source-local open questions

| Question | Why it matters | Suggested follow-up |
| --- | --- | --- |
| No implementation repository analyzed. | RTL/design details and reproducibility cannot be validated from PDF alone. | `nahida-github-repo-analyze` only if repo/artifact is found. |
| G2 MSM remains on CPU. | End-to-end speedup is capped by CPU residual work. | Track future ASIC/MSM-G2 or modern GPU/FPGA sources. |
| Process node and baseline are 2021-era. | Current hardware may change trade-offs. | Use `nahida-daily-fetch` or targeted research before engineering decisions. |
| Side-channel/constant-time implementation evidence is not deeply analyzed. | Hardware accelerators can introduce timing or memory-pattern issues. | Add security-implementation sources if needed. |

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-pipezk-pipelined-architecture | Deep-read PDF and created source note for absorption into Source + Knowledge + Bridge architecture. | codex |
