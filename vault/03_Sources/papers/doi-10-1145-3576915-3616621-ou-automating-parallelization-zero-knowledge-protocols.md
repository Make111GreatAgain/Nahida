---
id: "doi-10-1145-3576915-3616621-ou-automating-parallelization-zero-knowledge-protocols"
title: "Ou: Automating the Parallelization of Zero-Knowledge Protocols"
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
  key: "doi:10.1145/3576915.3616621"
source_refs:
  - "doi:10.1145/3576915.3616621"
  - "iacr:2023/657"
  - "sha256:dd9b5b3e54f932d9bc55148ccf408969c23c081980e9ffe5358fe052ffefab5a"
representative_source_refs:
  - "doi:10.1145/3576915.3616621"
authors:
  - "Yuyang Sang"
  - "Ning Luo"
  - "Samuel Judson"
  - "Ben Chaimberg"
  - "Timos Antonopoulos"
  - "Xiao Wang"
  - "Ruzica Piskac"
  - "Zhong Shao"
venue: "ACM CCS 2023"
year: "2023"
doi: "10.1145/3576915.3616621"
arxiv_id: ""
eprint_id: "2023/657"
canonical_url: "https://doi.org/10.1145/3576915.3616621"
local_pdf: "~/Desktop/paper/3576915.3616621.pdf"
pdf_sha256: "dd9b5b3e54f932d9bc55148ccf408969c23c081980e9ffe5358fe052ffefab5a"
extracted_text_path: "vault/02_Raw/pdf/extracted/ou-automating-the-parallelization-of-zero-knowledge-protocols-dd9b5b3e54f9-pages.txt"
pages: 15
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
domains:
  - "zero-knowledge-proofs"
topics:
  - "distributed-proof-generation"
  - "compiler-assisted-zkp-parallelization"
  - "zkp-programming-languages"
  - "statement-partitioning"
  - "commit-and-prove-arguments"
  - "proof-system-benchmarking"
topic_ids:
  - "distributed-proof-generation"
  - "compiler-assisted-zkp-parallelization"
  - "commit-and-prove-arguments"
query_keys:
  - "Ou"
  - "Lian"
  - "automating ZKP parallelization"
  - "ZKP programming language"
  - "ZKP compiler"
  - "statement partitioning"
  - "compiler-assisted distributed proof generation"
  - "PBO ILP ZKP partitioning"
  - "shallow simulation"
  - "deep simulation"
  - "extended witnesses"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Abstract and Sections 1-2 identify Ou/Lian as a language/compiler framework for automatically partitioning ZK statements across a cluster."
  - "Section 1.2 states that arbitrary partitioning relies on commit-and-prove style consistency of committed inputs."
  - "Sections 4-6 define shallow simulation, live-variable/PBO-ILP partitioning, deep simulation, and distribution correctness."
  - "The paper does not introduce a new proof-system foundation; it is a proof-system engineering and compiler route for distributed proof generation."
parent_knowledge_refs:
  - "nahida-knowledge-distributed-proof-generation"
  - "nahida-knowledge-commit-and-prove-arguments"
  - "nahida-knowledge-proof-systems"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-distributed-proof-generation"
related_paths:
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/commit-and-prove-arguments.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
  - "vault/05_Bridges/commit-and-prove-arguments-to-distributed-proof-generation.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0095"
queue_rank: 95
path_update_status: "propagated"
run_ids:
  - "nahida-knowledge-20260623-ou-zkp-parallelization"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
  - "nahida/zkp"
---

# Ou: Automating the Parallelization of Zero-Knowledge Protocols

## Paper Identity

| Field | Value |
| --- | --- |
| Title | Ou: Automating the Parallelization of Zero-Knowledge Protocols |
| Authors | Yuyang Sang; Ning Luo; Samuel Judson; Ben Chaimberg; Timos Antonopoulos; Xiao Wang; Ruzica Piskac; Zhong Shao |
| Venue | ACM CCS 2023, Copenhagen, Denmark |
| Year | 2023 |
| DOI | 10.1145/3576915.3616621 |
| ePrint | 2023/657, listed by the paper as the online full version |
| Local PDF | `~/Desktop/paper/3576915.3616621.pdf` |
| Source key | `doi:10.1145/3576915.3616621`; `sha256:dd9b5b3e54f932d9bc55148ccf408969c23c081980e9ffe5358fe052ffefab5a` |
| Pages | 15 |
| Extracted text | `vault/02_Raw/pdf/extracted/ou-automating-the-parallelization-of-zero-knowledge-protocols-dd9b5b3e54f9-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Absorption run: `nahida-knowledge-20260623-ou-zkp-parallelization`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0095`
- Primary classification correction: 队列原先的 `proof-system-foundations` 过宽；本文主问题是 compiler-assisted distributed proof generation，应该进入 [[distributed-proof-generation|Distributed proof generation]]，并通过 [[commit-and-prove-arguments|Commit-and-prove arguments]] 桥接解释一致性绑定。
- PDF extractor: `pypdf`
- Coverage: p1-p15, including abstract, introduction, Lian overview, Ou syntax and typing, dynamic semantics, shallow simulation, statement partitioning, deep simulation, evaluation, references, and Appendix A example.
- Skipped material: 论文把部分证明细节放在 ePrint online full version 的 Appendices B-F；本轮未重新打开外部 ePrint，只吸收本地 PDF 中的定理陈述、证明角色和 main-text argument。
- Extraction gaps: 形式化规则和图表在文本中有少量排版噪声，但章节结构、算法目标、实验表格和关键结论可恢复。

## 一句话贡献

Ou/Lian 提供一个面向 ZKP 的 C-like 前端语言和编译框架：程序员写单个 proof statement，Lian 通过类型系统、浅模拟、live-variable analysis、PBO/ILP cut search 和深模拟，把 statement 自动切成可并行证明/验证的子语句，同时用 commit-and-prove 风格的 commitment consistency 维护跨分片状态一致性。

## 章节地图

| Section/Page | 内容 | 对知识库的作用 |
| --- | --- | --- |
| Abstract, §1 / p1-p3 | ZKP 开销、ZK 编程语言不足、多机 scale-out proving 需要手动 partition；提出 Ou/Lian。 | 证明主路径是 distributed proof generation + compiler tooling。 |
| §1.1 / p2 | 贡献列表: C-like language, OCaml compiler/static analysis, soundness proof, GD/MT speedups。 | source-local contribution anchor。 |
| §1.2 / p2-p3 | 技术挑战: commit-and-prove backend、ZK 中 intermediate values 可由 prover 本地预计算、randomized verification、atomic annotations。 | 形成 bridge to commit-and-prove。 |
| §2 / p4-p5 | Lian workflow: parse/typecheck -> shallow simulation -> partition -> deep simulation -> backend binaries。 | 方法路线总览。 |
| §3 / p5-p7 | Ou syntax, security lattice, typing rules, sandboxed functions, pointer/array restrictions, dynamic semantics。 | PL/typing details 留在 source note。 |
| §4 / p7-p9 | Shallow simulation and Theorem 1 refinement。 | 解释 compile-time unfolding/reordering 的行为保持。 |
| §5 / p9-p11 | Live variable analysis, dependency graph, efficient-cut search as PBO/ILP, distributed program generation。 | 可复用的 statement partitioning route。 |
| §6 / p11-p12 | Deep simulation and distribution correctness Theorems 5-6。 | 说明 extended witnesses 与 sync data 足以让分片执行等价。 |
| §7 / p12-p13 | Evaluation: compilation time, effective ratio, execution time; GD and Merkle Tree。 | source-local benchmark evidence。 |
| Appendix A / p14-p15 | Merkle Tree example: shallow simulation, dependency graph, two generated chunks, consistency check。 | 具体机制示例。 |

## 核心精读笔记

### 问题、动机与边界

本文处理的不是“如何发明新的 ZKP 协议”，而是“如何让程序员把复杂 ZK statement 写成普通程序，并让编译器自动找到可并行证明的切分”。作者指出两类瓶颈:

- 开发瓶颈: 许多 ZK 语言只支持 data-oblivious circuit model，程序员需要把 statement 写成单体电路或面向特定 protocol 的约束系统；这限制了 nondeterminism、randomized verification 等更自然或更高效的模型。
- 资源瓶颈: zkSNARK 等协议可能需要与 computation running time 线性相关的临时存储；VOLE-based ZKP 可减少 memory 但增加 bandwidth。已有 DIZK、zkBridge/deVirgo、EZEE、Giraffe 等 scale-out route 往往需要开发者手动修改协议或切分 computation。

明确不解决的问题: Lian 不证明用户程序的功能正确性、data-obliviousness，也不证明 witness finding hardness。它假设 Ou 程序本身对目标 ZK 应用是安全/合适的；若目标是 circuit-based protocol，则程序仍需 data-oblivious。证据锚点: §1.1 p2。

### Ou 语言与类型系统

Ou 是 C-like imperative language，支持变量声明、赋值、函数调用、条件、while、assert、return、break/continue、数组、struct、pointer 和 built-in functions。它的关键扩展不是语法复杂度，而是 security lattice:

- 信息维度: public `pub`、authenticated/committed private `pvt`、prover-local `plc`。
- knowledge level: `K0` compile time, `K1` distribution time, `K2` runtime。
- 组合形成 `pub0/pub1/pub2`, `pvt1/pvt2`, `plc1/plc2` 七类 label；`pvt0/plc0` 不存在，因为 compile-time secret 不应存在。

类型系统目标:

- 防止 private/prover-local 信息隐式流入 public，除非通过 explicit lowering operations such as `reveal`。
- 用 `K0/K1/K2` 保证 shallow simulation 和 deep simulation 分别只执行自己有足够知识的部分。
- `normal/atomic` functions 只允许 `pub0` branch；`box1/box2` 支持 public randomness 等更高 knowledge-level branch；`plocal1/plocal2` 只操作 prover-local data。
- pointer access restricted to `pub0`，因为 live-variable analysis 必须在浅模拟阶段知道指针指向哪些 memory locations。

这组设计让编译器可以安全地部分执行程序、展开循环/函数、保留未知计算，并为后续 partitioning 建 dependency graph。证据锚点: §2-§3, Figure 3, Figure 5。

### Lian 编译流水线

Lian 的 pipeline:

1. 用户写 Ou 程序。
2. Parser/typechecker 检查 security lattice and non-interference。
3. Shallow simulation 用 `K0` knowledge 展开程序，执行 normal functions、unroll loops、inline functions，并把未知 computation 留成 sequential program。
4. Atomic functions 和 `K2` blocks 作为不可切开的 cumulative instruction。
5. Live variable analysis 从 sequential program 中提取 dependency graph。
6. PBO/ILP 求解器找到 `kappa` 个 chunks 的 cut scheme。
7. 编译出每个 chunk 的 backend program/binary。
8. Prover 用 private inputs 执行 deep simulation，计算跨分片所需 extended witnesses 和 public values。
9. Prover/verifier pairs 并行执行各自 chunk，最后做 consistency check。

重要边界: Lian 把底层 commit-and-prove ZK protocol 当黑盒，不要求改后端 protocol。它需要后端能证明多个 shared committed inputs 上的 statements 并维护 consistency；Fiat-Shamir / random oracle 等内部细节不是 Lian 需要修改的对象。证据锚点: §1.2 p2-p3, §2 p4-p5。

### 为什么 ZK 中可以自动切分 sequential computation

普通 computation 中，`y = f(g(x1), x2)` 的 `f` 依赖 `g`，通常不能并行。ZK proving 中，prover 知道 private inputs，可以先本地算出 intermediate value `t = g(x1)`，然后把 `t` 作为 extended witness；两个子 statement 分别证明 `t = g(x1)` 和 `y = f(t, x2)`，最后检查跨子 statement 的 consistency。

这就是本文进入 [[distributed-proof-generation|Distributed proof generation]] 的核心原因: Lian 利用 prover precomputation 把数据依赖转化为 witness/commitment consistency，而不是传统并行程序中的 runtime dependency。证据锚点: §1.2 p3。

### Commit-and-prove 依赖

任意 partitioning 需要底层协议支持同一 witness 或 committed values 在多个 substatements 中一致使用。论文明确聚焦 commit-and-prove paradigm:

- prover 先 commit private inputs；
- 对已承诺值上的公共关系构造 proofs；
- 多个 substatements 可以引用同一 committed values；
- verifier 通过 commitment consistency 确信跨分片的值没有被 prover 任意更改。

因此本文不应只进入 distributed proving；还应建立 [[commit-and-prove-arguments|Commit-and-prove arguments]] 到 [[distributed-proof-generation|Distributed proof generation]] 的 bridge。这个 bridge 的迁移边界是: CP 提供 consistency binding 接口，但不自动给出 optimal partition、compiler type safety、randomized verification ordering 或 worker scheduling。证据锚点: §1.2 p2-p3, §2 p5。

### Shallow simulation

Shallow simulation 用 compile-time known `K0` values 尽可能执行程序:

- normal functions 被执行并输出 execution history；
- atomic functions 不展开，只输出一个 atomic command；
- sandboxed functions 因依赖 `K1/K2` knowledge，不执行，保留在 sequential program；
- `push/pop` pseudo-commands 标记 function calls and returns；
- unknown values 用 symbolic values 表示。

Theorem 1 是 shallow simulation 的 refinement statement: 若原程序动态执行从 `Omega1` 到 `Omega2`，那么对 `Omega1` 做 `R` refinement 后的 shallow simulation 会产生 history `h`，并且执行 `h` 在原 stack 上能得到同样行为。主证明在 online full version；本地 PDF 给出 theorem 和 intuition。证据锚点: §4 p7-p9。

### Statement partitioning

Partitioning 从 shallow simulation 输出的 sequential program `h = c1; ...; cn` 开始。

Live variable analysis:

- 反向扫描命令序列，维护 `LIVE(i)`，表示未来哪些 L-values 会被哪些命令读取。
- 生成 dependency graph `DG = (DV, DE)`，边 `(i,j)` 上的 `DEP(i,j)` 是 `cj` 会读、且可能由 `ci` 操作的 L-values。
- Theorem 4 说明 `DEP(-,j)` 足以安全执行 `cj`，并产生未来所需的 `DEP(j,-)`。

Efficient-cut search:

- 从 dependency graph 提取 cost graph `G = (V,E)`。
- Node cost `PC_i`: block 的 prover/verifier computation cost。
- Edge cost `C_ij`: 若 cut 经过该 edge，需要同步/验证的通信/一致性成本。
- `K2` dependent values 不可跨 chunk，所以相应 edge 设为不可切。
- 目标函数最小化: 被 cut edges 的 communication cost 总和 + 最重 chunk 的 computation cost。
- 编码为 ILP；因变量都是 Boolean，也可作为 PBO。论文 benchmark 使用 Gurobi PBO solver。

关键点: partitions 不要求在原 sequential order 中 contiguous。ZK prover 可通过 extended witnesses 处理非连续依赖，但会付出更多 consistency communication。证据锚点: §5.1-§5.2 p9-p11。

### Distributed program and deep simulation

给定 `chunk(i)`，Lian 为每个 chunk 生成一个 sequential program，插入 `sync` operations:

- `sync` 将其他 chunk 产生、当前 chunk 需要的 `K0/K1` dependent data 加入本地 stack。
- Deep simulation 用 `K0/K1` knowledge 具体计算这些 dependent values。
- Fact 1 保证跨 chunk dependency 不含 `K2` L-values，所以 deep simulation 足以提供跨 chunk data。
- 所有 chunk 独立运行 proof/verification 后，最后执行 consistency check，防止 prover 在不同 chunk 中给同一 extended witness 不一致值。

Theorem 5 给出 deep simulation refinement；Theorem 6 说明 deep simulation 提供的数据足以让分布式执行在每个 chunk 中与未切分执行对齐。证据锚点: §5.3-§6.3 p11-p12。

### Evaluation

指标:

- Compilation time: shallow simulation + dependency analysis + efficient-cut search，不含 deep simulation；论文称 deep simulation 在所有 example 中少于 compilation time 的 0.5%。
- Effective ratio: sequential execution cost / distributed objective cost；`kappa` chunks 时越接近 `kappa` 越好。
- Execution time: Ou compiled to VOLE-based EMP backend 后的 end-to-end runtime。

Benchmarks:

- Gradient descent (GD): logistic regression with 10 features。
- Merkle tree (MT): verify data integrity by recursively hashing blocks。

Partition quality:

- GD/MT 规模变大时，Lian 更容易找到接近 optimal 的 effective ratio。
- 在机器数继续增加但程序规模固定时，effective ratio 会达到上限；小程序配太多机器会让 effective ratio 远小于 `kappa`。

Atomic annotation:

- `atomic` 可显著缩小 graph/search space，编译时间下降约 1x-60x。
- 代价是可能排除一部分 feasible partitions，使 effective ratio 下降；但在 solver time limit 很紧时，也可能提高 effective ratio，因为搜索空间变小更容易找到好解。

End-to-end:

- GD 在 `kappa = 1,5,10,20,40` 时 runtime 约 `681.55s, 147.91s, 71.23s, 38.06s, 21.90s`，speedup 到 `31.12x`；estimated effective ratio 到 `39.8`。
- MT 在同样 `kappa` 下 runtime 约 `40.23s, 11.08s, 7.63s, 6.5s, 5.25s`，speedup 到 `7.66x`；estimated effective ratio 到 `38.63` 但实际受 backend constant setup time 影响。

证据锚点: §7 p12-p13, Table 1, Figures 9-12。

### Appendix A 机制示例

Appendix A 用 Merkle Tree 例子展示从 Ou 程序到分布式程序:

- `merkle` recursion 在 shallow simulation 中展开成 15 行 sequential program。
- `sha256_leaf` 和 `sha256_node` 被标记为 atomic；`load_block` 是 `plocal1`，浅模拟忽略，深模拟执行。
- Live-variable graph 发现 cut between line 5 and 6 时只需同步 `hash5`。
- Chunk 1 产生 `hash5` 的 digest，chunk 2 的 `sync_6` 从 prover 得到 `hash5` 并记录 input digest。
- 最终 consistency check 确认 chunk 2 使用的 `hash5` 确实是 chunk 1 产生的值。

这个例子清晰说明 Lian 的 reusable insight: cut search 应找“足以安全执行和一致性检查的最小依赖”，否则会出现 undefined behavior 或多同步无用数据。证据锚点: Appendix A p14-p15。

## 与现有知识库的关系

| Knowledge node | 关系 | Ou/Lian 增量 | 边界 |
| --- | --- | --- | --- |
| [[distributed-proof-generation|Distributed proof generation]] | primary | 新增 compiler-assisted statement partitioning route: 通过 Ou language + Lian compiler 自动切分 ZK statements，不要求开发者手动 partition。 | 不替代 DIZK/Pianist/Hekaton；它是 compiler/front-end route，不是 cluster FFT/MSM/proof aggregation route。 |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | bridge dependency | commit-and-prove 为任意 partition 的 shared committed inputs 和 consistency checking 提供后端接口。 | CP 不自动提供 type system、partition objective 或 randomized verification ordering。 |
| [[proof-systems|Proof systems]] | parent | 强化 proof-system engineering 中“编译器/语言支持”轴。 | 不新增 proof-system foundation。 |
| [[proof-system-benchmarking|Proof-system benchmarking]] | secondary | 提供 effective ratio、compilation time、end-to-end runtime 等 source-local metrics。 | 不构成通用 benchmark framework；exact results 留在 source note。 |

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `zero-knowledge-proofs` | title, abstract, CCS security venue, ZKP keywords | high | existing domain |
| Research background | ZKP proof generation overhead and lack of parallel-aware ZK language/compiler support | §1 p1-p2 | high | update parent/problem background |
| Research problem | compiler-assisted distributed proof generation / automatic ZK statement partitioning | abstract, §1.1-§1.2, §5 | high | source extension under distributed-proof-generation |
| Foundation concepts | zero-knowledge proofs, commit-and-prove arguments, non-interference/type systems, combinatorial optimization | §1.2-§5 | high | update CP bridge; PL concepts stay source-local unless repeated |
| Method family | shallow/deep simulation + live-variable analysis + PBO/ILP partitioning | §4-§6 | high | method route in existing node |
| Application/evaluation context | GD, Merkle Tree, Freivalds randomized matrix multiplication, VOLE-based EMP backend | Fig. 1, §7, Appendix A | medium | source-local benchmark/context |
| Artifact/source instance | Ou language and Lian compiler | title, abstract, §2 | high | source instance; do not create `Ou` knowledge node now |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `zero-knowledge-proofs/proof-systems/distributed-proof-generation`。
- 它帮助未来查询:
  - “ZKP 证明如何自动并行化?”
  - “Ou/Lian 与 DIZK/Pianist/Hekaton 的区别?”
  - “commit-and-prove 为什么支持 distributed ZKP statement partition?”
  - “ZKP 编译器里的 shallow simulation/deep simulation 是什么?”
- 应留在 source note 的内容: Ou 的完整 grammar/typing rules、symbolic semantics、theorem statements、GD/MT exact runtime、Appendix A generated code。
- 不创建的上层节点: `Ou`, `Lian`, `shallow simulation`, `deep simulation`, `atomic annotation`。这些目前是本文系统机制或方法细节；若后续多篇 ZKP compiler/source 反复出现，再考虑 `ZKP programming languages and compilers` 子节点。

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Distributed proof generation | reusable method family | 更新现有 [[distributed-proof-generation|Distributed proof generation]]。 | 新建 `Ou` 作为方法族。 | §1-§2, §5-§7 |
| Commit-and-prove arguments | foundation/method dependency | 更新 [[commit-and-prove-arguments|Commit-and-prove arguments]] 并建 bridge。 | 把 CP 当成 Ou 独有机制。 | §1.2 |
| Ou/Lian | source/system instance | source extension / representative source。 | 作为 foundation concept 单独提升。 | title, abstract |
| Shallow/deep simulation | source-local compiler techniques | 放在 source note 和 distributed-proving 方法路线中。 | 拆成独立 knowledge nodes。 | §4, §6 |
| PBO/ILP cut search | reusable technique but current source-local | 作为 route detail；后续多来源后再判断。 | 建成 ZKP foundation。 | §5.2 |

## 证据记录

| 结论/观察 | 类型 | 位置 | 置信度 | 备注 |
| --- | --- | --- | --- | --- |
| Ou/Lian 目标是让程序员不用手动考虑 distributed computation，由 compiler 自动 chunk ZK statement。 | author_claim | Abstract, §1.1 | high | 主贡献。 |
| 任意 partition 依赖 commit-and-prove paradigm 来保证 shared committed values 一致。 | author_claim | §1.2 | high | bridge evidence。 |
| ZK 中 prover 可本地预计算 intermediate values，因此 sequential dependency 可转为 extended witness consistency。 | mechanism | §1.2 | high | distributed proving route。 |
| Type system 用 security lattice + knowledge levels 支撑 non-interference and staged simulation。 | mechanism | §2-§3 | high | source-local PL details。 |
| Shallow simulation behavior-preserving；main proof details deferred to full version。 | theorem_statement | §4.2 | medium | theorem in local PDF; proof external。 |
| Partition objective balances max per-chunk computation and cut communication cost。 | algorithm | §5.2 | high | PBO/ILP route。 |
| Deep simulation computes cross-chunk K0/K1 data; K2 dependencies are uncuttable。 | mechanism | §5.3-§6 | high | distribution correctness boundary。 |
| Evaluation shows near-linear effective ratios for large GD/MT programs, but real MT runtime is limited by backend constant setup. | empirical | §7, Table 1 | high | source-local benchmark。 |

## 知识交接

- 待更新 Knowledge node:
  - [[distributed-proof-generation|Distributed proof generation]]: add compiler-assisted statement partitioning route, Ou source extension, query keys, source refs, relation edge。
  - [[commit-and-prove-arguments|Commit-and-prove arguments]]: add distributed statement partitioning as CP backend usage and source extension。
- 待新增 Bridge:
  - [[commit-and-prove-arguments-to-distributed-proof-generation|Commit-and-prove arguments -> Distributed proof generation]]
- 无需更新或仅索引:
  - [[hardware-accelerated-proving|Hardware-accelerated proving]]: Ou does not target hardware acceleration。
  - [[memory-efficient-snarks|Memory-efficient SNARKs]]: Ou may reduce per-machine statement size but does not primarily solve peak-memory proof-system design。
- Domain dynamics impact: `unchanged`; this is a narrow proof-system engineering route, not enough by itself to rewrite domain-level research dynamics。
- Review queue:
  - Future split candidate: `ZKP programming languages and compilers` if more sources beyond Ou/ZK-SecreC/Circom/Cairo/Noir enter the vault。
  - Foundation gap: Plonk/VOLE/EMP are mentioned but not defined by this paper; do not let Ou source define them。

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-ou-zkp-parallelization | Deep-read PDF and created source note for Source + Knowledge + Bridge absorption. | codex |
