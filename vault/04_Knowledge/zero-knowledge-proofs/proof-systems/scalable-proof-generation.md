---
id: "nahida-knowledge-scalable-proof-generation"
title: "Scalable proof generation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "scalable-proof-generation"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-distributed-proof-generation"
  - "nahida-knowledge-hardware-accelerated-proving"
  - "nahida-knowledge-proof-system-benchmarking"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "scalable-proof-generation"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/scalable-proof-generation"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
  - "zero-knowledge-proofs/proof-systems/hardware-accelerated-proving"
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
relation_edges:
  - from: "nahida-knowledge-scalable-proof-generation"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/scalable-proof-generation.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-scalable-proof-generation"
    relation: "organizes"
    to: "nahida-knowledge-memory-efficient-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
      - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-scalable-proof-generation"
    relation: "organizes"
    to: "nahida-knowledge-distributed-proof-generation"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
      - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-scalable-proof-generation"
    relation: "organizes"
    to: "nahida-knowledge-hardware-accelerated-proving"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/hardware-accelerated-proving.md"
      - "vault/05_Bridges/hardware-accelerated-proving-to-proof-system-benchmarking.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-scalable-proof-generation"
    relation: "depends_on"
    to: "nahida-knowledge-proof-system-benchmarking"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/proof-system-benchmarking.md"
      - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-scalable-proof-generation"
    relation: "uses"
    to: "nahida-knowledge-commit-and-prove-arguments"
    evidence_refs:
      - "vault/05_Bridges/commit-and-prove-arguments-to-scalable-proof-generation.md"
      - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-scalable-proof-generation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-scalable-proof-generation"
    relation: "bridges_to"
    to: "nahida-bridge-commit-and-prove-arguments-to-scalable-proof-generation"
    evidence_refs:
      - "vault/05_Bridges/commit-and-prove-arguments-to-scalable-proof-generation.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-scalable-proof-generation"
  - "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
  - "nahida-bridge-hardware-accelerated-proving-to-proof-system-benchmarking"
source_note_refs:
  - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
  - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
  - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
  - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
  - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols.md"
  - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
  - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
representative_source_refs:
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
  - "doi:10.1109/TC.2023.3235975"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "doi:10.1145/3576915.3616621"
  - "doi:10.1109/isca52012.2021.00040"
  - "doi:10.1145/3575693.3575711"
query_keys:
  - "Scalable proof generation"
  - "prover scalability"
  - "large-scale ZK proof generation"
  - "zk-SNARK prover scalability"
  - "circuit partitioning for proving"
  - "serializable ZK-SNARK"
  - "Yoimiya"
  - "proof generation pipeline"
  - "prover memory and CPU utilization"
aliases:
  - "prover scalability"
  - "scalable ZKP generation"
  - "large-scale proof generation"
domains:
  - "zero-knowledge-proofs"
topics:
  - "scalable-proof-generation"
  - "memory-efficient-snarks"
  - "distributed-proof-generation"
  - "hardware-accelerated-proving"
  - "proof-system-benchmarking"
  - "commit-and-prove-arguments"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-scalable-zkp-generation"
source_refs:
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
confidence: "medium"
trust_tier: "primary"
---

# Scalable proof generation

## 定义与范围

- 定义: Scalable proof generation 研究如何让 ZK/SNARK 证明生成在大规模计算上可运行、可调度、可复现评测。它关注 prover 端的 peak memory、proving time、setup/material loading、CPU/GPU/cluster utilization、partitioning、consistency binding、pipeline scheduling 和 benchmark boundary。
- 不包含: 单个系统名、单篇论文、某个固定硬件上的速度数字、通用 ZK foundation、或只优化 verifier/proof size 的 aggregation 问题。Yoimiya、Split、DIZK、PipeZK、GZKP、Gemini、Epistle 都是路线/来源，不是本节点本体。
- Canonical terms: `scalable proof generation`, `prover scalability`, `large-scale ZK proof generation`
- Aliases/query keys: Yoimiya, serializable ZK-SNARKs, circuit partitioning, proof-generation pipeline, prover memory, CPU utilization
- Standalone completeness check: 本节点本地说明问题、路线、代表来源、边界和缺口；具体算法、证明和实验数值留在 source notes。
- Retrieval role: 查询“ZK 证明生成怎么扩展”“prover 内存或 CPU 利用率怎么优化”“Split/DIZK/Ou/Yoimiya/GPU proving 属于什么关系”时先读本节点，再跳转到具体子节点。
- Update scope: 新 source 若改变 proof generation 的内存/时间/并行度/调度/一致性绑定/硬件/benchmark 结构，应刷新本节点。

## 背景

zk-SNARKs 和相关证明系统常把 verifier 端做得非常小，但 prover 端仍可能需要持有完整 witness、constraint system、proving key、多项式系数、FFT/MSM 中间态或硬件/集群资源。随着电路规模进入千万、亿级 constraints，问题不再是“有没有一个 succinct proof”，而是证明能否在给定内存、硬件、延迟和吞吐目标下生成出来。

当前 vault 已经有多个局部路线:

- [[memory-efficient-snarks|Memory-efficient SNARKs]]: 通过 streaming、elastic prover、folding、front-end partitioning 等方式降低单个 prover 的 peak memory。
- [[distributed-proof-generation|Distributed proof generation]]: 通过 Spark/cluster、多 worker、多参与者或 compiler-assisted statement partitioning 分摊 proving。
- [[hardware-accelerated-proving|Hardware-accelerated proving]]: 通过 GPU/ASIC/pipeline architecture 加速 NTT/MSM/PCS/prover loops。
- [[proof-system-benchmarking|Proof-system benchmarking]]: 规范化比较 runtime、memory、proof size、setup、hardware 和 source-local boundary。

本节点把这些局部路线提升为同一上层问题: proof generation 的可扩展性。它不是要合并所有子节点，而是给它们一个共同问题框架，避免每篇论文都被误当成孤立概念。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它横跨 Yoimiya/Split/Gemini/Epistle/DIZK/Ou/PipeZK/GZKP/Hekaton 等来源，持续回答同一个上层问题: prover 端如何扩展。
- 为什么不是单篇论文/单个系统的局部概念: Yoimiya 是强来源，但它只是一个自动 partition + polynomial binding + pipeline framework；scalable proof generation 还包括 streaming/elastic、cluster-distributed、compiler-assisted、hardware-accelerated 和 benchmark routes。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[zk-snarks|zk-SNARKs]], [[proof-system-benchmarking|Proof-system benchmarking]]。
- 不应拆出的实例/协议/来源: Yoimiya、CDG partition、Good Split、DIZK Spark RDD layout、PipeZK pipeline architecture、GZKP kernels 默认保留为 source-local 或子路线，不单独成基础概念。

## 解决的问题

Scalable proof generation 解决的是 prover-side scalability problem:

- 大电路导致 witness/constraint/proving-key/trace peak memory 超出单机容量。
- Prover time 由 witness generation、constraint synthesis、FFT、MSM、PCS opening、IO/loading 和 proof finalization 多阶段组成，单点优化不能保证端到端收益。
- CPU/GPU/cluster 资源可能利用不足，尤其当 witness generation 串行而 proof computation 可并行时。
- Circuit 或 statement partition 后必须保证 shared private values 一致，否则每个 subproof 局部正确但全局计算错误。
- 低内存、并行化、分布式、硬件加速和 proof aggregation 会改变不同指标，必须通过 benchmark boundary 统一描述。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of / problem_of | Yoimiya thesis and existing memory/distributed/hardware benchmark sources | active_seed |
| [[zk-snarks|zk-SNARKs]] | applies_to | Most current evidence is Groth16/Plonk/zk-SNARK prover engineering | active_seed |

## 下级结构

| Child/node | Kind | 为什么需要 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | problem / route family | 处理单机 peak memory、streaming、folding、elastic prover、front-end partitioning。 | Gemini, Epistle, Split, Yoimiya | active_seed |
| [[distributed-proof-generation|Distributed proof generation]] | method_family | 处理多机/多参与者/分布式或 compiler-assisted proving。 | DIZK, Pianist, Hekaton, Ou | active_seed |
| [[hardware-accelerated-proving|Hardware-accelerated proving]] | method_family | 处理 NTT/MSM/PCS/prover loop 的 GPU/ASIC/architecture 加速。 | GZKP, PipeZK | active_seed |
| [[proof-system-benchmarking|Proof-system benchmarking]] | evaluation_axis | 所有扩展路线都需要 memory/runtime/setup/hardware/source-local boundary。 | zk-Bench, DIZK, GZKP, PipeZK, Yoimiya | active_seed |
| consistency binding for partitioned proofs | route section / bridge | 切分后必须绑定共享 private values，避免局部 subproof 拼出错误全局计算。 | Yoimiya polynomial binding; Ou commit-and-prove backend; Hekaton memory checking | active_seed |

## 方法族与解决路线

| 路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Streaming / elastic proving | 把 prover 状态改成 stream/pass 模型，以更多 pass/time 换较低 working memory。 | Constraint/witness/PCS layer 支持 streaming 或重放。 | 可能增加 pass/time；trace generation 仍可能耗内存。 | [[memory-efficient-snarks|Memory-efficient SNARKs]], [[elastic-snarks|Elastic SNARKs]] |
| Front-end circuit partitioning | 把大电路切成 serial subcircuits，避免一次持有全部 witness/constraints。 | 电路依赖可被分析，跨切分 state 较小。 | 需要一致性绑定；proof/setup/verify 可能随分片增加。 | [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]], [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|Ye 2026]] |
| Consistency binding for subproofs | 用 hash、commitment、polynomial binding 或 memory checking 绑定 shared private values。 | Partitioned proofs share private inputs or intermediate variables. | Hash circuits may be expensive; polynomial binding leaks public evaluation handles and needs challenge discipline; CP backend requires compatible proof system. | [[commit-and-prove-arguments-to-scalable-proof-generation|CP -> scalable proof generation]] |
| Cluster/distributed proving | 把 QAP/FFT/MSM/PIOP/proof chunks 分摊到多机或多 worker。 | 有集群资源且 workload 可分解。 | Communication、worker trust、straggler、setup 和 aggregation 成本。 | [[distributed-proof-generation|Distributed proof generation]] |
| Compiler-assisted statement partitioning | 用前端语言/编译器寻找 cut、同步变量和 consistency checks。 | 应用可被特定 ZK language/IR 编译，backend 支持所需 consistency interface。 | Compiler semantic restrictions and partition solver complexity. | [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou/Lian]] |
| Hardware acceleration | 优化 NTT/MSM/PCS/prover loops 的 dataflow、parallelism 和 memory movement。 | Bottleneck 在可硬件并行的 proof-computation phase。 | Witness generation、G2/data movement、curve/field width 和 workload sparsity 可能仍是瓶颈。 | [[hardware-accelerated-proving|Hardware-accelerated proving]] |
| Proof-generation pipeline scheduling | 解耦 witness generation、proof computation、resource loading and task batches，用 pipeline 提高资源利用率。 | 多任务或 subcircuit DAG 可被调度，内存预算可控。 | 不一定降低单个 proof latency；并发可能增加 memory pressure。 | [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|Ye 2026]], [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] |
| Recursive/folding compression after partitioning | 对多个 subproof 或 serial proof tuple 做 verifier-cost compression。 | 多 subproof verification 成为瓶颈。 | 增加额外 prover step；不自动降低原始 witness/prover memory。 | Hekaton, Yoimiya future work, [[snark-proof-aggregation|SNARK proof aggregation]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|面向大规模计算的可扩展零知识证明生成方法]] | master thesis | 创建本问题节点；提出 CDG automatic serial partition、polynomial-binding serializable zk-SNARKs、Yoimiya partition/pipeline framework。 | Gnark/Groth16/Plonk-oriented；partition heuristic not globally optimal；serial verification overhead remains. | Ch.1-Ch.6 |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] | paper | hash-bound front-end partitioning route for single-machine prover memory. | Good Split search and hash-constraint overhead. | p1-p12 |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]] / [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] | papers | elastic/streaming R1CS and Plonkish low-memory route. | More passes/time; lookup and PCS boundary matter. | Gemini §2-§10; Epistle §4-§7 |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]] | paper | Spark-distributed Groth zkSNARK baseline for cluster proving. | 2018 Spark/EC2/Groth source-local benchmark. | p1-p19 |
| [[doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols|Ou/Lian]] | paper | compiler-assisted partitioning and CP consistency backend route. | Requires compatible ZK language/compiler and CP backend. | p1-p15 |
| [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP]] / [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] | papers | GPU/ASIC and pipelined hardware routes for proof-computation acceleration. | Hardware/process/workload-specific; not full prover-stack solution by itself. | GZKP §5; PipeZK §6 |

## 正反例约束

- 正确: 把 Ye 2026 / Yoimiya 作为 scalable proof generation 的来源，而不是把 `Yoimiya` 单独提升为基础概念。
- 正确: 把 proof-generation pipeline 与 hardware pipeline 区分；二者都改善 utilization，但层次不同。
- 正确: 把 exact benchmark numbers 留在 source note；本节点只保留指标框架和路线边界。
- 错误: 把所有低内存 SNARK 都叫 distributed proof generation。
- 错误: 只看 proof size/verifier time 就判断一个 proof system 可扩展。
- 错误: 把 polynomial binding 当作通用 commit-and-prove SNARK；它是 partitioned proof consistency-binding route 的一个实例。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，覆盖当前 vault 已吸收的 proof-generation scalability sources。
- Freshness: `fresh` for current-vault synthesis; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: 当前 vault 的 prover-scalability 地图已经不适合只靠 `memory-efficient-snarks` 和 `distributed-proof-generation` 两个并列节点表达。Ye 2026 显示一个完整 scalable proof-generation system 同时需要自动 partition、shared-variable consistency、backend-specific resource loading、pipeline scheduling 和 benchmark discipline。Split/Gemini/Epistle 提供单机低内存路线；DIZK/Pianist/Hekaton/Ou 提供 cluster/distributed/compiler路线；GZKP/PipeZK 提供 accelerator 路线；zk-Bench 与各 source-local experiments 提供评测边界。本节点把它们组织成上层问题，便于未来把新论文/仓库先路由到“prover 端如何扩展”再落到具体路线。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing|面向大规模计算的可扩展零知识证明生成方法]] | 创建 scalable proof generation 问题节点；补充 CDG automatic partition、polynomial binding consistency、Yoimiya pipeline/resource scheduling 和 source-local benchmark axes。 | 定义; 背景; 下级结构; 方法族; 当前综合; Bridge Links | yes | 后续吸收 Yoimiya arXiv/repo 或相关系统时复核 pipeline framework。 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[commit-and-prove-arguments-to-scalable-proof-generation|Commit-and-prove arguments -> scalable proof generation]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; zero-knowledge-proofs/proof-systems/scalable-proof-generation` | dependency, consistency_binding, method_transfer | CP-style hidden-value consistency transfers to partitioned proving; exact partition search, polynomial binding formula, scheduler, and backend loading remain source-specific. | active_seed |
| [[memory-efficient-snarks-to-distributed-proof-generation|Memory-efficient SNARKs -> Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/proof-systems/distributed-proof-generation` | contrast, shared_bottleneck, scalability_alternative | Both are routes under scalable proof generation, but single-prover memory and multi-worker proving have different trust/communication/memory metrics. | active_seed |
| [[hardware-accelerated-proving-to-proof-system-benchmarking|Hardware-accelerated proving -> Proof-system benchmarking]] | `zero-knowledge-proofs/proof-systems/hardware-accelerated-proving; zero-knowledge-proofs/proof-systems/proof-system-benchmarking` | evaluation_axis, hardware_sensitivity | Scalable proving claims require hardware/source-local benchmark boundaries. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-scalable-proof-generation | is_a | nahida-knowledge-proof-systems | this node; parent proof-systems node | high | active_seed |
| nahida-knowledge-scalable-proof-generation | organizes | nahida-knowledge-memory-efficient-snarks | Ye 2026; Split/Gemini/Epistle nodes | high | active_seed |
| nahida-knowledge-scalable-proof-generation | organizes | nahida-knowledge-distributed-proof-generation | Ye 2026 related work and pipeline boundary; DIZK/Ou nodes | high | active_seed |
| nahida-knowledge-scalable-proof-generation | organizes | nahida-knowledge-hardware-accelerated-proving | GZKP/PipeZK route | medium | active_seed |
| nahida-knowledge-scalable-proof-generation | depends_on | nahida-knowledge-proof-system-benchmarking | source-local metrics and benchmark boundary | high | active_seed |
| nahida-knowledge-scalable-proof-generation | uses | nahida-knowledge-commit-and-prove-arguments | consistency-binding bridge | medium | active_seed |
| nahida-knowledge-scalable-proof-generation | evidenced_by | vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md | full source note | high | active_seed |
| nahida-knowledge-scalable-proof-generation | bridges_to | nahida-bridge-commit-and-prove-arguments-to-scalable-proof-generation | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Yoimiya arXiv/repository not analyzed. | Thesis reports framework and mentions arXiv output, but the local source note does not inspect code architecture/current maintenance. | nahida-github-repo-analyze / nahida-research-search | medium | queued_if_repo_known |
| Automatic circuit partitioning primary comparisons thin. | CDG heuristic is one source; more compiler/circuit partitioning work would clarify taxonomy. | nahida-research-search / nahida-update | medium | watching |
| Verification compression for serial subproofs remains open. | Partitioned proving may increase verifier work/on-chain gas; recursion/folding route needs source-backed integration. | nahida-update / nahida-research-search | high | open_problem |
| Adaptive proof-generation scheduling evidence thin. | Current evidence is Yoimiya source-local; production prover schedulers and repo evidence could change best practices. | nahida-github-repo-analyze / nahida-daily-fetch | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-scalable-zkp-generation | Created scalable proof generation as a problem node above memory-efficient, distributed, hardware and benchmark routes; absorbed Ye 2026 thesis. | 1 source note | codex |
