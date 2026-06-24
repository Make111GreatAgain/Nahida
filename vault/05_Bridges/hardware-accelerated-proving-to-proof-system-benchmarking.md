---
id: "nahida-bridge-hardware-accelerated-proving-to-proof-system-benchmarking"
title: "Hardware-accelerated proving -> Proof-system benchmarking"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "hardware-accelerated-proving"
  - "proof-system-benchmarking"
endpoint_knowledge_refs:
  - "nahida-knowledge-hardware-accelerated-proving"
  - "nahida-knowledge-proof-system-benchmarking"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/hardware-accelerated-proving"
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
relation_types:
  - "evaluation_axis"
  - "benchmark_dependency"
  - "hardware_sensitivity"
  - "implementation_reuse"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
  - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
representative_source_refs:
  - "doi:10.1145/3575693.3575711"
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "doi:10.1109/isca52012.2021.00040"
query_keys:
  - "GPU prover benchmarking"
  - "accelerator-aware ZKP benchmark"
  - "hardware accelerated proving benchmark"
  - "GZKP benchmark"
  - "PipeZK benchmark"
aliases:
  - "accelerated prover benchmarking"
  - "GPU ZKP benchmarking"
domains:
  - "zero-knowledge-proofs"
topics:
  - "hardware-accelerated-proving"
  - "proof-system-benchmarking"
  - "gpu-proving"
  - "asic-proving"
tags:
  - "nahida/bridge"
created: "2026-06-21"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-gzkp-hardware-accelerated-proving"
  - "nahida-knowledge-20260622-pipezk-pipelined-architecture"
source_refs:
  - "doi:10.1145/3575693.3575711"
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "doi:10.1109/isca52012.2021.00040"
confidence: "high"
trust_tier: "primary"
---

# Hardware-accelerated proving -> Proof-system benchmarking

## 关系命题

Hardware-accelerated proving 的性能主张必须通过 proof-system benchmarking 的评测纪律来解释: GPU/FPGA/ASIC prover speedup 只有在硬件型号、process node、curve/field bit width、workload sparsity、memory budget、baseline boundary、measurement phase、module-vs-end-to-end boundary 和 CPU residual work 都明确时才可迁移。

这条 bridge 不表示某个 GPU prover benchmark 可替代通用 proof-system benchmark framework。它只说明 accelerator route 需要 benchmarking axis 才能避免把 source-local 数字误读成全领域排序。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[hardware-accelerated-proving|Hardware-accelerated proving]] | `zero-knowledge-proofs/proof-systems/hardware-accelerated-proving` | 用 GPU/FPGA/ASIC/multi-GPU/arithmetic backend 加速 prover-heavy stages，如 NTT/MSM/finite-field arithmetic | proof-system prover-side problem |
| [[proof-system-benchmarking|Proof-system benchmarking]] | `zero-knowledge-proofs/proof-systems/proof-system-benchmarking` | 用可复现指标比较 proof systems、libraries、hardware and runtime behavior | evaluation axis |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `evaluation_axis` | 硬件加速结果需要 benchmark 轴解释 | GZKP §5; zk-Bench benchmark taxonomy | active_seed |
| `benchmark_dependency` | speedup 依赖硬件、curve、workload、library 和 phase boundary | GZKP Tables 2-8; zk-Bench hardware sensitivity discussion | active_seed |
| `hardware_sensitivity` | CPU/GPU/FPGA/mobile/accelerator 覆盖差异改变结论 | zk-Bench limitations; GZKP V100/GTX1080Ti comparison | active_seed |
| `implementation_reuse` | arithmetic/NTT/MSM benchmark methods可帮助选择 accelerated backend | GZKP breakdown and ablations | active_seed |

## Transfer Matrix

| From hardware-accelerated proving | Transfers to benchmarking? | How | Boundary |
| --- | --- | --- | --- |
| Hardware configuration | yes | GPU model, ASIC process node, memory channels, memory size and runtime/toolchain become benchmark dimensions | does not predict future GPU generations or ASIC process nodes automatically |
| Curve and field bit width | yes | MNT4753/BLS12-381/ALT-BN128 affect finite-field and MSM costs | rankings can flip with library implementations |
| Workload sparsity | yes | sparse scalar vector changes MSM load balance and baseline comparisons | dense synthetic data alone is insufficient |
| Phase breakdown | yes | separate POLY/NTT, MSM, finite-field library and end-to-end metrics | phase boundaries differ across systems |
| CPU residual work | yes | witness generation, G2 MSM, data movement and residual additions can dominate after accelerator modules improve | module speedup does not equal proof/application speedup |
| Memory budget | yes | precomputation can trade memory for time | memory-rich acceleration is not low-memory SNARK evidence |
| Exact speedup number | no | useful only as source-local evidence | not a durable global ranking |

## Non-Transfer Boundary

- GZKP's V100/GTX1080Ti results do not automatically rank current A100/H100/consumer GPU/FPGA/ASIC prover stacks.
- A GPU prover benchmark does not prove protocol-level security, side-channel safety, constant-time behavior or implementation correctness.
- Benchmarking discipline transfers; GZKP's kernel design, preprocessed point layout and checkpoint parameters remain source-specific.
- zk-Bench gives a benchmarking framework seed but explicitly lacks GPU/FPGA/mobile evidence; GZKP fills one GPU source seed, not the full accelerator landscape.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP]] §5.1 | hardware, baseline, curve and workload setup | source-local ASPLOS 2023 setup |
| GZKP Tables 2-4 | end-to-end speedups on xJsnark and Zcash workloads | exact values depend on V100, curve and baselines |
| GZKP Tables 5-8 / Figures 8-10 | NTT/MSM breakdown and ablations | module metrics do not equal production end-to-end ranking |
| [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] §6 | 28 nm ASIC-style NTT/MSM module and Zcash workload evaluation | exact values depend on process node, baseline, curve, and CPU-side G2/witness coverage |
| [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench]] §5-§7 | benchmarking metric discipline and hardware sensitivity | excludes GPU/FPGA/mobile |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[hardware-accelerated-proving|Hardware-accelerated proving]] | Created node and added bridge | done |
| [[proof-system-benchmarking|Proof-system benchmarking]] | Add GZKP and PipeZK as accelerator-aware source-local benchmark evidence | done |
| [[proof-systems|Proof systems]] | Add hardware acceleration as child problem and source extension | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-hardware-accelerated-proving | requires_evaluation_axis | nahida-knowledge-proof-system-benchmarking | GZKP §5; zk-Bench benchmark axis | high | active_seed |
| nahida-knowledge-proof-system-benchmarking | evaluates | nahida-knowledge-hardware-accelerated-proving | GZKP hardware-specific benchmark evidence | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| GZKP repo/artifact found | Validate reproducibility, kernel boundaries and build assumptions | `nahida-github-repo-analyze` |
| FPGA/newer ASIC source absorbed | Split custom accelerator taxonomy if needed | `nahida-knowledge-get` |
| Current GPU prover benchmark absorbed | Update benchmark transfer boundaries and hardware generations | `nahida-daily-fetch` or `nahida-research-search` |
| Production rollup prover benchmark absorbed | Connect accelerator benchmarking to rollup prover economics only if source supports it | bridge or application node update |

## 更新记录

| Date | Run ID | Change | Sources |
| --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-gzkp-hardware-accelerated-proving | Created bridge from hardware-accelerated proving to proof-system benchmarking. | GZKP; zk-Bench |
| 2026-06-22 | nahida-knowledge-20260622-pipezk-pipelined-architecture | Added PipeZK as custom ASIC benchmark evidence and clarified module-vs-end-to-end boundaries. | PipeZK |
