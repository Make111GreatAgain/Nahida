---
id: "sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system"
title: "DIZK: A Distributed Zero Knowledge Proof System"
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
  type: "sha256"
  key: "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
source_refs:
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "filename:sec18-wu.pdf"
representative_source_refs:
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
authors:
  - "Howard Wu"
  - "Wenting Zheng"
  - "Alessandro Chiesa"
  - "Raluca Ada Popa"
  - "Ion Stoica"
venue: "27th USENIX Security Symposium"
year: "2018"
doi: ""
arxiv_id: ""
canonical_url: "https://www.usenix.org/conference/usenixsecurity18/presentation/wu"
local_pdf: "~/Desktop/paper/sec18-wu.pdf"
pdf_sha256: "2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
extracted_text_path: "vault/02_Raw/pdf/extracted/dizk-a-distributed-zero-knowledge-proof-system-2714176ef590-pages.txt"
pages: 19
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
domains:
  - "zero-knowledge-proofs"
topics:
  - "distributed-proof-generation"
  - "distributed-zksnark"
  - "cluster-proving"
  - "apache-spark"
  - "groth16"
  - "qap"
  - "r1cs"
  - "distributed-fft"
  - "distributed-msm"
  - "proof-system-benchmarking"
topic_ids:
  - "distributed-proof-generation"
  - "proof-system-benchmarking"
  - "zk-snarks"
query_keys:
  - "DIZK"
  - "Distributed Zero Knowledge"
  - "distributed zkSNARK"
  - "Spark zkSNARK"
  - "distributed Groth16"
  - "distributed FFT"
  - "distributed multi-scalar multiplication"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Title, abstract, and design overview identify DIZK as a distributed zkSNARK system."
  - "Sections 3-6 distribute Groth setup/prover components over Apache Spark rather than introducing a new proof-system foundation."
  - "Sections 10-11 provide source-local cluster benchmark evidence and applications."
  - "The paper is best absorbed under distributed proof generation, with secondary links to zk-SNARKs and proof-system benchmarking."
parent_knowledge_refs:
  - "nahida-knowledge-distributed-proof-generation"
  - "nahida-knowledge-proof-system-benchmarking"
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-proof-systems"
bridge_refs:
  - "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
related_paths:
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/proof-system-benchmarking.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
  - "vault/05_Bridges/distributed-proof-generation-to-snark-proof-aggregation.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0052"
queue_rank: 52
run_ids:
  - "nahida-knowledge-20260622-dizk-distributed-zkp"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# DIZK: A Distributed Zero Knowledge Proof System

## Paper Identity

| Field | Value |
| --- | --- |
| Title | DIZK: A Distributed Zero Knowledge Proof System |
| Authors | Howard Wu; Wenting Zheng; Alessandro Chiesa; Raluca Ada Popa; Ion Stoica |
| Venue | 27th USENIX Security Symposium |
| Year | 2018 |
| DOI | not shown in local PDF |
| Canonical URL | https://www.usenix.org/conference/usenixsecurity18/presentation/wu |
| Local PDF | `~/Desktop/paper/sec18-wu.pdf` |
| Source key | `sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75` |
| Pages | 19 |
| Extracted text | `vault/02_Raw/pdf/extracted/dizk-a-distributed-zero-knowledge-proof-system-2714176ef590-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Absorption run: `nahida-knowledge-20260622-dizk-distributed-zkp`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0052`
- Primary classification correction: queue 中的 `proof-system-foundations` 过宽；本论文主要进入 [[distributed-proof-generation|Distributed proof generation]]，并作为 [[proof-system-benchmarking|Proof-system benchmarking]] 与 [[zk-snarks|zk-SNARKs]] 的 source extension。
- Identity note: 本地 PDF 无 DOI/arXiv ID；以 PDF sha256 和 USENIX 页面作为 source identity。

## 一句话贡献

DIZK 把 Groth zkSNARK 的 setup 和 prover 从单机内存密集流程改造成 Apache Spark 上的分布式流程，通过分布式 FFT、Lagrange interpolant evaluation、fixed/variable-base MSM，以及针对 QAP instance/witness reduction 中 dense rows/columns 的混合 join 方案，将 zkSNARK 证明扩展到十亿级约束规模。

## 章节地图

| Section | 内容 | 对知识库的作用 |
| --- | --- | --- |
| Abstract, 1 | 说明单机 zkSNARK prover 的时间和内存瓶颈，提出 DIZK 支持 billions of gates。 | 支撑 distributed proof generation 的基础 source。 |
| 2 | 回顾 publicly-verifiable preprocessing zkSNARK、R1CS、QAP、Groth protocol、bilinear encodings。 | 说明 DIZK 不改变 verifier/proof 接口，而是分布式实现 Groth setup/prover。 |
| 3 | 设计总览: setup/prover 运行在 cluster，R1CS、pk、witness 存为 RDD，verifier 保持不变。 | 给出 cluster proving 的系统边界。 |
| 4 | 分布式 field/group arithmetic: FFT、Lag、fixed-base MSM、variable-base MSM。 | 提供可复用的 prover backend 分解。 |
| 5 | 分布式 zkSNARK setup: QAP instance reduction 中按列处理稀疏矩阵，并单独处理 dense columns。 | 说明 naive Spark join 的 straggler 问题和 DIZK 的修正。 |
| 6 | 分布式 zkSNARK prover: QAP witness reduction 中按行处理稀疏矩阵，并单独处理 dense rows。 | 说明 prover-side dense-row imbalance 及其复用 setup 阶段标注。 |
| 7 | 应用: edited photo authenticity 与 ML model integrity。 | 提供大电路应用示例，不把应用本身提升为 DIZK 的主分类。 |
| 8-9 | Java/Spark 实现、EC2 集群、BN curve 参数。 | 给出实现和 benchmark 边界。 |
| 10 | setup/prover/components 的可扩展性评估。 | 进入 proof-system benchmarking 的 source-local evidence。 |
| 11 | 应用 constraint/witness generation 评估。 | 说明 DIZK 应用层 witness/constraint generation 也需分布式生成。 |
| 12-14 | 相关工作、局限、结论。 | 记录 trusted setup、成本仍高、public-randomness SNARK 作为 future direction。 |

## 解决的问题

DIZK 解决的是 zkSNARK prover-side cluster scalability problem:

- 传统 zkSNARK verifier 很快、proof 很短，但 setup/prover 的时间和空间至少随被证明计算的规模增长。
- 论文指出当时 state-of-the-art 单机 zkSNARK 只能支持约 10-20 million gates，并且 prover cost 超过 1 ms per gate；这使 SHA-256、图像处理、ML integrity 等较大计算很难进入实际 SNARK。
- Groth zkSNARK 的重计算包括大规模 polynomial arithmetic、FFT、Lagrange evaluation、fixed/variable-base MSM、R1CS-to-QAP instance reduction 和 witness reduction。
- 这些任务在单机上依赖大内存；在 cluster 上则遇到分布式内存、shuffle、straggler、dense row/column skew 和大对象重排问题。

边界: DIZK 不提出新的 zkSNARK 安全模型或新的 verifier。它保留 Groth verifier 和 128B proof 这类接口目标，把 expensive setup/prover execution 分布式化。

## 核心方法

### 系统接口和数据布局

DIZK 的接口仍是 R1CS-based zkSNARK:

- setup 输入 R1CS instance `phi = (k, N, M, a, b, c)`，输出 proving key `pk` 和 verification key `vk`。
- prover 输入 `pk`、public input `x` 和 witness `w`，输出 constant-size proof `pi`。
- verification key 和 proof 很小，verifier 不需要分布式执行；大的 R1CS、proving key、witness 以 Spark RDD 存储和处理。
- 论文实现约 10K 行 Java over Apache Spark；R1CS 的三组矩阵 `a, b, c` 分别用 RDD 表示，每条记录是 `(j, (i, v))`。

这个结构的知识层意义是: DIZK 是 cluster backend route，而不是 protocol-instance child。它提供一个早期、清晰的证明: SNARK setup/prover 可以被拆成可分布式执行的 backend components。

### 分布式 field arithmetic

QAP instance/witness reduction 需要处理大量多项式。DIZK 对 field arithmetic 的分布式化包括:

- Distributed FFT: 采用类似 Sze 的 MapReduce-friendly 分解，把大小为 `n` 的 FFT 降成两批大小约 `sqrt(n)` 的 FFT，并只需要一次大 shuffle。这样比传统 Cooley-Tukey butterfly 每层全量 shuffle 更适合 compute cluster。
- Distributed Lag: 对 multiplicative subgroup domain，使用 Lagrange interpolants 的闭式形式，让每个 executor 处理一段 index space 来计算 `L_i(t)`。
- Polynomial multiplication/division 由这些 evaluation/interpolation primitives 支撑。

知识层迁移点: distributed prover 的瓶颈不是单个 FFT 算法是否并行，而是 memory access pattern 和 shuffle 次数是否适合 cluster。

### 分布式 group arithmetic

DIZK 把 Groth setup/prover 中的 group operations 抽成两类:

- `fixMSM`: setup 中对许多 scalars 做 fixed-base scalar multiplication。DIZK 让 driver 构建 lookup table 并广播给 executors，再由 executors 处理各自的 scalar chunk。
- `varMSM`: prover 中对 scalar vector 和 group element vector 做 variable-base multi-scalar multiplication。DIZK 使用 Pippenger algorithm 的思想，但实际分布式实现不是按 bucket 做全局 partition shuffle，而是把问题均匀切给 executors，各自运行 serial Pippenger 后再合并。

知识层迁移点: DIZK 与后来 GZKP/PipeZK 一样把 MSM 视为 prover backend 核心瓶颈，但它的解决路径是 cluster parallelism，而不是 GPU/ASIC。

### QAP instance reduction: dense columns

在 setup 阶段，R1CS 的矩阵 `a, b, c` 需要转为 QAP polynomial evaluations。矩阵总体稀疏，但并非每列都稀疏:

- sparse columns 可用普通 join/map/reduce 路径处理。
- dense columns 会让 hash partitioner 把同一列的数据集中到少数 executors，产生 stragglers 和 heap pressure。
- DIZK 先运行轻量分布式统计，识别超过阈值的 dense columns；论文启发式设置阈值为 `sqrt(M)`。
- 之后采用 hybrid computation: dense columns 单独 filter/join/evaluate，sparse columns 走普通路径，最后 union and reduce。

这个机制比 generic `blockjoin`/`skewjoin` 更贴合 QAP structure，因为它避免大规模 key rewrite、replication 和额外 shuffle。

### QAP witness reduction: dense rows

在 prover 阶段，计算 QAP witness 的 numerator evaluation 需要处理形如 `sum_i a_{i,j} z_i` 的任务。这里 straggler 的来源从 dense columns 变成 dense rows:

- 某些 variables 会参与很多 constraints，例如常数 `1` 经常出现在 Boolean negation 等约束中。
- naive join by row index 会把 dense rows 分给少数 executors。
- DIZK 使用与 setup 类似的 two-part solution: setup 时识别 dense rows，prover 时用 hybrid computation 分别处理 dense 和 sparse rows。

知识层迁移点: 分布式 proving 不只是把矩阵 entries 切块；必须理解 arithmetization 产生的稀疏结构和 skew pattern。

## 应用评估

论文把 DIZK 应用于两个方向:

- Photo authenticity: 基于 PhotoProof 的思路，证明 edited image 是由 signed original image 经过允许变换得到。论文实现 crop、rotation 和 blur，并支持较大图像，例如 2048 by 2048。
- ML model integrity: 在敏感数据不能公开的场景下，用 SNARK 证明公开模型由私有数据经公开训练/计算得到。论文实现 linear regression 和 covariance matrix calculation 的约束与 witness generation。

这些应用在知识库中的位置是 DIZK 的 source-local demonstration，不应直接生成独立的 application bridge，除非后续有更多 photo authenticity 或 ML integrity sources。

## 主要评估结论

评估设置:

- 单机实验使用 Amazon EC2 `r3.large`；分布式实验使用 `r3.8xlarge` 集群，十台机器最多 128 executors，二十台机器最多 256 executors。
- 实例化使用 256-bit Barreto-Naehrig curve，并为支持十亿级实例生成了 `p - 1` 可被足够大 `2^a` 整除的曲线参数，论文中取 `a = 50`。
- baseline 包括 libsnark 中 Groth protocol 和 PGHR protocol 的单机实现。

结论要点:

- DIZK 支持超过 1 billion constraints/gates 的 instances，而单机 libsnark Groth/PGHR 在约 10-20 million gate 量级受内存限制。
- 论文声称相对 prior art 支持 100x larger circuits，并达到约 10 microseconds per gate 的 prover cost，约 100x faster than prior art。
- 固定 executor 数量时，setup/prover running time 随 instance size 近似线性增长；固定 instance size 时，增加 executors 后 setup/prover running time 近似线性下降。
- DIZK 的定制 dense row/column 方案相对使用 generic skewjoin 的未优化版本，使可支持 instance size 提高约 10x，setup/prover 快约 2-4x。
- Application-level constraint/witness generation 也可以分布式化，但 witness generation 因 data shuffling 更贵。例如 700x700 matrix multiply 报告 685M constraints，64 executors 下 constraint generation 12s、witness generation 62s；2048x2048 image blur/crop/rotation 分别报告 13.6M、4.2M、138M constraints。

知识库使用边界:

- exact numbers 是 source-local benchmark，不应直接外推到当前 rollup prover、现代 GPU/ASIC 或其他 proof systems。
- benchmark 依赖 Spark、EC2 instance、curve choice、R1CS/QAP representation 和 Groth setup/prover。
- DIZK 的 proof/verifier 接口继承 Groth zkSNARK；trusted setup 成本也随 circuit size 增长，并且分布式 setup 更难保护 secret randomness。

## 与现有知识库的关系

| Knowledge node | 关系 | DIZK 增量 | 边界 |
| --- | --- | --- | --- |
| [[distributed-proof-generation|Distributed proof generation]] | primary | 新增 canonical early cluster-based distributed Groth zkSNARK route: Spark RDDs、distributed FFT/Lag/MSM、QAP dense row/column handling。 | 不新建 DIZK knowledge node；DIZK 是 source instance。 |
| [[proof-system-benchmarking|Proof-system benchmarking]] | secondary | 新增 cluster-distributed zkSNARK source-local benchmark evidence，补充分布式 setup/prover scaling 和 component benchmark。 | exact numbers 留在 source note。 |
| [[zk-snarks|zk-SNARKs]] | secondary | 证明 zkSNARK setup/prover backend 可在不改变 verifier/proof interface 的情况下多机执行。 | 不改变 zk-SNARK 基础定义。 |
| [[proof-systems|Proof systems]] | parent | 强化 proof-system engineering 中 prover resource scaling 路线。 | 不升级为 proof-system foundation。 |
| [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]] | bridge contrast | DIZK 是没有 Hekaton-style proof aggregation 的分布式 proving 路线，用于校准 “distributed proving 不等于 proof aggregation”。 | 不作为该 bridge 的正向 aggregation evidence。 |

## 正反例约束

- 正确: 查询 “DIZK 解决什么问题” 时，回答单机 Groth zkSNARK setup/prover 的 time/memory bottleneck，以及 Spark 分布式 backend 设计。
- 正确: 查询 “distributed proving 的早期路线” 时，把 DIZK 与 Pianist、Hekaton、deVirgo、Siniel、Split Prover 区分: DIZK 是 cluster/Spark Groth route。
- 正确: 查询 “DIZK 和 PipeZK/GZKP 的区别” 时，解释为多机 cluster scaling 与单机/硬件 backend acceleration 的差异。
- 错误: 把 DIZK 当成新的 SNARK protocol、foundation definition 或 proof aggregation 方案。
- 错误: 只引用 100x/10 microseconds per gate，而不记录硬件、Spark、curve 和 2018-era baseline 边界。
- 错误: 忽略 trusted setup；DIZK 分布式化 setup/prover，但 secret randomness ceremony/security 仍是局限。

## 吸收交接

- Primary node to refresh: [[distributed-proof-generation|Distributed proof generation]]
- Secondary nodes to refresh: [[proof-system-benchmarking|Proof-system benchmarking]], [[zk-snarks|zk-SNARKs]], [[proof-systems|Proof systems]]
- Bridge to refresh lightly: [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]] as contrast boundary only.
- Do not create: `DIZK` standalone knowledge node, `proof-system-foundations` update, `photo authenticity` bridge, or legacy claim files.
- Follow-up queue: analyze the DIZK code repository only if a repo/artifact is located; compare with aPlonk/deVirgo primary sources when they enter the vault.

## Source-local open questions

| Question | Why it matters | Suggested follow-up |
| --- | --- | --- |
| Released source code not analyzed. | The paper says code will be released, but this run only deep-read the PDF. | `nahida-github-repo-analyze` if a stable DIZK repository is provided or found. |
| Trusted setup ceremony remains difficult at cluster scale. | Distributed setup handles large keys but increases operational security burden for secret randomness. | Add trusted-setup / MPC ceremony sources before production guidance. |
| Spark and 2018 EC2 baseline may be stale. | Current prover engineering may use different frameworks, hardware and proof systems. | Use `nahida-daily-fetch` or targeted research before current engineering decisions. |
| Application coverage is illustrative. | PhotoProof/ML integrity examples are source-local and not complete application surveys. | Add dedicated application sources if these become query targets. |

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-dizk-distributed-zkp | Deep-read PDF and created source note for absorption into Source + Knowledge + Bridge architecture. | codex |
